from write_section import *
b=[]
q=lambda x,y,a,z,f=None:qa(x,y,a,z,f,speaker='Sash')
b.append(q('How did you choose your first team at Meta?',[
'An initial London-based option lost its appeal when code review across locations took days. Sash then met someone who saw his mix of design and engineering experience as a fit for a team that would turn designers’ unused prototypes into shipped experiences.',
'That News Feed delight team prioritized animations, playful interactions and other small moments of enjoyment without a clear metrics requirement at the outset. He loved it, but the team lasted only about half a year. Looking back, he recognizes that an enjoyable proposition without a durable impact story was unlikely to survive scrutiny in that organization.'
],49,169))
b.append(q('How could a design-oriented team prove its work was successful?',[
'Sash retrospectively sees the need for an executive sponsor with a credible theory of value. He recalls a survey measure asking whether people felt Facebook cared about them, which supplied a possible connection for delight work. The measure was subjective and open to interpretation.',
'He thinks it is harder to defend such teams when the company is intensely focused on efficiency. This explains a tension in his choices: he sought work he found compelling even when its measurable payoff was uncertain.'
],169,230))
b.append(q('What were you optimizing for when choosing teams?',[
'Initially, fun. He followed people, intuition and opportunities that seemed interesting, then made sense of the resulting path afterward. Over time he became somewhat more deliberate but still preferred risky zero-to-one work.',
'He noticed that many strong engineers wanted a clear product definition, diagram or design before beginning. His comfort working without those gave him a useful niche. Breadth accumulated tools, relationships and knowledge that could become valuable on later projects, although that does not guarantee a successful outcome for every move.'
],232,338))
b.append(q('What makes a designer especially good to work with?',[
'A willingness to collaborate continuously. An initial design need not anticipate every engineering constraint, but the team eventually has to resolve missing data, network failure and other real-world conditions. Engineering can also introduce possibilities the designer may not have considered, such as sensors affecting an interaction.',
'He values short feedback loops. On an unreleased hardware project, he worked on a makeshift pipeline that showed Figma designs on the device quickly so designers could change them and immediately see the result. Both sides listening and adjusting produces a stronger product than handing off a supposedly finished idea.'
],338,447,[fu('Is the key both rapid iteration and two-way communication?','Yes. He likes beginning with an ambitious picture rather than rejecting it immediately through constraints, then jointly adapting it to processing power, heat or other limits. The constraints still matter; delaying premature dismissal gives the collaboration more room to discover a good solution.',449,503)]))
b.append(q('Why leave iOS work for experimental hardware and Android?',[
'He was looking for interesting work in New York and found a new hardware team’s opening more appealing than the available iOS options. The project used Android’s open-source platform. He had no hardware or Android experience, but wanted to try it.',
'The new domain was unfamiliar rather than a carefully planned career optimization. Once involved, he enjoyed the exploration. His first six months produced only about two committed diffs because much of the work was prototyping, sourcing hardware and learning what an eventual product could do.',
'One investigation used a Raspberry Pi to emulate a car’s Bluetooth messaging integration and inspect its communication with an iPhone. The throwaway code was not intended for the main repository: it helped establish the best experience the protocol might support before production implementation. Exploring that upper bound became a recurring part of his work.'
],504,726))
b.append(q('How was your performance judged when you committed so little code?',[
'The early team’s expectations centered on reducing uncertainty, not simply landing production code. It was staffed with senior people who understood that a risky project needed that kind of work. Sash describes this as one way a large company can encourage exploration without promising a promotion.',
'He also sees a tension in review cadence: frequent feedback is useful, but a short cycle can discourage bets whose outcome takes multiple cycles. He does not claim there is a review process that perfectly serves everyone. The important point in his example is that expected contribution was aligned with the project’s exploratory stage.'
],727,817))
b.append(q('What differed most between hardware and software teams?',[
'Timelines. A physical device must eventually have software flashed onto it and enter a manufacturing process. Moving that deadline can disrupt a much larger chain of commitments. A day-one update is possible but does not eliminate the need to put something usable in the box.',
'Compared with continuous software delivery, that makes the late project period more unforgiving. Work can feel relaxed early and become a crunch near the manufacturing date. He likens it to an earlier software era when a product had to be finalized and shipped on a physical disc.'
],819,908))
b.append(q('Why move from hardware back to software prototyping?',[
'He wanted to try living in London. Staying on the hardware team from abroad was not workable in the situation he encountered. He speculates that unreleased technology and cross-border complexity could have contributed, but does not claim to know the precise regulatory cause.',
'Instagram was opening a London office with a blockchain team, offering another exploratory opportunity. He helped ship an NFT feature and then became interested in a broader question inspired by leadership: could following a creator exist outside a single platform?',
'Translating that idea into a product required both technical experiments and partnerships. What would onboarding look like? How could another platform recognize the relationship? Would a wallet or token participate? More difficult still, why would advertising, subscription and merchant-service businesses all want the same system?',
'Working with partners gave him a view of business incentives he had not usually encountered as an engineer. The project ended as the crypto environment deteriorated, but the experience showed him that technical feasibility alone does not make a multi-company product viable.'
],910,1296))
b.append(q('How did you get involved in the early Threads project?',[
'As the blockchain effort wound down, he worked on more conventional Instagram features. People then contacted him about ActivityPub and decentralized social networking. He is uncertain exactly why they approached him, but suspects a reputation for sharing prototypes played a part.',
'During the holiday period, he connected internal Instagram and Mastodon instances with crude experimental code so that a user search could resolve an Instagram account. The technical possibility was not particularly surprising, but a concrete working example generated excitement more effectively than another presentation.',
'Next, he stripped images from an Instagram client, enlarged captions and worked with a deeply experienced back-end colleague to build text-only posting and feeds. The early experience lived behind internal gates inside Instagram. It was a progressive carving-out of a product, not an isolated application built without an existing platform.',
'Working from London, he often repaired broken experimental builds before US teammates came online. The early team grew around a leadership-backed opportunity to release a text product amid Twitter’s turmoil. Support for privacy, integrity and performance arrived as needed. He remembers roughly five or six months from prototype to public launch, while emphasizing the benefit of Instagram’s mature primitives and infrastructure.'
],1298,1743))
b.append(q('What made the senior back-end engineer on that project so effective?',[
'Deep familiarity with the existing system. The colleague knew how to create a feed, make a post work without an image and understand consequences elsewhere in the application. Their conversations rapidly became working front-end/back-end changes that Sash could test.',
'Large, mature primitives also helped. A high-level operation could provide defaults and integrations without each engineer rebuilding lower layers. The knowledgeable partner knew how to use those facilities appropriately. Sash’s playful comparison with a copilot emphasizes accurate context and judgment, rather than a literal substitute for the person.'
],1743,1854))
b.append(q('Did sharing prototypes build the reputation that led to new opportunities?',[
'He cannot know exactly what others thought, but believes repeated internal demonstrations made people associate him with fast, exploratory work. Prototypes using company technology could not be shared publicly, so internal posts were an important venue even when immediate engagement was modest.',
'Responding to an ambiguous inquiry with something working also showed initiative. Early projects benefit from people who can move without a fully assigned checklist. He thinks that behavior stands out amid the meetings and alignment work common in a large company.'
],1855,1995))
b.append(q('Which AI prototype stands out from the later part of your work?',[
'He built an early conversational assistant over public account-safety and support information using retrieval-augmented generation. It still hallucinated substantially, but it made a possible direction for support tangible. Sharing it produced many messages from people in other parts of the company.',
'He does not claim to have invented the approach or solved support. The value was bringing an outside technical possibility into a familiar corporate context and showing how it might interact with the company’s own data and products. Colleagues focused on their jobs may not follow every new industry development; a situated demonstration can make the opportunity visible.'
],1995,2120))
b.append(q('Why does a prototype communicate better than a written proposal?',[
'A written description depends on everyone constructing the same mental model. An image narrows that ambiguity; a video narrows it further. An interactive prototype lets people experience the behavior directly and talk about a specific interaction.',
'Sash has seen meetings progress for some time before participants discover they imagined different products. A prototype can expose that disagreement early and shorten the ambiguous part of a project. Its fidelity helps alignment, not merely publicity.'
],2120,2206))
b.append({'type':'flow','title':'What a prototype contributes before production','caption':'An editor-assembled sequence across Sash’s examples; arrows show a possible collaboration process, not a guarantee that a prototype will ship.','editorial':True,'steps':[
{'title':'Explore the upper bound','text':'Use rough code to discover the experience that might be possible.'},
{'title':'Make the idea tangible','text':'Give partners something they can inspect or interact with.'},
{'title':'Resolve different mental models','text':'Discuss concrete behavior instead of assuming everyone read a proposal the same way.'},
{'title':'Learn constraints and incentives','text':'Adapt the design to hardware, software and business realities.'},
{'title':'Decide what to productionize','text':'Turn selected learning into a durable product, or stop when the case is weak.'}
], 'evidence':ev(338,503)+ev(504,726)+ev(910,1296)+ev(1298,1743)+ev(2120,2206)})
b.append(q('How do you assess your growth from IC4 to IC6 despite frequent team switches?',[
'Staying in one space usually makes leveling easier: expertise, goodwill and relationships compound around a known problem. He saw that in a colleague who remained on the original team for years. He often found that kind of continuity less interesting for himself.',
'His choices favored enjoyable projects and breadth over maximizing promotion speed. They accumulated connections and knowledge, with some wrong turns along the way. Because he worked long hours, enjoyment mattered to sustaining the effort.',
'He explicitly resists turning his path into universal advice. The right strategy depends on the career and life a person wants. His eventual promotion does not prove that repeated switching is the fastest route, only that the route can develop a useful niche for someone with his preferences.'
],2207,2393))
b.append(q('How did your path compare with people from your original bootcamp group?',[
'He remembers peers becoming managers or remaining in the same application or domain, generally doing well. They preferred vertical growth more than his broad exploration. The comparison is a small anecdotal sample, not evidence that one strategy wins.',
'When leaving, he found it difficult to identify a replacement for a role centered almost entirely on prototyping. He thinks large-company incentives naturally direct most people toward predictable impact. Yet a company also needs some people prepared to test uncertain directions. That balance may help it discover options beyond its established work.'
],2394,2533))
b.append(q('What are the limits of optimizing only for a metric?',[
'Sash invokes the familiar problem that a measure can become less informative once it becomes a target: people learn to game it. He also thinks important parts of product quality are difficult to measure and require taste.',
'A relentlessly increasing local measure can obscure opportunities that require a temporary setback or a different direction. He recognizes the difficulty of translating that insight into a scalable framework, because large organizations also need repeatable processes. His preference for experimentation is a response to that tension, not a fully specified replacement for metrics.'
],2534,2577))
b.append(q('Do you regret any of the ten team switches?',[
'Some paid off less than he hoped, but he learned from them and built relationships. Trying to be a good teammate made those connections useful in both directions: someone could invite him to a later project, or he could bring them along.',
'The size of that network became particularly visible after he left Meta, when people offered introductions or expressed interest in what he might build next. He values the adventure and people as outcomes, rather than evaluating every move only by title progression.'
],2579,2679))
b.append(q('Why leave Meta instead of switching teams again?',[
'After a long period, he wanted to return to a startup-like environment where his preferred pace felt natural. He wanted to test his own ideas close to the outcome, without attributing failure to a meeting or another team.',
'He acknowledges greater financial and practical risk. He views a return to a larger company as a possible fallback, while recognizing that it is a hope rather than a guaranteed future offer. His circumstances allowed him to take the experiment, and the choice reflected that personal capacity.'
],2679,2803,[fu('Did it help to think of the decision as a two-way door?','Yes. He distinguishes decisions that are difficult to reverse from ones that appear reversible. A perceived fallback can justify taking a risk while circumstances permit, although it still calls for care. His language is a decision framework, not proof that any job transition will be reversible.',2732,2783)]))
b.append(q('What advice would you give yourself at the beginning of your career?',[
'Address weaknesses enough that they do not obstruct the work, then invest in the strengths that make the contribution distinctive. A manager helped him see that fixing every shortcoming was not necessarily the highest-value development plan.',
'For Sash, that means choosing a setting where his comfort with ambiguity, design collaboration and rapid prototyping can be useful. The advice asks a person to understand their own strengths and fit, rather than copy his specific team choices.'
],2803,2856))
save('source-f73980de1c633301','Sash: A Career Built Through Prototypes and Team Changes','A staff engineer explains the appeal and risks of broad exploration, from design delight and hardware to blockchain, Threads and early AI demonstrations.',b,'nonlinear',omissions=['Opening promotional montage repeats later discussion and is counted once; closing social-account and podcast engagement requests are omitted.'],notes='All five chunks read in full. Preserves each domain transition, the two-diff review explanation, uncertain opportunity attribution, partnership incentives, cohort comparison and the guest’s explicit warning against universalizing this career path.')
