#!/usr/bin/env python3
import os
import json
import re
import sys
import argparse

# Dynamic configuration based on argument
parser = argparse.ArgumentParser(description="Compile transcripts into a master book.")
parser.add_argument("channel_dir", nargs="?", default="interactive_english", help="Channel directory path or name under transcripts/")
args = parser.parse_args()

TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "transcripts")

# Determine paths
if os.path.isabs(args.channel_dir) or args.channel_dir.startswith(".") or "/" in args.channel_dir:
    INPUT_DIR = os.path.abspath(args.channel_dir)
    CHANNEL_NAME = os.path.basename(INPUT_DIR)
else:
    CHANNEL_NAME = args.channel_dir
    INPUT_DIR = os.path.join(TRANSCRIPTS_DIR, CHANNEL_NAME)

MASTER_FILE = os.path.join(os.path.dirname(INPUT_DIR), f"{CHANNEL_NAME}_master.md")
TRACKER_FILE = os.path.join(os.path.dirname(INPUT_DIR), f"{CHANNEL_NAME}_compile_tracker.json")

BATCH_SIZE = 5

def load_tracker():
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"last_index": 0, "processed_files": []}

def save_tracker(tracker):
    with open(TRACKER_FILE, 'w', encoding='utf-8') as f:
        json.dump(tracker, f, indent=2, ensure_ascii=False)

def get_markdown_files():
    if not os.path.exists(INPUT_DIR):
        print(f"Error: {INPUT_DIR} does not exist.")
        return []
    # Find all .md files in the channel directory, ignoring any master or TOC files
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.md') and not f.endswith('_master.md')]
    # Sort them alphabetically
    return sorted(files)

def generate_toc():
    """Read the master file and prepend a Table of Contents based on ## headings."""
    if not os.path.exists(MASTER_FILE):
        return
        
    print("\n[→] Generating Table of Contents...")
    with open(MASTER_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all ## headings (ignoring any existing TOC headings)
    headings = re.findall(r'^##\s+(.*?)$', content, re.MULTILINE)
    
    toc_lines = [
        f"# {CHANNEL_NAME.replace('_', ' ').title()} Master Transcript Book\n",
        f"This book contains the compiled study transcripts for the @{CHANNEL_NAME} YouTube channel.\n",
        "## Table of Contents\n"
    ]
    
    for heading in headings:
        # Create anchor link
        anchor = heading.lower()
        anchor = re.sub(r'[^a-z0-9\s_-]', '', anchor) # strip non-alphanumeric except spaces/dashes
        anchor = re.sub(r'\s+', '-', anchor) # convert spaces to dashes
        toc_lines.append(f"- [{heading}](#{anchor})")
        
    toc_lines.append("\n---\n")
    
    # Strip existing TOC/Headers if any to avoid duplication
    idx = content.find("## ")
    if idx != -1:
        body = content[idx:]
    else:
        body = content
        
    new_content = '\n'.join(toc_lines) + '\n' + body
    
    with open(MASTER_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("[✓] Table of Contents generated successfully!")

def main():
    tracker = load_tracker()
    files = get_markdown_files()
    total_files = len(files)
    
    if total_files == 0:
        print("No files found to compile.")
        return
        
    start_idx = tracker["last_index"]
    if start_idx >= total_files:
        print(f"All {total_files} files have already been compiled.")
        generate_toc()
        if os.path.exists(TRACKER_FILE):
            os.remove(TRACKER_FILE)
            print("[✓] Temporary tracker file deleted.")
        return

    # Loop over all remaining batches
    while start_idx < total_files:
        end_idx = min(start_idx + BATCH_SIZE, total_files)
        batch_files = files[start_idx:end_idx]
        
        print(f"=== Compiling Batch: {start_idx + 1} to {end_idx} of {total_files} ===")
        
        # Determine mode: write if first batch, append otherwise
        mode = 'w' if start_idx == 0 else 'a'
        
        with open(MASTER_FILE, mode, encoding='utf-8') as master:
            if start_idx == 0:
                master.write(f"# {CHANNEL_NAME.replace('_', ' ').title()} Master Transcript Book\n\n")
                
            for i, filename in enumerate(batch_files, start_idx + 1):
                filepath = os.path.join(INPUT_DIR, filename)
                print(f"[{i}/{total_files}] Merging: {filename}")
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    file_content = f.read().strip()
                    
                # Format each transcript as a chapter starting with ## {Index}. {Title}
                if file_content.startswith("# "):
                    lines = file_content.split('\n')
                    title = lines[0][2:].strip()
                    lines[0] = f"## {i}. {title}"
                    file_content = '\n'.join(lines)
                else:
                    title_clean = filename.replace('.md', '').replace('_en', '').replace('_', ' ')
                    file_content = f"## {i}. {title_clean}\n\n" + file_content
                    
                master.write(file_content)
                master.write("\n\n---\n\n")
                
                tracker["processed_files"].append(filename)
                
        tracker["last_index"] = end_idx
        save_tracker(tracker)
        print(f"Batch completed. Progress: {end_idx}/{total_files} files compiled.\n")
        start_idx = end_idx

    # Generate TOC and clean up
    generate_toc()
    if os.path.exists(TRACKER_FILE):
        os.remove(TRACKER_FILE)
        print("[✓] Temporary tracker file deleted.")
    print("\n=== Compilation Complete! ===")

if __name__ == '__main__':
    main()

