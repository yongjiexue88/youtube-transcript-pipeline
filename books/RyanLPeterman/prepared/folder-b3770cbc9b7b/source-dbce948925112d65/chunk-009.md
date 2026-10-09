Chunk 9; segments 2969–3297. Start may repeat the previous chunk for context.

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
[L3019] [100:02.52] something like that. So, this is the
[L3020] [100:04.72] layer of abstraction on kind of on top
[L3021] [100:06.88] of those types of primitives
[L3022] [100:08.36] >> Yes.
[L3023] [100:08.76] >> that makes it easier for an application
[L3024] [100:10.68] developer.
[L3025] [100:11.28] >> It ties into a lot of the stuff I I said
[L3026] [100:13.68] earlier about making problems go away.
[L3027] [100:15.56] And frankly, I mean, I I watched the
[L3028] [100:17.44] interview you did with Barbara Liskov,
[L3029] [100:18.88] and Barbara was my advisor in grad
[L3030] [100:20.60] school, and and I we worked a lot
[L3031] [100:22.64] together and a lot on abstraction, and
[L3032] [100:25.28] you know, the value in clean designs
[L3033] [100:27.52] that minimize complexity. And so, AWS is
[L3034] [100:30.40] a fine tool.
[L3035] [100:32.16] Postgres is a fine tool.
[L3036] [100:34.36] Although, none of the mainstream
[L3037] [100:35.20] databases are that great, frankly. But
[L3038] [100:37.32] um
[L3039] [100:37.92] they're fine tools, but they're not
[L3040] [100:39.56] they're not making problems go away,
[L3041] [100:41.32] right? And so, the idea of Convex is a
[L3042] [100:43.28] higher level set of abstractions that
[L3043] [100:45.48] you can use and not reason about state
[L3044] [100:47.76] management, not reason about
[L3045] [100:49.44] concurrency, not reason about
[L3046] [100:50.56] scheduling, not reason about
[L3047] [100:52.24] transactions, uh not reason about
[L3048] [100:54.40] polling and data sync and type safety
[L3049] [100:56.92] and all those things. So, Convex is a If
[L3050] [100:59.64] If you think about, you know, the
[L3051] [101:00.72] history of of engineering, over time the
[L3052] [101:03.24] abstraction floor raises. You know, when
[L3053] [101:05.24] Barbara was first starting,
[L3054] [101:07.64] she was using punch cards, you know? Um
[L3055] [101:10.40] I don't I don't know if she mentioned it
[L3056] [101:11.44] to you, but
[L3057] [101:12.40] uh when she started as a programmer, she
[L3058] [101:14.32] never heard the word programmer before,
[L3059] [101:16.16] you know?
[L3060] [101:16.92] Uh that was the first time she heard the
[L3061] [101:18.56] word, right? And then you you went from
[L3062] [101:20.76] punch cards to like, you know, having
[L3063] [101:23.04] proper operating systems and and and uh
[L3064] [101:26.04] you know, then you know,
[L3065] [101:27.64] languages like C and then higher level
[L3066] [101:29.00] languages and and then you had cloud
[L3067] [101:30.88] computing. And over time the abstraction
[L3068] [101:32.96] floor raises, and you largely forget
[L3069] [101:35.20] about what's going on beneath the
[L3070] [101:36.40] surfaces. Most people don't think about
[L3071] [101:38.36] how S3 is implemented. I do, but that's
[L3072] [101:40.68] what I used to work on. But like most
[L3073] [101:42.44] people just use it and it just stores
[L3074] [101:44.00] your data and it gives it back and
[L3075] [101:45.00] that's great.
[L3076] [101:46.56] That's a successful abstraction. But I
[L3077] [101:48.40] do strongly believe that the world
[L3078] [101:50.60] is and has been overdue for a new
[L3079] [101:52.56] abstraction. A one level up the stack.
[L3080] [101:55.48] And especially now that people are doing
[L3081] [101:57.12] agent development, largely they don't
[L3082] [101:59.16] want to own a Postgres instance. Largely
[L3083] [102:00.88] they don't want to think about Kafka
[L3084] [102:02.44] versus RabbitMQ. Uh they don't want to
[L3085] [102:04.48] think about, you know, what set of tools
[L3086] [102:05.96] to use. They want it just to work so
[L3087] [102:08.84] they can focus on building their
[L3088] [102:09.80] application.
[L3089] [102:11.28] >> When you talk about, you know, the
[L3090] [102:13.00] abstraction, there's obviously a lot of
[L3091] [102:14.68] stuff going on behind the scenes in
[L3092] [102:17.00] Convex and the the technical side. And
[L3093] [102:20.68] I, you know, what what is it that Convex
[L3094] [102:23.24] is building behind the scenes that
[L3095] [102:25.44] you're most excited about and why?
[L3096] [102:27.60] >> Basically, Convex is a new
[L3097] [102:30.80] operating system in some respects,
[L3098] [102:33.20] right? So we have the primitives,
[L3099] [102:34.64] queries, mutations, actions,
[L3100] [102:36.68] subscriptions.
[L3101] [102:38.32] What I think is kind of cool is how we
[L3102] [102:39.80] built this, you know? We have our own
[L3103] [102:41.40] database that we built. We have our own
[L3104] [102:42.88] distributed database that, you know,
[L3105] [102:44.72] does, you know, tracks read ranges and
[L3106] [102:46.76] write ranges and does very efficient um
[L3107] [102:49.88] subscriptions over web sockets, etc. So
[L3108] [102:52.28] that's that's the current operating
[L3109] [102:54.68] system set of primitives.
[L3110] [102:56.96] But um
[L3111] [102:58.52] Convex is getting much larger workloads
[L3112] [103:00.84] now and much more interesting workloads
[L3113] [103:02.32] and more high-performance workloads. And
[L3114] [103:04.52] so we're in the process of developing a
[L3115] [103:07.00] slightly lower-level API
[L3116] [103:09.68] for doing very efficient kind of
[L3117] [103:11.52] background processes, singletons,
[L3118] [103:13.92] APIs like fork, like you, you know, in
[L3119] [103:16.28] like operating system primitives. And
[L3120] [103:18.08] I'm pretty excited about launching these
[L3121] [103:21.72] and how much is faster it's going to
[L3122] [103:23.52] make various um Convex components like
[L3123] [103:25.72] the workflow system. Um
[L3124] [103:28.72] And to be honest, the thing I find
[L3125] [103:30.20] exciting every day,
[L3126] [103:31.96] challenging every day. I I still find
[L3127] [103:33.76] Convex very hard. Like
[L3128] [103:36.16] to be honest, like
[L3129] [103:37.72] I struggle every day.
[L3130] [103:39.76] Um I don't find my job easy. I I mean I
[L3131] [103:42.24] I
[L3132] [103:42.88] I feel confident in my job, but it's not
[L3133] [103:44.92] easy. Like designing the new API for
[L3134] [103:47.08] this is super hard. I can't just go ask
[L3135] [103:49.12] ChatGPT. It's not going to give a good
[L3136] [103:50.44] answer, right? And um cuz it's
[L3137] [103:53.52] innovation. It's a It's a new ideas. I
[L3138] [103:55.72] really enjoy it. I find it um stressful
[L3139] [103:58.44] sometimes. I find it um
[L3140] [104:01.24] challenging and tiring, but I also find
[L3141] [104:04.40] it exciting. And and and I would I you
[L3142] [104:06.36] know, I would encourage engineers to try
[L3143] [104:07.76] to find this kind of stuff to work on
[L3144] [104:09.52] where it's like you're on that edge of
[L3145] [104:11.56] like I'm really liking this, but also
[L3146] [104:14.00] it's a bit tricky, you know, it's it's a
[L3147] [104:15.40] bit tough.
[L3148] [104:16.60] >> You mentioned fork and in operating
[L3149] [104:18.72] systems I'm familiar, you know, you just
[L3150] [104:21.16] take the existing process and kind of
[L3151] [104:22.96] split it. What's the idea of fork in a
[L3152] [104:26.28] distributed system?
[L3153] [104:27.96] >> So, Convex almost never has scale issues
[L3154] [104:30.80] with regards to live traffic. You know,
[L3155] [104:32.44] live traffic is like um
[L3156] [104:34.72] typically bound by user-facing
[L3157] [104:36.36] interactions, people clicking on stuff,
[L3158] [104:37.84] running website, you know, acting on
[L3159] [104:39.16] website. Every now and then someone will
[L3160] [104:41.48] come to Convex and want to kick off a
[L3161] [104:42.96] million background jobs to do something,
[L3162] [104:44.88] background processing.
[L3163] [104:46.44] It's a big workload. You
[L3164] [104:47.32] programmatically you can trigger huge
[L3165] [104:49.36] workloads, right? And so the one of
[L3166] [104:51.08] things we have to scale is is kind of
[L3167] [104:52.72] these background workloads and a lot of
[L3168] [104:54.68] them involve things like scheduling.
[L3169] [104:57.24] And there are a lot of workloads in
[L3170] [104:58.44] Convex that would be um
[L3171] [105:01.08] very efficient if you had a background
[L3172] [105:03.32] singleton process to perform things like
[L3173] [105:06.16] aggregates, you know, um
[L3174] [105:09.08] I'll give a very silly example, right?
[L3175] [105:11.44] If you have a let's say you're building
[L3176] [105:13.80] an election on Convex, a voting system,
[L3177] [105:16.40] and every vote is a new uh row in the in
[L3178] [105:19.16] the table and you want to show a tally
[L3179] [105:20.88] of the votes.
[L3180] [105:22.12] You know, one way of doing this is
[L3181] [105:23.56] having a bunch of background processes
[L3182] [105:24.84] or crons adding these things up.
[L3183] [105:26.92] One way is doing a table scan, which is
[L3184] [105:29.16] you know, the obvious way to use
[L3185] [105:30.20] Postgres, which doesn't scale. The other
[L3186] [105:32.40] is to have a background job, which if
[L3187] [105:34.76] there's new votes, it adds them all up,
[L3188] [105:37.20] keeps a tally. If there's no new votes,
[L3189] [105:38.96] it goes to sleep and waits on like a
[L3190] [105:41.16] condition variable to wake up up to wake
[L3191] [105:43.40] up again when there's with a new job to
[L3192] [105:44.72] perform. And so these are the kind of
[L3193] [105:46.40] primitives
[L3194] [105:47.64] that we're working on right now. Most
[L3195] [105:49.16] people won't even know they exist, but
[L3196] [105:50.96] allow us to build these very
[L3197] [105:52.08] high-performance um primitives for
[L3198] [105:54.44] scheduling
[L3199] [105:56.16] um aggregates, you know, background
[L3200] [105:59.04] aggregations, etc. Um and I'm pretty
[L3201] [106:01.48] excited about like the the next
[L3202] [106:03.68] generation of workloads we can support
[L3203] [106:05.12] as a result.
[L3204] [106:06.44] >> When you reflect on your career and you
[L3205] [106:09.08] it sounds like you've done a lot of
[L3206] [106:10.36] gnarly technical work across your PhD,
[L3207] [106:13.80] ca- Dropbox seemed like pretty intense
[L3208] [106:16.04] systems work, and Convex is also doing a
[L3209] [106:19.00] lot of cool stuff. When you look back on
[L3210] [106:20.84] your career, what was the most
[L3211] [106:22.40] technically stimulating work you've ever
[L3212] [106:24.56] done? And you know, why was it hard and
[L3213] [106:27.52] what did you learn from it?
[L3214] [106:29.36] >> There was certainly times in grad school
[L3215] [106:30.76] where we were like um formally mo-
[L3216] [106:32.92] modeling consensus protocols and stuff
[L3217] [106:34.92] and you know, I'd be on the phone with
[L3218] [106:36.44] Barbara on weekends and talking through
[L3219] [106:38.92] um trying to reason about this in our
[L3220] [106:40.64] heads. That was pretty intellectually
[L3221] [106:41.84] stimulating and fun, but I think the
[L3222] [106:43.68] stuff I found most stimulating was stuff
[L3223] [106:46.32] like working on very large storage
[L3224] [106:49.60] system with a team where
[L3225] [106:52.16] you know, things are going wrong. You
[L3226] [106:53.84] know, where where the rubber hits the
[L3227] [106:55.36] road, that's where I find And this is
[L3228] [106:57.44] everyday at Convex. You know, the rubber
[L3229] [106:59.32] hits the road like you know, uh hey, we
[L3230] [107:00.52] have a uh compaction process that runs
[L3231] [107:02.48] in the background, but it's running into
[L3232] [107:04.08] issues. We might have to redesign it
[L3233] [107:05.56] using
[L3234] [107:06.56] partitioning, etc.
[L3235] [107:09.44] I I feel most intellectually stimulated
[L3236] [107:11.72] where where there's a really clear
[L3237] [107:14.44] constraint in front of me.
[L3238] [107:16.56] And um that to me is engineering. Like
[L3239] [107:19.12] if
[L3240] [107:20.36] I I actually know what the definition of
[L3241] [107:21.52] engineering is, but I'm just going to
[L3242] [107:23.40] make it up in my mind, engineering is
[L3243] [107:26.20] science with constraints. It's like It's
[L3244] [107:28.36] like how to How do you
[L3245] [107:31.52] solve problems in the presence of
[L3246] [107:33.36] resource constraints?
[L3247] [107:35.04] I'm not particularly interested in
[L3248] [107:36.44] constraint-free environments. That's
[L3249] [107:38.36] art.
[L3250] [107:39.32] I like craft and engineering. And the
[L3251] [107:43.08] the more visceral and difficult the
[L3252] [107:45.00] constraints, the more fun that is for
[L3253] [107:46.56] me.
[L3254] [107:47.96] And I I've I've been lucky enough to
[L3255] [107:50.96] I don't know whether it's luck or
[L3256] [107:53.24] intention, I don't know, but I I I've
[L3257] [107:55.08] always placed myself in those
[L3258] [107:57.28] environments, you know, like
[L3259] [108:00.80] let's go get on the hardest team and and
[L3260] [108:03.24] own the hardest problem and then
[L3261] [108:05.20] um and then, you know, put the effort
[L3262] [108:07.00] into to to survive.
[L3263] [108:10.20] >> This question might be a little bit off
[L3264] [108:11.80] topic, but you know, I know you were a
[L3265] [108:14.40] consultant for the show the TV show
[L3266] [108:16.80] Silicon Valley.
[L3267] [108:18.28] I love that show and I got to hear how'd
[L3268] [108:20.56] you get involved in that?
[L3269] [108:21.88] >> Yeah, that was a lot of fun. So, um
[L3270] [108:25.20] a lot of folks might not know this. Um
[L3271] [108:28.24] I had nothing to do with season 1. So, a
[L3272] [108:29.92] lot of TV shows, they don't know whether
[L3273] [108:31.40] they're going to survive as a TV show.
[L3274] [108:33.56] So, so, um Mike Judge who started um who
[L3275] [108:37.40] who who wrote Silicon Valley also was of
[L3276] [108:39.64] Beavis and Butt-Head and Office Space
[L3277] [108:41.24] fame. He started his career as a
[L3278] [108:43.12] software engineer at I think Lockheed or
[L3279] [108:45.04] something. So, he actually was a
[L3280] [108:46.48] software engineer that a lot of people
[L3281] [108:48.12] don't realize. And so, Silicon Valley
[L3282] [108:50.20] was like a throwback to the kind of
[L3283] [108:52.56] work he did. And if you anyone's seen
[L3284] [108:53.76] the movie Office Space, you would you
[L3285] [108:55.20] would get this. It's That's a really a
[L3286] [108:57.04] you know, dystopian cubicle era uh tech
[L3287] [108:59.88] uh industry um film.
[L3288] [109:01.48] Um so, they did season 1 of of Silicon
[L3289] [109:04.44] Valley and then it was very popular and
[L3290] [109:06.92] they got picked up and so, they had to
[L3291] [109:08.32] figure out what to do for season 2, but
[L3292] [109:09.80] they didn't know what to do because they
[L3293] [109:11.76] did they'd written a storyline that gets
[L3294] [109:13.84] to the point where there's a compression
[L3295] [109:15.16] algorithm. And And then what happens?
[L3296] [109:18.16] And so they needed to find um
[L3297] [109:21.68] an expert on compression and I guess
[L3298] [109:24.48] ostensibly that was me. And I don't know
[L3299] [109:26.16] whether I was an expert on compression.
[L3300] [109:27.64] I guess I was an expert on storage at
[L3301] [109:28.92] least. And so and so they came to the
[L3302] [109:31.64] office and and uh and we just chat
[L3303] [109:34.76] chatted and it was so much fun, you
[L3304] [109:36.24] know? And so I was involved in um you're
[L3305] [109:38.88] pretty heavily involved in the show. Um
[L3306] [109:42.24] A lot of it was you know storyline and
