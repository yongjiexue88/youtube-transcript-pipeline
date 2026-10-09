Chunk 5; segments 1328–1668. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L1337] [48:05.68] elements in it. Fine. I can just have
[L1338] [48:07.36] multiple physics handles if that's what
[L1339] [48:08.64] I need or something like this. I can
[L1340] [48:10.00] very flexibly like merge these things
[L1341] [48:11.76] together. I want something to not have
[L1342] [48:13.52] physics. I just don't ever insert the,
[L1343] [48:15.92] you know, I don't ever ask the physics
[L1344] [48:17.12] system to have a valid, you know, piece
[L1345] [48:19.76] of data for this handle in it and it
[L1346] [48:21.28] won't simulate any physics for it.
[L1347] [48:22.80] Right? Whether that's the world's best
[L1348] [48:26.00] architecture or not, I'm not going to
[L1349] [48:27.92] argue for it or against it. It's just
[L1350] [48:29.68] it's a lot better than domain model
[L1351] [48:31.36] hierarchies. That I will say, right?
[L1352] [48:34.40] OpenAI, Enthropic, Cursor, and Verscell
[L1353] [48:38.16] all use this product to make their lives
[L1354] [48:40.00] better. And the problem it solves is
[L1355] [48:42.56] when you're building SAS or an AI
[L1356] [48:44.40] product and you want to sell to other
[L1357] [48:46.32] companies, there's all these
[L1358] [48:47.84] requirements you need to meet. There's
[L1359] [48:49.76] SSO, there's skim, there's arbback,
[L1360] [48:53.04] there's audit logs. These are all things
[L1361] [48:54.88] that take time to integrate but aren't
[L1362] [48:57.04] the main focus of your app. Work OS is
[L1363] [48:59.36] an API layer that lets you meet all of
[L1364] [49:01.20] these requirements in just a few lines
[L1365] [49:03.44] of code. So let's say you have a new SAS
[L1366] [49:05.84] product and you want to sell to other
[L1367] [49:07.44] companies. Work OS will solve all of
[L1368] [49:09.68] these critical feature gaps for you. You
[L1369] [49:12.40] can check them out at workos.com to
[L1370] [49:14.88] learn more and get started. And I
[L1371] [49:17.04] appreciate them for supporting my work
[L1372] [49:18.72] and sponsoring this podcast. Jira
[L1373] [49:21.28] byatlassian isn't just for tracking work
[L1374] [49:23.52] anymore. Now you can pick your favorite
[L1375] [49:25.36] AI agent to assign tasks to and they'll
[L1376] [49:28.08] get access to the rich context that's
[L1377] [49:30.08] already in Jira. When the agent is done,
[L1378] [49:32.32] it surfaces a poll request. That way you
[L1379] [49:34.72] can get more done with your favorite
[L1380] [49:36.32] agents all in one place. Learn more at
[L1381] [49:39.28] jira.dev. That's jir.dev.
[L1382] [49:44.00] Appreciate them for sponsoring the
[L1383] [49:45.44] podcast. And back to the show. [snorts]
[L1384] [49:47.92] Earlier we talked about the the
[L1385] [49:49.68] trade-off between I guess performant
[L1386] [49:52.48] code and maintainable code and I saw you
[L1387] [49:56.80] had this one video said you know in
[L1388] [49:59.12] quotes clean code horrible performance
[L1389] [50:03.12] I feel like this is on the same topic.
[L1390] [50:05.60] What's your your take there on you know
[L1391] [50:08.80] because you also put clean code in
[L1392] [50:10.96] quotes. What does that mean?
[L1393] [50:12.56] >> So it's a it's a fairly subtle topic
[L1394] [50:14.72] right? Uh, and that's why the the quotes
[L1395] [50:16.88] are there because um the first thing
[L1396] [50:18.80] that I you have to point out is that
[L1397] [50:20.64] clean code is clean code,
[L1398] [50:23.28] object-oriented programming, a lot of
[L1399] [50:25.44] these phrases, they mean different
[L1400] [50:27.04] things to different people. And so if
[L1401] [50:29.04] you're going to say that you're, you
[L1402] [50:30.40] know, this code is clean, it's pretty
[L1403] [50:33.04] hard to find two programmers who will
[L1404] [50:36.08] agree on exactly whether it is or not,
[L1405] [50:38.96] right? Like like they all have like
[L1406] [50:40.40] different ideas about what is clean and
[L1407] [50:42.56] what is not,
[L1408] [50:43.36] >> right?
[L1409] [50:44.48] So the reason I put that in quotes is I
[L1410] [50:46.16] was talking about a very specific thing
[L1411] [50:47.36] which is like literally like the book
[L1412] [50:49.60] clean code like the thing where there's
[L1413] [50:51.36] like here are the things that we would
[L1414] [50:52.64] recommend that you do right so in that
[L1415] [50:55.60] particular case what I was talking about
[L1416] [50:56.80] is there's a certain set of ideas that
[L1417] [51:00.64] is advocated in clean code as like these
[L1418] [51:02.88] are the things you should do and they
[L1419] [51:05.12] are like you should have uh everything
[L1420] [51:07.44] should be kind of um I guess I would say
[L1421] [51:11.68] dynamic dispatch or at least You
[L1422] [51:13.84] shouldn't code shouldn't know the types
[L1423] [51:15.36] it's operating on. Right? Saying it's
[L1424] [51:17.36] dynamic dispatch is maybe it depends on
[L1425] [51:19.36] the language whether that's going to be
[L1426] [51:20.56] true or not. But when I write code I
[L1427] [51:22.64] don't know what types I have. It's just
[L1428] [51:24.40] I don't know like some base classes is
[L1429] [51:26.00] what I'm operating on and they could be
[L1430] [51:27.36] anything. Right? That's thing one. Thing
[L1431] [51:29.52] two is functions should be very small.
[L1432] [51:31.68] Uh in fact the the numbers are kind of
[L1433] [51:33.92] weird. They're like four lines or five
[L1434] [51:36.08] line. Like when you go look at the
[L1435] [51:37.44] actual things that are claimed in some
[L1436] [51:38.80] of the this literature it's it's really
[L1437] [51:40.72] strange. you're just like, gosh, that's
[L1438] [51:42.80] very small, right? Um, and I go through
[L1439] [51:46.88] some of those things and I say, look, if
[L1440] [51:48.40] we were to actually follow these, we get
[L1441] [51:51.20] into a really bad state because a lot of
[L1442] [51:53.92] the languages that people are going to
[L1443] [51:55.28] be using to implement this stuff, like
[L1444] [51:56.96] C++ for example, um, which even would be
[L1445] [51:59.60] a fairly good case in a lot of because
[L1446] [52:01.68] at least it's a compiled language and so
[L1447] [52:03.36] on.
[L1448] [52:05.28] In a a lot of cases, these things are
[L1449] [52:07.04] kind of a recipe for disaster if you're
[L1450] [52:10.40] if you're handing out types where you
[L1451] [52:12.48] can't know the type at compile time or
[L1452] [52:14.64] you can't know the type uh or it's or
[L1453] [52:16.40] it's you know going to be in a different
[L1454] [52:17.68] module. So, you know, unless you have
[L1455] [52:19.04] like a really aggressive link time code
[L1456] [52:20.56] generation, it's not going to be likely
[L1457] [52:21.76] that you could figure this out and
[L1458] [52:23.28] you're saying all the functions should
[L1459] [52:24.40] be very small and of course they're
[L1460] [52:25.60] going to be virtual because they're on
[L1461] [52:26.96] these sort of types that you don't know
[L1462] [52:28.08] what they are.
[L1463] [52:29.92] This creates a really uh toxic
[L1464] [52:32.32] combination for the compiler. Normally
[L1465] [52:36.00] you can have I mean you can have small
[L1466] [52:39.04] functions if you want them only four
[L1467] [52:40.32] lines long. If the compiler can know
[L1468] [52:42.32] that it can just inline that, right? If
[L1469] [52:44.24] it can see clearly what you're doing and
[L1470] [52:46.24] it can just merge those things in, we
[L1471] [52:48.00] don't have a problem. If they're behind
[L1472] [52:49.52] a virtual function, so it doesn't know
[L1473] [52:51.76] like it can't guarantee that it is that
[L1474] [52:54.08] type. Um it can't do that. And so when
[L1475] [52:58.32] you talk about all this stuff, what
[L1476] [52:59.76] you're what you're giving up people I
[L1477] [53:01.52] think also because the video I mean the
[L1478] [53:03.20] video was a very short video as part of
[L1479] [53:04.72] like a series
[L1480] [53:06.56] I think people sometimes get the wrong
[L1481] [53:07.84] idea that I think that virtual function
[L1482] [53:09.28] calls cost a lot. They do cost something
[L1483] [53:11.68] but you know depending on how you want
[L1484] [53:13.36] to look at it they actually don't cost
[L1485] [53:14.56] that much. Uh because you know it
[L1486] [53:17.04] depends on whether it's predicted
[L1487] [53:18.56] correctly or not but in general like the
[L1488] [53:20.48] cost of virtual function is less than
[L1489] [53:21.84] you would think. A lot of times
[L1490] [53:24.24] the actual reason that it slows things
[L1491] [53:25.92] down is because the compiler cannot
[L1492] [53:27.60] merge the code together, right? It can't
[L1493] [53:29.60] inline stuff and remove and reduce the
[L1494] [53:31.68] waste. Like that's the actual problem.
[L1495] [53:34.32] So if you just want to call a virtual
[L1496] [53:35.76] function, yeah, it if it was a really
[L1497] [53:38.24] really uh hardcore optimization
[L1498] [53:40.56] scenario, then you don't want anything
[L1499] [53:42.48] probably calling a virtual function in
[L1500] [53:44.00] general because there is some cost to
[L1501] [53:45.36] that. Just calling a function has cost.
[L1502] [53:48.56] But that wasn't the really bad part of
[L1503] [53:50.80] it, right? So, it's that plus there's an
[L1504] [53:53.68] additional thing which is that it can't
[L1505] [53:55.52] unroll and go wide on things. If the
[L1506] [53:57.52] compiler can see everything you're
[L1507] [53:58.80] doing, it can use SIMD. It can like
[L1508] [54:01.20] widen loops to operate on multiple
[L1509] [54:02.88] things at once. It can unroll those
[L1510] [54:04.16] loops. There's all these things it can
[L1511] [54:05.28] do. If it's got these virtual functions,
[L1512] [54:06.80] it's just like that's it. I don't know.
[L1513] [54:09.52] I I can't make decisions about that. I
[L1514] [54:11.04] have no idea what this thing on the
[L1515] [54:12.00] other end is doing. Right? So, uh that
[L1516] [54:14.96] was kind of my point on that. And uh
[L1517] [54:17.36] again I it's not meant to be uh
[L1518] [54:19.76] assailing the idea that your code should
[L1519] [54:21.68] be easy to read or easy to maintain.
[L1520] [54:23.68] It's just more like these guidelines
[L1521] [54:25.44] seem really bad. And also I don't think
[L1522] [54:27.60] we need them for code to be
[L1523] [54:29.20] maintainable. I I don't have trouble
[L1524] [54:31.12] maintaining functions that are 30 lines
[L1525] [54:32.80] long or 50 lines long. I don't find that
[L1526] [54:34.72] five is a magic number or something or
[L1527] [54:36.16] that has to be really short. Uh and also
[L1528] [54:38.00] I find that it's usually pretty easy to
[L1529] [54:39.52] write code where I know what the types
[L1530] [54:41.04] are. Um that those can be determined at
[L1531] [54:42.96] compile time. Like I don't think that
[L1532] [54:44.88] results in code that's particularly hard
[L1533] [54:47.36] to read.
[L1534] [54:48.80] >> When I was in college very and very
[L1535] [54:51.36] early I remember people recommend that
[L1536] [54:53.84] book say oh you should read clean code.
[L1537] [54:56.32] >> So my understanding that you wouldn't
[L1538] [54:57.76] recommend people who are software
[L1539] [54:59.76] engineers to read that.
[L1540] [55:01.92] >> I guess the way I would categorize it's
[L1541] [55:03.52] a mixed bag. So I would I wouldn't
[L1542] [55:05.44] actually say that I disagree with all
[L1543] [55:07.52] all of the things in the book though. I
[L1544] [55:09.20] mean some of the things are things that
[L1545] [55:10.80] I definitely do myself like giving um
[L1546] [55:14.16] variables like easy to understand names
[L1547] [55:17.36] uh is something that I think would be
[L1548] [55:19.20] and that's in that book uh is good
[L1549] [55:21.76] advice right and so kind of more I
[L1550] [55:24.96] wouldn't I wouldn't necessarily say do
[L1551] [55:26.48] or don't read a book what I would say is
[L1552] [55:28.40] like I think there's some things in this
[L1553] [55:30.32] book that don't that aren't addressed
[L1554] [55:32.72] properly like I don't think you want to
[L1555] [55:34.56] tell people these rules of thumb and not
[L1556] [55:36.32] tell them about these other problems
[L1557] [55:38.16] That was exactly what I was uh pointing
[L1558] [55:40.72] out there. And so usually it's more that
[L1559] [55:43.36] it's like
[L1560] [55:45.92] I find that often times there is this
[L1561] [55:49.44] tendency
[L1562] [55:51.20] um I guess I'll say to pretend
[L1563] [55:54.32] that
[L1564] [55:55.84] we don't have to talk about performance
[L1565] [55:57.84] and we can just say like in fact
[L1566] [55:59.52] premature optimization is root all evil.
[L1567] [56:01.36] Bringing it back to there. I feel like
[L1568] [56:03.36] there's this uh temptation and very
[L1569] [56:06.96] prevalent practice of sort of taking
[L1570] [56:09.04] that idea to mean we don't have to talk
[L1571] [56:12.16] about performance when we're teaching
[L1572] [56:13.28] people things at all. Or like when you
[L1573] [56:15.28] write the book clean code, you don't
[L1574] [56:16.64] have to talk about performance at all.
[L1575] [56:17.84] can just include a thing that's
[L1576] [56:19.68] basically like hey um you know there's
[L1577] [56:23.76] performance issues but most of the time
[L1578] [56:25.44] it's not a problem or something like
[L1579] [56:26.48] that which is you know or if you look at
[L1580] [56:28.72] uh refactoring the book refactoring very
[L1581] [56:32.00] popular it literally says exactly that
[L1582] [56:33.36] in like the opening thing it's like you
[L1583] [56:34.48] know there there might be performance
[L1584] [56:35.76] concerns but you know they're usually
[L1585] [56:37.68] okay or something right and it's like
[L1586] [56:39.44] that is not true I just think that's
[L1587] [56:41.68] fundamentally not true I think these
[L1588] [56:43.20] books should include detailed
[L1589] [56:46.00] discussions of the actual performance
[L1590] [56:48.48] problems that you are very likely to hit
[L1591] [56:50.32] if you take some of their advice. Um
[L1592] [56:52.96] because it's not that it means you can't
[L1593] [56:56.08] do those things, but I'll quote you back
[L1594] [56:59.28] to you. It's about trade-offs. There is
[L1595] [57:02.08] always a trade-off that you're making.
[L1596] [57:04.56] And sometimes if you understand the
[L1597] [57:06.88] trade-off, you will make it. You'll say,
[L1598] [57:09.52] I know this is going to cost this may be
[L1599] [57:11.52] a serious performance problem for us,
[L1600] [57:13.52] but I think that's okay. Like I think
[L1601] [57:15.76] it's not like our performance won't
[L1602] [57:17.36] suffer to the point where it's a problem
[L1603] [57:19.04] for the product. I understand what
[L1604] [57:22.16] that's is. There's a huge difference
[L1605] [57:24.80] between that and just going like ah we
[L1606] [57:26.96] don't worry about performance till the
[L1607] [57:28.00] end, right? Like there's it's completely
[L1608] [57:29.60] different, right? Those are two
[L1609] [57:30.56] different engineering approaches. Uh and
[L1610] [57:33.12] so what I try to do is encourage people
[L1611] [57:36.64] to put that analysis back in, understand
[L1612] [57:39.28] the performance trade-offs you're
[L1613] [57:40.48] making, understand how much it might
[L1614] [57:42.80] cost in the future to like make these
[L1615] [57:45.04] fixes. And I I don't really do any AI
[L1616] [57:48.88] stuff, but my sort of feeling is more so
[L1617] [57:52.40] now than ever, I feel like that's got to
[L1618] [57:54.08] be pretty important because you're
[L1619] [57:55.44] instructing these AIs to do what they're
[L1620] [57:57.92] going to do. And I feel like it would be
[L1621] [58:01.36] a bad idea to not know about performance
[L1622] [58:04.48] trade-offs because especially if an AI
[L1623] [58:07.20] is going to be doing your bidding and
[L1624] [58:09.36] structuring the code the way you want to
[L1625] [58:10.80] structure it or doing whatever. It seems
[L1626] [58:12.88] like a very straightforward part of the
[L1627] [58:14.08] process to include performance stuff in
[L1628] [58:16.88] those instructions, right? Like that
[L1629] [58:18.40] would be a natural thing that we would
[L1630] [58:19.68] want to understand and do, right? So I
[L1631] [58:21.92] feel like
[L1632] [58:23.76] really I've been just trying to get that
[L1633] [58:25.04] more into the conversation. Uh, and I
[L1634] [58:27.92] feel like it's it's as relevant now as
[L1635] [58:29.84] it ever was, and arguably maybe more so.
[L1636] [58:31.68] I don't know, but I could be wrong about
[L1637] [58:32.96] that.
[L1638] [58:34.00] >> What are some things that are in your
[L1639] [58:36.24] mind, they're those high value
[L1640] [58:39.20] performance things to consider that
[L1641] [58:41.04] don't cost a whole lot to think about?
[L1642] [58:43.68] >> So, to me, awareness is the number one
[L1643] [58:46.80] thing, right? Understanding roughly the
[L1644] [58:49.44] performance characteristics of the
[L1645] [58:51.44] hardware that you're working on. Uh,
[L1646] [58:53.12] which includes things like, you know, if
[L1647] [58:54.48] there's a network, like what does that
[L1648] [58:55.76] look like? and so on. Um, it's really
[L1649] [58:59.28] about awareness more than anything else
[L1650] [59:01.84] because a little bit of awareness can go
[L1651] [59:05.84] a very long way. If you understand the
[L1652] [59:08.96] basic concept that like you know a that
[L1653] [59:12.32] network latency versus network
[L1654] [59:14.16] throughput are different things, you can
[L1655] [59:16.40] make upfront decisions about structuring
[L1656] [59:18.48] code such that you batch things properly
[L1657] [59:21.28] uh and so on and so forth. If you don't
[L1658] [59:23.12] understand those things, you could get
[L1659] [59:24.40] very far down a project only to realize
[L1660] [59:27.20] that everything you designed and all the
[L1661] [59:29.36] way it works is all very serial and
[L1662] [59:31.44] really just cannot be accelerated over a
[L1663] [59:33.28] network at all. Like it's never going to
[L1664] [59:34.80] run uh reasonably or something like
[L1665] [59:36.56] this, right? Uh and so I think the the
[L1666] [59:40.56] lowest hanging fruit is just to get some
[L1667] [59:42.96] education in performance. like get some
[L1668] [59:45.28] education in how to think about the way
[L1669] [59:49.36] a machine works and what makes it fast
[L1670] [59:51.60] or slow, what it struggles with and what
[L1671] [59:53.36] it doesn't and just to keep that in the
[L1672] [59:55.68] back of your head because at the end of
[L1673] [59:58.00] the day, if you have that knowledge, I
[L1674] [01:00:00.24] think you're very unlikely to make the
[L1675] [01:00:02.32] kinds of architectural decisions that
[L1676] [01:00:04.72] will be hard to undo later, right?
[L1677] [01:00:08.00] Um, and so that's really that's really
