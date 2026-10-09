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
[L346] [12:09.20] that he actually committed it to paper
[L347] [12:10.64] would have been there but he may have
[L348] [12:12.40] said this a lot in lectures. He kind of
[L349] [12:14.48] obliquely refers to that in the touring
[L350] [12:16.24] lecture that maybe he had said this
[L351] [12:18.00] around you know around town so to speak.
[L352] [12:20.48] So you know where this was first uttered
[L353] [12:23.52] I don't think anyone knows but point
[L354] [12:25.68] being uh when he says that phrase kind
[L355] [12:28.32] of it's in this context of saying look
[L356] [12:30.96] we we need to be very concerned about
[L357] [12:32.88] efficiency. We shouldn't be leaving
[L358] [12:34.96] performance on the table when it
[L359] [12:36.24] matters. But at the same time, we need
[L360] [12:38.32] to know that it matters. If we don't
[L361] [12:40.16] know that it matters that we're going to
[L362] [12:41.92] apply this optimization, then you know
[L363] [12:44.80] that's a premature optimization and it
[L364] [12:47.28] has real costs. It it's going to make
[L365] [12:49.76] our maintenance and debugging of this
[L366] [12:51.44] program worse for all the same reasons
[L367] [12:53.60] that it would make it worse today. Like
[L368] [12:54.96] if we go into something and we start
[L369] [12:56.72] applying these like optimizations to it
[L370] [12:59.28] that are above and beyond the kind of
[L371] [13:01.44] structural things that we might be doing
[L372] [13:02.80] to that code otherwise that's creating a
[L373] [13:05.60] cognitive burden right um that other
[L374] [13:07.92] people are now going to have to deal
[L375] [13:08.88] with and you're going to have to deal
[L376] [13:10.00] with in the future. So I don't want to
[L377] [13:12.72] put too many words in Canuth's mouth
[L378] [13:14.40] certainly, but in general that's sort of
[L379] [13:17.20] the way that this comes together is
[L380] [13:19.36] those two things. This idea that we need
[L381] [13:20.96] to be more, you know, be doing things to
[L382] [13:22.48] solve the software crisis, have a more
[L383] [13:24.24] structured appro approach to
[L384] [13:25.44] programming, care about maintainability
[L385] [13:27.04] and debugability, composability,
[L386] [13:28.64] abstraction, all that stuff. But also at
[L387] [13:31.92] the same time, we do care about
[L388] [13:33.44] optimization. So how do you dovtail
[L389] [13:34.96] those things? Premature optimization is
[L390] [13:36.32] the root of all evil is kind of like
[L391] [13:37.84] this phrase he uses. I I would I would
[L392] [13:40.08] say if I had if I had to imagine his way
[L393] [13:43.20] of sort of reminding himself, think
[L394] [13:45.52] about all this before you make a
[L395] [13:48.88] decision, right? Um
[L396] [13:52.08] that would be kind of my take on it,
[L397] [13:53.44] right? And and where it comes from. So
[L398] [13:54.80] hopefully, I don't know, that's very
[L399] [13:56.16] long, but it's a very expansive
[L400] [13:57.20] question. So hopefully I've kind of
[L401] [13:58.16] wrangled most of the stuff into there.
[L402] [14:00.16] It sounds like this is really a
[L403] [14:02.40] engineering trade-off where the software
[L404] [14:06.08] crisis is about the maintainability and
[L405] [14:10.32] uh the the complexity for people to
[L406] [14:12.80] actually write and handle their code and
[L407] [14:16.64] then the trade-off between performance
[L408] [14:19.20] and I guess you know code that is
[L409] [14:20.88] maintainable and it sounds like this new
[L410] [14:23.60] quote is
[L411] [14:25.60] you know be mindful of where you pay
[L412] [14:28.00] that cost. Yes. And it's always
[L413] [14:31.04] important to understand the context in
[L414] [14:33.44] which this was said historically. It's
[L415] [14:35.68] why I want it to be a historical talk
[L416] [14:38.64] because who your audience is is a large
[L417] [14:42.80] determiner of what the root of all evil
[L418] [14:44.80] is. Right? If you talking if you're
[L419] [14:47.44] talking to a bunch of people who don't
[L420] [14:48.88] think about optimization at all, then
[L421] [14:50.88] you don't really need to say this phrase
[L422] [14:52.32] to them, right?
[L423] [14:54.24] And so if you fast forward to today when
[L424] [14:56.16] a lot of people don't really take
[L425] [14:57.60] optimization into account at all during
[L426] [14:59.84] their programming um or very very little
[L427] [15:03.52] uh this phrase doesn't make very much
[L428] [15:05.04] sense to someone who does care about
[L429] [15:06.80] performance because like why would you
[L430] [15:07.92] ever say that? It just kind of seems
[L431] [15:08.96] like it encourages people to not be
[L432] [15:11.60] mindful of the performance of their
[L433] [15:12.88] program.
[L434] [15:14.64] But if you rewind to that time
[L435] [15:17.92] and you understand that well a lot of
[L436] [15:20.88] the program you know they had the
[L437] [15:22.48] opposite problem. A lot of the programs
[L438] [15:24.32] at that time what what programming was
[L439] [15:27.12] was coming up with all these crazy
[L440] [15:29.20] little assembly tricks to like shave a
[L441] [15:31.84] cycle off here or there, right? And if
[L442] [15:34.24] you're talking to an auditorium full of
[L443] [15:35.92] people who are really into that sort of
[L444] [15:37.60] thing,
[L445] [15:39.28] uh then it really can be the root of all
[L446] [15:41.20] evil, right? It's like you guys are
[L447] [15:42.48] spending all your time on this, but we
[L448] [15:45.28] have this really big other problem and
[L449] [15:47.28] that is not the right trade-off, right?
[L450] [15:49.04] That is you've you've swung, you know,
[L451] [15:51.44] like calling it trade-offs is a great
[L452] [15:53.28] way to say it. You've swung the pendulum
[L453] [15:55.20] way too far in one of those directions
[L454] [15:57.04] at some point. And and so, you know, to
[L455] [15:59.36] some degree, while I wouldn't while I
[L456] [16:01.60] would highly dispute the the description
[L457] [16:03.84] root of all evil today as a good thing
[L458] [16:06.24] to say to somebody or or that it leaves
[L459] [16:08.56] a good impression, when we rewind to
[L460] [16:10.24] that time period, I think it makes a lot
[L461] [16:11.84] more sense because when you look at what
[L462] [16:13.36] people were actually spending their time
[L463] [16:14.72] doing, where their priorities were, I
[L464] [16:17.20] think that maybe that wasn't so much of
[L465] [16:19.04] an exaggeration. I mean, obviously, it's
[L466] [16:20.56] a hyperbole, but it's less of one. in
[L467] [16:23.68] your slides, there were so many quotes
[L468] [16:26.08] and snippets of really kind of digging
[L469] [16:28.40] into the true history. Was there
[L470] [16:30.24] anything you found that surprised you
[L471] [16:31.84] when you were doing the research?
[L472] [16:33.44] >> I mean, constantly. Uh, absolutely,
[L473] [16:36.32] constantly. And I mean, first of all,
[L474] [16:39.04] I'll just say that there's
[L475] [16:42.80] as a meta point, I'll I'll give you a
[L476] [16:44.56] specific thing that surprised me that's
[L477] [16:46.48] kind of funny. Um, that's that's more
[L478] [16:49.28] about like a technical thing. But first
[L479] [16:51.44] I want to talk about a broader picture
[L480] [16:53.84] which is one of the things that really
[L481] [16:57.12] hits home for me whenever I do these is
[L482] [16:59.60] the personal aspects of it like these
[L483] [17:03.12] people were like friends and competitors
[L484] [17:06.48] and like all these sorts of things and
[L485] [17:08.80] it's all kind of lost to us in a way
[L486] [17:12.24] when we think about computing history in
[L487] [17:14.16] like a sterile way like you know when I
[L488] [17:18.32] read up on what Dystra Dyster was the
[L489] [17:20.96] person who kind of kicked off the
[L490] [17:23.12] structured programming.
[L491] [17:25.76] I don't want to call it a revolution.
[L492] [17:26.96] That's a bit too probably grandiose, but
[L493] [17:29.36] kicked off that train of thought. Say uh
[L494] [17:32.08] he wrote a a thing called notes on
[L495] [17:34.88] structured programming. It was a
[L496] [17:35.92] manuscript or monograph. I don't I don't
[L497] [17:38.56] remember what they called, you know, got
[L498] [17:40.16] like a typewritten like it looks like
[L499] [17:41.52] exactly like a typewriter written thing,
[L500] [17:43.92] right? Um he when he wrote that he was
[L501] [17:48.40] like very depressed like he was having a
[L502] [17:51.04] lot of trouble in his life at that time.
[L503] [17:52.80] He had he had gone through this this
[L504] [17:54.72] situation where uh they had done what
[L505] [17:58.00] people today now recognize as like
[L506] [18:00.16] pioneering work in distributed computing
[L507] [18:02.24] like he and these other uh people at the
[L508] [18:05.20] Einhovven Technological University. I
[L509] [18:07.04] don't I apologize I can't say the proper
[L510] [18:09.12] name for it. It's it's you know it's
[L511] [18:11.52] well beyond my pronunciation
[L512] [18:12.96] capabilities. But point being um he had
[L513] [18:15.84] done this really foundational work in uh
[L514] [18:19.44] distributed computing and published it
[L515] [18:21.92] and people today now recognize it as
[L516] [18:24.24] that it is like undisputedly a massive
[L517] [18:26.40] contribution to distributed computing.
[L518] [18:28.24] He did it with a part-time team of
[L519] [18:30.08] people at the university who this wasn't
[L520] [18:31.68] their job. it was a mathematics
[L521] [18:33.36] department they were in and you know as
[L522] [18:36.32] a result of that uh basically they sort
[L523] [18:38.96] of just got dissolved like the the
[L524] [18:40.80] department of mathematics I guess like
[L525] [18:42.08] he wasn't really specific about it but
[L526] [18:43.92] in his notes like the department of
[L527] [18:45.12] maths was just like they disbanded the
[L528] [18:46.72] team he was like this you know this
[L529] [18:47.84] isn't math or whatever I don't know they
[L530] [18:49.44] just had a a pessimist view of it so um
[L531] [18:52.00] and he was really depressed about that
[L532] [18:53.44] and he wasn't sure what he should do
[L533] [18:54.64] with his life and like you know what's
[L534] [18:56.16] what what's the deal here right and he
[L535] [18:57.84] was having this sort of um I don't want
[L536] [18:59.84] to call it an existential crisis because
[L537] [19:01.36] I don't want again put words in his
[L538] [19:03.04] mouth. These are historical figures and
[L539] [19:05.04] you know I can that's why I try to use
[L540] [19:06.64] quotes to try to show you like what they
[L541] [19:08.32] said. Um but like that's it's just so
[L542] [19:12.00] relatable when you go through the
[L543] [19:13.20] history this way. It it's not just some
[L544] [19:15.12] random guy who wrote some math down in a
[L545] [19:17.20] paper. It's like people were really
[L546] [19:18.56] struggling with this and some of the
[L547] [19:21.04] most important aspects of computer
[L548] [19:22.48] history come out of these amazing human
[L549] [19:24.96] stories. And I found that absolutely
[L550] [19:26.56] fascinating. So, I'll just put that out
[L551] [19:29.04] there as one of the biggest rewarding
[L552] [19:31.36] things about looking into this history
[L553] [19:32.96] if you ever do it is if you can go find
[L554] [19:35.20] the actual writings of the people,
[L555] [19:38.56] like things outside of just their
[L556] [19:40.16] technical papers, it's just fascinating
[L557] [19:42.64] and it's so much more relatable and
[L558] [19:46.16] fascinating because you feel the story.
[L559] [19:48.40] It's not just this abstract computation
[L560] [19:50.88] uh computer science thing that happened.
[L561] [19:52.72] So that's one thing.
[L562] [19:54.96] But the other thing I was going to say
[L563] [19:55.92] is like when you read through this
[L564] [19:57.60] stuff, I'm just I just go through piles
[L565] [19:59.44] of documents and I'm just reading them
[L566] [20:00.88] and seeing, you know, does this fit into
[L567] [20:04.00] this story? You know, should it be part
[L568] [20:05.76] of what I'm telling or is it extraneous?
[L569] [20:07.76] Is it something that, you know, uh is
[L570] [20:10.16] interesting perhaps, but not actually
[L571] [20:11.60] part of it? And one thing that I found I
[L572] [20:14.72] when the VOD of this lecture uh or talk
[L573] [20:17.76] goes up I'm going to uh include this in
[L574] [20:20.64] the notes because I thought it was so if
[L575] [20:22.08] it didn't make it into the talk I found
[L576] [20:24.72] a thing
[L577] [20:26.72] uh like a a uh thing from Tony
[L578] [20:30.40] So, so Charles, Anthony, Richard
[L579] [20:32.40] uh, who again is another massive figure
[L580] [20:34.32] in computer science, right? Hora,
[L581] [20:35.76] Dystra, and Canuth are like, you know,
[L582] [20:37.36] the three amigos and like they they all
[L583] [20:39.36] write to each other, right? And they're
[L584] [20:41.36] very important people in computer
[L585] [20:42.40] science history. So, um, I found a thing
[L586] [20:45.52] by him that was like a a thing he did
[L587] [20:49.12] not decide to pursue. It's like this
[L588] [20:51.36] note where he's talking about, you know,
[L589] [20:53.04] he's talking about this thing that he's
[L590] [20:54.56] thinking of doing. And there's just a
[L591] [20:57.04] handwritten thing on him from later on
[L592] [20:58.80] in his life when he was I guess
[L593] [21:00.40] categorizing these documents. And he
[L594] [21:02.32] just writes down like I decided not to
[L595] [21:04.56] pursue this because you know I I talked
[L596] [21:07.12] about it at this conference that I was
[L597] [21:09.28] at and Peter Nauer who's like again
[L598] [21:12.40] another famous figure in computer
[L599] [21:14.24] science history. If you've ever heard
[L600] [21:15.28] the if you ever looked at um like
[L601] [21:16.72] contextfree grammarss and parsing you've
[L602] [21:19.44] probably heard Bakasau form. He's the
[L603] [21:21.92] ner in Bakasnau form. If you ever heard
[L604] [21:23.76] of the language Al Gallal, he was like a
[L605] [21:25.60] major, you know, figure in in
[L606] [21:27.44] standardizing that and writing up the
[L607] [21:28.80] standard and all this stuff, right? So
[L608] [21:31.44] anyway, Horus like yeah, I I proposed
[L609] [21:34.16] this thing. I went through I said it and
[L610] [21:36.16] like and Peter now was like ah making
[L611] [21:38.56] multipass compilers is easy. I I just
[L612] [21:40.80] wrote a nine pass one. So I was you know
[L613] [21:43.28] I decided not to pursue this, right? So
[L614] [21:45.68] what's the thing? I read through the
[L615] [21:47.36] thing and like maybe I'm just
[L616] [21:50.80] overreading it with the benefit of
[L617] [21:54.24] hindsight, but he pretty much describes
[L618] [21:57.36] static single assignment form like like
[L619] [21:59.44] SSA
[L620] [22:00.96] uh which is a very standard compiler
[L621] [22:02.40] technique developed in the 80s but this
[L622] [22:04.40] note is from the 60s. So it's like in my
[L623] [22:07.92] head I'm like did Peter Nau accidentally
[L624] [22:10.72] set back like computer like like
[L625] [22:14.00] compiler science by 20 years by like
[L626] [22:17.20] telling Tony well 15 let's say by
[L627] [22:19.52] telling Tony like this is not
[L628] [22:21.68] important when actually was would have
[L629] [22:24.00] been like very very important. So uh you
[L630] [22:27.04] find stuff like that all the time where
[L631] [22:28.64] you're like whoa what is this? I I saw
[L632] [22:30.56] another one too. Uh just one more I'll
[L633] [22:32.72] mention.
[L634] [22:34.40] Uh I I can't remember now. I'm sorry. Uh
[L635] [22:36.96] again, your brain kind of turns to mush
[L636] [22:38.80] when you try to dump this many documents
[L637] [22:40.56] into it for a talk. Uh uh there was a a
[L638] [22:43.60] pretty interesting thing I thought where
[L639] [22:45.68] uh uh Margaret Hamilton so the the
[L640] [22:48.64] person who you know managed the Apollo
[L641] [22:51.76] she was she was you know one of the core
[L642] [22:53.84] programmers originally on the project
[L643] [22:55.28] and then then was like the man like the
[L644] [22:57.12] manager of the whole OS like the whole
[L645] [22:59.84] like real-time software that ran the
[L646] [23:02.40] Apollo 11 well all the Apollo uh flight
[L647] [23:05.68] computer stuff right
[L648] [23:07.76] which I mean most people today herald is
[L649] [23:10.00] like a very very significant like
[L650] [23:12.16] real-time systems like achievement in
[L651] [23:14.24] that era, right? Like everyone pretty
[L652] [23:15.76] much agrees uh with that
[L653] [23:18.72] she had to write like a defense. I think
[L654] [23:21.52] it was in the AC the communication to
[L655] [23:23.28] the ACM maybe it was in data like they
[L656] [23:24.88] say apologize I can't remember the venue
[L657] [23:28.08] because like it had been pointed out as
[L658] [23:31.44] like a failure because people didn't
[L659] [23:34.08] understand the context that like the
[L660] [23:36.00] reason that the Apollo computer had to
[L661] [23:37.60] like trip those alarms was because that
[L662] [23:39.60] it had been used improperly like it was
[L663] [23:41.36] used in a configuration it wasn't
[L664] [23:42.72] supposed to and it actually rather than
[L665] [23:44.80] crashing went into backup modes and
[L666] [23:47.20] successfully landed like it it worked
[L667] [23:49.36] like it it actually was a triumph of
[L668] [23:51.36] like fault tolerant engineering and she
[L669] [23:53.68] had to write like a defense of this
[L670] [23:54.96] because people at the time were saying
[L671] [23:56.56] like oh that they screwed up like this
[L672] [23:58.08] is an example of of how why you wouldn't
[L673] [24:00.00] want to do engineering this way or like
[L674] [24:01.68] you know don't write the code this way
[L675] [24:03.44] and so um again stuff like that always
[L676] [24:06.88] makes me think like the more things
[L677] [24:08.32] change the more they stay the same
[L678] [24:09.92] exactly what would happen on Twitter now
[L679] [24:11.52] right like like some very successful
[L680] [24:13.44] thing that people did right they would
[L681] [24:14.88] just get like slandered and say that it
[L682] [24:17.44] was done wrong and there would be like a
[L683] [24:18.72] flame war and then they'd have to come
[L684] [24:19.92] out and have a thing, you know. So,
[L685] [24:21.68] anyway, uh those are just some examples,
[L686] [24:23.76] but there's so much great stuff in
[L687] [24:26.08] there. I highly recommend anyone who
[L688] [24:27.60] likes this kind of thing, you won't be
[L689] [24:28.96] disappointed if you go if you go
[L690] [24:30.24] dumpster diving, as I call it.
[L691] [24:32.08] >> When you said that you saw the human
[L692] [24:34.64] stories and that Dystra was depressed at
[L693] [24:37.28] that time, what did you see that made
[L694] [24:40.16] you realize that?
[L695] [24:42.32] >> One of the nice things about Dystra is
[L696] [24:44.56] that he's kind of a pretty straight
[L697] [24:46.72] shooter. And so I didn't actually have
[L698] [24:49.76] to do any interpretation. He literally
[L699] [24:52.72] talks about like being depressed. And
[L700] [24:55.28] like he has like a there's a paper uh
[L701] [24:57.76] not a paper like a thing that he did
[L702] [25:00.64] that's like a retrospective
[L703] [25:02.80] um on that's like handwritten by him
[L704] [25:05.52] later on in life and he literally says
[L705] [25:07.92] like in this period I was very depressed
[L706] [25:10.32] because of these reasons. Now he could
[L707] [25:13.28] be wrong about the source of his
[L708] [25:14.80] depression, right? Uh, so I don't want
[L709] [25:16.64] to claim that that just because he said
[L710] [25:18.40] it it's ne necessarily true or something
[L711] [25:20.00] like that. But one of the amazing things
[L712] [25:23.44] I I think one of the the really cool
[L713] [25:26.64] things about academics
[L714] [25:29.04] uh especially that era is they just
[L715] [25:31.60] produced a voluminous amount of material
[L716] [25:34.32] and so we don't have to guess that much
[L717] [25:36.56] in the private sector. I think it'd be a
[L718] [25:38.24] lot harder like if you wanted to know uh
[L719] [25:40.64] what people at you know maybe
[L720] [25:44.08] you know Lockheed or something were
[L721] [25:46.24] thinking or doing at that time I imagine
[L722] [25:47.84] it's much more difficult just because
[L723] [25:49.68] you know things are classified or
[L724] [25:51.28] they're not academics so they're not
[L725] [25:52.32] necessarily going to write them all up
[L726] [25:53.84] uh you know so a lot of the internal
[L727] [25:55.12] stuff when we read up academics don't
[L728] [25:56.64] really have that they don't have an
[L729] [25:57.92] incentive or a prohibition on writing up
[L730] [26:00.48] everything they do so they don't just
[L731] [26:02.16] have to have like a public-f facing
[L732] [26:04.08] statement of what they did or a public
[L733] [26:06.00] facing paper of what they and then oh
[L734] [26:07.76] there's this extra secret stuff. The
[L735] [26:09.52] academics don't have that restriction.
[L736] [26:11.36] They're sort of they benefit from being
[L737] [26:14.00] as forthcoming as possible about what
[L738] [26:16.24] they've accomplished. Usually
[L739] [26:17.76] >> I saw in the in the slides that you
[L740] [26:20.40] looked at go to considered harmful that
[L741] [26:22.80] FEMA. Do you have any sense of the the
[L742] [26:25.36] personal or people side of that?
[L743] [26:27.74] [laughter]
[L744] [26:28.48] Uh, so you're talking about the original
[L745] [26:30.32] like Dystra letter to the editor that's
[L746] [26:32.32] like Ed's Gdystra go-to cons uh
[L747] [26:35.52] statement considered harmful. This okay
[L748] [26:38.64] um the complete story is actually
[L749] [26:40.40] relatively simple. He according to him
[L750] [26:44.64] he was at a uh at a conference um uh in
[L751] [26:49.12] Tennessee
[L752] [26:50.80] where he was talking to Brian Randelle
[L753] [26:54.24] who's another computer science guy. um
[L754] [26:56.56] he he doesn't quite get the same level
[L755] [26:58.56] of uh name recognition as a canth or
[L756] [27:01.28] something like that. Uh but he has a lot
[L757] [27:03.20] of papers at that time. Like you can go
[L758] [27:04.64] find him. He's not an obscure he's not
[L759] [27:06.16] an obscure figure. I wouldn't say uh to
[L760] [27:08.32] anyone who reads the history. You'll see
[L761] [27:10.00] him come up. He's talking to Brian
[L762] [27:11.76] Randell and some other people outside.
[L763] [27:13.84] This is exactly like the same thing that
[L764] [27:15.68] happens at modern conferences. There's
[L765] [27:17.68] like the talks and then there's all the
[L766] [27:20.00] stuff that goes down at the bar, right?
[L767] [27:21.84] It's it's very much that they're
[L768] [27:23.20] outside. talking
[L769] [27:25.52] and according to him he's basically
[L770] [27:28.64] giving the same sort of example of a
[L771] [27:32.72] problem with the goto that he gives in
[L772] [27:34.96] the paper right this idea of enumeration
[L773] [27:37.44] we can talk about that later if but um
[L774] [27:39.68] but the sort of a side note
[L775] [27:42.72] he's sort of saying like here this is
[L776] [27:44.56] kind of a problem with with goto and one
[L777] [27:47.04] of the reasons that maybe it's not such
[L778] [27:48.48] a good idea and the people who are
[L779] [27:51.60] listening to him were like you know
[L780] [27:53.04] Brian and the others were like you
[L781] [27:54.56] should p like you should publish that
[L782] [27:56.48] that would be helpful because you know
[L783] [27:58.32] there's these arguments going on about
[L784] [27:59.60] whether goto is good or bad like that
[L785] [28:01.20] was kind of happening at the time
[L786] [28:02.16] already uh since since around 1959 even
[L787] [28:05.52] I think there'd kind of been a little
[L788] [28:06.80] bit of that had been kind of growing
[L789] [28:09.04] this idea that maybe go-to statements
[L790] [28:10.88] weren't weren't um the best idea
[L791] [28:14.08] uh as a way to structure your programs
[L792] [28:16.32] and so he does he goes back to Einhovven
[L793] [28:20.16] and he writes up this same thing he
[L794] [28:23.04] saying basically and he sends it to to
[L795] [28:25.36] communications of the ACM for
[L796] [28:26.88] publication.
[L797] [28:28.72] uh Nicholas Worth who is like the
[L798] [28:31.44] creator of Pascal right a very prominent
[L799] [28:33.28] figure also uh was very heavily involved
[L800] [28:35.60] in alol and all this sort of stuff like
[L801] [28:37.28] you know language designer guy he is the
[L802] [28:40.24] editor uh who is in charge of like
[L803] [28:43.52] getting this getting this thing
[L804] [28:45.04] published I guess I'm not exactly sure
[L805] [28:46.72] how things work at at the communications
[L806] [28:48.24] of the ACM
[L807] [28:50.08] he doesn't want to wait to have it
[L808] [28:52.96] published he doesn't want to take the
[L809] [28:55.12] time to like go through the referee
[L810] [28:57.36] process or whatever. I don't know like
[L811] [28:59.36] at that time what the requirements were
[L812] [29:01.36] for publishing a article in
[L813] [29:03.68] communications with the ACM but I'm sure
[L814] [29:05.68] that it involved a lot of procedure.
[L815] [29:08.08] wasn't just like, "Oh, hey, I'm, you
[L816] [29:09.84] know, I'm the creator of Pascal."
[L817] [29:11.84] Although that that time he wouldn't have
[L818] [29:13.04] been the creator of Pascal yet because
[L819] [29:14.40] Pascal comes later, I think, but but
[L820] [29:15.92] either way, he's like, "Hey, I'm this
[L821] [29:17.44] important guy. I'm just going to put
[L822] [29:18.72] this whatever I want communication."
[L823] [29:20.40] That's not how it worked. And so he
[L824] [29:22.96] decides that in order to get it
[L825] [29:24.32] published more quickly, he's just going
[L826] [29:25.84] to publish it as a letter to the editor
[L827] [29:27.84] because then there's no pro like any,
[L828] [29:29.68] you know, anything goes there as long as
[L829] [29:31.12] the editors are fine with the content, I
[L830] [29:32.48] assume. Like it doesn't have to be
[L831] [29:33.44] refereed, doesn't have to have any kind
[L832] [29:34.80] of review, it doesn't have to uh etc,
[L833] [29:36.88] etc.
[L834] [29:38.56] So, he turns it into a letter to the
[L835] [29:40.56] editor and he takes the name of the
[L836] [29:43.76] thing that Dystra sent, which was a case
[L837] [29:46.48] against the go-to statement. That was
[L838] [29:48.48] what Dyster wrote at the top of the
[L839] [29:50.24] thing as the title. He changes it for
[L840] [29:53.36] letters to the editor to Edgar Dystra
[L841] [29:57.28] go-to statement considered harm or
[L842] [29:59.76] considered harmful. Right?
[L843] [30:02.00] So, it wasn't it wasn't even Dyster's
[L844] [30:05.44] plan to like have it maybe be that
[L845] [30:08.00] confrontational,
[L846] [30:09.76] but that's what happens. Um, now this is
[L847] [30:13.28] not
[L848] [30:14.80] wellreceived to say the least. Uh, the
[L849] [30:19.20] according to can
[L850] [30:21.44] uh again I'm just trying to say who said
[L851] [30:23.20] what here. According to Canuth, Dystra
[L852] [30:26.16] said he got letters like like angry like
[L853] [30:30.16] threatening letters like uh in much the
[L854] [30:32.64] same way you would today, right? Like he
[L855] [30:34.32] got got people who were uh very abusive
[L856] [30:36.88] and at you know telling him off
[L857] [30:39.84] and I'm sure part of that is because by
[L858] [30:42.00] all accounts Dystra himself was also
[L859] [30:44.40] somebody who liked to push people's
[L860] [30:45.68] buttons. That's well acknowledged. Um I
[L861] [30:47.84] think Alan Kay is probably the best
[L862] [30:49.20] source for this. He talks about uh this
[L863] [30:51.44] uh he liked Dystra and they apparently
[L864] [30:53.44] got along well, but you know he he's
[L865] [30:56.16] often said that Dystra was someone who
[L866] [30:57.68] kind of leaned into the being uh sort of
[L867] [31:01.36] brash about stating things about
[L868] [31:03.36] programming and uh and kind of relished
[L869] [31:06.40] that position. So it probably didn't
[L870] [31:08.40] help that he was already sort of known a
[L871] [31:10.16] little bit in that way. But in general
[L872] [31:12.72] that's that's how it went down. And
[L873] [31:15.29] [clears throat]
[L874] [31:16.72] like I said, that wasn't the initial
[L875] [31:20.24] foray against goto statements by any
[L876] [31:22.96] stretch of the imagination, but it it
[L877] [31:25.44] just kind of
[L878] [31:27.60] maybe you call it the straw that broke
[L879] [31:28.96] the camel's back. It was like a it was
[L880] [31:30.64] like a flash point might be the way to
[L881] [31:32.24] say it. And so, and then the title of
[L882] [31:34.80] course be that Nicholas Berth picked uh
[L883] [31:38.08] is quite the doozy and kind of
[L884] [31:40.08] clickbaited everyone, you know, as I
[L885] [31:41.76] call it into that.
[L886] [31:43.68] It's funny. Yeah. Cuz I mean your social
[L887] [31:45.84] media, it's similar patterns, right?
[L888] [31:47.60] People have very explosive first lines
[L889] [31:50.72] and then the comments are full of all
[L890] [31:52.96] this [laughter] hate and stuff. In in
[L891] [31:55.52] their case, I'm guessing this is all
[L892] [31:57.60] papers. So you submit a letter to that.
[L893] [32:00.00] It's a physical thing and people are
[L894] [32:02.48] reading uh
[L895] [32:03.84] >> maybe a newspaper or something. I don't
[L896] [32:05.04] know what.
[L897] [32:05.36] >> Yeah, it's like a periodical like it
[L898] [32:06.88] comes, you know, as a bound. I mean, I
[L899] [32:08.56] guess there's all the things around us
[L900] [32:10.00] here are hard bound, but it's like
[L901] [32:11.68] usually was soft. It was a you know
[L902] [32:13.36] maybe a perfect binding uh kind of bound
[L903] [32:17.28] thing that has you you open it up table
[L904] [32:19.20] of contents and letters editor right and
[L905] [32:22.08] uh yeah like you can go find there are
[L906] [32:26.00] there are a few if you go look at
[L907] [32:28.16] people's personal papers which like like
[L908] [32:29.76] I said if I did this full-time I'm sure
[L909] [32:32.48] I could find out way more stuff than I
[L910] [32:34.48] did right
[L911] [32:36.32] but some people have gone and looked at
[L912] [32:37.76] the personal papers and occasionally
[L913] [32:39.76] some of them have been able to digitize
[L914] [32:41.52] some of those and put them online that
[L915] [32:42.96] we can look at and you can find for
[L916] [32:45.76] example online right now if you search
[L917] [32:47.52] for it uh
[L918] [32:50.96] there's a there's a back and forth
[L919] [32:52.80] letters personal letters between Dystra
[L920] [32:55.52] and a guy who is kind of into functional
[L921] [32:57.60] programming and promoting that and like
[L922] [32:59.60] you can look at the correspondence and
[L923] [33:01.92] it's kind of it's a little it's a little
[L924] [33:05.36] flame worry like like it it really like
[L925] [33:08.08] that's what they did they they didn't
[L926] [33:09.76] have the ability to do like pathy
[L927] [33:11.20] Twitter replies So it was just on paper.
[L928] [33:15.04] Uh and yeah and Canuth did something
[L929] [33:18.24] similar. It wasn't really a flame
[L930] [33:19.92] because he had a at least when reading
[L931] [33:22.56] it comes through as a tremendous amount
[L932] [33:24.40] of respect for the authors of the book
[L933] [33:26.16] structured programming which is uh
[L934] [33:28.08] Dystra and doll. Um he you know
[L935] [33:32.40] one of the things that he published was
[L936] [33:33.92] a series of open letters to them
[L937] [33:36.48] reviewing the book and talking about the
[L938] [33:38.64] things that he didn't find compelling in
[L939] [33:39.92] it. Right? like very respectful. So, it
[L940] [33:43.04] wasn't that one wasn't a a flame war.
[L941] [33:45.52] But that's what they Yeah, that's what
[L942] [33:46.96] they had to do because they didn't have
[L943] [33:48.48] social media. So, you know, Edgar
[L944] [33:51.20] Dystra's uh he wrote like all these
[L945] [33:53.60] things called EWD with a number. It was
[L946] [33:56.24] it was his initials basically. Um and
[L947] [33:59.28] then a number and that's like this like
[L948] [34:01.52] serialized list of all the things he
[L949] [34:03.28] wrote. And he like labels them this way.
[L950] [34:05.28] Like it's not like some historian
[L951] [34:06.80] characterized it after the fact. just
[L952] [34:08.08] like, "Oh, I'm doing a He's like, "I'm
[L953] [34:10.16] doing EWD 937 now." or whatever, right?
[L954] [34:12.96] It's hilarious. Uh, but anyway,
[L955] [34:17.04] several of those have been put online
[L956] [34:19.36] that are not necessarily technical.
[L957] [34:21.76] Like, for example, his trip reports. You
[L958] [34:24.00] can go read those and you can read about
[L959] [34:25.68] like, oh, like I went and I went and
[L960] [34:27.76] stayed at like such and such's house and
[L961] [34:29.84] like we went to dinner or whatever,
[L962] [34:31.12] right? So, you can find like some nice
[L963] [34:33.04] personal anecdotes in even the publicly
[L964] [34:35.12] available stuff. But in terms of like a
[L965] [34:37.28] real like heart-to-heart conversation, I
[L966] [34:39.92] didn't have access to anything like that
[L967] [34:41.60] that wouldn't have just been in a paper
[L968] [34:43.44] more or less normally. Um, so, you know,
[L969] [34:47.04] it's it's a shame. One of the problems
[L970] [34:49.60] with this stuff, it's so interesting,
[L971] [34:52.40] but it's not a job to do. Like, it's
[L972] [34:55.04] like if somehow it was a job, I probably
[L973] [34:57.12] would almost take that job. like like
[L974] [34:59.44] being the person who crawls through and
[L975] [35:00.88] tries to like redo this whole thing.
[L976] [35:03.04] But, you know, computer historian, no
[L977] [35:05.04] one's no one's hiring. Like that's not
[L978] [35:07.36] no one's interested in paying for that.
[L979] [35:08.88] So,
[L980] [35:10.00] >> you have this other talk and the title
[L981] [35:12.32] was just so catching. It was the big
[L982] [35:14.72] oops anatomy of a 35-year mistake.
[L983] [35:18.24] >> Yes.
[L984] [35:18.72] >> What is that 35-year mistake?
[L985] [35:21.12] >> Um, so this was a this was a kind of
[L986] [35:24.64] funny thing that happened to me that I
[L987] [35:26.88] uh then did a historical lecture on I
[L988] [35:32.32] I had worked on systems in the past that
[L989] [35:35.36] were basically like editors like you
[L990] [35:37.84] know you have to m like three 3D
[L991] [35:39.68] graphics editors like you have to multi
[L992] [35:41.12] select things and move them around and
[L993] [35:43.20] there's a bunch of like architecture
[L994] [35:44.72] things you have to learn to be able to
[L995] [35:46.16] write that kind of code and and certain
[L996] [35:47.92] kinds of problems you have to solve like
[L997] [35:49.68] a a very basic one that I would point
[L998] [35:51.76] out that hopefully most people can
[L999] [35:53.28] relate to would be if I have a bunch of
[L1000] [35:57.04] things on the screen. Uh some of which
[L1001] [35:59.20] have a color. So maybe maybe this is a
[L1002] [36:01.92] drawing program and I've got some text
[L1003] [36:03.60] and I've got some shapes and I've got um
[L1004] [36:05.76] some uh strokes, you know, some some
[L1005] [36:08.64] handdrawn stuff, whatever. And I want to
[L1006] [36:10.80] be able to to select a bunch of them and
[L1007] [36:13.20] I want the user interface to present to
[L1008] [36:15.68] me which things I could edit on these
[L1009] [36:18.40] shapes. So I want to be able to edit the
[L1010] [36:19.84] color and I want it to apply to all of
[L1011] [36:21.28] them. Right? This is just a basic
[L1012] [36:23.36] architectural problem that you have to
[L1013] [36:24.72] solve if you're going to write one of
[L1014] [36:25.68] these programs and you want it to be any
[L1015] [36:26.72] good. oftentimes you will see programs
[L1016] [36:29.12] where the person didn't solve this
[L1017] [36:30.32] problem and you can't do that. It's very
[L1018] [36:32.00] frustrating, right? So a good program
[L1019] [36:34.40] someone has solved that architectural
[L1020] [36:35.84] problem in some way
[L1021] [36:38.56] and I was watching um I just happened to
[L1022] [36:41.36] be watching because sometimes I do like
[L1023] [36:42.96] I like to watch old videos of computer
[L1024] [36:45.60] science pioneer stuff and I was watching
[L1025] [36:48.08] a a demo of Sketchpad. I'd seen it
[L1026] [36:50.24] before, but I was watching a de demo of
[L1027] [36:52.16] Ivan Southern Sketchpad. And Sketchpad,
[L1028] [36:54.16] for those who don't know, is a
[L1029] [36:55.44] groundbreaking computer graphics
[L1030] [36:57.28] program. It's done with a light pen. Uh,
[L1031] [37:01.28] and it was done in the early 60s. And
[L1032] [37:03.36] you could draw things like you do in a
[L1033] [37:05.84] modern CAD program and you could do
[L1034] [37:08.64] stuff that even a lot of modern CAD
[L1035] [37:10.88] programs don't really offer or only
[L1036] [37:13.04] offered recently. I think in the talk I
[L1037] [37:14.64] said in 2007 was the first time that
[L1038] [37:16.64] like AutoCAD got some of these features.
[L1039] [37:19.20] You could do stuff like say these two
[L1040] [37:21.04] shapes like this line has to be
[L1041] [37:22.88] perpendicular to that line, constrain
[L1042] [37:24.80] it, and you could just do whatever you
[L1043] [37:26.08] want with the drawing and it would like
[L1044] [37:27.36] resolve for like making that happen. And
[L1045] [37:29.52] these are very rare in programs even to
[L1046] [37:31.60] this day. Like that's just not a common
[L1047] [37:33.20] operation you would see in a drawing
[L1048] [37:34.48] package today. So [clears throat]
[L1049] [37:38.00] I was looking at this and I was like,
[L1050] [37:40.64] how the heck did he solve this
[L1051] [37:43.52] architectural problem? like how did he
[L1052] [37:47.60] do this stuff in the early 1960s like in
[L1053] [37:51.68] assembly language with no editing tools,
[L1054] [37:55.76] no debugging tools. I mean, this would
[L1055] [37:57.52] have been like, you know, either punch
[L1056] [38:00.48] cards or one step away from punch cards.
[L1057] [38:02.32] Like, it it would have been hard to
[L1058] [38:05.12] develop this stuff.
[L1059] [38:07.28] And when I went back and I went through
[L1060] [38:09.20] his thesis and I looked at the code,
[L1061] [38:11.28] it's actually documented how he did it.
[L1062] [38:13.20] And I realized like, oh crap, this is
[L1063] [38:16.32] actually like an entity component system
[L1064] [38:18.80] basically like what we would now
[L1065] [38:21.12] consider sort of stateofthe-art
[L1066] [38:24.72] of real time architecture for doing
[L1067] [38:28.40] these kind of operations meaning
[L1068] [38:30.32] crosscutting like operating on this kind
[L1069] [38:33.76] of property across many things at once
[L1070] [38:36.64] that are all kind of different.
[L1071] [38:39.68] And this was something that
[L1072] [38:41.28] object-oriented programming, I'm
[L1073] [38:42.80] editorializing now. Bunch of people will
[L1074] [38:44.80] complain that I'm saying this, but this
[L1075] [38:46.00] is just my opinion. Object-oriented
[L1076] [38:48.32] programming and the pedagogy around it
[L1077] [38:50.88] really struggled with that problem for a
[L1078] [38:52.80] long time because there were teaching
[L1079] [38:54.64] despite people who will now claim
[L1080] [38:56.48] otherwise. I document it very completely
[L1081] [38:58.08] in the talk. So I I don't think they
[L1082] [39:00.08] have any leg to stand on. But the
[L1083] [39:01.84] pedagogy at the time was all about build
[L1084] [39:03.76] a domain model. The domain model looks
[L1085] [39:06.32] like your hierarchy basically like I've
[L1086] [39:08.56] got employees and employees I've got
[L1087] [39:10.96] contractors and I've got derived like is
[L1088] [39:13.52] this a full-time employee or a part-time
[L1089] [39:15.20] employee like that was how they
[L1090] [39:17.44] suggested these things should be
[L1091] [39:19.28] implemented right and that kind of
[L1092] [39:21.52] architecture doesn't work for these
[L1093] [39:24.08] kinds of operations that I'm talking
[L1094] [39:26.16] about identity component systems do and
[L1095] [39:28.88] generally that kind of sort of uh
[L1096] [39:31.28] rotated architecture I might call it uh
[L1097] [39:33.92] does work for these.
[L1098] [39:36.16] And so what I call the 35 mistake is the
[L1099] [39:38.88] fact that
[L1100] [39:41.04] I very ironically in my opinion
[L1101] [39:44.32] sketchpad sort of showed in its
[L1102] [39:46.72] architecture how you could solve this
[L1103] [39:48.56] problem and how you could solve it in
[L1104] [39:50.24] arguably an object-oriented way. I think
[L1105] [39:52.72] if you squint at it, a person who does
[L1106] [39:54.56] object-oriented programming could easily
[L1107] [39:56.16] make an argument that you could do an
[L1108] [39:57.44] object-oriented version of this. You
[L1109] [39:59.04] don't have to violate any particular
[L1110] [40:00.64] principles to do it. It's just not the
[L1111] [40:03.84] hierarchy domain model way that people
[L1112] [40:07.44] were conceptualizing it through a lot of
[L1113] [40:09.36] the, you know, 80s and 90s, let's say,
[L1114] [40:12.40] and even unfortunately to this day, but,
[L1115] [40:14.24] you know, I think a lot of object
[L1116] [40:15.60] ordering programs don't do that anymore.
[L1117] [40:18.00] Ironically, that was in Sketchpad. The
[L1118] [40:20.40] DNA was there and we could have had it
[L1119] [40:22.32] right away because Ivan Sutherland
[L1120] [40:24.24] figured it out. But weirdly enough, the
[L1121] [40:27.60] whole idea of this sort of uh
[L1122] [40:29.76] inheritance hierarchy with lots of
[L1123] [40:31.68] encapsulation around it
[L1124] [40:34.48] grew in part out of Sketchpad because
[L1125] [40:37.52] like Alan K looked at it and said like,
[L1126] [40:39.68] "Oh, the interesting part of this is the
[L1127] [40:42.40] fact that you could take a a shape and
[L1128] [40:44.64] not know what it was and just have this
[L1129] [40:46.80] like draw a circle call on it or
[L1130] [40:48.48] something." That was the part they took
[L1131] [40:50.08] away from it, which is much less
[L1132] [40:51.20] interesting in my opinion and not that
[L1133] [40:52.72] architecturally useful in most cases.
[L1134] [40:55.60] So in kind of this amusing way,
[L1135] [40:57.84] Sketchpad contained in if if you know
[L1136] [41:00.48] I'm editorializing it contained what I
[L1137] [41:03.28] consider to be a good architectural
[L1138] [41:05.04] idea, but the takeaway from it was a bad
[L1139] [41:07.68] architectural idea is is how I would say
[L1140] [41:09.68] it. And saying bad architectural idea is
[L1141] [41:11.60] a little bit strong because as I say in
[L1142] [41:13.20] the talk, I think there are times when
[L1143] [41:15.04] you do want to think like a very high
[L1144] [41:17.04] level, you might want to think about
[L1145] [41:18.24] things in kind of the way that you know
[L1146] [41:20.88] small talk thinks about them. Um, so I
[L1147] [41:23.28] don't want to say bad idea in the
[L1148] [41:24.48] absolute sense, but bad in the way it
[L1149] [41:26.08] ended up being uh, you know, applied,
[L1150] [41:28.88] let's say.
[L1151] [41:29.84] >> Why is that class hierarchy not work for
[L1152] [41:32.32] this problem?
[L1153] [41:33.36] >> It's it's pretty easy to understand
[L1154] [41:34.96] actually. So when you think through an
[L1155] [41:38.00] inheritance hierarchy that's based on
[L1156] [41:39.76] sort of what you see in the real world
[L1157] [41:42.32] or what you're trying to model. So you
[L1158] [41:44.40] say like uh the typical example and it's
[L1159] [41:46.88] brought up tons of times by uh people
[L1160] [41:49.44] who wrote the oop literature like be
[L1161] [41:51.36] true strip uh like the small talk people
[L1162] [41:54.64] is the idea is uh keeping it with a
[L1163] [41:57.04] sketch pad example I'm going to have a
[L1164] [41:58.32] shape from the shape I'm going to derive
[L1165] [42:00.40] like triangle or circle and the
[L1166] [42:04.40] encapsulation is around that thing. So a
[L1167] [42:07.28] circle has a radius but shapes don't
[L1168] [42:10.48] have radiuses. shapes don't necessarily
[L1169] [42:13.28] know what that is, right? So, it tends
[L1170] [42:15.20] to get deferred down and the
[L1171] [42:16.48] encapsulation boundary is drawn around
[L1172] [42:19.52] that sort of derived class that's like
[L1173] [42:21.60] the most derived version of whatever
[L1174] [42:23.76] this thing is, right?
[L1175] [42:25.92] The problem is that creates a lot of
[L1176] [42:29.04] headaches when now something that wants
[L1177] [42:31.12] to work across a lot of shapes needs to
[L1178] [42:34.40] actually do something intelligent with
[L1179] [42:37.92] modifying say the scale of something or
[L1180] [42:41.12] wanting to change its color because it
[L1181] [42:43.28] doesn't really have a way to know what's
[L1182] [42:45.44] going on in these highly encapsulated
[L1183] [42:47.60] things.
[L1184] [42:49.52] So typically what you end up having to
[L1185] [42:51.12] do in those sit in those situations is
[L1186] [42:53.20] you then have to take this inheritance
[L1187] [42:54.64] hierarchy and kind of in a sense throw
[L1188] [42:56.56] away the benefits of it. you end up
[L1189] [42:58.56] having to make at the top all of these
[L1190] [43:00.80] accessor iterator things that allow you
[L1191] [43:03.12] to probe into that like lower class and
[L1192] [43:07.20] say tell me all of the colors that you
[L1193] [43:09.68] might be using and a name for them,
[L1194] [43:11.92] right? Or and so in a sense what you end
[L1195] [43:14.40] up having to do when you want the
[L1196] [43:16.00] architecture to work is you have to
[L1197] [43:17.68] rebuild the sketchpad version on top of
[L1198] [43:21.12] the inheritance hierarchy version which
[L1199] [43:22.80] doesn't really do anything for you,
[L1200] [43:24.08] right? And it's not to say that there
[L1201] [43:25.84] isn't some benefit that you can derive
[L1202] [43:28.56] from having derived is kind of a pun
[L1203] [43:30.64] here I guess that you can derive from
[L1204] [43:32.32] having this idea of saying this thing is
[L1205] [43:35.60] like this other thing. Please give me
[L1206] [43:37.60] some of the implementation of it. That's
[L1207] [43:39.52] not necessarily a bad thing in practice.
[L1208] [43:41.92] The problem is when you teach people
[L1209] [43:43.60] that this is how it's going to work.
[L1210] [43:45.04] Like you just make this hierarchy and
[L1211] [43:46.40] then your architecture is just supposed
[L1212] [43:47.76] to work. it really illprepares them for
[L1213] [43:50.56] the reality that like that's actually
[L1214] [43:52.16] not going to solve most of most of the
[L1215] [43:53.76] problems that you have are not going to
[L1216] [43:54.88] be solved that way. Um and again it just
[L1217] [43:57.28] comes from this fact that typically when
[L1218] [43:58.88] we're working with computer programs
[L1219] [44:01.04] most of the time what we need to do is
[L1220] [44:03.28] create crosscutting operations that work
[L1221] [44:06.72] with a lot of the data that's inside
[L1222] [44:08.80] these derived classes. that's actually
[L1223] [44:10.80] the thing that we want to do and it's
[L1224] [44:13.04] really cumbersome and typically a bad
[L1225] [44:15.52] fit for the problem space to put that
[L1226] [44:17.92] into some virtual functions that are
[L1227] [44:20.16] sitting at the top of this very uh sort
[L1228] [44:22.24] of tall hierarchy. It's usually much
[L1229] [44:24.40] better to do uh again even if you're
[L1230] [44:27.44] doing object programming you don't have
[L1231] [44:28.96] to stop doing objecting program you just
[L1232] [44:30.48] have to think about it differently you
[L1233] [44:32.56] have to think about what the objects are
[L1234] [44:34.24] differently uh where you're drawing the
[L1235] [44:35.92] encapsulation boundaries it just helps
[L1236] [44:37.76] to think about it differently and say
[L1237] [44:39.52] actually the more important things to
[L1238] [44:40.88] model are what are the things that stuff
[L1239] [44:42.88] is built out of how do I build a circle
[L1240] [44:46.24] out of objects right what are those
[L1241] [44:48.88] things a radius property a center
[L1242] [44:51.28] property those maybe should be the
[L1243] [44:53.28] objects that I'm thinking of as more
[L1244] [44:55.36] first class citizens and this
[L1245] [44:57.12] inheritance hierarchy stuff about what
[L1246] [44:58.64] the objects are that I see on the screen
[L1247] [45:00.00] like triangle and circle that's a
[L1248] [45:02.00] distraction that's not the proper way to
[L1249] [45:03.84] model the problem um and again I don't
[L1250] [45:06.72] think I would be pissing off any
[L1251] [45:08.16] object-oriented programmers by saying
[L1252] [45:09.84] that today because I think a lot of them
[L1253] [45:12.08] use architectures that do think about
[L1254] [45:15.04] objects in that sort of rotated sense
[L1255] [45:17.84] and not in the domain model hierarchy
[L1256] [45:19.76] sense not that there aren't still people
[L1257] [45:21.04] who are doing that but you know It's
[L1258] [45:22.96] it's not the only way to to go nowadays.
[L1259] [45:25.52] It's not the only way it's promulgated.
[L1260] [45:28.56] Yeah, because I guess my immediate
[L1261] [45:29.76] thought would have been in in that case
[L1262] [45:32.56] the the base class has the notion of a
[L1263] [45:35.44] color or some shared thing and we just
[L1264] [45:38.32] operate if you're a shape then we assume
[L1265] [45:40.80] you have a color and we but you're
[L1266] [45:42.64] saying refactoring and putting up in
[L1267] [45:45.20] there's suboptimal and there's you want
[L1268] [45:48.32] all these uh subasses to have some
[L1269] [45:51.84] handle to some radius property or
[L1270] [45:54.40] something like that. is that
[L1271] [45:55.68] >> what you just described is what tends to
[L1272] [45:57.84] happen in systems that are architected
[L1273] [45:59.44] this way. you end up with your derived
[L1274] [46:01.20] class not really being very much of
[L1275] [46:03.20] anything because in order to edit stuff
[L1276] [46:05.44] you had to migrate it all up to the top
[L1277] [46:08.08] and that there was actually terms for
[L1278] [46:09.76] this uh in the old days I don't still
[L1279] [46:11.20] use like fatty base classes right are
[L1280] [46:13.36] things like that's like it just ends up
[L1281] [46:14.96] your base class has like every type of
[L1282] [46:16.72] property that any derived class might
[L1283] [46:18.56] ever have like you have like get primary
[L1284] [46:20.64] color get secondary color get tertiary
[L1285] [46:22.16] color get right because it's like
[L1286] [46:23.36] something needed three different colors
[L1287] [46:24.72] or whatever uh and most things don't use
[L1288] [46:27.04] those colors and all these other sorts
[L1289] [46:28.72] of things
[L1290] [46:29.92] And so um there's certainly nothing
[L1291] [46:32.08] wrong with running a program that way.
[L1292] [46:33.44] It's just again why did you bother with
[L1293] [46:35.20] the hierarchy? Like you're not getting
[L1294] [46:36.88] any actual encapsulation benefits from
[L1295] [46:38.88] it because you just forced everything to
[L1296] [46:40.56] the base class anyway. So why didn't you
[L1297] [46:42.00] just make that be your thing? Just make
[L1298] [46:43.76] one class called shape and be done.
[L1299] [46:46.16] Right? So uh in terms of the the ECS
[L1300] [46:50.24] style of implementation and I don't
[L1301] [46:51.84] necessarily want to advocate for it or
[L1302] [46:53.76] not because uh I I don't actually
[L1303] [46:55.76] personally use ECS's or anything like
[L1304] [46:57.44] that but they are very common. Now
[L1305] [47:00.32] the idea there is to just turn it on its
[L1306] [47:02.16] side and say look typically what we want
[L1307] [47:04.88] to do is do things like okay there's
[L1308] [47:07.20] stuff that has like physics on it like
[L1309] [47:09.44] you know I'm I'm doing this thing and
[L1310] [47:10.56] and I want to have like physical
[L1311] [47:12.00] simulation of of entities. Well, the
[L1312] [47:14.64] physics system is the thing that
[L1313] [47:15.92] probably knows how that should be
[L1314] [47:17.12] stored. So rather than having that be
[L1315] [47:19.68] data in my derived class that is
[L1316] [47:22.24] encapsulated around the derived class.
[L1317] [47:24.24] Instead, why don't I just have the
[L1318] [47:25.84] physics system knows what physics is.
[L1319] [47:28.72] And then if you want to make something
[L1320] [47:30.32] that participates in physics, you just
[L1321] [47:32.56] have a handle for whatever this thing
[L1322] [47:34.72] is, like a handle for my shape. That
[L1323] [47:36.64] handle is valid in all the systems. So I
[L1324] [47:38.96] can go look up the physics properties of
[L1325] [47:41.04] the shape and gather it when I want to
[L1326] [47:43.84] actually do something with it. But
[L1327] [47:45.36] generally speaking, the encapsulation
[L1328] [47:47.20] stays around the system. So physics
[L1329] [47:49.84] properties are defined by the physics
[L1330] [47:51.60] system because hey, that's who knows how
[L1331] [47:53.76] physics should work and I just ask about
[L1332] [47:57.12] my physics when I need to do something
[L1333] [47:58.64] with it. And this kind of gets you out
[L1334] [48:00.32] of that problem. And then now you can
[L1335] [48:02.24] just compose things. Oh, I want to make
[L1336] [48:04.16] something that has several physics
[L1337] [48:05.68] elements in it. Fine. I can just have
[L1338] [48:07.36] multiple physics handles if that's what
[L1339] [48:08.64] I need or something like this. I can
[L1340] [48:10.00] very flexibly like merge these things
[L1341] [48:11.76] together. I want something to not have
[L1342] [48:13.52] physics. I just don't ever insert the,
[L1343] [48:15.92] you know, I don't ever ask the physics
[L1344] [48:17.12] system to have a valid, you know, piece
[L1345] [48:19.76] of data for this handle in it and it
[L1346] [48:21.28] won't simulate any physics for it.
[L1347] [48:22.80] Right? Whether that's the world's best
[L1348] [48:26.00] architecture or not, I'm not going to
[L1349] [48:27.92] argue for it or against it. It's just
[L1350] [48:29.68] it's a lot better than domain model
[L1351] [48:31.36] hierarchies. That I will say, right?
[L1352] [48:34.40] OpenAI, Enthropic, Cursor, and Verscell
[L1353] [48:38.16] all use this product to make their lives
[L1354] [48:40.00] better. And the problem it solves is
[L1355] [48:42.56] when you're building SAS or an AI
[L1356] [48:44.40] product and you want to sell to other
[L1357] [48:46.32] companies, there's all these
[L1358] [48:47.84] requirements you need to meet. There's
[L1359] [48:49.76] SSO, there's skim, there's arbback,
[L1360] [48:53.04] there's audit logs. These are all things
[L1361] [48:54.88] that take time to integrate but aren't
[L1362] [48:57.04] the main focus of your app. Work OS is
[L1363] [48:59.36] an API layer that lets you meet all of
[L1364] [49:01.20] these requirements in just a few lines
[L1365] [49:03.44] of code. So let's say you have a new SAS
[L1366] [49:05.84] product and you want to sell to other
[L1367] [49:07.44] companies. Work OS will solve all of
[L1368] [49:09.68] these critical feature gaps for you. You
[L1369] [49:12.40] can check them out at workos.com to
[L1370] [49:14.88] learn more and get started. And I
[L1371] [49:17.04] appreciate them for supporting my work
[L1372] [49:18.72] and sponsoring this podcast. Jira
[L1373] [49:21.28] byatlassian isn't just for tracking work
[L1374] [49:23.52] anymore. Now you can pick your favorite
[L1375] [49:25.36] AI agent to assign tasks to and they'll
[L1376] [49:28.08] get access to the rich context that's
[L1377] [49:30.08] already in Jira. When the agent is done,
[L1378] [49:32.32] it surfaces a poll request. That way you
[L1379] [49:34.72] can get more done with your favorite
[L1380] [49:36.32] agents all in one place. Learn more at
[L1381] [49:39.28] jira.dev. That's jir.dev.
[L1382] [49:44.00] Appreciate them for sponsoring the
[L1383] [49:45.44] podcast. And back to the show. [snorts]
[L1384] [49:47.92] Earlier we talked about the the
[L1385] [49:49.68] trade-off between I guess performant
[L1386] [49:52.48] code and maintainable code and I saw you
[L1387] [49:56.80] had this one video said you know in
[L1388] [49:59.12] quotes clean code horrible performance
[L1389] [50:03.12] I feel like this is on the same topic.
[L1390] [50:05.60] What's your your take there on you know
[L1391] [50:08.80] because you also put clean code in
[L1392] [50:10.96] quotes. What does that mean?
[L1393] [50:12.56] >> So it's a it's a fairly subtle topic
[L1394] [50:14.72] right? Uh, and that's why the the quotes
[L1395] [50:16.88] are there because um the first thing
[L1396] [50:18.80] that I you have to point out is that
[L1397] [50:20.64] clean code is clean code,
[L1398] [50:23.28] object-oriented programming, a lot of
[L1399] [50:25.44] these phrases, they mean different
[L1400] [50:27.04] things to different people. And so if
[L1401] [50:29.04] you're going to say that you're, you
[L1402] [50:30.40] know, this code is clean, it's pretty
[L1403] [50:33.04] hard to find two programmers who will
[L1404] [50:36.08] agree on exactly whether it is or not,
[L1405] [50:38.96] right? Like like they all have like
[L1406] [50:40.40] different ideas about what is clean and
[L1407] [50:42.56] what is not,
[L1408] [50:43.36] >> right?
[L1409] [50:44.48] So the reason I put that in quotes is I
[L1410] [50:46.16] was talking about a very specific thing
[L1411] [50:47.36] which is like literally like the book
[L1412] [50:49.60] clean code like the thing where there's
[L1413] [50:51.36] like here are the things that we would
[L1414] [50:52.64] recommend that you do right so in that
[L1415] [50:55.60] particular case what I was talking about
[L1416] [50:56.80] is there's a certain set of ideas that
[L1417] [51:00.64] is advocated in clean code as like these
[L1418] [51:02.88] are the things you should do and they
[L1419] [51:05.12] are like you should have uh everything
[L1420] [51:07.44] should be kind of um I guess I would say
[L1421] [51:11.68] dynamic dispatch or at least You
[L1422] [51:13.84] shouldn't code shouldn't know the types
[L1423] [51:15.36] it's operating on. Right? Saying it's
[L1424] [51:17.36] dynamic dispatch is maybe it depends on
[L1425] [51:19.36] the language whether that's going to be
[L1426] [51:20.56] true or not. But when I write code I
[L1427] [51:22.64] don't know what types I have. It's just
[L1428] [51:24.40] I don't know like some base classes is
[L1429] [51:26.00] what I'm operating on and they could be
[L1430] [51:27.36] anything. Right? That's thing one. Thing
[L1431] [51:29.52] two is functions should be very small.
[L1432] [51:31.68] Uh in fact the the numbers are kind of
[L1433] [51:33.92] weird. They're like four lines or five
[L1434] [51:36.08] line. Like when you go look at the
[L1435] [51:37.44] actual things that are claimed in some
[L1436] [51:38.80] of the this literature it's it's really
[L1437] [51:40.72] strange. you're just like, gosh, that's
[L1438] [51:42.80] very small, right? Um, and I go through
[L1439] [51:46.88] some of those things and I say, look, if
[L1440] [51:48.40] we were to actually follow these, we get
[L1441] [51:51.20] into a really bad state because a lot of
[L1442] [51:53.92] the languages that people are going to
[L1443] [51:55.28] be using to implement this stuff, like
[L1444] [51:56.96] C++ for example, um, which even would be
[L1445] [51:59.60] a fairly good case in a lot of because
[L1446] [52:01.68] at least it's a compiled language and so
[L1447] [52:03.36] on.
[L1448] [52:05.28] In a a lot of cases, these things are
[L1449] [52:07.04] kind of a recipe for disaster if you're
[L1450] [52:10.40] if you're handing out types where you
[L1451] [52:12.48] can't know the type at compile time or
[L1452] [52:14.64] you can't know the type uh or it's or
[L1453] [52:16.40] it's you know going to be in a different
[L1454] [52:17.68] module. So, you know, unless you have
[L1455] [52:19.04] like a really aggressive link time code
[L1456] [52:20.56] generation, it's not going to be likely
[L1457] [52:21.76] that you could figure this out and
[L1458] [52:23.28] you're saying all the functions should
[L1459] [52:24.40] be very small and of course they're
[L1460] [52:25.60] going to be virtual because they're on
[L1461] [52:26.96] these sort of types that you don't know
[L1462] [52:28.08] what they are.
[L1463] [52:29.92] This creates a really uh toxic
[L1464] [52:32.32] combination for the compiler. Normally
[L1465] [52:36.00] you can have I mean you can have small
[L1466] [52:39.04] functions if you want them only four
[L1467] [52:40.32] lines long. If the compiler can know
[L1468] [52:42.32] that it can just inline that, right? If
[L1469] [52:44.24] it can see clearly what you're doing and
[L1470] [52:46.24] it can just merge those things in, we
[L1471] [52:48.00] don't have a problem. If they're behind
[L1472] [52:49.52] a virtual function, so it doesn't know
[L1473] [52:51.76] like it can't guarantee that it is that
[L1474] [52:54.08] type. Um it can't do that. And so when
[L1475] [52:58.32] you talk about all this stuff, what
[L1476] [52:59.76] you're what you're giving up people I
[L1477] [53:01.52] think also because the video I mean the
[L1478] [53:03.20] video was a very short video as part of
[L1479] [53:04.72] like a series
[L1480] [53:06.56] I think people sometimes get the wrong
[L1481] [53:07.84] idea that I think that virtual function
[L1482] [53:09.28] calls cost a lot. They do cost something
[L1483] [53:11.68] but you know depending on how you want
[L1484] [53:13.36] to look at it they actually don't cost
[L1485] [53:14.56] that much. Uh because you know it
[L1486] [53:17.04] depends on whether it's predicted
[L1487] [53:18.56] correctly or not but in general like the
[L1488] [53:20.48] cost of virtual function is less than
[L1489] [53:21.84] you would think. A lot of times
[L1490] [53:24.24] the actual reason that it slows things
[L1491] [53:25.92] down is because the compiler cannot
[L1492] [53:27.60] merge the code together, right? It can't
[L1493] [53:29.60] inline stuff and remove and reduce the
[L1494] [53:31.68] waste. Like that's the actual problem.
[L1495] [53:34.32] So if you just want to call a virtual
[L1496] [53:35.76] function, yeah, it if it was a really
[L1497] [53:38.24] really uh hardcore optimization
[L1498] [53:40.56] scenario, then you don't want anything
[L1499] [53:42.48] probably calling a virtual function in
[L1500] [53:44.00] general because there is some cost to
[L1501] [53:45.36] that. Just calling a function has cost.
[L1502] [53:48.56] But that wasn't the really bad part of
[L1503] [53:50.80] it, right? So, it's that plus there's an
[L1504] [53:53.68] additional thing which is that it can't
[L1505] [53:55.52] unroll and go wide on things. If the
[L1506] [53:57.52] compiler can see everything you're
[L1507] [53:58.80] doing, it can use SIMD. It can like
[L1508] [54:01.20] widen loops to operate on multiple
[L1509] [54:02.88] things at once. It can unroll those
[L1510] [54:04.16] loops. There's all these things it can
[L1511] [54:05.28] do. If it's got these virtual functions,
[L1512] [54:06.80] it's just like that's it. I don't know.
[L1513] [54:09.52] I I can't make decisions about that. I
[L1514] [54:11.04] have no idea what this thing on the
[L1515] [54:12.00] other end is doing. Right? So, uh that
[L1516] [54:14.96] was kind of my point on that. And uh
[L1517] [54:17.36] again I it's not meant to be uh
[L1518] [54:19.76] assailing the idea that your code should
[L1519] [54:21.68] be easy to read or easy to maintain.
[L1520] [54:23.68] It's just more like these guidelines
[L1521] [54:25.44] seem really bad. And also I don't think
[L1522] [54:27.60] we need them for code to be
[L1523] [54:29.20] maintainable. I I don't have trouble
[L1524] [54:31.12] maintaining functions that are 30 lines
[L1525] [54:32.80] long or 50 lines long. I don't find that
[L1526] [54:34.72] five is a magic number or something or
[L1527] [54:36.16] that has to be really short. Uh and also
[L1528] [54:38.00] I find that it's usually pretty easy to
[L1529] [54:39.52] write code where I know what the types
[L1530] [54:41.04] are. Um that those can be determined at
[L1531] [54:42.96] compile time. Like I don't think that
[L1532] [54:44.88] results in code that's particularly hard
[L1533] [54:47.36] to read.
[L1534] [54:48.80] >> When I was in college very and very
[L1535] [54:51.36] early I remember people recommend that
[L1536] [54:53.84] book say oh you should read clean code.
[L1537] [54:56.32] >> So my understanding that you wouldn't
[L1538] [54:57.76] recommend people who are software
[L1539] [54:59.76] engineers to read that.
[L1540] [55:01.92] >> I guess the way I would categorize it's
[L1541] [55:03.52] a mixed bag. So I would I wouldn't
[L1542] [55:05.44] actually say that I disagree with all
[L1543] [55:07.52] all of the things in the book though. I
[L1544] [55:09.20] mean some of the things are things that
[L1545] [55:10.80] I definitely do myself like giving um
[L1546] [55:14.16] variables like easy to understand names
[L1547] [55:17.36] uh is something that I think would be
[L1548] [55:19.20] and that's in that book uh is good
[L1549] [55:21.76] advice right and so kind of more I
[L1550] [55:24.96] wouldn't I wouldn't necessarily say do
[L1551] [55:26.48] or don't read a book what I would say is
[L1552] [55:28.40] like I think there's some things in this
[L1553] [55:30.32] book that don't that aren't addressed
[L1554] [55:32.72] properly like I don't think you want to
[L1555] [55:34.56] tell people these rules of thumb and not
[L1556] [55:36.32] tell them about these other problems
[L1557] [55:38.16] That was exactly what I was uh pointing
[L1558] [55:40.72] out there. And so usually it's more that
[L1559] [55:43.36] it's like
[L1560] [55:45.92] I find that often times there is this
[L1561] [55:49.44] tendency
[L1562] [55:51.20] um I guess I'll say to pretend
[L1563] [55:54.32] that
[L1564] [55:55.84] we don't have to talk about performance
[L1565] [55:57.84] and we can just say like in fact
[L1566] [55:59.52] premature optimization is root all evil.
[L1567] [56:01.36] Bringing it back to there. I feel like
[L1568] [56:03.36] there's this uh temptation and very
[L1569] [56:06.96] prevalent practice of sort of taking
[L1570] [56:09.04] that idea to mean we don't have to talk
[L1571] [56:12.16] about performance when we're teaching
[L1572] [56:13.28] people things at all. Or like when you
[L1573] [56:15.28] write the book clean code, you don't
[L1574] [56:16.64] have to talk about performance at all.
[L1575] [56:17.84] can just include a thing that's
[L1576] [56:19.68] basically like hey um you know there's
[L1577] [56:23.76] performance issues but most of the time
[L1578] [56:25.44] it's not a problem or something like
[L1579] [56:26.48] that which is you know or if you look at
[L1580] [56:28.72] uh refactoring the book refactoring very
[L1581] [56:32.00] popular it literally says exactly that
[L1582] [56:33.36] in like the opening thing it's like you
[L1583] [56:34.48] know there there might be performance
[L1584] [56:35.76] concerns but you know they're usually
[L1585] [56:37.68] okay or something right and it's like
[L1586] [56:39.44] that is not true I just think that's
[L1587] [56:41.68] fundamentally not true I think these
[L1588] [56:43.20] books should include detailed
[L1589] [56:46.00] discussions of the actual performance
[L1590] [56:48.48] problems that you are very likely to hit
[L1591] [56:50.32] if you take some of their advice. Um
[L1592] [56:52.96] because it's not that it means you can't
[L1593] [56:56.08] do those things, but I'll quote you back
[L1594] [56:59.28] to you. It's about trade-offs. There is
[L1595] [57:02.08] always a trade-off that you're making.
[L1596] [57:04.56] And sometimes if you understand the
[L1597] [57:06.88] trade-off, you will make it. You'll say,
[L1598] [57:09.52] I know this is going to cost this may be
[L1599] [57:11.52] a serious performance problem for us,
[L1600] [57:13.52] but I think that's okay. Like I think
[L1601] [57:15.76] it's not like our performance won't
[L1602] [57:17.36] suffer to the point where it's a problem
[L1603] [57:19.04] for the product. I understand what
[L1604] [57:22.16] that's is. There's a huge difference
[L1605] [57:24.80] between that and just going like ah we
[L1606] [57:26.96] don't worry about performance till the
[L1607] [57:28.00] end, right? Like there's it's completely
[L1608] [57:29.60] different, right? Those are two
[L1609] [57:30.56] different engineering approaches. Uh and
[L1610] [57:33.12] so what I try to do is encourage people
[L1611] [57:36.64] to put that analysis back in, understand
[L1612] [57:39.28] the performance trade-offs you're
[L1613] [57:40.48] making, understand how much it might
[L1614] [57:42.80] cost in the future to like make these
[L1615] [57:45.04] fixes. And I I don't really do any AI
[L1616] [57:48.88] stuff, but my sort of feeling is more so
[L1617] [57:52.40] now than ever, I feel like that's got to
[L1618] [57:54.08] be pretty important because you're
[L1619] [57:55.44] instructing these AIs to do what they're
[L1620] [57:57.92] going to do. And I feel like it would be
[L1621] [58:01.36] a bad idea to not know about performance
[L1622] [58:04.48] trade-offs because especially if an AI
[L1623] [58:07.20] is going to be doing your bidding and
[L1624] [58:09.36] structuring the code the way you want to
[L1625] [58:10.80] structure it or doing whatever. It seems
[L1626] [58:12.88] like a very straightforward part of the
[L1627] [58:14.08] process to include performance stuff in
[L1628] [58:16.88] those instructions, right? Like that
[L1629] [58:18.40] would be a natural thing that we would
[L1630] [58:19.68] want to understand and do, right? So I
[L1631] [58:21.92] feel like
[L1632] [58:23.76] really I've been just trying to get that
[L1633] [58:25.04] more into the conversation. Uh, and I
[L1634] [58:27.92] feel like it's it's as relevant now as
[L1635] [58:29.84] it ever was, and arguably maybe more so.
[L1636] [58:31.68] I don't know, but I could be wrong about
[L1637] [58:32.96] that.
[L1638] [58:34.00] >> What are some things that are in your
[L1639] [58:36.24] mind, they're those high value
[L1640] [58:39.20] performance things to consider that
[L1641] [58:41.04] don't cost a whole lot to think about?
[L1642] [58:43.68] >> So, to me, awareness is the number one
[L1643] [58:46.80] thing, right? Understanding roughly the
[L1644] [58:49.44] performance characteristics of the
[L1645] [58:51.44] hardware that you're working on. Uh,
[L1646] [58:53.12] which includes things like, you know, if
[L1647] [58:54.48] there's a network, like what does that
[L1648] [58:55.76] look like? and so on. Um, it's really
[L1649] [58:59.28] about awareness more than anything else
[L1650] [59:01.84] because a little bit of awareness can go
[L1651] [59:05.84] a very long way. If you understand the
[L1652] [59:08.96] basic concept that like you know a that
[L1653] [59:12.32] network latency versus network
[L1654] [59:14.16] throughput are different things, you can
[L1655] [59:16.40] make upfront decisions about structuring
[L1656] [59:18.48] code such that you batch things properly
[L1657] [59:21.28] uh and so on and so forth. If you don't
[L1658] [59:23.12] understand those things, you could get
[L1659] [59:24.40] very far down a project only to realize
[L1660] [59:27.20] that everything you designed and all the
[L1661] [59:29.36] way it works is all very serial and
[L1662] [59:31.44] really just cannot be accelerated over a
[L1663] [59:33.28] network at all. Like it's never going to
[L1664] [59:34.80] run uh reasonably or something like
[L1665] [59:36.56] this, right? Uh and so I think the the
[L1666] [59:40.56] lowest hanging fruit is just to get some
[L1667] [59:42.96] education in performance. like get some
[L1668] [59:45.28] education in how to think about the way
[L1669] [59:49.36] a machine works and what makes it fast
[L1670] [59:51.60] or slow, what it struggles with and what
[L1671] [59:53.36] it doesn't and just to keep that in the
[L1672] [59:55.68] back of your head because at the end of
[L1673] [59:58.00] the day, if you have that knowledge, I
[L1674] [01:00:00.24] think you're very unlikely to make the
[L1675] [01:00:02.32] kinds of architectural decisions that
[L1676] [01:00:04.72] will be hard to undo later, right?
[L1677] [01:00:08.00] Um, and so that's really that's really
[L1678] [01:00:10.56] the majority of it I think and that is
[L1679] [01:00:13.12] by far the highest impact lowest cost
[L1680] [01:00:16.40] thing you can do is just do that
[L1681] [01:00:17.52] training once because once you have it
[L1682] [01:00:19.12] it's with you forever once you
[L1683] [01:00:20.88] understand how to think about
[L1684] [01:00:22.48] performance it can always be there and
[L1685] [01:00:26.24] at any time you can sort of have that
[L1686] [01:00:28.24] alarm bell of like this I don't see you
[L1687] [01:00:32.16] know you're always kind of looking like
[L1688] [01:00:33.44] I don't see the path towards this
[L1689] [01:00:35.28] running well and then So that's that
[L1690] [01:00:37.68] your key to stop and go like uh maybe we
[L1691] [01:00:39.68] need to rethink like how we were making
[L1692] [01:00:41.20] some of these decisions. As long as you
[L1693] [01:00:43.68] can see that path, you're pretty you can
[L1694] [01:00:46.00] you can delay most like optimization
[L1695] [01:00:49.20] work. As long as you can see the path
[L1696] [01:00:51.44] like here is how we will optimize this.
[L1697] [01:00:54.16] You're in pretty good shape because um
[L1698] [01:00:57.28] if you're making those trade-offs
[L1699] [01:00:58.72] correctly, you're not going to paint
[L1700] [01:01:00.80] yourself into a corner where there's
[L1701] [01:01:02.32] nothing that you can do other than scrap
[L1702] [01:01:04.32] and rewrite. Right. you had this one
[L1703] [01:01:06.72] video title. It said, you know, where
[L1704] [01:01:09.12] does bad code come from? And so, yeah,
[L1705] [01:01:11.32] [laughter] you know, I guess, yeah, my
[L1706] [01:01:12.56] question to you is, you know, what's the
[L1707] [01:01:14.00] answer to that? Where where does bad
[L1708] [01:01:15.68] code come from?
[L1709] [01:01:18.24] Yeah, that's a good question. Um, my
[L1710] [01:01:20.32] feeling on where bad code comes from is
[L1711] [01:01:23.12] that for everything that I've seen on
[L1712] [01:01:26.24] projects in the past, the bad code all
[L1713] [01:01:29.04] seems to come from roughly the same
[L1714] [01:01:31.52] source. And that is not dealing with the
[L1715] [01:01:36.64] actual thing that's happening, right? Um
[L1716] [01:01:41.44] there's a lot of ideas in computer
[L1717] [01:01:44.08] science about sort of doing upfront
[L1718] [01:01:47.52] design and making a lot of decisions
[L1719] [01:01:49.52] without ever really implementing
[L1720] [01:01:52.08] anything, right?
[L1721] [01:01:54.48] And I have found that universally that
[L1722] [01:01:57.76] leads to the worst kind of code. And the
[L1723] [01:02:00.56] reason for that is, you know, uh I hate
[L1724] [01:02:04.40] to be pessimistic and I hate to be
[L1725] [01:02:06.72] pessimistic about my own ability, but
[L1726] [01:02:08.88] I'll just say for me personally,
[L1727] [01:02:11.44] I am not able to correctly hold all of
[L1728] [01:02:16.40] the details for most complex software in
[L1729] [01:02:19.44] my head at once. There's just a lot of
[L1730] [01:02:22.16] stuff going on at like when when the
[L1731] [01:02:26.00] actual, you know, instructions hit the
[L1732] [01:02:28.32] CPU. There's a lot going on down there
[L1733] [01:02:31.52] that's very hard to keep all in your
[L1734] [01:02:33.52] head. And so when you approach an
[L1735] [01:02:35.76] upfront design, typically unless the
[L1736] [01:02:38.08] problem is very is like stupidly simple,
[L1737] [01:02:40.56] right?
[L1738] [01:02:42.64] When you approach something with upfront
[L1739] [01:02:44.08] design and you think you're going to get
[L1740] [01:02:45.92] all of this architecture worked out
[L1741] [01:02:47.84] ahead of time, you forget some important
[L1742] [01:02:51.28] things. You make decisions without
[L1743] [01:02:53.28] realizing, oh wait, there's this thing
[L1744] [01:02:55.60] that has to happen there that means that
[L1745] [01:02:57.84] this isn't really the right way for
[L1746] [01:03:00.24] these pieces of code to interoperate.
[L1747] [01:03:03.04] And so then you, you know, you end up
[L1748] [01:03:05.76] seeing these hilarious APIs or something
[L1749] [01:03:08.08] where it's like you're just like, how
[L1750] [01:03:09.60] did this end up being the way that you
[L1751] [01:03:12.00] do this, right? Like I have to create
[L1752] [01:03:13.52] all these objects and I have to connect
[L1753] [01:03:15.04] them together with these things and I
[L1754] [01:03:16.48] have to create this weird like filter
[L1755] [01:03:18.24] graph thing and then I have to call
[L1756] [01:03:19.28] compile on it. but only like you end up
[L1757] [01:03:21.36] with these like insane things. You're
[L1758] [01:03:22.80] like all I wanted to do was call this
[L1759] [01:03:24.72] one thing that said like low pass filter
[L1760] [01:03:26.48] this buffer. It could have been one
[L1761] [01:03:27.76] function call, right? It's like how did
[L1762] [01:03:29.60] you get there? And the answer is because
[L1763] [01:03:31.20] you weren't actually like dealing with
[L1764] [01:03:33.44] the actual problem and looking at what
[L1765] [01:03:35.04] the actual code looks like uh when you
[L1766] [01:03:37.92] want to actually uh when you actually
[L1767] [01:03:39.92] want to solve the problem in practice.
[L1768] [01:03:42.24] And so my idea of where bad code comes
[L1769] [01:03:44.08] from is usually just it's that it's this
[L1770] [01:03:46.24] failure to engage with the actual
[L1771] [01:03:48.24] reality of the situation.
[L1772] [01:03:50.72] Um
[L1773] [01:03:52.96] maybe there are people out there I
[L1774] [01:03:54.56] certainly have never met any but maybe
[L1775] [01:03:56.32] there are people out there whose brains
[L1776] [01:03:57.84] are so expansive that they can actually
[L1777] [01:03:59.68] hold all that in there and they can
[L1778] [01:04:01.12] therefore just do it upfront. Um, but
[L1779] [01:04:04.32] other than for very sort of constrained
[L1780] [01:04:06.80] problem spaces, I've never seen that
[L1781] [01:04:08.96] work. And and you know there, like I
[L1782] [01:04:11.12] said, there are sometimes when that's
[L1783] [01:04:12.24] the case with the trans like if you're
[L1784] [01:04:13.52] just doing like I'm trying to do this
[L1785] [01:04:15.92] particular mathematical operation, that
[L1786] [01:04:18.08] might be a case where you can work it
[L1787] [01:04:19.04] all out on paper because it's very
[L1788] [01:04:20.32] specific like what it is. It takes these
[L1789] [01:04:22.00] n inputs, produces this output, and I
[L1790] [01:04:23.84] can work right. But when you're talking
[L1791] [01:04:25.36] about architecture like, hey, it's a web
[L1792] [01:04:27.04] browser, right? Some complicated thing.
[L1793] [01:04:29.92] The details are all that matter to me,
[L1794] [01:04:32.96] right? It's like it's where all the
[L1795] [01:04:34.48] complexity lies and if you try to do the
[L1796] [01:04:36.80] design without reckoning with them, it
[L1797] [01:04:39.68] just leads to bad results in my
[L1798] [01:04:40.96] experience. So,
[L1799] [01:04:41.84] >> so how do you avoid writing bad code in
[L1800] [01:04:44.56] that case?
[L1801] [01:04:45.68] >> I I try to start with the actual
[L1802] [01:04:48.56] solutions to the problems and work up
[L1803] [01:04:50.80] from there. So, um
[L1804] [01:04:54.96] one way to say it would be instead of
[L1805] [01:04:56.24] top down programming, bottom up
[L1806] [01:04:57.60] programming, right? Uh as much as
[L1807] [01:04:59.12] possible. And top down programming isn't
[L1808] [01:05:00.48] really the same as designing up front,
[L1809] [01:05:01.76] but you know, I'm just saying like as a
[L1810] [01:05:03.92] contrast there, try to start with the
[L1811] [01:05:06.72] things that you know you need. Like it's
[L1812] [01:05:08.08] like, okay, if I'm if I'm building this
[L1813] [01:05:09.44] thing, it's got to have a rasterizer.
[L1814] [01:05:10.80] All right, I'm going to start making a
[L1815] [01:05:11.76] rasterizer. I'm going to see what kinds
[L1816] [01:05:13.12] of stuff that does and how I would like
[L1817] [01:05:15.28] what's the most uh straightforward way
[L1818] [01:05:17.36] to call this and use it. Okay, let's
[L1819] [01:05:19.36] make an API out of that, right?
[L1820] [01:05:21.44] build it out of steps where the
[L1821] [01:05:23.68] abstraction comes from actual working
[L1822] [01:05:27.04] code that gets abstracted rather than
[L1823] [01:05:29.76] pushing the abstraction down from the
[L1824] [01:05:31.60] top where I say this is how I will
[L1825] [01:05:34.48] abstract the rasterizer and now I go
[L1826] [01:05:37.68] write the rasterizer in the thing that
[L1827] [01:05:39.36] uses the rasterizer only to find that
[L1828] [01:05:41.60] that is not a very good way to use a
[L1829] [01:05:43.28] rasterizer right like so to me starting
[L1830] [01:05:46.40] with that and working upwards is the
[L1831] [01:05:48.96] best way to ensure that you will get an
[L1832] [01:05:50.96] architecture uh that is at least good
[L1833] [01:05:53.60] for one thing. Now, if you want it to be
[L1834] [01:05:55.52] good for multiple things, you probably
[L1835] [01:05:57.44] need a couple different like I want a
[L1836] [01:05:59.52] few different varied things that would
[L1837] [01:06:01.36] use this rasterizer that I will kind of
[L1838] [01:06:02.96] work on together and I'll make
[L1839] [01:06:04.48] abstraction decisions that work across
[L1840] [01:06:06.32] all three of them. That's a good way to
[L1841] [01:06:08.16] make a more reusable API that works for,
[L1842] [01:06:10.64] you know, a lot of things. But I never
[L1843] [01:06:12.88] want to just sit down and say, "How will
[L1844] [01:06:15.44] I design an API for lots of people to
[L1845] [01:06:17.68] use a rasterizer without actually
[L1846] [01:06:19.76] writing any of it?" It's like, "No, no,
[L1847] [01:06:21.28] no." Like, and I definitely can't do it.
[L1848] [01:06:23.44] And I I question I I would question
[L1849] [01:06:25.76] someone who says that they can, unless
[L1850] [01:06:28.16] one caveat, they've written a lot of
[L1851] [01:06:29.76] them before, right? If you've written
[L1852] [01:06:30.88] tons before, then you've sort of done
[L1853] [01:06:32.32] the thing that I'm talking about already
[L1854] [01:06:33.68] and you might remember, oh, it's this
[L1855] [01:06:35.44] way, right?
[L1856] [01:06:37.36] I think there's a lot of common advice,
[L1857] [01:06:40.08] especially at these these larger
[L1858] [01:06:41.68] companies where there's this processes
[L1859] [01:06:45.12] to, you know, write a design doc and
[L1860] [01:06:48.56] kind of uh, you know, put together
[L1861] [01:06:50.40] everything in advance, present it before
[L1862] [01:06:53.12] you write any code. And sounds like
[L1863] [01:06:56.00] you're saying that that's a terrible
[L1864] [01:06:57.44] idea.
[L1865] [01:06:57.92] >> I think that's an absolutely terrible
[L1866] [01:06:59.36] idea. Now, that doesn't mean that I
[L1867] [01:07:01.76] wouldn't be okay with that process with
[L1868] [01:07:03.20] like a slight modification, right? If
[L1869] [01:07:05.52] what you're doing during that time is
[L1870] [01:07:07.20] writing test code in the way that I'm
[L1871] [01:07:09.36] saying, so we're going to write a little
[L1872] [01:07:10.88] experimental rasterizer. We're going to
[L1873] [01:07:12.32] do those things. We're going to start
[L1874] [01:07:13.04] and then our document that we're
[L1875] [01:07:14.56] producing is here is what we have
[L1876] [01:07:17.04] determined is a good API based on these
[L1877] [01:07:19.36] experiments. I have no problem with
[L1878] [01:07:21.52] that. That's really that's following my
[L1879] [01:07:24.24] procedure pretty much to a tea. And you
[L1880] [01:07:27.36] know, I don't tend to produce
[L1881] [01:07:28.72] documentation because I work you know in
[L1882] [01:07:30.72] on smaller teams. I don't have to have a
[L1883] [01:07:34.72] thousand person org know exactly what it
[L1884] [01:07:36.80] what I'm doing there or whatever.
[L1885] [01:07:39.76] So I wouldn't produce upfront
[L1886] [01:07:40.88] documentation normally in a in a case
[L1887] [01:07:42.40] like that. But if you if you wanted to
[L1888] [01:07:44.32] that seems totally reasonable, right?
[L1889] [01:07:45.68] And that like is communicating our
[L1890] [01:07:47.76] research into how this should be
[L1891] [01:07:49.76] structured uh out to a wider audience.
[L1892] [01:07:52.40] But we still did the due diligence of
[L1893] [01:07:53.92] determining that it really does work in
[L1894] [01:07:55.44] practice. It's not just our guess about
[L1895] [01:07:57.76] what it will be.
[L1896] [01:07:59.20] >> I see. Okay. So you're saying kind of
[L1897] [01:08:01.04] this u pair design, pair prototype kind
[L1898] [01:08:04.64] of, you know, like you just build as you
[L1899] [01:08:06.48] go, but it's just so you get a sense of
[L1900] [01:08:08.48] the reality of the design.
[L1901] [01:08:10.64] >> Yeah. And I think I would be very
[L1902] [01:08:11.92] comfortable with the team that wanted to
[L1903] [01:08:13.04] work that way if they're like, look, we
[L1904] [01:08:14.24] want to produce, we want to document
[L1905] [01:08:15.84] this thing before we start developing
[L1906] [01:08:17.36] it. That's just how we feel more
[L1907] [01:08:19.12] comfortable, you know, with how we're
[L1908] [01:08:20.80] going to do it. Maybe it's a very large
[L1909] [01:08:22.24] org. Maybe we have some very good
[L1910] [01:08:24.08] reasons for that. Um, then I would say
[L1911] [01:08:27.68] totally fine. It's just I want I want to
[L1912] [01:08:30.00] hear you know if I'm going to be
[L1913] [01:08:31.36] comfortable with it I want to hear that
[L1914] [01:08:32.48] that process is not we're just typing on
[L1915] [01:08:34.16] paper. We are actually testing these API
[L1916] [01:08:37.52] uh design decisions and they come from
[L1917] [01:08:39.68] looking at actual usage code that we
[L1918] [01:08:42.48] have made and that we have implemented
[L1919] [01:08:44.48] at least uh experimental versions of so
[L1920] [01:08:47.84] that we know they really do account for
[L1921] [01:08:49.92] all the details that we're likely to
[L1922] [01:08:51.52] encounter in practice. That's what I
[L1923] [01:08:54.48] want to hear, right? I don't want to
[L1924] [01:08:55.68] hear like ah we thought it through. Like
[L1925] [01:08:57.44] I'm like did you did you think it all
[L1926] [01:09:00.08] the way through? Because I've seen a lot
[L1927] [01:09:01.36] of times where people thought they did
[L1928] [01:09:02.56] and they didn't including myself. Like
[L1929] [01:09:04.40] that is not that is not a I always think
[L1930] [01:09:06.08] it all the way through. So it's like no
[L1931] [01:09:07.12] this comes from a personal place of I
[L1932] [01:09:09.28] forgot the thing. Like I forgot this
[L1933] [01:09:10.88] important thing and I made a really
[L1934] [01:09:12.32] stupid design. Right.
[L1935] [01:09:14.32] >> There's another video you had. It was it
[L1936] [01:09:15.92] was titled the only unbreakable law.
[L1937] [01:09:19.20] >> Oh yeah.
[L1938] [01:09:19.76] >> And you know what is the only
[L1939] [01:09:22.00] unbreakable law in software engineering?
[L1940] [01:09:24.08] So yeah, that was that was a a lecture I
[L1941] [01:09:26.88] did um where I was trying to think of
[L1942] [01:09:30.32] like if I was going to say one thing
[L1943] [01:09:32.24] about architecture to people, right? If
[L1944] [01:09:33.92] I was going to say one thing about
[L1945] [01:09:34.88] architecture,
[L1946] [01:09:36.64] what could I say that isn't probably
[L1947] [01:09:39.60] wrong? Because you think about a lot of
[L1948] [01:09:41.52] our ideas about architecture, it's like
[L1949] [01:09:42.96] even the stuff I just said to you, who
[L1950] [01:09:45.04] knows what we're going to be thinking 10
[L1951] [01:09:46.80] years from now. It's like they're not
[L1952] [01:09:48.96] really laws. They're just
[L1953] [01:09:52.16] they're observations that we've had that
[L1954] [01:09:54.16] maybe this is a good way to do things,
[L1955] [01:09:55.84] but it's not really a law. Right? So, uh
[L1956] [01:09:59.36] the only thing I've seen that feels like
[L1957] [01:10:01.36] a real law to me is the thing I cover in
[L1958] [01:10:03.44] this lecture, which is Conway's law. Uh
[L1959] [01:10:06.00] and this is a a it's not a real law in
[L1960] [01:10:10.08] the sense of like the laws of gravity or
[L1961] [01:10:13.04] so like it's not a physics law like a a
[L1962] [01:10:15.20] physicist would laugh at calling it a
[L1963] [01:10:16.80] law. um you know, it's probably not even
[L1964] [01:10:20.08] a theory. It's more like a hypothesis at
[L1965] [01:10:23.12] this point, right? But in terms of
[L1966] [01:10:25.44] things that I would place money on
[L1967] [01:10:30.40] being validated as a law at some point
[L1968] [01:10:32.48] if we ever had the means to do so. This
[L1969] [01:10:35.76] would be one of the only software
[L1970] [01:10:37.44] engineering things that I think uh would
[L1971] [01:10:40.00] qualify and it is
[L1972] [01:10:43.84] that if you would like to organize
[L1973] [01:10:49.60] a series of like a set of people to work
[L1974] [01:10:52.56] on something or in the modern parliament
[L1975] [01:10:54.80] let's say agents. So it could be, it
[L1976] [01:10:56.88] doesn't have to be a human. It's any
[L1977] [01:10:59.52] system that has sort of its own internal
[L1978] [01:11:02.00] processing like a human brain does or
[L1979] [01:11:04.08] like a computer does.
[L1980] [01:11:06.64] If you need to partition a problem into
[L1981] [01:11:10.56] a set of workers in this way
[L1982] [01:11:14.16] where the communication between those
[L1983] [01:11:16.24] workers is slower than their own
[L1984] [01:11:18.40] internal computation ability, which we
[L1985] [01:11:20.80] would all agree is true about humans.
[L1986] [01:11:22.24] It's true about two computers running an
[L1987] [01:11:24.48] AI model as well, right? the amount of
[L1988] [01:11:26.00] time it takes to send information back
[L1989] [01:11:27.28] and forth to them is is significantly
[L1990] [01:11:29.28] slower than what like the GPU can be
[L1991] [01:11:31.12] processing directly on it on its own.
[L1992] [01:11:32.88] Right? In systems that look like that,
[L1993] [01:11:35.12] when you start to tackle a problem, in
[L1994] [01:11:38.16] order to get the benefits of that
[L1995] [01:11:39.52] parallelization,
[L1996] [01:11:41.12] you will have to make decisions about
[L1997] [01:11:42.72] who is working on what. At least some
[L1998] [01:11:44.88] decision. For example, if we're making a
[L1999] [01:11:47.44] car and you and I are the two people are
[L2000] [01:11:49.20] going to make the car, I'm going to
[L2001] [01:11:51.04] design the body of the car. you're gonna
[L2002] [01:11:52.56] design the wheels,
[L2003] [01:11:54.96] right? Just a decision someone could
[L2004] [01:11:56.88] make.
[L2005] [01:11:58.48] Once you've made that decision,
[L2006] [01:12:01.76] you have now locked in the fact that the
[L2007] [01:12:06.16] iteration
[L2008] [01:12:08.16] on the design
[L2009] [01:12:10.16] will be slower across that boundary than
[L2010] [01:12:13.28] it is interior to either of the two
[L2011] [01:12:15.36] parts. So for example, your ability to
[L2012] [01:12:18.56] improve the design of the wheels on
[L2013] [01:12:21.12] their own and my design ability to
[L2014] [01:12:24.00] design the body of the car uh and
[L2015] [01:12:26.00] improve that on its own will be much
[L2016] [01:12:28.16] faster than our ability to design the
[L2017] [01:12:30.00] interface between the wheels and the
[L2018] [01:12:31.44] tire like or or it's not even just the
[L2019] [01:12:33.92] interface. The
[L2020] [01:12:36.72] degree of harmony between the designs.
[L2021] [01:12:38.72] So the degree to which your wheels
[L2022] [01:12:40.48] complement my body design and my body
[L2023] [01:12:42.40] design complements your wheels that they
[L2024] [01:12:44.00] there's that they all are considering
[L2025] [01:12:45.44] the trade-offs together right
[L2026] [01:12:48.64] and Melvin Conway's paper which lays
[L2027] [01:12:50.48] this out uh this is a very early paper
[L2028] [01:12:53.12] it's you know it's in the 60s at least
[L2029] [01:12:56.00] was it in the 50s it's it's way back
[L2030] [01:12:58.64] when that lays this out points out the
[L2031] [01:13:02.16] consequence of this is that products
[L2032] [01:13:06.24] or any and when I say product I mean
[L2033] [01:13:08.00] anything that comes out of one of these
[L2034] [01:13:09.28] design processes or development
[L2035] [01:13:10.56] processes. Products will will have a
[L2036] [01:13:14.88] similar structure to the organization
[L2037] [01:13:16.56] that produced them. You will be able to
[L2038] [01:13:19.52] see in the product evidence of this
[L2039] [01:13:23.20] because the degree to which things are
[L2040] [01:13:26.24] able to harmonize is restricted across
[L2041] [01:13:28.48] that boundary. So when you look at the
[L2042] [01:13:30.40] object, it will have that boundary
[L2043] [01:13:32.64] visible in some way, right? It won't be
[L2044] [01:13:35.36] quite as good at the interface between
[L2045] [01:13:38.48] these two things or in the way that they
[L2046] [01:13:41.04] work together as the things are
[L2047] [01:13:43.52] themselves in inside like to themselves,
[L2048] [01:13:46.56] right?
[L2049] [01:13:48.32] And it gets sort of flattened like one
[L2050] [01:13:50.16] way the the rule is pithly stated is
[L2051] [01:13:52.00] like products look like the org chart,
[L2052] [01:13:54.40] right? But that's not exactly what it
[L2053] [01:13:57.12] says, but that's kind of a downstream
[L2054] [01:13:59.28] consequence. And boy, do you ever see it
[L2055] [01:14:02.88] in the real world. So, you know,
[L2056] [01:14:06.16] >> I've heard that in in the context of
[L2057] [01:14:08.24] these big tech companies, like almost
[L2058] [01:14:10.00] like it's a like a bad thing to quote
[L2059] [01:14:12.72] unquote ship your org chart or
[L2060] [01:14:14.80] basically, you know, the product you put
[L2061] [01:14:17.04] out there is has these uh inorganic
[L2062] [01:14:21.60] >> Yes.
[L2063] [01:14:22.00] >> You know, things. So, it sounds similar
[L2064] [01:14:23.76] to what you're saying.
[L2065] [01:14:25.04] >> Yeah. It's And I think like part of the
[L2066] [01:14:27.36] reason I think it is kind of an
[L2067] [01:14:28.64] unbreakable law is I think it's somewhat
[L2068] [01:14:30.32] unavoidable. uh it's more something that
[L2069] [01:14:32.56] you just have to be aware of and
[L2070] [01:14:34.00] mitigate to the degree that you can like
[L2071] [01:14:36.08] you just have to understand look that
[L2072] [01:14:39.36] lower communication time uh whether it's
[L2073] [01:14:42.96] humans or computers or whoever is doing
[L2074] [01:14:45.20] this work that lower communication time
[L2075] [01:14:49.60] uh or I should say that uh that lower
[L2076] [01:14:51.20] communication bandwidth is what um that
[L2077] [01:14:55.36] just means that we will like where we
[L2078] [01:14:58.24] draw these lines has consequences for
[L2079] [01:15:00.16] what we ship And so we really want to
[L2080] [01:15:03.12] try over time to align those boundary
[L2081] [01:15:06.72] drawings
[L2082] [01:15:08.40] to places where it will have the least
[L2083] [01:15:11.20] bad impact on the result of the product.
[L2084] [01:15:14.56] And you know that's true for org charts.
[L2085] [01:15:16.96] Like I said, I suspect it will also
[L2086] [01:15:18.48] become true for AIs and things like that
[L2087] [01:15:20.80] where it's like you will want to
[L2088] [01:15:22.56] partition these problems in ways that
[L2089] [01:15:24.48] respect that um that line drawing
[L2090] [01:15:27.60] because that will be less good than the
[L2091] [01:15:30.56] thing that can be wholly solved um you
[L2092] [01:15:33.04] know by one one unit whatever that unit
[L2093] [01:15:35.68] is. And so to me uh it's a very helpful
[L2094] [01:15:39.36] construct for thinking about things.
[L2095] [01:15:40.80] It's also a very good explanation for
[L2096] [01:15:42.32] why you see some things somewhere you're
[L2097] [01:15:43.68] like why isn't this just integrated in
[L2098] [01:15:45.44] this? It's like because they were two
[L2099] [01:15:46.80] different teams,
[L2100] [01:15:48.16] >> you know? It's like I'm sorry. Like I'm
[L2101] [01:15:49.44] so like I'm sorry that's just the
[L2102] [01:15:50.96] answer. And you know, it costs a lot
[L2103] [01:15:52.96] more for those two teams to have
[L2104] [01:15:54.16] integrated this. That's not how we work,
[L2105] [01:15:56.88] right?
[L2106] [01:15:57.84] >> I I'd love to hear more about I guess
[L2107] [01:16:00.64] your career and how you got into
[L2108] [01:16:03.12] programming.
[L2109] [01:16:04.32] >> I started programming when I was really
[L2110] [01:16:06.00] little because my father worked at
[L2111] [01:16:07.84] Digital Equipment Corporation, which is
[L2112] [01:16:10.56] actually a very important company in
[L2113] [01:16:13.12] that era. no longer exist, right? This
[L2114] [01:16:15.84] was the they would they would be sort of
[L2115] [01:16:17.76] like almost like a case study in how not
[L2116] [01:16:21.52] adapting to a change in technology uh
[L2117] [01:16:25.84] leads to your demise. They were one of
[L2118] [01:16:28.48] the most important companies in the
[L2119] [01:16:30.24] world for computing. If you ever heard
[L2120] [01:16:31.68] of a PDP11 or a vax in computing
[L2121] [01:16:34.56] history, that's them, right? They made
[L2122] [01:16:36.64] these things that were foundational
[L2123] [01:16:38.32] computers in computing history gone
[L2124] [01:16:40.88] today, right? they were uh part of them
[L2125] [01:16:42.96] got absorbed by Intel, part of them got
[L2126] [01:16:44.56] absorbed by Compact, but they're they
[L2127] [01:16:46.56] don't exist.
[L2128] [01:16:48.32] So he worked for that company
[L2129] [01:16:50.96] and so we always had computers in the
[L2130] [01:16:52.88] home and I learned to program when I was
[L2131] [01:16:54.40] little and that's just sort of always
[L2132] [01:16:56.96] what I wanted to do. I really enjoyed it
[L2133] [01:16:59.36] and so I ended up uh getting an
[L2134] [01:17:02.40] internship at Microsoft when I was
[L2135] [01:17:04.48] pretty young and I met some people
[L2136] [01:17:07.52] there. I came out to I I should say I
[L2137] [01:17:11.36] grew up on the east coast so nowhere
[L2138] [01:17:13.36] near Microsoft. Um I met some people
[L2139] [01:17:15.76] there. I ended up coming out to the west
[L2140] [01:17:17.12] coast really early on. This would be in
[L2141] [01:17:18.88] like 95. Uh so what didn't feel early at
[L2142] [01:17:22.48] the time. It felt late in the computer
[L2143] [01:17:23.92] history but nowadays it's like oh wait
[L2144] [01:17:26.32] 95. Oh my god. Like before before
[L2145] [01:17:28.40] everything was on the web, right? Uh I
[L2146] [01:17:31.04] ended up there was a web though. It was
[L2147] [01:17:32.88] it was nent. Um, I ended up uh coming
[L2148] [01:17:36.88] out and and working sort of in the game
[L2149] [01:17:38.96] industry and that's what I did ever
[L2150] [01:17:41.36] since. And I've mostly always worked on
[L2151] [01:17:44.80] game technology. I'm famously like
[L2152] [01:17:47.76] absolutely terrible at understanding
[L2153] [01:17:49.20] game design. Uh, people who watch my
[L2154] [01:17:51.52] stuff know this about me. Like I'm very
[L2155] [01:17:53.44] very bad at I've tried to make games a
[L2156] [01:17:54.96] couple times and I'm just I just cannot
[L2157] [01:17:56.48] do the design side. I'm awful at it. Uh,
[L2158] [01:17:59.44] but I really enjoy the engine stuff and
[L2159] [01:18:01.28] I've I've uh feel like I I'm o okay at
[L2160] [01:18:04.48] it and I've been able to contribute to
[L2161] [01:18:06.00] projects. Um, so in general, most of the
[L2162] [01:18:09.44] time if you've used code that was
[L2163] [01:18:11.52] written by me, you probably uh used it
[L2164] [01:18:13.68] in the context of like a video game that
[L2165] [01:18:15.60] was using technology that I wrote. And
[L2166] [01:18:17.44] so, you know, an example would be um I
[L2167] [01:18:20.48] worked at Rad Game Tools on a character
[L2168] [01:18:22.16] animation system. Uh, I wrote the entire
[L2169] [01:18:24.48] thing myself that is used well, that's
[L2170] [01:18:26.88] not entirely true. I really think myself
[L2171] [01:18:28.16] except for the texture compressor which
[L2172] [01:18:29.84] uh Jeff Roberts wrote. There was like
[L2173] [01:18:31.20] this texture compressor that you could
[L2174] [01:18:32.56] use um as part of the pipeline for the
[L2175] [01:18:35.12] exporting and stuff like that.
[L2176] [01:18:37.60] And it was a pretty cool project at the
[L2177] [01:18:39.28] time. Um I'm really proud of it. The
[L2178] [01:18:41.60] first version was awful uh as it is
[L2179] [01:18:43.84] because I was pretty new at the time.
[L2180] [01:18:44.88] The second version I thought we did a
[L2181] [01:18:46.00] really nice job. And it was made at a
[L2182] [01:18:48.48] time when people didn't think you could
[L2183] [01:18:50.88] do licensable game technology of that
[L2184] [01:18:53.60] kind because it was too hard to
[L2185] [01:18:55.44] integrate into things like you couldn't
[L2186] [01:18:56.96] get the performance or whatever. And we
[L2187] [01:18:58.64] did a lot of things that I think were
[L2188] [01:18:59.84] pretty innovative at the time and we
[L2189] [01:19:01.60] were able to make something that was
[L2190] [01:19:02.72] very successful. And it's uh I mean we
[L2191] [01:19:05.60] released the first version of that in
[L2192] [01:19:07.36] 99. It's still in use today, largely
[L2193] [01:19:12.00] unchanged from the architecture that I
[L2194] [01:19:14.64] guess was the second version I did in
[L2195] [01:19:15.92] like 2001 or something. Um, there are a
[L2196] [01:19:18.48] few changes to architecture that people
[L2197] [01:19:19.76] have made over the times, but it's
[L2198] [01:19:20.80] largely unchanged. And I mean like I
[L2199] [01:19:23.12] found out recently Balders's Gate 3,
[L2200] [01:19:24.72] which was a big game um from Larian came
[L2201] [01:19:27.60] out. I had no idea. It turns out they
[L2202] [01:19:29.12] still use they use it, right? It's in
[L2203] [01:19:30.64] their engine or whatever. So, I'm very
[L2204] [01:19:32.64] proud of that product because I think it
[L2205] [01:19:34.32] it it was in tons of games and was a
[L2206] [01:19:38.08] very hard problem to solve and I think
[L2207] [01:19:39.28] we solved it pretty well. It's largely
[L2208] [01:19:41.28] irrelevant today. I would say it's still
[L2209] [01:19:43.20] in some people's like engines over time,
[L2210] [01:19:45.04] but like it's not the kind of product
[L2211] [01:19:46.96] you would make today because nowadays
[L2212] [01:19:49.44] engines are monolithic and you license
[L2213] [01:19:51.44] them as a whole typically, right? Like
[L2214] [01:19:53.44] you you wouldn't be getting like a
[L2215] [01:19:56.24] character animation library. it's going
[L2216] [01:19:58.08] to be something that's like built into
[L2217] [01:19:59.68] Unreal Engine or built into Unity,
[L2218] [01:20:01.76] right? So, it's not the kind of product
[L2219] [01:20:03.36] you would probably consider making
[L2220] [01:20:04.56] today. So, that that was mostly um like
[L2221] [01:20:07.20] in terms of things that I've done that
[L2222] [01:20:08.64] people might have actually have
[L2223] [01:20:09.76] experienced or used.
[L2224] [01:20:12.16] Uh like folks at home, if you've played
[L2225] [01:20:14.48] games, you may have played something
[L2226] [01:20:15.84] that I had a hand in at some point, but
[L2227] [01:20:18.64] only the technology, not the design. Uh
[L2228] [01:20:21.12] I also worked uh a little bit on The
[L2229] [01:20:22.96] Witness um which was a game by Jonathan
[L2230] [01:20:25.20] Blow uh and and team uh that I thought
[L2231] [01:20:28.96] was absolutely fantastic and I did some
[L2232] [01:20:30.64] work on uh I did some work on the walk
[L2233] [01:20:32.88] system there that I was I was pretty
[L2234] [01:20:34.24] proud of. I thought it came out pretty
[L2235] [01:20:35.28] well. There's there's some parts of it
[L2236] [01:20:36.56] that are really janky. I I don't think I
[L2237] [01:20:38.32] did a very good job of the actual
[L2238] [01:20:39.68] implementation of it, but the design was
[L2239] [01:20:41.92] pretty good. Let's put it that way.
[L2240] [01:20:44.00] >> Early in your career, so you worked at
[L2241] [01:20:45.36] Microsoft and then and then you went to
[L2242] [01:20:48.24] go
[L2243] [01:20:48.64] >> I I was only ever an intern. I never
[L2244] [01:20:50.40] actually like I mean I guess that's
[L2245] [01:20:51.68] technically working there but I I didn't
[L2246] [01:20:53.20] ever work there as like an employee
[L2247] [01:20:54.80] employee right
[L2248] [01:20:55.76] >> as a someone who's writing code. I mean
[L2249] [01:20:58.72] there's a lot of different paths but
[L2250] [01:21:00.64] there's one one path I imagine is you go
[L2251] [01:21:03.28] and you work at one of these big tech
[L2252] [01:21:05.44] companies and create their tech products
[L2253] [01:21:08.56] I guess and then video gaming seems like
[L2254] [01:21:10.88] another path and I think there's other
[L2255] [01:21:12.56] paths as well of course. Um, what drew
[L2256] [01:21:15.76] you to, you know, going towards video
[L2257] [01:21:18.08] gaming and, you know, not continuing
[L2258] [01:21:21.44] down a Microsoft path or something like
[L2259] [01:21:24.08] that?
[L2260] [01:21:25.84] >> I think that there's a bunch of things I
[L2261] [01:21:29.04] could say about that, but they're
[L2262] [01:21:30.56] probably all BS.
[L2263] [01:21:33.04] The truth is probably that I'm probably
[L2264] [01:21:37.28] more uh affected by the people around me
[L2265] [01:21:41.20] than I would like to admit. I mean, I
[L2266] [01:21:43.76] guess I don't have a problem aditting it
[L2267] [01:21:44.80] now, but I mean, at the time, I probably
[L2268] [01:21:46.56] wouldn't have have said that, right? I
[L2269] [01:21:49.28] could envision a alternate past where I
[L2270] [01:21:52.08] did stay at Microsoft and, you know, try
[L2271] [01:21:54.48] to get a job there and work there
[L2272] [01:21:55.68] instead of being just an intern and then
[L2273] [01:21:57.36] going off and working at a different
[L2274] [01:21:58.64] place.
[L2275] [01:22:00.16] The reason that didn't happen was
[L2276] [01:22:02.16] because of the people who I worked with
[L2277] [01:22:05.68] there when I was an intern. I
[L2278] [01:22:08.64] fundamentally really like like nowadays
[L2279] [01:22:11.44] I fundamentally really love doing things
[L2280] [01:22:14.32] like you know analyzing assembly code or
[L2281] [01:22:18.24] looking at exactly how a micro
[L2282] [01:22:19.76] architecture is working and these sorts
[L2283] [01:22:21.36] of things. If I had gone to Microsoft
[L2284] [01:22:24.40] and had just happened to be under some
[L2285] [01:22:28.00] people who were doing that kind of work
[L2286] [01:22:29.60] and had like taught me how to write like
[L2287] [01:22:31.28] device drivers in assembly language or
[L2288] [01:22:33.12] something like that, I I might still be
[L2289] [01:22:34.72] there today. Right? That's not what
[L2290] [01:22:37.36] happened. The capsule summary is the
[L2291] [01:22:40.00] group that I was supposed to be in. The
[L2292] [01:22:42.00] way that they did internships at that
[L2293] [01:22:43.52] time was that a set of interns, say uh
[L2294] [01:22:47.04] three or four of them would be uh
[L2295] [01:22:50.24] underneath a particular manager who was
[L2296] [01:22:52.48] going to like be managing those interns.
[L2297] [01:22:54.88] So there were a couple of us who were
[L2298] [01:22:57.52] supposed to be reporting to to this guy
[L2299] [01:22:59.52] whose name I won't mention just in case
[L2300] [01:23:01.60] for some reason. It's ancient. He
[L2301] [01:23:03.20] probably wouldn't care at this point,
[L2302] [01:23:04.16] but we're supposed to be reporting to
[L2303] [01:23:05.36] this particular person
[L2304] [01:23:07.52] and literally the week before we arrive,
[L2305] [01:23:11.68] he has this massive flame out with upper
[L2306] [01:23:15.04] management,
[L2307] [01:23:16.64] leaves like just walks out of the
[L2308] [01:23:20.48] building and has not been heard from
[L2309] [01:23:23.36] since.
[L2310] [01:23:25.68] So we show up and it's me um there was
[L2311] [01:23:29.68] like uh me this a guy named Rudy a guy
[L2312] [01:23:33.04] named Rajie uh and we're just interns
[L2313] [01:23:36.48] show up we're like hey how's it going
[L2314] [01:23:39.20] and we we report to this test guy this
[L2315] [01:23:42.80] an SD uh guy named um Scott Leam really
[L2316] [01:23:46.32] nice guy
[L2317] [01:23:48.32] and we're like we're supposed to be like
[L2318] [01:23:49.76] reporting to like a like a program like
[L2319] [01:23:51.36] a you know a software or like what's
[L2320] [01:23:53.76] going on like this one of the guys in
[L2321] [01:23:55.36] the test or he's like, "Yeah, that that
[L2322] [01:23:57.66] [laughter] guy's gone, right?" Like,
[L2323] [01:24:00.64] he's out of here, right? Uh and and me
[L2324] [01:24:03.36] and this other guy, Bruce Johnson, are
[L2325] [01:24:04.96] going to like take care of the interns
[L2326] [01:24:07.52] because
[L2327] [01:24:09.92] right, we don't really know what you're
[L2328] [01:24:12.08] going to do. Uh the first thing I think
[L2329] [01:24:14.40] Bruce Bruce had me do was like an ANI
[L2330] [01:24:16.96] cursor loader. There was there's this
[L2331] [01:24:18.32] format I don't know uh ancient history
[L2332] [01:24:20.40] now, but there's this format for
[L2333] [01:24:21.60] animated cursors on Windows. If you ever
[L2334] [01:24:23.52] see the stupid little walking dinosaur
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
