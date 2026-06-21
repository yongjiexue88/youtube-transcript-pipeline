import re

file_path = "/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/starterstory/summary_batch_05.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

names = [
    "Follow Buddy",
    "Sheets & Giggles",
    "The Birdhouse",
    "finvsfin.com",
    "Paired",
    "Local Rank / Trackings.ai",
    "Unicorn Platform / SEO Bot / Listing Bot",
    "Stodzy Internet Marketing / Recovery Local / Copyblogger",
    "Packager",
    "Rummer / Parakeet AI / Optivase / Parakeet AI Apply Agent",
    "Marketing Examined / Content Examined / Social Examined",
    "《无路之路》（The Pathless Path）",
    "Oceans",
    "未提及",
    "Task Magic",
    "《Bake a Baby》/《Bathe a Baby》",
    "Stealth GPT",
    "Swim University",
    "Magi",
    "Algrow",
    "UseArtemis / StoryShort.ai / Capacity.so",
    "Bible Buddy / Magic Music / Toxic Traits / Pray Screen",
    "Pitch 2.0 / Onetap.ai / yourcoverletter.com / Recapg.com / Webdesigner.io / Softgen.ai",
    "未提及",
    "Go Polar / SunSeek / Posture AI / Tempo",
    "Bank Statement Converter",
    "Yataphone",
    "Audio Pen",
    "Starter Story"
]

def replacer(match):
    global idx
    name = names[idx]
    idx += 1
    original_text = match.group(0)
    prefix = f"0. **公司/产品名称：** {name}\n"
    return prefix + original_text

idx = 0
new_content = re.sub(r'^(?:1\.\s*\*\*他卖什么？\*\*|\*\*1\.\s*他卖什么？\*\*).*', replacer, content, flags=re.MULTILINE)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Replaced {idx} occurrences.")
