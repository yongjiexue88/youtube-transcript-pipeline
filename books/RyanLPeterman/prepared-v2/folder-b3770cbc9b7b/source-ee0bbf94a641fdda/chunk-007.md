Chunk 7; segments 1898–2194. Start may repeat the previous chunk for context.

# Uber Distinguished Eng: Unfair Promos, Influence, Engineering Regrets | Joakim Recht

Source ID: source-ee0bbf94a641fdda
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Uber_Distinguished_Eng_Unfair_Promos,_Influence,_Engineering_Regrets_Joakim_Recht_en.txt
Video: https://www.youtube.com/watch?v=feNh_ubBAMI

[L1907] [01:14:52.32] fundraising and oh we're about to run
[L1908] [01:14:54.24] out of money and then what and like that
[L1909] [01:14:56.08] whole thing. it can be a bit stressful.
[L1910] [01:14:58.16] Uh [laughter]
[L1911] [01:14:59.52] uh and yeah, so it's it's been good. Uh
[L1912] [01:15:04.88] uh it's been harder than I thought it
[L1913] [01:15:07.28] would be. Uh for for now, I would say
[L1914] [01:15:11.12] still still worth it. Uh not in not in
[L1915] [01:15:15.44] money. Yes, I hope it will eventually.
[L1916] [01:15:18.40] >> Coming to the end of the conversation, I
[L1917] [01:15:20.80] wanted to ask you some career
[L1918] [01:15:22.32] reflection. So, is there an engineering
[L1919] [01:15:25.60] mistake or the the biggest engineering
[L1920] [01:15:27.36] mistake that you saw happen at Uber that
[L1921] [01:15:30.88] was only obvious in hindsight?
[L1922] [01:15:33.60] >> I think it's hard because there were a
[L1923] [01:15:35.20] lot of choices that did not scale,
[L1924] [01:15:39.84] but at the point where they were made,
[L1925] [01:15:42.96] it was kind of the right choice. It's
[L1926] [01:15:45.68] just it got so painful later. Uh, does
[L1927] [01:15:49.04] that mean that you'd have done it
[L1928] [01:15:50.32] differently? I don't necessarily think
[L1929] [01:15:52.56] so. Um like for example I said like at
[L1930] [01:15:57.68] some point we were operating like 50
[L1931] [01:15:59.52] different databases or whatever. Was
[L1932] [01:16:02.08] that wrong as such? Well maybe that
[L1933] [01:16:04.32] maybe somehat that was wrong but but it
[L1934] [01:16:06.96] came out of the idea of like let
[L1935] [01:16:09.04] builders build like just like if you
[L1936] [01:16:11.12] need to do something go nuts. Let not
[L1937] [01:16:13.68] let nobody block you. Which once you're
[L1938] [01:16:17.68] 10 years into it is an insane strategy
[L1939] [01:16:21.28] that's going to like kill you. Uh but in
[L1940] [01:16:25.36] the early days like you don't want a lot
[L1941] [01:16:27.68] of structure. You just because you don't
[L1942] [01:16:29.60] know what you're doing. You don't know
[L1943] [01:16:30.88] if you're going to be successful. You
[L1944] [01:16:32.64] have no idea what's going to happen. So
[L1945] [01:16:34.24] they go nuts. Um I think the hard part
[L1946] [01:16:37.92] is like when do you like when do you
[L1947] [01:16:40.48] expand? When do you contract? like how
[L1948] [01:16:42.88] how do how do you kind of manage that in
[L1949] [01:16:44.96] a good way and that's super hard uh and
[L1950] [01:16:47.28] I think I think some of the things is
[L1951] [01:16:51.20] that I think Uber really should have and
[L1952] [01:16:53.52] I don't really I have not really
[L1953] [01:16:55.20] reflected much on how how we should have
[L1954] [01:16:57.44] done it but that's definitely something
[L1955] [01:16:59.04] where like we should have better at
[L1956] [01:17:01.44] doing those transition from like full
[L1957] [01:17:04.08] freedom to more structure
[L1958] [01:17:06.88] um like one of our prime examples is uh
[L1959] [01:17:10.40] at some point we start doing tracing uh
[L1960] [01:17:12.72] back when Jerger was uh was built uh for
[L1961] [01:17:15.44] for distributed tracing pretty nice and
[L1962] [01:17:18.88] everybody thought this is pretty nice uh
[L1963] [01:17:20.96] and then there was like a mandate to say
[L1964] [01:17:23.28] okay we need to we need to enable
[L1965] [01:17:24.96] tracing all on all all our service
[L1966] [01:17:26.48] because we have a microser we have like
[L1967] [01:17:27.76] a thousands of microservices nobody
[L1968] [01:17:29.12] knows what's going on let's do tracing
[L1969] [01:17:30.80] because that will give us a lot of
[L1970] [01:17:32.00] benefit and then there was an email
[L1971] [01:17:33.92] going out
[L1972] [01:17:35.92] and I don't remember the exact dates I'm
[L1973] [01:17:37.92] guessing the first email was in 15
[L1974] [01:17:39.76] saying oh okay we're doing tracing. All
[L1975] [01:17:42.40] teams must implement tracing.
[L1976] [01:17:45.20] And there probably was a deadline 3
[L1977] [01:17:47.52] months later. And then 3 months later,
[L1978] [01:17:49.60] it's like the same because it had not
[L1979] [01:17:51.84] happened surprisingly. And then it there
[L1980] [01:17:54.64] was just like maybe until maybe 17, 18,
[L1981] [01:17:57.60] they was like, "Okay, this now we're
[L1982] [01:17:59.36] doing it. Now we're doing it." And but
[L1983] [01:18:01.76] it never got done. And somehow the
[L1984] [01:18:03.76] emails just stopped coming, but it never
[L1985] [01:18:05.12] got done. Like for real.
[L1986] [01:18:09.12] So [snorts]
[L1987] [01:18:10.72] that's inability to kind of affect like
[L1988] [01:18:16.00] global change
[L1989] [01:18:18.24] just made so many projects so hard. Um
[L1990] [01:18:22.80] and it's really to a very large degree a
[L1991] [01:18:25.12] cultural problem. But I think it's not
[L1992] [01:18:27.20] just an engineering problem but it's an
[L1993] [01:18:29.12] engineering culture problem. And I think
[L1994] [01:18:30.80] that I think to me that is probably the
[L1995] [01:18:32.56] one of the biggest things that
[L1996] [01:18:36.16] that to some degree hurt the company
[L1997] [01:18:38.24] because there was there's a lot of waste
[L1998] [01:18:40.24] a lot of waste going on. um that was not
[L1999] [01:18:43.28] necessary later on was necessary in the
[L2000] [01:18:45.36] beginning but they don't not um so I
[L2001] [01:18:49.12] don't think I don't have like a concrete
[L2002] [01:18:50.64] like oh then we did this and then it was
[L2003] [01:18:52.40] kind of stupid and we should have done
[L2004] [01:18:53.68] that where where it was like super
[L2005] [01:18:55.92] obvious well okay I'll just mention one
[L2006] [01:18:58.88] thing and that is uh at some point and
[L2007] [01:19:03.76] maybe somebody's going to be super angry
[L2008] [01:19:05.52] about this I don't know but uh at some
[L2009] [01:19:08.08] point we tried to implement uh a a kind
[L2010] [01:19:12.56] of software networking stack. Um and the
[L2011] [01:19:16.40] the team building it was like, "Yeah, so
[L2012] [01:19:18.40] we're going to do this uh thing where
[L2013] [01:19:20.16] you like we're going to build a software
[L2014] [01:19:22.56] network uh uh where like if you are when
[L2015] [01:19:26.72] when when services need to communicate,
[L2016] [01:19:28.64] it goes into an ingress uh and then it
[L2017] [01:19:31.12] gets routed through a network and to a
[L2018] [01:19:32.56] to to to the right service." And that
[L2019] [01:19:34.48] whole thing we implement in node
[L2020] [01:19:38.40] and I like I just distinctly remember
[L2021] [01:19:41.84] there was like a platform tech talk or
[L2022] [01:19:44.08] about like this is like insane but it
[L2023] [01:19:48.24] was back in 16 or whatever and I was
[L2024] [01:19:49.84] like not that senior yet. So I okay but
[L2025] [01:19:52.56] those people are pretty senior they must
[L2026] [01:19:53.84] know what they're talking about. turned
[L2027] [01:19:56.24] out they did not know what they were
[L2028] [01:19:58.48] talking about and that that caused a lot
[L2029] [01:20:00.96] of pain [laughter]
[L2030] [01:20:02.64] and many years of untangling uh and
[L2031] [01:20:06.08] whatever. Um so I think that that was a
[L2032] [01:20:08.72] pretty bad decision.
[L2033] [01:20:11.44] Sorry to anybody who who don't think
[L2034] [01:20:13.12] there was but I think it was
[L2035] [01:20:15.52] >> about Uber's culture. Um earlier you
[L2036] [01:20:19.44] mentioned that especially with the promo
[L2037] [01:20:21.84] committees that there's a bit of a
[L2038] [01:20:24.00] unusual culture of you know everyone
[L2039] [01:20:27.12] needs to sell their managers just
[L2040] [01:20:29.60] present their reports and you just sell
[L2041] [01:20:31.36] it in a big group and you alluded to
[L2042] [01:20:33.84] that at that time there was also some
[L2043] [01:20:35.92] other cultural backlash and I vaguely
[L2044] [01:20:38.32] remember that too like around maybe it
[L2045] [01:20:40.32] was 2017 or something like that where
[L2046] [01:20:42.96] there was a lot of stuff going on at at
[L2047] [01:20:44.88] Uber. What was it like for you
[L2048] [01:20:47.68] experiencing that at the time?
[L2049] [01:20:49.68] >> There's a fairly big cultural difference
[L2050] [01:20:51.28] between Denmark and Silicon Valley. It's
[L2051] [01:20:55.28] very interesting like and in many ways
[L2052] [01:20:58.16] quite entertaining. Um
[L2053] [01:21:01.44] uh so like so it was a bit weird to
[L2054] [01:21:05.04] experience because like many of those
[L2055] [01:21:07.36] problems we just was we just were like
[L2056] [01:21:10.24] are these like is this how people
[L2057] [01:21:12.80] behave? I thought we were just like
[L2058] [01:21:14.64] coding and having fun. [laughter]
[L2059] [01:21:17.36] Like what are you doing over there? Like
[L2060] [01:21:19.60] you're apparently doing something very
[L2061] [01:21:20.96] different. Uh so it was like it was very
[L2062] [01:21:24.96] well first of all quite disconnected
[L2063] [01:21:26.64] because like we were not like we were
[L2064] [01:21:30.08] quite far from that whole thing. Um or
[L2065] [01:21:33.44] maybe it's just me. I was like maybe I
[L2066] [01:21:36.40] was just very naive. I don't know. Um
[L2067] [01:21:39.20] but first of all it was it was good to
[L2068] [01:21:40.56] be at a distance because we like there
[L2069] [01:21:42.32] was a lot of stuff going on. We could
[L2070] [01:21:44.08] just keep on like executing and doing
[L2071] [01:21:45.92] our thing. So in that sense it was nice
[L2072] [01:21:48.16] but it was also it was also insane like
[L2073] [01:21:50.16] so that much stuff that was happening
[L2074] [01:21:51.68] and people leaving getting fired, board
[L2075] [01:21:55.20] members getting kicked out, Travis
[L2076] [01:21:56.96] getting kicked out. A lot of stuff going
[L2077] [01:21:59.28] on was like every day you like what's
[L2078] [01:22:01.36] going to happen now?
[L2079] [01:22:03.60] Um but again daytime quiet here because
[L2080] [01:22:08.72] 9 9 hours time difference we can just do
[L2081] [01:22:11.28] our thing and then whatever happens
[L2082] [01:22:12.88] happens and there's not really anything
[L2083] [01:22:14.40] we can do about it. It's not like not
[L2084] [01:22:16.80] our fault. Uh there's some of it that of
[L2085] [01:22:19.28] course we also have to adapt to. Um but
[L2086] [01:22:23.36] there was very much like when I joined
[L2087] [01:22:25.92] there was very much like every
[L2088] [01:22:28.16] everything was very much about you like
[L2089] [01:22:30.80] performance reviews you promo you
[L2090] [01:22:33.60] conversation you like when you get hired
[L2091] [01:22:36.48] or and you negotiate your salary it's
[L2092] [01:22:38.32] just about how good you are at
[L2093] [01:22:39.60] negotiating. So it's all about you. It's
[L2094] [01:22:41.20] not about the team. The team doesn't
[L2095] [01:22:42.56] matter at all. It doesn't play into
[L2096] [01:22:43.92] anything more or less. uh which is
[L2097] [01:22:46.56] insane to me [laughter] like I don't get
[L2098] [01:22:50.32] it. So even though that was kind of how
[L2099] [01:22:52.80] how Uber works, we had never like gone
[L2100] [01:22:56.00] fully into that mindset. Uh so for for
[L2101] [01:22:59.84] us there wasn't that big of a of a
[L2102] [01:23:01.92] difference. Um it was more like okay now
[L2103] [01:23:04.56] like because I always thought like I
[L2104] [01:23:06.56] just thought that was how it was in the
[L2105] [01:23:08.08] US. Uh, so I was like, "Okay, so Oh,
[L2106] [01:23:10.88] it's not actually like you actually
[L2107] [01:23:13.20] wanted to be different." Like I thought
[L2108] [01:23:15.12] I thought you liked it like that,
[L2109] [01:23:17.05] [laughter] but but you don't I don't I
[L2110] [01:23:19.04] don't know why why you did it like that
[L2111] [01:23:20.40] then. But anyway, but it was very
[L2112] [01:23:22.96] interesting times and there was just a
[L2113] [01:23:24.48] lot of scandals also where we were like
[L2114] [01:23:27.60] why why did you do that? like why did
[L2115] [01:23:31.44] you decide to go to a strip bar or like
[L2116] [01:23:33.44] why did you decide to to kind of uh open
[L2117] [01:23:36.96] up somebody's private data and see where
[L2118] [01:23:39.12] they went? Like what what motivated you
[L2119] [01:23:41.20] to do that? I don't know. [laughter]
[L2120] [01:23:43.60] But like [snorts] what motivates a board
[L2121] [01:23:45.36] member to like on a live stream to the
[L2122] [01:23:48.08] entire company after a sec sexual
[L2123] [01:23:50.48] harassment scandal to say something
[L2124] [01:23:52.40] like, "Yeah, it's going to be nice to
[L2125] [01:23:54.16] get the women on the board because they
[L2126] [01:23:55.76] talk more." [laughter]
[L2127] [01:23:57.04] >> Oh, no. No. What's
[L2128] [01:23:59.44] >> that's so bad? Like what? Like what are
[L2129] [01:24:02.56] you thinking about? Like what is this
[L2130] [01:24:05.20] insanity? I have mixed feelings about
[L2131] [01:24:07.36] it. It was just I was just happy to be
[L2132] [01:24:09.12] at a distance and but sometimes you
[L2133] [01:24:11.04] could also just feel like okay bring out
[L2134] [01:24:12.96] the popcorn and like see what's
[L2135] [01:24:14.16] happening here because like it was just
[L2136] [01:24:16.24] it was very interesting times when I
[L2137] [01:24:18.32] went to the US to visit before 17. You
[L2138] [01:24:21.44] go to some of the offices people like
[L2139] [01:24:23.60] fist bump and then do you want a
[L2140] [01:24:25.84] whiskey? I don't know. It's like Tuesday
[L2141] [01:24:28.64] at 2:00 p.m. I don't know. Do I want
[L2142] [01:24:30.80] whiskey? I don't think so. Like I I
[L2143] [01:24:33.03] [laughter] don't know. Is that a thing?
[L2144] [01:24:35.92] >> If you look back on your career so far
[L2145] [01:24:38.64] and you knowing everything you know now,
[L2146] [01:24:41.04] if if you were to give yourself advice
[L2147] [01:24:43.12] when you just started in your career,
[L2148] [01:24:45.28] what would you say? Just try stuff and
[L2149] [01:24:48.64] don't don't be afraid just because it
[L2150] [01:24:51.12] looks hard or because those other people
[L2151] [01:24:52.72] look much better than you because they
[L2152] [01:24:55.68] might be better than you. Sure, but but
[L2153] [01:24:58.64] you can also get there. It's not it's
[L2154] [01:25:00.56] not it's not rocket science. Uh it it is
[L2155] [01:25:05.28] just computers. Uh and if if you like
[L2156] [01:25:07.52] computers, uh you're pretty well off uh
[L2157] [01:25:10.00] if you just keep going with that. Um, so
[L2158] [01:25:13.52] I think that's probably the main thing
[L2159] [01:25:15.28] in my view. It's like just let let the
[L2160] [01:25:18.56] let your curiosity take you where
[L2161] [01:25:20.48] wherever and don't just don't assume
[L2162] [01:25:23.84] that what you're doing right now is the
[L2163] [01:25:26.08] best thing you can be doing
[L2164] [01:25:28.64] because there's probably something
[L2165] [01:25:30.00] that's even better out there or or or
[L2166] [01:25:32.16] will will be soon. And then
[L2167] [01:25:35.28] don't don't just discard that just
[L2168] [01:25:37.28] because you're kind of having fun kind
[L2169] [01:25:39.68] of having fun now or whatever. Um, of
[L2170] [01:25:42.56] course it might be hard to like tell
[L2171] [01:25:44.80] which what what is better than what you
[L2172] [01:25:46.40] have now. Like you also just have to
[L2173] [01:25:48.32] take a chance sometime.
[L2174] [01:25:49.84] >> Awesome. Well, yeah, thanks so much for
[L2175] [01:25:52.48] your time. I really uh appreciated it
[L2176] [01:25:55.52] for the guests. I'll I'll link to your
[L2177] [01:25:58.08] socials in the show notes. Is there
[L2178] [01:26:00.32] anything else though you want to, you
[L2179] [01:26:02.08] know, point people to? Maybe something
[L2180] [01:26:03.76] you're working on or anything like that?
[L2181] [01:26:06.24] >> I think my LinkedIn profile is probably
[L2182] [01:26:08.00] the the most relevant place because like
[L2183] [01:26:10.16] that's where all the stuff I write. Uh,
[L2184] [01:26:11.92] it goes.
[L2185] [01:26:13.12] >> Okay, cool. Well, thanks so much. I
[L2186] [01:26:14.72] really appreciate it.
[L2187] [01:26:16.00] >> Awesome.
[L2188] [01:26:17.36] >> Thanks for listening to the podcast. I
[L2189] [01:26:19.92] don't sell anything or do sponsorships,
[L2190] [01:26:22.48] but if you want to help out with the
[L2191] [01:26:24.40] podcast, you can support by engaging
[L2192] [01:26:27.44] with the content on YouTube or on
[L2193] [01:26:29.84] Spotify. If you want to drop a review,
[L2194] [01:26:31.52] that'll be super helpful. And if there's
[L2195] [01:26:33.84] any guests that you want to bring on to,
[L2196] [01:26:35.84] please let me know. I feel like sourcing
[L2197] [01:26:38.16] very senior IC's, there's no wellstudied
[L2198] [01:26:42.00] list out there on Google that I can just
[L2199] [01:26:43.76] search this up. So, if there's someone
[L2200] [01:26:45.52] in your org or at your company who you
[L2201] [01:26:47.44] really look up to and you want to hear
[L2202] [01:26:48.80] their career story, let me know and I'll
[L2203] [01:26:51.36] reach out to
