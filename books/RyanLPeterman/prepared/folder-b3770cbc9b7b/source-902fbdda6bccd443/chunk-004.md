Chunk 4; segments 992–1335. Start may repeat the previous chunk for context.

# Sergey Levine: Humanoid Robotics Results, Chinese Labs & Future Timelines

Source ID: source-902fbdda6bccd443
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Sergey_Levine_Humanoid_Robotics_Results,_Chinese_Labs_&_Future_Timelines_en.txt
Video: https://www.youtube.com/watch?v=9OSbaPjv0Rc

[L1001] [33:51.36] generalization across robots and I'm
[L1002] [33:53.28] sure other generalization too can be
[L1003] [33:54.56] facilitated with thinking just like an
[L1004] [33:56.56] LLMs but with a twist. You have to think
[L1005] [33:58.72] in the right modality.
[L1006] [34:00.56] >> Interesting. So it it outputs a I guess
[L1007] [34:03.12] that image is what its video sensor is
[L1008] [34:07.44] seeing and it's like the next step.
[L1009] [34:09.84] >> Yeah. You can almost think of it like
[L1010] [34:10.88] image editing. You can do the same thing
[L1011] [34:12.56] with video. You can do it with video
[L1012] [34:13.76] prediction. But the key is to like
[L1013] [34:15.36] imagine what it would look like to
[L1014] [34:18.08] progress on this task. Like that seems
[L1015] [34:20.32] like a very human thing to do, right?
[L1016] [34:21.84] You know, some things you can you you
[L1017] [34:23.68] plan semantically and some things you
[L1018] [34:25.76] plan spatially. Like if you're doing
[L1019] [34:27.28] rock climbing, you're probably not
[L1020] [34:28.64] thinking like, hey, left arm to rock 37
[L1021] [34:31.28] cm to the left. You're probably more
[L1022] [34:32.56] like imagining your arm reaching for the
[L1023] [34:34.08] rock. Earlier in the conversation, you
[L1024] [34:36.48] mentioned that Whimo was very inspiring
[L1025] [34:40.32] and um you know their kind of path to
[L1026] [34:43.84] productionization is proof that you can
[L1027] [34:45.84] do real world generalized robotics. And
[L1028] [34:49.68] if I recall correctly when I was, you
[L1029] [34:52.48] know, a lot younger, it was kind of this
[L1030] [34:54.96] early promise of this is going to happen
[L1031] [34:58.16] and then in reality it took a lot
[L1032] [35:01.04] longer. And so I guess my question is in
[L1033] [35:04.72] the case of humanoid robotics,
[L1034] [35:07.60] what would make you say singledigit
[L1035] [35:10.32] years it's coming versus a long tail and
[L1036] [35:14.16] you know policy challenges as well. I
[L1037] [35:16.08] could imagine.
[L1038] [35:17.28] >> I think one big difference between how
[L1039] [35:21.04] robotic foundation models address the
[L1040] [35:22.96] problem and how more traditional
[L1041] [35:24.56] engineered systems address the problem
[L1042] [35:26.00] is that the stack is really thin. So
[L1043] [35:28.40] it's not easy to train a foundation
[L1044] [35:30.08] model. You need to uh obviously you need
[L1045] [35:32.08] to get the right data. There's a lot of
[L1046] [35:33.36] work that goes into curating, labeling,
[L1047] [35:35.12] all that other kind of stuff. But the
[L1048] [35:36.88] actual software that runs on the robot
[L1049] [35:40.08] is very very simple. Uh so uh you know
[L1050] [35:43.52] you might have some kind of thinking or
[L1051] [35:45.04] reasoning stage. You might have uh you
[L1052] [35:47.68] might have the model produce actions. It
[L1053] [35:49.44] needs to be fast enough. But the like
[L1054] [35:52.56] just if you think about in terms of raw
[L1055] [35:54.16] lines of code, it's much much lower than
[L1056] [35:57.52] a more traditional AV stack. Uh and you
[L1057] [36:01.60] know, partly that's because modern
[L1058] [36:05.36] autonomous vehicles, the work on that
[L1059] [36:07.20] started a lot earlier with very
[L1060] [36:08.48] different technologies and evolved over
[L1061] [36:10.00] time. Partly it's also because the
[L1062] [36:12.08] problem is more safety critical. Like
[L1063] [36:13.84] yes, you don't want uh a robotic
[L1064] [36:15.60] manipulator to like drop a fragile
[L1065] [36:17.52] object, but at the end of the day,
[L1066] [36:19.76] that's a lot less bad than having a car
[L1067] [36:22.08] hit somebody. So that is not to say that
[L1068] [36:24.56] the safety challenges with robots are uh
[L1069] [36:28.16] are not real. They're very real and it's
[L1070] [36:29.84] very important to tackle them. In fact,
[L1071] [36:30.96] it's probably one of the harder ends of
[L1072] [36:32.48] the problem. But they are not as much of
[L1073] [36:35.36] a hard stop to practical deployments
[L1074] [36:39.28] because you can come up with tasks and
[L1075] [36:41.68] environments and domains and also
[L1076] [36:43.04] physical hardware where those problems
[L1077] [36:44.88] are a lot less uh severe. So uh I think
[L1078] [36:48.56] that that that combination radically
[L1079] [36:50.96] simpler software stack plus uh less uh
[L1080] [36:55.04] drastic software challenges I think
[L1081] [36:56.64] actually make it a lot easier and
[L1082] [36:58.08] because you know to your earlier point
[L1083] [37:00.16] uh that there is this kind of flywheel
[L1084] [37:01.68] effect that there's a positive feedback
[L1085] [37:03.04] loop that uh you know starting to get
[L1086] [37:05.28] things out in the world even under some
[L1087] [37:06.96] constraints will actually facilitate
[L1088] [37:08.72] getting them out more and more. I think
[L1089] [37:10.72] a lot of people are familiar with this
[L1090] [37:12.24] idea of a post-mortem,
[L1091] [37:14.72] you know, looking back on why something
[L1092] [37:17.04] failed. But in this case, I'm curious,
[L1093] [37:19.84] what would you say to a a premortem? And
[L1094] [37:23.04] in the sense of if humanoid robotics did
[L1095] [37:26.24] not succeed in single-digit years, what
[L1096] [37:28.96] do you think would be the most likely
[L1097] [37:30.48] reason why humanoid robotics failed?
[L1098] [37:34.48] Ultimately, for these things to to be
[L1099] [37:37.04] truly useful, they do need to reach a
[L1100] [37:39.28] level of reliability and robustness and
[L1101] [37:41.36] generalization that is higher than what
[L1102] [37:43.28] we typically expect from LLMs for
[L1103] [37:46.08] example uh or uh you know generative AI
[L1104] [37:48.88] for like images and video because
[L1105] [37:50.40] typically like these tools they are very
[L1106] [37:52.56] much human interactive tools like you
[L1107] [37:54.48] you get an LLM to do something and it
[L1108] [37:56.56] doesn't do quite what you want so you
[L1109] [37:58.00] sort of revise your prompt and you you
[L1110] [37:59.44] basically like you iterate with it and
[L1111] [38:01.12] and that's why like even the earlier um
[L1112] [38:03.92] LM tools like the first version of Chad
[L1113] [38:05.92] GPT, even though they were much more
[L1114] [38:07.84] primitive than what we have now, they
[L1115] [38:08.96] were still already useful because
[L1116] [38:10.32] somebody could just like keep hammering
[L1117] [38:11.84] out until it it basically solves their
[L1118] [38:14.00] problem. You know, just like if if
[L1119] [38:15.52] you're using a search engine, like you
[L1120] [38:16.64] type something into the search engine,
[L1121] [38:17.44] you don't get quite what you want. You
[L1122] [38:18.56] revise your query and then you get what
[L1123] [38:19.84] you want. Whereas with a robot, like the
[L1124] [38:22.48] the full value of it is unlocked when
[L1125] [38:24.24] it's actually doing the thing
[L1126] [38:25.04] autonomously. So it's it's having to
[L1127] [38:28.08] have somebody like constantly iterate
[L1128] [38:29.92] for every single task is almost like
[L1129] [38:31.36] antithetical to the benefit that you're
[L1130] [38:32.72] getting. So I think a lot of the risk
[L1131] [38:35.20] has to do with how easy is it to get
[L1132] [38:37.60] that level of reliability and
[L1133] [38:39.44] robustness. And that's again where some
[L1134] [38:41.44] of the demos might be like a little bit
[L1135] [38:42.96] misleading because if someone shows a
[L1136] [38:44.88] demo of the robot doing something cool I
[L1137] [38:46.80] mean you know obviously if if everything
[L1138] [38:48.56] is presented in a forthright way that's
[L1139] [38:50.88] that could still be very good indicator
[L1140] [38:52.08] of progress but it doesn't make it
[L1141] [38:54.40] obvious how far or how close it is to
[L1142] [38:57.52] reaching that practically relevant level
[L1143] [38:59.36] of robustness. So, I'm personally a big
[L1144] [39:02.24] believer in uh using uh techniques like
[L1145] [39:06.24] reinforcement learning that can actually
[L1146] [39:08.00] benefit from autonomous experience to
[L1147] [39:10.24] kind of fine-tune that last few
[L1148] [39:11.68] percentage points to make it go from
[L1149] [39:13.44] like 95 to actually 100%. But that's
[L1150] [39:16.16] really important and it's not yet a
[L1151] [39:17.36] solved problem.
[L1152] [39:18.48] >> If it did take longer than expected,
[L1153] [39:21.44] it's because the bar is higher. because
[L1154] [39:23.28] the bar is higher and in particular like
[L1155] [39:25.04] those last few uh the kind of the last
[L1156] [39:27.68] inch so to speak is something that
[L1157] [39:30.24] requires not just really good models but
[L1158] [39:32.56] also new innovations in technology. I
[L1159] [39:35.36] mean I don't think that you know I'm not
[L1160] [39:38.00] the kind of person that would say like
[L1161] [39:39.12] oh we should like throw out everything
[L1162] [39:40.32] that we know about foundation models and
[L1163] [39:41.60] start over. I don't think it's that at
[L1164] [39:42.56] all. I think that roughly the puzzle
[L1165] [39:44.64] pieces that we have are actually very
[L1166] [39:45.92] good puzzle pieces. But still we should
[L1167] [39:47.68] acknowledge that right now the methods
[L1168] [39:50.40] and the models need more work to cross
[L1169] [39:53.92] that level of robustness.
[L1170] [39:55.44] >> In LLMs it feels like everyone is doing
[L1171] [39:58.40] kind of the same thing but different
[L1172] [40:00.48] flavors in the robotics industry. Is it
[L1173] [40:04.48] is everyone doing kind of the same
[L1174] [40:05.92] thing? Are there any hottake
[L1175] [40:07.60] architectures that are different
[L1176] [40:09.04] direction? I actually think that there's
[L1177] [40:10.88] a lot more heterogeneity than it might
[L1178] [40:12.48] seem. Um, one big dividing line that I
[L1179] [40:15.52] think is maybe not as obvious uh from
[L1180] [40:18.56] just kind of looking at the results is
[L1181] [40:20.72] the distinction between kind of fully
[L1182] [40:23.12] embracing the foundation model ethos so
[L1183] [40:25.68] to speak versus uh focusing on spec
[L1184] [40:29.68] specific like kind of vertical areas.
[L1185] [40:32.40] And I think this is like kind of hard to
[L1186] [40:35.04] tease out sometimes because obviously
[L1187] [40:36.32] like you know everyone's going to say
[L1188] [40:37.28] like oh I'm doing the thing that LM did
[L1189] [40:39.12] like because like that's the cool thing
[L1190] [40:41.04] but you know the foundational model
[L1191] [40:42.80] ethos fundamentally is something like
[L1192] [40:45.36] this that if you have a particular
[L1193] [40:47.76] problem you want to solve it is better
[L1194] [40:49.68] to train a more general model that can
[L1195] [40:52.24] use data from a breadth of problems and
[L1196] [40:54.88] if you do it right it'll actually be
[L1197] [40:56.40] better at the specialized problem you
[L1198] [40:57.84] want to solve than a narrow specialist.
[L1199] [41:00.24] So you know to again to come back to the
[L1200] [41:01.92] LM analogy if you want to do machine
[L1201] [41:03.28] translation don't build a machine
[L1202] [41:05.12] translation system build a language
[L1203] [41:06.40] model that understands all language
[L1204] [41:08.08] tasks and then throw it at machine
[L1205] [41:09.36] translation
[L1206] [41:10.96] and in robotics I think that is like
[L1207] [41:12.48] actually very deeply uncomfortable to
[L1208] [41:14.00] people because if someone is actually
[L1209] [41:15.76] like working on an application like
[L1210] [41:17.12] they're doing like warehouse automation
[L1211] [41:18.96] it is very awkward to then to to like
[L1212] [41:21.84] think like oh if I want to do warehouse
[L1213] [41:23.76] automation let me like collect data of
[L1214] [41:25.44] like putting away silverware in
[L1215] [41:26.72] kitchens. It just it just sounds
[L1216] [41:28.40] bizarre. But that is the foundation
[L1217] [41:31.04] model lesson that if you have enough
[L1218] [41:32.40] breadth, if you collect data from a wide
[L1219] [41:34.96] range of different tasks, then you will
[L1220] [41:36.72] acquire those generalizable skills and
[L1221] [41:39.28] if your model is is is built correctly,
[L1222] [41:41.20] it will repurpose those skills for
[L1223] [41:42.96] whatever situation it encounters. So I
[L1224] [41:45.52] think it is actually true that if even
[L1225] [41:46.88] if you want to build a warehousing
[L1226] [41:48.16] robot, you're better off collecting a
[L1227] [41:50.08] breath of data and will be better at
[L1228] [41:51.84] handling all the weird edge cases you
[L1229] [41:53.44] might encounter even in that warehouse
[L1230] [41:54.80] domain. But this is not something that's
[L1231] [41:56.32] easy for people to accept because it's
[L1232] [41:57.84] just so like antithetical to the uh
[L1233] [42:00.96] principle of building kind of a a
[L1234] [42:03.12] traditional vertically integrated
[L1235] [42:04.40] robotic system.
[L1236] [42:05.76] >> I noticed this this uh new interesting
[L1237] [42:09.52] phenomenon with these AI companies which
[L1238] [42:12.48] is if they are wildly successful it
[L1239] [42:16.64] creates this um I guess worry or new set
[L1240] [42:19.84] of things. So for instance when
[L1241] [42:22.08] enthropic became had a very powerful
[L1242] [42:24.16] model then the government comes in and
[L1243] [42:27.60] there's these you know worries about
[L1244] [42:30.08] safety and and risk and all that and I'm
[L1245] [42:33.84] I'm curious how you think about that
[L1246] [42:35.68] like if if physical intelligence this
[L1247] [42:38.40] year had a phenomenal incredibly capable
[L1248] [42:42.08] generalized model how do you think about
[L1249] [42:45.52] those kinds of topics that might come up
[L1250] [42:48.16] >> working on AI safety is not a new uh my
[L1251] [42:50.64] my colleague at UC Berkeley Stuart
[L1252] [42:52.16] Russell was talking about this stuff
[L1253] [42:53.84] like over a decade ago and lots of
[L1254] [42:55.92] people spent a lot of time working on
[L1255] [42:57.28] it. It's just that the trouble is when
[L1256] [42:59.76] the technology moves so fast the
[L1257] [43:02.08] important problems are not just a
[L1258] [43:03.60] function of like you know the core
[L1259] [43:05.92] principles it's also a function of how
[L1260] [43:07.28] society reacts to it what kind of tools
[L1261] [43:09.12] are adopted and so on um and I think
[L1262] [43:12.64] that's very very hard to anticipate so
[L1263] [43:15.52] um I don't have like a very satisfying
[L1264] [43:17.60] answer here in terms of how we are
[L1265] [43:21.04] approaching it our philosophy around all
[L1266] [43:23.28] this stuff is
[L1267] [43:26.24] basically one of empirical
[L1268] [43:28.08] experimentation like let's get stuff out
[L1269] [43:30.00] there. Let's see what happens in the
[L1270] [43:31.36] real world. Let's see what goes right
[L1271] [43:32.64] and what goes wrong so that we have as
[L1272] [43:34.88] much of a preview for you know what the
[L1273] [43:37.68] technology can do, what are its
[L1274] [43:39.60] weaknesses, what are its strengths uh
[L1275] [43:42.00] and and so on. But you know at the end
[L1276] [43:44.32] of the day you kind of have to just like
[L1277] [43:45.84] keep your eyes open, see what happens
[L1278] [43:47.44] and adjust as you go. It's it's very
[L1279] [43:49.12] hard to anticipate. And you know, I
[L1280] [43:51.44] think your question though is very
[L1281] [43:52.80] spoton even though I don't have a great
[L1282] [43:54.72] answer for you because like yeah, if
[L1283] [43:57.28] we're having like this much um concern
[L1284] [44:00.24] and and uh issues with AI systems that
[L1285] [44:04.96] are basically limited to using
[L1286] [44:06.32] computers, we're presumably going to
[L1287] [44:08.32] have strictly more concerns and issues
[L1288] [44:10.40] with AI systems that can do everything
[L1289] [44:12.88] in the physical world that we can do,
[L1290] [44:14.72] right? So the issues are real. It's
[L1291] [44:16.08] just, you know, you kind of have to like
[L1292] [44:17.60] see what happens and then adjust. And
[L1293] [44:19.44] that's kind of in the the scary path.
[L1294] [44:21.68] But in the in the happy path, if
[L1295] [44:24.32] everything goes well and we have
[L1296] [44:26.00] incredibly capable models and uh robots
[L1297] [44:31.04] in 10 years, is the north star that
[L1298] [44:34.88] that's the end of human labor. I believe
[L1299] [44:38.40] it's a mistake to think of robots as
[L1300] [44:41.44] mechanical people, right? like um you
[L1301] [44:44.32] know computers at some level are kind of
[L1302] [44:45.92] like mechanical brains but when personal
[L1303] [44:48.88] computers like really took off in the
[L1304] [44:50.72] '9s early 2000s etc. It's not like the
[L1305] [44:54.08] first thing that happened is that you
[L1306] [44:55.76] know people replaced their brains with
[L1307] [44:57.28] computers rather what we saw is actually
[L1308] [44:58.96] a proliferation of very different kinds
[L1309] [45:00.56] of computers. We saw kind of like uh
[L1310] [45:02.48] ubiquitous computing. So you would have
[L1311] [45:04.16] a computer on your desk but you might
[L1312] [45:05.52] also have one in your pocket. You might
[L1313] [45:06.96] have one in your refrigerator and in
[L1314] [45:08.32] your car like because computing became
[L1315] [45:10.32] so accessible, you could have a little
[L1316] [45:12.40] bit of computing in everything. And you
[L1317] [45:14.80] know, I don't think that that's what
[L1318] [45:15.84] like the the people that first started
[L1319] [45:19.04] thinking about this stuff in the 40s and
[L1320] [45:20.40] 50s would have imagined. They would have
[L1321] [45:21.60] imagined like, you know, roomsiz
[L1322] [45:22.96] computers that whose job it is to like
[L1323] [45:25.20] control the the the you know, the policy
[L1324] [45:28.16] of an entire country or something rather
[L1325] [45:30.00] than like a little bit of computer in
[L1326] [45:31.28] everybody's refrigerator. So I think
[L1327] [45:33.04] it's it's you know by analogy of that we
[L1328] [45:34.80] might imagine there might be like a
[L1329] [45:36.08] little bit of physical actuation in
[L1330] [45:37.84] everything and it might just be like
[L1331] [45:40.08] lots of everyday things that you have to
[L1332] [45:42.24] do yourself now you get like a little
[L1333] [45:44.16] bit of help with it. I think the other
[L1334] [45:47.76] example that's worth thinking about is
[L1335] [45:50.32] um modern coding agents, right? So I I
[L1336] [45:52.96] think that you know this is something
[L1337] [45:53.84] where of course the jury is still out as
[L1338] [45:55.20] to what the endgame of coding agents is,
[L1339] [45:57.60] but certainly uh from the experience of
[L1340] [46:01.44] uh software engineers today. Like it
[L1341] [46:03.04] kind of seems like probably fair to say
[L1342] [46:05.68] that most would consider coding agents
[L1343] [46:07.28] to be more empowering them rather than
[L1344] [46:10.56] like uh you know uh somehow causing them
