Chunk 1; segments 1–336. 

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L10] [00:00.24] The amount of stuff that you learn about
[L11] [00:02.88] what was going on at that time is just
[L12] [00:04.96] mind-boggling.
[L13] [00:06.40] >> This is Casey Muratori, video game
[L14] [00:08.72] developer and sometimes computer
[L15] [00:10.40] historian through his popular talks and
[L16] [00:12.64] I asked them all about the stories in
[L17] [00:14.48] computing he uncovered.
[L18] [00:15.92] >> Dystro was depressed at that time.
[L19] [00:18.64] >> He literally says like in this period I
[L20] [00:20.96] was very depressed because of these
[L21] [00:23.12] reasons. Look at the correspondence.
[L22] [00:25.60] They didn't have the ability to do like
[L23] [00:27.20] piffy Twitter replies, so it was just on
[L24] [00:29.76] paper.
[L25] [00:31.04] >> What drew you towards video gaming?
[L26] [00:33.76] >> There's a bunch of things I could say
[L27] [00:36.00] about that, but they're probably all BS.
[L28] [00:38.88] Here's the full episode.
[L29] [00:44.96] There's so much, you know, AI Doom
[L30] [00:47.68] content out there. I'm hoping that we
[L31] [00:50.00] can just talk about interesting things
[L32] [00:52.88] in software engineering and just see
[L33] [00:54.96] where it goes. So I'm not going to ask
[L34] [00:57.04] anything that's uh you know all this AI
[L35] [00:59.84] doom you're gonna you have two years
[L36] [01:01.76] left to be a software engineer. So
[L37] [01:04.32] >> fantastic. I will try to keep the AI
[L38] [01:06.08] mentions to a minimum. [laughter]
[L39] [01:08.48] >> There's this famous quote by Donald
[L40] [01:10.88] Kuth. The big part of it is premature
[L41] [01:14.00] optimization is the root of all evil.
[L42] [01:16.88] And I remember I've I've heard that
[L43] [01:18.40] before, but I I don't think I know the
[L44] [01:20.64] full history behind it. And you know,
[L45] [01:23.44] why is that significant?
[L46] [01:26.00] So I guess we can split that into two
[L47] [01:27.52] parts. Like what's the history behind it
[L48] [01:28.96] and why is this significant? The
[L49] [01:30.48] significant part is probably the easiest
[L50] [01:32.72] to answer because it's, you know, for
[L51] [01:36.64] whatever accident of history, it's
[L52] [01:38.48] something that people really remembered
[L53] [01:40.24] like it's stuck. And so the reason that
[L54] [01:42.96] it ended up being significant is people
[L55] [01:44.80] keep repeating it and they keep
[L56] [01:46.72] interpreting it or reinterpreting it. So
[L57] [01:49.92] the effects of that phrase far beyond
[L58] [01:53.28] what anyone may have done with it in
[L59] [01:55.04] context at the time or what they meant
[L60] [01:56.88] or any of those things or the history,
[L61] [01:59.84] the effects of it are like still felt to
[L62] [02:01.68] this day. Some people uh I think
[L63] [02:04.16] probably correctly you might say
[L64] [02:07.76] interpret the term with a fair bit of
[L65] [02:09.84] nuance and and say like oh well you know
[L66] [02:12.32] it can mean a number of different things
[L67] [02:13.60] or it's trying to capture something
[L68] [02:14.96] subtle or whatever. Other people are
[L69] [02:17.20] very blunt about it and just think like
[L70] [02:18.64] oh it just means I don't have to think
[L71] [02:20.00] about the performance of my code till
[L72] [02:21.84] like the end of the project right like
[L73] [02:23.84] like premature just means any
[L74] [02:25.44] consideration of performance is not
[L75] [02:27.68] worth it. eventually we'll see where the
[L76] [02:29.28] code is slow and we'll fix it or
[L77] [02:30.48] something, right? And so, uh, it's it's
[L78] [02:33.84] a significant phrase for that reason, at
[L79] [02:35.92] least to me. You still hear it to this
[L80] [02:38.00] day and it's at least, you know,
[L81] [02:39.76] depending on how, uh, you want to
[L82] [02:41.92] account for it, it's at least something
[L83] [02:44.32] that's 50 years old now. Uh, and so
[L84] [02:48.08] that's an incredibly lasting impact for
[L85] [02:50.80] a rule of thumb or however you want to
[L86] [02:53.28] look at it. So uh on the history side,
[L87] [02:56.32] this was really uh when I decided to to
[L88] [02:58.48] to do a talk on this, I knew I wanted to
[L89] [03:00.72] do another computer history talk um
[L90] [03:02.64] because I had given one before at at
[L91] [03:04.80] this was at something called the better
[L92] [03:05.92] software conference. It's you know
[L93] [03:07.36] there's been two of them so far and at
[L94] [03:10.24] the first one I did a history talk and I
[L95] [03:12.24] wanted to do another history talk and
[L96] [03:13.68] this was going to be like probably only
[L97] [03:15.28] going to do two of these and this second
[L98] [03:16.56] one. I wanted to do it on the history of
[L99] [03:19.68] this phrase because when I started
[L100] [03:21.04] looking into the history of this phrase
[L101] [03:22.48] a while back, I found that there was
[L102] [03:24.08] just a lot of stuff there that I didn't
[L103] [03:26.40] know. And this is true. I mean, I guess
[L104] [03:29.84] I would say every time I've ever looked
[L105] [03:31.68] at computer history, every every time
[L106] [03:33.60] I've go I I refer to it as dumpster
[L107] [03:35.44] diving, but it's not it's not like that
[L108] [03:37.52] makes it sound derogatory. I just think
[L109] [03:39.76] but I think of that as kind of what I'm
[L110] [03:40.96] doing but it's not really like it's
[L111] [03:42.48] actually a very enjoyable experience uh
[L112] [03:45.04] to go back through history and try to
[L113] [03:46.40] pick pick through what happened. But um
[L114] [03:49.28] so to do this talk I basically went and
[L115] [03:51.04] tried to do a a pretty detailed you know
[L116] [03:53.36] analysis of like how did this phrase end
[L117] [03:56.24] up being put in print? You know what
[L118] [03:58.40] were the worked examples at the time?
[L119] [03:59.92] What were they thinking about? Why might
[L120] [04:01.36] it have been said?
[L121] [04:02.96] >> What did you learn in doing all that
[L122] [04:04.72] research about these famous computer
[L123] [04:06.96] science phrases? The thing that shocks
[L124] [04:09.36] me, it shock it both times, even though
[L125] [04:11.12] I've now done it twice, the amount of
[L126] [04:13.20] stuff that you learn about what was
[L127] [04:15.52] going on at that time that you just had
[L128] [04:17.60] no idea is is just mind-boggling. And
[L129] [04:20.88] and I would point out that this is for a
[L130] [04:23.60] talk. You know, I'm not a historian. I
[L131] [04:25.76] don't do this for a living. I'm not at a
[L132] [04:28.16] university somewhere doing computer
[L133] [04:29.76] history research. So what I think of as
[L134] [04:34.00] a pretty thorough read for the history
[L135] [04:35.52] that I did for the talk is actually
[L136] [04:37.28] somewhat shallow. Like if you had time
[L137] [04:40.00] and the resources, you could go access
[L138] [04:41.92] some of these people's personal papers,
[L139] [04:43.68] make appointments to see things that are
[L140] [04:45.28] not really in the public record so much
[L141] [04:46.88] and so on. So even just with publicly
[L142] [04:50.08] available things that you can get, the
[L143] [04:52.48] amount of stuff that I found was just
[L144] [04:54.32] really kind of uh intriguing to me. And
[L145] [04:58.00] so um I'll give like a kind of a brief
[L146] [05:01.12] overview of sort of what what I thought
[L147] [05:03.52] was the story of this kind of phrase in
[L148] [05:06.08] a way. Um I think there are kind of two
[L149] [05:10.40] I guess I would say there there are sort
[L150] [05:11.92] of two threads that are good to
[L151] [05:14.00] understand that come together and this
[L152] [05:16.32] is what I tried to portray in the talk
[L153] [05:17.60] as well.
[L154] [05:19.04] The first thread is this idea um of a
[L155] [05:22.96] thing and you know we didn't really do
[L156] [05:25.44] an intro to this to this podcast but um
[L157] [05:28.08] so I'll just I'll say it now. I'm a big
[L158] [05:29.52] fan of your show. When when you said do
[L159] [05:32.00] you want to be on the podcast you didn't
[L160] [05:33.20] have to tell me what the show was. Like
[L161] [05:34.16] I've already watched it. I I love it. Uh
[L162] [05:36.32] and one of the people you had on for
[L163] [05:37.92] example was Barbara Liskoff. And in that
[L164] [05:40.96] interview she actually refers to
[L165] [05:43.04] something called the software crisis.
[L166] [05:45.20] Right. Um and I think you prompted or a
[L167] [05:48.96] question about this as well. Right? So,
[L168] [05:51.92] a lot of people don't really know about
[L169] [05:54.00] the software crisis. They don't know
[L170] [05:55.36] that that was a term. They don't know
[L171] [05:56.56] this something that happened because
[L172] [05:57.52] it's kind of ancient history now. It was
[L173] [05:59.04] in the sort of late 60s, early 70s. This
[L174] [06:01.84] was a thing. And what this was is
[L175] [06:06.80] originally, you know, computer hardware
[L176] [06:09.20] in a sense that you or I can't really
[L177] [06:11.04] conceive of it in practice because it
[L178] [06:13.12] was so far before our time, right?
[L179] [06:15.76] um that basically computer hardware
[L180] [06:19.12] originally was very simplistic. And so
[L181] [06:21.36] the things that you were going to do
[L182] [06:22.56] with it could be described very easily
[L183] [06:25.44] and really all you were trying to do
[L184] [06:27.92] when you programmed a computer was just
[L185] [06:30.16] translate a fairly straightforward
[L186] [06:31.84] definition of some computation into like
[L187] [06:34.72] machine instructions.
[L188] [06:36.88] The kind of thing that we would kind of
[L189] [06:38.40] think about today as like hand
[L190] [06:40.80] optimizing assembly code was really just
[L191] [06:43.44] all computer programming kind of was,
[L192] [06:45.04] right? It was just like, okay, we're
[L193] [06:46.24] going to we're going to take this
[L194] [06:47.20] problem description and and translate it
[L195] [06:48.72] in.
[L196] [06:50.24] But during the 60s, computing power was
[L197] [06:52.56] advancing to the point where people
[L198] [06:54.24] could consider doing much more
[L199] [06:56.00] significant things with it. They could
[L200] [06:57.28] run payroll systems. They could do
[L201] [06:59.44] analysis of of data sets. and they would
[L202] [07:01.92] want to be able to be flexible and
[L203] [07:03.36] change the sorts of computations they
[L204] [07:04.88] were doing and all these other sorts of
[L205] [07:06.40] things. They were starting to have
[L206] [07:07.92] graphical displays. Uh you know um Ivan
[L207] [07:10.48] Southerntherland sketchpad is like in
[L208] [07:12.08] the early 1960s, right? And so what they
[L209] [07:15.84] found was at that time programmers were
[L210] [07:18.64] not really ready to make that
[L211] [07:20.16] transition. They didn't think about
[L212] [07:22.40] things the way we kind of all now take
[L213] [07:24.24] for granted where it's like, oh yeah,
[L214] [07:25.84] you know, I built this library for
[L215] [07:27.68] loading JPEG images and now when I want
[L216] [07:29.52] to load a JPEG, I just call load JPEG
[L217] [07:31.36] and it's done. And you know, all of
[L218] [07:33.28] these things that we take for granted,
[L219] [07:35.04] that all had to that all had to be a
[L220] [07:37.84] cultural shift. The idea that there were
[L221] [07:39.84] going to be these um abstractions and
[L222] [07:42.56] these ways of of sort of breaking down a
[L223] [07:44.88] much more complex system into parts that
[L224] [07:46.64] we could manage, that actually was a
[L225] [07:48.56] transition that had to happen. And so
[L226] [07:49.84] the software crisis was kind of this
[L227] [07:51.36] period where people were starting to say
[L228] [07:53.28] the methods that we're using for
[L229] [07:54.56] programming will not scale to these
[L230] [07:56.88] larger problems that we want to do.
[L231] [07:59.12] We've got to figure out something uh to
[L232] [08:01.20] do about it. So that's one thread of
[L233] [08:04.56] history that's coming. Another thread of
[L234] [08:07.20] history that's coming that's you know
[L235] [08:09.60] it's a little bit more specific to
[L236] [08:11.28] Donald Kuth who was the first person to
[L237] [08:13.28] really put this into a worked example.
[L238] [08:15.44] like he's kind of who I would credit
[L239] [08:17.20] with the origin of this phrase, even if
[L240] [08:19.04] there are people who might debate that
[L241] [08:20.56] fact. And to me, it doesn't really
[L242] [08:22.00] matter who said the phrase, like the
[L243] [08:23.28] phrase lives on in on its own. So, you
[L244] [08:25.44] know, I I I wouldn't I wouldn't even
[L245] [08:27.68] argue with someone if they wanted to
[L246] [08:29.12] sort of uh make other claims about it.
[L247] [08:32.00] But just in general,
[L248] [08:34.48] he was going like like at Stanford at
[L249] [08:38.64] this time, he was sort of learning about
[L250] [08:40.96] the fact that you could do these
[L251] [08:43.12] profiles like taking actual execution
[L252] [08:46.00] profiles, figuring out where time was
[L253] [08:47.84] spent in the execution of a program and
[L254] [08:51.04] using that to guide your decision-m
[L255] [08:52.80] about how where are you going to spend
[L256] [08:54.08] time developing the software. Again,
[L257] [08:56.32] something that even today today
[L258] [08:58.00] performance is maybe not as much of an
[L259] [09:00.32] emphasis as it maybe should be in
[L260] [09:01.68] software, but even today with that in
[L261] [09:04.48] mind, most people understand the concept
[L262] [09:06.96] of an execution profile. They understand
[L263] [09:08.72] that you could go into Chrome and see
[L264] [09:10.16] like a network profile of how that's
[L265] [09:11.60] working. You could uh see a flame graph
[L266] [09:13.60] of of you know where time is being spent
[L267] [09:15.44] or all these sorts of things.
[L268] [09:18.16] Again, you have to remember if you
[L269] [09:19.60] rewind the clock back far enough, these
[L270] [09:21.84] were all brand new concepts, right? a
[L271] [09:24.48] sampling profiler, a block brace
[L272] [09:26.16] profiler, uh you know, a a binary
[L273] [09:28.80] instrumentation profiler. All these
[L274] [09:30.40] sorts of things were not just tools that
[L275] [09:32.96] everyone assumed that they could just go
[L276] [09:34.64] have and and had seen at some point.
[L277] [09:36.96] Some people may never have even realized
[L278] [09:38.48] that was was a thing, right?
[L279] [09:41.28] So that's another thread that's
[L280] [09:42.48] happening. And those two things converge
[L281] [09:45.20] effectively in 1974 roughly to get us
[L282] [09:49.60] this statement. Can is very much into
[L283] [09:54.40] this idea of structured programming
[L284] [09:56.40] which is sort of a a solution a proposed
[L285] [09:59.60] solution to the software crisis.
[L286] [10:03.20] Maybe a proposed solution is the wrong
[L287] [10:04.64] way to say it. It's a certain set of
[L288] [10:06.80] ideas that are trying to be employed to
[L289] [10:09.92] improve the situation. Let's say he's
[L290] [10:12.32] very much in into this and we can talk
[L291] [10:14.88] about what that is uh sort of a separate
[L292] [10:16.96] tangent if we want to later. He's very
[L293] [10:19.52] much into that. He's thinking about
[L294] [10:20.96] that. He's um he's thinking about this
[L295] [10:23.76] idea that programmers can't just be
[L296] [10:26.80] about writing all of this very tightly
[L297] [10:29.84] optimized assembly language code and
[L298] [10:31.44] that's all we're going to spend all our
[L299] [10:32.56] time doing. We have to be thinking
[L300] [10:33.92] bigger picture. We have to be picking
[L301] [10:35.36] and choosing our battles. We have to
[L302] [10:37.68] make concessions to maintainability. Uh
[L303] [10:40.96] you know if this particular routine is
[L304] [10:43.20] not really accounting for hardly any of
[L305] [10:44.72] our runtime, we should not be obuscating
[L306] [10:46.80] it with all of these like hand unrolling
[L307] [10:48.48] the loops and all these things. Remember
[L308] [10:50.00] again underlying all this they don't
[L309] [10:52.00] have like massive optimizing compiler
[L310] [10:55.44] kind of passes like we have with LLVM
[L311] [10:57.44] now right they don't have all of this
[L312] [10:59.04] extra stuff so if you wanted something
[L313] [11:00.64] unrolled you were going to unroll it
[L314] [11:01.84] yourself if you wanted some kind of loop
[L315] [11:03.84] hoist a loop invariant out you probably
[L316] [11:05.52] had to do that yourself like a lot of
[L317] [11:06.88] that stuff that we take for granted
[L318] [11:08.40] again not in there so um that sort of
[L319] [11:12.80] this he's very unstructured programming
[L320] [11:14.64] he's starting to see these execution
[L321] [11:16.16] time profiles they do a thing at
[L322] [11:17.60] Stanford in the n in in 1970 and he
[L323] [11:19.60] actually he does it with some students
[L324] [11:20.80] where they take a look at uh forrren
[L325] [11:23.44] programs and they instrument them to see
[L326] [11:24.88] where the time is being spent. Not in
[L327] [11:26.96] exactly the most rigorous way that you
[L328] [11:28.64] might imagine. That's another thing for
[L329] [11:29.84] my talk that I kind of go into. Um but
[L330] [11:32.32] he's sort of saying like look
[L331] [11:34.88] we we as programmers need to start
[L332] [11:37.76] taking the decision about what to
[L333] [11:39.52] optimize more seriously.
[L334] [11:42.40] And he kind of has a fairly nuanced take
[L335] [11:44.08] on it. If you actually read the section
[L336] [11:46.72] um of his 1974 paper uh structured
[L337] [11:49.52] programming with go-to statements where
[L338] [11:51.28] kind of the first time this was really
[L339] [11:52.80] put to print that I know of he he does
[L340] [11:55.04] he does say it in an ACM touring lecture
[L341] [11:57.60] a little earlier but he would have
[L342] [11:59.68] submitted like based on my timeline he
[L343] [12:02.64] would have submitted the manuscript for
[L344] [12:04.80] this publication prior to the lecture.
[L345] [12:07.36] So it was the first time that I know of
