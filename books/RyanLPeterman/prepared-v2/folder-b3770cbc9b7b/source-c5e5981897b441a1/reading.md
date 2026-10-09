# Meta Distinguished Eng (IC9): Influencing Engs, Failures, and Learnings | Adam Ernst

Source ID: source-c5e5981897b441a1
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Meta_Distinguished_Eng_(IC9)_Influencing_Engs,_Failures,_and_Learnings_Adam_Ernst_en.txt
Video: https://www.youtube.com/watch?v=YA_OYJF3Mmw

[L10] [00:00.32] When I run into a problem, instead of
[L11] [00:01.84] being like, "All right, got to go talk
[L12] [00:02.80] to the GraphQL team." I'm like, "Screw
[L13] [00:04.56] it. I'm just going to figure out what
[L14] [00:06.08] the problem is." This is Adam Ernst.
[L15] [00:09.04] He's [music] a distinguished engineer or
[L16] [00:10.72] IC9 at Meta who has built iOS
[L17] [00:13.12] infrastructure that impacted the entire
[L18] [00:15.20] company. And I asked them how his career
[L19] [00:17.60] grew. If you show up, you're like, "Hey,
[L20] [00:19.28] I did the work already for you." Much
[L21] [00:21.12] easier conversation. 1,600 diffs in 6
[L22] [00:24.00] months. Why did you spend so much time
[L23] [00:26.80] also reviewing code? It's really
[L24] [00:28.96] valuable because you can influence other
[L25] [00:30.56] engineers in an organic way.
[L26] [00:32.56] >> He was unusually honest about a major
[L27] [00:34.80] failed project. So, component script was
[L28] [00:37.12] interesting because it was a total and
[L29] [00:38.56] complete failure and I worked on it for
[L30] [00:40.32] like 2 years. With all that push back,
[L31] [00:42.32] did you ever doubt the direction that
[L32] [00:44.32] you're going in?
[L33] [00:45.28] >> There were some literally sleepless
[L34] [00:46.80] nights. Here's the full episode. [music]
[L35] [00:53.28] I saw that you have something on your
[L36] [00:54.88] resume. It says CosmicSoft, which
[L37] [00:57.12] started in 2000. And if I have the math
[L38] [01:00.80] right, that's like middle school for
[L39] [01:02.48] you. So, what was that? And can you talk
[L40] [01:05.20] more about the story behind Cosmicoft?
[L41] [01:07.68] >> Yeah, you dug deep, man. I got to take
[L42] [01:09.36] that off of there. That is indeed my
[L43] [01:11.36] middle school software company. I
[L44] [01:14.48] discovered at an early age that I liked
[L45] [01:17.20] writing software. My mom was a teacher
[L46] [01:20.32] and I would often spend time in her
[L47] [01:22.08] classroom after school just like messing
[L48] [01:24.32] around with computers and that gave me
[L49] [01:27.04] the inspiration for my first product to
[L50] [01:30.16] sell which was online testing software.
[L51] [01:33.92] I wrote it in a tool called real basic
[L52] [01:36.64] which was basically a crossplatform
[L53] [01:39.28] visual basic inspired language. So I was
[L54] [01:41.60] actually writing basic which oh god uh
[L55] [01:44.72] and uh yeah sold it on the internet to
[L56] [01:46.96] like tons of different countries. Uh it
[L57] [01:50.00] was a lot of fun.
[L58] [01:51.60] >> I was not a programmer at that time. Can
[L59] [01:54.96] you give some more context? Is that
[L60] [01:56.40] something that's running uh I guess
[L61] [01:58.32] native on like a Windows machine or
[L62] [02:00.48] something or what what is that? Well,
[L63] [02:02.48] Real Basic was this this product from a
[L64] [02:04.40] different company, not Microsoft. And it
[L65] [02:06.00] was inspired by Visual Basic, very
[L66] [02:07.68] clearly Visual Basicesque, but it was
[L67] [02:10.48] crossplatform, meaning you could design
[L68] [02:11.92] the software on any platform. I used a
[L69] [02:13.84] Mac. The concept behind Visual Basic for
[L70] [02:15.92] those who haven't used it is that you
[L71] [02:17.36] basically had this like blank canvas and
[L72] [02:19.36] you could just drag and drop buttons and
[L73] [02:21.92] text fields and all this stuff on it.
[L74] [02:24.08] Very easy to get into, right? Because
[L75] [02:26.56] even nowadays with something like Swift
[L76] [02:28.32] UI or React, you're writing code that
[L77] [02:30.64] describes your user interface. There's a
[L78] [02:32.56] separation there. Whereas Visual Basic,
[L79] [02:34.32] you're like, well, I want a button,
[L80] [02:35.60] drag, drop. Hm. When the button is
[L81] [02:37.60] clicked, I want it to close the screen.
[L82] [02:39.36] Okay, double click on the button. And
[L83] [02:40.80] you write some code that's like
[L84] [02:42.00] window.clo. Uh so really easy to get
[L85] [02:44.24] started with, not very scalable and you
[L86] [02:47.12] know basic is a horrifying language but
[L87] [02:49.52] uh it was a fun way to get started and
[L88] [02:52.08] really easy for me as basically a middle
[L89] [02:53.92] schooler to write an actual software
[L90] [02:55.60] product that was useful. How are you
[L91] [02:57.68] selling that on the internet? Because at
[L92] [02:59.76] the time they didn't have Stripe or
[L93] [03:01.76] anything like that. Like how do you even
[L94] [03:03.36] receive money from these people in other
[L95] [03:05.04] countries?
[L96] [03:05.84] >> There was a service called Eccelerate
[L97] [03:08.16] which was like a prototype. It allowed
[L98] [03:10.56] you to create an online store for your
[L99] [03:13.36] software. It would help you create uh
[L100] [03:16.32] you know like a code that you could
[L101] [03:17.36] enter to unlock the software. And so
[L102] [03:19.28] people would go to this website, they
[L103] [03:20.56] type in their credit card info, and they
[L104] [03:23.04] would get a code to unlock my software.
[L105] [03:25.52] Fun fact, I also accepted payment via
[L106] [03:27.84] check. So for a while as like an eighth
[L107] [03:29.92] grader, I was getting checks from all
[L108] [03:31.20] over the United States from teachers.
[L109] [03:32.72] They'd mail me a check for 1995 and I
[L110] [03:35.12] would send them via email a code to
[L111] [03:36.80] unlock their software. Good times. Did
[L112] [03:38.72] your parents know you were selling
[L113] [03:40.48] software to strangers on the internet?
[L114] [03:42.48] >> They did. I don't know what I don't know
[L115] [03:44.08] what they thought of it or or or what
[L116] [03:45.92] they could make of it, but they did know
[L117] [03:47.84] I was doing it. [laughter]
[L118] [03:50.24] >> Okay, that that's so cool. But yeah, let
[L119] [03:52.16] let's get into kind of like the main
[L120] [03:53.60] part of your career, which is um you
[L121] [03:55.76] joining Facebook. You joined the company
[L122] [03:58.00] to help with the native app rewrite from
[L123] [04:00.80] HTML 5, and you got promoted to uh the
[L124] [04:04.80] staff equivalent or E6 very fast. Were
[L125] [04:07.52] you hired as a E5?
[L126] [04:10.08] >> I'm pretty sure I was hired as an E5
[L127] [04:12.00] because I had industry experience. I was
[L128] [04:14.64] self-employed, but I, you know, like
[L129] [04:15.92] wrote software in the industry for
[L130] [04:17.60] iPhone. And yeah, it was funny because
[L131] [04:20.16] Facebook was just a totally different
[L132] [04:21.68] company. I joined just before the IPO,
[L133] [04:24.40] like literally weeks before the IPO. And
[L134] [04:26.40] so it was already a large company, but
[L135] [04:28.00] compared to what it is today, totally
[L136] [04:29.76] different. All of the iOS engineers
[L137] [04:31.60] could meet in one conference room and
[L138] [04:33.12] and we did, right? like every week we
[L139] [04:35.04] had a a stand up and like we talked
[L140] [04:36.56] through what we did that week and all
[L141] [04:37.68] that stuff and yeah it was a fun time to
[L142] [04:39.36] join because we were totally rewriting
[L143] [04:41.12] the app. There was this cultural shift
[L144] [04:43.28] away from face web this like HTML 5
[L145] [04:46.24] attempt at making a native app and
[L146] [04:48.16] towards the native code and the native
[L147] [04:49.92] engineers were very much like ascendant
[L148] [04:52.32] right like we had we had won the battle
[L149] [04:53.84] and now we were we needed to prove
[L150] [04:55.44] ourselves that it was going to work out
[L151] [04:57.12] and it did and that also meant a lot of
[L152] [04:58.88] big pro uh a lot of big opportunities a
[L153] [05:01.76] lot of big problems that needed solving
[L154] [05:03.36] because our codebase was brand new and
[L155] [05:05.28] we were discovering all the ways where
[L156] [05:07.12] it was going to fall over as we
[L157] [05:09.52] continued making the app bigger adding
[L158] [05:11.04] new features
[L159] [05:12.00] So that's what I walked into in 2012 and
[L160] [05:14.56] it was definitely a fun time.
[L161] [05:16.80] >> One of the first projects that you
[L162] [05:18.32] worked on was one of those scaling
[L163] [05:20.32] challenges in adopting native code and
[L164] [05:22.96] that also happened to be your E6 promo.
[L165] [05:25.68] Could you talk a little bit about the
[L166] [05:27.60] core data problem and you know why it
[L167] [05:29.76] was E6?
[L168] [05:31.04] >> Yeah, core data is Apple's OM database
[L169] [05:35.04] framework. It's great if you are a
[L170] [05:37.44] startup that has like two engineers and
[L171] [05:39.44] you just need a small little way to
[L172] [05:41.20] store data. It works great for that. We
[L173] [05:43.44] already had, like I said, we had enough
[L174] [05:45.36] iOS engineers we could all fit in one
[L175] [05:46.88] conference room. So, we started with
[L176] [05:48.00] like 15 to 20 maybe by the time I got
[L177] [05:50.40] there. And we were rapidly growing,
[L178] [05:52.64] right? Like soon we had 100, soon we had
[L179] [05:54.48] 200. Core data falls over completely at
[L180] [05:56.80] that scale. So, we needed to swap out
[L181] [06:00.08] how we store data. But this was also a
[L182] [06:02.64] really critical time, right? We had at
[L183] [06:04.32] this point just launched our native
[L184] [06:06.16] rewrite using core data and so everyone
[L185] [06:08.64] wanted to add features. The groups team,
[L186] [06:10.56] the events team, the pages team, they
[L187] [06:12.40] all wanted to like rewrite their stuff
[L188] [06:14.08] in native and get all the great wins
[L189] [06:15.60] from native code. Meanwhile, we on the
[L190] [06:18.00] on at that time we mobile was a separate
[L191] [06:19.76] org inside of Facebook. We on the mobile
[L192] [06:21.36] team were like uh this is not going so
[L193] [06:23.12] well. Like cord data is going to fall
[L194] [06:24.48] over tomorrow and everyone's knocking
[L195] [06:26.16] down our door being like please rewrite
[L196] [06:27.92] native. So we had to find a way to do it
[L197] [06:29.28] incrementally. we needed to find a a
[L198] [06:31.04] better architecture which was what we
[L199] [06:33.28] you know found along the way. So that's
[L200] [06:35.28] where we were in like 2012 2013 and we
[L201] [06:38.24] called our new solution mem models which
[L202] [06:40.16] was an immutable model system which made
[L203] [06:42.08] it a lot easier to reason about thread
[L204] [06:44.08] safety mutations etc.
[L205] [06:46.88] >> You had this new offering that you know
[L206] [06:49.36] had a lot of benefits to it but still I
[L207] [06:52.00] imagine you had to convince other teams
[L208] [06:54.00] to adopt it. So, you know, the core
[L209] [06:56.80] features of the app, feed, etc. were
[L210] [06:58.64] already bought in because the
[L211] [06:59.60] performance was miles better and they
[L212] [07:01.52] didn't require any convincing. It was
[L213] [07:03.44] driving it all the way to the finish
[L214] [07:04.72] line. Getting the last regular products
[L215] [07:06.72] to onboard that was harder, right?
[L216] [07:08.32] Because for them, they were like, "Yeah,
[L217] [07:09.60] so our performance is a little bit
[L218] [07:10.64] better. Who cares? We don't care. We
[L219] [07:12.08] we're more interested in other things."
[L220] [07:14.32] Also, it wasn't necessarily individual
[L221] [07:16.96] teams that were skeptical of the entire
[L222] [07:18.72] project. But there we did get a lot of
[L223] [07:20.40] push back from Apple engineers for a
[L224] [07:22.80] lack of a better word like engineers who
[L225] [07:24.24] believe in Apple's built-in solutions
[L226] [07:26.40] and are like why would we not use core
[L227] [07:27.92] data like I'm an iOS engineer we should
[L228] [07:30.16] use core data and everything else
[L229] [07:31.68] vanilla from Apple. I think that's
[L230] [07:33.60] lesson to someone over the years just
[L231] [07:35.12] because meta and Facebook and Instagram
[L232] [07:37.44] and all of our other properties have
[L233] [07:38.96] gotten so large it's clear that Apple's
[L234] [07:40.88] solutions don't scale to that size. But
[L235] [07:43.28] at least in 2012 and 2013, there was
[L236] [07:45.12] there were a lot of people still
[L237] [07:46.24] clinging to this idea that hey, we
[L238] [07:47.84] should just use the vanilla Apple
[L239] [07:49.20] frameworks and we needed to convince
[L240] [07:50.96] them over and over and over like here's
[L241] [07:52.88] why that's just not going to work. So
[L242] [07:55.20] that was a big challenge for us at the
[L243] [07:56.80] time.
[L244] [07:57.52] >> What did you learn about influencing
[L245] [07:59.68] other engineers without uh authority and
[L246] [08:02.64] do you have any tips on how to do that
[L247] [08:04.56] across like a large code base?
[L248] [08:06.24] >> My number one tip is talk in person or
[L249] [08:07.92] via video conference if possible. you
[L250] [08:09.92] spend a lot of time trying to make your
[L251] [08:11.84] writing clear and accessible and have a
[L252] [08:15.20] good tone and you can often convey that
[L253] [08:17.04] tone way faster in person. My other
[L254] [08:20.32] feedback is to be sympathetic to their
[L255] [08:23.68] point of view, right? Like my I would
[L256] [08:25.20] always start the conversation saying
[L257] [08:26.48] like, "Yes, I prefer vanilla Apple
[L258] [08:28.88] frameworks too. We're not going down
[L259] [08:30.48] this path just because I want to invent
[L260] [08:32.16] a new framework. Here are the specific
[L261] [08:34.56] reasons why we think it can't scale.
[L262] [08:36.72] Give data. give actual you know we were
[L263] [08:39.52] getting to the point where we were
[L264] [08:40.64] disassembling core data's source code
[L265] [08:42.96] because it's not open source to
[L266] [08:44.56] understand what is it doing why is it
[L267] [08:46.48] taking so long to initialize having that
[L268] [08:49.20] data to give to other engineers is
[L269] [08:50.64] really useful right like hey you don't
[L270] [08:51.92] know how core data works because it's a
[L271] [08:53.36] black box we know how it works here's
[L272] [08:54.96] how it works and that's why that's not
[L273] [08:56.24] going to work for us so you know I guess
[L274] [08:58.64] that sums up as do your research so that
[L275] [09:00.88] you can be convincing in that fashion
[L276] [09:03.84] and the final one for me personally is
[L277] [09:05.84] just do the work for them. I think there
[L278] [09:08.24] are some engineers who would go about
[L279] [09:09.60] this project in the sense of hey I built
[L280] [09:11.92] this scaffolding now my job is to
[L281] [09:13.60] convince other people to do the work of
[L282] [09:16.00] migration. We call this code archetype
[L283] [09:18.64] coding machine. I have mixed feelings
[L284] [09:20.16] about archetypes in general but like in
[L285] [09:21.68] general the idea is like I write a lot
[L286] [09:23.04] of code. I like to write code. So my
[L287] [09:24.88] thought was I'll just go do it for them.
[L288] [09:27.12] It's one thing to convince them hey you
[L289] [09:28.96] have to step up and do all this work.
[L290] [09:31.12] The other is like if you show up you're
[L291] [09:32.32] like hey I did the work already for you.
[L292] [09:34.00] Here are the benefits. I just need you
[L293] [09:36.00] to sign off and say yes, this is fine in
[L294] [09:37.68] our codebase. Much easier conversation.
[L295] [09:40.64] That mode of operation was very
[L296] [09:42.40] successful here at Meta for a long time.
[L297] [09:45.52] I think it's getting harder now. Our
[L298] [09:47.28] codebase is so big that one person can't
[L299] [09:49.12] necessarily do the entire migration. You
[L300] [09:51.92] require some more alignment, but for a
[L301] [09:54.24] long time that was a very good way to
[L302] [09:55.44] operate because you just show up and be
[L303] [09:56.64] like, "Hey, I solved the problem." And
[L304] [09:58.16] people be like, "Great, love that you
[L305] [09:59.44] solved the problem." And then I have to
[L306] [10:00.40] do nothing. I just say yes. Worked
[L307] [10:02.80] really well. I saw like in the career
[L308] [10:04.88] note that you wrote about this promotion
[L309] [10:06.72] that you'd also reviewed over 1,600
[L310] [10:12.16] uh diffs in a half and that comes out to
[L311] [10:14.80] around like 14 diffs per workday. Why
[L312] [10:18.48] did you spend so much time also
[L313] [10:20.40] reviewing code?
[L314] [10:22.48] I think code review is super undervalued
[L315] [10:25.36] and I still do a ton of it. It's really
[L316] [10:27.68] valuable because you can influence other
[L317] [10:29.36] engineers in an organic way, right?
[L318] [10:31.68] Someone's like, "Adam, what's your
[L319] [10:33.12] message to other engineers at the
[L320] [10:34.48] company? What do you want to change?"
[L321] [10:35.60] I'm like, "I I don't know." But if I see
[L322] [10:38.24] a concrete diff and I'm like, "I don't
[L323] [10:39.92] like how they're doing this and here's
[L324] [10:41.44] why." It gives me a perfect opening to
[L325] [10:43.60] to get into it. However, I also try to
[L326] [10:46.80] be a very flexible different reviewer,
[L327] [10:48.56] right? I feel like there were some
[L328] [10:49.60] different reviewers who had that
[L329] [10:51.52] attitude of like, I'm going to help
[L330] [10:52.48] other engineers and then they were very
[L331] [10:53.84] inflexible. Anytime they saw any little
[L332] [10:55.60] thing they didn't like, reject. My view
[L333] [10:58.16] was like, "All right, I see what you're
[L334] [11:00.08] doing and why you're doing it this way.
[L335] [11:01.84] Here's my concern." And then either
[L336] [11:04.08] like, "I'm gonna let you do what you
[L337] [11:05.52] want if you really feel strongly, but
[L338] [11:07.52] here's what I would do differently next
[L339] [11:08.72] time." Or I'd be like, "Let's talk about
[L340] [11:10.88] how to redo your work to accomplish
[L341] [11:14.08] whatever concern I have." basically hold
[L342] [11:16.96] their hand through the process if if I
[L343] [11:18.72] can because I feel like that's a great
[L344] [11:20.80] way to, you know, now they're gonna
[L345] [11:23.60] hopefully if they're convinced by my
[L346] [11:25.28] argument, they're going to hold that
[L347] [11:27.28] same change in how they operate for
[L348] [11:30.00] their own future work and in all the
[L349] [11:31.52] future code review they do. It's like
[L350] [11:32.88] viral, right? And you see this would
[L351] [11:34.80] would spread through the code reviews
[L352] [11:36.16] that they did. So, I thought it was a
[L353] [11:38.32] really great way to like get my opinions
[L354] [11:40.40] out there and have those debates in a
[L355] [11:42.24] really structured format.
[L356] [11:43.76] >> Given that you've done just such an
[L357] [11:45.44] absurd volume of diff reviews, what
[L358] [11:47.76] makes a good diff comment versus a bad
[L359] [11:50.72] one in your opinion?
[L360] [11:52.08] >> Talk through why you care about what you
[L361] [11:55.12] are nitpicking and not just what to
[L362] [11:57.84] change, right? Don't say change X to Y.
[L363] [11:59.92] Say, hey, X has some problems, so I
[L364] [12:02.72] really want you to use Y instead. But if
[L365] [12:04.72] you really feel strongly if there's
[L366] [12:06.00] something I'm missing, then you can go
[L367] [12:07.20] ahead and use X. Right? The other thing
[L368] [12:09.12] I was always open to in different review
[L369] [12:10.64] comments was the fact that I might be
[L370] [12:12.00] missing context. And that's still the
[L371] [12:13.44] diff author's fault, maybe because like
[L372] [12:16.56] your diff should contain enough context
[L373] [12:18.56] for anyone to review it on its own
[L374] [12:20.40] merits, but I'd often be like, "Hey, I
[L375] [12:22.56] don't understand why you're doing it
[L376] [12:23.68] this way. I want you to do it this way
[L377] [12:25.68] instead, but is there some missing
[L378] [12:27.60] context that would change my mind? If
[L379] [12:29.04] so, fill me in and put it in your diff
[L380] [12:31.12] summary." which again I feel like makes
[L381] [12:33.60] sure that if I'm making a stupid mistake
[L382] [12:35.44] which happens I don't look like a total
[L383] [12:38.40] idiot who's just like getting it wrong.
[L384] [12:41.12] It really helps. So moving on to like
[L385] [12:43.76] you know E7 promo or the senior staff
[L386] [12:46.08] promo. I know that the main project that
[L387] [12:48.48] kind of drove that was component kit.
[L388] [12:50.80] Can you give some context on the story
[L389] [12:53.04] behind component kit?
[L390] [12:54.96] >> The years all blur together at this
[L391] [12:56.80] point but this was like 2014 maybe. We
[L392] [12:59.52] had a very large and complex product,
[L393] [13:02.32] Facebook newsfeed, which was growing and
[L394] [13:04.80] growing and growing so fast because the
[L395] [13:07.04] company hired lots of new engineers and
[L396] [13:08.96] they stuffed everyone on newsfeed
[L397] [13:10.56] because that was the hot product at the
[L398] [13:11.92] time. So it was basically falling apart,
[L399] [13:14.16] right? We had constant crashes, constant
[L400] [13:16.80] layout bugs where like content would be
[L401] [13:18.64] overlapping in weird ways and it was a
[L402] [13:21.20] struggle to keep performance good. I
[L403] [13:23.92] can't claim credit for the idea again
[L404] [13:25.60] here. It was Lee Byron who was I think
[L405] [13:28.40] my manager at the time but was for a
[L406] [13:30.96] long time a very senior engineer at the
[L407] [13:32.64] company and co-invented GraphQL and he
[L408] [13:36.32] had done a lot of work with React on the
[L409] [13:38.24] web which was relatively new then too
[L410] [13:40.48] even on the web it was new and he was
[L411] [13:42.32] like you know what we really need this
[L412] [13:45.04] React concept but for iOS development at
[L413] [13:48.08] this time React Native either didn't
[L414] [13:50.24] exist or was just a prototype and so Lee
[L415] [13:53.60] told me like why don't you just take
[L416] [13:55.04] some time and think about how would the
[L417] [13:57.28] concepts of react work in an iOS first
[L418] [14:01.12] way and component kit was my answer to
[L419] [14:04.00] that question. So it uses the same
[L420] [14:06.56] concepts of like components
[L421] [14:07.92] immutability, rerender everything
[L422] [14:10.48] conceptually at least when anything
[L423] [14:12.40] changes
[L424] [14:13.92] view reconciliation, right? So you're
[L425] [14:15.68] not directly managing UI views. You're
[L426] [14:17.76] instead just stating, hey, I want there
[L427] [14:19.60] to be a button that has this caption.
[L428] [14:21.76] The framework takes care of creating the
[L429] [14:23.44] actual button view. And I'm pretty proud
[L430] [14:26.40] of the balance that it struck in terms
[L431] [14:28.72] of the syntax was appealing, the
[L432] [14:30.64] performance was amazing, and it allowed
[L433] [14:33.84] us to solve a problem that we really
[L434] [14:35.44] needed to solve as a business. And
[L435] [14:37.60] again, this was 2014, so years before
[L436] [14:39.92] Swift UI. Swift didn't exist yet. Swift
[L437] [14:42.00] UI didn't exist yet. React Native didn't
[L438] [14:44.16] exist yet. It was a very early on the
[L439] [14:46.08] scene. And it did take some convincing
[L440] [14:49.44] of other iOS engineers because it was
[L441] [14:51.76] still a very alien way to write code on
[L442] [14:53.92] iOS. But once convinced, everybody loved
[L443] [14:56.64] it. Everybody thought this is a really
[L444] [14:57.92] great way to write the UI for a complex
[L445] [15:00.72] product like Facebook newsfeed. So the
[L446] [15:03.44] big challenge there was inventing the
[L447] [15:04.72] framework, getting it adopted in
[L448] [15:06.40] newsfeed and then getting it adopted
[L449] [15:08.24] everywhere else. So I had lots of lots
[L450] [15:10.16] of work to do. How did you convince
[L451] [15:12.24] people because you know this declarative
[L452] [15:14.08] framework was such a different way of
[L453] [15:16.40] doing things. I imagine there was a lot
[L454] [15:18.16] of push back. How did you you drive
[L455] [15:21.20] those difficult conversations?
[L456] [15:23.68] Tons of push back. Um some people were
[L457] [15:26.16] convinced when they saw concrete
[L458] [15:27.84] examples of hey here's what the same
[L459] [15:31.60] code would look like in component kit.
[L460] [15:33.28] It's now like a third as much code. Some
[L461] [15:36.48] people were convinced when they could
[L462] [15:37.44] see the performance, right? Oh, look, it
[L463] [15:38.96] allows us to render all the viewed
[L464] [15:41.68] hierarchies on a background thread and
[L465] [15:43.36] then only do the minimal amount of work
[L466] [15:44.72] on the main thread. And they were like,
[L467] [15:45.76] that's really cool. But there were
[L468] [15:47.52] plenty of people who were hold outs even
[L469] [15:49.12] then and we had to call in mediators,
[L470] [15:51.92] right? Basically, like there were other
[L471] [15:53.12] senior engineers at the time because
[L472] [15:54.72] when I was inventing component kit, I
[L473] [15:56.16] was an IC6. there were other more senior
[L474] [15:58.40] engineers who would you know get us to
[L475] [16:00.96] huddle up and try to talk through how do
[L476] [16:03.92] we find a path forward that we can all
[L477] [16:06.40] agree on and I think Lee Byron was very
[L478] [16:08.72] involved in these conversations. I know
[L479] [16:10.72] uh Alan Kennaro was a senior engineer at
[L480] [16:12.72] the time who was very involved in this
[L481] [16:14.32] helping us like mediate between these
[L482] [16:16.40] different groups but I think the fact
[L483] [16:18.56] that React had a lot of cred as a
[L484] [16:20.96] framework at the company on the web
[L485] [16:22.32] really helped right because we could
[L486] [16:23.44] point and be like look at what React is
[L487] [16:25.04] doing on the web. We want to do the same
[L488] [16:26.40] on iOS. There aren't any really good
[L489] [16:28.88] reasons why we can't do it. It's not
[L490] [16:30.56] impossible to do on the platform. We we
[L491] [16:32.08] have proven we can. So get on board. And
[L492] [16:35.20] I acknowledge the downsides of component
[L493] [16:36.80] kit, right? It's by now it's very creaky
[L494] [16:39.28] and old because it was a C++ objective
[L495] [16:42.16] C++ framework. Now we have a Swift API
[L496] [16:44.64] for it. That's great. But still at the
[L497] [16:47.28] time the weirdnesses of component kit
[L498] [16:49.60] were even then somewhat unappealing. But
[L499] [16:52.64] my pitch was always, yes, it's a little
[L500] [16:54.88] weird. It's not the usual way of writing
[L501] [16:56.56] code in iOS, but here's all the amazing
[L502] [16:58.56] things we get. That's why you should do
[L503] [17:00.40] it. So that's the pitch that we had to
[L504] [17:03.12] make again and again and again to
[L505] [17:04.64] skeptical iOS engineers. Is there
[L506] [17:06.40] anything that you learned in trying to
[L507] [17:08.48] convince these people that were very
[L508] [17:10.40] against this this approach that is kind
[L509] [17:13.12] of useful and general learning for
[L510] [17:15.28] anyone that's trying to have some new
[L511] [17:17.60] developer offering and convince people
[L512] [17:19.52] to use it? Allies are super useful,
[L513] [17:21.76] right? Um, I still remember uh there
[L514] [17:23.52] were some engineers like Clement Gendmer
[L515] [17:25.28] and Greg Mech who carried a lot of
[L516] [17:27.92] weight in the company and they saw it
[L517] [17:29.84] and liked it. So great, I wasn't alone
[L518] [17:31.68] and they could help convince other
[L519] [17:33.20] people because, you know, I have one way
[L520] [17:35.20] of convincing people which isn't always
[L521] [17:36.72] effective and they have other ways of
[L522] [17:37.92] convincing people which often were more
[L523] [17:39.52] effective. And so it was nice to be able
[L524] [17:41.44] to break it down and like, you know, see
[L525] [17:42.96] the different ways that this discussion
[L526] [17:44.64] happened over time. There were
[L527] [17:46.16] opportunities for compromise. The other
[L528] [17:48.00] big alternative out there was this
[L529] [17:49.60] framework called panels which hadn't
[L530] [17:50.96] really gotten off the ground yet but was
[L531] [17:52.32] supposed to be like the next way to
[L532] [17:53.76] write UI at Facebook and I knew them
[L533] [17:57.52] really well because one of them was like
[L534] [17:58.88] my mentor and so I you know was very
[L535] [18:01.36] very close to Jonathan Dan the guy
[L536] [18:03.44] behind panels and boy they had a really
[L537] [18:05.92] hard time because they felt like they
[L538] [18:07.20] were developing the next thing and then
[L539] [18:08.32] I came along was like actually let's do
[L540] [18:09.60] component kit wasn't so good but we
[L541] [18:12.08] found a way to compromise and we adopted
[L542] [18:13.68] some of the panels data source
[L543] [18:15.68] technology to power component kit which
[L544] [18:17.44] was a good compromise and allowed us all
[L545] [18:18.88] to feel like we had a win. Instead of
[L546] [18:20.56] sticking to your guns and every little
[L547] [18:21.76] thing, if you can find a way to bring
[L548] [18:23.36] people into your fold, into the tent,
[L549] [18:25.52] that's really really helpful.
[L550] [18:26.80] >> With all that push back, did you ever
[L551] [18:28.80] doubt the direction that you're going
[L552] [18:30.48] in?
[L553] [18:31.60] >> No, I was very convinced that this was
[L554] [18:33.12] the right call for Facebook newsfeed. I
[L555] [18:35.20] will say, and this goes for all
[L556] [18:36.80] declarative UI frameworks, React, Swift
[L557] [18:38.64] UI, component kit. They're really good
[L558] [18:41.20] at some things, like a Facebook newsfeed
[L559] [18:42.88] is the perfect thing for it because it's
[L560] [18:44.64] like a scrolling list of complicated
[L561] [18:47.28] multi-level nesting and it's mostly
[L562] [18:49.76] static, right? There's some animation
[L563] [18:51.04] and cool stuff, but mostly it just is
[L564] [18:52.56] like a list of stuff. That's the perfect
[L565] [18:55.04] application for it. When you look at
[L566] [18:57.20] like a super dynamic drag and drop
[L567] [18:58.96] interface, h maybe not the right thing
[L568] [19:01.68] for it, right? Maybe not the ideal case
[L569] [19:03.60] anyway. you can make it work, but it's
[L570] [19:05.04] not going to be incredibly natural. So,
[L571] [19:07.20] I'm very aware that like there are
[L572] [19:09.20] trade-offs to these different paradigms.
[L573] [19:12.32] And I wasn't drinking the Kool-Aid in
[L574] [19:14.56] terms of telling everyone component
[L575] [19:15.76] kit's the only way to write UIs on
[L576] [19:17.28] Facebook. Like that should be the, you
[L577] [19:18.64] know, our only option is component kit.
[L578] [19:21.04] Uh, no. But in general, for what we
[L579] [19:23.36] wanted to use it for, yes, I was very
[L580] [19:24.80] convinced that it was the right path
[L581] [19:26.24] forward. You know, the next project you
[L582] [19:28.08] worked on was component script. What was
[L583] [19:31.04] the motivation behind that project? And
[L584] [19:34.00] you know what's the story behind it?
[L585] [19:36.16] >> So component script was interesting
[L586] [19:37.44] because it was a total and complete
[L587] [19:38.96] failure and I worked on it for like two
[L588] [19:40.80] years. At the time, my manager was a guy
[L589] [19:44.64] named Ari Grant who was a force of
[L590] [19:46.72] nature, right? He was like all over the
[L591] [19:48.32] place, very busy,
[L592] [19:50.96] carried a lot of influence. And Ari felt
[L593] [19:53.36] really strongly that we needed to get
[L594] [19:54.88] out of the perplatform silo, right? So
[L595] [19:57.68] like iOS had component kit, Android had
[L596] [19:59.92] a React and Component kit inspired by
[L597] [20:02.16] then called WHO. But this meant we were
[L598] [20:04.16] writing everything multiple times,
[L599] [20:05.36] right? We had to write it in component
[L600] [20:06.56] kit for iOS, we had to write it in
[L601] [20:07.92] Android. He wanted to have a
[L602] [20:09.20] crossplatform solution. React Native was
[L603] [20:11.20] not that solution and we knew that at
[L604] [20:13.20] this time we had tried React Native and
[L605] [20:14.64] it didn't go well. The reason was in my
[L606] [20:16.88] opinion, this is just my opinion, React
[L607] [20:18.80] Native is designed to be in charge of
[L608] [20:20.40] the entire app. It works really well if
[L609] [20:22.08] your entire app is React Native or if
[L610] [20:24.40] you have entire app React Native and
[L611] [20:25.92] then small little pieces on the very
[L612] [20:27.76] bottom are native or bridged. Where it
[L613] [20:30.72] doesn't work is the way we wrote
[L614] [20:32.80] software at that time which was we had
[L615] [20:35.44] this large complex native app and we
[L616] [20:38.16] wanted to slot in small pieces of
[L617] [20:40.32] crossplatform in different areas right
[L618] [20:42.56] so like oh maybe this little square on
[L619] [20:44.48] this screen is rendered using JavaScript
[L620] [20:47.36] maybe this tab is rendered in JavaScript
[L621] [20:50.48] and this tab is native React Native
[L622] [20:52.24] could not do that for us at the time
[L623] [20:54.48] they've done a lot of architectural
[L624] [20:55.60] changes to React Native in the last 10
[L625] [20:57.52] years since then and maybe it's better
[L626] [20:58.88] at it now but at the
[L627] [21:00.32] didn't really work. So we wanted
[L628] [21:02.72] crossplatform. We knew React Native was
[L629] [21:04.72] not it. What could we do? And so Ari
[L630] [21:07.12] asked me to go and work on this. And I
[L631] [21:09.28] at the time it was like okay this is the
[L632] [21:10.80] next nudge, right? Like we Byron nudged
[L633] [21:12.80] me to work on React for iOS. That was
[L634] [21:15.28] component kit. Great. This is the next
[L635] [21:16.80] nudge work on crossplatform for our UI
[L636] [21:20.32] rendering frameworks that we use on iOS
[L637] [21:21.76] and Android. And so I came up with a
[L638] [21:23.76] framework called component script. The
[L639] [21:26.08] idea was basically at first I took the
[L640] [21:28.08] React APIs, the actual React
[L641] [21:30.16] implementation. I said, "What if we just
[L642] [21:31.44] made a different React Native, right?"
[L643] [21:32.72] So exactly like React Native except that
[L644] [21:34.40] it works on top of component kit and
[L645] [21:35.68] width because that's what we already
[L646] [21:36.96] have. This turned out to be too
[L647] [21:38.72] difficult. React had a really large
[L648] [21:40.88] surface area and a very complex surface
[L649] [21:42.80] area and trying to make that work on on
[L650] [21:45.44] component kit and with it was too
[L651] [21:46.80] challenging. So I was like, "All right,
[L652] [21:48.16] I'll do a smaller paired down API that
[L653] [21:51.76] feels just like React, but actually is
[L654] [21:54.08] simpler and make that work on top of
[L655] [21:56.08] component kit and litho." And I made it
[L656] [21:57.84] work. It was a real framework. People
[L657] [21:59.60] built real features on it. You could
[L658] [22:01.28] build full screens. You could build
[L659] [22:02.72] individual units. You could do all kinds
[L660] [22:04.56] of, you know, birectional embeddings.
[L661] [22:06.48] You could have a native screen that had
[L662] [22:07.52] a component script unit which had a
[L663] [22:09.84] native component inside of that. You
[L664] [22:11.52] could have a component script screen
[L665] [22:12.88] which had a native section. All this
[L666] [22:14.80] stuff, really cool features.
[L667] [22:17.04] And for me, it was a real learning
[L668] [22:19.12] experience because I learned that just
[L669] [22:20.80] because it was technically excellent
[L670] [22:22.72] didn't mean it was going to win. It
[L671] [22:25.68] checked all the boxes we needed in terms
[L672] [22:27.52] of interop and type safety, but it
[L673] [22:31.04] didn't win and didn't come close to
[L674] [22:32.56] winning because there were many other
[L675] [22:34.16] factors that I didn't take into account.
[L676] [22:37.52] So, a great example of writing a lot of
[L677] [22:39.28] code and doing a lot of technical work
[L678] [22:41.12] doesn't mean that it's going to win. I
[L679] [22:43.36] mean, if we were to kind of postmortem
[L680] [22:45.92] why it didn't win, what are the things
[L681] [22:48.40] that you did well and what are the
[L682] [22:50.40] things that maybe could have gone
[L683] [22:51.68] better?
[L684] [22:52.24] >> Um, I mean, doing well, I just mentioned
[L685] [22:54.40] it did check it checked all the
[L686] [22:55.92] technical boxes that we as in like the
[L687] [22:58.32] core product infra group cared about,
[L688] [23:01.12] right? Like it was type safe. It
[L689] [23:04.08] integrated with GraphQL and component
[L690] [23:06.08] kit and WHO, our existing native
[L691] [23:07.52] frameworks. It was birectional. So, you
[L692] [23:09.44] would never be suddenly cut off. There
[L693] [23:11.36] would never be a point where you're
[L694] [23:12.24] like, "Oh, I just need to embed this
[L695] [23:13.60] native component and I can't do it." No,
[L696] [23:15.60] you could always do it. The mistakes
[L697] [23:17.28] were number one, I wasn't really aiming
[L698] [23:20.80] at a particular target engineer, right?
[L699] [23:23.28] So, React Native was focused on like web
[L700] [23:25.44] engineers who wanted to write for
[L701] [23:26.64] mobile. Component kit was focused on,
[L702] [23:29.52] hey, we have iOS engineers that already
[L703] [23:31.44] know how to write iOS code. Let's let
[L704] [23:34.32] them write iOS code, but have excellent
[L705] [23:36.72] performance.
[L706] [23:38.40] Component script is like, hey, you can
[L707] [23:39.76] write JavaScript, but it's not React.
[L708] [23:41.84] So, like iOS engineers were like, I
[L709] [23:43.28] don't want to learn a whole new
[L710] [23:44.16] language. I don't want to learn
[L711] [23:45.12] JavaScript. And JavaScript engineers
[L712] [23:47.28] were like, I'll use React Native. I
[L713] [23:48.88] don't want to touch this like weird not
[L714] [23:50.88] React API. No thank you. So, we were
[L715] [23:53.84] kind of stuck. Number two is that like
[L716] [23:56.00] we on the product infrastructure group
[L717] [23:57.52] really cared about GraphQL. We were
[L718] [23:58.88] like, hey, we want data consistency
[L719] [24:00.64] everywhere. So, this framework needs to
[L720] [24:02.16] be based on GraphQL. But it turns out
[L721] [24:04.32] GraphQL can be kind of a pain sometimes,
[L722] [24:06.96] right? Especially at that time, GraphQL
[L723] [24:10.24] tooling was slow and a lot of uh a lot
[L724] [24:13.04] of hassle. We've fixed it a lot since
[L725] [24:15.20] then, but at the time it was bad. And so
[L726] [24:18.08] trying to build on top of this slow,
[L727] [24:21.60] janky native GraphQL stack really slowed
[L728] [24:23.76] us down. Meanwhile, there was another
[L729] [24:25.76] framework out there that was, you know,
[L730] [24:27.20] coming in with a server-driven sort of
[L731] [24:29.52] UI approach. And their solution was
[L732] [24:32.00] like, don't worry about data
[L733] [24:32.96] consistency.
[L734] [24:34.48] What if we just didn't do it? And we
[L735] [24:36.08] were all horrified. were like, "What?
[L736] [24:37.44] You don't have data consistency?" So, if
[L737] [24:39.36] you like a post on one screen and you go
[L738] [24:41.04] to another screen, it won't show you
[L739] [24:42.56] that the post is liked. And the answer
[L740] [24:45.20] was yes. 60% of the time, 80% of the
[L741] [24:48.72] time, products just don't care. And for
[L742] [24:50.72] the 20% that do care, you could hack
[L743] [24:52.96] something in there that makes it work.
[L744] [24:54.80] So, we were pretty horrified by not
[L745] [24:56.24] using GraphQL, but it that was a huge
[L746] [24:58.40] advantage if you could just skip all
[L747] [25:00.48] that stuff. But, I refused to compromise
[L748] [25:02.40] and that was a problem. And then
[L749] [25:04.00] finally, I went really wide. I was like,
[L750] [25:06.24] "All right, I'm just going to talk to
[L751] [25:07.28] all engineers, all mobile engineers, and
[L752] [25:09.76] be like, you guys should all try out
[L753] [25:10.96] component script." And this meant that I
[L754] [25:12.88] got little pings of interest all over
[L755] [25:14.40] the place. Because there were a few
[L756] [25:16.16] engineers here and there that were like,
[L757] [25:17.28] "Sure, I'll try JavaScript. Sure, I'll
[L758] [25:18.80] try crossplatform." But there wasn't any
[L759] [25:21.36] individual team that was like, "Yes,
[L760] [25:23.36] this is how we want to write products
[L761] [25:25.20] from now on." And so that meant that it
[L762] [25:27.44] never went anywhere, right? Individual
[L763] [25:29.12] engineers would try individual little
[L764] [25:30.64] things here and there, but that was not
[L765] [25:32.16] going to get any momentum. Funny thing
[L766] [25:34.16] was just when I finally pulled the plug
[L767] [25:36.00] on component script the group's team was
[L768] [25:37.68] like oh we just decided we were going to
[L769] [25:39.12] go all in on component script and I was
[L770] [25:40.56] like oh man no [laughter] u but even
[L771] [25:42.88] that would not have been enough momentum
[L772] [25:44.40] right it was too little too late so you
[L773] [25:46.32] wrote about this retrospection it's you
[L774] [25:48.64] know very detailed one of the best you
[L775] [25:50.88] know retrospectives I've I've read why
[L776] [25:53.60] did you publish that so publicly what
[L777] [25:57.28] was the motivation behind it
[L778] [25:59.52] >> I don't recall it might have been
[L779] [26:02.00] encouraged that I write it, but I
[L780] [26:03.76] certainly wanted to write it. It was
[L781] [26:04.96] cathartic to talk about what went wrong.
[L782] [26:07.52] And even at the time, I had a
[L783] [26:09.36] reputation, right? People who knew who I
[L784] [26:11.04] was. So, everyone would always be like,
[L785] [26:12.32] "Hey, how's that component script thing
[L786] [26:13.68] going?" And the postmortem was a
[L787] [26:15.28] convenient way for me to rip the
[L788] [26:16.56] band-aid off and be candid about, "Hey,
[L789] [26:18.40] it didn't work and here's why." And not
[L790] [26:20.08] have to constantly rehash that
[L791] [26:22.00] conversation over and over and over. Um,
[L792] [26:24.32] but also I hope that it would influence
[L793] [26:26.72] the way that people did stuff at the
[L794] [26:28.24] company in the future, right? Like
[L795] [26:29.60] hopefully no one made the same mistake
[L796] [26:31.04] after that if they read my postmortem or
[L797] [26:32.88] at least they were aware of what they
[L798] [26:34.16] were walking into. And you know in this
[L799] [26:36.08] case you drove a very ambitious project
[L800] [26:39.12] and it did fail in the end when it comes
[L801] [26:42.08] to performance reviews in a half where
[L802] [26:44.64] something like this is happening or a
[L803] [26:46.24] year where something like this is
[L804] [26:47.36] happening. How does that play out and
[L805] [26:49.76] should people be worried about you know
[L806] [26:52.08] their projects getting cancelled or
[L807] [26:53.76] things like that?
[L808] [26:54.72] >> The thing that made me realize it needed
[L809] [26:56.24] to be cancelled is that I got a meets
[L810] [26:57.92] most. So performance did its job there.
[L811] [27:00.48] >> My manager at the time did the right
[L812] [27:02.72] thing and was like this is not working.
[L813] [27:04.72] >> He was also a new manager for me. So I
[L814] [27:06.96] think he like
[L815] [27:08.64] >> could see it with fresh eyes and be like
[L816] [27:10.24] this is not going to work. And then when
[L817] [27:13.04] I did cancel it, I like to think I did
[L818] [27:15.28] it in the right way, which is there were
[L819] [27:17.12] products and features written in
[L820] [27:18.80] component script and I helped those
[L821] [27:20.08] teams migrate back to native code or to
[L822] [27:22.16] react native or whatever they wanted and
[L823] [27:24.96] I completely deleted the framework. I
[L824] [27:26.72] didn't weave it as like, you know, oh,
[L825] [27:29.28] this one product is still on component
[L826] [27:30.88] script, so we have to weave it around
[L827] [27:31.84] forever and someone will have to clean
[L828] [27:33.28] it up someday. No, I was like, I'm
[L829] [27:35.36] driving this all the way and I'm
[L830] [27:36.40] deleting the code is going to be gone
[L831] [27:37.68] from the repo, which I think garnered
[L832] [27:39.44] some goodwill because it showed others
[L833] [27:41.60] this is the right way to clean up after
[L834] [27:42.96] your mess. Um, so I feel like I got in
[L835] [27:46.08] if anything a positive bump after the
[L836] [27:48.00] fact, right? Like there was enough
[L837] [27:50.48] relief of like, all right, this showed
[L838] [27:52.00] people how to wind up wind down a
[L839] [27:53.92] project that isn't working out. and he
[L840] [27:55.84] posted publicly about it show talking
[L841] [27:58.24] about the lessons learned and there's no
[L842] [28:00.16] mass left behind. So if anything I feel
[L843] [28:02.40] like it helped in the in the immediate
[L844] [28:04.72] aftermath. So if anyone is like staring
[L845] [28:06.32] down the barrel of like I think my
[L846] [28:07.76] framework's not going well but I'm
[L847] [28:09.36] afraid to kill it. You might get more
[L848] [28:10.64] goodwill from killing it responsibly
[L849] [28:12.72] than just like dragging it out and
[L850] [28:14.56] constantly waiting until it's too late.
[L851] [28:17.60] Were there signs that like looking back
[L852] [28:20.48] you could have maybe avoided some of the
[L853] [28:23.44] pain of I don't know meets most or you
[L854] [28:26.08] know kind of like it going on as long as
[L855] [28:28.08] it did.
[L856] [28:28.96] >> Yeah. I mean look there were there was
[L857] [28:31.36] it was a two-year project and for the
[L858] [28:32.96] last year I knew it wasn't going right
[L859] [28:34.72] and I should have listened to my gut,
[L860] [28:36.16] right? I there were some literally
[L861] [28:37.68] sleepless nights. Not a lot but like
[L862] [28:39.60] some where I was like this is it doesn't
[L863] [28:40.96] feel right. It's not going well. I don't
[L864] [28:42.48] understand what to do. And I'm a coding
[L865] [28:45.60] machine. So my reaction was I just need
[L866] [28:47.12] to write more code. I just need to help
[L867] [28:48.88] more features convert and it'll suddenly
[L868] [28:51.12] take off. And I should have listened
[L869] [28:52.48] instead to that part of my gut that was
[L870] [28:55.12] telling me this is not going to work
[L871] [28:56.32] out. Just go do something you love and
[L872] [28:58.64] find a different way to have impact and
[L873] [29:01.04] uh that would have been much better for
[L874] [29:02.64] me in the short and long run.
[L875] [29:04.80] >> You said before that you know for sure
[L876] [29:07.20] you you never wanted to try management
[L877] [29:09.36] and it was not right for you. Um, for
[L878] [29:11.76] someone who's considering that kind of
[L879] [29:13.20] decision, how did you know that
[L880] [29:15.52] management's not right for you?
[L881] [29:17.36] >> I like writing code. I really like
[L882] [29:18.96] writing code a lot. And as a manager,
[L883] [29:21.20] you can't write codes. So, I mean, for
[L884] [29:22.40] me, it's a no-brainer, right? I'm also
[L885] [29:24.32] just I'm
[L886] [29:26.24] less good at the non-code related parts
[L887] [29:30.56] of the job. So, like driving alignment
[L888] [29:33.52] and writing docs, I'm just not good at
[L889] [29:35.44] that stuff. And so, for me, I'm like,
[L890] [29:37.12] yeah, I don't want to touch that. And
[L891] [29:38.48] finally, I feel like I'm very good at
[L892] [29:39.84] communication with other engineers in a
[L893] [29:41.76] technical role. Like I'm very good at
[L894] [29:43.12] like, hey, we need to solve this
[L895] [29:44.16] technical problem. Let's all get on the
[L896] [29:45.44] same page about how to solve it. I don't
[L897] [29:47.44] think I'm as good at doing that when I'm
[L898] [29:49.04] not quite when I'm more removed from the
[L899] [29:51.28] problem, right? Managers have to lot of
[L900] [29:52.56] do a lot of direction setting and
[L901] [29:56.16] influencing people without directly
[L902] [29:58.08] pointing to like this line of code is
[L903] [29:59.44] the problem and that I think I'm less
[L904] [30:01.28] good at. So for me, I always knew
[L905] [30:04.16] management is not for me. Uh but it
[L906] [30:06.16] depends on the person. Obviously, I'm a
[L907] [30:07.52] pretty extreme case.
[L908] [30:09.04] >> What about um picking the domain that
[L909] [30:11.04] you went with? So, from what I see in
[L910] [30:12.80] your career, it's almost entirely on the
[L911] [30:15.04] iOS side with some crossplatform work.
[L912] [30:18.08] Well, how did you align on iOS? And is
[L913] [30:20.72] that something that you feel strongly
[L914] [30:22.32] about being tied to or is that just
[L915] [30:24.96] where things have taken you?
[L916] [30:26.40] >> That's where things have taken me. I
[L917] [30:28.56] don't change around a lot. I've never
[L918] [30:30.16] really changed teams once at this
[L919] [30:31.84] company, right? like I've like been
[L920] [30:33.60] shifted on to different teams as part of
[L921] [30:35.44] reorgs, but I don't know. I just kind of
[L922] [30:38.24] roll with the punches and I like what
[L923] [30:39.44] I'm doing. I feel like I like the team,
[L924] [30:41.28] so why mess it up? I admire engineers
[L925] [30:44.00] that are like, you know what, I want to
[L926] [30:45.12] go see what this AI thing is about. I'm
[L927] [30:46.48] going to go check it out. Or like, oh
[L928] [30:47.76] man, I really want to go work on ARVR.
[L929] [30:50.00] That's not me. I knew I liked mobile and
[L930] [30:52.88] I felt like I was getting the right
[L931] [30:55.52] opportunities to work on stuff I cared
[L932] [30:57.12] about. So, I just kept rolling with it.
[L933] [30:58.96] And I think it has worked out really
[L934] [31:00.16] well for me because it allowed me to
[L935] [31:01.68] build deep knowledge expertise about how
[L936] [31:06.08] all different parts of our system work.
[L937] [31:07.92] Right? If you want to know the guts of
[L938] [31:09.28] the graphical codegen or value object
[L939] [31:11.84] generation or buck or all these things,
[L940] [31:13.84] I know what's up. And so it's really
[L941] [31:16.24] helped me get really deep in this
[L942] [31:18.16] particular domain. And that means I have
[L943] [31:19.60] a lot of knowledge about it that helps
[L944] [31:21.92] answer questions from others. Very
[L945] [31:23.84] useful. Would I do mobile if I was a
[L946] [31:26.96] brand new engineer today? Maybe not.
[L947] [31:28.64] Maybe I do AI because that seems like
[L948] [31:30.16] the hot stuff, right? Or I don't know
[L949] [31:31.44] what else. Uh but I don't feel too bad
[L950] [31:34.56] about sticking with it. You you talked
[L951] [31:36.56] about the technical depth. Let's say
[L952] [31:38.32] someone's goal was to be like you. They
[L953] [31:40.64] they really wanted to, you know, super
[L954] [31:43.12] aggressively pursue the high IC career
[L955] [31:45.84] path. They want to go IC9 or bust. Do
[L956] [31:48.88] you think that technical depth is better
[L957] [31:51.84] than breath for becoming the highest
[L958] [31:54.32] levels of uh senior IC? I I mean it
[L959] [31:57.04] depends on how you operate. I've seen
[L960] [31:58.64] lots of different engineers that operate
[L961] [32:00.00] in different ways. I will say I have
[L962] [32:01.60] breath and depth, right? As in like not
[L963] [32:03.52] that you know it's perfect. It's not
[L964] [32:05.68] like I only know mobile though, right?
[L965] [32:07.12] Like I know ex a lot about how buck
[L966] [32:08.96] operates. I know a lot about how uh
[L967] [32:11.36] GraphQL
[L968] [32:12.96] schema works. And so for me, the thing
[L969] [32:15.20] that helped me personally worked for me,
[L970] [32:17.68] maybe not for everyone, when I run into
[L971] [32:19.84] a problem, instead of being like, "All
[L972] [32:20.96] right, got to go talk to the GraphQL
[L973] [32:22.32] team." I'm like, "Screw it. I'm just
[L974] [32:23.92] going to figure out what the problem is.
[L975] [32:25.52] I'm going to dive eight levels deep into
[L976] [32:27.28] their codegen guts until I find the
[L977] [32:29.76] problem and then I'll either fix it
[L978] [32:31.60] myself and now I know GraphQL codegen or
[L979] [32:34.08] I will show up to the GraphQL team and
[L980] [32:35.60] I'll be like hey ran into this problem
[L981] [32:37.60] debugged it eight levels deep here's the
[L982] [32:39.36] problem how do I fix it which impresses
[L983] [32:42.16] the GraphQL team means that I'm not
[L984] [32:44.24] taking up all their time and I've
[L985] [32:45.84] learned something new about a new system
[L986] [32:47.52] and if you keep doing that enough then
[L987] [32:50.00] you will discover a lot about a lot of
[L988] [32:52.16] different systems and you'll understand
[L989] [32:53.36] them and that'll give you so much
[L990] [32:55.60] knowledge and so much it's like a
[L991] [32:57.28] superpower to be able to dive into all
[L992] [32:58.96] these systems that you now know. It's
[L993] [33:01.36] also organic, right? We talked before
[L994] [33:02.96] about code review and how if you just
[L995] [33:04.48] review code that organically gives you
[L996] [33:06.96] actual discussions about how do we want
[L997] [33:09.36] to write our code? Same thing with this,
[L998] [33:11.68] right? Instead of being like, hm, which
[L999] [33:13.12] systems do I need to go learn for my
[L1000] [33:14.80] job? I'm like, they'll come to me,
[L1001] [33:16.88] right? I'm going to have a problem that
[L1002] [33:18.08] I run into. GraphQL is going to block my
[L1003] [33:20.32] code from landing. Great. Now I have a
[L1004] [33:22.56] reason to go delve into GraphQL code
[L1005] [33:24.40] genen. I'm not gonna study it from first
[L1006] [33:26.08] principles and be like well I should go
[L1007] [33:27.28] learn the graphical code genen systems
[L1008] [33:28.72] just because but when it comes up sure
[L1009] [33:31.36] I'll do that. A lot of people that get
[L1010] [33:33.60] promoted to these really high levels.
[L1011] [33:35.52] One thing I've noticed is the the
[L1012] [33:37.84] expectations become I guess scarier and
[L1013] [33:40.88] scarier for people or they they they get
[L1014] [33:42.88] there and they kind of get worried that
[L1015] [33:44.32] they can meet expectations. You know for
[L1016] [33:46.40] you as a IC9 and you're you're writing
[L1017] [33:49.44] code. How do you make sure that it's,
[L1018] [33:51.84] you know, IC9 code? Like there's this
[L1019] [33:54.88] does it, you don't worry about that.
[L1020] [33:56.56] I've flipped the switch off. I just
[L1021] [33:58.16] don't care. Uh I used to worry about
[L1022] [34:00.16] that too a lot. And then I was like, you
[L1023] [34:01.76] know what? I'm just going to do what I
[L1024] [34:02.96] love and I'm going to check in my check
[L1025] [34:05.52] in with my manager often to make sure
[L1026] [34:07.20] that I'm solving problems that need
[L1027] [34:08.56] solving, right? I'm not just going to go
[L1028] [34:09.76] work on something that doesn't matter.
[L1029] [34:11.68] But as long as I'm working on what's
[L1030] [34:13.12] important for my org and I like what I'm
[L1031] [34:16.00] doing, I'm just not going to worry about
[L1032] [34:17.52] it and I'm going to do it. And that has
[L1033] [34:19.84] served me really well, right? Uh
[L1034] [34:22.00] component script being the ex exception
[L1035] [34:23.84] where like eventually it was no longer
[L1036] [34:25.84] important for the company or the or that
[L1037] [34:28.00] was like someone needed to prod me to
[L1038] [34:29.60] realize that. But they prodded me and I
[L1039] [34:32.16] realized it and the problem was solved,
[L1040] [34:33.60] right? Like in some sense like getting a
[L1041] [34:35.04] meets most was freeing in the sense of
[L1042] [34:36.56] like well if that happens again I'll
[L1043] [34:37.76] know that like I went too deep and too
[L1044] [34:39.20] hard and didn't listen and now I go
[L1045] [34:41.36] listen and fix it. So yeah, my answer is
[L1046] [34:43.44] I just flip the switch off and don't
[L1047] [34:44.72] worry about it because that's
[L1048] [34:45.60] counterproductive. as a you know senior
[L1049] [34:48.08] IC you you are in forums with other
[L1050] [34:51.52] senior IC's and also you have a
[L1051] [34:54.32] viewpoint that others don't which you
[L1052] [34:56.00] could see what uh work is technically
[L1053] [34:58.64] difficult and exceptional you know what
[L1054] [35:00.72] are some other engineers that you think
[L1055] [35:02.64] are exceptional and what in your opinion
[L1056] [35:05.60] makes their work exceptional
[L1057] [35:07.84] >> I've got a list so I'm going to go down
[L1058] [35:09.60] the list
[L1059] [35:10.32] >> okay
[L1060] [35:11.12] >> I really admire Dustin Shahitapor who's
[L1061] [35:13.04] an engineer who works very much like me
[L1062] [35:15.44] he writes a lot of code. That's the part
[L1063] [35:17.76] of the job he enjoys. He and I have a
[L1064] [35:20.08] very similar working style. So, for that
[L1065] [35:21.52] reason, I get along with him great. Uh,
[L1066] [35:23.36] another engineer that I've worked on for
[L1067] [35:25.04] worked with for a very, very long time
[L1068] [35:26.64] is Wei Han, who joined the company on
[L1069] [35:29.36] the same day I did in 2012. Uh, and our
[L1070] [35:32.24] careers often over overlapped. We worked
[L1071] [35:33.84] together on a lot of things, including
[L1072] [35:35.28] component script for a while. And she is
[L1073] [35:38.16] many different archetypes. She does not
[L1074] [35:40.08] fit in one box, but she's she's more of
[L1075] [35:41.92] a fixer. She's very good at like, hey,
[L1076] [35:43.68] this metric is not right. what is the
[L1077] [35:45.68] deal? Which is something I can kind of
[L1078] [35:47.52] do, but she can really do. And so I love
[L1079] [35:49.60] someone that can dive. Again, it's like
[L1080] [35:51.44] diving 10 layers into systems you don't
[L1081] [35:53.20] know and figuring out what the hell is
[L1082] [35:55.04] going on here. She's great at that. He's
[L1083] [35:56.80] no longer with our comp with Meta, but
[L1084] [35:58.48] Michael Bolan was always an engineer I
[L1085] [36:00.00] looked up to because he was a great
[L1086] [36:01.28] project starter. He could identify the
[L1087] [36:03.68] need. Hey, we need a fuzzy file searcher
[L1088] [36:05.92] that works on in insanely large repos.
[L1089] [36:08.80] What do we do? He kickstarted a project
[L1090] [36:11.12] called Miles and just did it, right?
[L1091] [36:12.80] which is like backend binaries on a
[L1092] [36:15.44] multiple platforms, deployment,
[L1093] [36:17.20] documentation, naming, all this stuff
[L1094] [36:18.88] that he could just do and he did it over
[L1095] [36:20.32] and over and over again. That's just one
[L1096] [36:22.00] of the many things he started. I think
[L1097] [36:23.60] he started buck too. Let's see here. Bob
[L1098] [36:25.92] Baldwin is a very senior product
[L1099] [36:28.64] engineer. I mean, I think he works on
[L1100] [36:30.00] Inferno now, but for a long time he was
[L1101] [36:31.36] on product and he's an excellent
[L1102] [36:32.72] communicator. He can really boil down
[L1103] [36:34.88] the message, which is something I think
[L1104] [36:36.24] a lot of engineers very much struggle
[L1105] [36:37.92] with and it's a really important skill
[L1106] [36:39.60] is writing and communication. So I
[L1107] [36:42.16] really admired his communication and how
[L1108] [36:44.00] he could make things clear. Another
[L1109] [36:46.16] engineer that's similar is Oliver Ricard
[L1110] [36:48.56] who uh is a very very good writer and a
[L1111] [36:51.28] very good communicator and his posts are
[L1112] [36:53.20] absolute masterworks. Whenever someone
[L1113] [36:54.72] is like hey my engineer needs to work on
[L1114] [36:56.88] communication I'm like go look at
[L1115] [36:58.16] Oliver's posts. That's the bar. That's
[L1116] [37:00.00] what you should be aiming for.
[L1117] [37:02.48] And finally I'm aware of what I'm not
[L1118] [37:04.48] the skills that I'm missing. So another
[L1119] [37:06.32] senior engineer that I work with almost
[L1120] [37:07.92] every day is Nolan O'Brien. uh and he is
[L1121] [37:11.28] like my polar opposite. He writes code
[L1122] [37:12.96] but not a not a whole lot. He is
[L1123] [37:15.28] extremely good at driving alignment
[L1124] [37:17.92] between different teams and he's
[L1125] [37:19.68] extremely good at managing the Apple
[L1126] [37:21.28] relationship which is something I never
[L1127] [37:22.80] had patience to do, right? Like Meta and
[L1128] [37:24.88] Apple, they don't always get along.
[L1129] [37:27.12] Nolan finds a way to communicate between
[L1130] [37:28.96] these two companies and try to get us on
[L1131] [37:30.80] the same page, focus on what we can do
[L1132] [37:32.80] together. And I I really admire him for
[L1133] [37:34.80] that. So that's my list of other senior
[L1134] [37:37.92] engineers I really really admire.
[L1135] [37:40.16] >> The last thing that I'd like to ask you
[L1136] [37:42.00] is you have a lot of, you know,
[L1137] [37:44.56] experience at this point. And if you
[L1138] [37:46.88] were to go back to yourself right when
[L1139] [37:49.20] you had graduated Princeton and give
[L1140] [37:51.36] yourself some career advice, what would
[L1141] [37:53.52] you say?
[L1142] [37:54.56] >> Nothing. It worked out pretty well for
[L1143] [37:55.92] me. I'm not screwing with it, man.
[L1144] [37:57.46] [laughter]
[L1145] [37:58.48] Um, the funny thing is when I was
[L1146] [38:00.24] graduating Princeton in 2010, I thought
[L1147] [38:02.96] about applying. I was like, should I be
[L1148] [38:04.24] self-employed and write iPhone apps or
[L1149] [38:06.00] should I go work for a company? And I
[L1150] [38:08.08] actually applied to Facebook. And I'm
[L1151] [38:11.12] pretty sure at the time what they would
[L1152] [38:12.40] do is they would send you this puzzle.
[L1153] [38:13.84] They'd send you like a mysterious puzzle
[L1154] [38:15.28] that you had to like solve the mystery
[L1155] [38:17.20] and then you could apply. And I threw it
[L1156] [38:19.20] in the trash. I was like, I don't have
[L1157] [38:20.32] time for that. I'm not doing that. Uh,
[L1158] [38:22.24] and so I'm like, what if I joined
[L1159] [38:23.52] Facebook in 2010? What would that have
[L1160] [38:25.28] been like? It probably would have been a
[L1161] [38:27.20] lot worse because I would have been
[L1162] [38:28.24] around for all the HTML 5 stuff and I
[L1163] [38:30.24] would have just been like, oh no, no,
[L1164] [38:31.60] no. Um, but yeah, I I don't think I
[L1165] [38:35.44] would offer any advice to myself at the
[L1166] [38:37.12] time because uh my personal situation
[L1167] [38:40.96] worked out really well. Um, as far as
[L1168] [38:43.12] general career advice, I don't know, do
[L1169] [38:45.52] what you like, right? Like I feel like
[L1170] [38:46.72] it's really hard to fake enthusiasm or
[L1171] [38:49.36] like find enthusiasm for something you
[L1172] [38:50.88] really don't enjoy doing. So like find
[L1173] [38:52.88] what you love doing and do that. Uh, and
[L1174] [38:54.96] if that intersects with what the
[L1175] [38:56.24] industry needs, you're in a really lucky
[L1176] [38:59.04] place. You know, I used to always hear
[L1177] [39:00.80] that advice and think that is uh cliche
[L1178] [39:04.08] and
[L1179] [39:04.48] >> it's very cliche.
[L1180] [39:05.44] >> Yeah. But actually there's so much stuff
[L1181] [39:08.32] downstream of that like your
[L1182] [39:10.32] productivity comes from you loving the
[L1183] [39:13.60] work. I mean you have insane uh output
[L1184] [39:16.48] and your curiosity and the learning it's
[L1185] [39:19.84] got to be order of magnitude more than
[L1186] [39:21.68] it would be if you hated it and you
[L1187] [39:23.52] didn't proactively dig you know 10
[L1188] [39:26.08] layers deep. So,
[L1189] [39:27.44] >> I think it's good if you if you like
[L1190] [39:28.88] solving problems. That's the thing,
[L1191] [39:30.56] right? Because it's not like every
[L1192] [39:31.52] single moment I'm debugging some really
[L1193] [39:33.52] bad code deep in some awful system. I'm
[L1194] [39:36.32] loving what I'm doing. But I like the
[L1195] [39:38.40] challenge of solving problems. And so,
[L1196] [39:39.92] if you like that, you're in good you're
[L1197] [39:41.44] in a good place.
[L1198] [39:42.72] >> Thanks so much for your time, Adam. I
[L1199] [39:44.32] really appreciate it. Um I was really
[L1200] [39:46.56] looking forward to talking to you. So,
[L1201] [39:47.76] thanks so much for sharing your career
[L1202] [39:49.68] story with the community.
[L1203] [39:51.04] >> Sure thing. Thanks, Ryan.
[L1204] [39:52.64] >> Thank you for listening to the podcast.
[L1205] [39:54.40] It's a passion project of mine that I've
[L1206] [39:56.64] really enjoyed building. Another passion
[L1207] [39:58.72] project that I've been working on kind
[L1208] [40:00.00] of in secret is building an ergonomic
[L1209] [40:02.56] keyboard that I wish existed and I
[L1210] [40:04.80] finally have a prototype. So, I'd love
[L1211] [40:06.48] to show you what we've built. It's ultra
[L1212] [40:09.28] lowprofile and ergonomic and I couldn't
[L1213] [40:12.08] find anything like it on the market. So,
[L1214] [40:13.68] that's why we built it. I'll put a link
[L1215] [40:15.44] to the keyboard in the description. You
[L1216] [40:17.12] can take a look and learn more about the
[L1217] [40:18.72] project there. We could definitely use
[L1218] [40:20.32] your support. Also, if you have any
[L1219] [40:22.40] feedback for me about the show, I'd love
[L1220] [40:24.32] to hear it. Comments on YouTube have led
[L1221] [40:26.80] to guests coming on like Ilia Gregoric
[L1222] [40:29.44] and David Fowler. I wasn't aware of them
[L1223] [40:31.76] until someone dropped a comment. Also,
[L1224] [40:34.00] feedback in the comments helped me learn
[L1225] [40:35.52] to reduce the number of cliffhers in the
[L1226] [40:38.00] intros. So, your comments definitely
[L1227] [40:39.84] make a difference. Please keep letting
[L1228] [40:41.28] me know what you'd like to see more of
[L1229] [40:42.88] in the show, and I'll see you in the
[L1230] [40:44.40] next episode.
