from pathlib import Path
import json, importlib.util
BASE=Path(__file__).resolve().parents[1]
MANIFEST=json.loads((BASE/'prepared-v2/manifest.json').read_text())
FOLDER=MANIFEST['books'][0]
SOURCES={s['id']:s for s in FOLDER['sources']}
_spec=importlib.util.spec_from_file_location('book_renderer','/Users/yongjiexue/.codex/skills/transcript-to-book/scripts/render_book.py')
_renderer=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_renderer)
def seconds(v):
 if isinstance(v,(int,float)):return v
 n=0
 for x in v.split(':'):n=n*60+float(x)
 return n
def ev(a,b,label=None):
 d={'start':seconds(a),'end':seconds(b)}
 if label:d['label']=label
 return [d]
def p(text,a,b,heading=None):
 d={'type':'paragraph','text':text,'evidence':ev(a,b)}
 if heading:d['heading']=heading
 return d
def qa(question,answer,a,b,speaker=None,followups=None):
 d={'type':'qa','question':question,'answer':answer if isinstance(answer,list) else [answer],'evidence':ev(a,b),'followups':followups or []}
 if speaker:d['speaker']=speaker
 return d
def follow(question,answer,a,b,speaker=None):
 d={'question':question,'answer':answer if isinstance(answer,list) else [answer],'evidence':ev(a,b)}
 if speaker:d['speaker']=speaker
 return d
def flow(title,steps,caption,a,b):return {'type':'flow','title':title,'steps':[{'title':x,'text':y} for x,y in steps],'caption':caption,'editorial':True,'evidence':ev(a,b)}
def table(title,headers,rows,a,b):return {'type':'table','title':title,'headers':headers,'rows':rows,'evidence':ev(a,b)}
def callout(label,text,a,b):return {'type':'callout','label':label,'text':text,'evidence':ev(a,b)}
def write(identity,theme,title,kind,deck,blocks,omissions=None,notes='',excluded=False):
 source=SOURCES[identity]
 coverage={'source_id':identity,'sha256':source['sha256'],'reviewed_chunks':[c['number'] for c in source['chunks']],'status':'excluded' if excluded else 'included','reason':notes or 'All compact reading chunks read in full; substantive discussion paraphrased with source ranges.'}
 section=None if excluded else {'id':identity,'source_id':identity,'title':title,'kind':kind,'deck':deck,'blocks':blocks,'related':[],'omissions':omissions or []}
 if section:
  candidate={'version':1,'folder_id':FOLDER['folder_id'],'title':'Validation','subtitle':'Section validation','language':'en','status':'preview','introduction':['Section validation.'],'parts':[{'id':'test-part','title':'Test part','sections':[section]}],'coverage':[coverage]}
  _renderer.validate(candidate,MANIFEST)
 wrapper={'section':section,'coverage':coverage,'editorial':{'theme':theme,'question_rounds':sum(b['type']=='qa' for b in blocks),'followup_count':sum(len(b.get('followups',[])) for b in blocks),'notes':notes}}
 path=BASE/'sections'/f'{identity}.json';temporary=path.with_suffix('.tmp');temporary.write_text(json.dumps(wrapper,ensure_ascii=False,indent=2)+'\n');temporary.replace(path)
 print(identity,title)
