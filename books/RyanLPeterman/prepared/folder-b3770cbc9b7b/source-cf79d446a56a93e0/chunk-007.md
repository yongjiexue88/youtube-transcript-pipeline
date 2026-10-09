Chunk 7; segments 2078–2348. Start may repeat the previous chunk for context.

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L2087] [106:00.32] you build something for a million
[L2088] [106:02.32] people, you can do harm in the world.
[L2089] [106:05.60] And so that's what it's for. Um
[L2090] [106:10.96] I uh I mean Gildolf and Russen built um
[L2091] [106:15.36] built Python with the explicit aim of
[L2092] [106:18.64] allowing many people or even or
[L2093] [106:21.20] everybody to program and he succeeded.
[L2094] [106:25.76] I designed C++ to be a really good tool
[L2095] [106:29.92] for serious programmers, for engineers
[L2096] [106:32.72] and mathematicians and such and I
[L2097] [106:35.52] succeeded too.
[L2098] [106:37.76] Um, it's just not the same problem.
[L2099] [106:40.88] Remember where we started? I said the
[L2100] [106:43.28] problem look at the problem and then
[L2101] [106:45.20] learn from uh what worked and what
[L2102] [106:47.52] doesn't. Looking back on C++ and the
[L2103] [106:50.88] whole journey, is there any part where
[L2104] [106:53.76] you think oh that that was a mistake or
[L2105] [106:55.84] something that you learned from in the
[L2106] [106:57.76] design?
[L2107] [107:00.24] >> Many many uh times I learned something.
[L2108] [107:04.96] Um
[L2109] [107:08.32] I think most of the things never made it
[L2110] [107:12.00] into C++.
[L2111] [107:14.08] That is that's what you have experiments
[L2112] [107:16.72] for.
[L2113] [107:18.48] And that's what you have initial uses
[L2114] [107:21.92] for.
[L2115] [107:24.56] I think I got the major part of the
[L2116] [107:28.24] language right
[L2117] [107:30.80] and I think I could improve every single
[L2118] [107:34.32] detail.
[L2119] [107:36.56] But
[L2120] [107:38.16] stability, compatibility
[L2121] [107:41.04] is essential.
[L2122] [107:42.96] If you make an insignificant change, it
[L2123] [107:45.44] will annoy a few people and it wouldn't
[L2124] [107:47.28] matter. If you make a significant
[L2125] [107:50.08] change, you will annoy a lot of people
[L2126] [107:52.32] and it will not work because uh say a
[L2127] [107:56.08] million people will stick to the old
[L2128] [107:57.84] way.
[L2129] [108:00.16] So, um I I try to
[L2130] [108:04.64] grow the language without breaking it.
[L2131] [108:08.72] Um I have this thing that happens again
[L2132] [108:11.04] and again. and I explain it. People come
[L2133] [108:14.24] up and say to me C++ is too complicated.
[L2134] [108:18.96] Yeah. Um you you you must simplify it.
[L2135] [108:25.28] And I need these two features. I need
[L2136] [108:28.56] them yesterday. You must when you're
[L2137] [108:30.72] doing this. Give me these two features.
[L2138] [108:34.24] Yes.
[L2139] [108:36.16] And whatever you do, don't break my
[L2140] [108:38.08] code. I have a million lines of it.
[L2141] [108:42.16] That doesn't work. That's impossible.
[L2142] [108:45.68] And so that is why I'm working on coding
[L2143] [108:48.08] guidelines and on profiles which is
[L2144] [108:51.20] enforced guidelines. That way you can
[L2145] [108:54.48] design a profile that ensures that you
[L2146] [108:59.68] can use the libraries that you need and
[L2147] [109:02.96] ensure that you don't misuse the
[L2148] [109:05.28] features that are
[L2149] [109:08.32] unnecessary. and dangerous in your
[L2150] [109:11.44] field. for anyone who wants to um you
[L2151] [109:15.44] know learn C++ I think a common question
[L2152] [109:17.68] is like what is the you know top
[L2153] [109:20.48] technical book recommendation that you
[L2154] [109:22.40] would have
[L2155] [109:24.24] learn modern C++
[L2156] [109:26.72] there's a book I wrote when I was
[L2157] [109:29.12] teaching undergrads this this is
[L2158] [109:30.88] accidental I didn't mean it to be there
[L2159] [109:33.20] but anyway this is a second edition of
[L2160] [109:36.32] uh programming principles and practice
[L2161] [109:38.40] using C++ this is a big fat book um
[L2162] [109:42.64] written for undergrads. The third
[L2163] [109:45.44] edition is not as thick because the
[L2164] [109:48.72] language has improved and uh I can
[L2165] [109:51.36] actually um get the ideas across uh
[L2166] [109:55.28] better with less text. Um but use the
[L2167] [110:00.88] latest uh C++ learn the modern way
[L2168] [110:04.00] first. Don't start learning all the bad
[L2169] [110:07.28] ways of writing C as the starter. And a
[L2170] [110:10.88] lot of courses still says you learn C
[L2171] [110:14.08] first. So you learn some issues maloc
[L2172] [110:17.12] and uh pointers and uh then
[L2173] [110:21.76] later you can learn how to use a vector
[L2174] [110:23.92] on a string and not have the problems.
[L2175] [110:27.04] But
[L2176] [110:28.56] yeah, profiles are there
[L2177] [110:32.72] to be able to have compiler and static
[L2178] [110:36.08] analyzer support for that kind of
[L2179] [110:38.96] thinking.
[L2180] [110:40.40] And educators are asking for something
[L2181] [110:42.48] like that too. A lot of people think the
[L2182] [110:45.12] profile simply is to deal with memory
[L2183] [110:48.00] safety and performance. No, it it has to
[L2184] [110:52.08] give people a better tool uh both for
[L2185] [110:55.44] learning and for doing specific kinds of
[L2186] [110:58.08] work.
[L2187] [110:59.28] >> And then last question for you is if you
[L2188] [111:01.68] could go back to the beginning of your
[L2189] [111:03.60] career and give yourself some advice,
[L2190] [111:05.36] what would you say?
[L2191] [111:06.88] >> Oh dear. Yeah, that's a time machine
[L2192] [111:08.88] question. I I sometimes set that for uh
[L2193] [111:12.88] my students.
[L2194] [111:14.72] Uh you have a time machine. Go back and
[L2195] [111:17.36] uh give Dennis some advice and uh once
[L2196] [111:19.84] you've done that uh uh step 10 years uh
[L2197] [111:24.24] for forward and give me some advice.
[L2198] [111:27.44] It's a it's a good exercise. I usually I
[L2199] [111:30.24] usually get some really good stories out
[L2200] [111:32.32] of it, some suggestions.
[L2201] [111:35.04] Um,
[L2202] [111:39.68] I think
[L2203] [111:43.12] a lot of
[L2204] [111:47.60] I I I tried to avoid the two-way
[L2205] [111:52.16] conversions in of the built-in types and
[L2206] [111:55.28] C.
[L2207] [111:57.20] I should have fought harder for that. I
[L2208] [111:59.36] tried but uh was stopped by the people
[L2209] [112:02.80] in in in Bell Labs. Um and these were
[L2210] [112:07.76] more experienced people than me and
[L2211] [112:09.76] such. Now I I should have should have
[L2212] [112:12.72] gone further there. Furthermore, I
[L2213] [112:15.52] should have delayed the release of C++
[L2214] [112:20.08] till I could have something template
[L2215] [112:22.48] like so I could do a better uh standard
[L2216] [112:25.12] library.
[L2217] [112:27.44] um it wouldn't have been good enough,
[L2218] [112:30.08] but it would have gotten people into the
[L2219] [112:32.24] habit of of using a standard. Everybody
[L2220] [112:35.20] was building standard libraries and we
[L2221] [112:37.20] got saved by uh Alex Stefanov with the
[L2222] [112:40.48] STL. Uh but that was that was real luck
[L2223] [112:45.12] because I made a mistake in in not
[L2224] [112:48.56] delaying till I could have built a a a
[L2225] [112:52.00] good vector and uh class hierarchy. uh
[L2226] [112:56.80] stuff.
[L2227] [112:58.32] And then finally,
[L2228] [113:01.12] if I'd known what I know now about
[L2229] [113:04.40] standards committees and bloated
[L2230] [113:06.96] bureaucracies and we have more subgroups
[L2231] [113:10.56] now than we had members to start out
[L2232] [113:12.88] with, I would have tried very hard to
[L2233] [113:16.48] set up a
[L2234] [113:19.44] um some kind of
[L2235] [113:23.44] steering group so that people could make
[L2236] [113:27.04] suggestions. But
[L2237] [113:29.76] we wouldn't have a vote with say 500
[L2238] [113:33.76] people. We would have suggestions from a
[L2239] [113:36.56] community of 500 people and we would
[L2240] [113:39.28] have maybe a group of five or six people
[L2241] [113:44.40] uh with vast experience and cared for
[L2242] [113:47.20] the whole language who made the
[L2243] [113:49.76] decisions based on what was proposed.
[L2244] [113:52.80] Something like that. But I did not have
[L2245] [113:55.92] the experience or the knowledge to make
[L2246] [113:57.92] such a suggestion.
[L2247] [114:00.00] Uh notice that I did not mention tools.
[L2248] [114:03.68] C++ has a weakness in tools
[L2249] [114:07.20] and that was because it grew up early in
[L2250] [114:12.24] a time with limited tools, limited uh
[L2251] [114:19.92] compute power, limited memory. So I
[L2252] [114:22.96] couldn't have done it. One constraint on
[L2253] [114:25.84] the exercise I give to the uh students
[L2254] [114:28.80] for time machines is try and make sure
[L2255] [114:31.92] that it would be possible to follow your
[L2256] [114:33.92] advice.
[L2257] [114:35.92] And uh if I just said I want this then a
[L2258] [114:40.56] lot of the things couldn't be done till
[L2259] [114:44.72] uh 20 years later and therefore would
[L2260] [114:48.00] never have happened. There's a lot of
[L2261] [114:50.00] languages designed to be perfect
[L2262] [114:53.52] uh for the future uh computers and the
[L2263] [114:56.64] future programmers. Most of them die
[L2264] [115:00.40] because by the time 10 years later they
[L2265] [115:03.28] get the language, the world has changed
[L2266] [115:07.20] >> on that first one. I imagine that would
[L2267] [115:09.76] have been really tough to do because the
[L2268] [115:12.40] the Bell Labs people were so senior.
[L2269] [115:15.36] >> I I failed. I tried. Um, but it's it's
[L2270] [115:19.12] obvious that you don't want narrowing
[L2271] [115:21.60] conversions. I even wrote a paper about
[L2272] [115:24.40] how to get rid of them uh today in a
[L2273] [115:26.96] library
[L2274] [115:28.48] uh last year. But it is a fundamental
[L2275] [115:34.80] flaw in the type system of C and C++.
[L2276] [115:38.48] And it came because they needed they
[L2277] [115:42.56] being people like Dennis Richie and the
[L2278] [115:45.12] Unix team and so they needed to be able
[L2279] [115:47.76] to handle both integers and floating
[L2280] [115:49.76] point and they didn't think of explicit
[L2281] [115:54.48] type conversion and they thought
[L2282] [115:56.56] explicit type conversion was too clunky.
[L2283] [115:59.84] They didn't actually get casts till
[L2284] [116:02.24] about 5 years after they got floating
[L2285] [116:05.44] point integers. And of course you have
[L2286] [116:08.72] to be able to turn a floating point into
[L2287] [116:10.64] an integer, right? And so that you get
[L2288] [116:14.72] implicit conversions whenever you can.
[L2289] [116:18.24] Also things like integers into
[L2290] [116:20.24] characters
[L2291] [116:22.56] uh problematic. But since you are
[L2292] [116:24.80] writing fundamental software, you didn't
[L2293] [116:27.20] want to write something
[L2294] [116:29.60] complicated and you didn't want to have
[L2295] [116:32.48] runtime checking. You couldn't afford
[L2296] [116:34.48] that.
[L2297] [116:36.24] And uh well so it was established uh
[L2298] [116:40.80] long before I came and my my attempts to
[L2299] [116:45.12] to deal with that failed.
[L2300] [116:47.28] >> It sounds like it wasn't for no reason.
[L2301] [116:49.76] It um you know saves resources maybe are
[L2302] [116:53.20] very limited.
[L2303] [116:54.00] >> They didn't have the resources to to
[L2304] [116:56.08] deal with it. They built lint the static
[L2305] [117:00.08] cheer to deal with some of it and uh
[L2306] [117:04.40] small machines. Another thing was that
[L2307] [117:07.68] that group of programmers was
[L2308] [117:09.76] significantly smarter and significantly
[L2309] [117:12.00] more experienced than the average
[L2310] [117:13.76] developer today. We have the law of
[L2311] [117:17.76] large numbers.
[L2312] [117:19.68] uh I think the last num the latest
[L2313] [117:22.24] estimate I've seen on the number of
[L2314] [117:24.08] software developers in the world is 47
[L2315] [117:26.96] million
[L2316] [117:28.64] and at that time with Unix the number of
[L2317] [117:34.24] uh programmers
[L2318] [117:36.72] probably was a few dozen and the ones
[L2319] [117:41.36] that didn't have a PhD in uh from a good
[L2320] [117:45.52] university were geniuses.
[L2321] [117:47.92] it's easier to get a PhD and being a
[L2322] [117:50.08] genius. And so they were for a different
[L2323] [117:54.32] set of problems with a different set of
[L2324] [117:56.48] machines and a different set of people.
[L2325] [117:59.04] Boy, it was a pain and still is.
[L2326] [118:02.32] >> Awesome. Well, thank you so much for
[L2327] [118:03.60] your time, professor. I really
[L2328] [118:05.04] appreciate it.
[L2329] [118:05.84] >> Okay. Thank you.
[L2330] [118:07.04] >> Hey, thank you for watching this
[L2331] [118:08.16] podcast. If you liked it and you want to
[L2332] [118:09.84] see the show grow, please support with a
[L2333] [118:12.16] comment or a like. Also, if you have any
[L2334] [118:15.04] recommendations for people you want me
[L2335] [118:16.72] to bring on, please drop a comment.
[L2336] [118:19.36] Guests like Barbara Liskoff, Mike
[L2337] [118:21.52] Stonereaker, Mark Brooker, these were
[L2338] [118:24.00] all people that I brought on because
[L2339] [118:25.92] someone left a comment. On another note,
[L2340] [118:28.24] aside from the podcast, I'm working on
[L2341] [118:30.08] building the ergonomic keyboard that I
[L2342] [118:32.00] wish existed. Here's a glance at the
[L2343] [118:34.16] prototype. It's a split keyboard, so
[L2344] [118:36.40] there's two sides. Um, this is in the
[L2345] [118:38.56] case, but yeah, we launched on
[L2346] [118:40.08] Kickstarter and we hit our goal within 8
[L2347] [118:42.32] hours of launching. I really appreciate
[L2348] [118:44.00] it if you were one of the people who
[L2349] [118:45.44] grabbed one of the early units. Um,
[L2350] [118:47.68] we're now working on the long journey of
[L2351] [118:49.60] building the tooling now and so if you
[L2352] [118:51.36] still want to pick one up, I've left the
[L2353] [118:53.44] late pledges open on Kickstarter, so you
[L2354] [118:56.08] can grab one there. I'll put a link in
[L2355] [118:57.68] the description. Thank you again for
[L2356] [119:00.00] watching the podcast and I'll see you in
[L2357] [119:02.24] the next
