#!/usr/bin/env python3
"""
Reformat YouTube transcript files from timestamped format to article format.
- Strips timestamps like [00:00.00]
- Merges text into flowing paragraphs
- If the title is random letters (a YouTube video ID), generates a descriptive title from content
- Renames files with random-letter titles
- Preserves original metadata header
"""

import os
import re
import sys
import shutil

# Folder where transcripts are located
TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "transcripts")

# Regex to detect YouTube video ID pattern (11 chars, alphanumeric + dash/underscore)
VIDEO_ID_PATTERN = re.compile(r'^[A-Za-z0-9_-]{5,15}$')

# Regex to match timestamp lines like [00:00.00]  text
TIMESTAMP_LINE = re.compile(r'^\[(\d{2}:\d{2}\.\d{2})\]\s*(.*)')

# Regex to detect if title looks like a video ID (random letters/numbers)
def is_random_title(title):
    """Check if the title looks like a YouTube video ID rather than a real title."""
    title = title.strip()
    # YouTube video IDs are typically 11 characters of [A-Za-z0-9_-]
    if VIDEO_ID_PATTERN.match(title):
        return True
    return False

def extract_title_from_content(lines, language):
    """Generate a descriptive title from the first few lines of content."""
    # Collect the first ~200 characters of content to derive a title
    content_text = []
    for line in lines:
        match = TIMESTAMP_LINE.match(line)
        if match:
            text = match.group(2).strip()
            if text:
                content_text.append(text)
        if len(' '.join(content_text)) > 300:
            break
    
    if not content_text:
        return None
    
    # For Chinese content, take the first meaningful sentence
    full_text = ' '.join(content_text)
    
    # Try to find a natural title from the first few sentences
    if 'zh' in language:
        # Chinese: look for the first complete thought (usually within first few lines)
        # Remove filler words at start
        combined = ''.join(content_text[:10])  # Join without spaces for Chinese
        # Try to find a good breaking point
        for sep in ['。', '？', '！', '，', ' ']:
            idx = combined.find(sep)
            if 15 < idx < 80:
                return combined[:idx]
        # Fall back to first ~50 chars
        return combined[:50] if len(combined) > 50 else combined
    else:
        # English: take the first sentence or meaningful phrase
        # Join first few lines
        combined = ' '.join(content_text[:8])
        # Clean up
        combined = re.sub(r'\s+', ' ', combined).strip()
        # Try to find sentence end
        for sep in ['. ', '? ', '! ']:
            idx = combined.find(sep)
            if 15 < idx < 100:
                return combined[:idx]
        # Fall back to first ~80 chars, break at word boundary
        if len(combined) > 80:
            idx = combined.rfind(' ', 0, 80)
            if idx > 20:
                return combined[:idx]
        return combined[:80] if len(combined) > 80 else combined

def sanitize_filename(title):
    """Convert a title to a safe filename."""
    # Replace problematic characters
    safe = title.replace('/', '／').replace('\\', '＼')
    safe = safe.replace(':', '：').replace('*', '＊')
    safe = safe.replace('?', '？').replace('"', '"')
    safe = safe.replace('<', '＜').replace('>', '＞')
    safe = safe.replace('|', '｜').replace('\n', ' ')
    safe = safe.replace('\r', '')
    safe = re.sub(r'\s+', '_', safe.strip())
    # Limit length
    if len(safe) > 150:
        safe = safe[:150]
    return safe

def is_sentence_end(text, language):
    """Check if text ends with a sentence-ending punctuation."""
    text = text.rstrip()
    if not text:
        return False
    if 'zh' in language:
        return text[-1] in '。？！…」】）'
    else:
        return text[-1] in '.?!' and not text.endswith('..') and not re.search(r'\b[A-Z]\.$', text)

def get_pause_duration(ts1, ts2):
    """Calculate pause between two timestamps in seconds."""
    def parse_ts(ts):
        parts = ts.split(':')
        minutes = int(parts[0])
        seconds = float(parts[1])
        return minutes * 60 + seconds
    
    try:
        return parse_ts(ts2) - parse_ts(ts1)
    except:
        return 0

