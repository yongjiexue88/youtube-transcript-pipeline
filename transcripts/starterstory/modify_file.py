import re

file_path = '/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/starterstory/date_batch_04.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: 0. **公司/产品名称：** [Name]
# Replace with: same line + \n0.5. **成立时间：** 未提及

new_content = re.sub(
    r'(0\.\s*\*\*公司/产品名称：\*\*\s*.*?)\n(1\.\s*\*\*他卖什么？\*\*)',
    r'\1\n0.5. **成立时间：** 未提及\n\2',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Modification done.")
