import json
from pathlib import Path
s=json.load(open('books/RyanLPeterman/editorial/worker3.json'))['sources'][1]
b=[]
def f(q,a,x,y):return {'question':q,'answer':a,'speaker':'Ricky','evidence':[{'start':x,'end':y}]}
def q(q,a,x,y,fs=[]):b.append({'type':'qa','question':q,'answer':a,'speaker':'Ricky','evidence':[{'start':x,'end':y}],'followups':fs})
q('What was the overall promotion and compensation timeline?',[
'Ricky joined Google as a new graduate in 2017 after an internship. He reports approximately $180,000 annual compensation plus a signing bonus, then promotion to L4 after a year and a half at about $250,000, L5 after another year and a half at roughly $350,000, and L6 three years later at roughly $500,000–$520,000. The amounts are retrospective figures from his own situation, including equity effects, rather than current compensation guarantees.',
'He credits a fortunate team match and considers reaching senior in three years faster than the typical path he observed. Staff took longer and involved a different kind of responsibility. The career story combines his deliberate work with opportunities he did not control.'
],43.28,149.76)
q('What happened in the junior-to-midlevel promotion process?',[
'In the review system Ricky describes, ratings arrived every six months. He first met expectations, then exceeded them, and received a still stronger rating alongside promotion. He believed his impact and independence matched the next level but worried that short tenure might count against him. His manager supported the attempt.'
],142.12,236.24,[f('Who should initiate promotion discussions?',[
'He recommends employee initiative supported by an ongoing conversation with the manager. He regularly asked whether his current projects demonstrated the next level and aligned expectations about timing and scope. Managing upward made an accelerated path more deliberate; it was not a promotion that arrived without discussion.'
],192.2,268.08)])
q('What behavior made the first promotion possible?',[
'Independence: finishing projects with less handholding and finding ways to unblock himself. This did not mean refusing to ask anyone for help. It meant learning enough to move the project without requiring the manager to solve every obstacle.'
],260.0,289.6,[f('How did you become better at unblocking yourself?',[
'He deliberately asked questions despite fearing he would look incompetent. His alternative was worse: staying silent, learning nothing, and failing to deliver. Colleagues generally wanted him to succeed. Asking the knowledgeable engineer helped him learn to do the work himself.',
'They recommend a real attempt before asking, but not remaining motionless for half a day or longer. Repeatedly asking the same question or receiving the same code-review feedback without improvement is different from healthy learning. The desired pattern is increasing independence and fewer repeated mistakes over time.'
],289.6,425.4)])
q('What changed when working toward senior?',[
'He became the owner and go-to person for a defined area, learning its code and delivering several impactful projects there. Ownership meant being able to answer questions and advance the area, not merely shipping more isolated changes.'
],425.4,475.2,[f('Did you choose the area through an explicit promotion plan?',[
'At first he simply found a part of the advertising experience visually unappealing and interesting to improve. The improvements could also produce measurable impact. Repeated projects and exploration gradually made him the owner, rather than a manager initially assigning a complete senior-level charter.'
],456.2,526.0),f('Did you have to compete for that scope?',[
'His team allowed engineers to choose many of their own projects. He sought work with meaningful impact and enough challenge to extend his skills. He recognizes that managers may assign useful work too, but relying only on assignments would not necessarily supply the scope needed for his desired growth.'
],509.16,571.48)])
q('How did you recognize projects that were genuinely at the next level?',[
'He studied teammates’ successful senior promotions to understand the scope and complexity expected, generated comparable ideas, and asked his manager to calibrate them. Roughly a year before his promotion he proposed a roadmap and asked whether completing it would meet the bar.',
'This gave the manager something concrete to assess and made the growth plan explicit. The roadmap emerged after approximately six months of exploration following L4, rather than immediately on the day of that promotion.'
],551.48,666.76,[f('When did you put that roadmap together?',[
'After the midlevel promotion he tried different projects and learned what interested him. He then wrote the one-year plan himself and sought managerial buy-in. Exploration preceded the more committed roadmap.'
],621.0,666.76)])
q('What did you do when requested work did not advance that roadmap?',[
'He learned to say no to unrelated projects that consumed time without helping him grow. He distinguishes that from accountability: a bug he caused, or a bug within his owned area, still needed attention. A new request could also be worth accepting if its impact and scope were stronger than the existing plan.'
],669.08,721.4,[f('How can someone say no without damaging the relationship?',[
'For an outside request he would bring the tradeoff to his manager and understand why it was assigned. For the manager’s own request he would ask whether it was required and explain the competing projects’ impact and growth value. This is a discussion of priorities, not a license to ignore obligations.',
'He believes managers should try to match important work with reports’ growth and interests. His own early record of finding and delivering projects earned trust, although the manager continued to guide which ideas were useful.'
],723.84,821.8)])
q('How did you learn which ideas would have impact?',[
'First define what the organization values. In his advertising area, revenue was a central metric, alongside whether the work helped users, advertisers, and publishers. Other teams might care about active users or product interactions. Running experiments exposed gaps where improvements could move the relevant outcome.',
'He found measurable results persuasive in arguments about project value. His emphatic statement that numbers settle the matter belongs to his experience in a revenue-measured area; it should not be treated as a claim that every engineering contribution is captured by one number.'
],815.36,919.52)
q('How did the senior promotion itself feel?',[
'It felt more uncertain than the first promotion. Ricky believed he was ahead of the timing commonly observed around him and worried that the committee might want a longer record of next-level work. His manager supported submitting while setting realistic expectations that it could fail. It succeeded on the first attempt, which Ricky describes as fortunate.'
],911.56,985.88)
q('Were there growing pains in becoming a leader?',[
'Yes. Handing project ideas to junior engineers made him anxious about whether experiments would succeed; some did not. He had to become comfortable with a portfolio of ideas rather than expect every one to work. A comparatively good success rate, mentoring, and positive influence on other people’s projects supported the case, while confidence developed through practice.'
],986.0,1062.6)
q('Did you feel stuck waiting for staff?',[
'Rather than wishing it had arrived sooner, he sometimes wishes the opportunity came later. Senior offered more flexibility for breaks and personal activities, whereas broader projects created meetings and a more rigid schedule. He advises looking at the actual calendars and work of nearby staff engineers before deciding the trade is desirable.'
],1042.6,1112.12,[f('Is staff required by an up-or-out policy?',[
'In the Google context he describes, senior engineers could stay at senior without an expectation to advance to staff. He is less sure about whether the same applies at midlevel. He frames staff as a choice to take on more responsibility rather than an obligatory badge of success.'
],1112.12,1161.08)])
q('What was the biggest difference between your senior and staff work?',[
'At senior he knew and owned a space and delivered projects within it. Toward staff he challenged the boundaries of that space, questioned the established direction, and guided consequential decisions across teams and functions. Some changes required senior-leadership buy-in. Knowing an area became a platform for shaping where it should go, rather than only operating effectively inside it.'
],1134.56,1217.08)
q('How did you find the anchor project for staff?',[
'Deep familiarity made him question practices that no longer made sense. In one example, established user research supported a conclusion but product experiments contradicted it. He pushed the evidence that another direction could produce greater impact. He does not disclose the specific product decision, so the lesson remains about examining assumptions and reconciling conflicting evidence rather than a reproducible advertising tactic.'
],1200.0,1263.52)
q('How did you influence other teams and partners?',[
'He had developed a reputation for finding impactful projects. He shared ideas, collaborated without trying to displace others, and turned proposals into projects that launched successfully. Relationships and repeated results gave his judgment weight.'
],1265.56,1420.6,[f('Did your previous results make that easier?',[
'Yes. Trust would have been harder to build if the projects repeatedly failed. Staying in the same organization let colleagues accumulate evidence of his work, whereas a new senior hire would need to establish that record. Ricky is cautious about the host’s description of him as a rising star but agrees that past successes made his proposals more credible.'
],1324.8,1420.6)])
q('Why did you want to try management?',[
'He already enjoyed helping colleagues grow, finding projects for them, and seeing them succeed. A formal management opportunity appeared after he had expressed that interest, and the team supported it. Fulfillment in developing others was the principal motivation.'
],1405.96,1475.04,[f('Did the manager closely vet your motivation first?',[
'He does not remember a formal process of that kind. He had raised the aspiration earlier, and the right opportunity eventually appeared. Becoming a manager young felt awkward at times.'
],1459.44,1515.04),f('What did feeling insufficiently mature mean?',[
'He felt younger than the more experienced managers around him and encountered an unfamiliar social-boundary issue when seeing reports at a music festival while drunk. He thinks it was probably fine, but it illustrated situations he had not anticipated before taking the role.'
],1516.6,1562.2),f('Was there prior management experience or a structured preparation path?',[
'He does not describe prior formal management experience and was surprised by how much learning happened after entering the role. Google had many resources, but he had expected a more structured guide to becoming effective. The earlier discussion of informal mentoring should not be mistaken for having already held the full manager job.'
],1564.76,1619.2)])
q('What changed most between IC leadership and management?',[
'Technical leadership supplied enjoyable elements of helping people succeed. Formal management added difficult performance feedback, review writing, and calibration overhead. At the same time, seeing an actual report get promoted felt especially rewarding because he had direct responsibility for supporting that growth.'
],1610.0,1678.28)
q('Do you regret becoming a manager?',[
'He mainly wishes it had happened later. In an unusual period with around twenty new hires, he was informally helping many of them; becoming the formal manager of four narrowed that responsibility and gave some time back. Nevertheless, he would have liked a few more years of senior-level flexibility and lower stress.',
'He now better understands what higher-level work entails: much of the influence is through other people, so meetings increase whether one is an IC or manager. A nine-to-five calendar can still be an intensely committed day with little discretion about naps or gym trips. Ryan adds that fragmented daytime meetings pushed his own technical work into evenings after reaching staff. The title’s appeal should be assessed against its daily experience.'
],1660.0,1832.36)
q('Was the staff promotion different from the previous applications?',[
'He again felt uncertain despite sustained top ratings. Moving from senior to staff could feel like a job change: being an exceptional senior with high impact did not automatically prove readiness for the broader role. A supportive manager and a successful first submission made the outcome fortunate.'
],1835.32,1949.4,[f('Did every promotion succeed on the first attempt?',[
'Yes. He did not experience a rejection-and-resubmission cycle at any of these stages and repeatedly acknowledges the luck in that record.'
],1920.0,1949.4)])
q('Could you repeat that career path, or did luck explain much of it?',[
'He benefited from enjoying the team he was matched into, organizational stability, and managers able to support him. Reorganizations, poor fit, or a manager’s absence could have delayed otherwise good work. He separates the chance that an opportunity appears from being prepared to use it. Effort helped with the second; it did not fully control the first.'
],1934.72,2018.84,[f('How much was ability and how much luck?',[
'He offers a rough fifty-fifty impression rather than a measured estimate. He feels confident he would eventually have reached senior with continued growth and effort, but another team might have required a move and a new ramp-up. His speed depended on the unusually good fit. Ryan notes that even a stronger engineer can struggle in an organization with repeated disruption.'
],2010.96,2108.08)])
q('Why stay at Google for seven years?',[
'He regularly reassessed whether he enjoyed the work and whether the team still offered what he wanted: growth, travel, and work that was sufficiently interesting. Staying was an active decision, not proof that he never considered alternatives. He also acknowledges survivorship bias: people without comparable growth or fit might have had good reasons to leave.',
'Ryan describes the accumulated advantage of staying in a healthy setting: relationships, code knowledge, and organizational context can expand from expertise in one area to many. That momentum can enable unusually fast growth, while changing employers can offer other benefits. They do not reduce the choice to a universal rule about job hopping.'
],2111.56,2275.8)
q('What advice would you give your new-graduate self?',[
'Trust his judgment more and try boundary-pushing ideas earlier. Anxiety made him postpone ideas he later pursued successfully. He believes earlier confidence could have reduced stress and enabled more experimentation, though he developed it gradually through results and good feedback.'
],2247.44,2326.8,[f('Was the impostor feeling about technical ability?',[
'He worried that he had been hired for personality rather than ability because his interview and internship had not felt spectacular. At low levels he also lacked a way to judge his own performance. Repeated reassurance that he was doing fine did not answer his internal question of whether that meant barely passing or excelling. Successful projects and collaboration eventually supplied more convincing evidence.'
],2328.44,2428.2)])
for x in b:
 for e in x['evidence']:
  assert 0<=e['start']<=e['end']<=s['time_end']
out={'section':{'id':s['id'],'source_id':s['id'],'title':'Choose the staff role with its responsibilities in view','kind':'interview','deck':'Ricky explains a fast Google promotion path built on ownership and measurable impact, while questioning whether faster advancement always improves daily life.','blocks':b,'related':[],'omissions':['The opening trailer at 00:00–00:41 is summarized only through the later full discussion.','Closing social links, channel promotion, production feedback, and farewell at 00:40:28–00:41:57 are omitted.']},'coverage':{'source_id':s['id'],'sha256':s['sha256'],'reviewed_chunks':[1,2,3,4],'status':'included','reason':'Read all four compact chunks in full and retained all substantive initiating questions and ordered follow-ups.'},'editorial':{'theme':'career','question_rounds':len(b),'followup_count':sum(len(z['followups']) for z in b),'notes':'Compensation and promotion timing describe the guest’s historical situation. His uncertainty about midlevel terminal status and mixed recollections about informal intern mentoring versus prior formal management experience are preserved without supplying a rule.'}}
Path('books/RyanLPeterman/sections/'+s['id']+'.json').write_text(json.dumps(out,indent=2))
