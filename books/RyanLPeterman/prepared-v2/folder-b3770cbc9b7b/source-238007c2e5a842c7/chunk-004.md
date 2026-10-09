Chunk 4; segments 1051–1407. Start may repeat the previous chunk for context.

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

Source ID: source-238007c2e5a842c7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_P_vs_NP,_Zero-Knowledge_Proofs,_Quantum_Computation_Avi_Wigderson_en.txt
Video: https://www.youtube.com/watch?v=5GUcvSAJcJw

[L1060] [49:31.36] guaranteeing I mean you are running it
[L1061] [49:33.04] really on your laptop you it's not you
[L1062] [49:35.12] know okay the paper was written we can
[L1063] [49:38.00] test primality with probabistic
[L1064] [49:39.76] algorithm now we want to run it what do
[L1065] [49:41.44] you use so it makes sense to ask lots of
[L1066] [49:44.88] questions about randomness but to
[L1067] [49:46.64] guarantee the quality of the randomness
[L1068] [49:49.92] um and maybe you can minimize the is the
[L1069] [49:53.36] use of randomness by the way another
[L1070] [49:55.76] issue with randomness is that
[L1071] [49:58.24] you know the outcome is a random
[L1072] [49:59.92] variable and it's not always correct
[L1073] [50:02.40] right the whole point in most of these
[L1074] [50:04.08] algorithms you just have some small
[L1075] [50:06.32] probability of error if you have a
[L1076] [50:08.48] deterministic algorithm there's no error
[L1077] [50:11.20] so you also don't like the error so
[L1078] [50:14.48] treating it as a resource is simply a
[L1079] [50:16.88] convenient complexity theoretic way of
[L1080] [50:19.20] saying how do we understand you know uh
[L1081] [50:23.28] the amount of this resource we have to
[L1082] [50:25.52] invest or the number of bits we have to
[L1083] [50:27.28] invest
[L1084] [50:28.24] their quality and so on. So it's uh yeah
[L1085] [50:31.76] it's it's almost automatic for if you
[L1086] [50:34.96] think like a like a complexity theories.
[L1087] [50:37.60] How do we minimize for particular
[L1088] [50:39.68] algorithm like primarity testing
[L1089] [50:42.64] you know do you really need this? Do you
[L1090] [50:44.88] need them to be independent? Maybe you
[L1091] [50:46.72] can generate them in a you know maybe
[L1092] [50:49.20] you can you need n bits but you can
[L1093] [50:51.20] start from square n bits or from log n
[L1094] [50:53.68] bits that are really random and make
[L1095] [50:56.16] from them in some deterministic way uh
[L1096] [51:00.40] you know sort of pseudo random sequence
[L1097] [51:02.56] you can call it which is a good name
[L1098] [51:04.64] actually uh that will for this purpose
[L1099] [51:07.68] of this algorithm will look as if it was
[L1100] [51:11.76] random.
[L1101] [51:13.36] If you could do that, you don't need all
[L1102] [51:15.28] these bits. You can use much fewer. And
[L1103] [51:18.24] this whole theory of you know reducing
[L1104] [51:21.36] randomness, dandomization, removing
[L1105] [51:23.60] randomness is a huge field. And uh
[L1106] [51:27.12] people are you know there there are many
[L1107] [51:30.00] u problems and many ways of doing it and
[L1108] [51:33.04] uh uh the story with primality is
[L1109] [51:35.92] actually fascinating. So I mentioned
[L1110] [51:39.28] these two algorithms that were invented
[L1111] [51:41.20] and people were wondering about the
[L1112] [51:43.36] deterministic algorithm for primality.
[L1113] [51:45.36] It's a problem that has been articulated
[L1114] [51:48.32] already by Gaus in the most you know
[L1115] [51:51.84] complex theoretic way you can you know
[L1116] [51:55.92] uh back in his days hundreds of years
[L1117] [51:58.96] ago and uh maybe 150 I don't know
[L1118] [52:03.84] he was asking for an indefatigable
[L1119] [52:07.12] calculator
[L1120] [52:08.72] of course is a person but
[L1121] [52:11.36] he wanted this to be efficient that's
[L1122] [52:13.84] bas basically what
[L1123] [52:15.76] uh was looking for a primality test for
[L1124] [52:18.48] large numbers because they really wanted
[L1125] [52:20.16] to know about numbers maybe only few
[L1126] [52:22.72] tens of digits. They wanted to know
[L1127] [52:24.40] whether they are prime or not. There was
[L1128] [52:26.72] no efficient algorithm. Anyway, uh you
[L1129] [52:30.24] can wonder about this survey s and
[L1130] [52:32.80] algorithm.
[L1131] [52:34.56] Maybe you can use less randomness or
[L1132] [52:36.88] structural randomness that you can
[L1133] [52:38.48] generate from fewer bits and nobody had
[L1134] [52:41.76] any good idea. And then in the early
[L1135] [52:44.16] 2000s
[L1136] [52:46.00] Agaral Kay and Fenna
[L1137] [52:48.80] uh devised a different probabilistic
[L1138] [52:52.08] primality test and it's different. So
[L1139] [52:55.52] the analysis of randomness in it is
[L1140] [52:58.40] different and once you understand how
[L1141] [53:01.04] randomness is used,
[L1142] [53:03.44] you can maybe say ah we don't need to be
[L1143] [53:06.16] really totally independent bits. it's
[L1144] [53:08.56] it's okay if it has some structure and
[L1145] [53:12.24] then they found using number theoretic
[L1146] [53:15.04] ways uh a method to to generate this
[L1147] [53:20.40] pseudo you know pseudo randomly
[L1148] [53:22.32] generated from very few bits and that's
[L1149] [53:25.76] that's how the so often I don't know
[L1150] [53:28.72] often but sometimes deterministic
[L1151] [53:31.04] versions of probabistic algorithms are
[L1152] [53:34.00] discovered in simply understanding the
[L1153] [53:37.36] way in which the algorithm is using the
[L1154] [53:39.52] randomness understanding the analysis of
[L1155] [53:41.76] the algorithm
[L1156] [53:43.20] >> and saying okay it doesn't use all that
[L1157] [53:47.60] much
[L1158] [53:49.04] >> you you mentioned a few times the
[L1159] [53:51.20] quality of the randomness
[L1160] [53:52.96] >> how do you quantify the quality of
[L1161] [53:55.60] random bits
[L1162] [53:56.64] >> this basically a question about what
[L1163] [54:00.64] sudo randomness is and the general
[L1164] [54:02.72] answer is that it depends
[L1165] [54:05.84] uh you want
[L1166] [54:08.32] to fool a particular algorithm let's say
[L1167] [54:10.64] for primality.
[L1168] [54:12.40] So you want the randomness to fool the
[L1169] [54:15.04] this you want the al this algorithm not
[L1170] [54:18.00] to notice that you switched from perfect
[L1171] [54:21.20] randomness to something that's really
[L1172] [54:24.00] far less random has far less entropy but
[L1173] [54:26.96] the analysis works nonetheless.
[L1174] [54:29.60] Another algorithm maybe you need you a
[L1175] [54:32.64] completely different type of pseudo
[L1176] [54:34.40] randomness for it. There are there's a
[L1177] [54:36.80] set of examples of uh algorithmic
[L1178] [54:39.52] problems for which when you look at the
[L1179] [54:41.60] analysis they are much simpler than this
[L1180] [54:43.52] primality uh testing. When you look at
[L1181] [54:45.92] the analysis it seems to use not the
[L1182] [54:49.44] independence of all the n bits. You
[L1183] [54:52.00] really need only every pair of them to
[L1184] [54:54.16] be independent or every triple and
[L1185] [54:58.40] spaces of random variables which have
[L1186] [55:00.96] this property are much smaller. you can
[L1187] [55:03.92] generate them from login bits and so you
[L1188] [55:07.52] can fool them with this stuff. So the
[L1189] [55:09.20] quality of randomness there's a phrase I
[L1190] [55:12.00] like that it's the quality of randomness
[L1191] [55:14.64] is in the eye of the beholder
[L1192] [55:17.28] uh or in the computational power of the
[L1193] [55:19.36] beholder. You really need it to be just
[L1194] [55:22.48] as good as the tests that are applied to
[L1195] [55:26.16] it. You know you just want to be
[L1196] [55:28.48] completely pragmatic. You don't care
[L1197] [55:31.04] whether it's random or not. You just
[L1198] [55:32.72] care that an observer of a particular
[L1199] [55:36.32] structure or particular computational
[L1200] [55:38.72] power will not distinguish the
[L1201] [55:42.56] pseudo random distribution which have
[L1202] [55:44.56] may have less much less randomness in it
[L1203] [55:47.04] than the perfect one.
[L1204] [55:48.64] >> In one of your lectures actually you you
[L1205] [55:50.80] mentioned that and you gave a good
[L1206] [55:52.08] example and I was wondering if you could
[L1207] [55:54.32] um give the intuitive example of why
[L1208] [55:57.12] randomness is a function of the
[L1209] [55:58.96] observer's computational power.
[L1210] [56:00.96] >> Yeah. So I uh if you watch this talk you
[L1211] [56:04.08] know what the the example I give is an
[L1212] [56:06.48] example that's taken from this
[L1213] [56:08.64] fundamental paper of Manuel Blum and
[L1214] [56:12.96] Sylvia Malli. They tell you to consider
[L1215] [56:16.08] three experiments and the experiments go
[L1216] [56:20.16] as follows. They always between you and
[L1217] [56:22.56] me. You are the observer. I am the coin
[L1218] [56:24.80] tosser. I have a coin on my finger and I
[L1219] [56:28.08] toss it and just as it leaves my finger
[L1220] [56:31.84] you are supposed to predict what the
[L1221] [56:34.24] value will be when it falls on the floor
[L1222] [56:36.48] like in two seconds you have to
[L1223] [56:39.12] immediately say heads or tails. Okay
[L1224] [56:42.24] before you have to predict before it
[L1225] [56:44.00] falls. Uh well this is the first
[L1226] [56:47.92] experiment and uh you know what I ask
[L1227] [56:50.08] and what they ask you know what do you
[L1228] [56:52.00] think is a success your success what are
[L1229] [56:55.20] your chances of predicting it and the
[L1230] [56:57.52] obvious answer is you know one half you
[L1231] [56:59.60] know what uh how can it help you know
[L1232] [57:02.64] how what what can you do
[L1233] [57:05.44] the second is when you sit there but you
[L1234] [57:07.68] have a laptop like you have now and uh
[L1235] [57:11.12] yeah what what can you you will yeah I
[L1236] [57:13.68] don't know that you can how fast you
[L1237] [57:15.36] type, but the coin will be on the floor
[L1238] [57:19.28] in a second. The third experiment is
[L1239] [57:22.72] where your laptop is connected to a Cray
[L1240] [57:25.44] superco computer and the Cray superco
[L1241] [57:27.28] computer is connected to a bunch of
[L1242] [57:29.60] sensors and cameras and whatever devices
[L1243] [57:33.12] you want. They are all trained on my
[L1244] [57:35.20] finger.
[L1245] [57:36.72] Okay? And so as it leaves my finger the
[L1246] [57:39.44] coin the this apparatus certainly is
[L1247] [57:44.00] more than enough to calculate all the
[L1248] [57:46.88] you know angular momentum of the coin
[L1249] [57:49.44] and the distance to the floor and the
[L1250] [57:51.36] humidity in the air and whatever
[L1251] [57:52.96] parameters that completely determine its
[L1252] [57:56.64] motion in particular how it will land in
[L1253] [57:59.68] a split second far less than the time
[L1254] [58:02.40] needed to. So the the real point in this
[L1255] [58:07.04] example is
[L1256] [58:09.68] that the experiment the random cointos
[L1257] [58:14.48] this cointos did not change in all of
[L1258] [58:16.64] them. It is the same what you know
[L1259] [58:21.36] masses of people in math and physics and
[L1260] [58:24.32] philosophy and you know defined
[L1261] [58:26.64] randomness in various ways. There are
[L1262] [58:28.40] many definitions of of randomness and
[L1263] [58:31.36] they all focus on this event on the
[L1264] [58:34.48] cointos or sequence of cointoses. We in
[L1265] [58:37.52] complexity theory starting from this
[L1266] [58:39.60] paper
[L1267] [58:41.52] don't care about this event. I mean the
[L1268] [58:43.76] event stays the same and all it focuses
[L1269] [58:46.08] on the observer and it the only thing
[L1270] [58:49.12] that changed in these three experiments
[L1271] [58:51.36] is the computational power. So we want
[L1272] [58:54.64] to know how much enthropy is in the
[L1273] [58:56.40] coin. If you don't have enough
[L1274] [58:58.32] computational power, it seems to be full
[L1275] [59:00.96] entropy. It's a half half, right? You
[L1276] [59:03.52] don't know what it will be. If you have
[L1277] [59:05.60] enough computational power, you can
[L1278] [59:07.44] predict it completely and then it has
[L1279] [59:10.72] zero entropy.
[L1280] [59:12.56] So what changed is the observer. So the
[L1281] [59:16.00] observer is this algorithm we talked
[L1282] [59:18.00] about before. And uh any test that's
[L1283] [59:20.00] applied to you know uh to a set of to a
[L1284] [59:24.88] distribution to test the quality of
[L1285] [59:27.04] randomness depending on the test you
[L1286] [59:29.20] want to just make sure you you you want
[L1287] [59:33.04] to use as little true randomness uh in a
[L1288] [59:36.24] way that the observer will not notice.
[L1289] [59:38.96] And this is the source of many of the
[L1290] [59:41.44] important theorems that
[L1291] [59:44.00] um you know show that you can remove
[L1292] [59:47.76] remove randomness or reduce randomness
[L1293] [59:50.88] uh uh in probabilistic algorithms with
[L1294] [59:54.00] or without assumptions and uh uh really
[L1295] [59:57.68] are behind this understanding that we
[L1296] [59:59.60] have today. Randomness in algorithms is
[L1297] [01:00:01.84] not as powerful as we thought it is.
[L1298] [01:00:04.40] Like if if you know that something like
[L1299] [01:00:06.96] P is [clears throat] different than NP
[L1300] [01:00:08.56] or you have a hardware sing salesman is
[L1301] [01:00:11.44] exponentially hard or sus. If you know
[L1302] [01:00:14.72] that then in fact I can give you a sud
[L1303] [01:00:18.56] random generator that will dandomize any
[L1304] [01:00:22.64] probabistic algorithms. We know that
[L1305] [01:00:24.64] under this assumption we have what we
[L1306] [01:00:26.56] call P= BPP. Anything that has an
[L1307] [01:00:29.52] efficient probabistic algorithm also has
[L1308] [01:00:32.24] a probab
[L1309] [01:00:34.00] an efficient deterministic algorithm.
[L1310] [01:00:36.40] You just need to know that there is a
[L1311] [01:00:39.12] hard function somewhere. Under what
[L1312] [01:00:41.12] assumptions do we know P equals BPP? uh
[L1313] [01:00:45.44] the assumption uh the very natural is
[L1314] [01:00:50.64] that one of these NPR problems or in
[L1315] [01:00:54.24] fact even problems in higher classes
[L1316] [01:00:57.92] requires a lot of hardware require
[L1317] [01:01:00.56] exponential size circuits to solve okay
[L1318] [01:01:04.32] we believe that it's like P versus NP
[L1319] [01:01:07.92] strengthened you cannot cut down the
[L1320] [01:01:10.88] exponential search space
[L1321] [01:01:13.44] Um and uh so maybe people are you know
[L1322] [01:01:19.12] happier with with with this assumption
[L1323] [01:01:21.20] but this assumption about uh time
[L1324] [01:01:24.72] complexity it has no randomness in it.
[L1325] [01:01:28.56] It's sort of at first it's shocking uh
[L1326] [01:01:32.00] that it's actually related to the
[L1327] [01:01:34.24] problem of removing randomness from
[L1328] [01:01:36.72] algorithms. So that's one fundament
[L1329] [01:01:39.60] fundamental connection. It's this
[L1330] [01:01:42.00] hardness versus randomness paradigm.
[L1331] [01:01:45.76] But we know even more. We know that it
[L1332] [01:01:49.20] goes both ways. We know that if you are
[L1333] [01:01:52.96] trying to remove randomness for some
[L1334] [01:01:55.12] algorithms, if you can do that, then you
[L1335] [01:01:59.68] found the hard function.
[L1336] [01:02:02.32] So there's really a an almost it's not
[L1337] [01:02:05.28] an exact if and only if but
[L1338] [01:02:08.96] uh again and there are many variants of
[L1339] [01:02:11.76] this in some variants is if and only if
[L1340] [01:02:14.32] is stronger but we really know that it's
[L1341] [01:02:16.72] really one of the other and since it's
[L1342] [01:02:19.60] hard to believe that all these hard
[L1343] [01:02:21.84] problems are easy or the similing the
[L1344] [01:02:23.92] hard problem like P= NP we tend much
[L1345] [01:02:26.72] more to believe the other alternative
[L1346] [01:02:28.64] name is that randomness in algorithms is
[L1347] [01:02:31.12] weak and you can remove it.
[L1348] [01:02:33.52] >> Open AAI, Enthropic, Cursor, and
[L1349] [01:02:36.48] Verscell all use this product to make
[L1350] [01:02:38.64] their lives better. And the problem it
[L1351] [01:02:40.80] solves is when you're building SAS or an
[L1352] [01:02:43.12] AI product, and you want to sell to
[L1353] [01:02:45.20] other companies, there's all these
[L1354] [01:02:46.96] requirements you need to meet. There's
[L1355] [01:02:48.88] SSO, there's SKIM, there's arbback,
[L1356] [01:02:52.16] there's audit logs. These are all things
[L1357] [01:02:53.92] that take time to integrate, but aren't
[L1358] [01:02:56.16] the main focus of your app. Work OS is
[L1359] [01:02:58.32] an API layer that lets you meet all of
[L1360] [01:03:00.16] these requirements in just a few lines
[L1361] [01:03:02.40] of code. So let's say you have a new SAS
[L1362] [01:03:04.80] product and you want to sell to other
[L1363] [01:03:06.40] companies. Work OS will solve all of
[L1364] [01:03:08.56] these critical feature gaps for you. You
[L1365] [01:03:11.36] can check them out at workos.com to
[L1366] [01:03:13.84] learn more and get started. And I
[L1367] [01:03:16.00] appreciate them for supporting my work
[L1368] [01:03:17.68] and sponsoring this podcast. Is [snorts]
[L1369] [01:03:19.92] there an intuitive explanation for the
[L1370] [01:03:22.08] relationship between problem hardness
[L1371] [01:03:24.48] and randomness? Yeah. [laughter]
[L1372] [01:03:27.44] Yeah. There's almost always an intuitive
[L1373] [01:03:29.76] explanation for Yeah. So what's the hard
[L1374] [01:03:33.20] what's the hard problem? I give you the
[L1375] [01:03:35.84] input. You you are a limited computer.
[L1376] [01:03:38.48] You are a polinomial time algorithm. I
[L1377] [01:03:41.12] give you the input. Let's say it's a
[L1378] [01:03:43.28] traveling salesman problem or you don't
[L1379] [01:03:46.48] know the answer. So you there's some
[L1380] [01:03:48.72] entropy in the answer, right? It's in
[L1381] [01:03:51.52] the same sense we discussed before
[L1382] [01:03:54.08] there's some entropy tiny entropy maybe
[L1383] [01:03:56.40] exponentially small entropy because
[L1384] [01:03:58.32] maybe the you know if the input is
[L1385] [01:04:00.40] random maybe only few instances are hard
[L1386] [01:04:04.08] and all the others you can solve but at
[L1387] [01:04:06.56] least you see a hint of a relationship
[L1388] [01:04:09.84] between hardness and entropy. This of
[L1389] [01:04:13.36] course is not satisfactory because we
[L1390] [01:04:15.20] want half we want the you know we want
[L1391] [01:04:18.48] uh that for you the answer will be like
[L1392] [01:04:21.12] a cointos not like a very biased
[L1393] [01:04:23.68] cointos.
[L1394] [01:04:25.28] So we need to find ways to amplify
[L1395] [01:04:28.88] this uh uncertainty for you. They
[L1396] [01:04:31.68] amplify the hardness. We want not just
[L1397] [01:04:33.60] that some instances will be hard but
[L1398] [01:04:36.40] that the random instance
[L1399] [01:04:39.44] whether the answer is yes or no for
[L1400] [01:04:42.80] polomial time observer will be half you
[L1401] [01:04:47.28] will not be able to gain an epsilon
[L1402] [01:04:49.60] advantage over a random guess.
[L1403] [01:04:54.00] So for this there we developed all sorts
[L1404] [01:04:56.24] of methods that amplify amplify
[L1405] [01:04:59.44] randomness. Now this doesn't solve the
[L1406] [01:05:02.24] problem at all because I managed to take
[L1407] [01:05:05.28] you know n bits a random instance of a
[L1408] [01:05:07.60] problem and manufacture one bit that's
[L1409] [01:05:11.28] hard for you to guess but I could have
[L1410] [01:05:13.84] taken the first random bit I pick for
[L1411] [01:05:16.24] the so I generate from many a few one
[L1412] [01:05:21.04] what you want to do is the opposite you
[L1413] [01:05:22.80] want a method that will take a few and
[L1414] [01:05:25.52] we generate many
[L1415] [01:05:28.08] right that's a random generator So, so
[L1416] [01:05:30.48] the random generator starts for a few
