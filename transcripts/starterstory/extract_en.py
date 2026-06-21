import os

batch_file = "batch_05.txt"
with open(batch_file, "r") as f:
    files = [line.strip() for line in f if line.strip()]

for i, fname in enumerate(files):
    if not os.path.exists(fname):
        print(f"Missing {fname}")
        continue
    with open(fname, "r") as f:
        content = f.read()
    
    # Split by "## 中文翻译" to only get English
    en_content = content.split("## 中文翻译")[0]
    
    out_name = f"en_only_{i}.txt"
    with open(out_name, "w") as f:
        f.write(en_content)
    print(f"Saved {out_name} for {fname}")
