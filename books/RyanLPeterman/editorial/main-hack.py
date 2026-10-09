from author_helpers import *

write('source-ca7d69f79eef10a3','career','From producing code to choosing the right problem','interview',
 'Dwayne Reeves’s growth on Hack shows how migration strategy, trusted types, delegation, and approachable leadership can create value beyond personal code output.',[
 qa('Why did you join Facebook as a new graduate?',[
 'Facebook was not his original goal. Google appealed partly because of its East Coast offices, and Twitter because he liked Scala. A friend at Facebook persuaded him to interview as practice. Meeting engineers changed his view: behind the website were interesting problems in caching, scale, and a custom PHP runtime.',
 'He also felt wanted. The offer was his strongest, the recruiter increased it without a request, and a senior company leader met accepted MIT graduates personally. He contrasts that experience with another recruiter’s response in his own process. These examples describe his recruiting experience at the much smaller company of that period.'
 ],'00:32.88','04:50.48','Dwayne Reeves'),
 qa('How much does college prestige affect later success?',[
 'He values the education he received at MIT, but sees access to opportunity as the clearest differentiator. Recruiters were willing to speak to him from his first year; an early internship also helped open the next opportunity.',
 'He worked with equally capable engineers from other educational paths, including people who had not attended college, whose entry into the company depended much more on chance. His point is that recognizable credentials can open doors without defining the person’s eventual engineering ability.',
 'That access was striking to someone raised in Bridgeport, Connecticut, in public schools and a family of immigrants. Companies he had regarded as distant dreams became normal places for classmates to intern.'
 ],'04:52.24','07:11.36','Dwayne Reeves'),
 qa('How did you end up working on programming languages?',[
 'His first team was building a service and a custom language to move some computation out of the main PHP codebase and closer to data. He initially translated PHP into the new DSL, then developed language features. The project was eventually canceled.',
 'He moved into privacy infrastructure, representing policies more clearly than chains of conditionals. That framework adopted Hack and types early. Later, he tried to add Hack types to a core API originally designed without them. What looked like one or two weeks of work took a quarter and involved considerable scripting and collaboration with the Hack team.',
 'He reports that migration exposed errors in roughly 20% of the moved call sites, often involving null handling. The result made types’ value concrete at scale and strengthened the case for broader Hack adoption. It was an outcome from that migration, rather than a prediction that every codebase would show the same error rate.'
 ],'07:13.44','10:36.40','Dwayne Reeves'),
 qa('Are statically typed languages objectively better for industry work?',[
 'He calls the judgment subjective, while making a strong case for types in a large, shared codebase. As code and contributors multiply, keeping every assumption in one person’s head becomes impractical. Types communicate intent and help tools track that intent.',
 'Autocomplete, search, and static analysis add value beyond error messages. He allows that a person working alone might move quickly in a dynamic language; his argument concerns the communication burden at organizational scale.',
 'Peterman summarizes the mechanism as making more state and intent explicit in code so tools can inspect it. Reeves agrees, emphasizing the power of ruling out particular classes of errors by construction. That is a guarantee about what the type system establishes, rather than proof that the entire program has no bugs.'
 ],'10:37.12','13:16.48','Dwayne Reeves'),
 qa('What is the uncanny valley of type systems?',[
 'A partially typed language can look familiar enough to invite expectations from a fully static language, while behaving differently in subtle places. Developers may become more uncomfortable as the system approaches the expected behavior without actually supplying its guarantees.',
 'He used the graphics analogy to explain the transition problem on Hack. It gave the team a shared way to describe why almost-reliable types could still be frustrating.',
 'There was also a specific technical source of the gap: some inherited PHP behaviors conflicted with making the checker sound. He argued for removing those behaviors so that annotations could become dependable. The goal was not simply to maximize the number of written types while preserving exceptions that undermined their meaning.'
 ],'13:17.36','16:07.52','Dwayne Reeves'),
 qa('Which experiences changed your idea of how an individual contributor creates value?',[
 'The first was a broader PHP-to-Hack migration. He spent much of a half talking to engineers, identifying useful work, and helping people contribute, while writing less code himself. At first he thought this was his worst period. His manager initially suggested he find more time to code, then revised that advice to focus on the outcome.',
 'Adoption grew from roughly 20–30% to 60–70% of the codebase in his recollection, and Hack became a default choice. He received his highest review so far and a promotion to IC5. The result challenged his assumption that personal code volume defined his contribution: the job was to identify and solve problems, sometimes through clarity and coordination.',
 'The second came after he joined the Hack team as technical lead. With much of the previous team gone, he was learning what that role meant. He designed changes to the collection system, secured runtime-team agreement, and saw implementation begin. He wanted to finish the project himself as a route to IC6.',
 'His manager asked him to hand it off. The analogy was a staged rocket: Reeves had done the work of getting the effort moving; another person could carry the next stage. He reluctantly delegated and moved to another problem, then learned he had already been promoted. In both cases, his mental model of the next level lagged the work the organization actually valued.',
 'A good manager relationship is a through-line he sees in his career. Connection and clarity helped him do his best work; disconnects were associated with frustration. The lesson combines choosing the right direction with being willing to release direct control of every implementation step.'
 ],'16:09.36','23:46.64','Dwayne Reeves'),
 flow('How his contribution changed',[
 ('Find the problem','Recognize a migration or language issue worth solving.'),
 ('Create a direction','Explain the need, design an approach, and secure alignment.'),
 ('Enable execution','Give others the context and ownership to carry it forward.'),
 ('Move to the next need','Apply judgment where the organization next needs it.')
 ],'An editorial outline of the two promotion stories; it does not make their timing a universal ladder rule.','16:29.20','23:46.64'),
 qa('Why did you try management?',[
 'It was not his original plan. As the team grew, his manager suggested he become a manager; he initially declined. A technical-lead-manager role sounded like a way to retain technical involvement while experimenting with management.',
 'His manager first warned that it could mean two jobs, then supported trying it. Reeves had noticed that several useful career changes came from doing something outside his comfort zone, so he accepted the chance to learn.'
 ],'23:46.64','25:26.80','Dwayne Reeves',[
 follow('Did combining technical leadership and management work?',[
 'Initially it did. His reporting group grew from a few people to roughly a dozen, and he began supporting other managers while still giving technical direction.',
 'As the organization expanded, the best use of his technical leadership for a group of around 35–40 people could differ from what his six or seven direct reports needed from a manager. He was doing strong technical leadership and adequate management, but was not optimizing those individuals’ development as a focused manager might.',
 'The conflict was therefore about responsibilities and organizational health as much as workload. He could replace himself as technical lead and focus on management, or return to the IC path and focus on broad technical needs. Finding a manager for the smaller reporting group seemed easier than replacing the broader technical role, so he returned to being an IC.'
 ],'25:26.80','28:55.36')]),
 qa('What differs between supporting an IC and supporting an engineering manager?',[
 'The center of attention shifts from technical problems toward people and organizational problems. Both coaching relationships have a longer feedback loop than coding: advice might not visibly help for six or nine months. The manager-of-managers loop can be even less immediate.',
 'He admits that he remained focused on whether the organization was operating adequately so he could continue technical work. A more intentional organizational leader would also examine the structure, how managers coach their teams, what opportunities they should create, and whether the role is still right for each person.',
 'He enjoyed one-on-one coaching, particularly helping people with their technical challenges. But switching from a day dominated by technical direction to a smaller portion focused on organizational design did not come naturally. His reflection is about where his attention and strengths were, rather than a claim that managing managers is merely more delegation.'
 ],'28:57.28','32:52.00','Dwayne Reeves'),
 table('The two responsibilities that pulled in different directions',['Responsibility','Group affected','What deserved deliberate attention'],[
 ['Broad technical leadership','The larger language organization.','Strategy, technical challenges, and coordinated execution.'],
 ['Direct people management','The engineers he directly supported.','Individual development and the conditions for doing their best work.'],
 ['Supporting other managers','Teams led by those managers.','Coaching, organizational structure, opportunities, and leadership effectiveness.']
 ],'25:45.28','32:52.00'),
 qa('What led to the senior staff-equivalent promotion?',[
 'The uncanny-valley argument became a shared technical vision. As the organization executed it and results accumulated, the effect became attributable to his direction. This time he discussed the path more actively with his manager; they needed to see enough progress against that vision.',
 'He was still a manager when promoted and returned to the IC path afterward. He believes the promotion reflected technical contribution more than organizational leadership.',
 'The scale was substantial. When he joined in 2015, there was a mixture of PHP and Hack, and only a small fraction of Hack files used strict mode. By the later period he describes, the relevant codebase was more or less strict Hack, alongside runtime and language improvements. The adoption and strict-mode percentages refer to the codebase and times he discusses, not all programming at Meta.'
 ],'32:54.08','35:40.32','Dwayne Reeves'),
 qa('Which colleagues helped you develop?',[
 'He credits a colleague who brought the product developer’s perspective to changes Reeves saw from the language side. That perspective helped the team plan migrations around what engineers actually needed to build.',
 'Another colleague was a patient sounding board for language and compiler questions. Reeves had little prior compiler experience when he joined Hack and remembers not knowing what a lexer was. The ability to ask basic questions safely was crucial.',
 'He also describes learning from Andrew Kennedy, whose foundational type-theory work initially made Reeves feel junior by comparison. Kennedy’s humility and willingness to consider a practical viewpoint helped Reeves recognize that different strengths can each contribute. He could offer useful insight without possessing the same background.'
 ],'35:42.48','39:16.64','Dwayne Reeves',[
 follow('Did that experience make accomplished engineers feel more approachable?', 'Yes, and he wants to pass that experience on. He does not want newer engineers to see his years on Hack as a reason to withhold their ideas. Past accomplishments do not make him always right, and he wants to keep learning. Senior colleagues who explained concepts patiently set the example he thinks others should follow.','39:16.64','40:32.64')]),
 qa('Why have you stayed at Meta for so long?',[
 'He has considered leaving and interviewed elsewhere. Before accepting a move, he asks whether it would solve the fundamental issue or merely react to a temporary period of discomfort.',
 'He values the influence he has earned, opportunities to help bring in diverse talent, an unusual chance to work on a programming language, and a strong team. In several cases, the temporary issue improved without leaving.',
 'He does not treat staying as an unconditional rule. Feeling fundamentally unvalued, no longer believing in the mission, or being in a toxic management environment would be different. Those were not his circumstances. He emphasizes the good fortune of his experience and the difference between solvable frustration and a persistent mismatch.'
 ],'40:33.60','44:38.32','Dwayne Reeves'),
 qa('What would you tell yourself at graduation?', 'When asked to write some code, first ask how the requester knows that it is the right code to write. Aim to participate in deciding what should be done. He wanted his earlier self to see the value of his ideas and judgment beyond keyboard output, especially when impostor feelings made that value harder to recognize.','44:38.32','45:26.48','Dwayne Reeves')
 ],omissions=['Opening teaser montage (00:00–00:32) repeats later material.','Closing thanks and audience-support request (45:28–46:08) omitted.'],notes='All four compact chunks read in full. Retains recruiting and educational opportunity context, DSL cancellation, privacy and Hack migrations, type soundness, IC5/IC6/IC7-equivalent stories, TLM responsibility conflict, long management feedback loops, mentorship and decision criteria for staying. Clear-context lexer spelling normalized; uncertain caption surnames omitted rather than guessed.')
