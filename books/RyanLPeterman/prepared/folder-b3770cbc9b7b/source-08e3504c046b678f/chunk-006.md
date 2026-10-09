Chunk 6; segments 1634–1963. Start may repeat the previous chunk for context.

# Meta Senior Staff Eng (IC7): Zuck Stories, Rapid Career Growth, Code Machine Archetype

Source ID: source-08e3504c046b678f
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Meta_Senior_Staff_Eng_(IC7)_Zuck_Stories,_Rapid_Career_Growth,_Code_Machine_Archetype_en.txt
Video: https://www.youtube.com/watch?v=OzlK68kcuHc

[L1643] [01:01:24.48] revert the change from the code because
[L1644] [01:01:26.96] they didn't want to have to deal with
[L1645] [01:01:28.08] like merging that into their complex uh
[L1646] [01:01:30.64] change, right? Um and that's feedback to
[L1647] [01:01:33.68] be careful for that stuff like I would I
[L1648] [01:01:35.68] would didn't pay attention to that. So
[L1649] [01:01:36.96] it's like okay that is one one use case
[L1650] [01:01:39.44] where you got to be careful is if teams
[L1651] [01:01:40.96] are working on complex longer term thing
[L1652] [01:01:43.84] migrations already like be careful in
[L1653] [01:01:46.16] that area of the code.
[L1654] [01:01:47.36] >> What about the case of ownership? So,
[L1655] [01:01:50.96] you know, software isn't just about
[L1656] [01:01:53.76] creating it, but there's all this
[L1657] [01:01:55.68] management and maintenance burden after
[L1658] [01:01:58.00] it's created. Did any team get upset? I
[L1659] [01:02:01.12] said, "Hey, you add this feature, great,
[L1660] [01:02:02.80] but who's owning this thing now? Who's
[L1661] [01:02:05.68] going to actually maintain it?" That
[L1662] [01:02:08.32] didn't come up for me. And I don't know
[L1663] [01:02:10.48] if it's the philosophy. I don't know if
[L1664] [01:02:12.80] it's still the case, but the philosophy
[L1665] [01:02:14.88] back then was like every line of code
[L1666] [01:02:16.96] you wrote, you're responsible for. Um
[L1667] [01:02:19.60] Kent Beck talked about this recently
[L1668] [01:02:21.60] that yeah he was like it's a really
[L1669] [01:02:24.00] strong sense of ownership. So like if
[L1670] [01:02:25.92] you if you are okay being woken up at
[L1671] [01:02:29.52] 3:00 a.m. and you're going to respond
[L1672] [01:02:31.12] and fix some bug in your code any time
[L1673] [01:02:34.24] of the day anywhere then like do what
[L1674] [01:02:38.56] you want with like you know don't write
[L1675] [01:02:40.80] tests then go ahead as long as you're
[L1676] [01:02:43.52] maintaining it. If you don't want that
[L1677] [01:02:45.28] and you want to work nine to five, then
[L1678] [01:02:47.04] you might want to write more tests to
[L1679] [01:02:48.64] make sure that your code's stable when
[L1680] [01:02:51.04] you're not around. Um, so I think if I
[L1681] [01:02:53.36] like I I didn't just like touch code,
[L1682] [01:02:55.12] didn't refactor code and forget it. I
[L1683] [01:02:57.04] was responsible if there was any bugs
[L1684] [01:02:59.04] and then in the future like sometimes
[L1685] [01:03:01.92] two years later there's like something
[L1686] [01:03:03.60] that I get an automatic bug assigned to
[L1687] [01:03:06.48] me because it's like you touched this
[L1688] [01:03:07.84] code last and I'm like oh man, I don't
[L1689] [01:03:10.32] even remember doing this. Um, but then I
[L1690] [01:03:12.32] would fix the bug because even though I
[L1691] [01:03:14.08] didn't cause the bug, it was just like
[L1692] [01:03:15.36] that is now my code. Um, now I didn't I
[L1693] [01:03:18.00] didn't have any territorial conflicts
[L1694] [01:03:19.60] because I don't I don't know why I I
[L1695] [01:03:21.84] didn't I just didn't really come up. Um,
[L1696] [01:03:25.12] I never I didn't like step on people's
[L1697] [01:03:27.12] product
[L1698] [01:03:28.72] judgment. I mean, this is part of the
[L1699] [01:03:30.72] the judgment calls I guess that you're
[L1700] [01:03:32.40] building up. Like it it's kind of like
[L1701] [01:03:35.20] performing a surgery and you're not
[L1702] [01:03:36.72] really like you got to be really careful
[L1703] [01:03:38.80] about what you're changing. You don't
[L1704] [01:03:40.56] want to impact.
[L1705] [01:03:42.48] Like I said, I learned maybe learned the
[L1706] [01:03:44.24] hard way from making some mistakes early
[L1707] [01:03:45.84] on and being a bit too aggressive in
[L1708] [01:03:47.60] certain areas. Like you start to learn
[L1709] [01:03:49.68] where that line is between
[L1710] [01:03:52.32] um like messing up people's day-to-day
[L1711] [01:03:54.40] and
[L1712] [01:03:56.00] not and still getting the refactoring or
[L1713] [01:03:59.28] the cleanup done. One thing that I'm
[L1714] [01:04:01.60] curious about you, as you become a more
[L1715] [01:04:03.76] senior engineer, it's very common to get
[L1716] [01:04:05.76] pulled into more and more meetings.
[L1717] [01:04:09.76] miscellaneous overhead. How did you
[L1718] [01:04:12.64] manage your your focus as you got
[L1719] [01:04:14.56] promoted to be a coding machine? You
[L1720] [01:04:16.56] must have had a lot of focus time even
[L1721] [01:04:18.64] as IC7.
[L1722] [01:04:19.76] >> I really try to minimize my meetings. If
[L1723] [01:04:21.76] someone like just added I don't know if
[L1724] [01:04:23.44] this still happens, but people would
[L1725] [01:04:24.64] like just make meetings, add you to the
[L1726] [01:04:26.16] calendar, there's no context. It's just
[L1727] [01:04:27.84] like something something like sync.
[L1728] [01:04:30.96] You're like, I don't know what this is.
[L1729] [01:04:32.40] I like would ask like what is this? Um,
[L1730] [01:04:34.96] which I think people maybe I don't know
[L1731] [01:04:36.64] if it's still like the the norms have
[L1732] [01:04:38.24] changed, but I would push back on a lot
[L1733] [01:04:40.32] of meetings. Um, I generally didn't do
[L1734] [01:04:43.68] like go to standups unless it was like
[L1735] [01:04:45.92] relevant. Like there's a we're working
[L1736] [01:04:48.08] really hard to ship to something in a
[L1737] [01:04:49.60] month. I need to go to the standup every
[L1738] [01:04:51.76] day because it's like important to be on
[L1739] [01:04:54.40] pace. But if there was like a standup
[L1740] [01:04:56.48] that was more like just social chitchat
[L1741] [01:04:58.40] like cuz the team I don't know some
[L1742] [01:05:01.04] standups end up being that way. I don't
[L1743] [01:05:02.56] know if you've seen them, but like it
[L1744] [01:05:03.76] happens and I would not generally go to
[L1745] [01:05:05.84] those. Um, but yeah, so just being
[L1746] [01:05:08.48] pretty pretty strict about time and then
[L1747] [01:05:10.40] also like having the manager support was
[L1748] [01:05:12.16] like pretty important. like I wouldn't I
[L1749] [01:05:14.56] was pretty choosy and I like went on
[L1750] [01:05:16.64] very I made very conscious team changes
[L1751] [01:05:20.08] when I whenever I did change teams and
[L1752] [01:05:22.32] the manager was like very like in tune
[L1753] [01:05:24.56] with like managers at Meta um like their
[L1754] [01:05:29.20] job is to make their reports perform
[L1755] [01:05:33.20] exceptionally well. I think I don't know
[L1756] [01:05:34.88] if that's how you would summarize it in
[L1757] [01:05:36.24] one sentence, but like um like if your
[L1758] [01:05:40.24] if your reports get promoted and have a
[L1759] [01:05:42.40] lot of impact, like that's what makes
[L1760] [01:05:44.16] you a recognized as a high performing
[L1761] [01:05:47.12] manager too. And so my managers are
[L1762] [01:05:50.72] generally trying to pro like protect me
[L1763] [01:05:54.24] and manage me so that I can have the
[L1764] [01:05:57.44] most impact possible, which means not
[L1765] [01:06:00.00] getting pulled into a lot of meetings
[L1766] [01:06:02.00] where unnecessary. But I also I think I
[L1767] [01:06:05.28] was too arrogant sometimes and that's
[L1768] [01:06:08.08] like one of the things I would tell my
[L1769] [01:06:09.36] older self. Um like sometimes I I I
[L1770] [01:06:12.48] definitely remember walking out on a
[L1771] [01:06:13.84] meeting or two where I was just like I
[L1772] [01:06:15.44] don't think this meeting is useful for
[L1773] [01:06:16.56] me anymore. I'm leaving. I'm just
[L1774] [01:06:18.32] leaving.
[L1775] [01:06:18.64] >> You you said that?
[L1776] [01:06:19.92] >> Yeah. Like I just remember this
[L1777] [01:06:21.84] happening a couple times and I'm like
[L1778] [01:06:23.12] wow that was like not like good
[L1779] [01:06:25.92] behavior.
[L1780] [01:06:28.40] like I wouldn't like I I I like almost
[L1781] [01:06:31.60] feel really bad because like the person
[L1782] [01:06:34.24] running the meeting probably felt really
[L1783] [01:06:35.84] bad and now I feel like really really
[L1784] [01:06:39.44] >> Yeah. Yeah. Did HR ever reach out and
[L1785] [01:06:41.92] say, "Hey, you're you're productive, but
[L1786] [01:06:45.20] can you be nicer and stuff like that?"
[L1787] [01:06:48.64] >> Uh, no. I don't I mean I I don't because
[L1788] [01:06:51.60] I wasn't like mean. It wasn't like a
[L1789] [01:06:53.84] flip the table type thing. It was like
[L1790] [01:06:55.68] very and I would talk to the like I had
[L1791] [01:06:57.36] a good relationship with most like I
[L1792] [01:06:59.28] think all the PMs I worked with I had a
[L1793] [01:07:01.60] pretty good relationship with because I
[L1794] [01:07:03.28] built stuff really fast. I fix bugs
[L1795] [01:07:05.36] really fast. Like not even my own bugs.
[L1796] [01:07:07.52] Just like if they h the PMs like the PMs
[L1797] [01:07:10.16] that a lot of the PMs that I mean Meta
[L1798] [01:07:12.64] is very high performing company. Almost
[L1799] [01:07:14.88] everybody's very strong who works there.
[L1800] [01:07:16.40] And like the PMs are like they want to
[L1801] [01:07:17.92] like get stuff moving fast. They pay
[L1802] [01:07:20.32] attention to every pixel and they're
[L1803] [01:07:21.60] like, "Oh no, this is like broken. This
[L1804] [01:07:23.04] this test wasn't configured right." And
[L1805] [01:07:24.72] there's like things that I was very
[L1806] [01:07:26.32] helpful to PM. So they actually like
[L1807] [01:07:28.00] liked me a lot. Um, and if I like walked
[L1808] [01:07:30.64] out of me, if I like had to leave a
[L1809] [01:07:32.24] meeting, it was like they would almost
[L1810] [01:07:34.24] like give me permission like, "Yeah,
[L1811] [01:07:36.32] like Michael, you don't really you're
[L1812] [01:07:37.52] not needed for this next part of the
[L1813] [01:07:38.80] meeting, you can go." Like it was not as
[L1814] [01:07:40.88] jerkish as it sounds. But I just
[L1815] [01:07:42.72] remember being like that cutthroat where
[L1816] [01:07:44.72] it was just like like I don't want to
[L1817] [01:07:47.20] spend times in meetings that I can't be
[L1818] [01:07:49.92] coding. Like it was like that that uh
[L1819] [01:07:53.52] that vi that that level of like
[L1820] [01:07:55.52] strictness. I would say
[L1821] [01:07:57.36] >> you mentioned that your productivity
[L1822] [01:07:59.84] over your whole career was was high and
[L1823] [01:08:02.48] it didn't change that much. It just what
[L1824] [01:08:04.64] changed was what you wrote code about
[L1825] [01:08:07.28] and the problems that you solved. How
[L1826] [01:08:09.68] did you like grow that skill of project
[L1827] [01:08:13.84] taste or picking problems that mattered
[L1828] [01:08:16.56] so that the code was more impactful? I I
[L1829] [01:08:19.36] don't think that so first of all I don't
[L1830] [01:08:20.64] think that I'm like great great at it
[L1831] [01:08:23.20] necessarily. I generally picked and I'm
[L1832] [01:08:25.76] still not good at pri prioritizing in
[L1833] [01:08:27.92] general. I pick things that I like know
[L1834] [01:08:30.64] how to do if that makes sense. All
[L1835] [01:08:32.48] right. I pick things where I see the
[L1836] [01:08:34.24] answer in my head and um it's just how
[L1837] [01:08:38.72] fast can I like type or like get this
[L1838] [01:08:42.40] into the code. Um, and which is also why
[L1839] [01:08:45.36] LLMs particularly are helping me be
[L1840] [01:08:47.52] personally so much more efficient
[L1841] [01:08:48.88] because it's like I have what I want to
[L1842] [01:08:50.48] do in my head and I need to get it out
[L1843] [01:08:52.24] fast and LLMs can really help with that.
[L1844] [01:08:54.56] Yeah. So, sometimes like it might not be
[L1845] [01:08:56.96] the most impactful thing but it's like a
[L1846] [01:08:59.20] tricky thing and I have the idea in my
[L1847] [01:09:01.28] head on how to do it. I might just do it
[L1848] [01:09:03.84] even though it's not as important as
[L1849] [01:09:05.60] like another thing. Honestly, this is
[L1850] [01:09:07.28] probably one of the things that held me
[L1851] [01:09:08.64] back career-wise. And it was also
[L1852] [01:09:11.12] frustrating for my managers if they did
[L1853] [01:09:13.12] try to communicate like, "Hey, this
[L1854] [01:09:15.20] thing's very important. Can you do
[L1855] [01:09:16.72] that?" And I'm like, I don't see the
[L1856] [01:09:18.56] answer to it. Like, it's not I don't I
[L1857] [01:09:20.80] don't have it. If I don't have it in my
[L1858] [01:09:22.32] head, I can't do that like super fast. I
[L1859] [01:09:24.40] like need to have I need to like see the
[L1860] [01:09:26.96] answer, you know, in a sense. Um, so I'm
[L1861] [01:09:29.28] going to work on B. It's like, can you
[L1862] [01:09:30.72] please work on A? It's like I have to do
[L1863] [01:09:32.80] B C D E F G H. It's like, okay, that's
[L1864] [01:09:37.20] like a lot of work and that's like
[L1865] [01:09:38.80] helpful, but like A would be really
[L1866] [01:09:40.56] good. And I just like I that was like
[L1867] [01:09:41.92] and I think that that's one of the
[L1868] [01:09:43.36] things that probably held me back in
[L1869] [01:09:45.68] general because that limit like if A
[L1870] [01:09:48.48] really really was so important and I and
[L1871] [01:09:51.20] it was not done, you know, it's like you
[L1872] [01:09:53.28] get a passing grade for doing all the
[L1873] [01:09:54.96] other stuff and it's appreciated, but
[L1874] [01:09:57.20] like the company would overall impact
[L1875] [01:09:59.92] would probably be higher by doing a if I
[L1876] [01:10:02.00] was able to do it. But um I'm somewhat
[L1877] [01:10:04.24] limited by like what I can figure out
[L1878] [01:10:06.48] how to do. I frame it as a weakness. But
[L1879] [01:10:08.56] yeah,
[L1880] [01:10:08.96] >> that's interesting. So you always
[L1881] [01:10:10.48] optimize rather than business value
[L1882] [01:10:14.08] fully. You your rank ordered list of
[L1883] [01:10:16.56] priorities was what can I just crank out
[L1884] [01:10:19.60] instantly?
[L1885] [01:10:20.56] >> Yeah. And if you crank out enough stuff,
[L1886] [01:10:22.08] it adds up and it can have a huge amount
[L1887] [01:10:24.08] of impact. But it is definitely
[L1888] [01:10:26.00] definitely like a a different way of
[L1889] [01:10:28.48] thinking of work, I think. Yeah. So once
[L1890] [01:10:31.04] you got promoted to IC7 I think you had
[L1891] [01:10:33.76] shared that you were added to an IC7
[L1892] [01:10:38.24] plus only group and I'm curious was
[L1893] [01:10:41.68] there anything interesting you learned
[L1894] [01:10:43.20] by being a part of that group or was
[L1895] [01:10:44.80] there anything common among all the IC7
[L1896] [01:10:47.04] plus engineers? There's a certain there
[L1897] [01:10:48.88] was a certain kind of bar that everyone
[L1898] [01:10:51.76] had regardless of if they were a coding
[L1899] [01:10:53.84] machine, regardless of if they were a
[L1900] [01:10:56.08] specialist or a fixer, these different
[L1901] [01:10:58.40] like
[L1902] [01:10:59.92] uh reasons why they're there. Um,
[L1903] [01:11:02.40] everyone had like certain traits that
[L1904] [01:11:04.80] were common like extremely strong
[L1905] [01:11:07.52] diligence and conscientiousness.
[L1906] [01:11:10.80] Um, and very uh I wouldn't say fast or
[L1907] [01:11:14.72] quick. I don't know the right word, but
[L1908] [01:11:16.56] like very like sharp. Sharp is the word
[L1909] [01:11:18.64] I'm looking for. If uh if this group was
[L1910] [01:11:21.60] even me as someone who I feel like I'm
[L1911] [01:11:24.08] not I was a very strong student in
[L1912] [01:11:26.48] school. I was like straight A student. I
[L1913] [01:11:28.48] think I'm a pretty smart person, but the
[L1914] [01:11:30.72] most of these people are still are like
[L1915] [01:11:32.40] smarter. Like these are exceptionally
[L1916] [01:11:34.40] smart people who I would who I have to
[L1917] [01:11:37.12] like acknowledge might be smarter than
[L1918] [01:11:38.56] me. Um, but we all could be in the same
[L1919] [01:11:42.16] room and talk about something like very
[L1920] [01:11:45.04] and very quickly move through the
[L1921] [01:11:46.88] concepts. So like here's this new
[L1922] [01:11:48.72] proposed protocol and instead of like
[L1923] [01:11:51.20] having an hourong presentation on it and
[L1924] [01:11:53.36] discussing it, everyone would be pretty
[L1925] [01:11:55.04] sharp sharply be like, "Oh, what about
[L1926] [01:11:57.36] ABCD?" And like the qu follow-up
[L1927] [01:11:58.96] questions would happen very quickly. Um,
[L1928] [01:12:01.68] very sharp fast conversations. Um, and
[L1929] [01:12:05.28] very high attention to detail. Some
[L1930] [01:12:07.76] people like were really like earlier in
[L1931] [01:12:09.76] their career accelerated very fast. They
[L1932] [01:12:11.68] had these traits. Maybe they're
[L1933] [01:12:12.96] personality traits. Like for me, these
[L1934] [01:12:14.64] are more personality traits. I would say
[L1935] [01:12:16.80] like it's like leveraging like OCD and
[L1936] [01:12:19.44] like a way a productive way to be like
[L1937] [01:12:22.96] obsessed about every detail of the
[L1938] [01:12:24.80] product instead of like things that are
[L1939] [01:12:26.64] not productive. For other people, they
[L1940] [01:12:28.80] had like their 25 years of experience
[L1941] [01:12:31.04] and they kind of built these things
[L1942] [01:12:32.80] through different ways, but like
[L1943] [01:12:34.40] everyone kind of had that. Um whereas
[L1944] [01:12:37.12] when a lot of conversations with junior
[L1945] [01:12:40.00] people there's a lot less cont there's
[L1946] [01:12:41.76] context missing. There's not necess like
[L1947] [01:12:44.72] the follow-up questions are not
[L1948] [01:12:46.00] necessarily as like sharp and on super
[L1949] [01:12:49.20] fast. It takes a little longer to get
[L1950] [01:12:51.60] things out. Usually the projects are
[L1951] [01:12:53.12] smaller in scope as a result and stuff
[L1952] [01:12:55.44] like that.
[L1953] [01:12:56.08] >> One thing I want to go over is kind of
[L1954] [01:12:57.68] like a set of topics on just how do you
[L1955] [01:13:01.44] how do you land code fast? Like let's
[L1956] [01:13:03.20] say you're I'm a you know new software
[L1957] [01:13:06.72] engineer.
[L1958] [01:13:08.24] I want to absorb your your coding
[L1959] [01:13:10.72] machine's abilities. Is there a you know
[L1960] [01:13:13.52] top 20% of tips that get is going to
[L1961] [01:13:16.16] give me 80% of the benefit to become
[L1962] [01:13:19.12] more productive? The general advice is
[L1963] [01:13:22.88] you have to move move you can say it
[L1964] [01:13:26.32] just in the shortest possible just like
[L1965] [01:13:28.08] do something like write code. A lot of
[L1966] [01:13:30.56] people I I who ask me for advice or
[L1967] [01:13:33.52] questions like they're like thinking too
[L1968] [01:13:36.08] much about what to do and not doing
[L1969] [01:13:38.08] enough. Um so like step one is like do
[L1970] [01:13:41.12] something just do anything. Um and then
[L1971] [01:13:44.56] step two which is critical is getting
[L1972] [01:13:46.32] feedback from
