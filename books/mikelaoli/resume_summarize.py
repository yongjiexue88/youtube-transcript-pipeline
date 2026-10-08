import os
import re
import requests
import json
import time

base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/mikelaoli"
api_key = os.environ.get("GEMINI_API_KEY", "")

if not api_key:
    # Try reading from .env
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

# Load existing summaries
output_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/books/mikelaoli/raw_summaries.json"
if os.path.exists(output_path):
    with open(output_path, "r", encoding="utf-8") as f:
        summaries = json.load(f)
else:
    summaries = {}

# Process each file to extract its main message/principles via Gemini
for idx, filename in enumerate(files, 1):
    # Only process files that failed or haven't been summarized
    if summaries.get(filename) != "Error summarizing." and filename in summaries:
        print(f"[{idx}/{len(files)}] Skipping {filename} (already completed)...")
        continue

    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()[:15000] # Limit to first 15k chars for prompt
    
    print(f"[{idx}/{len(files)}] Summarizing {filename}...")
    
    prompt = f"""You are Cangjie Skill Extractor. Analyze this transcript content from YouTube channel "mikelaoli" (an ex-Amazon Director sharing career guidance, corporate politics strategies, communication techniques, and workplace survival skills).
Extract:
1. Core problem/topic being discussed.
2. The core methodology, framework, rules, or steps proposed.
3. Relevant examples or counter-examples.

Transcript text:
{content}

Respond in concise Chinese. Keep it short (maximum 150-200 words).
"""
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    # Try up to 5 times with backoff when encountering rate limits
    max_retries = 5
    retry_count = 0
    success = False
    
    while retry_count < max_retries and not success:
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            res_data = response.json()
            if "candidates" in res_data:
                summary_text = res_data["candidates"][0]["content"]["parts"][0]["text"]
                summaries[filename] = summary_text
                print("Success.")
                success = True
                # Save progressively
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(summaries, f, ensure_ascii=False, indent=2)
            elif "error" in res_data and res_data["error"].get("code") == 429:
                retry_count += 1
                wait_time = 60
                print(f"Rate limited (429). Retrying {retry_count}/{max_retries} in {wait_time}s...")
                time.sleep(wait_time)
            elif "error" in res_data and res_data["error"].get("code") == 503:
                retry_count += 1
                wait_time = 15
                print(f"Service Unavailable (503). Retrying {retry_count}/{max_retries} in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"Failed response structure: {res_data}")
                summaries[filename] = "Error summarizing."
                break
        except Exception as e:
            print(f"Failed: {e}")
            summaries[filename] = "Error summarizing."
            break
    
    # Wait 6 seconds between success requests to avoid rate limits
    if success:
        time.sleep(6)

print("Saved final summaries.")
