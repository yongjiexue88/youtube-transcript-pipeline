import os
import re

channels = ["microconf", "saasclub", "robwalling", "lennyspodcast", "gregisenberg", "saastr"]
base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts"
output_base_dir = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/clean_transcripts"

os.makedirs(output_base_dir, exist_ok=True)

def preprocess_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata
    title_match = re.search(r'^Title\s*:\s*(.*)$', content, re.MULTILINE)
    video_id_match = re.search(r'^Video ID\s*:\s*(.*)$', content, re.MULTILINE)
    url_match = re.search(r'^URL\s*:\s*(.*)$', content, re.MULTILINE)
    
    title = title_match.group(1).strip() if title_match else ""
    video_id = video_id_match.group(1).strip() if video_id_match else ""
    url = url_match.group(1).strip() if url_match else ""
    
    # Find the divider
    divider = "------------------------------------------------------------"
    parts = content.split(divider)
    if len(parts) < 2:
        # If no divider, just use the whole content
        transcript_body = content
    else:
        transcript_body = parts[1]
        
    # Clean transcript body
    lines = transcript_body.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Remove timestamp [00:00.00] or [00:00:00.00]
        line = re.sub(r'^\[\d{2}:\d{2}(?::\d{2})?(?:\.\d+)?\]\s*', '', line)
        # Remove speaker markers >> or similar
        line = re.sub(r'^>>\s*', '', line)
        line = line.strip()
        if line:
            cleaned_lines.append(line)
            
    # Combine short lines into paragraphs (e.g. 15 lines per paragraph)
    paragraphs = []
    current_para = []
    for line in cleaned_lines:
        current_para.append(line)
        if len(current_para) >= 15:
            paragraphs.append(" ".join(current_para))
            current_para = []
    if current_para:
        paragraphs.append(" ".join(current_para))
        
    # Format output
    output = f"Title: {title}\nVideo ID: {video_id}\nURL: {url}\n\n"
    output += "\n\n".join(paragraphs)
    return output

for channel in channels:
    channel_dir = os.path.join(base_dir, channel)
    output_channel_dir = os.path.join(output_base_dir, channel)
    os.makedirs(output_channel_dir, exist_ok=True)
    
    if not os.path.exists(channel_dir):
        print(f"Directory {channel_dir} does not exist. Skipping.")
        continue
        
    files = [f for f in os.listdir(channel_dir) if f.endswith(('.txt', '.md'))]
    print(f"Preprocessing {len(files)} files for channel '{channel}'...")
    
    for filename in files:
        src_path = os.path.join(channel_dir, filename)
        dest_path = os.path.join(output_channel_dir, filename)
        try:
            cleaned_text = preprocess_file(src_path)
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_text)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Preprocessing completed successfully.")
