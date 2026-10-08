import os
import re
import json
import requests
import time
import yaml

base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/mikelaoli"
api_key = os.environ.get("GEMINI_API_KEY", "")

if not api_key:
    env_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/.env"
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    if k.strip() == "GEMINI_API_KEY":
                        api_key = v.strip().strip("\"").strip("\'")

print(f"API Key found: {bool(api_key)}")

files = [f for f in os.listdir(base_dir) if f.endswith(".txt")]
files.sort()

candidates_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/books/mikelaoli/candidates"
os.makedirs(candidates_dir, exist_ok=True)

# Initialize output files (write markdown headers)
headers = {
    "frameworks": "# Framework Candidates\n\n",
    "principles": "# Principle Candidates\n\n",
    "cases": "# Case Candidates\n\n",
    "counter_examples": "# Counter-Example Candidates\n\n",
    "glossary": "# Glossary Candidates\n\n"
}

for name, header in headers.items():
    path = os.path.join(candidates_dir, f"{name}.md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(header)

def run_extraction(filename, content):
    prompt = f"""You are the Cangjie Unified Extractor. Analyze this transcript content from ex-Amazon L8 Director Mike Laoli's video.
Your task is to identify and extract the following 5 categories:

1. 思维模型/决策框架 (Frameworks): 可迁移的思考结构、面对决策时的结构化流程、推理方法。
2. 原则/清单/规则 (Principles): 具体的行为准则、行动指南、避坑清单。
3. 实例 (Cases): 说话者在职场中亲自采用并取得成果的案例。
4. 反例/警告/失败模式 (Counter-Examples): 说话者警告的职场失败场景、中式礼貌陷阱、无效做法等。
5. 关键术语 (Glossary): 说话者自己定义并赋予特定含义的专业术语。

For each category, extract as many items as possible. Every item MUST have:
- title (or term for glossary): 标题或术语 (简明中文)
- source_quote: 必须是文中能直接印证该条目的核心原文引句 (原句，限制在150字以内)
- summary (or definition for glossary): 该条目的详细解析或定义 (中文)
- tags: 2-3个相关标签

Output ONLY a JSON block, no other text:
{{
  "frameworks": [
    {{ "title": "...", "source_quote": "...", "summary": "...", "tags": ["tag1", "tag2"] }}
  ],
  "principles": [
    {{ "title": "...", "source_quote": "...", "summary": "...", "tags": ["tag1", "tag2"] }}
  ],
  "cases": [
    {{ "title": "...", "source_quote": "...", "summary": "...", "tags": ["tag1", "tag2"] }}
  ],
  "counter_examples": [
    {{ "title": "...", "source_quote": "...", "summary": "...", "tags": ["tag1", "tag2"] }}
  ],
  "glossary": [
    {{ "term": "...", "definition": "...", "source_quote": "...", "tags": ["tag1"] }}
  ]
}}

Transcript content from video:
{content}
"""
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=45)
            res_json = response.json()
            if "candidates" in res_json:
                text = res_json["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(text)
            elif "error" in res_json and res_json["error"].get("code") in (429, 503):
                wait = 60 if res_json["error"].get("code") == 429 else 15
                print(f"[{attempt}/{max_retries}] API Code {res_json['error'].get('code')}. Waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"Error payload: {res_json}")
                break
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(5)
    return None

def append_to_file(name, items, source_chapter):
    if not items:
        return
    path = os.path.join(candidates_dir, f"{name}.md")
    
    yaml_items = []
    for item in items:
        entry = {}
        if name == "glossary":
            entry["term"] = item.get("term", item.get("title", ""))
            entry["definition"] = item.get("definition", item.get("summary", ""))
        else:
            entry["title"] = item.get("title", "")
            entry["type"] = name[:-1] if name.endswith("s") else name
            entry["summary"] = item.get("summary", "")
        
        entry["source_chapter"] = source_chapter
        entry["source_quote"] = item.get("source_quote", "").strip()
        entry["tags"] = item.get("tags", [])
        yaml_items.append(entry)
        
    yaml_text = yaml.dump(yaml_items, allow_unicode=True, default_flow_style=False)
    with open(path, "a", encoding="utf-8") as f:
        f.write(yaml_text + "\n")

# Main execution loop
for idx, filename in enumerate(files, 1):
    # Skip large files since they might trigger TPM or excessive billing
    if "Retired_Amazon_VP" in filename or "The_Managers_Path" in filename:
        print(f"[{idx}/{len(files)}] Skipping very large book files for candidates: {filename}...")
        continue

    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()[:20000] # Limit size
        
    print(f"[{idx}/{len(files)}] Extracting from {filename}...")
    res = run_extraction(filename, content)
    if res:
        for cat in ["frameworks", "principles", "cases", "counter_examples", "glossary"]:
            append_to_file(cat, res.get(cat, []), filename)
        print("Success.")
    else:
        print("Failed.")
        
    time.sleep(6)

print("Extraction completed!")
