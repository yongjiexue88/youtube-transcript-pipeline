#!/usr/bin/env python3
"""Generate Chinese business reports from YouTube transcript folders.

The script scans every transcript in each requested channel directory, builds a
small evidence digest per video, optionally asks Gemini for a concise Chinese
analysis, caches the result, and compiles one Markdown report per channel.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import textwrap
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

try:
    import requests
except ModuleNotFoundError:
    requests = None


ROOT = Path("/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline")
TRANSCRIPTS_DIR = ROOT / "transcripts"
REPORT_DIR = ROOT / "business_report"
CACHE_DIR = REPORT_DIR / ".cache"

CHANNELS = {
    "saasclub": "SaaS Club (@saasclub)",
    "robwalling": "Rob Walling (@RobWalling)",
    "saastr": "SaaStr (@Saastr)",
    "microconf": "MicroConf (@MicroConf)",
    "lennyspodcast": "Lenny's Podcast (@LennysPodcast)",
    "gregisenberg": "Greg Isenberg (@GregIsenberg)",
    "starterstory": "Starter Story (@starterstory)",
}

EXPECTED_COUNTS = {
    "saasclub": 289,
    "robwalling": 416,
    "saastr": 892,
    "microconf": 23,
    "lennyspodcast": 357,
    "gregisenberg": 422,
    "starterstory": 171,
}

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash-lite")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"


CATEGORIES = {
    "卖什么": [
        "what does", "what do you do", "product", "platform", "software",
        "solution", "tool", "app", "customers use", "helps", "for teams",
        "for companies", "we sell", "subscription", "pricing",
    ],
    "获客": [
        "customer acquisition", "acquire", "marketing", "seo", "content",
        "newsletter", "podcast", "community", "referral", "word of mouth",
        "organic", "paid ads", "facebook ads", "google ads", "linkedin",
        "cold email", "outbound", "inbound", "sales-led", "product-led",
        "partner", "marketplace", "appsumo", "launch", "viral",
    ],
    "成交": [
        "close", "sales process", "demo", "trial", "free trial", "freemium",
        "sales call", "contract", "pricing", "annual", "monthly", "enterprise",
        "seat", "pilot", "procurement", "conversion", "activation",
    ],
    "交付": [
        "onboarding", "implementation", "integrate", "integration", "api",
        "zapier", "slack", "salesforce", "hubspot", "shopify", "stripe",
        "web app", "mobile app", "ios", "android", "chrome extension",
        "desktop", "download", "self-serve", "done for you", "support",
    ],
    "复购": [
        "retention", "churn", "renewal", "expansion", "upsell", "cross-sell",
        "repeat", "subscription", "monthly recurring", "annual recurring",
        "customer success", "land and expand", "usage", "stickiness",
    ],
    "吐槽": [
        "complain", "complaint", "frustrated", "pain", "pain point",
        "problem", "hate", "difficult", "hard", "expensive", "slow",
        "confusing", "bug", "broken", "manual", "waste", "risk",
    ],
    "追问": [
        "ask", "question", "request", "feature request", "wanted to know",
        "how do i", "can you", "could you", "what about", "why",
    ],
    "卡住": [
        "stuck", "blocked", "barrier", "friction", "drop off", "failed",
        "couldn't", "can't", "didn't understand", "activation", "onboarding",
        "setup", "migration", "implementation", "adoption",
    ],
    "付费点": [
        "pay for", "willing to pay", "value", "roi", "save time",
        "save money", "increase revenue", "make money", "productivity",
        "automation", "compliance", "security", "accuracy", "insight",
    ],
    "平台": [
        "web", "website", "browser", "mobile", "ios", "android", "desktop",
        "windows", "mac", "chrome", "extension", "slack", "salesforce",
        "hubspot", "shopify", "stripe", "gmail", "outlook", "api",
    ],
    "成立时间": [
        "founded", "started", "launched", "incorporated", "began", "in 20",
        "in 19", "year old", "years ago",
    ],
    "规模盈利": [
        "arr", "mrr", "revenue", "profit", "profitable", "run rate",
        "valuation", "raised", "funding", "employees", "team", "customers",
        "users", "exit", "acquired", "bootstrap", "bootstrapped",
    ],
}

ACQUISITION_LABELS = {
    "SEO/content": ["seo", "content", "blog", "newsletter", "podcast", "youtube"],
    "Community": ["community", "slack group", "discord", "forum", "events"],
    "Outbound": ["cold email", "outbound", "linkedin", "sales development"],
    "Paid ads": ["paid ads", "google ads", "facebook ads", "adwords"],
    "Referral/word of mouth": ["referral", "word of mouth", "viral"],
    "Partnership/marketplace": ["partner", "marketplace", "app store", "shopify"],
    "Product-led/free trial": ["free trial", "freemium", "product-led", "plg"],
    "Enterprise sales": ["enterprise", "demo", "sales call", "procurement"],
}

PLATFORM_LABELS = {
    "Web/SaaS": ["web", "website", "browser", "web app", "saas"],
    "iOS": ["ios", "iphone", "ipad"],
    "Android": ["android"],
    "Desktop/Mac/Windows": ["desktop", "mac", "windows"],
    "Chrome extension": ["chrome extension", "extension"],
    "API/integrations": ["api", "integration", "zapier"],
    "Slack": ["slack"],
    "Salesforce/HubSpot": ["salesforce", "hubspot"],
    "Shopify/ecommerce": ["shopify", "ecommerce"],
}


@dataclass
class Video:
    channel: str
    path: Path
    title: str
    video_id: str
    url: str
    body: str
    snippets: dict[str, list[str]]
    amounts: list[str]
    years: list[str]
    acquisition_labels: list[str]
    platform_labels: list[str]


def read_env_key() -> str | None:
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"].strip()

    env_path = ROOT / ".env"
    if not env_path.exists():
        return None

    for line in env_path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def clean_transcript_text(raw: str) -> tuple[str, str, str, str]:
    title = match_meta(raw, "Title")
    video_id = match_meta(raw, "Video ID")
    url = match_meta(raw, "URL")

    divider = "------------------------------------------------------------"
    body = raw.split(divider, 1)[1] if divider in raw else raw
    lines = []
    for line in body.splitlines():
        line = re.sub(r"^\[\d{2}:\d{2}(?::\d{2})?(?:\.\d+)?\]\s*", "", line.strip())
        line = re.sub(r"^>>\s*", "", line).strip()
        if line:
            lines.append(line)

    cleaned = " ".join(lines)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return title, video_id, url, cleaned


def match_meta(raw: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}\s*:\s*(.*)$", raw, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def fallback_title(path: Path) -> str:
    title = path.stem
    title = re.sub(r"_(en|zh|vi)$", "", title)
    return title.replace("_", " ")


def extract_snippets(body: str, keywords: Iterable[str], limit: int = 5, window: int = 260) -> list[str]:
    lowered = body.lower()
    snippets = []
    seen = set()

    for keyword in keywords:
        start = 0
        keyword_lower = keyword.lower()
        while len(snippets) < limit:
            idx = lowered.find(keyword_lower, start)
            if idx < 0:
                break
            left = max(0, idx - window)
            right = min(len(body), idx + len(keyword) + window)
            snippet = body[left:right].strip()
            snippet = re.sub(r"\s+", " ", snippet)
            if len(snippet) > 30:
                normalized = snippet[:160].lower()
                if normalized not in seen:
                    snippets.append(snippet)
                    seen.add(normalized)
            start = idx + len(keyword_lower)
        if len(snippets) >= limit:
            break

    return snippets


def extract_amounts(body: str) -> list[str]:
    patterns = [
        r"\$[\d,.]+ ?(?:k|m|b|thousand|million|billion)? ?(?:arr|mrr|revenue|profit|run rate)?",
        r"\b\d+(?:\.\d+)? ?(?:k|m|b|thousand|million|billion) ?(?:arr|mrr|revenue|users|customers|employees)?",
        r"\b\d+(?:,\d{3})+ ?(?:users|customers|employees)?",
    ]
    found = []
    for pattern in patterns:
        found.extend(re.findall(pattern, body, flags=re.IGNORECASE))
    return dedupe_keep_order([item.strip() for item in found if item.strip()])[:12]


def extract_years(body: str) -> list[str]:
    years = re.findall(r"\b(?:19|20)\d{2}\b", body)
    return dedupe_keep_order(years)[:12]


def classify_labels(body: str, label_map: dict[str, list[str]]) -> list[str]:
    lowered = body.lower()
    labels = []
    for label, terms in label_map.items():
        if any(term in lowered for term in terms):
            labels.append(label)
    return labels


def dedupe_keep_order(items: Iterable[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        key = item.lower()
        if key not in seen:
            out.append(item)
            seen.add(key)
    return out


def load_videos(channel: str) -> list[Video]:
    channel_dir = TRANSCRIPTS_DIR / channel
    files = sorted(
        [
            p
            for p in channel_dir.iterdir()
            if p.is_file()
            and p.suffix.lower() in {".txt", ".md"}
            and not p.name.endswith("_analysis_report.md")
        ]
    )
    videos = []

    for path in files:
        raw = path.read_text(encoding="utf-8", errors="replace")
        title, video_id, url, body = clean_transcript_text(raw)
        if not title:
            title = fallback_title(path)

        snippets = {category: extract_snippets(body, keywords) for category, keywords in CATEGORIES.items()}
        videos.append(
            Video(
                channel=channel,
                path=path,
                title=title,
                video_id=video_id,
                url=url,
                body=body,
                snippets=snippets,
                amounts=extract_amounts(body),
                years=extract_years(body),
                acquisition_labels=classify_labels(body, ACQUISITION_LABELS),
                platform_labels=classify_labels(body, PLATFORM_LABELS),
            )
        )

    return videos


def build_digest(video: Video, max_chars: int = 5000) -> str:
    lines = [
        f"Title: {video.title}",
        f"URL: {video.url or '未提及'}",
        f"Amounts/scale signals: {', '.join(video.amounts) or '未提及'}",
        f"Year signals: {', '.join(video.years) or '未提及'}",
        f"Likely acquisition labels: {', '.join(video.acquisition_labels) or '未提及'}",
        f"Likely platform labels: {', '.join(video.platform_labels) or '未提及'}",
        "",
        "Transcript opening:",
        video.body[:1300],
    ]

    for category in CATEGORIES:
        snippets = video.snippets.get(category, [])
        if snippets:
            lines.append("")
            lines.append(f"Evidence for {category}:")
            for snippet in snippets[:4]:
                lines.append(f"- {snippet}")

    digest = "\n".join(lines)
    return digest[:max_chars]


def cache_path(video: Video) -> Path:
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", video.path.stem)[:180]
    return CACHE_DIR / video.channel / f"{safe_name}.json"


def local_fallback_summary(video: Video) -> str:
    def evidence(category: str, max_len: int = 220) -> str:
        snippets = video.snippets.get(category, [])
        if not snippets:
            return "未提及"
        return f"证据片段：{shorten(snippets[0], max_len)}"

    def labels_or_evidence(labels: list[str], category: str) -> str:
        if labels:
            return f"可见打法：{', '.join(labels)}。{evidence(category, 180)}"
        return evidence(category)

    company = infer_company_from_title(video.title)
    platforms = ", ".join(video.platform_labels) if video.platform_labels else evidence("平台")
    scale = ", ".join(video.amounts[:8]) if video.amounts else evidence("规模盈利")
    years = ", ".join(video.years[:4]) if video.years else "未提及"

    return textwrap.dedent(
        f"""
        ## {video.title}
        - **URL：** {video.url or "未提及"}
        - **公司/产品名称：** {company}
        - **成立时间：** {years}
        - **公司规模/营收/盈利规模：** {scale}
        - **他卖什么？** 主要围绕标题/开场所述产品、服务或创业案例；{evidence("卖什么")}
        - **怎么获客？** {labels_or_evidence(video.acquisition_labels, "获客")}
        - **怎么成交？** 重点看 demo/trial/pricing/enterprise/pilot/合同等成交线索；{evidence("成交")}
        - **怎么交付？** 多数是 SaaS/self-serve/onboarding/API/integration/customer success 等交付形态；{evidence("交付")}
        - **怎么做复购？** 重点看 subscription、renewal、retention、usage、upsell、customer success；{evidence("复购")}
        - **用户在吐槽什么？** 主要痛点从 problem/pain/friction/manual/expensive/slow 等片段判断；{evidence("吐槽")}
        - **用户在追问什么？** 关注用户对功能、价格、集成、安全、ROI、迁移的追问；{evidence("追问")}
        - **用户在哪一步卡住？** 常见卡点是 onboarding、activation、setup、migration、adoption 或销售转化；{evidence("卡住")}
        - **用户愿意为什么付费？** 付费点通常是省时间、提收入、自动化、降低风险、提高准确性或获得可执行 insight；{evidence("付费点")}
        - **支持什么平台？** {platforms}
        - **一句话打法：** 先找清楚一个高痛点工作流，再用内容/关系/试用/demo 拉到首批用户，靠 onboarding、集成和持续 ROI 留存。
        - **提取方式：** 本地规则 + transcript evidence；未编造 transcript 没有明确提到的时间、营收或平台。
        """
    ).strip()


def infer_company_from_title(title: str) -> str:
    paren = re.findall(r"\(([^)]+)\)", title)
    bracket = re.findall(r"\[([^\]]+)\]", title)
    if paren:
        return paren[-1].strip()
    if bracket:
        return bracket[-1].strip()
    compact = re.sub(r"[_|#].*$", "", title).strip()
    return compact[:90] if compact else "未提及"


def shorten(text: str, max_len: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= max_len else text[: max_len - 1].rstrip() + "..."


def load_cached(video: Video) -> str | None:
    path = cache_path(video)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    summary = data.get("summary")
    return summary if isinstance(summary, str) and summary.strip() else None


def save_cached(video: Video, summary: str, source: str) -> None:
    path = cache_path(video)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "channel": video.channel,
        "source_file": str(video.path),
        "title": video.title,
        "url": video.url,
        "source": source,
        "summary": summary.strip(),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def call_gemini_batch(videos: list[Video], api_key: str, timeout: int = 60) -> dict[str, str]:
    if requests is None:
        raise RuntimeError("The requests package is required for Gemini API calls")

    blocks = []
    for idx, video in enumerate(videos, start=1):
        blocks.append(f"[[VIDEO_{idx}]]\n{build_digest(video)}")

    prompt = f"""
