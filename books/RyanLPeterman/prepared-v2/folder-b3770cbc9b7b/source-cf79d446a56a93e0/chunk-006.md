Chunk 6; segments 1751–2111. Start may repeat the previous chunk for context.

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L1760] [01:29:34.40] The examples I've seen of attempts for
[L1761] [01:29:39.20] AI to generate code in this domain
[L1762] [01:29:43.12] uh has not been successful.
[L1763] [01:29:45.60] it uh they generate more bugs, more
[L1764] [01:29:49.12] security holes. They have uh bloated
[L1765] [01:29:52.48] code which pessimize again because you
[L1766] [01:29:56.08] use more memory
[L1767] [01:29:58.32] and um it's hard to validate
[L1768] [01:30:03.04] and the senior developers that would be
[L1769] [01:30:06.00] needed to validate it um I've seen some
[L1770] [01:30:10.00] of them starting to retire because they
[L1771] [01:30:12.80] don't want to deal with the validation
[L1772] [01:30:14.96] of something that changes every time you
[L1773] [01:30:17.20] make a change in your code in your
[L1774] [01:30:19.28] prompts.
[L1775] [01:30:20.88] And furthermore, a lot of the things I
[L1776] [01:30:24.16] think about um there's regulatory
[L1777] [01:30:27.76] bodies, there's validation. You have to
[L1778] [01:30:30.40] be able to validate what you changed
[L1779] [01:30:32.48] when you make a change. And the AIS the
[L1780] [01:30:36.16] the tools change the uh even if you make
[L1781] [01:30:39.92] a slight different prompt, the uh a lot
[L1782] [01:30:43.04] of the code will change and you have to
[L1783] [01:30:45.44] now check it again.
[L1784] [01:30:47.92] all of the code that was generated and
[L1785] [01:30:49.84] know there's more code generated than if
[L1786] [01:30:51.68] it was written by humans. And when a
[L1787] [01:30:54.80] human make a change, it it'll make a
[L1788] [01:30:57.44] change that's localized and you can look
[L1789] [01:31:00.08] for the effects of that localized
[L1790] [01:31:02.56] change. If an AI writes it, uh it uh it
[L1791] [01:31:07.52] you don't actually know where it's
[L1792] [01:31:09.12] changed. You have to try and figure that
[L1793] [01:31:11.12] out. So if you're doing something that
[L1794] [01:31:14.40] has been done many times before, you
[L1795] [01:31:17.28] write a standard web app, uh what you
[L1796] [01:31:20.24] say is correct. Um also AI is not
[L1797] [01:31:24.48] useless. That's not what I'm saying. It
[L1798] [01:31:26.96] can be used to write uh documentation.
[L1799] [01:31:30.32] Again, it has to be humanly validated,
[L1800] [01:31:33.52] but it helps write uh things. It's good
[L1801] [01:31:36.80] at text.
[L1802] [01:31:38.72] It's not
[L1803] [01:31:41.92] at least now good at
[L1804] [01:31:46.32] um
[L1805] [01:31:48.16] safety critical performance critical uh
[L1806] [01:31:51.44] code. Now
[L1807] [01:31:54.24] let's say that 70 or 80% of the code of
[L1808] [01:31:57.76] the world's code doesn't fit that
[L1809] [01:31:59.76] pattern but it's the that 10 20% of the
[L1810] [01:32:05.68] code that I'm interested in and there
[L1811] [01:32:08.88] it's not there and I don't see it coming
[L1812] [01:32:11.60] with the LLM model. Furthermore, ILM
[L1813] [01:32:17.04] when fed with training data
[L1814] [01:32:22.48] has to be trained with old code.
[L1815] [01:32:25.68] And my job as I see it is to make sure
[L1816] [01:32:30.96] people write new things and use new
[L1817] [01:32:33.44] techniques that are improvement over the
[L1818] [01:32:35.92] old code. So I find that LLM based code
[L1819] [01:32:42.72] is imitating old code and getting old
[L1820] [01:32:47.04] performance and old bugs.
[L1821] [01:32:50.24] Uh again maybe you can improve that. I
[L1822] [01:32:53.76] hear rumors of Biana apps being written.
[L1823] [01:32:57.36] Uh that's fed my uh writings, but even
[L1824] [01:33:01.60] that is problematic because I'm not
[L1825] [01:33:03.68] saying exactly the same as I did 20
[L1826] [01:33:06.32] years ago. But anyway, we we'll we'll
[L1827] [01:33:08.64] see. Um
[L1828] [01:33:11.36] also even Dystra was looking into the
[L1829] [01:33:14.96] possibility and he claimed that um the
[L1830] [01:33:18.88] idea of having natural languages being
[L1831] [01:33:23.44] the programming language was idiotic. He
[L1832] [01:33:26.56] is less polite than I am. And um I think
[L1833] [01:33:31.44] that a language like English is very
[L1834] [01:33:34.64] flexible and what we say is often very
[L1835] [01:33:38.96] ambiguous. We need a programming
[L1836] [01:33:41.20] language that's precise that's that's
[L1837] [01:33:43.92] engineering that's math. It's not
[L1838] [01:33:46.56] English.
[L1839] [01:33:48.48] And for that code that is uh performance
[L1840] [01:33:51.68] or safety critical I imagine there will
[L1841] [01:33:54.64] be some uh group of people that is using
[L1842] [01:33:57.60] uh LLM for that and I guess based off
[L1843] [01:34:00.56] what you're saying is the intuition that
[L1844] [01:34:02.80] you would foresee more breakages and
[L1845] [01:34:06.08] bugs and uh you know because it's not
[L1846] [01:34:09.76] valid
[L1847] [01:34:10.16] >> and the people that are really good at
[L1848] [01:34:12.64] that kind of stuff uh tend to to not
[L1849] [01:34:17.12] want to spend all their time validating.
[L1850] [01:34:20.08] Another problem is that they want to
[L1851] [01:34:22.24] eliminate
[L1852] [01:34:23.76] junior programmers because there's lots
[L1853] [01:34:26.08] of them. But if you do that, where do
[L1854] [01:34:29.60] you get the senior programmers from?
[L1855] [01:34:32.88] We will see. I mean, you can ask me the
[L1856] [01:34:34.88] same question again in 10 years and
[L1857] [01:34:36.72] there will be more knowledge and uh
[L1858] [01:34:39.84] undoubtedly some of what I said will not
[L1859] [01:34:41.92] be correct and my guess is some of what
[L1860] [01:34:44.32] I say will be correct in 10 years. I'm
[L1861] [01:34:47.76] always told by AI uh proponents that
[L1862] [01:34:53.20] uh either the problem has already been
[L1863] [01:34:55.12] solved or it'll be solved in the next
[L1864] [01:34:57.04] release.
[L1865] [01:34:58.72] But I I hear anthropic 4.7 is having
[L1866] [01:35:04.48] more problems than 4.6
[L1867] [01:35:07.28] uh for reasons I don't understand. But
[L1868] [01:35:11.20] the the idea that the next version will
[L1869] [01:35:15.12] solve the problem uh is is always a a
[L1870] [01:35:18.32] dangerous assumption. Furthermore,
[L1871] [01:35:21.44] it's getting more and more expensive. If
[L1872] [01:35:23.76] you have to build a hundred million uh
[L1873] [01:35:26.56] dollar um
[L1874] [01:35:29.04] center and use and run the electricity
[L1875] [01:35:32.24] for it, how many junior developers uh
[L1876] [01:35:35.60] does it take to be cheaper?
[L1877] [01:35:39.52] um they they're starting to uh need
[L1878] [01:35:42.00] money. It's it's not un problematic and
[L1879] [01:35:47.20] I'm in a sub field where it is probably
[L1880] [01:35:50.08] more problematic than most.
[L1881] [01:35:54.56] One thing I saw in in a profile that you
[L1882] [01:35:57.44] did is they asked you what keeps you
[L1883] [01:36:00.40] going on C++ or what motivates you and
[L1884] [01:36:03.36] you said one is the fun of kind of
[L1885] [01:36:06.72] building the the future and the second
[L1886] [01:36:09.52] thing was the obligation to make sure
[L1887] [01:36:13.12] C++ moves forward and like when you
[L1888] [01:36:16.00] started C++ I can't imagine you knew
[L1889] [01:36:19.04] that you were embarking on a journey for
[L1890] [01:36:21.04] decades and so
[L1891] [01:36:22.64] >> not not decades But I knew it was a
[L1892] [01:36:25.36] longer journey because I knew I couldn't
[L1893] [01:36:27.68] build the language I wanted. I could
[L1894] [01:36:30.64] build a a subset of it. And there was
[L1895] [01:36:33.76] two reasons for that. One was well, I
[L1896] [01:36:36.24] was a I was a team that did it. Um
[L1897] [01:36:39.76] secondly, um so lack of resources, lack
[L1898] [01:36:43.04] of time, and secondly, I didn't have the
[L1899] [01:36:46.08] input needed to make sure that what I
[L1900] [01:36:50.32] designed was right. And so we have the
[L1901] [01:36:53.84] engineering issue. Build what you can,
[L1902] [01:36:56.96] see what works, improve it. And so I
[L1903] [01:37:00.56] knew I was getting into something like
[L1904] [01:37:03.52] that. I knew I was building a language
[L1905] [01:37:06.32] meant to evolve. And meant to evolve
[L1906] [01:37:09.20] means that you make certain decisions in
[L1907] [01:37:12.80] um knowing that that is different. For
[L1908] [01:37:16.16] instance, I that's one reason C++ wasn't
[L1909] [01:37:20.40] just a uh object-oriented programming
[L1910] [01:37:23.52] language because I could see in the
[L1911] [01:37:26.56] world that there was things that didn't
[L1912] [01:37:29.28] seem to fit that paradigm.
[L1913] [01:37:32.16] And so I I knew we would evolve. The
[L1914] [01:37:35.92] other half of that answer to that
[L1915] [01:37:37.92] question, what keeps me going is
[L1916] [01:37:40.16] applications.
[L1917] [01:37:42.00] It's really nice to see interesting uses
[L1918] [01:37:45.44] and in such. So I was at JPL and uh I
[L1919] [01:37:50.40] talked to the people was doing the Mars
[L1920] [01:37:52.16] rovers. That's cool stuff. I've been to
[L1921] [01:37:54.96] J uh I've been to CERN. I'm going to
[L1922] [01:37:57.76] CERN this summer to see how you do high
[L1923] [01:38:00.64] energy physics. I don't know anything
[L1924] [01:38:02.88] about high energy physics. Well,
[L1925] [01:38:05.68] probably more than the average, but but
[L1926] [01:38:08.08] nowhere near being a physicist. And so
[L1927] [01:38:10.80] you can go there and see they do
[L1928] [01:38:12.48] interesting things and there's things
[L1929] [01:38:14.88] that surprise you. So I was talking to a
[L1930] [01:38:18.16] guy in CERN some years ago and
[L1931] [01:38:20.96] [clears throat] his job was to open and
[L1932] [01:38:23.60] close doors.
[L1933] [01:38:27.36] These doors weigh a couple of tons and
[L1934] [01:38:30.64] are made of lead and they move across to
[L1935] [01:38:34.56] close off an area to protect against
[L1936] [01:38:38.16] radiation or something like that. I
[L1937] [01:38:40.08] don't know the details, but the point is
[L1938] [01:38:42.40] he has to start up this door, which is
[L1939] [01:38:45.44] not too hard. You have engines, but then
[L1940] [01:38:47.68] you have to make sure you stop it
[L1941] [01:38:49.52] because when you have a couple of tons
[L1942] [01:38:52.40] uh this wide going into a wall, it will
[L1943] [01:38:56.32] not stop normally. Uh you have to write
[L1944] [01:38:59.04] and the code for that was was
[L1945] [01:39:01.12] interesting. I learned something and uh
[L1946] [01:39:04.08] I still travel around and uh talk to
[L1947] [01:39:07.68] people and see what C++ is being used
[L1948] [01:39:10.56] for and what it can be used for and what
[L1949] [01:39:13.28] it can't be used for. Just learning and
[L1950] [01:39:16.48] learning is fun.
[L1951] [01:39:18.48] >> There's a a few quotes that you have
[L1952] [01:39:20.80] which I thought would be interesting
[L1953] [01:39:22.80] kind of if you could just give some
[L1954] [01:39:24.24] context behind them. Well, one of the
[L1955] [01:39:26.64] quotes is C makes it easy to shoot
[L1956] [01:39:29.84] yourself in the foot. C++ makes it
[L1957] [01:39:32.64] harder, but when you do it, it blows
[L1958] [01:39:34.72] your whole leg off.
[L1959] [01:39:36.16] >> Yeah. Yeah. I I um somebody asked a
[L1960] [01:39:39.20] question at a talk I was given in uh
[L1961] [01:39:43.20] Boston back in the 80s and I shot that
[L1962] [01:39:46.56] one back. Well, not not not thinking. Um
[L1963] [01:39:50.64] but it's a good quote and it's correct.
[L1964] [01:39:53.68] Um,
[L1965] [01:39:55.28] Arnold Penes
[L1966] [01:39:57.28] got in the Nobel Prize in physics, so
[L1967] [01:39:59.12] he's not a nobody, was one trying to
[L1968] [01:40:01.76] explain to a large group of uh, Bell
[L1969] [01:40:07.60] Labs managers about C++.
[L1970] [01:40:11.44] And he says, you can't have a power tool
[L1971] [01:40:16.16] without knowing how to use it. So if you
[L1972] [01:40:19.20] have a saw, you saw like this. If you
[L1973] [01:40:23.04] have a power saw and you try and do
[L1974] [01:40:26.40] that, it'll bounce
[L1975] [01:40:29.12] and you will have to be very lucky not
[L1976] [01:40:31.84] to get hurt.
[L1977] [01:40:34.00] Notice it's roughly the same story.
[L1978] [01:40:37.76] Uh and so what is behind that is if you
[L1979] [01:40:41.92] get a power tool and you misuse it, you
[L1980] [01:40:45.36] will get more uh problems. Get a car
[L1981] [01:40:48.80] that accelerate faster and it can wrap
[L1982] [01:40:51.68] you around the tree uh in a way a
[L1983] [01:40:55.52] old-fashioned slow accelerating car
[L1984] [01:40:58.72] can't. It's fundamental to having power
[L1985] [01:41:01.68] tools.
[L1986] [01:41:03.28] >> You also have this other great quote.
[L1987] [01:41:04.80] It's um nobody should call themselves a
[L1988] [01:41:07.68] professional if they only know one
[L1989] [01:41:09.60] language. I obviously you'd recommend
[L1990] [01:41:12.08] people learn C++, but if they had to
[L1991] [01:41:14.96] know a second or a third language for
[L1992] [01:41:17.04] the sake of you know being a better
[L1993] [01:41:19.68] engineer or programmer, what would you
[L1994] [01:41:21.60] recommend?
[L1995] [01:41:22.72] >> Yeah. And uh if you've heard if you've
[L1996] [01:41:26.72] seen that interview, you'll know I
[L1997] [01:41:28.48] waffle on that deliberately.
[L1998] [01:41:32.24] uh it is not so much which other
[L1999] [01:41:34.56] languages you know but that you get a
[L2000] [01:41:38.56] set of ideas that are embedded in those
[L2001] [01:41:42.08] languages. So what you should do is to
[L2002] [01:41:45.68] learn languages that are different from
[L2003] [01:41:48.08] yours
[L2004] [01:41:49.92] and um I'm not too
[L2005] [01:41:54.72] fuzzy about which languages they are. I
[L2006] [01:41:57.60] think I said uh learn learn a scripting
[L2007] [01:42:02.32] language today that would be Python or
[L2008] [01:42:05.76] JavaScript. Uh then I guess it was Unix
[L2009] [01:42:09.20] shell or something like that. Um have a
[L2010] [01:42:12.72] look at a functional language uh ML or
[L2011] [01:42:16.72] hasll would be obvious uh solutions or
[L2012] [01:42:20.72] just pick something
[L2013] [01:42:23.12] different. The point is that you mustn't
[L2014] [01:42:26.24] get stuck with just what's in your
[L2015] [01:42:29.04] language. It It's like it's not good for
[L2016] [01:42:32.08] you to be monogl
[L2017] [01:42:34.88] you you know what you call somebody who
[L2018] [01:42:37.12] knows three languages triilingual who
[L2019] [01:42:39.76] knows two languages bilingual
[L2020] [01:42:42.56] uh one language American [laughter]
[L2021] [01:42:45.68] is a a very popular joke at least
[L2022] [01:42:48.08] outside America.
[L2023] [01:42:50.16] Um, and it's the same idea with
[L2024] [01:42:52.72] programming languages, but it's more
[L2025] [01:42:54.56] important with programming languages, I
[L2026] [01:42:56.64] think. Um, because uh you you're you're
[L2027] [01:43:01.28] building things and you shouldn't you
[L2028] [01:43:03.92] you should broaden your mind uh with
[L2029] [01:43:06.80] ideas and techniques.
[L2030] [01:43:08.88] >> Another quote is people people who think
[L2031] [01:43:11.12] they know everything really annoy those
[L2032] [01:43:14.08] of us who know we don't. And I was
[L2033] [01:43:17.12] curious the context behind that or your
[L2034] [01:43:19.20] thoughts on
[L2035] [01:43:20.00] >> Well, that's I mean that's that's very
[L2036] [01:43:22.08] simple. It's there's so many people who
[L2037] [01:43:26.72] who who think there simple solutions to
[L2038] [01:43:29.52] just about everything in the world. Uh
[L2039] [01:43:32.00] in this context they they'll come and
[L2040] [01:43:34.32] tell me how how much simpler C++ could
[L2041] [01:43:37.12] be. And this is true. Um if you only
[L2042] [01:43:42.00] want to do one thing usually the one
[L2043] [01:43:44.32] they have in mind you can make a much
[L2044] [01:43:47.12] simp simpler language but
[L2045] [01:43:50.64] this is like uh if we throw away this
[L2046] [01:43:53.36] part of C++ it will be much simpler
[L2047] [01:43:56.40] nicer usually they want to throw away
[L2048] [01:43:58.96] things like C. So but then you annoy a
[L2049] [01:44:02.56] few million people
[L2050] [01:44:04.88] and you don't actually succeed because
[L2051] [01:44:06.96] they'll stick to the old stuff. So um
[L2052] [01:44:10.88] it's a it's a way of expressing my
[L2053] [01:44:15.12] frustration with people who
[L2054] [01:44:16.64] oversimplify.
[L2055] [01:44:18.64] Uh people think they can program without
[L2056] [01:44:21.92] being learning to program. Uh they think
[L2057] [01:44:25.36] they can be engineers without learning
[L2058] [01:44:27.60] engineering. They think they can be
[L2059] [01:44:30.24] politicians without knowing how to run a
[L2060] [01:44:33.76] company or a country. Um it's it's
[L2061] [01:44:37.92] oversimplification annoys me and I
[L2062] [01:44:41.12] probably shouldn't express annoyance. I
[L2063] [01:44:43.36] very rarely do but uh in this particular
[L2064] [01:44:46.96] case it my my frustration showed.
[L2065] [01:44:50.56] >> Yeah. I think I saw somewhere kind of in
[L2066] [01:44:52.80] response to C++ being difficult for some
[L2067] [01:44:56.48] people people who have the perspective
[L2068] [01:44:58.56] of you know programming should be
[L2069] [01:45:00.80] approachable and you know anyone can
[L2070] [01:45:03.20] learn programming. And I think you you
[L2071] [01:45:05.52] expressed the opinion that C++ is not
[L2072] [01:45:09.20] necessarily for everyone. It's for
[L2073] [01:45:10.96] serious programmers.
[L2074] [01:45:12.16] >> Yeah. I mean uh the the first
[L2075] [01:45:16.96] line of the C++ programming language uh
[L2076] [01:45:21.52] version one first edition was uh C++ is
[L2077] [01:45:28.24] designed to make life more pleasant for
[L2078] [01:45:32.08] the serious programmer and I took away
[L2079] [01:45:36.08] the first version which was professional
[L2080] [01:45:38.40] because I saw amateurs that was really
[L2081] [01:45:40.56] really good. So a serious programmer is
[L2082] [01:45:45.12] probably programming for somebody else.
[L2083] [01:45:48.80] If you program for yourself, it doesn't
[L2084] [01:45:50.88] matter. It's your it's it's you. Uh and
[L2085] [01:45:55.28] that's your problem. If you do it for
[L2086] [01:45:57.84] your friends, you can lose friends. If
[L2087] [01:46:00.32] you build something for a million
[L2088] [01:46:02.32] people, you can do harm in the world.
[L2089] [01:46:05.60] And so that's what it's for. Um
[L2090] [01:46:10.96] I uh I mean Gildolf and Russen built um
[L2091] [01:46:15.36] built Python with the explicit aim of
[L2092] [01:46:18.64] allowing many people or even or
[L2093] [01:46:21.20] everybody to program and he succeeded.
[L2094] [01:46:25.76] I designed C++ to be a really good tool
[L2095] [01:46:29.92] for serious programmers, for engineers
[L2096] [01:46:32.72] and mathematicians and such and I
[L2097] [01:46:35.52] succeeded too.
[L2098] [01:46:37.76] Um, it's just not the same problem.
[L2099] [01:46:40.88] Remember where we started? I said the
[L2100] [01:46:43.28] problem look at the problem and then
[L2101] [01:46:45.20] learn from uh what worked and what
[L2102] [01:46:47.52] doesn't. Looking back on C++ and the
[L2103] [01:46:50.88] whole journey, is there any part where
[L2104] [01:46:53.76] you think oh that that was a mistake or
[L2105] [01:46:55.84] something that you learned from in the
[L2106] [01:46:57.76] design?
[L2107] [01:47:00.24] >> Many many uh times I learned something.
[L2108] [01:47:04.96] Um
[L2109] [01:47:08.32] I think most of the things never made it
[L2110] [01:47:12.00] into C++.
[L2111] [01:47:14.08] That is that's what you have experiments
[L2112] [01:47:16.72] for.
[L2113] [01:47:18.48] And that's what you have initial uses
[L2114] [01:47:21.92] for.
[L2115] [01:47:24.56] I think I got the major part of the
[L2116] [01:47:28.24] language right
[L2117] [01:47:30.80] and I think I could improve every single
[L2118] [01:47:34.32] detail.
[L2119] [01:47:36.56] But
[L2120] [01:47:38.16] stability, compatibility
