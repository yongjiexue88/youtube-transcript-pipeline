Chunk 6; segments 2077–2278. Start may repeat the previous chunk for context.

# Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy

Source ID: source-fba2cff234dd0aeb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_OCaml_Functional_Programming,_Formal_Verification,_Programming_Languages_Xavier_Leroy_en.txt
Video: https://www.youtube.com/watch?v=9Cswiqrq6So

[L2086] [01:16:53.04] verifying simple neural networks like
[L2087] [01:16:56.16] those used for I don't know computer
[L2088] [01:16:58.48] vision
[L2089] [01:16:59.80] or self-driving cars or or or some
[L2090] [01:17:02.92] numerical computations like you know
[L2091] [01:17:05.08] weather prediction and so on. So so
[L2092] [01:17:07.24] specialized LLMs but you still want some
[L2093] [01:17:09.76] guarantees about
[L2094] [01:17:11.40] what they produce that they cannot
[L2095] [01:17:13.88] produce completely inconsistent outputs
[L2096] [01:17:15.72] for instance. There were some some
[L2097] [01:17:17.72] attempts in in in the last years at
[L2098] [01:17:20.80] using static analysis tools and
[L2099] [01:17:23.76] basically program verification tools
[L2100] [01:17:26.24] applied to LLMs
[L2101] [01:17:27.88] but well it it it doesn't scale.
[L2102] [01:17:32.48] LLMs are big.
[L2103] [01:17:34.40] Sorry.
[L2104] [01:17:35.80] Neural networks are big.
[L2105] [01:17:37.56] And for LLMs there's also
[L2106] [01:17:40.12] a distinct lack of specification. Okay.
[L2107] [01:17:44.12] You don't really know what's a good
[L2108] [01:17:46.68] answer from an LLM.
[L2109] [01:17:48.76] Well you know it when you see it but you
[L2110] [01:17:50.84] cannot write a mathematical
[L2111] [01:17:52.08] specification of it. So so that part is
[L2112] [01:17:54.64] probably over. What I would say are the
[L2113] [01:17:57.76] big problems for today yeah probably
[L2114] [01:18:00.40] maintaining software quality despite
[L2115] [01:18:02.96] AI's love despite a lot of pressure to
[L2116] [01:18:06.60] throw away traditional software
[L2117] [01:18:09.04] development techniques using
[L2118] [01:18:12.24] LLMs as an AI as much as we can to do
[L2119] [01:18:16.32] mechanized proofs so proofs that can be
[L2120] [01:18:18.52] checked by machines.
[L2121] [01:18:20.32] Maybe this will be the the decade of
[L2122] [01:18:22.68] formal verification of software. We've
[L2123] [01:18:24.72] been waiting for that for 50 years so
[L2124] [01:18:27.92] maybe it will it will finally take off.
[L2125] [01:18:31.00] >> What's your top book recommendation for
[L2126] [01:18:33.20] software engineers and why?
[L2127] [01:18:36.36] >> Well this this is an old one, the
[L2128] [01:18:38.24] Programming Pearls by Jon
[L2129] [01:18:40.36] I think I read it when I was a PhD
[L2130] [01:18:41.84] student, but I think it's it's nice as
[L2131] [01:18:45.36] showing how very talented programmers
[L2132] [01:18:48.80] work, [snorts] how they think about
[L2133] [01:18:51.12] their programs. So, it's it's it's it's
[L2134] [01:18:53.32] a combination of choosing the right
[L2135] [01:18:54.92] algorithms,
[L2136] [01:18:56.56] expressing them clearly,
[L2137] [01:18:59.00] uh knowing when to stop,
[L2138] [01:19:01.12] when when to use a simple algorithm,
[L2139] [01:19:04.04] where where
[L2140] [01:19:06.36] when a more complicated one is not
[L2141] [01:19:08.20] needed,
[L2142] [01:19:09.20] uh having a sense of elegance in in the
[L2143] [01:19:12.08] code you write, um
[L2144] [01:19:14.96] uh having a feeling for where the
[L2145] [01:19:16.96] problem is when when the the code
[L2146] [01:19:18.92] misbehave. So, all all that kind of
[L2147] [01:19:21.00] things that are hard to communicate, and
[L2148] [01:19:22.76] I think those those pearls
[L2149] [01:19:24.92] that are very easy to read, uh
[L2150] [01:19:27.48] and and and don't use any complicated
[L2151] [01:19:30.00] data structures, don't use any
[L2152] [01:19:31.36] complicated language. I mean, it it's
[L2153] [01:19:33.56] it's kind of timeless, you know.
[L2154] [01:19:35.56] Um
[L2155] [01:19:37.00] I think those pearls are are good
[L2156] [01:19:38.72] illustration of that.
[L2157] [01:19:41.16] Uh so, if you haven't read it, it's it's
[L2158] [01:19:43.00] a classic, but
[L2159] [01:19:45.04] I think it's a nice reading.
[L2160] [01:19:46.92] Nice read. Uh the second one is a little
[L2161] [01:19:49.44] more controversial, I guess.
[L2162] [01:19:51.52] So, in the How to Design Program, which
[L2163] [01:19:54.56] is a fairly ambitious title as well.
[L2164] [01:19:56.84] And this comes from the Scheme
[L2165] [01:19:58.08] community, okay, Abelson and Findler,
[L2166] [01:20:01.44] Flatt, and Krishnamurthi.
[L2167] [01:20:03.44] Um and and those people have developed
[L2168] [01:20:06.60] uh well, the Scheme community is famous
[L2169] [01:20:08.28] for having developed uh pedagogical
[L2170] [01:20:10.12] resources that are
[L2171] [01:20:11.72] I mean, ways to teach programming uh
[L2172] [01:20:16.08] that that go beyond teaching functional
[L2173] [01:20:18.04] programming, basically.
[L2174] [01:20:20.68] And so, so there was the
[L2175] [01:20:23.08] the MIT [clears throat]
[L2176] [01:20:24.00] Course Structure and Interpretation of
[L2177] [01:20:25.56] Computer Programs, which was quite
[L2178] [01:20:26.92] famous, and this is kind of a more
[L2179] [01:20:28.44] modern
[L2180] [01:20:30.60] twist on on on similar ideas.
[L2181] [01:20:33.64] And and and
[L2182] [01:20:35.76] I find this book interesting because
[L2183] [01:20:38.24] well, it it it really teaches you the
[L2184] [01:20:40.96] way of functional programming
[L2185] [01:20:43.52] a way to functional programming. It can
[L2186] [01:20:45.68] be very irritating sometimes, very
[L2187] [01:20:47.72] opinionated, very
[L2188] [01:20:49.76] um almost mystical sometimes, but
[L2189] [01:20:53.44] but it's also
[L2190] [01:20:55.36] another
[L2191] [01:20:56.56] great attempt at at trying to
[L2192] [01:20:58.32] communicate
[L2193] [01:21:00.24] how experienced programmers go about uh
[L2194] [01:21:03.64] designing a program
[L2195] [01:21:06.24] uh
[L2196] [01:21:07.24] even before writing the first line.
[L2197] [01:21:09.64] Okay. And and then how
[L2198] [01:21:11.76] given a language like Scheme, which is
[L2199] [01:21:13.64] pretty flexible, how the code kind of
[L2200] [01:21:16.48] follows uh naturally.
[L2201] [01:21:19.68] >> You know, knowing what you know now, if
[L2202] [01:21:21.12] you could go back to when you just
[L2203] [01:21:23.32] started your career and give yourself
[L2204] [01:21:25.12] some advice, what would you say?
[L2205] [01:21:27.48] >> Sometimes I got that uh maybe I
[L2206] [01:21:31.16] specialized a little too early in in in
[L2207] [01:21:34.36] um
[L2208] [01:21:35.44] in programming language research.
[L2209] [01:21:37.72] Uh maybe
[L2210] [01:21:39.12] well, there there are some topics that
[L2211] [01:21:40.72] are I didn't learn
[L2212] [01:21:44.00] because I didn't feel like it. And and
[L2213] [01:21:46.80] that I had to relearn later or I still
[L2214] [01:21:50.68] have to learn now that I'm almost 60 and
[L2215] [01:21:55.56] maybe not not as um
[L2216] [01:21:57.72] uh
[L2217] [01:21:59.56] not as quick uh
[L2218] [01:22:01.68] as I was back in the day. So, yeah,
[L2219] [01:22:03.28] maybe I I did specialize a little too
[L2220] [01:22:06.16] early. And so, I would encourage
[L2221] [01:22:07.96] everyone to get a everyone who's serious
[L2222] [01:22:10.76] about working in computing uh to get a
[L2223] [01:22:15.12] fairly diverse computer science
[L2224] [01:22:17.28] background. Even even for topics that
[L2225] [01:22:19.44] look super theoretical and are not very
[L2226] [01:22:22.56] uh relevant to
[L2227] [01:22:24.52] uh to everyday uh
[L2228] [01:22:27.36] jobs.
[L2229] [01:22:28.48] Uh well, we mentioned the
[L2230] [01:22:30.20] computability for instance things like
[L2231] [01:22:31.96] the halting problem and so on. You're
[L2232] [01:22:33.44] not going to run into that very often,
[L2233] [01:22:36.08] but it still
[L2234] [01:22:37.84] gives
[L2235] [01:22:38.96] interesting perspectives, I think.
[L2236] [01:22:42.80] And then it also helps understanding new
[L2237] [01:22:44.76] problems.
[L2238] [01:22:46.36] Like
[L2239] [01:22:48.12] with quantum computing.
[L2240] [01:22:50.40] What can you do with a quantum computer
[L2241] [01:22:52.12] that you cannot do with a normal
[L2242] [01:22:53.64] computer?
[L2243] [01:22:55.56] And and and it's it's time to to revisit
[L2244] [01:22:58.84] all of the classic complexity theory I
[L2245] [01:23:01.12] learned earlier and when when I was
[L2246] [01:23:04.80] young. And and so yeah, I think I think
[L2247] [01:23:07.92] it's good to have those this kind of
[L2248] [01:23:09.60] background even if
[L2249] [01:23:12.40] it's not obvious you will be using it
[L2250] [01:23:14.56] everyday.
[L2251] [01:23:15.80] And and sometimes I wish I had taken
[L2252] [01:23:18.24] time to accumulate a little more of this
[L2253] [01:23:20.80] background
[L2254] [01:23:22.00] before specializing in in programming
[L2255] [01:23:24.36] languages.
[L2256] [01:23:25.68] >> Awesome. Well, thank you so much for
[L2257] [01:23:26.96] your time Professor Liwei. I appreciate
[L2258] [01:23:28.68] it.
[L2259] [01:23:28.84] >> Thank you Aaron. That was nice.
[L2260] [01:23:31.40] >> Hey, thank you for watching this
[L2261] [01:23:32.36] podcast. If you liked it and you want to
[L2262] [01:23:34.04] see the show grow, please support with a
[L2263] [01:23:36.20] comment or a like.
[L2264] [01:23:38.24] Also, if you have any recommendations
[L2265] [01:23:40.04] for people you want me to bring on,
[L2266] [01:23:42.04] please drop a comment. Guests like
[L2267] [01:23:44.20] Barbara Liskov, Mike Stonebraker, Mark
[L2268] [01:23:46.92] Brooker, these were all people that I
[L2269] [01:23:48.96] brought on because someone left a
[L2270] [01:23:50.80] comment. On another note, aside from the
[L2271] [01:23:53.04] podcast, I'm working on building the
[L2272] [01:23:54.88] ergonomic keyboard that I wish existed.
[L2273] [01:23:57.36] Here's a glance at the prototype. It's a
[L2274] [01:23:59.24] split keyboard, so there's two sides.
[L2275] [01:24:02.12] Um this is in the case. But yeah, we
[L2276] [01:24:03.72] launched on Kickstarter and we hit our
[L2277] [01:24:05.52] goal within 8 hours of launching. I
[L2278] [01:24:07.60] really appreciate it if you were one of
[L2279] [01:24:09.00] the people who grabbed one of the early
[L2280] [01:24:10.72] units. Um we're now working on the long
[L2281] [01:24:13.08] journey of building the tooling now. And
[L2282] [01:24:15.20] so if you still want to pick one up,
[L2283] [01:24:16.88] I've left the late pledges open on
[L2284] [01:24:18.88] Kickstarter, so you can grab one there.
[L2285] [01:24:21.12] I'll put a link in the description.
[L2286] [01:24:23.08] Thank you again for watching the podcast
[L2287] [01:24:25.44] and I'll see you in the next episode.
