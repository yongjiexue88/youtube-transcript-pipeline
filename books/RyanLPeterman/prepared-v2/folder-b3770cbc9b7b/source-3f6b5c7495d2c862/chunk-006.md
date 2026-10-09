Chunk 6; segments 2000–2396. Start may repeat the previous chunk for context.

# Co-Creator of Haskell: Useless vs Useful Languages, Rust vs C, Functional Programming | Simon Jones

Source ID: source-3f6b5c7495d2c862
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Co-Creator_of_Haskell_Useless_vs_Useful_Languages,_Rust_vs_C,_Functional_Programming_Simon_Jones_en.txt
Video: https://www.youtube.com/watch?v=xcB_LF3cdqw

[L2009] [01:08:19.44] them back."
[L2010] [01:08:21.72] So, of course, those days are long gone.
[L2011] [01:08:23.56] We pay a lot more attention to our users
[L2012] [01:08:25.20] and have much more rigorous CI testing
[L2013] [01:08:27.04] than ever we did, right? So, um
[L2014] [01:08:29.44] that's a that's a a story from a long
[L2015] [01:08:31.04] time ago, but it's a good cultural story
[L2016] [01:08:32.80] because it suggests that we've cared
[L2017] [01:08:34.92] about our users very much, but we we we
[L2018] [01:08:37.76] care about users who want in the in
[L2019] [01:08:39.72] their hearts want to be principled.
[L2020] [01:08:41.40] We're trying to appeal to One One of the
[L2021] [01:08:43.24] things I like best about Haskell is
[L2022] [01:08:44.72] people often say, "I just enjoy writing
[L2023] [01:08:47.64] Haskell."
[L2024] [01:08:48.72] Right? It's fun, right? My boss doesn't
[L2025] [01:08:51.60] allow me to because, you know, it
[L2026] [01:08:55.00] somehow doesn't fit with my production
[L2027] [01:08:56.52] shop. And And I but but for me, I would
[L2028] [01:08:59.16] go for I love writing this stuff every
[L2029] [01:09:02.24] time. Every time. Yeah,
[L2030] [01:09:04.76] that's that's very rewarding to me.
[L2031] [01:09:07.00] >> There's also this interesting, I don't
[L2032] [01:09:09.16] know if it's a cultural value, but it's
[L2033] [01:09:10.96] a statement that you say often in the
[L2034] [01:09:13.12] context of these older talks. You say
[L2035] [01:09:16.12] that you avoid success at all costs.
[L2036] [01:09:19.68] Could Could you explain what you mean by
[L2037] [01:09:21.20] that phrase?
[L2038] [01:09:21.92] >> Oh, yeah, this was just a little a
[L2039] [01:09:23.44] little play on words.
[L2040] [01:09:25.56] It was in a retrospective on Haskell I
[L2041] [01:09:27.48] gave as an invited talk at and um
[L2042] [01:09:30.28] Popple in a long time ago, probably 20
[L2043] [01:09:32.72] years ago. Uh so, it's a it's a little
[L2044] [01:09:35.08] play on words because it you can read it
[L2045] [01:09:36.84] as either avoid success at all costs.
[L2046] [01:09:41.60] And that's what we've been discussing.
[L2047] [01:09:43.20] Success at all costs means compromise
[L2048] [01:09:44.96] your principles in order to satisfy your
[L2049] [01:09:47.08] users or think that you're satisfying
[L2050] [01:09:48.84] users, you know, uh give them what they
[L2051] [01:09:51.24] say they want. Uh where more if we build
[L2052] [01:09:53.52] it, they will come kind of deal, right?
[L2053] [01:09:55.48] So,
[L2054] [01:09:56.48] avoid success at all costs. Or if you
[L2055] [01:09:59.36] parenthesize the other way, it says
[L2056] [01:10:00.76] avoid success
[L2057] [01:10:02.32] at all costs.
[L2058] [01:10:05.44] Or at all costs avoid success. And
[L2059] [01:10:07.84] that's saying uh that's a little joke,
[L2060] [01:10:10.04] but it says if you're too successful and
[L2061] [01:10:12.28] have too many users, it becomes more
[L2062] [01:10:14.24] difficult to make changes.
[L2063] [01:10:17.72] And we experience that right now. So, I
[L2064] [01:10:19.84] devote many many more of my personal
[L2065] [01:10:22.28] cycles to backward compati-
[L2066] [01:10:25.00] compatibility issues than ever I did.
[L2067] [01:10:28.24] I've devoted hundreds of uh you know, uh
[L2068] [01:10:30.72] hours and hours and well,
[L2069] [01:10:32.68] days and days, weeks and weeks in the
[L2070] [01:10:33.88] last year or two to the following what
[L2071] [01:10:36.88] seems to be a very simple property. If
[L2072] [01:10:40.68] if you can compile a program, a package,
[L2073] [01:10:43.60] in a whole program with GHC 10.0 and we
[L2074] [01:10:46.12] release GHC 10.2, you should be able to
[L2075] [01:10:48.32] compile that same package unchanged with
[L2076] [01:10:50.64] GHC 10.2.
[L2077] [01:10:53.36] Seems reasonable, right?
[L2078] [01:10:55.72] After all, 10.2 should just be better.
[L2079] [01:10:58.76] But, no.
[L2080] [01:10:59.88] GHC has never had that property.
[L2081] [01:11:02.20] And making it have that property has
[L2082] [01:11:03.64] turned out to be very, very
[L2083] [01:11:04.92] time-consuming. Previously, we just
[L2084] [01:11:06.48] never cared.
[L2085] [01:11:08.24] Then we started to care, but thought it
[L2086] [01:11:10.20] was a lot of work, and now we're
[L2087] [01:11:11.52] investing the work.
[L2088] [01:11:13.08] >> I guess that was from a long time ago. I
[L2089] [01:11:15.32] think nowadays, software engineering,
[L2090] [01:11:18.08] there's been a major shift in the last
[L2091] [01:11:19.68] year where a lot of code is being
[L2092] [01:11:21.88] generated by these models or these LLMs.
[L2093] [01:11:25.84] How do you see programming language
[L2094] [01:11:27.52] design shifting to accommodate a world
[L2095] [01:11:30.24] where a lot of the code is no longer
[L2096] [01:11:32.48] written by humans?
[L2097] [01:11:34.12] >> I think it may be the best thing that's
[L2098] [01:11:36.36] happened to statically typed languages
[L2099] [01:11:38.08] for a long time.
[L2100] [01:11:40.20] Because, as we've been discussing,
[L2101] [01:11:43.16] with a static type system, you cut down
[L2102] [01:11:46.04] the space of programs that the LLM can
[L2103] [01:11:48.24] generate.
[L2104] [01:11:50.16] Because it is perfectly capable of
[L2105] [01:11:51.96] running the compiler and saying, "Oh,
[L2106] [01:11:53.04] darn, that was a bad program. Better fix
[L2107] [01:11:54.64] it."
[L2108] [01:11:56.24] Right? So, a zillion iterations get done
[L2109] [01:11:59.60] behind the scenes.
[L2110] [01:12:01.92] Whereas in an untyped language, the
[L2111] [01:12:03.24] first one it coughed up, you'd have had
[L2112] [01:12:04.68] to run or run against its test suite, or
[L2113] [01:12:06.76] who knows what, but it's it drastically
[L2114] [01:12:09.36] tightens up that cycle.
[L2115] [01:12:11.36] Right?
[L2116] [01:12:12.32] So, I think that statically typed
[L2117] [01:12:15.08] languages are huge boon for LLMs.
[L2118] [01:12:18.48] Because it's too easy to
[L2119] [01:12:19.92] Programs are just strings, right? We
[L2120] [01:12:21.24] could um
[L2121] [01:12:23.28] They can just generate the next
[L2122] [01:12:24.68] plausible word, uh and you want you want
[L2123] [01:12:27.12] to make any implausible programs,
[L2124] [01:12:28.64] programs that really shouldn't run. You
[L2125] [01:12:29.96] want to make them not run right away.
[L2126] [01:12:31.60] Yeah.
[L2127] [01:12:32.56] >> If there's a slider on, I guess, the
[L2128] [01:12:34.68] strength of a type system, and you know,
[L2129] [01:12:37.68] the other side is weak. What what do you
[L2130] [01:12:39.56] see as the absolute strongest type
[L2131] [01:12:41.48] systems among programming languages?
[L2132] [01:12:43.68] >> Oh, Haskells, I think.
[L2133] [01:12:45.28] Haskell is exploring the bleeding edge.
[L2134] [01:12:48.28] There's an exception, which is that
[L2135] [01:12:49.80] module systems
[L2136] [01:12:52.12] are a um
[L2137] [01:12:54.40] and in particular sort of a functor
[L2138] [01:12:56.12] style module systems are explored much
[L2139] [01:12:59.36] more deeply in um the ML OCaml world.
[L2140] [01:13:04.08] And in the Haskell world we've
[L2141] [01:13:05.44] essentially never gone there. But
[L2142] [01:13:07.36] otherwise I think Haskell's right up
[L2143] [01:13:08.84] there. Now, of course, a language like
[L2144] [01:13:11.04] Scala
[L2145] [01:13:12.36] um
[L2146] [01:13:13.28] is also as the Scala has almost
[L2147] [01:13:17.12] everything Haskell has. I think not
[L2148] [01:13:19.04] quite. Um but it also has subtyping and
[L2149] [01:13:22.24] object oriented type object object
[L2150] [01:13:23.72] orientation. So that's a lot more
[L2151] [01:13:25.40] complicated, a lot more complicated I
[L2152] [01:13:28.08] think.
[L2153] [01:13:29.08] um
[L2154] [01:13:30.80] And they pay a price for it. I think
[L2155] [01:13:32.96] well, you know, Martin Odetsky would
[L2156] [01:13:34.24] agree that they pay a price for it. So
[L2157] [01:13:37.16] uh in complexity it's probably more
[L2158] [01:13:39.40] complicated than Haskell's.
[L2159] [01:13:42.28] um
[L2160] [01:13:44.12] Uh and maybe in terms of power. So maybe
[L2161] [01:13:46.08] I should have said Haskell and Scala are
[L2162] [01:13:47.60] the two lead Haskell, Scala, OCaml.
[L2163] [01:13:49.96] Perhaps I'll just put them in an
[L2164] [01:13:50.84] equivalence class for now. They're not
[L2165] [01:13:52.44] strictly comparable. They all have
[L2166] [01:13:54.16] things that we we in which they're more
[L2167] [01:13:55.56] powerful than the other probably.
[L2168] [01:13:57.52] >> What do you think are, you know, the
[L2169] [01:13:58.96] important problems to solve in the
[L2170] [01:14:01.40] future of programming languages today?
[L2171] [01:14:03.00] Maybe, you know, what are the unsolved
[L2172] [01:14:05.12] problems in the domain that are top of
[L2173] [01:14:07.12] mind for you?
[L2174] [01:14:08.36] >> I think it's actually hard to identify,
[L2175] [01:14:10.08] you know, to say here's a problem we
[L2176] [01:14:11.72] ought to solve, let's try to solve it.
[L2177] [01:14:13.16] But I think
[L2178] [01:14:14.56] another way to tackle is to say what are
[L2179] [01:14:16.60] interesting, you know, new languages out
[L2180] [01:14:19.24] there that are exploring very different
[L2181] [01:14:20.80] parts of the design space. And there I
[L2182] [01:14:22.68] think I do I do have a a candidate. So
[L2183] [01:14:25.20] um the language that is my day job,
[L2184] [01:14:27.24] right? I work for Epic and we're
[L2185] [01:14:28.84] designing a a programming language
[L2186] [01:14:30.16] called Verse.
[L2187] [01:14:32.04] Now Verse is a very exotic language.
[L2188] [01:14:34.28] It's it's really uh a functional logic
[L2189] [01:14:37.56] language. Um
[L2190] [01:14:39.16] So it's yet more expressive than
[L2191] [01:14:40.56] Haskell. It has a static type system but
[L2192] [01:14:42.16] a very different one to Haskell's. So if
[L2193] [01:14:44.80] you like uh the way I think of it is
[L2194] [01:14:46.20] like this. If you look at
[L2195] [01:14:48.00] um
[L2196] [01:14:48.88] uh C and Fortran, they look pretty
[L2197] [01:14:50.52] different if you're an imperative
[L2198] [01:14:52.08] programmer. But if you look at them, if
[L2199] [01:14:53.92] you zoom out so you can see functional
[L2200] [01:14:56.12] languages, then C and Fortran are pretty
[L2201] [01:14:57.72] close together.
[L2202] [01:14:59.24] Um you know, along with object-oriented
[L2203] [01:15:01.20] languages, they're all in a clump,
[L2204] [01:15:02.24] right? And then there's some functional
[L2205] [01:15:03.96] languages, you know, Haskell and ML and
[L2206] [01:15:05.28] OCaml and Scala out here. If you zoom
[L2207] [01:15:07.44] out still further,
[L2208] [01:15:09.04] then um the imperative languages and
[L2209] [01:15:11.24] functional languages are all together,
[L2210] [01:15:12.32] and Verse is way out here.
[L2211] [01:15:15.04] Right? So Verse is exploring a very new
[L2212] [01:15:17.52] point in the design space.
[L2213] [01:15:19.36] But just like functional programming
[L2214] [01:15:21.20] back in 1980,
[L2215] [01:15:23.48] it seems sufficiently interesting and
[L2216] [01:15:25.04] cool and unusual and weird that it's
[L2217] [01:15:27.04] worth exploring, right? So back in 1980,
[L2218] [01:15:30.96] nobody would said, "We're definitely
[L2219] [01:15:32.52] going to do functional programming, and
[L2220] [01:15:33.68] it's going to be useful for practical
[L2221] [01:15:34.68] applications." They said, "That's pretty
[L2222] [01:15:35.72] weird." Uh you know, by all means give
[L2223] [01:15:37.36] it a try, guys. And that's kind of where
[L2224] [01:15:38.96] I'm with Verse. Um Uh one difference is
[L2225] [01:15:41.48] that back in 1980, we were purely
[L2226] [01:15:43.00] academics. And now but Verse is being
[L2227] [01:15:45.12] developed by well, Epic Games.
[L2228] [01:15:47.52] Um so we've got some, you know, much
[L2229] [01:15:49.08] more muscle behind it um than um
[L2230] [01:15:52.28] uh you know, was behind functional
[L2231] [01:15:53.36] programming to begin with. So we'll see.
[L2232] [01:15:54.88] It's a very interesting intellectual
[L2233] [01:15:56.40] endeavor.
[L2234] [01:15:57.80] Adventure, I should say.
[L2235] [01:16:00.08] >> Yeah, I think a lot of people, like
[L2236] [01:16:01.40] students, they may be worried about AI
[L2237] [01:16:04.00] or you know, studying computer science.
[L2238] [01:16:06.28] Would you recommend people learn how to
[L2239] [01:16:09.12] program today given that AI is uh
[L2240] [01:16:12.00] starting to write reasonable code now?
[L2241] [01:16:13.88] >> Oh, yeah. Yeah. So I think people are
[L2242] [01:16:16.16] right to be worried in the sense that I
[L2243] [01:16:17.32] think there's going to be considerable
[L2244] [01:16:18.88] dislocation.
[L2245] [01:16:20.64] Right?
[L2246] [01:16:21.76] It's like, you know,
[L2247] [01:16:22.88] if you were in the industrial
[L2248] [01:16:23.84] revolution, then lots of people lost
[L2249] [01:16:25.52] their jobs as, you know, spinners and
[L2250] [01:16:27.32] weavers. Um
[L2251] [01:16:29.00] and it wasn't easy for them to get a new
[L2252] [01:16:30.48] job in the new economy. Now, the new
[L2253] [01:16:31.88] economy had in the end had more jobs,
[L2254] [01:16:34.36] but
[L2255] [01:16:35.44] there was if you were one of the people
[L2256] [01:16:37.08] who just lost their job, that was not a
[L2257] [01:16:38.32] happy place to be.
[L2258] [01:16:39.96] From our perspective, you know, Olympian
[L2259] [01:16:41.44] perspective of a few hundred years
[L2260] [01:16:42.88] later, we think, well, it's just a blip,
[L2261] [01:16:44.64] right? If you're part of the blip,
[L2262] [01:16:46.76] problem, right? So, I think they're
[L2263] [01:16:49.16] right to be worried.
[L2264] [01:16:51.80] Um we don't know how things will shake
[L2265] [01:16:53.68] out. I'm actually optimistic that in the
[L2266] [01:16:56.20] medium term, if we don't, you know,
[L2267] [01:16:57.36] destroy ourselves with some truly
[L2268] [01:16:59.20] existential thing, but from an
[L2269] [01:17:00.64] employment market point of view, I'm
[L2270] [01:17:02.36] optimistic that in the end, you know,
[L2271] [01:17:04.44] we'll just be in a higher place that AIs
[L2272] [01:17:06.84] will just be a
[L2273] [01:17:08.72] a bigger power tool. I mean,
[L2274] [01:17:10.84] everyone, we like using compilers,
[L2275] [01:17:12.48] right? We don't like machine code
[L2276] [01:17:13.48] anymore. Compilers make us more
[L2277] [01:17:14.96] productive. Maybe LLMs can make us more
[L2278] [01:17:17.24] productive. That's what I hope. I sort
[L2279] [01:17:19.36] of believe modulo dislocation effects.
[L2280] [01:17:22.52] Now,
[L2281] [01:17:24.36] um
[L2282] [01:17:25.84] should we
[L2283] [01:17:27.44] teach children or even undergraduates
[L2284] [01:17:29.76] how to program? So, I think still yes.
[L2285] [01:17:32.76] Um
[L2286] [01:17:33.48] um the reason is because
[L2287] [01:17:36.20] um
[L2288] [01:17:37.32] uh like one way to say it is co-pilots
[L2289] [01:17:40.04] need pilots.
[L2290] [01:17:42.40] Right? I think co-pilot is quite a good
[L2291] [01:17:43.84] title that Microsoft gave their tools,
[L2292] [01:17:46.24] right? Because it encourages you to
[L2293] [01:17:47.88] believe it's your partner, not your
[L2294] [01:17:49.20] boss.
[L2295] [01:17:50.36] Um
[L2296] [01:17:51.20] if LLMs spit out a pile of goop, and we
[L2297] [01:17:54.08] literally do not understand what it
[L2298] [01:17:55.52] does, we just try it and it kind of
[L2299] [01:17:56.72] works,
[L2300] [01:17:57.92] that might be okay if we're just
[L2301] [01:17:59.00] throwing up a quick visualization. It
[L2302] [01:18:00.92] might be less okay if the quick
[L2303] [01:18:02.40] visualization is going to drive our
[L2304] [01:18:03.80] policy um choices about as a nation
[L2305] [01:18:06.72] whether to go into lockdown because of
[L2306] [01:18:08.04] COVID, um or if this program is going to
[L2307] [01:18:11.56] run my airplane or train signaling
[L2308] [01:18:13.56] system.
[L2309] [01:18:15.32] So, now those are, you know, extreme
[L2310] [01:18:17.32] ends of the spectrum, you know, from
[L2311] [01:18:19.16] quick and dirty things it really doesn't
[L2312] [01:18:20.68] matter if it doesn't work, uh
[L2313] [01:18:22.84] but it kind of does a lot of the time,
[L2314] [01:18:24.56] absolutely fine, to
[L2315] [01:18:27.12] this is a 30-year code base, it's going
[L2316] [01:18:28.84] to last a long time. I really want to
[L2317] [01:18:30.56] make sure that it like putting new stuff
[L2318] [01:18:32.52] into GHC. If somebody sends me a pile of
[L2319] [01:18:34.72] AI-generated code to put into GHC, I'm
[L2320] [01:18:36.60] not going to put it in. Unless I've
[L2321] [01:18:38.24] reviewed it, or somebody's reviewed it,
[L2322] [01:18:40.00] because in 10 years time, I'm going to
[L2323] [01:18:42.24] want to change that code. How do I even
[L2324] [01:18:43.60] know what it does? If it's simply a
[L2325] [01:18:45.28] magic incantation that somebody's done
[L2326] [01:18:46.92] that kind of worked on the test they
[L2327] [01:18:48.52] did, but maybe won't work in deployment,
[L2328] [01:18:50.44] that's no good. So,
[L2329] [01:18:52.12] I really want
[L2330] [01:18:53.84] uh long-lived maintainable code to be
[L2331] [01:18:55.96] well reviewed. Sorry. Um so, and to do
[L2332] [01:18:58.52] that, I need reviewers who can write
[L2333] [01:19:00.08] code, who know
[L2334] [01:19:01.36] Um let me mention one other
[L2335] [01:19:03.84] perspective. Um
[L2336] [01:19:06.04] If you think about what every child
[L2337] [01:19:07.64] should know,
[L2338] [01:19:09.44] um
[L2339] [01:19:10.28] when I um
[L2340] [01:19:12.24] uh think about whatever a child should
[L2341] [01:19:14.00] know about computing, I would include
[L2342] [01:19:16.12] binary and bits.
[L2343] [01:19:19.08] Not Oh, just as for physics, I would
[L2344] [01:19:21.12] include atoms and molecules.
[L2345] [01:19:23.84] Now, it's not that in real life anybody
[L2346] [01:19:25.64] manipulates atoms or molecules, or takes
[L2347] [01:19:27.92] decisions which are based directly on
[L2348] [01:19:30.08] their knowledge of atom knowledge, but
[L2349] [01:19:31.64] somehow knowledge that all matter is
[L2350] [01:19:33.84] made up of atoms.
[L2351] [01:19:35.64] You know, constituted of a finite number
[L2352] [01:19:37.20] of elements that atoms could block
[L2353] [01:19:38.28] together with. That knowledge underpins
[L2354] [01:19:40.68] everything we understand about the
[L2355] [01:19:41.88] natural world. If you literally have
[L2356] [01:19:43.76] never been told that,
[L2357] [01:19:46.48] you are sort of emasculated
[L2358] [01:19:48.68] as a even as a citizen, let alone as a
[L2359] [01:19:50.88] scientist. So,
[L2360] [01:19:52.56] if you literally do not know that
[L2361] [01:19:54.32] everything is composed of bits, that
[L2362] [01:19:55.72] words and music and text and LLMs and
[L2363] [01:19:58.44] everything's all just bits,
[L2364] [01:20:00.32] I think you're crippled.
[L2365] [01:20:01.92] So, I want every child to learn uh you
[L2366] [01:20:04.48] know, it's like I want you to learn the
[L2367] [01:20:05.56] bottom that they It's It's all bits,
[L2368] [01:20:08.04] nothing else. It's all just bits.
[L2369] [01:20:11.40] I give a talk. The talk is called Bits
[L2370] [01:20:14.16] with Soul.
[L2371] [01:20:17.00] Um they're easy to grab for. It's a talk
[L2372] [01:20:19.36] I gave to an audience that was not
[L2373] [01:20:20.88] computer science audience at all. It was
[L2374] [01:20:22.48] a completely lay audience, ranging from
[L2375] [01:20:24.36] 14-year-olds to professors of quantum
[L2376] [01:20:26.04] mechanics. Pretty difficult audience to
[L2377] [01:20:28.76] address. Um and it was meant to be about
[L2378] [01:20:30.72] um
[L2379] [01:20:31.68] all about uh codes and coding and bits.
[L2380] [01:20:33.80] So, um,
[L2381] [01:20:35.12] and so it tries to get at the essence of
[L2382] [01:20:37.76] why why do I think it's important that
[L2383] [01:20:39.68] every every child, every person, every
[L2384] [01:20:41.84] human being should understand something
[L2385] [01:20:44.00] about the computational universe that
[L2386] [01:20:45.40] surrounds them. And that's founded in
[L2387] [01:20:46.60] bits. Now, just to to develop the
[L2388] [01:20:48.44] analogy a bit further, I would then say,
[L2389] [01:20:49.72] "And it also, I think I want them to
[L2390] [01:20:52.28] also know about programming programs. I
[L2391] [01:20:55.32] want them to know that computers
[L2392] [01:20:56.72] fundamentally execute by following
[L2393] [01:20:58.40] machine instructions blindly. Right?
[L2394] [01:21:00.68] There is not magic. It's not hocus
[L2395] [01:21:02.36] pocus. It's just remorseless and very
[L2396] [01:21:05.84] dumb.
[L2397] [01:21:07.04] Right? It's incredibly empowering then.
[L2398] [01:21:09.52] Um,
[L2399] [01:21:10.32] and also to learn the basics about how
[L2400] [01:21:12.04] neural networks work. In the same talk,
[L2401] [01:21:14.56] I explain how a a one neuron neural
[L2402] [01:21:17.20] network works.
[L2403] [01:21:18.60] Um,
[L2404] [01:21:19.56] and that's enough. Uh, then then it's
[L2405] [01:21:21.60] actually true to say, not distorting the
