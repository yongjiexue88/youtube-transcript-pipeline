Chunk 7; segments 1994–2333. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L2003] [01:11:54.96] right? Just a decision someone could
[L2004] [01:11:56.88] make.
[L2005] [01:11:58.48] Once you've made that decision,
[L2006] [01:12:01.76] you have now locked in the fact that the
[L2007] [01:12:06.16] iteration
[L2008] [01:12:08.16] on the design
[L2009] [01:12:10.16] will be slower across that boundary than
[L2010] [01:12:13.28] it is interior to either of the two
[L2011] [01:12:15.36] parts. So for example, your ability to
[L2012] [01:12:18.56] improve the design of the wheels on
[L2013] [01:12:21.12] their own and my design ability to
[L2014] [01:12:24.00] design the body of the car uh and
[L2015] [01:12:26.00] improve that on its own will be much
[L2016] [01:12:28.16] faster than our ability to design the
[L2017] [01:12:30.00] interface between the wheels and the
[L2018] [01:12:31.44] tire like or or it's not even just the
[L2019] [01:12:33.92] interface. The
[L2020] [01:12:36.72] degree of harmony between the designs.
[L2021] [01:12:38.72] So the degree to which your wheels
[L2022] [01:12:40.48] complement my body design and my body
[L2023] [01:12:42.40] design complements your wheels that they
[L2024] [01:12:44.00] there's that they all are considering
[L2025] [01:12:45.44] the trade-offs together right
[L2026] [01:12:48.64] and Melvin Conway's paper which lays
[L2027] [01:12:50.48] this out uh this is a very early paper
[L2028] [01:12:53.12] it's you know it's in the 60s at least
[L2029] [01:12:56.00] was it in the 50s it's it's way back
[L2030] [01:12:58.64] when that lays this out points out the
[L2031] [01:13:02.16] consequence of this is that products
[L2032] [01:13:06.24] or any and when I say product I mean
[L2033] [01:13:08.00] anything that comes out of one of these
[L2034] [01:13:09.28] design processes or development
[L2035] [01:13:10.56] processes. Products will will have a
[L2036] [01:13:14.88] similar structure to the organization
[L2037] [01:13:16.56] that produced them. You will be able to
[L2038] [01:13:19.52] see in the product evidence of this
[L2039] [01:13:23.20] because the degree to which things are
[L2040] [01:13:26.24] able to harmonize is restricted across
[L2041] [01:13:28.48] that boundary. So when you look at the
[L2042] [01:13:30.40] object, it will have that boundary
[L2043] [01:13:32.64] visible in some way, right? It won't be
[L2044] [01:13:35.36] quite as good at the interface between
[L2045] [01:13:38.48] these two things or in the way that they
[L2046] [01:13:41.04] work together as the things are
[L2047] [01:13:43.52] themselves in inside like to themselves,
[L2048] [01:13:46.56] right?
[L2049] [01:13:48.32] And it gets sort of flattened like one
[L2050] [01:13:50.16] way the the rule is pithly stated is
[L2051] [01:13:52.00] like products look like the org chart,
[L2052] [01:13:54.40] right? But that's not exactly what it
[L2053] [01:13:57.12] says, but that's kind of a downstream
[L2054] [01:13:59.28] consequence. And boy, do you ever see it
[L2055] [01:14:02.88] in the real world. So, you know,
[L2056] [01:14:06.16] >> I've heard that in in the context of
[L2057] [01:14:08.24] these big tech companies, like almost
[L2058] [01:14:10.00] like it's a like a bad thing to quote
[L2059] [01:14:12.72] unquote ship your org chart or
[L2060] [01:14:14.80] basically, you know, the product you put
[L2061] [01:14:17.04] out there is has these uh inorganic
[L2062] [01:14:21.60] >> Yes.
[L2063] [01:14:22.00] >> You know, things. So, it sounds similar
[L2064] [01:14:23.76] to what you're saying.
[L2065] [01:14:25.04] >> Yeah. It's And I think like part of the
[L2066] [01:14:27.36] reason I think it is kind of an
[L2067] [01:14:28.64] unbreakable law is I think it's somewhat
[L2068] [01:14:30.32] unavoidable. uh it's more something that
[L2069] [01:14:32.56] you just have to be aware of and
[L2070] [01:14:34.00] mitigate to the degree that you can like
[L2071] [01:14:36.08] you just have to understand look that
[L2072] [01:14:39.36] lower communication time uh whether it's
[L2073] [01:14:42.96] humans or computers or whoever is doing
[L2074] [01:14:45.20] this work that lower communication time
[L2075] [01:14:49.60] uh or I should say that uh that lower
[L2076] [01:14:51.20] communication bandwidth is what um that
[L2077] [01:14:55.36] just means that we will like where we
[L2078] [01:14:58.24] draw these lines has consequences for
[L2079] [01:15:00.16] what we ship And so we really want to
[L2080] [01:15:03.12] try over time to align those boundary
[L2081] [01:15:06.72] drawings
[L2082] [01:15:08.40] to places where it will have the least
[L2083] [01:15:11.20] bad impact on the result of the product.
[L2084] [01:15:14.56] And you know that's true for org charts.
[L2085] [01:15:16.96] Like I said, I suspect it will also
[L2086] [01:15:18.48] become true for AIs and things like that
[L2087] [01:15:20.80] where it's like you will want to
[L2088] [01:15:22.56] partition these problems in ways that
[L2089] [01:15:24.48] respect that um that line drawing
[L2090] [01:15:27.60] because that will be less good than the
[L2091] [01:15:30.56] thing that can be wholly solved um you
[L2092] [01:15:33.04] know by one one unit whatever that unit
[L2093] [01:15:35.68] is. And so to me uh it's a very helpful
[L2094] [01:15:39.36] construct for thinking about things.
[L2095] [01:15:40.80] It's also a very good explanation for
[L2096] [01:15:42.32] why you see some things somewhere you're
[L2097] [01:15:43.68] like why isn't this just integrated in
[L2098] [01:15:45.44] this? It's like because they were two
[L2099] [01:15:46.80] different teams,
[L2100] [01:15:48.16] >> you know? It's like I'm sorry. Like I'm
[L2101] [01:15:49.44] so like I'm sorry that's just the
[L2102] [01:15:50.96] answer. And you know, it costs a lot
[L2103] [01:15:52.96] more for those two teams to have
[L2104] [01:15:54.16] integrated this. That's not how we work,
[L2105] [01:15:56.88] right?
[L2106] [01:15:57.84] >> I I'd love to hear more about I guess
[L2107] [01:16:00.64] your career and how you got into
[L2108] [01:16:03.12] programming.
[L2109] [01:16:04.32] >> I started programming when I was really
[L2110] [01:16:06.00] little because my father worked at
[L2111] [01:16:07.84] Digital Equipment Corporation, which is
[L2112] [01:16:10.56] actually a very important company in
[L2113] [01:16:13.12] that era. no longer exist, right? This
[L2114] [01:16:15.84] was the they would they would be sort of
[L2115] [01:16:17.76] like almost like a case study in how not
[L2116] [01:16:21.52] adapting to a change in technology uh
[L2117] [01:16:25.84] leads to your demise. They were one of
[L2118] [01:16:28.48] the most important companies in the
[L2119] [01:16:30.24] world for computing. If you ever heard
[L2120] [01:16:31.68] of a PDP11 or a vax in computing
[L2121] [01:16:34.56] history, that's them, right? They made
[L2122] [01:16:36.64] these things that were foundational
[L2123] [01:16:38.32] computers in computing history gone
[L2124] [01:16:40.88] today, right? they were uh part of them
[L2125] [01:16:42.96] got absorbed by Intel, part of them got
[L2126] [01:16:44.56] absorbed by Compact, but they're they
[L2127] [01:16:46.56] don't exist.
[L2128] [01:16:48.32] So he worked for that company
[L2129] [01:16:50.96] and so we always had computers in the
[L2130] [01:16:52.88] home and I learned to program when I was
[L2131] [01:16:54.40] little and that's just sort of always
[L2132] [01:16:56.96] what I wanted to do. I really enjoyed it
[L2133] [01:16:59.36] and so I ended up uh getting an
[L2134] [01:17:02.40] internship at Microsoft when I was
[L2135] [01:17:04.48] pretty young and I met some people
[L2136] [01:17:07.52] there. I came out to I I should say I
[L2137] [01:17:11.36] grew up on the east coast so nowhere
[L2138] [01:17:13.36] near Microsoft. Um I met some people
[L2139] [01:17:15.76] there. I ended up coming out to the west
[L2140] [01:17:17.12] coast really early on. This would be in
[L2141] [01:17:18.88] like 95. Uh so what didn't feel early at
[L2142] [01:17:22.48] the time. It felt late in the computer
[L2143] [01:17:23.92] history but nowadays it's like oh wait
[L2144] [01:17:26.32] 95. Oh my god. Like before before
[L2145] [01:17:28.40] everything was on the web, right? Uh I
[L2146] [01:17:31.04] ended up there was a web though. It was
[L2147] [01:17:32.88] it was nent. Um, I ended up uh coming
[L2148] [01:17:36.88] out and and working sort of in the game
[L2149] [01:17:38.96] industry and that's what I did ever
[L2150] [01:17:41.36] since. And I've mostly always worked on
[L2151] [01:17:44.80] game technology. I'm famously like
[L2152] [01:17:47.76] absolutely terrible at understanding
[L2153] [01:17:49.20] game design. Uh, people who watch my
[L2154] [01:17:51.52] stuff know this about me. Like I'm very
[L2155] [01:17:53.44] very bad at I've tried to make games a
[L2156] [01:17:54.96] couple times and I'm just I just cannot
[L2157] [01:17:56.48] do the design side. I'm awful at it. Uh,
[L2158] [01:17:59.44] but I really enjoy the engine stuff and
[L2159] [01:18:01.28] I've I've uh feel like I I'm o okay at
[L2160] [01:18:04.48] it and I've been able to contribute to
[L2161] [01:18:06.00] projects. Um, so in general, most of the
[L2162] [01:18:09.44] time if you've used code that was
[L2163] [01:18:11.52] written by me, you probably uh used it
[L2164] [01:18:13.68] in the context of like a video game that
[L2165] [01:18:15.60] was using technology that I wrote. And
[L2166] [01:18:17.44] so, you know, an example would be um I
[L2167] [01:18:20.48] worked at Rad Game Tools on a character
[L2168] [01:18:22.16] animation system. Uh, I wrote the entire
[L2169] [01:18:24.48] thing myself that is used well, that's
[L2170] [01:18:26.88] not entirely true. I really think myself
[L2171] [01:18:28.16] except for the texture compressor which
[L2172] [01:18:29.84] uh Jeff Roberts wrote. There was like
[L2173] [01:18:31.20] this texture compressor that you could
[L2174] [01:18:32.56] use um as part of the pipeline for the
[L2175] [01:18:35.12] exporting and stuff like that.
[L2176] [01:18:37.60] And it was a pretty cool project at the
[L2177] [01:18:39.28] time. Um I'm really proud of it. The
[L2178] [01:18:41.60] first version was awful uh as it is
[L2179] [01:18:43.84] because I was pretty new at the time.
[L2180] [01:18:44.88] The second version I thought we did a
[L2181] [01:18:46.00] really nice job. And it was made at a
[L2182] [01:18:48.48] time when people didn't think you could
[L2183] [01:18:50.88] do licensable game technology of that
[L2184] [01:18:53.60] kind because it was too hard to
[L2185] [01:18:55.44] integrate into things like you couldn't
[L2186] [01:18:56.96] get the performance or whatever. And we
[L2187] [01:18:58.64] did a lot of things that I think were
[L2188] [01:18:59.84] pretty innovative at the time and we
[L2189] [01:19:01.60] were able to make something that was
[L2190] [01:19:02.72] very successful. And it's uh I mean we
[L2191] [01:19:05.60] released the first version of that in
[L2192] [01:19:07.36] 99. It's still in use today, largely
[L2193] [01:19:12.00] unchanged from the architecture that I
[L2194] [01:19:14.64] guess was the second version I did in
[L2195] [01:19:15.92] like 2001 or something. Um, there are a
[L2196] [01:19:18.48] few changes to architecture that people
[L2197] [01:19:19.76] have made over the times, but it's
[L2198] [01:19:20.80] largely unchanged. And I mean like I
[L2199] [01:19:23.12] found out recently Balders's Gate 3,
[L2200] [01:19:24.72] which was a big game um from Larian came
[L2201] [01:19:27.60] out. I had no idea. It turns out they
[L2202] [01:19:29.12] still use they use it, right? It's in
[L2203] [01:19:30.64] their engine or whatever. So, I'm very
[L2204] [01:19:32.64] proud of that product because I think it
[L2205] [01:19:34.32] it it was in tons of games and was a
[L2206] [01:19:38.08] very hard problem to solve and I think
[L2207] [01:19:39.28] we solved it pretty well. It's largely
[L2208] [01:19:41.28] irrelevant today. I would say it's still
[L2209] [01:19:43.20] in some people's like engines over time,
[L2210] [01:19:45.04] but like it's not the kind of product
[L2211] [01:19:46.96] you would make today because nowadays
[L2212] [01:19:49.44] engines are monolithic and you license
[L2213] [01:19:51.44] them as a whole typically, right? Like
[L2214] [01:19:53.44] you you wouldn't be getting like a
[L2215] [01:19:56.24] character animation library. it's going
[L2216] [01:19:58.08] to be something that's like built into
[L2217] [01:19:59.68] Unreal Engine or built into Unity,
[L2218] [01:20:01.76] right? So, it's not the kind of product
[L2219] [01:20:03.36] you would probably consider making
[L2220] [01:20:04.56] today. So, that that was mostly um like
[L2221] [01:20:07.20] in terms of things that I've done that
[L2222] [01:20:08.64] people might have actually have
[L2223] [01:20:09.76] experienced or used.
[L2224] [01:20:12.16] Uh like folks at home, if you've played
[L2225] [01:20:14.48] games, you may have played something
[L2226] [01:20:15.84] that I had a hand in at some point, but
[L2227] [01:20:18.64] only the technology, not the design. Uh
[L2228] [01:20:21.12] I also worked uh a little bit on The
[L2229] [01:20:22.96] Witness um which was a game by Jonathan
[L2230] [01:20:25.20] Blow uh and and team uh that I thought
[L2231] [01:20:28.96] was absolutely fantastic and I did some
[L2232] [01:20:30.64] work on uh I did some work on the walk
[L2233] [01:20:32.88] system there that I was I was pretty
[L2234] [01:20:34.24] proud of. I thought it came out pretty
[L2235] [01:20:35.28] well. There's there's some parts of it
[L2236] [01:20:36.56] that are really janky. I I don't think I
[L2237] [01:20:38.32] did a very good job of the actual
[L2238] [01:20:39.68] implementation of it, but the design was
[L2239] [01:20:41.92] pretty good. Let's put it that way.
[L2240] [01:20:44.00] >> Early in your career, so you worked at
[L2241] [01:20:45.36] Microsoft and then and then you went to
[L2242] [01:20:48.24] go
[L2243] [01:20:48.64] >> I I was only ever an intern. I never
[L2244] [01:20:50.40] actually like I mean I guess that's
[L2245] [01:20:51.68] technically working there but I I didn't
[L2246] [01:20:53.20] ever work there as like an employee
[L2247] [01:20:54.80] employee right
[L2248] [01:20:55.76] >> as a someone who's writing code. I mean
[L2249] [01:20:58.72] there's a lot of different paths but
[L2250] [01:21:00.64] there's one one path I imagine is you go
[L2251] [01:21:03.28] and you work at one of these big tech
[L2252] [01:21:05.44] companies and create their tech products
[L2253] [01:21:08.56] I guess and then video gaming seems like
[L2254] [01:21:10.88] another path and I think there's other
[L2255] [01:21:12.56] paths as well of course. Um, what drew
[L2256] [01:21:15.76] you to, you know, going towards video
[L2257] [01:21:18.08] gaming and, you know, not continuing
[L2258] [01:21:21.44] down a Microsoft path or something like
[L2259] [01:21:24.08] that?
[L2260] [01:21:25.84] >> I think that there's a bunch of things I
[L2261] [01:21:29.04] could say about that, but they're
[L2262] [01:21:30.56] probably all BS.
[L2263] [01:21:33.04] The truth is probably that I'm probably
[L2264] [01:21:37.28] more uh affected by the people around me
[L2265] [01:21:41.20] than I would like to admit. I mean, I
[L2266] [01:21:43.76] guess I don't have a problem aditting it
[L2267] [01:21:44.80] now, but I mean, at the time, I probably
[L2268] [01:21:46.56] wouldn't have have said that, right? I
[L2269] [01:21:49.28] could envision a alternate past where I
[L2270] [01:21:52.08] did stay at Microsoft and, you know, try
[L2271] [01:21:54.48] to get a job there and work there
[L2272] [01:21:55.68] instead of being just an intern and then
[L2273] [01:21:57.36] going off and working at a different
[L2274] [01:21:58.64] place.
[L2275] [01:22:00.16] The reason that didn't happen was
[L2276] [01:22:02.16] because of the people who I worked with
[L2277] [01:22:05.68] there when I was an intern. I
[L2278] [01:22:08.64] fundamentally really like like nowadays
[L2279] [01:22:11.44] I fundamentally really love doing things
[L2280] [01:22:14.32] like you know analyzing assembly code or
[L2281] [01:22:18.24] looking at exactly how a micro
[L2282] [01:22:19.76] architecture is working and these sorts
[L2283] [01:22:21.36] of things. If I had gone to Microsoft
[L2284] [01:22:24.40] and had just happened to be under some
[L2285] [01:22:28.00] people who were doing that kind of work
[L2286] [01:22:29.60] and had like taught me how to write like
[L2287] [01:22:31.28] device drivers in assembly language or
[L2288] [01:22:33.12] something like that, I I might still be
[L2289] [01:22:34.72] there today. Right? That's not what
[L2290] [01:22:37.36] happened. The capsule summary is the
[L2291] [01:22:40.00] group that I was supposed to be in. The
[L2292] [01:22:42.00] way that they did internships at that
[L2293] [01:22:43.52] time was that a set of interns, say uh
[L2294] [01:22:47.04] three or four of them would be uh
[L2295] [01:22:50.24] underneath a particular manager who was
[L2296] [01:22:52.48] going to like be managing those interns.
[L2297] [01:22:54.88] So there were a couple of us who were
[L2298] [01:22:57.52] supposed to be reporting to to this guy
[L2299] [01:22:59.52] whose name I won't mention just in case
[L2300] [01:23:01.60] for some reason. It's ancient. He
[L2301] [01:23:03.20] probably wouldn't care at this point,
[L2302] [01:23:04.16] but we're supposed to be reporting to
[L2303] [01:23:05.36] this particular person
[L2304] [01:23:07.52] and literally the week before we arrive,
[L2305] [01:23:11.68] he has this massive flame out with upper
[L2306] [01:23:15.04] management,
[L2307] [01:23:16.64] leaves like just walks out of the
[L2308] [01:23:20.48] building and has not been heard from
[L2309] [01:23:23.36] since.
[L2310] [01:23:25.68] So we show up and it's me um there was
[L2311] [01:23:29.68] like uh me this a guy named Rudy a guy
[L2312] [01:23:33.04] named Rajie uh and we're just interns
[L2313] [01:23:36.48] show up we're like hey how's it going
[L2314] [01:23:39.20] and we we report to this test guy this
[L2315] [01:23:42.80] an SD uh guy named um Scott Leam really
[L2316] [01:23:46.32] nice guy
[L2317] [01:23:48.32] and we're like we're supposed to be like
[L2318] [01:23:49.76] reporting to like a like a program like
[L2319] [01:23:51.36] a you know a software or like what's
[L2320] [01:23:53.76] going on like this one of the guys in
[L2321] [01:23:55.36] the test or he's like, "Yeah, that that
[L2322] [01:23:57.66] [laughter] guy's gone, right?" Like,
[L2323] [01:24:00.64] he's out of here, right? Uh and and me
[L2324] [01:24:03.36] and this other guy, Bruce Johnson, are
[L2325] [01:24:04.96] going to like take care of the interns
[L2326] [01:24:07.52] because
[L2327] [01:24:09.92] right, we don't really know what you're
[L2328] [01:24:12.08] going to do. Uh the first thing I think
[L2329] [01:24:14.40] Bruce Bruce had me do was like an ANI
[L2330] [01:24:16.96] cursor loader. There was there's this
[L2331] [01:24:18.32] format I don't know uh ancient history
[L2332] [01:24:20.40] now, but there's this format for
[L2333] [01:24:21.60] animated cursors on Windows. If you ever
[L2334] [01:24:23.52] see the stupid little walking dinosaur
[L2335] [01:24:25.28] or the like this is no one uses these
[L2336] [01:24:27.60] anymore, I don't think, but they were
[L2337] [01:24:28.96] this thing that were in was in there. He
[L2338] [01:24:30.88] had me write a parser for loading ANI
[L2339] [01:24:32.96] files, right? Like it's just meaningless
[L2340] [01:24:35.04] stuff. Uh, so my experience there was
[L2341] [01:24:37.92] pretty lame. Like I was like, this is
[L2342] [01:24:39.28] kind of dumb. Like I don't really want
