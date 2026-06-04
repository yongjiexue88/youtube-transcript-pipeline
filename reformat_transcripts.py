#!/usr/bin/env python3
"""
Reformat YouTube transcript files from timestamped or plain text format to Markdown (.md) format.
- Strips timestamps like [00:00.00]
- Merges text into flowing paragraphs with improved heuristics for auto-generated captions
- Splits giant paragraphs (both timestamped and pre-formatted text) into readable chunks
- If the title is random letters (a YouTube video ID), generates a descriptive title from content
- Preserves original metadata in a clean Markdown table
- Converts files to .md format and deletes the original .txt files
"""

import os
import re
import sys
import shutil

# Folder where transcripts are located
TRANSCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "transcripts")

# Regex to detect YouTube video ID pattern (11 chars, alphanumeric + dash/underscore)
VIDEO_ID_PATTERN = re.compile(r'^[A-Za-z0-9_-]{5,15}$')

# Regex to match timestamp lines like [00:00.00]  text (handles 2+ digit minutes)
TIMESTAMP_LINE = re.compile(r'^\[(\d{2,}:\d{2}\.\d{2})\]\s*(.*)')

def is_random_title(title):
    """Check if the title looks like a YouTube video ID rather than a real title."""
    title = title.strip()
    # YouTube video IDs are typically 11 characters of [A-Za-z0-9_-]
    if VIDEO_ID_PATTERN.match(title):
        return True
    return False

def extract_title_from_content(lines, language, has_timestamps=True):
    """Generate a descriptive title from the first few lines of content."""
    # Collect the first ~300 characters of content to derive a title
    content_text = []
    for line in lines:
        if has_timestamps:
            match = TIMESTAMP_LINE.match(line.strip())
            if match:
                text = match.group(2).strip()
                if text:
                    content_text.append(text)
        else:
            text = line.strip()
            if text:
                content_text.append(text)
                
        if len(' '.join(content_text)) > 300:
            break
    
    if not content_text:
        return None
    
    # For Chinese content, take the first meaningful sentence
    if 'zh' in language:
        # Chinese: look for the first complete thought (usually within first few lines)
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
    # Replace problematic characters with full-width equivalents or underscores
    safe = title.replace('/', '／').replace('\\', '＼')
    safe = safe.replace(':', '：').replace('*', '＊')
    safe = safe.replace('?', '？').replace('"', '"')
    safe = safe.replace('<', '＜').replace('>', '＞')
    safe = safe.replace('|', '｜').replace('\n', ' ')
    safe = safe.replace('\r', '')
    safe = re.sub(r'\s+', '_', safe.strip())
    # Limit length
    if len(safe) > 120:
        safe = safe[:120]
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

def split_giant_paragraph(text, language):
    """Split a giant paragraph into smaller, more readable paragraphs."""
    if 'zh' in language.lower():
        # Chinese: split by punctuation or character count
        if re.search(r'[。？！]', text):
            sentences = re.split(r'([。？！])', text)
            paragraphs = []
            current = ""
            for i in range(0, len(sentences)-1, 2):
                sentence = sentences[i] + sentences[i+1]
                current += sentence
                if len(current) > 180:
                    paragraphs.append(current.strip())
                    current = ""
            if current:
                paragraphs.append(current.strip())
            return paragraphs if paragraphs else [text]
        else:
            # No punctuation: split by length (around 150 chars)
            paragraphs = []
            for i in range(0, len(text), 150):
                paragraphs.append(text[i:i+150].strip())
            return paragraphs
    else:
        # English:
        # If there's punctuation:
        if re.search(r'[.?!](?:\s|$)', text):
            sentences = re.split(r'([.?!]\s+)', text)
            paragraphs = []
            current = ""
            sentence_count = 0
            for i in range(0, len(sentences)-1, 2):
                sentence = sentences[i] + sentences[i+1]
                current += sentence
                sentence_count += 1
                if sentence_count >= 4 or len(current.split()) > 100:
                    paragraphs.append(current.strip())
                    current = ""
                    sentence_count = 0
            if current:
                paragraphs.append(current.strip())
            return paragraphs if paragraphs else [text]
        else:
            # No punctuation: split on transitions and clause boundaries, aiming for 70-100 words per paragraph
            words = text.split()
            paragraphs = []
            current_words = []
            
            boundary_words = {
                "the", "this", "these", "first", "next", "another", "if", "when", 
                "but", "and", "so", "then", "because", "after", "before", "once",
                "we", "you", "they", "he", "she", "i", "it", "please", "thanks", 
                "let's", "there"
            }
            
            for word in words:
                current_words.append(word)
                if len(current_words) > 70 and word.lower().strip(',.?!') in boundary_words:
                    last_word = current_words.pop()
                    paragraphs.append(' '.join(current_words))
                    current_words = [last_word]
                    
            if current_words:
                paragraphs.append(' '.join(current_words))
            return paragraphs

