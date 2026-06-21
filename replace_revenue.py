import re

file_path = '/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/starterstory/revenue_batch_07.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
current_title = ""

for i, line in enumerate(lines):
    if line.startswith('#'):
        current_title = line.strip()
    
    new_lines.append(line)
    
    if line.startswith('0.5. **成立时间：**'):
        # Determine revenue from current_title
        revenue = "未提及"
        
        # Extract dollar amounts
        # e.g., $1.8M, $10M ARR, $25K/Month, $10M/Year, $30,000,000
        # We can write a custom mapping or regex
        title_lower = current_title.lower()
        
        if '1.8m' in title_lower: revenue = "$1.8M"
        elif '10m ai saas' in title_lower: revenue = "$10M ARR"
        elif '$1m mobile app' in title_lower: revenue = "$1M"
        elif '$25k/month' in title_lower: revenue = "$25K/Month"
        elif '$10m/year' in title_lower: revenue = "$10M/Year"
        elif '$10m portfolio' in title_lower: revenue = "$10M"
        elif '$1.7m' in title_lower: revenue = "$1.7M"
        elif '$1.5m/year' in title_lower: revenue = "$1.5M/Year"
        elif '$1m app maker' in title_lower: revenue = "$1M"
        elif '30,000,000' in title_lower: revenue = "$30,000,000"
        elif '$25m' in title_lower: revenue = "$25M"
        elif '$100m/year' in title_lower: revenue = "$100M/Year"
        elif '150m' in title_lower and '1,000' in title_lower: revenue = "$150M"
        elif '48m' in title_lower and '4,000' in title_lower: revenue = "$48M"
        elif 'reset_on_my_life' in title_lower: revenue = "未提及"
        elif '2m_business' in title_lower: revenue = "$2M"
        elif '1.4m／year' in title_lower: revenue = "$1.4M/Year"
        elif '25,000／month' in title_lower: revenue = "$25,000/Month"
        elif 'over_$1m' in title_lower: revenue = "超过$1M"
        elif '150k／year' in title_lower: revenue = "$150K/Year"
        elif '1.1b' in title_lower: revenue = "$1.1B"
        elif '40k／month' in title_lower: revenue = "$40K/Month"
        
        new_lines.append(f"0.8. **营收规模：** {revenue}\n")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done")
