import os
import re
import sys
import time
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

channels = ["microconf", "saasclub", "robwalling", "lennyspodcast", "gregisenberg", "saastr"]
clean_base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/clean_transcripts"
cache_base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/cached_summaries"
report_base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/business_report"

# Rate limiting settings
MAX_WORKERS = 3  # Keep concurrent requests low to avoid hitting TPM/RPM limits
RPM_LIMIT = 15
REQUEST_DELAY = 60.0 / RPM_LIMIT  # delay between starting requests

def get_api_key():
    # 1. Check environment
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return api_key
        
    # 2. Check .env file
    env_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/.env"
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    return line.strip().split("=", 1)[1].strip('"').strip("'")
    return None

def analyze_transcript(filepath, api_key):
    with open(filepath, 'r', encoding='utf-8') as f:
        transcript_text = f.read()
        
    # Construct Prompt
    prompt = f"""You are a business analysis expert. Your task is to read the YouTube transcript of a video and produce a detailed business analysis report in Chinese.

Transcript text:
{transcript_text}

Analyze the transcript carefully and answer these 13 specific questions in Chinese. Keep your answers extremely concise (use brief phrases or bullet points instead of long sentences):

0. **公司/产品名称：** (Startup/Product Name - note "未提及" if not mentioned)
0.5. **成立时间：** (Establishment Date - note "未提及" if not mentioned)
0.8. **公司规模/营收/盈利规模：** (Company Size, Revenue, or Profit - note "未提及" if not mentioned)
1. **他卖什么？** (What do they sell? Product/service description, pricing model, target audience)
2. **怎么获客？** (How do they acquire customers? Marketing channels, growth strategies, traffic sources)
3. **怎么成交？** (How do they close sales? Sales process, conversion tactics, pricing strategy)
4. **怎么交付？** (How do they deliver? Product delivery method, tech stack, onboarding)
5. **怎么做复购？** (How do they drive repeat purchases/retention? Retention strategies, subscription model, upselling)
6. **用户在吐槽什么？** (What are users complaining about? Pain points, negative feedback)
7. **用户在追问什么？** (What are users asking about? Common questions, feature requests)
8. **用户在哪一步卡住？** (Where do users get stuck? Friction points, barriers to adoption)
9. **用户愿意为什么付费？** (What are users willing to pay for? Value proposition, key features worth paying for)
10. **支持什么平台？** (What platforms do they support? Web, mobile (iOS/Android), desktop, etc.)

Format your response as a markdown block with the video title as the heading:
# [Video Title]
0. **公司/产品名称：** ...
0.5. **成立时间：** ...
0.8. **公司规模/营收/盈利规模：** ...
1. **他卖什么？** ...
...

Write the analysis in Chinese, keeping technical terms or product names in English where appropriate. If the video is a general tutorial/advice rather than a case study of a specific startup, note that it's a general topic and summarize its key takeaways within the questions above, referencing examples given in the video.
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 2048,
            "temperature": 0.2
        }
    }
    
    # Retry loop for rate limits and connection issues
    backoff = 2
    for attempt in range(5):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                resp_json = response.json()
                text = resp_json['candidates'][0]['content']['parts'][0]['text']
                return text
            elif response.status_code == 429:
                # Rate limit exceeded
                print(f"Rate limit hit for {os.path.basename(filepath)}. Retrying in {backoff}s...")
                time.sleep(backoff)
                backoff *= 2
            else:
                print(f"Error {response.status_code} for {os.path.basename(filepath)}: {response.text}")
                time.sleep(backoff)
                backoff *= 2
        except Exception as e:
            print(f"Exception during request for {os.path.basename(filepath)}: {e}")
            time.sleep(backoff)
            backoff *= 2
            
    raise Exception(f"Failed to analyze {os.path.basename(filepath)} after 5 attempts.")

def process_file(filepath, cache_path, api_key):
    # Check cache
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'summary' in data and data['summary']:
                    return data['summary']
        except Exception:
            pass
            
    # Process
    summary = analyze_transcript(filepath, api_key)
    
    # Save cache
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, 'w', encoding='utf-8') as f:
        json.dump({'file': os.path.basename(filepath), 'summary': summary}, f, ensure_ascii=False, indent=2)
        
    return summary

def main():
    api_key = get_api_key()
    if not api_key:
        print("ERROR: GEMINI_API_KEY is not configured in your environment or .env file.")
        print("Please export GEMINI_API_KEY=your_key or add GEMINI_API_KEY=\"your_key\" to your .env file.")
        sys.exit(1)
        
    os.makedirs(report_base_dir, exist_ok=True)
    
    for channel in channels:
        channel_clean_dir = os.path.join(clean_base_dir, channel)
        channel_cache_dir = os.path.join(cache_base_dir, channel)
        
        if not os.path.exists(channel_clean_dir):
            continue
            
        files = sorted([f for f in os.listdir(channel_clean_dir) if f.endswith(('.txt', '.md'))])
        print(f"\n========================================")
        print(f"Processing channel '{channel}' ({len(files)} files)")
        print(f"========================================")
        
        # Determine files that actually need processing
        to_process = []
        for f in files:
            src = os.path.join(channel_clean_dir, f)
            cache = os.path.join(channel_cache_dir, f.replace('.txt', '.json').replace('.md', '.json'))
            if os.path.exists(cache):
                try:
                    with open(cache, 'r', encoding='utf-8') as cf:
                        data = json.load(cf)
                        if 'summary' in data and data['summary']:
                            continue
                except Exception:
                    pass
            to_process.append((src, cache))
            
        print(f"{len(files) - len(to_process)} files already cached. {len(to_process)} files to analyze.")
        
        if to_process:
            # Process in thread pool
            futures = {}
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                for idx, (src, cache) in enumerate(to_process):
                    # Add delay between submission to avoid burst RPM limit
                    time.sleep(REQUEST_DELAY)
                    future = executor.submit(process_file, src, cache, api_key)
                    futures[future] = src
                    
                completed = 0
                for future in as_completed(futures):
                    src = futures[future]
                    completed += 1
                    try:
                        future.result()
                        print(f"[{completed}/{len(to_process)}] Completed: {os.path.basename(src)}")
                    except Exception as e:
                        print(f"[{completed}/{len(to_process)}] Failed: {os.path.basename(src)}: {e}")
                        
        # Merge all summaries for this channel into the final report
        report_path = os.path.join(report_base_dir, f"{channel}.md")
        print(f"Compiling final report for '{channel}' to {report_path}...")
        
        summaries = []
        for f in files:
            cache = os.path.join(channel_cache_dir, f.replace('.txt', '.json').replace('.md', '.json'))
            if os.path.exists(cache):
                try:
                    with open(cache, 'r', encoding='utf-8') as cf:
                        data = json.load(cf)
                        if 'summary' in data and data['summary']:
                            summaries.append(data['summary'].strip())
                except Exception as e:
                    print(f"Error reading cache for {f}: {e}")
                    
        channel_title = channel.capitalize() if channel != "saastr" else "SaaStr"
        if channel == "lennyspodcast":
            channel_title = "Lenny's Podcast"
        elif channel == "gregisenberg":
            channel_title = "Greg Isenberg"
        elif channel == "saasclub":
            channel_title = "SaaS Club"
        elif channel == "robwalling":
            channel_title = "Rob Walling"
        elif channel == "microconf":
            channel_title = "MicroConf"
            
        report_content = f"# {channel_title} Business Analysis Report\n\n"
        report_content += "\n\n---\n\n".join(summaries)
        
        with open(report_path, 'w', encoding='utf-8') as rf:
            rf.write(report_content)
            
        print(f"Report for '{channel}' generated successfully. Size: {len(report_content)} characters.")

if __name__ == "__main__":
    main()
