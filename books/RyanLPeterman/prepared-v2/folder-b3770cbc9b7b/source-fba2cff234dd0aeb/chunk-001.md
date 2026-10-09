Chunk 1; segments 1–426. 

# Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy

Source ID: source-fba2cff234dd0aeb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_OCaml_Functional_Programming,_Formal_Verification,_Programming_Languages_Xavier_Leroy_en.txt
Video: https://www.youtube.com/watch?v=9Cswiqrq6So

[L10] [00:00.00] Testing can only show the presence of
[L11] [00:01.92] bugs, but not their complete absence.
[L12] [00:04.40] >> This is the creator of the OCaml
[L13] [00:06.44] programming language, and I asked him
[L14] [00:08.12] all about programming language design
[L15] [00:09.96] and formal verification.
[L16] [00:11.36] >> Oh my god.
[L17] [00:12.45] >> [laughter]
[L18] [00:12.56] >> Uh
[L19] [00:13.32] yeah, I'm not a big fan of JavaScript.
[L20] [00:15.32] And Rust is the finest language for
[L21] [00:18.20] manual memory management. Manual memory
[L22] [00:20.64] management is not always faster.
[L23] [00:22.92] Maybe this will be the the decade of
[L24] [00:25.36] formal verification of software.
[L25] [00:27.56] >> If you took LLM-generated code and
[L26] [00:30.56] turned it up, what languages would
[L27] [00:32.12] become more popular? What languages
[L28] [00:34.16] might fade away?
[L29] [00:35.36] >> Woof.
[L30] [00:36.72] Uh
[L31] [00:37.88] >> Here's the full episode.
[L32] [00:43.60] What sets OCaml apart from other
[L33] [00:45.84] programming languages?
[L34] [00:47.52] >> It it is a fine functional language.
[L35] [00:50.00] Okay, you can
[L36] [00:51.56] like functions by case over inductive
[L37] [00:54.64] types and recursion and combine them
[L38] [00:57.28] with combinators and then higher-order
[L39] [00:59.80] functions and everything. So so it's
[L40] [01:01.60] really a a a fine functional language,
[L41] [01:04.60] but it's also a fairly decent systems
[L42] [01:07.20] programming language.
[L43] [01:08.84] And
[L44] [01:10.16] um
[L45] [01:11.04] so it has fully imperative power. It has
[L46] [01:13.48] lots of
[L47] [01:14.76] interesting control structures, um
[L48] [01:17.60] exceptions, threads,
[L49] [01:20.60] handlers for user-defined effects, which
[L50] [01:22.96] we added recently.
[L51] [01:24.68] Um and it has a very predictable cost
[L52] [01:28.96] model execution model. So so when you
[L53] [01:31.48] write your code, you have a pretty good
[L54] [01:32.84] idea what what will take time and what
[L55] [01:36.12] will be fast and what will be slow. And
[L56] [01:38.08] that that's not the case for all
[L57] [01:39.44] functional languages.
[L58] [01:41.24] Some are pretty unpredictable. And and
[L59] [01:43.92] then the implementation is also pretty
[L60] [01:45.60] performant. Okay, so there's there's a
[L61] [01:47.80] fairly decent compiler, not the best in
[L62] [01:50.20] in its class, but the code is pretty
[L63] [01:52.04] efficient. There's a very good allocator
[L64] [01:54.56] and garbage collector with low latency,
[L65] [01:56.68] so you don't have much pauses.
[L66] [01:59.44] You don't have long long pauses and that
[L67] [02:01.16] that's quite important when you do
[L68] [02:02.48] things like network programming.
[L69] [02:04.68] And and so
[L70] [02:06.72] and so you can write systems
[L71] [02:08.28] applications in
[L72] [02:10.28] in in mostly functional style and and
[L73] [02:13.72] with all the benefits of functional
[L74] [02:15.12] programming.
[L75] [02:16.88] And and so initially
[L76] [02:19.48] OCaml wasn't
[L77] [02:21.04] wasn't designed for those kind of
[L78] [02:22.44] applications, okay? It was more for
[L79] [02:24.60] things like theorem proving
[L80] [02:27.52] or implementing domain-specific
[L81] [02:28.76] languages.
[L82] [02:30.20] And then we got some of the first users
[L83] [02:33.24] who were from the systems community, in
[L84] [02:35.12] particular
[L85] [02:37.64] the Ensemble project in the late '90s at
[L86] [02:40.72] Cornell University. So so it was a
[L87] [02:42.72] network stack for a network protocol
[L88] [02:46.04] stack for
[L89] [02:47.64] reliable multicast and those kind of,
[L90] [02:50.48] you know,
[L91] [02:51.36] collaborative distributed applications
[L92] [02:53.48] like collaborative editing or
[L93] [02:55.24] multiplayer video games.
[L94] [02:57.28] And and their first code was in C, of
[L95] [02:59.56] course.
[L96] [03:00.80] They were systems people, right? And and
[L97] [03:03.28] it worked, but it was unmaintainable and
[L98] [03:05.60] they couldn't extend it anymore. And
[L99] [03:07.36] someone had the idea to try OCaml and
[L100] [03:10.64] and so first the code became a lot nicer
[L101] [03:13.00] and easier to to to evolve and the
[L102] [03:15.64] performance was about as good
[L103] [03:18.12] as the C code. And in particular, they
[L104] [03:20.24] they had this uh
[L105] [03:22.16] brilliant trick of running the garbage
[L106] [03:23.96] collector while
[L107] [03:26.24] packets are in flight, okay? Well,
[L108] [03:28.80] once you've sent a packet, you're you're
[L109] [03:30.68] idle for a few
[L110] [03:32.32] microseconds and so you can run some
[L111] [03:35.36] GC. It costs nothing.
[L112] [03:37.88] And so they were very happy with that
[L113] [03:40.44] and and and then there were some other
[L114] [03:42.60] projects
[L115] [03:44.44] like this using
[L116] [03:46.64] OCaml for systems applications like the
[L117] [03:49.04] Mirage Mirage uh
[L118] [03:52.76] And and and yeah, and and and another
[L119] [03:55.68] benefit or consequence of this uh
[L120] [03:58.72] Ensemble project is that uh one of the
[L121] [04:00.80] PhD students working on that was Yaron
[L122] [04:02.72] Minsky, who then went to Jane Street and
[L123] [04:06.20] and implemented their
[L124] [04:08.52] their trading infrastructure in OCaml.
[L125] [04:11.28] Uh so they are still today one of our
[L126] [04:13.32] big users.
[L127] [04:14.80] >> [snorts]
[L128] [04:14.92] >> And and again, it's well, they do
[L129] [04:16.88] automatic trading, so it must be fast
[L130] [04:18.80] and reliable and
[L131] [04:20.72] and no long pauses, but they also want
[L132] [04:22.88] the elegance of functional programming.
[L133] [04:24.96] And they want non- non-programmers to be
[L134] [04:27.92] able to read and and their code like
[L135] [04:30.36] financial engineers or quantitative
[L136] [04:32.32] analysts.
[L137] [04:33.68] And and so yeah, so OCaml is a fairly
[L138] [04:36.32] good match for those kind of
[L139] [04:37.52] applications.
[L140] [04:39.40] >> I thought it might be interesting to
[L141] [04:41.04] ground some of the conversation here by
[L142] [04:44.36] making comparisons across programming
[L143] [04:46.84] languages, maybe ones that people know
[L144] [04:49.48] more.
[L145] [04:50.56] When you think about Rust versus OCaml,
[L146] [04:53.56] what are the big differences and the
[L147] [04:55.48] pros and cons of the various design
[L148] [04:57.68] decisions in those languages?
[L149] [04:59.68] >> The the big dividing line is between
[L150] [05:02.20] Rust and OCaml is
[L151] [05:04.04] uh well, OCaml has automatic memory
[L152] [05:05.80] management, garbage collection.
[L153] [05:07.96] And Rust is uh is definitely uh a
[L154] [05:11.24] language for manual memory management.
[L155] [05:13.84] Uh it's a it's it's the finest language
[L156] [05:16.16] for that I know for uh manual memory
[L157] [05:18.64] management, okay? It means manages to to
[L158] [05:20.84] make it
[L159] [05:21.96] uh mostly safe
[L160] [05:23.76] uh with with the discipline of uh
[L161] [05:26.40] borrowing, etc. And uh and and tracking
[L162] [05:29.60] ownership and so on. So it's in
[L163] [05:31.84] infinitely uh uh safer than C or C++,
[L164] [05:35.56] but it's still uh a language where you
[L165] [05:38.04] uh allocate and free memory uh yourself.
[L166] [05:42.40] And on the one hand, it gives more
[L167] [05:44.16] control over what the program is doing.
[L168] [05:46.60] On the other hand, it's still a big
[L169] [05:47.92] responsibility. It's significantly
[L170] [05:50.12] harder to write programs when you have
[L171] [05:51.84] to to manage your memory, even with the
[L172] [05:54.08] help of Rust
[L173] [05:56.36] types.
[L174] [05:57.84] So,
[L175] [05:59.12] so yeah, so for me that that's kind of
[L176] [06:01.04] the main
[L177] [06:02.52] dividing line.
[L178] [06:03.96] Otherwise, Rust has
[L179] [06:07.28] Well, Rust has many of the high-level
[L180] [06:10.04] features of functional languages, okay?
[L181] [06:13.92] And in particular in in
[L182] [06:17.44] data structures and ability to do
[L183] [06:19.48] pattern matching and so on. So, it's a
[L184] [06:22.28] very interesting design because they
[L185] [06:24.00] really managed to
[L186] [06:26.52] some kind of fusion between
[L187] [06:29.04] you know, C or C++ style low-level
[L188] [06:31.88] programming
[L189] [06:33.04] and and some of the high-level
[L190] [06:34.36] facilities of functional programming.
[L191] [06:37.48] But still, that that divide, garbage
[L192] [06:39.20] collection versus manual memory
[L193] [06:41.04] management, remains.
[L194] [06:43.48] >> So, it sounds like this is a performance
[L195] [06:46.60] trade-off where you give more to the
[L196] [06:48.64] programmer in exchange for higher
[L197] [06:50.36] performance.
[L198] [06:52.68] >> That's mostly true. That said,
[L199] [06:56.28] manual memory management is not always
[L200] [06:58.76] faster.
[L201] [07:00.44] Or or or you need to be a very good
[L202] [07:02.52] programmer so that it's always faster.
[L203] [07:05.68] There's been some
[L204] [07:07.32] some some mostly C++ code, for instance,
[L205] [07:10.40] that that does a lot of copying
[L206] [07:12.84] of objects just because you know, you're
[L207] [07:15.28] you're not quite sure you're the only
[L208] [07:16.76] owner. So, so you make a copy and now
[L209] [07:19.00] you're the only owner. But the copying
[L210] [07:21.84] is is quite costly in time and in and in
[L211] [07:24.28] memory
[L212] [07:26.08] bloat.
[L213] [07:27.24] So, and and for those kind of
[L214] [07:29.32] applications, a garbage collected
[L215] [07:30.88] language is better.
[L216] [07:32.56] And likewise with with
[L217] [07:34.80] GC, you can work with shared sharing in
[L218] [07:38.20] data structures, okay? And it's
[L219] [07:40.44] perfectly safe.
[L220] [07:42.00] Um
[L221] [07:43.36] uh while um
[L222] [07:45.00] uh
[L223] [07:46.08] sharing is kind of limited with uh
[L224] [07:48.28] Rust's uh
[L225] [07:49.92] ownership discipline. Uh
[L226] [07:52.20] there there are more constraints. And so
[L227] [07:54.16] you may end up unsharing and so using
[L228] [07:56.28] more memory.
[L229] [07:57.68] >> It is surprising to me that um
[L230] [08:01.20] that manual memory management would in
[L231] [08:03.96] many cases be more performant than
[L232] [08:05.92] automatic because for instance in in
[L233] [08:08.32] other patterns in computer science, like
[L234] [08:10.08] let's say letting the compiler optimize
[L235] [08:12.40] things for you instead of optimizing
[L236] [08:14.28] things yourself, I would have thought
[L237] [08:16.44] that, you know, letting some system
[L238] [08:19.24] manage memory for you rather than
[L239] [08:21.48] manually mem- managing it would also be
[L240] [08:24.12] better. So, why is there a difference
[L241] [08:26.16] there?
[L242] [08:27.04] >> Well, because garbage collection takes
[L243] [08:28.60] place at run time. So, so we need from
[L244] [08:31.44] time to time the
[L245] [08:33.36] the program is no longer
[L246] [08:35.92] computing, executing
[L247] [08:37.80] what what you wrote. It is actually uh
[L248] [08:40.32] uh scanning memory,
[L249] [08:42.08] trying to find uh memory that is no
[L250] [08:43.96] longer used. So, [snorts] so uh there's
[L251] [08:47.00] there is uh a run time overhead.
[L252] [08:50.20] And it can be uh depending on
[L253] [08:52.52] applications 10%, 20%,
[L254] [08:55.32] maybe sometimes 30%. Um but again uh
[L255] [08:59.92] that that doesn't mean the whole program
[L256] [09:01.96] is 30% uh
[L257] [09:03.68] slower than if uh you had written it
[L258] [09:05.80] with manual memory management because
[L259] [09:07.60] there may have been uh other costs as
[L260] [09:09.68] you said uh uh of of of manual memory
[L261] [09:12.52] management. But yes, um there's
[L262] [09:16.48] Uh um well, there's been a lot of
[L263] [09:18.48] research on on trying to do um more, I'd
[L264] [09:21.84] say, compile time automatic memory
[L265] [09:23.72] management.
[L266] [09:25.08] And you can do that to some extent, but
[L267] [09:28.00] it it's for for for some some
[L268] [09:30.16] programming styles where it's easy to
[L269] [09:31.68] track the lifetime of of objects and and
[L270] [09:34.92] and data blocks.
[L271] [09:36.36] But in general, you still have quite a
[L272] [09:38.72] bit of work to do at runtime.
[L273] [09:41.12] >> I think a lot of people for garbage
[L274] [09:42.84] collection, they might think of it as a
[L275] [09:44.88] binary thing. It's either you have it or
[L276] [09:47.44] you don't.
[L277] [09:48.72] But I wonder in OCaml, is there some way
[L278] [09:51.84] to
[L279] [09:53.40] like turn down the memory management and
[L280] [09:55.28] do some manual, so kind of like a
[L281] [09:57.04] mixture to have the benefits of both?
[L282] [10:00.92] >> So that's one of the things that the
[L283] [10:02.88] Jane Street people are looking at. So
[L284] [10:04.88] they have their
[L285] [10:06.32] OCaml variant, Oxidized OCaml, which is
[L286] [10:10.36] kind of OCaml with some inspiration from
[L287] [10:12.44] Rust. So it's still very very
[L288] [10:14.40] experimental, but yeah, they've been
[L289] [10:16.40] playing with things like stack
[L290] [10:18.20] allocation of some data structures
[L291] [10:21.00] so that automatically deallocated when
[L292] [10:23.36] the function returns, which is quite
[L293] [10:25.32] cheap. Yeah, there there are a few
[L294] [10:27.08] things you could try, but but I'm not
[L295] [10:29.56] sure they are going to make such a big
[L296] [10:30.92] difference. I remember doing this with a
[L297] [10:33.12] student some experiments with stack
[L298] [10:34.84] allocation of uh
[L299] [10:37.04] of data structures a long time ago, and
[L300] [10:40.32] you don't win as much as you would
[L301] [10:42.24] think. See, garbage collection or
[L302] [10:45.60] heap allocation is pretty cheap for
[L303] [10:47.68] objects that have a very short lifetime.
[L304] [10:49.80] Okay, if if they if they die before the
[L305] [10:52.48] next garbage collector,
[L306] [10:55.04] they they they will cost very little in
[L307] [10:56.88] garbage collection time.
[L308] [10:58.64] Uh but it's more expensive for
[L309] [11:01.08] long-lived data structures, okay,
[L310] [11:03.32] because those will be scanned and uh
[L311] [11:05.40] analyzed uh
[L312] [11:07.20] multiple times.
[L313] [11:08.84] And stack allocation works for the first
[L314] [11:10.84] kind of objects, things that
[L315] [11:13.08] have short lifetime anyway.
[L316] [11:15.04] So so you don't you don't win as much as
[L317] [11:17.52] as as you think.
[L318] [11:20.84] >> Um one of the most popular programming
[L319] [11:23.12] languages JavaScript. Uh curious when
[L320] [11:25.52] you think about the difference between
[L321] [11:26.88] JavaScript and OCaml, what's the main
[L322] [11:29.32] thing that comes to mind?
[L323] [11:31.16] >> Yeah, I'm not a big fan of JavaScript.
[L324] [11:33.08] Well, so JavaScript is uh Well, first
[L325] [11:35.96] it's it's very dynamic. So,
[L326] [11:38.72] type checking is entirely dynamic, but
[L327] [11:40.92] it's more than that. I mean, pretty much
[L328] [11:42.32] everything can be redefined at run time,
[L329] [11:44.80] including, I don't know, the semantics
[L330] [11:46.48] of method invocation, for instance. So,
[L331] [11:48.96] so really some some pretty
[L332] [11:52.24] fundamental aspects of the language
[L333] [11:55.44] are very flexible. So, some people say,
[L334] [11:57.04] "Oh, that's great. We can do lots of
[L335] [11:59.48] meta meta programming, etc." And and to
[L336] [12:03.08] me it it also it it's a big weakness. I
[L337] [12:05.48] mean, it it is pro it makes programs
[L338] [12:07.56] that are that can be very fragile
[L339] [12:10.20] and [snorts]
[L340] [12:11.16] also have some security issues. So, so
[L341] [12:13.72] yeah, so JavaScript is the ultimate
[L342] [12:16.16] dynamic language, in my opinion, while
[L343] [12:18.40] OCaml is very static. Static typing,
[L344] [12:20.56] static binding, pretty much everything
[L345] [12:22.80] is fixed at compile time. Okay.
[L346] [12:25.48] Uh
[L347] [12:26.24] and then
[L348] [12:27.96] Well, I guess it's a kind of a different
[L349] [12:29.80] data data model. Uh JavaScript is a
[L350] [12:32.32] little more object-oriented in in in the
[L351] [12:35.08] way it it presents data. Maybe that's
[L352] [12:37.60] not that important. And and to say one
[L353] [12:40.60] good thing about JavaScript is that it
[L354] [12:42.68] also contains a decent functional
[L355] [12:45.12] language
[L356] [12:46.28] inside. You know, there's there's a
[L357] [12:47.72] little bit of a little core of
[L358] [12:49.28] JavaScript which is basically Lisp
[L359] [12:51.76] and and can be used to do a functional
[L360] [12:54.12] programming if you want.
[L361] [12:56.04] Um and and actually the the designer
[L362] [12:59.84] of JavaScript, I think, was a former
[L363] [13:02.00] Lisp person. I can't remember his name,
[L364] [13:04.44] but
[L365] [13:05.36] >> Brendan Eich, maybe?
[L366] [13:06.72] >> Uh yeah, Brendan Eich, yeah.
[L367] [13:08.96] There there was a little bit of heritage
[L368] [13:10.40] from from Lisp to to JavaScript.
[L369] [13:14.48] But a very dynamic kind of Lisp.
[L370] [13:17.32] >> You said you weren't the biggest fan. Is
[L371] [13:19.16] that just because of the dynamics or is
[L372] [13:21.16] there some other aspect?
[L373] [13:22.72] >> Yeah, mostly the dynamics. I think
[L374] [13:26.32] They really went overboard with that.
[L375] [13:28.64] This kind of meta meta object protocol
[L376] [13:31.32] where you can really find the semantics
[L377] [13:33.40] of
[L378] [13:34.92] very basic operations like method
[L379] [13:36.52] invocation. The fact that a method can
[L380] [13:40.12] There's a lot of introspection. A method
[L381] [13:41.92] can look at its own call stack, look at
[L382] [13:44.24] its callers, look at the code of their
[L383] [13:46.56] of its callers, which is a security
[L384] [13:48.60] nightmare.
[L385] [13:49.92] Um
[L386] [13:50.96] All those things I think are completely
[L387] [13:52.92] unnecessary and not conducive to good
[L388] [13:55.32] programs.
[L389] [13:57.04] Easily abused. Yeah. Easily abused.
[L390] [14:00.16] >> I think on the topic of functional
[L391] [14:02.44] languages compared to imperative
[L392] [14:04.40] languages, there's this thought that uh
[L393] [14:07.40] functional languages are kind of hard
[L394] [14:09.40] harder to learn or maybe they have more
[L395] [14:11.80] perceived complexity. And actually, I
[L396] [14:15.04] when I my research, there's this popular
[L397] [14:17.32] quote from the designer of Go, Rob Pike.
[L398] [14:21.56] And he's talking about what they
[L399] [14:22.96] intended to do with code with Go.
[L400] [14:25.60] And he said, you know, the key point
[L401] [14:27.60] here is the programmers are are
[L402] [14:29.56] Googlers. They're not researchers. You
[L403] [14:31.84] know, they they're young, fresh out of
[L404] [14:33.88] school. They're not capable of
[L405] [14:35.76] understanding a a brilliant language.
[L406] [14:37.92] And I think, you know, that that thought
[L407] [14:40.44] of a brilliant language is often
[L408] [14:42.16] attributed to functional languages.
[L409] [14:44.84] What do you think about is a language
[L410] [14:47.16] like OCaml harder for programmers to
[L411] [14:49.48] grasp than imperative languages?
[L412] [14:51.68] >> I think functional programming is not
[L413] [14:53.76] fundamentally harder, especially if you
[L414] [14:56.00] have a little bit of mathematics
[L415] [14:57.96] background. So, coming back to the quote
[L416] [15:00.00] by
[L417] [15:01.64] by Rob Pike, uh
[L418] [15:04.00] I think it describes very much how they
[L419] [15:06.12] go about hiring at Google. Okay, they
[L420] [15:08.72] they they hire a lot of uh
[L421] [15:11.68] engineers who are fresh out of of
[L422] [15:14.08] college. Some of them have master's
[L423] [15:15.56] degree, but And and then they train them
[L424] [15:17.76] internally. Other other companies I I
[L425] [15:20.32] try to to hire people with more
[L426] [15:22.68] education and perhaps a more diverse
[L427] [15:25.16] backgrounds.
[L428] [15:27.36] Um and and yeah, so so Jane Street for
[L429] [15:30.72] instance and and some of those use OCaml
[L430] [15:33.04] as a filter on on who who they want to
[L431] [15:35.36] hire.
[L432] [15:36.96] Yeah, they have fewer applicants, but in
[L433] [15:39.20] general they have more interesting
[L434] [15:40.92] backgrounds. So
[L435] [15:42.88] um
