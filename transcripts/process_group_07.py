import os
import re
import sys
import json
import time
import requests
import subprocess

group_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/subagent_tasks/group_07.json"
clean_base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/clean_transcripts"
api_key = "AIzaSyDPgHA3CXNvTwaMjmHrNpWUQh7XxhiRnzI"
model_name = "gemini-3-flash-preview"

def get_video_title(filepath, filename):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line.startswith("Title:"):
                return first_line[len("Title:"):].strip()
    except Exception as e:
        print(f"Error reading title from file {filepath}: {e}")
    
    # Fallback
    base = re.sub(r'_[a-z]{2}\.txt$', '', filename)
    return base.replace('_', ' ')

def count_processed_videos(output_file):
    if not os.path.exists(output_file):
        return 0
    try:
        count = 0
        with open(output_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("# "):
                    count += 1
        return count
    except Exception as e:
        print(f"Error reading output file {output_file}: {e}")
        return 0

def call_gemini(transcript_text, title):
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
# {title}
0. **公司/产品名称：** ...
0.5. **成立时间：** ...
0.8. **公司规模/营收/盈利规模：** ...
1. **他卖什么？** ...
2. **怎么获客？** ...
3. **怎么成交？** ...
4. **怎么交付？** ...
5. **怎么做复购？** ...
6. **用户在吐槽什么？** ...
7. **用户在追问什么？** ...
8. **用户在哪一步卡住？** ...
9. **用户愿意为什么付费？** ...
10. **支持什么平台？** ...

Write the analysis in Chinese, keeping technical terms or product names in English where appropriate. If the video is a general tutorial/advice rather than a case study of a specific startup, note that it's a general topic and summarize its key takeaways within the questions above, referencing examples given in the video.
"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 2048,
            "temperature": 0.2
        }
    }
    
    backoff = 5
    for attempt in range(8):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                resp_json = response.json()
                text = resp_json['candidates'][0]['content']['parts'][0]['text']
                return text
            elif response.status_code == 429:
                print(f"Rate limit (429) hit. Retrying in {backoff} seconds...")
                time.sleep(backoff)
                backoff *= 2
            else:
                print(f"Error {response.status_code}: {response.text}. Retrying in {backoff} seconds...")
                time.sleep(backoff)
                backoff *= 2
        except Exception as e:
            print(f"Exception: {e}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            backoff *= 2
            
    raise Exception("Failed to call Gemini API after multiple retries.")

def main():
    with open(group_path, 'r', encoding='utf-8') as f:
        group_data = json.load(f)
    
    tasks = group_data["tasks"]
    print(f"Loaded group {group_data['group_id']} with {len(tasks)} tasks.")
    
    for task_path in tasks:
        print(f"\nProcessing task: {task_path}")
        with open(task_path, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
        
        channel = task_data["channel"]
        files = task_data["files"]
        output_file = task_data["output_file"]
        
        # Check how many are already processed
        processed_count = count_processed_videos(output_file)
        print(f"Output file: {output_file}")
        print(f"Processed count: {processed_count} / {len(files)}")
        
        remaining_files = files[processed_count:]
        if not remaining_files:
            print(f"All files in task {task_path} are already processed.")
            continue
            
        print(f"Processing remaining {len(remaining_files)} files...")
        
        for idx, filename in enumerate(remaining_files, start=processed_count + 1):
            filepath = os.path.join(clean_base_dir, channel, filename)
            if not os.path.exists(filepath):
                print(f"File not found: {filepath}. Skipping.")
                continue
                
            print(f"[{idx}/{len(files)}] Processing: {filename}")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                transcript_text = f.read()
                
            title = get_video_title(filepath, filename)
            print(f"Extract title: {title}")
            
            try:
                summary = call_gemini(transcript_text, title)
                
                # Write to temp file
                temp_file = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/temp_summary.txt"
                with open(temp_file, 'w', encoding='utf-8') as tf:
                    tf.write(summary)
                    
                # Run save_summary.py
                save_script = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/save_summary.py"
                cmd = [sys.executable, save_script, output_file, temp_file]
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"Error running save_summary.py: {result.stderr}")
                    sys.exit(1)
                else:
                    print(f"Saved successfully: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
                sys.exit(1)
                
            # Sleep 4.5 seconds to avoid hitting RPM limits
            time.sleep(4.5)

    print("\nAll tasks in group completed successfully!")

if __name__ == "__main__":
    main()
