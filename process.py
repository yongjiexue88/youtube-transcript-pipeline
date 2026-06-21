import re

file_path = '/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/starterstory/summary_batch_01.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

names_map = {
    "9 Things That Make Me $1.8M/Year": "Starter Story",
    "Faceless: From Immigrant to $1M/Year": "未提及",
    "From Zero to $42K/Month in 90 Days with AI": "Code Guide",
    "He's Launching A New $1M Business Every Month": "未提及",
    "He Built A $2.5M/Year Business In 2 Years": "Draft.dev",
    "He Built A $600,000 One Person Business (with video editing)": "未提及",
    "He Made $10M with 3 iPhone Apps": "Riz GPT / Umax / Cal AI",
    "He Makes $125,000/year As A Niche YouTuber": "未提及",
    "He Quit His Job And Makes $10M/Year Writing Online": "Ship 30 for 30 / Premium Ghostwriting Academy / Write with AI / Typeshare",
    "He Turned $500 Into $10M": "Greek House / College Thread / Threadly / Athlete's Thread",
    "How I Built A $1M Business From This Starbucks": "Starter Story",
    "How I Built A $1M Business in 117 Days": "Chatbase",
    "How I Built It: $10K/Month AI Image Generator": "Potion",
    "How I Built It: $12K/Month Micro SaaS": "SiteGPT",
    "How I Built It: $15K/month Mobile App": "Habit Kit",
    "How I Built It: $17K/Month Open Source SaaS": "Postiz",
    "How I Built It: $20K/Month AI App as a Non-Technical Founder": "SheetsResume.com",
    "How I Built It: $20K/Month Chrome Extension": "Superpower ChatGPT",
    "How I Built It: $23K/month micro-saas": "Data Fetcher",
    "How I Built It: $30K/month Micro-SaaS (Subscribr Breakdown)": "Subscribr",
}

new_lines = []
current_title = ""

for line in lines:
    if line.startswith("# "):
        current_title = line.strip()[2:]
        new_lines.append(line)
    elif line.startswith("1. **他卖什么？**"):
        if current_title in names_map:
            name = names_map[current_title]
            new_lines.append(f"0. **公司/产品名称：** {name}\n")
        else:
            new_lines.append(f"0. **公司/产品名称：** 未提及\n")
        new_lines.append(line)
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done")
