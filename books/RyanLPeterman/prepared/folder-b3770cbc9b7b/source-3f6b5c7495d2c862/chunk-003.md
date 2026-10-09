Chunk 3; segments 810–1218. Start may repeat the previous chunk for context.

# Co-Creator of Haskell: Useless vs Useful Languages, Rust vs C, Functional Programming | Simon Jones

Source ID: source-3f6b5c7495d2c862
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Co-Creator_of_Haskell_Useless_vs_Useful_Languages,_Rust_vs_C,_Functional_Programming_Simon_Jones_en.txt
Video: https://www.youtube.com/watch?v=xcB_LF3cdqw

[L819] [27:27.36] It could do no IO. All it could do was
[L820] [27:29.20] take a string and produce a string.
[L821] [27:31.88] So, obviously that's not very useful.
[L822] [27:34.76] It's a little bit more useful. A
[L823] [27:35.92] language that is very very safe
[L824] [27:38.12] and completely useless is no-op
[L825] [27:40.68] that does nothing ever.
[L826] [27:42.36] Very safe
[L827] [27:43.80] but very useless. Haskell was a bit
[L828] [27:45.24] better, right? At least it lets you um
[L829] [27:48.40] apply a function to a string and get
[L830] [27:49.80] back another string.
[L831] [27:52.28] So, of course we then worked on how
[L832] [27:53.92] could we do IO in Haskell in a safe way.
[L833] [27:56.16] That will lead to, you know, monads and
[L834] [27:57.88] stuff. But But so, just as uh uh
[L835] [28:01.04] the you know, we're moving from C
[L836] [28:03.24] horizontally to go safer and safer
[L837] [28:06.24] um but
[L838] [28:07.52] uh but staying useful. So, from Haskell
[L839] [28:10.48] we're moving sort of vertically to get
[L840] [28:12.48] more and more useful without stopping
[L841] [28:14.12] being safe.
[L842] [28:16.08] And Nirvana is when we sort of meet up,
[L843] [28:18.36] right? So, but the point is not to say
[L844] [28:20.48] one is better than the other, but just
[L845] [28:22.00] to say that we both seek things that are
[L846] [28:23.76] useful and safe.
[L847] [28:26.00] >> And when I think of functional languages
[L848] [28:28.68] um in I guess in the mainstream or you
[L849] [28:30.88] know, what people are kind of thinking
[L850] [28:32.12] about, I hear Haskell. I also hear
[L851] [28:34.84] OCaml. Uh how do these two programming
[L852] [28:37.32] languages compare if someone was trying
[L853] [28:38.96] to pick a functional language to work
[L854] [28:40.72] with?
[L855] [28:41.64] >> So, OCaml is um a strict language that
[L856] [28:44.12] is called by value.
[L857] [28:46.00] So, when you say F applied to 3 + 4,
[L858] [28:48.52] it'll add 3 + 4 and then call F
[L859] [28:51.16] to get 7, right? In Haskell, if you say
[L860] [28:52.64] F of 3 + 4, it'll build a little
[L861] [28:54.60] suspension that says, "Well, if you ever
[L862] [28:55.96] need this 3 + 4,
[L863] [28:57.84] you can evaluate it, but maybe you'll
[L864] [28:59.20] never need it." And then it calls F.
[L865] [29:01.28] That's a lazy language. Right? Now, uh
[L866] [29:05.00] so because OCaml is strict, it has a
[L867] [29:08.12] defined order of evaluation.
[L868] [29:11.48] So if you say F of 3 + 4 and a second
[L869] [29:14.52] parameter 8 + 9, it'll evaluate 3 + 4
[L870] [29:17.12] and then 8 + 9 in that order.
[L871] [29:20.04] Right? So it makes sense to say you can
[L872] [29:22.16] say F of print hello, {comma} print
[L873] [29:25.00] goodbye.
[L874] [29:27.60] Right? Because you'll get hello and then
[L875] [29:29.56] goodbye printed.
[L876] [29:31.24] So once you have a defined order of
[L877] [29:32.80] evaluation, then it's pretty easy to
[L878] [29:34.92] incorporate IO.
[L879] [29:37.44] Right? Even though it's {quotes} a
[L880] [29:39.04] functional language,
[L881] [29:41.24] OCaml allows you to do IO without, you
[L882] [29:44.60] know, without saying unsafe before my IO
[L883] [29:46.32] or anything. In fact,
[L884] [29:48.20] it has a defined order of evaluation and
[L885] [29:49.88] it's perfectly kosher to do that.
[L886] [29:52.40] As a sort of unintended consequence of
[L887] [29:55.36] being called by value, it was also by
[L888] [29:57.88] default impure. Now, good Haskell good
[L889] [30:00.12] OCaml programmers won't use many side
[L890] [30:01.80] effects, but
[L891] [30:04.80] OCaml doesn't prevent you.
[L892] [30:07.44] Haskell prevents you. Why does it
[L893] [30:09.24] prevent you? Because if we'd allowed you
[L894] [30:11.80] to say F of print hello, {comma} print
[L895] [30:14.60] goodbye,
[L896] [30:16.68] those would be thunks, right? Not yet
[L897] [30:18.36] evaluated.
[L898] [30:20.56] Right? So if F happened to evaluate its
[L899] [30:22.60] first argument and then its second,
[L900] [30:25.68] we'd print hello and then goodbye. If it
[L901] [30:27.44] evaluated its second and then its first,
[L902] [30:29.00] we'd print goodbye and then hello. If it
[L903] [30:30.24] didn't evaluate either, we wouldn't
[L904] [30:31.32] print either of them.
[L905] [30:32.76] That doesn't sound very good from a uh
[L906] [30:34.52] you know, if you want to control what IO
[L907] [30:35.84] is happening. Right? Laziness forced
[L908] [30:39.08] Haskell to stay pure. Strictness allowed
[L909] [30:42.20] OCaml, which grew out of the ML
[L910] [30:44.20] tradition by the way, ML is another
[L911] [30:46.04] functional language that predated
[L912] [30:47.28] Haskell.
[L913] [30:48.28] It was always strict and it always had
[L914] [30:50.40] IO by default.
[L915] [30:52.48] Um
[L916] [30:53.60] it wasn't a goal, but that's just the
[L917] [30:55.20] way it worked out. At the time, nobody
[L918] [30:57.04] thought about it. It was just obvious.
[L919] [31:00.28] So, that's a big difference between
[L920] [31:01.36] OCaml and Haskell, right? Is that um
[L921] [31:04.68] Now then, since then they've both grown
[L922] [31:06.52] up. Haskell's gained sort of monads and
[L923] [31:09.04] I uh OCaml has gained lots of uh lots of
[L924] [31:11.80] fancy type systems. Some of them uh
[L925] [31:13.96] Haskell and OCaml have learned from each
[L926] [31:15.44] other. Um OCaml has gained an
[L927] [31:17.56] interesting effect system recently and a
[L928] [31:19.36] whole lot of new extensions. It's an
[L929] [31:20.96] absolute hotbed of innovation at the
[L930] [31:23.00] moment OCaml. So, I view OCaml and and
[L931] [31:26.08] Haskell as kind of um siblings.
[L932] [31:28.28] Um brothers and sisters, right? We love
[L933] [31:30.28] each other, we learn from each other, um
[L934] [31:32.44] we compete with each other, all of the
[L935] [31:34.04] things that siblings do.
[L936] [31:35.60] But, they're not the same, right? So,
[L937] [31:37.40] siblings don't say, "I'm I'm just better
[L938] [31:39.60] than you. You shouldn't exist." We say,
[L939] [31:41.68] "Let's Let's enjoy our life together."
[L940] [31:43.28] And that's what it That's the way it is.
[L941] [31:44.92] >> You described the laziness and the
[L942] [31:46.56] strict and as a programmer I my initial
[L943] [31:50.24] thought is I would like to control the
[L944] [31:52.76] order of execution. And when I say
[L945] [31:55.68] print X, I and then print Y, I I want it
[L946] [31:59.32] to happen that order, otherwise it would
[L947] [32:01.04] be a little unintuitive. What is the
[L948] [32:03.52] main benefit of laziness?
[L949] [32:05.80] >> Why is laziness good? Well, um
[L950] [32:08.80] uh John Hughes did did this rather well
[L951] [32:11.16] way ago, 1980 something. He wrote a
[L952] [32:14.08] program called Why Functional
[L953] [32:15.12] Programming Matters.
[L954] [32:16.64] Um
[L955] [32:17.40] and one of its main thesis was that lazy
[L956] [32:19.20] evaluation lets you um
[L957] [32:21.96] uh compose programs in a particularly
[L958] [32:24.44] modular way.
[L959] [32:25.80] So, imagine a program that is I mean,
[L960] [32:27.68] his classic example is a program that
[L961] [32:29.08] plays chess,
[L962] [32:30.52] right? So, one thing you could do is you
[L963] [32:32.60] could imagine building a tree of all
[L964] [32:35.32] possible moves starting from the
[L965] [32:36.92] position we're at.
[L966] [32:38.36] It would be a very, very big tree.
[L967] [32:40.68] You know, OCaml, it would be too big.
[L968] [32:43.12] Because first of all, I compute the
[L969] [32:44.52] tree,
[L970] [32:45.64] and then I'd start deciding what move to
[L971] [32:47.12] do. I couldn't possibly do that. But if
[L972] [32:49.20] the tree of all possible moves, you
[L973] [32:50.64] know, has more nodes in it than the
[L974] [32:51.84] number protons in the universe.
[L975] [32:54.36] So, let's not do that. Now,
[L976] [32:56.76] if instead you could build the tree Oh,
[L977] [32:58.96] having got this tree, supposing you had
[L978] [33:00.76] it, you could then walk over the tree
[L979] [33:02.32] saying, "Ah, let me do some mini-maxing
[L980] [33:04.64] and see Oh, this is looks like a good
[L981] [33:06.48] Let me go this way." I could explore the
[L982] [33:08.20] tree, right? Um
[L983] [33:10.36] Now then, so
[L984] [33:12.52] if you you know, OCaml, then you would
[L985] [33:14.32] have to put the tree generation and the
[L986] [33:16.08] tree exploration in one function.
[L987] [33:19.72] Right? In Haskell, with lazy evaluation,
[L988] [33:22.00] you can generate an infinite tree,
[L989] [33:24.44] and then the explorer that prunes the
[L990] [33:26.68] tree and explores just the bits of it
[L991] [33:28.72] that is necessary is completely
[L992] [33:30.92] modularly separated.
[L993] [33:32.72] Right? I can build a different generator
[L994] [33:34.60] and a different pruner. They're just
[L995] [33:36.36] completely separate programs.
[L996] [33:38.68] So, lazy evaluation is very powerful
[L997] [33:40.80] glue that lets you glue together um
[L998] [33:45.48] uh two programs that you'd like to be
[L999] [33:48.16] distinct. Strict evaluation forces you
[L1000] [33:50.80] to merge them together.
[L1001] [33:53.24] >> Yeah, this reminds me I mean um
[L1002] [33:55.48] so, in Python, for instance, they have
[L1003] [33:57.64] the idea of a generator where
[L1004] [33:59.56] >> Yes.
[L1005] [34:00.00] >> you can lazily retrieve things.
[L1006] [34:01.92] >> Every strict language, every, you know,
[L1007] [34:04.24] serious strict language has lazy
[L1008] [34:06.40] evaluation in it. They're called
[L1009] [34:07.72] iterators or generators.
[L1010] [34:10.16] And so does OCaml.
[L1011] [34:11.72] All right?
[L1012] [34:12.68] But in Haskell, that's the default.
[L1013] [34:15.84] Now, instead in Haskell, so this is a
[L1014] [34:17.40] bit like Again, the two are converging
[L1015] [34:19.20] on the middle, right? Haskell, lazy by
[L1016] [34:21.44] default, but you can make things strict.
[L1017] [34:23.64] You can put in exclamation marks to say,
[L1018] [34:25.48] "Please evaluate this before the call."
[L1019] [34:28.36] All right?
[L1020] [34:29.28] Or the IO monad know how say evaluate,
[L1021] [34:30.84] but that's a a more brutal strict strict
[L1022] [34:32.92] annotation. So, in Haskell you can make
[L1023] [34:34.64] things stricter.
[L1024] [34:36.64] In OCaml you can make things lazier.
[L1025] [34:40.60] All right? So, it really boils down to
[L1026] [34:43.32] is what's the default.
[L1027] [34:45.76] We both want to have a mixture of the
[L1028] [34:47.68] two.
[L1029] [34:49.24] And then it becomes a bit cultural as to
[L1030] [34:50.88] which you prefer. Um
[L1031] [34:52.92] I I don't know. Uh some people sometimes
[L1032] [34:54.92] ask me, they say, "Well, if you were
[L1033] [34:56.76] designing Haskell again, would you make
[L1034] [34:58.28] it strict by default
[L1035] [35:00.56] with really good support for laziness?"
[L1036] [35:02.96] And I often say, "Well, I might."
[L1037] [35:05.52] Uh yeah, that seemed attractive because
[L1038] [35:07.16] frequently I found myself cursing
[L1039] [35:09.20] laziness as an implementer.
[L1040] [35:11.32] But, I strongly suspect that 10 years
[L1041] [35:13.48] after that I'd be thinking,
[L1042] [35:15.16] "Man, if only it was lazy by default."
[L1043] [35:19.68] Oh, when I say strict by default I would
[L1044] [35:21.32] or definitely mean strict but pure.
[L1045] [35:24.68] Like, no side effects.
[L1046] [35:26.72] >> A few times in our conversation you've
[L1047] [35:28.68] mentioned the word monad. And it seems
[L1048] [35:31.60] like it allows us to do the side effects
[L1049] [35:33.84] and
[L1050] [35:34.72] um
[L1051] [35:35.80] what is a monad and yeah, how does it
[L1052] [35:38.52] help us do side effects and preserve
[L1053] [35:40.44] ordering?
[L1054] [35:41.48] >> One
[L1055] [35:42.60] way to think about it that's very um
[L1056] [35:45.52] easy to understand and use is just to
[L1057] [35:47.36] imagine that the do notation is somehow
[L1058] [35:50.00] built into Haskell. So, you can say do
[L1059] [35:52.76] print X semicolon print Y.
[L1060] [35:56.28] And that has type
[L1061] [35:59.08] IO unit.
[L1062] [36:00.56] So,
[L1063] [36:01.48] a value of type IO unit means I do some
[L1064] [36:04.56] do some input output and return a value
[L1065] [36:06.44] of type unit.
[L1066] [36:08.52] An expression of type IO int
[L1067] [36:11.00] is an expression that when you run it
[L1068] [36:13.28] will do some
[L1069] [36:14.56] IO and return an int.
[L1070] [36:17.32] Okay? So, do let's you combine um
[L1071] [36:21.20] IO performing computations together. So,
[L1072] [36:23.88] uh
[L1073] [36:24.56] print three
[L1074] [36:26.56] has type
[L1075] [36:28.08] IO unit.
[L1076] [36:30.56] It does some IO,
[L1077] [36:32.20] namely printing three, um
[L1078] [36:34.20] get char
[L1079] [36:36.60] has type IO char. It does some IO,
[L1080] [36:39.56] namely reading a character from standard
[L1081] [36:41.32] input, and returns a character.
[L1082] [36:44.44] All right?
[L1083] [36:46.20] Notice that's different from just char.
[L1084] [36:48.08] So, you know, {quotes} x {quote} that
[L1085] [36:50.80] has type char.
[L1086] [36:53.36] It's just a character pure, right?
[L1087] [36:56.84] Get char, the IO performing operation,
[L1088] [36:58.56] has type
[L1089] [36:59.64] IO char. It does some input output,
[L1090] [37:02.12] and returns a character. Okay.
[L1091] [37:05.16] The do notation lets you combine
[L1092] [37:07.20] together,
[L1093] [37:08.36] um
[L1094] [37:09.44] IO performing computations.
[L1095] [37:12.52] So, if you could say do,
[L1096] [37:14.44] and then you say x {left arrow} get
[L1097] [37:16.64] char,
[L1098] [37:18.04] semicolon,
[L1099] [37:21.32] put char x,
[L1100] [37:23.80] then that x {left arrow} get char, that
[L1101] [37:26.00] says run the get char computation,
[L1102] [37:28.84] and get me the character, call it x.
[L1103] [37:31.64] The put char x says
[L1104] [37:33.64] run the put char computation to put x,
[L1105] [37:35.24] and we combine them together with the do
[L1106] [37:36.60] notation, and it combines two
[L1107] [37:39.04] uh two computations to make one IO
[L1108] [37:41.56] performing computation.
[L1109] [37:43.64] Right?
[L1110] [37:45.52] So, but these things are completely
[L1111] [37:47.00] first class. That's what's new about
[L1112] [37:48.84] monads compared to just make it into
[L1113] [37:51.08] into C.
[L1114] [37:52.64] x {left arrow} get char semicolon put
[L1115] [37:54.40] char x.
[L1116] [37:56.12] That's a computation whose type is IO
[L1117] [37:57.96] unit.
[L1118] [37:59.84] Right? Let me give it a name, so I can
[L1119] [38:01.44] say let foo
[L1120] [38:03.24] with type IO unit equals that do.
[L1121] [38:06.16] Now, I can pass foo as an argument to
[L1122] [38:08.16] something. I could put foo in a data
[L1123] [38:09.88] structure. I could return foo as a
[L1124] [38:11.68] result.
[L1125] [38:13.00] It's a value just as much as three
[L1126] [38:16.60] or plus.
[L1127] [38:21.08] In particular, for example, I could say,
[L1128] [38:23.04] "Do foo semicolon foo."
[L1129] [38:27.60] That takes foo, uses it twice. Each time
[L1130] [38:31.44] do foo semicolon foo says, "Do foo." and
[L1131] [38:33.68] then do foo again.
[L1132] [38:35.92] Right? So, I'll read a character and put
[L1133] [38:37.24] it and then read a character and put it
[L1134] [38:38.28] again.
[L1135] [38:40.00] So, these values of type IO T for some
[L1136] [38:44.28] type T are first-class values.
[L1137] [38:48.48] Right?
[L1138] [38:49.64] In C, I can't take X colon equals three
[L1139] [38:52.64] semicolon, you know, Y plus four
[L1140] [38:55.96] and pass that as an argument to
[L1141] [38:58.08] something and expect it to happen
[L1142] [38:59.84] wherever it's used, right? It's not a
[L1143] [39:01.44] first-class value.
[L1144] [39:03.40] >> When I first was learning this this
[L1145] [39:05.24] monad idea, it seems like you've you've
[L1146] [39:07.96] said in a few places it's a way to do
[L1147] [39:10.44] the side effects, but keeps the language
[L1148] [39:12.28] pure. But, when I saw it, my first
[L1149] [39:15.84] thought was it's almost like this little
[L1150] [39:19.44] you know, place where we segregate the
[L1151] [39:22.04] dirty things we want to do, I guess.
[L1152] [39:23.80] But, then how does that keep the
[L1153] [39:25.20] language pure?
[L1154] [39:26.60] >> Oh.
[L1155] [39:27.52] Because because I mean yeah, we are
[L1156] [39:29.36] lying here, but look, if your function
[L1157] [39:31.16] has type int to int, can it do any IO
[L1158] [39:33.68] any IO?
[L1159] [39:34.96] >> No.
[L1160] [39:35.88] >> No.
[L1161] [39:37.08] If it has type int to IO int, it could
[L1162] [39:39.44] do arbitrary IO.
[L1163] [39:42.64] So, yes. So, it's nice pure int to int
[L1164] [39:45.88] function or dirty int to int function.
[L1165] [39:49.00] So, you might say, perhaps you're about
[L1166] [39:50.48] to say, that's a bit of a blunt
[L1167] [39:51.76] instrument.
[L1168] [39:53.88] Either completely pure or completely
[L1169] [39:55.68] dirty, right?
[L1170] [39:59.16] It gets you a awfully long way.
[L1171] [40:03.08] But, nevertheless, it would be cool if
[L1172] [40:05.40] you could um say, "Oh, I am a int to um
[L1173] [40:11.08] effectful
[L1174] [40:12.84] doing reading of files only int."
[L1175] [40:17.92] Right? So, you'd like to in the type
[L1176] [40:20.36] you'd like to say what kind of effects
[L1177] [40:22.48] can it have.
[L1178] [40:25.12] Can it throw exceptions?
[L1179] [40:27.36] Can it, you know, spawn new threads?
[L1180] [40:31.20] So, you'd like to enumerate the effects
[L1181] [40:34.20] this
[L1182] [40:35.48] computation could have, right? That
[L1183] [40:37.24] would be cool.
[L1184] [40:38.44] That's called an effect system.
[L1185] [40:40.40] And there's, you know, Brazilian
[L1186] [40:41.68] programming language papers about effect
[L1187] [40:43.32] systems. And it turns out that you can
[L1188] [40:45.76] indeed in the type system of Haskell
[L1189] [40:48.40] and indeed OCaml is is rapidly becoming
[L1190] [40:50.80] same. Uh you can express
[L1191] [40:53.20] just not just all or nothing, does it do
[L1192] [40:55.72] IO
[L1193] [40:56.80] game over
[L1194] [40:58.36] but rather
[L1195] [40:59.84] which particular effects does it do?
[L1196] [41:03.04] Including no effects at all, that's
[L1197] [41:05.12] pure.
[L1198] [41:05.92] Right?
[L1199] [41:07.92] A good place to start is a library
[L1200] [41:09.52] called Bluefin, which my um colleague
[L1201] [41:11.80] Tom Ellis has designed. It's a very nice
[L1202] [41:14.36] take on how to do effect systems in
[L1203] [41:16.00] Haskell.
[L1204] [41:17.60] >> I guess the purity comes from that this
[L1205] [41:21.44] is this this dirty stuff is signaled
[L1206] [41:24.36] through the type system. So
[L1207] [41:25.68] >> Correct.
[L1208] [41:26.96] >> Okay.
[L1209] [41:27.32] >> Correct. So, we can do it, but here it
[L1210] [41:28.80] is and be aware.
[L1211] [41:31.56] Yep. And because you have to thread, you
[L1212] [41:34.24] know, because the type system gets in
[L1213] [41:35.64] your face, you know, you you were trying
[L1214] [41:37.32] to
[L1215] [41:38.48] um
[L1216] [41:39.32] uh like map, say.
[L1217] [41:41.16] No.
[L1218] [41:42.20] Map says I apply a function to every
[L1219] [41:43.44] element of the list. Well, um
[L1220] [41:45.84] uh
[L1221] [41:46.56] so, it has type A to B to list of A to
[L1222] [41:48.32] list of B. If you were to apply an
[L1223] [41:50.24] IO-performing function, so it the
[L1224] [41:52.24] function you're applying has type like
[L1225] [41:53.80] int to IO of char
[L1226] [41:57.60] you could map that over a list, but you
[L1227] [41:58.92] just get a list of IO of chars.
