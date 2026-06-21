import sys
import os

if len(sys.argv) < 3:
    print("Usage: python3 save_summary.py [output_file_path] [summary_text_or_file]")
    sys.exit(1)

output_file = sys.argv[1]
arg2 = sys.argv[2]

# If the second argument is a file path and exists, read content from it
if os.path.exists(arg2):
    with open(arg2, 'r', encoding='utf-8') as f:
        summary_text = f.read()
else:
    summary_text = arg2

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Append summary
with open(output_file, 'a', encoding='utf-8') as f:
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        # Check if it already ends with the divider
        with open(output_file, 'r', encoding='utf-8') as check_f:
            check_content = check_f.read()
        if not check_content.strip().endswith("---"):
            f.write("\n\n---\n\n")
    f.write(summary_text.strip() + "\n")

print(f"Summary appended successfully to {output_file}.")
