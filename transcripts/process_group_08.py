import os
import sys
import json
import time
import requests
import re
import signal
import subprocess

def get_api_key():
    env_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/.env"
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    return line.strip().split("=", 1)[1].strip('"').strip("'")
    return os.environ.get("GEMINI_API_KEY")

def clean_markdown(text):
    text = text.strip()
    text = re.sub(r'^```[a-zA-Z]*\n', '', text)
    text = re.sub(r'\n```$', '', text)
    return text.strip()

def analyze_transcript(filepath, api_key):
    with open(filepath, 'r', encoding='utf-8') as f:
        transcript_text = f.read()

    # Extract title from transcript (line 1 usually starts with "Title: ")
    title = "Video Transcript"
    for line in transcript_text.split('\n'):
        if line.startswith("Title:"):
            title = line.replace("Title:", "").strip()
            break

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
...

Write the analysis in Chinese, keeping technical terms or product names in English where appropriate. If the video is a general tutorial/advice rather than a case study of a specific startup, note that it's a general topic and summarize its key takeaways within the questions above, referencing examples given in the video.
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 2048,
            "temperature": 0.2
        }
    }

    backoff = 2
    for attempt in range(10):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                resp_json = response.json()
                text = resp_json['candidates'][0]['content']['parts'][0]['text']
                return clean_markdown(text)
            elif response.status_code == 429:
                print(f"Rate limit hit for {os.path.basename(filepath)}. Retrying in {backoff}s...")
                time.sleep(backoff)
                backoff *= 2.5
            else:
                print(f"Error {response.status_code} for {os.path.basename(filepath)}: {response.text}. Retrying...")
                time.sleep(backoff)
                backoff *= 2
        except Exception as e:
            print(f"Exception during request for {os.path.basename(filepath)}: {e}. Retrying...")
            time.sleep(backoff)
            backoff *= 2

    raise Exception(f"Failed to analyze {os.path.basename(filepath)} after all attempts.")

def save_summary_safely(output_file, summary_text):
    # Find conflicting python PIDs
    pids = []
    my_pid = os.getpid()
    try:
        res = subprocess.run(["ps", "aux"], capture_output=True, text=True)
        for line in res.stdout.split('\n'):
            if "python" in line and "youtube-transcript-pipeline" in line:
                if "grep" in line or "process_group_08" in line:
                    continue
                parts = line.split()
                if len(parts) > 1:
                    try:
                        pid = int(parts[1])
                        if pid != my_pid:
                            pids.append(pid)
                    except ValueError:
                        pass
    except Exception as e:
        print(f"Error listing processes: {e}")
        pids = []

    pids = list(set(pids))

    # Pause other processes
    for pid in pids:
        try:
            os.kill(pid, signal.SIGSTOP)
        except Exception:
            pass

    try:
        # Write to temp_summary.txt
        temp_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/temp_summary.txt"
        with open(temp_path, 'w', encoding='utf-8') as temp_f:
            temp_f.write(summary_text)

        # Run save_summary.py
        cmd = f"python3 /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/save_summary.py {output_file} {temp_path}"
        os.system(cmd)
    finally:
        # Resume other processes
        for pid in pids:
            try:
                os.kill(pid, signal.SIGCONT)
            except Exception:
                pass

def main():
    api_key = get_api_key()
    if not api_key:
        print("GEMINI_API_KEY not found.")
        sys.exit(1)

    group_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/subagent_tasks/group_08.json"
    with open(group_path, 'r', encoding='utf-8') as f:
        group_data = json.load(f)

    tasks = group_data["tasks"]
    for task_path in tasks:
        print(f"\n========================================")
        print(f"Processing task: {task_path}")
        print(f"========================================")
        with open(task_path, 'r', encoding='utf-8') as tf:
            task_data = json.load(tf)

        channel = task_data["channel"]
        files = task_data["files"]
        output_file = task_data["output_file"]

        # Check existing output
        processed_count = 0
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as out_f:
                for line in out_f:
                    if line.startswith("# "):
                        processed_count += 1

        print(f"Channel: {channel}, Total files: {len(files)}, Processed: {processed_count}")

        # Skip already processed
        remaining_files = files[processed_count:]
        for idx, filename in enumerate(remaining_files):
            real_idx = processed_count + idx
            filepath = f"/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/clean_transcripts/{channel}/{filename}"
            print(f"[{real_idx + 1}/{len(files)}] Processing {filename}...")

            if not os.path.exists(filepath):
                print(f"File not found: {filepath}. Skipping.")
                continue

            # Analyze
            summary = analyze_transcript(filepath, api_key)

            # Save summary safely without race conditions
            save_summary_safely(output_file, summary)

            # Add a small delay between requests to avoid rate limits
            time.sleep(3)

    print("ALL TASKS IN GROUP_08 COMPLETED SUCCESSFULLY.")

if __name__ == '__main__':
    main()
