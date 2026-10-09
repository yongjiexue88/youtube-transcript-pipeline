Chunk 6; segments 1738–2069. Start may repeat the previous chunk for context.

# How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar

Source ID: source-cfa80c9b2999d9de
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/How_Anthropic_Builds_And_How_Engineering_Will_Change_Soon_Thariq_Shihipar_en.txt
Video: https://www.youtube.com/watch?v=2Kch3tWMnw8

[L1747] [59:35.92] interpretability visualization and I
[L1748] [59:38.16] shared about it. This is my first like
[L1749] [59:39.52] big post on Twitter but it was only 500
[L1750] [59:41.40] likes or something. Like at like now
[L1751] [59:43.52] like you know, that's like not very much
[L1752] [59:45.56] to me but like it's like back then it
[L1753] [59:46.84] was like a huge post and um several
[L1754] [59:49.72] people saw it and like some of them DM'd
[L1755] [59:51.52] me about it and then uh like I then got
[L1756] [59:56.68] an intro into
[L1757] [59:59.00] you know, like uh into a role here and
[L1758] [01:00:01.68] so
[L1759] [01:00:02.60] um
[L1760] [01:00:03.32] I think that like I spent like a month
[L1761] [01:00:05.60] on that project I think in particular.
[L1762] [01:00:07.64] So it wasn't like you know, crazy um
[L1763] [01:00:11.72] and uh yeah, it just like showed people
[L1764] [01:00:15.00] that I could like do interesting work
[L1765] [01:00:17.76] and um
[L1766] [01:00:19.08] and I got paid for it too. So it wasn't
[L1767] [01:00:20.24] like I was doing it for free.
[L1768] [01:00:21.96] Um
[L1769] [01:00:23.24] And and there's plenty of examples of
[L1770] [01:00:24.72] like I think people are happy to do that
[L1771] [01:00:26.80] sort of thing for you. You know, like if
[L1772] [01:00:28.08] you like sort of show that kind of
[L1773] [01:00:30.32] initiative. Um but yeah, you have to
[L1774] [01:00:34.28] like it it it is like you really have to
[L1775] [01:00:36.88] like do interesting and novel work and
[L1776] [01:00:38.44] work work hard and be proud of your work
[L1777] [01:00:40.36] as well. You know, there's not like a
[L1778] [01:00:42.32] shortcut to that I think but
[L1779] [01:00:44.76] um if you do I think everyone is always
[L1780] [01:00:47.12] looking for interesting work and wants
[L1781] [01:00:48.68] to support you and you know, wants to
[L1782] [01:00:50.76] hire you or um
[L1783] [01:00:53.00] yeah, give you money like
[L1784] [01:00:55.48] uh lots of good things.
[L1785] [01:00:57.80] >> I see this tagline going out a lot with
[L1786] [01:01:00.88] some of the stuff Anthropic's been um
[L1787] [01:01:03.64] maybe like I think it's like Boris went
[L1788] [01:01:05.48] on some podcast and the tagline was
[L1789] [01:01:08.20] coding is largely solved. You should
[L1790] [01:01:10.80] people still learn to code if coding is
[L1791] [01:01:13.40] largely solved.
[L1792] [01:01:14.88] >> I think being technical is really really
[L1793] [01:01:16.68] important. Knowing how do computers
[L1794] [01:01:19.12] work, how does like um
[L1795] [01:01:22.04] yeah, how does how do computer programs
[L1796] [01:01:23.60] work? How do languages work? Like what
[L1797] [01:01:25.12] are the hard things and like what's a
[L1798] [01:01:27.12] back-end service? Like what's a cache?
[L1799] [01:01:28.80] Like what's what like like, you know,
[L1800] [01:01:30.28] what like what is memory allocation?
[L1801] [01:01:32.72] Like all of these things are actually
[L1802] [01:01:33.76] kind of really important to learn.
[L1803] [01:01:35.68] Um, I do think it's hard to motivate
[L1804] [01:01:39.08] yourself sometimes to do in the same way
[L1805] [01:01:41.04] that like, you know, doing math by hand
[L1806] [01:01:44.00] was not that motivating to me, you know,
[L1807] [01:01:46.08] but some people just love math and did
[L1808] [01:01:47.64] it. Um, I I think that like that's
[L1809] [01:01:50.80] probably
[L1810] [01:01:52.80] like something that people have to
[L1811] [01:01:53.96] figure out, but I think it is really
[L1812] [01:01:55.28] worth it. Like being technical is really
[L1813] [01:01:57.36] really important. Like we talked about
[L1814] [01:01:59.16] at the start of or like earlier where
[L1815] [01:02:01.44] like, "Oh, the only way you can tell you
[L1816] [01:02:02.84] solved you know, the Riemann hypothesis
[L1817] [01:02:05.84] or like made progress or whatever is
[L1818] [01:02:07.52] like or the Jacobian conjecture is like
[L1819] [01:02:10.20] if you're a great mathematician, right?"
[L1820] [01:02:12.28] And in the same way the only way you can
[L1821] [01:02:14.20] tell if you're like built great software
[L1822] [01:02:16.28] is like if you're a great software
[L1823] [01:02:17.40] engineer. Um,
[L1824] [01:02:19.68] I think that like how do you do that
[L1825] [01:02:22.76] hard, but like we've talked about some
[L1826] [01:02:24.32] of this stuff before just like staying
[L1827] [01:02:25.56] in the loop like, you know, like put
[L1828] [01:02:27.52] like, uh,
[L1829] [01:02:29.20] like putting like reflecting on your
[L1830] [01:02:31.04] process and and getting better and and
[L1831] [01:02:33.00] you can use Claude to learn as well and
[L1832] [01:02:35.08] and sort of explain things to you. So
[L1833] [01:02:36.96] like treating it like a thought partner.
[L1834] [01:02:39.44] Um, but learning like truly I I think
[L1835] [01:02:41.88] like, you know, Kaparthy says like
[L1836] [01:02:43.32] learning should feel like effort, you
[L1837] [01:02:45.00] know, and I think that's like one of the
[L1838] [01:02:46.76] hard things is like a lot of times even
[L1839] [01:02:48.84] if you ask Claude to explain something
[L1840] [01:02:50.16] to you and you might just like nod along
[L1841] [01:02:51.48] and you're like, "Oh, yeah, like I
[L1842] [01:02:52.40] learned it." But you didn't really cuz
[L1843] [01:02:53.72] you didn't put any effort in, right? So
[L1844] [01:02:55.56] I think that like it is really
[L1845] [01:02:57.16] technical. You should learn. It's hard
[L1846] [01:03:00.44] to learn. And and sometimes like what
[L1847] [01:03:02.32] school forces you to do is to learn
[L1848] [01:03:04.00] that. Um, I don't know truly like I'm
[L1849] [01:03:06.96] not learning programming from scratch.
[L1850] [01:03:08.88] So I don't know exactly what how to do
[L1851] [01:03:11.16] it now. I think if short of better ways,
[L1852] [01:03:14.72] I would still like type out and build
[L1853] [01:03:17.40] programs and run them and learn them.
[L1854] [01:03:19.36] You know what I mean?
[L1855] [01:03:20.64] Um there might be better ways that are
[L1856] [01:03:21.80] more cloud informed as well, but I think
[L1857] [01:03:24.00] it's really important.
[L1858] [01:03:25.80] Um
[L1859] [01:03:26.72] I think when Boris says coding is
[L1860] [01:03:28.12] solved, I think it just means like
[L1861] [01:03:30.92] um you know, we don't get stuck in the
[L1862] [01:03:33.28] same ways that we used to before. Like I
[L1863] [01:03:34.88] think coding used to be this very high
[L1864] [01:03:36.44] variability thing where you're like, oh
[L1865] [01:03:38.68] like could this bug take a day or could
[L1866] [01:03:41.40] it take 2 weeks? You have no idea
[L1867] [01:03:43.40] sometimes, you know? And I think like um
[L1868] [01:03:46.20] on the whole coding used to be like in
[L1869] [01:03:49.04] real terms
[L1870] [01:03:50.60] like something that was very rare for
[L1871] [01:03:53.64] something to go well. Do you know what I
[L1872] [01:03:55.48] mean? Like very few people in the entire
[L1873] [01:03:57.84] world could write software and they were
[L1874] [01:04:00.00] very very rare and even if you got them
[L1875] [01:04:02.32] all together, there were so many other
[L1876] [01:04:03.88] reasons why it wouldn't work, right? And
[L1877] [01:04:06.48] coding was this like one of the rarest
[L1878] [01:04:08.64] things in the world where like the
[L1879] [01:04:09.68] chance of software
[L1880] [01:04:11.08] project going well was like
[L1881] [01:04:13.88] on absolute terms very low, you know?
[L1882] [01:04:16.60] Uh and if you were like hiring someone
[L1883] [01:04:18.84] to
[L1884] [01:04:19.84] like make software for you for something
[L1885] [01:04:22.36] that's not like a huge product. Like if
[L1886] [01:04:25.20] you're hiring someone to make software
[L1887] [01:04:26.84] for your car dealership, you were almost
[L1888] [01:04:28.80] certainly not going to get the software
[L1889] [01:04:30.52] you wanted. You're going to get like
[L1890] [01:04:32.16] essentially scammed, you know what I
[L1891] [01:04:33.68] mean? Um not because anyone was trying
[L1892] [01:04:36.04] to scam you. It was just like software
[L1893] [01:04:37.24] was really really hard and you know, it
[L1894] [01:04:39.36] could only be spent on like the most
[L1895] [01:04:41.40] important scalable things in the world.
[L1896] [01:04:43.72] And now that coding is solved, I think
[L1897] [01:04:46.08] what we mean is that like you can use
[L1898] [01:04:47.40] coding to do all these other things that
[L1899] [01:04:50.12] we not done before, but that's not to
[L1900] [01:04:52.96] say that like that's not a lot of work
[L1901] [01:04:54.72] still. Um
[L1902] [01:04:56.64] it's just like it's not this like
[L1903] [01:04:57.88] incredibly rare difficult thing that
[L1904] [01:05:00.28] mostly like just doesn't work and you
[L1905] [01:05:02.72] have to spend like 8 hours a day locked
[L1906] [01:05:05.00] in to do.
[L1907] [01:05:07.16] >> What's really insane, that shows the
[L1908] [01:05:08.96] difference in expectation, is when I
[L1909] [01:05:11.52] used to write software, I would be
[L1910] [01:05:14.20] shocked if it worked on the first try. I
[L1911] [01:05:16.44] was like, "Whoa.
[L1912] [01:05:17.64] >> Wait, why is this working?"
[L1913] [01:05:18.91] >> [laughter]
[L1914] [01:05:19.40] >> And you you'd expect to kind of bash
[L1915] [01:05:21.64] your head against the wall a little bit,
[L1916] [01:05:23.08] and then it it works. Even if it's just
[L1917] [01:05:24.80] like you missed the semicolon or
[L1918] [01:05:26.88] something like that. And now I almost
[L1919] [01:05:29.00] have the flip expectation where it when
[L1920] [01:05:31.28] it doesn't work, I'm like, "Wait, what
[L1921] [01:05:32.60] what why did Claude What what happened
[L1922] [01:05:35.04] here?"
[L1923] [01:05:35.92] Usually, I expect it to work almost uh
[L1924] [01:05:39.36] the opposite
[L1925] [01:05:40.08] >> like on the first try. It's crazy.
[L1926] [01:05:42.20] >> Immediately. Yeah, yeah, I think humans
[L1927] [01:05:43.64] get really used to abundance, right?
[L1928] [01:05:45.28] Like there was this like
[L1929] [01:05:46.92] um article someone shared recently about
[L1930] [01:05:48.80] like going through a modern apartment
[L1931] [01:05:50.80] and talking about all the like wonderful
[L1932] [01:05:52.40] things that we have now that people
[L1933] [01:05:54.32] could not have imagined before. Like
[L1934] [01:05:56.16] something that can play music on demand
[L1935] [01:05:58.20] that's suited for your mood. You know,
[L1936] [01:06:00.44] like before you'd have to like hire a
[L1937] [01:06:02.84] musician, you know, to like go write
[L1938] [01:06:06.36] like, you know, incredible music, right?
[L1939] [01:06:09.12] Um but I'd say on the whole, probably
[L1940] [01:06:11.40] more people are getting paid to make
[L1941] [01:06:13.08] music now than ever before, right? Like
[L1942] [01:06:15.88] um and I think that like music is
[L1943] [01:06:17.68] reaching more people than ever before.
[L1944] [01:06:19.72] And I think probably the same thing will
[L1945] [01:06:21.36] happen with software, will happen with
[L1946] [01:06:23.00] math, will happen with all of these
[L1947] [01:06:24.68] things. Um
[L1948] [01:06:26.76] where you know, when you get abundance,
[L1949] [01:06:28.64] people are like, "Great. Like I want
[L1950] [01:06:29.84] more abundance. I want my software in
[L1951] [01:06:31.72] everything, you know? Like I want my
[L1952] [01:06:33.08] music everywhere, you know?" So, yeah.
[L1953] [01:06:36.00] >> Yeah, one potential other data point for
[L1954] [01:06:38.24] this conversation saying that maybe
[L1955] [01:06:40.40] people should still be technical or
[L1956] [01:06:43.00] learn how to code is I think earlier in
[L1957] [01:06:45.12] the conversation we talked about
[L1958] [01:06:47.04] automating knowledge work, and you
[L1959] [01:06:48.76] mentioned that
[L1960] [01:06:50.48] people who are technical had kind of a
[L1961] [01:06:52.16] leg up cuz they could kind of understood
[L1962] [01:06:54.60] how to coordinate Claude to do a variety
[L1963] [01:06:57.44] thing. Like you're calling FFmpeg to
[L1964] [01:07:00.00] automate some video editing, and like I
[L1965] [01:07:02.76] don't think someone who is not technical
[L1966] [01:07:04.48] would have that thought. So, it does
[L1967] [01:07:07.08] seem like even in this case where models
[L1968] [01:07:09.00] are doing a lot, there's still so much
[L1969] [01:07:11.32] value in being technical.
[L1970] [01:07:13.80] >> Knowing how computers work. You know, in
[L1971] [01:07:15.88] the same way that like like probably
[L1972] [01:07:18.68] like the most technical CEOs are like
[L1973] [01:07:20.92] the best CEOs are technical, right? Like
[L1974] [01:07:22.56] Zuckerberg, Elon, right? But like they
[L1975] [01:07:24.64] probably haven't written like a line of
[L1976] [01:07:26.04] code truly in a long time, but you know,
[L1977] [01:07:29.00] they understand how systems work, they
[L1978] [01:07:30.80] understand you know, constraints and
[L1979] [01:07:32.84] things like that and then that's really
[L1980] [01:07:34.20] really important. And so,
[L1981] [01:07:36.24] um you know, even if all that work is
[L1982] [01:07:38.64] changed, I think like being technical is
[L1983] [01:07:40.28] really really important.
[L1984] [01:07:42.28] >> And then last question for you is if you
[L1985] [01:07:44.40] could go back to when you just entered
[L1986] [01:07:46.32] the industry and give yourself some
[L1987] [01:07:47.72] advice knowing what you know now, what
[L1988] [01:07:49.80] would you say?
[L1989] [01:07:52.28] >> There are like kind of like two wolves
[L1990] [01:07:54.92] sort of I I think like you have to
[L1991] [01:07:57.16] believe in yourself, you know, I think
[L1992] [01:07:58.88] like this is really important and I
[L1993] [01:08:00.36] think that like at least when I joined
[L1994] [01:08:03.08] in the industry, it was rarer to believe
[L1995] [01:08:05.36] in people when they were
[L1996] [01:08:07.72] kind of the younger. Like I think that
[L1997] [01:08:09.00] was like the whole point of Y Combinator
[L1998] [01:08:10.88] or something was like believing in young
[L1999] [01:08:12.44] people early on to do really great
[L2000] [01:08:14.80] things. And so, I think that like you
[L2001] [01:08:16.68] know, even going back to like the intern
[L2002] [01:08:18.68] discussion we had earlier, right? Like I
[L2003] [01:08:20.32] think that like
[L2004] [01:08:22.40] thinking of yourself not as like someone
[L2005] [01:08:23.84] who's like being trained to do
[L2006] [01:08:25.16] something, but someone who can do like
[L2007] [01:08:26.48] something incredible right away, I think
[L2008] [01:08:28.08] is really important, you know? And um
[L2009] [01:08:31.20] I think I wish I had done
[L2010] [01:08:33.92] bigger, bolder things that I'd written
[L2011] [01:08:37.12] and and shared about. I think there were
[L2012] [01:08:38.92] lots of ideas where I was like, "Wow,
[L2013] [01:08:40.56] like I think
[L2014] [01:08:41.92] I think I had like I thought I had done
[L2015] [01:08:44.72] original work that I wish
[L2016] [01:08:47.12] maybe I'd even shared in some form, but
[L2017] [01:08:48.72] maybe not like form that it like
[L2018] [01:08:50.40] survived the internet, you know? And it
[L2019] [01:08:52.84] wasn't like a like goal of mine. And so,
[L2020] [01:08:55.56] I wish I'd like sort of been bolder and
[L2021] [01:08:57.80] like you know,
[L2022] [01:08:59.80] done and shared some of this work, but
[L2023] [01:09:02.28] at the same time you also there is a lot
[L2024] [01:09:04.12] to learn from people, you know what I
[L2025] [01:09:05.76] mean? And like I think that um
[L2026] [01:09:08.92] you like I think when you're young,
[L2027] [01:09:10.68] you're like, you know, you tend to fold
[L2028] [01:09:13.00] fall either you're not bold enough or
[L2029] [01:09:14.68] you're
[L2030] [01:09:15.56] you're not like
[L2031] [01:09:17.36] uh
[L2032] [01:09:18.96] you don't like learn enough, you know,
[L2033] [01:09:20.68] or you're like you're not like you don't
[L2034] [01:09:22.64] like you're too bold and you don't like
[L2035] [01:09:25.12] figure out what people have done before
[L2036] [01:09:26.40] and figure out why it's not working,
[L2037] [01:09:28.00] right? Um and there's this balance and I
[L2038] [01:09:31.00] think uh you everyone has different
[L2039] [01:09:33.40] failure modes, but I think like uh I
[L2040] [01:09:35.68] think I probably didn't take it enough
[L2041] [01:09:37.16] advantage of like, you know, mentors and
[L2042] [01:09:39.92] people who had learned a lot. Um and I
[L2043] [01:09:41.96] think I probably had to like relearn a
[L2044] [01:09:43.72] bunch of things as a result. Um
[L2045] [01:09:46.48] So, there's probably not universal good
[L2046] [01:09:48.56] advice, but just things to think about
[L2047] [01:09:50.76] as you're, you know, as you're entering.
[L2048] [01:09:53.12] >> Awesome. Well, thanks so much for your
[L2049] [01:09:54.52] time, Derek. Really appreciate it.
[L2050] [01:09:56.28] >> Yeah, of course. Thanks, fine. It's fun.
[L2051] [01:09:58.76] >> Hey, thank you for watching this
[L2052] [01:09:59.80] podcast. If you liked it and you want to
[L2053] [01:10:01.44] see the show grow, please support with a
[L2054] [01:10:03.64] comment or a like.
[L2055] [01:10:05.64] Also, if you have any recommendations
[L2056] [01:10:07.48] for people you want me to bring on,
[L2057] [01:10:09.48] please drop a comment. Guests like
[L2058] [01:10:11.64] Barbara Liskov, Mike Stonebraker, Mark
[L2059] [01:10:14.36] Brooker, these were all people that I
[L2060] [01:10:16.40] brought on because someone left a
[L2061] [01:10:18.24] comment. On another note, aside from the
[L2062] [01:10:20.52] podcast, I'm working on building the
[L2063] [01:10:22.32] ergonomic keyboard that I wish existed.
[L2064] [01:10:24.76] Here's a glance at the prototype. It's a
[L2065] [01:10:26.64] split keyboard, so there's two sides. Um
[L2066] [01:10:29.68] this is in the case. But yeah, we
[L2067] [01:10:31.12] launched on Kickstarter and we hit our
[L2068] [01:10:32.92] goal within 8 hours of launching. I
[L2069] [01:10:35.00] really appreciate it if you were one of
[L2070] [01:10:36.40] the people who grabbed one of the early
[L2071] [01:10:38.16] units. Um we're now working on the long
[L2072] [01:10:40.52] journey of building the tooling now, and
[L2073] [01:10:42.64] so if you still want to pick one up,
[L2074] [01:10:44.32] I've left the late pledges open on
[L2075] [01:10:46.32] Kickstarter, so you can grab one there.
[L2076] [01:10:48.56] I'll put a link in the description.
[L2077] [01:10:50.52] Thank you again for watching the podcast
[L2078] [01:10:52.84] and I'll see you in the next episode.
