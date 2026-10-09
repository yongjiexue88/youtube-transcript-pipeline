Chunk 10; segments 2949–3233. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L2958] [107:08.88] better than they were, right? Like that
[L2959] [107:10.88] that is the only way out of the current
[L2960] [107:13.68] situation as I see it, right? Uh I don't
[L2961] [107:17.60] know if that's fair, but that's my
[L2962] [107:19.12] that's my sort of feeling on that. One
[L2963] [107:21.68] of your other top tweets it was, you
[L2964] [107:24.24] know, Shopify put out this internal memo
[L2965] [107:27.04] and you just, you know, you replied, you
[L2966] [107:29.28] know, slopify. Yes. [laughter]
[L2967] [107:30.88] >> So, I guess it's cuz in this tweet, it's
[L2968] [107:33.36] leadership pushing the adoption curve
[L2969] [107:35.60] maybe harder than the capabilities of
[L2970] [107:38.08] the AI in this case.
[L2971] [107:39.84] >> Yeah. Uh, although I also just like the
[L2972] [107:41.76] bot. One of the things that I think is
[L2973] [107:44.24] most unfortunate about the AI adoption
[L2974] [107:47.36] as I've seen it is just the because
[L2975] [107:52.08] people think that it's going to be this
[L2976] [107:54.96] major um I guess if I had to categorize
[L2977] [107:57.92] the way it appears that companies are
[L2978] [107:59.68] reasoning about it. They're assuming
[L2979] [108:01.52] that if they don't get in early, it will
[L2980] [108:03.76] be a big disaster for them, right? like
[L2981] [108:06.00] like there's a tremendous like they
[L2982] [108:08.00] don't just think oh well we can just
[L2983] [108:09.68] wait until the AI does what we need it
[L2984] [108:11.36] to do and then start using it. They're
[L2985] [108:12.72] like, "No, we have to do it now." Like
[L2986] [108:14.64] even before we know whether it can
[L2987] [108:16.32] really do the thing that we want it to
[L2988] [108:17.44] do or whether we know whether the
[L2989] [108:18.48] outcomes will be good, everyone has to
[L2990] [108:20.08] do it right now. Let's do this. Right.
[L2991] [108:22.32] Um and I understand why they want why
[L2992] [108:24.72] they're going about it that way because
[L2993] [108:25.68] they think that that that is critical,
[L2994] [108:27.12] right? They obviously believe that's
[L2995] [108:28.24] very important.
[L2996] [108:30.00] Um, and to me that's just that's just
[L2997] [108:32.72] kind of terrifying because as with any
[L2998] [108:35.52] technology, the sane way to do it is to
[L2999] [108:39.52] measure its capabilities, see how well
[L3000] [108:42.00] it is able to solve problems that you
[L3001] [108:43.60] have, see if it solves them faster than
[L3002] [108:45.60] the way that you were do doing it, and
[L3003] [108:48.88] put it into a workflow at such a time as
[L3004] [108:51.44] you've determined that it is a net
[L3005] [108:53.12] positive. That's just the same like
[L3006] [108:54.96] that's what you do with any technology,
[L3007] [108:56.72] right? And you'd probably have like your
[L3008] [108:58.88] team of people whose job it is to assess
[L3009] [109:00.88] this thing and they're out there yolo
[L3010] [109:02.56] swagging it, right? They've got 3,000
[L3011] [109:05.28] agents working on this cluster talking
[L3012] [109:07.28] to each other and doing, you know, god
[L3013] [109:09.04] knows what, right? And uh so there's
[L3014] [109:12.08] going to be that and someone's going to
[L3015] [109:13.76] be doing that, but that is should not be
[L3016] [109:15.20] every or right like you wouldn't just be
[L3017] [109:16.80] like everyone needs to use a ton of
[L3018] [109:18.56] tokens, right? Um
[L3019] [109:21.44] so yeah, like I I do have concerns about
[L3020] [109:23.92] that. I don't think that that the way AI
[L3021] [109:26.96] adoption was done was was the best way
[L3022] [109:30.16] for quality in software. But I would
[L3023] [109:34.32] temper that statement with just the
[L3024] [109:36.40] obvious fact that like we were not
[L3025] [109:38.56] exactly a 59's uh industry to start out
[L3026] [109:42.72] with. Like software quality was really
[L3027] [109:45.20] pretty low rolling into the AI era. So I
[L3028] [109:49.44] always try to just also caveat most of
[L3029] [109:52.32] the things that I have to say that might
[L3030] [109:54.40] be critical of a particular thing
[L3031] [109:55.76] happening with AI with just the fact
[L3032] [109:57.04] that like look it wasn't particularly
[L3033] [109:59.04] great beforehand either. Uh a lot of
[L3034] [110:02.00] this software was pretty low quality and
[L3035] [110:04.00] so you can't
[L3036] [110:06.88] some AI things may may make things worse
[L3037] [110:09.84] but it's not like software was amazing
[L3038] [110:11.84] and the AI showed up and ruined
[L3039] [110:13.52] everything. That is completely
[L3040] [110:14.96] ridiculous narrative that that is not
[L3041] [110:16.64] true at all. Do you have any top
[L3042] [110:19.68] technical book recommendations for any
[L3043] [110:21.92] engineers that might be listening?
[L3044] [110:24.08] >> Uh, no. I would probably use this
[L3045] [110:27.52] opportunity to try to pitch reading
[L3046] [110:30.24] technical papers. I think something that
[L3047] [110:33.44] uh really the industry could use more of
[L3048] [110:35.92] is people being more aware of what's
[L3049] [110:38.80] happening um both like the historical
[L3050] [110:41.76] papers but also just current papers. Uh
[L3051] [110:45.84] it's daunting at first to be sure if you
[L3052] [110:48.88] don't tend to read technical papers in
[L3053] [110:50.96] your field. You will probably find it
[L3054] [110:54.88] confusing. You won't know where to find
[L3055] [110:56.72] them. You won't know how how to approach
[L3056] [110:59.28] them. Um it will seem to take too long
[L3057] [111:01.60] to read them because you don't know how
[L3058] [111:02.72] to like skim them properly and determine
[L3059] [111:04.32] whether it's worth your time to
[L3060] [111:05.68] investigate a particular section of a
[L3061] [111:06.96] paper and all that stuff. But if you're
[L3062] [111:08.96] willing to spend uh a few months of just
[L3063] [111:13.12] like I at night I look at a paper, you
[L3064] [111:16.64] know, or on my lunch break I look at a
[L3065] [111:18.48] paper, you know, if you're willing to
[L3066] [111:20.64] spend a few months of just doing that,
[L3067] [111:22.32] you will get your bearings and you will
[L3068] [111:23.92] start to know where the good papers are
[L3069] [111:25.36] in your field. You'll know how to find
[L3070] [111:26.72] them. You'll know what where they tend
[L3071] [111:28.08] to be published. Uh you'll be able to
[L3072] [111:31.20] read them much more effectively. You'll
[L3073] [111:32.72] be able to know how to spend your time
[L3074] [111:33.76] on them. And I think in all but probably
[L3075] [111:37.68] a few small fields that probably exist
[L3076] [111:40.40] somewhere that maybe people don't tend
[L3077] [111:42.08] to write much papers in or something
[L3078] [111:43.44] like that, it's tremendously valuable.
[L3079] [111:45.60] And I think it's so valuable that I read
[L3080] [111:48.16] papers in disciplines I don't even do
[L3081] [111:50.64] and I find it extremely rewarding. I I
[L3082] [111:53.36] read security research papers all the
[L3083] [111:55.84] time. I don't even work in a field where
[L3084] [111:57.84] there are security research
[L3085] [111:59.36] implications. Like games don't really do
[L3086] [112:01.60] much of that. that they tend to be run
[L3087] [112:03.04] like very sandboxed and they don't, you
[L3088] [112:04.88] know, sometimes there are, but they're
[L3089] [112:06.64] not that kind of thing. They're not like
[L3090] [112:07.84] a, you know, web server authentication
[L3091] [112:10.48] protocol or something like this.
[L3092] [112:13.28] Uh, and I just find it incredibly
[L3093] [112:14.88] rewarding because there's just so much
[L3094] [112:16.24] good stuff out there that you can learn.
[L3095] [112:17.92] So, I would say that would be it instead
[L3096] [112:20.24] of a book wreck. I would say find a
[L3097] [112:22.56] paper. Try reading a paper. How do I go
[L3098] [112:25.20] and find that, you know, first paper or
[L3099] [112:28.16] some place to get started that will be
[L3100] [112:30.08] valuable
[L3101] [112:31.12] >> for most people who are watching because
[L3102] [112:33.20] they they might be like generalists or,
[L3103] [112:35.60] you know, work work in in webdev or in
[L3104] [112:38.56] just a a tech general tech org at a at a
[L3105] [112:41.12] big tech company or something like that.
[L3106] [112:43.44] I would say like pull up the proceedings
[L3107] [112:46.32] of USNIX uh US NIX. Um
[L3108] [112:51.76] look through it for a paper that sounds
[L3109] [112:53.12] interesting to you and try reading that
[L3110] [112:54.40] paper or uh oftentimes there's a awards
[L3111] [112:57.76] I think USNIX has them where it's like
[L3112] [112:59.60] best paper of the conference. Try
[L3113] [113:00.88] reading the best paper conference. See
[L3114] [113:02.24] what you think. Um because that's like a
[L3115] [113:04.64] that's a collection of papers that's
[L3116] [113:06.08] usually about like operating system
[L3117] [113:07.44] stuff and you know systems design stuff.
[L3118] [113:09.60] So it's going to be something that most
[L3119] [113:11.52] people can relate to. It's not going to
[L3120] [113:13.12] be really esoteric like if you were to
[L3121] [113:15.68] open up the proceedings of sigraph for
[L3122] [113:17.52] example it'd be like oh uh you know
[L3123] [113:21.84] neural networks for cloth simulation or
[L3124] [113:24.64] something you're like okay like
[L3125] [113:27.28] this is not I can't relate to this
[L3126] [113:29.92] because I don't do graphics or whatever
[L3127] [113:31.84] right uh so usix might be a good place
[L3128] [113:34.24] to start um but in general yeah like if
[L3129] [113:38.08] you had another option would be to go to
[L3130] [113:41.28] scholar.google google.com
[L3131] [113:44.00] which is their search that just
[L3132] [113:45.36] specializes in like papers and type in a
[L3133] [113:48.64] topic description that you find
[L3134] [113:50.72] interesting. So like um if you wanted to
[L3135] [113:53.60] learn you know maybe maybe you were very
[L3136] [113:56.00] interested in consensus algor Paxos or
[L3137] [113:58.32] something and I don't know what that is
[L3138] [113:59.76] or I it came up at work and I haven't
[L3139] [114:02.08] really ever looked at it. You can just
[L3140] [114:03.36] type that in Paxos and it'll just be a
[L3141] [114:05.28] list of papers and they'll say a thing
[L3142] [114:06.80] like cited by you can see how many
[L3143] [114:08.80] citations they have. That's usually how
[L3144] [114:10.40] influential that paper was. Like I mean
[L3145] [114:12.48] to a certain extent. Um so you know
[L3146] [114:16.00] those are some ways you could get
[L3147] [114:17.44] started and find something that might
[L3148] [114:18.96] interest you. Uh and you know it won't
[L3149] [114:21.76] be for everyone. You may bounce off it
[L3150] [114:23.28] but it be that'd be my recommendation is
[L3151] [114:25.04] something to try. You you might you
[L3152] [114:26.56] might find it interesting.
[L3153] [114:28.08] >> And then yeah last question for you is
[L3154] [114:30.16] if you could go back to the beginning of
[L3155] [114:31.92] your career when you just entered the
[L3156] [114:34.16] industry and give yourself some advice
[L3157] [114:35.92] what would you say?
[L3158] [114:38.00] So I think the advice I would have given
[L3159] [114:39.76] to myself was to get into low-level
[L3160] [114:42.40] programming earlier.
[L3161] [114:45.12] Uh, I didn't really learn how to like
[L3162] [114:49.28] properly analyze and or even really
[L3163] [114:52.00] write assembly language code until
[L3164] [114:55.68] probably like
[L3165] [114:58.48] gosh 201 or 15 or like I mean it's
[L3166] [115:03.28] recent um because I'm pretty old and you
[L3167] [115:07.44] know it it's like last 10 years or so or
[L3168] [115:10.56] something, right?
[L3169] [115:12.56] And uh and I feel like I always
[L3170] [115:17.76] I always wanted to know how to do it and
[L3171] [115:20.00] just never seemed to. And like the the
[L3172] [115:23.36] advice I would have given to myself that
[L3173] [115:25.12] was like just just go like down the hall
[L3174] [115:28.64] like what I was interested like go down
[L3175] [115:30.08] the hall and like be like grab some be
[L3176] [115:32.40] like show me how the heck you write this
[L3177] [115:34.88] like just just show it to me. like
[L3178] [115:36.32] right. I think one of the problems is uh
[L3179] [115:39.04] a lot of people especially when they're
[L3180] [115:40.72] young they are afraid of appearing like
[L3181] [115:43.92] they don't know things and I think that
[L3182] [115:46.72] can be a real impediment to learning.
[L3183] [115:48.56] I'm sure it was for me and I probably
[L3184] [115:50.80] like just didn't want to like literally
[L3185] [115:52.32] say like I don't know I don't understand
[L3186] [115:53.76] any of this stuff like can you explain
[L3187] [115:54.96] it to me and uh and I think that's one
[L3188] [115:59.20] of the most useful things you can do
[L3189] [116:00.72] like I don't understand this please
[L3190] [116:02.40] explain it to me is very useful and most
[L3191] [116:05.12] people will be very happy to do that if
[L3192] [116:07.44] they're not a dick like most people will
[L3193] [116:09.60] be like oh sure like here you know um
[L3194] [116:12.08] now they might not be good at explaining
[L3195] [116:13.84] it there are plenty of engineers who are
[L3196] [116:16.24] like really good at something and suck
[L3197] [116:18.16] suck at like telling you how they do
[L3198] [116:20.72] what they do. So you won't always get a
[L3199] [116:23.60] great explanation, but sometimes you
[L3200] [116:26.48] will. Sometimes you'll find the type of
[L3201] [116:28.16] person who can explain very clearly how
[L3202] [116:30.32] it is they do what they do. So if just
[L3203] [116:32.16] keep asking, you'll get you'll get the
[L3204] [116:33.84] good explanation. Nowadays,
[L3205] [116:36.80] I wouldn't really need to give myself
[L3206] [116:38.16] exactly that advice because the internet
[L3207] [116:40.08] has so much great information on it. I
[L3208] [116:42.24] could have taught myself. That did not
[L3209] [116:44.48] exist at the time.
[L3210] [116:46.48] >> Awesome. Well, thank you so much for
[L3211] [116:47.76] your time, Casey. I really appreciate
[L3212] [116:48.96] it.
[L3213] [116:49.36] >> Thank you so much for having me. Like I
[L3214] [116:50.56] said, I love the show. It was it was an
[L3215] [116:52.08] honor to be invited on. So, thank you
[L3216] [116:53.36] very much.
[L3217] [116:54.56] >> Hey, thank you for watching this
[L3218] [116:55.76] podcast. If you liked it and you want to
[L3219] [116:57.36] see the show grow, please support with a
[L3220] [116:59.68] comment or a like. Also, if you have any
[L3221] [117:02.56] recommendations for people you want me
[L3222] [117:04.24] to bring on, please drop a comment.
[L3223] [117:06.88] Guests like Barbara Liskov, Mike
[L3224] [117:09.04] Stonereaker, Mark Brooker, these were
[L3225] [117:11.52] all people that I brought on because
[L3226] [117:13.52] someone left a comment. On another note,
[L3227] [117:15.76] aside from the podcast, I'm working on
[L3228] [117:17.68] building the ergonomic keyboard that I
[L3229] [117:19.52] wish existed. Here's a glance at the
[L3230] [117:21.76] prototype. It's a split keyboard, so
[L3231] [117:24.00] there's two sides. Um, this is in the
[L3232] [117:26.16] case, but yeah, we launched on
[L3233] [117:27.60] Kickstarter and we hit our goal within
[L3234] [117:29.68] eight hours of launching. I really
[L3235] [117:31.28] appreciate it if you were one of the
[L3236] [117:32.56] people who grabbed one of the early
[L3237] [117:34.08] units. Um, we're now working on the long
[L3238] [117:36.48] journey of building the tooling now. And
[L3239] [117:38.48] so, if you still want to pick one up,
[L3240] [117:40.24] I've left the late pledges open on
[L3241] [117:42.24] Kickstarter, so you can grab one there.
[L3242] [117:44.48] I'll put a link in the description.
