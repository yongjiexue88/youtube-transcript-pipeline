Chunk 5; segments 1401–1730. Start may repeat the previous chunk for context.

# Ex-Citadel Quant and AI Researcher: Breaking In, Tech vs Finance Careers | Nimit Sohoni

Source ID: source-bd9897a51211e805
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Ex-Citadel_Quant_and_AI_Researcher_Breaking_In,_Tech_vs_Finance_Careers_Nimit_Sohoni_en.txt
Video: https://www.youtube.com/watch?v=_jECS37M3dQ

[L1410] [47:04.72] basically interleave state space model
[L1411] [47:06.80] and transformer layers with you know
[L1412] [47:08.60] with some ratios. And so yeah Nvidia's
[L1413] [47:11.36] put out stuff like this even the Quinn
[L1414] [47:13.72] you know their latest Quinn models
[L1415] [47:15.16] follow this strategy as well. So yeah I
[L1416] [47:17.64] think the you know the cutting edge I
[L1417] [47:19.24] would say for for text is is probably in
[L1418] [47:22.04] these hybrid models at least in terms of
[L1419] [47:24.28] like what's what's out there for open
[L1420] [47:25.64] source.
[L1421] [47:26.64] But the interesting thing is that
[L1422] [47:28.60] you know for for other modalities like
[L1423] [47:30.04] audio it actually makes a lot of sense
[L1424] [47:32.60] to to have this compression as like a as
[L1425] [47:35.32] a explicit inductive bias. So using you
[L1426] [47:37.60] know SSMs
[L1427] [47:39.04] for for audio has proven you know very
[L1428] [47:41.24] useful for us. You know we found that it
[L1429] [47:43.12] actually improves performance. It's kind
[L1430] [47:45.48] of almost a free lunch you know you get
[L1431] [47:46.96] improved performance
[L1432] [47:48.84] improved quality and improved
[L1433] [47:50.20] performance at inference time. And the
[L1434] [47:52.08] reason is that sort of like
[L1435] [47:53.80] if you think about what these models are
[L1436] [47:55.56] doing you know
[L1437] [47:57.28] audio is you know depending on how you
[L1438] [47:59.44] represent it is a very like you know um
[L1439] [48:03.28] there's
[L1440] [48:05.32] there's very little information
[L1441] [48:06.56] contained in any one like you know time
[L1442] [48:08.64] step or token if you will of audio. It's
[L1443] [48:12.12] you know like a
[L1444] [48:13.56] frame of you know depending on what
[L1445] [48:15.44] you're doing like you know 10
[L1446] [48:16.44] milliseconds to 100 milliseconds. And so
[L1447] [48:19.20] you know one frame to the next doesn't
[L1448] [48:20.84] really vary that much and so you know
[L1449] [48:22.96] compressing these into you know sort of
[L1450] [48:25.24] fixed size state can actually like makes
[L1451] [48:27.88] a lot of sense as opposed to text which
[L1452] [48:29.52] is a much like sort of
[L1453] [48:31.52] densely informational modality. You know
[L1454] [48:33.76] one word to the next there is actually a
[L1455] [48:35.40] ton of
[L1456] [48:36.40] information contained in each of those
[L1457] [48:38.00] tokens. And so you know compression is
[L1458] [48:40.40] less
[L1459] [48:41.76] you know it's kind of already like
[L1460] [48:42.88] pre-compressed if if you're if you're
[L1461] [48:44.64] using a token level representation.
[L1462] [48:47.04] But but yeah even so I think you know
[L1463] [48:48.76] hybrid models I would say hybrid models
[L1464] [48:51.00] I think are are the future in in in that
[L1465] [48:53.56] regard.
[L1466] [48:54.96] I see okay. So it's because the modality
[L1467] [48:58.04] itself has I guess redundancy in the
[L1468] [49:01.00] data that means that this lossiness is
[L1469] [49:03.88] actually an asset rather than
[L1470] [49:06.84] a problem. Exactly. Yeah. So yeah I
[L1471] [49:10.16] think you know there's a lot of
[L1472] [49:11.32] interplay between modality and
[L1473] [49:13.36] architecture. It's definitely not
[L1474] [49:14.88] something you cannot design your
[L1475] [49:16.80] architecture independently of your data.
[L1476] [49:19.52] And so yeah kind of this like you know
[L1477] [49:21.44] co-design and like thinking about
[L1478] [49:23.88] you know modality multi-modality from a
[L1479] [49:25.96] fundamental level you know this is one
[L1480] [49:27.68] of you know the research problems that I
[L1481] [49:29.40] mentioned that like kind of drives
[L1482] [49:31.44] drives a lot of the work we do here.
[L1483] [49:33.24] When you think about companies that
[L1484] [49:35.72] focus on product versus research, what
[L1485] [49:39.36] pattern do you think is
[L1486] [49:41.44] most effective? Um so, I think, you
[L1487] [49:44.48] know, personally and and this is one of
[L1488] [49:46.32] you know, also one of the reasons I
[L1489] [49:48.00] decided to join Cartesia. I think it is
[L1490] [49:50.04] very important to have have both.
[L1491] [49:53.04] I think like so there are you know,
[L1492] [49:55.36] several startups popping out recently
[L1493] [49:57.48] that are really
[L1494] [49:59.20] you know, focused on core research and
[L1495] [50:00.68] not don't even necessarily have like an
[L1496] [50:03.16] idea how to productionize it or or turn
[L1497] [50:05.44] that into
[L1498] [50:06.72] you know, a product product or revenue
[L1499] [50:08.84] stream. Um I think like you know, I
[L1500] [50:11.44] personally am am fairly skeptical of
[L1501] [50:13.56] this approach. I think
[L1502] [50:15.28] you know, for a few reasons. I think
[L1503] [50:17.16] first of all, you know, you know, big
[L1504] [50:18.92] labs you know, have tons of resources
[L1505] [50:20.76] and also have you know, large teams
[L1506] [50:22.80] focused on this sort of thing. I think
[L1507] [50:25.56] um
[L1508] [50:26.32] Yeah, I think like
[L1509] [50:27.88] you know, ultimately the goal of a
[L1510] [50:29.00] company is to is to make money, right?
[L1511] [50:30.84] And so I think you know, eventually you
[L1512] [50:33.76] know, if you are if you are a company of
[L1513] [50:35.24] this form like you need to eventually
[L1514] [50:37.28] deliver like you know, massively
[L1515] [50:39.12] outsized returns you know, at some
[L1516] [50:41.12] point.
[L1517] [50:42.32] So I think you're you're taking a big
[L1518] [50:43.56] risk where it can kind of be all or
[L1519] [50:45.28] nothing type thing. Um I think the flip
[L1520] [50:48.00] side of it like a sort of product only
[L1521] [50:49.92] company that's built on AI models that
[L1522] [50:52.96] are built by other people. Um I think
[L1523] [50:55.56] that is like risky in the sense that you
[L1524] [50:57.68] don't have as much of a moat.
[L1525] [50:59.80] So you know,
[L1526] [51:01.64] like we saw this with you know,
[L1527] [51:04.56] initial chat GPT or you know, going from
[L1528] [51:06.96] GPT3 or GPT4, right? A lot of these
[L1529] [51:09.52] wrapper companies kind of just got made
[L1530] [51:11.40] obsolete by the fact that the base
[L1531] [51:12.84] models improved so much that they could
[L1532] [51:14.24] often just do what the wrapper was
[L1533] [51:16.72] trying to do
[L1534] [51:18.00] by by by themselves with without very
[L1535] [51:20.44] much scaffolding and so it became kind
[L1536] [51:22.56] of thing you can
[L1537] [51:24.08] just build build in-house rather than
[L1538] [51:26.76] needing another company to
[L1539] [51:28.88] you know, post process the output of
[L1540] [51:30.28] these outputs of these models. I think
[L1541] [51:32.56] like being in the intersection is
[L1542] [51:33.80] actually quite valuable for
[L1543] [51:36.36] you know, for many reasons. I think
[L1544] [51:38.40] having a product a real product that
[L1545] [51:40.24] customers use is something that can
[L1546] [51:42.04] drive the research. So you see firsthand
[L1547] [51:46.36] the issues
[L1548] [51:47.80] and you can use that to drive you know,
[L1549] [51:50.84] your next iteration of modeling you
[L1550] [51:52.80] know, try and fix these issues not as a
[L1551] [51:54.88] band-aid but like you know, from the
[L1552] [51:57.24] ground up right? Like from
[L1553] [51:59.52] at the model level itself. And so I
[L1554] [52:01.68] think having control over the models is
[L1555] [52:04.56] like very important when you're when
[L1556] [52:06.68] you're building an AI product. Um which
[L1557] [52:09.28] is not to say that like you know,
[L1558] [52:10.36] there's no room for any non-research
[L1559] [52:13.36] company. I think it just like
[L1560] [52:15.60] it has to be in the you know, right
[L1561] [52:17.92] right kind of right kind of space. Um
[L1562] [52:20.24] and so yeah, I think um
[L1563] [52:22.28] Cartesia has a great blend of research
[L1564] [52:23.80] and product. You know, we're very
[L1565] [52:25.84] I would say we're first and foremost a
[L1566] [52:27.08] product company. Uh but you know, we
[L1567] [52:30.04] want to build the best products we can
[L1568] [52:32.48] and we believe that that requires us to
[L1569] [52:34.52] actually solve some of these fundamental
[L1570] [52:36.12] research problems in order to do that.
[L1571] [52:38.56] I think there's a lot of people who want
[L1572] [52:40.60] to get into AI research. I mean I was
[L1573] [52:42.56] just talking with a friend today who's a
[L1574] [52:44.60] SWE and he's saying
[L1575] [52:46.80] I don't think software engineering is
[L1576] [52:48.00] going to be around in
[L1577] [52:50.16] 10 years or something like that. So he's
[L1578] [52:51.96] been investigating. And I'm curious, do
[L1579] [52:54.44] you have any advice for someone who is
[L1580] [52:56.96] technical and wants to move into AI
[L1581] [52:59.24] research?
[L1582] [53:00.60] My my philosophy has always been to try
[L1583] [53:02.52] and build up my technical skills as much
[L1584] [53:05.04] as possible. I think you're if you're if
[L1585] [53:07.20] your fundamentals are good enough like
[L1586] [53:09.04] you know, at some point
[L1587] [53:10.96] you know,
[L1588] [53:11.84] the opportunities will just come to you
[L1589] [53:13.48] rather than the other way around. And so
[L1590] [53:15.56] I would say just focus on getting as
[L1591] [53:17.72] good as you can at you know, at coding
[L1592] [53:20.72] at you know, AI read tons of papers.
[L1593] [53:23.36] Yeah, I think math skills and math
[L1594] [53:25.36] intuition are really important. And so
[L1595] [53:27.24] that's that's what I've kind of been
[L1596] [53:29.12] optimizing for um you know, ever since
[L1597] [53:32.40] undergrad when I realized what I wanted
[L1598] [53:34.04] to do was at least you know, some
[L1599] [53:35.72] combination of math and computer
[L1600] [53:36.92] science. And so I've always more focused
[L1601] [53:39.12] on like kind of building up those
[L1602] [53:40.52] fundamentals and I think that is the way
[L1603] [53:42.80] to get your foot in the door. I think
[L1604] [53:45.16] like bigger companies it can be a bit
[L1605] [53:47.20] harder to pivot you know, teams or what
[L1606] [53:50.24] you work on. And so
[L1607] [53:52.52] uh for for someone like that I think you
[L1608] [53:55.04] just switching like teams or companies
[L1609] [53:56.88] can can be like you know, sort of the
[L1610] [53:59.08] only path forward. I think you you can
[L1611] [54:00.84] kind of get siloed in a little bit if
[L1612] [54:03.04] you're at a bigger company sometimes. I
[L1613] [54:05.04] do think you know, some companies are
[L1614] [54:06.32] better about it and you know, I have
[L1615] [54:07.92] seen people transition from SWEs to
[L1616] [54:09.84] research and and and stuff like that.
[L1617] [54:12.48] Um so I think you know, this is one of
[L1618] [54:15.24] the areas where getting a sort of
[L1619] [54:17.44] qualification on your
[L1620] [54:19.52] resume can be useful like getting a you
[L1621] [54:21.60] know, a master's in AI at least or
[L1622] [54:23.16] something like that can help
[L1623] [54:25.80] when when you're looking to make a sort
[L1624] [54:27.36] of lateral career change like that.
[L1625] [54:29.92] You're you're saying there's kind of two
[L1626] [54:31.84] common paths. One would be get more
[L1627] [54:34.80] education and use that qualification to
[L1628] [54:37.20] kind of pivot directly into AI research
[L1629] [54:39.92] or go to a startup where you can kind of
[L1630] [54:43.52] like mold yourself into an AI research
[L1631] [54:45.96] role.
[L1632] [54:46.84] That's kind of right but I think even if
[L1633] [54:48.92] you want to go to a startup, right? And
[L1634] [54:50.60] you want to but you want to sort of
[L1635] [54:52.04] switch from a SWE track to AI track like
[L1636] [54:54.92] there's got to be some
[L1637] [54:56.84] there's got to be something behind it,
[L1638] [54:57.88] right? Like you have to have some
[L1639] [54:59.32] evidence of a skill set whether it's
[L1640] [55:01.68] like sort of
[L1641] [55:02.92] organically grown or from you know, from
[L1642] [55:06.52] from schooling.
[L1643] [55:08.08] But I think it can probably be a lot
[L1644] [55:10.16] easier to get your foot in the door if
[L1645] [55:11.56] you have some evidence of of it on your
[L1646] [55:13.92] resume. So like let's say you were
[L1647] [55:17.48] you hired at Cartesia and then that
[L1648] [55:20.48] person comes to you and he's like, hey,
[L1649] [55:22.88] I want to do more AI research. In that
[L1650] [55:26.12] case, is that something where it's like
[L1651] [55:28.56] just flip the switch and next project is
[L1652] [55:30.92] AI research project? This has actually
[L1653] [55:33.12] has actually happened you know, in
[L1654] [55:34.24] Cartesia itself. You know, we have had
[L1655] [55:35.84] people transition
[L1656] [55:37.44] roles like that. So I think it is
[L1657] [55:39.88] definitely easier at a startup which is
[L1658] [55:43.20] it can be a bit more flexible just cuz
[L1659] [55:45.24] you know, everyone kind of knows
[L1660] [55:46.88] everyone and so
[L1661] [55:48.88] you can get a sense of you know, whether
[L1662] [55:51.08] this might be an appropriate career
[L1663] [55:52.88] change just by like kind of knowing the
[L1664] [55:54.36] person for a while. And so yeah, I mean
[L1665] [55:56.36] we've actually done you know, people
[L1666] [55:58.40] have done this in in Cartesia with with
[L1667] [56:00.64] you know, a lot of success.
[L1668] [56:02.36] Do you have a biggest regret when you
[L1669] [56:04.56] look back on your whole career? I mean I
[L1670] [56:06.84] I think I often overthink things and I
[L1671] [56:08.52] think I have spent a lot of time
[L1672] [56:10.52] regretting you know, past decisions that
[L1673] [56:12.48] turned out not to matter in the end and
[L1674] [56:14.32] I kind of regret the amount of time I
[L1675] [56:15.76] spent regretting other things. So you
[L1676] [56:17.88] know, I try I try to learn from that
[L1677] [56:19.28] now. You know, I think like you know,
[L1678] [56:21.40] don't sweat the small stuff like you
[L1679] [56:22.96] know,
[L1680] [56:24.32] you know, minor setbacks happen and they
[L1681] [56:26.52] happen but I think uh you know,
[L1682] [56:29.68] there's a risk of
[L1683] [56:31.12] you know, putting too much stress on
[L1684] [56:32.60] yourself and you're like beating
[L1685] [56:33.76] yourself up and and stuff like that. And
[L1686] [56:36.28] those are just like not productive ways
[L1687] [56:38.12] to spend your time and they don't make
[L1688] [56:39.52] anyone feel good and so I think yeah, I
[L1689] [56:42.16] try and you know, I try not to regret
[L1690] [56:44.60] stuff because yeah, I think it's just
[L1691] [56:46.08] not not a super good use of time. If you
[L1692] [56:48.72] had to go back in time and you could
[L1693] [56:51.00] give yourself some advice when you're
[L1694] [56:52.60] just entering the industry, what would
[L1695] [56:55.32] you say? Focus on building the deep
[L1696] [56:57.72] technical skills.
[L1697] [56:59.44] Yeah, don't waste time with like sort of
[L1698] [57:01.76] trifling stuff or spreading your
[L1699] [57:03.84] yourself too thin. Um yeah, just like
[L1700] [57:07.28] focus on
[L1701] [57:08.68] what you want to focus on I guess like
[L1702] [57:10.20] basically like the the skills that you
[L1703] [57:12.20] want to leverage in your day job just
[L1704] [57:14.12] like do those and get good at those and
[L1705] [57:16.60] you know, that's that's that's where you
[L1706] [57:18.76] should spend all your time at work. Um
[L1707] [57:21.92] and
[L1708] [57:23.00] yeah.
[L1709] [57:23.92] You make it sound so simple.
[L1710] [57:26.72] Maybe it is.
[L1711] [57:27.40] >> it is it is a simple it's kind of a
[L1712] [57:29.32] simple recipe that's very hard to
[L1713] [57:30.64] follow, right? Like it's very hard to
[L1714] [57:32.04] maintain that discipline.
[L1715] [57:33.68] It's kind of like you know, um
[L1716] [57:36.20] you know, what's the secret to being
[L1717] [57:37.60] healthier? It's you know, exercising and
[L1718] [57:39.44] eating right and those are things that
[L1719] [57:40.92] are just very much easier said than
[L1720] [57:42.92] done.
[L1721] [57:44.20] But yeah, I think
[L1722] [57:45.88] it is it is that simple.
[L1723] [57:48.16] Awesome. Cool. Well, thanks so much for
[L1724] [57:50.40] your time, Amit. Thanks for listening to
[L1725] [57:52.72] the podcast. I don't sell anything or do
[L1726] [57:55.96] sponsorships but if you want to help out
[L1727] [57:58.48] with the podcast, you can support by
[L1728] [58:01.52] engaging with the content on YouTube or
[L1729] [58:04.16] on Spotify. If you want to drop a
[L1730] [58:05.64] review, that will be super helpful. And
[L1731] [58:07.92] if there's any guests that you want to
[L1732] [58:09.56] bring on to, please let me know. I feel
[L1733] [58:11.40] like sourcing very senior ICs, there's
[L1734] [58:14.44] no well-studied list out there on Google
[L1735] [58:17.72] that I can just search this up. So if
[L1736] [58:19.56] there's someone in your org or at your
[L1737] [58:21.04] company who you really look up to and
[L1738] [58:22.76] you want to hear their career story, let
[L1739] [58:24.92] me know and I'll reach out to them.
