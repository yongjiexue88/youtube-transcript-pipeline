Chunk 9; segments 2969–3341. Start may repeat the previous chunk for context.

# Dropbox’s Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling

Source ID: source-dbce948925112d65
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Dropbox’s_Former_Most_Senior_Eng_Building_Great_Systems_and_Advice_for_the_AI_Era_James_Cowling_en.txt
Video: https://www.youtube.com/watch?v=3XkmNSuHFmY

[L2978] [01:38:45.84] client sees is a consistent view of
[L2979] [01:38:47.80] what's on the on the server.
[L2980] [01:38:50.24] And I would say Convex is a very
[L2981] [01:38:51.92] designed platform cuz Convex is designed
[L2982] [01:38:54.28] to be very composable and fit together
[L2983] [01:38:55.80] well.
[L2984] [01:38:56.64] And so, we designed Convex for
[L2985] [01:38:58.32] developers to use. In particular, we
[L2986] [01:39:00.04] wanted to make it so that application
[L2987] [01:39:02.16] developers were able to build complex
[L2988] [01:39:04.16] full-stack applications. That was the
[L2989] [01:39:06.04] goal of Convex. Now, all of a sudden,
[L2990] [01:39:08.56] agentic development came along.
[L2991] [01:39:10.44] And that's been really interesting for
[L2992] [01:39:12.20] us because it turns out
[L2993] [01:39:14.40] that um,
[L2994] [01:39:15.72] what humans find hard is also what
[L2995] [01:39:18.08] agents find hard. You know,
[L2996] [01:39:20.28] you know, the coding agents are not
[L2997] [01:39:21.84] particularly good with large
[L2998] [01:39:24.16] code bases, they're not particularly
[L2999] [01:39:25.52] good with um, reasoning about um, action
[L3000] [01:39:28.56] at a distance, you know, race conditions
[L3001] [01:39:30.84] across services, they're not
[L3002] [01:39:32.48] particularly good at simple
[L3003] [01:39:34.56] architectures over time. And these are
[L3004] [01:39:36.36] the things that Convex gives you as a
[L3005] [01:39:38.00] developer. So, the idea now, and and
[L3006] [01:39:39.92] almost everyone using Convex is using
[L3007] [01:39:41.64] Convex because they have their coding
[L3008] [01:39:43.40] agent doing their front end, but they
[L3009] [01:39:45.44] need
[L3010] [01:39:46.60] a back end abstraction, a higher level
[L3011] [01:39:48.88] abstraction than something like AWS or
[L3012] [01:39:50.80] something like hosted Postgres, which
[L3013] [01:39:52.68] makes their problems go away. And that's
[L3014] [01:39:54.32] that's the company.
[L3015] [01:39:55.64] >> That was one thing I wanted to ask cuz
[L3016] [01:39:57.36] immediately when I think, oh, I just
[L3017] [01:39:58.48] need a back end or something like that,
[L3018] [01:39:59.88] just go to AWS or, you know, just host
[L3019] [01:40:02.52] something like that. So, this is the
[L3020] [01:40:04.72] layer of abstraction on kind of on top
[L3021] [01:40:06.88] of those types of primitives
[L3022] [01:40:08.36] >> Yes.
[L3023] [01:40:08.76] >> that makes it easier for an application
[L3024] [01:40:10.68] developer.
[L3025] [01:40:11.28] >> It ties into a lot of the stuff I I said
[L3026] [01:40:13.68] earlier about making problems go away.
[L3027] [01:40:15.56] And frankly, I mean, I I watched the
[L3028] [01:40:17.44] interview you did with Barbara Liskov,
[L3029] [01:40:18.88] and Barbara was my advisor in grad
[L3030] [01:40:20.60] school, and and I we worked a lot
[L3031] [01:40:22.64] together and a lot on abstraction, and
[L3032] [01:40:25.28] you know, the value in clean designs
[L3033] [01:40:27.52] that minimize complexity. And so, AWS is
[L3034] [01:40:30.40] a fine tool.
[L3035] [01:40:32.16] Postgres is a fine tool.
[L3036] [01:40:34.36] Although, none of the mainstream
[L3037] [01:40:35.20] databases are that great, frankly. But
[L3038] [01:40:37.32] um
[L3039] [01:40:37.92] they're fine tools, but they're not
[L3040] [01:40:39.56] they're not making problems go away,
[L3041] [01:40:41.32] right? And so, the idea of Convex is a
[L3042] [01:40:43.28] higher level set of abstractions that
[L3043] [01:40:45.48] you can use and not reason about state
[L3044] [01:40:47.76] management, not reason about
[L3045] [01:40:49.44] concurrency, not reason about
[L3046] [01:40:50.56] scheduling, not reason about
[L3047] [01:40:52.24] transactions, uh not reason about
[L3048] [01:40:54.40] polling and data sync and type safety
[L3049] [01:40:56.92] and all those things. So, Convex is a If
[L3050] [01:40:59.64] If you think about, you know, the
[L3051] [01:41:00.72] history of of engineering, over time the
[L3052] [01:41:03.24] abstraction floor raises. You know, when
[L3053] [01:41:05.24] Barbara was first starting,
[L3054] [01:41:07.64] she was using punch cards, you know? Um
[L3055] [01:41:10.40] I don't I don't know if she mentioned it
[L3056] [01:41:11.44] to you, but
[L3057] [01:41:12.40] uh when she started as a programmer, she
[L3058] [01:41:14.32] never heard the word programmer before,
[L3059] [01:41:16.16] you know?
[L3060] [01:41:16.92] Uh that was the first time she heard the
[L3061] [01:41:18.56] word, right? And then you you went from
[L3062] [01:41:20.76] punch cards to like, you know, having
[L3063] [01:41:23.04] proper operating systems and and and uh
[L3064] [01:41:26.04] you know, then you know,
[L3065] [01:41:27.64] languages like C and then higher level
[L3066] [01:41:29.00] languages and and then you had cloud
[L3067] [01:41:30.88] computing. And over time the abstraction
[L3068] [01:41:32.96] floor raises, and you largely forget
[L3069] [01:41:35.20] about what's going on beneath the
[L3070] [01:41:36.40] surfaces. Most people don't think about
[L3071] [01:41:38.36] how S3 is implemented. I do, but that's
[L3072] [01:41:40.68] what I used to work on. But like most
[L3073] [01:41:42.44] people just use it and it just stores
[L3074] [01:41:44.00] your data and it gives it back and
[L3075] [01:41:45.00] that's great.
[L3076] [01:41:46.56] That's a successful abstraction. But I
[L3077] [01:41:48.40] do strongly believe that the world
[L3078] [01:41:50.60] is and has been overdue for a new
[L3079] [01:41:52.56] abstraction. A one level up the stack.
[L3080] [01:41:55.48] And especially now that people are doing
[L3081] [01:41:57.12] agent development, largely they don't
[L3082] [01:41:59.16] want to own a Postgres instance. Largely
[L3083] [01:42:00.88] they don't want to think about Kafka
[L3084] [01:42:02.44] versus RabbitMQ. Uh they don't want to
[L3085] [01:42:04.48] think about, you know, what set of tools
[L3086] [01:42:05.96] to use. They want it just to work so
[L3087] [01:42:08.84] they can focus on building their
[L3088] [01:42:09.80] application.
[L3089] [01:42:11.28] >> When you talk about, you know, the
[L3090] [01:42:13.00] abstraction, there's obviously a lot of
[L3091] [01:42:14.68] stuff going on behind the scenes in
[L3092] [01:42:17.00] Convex and the the technical side. And
[L3093] [01:42:20.68] I, you know, what what is it that Convex
[L3094] [01:42:23.24] is building behind the scenes that
[L3095] [01:42:25.44] you're most excited about and why?
[L3096] [01:42:27.60] >> Basically, Convex is a new
[L3097] [01:42:30.80] operating system in some respects,
[L3098] [01:42:33.20] right? So we have the primitives,
[L3099] [01:42:34.64] queries, mutations, actions,
[L3100] [01:42:36.68] subscriptions.
[L3101] [01:42:38.32] What I think is kind of cool is how we
[L3102] [01:42:39.80] built this, you know? We have our own
[L3103] [01:42:41.40] database that we built. We have our own
[L3104] [01:42:42.88] distributed database that, you know,
[L3105] [01:42:44.72] does, you know, tracks read ranges and
[L3106] [01:42:46.76] write ranges and does very efficient um
[L3107] [01:42:49.88] subscriptions over web sockets, etc. So
[L3108] [01:42:52.28] that's that's the current operating
[L3109] [01:42:54.68] system set of primitives.
[L3110] [01:42:56.96] But um
[L3111] [01:42:58.52] Convex is getting much larger workloads
[L3112] [01:43:00.84] now and much more interesting workloads
[L3113] [01:43:02.32] and more high-performance workloads. And
[L3114] [01:43:04.52] so we're in the process of developing a
[L3115] [01:43:07.00] slightly lower-level API
[L3116] [01:43:09.68] for doing very efficient kind of
[L3117] [01:43:11.52] background processes, singletons,
[L3118] [01:43:13.92] APIs like fork, like you, you know, in
[L3119] [01:43:16.28] like operating system primitives. And
[L3120] [01:43:18.08] I'm pretty excited about launching these
[L3121] [01:43:21.72] and how much is faster it's going to
[L3122] [01:43:23.52] make various um Convex components like
[L3123] [01:43:25.72] the workflow system. Um
[L3124] [01:43:28.72] And to be honest, the thing I find
[L3125] [01:43:30.20] exciting every day,
[L3126] [01:43:31.96] challenging every day. I I still find
[L3127] [01:43:33.76] Convex very hard. Like
[L3128] [01:43:36.16] to be honest, like
[L3129] [01:43:37.72] I struggle every day.
[L3130] [01:43:39.76] Um I don't find my job easy. I I mean I
[L3131] [01:43:42.24] I
[L3132] [01:43:42.88] I feel confident in my job, but it's not
[L3133] [01:43:44.92] easy. Like designing the new API for
[L3134] [01:43:47.08] this is super hard. I can't just go ask
[L3135] [01:43:49.12] ChatGPT. It's not going to give a good
[L3136] [01:43:50.44] answer, right? And um cuz it's
[L3137] [01:43:53.52] innovation. It's a It's a new ideas. I
[L3138] [01:43:55.72] really enjoy it. I find it um stressful
[L3139] [01:43:58.44] sometimes. I find it um
[L3140] [01:44:01.24] challenging and tiring, but I also find
[L3141] [01:44:04.40] it exciting. And and and I would I you
[L3142] [01:44:06.36] know, I would encourage engineers to try
[L3143] [01:44:07.76] to find this kind of stuff to work on
[L3144] [01:44:09.52] where it's like you're on that edge of
[L3145] [01:44:11.56] like I'm really liking this, but also
[L3146] [01:44:14.00] it's a bit tricky, you know, it's it's a
[L3147] [01:44:15.40] bit tough.
[L3148] [01:44:16.60] >> You mentioned fork and in operating
[L3149] [01:44:18.72] systems I'm familiar, you know, you just
[L3150] [01:44:21.16] take the existing process and kind of
[L3151] [01:44:22.96] split it. What's the idea of fork in a
[L3152] [01:44:26.28] distributed system?
[L3153] [01:44:27.96] >> So, Convex almost never has scale issues
[L3154] [01:44:30.80] with regards to live traffic. You know,
[L3155] [01:44:32.44] live traffic is like um
[L3156] [01:44:34.72] typically bound by user-facing
[L3157] [01:44:36.36] interactions, people clicking on stuff,
[L3158] [01:44:37.84] running website, you know, acting on
[L3159] [01:44:39.16] website. Every now and then someone will
[L3160] [01:44:41.48] come to Convex and want to kick off a
[L3161] [01:44:42.96] million background jobs to do something,
[L3162] [01:44:44.88] background processing.
[L3163] [01:44:46.44] It's a big workload. You
[L3164] [01:44:47.32] programmatically you can trigger huge
[L3165] [01:44:49.36] workloads, right? And so the one of
[L3166] [01:44:51.08] things we have to scale is is kind of
[L3167] [01:44:52.72] these background workloads and a lot of
[L3168] [01:44:54.68] them involve things like scheduling.
[L3169] [01:44:57.24] And there are a lot of workloads in
[L3170] [01:44:58.44] Convex that would be um
[L3171] [01:45:01.08] very efficient if you had a background
[L3172] [01:45:03.32] singleton process to perform things like
[L3173] [01:45:06.16] aggregates, you know, um
[L3174] [01:45:09.08] I'll give a very silly example, right?
[L3175] [01:45:11.44] If you have a let's say you're building
[L3176] [01:45:13.80] an election on Convex, a voting system,
[L3177] [01:45:16.40] and every vote is a new uh row in the in
[L3178] [01:45:19.16] the table and you want to show a tally
[L3179] [01:45:20.88] of the votes.
[L3180] [01:45:22.12] You know, one way of doing this is
[L3181] [01:45:23.56] having a bunch of background processes
[L3182] [01:45:24.84] or crons adding these things up.
[L3183] [01:45:26.92] One way is doing a table scan, which is
[L3184] [01:45:29.16] you know, the obvious way to use
[L3185] [01:45:30.20] Postgres, which doesn't scale. The other
[L3186] [01:45:32.40] is to have a background job, which if
[L3187] [01:45:34.76] there's new votes, it adds them all up,
[L3188] [01:45:37.20] keeps a tally. If there's no new votes,
[L3189] [01:45:38.96] it goes to sleep and waits on like a
[L3190] [01:45:41.16] condition variable to wake up up to wake
[L3191] [01:45:43.40] up again when there's with a new job to
[L3192] [01:45:44.72] perform. And so these are the kind of
[L3193] [01:45:46.40] primitives
[L3194] [01:45:47.64] that we're working on right now. Most
[L3195] [01:45:49.16] people won't even know they exist, but
[L3196] [01:45:50.96] allow us to build these very
[L3197] [01:45:52.08] high-performance um primitives for
[L3198] [01:45:54.44] scheduling
[L3199] [01:45:56.16] um aggregates, you know, background
[L3200] [01:45:59.04] aggregations, etc. Um and I'm pretty
[L3201] [01:46:01.48] excited about like the the next
[L3202] [01:46:03.68] generation of workloads we can support
[L3203] [01:46:05.12] as a result.
[L3204] [01:46:06.44] >> When you reflect on your career and you
[L3205] [01:46:09.08] it sounds like you've done a lot of
[L3206] [01:46:10.36] gnarly technical work across your PhD,
[L3207] [01:46:13.80] ca- Dropbox seemed like pretty intense
[L3208] [01:46:16.04] systems work, and Convex is also doing a
[L3209] [01:46:19.00] lot of cool stuff. When you look back on
[L3210] [01:46:20.84] your career, what was the most
[L3211] [01:46:22.40] technically stimulating work you've ever
[L3212] [01:46:24.56] done? And you know, why was it hard and
[L3213] [01:46:27.52] what did you learn from it?
[L3214] [01:46:29.36] >> There was certainly times in grad school
[L3215] [01:46:30.76] where we were like um formally mo-
[L3216] [01:46:32.92] modeling consensus protocols and stuff
[L3217] [01:46:34.92] and you know, I'd be on the phone with
[L3218] [01:46:36.44] Barbara on weekends and talking through
[L3219] [01:46:38.92] um trying to reason about this in our
[L3220] [01:46:40.64] heads. That was pretty intellectually
[L3221] [01:46:41.84] stimulating and fun, but I think the
[L3222] [01:46:43.68] stuff I found most stimulating was stuff
[L3223] [01:46:46.32] like working on very large storage
[L3224] [01:46:49.60] system with a team where
[L3225] [01:46:52.16] you know, things are going wrong. You
[L3226] [01:46:53.84] know, where where the rubber hits the
[L3227] [01:46:55.36] road, that's where I find And this is
[L3228] [01:46:57.44] everyday at Convex. You know, the rubber
[L3229] [01:46:59.32] hits the road like you know, uh hey, we
[L3230] [01:47:00.52] have a uh compaction process that runs
[L3231] [01:47:02.48] in the background, but it's running into
[L3232] [01:47:04.08] issues. We might have to redesign it
[L3233] [01:47:05.56] using
[L3234] [01:47:06.56] partitioning, etc.
[L3235] [01:47:09.44] I I feel most intellectually stimulated
[L3236] [01:47:11.72] where where there's a really clear
[L3237] [01:47:14.44] constraint in front of me.
[L3238] [01:47:16.56] And um that to me is engineering. Like
[L3239] [01:47:19.12] if
[L3240] [01:47:20.36] I I actually know what the definition of
[L3241] [01:47:21.52] engineering is, but I'm just going to
[L3242] [01:47:23.40] make it up in my mind, engineering is
[L3243] [01:47:26.20] science with constraints. It's like It's
[L3244] [01:47:28.36] like how to How do you
[L3245] [01:47:31.52] solve problems in the presence of
[L3246] [01:47:33.36] resource constraints?
[L3247] [01:47:35.04] I'm not particularly interested in
[L3248] [01:47:36.44] constraint-free environments. That's
[L3249] [01:47:38.36] art.
[L3250] [01:47:39.32] I like craft and engineering. And the
[L3251] [01:47:43.08] the more visceral and difficult the
[L3252] [01:47:45.00] constraints, the more fun that is for
[L3253] [01:47:46.56] me.
[L3254] [01:47:47.96] And I I've I've been lucky enough to
[L3255] [01:47:50.96] I don't know whether it's luck or
[L3256] [01:47:53.24] intention, I don't know, but I I I've
[L3257] [01:47:55.08] always placed myself in those
[L3258] [01:47:57.28] environments, you know, like
[L3259] [01:48:00.80] let's go get on the hardest team and and
[L3260] [01:48:03.24] own the hardest problem and then
[L3261] [01:48:05.20] um and then, you know, put the effort
[L3262] [01:48:07.00] into to to survive.
[L3263] [01:48:10.20] >> This question might be a little bit off
[L3264] [01:48:11.80] topic, but you know, I know you were a
[L3265] [01:48:14.40] consultant for the show the TV show
[L3266] [01:48:16.80] Silicon Valley.
[L3267] [01:48:18.28] I love that show and I got to hear how'd
[L3268] [01:48:20.56] you get involved in that?
[L3269] [01:48:21.88] >> Yeah, that was a lot of fun. So, um
[L3270] [01:48:25.20] a lot of folks might not know this. Um
[L3271] [01:48:28.24] I had nothing to do with season 1. So, a
[L3272] [01:48:29.92] lot of TV shows, they don't know whether
[L3273] [01:48:31.40] they're going to survive as a TV show.
[L3274] [01:48:33.56] So, so, um Mike Judge who started um who
[L3275] [01:48:37.40] who who wrote Silicon Valley also was of
[L3276] [01:48:39.64] Beavis and Butt-Head and Office Space
[L3277] [01:48:41.24] fame. He started his career as a
[L3278] [01:48:43.12] software engineer at I think Lockheed or
[L3279] [01:48:45.04] something. So, he actually was a
[L3280] [01:48:46.48] software engineer that a lot of people
[L3281] [01:48:48.12] don't realize. And so, Silicon Valley
[L3282] [01:48:50.20] was like a throwback to the kind of
[L3283] [01:48:52.56] work he did. And if you anyone's seen
[L3284] [01:48:53.76] the movie Office Space, you would you
[L3285] [01:48:55.20] would get this. It's That's a really a
[L3286] [01:48:57.04] you know, dystopian cubicle era uh tech
[L3287] [01:48:59.88] uh industry um film.
[L3288] [01:49:01.48] Um so, they did season 1 of of Silicon
[L3289] [01:49:04.44] Valley and then it was very popular and
[L3290] [01:49:06.92] they got picked up and so, they had to
[L3291] [01:49:08.32] figure out what to do for season 2, but
[L3292] [01:49:09.80] they didn't know what to do because they
[L3293] [01:49:11.76] did they'd written a storyline that gets
[L3294] [01:49:13.84] to the point where there's a compression
[L3295] [01:49:15.16] algorithm. And And then what happens?
[L3296] [01:49:18.16] And so they needed to find um
[L3297] [01:49:21.68] an expert on compression and I guess
[L3298] [01:49:24.48] ostensibly that was me. And I don't know
[L3299] [01:49:26.16] whether I was an expert on compression.
[L3300] [01:49:27.64] I guess I was an expert on storage at
[L3301] [01:49:28.92] least. And so and so they came to the
[L3302] [01:49:31.64] office and and uh and we just chat
[L3303] [01:49:34.76] chatted and it was so much fun, you
[L3304] [01:49:36.24] know? And so I was involved in um you're
[L3305] [01:49:38.88] pretty heavily involved in the show. Um
[L3306] [01:49:42.24] A lot of it was you know storyline and
[L3307] [01:49:44.64] and so forth. So like yes, sure, what
[L3308] [01:49:45.76] would you do with the compression
[L3309] [01:49:46.80] algorithm? What would could you design a
[L3310] [01:49:48.04] storage system? And and so coming up
[L3311] [01:49:49.48] with story ideas that that technically
[L3312] [01:49:51.80] accurate. They were really
[L3313] [01:49:54.80] you'd be surprised to know how much they
[L3314] [01:49:56.64] care about accuracy. A lot of um
[L3315] [01:49:59.48] people I know can't watch that show cuz
[L3316] [01:50:01.60] it's just so creepily [snorts]
[L3317] [01:50:04.04] accurate. They find it so cringey. And
[L3318] [01:50:06.20] partly why Silicon Valley can this TV
[L3319] [01:50:08.52] show could be so cringey is because
[L3320] [01:50:11.52] it's it's real. Like those stories are
[L3321] [01:50:14.12] almost almost
[L3322] [01:50:16.24] I don't know everyone. So many of the
[L3323] [01:50:17.96] stories in Silicon Valley are just real
[L3324] [01:50:19.40] stories. They're just they went to a
[L3325] [01:50:21.36] bunch of companies just farmed everyone
[L3326] [01:50:24.12] for like stories of crazy things that
[L3327] [01:50:26.60] happened in the tech industry and they
[L3328] [01:50:28.16] wove them into the series. And all the
[L3329] [01:50:30.20] characters are based on real people and
[L3330] [01:50:32.52] and real archetypes. Um but they also
[L3331] [01:50:34.60] cared very much about technical
[L3332] [01:50:35.68] accuracy. So I would also do technical
[L3333] [01:50:37.20] consulting and then they'd say stuff
[L3334] [01:50:38.40] like oh we're
[L3335] [01:50:40.08] building a data center in our house.
[L3336] [01:50:41.36] What should the rack look like? And you
[L3337] [01:50:43.84] know, what should the
[L3338] [01:50:45.20] diagram on the wall look like? And and
[L3339] [01:50:47.20] partly, you know, I wanted to be like oh
[L3340] [01:50:49.12] well it doesn't really matter. No one's
[L3341] [01:50:50.36] going to care. And they're like no, no,
[L3342] [01:50:51.68] no, it matters. Like they really cared
[L3343] [01:50:54.16] to get it right. Um
[L3344] [01:50:56.20] So yeah, I love the show, but it it can
[L3345] [01:50:58.44] be hard to watch just because of
[L3346] [01:51:00.56] oh my god, how how
[L3347] [01:51:03.04] real it can feel.
[L3348] [01:51:05.00] >> Are there any Easter eggs where you look
[L3349] [01:51:08.12] at it and go that's unusually accurate
[L3350] [01:51:10.24] or or you know, that system diagram
