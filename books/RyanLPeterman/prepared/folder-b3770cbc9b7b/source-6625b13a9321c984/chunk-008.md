Chunk 8; segments 2326–2653. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L2335] [01:24:25.28] or the like this is no one uses these
[L2336] [01:24:27.60] anymore, I don't think, but they were
[L2337] [01:24:28.96] this thing that were in was in there. He
[L2338] [01:24:30.88] had me write a parser for loading ANI
[L2339] [01:24:32.96] files, right? Like it's just meaningless
[L2340] [01:24:35.04] stuff. Uh, so my experience there was
[L2341] [01:24:37.92] pretty lame. Like I was like, this is
[L2342] [01:24:39.28] kind of dumb. Like I don't really want
[L2343] [01:24:41.36] to work here, right? But it could have
[L2344] [01:24:43.36] been totally different. Like if I had
[L2345] [01:24:45.12] been on some team that had like really
[L2346] [01:24:47.28] inspired me to like learn the stuff that
[L2347] [01:24:49.76] I didn't know. I didn't know assembly
[L2348] [01:24:51.20] language at that time really at all. I
[L2349] [01:24:53.20] think the only thing I'd ever written
[L2350] [01:24:54.16] assembly language was a joystick pulling
[L2351] [01:24:55.68] routine for DOSs because the only way
[L2352] [01:24:57.12] you could pull the joy joystick in DOSs,
[L2353] [01:24:59.04] right? And I think that's really it. If
[L2354] [01:25:01.44] I'm honest about it, I think most of it
[L2355] [01:25:03.12] is that I think when you're even if
[L2356] [01:25:05.04] you're a very brash youngster, which I
[L2357] [01:25:07.04] was, and even if you think that you're
[L2358] [01:25:09.36] very independent,
[L2359] [01:25:11.12] um I think you definitely
[L2360] [01:25:14.40] gravitate towards people who you see
[L2361] [01:25:16.72] doing things you think are impressive
[L2362] [01:25:19.68] or, you know, technologically
[L2363] [01:25:21.92] interesting.
[L2364] [01:25:23.60] And that is just not the experience I
[L2365] [01:25:25.44] had at Microsoft. Now, there were some
[L2366] [01:25:26.88] people who I like the people I went out
[L2367] [01:25:28.40] to go work with were people in other
[L2368] [01:25:30.32] parts of Microsoft who were leaving
[L2369] [01:25:31.92] Microsoft to do like a startup company,
[L2370] [01:25:33.92] right? And those were the people that I
[L2371] [01:25:36.00] was really like impressed with. Like
[L2372] [01:25:37.52] those were the people that I wanted to
[L2373] [01:25:38.72] hang out with. So like if I just look at
[L2374] [01:25:40.88] it in a rears like if those people had
[L2375] [01:25:42.80] just been staying at Microsoft and doing
[L2376] [01:25:44.32] something maybe I would have gone,
[L2377] [01:25:46.08] right? And I think that's the truth of
[L2378] [01:25:48.56] it as best I can determine at this
[L2379] [01:25:50.40] point. Anyway,
[L2380] [01:25:51.60] >> so you moved across the country to go
[L2381] [01:25:54.56] and work with those people at a startup.
[L2382] [01:25:56.32] >> Yes.
[L2383] [01:25:56.88] >> That's feels pretty risky uh to do. You
[L2384] [01:26:00.48] know,
[L2385] [01:26:00.88] >> it it was especially because at that
[L2386] [01:26:02.64] time a startup is not really what you
[L2387] [01:26:04.80] think of as a startup today. Like
[L2388] [01:26:06.40] startup is just like some scrappy people
[L2389] [01:26:08.08] in like a crappy office doing stuff.
[L2390] [01:26:10.00] Like nowadays you think startup it's
[L2391] [01:26:11.52] like well we've got $10 million in VC
[L2392] [01:26:13.52] funding and we you know like have free
[L2393] [01:26:16.24] sodas and what like in the break room
[L2394] [01:26:18.88] and a massage uh a masseuse comes in
[L2395] [01:26:21.60] periodically or something like this
[L2396] [01:26:22.80] right like I don't know what the what
[L2397] [01:26:24.24] the now version of a startup is but it's
[L2398] [01:26:26.88] very different right um so yeah it was
[L2399] [01:26:30.96] it was pretty risky and I don't really
[L2400] [01:26:33.28] know why I did it it was mostly just
[L2401] [01:26:35.52] because I hadn't had really good
[L2402] [01:26:36.88] experiences with education like I didn't
[L2403] [01:26:39.52] really want to to do um like college or
[L2404] [01:26:44.72] like I I didn't want to do any more
[L2405] [01:26:47.12] education. Like I wanted to actually
[L2406] [01:26:48.40] work for whatever reason and this seemed
[L2407] [01:26:51.60] like a this was just the easiest way to
[L2408] [01:26:54.56] do that. And I don't really regret it
[L2409] [01:26:56.64] honestly. Um,
[L2410] [01:26:59.44] I've been able to learn most of the
[L2411] [01:27:00.88] things that I would have needed to like
[L2412] [01:27:02.72] if I was going to go do a PhD or
[L2413] [01:27:04.24] something like I've ended up doing work
[L2414] [01:27:06.00] that I that is the sorts of stuff like
[L2415] [01:27:08.16] I've I've been lucky enough to be in
[L2416] [01:27:10.24] positions where I could go spend, you
[L2417] [01:27:12.32] know, a few months writing like this,
[L2418] [01:27:15.36] you know, uh, this particular like
[L2419] [01:27:18.00] linear lease squares solver or something
[L2420] [01:27:19.60] like that like the kinds of things you
[L2421] [01:27:21.04] might have done as like a thesis or
[L2422] [01:27:22.56] something. uh or or you know that that
[L2423] [01:27:26.24] walks somebody might have done the
[L2424] [01:27:27.12] witness those sorts of things are the
[L2425] [01:27:29.20] kinds of things you would have done had
[L2426] [01:27:30.96] you decided to get a master's degree or
[L2427] [01:27:32.64] something like that so I'm fortunate
[L2428] [01:27:34.40] enough that I've kind of been able to
[L2429] [01:27:36.56] have that part of the education um
[L2430] [01:27:39.52] because not everyone gets that
[L2431] [01:27:40.72] opportunity like you may never get you
[L2432] [01:27:42.72] know if you if you don't do a master's
[L2433] [01:27:44.80] thesis or you don't do a PhD thesis you
[L2434] [01:27:46.96] may never really get the chance to like
[L2435] [01:27:48.72] really do a deep like work on a on one
[L2436] [01:27:51.92] problem and like learn a lot about it,
[L2437] [01:27:53.92] read a lot of papers, do you know may
[L2438] [01:27:55.84] maybe make some novel contribution in in
[L2439] [01:27:58.32] some very small way usually, right? But
[L2440] [01:28:00.80] um and so that that I was just lucky
[L2441] [01:28:03.20] enough to do. So I don't really regret
[L2442] [01:28:05.44] not doing something like that. But I
[L2443] [01:28:07.60] think you know had I not had that those
[L2444] [01:28:10.08] opportunities and subsequently I could
[L2445] [01:28:12.64] see being I could see being regretful
[L2446] [01:28:14.16] about that because that is something
[L2447] [01:28:15.12] that I do enjoy doing and if id never
[L2448] [01:28:17.36] had the chance I would have been sad. So
[L2449] [01:28:19.20] you you went and you traveled to this
[L2450] [01:28:21.12] startup
[L2451] [01:28:22.72] because there's there's no there's no
[L2452] [01:28:24.80] funding it sounds like. So yeah, what
[L2453] [01:28:26.64] did you So it's just a group of guys
[L2454] [01:28:28.80] just was there pay or it's just
[L2455] [01:28:30.72] >> not really no it was it was pretty
[L2456] [01:28:32.64] rough. Uh and I it didn't last very
[L2457] [01:28:34.56] long, right? Um I ended up going to work
[L2458] [01:28:37.12] at an actual game company shortly after
[L2459] [01:28:38.64] that called Gaspired Games. And then
[L2460] [01:28:40.56] shortly after that I started work at Rad
[L2461] [01:28:42.32] Game Tools which I stayed at for quite
[L2462] [01:28:43.84] some time uh and where I did like that
[L2463] [01:28:46.08] character animation system and stuff. So
[L2464] [01:28:47.44] it was it was pretty quick into not
[L2465] [01:28:50.24] doing that. But um it was still a pretty
[L2466] [01:28:52.80] educational experience for me. And also
[L2467] [01:28:54.72] uh what I will say is um at the time so
[L2468] [01:28:58.00] uh I worked with there a guy named Chris
[L2469] [01:29:00.48] Hecker who uh I have to give like
[L2470] [01:29:03.68] basically complete credit to for
[L2471] [01:29:06.72] teaching me basically about like reading
[L2472] [01:29:09.84] technical papers.
[L2473] [01:29:11.84] Like before that time, I just thought
[L2474] [01:29:14.72] math was kind of stupid and an annoying
[L2475] [01:29:16.32] thing you had to do like in class,
[L2476] [01:29:17.84] right? And I I definitely didn't know
[L2477] [01:29:20.32] anything about like
[L2478] [01:29:22.32] reading a sigraph's proceedings really,
[L2479] [01:29:24.56] right? Um and I may have been like aware
[L2480] [01:29:27.36] I mean I was aware of sigraph. I knew
[L2481] [01:29:28.88] what it was, but I don't think if you'd
[L2482] [01:29:30.72] handed me, you know, that binder, I
[L2483] [01:29:33.52] would have known what that was or what
[L2484] [01:29:35.44] to do with it. like, you know, I think
[L2485] [01:29:38.24] like the biggest takeaway that I got
[L2486] [01:29:40.24] from that other than startups are hard
[L2487] [01:29:42.48] and maybe don't do them uh unless you
[L2488] [01:29:44.64] have a lot of people and a lot of
[L2489] [01:29:45.84] funding and aren't really that much on
[L2490] [01:29:47.92] the line like maybe uh but uh the
[L2491] [01:29:52.40] biggest takeaway that I got from that
[L2492] [01:29:53.92] that was positive was just a a a much
[L2493] [01:29:57.52] deeper appreciation for math, a much
[L2494] [01:30:00.08] deeper appreciation for research, how to
[L2495] [01:30:02.08] read it. Um, that's where I learned to
[L2496] [01:30:04.40] use like Sightseer, which would be like
[L2497] [01:30:06.00] kind of the precursor to like Google
[L2498] [01:30:07.68] Scholar or whatever, crawling references
[L2499] [01:30:09.76] and all that stuff. In a lot of ways,
[L2500] [01:30:11.28] you could say, uh, if I hadn't had that
[L2501] [01:30:13.36] experience, I bet I wouldn't have given
[L2502] [01:30:14.48] the two talks that we've talked about
[L2503] [01:30:16.24] for most of the interview because what
[L2504] [01:30:18.80] are those talks? They're me crawling
[L2505] [01:30:20.24] every reference, right? They're just me
[L2506] [01:30:22.00] going back and back and back and back
[L2507] [01:30:23.68] and looking at everything that I can
[L2508] [01:30:25.52] find. Um, and that's something that if
[L2509] [01:30:29.60] you if no one ever conveys to you the
[L2510] [01:30:33.36] importance of reading the scholarship
[L2511] [01:30:35.36] and being aware of what's being done and
[L2512] [01:30:37.12] also teaches you how to read a tech
[L2513] [01:30:38.72] paper and how to parse through it. I I
[L2514] [01:30:41.68] don't know that you get that, you know,
[L2515] [01:30:42.72] I don't know that you get that.
[L2516] [01:30:44.40] >> I remember early in my career, I think
[L2517] [01:30:46.40] there's this, I guess, common path of
[L2518] [01:30:48.96] like these, you know, big companies and
[L2519] [01:30:50.80] then there's this thought of, oh, me and
[L2520] [01:30:53.04] a couple buddies, let's go, let's go
[L2521] [01:30:54.88] build [laughter] something. Now, now
[L2522] [01:30:56.64] with your experience looking back, if
[L2523] [01:30:59.36] you someone out there's uh young and
[L2524] [01:31:02.16] thinking about starting, would you say
[L2525] [01:31:04.24] go that common path or would you say
[L2526] [01:31:08.00] take the the chance?
[L2527] [01:31:11.12] >> You know, uh it's a really tough
[L2528] [01:31:14.48] question and I think that the advice
[L2529] [01:31:17.44] like the advice is that you have to
[L2530] [01:31:20.00] think about what it is that you want to
[L2531] [01:31:23.28] do every day. Like, so in my mind, the
[L2532] [01:31:28.80] things I regret are the times when I've
[L2533] [01:31:31.84] had to do things or chosen to do things
[L2534] [01:31:34.72] that I wasn't really that happy doing
[L2535] [01:31:36.88] every day, right?
[L2536] [01:31:39.04] And so I think you just have to optimize
[L2537] [01:31:41.36] for the experience you want to have
[L2538] [01:31:42.96] because a startup might work out, it
[L2539] [01:31:44.64] might not. It's always a risk, right?
[L2540] [01:31:47.20] You may go to the big company um and you
[L2541] [01:31:50.72] know it may be cool, there may be
[L2542] [01:31:52.08] interesting things there or there might
[L2543] [01:31:53.28] not be. like who know like you don't
[L2544] [01:31:54.72] really know you're making a kind of
[L2545] [01:31:56.32] blind decision
[L2546] [01:31:59.04] and so I think you kind of have to
[L2547] [01:32:00.48] optimize for what do you want your
[L2548] [01:32:02.32] dayto-day to be like like what do you
[L2549] [01:32:04.40] want the experience to be and you want
[L2550] [01:32:08.64] to like keep a running t like you want
[L2551] [01:32:11.92] to be aware of it like if you make a
[L2552] [01:32:13.60] decision and six months in you are not
[L2553] [01:32:16.24] liking what you're doing every day then
[L2554] [01:32:18.00] you need to get out of that right like
[L2555] [01:32:20.08] that's my opinion
[L2556] [01:32:22.24] so I don't know I I think most people
[L2557] [01:32:24.48] probably if they sit down and actually
[L2558] [01:32:28.16] like clear their mind and aren't aren't
[L2559] [01:32:32.08] engaging in too motivated a reasoning
[L2560] [01:32:33.92] but just for themselves go what do I
[L2561] [01:32:36.56] envision working at the startup will be
[L2562] [01:32:38.32] like what will I actually be doing every
[L2563] [01:32:40.16] day like am I going to like that is this
[L2564] [01:32:42.56] going to be thrilling like trying to
[L2565] [01:32:44.00] make this thing work and like being kind
[L2566] [01:32:46.24] of on the edge um and you know uh do I
[L2567] [01:32:50.96] want the the kind of war stories of like
[L2568] [01:32:53.44] the things we had to do to pull off the
[L2569] [01:32:55.36] demo or whatever, right? If all that
[L2570] [01:32:58.08] sounds exciting to you and you want to
[L2571] [01:32:59.28] have that experience, then you should do
[L2572] [01:33:00.72] that thing. And and and I would say like
[L2573] [01:33:03.44] really I really mean that like I don't
[L2574] [01:33:06.00] even think you should take into account
[L2575] [01:33:07.20] like even like let's say you know the
[L2576] [01:33:08.40] startup's going to fail. If that's if
[L2577] [01:33:11.04] you want to have that experience then
[L2578] [01:33:12.40] you need to do it, right? It's just like
[L2579] [01:33:13.92] anything else. It's like going and um
[L2580] [01:33:17.28] backpacking across Europe or playing
[L2581] [01:33:19.12] guitar at a nightclub. It's like you may
[L2582] [01:33:22.08] know that these things are not
[L2583] [01:33:23.44] profitable.
[L2584] [01:33:24.96] It's just is that the experience you
[L2585] [01:33:26.56] want to have? Are you going to look back
[L2586] [01:33:27.68] on that six months or a year or five
[L2587] [01:33:29.28] years or whatever the amount of time
[L2588] [01:33:30.72] you're thinking of committing to it? Are
[L2589] [01:33:32.24] you going to look back and say I'm glad
[L2590] [01:33:33.60] I did that or are you going to be like
[L2591] [01:33:36.24] that was the you know those that's time
[L2592] [01:33:38.16] that I would have rather have spent some
[L2593] [01:33:39.68] other way, right? And so I think most
[L2594] [01:33:42.32] people can probably if they're honest
[L2595] [01:33:43.92] with themselves at least make a pretty
[L2596] [01:33:45.36] good guess. And that guess if they're
[L2597] [01:33:47.04] honest with themselves is going to be
[L2598] [01:33:48.08] better than any advice I'm going to give
[L2599] [01:33:49.28] them. like my guess about what you
[L2600] [01:33:51.28] should do is going to be worse than
[L2601] [01:33:52.24] yours. So, you should just make that uh
[L2602] [01:33:54.64] determination because another way to
[L2603] [01:33:56.48] look at it is like you know that the big
[L2604] [01:33:57.84] company side is like maybe you just want
[L2605] [01:34:00.48] to have some security like maybe when
[L2606] [01:34:02.80] you're starting out like I mean I'll
[L2607] [01:34:04.00] just give some examples like maybe you
[L2608] [01:34:05.92] want to uh spend a lot of time dating.
[L2609] [01:34:08.32] You want to you want to uh find a
[L2610] [01:34:10.64] partner and you want to have a
[L2611] [01:34:11.76] relationship and you want to have a
[L2612] [01:34:12.96] family.
[L2613] [01:34:14.48] Maybe that's more important to you.
[L2614] [01:34:16.40] Maybe the startup yeah might be fun.
[L2615] [01:34:18.80] Maybe it would be more money if it
[L2616] [01:34:20.40] worked out or whatever, but like maybe
[L2617] [01:34:21.76] the stability is is actually going to be
[L2618] [01:34:23.92] something that that you would that that
[L2619] [01:34:25.52] you would really benefit from because
[L2620] [01:34:27.44] the sorts of things that you imagine
[L2621] [01:34:29.28] being fulfilling in your life are not
[L2622] [01:34:30.88] all around what you're going to be doing
[L2623] [01:34:33.12] in computing. I think you can know have
[L2624] [01:34:36.72] some guess about those things when you
[L2625] [01:34:39.36] if you just let yourself have some space
[L2626] [01:34:41.12] to think about it and don't engage in
[L2627] [01:34:42.96] too much motivated reasoning about it.
[L2628] [01:34:44.56] Right?
[L2629] [01:34:46.00] And uh and I think that would be the
[L2630] [01:34:47.68] best way to make a decision if you're
[L2631] [01:34:48.96] going to make one. That's my that's my
[L2632] [01:34:50.64] feeling about it. Anyway,
[L2633] [01:34:52.56] >> if we talked a lot about video game
[L2634] [01:34:54.16] engineering, and I have no idea what
[L2635] [01:34:57.04] goes into video games, if you were to
[L2636] [01:34:59.44] just boil it down to the the big pieces
[L2637] [01:35:02.24] that you need for a video game, what are
[L2638] [01:35:04.80] those software components?
[L2639] [01:35:07.28] So the biggest thing that's different
[L2640] [01:35:10.56] about a video game is that the sort of
[L2641] [01:35:14.32] original mental model that you're talked
[L2642] [01:35:16.40] that you're taught in programming which
[L2643] [01:35:18.56] is like the uh standard IO like I get
[L2644] [01:35:21.60] some input in I process it I put some
[L2645] [01:35:24.08] input out is like not how it works right
[L2646] [01:35:27.76] so the biggest mental shift is just like
[L2647] [01:35:29.76] oh the way that a video game or a
[L2648] [01:35:32.16] simulation of any kind right works is I
[L2649] [01:35:35.76] need to have some world state and I'm
[L2650] [01:35:38.08] constantly updating that world state on
[L2651] [01:35:40.48] a regular interval. Everything is always
[L2652] [01:35:42.56] happening. There's no I wait for input
[L2653] [01:35:44.80] and then I do something, right?
[L2654] [01:35:46.48] Everything is always going because it is
[L2655] [01:35:48.16] real time like the time is going um
[L2656] [01:35:51.20] forward. So the components tend to be
[L2657] [01:35:54.00] built around this idea and it depends on
[L2658] [01:35:56.80] what level of sophistication you end up
[L2659] [01:35:58.48] getting into but in general you need a
[L2660] [01:36:01.92] way of storing that world state. So some
[L2661] [01:36:03.92] kind of we usually call these entities.
[L2662] [01:36:06.16] um like the things that make up a world,
