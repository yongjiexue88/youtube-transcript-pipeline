Chunk 4; segments 1108–1489. Start may repeat the previous chunk for context.

# The Co-Creator of Kubernetes: Engineering-Led Direction and Convincing Management | Brendan Burns

Source ID: source-176a06af7f6bc865
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/The_Co-Creator_of_Kubernetes_Engineering-Led_Direction_and_Convincing_Management_Brendan_Burns_en.txt
Video: https://www.youtube.com/watch?v=FKijpCEH9D8

[L1117] [35:25.00] that design decision.
[L1118] [35:26.64] >> Um well, yeah. I mean, and that was
[L1119] [35:28.24] something that was happening broadly in
[L1120] [35:29.56] the industry. Like, that's a part of the
[L1121] [35:31.44] whole like infrastructure as code
[L1122] [35:33.12] movement that was happening at the time.
[L1123] [35:35.36] Um so, we're not the only ones who said
[L1124] [35:37.16] that, but we definitely embraced it. Um
[L1125] [35:40.36] I you know, I mean, I think the benefit
[L1126] [35:42.20] is, you know, you have clarity about the
[L1127] [35:45.16] way you want the world to work.
[L1128] [35:47.12] Right? It's not Like, if you if you if
[L1129] [35:49.96] you execute a bunch of instructions,
[L1130] [35:52.24] start this, run that, do this, like
[L1131] [35:55.76] you've done a bunch of stuff in pursuit
[L1132] [35:58.24] of some objective.
[L1133] [36:01.04] But you never wrote down what the
[L1134] [36:02.24] objective was.
[L1135] [36:03.96] Right? There's no record of like what
[L1136] [36:05.52] you were trying to achieve. I'm trying
[L1137] [36:07.04] to create a website. Well, you didn't
[L1138] [36:08.16] write that down. You just took a bunch
[L1139] [36:09.48] of steps.
[L1140] [36:11.28] Right? With a declarative with a
[L1141] [36:13.00] declarative approach, you actually write
[L1142] [36:14.32] it down. You say like, "I'm trying to
[L1143] [36:15.84] create a reliable website, and here's
[L1144] [36:17.88] what a reliable website looks like."
[L1145] [36:20.00] "Hey system, could you take the steps to
[L1146] [36:22.72] get there?"
[L1147] [36:23.88] Right? And so, you have that record. Um
[L1148] [36:26.88] and it obviously makes it easier for
[L1149] [36:28.40] things to be self-healing because if
[L1150] [36:31.16] you've written it down, now I know where
[L1151] [36:33.44] I'm supposed to go back if like if I get
[L1152] [36:34.68] perturbed from that state, if something
[L1153] [36:36.24] fails, if something restarts, well, I
[L1154] [36:38.16] know where I'm supposed to go back to.
[L1155] [36:40.20] Um
[L1156] [36:41.44] and similarly, like it has ans- it has
[L1157] [36:44.76] side benefits of like once I write it
[L1158] [36:47.08] down, well, I can apply code review to
[L1159] [36:49.20] it.
[L1160] [36:50.08] I can apply unit tests to it.
[L1161] [36:52.32] Like there's a lot of like the the
[L1162] [36:53.96] mechanics of how we do software
[L1163] [36:55.48] development that apply once you write
[L1164] [36:57.72] down that declaration.
[L1165] [37:00.16] Um so like a lot of those are the
[L1166] [37:01.48] benefits. I think the downside is
[L1167] [37:02.96] probably just complexity.
[L1168] [37:05.48] Right?
[L1169] [37:06.52] You know, in comparison to go and click
[L1170] [37:08.04] click click through a wizard or
[L1171] [37:09.84] whatever, you know, in a GUI. Um
[L1172] [37:12.96] learning and you know, everybody
[L1173] [37:14.32] complains about the YAML and I have to
[L1174] [37:16.40] learn all this stuff and you know, like
[L1175] [37:19.24] it does introduce a
[L1176] [37:22.04] a learning curve.
[L1177] [37:23.60] Um now, I think fortunately at this
[L1178] [37:25.28] point there's enough educational
[L1179] [37:26.20] material out there that it's not and and
[L1180] [37:28.00] GenAI, too, for that matter, that it's
[L1181] [37:30.40] not that bad a learning curve.
[L1182] [37:32.52] Um but certainly in comparison to what
[L1183] [37:35.48] people have done before, that's probably
[L1184] [37:36.84] the biggest downside. But I don't know.
[L1185] [37:38.28] I think that the upsides are
[L1186] [37:40.04] like up here and the downsides are like
[L1187] [37:41.80] way down like there's there's not a lot
[L1188] [37:43.36] of downside.
[L1189] [37:45.08] >> I see. Yeah, I could also see that being
[L1190] [37:47.32] helpful for I guess if you want to
[L1191] [37:49.48] optimize anything under the hood cuz
[L1192] [37:51.80] you're just making a promise to people
[L1193] [37:53.56] that this is going to happen, but if you
[L1194] [37:55.92] want to do it in a more efficient way or
[L1195] [37:57.60] something like that, then I guess it
[L1196] [38:00.20] just gives you all the the power to do
[L1197] [38:02.04] so.
[L1198] [38:02.52] >> Yeah, well, I mean, then that does make
[L1199] [38:03.76] things like machines failing a lot
[L1200] [38:05.20] easier.
[L1201] [38:06.36] Right? Because people don't say run this
[L1202] [38:08.56] on this machine. They just say, "I want
[L1203] [38:10.76] three of this to be somewhere."
[L1204] [38:13.20] And if a machine fails, well, it just
[L1205] [38:15.20] moves somewhere else, right? Because the
[L1206] [38:16.84] application isn't tied cuz I can't In
[L1207] [38:19.32] some ways, I don't know your intent,
[L1208] [38:20.72] right? If you log into a machine and you
[L1209] [38:22.84] start a process on that machine,
[L1210] [38:25.72] is it because you wanted a process?
[L1211] [38:28.00] Or is it because you wanted a process on
[L1212] [38:29.68] that machine?
[L1213] [38:31.52] I don't know. You didn't tell me.
[L1214] [38:33.68] And so if that machine fails,
[L1215] [38:36.24] what should I do? Well, I don't know,
[L1216] [38:38.28] right? But if I But if I know you said,
[L1217] [38:40.16] "Hey, I just want three replicas."
[L1218] [38:41.96] Well, then I know it doesn't matter that
[L1219] [38:43.36] it's on that machine. It could be on a
[L1220] [38:44.92] different machine. You'd be just as
[L1221] [38:46.08] happy.
[L1222] [38:47.04] >> I want to shift a little bit to kind of
[L1223] [38:49.64] when Kubernetes was was scaling and it
[L1224] [38:53.68] sounds like a a large part of this was
[L1225] [38:55.44] getting buy-in from other companies and
[L1226] [38:57.44] other people.
[L1227] [38:58.72] And so, you know, how how did you get
[L1228] [39:01.12] the buy-in from I know OpenShift was an
[L1229] [39:04.40] important part of Yeah, Red Hat
[L1230] [39:07.12] um and other companies that that joined
[L1231] [39:09.16] on. Like, how did you sell those
[L1232] [39:10.44] companies that Kubernetes is what you
[L1233] [39:12.44] want to use?
[L1234] [39:14.16] >> Well, I think I think for a lot of them,
[L1235] [39:15.56] especially in the early days, it was
[L1236] [39:17.28] kind of that quote around uh
[L1237] [39:18.88] undifferentiated heavy lifting.
[L1238] [39:21.52] Right? Like, they had some other
[L1239] [39:22.80] objective. Like, OpenShift was trying to
[L1240] [39:24.40] build a platform as a service.
[L1241] [39:26.60] Um or, you know, they were
[L1242] [39:29.20] you know, a lot of our early users who
[L1243] [39:30.84] were also contributors, you know, they
[L1244] [39:32.60] were trying to build some sort of
[L1245] [39:33.56] reliable web service or something like
[L1246] [39:35.28] that, right? And so, it was like, "Well,
[L1247] [39:38.56] we're going to have to build this thing
[L1248] [39:39.64] anyway.
[L1249] [39:40.80] Why don't we all build it together?
[L1250] [39:42.84] And we don't really care cuz we don't
[L1251] [39:44.00] think that's our value. Like, our we
[L1252] [39:45.36] don't think our value is tied up in that
[L1253] [39:47.68] layer.
[L1254] [39:48.72] So, we'll go contribute to your thing
[L1255] [39:50.64] cuz we're going to get more value out of
[L1256] [39:52.24] the collective than out of trying to do
[L1257] [39:54.16] it ourselves."
[L1258] [39:55.72] Um
[L1259] [39:57.16] and and so for a lot of the early
[L1260] [39:58.48] partners, that was a big part of the
[L1261] [39:59.80] argument was was like,
[L1262] [40:02.24] "Hey, we'll let you in." And And part of
[L1263] [40:03.80] that is making sure that they understand
[L1264] [40:04.96] that they're going to like that they're
[L1265] [40:06.72] going to be equal partners.
[L1266] [40:08.60] Right? Where it's not like cuz it's it's
[L1267] [40:10.40] one thing to take a dependency on
[L1268] [40:11.64] something, but then you're kind of like
[L1269] [40:13.96] taking dependency on someone else's road
[L1270] [40:15.76] map.
[L1271] [40:17.40] And so, it was really important also to
[L1272] [40:19.56] say, "Hey, like
[L1273] [40:21.72] you can come take a dependency on us,
[L1274] [40:24.36] but also we'll give you a seat at the
[L1275] [40:26.32] design table. So, when you need new
[L1276] [40:27.88] features,
[L1277] [40:29.12] you can, you know, contribute those
[L1278] [40:30.76] features. And And here's what we're
[L1279] [40:32.16] trying to achieve. And And And it
[L1280] [40:33.76] matches up with your road map. And you
[L1281] [40:35.88] know, that kind of stuff." So, I think
[L1282] [40:37.68] that's how we we approached it. And
[L1283] [40:39.00] then,
[L1284] [40:39.80] uh over time, you know, people became
[L1285] [40:42.88] more and more interested in being part
[L1286] [40:44.40] of it because there was a growing
[L1287] [40:45.76] ecosystem.
[L1288] [40:47.04] So, when you look at like networking
[L1289] [40:48.32] providers or storage providers, you
[L1290] [40:50.76] know, as their users were starting to
[L1291] [40:52.48] become Kubernetes users,
[L1292] [40:54.48] um they were motivated to make sure that
[L1293] [40:56.76] their networking system worked well with
[L1294] [40:58.96] Kubernetes or their storage system
[L1295] [41:00.60] worked well with Kubernetes and things
[L1296] [41:02.20] like that. Um so, that was sort of a
[L1297] [41:03.80] secondary layer of partner discussions
[L1298] [41:05.44] that we had.
[L1299] [41:06.84] >> Right. And that's not downstream of
[L1300] [41:08.80] becoming the dominant player. And I
[L1301] [41:10.40] guess that's validating the open source
[L1302] [41:12.32] strategy, which is you become dominant,
[L1303] [41:14.64] everyone's kind of got a
[L1304] [41:16.44] um integrate with you and all of that.
[L1305] [41:18.56] How did you prevent Google from
[L1306] [41:20.48] dominating in the the road map or I
[L1307] [41:23.28] guess controlling what Kubernetes would
[L1308] [41:25.04] be, given that it started at Google,
[L1309] [41:27.96] funded largely by Google?
[L1310] [41:30.28] >> Yeah, I mean, I think that was really
[L1311] [41:31.28] important. Um and and I think it was a
[L1312] [41:33.04] critical part of gaining adoption,
[L1313] [41:35.36] right? Um
[L1314] [41:36.72] and and and becoming the industry
[L1315] [41:38.04] standard and was was giving it
[L1316] [41:40.60] independence. Um and I think, you know,
[L1317] [41:42.92] there's two pieces to that. The first is
[L1318] [41:45.40] um getting it to foundation. So, the
[L1319] [41:48.12] creation uh it was only a year in that
[L1320] [41:51.68] we created the Cloud Native Compute
[L1321] [41:53.28] Foundation, that we donated all of
[L1322] [41:55.64] Kubernetes to the Cloud Native Compute
[L1323] [41:57.16] Foundation. Um and so, getting the
[L1324] [41:59.84] project, the logos, all of the legal
[L1325] [42:03.32] stuff, trademarks, all of that stuff,
[L1326] [42:06.00] um
[L1327] [42:07.04] into a independent software foundation
[L1328] [42:09.48] um with the Linux Foundation was
[L1329] [42:11.44] critical, right? Cuz cuz it's hard to
[L1330] [42:13.84] partner if you know, somebody else has
[L1331] [42:15.44] trademarks on the Kubernetes logo or
[L1332] [42:17.04] whatever.
[L1333] [42:18.08] Um
[L1334] [42:19.80] and then I think the other piece that
[L1335] [42:22.00] was important that came a little bit
[L1336] [42:23.32] later um
[L1337] [42:24.96] was writing down the governance rules.
[L1338] [42:27.88] So, you know, for the first time for
[L1339] [42:32.08] first for a few years, Kubernetes didn't
[L1340] [42:34.88] have any really governance rules written
[L1341] [42:36.60] down.
[L1342] [42:37.64] Um it was a mistake I would say, right?
[L1343] [42:39.44] Like we didn't realize how
[L1344] [42:41.80] it was really it was something we should
[L1345] [42:43.04] have done earlier, but we didn't. Um
[L1346] [42:46.48] and so we sat down in 2016 to write the
[L1347] [42:50.88] governance rules
[L1348] [42:52.72] um
[L1349] [42:53.52] and I think all of us were aligned and
[L1350] [42:56.60] on this idea that we didn't want any one
[L1351] [42:59.24] company to be able to take control of
[L1352] [43:00.88] the community.
[L1353] [43:02.56] Um and we really built the community and
[L1354] [43:05.52] the govern the rules of governance to be
[L1355] [43:07.64] democratic. Um
[L1356] [43:10.04] you know, we never I mean I think that's
[L1357] [43:11.56] an aesthetic from Craig and Joe and I.
[L1358] [43:13.12] We never set out to be like a benevolent
[L1359] [43:14.68] dictator for life style project. We
[L1360] [43:16.84] always set out to be a distributed
[L1361] [43:19.52] uh you know, distributed ownership
[L1362] [43:21.52] democratic kind of project. Um and we
[L1363] [43:24.96] codified we codified a lot of that into
[L1364] [43:27.36] the governance docs that you know,
[L1365] [43:29.16] continue to this day. So, um I think
[L1366] [43:31.60] both those things together really helped
[L1367] [43:34.16] make sure that it was a an industry
[L1368] [43:36.08] standard not a and not any one
[L1369] [43:37.76] particular company standard.
[L1370] [43:40.00] But also I think were critical to its
[L1371] [43:41.28] success. Like I think they're they're
[L1372] [43:43.16] they're jewels of each other, right?
[L1373] [43:44.52] Like you can't have one without the
[L1374] [43:45.68] other.
[L1375] [43:46.40] >> People wouldn't have come on if they
[L1376] [43:48.72] didn't see that it was uh governed well
[L1377] [43:51.36] and open.
[L1378] [43:52.24] >> Yeah, I mean cuz obviously like you're
[L1379] [43:53.56] thinking about adopting it or you're
[L1380] [43:54.88] thinking about you know, putting it in
[L1381] [43:57.08] your service like the thing the thing
[L1382] [43:58.64] you're worried about is like whose road
[L1383] [44:00.56] map am I betting on?
[L1384] [44:02.16] >> Um when you said governance, is that I
[L1385] [44:04.80] mean mean, that literally like uh like
[L1386] [44:06.52] when I think of government, like there's
[L1387] [44:07.84] a constitution somewhere?
[L1388] [44:09.76] >> That's literally what we wrote.
[L1389] [44:11.36] >> Did you write that yourself or is that
[L1390] [44:12.52] something that like lawyers do or
[L1391] [44:14.44] >> Uh no, no, we wrote it ourselves, yeah.
[L1392] [44:16.48] Um
[L1393] [44:18.12] in the span of about uh it was a couple
[L1394] [44:20.92] of free couple free fairly intense
[L1395] [44:22.64] meetings amongst amongst like six or
[L1396] [44:24.44] seven of us. We got together um
[L1397] [44:27.44] and uh
[L1398] [44:29.28] and just kind of talked it through.
[L1399] [44:31.08] And and and looked at a bunch of other
[L1400] [44:34.68] communities and kind of like what had
[L1401] [44:37.48] worked, what had not worked, what were
[L1402] [44:39.24] we worried about, what were we trying to
[L1403] [44:41.16] achieve.
[L1404] [44:42.52] Um some of it was codifying stuff that
[L1405] [44:44.68] already existed.
[L1406] [44:46.48] Um so we had some loose organization
[L1407] [44:49.00] stuff that already existed in sort of a
[L1408] [44:51.24] de facto way, but didn't it exist in a
[L1409] [44:53.76] explicit way.
[L1410] [44:55.20] Um some of it was, you know, uh we we
[L1411] [44:58.68] created the steering committee
[L1412] [45:00.88] uh that had never existed before, right?
[L1413] [45:03.04] And we just basically uh and we were
[L1414] [45:05.88] lucky, I think, that we were able to
[L1415] [45:07.76] gather
[L1416] [45:09.12] uh so the people that came together, we
[L1417] [45:10.44] called it the bootstrap committee.
[L1418] [45:12.52] Um
[L1419] [45:13.88] you know, we we were lucky in the sense
[L1420] [45:15.52] that we had enough people
[L1421] [45:18.04] in who kind of were
[L1422] [45:20.16] not who who the entire community would
[L1423] [45:22.84] look at as being leaders.
[L1424] [45:25.76] And and and they worked we weren't
[L1425] [45:27.44] fighting with each other, you know, we
[L1426] [45:28.88] weren't in fighting, so we were all kind
[L1427] [45:30.20] of aligned. And we kind of got
[L1428] [45:32.04] everybody. So we didn't have to be like,
[L1429] [45:33.76] oh, you know, we grabbed this side and
[L1430] [45:35.64] not that side. We kind of we grabbed we
[L1431] [45:37.60] were able in
[L1432] [45:38.96] it was like seven people, I think, seven
[L1433] [45:40.28] or eight people. Um
[L1434] [45:42.04] we were able to pull together
[L1435] [45:44.68] a group of people that really
[L1436] [45:46.04] represented everybody and that everybody
[L1437] [45:48.00] kind of all respected each other and
[L1438] [45:50.08] respected each other as leaders in the
[L1439] [45:51.52] space. Um and a lot of credit there, I
[L1440] [45:53.80] think, goes to I mean, everybody deserve
[L1441] [45:55.56] who is involved deserves a lot of
[L1442] [45:56.76] credit, but um
[L1443] [45:58.56] Sarah Novotny, who was the um
[L1444] [46:01.36] uh our community leader at the time
[L1445] [46:03.48] deserves I think a ton of credit for
[L1446] [46:05.08] bringing that bringing that thing
[L1447] [46:06.68] together.
[L1448] [46:07.64] >> When you look back on on Kubernetes, cuz
[L1449] [46:11.52] with an open source project, there's
[L1450] [46:13.52] obviously the the read aspect, which is
[L1451] [46:15.84] everyone can use and duplicate this code
[L1452] [46:18.68] and execute it. But there's also I guess
[L1453] [46:21.00] the writing part, which is people making
[L1454] [46:22.84] contributions.
[L1455] [46:24.40] What percent of the contributions
[L1456] [46:25.80] actually come from the community and
[L1457] [46:27.48] what percent is actually just the main
[L1458] [46:30.16] stakeholder companies just putting in
[L1459] [46:32.16] their code?
[L1460] [46:33.60] >> Um yeah, I don't have the specific
[L1461] [46:35.04] numbers for Kubernetes, but my
[L1462] [46:36.24] experience in open source says it's like
[L1463] [46:38.40] 80 to 80 90% the core contributors.
[L1464] [46:41.96] And like less than 10%
[L1465] [46:44.80] other people. It It's It's It's hard I
[L1466] [46:47.52] think in general. It's really hard to
[L1467] [46:49.00] get people to contribute. Um part of it
[L1468] [46:52.72] is companies, honestly, right? Like you
[L1469] [46:55.12] know, companies like Microsoft, uh
[L1470] [46:57.56] we make a commitment to contributing to
[L1471] [47:00.24] open source. And so, you know, we at a
[L1472] [47:02.32] leadership level, we've decided that
[L1473] [47:04.16] this is something that we want to invest
[L1474] [47:05.56] in.
[L1475] [47:06.36] Um and so we're willing to have teams of
[L1476] [47:08.08] people who specialize in working in
[L1477] [47:10.20] upstream open source projects.
[L1478] [47:12.04] Um
[L1479] [47:13.00] but for a lot of users of Kubernetes,
[L1480] [47:15.48] you know, they're a retailer or they're
[L1481] [47:17.08] a banking industry or they're like
[L1482] [47:19.76] it's tech isn't their core thing that
[L1483] [47:21.64] they're doing. Tech is a means to an end
[L1484] [47:23.88] to deliver an app for their user. And in
[L1485] [47:26.16] that world, it's pretty hard to justify
[L1486] [47:29.04] well, I'm going to take
[L1487] [47:30.56] 10% of my people and I'm just going to
[L1488] [47:32.12] do upstream open source contributions.
[L1489] [47:34.96] Right? Um and especially if the
[L1490] [47:37.08] leadership is like not a technical
[L1491] [47:39.76] leadership, and so they didn't
[L1492] [47:41.00] necessarily grow up in those
[L1493] [47:42.12] communities. And if you grow up in
[L1494] [47:43.28] finance, it's hard to explain like
[L1495] [47:45.32] what's the value of contributing to the
[L1496] [47:47.40] I mean, the value of taking the open
[L1497] [47:48.96] source is very clear, right? It's free.
[L1498] [47:51.32] Um but the value of contributing back,
