Chunk 5; segments 1300–1623. Start may repeat the previous chunk for context.

# Creator of uv, ty, Ruff: How Software Engineering Is Changing | Charlie Marsh

Source ID: source-e744e4ed615158a6
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_uv,_ty,_Ruff_How_Software_Engineering_Is_Changing_Charlie_Marsh_en.txt
Video: https://www.youtube.com/watch?v=Iw65FD4MGgs

[L1309] [47:36.80] um you know I've had people on my team
[L1310] [47:38.64] like because I'm using agents a lot and
[L1311] [47:40.80] and also was you know to some degree
[L1312] [47:43.04] trying to like
[L1313] [47:45.76] push our team to like use agents more. I
[L1314] [47:49.44] mean I mean some of that for me came
[L1315] [47:50.72] from a place of like we build tools for
[L1316] [47:53.52] software engineers and a lot of our
[L1317] [47:56.64] users are now using agents and so if we
[L1318] [47:59.84] like if I if everything good that we do
[L1319] [48:02.88] that's an exaggeration but if everything
[L1320] [48:04.16] good that we do comes from like
[L1321] [48:05.28] understanding our users very well and
[L1322] [48:06.80] like how they work then like we should
[L1323] [48:08.56] probably be like using agents that we
[L1324] [48:10.00] understand like what it's like to build
[L1325] [48:11.20] software for with them so that we can
[L1326] [48:12.96] build better tools for our users. That
[L1327] [48:14.56] was part of my motivation. Um, and part
[L1328] [48:16.64] of it was just kind of seeing how it can
[L1329] [48:19.68] change like how you work. And I don't
[L1330] [48:21.60] know, I think I'm shipping a lot more.
[L1331] [48:23.68] Um, but but it has been like um it has
[L1332] [48:27.52] been like a a difficult process. Like
[L1333] [48:29.04] I've had people on the team tell me um
[L1334] [48:32.72] uh which I think is great that they tell
[L1335] [48:34.48] me this. Um but they're like, "Oh, it
[L1336] [48:36.80] used to be the case that like whenever
[L1337] [48:38.32] you put up a PR, I could like review it
[L1338] [48:40.00] pretty minimally because I had a lot of
[L1339] [48:41.36] confidence in it and like your work. And
[L1340] [48:43.44] now it's like when you put up a PR I
[L1341] [48:45.20] actually have to review it really
[L1342] [48:46.32] closely because you're not like writing
[L1343] [48:48.40] it anymore. It's like the agent and I
[L1344] [48:50.00] was like wow that's like that's like
[L1345] [48:51.84] very interesting to they're completely
[L1346] [48:53.44] right which is and like and the same
[L1347] [48:56.08] thing happens to me. It's like if I go
[L1348] [48:58.64] to sleep and then wake up in the morning
[L1349] [48:59.76] and look at one of the PRs I put up and
[L1350] [49:01.12] I'm like wait this is terrible. You know
[L1351] [49:02.32] what I mean? It's like you can it's it
[L1352] [49:04.40] it's just uh it is easy to trick
[L1353] [49:07.36] yourself into like
[L1354] [49:10.40] basically believing work that isn't at
[L1355] [49:13.52] the same standard as what you would do
[L1356] [49:14.88] before. And I don't think I think we
[L1357] [49:16.56] have we don't really know what to do
[L1358] [49:17.84] with that. Um, and I'm kind of learning
[L1359] [49:20.00] and getting better and like I mean this
[L1360] [49:21.44] was I think I'm doing a lot better job
[L1361] [49:23.28] now than I was in like probably you know
[L1362] [49:25.52] like February or something where I was
[L1363] [49:27.60] like I was just like you know fully
[L1364] [49:30.56] agent killed and I'm like now I'm like a
[L1365] [49:33.04] little bit more like um but so my point
[L1366] [49:36.40] is like that was like a par powerful
[L1367] [49:38.08] kind of like moment for me when someone
[L1368] [49:39.52] on the team said that and I was like wow
[L1369] [49:41.12] like you're right and I and I see that
[L1370] [49:42.96] in other people on the team's work too
[L1371] [49:44.16] like it's not just limited to me but
[L1372] [49:45.44] it's like um you know it really guys
[L1373] [49:48.32] throw a lot of things on their head.
[L1374] [49:50.48] >> If you generate pure slop, that's that's
[L1375] [49:53.52] easy. But I think there's this gray area
[L1376] [49:55.44] where you you generate partially AI slop
[L1377] [49:59.36] or it's, you know, it's it's acceptable,
[L1378] [50:01.52] but it's not at the bar that you used to
[L1379] [50:03.44] have. Do you What are the tactics that
[L1380] [50:06.08] you've used on the team that have worked
[L1381] [50:08.24] for combating this kind of gray area AI
[L1382] [50:11.28] slop?
[L1383] [50:12.88] I'd like to get to a world.
[L1384] [50:15.76] We're not here and I don't know if we'll
[L1385] [50:17.68] ever get there. I'd like to get to a
[L1386] [50:19.68] world where if you put up a PR and it's
[L1387] [50:24.00] all green, then the odds of it getting
[L1388] [50:27.76] merged are like extremely high, right?
[L1389] [50:31.36] Um because that would mean that like you
[L1390] [50:33.44] have automated verification for like
[L1391] [50:35.44] most of what matters. Um and we have a
[L1392] [50:38.24] lot of that in our projects and we've
[L1393] [50:39.28] tried to add more over time and I think
[L1394] [50:40.64] it's helpful. Like we have like in TY
[L1395] [50:42.40] especially we have um
[L1396] [50:44.96] uh tons of like benchmarks like that run
[L1397] [50:47.44] under val grind like um through through
[L1398] [50:49.68] co cod speed like on every PR. So we get
[L1399] [50:51.84] like and that includes memory. So we
[L1400] [50:53.36] benchmark like memory usage and um uh
[L1401] [50:57.20] simulation time and wall time like on
[L1402] [50:58.96] every PR. And then we also have a really
[L1403] [51:02.24] big suite of ecosystem
[L1404] [51:05.36] um tests. So basically every time you
[L1405] [51:07.68] put up a PR we run before and after on
[L1406] [51:10.64] like a bunch of projects in the
[L1407] [51:12.00] ecosystem and then we create this report
[L1408] [51:14.72] of the diff of all the diagnostics like
[L1409] [51:17.20] the errors that got removed and added
[L1410] [51:18.96] and everything. So we have like over
[L1411] [51:20.72] time we've tried to do like more and
[L1412] [51:22.00] more uh these are important honestly
[L1413] [51:24.16] even before we had agents like these
[L1414] [51:25.52] were like we basically couldn't build
[L1415] [51:26.64] without these things but the point is
[L1416] [51:28.40] like I want to have like more automated
[L1417] [51:30.48] verification um and try to get better at
[L1418] [51:32.80] that um and that includes things too
[L1419] [51:36.16] like um we basically assume now that
[L1420] [51:42.56] anyone on the team that puts up a PR has
[L1421] [51:46.00] already run that through codeex review
[L1422] [51:48.00] like probably several times. Um, and
[L1423] [51:50.16] that's basically an assumption. Um, I
[L1424] [51:52.00] mean, we could automate that process,
[L1425] [51:53.20] but
[L1426] [51:53.52] >> codeex review is just an agent reviewing
[L1427] [51:55.36] the code and double checking.
[L1428] [51:56.48] >> Yeah, it's just running codeex and then
[L1429] [51:57.60] just doing slash review.
[L1430] [51:58.56] >> I see.
[L1431] [51:59.04] >> That's it. Yeah, it's not that fancy. I
[L1432] [52:00.32] mean, it's not sorry, it's not that
[L1433] [52:01.36] sophisticated, but it's just like
[L1434] [52:03.04] because now it's like if if a
[L1435] [52:04.32] contributor puts up a PR, that's the
[L1436] [52:05.44] first thing that we do,
[L1437] [52:06.40] >> right?
[L1438] [52:07.84] >> Um because it tends to find good things.
[L1439] [52:10.16] Um, you know, I think I think the things
[L1440] [52:12.40] that I've uh so so like basically I
[L1441] [52:15.28] think one bucket is like how do you um
[L1442] [52:21.52] create more like automated systems that
[L1443] [52:24.16] just help get things make sure things
[L1444] [52:26.72] are right. Um, and that also includes
[L1445] [52:29.52] things like trying to improve your like
[L1446] [52:31.44] agents.mmd file over time. Like if there
[L1447] [52:33.52] are things if there's feedback you're
[L1448] [52:34.72] giving in a review that the agent's not
[L1449] [52:36.56] respecting, try to find a way to help
[L1450] [52:37.92] the agent learn that. even learn um uh
[L1451] [52:41.36] skills like we have some shared skills
[L1452] [52:42.80] on the team stuff like that like none of
[L1453] [52:44.48] this stuff is very sophisticated by the
[L1454] [52:45.68] way it's like pretty simple um the other
[L1455] [52:48.80] piece is like how do I make sure that I
[L1456] [52:52.16] put in the work to ensure that I'm
[L1457] [52:54.24] creating a good PR um and so for me
[L1458] [52:58.08] that's like
[L1459] [53:00.96] I really should understand it's again it
[L1460] [53:03.20] sounds like a really not it really
[L1461] [53:05.44] sounds like a low bar but I should
[L1462] [53:07.52] understand like each line in the PR.
[L1463] [53:10.96] I know it's crazy. Um uh but also I do I
[L1464] [53:16.72] do try to um review each PR myself in
[L1465] [53:21.92] the GitHub UI. This is something I've
[L1466] [53:23.60] always found really helpful. Like if you
[L1467] [53:25.84] actually just like open up your PR and
[L1468] [53:28.48] click files and read through it as if
[L1469] [53:30.48] you were a reviewer, you tend to find
[L1470] [53:32.00] things that you would miss if you were
[L1471] [53:33.28] just looking at your local diff. I find
[L1472] [53:34.88] that very useful. And then the other is
[L1473] [53:37.92] trying to like encode skill. I guess
[L1474] [53:41.20] this is a little bit more in the first
[L1475] [53:42.48] category, but trying to encode skills um
[L1476] [53:45.68] or trying to encode in skills uh things
[L1477] [53:48.48] I'm contin consistently getting wrong
[L1478] [53:50.80] that the agent is getting wrong. Like I
[L1479] [53:52.32] had like a recent example would be I I
[L1480] [53:56.48] found that I was often getting feedback
[L1481] [53:58.16] on PRs that was of the form
[L1482] [54:02.56] what you know this condition here this
[L1483] [54:04.32] like if statement what case is this
[L1484] [54:06.96] intended to catch because if I comment
[L1485] [54:08.96] it out all the tests pass and so I was
[L1486] [54:12.00] like okay I should probably have a pass
[L1487] [54:14.40] before I put up any PR where I have the
[L1488] [54:17.52] agent like go through and check like are
[L1489] [54:19.76] these conditions still relevant or are
[L1490] [54:21.28] they left over from a product refactor
[L1491] [54:22.72] or something else. So, um I I don't
[L1492] [54:25.28] know. I'm not I'm still learning, but
[L1493] [54:27.36] those are some of the things I've been
[L1494] [54:28.64] doing. Yeah, it's again I think it's
[L1495] [54:30.32] like a it's a pretty hard time to be
[L1496] [54:31.60] like building software, but I felt for a
[L1497] [54:34.00] long time or I had a fear that AI was
[L1498] [54:36.80] going to make us more productive, but
[L1499] [54:40.00] that programming would be like a lot
[L1500] [54:41.44] less fun. Um because I just like love I
[L1501] [54:45.60] just like love programming. Um uh and I
[L1502] [54:49.36] was like, "Oh, now I'm going to have to
[L1503] [54:50.48] spend all my time like reviewing code
[L1504] [54:53.36] and like prompting this like idiot agent
[L1505] [54:56.80] to like that's like keeps getting things
[L1506] [54:58.56] wrong and like but ultimately like is
[L1507] [55:00.72] probably more productive." Um I actually
[L1508] [55:03.60] feel way better about that right now
[L1509] [55:05.52] than I did like a few months ago. And I
[L1510] [55:08.64] don't I don't exactly know why. Like I
[L1511] [55:10.88] think
[L1512] [55:12.48] I think it's because
[L1513] [55:15.44] well I think the agents getting better
[L1514] [55:17.04] and the tooling getting better and me
[L1515] [55:18.64] getting more comfortable with it is one
[L1516] [55:20.40] factor. I think the other is um I've
[L1517] [55:24.08] grown to appreciate more of
[L1518] [55:27.68] the the the kinds of things that like
[L1519] [55:29.76] working with agents has unlocked like
[L1520] [55:31.28] the cost of running an experiment is
[L1521] [55:32.96] incredibly low. There's so many things
[L1522] [55:34.72] I've wanted to try or like questions
[L1523] [55:36.96] I've wanted to answer that I could now
[L1524] [55:39.44] answer like almost instantly. Like I
[L1525] [55:42.40] like a sort of a dumb example, we UV in
[L1526] [55:45.52] UV um everything is snapshot tested. So
[L1527] [55:48.80] like basically all of our testing is
[L1528] [55:51.60] effectively
[L1529] [55:53.20] running UV and verifying the output.
[L1530] [55:56.16] That's how we test like basically the
[L1531] [55:57.52] entire program. Um and so that mean we
[L1532] [56:00.64] have a lot of tests that means we have a
[L1533] [56:02.32] lot of test output and the test output
[L1534] [56:06.00] is um it actually ends up in the test
[L1535] [56:09.12] files. So we have rust files like we
[L1536] [56:11.68] have a file called like lock rs that
[L1537] [56:14.40] tests all our UV lock. It's all our UV
[L1538] [56:16.40] lock tests and it's very very long in
[L1539] [56:18.40] part because it has all the lock output
[L1540] [56:20.40] snapshotted in the test. And I was like
[L1541] [56:22.56] hm like what if we stored the snapshots
[L1542] [56:25.20] in separate files?
[L1543] [56:27.44] like would that somehow make our like
[L1544] [56:30.40] compiles faster because then you don't
[L1545] [56:33.04] have technically that's like rust code
[L1546] [56:35.12] and so it's like would that all
[L1547] [56:36.48] disappear and like would that make like
[L1548] [56:38.16] our builds faster or blah blah blah and
[L1549] [56:41.44] I'd always want to do that but it
[L1550] [56:42.56] sounded like like to do that to do that
[L1551] [56:44.40] experiment as a human would be like
[L1552] [56:45.60] extremely painful because you have to
[L1553] [56:47.04] convert all of those tests and I just
[L1554] [56:49.12] had an agent do it in the background
[L1555] [56:50.00] while I did a bunch of other things and
[L1556] [56:51.04] I got a bunch of data on it and the
[L1557] [56:52.72] answer is no but but it's like I you
[L1558] [56:55.52] know what I mean like I I I mean, sorry,
[L1559] [56:57.68] the answer is a little bit more nuanced.
[L1560] [56:59.04] It actually does have a good impact if
[L1561] [57:00.80] um if you're just iterating on the
[L1562] [57:02.64] snapshot outputs, you no longer have to
[L1563] [57:04.40] recompile your program at all because
[L1564] [57:06.16] this outputs are stored somewhere else.
[L1565] [57:07.84] Anyway, that's the thing that makes a
[L1566] [57:09.20] difference on. But my point is I'm just
[L1567] [57:11.04] like running experiments like that like
[L1568] [57:12.56] all day like like trying things that
[L1569] [57:14.48] were used to be hard like used to cost a
[L1570] [57:17.20] lot to um to answer. Uh the work of then
[L1571] [57:21.12] going from that to like production,
[L1572] [57:22.88] there's still like real work there. Um,
[L1573] [57:25.28] but so you know, I think one piece is
[L1574] [57:28.32] the tools and the agents getting better.
[L1575] [57:29.92] The other is things that I just wouldn't
[L1576] [57:32.64] have been able to do before that I can
[L1577] [57:34.00] now do like incredibly easily. And then
[L1578] [57:36.80] um and then the third is I think I'm
[L1579] [57:39.44] more and more realizing that like a lot
[L1580] [57:40.80] of the value I get from building
[L1581] [57:42.24] software is not uh is retained because
[L1582] [57:47.52] some of it is like thinking hard about
[L1583] [57:49.20] like the not it doesn't have to be
[L1584] [57:50.80] typing out the code but it's like
[L1585] [57:52.08] thinking hard about like the layout of a
[L1586] [57:53.52] data structure. A lot of it is merging a
[L1587] [57:56.00] PR that closes a user issue. I get a lot
[L1588] [57:58.08] of satisfaction from actually like like
[L1589] [58:00.64] fixing and improving something. It's not
[L1590] [58:02.24] necessarily just from typing out the
[L1591] [58:03.60] code. So, I I do feel for people a lot
[L1592] [58:06.48] who
[L1593] [58:08.24] feel like they're losing something by
[L1594] [58:09.92] like working with agents because I do
[L1595] [58:11.76] feel that myself. Um, but I feel better
[L1596] [58:14.80] now than I did a few months ago about
[L1597] [58:18.56] my like like what it's like to work as a
[L1598] [58:21.68] software engineer with agents.
[L1599] [58:23.92] You mentioned in the like one of the
[L1600] [58:25.76] performance optimization examples you
[L1601] [58:27.92] said if you just unleash codecs it kind
[L1602] [58:30.16] of does this local optimizations and
[L1603] [58:31.92] it's very
[L1604] [58:32.96] >> good at that but it's not
[L1605] [58:34.88] >> great at kind of like some of the I mean
[L1606] [58:37.44] today it's more human ingenuity of like
[L1607] [58:39.68] system level um
[L1608] [58:41.76] >> optimizations and it kind of reminded me
[L1609] [58:44.48] of this tweet that you had you said it
[L1610] [58:47.04] says I I'm slightly concerned by how
[L1611] [58:49.84] much garbage I would be turnurning out
[L1612] [58:51.60] if I was trying to use these tools
[L1613] [58:53.68] without significant software engineering
[L1614] [58:55.68] experience.
[L1615] [58:57.44] >> I remain concerned about that.
[L1616] [58:58.96] >> Yeah, it it it reminds me and similar to
[L1617] [59:02.56] what uh the Mitchell Hashimoto tweet
[L1618] [59:05.04] that you said. It was like there's a
[L1619] [59:06.56] very big difference between Codex go and
[L1620] [59:09.52] do this versus um you know, you are like
[L1621] [59:13.20] wielding it like this tool and you're
[L1622] [59:14.88] kind of like proddding in the right
[L1623] [59:16.08] direction.
[L1624] [59:16.80] >> Yeah. Um, but yeah, I was curious your
[L1625] [59:19.12] thoughts on that because it seemed like
[L1626] [59:20.56] it went pretty viral and I think a lot
[L1627] [59:22.32] of people are thinking about that.
[L1628] [59:24.32] >> Like being a great software engineer is
[L1629] [59:26.96] like uh
[L1630] [59:30.00] like more like useful than ever. like I
[L1631] [59:32.56] I don't like it's um you know it's still
[L1632] [59:36.72] the case that I I think that the people
