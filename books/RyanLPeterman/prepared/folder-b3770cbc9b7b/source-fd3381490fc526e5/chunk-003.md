Chunk 3; segments 689–1044. Start may repeat the previous chunk for context.

# Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg

Source ID: source-fd3381490fc526e5
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_TypeScript_10x_Faster_Typescript,_Why_AI_Won't_Replace_SWEs_Anders_Hejlsberg_en.txt
Video: https://www.youtube.com/watch?v=cywK3XYYJ2o

[L698] [27:14.64] had to write that because your native
[L699] [27:16.72] language wasn't really intended to
[L700] [27:18.96] target that particular community. So, I
[L701] [27:22.32] think it very much depends on
[L702] [27:25.44] your what what your problem is
[L703] [27:27.28] affinitized with. Um, and and often PF
[L704] [27:31.60] of your code isn't the bottleneck. I
[L705] [27:34.40] mean, like look at Python. I mean right
[L706] [27:37.28] it's it's used to basically script and
[L707] [27:39.92] all of the LLM training in in the world
[L708] [27:42.32] right I mean which clearly a lot of that
[L709] [27:44.96] code is ultra timer critical uh but
[L710] [27:47.68] that's written in native code right and
[L711] [27:49.20] then you use Python as the orchestration
[L712] [27:51.04] language and in a sense in a web server
[L713] [27:53.60] you know like TypeScript is just an
[L714] [27:55.20] orchestrator you know of talking to a
[L715] [27:58.16] database and doing this and that what
[L716] [27:59.76] and and and the things that the things
[L717] [28:01.68] that that ultimately control the
[L718] [28:03.76] performance of applications like that
[L719] [28:05.36] aren't necessarily
[L720] [28:07.20] whether that inner for loop is running
[L721] [28:10.40] as as as native code or not which
[L722] [28:13.04] actually it is because of the JIT anyway
[L723] [28:15.92] right I mean so
[L724] [28:18.56] I mean measure measure first and then
[L725] [28:22.16] make decisions right because you always
[L726] [28:24.08] get surprised when you measure
[L727] [28:26.88] >> when you talk about how much faster it
[L728] [28:28.64] was too one of my immediate thoughts is
[L729] [28:31.44] why wasn't it done sooner
[L730] [28:33.44] >> you know at the time we started
[L731] [28:35.52] TypeScript script. I don't know that we
[L732] [28:37.60] had ever envisioned that people would be
[L733] [28:39.84] writing projects that are the size of
[L734] [28:42.08] the projects that people are now writing
[L735] [28:44.08] in Typescript, right? Like Visual Studio
[L736] [28:47.36] Code is like 2.3 million lines of code.
[L737] [28:50.24] I mean, we have in in-house projects
[L738] [28:52.32] that are over 10 million lines of of of
[L739] [28:55.20] code, which is insanity. We would have
[L740] [28:57.36] just at the time gone, well, that's
[L741] [28:58.80] clearly no one's ever going to do that,
[L742] [29:00.72] right? But that was a decade ago or more
[L743] [29:02.88] than a decade ago, right? We started in
[L744] [29:04.64] 2012 with the TypeScript project and the
[L745] [29:06.64] world looked very different and so
[L746] [29:08.56] gradually people have started writing
[L747] [29:11.68] larger and larger and larger projects,
[L748] [29:13.68] right? And at the same time, our
[L749] [29:16.72] compiler has gotten smarter and smarter.
[L750] [29:18.56] We've added all sorts of cool features
[L751] [29:20.48] like union types and discriminated
[L752] [29:22.48] unions and control flow analysis and
[L753] [29:24.80] blah blah blah. And all of these things
[L754] [29:28.32] make our type checking even better, but
[L755] [29:30.24] it also makes it go a little slower
[L756] [29:32.00] every time we add a new feature. Right?
[L757] [29:33.76] In fact, our TypeScript 6 runs only
[L758] [29:35.92] about 50% of the speed of TypeScript 1.5
[L759] [29:39.92] for example. But TypeScript 1.5 also did
[L760] [29:42.72] a whole lot less. Um, so projects have
[L761] [29:46.00] gotten bigger and the compiler does
[L762] [29:48.24] more. All of which [laughter]
[L763] [29:51.04] detract from your effective output. And
[L764] [29:53.36] as I mentioned, Mors law also
[L765] [29:56.24] unfortunately stopped delivering faster
[L766] [29:58.40] CPUs and JavaScript keeps you from
[L767] [30:00.72] taking advantage of the additional
[L768] [30:02.40] cores. And it's not clear that we could
[L769] [30:04.88] have foreseen all of that, right? But
[L770] [30:07.36] but but it's just the way it panned out,
[L771] [30:10.16] right? [snorts]
[L772] [30:11.12] >> Open AAI, Enthropic, Curser, and
[L773] [30:14.08] Verscell all use this product to make
[L774] [30:16.32] their lives better. And the problem it
[L775] [30:18.48] solves is when you're building SAS or an
[L776] [30:20.72] AI product and you want to sell to other
[L777] [30:23.04] companies, there's all these
[L778] [30:24.56] requirements you need to meet. There's
[L779] [30:26.56] SSO, there's skim, there's arbback,
[L780] [30:29.76] there's audit logs. These are all things
[L781] [30:31.60] that take time to integrate but aren't
[L782] [30:33.76] the main focus of your app. Work OS is
[L783] [30:36.08] an API layer that lets you meet all of
[L784] [30:37.92] these requirements in just a few lines
[L785] [30:40.16] of code. So let's say you have a new SAS
[L786] [30:42.56] product and you want to sell to other
[L787] [30:44.16] companies. work OS will solve all of
[L788] [30:46.40] these critical feature gaps for you. You
[L789] [30:49.12] can check them out at workos.com to
[L790] [30:51.60] learn more and get started. And I
[L791] [30:53.76] appreciate them for supporting my work
[L792] [30:55.44] and sponsoring this podcast. Jira by
[L793] [30:58.16] Atlassian isn't just for tracking work
[L794] [31:00.24] anymore. Now you can pick your favorite
[L795] [31:02.08] AI agent to assign tasks to and they'll
[L796] [31:04.80] get access to the rich context that's
[L797] [31:06.80] already in Jira. When the agent is done,
[L798] [31:09.12] it surfaces a pull request. That way you
[L799] [31:11.44] can get more done with your favorite
[L800] [31:13.04] agents all in one place. Learn more at
[L801] [31:16.00] jira.dev. That's jir.dev.
[L802] [31:20.72] Appreciate them for sponsoring the
[L803] [31:22.16] podcast. And back to the show. When I
[L804] [31:24.72] first became a software engineer and I I
[L805] [31:27.20] went to start working at Facebook at the
[L806] [31:29.44] time, they had this popular framework
[L807] [31:32.24] called Flow, which was
[L808] [31:34.16] >> doing type inference on top of
[L809] [31:36.72] JavaScript. It was this thing that would
[L810] [31:38.16] take a long time.
[L811] [31:39.12] >> Yep. And then I' I'd never hear about it
[L812] [31:41.36] these days. So it sounds like Typescript
[L813] [31:44.40] won if there was a competition to
[L814] [31:46.40] typing.
[L815] [31:47.12] >> There was a bit of it. Yeah. In in in
[L816] [31:49.12] the early days. Um I think the thing
[L817] [31:52.64] that worked for us was actually the fact
[L818] [31:54.88] that we were self-hosted which made it a
[L819] [31:57.52] lot easier for the community to
[L820] [31:58.88] contribute to the project. [snorts]
[L821] [32:01.28] Flow was written as I recall in camel.
[L822] [32:04.88] Um, and so in order to contribute to
[L823] [32:07.52] flow, you had to go learn a whole
[L824] [32:09.20] different way of programming and and in
[L825] [32:11.20] a in a different language, right? And
[L826] [32:13.44] Float also didn't really focus all that
[L827] [32:15.84] much on
[L828] [32:17.60] IDE based tooling,
[L829] [32:20.00] which we knew full well going in. We're
[L830] [32:22.48] writing a compiler, but we're not
[L831] [32:23.76] writing a compiler in order to generate
[L832] [32:26.16] machine code. We're writing it to make
[L833] [32:27.92] better tooling. That was why we wrote
[L834] [32:30.08] it, you know, and so right there
[L835] [32:33.04] handinhand with our compiler, we had a
[L836] [32:35.12] language service. It was deeply
[L837] [32:36.56] integrated into Visual Studio, Visual
[L838] [32:38.48] Studio Code, all sorts of other editors
[L839] [32:40.64] through an open protocol, you know, and
[L840] [32:42.72] that just that's where that was the
[L841] [32:46.32] problem that needed solving, right? I
[L842] [32:48.32] mean, it's not it's it's nice to have a
[L843] [32:50.48] type checker, but boy, you you want
[L844] [32:52.48] that. You also want statement
[L845] [32:53.92] completion. You wanted red squiggies.
[L846] [32:55.92] You want like I mean, you want it
[L847] [32:57.36] interactive, right?
[L848] [32:59.12] So I know in your career you've you've
[L849] [33:01.28] worked on uh multiple programming
[L850] [33:03.44] languages. What does it take to build a
[L851] [33:06.08] programming language? Well, first I'll
[L852] [33:09.92] say that the world needs another
[L853] [33:11.52] programming language like it needs
[L854] [33:12.72] another hole in the head. I mean it it's
[L855] [33:14.48] it's like you you kind of got to be a
[L856] [33:16.64] certain [laughter] kind of of person to
[L857] [33:20.08] to even embark on it to begin with,
[L858] [33:22.16] right? It's a super fascinating area of
[L859] [33:25.44] of computer science and it's one that's
[L860] [33:27.44] been around ever since the beginning of
[L861] [33:29.92] of of computers. Now, every compiler,
[L862] [33:33.28] every language has a whole bunch of
[L863] [33:35.60] things you need to to understand like
[L864] [33:37.20] parsers and scanners and lexers and code
[L865] [33:39.28] generators and and and and whatever,
[L866] [33:41.60] right? But but that's sort of the
[L867] [33:44.08] mechanics of implementing the language.
[L868] [33:46.88] And then there's the design of the of
[L869] [33:49.68] the language, sort of the art of making
[L870] [33:53.36] it feel right and whatever, right? And I
[L871] [33:55.84] I think you sort of have to master both.
[L872] [33:59.36] And then you also got to appreciate that
[L873] [34:01.28] like every new language is actually only
[L874] [34:03.60] 10% new and then it's 90% the same
[L875] [34:06.56] drudgery that every other language has
[L876] [34:08.32] to go do. And so be prepared for a lot
[L877] [34:11.12] of work that maybe isn't as interesting,
[L878] [34:14.40] you know.
[L879] [34:16.48] And then finally maybe I'll say that you
[L880] [34:19.20] know like never forget there that you
[L881] [34:21.92] you stand on the shoulders of giants. I
[L882] [34:24.40] mean you you in order to make a great
[L883] [34:26.32] programming language you got to
[L884] [34:27.52] understand a bunch of other programming
[L885] [34:28.96] languages first uh and understand all
[L886] [34:31.60] the all the distinctions between the
[L887] [34:33.52] different styles of programming like
[L888] [34:34.88] procedural and object-oriented or
[L889] [34:36.48] functional or what have you. Um
[L890] [34:40.08] and then last but not least it's like
[L891] [34:43.12] it's a long game. I mean, it is probably
[L892] [34:45.84] a longer game than anything else. I
[L893] [34:47.76] mean, like every language project I've
[L894] [34:51.76] worked on, I've worked on each of them
[L895] [34:53.76] for at least 10 years. Um, and shipped
[L896] [34:57.68] multiple versions, and it's really never
[L897] [34:59.84] until version three that it truly starts
[L898] [35:02.24] to get okay. Do you know what I mean?
[L899] [35:05.20] And, and it just takes an incredible
[L900] [35:07.12] amount of devotion to to that. So, you
[L901] [35:09.20] got to really not be the type that tires
[L902] [35:11.52] of a problem quickly and then moves
[L903] [35:13.12] along. that you're not meant to do
[L904] [35:14.96] language design.
[L905] [35:17.28] And you see that too if when you talk to
[L906] [35:19.44] language designers in the industry,
[L907] [35:20.80] they've been doing it for a long time.
[L908] [35:22.96] >> You mentioned those two parts. There's
[L909] [35:24.56] the the objective pieces that you need
[L910] [35:28.40] to implement and then there's the the
[L911] [35:31.04] art of the design and making the
[L912] [35:32.88] language I guess ergonomic for
[L913] [35:35.44] developers. When you think of that
[L914] [35:37.84] second part, that art
[L915] [35:39.68] >> and you look at other programming
[L916] [35:41.28] languages, are there any that you admire
[L917] [35:43.76] outside of the ones that you've worked
[L918] [35:45.12] on? Of course,
[L919] [35:47.04] >> learning and and and fully appreciating
[L920] [35:49.60] the beauty of functional programming has
[L921] [35:51.76] has been very educational, right? I
[L922] [35:54.00] mean, because it really is a different
[L923] [35:55.76] way of thinking about programming, a way
[L924] [35:58.72] of thinking of programming that's much
[L925] [36:00.48] closer to math than it is to
[L926] [36:04.40] machines. Um,
[L927] [36:07.28] and I think there's there's a lot of uh
[L928] [36:10.48] incredible goodness that has come from
[L929] [36:12.24] that. And and honestly even in in like
[L930] [36:14.16] like building the TypeScript project uh
[L931] [36:17.04] large portions of the TypeScript
[L932] [36:18.64] compiler are written in a highly
[L933] [36:20.48] functional style um and work on
[L934] [36:23.28] immutable data structures that are then
[L935] [36:25.60] now because of shared memory concurrency
[L936] [36:27.84] can be shared between different
[L937] [36:32.32] uh threads or processes that don't
[L938] [36:35.44] mutate the data and therefore they can
[L939] [36:37.20] share one data structure. Right? And
[L940] [36:39.52] that's incredibly powerful. But
[L941] [36:41.60] mastering this, you know, like writing
[L942] [36:43.76] islands of pure functional programming
[L943] [36:46.08] inside an imperative program and ma and
[L944] [36:48.72] and and putting it together with
[L945] [36:50.00] concurrency. I mean, it's it's it's
[L946] [36:51.36] complex, but I think functional
[L947] [36:53.28] programming has brought a lot to the
[L948] [36:54.72] world. Um, I know object-oriented
[L949] [36:56.96] programming as well. I mean, but I
[L950] [36:58.56] wouldn't single out any particular
[L951] [37:01.44] language. Every one language you you
[L952] [37:03.92] come in contact with, you learn
[L953] [37:05.28] something. You know,
[L954] [37:07.12] >> you mentioned the world doesn't really
[L955] [37:10.24] need more programming languages and uh
[L956] [37:14.32] if you think 10 years from now, do you
[L957] [37:16.08] think there'll be less programming
[L958] [37:17.52] languages than there are today?
[L959] [37:19.36] >> It's hard to say. I mean, but like I
[L960] [37:22.24] said,
[L961] [37:24.24] AI tends to favor the incumbents, right?
[L962] [37:28.56] And I I do think and I I think this has
[L963] [37:30.88] been true even before AI. The bar keeps
[L964] [37:33.44] going up for what it takes to
[L965] [37:36.40] successfully implement a programming
[L966] [37:38.64] language and create an ecosystem around
[L967] [37:40.48] it. I mean it used to be oh you just
[L968] [37:42.96] need a compiler.
[L969] [37:45.20] Well
[L970] [37:46.88] you also kind of need tooling now. I
[L971] [37:48.72] mean you need a language service you
[L972] [37:50.56] need uh you need debuggers. You need
[L973] [37:52.80] profilers. You need frameworks and
[L974] [37:54.88] libraries. You need code generators that
[L975] [37:58.24] can target all sorts of I mean it's like
[L976] [38:02.08] it just keeps getting harder and harder
[L977] [38:04.88] uh you know to to to get all the way
[L978] [38:07.20] there.
[L979] [38:08.48] >> Well, when you think about all those
[L980] [38:09.76] pieces that really they're all for the
[L981] [38:13.60] people or I mean the you know the IDE
[L982] [38:16.56] and the types and I mean the the
[L983] [38:19.84] computer looks at that too but it's so
[L984] [38:22.08] that we can read source.
[L985] [38:24.32] Maybe one day the LMS will generate
[L986] [38:27.12] machine code directly. I wonder. Um
[L987] [38:32.32] I think
[L988] [38:35.44] I think LLMs are better at what they do
[L989] [38:39.52] when when they don't have to repeat
[L990] [38:41.68] themselves a lot. I I I think like
[L991] [38:46.64] when a program is expressed in text, it
[L992] [38:49.60] is closest to its sort of ultimate
[L993] [38:54.72] condensed meaning and representation,
[L994] [38:57.20] right? If you translate it into machine
[L995] [38:59.20] code, there's an awful lot of noise in
[L996] [39:01.44] that machine code. Like all of the
[L997] [39:03.68] instructions, like half of the
[L998] [39:04.96] instructions are memory addresses that
[L999] [39:06.64] have absolutely no bearing on what's
[L1000] [39:08.48] going on here, right? So half of it,
[L1001] [39:10.16] half of all the data is noise already,
[L1002] [39:12.32] right? And then whichever register you
[L1003] [39:14.24] pick, well, that doesn't matter either
[L1004] [39:15.60] in the code generator. And honestly, you
[L1005] [39:17.28] could change your mind at any point in
[L1006] [39:18.64] time. So, so teasing the truth out of
[L1007] [39:21.28] that noise is a lot harder than if you
[L1008] [39:26.40] just have a program where the variable
[L1009] [39:27.76] is called I and whatever. And by the
[L1010] [39:29.52] way, that you can relate to the written
[L1011] [39:32.08] instruction that the user just gave you.
[L1012] [39:34.16] I mean, keep in mind that that like AI
[L1013] [39:36.80] are they're just emulators of humans in
[L1014] [39:39.28] a sense, right? I mean, they they it's
[L1015] [39:41.12] like neural networks, right? There's a
[L1016] [39:42.96] reason we have programming languages
[L1017] [39:44.72] because we're terrible at writing
[L1018] [39:46.40] machine code straight off. out of our
[L1019] [39:49.12] head, right? AI is not that different
[L1020] [39:51.92] from us, you know? So, the same would
[L1021] [39:54.96] probably be true there. when you look
[L1022] [39:57.20] back on working on C and you know
[L1023] [39:59.60] TypeScript and these language projects
[L1024] [40:02.56] they were long journeys and I think you
[L1025] [40:04.80] know one thing people might want to know
[L1026] [40:06.72] is what did you learn through those
[L1027] [40:09.28] journeys that if you knew at the
[L1028] [40:11.44] beginning of when you embarked on
[L1029] [40:12.96] working on them you you might have been
[L1030] [40:16.32] better off
[L1031] [40:19.44] gosh well each journey is is different
[L1032] [40:23.52] uh I mean like the first project I
[L1033] [40:25.52] worked on turbo Pascal. I I think
[L1034] [40:30.32] that project started back in the old
[L1035] [40:32.32] days when it was 8-bit micros and 64k of
[L1036] [40:34.88] memory and one person could do
[L1037] [40:36.56] everything themselves and have ultimate
[L1038] [40:39.28] control of everything. And so I was very
[L1039] [40:41.28] much a one-man shop, right? But that
[L1040] [40:45.76] quickly was not scalable, right? And and
[L1041] [40:48.00] and capacities of machines. So we went
[L1042] [40:50.32] for 64 to 640K and then then kaboom the
[L1043] [40:53.12] the the the lid went off, right? and you
[L1044] [40:54.96] could have as much memory as you wanted
[L1045] [40:56.88] and so not one person couldn't do it and
[L1046] [40:59.60] I had to learn to become a team player
[L1047] [41:02.00] right and that that was a big journey
[L1048] [41:05.52] for me I mean to learn to let go right
[L1049] [41:08.40] if you're a perfectionist that that that
[L1050] [41:10.24] could be hard but that's one thing that
[L1051] [41:12.24] I would say I learned there
[L1052] [41:14.24] >> well another way to word this question
[L1053] [41:16.32] is you know what's the most common
