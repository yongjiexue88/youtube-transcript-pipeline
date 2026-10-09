Chunk 3; segments 827–1254. Start may repeat the previous chunk for context.

# Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy

Source ID: source-fba2cff234dd0aeb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_OCaml_Functional_Programming,_Formal_Verification,_Programming_Languages_Xavier_Leroy_en.txt
Video: https://www.youtube.com/watch?v=9Cswiqrq6So

[L836] [30:23.20] Um so yeah, so it's really uh
[L837] [30:24.84] programming taken to a higher level. Um
[L838] [30:28.84] And and today it's quite expensive. Um
[L839] [30:31.76] it takes a lot more time to to prove a
[L840] [30:34.16] program than to write it in the first
[L841] [30:36.16] place. But maybe this is getting a
[L842] [30:38.08] little better.
[L843] [30:39.48] Um
[L844] [30:41.68] Yeah, and I should also mention another
[L845] [30:43.44] great uh of certified software is the
[L846] [30:46.80] it's a microkernel, the SEL4
[L847] [30:49.12] microkernel,
[L848] [30:50.52] uh developed in Australia, and which is
[L849] [30:53.24] used as an hypervisor in in some in some
[L850] [30:56.84] applications.
[L851] [30:58.36] And so it is uh
[L852] [31:00.88] is
[L853] [31:02.00] really like 8,000 lines of extremely
[L854] [31:04.44] technical C code that that, you know,
[L855] [31:06.48] manipulates uh
[L856] [31:08.36] uh processes and uh
[L857] [31:11.52] capabilities and security tokens and so
[L858] [31:14.12] on. And it's been proved correct. Every
[L859] [31:16.68] line has been proved correct. And that
[L860] [31:18.76] that's a very big achievement.
[L861] [31:21.00] >> When you mentioned the example of
[L862] [31:22.56] verifying a mathematical proof, that
[L863] [31:26.20] uh makes sense to me. When you talk
[L864] [31:28.00] about proving something about a program,
[L865] [31:31.20] it's a little bit more abstract to me or
[L866] [31:33.00] I'm having some trouble visualizing.
[L867] [31:35.60] Could you give a concrete example like
[L868] [31:38.48] uh maybe some trivial program that we're
[L869] [31:41.68] trying to prove something about it and
[L870] [31:43.20] how that uh theorem prover would work.
[L871] [31:46.64] >> Let's say
[L872] [31:48.40] you have a function that takes three
[L873] [31:49.88] numbers, X, Y, Z, and um returns the
[L874] [31:52.84] average of those numbers.
[L875] [31:55.28] Okay?
[L876] [31:56.56] Um
[L877] [31:58.72] only
[L878] [31:59.96] yeah, and and maybe
[L879] [32:02.96] you're using a not completely obvious
[L880] [32:05.12] formula like uh
[L881] [32:07.36] T equals X plus Y and then T equals T
[L882] [32:10.88] plus Z and then um T equals T divided by
[L883] [32:14.64] 3 and then return T. Okay? So not that
[L884] [32:17.52] exactly is the formula for the
[L885] [32:20.00] average.
[L886] [32:22.72] Uh and you want to prove that that
[L887] [32:24.08] function is correct. So so you want to
[L888] [32:26.72] prove that
[L889] [32:28.36] it it returns uh
[L890] [32:30.52] X plus Y plus Z divided by 3. And maybe
[L891] [32:33.60] you will have to make it clear whether
[L892] [32:35.32] you're rounding up or rounding down.
[L893] [32:38.36] If you're using integers or
[L894] [32:39.76] floating-point numbers, you know, it's
[L895] [32:41.20] not a exact arithmetic, so
[L896] [32:43.71] >> [snorts]
[L897] [32:43.84] >> um
[L898] [32:45.12] So, yeah, you you'll have to to say
[L899] [32:46.92] exactly what you mean by divided by
[L900] [32:48.60] three.
[L901] [32:49.61] >> [snorts]
[L902] [32:50.00] >> And then, uh if you are in a language
[L903] [32:51.72] like C, you can have arithmetic
[L904] [32:53.20] overflows.
[L905] [32:54.68] Okay? When you compute X + Y or
[L906] [32:57.84] + Z,
[L907] [32:59.36] um
[L908] [33:00.20] you can overflow the range of
[L909] [33:01.96] representable representable integers,
[L910] [33:03.92] and in C, it's it's a bug. It's an
[L911] [33:05.72] undefined behavior.
[L912] [33:07.72] So, typically, you will want to put a
[L913] [33:10.16] so-called precondition on your function
[L914] [33:11.92] saying, "Okay,
[L915] [33:13.16] uh if you call me, call me with numbers
[L916] [33:15.84] that are between, I don't know, zero and
[L917] [33:18.00] 1 million for instance, but no bigger
[L918] [33:20.08] than that." And and then, the prover
[L919] [33:23.60] will check that no overflow can occur in
[L920] [33:26.12] this case.
[L921] [33:27.44] Um okay? And so So, basically, you have
[L922] [33:31.20] the precondition that says, "Okay, these
[L923] [33:33.40] are safety guarantees um
[L924] [33:35.88] that must hold of the parameters,
[L925] [33:37.68] otherwise, anything can happen."
[L926] [33:40.52] And then, there will be a little bit of
[L927] [33:42.16] kind of symbolic execution of the
[L928] [33:43.68] function body
[L929] [33:45.08] that says, "Okay, when you T equals X +
[L930] [33:47.28] Y, then T plus equals Z, then T {slash}
[L931] [33:50.04] equals three, then in the end, T is X +
[L932] [33:52.68] Y + Z divided by three, provided no
[L933] [33:55.28] overflow occurred."
[L934] [33:58.16] And then, you put that with a
[L935] [33:59.56] precondition that says,
[L936] [34:01.36] "There cannot be any
[L937] [34:02.72] overflow," and you get your final
[L938] [34:04.64] result.
[L939] [34:05.68] Okay? So, basically, you're stating a
[L940] [34:07.12] contract for your function, the pre-
[L941] [34:09.96] hypotheses on the arguments,
[L942] [34:11.84] uh guarantees on the results.
[L943] [34:14.00] And
[L944] [34:15.36] uh and and you want to prove or analyze
[L945] [34:18.76] the function body to show that this
[L946] [34:21.16] contract is respected.
[L947] [34:23.24] I hope it's a little more concrete.
[L948] [34:25.72] >> So, it it sounds like a lean will help
[L949] [34:28.44] you basically take in some invariants
[L950] [34:31.28] about a program and kind of propagate
[L951] [34:33.00] them through line by line and uphold
[L952] [34:36.04] them. And so you can say something about
[L953] [34:38.44] >> Yes.
[L954] [34:41.04] Maybe not Lean by itself. Well, a
[L955] [34:43.40] program prover a program prover will do
[L956] [34:45.60] exactly what you say.
[L957] [34:47.32] And for Lean to be able to do it, you
[L958] [34:49.84] still need to teach it a little bit
[L959] [34:51.32] about the semantics of your programming
[L960] [34:52.84] language.
[L961] [34:54.04] Okay, that
[L962] [34:55.68] what does a plus means, what does
[L963] [34:59.40] assignment means, okay? Lean Lean is
[L964] [35:02.00] mathematics. You don't assign in
[L965] [35:03.96] mathematics. You don't say x equals x
[L966] [35:05.80] plus one or or or
[L967] [35:08.20] or you're just comparing x and x plus y
[L968] [35:10.16] and it's always false. There's no
[L969] [35:11.80] assignment in mathematics. There's
[L970] [35:13.64] assignment in many programs. So you need
[L971] [35:16.04] to
[L972] [35:17.16] make it explicit that
[L973] [35:19.44] there are [snorts] actually three
[L974] [35:20.52] different states for the t variable,
[L975] [35:22.80] three different values and and
[L976] [35:26.60] and relate [clears throat] those values
[L977] [35:27.84] to
[L978] [35:29.40] Well, the program defines what those
[L979] [35:30.80] values are and then a prover like Lean
[L980] [35:33.20] can can reason about those three
[L981] [35:35.24] successive values.
[L982] [35:37.40] Because now you're in you're in
[L983] [35:38.80] mathematics.
[L984] [35:40.00] And and that that kind of bridge between
[L985] [35:43.44] programs and their mathematical meaning
[L986] [35:46.28] is called semantics. That that the field
[L987] [35:48.80] of semantics of programming languages
[L988] [35:51.24] has been a big topic in in PL research
[L989] [35:53.64] since the the '60s at least.
[L990] [35:56.52] >> Am I understanding then that
[L991] [35:58.60] like a pure functional programming
[L992] [36:00.08] language, the gap between mathematics
[L993] [36:03.28] and
[L994] [36:04.48] the actual symbols is much smaller than
[L995] [36:07.08] an imperative?
[L996] [36:08.04] >> Absolutely. Yeah, you're you're
[L997] [36:10.00] absolutely right.
[L998] [36:12.72] And that's one of the reasons why
[L999] [36:15.64] people who do formal methods don't like
[L1000] [36:17.56] assignment, don't like imperative
[L1001] [36:18.96] features.
[L1002] [36:20.32] Purely functional style is much closer
[L1003] [36:22.88] to mathematical style, so much easier to
[L1004] [36:24.72] reason going
[L1005] [36:26.28] There can still be few discrepancies
[L1006] [36:28.80] between the program and the math. Uh,
[L1007] [36:31.00] for instance, functional programs may
[L1008] [36:32.24] not terminate.
[L1009] [36:33.80] They may loop forever. Um, mathematics
[L1010] [36:36.84] doesn't like that. So, so you need a way
[L1011] [36:38.60] to to reason about termination.
[L1012] [36:41.24] Um, and uh
[L1013] [36:44.32] and also yeah, sometimes for instance,
[L1014] [36:47.16] the the arithmetic you get in the
[L1015] [36:48.56] programming language is not
[L1016] [36:50.80] uh, integer arithmetic or is not
[L1017] [36:53.24] uh, real reals. [clears throat] You
[L1018] [36:55.04] know, it's floating point, it's not
[L1019] [36:56.36] reals. So, so you still have to
[L1020] [36:59.16] uh, account for that
[L1021] [37:01.36] gap. Uh, but you're you're absolutely
[L1022] [37:03.84] right that the gap is much shorter for
[L1023] [37:06.12] functional programming. And and uh
[L1024] [37:10.52] in the experience of CompCert, my my
[L1025] [37:12.20] verified compiler,
[L1026] [37:13.84] I think the the first decision was to
[L1027] [37:15.40] write it in a purely functional style
[L1028] [37:18.40] so that it would be easier to to reason
[L1029] [37:20.40] about it later.
[L1030] [37:22.12] >> You mentioned the the specifications
[L1031] [37:24.32] that we could prove, and one of them was
[L1032] [37:27.24] proving that the program terminates, but
[L1033] [37:29.76] I thought that's a famously
[L1034] [37:32.16] difficult or impossible. I forgot
[L1035] [37:33.72] exactly that the halting problem, right?
[L1036] [37:35.40] So, how how is that something that you
[L1037] [37:37.60] could prove?
[L1038] [37:39.08] >> Okay, so what the
[L1039] [37:41.08] um computability theory says is that
[L1040] [37:43.12] there is no algorithm that will always
[L1041] [37:46.28] that can always say
[L1042] [37:48.24] this program terminates or this program
[L1043] [37:50.00] doesn't terminate.
[L1044] [37:51.40] Um,
[L1045] [37:52.20] so so there will always be some very
[L1046] [37:53.84] weird programs for which your your
[L1047] [37:57.64] analyzer your your automatic termination
[L1048] [37:59.84] analyzer will produce a wrong result
[L1049] [38:02.60] or will not terminate itself.
[L1050] [38:06.68] Uh, so it will not work.
[L1051] [38:08.44] Um, uh but
[L1052] [38:11.12] still for for many programs, you can
[L1053] [38:13.44] succeed. Okay, you can write automatic
[L1054] [38:16.00] termination analyzers that will work for
[L1055] [38:18.16] a large uh class of programs.
[L1056] [38:21.76] And then the termination analysis,
[L1057] [38:23.84] termination proof can also be done by
[L1058] [38:25.36] hand by by a mathematician. Okay, so
[L1059] [38:30.32] So, perhaps
[L1060] [38:32.92] a human can can see through those weird
[L1061] [38:36.64] Turing programs that that are hard to
[L1062] [38:38.96] prove to terminate and
[L1063] [38:40.96] and and recognize the trick.
[L1064] [38:43.00] But, anyway, so yeah, it's a hard
[L1065] [38:44.56] problem and all all program verification
[L1066] [38:47.36] tasks are are difficult pro
[L1067] [38:49.96] problems, okay? Uh
[L1068] [38:52.48] They are pretty much all undecidable.
[L1069] [38:55.44] So, you know that there there is no
[L1070] [38:57.08] static analyzer that will always
[L1071] [38:59.92] find all problem all problems in all
[L1072] [39:02.08] programs.
[L1073] [39:03.62] >> [snorts]
[L1074] [39:03.92] >> But, still you can try, okay? You can
[L1075] [39:06.20] try for specific problems, for specific
[L1076] [39:08.60] programs and and get some very useful
[L1077] [39:11.28] results out of them out of that.
[L1078] [39:13.80] You only need to be able to do it for
[L1079] [39:15.20] the cases that are of interest to you,
[L1080] [39:17.44] the programs you really care about.
[L1081] [39:20.00] >> OpenAI, Anthropic, Cursor, and Vercel
[L1082] [39:23.76] all use this product to make their lives
[L1083] [39:25.48] better.
[L1084] [39:26.44] And the problem it solves is when you're
[L1085] [39:28.32] building SaaS or an AI product and you
[L1086] [39:30.96] want to sell to other companies, there's
[L1087] [39:32.88] all these requirements you need to meet.
[L1088] [39:34.96] There's SSO, there's SCIM, there's RBAC,
[L1089] [39:38.60] there's audit logs. These are all things
[L1090] [39:40.40] that take time to integrate, but aren't
[L1091] [39:42.60] the main focus of your app. WorkOS is an
[L1092] [39:44.92] API layer that lets you meet all of
[L1093] [39:46.60] these requirements in just a few lines
[L1094] [39:48.76] of code. So, let's say you have a new
[L1095] [39:50.80] SaaS product and you want to sell to
[L1096] [39:52.48] other companies, WorkOS will solve all
[L1097] [39:54.96] of these critical feature gaps for you.
[L1098] [39:57.72] You can check them out at workos.com to
[L1099] [40:00.12] learn more and get started. And I
[L1100] [40:02.28] appreciate them for supporting my work
[L1101] [40:04.20] and sponsoring this podcast. One thing
[L1102] [40:06.50] [snorts] I saw when I was researching
[L1103] [40:07.68] OCaml is that
[L1104] [40:09.96] uh in 2022, OCaml added multicore
[L1105] [40:13.40] support. And but from my memory, I
[L1106] [40:16.40] remember multi-core processors became
[L1107] [40:19.16] standard much earlier than that. And so,
[L1108] [40:21.60] I figured there might be some unique
[L1109] [40:23.56] engineering challenge in adding that
[L1110] [40:25.16] support. So, yeah, what what happened
[L1111] [40:27.48] there and what made it difficult?
[L1112] [40:29.96] >> Uh well, there were
[L1113] [40:31.80] engineering challenges, that's for sure.
[L1114] [40:33.72] There there were also some language
[L1115] [40:34.96] design issues.
[L1116] [40:36.80] So, so but let's talk about the
[L1117] [40:38.56] engineering challenges first.
[L1118] [40:40.52] Um so, it's true that that when you have
[L1119] [40:42.80] a a language with with a runtime system
[L1120] [40:45.72] memory allocator or garbage collector
[L1121] [40:48.28] uh
[L1122] [40:49.64] well, at least the one of for for OCaml
[L1123] [40:51.92] was really designed with sequential
[L1124] [40:53.72] executions in mind.
[L1125] [40:55.48] So, if you have if you add a shared
[L1126] [40:57.44] memory concurrency, then you need a
[L1127] [41:00.04] garbage collector or a memory allocator
[L1128] [41:01.76] that that that that can work
[L1129] [41:03.24] concurrently. And that's actually quite
[L1130] [41:05.44] difficult.
[L1131] [41:06.72] Uh at least if you want them to be fast.
[L1132] [41:09.88] Of course, you
[L1133] [41:11.16] you could always, you know, take take
[L1134] [41:12.64] take a lock at at every operation in the
[L1135] [41:15.52] heap, but then uh you would
[L1136] [41:17.64] sequentialize your programs. Basically,
[L1137] [41:19.48] they they they would run as slowly as a
[L1138] [41:21.52] single processor. So, so that's not
[L1139] [41:24.04] interesting. So, yeah, so there were
[L1140] [41:25.96] engineering challenges. Um um yeah, I
[L1141] [41:28.80] was at least initially quite quite
[L1142] [41:30.88] reluctant to
[L1143] [41:32.84] uh basically re-implement a complete uh
[L1144] [41:36.20] garbage collector and and uh memory
[L1145] [41:38.76] allocator or large parts of the runtime
[L1146] [41:40.28] system. That's what we did eventually
[L1147] [41:42.52] with uh as well, it was done mostly by
[L1148] [41:45.12] the team at OCaml Labs at Cambridge
[L1149] [41:47.52] University.
[L1150] [41:48.68] >> [snorts]
[L1151] [41:48.76] >> Uh but yes, it was a really big rewrite.
[L1152] [41:53.72] Um but then I said there's also a
[L1153] [41:56.28] language design issue.
[L1154] [41:58.88] Which is that for for the longest time
[L1155] [42:01.24] well
[L1156] [42:02.20] uh
[L1157] [42:03.24] is
[L1158] [42:04.08] now when when you say uh
[L1159] [42:06.56] multi-core
[L1160] [42:09.00] processors and so on, pretty much
[L1161] [42:10.68] everyone
[L1162] [42:11.88] and language support for multi-core
[L1163] [42:13.92] processors, everyone thinks about
[L1164] [42:16.20] language support for shared memory
[L1165] [42:18.00] concurrency.
[L1166] [42:19.36] You know, this model where you have
[L1167] [42:20.56] several sites of control and they access
[L1168] [42:23.08] the same memory
[L1169] [42:24.80] and basically the sites communicate by
[L1170] [42:26.92] modifying the memory and someone else is
[L1171] [42:29.40] going to notice.
[L1172] [42:31.00] You know, it and
[L1173] [42:32.80] I've never liked this model of of
[L1174] [42:35.92] communication.
[L1175] [42:38.16] I mean, it's a bit like if you want to
[L1176] [42:40.44] communicate with your neighbor then then
[L1177] [42:42.20] you you you break into their houses and
[L1178] [42:44.96] their house and then you move the
[L1179] [42:46.96] furniture around and then when they are
[L1180] [42:48.88] back they say, "Oh, something something
[L1181] [42:51.12] was moved so it's probably Iron who's
[L1182] [42:53.04] trying to tell us something."
[L1183] [42:55.08] Maybe you could just meet your
[L1184] [42:56.32] neighbors, you know? And and that would
[L1185] [42:58.24] be things like message passing
[L1186] [43:01.24] which is a completely different form of
[L1187] [43:02.80] communication, much higher level.
[L1188] [43:05.12] So, yeah, so for the longest time I was
[L1189] [43:07.48] really interested in message passing
[L1190] [43:10.60] concurrency.
[L1191] [43:12.84] And there's for instance a functional
[L1192] [43:15.36] language called Erlang that was built on
[L1193] [43:18.32] around those ideas and that I found
[L1194] [43:20.72] quite interesting.
[L1195] [43:22.28] However, I never got to to have a
[L1196] [43:24.92] decent language design and
[L1197] [43:28.40] everyone was saying, "No, but but it
[L1198] [43:30.36] it's it's too costly. It's not
[L1199] [43:32.60] effective. There's too much copying of
[L1200] [43:34.32] data.
[L1201] [43:35.60] With shared memory you can you can share
[L1202] [43:37.36] some kind of huge database in memory. If
[L1203] [43:40.28] you don't modify it too much, then
[L1204] [43:42.24] basically the sharing is the the
[L1205] [43:44.56] concurrency is free.
[L1206] [43:46.60] While with message passing we'll have to
[L1207] [43:48.08] exchange a lot of data so
[L1208] [43:50.60] to to get the same effect so so you will
[L1209] [43:52.32] pay more for it.
[L1210] [43:53.72] Anyway,
[L1211] [43:54.76] so
[L1212] [43:55.92] so okay, so
[L1213] [43:57.76] starting with Java I guess and then C
[L1214] [44:00.60] C++ 2011 there was this idea that okay,
[L1215] [44:04.16] we we we need to expose shared memory
[L1216] [44:06.28] concurrency to the programmers.
[L1217] [44:09.08] But then comes the problem of the memory
[L1218] [44:10.80] model, which is that
[L1219] [44:12.92] what happens when there's a race, for
[L1220] [44:15.28] instance, when when two
[L1221] [44:17.20] uh two threads want to access the same
[L1222] [44:20.04] uh location, and maybe they want to
[L1223] [44:21.60] modify it in different ways.
[L1224] [44:23.76] And so, sometimes parts of the C C++
[L1225] [44:27.32] standard says, "It's undefined behavior.
[L1226] [44:29.76] Anything can happen." But still, you
[L1227] [44:31.56] need to give a little more guarantees.
[L1228] [44:33.80] Uh at the other end of the spectrum,
[L1229] [44:35.48] there's a so-called uh sequential
[L1230] [44:36.84] consistency, which says, "Well, what
[L1231] [44:38.80] happens is like an interleaving of reads
[L1232] [44:41.80] and writes of your program."
[L1233] [44:43.64] You don't know which interleaving, but
[L1234] [44:44.92] there is an interleaving.
[L1235] [44:47.36] But that doesn't work with modern
[L1236] [44:50.00] uh processors, multi-core processors.
[L1237] [44:52.00] They reorder memory accesses in in very
[L1238] [44:54.96] clever ways to get more performance. And
[L1239] [44:57.40] so, viewed from the program, it's very
[L1240] [44:59.08] hard to predict what they are actually
[L1241] [45:00.36] doing.
[L1242] [45:01.60] And so, you need to give your
[L1243] [45:03.40] programmers, when you're designing a
[L1244] [45:04.84] language with shared memory concurrency,
[L1245] [45:06.40] you need to give your programmers some
[L1246] [45:07.96] guarantees about uh the ordering of
[L1247] [45:11.24] reads and writes, concurrent reads and
[L1248] [45:12.88] writes, while not constraining the
[L1249] [45:14.88] hardware too much.
[L1250] [45:17.04] And it's very difficult. So, Java went
[L1251] [45:20.20] through like five different iterations
[L1252] [45:22.28] of the memory model. Some were too
[L1253] [45:23.96] strict, some were too lax, some were
[L1254] [45:25.76] kind of in
[L1255] [45:27.16] inconsistent. They were were were making
[L1256] [45:29.48] predictions, impossible predictions,
[L1257] [45:31.48] where where the past depends on the
[L1258] [45:32.96] future.
[L1259] [45:34.66] >> [snorts]
[L1260] [45:34.84] >> Crazy, really crazy stuff.
[L1261] [45:37.04] Uh then C C++ 11 did a little better,
[L1262] [45:40.16] but still extremely complex memory
[L1263] [45:42.36] model. And so, when we wanted to add
