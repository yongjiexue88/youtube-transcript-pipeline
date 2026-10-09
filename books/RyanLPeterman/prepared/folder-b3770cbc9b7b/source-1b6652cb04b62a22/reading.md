# "Clean Code", Horrible Performance | Casey Muratori

Source ID: source-1b6652cb04b62a22
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Clean_Code_,_Horrible_Performance_Casey_Muratori_en.txt
Video: https://www.youtube.com/watch?v=czr1L3JocOI

[L10] [00:00.00] Earlier we talked about the the
[L11] [00:01.76] trade-off between, I guess, performance
[L12] [00:04.56] code and maintainable code. And I saw
[L13] [00:08.72] you had this one video said, you know,
[L14] [00:10.96] in quotes, clean code horrible
[L15] [00:13.64] performance. Now,
[L16] [00:15.32] I feel like this is on the same topic.
[L17] [00:17.72] What's your your take there on, you
[L18] [00:20.44] know, because you also put clean code in
[L19] [00:23.00] quotes. What does that mean?
[L20] [00:24.60] >> So, it's a it's a pretty fairly subtle
[L21] [00:26.20] topic, right? Uh and that's why the the
[L22] [00:28.64] quotes are there because um the first
[L23] [00:30.80] thing that I you have to point out is
[L24] [00:32.48] that clean code is clean code,
[L25] [00:35.32] object-oriented programming, a lot of
[L26] [00:37.56] these phrases, they mean different
[L27] [00:39.12] things to different people. And so, if
[L28] [00:41.04] you're going to say that you're, you
[L29] [00:42.40] know, this code is clean, it's pretty
[L30] [00:45.00] hard to find two programmers who will
[L31] [00:48.12] agree on exactly whether it is or not,
[L32] [00:51.04] right? Like like they all have like
[L33] [00:52.40] different ideas about what is clean and
[L34] [00:54.64] what is not, right?
[L35] [00:56.72] So, the reason I put that in quotes is I
[L36] [00:58.16] was talking about a very specific thing,
[L37] [00:59.44] which is like literally like the book
[L38] [01:01.64] Clean Code, like the thing where there's
[L39] [01:03.40] like here are the things that we would
[L40] [01:04.64] recommend that you do, right?
[L41] [01:06.88] So, in that particular case, what I was
[L42] [01:08.44] talking about is there's a certain set
[L43] [01:10.84] of ideas that is advocated in Clean Code
[L44] [01:14.24] as like these are the things you should
[L45] [01:15.60] do, and they are like you should have
[L46] [01:19.00] everything should be kind of um
[L47] [01:22.04] I guess I would say
[L48] [01:23.64] dynamic dispatch, or at least you
[L49] [01:25.88] shouldn't code shouldn't know the types
[L50] [01:27.44] it's operating on, right? Saying it's
[L51] [01:29.40] dynamic dispatch is maybe it depends on
[L52] [01:31.40] the language whether that's going to be
[L53] [01:32.52] true or not, but when I write code, I
[L54] [01:34.56] don't know what types I have. It's just
[L55] [01:36.56] I don't know, like some base classes is
[L56] [01:38.04] what I'm operating on, and they could be
[L57] [01:39.32] anything, right? That's thing one. Thing
[L58] [01:41.64] two is functions should be very small.
[L59] [01:43.72] Uh in fact, the the numbers are kind of
[L60] [01:46.04] weird. They're like four lines or five
[L61] [01:48.16] line Like when you go look at the actual
[L62] [01:49.76] things that are claimed in some of the
[L63] [01:51.28] this literature, it's it's really
[L64] [01:52.72] strange. You're just like, "Gosh, that's
[L65] [01:54.64] very small, right?"
[L66] [01:56.88] Um
[L67] [01:58.32] and I go through some of those things
[L68] [01:59.60] and I say, "Look, if we were to actually
[L69] [02:01.28] follow these,
[L70] [02:03.04] we get into a really bad state because a
[L71] [02:05.72] lot of the languages that people are
[L72] [02:07.04] going to be using to implement this
[L73] [02:08.32] stuff, like C++ for example, um which
[L74] [02:11.16] even would be a fairly good case in a
[L75] [02:13.24] lot of cases at least it's a compiled
[L76] [02:14.60] language and so on.
[L77] [02:17.44] In a a lot of cases, these things are
[L78] [02:19.00] kind of a recipe for disaster.
[L79] [02:21.00] If you're
[L80] [02:22.60] if you're handing out types where you
[L81] [02:24.44] can't know the type at compile time or
[L82] [02:26.68] you can't know the type uh or it's or
[L83] [02:28.44] it's, you know, going to be in a
[L84] [02:29.36] different module, so it, you know,
[L85] [02:30.60] unless you have like a really aggressive
[L86] [02:32.00] link time code generation, it's not
[L87] [02:33.28] going to be likely that you could figure
[L88] [02:34.28] this out. And you're saying all the
[L89] [02:35.96] functions should be very small and of
[L90] [02:37.32] course they're going to be virtual
[L91] [02:38.24] because they're on these sort of types
[L92] [02:39.76] that you don't know what they are.
[L93] [02:41.88] This creates a really uh toxic
[L94] [02:44.36] combination for the compiler.
[L95] [02:46.56] Normally,
[L96] [02:48.08] you can have I mean, you can have small
[L97] [02:51.12] functions if you want them only four
[L98] [02:52.28] lines long. If the compiler can know
[L99] [02:54.48] that it can just inline that, right? If
[L100] [02:56.24] it can see clearly what you're doing and
[L101] [02:58.40] it can just merge those things in, we
[L102] [02:59.96] don't have a problem. If they're behind
[L103] [03:01.64] a virtual function, so it doesn't know,
[L104] [03:03.88] like it can't guarantee that it is that
[L105] [03:06.04] type,
[L106] [03:07.44] um it can't do that.
[L107] [03:09.76] And so, when you talk about all this
[L108] [03:11.32] stuff, what you're what you're giving
[L109] [03:12.68] up, people I think also because the
[L110] [03:14.52] video I mean, the video was a very short
[L111] [03:16.08] video, it's part of like a series.
[L112] [03:18.76] I think people sometimes get the wrong
[L113] [03:19.84] idea that I think that virtual function
[L114] [03:21.32] calls cost a lot. They do cost
[L115] [03:23.00] something, but, you know, depending on
[L116] [03:25.12] how you want to look at it, they
[L117] [03:25.92] actually don't cost that much
[L118] [03:27.80] uh because, you know, it depends on
[L119] [03:29.80] whether it's predicted correctly or not,
[L120] [03:31.28] but in general, like the cost of virtual
[L121] [03:33.12] function is less than you would think a
[L122] [03:34.40] lot of times.
[L123] [03:36.36] The actual reason that it slows things
[L124] [03:37.92] down is because the compiler cannot
[L125] [03:39.64] merge the code together, right? It can't
[L126] [03:41.68] inline stuff and remove and reduce the
[L127] [03:43.72] waste. Like, that's the actual problem.
[L128] [03:46.44] So, if you just want to call a virtual
[L129] [03:47.72] function, yeah, it it if it was a
[L130] [03:49.84] really, really uh hardcore optimization
[L131] [03:52.64] scenario, then you don't want anything
[L132] [03:54.60] probably calling a virtual function in
[L133] [03:56.00] general cuz there is some cost to that.
[L134] [03:58.00] Just calling a function has cost.
[L135] [04:00.64] But that wasn't the really bad part of
[L136] [04:02.88] it, right? So it's that plus there's an
[L137] [04:05.68] additional thing which is that it can't
[L138] [04:07.56] unroll and go wide on things. If the
[L139] [04:09.56] compiler can see everything you're
[L140] [04:10.68] doing, it can use SIMD, it can like
[L141] [04:13.32] widen loops to operate on multiple
[L142] [04:14.88] things at once, it can unroll those
[L143] [04:16.20] loops. There's all these things it can
[L144] [04:17.24] do. If it's got these virtual functions,
[L145] [04:18.80] it's just like
[L146] [04:20.64] that's it. I don't know I I can't make
[L147] [04:22.36] decisions about that. I have no idea
[L148] [04:23.52] what this thing on the other end is
[L149] [04:24.28] doing, right?
[L150] [04:25.96] So uh that was kind of my point on that
[L151] [04:28.72] and uh again, I it's not meant to be uh
[L152] [04:31.96] assailing the idea that your code should
[L153] [04:33.72] be easy to read or easy to maintain.
[L154] [04:35.72] It's just more like these guidelines
[L155] [04:37.52] seem really bad and also I don't think
[L156] [04:39.68] we need them for code to be
[L157] [04:41.20] maintainable. I I don't have trouble
[L158] [04:43.08] maintaining functions that are 30 lines
[L159] [04:44.80] long or 50 lines long. I don't find that
[L160] [04:46.68] five is a magic number or something or
[L161] [04:48.28] that it has to be really short. Uh and
[L162] [04:49.80] also I find that it's usually pretty
[L163] [04:51.12] easy to write code where I know what the
[L164] [04:52.68] types are. Um that those can be
[L165] [04:54.44] determined at compile time. Like I don't
[L166] [04:56.28] think that results in code that's
[L167] [04:58.60] particularly hard to read.
[L168] [05:00.92] >> When I was in college, very in very
[L169] [05:03.36] early, I remember people recommend that
[L170] [05:05.88] book. So oh, you should read Clean Code.
[L171] [05:08.48] So my understanding that you wouldn't
[L172] [05:09.68] recommend people who are software
[L173] [05:11.76] engineers to read that.
[L174] [05:14.08] >> I guess the way I would categorize it is
[L175] [05:15.52] a mixed bag. So I would I wouldn't
[L176] [05:17.40] actually say that I disagree with all of
[L177] [05:19.60] all of the things in the book, though. I
[L178] [05:21.08] mean, some of the things are things that
[L179] [05:22.88] I definitely do myself. Like giving um
[L180] [05:26.16] variables like easy to understand names
[L181] [05:29.28] uh is something that I think would be
[L182] [05:31.24] and then that's in that book. Uh
[L183] [05:33.48] is good advice, right? And so kind of
[L184] [05:36.32] more I wouldn't I wouldn't necessarily
[L185] [05:38.08] say do or don't read a book. What I
[L186] [05:40.00] would say is like I think there's some
[L187] [05:41.84] things in this book that don't that
[L188] [05:43.84] aren't addressed properly. Like I don't
[L189] [05:46.16] think you want to tell people these
[L190] [05:47.36] rules of thumb and not tell them about
[L191] [05:49.12] these other problems that was exactly
[L192] [05:51.32] what I was uh pointing out there.
[L193] [05:53.92] And so, usually it's more that. It's
[L194] [05:55.64] like
[L195] [05:58.00] I find that oftentimes there is this
[L196] [06:01.44] tendency
[L197] [06:03.08] um I guess I'll say to pretend
[L198] [06:06.32] that
[L199] [06:07.92] we don't have to talk about performance
[L200] [06:10.04] and we can just say like, "In fact,
[L201] [06:11.64] premature optimization is the root of
[L202] [06:12.80] all evil." Bringing it back to there. I
[L203] [06:15.12] feel like there's this uh temptation and
[L204] [06:18.68] very prevalent practice of sort of
[L205] [06:20.60] taking that idea to mean we don't have
[L206] [06:23.88] to talk about performance when we're
[L207] [06:25.04] teaching people things at all.
[L208] [06:26.76] Or like when you write the book Clean
[L209] [06:28.12] Code, you don't have to talk about
[L210] [06:29.16] performance at all. You can just include
[L211] [06:30.68] a thing that's basically like, "Hey, um
[L212] [06:34.16] you know,
[L213] [06:35.16] there's performance issues, but most of
[L214] [06:37.36] the time it's not a problem." or
[L215] [06:38.28] something like that, which is, you know,
[L216] [06:39.80] or if you look at uh
[L217] [06:41.80] Refactoring, the book Refactoring, very
[L218] [06:43.88] popular. It literally says exactly that
[L219] [06:45.56] in like the opening thing. It's like,
[L220] [06:46.36] "You know, there there might be
[L221] [06:47.40] performance concerns, but you know,
[L222] [06:49.32] they're usually okay." or something,
[L223] [06:50.40] right? And it's like, that is not true.
[L224] [06:53.12] I just think that's fundamentally not
[L225] [06:54.48] true. I think these books should include
[L226] [06:57.32] detailed discussions of the actual
[L227] [06:59.96] performance problems that you are very
[L228] [07:01.68] likely to hit if you take some of their
[L229] [07:03.56] advice um because it's not that it means
[L230] [07:06.84] you can't do those things,
[L231] [07:09.64] but
[L232] [07:10.64] I'll quote you back to you, it's about
[L233] [07:12.48] trade-offs.
[L234] [07:13.64] There is always a trade-off that you're
[L235] [07:15.52] making.
[L236] [07:16.64] And sometimes, if you understand the
[L237] [07:18.88] trade-off, you will make it. You'll say,
[L238] [07:21.36] "Mm, I know this is going to cost This
[L239] [07:23.32] may be a serious performance problem for
[L240] [07:25.04] us, but I think that's okay."
[L241] [07:27.32] Like, I think it's not like our
[L242] [07:28.80] performance won't suffer to the point
[L243] [07:30.20] where it's a problem for the product. I
[L244] [07:32.76] understand what that's is.
[L245] [07:35.88] There's a huge difference between that
[L246] [07:37.48] and just going like, "Uh we don't worry
[L247] [07:39.24] about performance till the end." Right?
[L248] [07:40.36] Like, there's it's completely different,
[L249] [07:41.96] right? Those are two different
[L250] [07:42.88] engineering approaches.
[L251] [07:44.56] Uh and so what I try to do is encourage
[L252] [07:47.44] people
[L253] [07:48.84] to put that analysis back in. Understand
[L254] [07:51.52] the performance tradeoffs you're making.
[L255] [07:52.88] Understand how much it might cost in the
[L256] [07:55.44] future to like make these fixes.
[L257] [07:58.44] And I
[L258] [07:59.68] I don't really do any AI stuff, but my
[L259] [08:02.08] sort of feeling is
[L260] [08:03.80] more so now than ever I feel like that's
[L261] [08:05.88] got to be pretty important because
[L262] [08:07.28] you're instructing these AIs to do what
[L263] [08:09.76] they're going to do.
[L264] [08:11.24] And I feel like it would be a bad idea
[L265] [08:14.32] to not know about performance tradeoffs
[L266] [08:17.48] because especially if an AI is going to
[L267] [08:20.16] be doing your bidding and structuring
[L268] [08:21.84] the code the way you want to structure
[L269] [08:23.12] it or doing whatever.
[L270] [08:24.64] It seems like a very straightforward
[L271] [08:25.76] part of the process to include
[L272] [08:27.56] performance stuff in those instructions,
[L273] [08:29.72] right? Like that would be a natural
[L274] [08:31.16] thing that we would want to understand
[L275] [08:32.48] and do, right? So I feel like
[L276] [08:35.96] really I've been just trying to get that
[L277] [08:37.12] more into the conversation.
[L278] [08:39.08] Uh and I feel like it's it's as relevant
[L279] [08:41.52] now as it ever was and arguably maybe
[L280] [08:43.20] more so. I don't know, but I could be
[L281] [08:44.52] wrong about that.
[L282] [08:46.12] >> What are some things that are in your
[L283] [08:48.20] mind that are those high-value
[L284] [08:51.24] performance things to consider that
[L285] [08:53.00] don't cost a whole lot to think about?
[L286] [08:55.72] >> So to me awareness is the number one
[L287] [08:58.84] thing, right? Understanding roughly the
[L288] [09:01.40] performance characteristics of the
[L289] [09:03.48] hardware that you're working on, which
[L290] [09:05.36] includes things like, you know, if
[L291] [09:06.48] there's a network, like what does that
[L292] [09:07.80] look like and so on.
[L293] [09:10.04] Um it's really about awareness more than
[L294] [09:12.80] anything else because a little bit of
[L295] [09:15.24] awareness can go a very long way.
[L296] [09:19.56] If you understand the basic concept that
[L297] [09:22.04] like, you know, a that network latency
[L298] [09:25.40] versus network throughput are different
[L299] [09:27.12] things,
[L300] [09:28.20] you can make upfront decisions about
[L301] [09:29.96] structuring code such that you batch
[L302] [09:31.96] things properly, uh and so on and so
[L303] [09:34.44] forth. If you don't understand those
[L304] [09:35.76] things, you could get very far down a
[L305] [09:37.28] project only to realize that everything
[L306] [09:40.20] you designed and all the way it works is
[L307] [09:42.12] all very serial and really just cannot
[L308] [09:44.28] be accelerated over a network at all.
[L309] [09:45.96] Like it's never going to run uh
[L310] [09:47.72] reasonably or something like this,
[L311] [09:48.80] right?
[L312] [09:50.28] Uh and so I think the the lowest-hanging
[L313] [09:53.40] fruit is just to get some education in
[L314] [09:55.68] performance. Like get some education in
[L315] [09:59.04] how to think about the way a machine
[L316] [10:02.00] works and what makes it faster or slow,
[L317] [10:04.12] what it struggles with and what it
[L318] [10:05.48] doesn't.
[L319] [10:06.68] And just to keep that in the back of
[L320] [10:07.96] your head. Because at the end of the
[L321] [10:10.12] day, if you have that knowledge, I think
[L322] [10:12.44] you're very unlikely to make the kinds
[L323] [10:14.64] of architectural decisions that will be
[L324] [10:17.04] hard to undo later, right?
[L325] [10:20.04] Um
[L326] [10:21.00] and so that's really that's really the
[L327] [10:22.72] majority of it, I think. And that is by
[L328] [10:25.52] far the highest-impact, lowest-cost
[L329] [10:28.44] thing you can do is just do that
[L330] [10:29.56] training once. Cuz once you have it,
[L331] [10:31.20] it's with you forever. Once you
[L332] [10:32.84] understand how to think about
[L333] [10:34.44] performance,
[L334] [10:35.76] it can always be there and at any time,
[L335] [10:39.40] you can sort of have that alarm bell of
[L336] [10:40.84] like, "Hmm, this I don't see, you know,
[L337] [10:44.36] you're always kind of looking like I
[L338] [10:45.60] don't see the path towards this running
[L339] [10:47.56] well."
[L340] [10:48.64] And then so that's that your key to stop
[L341] [10:50.56] and go like, "Uh maybe we need to
[L342] [10:51.96] rethink like how we were making some of
[L343] [10:53.48] these decisions."
[L344] [10:54.96] As long as you can see that path, you're
[L345] [10:57.44] pretty you can you can delay most like
[L346] [11:00.40] optimization work. As long as you can
[L347] [11:02.64] see the path, like here is how we will
[L348] [11:04.92] optimize this, you're in pretty good
[L349] [11:06.96] shape because um
[L350] [11:09.40] if you're making those tradeoffs
[L351] [11:10.68] correctly, you're not going to paint
[L352] [11:12.84] yourself into a corner where there's
[L353] [11:14.32] nothing that you can do other than scrap
[L354] [11:16.44] and rewrite.
