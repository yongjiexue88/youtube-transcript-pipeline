Chunk 6; segments 1856–2103. Start may repeat the previous chunk for context.

# The Co-Creator of Kubernetes: Engineering-Led Direction and Convincing Management | Brendan Burns

Source ID: source-176a06af7f6bc865
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/The_Co-Creator_of_Kubernetes_Engineering-Led_Direction_and_Convincing_Management_Brendan_Burns_en.txt
Video: https://www.youtube.com/watch?v=FKijpCEH9D8

[L1865] [59:43.44] plan.
[L1866] [59:44.56] I've never had a plan for my career.
[L1867] [59:46.28] Like, never ever ever.
[L1868] [59:48.28] Like, I've always just chased after
[L1869] [59:50.04] things that I thought were useful and or
[L1870] [59:51.52] fun and interesting.
[L1871] [59:53.64] Um
[L1872] [59:54.72] and
[L1873] [59:56.36] uh and, you know, obviously like that
[L1874] [59:58.80] can work out badly for people. I'm sure
[L1875] [01:00:00.44] it's good to have a plan probably for
[L1876] [01:00:01.88] some people, but like I also want to
[L1877] [01:00:03.28] make sure people understand that like
[L1878] [01:00:05.32] when you look back
[L1879] [01:00:07.12] sometimes the things you think were
[L1880] [01:00:08.44] mistakes or dead ends, like
[L1881] [01:00:10.96] actually were critical things that
[L1882] [01:00:12.28] taught you stuff.
[L1883] [01:00:13.64] Um
[L1884] [01:00:15.16] and so like worrying about did I choose
[L1885] [01:00:17.00] the wrong thing? Am I going to choose
[L1886] [01:00:18.40] the wrong thing? Like, eh,
[L1887] [01:00:20.36] as long as you're learning, you're
[L1888] [01:00:21.68] probably doing okay.
[L1889] [01:00:23.12] >> I mean, what you're describing it
[L1890] [01:00:24.56] reminds me of I don't know if you've
[L1891] [01:00:25.80] seen that Steve Jobs commencement
[L1892] [01:00:27.76] speech, but he
[L1893] [01:00:29.36] he literally says exactly that. You
[L1894] [01:00:32.08] wrote down somewhere I I don't fully
[L1895] [01:00:34.52] remember where you wrote this down, but
[L1896] [01:00:35.88] I have this in my notes. It says,
[L1897] [01:00:37.84] "The inevitable trajectory of software
[L1898] [01:00:40.20] is death."
[L1899] [01:00:41.52] And I just can't imagine Kubernetes
[L1900] [01:00:44.04] dying, but I how do you see that
[L1901] [01:00:46.48] happening and you know, what what do you
[L1902] [01:00:48.20] think about that if it did?
[L1903] [01:00:50.52] >> I mean, I definitely stick by that uh
[L1904] [01:00:53.56] that statement. Um
[L1905] [01:00:55.48] Although I think that the the the the
[L1906] [01:00:57.12] the sense before I said that was you
[L1907] [01:00:59.96] really should never fall in love with
[L1908] [01:01:01.48] your software
[L1909] [01:01:03.04] because the inevitable
[L1910] [01:01:04.96] trajectory of software is death. I am
[L1911] [01:01:08.00] It's which means don't stick with it
[L1912] [01:01:09.32] don't stick with it past when it's
[L1913] [01:01:11.04] dying, right? Um
[L1914] [01:01:13.40] like you should always be willing to
[L1915] [01:01:14.40] throw away stuff. Just don't stick with
[L1916] [01:01:15.96] it just cuz you wrote it. You should
[L1917] [01:01:17.32] always be willing to throw it away.
[L1918] [01:01:19.36] But, like obviously I think if you look
[L1919] [01:01:21.88] historically across the industry, it's
[L1920] [01:01:23.44] it's true, too, right? Like like
[L1921] [01:01:26.72] Um and and quite frankly, like even
[L1922] [01:01:28.52] within Kubernetes, like
[L1923] [01:01:30.40] the source code that I wrote has been
[L1924] [01:01:32.40] rewritten a number of times.
[L1925] [01:01:34.44] Um
[L1926] [01:01:36.24] over the 10-plus years history of the
[L1927] [01:01:37.88] project. Um
[L1928] [01:01:39.28] so, what does it look like? I mean, I
[L1929] [01:01:40.56] think it looks like uh
[L1930] [01:01:42.48] something coming along that achieves
[L1931] [01:01:44.92] similar things, but easier with more uh
[L1932] [01:01:49.20] you know, you with with less complexity
[L1933] [01:01:50.92] and and more utility. Um and and I think
[L1934] [01:01:53.64] that
[L1935] [01:01:54.96] you know, I can imagine what that looks
[L1936] [01:01:56.72] like. Like I think some of these natural
[L1937] [01:01:58.64] language stuff, if you could actually
[L1938] [01:02:00.56] really get it to be an interface that
[L1939] [01:02:01.92] worked 100% of the time, like obviously,
[L1940] [01:02:04.64] it's way easier to come in and say
[L1941] [01:02:07.12] I would like a reliable web service than
[L1942] [01:02:08.80] it is to say "YAML YAML YAML YAML YAML."
[L1943] [01:02:11.60] You know, I I think sometimes I I think
[L1944] [01:02:13.16] it's sort of your two different
[L1945] [01:02:14.12] trajectories. Like sometimes the
[L1946] [01:02:15.16] trajectory is
[L1947] [01:02:16.88] it it goes away. Sometimes it just
[L1948] [01:02:18.36] becomes so hidden that nobody sees it.
[L1949] [01:02:20.92] Right? Like underneath Linux, there's
[L1950] [01:02:24.16] I mean, excuse me, underneath
[L1951] [01:02:24.96] Kubernetes, there's Linux. And
[L1952] [01:02:26.20] underneath Linux, there's a processor.
[L1953] [01:02:28.40] But, you know, people don't pay much
[L1954] [01:02:29.44] attention to that. Um
[L1955] [01:02:31.60] and there's a lot of attention now on
[L1956] [01:02:32.72] AI, and underneath a lot of the AI is
[L1957] [01:02:34.72] Linux, but it could be that people focus
[L1958] [01:02:36.28] so much on the AI that they forget about
[L1959] [01:02:38.64] the Kubernetes part.
[L1960] [01:02:40.36] Um
[L1961] [01:02:41.40] and I think that's happening already,
[L1962] [01:02:42.60] honestly. Like I feel like
[L1963] [01:02:44.56] if I look at the volume of changes and
[L1964] [01:02:46.56] things like that, like I think it's you
[L1965] [01:02:48.20] know, I think we've sort of plateaued in
[L1966] [01:02:49.44] terms of like the amount of change
[L1967] [01:02:51.60] that's driving through the system. Um
[L1968] [01:02:54.20] stuff needed to support AI is kind of
[L1969] [01:02:55.92] like the
[L1970] [01:02:57.20] exception to that category.
[L1971] [01:02:59.12] Um
[L1972] [01:03:01.00] but, you know, I I I
[L1973] [01:03:03.56] I'd be shocked. I mean, I guess I'll put
[L1974] [01:03:04.80] it this way. Like let me take the long
[L1975] [01:03:05.88] view and say
[L1976] [01:03:07.28] in 100 years,
[L1977] [01:03:09.12] is Kubernetes still going to be running?
[L1978] [01:03:10.56] I'd be pretty surprised.
[L1979] [01:03:12.49] >> [laughter]
[L1980] [01:03:12.96] >> Right?
[L1981] [01:03:14.24] It's hard to imagine, right?
[L1982] [01:03:16.52] Um that that that would be true. I mean,
[L1983] [01:03:18.24] I don't know. We haven't had computing
[L1984] [01:03:19.36] systems for long enough to maybe know
[L1985] [01:03:20.76] for certain.
[L1986] [01:03:21.96] Um
[L1987] [01:03:24.08] and there are things that we still use.
[L1988] [01:03:26.00] I mean, there is some stuff that we
[L1989] [01:03:27.64] still use from back then. Plugs are
[L1990] [01:03:29.24] still the same shape-ish, stuff like
[L1991] [01:03:31.36] that.
[L1992] [01:03:32.28] Um
[L1993] [01:03:33.48] so maybe.
[L1994] [01:03:34.64] But even like something like x86, like
[L1995] [01:03:36.12] if you'd asked me 6 years ago and said,
[L1996] [01:03:38.24] "Is the x86 processor going away?"
[L1997] [01:03:41.04] I'd say like, "Well, maybe on I mean,
[L1998] [01:03:43.16] obviously on mobile it did, but like in
[L1999] [01:03:45.60] the server?
[L2000] [01:03:47.36] Maybe not." Um but now two things have
[L2001] [01:03:50.44] happened. One is all the processing is
[L2002] [01:03:51.76] on GPU now.
[L2003] [01:03:53.08] And two, like arm 64 is now pretty
[L2004] [01:03:56.40] important platform on the server for
[L2005] [01:03:57.88] energy usage and other reasons, right?
[L2006] [01:04:00.44] And so
[L2007] [01:04:02.04] it's pretty dangerous to predict the
[L2008] [01:04:03.28] future cuz like
[L2009] [01:04:05.20] it has a tendency of show up sooner than
[L2010] [01:04:06.96] you you you predict. So, or or longer
[L2011] [01:04:09.60] than you predict, too, right?
[L2012] [01:04:10.80] Self-driving cars, like I've heard I've
[L2013] [01:04:12.52] heard self-driving cars were 5 years
[L2014] [01:04:14.20] away for like the last 15 years.
[L2015] [01:04:16.68] >> [laughter]
[L2016] [01:04:16.84] >> Yeah. Uh,
[L2017] [01:04:18.32] me too. I I don't know if you read books
[L2018] [01:04:21.48] for career's sake, but if you do, is
[L2019] [01:04:24.12] there a book that impacted your career
[L2020] [01:04:26.08] the most?
[L2021] [01:04:27.44] >> Well, I mean, I would say like early on
[L2022] [01:04:29.08] the book that that impacted my career
[L2023] [01:04:30.72] the most was a book uh was the gang of
[L2024] [01:04:32.72] four book. Was it software engineering
[L2025] [01:04:35.04] designs and patterns or whatever? Like
[L2026] [01:04:36.48] it's a software engineering book.
[L2027] [01:04:37.92] >> I I see it. It's design patterns,
[L2028] [01:04:39.88] elements of reusable object-oriented
[L2029] [01:04:42.80] software.
[L2030] [01:04:43.48] >> Yeah, there you go. So, that like early
[L2031] [01:04:44.88] on that was a very influential book.
[L2032] [01:04:46.28] It's like a late '90s or mid '90s kind
[L2033] [01:04:48.16] of book. Uh there's a much more recent
[L2034] [01:04:50.56] book called uh Leadership on the Line
[L2035] [01:04:53.44] that as I've become sort of a large org
[L2036] [01:04:55.04] leader, that's uh I really like that
[L2037] [01:04:57.52] book. And then there's this What's this
[L2038] [01:04:59.32] book? It's called I think Five
[L2039] [01:05:00.32] Dysfunctions of Teams, I think. That's a
[L2040] [01:05:02.52] really good book, too, for uh from a
[L2041] [01:05:04.16] like a how teams operate perspective.
[L2042] [01:05:07.68] >> If I'm understanding if you're an if
[L2043] [01:05:09.08] you're an engineer,
[L2044] [01:05:10.40] check out that first book. If you're a
[L2045] [01:05:11.92] manager or a leader, check out the
[L2046] [01:05:13.80] second two books. Yeah, that's probably
[L2047] [01:05:15.40] about right. Yeah, I think that's I
[L2048] [01:05:16.88] think that's right. And then, you know,
[L2049] [01:05:17.80] it's an evolution over time, right? So,
[L2050] [01:05:19.28] like, maybe you'll do both.
[L2051] [01:05:21.88] Uh last question for you is
[L2052] [01:05:23.92] um if you could go back to yourself when
[L2053] [01:05:26.00] you just graduated college and give
[L2054] [01:05:28.12] yourself some advice,
[L2055] [01:05:29.84] what would you say?
[L2056] [01:05:31.60] >> Uh keep better notes.
[L2057] [01:05:33.64] You know, I feel like there's a great
[L2058] [01:05:35.12] MBA thesis or a great like book
[L2059] [01:05:38.36] in the whole Kubernetes journey and
[L2060] [01:05:40.88] beyond and like
[L2061] [01:05:42.56] I you know, like I don't I just don't
[L2062] [01:05:43.84] have enough notes to
[L2063] [01:05:45.64] uh to to do that, to write it down. You
[L2064] [01:05:48.32] know, I like we we went through a lot
[L2065] [01:05:49.76] like a lot of different stuff happened,
[L2066] [01:05:51.28] and I remember some of it, and I don't
[L2067] [01:05:53.16] remember a lot of it, and it would I
[L2068] [01:05:55.04] would have been nicer if I'd kept better
[L2069] [01:05:56.52] notes, I feel like.
[L2070] [01:05:57.88] >> All right. Well, well, you got all the
[L2071] [01:05:59.00] code there. Maybe an LLM can parse it or
[L2072] [01:06:01.48] something. You can reach out
[L2073] [01:06:02.96] >> more It's not so much about the notes
[L2074] [01:06:04.48] part. It's not so much about the code
[L2075] [01:06:05.64] part. It's like all of the Like the
[L2076] [01:06:07.36] stuff you were talking about, like all
[L2077] [01:06:08.40] the partner discussions and all of the
[L2078] [01:06:11.00] like interpersonal stuff and, you know,
[L2079] [01:06:13.72] all that kind of stuff. And like I
[L2080] [01:06:15.64] remember a lot of it, but I don't
[L2081] [01:06:16.88] remember all of it.
[L2082] [01:06:18.20] >> Cool. Well, thank you so much for your
[L2083] [01:06:19.64] time, Brendan. I really appreciate it.
[L2084] [01:06:21.12] >> Yeah, for sure. Thank you.
[L2085] [01:06:22.88] >> Thank you for listening to the podcast.
[L2086] [01:06:24.56] It's a passion project of mine that I've
[L2087] [01:06:26.72] really enjoyed building. Another passion
[L2088] [01:06:28.80] project that I've been working on kind
[L2089] [01:06:30.16] of in secret is building an ergonomic
[L2090] [01:06:32.68] keyboard that I wish existed, and I
[L2091] [01:06:34.92] finally have a prototype, so I'd love to
[L2092] [01:06:36.64] show you what we've built. It's ultra
[L2093] [01:06:39.44] low profile and ergonomic, and I
[L2094] [01:06:41.96] couldn't find anything like it on the
[L2095] [01:06:43.16] market, so that's why we built it. I'll
[L2096] [01:06:45.16] put a link to the keyboard in the
[L2097] [01:06:46.36] description. You can take a look and
[L2098] [01:06:47.96] learn more about the project there. We
[L2099] [01:06:49.80] could definitely use your support. Also,
[L2100] [01:06:51.80] if you have any feedback for me about
[L2101] [01:06:53.44] the show, I'd love to hear it. Comments
[L2102] [01:06:55.88] on YouTube have led to guests coming on
[L2103] [01:06:57.88] like Ilya Grigorik and David Fowler. I
[L2104] [01:07:00.92] wasn't aware of them until someone
[L2105] [01:07:02.76] dropped a comment. Also, feedback in the
[L2106] [01:07:04.64] comments helped me learn to reduce the
[L2107] [01:07:06.32] number of cliff hangers in the intros.
[L2108] [01:07:08.96] So, your comments definitely make a
[L2109] [01:07:10.24] difference. Please keep letting me know
[L2110] [01:07:11.92] what you'd like to see more of in the
[L2111] [01:07:13.28] show, and I'll see you in the next
[L2112] [01:07:14.68] episode.
