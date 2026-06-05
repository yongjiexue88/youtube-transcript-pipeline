#!/usr/bin/env python3
import os
import json
import re

TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "transcripts")
INPUT_DIR = os.path.join(TRANSCRIPTS_DIR, "interactive_english")
MASTER_FILE = os.path.join(TRANSCRIPTS_DIR, "interactive_english_master.md")
TRACKER_FILE = os.path.join(TRANSCRIPTS_DIR, "interactive_english_compile_tracker.json")

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
    # Find all .md files in the channel directory
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.md')]
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
        "# Interactive English Master Transcript Book\n",
        "This book contains the compiled study transcripts for the @InteractiveEng YouTube channel.\n",
        "## Table of Contents\n"
    ]
    
    for heading in headings:
        # Create anchor link
        anchor = heading.lower()
        anchor = re.sub(r'[^a-z0-9\s_-]', '', anchor) # strip non-alphanumeric except spaces/dashes
        anchor = re.sub(r'\s+', '-', anchor) # convert spaces to dashes
        toc_lines.append(f"- [{heading}](#{anchor})")
        
    toc_lines.append("\n---\n")
    
    # Check if there is an existing title or separator and strip it
    # We will search for the first '---' or first '## ' and keep everything from there
    # If the file already has a TOC from a previous run, strip it.
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
        # Make sure TOC is generated
        generate_toc()
        return

    end_idx = min(start_idx + BATCH_SIZE, total_files)
    batch_files = files[start_idx:end_idx]
    
    print(f"=== Compiling Batch: {start_idx + 1} to {end_idx} of {total_files} ===")
    
    # Determine mode: write if first batch, append otherwise
    mode = 'w' if start_idx == 0 else 'a'
    
    with open(MASTER_FILE, mode, encoding='utf-8') as master:
        # If starting fresh, write a placeholder header (will be replaced by TOC at the end)
        if start_idx == 0:
            master.write("# Interactive English Master Transcript Book\n\n")
            
        for i, filename in enumerate(batch_files, start_idx + 1):
            filepath = os.path.join(INPUT_DIR, filename)
            print(f"[{i}/{total_files}] Merging: {filename}")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                file_content = f.read().strip()
                
            # If the file content starts with `# `, convert it to `## ` to fit into the book-ish hierarchy
            if file_content.startswith("# "):
                # Find the title line
                lines = file_content.split('\n')
                title = lines[0][2:].strip()
                # Change title header to ## [Index]. [Title]
                lines[0] = f"## {i}. {title}"
                file_content = '\n'.join(lines)
            else:
                # Fallback if title is missing/different
                title_clean = filename.replace('.md', '').replace('_en', '').replace('_', ' ')
                file_content = f"## {i}. {title_clean}\n\n" + file_content
                
            master.write(file_content)
            master.write("\n\n---\n\n")
            
            tracker["processed_files"].append(filename)
            
    tracker["last_index"] = end_idx
    save_tracker(tracker)
    
    print(f"Batch completed. Progress: {end_idx}/{total_files} files compiled.")
    
    # If this was the last batch, generate the Table of Contents
    if end_idx >= total_files:
        generate_toc()
        print("\n=== Compilation Complete! ===")
    else:
        print("Run the script again to process the next batch.")

if __name__ == '__main__':
    main()
