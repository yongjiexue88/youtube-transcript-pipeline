Chunk 4; segments 1112–1490. Start may repeat the previous chunk for context.

# Dropbox’s Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling

Source ID: source-dbce948925112d65
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Dropbox’s_Former_Most_Senior_Eng_Building_Great_Systems_and_Advice_for_the_AI_Era_James_Cowling_en.txt
Video: https://www.youtube.com/watch?v=3XkmNSuHFmY

[L1121] [37:42.56] agentic development. They They're not
[L1122] [37:44.40] the best at building simple systems.
[L1123] [37:45.88] Like simplicity is still the domain of
[L1124] [37:47.88] human beings for now. But um a big focus
[L1125] [37:50.76] on simplicity. The other was um
[L1126] [37:53.76] you know, this this very thick layer of
[L1127] [37:56.24] validation checks during this migration.
[L1128] [37:58.64] And And in fact, um we had uh
[L1129] [38:02.24] when we did the migration off of S3, we
[L1130] [38:04.52] had this um something called the dark
[L1131] [38:06.12] launch where we would you know, be
[L1132] [38:07.56] moving data off of S3, but we were
[L1133] [38:09.80] keeping it in both locations. And we had
[L1134] [38:12.12] to demonstrate to the We had this kind
[L1135] [38:13.68] of contract with the Dropbox founders.
[L1136] [38:17.28] We'd have to kind of keep the system
[L1137] [38:18.92] running with no incidents,
[L1138] [38:21.12] uh no downtime, no data loss, for 6
[L1139] [38:23.24] months before we would delete any of the
[L1140] [38:25.36] data from S3. So, we have double write
[L1141] [38:27.80] it. And, um,
[L1142] [38:30.32] and there's one point in time, halfway
[L1143] [38:32.28] through this process, where there was a
[L1144] [38:33.92] a bug got through to production.
[L1145] [38:35.92] Um, and it didn't nothing bad happened
[L1146] [38:38.16] with the bug. But, it was a it was like
[L1147] [38:39.88] a,
[L1148] [38:41.36] it was it was like a a bug
[L1149] [38:43.44] slipped through our multiple layers of,
[L1150] [38:45.48] you know, release process, etc.
[L1151] [38:47.48] And, um,
[L1152] [38:48.92] so, I went to the VP and I said, "Hey,
[L1153] [38:50.64] you a bug made it through to production,
[L1154] [38:53.12] and we're going to reset the launch
[L1155] [38:55.40] clock.
[L1156] [38:56.64] And, as a result, it's going to launch
[L1157] [38:58.84] later, and it's going to cost us
[L1158] [39:01.36] some amount of money. Let's say
[L1159] [39:02.48] double-digit millions, you know?
[L1160] [39:05.36] And, they were like, "Great.
[L1161] [39:07.56] Thank you. That's good. I trust you."
[L1162] [39:09.32] And, that was that that was a cool
[L1163] [39:10.80] thing. I mean, Dropbox had a lot of
[L1164] [39:11.92] incredible cultural values. But, like,
[L1165] [39:14.04] that was like, "Okay, cool. If you're
[L1166] [39:15.72] prioritizing user safety, that's the
[L1167] [39:17.12] right thing to do." And, um, no one was
[L1168] [39:19.96] mad about that. It was almost like they
[L1169] [39:21.32] were
[L1170] [39:22.68] proud, almost. You know, it was it was
[L1171] [39:24.52] just like a it was like, "Yes, you're
[L1172] [39:26.56] you're operating, uh, in accordance to
[L1173] [39:29.00] the
[L1174] [39:29.76] principles of this company." And, yeah.
[L1175] [39:32.04] >> Okay, so, it it was double writing both
[L1176] [39:33.80] systems for a while, and then
[L1177] [39:35.08] >> For some subset of data, yeah.
[L1178] [39:36.56] >> Uh, okay. And, then you switched over
[L1179] [39:38.16] reads.
[L1180] [39:39.00] >> Once we were sure the system was
[L1181] [39:40.64] durable, and we had all these validators
[L1182] [39:42.24] running in production 24/7, uh, then we
[L1183] [39:44.80] were just migrating as fast as we could.
[L1184] [39:46.28] I think at some point we got up to 700
[L1185] [39:49.12] gigabits per second, 764 gigabits per
[L1186] [39:52.24] second of peering bandwidth between
[L1187] [39:54.24] Amazon servers and ours. Um,
[L1188] [39:57.12] certainly someone on the network team
[L1189] [39:58.60] over there noticed
[L1190] [39:59.92] that [laughter] there was that much data
[L1191] [40:01.00] moving out.
[L1192] [40:02.88] At one point, I got a a slightly nasty
[L1193] [40:05.28] email from someone saying
[L1194] [40:07.15] >> [snorts]
[L1195] [40:07.68] >> it was super weird. I think the phrase
[L1196] [40:09.56] super weird, it's like, "It's super
[L1197] [40:11.40] weird that you're doing so many reads
[L1198] [40:13.16] and not that many writes."
[L1199] [40:14.72] >> Mhm.
[L1200] [40:15.00] >> And, I didn't didn't respond to that
[L1201] [40:17.04] email. But to be fair, like Amazon was
[L1202] [40:19.76] us are a great have been a were a great
[L1203] [40:21.28] partner for Dropbox. And Dropbox still
[L1204] [40:23.04] uses AWS. They always
[L1205] [40:26.04] um
[L1206] [40:26.80] there was no concern that they would do
[L1207] [40:28.04] the wrong thing by us as a company. I
[L1208] [40:29.48] mean, like well we we only had excellent
[L1209] [40:31.88] experience with AWS. Um but yeah, there
[L1210] [40:34.56] was a it was a moment for us, you know,
[L1211] [40:36.68] it was a
[L1212] [40:38.48] it probably strained the relationship
[L1213] [40:40.28] somewhat.
[L1214] [40:41.52] >> You mentioned simplicity and
[L1215] [40:44.16] intuition-wise, it makes sense.
[L1216] [40:46.80] Do you have a concrete example though?
[L1217] [40:49.00] >> Yeah, I've got a concrete example for
[L1218] [40:50.08] you. And it it maybe it shows the
[L1219] [40:51.40] difference between academia and
[L1220] [40:53.08] industry.
[L1221] [40:54.32] Um so um
[L1222] [40:56.76] the storage system is a giant
[L1223] [40:58.56] distributed system with a files stored
[L1224] [41:01.60] in various locations. And so you need a
[L1225] [41:03.76] a mapping from from the file to where it
[L1226] [41:06.28] lives on these disks.
[L1227] [41:08.20] And so all we did was had a cluster of a
[L1228] [41:11.36] thousand MySQL nodes.
[L1229] [41:14.20] All right?
[L1230] [41:15.24] Big giant database, and it was indexed
[L1231] [41:17.76] by the block ID, and it said this block
[L1232] [41:19.92] is on these disks.
[L1233] [41:21.40] And that's a pretty
[L1234] [41:23.84] like simple, it's not sophisticated, you
[L1235] [41:26.20] know? And it And every time we'd hire
[L1236] [41:29.28] someone out of academia, or maybe from
[L1237] [41:32.36] other companies, they'd say, "Oh, this
[L1238] [41:33.52] is not very sophisticated because like
[L1239] [41:35.60] you could use a Patricia trie, or you
[L1240] [41:37.96] could use a distributed hash table, and
[L1241] [41:40.64] that would map um a block to a set of um
[L1242] [41:44.56] of of locations." And I think
[L1243] [41:48.88] that's optimizing for the wrong thing.
[L1244] [41:51.68] Because the really nice thing about
[L1245] [41:52.92] dumping a list of files and their
[L1246] [41:54.68] locations in a giant database is it's
[L1247] [41:56.84] written in one location. If I want to
[L1248] [41:59.00] validate what happened, if I want to
[L1249] [42:00.92] check all the data there is where it's
[L1250] [42:02.52] meant to be, I just walk over the table
[L1251] [42:05.12] and check. And we did. We had services
[L1252] [42:07.20] constantly walking over in the table and
[L1253] [42:08.80] checking. Whereas if it it a distributed
[L1254] [42:10.68] hash table or some giant complex data
[L1255] [42:12.56] structure, it's very hard to to
[L1256] [42:14.28] validate. So, I mean, designing for
[L1257] [42:16.84] validation is very important. Designing
[L1258] [42:18.36] for understanding is very important.
[L1259] [42:19.56] It's not about getting a system to work.
[L1260] [42:22.20] It's what do you do when it doesn't
[L1261] [42:24.12] work, right? And so, having a very
[L1262] [42:26.72] simple boundary That's That's a It's a
[L1263] [42:29.00] very basic example, you know, there's
[L1264] [42:30.44] there's more There's more sophisticated
[L1265] [42:31.96] examples that take more time to explain,
[L1266] [42:33.44] but like something like that is
[L1267] [42:36.76] a lot of engineers will feel, you know,
[L1268] [42:39.36] a lot of engineers will want to do
[L1269] [42:40.76] interesting work. Will want to advance
[L1270] [42:42.24] in their career. They They want to be
[L1271] [42:44.68] seen as a as a intellectual problem
[L1272] [42:48.36] solver.
[L1273] [42:49.64] And so, the tendency can be to design
[L1274] [42:52.68] complex systems. And my argument is
[L1275] [42:55.12] always that like
[L1276] [42:56.56] simple systems are way harder to design
[L1277] [42:59.28] than complex systems.
[L1278] [43:01.52] Like, simplicity is so hard. And I think
[L1279] [43:03.88] to like maybe the untrained eye, a
[L1280] [43:05.72] simple system can seem like obvious. And
[L1281] [43:08.76] the the And the best compliment you
[L1282] [43:10.20] could ever get about anything you design
[L1283] [43:13.00] is people say like, "Oh, isn't that the
[L1284] [43:15.04] Isn't that the obvious way of doing it?"
[L1285] [43:16.56] It's It's like the same as convex, you
[L1286] [43:18.32] know, people say, "Oh, isn't that
[L1287] [43:20.68] What's that? That's just like the
[L1288] [43:21.76] obvious way of structuring?" Like,
[L1289] [43:22.96] great. Because it wasn't obvious when we
[L1290] [43:25.04] did it. No one else was doing it, right?
[L1291] [43:26.76] Everyone thought we were idiots. If
[L1292] [43:28.52] after the fact people think it's
[L1293] [43:30.56] obvious, then you then you really nailed
[L1294] [43:32.00] it. I think um
[L1295] [43:33.72] But I think that's a um it requires a an
[L1296] [43:36.32] understanding that's that that
[L1297] [43:37.44] simplicity is is the hardest thing in
[L1298] [43:39.28] systems. And cuz simplicity is
[L1299] [43:42.12] is scalable. And I don't Yes, simplicity
[L1300] [43:44.20] is scalable in terms of numbers of
[L1301] [43:46.88] queries per second, right? But what I
[L1302] [43:48.76] really mean about scalability is you can
[L1303] [43:50.92] take a simple system
[L1304] [43:53.12] and and have it run for 5 years, and
[L1305] [43:55.64] have people work on it for 5 years, and
[L1306] [43:57.92] have all sorts of features added to it,
[L1307] [44:00.08] and have requirements changed cuz the
[L1308] [44:01.72] company realized the product didn't work
[L1309] [44:03.28] the way it wanted to work, and it wants
[L1310] [44:04.60] to change things, and it still stands
[L1311] [44:07.04] the test of time.
[L1312] [44:08.44] Whereas a complex over-optimized system
[L1313] [44:10.76] will not. And And that's the tough thing
[L1314] [44:12.80] about
[L1315] [44:13.92] distributed systems design, especially
[L1316] [44:16.48] um
[L1317] [44:17.28] LLM augmented distributed systems
[L1318] [44:19.04] design, is just because something works
[L1319] [44:22.68] doesn't mean it's maintainable over a
[L1320] [44:24.36] long period of time. Doesn't mean it's
[L1321] [44:25.56] understandable. Doesn't mean it's
[L1322] [44:26.64] cleanly up architected and abstracted.
[L1323] [44:29.28] That stuff's really very hard.
[L1324] [44:31.52] >> Absolutely. And I agree with you. I
[L1325] [44:34.12] think it's the long-term beneficial
[L1326] [44:35.80] thing to do.
[L1327] [44:37.24] One unusual thing though in the industry
[L1328] [44:39.04] that I I've seen is
[L1329] [44:41.04] the incentive system for engineers is
[L1330] [44:44.04] actually I mean, you mentioned the
[L1331] [44:45.88] desire for an engineer to want to be
[L1332] [44:48.52] seen that they can do something
[L1333] [44:50.16] difficult. There's that, but there's
[L1334] [44:51.68] also the incentive system of promotions.
[L1335] [44:54.76] And I've had many friends whose
[L1336] [44:57.04] promotions were rejected because their
[L1337] [44:59.52] work wasn't complex enough. And so that
[L1338] [45:02.12] kind of forces It's a forces complexity,
[L1339] [45:05.00] which is kind of unusual. I wanted to
[L1340] [45:07.12] know what you thought about that.
[L1341] [45:08.44] >> Yeah. It I mean, almost
[L1342] [45:11.48] angers me. I just like it so much.
[L1343] [45:14.48] Partly why I started my own company, you
[L1344] [45:16.12] know.
[L1345] [45:17.16] Um
[L1346] [45:18.16] I think
[L1347] [45:20.00] the ideal for anyone is to be doing work
[L1348] [45:23.92] where the you're being appreciated for
[L1349] [45:27.32] solving the problem. Like, you know, and
[L1350] [45:29.92] this is
[L1351] [45:31.12] if we get philosophical, this is what it
[L1352] [45:32.44] was like going back to the farming days,
[L1353] [45:34.52] right? There was no incentive to make it
[L1354] [45:36.48] really complicated to milk a cow, cuz
[L1355] [45:38.36] the goal is to like milk the cow, and
[L1356] [45:40.12] then the back The reward is you got
[L1357] [45:41.64] milk, right? And I think at a It sounds
[L1358] [45:44.20] so silly, but at a startup, that's the
[L1359] [45:46.36] same thing. The startup, the goal is to
[L1360] [45:48.20] build the system, have it work, have the
[L1361] [45:49.88] users like it, have it grow, and
[L1362] [45:52.44] everyone gets rewarded and celebrated
[L1363] [45:55.16] for solving the problem.
[L1364] [45:57.92] It gets hard to scale that. So at large
[L1365] [46:00.08] companies
[L1366] [46:01.80] the end up with so many layers of
[L1367] [46:03.96] organization that people end up building
[L1368] [46:06.60] alternative incentive structures, right?
[L1369] [46:08.72] It's like I'm so far away from whatever
[L1370] [46:11.28] the hell we're trying to do over here
[L1371] [46:12.88] that my goal now is to get all green
[L1372] [46:15.80] check marks on my OKR plan.
[L1373] [46:18.64] But who cares about your OKR plan unless
[L1374] [46:20.20] it solves the problem? And so the you
[L1375] [46:22.20] know, the thing that really drives me um
[L1376] [46:25.28] really drives me insane is when people
[L1377] [46:27.48] try to chase
[L1378] [46:29.92] um
[L1379] [46:31.20] artificial goals.
[L1380] [46:32.60] Right? And I And I understand that if
[L1381] [46:34.84] you're in a company with um like this
[L1382] [46:37.36] that you may have no choice in the
[L1383] [46:38.76] matter. But what I want to tell people
[L1384] [46:40.88] there is a better way.
[L1385] [46:43.56] And it you know, and that that better
[L1386] [46:45.64] way may not be available to you. You may
[L1387] [46:47.16] not
[L1388] [46:48.16] have job opportunities near where you
[L1389] [46:50.52] are, for example.
[L1390] [46:51.84] But if you do have the ability to go
[L1391] [46:54.40] work at a company where
[L1392] [46:57.08] like you are being appreciated for
[L1393] [46:58.68] problem solving,
[L1394] [47:00.56] that will make you so much better as an
[L1395] [47:02.36] engineer. Like And I see this when I
[L1396] [47:04.64] when I interview people, you know?
[L1397] [47:06.56] Um and I if if I, you know, do a um
[L1398] [47:09.60] I mean, everyone knows Google has
[L1399] [47:10.84] tremendous engineering and tremendous
[L1400] [47:12.28] engineers. Um a lot of
[L1401] [47:14.68] folks there though, I'm not
[L1402] [47:16.72] that interested in hiring
[L1403] [47:19.68] because
[L1404] [47:21.88] you know, if I'll do a deep dive with
[L1405] [47:23.64] them and they'll say they built a system
[L1406] [47:24.80] and I'll say, "Well, why did you build
[L1407] [47:25.72] it?" And they're like, "I don't know.
[L1408] [47:26.48] The VP told me to." And like, "Oh, how
[L1409] [47:28.92] is this system used?" And they're like,
[L1410] [47:30.00] "I
[L1411] [47:30.84] I don't really know. I think ads uses
[L1412] [47:32.32] it. I'm not sure." And this is a this is
[L1413] [47:34.36] a caricature, but I think it's very,
[L1414] [47:36.16] very hard to do good engineering in that
[L1415] [47:37.80] environment. You can do competent
[L1416] [47:39.88] engineering, but the best engineering
[L1417] [47:41.84] comes from a deep understanding of why.
[L1418] [47:44.60] And this is something we just drill into
[L1419] [47:47.32] you know, the the team here Convex, or
[L1420] [47:48.88] you know, the team embodies so strongly
[L1421] [47:50.44] at Convex is like everything exists for
[L1422] [47:52.44] the why. Do like don't build a a fancy
[L1423] [47:55.76] load balancer unless it's not needed.
[L1424] [47:57.32] Turns out we do need a fancy load
[L1425] [47:58.68] balancer, we're building it right now.
[L1426] [48:00.12] But but you know,
[L1427] [48:01.68] you should always start with why are we
[L1428] [48:02.88] doing this? What's the point?
[L1429] [48:05.04] And
[L1430] [48:06.92] I feel for people stuck in environments
[L1431] [48:09.96] that are not like this. But you know
[L1432] [48:11.52] what? Like I don't know.
[L1433] [48:14.84] Try to fight the system a little bit. I
[L1434] [48:16.52] think I do see a lot of maybe nihilism,
[L1435] [48:19.36] a lot of defeatedness sometimes amongst
[L1436] [48:21.68] junior engineers. A lot of this um
[L1437] [48:23.96] cynicism.
[L1438] [48:25.36] Like you know, what does it matter? Like
[L1439] [48:27.52] who cares? It's just a big organization
[L1440] [48:29.24] and nothing matters and but I think it
[L1441] [48:31.28] does matter. Like
[L1442] [48:33.36] I've just if I think of like the
[L1443] [48:35.12] happiest times in my life, it's been
[L1444] [48:36.84] like just
[L1445] [48:37.96] dedicating myself to a cause and
[L1446] [48:40.60] and
[L1447] [48:41.56] and trying really hard and and trying to
[L1448] [48:43.60] do the right thing and and I felt good
[L1449] [48:45.32] when I went home and and not trying to
[L1450] [48:47.52] get promoted, just trying to do the
[L1451] [48:48.52] right thing and then and then
[L1452] [48:50.52] assume me I'm going to get promoted and
[L1453] [48:51.60] if not go somewhere else. Um I know it
[L1454] [48:54.08] does sound quaint when I'm saying this,
[L1455] [48:55.96] but I think it's possible to do this and
[L1456] [48:57.48] especially possible if you surround
[L1457] [48:59.28] yourself with people like this.
[L1458] [49:01.24] And if someone is in a big company and
[L1459] [49:03.48] they're feeling frustrated by politics,
[L1460] [49:05.84] look around and see if there's a team of
[L1461] [49:07.56] folks who just seem to
[L1462] [49:09.40] want to do the right thing. Just seem to
[L1463] [49:10.76] want to do good stuff. I don't think
[L1464] [49:12.44] that's selling out. I think that's being
[L1465] [49:13.76] true to yourself. Like just
[L1466] [49:15.68] that's what real engineering is.
[L1467] [49:17.72] Not trying to make a complicated fancy
[L1468] [49:19.44] thing to get promoted. Just build the
[L1469] [49:20.56] coolest thing that's solves the problem.
[L1470] [49:23.08] >> This really reminds me of something you
[L1471] [49:24.72] had written and I thought it was really
[L1472] [49:25.92] good writing. And in the writing there
[L1473] [49:28.52] was this idea of system bias.
[L1474] [49:31.88] And
[L1475] [49:32.48] >> Yes.
[L1476] [49:32.96] >> you you have this
[L1477] [49:34.92] uh quote your your writing. It says you
[L1478] [49:36.96] know, here's some examples. It says the
[L1479] [49:38.56] team is spending 6 months to improve
[L1480] [49:40.36] performance by 10% when it was
[L1481] [49:42.40] completely fine to begin with or you
[L1482] [49:44.80] know, the team is trying desperately to
[L1483] [49:46.48] force their tooling on clients who don't
[L1484] [49:48.96] need it or you know, the team is riding
[L1485] [49:51.76] their outdated system to the grave like
[L1486] [49:54.04] the captain going down on the Titanic.
[L1487] [49:57.64] I I've I've definitely seen examples of
[L1488] [49:59.60] all those types of things in industry.
[L1489] [50:02.56] Um
[L1490] [50:03.52] And so
[L1491] [50:04.72] yeah, it I I think it was it was in the
[L1492] [50:06.92] the
[L1493] [50:08.12] It was in the context of your writing
[L1494] [50:10.00] about um what you should orient your
[L1495] [50:13.20] your team around, not systems, but
[L1496] [50:15.68] actually missions. And maybe that's a
[L1497] [50:18.08] way to fight system bias.
[L1498] [50:20.20] >> Yeah, I mean, one of one of my jobs at
[L1499] [50:21.72] Dropbox um
