Chunk 5; segments 1505–1883. Start may repeat the previous chunk for context.

# AWS Distinguished Eng: Learning From 3000 Incidents And How Engineering Is Changing | Marc Brooker

Source ID: source-45044ebe79206044
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/AWS_Distinguished_Eng_Learning_From_3000_Incidents_And_How_Engineering_Is_Changing_Marc_Brooker_en.txt
Video: https://www.youtube.com/watch?v=u3GjIXP9N0s

[L1514] [55:06.80] new teams, new people, people ex- you
[L1515] [55:09.36] know,
[L1516] [55:10.16] or I want to share something with
[L1517] [55:11.48] customers or I want to share something
[L1518] [55:12.92] with the world. And so that's super
[L1519] [55:14.20] valuable.
[L1520] [55:15.56] Or I want to write down something so I
[L1521] [55:18.76] can think through a really difficult,
[L1522] [55:22.00] often one-way door kind of
[L1523] [55:24.76] un- hard to change technical decision or
[L1524] [55:28.40] API design decision.
[L1525] [55:30.36] And I'm not going to do that every time
[L1526] [55:33.00] I make a technical decision. It's not
[L1527] [55:34.64] worth it because a lot of those
[L1528] [55:35.84] technical decisions are either easy or
[L1529] [55:38.72] or not as critical or can be just be
[L1530] [55:40.44] taken back if we figure out they're
[L1531] [55:42.12] wrong.
[L1532] [55:43.48] But I am going to to spend my time that
[L1533] [55:45.76] way when there are key decisions to
[L1534] [55:49.48] make, when there are key
[L1535] [55:51.92] um
[L1536] [55:52.64] insights to to find.
[L1537] [55:56.12] And
[L1538] [55:57.84] I think, you know, and so
[L1539] [56:00.56] it is that like what is the purpose of
[L1540] [56:02.40] writing?
[L1541] [56:03.56] Uh that
[L1542] [56:04.92] uh is that that separates
[L1543] [56:06.92] well-spent time from
[L1544] [56:09.68] poorly spent time.
[L1545] [56:11.68] Now, there are people who still don't
[L1546] [56:13.28] like writing even when it's well-spent
[L1547] [56:15.16] time, even when it's like
[L1548] [56:17.80] you know, you have to explain this piece
[L1549] [56:19.72] of technology to, you know, to a future
[L1550] [56:21.96] team. Um
[L1551] [56:23.88] I think that's a skill worth developing.
[L1552] [56:25.72] You know, sometimes you you do need to,
[L1553] [56:27.76] you know, uh eat your vegetables, uh you
[L1554] [56:30.40] know, and it's it's it is a skill worth
[L1555] [56:32.36] getting good at.
[L1556] [56:33.96] Um
[L1557] [56:35.56] and you know, especially in
[L1558] [56:39.20] documenting the core kind of technical
[L1559] [56:41.52] decisions behind a design is is so
[L1560] [56:44.60] useful. And that's useful in two ways,
[L1561] [56:46.68] by the way. Like one of them is as we
[L1562] [56:49.16] think about building a big system,
[L1563] [56:51.32] um we make thousands of decisions. And
[L1564] [56:55.44] some of those decisions are very
[L1565] [56:57.96] carefully chosen, very particular, and
[L1566] [57:01.36] very impactful.
[L1567] [57:03.44] And some of those decisions are
[L1568] [57:06.08] the best thing we could guess in the
[L1569] [57:07.64] moment based on having no data to make
[L1570] [57:09.72] that decision.
[L1571] [57:11.24] And it's super useful for people who are
[L1572] [57:13.28] coming in to improve that system down
[L1573] [57:15.76] the line to be able to look at the
[L1574] [57:18.08] design and say which of these things
[L1575] [57:20.24] were very carefully chosen and thought
[L1576] [57:21.88] through, and which of these things were
[L1577] [57:23.72] arbitrary.
[L1578] [57:25.40] And because the arbitrary things like
[L1579] [57:27.56] okay, well, I'm going to change that and
[L1580] [57:29.20] I'm going to just go ahead and change
[L1581] [57:30.44] that cuz I have better data now. I've
[L1582] [57:32.00] watched the system run. I can go and
[L1583] [57:33.48] change those. And these other ones were
[L1584] [57:35.40] like, well, let me really engage with
[L1585] [57:37.36] the reason that we made this decision.
[L1586] [57:38.96] Maybe it was non-obvious. Maybe there
[L1587] [57:40.56] was some some more advanced thinking.
[L1588] [57:42.76] And so, being able to kind of understand
[L1589] [57:45.16] the amount of thought that went into a
[L1590] [57:47.00] decision is almost as important as
[L1591] [57:48.84] understanding what that thought was. You
[L1592] [57:51.40] had a really interesting blog post. This
[L1593] [57:53.32] was um
[L1594] [57:54.60] from a while back. It it's titled the
[L1595] [57:57.56] four hobbies and apparent expertise.
[L1596] [58:01.12] And you introduced this really
[L1597] [58:03.04] interesting idea. It's a 2 by 2 matrix.
[L1598] [58:05.64] And on one side, there's doing versus
[L1599] [58:08.68] discussing. And on the other side,
[L1600] [58:11.08] there's the hobby and the gear. Maybe I
[L1601] [58:13.88] can overlay it for people who want to
[L1602] [58:15.84] see. And then later you you kind of
[L1603] [58:17.52] liken that to your career and how I
[L1604] [58:20.56] guess maybe we can imagine the hobby is
[L1605] [58:23.00] is actually coding. And maybe the gear
[L1606] [58:25.48] is
[L1607] [58:26.44] let's just say it's like your dev setup
[L1608] [58:27.84] or something like that. You talked about
[L1609] [58:29.60] these two aspects of being in in
[L1610] [58:33.00] depending on which quadrant you are,
[L1611] [58:34.48] which is there's this trade-off between
[L1612] [58:36.76] expertise and visibility. Where imagine
[L1613] [58:39.92] you're really into coding and you're
[L1614] [58:41.52] really into doing, you're going to be
[L1615] [58:44.16] phenomenal in terms of expertise, but
[L1616] [58:47.12] maybe not as visible, cuz you're not
[L1617] [58:49.24] talking with everyone about how cool
[L1618] [58:51.64] your setup is and and all of that. And
[L1619] [58:54.40] on the flip side, if you're really into
[L1620] [58:56.80] the gear, or maybe your setup in this
[L1621] [58:58.88] case, and you're really into discussing,
[L1622] [59:01.04] you're you're on all the messaging posts
[L1623] [59:03.60] and that, you might not actually be that
[L1624] [59:05.40] good at at coding, but you're very
[L1625] [59:07.80] visible and you have this apparent
[L1626] [59:10.64] competence.
[L1627] [59:12.12] And I thought that trade-off was really
[L1628] [59:13.68] interesting, because I've seen that so
[L1629] [59:15.44] much in software engineering, too, is
[L1630] [59:17.32] there might be someone who's
[L1631] [59:19.04] really quiet coder. They never write
[L1632] [59:21.12] anything, but they know everything, cuz
[L1633] [59:23.92] they've just been in the weeds all the
[L1634] [59:25.92] time. And then there are people on the
[L1635] [59:28.00] complete opposite end of the spectrum
[L1636] [59:29.48] that writing all the time, speaking all
[L1637] [59:31.92] the time, but maybe not actually
[L1638] [59:34.12] practicing as much. And my question to
[L1639] [59:36.60] you is, how do you strike that balance?
[L1640] [59:38.40] Cuz obviously too far in either
[L1641] [59:39.96] direction is not optimal. So, how do you
[L1642] [59:42.72] strike that balance?
[L1643] [59:44.44] Yeah, that's uh you know, that's that's
[L1644] [59:46.72] something that I reflect on a on a lot.
[L1645] [59:49.28] Uh you know, and I do explicitly think
[L1646] [59:50.92] that sort of being 100% on either of
[L1647] [59:52.80] those ends is a is a is a is a failure
[L1648] [59:55.00] mode. And I think
[L1649] [59:56.60] you know, I I will say that
[L1650] [59:58.96] I have a lot more
[L1651] [01:00:01.72] personal enjoyment working with the
[L1652] [01:00:03.88] people that are 100% on the doing side
[L1653] [01:00:06.56] and and 0% on the talking side. I I I I
[L1654] [01:00:09.28] appreciate and and deeply you know,
[L1655] [01:00:11.28] deeply love their expertise. Um
[L1656] [01:00:14.68] but I I I do think that you know, they
[L1657] [01:00:16.48] they could have more impact and and and
[L1658] [01:00:18.64] leverage if if if they you know, swung a
[L1659] [01:00:20.76] little bit away from that. Um
[L1660] [01:00:23.08] you know, I I tend to not enjoy as much
[L1661] [01:00:25.88] interacting with the people who are 100%
[L1662] [01:00:27.92] on on on on the speaking side. Um
[L1663] [01:00:31.48] Uh but I I
[L1664] [01:00:33.40] and I think they would you know, have a
[L1665] [01:00:35.20] lot more
[L1666] [01:00:37.04] relevant things to say
[L1667] [01:00:39.44] you know, if if if they you know, swung
[L1668] [01:00:42.00] a little bit back towards the center.
[L1669] [01:00:45.56] The other challenge of being on a 100%
[L1670] [01:00:47.36] on the doing side is sort of gets back
[L1671] [01:00:48.92] to that, how do you find the really
[L1672] [01:00:50.28] important problems? And you know, if
[L1673] [01:00:52.48] your head's down in your IDE all day
[L1674] [01:00:56.08] you could very likely be working on the
[L1675] [01:00:58.36] wrong thing.
[L1676] [01:00:59.84] Um you know, something that that isn't
[L1677] [01:01:01.52] as as important, isn't as impactful. Um
[L1678] [01:01:05.52] you know, doesn't have these properties
[L1679] [01:01:06.88] that that people want. So, you know, how
[L1680] [01:01:09.24] how do you find the optimal balance? Uh
[L1681] [01:01:11.52] I don't have a have a recipe for you
[L1682] [01:01:13.80] know, what really is is optimal.
[L1683] [01:01:17.04] I tend to
[L1684] [01:01:19.56] do about let's say 75/25
[L1685] [01:01:23.20] kind of practitioner versus you know
[L1686] [01:01:25.52] teaching and and and and communicating.
[L1687] [01:01:28.28] Maybe 80/20 at times. I found that's
[L1688] [01:01:31.12] about what feels right for me. Um
[L1689] [01:01:36.04] I would say that, you know, the great
[L1690] [01:01:37.88] people I work with, you know, from sort
[L1691] [01:01:40.64] of 90/10 on that scale up to about 50/50
[L1692] [01:01:43.92] on that scale. I think, you know,
[L1693] [01:01:45.48] outside of those, you know, folks tend
[L1694] [01:01:47.64] to
[L1695] [01:01:48.76] um
[L1696] [01:01:50.00] you know, tend to get into trouble
[L1697] [01:01:52.16] um as practitioners, right? Like, you
[L1698] [01:01:54.16] know, there people whose job it is to
[L1699] [01:01:55.60] be, you know, communicators and and
[L1700] [01:01:57.44] that's great as long as they have the
[L1701] [01:01:58.68] curiosity and and are clear about what
[L1702] [01:02:00.88] they, you know, know and and and don't
[L1703] [01:02:02.68] know. Um
[L1704] [01:02:04.92] But you know, I found that sweet spot at
[L1705] [01:02:06.96] that sort of 75/25 point in in in my
[L1706] [01:02:10.36] career and and that's what's what's
[L1707] [01:02:12.44] worked for me. I think
[L1708] [01:02:15.12] um
[L1709] [01:02:16.32] And I I I think in this moment where
[L1710] [01:02:20.08] things are changing so fast, there's so
[L1711] [01:02:21.56] much to learn,
[L1712] [01:02:23.12] um you know, swinging a little bit more
[L1713] [01:02:25.28] towards the practitioner side, I think
[L1714] [01:02:27.08] generally will help people. But again,
[L1715] [01:02:29.36] you don't want to go too far that way
[L1716] [01:02:30.64] because then you lose the
[L1717] [01:02:32.52] um you know, what's important for you
[L1718] [01:02:34.92] that comes with interacting with the
[L1719] [01:02:36.40] outside world. On the doing versus
[L1720] [01:02:38.56] discussing axis, I I kind of view the
[L1721] [01:02:41.60] doing one as if you were too far, you
[L1722] [01:02:44.12] would be underrated. And if you were too
[L1723] [01:02:47.68] far at the discussing, you would be
[L1724] [01:02:50.08] overrated. Mhm. And
[L1725] [01:02:52.80] if for someone who's structuring their
[L1726] [01:02:54.84] career,
[L1727] [01:02:56.12] uh would you say it's better to be
[L1728] [01:02:58.16] overrated or underrated?
[L1729] [01:03:01.24] I think long-term, you know, if if
[L1730] [01:03:03.20] you're if you're using that terminology,
[L1731] [01:03:04.96] it's probably better to be underrated. I
[L1732] [01:03:07.08] think
[L1733] [01:03:08.16] you know, being
[L1734] [01:03:09.68] being overrated can feel great
[L1735] [01:03:12.12] in the moment, um but is rarely
[L1736] [01:03:14.76] sustainable.
[L1737] [01:03:16.40] Uh and and and really sort of gets you
[L1738] [01:03:19.16] where
[L1739] [01:03:20.72] to where you you you you need to be. I
[L1740] [01:03:23.16] really enjoy, you know,
[L1741] [01:03:25.52] uh,
[L1742] [01:03:27.04] you know, things like sports and and
[L1743] [01:03:28.80] and, you know, these sort of creative
[L1744] [01:03:30.36] hobbies and and, uh, you know, crafts
[L1745] [01:03:33.00] because it it it does,
[L1746] [01:03:35.20] you know, turn that, um,
[L1747] [01:03:37.60] let's say perception and reality
[L1748] [01:03:40.24] knob to to very much reality, right?
[L1749] [01:03:43.12] Like as a as a as a sports person, you
[L1750] [01:03:45.36] can't you can't fool the world for very
[L1751] [01:03:47.24] long. Uh, it it it very quickly becomes,
[L1752] [01:03:50.52] uh, you know, very obvious, you know,
[L1753] [01:03:51.96] who who can and who can't. Uh,
[L1754] [01:03:54.36] you know, I think as a as a crafts
[L1755] [01:03:55.84] person, the same, right? It it very
[L1756] [01:03:57.84] quickly becomes,
[L1757] [01:03:59.52] um,
[L1758] [01:04:00.20] obvious [clears throat] who who can and
[L1759] [01:04:01.32] who can't. And I think it takes a little
[L1760] [01:04:03.20] bit longer in a field like ours where
[L1761] [01:04:05.04] there always is so much kind of
[L1762] [01:04:06.84] qualitative stuff that goes on.
[L1763] [01:04:09.16] Um, but I think long-term when I look
[L1764] [01:04:11.12] at, you know, careers that I really
[L1765] [01:04:12.88] admire and people I really admire, uh,
[L1766] [01:04:15.80] they tend to be people who are
[L1767] [01:04:17.64] personally very honest about their level
[L1768] [01:04:20.68] of of knowledge and understanding and
[L1769] [01:04:22.36] skill.
[L1770] [01:04:23.64] So, people who walk the walk, not
[L1771] [01:04:26.44] necessarily talk the talk. I see. Yeah,
[L1772] [01:04:28.92] about engineers that you admire, I'd be
[L1773] [01:04:30.76] curious cuz you have worked at AWS and
[L1774] [01:04:33.76] for such a long time and you have seen
[L1775] [01:04:36.84] so many legendary engineers.
[L1776] [01:04:39.36] Who at AWS do you look up to and and
[L1777] [01:04:41.88] why?
[L1778] [01:04:43.56] Yeah, I mean, you know, just fantastic.
[L1779] [01:04:46.16] One of the blessings of working at a
[L1780] [01:04:47.40] place like AWS is I get to work with so
[L1781] [01:04:49.12] many great people. Um,
[L1782] [01:04:50.96] you know, maybe because he's retired,
[L1783] [01:04:53.20] I'll I'll I'll talk a little bit about
[L1784] [01:04:55.04] Al Vermeulen. Uh, was was one of the
[L1785] [01:04:57.08] sort of early engineers at AWS and,
[L1786] [01:04:59.68] um,
[L1787] [01:05:00.96] original,
[L1788] [01:05:02.64] say, huge contributor to the design of
[L1789] [01:05:05.08] S3, a really big contributor to the
[L1790] [01:05:07.20] design of a lot of a lot of our database
[L1791] [01:05:09.20] services over time.
[L1792] [01:05:11.20] Um, Al was actually the the CTO of
[L1793] [01:05:14.12] Amazon for a for a period of time when
[L1794] [01:05:16.12] he realized, I think,
[L1795] [01:05:17.80] that wasn't the job he wanted to do. Um,
[L1796] [01:05:20.96] but I, you know, what I really admired
[L1797] [01:05:24.08] about uh about Al from early in my
[L1798] [01:05:26.60] career is,
[L1799] [01:05:29.24] you know, very clearly he was somebody
[L1800] [01:05:31.76] who deeply understood the things he was
[L1801] [01:05:33.64] he was doing. And he could work in these
[L1802] [01:05:36.28] two modes, right? Like, you know, I I
[L1803] [01:05:38.64] have a great um memory of a sort of
[L1804] [01:05:42.68] 2010-ish, uh
[L1805] [01:05:44.64] you know, arguing with Al about some of
[L1806] [01:05:46.44] the edge cases in in the the Paxos
[L1807] [01:05:49.20] paper. And, you know, he was super deep
[L1808] [01:05:51.68] at that level, but could also get up to
[L1809] [01:05:53.44] the the really kind of executive level
[L1810] [01:05:55.44] and talk about, you know, cloud strategy
[L1811] [01:05:57.88] and the way we should be explaining
[L1812] [01:05:59.44] things to people and some of the, you
[L1813] [01:06:00.96] know, sort of fundamental things that we
[L1814] [01:06:02.68] need to be building.
[L1815] [01:06:04.12] Um,
[L1816] [01:06:05.44] and I really admired that ability to
[L1817] [01:06:07.40] work sort of almost at at at every
[L1818] [01:06:09.92] level. And I was like, "Wow, you know,
[L1819] [01:06:11.20] this is this is something I aspire to."
[L1820] [01:06:13.88] Um, and uh you know, want to model my
[L1821] [01:06:16.96] want to model my own career after.
[L1822] [01:06:19.88] Um,
[L1823] [01:06:21.92] and so, you know, that's I I think that
[L1824] [01:06:23.68] is uh you know, the kind of person I've
[L1825] [01:06:26.24] really, you know, really enjoyed working
[L1826] [01:06:29.00] with is is people who do have that, you
[L1827] [01:06:31.60] know, do have that breadth. Um,
[L1828] [01:06:34.32] and I think, you know, one of the other
[L1829] [01:06:35.64] things that is you know, really
[L1830] [01:06:39.04] admirable about a lot of these folks is,
[L1831] [01:06:41.76] you know, they
[L1832] [01:06:43.32] they don't want to be celebrities,
[L1833] [01:06:44.56] right? They they they want to do cool
[L1834] [01:06:46.12] work for, you know, have an impact, do
[L1835] [01:06:48.08] great stuff for customers, you know,
[L1836] [01:06:50.12] optimize for having impact. You know,
[L1837] [01:06:52.36] for people who want to continue their
[L1838] [01:06:54.28] engineering education and really remain
[L1839] [01:06:57.32] on top of things, deeply understand the
[L1840] [01:06:59.64] technology, do you have any top
[L1841] [01:07:02.28] technical book recommendations? You
[L1842] [01:07:04.36] know, anybody who's building distributed
[L1843] [01:07:06.48] system things, I I I highly recommend uh
[L1844] [01:07:10.28] Martin Kleppmann's book.
[L1845] [01:07:12.92] I think there's a second edition of that
[L1846] [01:07:14.68] coming out, you know, soon. Um
[L1847] [01:07:18.12] there's a new edition of quantitative
[L1848] [01:07:20.24] systems design book, which I also think
[L1849] [01:07:22.12] is is is great. Sorry, Hennessy and
[L1850] [01:07:24.24] Patterson's computer architecture book.
[L1851] [01:07:26.64] This this is a super super useful one
[L1852] [01:07:29.24] that covers a
[L1853] [01:07:30.52] ton of ground. I read a ton of you know,
[L1854] [01:07:33.56] fiction and and non-fiction and and
[L1855] [01:07:35.64] mostly papers when I'm reading technical
[L1856] [01:07:37.48] things I find you know, I find engaging
[L1857] [01:07:39.56] at that level you know, more more useful
[L1858] [01:07:41.96] for me.
[L1859] [01:07:43.36] And by the way, that's that's become way
[L1860] [01:07:45.20] more accessible now. You know, one of
[L1861] [01:07:47.68] the great ways to dive into a paper is
[L1862] [01:07:50.36] you know, hey
[L1863] [01:07:51.88] you know, hey Claude summarize this for
[L1864] [01:07:53.92] me and then then I can dive into it and
[L1865] [01:07:56.44] and and read you know, the author's
[L1866] [01:07:57.88] words and I I find that mode is great
[L1867] [01:08:00.40] and and this is super accessible for
[L1868] [01:08:02.04] people who haven't been able to read
[L1869] [01:08:04.12] papers in in the past. Um
[L1870] [01:08:08.92] but uh
[L1871] [01:08:11.48] you know, and then there's also a ton of
[L1872] [01:08:12.96] insight in in some really old stuff too.
[L1873] [01:08:16.20] Uh
[L1874] [01:08:16.80] for example
[L1875] [01:08:18.52] um
[L1876] [01:08:19.64] you know, some of the
[L1877] [01:08:22.28] algorithms that we used in in in Lambda
[L1878] [01:08:25.52] to to manage traffic and and manage
[L1879] [01:08:27.68] bursts of traffic come from Erlang's
[L1880] [01:08:29.96] work like a hundred years ago on on
[L1881] [01:08:32.00] managing telephone call centers
[L1882] [01:08:34.44] and and his book about that and um
[L1883] [01:08:38.16] and so you know, folks also shouldn't
[L1884] [01:08:40.04] think that oh well, the industry is
[L1885] [01:08:41.44] changing super fast and so I should only
[L1886] [01:08:43.20] read recent things like there's still
[L1887] [01:08:45.56] incredible insights in some of the you
[L1888] [01:08:48.08] know, older work
[L1889] [01:08:49.88] and in the foundations of
[L1890] [01:08:52.92] computing and infrastructure and and and
[L1891] [01:08:55.32] networking and and computer science that
[L1892] [01:08:57.48] there is um
