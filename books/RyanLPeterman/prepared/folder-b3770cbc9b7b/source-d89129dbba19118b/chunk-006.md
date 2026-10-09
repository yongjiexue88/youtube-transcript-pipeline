Chunk 6; segments 1558–1889. Start may repeat the previous chunk for context.

# OpenAI Codex Tech Lead: How His Career Grew And How He Uses Codex | Michael Bolin

Source ID: source-d89129dbba19118b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/OpenAI_Codex_Tech_Lead_How_His_Career_Grew_And_How_He_Uses_Codex_Michael_Bolin_en.txt
Video: https://www.youtube.com/watch?v=hN5ZFzWFhhg

[L1567] [56:40.64] get through these PRs faster, which is
[L1568] [56:42.48] good because there was a lot more review
[L1569] [56:44.40] to do.
[L1570] [56:45.28] >> That's I mean that's amazing. I feel
[L1571] [56:46.80] like and 50% of diffs have like you know
[L1572] [56:51.36] almost blank the test plan says you know
[L1573] [56:55.28] >> uh I don't know arc build or whatever
[L1574] [56:56.88] the oh I know but [laughter]
[L1575] [57:00.40] >> um I want to talk about the the the
[L1576] [57:03.12] codec cli that's that's open source why
[L1577] [57:06.48] is it open source
[L1578] [57:08.96] you know for something that's that
[L1579] [57:11.60] critical to like what's going on on your
[L1580] [57:14.00] machine right like that that like that's
[L1581] [57:16.64] one of the aspects of open source is
[L1582] [57:18.08] that I'm not you know the most um
[L1583] [57:21.28] zealous about this sort of thing but I
[L1584] [57:22.88] but I I sympathize with it this idea
[L1585] [57:24.48] that like hey you're going to put this
[L1586] [57:26.72] thing on my machine I care about what
[L1587] [57:29.52] it's doing right and I think in this
[L1588] [57:30.88] domain in particular it's really
[L1589] [57:32.56] important that people can look at it you
[L1590] [57:35.28] know and have have an idea of what it's
[L1591] [57:37.36] doing um because you know people have a
[L1592] [57:39.44] lot of questions about AI agents and
[L1593] [57:41.92] that sort of thing um and so I think I
[L1594] [57:45.92] think this this this
[L1595] [57:48.16] area this domain I think it's actually
[L1596] [57:49.76] really important um and also we um you
[L1597] [57:53.52] know we have gotten a lot of uh I think
[L1598] [57:56.00] like great compriations and bug reports
[L1599] [57:58.16] and things like that that we um would
[L1600] [58:00.72] have missed out on um and and and then
[L1601] [58:03.44] also I think it's you know um just you
[L1602] [58:06.32] know sharing with the world with like
[L1603] [58:07.92] how this is done um so we do it through
[L1604] [58:09.76] code right I've I've put out um one blog
[L1605] [58:12.48] post about how the agent loop works like
[L1606] [58:14.40] there is plan to do more of that. I'm
[L1607] [58:15.92] actually excited to. It's just, you
[L1608] [58:17.12] know, just it's just time is this liming
[L1609] [58:19.68] factor.
[L1610] [58:21.20] >> Really, not
[L1611] [58:22.16] >> Yeah. It was funny because I had I had I
[L1612] [58:25.20] had two candidates who came through and
[L1613] [58:26.64] one's like he's like, "Hey, I wrote it,
[L1614] [58:28.00] right?" I was like, "No, no, I I
[L1615] [58:29.53] [snorts] wrote it." And another person
[L1616] [58:30.80] came in. He's like, "Oh, you can tell
[L1617] [58:32.00] that that you know that you did not
[L1618] [58:34.08] outsource the
[L1619] [58:35.36] >> Okay, good. Right. I was like, oh, thank
[L1620] [58:36.64] you." You know? Um, so yeah,
[L1621] [58:38.56] >> you mentioned the blog post. How does
[L1622] [58:40.48] Codeex find what is available to it in
[L1623] [58:43.20] its environment? And when I'm running
[L1624] [58:45.12] these things, I'll see it's kind of
[L1625] [58:47.60] amazing. It's thinking to itself and
[L1626] [58:49.52] like discovering all these things in in
[L1627] [58:51.76] my uh terminal. So yeah, how does that
[L1628] [58:54.64] typically work?
[L1629] [58:55.52] >> Yeah, I mean there's, you know, there's
[L1630] [58:56.72] a few. I mean there's obviously what is
[L1631] [58:58.88] you know when Codex is based training
[L1632] [59:00.40] like it loves to use rip grip. It uses
[L1633] [59:01.84] rip grip very well to find all sorts of
[L1634] [59:04.00] things. Um, and then there's, you know,
[L1635] [59:06.40] if you have your agents MD file and
[L1636] [59:07.92] you're say, hey, in this repo, like
[L1637] [59:09.52] these tools are really important, right?
[L1638] [59:11.60] You should use these, right? Or the
[L1639] [59:13.04] readmemes or whatever. Um, or uh
[L1640] [59:16.80] obviously if you use MCP and you
[L1641] [59:19.52] associate these MCP servers with your
[L1642] [59:22.08] um, you know, where you're working on,
[L1643] [59:23.52] right, that that that um injects the set
[L1644] [59:26.64] of tool definitions like at the start of
[L1645] [59:29.04] the the conversation, right? So then uh
[L1646] [59:32.16] that kind of Yeah. So that's that's not
[L1647] [59:34.16] even like discovery on Codex's part,
[L1648] [59:36.08] right? It's kind of just like put front
[L1649] [59:37.68] and center there. I see. So some of it's
[L1650] [59:39.60] the harness explicitly throwing that
[L1651] [59:42.72] into the context
[L1652] [59:44.16] >> and then there is a big chunk though
[L1653] [59:46.00] where the model is just doing all the
[L1654] [59:47.84] heavy lifting of finding things. Is that
[L1655] [59:49.84] right?
[L1656] [59:50.16] >> Yeah.
[L1657] [59:50.64] >> Kind of like reflecting over your
[L1658] [59:52.16] career. The breadth and depth of your
[L1659] [59:55.20] work if we look across all of it. I mean
[L1660] [59:57.44] it's it's insane. you were your
[L1661] [59:59.44] javascript front end then you have all
[L1662] [01:00:01.76] these dev tool you know build fuzzy file
[L1663] [01:00:04.48] search you know virtual now you're
[L1664] [01:00:06.64] working on codecs you I'm sure you had
[L1665] [01:00:09.68] to uh continue your engineering educa
[L1666] [01:00:12.16] education to kind of get through all
[L1667] [01:00:14.08] these projects what are the top
[L1668] [01:00:16.64] technical books that have helped you
[L1669] [01:00:18.96] educate yourself
[L1670] [01:00:20.24] >> yeah I mean um you know so one was this
[L1671] [01:00:23.92] uh this book on operating systems um
[L1672] [01:00:26.88] it's like a thousand pages or something
[L1673] [01:00:28.96] like this. Uh it's the Addison Wesley
[L1674] [01:00:31.68] book. I'm trying the author, but it was
[L1675] [01:00:33.28] funny because I was when I was working
[L1676] [01:00:35.44] on the virtual file system. So I had
[L1677] [01:00:37.44] actually gotten to that point in my
[L1678] [01:00:39.04] career without ever writing C like
[L1679] [01:00:41.44] undergrad like it was like more
[L1680] [01:00:42.80] theoretical like we just never had to
[L1681] [01:00:44.88] touch it. And then yet I'm like working
[L1682] [01:00:46.64] on a virtual file system project and
[L1683] [01:00:48.56] then like very low operating system.
[L1684] [01:00:50.64] That's why I was, you know, joke that I
[L1685] [01:00:51.92] was kind of the worst engineer of the
[L1686] [01:00:53.12] project. And, you know, and someone said
[L1687] [01:00:55.76] something and I realized I was like, I
[L1688] [01:00:57.76] don't know what they're talking about.
[L1689] [01:00:59.20] This is kind of embarrassing. And I was
[L1690] [01:01:01.20] just like, you know, what book do I have
[L1691] [01:01:02.96] to read? And I think my manager, Aaron
[L1692] [01:01:04.80] Kushner at the time was like, he's like,
[L1693] [01:01:06.00] well, there's this thousandpage book.
[L1694] [01:01:07.20] And I was like, done. So, I bought it,
[L1695] [01:01:10.48] read the thing cover to cover. I like
[L1696] [01:01:12.08] took it to Hawaii with me. I took it
[L1697] [01:01:13.44] everywhere until I finished it. It's
[L1698] [01:01:15.12] it's kind of amazing and sad or weird
[L1699] [01:01:17.44] that like how um how far many of us can
[L1700] [01:01:21.20] get like in software engineering without
[L1701] [01:01:22.96] really having a clue how computers work.
[L1702] [01:01:24.88] Like there's just so many of those
[L1703] [01:01:26.72] levels of abstraction. Um but you know
[L1704] [01:01:29.92] one hand it's very freeing and then on
[L1705] [01:01:31.60] the other hand it's a little bananas.
[L1706] [01:01:33.52] And I think that um what I would say to
[L1707] [01:01:35.52] people right now is um is you know
[L1708] [01:01:41.04] actively trying to go like deeper
[L1709] [01:01:42.72] through the layers and understand these
[L1710] [01:01:44.48] things. Um and uh like cuz many times I
[L1711] [01:01:50.64] saw other people do it and now I can do
[L1712] [01:01:52.40] it is that there are problems some other
[L1713] [01:01:54.24] people could solve that I couldn't solve
[L1714] [01:01:55.92] because I just didn't know that like
[L1715] [01:01:58.08] there was this croft between these two
[L1716] [01:01:59.68] layers and if you got rid of it, right,
[L1717] [01:02:00.96] you get like a 10x improvement or
[L1718] [01:02:02.40] something like that, right? If you if
[L1719] [01:02:04.00] you're just operating so high up, you
[L1720] [01:02:05.44] don't really know, you know, what you
[L1721] [01:02:06.72] can what you can break down. um you know
[L1722] [01:02:09.68] so that um and so in terms of books like
[L1723] [01:02:12.32] uh I've enjoyed the like the O'Reilly uh
[L1724] [01:02:14.24] the Rust books um I you know big fan of
[L1725] [01:02:16.80] Rust um I think but they're also like
[L1726] [01:02:18.96] well written um and and thorough and
[L1727] [01:02:22.08] then honestly another thing I've been
[L1728] [01:02:24.08] telling people um that's not in the book
[L1729] [01:02:26.72] category but probably more fun and I
[L1730] [01:02:29.12] learned a lot uh actually um are um
[L1731] [01:02:32.72] these CTFs are like capture the flag
[L1732] [01:02:35.28] like security type competitions And
[L1733] [01:02:38.40] just, you know, it helps with like kind
[L1734] [01:02:40.00] of like adversarial mindset. it helps
[L1735] [01:02:42.32] with I think uh they're usually just
[L1736] [01:02:44.80] like it's like a it's like a dicath like
[L1737] [01:02:47.28] a computer dicathlon I feel like right
[L1738] [01:02:48.96] because like like there'll be multiple
[L1739] [01:02:50.64] challenges and maybe this one you need
[L1740] [01:02:52.56] to like understand assembly and this one
[L1741] [01:02:54.24] you need to understand like what
[L1742] [01:02:56.08] someone's like janky PHP admin pages do
[L1743] [01:02:59.92] all this sort of thing and it and it
[L1744] [01:03:01.68] just forces this um breadth on you uh in
[L1745] [01:03:06.08] a way that's kind of hard to to generate
[L1746] [01:03:08.72] otherwise and it's also you know just
[L1747] [01:03:10.56] more fun because it's like a game and
[L1748] [01:03:12.00] that sort of thing.
[L1749] [01:03:12.72] >> Can you give some context on what CTF
[L1750] [01:03:14.88] is? Yeah. So, it's it's it can be a
[L1751] [01:03:17.44] number of things, but uh it's it's
[L1752] [01:03:18.88] usually a competition usually in like
[L1753] [01:03:20.56] the infosc the security domain and
[L1754] [01:03:23.60] there'll be a set of uh there's like the
[L1755] [01:03:26.24] Jeopardy style one which is like there's
[L1756] [01:03:27.68] a bunch of challenges um and like you
[L1757] [01:03:30.96] know designed like crafted ahead of time
[L1758] [01:03:33.44] and they all have point values
[L1759] [01:03:34.80] associated with them and so you know
[L1760] [01:03:37.12] there's usually some fixed amount of
[L1761] [01:03:38.40] time and it could be individual it could
[L1762] [01:03:39.76] be with a team and you're trying to
[L1763] [01:03:41.84] solve these things and and there's a
[L1764] [01:03:44.16] flag there's always like a secret, you
[L1765] [01:03:46.32] know, um, piece of text um, in there
[L1766] [01:03:49.68] that usually has some format. And the
[L1767] [01:03:52.40] way is that you basically if you can
[L1768] [01:03:54.16] discover the secret piece of text, that
[L1769] [01:03:55.68] means that you have the the challenge is
[L1770] [01:03:58.24] set up that you would only have gotten
[L1771] [01:03:59.44] that if you had figured out, you know,
[L1772] [01:04:00.56] reverse engineered or whatever you were
[L1773] [01:04:02.08] supposed to do and then you get submit
[L1774] [01:04:03.44] that piece of text and that's your, you
[L1775] [01:04:05.28] know, token to demonstrate that you had
[L1776] [01:04:06.80] solved the challenge. And so it could be
[L1777] [01:04:08.08] like a race to like solve everything
[L1778] [01:04:10.24] first or get the most points in a
[L1779] [01:04:11.60] certain amount of time or different
[L1780] [01:04:12.80] things like that. So it's like it's kind
[L1781] [01:04:14.56] of like an escape room but in your
[L1782] [01:04:16.56] terminal you use only computers to
[L1783] [01:04:18.72] figure everything out.
[L1784] [01:04:19.76] >> Yes.
[L1785] [01:04:20.48] >> I see. Okay. And your recommendation is
[L1786] [01:04:22.88] people who want to become better
[L1787] [01:04:25.12] engineers they should invest in doing
[L1788] [01:04:28.08] some of these CTF because they make you
[L1789] [01:04:29.84] solve problems that make you a better
[L1790] [01:04:31.20] engineer.
[L1791] [01:04:31.92] >> Yeah. and you know and then you you know
[L1792] [01:04:33.60] also develop skills and things that you
[L1793] [01:04:35.52] just wouldn't have you know if you're
[L1794] [01:04:36.72] just like a you know writing react every
[L1795] [01:04:38.72] day like you're probably not going to
[L1796] [01:04:41.12] like open up GDB and like reverse a you
[L1797] [01:04:43.92] know a tic-tac-toe game but like I did
[L1798] [01:04:45.68] that because of you know a CTF challenge
[L1799] [01:04:47.68] was to do you know exactly that
[L1800] [01:04:49.76] >> right
[L1801] [01:04:50.48] >> um and but then it's like but then I
[L1802] [01:04:52.56] learned how to use GDB and like and and
[L1803] [01:04:55.04] then then you start you know when you're
[L1804] [01:04:57.04] faced with other problems you're like oh
[L1805] [01:04:58.40] my my just toolkit of of ways to solve
[L1806] [01:05:00.96] things is just much broader broader a
[L1807] [01:05:03.04] lot of people especially earlier in
[L1808] [01:05:04.80] their career they see the power of
[L1809] [01:05:07.52] codeex doing everything for them in the
[L1810] [01:05:10.40] terminal and I just imagine them saying
[L1811] [01:05:12.48] oh well I don't need to learn GDB
[L1812] [01:05:14.24] because uh Codex knows it so
[L1813] [01:05:17.44] >> um would what would your advice be given
[L1814] [01:05:19.92] the landscape of these AI tools for
[L1815] [01:05:22.08] people thinking about their engineering
[L1816] [01:05:23.68] education
[L1817] [01:05:24.56] >> yeah no that's I mean I think everyone's
[L1818] [01:05:26.40] like struggling to answer that uh
[L1819] [01:05:28.32] question right now um I do think about
[L1820] [01:05:31.12] it you a a lot and I I don't have a
[L1821] [01:05:33.44] great answer. I I I kind of personally
[L1822] [01:05:35.52] come back to my thing about like
[L1823] [01:05:38.40] um I still think like trying to
[L1824] [01:05:41.60] forcefully kind of go through the levels
[L1825] [01:05:43.20] of of abstraction and just understand um
[L1826] [01:05:46.96] you know more like at a deeper level how
[L1827] [01:05:48.96] things work um is going to be important.
[L1828] [01:05:51.44] I mean I think this will change. I'm
[L1829] [01:05:53.60] sure this will change over time, but
[L1830] [01:05:54.80] right now it's still kind of like,
[L1831] [01:05:57.68] you know, the questions that you asked
[L1832] [01:06:00.08] the agent is going to affect the quality
[L1833] [01:06:02.00] of the thing that you get out, right?
[L1834] [01:06:04.16] So, if you're not asking the right
[L1835] [01:06:05.60] questions, you're not maybe going to get
[L1836] [01:06:07.60] the best engineering solution out the
[L1837] [01:06:09.44] other side. You know, as things go on,
[L1838] [01:06:11.92] perhaps that will also be, you know,
[L1839] [01:06:14.48] another layer that's removed. I mean, I
[L1840] [01:06:16.00] think, you know, that's certainly where
[L1841] [01:06:16.88] we're going. I don't know what time
[L1842] [01:06:18.08] frame we'll get there. things do seem to
[L1843] [01:06:19.36] be happening faster than we expect. But
[L1844] [01:06:22.16] um
[L1845] [01:06:23.68] yeah, I think in general, but
[L1846] [01:06:27.20] learning how to ask what the right
[L1847] [01:06:28.56] question is and I and I haven't, you
[L1848] [01:06:30.64] know, for myself even like totally
[L1849] [01:06:32.16] pinned down what that means for for
[L1850] [01:06:33.84] someone who's like starting out new,
[L1851] [01:06:35.28] right? You fortunately have experience
[L1852] [01:06:37.36] to to fall back on or like that's where
[L1853] [01:06:39.52] that that that taste or that um
[L1854] [01:06:43.28] intuition of what to ask has has
[L1855] [01:06:45.20] developed. But, you know, if you're if
[L1856] [01:06:46.80] you're starting out, um, I'm still not
[L1857] [01:06:49.68] sure yet. And it's also hard to say
[L1858] [01:06:51.20] because we we don't really know 100%
[L1859] [01:06:53.20] where everything's going.
[L1860] [01:06:54.96] >> Yeah. When you reflect over your career,
[L1861] [01:06:58.24] the expectations at these really high
[L1862] [01:07:00.40] levels is kind of crazy. I mean, it's
[L1863] [01:07:02.72] like already for most people, this E7 or
[L1864] [01:07:05.92] senior staff level is this unattainable
[L1865] [01:07:08.80] level of impact. So someone who gets
[L1866] [01:07:10.40] promoted to that level is thinking, I
[L1867] [01:07:12.88] gotta really work super hard now because
[L1868] [01:07:15.84] the bar is like up here.
[L1869] [01:07:18.16] >> And then you went two levels past that.
[L1870] [01:07:20.64] And so I I'm curious like in the
[L1871] [01:07:23.60] day-to-day now, what what are your
[L1872] [01:07:25.76] thoughts on these like crazy
[L1873] [01:07:27.60] expectations? Is it stressful for you?
[L1874] [01:07:30.08] I mean it never it was never not
[L1875] [01:07:32.88] stressful I think um for me because I
[L1876] [01:07:36.64] really I think also because I sat in
[L1877] [01:07:39.20] calibrations right and I um you know so
[L1878] [01:07:42.48] for a bunch of other people you know you
[L1879] [01:07:44.08] talk about their level you talk about
[L1880] [01:07:45.44] their impact and you know you wanted to
[L1881] [01:07:47.04] be really fair and have this integrity
[L1882] [01:07:49.44] around well this level means this thing
[L1883] [01:07:50.96] and this is the impact like that's what
[L1884] [01:07:52.32] it means all is that's what exceeds this
[L1885] [01:07:53.76] and then knowing that like then you're
[L1886] [01:07:55.52] you know playing it out in your mind
[L1887] [01:07:56.56] like well someone's sitting in my
[L1888] [01:07:57.76] calibration and talking about this thing
[L1889] [01:07:59.68] and they want to be fair, right? And and
[L1890] [01:08:02.08] it is a little scary like you know you
[L1891] [01:08:03.76] get to E8 and you're like oh you know
[L1892] [01:08:05.28] it's a D1 a director
[L1893] [01:08:07.28] >> and you're like how do I have as much
[L1894] [01:08:08.80] impact as a person who has maybe like
[L1895] [01:08:11.20] over a hundred people
[L1896] [01:08:12.96] >> in their or so that's hard a lot of
[L1897] [01:08:15.36] people do it again a lot of people who
[L1898] [01:08:17.84] are I see who do it do it more by
