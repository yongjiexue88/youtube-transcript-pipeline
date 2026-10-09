Chunk 3; segments 698–1065. Start may repeat the previous chunk for context.

# Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura

Source ID: source-70f1e2ca6c128ddc
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lean_Handwritten_Math_Will_Change_Dramatically_Leonardo_de_Moura_en.txt
Video: https://www.youtube.com/watch?v=KzdYKeAqWhY

[L707] [30:50.80] Verscell all use this product to make
[L708] [30:52.96] their lives better. And the problem it
[L709] [30:55.20] solves is when you're building SAS or an
[L710] [30:57.44] AI product and you want to sell to other
[L711] [30:59.76] companies, there's all these
[L712] [31:01.28] requirements you need to meet. There's
[L713] [31:03.20] SSO, there's SKIM, there's arbback,
[L714] [31:06.48] there's audit logs. These are all things
[L715] [31:08.32] that take time to integrate but aren't
[L716] [31:10.48] the main focus of your app. Work OS is
[L717] [31:12.64] an API layer that lets you meet all of
[L718] [31:14.56] these requirements in just a few lines
[L719] [31:16.72] of code. So let's say you have a new SAS
[L720] [31:19.12] product and you want to sell to other
[L721] [31:20.72] companies. Work OS will solve all of
[L722] [31:22.96] these critical feature gaps for you. You
[L723] [31:25.68] can check them out at workos.com to
[L724] [31:28.16] learn more and get started. And I
[L725] [31:30.32] appreciate them for supporting my work
[L726] [31:32.00] and sponsoring this podcast. when I see
[L727] [31:34.24] on Twitter this, you know, major
[L728] [31:36.24] conjecture, they made headway on it,
[L729] [31:38.64] it's that they made headway on
[L730] [31:40.80] confirming something
[L731] [31:42.08] >> or or disproving. They also have uh uh
[L732] [31:45.44] this 1 million lines, they shown the
[L733] [31:47.60] conjecture was false. They have a proof
[L734] [31:49.84] showing that it's false, [snorts] but
[L735] [31:51.76] but it's a formal proof. They did not
[L736] [31:55.92] came up with a new
[L737] [31:58.88] theory or anything like that. They're
[L738] [32:01.44] coming up with a proof, right? I mean,
[L739] [32:04.32] >> at what points would you say someone
[L740] [32:06.80] should evaluate formalizing something in
[L741] [32:09.92] lean?
[L742] [32:11.92] >> I I I think if if it's safe if it's
[L743] [32:15.12] critical or if you don't understand
[L744] [32:18.16] really well, I mean this is important
[L745] [32:20.32] part. I don't really understand. Anybody
[L746] [32:23.68] that went through the process of
[L747] [32:25.92] formalizing something understands the
[L748] [32:28.00] subject way better after that. I I
[L749] [32:30.96] almost feel like I remember when I was
[L750] [32:33.44] in college people would say wow after I
[L751] [32:35.92] implement this algorithm now I
[L752] [32:38.48] understand it much better.
[L753] [32:41.36] The next level is that you implement the
[L754] [32:43.36] algorithm you prove the properties you
[L755] [32:46.24] expect
[L756] [32:48.08] your level of understanding grows.
[L757] [32:50.56] Right? I mean, uh, another cool thing is
[L758] [32:53.68] that it enables you to to be much more
[L759] [32:58.00] bold on on your optimizations
[L760] [33:01.04] because sometimes
[L761] [33:02.96] I I've seen that all the time people
[L762] [33:05.12] fear implementing optimization because
[L763] [33:07.04] they don't really understand why the the
[L764] [33:08.88] piece of software works. They feel like
[L765] [33:12.16] if I do that still works and is faster,
[L766] [33:15.12] but they are not confident with proofs.
[L767] [33:18.40] you eliminate this discomfort, right?
[L768] [33:21.36] You you can prove it's again or the AI
[L769] [33:23.68] can prove for you or find a counter
[L770] [33:25.76] example. They're good at both things.
[L771] [33:29.76] But if you were to speculate or draw
[L772] [33:31.92] into the future, maybe 3 to 5 years from
[L773] [33:34.88] now, if the cost of formalizing things
[L774] [33:38.56] goes down, how does that change
[L775] [33:40.88] software? How does that change um you
[L776] [33:44.16] know, handwritten math? Oh, I think
[L777] [33:46.80] we've changed dramatically, right? Uh,
[L778] [33:49.28] we have to keep in mind the big labs,
[L779] [33:52.00] they only start training for formal
[L780] [33:54.80] verification lean very recently, right?
[L781] [33:58.00] Seriously, before that was like, oh, is
[L782] [34:01.12] in the data sets. I mean, you don't
[L783] [34:03.12] really have the the enforcement learning
[L784] [34:06.48] pipelines to to optimize.
[L785] [34:09.28] The behavior we see today that is
[L786] [34:11.20] already amazing will get way better in
[L787] [34:14.00] the future.
[L788] [34:15.92] uh the costs will reduce programming
[L789] [34:19.28] languages like ling and rock will become
[L790] [34:22.32] more mainstream because of that
[L791] [34:25.52] uh many people are not so in the past
[L792] [34:28.08] people say oh functional programming h I
[L793] [34:31.20] don't like it
[L794] [34:33.60] but if I'm not the one that's writing
[L795] [34:35.76] most of the codes anyway
[L796] [34:38.32] it doesn't really matter what matters
[L797] [34:40.16] are the specification level right
[L798] [34:43.84] doesn't really matter how the code has
[L799] [34:46.00] been written. Yeah, I think it will
[L800] [34:48.24] change a lot because of that. At least
[L801] [34:50.40] that's the direction we are pushing
[L802] [34:52.16] into.
[L803] [34:53.52] >> What about let's say you know 10 years
[L804] [34:56.56] from now lean is everything's going
[L805] [34:58.64] really well with lean. Is that the could
[L806] [35:02.32] that be the end of handwritten math or
[L807] [35:05.04] handwritten proofs?
[L808] [35:07.44] >> I think there will be always aspects
[L809] [35:09.36] that is handwritten. The
[L810] [35:12.88] some people like to make a proof look
[L811] [35:17.28] they they want to use the proof as an
[L812] [35:21.12] artifact. You communicate ideas to
[L813] [35:23.60] others. I can't imagine there will
[L814] [35:26.32] always be people polishing making them
[L815] [35:29.36] super easy to understand for for another
[L816] [35:32.48] human to communicate ideas to other
[L817] [35:35.04] people. There will always be people like
[L818] [35:37.36] that. The same way today we have people
[L819] [35:40.08] that uh we have machines that build
[L820] [35:43.12] furniture but people they like to to
[L821] [35:47.20] create them by hands and polish them
[L822] [35:50.00] make them perfect. This will always
[L823] [35:53.04] exist but it will be a mixture. I I
[L824] [35:56.56] would be surprised as if there's someone
[L825] [35:58.80] that's completely
[L826] [36:01.52] AI is not in their workflow somehow
[L827] [36:05.28] right I mean you'll be hybrids many
[L828] [36:08.40] hybrids some people don't like feel this
[L829] [36:11.60] uncomfortable about this future but for
[L830] [36:14.56] me super exciting because I view
[L831] [36:17.36] developing software is super painful
[L832] [36:19.68] process
[L833] [36:21.60] and with AI it's crazy how it bring you
[L834] [36:26.56] awareness of how many steps are just uh
[L835] [36:32.40] repetitive
[L836] [36:34.08] and there's no creativity you're just
[L837] [36:36.64] patching things and AI automates removes
[L838] [36:40.56] lots of this pain right I mean
[L839] [36:44.16] I cannot go back to
[L840] [36:47.28] I'm looking forward to this future you
[L841] [36:49.04] describe
[L842] [36:50.32] >> yeah I guess the thing that gives people
[L843] [36:52.88] I mean I'm guessing The discomfort is
[L844] [36:56.08] the worry that if it kept going then you
[L845] [36:59.84] know then we need less mathematicians or
[L846] [37:02.72] less computer scientists or something
[L847] [37:04.32] like that.
[L848] [37:06.08] People don't see that AI can bring more
[L849] [37:08.08] people. Uh uh there's also the
[L850] [37:10.88] specification. I mean some I've see
[L851] [37:13.52] people saying oh we are going to leave
[L852] [37:16.24] AI we'll come up with new math. But if
[L853] [37:19.84] there's no connection to our world,
[L854] [37:24.88] this is some alien thing that's going by
[L855] [37:27.44] itself. You need an interface. Uh for
[L856] [37:30.80] example, we want to build programs
[L857] [37:32.56] because you want to accomplish
[L858] [37:33.76] something. Uh just something whatever it
[L859] [37:37.04] is has an specification. There will be
[L860] [37:39.84] always humans in the loop saying this is
[L861] [37:41.76] what we need. This is what we want.
[L862] [37:44.80] Right? writing this interface
[L863] [37:47.12] interacting with the AI.
[L864] [37:49.92] The AI will have math libraries and
[L865] [37:52.40] everything to prove things about these
[L866] [37:56.00] these programs we are writing these
[L867] [37:57.68] artifacts this this whatever we are
[L868] [38:00.64] trying to build
[L869] [38:03.20] but we have to be able to interact these
[L870] [38:06.80] libraries we have to understand the
[L871] [38:08.80] abstractions that are there
[L872] [38:12.32] I I don't see humans being eliminated we
[L873] [38:14.56] are always going to be there in the
[L874] [38:16.00] interface
[L875] [38:17.60] righth uh we are telling them what we
[L876] [38:21.04] want right I mean uh specifications will
[L877] [38:24.64] be there I can see people always writing
[L878] [38:27.60] codes
[L879] [38:29.20] uh even another thing a lot of people
[L880] [38:32.48] like to write they say I love coding my
[L881] [38:35.20] interpretation is they love to write
[L882] [38:37.44] prototypes
[L883] [38:38.96] I this is fun this is the fun part to
[L884] [38:41.12] try a new idea but to transform it into
[L885] [38:44.16] a product is never fun I can tell you
[L886] [38:46.88] it's never fun
[L887] [38:49.04] and I can take over these parts and
[L888] [38:51.52] nobody really likes doing
[L889] [38:54.24] >> outside of lean. I I know you worked on
[L890] [38:56.80] the Z3 SMT solver
[L891] [38:59.60] >> and that sounds like a really difficult
[L892] [39:02.40] thing to build. So first, what is that
[L893] [39:05.04] solver in your words? And um yeah, how
[L894] [39:08.32] does it differ from a SAT solver?
[L895] [39:10.64] >> Yeah, I s long is going to be yes 20
[L896] [39:15.04] years ago. I started history. I mean
[L897] [39:17.44] when I joined Microsoft research
[L898] [39:20.56] uh yeah this is a semmit to solver is
[L899] [39:23.28] like a set solver but you have
[L900] [39:24.80] backgrounds theories like you [snorts]
[L901] [39:27.28] have support for arithmetic
[L902] [39:29.44] for arrays uh these are not random
[L903] [39:33.20] choices right this is because we use for
[L904] [39:36.24] doing test case generation in software
[L905] [39:38.56] for doing software verification
[L906] [39:41.20] link fully Z3 is fully automated is a
[L907] [39:44.24] push button although lens Z3 are called
[L908] [39:47.28] ton provers. They are completely
[L909] [39:49.60] different beasts. Z3 is fully automatic.
[L910] [39:52.96] Ling is interactive. Has automation but
[L911] [39:55.60] it's interactive.
[L912] [39:58.96] Tree is not a programming language. It's
[L913] [40:00.96] like you can do is more like a
[L914] [40:02.72] constraint solver.
[L915] [40:04.88] It turns out you can prove simple things
[L916] [40:06.96] about it. Not you cannot do advanced
[L917] [40:09.60] math with abstract math. you can solve
[L918] [40:13.52] constraints with with Z3.
[L919] [40:16.24] >> What's an example of the the inputs to
[L920] [40:18.88] this SMT solver and what you get out
[L921] [40:21.84] from it?
[L922] [40:22.80] >> Oh, I I can give you one. I mean that's
[L923] [40:24.88] even in the Z3 manual. Uh you can encode
[L924] [40:28.40] a sudoko problem as a set of constraints
[L925] [40:31.52] and you can ask Z3 to solve and will
[L926] [40:34.24] give you back the answer
[L927] [40:35.60] instantaneously.
[L928] [40:37.12] For real applications, Z3 was used very
[L929] [40:40.80] successfully for finding bugs in
[L930] [40:42.64] software. Uh people would convert for
[L931] [40:45.60] example suppose that you have a path in
[L932] [40:47.36] your code you know that's has a security
[L933] [40:51.12] vulnerability but you don't know which
[L934] [40:53.60] inputs to the program allow you to
[L935] [40:56.24] execute this path. you can convert that
[L936] [40:59.52] into a set of constraints that you send
[L937] [41:02.24] to Z3 and it will say unsatisfiable
[L938] [41:06.24] which means is impossible to execute
[L939] [41:08.16] this path and you are happy or it gives
[L940] [41:11.28] you back an example saying look with
[L941] [41:13.44] this inputs you're going to be able to
[L942] [41:15.36] do it I mean and people use it for doing
[L943] [41:19.52] software verification
[L944] [41:21.92] uh but because the problem becomes
[L945] [41:24.24] undecidable
[L946] [41:26.48] at that level you have many universal
[L947] [41:28.80] quantifiers for stating properties about
[L948] [41:30.96] your program, your pre and post
[L949] [41:33.28] conditions.
[L950] [41:35.36] The server has heristics
[L951] [41:38.00] and this was all before AI. The
[L952] [41:40.80] heristics were handcoded and they will
[L953] [41:43.20] always fail and for simple things people
[L954] [41:46.64] would be very happy with the push the
[L955] [41:48.32] fact that Z3 is push button. But when
[L956] [41:51.36] the property is not trivial, they would
[L957] [41:53.36] come back saying come on I know the
[L958] [41:55.60] proof. I mean why is it we can't find it
[L959] [41:58.32] that's why ling started I started ling
[L960] [42:01.04] to make sure that we would have a system
[L961] [42:04.24] that's really good for software
[L962] [42:05.76] verification right for Z3 was successful
[L963] [42:09.20] for finding bugs but not so much for
[L964] [42:13.04] software for proving the absence of bugs
[L965] [42:16.96] it was never super successful there but
[L966] [42:20.08] len uh was born to fill this gap
[L967] [42:25.20] >> you that undecidable but in practice in
[L968] [42:27.92] the real world if you run it does it
[L969] [42:31.20] typically terminate?
[L970] [42:32.64] >> Yeah. Yeah. Great question. Uh uh Z3
[L971] [42:36.16] goes the whole complexity level, right?
[L972] [42:38.72] You you have sets uh uh you have NP
[L973] [42:42.24] complete, P space complete, XP complete.
[L974] [42:46.00] You have the whole undecidable, right? I
[L975] [42:48.88] mean uh surprisingly even for sets you
[L976] [42:53.60] can write really tiny set problems that
[L977] [42:56.16] are really hard to solve. No set solver
[L978] [42:58.40] will solve them. But in practice, the
[L979] [43:02.32] problems we get for hardware
[L980] [43:04.56] verification,
[L981] [43:06.40] uh, uh, especially if you bound
[L982] [43:08.40] everything, you say, "Oh, I'm trying to
[L983] [43:09.92] look for a bug in the first 10 steps,
[L984] [43:13.12] right? Everything's bounded. You're not
[L985] [43:15.76] trying to prove, but you're trying to
[L986] [43:18.40] capture a class like a space of
[L987] [43:22.24] scenarios, right?
[L988] [43:24.80] They are very effective than there. I
[L989] [43:27.04] mean there I I I think the lesson there
[L990] [43:30.08] is that programs and hardware
[L991] [43:33.36] they're not correct by esoteric reasons
[L992] [43:36.32] right they they are correct for very
[L993] [43:39.12] simple reasons I mean that's why these
[L994] [43:41.44] tools are super effective they [snorts]
[L995] [43:44.80] um yeah but when you get to undecidable
[L996] [43:48.40] and you're trying to prove even if the
[L997] [43:52.08] property is not trivial there I mean it
[L998] [43:55.60] runs out of team I mean and they time
[L999] [43:58.40] out frequently and [snorts] sometimes
[L1000] [44:01.04] the there's a here a colleague of mine
[L1001] [44:04.56] here at Amazon I mean like chooses the
[L1002] [44:08.00] name proof instability
[L1003] [44:11.12] because sometimes if you change the
[L1004] [44:13.28] problem you just flip I mean you have A
[L1005] [44:16.48] and B you write B and A where B and A
[L1006] [44:18.96] are complicated formulas you may fail to
[L1007] [44:21.68] prove and when she was just trying to
[L1008] [44:24.72] maintain things proof would break if
[L1009] [44:27.44] using this kind of technology. But with
[L1010] [44:29.52] lean, she she switches to lean and super
[L1011] [44:33.60] smooth, right? Because you're
[L1012] [44:35.60] controlling uh the proof
[L1013] [44:38.32] >> in the lean case. Why is it so much more
[L1014] [44:41.76] efficient?
[L1015] [44:43.12] >> Your proof is basically you can view the
[L1016] [44:45.68] sequence of steps for solving the
[L1017] [44:47.52] problem.
[L1018] [44:50.00] In in Z3, you can view that you have
[L1019] [44:51.76] only one proof step. solve, right? I
[L1020] [44:56.24] mean, you're saying you have options to
[L1021] [44:58.56] solve flags, but you have very you don't
[L1022] [45:03.20] you cannot influence what Z3 is going to
[L1023] [45:06.24] do. It's much harder to influence this
[L1024] [45:08.96] kind of system.
[L1025] [45:11.28] In in ling you can if you want to give a
[L1026] [45:13.92] step super detailed stepbystep proof you
[L1027] [45:17.28] can you can use proof automation like is
[L1028] [45:20.00] available in Z3 but you can also break
[L1029] [45:22.96] it down step by step and the fact you
[L1030] [45:26.32] can do that humans can do it but the
[L1031] [45:29.36] happy surprise is that AI can do it
[L1032] [45:32.96] because now you can say step by step why
[L1033] [45:35.68] something is true. the AI can convince
[L1034] [45:39.28] lean that
[L1035] [45:41.52] it can provide a proof. I mean
[L1036] [45:44.32] >> when you were working on Z3 and lean,
[L1037] [45:47.36] what was the most technically
[L1038] [45:49.28] challenging
[L1039] [45:51.44] part that you had to build for for
[L1040] [45:53.60] either project?
[L1041] [45:55.20] >> I understand how much harder ling is in
[L1042] [45:58.96] comparison of Z3 this is or of a
[L1043] [46:01.52] magnitude harder. I mean uh one explan I
[L1044] [46:05.84] I talked to many colleagues about that
[L1045] [46:08.00] why I felt like L was so much harder I I
[L1046] [46:12.72] think it's the surface the interface
[L1047] [46:14.72] with humans is way
[L1048] [46:17.76] for the tree you have defined as a
[L1049] [46:20.24] language for it's called SMT lib it's
[L1050] [46:24.64] very simple language it's not meant for
[L1051] [46:27.60] humans it's meant for tools I mean it is
[L1052] [46:30.16] uses just the back ends of many
[L1053] [46:31.92] different tools
[L1054] [46:33.04] Someone's gener some program is
[L1055] [46:34.88] generating input for Z3 and people
[L1056] [46:38.32] expect a counter example or saying it's
[L1057] [46:41.84] impossible is unsatisfiable to come up
[L1058] [46:43.92] with the counter example. The interface
[L1059] [46:46.88] is really really simple, right? You you
[L1060] [46:50.40] can view it as a command line tool that
[L1061] [46:52.64] you pass this file on this very low
[L1062] [46:55.76] level language that's super easy to
[L1063] [46:57.68] parse and you come back with yes or no.
[L1064] [47:02.08] And l you have is a programming
[L1065] [47:03.84] language. You have libraries. You have
[L1066] [47:06.48] mechanisms. You have interactivity. You
[L1067] [47:08.32] have user interface. You have LSP. You
[L1068] [47:10.72] have build system. You have G. You have
[L1069] [47:12.72] that is so vast. I mean that's
[L1070] [47:18.40] another challenging part for me as I
[L1071] [47:22.00] mentioned Z3 was a back end.
[L1072] [47:24.80] The Z3 users
[L1073] [47:27.04] are very sophisticated software
[L1074] [47:30.08] developers people that speak the same
