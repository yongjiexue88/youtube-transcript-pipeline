import json,pathlib
P=pathlib.Path('books/RyanLPeterman')
S={s['id']:s for f in ['worker2.json','worker2-extra.json'] for s in json.load(open(P/'editorial'/f))['sources']}
def evidence(a,b): return [{'start':a,'end':b}]
def qa(q,a,x,y,followups=None,speaker=None):
 d={'type':'qa','question':q,'answer':a if isinstance(a,list) else [a],'evidence':evidence(x,y),'followups':followups or []}
 if speaker:d['speaker']=speaker
 return d
def follow(q,a,x,y):return {'question':q,'answer':a if isinstance(a,list) else [a],'evidence':evidence(x,y)}
def save(id,title,deck,blocks,theme,omissions=None,notes=''):
 s=S[id]
 obj={'section':{'id':id,'source_id':id,'title':title,'kind':'interview','deck':deck,'blocks':blocks,'related':[],'omissions':omissions or []},'coverage':{'source_id':id,'sha256':s['sha256'],'reviewed_chunks':[c['number'] for c in s['chunks']],'status':'included','reason':'Read every compact-reading chunk in order; preserved substantive exchanges and recorded repetitive trailer and housekeeping omissions.'},'editorial':{'theme':theme,'question_rounds':sum(b['type']=='qa' for b in blocks),'followup_count':sum(len(b.get('followups',[])) for b in blocks),'notes':notes}}
 (P/'sections'/f'{id}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 print(id,len(blocks),'blocks',sum(len(' '.join(b.get('answer',[])).split()) for b in blocks),'main answer words')
