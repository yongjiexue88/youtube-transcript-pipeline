Chunk 3; segments 707–1069. Start may repeat the previous chunk for context.

# Harvard Professor: CS50, What Matters More Than Programming Now, Lecturing Well | David J Malan

Source ID: source-f55dd5f460ec58d2
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Harvard_Professor_CS50,_What_Matters_More_Than_Programming_Now,_Lecturing_Well_David_J_Malan_en.txt
Video: https://www.youtube.com/watch?v=bB2o81DnKHk

[L716] [23:47.40] constructs that are now fundamental to
[L717] [23:48.92] those kinds of languages, loops and
[L718] [23:50.44] conditions and functions and variables
[L719] [23:52.08] and return values and so forth. It sort
[L720] [23:53.52] of got It's got everything, but it's
[L721] [23:55.28] also a pretty small language, and unless
[L722] [23:57.52] you download third-party stuff, there's
[L723] [23:59.48] not a very large standard library, in
[L724] [24:01.96] fact. So most anything you want, you
[L725] [24:03.68] need to build yourself. And so we
[L726] [24:05.28] leverage this significantly in CS50, so
[L727] [24:07.60] much so that by mid-semester in week
[L728] [24:09.20] five of the class, students are building
[L729] [24:10.68] their own hash tables, and we're talking
[L730] [24:12.56] about how you could construct singly
[L731] [24:14.20] linked, doubly linked lists, uh
[L732] [24:16.24] hash tables and tries, uh trees, yeah,
[L733] [24:19.20] abstract data types like stacks and
[L734] [24:20.84] queues and so many more. And what I
[L735] [24:22.72] think is especially meaningful about C
[L736] [24:24.28] is that you can't just instantiate one
[L737] [24:26.00] of those data structures if you want
[L738] [24:27.40] one, like you can in Java and C++ with
[L739] [24:30.08] STL and certain other libraries. Like,
[L740] [24:32.16] if you want it, you're going to have to
[L741] [24:33.04] build it yourself. And I think that
[L742] [24:34.76] alone is a good educational exercise,
[L743] [24:37.64] not because you're going to need to
[L744] [24:39.04] build that thing again, but because
[L745] [24:40.56] there's value, I think, in really
[L746] [24:42.20] understanding from the bottom up what is
[L747] [24:45.52] going on inside of that device, so that
[L748] [24:47.64] one, you can make more informed
[L749] [24:48.84] decisions as to how you want to engineer
[L750] [24:50.56] and design your own data structures down
[L751] [24:52.24] the line. Two, you can
[L752] [24:54.56] diagnose problems by reasoning through
[L753] [24:57.12] first principles What could possibly go
[L754] [24:59.16] wrong because you understand how the
[L755] [25:01.52] data is being stored and what the
[L756] [25:03.36] algorithms are that are performing on
[L757] [25:04.92] that data. Um and three, it's a
[L758] [25:08.56] wonderful scaffold to higher-level
[L759] [25:10.72] languages because one of my favorite
[L760] [25:12.36] things from week five to six in CS50 is
[L761] [25:15.32] students go from having written the week
[L762] [25:16.80] in week five like their own hash tables
[L763] [25:18.96] implementation
[L764] [25:20.40] uh for adding data, retrieving data, and
[L765] [25:22.04] so forth, which is like this many lines
[L766] [25:23.44] of code for some font size. And it it
[L767] [25:26.52] gets whittled down in week six to one
[L768] [25:27.96] line where you just instantiate a Python
[L769] [25:29.84] dictionary. But and you can be
[L770] [25:32.00] productive with a dictionary and many
[L771] [25:33.56] courses do teach programming by way of
[L772] [25:35.48] Python alone and we too have done it for
[L773] [25:37.32] some of our audiences.
[L774] [25:39.16] But you really never get around to
[L775] [25:40.96] understanding what's going on underneath
[L776] [25:42.56] the hood. And our goal in CS50 among
[L777] [25:44.60] them is not to uh output programmers,
[L778] [25:47.96] but engineers and educated citizens and
[L779] [25:51.12] folks who really understand from first
[L780] [25:52.88] principles how technology works. And so
[L781] [25:55.20] C for instance strikes I think just that
[L782] [25:57.72] right balance. And for those students
[L783] [25:59.00] who want to go even deeper in a systems
[L784] [26:00.56] class, they can go learn about assembly
[L785] [26:02.64] and compilers and so forth. Um but those
[L786] [26:04.96] students who want to go on to web
[L787] [26:06.00] programming or data science stuff or AI
[L788] [26:08.40] nowadays can just build on top of the C
[L789] [26:10.68] and then in turn Python um layers that
[L790] [26:13.08] we use in the class.
[L791] [26:14.76] For this podcast, I produced transcripts
[L792] [26:16.72] for every episode for convenient
[L793] [26:18.40] skimming and I built a custom tool to
[L794] [26:20.52] automate that.
[L795] [26:21.80] Recently, I noticed in the Barbara
[L796] [26:23.60] Liskov transcript my simple
[L797] [26:26.04] speech-to-text tool was getting a lot of
[L798] [26:27.84] things wrong. For instance, the CLU
[L799] [26:29.76] programming language is spelled all caps
[L800] [26:32.12] CLU, not CLU.
[L801] [26:34.72] So, to fix this, I used Cursor 3, picked
[L802] [26:37.56] the strongest version of Opus 4.7 extra
[L803] [26:40.68] high, and had an agent make a plan to
[L804] [26:42.60] fix that. And while I was waiting, I
[L805] [26:44.56] figured I'd trigger a few more agents
[L806] [26:46.04] for code cleanups and front-end
[L807] [26:47.60] improvements.
[L808] [26:48.80] Um it generated a reasonable plan with
[L809] [26:50.76] rich system diagrams. It applied all the
[L810] [26:53.40] changes within minutes and worked on the
[L811] [26:55.48] first try.
[L812] [26:56.64] So, if you want to build something with
[L813] [26:58.20] the flexibility of sending off a bunch
[L814] [27:00.04] of agents with frontier models of your
[L815] [27:01.92] choice, you can go to cursor.com to try
[L816] [27:05.04] out Cursor 3.
[L817] [27:06.52] >> This is not my [snorts] perspective, but
[L818] [27:08.84] um I was doing research and I saw a
[L819] [27:11.36] YouTube video that said, "Whatever you
[L820] [27:12.88] do, don't take CS50." Clickbait,
[L821] [27:15.48] whatever. Yeah, I So, I watched the
[L822] [27:17.08] video and the person worked. Yeah, it
[L823] [27:19.80] got me. It got me. And the perspective
[L824] [27:22.44] of the author of this video was that
[L825] [27:25.52] CS50 teaches you all this stuff that you
[L826] [27:27.92] don't really need to know if you were
[L827] [27:29.20] like a full stack engineer or something.
[L828] [27:31.24] Like, if you if I was just going into
[L829] [27:33.12] the industry and I'm just making web
[L830] [27:35.80] apps, that a lot of this um underlying
[L831] [27:38.72] stuff you you might not need. And so,
[L832] [27:40.56] maybe it's not a good use of time. And
[L833] [27:42.68] I'm curious what you would say to
[L834] [27:44.56] someone that has that that mindset that
[L835] [27:47.80] you don't need to actually know how the
[L836] [27:49.32] computer works.
[L837] [27:51.04] >> I don't want to get into a whole
[L838] [27:51.96] internet fight here, but I think that is
[L839] [27:54.52] absolutely the wrong mindset. Certainly
[L840] [27:56.48] for a full stack engineer. I mean, by
[L841] [27:58.04] definition of full stack, you should be
[L842] [27:59.60] understanding everything that's
[L843] [28:01.80] happening among those layers. So, I
[L844] [28:03.36] think the better formulation isn't that
[L845] [28:05.64] you don't need to know these things, but
[L846] [28:08.40] rather you won't need to use these
[L847] [28:10.48] things. Use in a literal sense. Like, I
[L848] [28:12.84] don't my C is a very popular language
[L849] [28:15.04] even according to some rankings each
[L850] [28:16.80] year. It's, you know, the number one,
[L851] [28:17.92] number two language in terms of its
[L852] [28:19.24] omnipresence still to this day because
[L853] [28:21.16] it's very highly performant. Um
[L854] [28:23.96] albeit more challenging to write than
[L855] [28:25.52] some languages. I only use C for 5 weeks
[L856] [28:29.28] during CS50 itself, but that doesn't
[L857] [28:31.48] mean that it hasn't helped me understand
[L858] [28:33.60] higher-level languages, what is going on
[L859] [28:36.12] inside of a system, how you can improve
[L860] [28:38.52] the performance of or the design of some
[L861] [28:40.12] system by understanding again those
[L862] [28:41.80] first principles.
[L863] [28:43.48] Uh I don't use Scratch except for 1 week
[L864] [28:46.12] out of the year. I do use Python more
[L865] [28:48.32] frequently and I use JavaScript and some
[L866] [28:50.28] HTML and CSS, but I think if you're
[L867] [28:52.84] going to call yourself an engineer, you
[L868] [28:54.36] should absolutely
[L869] [28:56.12] have mastery of and knowledge of those
[L870] [28:59.80] underlying building blocks if you want
[L871] [29:01.80] to not just output something that
[L872] [29:03.76] frankly AI could output nowadays, but
[L873] [29:06.28] you can understand and you can create
[L874] [29:08.08] the next thing or the solution to some
[L875] [29:10.36] other problem that we haven't even yet
[L876] [29:11.80] solved. Um I think that's the better
[L877] [29:13.56] mindset to appreciate yes, I'm not going
[L878] [29:15.80] to need to use Scratch or C or maybe
[L879] [29:19.04] some of the other things we touch on in
[L880] [29:20.24] CS50, but the knowledge and the
[L881] [29:23.44] principles that we extract from those
[L882] [29:25.88] implementation details are incredibly
[L883] [29:27.60] valuable. If you want to be an engineer
[L884] [29:29.12] and not just say
[L885] [29:30.48] a coder, is which is a distinction that
[L886] [29:32.24] some folks might make.
[L887] [29:34.16] >> I was looking at the syllabus and
[L888] [29:36.08] there's C obviously and there's all the
[L889] [29:38.48] I mean, you know, basic data structures,
[L890] [29:40.76] those types of things, bread and butter.
[L891] [29:42.88] And then in the end of the course,
[L892] [29:44.88] there's the a week on artificial
[L893] [29:46.52] intelligence, which I was surprised to
[L894] [29:49.12] see in a intro course because it's kind
[L895] [29:51.60] of like
[L896] [29:52.68] there's no way that you could teach
[L897] [29:55.08] AI in a week. So I I'm assuming it's a
[L898] [29:59.00] more high-level introduction.
[L899] [30:00.40] >> It is. It's only for an hour and it
[L900] [30:01.84] technically temporally it's offered in
[L901] [30:03.56] the middle of the semester for the
[L902] [30:04.76] on-campus students. Um it coincides by
[L903] [30:07.16] design with uh family weekend when uh
[L904] [30:10.20] first years and juniors uh students'
[L905] [30:12.92] parents come to town very frequently. Um
[L906] [30:15.04] and so we do it as a very broad
[L907] [30:16.68] introduction to what everyone is talking
[L908] [30:18.44] about
[L909] [30:19.20] nowadays in the AI space. Um there are
[L910] [30:21.36] full-fledged classes of course at
[L911] [30:22.60] Harvard and other institutions that
[L912] [30:24.12] students can take and it's really meant
[L913] [30:25.48] to wet their appetite, but also give
[L914] [30:27.12] them some context for the very tools
[L915] [30:28.68] we're using in CS50. We have this
[L916] [30:30.80] virtual rubber duck that's built on top
[L917] [30:32.36] of OpenAI's APIs and Microsoft Azure's
[L918] [30:34.72] web ser- API service um that they're
[L919] [30:37.36] using every day or every week certainly
[L920] [30:39.60] throughout CS50. So among the goals
[L921] [30:41.28] pedagogically is to help them understand
[L922] [30:42.96] what are the tool how do the tools work
[L923] [30:44.64] that you yourself have been using.
[L924] [30:46.64] Two, to help them understand what is it
[L925] [30:48.44] that the world is talking about
[L926] [30:49.76] nowadays, and three, is prepare them to
[L927] [30:51.84] use these tools more effectively by the
[L928] [30:53.72] end of the semester because for instance
[L929] [30:55.12] for CS50's final project, students are
[L930] [30:57.12] encouraged and welcome to use Claude or
[L931] [30:59.32] ChatGPT or Gemini or any number of
[L932] [31:01.44] off-the-shelf AI tools that we don't
[L933] [31:03.36] allow those through policy for the
[L934] [31:05.20] course's assignments.
[L935] [31:07.16] >> Yeah, I had a conversation with a
[L936] [31:09.48] another professor and a specifically
[L937] [31:12.44] about um you know, is AI affecting how
[L938] [31:15.40] the kids are learning?
[L939] [31:17.16] And uh his perspective was it was kind
[L940] [31:19.80] of um maybe he didn't do it properly and
[L941] [31:22.28] the students were over-relying on it and
[L942] [31:24.44] I think that is a concern that a lot of
[L943] [31:26.00] people have is that students these days
[L944] [31:29.04] can be more brain-dead. Like you could
[L945] [31:31.84] just go to ChatGPT and say, "Honestly,
[L946] [31:34.96] just solve the problem for me."
[L947] [31:36.92] For you as an educator in computer
[L948] [31:38.76] science, what is the ideal uh
[L949] [31:41.88] relationship with AI for your students?
[L950] [31:44.60] >> Yeah, so this virtual rubber duck at
[L951] [31:47.44] cs50.ai, which anyone with a free GitHub
[L952] [31:49.60] account can use, um is really meant by
[L953] [31:52.32] design to be a less helpful version of
[L954] [31:53.96] ChatGPT, one that is also more tuned to
[L955] [31:56.44] CS50's own material and syllabus and so
[L956] [31:58.88] forth. Um and that's because all of
[L957] [32:00.64] these tools off-the-shelf can pretty
[L958] [32:01.80] much do your homework for you. And this
[L959] [32:03.12] has been true for several years even
[L960] [32:04.36] before the fall of 2022 when ChatGPT
[L961] [32:07.00] came out. I mean, we were looking
[L962] [32:08.32] closely at GitHub Copilot for some time
[L963] [32:10.64] because if you created an empty text
[L964] [32:12.44] file in VS Code called mario.c, which is
[L965] [32:15.08] the file name we use for one of CS50's
[L966] [32:16.52] pro
[L967] [32:17.64] problem sets, and if you so much as
[L968] [32:19.48] type, I think, hash and then I for
[L969] [32:22.64] include, you pretty much get a
[L970] [32:24.28] suggestion to auto-complete the entirety
[L971] [32:26.12] of that particular problem set. Um and
[L972] [32:28.52] that's just because I mean, we for
[L973] [32:30.36] better for worse are part of these
[L974] [32:31.76] models in so far as the open courseware
[L975] [32:33.44] has presumably been slurped up as with
[L976] [32:35.28] the rest of the internet as part of the
[L977] [32:36.80] training data, so to speak, for these AI
[L978] [32:38.40] models. Um so, that has both good and
[L979] [32:40.64] bad, and that's why we set out to make
[L980] [32:42.20] our own sort of duck-themed version of
[L981] [32:44.76] these tools that puts downward pressure
[L982] [32:46.52] on that willingness of the tools to be
[L983] [32:48.56] too helpful, and we've tried to attune
[L984] [32:50.68] the duck to be more akin to a good
[L985] [32:52.08] teacher or tutor that leads you to the
[L986] [32:53.76] solution, but certainly doesn't
[L987] [32:54.88] auto-complete your whole way through it.
[L988] [32:57.80] >> I see. So, there's uh like a system
[L989] [32:59.76] prompt, there's some scaffolding that
[L990] [33:01.76] says,
[L991] [33:02.76] "Don't answer the question, but help me
[L992] [33:04.80] figure it out."
[L993] [33:05.76] >> Pretty much. And it's much easier to do
[L994] [33:06.92] this now than it was in 2022 and 2023
[L995] [33:09.64] when we first rolled this out, um which
[L996] [33:11.96] is to say, there's a lot of tools, even
[L997] [33:13.68] commercial tools, that faculty can use
[L998] [33:15.92] to do the same kind of thing for their
[L999] [33:17.88] own course. Um for us, it was important
[L1000] [33:20.68] to draw a clean line in the sand to
[L1001] [33:22.04] students because you could approximate
[L1002] [33:24.00] this duck by just telling students, "Hey
[L1003] [33:25.80] everyone, go copy-paste this system
[L1004] [33:28.24] prompt, as you described, into ChatGPT
[L1005] [33:30.80] before you ask your homework question."
[L1006] [33:32.48] And no one's going to do that, and like
[L1007] [33:34.00] that's going to drift out of date, and
[L1008] [33:35.36] it just feels too clunky. Students are
[L1009] [33:36.96] just going to end up typing into the
[L1010] [33:38.12] prompt. Whereas, I think it's a lot
[L1011] [33:40.24] cleaner, um if not simpler, to know I
[L1012] [33:42.92] cannot, through policy,
[L1013] [33:45.08] go to ChatGPT, Gemini, Copilot, any of
[L1014] [33:47.16] these things, but I can go to and use as
[L1015] [33:49.00] much as I want cs50.ai or the plugin we
[L1016] [33:51.56] have in VS Code of the same. Um and that
[L1017] [33:53.84] to me is a very healthy line because you
[L1018] [33:55.72] know if you're crossing that line, if
[L1019] [33:57.60] you're pulling up chat.openai.com or
[L1020] [34:00.48] gemini.google.com and the like, um and
[L1021] [34:03.16] that at that point it's a conscious
[L1022] [34:04.64] choice to be academically dishonest, as
[L1023] [34:06.84] we would describe it in CS50's syllabus.
[L1024] [34:10.20] >> When I was going through my CS
[L1025] [34:12.16] education, um
[L1026] [34:13.88] cheating was already pretty rampant. Um
[L1027] [34:16.20] I mean, people put their code on GitHub,
[L1028] [34:17.92] and you kind of paraphrase someone
[L1029] [34:19.92] else's code. Well, not me, but other
[L1030] [34:21.68] people. Okay.
[L1031] [34:22.62] >> [laughter]
[L1032] [34:23.04] >> And uh I I imagine with the new
[L1033] [34:26.64] technology that actually, I mean, with
[L1034] [34:28.88] with anything with cheating, it's
[L1035] [34:30.32] adversarial. There's people who are
[L1036] [34:31.64] cheating, and there's people who trying
[L1037] [34:32.68] to catch the cheaters, right?
[L1038] [34:34.76] I could imagine that the cheating tools
[L1039] [34:37.80] are advancing faster than the ability to
[L1040] [34:40.24] catch them because you just generate the
[L1041] [34:42.44] code, it's not easy to say, "Oh, that
[L1042] [34:46.16] was um you know, AI generated or
[L1043] [34:48.56] whatever."
[L1044] [34:49.80] So, uh I'm curious if you see more
[L1045] [34:52.68] cheating on your end and um yeah,
[L1046] [34:55.76] generally if you're catching more of
[L1047] [34:57.80] dishonesty.
[L1048] [34:59.64] >> Statistically Statistically we are not
[L1049] [35:01.04] catching more. I would like to think
[L1050] [35:04.08] that the
[L1051] [35:06.04] behave the misbehavior has not markedly
[L1052] [35:08.44] increased if only because we, like a lot
[L1053] [35:11.04] of intro courses around the world,
[L1054] [35:13.36] um have a tradition of looking for
[L1055] [35:15.64] academic dishonesty, plagiarism, code
[L1056] [35:17.44] that was copied and pasted off the
[L1057] [35:18.92] internet or YouTube video. And we,
[L1058] [35:20.72] within CS50, like a lot of peer
[L1059] [35:22.56] institutions, are very good at catching
[L1060] [35:24.16] that. Like we have tools that
[L1061] [35:25.24] cross-compare all of student submissions
[L1062] [35:26.80] against each other, against GitHub
[L1063] [35:28.16] repositories of past submissions that we
[L1064] [35:29.84] have, of YouTube videos that have been
[L1065] [35:31.16] transcribed. So, we have historically
[L1066] [35:35.88] administratively disciplined, so to
[L1067] [35:37.44] speak, between 5 and 10% of CS50 student
[L1068] [35:40.28] body every semester. And that's kind of
[L1069] [35:42.92] a norm among across peer institutions,
[L1070] [35:44.92] you know,
[L1071] [35:45.80] upper bound of roughly 10%. There's
[L1072] [35:47.88] certainly probably some percentage of
[L1073] [35:49.92] students who have been cheating in some
[L1074] [35:52.24] form all these years and never have been
[L1075] [35:54.32] detected.
[L1076] [35:55.64] But just based on the rigor with which
[L1077] [35:57.32] we go through this, the messaging
[L1078] [35:58.72] throughout the course, and like I like
