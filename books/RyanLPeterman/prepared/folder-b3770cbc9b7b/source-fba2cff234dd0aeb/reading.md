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
[L436] [15:44.64] And perhaps one last thing I would like
[L437] [15:46.24] to say, Python is 50% functional
[L438] [15:48.80] language.
[L439] [15:49.88] Okay. Uh
[L440] [15:51.04] a lot of good Python code looks like
[L441] [15:53.32] functional uh code with comprehensions.
[L442] [15:56.32] So I think uh uh
[L443] [15:58.36] people are already halfway uh through
[L444] [16:00.48] through functional programming uh when
[L445] [16:02.64] when when they are comfortable with
[L446] [16:04.12] Python.
[L447] [16:05.72] >> Yeah, when I was learning OCaml in
[L448] [16:07.88] college, I think one thing that really
[L449] [16:10.48] stood out to me and I thought was
[L450] [16:11.96] interesting was this concept of type
[L451] [16:13.96] inference
[L452] [16:15.12] where the compiler is
[L453] [16:17.08] kind of uh it knows the types of
[L454] [16:19.00] everything implicitly in the the way
[L455] [16:21.80] that the code is written.
[L456] [16:23.36] Um can you explain uh type inference and
[L457] [16:25.92] what the advantages are?
[L458] [16:27.88] >> Well, the the basic idea is that uh you
[L459] [16:30.48] don't have to declare the type of every
[L460] [16:32.96] variable you introduce, every function
[L461] [16:35.20] parameter, every local variable because
[L462] [16:37.96] quite often the type can be deduced from
[L463] [16:39.64] the uses of the variable. Okay? Uh like
[L464] [16:43.40] if you do uh I don't know X equals
[L465] [16:45.68] string length of S, uh then you kind of
[L466] [16:48.80] know that S is a string and X is an
[L467] [16:51.16] integer, right? Because that's what the
[L468] [16:52.96] string length function uh that's the
[L469] [16:55.20] type of string length and it it tells
[L470] [16:57.16] you that.
[L471] [16:59.56] Um so so that's the basic idea. Uh
[L472] [17:03.20] now the the actual realization is a
[L473] [17:05.92] little more complicated. Basically, you
[L474] [17:07.60] need to collect a number of con- the
[L475] [17:09.36] compiler needs to collect a number of
[L476] [17:11.24] constraints and then try to solve them.
[L477] [17:14.24] Uh see uh
[L478] [17:16.16] well, if there's no solution, then it's
[L479] [17:17.84] a type error. But, sometimes there are
[L480] [17:19.88] several solutions and you must find good
[L481] [17:22.68] criteria to choose one, otherwise you're
[L482] [17:25.00] I mean, it also needs to be predictable
[L483] [17:27.04] for for programmers.
[L484] [17:28.88] Um, and often also you can you
[L485] [17:32.24] um you can still put type annotation as
[L486] [17:34.12] a programmer you can still put type
[L487] [17:35.44] annotations if that makes the code
[L488] [17:37.12] clearer.
[L489] [17:38.52] So, I think the the the main advantage
[L490] [17:40.56] is precisely to have less verbose code,
[L491] [17:43.28] less verbose code. Well, you don't
[L492] [17:46.68] you don't need to put types everywhere,
[L493] [17:49.08] but only where they help uh
[L494] [17:51.08] documentation and and documenting the
[L495] [17:53.96] code and and making the making it easier
[L496] [17:57.36] to read. Okay.
[L497] [17:59.32] Uh, but quite often you
[L498] [18:02.20] um for for like small local functions,
[L499] [18:05.04] for uh short-lived temporary variables,
[L500] [18:07.76] you you
[L501] [18:09.32] the type is obvious from the context, so
[L502] [18:11.40] let's just omit it.
[L503] [18:13.08] >> If I'm trying to figure out how this
[L504] [18:14.32] type inference works, the intuitive
[L505] [18:16.32] example you said makes sense. But, uh
[L506] [18:18.84] you mentioned it seems to be some sort
[L507] [18:20.28] of system of equations that you solve or
[L508] [18:23.04] something like that. Can you give a uh
[L509] [18:25.32] concrete example maybe, you know, what
[L510] [18:27.36] does that look like to the compiler?
[L511] [18:29.32] >> Okay. Well, for a slightly more complex
[L512] [18:31.48] example, say you have um
[L513] [18:34.32] function with two parameters X and Y,
[L514] [18:36.24] and then you do if X equals Y.
[L515] [18:40.16] So, that tells you that X and Y have the
[L516] [18:41.88] same type, but that still doesn't tell
[L517] [18:43.72] you which type it is, uh assuming a
[L518] [18:46.00] polymorphic uh equality comparison.
[L519] [18:49.76] So, you've learned something about X and
[L520] [18:51.28] Y, that they have the same type, but you
[L521] [18:53.12] still don't know what the type is.
[L522] [18:55.20] And later maybe you will learn something
[L523] [18:56.80] about the type of X.
[L524] [18:58.80] And now you will have determined the
[L525] [19:00.64] type of Y as well.
[L526] [19:02.60] So, so that's the kind of constraints
[L527] [19:04.52] you you you accumulate and solve, um
[L528] [19:07.40] little bit like, you know, Sudoku or uh
[L529] [19:10.56] those kind of puzzles. And then there's
[L530] [19:12.56] the interesting case where you don't
[L531] [19:14.64] have enough constraints to find
[L532] [19:17.04] a unique type.
[L533] [19:18.72] So maybe in the end X and Y will be you
[L534] [19:21.88] know they have the same type but it's
[L535] [19:23.04] still unconstrained.
[L536] [19:24.60] And and then that's where you
[L537] [19:26.68] automatically get polymorphism for free.
[L538] [19:29.28] Okay, the type checker said, "Okay,
[L539] [19:31.00] those types are unconstrained so it can
[L540] [19:33.20] work for any type."
[L541] [19:35.44] So my function can take an X of any type
[L542] [19:37.84] and a Y of the same type. Again, any
[L543] [19:40.68] type and it's a polymorphic function.
[L544] [19:43.36] So there's there's this beautiful I
[L545] [19:45.84] think
[L546] [19:47.48] phenomena phenomenon that that
[L547] [19:50.04] polymorphism can be discovered
[L548] [19:52.92] just by running type inference and
[L549] [19:54.80] noticing that oh there are no
[L550] [19:56.32] constraints so it must be polymorphic.
[L551] [19:59.68] And and that was a great insight by
[L552] [20:01.96] Robin Milner, the British computer
[L553] [20:03.72] scientist pioneer who invented this ML
[L554] [20:05.76] family of languages and and and this
[L555] [20:08.68] kind of type inference in the 70s.
[L556] [20:11.00] Polymorphism
[L557] [20:12.68] was was
[L558] [20:14.56] was not very well understood at the time
[L559] [20:16.64] and so the fact that that he could have
[L560] [20:19.52] he could introduce polymorphism so
[L561] [20:21.64] easily in his language just as a
[L562] [20:23.68] consequence of type inference
[L563] [20:26.08] was a beautiful discovery.
[L564] [20:28.56] >> So for type inference it seems like the
[L565] [20:30.88] benefit is
[L566] [20:33.40] you know the code is going to be a lot
[L567] [20:34.96] more concise because we don't need to
[L568] [20:37.52] write out all the types which seems
[L569] [20:39.04] nice. But what are the tradeoffs of
[L570] [20:41.56] adding type inference to a programming
[L571] [20:43.12] language?
[L572] [20:43.96] >> Well, as I said error messages can be
[L573] [20:46.80] type error messages can be very
[L574] [20:48.56] confusing
[L575] [20:49.96] because
[L576] [20:51.64] they not always point to the actual
[L577] [20:54.08] source of the type error.
[L578] [20:55.84] Okay.
[L579] [20:58.96] The system may have done some some wrong
[L580] [21:00.92] inferences and and and will report
[L581] [21:03.92] though some of those inferences instead
[L582] [21:05.84] of reporting the source the actual
[L583] [21:07.88] source of the type error. So, it's been
[L584] [21:09.84] it's been
[L585] [21:11.04] the subject of much research.
[L586] [21:13.16] And and there's there's no very
[L587] [21:16.24] well-defined idea of the the source of a
[L588] [21:18.60] type error, basically.
[L589] [21:20.72] Um so, yeah. So, errors can be an issue.
[L590] [21:24.08] Some features of type systems
[L591] [21:26.32] are easy to combine with type inference,
[L592] [21:28.20] to handle with type inference, and some
[L593] [21:29.76] are harder.
[L594] [21:31.56] Uh for instance, when it comes to
[L595] [21:32.68] genericity, so I mentioned the
[L596] [21:35.04] polymorphic parameter uh parametric
[L597] [21:36.96] polymorphism, which which is very well
[L598] [21:38.60] handled, but subtyping, the kind of
[L599] [21:42.36] uh
[L600] [21:42.92] thing you have in object-oriented
[L601] [21:44.36] languages, is actually harder to to
[L602] [21:46.76] combine with with type inference for
[L603] [21:50.48] super technical reasons that I'm not
[L604] [21:52.04] going to to go into.
[L605] [21:53.92] Um so, so sometimes uh you have to make
[L606] [21:57.00] a choice. Either you have type
[L607] [21:58.40] inference, but it is less powerful,
[L608] [22:02.00] uh or you you have uh full type
[L609] [22:05.28] inference, but more restrictive type
[L610] [22:07.24] system.
[L611] [22:08.28] Uh
[L612] [22:09.24] And and that that that that choice is
[L613] [22:11.36] part of the language design, actually.
[L614] [22:14.32] >> You mentioning this uh solver kind of
[L615] [22:17.00] reminds me of the topic of formal
[L616] [22:19.16] verification. Could you explain what
[L617] [22:21.20] formal verification is?
[L618] [22:23.32] >> Woo.
[L619] [22:25.68] Well, it's the idea that um
[L620] [22:28.08] um
[L621] [22:29.48] you for for some programs, you want you
[L622] [22:31.84] want strong guarantees that that that
[L623] [22:34.08] the program is correct. Well, and and
[L624] [22:36.08] guarantees that are hard to get just
[L625] [22:37.76] with testing and and reviews, code
[L626] [22:40.48] reviews.
[L627] [22:41.96] Uh you know, there's uh this famous
[L628] [22:43.56] quote by
[L629] [22:44.92] uh Dijkstra, the the Dutch computer
[L630] [22:47.08] pioneer,
[L631] [22:48.52] uh which is which goes something like uh
[L632] [22:51.52] testing can only show the presence of
[L633] [22:53.40] bugs, but not their complete absence.
[L634] [22:56.40] Uh because in general, there's an
[L635] [22:57.80] infinite infinitely many inputs to your
[L636] [23:00.04] program, and you cannot test them all.
[L637] [23:03.08] So, you only test in your sample and
[L638] [23:04.80] then sometimes you have surprises.
[L639] [23:07.08] So, what if you want to make sure that
[L640] [23:09.00] program is correct for an infinite
[L641] [23:10.68] number of inputs?
[L642] [23:12.28] And that's where you need to turn to
[L643] [23:14.60] those so-called formal methods. So,
[L644] [23:16.52] you're using mathematical reasoning,
[L645] [23:18.28] you're using the uh
[L646] [23:20.80] uh
[L647] [23:21.64] static analysis algorithms on your on
[L648] [23:23.68] your program to
[L649] [23:26.08] really analyze all possible executions
[L650] [23:28.76] of a piece of code and making sure that
[L651] [23:32.12] it matches a specification.
[L652] [23:35.12] The specification can be very simple
[L653] [23:36.88] like the code will never crash
[L654] [23:39.84] given well-formed inputs.
[L655] [23:41.96] So, that that's a fairly simple
[L656] [23:44.12] property, but still extremely useful
[L657] [23:46.00] because code that crashes is always code
[L658] [23:48.24] that can be attacked. It's always is
[L659] [23:50.56] often security hole.
[L660] [23:52.50] >> [sighs and gasps]
[L661] [23:52.80] >> Um
[L662] [23:54.32] so, for instance, all accesses within
[L663] [23:56.56] array
[L664] [23:58.12] all array accesses are within bounds.
[L665] [24:01.20] That's a very simple property and it's
[L666] [24:03.92] very hard to to ensure just by a type
[L667] [24:06.88] system or just by testing. So, that's
[L668] [24:09.53] [snorts] where you need some more
[L669] [24:11.04] advanced formal verification.
[L670] [24:12.88] And then there are
[L671] [24:14.16] there are much more powerful specific
[L672] [24:15.76] much more precise specifications that
[L673] [24:17.40] you may want to check that can be where
[L674] [24:19.20] the program always terminates. It can be
[L675] [24:21.04] the program
[L676] [24:22.28] doesn't [snorts] leak
[L677] [24:23.72] confidential data. It can even be where
[L678] [24:26.84] the program computes this mathematical
[L679] [24:29.28] function
[L680] [24:30.49] >> [snorts]
[L681] [24:30.52] >> uh with
[L682] [24:31.72] with an error floating point error under
[L683] [24:35.36] I don't know, 10 to the minus six. Okay.
[L684] [24:38.60] Something like that. Something very
[L685] [24:39.96] precise like that.
[L686] [24:42.72] And so, it's it's been really hot topic
[L687] [24:45.04] in in
[L688] [24:46.24] in in software sciences since the
[L689] [24:49.88] uh since the '70s, I would say. There's
[L690] [24:51.92] lots of techniques.
[L691] [24:53.60] Some are just fully automatic like
[L692] [24:56.64] static analysis, uh
[L693] [24:58.88] but they're already pretty good at
[L694] [25:00.20] finding bugs and making sure that some
[L695] [25:02.48] bugs like array out of bounds are not
[L696] [25:04.68] there.
[L697] [25:06.12] And some
[L698] [25:07.56] are a lot more interactive and and
[L699] [25:09.44] require a lot more formal assistance to
[L700] [25:11.68] write specifications and then do can so
[L701] [25:15.16] called program proofs. So proving
[L702] [25:17.24] mathematical statements about the
[L703] [25:18.72] program.
[L704] [25:19.96] >> I hear about it a lot more now which is
[L705] [25:22.44] lean and these theorem provers.
[L706] [25:24.92] Um what are those in this context and
[L707] [25:28.24] how how are they used?
[L708] [25:30.36] >> Uh so yeah so lean is is an example an
[L709] [25:34.24] instance of the so called
[L710] [25:36.96] provers or proof assistants.
[L711] [25:40.68] Um so originally those were developed to
[L712] [25:43.44] do mathematics on the computer. So not
[L713] [25:46.76] nothing with
[L714] [25:48.56] not formal verification of programs but
[L715] [25:51.16] but they can also be used for formal
[L716] [25:52.64] verification of programs. But the
[L717] [25:54.52] initial motivation was really to do
[L718] [25:56.04] mathematics with the help of the
[L719] [25:57.24] computer.
[L720] [25:59.08] Um where originally everyone focused on
[L721] [26:02.88] automatic theorem proving. So having the
[L722] [26:05.08] machine find proofs from
[L723] [26:07.92] all by itself.
[L724] [26:09.40] But that's very very difficult
[L725] [26:12.64] and not necessarily what what
[L726] [26:15.12] mathematicians need.
[L727] [26:17.72] And so those proof assistants are more
[L728] [26:20.84] like
[L729] [26:22.36] where formal language is like like
[L730] [26:24.32] programming languages but where you can
[L731] [26:26.20] write mathematic definition mathematical
[L732] [26:28.12] definitions mathematical statements
[L733] [26:31.00] and they will help you prove. So so some
[L734] [26:34.32] small proof steps they will do
[L735] [26:35.68] automatically and for others the the
[L736] [26:38.88] user still has to guide the prover
[L737] [26:41.16] through through the major steps.
[L738] [26:43.72] But the good thing is that the proof is
[L739] [26:45.00] recorded also in a format that the
[L740] [26:46.72] machine can understand and recheck.
[L741] [26:50.08] So when you complete a proof in lean or
[L742] [26:52.64] Coq, or Isabelle, or one of those tools,
[L743] [26:55.64] and and it is rechecked, and and the
[L744] [26:58.48] computer makes sure that all inferences
[L745] [27:00.88] are justified, that you didn't forget
[L746] [27:02.96] any case, that you uh you didn't use a
[L747] [27:05.96] conclusion as an hypothesis, or where
[L748] [27:08.08] all all kind of
[L749] [27:09.84] problems you can have with a pencil and
[L750] [27:11.64] paper proof.
[L751] [27:13.04] And so, in the end, you get proofs that
[L752] [27:15.04] are extremely uh
[L753] [27:16.80] reliable, extremely credible.
[L754] [27:20.08] Um and and it's been so so those tools
[L755] [27:23.40] have been used a little bit uh
[L756] [27:27.28] for well for for for some um
[L757] [27:30.32] uh some big mathematical results, where
[L758] [27:32.64] where the proofs are so big that that
[L759] [27:34.84] that they can't be done just by humans.
[L760] [27:37.16] They really need uh
[L761] [27:38.76] computer assistance.
[L762] [27:40.48] Uh
[L763] [27:41.20] I think there's a recent example with a
[L764] [27:43.40] weak uh Goldbach conjecture. Uh so, part
[L765] [27:46.64] of the proof involved checking a whole
[L766] [27:48.64] lot of inequality, maybe a thousand
[L767] [27:50.80] inequalities involving several real
[L768] [27:53.40] variables, and blah blah blah. And so,
[L769] [27:56.88] um
[L770] [27:57.80] computer assistance was really needed uh
[L771] [27:59.88] to make sure that that everything was
[L772] [28:01.72] checked, and and there was no no human
[L773] [28:04.20] mistakes uh left.
[L774] [28:07.12] And and maybe we'll talk about
[L775] [28:09.32] generative AI later, but there's there's
[L776] [28:11.60] also now a lot of interest in
[L777] [28:13.80] conjunction with generative AI.
[L778] [28:16.12] Uh AI is pretty good as that coming up
[L779] [28:18.56] with plausible proofs.
[L780] [28:20.88] Okay, but then they have to be checked
[L781] [28:22.88] by humans.
[L782] [28:25.36] Unless uh
[L783] [28:26.96] AI writes a proof in one of those formal
[L784] [28:29.04] languages like Lean, in which case it
[L785] [28:31.36] can be checked by a machine, and that's
[L786] [28:34.32] much more much more effective.
[L787] [28:37.48] Um
[L788] [28:38.80] So, yeah. So, it's it's the idea of of
[L789] [28:41.40] using the machine to help you write
[L790] [28:43.24] proofs and recheck proofs that you've
[L791] [28:45.60] written yourself, or maybe with some
[L792] [28:47.24] help from an AI.
[L793] [28:49.24] And now those tools can also be used to
[L794] [28:51.48] prove properties about programs.
[L795] [28:54.92] And so so I I spent uh
[L796] [28:58.16] many [clears throat] years uh uh
[L797] [29:00.32] proving the correctness of a compiler, C
[L798] [29:02.92] compiler,
[L799] [29:04.24] uh using one of those tools, the the
[L800] [29:06.16] Rock uh proof assistant.
[L801] [29:09.44] Um so so basically um
[L802] [29:12.80] when I'm proving about the compiler, so
[L803] [29:14.76] it takes C code, it produces assembly
[L804] [29:16.72] code, and
[L805] [29:18.04] um proving that the assembly code is
[L806] [29:19.52] faithful to the C code. So so there's no
[L807] [29:21.72] miscompilation. The the compiler didn't
[L808] [29:23.80] introduce a bug in the program that
[L809] [29:25.88] wasn't there originally.
[L810] [29:28.64] And and it's a fairly big proof because
[L811] [29:31.08] compilers do complicated things about
[L812] [29:32.72] programs, and then you have to define
[L813] [29:34.36] exactly what it means to preserve the
[L814] [29:36.32] semantics of a program. So you have to
[L815] [29:37.96] define the semantics of your programming
[L816] [29:39.64] languages. And and so so it's all a very
[L817] [29:42.68] good use of those uh uh machines
[L818] [29:46.08] uh of those proof assistants. Uh
[L819] [29:49.08] the the same work could be done on
[L820] [29:50.48] paper, but I mean this would be a proof
[L821] [29:52.76] of several thousand pages, and nobody
[L822] [29:55.28] would want to read it.
[L823] [29:57.32] Nobody would trust it. It's just too
[L824] [29:59.00] big. Uh and and it would be very hard to
[L825] [30:01.60] evolve. Um
[L826] [30:03.92] One good thing about
[L827] [30:05.76] um those um
[L828] [30:07.36] mechanized verifications of of programs
[L829] [30:09.56] is that
[L830] [30:10.44] uh
[L831] [30:11.12] it can also help you evolve the program.
[L832] [30:13.44] Okay? You can add new features and so
[L833] [30:15.24] on, and and adapt your proofs, and be
[L834] [30:17.24] really sure that you haven't introduced
[L835] [30:19.12] a regression or things like that.
[L836] [30:23.20] Um so yeah, so it's really uh
[L837] [30:24.84] programming taken to a higher level. Um
[L838] [30:28.84] And and today it's quite expensive. Um
[L839] [30:31.76] it takes a lot more time to to prove a
[L840] [30:34.16] program than to write it in the first
[L841] [30:36.16] place. But maybe this is getting a
[L842] [30:38.08] little better.
[L843] [30:39.48] Um
[L844] [30:41.68] Yeah, and I should also mention another
[L845] [30:43.44] great uh of certified software is the
[L846] [30:46.80] it's a microkernel, the SEL4
[L847] [30:49.12] microkernel,
[L848] [30:50.52] uh developed in Australia, and which is
[L849] [30:53.24] used as an hypervisor in in some in some
[L850] [30:56.84] applications.
[L851] [30:58.36] And so it is uh
[L852] [31:00.88] is
[L853] [31:02.00] really like 8,000 lines of extremely
[L854] [31:04.44] technical C code that that, you know,
[L855] [31:06.48] manipulates uh
[L856] [31:08.36] uh processes and uh
[L857] [31:11.52] capabilities and security tokens and so
[L858] [31:14.12] on. And it's been proved correct. Every
[L859] [31:16.68] line has been proved correct. And that
[L860] [31:18.76] that's a very big achievement.
[L861] [31:21.00] >> When you mentioned the example of
[L862] [31:22.56] verifying a mathematical proof, that
[L863] [31:26.20] uh makes sense to me. When you talk
[L864] [31:28.00] about proving something about a program,
[L865] [31:31.20] it's a little bit more abstract to me or
[L866] [31:33.00] I'm having some trouble visualizing.
[L867] [31:35.60] Could you give a concrete example like
[L868] [31:38.48] uh maybe some trivial program that we're
[L869] [31:41.68] trying to prove something about it and
[L870] [31:43.20] how that uh theorem prover would work.
[L871] [31:46.64] >> Let's say
[L872] [31:48.40] you have a function that takes three
[L873] [31:49.88] numbers, X, Y, Z, and um returns the
[L874] [31:52.84] average of those numbers.
[L875] [31:55.28] Okay?
[L876] [31:56.56] Um
[L877] [31:58.72] only
[L878] [31:59.96] yeah, and and maybe
[L879] [32:02.96] you're using a not completely obvious
[L880] [32:05.12] formula like uh
[L881] [32:07.36] T equals X plus Y and then T equals T
[L882] [32:10.88] plus Z and then um T equals T divided by
[L883] [32:14.64] 3 and then return T. Okay? So not that
[L884] [32:17.52] exactly is the formula for the
[L885] [32:20.00] average.
[L886] [32:22.72] Uh and you want to prove that that
[L887] [32:24.08] function is correct. So so you want to
[L888] [32:26.72] prove that
[L889] [32:28.36] it it returns uh
[L890] [32:30.52] X plus Y plus Z divided by 3. And maybe
[L891] [32:33.60] you will have to make it clear whether
[L892] [32:35.32] you're rounding up or rounding down.
[L893] [32:38.36] If you're using integers or
[L894] [32:39.76] floating-point numbers, you know, it's
[L895] [32:41.20] not a exact arithmetic, so
[L896] [32:43.71] >> [snorts]
[L897] [32:43.84] >> um
[L898] [32:45.12] So, yeah, you you'll have to to say
[L899] [32:46.92] exactly what you mean by divided by
[L900] [32:48.60] three.
[L901] [32:49.61] >> [snorts]
[L902] [32:50.00] >> And then, uh if you are in a language
[L903] [32:51.72] like C, you can have arithmetic
[L904] [32:53.20] overflows.
[L905] [32:54.68] Okay? When you compute X + Y or
[L906] [32:57.84] + Z,
[L907] [32:59.36] um
[L908] [33:00.20] you can overflow the range of
[L909] [33:01.96] representable representable integers,
[L910] [33:03.92] and in C, it's it's a bug. It's an
[L911] [33:05.72] undefined behavior.
[L912] [33:07.72] So, typically, you will want to put a
[L913] [33:10.16] so-called precondition on your function
[L914] [33:11.92] saying, "Okay,
[L915] [33:13.16] uh if you call me, call me with numbers
[L916] [33:15.84] that are between, I don't know, zero and
[L917] [33:18.00] 1 million for instance, but no bigger
[L918] [33:20.08] than that." And and then, the prover
[L919] [33:23.60] will check that no overflow can occur in
[L920] [33:26.12] this case.
[L921] [33:27.44] Um okay? And so So, basically, you have
[L922] [33:31.20] the precondition that says, "Okay, these
[L923] [33:33.40] are safety guarantees um
[L924] [33:35.88] that must hold of the parameters,
[L925] [33:37.68] otherwise, anything can happen."
[L926] [33:40.52] And then, there will be a little bit of
[L927] [33:42.16] kind of symbolic execution of the
[L928] [33:43.68] function body
[L929] [33:45.08] that says, "Okay, when you T equals X +
[L930] [33:47.28] Y, then T plus equals Z, then T {slash}
[L931] [33:50.04] equals three, then in the end, T is X +
[L932] [33:52.68] Y + Z divided by three, provided no
[L933] [33:55.28] overflow occurred."
[L934] [33:58.16] And then, you put that with a
[L935] [33:59.56] precondition that says,
[L936] [34:01.36] "There cannot be any
[L937] [34:02.72] overflow," and you get your final
[L938] [34:04.64] result.
[L939] [34:05.68] Okay? So, basically, you're stating a
[L940] [34:07.12] contract for your function, the pre-
[L941] [34:09.96] hypotheses on the arguments,
[L942] [34:11.84] uh guarantees on the results.
[L943] [34:14.00] And
[L944] [34:15.36] uh and and you want to prove or analyze
[L945] [34:18.76] the function body to show that this
[L946] [34:21.16] contract is respected.
[L947] [34:23.24] I hope it's a little more concrete.
[L948] [34:25.72] >> So, it it sounds like a lean will help
[L949] [34:28.44] you basically take in some invariants
[L950] [34:31.28] about a program and kind of propagate
[L951] [34:33.00] them through line by line and uphold
[L952] [34:36.04] them. And so you can say something about
[L953] [34:38.44] >> Yes.
[L954] [34:41.04] Maybe not Lean by itself. Well, a
[L955] [34:43.40] program prover a program prover will do
[L956] [34:45.60] exactly what you say.
[L957] [34:47.32] And for Lean to be able to do it, you
[L958] [34:49.84] still need to teach it a little bit
[L959] [34:51.32] about the semantics of your programming
[L960] [34:52.84] language.
[L961] [34:54.04] Okay, that
[L962] [34:55.68] what does a plus means, what does
[L963] [34:59.40] assignment means, okay? Lean Lean is
[L964] [35:02.00] mathematics. You don't assign in
[L965] [35:03.96] mathematics. You don't say x equals x
[L966] [35:05.80] plus one or or or
[L967] [35:08.20] or you're just comparing x and x plus y
[L968] [35:10.16] and it's always false. There's no
[L969] [35:11.80] assignment in mathematics. There's
[L970] [35:13.64] assignment in many programs. So you need
[L971] [35:16.04] to
[L972] [35:17.16] make it explicit that
[L973] [35:19.44] there are [snorts] actually three
[L974] [35:20.52] different states for the t variable,
[L975] [35:22.80] three different values and and
[L976] [35:26.60] and relate [clears throat] those values
[L977] [35:27.84] to
[L978] [35:29.40] Well, the program defines what those
[L979] [35:30.80] values are and then a prover like Lean
[L980] [35:33.20] can can reason about those three
[L981] [35:35.24] successive values.
[L982] [35:37.40] Because now you're in you're in
[L983] [35:38.80] mathematics.
[L984] [35:40.00] And and that that kind of bridge between
[L985] [35:43.44] programs and their mathematical meaning
[L986] [35:46.28] is called semantics. That that the field
[L987] [35:48.80] of semantics of programming languages
[L988] [35:51.24] has been a big topic in in PL research
[L989] [35:53.64] since the the '60s at least.
[L990] [35:56.52] >> Am I understanding then that
[L991] [35:58.60] like a pure functional programming
[L992] [36:00.08] language, the gap between mathematics
[L993] [36:03.28] and
[L994] [36:04.48] the actual symbols is much smaller than
[L995] [36:07.08] an imperative?
[L996] [36:08.04] >> Absolutely. Yeah, you're you're
[L997] [36:10.00] absolutely right.
[L998] [36:12.72] And that's one of the reasons why
[L999] [36:15.64] people who do formal methods don't like
[L1000] [36:17.56] assignment, don't like imperative
[L1001] [36:18.96] features.
[L1002] [36:20.32] Purely functional style is much closer
[L1003] [36:22.88] to mathematical style, so much easier to
[L1004] [36:24.72] reason going
[L1005] [36:26.28] There can still be few discrepancies
[L1006] [36:28.80] between the program and the math. Uh,
[L1007] [36:31.00] for instance, functional programs may
[L1008] [36:32.24] not terminate.
[L1009] [36:33.80] They may loop forever. Um, mathematics
[L1010] [36:36.84] doesn't like that. So, so you need a way
[L1011] [36:38.60] to to reason about termination.
[L1012] [36:41.24] Um, and uh
[L1013] [36:44.32] and also yeah, sometimes for instance,
[L1014] [36:47.16] the the arithmetic you get in the
[L1015] [36:48.56] programming language is not
[L1016] [36:50.80] uh, integer arithmetic or is not
[L1017] [36:53.24] uh, real reals. [clears throat] You
[L1018] [36:55.04] know, it's floating point, it's not
[L1019] [36:56.36] reals. So, so you still have to
[L1020] [36:59.16] uh, account for that
[L1021] [37:01.36] gap. Uh, but you're you're absolutely
[L1022] [37:03.84] right that the gap is much shorter for
[L1023] [37:06.12] functional programming. And and uh
[L1024] [37:10.52] in the experience of CompCert, my my
[L1025] [37:12.20] verified compiler,
[L1026] [37:13.84] I think the the first decision was to
[L1027] [37:15.40] write it in a purely functional style
[L1028] [37:18.40] so that it would be easier to to reason
[L1029] [37:20.40] about it later.
[L1030] [37:22.12] >> You mentioned the the specifications
[L1031] [37:24.32] that we could prove, and one of them was
[L1032] [37:27.24] proving that the program terminates, but
[L1033] [37:29.76] I thought that's a famously
[L1034] [37:32.16] difficult or impossible. I forgot
[L1035] [37:33.72] exactly that the halting problem, right?
[L1036] [37:35.40] So, how how is that something that you
[L1037] [37:37.60] could prove?
[L1038] [37:39.08] >> Okay, so what the
[L1039] [37:41.08] um computability theory says is that
[L1040] [37:43.12] there is no algorithm that will always
[L1041] [37:46.28] that can always say
[L1042] [37:48.24] this program terminates or this program
[L1043] [37:50.00] doesn't terminate.
[L1044] [37:51.40] Um,
[L1045] [37:52.20] so so there will always be some very
[L1046] [37:53.84] weird programs for which your your
[L1047] [37:57.64] analyzer your your automatic termination
[L1048] [37:59.84] analyzer will produce a wrong result
[L1049] [38:02.60] or will not terminate itself.
[L1050] [38:06.68] Uh, so it will not work.
[L1051] [38:08.44] Um, uh but
[L1052] [38:11.12] still for for many programs, you can
[L1053] [38:13.44] succeed. Okay, you can write automatic
[L1054] [38:16.00] termination analyzers that will work for
[L1055] [38:18.16] a large uh class of programs.
[L1056] [38:21.76] And then the termination analysis,
[L1057] [38:23.84] termination proof can also be done by
[L1058] [38:25.36] hand by by a mathematician. Okay, so
[L1059] [38:30.32] So, perhaps
[L1060] [38:32.92] a human can can see through those weird
[L1061] [38:36.64] Turing programs that that are hard to
[L1062] [38:38.96] prove to terminate and
[L1063] [38:40.96] and and recognize the trick.
[L1064] [38:43.00] But, anyway, so yeah, it's a hard
[L1065] [38:44.56] problem and all all program verification
[L1066] [38:47.36] tasks are are difficult pro
[L1067] [38:49.96] problems, okay? Uh
[L1068] [38:52.48] They are pretty much all undecidable.
[L1069] [38:55.44] So, you know that there there is no
[L1070] [38:57.08] static analyzer that will always
[L1071] [38:59.92] find all problem all problems in all
[L1072] [39:02.08] programs.
[L1073] [39:03.62] >> [snorts]
[L1074] [39:03.92] >> But, still you can try, okay? You can
[L1075] [39:06.20] try for specific problems, for specific
[L1076] [39:08.60] programs and and get some very useful
[L1077] [39:11.28] results out of them out of that.
[L1078] [39:13.80] You only need to be able to do it for
[L1079] [39:15.20] the cases that are of interest to you,
[L1080] [39:17.44] the programs you really care about.
[L1081] [39:20.00] >> OpenAI, Anthropic, Cursor, and Vercel
[L1082] [39:23.76] all use this product to make their lives
[L1083] [39:25.48] better.
[L1084] [39:26.44] And the problem it solves is when you're
[L1085] [39:28.32] building SaaS or an AI product and you
[L1086] [39:30.96] want to sell to other companies, there's
[L1087] [39:32.88] all these requirements you need to meet.
[L1088] [39:34.96] There's SSO, there's SCIM, there's RBAC,
[L1089] [39:38.60] there's audit logs. These are all things
[L1090] [39:40.40] that take time to integrate, but aren't
[L1091] [39:42.60] the main focus of your app. WorkOS is an
[L1092] [39:44.92] API layer that lets you meet all of
[L1093] [39:46.60] these requirements in just a few lines
[L1094] [39:48.76] of code. So, let's say you have a new
[L1095] [39:50.80] SaaS product and you want to sell to
[L1096] [39:52.48] other companies, WorkOS will solve all
[L1097] [39:54.96] of these critical feature gaps for you.
[L1098] [39:57.72] You can check them out at workos.com to
[L1099] [40:00.12] learn more and get started. And I
[L1100] [40:02.28] appreciate them for supporting my work
[L1101] [40:04.20] and sponsoring this podcast. One thing
[L1102] [40:06.50] [snorts] I saw when I was researching
[L1103] [40:07.68] OCaml is that
[L1104] [40:09.96] uh in 2022, OCaml added multicore
[L1105] [40:13.40] support. And but from my memory, I
[L1106] [40:16.40] remember multi-core processors became
[L1107] [40:19.16] standard much earlier than that. And so,
[L1108] [40:21.60] I figured there might be some unique
[L1109] [40:23.56] engineering challenge in adding that
[L1110] [40:25.16] support. So, yeah, what what happened
[L1111] [40:27.48] there and what made it difficult?
[L1112] [40:29.96] >> Uh well, there were
[L1113] [40:31.80] engineering challenges, that's for sure.
[L1114] [40:33.72] There there were also some language
[L1115] [40:34.96] design issues.
[L1116] [40:36.80] So, so but let's talk about the
[L1117] [40:38.56] engineering challenges first.
[L1118] [40:40.52] Um so, it's true that that when you have
[L1119] [40:42.80] a a language with with a runtime system
[L1120] [40:45.72] memory allocator or garbage collector
[L1121] [40:48.28] uh
[L1122] [40:49.64] well, at least the one of for for OCaml
[L1123] [40:51.92] was really designed with sequential
[L1124] [40:53.72] executions in mind.
[L1125] [40:55.48] So, if you have if you add a shared
[L1126] [40:57.44] memory concurrency, then you need a
[L1127] [41:00.04] garbage collector or a memory allocator
[L1128] [41:01.76] that that that that can work
[L1129] [41:03.24] concurrently. And that's actually quite
[L1130] [41:05.44] difficult.
[L1131] [41:06.72] Uh at least if you want them to be fast.
[L1132] [41:09.88] Of course, you
[L1133] [41:11.16] you could always, you know, take take
[L1134] [41:12.64] take a lock at at every operation in the
[L1135] [41:15.52] heap, but then uh you would
[L1136] [41:17.64] sequentialize your programs. Basically,
[L1137] [41:19.48] they they they would run as slowly as a
[L1138] [41:21.52] single processor. So, so that's not
[L1139] [41:24.04] interesting. So, yeah, so there were
[L1140] [41:25.96] engineering challenges. Um um yeah, I
[L1141] [41:28.80] was at least initially quite quite
[L1142] [41:30.88] reluctant to
[L1143] [41:32.84] uh basically re-implement a complete uh
[L1144] [41:36.20] garbage collector and and uh memory
[L1145] [41:38.76] allocator or large parts of the runtime
[L1146] [41:40.28] system. That's what we did eventually
[L1147] [41:42.52] with uh as well, it was done mostly by
[L1148] [41:45.12] the team at OCaml Labs at Cambridge
[L1149] [41:47.52] University.
[L1150] [41:48.68] >> [snorts]
[L1151] [41:48.76] >> Uh but yes, it was a really big rewrite.
[L1152] [41:53.72] Um but then I said there's also a
[L1153] [41:56.28] language design issue.
[L1154] [41:58.88] Which is that for for the longest time
[L1155] [42:01.24] well
[L1156] [42:02.20] uh
[L1157] [42:03.24] is
[L1158] [42:04.08] now when when you say uh
[L1159] [42:06.56] multi-core
[L1160] [42:09.00] processors and so on, pretty much
[L1161] [42:10.68] everyone
[L1162] [42:11.88] and language support for multi-core
[L1163] [42:13.92] processors, everyone thinks about
[L1164] [42:16.20] language support for shared memory
[L1165] [42:18.00] concurrency.
[L1166] [42:19.36] You know, this model where you have
[L1167] [42:20.56] several sites of control and they access
[L1168] [42:23.08] the same memory
[L1169] [42:24.80] and basically the sites communicate by
[L1170] [42:26.92] modifying the memory and someone else is
[L1171] [42:29.40] going to notice.
[L1172] [42:31.00] You know, it and
[L1173] [42:32.80] I've never liked this model of of
[L1174] [42:35.92] communication.
[L1175] [42:38.16] I mean, it's a bit like if you want to
[L1176] [42:40.44] communicate with your neighbor then then
[L1177] [42:42.20] you you you break into their houses and
[L1178] [42:44.96] their house and then you move the
[L1179] [42:46.96] furniture around and then when they are
[L1180] [42:48.88] back they say, "Oh, something something
[L1181] [42:51.12] was moved so it's probably Iron who's
[L1182] [42:53.04] trying to tell us something."
[L1183] [42:55.08] Maybe you could just meet your
[L1184] [42:56.32] neighbors, you know? And and that would
[L1185] [42:58.24] be things like message passing
[L1186] [43:01.24] which is a completely different form of
[L1187] [43:02.80] communication, much higher level.
[L1188] [43:05.12] So, yeah, so for the longest time I was
[L1189] [43:07.48] really interested in message passing
[L1190] [43:10.60] concurrency.
[L1191] [43:12.84] And there's for instance a functional
[L1192] [43:15.36] language called Erlang that was built on
[L1193] [43:18.32] around those ideas and that I found
[L1194] [43:20.72] quite interesting.
[L1195] [43:22.28] However, I never got to to have a
[L1196] [43:24.92] decent language design and
[L1197] [43:28.40] everyone was saying, "No, but but it
[L1198] [43:30.36] it's it's too costly. It's not
[L1199] [43:32.60] effective. There's too much copying of
[L1200] [43:34.32] data.
[L1201] [43:35.60] With shared memory you can you can share
[L1202] [43:37.36] some kind of huge database in memory. If
[L1203] [43:40.28] you don't modify it too much, then
[L1204] [43:42.24] basically the sharing is the the
[L1205] [43:44.56] concurrency is free.
[L1206] [43:46.60] While with message passing we'll have to
[L1207] [43:48.08] exchange a lot of data so
[L1208] [43:50.60] to to get the same effect so so you will
[L1209] [43:52.32] pay more for it.
[L1210] [43:53.72] Anyway,
[L1211] [43:54.76] so
[L1212] [43:55.92] so okay, so
[L1213] [43:57.76] starting with Java I guess and then C
[L1214] [44:00.60] C++ 2011 there was this idea that okay,
[L1215] [44:04.16] we we we need to expose shared memory
[L1216] [44:06.28] concurrency to the programmers.
[L1217] [44:09.08] But then comes the problem of the memory
[L1218] [44:10.80] model, which is that
[L1219] [44:12.92] what happens when there's a race, for
[L1220] [44:15.28] instance, when when two
[L1221] [44:17.20] uh two threads want to access the same
[L1222] [44:20.04] uh location, and maybe they want to
[L1223] [44:21.60] modify it in different ways.
[L1224] [44:23.76] And so, sometimes parts of the C C++
[L1225] [44:27.32] standard says, "It's undefined behavior.
[L1226] [44:29.76] Anything can happen." But still, you
[L1227] [44:31.56] need to give a little more guarantees.
[L1228] [44:33.80] Uh at the other end of the spectrum,
[L1229] [44:35.48] there's a so-called uh sequential
[L1230] [44:36.84] consistency, which says, "Well, what
[L1231] [44:38.80] happens is like an interleaving of reads
[L1232] [44:41.80] and writes of your program."
[L1233] [44:43.64] You don't know which interleaving, but
[L1234] [44:44.92] there is an interleaving.
[L1235] [44:47.36] But that doesn't work with modern
[L1236] [44:50.00] uh processors, multi-core processors.
[L1237] [44:52.00] They reorder memory accesses in in very
[L1238] [44:54.96] clever ways to get more performance. And
[L1239] [44:57.40] so, viewed from the program, it's very
[L1240] [44:59.08] hard to predict what they are actually
[L1241] [45:00.36] doing.
[L1242] [45:01.60] And so, you need to give your
[L1243] [45:03.40] programmers, when you're designing a
[L1244] [45:04.84] language with shared memory concurrency,
[L1245] [45:06.40] you need to give your programmers some
[L1246] [45:07.96] guarantees about uh the ordering of
[L1247] [45:11.24] reads and writes, concurrent reads and
[L1248] [45:12.88] writes, while not constraining the
[L1249] [45:14.88] hardware too much.
[L1250] [45:17.04] And it's very difficult. So, Java went
[L1251] [45:20.20] through like five different iterations
[L1252] [45:22.28] of the memory model. Some were too
[L1253] [45:23.96] strict, some were too lax, some were
[L1254] [45:25.76] kind of in
[L1255] [45:27.16] inconsistent. They were were were making
[L1256] [45:29.48] predictions, impossible predictions,
[L1257] [45:31.48] where where the past depends on the
[L1258] [45:32.96] future.
[L1259] [45:34.66] >> [snorts]
[L1260] [45:34.84] >> Crazy, really crazy stuff.
[L1261] [45:37.04] Uh then C C++ 11 did a little better,
[L1262] [45:40.16] but still extremely complex memory
[L1263] [45:42.36] model. And so, when we wanted to add
[L1264] [45:44.72] when the especially the OCaml Labs
[L1265] [45:46.84] people wanted to add uh shared memory
[L1266] [45:48.88] concurrency to OCaml, we had to also
[L1267] [45:51.36] agree on a memory model
[L1268] [45:53.24] that would be
[L1269] [45:54.68] exposed to the programmers.
[L1270] [45:56.64] And and that's also took quite a bit of
[L1271] [45:58.92] a design uh quite a bit of time to come
[L1272] [46:01.24] up with a good design. Uh
[L1273] [46:03.28] And I
[L1274] [46:04.16] I think it's it's
[L1275] [46:05.80] better and easier to understand and use
[L1276] [46:08.36] than the one of Java, but the the OCaml
[L1277] [46:11.36] memory model is still quite complicated.
[L1278] [46:14.32] And
[L1279] [46:15.72] And sometimes I feel sorry our users are
[L1280] [46:18.00] are exposed to that. Okay. Uh
[L1281] [46:21.20] Uh
[L1282] [46:22.08] So, that that that explains why it took
[L1283] [46:24.16] so long.
[L1284] [46:25.76] Solving the
[L1285] [46:27.32] engineering challenges, but also
[L1286] [46:30.36] having a
[L1287] [46:31.56] agreeing on the memory model and what
[L1288] [46:33.32] kind of guarantees we're going to give
[L1289] [46:34.96] to programmers.
[L1290] [46:36.56] Oh, yeah. I forgot to say one thing,
[L1291] [46:38.76] which is that
[L1292] [46:40.36] So, C and C++ there's a lot of things
[L1293] [46:42.92] you can say, "Oh, it's just undefined
[L1294] [46:44.40] behavior or anything can happen."
[L1295] [46:46.52] In type-safe languages like Java and
[L1296] [46:48.44] OCaml, you want to give stronger
[L1297] [46:49.92] guarantees. Okay. Maybe many things can
[L1298] [46:53.00] happen, but your data should should
[L1299] [46:55.68] remain well-typed.
[L1300] [46:57.56] Okay. Typically, you don't want to
[L1301] [46:59.56] expose an object to another thread
[L1302] [47:02.04] before it's been fully initialized, for
[L1303] [47:03.68] instance.
[L1304] [47:04.84] Um And And that's that's actually very
[L1305] [47:08.20] hard to guarantee in your memory model.
[L1306] [47:10.84] And then
[L1307] [47:12.16] you have to implement that memory model,
[L1308] [47:13.60] so your compiler also needs to take
[L1309] [47:15.28] extra
[L1310] [47:16.48] precautions to to to guarantee this. So,
[L1311] [47:19.48] yeah, type safety in the presence of
[L1312] [47:22.84] shared memory concurrency is is not
[L1313] [47:25.80] obvious at all.
[L1314] [47:27.60] And so, that's why it took so long.
[L1315] [47:30.20] >> So, in Python, I know there's the famous
[L1316] [47:32.68] GIL or the global interpreter lock. What
[L1317] [47:35.80] is that lock protecting? Is it the the
[L1318] [47:37.92] cleanup of objects on the heap or is it
[L1319] [47:40.88] something else?
[L1320] [47:41.92] >> Among other things, yes. So, yeah, we we
[L1321] [47:44.52] had the same thing in OCaml before
[L1322] [47:46.80] before
[L1323] [47:47.96] multicore OCaml with
[L1324] [47:50.24] >> [snorts]
[L1325] [47:51.16] >> with Marstin. So, yeah, well, basically,
[L1326] [47:53.80] the idea that when when your runtime
[L1327] [47:55.36] system is not thread-safe, as we said,
[L1328] [47:57.92] you can protect the non-thread safe
[L1329] [47:59.84] functions by your lock so that
[L1330] [48:02.24] they will never be executed
[L1331] [48:03.40] concurrently.
[L1332] [48:04.72] But if you take the lock at every
[L1333] [48:06.32] allocation and release it,
[L1334] [48:08.80] you take and release the lock for every
[L1335] [48:10.20] allocation and it's just too slow
[L1336] [48:11.80] anyway.
[L1337] [48:12.96] And so the idea is that
[L1338] [48:15.24] you take the lock when you enter Python
[L1339] [48:18.32] code, let's say, and you start executing
[L1340] [48:20.88] Python code.
[L1341] [48:22.48] But you can still release it when you do
[L1342] [48:25.00] input output for instance, when you're
[L1343] [48:26.36] going to block for a long time.
[L1344] [48:28.60] Or when you're calling into C code that
[L1345] [48:31.40] that
[L1346] [48:32.80] that is thread safe and is not going to
[L1347] [48:34.60] use your runtime system.
[L1348] [48:36.60] Then you can release the lock and some
[L1349] [48:38.20] other
[L1350] [48:39.44] Python thread can take it and execute.
[L1351] [48:42.52] So you get a little bit of concurrency.
[L1352] [48:44.32] You can overlap computations in your
[L1353] [48:47.40] high-level language with IO or
[L1354] [48:49.40] computation is a low-level language in
[L1355] [48:51.60] another language.
[L1356] [48:53.16] But you still have mutual exclusion
[L1357] [48:54.84] between your
[L1358] [48:56.76] between two threads running Python or
[L1359] [48:59.28] running OCaml before before multicore
[L1360] [49:01.52] OCaml.
[L1361] [49:03.64] So so you get some benefits like
[L1362] [49:07.04] concurrent IO, but you don't get any
[L1363] [49:08.64] parallelism.
[L1364] [49:09.92] Okay, yeah. You don't get a speed up for
[L1365] [49:12.48] computations.
[L1366] [49:14.64] And so so yeah, so we used to have this
[L1367] [49:17.28] this this GIL in in in OCaml as well.
[L1368] [49:20.88] And
[L1369] [49:22.48] so you can get rid of it, but in
[L1370] [49:24.72] general, you need to redesign at least
[L1371] [49:26.96] the garbage collector and and memory
[L1372] [49:29.52] allocator.
[L1373] [49:32.80] There's probably a few places in the
[L1374] [49:34.44] OCaml runtime system that still use
[L1375] [49:36.08] locks to
[L1376] [49:38.24] to to ensure mutual exclusion like in
[L1377] [49:40.04] the IO subsystem.
[L1378] [49:44.60] And and some phases of the garbage
[L1379] [49:46.16] collector, I think that there's a phase
[L1380] [49:48.24] which is kind of stop the world where
[L1381] [49:50.12] you need to make sure that everyone
[L1382] [49:53.28] no no no camel code is is running.
[L1383] [49:56.16] So for a short time you need to make
[L1384] [49:57.68] sure that everyone is stopped and then
[L1385] [49:59.72] do a little bit of work to finish the GC
[L1386] [50:02.08] and then you can restart everyone.
[L1387] [50:04.56] Um so yeah, that these are tricky things
[L1388] [50:07.08] and I don't know what the Python people
[L1389] [50:08.76] are up to with their GIL if if they
[L1390] [50:10.96] finally managed to remove it or
[L1391] [50:13.68] they're still working on it but I I I've
[L1392] [50:15.52] heard they're making progress. So.
[L1393] [50:17.96] >> Yeah, you mentioned Python calling into
[L1394] [50:21.08] C and I've seen that pattern before of a
[L1395] [50:24.48] higher level language interfacing with a
[L1396] [50:26.64] lower level one. How does that binding
[L1397] [50:29.72] typically work?
[L1398] [50:31.60] >> Oh, it's another can of worms.
[L1399] [50:33.68] Um
[L1400] [50:36.24] Um
[L1401] [50:38.40] Well, there are two aspects. There are
[L1402] [50:39.48] there are the the control flow and there
[L1403] [50:41.12] are the
[L1404] [50:42.40] the data.
[L1405] [50:43.92] So the control part is is
[L1406] [50:47.00] not that hard. So yes, you need you need
[L1407] [50:49.08] a mechanism so that your your Python
[L1408] [50:51.28] interpreter or your OCaml compiled code
[L1409] [50:53.72] will actually jump to the C function.
[L1410] [50:57.04] Uh so for OCaml basically you you tell
[L1411] [50:59.40] your OCaml compiler that this function
[L1412] [51:01.20] is not implemented in OCaml, it's
[L1413] [51:03.12] actually implemented by a C function and
[L1414] [51:05.12] you give its name and then the compiler
[L1415] [51:07.04] will emit a call to the C function using
[L1416] [51:09.60] the C calling conventions which are not
[L1417] [51:11.44] exactly the same as the OCaml calling
[L1418] [51:13.16] convention but
[L1419] [51:14.64] the compiler knows about that. And so it
[L1420] [51:17.24] will
[L1421] [51:18.16] call the C function maybe through a
[L1422] [51:19.64] little bit of glue code or whatever and
[L1423] [51:22.32] then the C function will execute and and
[L1424] [51:25.28] return back to the OCaml code.
[L1425] [51:28.12] Um
[L1426] [51:30.28] That's relatively easy. Uh now the hard
[L1427] [51:33.40] part is uh data
[L1428] [51:35.64] uh like function arguments and function
[L1429] [51:37.68] results
[L1430] [51:39.40] because OCaml and C have different data
[L1431] [51:42.20] representations.
[L1432] [51:43.92] Uh for instance, a floating point number
[L1433] [51:45.72] in in OCaml is generally boxed, so it's
[L1434] [51:48.88] allocated in the heap and handled
[L1435] [51:50.40] through a pointer. So, it's more like a
[L1436] [51:52.64] double star in in C
[L1437] [51:55.32] and it's not a double, which is not
[L1438] [51:57.68] allocated.
[L1439] [51:59.32] Just it's in a register.
[L1440] [52:01.72] Um so
[L1441] [52:03.88] so typically the C code needs to use a
[L1442] [52:06.32] so-called foreign function interface, so
[L1443] [52:08.20] some C function and macros provided by
[L1444] [52:10.36] OCaml to access the OCaml data, the
[L1445] [52:13.48] OCaml arguments, you know, extract the
[L1446] [52:15.72] part that it needs, the the numbers, the
[L1447] [52:19.44] uh
[L1448] [52:20.08] uh yeah, another example is arrays. Um
[L1449] [52:23.20] in OCaml when you have
[L1450] [52:25.44] a two-dimensional array, it's actually
[L1451] [52:26.96] an array of arrays. So, viewed from C,
[L1452] [52:29.20] it's an array of pointers to arrays.
[L1453] [52:31.48] While in C, an array of arrays is
[L1454] [52:33.60] there's no intermediate pointer, so it's
[L1455] [52:35.08] not the same representation. And so, you
[L1456] [52:37.24] have to explain to C or give C some
[L1457] [52:39.76] functions and macros to to access uh
[L1458] [52:43.12] elements in OCaml arrays. Uh it's not
[L1459] [52:45.56] exactly the same code that that that
[L1460] [52:48.32] that that you would do to access a C
[L1461] [52:50.48] array from C.
[L1462] [52:52.88] Okay, so you need accessors, but now if
[L1463] [52:55.60] you want to uh
[L1464] [52:57.48] if your C code wants to return some
[L1465] [52:59.36] complex results like a list, an array,
[L1466] [53:02.72] and so on, it needs to allocate it in
[L1467] [53:04.76] the OCaml heap. So, it needs to ask the
[L1468] [53:08.04] runtime system to do some heap
[L1469] [53:10.00] allocation and then fill the uh
[L1470] [53:12.51] >> [snorts]
[L1471] [53:12.96] >> heap blocks correctly. And then this
[L1472] [53:15.56] allocation can can trigger a garbage
[L1473] [53:17.52] collection, so the C code that also kind
[L1474] [53:20.00] of cooperate with a garbage collection
[L1475] [53:23.48] with registration mechanisms, etc., etc.
[L1476] [53:26.36] So, so there's quite a bit of work to to
[L1477] [53:28.32] be done.
[L1478] [53:29.48] And and uh and then different foreign
[L1479] [53:32.60] function interfaces
[L1480] [53:34.76] arrange this work differently. So,
[L1481] [53:36.76] there's a base FFI for OCaml, basically
[L1482] [53:39.64] uh it's a C code that must do all the
[L1483] [53:41.28] work.
[L1484] [53:42.36] But but then it can be very fast and
[L1485] [53:45.04] quite optimized.
[L1486] [53:46.60] Uh but there are other FFIs like the C
[L1487] [53:49.08] types FFI in OCaml where most of these
[L1488] [53:51.52] data conversion and and mediating
[L1489] [53:53.88] between two data formats is automated.
[L1490] [53:56.88] Uh you start basically with a
[L1491] [53:58.60] description of the the the the the C
[L1492] [54:00.96] type of the C function and and you can
[L1493] [54:03.32] automate some of those conversions. But
[L1494] [54:05.32] sometimes it can be tricky it can be
[L1495] [54:06.92] expensive. For instance, [snorts] you
[L1496] [54:08.60] may end up copying the whole array while
[L1497] [54:12.16] your C code only needs to access two or
[L1498] [54:13.96] three elements in it.
[L1499] [54:15.60] Um okay. So there's lots of trade-offs.
[L1500] [54:18.92] And quite frankly it it's a dirty part
[L1501] [54:22.32] of of programming language
[L1502] [54:23.44] implementation. Uh the the OCaml FFI is
[L1503] [54:27.92] not that clean, but if you look at the
[L1504] [54:29.92] Java FFI for instance, it's also quite
[L1505] [54:31.96] complicated. And for Python I've I've
[L1506] [54:34.52] never tried. Uh so I I don't know what
[L1507] [54:37.40] it looks like.
[L1508] [54:39.28] Uh
[L1509] [54:39.96] but yeah, it's a it's a necessity.
[L1510] [54:42.36] Uh but but it can be quite hard because
[L1511] [54:44.60] the data models are different between
[L1512] [54:47.44] the two languages.
[L1513] [54:49.28] >> So to kind of get the big picture, on
[L1514] [54:52.32] the OCaml side, there's an interpreter
[L1515] [54:55.36] which is a program running in
[L1516] [54:57.16] application space that is interpreting
[L1517] [55:00.56] your OCaml code. And then at some point
[L1518] [55:03.52] in the OCaml code, it says
[L1519] [55:06.48] do some, you know, load this C program.
[L1520] [55:09.60] And the C program is a binary somewhere.
[L1521] [55:12.48] And the OCaml interpreter then starts to
[L1522] [55:16.08] load those instructions and execute
[L1523] [55:17.84] them.
[L1524] [55:18.36] >> Okay. So actually this is the third
[L1525] [55:20.52] aspect that I didn't touch.
[L1526] [55:22.88] So so OCaml well, there's an interpreter
[L1527] [55:25.72] mode, but in general we compile. We
[L1528] [55:28.08] compile to assembly code and then
[L1529] [55:30.60] machine code.
[L1530] [55:32.08] And so
[L1531] [55:33.48] so in in in compiled mode,
[L1532] [55:36.48] what what you say is
[L1533] [55:39.00] how you put together the OCaml code and
[L1534] [55:41.56] the C code is done by the the linker,
[L1535] [55:44.08] the C linker. So so
[L1536] [55:46.76] So basically someone else is doing that
[L1537] [55:48.92] for us. And and and it's not that
[L1538] [55:51.80] different from linking together two
[L1539] [55:55.32] object files produced by C or two object
[L1540] [55:58.32] files produced by OCaml.
[L1541] [56:00.96] But you write that for for more
[L1542] [56:02.60] interpreted
[L1543] [56:04.12] languages, there's also the question of
[L1544] [56:05.68] how you load the C code.
[L1545] [56:07.88] Generally you know you use the dynamic
[L1546] [56:10.04] loading like interface dlopen for
[L1547] [56:12.56] instance in in in Unix.
[L1548] [56:17.12] So and and and then there's a little bit
[L1549] [56:19.72] of introspection. So so at at run time
[L1550] [56:22.40] the interpreter will query the C
[L1551] [56:24.08] libraries and where is the address of a
[L1552] [56:26.60] function named foo? And then it will
[L1553] [56:29.28] find the address and use that to
[L1554] [56:30.92] manufacture a call. So yeah, if you're
[L1555] [56:34.24] in an interpreted setting or
[L1556] [56:36.60] or bytecode compiled setting like
[L1557] [56:38.04] Python, it's there's this additional
[L1558] [56:40.56] level of complexity on top of it.
[L1559] [56:44.28] >> I see. I see. Okay, so if I had a mixed
[L1560] [56:48.00] OCaml C program
[L1561] [56:50.84] to my computer it's just one binary or
[L1562] [56:54.68] one one blob.
[L1563] [56:56.16] >> In in in the simplest case, yes.
[L1564] [57:00.36] There are also dynamic loading
[L1565] [57:02.20] facilities in OCaml, but I don't want to
[L1566] [57:04.16] get into that because I'm a firm
[L1567] [57:06.08] believer in static linking. I think
[L1568] [57:08.64] programs should be statically linked so
[L1569] [57:11.04] that there's no surprise when you run
[L1570] [57:13.44] them. Okay, like oh, where is this DLL
[L1571] [57:16.28] or DLL not found for instance problems.
[L1572] [57:19.36] But
[L1573] [57:21.64] of course you lose a little bit in
[L1574] [57:22.88] flexibility.
[L1575] [57:26.00] But yeah, I think the static static
[L1576] [57:28.00] linking has a lot to
[L1577] [57:31.96] is is actually quite useful in in that
[L1578] [57:34.36] it it guarantees a lot of things. It
[L1579] [57:36.08] checks a lot of things at link time that
[L1580] [57:37.84] you
[L1581] [57:38.80] don't have to check again at run time.
[L1582] [57:41.48] >> We mentioned earlier in the conversation
[L1583] [57:43.44] talking a little bit about LLM generated
[L1584] [57:45.36] code. I thought that might be
[L1585] [57:46.40] interesting to cover. Um and in one
[L1586] [57:49.80] interview you talked about the danger of
[L1587] [57:53.00] almost correct code. So, plausible code
[L1588] [57:55.96] but it's it's wrong that an LLM can
[L1589] [57:57.84] produce. And what are your thoughts on
[L1590] [58:01.00] you know how to address that kind of
[L1591] [58:02.72] problem?
[L1592] [58:04.72] >> It's it's it's a tough problem. I mean
[L1593] [58:07.00] you
[L1594] [58:08.28] um
[L1595] [58:09.36] globally I'm a little bit skeptical
[L1596] [58:11.08] about generative AI. Oh, of course they
[L1597] [58:14.16] they they
[L1598] [58:15.40] they can do amazing things that were
[L1599] [58:17.72] unthinkable like a few years ago.
[L1600] [58:20.48] But there's also
[L1601] [58:22.92] there's always some errors. Okay. It's
[L1602] [58:25.52] it's
[L1603] [58:26.36] you can't really trust
[L1604] [58:28.56] oh
[L1605] [58:29.64] what's what's being produced by by
[L1606] [58:31.60] generative AI.
[L1607] [58:33.08] And so
[L1608] [58:35.00] the the
[L1609] [58:37.64] uh
[L1610] [58:38.68] in principle humans should be there to
[L1611] [58:41.76] check the output and
[L1612] [58:44.20] and fix errors or ask the LLM to fix its
[L1613] [58:48.08] own errors
[L1614] [58:49.32] until the result is actually usable. But
[L1615] [58:52.60] of course it's very hard because well
[L1616] [58:54.48] there's a slot problem. Okay.
[L1617] [58:56.72] AI's produce so much it's so it's so
[L1618] [58:59.76] easy to produce
[L1619] [59:01.44] uh
[L1620] [59:02.00] to produce large number large quantities
[L1621] [59:04.96] of text of code or pictures or whatever
[L1622] [59:08.88] that that that in the end
[L1623] [59:10.92] there's there's there's no human
[L1624] [59:14.60] no no no human time to to check it all.
[L1625] [59:18.68] So,
[L1626] [59:20.08] recently I heard a
[L1627] [59:22.40] uh well someone working in an AI startup
[L1628] [59:24.52] who was enthusiastic about
[L1629] [59:27.24] uh
[L1630] [59:28.32] AI generated code thing that thanks to
[L1631] [59:30.28] Genady AI is a cost of programming is
[L1632] [59:33.04] dropping to zero.
[L1633] [59:35.08] But well, the cost of writing code
[L1634] [59:37.12] maybe, but
[L1635] [59:39.32] what about you know checking it,
[L1636] [59:42.24] making sure it is correct, um
[L1637] [59:45.28] that it does what we want, that
[L1638] [59:47.76] well, that cost is not zero at all.
[L1639] [59:50.12] >> Uh-huh.
[L1640] [59:50.92] >> And and for me
[L1641] [59:52.44] every new line of code is a liability.
[L1642] [59:54.96] So you you have to test it, you have to
[L1643] [59:57.76] check it, maybe you have to do formal
[L1644] [59:59.20] verification. You have to
[L1645] [01:00:02.04] evolve it, maintain it later. So so no,
[L1646] [01:00:05.84] I don't want huge amounts of code, okay?
[L1647] [01:00:07.92] I want I want
[L1648] [01:00:09.12] 50 lines of code that have been
[L1649] [01:00:11.48] thought that have been polished over the
[L1650] [01:00:13.56] years.
[L1651] [01:00:14.64] So anyway, I'm not getting that with AI.
[L1652] [01:00:18.92] And and and I think that's the problem.
[L1653] [01:00:22.52] And this idea that humans will be there
[L1654] [01:00:24.60] to check the output of Genady AI is just
[L1655] [01:00:28.00] wrong.
[L1656] [01:00:29.32] No, they they they are not available for
[L1657] [01:00:31.72] that. They
[L1658] [01:00:32.96] There's too much of it and it's
[L1659] [01:00:35.04] and it's [snorts] not it's not pleasant
[L1660] [01:00:37.72] either, okay? I mean, I don't think it's
[L1661] [01:00:39.64] a good way to to to split the work
[L1662] [01:00:41.64] between machines and and humans.
[L1663] [01:00:44.68] So anyway, so maybe there will be some
[L1664] [01:00:46.88] social
[L1665] [01:00:48.16] solution like big
[L1666] [01:00:51.01] >> [snorts]
[L1667] [01:00:51.04] >> no to AI slop movements. So we we we're
[L1668] [01:00:53.80] trying to see that in some open source
[L1669] [01:00:56.44] projects that that refuse AI generated
[L1670] [01:00:59.56] contributions because there's just too
[L1671] [01:01:01.28] many.
[L1672] [01:01:02.15] >> [snorts]
[L1673] [01:01:02.28] >> I know that well for for for OCaml and
[L1674] [01:01:05.88] especially for Coq Certified have have
[L1675] [01:01:07.56] received some uh
[L1676] [01:01:09.32] uh issues, a lot of issues that were
[L1677] [01:01:12.44] obviously generated by AI. And there was
[L1678] [01:01:15.60] maybe one good issue among 10 reports,
[L1679] [01:01:18.72] okay? And and and each report was
[L1680] [01:01:20.72] several page long and it's, you know,
[L1681] [01:01:23.48] very detailed explanations, and repro
[L1682] [01:01:26.28] case that in the end doesn't repro
[L1683] [01:01:28.24] anything or repro reproduces something
[L1684] [01:01:30.72] else. And but but it takes time to to go
[L1685] [01:01:33.44] through all those things, and and maybe
[L1686] [01:01:36.04] at some point I will say no to to AI
[L1687] [01:01:38.20] generated contributions.
[L1688] [01:01:40.52] Okay. But maybe there's also a bit of a
[L1689] [01:01:42.92] technical solution,
[L1690] [01:01:44.60] which is, as as we said earlier,
[L1691] [01:01:48.08] to have AI produce proofs,
[L1692] [01:01:50.80] so evidence that
[L1693] [01:01:53.16] its creation is correct. So, as I said,
[L1694] [01:01:55.32] this is starting to work for
[L1695] [01:01:58.04] mathematical proofs. Some generally the
[L1696] [01:02:00.60] AIs are able to produce proofs both in
[L1697] [01:02:03.40] English and in the formal language of
[L1698] [01:02:06.04] the Lean prover, for instance. And so,
[L1699] [01:02:08.68] you can get
[L1700] [01:02:11.04] a Lean to recheck the proof and get some
[L1701] [01:02:13.12] confidence. You still need to be very
[L1702] [01:02:15.08] careful about the statement,
[L1703] [01:02:19.20] because sometimes
[L1704] [01:02:21.08] AIs will change the statement or the
[L1705] [01:02:23.72] definitions to make the proof easier.
[L1706] [01:02:27.80] That happens.
[L1707] [01:02:29.92] And
[L1708] [01:02:31.52] also, you you should be careful about
[L1709] [01:02:33.92] so-called self-formalizations, where the
[L1710] [01:02:36.52] the AI also comes up with some
[L1711] [01:02:38.40] definitions and some statements
[L1712] [01:02:42.20] by parsing a PDF file or whatever, and
[L1713] [01:02:45.12] and sometimes it introduces errors at
[L1714] [01:02:46.88] that point.
[L1715] [01:02:48.28] So, anyway, there's still need need for
[L1716] [01:02:50.40] human review, but
[L1717] [01:02:52.12] on smaller quantities of of text and and
[L1718] [01:02:55.24] mathematical text.
[L1719] [01:02:58.28] And maybe one day it will also work for
[L1720] [01:03:00.44] program proof. So, when an AI generates
[L1721] [01:03:03.04] a program, it might it be able to
[L1722] [01:03:05.88] generate some Lean proof or whatever,
[L1723] [01:03:08.76] that that the program satisfies some
[L1724] [01:03:10.52] specification.
[L1725] [01:03:12.32] Um
[L1726] [01:03:14.96] So, I I think it is possible.
[L1727] [01:03:17.72] Um but now the question will be where
[L1728] [01:03:19.24] does the specification come from?
[L1729] [01:03:22.32] It's always been a big issue for formal
[L1730] [01:03:23.96] methods.
[L1731] [01:03:26.16] It's not just that verification is hard,
[L1732] [01:03:28.40] but agreeing on the spec can be
[L1733] [01:03:31.64] can be difficult, too.
[L1734] [01:03:33.52] And well, mathematicians
[L1735] [01:03:35.88] have a lot of experience, you know, in
[L1736] [01:03:38.16] in stating
[L1737] [01:03:40.16] finding a definition that they find
[L1738] [01:03:41.76] interesting and stating theorems that
[L1739] [01:03:44.80] that that
[L1740] [01:03:46.24] that they believe
[L1741] [01:03:47.80] should be true or or or that that will
[L1742] [01:03:50.16] um
[L1743] [01:03:51.04] mean something.
[L1744] [01:03:53.72] Computer programmers are less good with
[L1745] [01:03:56.56] that. And it's fairly easy to come up
[L1746] [01:03:58.92] with specifications that are
[L1747] [01:04:00.08] inconsistent for instance or impossible.
[L1748] [01:04:02.64] Uh so, remember this this average
[L1749] [01:04:04.28] function
[L1750] [01:04:05.92] where there was a a precondition of the
[L1751] [01:04:07.52] three numbers three arguments saying
[L1752] [01:04:09.16] they must not be too big.
[L1753] [01:04:11.04] But say
[L1754] [01:04:13.72] maybe you you can end up with a
[L1755] [01:04:15.60] precondition that that just cannot be
[L1756] [01:04:17.56] satisfied.
[L1757] [01:04:20.16] And and
[L1758] [01:04:22.48] and and at this point, the body of the
[L1759] [01:04:24.64] function will always be verified, okay?
[L1760] [01:04:27.08] Even if it's completely wrong because
[L1761] [01:04:28.80] because the assumption says
[L1762] [01:04:30.84] basically this function cannot be
[L1763] [01:04:32.20] called.
[L1764] [01:04:33.32] Um and and so, you get a false sense of
[L1765] [01:04:35.88] confidence.
[L1766] [01:04:37.24] Okay, you verified something, but but
[L1767] [01:04:39.76] it's actually unusable.
[L1768] [01:04:42.36] And and and that that's a fairly
[L1769] [01:04:44.44] delicate point
[L1770] [01:04:46.72] where I'm not sure LLMs are going to or
[L1771] [01:04:49.72] AI is going to help much.
[L1772] [01:04:51.96] Uh
[L1773] [01:04:52.52] but but it's a problem with formal
[L1774] [01:04:53.88] methods in general. And and some
[L1775] [01:04:56.00] possibilities include
[L1776] [01:04:58.44] uh
[L1777] [01:04:59.32] the ability to test specifications for
[L1778] [01:05:01.64] instance.
[L1779] [01:05:03.56] Um
[L1780] [01:05:04.64] so, instead of using your test suite to
[L1781] [01:05:07.20] to to see if your code works out, you
[L1782] [01:05:10.16] can also use it to see if your spec um
[L1783] [01:05:13.44] um
[L1784] [01:05:14.80] it checks out. Um
[L1785] [01:05:17.52] those kind of things, but um
[L1786] [01:05:20.20] yeah, we we're kind of moving some of
[L1787] [01:05:21.88] the difficulties from the programming
[L1788] [01:05:23.28] phase to the uh specification phase, but
[L1789] [01:05:26.40] we still have some problems.
[L1790] [01:05:30.00] Anyway, so that might be a way to to
[L1791] [01:05:32.60] deal with the um
[L1792] [01:05:34.52] uh AI-generated code and and and develop
[L1793] [01:05:37.44] some confidence in it.
[L1794] [01:05:39.60] >> You know, LLM-generated code is becoming
[L1795] [01:05:41.64] extremely popular, and I think there's a
[L1796] [01:05:43.80] lot of potential downstream consequences
[L1797] [01:05:46.64] on this on the programming language uh
[L1798] [01:05:49.68] landscape.
[L1799] [01:05:51.12] And I thought it might be interesting to
[L1800] [01:05:53.00] hear your thoughts on speculating. Like,
[L1801] [01:05:55.60] imagine 10 years from now, if you took
[L1802] [01:05:58.80] LLM-generated code and turned it up,
[L1803] [01:06:01.96] how might you think that the programming
[L1804] [01:06:05.16] language
[L1805] [01:06:06.68] landscape might change?
[L1806] [01:06:08.60] >> Yeah, a couple of years ago uh someone
[L1807] [01:06:10.92] asked me about that, and and there was
[L1808] [01:06:13.44] there was a a concern that the training
[L1809] [01:06:15.84] data would be um there wouldn't be
[L1810] [01:06:18.44] enough training data in OCaml
[L1811] [01:06:21.28] uh for for an LLM to really learn how to
[L1812] [01:06:24.00] program in OCaml.
[L1813] [01:06:25.52] And it's true that there's less OCaml
[L1814] [01:06:27.76] code in the wild than uh JavaScript
[L1815] [01:06:30.00] code, for instance.
[L1816] [01:06:31.52] Uh but apparently
[L1817] [01:06:34.44] um uh contemporary LLMs do do do well
[L1818] [01:06:38.44] with with uh the amount of uh of OCaml
[L1819] [01:06:41.32] code uh
[L1820] [01:06:43.24] they have.
[L1821] [01:06:44.80] Uh
[L1822] [01:06:45.52] maybe because there's enough, maybe
[L1823] [01:06:47.16] because learning has become a little
[L1824] [01:06:48.72] more efficient, maybe because uh well,
[L1825] [01:06:51.80] there's there's there's less OCaml code
[L1826] [01:06:53.84] than JavaScript code, but maybe the
[L1827] [01:06:55.40] OCaml code is better quality average
[L1828] [01:06:58.44] on an average. I don't know. Anyway, uh
[L1829] [01:07:01.16] maybe LLMs are getting better also to to
[L1830] [01:07:03.92] transfer knowledge from that they've
[L1831] [01:07:05.52] learned from one language to another.
[L1832] [01:07:08.08] That that could be. Um I have no idea
[L1833] [01:07:10.52] how those things work.
[L1834] [01:07:12.92] But yeah, so so the latest feedback I've
[L1835] [01:07:14.60] got about LLMs and
[L1836] [01:07:17.20] well, yeah,
[L1837] [01:07:18.36] generative AI and OCaml is that the the
[L1838] [01:07:20.96] OCaml code generated is is quite decent
[L1839] [01:07:24.48] and quite similar in quality to
[L1840] [01:07:27.64] to more popular languages.
[L1841] [01:07:30.04] And one thing that seems to help the
[L1842] [01:07:33.24] generative AI is a type system. So the
[L1843] [01:07:36.00] fact that there's some static checking
[L1844] [01:07:38.60] just of the types uh
[L1845] [01:07:41.08] uh it's already uh effective in, you
[L1846] [01:07:43.92] know, the
[L1847] [01:07:45.84] uh avoiding some some errors and maybe
[L1848] [01:07:49.36] uh encouraging the LLM to like like
[L1849] [01:07:52.12] declare types
[L1850] [01:07:54.20] uh first. Um so so give give some type
[L1851] [01:07:57.04] structure to the program.
[L1852] [01:07:59.12] All right.
[L1853] [01:08:00.04] Um
[L1854] [01:08:01.36] And now from 10 years from now,
[L1855] [01:08:04.80] it's it's it's difficult to guess. So,
[L1856] [01:08:07.24] will it be the more the more popular
[L1857] [01:08:09.16] languages of today that will be even
[L1858] [01:08:11.72] more popular because of generative AI?
[L1859] [01:08:15.28] Will it be the safer languages of today
[L1860] [01:08:18.60] that will be more popular with AI
[L1861] [01:08:20.48] because uh
[L1862] [01:08:22.72] well, because there's fewer errors in
[L1863] [01:08:24.24] the end?
[L1864] [01:08:25.28] Um I'm hoping it will be the the safer
[L1865] [01:08:27.88] languages, but uh
[L1866] [01:08:30.00] I really don't know.
[L1867] [01:08:31.72] >> I've seen in the industry, there's a few
[L1868] [01:08:33.84] cases where because it's so easy to
[L1869] [01:08:36.64] generate code, uh massive rewrites are
[L1870] [01:08:41.12] something that would have been very
[L1871] [01:08:42.96] infeasible in the past are very
[L1872] [01:08:45.52] realizable now. So, if there's an
[L1873] [01:08:48.16] existing project where they chose a
[L1874] [01:08:51.00] programming language for whatever reason
[L1875] [01:08:53.20] in the past, they could translate the
[L1876] [01:08:56.12] entire thing into another language
[L1877] [01:08:59.20] with reasonable confidence. Given that
[L1878] [01:09:01.84] kind of environment, which programming
[L1879] [01:09:04.32] languages would you expect more people
[L1880] [01:09:07.08] would switch to because they they want
[L1881] [01:09:09.64] to switch to it but they weren't able to
[L1882] [01:09:11.24] in the past but now it's cheaper so they
[L1883] [01:09:12.88] can.
[L1884] [01:09:13.88] >> Well, so today
[L1885] [01:09:15.76] it seems I've heard mostly about C and
[L1886] [01:09:19.04] C++ to Rust
[L1887] [01:09:21.16] translations
[L1888] [01:09:22.88] hoping that the generated Rust code will
[L1889] [01:09:25.28] be safer.
[L1890] [01:09:27.92] He said I've seen at least one project
[L1891] [01:09:29.80] when the generated Rust code is entirely
[L1892] [01:09:32.00] in unsafe blocks. So so it's really kind
[L1893] [01:09:34.40] of line by line translation of the C
[L1894] [01:09:36.56] code, you know, it's
[L1895] [01:09:37.96] but well,
[L1896] [01:09:39.64] but maybe it can still be used as a
[L1897] [01:09:41.08] starting point for making it safer
[L1898] [01:09:43.16] later.
[L1899] [01:09:44.32] So
[L1900] [01:09:46.36] yeah, I would say today
[L1901] [01:09:48.60] I can imagine
[L1902] [01:09:50.44] significant efforts being being done
[L1903] [01:09:52.60] with Rust as the as a target language.
[L1904] [01:09:56.00] In the functional world, I'm not quite
[L1905] [01:09:58.20] sure. Well, maybe or well
[L1906] [01:10:01.22] >> [snorts]
[L1907] [01:10:01.68] >> maybe functional language to one of
[L1908] [01:10:05.24] those proof assistants
[L1909] [01:10:07.28] like like Lean or Coq because they they
[L1910] [01:10:09.16] also have
[L1911] [01:10:11.68] programming languages functional
[L1912] [01:10:13.16] programming languages in them much more
[L1913] [01:10:15.32] restricted but much more amenable to
[L1914] [01:10:17.60] proofs. So
[L1915] [01:10:19.92] maybe for a few projects that that could
[L1916] [01:10:21.96] be interesting as again as a first step
[L1917] [01:10:24.52] towards a formal proof as we as we said
[L1918] [01:10:27.64] earlier.
[L1919] [01:10:28.80] >> When you compare industry versus
[L1920] [01:10:30.68] academia,
[L1921] [01:10:32.24] today where would you say most of the
[L1922] [01:10:34.32] innovation in programming languages
[L1923] [01:10:36.00] comes from? And also has that changed
[L1924] [01:10:38.44] over time?
[L1925] [01:10:41.44] >> Okay, well, I think the
[L1926] [01:10:44.36] most of the innovations
[L1927] [01:10:46.60] have come from industry lately.
[L1928] [01:10:49.96] And that wasn't the case in the early
[L1929] [01:10:53.04] days of computer science.
[L1930] [01:10:55.48] If you think of I mean, the the totally
[L1931] [01:10:58.24] innovative languages like like Algol,
[L1932] [01:11:02.04] Lisp,
[L1933] [01:11:03.28] uh
[L1934] [01:11:04.28] um
[L1935] [01:11:06.32] Prolog, uh Smalltalk were were developed
[L1936] [01:11:09.44] in mostly academic settings. Well,
[L1937] [01:11:11.32] Smalltalk was Xerox PARC, which was an
[L1938] [01:11:13.56] industrial research lab, but very very
[L1939] [01:11:15.64] far away from
[L1940] [01:11:17.08] uh industrial customers.
[L1941] [01:11:18.80] Uh and then there were, you know, much
[L1942] [01:11:21.24] more
[L1943] [01:11:22.08] uh practical languages and ugly uh
[L1944] [01:11:25.08] uglier languages developed typically at
[L1945] [01:11:27.48] IBM like Fortran, COBOL, PL/I, etc.
[L1946] [01:11:32.04] Um and then um
[L1947] [01:11:34.56] so so really the idea that the the the
[L1948] [01:11:36.80] nice ideas come from academia and and
[L1949] [01:11:39.84] mature there. Uh
[L1950] [01:11:42.16] And then uh well, the nice ideas from
[L1951] [01:11:44.72] academia started to to be transferred by
[L1952] [01:11:47.68] industry much much more quickly. I'm
[L1953] [01:11:50.92] thinking of well, C and especially C++
[L1954] [01:11:53.76] and then Java, which really uh took uh
[L1955] [01:11:57.84] ideas like object-orientation and uh
[L1956] [01:12:00.56] well, garbage collection, automatic
[L1957] [01:12:02.08] memory management uh in in
[L1958] [01:12:04.92] um in industry.
[L1959] [01:12:07.04] All right. Before Java, it was just, you
[L1960] [01:12:10.20] know, uh crazy academics in the ivory
[L1961] [01:12:12.80] tower that were using garbage collected
[L1962] [01:12:14.64] languages, right? It was completely
[L1963] [01:12:17.32] impossible to have that in enterprise
[L1964] [01:12:19.16] compu- computing. And Java came and 2
[L1965] [01:12:21.80] years later everyone was doing garbage
[L1966] [01:12:23.52] collection and
[L1967] [01:12:25.12] being very happy about it.
[L1968] [01:12:26.63] >> [snorts]
[L1969] [01:12:26.96] >> Uh and then there were well, Java also
[L1970] [01:12:29.32] popularized type safety um
[L1971] [01:12:32.04] bytecode verification. Well, some some
[L1972] [01:12:34.20] pretty advanced techniques of the '90s.
[L1973] [01:12:37.88] And if you look at further developments,
[L1974] [01:12:40.00] uh
[L1975] [01:12:40.96] I don't know, Swift for instance
[L1976] [01:12:42.52] popularized the idea of algebraic data
[L1977] [01:12:44.48] types and pattern matching. Uh and then
[L1978] [01:12:47.36] Rust uh and
[L1979] [01:12:49.60] uh Uh, well, Rust is even more
[L1980] [01:12:52.00] spectacular, I would say, because uh,
[L1981] [01:12:54.68] well, algebraic data types, garbage
[L1982] [01:12:56.20] collections, etc., those were already
[L1983] [01:12:57.96] present in in academic languages like,
[L1984] [01:13:00.44] well, Camel, for instance. But, uh,
[L1985] [01:13:03.72] Rust really took very recent research
[L1986] [01:13:05.92] results of the 2000s and safe low-level
[L1987] [01:13:08.68] programming that were basically never
[L1988] [01:13:10.96] implemented in any language, and managed
[L1989] [01:13:14.20] to do a a consistent whole,
[L1990] [01:13:16.52] uh, from that.
[L1991] [01:13:17.96] And so, I'm I'm really admiring it.
[L1992] [01:13:20.24] And I have the impression that
[L1993] [01:13:22.92] well, uh,
[L1994] [01:13:24.40] uh, I would have loved if if Rust came
[L1995] [01:13:27.04] out of academia, uh, but I'm not sure it
[L1996] [01:13:29.84] would have been possible, because it's
[L1997] [01:13:31.24] also a huge effort, and you really need
[L1998] [01:13:34.12] uh,
[L1999] [01:13:35.40] the backing of of a big, uh, company.
[L2000] [01:13:38.40] But, still, I'm not I'm not sad because,
[L2001] [01:13:41.12] uh,
[L2002] [01:13:41.92] I think it's also a very good sign that
[L2003] [01:13:43.72] industry is interested in new
[L2004] [01:13:45.80] programming languages.
[L2005] [01:13:47.52] You know, at at some point,
[L2006] [01:13:50.00] in in the '90s, well, pretty much when I
[L2007] [01:13:51.88] was hired uh, at INRIA on a research
[L2008] [01:13:54.28] position, uh,
[L2009] [01:13:56.96] uh, when I was hired as someone who had
[L2010] [01:14:00.04] developed uh,
[L2011] [01:14:01.60] first versions of OCaml, well,
[L2012] [01:14:03.64] predecessor of OCaml, and who was
[L2013] [01:14:05.16] working on type systems for programming
[L2014] [01:14:06.72] languages, and so on.
[L2015] [01:14:08.52] Uh, but then some people told me, but
[L2016] [01:14:10.48] there's no future in programming
[L2017] [01:14:11.68] language research, right? Industry has
[L2018] [01:14:13.72] decided it will be C++ forever.
[L2019] [01:14:16.88] So, deal with it. Uh, maybe maybe you
[L2020] [01:14:19.40] could do software engineering, and not
[L2021] [01:14:21.04] not not PL research.
[L2022] [01:14:23.68] Uh,
[L2023] [01:14:25.16] and then Java came a few years later,
[L2024] [01:14:27.28] and and showing that no, uh,
[L2025] [01:14:30.48] industry hasn't [clears throat] decided
[L2026] [01:14:32.36] on a functional on a on a particular
[L2027] [01:14:34.52] programming language. Industry is still
[L2028] [01:14:36.20] in interested in new programming
[L2029] [01:14:37.88] languages. Industry still thinks that a
[L2030] [01:14:41.00] new programming language can be part of
[L2031] [01:14:42.64] the solution to to software problems.
[L2032] [01:14:45.32] And and I find it extremely encouraging.
[L2033] [01:14:47.96] We are not stuck with with bad languages
[L2034] [01:14:50.88] from the past. Well, there's a lot of
[L2035] [01:14:52.72] legacy code, of course, but but they're
[L2036] [01:14:54.60] still
[L2037] [01:14:55.68] uh um
[L2038] [01:14:57.24] real interest for for for better
[L2039] [01:14:59.28] languages, and I think this will
[L2040] [01:15:01.00] continue, and I think it's good for for
[L2041] [01:15:03.88] the computing field.
[L2042] [01:15:06.12] >> In 2018, there was a interview that you
[L2043] [01:15:08.48] did, and they asked you what are the
[L2044] [01:15:10.76] most interesting and important problems
[L2045] [01:15:13.00] to focus on in the coming years.
[L2046] [01:15:15.16] And you called out the difficulty of
[L2047] [01:15:17.76] programming, you know, GPUs, cuz they
[L2048] [01:15:20.24] were using dialects of C, shoddy tools,
[L2049] [01:15:23.16] and also the challenges in verifying
[L2050] [01:15:26.00] machine learned code, basically. Um and
[L2051] [01:15:30.52] that sounds pretty relevant today, but
[L2052] [01:15:33.16] what would you say your answer is today?
[L2053] [01:15:35.64] >> So, yeah, I think well, for for the um
[L2054] [01:15:38.68] um the question of how we program
[L2055] [01:15:40.68] massively parallel hardware,
[L2056] [01:15:43.32] I think we we've made a little bit of
[L2057] [01:15:44.88] progress recently with things like the
[L2058] [01:15:47.64] uh MLIR initiative um
[L2059] [01:15:51.08] on the on LLVM, or some domain-specific
[L2060] [01:15:54.80] languages uh like Halide, which are
[L2061] [01:15:57.00] pretty good. You know, those tensor uh
[L2062] [01:15:59.24] domain-specific languages for tensor
[L2063] [01:16:00.80] computations are getting a little
[L2064] [01:16:02.24] better.
[L2065] [01:16:03.44] Um but still, I find it a little bit
[L2066] [01:16:05.68] frustrating that I cannot do uh I don't
[L2067] [01:16:07.96] know, theorem proving on a GPU. Uh I
[L2068] [01:16:10.48] have absolutely no idea how to go about
[L2069] [01:16:12.36] that.
[L2070] [01:16:13.68] Uh and in part by by by lack of uh an
[L2071] [01:16:17.36] appropriate language, okay? Uh
[L2072] [01:16:19.60] uh
[L2073] [01:16:20.96] So, I'm I'm not ready to program the GPU
[L2074] [01:16:24.08] pipelines
[L2075] [01:16:25.52] at the very low level myself, so
[L2076] [01:16:28.56] So, and and I think it's more general. I
[L2077] [01:16:30.64] think we're we're not using uh all these
[L2078] [01:16:34.00] GPU and other highly parallel hardware
[L2079] [01:16:36.52] as much as we could. Yeah, so verifying
[L2080] [01:16:39.00] applications that have been learned or
[L2081] [01:16:42.56] generated
[L2082] [01:16:44.24] or generated by AI also and it's still a
[L2083] [01:16:47.68] pretty
[L2084] [01:16:48.84] hot issue.
[L2085] [01:16:50.16] Back in 2018 I was more thinking of of
[L2086] [01:16:53.04] verifying simple neural networks like
[L2087] [01:16:56.16] those used for I don't know computer
[L2088] [01:16:58.48] vision
[L2089] [01:16:59.80] or self-driving cars or or or some
[L2090] [01:17:02.92] numerical computations like you know
[L2091] [01:17:05.08] weather prediction and so on. So so
[L2092] [01:17:07.24] specialized LLMs but you still want some
[L2093] [01:17:09.76] guarantees about
[L2094] [01:17:11.40] what they produce that they cannot
[L2095] [01:17:13.88] produce completely inconsistent outputs
[L2096] [01:17:15.72] for instance. There were some some
[L2097] [01:17:17.72] attempts in in in the last years at
[L2098] [01:17:20.80] using static analysis tools and
[L2099] [01:17:23.76] basically program verification tools
[L2100] [01:17:26.24] applied to LLMs
[L2101] [01:17:27.88] but well it it it doesn't scale.
[L2102] [01:17:32.48] LLMs are big.
[L2103] [01:17:34.40] Sorry.
[L2104] [01:17:35.80] Neural networks are big.
[L2105] [01:17:37.56] And for LLMs there's also
[L2106] [01:17:40.12] a distinct lack of specification. Okay.
[L2107] [01:17:44.12] You don't really know what's a good
[L2108] [01:17:46.68] answer from an LLM.
[L2109] [01:17:48.76] Well you know it when you see it but you
[L2110] [01:17:50.84] cannot write a mathematical
[L2111] [01:17:52.08] specification of it. So so that part is
[L2112] [01:17:54.64] probably over. What I would say are the
[L2113] [01:17:57.76] big problems for today yeah probably
[L2114] [01:18:00.40] maintaining software quality despite
[L2115] [01:18:02.96] AI's love despite a lot of pressure to
[L2116] [01:18:06.60] throw away traditional software
[L2117] [01:18:09.04] development techniques using
[L2118] [01:18:12.24] LLMs as an AI as much as we can to do
[L2119] [01:18:16.32] mechanized proofs so proofs that can be
[L2120] [01:18:18.52] checked by machines.
[L2121] [01:18:20.32] Maybe this will be the the decade of
[L2122] [01:18:22.68] formal verification of software. We've
[L2123] [01:18:24.72] been waiting for that for 50 years so
[L2124] [01:18:27.92] maybe it will it will finally take off.
[L2125] [01:18:31.00] >> What's your top book recommendation for
[L2126] [01:18:33.20] software engineers and why?
[L2127] [01:18:36.36] >> Well this this is an old one, the
[L2128] [01:18:38.24] Programming Pearls by Jon
[L2129] [01:18:40.36] I think I read it when I was a PhD
[L2130] [01:18:41.84] student, but I think it's it's nice as
[L2131] [01:18:45.36] showing how very talented programmers
[L2132] [01:18:48.80] work, [snorts] how they think about
[L2133] [01:18:51.12] their programs. So, it's it's it's it's
[L2134] [01:18:53.32] a combination of choosing the right
[L2135] [01:18:54.92] algorithms,
[L2136] [01:18:56.56] expressing them clearly,
[L2137] [01:18:59.00] uh knowing when to stop,
[L2138] [01:19:01.12] when when to use a simple algorithm,
[L2139] [01:19:04.04] where where
[L2140] [01:19:06.36] when a more complicated one is not
[L2141] [01:19:08.20] needed,
[L2142] [01:19:09.20] uh having a sense of elegance in in the
[L2143] [01:19:12.08] code you write, um
[L2144] [01:19:14.96] uh having a feeling for where the
[L2145] [01:19:16.96] problem is when when the the code
[L2146] [01:19:18.92] misbehave. So, all all that kind of
[L2147] [01:19:21.00] things that are hard to communicate, and
[L2148] [01:19:22.76] I think those those pearls
[L2149] [01:19:24.92] that are very easy to read, uh
[L2150] [01:19:27.48] and and and don't use any complicated
[L2151] [01:19:30.00] data structures, don't use any
[L2152] [01:19:31.36] complicated language. I mean, it it's
[L2153] [01:19:33.56] it's kind of timeless, you know.
[L2154] [01:19:35.56] Um
[L2155] [01:19:37.00] I think those pearls are are good
[L2156] [01:19:38.72] illustration of that.
[L2157] [01:19:41.16] Uh so, if you haven't read it, it's it's
[L2158] [01:19:43.00] a classic, but
[L2159] [01:19:45.04] I think it's a nice reading.
[L2160] [01:19:46.92] Nice read. Uh the second one is a little
[L2161] [01:19:49.44] more controversial, I guess.
[L2162] [01:19:51.52] So, in the How to Design Program, which
[L2163] [01:19:54.56] is a fairly ambitious title as well.
[L2164] [01:19:56.84] And this comes from the Scheme
[L2165] [01:19:58.08] community, okay, Abelson and Findler,
[L2166] [01:20:01.44] Flatt, and Krishnamurthi.
[L2167] [01:20:03.44] Um and and those people have developed
[L2168] [01:20:06.60] uh well, the Scheme community is famous
[L2169] [01:20:08.28] for having developed uh pedagogical
[L2170] [01:20:10.12] resources that are
[L2171] [01:20:11.72] I mean, ways to teach programming uh
[L2172] [01:20:16.08] that that go beyond teaching functional
[L2173] [01:20:18.04] programming, basically.
[L2174] [01:20:20.68] And so, so there was the
[L2175] [01:20:23.08] the MIT [clears throat]
[L2176] [01:20:24.00] Course Structure and Interpretation of
[L2177] [01:20:25.56] Computer Programs, which was quite
[L2178] [01:20:26.92] famous, and this is kind of a more
[L2179] [01:20:28.44] modern
[L2180] [01:20:30.60] twist on on on similar ideas.
[L2181] [01:20:33.64] And and and
[L2182] [01:20:35.76] I find this book interesting because
[L2183] [01:20:38.24] well, it it it really teaches you the
[L2184] [01:20:40.96] way of functional programming
[L2185] [01:20:43.52] a way to functional programming. It can
[L2186] [01:20:45.68] be very irritating sometimes, very
[L2187] [01:20:47.72] opinionated, very
[L2188] [01:20:49.76] um almost mystical sometimes, but
[L2189] [01:20:53.44] but it's also
[L2190] [01:20:55.36] another
[L2191] [01:20:56.56] great attempt at at trying to
[L2192] [01:20:58.32] communicate
[L2193] [01:21:00.24] how experienced programmers go about uh
[L2194] [01:21:03.64] designing a program
[L2195] [01:21:06.24] uh
[L2196] [01:21:07.24] even before writing the first line.
[L2197] [01:21:09.64] Okay. And and then how
[L2198] [01:21:11.76] given a language like Scheme, which is
[L2199] [01:21:13.64] pretty flexible, how the code kind of
[L2200] [01:21:16.48] follows uh naturally.
[L2201] [01:21:19.68] >> You know, knowing what you know now, if
[L2202] [01:21:21.12] you could go back to when you just
[L2203] [01:21:23.32] started your career and give yourself
[L2204] [01:21:25.12] some advice, what would you say?
[L2205] [01:21:27.48] >> Sometimes I got that uh maybe I
[L2206] [01:21:31.16] specialized a little too early in in in
[L2207] [01:21:34.36] um
[L2208] [01:21:35.44] in programming language research.
[L2209] [01:21:37.72] Uh maybe
[L2210] [01:21:39.12] well, there there are some topics that
[L2211] [01:21:40.72] are I didn't learn
[L2212] [01:21:44.00] because I didn't feel like it. And and
[L2213] [01:21:46.80] that I had to relearn later or I still
[L2214] [01:21:50.68] have to learn now that I'm almost 60 and
[L2215] [01:21:55.56] maybe not not as um
[L2216] [01:21:57.72] uh
[L2217] [01:21:59.56] not as quick uh
[L2218] [01:22:01.68] as I was back in the day. So, yeah,
[L2219] [01:22:03.28] maybe I I did specialize a little too
[L2220] [01:22:06.16] early. And so, I would encourage
[L2221] [01:22:07.96] everyone to get a everyone who's serious
[L2222] [01:22:10.76] about working in computing uh to get a
[L2223] [01:22:15.12] fairly diverse computer science
[L2224] [01:22:17.28] background. Even even for topics that
[L2225] [01:22:19.44] look super theoretical and are not very
[L2226] [01:22:22.56] uh relevant to
[L2227] [01:22:24.52] uh to everyday uh
[L2228] [01:22:27.36] jobs.
[L2229] [01:22:28.48] Uh well, we mentioned the
[L2230] [01:22:30.20] computability for instance things like
[L2231] [01:22:31.96] the halting problem and so on. You're
[L2232] [01:22:33.44] not going to run into that very often,
[L2233] [01:22:36.08] but it still
[L2234] [01:22:37.84] gives
[L2235] [01:22:38.96] interesting perspectives, I think.
[L2236] [01:22:42.80] And then it also helps understanding new
[L2237] [01:22:44.76] problems.
[L2238] [01:22:46.36] Like
[L2239] [01:22:48.12] with quantum computing.
[L2240] [01:22:50.40] What can you do with a quantum computer
[L2241] [01:22:52.12] that you cannot do with a normal
[L2242] [01:22:53.64] computer?
[L2243] [01:22:55.56] And and and it's it's time to to revisit
[L2244] [01:22:58.84] all of the classic complexity theory I
[L2245] [01:23:01.12] learned earlier and when when I was
[L2246] [01:23:04.80] young. And and so yeah, I think I think
[L2247] [01:23:07.92] it's good to have those this kind of
[L2248] [01:23:09.60] background even if
[L2249] [01:23:12.40] it's not obvious you will be using it
[L2250] [01:23:14.56] everyday.
[L2251] [01:23:15.80] And and sometimes I wish I had taken
[L2252] [01:23:18.24] time to accumulate a little more of this
[L2253] [01:23:20.80] background
[L2254] [01:23:22.00] before specializing in in programming
[L2255] [01:23:24.36] languages.
[L2256] [01:23:25.68] >> Awesome. Well, thank you so much for
[L2257] [01:23:26.96] your time Professor Liwei. I appreciate
[L2258] [01:23:28.68] it.
[L2259] [01:23:28.84] >> Thank you Aaron. That was nice.
[L2260] [01:23:31.40] >> Hey, thank you for watching this
[L2261] [01:23:32.36] podcast. If you liked it and you want to
[L2262] [01:23:34.04] see the show grow, please support with a
[L2263] [01:23:36.20] comment or a like.
[L2264] [01:23:38.24] Also, if you have any recommendations
[L2265] [01:23:40.04] for people you want me to bring on,
[L2266] [01:23:42.04] please drop a comment. Guests like
[L2267] [01:23:44.20] Barbara Liskov, Mike Stonebraker, Mark
[L2268] [01:23:46.92] Brooker, these were all people that I
[L2269] [01:23:48.96] brought on because someone left a
[L2270] [01:23:50.80] comment. On another note, aside from the
[L2271] [01:23:53.04] podcast, I'm working on building the
[L2272] [01:23:54.88] ergonomic keyboard that I wish existed.
[L2273] [01:23:57.36] Here's a glance at the prototype. It's a
[L2274] [01:23:59.24] split keyboard, so there's two sides.
[L2275] [01:24:02.12] Um this is in the case. But yeah, we
[L2276] [01:24:03.72] launched on Kickstarter and we hit our
[L2277] [01:24:05.52] goal within 8 hours of launching. I
[L2278] [01:24:07.60] really appreciate it if you were one of
[L2279] [01:24:09.00] the people who grabbed one of the early
[L2280] [01:24:10.72] units. Um we're now working on the long
[L2281] [01:24:13.08] journey of building the tooling now. And
[L2282] [01:24:15.20] so if you still want to pick one up,
[L2283] [01:24:16.88] I've left the late pledges open on
[L2284] [01:24:18.88] Kickstarter, so you can grab one there.
[L2285] [01:24:21.12] I'll put a link in the description.
[L2286] [01:24:23.08] Thank you again for watching the podcast
[L2287] [01:24:25.44] and I'll see you in the next episode.
