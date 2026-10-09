import bisect,json,re
from pathlib import Path
assignment=json.load(open('books/RyanLPeterman/editorial/worker3.json'))
assignment['sources'] += json.load(open('books/RyanLPeterman/editorial/worker3-extra.json'))['sources']
for src in assignment['sources']:
 p=Path('books/RyanLPeterman/sections')/(src['id']+'.json')
 if not p.exists():continue
 data=json.loads(p.read_text())
 stamps=[]
 for line in Path(src['reading_file']).read_text().splitlines():
  match=re.match(r'\[L\d+\] \[([\d:.]+)\]',line)
  if match:
   pieces=match.group(1).split(':'); stamps.append(round(sum(float(x)*60**i for i,x in enumerate(reversed(pieces))),2))
 stamps=sorted(set(stamps+[src['time_end']]))
 def walk(x):
  if isinstance(x,dict):
   for ev in x.get('evidence',[]):
    if 'start' in ev:
     assert src['time_start']<=ev['start']<=ev['end']<=src['time_end'],(src['id'],ev)
     ev['start']=stamps[max(0,bisect.bisect_right(stamps,ev['start'])-1)]
     ev['end']=stamps[min(len(stamps)-1,bisect.bisect_left(stamps,ev['end']))]
   for y in x.values():walk(y)
  elif isinstance(x,list):
   for y in x:walk(y)
 walk(data)
 p.write_text(json.dumps(data,indent=2))
 print(src['id'],len(data['section']['blocks']),sum(z['type']=='qa' for z in data['section']['blocks']))
