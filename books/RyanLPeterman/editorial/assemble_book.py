#!/usr/bin/env python3
"""Assemble authored source sections; missing work stays visible in the coverage ledger."""
from pathlib import Path
import argparse, copy, importlib.util, json
BASE=Path(__file__).resolve().parents[1]
MANIFEST=json.loads((BASE/'prepared-v2/manifest.json').read_text())
FOLDER=MANIFEST['books'][0]
PARTS=[
 ('craft','Thinking, learning, and explaining','Clear reasoning starts before implementation. These conversations connect writing, mathematical models, teaching, and the habit of understanding what sits below an abstraction.'),
 ('languages','Languages, abstractions, and performance','Language creators make their tradeoffs visible: what a compiler can know, what a programmer must manage, and when a useful abstraction helps or hurts.'),
 ('systems','Building systems that survive reality','Large systems test more than a design on paper. Follow the choices around architecture, data movement, reliability, integration, and the responsibility to end a project that no longer works.'),
 ('ai','Engineering in the AI era','The guests disagree about speed, autonomy, and the future of programming. Their distinct arguments remain separate, with the assumptions and conditions that make each useful to examine.'),
 ('career','Growing as an individual contributor','Career stories reveal how scope, technical ownership, visibility, and timing interact. These are particular experiences and organizational practices, rather than a universal promotion formula.'),
 ('leadership','Leadership, influence, and organization','Technical work happens inside relationships and organizations. These sections examine decision-making, management, corporate politics, and the ways good intent can create unexpected effects.'),
 ('hiring','Hiring, interviews, and evaluation','Interview and calibration stories connect demonstrated skill with the imperfect processes used to assess it. Keep the examples and company context in view when applying a lesson.'),
 ('nonlinear','Choices, reinvention, and tradeoffs','A career can change direction, and a desired title can fail to deliver the life imagined behind it. These reflections make room for curiosity, setbacks, personal values, and the cost of a chosen pace.'),
 ('community','Behind the work','A small collection of creator and community accounts puts the interviews themselves in context.')]
# Curated thematic connections. These link related ideas without claiming that
# repeated clips are independent evidence or that every pair is an exact excerpt.
PAIRS=[
 ('source-86f26e37f38cf04d','source-4005a50ded85af4c'),
 ('source-deae94e8883282bf','source-3f6b5c7495d2c862'),
 ('source-fea7404eb5982785','source-eb789a15ce2c0992'),
 ('source-83ff6425ab4f55d4','source-eb789a15ce2c0992'),
 ('source-054cafd98518a73a','source-718685b697faad4b'),
 ('source-ee25ad8652ca7687','source-cf79d446a56a93e0'),
 ('source-1b6652cb04b62a22','source-6625b13a9321c984'),
 ('source-ee25ad8652ca7687','source-1b6652cb04b62a22'),
 ('source-c42eb00727bb6555','source-09f01df3be927a94'),
 ('source-c42eb00727bb6555','source-63f69eab0d205ab4'),
 ('source-46b2938c1a52173e','source-fb9e5bfc4e96bcc9'),
 ('source-320779e23fa412ba','source-80dcd202730f9f53'),
 ('source-db8ddf6fa0c9cddb','source-ad1b57c76cb679ce'),
 ('source-e763d45a670dd9ac','source-c5e5981897b441a1'),
 ('source-a0de28000368bd2f','source-fd3381490fc526e5'),
 ('source-14bee73b27dd46aa','source-fd3381490fc526e5'),
 ('source-64083bdf5826e9df','source-26f8143fe83dfc59'),
 ('source-64083bdf5826e9df','source-b9d36546f9e9bf11'),
 ('source-0a0a19a690dbea54','source-6625b13a9321c984'),
 ('source-8baa078aa4b5a40a','source-5f7cf6e81e665bd5'),
 ('source-7f09fb95f7d0e9d0','source-5f7cf6e81e665bd5'),
 ('source-c12bff19f1a9e9c6','source-ce5d21a3243dbd18'),
 ('source-a4c1c85d759dcef8','source-176a06af7f6bc865'),
 ('source-1f8e66c58d2a4c8b','source-dbce948925112d65'),
 ('source-c0a1ff552da11424','source-e0ba6d1b172ce120'),
 ('source-0b19b01a734b60d2','source-b3da78875be78b52'),
 ('source-c6e55d0a6948853b','source-e4725309875844e7'),
 ('source-99abc36ced59a4c3','source-e4725309875844e7'),
 ('source-21c7204c69a69356','source-11a9088fd11380a0'),
 ('source-21c7204c69a69356','source-b13f2c34fa23ff4d'),
 ('source-76673ebc5370f1bd','source-b13f2c34fa23ff4d'),
 ('source-583d88754f37877b','source-9d2b2514511729fb'),
 ('source-894cf0375c4d9944','source-b9d36546f9e9bf11'),
 ('source-0ff73d892aeb9a09','source-ba37f130205fc8b6'),
 ('source-d2182159ae32e297','source-238007c2e5a842c7'),
 ('source-3babf3fa4c27af3b','source-f55dd5f460ec58d2'),
 ('source-d23f1809e27bec76','source-4005a50ded85af4c'),
 ('source-d23f1809e27bec76','source-176a06af7f6bc865'),
 ('source-de97c799fd5897ae','source-db8ddf6fa0c9cddb'),
 ('source-de97c799fd5897ae','source-764a24a02d3960f9'),
 ('source-4195363691199609','source-764a24a02d3960f9'),
 ('source-4195363691199609','source-238007c2e5a842c7')]

