Chunk 4; segments 1058–1415. Start may repeat the previous chunk for context.

# Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura

Source ID: source-70f1e2ca6c128ddc
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lean_Handwritten_Math_Will_Change_Dramatically_Leonardo_de_Moura_en.txt
Video: https://www.youtube.com/watch?v=KzdYKeAqWhY

[L1067] [47:08.32] have user interface. You have LSP. You
[L1068] [47:10.72] have build system. You have G. You have
[L1069] [47:12.72] that is so vast. I mean that's
[L1070] [47:18.40] another challenging part for me as I
[L1071] [47:22.00] mentioned Z3 was a back end.
[L1072] [47:24.80] The Z3 users
[L1073] [47:27.04] are very sophisticated software
[L1074] [47:30.08] developers people that speak the same
[L1075] [47:32.96] language I speak. It's way easy easier
[L1076] [47:37.20] to talk to people that speak your the
[L1077] [47:39.60] same language with L is completely
[L1078] [47:42.56] different, right? The B the first users
[L1079] [47:44.72] are all math math people. They have
[L1080] [47:48.00] completely different backgrounds,
[L1081] [47:49.36] different expectations, different
[L1082] [47:52.16] everything and a different community
[L1083] [47:55.60] and then you have people that want to
[L1084] [47:57.84] use L as a programming language. You
[L1085] [48:00.00] have I I I'm not a programming language
[L1086] [48:02.24] person. uh my background is automated
[L1087] [48:05.04] reasoning
[L1088] [48:06.64] and yeah it's different language
[L1089] [48:09.04] different expectations
[L1090] [48:11.20] >> was there like a a singular component
[L1091] [48:14.00] that was just really technically
[L1092] [48:17.52] challenging
[L1093] [48:18.40] >> I I told you that l implemented in ling
[L1094] [48:21.84] of course it was not always like that
[L1095] [48:24.64] right I mean it had to be implemented in
[L1096] [48:27.76] something else at the beginning the
[L1097] [48:30.08] switch from origin origally was C++.
[L1098] [48:35.44] The switch from CC C++ to lean was
[L1099] [48:38.80] extremely painful. Really really uh I
[L1100] [48:43.28] remember I literally want to cry when
[L1101] [48:46.72] when I managed to compile Ling. I was
[L1102] [48:49.76] just uh Sebastian and I at the time were
[L1103] [48:53.68] building L for together
[L1104] [48:56.64] and but this was before we had a
[L1105] [48:58.48] nonprofit for Ling. I remember calling
[L1106] [49:01.76] him and I said, "Wow, man. This is
[L1107] [49:05.28] insane."
[L1108] [49:06.80] Say, "Are you not excited?" He said, he
[L1109] [49:08.72] said, "Yes, I am. I am." I mean, super
[L1110] [49:11.28] excited. [laughter]
[L1111] [49:13.12] >> What What made that switch uh hard?
[L1112] [49:16.88] >> The first thing is is imagine you're
[L1113] [49:20.24] going to implement the language in
[L1114] [49:21.76] itself. The first thing you want is to
[L1115] [49:23.76] reduce to minimize number of features as
[L1116] [49:26.40] much as possible. So you want to
[L1117] [49:28.56] implement ling using barebones
[L1118] [49:31.68] features because you're going to have to
[L1119] [49:33.44] be able to compile it with itself.
[L1120] [49:36.48] uh uh then now you have like 100,000
[L1121] [49:40.96] lines more or less uh I don't know the
[L1122] [49:44.56] exact number but was between 100 around
[L1123] [49:47.20] 100,000 lines and you start trying
[L1124] [49:50.96] compile you fail the first you cannot
[L1125] [49:53.68] even compile the first file in the
[L1126] [49:55.44] pipeline that that more than 1,000 and
[L1127] [49:58.32] the first one fails then you fix the bug
[L1128] [50:00.88] you can compile the first one then you
[L1129] [50:03.76] can compile the second and you keep
[L1130] [50:06.16] moving and you're always finding
[L1131] [50:08.40] discrepancies between the new and the
[L1132] [50:11.68] old one. I mean and you're trying to
[L1133] [50:14.32] reconcile make things easier for the new
[L1134] [50:17.60] one.
[L1135] [50:18.48] because you want to replace the old one
[L1136] [50:20.88] and this process
[L1137] [50:24.88] is pain and l is a complicated language
[L1138] [50:26.88] because of these dependence types and so
[L1139] [50:28.80] on the proofs
[L1140] [50:31.28] for example
[L1141] [50:33.92] when you're implementing ling you you
[L1142] [50:35.60] still need some proofs there I mean
[L1143] [50:38.32] there are some basic proofs you need but
[L1144] [50:41.60] you have to construct these proofs
[L1145] [50:43.20] without no interactivity nothing bare
[L1146] [50:46.08] bones you have to provide the proof
[L1147] [50:47.76] time. It's almost like programming in
[L1148] [50:50.40] assembly. The proof uh this was also
[L1149] [50:53.68] super painful. I mean, my god.
[L1150] [50:56.24] >> Yeah. [laughter]
[L1151] [50:57.36] But it took Yeah. Many people thought we
[L1152] [51:01.36] we were going to fail. Sebastian and I
[L1153] [51:03.28] would not be able to do it.
[L1154] [51:05.44] >> 100,000 lines is a lot. Like all human
[L1155] [51:07.68] written.
[L1156] [51:08.16] >> Yes. All human written. Yeah.
[L1157] [51:10.40] >> We talked a lot about lean and I know
[L1158] [51:12.80] there's competitors to lean. What are
[L1159] [51:15.20] the pros and cons of the different proof
[L1160] [51:17.68] assistants? You know, in what scenarios
[L1161] [51:20.96] is one preferred over the others? For
[L1162] [51:23.36] instance, the first disclaimer, I'm a
[L1163] [51:25.52] completely biased person here, right?
[L1164] [51:28.08] But I can tell you what users tell me. I
[L1165] [51:31.04] mean about for example one thing the
[L1166] [51:33.36] users love is the fact as l is super
[L1167] [51:36.56] extensible because l implemented in ling
[L1168] [51:40.24] you can add extensions to imagine you're
[L1169] [51:43.52] doing your math proof in the middle of
[L1170] [51:45.84] this math proof and say oh I want this
[L1171] [51:47.76] fancy automation here you can write in
[L1172] [51:49.92] the same file or the AI can write for
[L1173] [51:53.12] you the extension for automating a proof
[L1174] [51:57.28] and it will do it I mean even the AI is
[L1175] [52:00.72] they know about the the fact L is
[L1176] [52:03.44] extensible.
[L1177] [52:05.28] If I ask the AI to isolate an issue in
[L1178] [52:09.12] ling, I give the AI a link file, it will
[L1179] [52:13.12] start writing a ling meta program, a
[L1180] [52:16.00] program about the link tunnels to
[L1181] [52:18.96] validate the conjecture it has about why
[L1182] [52:22.56] it doesn't work. It's crazy. I mean the
[L1183] [52:26.08] I keeps writing link meta extension
[L1184] [52:28.32] there. The fact that L extension is
[L1185] [52:31.12] really popular with so many people for
[L1186] [52:33.52] example there is Patrick Masur he's a
[L1187] [52:37.20] French mathematician
[L1188] [52:40.88] uh he wrote something called Labos
[L1189] [52:44.24] Labose you can he uses for teaching we
[L1190] [52:48.00] have this language for writing the
[L1191] [52:50.16] proofs but he made the language look
[L1192] [52:52.80] like English and he has the info view
[L1193] [52:56.48] now is a point and click you can click
[L1194] [52:58.32] there it gives you suggestions about the
[L1195] [53:00.48] next move that's written in structured
[L1196] [53:04.32] English like you find in a textbook. You
[L1197] [53:07.36] see the the the student has a really
[L1198] [53:10.48] good idea on how to write in formal math
[L1199] [53:13.20] proof and he did that without asking me
[L1200] [53:16.56] any questions and he all this stuff the
[L1201] [53:18.96] point and click the the new language the
[L1202] [53:22.48] new interactivity he did all by himself.
[L1203] [53:25.52] He's not a computer scientist. He he's
[L1204] [53:28.16] has a math degree and he did all this
[L1205] [53:30.88] stuff and it's for English and French. I
[L1206] [53:33.52] mean you can choose I mean you can write
[L1207] [53:36.32] the proofs in French
[L1208] [53:38.64] uh and looks a textbook proof. I mean uh
[L1209] [53:42.16] uh the people that write visualizations
[L1210] [53:45.04] right for you want to visual you're
[L1211] [53:47.92] trying to prove something about a math
[L1212] [53:49.60] object you can write extension that
[L1213] [53:52.56] visualize these objects in your info
[L1214] [53:55.12] view right [snorts] that people that
[L1215] [53:57.60] write new domain specific languages
[L1216] [54:00.40] embedded in link for different purposes
[L1217] [54:02.64] for example for protocol verification
[L1218] [54:05.52] there's a language called veil is a link
[L1219] [54:08.88] you open veil you feel like it's a
[L1220] [54:10.56] different system for protocol
[L1221] [54:12.00] verification, but it's just a link file
[L1222] [54:15.60] with these extensions for protocol
[L1223] [54:17.52] verification. The language for this
[L1224] [54:20.48] writing protocol is a very convenient
[L1225] [54:22.80] way.
[L1226] [54:25.36] These folks wrote the whole thing
[L1227] [54:27.44] without ever talking to us. They only
[L1228] [54:30.48] talked to us after they had done it said
[L1229] [54:33.36] look I want this pass of link to be
[L1230] [54:35.04] faster. That's was the only interaction
[L1231] [54:37.28] we had. uh and so interactivity is a big
[L1232] [54:40.64] deal.
[L1233] [54:42.32] Uh another big deal now is the
[L1234] [54:44.48] mathematical library uh is vast. I mean
[L1235] [54:48.16] for stating problems open conjectures
[L1236] [54:51.92] you need a library to with the concept
[L1237] [54:54.48] to even state the problem right. So le
[L1238] [54:57.44] has a massive library and a massive
[L1239] [55:00.64] community.
[L1240] [55:02.16] Uh the community also plays a big role.
[L1241] [55:05.84] people uh before AI I think now most
[L1242] [55:08.56] people ask questions about link to AI
[L1243] [55:10.80] but in the past people would go to the
[L1244] [55:12.88] lens lip channel
[L1245] [55:15.12] ask a question about ling they would get
[L1246] [55:16.96] an answer in five minutes I mean people
[L1247] [55:19.76] would say human based AI I mean people
[L1248] [55:22.64] would be writing answers instantaneously
[L1249] [55:25.52] to your problems the community played a
[L1250] [55:28.40] big role another one was
[L1251] [55:32.96] we listen to to to our users I mean uh
[L1252] [55:37.68] uh the math I mean if you talk for
[L1253] [55:40.00] example Jeremat was the first user I
[L1254] [55:43.76] mean he has math backgrounds
[L1255] [55:47.84] he he you ask him look he said look I
[L1256] [55:52.48] could ask anything any new feature I
[L1257] [55:55.60] would get back the same day I mean this
[L1258] [55:58.16] the fix the new feature the same day and
[L1259] [56:01.60] this attracts people right I mean
[L1260] [56:03.36] because you are making improvements
[L1261] [56:04.80] making sure the system does what they
[L1262] [56:07.76] once uh uh they come back for more. I
[L1263] [56:11.28] mean uh this also has a huge impact in
[L1264] [56:15.04] growing the community. when I was doing
[L1265] [56:17.76] some research there was this idea I
[L1266] [56:19.36] think you mentioned in this conversation
[L1267] [56:20.64] too there's this uh dependent type yes
[L1268] [56:24.64] >> proof assistance and then there's higher
[L1269] [56:26.56] order logic what what is that difference
[L1270] [56:28.88] there
[L1271] [56:29.84] >> at the beginning uh when I start I won't
[L1272] [56:32.56] choose high order logic because it's
[L1273] [56:35.04] much [snorts] easier to implement I mean
[L1274] [56:37.92] uh the pen types is way harder there
[L1275] [56:41.84] uh
[L1276] [56:43.44] but the math community I mean Jeremy is
[L1277] [56:46.32] the one that convinced me that I would
[L1278] [56:48.56] never be able to attract serious
[L1279] [56:51.12] mathematicians like fields medal level
[L1280] [56:53.52] math people with high order logic.
[L1281] [56:56.32] Right? His his point is like how logic
[L1282] [56:59.12] is good for concrete math but if you
[L1283] [57:02.08] want to talk about abstract objects
[L1284] [57:05.28] uh dependent type theory is way more
[L1285] [57:07.76] powerful and is beautiful is easy to
[L1286] [57:11.12] explain why is called dependent. For
[L1287] [57:13.60] example, you can have a structure in
[L1288] [57:15.84] ling when you have several fields like x
[L1289] [57:18.64] and y are natural numbers or integers.
[L1290] [57:20.88] Let's say they're integers.
[L1291] [57:23.36] You can have another field. The type of
[L1292] [57:25.84] the field is a proof that x greater than
[L1293] [57:28.64] y. The type of this field is x let's
[L1294] [57:32.48] call greater
[L1295] [57:34.48] column. You say x greater than y. The
[L1296] [57:37.04] type depends on the value of the
[L1297] [57:39.76] previous fields. That's why it's called
[L1298] [57:41.84] dependence type theory. You can have
[L1299] [57:43.92] types that depends on the values of
[L1300] [57:46.32] other parameters, other fields and so
[L1301] [57:49.60] on. But the beautiful thing about that
[L1302] [57:53.52] that's in this you have this very small
[L1303] [57:56.88] language that is so expressive
[L1304] [57:59.84] for example this fields now that's a
[L1305] [58:02.48] proof [snorts] you you have to provide a
[L1306] [58:04.96] proof you can view it as invariance I
[L1307] [58:07.20] can only build elements of this type if
[L1308] [58:12.48] I give the x and y like in other
[L1309] [58:14.40] programming languages but I have to give
[L1310] [58:16.08] a proof that the x is greater than y is
[L1311] [58:19.44] impossible ble to construct elements
[L1312] [58:21.92] without providing this evidence, right?
[L1313] [58:25.36] Uh you can do this in variance that's
[L1314] [58:28.56] you don't have to invent invariants,
[L1315] [58:30.48] right? the language just the fact you
[L1316] [58:32.32] have these dependencies you can express
[L1317] [58:35.92] uh in the functions you can have a
[L1318] [58:38.40] function for example that says takes a x
[L1319] [58:41.52] a y and a proof that's y is different
[L1320] [58:43.84] from zero right I mean it's impossible
[L1321] [58:47.60] to call the function if you do not
[L1322] [58:49.36] provide evidence that y is different
[L1323] [58:51.60] from zero this was always cool but in
[L1324] [58:55.12] the past people would say wow providing
[L1325] [58:57.20] this proofs is really annoying but with
[L1326] [58:59.92] AI Now the I can synthesize the proofs
[L1327] [59:02.56] for you. Uh and it's really cool.
[L1328] [59:07.28] >> In higher order logic though could you
[L1329] [59:09.28] express the same?
[L1330] [59:10.56] >> No no that's you cannot you don't have
[L1331] [59:12.56] the you lose the dependencies. For
[L1332] [59:14.56] example one thing that you cannot do in
[L1333] [59:16.16] high order logic. Uh in l
[L1334] [59:20.72] in serious math people you have a bunch
[L1335] [59:24.40] of structures they manipulate. you have
[L1336] [59:27.20] like something a field I mean a ring a
[L1337] [59:30.72] group
[L1338] [59:32.96] you can write a function in ling that
[L1339] [59:35.28] takes a group and he turns a new group a
[L1340] [59:39.44] new structure
[L1341] [59:42.16] you're not man you don't really care
[L1342] [59:44.08] about the elements of the structure you
[L1343] [59:45.68] are viewing the structure as a first
[L1344] [59:47.52] class citizen that's something that the
[L1345] [59:50.16] penet can do easily and in order logic
[L1346] [59:53.76] is you have to play in coding tricks is
[L1347] [59:56.88] a mess. I mean, uh, some people say,
[L1348] [01:00:00.64] "Oh, it works for math." None of the
[L1349] [01:00:02.96] mathematicians agree with this
[L1350] [01:00:04.72] statement. None. I mean, you talk to to
[L1351] [01:00:08.40] terish,
[L1352] [01:00:11.36] Jerem,
[L1353] [01:00:12.88] Kevin Buzzard, Patrick Masu, they would
[L1354] [01:00:15.36] say, "No, no, you have to do the pens
[L1355] [01:00:17.68] type theory." I mean,
[L1356] [01:00:22.00] that's another example for me that
[L1357] [01:00:23.68] listening to your users is important. If
[L1358] [01:00:25.84] you want to appeal to this community,
[L1359] [01:00:27.68] it's totally okay to say I don't care
[L1360] [01:00:30.96] about this community. But if you care,
[L1361] [01:00:33.44] listening to what they really want is
[L1362] [01:00:35.68] importance.
[L1363] [01:00:37.36] >> So when we think about the the future of
[L1364] [01:00:40.00] lean, I'm curious to hear your thoughts
[L1365] [01:00:42.64] on where you think lean is going. Um
[L1366] [01:00:46.32] things you're excited about in the
[L1367] [01:00:47.76] future. You know, what might it look
[L1368] [01:00:50.08] like in in a few years?
[L1369] [01:00:51.84] >> Yeah. Yeah. One thing uh we have this
[L1370] [01:00:55.36] nonprofit behind LIN since 2023.
[L1371] [01:00:59.12] I mean L 13 years old uh the first 10
[L1372] [01:01:03.04] years was
[L1373] [01:01:05.36] such project right I mean only when we
[L1374] [01:01:08.40] got the nonprofits behind ling that it
[L1375] [01:01:11.76] became you can view as a product we have
[L1376] [01:01:14.00] a team of engineers
[L1377] [01:01:16.56] and we managed to do it because the
[L1378] [01:01:19.28] impact on math right but Sebastian and I
[L1379] [01:01:23.36] I mean we co-ounded this nonprofit what
[L1380] [01:01:25.84] we are really excited about is le as
[L1381] [01:01:28.72] programming language, a programming
[L1382] [01:01:29.84] language where you can prove things
[L1383] [01:01:31.68] about your programs, right? And that's a
[L1384] [01:01:34.64] direction we are pushing really hard,
[L1385] [01:01:36.96] right? Link to uh uh we are super
[L1386] [01:01:40.72] grateful for AWS,
[L1387] [01:01:43.28] Amazon, they they're making the largest
[L1388] [01:01:46.40] donation so far to these nonprofits
[L1389] [01:01:49.20] where the goal is to accelerate this
[L1390] [01:01:52.32] path. I mean, LIN is doing super well in
[L1391] [01:01:54.32] the math path, but let's make Ling as a
[L1392] [01:01:56.72] programming language. lings a system for
[L1393] [01:01:59.36] social verification, harder
[L1394] [01:02:01.12] verification. Let's push to the extreme.
[L1395] [01:02:04.64] Let's give some love to these people uh
[L1396] [01:02:07.92] uh to this path that's right now we do
[L1397] [01:02:10.24] not really have funing to push seriously
[L1398] [01:02:12.88] this path. That's the nonprofits, right?
[L1399] [01:02:16.64] Uh for me to be in a world where you can
[L1400] [01:02:20.56] reason about your codes uh uh is part of
[L1401] [01:02:23.04] my life. They I'm not writing testes
[L1402] [01:02:25.84] anymore. I'm writing properties and
[L1403] [01:02:29.44] proving them. The AI is proving most of
[L1404] [01:02:32.40] them for me. Uh this is direction we are
[L1405] [01:02:36.32] pushing hard. And one people one thing
[L1406] [01:02:39.44] that people don't realize is that when
[L1407] [01:02:41.92] you have proofs it enables optimizations
[L1408] [01:02:45.60] for free. You can ask the for example
[L1409] [01:02:48.00] today if you ask the AI to optimize you
[L1410] [01:02:50.88] have to inspect the code to make sure no
[L1411] [01:02:53.52] bugs were introduced in the process.
[L1412] [01:02:56.72] But
[L1413] [01:02:58.24] if the AI is telling you, look, I
[L1414] [01:03:00.64] optimize it. It still computes the same
[L1415] [01:03:02.80] thing. Here's the proof.
[L1416] [01:03:05.60] Uh this is a game changer in my points
[L1417] [01:03:09.12] of view.
[L1418] [01:03:10.72] >> Yeah, I've heard multiple people say
[L1419] [01:03:13.60] this decade will be the you the decade
[L1420] [01:03:16.48] of formal verification of software and
[L1421] [01:03:19.28] yeah, maybe, you know, lean will be a
[L1422] [01:03:21.92] huge part of that.
[L1423] [01:03:23.68] >> Yeah. Yeah. We we for sure we're super
[L1424] [01:03:26.24] excited to make it happen. I mean uh we
