import re

file_path = '/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/starterstory/date_batch_07.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert `0.5. **成立时间：** 未提及` between 0 and 1.
# But we will do it smartly by finding the block and replacing it.
def replacer(match):
    name_line = match.group(1)
    name = match.group(2).strip()
    
    date_str = "未提及"
    if name == "FE International":
        date_str = "2010年左右"
    elif name == "Wishlist":
        date_str = "兼职开发了6年"
        
    return f"{name_line}\n0.5. **成立时间：** {date_str}"

# The regex matches:
# (0\. \*\*公司/产品名称：\*\* (.*?))
# followed by a newline and 1.
pattern = re.compile(r'(0\. \*\*公司/产品名称：\*\*\s*(.*?))(?=\n1\. \*\*他卖什么？\*\*)')

new_content = pattern.sub(replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated successfully.")
