import re
content = """
1. **他卖什么？**
**1. 他卖什么？**
1. **他卖什么？** (What do they sell?) - 销售多个
"""
matches = re.findall(r'^(?:1\.\s*\*\*他卖什么？\*\*|\*\*1\.\s*他卖什么？\*\*).*', content, flags=re.MULTILINE)
for m in matches:
    print(m)