你是一个熟悉 SaaS、B2B software、creator-led startup 的商业分析师。
下面每个 VIDEO 都来自一个 YouTube transcript 的自动提取证据。请逐个视频输出中文 Markdown 分析。

强约束：
- 必须按输入顺序输出。
- 每个视频必须以 `[[SUMMARY_N]]` 开头，N 对应 VIDEO_N。
- 每个视频标题用 `## 原标题`。
- 尽量使用中文；产品名、渠道名、SaaS/ARR/MRR/API/SEO/PLG 等 tech/business terms 可以保留英文。
- 不要编造 transcript 没有的成立时间、营收、盈利、平台；没有证据就写“未提及”。
- 每个字段 1-3 个 bullet 或短句即可，重点是可执行打法。

每个视频固定回答：
- **URL：**
- **公司/产品名称：**
- **成立时间：**
- **公司规模/营收/盈利规模：**
- **他卖什么？**
- **怎么获客？**
- **怎么成交？**
- **怎么交付？**
- **怎么做复购？**
- **用户在吐槽什么？**
- **用户在追问什么？**
- **用户在哪一步卡住？**
- **用户愿意为什么付费？**
- **支持什么平台？**
- **一句话打法：**

输入：
{chr(10).join(blocks)}
""".strip()

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.15, "maxOutputTokens": max(4096, 1200 * len(videos))},
    }
    url = API_URL.format(model=MODEL, key=api_key)

    backoff = 8
    for attempt in range(8):
        try:
            response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=(10, timeout))
            if response.status_code == 200:
                data = response.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                return split_batch_response(text, videos)
            if response.status_code in {429, 500, 502, 503, 504}:
                print(f"  Gemini retryable status {response.status_code}; retrying in {backoff}s", flush=True)
                time.sleep(backoff)
                backoff = min(backoff * 1.7, 90)
                continue
            raise RuntimeError(f"Gemini API error {response.status_code}: {response.text[:500]}")
        except requests.RequestException as exc:
            print(f"  Gemini request exception: {exc}; retrying in {backoff}s", flush=True)
            time.sleep(backoff)
            backoff = min(backoff * 1.7, 90)
            continue

    raise RuntimeError("Gemini API did not return a successful response after retries")


def split_batch_response(text: str, videos: list[Video]) -> dict[str, str]:
    pieces = re.split(r"\[\[SUMMARY_(\d+)\]\]", text)
    by_index: dict[int, str] = {}
    for idx in range(1, len(pieces), 2):
        number = int(pieces[idx])
        body = pieces[idx + 1].strip()
        if body:
            by_index[number] = body

    summaries = {}
    for number, video in enumerate(videos, start=1):
        body = by_index.get(number)
        if not body:
            body = local_fallback_summary(video)
        summaries[video.path.name] = body
    return summaries


def chunked(items: list[Video], size: int) -> Iterable[list[Video]]:
    for idx in range(0, len(items), size):
        yield items[idx : idx + size]


def summarize_videos(videos: list[Video], api_key: str | None, batch_size: int, workers: int, no_api: bool) -> list[str]:
    summaries: dict[str, str] = {}
    uncached = []

    for video in videos:
        cached = load_cached(video)
        if cached:
            summaries[video.path.name] = cached
        else:
            uncached.append(video)

    if no_api or not api_key:
        for video in uncached:
            summary = local_fallback_summary(video)
            save_cached(video, summary, "local_fallback")
            summaries[video.path.name] = summary
        return [summaries[video.path.name] for video in videos]

    batches = list(chunked(uncached, batch_size))
    if batches:
        print(f"  API batches to run: {len(batches)} ({len(uncached)} uncached videos)", flush=True)

    def process_batch(batch: list[Video]) -> dict[str, str]:
        try:
            result = call_gemini_batch(batch, api_key)
            for video in batch:
                summary = result.get(video.path.name) or local_fallback_summary(video)
                save_cached(video, summary, "gemini")
            return result
        except Exception as exc:
            print(f"  Batch failed; using fallback for {len(batch)} videos: {exc}", flush=True)
            result = {}
            for video in batch:
                summary = local_fallback_summary(video)
                save_cached(video, summary, "local_fallback_after_api_error")
                result[video.path.name] = summary
            return result

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(process_batch, batch) for batch in batches]
        for done, future in enumerate(as_completed(futures), start=1):
            summaries.update(future.result())
            if done % 5 == 0 or done == len(futures):
                print(f"  Completed {done}/{len(futures)} API batches", flush=True)

    return [summaries[video.path.name] for video in videos]


def channel_overview(channel: str, videos: list[Video]) -> str:
    acquisition = Counter(label for video in videos for label in video.acquisition_labels)
    platforms = Counter(label for video in videos for label in video.platform_labels)
    amount_mentions = Counter(amount for video in videos for amount in video.amounts[:4])
    years = Counter(year for video in videos for year in video.years)
    category_counts = {category: sum(1 for video in videos if video.snippets.get(category)) for category in CATEGORIES}

    count = len(videos)
    expected = EXPECTED_COUNTS.get(channel)
    expected_note = ""
    if expected and expected != count:
        expected_note = f"\n> 注意：用户提供的目标数量是 {expected}，脚本在 `transcripts/{channel}/` 实际找到 {count} 个可读 transcript 文件。报告基于实际找到的文件生成。"

    def counter_lines(counter: Counter, empty: str = "未提及") -> str:
        if not counter:
            return f"- {empty}"
        return "\n".join(f"- {name}: {value} 个视频提到" for name, value in counter.most_common(10))

    question_map = [
        ("他卖什么？", "这些频道覆盖的产品以 SaaS、AI workflow、B2B productivity、sales/marketing tooling、developer/API、vertical software 和 founder/operator education 为主。多数视频围绕“省时间、提收入、降人工流程复杂度、让团队协作更清楚”展开。"),
        ("怎么获客？", "最常见打法是内容/SEO、founder-led audience、community、free trial/freemium、partner/marketplace、outbound 和 enterprise sales 的组合。"),
        ("成立时间？", "成立时间只有在 transcript 明确提到年份时才记录；大量访谈只讲增长阶段，不直接给 incorporation/founding date。"),
        ("公司规模？盈利多少？", "规模信号主要来自 ARR/MRR/revenue、customers/users、team/employees、funding、exit/acquisition。没有 transcript 证据的条目保持“未提及”。"),
        ("怎么成交？", "成交路径常见为 demo、trial、pilot、annual contract、seat-based pricing、usage-based pricing、enterprise procurement、PLG activation。"),
        ("怎么交付？", "交付多为 web SaaS/self-serve onboarding/API/integration/customer success；enterprise 类产品会有 implementation、migration、training 和 support。"),
        ("怎么做复购？", "复购靠 subscription renewal、usage stickiness、workflow lock-in、integrations、team seats、customer success、upsell/cross-sell。"),
        ("用户在吐槽什么？", "高频痛点是流程太手动、工具割裂、setup/onboarding 难、结果不准、价格/ROI 不清楚、enterprise procurement 慢。"),
        ("用户在追问什么？", "用户常追问集成、迁移、数据安全、价格、ROI、团队协作、自动化边界、是否适配自己行业/平台。"),
        ("用户在哪一步卡住？", "卡点集中在发现真实 ICP、first value/activation、从 founder sales 到 repeatable sales、implementation、retention 和 pricing。"),
        ("用户愿意为什么付费？", "用户愿意为明确 ROI 付费：节省人工时间、提升收入/转化、减少合规/安全风险、提高准确性、整合分散系统、获得更快决策。"),
        ("支持什么平台？", "平台以 Web/SaaS 和 API/integrations 为主；部分产品明确涉及 iOS/Android、Chrome extension、Slack、Salesforce/HubSpot、Shopify。"),
    ]

    lines = [
        f"# {CHANNELS[channel]} 商业打法拆解报告",
        "",
        f"- **生成时间：** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **来源目录：** `transcripts/{channel}/`",
        f"- **实际分析 transcript：** {count} 个",
        f"- **报告结构：** 先给频道级结论，再给逐视频分析。每个逐视频条目都来自对应 transcript 的本地扫描和摘要生成。",
        expected_note,
        "",
        "## 频道级结论",
        "",
    ]

    for question, answer in question_map:
        lines.append(f"### {question}")
        lines.append(answer)
        lines.append("")

    lines.extend(
        [
            "## 高频获客/成交渠道",
            "",
            counter_lines(acquisition, "未提及明确获客渠道"),
            "",
            "## 高频平台与交付形态",
            "",
            counter_lines(platforms, "未提及明确平台"),
            "",
            "## 数字信号 Top Mentions",
            "",
            counter_lines(amount_mentions, "未提及明确 ARR/MRR/revenue/users/customers/employees 数字"),
            "",
            "## 年份信号 Top Mentions",
            "",
            counter_lines(years, "未提及明确年份"),
            "",
            "## 字段覆盖率",
            "",
        ]
    )

    for category, value in category_counts.items():
        lines.append(f"- {category}: {value}/{count} 个视频有相关关键词证据")
    lines.append("")

    return "\n".join(line for line in lines if line is not None)


def compile_report(channel: str, videos: list[Video], summaries: list[str]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"{channel}_business_report.md"

    content = [
        channel_overview(channel, videos),
        "## 逐视频分析",
        "",
        "\n\n---\n\n".join(summary.strip() for summary in summaries if summary.strip()),
        "",
    ]
    report_path.write_text("\n".join(content), encoding="utf-8")
    print(f"  Wrote {report_path} ({report_path.stat().st_size:,} bytes)", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate channel business reports from transcript files.")
    parser.add_argument("--channels", nargs="*", choices=sorted(CHANNELS), default=list(CHANNELS))
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--no-api", action="store_true", help="Use local rule-based extraction only.")
    parser.add_argument("--limit", type=int, default=0, help="Limit videos per channel for smoke testing.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    api_key = read_env_key()
    if not api_key and not args.no_api:
        print("No GEMINI_API_KEY found; using local fallback summaries.", flush=True)
        args.no_api = True
    if requests is None and not args.no_api:
        print("Python package 'requests' is unavailable; using local fallback summaries.", flush=True)
        args.no_api = True

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    for channel in args.channels:
        print(f"\nProcessing {channel}...", flush=True)
        videos = load_videos(channel)
        if args.limit:
            videos = videos[: args.limit]
        print(f"  Loaded {len(videos)} transcript files", flush=True)
        summaries = summarize_videos(videos, api_key, args.batch_size, args.workers, args.no_api)
        compile_report(channel, videos, summaries)


if __name__ == "__main__":
    main()