def reading_words(value):
 # Count prose and visible diagram/table text, rather than JSON schema,
 # evidence coordinates, identifiers, or source paths.
 if isinstance(value,str):return len(value.split())
 if isinstance(value,list):return sum(reading_words(item) for item in value)
 if isinstance(value,dict):
  return sum(reading_words(item) for key,item in value.items() if key in {
   'title','deck','introduction','text','heading','label','question','answer',
   'caption','items','headers','rows','steps','blocks','followups'})
 return 0

def assemble(complete=False):
 wrappers={}
 for path in (BASE/'sections').glob('source-*.json'):
  wrapper=json.loads(path.read_text());identity=wrapper['coverage']['source_id']
  if identity in wrappers:raise ValueError(f'Duplicate authored source {identity}')
  wrappers[identity]=wrapper
 sources={s['id']:s for s in FOLDER['sources']}
 if not set(wrappers)<=set(sources):raise ValueError('Unexpected authored sources')
 if complete and set(wrappers)!=set(sources):raise ValueError(f"Still missing {len(set(sources)-set(wrappers))} sources")
 groups={theme:[] for theme,_,_ in PARTS};coverage=[];question_rounds=0;followups=0
 for source in FOLDER['sources']:
  identity=source['id']
  if identity not in wrappers:
   coverage.append({'source_id':identity,'sha256':source['sha256'],'reviewed_chunks':[],'status':'pending','reason':'Awaiting complete semantic reading and authored section.'});continue
  wrapper=wrappers[identity];coverage.append(wrapper['coverage']);section=copy.deepcopy(wrapper.get('section'))
  if section is None:continue
  theme=wrapper['editorial']['theme']
  if theme not in groups:raise ValueError(f'Unknown theme {theme}: {identity}')
  groups[theme].append(section)
  question_rounds+=sum(b['type']=='qa' for b in section['blocks'])
  followups+=sum(len(b.get('followups',[])) for b in section['blocks'])
 sections={s['id']:s for group in groups.values() for s in group}
 for a,b in PAIRS:
  if a in sections and b in sections:
   for first,second in [(a,b),(b,a)]:
    if second not in sections[first]['related']:sections[first]['related'].append(second)
 parts=[]
 for theme,title,intro in PARTS:
  group=groups[theme]
  if not group:continue
  # A foundation clip may precede a full interview in a learning path;
  # source titles are used only to make ordering deterministic within a theme.
  group.sort(key=lambda section:(0 if sources[section['source_id']]['word_count']<3500 else 1,section['title'].casefold()))
  parts.append({'id':'part-'+theme,'title':title,'introduction':intro,'sections':group})
 book={'version':1,'folder_id':FOLDER['folder_id'],'title':'The Engineering Judgment Library','subtitle':'Conversations on building software, growing a career, and deciding what matters.','language':'en','status':'complete' if complete else 'preview','introduction':[
  'Good engineering depends on more than producing code. It involves understanding the mechanism, choosing an appropriate design, making progress with other people, and deciding which outcomes deserve your effort. This reading edition brings together the Ryan Peterman transcript collection around those questions.',
  'Each source has its own section. Interviews retain the sequence of substantive questions and answers, with follow-ups attached to the discussion they extend. Spoken repetition, opening montages, sponsor messages, and channel housekeeping are condensed so the argument and examples can be read as prose. Source links return you to the relevant point in the original conversation.',
  'Read from foundations toward systems and organizational work, or use the contents and search to follow a particular question. Related-section links connect short clips with full conversations and contrasting views. The guests’ observations, predictions, and career experiences are presented in their own context; this edition does not turn them into one universal rule. Diagrams labeled editorial synthesis organize an explanation without pretending the speaker supplied that exact framework.'
 ],'parts':parts,'coverage':coverage,'ignored_files_reviewed':FOLDER.get('ignored_files',[])}
 spec=importlib.util.spec_from_file_location('renderer','/Users/yongjiexue/.codex/skills/transcript-to-book/scripts/render_book.py');renderer=importlib.util.module_from_spec(spec);spec.loader.exec_module(renderer)
 rendered=renderer.render(book,MANIFEST)
 (BASE/'book.json').write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n')
 (BASE/'book.html').write_text(rendered)
 progress={'folder_id':FOLDER['folder_id'],'status':book['status'],'source_count':len(sources),'source_words':FOLDER['word_count'],'language':'English','edition':'Detailed condensation','completed_sources':list(wrappers),'sources_reviewed':len(wrappers),'included_sections':len(sections),'excluded_sources':sum(e['status']=='excluded' for e in coverage),'question_rounds':question_rounds,'followup_count':followups,'summary_words':sum(reading_words(s) for s in sections.values())}
 (BASE/'editorial/progress.json').write_text(json.dumps(progress,indent=2)+'\n')
 print(json.dumps({k:v for k,v in progress.items() if k!='completed_sources'},indent=2))
 return book

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--complete',action='store_true');args=parser.parse_args();assemble(args.complete)
