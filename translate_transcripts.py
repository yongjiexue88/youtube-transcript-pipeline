#!/usr/bin/env python3
import os
import re
import sys
import time
import requests
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

load_dotenv()

TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "transcripts", "starterstory")

# Construct proxy
WEBSHARE_USER = os.getenv("WEBSHARE_USERNAME")
WEBSHARE_PASS = os.getenv("WEBSHARE_PASSWORD")
PROXIES = None
if WEBSHARE_USER and WEBSHARE_PASS:
    user = WEBSHARE_USER.replace("-rotate", "")
    proxy_url = f"http://{user}-rotate:{WEBSHARE_PASS}@p.webshare.io:80"
    PROXIES = {
        "http": proxy_url,
        "https": proxy_url
    }
    print(f"[i] Using Webshare rotating proxy: p.webshare.io")

def translate_chunk(text, sl='en', tl='zh-CN', retries=5):
    if not text.strip():
        return ""
    
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t"
    for attempt in range(retries):
        try:
            # We set trust_env=False to ensure standard proxy overrides are used
            session = requests.Session()
            session.trust_env = False
            response = session.post(url, data={"q": text}, proxies=PROXIES, timeout=30)
            if response.status_code == 429:
                wait_time = 3 * (attempt + 1)
                print(f"  [!] Rate limited (429). Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
                continue
            response.raise_for_status()
            data = response.json()
            translated = "".join([c[0] for c in data[0] if c[0]])
            return translated
        except Exception as e:
            wait_time = 2 * (attempt + 1)
            print(f"  [!] Translation failed ({e}). Retrying in {wait_time}s...")
            time.sleep(wait_time)
    return None

def translate_file(filepath):
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if translation already exists
        if "## 中文翻译" in content or "## Chinese Translation" in content:
            return "skipped"

        # Parse metadata and original content
        parts = content.split("\n---\n", 1)
        if len(parts) < 2:
            print(f"  [!] Error: Could not find separator '---' in {filename}")
            return "failed"

        header = parts[0]
        body = parts[1].strip()

        # Extract title from header
        title_match = re.search(r'^#\s+(.*?)$', header, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else ""
        if not title:
            # Fallback to looking at the first line
            first_line = header.split("\n")[0]
            if first_line.startswith("# "):
                title = first_line[2:].strip()

        # Translate title
        cn_title = ""
        if title:
            cn_title = translate_chunk(title)
            if not cn_title:
                print(f"  [!] Failed to translate title for {filename}")
                return "failed"
            cn_title = cn_title.strip()

        # Split body into paragraphs
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        
        # Group paragraphs into chunks of at most 4000 characters
        chunks = []
        current_chunk = []
        current_length = 0

        for p in paragraphs:
            if current_length + len(p) + 2 > 4000:
                chunks.append("\n\n".join(current_chunk))
                current_chunk = [p]
                current_length = len(p)
            else:
                current_chunk.append(p)
                current_length += len(p) + 2

        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        # Translate each chunk
        cn_paragraphs = []
        for i, chunk in enumerate(chunks):
            cn_chunk = translate_chunk(chunk)
            if cn_chunk is None:
                print(f"  [!] Failed to translate chunk {i+1} in {filename}")
                return "failed"
            cn_paragraphs.append(cn_chunk.strip())

        cn_body = "\n\n".join(cn_paragraphs)

        # Append translation to original file
        translation_section = f"\n\n---\n\n## 中文翻译\n\n# {cn_title}\n\n{cn_body}\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content + translation_section)

        print(f"  [✓] Translated: {filename} -> {cn_title}")
        return "success"
    except Exception as e:
        print(f"  [!] Error processing {filename}: {e}")
        return "failed"

def main():
    global TRANSCRIPTS_DIR
    if not os.path.exists(TRANSCRIPTS_DIR):
        print(f"Error: {TRANSCRIPTS_DIR} does not exist.")
        sys.exit(1)

    # Check if specific file is passed as argument
    if len(sys.argv) > 1:
        arg_path = os.path.abspath(sys.argv[1])
        if os.path.isfile(arg_path):
            md_files = [os.path.basename(arg_path)]
            TRANSCRIPTS_DIR = os.path.dirname(arg_path)
        else:
            md_files = [sys.argv[1]]
    else:
        md_files = sorted([f for f in os.listdir(TRANSCRIPTS_DIR) if f.endswith('.md')])

    print(f"Found {len(md_files)} markdown files to process.")

    success_count = 0
    fail_count = 0
    skipped_count = 0

    # Process files concurrently
    max_workers = 10
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(translate_file, os.path.join(TRANSCRIPTS_DIR, f)): f for f in md_files}
        for future in as_completed(futures):
            filename = futures[future]
            try:
                res = future.result()
                if res == "success":
                    success_count += 1
                elif res == "skipped":
                    skipped_count += 1
                else:
                    fail_count += 1
            except Exception as e:
                print(f"  [!] Future error for {filename}: {e}")
                fail_count += 1

    print("\n=== Translation Summary ===")
    print(f"Successfully translated: {success_count}")
    print(f"Skipped (already translated): {skipped_count}")
    print(f"Failed: {fail_count}")

if __name__ == '__main__':
    main()
