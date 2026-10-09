Chunk 6; segments 1661–2001. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L1670] [59:51.60] or slow, what it struggles with and what
[L1671] [59:53.36] it doesn't and just to keep that in the
[L1672] [59:55.68] back of your head because at the end of
[L1673] [59:58.00] the day, if you have that knowledge, I
[L1674] [01:00:00.24] think you're very unlikely to make the
[L1675] [01:00:02.32] kinds of architectural decisions that
[L1676] [01:00:04.72] will be hard to undo later, right?
[L1677] [01:00:08.00] Um, and so that's really that's really
[L1678] [01:00:10.56] the majority of it I think and that is
[L1679] [01:00:13.12] by far the highest impact lowest cost
[L1680] [01:00:16.40] thing you can do is just do that
[L1681] [01:00:17.52] training once because once you have it
[L1682] [01:00:19.12] it's with you forever once you
[L1683] [01:00:20.88] understand how to think about
[L1684] [01:00:22.48] performance it can always be there and
[L1685] [01:00:26.24] at any time you can sort of have that
[L1686] [01:00:28.24] alarm bell of like this I don't see you
[L1687] [01:00:32.16] know you're always kind of looking like
[L1688] [01:00:33.44] I don't see the path towards this
[L1689] [01:00:35.28] running well and then So that's that
[L1690] [01:00:37.68] your key to stop and go like uh maybe we
[L1691] [01:00:39.68] need to rethink like how we were making
[L1692] [01:00:41.20] some of these decisions. As long as you
[L1693] [01:00:43.68] can see that path, you're pretty you can
[L1694] [01:00:46.00] you can delay most like optimization
[L1695] [01:00:49.20] work. As long as you can see the path
[L1696] [01:00:51.44] like here is how we will optimize this.
[L1697] [01:00:54.16] You're in pretty good shape because um
[L1698] [01:00:57.28] if you're making those trade-offs
[L1699] [01:00:58.72] correctly, you're not going to paint
[L1700] [01:01:00.80] yourself into a corner where there's
[L1701] [01:01:02.32] nothing that you can do other than scrap
[L1702] [01:01:04.32] and rewrite. Right. you had this one
[L1703] [01:01:06.72] video title. It said, you know, where
[L1704] [01:01:09.12] does bad code come from? And so, yeah,
[L1705] [01:01:11.32] [laughter] you know, I guess, yeah, my
[L1706] [01:01:12.56] question to you is, you know, what's the
[L1707] [01:01:14.00] answer to that? Where where does bad
[L1708] [01:01:15.68] code come from?
[L1709] [01:01:18.24] Yeah, that's a good question. Um, my
[L1710] [01:01:20.32] feeling on where bad code comes from is
[L1711] [01:01:23.12] that for everything that I've seen on
[L1712] [01:01:26.24] projects in the past, the bad code all
[L1713] [01:01:29.04] seems to come from roughly the same
[L1714] [01:01:31.52] source. And that is not dealing with the
[L1715] [01:01:36.64] actual thing that's happening, right? Um
[L1716] [01:01:41.44] there's a lot of ideas in computer
[L1717] [01:01:44.08] science about sort of doing upfront
[L1718] [01:01:47.52] design and making a lot of decisions
[L1719] [01:01:49.52] without ever really implementing
[L1720] [01:01:52.08] anything, right?
[L1721] [01:01:54.48] And I have found that universally that
[L1722] [01:01:57.76] leads to the worst kind of code. And the
[L1723] [01:02:00.56] reason for that is, you know, uh I hate
[L1724] [01:02:04.40] to be pessimistic and I hate to be
[L1725] [01:02:06.72] pessimistic about my own ability, but
[L1726] [01:02:08.88] I'll just say for me personally,
[L1727] [01:02:11.44] I am not able to correctly hold all of
[L1728] [01:02:16.40] the details for most complex software in
[L1729] [01:02:19.44] my head at once. There's just a lot of
[L1730] [01:02:22.16] stuff going on at like when when the
[L1731] [01:02:26.00] actual, you know, instructions hit the
[L1732] [01:02:28.32] CPU. There's a lot going on down there
[L1733] [01:02:31.52] that's very hard to keep all in your
[L1734] [01:02:33.52] head. And so when you approach an
[L1735] [01:02:35.76] upfront design, typically unless the
[L1736] [01:02:38.08] problem is very is like stupidly simple,
[L1737] [01:02:40.56] right?
[L1738] [01:02:42.64] When you approach something with upfront
[L1739] [01:02:44.08] design and you think you're going to get
[L1740] [01:02:45.92] all of this architecture worked out
[L1741] [01:02:47.84] ahead of time, you forget some important
[L1742] [01:02:51.28] things. You make decisions without
[L1743] [01:02:53.28] realizing, oh wait, there's this thing
[L1744] [01:02:55.60] that has to happen there that means that
[L1745] [01:02:57.84] this isn't really the right way for
[L1746] [01:03:00.24] these pieces of code to interoperate.
[L1747] [01:03:03.04] And so then you, you know, you end up
[L1748] [01:03:05.76] seeing these hilarious APIs or something
[L1749] [01:03:08.08] where it's like you're just like, how
[L1750] [01:03:09.60] did this end up being the way that you
[L1751] [01:03:12.00] do this, right? Like I have to create
[L1752] [01:03:13.52] all these objects and I have to connect
[L1753] [01:03:15.04] them together with these things and I
[L1754] [01:03:16.48] have to create this weird like filter
[L1755] [01:03:18.24] graph thing and then I have to call
[L1756] [01:03:19.28] compile on it. but only like you end up
[L1757] [01:03:21.36] with these like insane things. You're
[L1758] [01:03:22.80] like all I wanted to do was call this
[L1759] [01:03:24.72] one thing that said like low pass filter
[L1760] [01:03:26.48] this buffer. It could have been one
[L1761] [01:03:27.76] function call, right? It's like how did
[L1762] [01:03:29.60] you get there? And the answer is because
[L1763] [01:03:31.20] you weren't actually like dealing with
[L1764] [01:03:33.44] the actual problem and looking at what
[L1765] [01:03:35.04] the actual code looks like uh when you
[L1766] [01:03:37.92] want to actually uh when you actually
[L1767] [01:03:39.92] want to solve the problem in practice.
[L1768] [01:03:42.24] And so my idea of where bad code comes
[L1769] [01:03:44.08] from is usually just it's that it's this
[L1770] [01:03:46.24] failure to engage with the actual
[L1771] [01:03:48.24] reality of the situation.
[L1772] [01:03:50.72] Um
[L1773] [01:03:52.96] maybe there are people out there I
[L1774] [01:03:54.56] certainly have never met any but maybe
[L1775] [01:03:56.32] there are people out there whose brains
[L1776] [01:03:57.84] are so expansive that they can actually
[L1777] [01:03:59.68] hold all that in there and they can
[L1778] [01:04:01.12] therefore just do it upfront. Um, but
[L1779] [01:04:04.32] other than for very sort of constrained
[L1780] [01:04:06.80] problem spaces, I've never seen that
[L1781] [01:04:08.96] work. And and you know there, like I
[L1782] [01:04:11.12] said, there are sometimes when that's
[L1783] [01:04:12.24] the case with the trans like if you're
[L1784] [01:04:13.52] just doing like I'm trying to do this
[L1785] [01:04:15.92] particular mathematical operation, that
[L1786] [01:04:18.08] might be a case where you can work it
[L1787] [01:04:19.04] all out on paper because it's very
[L1788] [01:04:20.32] specific like what it is. It takes these
[L1789] [01:04:22.00] n inputs, produces this output, and I
[L1790] [01:04:23.84] can work right. But when you're talking
[L1791] [01:04:25.36] about architecture like, hey, it's a web
[L1792] [01:04:27.04] browser, right? Some complicated thing.
[L1793] [01:04:29.92] The details are all that matter to me,
[L1794] [01:04:32.96] right? It's like it's where all the
[L1795] [01:04:34.48] complexity lies and if you try to do the
[L1796] [01:04:36.80] design without reckoning with them, it
[L1797] [01:04:39.68] just leads to bad results in my
[L1798] [01:04:40.96] experience. So,
[L1799] [01:04:41.84] >> so how do you avoid writing bad code in
[L1800] [01:04:44.56] that case?
[L1801] [01:04:45.68] >> I I try to start with the actual
[L1802] [01:04:48.56] solutions to the problems and work up
[L1803] [01:04:50.80] from there. So, um
[L1804] [01:04:54.96] one way to say it would be instead of
[L1805] [01:04:56.24] top down programming, bottom up
[L1806] [01:04:57.60] programming, right? Uh as much as
[L1807] [01:04:59.12] possible. And top down programming isn't
[L1808] [01:05:00.48] really the same as designing up front,
[L1809] [01:05:01.76] but you know, I'm just saying like as a
[L1810] [01:05:03.92] contrast there, try to start with the
[L1811] [01:05:06.72] things that you know you need. Like it's
[L1812] [01:05:08.08] like, okay, if I'm if I'm building this
[L1813] [01:05:09.44] thing, it's got to have a rasterizer.
[L1814] [01:05:10.80] All right, I'm going to start making a
[L1815] [01:05:11.76] rasterizer. I'm going to see what kinds
[L1816] [01:05:13.12] of stuff that does and how I would like
[L1817] [01:05:15.28] what's the most uh straightforward way
[L1818] [01:05:17.36] to call this and use it. Okay, let's
[L1819] [01:05:19.36] make an API out of that, right?
[L1820] [01:05:21.44] build it out of steps where the
[L1821] [01:05:23.68] abstraction comes from actual working
[L1822] [01:05:27.04] code that gets abstracted rather than
[L1823] [01:05:29.76] pushing the abstraction down from the
[L1824] [01:05:31.60] top where I say this is how I will
[L1825] [01:05:34.48] abstract the rasterizer and now I go
[L1826] [01:05:37.68] write the rasterizer in the thing that
[L1827] [01:05:39.36] uses the rasterizer only to find that
[L1828] [01:05:41.60] that is not a very good way to use a
[L1829] [01:05:43.28] rasterizer right like so to me starting
[L1830] [01:05:46.40] with that and working upwards is the
[L1831] [01:05:48.96] best way to ensure that you will get an
[L1832] [01:05:50.96] architecture uh that is at least good
[L1833] [01:05:53.60] for one thing. Now, if you want it to be
[L1834] [01:05:55.52] good for multiple things, you probably
[L1835] [01:05:57.44] need a couple different like I want a
[L1836] [01:05:59.52] few different varied things that would
[L1837] [01:06:01.36] use this rasterizer that I will kind of
[L1838] [01:06:02.96] work on together and I'll make
[L1839] [01:06:04.48] abstraction decisions that work across
[L1840] [01:06:06.32] all three of them. That's a good way to
[L1841] [01:06:08.16] make a more reusable API that works for,
[L1842] [01:06:10.64] you know, a lot of things. But I never
[L1843] [01:06:12.88] want to just sit down and say, "How will
[L1844] [01:06:15.44] I design an API for lots of people to
[L1845] [01:06:17.68] use a rasterizer without actually
[L1846] [01:06:19.76] writing any of it?" It's like, "No, no,
[L1847] [01:06:21.28] no." Like, and I definitely can't do it.
[L1848] [01:06:23.44] And I I question I I would question
[L1849] [01:06:25.76] someone who says that they can, unless
[L1850] [01:06:28.16] one caveat, they've written a lot of
[L1851] [01:06:29.76] them before, right? If you've written
[L1852] [01:06:30.88] tons before, then you've sort of done
[L1853] [01:06:32.32] the thing that I'm talking about already
[L1854] [01:06:33.68] and you might remember, oh, it's this
[L1855] [01:06:35.44] way, right?
[L1856] [01:06:37.36] I think there's a lot of common advice,
[L1857] [01:06:40.08] especially at these these larger
[L1858] [01:06:41.68] companies where there's this processes
[L1859] [01:06:45.12] to, you know, write a design doc and
[L1860] [01:06:48.56] kind of uh, you know, put together
[L1861] [01:06:50.40] everything in advance, present it before
[L1862] [01:06:53.12] you write any code. And sounds like
[L1863] [01:06:56.00] you're saying that that's a terrible
[L1864] [01:06:57.44] idea.
[L1865] [01:06:57.92] >> I think that's an absolutely terrible
[L1866] [01:06:59.36] idea. Now, that doesn't mean that I
[L1867] [01:07:01.76] wouldn't be okay with that process with
[L1868] [01:07:03.20] like a slight modification, right? If
[L1869] [01:07:05.52] what you're doing during that time is
[L1870] [01:07:07.20] writing test code in the way that I'm
[L1871] [01:07:09.36] saying, so we're going to write a little
[L1872] [01:07:10.88] experimental rasterizer. We're going to
[L1873] [01:07:12.32] do those things. We're going to start
[L1874] [01:07:13.04] and then our document that we're
[L1875] [01:07:14.56] producing is here is what we have
[L1876] [01:07:17.04] determined is a good API based on these
[L1877] [01:07:19.36] experiments. I have no problem with
[L1878] [01:07:21.52] that. That's really that's following my
[L1879] [01:07:24.24] procedure pretty much to a tea. And you
[L1880] [01:07:27.36] know, I don't tend to produce
[L1881] [01:07:28.72] documentation because I work you know in
[L1882] [01:07:30.72] on smaller teams. I don't have to have a
[L1883] [01:07:34.72] thousand person org know exactly what it
[L1884] [01:07:36.80] what I'm doing there or whatever.
[L1885] [01:07:39.76] So I wouldn't produce upfront
[L1886] [01:07:40.88] documentation normally in a in a case
[L1887] [01:07:42.40] like that. But if you if you wanted to
[L1888] [01:07:44.32] that seems totally reasonable, right?
[L1889] [01:07:45.68] And that like is communicating our
[L1890] [01:07:47.76] research into how this should be
[L1891] [01:07:49.76] structured uh out to a wider audience.
[L1892] [01:07:52.40] But we still did the due diligence of
[L1893] [01:07:53.92] determining that it really does work in
[L1894] [01:07:55.44] practice. It's not just our guess about
[L1895] [01:07:57.76] what it will be.
[L1896] [01:07:59.20] >> I see. Okay. So you're saying kind of
[L1897] [01:08:01.04] this u pair design, pair prototype kind
[L1898] [01:08:04.64] of, you know, like you just build as you
[L1899] [01:08:06.48] go, but it's just so you get a sense of
[L1900] [01:08:08.48] the reality of the design.
[L1901] [01:08:10.64] >> Yeah. And I think I would be very
[L1902] [01:08:11.92] comfortable with the team that wanted to
[L1903] [01:08:13.04] work that way if they're like, look, we
[L1904] [01:08:14.24] want to produce, we want to document
[L1905] [01:08:15.84] this thing before we start developing
[L1906] [01:08:17.36] it. That's just how we feel more
[L1907] [01:08:19.12] comfortable, you know, with how we're
[L1908] [01:08:20.80] going to do it. Maybe it's a very large
[L1909] [01:08:22.24] org. Maybe we have some very good
[L1910] [01:08:24.08] reasons for that. Um, then I would say
[L1911] [01:08:27.68] totally fine. It's just I want I want to
[L1912] [01:08:30.00] hear you know if I'm going to be
[L1913] [01:08:31.36] comfortable with it I want to hear that
[L1914] [01:08:32.48] that process is not we're just typing on
[L1915] [01:08:34.16] paper. We are actually testing these API
[L1916] [01:08:37.52] uh design decisions and they come from
[L1917] [01:08:39.68] looking at actual usage code that we
[L1918] [01:08:42.48] have made and that we have implemented
[L1919] [01:08:44.48] at least uh experimental versions of so
[L1920] [01:08:47.84] that we know they really do account for
[L1921] [01:08:49.92] all the details that we're likely to
[L1922] [01:08:51.52] encounter in practice. That's what I
[L1923] [01:08:54.48] want to hear, right? I don't want to
[L1924] [01:08:55.68] hear like ah we thought it through. Like
[L1925] [01:08:57.44] I'm like did you did you think it all
[L1926] [01:09:00.08] the way through? Because I've seen a lot
[L1927] [01:09:01.36] of times where people thought they did
[L1928] [01:09:02.56] and they didn't including myself. Like
[L1929] [01:09:04.40] that is not that is not a I always think
[L1930] [01:09:06.08] it all the way through. So it's like no
[L1931] [01:09:07.12] this comes from a personal place of I
[L1932] [01:09:09.28] forgot the thing. Like I forgot this
[L1933] [01:09:10.88] important thing and I made a really
[L1934] [01:09:12.32] stupid design. Right.
[L1935] [01:09:14.32] >> There's another video you had. It was it
[L1936] [01:09:15.92] was titled the only unbreakable law.
[L1937] [01:09:19.20] >> Oh yeah.
[L1938] [01:09:19.76] >> And you know what is the only
[L1939] [01:09:22.00] unbreakable law in software engineering?
[L1940] [01:09:24.08] So yeah, that was that was a a lecture I
[L1941] [01:09:26.88] did um where I was trying to think of
[L1942] [01:09:30.32] like if I was going to say one thing
[L1943] [01:09:32.24] about architecture to people, right? If
[L1944] [01:09:33.92] I was going to say one thing about
[L1945] [01:09:34.88] architecture,
[L1946] [01:09:36.64] what could I say that isn't probably
[L1947] [01:09:39.60] wrong? Because you think about a lot of
[L1948] [01:09:41.52] our ideas about architecture, it's like
[L1949] [01:09:42.96] even the stuff I just said to you, who
[L1950] [01:09:45.04] knows what we're going to be thinking 10
[L1951] [01:09:46.80] years from now. It's like they're not
[L1952] [01:09:48.96] really laws. They're just
[L1953] [01:09:52.16] they're observations that we've had that
[L1954] [01:09:54.16] maybe this is a good way to do things,
[L1955] [01:09:55.84] but it's not really a law. Right? So, uh
[L1956] [01:09:59.36] the only thing I've seen that feels like
[L1957] [01:10:01.36] a real law to me is the thing I cover in
[L1958] [01:10:03.44] this lecture, which is Conway's law. Uh
[L1959] [01:10:06.00] and this is a a it's not a real law in
[L1960] [01:10:10.08] the sense of like the laws of gravity or
[L1961] [01:10:13.04] so like it's not a physics law like a a
[L1962] [01:10:15.20] physicist would laugh at calling it a
[L1963] [01:10:16.80] law. um you know, it's probably not even
[L1964] [01:10:20.08] a theory. It's more like a hypothesis at
[L1965] [01:10:23.12] this point, right? But in terms of
[L1966] [01:10:25.44] things that I would place money on
[L1967] [01:10:30.40] being validated as a law at some point
[L1968] [01:10:32.48] if we ever had the means to do so. This
[L1969] [01:10:35.76] would be one of the only software
[L1970] [01:10:37.44] engineering things that I think uh would
[L1971] [01:10:40.00] qualify and it is
[L1972] [01:10:43.84] that if you would like to organize
[L1973] [01:10:49.60] a series of like a set of people to work
[L1974] [01:10:52.56] on something or in the modern parliament
[L1975] [01:10:54.80] let's say agents. So it could be, it
[L1976] [01:10:56.88] doesn't have to be a human. It's any
[L1977] [01:10:59.52] system that has sort of its own internal
[L1978] [01:11:02.00] processing like a human brain does or
[L1979] [01:11:04.08] like a computer does.
[L1980] [01:11:06.64] If you need to partition a problem into
[L1981] [01:11:10.56] a set of workers in this way
[L1982] [01:11:14.16] where the communication between those
[L1983] [01:11:16.24] workers is slower than their own
[L1984] [01:11:18.40] internal computation ability, which we
[L1985] [01:11:20.80] would all agree is true about humans.
[L1986] [01:11:22.24] It's true about two computers running an
[L1987] [01:11:24.48] AI model as well, right? the amount of
[L1988] [01:11:26.00] time it takes to send information back
[L1989] [01:11:27.28] and forth to them is is significantly
[L1990] [01:11:29.28] slower than what like the GPU can be
[L1991] [01:11:31.12] processing directly on it on its own.
[L1992] [01:11:32.88] Right? In systems that look like that,
[L1993] [01:11:35.12] when you start to tackle a problem, in
[L1994] [01:11:38.16] order to get the benefits of that
[L1995] [01:11:39.52] parallelization,
[L1996] [01:11:41.12] you will have to make decisions about
[L1997] [01:11:42.72] who is working on what. At least some
[L1998] [01:11:44.88] decision. For example, if we're making a
[L1999] [01:11:47.44] car and you and I are the two people are
[L2000] [01:11:49.20] going to make the car, I'm going to
[L2001] [01:11:51.04] design the body of the car. you're gonna
[L2002] [01:11:52.56] design the wheels,
[L2003] [01:11:54.96] right? Just a decision someone could
[L2004] [01:11:56.88] make.
[L2005] [01:11:58.48] Once you've made that decision,
[L2006] [01:12:01.76] you have now locked in the fact that the
[L2007] [01:12:06.16] iteration
[L2008] [01:12:08.16] on the design
[L2009] [01:12:10.16] will be slower across that boundary than
[L2010] [01:12:13.28] it is interior to either of the two