def reformat_file(filepath):
    """Reformat a single transcript file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Parse header
    header_lines = []
    content_lines = []
    separator_found = False
    header_end = 0
    
    for i, line in enumerate(lines):
        if line.strip() == '-' * 60:
            separator_found = True
            header_end = i + 1
            header_lines = lines[:i+1]
            break
    
    if not separator_found:
        print(f"  WARNING: No separator found in {filepath}, skipping")
        return None
    
    content_lines = lines[header_end:]
    
    # Extract metadata from header
    title = ""
    language = ""
    video_id = ""
    for line in header_lines:
        if line.startswith("Title"):
            title = line.split(':', 1)[1].strip()
        elif line.startswith("Language"):
            language = line.split(':', 1)[1].strip()
        elif line.startswith("Video ID"):
            video_id = line.split(':', 1)[1].strip()
    
    # Check if title needs replacement
    new_title = None
    if is_random_title(title):
        new_title = extract_title_from_content(content_lines, language)
        if new_title:
            print(f"  Generated title: '{new_title}' (was: '{title}')")
    
    # Strip timestamps and merge into paragraphs
    paragraphs = []
    current_paragraph = []
    prev_timestamp = None
    
    for line in content_lines:
        line = line.rstrip()
        if not line.strip():
            continue
        
        match = TIMESTAMP_LINE.match(line)
        if match:
            timestamp = match.group(1)
            text = match.group(2).strip()
            
            if not text:
                continue
            
            # Determine if we should start a new paragraph
            start_new = False
            
            if prev_timestamp and current_paragraph:
                pause = get_pause_duration(prev_timestamp, timestamp)
                # Long pause suggests topic change / new paragraph
                if pause > 3.0:
                    start_new = True
                # Also check if previous text ended with sentence-ending punctuation
                # and there's a moderate pause
                elif pause > 1.5 and current_paragraph:
                    last_text = current_paragraph[-1]
                    if is_sentence_end(last_text, language):
                        start_new = True
            
            if start_new and current_paragraph:
                paragraphs.append(current_paragraph)
                current_paragraph = []
            
            current_paragraph.append(text)
            prev_timestamp = timestamp
        else:
            # Non-timestamp, non-empty line - treat as content
            if line.strip():
                current_paragraph.append(line.strip())
    
    if current_paragraph:
        paragraphs.append(current_paragraph)
    
    # Join paragraphs - use space for English, no separator for Chinese
    formatted_paragraphs = []
    for para in paragraphs:
        if 'zh' in language:
            # Chinese: no spaces between fragments  
            joined = ''
            for i, text in enumerate(para):
                # Check if we need a space (e.g., between English words in Chinese text)
                if joined and text:
                    last_char = joined[-1] if joined else ''
                    first_char = text[0] if text else ''
                    # Add space between English/number tokens
                    needs_space = (
                        (last_char.isascii() and last_char.isalnum() and 
                         first_char.isascii() and first_char.isalnum()) or
                        (last_char.isascii() and last_char.isalnum() and
                         not first_char.isascii()) or
                        (not last_char.isascii() and
                         first_char.isascii() and first_char.isalnum())
                    )
                    if needs_space:
                        joined += ' '
                joined += text
            formatted_paragraphs.append(joined)
        else:
            # English: space between fragments
            formatted_paragraphs.append(' '.join(para))
    
    # Build output
    output_lines = []
    
    # Rebuild header with possibly new title
    for line in header_lines:
        if new_title and line.startswith("Title"):
            output_lines.append(f"Title     : {new_title}\n")
        elif line.startswith("Snippets"):
            # Remove snippets count since we're reformatting
            continue
        else:
            output_lines.append(line)
    
    output_lines.append('\n')
    
    # Add formatted content
    for i, para in enumerate(formatted_paragraphs):
        output_lines.append(para + '\n')
        if i < len(formatted_paragraphs) - 1:
            output_lines.append('\n')
    
    # Determine output filename
    old_basename = os.path.basename(filepath)
    if new_title:
        # Extract language suffix from old filename
        lang_suffix = ''
        name_no_ext = os.path.splitext(old_basename)[0]
        # Check for language suffixes like _zh, _en, _zh-CN
        lang_match = re.search(r'_([a-z]{2}(?:-[A-Z]{2})?)$', name_no_ext)
        if lang_match:
            lang_suffix = '_' + lang_match.group(1)
        
        new_basename = sanitize_filename(new_title) + lang_suffix + '.txt'
    else:
        new_basename = old_basename
    
    new_filepath = os.path.join(os.path.dirname(filepath), new_basename)
    
    # Write output
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    # If file was renamed, remove old file
    if new_filepath != filepath and os.path.exists(filepath):
        os.remove(filepath)
        print(f"  Renamed: {old_basename} -> {new_basename}")
    
    return new_filepath

def main():
    if not os.path.exists(TRANSCRIPTS_DIR):
        print(f"Error: {TRANSCRIPTS_DIR} does not exist.")
        sys.exit(1)

    total = 0
    processed = 0
    errors = 0
    renamed = 0
    
    # Check if a specific subdirectory or file is passed as command line argument
    target_dirs = []
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            arg_path = os.path.abspath(arg)
            if os.path.isdir(arg_path):
                target_dirs.append(arg_path)
            elif os.path.isfile(arg_path) and arg_path.endswith('.txt'):
                total += 1
                try:
                    old_name = os.path.basename(arg_path)
                    result = reformat_file(arg_path)
                    if result:
                        processed += 1
                        new_name = os.path.basename(result)
                        if new_name != old_name:
                            renamed += 1
                    else:
                        errors += 1
                except Exception as e:
                    print(f"  ERROR processing {old_name}: {e}")
                    errors += 1
    else:
        # Default to all subdirectories in transcripts/
        for channel_dir in sorted(os.listdir(TRANSCRIPTS_DIR)):
            channel_path = os.path.join(TRANSCRIPTS_DIR, channel_dir)
            if os.path.isdir(channel_path):
                target_dirs.append(channel_path)

    for channel_path in target_dirs:
        channel_dir = os.path.basename(channel_path)
        print(f"\n=== Processing channel directory: {channel_dir} ===")
        
        files = sorted([f for f in os.listdir(channel_path) if f.endswith('.txt')])
        print(f"Found {len(files)} files")
        
        for filename in files:
            filepath = os.path.join(channel_path, filename)
            total += 1
            
            try:
                old_name = filename
                result = reformat_file(filepath)
                if result:
                    processed += 1
                    new_name = os.path.basename(result)
                    if new_name != old_name:
                        renamed += 1
                else:
                    errors += 1
            except Exception as e:
                print(f"  ERROR processing {filename}: {e}")
                errors += 1
    
    print(f"\n=== Summary ===")
    print(f"Total files: {total}")
    print(f"Processed: {processed}")
    print(f"Renamed: {renamed}")
    print(f"Errors: {errors}")

if __name__ == '__main__':
    main()
