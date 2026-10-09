Chunk 1; segments 1–352. 

# Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg

Source ID: source-fd3381490fc526e5
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_TypeScript_10x_Faster_Typescript,_Why_AI_Won't_Replace_SWEs_Anders_Hejlsberg_en.txt
Video: https://www.youtube.com/watch?v=cywK3XYYJ2o

[L10] [00:00.32] Don't let people tell you that it can't
[L11] [00:02.16] be done. [music] When they tell you it
[L12] [00:03.68] can't be done, it's because they can't
[L13] [00:05.28] do it.
[L14] [00:06.16] >> This is Anders Hilesberg, the creator of
[L15] [00:08.40] Typescript and C. And we talked about
[L16] [00:10.80] how Typescript recently became [music]
[L17] [00:12.88] 10 times faster through a native
[L18] [00:14.80] rewrite.
[L19] [00:15.60] >> Couldn't we like fix JavaScript? [music]
[L20] [00:17.20] Wouldn't that be better? [laughter]
[L21] [00:19.04] Do you know what I mean?
[L22] [00:20.16] >> If you think about Rust, what didn't it
[L23] [00:22.88] have that if it had it, you would have
[L24] [00:24.88] picked it?
[L25] [00:25.36] >> I mean, I think there are two things.
[L26] [00:26.86] [music] Um, if you're going to hand AI
[L27] [00:29.52] the keys, I mean, then all bets are off,
[L28] [00:32.08] right?
[L29] [00:33.04] >> Why is there such a big difference
[L30] [00:34.72] between this opinion and what I see from
[L31] [00:38.88] maybe people who work at Anthropic?
[L32] [00:40.96] People love these like take it all the
[L33] [00:43.36] way to 100%. [music] Right? And that's
[L34] [00:45.52] where I get off the bus.
[L35] [00:47.36] >> Here's the full episode.
[L36] [00:51.76] The big thing that we're going to talk
[L37] [00:53.12] about here is obviously TypeScript 7
[L38] [00:55.76] with the native rewrite. And the first
[L39] [00:58.24] thing that I think of when I see this
[L40] [00:59.76] was I didn't even realize that the
[L41] [01:02.16] compiler was written in JavaScript to
[L42] [01:03.84] begin with because I don't usually think
[L43] [01:05.60] of compilers being written in you know
[L44] [01:08.00] highle dynamic languages.
[L45] [01:10.08] >> Yeah. No.
[L46] [01:11.60] >> So why was Typescript written originally
[L47] [01:14.88] the compiler written in JavaScript?
[L48] [01:17.92] >> No, it's a good question. Uh, and
[L49] [01:20.32] honestly, if you had told me like before
[L50] [01:23.04] the TypeScript project started that
[L51] [01:24.48] Anders you're going to be writing
[L52] [01:25.60] compilers in JavaScript, I'm like, "No,
[L53] [01:27.84] no, I'm not." But I mean it it it you
[L54] [01:31.36] know the original prototypes for for
[L55] [01:34.00] TypeScript um the Strata project as it
[L56] [01:36.64] was called in the in the very early days
[L57] [01:39.04] was actually written in C because it was
[L58] [01:42.56] like an adapt adaptation of the the
[L59] [01:45.44] parser the JavaScript parser that we had
[L60] [01:47.60] in IE and whatever and and then we moved
[L61] [01:50.48] to to JavaScript but we wrote it sort of
[L62] [01:52.64] C style. Um but why did why did we go
[L63] [01:56.40] with JavaScript? Well, I mean, if you
[L64] [01:59.60] can self-host in the ecosystem that you
[L65] [02:03.52] want to be a part of, then that is just
[L66] [02:05.84] dramatically better than putting
[L67] [02:07.44] yourself outside the ecosystem and
[L68] [02:09.36] trying to target that ecosystem. Do you
[L69] [02:11.20] know what I mean? Because by writing it
[L70] [02:13.68] in Typescript, we were also
[L71] [02:17.12] daily users of Typescript and daily
[L72] [02:19.12] users of the tooling that we were
[L73] [02:20.80] building. And whenever something didn't
[L74] [02:22.48] work right, we knew it immediately. And
[L75] [02:24.64] whenever something didn't perform right,
[L76] [02:26.40] we knew it, you know. And so so in the
[L77] [02:29.44] early in the early years, it was it was
[L78] [02:31.92] a huge uh boon I think. And then of
[L79] [02:35.68] course
[L80] [02:37.28] JavaScript runs everywhere, right? And
[L81] [02:38.88] that meant automatically our compiler
[L82] [02:40.72] could run on every platform anywhere
[L83] [02:42.56] even in the browser right uh had we gone
[L84] [02:45.44] with a native code solution at that time
[L85] [02:47.92] it wouldn't have been possible to run it
[L86] [02:49.36] in the browser. Now we have web assembly
[L87] [02:51.20] or wom you know but that didn't exist at
[L88] [02:54.00] the time right um so so it was it was a
[L89] [02:58.00] meaningful choice uh and honestly
[L90] [03:02.00] at that time also people didn't really
[L91] [03:04.80] realize how fast JavaScript had gotten I
[L92] [03:08.00] mean it used to be very slow and then
[L93] [03:10.64] Google did all of their excellent work
[L94] [03:12.48] with V8 and got it to within two or 3x
[L95] [03:16.08] of of native code which is pretty darn
[L96] [03:18.48] impressive. Um, and it was like full
[L97] [03:22.24] well possible to write compilers in in
[L98] [03:25.36] JavaScript. Um, and you could even get
[L99] [03:28.56] them performant. Uh, because often
[L100] [03:31.28] it's the algorithms that determine how
[L101] [03:33.12] performant you are. It isn't necessarily
[L102] [03:34.80] the runtime environment, right? I mean,
[L103] [03:36.48] it's a combo, but but yeah.
[L104] [03:38.88] >> Is there anything unique about the
[L105] [03:40.88] TypeScript compiler? like you know I
[L106] [03:43.12] think of a compiler I think of clang or
[L107] [03:46.00] or you know one of those ones that is
[L108] [03:48.48] used for maybe C, C++ or those static
[L109] [03:51.44] languages. What's unique about the
[L110] [03:53.76] TypeScript compiler when it was written
[L111] [03:55.76] in JavaScript compared to these native
[L112] [03:59.04] uh compilers?
[L113] [04:00.80] >> I think there are a couple of things
[L114] [04:02.32] that are pretty unique about
[L115] [04:04.80] TypeScript's compiler. First of all, it
[L116] [04:07.20] doesn't target machine code. targets
[L117] [04:09.44] JavaScript [laughter]
[L118] [04:11.04] and and some people call that a
[L119] [04:12.64] transpiler and in a sense you know the
[L120] [04:15.36] the compilation phase is mostly about
[L121] [04:17.84] removing the type annotations and
[L122] [04:19.60] turning your TypeScript back into
[L123] [04:21.44] JavaScript. Right now in the early days
[L124] [04:24.16] also an important part of of the
[L125] [04:27.52] compilation process was to downlevel
[L126] [04:29.92] your JavaScript meaning
[L127] [04:32.80] all of the runtime environments at the
[L128] [04:34.56] time were not evergreen. uh and
[L129] [04:36.72] sometimes people were lagging like
[L130] [04:38.64] multiple years behind on which level of
[L131] [04:41.20] the standard was implemented and for
[L132] [04:43.36] example when classes got standardized
[L133] [04:46.08] most JavaScript runtimes didn't
[L134] [04:47.68] implement classes but it turns out that
[L135] [04:49.84] you can downlevel to constructor
[L136] [04:51.84] functions and and trans transform the
[L137] [04:54.96] code and so part of what we did was this
[L138] [04:58.48] transformation down level transpiling of
[L139] [05:01.28] the code but then of course the type
[L140] [05:03.60] checking uh is is the big thing that we
[L141] [05:05.68] loop and the type checker in in
[L142] [05:09.12] Typescript is also quite unlike any
[L143] [05:11.52] other type checker uh in other
[L144] [05:14.24] compilers. Typically type checkers exist
[L145] [05:17.52] in compilers to guide the code generator
[L146] [05:21.52] um because you want to know are we
[L147] [05:23.04] dealing with a float or an in or a
[L148] [05:24.48] string here so we can generate you know
[L149] [05:26.32] the correct machine instructions for
[L150] [05:28.16] that data type etc etc. That's not the
[L151] [05:31.52] case in in Typescript. In fact, since we
[L152] [05:34.56] erased the types, the types have no
[L153] [05:36.48] impact whatsoever on the runtime
[L154] [05:38.80] behavior of the code. They purely exist
[L155] [05:41.68] for for tooling sake and for the
[L156] [05:45.12] developer sake and to guide things like
[L157] [05:48.08] statement completion and refactoring and
[L158] [05:50.48] code navigation, which is a whole
[L159] [05:52.88] different thing. Um, and also they don't
[L160] [05:56.40] necessarily have to be there. Uh, and so
[L161] [05:59.12] Typescript has a gradual type system.
[L162] [06:01.04] you can sort of have half of your code
[L163] [06:02.64] have types and the other half is just
[L164] [06:04.48] any um that we don't check. Now very few
[L165] [06:09.12] languages have anything like that. So,
[L166] [06:13.04] so it's very it's a very different
[L167] [06:14.56] compiler in in in that sense, you know,
[L168] [06:16.80] and a very different language in in that
[L169] [06:18.56] sense. Um, that actually made it
[L170] [06:20.64] fascinating to work on because we were
[L171] [06:22.16] solving problems that no one had solved
[L172] [06:24.24] before, you know.
[L173] [06:25.76] >> I know a lot of compilers, you know,
[L174] [06:27.44] they take the the higher level code and
[L175] [06:29.44] they typically apply optimizations as
[L176] [06:31.60] well. Maybe, you know, they unroll loops
[L177] [06:34.24] or they get rid of duplicate
[L178] [06:36.40] instructions, simplify things. Is
[L179] [06:38.48] anything like that happen in the
[L180] [06:40.48] TypeScript to Java compilation process?
[L181] [06:44.24] >> Very little. Um, like I said, when we do
[L182] [06:47.20] the down leveling, there there's some
[L183] [06:50.16] transformations that that that go on
[L184] [06:52.00] that are that are complex, but it is
[L185] [06:55.20] less and less the thing that's important
[L186] [06:57.20] about Typescript. And in fact, a lot of
[L187] [06:59.60] people use TypeScript only for the type
[L188] [07:01.84] checker. uh and then they use some
[L189] [07:05.12] bundler like ESB build or SWC or
[L190] [07:08.00] whatever to package their app, erase the
[L191] [07:10.72] types, do whatever needs to be done in
[L192] [07:13.20] order to make it runnable in in in the
[L193] [07:15.12] browser. And so we're not really there
[L194] [07:18.80] to optimize your your code for runtime.
[L195] [07:21.60] We're there to make you more productive
[L196] [07:23.84] as a developer or make AI more
[L197] [07:26.08] productive as a as a developer.
[L198] [07:29.44] So with the the native rewrite of this
[L199] [07:32.48] originally fully JavaScript compiler,
[L200] [07:35.68] what was the problem you were trying to
[L201] [07:37.36] solve with the rewrite and why did you
[L202] [07:40.24] end up write rewriting it in native
[L203] [07:42.24] code?
[L204] [07:43.12] >> Well, I mean the the problem we were
[L205] [07:44.88] trying to solve it's real simple
[L206] [07:46.48] performance and scalability. JavaScript
[L207] [07:48.56] was never really optimized for compute
[L208] [07:52.08] inensive workloads like compilers,
[L209] [07:54.40] right? JavaScript is more about creating
[L210] [07:57.28] UI that runs in a browser. Was
[L211] [07:59.52] originally intended for just like maybe
[L212] [08:02.00] a 100 lines of code, but now of course
[L213] [08:03.84] it's gotten to be a lot more. Um, but
[L214] [08:06.96] it's not it's not a place that that you
[L215] [08:09.76] would optimize for um for the kind of
[L216] [08:13.76] workload that that we are. So in
[L217] [08:16.80] JavaScript, first of all, you pay a 2 to
[L218] [08:19.52] 3x perf penalty compared to native code.
[L219] [08:22.40] I mean it depends on on the workload you
[L220] [08:24.32] know but that's but if if you're doing
[L221] [08:26.48] compute that's about where it's at. Um
[L222] [08:30.16] and then secondly in JavaScript there
[L223] [08:32.24] are a lot of restrictions around use of
[L224] [08:34.96] concurrency. Uh JavaScript was always
[L225] [08:38.40] engineered in fact to be a single
[L226] [08:40.24] threaded language. That's why we have
[L227] [08:41.76] callbacks and async and and and
[L228] [08:43.84] whatever. It's because you can't spin up
[L229] [08:45.60] threads. Um, and that's a good thing
[L230] [08:49.44] mostly because concurrency in a language
[L231] [08:52.64] with mutable data is very very hard
[L232] [08:55.44] because you can have races and deadlocks
[L233] [08:57.28] and all of this good stuff, right?
[L234] [08:58.88] That's why functional programming
[L235] [09:01.04] languages are easier with concurrency
[L236] [09:03.52] because all the data is immutable and
[L237] [09:05.28] it's much easier to reason about. Um
[L238] [09:09.28] so JavaScript doesn't give you access to
[L239] [09:12.48] concurrency other than web workers and
[L240] [09:15.60] but web workers can't share data between
[L241] [09:18.40] each other other than by remoting it. So
[L242] [09:20.56] you can you can have one web worker
[L243] [09:22.56] compute some something, but if it wants
[L244] [09:24.24] to give it to some other web worker, it
[L245] [09:26.64] has to turn it into JSON or it can't
[L246] [09:29.04] just hand it objects. And that means you
[L247] [09:32.48] can't have one worker compute some data
[L248] [09:36.16] structure and then have someone else use
[L249] [09:38.32] it. In other words, you can't have
[L250] [09:40.24] shared memory concurrency. And really
[L251] [09:42.72] that's what we wanted in order to gain
[L252] [09:46.24] all of the perf that we were leaving on
[L253] [09:48.32] the table by not utilizing multi-core
[L254] [09:50.64] CPUs that everyone has today, right?
[L255] [09:53.28] Because Moors law has stopped giving us
[L256] [09:56.40] faster CPUs. It's giving us more CPUs
[L257] [09:59.20] and we got to like find ways to use them
[L258] [10:01.12] in our in our compute intensive
[L259] [10:02.72] workloads or else we're leaving money on
[L260] [10:04.32] the table. And so we were leaving money
[L261] [10:05.84] on the table in multiple ways, right?
[L262] [10:08.56] And so native code and that was why we
[L263] [10:11.44] we looked for a language that
[L264] [10:15.20] would get us out of both of those binds.
[L265] [10:17.44] It had to be native and it had to have
[L266] [10:19.28] access to shared memory concurrency.
[L267] [10:21.68] >> I saw for the language choice you went
[L268] [10:23.68] with Go. And when I think of all the
[L269] [10:26.32] systems languages, the ones that are
[L270] [10:28.00] often hot or maybe you know Rust or
[L271] [10:31.04] Zigg, why did you choose Go for the
[L272] [10:34.16] native rewrite? I think the decision
[L273] [10:36.48] process was actually pretty structured.
[L274] [10:39.68] You know, the first decision we made was
[L275] [10:43.04] we're not going to rewrite. We're going
[L276] [10:44.72] to port because only by porting can we
[L277] [10:48.16] preserve the semantics and the
[L278] [10:49.84] algorithms and the exact behavior of our
[L279] [10:52.96] existing compiler which everyone depends
[L280] [10:55.04] on for backwards compatibility. Now we
[L281] [10:57.52] could have we could have cleaned the
[L282] [10:59.60] slate and started completely from
[L283] [11:01.12] scratch but we would have come we would
[L284] [11:02.88] have come up with a different language
[L285] [11:04.16] in the sense that it would give you
[L286] [11:06.16] different errors or behave differently
[L287] [11:07.92] in certain situations where it has to
[L288] [11:09.92] make choices between multiple
[L289] [11:12.72] possibilities and and what have you.
[L290] [11:14.72] Right? So we wanted to port and that
[L291] [11:17.84] meant our code makes certain assumptions
[L292] [11:21.12] like our code for example assumes the
[L293] [11:23.04] existence of garbage collection. It
[L294] [11:26.08] assumes the existence of first class um
[L295] [11:31.04] uh treatment of functions. You know, you
[L296] [11:33.04] can have functions within functions and
[L297] [11:34.48] you can close over over out of state and
[L298] [11:36.88] so forth. Um and as we evaluated all of
[L299] [11:40.56] these,
[L300] [11:42.08] Go was was the one that checked the most
[L301] [11:44.16] boxes. You know, it gives us it gives us
[L302] [11:48.56] very robust and mature native code
[L303] [11:51.20] generation on all major platforms. it
[L304] [11:54.32] has garbage collection and it has access
[L305] [11:58.08] excellent access to shared memory
[L306] [11:59.92] concurrency. Um, and those were like the
[L307] [12:02.40] high order bits that we wanted to check
[L308] [12:04.24] and every other language had something
[L309] [12:08.72] that kind of worked against those
[L310] [12:10.24] objectives. So for this particular
[L311] [12:12.00] workload, Go was the right was the right
[L312] [12:13.84] choice for us and it's worked out well.
[L313] [12:16.32] >> If you think about Rusk, what didn't it
[L314] [12:19.60] have that if it had it, you would have
[L315] [12:21.92] picked it? I mean I think there are
[L316] [12:23.28] there are there are two things um it
[L317] [12:26.08] doesn't have uh garbage collection
[L318] [12:29.60] it's done manually you know uh well or
[L319] [12:33.12] it's done through the borrow checker but
[L320] [12:35.04] the borrow checker doesn't allow
[L321] [12:36.72] circular data structures and our
[L322] [12:39.28] compiler is chalk full of circular data
[L323] [12:42.16] structures we have trees with parent
[L324] [12:43.92] pointers we have types that are
[L325] [12:45.44] recursive we have symbols that refer I
[L326] [12:47.76] mean it's everywhere and like I said if
[L327] [12:50.24] we had chosen to rewrite we could have
[L328] [12:52.24] probably solved all of that, but it
[L329] [12:54.96] wouldn't have been just porting the
[L330] [12:56.64] code. It would also have been like
[L331] [12:57.92] solving a whole bunch of new problems
[L332] [12:59.60] that we had bought ourselves by by going
[L333] [13:01.52] that route. We tried [laughter]
[L334] [13:04.72] and it just wasn't feasible, you know,
[L335] [13:07.28] uh and and and so so we were we were
[L336] [13:09.76] just trying to optimize for, you know,
[L337] [13:12.56] doing as little work as possible to get
[L338] [13:14.72] us to the payout, which is which and
[L339] [13:18.56] honestly, Rust is no better when it
[L340] [13:20.56] comes to like the quality of the
[L341] [13:22.00] generated code or the or the the
[L342] [13:24.32] concurrency gains that we could have
[L343] [13:25.76] gotten out of it.
[L344] [13:27.84] Go just as it's great. I mean, so so we
[L345] [13:31.60] got we got all the bennies with for less
[L346] [13:33.68] work by by going that route.
[L347] [13:35.76] >> I know some languages they're when you
[L348] [13:37.92] say they're garbage collected, they
[L349] [13:40.40] >> there's something in the the language
[L350] [13:42.72] itself that is doing garbage collection,
[L351] [13:45.04] but um there's also independent
[L352] [13:48.56] libraries that can provide garbage
[L353] [13:50.48] collection, right?
[L354] [13:52.48] There is, but it it but it comes often
[L355] [13:55.44] with a whole bunch of restrictions and
[L356] [13:57.84] and and it doesn't come necessarily with
[L357] [14:00.80] the safety guarantees that we were
[L358] [14:02.32] looking for. I mean, like Go is type
[L359] [14:04.72] safe and memory safe. uh meaning that
[L360] [14:07.36] you don't get to just like have stray
[L361] [14:10.32] pointers or or whatever where Rust you
