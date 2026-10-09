Chunk 3; segments 706–1058. Start may repeat the previous chunk for context.

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

Source ID: source-238007c2e5a842c7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_P_vs_NP,_Zero-Knowledge_Proofs,_Quantum_Computation_Avi_Wigderson_en.txt
Video: https://www.youtube.com/watch?v=5GUcvSAJcJw

[L715] [33:15.04] computation
[L716] [33:16.72] uh you cannot improve that I not
[L717] [33:20.24] describe you know this restricted models
[L718] [33:23.52] but some natural restricted models
[L719] [33:26.40] You cannot beat this.
[L720] [33:29.68] And what Ryan Williams descri
[L721] [33:33.12] found out last year is that in fact much
[L722] [33:36.32] better can be done. Any computation that
[L723] [33:40.32] runs in time t can be simulated by
[L724] [33:42.48] another algorithm that uses only square
[L725] [33:44.96] root of t space far far less than you
[L726] [33:48.56] know before. And uh the algorithm is
[L727] [33:52.08] quite uh uh sophisticated and uses an
[L728] [33:56.64] earlier result of uh James Cook, the son
[L729] [33:59.92] of Steve Cook of MP completeness and Ian
[L730] [34:03.44] Mer that was you know an essential
[L731] [34:06.48] technical ingredient but anyway uh you
[L732] [34:10.00] can you know there's a a really
[L733] [34:13.12] interesting uh way to to save space very
[L734] [34:16.96] very non-trivial way to save space.
[L735] [34:19.52] Again this algorithm will run in a lot
[L736] [34:22.16] of time but at least you you have a
[L737] [34:23.84] sense that uh yeah there the two
[L738] [34:26.48] parameters are related in a highly
[L739] [34:28.16] non-trivial way.
[L740] [34:29.36] >> Is this for a a general problem or
[L741] [34:31.76] >> general problem for touring machines?
[L742] [34:34.16] >> Okay.
[L743] [34:34.64] >> It may not work on random access
[L744] [34:36.40] machines or Yeah. What's the the trick I
[L745] [34:40.24] if you could explain intuitively or is
[L746] [34:42.24] it too deep to explain in
[L747] [34:45.28] >> it is
[L748] [34:47.12] you know really technically explaining
[L749] [34:49.36] it it's too deep but let me I'll give
[L750] [34:52.08] you a much earlier result which sort of
[L751] [34:55.60] indicates that really mysterious things
[L752] [34:58.72] can be done in small space.
[L753] [35:01.68] uh again it's uh probably yeah over 40
[L754] [35:04.96] years ago people discovered the
[L755] [35:06.72] following Dave Barington discovered the
[L756] [35:09.52] following really interesting uh
[L757] [35:12.00] phenomena. So suppose all you want is to
[L758] [35:14.32] count. I give you a sequence of bits and
[L759] [35:17.36] bits and you you want to count. You say
[L760] [35:21.28] you want to know whether there are more
[L761] [35:22.88] zeros than ones like the majority
[L762] [35:25.20] problem. Who wants the vote? Zeros or
[L763] [35:27.68] ones. Okay. Well, you can count. You can
[L764] [35:31.52] just add them up. And this takes
[L765] [35:33.84] logarithmic space.
[L766] [35:36.16] And it seems that the best you can do. I
[L767] [35:37.84] mean you want to count up to n
[L768] [35:40.64] to represent n takes login bits right I
[L769] [35:44.40] mean whatever n or the sum any number
[L770] [35:46.40] between one and takes login bit it seems
[L771] [35:49.20] essential
[L772] [35:51.52] it turns out that there's an algorithm
[L773] [35:54.88] I have to define exactly how it works it
[L774] [35:59.76] um I I will not define let me I will not
[L775] [36:02.80] define exactly how it works but it solve
[L776] [36:05.52] this problem in constant space. It seems
[L777] [36:08.96] like you can count arbitrarily high.
[L778] [36:12.40] All you need is access to whatever bit
[L779] [36:14.56] you like whenever you like. I want the
[L780] [36:16.56] 17th one. I want the 81st one. I want if
[L781] [36:20.56] you can uh have random access to the
[L782] [36:23.68] bits, even if you have constant space,
[L783] [36:26.72] you can tell whether there are more
[L784] [36:28.72] zeros than ones or ones and zeros
[L785] [36:31.36] regardless how long the input is. The
[L786] [36:34.16] trick is that somehow you use
[L787] [36:36.48] non-commutive algebra. You use something
[L788] [36:40.72] you know non-commutive algebra is not a
[L789] [36:42.88] because everybody's familiar with
[L790] [36:44.56] non-commutive things. I mean you we
[L791] [36:47.36] usually put the cars behind the horse
[L792] [36:49.92] and not in front of the horse. It
[L793] [36:51.60] matters or in software engineering we do
[L794] [36:54.72] this before that or it's very important.
[L795] [36:57.28] The order of things matter. uh uh so you
[L796] [37:02.40] can think about uh uh
[L797] [37:06.48] applying permutations one after the
[L798] [37:09.12] other you know if I rotate
[L799] [37:12.72] a circle and then take a mirror image it
[L800] [37:16.24] will give me the so these are two
[L801] [37:18.16] permutations right I mean say I have end
[L802] [37:20.32] points in a circle can shift it by one
[L803] [37:23.60] or I can uh you know let's say flip it
[L804] [37:26.40] around some uh diameter
[L805] [37:30.48] There are two permutations and and they
[L806] [37:33.12] don't commute. I mean if I first flip
[L807] [37:35.36] and then rotate I'll get something else
[L808] [37:37.52] if I first rotated and yeah think of all
[L809] [37:41.12] the points as colored by yeah so it's
[L810] [37:44.24] they don't commute. Bington is using uh
[L811] [37:48.08] you know he's somehow encoding the bits
[L812] [37:50.08] in the input by permutations
[L813] [37:53.60] not large permutations permutations of
[L814] [37:55.84] size five and somehow when he sees a one
[L815] [37:58.88] he maybe rotates and when he sees a zero
[L816] [38:01.60] he flips and the non-commutivity of this
[L817] [38:07.12] um u of these operations
[L818] [38:11.20] allow me to carry out a general formula
[L819] [38:15.52] a formula of ns and os and knots you
[L820] [38:19.44] know uh any formula like this formula
[L821] [38:23.12] that uh let's say of some size s uh it
[L822] [38:28.80] allows him to carry out this computation
[L823] [38:31.68] to really simulate the ends and os and
[L824] [38:34.32] not in this uh formula by rotations and
[L825] [38:38.08] flips of this uh you know five
[L826] [38:41.84] side sided pentagon Okay. And uh so just
[L827] [38:47.12] to remember the configuration of this
[L828] [38:49.52] pentagon, you need I don't know five
[L829] [38:51.92] bits or right. So you need constant
[L830] [38:56.00] space. How this captures the you know
[L831] [39:00.48] the computation? I can tell you you know
[L832] [39:02.80] one more sentence maybe it will not be
[L833] [39:05.76] uh clear to um
[L834] [39:10.00] everybody but
[L835] [39:12.32] you this non-commuting things
[L836] [39:16.08] uh you can you can do the following type
[L837] [39:18.48] of operation
[L838] [39:20.24] uh do rotate do flip then rotate back
[L839] [39:24.80] and flip back. This is called the
[L840] [39:27.92] commutator and it it can simulate an
[L841] [39:31.44] endgate
[L842] [39:33.60] the you know I can
[L843] [39:36.64] it's too much to describe in words
[L844] [39:38.56] without a board how it does it but
[L845] [39:41.28] there's a very famous analogy which is a
[L846] [39:44.08] riddle uh which if nobody I mean it's a
[L847] [39:47.68] good riddle to to think about uh which
[L848] [39:50.88] really captures this uh endgate problem.
[L849] [39:53.84] You you want to hang a painting in the
[L850] [39:57.20] following way. You have a painting uh
[L851] [40:00.00] it's the it has a string connecting the
[L852] [40:02.96] the two side but you want to hang it not
[L853] [40:05.76] on one nail but on two nails. Okay.
[L854] [40:09.52] There are two nails on the wall and you
[L855] [40:12.72] can do with the string whatever you want
[L856] [40:14.88] and the property you want
[L857] [40:17.68] is that if the two nails are there it's
[L858] [40:21.68] hanging every everybody's happy. If you
[L859] [40:24.72] pull out one nail doesn't matter which
[L860] [40:28.96] the picture falls to the floor.
[L861] [40:32.48] How would you loop the string around
[L862] [40:34.40] these nails so that you know this
[L863] [40:36.88] happens? Clearly this is an end gate or
[L864] [40:38.96] an O gate. Right. If one Yeah. And this
[L865] [40:43.04] has to do I mean if anybody finds a
[L866] [40:45.52] solution they realize what
[L867] [40:47.92] non-commutivity I'm talking about. And
[L868] [40:51.12] uh yeah it's a nice middle. Anyway so
[L869] [40:54.08] this type of trick where you can really
[L870] [40:57.36] um um this type of result you can really
[L871] [41:01.28] do uh in small space things you wouldn't
[L872] [41:04.40] imagine possible. It's a striking
[L873] [41:06.32] example. It's really when I heard this
[L874] [41:09.20] result first time I was the postto
[L875] [41:12.56] um and somebody told me uh uh and I just
[L876] [41:17.28] didn't believe it's possible. I mean you
[L877] [41:18.96] cannot count arbit high with a yeah. So
[L878] [41:22.96] yeah so the the trick that cook and
[L879] [41:26.56] merits have in their algorithm is a
[L880] [41:29.52] solution to a natural problem in much
[L881] [41:32.80] less space than you would think
[L882] [41:36.24] uh and uh it uses
[L883] [41:40.24] some sense tricks of this nature.
[L884] [41:44.00] So if you're counting arbitrarily large
[L885] [41:46.64] that is information and you're saying
[L886] [41:50.08] like maybe the intuition is that
[L887] [41:51.76] information is encoded in the sequence
[L888] [41:53.84] of operations. It is encoded. Yeah, of
[L889] [41:57.52] course you are not you are not
[L890] [41:59.12] delivering the final count. You just say
[L891] [42:01.92] whether there are more zeros than ones.
[L892] [42:04.08] If you have to write down of course you
[L893] [42:05.92] need if the answer takes
[L894] [42:09.12] some number of bits long then you need
[L895] [42:11.52] this this number to write it down. If
[L896] [42:14.48] you have a decision problem say like yes
[L897] [42:18.24] or no like are there more zeros than
[L898] [42:20.48] ones then you can do it for any any size
[L899] [42:24.00] input in constant space. Yeah
[L900] [42:26.64] >> that's incredible.
[L901] [42:27.68] >> It's pretty pretty incredible. Yeah. And
[L902] [42:30.56] by the way, this is a highly applicable
[L903] [42:32.72] result. It's used in cryptography in a
[L904] [42:34.80] fun in fundamental ways. It's useful.
[L905] [42:37.92] Yeah, it's used in various places and
[L906] [42:41.12] it's yeah, an extremely useful result
[L907] [42:44.48] here. By the way, unlike the Ryan
[L908] [42:46.72] Williams result, if you have a formula
[L909] [42:48.72] of size S, you can do it in constant
[L910] [42:51.36] space and the time of this algorithm
[L911] [42:54.48] does not blow up really a lot. It's just
[L912] [42:57.68] quadratic. So it's quadratic time. So
[L913] [43:00.48] this is something actually doable,
[L914] [43:02.64] useful, efficient and yeah, and it's
[L915] [43:05.52] also magical.
[L916] [43:06.80] >> We talked about the equivalence between
[L917] [43:09.12] um these MPMPlete problems and then I
[L918] [43:11.68] know in practice a lot of people to
[L919] [43:14.80] solve the other problems they just use
[L920] [43:16.48] SAT solvers.
[L921] [43:17.44] >> Yeah,
[L922] [43:18.80] >> I would have thought that would be less
[L923] [43:20.80] efficient though because you got to kind
[L924] [43:22.16] of translate it and then you're doing it
[L925] [43:23.68] in almost like a different problem
[L926] [43:25.52] space. Yeah, you you usually also
[L927] [43:27.60] enlarge the instance. Usually in
[L928] [43:30.88] translation you enlarge the instance. So
[L929] [43:33.20] what your question is why do people use
[L930] [43:35.84] cell service? I would say that uh
[L931] [43:38.80] there's no problem other than
[L932] [43:42.32] satisfiability that people uh uh thought
[L933] [43:46.96] so hard about
[L934] [43:49.12] really uh optimizing the huristics
[L935] [43:53.92] that uh efficiently work on many
[L936] [43:56.40] instances. There are very very clever
[L937] [43:58.72] ways in which you can um you know try
[L938] [44:03.76] start I mean you are not going to guess
[L939] [44:05.92] all the end bits but you want to start
[L940] [44:09.76] by guessing some bits that seem more
[L941] [44:11.92] pivotal that if you like in dominoes
[L942] [44:14.88] maybe when you set them to one value
[L943] [44:17.92] they force many other many other other
[L944] [44:20.72] values to be set and if that happens you
[L945] [44:23.60] cut down your search space. So there are
[L946] [44:26.08] many heristics of this type and also
[L947] [44:28.80] more clever than this that allow to
[L948] [44:31.28] solve such liability problems. If they
[L949] [44:34.32] have such structure again the worst case
[L950] [44:37.60] it will not will not help you. There is
[L951] [44:41.68] in fact a conjecture
[L952] [44:44.24] uh this is much stronger somehow than
[L953] [44:46.40] npmpleteness
[L954] [44:48.32] uh you know np complete problems taking
[L955] [44:50.48] exponential time. He said that uh we
[L956] [44:53.68] don't expect
[L957] [44:55.52] any savings. We we expect satisfiability
[L958] [44:58.48] problems to require really uh two to
[L959] [45:02.88] some constant times n. It's not it's not
[L960] [45:06.16] going to be two to the square root n or
[L961] [45:08.80] or n to the log or something like this
[L962] [45:10.96] is you know so yeah. So but the worst
[L963] [45:14.08] case may be hard but people optimize
[L964] [45:17.12] uh attacks on many many such formulas
[L965] [45:22.16] that somehow have all sorts of
[L966] [45:24.88] structural properties arising maybe in
[L967] [45:27.52] practice and I think that's the main
[L968] [45:30.00] reason that uh they are used it's also
[L969] [45:32.56] convenient I mean uh it's very you know
[L970] [45:36.16] people do it for uh testing
[L971] [45:39.36] specification that programs protocols
[L972] [45:42.96] meet specification. They're usually the
[L973] [45:46.08] specification are usually easily
[L974] [45:48.16] translated into simple constraints and
[L975] [45:51.20] that's almost a susceptibility problem.
[L976] [45:53.84] >> We talked about all the different types
[L977] [45:55.84] of resources in an algorithm and in one
[L978] [45:59.36] of your talks you said something where
[L979] [46:02.32] you you consider randomness another
[L980] [46:05.20] resource for an algorithm. What do you
[L981] [46:07.12] mean when you say randomness is a
[L982] [46:09.12] resource for an algorithm? In the early
[L983] [46:12.48] 70s,
[L984] [46:14.24] of course, randomized algorithms existed
[L985] [46:16.88] since antiquity and everybody was
[L986] [46:19.52] tossing coins for lots of reasons and of
[L987] [46:22.32] course statisticians
[L988] [46:24.32] uh you know do sampling and use
[L989] [46:26.32] randomness for but when when
[L990] [46:29.52] algorithmics you know designing
[L991] [46:31.44] efficient algorithms became big once we
[L992] [46:34.64] have had computers uh people realized
[L993] [46:37.36] that it can really enhance all sorts of
[L994] [46:39.52] uh uh computation for example we had no
[L995] [46:43.76] idea how to test primality of a number
[L996] [46:46.80] and in the 70s uh both microabin and uh
[L997] [46:50.96] survey and sass and found proistic
[L998] [46:53.04] algorithms which are fast to test
[L999] [46:55.60] primality okay so what does it mean a
[L1000] [46:58.48] probabistic algorithm it's an algorithm
[L1001] [47:00.80] that's allowed to make random choices so
[L1002] [47:03.36] you can think that there's an internal
[L1003] [47:06.32] uh you know little person or device
[L1004] [47:08.40] inside that tosses coins Of course,
[L1005] [47:10.80] that's not what happens. There's no
[L1006] [47:12.96] little person sitting in your laptop. So
[L1007] [47:16.16] the question is where do you get these
[L1008] [47:18.08] random bits? But it's very important to
[L1009] [47:20.40] stress that in all these um probabistic
[L1010] [47:24.64] algorithms, the underlying assumption is
[L1011] [47:27.52] that the bits you get are perfect. They
[L1012] [47:29.52] are half half each one and independent
[L1013] [47:33.44] of each other. It's like a uniform
[L1014] [47:35.20] distribution on all possibilities.
[L1015] [47:38.32] Now, where do you get this? I mean,
[L1016] [47:41.12] where seriously do you get this? I mean,
[L1017] [47:42.88] if you run a probabistic algorithm of
[L1018] [47:44.88] your laptop, since it doesn't have this
[L1019] [47:47.52] person inside tossing coins, it does
[L1020] [47:50.32] something.
[L1021] [47:52.32] Well, high quality randomness of this
[L1022] [47:54.88] type uh
[L1023] [47:57.84] costs money like time and like memory.
[L1024] [48:01.52] What do I mean by cost money? You can
[L1025] [48:03.92] have a very cheap solution. you can just
[L1026] [48:06.72] I don't know measure the thermal noise
[L1027] [48:08.88] in your computer or have one of the
[L1028] [48:10.72] Intel chips uh you know um you can
[L1029] [48:14.64] measure internet traffic and sample it
[L1030] [48:16.96] and believe it's random and and all of
[L1031] [48:19.36] these things are used you can do
[L1032] [48:21.44] something mathematical have some simple
[L1033] [48:24.16] procedure that is actually deterministic
[L1034] [48:27.36] like a linear congren generator
[L1035] [48:30.24] something like this and believe it's
[L1036] [48:31.92] random or you take can take the digits
[L1037] [48:33.92] of pi it's also So you know looks random
[L1038] [48:36.80] in some sense. So there are many things
[L1039] [48:38.96] you can use but you don't know they are
[L1040] [48:41.36] random. If you want them to be random
[L1041] [48:43.20] you know one source even this is not a
[L1042] [48:46.00] perfect source but we have quantum
[L1043] [48:48.56] mechanics. People believe you know
[L1044] [48:51.12] people believe it works in in life. It
[L1045] [48:53.44] seems like a cool theory of nature.
[L1046] [48:56.08] There are all sorts of arguments about
[L1047] [48:58.48] it but let's um put them aside. They
[L1048] [49:02.40] predict that if if you measure photons
[L1049] [49:05.68] coming out from some source and you
[L1050] [49:08.80] measure their spin whether it's up or
[L1051] [49:10.72] down, the prediction is that each one is
[L1052] [49:13.44] half half and it's independent of each
[L1053] [49:16.32] other. That's very nice. But if you are
[L1054] [49:18.24] going to build this device, it's going
[L1055] [49:19.92] to cost you a lot of money
[L1056] [49:22.48] and let alone that it will not be
[L1057] [49:24.64] perfect. But let's leave this aside
[L1058] [49:27.12] anyway. Since you want high quality
[L1059] [49:29.60] randomness or you have some way of
[L1060] [49:31.36] guaranteeing I mean you are running it
[L1061] [49:33.04] really on your laptop you it's not you
[L1062] [49:35.12] know okay the paper was written we can
[L1063] [49:38.00] test primality with probabistic
[L1064] [49:39.76] algorithm now we want to run it what do
[L1065] [49:41.44] you use so it makes sense to ask lots of
[L1066] [49:44.88] questions about randomness but to
[L1067] [49:46.64] guarantee the quality of the randomness
