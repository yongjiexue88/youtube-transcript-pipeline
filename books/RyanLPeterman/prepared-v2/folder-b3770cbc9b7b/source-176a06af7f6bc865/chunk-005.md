Chunk 5; segments 1482–1863. Start may repeat the previous chunk for context.

# The Co-Creator of Kubernetes: Engineering-Led Direction and Convincing Management | Brendan Burns

Source ID: source-176a06af7f6bc865
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/The_Co-Creator_of_Kubernetes_Engineering-Led_Direction_and_Convincing_Management_Brendan_Burns_en.txt
Video: https://www.youtube.com/watch?v=FKijpCEH9D8

[L1491] [47:39.76] leadership, and so they didn't
[L1492] [47:41.00] necessarily grow up in those
[L1493] [47:42.12] communities. And if you grow up in
[L1494] [47:43.28] finance, it's hard to explain like
[L1495] [47:45.32] what's the value of contributing to the
[L1496] [47:47.40] I mean, the value of taking the open
[L1497] [47:48.96] source is very clear, right? It's free.
[L1498] [47:51.32] Um but the value of contributing back,
[L1499] [47:53.96] it's harder to explain. And
[L1500] [47:55.76] um or legally, like I've we ran into
[L1501] [47:58.04] people even today. It's getting better I
[L1502] [48:00.12] think but like even today I've run into
[L1503] [48:01.96] people who say like we would really love
[L1504] [48:03.60] to contribute.
[L1505] [48:05.00] Our engineering leadership is aligned
[L1506] [48:07.28] that we would want to contribute. But
[L1507] [48:09.88] our legal team is worried that if we
[L1508] [48:11.76] contribute we'll be liable if we
[L1509] [48:13.56] introduce bugs.
[L1510] [48:15.96] Right? So like if
[L1511] [48:17.52] >> Would someone sue them or?
[L1512] [48:18.84] >> Yeah, I think that's what they're
[L1513] [48:19.60] worried about. I I don't it doesn't hold
[L1514] [48:21.56] water legally and I think the Linux
[L1515] [48:23.20] Foundation can give you plenty of like
[L1516] [48:26.12] case law and things like that to show
[L1517] [48:27.88] why it doesn't hold water.
[L1518] [48:29.84] Um
[L1519] [48:30.96] but sometimes that's enough to block
[L1520] [48:34.00] uh
[L1521] [48:34.72] someone from contributing.
[L1522] [48:36.68] Okay?
[L1523] [48:37.08] >> I I never thought someone would get sued
[L1524] [48:39.52] for adding a bug. I mean everyone adds
[L1525] [48:42.00] bugs on accident.
[L1526] [48:44.36] >> Well, but I mean but on the other hand
[L1527] [48:46.00] like if you write a proprietary piece of
[L1528] [48:47.76] software and you sell it to somebody and
[L1529] [48:49.16] it has a bug and it causes your house to
[L1530] [48:50.76] burn down. Like you can imagine you're
[L1531] [48:53.08] going to sue the you're going to sue the
[L1532] [48:54.32] people, right? So like
[L1533] [48:56.08] it is sort of a legit worry at some
[L1534] [48:58.24] level of like if I wrote the JPEG open
[L1535] [49:01.08] source JPEG library that ended up in the
[L1536] [49:02.84] smoke detector that caused the house
[L1537] [49:04.36] Yeah, like
[L1538] [49:06.00] you can sort of imagine the chain of
[L1539] [49:07.76] logic that gets you there. I don't think
[L1540] [49:09.12] it's true. I don't think it would hold
[L1541] [49:10.64] up. I think a lot of the licenses, you
[L1542] [49:12.84] know, a lot of the
[L1543] [49:14.24] open source licenses include
[L1544] [49:16.00] indemnification language that basically
[L1545] [49:18.52] says
[L1546] [49:19.60] if you use this you're using it under
[L1547] [49:21.40] your own risk and like you can't sue us
[L1548] [49:23.36] if it burns down your house. Um
[L1549] [49:26.28] but
[L1550] [49:27.52] I think that that's a worry for I mean
[L1551] [49:29.12] what I've heard No, I don't think. I've
[L1552] [49:30.24] heard from people that that that that
[L1553] [49:32.24] their companies do have that worry. Um
[L1554] [49:34.92] and again in some sense it's because
[L1555] [49:36.20] they're like well, what's the value?
[L1556] [49:39.32] If I see this potential risk and I don't
[L1557] [49:41.32] necessarily see the value. And I mean
[L1558] [49:43.24] and like also like again if it's not a
[L1559] [49:44.80] core thing, if you're not a tech
[L1560] [49:46.32] company,
[L1561] [49:47.64] you know, is that developer really
[L1562] [49:49.12] capable of like arguing with legal
[L1563] [49:51.60] arguing with legal about what you can
[L1564] [49:53.40] and can't do. Yeah, probably not, right?
[L1565] [49:55.36] Like they're probably just going to fade
[L1566] [49:56.36] away, right?
[L1567] [49:57.72] Um so, you know, there's that aspect
[L1568] [50:00.20] too.
[L1569] [50:01.24] >> I remember this is many years ago, I
[L1570] [50:04.16] read this blog post that OpenAI put out
[L1571] [50:06.52] before I think OpenAI was kind of huge
[L1572] [50:09.36] and it says, "Here's how we scaled
[L1573] [50:11.20] Kubernetes to 7,500 nodes or something
[L1574] [50:14.72] crazy." I forgot exactly
[L1575] [50:15.60] >> On ours, yeah.
[L1576] [50:16.80] >> Yeah, yeah.
[L1577] [50:18.32] And so, I I I want to know um you know,
[L1578] [50:21.88] there's this new
[L1579] [50:23.52] these new workloads coming in for AI.
[L1580] [50:25.72] There's training, which is this huge I
[L1581] [50:29.00] guess all at once workload and then
[L1582] [50:30.96] there's inference, which is latency
[L1583] [50:32.72] sensitive and
[L1584] [50:34.36] you kind of need it to to come out
[L1585] [50:35.92] instantly. I guess how does how has
[L1586] [50:38.44] Kubernetes adjusted over the years to
[L1587] [50:40.84] handle these kinds of workloads?
[L1588] [50:43.60] >> Yeah, I mean, I remember when you know,
[L1589] [50:45.28] like we couldn't really handle more than
[L1590] [50:47.12] about 100 uh more than about 100 nodes.
[L1591] [50:49.76] So,
[L1592] [50:51.12] uh it's definitely been a lot of
[L1593] [50:52.88] optimization in the in the core systems
[L1594] [50:56.00] and there's places where the
[L1595] [50:58.08] APIs were pretty noisy.
[L1596] [51:00.24] Um and we needed to reduce the noise
[L1597] [51:04.28] level or we needed to extract
[L1598] [51:07.28] components into in another component so
[L1599] [51:09.12] that you could scale etcd in particular
[L1600] [51:10.80] actually is one of the could be the main
[L1601] [51:12.68] bottleneck to that kind of scale. And
[L1602] [51:14.76] so, figuring out how to run etcd really
[L1603] [51:16.56] well is a core part of figuring out how
[L1604] [51:18.88] to run Kubernetes really well at scale.
[L1605] [51:21.64] Um
[L1606] [51:23.44] I I mean, I don't think it's that
[L1607] [51:24.40] different than like learning how to run
[L1608] [51:25.56] a database or anything else like that at
[L1609] [51:27.04] scale. Like large scale is just weird
[L1610] [51:29.12] and you just have to
[L1611] [51:31.16] you know, run it, see where it breaks,
[L1612] [51:33.92] figure out how to fix it, or well, rinse
[L1613] [51:36.36] and repeat, you know. Um
[L1614] [51:39.20] And uh I do think what's interesting is
[L1615] [51:41.96] that while, you know, AI training as an
[L1616] [51:44.44] example is is a really large large
[L1617] [51:46.84] cluster or scale kind of thing. Um
[L1618] [51:50.48] you know, I think by virtue of being in
[L1619] [51:51.56] the cloud, a lot of our users actually
[L1620] [51:53.44] have much much smaller clusters.
[L1621] [51:55.60] But lots of them.
[L1622] [51:57.20] Right? So, hundreds or thousands of
[L1623] [51:59.24] clusters where each cluster itself is a
[L1624] [52:01.20] little bit smaller.
[L1625] [52:02.68] Um and I think that's not something we
[L1626] [52:04.84] anticipated cuz we came from a world of
[L1627] [52:06.72] like physical data centers where
[L1628] [52:09.68] you know, you only want one because like
[L1629] [52:11.40] you don't want to have to set it up a
[L1630] [52:12.44] bunch of times, right? You just want to
[L1631] [52:13.92] set one up for the entire data center,
[L1632] [52:15.48] call it a day. Um but because of the
[L1633] [52:17.88] cloud, because AKS you know, you press a
[L1634] [52:20.28] button
[L1635] [52:21.32] pops up in 2 minutes, right? Like it's
[L1636] [52:23.28] really easy to get yourself a cluster.
[L1637] [52:25.08] So, people create lots of clusters. Um
[L1638] [52:28.24] and and so I think we've also invested a
[L1639] [52:30.28] lot in the Kubernetes community and in
[L1640] [52:32.48] Azure as well on um managing lots of
[L1641] [52:36.32] clusters. How do I manage clusters at
[L1642] [52:38.40] scale? Um
[L1643] [52:40.08] you know, I think one of the jokes we
[L1644] [52:41.76] sort of like we spent a lot of time
[L1645] [52:43.72] talking about containers as replacing
[L1646] [52:45.44] snowflake servers.
[L1647] [52:47.44] Not snowflake the company, but like you
[L1648] [52:49.00] know, specially handcrafted servers.
[L1649] [52:52.24] Um
[L1650] [52:53.68] and now we just have a bunch of
[L1651] [52:55.20] snowflake clusters. So, the VMs all look
[L1652] [52:57.32] the same, but the clusters are all
[L1653] [52:58.72] weird. So, like we have to
[L1654] [53:00.28] provide people with tools to make sure
[L1655] [53:01.80] that the monitoring software is the same
[L1656] [53:03.20] on all of them and that the you know,
[L1657] [53:05.24] all of the Kubernetes versions are the
[L1658] [53:06.60] same and like you know, all this admin
[L1659] [53:09.24] users are the same and like all this
[L1660] [53:10.92] kind of stuff, right?
[L1661] [53:12.36] Um so, that's another aspect of scale
[L1662] [53:14.24] out that I think we didn't anticipate
[L1663] [53:15.88] that we had to go and and build, which
[L1664] [53:18.00] is num number of clusters as opposed to
[L1665] [53:20.52] size of cluster.
[L1666] [53:22.04] >> I always hear in the news that I mean,
[L1667] [53:24.32] this the anticipated scale is even
[L1668] [53:27.04] higher than today's unprecedented scale.
[L1669] [53:30.36] And I see people are purchasing GPUs
[L1670] [53:33.72] like crazy.
[L1671] [53:35.20] I'm curious, is there any upper bound
[L1672] [53:37.04] where Kubernetes just
[L1673] [53:39.08] it cannot handle that that um
[L1674] [53:42.32] that load? Like, let's say you you 10x
[L1675] [53:44.76] it from where it is today.
[L1676] [53:46.80] Is it Is it going to break down at some
[L1677] [53:49.20] point and you need something more
[L1678] [53:50.24] custom?
[L1679] [53:51.28] >> Uh well, I mean, I think it all comes
[L1680] [53:52.60] down It all comes back to the to the to
[L1681] [53:54.76] the storage layer that cuz everything
[L1682] [53:57.00] again cuz there was this design decision
[L1683] [53:59.36] that everything routes around the um
[L1684] [54:02.68] the storage layer.
[L1685] [54:04.32] Um everything else is basically
[L1686] [54:06.60] horizontally scalable. So, you you have
[L1687] [54:09.56] more API requests coming in from more
[L1688] [54:11.20] nodes, well, you just need more API
[L1689] [54:12.56] servers.
[L1690] [54:13.64] Um you know, you want to do scheduling
[L1691] [54:15.72] faster, well, you need to just have more
[L1692] [54:18.24] schedulers.
[L1693] [54:19.36] Um
[L1694] [54:21.20] so everything else more or less you can
[L1695] [54:22.88] just horizontally scale out.
[L1696] [54:25.04] Um
[L1697] [54:26.48] it's the it's it's the storage layer
[L1698] [54:28.48] that is the is the the bottleneck. Um
[L1699] [54:31.76] and that's where the work comes. And so,
[L1700] [54:33.32] you want to say go 10x up, well, you're
[L1701] [54:34.80] going to have to probably figure out um
[L1702] [54:37.84] if you can make etcd scale that way or
[L1703] [54:39.68] if you need to replace etcd with
[L1704] [54:41.08] something else that has the same
[L1705] [54:42.04] characteristics but can operate at
[L1706] [54:43.96] scale. Um
[L1707] [54:45.84] So, so I don't think there's anything
[L1708] [54:47.20] like inherent in the design that would
[L1709] [54:49.72] prevent it. Um but obviously
[L1710] [54:52.64] you know, there's a famous quote that
[L1711] [54:54.68] that every time you change an order of
[L1712] [54:56.20] magnitude, the problem moves. Um and so,
[L1713] [54:58.72] I think that's really true. Is every
[L1714] [55:00.08] time you increase by an order of
[L1715] [55:01.04] magnitude, what you thought was the main
[L1716] [55:02.96] problem is going to become easy and then
[L1717] [55:05.60] like the problem moves somewhere else.
[L1718] [55:07.64] So, you were never constrained, now
[L1719] [55:08.92] you're CPU constrained. You were never
[L1720] [55:10.20] constrained, now you're network
[L1721] [55:11.40] constrained.
[L1722] [55:12.24] >> Yeah, that'll be cool to watch how I
[L1723] [55:14.00] mean, cuz it seems like everyone wants
[L1724] [55:15.64] to
[L1725] [55:16.24] >> Yeah, I think it's definitely it's
[L1726] [55:17.20] definitely the case that people continue
[L1727] [55:18.44] to try and push the limits of scale. Um
[L1728] [55:21.32] and uh
[L1729] [55:23.20] but I think like anything else, like
[L1730] [55:24.68] when there's motivation
[L1731] [55:26.40] people go and figure it out.
[L1732] [55:28.36] All right, as long as there's not
[L1733] [55:29.24] something inherent in the design.
[L1734] [55:31.20] >> But the last part of this conversation,
[L1735] [55:32.56] I just wanted to reflect over your
[L1736] [55:34.56] career a a bit and maybe ask you a few
[L1737] [55:36.40] questions about things, and
[L1738] [55:39.16] uh you mentioned that you had a PhD in
[L1739] [55:40.84] robotics, and I hear a lot of people say
[L1740] [55:43.56] they don't recommend PhDs. Some people
[L1741] [55:45.52] do. I'm curious what your take on on
[L1742] [55:47.88] getting a PhD is.
[L1743] [55:49.12] >> Yeah, that's probably like like if I had
[L1744] [55:51.04] to have a top 10 questions or top five
[L1745] [55:52.88] questions that people ask me, uh that's
[L1746] [55:54.92] definitely in the top five top 10
[L1747] [55:56.32] questions. Um and I guess I'll I'll I'll
[L1748] [55:59.32] answer it with two different stories.
[L1749] [56:01.60] Um
[L1750] [56:02.32] one story is that uh
[L1751] [56:05.04] at one point in my career I ran into a
[L1752] [56:08.12] guy at same company, this guy who I went
[L1753] [56:10.88] to undergrad with.
[L1754] [56:12.52] Um and he'd gone off and done startups,
[L1755] [56:15.64] and you know, done the tech industry
[L1756] [56:17.56] thing, and ended up in the same company
[L1757] [56:19.44] that I was working at. And I'd gone off
[L1758] [56:21.16] and done my PhD, and come back into the
[L1759] [56:23.20] industry, and and we were the exact same
[L1760] [56:25.20] level. We graduated the exact same year,
[L1761] [56:27.12] same degree, and we were at the exact
[L1762] [56:29.08] same level in this company. And so I
[L1763] [56:31.68] guess that's one way of me saying like,
[L1764] [56:33.40] "Eh?"
[L1765] [56:34.88] You know, like it probably doesn't
[L1766] [56:36.16] matter. It probably doesn't matter one
[L1767] [56:37.64] way or the other. Um
[L1768] [56:40.92] but I'll also turn it around and say,
[L1769] [56:43.24] "A, I had a lot of fun."
[L1770] [56:45.24] Right? So like I had a lot of fun doing
[L1771] [56:47.12] a PhD in robotics. So
[L1772] [56:49.24] that's worth it to me. Um
[L1773] [56:52.44] and then two, I think I learned a lot
[L1774] [56:55.52] about how to um I think from the PhD and
[L1775] [56:59.28] my PhD advisor, I learned a lot about
[L1776] [57:01.16] how to write and put my ideas forth in
[L1777] [57:04.20] both written and presentation form.
[L1778] [57:07.68] That you don't necessarily learn in the
[L1779] [57:09.00] industry.
[L1780] [57:10.20] Um and I think that benefited me. I
[L1781] [57:11.92] think I benefited my ability to, you
[L1782] [57:14.52] know, argue We talked about that
[L1783] [57:15.92] six-month period where we were arguing
[L1784] [57:17.60] for like why we should be allowed to
[L1785] [57:19.36] open source this thing.
[L1786] [57:20.88] Um
[L1787] [57:21.44] I think the thing The skills I learned
[L1788] [57:22.88] in terms of presentation and in terms of
[L1789] [57:24.60] writing
[L1790] [57:25.72] um benefited me uh during that time. Uh
[L1791] [57:29.60] and have continued to benefit me.
[L1792] [57:31.72] Um
[L1793] [57:32.52] and and then I think
[L1794] [57:34.36] you know, when I went out as a professor
[L1795] [57:35.76] for a couple of years, um teaching CS
[L1796] [57:38.76] 101 and having to like explain stuff to
[L1797] [57:41.12] students who didn't really know anything
[L1798] [57:42.72] about computers,
[L1799] [57:44.04] um
[L1800] [57:45.40] I think really helped me organize the
[L1801] [57:48.12] the in the initial parts of the
[L1802] [57:50.20] Kubernetes project so that somebody
[L1803] [57:51.44] could learn about Kubernetes cuz people
[L1804] [57:52.76] were coming in and being like, "What is
[L1805] [57:54.16] a container? What is orchestration? How
[L1806] [57:55.64] do I do this?" Like there's a lot of
[L1807] [57:57.36] like just teaching that you had to do.
[L1808] [57:59.44] And and I think that experience as a
[L1809] [58:00.96] professor thinking about how do I teach
[L1810] [58:03.08] students something really helped me do a
[L1811] [58:05.84] good job um
[L1812] [58:07.48] with you know, teaching Kubernetes to
[L1813] [58:09.32] people. Um and so I think those things
[L1814] [58:11.88] were really beneficial. And so I guess
[L1815] [58:13.40] there's there's you know, the two
[L1816] [58:14.32] different arguments which is one is like
[L1817] [58:17.84] it doesn't matter. The other is I
[L1818] [58:19.16] learned a ton of stuff that I think was
[L1819] [58:20.88] pretty useful to my career.
[L1820] [58:22.72] Um and I had some fun.
[L1821] [58:24.84] >> Earlier you said uh top questions that
[L1822] [58:27.16] people ask you and I'm kind of curious,
[L1823] [58:29.20] what's the top question?
[L1824] [58:31.28] >> I think the one the other one that I get
[L1825] [58:33.60] a lot um
[L1826] [58:35.44] is uh
[L1827] [58:37.28] how do I know what I should learn?
[L1828] [58:39.72] Like a lot of a lot of especially when I
[L1829] [58:41.20] talk to the interns for the first couple
[L1830] [58:43.00] of years,
[L1831] [58:44.40] you know, a lot of the questions are
[L1832] [58:45.44] right revolving around like "AI seems
[L1833] [58:47.68] really hot right now, but I'm really
[L1834] [58:49.04] interested in systems. Like should I
[L1835] [58:51.12] like go learn AI cuz it's hot or should
[L1836] [58:53.20] I learn systems cuz I think systems are
[L1837] [58:55.52] interesting?" Actually kind of don't
[L1838] [58:57.12] care what you learn. I care that you're
[L1839] [58:58.88] learning.
[L1840] [59:00.04] Um and and so the most important thing
[L1841] [59:03.00] is to find something that you're excited
[L1842] [59:04.40] about and energized about
[L1843] [59:06.48] um because you know, you'll do that
[L1844] [59:09.04] instead of watching YouTube. Uh
[L1845] [59:11.12] you know, so if you're not excited about
[L1846] [59:12.32] AI, like well, you're probably not going
[L1847] [59:14.28] to do a very good job learning AI. Which
[L1848] [59:16.76] means that you're kind of going to waste
[L1849] [59:17.92] your time.
[L1850] [59:19.16] Um but if you're really excited about
[L1851] [59:21.00] systems, you probably put a lot of
[L1852] [59:22.60] passion and energy into it. And you
[L1853] [59:24.80] know, we still need systems engineers.
[L1854] [59:26.24] Like so,
[L1855] [59:28.16] um
[L1856] [59:29.12] I you know, I think that's the that's
[L1857] [59:31.04] kind of a pretty popular question. I
[L1858] [59:33.00] think there's a lot of I I sense anyway
[L1859] [59:35.24] a lot of like
[L1860] [59:36.64] fear [snorts] of making the wrong
[L1861] [59:37.92] decision.
[L1862] [59:39.88] And,
[L1863] [59:41.56] uh
[L1864] [59:42.24] I will tell everybody like there was no
[L1865] [59:43.44] plan.
[L1866] [59:44.56] I've never had a plan for my career.
[L1867] [59:46.28] Like, never ever ever.
[L1868] [59:48.28] Like, I've always just chased after
[L1869] [59:50.04] things that I thought were useful and or
[L1870] [59:51.52] fun and interesting.
[L1871] [59:53.64] Um
[L1872] [59:54.72] and
