Chunk 7; segments 2083–2457. Start may repeat the previous chunk for context.

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
[L2166] [01:40:02.40] quantum computer is at least as strong
[L2167] [01:40:04.40] as a proistic computer. How do you see
[L2168] [01:40:06.96] it? You just measure the quantum bits
[L2169] [01:40:09.20] before you start. You measure them. This
[L2170] [01:40:12.08] what I mentioned about the photons in
[L2171] [01:40:14.00] the beginning. If you you have a some
[L2172] [01:40:16.72] basic superposition on I mean quantum
[L2173] [01:40:19.68] quantum bit if you measure it you get a
[L2174] [01:40:22.16] random bit. So because of that quantum
[L2175] [01:40:25.12] computers are at least as strong as
[L2176] [01:40:27.52] proistic computers. uh okay so it's a
[L2177] [01:40:31.44] model of computation and uh it was
[L2178] [01:40:34.56] suggested in the 80s fineman
[L2179] [01:40:38.96] uh and man and others
[L2180] [01:40:41.84] uh suggested you know letting algorithms
[L2181] [01:40:46.64] use these quantum mechanical operations
[L2182] [01:40:50.08] mainly in originally for just simulating
[L2183] [01:40:52.88] quantum systems rather than building
[L2184] [01:40:55.68] bigger apparatus to yeah like we
[L2185] [01:40:58.40] simulate other things turbulence I don't
[L2186] [01:41:00.48] know what's the power of quantum
[L2187] [01:41:02.64] algorithms again let's say running in
[L2188] [01:41:05.52] polinomial time or efficient quantum
[L2189] [01:41:07.36] algorithm can they do more than
[L2190] [01:41:09.92] efficient classical ones deterministic
[L2191] [01:41:12.64] or probabilistic and it wasn't clear for
[L2192] [01:41:15.68] a while and there were
[L2193] [01:41:18.08] a few examples that were very stylized
[L2194] [01:41:20.40] but were not for concrete natural
[L2195] [01:41:22.88] problems we care about and then in 94
[L2196] [01:41:26.00] Peter saw sort of Yeah, created an
[L2197] [01:41:30.56] earthquake or an avalanche. Uh he uh
[L2198] [01:41:35.44] found quantum algorithms that are
[L2199] [01:41:37.44] efficient, the factual integers and also
[L2200] [01:41:41.44] complete discrete logarithms. The two
[L2201] [01:41:43.44] most basic uh underpinnings of all
[L2202] [01:41:46.56] security systems that exist and this set
[L2203] [01:41:49.60] the world on fire, right? So uh lots of
[L2204] [01:41:53.28] people try to do a lot of things. uh of
[L2205] [01:41:56.40] course you know people want to you have
[L2206] [01:41:59.92] them these algorithms they implement
[L2207] [01:42:02.08] maybe they want to break or other people
[L2208] [01:42:04.96] skip the system. So as you know since
[L2209] [01:42:07.52] then billions were invested by companies
[L2210] [01:42:10.64] by governments by uh lots of people
[L2211] [01:42:14.80] trying to to build the technological
[L2212] [01:42:17.92] infrastructure and this is extremely
[L2213] [01:42:20.40] complicated. holding beats in superp
[L2214] [01:42:23.12] position is extremely complicated.
[L2215] [01:42:25.92] There's things that are called the
[L2216] [01:42:28.24] there's the noise. I mean when people
[L2217] [01:42:31.28] build classical computers like for noman
[L2218] [01:42:33.76] here in the
[L2219] [01:42:35.68] uh building next door u u you know noise
[L2220] [01:42:40.88] was one of the serious problems because
[L2221] [01:42:42.64] the bits were really in vacuum tubes and
[L2222] [01:42:45.76] uh they had to contend and in fact he
[L2223] [01:42:48.56] built a nice theory of uh classical
[L2224] [01:42:51.84] computers that have errors noise they
[L2225] [01:42:54.48] have to cope with errors some of their
[L2226] [01:42:56.16] components can be faulty but this today
[L2227] [01:42:59.84] is hardware you know has no errors to
[L2228] [01:43:02.56] speak of. We don't I mean there are
[L2229] [01:43:04.40] error correcting mechanisms but uh we
[L2230] [01:43:07.44] don't need them for classical computing.
[L2231] [01:43:10.24] Intel chips don't have you know I think
[L2232] [01:43:12.88] error correction in them. Hardware is
[L2233] [01:43:15.12] very reliable. When you move to quantum
[L2234] [01:43:18.32] there is this the coherence noise
[L2235] [01:43:21.76] in quantum mechanics everything depends
[L2236] [01:43:23.92] on everything. the world can influence
[L2237] [01:43:27.12] uh the computation in your laptop and uh
[L2238] [01:43:31.68] and protecting from this is very hard.
[L2239] [01:43:34.00] There are quantum correcting codes and
[L2240] [01:43:36.08] that's part of the solutions. That's
[L2241] [01:43:38.40] only one of the problems. Just holding
[L2242] [01:43:40.32] bits in superp position is hard and
[L2243] [01:43:42.72] there are many hard technological issues
[L2244] [01:43:45.44] and there's progress on that. So this is
[L2245] [01:43:47.68] one line of huge investment.
[L2246] [01:43:50.88] Uh the other line comes from
[L2247] [01:43:52.40] cryptography because of course everybody
[L2248] [01:43:55.04] should be worried right. I mean you know
[L2249] [01:43:57.76] forget quantum computers if tomorrow uh
[L2250] [01:44:00.96] I mean really tomorrow uh somebody finds
[L2251] [01:44:04.48] even a classical factory algorithms in
[L2252] [01:44:07.36] algorithm in polinomial time I think
[L2253] [01:44:09.20] there'll be chaos in the world because
[L2254] [01:44:11.76] nobody nobody can do any transactions
[L2255] [01:44:14.80] because most security systems still rely
[L2256] [01:44:17.04] on
[L2257] [01:44:19.52] um
[L2258] [01:44:21.04] and so of course uh we want to change
[L2259] [01:44:25.12] these
[L2260] [01:44:26.08] We want to change the underlying
[L2261] [01:44:27.76] assumptions of security. We want to rely
[L2262] [01:44:31.68] the whole revolution in cryptography was
[L2263] [01:44:33.84] that we rest cryptography on
[L2264] [01:44:35.84] computationally hard assumptions and
[L2265] [01:44:38.56] with this we build all the wonderful
[L2266] [01:44:40.48] public key systems and you know all the
[L2267] [01:44:45.04] magical things you can do with
[L2268] [01:44:48.00] under uh by assuming that players are
[L2269] [01:44:52.24] computationally limited.
[L2270] [01:44:54.56] uh but now if they are the the
[L2271] [01:44:57.04] adversaries are quantum computers
[L2272] [01:44:59.44] certainly they can break this assumption
[L2273] [01:45:02.00] you want to find other mathematical
[L2274] [01:45:04.24] problems computational problems
[L2275] [01:45:07.84] uh which are somehow hard even to
[L2276] [01:45:11.68] quantum computers.
[L2277] [01:45:13.84] So that's a the whole field this change
[L2278] [01:45:16.48] complexity theory and cryptography there
[L2279] [01:45:19.52] is an army of people who are just uh
[L2280] [01:45:23.12] trying to invent problems. I maybe
[L2281] [01:45:26.08] should stress one way functions are easy
[L2282] [01:45:28.08] to find. I mean most problems you most
[L2283] [01:45:31.44] processes in nature are not easily
[L2284] [01:45:33.84] reversible. You make an omelette from an
[L2285] [01:45:36.72] egg, you know, reversing this is
[L2286] [01:45:40.16] doesn't take the same amount of time.
[L2287] [01:45:44.24] That's the usual example of a physical
[L2288] [01:45:46.40] one function. But trap door functions
[L2289] [01:45:49.28] like factoring
[L2290] [01:45:51.20] problems for which from which you can
[L2291] [01:45:53.12] build public key systems and that's the
[L2292] [01:45:56.00] most really basic thing for electronic
[L2293] [01:45:58.72] commerce
[L2294] [01:46:00.32] uh are few. We don't know many. So we
[L2295] [01:46:03.04] know this I mentioned factoring discrete
[L2296] [01:46:05.44] log in the 90s
[L2297] [01:46:08.48] it and created this another type of step
[L2298] [01:46:13.12] function from uh problems on latises in
[L2299] [01:46:16.48] high dimensions I will not describe it
[L2300] [01:46:18.48] but it's another problem and then people
[L2301] [01:46:20.80] refined and got a few more similar of
[L2302] [01:46:23.68] similar nature and it turned out when
[L2303] [01:46:26.40] Peter Sh discovered this people
[L2304] [01:46:28.48] immediately tried to solve other
[L2305] [01:46:30.24] problems with quantum computers in Fact
[L2306] [01:46:33.04] even today we cannot solve too many
[L2307] [01:46:34.96] other problems with quantum computers.
[L2308] [01:46:37.52] These are special. The special thing
[L2309] [01:46:40.40] about them is that somehow you can
[L2310] [01:46:42.16] reduce them to finding periods in a
[L2311] [01:46:45.52] signal and periods is like fel
[L2312] [01:46:47.52] transform. A f transform turns out to in
[L2313] [01:46:50.88] exponential space but f transform you
[L2314] [01:46:53.92] can do somehow with quantum computers
[L2315] [01:46:57.12] with interference. the latis problems
[L2316] [01:46:59.84] and problems related to it some called
[L2317] [01:47:03.52] learning with arrows and similar uh you
[L2318] [01:47:07.28] know to this day nobody found an
[L2319] [01:47:10.96] efficient quantum algorithm for them so
[L2320] [01:47:13.52] there's no even theory forget building
[L2321] [01:47:15.52] quantum computers we don't know how to
[L2322] [01:47:18.24] solve them and so uh what the world is
[L2323] [01:47:21.52] not just complexity theory is the whole
[L2324] [01:47:23.20] physical world of you know uh security
[L2325] [01:47:26.88] systems
[L2326] [01:47:28.32] And also governments like the NSA,
[L2327] [01:47:31.84] you know, is you know supporting or you
[L2328] [01:47:35.28] know asking the world to produce
[L2329] [01:47:38.88] assumptions that may be resilient to
[L2330] [01:47:42.32] quantum attacks. And so this is a huge
[L2331] [01:47:46.08] change. There's a major change in the
[L2332] [01:47:48.48] interaction between computer scientists
[L2333] [01:47:50.88] and physicists which grew tremendously
[L2334] [01:47:54.08] since this discovery
[L2335] [01:47:56.40] and it's reached in in many many ways
[L2336] [01:47:58.80] that are not the the influence of the
[L2337] [01:48:02.72] algorithmic thinking of uh on on
[L2338] [01:48:06.16] physical theories including today
[L2339] [01:48:08.88] theories in quantum gravity, black holes
[L2340] [01:48:11.04] and so is immense and yeah we have new
[L2341] [01:48:14.32] sources of problems and new models and
[L2342] [01:48:16.56] complexity classes etc etc and uh
[L2343] [01:48:20.96] there's a a fantastic fantastic
[L2344] [01:48:23.60] interaction
[L2345] [01:48:25.36] um
[L2346] [01:48:26.96] and uh it's also in complexity theory
[L2347] [01:48:30.80] uh in that it turns out that you can
[L2348] [01:48:34.72] discover quantum algorithms and maybe
[L2349] [01:48:37.04] then dequantize them in special cases
[L2350] [01:48:40.32] like I mentioned factoring before the
[L2351] [01:48:43.28] randomizing
[L2352] [01:48:44.80] and so sometimes It's a way, it's a road
[L2353] [01:48:47.60] to discover new algorithms.
[L2354] [01:48:50.48] It reveals connections between problems.
[L2355] [01:48:52.88] It's it's extremely rich. But one of the
[L2356] [01:48:55.84] maybe most amazing consequences is that
[L2357] [01:48:59.76] people I mean we being what we are, we
[L2358] [01:49:02.88] make up models and uh study them. And uh
[L2359] [01:49:07.44] the interactive proofs I mentioned
[L2360] [01:49:09.20] before uh turns out that uh even before
[L2361] [01:49:12.80] quantum they were generalized to
[L2362] [01:49:15.20] interactive proofs with not with one
[L2363] [01:49:17.20] prover but with many provers which seem
[L2364] [01:49:19.68] to be you know weird but turns out to be
[L2365] [01:49:22.88] very important in itself because it led
[L2366] [01:49:25.52] to this PCP theorem. Then people said
[L2367] [01:49:29.12] okay let's allow quantum verifiers
[L2368] [01:49:31.36] quantum provers and see what they can.
[L2369] [01:49:34.88] So one amazing result which is about
[L2370] [01:49:37.04] five years ago is the acronyms. Of
[L2371] [01:49:40.72] course we have acquames for all these
[L2372] [01:49:42.40] complexity classes. It's MIP star equal.
[L2373] [01:49:46.48] You may have seen it maybe you didn't.
[L2374] [01:49:49.20] And it looks weird but I'll tell you
[L2375] [01:49:50.96] what what it says really. It says that
[L2376] [01:49:54.16] there is a weird really weird uh proof
[L2377] [01:49:58.16] system with quantum provers
[L2378] [01:50:01.04] that uh you know trying to convince
[L2379] [01:50:03.92] verifiers an efficient verifier and it
[L2380] [01:50:07.12] turns out you know you ask for which
[L2381] [01:50:08.72] problems can they do it? Forget their
[L2382] [01:50:10.24] own knowledge just convince. And it
[L2383] [01:50:12.72] turns out they can do it for the holding
[L2384] [01:50:15.52] problem for for problems that are not
[L2385] [01:50:18.32] computable. Things that are not
[L2386] [01:50:20.56] computable are verifiable
[L2387] [01:50:24.48] by efficient verifiers if the provers
[L2388] [01:50:27.84] are quantum and they are entangled and
[L2389] [01:50:30.00] whatever. But it's a weird proof system.
[L2390] [01:50:33.12] Very weird. But it does something that
[L2391] [01:50:35.92] looks totally, you know, ridiculous.
[L2392] [01:50:38.72] things that are uncomputable by any any
[L2393] [01:50:41.68] classical are verifiable in this
[L2394] [01:50:45.12] interactive probabistic sense by uh
[L2395] [01:50:49.04] efficient verifier.
[L2396] [01:50:51.84] So what I like to say in talking about
[L2397] [01:50:55.52] this is that it seems that the best
[L2398] [01:50:58.08] reaction, best hypothetical reaction of
[L2399] [01:51:00.96] anybody who hears this. Okay, you
[L2400] [01:51:03.60] complexity theorist, you you plain your
[L2401] [01:51:06.48] sandbox and you build all these sand
[L2402] [01:51:08.80] casters and make up all these models
[L2403] [01:51:10.96] that have nothing to do with anything
[L2404] [01:51:13.28] just because you can and you get once
[L2405] [01:51:15.68] you weird enough, you get weird enough,
[L2406] [01:51:18.48] you know, consequences. So one message
[L2407] [01:51:21.28] which I think is very powerful is that
[L2408] [01:51:24.48] this result has absolutely fundamental
[L2409] [01:51:28.40] impact on math and physics. It turns out
[L2410] [01:51:32.00] that it implies and this was already
[L2411] [01:51:35.12] done in the initial paper.
[L2412] [01:51:39.12] It implies resolution of well-known
[L2413] [01:51:43.20] conjectures in math and physics.
[L2414] [01:51:46.00] It turns out that the you know weird as
[L2415] [01:51:48.72] it is it's a new mathematical technique
[L2416] [01:51:52.40] to solve problems that nobody had any
[L2417] [01:51:55.04] idea famous problems important problems
[L2418] [01:51:57.36] that fields were dedicated to are
[L2419] [01:52:00.80] resolved by this result by the
[L2420] [01:52:02.80] techniques of this result. So you ask
[L2421] [01:52:05.60] the impact of you see the impact is
[L2422] [01:52:09.20] many generations over with for different
[L2423] [01:52:12.24] motivations and uh developments but all
[L2424] [01:52:16.40] of them following the methodology of
[L2425] [01:52:19.44] complexity theory of understanding the
[L2426] [01:52:21.52] power of you know composational models,
[L2427] [01:52:24.24] proof systems and so on has magically
[L2428] [01:52:27.44] led to such a consequence
[L2429] [01:52:30.80] and this is just we are in the beginning
[L2430] [01:52:33.44] of this right this type of proof
[L2431] [01:52:35.20] technique is now being explored and used
[L2432] [01:52:37.84] and there are more results you know
[L2433] [01:52:41.04] using this type of techniques to
[L2434] [01:52:42.88] longstanding problems pretty amazing
[L2435] [01:52:45.68] >> that's incredible yeah I mean in
[L2436] [01:52:47.60] complexity theory you know there's these
[L2437] [01:52:49.60] um what do you call them I guess like
[L2438] [01:52:52.08] ven diagrams of all possible problems
[L2439] [01:52:55.68] and you know the implicit assumption in
[L2440] [01:52:58.64] this picture is that these are these are
[L2441] [01:53:01.44] >> decidable problems
[L2442] [01:53:04.00] In some of these diagrams there's a
[L2443] [01:53:06.16] little in the corner there's a
[L2444] [01:53:07.68] >> unidable
[L2445] [01:53:08.40] >> undecidable ones and
[L2446] [01:53:09.76] >> unreachable. Yeah.
[L2447] [01:53:10.88] >> Right. And it's just uh I I can't I
[L2448] [01:53:15.36] don't even understand how you could
[L2449] [01:53:17.44] verify an undecidable.
[L2450] [01:53:19.52] >> It's a 200page paper. It builds on 10
[L2451] [01:53:22.32] years of understanding which is both a
[L2452] [01:53:25.92] lot of development in the quantum
[L2453] [01:53:29.20] algorithms and quantum proof systems
[L2454] [01:53:32.24] sphere but also relying on techniques
[L2455] [01:53:35.12] from classical proof systems which have
[L2456] [01:53:37.76] to do with coding theory and uh various
[L2457] [01:53:41.36] algebraic stuff that is used to prove
[L2458] [01:53:43.44] for example the PCP theorem that I
[L2459] [01:53:45.52] mentioned it's you know it's a huge body
[L2460] [01:53:48.80] of work and on top of this they all this
[L2461] [01:53:52.00] 200page paper in which they had to
[L2462] [01:53:54.16] develop many more tools and uh yeah
[L2463] [01:53:57.52] there you have it.
[L2464] [01:53:58.64] >> Wow. I mean when someone produces 200
[L2465] [01:54:02.16] pages of such complicated work that
[L2466] [01:54:05.68] makes such a outrageous claim how how
