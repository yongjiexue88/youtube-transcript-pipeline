Chunk 1; segments 1–333. 

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
