import json
import importlib.util
from pathlib import Path
BASE=Path('/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/books/RyanLPeterman')
A=json.load(open(BASE/'editorial/worker1.json'))
E=json.load(open(BASE/'editorial/worker1-extra.json'))
S={s['id']:s for s in A['sources']+E['sources']}
MANIFEST=json.load(open(BASE/'prepared-v2/manifest.json'))
SPEC=importlib.util.spec_from_file_location('book_renderer','/Users/yongjiexue/.codex/skills/transcript-to-book/scripts/render_book.py')
RENDERER=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RENDERER)
def validate_wrapper(wrapper):
 book={'version':1,'folder_id':MANIFEST['books'][0]['folder_id'],'title':'Section validation','subtitle':'A source-complete section','language':'English','status':'preview','introduction':['A validation-only preview.'],'parts':[{'id':'validation-part','title':'Validation','sections':[wrapper['section']]}],'coverage':[wrapper['coverage']]}
 RENDERER.validate(book,MANIFEST)
def ev(a,b): return [{'start':a,'end':b}]
def fu(question,answer,a,b,speaker=None):
 d={'question':question,'answer':answer if isinstance(answer,list) else [answer],'evidence':ev(a,b)}
 if speaker:d['speaker']=speaker
 return d
def qa(question,answer,a,b,followups=None,speaker='Guest',takeaway=None):
 d={'type':'qa','question':question,'answer':answer if isinstance(answer,list) else [answer],'speaker':speaker,'evidence':ev(a,b),'followups':followups or []}
 if takeaway:d['takeaway']=takeaway
 return d
def save(sid,title,deck,blocks,theme,omissions=None,notes='',kind='interview'):
 s=S[sid]
 omission_notes=[]
 for item in omissions or []:
  if isinstance(item,str):omission_notes.append(item)
  else:
   ranges=', '.join(f"{r['start']}–{r['end']} seconds" for r in item.get('evidence',[]))
   omission_notes.append(item['reason']+(f' Source ranges: {ranges}.' if ranges else ''))
 section={'id':sid,'source_id':sid,'title':title,'kind':kind,'deck':deck,'blocks':blocks,'related':[],'omissions':omission_notes}
 wrapper={'section':section,'coverage':{'source_id':sid,'sha256':s['sha256'],'reviewed_chunks':[c['number'] for c in s['chunks']],'status':'included','reason':'Read every complete compact chunk, preserving all caption words; condensed the full discussion in source order.'},'editorial':{'theme':theme,'question_rounds':sum(b['type']=='qa' for b in blocks),'followup_count':sum(len(b.get('followups',[])) for b in blocks),'notes':notes}}
 validate_wrapper(wrapper)
 path=BASE/'sections'/f'{sid}.json'
 path.write_text(json.dumps(wrapper,ensure_ascii=False,indent=2)+'\n')
 print(path.name,len(blocks),sum(len(b.get('followups',[])) for b in blocks))
