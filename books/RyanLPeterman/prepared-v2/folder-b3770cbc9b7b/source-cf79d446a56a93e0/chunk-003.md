Chunk 3; segments 676–1035. Start may repeat the previous chunk for context.

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L685] [34:32.96] It's type oriented, class oriented. uh
[L686] [34:36.64] it actually supports the techniques of
[L687] [34:39.20] object orientation very well and it in
[L688] [34:43.76] particular follows similar's model of uh
[L689] [34:48.72] defining types defining classes and
[L690] [34:52.24] defining class hierarchies to uh handle
[L691] [34:56.96] uh groups of related uh classes but that
[L692] [35:00.88] was never all it was for instance I do
[L693] [35:05.04] not want object object oriented complex
[L694] [35:07.20] numbers. I don't want to say two dot uh
[L695] [35:12.80] uh something to
[L696] [35:16.64] uh to to get to uh some parts of uh
[L697] [35:22.00] numbers. I really want to say uh two two
[L698] [35:27.04] plus uh zed. Um, and I want that to be
[L699] [35:31.76] the end up being roughly the same as set
[L700] [35:35.76] plus two. And um, no dots, no arrows.
[L701] [35:40.88] Uh, math has developed a notation over
[L702] [35:44.48] the last 300 years or so. Uh, Decard
[L703] [35:47.60] was, I think, the first one to to use
[L704] [35:50.16] this notation and it is very good. Uh,
[L705] [35:53.84] so I I didn't want everything to to be
[L706] [35:56.72] object-oriented.
[L707] [35:58.24] Uh furthermore, I wanted
[L708] [36:02.48] things that did not require inheritance
[L709] [36:05.20] that did not require runtime resolution
[L710] [36:09.04] not to use it. Um so for arithmetic
[L711] [36:14.72] and for complex numbers and such I
[L712] [36:17.60] wanted for compatibility.
[L713] [36:20.08] I mean I was rather keen on what's
[L714] [36:22.32] called use reuse in those days but I saw
[L715] [36:26.16] it slightly different from a lot of
[L716] [36:28.08] researchers. A lot of researchers wanted
[L717] [36:30.96] to build a language a system that
[L718] [36:35.20] allowed res um reuse. I wanted to re re
[L719] [36:40.32] use things that existed. I mean forran
[L720] [36:44.08] was there uh with some great uh
[L721] [36:47.44] software. uh C was there with some great
[L722] [36:50.96] uh system software and actually helped
[L723] [36:54.40] with with compilers and such and there
[L724] [36:57.12] was a simpler that was used a fair bit
[L725] [37:00.08] too. So I wanted to reuse that and I
[L726] [37:02.64] wanted to make sure that worked and that
[L727] [37:05.68] meant I couldn't go too far away from
[L728] [37:07.84] the hardware. I couldn't build uh all of
[L729] [37:10.96] the things that was considered ideal or
[L730] [37:15.04] even the things I would consider ideal.
[L731] [37:18.48] Um this is the real world. This is the
[L732] [37:22.00] real set of problems you are attacking.
[L733] [37:24.56] And so you have to respect the
[L734] [37:26.80] constraints uh that comes with with that
[L735] [37:29.44] view of the of what you're doing. at the
[L736] [37:32.96] time that you wrote C++, C was already
[L737] [37:35.28] there and it had a weaker type system
[L738] [37:37.68] than what C++ eventually had. And I was
[L739] [37:40.88] guess your thoughts on, you know, the
[L740] [37:42.56] trade-offs behind that and why did you
[L741] [37:44.48] choose to make the typing system
[L742] [37:46.16] stronger in C++?
[L743] [37:47.92] >> Because we needed it. Um uh the weakness
[L744] [37:51.52] in the type system is one of the most
[L745] [37:54.72] obvious sources of uh errors and it's
[L746] [37:59.68] certainly one of the sources of um
[L747] [38:03.84] endless testing and uh debugging. I hate
[L748] [38:09.12] debugging. I would much rather do
[L749] [38:11.36] design. And so you can't really have
[L750] [38:15.44] either design or debugging. Some people
[L751] [38:18.72] claim they can but they can't. Uh so I
[L752] [38:22.08] want to move the the arrow over towards
[L753] [38:25.84] more design uh that helps the debugging
[L754] [38:29.44] and makes fewer uh mistakes at runtime.
[L755] [38:33.76] And uh the type system is is one of
[L756] [38:36.24] them. And uh actually what you get in C
[L757] [38:39.44] today to a large extent is stronger well
[L758] [38:43.12] no it is much stronger uh type than it
[L759] [38:45.68] was in those days and partly because of
[L760] [38:48.64] C++.
[L761] [38:50.64] Um also there's things you can't express
[L762] [38:53.68] unless you have a strong type system. Um
[L763] [38:56.40] I mentioned overloading before. Uh
[L764] [38:59.20] overloading is essential for generic
[L765] [39:01.44] programming. And if you want to write
[L766] [39:03.68] say a vector of T where T is a parameter
[L767] [39:06.72] type, you have to have overloading
[L768] [39:08.96] because you can only operate on T's
[L769] [39:11.76] providing all the T's have the same
[L770] [39:14.08] interface
[L771] [39:15.68] uh for what you need. So you you need
[L772] [39:19.04] the type system to resolve those things
[L773] [39:22.08] and that can be resolved at compile
[L774] [39:24.40] time. So the compiler gets a bit more
[L775] [39:27.52] complicated probably a bit slower
[L776] [39:30.88] but you don't do so much debugging. Um
[L777] [39:34.88] there was a largecale
[L778] [39:37.76] experiment done in Bell Labs in Chicago
[L779] [39:41.68] where they had
[L780] [39:44.16] some groups using C++ switching to C++
[L781] [39:49.04] and they wanted to know whether they
[L782] [39:52.40] were more or less uh productive.
[L783] [39:57.76] And some people claimed that the slower
[L784] [40:00.32] compilation slowed them down.
[L785] [40:03.28] And uh somebody simply measured how much
[L786] [40:06.80] compile time was used uh before after
[L787] [40:10.24] switching to C++. And they found that
[L788] [40:13.76] the amount of [snorts]
[L789] [40:17.28] commulation time of compute power was
[L790] [40:20.72] roughly identical. that is C++ was
[L791] [40:24.16] slower but you uh by about a factor of
[L792] [40:27.12] two at that time but the C people
[L793] [40:31.28] compiled twice as often.
[L794] [40:34.72] Um this is just one experiment. the
[L795] [40:38.16] factor of two is is is just one
[L796] [40:40.88] experiment but um
[L797] [40:44.96] I wanted to move towards using more
[L798] [40:48.00] compile uh compile time resolution still
[L799] [40:52.48] doing that
[L800] [40:53.92] >> I mean for every language there's this
[L801] [40:56.40] um you know dichotomy of having it being
[L802] [40:59.52] statically typed versus dynamically
[L803] [41:01.44] typed and C++ is one of the most famous
[L804] [41:04.08] statically typed languages why did you
[L805] [41:06.48] choose statically typed language
[L806] [41:09.92] >> because of the problems I wanted to um
[L807] [41:14.48] to attack. Um what do you do when you
[L808] [41:18.48] get a runtime error and
[L809] [41:22.40] in something like small talk? You go
[L810] [41:25.04] into the debugger
[L811] [41:27.52] and that makes a lot of sense if there's
[L812] [41:30.24] a programmer sitting at a screen uh
[L813] [41:32.64] getting the error. It doesn't make any
[L814] [41:34.80] sense if a telephone switch um finds a a
[L815] [41:38.72] runtime error and then you have to
[L816] [41:40.80] resolve it. Furthermore, you want
[L817] [41:43.44] performance and you want small programs
[L818] [41:46.16] to fit into memories. This is true even
[L819] [41:49.28] today because as I think 99% of all
[L820] [41:54.48] computers are embedded systems and they
[L821] [41:57.20] tend to be uh memory rest constraint
[L822] [42:01.44] and um again if you do runtime
[L823] [42:06.00] resolution you need to have enough
[L824] [42:08.24] information enough data to do the
[L825] [42:11.04] runtime resolution and I wanted to fit
[L826] [42:13.92] into small memories. uh small meaning
[L827] [42:17.92] 100 uh
[L828] [42:20.56] 120k 250k 1 megabyte things like that
[L829] [42:26.56] and I think it's still relevant uh for
[L830] [42:29.92] for many systems uh you can build a a
[L831] [42:35.12] camera like that it can still have
[L832] [42:37.12] several megabytes of memory but uh if
[L833] [42:41.20] you put in a lot of memory it gets
[L834] [42:43.28] bigger and it cost more and the battery
[L835] [42:46.56] um runs out uh quicker. So, we don't do
[L836] [42:50.80] that. Um phones and cameras and things
[L837] [42:55.36] like that are still memory constraint.
[L838] [42:58.40] And um static type languages, languages
[L839] [43:02.24] optimized for memory consumption are
[L840] [43:05.68] just better at that, which is why we use
[L841] [43:07.92] it. We're using it right now. I suspect
[L842] [43:11.52] that the microphones have uh chips in
[L843] [43:13.92] them, too. And there's a lot of C++ in
[L844] [43:17.60] that uh world.
[L845] [43:20.16] Uh the composition there is C and
[L846] [43:23.44] assembler.
[L847] [43:24.48] >> And you mentioned the the research that
[L848] [43:27.20] was done on the the compile time on you
[L849] [43:31.68] know if you catch things earlier you
[L850] [43:34.40] compile less often but maybe it takes
[L851] [43:36.64] longer. In this case, I I could see a
[L852] [43:39.28] similar analogy where um you catch
[L853] [43:42.48] errors way earlier if you have a
[L854] [43:44.16] statically typed language because the
[L855] [43:46.00] compiler is yelling at you before you
[L856] [43:48.48] put together that final thing. Whereas
[L857] [43:50.88] in dynamically typed language, the
[L858] [43:53.44] errors may come later. Comparing for a
[L859] [43:55.84] developer like which one is more time
[L860] [43:58.24] efficient.
[L861] [43:59.28] >> I I don't know any solid research on
[L862] [44:02.64] that, but you can look at it. uh
[L863] [44:07.44] JavaScript and Pythons are very are very
[L864] [44:10.48] uh popular and they are um runtime
[L865] [44:14.96] uh checked and they run much slower. I
[L866] [44:18.88] mean raw uh Python runs something like
[L867] [44:21.60] 70 times slower than raw C++ and the
[L868] [44:26.00] reason it's viable is that a lot of key
[L869] [44:30.08] uh Python libraries are written in C or
[L870] [44:32.56] C++ to get the performance and so you
[L871] [44:36.16] get the performance by actually getting
[L872] [44:39.84] to the point that I was starting out
[L873] [44:42.80] with you need a highle stuff and you
[L874] [44:45.36] need the thing that can manipulate
[L875] [44:47.44] hardware.
[L876] [44:48.56] uh here they are using two languages but
[L877] [44:51.68] uh still the same uh needs fundamental
[L878] [44:56.00] needs
[L879] [44:57.52] and uh it's easier to uh try out things
[L880] [45:01.92] in a dynamically uh check language
[L881] [45:04.48] because you don't have to know enough
[L882] [45:06.56] about the language. You don't have to
[L883] [45:08.32] know about type systems and your average
[L884] [45:12.00] uh web developer or astrophysicist
[L885] [45:16.16] is not a computer scientist and don't
[L886] [45:18.24] want to become one. So there's
[L887] [45:20.80] advantages there. But the problem is
[L888] [45:23.60] that errors that are found by the type
[L889] [45:26.08] system in a statically typed language is
[L890] [45:28.72] found at runtime later. And so as
[L891] [45:34.80] systems grow
[L892] [45:37.20] uh the performance problems uh start
[L893] [45:41.60] furthermore you find it get harder to
[L894] [45:44.64] write reliable
[L895] [45:46.64] uh software. uh you need much more unit
[L896] [45:50.40] testing for instance in a dynamic uh
[L897] [45:53.92] language because it's um
[L898] [45:58.24] well
[L899] [46:00.08] the compiler doesn't do it for you. And
[L900] [46:02.64] if you want things to guarantee to work
[L901] [46:07.60] like the telephone switch mustn't crash,
[L902] [46:10.24] your car mustn't crash, your plane
[L903] [46:12.64] mustn't crash. You want guarantees and
[L904] [46:15.68] they're harder to provide in a very
[L905] [46:18.24] flexible dynamic type system.
[L906] [46:21.04] >> One thing that I think C++ is uh
[L907] [46:25.04] infamous for is kind of like memory
[L908] [46:27.44] safety issues or kind of foot guns that
[L909] [46:30.64] exist there.
[L910] [46:31.44] >> I'm so tired of that. Um I haven't had
[L911] [46:34.80] those problems for years. Um, and
[L912] [46:38.56] somebody did a a study of
[L913] [46:42.88] the obvious problems with buffer
[L914] [46:45.28] overflows and um
[L915] [46:49.20] people hacking in using that kind of
[L916] [46:52.16] stuff and uh
[L917] [46:56.08] almost all of the uh these cases when
[L918] [46:59.12] people writing C style code or in C
[L919] [47:02.88] and uh Herb Server has a a talk with
[L920] [47:07.68] with actual numbers and they they are
[L921] [47:11.12] quite significant. It's it's sort of
[L922] [47:15.68] that kind of problems
[L923] [47:18.24] more than 90% are for people that don't
[L924] [47:21.28] write modern C++.
[L925] [47:23.52] They they use raw pointers to pass
[L926] [47:27.76] things around without
[L927] [47:30.40] um the number of elements. No fat
[L928] [47:32.64] pointers, no spans.
[L929] [47:35.04] um you you have them in C++. You can use
[L930] [47:38.16] them. You can use uh vectors. We have
[L931] [47:42.24] hardened libraries. Everybody has
[L932] [47:44.24] hardened libraries that that does the
[L933] [47:46.72] runtime checking. Uh Apple has it.
[L934] [47:50.00] Google has it. Microsoft has it. It's
[L935] [47:52.72] just not standard till now. C++ 26 has a
[L936] [47:58.40] hardened option that are standard. uh
[L937] [48:02.32] and the work I'm doing on profiles will
[L938] [48:05.84] give you a way of guaranteeing that you
[L939] [48:08.24] don't do the stupid things.
[L940] [48:10.88] Um
[L941] [48:12.56] so anyway, uh fundamentally
[L942] [48:16.64] theoretically the problem was solved
[L943] [48:18.72] many years ago and people just do what
[L944] [48:23.20] they've always done and get the problems
[L945] [48:25.20] they've always had. And uh that makes me
[L946] [48:28.64] sad and uh it's one of the things that
[L947] [48:32.32] makes me work on uh coding guidelines
[L948] [48:35.76] and on enforced profiles and on
[L949] [48:38.24] education.
[L950] [48:40.40] >> I mean education is one way to solve the
[L951] [48:42.48] problem. Is there a way to get the
[L952] [48:45.04] compiler to just prevent people from
[L953] [48:47.92] doing all those risky things?
[L954] [48:50.08] >> And is that enabled by default in modern
[L955] [48:52.48] C++ today?
[L956] [48:53.68] >> No, but it should be. I'm proposing that
[L957] [48:56.24] for C++ 29. Uh the simpler versions of
[L958] [49:00.00] that should have been in in in uh C++
[L959] [49:04.40] 26, but there are still a lot of people
[L960] [49:07.04] even in the C++ standards committee that
[L961] [49:09.76] are very devoted to uh their old code
[L962] [49:12.64] and their old ways of doing things. Um
[L963] [49:16.64] there's people who says you should only
[L964] [49:18.24] standardize what is common in industry.
[L965] [49:21.60] But when the bugs are common in
[L966] [49:23.76] industry, you should do something else.
[L967] [49:26.80] >> The standards committee is a a topic I
[L968] [49:29.04] want to talk about actually. It's
[L969] [49:30.24] interesting. I mean the language is now
[L970] [49:32.00] run um you know by a democracy and one
[L971] [49:36.40] question I want to ask you is if it was
[L972] [49:39.20] a dictatorship so you just had full say
[L973] [49:42.64] what what language features would be in
[L974] [49:45.60] that you know maybe a harder to get by
[L975] [49:47.84] >> f first of all it never was a
[L976] [49:51.52] dictatorship uh I I never had full
[L977] [49:54.56] control once you have some users in my
[L978] [49:58.48] opinion you gain some responsibility for
[L979] [50:02.40] making sure that they're helped and
[L980] [50:04.80] their stuff works. You can't keep
[L981] [50:07.44] breaking the language. That's what
[L982] [50:10.40] academic language development does. They
[L983] [50:12.80] they they break to improve all the time
[L984] [50:16.00] and then they can't maintain a user
[L985] [50:18.32] population. I didn't actually choose to
[L986] [50:20.96] have a standards committee. I I chose
[L987] [50:24.72] responsibility to the commuter to the uh
[L988] [50:28.08] to the community. But one day um two
[L989] [50:32.48] guys came in uh representing uh IBM and
[L990] [50:37.12] HP
[L991] [50:38.64] and I can't remember if it was Sun or
[L992] [50:42.32] Deck that was the third thing they
[L993] [50:44.56] represented but anyway the biggest
[L994] [50:47.52] computer and software uh suppliers in
[L995] [50:50.64] the world at the time they come into my
[L996] [50:53.20] office in it was uh
[L997] [50:56.88] ah it's 89 n and they say well pian you
[L998] [51:02.40] want to help us standardize C++ under
[L999] [51:05.92] ISO rules
[L1000] [51:08.56] and I said no I can't do that I'm still
[L1001] [51:11.04] doing experiments it's still not
[L1002] [51:13.92] complete
[L1003] [51:15.44] so they said no B you don't get it
[L1004] [51:19.68] our
[L1005] [51:22.16] organizations cannot use a language
[L1006] [51:24.64] that's not standardized
[L1007] [51:27.28] they cannot use a language that's owned
[L1008] [51:30.00] by a corporation that we might compete
[L1009] [51:33.36] with and we do sometimes.
[L1010] [51:36.72] Okay, we we we trust you of course but
[L1011] [51:40.00] not your employer.
[L1012] [51:42.48] We compete with them sometimes and you
[L1013] [51:45.44] can get run over by a boss. This uh No,
[L1014] [51:48.88] no, no. We need a standards and we need
[L1015] [51:50.64] a standards committee. So this goes on
[L1016] [51:53.44] for about an hour and they twist my arm.
[L1017] [51:55.84] Ow ow ow. And in the end they said okay
[L1018] [51:58.64] I I I I will uh standardize C++ under
[L1019] [52:02.16] anti- rules uh just like you suggest and
[L1020] [52:05.04] you need the the computer community
[L1021] [52:08.16] needs that and u by the way what's NI
[L1022] [52:13.84] rules for standardization
[L1023] [52:17.12] and um so they told me and we started a
[L1024] [52:20.08] year later but um this this was the way
[L1025] [52:23.92] it came about some very important
[L1026] [52:26.64] important organizations wanted that
[L1027] [52:29.12] standardization.
[L1028] [52:30.80] C was on the track to get standard
[L1029] [52:33.60] standardized
[L1030] [52:35.12] and AT&T being primarily a user of
[L1031] [52:39.92] software was also in favor of
[L1032] [52:42.16] standardization I found out and so they
[L1033] [52:45.20] supported it and the documentation I had
[L1034] [52:49.68] written was bases on it. Actually, I
[L1035] [52:52.72] rewrote the documentation that became
[L1036] [52:55.36] the the ARM, the annotated C++ standards
[L1037] [52:59.52] uh manual that uh gave the definition
[L1038] [53:04.48] the manual of the language and for every
[L1039] [53:08.96] feature some rationale and some way it
[L1040] [53:13.04] could be implemented or was implemented
[L1041] [53:16.44] [snorts]
[L1042] [53:16.96] and that became the the foundation
[L1043] [53:19.04] document for the standardization.
[L1044] [53:21.68] when they were strongarmming you, what