def reformat_file(filepath):
    """Reformat a single transcript file (.txt or .md) to Markdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    title = ""
    video_id = ""
    url = ""
    language = ""
    generated = ""
    saved_at = ""
    content_lines = []
    
    is_md = filepath.endswith('.md')
    
    if is_md:
        # Parse existing Markdown file metadata
        separator_found = False
        for line in lines:
            line_str = line.strip()
            if line_str.startswith("# "):
                title = line_str[2:].strip()
            elif line_str.startswith("| **Video ID** |"):
                match = re.search(r'`(.*?)`', line_str)
                if match:
                    video_id = match.group(1)
            elif line_str.startswith("| **URL** |"):
                match = re.search(r'\[Watch on YouTube\]\((.*?)\)', line_str)
                if match:
                    url = match.group(1)
            elif line_str.startswith("| **Language** |"):
                parts = line_str.split('|')
                if len(parts) >= 3:
                    language = parts[2].strip()
            elif line_str.startswith("| **Type** |"):
                parts = line_str.split('|')
                if len(parts) >= 3:
                    generated = parts[2].strip()
            elif line_str.startswith("| **Saved At** |"):
                parts = line_str.split('|')
                if len(parts) >= 3:
                    saved_at = parts[2].strip()
            elif line_str == "---":
                separator_found = True
                # Read content from the line after '---'
                idx = lines.index(line) if line in lines else [i for i, l in enumerate(lines) if l.strip() == "---"][0]
                content_lines = lines[idx+1:]
                break
        
        if not separator_found:
            content_lines = lines
    else:
        # Parse traditional Text file structure
        separator_found = False
        header_end = 0
        for i, line in enumerate(lines):
            if line.strip() == '-' * 60:
                separator_found = True
                header_end = i + 1
                header_lines = [l.strip() for l in lines[:i]]
                break
        
        if not separator_found:
            print(f"  WARNING: No separator found in {filepath}, skipping")
            return None
        
        content_lines = lines[header_end:]
        
        # Extract metadata from header
        metadata = {}
        for line in header_lines:
            if ':' in line:
                parts = line.split(':', 1)
                metadata[parts[0].strip()] = parts[1].strip()
                
        title = metadata.get("Title", "")
        video_id = metadata.get("Video ID", "")
        url = metadata.get("URL", f"https://www.youtube.com/watch?v={video_id}" if video_id else "")
        language = metadata.get("Language", "")
        generated = metadata.get("Generated", "")
        saved_at = metadata.get("Saved at", "")
    
    # Check if content lines contain timestamps
    has_timestamps = False
    all_content_text = ""
    for line in content_lines:
        line_str = line.strip()
        if not line_str:
            continue
        match = TIMESTAMP_LINE.match(line_str)
        if match:
            has_timestamps = True
            all_content_text += " " + match.group(2)
        else:
            all_content_text += " " + line_str
            
    # Check if title needs replacement
    new_title = None
    if is_random_title(title):
        new_title = extract_title_from_content(content_lines, language, has_timestamps)
        if new_title:
            print(f"  Generated title: '{new_title}' (was: '{title}')")
            title = new_title
            
    formatted_paragraphs = []
    
    if has_timestamps:
        # Determine if this transcript lacks punctuation
        has_punctuation = False
        if re.search(r'[.?!](?:\s|$)', all_content_text) or ('zh' in language.lower() and re.search(r'[。？！]', all_content_text)):
            has_punctuation = True

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
                
                start_new = False
                
                if prev_timestamp and current_paragraph:
                    pause = get_pause_duration(prev_timestamp, timestamp)
                    
                    if not has_punctuation:
                        # Auto-generated transcript paragraph heuristic:
                        words_in_para = len(' '.join(current_paragraph).split())
                        if 'zh' in language.lower():
                            chars_in_para = len(''.join(current_paragraph))
                            if pause > 2.0:
                                start_new = True
                            elif pause > 1.0 and chars_in_para > 150:
                                start_new = True
                        else:
                            if pause > 2.0:
                                start_new = True
                            elif pause > 1.0 and words_in_para > 80:
                                start_new = True
                    else:
                        # Punctuated transcript heuristic:
                        if pause > 3.0:
                            start_new = True
                        elif pause > 1.5:
                            last_text = current_paragraph[-1]
                            if is_sentence_end(last_text, language):
                                start_new = True
                
                if start_new and current_paragraph:
                    paragraphs.append(current_paragraph)
                    current_paragraph = []
                
                current_paragraph.append(text)
                prev_timestamp = timestamp
            else:
                if line.strip():
                    current_paragraph.append(line.strip())
        
        if current_paragraph:
            paragraphs.append(current_paragraph)
        
        # Join fragments in each paragraph
        for para in paragraphs:
            if 'zh' in language.lower():
                joined = ''
                for text in para:
                    if joined and text:
                        last_char = joined[-1]
                        first_char = text[0]
                        needs_space = (
                            (last_char.isascii() and last_char.isalnum() and 
                             first_char.isascii() and first_char.isalnum()) or
                            (last_char.isascii() and last_char.isalnum() and not first_char.isascii()) or
                            (not last_char.isascii() and first_char.isascii() and first_char.isalnum())
                        )
                        if needs_space:
                            joined += ' '
                    joined += text
                formatted_paragraphs.append(joined)
            else:
                formatted_paragraphs.append(' '.join(para))
    else:
        # Already reformatted plain text — load non-empty lines as paragraphs
        formatted_paragraphs = [line.strip() for line in content_lines if line.strip()]
        
    # Split giant paragraphs into smaller readable paragraphs
    final_paragraphs = []
    for para in formatted_paragraphs:
        is_too_long = False
        if 'zh' in language.lower():
            if len(para) > 200:
                is_too_long = True
        else:
            if len(para.split()) > 100:
                is_too_long = True
                
        if is_too_long:
            split_paras = split_giant_paragraph(para, language)
            final_paragraphs.extend(split_paras)
        else:
            final_paragraphs.append(para)
            
    # Build Markdown output
    output = []
    output.append(f"# {title}\n\n")
    output.append("| Metadata | Value |")
    output.append("| :--- | :--- |")
    output.append(f"| **Video ID** | `{video_id}` |")
    output.append(f"| **URL** | [Watch on YouTube]({url}) |")
    output.append(f"| **Language** | {language} |")
    output.append(f"| **Type** | {generated} |")
    output.append(f"| **Saved At** | {saved_at} |")
    output.append("\n---\n")
    
    for para in final_paragraphs:
        output.append(para + "\n")
        
    # Determine output filename
    old_basename = os.path.basename(filepath)
    name_no_ext = os.path.splitext(old_basename)[0]
    
    # Extract language suffix from old filename if it's there
    lang_suffix = ''
    lang_match = re.search(r'_([a-z]{2}(?:-[a-zA-Z0-9]+)?)$', name_no_ext)
    if lang_match:
        lang_suffix = '_' + lang_match.group(1)
        clean_name = sanitize_filename(title)
        if clean_name.endswith(lang_suffix):
            clean_name = clean_name[:-len(lang_suffix)]
        new_basename = clean_name + lang_suffix + '.md'
    else:
        new_basename = sanitize_filename(title) + '.md'
        
    new_filepath = os.path.join(os.path.dirname(filepath), new_basename)
    
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
        
    # If the file extension changed or it was renamed, remove the original file
    if new_filepath != filepath and os.path.exists(filepath):
        os.remove(filepath)
        print(f"  Converted/Renamed: {old_basename} -> {new_basename}")
    elif new_filepath == filepath:
        print(f"  Updated: {old_basename}")
        
    return new_filepath

def main():
    if not os.path.exists(TRANSCRIPTS_DIR):
        print(f"Error: {TRANSCRIPTS_DIR} does not exist.")
        sys.exit(1)

    total = 0
    processed = 0
    errors = 0
    renamed = 0
    
    target_dirs = []
    # Check if specific arguments (files/folders) are passed
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            arg_path = os.path.abspath(arg)
            if os.path.isdir(arg_path):
                target_dirs.append(arg_path)
            elif os.path.isfile(arg_path) and (arg_path.endswith('.txt') or arg_path.endswith('.md')):
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
        # Default: scan all folders under transcripts/
        for channel_dir in sorted(os.listdir(TRANSCRIPTS_DIR)):
            channel_path = os.path.join(TRANSCRIPTS_DIR, channel_dir)
            if os.path.isdir(channel_path):
                target_dirs.append(channel_path)

    for channel_path in target_dirs:
        channel_dir = os.path.basename(channel_path)
        print(f"\n=== Processing channel directory: {channel_dir} ===")
        
        # Scan for both .txt and .md files
        files = sorted([f for f in os.listdir(channel_path) if f.endswith('.txt') or f.endswith('.md')])
        print(f"Found {len(files)} files to check/reformat")
        
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
    print(f"Total files checked: {total}")
    print(f"Updated/Converted: {processed}")
    print(f"Errors: {errors}")

if __name__ == '__main__':
    main()
