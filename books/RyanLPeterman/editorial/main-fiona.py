from author_helpers import *

write('source-de97c799fd5897ae','leadership',
      'Support people, stay close to the product, and make tradeoffs explicit',
      'interview',
      'Fiona Fung reflects on management, mentorship, product feedback, and the choices that took her from Microsoft to Meta and Anthropic.',[
 p('Fiona Fung’s account connects three habits: make the partnership with people explicit, experience the product yourself, and treat culture as something people enact. The examples span developer tools, Marketplace, VR, and her early experience with Claude Code. Her comparisons describe those teams at the times she worked on them; they are observations from a career, rather than permanent descriptions of entire companies.','00:03.04','00:18.08'),
 qa('How do you balance an important project against team health?',[
 'First establish whether the situation really warrants an exceptional push. Fung remembers Marketplace lockdowns or war rooms that concentrated people on an urgent objective. That focus could be valuable, but it had a real cost to morale. Leadership should discuss the tradeoff deliberately with the team, rather than allowing the cost to remain implicit.',
 'One war room had a growth target as its exit condition. The team initially imagined that a few fixes might achieve it, but the effort continued much longer than expected. In hindsight, she would have assessed the likely duration more realistically, discussed the effect on team health, and explained the journey and expected length up front. A measurable target alone did not make the sustained intensity manageable.'
 ],'00:34.16','02:24.80','Fiona Fung',[
 follow('How long did that war room last?', 'It felt like at least two months. There were physical rooms in Menlo Park and Seattle, and at one point the team launched 75 experiments at once. The contrast with a week-long launch push is central to the lesson: the team did not understand the duration when it entered the arrangement.','02:25.60','03:04.24')]),
 flow('Before committing to an exceptional push',[
 ('Name the need','Identify why the moment requires unusual focus.'),
 ('Estimate the journey','Examine how long the outcome may take, rather than relying only on the exit metric.'),
 ('Discuss the cost','Make morale and team health part of the leadership and team conversation.'),
 ('Set expectations','Explain the expected duration and tradeoffs before the push begins.')
 ],'An editorial outline of Fung’s retrospective lesson from the Marketplace war room.','00:49.52','03:04.24'),
 qa('What changes when you become a manager of managers?',[
 'The relationship becomes a partnership between people who each bring management skills as well as technical skills. When she first supported managers, including a TypeScript manager she considered an exceptional compiler engineer, she asked what each person did well and how they could divide responsibility. Supporting another manager creates more opportunities to complement strengths.',
 'Delegation also needs a balance of trust and verification. If delegation removes too much contact with the project, the supporting leader can lose touch. She asks managers for fast feedback and transparency about both successes and problems. The useful conversation is the one that exposes where help is needed; a reassuring report that everything is fine can conceal the very issue the partnership should solve.'
 ],'03:05.04','05:30.16','Fiona Fung'),
 qa('How can a mentor make the relationship useful?',[
 'Begin by asking the mentee what they want from the relationship and what success would look like after three or six months. An explicit goal gives both people a way to use their time effectively.',
 'Also distinguish mentoring from coaching. In her description, mentoring combines listening with advice drawn from experience. Coaching acts more like a mirror, helping the other person discover answers within themselves. Clarifying which mode the person wants can change how the conversation should work.'
 ],'05:32.08','06:21.52','Fiona Fung',[
 follow('Should the mentee or mentor drive the relationship?', 'The most effective relationships she has seen start with goals set by the mentee. The mentor contributes experience, advice, and resources, but the person seeking mentorship should state what they hope to gain.','06:23.76','06:54.00')]),
 table('Two modes of helping someone grow',['Mode','What the helper contributes','Useful starting question'],[
 ['Mentoring','Listening, experience, advice, and resources.','What do you want to gain over the next few months?'],
 ['Coaching','A mirror that helps the person find their own answers.','What do you need to understand or discover for yourself?']
 ],'05:40.64','06:54.00'),
 qa('What should an individual contributor do with one-on-one time?',[
 'Put routine status reporting into an asynchronous channel. Fung uses messages or a shared, living one-on-one document where either person can add updates.',
 'Use the live conversation for topics that benefit from interaction: something the person wants to learn, a deeper discussion of their work, or a product question worth exploring together. The point is to reserve the scarce meeting time for conversation, while making the operational updates available separately.'
 ],'06:55.76','07:41.28','Fiona Fung'),
 qa('Why did you leave Microsoft for Facebook?',[
 'She had friends enjoying Facebook, but repeatedly wanted to finish the work in front of her at Microsoft. Her final project there involved JavaScript and TypeScript, and she cared about helping the team deliver TypeScript 1.0. A former Visual Studio colleague, who became her first Facebook manager, contacted her in late 2014 about building a product around buying and selling in groups. She joined in 2015.',
 'The commerce mission mattered for three reasons. Used goods could make a meaningful affordability difference for people with tighter budgets. Reuse could give existing goods a second, third, or fourth life. A selling platform could help a local business begin without first needing a physical store. Marketplace also represented a new kind of connection for her: meeting new people, rather than only reconnecting with people she already knew.',
 'After eleven and a half years at Microsoft, she also wanted to test and broaden her engineering ability outside an ecosystem in which she had become comfortable. The move combined a mission she cared about with a chance to learn beyond familiar tools and practices.'
 ],'07:41.28','10:58.56','Fiona Fung'),
 qa('What stood out about the difference between Microsoft and Facebook?',[
 'Both offered talented colleagues who cared about their work. The clearest difference in her example was speed: early Marketplace shipped weekly updates, while the Visual Studio work she remembered used roughly four-week sprints. Even those four-week sprints had once felt short compared with earlier development cycles.',
 'Facebook also felt much smaller at the time. She appreciated the expectation that a problem was everyone’s responsibility, regardless of role. Her example is a willingness to lean in and help, rather than to treat an issue as belonging exclusively to someone else.'
 ],'10:59.60','12:12.16','Fiona Fung'),
 qa('Why is using your own product so valuable?',[
 'Her first job involved using Visual Studio to build Visual Studio, so daily product use was built into the work. It gave her empathy for users and a feel for the product’s condition. She carried that habit into Marketplace, keeping items to sell so that she could experience the workflow herself. Meeting users also made the effect of the work tangible and motivating.',
 'On VR and related device teams, she used Quest devices and early Ray-Ban products. For a manager who rarely gets to write code, using the product can be a way to experience what the team is building and to contribute directly. She describes reproducing a difficult floor-height bug at home and collecting logs as a small piece of maker time.',
 'Peterman adds that a leader’s report can bring attention to a bug that was already known but had lost urgency. Fung emphasizes another effect: team members notice when a leader uses and cares about their product, and that can build rapport.'
 ],'12:14.56','15:34.96','Fiona Fung'),
 qa('How do you make frequent product use sustainable?',[
 'Integrate the product into something you enjoy. She used VR for exercise, watching movies, and knitting while watching. Enjoyable everyday use creates repeated exposure without making the activity feel like a chore.',
 'At the time of the interview, building Claude Code with Claude Code made that feedback loop part of her day job and let her ship production software again. She also mentions continuing to submit Meta product feedback after leaving.',
 'Leaders can add structured product sessions. On her last VR team, she and her product and design partners tried nearly ready features together on Fridays and gave fast feedback. That complements daily use with a regular opportunity to inspect what is approaching release.'
 ],'15:37.44','17:26.64','Fiona Fung'),
 qa('How can an engineering leader work well with product management?',[
 'Start with the shared objective of the leadership group and the strengths each person brings. Because there will be more work than people, agree explicitly on who owns which pieces and divide the work accordingly.',
 'Using the product also improved her partnership with product managers. Their one-on-ones could become substantive product conversations grounded in something they had actually experienced. The discussion links partnership and product knowledge: an engineering leader has more to contribute when they stay close to what customers use.'
 ],'17:28.00','18:31.92','Fiona Fung'),
 qa('What does kindness contribute to an engineering organization?',[
 'She connects the principle to the pandemic, when device teams were trying to ship Quest 2 and develop Ray-Ban products without normal access to offices, labs, and colocated specialists. People were doing difficult work while also coping with pressures at home.',
 'A personal example made the principle vivid. Her grandmother was in a Canadian care facility that she could not visit. Staff could arrange only limited FaceTime calls, and a rare available slot conflicted with a one-on-one she had promised to attend. The person she supported readily accepted a last-minute cancellation. What may have felt like a small accommodation to him had a large effect on her.',
 'The lesson is that a colleague’s private circumstances are often invisible. Kindness is a practical way to work with people whose full situation you do not know, while the team is trying to accomplish difficult things together.'
 ],'18:32.40','21:25.04','Fiona Fung'),
 qa('Why did you choose Anthropic?',[
 'She was happy working on VR and Horizon OS at Meta and was not conducting a broad search for a new job. The choice she describes was essentially joining Anthropic or staying in a role she already enjoyed.',
 'Using an internal AI tool to build useful work tools showed her that AI was already changing her own workflow. Conversations with Anthropic employees then drew her to their mission orientation, emphasis on safety, and sense of shared responsibility. She likens that attraction to the mission that had drawn her to Marketplace. These are her reasons for the move and impressions of the organization at that time.'
 ],'21:26.40','23:12.08','Fiona Fung'),
 qa('Did Facebook’s culture change as it grew?',[
 'Yes. She treats culture as a living thing expressed through actions, rather than a statement on a wall. Growth changed the company, although she still saw strong commitment to the mission within teams such as VR.',
 'When new employees asked which team would give them the most impact, she also asked what they were passionate about. That question restored a dimension that could disappear in a comparison focused only on career impact.'
 ],'23:13.84','24:35.60','Fiona Fung',[
 follow('How should someone choose between greater impact and work they care more about?',[
 'Have an honest conversation with yourself about what motivates you. Impact, learning, and working with good people can matter in different proportions to different people; she does not prescribe one universal winner.',
 'Share those priorities with your manager. When supporting someone new, she asks what they want from the partnership, what has worked or failed before, and what is important to them. An explicit discussion is more useful than either person guessing the other’s priorities.'
 ],'24:36.40','25:43.12')]),
 qa('What stood out during your first two months at Anthropic?',[
 'She saw the mission and responsibility toward society expressed in onboarding, which made it feel more substantial than an interview slogan.',
 'The speed of the Claude Code team also stood out, even compared with the Marketplace period she remembered as fast. Broad internal use supplied a rapid cycle: build an idea, launch internally, get feedback from employees, release publicly, and keep learning. Her concern as the team grew was preserving that agility and speed.'
 ],'25:45.44','27:21.92','Fiona Fung'),
 flow('The product feedback loop she observed',[
 ('Build an idea','Turn an idea into something people can try.'),
 ('Use it internally','Expose it to colleagues who use the product in their own work.'),
 ('Respond to feedback','Learn quickly from internal experience.'),
 ('Release and learn','Bring it to users and continue the feedback cycle.')
 ],'An editorial rendering of Fung’s early Claude Code observations, rather than a claim that every team uses this exact process.','25:55.04','27:21.92'),
 qa('What feedback most changed your career?',[
 'It was feedback on how she received feedback. Her instinct as an engineer was to debug the situation immediately: ask questions, replay what happened, and determine how to improve. Someone pointed out that giving constructive feedback was already uncomfortable, and her questions could make the person feel they had to justify it.',
 'She changed the first conversation to listening and learning. Questions could wait until another day, after she had reflected. The distinction is about timing and the experience of the person raising the issue: a sincere wish to understand can still feel like a demand to defend the feedback if it arrives too quickly.'
 ],'27:23.60','28:43.20','Fiona Fung'),
 qa('What would you tell yourself at the beginning of your career?', 'Enjoy the experience while it is happening. Work and life move quickly, and the moments that later feel like the good old days are also the moments you are living now.','28:44.16','29:08.16','Fiona Fung')
 ],omissions=['Opening teaser montage (00:00–00:34) repeats later material.','Closing thanks and audience-support request (29:08–29:48) omitted.'],notes='All three compact chunks read in full. Seventeen initiating rounds and three sequential follow-ups preserve the management, mentorship, product, kindness, mission, and reflection discussions. Caption spelling of Claude Code normalized using the interview context; role descriptions and company comparisons are historical to the conversation.')
