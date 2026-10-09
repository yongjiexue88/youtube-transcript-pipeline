Chunk 3; segments 805–1194. Start may repeat the previous chunk for context.

# Turing Award Winner: Early AI, LLM Predictions, Causality | Judea Pearl

Source ID: source-0960ba5d23f1b542
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Early_AI,_LLM_Predictions,_Causality_Judea_Pearl_en.txt
Video: https://www.youtube.com/watch?v=FleTXB1fAcQ

[L814] [40:24.96] what is relevant to what and deal with
[L815] [40:27.60] the relevant only.
[L816] [40:30.08] Great. And then came the work on Beijian
[L817] [40:32.88] network. Okay.
[L818] [40:35.60] You define a network error or no error.
[L819] [40:40.48] The combination of errors gives you
[L820] [40:44.08] information about what is independent on
[L821] [40:47.60] what given what. So for every triplet X
[L822] [40:51.36] is independent on Y given Z where Z can
[L823] [40:54.48] be a set and so on and X and Y can be
[L824] [40:58.96] computed from the graph not from the
[L825] [41:02.40] probability but from the graph
[L826] [41:06.64] which actually if you look at it from a
[L827] [41:09.44] philosophical viewpoint it's a
[L828] [41:12.80] revolution.
[L829] [41:14.40] What does probabilities have to do with
[L830] [41:16.64] graphs?
[L831] [41:18.24] When you took probability theory 101 is
[L832] [41:22.16] anybody talking to graph about you? No.
[L833] [41:25.04] Right. So both the probabilists and the
[L834] [41:28.56] philosophers
[L835] [41:30.16] got irritated or should be irritated.
[L836] [41:33.60] What is the connection between
[L837] [41:35.52] probabilities? And now it turns out
[L838] [41:37.52] there is a very strong logical
[L839] [41:40.64] connection between the two
[L840] [41:43.28] because [clears throat]
[L841] [41:44.08] the axioms of conditional probability
[L842] [41:48.24] or conditional independence in
[L843] [41:50.40] probability theory are the same axiom as
[L844] [41:54.00] you have in graph separation.
[L845] [41:56.88] In graph you have idea of separation.
[L846] [42:00.08] There's no connection between node X and
[L847] [42:02.96] node Y
[L848] [42:05.28] unless you go through a set of node Z.
[L849] [42:08.48] So Z separate X from Y. Okay,
[L850] [42:12.48] it's the same logic that you have when X
[L851] [42:16.24] is independent on Y given Z in
[L852] [42:18.96] probability theory.
[L853] [42:21.12] Independent
[L854] [42:22.64] separation is a connection between them.
[L855] [42:25.76] They share a
[L856] [42:27.98] [laughter]
[L857] [42:28.96] you happy. I'm happy because I relive
[L858] [42:32.32] now the excitement we have in the 1970s
[L859] [42:37.36] when we discovered all this connection
[L860] [42:39.68] between two seemingly unrelated
[L861] [42:44.40] uh perspective on science, probability
[L862] [42:47.92] theory and graph theory.
[L863] [42:52.00] That by the way I did in um
[L864] [42:55.36] joint work with Aaria Paz who came to
[L865] [42:58.88] visit me from the technon in Israel.
[L866] [43:01.68] Yeah. And that is called by the way
[L867] [43:03.60] should I should mention it the theory of
[L868] [43:05.60] graphoid
[L869] [43:07.12] graphoid
[L870] [43:09.04] openai [snorts]
[L871] [43:10.08] anthropic cursor and Verscell all use
[L872] [43:13.36] this product to make their lives better.
[L873] [43:15.36] And the problem it solves is when you're
[L874] [43:17.44] building SAS or an AI product and you
[L875] [43:20.00] want to sell to other companies, there's
[L876] [43:21.92] all these requirements you need to meet.
[L877] [43:24.00] There's SSO, there's SKIM, there's
[L878] [43:26.56] arbback, there's audit logs. These are
[L879] [43:29.04] all things that take time to integrate,
[L880] [43:31.04] but aren't the main focus of your app.
[L881] [43:33.04] Work OS is an API layer that lets you
[L882] [43:35.12] meet all of these requirements in just a
[L883] [43:37.44] few lines of code. So, let's say you
[L884] [43:39.28] have a new SAS product and you want to
[L885] [43:41.20] sell to other companies. work OS will
[L886] [43:43.52] solve all of these critical feature gaps
[L887] [43:45.44] for you. You can check them out at
[L888] [43:47.92] workos.com to learn more and get
[L889] [43:50.32] started. And I appreciate them for
[L890] [43:52.40] supporting my work and sponsoring this
[L891] [43:54.16] podcast. This all makes sense, but my
[L892] [43:56.56] immediate thought is where do you get
[L893] [43:58.40] the graph? Everything depends on where
[L894] [44:01.12] do you get on the input. Sometimes the
[L895] [44:04.72] input is in the data. Sometimes the
[L896] [44:07.12] input is in a judgment. But suppose you
[L897] [44:10.00] need a judgment for that. Okay. Are you
[L898] [44:14.08] are you giving up? If the judgment
[L899] [44:17.36] required
[L900] [44:18.96] uh intuitive, meaningful, something that
[L901] [44:21.84] you are willing to defend, right? Why
[L902] [44:25.20] not use judgment?
[L903] [44:27.44] Like if I know that if I know that the
[L904] [44:31.60] sun doesn't listen to the rooster
[L905] [44:33.84] crowing, right? Doesn't care. Okay. I
[L906] [44:37.20] strongly believe in that. Do I need the
[L907] [44:39.52] data to support it or I can insert it,
[L908] [44:43.04] assert it and defend it when needed? So
[L909] [44:47.68] this is a trick here which people don't
[L910] [44:49.60] realize don't don't appreciate. Okay.
[L911] [44:53.76] Judgment is not a no no if it is
[L912] [44:57.84] meaningful and if you can if
[L913] [45:01.92] if it is condensed is very few judgment
[L914] [45:05.36] can buy you lots of computation and if
[L915] [45:08.80] you are willing to defend it because
[L916] [45:10.64] it's so intuitive where you get the idea
[L917] [45:13.84] that where do you get the idea that the
[L918] [45:15.76] sun doesn't care about the rooster?
[L919] [45:17.44] Where have you done an experiment? No.
[L920] [45:20.48] But it's so obvious, right?
[L921] [45:22.64] Okay.
[L922] [45:23.76] >> But what if your intuition's wrong?
[L923] [45:26.08] >> Indeed, that's our problem. It's part of
[L924] [45:28.24] our problem. Even with
[L925] [45:30.72] talk about because what is a summary is
[L926] [45:34.96] average of all possible judgment that
[L927] [45:37.76] people put in the internet.
[L928] [45:40.96] It's a summary of a huge trillion number
[L929] [45:43.68] of judgment over which you have no
[L930] [45:45.36] control. Over which the LM does have no
[L931] [45:48.64] control. Okay? You live with it.
[L932] [45:51.92] Hopefully he put more weights
[L933] [45:55.52] on people whose judgment you trust and
[L934] [45:58.96] less weight on on just the quirks of
[L935] [46:03.84] people who purposely trying to get the
[L936] [46:08.64] system to fail. So no, there is wisdom
[L937] [46:12.32] in in in looking at the crowd judgment.
[L938] [46:16.88] There is wisdom in that, but there's
[L939] [46:19.20] also danger in that.
[L940] [46:21.20] Then after expert system and uncertainty
[L941] [46:24.40] in Beijian network came causality. I
[L942] [46:27.92] mentioned that in development of Beijian
[L943] [46:30.24] network I was extremely sure that
[L944] [46:35.20] probability
[L945] [46:36.88] they
[L946] [46:38.64] captures our intuition
[L947] [46:41.68] our reasoning mode and it's the best
[L948] [46:44.32] protection against paradoxes
[L949] [46:48.16] essentially that it it it's sufficient
[L950] [46:51.36] for capture human reasoning. I was wrong
[L951] [46:55.84] and I realized that already when the
[L952] [46:58.08] Beij became famous and popular and um I
[L953] [47:04.80] realized it by uh
[L954] [47:07.92] in the introduction to my book uh
[L955] [47:10.80] causality
[L956] [47:12.80] I confessed being wrong and and I I
[L957] [47:17.12] understand why I got into that why it's
[L958] [47:20.32] so it was misleading and
[L959] [47:23.92] The transition came when we looked into
[L960] [47:27.36] the simple phenomena that we never ask
[L961] [47:32.24] an expert
[L962] [47:34.32] to encode judge probabilistic judgment
[L963] [47:38.08] in a form of bijian network namely with
[L964] [47:41.12] arrows and dots. Okay. Always the arrows
[L965] [47:44.88] went from what we believe to be cause
[L966] [47:48.16] into the effect. It never went the other
[L967] [47:50.80] way around.
[L968] [47:52.64] psychological phenomena. Okay.
[L969] [47:56.64] Why [clears throat] is that?
[L970] [47:59.20] So people try to reverse errors. What
[L971] [48:02.16] about if you ask specifically give me
[L972] [48:04.64] error between the symptom and the
[L973] [48:06.32] disease?
[L974] [48:08.08] Bad judgment. If it couldn't put the
[L975] [48:10.96] right judgment. Evidently we have
[L976] [48:13.44] something in causality which is basic to
[L977] [48:16.32] our reasoning that is not captured by
[L978] [48:19.12] probability.
[L979] [48:21.12] And that was the idea of invariance.
[L980] [48:23.44] Yeah. The relationship between disease
[L981] [48:26.96] and fever is a stable one as opposed to
[L982] [48:31.60] the relationship between the opposite
[L983] [48:33.60] relationship
[L984] [48:35.36] also in variance. Yeah. When you talk
[L985] [48:37.84] about car diagnosis for instance and um
[L986] [48:42.64] [clears throat] so you have an expert
[L987] [48:44.88] system for diagnosing tr troubleshooting
[L988] [48:48.24] cars. Okay. And then you have a new
[L989] [48:51.28] model.
[L990] [48:53.28] Okay. So the um let's see the charger is
[L991] [48:57.28] on different corner of the of the motor.
[L992] [49:00.40] Okay. You don't need to reformulate
[L993] [49:05.44] your entire database from fresh. You
[L994] [49:09.12] only change one component
[L995] [49:11.76] the location of the charger. Okay. All
[L996] [49:15.36] the rest
[L997] [49:17.36] remains intact.
[L998] [49:19.60] So the whole system you can amortize the
[L999] [49:22.64] investment in eliciting knowledge that
[L1000] [49:25.12] you got in one system after a local
[L1001] [49:28.48] modification of the system and that if
[L1002] [49:32.00] you do it in a causal way in a causal
[L1003] [49:34.80] direction it doesn't work if you don't
[L1004] [49:37.52] do it in the causal direction and that
[L1005] [49:41.04] jolted me to think maybe you were wrong
[L1006] [49:44.24] or wrong and probability is not
[L1007] [49:46.32] sufficient if not what is sufficient
[L1008] [49:49.84] But let's capture the puzzle here. I
[L1009] [49:52.88] have a puzzle. You and I operate very
[L1010] [49:54.96] nicely with causation. Can we program
[L1011] [49:58.80] causation on a computer? Then this is a
[L1012] [50:02.16] a question because you we are so much
[L1013] [50:06.24] immersed in our language in and in our
[L1014] [50:09.92] assumptions that we cannot even
[L1015] [50:11.92] distinguish what is an assumption and
[L1016] [50:13.84] what is a conclusion. We just talked
[L1017] [50:17.12] cause and effect and we your assumption
[L1018] [50:19.68] are the same as mine. So there's no way
[L1019] [50:21.52] to convince you that we made an
[L1020] [50:22.88] assumption, right? We takes everything
[L1021] [50:25.12] for granted. But when you have to teach
[L1022] [50:27.60] it to a brainless robot, you have to
[L1023] [50:30.56] distinguish between assumptions and
[L1024] [50:33.44] conclusions and and logic.
[L1025] [50:37.92] That was a task. We had to invent a new
[L1026] [50:41.28] science, a new mathematics to capture a
[L1027] [50:44.48] new phenomena, the phenomena of cause
[L1028] [50:46.88] and effect.
[L1029] [50:48.88] It hasn't been done for us. Why?
[L1030] [50:53.68] Because science
[L1031] [50:56.24] was in bed with algebra
[L1032] [51:00.24] from the time of Galileo
[L1033] [51:04.48] from
[L1034] [51:06.08] 1632.
[L1035] [51:09.52] He invented what? He got the idea and he
[L1036] [51:12.32] was very happy that um science speaks
[L1037] [51:15.68] algebra
[L1038] [51:18.00] which is great because uh you can ask
[L1039] [51:21.44] questions and solve and get answers to
[L1040] [51:24.16] question that people could not do
[L1041] [51:26.32] without algebra like how the load on a
[L1042] [51:30.16] beam when would the beam break if you
[L1043] [51:32.40] put a certain load on it and you figure
[L1044] [51:34.80] out that in [clears throat] you can ask
[L1045] [51:38.48] questions both ways. is because the
[L1046] [51:41.44] equality sign is symmetric. So from
[L1047] [51:45.28] answering the question
[L1048] [51:48.08] uh when would the beam break if you put
[L1049] [51:50.96] a certain load on it? You can ask the
[L1050] [51:53.20] question how should you shape the beam
[L1051] [51:56.24] so that it will hold a load of that
[L1052] [51:59.52] magnitude. You can invert it. And that
[L1053] [52:03.04] was a real revolution in science.
[L1054] [52:08.56] I'm telling you my perception of
[L1055] [52:10.32] science. Not many philosopher will say
[L1056] [52:12.64] that was a revolution. I say so. Okay.
[L1057] [52:15.44] But perhaps they agree with me or not,
[L1058] [52:17.76] but
[L1059] [52:19.60] at least I I trace the evolution of
[L1060] [52:22.40] ideas carefully. And so that was a
[L1061] [52:26.88] revolution. Not it carries some
[L1062] [52:31.84] limitation
[L1063] [52:33.52] because equality sign is indeed
[L1064] [52:35.60] symmetric
[L1065] [52:37.20] and science has not developed
[L1066] [52:40.80] algebra for the directionality that we
[L1067] [52:44.48] see in cause and effect relationship. If
[L1068] [52:47.28] I tell you that the atmospheric pressure
[L1069] [52:50.48] affect the deviation of the barometer
[L1070] [52:52.64] and not the other way around, you agree
[L1071] [52:54.64] with me? Yeah. But if you write the
[L1072] [52:56.88] equation, the robot might think that
[L1073] [52:59.28] maybe fiddling around with the barometer
[L1074] [53:01.92] will change the weather tomorrow.
[L1075] [53:04.80] I'm talking about a stupid robot, right?
[L1076] [53:07.44] Yeah. But if you give him the equation,
[L1077] [53:10.80] it can work both ways. If F is equal to
[L1078] [53:14.16] M A, then M is equal to F / A, which
[L1079] [53:18.80] mean that if you want to change the
[L1080] [53:20.24] mass, okay, you increase the
[L1081] [53:22.00] acceleration or whatever, right?
[L1082] [53:25.20] The symmetry might
[L1083] [53:27.92] produce paradoxes, might use wrong
[L1084] [53:30.88] action. So the symmetry is the
[L1085] [53:33.68] limitation of algebra in terms of
[L1086] [53:36.32] capturing science
[L1087] [53:40.16] and we have to build a new algebra to
[L1088] [53:43.52] take care of the directionality that we
[L1089] [53:46.96] have in cause and effect relationship.
[L1090] [53:50.40] That takes computer science because we
[L1091] [53:53.84] in computer science have the operation
[L1092] [53:55.76] called assignment right when you assign
[L1093] [53:58.96] the content of register A into register
[L1094] [54:02.16] B it doesn't mean that is not reversible
[L1095] [54:06.48] okay so if you take the logic of
[L1096] [54:09.12] assignment
[L1097] [54:10.64] you put [clears throat] it on top of the
[L1098] [54:11.92] algebra on top of physics you get
[L1099] [54:15.84] causal science
[L1100] [54:18.56] and that's what I try to
[L1101] [54:20.72] And I think that I so far I'm very happy
[L1102] [54:24.96] what we what came up. We do have a new
[L1103] [54:27.04] algebra to capture cause and effect
[L1104] [54:30.24] relationship and we can answer
[L1105] [54:35.20] causal queries on three levels. The
[L1106] [54:38.72] ladder of causation from association to
[L1107] [54:41.68] intervention to explanation. Okay. So
[L1108] [54:46.64] and and we found out that we have a
[L1109] [54:48.40] ladder here in a hierarchy that you
[L1110] [54:52.40] cannot solve a
[L1111] [54:55.44] you cannot answer questions in in level
[L1112] [54:59.20] I unless you have assumptions of level I
[L1113] [55:03.60] or higher. So it's a hierarchy in the
[L1114] [55:06.72] formal sense
[L1115] [55:09.04] and we know how to handle it which is
[L1116] [55:11.44] very useful because you give me a query
[L1117] [55:14.88] I can tell you what level it is I can
[L1118] [55:17.12] tell you what assumption you might what
[L1119] [55:19.28] sort of assumption you need to have
[L1120] [55:21.68] before you can answer it and I can tell
[L1121] [55:24.00] you if you can get it from the data or
[L1122] [55:26.08] you can get it from experiments or you
[L1123] [55:28.16] can get it by somebody's else's
[L1124] [55:30.56] explanation or whatever but I can tell
[L1125] [55:33.44] you the source of knowledge that you
[L1126] [55:35.52] need in order to answer it.
[L1127] [55:38.96] >> Can you explain that causal hierarchy?
[L1128] [55:41.68] >> Ah yes yes that's very easy. It's a
[L1129] [55:45.52] threelevel um ladder
[L1130] [55:48.56] that goes from the bottom which is
[L1131] [55:51.20] association that's straight statistics.
[L1132] [55:54.64] If you [clears throat] see X what can
[L1133] [55:58.00] you tell me about Y? If you see
[L1134] [56:00.40] passively, hands off. Okay, no
[L1135] [56:03.92] intervention.
[L1136] [56:05.60] You're watching patients. Some of them
[L1137] [56:08.24] have cancer, some of them don't have,
[L1138] [56:10.72] some of them smoke, some of them don't
[L1139] [56:12.64] smoke. And you're trying to figure out
[L1140] [56:16.08] uh whether
[L1141] [56:18.72] how how many years a guy will live given
[L1142] [56:22.08] that he is a heavy smoker of that
[L1143] [56:25.04] magnitude. Okay, that's
[L1144] [56:28.08] association,
[L1145] [56:29.68] correlation.
[L1146] [56:32.48] That's entire
[L1147] [56:34.80] fields of probability and statistics.
[L1148] [56:37.68] This is what they teach you in
[L1149] [56:39.76] statistics 101 even to 808. Okay, it's
[L1150] [56:44.72] all they do.
[L1151] [56:47.84] And now comes the question, what I
[L1152] [56:49.76] intervene, what if I force you to smoke
[L1153] [56:54.00] five packs a day?
[L1154] [56:57.84] Don't laugh for me.
[L1155] [57:00.45] [laughter] It's illegal. I know. But if
[L1156] [57:03.60] you want to talk about
[L1157] [57:06.64] uh the probability of um living 20
[L1158] [57:11.60] years, if I start smoking tomorrow, I
[L1159] [57:15.20] have to think in terms of experience. I
[L1160] [57:16.96] stop, which means I'm going to choose to
[L1161] [57:20.08] smoke five packs a day. So it's a matter
[L1162] [57:23.12] of intervention. What is intervention?
[L1163] [57:25.84] Dimension is forcing you to do something
[L1164] [57:29.92] that you are not inclined to do
[L1165] [57:32.40] naturally. That's the second level
[L1166] [57:35.12] intervention or doing. If you have
[L1167] [57:39.20] experiments,
[L1168] [57:40.72] you can answer queries on level two.
[L1169] [57:46.64] But that's not the end because we also
[L1170] [57:49.12] need to ask to answer question of
[L1171] [57:51.60] explanation.
[L1172] [57:53.28] Given that I observe that I am 80 years
[L1173] [57:58.80] old and I am still alive and alert and I
[L1174] [58:03.84] smoke five packs a day.
[L1175] [58:06.72] What if I didn't smoke? Okay. Would I be
[L1176] [58:10.96] as alert? You Why is it different?
[L1177] [58:14.32] Because you have already information
[L1178] [58:16.48] about the outcome. Okay. You know how
[L1179] [58:19.44] I'm doing today. It gives you a an idea
[L1180] [58:23.44] about my metabolism and about my anatomy
[L1181] [58:27.60] that you didn't know before. Okay? And
[L1182] [58:31.28] using that you can find you can
[L1183] [58:34.88] try to figure out what the outcome would
[L1184] [58:38.88] have been had the input been different.
[L1185] [58:42.72] Okay,
[L1186] [58:44.48] that's a different level require
[L1187] [58:46.72] different kind of assumptions, different
[L1188] [58:49.44] techniques, different algebra we have it
[L1189] [58:53.36] so that I call it explanation. It's more
[L1190] [58:56.80] the creative retrospection
[L1191] [58:59.36] and it's not an easy problem even the
[L1192] [59:03.44] first level especially when you have
[L1193] [59:05.52] finite sample and you have to figure out
[L1194] [59:08.56] these are probabilities probabilities
[L1195] [59:10.88] mean properties of population right from
[L1196] [59:14.48] finite sample so I have all this
[L1197] [59:18.72] p level values and struggles among
[L1198] [59:25.36] such statisticians of what would be a
[L1199] [59:27.68] proper way of quantifying the
[L1200] [59:30.72] uncertainty that you have given you have
[L1201] [59:33.04] finite sample.
[L1202] [59:34.24] >> Where would you place LLMs in this
[L1203] [59:36.24] causal hierarchy?
