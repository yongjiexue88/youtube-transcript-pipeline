Chunk 3; segments 784–1225. Start may repeat the previous chunk for context.

# MIT Professor: Leetcode, P vs NP, SAT Solvers | Ryan Williams

Source ID: source-d01b8ceb8d9ebc26
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/MIT_Professor_Leetcode,_P_vs_NP,_SAT_Solvers_Ryan_Williams_en.txt
Video: https://www.youtube.com/watch?v=AaK1SL2i_4Y

[L793] [29:46.16] wrong, it's going to be false. Okay, so
[L794] [29:48.20] we have to avoid one of those
[L795] [29:50.20] assignments, okay?
[L796] [29:52.04] Well, that means that there are seven
[L797] [29:54.56] out of the eight possible assignments,
[L798] [29:56.68] so there's like three variables,
[L799] [29:58.52] two to the three, eight possible
[L800] [30:00.44] assignments, seven of them could be a
[L801] [30:03.20] satisfying assignment. They uh they
[L802] [30:04.96] could be part of a satisfying
[L803] [30:06.16] assignment, we don't know. But one of
[L804] [30:07.68] them is definitely not.
[L805] [30:09.48] So the one easy way to see that 2-SAT
[L806] [30:14.20] can be solved in less than 2 to the n
[L807] [30:15.88] time is just take any clause,
[L808] [30:19.00] try one of the seven possible
[L809] [30:21.36] assignments,
[L810] [30:23.28] and plug them in,
[L811] [30:25.40] and then recurse
[L812] [30:27.20] on the remaining formula.
[L813] [30:29.52] Now, let's think about what we did. If
[L814] [30:31.44] we were just trying all the possible 2
[L815] [30:33.92] to the n assignments,
[L816] [30:35.64] and we we would like plug in,
[L817] [30:38.40] you know,
[L818] [30:39.44] uh one of eight possible assignments
[L819] [30:42.32] for each of those three variables. And
[L820] [30:44.04] so we'd have eight recursive calls.
[L821] [30:47.28] Well, we instead, because we're clever
[L822] [30:49.20] and we looked at the clauses, we have
[L823] [30:51.00] seven recursive calls.
[L824] [30:53.12] And that that's the difference. So so we
[L825] [30:55.24] reduced
[L826] [30:56.68] by three variables at the cost of seven
[L827] [30:58.92] recursive calls as opposed to eight.
[L828] [31:02.32] And this gets you a slight improvement.
[L829] [31:04.80] This gets you about
[L830] [31:06.28] uh 1.9
[L831] [31:08.40] two to the end.
[L832] [31:09.76] Something slightly better than
[L833] [31:11.80] than
[L834] [31:13.04] uh two to the end.
[L835] [31:14.20] Okay, but you can do better than this.
[L836] [31:16.76] Um
[L837] [31:17.48] But this is this is sort of like the
[L838] [31:19.84] idea. You try to look at ways to plug in
[L839] [31:23.12] variables that will force constraints so
[L840] [31:26.76] you can rule out a large portion of the
[L841] [31:29.44] possible assignments.
[L842] [31:30.84] >> When I was thinking about circuits, it
[L843] [31:33.56] and you know, the different widths and
[L844] [31:35.16] depths, I I don't know if this is uh
[L845] [31:37.60] unusual question, but it it reminds me
[L846] [31:41.08] of neural nets, but the operators are
[L847] [31:43.44] different and the space of the
[L848] [31:47.36] uh the literals is different. So instead
[L849] [31:49.16] of booleans, it's maybe floating points.
[L850] [31:51.96] And so it just made me wonder about uh
[L851] [31:55.08] the algorithms that you might apply on a
[L852] [31:56.76] neural net. Is there, you know, analogs
[L853] [31:59.64] in between these two spaces?
[L854] [32:01.16] >> Yes. Yes. So
[L855] [32:03.08] um
[L856] [32:04.88] Yeah, if we look at
[L857] [32:07.04] say I want to model a neural network
[L858] [32:10.48] on So I want to compute say it's still a
[L859] [32:13.44] boolean function,
[L860] [32:15.04] but I want to do it with like a neural
[L861] [32:16.72] network. So like I want to
[L862] [32:19.28] use, let's say
[L863] [32:21.40] uh relus or
[L864] [32:23.56] um sign activation functions or or what
[L865] [32:26.92] what have you. Um
[L866] [32:29.20] There is
[L867] [32:30.36] a slightly more general like gate that
[L868] [32:33.32] we can use instead of ors and ands. That
[L869] [32:36.12] turns out to basically be equivalent.
[L870] [32:39.00] So, if instead of using ORs and ANDs, we
[L871] [32:42.52] use a so-called majority gate,
[L872] [32:45.04] which outputs one if and only if at
[L873] [32:47.84] least half of its inputs are one.
[L874] [32:51.92] Using this and negations, we can
[L875] [32:54.12] actually simulate
[L876] [32:56.24] uh neural nets, like the usual types of
[L877] [32:58.84] neural nets that you think of with the
[L878] [33:01.60] usual types of activation functions. So,
[L879] [33:04.04] if they have a constant number of layers
[L880] [33:06.88] of neurons, we can get a constant number
[L881] [33:09.16] of layers
[L882] [33:10.48] of majority gates and and negations.
[L883] [33:14.68] So, once you go So, this is so-called TC
[L884] [33:16.84] circuits for threshold circuits.
[L885] [33:19.52] Uh yeah, so once you allow threshold
[L886] [33:21.00] circuits, you can start to model uh
[L887] [33:23.12] neural networks.
[L888] [33:24.40] >> Still using booleans. It's just
[L889] [33:26.04] >> We're still looking at boolean inputs
[L890] [33:27.40] though, yes. So, once you allow your
[L891] [33:30.20] input space
[L892] [33:32.08] to
[L893] [33:33.44] to be larger and like have floating
[L894] [33:36.12] points, then
[L895] [33:37.84] um you can you can prove a lot
[L896] [33:40.96] uh
[L897] [33:41.60] more in terms of lower bounds. You can
[L898] [33:43.48] find like things that take like depth
[L899] [33:46.24] three
[L900] [33:47.36] in a neural net that's, you know, can't
[L901] [33:48.92] be done in depth two and so on.
[L902] [33:51.20] Um
[L903] [33:52.68] So, yeah, once you go
[L904] [33:54.92] past that and you start looking at just
[L905] [33:56.72] arbitrary real domain, it it becomes a
[L906] [34:00.40] a a totally different picture than from
[L907] [34:02.64] a discrete domain.
[L908] [34:04.84] >> OpenAI, Anthropic, Cursor, and Vercel
[L909] [34:08.60] all use this product to make their lives
[L910] [34:10.36] better.
[L911] [34:11.32] And the problem it solves is when you're
[L912] [34:13.20] building SaaS or an ad product and you
[L913] [34:15.88] want to sell to other companies, there's
[L914] [34:17.72] all these requirements you need to meet.
[L915] [34:19.84] There's SSO, there's SCIM, there's RBAC,
[L916] [34:23.48] there's audit logs. These are all things
[L917] [34:25.28] that take time to integrate, but aren't
[L918] [34:27.48] the main focus of your app. WorkOS is an
[L919] [34:29.80] API layer that lets you meet all of
[L920] [34:31.44] these requirements in just a few lines
[L921] [34:33.68] of code. So, let's say you have a new
[L922] [34:35.72] SaaS product and you want to sell to
[L923] [34:37.40] other companies, WorkOS will solve all
[L924] [34:39.88] of these critical feature gaps for you.
[L925] [34:42.60] You can check them out at workos.com to
[L926] [34:45.04] learn more and get started. And I
[L927] [34:47.20] appreciate them for supporting my work
[L928] [34:49.08] and sponsoring this podcast. One topic I
[L929] [34:51.64] thought might be fun to go over is you
[L930] [34:53.76] you wrote this paper about the
[L931] [34:55.76] likelihoods of these various conjectures
[L932] [34:58.72] in complexity theory and
[L933] [35:01.52] I I pulled a few of these that were kind
[L934] [35:04.24] of a minority opinions or maybe, you
[L935] [35:06.96] know, less less common takes. So, I'm
[L936] [35:09.36] curious to hear your rationale. So,
[L937] [35:11.74] >> [laughter]
[L938] [35:12.28] >> uh one of them the well-known one, you P
[L939] [35:15.28] P not equal to NP or, you know, P versus
[L940] [35:17.76] NP.
[L941] [35:18.84] Um
[L942] [35:20.20] you assigned an 80% confidence that
[L943] [35:22.60] they're not the same. And I think most
[L944] [35:25.64] people say much higher confidence. So,
[L945] [35:28.44] why do you why would you assign such a
[L946] [35:29.92] low confidence that they're not the
[L947] [35:31.32] same?
[L948] [35:32.68] >> It's interesting because I think I
[L949] [35:34.20] originally had something like
[L950] [35:36.56] 75%
[L951] [35:38.92] but then uh my college classmate Scott
[L952] [35:41.84] Aaronson was like, "How dare you?" kind
[L953] [35:44.08] of you know,
[L954] [35:44.92] he was
[L955] [35:45.15] >> [laughter]
[L956] [35:45.52] >> he was he he sort of called me out and
[L957] [35:47.44] I'm like, "Okay, fine. For you 80%
[L958] [35:49.48] fine."
[L959] [35:50.40] I guess that my point is that
[L960] [35:53.80] we really don't understand polynomial
[L961] [35:56.64] time computation
[L962] [35:58.76] as deeply
[L963] [36:00.12] as we think we do. And
[L964] [36:02.92] there are
[L965] [36:03.92] surprises like all the time
[L966] [36:07.16] in the power of algorithms.
[L967] [36:10.08] There are very few surprises in terms of
[L968] [36:12.92] lower bounds. Like, when we are able to
[L969] [36:15.24] prove a lower bound,
[L970] [36:17.36] typically it's something we
[L971] [36:20.20] very much expected to be true
[L972] [36:22.40] but it was hard to prove. It was hard to
[L973] [36:24.72] prove.
[L974] [36:26.16] Somehow we pulled it off, we got what we
[L975] [36:28.00] expected to be true.
[L976] [36:29.68] But all the time in algorithms
[L977] [36:31.88] people are finding algorithms where
[L978] [36:35.00] it's just like surprising. Just
[L979] [36:37.56] Wait. What? How How do you get something
[L980] [36:42.16] that fast? You're right. So
[L981] [36:44.80] uh this just happens over and over.
[L982] [36:47.48] When I was younger
[L983] [36:49.44] um when I was first thinking about P
[L984] [36:51.04] versus NP
[L985] [36:53.44] I
[L986] [36:55.72] like I had an intuition for what should
[L987] [36:57.92] be.
[L988] [36:59.24] And
[L989] [37:01.00] what I've understood over the years is
[L990] [37:02.56] that
[L991] [37:03.52] my intuition for what should be
[L992] [37:06.04] is often just wrong. And I'm I'm having
[L993] [37:09.36] to revise my intuitions uh all the time.
[L994] [37:13.28] So when something like this happens
[L995] [37:16.40] often enough
[L996] [37:18.28] you start asking yourself, "What do I
[L997] [37:20.84] really understand?
[L998] [37:23.84] Uh do I really understand P versus NP?"
[L999] [37:26.56] Like I mean, I understand the the the
[L1000] [37:29.24] statement, right? Like it's just one of
[L1001] [37:31.32] those problems where
[L1002] [37:33.76] somehow it is not so difficult to to
[L1003] [37:37.28] make formal, to write down
[L1004] [37:38.92] mathematically.
[L1005] [37:40.48] But to actually know what the answer is
[L1006] [37:43.72] is just orders of magnitude more
[L1007] [37:46.52] difficult than it is to phrase the
[L1008] [37:48.96] problem. And complexity theory in
[L1009] [37:50.84] particular is littered with
[L1010] [37:54.32] statements like this where
[L1011] [37:56.68] um
[L1012] [37:58.28] the the space of algorithms is just that
[L1013] [38:00.28] vast. Um
[L1014] [38:01.84] so if you just if you're just keep
[L1015] [38:03.72] getting surprised over time, you're just
[L1016] [38:05.16] like, "Well, what
[L1017] [38:06.68] what do I understand?" Maybe it was just
[L1018] [38:08.36] misplaced confidence.
[L1019] [38:10.36] >> Okay, what about this one? So
[L1020] [38:12.60] EXP not equal to NEXP or would you say
[L1021] [38:15.88] NEXP?
[L1022] [38:16.80] >> Oh, NEXP. Yeah. EXP versus NEXP. So this
[L1023] [38:19.36] is like the exponential time
[L1024] [38:22.12] of P versus NP.
[L1025] [38:24.40] >> For X not equal to NX or NEXP,
[L1026] [38:29.40] you gave it a 45% chance. And if this is
[L1027] [38:32.18] >> [laughter]
[L1028] [38:32.40] >> the P not equal to NP
[L1029] [38:34.96] equivalent, but for exponential time,
[L1030] [38:36.84] why is your
[L1031] [38:37.68] >> Yeah.
[L1032] [38:38.16] >> Why is it so low?
[L1033] [38:39.40] >> Oh, because exponential time algorithms
[L1034] [38:41.80] are even more powerful.
[L1035] [38:43.64] Did I really say 45%? I mean,
[L1036] [38:45.96] >> You did.
[L1037] [38:47.28] >> versus X or NX versus co-NX.
[L1038] [38:50.16] >> Yeah, NX not equal to X 45%.
[L1039] [38:53.14] >> [laughter]
[L1040] [38:53.16] >> I have it.
[L1041] [38:53.92] It's in this table.
[L1042] [38:55.20] >> So, so in other words, I believe NX
[L1043] [38:57.60] equals X more
[L1044] [38:59.68] than I believe they're different, right?
[L1045] [39:01.92] So,
[L1046] [39:03.64] um yeah, let me try to explain why. So,
[L1047] [39:06.60] you can think of the NX versus X
[L1048] [39:10.00] question
[L1049] [39:11.68] as
[L1050] [39:13.16] um some special case
[L1051] [39:15.32] of P versus NP,
[L1052] [39:17.24] where instead of looking at the
[L1053] [39:19.40] arbitrary SAT problem,
[L1054] [39:21.88] I'm looking at a SAT problem which is
[L1055] [39:24.84] extremely compressible.
[L1056] [39:27.56] So, there's like a really small little
[L1057] [39:30.12] computer
[L1058] [39:32.04] that is exponentially smaller than the
[L1059] [39:34.40] length of the instance, and it just
[L1060] [39:36.52] outputs the character
[L1061] [39:38.72] uh on the line number and the column
[L1062] [39:40.52] number for the for the DIMACS CNF, like
[L1063] [39:42.68] the the CNF file, okay? So, it's like a
[L1064] [39:45.56] extreme compression
[L1065] [39:47.96] of like some file.
[L1066] [39:49.76] So, it's like you zipped it down to like
[L1067] [39:51.56] something like exponentially smaller
[L1068] [39:53.96] than its original length, okay?
[L1069] [39:56.60] So, it's like some super compressed,
[L1070] [39:58.28] extremely highly regular
[L1071] [40:00.60] SAT instance. So, I give you that, and I
[L1072] [40:03.48] ask you,
[L1073] [40:05.44] uh when you unpack this thing,
[L1074] [40:07.76] decompress it,
[L1075] [40:09.60] is the result going to be satisfiable or
[L1076] [40:11.92] not?
[L1077] [40:13.12] And I want you to solve this
[L1078] [40:15.96] in time polynomial in the decompressed
[L1079] [40:18.80] representation.
[L1080] [40:20.84] Okay.
[L1081] [40:21.92] Okay. So, the point is that like this is
[L1082] [40:24.00] SAT, but
[L1083] [40:25.88] in the some very special case where the
[L1084] [40:27.72] thing is extremely structured.
[L1085] [40:30.20] So, the idea
[L1086] [40:31.88] um one conjecture for why SAT solvers
[L1087] [40:37.52] work
[L1088] [40:38.72] um
[L1089] [40:39.32] in practice.
[L1090] [40:40.80] Like one I mean this is
[L1091] [40:42.96] I mean conjecture maybe overkill because
[L1092] [40:46.24] I mean this is just this is not even a
[L1093] [40:48.32] well-formed mathematical statement. So,
[L1094] [40:50.92] one hypothesis for why SAT solvers work
[L1095] [40:53.72] in practice is because
[L1096] [40:55.80] um the real world is highly structured.
[L1097] [40:58.60] The real world is governed by physical
[L1098] [41:01.08] laws
[L1099] [41:02.24] that are not random. They're not
[L1100] [41:04.04] arbitrary. Like from a very small number
[L1101] [41:06.88] of rules, we can recreate so much of
[L1102] [41:09.32] science.
[L1103] [41:10.84] So,
[L1104] [41:12.08] what arises in practice from designs of
[L1105] [41:15.32] hardware and things like this are often
[L1106] [41:17.56] extremely compressible. They have to be
[L1107] [41:19.88] extremely compressible.
[L1108] [41:22.56] And
[L1109] [41:23.92] so maybe it's true that you know, every
[L1110] [41:27.68] uh SAT which has
[L1111] [41:29.60] uh a highly compact representation can
[L1112] [41:32.36] just be solved uh efficiently. This is
[L1113] [41:35.32] This is the idea of whether, you know,
[L1114] [41:37.68] NEXP equals EXP.
[L1115] [41:39.64] Um that it when it's really really
[L1116] [41:41.44] structured like that and super
[L1117] [41:42.88] compressible, there is some advantage.
[L1118] [41:45.24] It's not like a completely random and
[L1119] [41:47.88] since it's not like something arbitrary,
[L1120] [41:49.44] it's No, it's in fact very very special.
[L1121] [41:51.92] >> The other one is 80% likelihood on NEXP
[L1122] [41:56.24] equal to coNEXP,
[L1123] [41:58.60] and you wrote why would a
[L1124] [42:00.28] self-respecting complexity theory do
[L1125] [42:02.68] that?
[L1126] [42:03.74] >> [laughter]
[L1127] [42:04.68] >> Yeah, I was curious why that's such a
[L1128] [42:06.60] contentious statement.
[L1129] [42:08.36] >> So, NEXP versus coNEXP. Let's Let's
[L1130] [42:10.48] first talk about NP versus co-NP.
[L1131] [42:13.84] So, co-NP
[L1132] [42:15.64] um
[L1133] [42:17.12] is like the class of sort of complements
[L1134] [42:20.56] of NP-complete problems like
[L1135] [42:23.00] like UNSAT, like checking whether
[L1136] [42:24.72] something's UNSAT.
[L1137] [42:26.44] Now, from the time complexity point of
[L1138] [42:28.28] view
[L1139] [42:29.36] there's no difference between checking
[L1140] [42:31.20] SAT and UNSAT. You can always flip the
[L1141] [42:32.84] answer.
[L1142] [42:34.00] But from the complexity point of view,
[L1143] [42:35.88] if I if I ask you does co-NP equal NP?
[L1144] [42:40.20] What I'm asking you is, could you prove
[L1145] [42:42.72] to me
[L1146] [42:43.84] that a formula is unsatisfiable
[L1147] [42:46.96] with a short proof?
[L1148] [42:48.72] When it's satisfiable I can give you a
[L1149] [42:51.16] short proof. I can just give you the
[L1150] [42:52.60] satisfying assignment. You plug it in,
[L1151] [42:55.00] check that it works. But if it's
[L1152] [42:56.68] unsatisfiable, if there no assignment
[L1153] [42:59.08] works
[L1154] [43:00.36] we're saying for all assignments
[L1155] [43:02.80] the formula is not true. Can you flip
[L1156] [43:04.44] that to an existential statement and
[L1157] [43:06.64] say, "Oh, there exists this little proof
[L1158] [43:08.96] makes it work." So
[L1159] [43:10.44] people don't believe that NP is equal to
[L1160] [43:13.88] co-NP
[L1161] [43:15.40] and in fact like NP different from co-NP
[L1162] [43:19.24] implies P different from NP.
[L1163] [43:21.36] Um
[L1164] [43:22.16] But so this is the exponential time
[L1165] [43:24.08] version
[L1166] [43:25.56] of NP versus co-NP. So it's co-NEX
[L1167] [43:29.84] uh
[L1168] [43:30.40] versus NEX.
[L1169] [43:32.32] The reason why I think
[L1170] [43:35.24] these are likely to be equal
[L1171] [43:38.00] is that
[L1172] [43:39.72] if a little birdie
[L1173] [43:41.72] sat on an NEX machine's shoulder and
[L1174] [43:44.72] gave it a little bit of advice
[L1175] [43:47.20] about what the co-NEX thing is doing
[L1176] [43:50.84] then
[L1177] [43:51.88] the an NEX
[L1178] [43:53.80] uh algorithm
[L1179] [43:55.28] can actually solve co-NEX problems.
[L1180] [43:58.36] And so let let me explain
[L1181] [44:00.16] uh let me explain why Yeah, what's the
[L1182] [44:01.52] little birdie What the heck is the
[L1183] [44:02.76] little birdie saying? So
[L1184] [44:04.80] because NEX problems can run in 2 to the
[L1185] [44:07.92] end time and two to the N squared time
[L1186] [44:10.32] and things like that.
[L1187] [44:12.04] Running an exhaustive search over all
[L1188] [44:14.56] possible inputs of length N is no
[L1189] [44:16.72] problem
[L1190] [44:17.88] for NX.
[L1191] [44:19.08] So, what a little birdie can do is say,
[L1192] [44:21.76] "Okay, suppose um
[L1193] [44:24.52] like I want to verify that
[L1194] [44:27.88] this particular
[L1195] [44:30.04] um instance
[L1196] [44:32.36] like let's say let we can talk about
[L1197] [44:33.88] like an unsat but like the you know some
[L1198] [44:36.04] compressible unsat problem or something.
[L1199] [44:38.40] Suppose I want to prove that this
[L1200] [44:39.56] compressible unsat instance
[L1201] [44:42.44] um
[L1202] [44:43.04] is a yes. Okay? How am I going to do
[L1203] [44:45.32] that uh
[L1204] [44:47.16] with NX?
[L1205] [44:48.56] The little birdie will tell me
[L1206] [44:51.12] the total number of inputs of length N
[L1207] [44:54.04] which are a yes.
[L1208] [44:56.60] Okay?
[L1209] [44:57.56] So, it it will it will just tell me some
[L1210] [44:59.64] string which says, "Here's the total
[L1211] [45:01.52] number of inputs of length N. You gave
[L1212] [45:03.60] me a length N input. Here's the total
[L1213] [45:05.24] number of inputs of length N
[L1214] [45:07.96] uh
[L1215] [45:08.56] that are a yes. Okay?
[L1216] [45:11.40] Okay? So,
[L1217] [45:13.84] um this this advice this little you know
[L1218] [45:18.08] birdie's advice doesn't take very much
[L1219] [45:20.36] like to encode a count. It's like order
[L1220] [45:22.80] N bits to encode a count uh of things.
[L1221] [45:26.60] So,
[L1222] [45:27.96] um so, what does the NX thing do to
[L1223] [45:31.12] prove a co-NX thing? What it does is it
[L1224] [45:33.88] guesses
[L1225] [45:35.56] the things which are a no.
[L1226] [45:38.04] So, I'm trying to prove unsat. So, unsat
[L1227] [45:40.16] means yes, sat means no.
[L1228] [45:42.64] So, the NX thing guesses those things
[L1229] [45:44.96] which are no.
[L1230] [45:46.16] The no things it can answer, right? If
[L1231] [45:48.28] it's a sat thing, it can just guess the
[L1232] [45:50.40] answer to each of the nos.
[L1233] [45:53.36] Okay?
[L1234] [45:54.44] So, it guesses the answer to each of the
