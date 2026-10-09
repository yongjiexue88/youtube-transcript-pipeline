from author_helpers import *

write('source-0cbb00b61cc20a18','nonlinear','Build early, show the result, and define your own conditions','interview',
 'Jia Chen describes how hackathons led to a startup, while distinguishing a finished demo, a useful product, and the conditions behind her choice to leave school.',[
 qa('How did you become so involved in hackathons?',[
 'She entered college as a finance major, having taken a Python class and encountered computer science in high school without much interest. At the first hackathon, she expected other builders might implement her idea. Instead, she spent the event building herself. The team lost, but the experience made her excited about creating things.',
 'She went to another event in Ohio and won a hardware prize. During that period she combined classes with long hours learning tools, APIs, libraries, and microcontrollers. Her example is an unusually intense personal schedule, rather than a necessary formula for becoming a builder.'
 ],'00:44.56','03:11.20','Jia Chen',[
 follow('What did you build for that early win?', 'A Raspberry Pi Pico with modules that measured the distance to an object in front of it. She describes it as an exploratory aid for people with visual disabilities, extending the distance information a cane might supply. The discussion is about a hackathon prototype, not a validated assistive device.','03:11.20','04:00.08'),
 follow('Did you have a team?', 'She found someone through Discord and traveled with that person, but built the entry solo. For larger prizes, she considers a team an advantage because people can divide work and specialize.','04:00.08','04:43.60')]),
 qa('How do you choose good teammates?', 'Look at demonstrated skills and projects rather than titles alone. She checks GitHub work, activity, and experience relevant to the proposed project. She also values enthusiasm, effort, resourcefulness, and a willingness to attempt the unfamiliar. The best credential is useful evidence that the person can contribute to this particular build.','04:43.60','05:13.76','Jia Chen'),
 qa('Do you arrive with an idea already prepared?',[
 'Yes. A hackathon has a time limit, sponsor tools, prize categories, and a social environment. She researches those constraints and uses a document to map how the tools could support her ideas before writing code. The important question is whether the proposed product can be finished within the event.',
 'She often prefers a simple, complete result to an elaborate unfinished one. More ambitious entries can work when the implementation steps have been thought through. Her example is a project tracing altered digital artwork back toward an original artist; the interview briefly discusses its provenance interface without supplying a complete technical description of the algorithm.'
 ],'05:13.76','07:03.20','Jia Chen'),
 qa('What is the social part of a hackathon?', 'It includes both the team and the judges. Inside the team, motivation matters over the whole event: one person giving up can affect a small group disproportionately. An enthusiastic teammate can lift the group, and she has seen the strongest results when everyone is fully engaged.','07:03.20','08:02.48','Jia Chen'),
 qa('How do you present a project to judges?',[
 'Keep the pitch short: state the idea, explain what it does, and spend most of the time demonstrating it. Watch whether the judges understand and let them interact with the result. In her experience, many judges were not deeply technical, so a list of frameworks was less persuasive than a product whose value they could see.',
 'This does not rule out technical ambition. A complex project can feel clear and simple when it works well and the presentation makes its purpose obvious. The mistake is assuming that complexity alone is the reason it should win.'
 ],'08:02.48','09:44.32','Jia Chen'),
 qa('Does the idea matter more than execution?', 'Both matter to her: a distinctive idea and a working connection between the frontend and backend. A strong presentation rests on something that actually functions.','09:44.32','10:06.08','Jia Chen',[
 follow('Can you win with a polished frontend and a mocked backend?',[
 'It can sometimes look convincing, but she prefers a genuinely connected project because that enables further development. She describes a common failure: split into frontend and backend groups, add features independently, and leave integration until the end. The pieces can then remain disconnected.',
 'Her approach is to connect the smallest useful path in the first few hours, test the communication, and iterate on that. Integration is an early milestone, rather than the final task after every component is polished.'
 ],'10:06.08','11:45.44')]),
 flow('A workable short-event build',[
 ('Check feasibility','Match the idea, tools, and available time.'),
 ('Connect the smallest version','Make the frontend and backend communicate early.'),
 ('Iterate together','Add features around the working path rather than in isolated pieces.'),
 ('Demonstrate the value','Let the audience try the result and understand what it does.')
 ],'An editorial outline of her planning, integration, and presentation advice.','05:13.76','11:45.44'),
 qa('Which project was your favorite?',[
 'She describes a homemade glasses prototype built from cardboard, glass, and an Arduino-connected OLED display. Whisper transcription appeared through a prism-like display, with a web application also collecting and summarizing the material. Bluetooth connected parts of the setup.',
 'The team completed the build in about nine hours, according to her account. She assembled it from people who were already making things: one built rockets, and others spent time building in an entrepreneurship center. They remained in contact afterward. The account illustrates the value she places on practical builders; it is a prototype story rather than a claim of production readiness.'
 ],'11:45.44','13:32.32','Jia Chen'),
 qa('Would you recommend doing many hackathons?',[
 'She sees them as useful for learning to act in an unfamiliar environment, finishing a project, meeting recruiters, and gaining confidence. But she also sees diminishing returns. Her own suggested range is roughly three to five before considering other uses of the time.',
 'For deeper learning and standing out, she would increasingly favor building a product people keep using. The finished project and real users can matter more than attendance at the event itself. Repeated short, improvised builds do not provide every lesson of sustaining a product.'
 ],'13:32.32','15:21.12','Jia Chen'),
 qa('Did hackathons strengthen your initiative?', 'She already had some willingness to try unusual things, but thinks the events helped. School sometimes felt repetitive, and building offered a more stimulating outlet. Coming from an environment where few people were seriously pursuing startups made that experimentation feel different from the usual path.','15:21.12','16:26.72','Jia Chen'),
 qa('How did you balance classes, hackathons, and content?',[
 'During one demanding semester, she reports maintaining an engineering GPA above 3.5, attending fifteen hackathons, and growing an audience to around fifty thousand. She also describes the pressure of trying to satisfy several different expectations at once.',
 'Time blocking helped: choose a time and place for homework, finish it before the weekend event, and focus on the environment she was in. Content was often short and casual rather than a heavily produced video.',
 'She also deliberately placed herself where useful information and people were available. Office hours could teach her through other students’ questions even when she had no specific question. Later, being in the startup environment in California served a similar purpose. The account combines scheduling with choosing a setting that makes learning and connection easier.'
 ],'16:26.72','19:27.68','Jia Chen'),
 qa('What can a student at a less recognizable school do to stand out?', 'Develop initiative and responsibility: lead a club, help decide the direction of a substantial project, or make useful work visible. Her point is to become someone who makes decisions and carries them through, rather than relying exclusively on the school’s name.','19:27.68','20:18.16','Jia Chen'),
 qa('What did college give you, and where did it fall short?',[
 'She thinks its value depends on the person. Structure, discipline, a learning path, and access to peers can be useful, particularly before someone knows what to learn independently. Completing the path can also be a good route into a desired career.',
 'For her, aspects of school reduced enthusiasm and creativity. Even so, she does not regard the experience as irrelevant: college introduced her to hackathons and contributed to the person she became. She also describes earlier creative experimentation through releasing music in high school.'
 ],'20:18.16','22:14.24','Jia Chen',[
 follow('What do you wish you had understood before college?', 'How much relationships and information can shape opportunity. Advice about applications, access to experiences, and introductions can affect a path even when people have similar skills. Peterman connects that idea with the podcast’s effort to make experienced people’s knowledge more broadly available.','22:14.24','23:44.00')]),
 qa('How did you begin making hackathon content?', 'A friend suggested vlogging an event. She delayed trying it until she had already won many hackathons, then found that the story attracted attention. Showing a student building and winning a substantial prize gave viewers something concrete and unusual to watch.','23:44.00','24:29.92','Jia Chen'),
 qa('What does a personal brand do for a student?', 'It makes subsequent work easier to discover. A project shown to a small group reaches only that group; a visible body of work can reach many more recruiters or potential collaborators at once. She sees it as increasing the chances that useful opportunities find her.','24:29.92','25:01.28','Jia Chen',[
 follow('How did you overcome fear of putting yourself out there?', 'She discussed ideas with a few close friends. Knowing that a small group would support her helped make negative reactions from strangers less important. She acted while still feeling nervous, with a grounding support network.','25:01.28','26:00.16'),
 follow('What is one concrete step for someone who does not want to become a frequent creator?', 'Move the project beyond localhost. Publish a working version, make the repository available where appropriate, and give people a usable link. Visibility can begin with sharing the work itself rather than posting constantly.','26:00.16','26:26.24')]),
 qa('How did a gap semester and a startup happen?',[
 'She began an MVP one evening after deciding to try a company. The initial idea responded to questions from her audience about entering hackathons. She posted it the next morning, and the application crashed under the traffic.',
 'Months later, a cofounder helped restore it. A trip with hackathon friends became a longer stay in San Francisco. She describes meeting investors at events, including an informal hot-pot gathering, while the product already had users and some business revenue.',
 'An investor’s interest in the story and the match between her experience and the product brought an initial check. Posting about that moment attracted further interest. Her account combines prior building experience, a network, traction, and distribution; it was not a company emerging from a social post alone.'
 ],'26:26.24','28:41.52','Jia Chen',[
 follow('Did you plan to return to the same school?', 'At the time of the conversation, she thought returning to Michigan State was unlikely, while leaving open a possible transfer to a California school. The plan remained unsettled.','28:41.52','29:01.60')]),
 qa('What startup advice proved useful?',[
 'Keep shipping, and also avoid exhausting yourself. She sees the tension between those instructions and now thinks consistent progress needs room for breaks and other parts of life.',
 'The pressure was real: she describes a robbery in which laptops and personal belongings were stolen, followed by continued customer outreach. She reports winning business from several companies and reaching five-figure monthly recurring revenue in that period.',
 'She does not label the experience as having fully burned out, but says it weighed on mental health and relationships. Continuing to work through a crisis is part of her story, rather than evidence that rest or security are dispensable.'
 ],'29:01.60','30:48.64','Jia Chen'),
 qa('Would you recommend leaving college to start a company?',[
 'She would not recommend dropping out immediately. Set personal conditions first. Her own conditions included a credible network for funding and customers, the ability to support herself, technical capacity with the right collaborators, and a way to distribute the product.',
 'Those conditions made her position different from someone with only a fresh idea. The useful takeaway is to make the prerequisites explicit for your own circumstances, rather than treating her decision as a default recommendation.'
 ],'30:48.64','31:48.48','Jia Chen'),
 table('The conditions she checked before committing',['Condition','Question behind it'],[
 ['Technical execution','Do we have the skills and collaborators to build the product?'],
 ['Distribution','Can we reach the people who would use it?'],
 ['Customer and funding network','Can we connect with customers and potential supporters?'],
 ['Ability to sustain the move','Can we support ourselves in the environment we are choosing?']
 ],'30:48.64','31:48.48'),
 qa('Would you advise someone to pursue computer science now?', 'She says it depends on the person, but recommends trying to build something people want to use. That experiment can reveal whether the person enjoys product building, create useful work in its own right, and supply concrete evidence to show a recruiter.','31:48.48','32:38.24','Jia Chen'),
 qa('What would you tell your earlier self?', 'Be more open to experiences and people that can teach you something. She used to stay within a small social circle and decline invitations more readily. Her reflection connects learning with participation and relationships, as well as technical practice.','32:38.24','33:21.60','Jia Chen'),
 p('The company discussed at the end, Sprint.dev, was intended to make hackathons more approachable through tools, support, and opportunities to build together. Her description of the builders she wanted emphasized creativity, execution, collaboration, and shipping useful work, rather than credentials alone.','33:34.16','34:27.20',heading='The product behind the story')
 ],omissions=['Opening teaser montage (00:00–00:44) repeats later discussion.','Closing promotional sign-up language condensed into a brief product-context paragraph.'],notes='All three compact reading chunks read in full. Preserves ordered hackathon prompts and follow-ups, early integration, demo criteria, diminishing returns, educational qualifications, time-blocking, network/distribution, startup conditions, and personal costs. Achievement and revenue figures remain self-reported; prototypes are not treated as validated products.')
