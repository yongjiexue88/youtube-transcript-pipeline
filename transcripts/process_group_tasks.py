import os
import re
import sys
import time
import json
import subprocess
import requests

API_KEY = "AIzaSyDPgHA3CXNvTwaMjmHrNpWUQh7XxhiRnzI"
MODEL = "gemini-2.5-flash-lite"
GROUP_JSON_PATH = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/subagent_tasks/group_03.json"
CLEAN_TRANSCRIPTS_DIR = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/clean_transcripts"
TEMP_SUMMARY_PATH = f"/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/temp_summary_{os.getpid()}.txt"
SAVE_SUMMARY_SCRIPT = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/save_summary.py"

def get_video_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line.startswith("Title:"):
                return first_line.replace("Title:", "").strip()
    except Exception as e:
        print(f"Error reading title from {filepath}: {e}")
    # Fallback to filename
    basename = os.path.basename(filepath)
    title = os.path.splitext(basename)[0]
    if title.endswith("_en") or title.endswith("_zh") or title.endswith("_vi"):
        title = title[:-3]
    return title.replace("_", " ")

def call_gemini_api(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 2048,
            "temperature": 0.2
        }
    }
    
    backoff = 5
    for attempt in range(15):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=90)
            if response.status_code == 200:
                resp_json = response.json()
                text = resp_json['candidates'][0]['content']['parts'][0]['text']
                return text
            elif response.status_code == 429:
                print(f"Rate limit 429 hit. Retrying in {backoff} seconds...")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)
            else:
                print(f"API Error {response.status_code}: {response.text}. Retrying in {backoff} seconds...")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)
        except Exception as e:
            print(f"Request exception: {e}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            backoff = min(backoff * 2, 60)
            
    raise Exception(f"Failed to call Gemini API after multiple attempts.")


def process_task_file(task_path):
    print(f"\n==================================================")
    print(f"Processing Task File: {os.path.basename(task_path)}")
    print(f"==================================================")
    
    with open(task_path, 'r', encoding='utf-8') as f:
        task_data = json.load(f)
        
    channel = task_data["channel"]
    files = task_data["files"]
    output_file = task_data["output_file"]
    
    # Check if output file already exists
    processed_count = 0
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("# "):
                    processed_count += 1
        print(f"Output file exists. Found {processed_count} already processed summaries.")
    else:
        print(f"Output file does not exist yet. Will create: {output_file}")
        
    remaining_files = files[processed_count:]
    print(f"Total files in task: {len(files)}, Remaining to process: {len(remaining_files)}")
    
    for idx, filename in enumerate(remaining_files):
        real_idx = processed_count + idx
        print(f"\n[{real_idx + 1}/{len(files)}] Processing {filename}...")
        
        transcript_path = os.path.join(CLEAN_TRANSCRIPTS_DIR, channel, filename)
        if not os.path.exists(transcript_path):
            print(f"WARNING: Transcript file not found at {transcript_path}. Skipping.")
            continue
            
        with open(transcript_path, 'r', encoding='utf-8') as tf:
            transcript_text = tf.read()
            
        video_title = get_video_title(transcript_path)
        print(f"Video Title: {video_title}")
        
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

Format your response exactly as a markdown block with the video title as the heading:
# {video_title}
0. **公司/产品名称：** ...
0.5. **成立时间：** ...
0.8. **公司规模/营收/盈利规模：** ...
1. **他卖什么？** ...
...

Write the analysis in Chinese, keeping technical terms or product names in English where appropriate. If the video is a general tutorial/advice rather than a case study of a specific startup, note that it's a general topic and summarize its key takeaways within the questions above, referencing examples given in the video.
"""

        try:
            summary = call_gemini_api(prompt)
            
            # Write summary to temp file
            with open(TEMP_SUMMARY_PATH, 'w', encoding='utf-8') as temp_f:
                temp_f.write(summary)
                
            # Run save_summary.py
            cmd = ["python3", SAVE_SUMMARY_SCRIPT, output_file, TEMP_SUMMARY_PATH]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print(f"Successfully appended summary for '{video_title}'.")
            else:
                print(f"Error appending summary: {res.stderr}")
                
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
        finally:
            if os.path.exists(TEMP_SUMMARY_PATH):
                try:
                    os.remove(TEMP_SUMMARY_PATH)
                except Exception:
                    pass
            
        # Rate limit delay (about 4 seconds between requests to stay under 15 RPM)
        time.sleep(4.0)

def main():
    global GROUP_JSON_PATH
    if len(sys.argv) > 1:
        GROUP_JSON_PATH = sys.argv[1]
    if not os.path.exists(GROUP_JSON_PATH):
        print(f"ERROR: Group JSON not found at {GROUP_JSON_PATH}")
        sys.exit(1)
        
    with open(GROUP_JSON_PATH, 'r', encoding='utf-8') as f:
        group_data = json.load(f)
        
    group_id = group_data["group_id"]
    tasks = group_data["tasks"]
    
    print(f"Starting execution of Group: {group_id}")
    print(f"Number of tasks to process: {len(tasks)}")
    
    for task_path in tasks:
        process_task_file(task_path)
        
    print(f"\nAll tasks in group {group_id} processed successfully.")

if __name__ == "__main__":
    main()
