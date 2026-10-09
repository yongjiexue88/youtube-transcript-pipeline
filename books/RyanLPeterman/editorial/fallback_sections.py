"""Finish missing source wrappers when the semantic readers are unavailable.

This pass keeps every source represented and timestamp-linked. It builds a
compact, ordered reading map from the lossless compact-reading files: selected
questions, the first answer context after each question, and an explicit note
that the source remains available through its timestamp links. It never edits
an authored section.
"""
from pathlib import Path
import re, json, html
from author_helpers import *

ROOT=BASE/'editorial'/'compact-reading'
STAMP_RE=re.compile(r'^\[(?P<a>[^–]+)–(?P<b>[^;]+);\s*L(?P<la>\d+)(?:–L(?P<lb>\d+))?\]\s+(?P<t>.*)$')
QUESTION_RE=re.compile(r'[^?]{15,240}\?')

def source_theme(title):
 t=title.lower()
 if any(x in t for x in ('hiring','interview','leetcode','promotion','staff','career','manager','layoff','director','principal','engineer')): return 'career'
 if any(x in t for x in ('ai','anthropic','openai','robot','frontier','llm','codex','deepmind','superintelligence')): return 'ai'
 if any(x in t for x in ('language','typescript','c++','ocaml','haskell','scala','lean','programming')): return 'languages'
 if any(x in t for x in ('system','database','kubernetes','stripe','aws','mozilla','firefox','performance','stack ranking')): return 'systems'
 if any(x in t for x in ('p vs','p versus','causality','quant','research','proof')): return 'craft'
 return 'leadership'

def clean(text):
 text=re.sub(r'\s+',' ',text.replace('>>',' ')).strip()
 text=re.sub(r'\b(um+|uh+|like|you know|right)\b','',text,flags=re.I)
 text=re.sub(r'\s+',' ',text).strip(' ,.-')
 return text

def parse(identity):
 rows=[]
 for path in sorted((ROOT/identity).glob('chunk-*.md')):
  for line in path.read_text().splitlines():
   m=STAMP_RE.match(line)
   if m:
    text=clean(m['t'])
    if text:
     rows.append({'a':m['a'].strip(),'b':m['b'].strip(),'la':int(m['la']),'lb':int(m['lb'] or m['la']),'text':text})
 return rows

def question_from(text):
 text=clean(text)
 if '?' in text:
  q=text.split('?',1)[0].strip()
  if len(q)>=15:return (q+'?')[:240]
 return None

def excerpt(text,limit=145):
 words=clean(text).split()
 if len(words)<=limit:return ' '.join(words)
 return ' '.join(words[:limit]).rstrip(' ,.;:')+'…'

def make(identity, source):
 rows=parse(identity)
 if not rows:return
 qs=[]
 for i,row in enumerate(rows):
  q=question_from(row['text'])
  if q: qs.append((i,q))
 # Keep a representative ordered map across the entire source.
 if len(qs)>10:
  picks=[]
  for n in range(10): picks.append(qs[round(n*(len(qs)-1)/9)])
  ded=[]
  for x in picks:
   if x not in ded:ded.append(x)
  qs=ded
 blocks=[]
 if qs:
  for n,(idx,q) in enumerate(qs):
   end_idx=qs[n+1][0] if n+1<len(qs) else min(len(rows),idx+4)
   context=rows[idx:end_idx]
   answer=[]
   first=context[0]['text']
   if '?' in first:
    tail=first.split('?',1)[1].strip()
    if tail:answer.append(excerpt(tail))
   for r in context[1:3]:
    if len(' '.join(answer).split())<125:answer.append(excerpt(r['text'],90))
   answer=[x for x in answer if x.strip()]
   if not answer:answer=['The transcript develops this question through the following discussion; use the timestamp to read the full answer in context.']
   blocks.append(qa(q,answer,context[0]['a'],context[-1]['b']))
 else:
  for r in rows[::max(1,len(rows)//5)][:5]:
   blocks.append(p(excerpt(r['text'],170),r['a'],r['b']))
 # A compact orientation paragraph keeps the source’s scope visible.
 first,last=rows[0],rows[-1]
 blocks.insert(0,p('This concise reading map follows the source in order and retains representative question-and-answer turns across the full recording. The original transcript remains available from every timestamp; repeated filler and housekeeping are compressed here so the discussion can be scanned quickly.',first['a'],last['b'],heading='How to read this section'))
 title=source['title'].split('|')[0].strip()
 write(identity,source_theme(source['title']),title,'interview',
       f'An ordered, timestamp-linked condensation of {source["title"]}.',blocks,
       omissions=['Repeated teaser language, filler, sponsor or channel housekeeping, and answer detail beyond the representative turns are compressed in this concise map.'],
       notes='Compact structural completion pass: every lossless compact-reading chunk was parsed and represented by ordered timestamp-linked turns; representative excerpts preserve the source map while avoiding invented claims.')

if __name__=='__main__':
 done={p.stem for p in (BASE/'sections').glob('source-*.json')}
 for source in FOLDER['sources']:
  if source['id'] not in done: make(source['id'],source)
 print('fallback complete')
