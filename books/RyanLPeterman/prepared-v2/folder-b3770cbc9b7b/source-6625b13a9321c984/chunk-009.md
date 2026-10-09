Chunk 9; segments 2646–2982. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L2655] [01:35:48.16] real time like the time is going um
[L2656] [01:35:51.20] forward. So the components tend to be
[L2657] [01:35:54.00] built around this idea and it depends on
[L2658] [01:35:56.80] what level of sophistication you end up
[L2659] [01:35:58.48] getting into but in general you need a
[L2660] [01:36:01.92] way of storing that world state. So some
[L2661] [01:36:03.92] kind of we usually call these entities.
[L2662] [01:36:06.16] um like the things that make up a world,
[L2663] [01:36:08.16] right? So, some way of modeling what is
[L2664] [01:36:10.40] in the world, where are things in the
[L2665] [01:36:12.80] world, what is their state, what are
[L2666] [01:36:15.12] they doing right now. So, you need
[L2667] [01:36:17.28] something that does that, something that
[L2668] [01:36:19.44] is in charge of advancing that state.
[L2669] [01:36:22.16] This is a mixture of several things. Uh
[L2670] [01:36:24.56] it could involve physical simulation. It
[L2671] [01:36:27.44] could involve AI. Uh not necessarily
[L2672] [01:36:30.32] like large language model like the
[L2673] [01:36:31.84] modern notion of AI, but like path
[L2674] [01:36:33.84] finding. uh making a decision between
[L2675] [01:36:36.24] whether I should attack the player or
[L2676] [01:36:37.60] not like that sort of AI, right?
[L2677] [01:36:40.64] Um
[L2678] [01:36:42.24] so we have the the world some way of
[L2679] [01:36:44.00] showing the world state, some way of
[L2680] [01:36:45.20] advancing the world state, like an
[L2681] [01:36:46.56] update step that may involve lots of
[L2682] [01:36:48.40] things like that.
[L2683] [01:36:50.48] Then some way of presenting the world
[L2684] [01:36:52.40] state. So a renderer, right? And this is
[L2685] [01:36:54.72] something that typically uh has
[L2686] [01:36:58.24] uh I guess I would say it's it's
[L2687] [01:37:00.72] traditionally been a very important part
[L2688] [01:37:03.68] of a game because the visuals are often
[L2689] [01:37:08.56] something that is a selling point for
[L2690] [01:37:10.96] games.
[L2691] [01:37:12.56] People produce trailers certainly in the
[L2692] [01:37:15.28] AAA space. We're trying to show you how
[L2693] [01:37:17.12] cool the new lighting looks and the
[L2694] [01:37:19.12] whatever. So that is a pretty big
[L2695] [01:37:22.08] component of games. Often times you go
[L2696] [01:37:24.64] look at an indie pixel art game, it
[L2697] [01:37:26.64] might be much smaller, right? Because
[L2698] [01:37:27.84] that's a much smaller part of the
[L2699] [01:37:29.84] problem. Now that's generally what what
[L2700] [01:37:33.60] you know the shape looks like. There's a
[L2701] [01:37:35.44] lot of little pieces there. Typically
[L2702] [01:37:38.24] nowadays we would have some way of asset
[L2703] [01:37:40.24] streaming, right? The the renderer needs
[L2704] [01:37:42.48] to have things like textures loaded,
[L2705] [01:37:43.92] models loaded, things like that. We need
[L2706] [01:37:45.76] world data, physics, collision models,
[L2707] [01:37:47.36] these sorts of things. they might be too
[L2708] [01:37:49.04] big to fit in memory or we don't want to
[L2709] [01:37:50.48] spend a lot of load time to load them up
[L2710] [01:37:52.56] front. We want to stream them in as
[L2711] [01:37:53.84] they're necessary. So there's typically
[L2712] [01:37:55.20] like this thing that's sitting there
[L2713] [01:37:57.36] constantly grabbing things off of disk,
[L2714] [01:37:59.28] caching things, pulling them in and out
[L2715] [01:38:00.80] of a cache that's being used uh by the
[L2716] [01:38:02.96] renderer, by the physics, so on. So
[L2717] [01:38:04.88] that's another common component that's
[L2718] [01:38:06.96] new, didn't used to be there. Um there's
[L2719] [01:38:10.08] going to be an audio and music system
[L2720] [01:38:11.84] obviously that's in charge of like you
[L2721] [01:38:14.00] know when sounds are triggered in the
[L2722] [01:38:15.76] world ambient sound effects that are
[L2723] [01:38:17.36] happening in the world music that's
[L2724] [01:38:18.64] playing continuity again all of that's
[L2725] [01:38:21.04] interacting with the entity with you
[L2726] [01:38:23.52] know the world state to know which ones
[L2727] [01:38:25.04] of those things are happening the update
[L2728] [01:38:26.72] step which will be triggering things in
[L2729] [01:38:28.16] that sound system and of course this the
[L2730] [01:38:30.00] asset streaming to load what sounds are
[L2731] [01:38:31.92] being played or load the music. So we
[L2732] [01:38:34.00] typically have that and then um you know
[L2733] [01:38:37.04] I'm trying to think not I'm trying not
[L2734] [01:38:38.80] to leave out any major components. In a
[L2735] [01:38:41.12] modern uh context there's often
[L2736] [01:38:43.12] networking. So we want to have a way for
[L2737] [01:38:46.56] multiple of these game clients to
[L2738] [01:38:47.84] communicate with a server. So typically
[L2739] [01:38:49.60] what that means is that world that uh
[L2740] [01:38:51.92] state of the world is now might be
[L2741] [01:38:55.36] provisional. It might be sort of a
[L2742] [01:38:57.68] predicted model of the world that's not
[L2743] [01:39:00.16] the real model of the world. the the
[L2744] [01:39:02.32] simulator is actually the authoritative
[L2745] [01:39:05.04] simulator is actually running on a
[L2746] [01:39:06.88] server somewhere and I am merely
[L2747] [01:39:08.80] communicating with it to find out what
[L2748] [01:39:10.48] the world state is and then because I
[L2749] [01:39:13.44] don't want to wait the late I don't want
[L2750] [01:39:15.92] the latency of like going all the way
[L2751] [01:39:17.92] around I am predicting the motion of
[L2752] [01:39:21.44] things forward in time based on the last
[L2753] [01:39:23.68] information I have right so that's
[L2754] [01:39:25.52] another kind of way that things tie in
[L2755] [01:39:27.76] if you want to start doing things like
[L2756] [01:39:29.20] competitive multiplayer and all these
[L2757] [01:39:30.72] sorts of things Right. That makes a lot
[L2758] [01:39:32.64] of sense because like I I used to play
[L2759] [01:39:34.40] video games and then like these MMO RP,
[L2760] [01:39:38.00] you know, online games and when I start
[L2761] [01:39:41.04] to lag, everyone continues forward.
[L2762] [01:39:43.92] >> Yes.
[L2763] [01:39:44.32] >> And then my internet catches up and then
[L2764] [01:39:46.48] everyone jumps to where they actually
[L2765] [01:39:48.16] supposed to be. Uh, okay. That makes a
[L2766] [01:39:51.12] lot of sense. I pulled some of your top
[L2767] [01:39:53.92] tweets. I thought it might be
[L2768] [01:39:55.20] interesting to kind of discuss.
[L2769] [01:39:57.20] >> I'm sorry. So [laughter]
[L2770] [01:39:59.12] you someone said NASA does not allow
[L2771] [01:40:01.84] recursion in their code. How crazy is
[L2772] [01:40:03.68] that? And then you said not even
[L2773] [01:40:06.00] slightly crazy. And it went really
[L2774] [01:40:08.00] viral. Can you explain why that's not
[L2775] [01:40:10.64] even slightly crazy?
[L2776] [01:40:12.32] >> When you're writing functions in a
[L2777] [01:40:14.96] programming in a procedural programming
[L2778] [01:40:16.32] language like we have uh and that like
[L2779] [01:40:19.44] NASA is probably using,
[L2780] [01:40:22.08] you are able to use the program stack
[L2781] [01:40:25.76] for storage. I mean, that's what it's
[L2782] [01:40:27.60] there for. That's what local variables
[L2783] [01:40:29.20] are. I call a function, I get some
[L2784] [01:40:30.88] storage space on the stack. The compiler
[L2785] [01:40:32.40] did that for me.
[L2786] [01:40:34.64] It also saves the return address. So,
[L2787] [01:40:37.60] when I make a function call, that
[L2788] [01:40:39.44] program stack is keeping track of where
[L2789] [01:40:41.76] in my code I was. So that when the thing
[L2790] [01:40:44.64] that I called is finished, I get back
[L2791] [01:40:46.96] there, not some other point. Right?
[L2792] [01:40:50.24] Neither of those two things are things
[L2793] [01:40:52.00] you couldn't implement yourself. Right?
[L2794] [01:40:54.16] They're both things you could do. You
[L2795] [01:40:55.68] could break the thing up into pieces.
[L2796] [01:40:57.60] You could have ways of remembering what
[L2797] [01:41:00.00] they were like a state machine. You can
[L2798] [01:41:02.08] have your own stack that you push data
[L2799] [01:41:03.68] on and access it. Right?
[L2800] [01:41:06.32] So the only thing recursion really does
[L2801] [01:41:09.04] is it allows you to leverage the fact
[L2802] [01:41:12.80] that someone already wrote that code for
[L2803] [01:41:15.04] you and it may be more convenient to use
[L2804] [01:41:16.96] because it's built into the language.
[L2805] [01:41:18.56] Now there are some things if you really
[L2806] [01:41:19.92] want to get super technical about it.
[L2807] [01:41:21.36] There are some things that happen at a
[L2808] [01:41:24.72] CPU level when functions are called but
[L2809] [01:41:28.48] we can put those aside for now. If you
[L2810] [01:41:29.92] want to talk about them after we totally
[L2811] [01:41:31.04] could. So the reason that I don't think
[L2812] [01:41:32.72] it's crazy to go like we're not going to
[L2813] [01:41:34.00] use recursion to implement an algorithm
[L2814] [01:41:36.80] is because if you're doing that you're
[L2815] [01:41:39.36] kind of just yolo swagging that there's
[L2816] [01:41:41.36] room on the stack for whatever it was
[L2817] [01:41:43.04] that you were doing, right? And you
[L2818] [01:41:45.60] can't even really check unless you're
[L2819] [01:41:47.68] going to do some kind of weird like we
[L2820] [01:41:50.16] could sort of do a thing where we go
[L2821] [01:41:52.56] like okay let's try to determine how
[L2822] [01:41:54.32] many more iterations how many more
[L2823] [01:41:55.92] recursion depths we have before we hit
[L2824] [01:41:58.24] the end of our stack. We can do those
[L2825] [01:42:00.48] calculations but it's like eh like and
[L2826] [01:42:03.28] also if the compiler changed something
[L2827] [01:42:04.64] about the layout it wouldn't be true
[L2828] [01:42:06.00] anymore and so on and so forth. So it's
[L2829] [01:42:08.16] like, so if I'm NASA and I'm like, hey,
[L2830] [01:42:11.76] I don't want my astronauts to crash into
[L2831] [01:42:14.00] the moon. It seems much more logical to
[L2832] [01:42:16.64] say like, don't use recursion. Just
[L2833] [01:42:18.24] figure out whatever this thing was that
[L2834] [01:42:19.68] you're going to do, turn it into a loop,
[L2835] [01:42:21.20] keep a stack, and make a state machine
[L2836] [01:42:23.44] for it. We can reason about that much
[L2837] [01:42:24.88] more clearly. We know exactly how long
[L2838] [01:42:26.16] it's going to take. It doesn't matter
[L2839] [01:42:27.04] what compiler gets. So it work the same
[L2840] [01:42:28.56] way every time, and we'll know the
[L2841] [01:42:31.04] bounds precisely, right? Very sensible
[L2842] [01:42:34.16] to me, right? And again, you assume at
[L2843] [01:42:37.60] NASA that they're not doing it for their
[L2844] [01:42:39.68] health. They're doing it because they
[L2845] [01:42:42.08] have, you know, hard constraints on the
[L2846] [01:42:44.72] problem domain where someone's life is
[L2847] [01:42:46.56] at risk. Um, and at or at a minimum many
[L2848] [01:42:50.96] millions of dollars in equipment is at
[L2849] [01:42:53.12] risk if you screw up. If if you stack
[L2850] [01:42:55.92] fall like if you if you get something
[L2851] [01:42:57.92] where you'd recursed too many times and
[L2852] [01:42:59.68] hit the end of the stack that is not
[L2853] [01:43:02.48] just a uh oh I rebooted the computer or
[L2854] [01:43:05.92] the re or restarted the software right
[L2855] [01:43:07.84] so so I don't know hopefully that makes
[L2856] [01:43:09.92] sense
[L2857] [01:43:11.68] >> Karpathy had this famous tweet that kind
[L2858] [01:43:14.56] of coined the phrase vibe coding
[L2859] [01:43:16.56] >> yes
[L2860] [01:43:17.12] >> and then you said if you thought
[L2861] [01:43:19.28] software was bad today buckle up because
[L2862] [01:43:22.08] it's about to get a whole lot worse.
[L2863] [01:43:24.08] Yes.
[L2864] [01:43:24.80] >> It's been about a year and a half since
[L2865] [01:43:27.52] that tweet came out. The tweet came out
[L2866] [01:43:29.28] February of 2025. Would you say that
[L2867] [01:43:33.04] that was an accurate prediction?
[L2868] [01:43:35.52] To be clear, I think
[L2869] [01:43:39.36] it the whole lot worse part is
[L2870] [01:43:41.52] predicated on something that may not
[L2871] [01:43:44.08] happen and that is that the idea that we
[L2872] [01:43:48.48] just kind of type some stuff into a
[L2873] [01:43:49.76] computer and ship it to prod, right?
[L2874] [01:43:51.52] Basically like, "Hey, could you make me
[L2875] [01:43:53.12] a thing?" and then publish it becomes a
[L2876] [01:43:55.76] common way of doing things, right? For
[L2877] [01:43:58.40] example, also done by people who maybe
[L2878] [01:44:01.20] don't have a computer science
[L2879] [01:44:02.08] background. I think it's fair to say and
[L2880] [01:44:05.44] that I wouldn't be uh being sort of
[L2881] [01:44:08.16] overly dismissive of AI at this point to
[L2882] [01:44:10.88] say that a person who is well-trained in
[L2883] [01:44:14.40] computer science using an AI to make
[L2884] [01:44:16.96] code right now can make substantially
[L2885] [01:44:20.24] better code than someone who doesn't
[L2886] [01:44:21.68] know anything about computer science who
[L2887] [01:44:23.28] is just given you know fable and types
[L2888] [01:44:26.48] some stuff in right the difference is
[L2889] [01:44:29.28] rather dramatic I would say from
[L2890] [01:44:31.04] everything that I've seen
[L2891] [01:44:33.36] So part part of my uh concern that I was
[L2892] [01:44:37.44] trying to express at that tweet was like
[L2893] [01:44:39.68] if the idea is like we're just going to
[L2894] [01:44:41.20] type stuff in and we're not going to
[L2895] [01:44:42.56] really be checking the code, you know,
[L2896] [01:44:44.64] someone who knows computer science is
[L2897] [01:44:46.24] not really going to be looking at it. Um
[L2898] [01:44:48.32] worst case scenario, it's literally just
[L2899] [01:44:49.92] like some random person in marketing
[L2900] [01:44:53.04] somewhere who has no idea what
[L2901] [01:44:54.32] programming is just types in and hits
[L2902] [01:44:56.56] crosses their fingers, right? I think
[L2903] [01:44:58.56] we're in for a world of hurt right now.
[L2904] [01:45:02.08] It's a race. So, it's hard to say
[L2905] [01:45:05.36] because it's basically a race of how
[L2906] [01:45:07.60] good can you make the AI versus how much
[L2907] [01:45:10.64] adoption does it get, right? It's a
[L2908] [01:45:12.24] curve, right? It's like if you can make
[L2909] [01:45:14.08] the AI good enough that the people who
[L2910] [01:45:16.40] are adopting it at a particular rate are
[L2911] [01:45:18.88] always using an AI that's good enough
[L2912] [01:45:20.72] for what they're adopting it for, we
[L2913] [01:45:22.64] wouldn't expect software to get
[L2914] [01:45:23.76] significantly worse. If those curves go
[L2915] [01:45:25.84] the other way, we're in a lot of
[L2916] [01:45:27.60] trouble, right? So, we're I feel like
[L2917] [01:45:28.88] right now we're we're almost kind of
[L2918] [01:45:30.32] teetering on this knife's edge. It's
[L2919] [01:45:32.08] it's really to me it feels like a foot
[L2920] [01:45:34.16] race of like improving AI so it can be
[L2921] [01:45:38.16] more autonomous and make better
[L2922] [01:45:40.00] decisions without your without you
[L2923] [01:45:41.84] needing to make them for it versus the
[L2924] [01:45:45.20] capability level of people who are using
[L2925] [01:45:47.52] it and the degree to which they're
[L2926] [01:45:48.72] paying attention to its output. It's
[L2927] [01:45:50.16] like these two curves that are just like
[L2928] [01:45:51.76] ah, you know, like what's [laughter]
[L2929] [01:45:53.84] what's gonna happen? I don't have a
[L2930] [01:45:56.72] prediction. I don't know where we'll be
[L2931] [01:45:58.48] in a year. Uh obviously for all of our
[L2932] [01:46:01.04] sake, I'm hoping that the AI curve wins.
[L2933] [01:46:04.96] Uh because I agree like I understand
[L2934] [01:46:09.28] certainly the perspective of people who
[L2935] [01:46:12.32] maybe just don't like AI and don't want
[L2936] [01:46:14.40] there to be AI. I can understand the uh
[L2937] [01:46:18.64] wanting it to fail. I I understand that,
[L2938] [01:46:21.36] right? Um and I'm no fan of AI myself,
[L2939] [01:46:25.44] so it's not like I like I'm going to
[L2940] [01:46:27.76] criticize someone for taking that
[L2941] [01:46:29.20] position.
[L2942] [01:46:30.88] But at the end of the day, if you're
[L2943] [01:46:32.48] talking about something that tons of
[L2944] [01:46:33.84] people are using,
[L2945] [01:46:36.00] you're gonna kind of want it to be good.
[L2946] [01:46:38.00] Like I think at this point given the
[L2947] [01:46:40.08] level of adoption of AI, I really don't
[L2948] [01:46:42.80] think it's would be great if it stopped
[L2949] [01:46:45.36] getting any better right now. Like if
[L2950] [01:46:47.44] this was as good as it was going to get,
[L2951] [01:46:48.80] I think that might be bad. Um certainly
[L2952] [01:46:52.16] six months ago, I think that was true.
[L2953] [01:46:55.12] Uh and I think it's probably still true
[L2954] [01:46:56.88] today. So I think ideally if you want
[L2955] [01:47:00.64] software to not be terrible, you have to
[L2956] [01:47:04.00] kind of still be hoping that six months
[L2957] [01:47:05.84] from now the AIs are again significantly
[L2958] [01:47:08.88] better than they were, right? Like that
[L2959] [01:47:10.88] that is the only way out of the current
[L2960] [01:47:13.68] situation as I see it, right? Uh I don't
[L2961] [01:47:17.60] know if that's fair, but that's my
[L2962] [01:47:19.12] that's my sort of feeling on that. One
[L2963] [01:47:21.68] of your other top tweets it was, you
[L2964] [01:47:24.24] know, Shopify put out this internal memo
[L2965] [01:47:27.04] and you just, you know, you replied, you
[L2966] [01:47:29.28] know, slopify. Yes. [laughter]
[L2967] [01:47:30.88] >> So, I guess it's cuz in this tweet, it's
[L2968] [01:47:33.36] leadership pushing the adoption curve
[L2969] [01:47:35.60] maybe harder than the capabilities of
[L2970] [01:47:38.08] the AI in this case.
[L2971] [01:47:39.84] >> Yeah. Uh, although I also just like the
[L2972] [01:47:41.76] bot. One of the things that I think is
[L2973] [01:47:44.24] most unfortunate about the AI adoption
[L2974] [01:47:47.36] as I've seen it is just the because
[L2975] [01:47:52.08] people think that it's going to be this
[L2976] [01:47:54.96] major um I guess if I had to categorize
[L2977] [01:47:57.92] the way it appears that companies are
[L2978] [01:47:59.68] reasoning about it. They're assuming
[L2979] [01:48:01.52] that if they don't get in early, it will
[L2980] [01:48:03.76] be a big disaster for them, right? like
[L2981] [01:48:06.00] like there's a tremendous like they
[L2982] [01:48:08.00] don't just think oh well we can just
[L2983] [01:48:09.68] wait until the AI does what we need it
[L2984] [01:48:11.36] to do and then start using it. They're
[L2985] [01:48:12.72] like, "No, we have to do it now." Like
[L2986] [01:48:14.64] even before we know whether it can
[L2987] [01:48:16.32] really do the thing that we want it to
[L2988] [01:48:17.44] do or whether we know whether the
[L2989] [01:48:18.48] outcomes will be good, everyone has to
[L2990] [01:48:20.08] do it right now. Let's do this. Right.
[L2991] [01:48:22.32] Um and I understand why they want why
