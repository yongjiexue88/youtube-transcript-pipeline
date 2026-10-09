Chunk 7; segments 2104–2348. Start may repeat the previous chunk for context.

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L2113] [01:47:18.48] And that's what you have initial uses
[L2114] [01:47:21.92] for.
[L2115] [01:47:24.56] I think I got the major part of the
[L2116] [01:47:28.24] language right
[L2117] [01:47:30.80] and I think I could improve every single
[L2118] [01:47:34.32] detail.
[L2119] [01:47:36.56] But
[L2120] [01:47:38.16] stability, compatibility
[L2121] [01:47:41.04] is essential.
[L2122] [01:47:42.96] If you make an insignificant change, it
[L2123] [01:47:45.44] will annoy a few people and it wouldn't
[L2124] [01:47:47.28] matter. If you make a significant
[L2125] [01:47:50.08] change, you will annoy a lot of people
[L2126] [01:47:52.32] and it will not work because uh say a
[L2127] [01:47:56.08] million people will stick to the old
[L2128] [01:47:57.84] way.
[L2129] [01:48:00.16] So, um I I try to
[L2130] [01:48:04.64] grow the language without breaking it.
[L2131] [01:48:08.72] Um I have this thing that happens again
[L2132] [01:48:11.04] and again. and I explain it. People come
[L2133] [01:48:14.24] up and say to me C++ is too complicated.
[L2134] [01:48:18.96] Yeah. Um you you you must simplify it.
[L2135] [01:48:25.28] And I need these two features. I need
[L2136] [01:48:28.56] them yesterday. You must when you're
[L2137] [01:48:30.72] doing this. Give me these two features.
[L2138] [01:48:34.24] Yes.
[L2139] [01:48:36.16] And whatever you do, don't break my
[L2140] [01:48:38.08] code. I have a million lines of it.
[L2141] [01:48:42.16] That doesn't work. That's impossible.
[L2142] [01:48:45.68] And so that is why I'm working on coding
[L2143] [01:48:48.08] guidelines and on profiles which is
[L2144] [01:48:51.20] enforced guidelines. That way you can
[L2145] [01:48:54.48] design a profile that ensures that you
[L2146] [01:48:59.68] can use the libraries that you need and
[L2147] [01:49:02.96] ensure that you don't misuse the
[L2148] [01:49:05.28] features that are
[L2149] [01:49:08.32] unnecessary. and dangerous in your
[L2150] [01:49:11.44] field. for anyone who wants to um you
[L2151] [01:49:15.44] know learn C++ I think a common question
[L2152] [01:49:17.68] is like what is the you know top
[L2153] [01:49:20.48] technical book recommendation that you
[L2154] [01:49:22.40] would have
[L2155] [01:49:24.24] learn modern C++
[L2156] [01:49:26.72] there's a book I wrote when I was
[L2157] [01:49:29.12] teaching undergrads this this is
[L2158] [01:49:30.88] accidental I didn't mean it to be there
[L2159] [01:49:33.20] but anyway this is a second edition of
[L2160] [01:49:36.32] uh programming principles and practice
[L2161] [01:49:38.40] using C++ this is a big fat book um
[L2162] [01:49:42.64] written for undergrads. The third
[L2163] [01:49:45.44] edition is not as thick because the
[L2164] [01:49:48.72] language has improved and uh I can
[L2165] [01:49:51.36] actually um get the ideas across uh
[L2166] [01:49:55.28] better with less text. Um but use the
[L2167] [01:50:00.88] latest uh C++ learn the modern way
[L2168] [01:50:04.00] first. Don't start learning all the bad
[L2169] [01:50:07.28] ways of writing C as the starter. And a
[L2170] [01:50:10.88] lot of courses still says you learn C
[L2171] [01:50:14.08] first. So you learn some issues maloc
[L2172] [01:50:17.12] and uh pointers and uh then
[L2173] [01:50:21.76] later you can learn how to use a vector
[L2174] [01:50:23.92] on a string and not have the problems.
[L2175] [01:50:27.04] But
[L2176] [01:50:28.56] yeah, profiles are there
[L2177] [01:50:32.72] to be able to have compiler and static
[L2178] [01:50:36.08] analyzer support for that kind of
[L2179] [01:50:38.96] thinking.
[L2180] [01:50:40.40] And educators are asking for something
[L2181] [01:50:42.48] like that too. A lot of people think the
[L2182] [01:50:45.12] profile simply is to deal with memory
[L2183] [01:50:48.00] safety and performance. No, it it has to
[L2184] [01:50:52.08] give people a better tool uh both for
[L2185] [01:50:55.44] learning and for doing specific kinds of
[L2186] [01:50:58.08] work.
[L2187] [01:50:59.28] >> And then last question for you is if you
[L2188] [01:51:01.68] could go back to the beginning of your
[L2189] [01:51:03.60] career and give yourself some advice,
[L2190] [01:51:05.36] what would you say?
[L2191] [01:51:06.88] >> Oh dear. Yeah, that's a time machine
[L2192] [01:51:08.88] question. I I sometimes set that for uh
[L2193] [01:51:12.88] my students.
[L2194] [01:51:14.72] Uh you have a time machine. Go back and
[L2195] [01:51:17.36] uh give Dennis some advice and uh once
[L2196] [01:51:19.84] you've done that uh uh step 10 years uh
[L2197] [01:51:24.24] for forward and give me some advice.
[L2198] [01:51:27.44] It's a it's a good exercise. I usually I
[L2199] [01:51:30.24] usually get some really good stories out
[L2200] [01:51:32.32] of it, some suggestions.
[L2201] [01:51:35.04] Um,
[L2202] [01:51:39.68] I think
[L2203] [01:51:43.12] a lot of
[L2204] [01:51:47.60] I I I tried to avoid the two-way
[L2205] [01:51:52.16] conversions in of the built-in types and
[L2206] [01:51:55.28] C.
[L2207] [01:51:57.20] I should have fought harder for that. I
[L2208] [01:51:59.36] tried but uh was stopped by the people
[L2209] [01:52:02.80] in in in Bell Labs. Um and these were
[L2210] [01:52:07.76] more experienced people than me and
[L2211] [01:52:09.76] such. Now I I should have should have
[L2212] [01:52:12.72] gone further there. Furthermore, I
[L2213] [01:52:15.52] should have delayed the release of C++
[L2214] [01:52:20.08] till I could have something template
[L2215] [01:52:22.48] like so I could do a better uh standard
[L2216] [01:52:25.12] library.
[L2217] [01:52:27.44] um it wouldn't have been good enough,
[L2218] [01:52:30.08] but it would have gotten people into the
[L2219] [01:52:32.24] habit of of using a standard. Everybody
[L2220] [01:52:35.20] was building standard libraries and we
[L2221] [01:52:37.20] got saved by uh Alex Stefanov with the
[L2222] [01:52:40.48] STL. Uh but that was that was real luck
[L2223] [01:52:45.12] because I made a mistake in in not
[L2224] [01:52:48.56] delaying till I could have built a a a
[L2225] [01:52:52.00] good vector and uh class hierarchy. uh
[L2226] [01:52:56.80] stuff.
[L2227] [01:52:58.32] And then finally,
[L2228] [01:53:01.12] if I'd known what I know now about
[L2229] [01:53:04.40] standards committees and bloated
[L2230] [01:53:06.96] bureaucracies and we have more subgroups
[L2231] [01:53:10.56] now than we had members to start out
[L2232] [01:53:12.88] with, I would have tried very hard to
[L2233] [01:53:16.48] set up a
[L2234] [01:53:19.44] um some kind of
[L2235] [01:53:23.44] steering group so that people could make
[L2236] [01:53:27.04] suggestions. But
[L2237] [01:53:29.76] we wouldn't have a vote with say 500
[L2238] [01:53:33.76] people. We would have suggestions from a
[L2239] [01:53:36.56] community of 500 people and we would
[L2240] [01:53:39.28] have maybe a group of five or six people
[L2241] [01:53:44.40] uh with vast experience and cared for
[L2242] [01:53:47.20] the whole language who made the
[L2243] [01:53:49.76] decisions based on what was proposed.
[L2244] [01:53:52.80] Something like that. But I did not have
[L2245] [01:53:55.92] the experience or the knowledge to make
[L2246] [01:53:57.92] such a suggestion.
[L2247] [01:54:00.00] Uh notice that I did not mention tools.
[L2248] [01:54:03.68] C++ has a weakness in tools
[L2249] [01:54:07.20] and that was because it grew up early in
[L2250] [01:54:12.24] a time with limited tools, limited uh
[L2251] [01:54:19.92] compute power, limited memory. So I
[L2252] [01:54:22.96] couldn't have done it. One constraint on
[L2253] [01:54:25.84] the exercise I give to the uh students
[L2254] [01:54:28.80] for time machines is try and make sure
[L2255] [01:54:31.92] that it would be possible to follow your
[L2256] [01:54:33.92] advice.
[L2257] [01:54:35.92] And uh if I just said I want this then a
[L2258] [01:54:40.56] lot of the things couldn't be done till
[L2259] [01:54:44.72] uh 20 years later and therefore would
[L2260] [01:54:48.00] never have happened. There's a lot of
[L2261] [01:54:50.00] languages designed to be perfect
[L2262] [01:54:53.52] uh for the future uh computers and the
[L2263] [01:54:56.64] future programmers. Most of them die
[L2264] [01:55:00.40] because by the time 10 years later they
[L2265] [01:55:03.28] get the language, the world has changed
[L2266] [01:55:07.20] >> on that first one. I imagine that would
[L2267] [01:55:09.76] have been really tough to do because the
[L2268] [01:55:12.40] the Bell Labs people were so senior.
[L2269] [01:55:15.36] >> I I failed. I tried. Um, but it's it's
[L2270] [01:55:19.12] obvious that you don't want narrowing
[L2271] [01:55:21.60] conversions. I even wrote a paper about
[L2272] [01:55:24.40] how to get rid of them uh today in a
[L2273] [01:55:26.96] library
[L2274] [01:55:28.48] uh last year. But it is a fundamental
[L2275] [01:55:34.80] flaw in the type system of C and C++.
[L2276] [01:55:38.48] And it came because they needed they
[L2277] [01:55:42.56] being people like Dennis Richie and the
[L2278] [01:55:45.12] Unix team and so they needed to be able
[L2279] [01:55:47.76] to handle both integers and floating
[L2280] [01:55:49.76] point and they didn't think of explicit
[L2281] [01:55:54.48] type conversion and they thought
[L2282] [01:55:56.56] explicit type conversion was too clunky.
[L2283] [01:55:59.84] They didn't actually get casts till
[L2284] [01:56:02.24] about 5 years after they got floating
[L2285] [01:56:05.44] point integers. And of course you have
[L2286] [01:56:08.72] to be able to turn a floating point into
[L2287] [01:56:10.64] an integer, right? And so that you get
[L2288] [01:56:14.72] implicit conversions whenever you can.
[L2289] [01:56:18.24] Also things like integers into
[L2290] [01:56:20.24] characters
[L2291] [01:56:22.56] uh problematic. But since you are
[L2292] [01:56:24.80] writing fundamental software, you didn't
[L2293] [01:56:27.20] want to write something
[L2294] [01:56:29.60] complicated and you didn't want to have
[L2295] [01:56:32.48] runtime checking. You couldn't afford
[L2296] [01:56:34.48] that.
[L2297] [01:56:36.24] And uh well so it was established uh
[L2298] [01:56:40.80] long before I came and my my attempts to
[L2299] [01:56:45.12] to deal with that failed.
[L2300] [01:56:47.28] >> It sounds like it wasn't for no reason.
[L2301] [01:56:49.76] It um you know saves resources maybe are
[L2302] [01:56:53.20] very limited.
[L2303] [01:56:54.00] >> They didn't have the resources to to
[L2304] [01:56:56.08] deal with it. They built lint the static
[L2305] [01:57:00.08] cheer to deal with some of it and uh
[L2306] [01:57:04.40] small machines. Another thing was that
[L2307] [01:57:07.68] that group of programmers was
[L2308] [01:57:09.76] significantly smarter and significantly
[L2309] [01:57:12.00] more experienced than the average
[L2310] [01:57:13.76] developer today. We have the law of
[L2311] [01:57:17.76] large numbers.
[L2312] [01:57:19.68] uh I think the last num the latest
[L2313] [01:57:22.24] estimate I've seen on the number of
[L2314] [01:57:24.08] software developers in the world is 47
[L2315] [01:57:26.96] million
[L2316] [01:57:28.64] and at that time with Unix the number of
[L2317] [01:57:34.24] uh programmers
[L2318] [01:57:36.72] probably was a few dozen and the ones
[L2319] [01:57:41.36] that didn't have a PhD in uh from a good
[L2320] [01:57:45.52] university were geniuses.
[L2321] [01:57:47.92] it's easier to get a PhD and being a
[L2322] [01:57:50.08] genius. And so they were for a different
[L2323] [01:57:54.32] set of problems with a different set of
[L2324] [01:57:56.48] machines and a different set of people.
[L2325] [01:57:59.04] Boy, it was a pain and still is.
[L2326] [01:58:02.32] >> Awesome. Well, thank you so much for
[L2327] [01:58:03.60] your time, professor. I really
[L2328] [01:58:05.04] appreciate it.
[L2329] [01:58:05.84] >> Okay. Thank you.
[L2330] [01:58:07.04] >> Hey, thank you for watching this
[L2331] [01:58:08.16] podcast. If you liked it and you want to
[L2332] [01:58:09.84] see the show grow, please support with a
[L2333] [01:58:12.16] comment or a like. Also, if you have any
[L2334] [01:58:15.04] recommendations for people you want me
[L2335] [01:58:16.72] to bring on, please drop a comment.
[L2336] [01:58:19.36] Guests like Barbara Liskoff, Mike
[L2337] [01:58:21.52] Stonereaker, Mark Brooker, these were
[L2338] [01:58:24.00] all people that I brought on because
[L2339] [01:58:25.92] someone left a comment. On another note,
[L2340] [01:58:28.24] aside from the podcast, I'm working on
[L2341] [01:58:30.08] building the ergonomic keyboard that I
[L2342] [01:58:32.00] wish existed. Here's a glance at the
[L2343] [01:58:34.16] prototype. It's a split keyboard, so
[L2344] [01:58:36.40] there's two sides. Um, this is in the
[L2345] [01:58:38.56] case, but yeah, we launched on
[L2346] [01:58:40.08] Kickstarter and we hit our goal within 8
[L2347] [01:58:42.32] hours of launching. I really appreciate
[L2348] [01:58:44.00] it if you were one of the people who
[L2349] [01:58:45.44] grabbed one of the early units. Um,
[L2350] [01:58:47.68] we're now working on the long journey of
[L2351] [01:58:49.60] building the tooling now and so if you
[L2352] [01:58:51.36] still want to pick one up, I've left the
[L2353] [01:58:53.44] late pledges open on Kickstarter, so you
[L2354] [01:58:56.08] can grab one there. I'll put a link in
[L2355] [01:58:57.68] the description. Thank you again for
[L2356] [01:59:00.00] watching the podcast and I'll see you in
[L2357] [01:59:02.24] the next
