Chunk 5; segments 1392–1745. Start may repeat the previous chunk for context.

# How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar

Source ID: source-cfa80c9b2999d9de
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/How_Anthropic_Builds_And_How_Engineering_Will_Change_Soon_Thariq_Shihipar_en.txt
Video: https://www.youtube.com/watch?v=2Kch3tWMnw8

[L1401] [48:03.72] on the order of I'd say more like a
[L1402] [48:05.52] hundred times more testing code than
[L1403] [48:07.92] you've ever had before. You know what I
[L1404] [48:09.36] mean? So like,
[L1405] [48:10.88] uh,
[L1406] [48:11.48] you should have
[L1407] [48:12.72] uh, fixtures for everything. You can
[L1408] [48:14.04] just pull production code and create
[L1409] [48:15.60] fixtures and mock-ups on the fly for for
[L1410] [48:17.72] databases. You can uh, have storybooks
[L1411] [48:20.52] for front-end and things like that. And
[L1412] [48:22.40] you can have all these different ways of
[L1413] [48:24.08] testing and verifying your code. And
[L1414] [48:25.92] that I think is really valuable for
[L1415] [48:27.36] maintainability, right? It's like um,
[L1416] [48:30.76] just having like all these ways of
[L1417] [48:32.52] verifying it.
[L1418] [48:33.84] Uh, and then uh, yeah, of course like
[L1419] [48:36.32] there's just like the human element of
[L1420] [48:37.76] like where do you want your code base to
[L1421] [48:40.40] go? If you know that's the case,
[L1422] [48:43.36] probably you start thinking about like,
[L1423] [48:45.16] you know, how you'd replay and undo and
[L1424] [48:47.04] redo becomes really important, right?
[L1425] [48:48.60] Like just like that sort of stuff. And
[L1426] [48:51.04] so the but if you're single player only,
[L1427] [48:53.60] that actually matters a little bit less.
[L1428] [48:56.12] You know, like you like the average user
[L1429] [48:58.48] is not going to undo a hundred times or
[L1430] [49:00.80] something, right? And so like, you know,
[L1431] [49:03.00] many like single player applications
[L1432] [49:05.40] undo stop working
[L1433] [49:07.32] pretty quickly. Like, you know, like
[L1434] [49:08.52] after like four or five times, right?
[L1435] [49:10.28] Um, just cuz it's not that important.
[L1436] [49:11.64] But in multiplayer, the ability to
[L1437] [49:13.32] compose different things together is
[L1438] [49:15.00] really important or compose different
[L1439] [49:16.56] operations together is really important.
[L1440] [49:17.80] And so, um,
[L1441] [49:19.44] that's just an example where like if you
[L1442] [49:21.04] know the direction of your code base,
[L1443] [49:22.28] there are things you care about and you
[L1444] [49:23.36] want the models to know. And uh, you
[L1445] [49:25.56] know, you can include that in your
[L1446] [49:26.44] skills. You can also just like
[L1447] [49:28.60] you know, like that's sort of what
[L1448] [49:29.92] maintainability means to me is like
[L1449] [49:31.76] having a vision for what your code base
[L1450] [49:33.12] is good at, where you're where you're
[L1451] [49:34.40] going, you know, keeping it in line.
[L1452] [49:37.52] Um, I do think the models are getting
[L1453] [49:38.88] better and better and better. And like
[L1454] [49:41.32] almost every code base probably I think
[L1455] [49:43.92] will have this moment where you're like,
[L1456] [49:45.24] do you just ask the model to rewrite all
[L1457] [49:47.60] of it? You know?
[L1458] [49:49.48] Um, and like because now you're like,
[L1459] [49:52.80] oh, like I can do it in the most
[L1460] [49:54.28] performant language. I can mix and match
[L1461] [49:57.32] like you know like there's not a reason
[L1462] [49:58.72] that every software in the world
[L1463] [50:00.56] shouldn't run in web assembly in the
[L1464] [50:02.16] browser. You know what I mean? There's
[L1465] [50:03.56] not a reason why
[L1466] [50:05.36] I don't know like your Xbox game can't
[L1467] [50:08.64] run in your browser actually, right?
[L1468] [50:09.96] Like the Xbox like the hardware like the
[L1469] [50:12.64] consoles are much weaker than your
[L1470] [50:14.68] average like MacBook right now. You know
[L1471] [50:16.84] what I mean? But it's just like the code
[L1472] [50:18.64] base, right? [snorts] Um but we could
[L1473] [50:21.64] like and and so I I think probably over
[L1474] [50:23.92] the next year or two like everyone's
[L1475] [50:25.76] going to need to think about that,
[L1476] [50:27.20] right?
[L1477] [50:28.32] And so I I don't think you want to spend
[L1478] [50:30.44] too much time
[L1479] [50:32.20] like worrying about maintainability in
[L1480] [50:34.20] this like way that might not matter
[L1481] [50:35.52] anymore. I'm not saying maintainability
[L1482] [50:37.00] doesn't matter. You just have to update
[L1483] [50:38.20] your mental model of like what does it
[L1484] [50:39.44] mean for like code to be maintainable,
[L1485] [50:42.20] you know?
[L1486] [50:43.92] >> I was talking to this friend um
[L1487] [50:46.48] who was saying that
[L1488] [50:48.20] he leaves tons and tons of tech debt
[L1489] [50:51.80] leaving around because the next you know
[L1490] [50:54.36] the next iteration why why waste time
[L1491] [50:56.44] fixing that now when the next iteration
[L1492] [50:58.56] of Fable's going to one shot all this
[L1493] [51:00.72] tech debt and refactor this for me. So
[L1494] [51:04.12] kind of funny.
[L1495] [51:05.40] >> Yeah, I I don't think that's completely
[L1496] [51:07.32] incorrect. It depends on the
[L1497] [51:09.28] circumstance, right? Like I think this
[L1498] [51:10.64] is also just a classic thing in
[L1499] [51:12.52] startups, right? Where you're like, you
[L1500] [51:14.52] know, even in normal human engineer you
[L1501] [51:16.48] always have this problem of like um
[L1502] [51:18.84] hey, do I refactor or do I do tech debt
[L1503] [51:21.36] or do I deliver more customer value?
[L1504] [51:23.44] Would refactoring help me deliver more
[L1505] [51:25.12] customer value right now? I do think
[L1506] [51:27.36] that like just generally I think you
[L1507] [51:29.28] should think on your projects on shorter
[L1508] [51:31.88] time scales. So you're like okay, how do
[L1509] [51:33.96] I deliver value over the next month or
[L1510] [51:35.96] two? And if you the project you're
[L1511] [51:37.88] talking about is delivering value over
[L1512] [51:39.80] six months or 12 months, you know, then
[L1513] [51:42.92] maybe yeah, maybe like wait for the next
[L1514] [51:44.88] model a little bit, you know, and then
[L1515] [51:46.44] like that like
[L1516] [51:48.64] just deliver value on like the short
[L1517] [51:50.36] time scale scale, make sure it's like,
[L1518] [51:52.56] you know, really good. And if the models
[L1519] [51:54.00] are not quite good
[L1520] [51:55.40] enough, like they might get there soon.
[L1521] [51:57.56] It depends very much on the like
[L1522] [51:58.96] specific case, right? But and I'm not
[L1523] [52:01.28] saying this is true of everything, but
[L1524] [52:02.60] like just something you should keep in
[L1525] [52:04.08] mind.
[L1526] [52:04.96] >> I've talked to some friends who work at
[L1527] [52:06.68] big tech companies like Google,
[L1528] [52:09.12] Facebook, those types of places.
[L1529] [52:11.16] And then they as they've become more and
[L1530] [52:14.28] more AI pilled, one thing that people
[L1531] [52:17.40] have noticed is there's a lot more
[L1532] [52:19.08] incidents or SEVs in in their usage.
[L1533] [52:22.64] And
[L1534] [52:23.68] it's natural in those organizations cuz
[L1535] [52:25.88] they they read the code less and there's
[L1536] [52:27.96] more code flying out. You know, what
[L1537] [52:30.04] countermeasures have worked really well
[L1538] [52:32.04] for Anthropic to prevent breakages given
[L1539] [52:36.04] that the code velocity is so much
[L1540] [52:37.40] higher?
[L1541] [52:38.36] >> Yeah, I I think this is something that
[L1542] [52:40.20] like is a byproduct of moving faster
[L1543] [52:43.40] sometimes and we have to figure it out.
[L1544] [52:45.00] Like I think that
[L1545] [52:46.96] uh you know,
[L1546] [52:48.20] I don't think our uptime is exactly
[L1547] [52:49.76] where we want it to be either, but also
[L1548] [52:52.24] as a company we're a little like almost
[L1549] [52:54.64] 6 years old I think around, right? So
[L1550] [52:56.32] it's like no company has grown this fast
[L1551] [52:58.96] before and a lot of that is because we
[L1552] [53:00.96] were enabled to like create more
[L1553] [53:02.08] products faster than ever before, right?
[L1554] [53:04.36] And so you can use Claude to make your
[L1555] [53:06.84] uptime better, right? And I think that
[L1556] [53:08.48] like the way we think about this is just
[L1557] [53:09.84] like really good what's the dream
[L1558] [53:12.40] testing environment, the dream like you
[L1559] [53:14.96] know, deployment environment. Like can
[L1560] [53:16.92] you like you know, take requests and
[L1561] [53:19.48] replay them across like, you know, mock
[L1562] [53:21.72] databases and fixtures across
[L1563] [53:23.28] everything? Can you chaos monkey
[L1564] [53:24.80] everything, you know?
[L1565] [53:26.96] >> In my personal workflows, I have so many
[L1566] [53:30.28] more custom random tools and scripts
[L1567] [53:33.60] that just make everything faster.
[L1568] [53:35.92] And just curious, you know, on your team
[L1569] [53:39.24] at Anthropic for instance, does everyone
[L1570] [53:41.92] have a set of
[L1571] [53:43.80] miscellaneous tools that help them,
[L1572] [53:46.64] you know, get random things done?
[L1573] [53:48.92] >> Yeah, everyone does for sure. Like I I
[L1574] [53:51.12] think
[L1575] [53:51.92] part of this is is the job. Like I think
[L1576] [53:54.00] that sometimes uh
[L1577] [53:56.08] what we try and do is we play around
[L1578] [53:57.48] with harnesses. Like sometimes some
[L1579] [53:58.96] people on the team build their own
[L1580] [54:00.00] harnesses for a little bit to figure out
[L1581] [54:02.48] like, "Oh, is this like useful or not?"
[L1582] [54:05.28] You know, and then they they figure out
[L1583] [54:06.56] if it works and if not, they like
[L1584] [54:08.00] integrate it, right? So, I think there's
[L1585] [54:09.68] like that's part of the job uh in some
[L1586] [54:12.12] ways. Um
[L1587] [54:13.80] I think like other examples of like sort
[L1588] [54:16.12] of like misc stuff people will do. A lot
[L1589] [54:18.84] of people will have like
[L1590] [54:20.16] uh unique Claude tag setups. I think
[L1591] [54:22.88] Claude tag is one of these things where
[L1592] [54:24.48] like, you know, you can have it like I
[L1593] [54:27.36] have it scheduled my calendar invites,
[L1594] [54:29.08] right? And so like if someone
[L1595] [54:30.72] wants to like schedule something with
[L1596] [54:32.00] me, then I'm just like, "Hey, you can
[L1597] [54:33.08] just like tag Claude here in this
[L1598] [54:34.44] channel and I'll accept whatever it like
[L1599] [54:36.96] puts on my calendar, you know what I
[L1600] [54:38.28] mean?" So, um I think there's like some
[L1601] [54:40.88] stuff like that. I know like a lot of
[L1602] [54:42.76] people use it for like email. I I think
[L1603] [54:45.00] that um
[L1604] [54:46.96] I've seen like some people do like
[L1605] [54:49.84] interesting like multi-Clauding sort of
[L1606] [54:51.84] like
[L1607] [54:52.84] tmuxing like setups, right? Like where
[L1608] [54:55.48] like what's the ideal scenario for you
[L1609] [54:57.48] to like display like 50 different Claude
[L1610] [55:00.00] codes and, you know, what's the best way
[L1611] [55:02.12] to for you to figure out what's going on
[L1612] [55:04.00] at any one time? So, um
[L1613] [55:06.84] yeah, I think there's a lot of different
[L1614] [55:08.80] ways and we're trying to make Claude
[L1615] [55:10.00] code more hackable as well so that like,
[L1616] [55:12.20] you know, more people can
[L1617] [55:14.32] uh sort of like even
[L1618] [55:16.60] uh make their own version of Claude code
[L1619] [55:18.76] like more different and everyone might
[L1620] [55:20.68] have their own little twist on it.
[L1621] [55:24.40] >> Your role at Anthropic's really
[L1622] [55:25.68] interesting cuz of the external
[L1623] [55:27.76] visibility that you have and um I think
[L1624] [55:30.96] a lot of people when they give career
[L1625] [55:32.84] advice,
[L1626] [55:34.20] visibility's a a good thing,
[L1627] [55:36.84] but they don't have this level of
[L1628] [55:38.32] external visibility. And so, do you
[L1629] [55:40.36] recommend to software engineers like
[L1630] [55:42.76] they should be posting on Twitter and X
[L1631] [55:45.04] and, you know, if so, what what advice
[L1632] [55:47.52] would you give in that sense?
[L1633] [55:49.24] >> Generally,
[L1634] [55:50.92] the thing I say to people that you
[L1635] [55:52.40] should share your work
[L1636] [55:54.56] externally as much as you can,
[L1637] [55:55.68] especially
[L1638] [55:56.88] um I think within certain companies like
[L1639] [55:59.84] you might not be able to, but like maybe
[L1640] [56:01.60] you have side projects or something like
[L1641] [56:03.16] that. I think just um before I joined
[L1642] [56:05.80] Anthropic, what I did was like I spent a
[L1643] [56:07.84] bunch of time working with different
[L1644] [56:09.64] companies, building stuff, and writing
[L1645] [56:11.52] about it, and talking about it. Um and
[L1646] [56:14.60] uh like this was really valuable cuz it
[L1647] [56:17.92] like increased my surface area of luck,
[L1648] [56:20.28] you know? And so, I think that like uh
[L1649] [56:24.88] it's really
[L1650] [56:26.56] like the bar is much lower than you
[L1651] [56:28.52] think. Like basically, whenever someone
[L1652] [56:29.96] asked me for advice, I'm like, "Okay,
[L1653] [56:31.88] I I'll I'll sit them down. I'll be like,
[L1654] [56:33.16] "I know statistically I I tell this
[L1655] [56:35.68] advice to a lot of people, and almost no
[L1656] [56:37.68] one does it. Um and everyone who's done
[L1657] [56:40.12] it is like either in a job that they're
[L1658] [56:42.24] pretty excited about or running their
[L1659] [56:43.60] own company.
[L1660] [56:45.04] Um
[L1661] [56:45.64] and there are reasons why you're not
[L1662] [56:46.76] going to want to do it, but like this is
[L1663] [56:48.32] it. Like I'm just going to tell you.
[L1664] [56:49.84] One, like I don't care about your
[L1665] [56:50.80] resume. Like like, you know, don't do
[L1666] [56:52.80] that. Um you have to choose like an
[L1667] [56:54.96] interesting project to work on. You have
[L1668] [56:56.72] to work really hard on it. You have to
[L1669] [56:58.24] like lock in, and then you have to ship
[L1670] [57:01.16] it and write about it. Like you have to
[L1671] [57:02.52] do it. You can't like There's going to
[L1672] [57:04.88] be so many reasons why you don't want
[L1673] [57:06.12] to. It's like not good enough yet, or
[L1674] [57:07.60] like you haven't like you think the
[L1675] [57:09.52] write-up is not very interesting or
[L1676] [57:10.96] something, but you have to do it, and
[L1677] [57:14.24] you can't get discouraged, you know?
[L1678] [57:15.84] Like maybe the first one might not work,
[L1679] [57:17.16] but you have to do it again. Um
[L1680] [57:19.60] and maybe Twitter is not the right
[L1681] [57:20.88] place. Maybe it's Reddit. Uh maybe
[L1682] [57:22.80] there's a specific Reddit or Hacker News
[L1683] [57:24.76] or something like that. Part of what
[L1684] [57:26.24] you're trying to do is you're just
[L1685] [57:27.00] trying to find people who like like what
[L1686] [57:28.88] you're doing, right? But I think that
[L1687] [57:30.76] like people in general want to really
[L1688] [57:35.00] like you know we since consume more
[L1689] [57:37.84] content than ever right and you know
[L1690] [57:39.68] this right like I think that like people
[L1691] [57:42.24] want really high quality content high
[L1692] [57:44.40] quality content as you know is a lot of
[L1693] [57:46.20] work and so I think going back to like
[L1694] [57:48.72] what we said before about like would you
[L1695] [57:50.92] show someone the prompt you did right
[L1696] [57:52.64] like I think a lot of times people are
[L1697] [57:54.40] like oh what's the shortcut like oh like
[L1698] [57:56.48] should I just ask Claude to manage my
[L1699] [57:58.28] Twitter account and is that how I like
[L1700] [58:00.04] grow and and I'm like no like like you
[L1701] [58:02.16] should not do that right like you have
[L1702] [58:03.48] to sort of engage authentically
[L1703] [58:06.16] you have to like post like you know do
[L1704] [58:08.36] good work and talk about it and I think
[L1705] [58:10.16] like build up networks and things like
[L1706] [58:12.40] that but I think that as long as that's
[L1707] [58:14.64] one of your goals and you try hard at it
[L1708] [58:16.96] I've been seeing anyone not succeed at
[L1709] [58:19.44] it but it is really hard it's kind of
[L1710] [58:21.40] like saying like oh I want to like go to
[L1711] [58:23.68] the gym every day or I want to like lose
[L1712] [58:25.68] weight or something you know like there
[L1713] [58:27.04] are simple things that you can do that
[L1714] [58:29.44] take a lot of discipline and are easy to
[L1715] [58:31.36] get discouraged with and
[L1716] [58:33.56] um
[L1717] [58:34.40] but like worth doing if you do it and I
[L1718] [58:36.12] think like posting or more specific more
[L1719] [58:38.60] specifically like writing about your
[L1720] [58:40.28] work is like I think really really
[L1721] [58:41.52] valuable.
[L1722] [58:42.52] >> You mentioned luck surface area. Do you
[L1723] [58:44.84] have an example that kind of illustrates
[L1724] [58:47.68] the value of expanding your luck surface
[L1725] [58:50.40] area?
[L1726] [58:52.20] >> Yeah I mean okay how did I get my job at
[L1727] [58:54.76] Anthropic? I did
[L1728] [58:57.56] a fellowship with a company called Good
[L1729] [58:59.68] Fire where I did like some applied
[L1730] [59:01.72] research and so they they're an
[L1731] [59:03.20] interpretability AI company and I was
[L1732] [59:05.72] trying to figure out like how do I use
[L1733] [59:06.92] interpretability to in like to make
[L1734] [59:08.68] better products and so I learned about
[L1735] [59:10.84] their research
[L1736] [59:12.56] and I uh like felt like I want to work
[L1737] [59:17.12] on a project and it was really important
[L1738] [59:19.44] for me to like share it and so like I
[L1739] [59:21.76] when I agreed to work with them I was
[L1740] [59:23.56] like that's my goal is I want to like
[L1741] [59:25.76] share what I'm building I think that's
[L1742] [59:27.72] good for you as well because good fire
[L1743] [59:29.36] is a startup and you know, people I want
[L1744] [59:31.56] they want people to learn about them.
[L1745] [59:33.56] And so this is what something I'm going
[L1746] [59:34.60] to do. So I built this like
[L1747] [59:35.92] interpretability visualization and I
[L1748] [59:38.16] shared about it. This is my first like
[L1749] [59:39.52] big post on Twitter but it was only 500
[L1750] [59:41.40] likes or something. Like at like now
[L1751] [59:43.52] like you know, that's like not very much
[L1752] [59:45.56] to me but like it's like back then it
[L1753] [59:46.84] was like a huge post and um several
[L1754] [59:49.72] people saw it and like some of them DM'd
