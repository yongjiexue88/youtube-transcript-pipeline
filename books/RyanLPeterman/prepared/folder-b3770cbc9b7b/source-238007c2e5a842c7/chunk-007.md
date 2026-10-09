Chunk 7; segments 2083–2417. Start may repeat the previous chunk for context.

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

Source ID: source-238007c2e5a842c7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_P_vs_NP,_Zero-Knowledge_Proofs,_Quantum_Computation_Avi_Wigderson_en.txt
Video: https://www.youtube.com/watch?v=5GUcvSAJcJw

[L2092] [01:36:44.16] np completeness. This is an NP complete
[L2093] [01:36:46.80] problem. Anything can be that can be
[L2094] [01:36:49.68] proved is really something in NP. Right?
[L2095] [01:36:52.64] This is the definition. So you reduce it
[L2096] [01:36:55.68] to three color. You prove it in zero
[L2097] [01:36:57.52] knowledge. And and the main point about
[L2098] [01:37:00.80] reductions in NP is that they don't only
[L2099] [01:37:05.04] uh convert the you know the yes no
[L2100] [01:37:07.20] answer in a consistent way that if this
[L2101] [01:37:10.08] sort of this sable but actually if you
[L2102] [01:37:12.56] have a a witness if you have a proof for
[L2103] [01:37:15.84] I don't know whatever it will become a a
[L2104] [01:37:20.48] a legal three coloring of the graph you
[L2105] [01:37:22.80] generate. So if you have a proof you can
[L2106] [01:37:24.88] also have the three coloring. is very
[L2107] [01:37:26.80] important that the reduction
[L2108] [01:37:30.40] also provides a translation not just
[L2109] [01:37:33.04] between the instances but also between
[L2110] [01:37:35.36] the proofs. So NP completeness theory
[L2111] [01:37:38.48] gives you for free that if you solve the
[L2112] [01:37:40.56] problem for graph coloring instances you
[L2113] [01:37:43.92] solve it for any you can prove anything
[L2114] [01:37:46.24] in zero knowledge.
[L2115] [01:37:47.44] >> So um with the zero knowledge proofs you
[L2116] [01:37:50.80] can never be 100% sure. No
[L2117] [01:37:53.60] >> okay but practically I mean
[L2118] [01:37:56.32] exponentially approaching
[L2119] [01:37:57.84] >> you can make you can make the
[L2120] [01:37:59.68] completeness
[L2121] [01:38:01.60] uh 100% namely if I do have a proof you
[L2122] [01:38:05.04] will be yeah there will be no error in
[L2123] [01:38:07.20] your but there is a slight possibility
[L2124] [01:38:09.92] that the graph is not three coloring not
[L2125] [01:38:12.40] three colorable and you will not catch
[L2126] [01:38:14.08] me you can make this exponentially small
[L2127] [01:38:16.72] you cannot make it zero
[L2128] [01:38:18.40] >> when I think of cryptography oneway
[L2129] [01:38:20.56] functions there's this idea of you
[L2130] [01:38:22.96] quantum computation that's kind of
[L2131] [01:38:25.28] changed uh complexity theory a bit and
[L2132] [01:38:28.64] >> big time. Yeah.
[L2133] [01:38:30.24] >> Yeah. And I wanted to ask your thoughts
[L2134] [01:38:32.16] on you know how quantum computation or
[L2135] [01:38:35.36] that model of uh computation is changing
[L2136] [01:38:39.76] uh complexity theory like what are the
[L2137] [01:38:41.60] big takeaways?
[L2138] [01:38:43.12] >> Okay, let me say what it is first of
[L2139] [01:38:44.96] all. I mean uh yeah uh quantum mechanics
[L2140] [01:38:48.16] is a theory of nature that you know
[L2141] [01:38:50.80] seems to be everybody believes and
[L2142] [01:38:53.52] accepts. So uh like with randomness we
[L2143] [01:38:57.44] can ask why not enhance computers with
[L2144] [01:39:00.80] you know this physical knowledge. We
[L2145] [01:39:02.72] allow uh our computers to operate in the
[L2146] [01:39:06.56] you know ways that quantum mechanics
[L2147] [01:39:09.52] dictates namely manipulate
[L2148] [01:39:12.24] bits in superposition using unitary
[L2149] [01:39:14.80] operations whatever this means but you
[L2150] [01:39:17.84] know according to the rules of uh
[L2151] [01:39:20.32] quantum mechanics and uh really strange
[L2152] [01:39:24.32] things happen in quantum mechanics I'm
[L2153] [01:39:26.24] sure many many people know because you
[L2154] [01:39:28.96] know you can there are all these
[L2155] [01:39:30.96] interference pattern turns you. Yeah, it
[L2156] [01:39:34.16] seems that uh you know you can uh u
[L2157] [01:39:38.56] basically you are working with
[L2158] [01:39:39.84] probability theory with negative
[L2159] [01:39:41.60] numbers. Events cannot uh you know
[L2160] [01:39:44.88] aggregate only they can cancel each
[L2161] [01:39:47.04] other and uh okay so it's a model of
[L2162] [01:39:51.28] computation. It's a generalization of uh
[L2163] [01:39:54.56] touring machines. In fact it's
[L2164] [01:39:55.92] generalization of randomized touring
[L2165] [01:39:58.08] machine. It's very easy to see that uh a
[L2166] [100:02.40] quantum computer is at least as strong
[L2167] [100:04.40] as a proistic computer. How do you see
[L2168] [100:06.96] it? You just measure the quantum bits
[L2169] [100:09.20] before you start. You measure them. This
[L2170] [100:12.08] what I mentioned about the photons in
[L2171] [100:14.00] the beginning. If you you have a some
[L2172] [100:16.72] basic superposition on I mean quantum
[L2173] [100:19.68] quantum bit if you measure it you get a
[L2174] [100:22.16] random bit. So because of that quantum
[L2175] [100:25.12] computers are at least as strong as
[L2176] [100:27.52] proistic computers. uh okay so it's a
[L2177] [100:31.44] model of computation and uh it was
[L2178] [100:34.56] suggested in the 80s fineman
[L2179] [100:38.96] uh and man and others
[L2180] [100:41.84] uh suggested you know letting algorithms
[L2181] [100:46.64] use these quantum mechanical operations
[L2182] [100:50.08] mainly in originally for just simulating
[L2183] [100:52.88] quantum systems rather than building
[L2184] [100:55.68] bigger apparatus to yeah like we
[L2185] [100:58.40] simulate other things turbulence I don't
[L2186] [101:00.48] know what's the power of quantum
[L2187] [101:02.64] algorithms again let's say running in
[L2188] [101:05.52] polinomial time or efficient quantum
[L2189] [101:07.36] algorithm can they do more than
[L2190] [101:09.92] efficient classical ones deterministic
[L2191] [101:12.64] or probabilistic and it wasn't clear for
[L2192] [101:15.68] a while and there were
[L2193] [101:18.08] a few examples that were very stylized
[L2194] [101:20.40] but were not for concrete natural
[L2195] [101:22.88] problems we care about and then in 94
[L2196] [101:26.00] Peter saw sort of Yeah, created an
[L2197] [101:30.56] earthquake or an avalanche. Uh he uh
[L2198] [101:35.44] found quantum algorithms that are
[L2199] [101:37.44] efficient, the factual integers and also
[L2200] [101:41.44] complete discrete logarithms. The two
[L2201] [101:43.44] most basic uh underpinnings of all
[L2202] [101:46.56] security systems that exist and this set
[L2203] [101:49.60] the world on fire, right? So uh lots of
[L2204] [101:53.28] people try to do a lot of things. uh of
[L2205] [101:56.40] course you know people want to you have
[L2206] [101:59.92] them these algorithms they implement
[L2207] [102:02.08] maybe they want to break or other people
[L2208] [102:04.96] skip the system. So as you know since
[L2209] [102:07.52] then billions were invested by companies
[L2210] [102:10.64] by governments by uh lots of people
[L2211] [102:14.80] trying to to build the technological
[L2212] [102:17.92] infrastructure and this is extremely
[L2213] [102:20.40] complicated. holding beats in superp
[L2214] [102:23.12] position is extremely complicated.
[L2215] [102:25.92] There's things that are called the
[L2216] [102:28.24] there's the noise. I mean when people
[L2217] [102:31.28] build classical computers like for noman
[L2218] [102:33.76] here in the
[L2219] [102:35.68] uh building next door u u you know noise
[L2220] [102:40.88] was one of the serious problems because
[L2221] [102:42.64] the bits were really in vacuum tubes and
[L2222] [102:45.76] uh they had to contend and in fact he
[L2223] [102:48.56] built a nice theory of uh classical
[L2224] [102:51.84] computers that have errors noise they
[L2225] [102:54.48] have to cope with errors some of their
[L2226] [102:56.16] components can be faulty but this today
[L2227] [102:59.84] is hardware you know has no errors to
[L2228] [103:02.56] speak of. We don't I mean there are
[L2229] [103:04.40] error correcting mechanisms but uh we
[L2230] [103:07.44] don't need them for classical computing.
[L2231] [103:10.24] Intel chips don't have you know I think
[L2232] [103:12.88] error correction in them. Hardware is
[L2233] [103:15.12] very reliable. When you move to quantum
[L2234] [103:18.32] there is this the coherence noise
[L2235] [103:21.76] in quantum mechanics everything depends
[L2236] [103:23.92] on everything. the world can influence
[L2237] [103:27.12] uh the computation in your laptop and uh
[L2238] [103:31.68] and protecting from this is very hard.
[L2239] [103:34.00] There are quantum correcting codes and
[L2240] [103:36.08] that's part of the solutions. That's
[L2241] [103:38.40] only one of the problems. Just holding
[L2242] [103:40.32] bits in superp position is hard and
[L2243] [103:42.72] there are many hard technological issues
[L2244] [103:45.44] and there's progress on that. So this is
[L2245] [103:47.68] one line of huge investment.
[L2246] [103:50.88] Uh the other line comes from
[L2247] [103:52.40] cryptography because of course everybody
[L2248] [103:55.04] should be worried right. I mean you know
[L2249] [103:57.76] forget quantum computers if tomorrow uh
[L2250] [104:00.96] I mean really tomorrow uh somebody finds
[L2251] [104:04.48] even a classical factory algorithms in
[L2252] [104:07.36] algorithm in polinomial time I think
[L2253] [104:09.20] there'll be chaos in the world because
[L2254] [104:11.76] nobody nobody can do any transactions
[L2255] [104:14.80] because most security systems still rely
[L2256] [104:17.04] on
[L2257] [104:19.52] um
[L2258] [104:21.04] and so of course uh we want to change
[L2259] [104:25.12] these
[L2260] [104:26.08] We want to change the underlying
[L2261] [104:27.76] assumptions of security. We want to rely
[L2262] [104:31.68] the whole revolution in cryptography was
[L2263] [104:33.84] that we rest cryptography on
[L2264] [104:35.84] computationally hard assumptions and
[L2265] [104:38.56] with this we build all the wonderful
[L2266] [104:40.48] public key systems and you know all the
[L2267] [104:45.04] magical things you can do with
[L2268] [104:48.00] under uh by assuming that players are
[L2269] [104:52.24] computationally limited.
[L2270] [104:54.56] uh but now if they are the the
[L2271] [104:57.04] adversaries are quantum computers
[L2272] [104:59.44] certainly they can break this assumption
[L2273] [105:02.00] you want to find other mathematical
[L2274] [105:04.24] problems computational problems
[L2275] [105:07.84] uh which are somehow hard even to
[L2276] [105:11.68] quantum computers.
[L2277] [105:13.84] So that's a the whole field this change
[L2278] [105:16.48] complexity theory and cryptography there
[L2279] [105:19.52] is an army of people who are just uh
[L2280] [105:23.12] trying to invent problems. I maybe
[L2281] [105:26.08] should stress one way functions are easy
[L2282] [105:28.08] to find. I mean most problems you most
[L2283] [105:31.44] processes in nature are not easily
[L2284] [105:33.84] reversible. You make an omelette from an
[L2285] [105:36.72] egg, you know, reversing this is
[L2286] [105:40.16] doesn't take the same amount of time.
[L2287] [105:44.24] That's the usual example of a physical
[L2288] [105:46.40] one function. But trap door functions
[L2289] [105:49.28] like factoring
[L2290] [105:51.20] problems for which from which you can
[L2291] [105:53.12] build public key systems and that's the
[L2292] [105:56.00] most really basic thing for electronic
[L2293] [105:58.72] commerce
[L2294] [106:00.32] uh are few. We don't know many. So we
[L2295] [106:03.04] know this I mentioned factoring discrete
[L2296] [106:05.44] log in the 90s
[L2297] [106:08.48] it and created this another type of step
[L2298] [106:13.12] function from uh problems on latises in
[L2299] [106:16.48] high dimensions I will not describe it
[L2300] [106:18.48] but it's another problem and then people
[L2301] [106:20.80] refined and got a few more similar of
[L2302] [106:23.68] similar nature and it turned out when
[L2303] [106:26.40] Peter Sh discovered this people
[L2304] [106:28.48] immediately tried to solve other
[L2305] [106:30.24] problems with quantum computers in Fact
[L2306] [106:33.04] even today we cannot solve too many
[L2307] [106:34.96] other problems with quantum computers.
[L2308] [106:37.52] These are special. The special thing
[L2309] [106:40.40] about them is that somehow you can
[L2310] [106:42.16] reduce them to finding periods in a
[L2311] [106:45.52] signal and periods is like fel
[L2312] [106:47.52] transform. A f transform turns out to in
[L2313] [106:50.88] exponential space but f transform you
[L2314] [106:53.92] can do somehow with quantum computers
[L2315] [106:57.12] with interference. the latis problems
[L2316] [106:59.84] and problems related to it some called
[L2317] [107:03.52] learning with arrows and similar uh you
[L2318] [107:07.28] know to this day nobody found an
[L2319] [107:10.96] efficient quantum algorithm for them so
[L2320] [107:13.52] there's no even theory forget building
[L2321] [107:15.52] quantum computers we don't know how to
[L2322] [107:18.24] solve them and so uh what the world is
[L2323] [107:21.52] not just complexity theory is the whole
[L2324] [107:23.20] physical world of you know uh security
[L2325] [107:26.88] systems
[L2326] [107:28.32] And also governments like the NSA,
[L2327] [107:31.84] you know, is you know supporting or you
[L2328] [107:35.28] know asking the world to produce
[L2329] [107:38.88] assumptions that may be resilient to
[L2330] [107:42.32] quantum attacks. And so this is a huge
[L2331] [107:46.08] change. There's a major change in the
[L2332] [107:48.48] interaction between computer scientists
[L2333] [107:50.88] and physicists which grew tremendously
[L2334] [107:54.08] since this discovery
[L2335] [107:56.40] and it's reached in in many many ways
[L2336] [107:58.80] that are not the the influence of the
[L2337] [108:02.72] algorithmic thinking of uh on on
[L2338] [108:06.16] physical theories including today
[L2339] [108:08.88] theories in quantum gravity, black holes
[L2340] [108:11.04] and so is immense and yeah we have new
[L2341] [108:14.32] sources of problems and new models and
[L2342] [108:16.56] complexity classes etc etc and uh
[L2343] [108:20.96] there's a a fantastic fantastic
[L2344] [108:23.60] interaction
[L2345] [108:25.36] um
[L2346] [108:26.96] and uh it's also in complexity theory
[L2347] [108:30.80] uh in that it turns out that you can
[L2348] [108:34.72] discover quantum algorithms and maybe
[L2349] [108:37.04] then dequantize them in special cases
[L2350] [108:40.32] like I mentioned factoring before the
[L2351] [108:43.28] randomizing
[L2352] [108:44.80] and so sometimes It's a way, it's a road
[L2353] [108:47.60] to discover new algorithms.
[L2354] [108:50.48] It reveals connections between problems.
[L2355] [108:52.88] It's it's extremely rich. But one of the
[L2356] [108:55.84] maybe most amazing consequences is that
[L2357] [108:59.76] people I mean we being what we are, we
[L2358] [109:02.88] make up models and uh study them. And uh
[L2359] [109:07.44] the interactive proofs I mentioned
[L2360] [109:09.20] before uh turns out that uh even before
[L2361] [109:12.80] quantum they were generalized to
[L2362] [109:15.20] interactive proofs with not with one
[L2363] [109:17.20] prover but with many provers which seem
[L2364] [109:19.68] to be you know weird but turns out to be
[L2365] [109:22.88] very important in itself because it led
[L2366] [109:25.52] to this PCP theorem. Then people said
[L2367] [109:29.12] okay let's allow quantum verifiers
[L2368] [109:31.36] quantum provers and see what they can.
[L2369] [109:34.88] So one amazing result which is about
[L2370] [109:37.04] five years ago is the acronyms. Of
[L2371] [109:40.72] course we have acquames for all these
[L2372] [109:42.40] complexity classes. It's MIP star equal.
[L2373] [109:46.48] You may have seen it maybe you didn't.
[L2374] [109:49.20] And it looks weird but I'll tell you
[L2375] [109:50.96] what what it says really. It says that
[L2376] [109:54.16] there is a weird really weird uh proof
[L2377] [109:58.16] system with quantum provers
[L2378] [110:01.04] that uh you know trying to convince
[L2379] [110:03.92] verifiers an efficient verifier and it
[L2380] [110:07.12] turns out you know you ask for which
[L2381] [110:08.72] problems can they do it? Forget their
[L2382] [110:10.24] own knowledge just convince. And it
[L2383] [110:12.72] turns out they can do it for the holding
[L2384] [110:15.52] problem for for problems that are not
[L2385] [110:18.32] computable. Things that are not
[L2386] [110:20.56] computable are verifiable
[L2387] [110:24.48] by efficient verifiers if the provers
[L2388] [110:27.84] are quantum and they are entangled and
[L2389] [110:30.00] whatever. But it's a weird proof system.
[L2390] [110:33.12] Very weird. But it does something that
[L2391] [110:35.92] looks totally, you know, ridiculous.
[L2392] [110:38.72] things that are uncomputable by any any
[L2393] [110:41.68] classical are verifiable in this
[L2394] [110:45.12] interactive probabistic sense by uh
[L2395] [110:49.04] efficient verifier.
[L2396] [110:51.84] So what I like to say in talking about
[L2397] [110:55.52] this is that it seems that the best
[L2398] [110:58.08] reaction, best hypothetical reaction of
[L2399] [111:00.96] anybody who hears this. Okay, you
[L2400] [111:03.60] complexity theorist, you you plain your
[L2401] [111:06.48] sandbox and you build all these sand
[L2402] [111:08.80] casters and make up all these models
[L2403] [111:10.96] that have nothing to do with anything
[L2404] [111:13.28] just because you can and you get once
[L2405] [111:15.68] you weird enough, you get weird enough,
[L2406] [111:18.48] you know, consequences. So one message
[L2407] [111:21.28] which I think is very powerful is that
[L2408] [111:24.48] this result has absolutely fundamental
[L2409] [111:28.40] impact on math and physics. It turns out
[L2410] [111:32.00] that it implies and this was already
[L2411] [111:35.12] done in the initial paper.
[L2412] [111:39.12] It implies resolution of well-known
[L2413] [111:43.20] conjectures in math and physics.
[L2414] [111:46.00] It turns out that the you know weird as
[L2415] [111:48.72] it is it's a new mathematical technique
[L2416] [111:52.40] to solve problems that nobody had any
[L2417] [111:55.04] idea famous problems important problems
[L2418] [111:57.36] that fields were dedicated to are
[L2419] [112:00.80] resolved by this result by the
[L2420] [112:02.80] techniques of this result. So you ask
[L2421] [112:05.60] the impact of you see the impact is
[L2422] [112:09.20] many generations over with for different
[L2423] [112:12.24] motivations and uh developments but all
[L2424] [112:16.40] of them following the methodology of
[L2425] [112:19.44] complexity theory of understanding the
[L2426] [112:21.52] power of you know composational models,
