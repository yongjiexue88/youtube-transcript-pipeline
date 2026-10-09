Chunk 10; segments 2975–3233. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L2984] [01:48:11.36] to do and then start using it. They're
[L2985] [01:48:12.72] like, "No, we have to do it now." Like
[L2986] [01:48:14.64] even before we know whether it can
[L2987] [01:48:16.32] really do the thing that we want it to
[L2988] [01:48:17.44] do or whether we know whether the
[L2989] [01:48:18.48] outcomes will be good, everyone has to
[L2990] [01:48:20.08] do it right now. Let's do this. Right.
[L2991] [01:48:22.32] Um and I understand why they want why
[L2992] [01:48:24.72] they're going about it that way because
[L2993] [01:48:25.68] they think that that that is critical,
[L2994] [01:48:27.12] right? They obviously believe that's
[L2995] [01:48:28.24] very important.
[L2996] [01:48:30.00] Um, and to me that's just that's just
[L2997] [01:48:32.72] kind of terrifying because as with any
[L2998] [01:48:35.52] technology, the sane way to do it is to
[L2999] [01:48:39.52] measure its capabilities, see how well
[L3000] [01:48:42.00] it is able to solve problems that you
[L3001] [01:48:43.60] have, see if it solves them faster than
[L3002] [01:48:45.60] the way that you were do doing it, and
[L3003] [01:48:48.88] put it into a workflow at such a time as
[L3004] [01:48:51.44] you've determined that it is a net
[L3005] [01:48:53.12] positive. That's just the same like
[L3006] [01:48:54.96] that's what you do with any technology,
[L3007] [01:48:56.72] right? And you'd probably have like your
[L3008] [01:48:58.88] team of people whose job it is to assess
[L3009] [01:49:00.88] this thing and they're out there yolo
[L3010] [01:49:02.56] swagging it, right? They've got 3,000
[L3011] [01:49:05.28] agents working on this cluster talking
[L3012] [01:49:07.28] to each other and doing, you know, god
[L3013] [01:49:09.04] knows what, right? And uh so there's
[L3014] [01:49:12.08] going to be that and someone's going to
[L3015] [01:49:13.76] be doing that, but that is should not be
[L3016] [01:49:15.20] every or right like you wouldn't just be
[L3017] [01:49:16.80] like everyone needs to use a ton of
[L3018] [01:49:18.56] tokens, right? Um
[L3019] [01:49:21.44] so yeah, like I I do have concerns about
[L3020] [01:49:23.92] that. I don't think that that the way AI
[L3021] [01:49:26.96] adoption was done was was the best way
[L3022] [01:49:30.16] for quality in software. But I would
[L3023] [01:49:34.32] temper that statement with just the
[L3024] [01:49:36.40] obvious fact that like we were not
[L3025] [01:49:38.56] exactly a 59's uh industry to start out
[L3026] [01:49:42.72] with. Like software quality was really
[L3027] [01:49:45.20] pretty low rolling into the AI era. So I
[L3028] [01:49:49.44] always try to just also caveat most of
[L3029] [01:49:52.32] the things that I have to say that might
[L3030] [01:49:54.40] be critical of a particular thing
[L3031] [01:49:55.76] happening with AI with just the fact
[L3032] [01:49:57.04] that like look it wasn't particularly
[L3033] [01:49:59.04] great beforehand either. Uh a lot of
[L3034] [01:50:02.00] this software was pretty low quality and
[L3035] [01:50:04.00] so you can't
[L3036] [01:50:06.88] some AI things may may make things worse
[L3037] [01:50:09.84] but it's not like software was amazing
[L3038] [01:50:11.84] and the AI showed up and ruined
[L3039] [01:50:13.52] everything. That is completely
[L3040] [01:50:14.96] ridiculous narrative that that is not
[L3041] [01:50:16.64] true at all. Do you have any top
[L3042] [01:50:19.68] technical book recommendations for any
[L3043] [01:50:21.92] engineers that might be listening?
[L3044] [01:50:24.08] >> Uh, no. I would probably use this
[L3045] [01:50:27.52] opportunity to try to pitch reading
[L3046] [01:50:30.24] technical papers. I think something that
[L3047] [01:50:33.44] uh really the industry could use more of
[L3048] [01:50:35.92] is people being more aware of what's
[L3049] [01:50:38.80] happening um both like the historical
[L3050] [01:50:41.76] papers but also just current papers. Uh
[L3051] [01:50:45.84] it's daunting at first to be sure if you
[L3052] [01:50:48.88] don't tend to read technical papers in
[L3053] [01:50:50.96] your field. You will probably find it
[L3054] [01:50:54.88] confusing. You won't know where to find
[L3055] [01:50:56.72] them. You won't know how how to approach
[L3056] [01:50:59.28] them. Um it will seem to take too long
[L3057] [01:51:01.60] to read them because you don't know how
[L3058] [01:51:02.72] to like skim them properly and determine
[L3059] [01:51:04.32] whether it's worth your time to
[L3060] [01:51:05.68] investigate a particular section of a
[L3061] [01:51:06.96] paper and all that stuff. But if you're
[L3062] [01:51:08.96] willing to spend uh a few months of just
[L3063] [01:51:13.12] like I at night I look at a paper, you
[L3064] [01:51:16.64] know, or on my lunch break I look at a
[L3065] [01:51:18.48] paper, you know, if you're willing to
[L3066] [01:51:20.64] spend a few months of just doing that,
[L3067] [01:51:22.32] you will get your bearings and you will
[L3068] [01:51:23.92] start to know where the good papers are
[L3069] [01:51:25.36] in your field. You'll know how to find
[L3070] [01:51:26.72] them. You'll know what where they tend
[L3071] [01:51:28.08] to be published. Uh you'll be able to
[L3072] [01:51:31.20] read them much more effectively. You'll
[L3073] [01:51:32.72] be able to know how to spend your time
[L3074] [01:51:33.76] on them. And I think in all but probably
[L3075] [01:51:37.68] a few small fields that probably exist
[L3076] [01:51:40.40] somewhere that maybe people don't tend
[L3077] [01:51:42.08] to write much papers in or something
[L3078] [01:51:43.44] like that, it's tremendously valuable.
[L3079] [01:51:45.60] And I think it's so valuable that I read
[L3080] [01:51:48.16] papers in disciplines I don't even do
[L3081] [01:51:50.64] and I find it extremely rewarding. I I
[L3082] [01:51:53.36] read security research papers all the
[L3083] [01:51:55.84] time. I don't even work in a field where
[L3084] [01:51:57.84] there are security research
[L3085] [01:51:59.36] implications. Like games don't really do
[L3086] [01:52:01.60] much of that. that they tend to be run
[L3087] [01:52:03.04] like very sandboxed and they don't, you
[L3088] [01:52:04.88] know, sometimes there are, but they're
[L3089] [01:52:06.64] not that kind of thing. They're not like
[L3090] [01:52:07.84] a, you know, web server authentication
[L3091] [01:52:10.48] protocol or something like this.
[L3092] [01:52:13.28] Uh, and I just find it incredibly
[L3093] [01:52:14.88] rewarding because there's just so much
[L3094] [01:52:16.24] good stuff out there that you can learn.
[L3095] [01:52:17.92] So, I would say that would be it instead
[L3096] [01:52:20.24] of a book wreck. I would say find a
[L3097] [01:52:22.56] paper. Try reading a paper. How do I go
[L3098] [01:52:25.20] and find that, you know, first paper or
[L3099] [01:52:28.16] some place to get started that will be
[L3100] [01:52:30.08] valuable
[L3101] [01:52:31.12] >> for most people who are watching because
[L3102] [01:52:33.20] they they might be like generalists or,
[L3103] [01:52:35.60] you know, work work in in webdev or in
[L3104] [01:52:38.56] just a a tech general tech org at a at a
[L3105] [01:52:41.12] big tech company or something like that.
[L3106] [01:52:43.44] I would say like pull up the proceedings
[L3107] [01:52:46.32] of USNIX uh US NIX. Um
[L3108] [01:52:51.76] look through it for a paper that sounds
[L3109] [01:52:53.12] interesting to you and try reading that
[L3110] [01:52:54.40] paper or uh oftentimes there's a awards
[L3111] [01:52:57.76] I think USNIX has them where it's like
[L3112] [01:52:59.60] best paper of the conference. Try
[L3113] [01:53:00.88] reading the best paper conference. See
[L3114] [01:53:02.24] what you think. Um because that's like a
[L3115] [01:53:04.64] that's a collection of papers that's
[L3116] [01:53:06.08] usually about like operating system
[L3117] [01:53:07.44] stuff and you know systems design stuff.
[L3118] [01:53:09.60] So it's going to be something that most
[L3119] [01:53:11.52] people can relate to. It's not going to
[L3120] [01:53:13.12] be really esoteric like if you were to
[L3121] [01:53:15.68] open up the proceedings of sigraph for
[L3122] [01:53:17.52] example it'd be like oh uh you know
[L3123] [01:53:21.84] neural networks for cloth simulation or
[L3124] [01:53:24.64] something you're like okay like
[L3125] [01:53:27.28] this is not I can't relate to this
[L3126] [01:53:29.92] because I don't do graphics or whatever
[L3127] [01:53:31.84] right uh so usix might be a good place
[L3128] [01:53:34.24] to start um but in general yeah like if
[L3129] [01:53:38.08] you had another option would be to go to
[L3130] [01:53:41.28] scholar.google google.com
[L3131] [01:53:44.00] which is their search that just
[L3132] [01:53:45.36] specializes in like papers and type in a
[L3133] [01:53:48.64] topic description that you find
[L3134] [01:53:50.72] interesting. So like um if you wanted to
[L3135] [01:53:53.60] learn you know maybe maybe you were very
[L3136] [01:53:56.00] interested in consensus algor Paxos or
[L3137] [01:53:58.32] something and I don't know what that is
[L3138] [01:53:59.76] or I it came up at work and I haven't
[L3139] [01:54:02.08] really ever looked at it. You can just
[L3140] [01:54:03.36] type that in Paxos and it'll just be a
[L3141] [01:54:05.28] list of papers and they'll say a thing
[L3142] [01:54:06.80] like cited by you can see how many
[L3143] [01:54:08.80] citations they have. That's usually how
[L3144] [01:54:10.40] influential that paper was. Like I mean
[L3145] [01:54:12.48] to a certain extent. Um so you know
[L3146] [01:54:16.00] those are some ways you could get
[L3147] [01:54:17.44] started and find something that might
[L3148] [01:54:18.96] interest you. Uh and you know it won't
[L3149] [01:54:21.76] be for everyone. You may bounce off it
[L3150] [01:54:23.28] but it be that'd be my recommendation is
[L3151] [01:54:25.04] something to try. You you might you
[L3152] [01:54:26.56] might find it interesting.
[L3153] [01:54:28.08] >> And then yeah last question for you is
[L3154] [01:54:30.16] if you could go back to the beginning of
[L3155] [01:54:31.92] your career when you just entered the
[L3156] [01:54:34.16] industry and give yourself some advice
[L3157] [01:54:35.92] what would you say?
[L3158] [01:54:38.00] So I think the advice I would have given
[L3159] [01:54:39.76] to myself was to get into low-level
[L3160] [01:54:42.40] programming earlier.
[L3161] [01:54:45.12] Uh, I didn't really learn how to like
[L3162] [01:54:49.28] properly analyze and or even really
[L3163] [01:54:52.00] write assembly language code until
[L3164] [01:54:55.68] probably like
[L3165] [01:54:58.48] gosh 201 or 15 or like I mean it's
[L3166] [01:55:03.28] recent um because I'm pretty old and you
[L3167] [01:55:07.44] know it it's like last 10 years or so or
[L3168] [01:55:10.56] something, right?
[L3169] [01:55:12.56] And uh and I feel like I always
[L3170] [01:55:17.76] I always wanted to know how to do it and
[L3171] [01:55:20.00] just never seemed to. And like the the
[L3172] [01:55:23.36] advice I would have given to myself that
[L3173] [01:55:25.12] was like just just go like down the hall
[L3174] [01:55:28.64] like what I was interested like go down
[L3175] [01:55:30.08] the hall and like be like grab some be
[L3176] [01:55:32.40] like show me how the heck you write this
[L3177] [01:55:34.88] like just just show it to me. like
[L3178] [01:55:36.32] right. I think one of the problems is uh
[L3179] [01:55:39.04] a lot of people especially when they're
[L3180] [01:55:40.72] young they are afraid of appearing like
[L3181] [01:55:43.92] they don't know things and I think that
[L3182] [01:55:46.72] can be a real impediment to learning.
[L3183] [01:55:48.56] I'm sure it was for me and I probably
[L3184] [01:55:50.80] like just didn't want to like literally
[L3185] [01:55:52.32] say like I don't know I don't understand
[L3186] [01:55:53.76] any of this stuff like can you explain
[L3187] [01:55:54.96] it to me and uh and I think that's one
[L3188] [01:55:59.20] of the most useful things you can do
[L3189] [01:56:00.72] like I don't understand this please
[L3190] [01:56:02.40] explain it to me is very useful and most
[L3191] [01:56:05.12] people will be very happy to do that if
[L3192] [01:56:07.44] they're not a dick like most people will
[L3193] [01:56:09.60] be like oh sure like here you know um
[L3194] [01:56:12.08] now they might not be good at explaining
[L3195] [01:56:13.84] it there are plenty of engineers who are
[L3196] [01:56:16.24] like really good at something and suck
[L3197] [01:56:18.16] suck at like telling you how they do
[L3198] [01:56:20.72] what they do. So you won't always get a
[L3199] [01:56:23.60] great explanation, but sometimes you
[L3200] [01:56:26.48] will. Sometimes you'll find the type of
[L3201] [01:56:28.16] person who can explain very clearly how
[L3202] [01:56:30.32] it is they do what they do. So if just
[L3203] [01:56:32.16] keep asking, you'll get you'll get the
[L3204] [01:56:33.84] good explanation. Nowadays,
[L3205] [01:56:36.80] I wouldn't really need to give myself
[L3206] [01:56:38.16] exactly that advice because the internet
[L3207] [01:56:40.08] has so much great information on it. I
[L3208] [01:56:42.24] could have taught myself. That did not
[L3209] [01:56:44.48] exist at the time.
[L3210] [01:56:46.48] >> Awesome. Well, thank you so much for
[L3211] [01:56:47.76] your time, Casey. I really appreciate
[L3212] [01:56:48.96] it.
[L3213] [01:56:49.36] >> Thank you so much for having me. Like I
[L3214] [01:56:50.56] said, I love the show. It was it was an
[L3215] [01:56:52.08] honor to be invited on. So, thank you
[L3216] [01:56:53.36] very much.
[L3217] [01:56:54.56] >> Hey, thank you for watching this
[L3218] [01:56:55.76] podcast. If you liked it and you want to
[L3219] [01:56:57.36] see the show grow, please support with a
[L3220] [01:56:59.68] comment or a like. Also, if you have any
[L3221] [01:57:02.56] recommendations for people you want me
[L3222] [01:57:04.24] to bring on, please drop a comment.
[L3223] [01:57:06.88] Guests like Barbara Liskov, Mike
[L3224] [01:57:09.04] Stonereaker, Mark Brooker, these were
[L3225] [01:57:11.52] all people that I brought on because
[L3226] [01:57:13.52] someone left a comment. On another note,
[L3227] [01:57:15.76] aside from the podcast, I'm working on
[L3228] [01:57:17.68] building the ergonomic keyboard that I
[L3229] [01:57:19.52] wish existed. Here's a glance at the
[L3230] [01:57:21.76] prototype. It's a split keyboard, so
[L3231] [01:57:24.00] there's two sides. Um, this is in the
[L3232] [01:57:26.16] case, but yeah, we launched on
[L3233] [01:57:27.60] Kickstarter and we hit our goal within
[L3234] [01:57:29.68] eight hours of launching. I really
[L3235] [01:57:31.28] appreciate it if you were one of the
[L3236] [01:57:32.56] people who grabbed one of the early
[L3237] [01:57:34.08] units. Um, we're now working on the long
[L3238] [01:57:36.48] journey of building the tooling now. And
[L3239] [01:57:38.48] so, if you still want to pick one up,
[L3240] [01:57:40.24] I've left the late pledges open on
[L3241] [01:57:42.24] Kickstarter, so you can grab one there.
[L3242] [01:57:44.48] I'll put a link in the description.
