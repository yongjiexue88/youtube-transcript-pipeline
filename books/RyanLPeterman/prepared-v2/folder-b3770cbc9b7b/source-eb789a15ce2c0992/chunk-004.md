Chunk 4; segments 1106–1490. Start may repeat the previous chunk for context.

# Creator of Lua: What People Get Wrong About Scripting Languages | Roberto Ierusalimschy

Source ID: source-eb789a15ce2c0992
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lua_What_People_Get_Wrong_About_Scripting_Languages_Roberto_Ierusalimschy_en.txt
Video: https://www.youtube.com/watch?v=jCZnFKk6M9A

[L1115] [47:46.92] the original address. So
[L1116] [47:50.16] C doesn't have index indexing. So when
[L1117] [47:53.40] you say A is index by zero, it doesn't
[L1118] [47:56.24] index by zero because it doesn't index
[L1119] [47:58.44] by anything. But it it have this
[L1120] [48:01.00] illusion of indexing and then it's easy
[L1121] [48:03.96] to think that it
[L1122] [48:05.36] And then a lot of language that do not
[L1123] [48:07.52] use pointer arithmetic do not have this
[L1124] [48:10.28] restriction, do not have this semantics,
[L1125] [48:13.16] copy it C and kept the the zero indexing
[L1126] [48:17.92] as the thing. If you got a 12-year-old
[L1127] [48:21.16] and try to explain to them
[L1128] [48:24.12] the zero indexing,
[L1129] [48:26.12] I I assure it's much much easier for
[L1130] [48:29.04] them
[L1131] [48:30.16] to write, "Oh, I I have a list of the
[L1132] [48:32.88] first element." I always joke that is
[L1133] [48:35.00] the first element is zero. And you write
[L1134] [48:38.80] first you for one, but the first element
[L1135] [48:41.84] one
[L1136] [48:42.92] is not one, is zero.
[L1137] [48:45.84] So,
[L1138] [48:46.80] it has advantages zero for this first
[L1139] [48:49.48] some specific operators mathematically.
[L1140] [48:53.12] For instance, you want to do a circular
[L1141] [48:55.28] buffer, zero is better. There are some
[L1142] [48:58.40] small advantage, but it's much much more
[L1143] [49:01.84] confusing.
[L1144] [49:03.16] And as mIRC has this idea of end user
[L1145] [49:05.88] programming,
[L1146] [49:07.40] we always joke it's much easier to make
[L1147] [49:09.64] life easier for the non-programmers.
[L1148] [49:14.12] And I am sure that programmers can
[L1149] [49:18.44] program whatever index they have to do
[L1150] [49:21.00] because they are supposedly they are
[L1151] [49:23.04] professional. They can learn that all
[L1152] [49:26.12] indexing is from them to put all the end
[L1153] [49:30.00] user the burden and of using something
[L1154] [49:32.84] completely different from them indexing
[L1155] [49:35.20] by zero. What does it mean the element
[L1156] [49:37.48] index zero? They never saw and oh, are
[L1157] [49:40.24] the chapters in the book? Yes, the first
[L1158] [49:42.04] chapter is at zero, the second chapter
[L1159] [49:44.56] is at one. It
[L1160] [49:46.24] No, I'm not joking. When you try to
[L1161] [49:48.04] explain that to non-programmer, even
[L1162] [49:50.28] though
[L1163] [49:51.20] they don't need to be 12
[L1164] [49:53.60] I mean, just get anyone that is not
[L1165] [49:56.48] an internet programmer think, "Oh, I
[L1166] [49:58.24] have the absolute I mean, but they are
[L1167] [50:00.28] grown-up. You are
[L1168] [50:02.28] I mean, okay, you are a Christian. You
[L1169] [50:04.84] are
[L1170] [50:05.96] If zero and sure you can learn through
[L1171] [50:08.24] truth to program if one or minus one or
[L1172] [50:11.72] whatever it is the the base you have to
[L1173] [50:14.48] use them. Sure.
[L1174] [50:16.16] >> But do you think you see a lot of bugs
[L1175] [50:19.04] cuz um
[L1176] [50:20.52] maybe someone thinks it's zero.
[L1177] [50:22.52] >> Unfortunately, I see some bugs.
[L1178] [50:25.96] But as I always say, that's are the kind
[L1179] [50:28.40] of bugs that
[L1180] [50:30.76] just shows that you will be then do
[L1181] [50:34.32] minimum testing.
[L1182] [50:36.60] Because that kind of bug is not a kind
[L1183] [50:39.24] of that kind of bug that always you
[L1184] [50:43.12] try to anything you try to do
[L1185] [50:46.40] in a the way.
[L1186] [50:48.56] If you
[L1187] [50:49.52] start from zero or start from one, you
[L1188] [50:52.36] have a bug.
[L1189] [50:53.64] So, the the most simple test that you
[L1190] [50:56.60] can imagine to test anything related to
[L1191] [51:00.48] an array, to a list, etc. And if you if
[L1192] [51:03.24] you
[L1193] [51:04.12] mistake zero to one, you you detect
[L1194] [51:07.60] that. So, if you
[L1195] [51:09.84] have that kind of bug, it just shows
[L1196] [51:12.20] that you didn't
[L1197] [51:14.76] test that code at all.
[L1198] [51:17.40] >> There was this talk that you gave on the
[L1199] [51:19.28] cost of adding uh
[L1200] [51:21.32] language features to Lua and how there's
[L1201] [51:23.56] a lot of hidden costs. And I think it
[L1202] [51:26.36] today
[L1203] [51:27.72] um implementation cost of software is
[L1204] [51:29.96] going down due to, you know, AI code
[L1205] [51:32.76] generation or LLMs.
[L1206] [51:35.24] And I was wondering if that changes your
[L1207] [51:36.88] thinking on
[L1208] [51:38.52] um I guess the cost of adding features
[L1209] [51:41.04] to a programming language.
[L1210] [51:43.44] >> AI is something that
[L1211] [51:45.92] we don't really know what is going to
[L1212] [51:49.16] happen. If you go to an extreme
[L1213] [51:53.00] it's com- completely feasible
[L1214] [51:56.84] that we
[L1215] [51:58.12] we won't have programming languages. And
[L1216] [52:00.72] I mean
[L1217] [52:01.88] because if you did the AI is writing all
[L1218] [52:05.00] your code and is checking all your code
[L1219] [52:07.20] and doing everything, in a few years
[L1220] [52:09.92] maybe we don't need programming. AI can
[L1221] [52:12.00] write machine code directly, it doesn't
[L1222] [52:14.00] need programming languages. It
[L1223] [52:17.08] It's easier for for them to compile or
[L1224] [52:19.64] even generate the code directly. I mean,
[L1225] [52:22.00] I don't know what is going to happen in
[L1226] [52:23.84] a few years. So,
[L1227] [52:27.12] I
[L1228] [52:28.00] think it's very hard for me to
[L1229] [52:31.60] talk anything about AI because I have
[L1230] [52:35.04] and I think nobody have a clear idea
[L1231] [52:38.24] what I mean, people have a maybe a clear
[L1232] [52:41.28] idea what it happens in 1 year or 2
[L1233] [52:43.96] years, but in 5 years, I I mean, anyone
[L1234] [52:47.60] that says, "Oh, that's going to happen
[L1235] [52:49.48] in 5 years." It's just
[L1236] [52:51.68] I mean,
[L1237] [52:52.80] it's
[L1238] [52:53.56] just guess.
[L1239] [52:54.96] So,
[L1240] [52:56.32] I I think it's hard to to say anything.
[L1241] [52:59.72] This is all because of AI. So,
[L1242] [53:03.60] keeping the meaning thing, I mean, that
[L1243] [53:06.00] is still have the for instance the Oh,
[L1244] [53:07.88] why you still use programming languages?
[L1245] [53:10.44] Because if you want the the user or the
[L1246] [53:13.76] some
[L1247] [53:14.92] human to be able to check the result of
[L1248] [53:18.08] what the AI is doing etc. So, I still
[L1249] [53:21.96] think that most of the things about
[L1250] [53:24.80] programming language still hold. For
[L1251] [53:27.20] instance, the the the cost of complexity
[L1252] [53:29.72] of you understanding I mean, AI create a
[L1253] [53:32.48] code for you and then you really
[L1254] [53:34.64] understanding what that code does. I
[L1255] [53:37.32] mean, it's even worse. I mean, it's much
[L1256] [53:39.60] more important that the language should
[L1257] [53:42.56] be clear and and has a
[L1258] [53:46.20] not no hidden mechanisms because they I
[L1259] [53:50.76] may use a hidden mechanism it doesn't
[L1260] [53:52.88] have the concept oh that will be
[L1261] [53:54.68] difficult for a human to understand that
[L1262] [53:57.68] what is really happening here is is
[L1263] [54:00.52] something it's a something that for
[L1264] [54:02.04] instance oh I can use that but I'm for
[L1265] [54:04.48] sure it's going to put a comment here
[L1266] [54:07.24] because I'm sure that someone that reads
[L1267] [54:09.48] that in 1 month it's not going to
[L1268] [54:12.28] understand.
[L1269] [54:14.12] AI doesn't have that kind of
[L1270] [54:16.60] of
[L1271] [54:17.56] of thinking and so it just use that that
[L1272] [54:20.56] trick or that thing and it's so I think
[L1273] [54:24.12] the AI if you think about this idea of
[L1274] [54:26.64] AI generating code I think it's even
[L1275] [54:28.92] more important for the language to be
[L1276] [54:31.04] simple to be understandable for you to
[L1277] [54:34.36] be able to really understand that the
[L1278] [54:36.56] code that you are seeing does what you
[L1279] [54:39.32] think it should it should do it it
[L1280] [54:41.72] really understand what the code is
[L1281] [54:44.04] doing. So this thing about simplicity I
[L1282] [54:47.36] think it's it's very important. And
[L1283] [54:50.76] I think
[L1284] [54:52.28] the other part from the need maybe I may
[L1285] [54:55.20] facilitate documentation I'm not sure if
[L1286] [54:58.32] I need this thing about conceptual
[L1287] [55:00.80] integrity for instance to keep things oh
[L1288] [55:03.68] that makes sense etc. I really think
[L1289] [55:06.76] that one of the main costs is that it
[L1290] [55:09.40] it's the the the burden you put on the
[L1291] [55:11.68] user to learn
[L1292] [55:14.08] one more thing about it
[L1293] [55:16.20] your language.
[L1294] [55:17.64] So there's the other possibility I have
[L1295] [55:20.24] said that implementation is the that is
[L1296] [55:23.00] the the the part that AI can really
[L1297] [55:25.84] help you.
[L1298] [55:27.76] It's not a really re-
[L1299] [55:31.20] really important cost.
[L1300] [55:32.88] >> If you think about like a spectrum of
[L1301] [55:34.84] simple to complex, what programming
[L1302] [55:37.64] languages are, you know, the most simple
[L1303] [55:40.28] ones that you think of that are easy to
[L1304] [55:42.16] understand, less confusing side effects,
[L1305] [55:45.08] and what programming languages are the
[L1306] [55:47.20] most complex and have the most foot
[L1307] [55:49.40] guns?
[L1308] [55:50.40] >> This this famous quote comes from, I
[L1309] [55:53.36] don't know from whom, that the simplest
[L1310] [55:57.52] possible, but not simpler than that.
[L1311] [56:00.88] Because you see, if you go to the
[L1312] [56:02.40] extreme of simplicity, you could get for
[L1313] [56:05.84] instance lambda calculus or Turing
[L1314] [56:08.00] machines and say, "Oh, that's really
[L1315] [56:10.48] simple." I mean, this is really simple,
[L1316] [56:12.92] but it's completely impossible to to
[L1317] [56:15.56] write any program in that. I mean, if
[L1318] [56:18.08] you have really simple stuff, I think
[L1319] [56:20.64] the extremes would be like that, but you
[L1320] [56:23.08] don't want to be there. But for the
[L1321] [56:25.28] other side,
[L1322] [56:26.60] I think C++ I think is a good example of
[L1323] [56:29.52] a language that I think it's really
[L1324] [56:31.72] really complex.
[L1325] [56:33.44] >> A question that comes up a lot is
[L1326] [56:35.92] given how much AI has been progressing,
[L1327] [56:38.72] you know, would you still recommend
[L1328] [56:40.08] people learn computer science today?
[L1329] [56:43.52] >> If you really think about that, it's
[L1330] [56:45.84] really difficult to recommend people
[L1331] [56:47.68] learning anything
[L1332] [56:49.52] for a profession. I mean, we have no
[L1333] [56:51.92] idea what AI will do in 5 years. If
[L1334] [56:55.20] someone is entering university now, they
[L1335] [56:58.16] are going to graduate in 4 years, 5
[L1336] [57:00.60] years, or
[L1337] [57:02.40] I think maybe three three and a half
[L1338] [57:05.04] years or
[L1339] [57:06.16] then
[L1340] [57:07.32] nobody have
[L1341] [57:08.88] any idea what it's what the world is the
[L1342] [57:13.08] your profession will be like in in 4
[L1343] [57:15.92] years from now. So, it's really hard to
[L1344] [57:18.52] I mean to say, "Oh, yes, you can you
[L1345] [57:20.92] still going to have me." Because now
[L1346] [57:22.48] people say, "Oh, no." The the the
[L1347] [57:26.40] manual tasks, the AI is very good, but
[L1348] [57:29.08] it's you needed the the whole
[L1349] [57:30.76] architecture, you needed the
[L1350] [57:33.12] like a software engineer to do to
[L1351] [57:35.80] see the big picture, etc. That it's now,
[L1352] [57:38.56] but it you have no idea that that will
[L1353] [57:41.20] be true in 4 years and or 5 years. So, I
[L1354] [57:45.60] think I mean I like I enjoy programming.
[L1355] [57:49.24] I I could do I mean some people say,
[L1356] [57:51.28] "Oh, use the AI for that." I mean I
[L1357] [57:52.96] program because I like that. But exactly
[L1358] [57:55.52] but so if choose something that you
[L1359] [57:57.84] like, but really for if you are really
[L1360] [58:00.04] thinking about how am I going to live
[L1361] [58:02.36] with that? I have no idea it's really I
[L1362] [58:05.60] think it's a really
[L1363] [58:08.52] hard time to
[L1364] [58:11.52] to be choosing a profession.
[L1365] [58:13.84] >> Yeah, I mean you've worked on Lua for
[L1366] [58:15.64] such a long time. When you look back on
[L1367] [58:17.96] it, what went well and what didn't go
[L1368] [58:21.24] well?
[L1369] [58:22.32] >> We had this privilege
[L1370] [58:24.56] of
[L1371] [58:25.64] not having to satisfy clients.
[L1372] [58:29.08] So, we are the we don't have as I said
[L1373] [58:31.16] for instance, you can choose to add some
[L1374] [58:33.08] feature to the language because you do
[L1375] [58:34.80] not have a pressure, "Oh, we need that
[L1376] [58:36.84] feature that feature whatever it takes
[L1377] [58:40.24] or etc." So, we have this privilege of,
[L1378] [58:43.44] "Oh, we are not sure whether to put
[L1379] [58:45.48] that, we don't put that, we can wait 1
[L1380] [58:47.56] year or so." I think that it's it's much
[L1381] [58:50.40] easier to do a
[L1382] [58:52.80] a good project, a beautiful project. So,
[L1383] [58:55.92] I'm not I'm not sure this is a
[L1384] [58:57.52] recommendation.
[L1385] [58:59.20] Try to work with
[L1386] [59:01.16] without much pressure.
[L1387] [59:03.16] People usually do not have
[L1388] [59:05.36] this choice.
[L1389] [59:07.24] >> What was your measure of success if
[L1390] [59:09.76] you're working on a programming
[L1391] [59:11.00] language? Like,
[L1392] [59:12.36] you know, how did you know it was good?
[L1393] [59:14.72] >> It's more important to receive sometimes
[L1394] [59:17.44] that good people that I recognize that
[L1395] [59:21.24] as we like the the result than a lot of
[L1396] [59:25.20] people that I have no idea what they who
[L1397] [59:28.92] they are etc. Like so I I
[L1398] [59:31.60] I think this metric of quantity that is
[L1399] [59:34.24] the standard metric nowadays in
[L1400] [59:37.44] in the web it's got much worse that
[L1401] [59:39.84] everything is just in the number of
[L1402] [59:41.52] followers that me doesn't care who is
[L1403] [59:44.36] following you just as as many people as
[L1404] [59:47.16] possible. So sometimes for me it's much
[L1405] [59:49.52] more important if someone that I really
[L1406] [59:51.96] admire of thing all this that say
[L1407] [59:55.04] something good about Lua than oh we have
[L1408] [59:57.68] that many
[L1409] [01:00:00.24] But of course it's good also to have
[L1410] [01:00:02.56] some number of users and to be
[L1411] [01:00:04.40] recognized but I think it says a balance
[L1412] [01:00:08.44] between all of this.
[L1413] [01:00:10.28] >> Do you recommend people study other
[L1414] [01:00:11.96] programming languages to get better at
[L1415] [01:00:14.24] programming? And so question is you know
[L1416] [01:00:17.40] what are the top three programming
[L1417] [01:00:19.12] languages that you think every engineer
[L1418] [01:00:21.52] should learn in 2026 to kind of become
[L1419] [01:00:24.92] better at programming?
[L1420] [01:00:26.96] >> Haskell
[L1421] [01:00:28.68] I think it's a
[L1422] [01:00:31.12] it's an incredible language that it has
[L1423] [01:00:33.64] everything you need to
[L1424] [01:00:35.44] really learn about functional
[L1425] [01:00:37.84] programming.
[L1426] [01:00:39.76] I think one of the main benefits is much
[L1427] [01:00:43.52] there is a old joke
[L1428] [01:00:45.80] seen in the Haskell community that
[L1429] [01:00:50.28] if you write a program in in
[L1430] [01:00:53.32] Haskell and in C
[L1431] [01:00:56.12] in C
[L1432] [01:00:57.68] really spend one week
[L1433] [01:00:59.76] to make it efficient
[L1434] [01:01:02.24] and then you spend one year to make it
[L1435] [01:01:04.68] correct.
[L1436] [01:01:07.44] In Haskell you spend one week to make it
[L1437] [01:01:10.20] correct and then you may spend one year
[L1438] [01:01:13.12] to make it efficient.
[L1439] [01:01:15.68] Again it's not my joke but
[L1440] [01:01:18.12] I it has some truth not
[L1441] [01:01:20.84] always true etc. but I think it gives
[L1442] [01:01:23.36] the the idea. I think this is
[L1443] [01:01:26.24] maybe the the the main the most
[L1444] [01:01:28.68] important lesson of Haskell. But,
[L1445] [01:01:31.08] Haskell has many other
[L1446] [01:01:33.64] validity this thing about type
[L1447] [01:01:35.44] inference, for instance, that I mean the
[L1448] [01:01:37.36] entire language is built is
[L1449] [01:01:41.24] types are optional everywhere, and yet
[L1450] [01:01:44.52] it can do type inference for everything.
[L1451] [01:01:47.68] It can infer the types correctly, etc.
[L1452] [01:01:51.52] C or some
[L1453] [01:01:53.56] low language I mean, you can also have a
[L1454] [01:01:57.40] to learn some assembler or I mean to to
[L1455] [01:01:59.96] see you. But, assemblers now are
[L1456] [01:02:02.04] becoming too much complex. It would be
[L1457] [01:02:04.40] to learn like the
[L1458] [01:02:06.28] the 8080 assembler, very old assembler
[L1459] [01:02:09.64] of a very
[L1460] [01:02:10.88] but to have this exactly this idea of
[L1461] [01:02:13.28] what a machine does, how it does stuff
[L1462] [01:02:16.20] it exactly the basic level to have this
[L1463] [01:02:18.80] understanding.
[L1464] [01:02:20.28] Scheme is a language that I I like very
[L1465] [01:02:22.64] much because of this exactly this
[L1466] [01:02:25.32] economy of of ideas, very very few
[L1467] [01:02:29.00] concepts, and it can do some amazing
[L1468] [01:02:32.40] things with the
[L1469] [01:02:34.12] with very few concepts. The one language
[L1470] [01:02:36.96] that this is very very very old, but I
[L1471] [01:02:40.84] still think it is Snowball.
[L1472] [01:02:43.64] What was the first I think it was the
[L1473] [01:02:45.04] first languages to have pattern matching
[L1474] [01:02:47.36] and this idea of doing I mean, it's
[L1475] [01:02:50.32] really strong patterns, etc. And I think
[L1476] [01:02:54.52] it's sometimes it's interesting to see
[L1477] [01:02:57.08] old languages because exactly nowadays a
[L1478] [01:03:00.60] lot of languages tend to like I said,
[L1479] [01:03:02.64] the zero indexing that people
[L1480] [01:03:05.24] they copy a lot of they they tend to be
[L1481] [01:03:08.76] too uniform in some aspects. And so,
[L1482] [01:03:12.24] it's interesting to see some older
[L1483] [01:03:14.28] languages that have some ideas that may
[L1484] [01:03:17.72] maybe not even good ideas, but it's very
[L1485] [01:03:20.16] interesting.
[L1486] [01:03:21.44] >> Last question for you is
[L1487] [01:03:23.88] you know, knowing everything you know
[L1488] [01:03:25.08] now,
[L1489] [01:03:26.20] if you could go back to when you had
[L1490] [01:03:29.28] just started your career and give
[L1491] [01:03:31.76] yourself some advice, what would you
[L1492] [01:03:33.60] say?
[L1493] [01:03:34.76] >> To know a lot of stuff, you really have
[L1494] [01:03:36.72] to study a lot of stuff and it takes
[L1495] [01:03:39.36] time it's the
[L1496] [01:03:40.92] I I also joke about that people say,
[L1497] [01:03:43.40] "Oh, learn Lua in 30 minutes or learn
[L1498] [01:03:46.40] learn Python in 5 minutes or and I
[L1499] [01:03:50.20] always say that I wanted to
