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
[L362] [14:13.36] can do ref counting or you can do you
[L363] [14:15.44] can do all sorts of different strategies
[L364] [14:17.52] but there's always like that little bit
[L365] [14:20.24] of unsafe where you have to like do this
[L366] [14:22.64] in order to make it all work you know uh
[L367] [14:25.36] where where if garbage collection is
[L368] [14:28.56] engineered into the language it really
[L369] [14:30.56] is a a separate concern that is you you
[L370] [14:33.36] you don't you don't have to do anything
[L371] [14:35.92] special in I mean of course you you have
[L372] [14:39.04] to like not hold on to data that you no
[L373] [14:41.60] longer need and whatever you know but
[L374] [14:43.36] that's true of ref counting as well
[L375] [14:45.04] right but but it is inherent in in the
[L376] [14:48.32] language
[L377] [14:49.84] when you ported it from JavaScript to go
[L378] [14:52.64] I'm curious how much LLMs were used in
[L379] [14:55.68] that process because I know famously
[L380] [14:58.88] there's some major projects that have
[L381] [15:00.64] been doing uh rewrites of their entire
[L382] [15:03.20] codebase I know there's this JavaScript
[L383] [15:05.44] project called bun
[L384] [15:06.80] >> that rewrote everything from Zigg into
[L385] [15:09.44] Rust and so
[L386] [15:10.80] >> seems like a pretty useful tactic and
[L387] [15:13.20] I'm curious if you leverage that in this
[L388] [15:16.00] process.
[L389] [15:16.80] >> Not a whole lot but it also has to do
[L390] [15:18.96] with timing. Uh we started this project
[L391] [15:21.36] two years ago and two years ago LLMs
[L392] [15:23.68] were nowhere near as good as they are
[L393] [15:25.04] now. I mean that's how crazy fast it
[L394] [15:27.36] it's all moved, right? Um,
[L395] [15:31.84] so what we did though is we we certainly
[L396] [15:34.72] had
[L397] [15:36.48] a bunch of tools that aided us in the in
[L398] [15:39.12] the in the the port. I'd say the
[L399] [15:42.32] prototypes we wrote, the scanner and the
[L400] [15:43.92] parser we wrote manually. Um, and at
[L401] [15:47.60] that point we could convince ourselves,
[L402] [15:49.20] wow, we can actually get 10x out of
[L403] [15:51.04] this. Now what do we do with the rest of
[L404] [15:53.84] this codebase? And what we did was we
[L405] [15:56.80] wrote a tool that syntactically
[L406] [15:58.96] translates TypeScript into Go.
[L407] [16:03.20] This Go that comes out of it, it has no
[L408] [16:05.20] syntax errors in it, but it doesn't
[L409] [16:06.72] compile either because it's full of, you
[L410] [16:09.92] know, like it uses types as if they were
[L411] [16:12.56] TypeScript, which they're not in Go. And
[L412] [16:14.88] so all of that had to be refactored. We
[L413] [16:17.12] had to redo all the data structures or
[L414] [16:18.80] whatever, but we got the same code base
[L415] [16:21.52] out of it. And then we can sort of bang
[L416] [16:23.12] on that. and then in a more localized
[L417] [16:25.60] fashion maybe use AI occasionally to
[L418] [16:28.24] help us do the transformation. So it was
[L419] [16:30.40] sort of manual and automated
[L420] [16:34.88] and a little bit of AI. Now if we were
[L421] [16:38.32] to start the project today would we do
[L422] [16:41.04] it differently? Possibly. Um although I
[L423] [16:43.76] will say if if we just let AI loose on
[L424] [16:48.08] you know what is it like half a million
[L425] [16:49.44] lines of code that we have in the old
[L426] [16:50.80] compiler or somewhere between half a
[L427] [16:52.32] million and a million right uh and asked
[L428] [16:54.72] it to translate it all. Well I don't
[L429] [16:57.28] know that that would absolve us from
[L430] [16:58.88] then having go in and carefully
[L431] [17:00.48] examining every line that came out of it
[L432] [17:02.32] to make sure that there were no
[L433] [17:03.44] hallucinations. Right? Unless you have
[L434] [17:05.60] 100% perfect test coverage, you probably
[L435] [17:08.24] still got to go check all of that. Now I
[L436] [17:11.76] think a a a better approach quite
[L437] [17:14.00] honestly would be enlist AI to write a
[L438] [17:17.92] program that helps you translate from
[L439] [17:20.40] Typescript to Go because at that point
[L440] [17:23.28] you can park the stochasticness in that
[L441] [17:25.76] program and then you can get
[L442] [17:27.60] deterministic behavior whenever you run
[L443] [17:29.76] the program which means you get the same
[L444] [17:31.60] transformation every time you run it
[L445] [17:34.48] right that's always the thing about AI
[L446] [17:36.64] that people forget it's not
[L447] [17:37.92] deterministic right so you can't really
[L448] [17:40.00] trust that it's going to do the same
[L449] [17:41.52] thing twice.
[L450] [17:43.68] Um, [snorts]
[L451] [17:44.72] so, so we might have done it that way,
[L452] [17:47.44] but AI was not ready to do it at the
[L453] [17:49.60] time. Now, that doesn't mean that we
[L454] [17:50.88] don't use AI. I mean, like now down the
[L455] [17:53.44] line, we use AI a lot in our in our
[L456] [17:56.24] internal processes around like the the
[L457] [17:58.24] compiler as everyone does, right? Like
[L458] [18:00.40] help it to write tests and to move pull
[L459] [18:03.04] requests and what what what have you.
[L460] [18:05.36] and and whenever an issue is logged, we
[L461] [18:08.08] first thing we do is put copilot on and
[L462] [18:09.84] see if it can fix it for us, right? I
[L463] [18:11.44] mean, and so yeah,
[L464] [18:13.04] >> in that approach where you you use the
[L465] [18:15.68] LM to generate uh tooling and then you
[L466] [18:19.12] know the tooling is deterministic,
[L467] [18:21.12] >> but you'd still have to validate that
[L468] [18:23.52] thing.
[L469] [18:23.92] >> Yes. But that's that's a lot smaller
[L470] [18:25.92] surface area that you have to validate,
[L471] [18:27.76] right? And honestly, I I've seen that
[L472] [18:30.48] even with friends that are like we did
[L473] [18:32.64] some trip together and there was like
[L474] [18:34.08] some some accounting of they go, well,
[L475] [18:36.48] he paid for the hotel rooms or we paid
[L476] [18:38.16] for this and whatever and we needed to
[L477] [18:39.68] like sort it all out, right? And so, so,
[L478] [18:42.16] okay, well, here's what all the costs
[L479] [18:43.76] were and here were the pie and like have
[L480] [18:45.44] AI fix it for us, right? Or like tell
[L481] [18:47.52] who owes who what and it very
[L482] [18:50.64] authoritatively came up with the wrong
[L483] [18:52.56] answer, right? [laughter]
[L484] [18:54.96] Because it just forgot like about some
[L485] [18:57.04] of the settlements, right? And but if we
[L486] [18:59.20] had asked it to write a spreadsheet,
[L487] [19:02.16] which is really that's just a program,
[L488] [19:03.92] right? Then we would have gotten the
[L489] [19:05.36] right answer because it's very good at
[L490] [19:06.88] writing programs. So it's kind of funny
[L491] [19:09.60] how you you you don't sometimes you you
[L492] [19:12.24] don't ask AI for the for the answer. You
[L493] [19:14.64] ask it for a program that computes the
[L494] [19:16.48] answer.
[L495] [19:17.84] >> What are the potential benefits that you
[L496] [19:20.00] left on the table by doing a port
[L497] [19:21.84] instead of a full rewrite?
[L498] [19:23.52] >> To be honest, I don't think there are
[L499] [19:25.20] any. Um, and I don't think we would
[L500] [19:27.52] consider uh a rewrite. We were quite
[L501] [19:29.76] happy we're quite happy with the way
[L502] [19:31.52] this codebase works. Uh, and we're and
[L503] [19:34.00] we certainly I don't think we're leaving
[L504] [19:36.56] any any money on the on the table
[L505] [19:38.64] currently. Um, and and as I said
[L506] [19:41.28] earlier, rewrites are toxic often for
[L507] [19:44.40] ecosystems because they sacrifice
[L508] [19:47.68] compatibility because you never rewrite
[L509] [19:50.32] and you get you never get back to
[L510] [19:52.08] exactly what you had before, right? Oh,
[L511] [19:54.24] but oh, but in the name of making it
[L512] [19:56.16] better or prettier or whatever, we
[L513] [19:57.84] change this and that and this and that
[L514] [19:59.20] and the other, right? And then well, all
[L515] [20:01.44] the users get to suffer through that,
[L516] [20:03.12] right? So, so backwards compatibility is
[L517] [20:05.92] super important if you want to keep your
[L518] [20:08.08] ecosystem happy. Uh, and and and we we
[L519] [20:10.64] do want that. [laughter]
[L520] [20:12.72] In studying for this interview, I I just
[L521] [20:15.20] keep reading about JavaScript and the
[L522] [20:17.68] the strange semantics of the language.
[L523] [20:20.24] And I think throughout my career too,
[L524] [20:22.24] people have typically
[L525] [20:24.56] not been super satisfied or happy with
[L526] [20:27.44] JavaScript for some reason or the other,
[L527] [20:29.84] >> right?
[L528] [20:30.72] >> And my question is why is it so popular
[L529] [20:34.64] despite that?
[L530] [20:36.24] >> So first of all, I I don't think
[L531] [20:38.24] JavaScript is as bad of a lang of a
[L532] [20:40.56] language as as some people make it out
[L533] [20:42.32] to be. I I I will say in in like the
[L534] [20:44.64] three about three four weeks that
[L535] [20:46.32] Brendan Ike had to create this language
[L536] [20:48.32] back in the mid 90s, he did a lot of
[L537] [20:51.12] things right. Um and thank God that he
[L538] [20:54.24] had been educated on functional
[L539] [20:55.92] programming and and got first class
[L540] [20:58.16] functions done right where you can have
[L541] [21:00.00] functions within functions and the inner
[L542] [21:02.32] functions can access the outer function
[L543] [21:04.16] state and you can pass functions around
[L544] [21:07.04] as first class values.
[L545] [21:10.00] that is super powerful and JavaScript
[L546] [21:12.16] actually got that very right. Um, now
[L547] [21:15.92] there's some quirks in the language too,
[L548] [21:18.08] like all of the automatic conversions
[L549] [21:20.64] and all of the bizarre differences
[L550] [21:22.32] between double equals and triple equals
[L551] [21:24.40] are just like drives everyone mad,
[L552] [21:27.04] right? But that's exactly what type
[L553] [21:28.88] checkers are happy to do. They can like
[L554] [21:30.48] they can far it out all the little
[L555] [21:32.32] differences because they understand the
[L556] [21:34.56] all the deep semantics of the language
[L557] [21:36.40] that no one seems to be able to keep in
[L558] [21:38.40] their mind, right? So, and I think
[L559] [21:40.88] that's part of why Typescript has become
[L560] [21:42.72] so popular, right? It's like it can
[L561] [21:44.48] actually like truly bring out the best
[L562] [21:46.80] parts of JavaScript uh and leave the bad
[L563] [21:49.28] stuff behind. And of course, you can't
[L564] [21:52.88] like like the thing about JavaScript is
[L565] [21:55.52] it is the crossplatform language. Like
[L566] [21:58.32] even Java that was engineered and
[L567] [22:00.64] intended to be the way to write
[L568] [22:02.40] crossplatform applications, it's not
[L569] [22:04.80] really crossplatform. It doesn't run in
[L570] [22:07.36] the browser, you I mean it doesn't it
[L571] [22:09.20] doesn't run everywhere, right?
[L572] [22:10.32] JavaScript runs everywhere. Um, so there
[L573] [22:15.20] are a lot of there are a lot of reasons
[L574] [22:16.80] why you should like JavaScript and and
[L575] [22:20.16] with TypeScript, I think we've managed
[L576] [22:22.00] to sort of capture all the badness and
[L577] [22:25.76] park it.
[L578] [22:27.76] I saw there were some projects. I don't
[L579] [22:29.84] know if you're familiar with Dart or
[L580] [22:32.72] CoffeeScript and
[L581] [22:34.64] >> it seems like these were some effort to
[L582] [22:37.68] replace JavaScript or improve it and
[L583] [22:40.96] >> right
[L584] [22:41.44] >> but they're not popular today. So I'm
[L585] [22:43.36] curious what happened.
[L586] [22:44.72] >> I mean I think coffecript was mostly
[L587] [22:49.28] it's a different syntax for JavaScript.
[L588] [22:51.60] So, so it doesn't really change the the
[L589] [22:53.68] semantics and it doesn't it didn't
[L590] [22:55.52] provide any additional tooling and and
[L591] [22:57.68] whatever. And and Dart was also in a
[L592] [23:00.08] sense about fixing JavaScript, right?
[L593] [23:03.12] But if you can fix something by fixing
[L594] [23:06.88] it instead of trying to replace it with
[L595] [23:09.92] something else, then you're doing the
[L596] [23:13.84] ecosystem a much bigger favor, I think.
[L597] [23:16.56] Right. And that's what we set out to do
[L598] [23:18.32] with TypeScript. We weren't trying to
[L599] [23:19.84] change JavaScript. we were trying to
[L600] [23:21.60] improve JavaScript. Um, and I think
[L601] [23:24.80] that's ultimately why we why we
[L602] [23:26.80] succeeded.
[L603] [23:28.24] >> I mean, in this new age where it's very
[L604] [23:31.92] feasible that maybe AI could rewrite
[L605] [23:34.24] code bases,
[L606] [23:36.08] um, I imagine people will start to go
[L607] [23:39.36] towards the the desired languages rather
[L608] [23:42.40] than the ones that are the incumbent
[L609] [23:43.84] languages.
[L610] [23:45.44] And I'm curious if you think that
[L611] [23:47.36] JavaScript might become less used in the
[L612] [23:49.84] future.
[L613] [23:51.52] >> See, I I don't think so. I I what I've
[L614] [23:54.16] observed is that AI
[L615] [23:58.40] is best at the languages if seen the
[L616] [24:01.68] most of in its training set, right? And
[L617] [24:04.48] AI gets trained on all the code that
[L618] [24:06.40] exists in the world. Um,
[L619] [24:09.68] which means there's an awful lot of
[L620] [24:11.28] JavaScript, an awful lot of TypeScript,
[L621] [24:12.96] an awful lot of Python. And therefore,
[L622] [24:15.20] AI is good at JavaScript and TypeScript
[L623] [24:17.36] and Python. And it is less good at my
[L624] [24:20.72] favorite little language that I just
[L625] [24:22.32] invented. In fact, there's none of it in
[L626] [24:23.92] the training set, which means you have
[L627] [24:25.52] to sacrifice God knows how many tokens
[L628] [24:27.60] in the prompt to teach AI the language
[L629] [24:31.84] before you can even ask it a question
[L630] [24:33.52] about the language. Do you know what I
[L631] [24:35.20] mean? So in that sense I think incumbent
[L632] [24:38.96] languages are actually if anything going
[L633] [24:41.20] to flourish uh because of AI and we're
[L634] [24:44.00] sort of seeing that right now with with
[L635] [24:45.76] TypeScript too right there there's a
[L636] [24:47.84] noticeable knee in the curve of
[L637] [24:49.52] TypeScript adoption that coincides with
[L638] [24:52.88] the advent of AI. I do think the
[L639] [24:55.52] incumbent languages are actually if
[L640] [24:57.52] anything getting stronger.
[L641] [24:59.12] >> What percent of all JavaScript is
[L642] [25:02.24] written in Typescript?
[L643] [25:04.80] Well, so, so in the last year,
[L644] [25:08.08] Typescript uh became the number one used
[L645] [25:11.92] language on GitHub. Um, so there's
[L646] [25:14.96] JavaScript more than JavaScript.
[L647] [25:16.72] >> So, so more than 50% on GitHub at least
[L648] [25:20.56] >> is is is written in in Typescript. Um,
[L649] [25:23.68] so so we're actually like larger now
[L650] [25:25.84] than the language that we set out to
[L651] [25:27.68] improve.
[L652] [25:28.96] >> Wow.
[L653] [25:29.52] >> Yeah. And larger than Python. If you
[L654] [25:32.00] were to just draw that out in the
[L655] [25:33.28] future, do you think that eventually
[L656] [25:35.76] TypeScript would become the default and
[L657] [25:37.92] almost 100% of all JavaScript would be
[L658] [25:40.40] typed?
[L659] [25:41.60] >> Well, certainly, I mean, if you're
[L660] [25:43.36] having AI write it, I I almost challenge
[L661] [25:46.56] you to find a tool that writes
[L662] [25:48.16] JavaScript. They all write TypeScript.
[L663] [25:50.40] Uh because it helps AI write better code
[L664] [25:53.92] because the type annotations guide the
[L665] [25:56.64] LLM towards writing or to write making
[L666] [25:59.84] fewer mistakes. and the ability for us
[L667] [26:02.80] to statically validate the code before
[L668] [26:06.16] you run it. I mean, that's the
[L669] [26:08.24] distinction, right? The only way you can
[L670] [26:09.76] validate JavaScript is by running it,
[L671] [26:12.88] which means you have to set up a runtime
[L672] [26:14.48] environment, which might not be possible
[L673] [26:16.24] for AI to do because AI lives in a
[L674] [26:18.72] sandbox, right? But AI can run through
[L675] [26:21.68] tools, the compiler, and check the code
[L676] [26:24.72] that it just generated and be told, "Oh,
[L677] [26:26.64] you made a mistake. Oh, well, let me fix
[L678] [26:28.24] it then before I even tell anyone that I
[L679] [26:30.08] made the mistake, right? [laughter]
[L680] [26:32.32] [snorts]
[L681] [26:32.96] >> After learning about the this 10x
[L682] [26:35.12] improvement in performance from uh
[L683] [26:37.68] rewriting in native, I makes me wonder
[L684] [26:40.96] why anyone would use JavaScript on the
[L685] [26:44.00] back end. Why not just always use native
[L686] [26:47.28] languages on the back end?
[L687] [26:48.48] >> Well, it depends on your problem. Uh I
[L688] [26:51.20] think because the thing that that
[L689] [26:52.96] overlooks is
[L690] [26:55.36] what kind of thing am I going to write
[L691] [26:56.72] on the back end, you know, like like
[L692] [26:58.40] there are an awful lot of very very good
[L693] [27:02.00] web server frameworks for example that
[L694] [27:04.72] that use TypeScript or JavaScript,
[L695] [27:07.12] right? So, so if there are like
[L696] [27:10.00] frameworks in your ecosystem that gets
[L697] [27:11.84] you to a solution quicker than if you
[L698] [27:14.64] had to write that because your native
[L699] [27:16.72] language wasn't really intended to
[L700] [27:18.96] target that particular community. So, I
[L701] [27:22.32] think it very much depends on
[L702] [27:25.44] your what what your problem is
[L703] [27:27.28] affinitized with. Um, and and often PF
[L704] [27:31.60] of your code isn't the bottleneck. I
[L705] [27:34.40] mean, like look at Python. I mean right
[L706] [27:37.28] it's it's used to basically script and
[L707] [27:39.92] all of the LLM training in in the world
[L708] [27:42.32] right I mean which clearly a lot of that
[L709] [27:44.96] code is ultra timer critical uh but
[L710] [27:47.68] that's written in native code right and
[L711] [27:49.20] then you use Python as the orchestration
[L712] [27:51.04] language and in a sense in a web server
[L713] [27:53.60] you know like TypeScript is just an
[L714] [27:55.20] orchestrator you know of talking to a
[L715] [27:58.16] database and doing this and that what
[L716] [27:59.76] and and and the things that the things
[L717] [28:01.68] that that ultimately control the
[L718] [28:03.76] performance of applications like that
[L719] [28:05.36] aren't necessarily
[L720] [28:07.20] whether that inner for loop is running
[L721] [28:10.40] as as as native code or not which
[L722] [28:13.04] actually it is because of the JIT anyway
[L723] [28:15.92] right I mean so
[L724] [28:18.56] I mean measure measure first and then
[L725] [28:22.16] make decisions right because you always
[L726] [28:24.08] get surprised when you measure
[L727] [28:26.88] >> when you talk about how much faster it
[L728] [28:28.64] was too one of my immediate thoughts is
[L729] [28:31.44] why wasn't it done sooner
[L730] [28:33.44] >> you know at the time we started
[L731] [28:35.52] TypeScript script. I don't know that we
[L732] [28:37.60] had ever envisioned that people would be
[L733] [28:39.84] writing projects that are the size of
[L734] [28:42.08] the projects that people are now writing
[L735] [28:44.08] in Typescript, right? Like Visual Studio
[L736] [28:47.36] Code is like 2.3 million lines of code.
[L737] [28:50.24] I mean, we have in in-house projects
[L738] [28:52.32] that are over 10 million lines of of of
[L739] [28:55.20] code, which is insanity. We would have
[L740] [28:57.36] just at the time gone, well, that's
[L741] [28:58.80] clearly no one's ever going to do that,
[L742] [29:00.72] right? But that was a decade ago or more
[L743] [29:02.88] than a decade ago, right? We started in
[L744] [29:04.64] 2012 with the TypeScript project and the
[L745] [29:06.64] world looked very different and so
[L746] [29:08.56] gradually people have started writing
[L747] [29:11.68] larger and larger and larger projects,
[L748] [29:13.68] right? And at the same time, our
[L749] [29:16.72] compiler has gotten smarter and smarter.
[L750] [29:18.56] We've added all sorts of cool features
[L751] [29:20.48] like union types and discriminated
[L752] [29:22.48] unions and control flow analysis and
[L753] [29:24.80] blah blah blah. And all of these things
[L754] [29:28.32] make our type checking even better, but
[L755] [29:30.24] it also makes it go a little slower
[L756] [29:32.00] every time we add a new feature. Right?
[L757] [29:33.76] In fact, our TypeScript 6 runs only
[L758] [29:35.92] about 50% of the speed of TypeScript 1.5
[L759] [29:39.92] for example. But TypeScript 1.5 also did
[L760] [29:42.72] a whole lot less. Um, so projects have
[L761] [29:46.00] gotten bigger and the compiler does
[L762] [29:48.24] more. All of which [laughter]
[L763] [29:51.04] detract from your effective output. And
[L764] [29:53.36] as I mentioned, Mors law also
[L765] [29:56.24] unfortunately stopped delivering faster
[L766] [29:58.40] CPUs and JavaScript keeps you from
[L767] [30:00.72] taking advantage of the additional
[L768] [30:02.40] cores. And it's not clear that we could
[L769] [30:04.88] have foreseen all of that, right? But
[L770] [30:07.36] but but it's just the way it panned out,
[L771] [30:10.16] right? [snorts]
[L772] [30:11.12] >> Open AAI, Enthropic, Curser, and
[L773] [30:14.08] Verscell all use this product to make
[L774] [30:16.32] their lives better. And the problem it
[L775] [30:18.48] solves is when you're building SAS or an
[L776] [30:20.72] AI product and you want to sell to other
[L777] [30:23.04] companies, there's all these
[L778] [30:24.56] requirements you need to meet. There's
[L779] [30:26.56] SSO, there's skim, there's arbback,
[L780] [30:29.76] there's audit logs. These are all things
[L781] [30:31.60] that take time to integrate but aren't
[L782] [30:33.76] the main focus of your app. Work OS is
[L783] [30:36.08] an API layer that lets you meet all of
[L784] [30:37.92] these requirements in just a few lines
[L785] [30:40.16] of code. So let's say you have a new SAS
[L786] [30:42.56] product and you want to sell to other
[L787] [30:44.16] companies. work OS will solve all of
[L788] [30:46.40] these critical feature gaps for you. You
[L789] [30:49.12] can check them out at workos.com to
[L790] [30:51.60] learn more and get started. And I
[L791] [30:53.76] appreciate them for supporting my work
[L792] [30:55.44] and sponsoring this podcast. Jira by
[L793] [30:58.16] Atlassian isn't just for tracking work
[L794] [31:00.24] anymore. Now you can pick your favorite
[L795] [31:02.08] AI agent to assign tasks to and they'll
[L796] [31:04.80] get access to the rich context that's
[L797] [31:06.80] already in Jira. When the agent is done,
[L798] [31:09.12] it surfaces a pull request. That way you
[L799] [31:11.44] can get more done with your favorite
[L800] [31:13.04] agents all in one place. Learn more at
[L801] [31:16.00] jira.dev. That's jir.dev.
[L802] [31:20.72] Appreciate them for sponsoring the
[L803] [31:22.16] podcast. And back to the show. When I
[L804] [31:24.72] first became a software engineer and I I
[L805] [31:27.20] went to start working at Facebook at the
[L806] [31:29.44] time, they had this popular framework
[L807] [31:32.24] called Flow, which was
[L808] [31:34.16] >> doing type inference on top of
[L809] [31:36.72] JavaScript. It was this thing that would
[L810] [31:38.16] take a long time.
[L811] [31:39.12] >> Yep. And then I' I'd never hear about it
[L812] [31:41.36] these days. So it sounds like Typescript
[L813] [31:44.40] won if there was a competition to
[L814] [31:46.40] typing.
[L815] [31:47.12] >> There was a bit of it. Yeah. In in in
[L816] [31:49.12] the early days. Um I think the thing
[L817] [31:52.64] that worked for us was actually the fact
[L818] [31:54.88] that we were self-hosted which made it a
[L819] [31:57.52] lot easier for the community to
[L820] [31:58.88] contribute to the project. [snorts]
[L821] [32:01.28] Flow was written as I recall in camel.
[L822] [32:04.88] Um, and so in order to contribute to
[L823] [32:07.52] flow, you had to go learn a whole
[L824] [32:09.20] different way of programming and and in
[L825] [32:11.20] a in a different language, right? And
[L826] [32:13.44] Float also didn't really focus all that
[L827] [32:15.84] much on
[L828] [32:17.60] IDE based tooling,
[L829] [32:20.00] which we knew full well going in. We're
[L830] [32:22.48] writing a compiler, but we're not
[L831] [32:23.76] writing a compiler in order to generate
[L832] [32:26.16] machine code. We're writing it to make
[L833] [32:27.92] better tooling. That was why we wrote
[L834] [32:30.08] it, you know, and so right there
[L835] [32:33.04] handinhand with our compiler, we had a
[L836] [32:35.12] language service. It was deeply
[L837] [32:36.56] integrated into Visual Studio, Visual
[L838] [32:38.48] Studio Code, all sorts of other editors
[L839] [32:40.64] through an open protocol, you know, and
[L840] [32:42.72] that just that's where that was the
[L841] [32:46.32] problem that needed solving, right? I
[L842] [32:48.32] mean, it's not it's it's nice to have a
[L843] [32:50.48] type checker, but boy, you you want
[L844] [32:52.48] that. You also want statement
[L845] [32:53.92] completion. You wanted red squiggies.
[L846] [32:55.92] You want like I mean, you want it
[L847] [32:57.36] interactive, right?
[L848] [32:59.12] So I know in your career you've you've
[L849] [33:01.28] worked on uh multiple programming
[L850] [33:03.44] languages. What does it take to build a
[L851] [33:06.08] programming language? Well, first I'll
[L852] [33:09.92] say that the world needs another
[L853] [33:11.52] programming language like it needs
[L854] [33:12.72] another hole in the head. I mean it it's
[L855] [33:14.48] it's like you you kind of got to be a
[L856] [33:16.64] certain [laughter] kind of of person to
[L857] [33:20.08] to even embark on it to begin with,
[L858] [33:22.16] right? It's a super fascinating area of
[L859] [33:25.44] of computer science and it's one that's
[L860] [33:27.44] been around ever since the beginning of
[L861] [33:29.92] of of computers. Now, every compiler,
[L862] [33:33.28] every language has a whole bunch of
[L863] [33:35.60] things you need to to understand like
[L864] [33:37.20] parsers and scanners and lexers and code
[L865] [33:39.28] generators and and and and whatever,
[L866] [33:41.60] right? But but that's sort of the
[L867] [33:44.08] mechanics of implementing the language.
[L868] [33:46.88] And then there's the design of the of
[L869] [33:49.68] the language, sort of the art of making
[L870] [33:53.36] it feel right and whatever, right? And I
[L871] [33:55.84] I think you sort of have to master both.
[L872] [33:59.36] And then you also got to appreciate that
[L873] [34:01.28] like every new language is actually only
[L874] [34:03.60] 10% new and then it's 90% the same
[L875] [34:06.56] drudgery that every other language has
[L876] [34:08.32] to go do. And so be prepared for a lot
[L877] [34:11.12] of work that maybe isn't as interesting,
[L878] [34:14.40] you know.
[L879] [34:16.48] And then finally maybe I'll say that you
[L880] [34:19.20] know like never forget there that you
[L881] [34:21.92] you stand on the shoulders of giants. I
[L882] [34:24.40] mean you you in order to make a great
[L883] [34:26.32] programming language you got to
[L884] [34:27.52] understand a bunch of other programming
[L885] [34:28.96] languages first uh and understand all
[L886] [34:31.60] the all the distinctions between the
[L887] [34:33.52] different styles of programming like
[L888] [34:34.88] procedural and object-oriented or
[L889] [34:36.48] functional or what have you. Um
[L890] [34:40.08] and then last but not least it's like
[L891] [34:43.12] it's a long game. I mean, it is probably
[L892] [34:45.84] a longer game than anything else. I
[L893] [34:47.76] mean, like every language project I've
[L894] [34:51.76] worked on, I've worked on each of them
[L895] [34:53.76] for at least 10 years. Um, and shipped
[L896] [34:57.68] multiple versions, and it's really never
[L897] [34:59.84] until version three that it truly starts
[L898] [35:02.24] to get okay. Do you know what I mean?
[L899] [35:05.20] And, and it just takes an incredible
[L900] [35:07.12] amount of devotion to to that. So, you
[L901] [35:09.20] got to really not be the type that tires
[L902] [35:11.52] of a problem quickly and then moves
[L903] [35:13.12] along. that you're not meant to do
[L904] [35:14.96] language design.
[L905] [35:17.28] And you see that too if when you talk to
[L906] [35:19.44] language designers in the industry,
[L907] [35:20.80] they've been doing it for a long time.
[L908] [35:22.96] >> You mentioned those two parts. There's
[L909] [35:24.56] the the objective pieces that you need
[L910] [35:28.40] to implement and then there's the the
[L911] [35:31.04] art of the design and making the
[L912] [35:32.88] language I guess ergonomic for
[L913] [35:35.44] developers. When you think of that
[L914] [35:37.84] second part, that art
[L915] [35:39.68] >> and you look at other programming
[L916] [35:41.28] languages, are there any that you admire
[L917] [35:43.76] outside of the ones that you've worked
[L918] [35:45.12] on? Of course,
[L919] [35:47.04] >> learning and and and fully appreciating
[L920] [35:49.60] the beauty of functional programming has
[L921] [35:51.76] has been very educational, right? I
[L922] [35:54.00] mean, because it really is a different
[L923] [35:55.76] way of thinking about programming, a way
[L924] [35:58.72] of thinking of programming that's much
[L925] [36:00.48] closer to math than it is to
[L926] [36:04.40] machines. Um,
[L927] [36:07.28] and I think there's there's a lot of uh
[L928] [36:10.48] incredible goodness that has come from
[L929] [36:12.24] that. And and honestly even in in like
[L930] [36:14.16] like building the TypeScript project uh
[L931] [36:17.04] large portions of the TypeScript
[L932] [36:18.64] compiler are written in a highly
[L933] [36:20.48] functional style um and work on
[L934] [36:23.28] immutable data structures that are then
[L935] [36:25.60] now because of shared memory concurrency
[L936] [36:27.84] can be shared between different
[L937] [36:32.32] uh threads or processes that don't
[L938] [36:35.44] mutate the data and therefore they can
[L939] [36:37.20] share one data structure. Right? And
[L940] [36:39.52] that's incredibly powerful. But
[L941] [36:41.60] mastering this, you know, like writing
[L942] [36:43.76] islands of pure functional programming
[L943] [36:46.08] inside an imperative program and ma and
[L944] [36:48.72] and and putting it together with
[L945] [36:50.00] concurrency. I mean, it's it's it's
[L946] [36:51.36] complex, but I think functional
[L947] [36:53.28] programming has brought a lot to the
[L948] [36:54.72] world. Um, I know object-oriented
[L949] [36:56.96] programming as well. I mean, but I
[L950] [36:58.56] wouldn't single out any particular
[L951] [37:01.44] language. Every one language you you
[L952] [37:03.92] come in contact with, you learn
[L953] [37:05.28] something. You know,
[L954] [37:07.12] >> you mentioned the world doesn't really
[L955] [37:10.24] need more programming languages and uh
[L956] [37:14.32] if you think 10 years from now, do you
[L957] [37:16.08] think there'll be less programming
[L958] [37:17.52] languages than there are today?
[L959] [37:19.36] >> It's hard to say. I mean, but like I
[L960] [37:22.24] said,
[L961] [37:24.24] AI tends to favor the incumbents, right?
[L962] [37:28.56] And I I do think and I I think this has
[L963] [37:30.88] been true even before AI. The bar keeps
[L964] [37:33.44] going up for what it takes to
[L965] [37:36.40] successfully implement a programming
[L966] [37:38.64] language and create an ecosystem around
[L967] [37:40.48] it. I mean it used to be oh you just
[L968] [37:42.96] need a compiler.
[L969] [37:45.20] Well
[L970] [37:46.88] you also kind of need tooling now. I
[L971] [37:48.72] mean you need a language service you
[L972] [37:50.56] need uh you need debuggers. You need
[L973] [37:52.80] profilers. You need frameworks and
[L974] [37:54.88] libraries. You need code generators that
[L975] [37:58.24] can target all sorts of I mean it's like
[L976] [38:02.08] it just keeps getting harder and harder
[L977] [38:04.88] uh you know to to to get all the way
[L978] [38:07.20] there.
[L979] [38:08.48] >> Well, when you think about all those
[L980] [38:09.76] pieces that really they're all for the
[L981] [38:13.60] people or I mean the you know the IDE
[L982] [38:16.56] and the types and I mean the the
[L983] [38:19.84] computer looks at that too but it's so
[L984] [38:22.08] that we can read source.
[L985] [38:24.32] Maybe one day the LMS will generate
[L986] [38:27.12] machine code directly. I wonder. Um
[L987] [38:32.32] I think
[L988] [38:35.44] I think LLMs are better at what they do
[L989] [38:39.52] when when they don't have to repeat
[L990] [38:41.68] themselves a lot. I I I think like
[L991] [38:46.64] when a program is expressed in text, it
[L992] [38:49.60] is closest to its sort of ultimate
[L993] [38:54.72] condensed meaning and representation,
[L994] [38:57.20] right? If you translate it into machine
[L995] [38:59.20] code, there's an awful lot of noise in
[L996] [39:01.44] that machine code. Like all of the
[L997] [39:03.68] instructions, like half of the
[L998] [39:04.96] instructions are memory addresses that
[L999] [39:06.64] have absolutely no bearing on what's
[L1000] [39:08.48] going on here, right? So half of it,
[L1001] [39:10.16] half of all the data is noise already,
[L1002] [39:12.32] right? And then whichever register you
[L1003] [39:14.24] pick, well, that doesn't matter either
[L1004] [39:15.60] in the code generator. And honestly, you
[L1005] [39:17.28] could change your mind at any point in
[L1006] [39:18.64] time. So, so teasing the truth out of
[L1007] [39:21.28] that noise is a lot harder than if you
[L1008] [39:26.40] just have a program where the variable
[L1009] [39:27.76] is called I and whatever. And by the
[L1010] [39:29.52] way, that you can relate to the written
[L1011] [39:32.08] instruction that the user just gave you.
[L1012] [39:34.16] I mean, keep in mind that that like AI
[L1013] [39:36.80] are they're just emulators of humans in
[L1014] [39:39.28] a sense, right? I mean, they they it's
[L1015] [39:41.12] like neural networks, right? There's a
[L1016] [39:42.96] reason we have programming languages
[L1017] [39:44.72] because we're terrible at writing
[L1018] [39:46.40] machine code straight off. out of our
[L1019] [39:49.12] head, right? AI is not that different
[L1020] [39:51.92] from us, you know? So, the same would
[L1021] [39:54.96] probably be true there. when you look
[L1022] [39:57.20] back on working on C and you know
[L1023] [39:59.60] TypeScript and these language projects
[L1024] [40:02.56] they were long journeys and I think you
[L1025] [40:04.80] know one thing people might want to know
[L1026] [40:06.72] is what did you learn through those
[L1027] [40:09.28] journeys that if you knew at the
[L1028] [40:11.44] beginning of when you embarked on
[L1029] [40:12.96] working on them you you might have been
[L1030] [40:16.32] better off
[L1031] [40:19.44] gosh well each journey is is different
[L1032] [40:23.52] uh I mean like the first project I
[L1033] [40:25.52] worked on turbo Pascal. I I think
[L1034] [40:30.32] that project started back in the old
[L1035] [40:32.32] days when it was 8-bit micros and 64k of
[L1036] [40:34.88] memory and one person could do
[L1037] [40:36.56] everything themselves and have ultimate
[L1038] [40:39.28] control of everything. And so I was very
[L1039] [40:41.28] much a one-man shop, right? But that
[L1040] [40:45.76] quickly was not scalable, right? And and
[L1041] [40:48.00] and capacities of machines. So we went
[L1042] [40:50.32] for 64 to 640K and then then kaboom the
[L1043] [40:53.12] the the the lid went off, right? and you
[L1044] [40:54.96] could have as much memory as you wanted
[L1045] [40:56.88] and so not one person couldn't do it and
[L1046] [40:59.60] I had to learn to become a team player
[L1047] [41:02.00] right and that that was a big journey
[L1048] [41:05.52] for me I mean to learn to let go right
[L1049] [41:08.40] if you're a perfectionist that that that
[L1050] [41:10.24] could be hard but that's one thing that
[L1051] [41:12.24] I would say I learned there
[L1052] [41:14.24] >> well another way to word this question
[L1053] [41:16.32] is you know what's the most common
[L1054] [41:18.96] mistake that you see people make when
[L1055] [41:20.96] they embark on building a programming
[L1056] [41:22.80] language
[L1057] [41:24.40] Well, I think people tend to overindex
[L1058] [41:26.96] on one idea, you know, that that they
[L1059] [41:29.28] have that they think, "Oh, wouldn't it
[L1060] [41:30.72] be cool if my language could do blah,
[L1061] [41:33.44] and then they underindex on all of the
[L1062] [41:35.92] mundane stuff that every programming
[L1063] [41:38.08] language has to do, you know, and then
[L1064] [41:40.08] it ends up doing that one thing they
[L1065] [41:41.92] love maybe better, but then it does
[L1066] [41:44.40] everything else not as good." [laughter]
[L1067] [41:47.60] And and and the net is a detractor,
[L1068] [41:50.88] right? And so it's so hard to convey how
[L1069] [41:55.36] many things you have to do that really
[L1070] [41:57.68] doesn't have anything to do with the
[L1071] [41:59.68] problem you're you're trying to solve
[L1072] [42:02.08] per se, you know, when you're
[L1073] [42:04.16] implementing programming languages.
[L1074] [42:06.00] >> And when you were working on C, do you
[L1075] [42:08.48] keep tabs on the other languages and
[L1076] [42:11.20] >> you know what they're doing better, what
[L1077] [42:13.12] you could do better with C?
[L1078] [42:15.28] >> Yeah. No, you got to keep yourself
[L1079] [42:16.88] informed about because like I said, we
[L1080] [42:19.60] all stand on the shoulders of giants,
[L1081] [42:21.36] you know, no other no programming
[L1082] [42:23.52] language was ever created in in in
[L1083] [42:26.40] perfect isolation, right? Everyone
[L1084] [42:28.56] learns from from everyone and then
[L1085] [42:30.48] someone comes up with a good idea and
[L1086] [42:32.08] then you see it adopted elsewhere and
[L1087] [42:33.52] we've adopted many ideas from functional
[L1088] [42:35.44] programming you know in C for example
[L1089] [42:38.40] and then other languages have adopted
[L1090] [42:40.24] some of the good ideas we had in C# like
[L1091] [42:42.08] async you know now is in JavaScript and
[L1092] [42:44.80] in some of the other programming
[L1093] [42:45.92] languages out there and that was
[L1094] [42:47.20] pioneered in C and so you know it's it's
[L1095] [42:50.88] we all learn from each other um and and
[L1096] [42:53.84] that's how the industry moves forward
[L1097] [42:56.40] really You mentioned the I guess
[L1098] [42:59.36] learning to let go. I think that's
[L1099] [43:00.96] something that a lot of people as their
[L1100] [43:03.28] career advances they they start with you
[L1101] [43:06.00] know individual contributor work and
[L1102] [43:07.60] then later they start delegating things.
[L1103] [43:10.56] >> How did you learn that or what was the
[L1104] [43:12.88] is there like a maybe a story or
[L1105] [43:14.80] particular project where you you let go
[L1106] [43:17.84] and you you kind of develop that skill?
[L1107] [43:21.36] Well, it's it's almost like I got a
[L1108] [43:23.12] counter story to the to the letting
[L1109] [43:24.88] letting go there because in the C
[L1110] [43:28.16] project um my main function was not
[L1111] [43:31.52] implementing the the C# compiler. It was
[L1112] [43:34.00] being the language designer and writing
[L1113] [43:35.60] the spec and designing all the new
[L1114] [43:37.76] language features. And
[L1115] [43:42.00] before that when I when I had worked on
[L1116] [43:44.00] Turbo Pascal, I was I was doing a bunch
[L1117] [43:45.92] of active coding, you know, on on the
[L1118] [43:48.24] thing itself, right? But then I sort of
[L1119] [43:50.72] let go of that. But I let go of it too
[L1120] [43:52.96] much and I sort of drifted up into the
[L1121] [43:55.60] stratosphere and became more of an
[L1122] [43:57.20] architecture astronaut. Do you know what
[L1123] [43:59.12] I mean? And and and I wasn't getting my
[L1124] [44:01.28] hands dirty. I was writing stuff in the
[L1125] [44:03.12] framework and in the libraries, but it
[L1126] [44:04.80] was it didn't quite these are not like
[L1127] [44:07.36] the deep really super hard problems to
[L1128] [44:10.16] solve, right? And and I didn't really
[L1129] [44:12.24] know it at the time, but I was gradually
[L1130] [44:14.16] getting less happy with with the work
[L1131] [44:17.12] that I was that I was doing, right? I
[L1132] [44:19.28] mean, it's I still enjoy, but there was
[L1133] [44:21.04] something missing, right? And so when
[L1134] [44:23.60] when this TypeScript opportunity came
[L1135] [44:25.44] along, I decided to jump in and actually
[L1136] [44:28.24] actively participating writing compiler
[L1137] [44:30.24] and it brought so much happiness to my
[L1138] [44:32.24] life. Like I I I I finally realized I'm
[L1139] [44:34.96] just I'm just a happy coder, you know? I
[L1140] [44:37.04] mean, I like the spec stuff too, but but
[L1141] [44:40.08] coding is like, man, that's what gets me
[L1142] [44:42.32] up in the morning, make coffee, and
[L1143] [44:43.52] write some code, you know? That's that's
[L1144] [44:45.36] that's that's when I'm my in in my happy
[L1145] [44:48.32] space, you know.
[L1146] [44:50.24] you know, when people are at these
[L1147] [44:51.60] really really high levels, they're kind
[L1148] [44:53.92] of have this expectation of a certain
[L1149] [44:55.76] level of impact. And so, how do you
[L1150] [44:58.96] continue to write code at as such a high
[L1151] [45:01.76] level engineer?
[L1152] [45:02.80] >> Well, the specific code I'm writing
[L1153] [45:06.08] isn't necessarily having all all that
[L1154] [45:08.64] impact, but it's it's the fact that I
[L1155] [45:10.88] also do the architectural guidance, you
[L1156] [45:14.32] know, as part of a a group of people,
[L1157] [45:16.72] right? in a in a project, you know,
[L1158] [45:18.32] there's plenty of work for everyone to
[L1159] [45:19.68] go around and then you you just but you
[L1160] [45:21.68] you you stay involved in a corner of the
[L1161] [45:23.92] project because then you see what
[L1162] [45:25.52] happens in the code, you know, when
[L1163] [45:27.60] you're checking in your code, you go,
[L1164] [45:29.28] what was what what was that over there?
[L1165] [45:31.28] Let let me just what what's happening
[L1166] [45:32.80] over here, you know, or or you realize,
[L1167] [45:35.04] oh, we need to refactor this. This this
[L1168] [45:36.96] is not this is not feeling right
[L1169] [45:38.40] anymore. Or if if but if you let go of
[L1170] [45:41.28] that you don't really you can't really
[L1171] [45:43.60] talk about the thing that people use
[L1172] [45:46.48] day-to-day. You can talk about the
[L1173] [45:47.76] syntax of the thing that people use
[L1174] [45:49.36] day-to-day but you can't talk about that
[L1175] [45:50.96] thing you know so
[L1176] [45:54.40] so both are important I think and I'm
[L1177] [45:56.80] happy that I get to do both now I know a
[L1178] [46:00.08] lot of companies have this idea of
[L1179] [46:01.60] engineering archetypes or the the way
[L1180] [46:04.40] that highle engineers get some work done
[L1181] [46:07.84] and you mentioned architect for instance
[L1182] [46:10.00] a lot of companies have different words
[L1183] [46:11.52] for architect I'm not sure if you're
[L1184] [46:13.68] saying it's just your working style or
[L1185] [46:16.08] are you saying that all high level
[L1186] [46:18.32] engineers should be hands-on at some
[L1187] [46:21.12] level.
[L1188] [46:22.08] >> No, I I'm not saying that because I
[L1189] [46:24.64] don't think it's it's like I made a
[L1190] [46:26.32] conscious choice to
[L1191] [46:28.72] remain an independent uh contributor as
[L1192] [46:31.44] opposed to become a manager. I mean, I
[L1193] [46:33.20] had plenty of opportunities um but but
[L1194] [46:36.88] it that is not where I do my best work,
[L1195] [46:39.36] right? So I think you have to decide for
[L1196] [46:41.28] yourself what is it that motivates you,
[L1197] [46:44.32] makes you happy, keeps you doing this
[L1198] [46:46.24] for for a lifetime. Do do you know what
[L1199] [46:49.04] I mean? And and and you only get one run
[L1200] [46:52.08] at it in in life here, you know? And so,
[L1201] [46:54.64] and if you're going to do your best
[L1202] [46:56.00] work, do the thing that that makes you
[L1203] [46:58.88] the most happy, I think, is and and
[L1204] [47:01.68] that's what I
[L1205] [47:04.16] learned, you know, along the way there,
[L1206] [47:06.96] that coding is part of that, a big part
[L1207] [47:08.88] of that.
[L1208] [47:10.08] >> So then when you were working on C, but
[L1209] [47:12.96] before Typescript, like how did you know
[L1210] [47:15.28] something was missing?
[L1211] [47:16.48] >> I just knew something. I I I I don't
[L1212] [47:18.64] know how I mean it it just I would I
[L1213] [47:20.40] just wasn't feeling as fulfilled with
[L1214] [47:23.04] with with the with only doing the design
[L1215] [47:26.00] part, right? I I I missed the coding.
[L1216] [47:28.80] And whenever I had a chance to write a
[L1217] [47:31.68] little bit of code, I would feel a lot
[L1218] [47:33.04] happier and I go, it's kind of
[L1219] [47:34.40] interesting. I mean, do you know what I
[L1220] [47:36.32] mean? But now I got to go write some
[L1221] [47:37.84] more specs, you know? [laughter]
[L1222] [47:41.60] >> So then, uh was Typescript something you
[L1223] [47:43.92] kind of went towards because you wanted
[L1224] [47:46.08] to write more code? I went towards it
[L1225] [47:47.84] for for many reasons. I mean it wasn't
[L1226] [47:50.32] specifically that to begin with. I I
[L1227] [47:52.40] just found the problem fascinating,
[L1228] [47:54.16] right? I mean because the way Typescript
[L1229] [47:56.32] came about was
[L1230] [47:58.64] actually indirectly through C because
[L1231] [48:01.52] the outlook.com team I think it was
[L1232] [48:04.24] approached the C group and asked whether
[L1233] [48:07.36] we would pretty please productize
[L1234] [48:09.44] something called script sharp. And
[L1235] [48:11.68] script sharp was this thing that took C
[L1236] [48:14.24] and transpiled it into JavaScript so you
[L1237] [48:17.44] could run it in a browser. And I'm like
[L1238] [48:20.48] what? Why? Why would you want to do
[L1239] [48:23.20] that? Why don't you just write the job?
[L1240] [48:24.80] Well, because that way we can get great
[L1241] [48:26.64] tooling. Then we can use Visual Studio
[L1242] [48:29.36] and we can have projects and we can have
[L1243] [48:31.60] type checking and we can have code
[L1244] [48:33.84] refactoring and navigation and we can
[L1245] [48:35.84] write interfaces and people can
[L1246] [48:37.52] understand how this all works. And I'm
[L1247] [48:40.00] like, "Wow,
[L1248] [48:42.88] is JavaScript really that busted?" And
[L1249] [48:45.20] and you're saying like the the way you
[L1250] [48:47.04] want to fix that problem is by
[L1251] [48:48.96] abandoning JavaScript, treating it as an
[L1252] [48:50.96] instruction language, right? And then
[L1253] [48:52.72] having a code generator target it. I'm
[L1254] [48:54.96] like, couldn't we like fix JavaScript?
[L1255] [48:57.52] Wouldn't that be better? Do you know
[L1256] [48:59.68] what I mean? And that's how Typescript
[L1257] [49:01.76] kind of got off the ground, right? It
[L1258] [49:03.28] was like, gosh, there's something here
[L1259] [49:05.68] that's really broken that needs to be
[L1260] [49:07.60] fixed, right? and when it comes to
[L1261] [49:10.72] JavaScript tooling
[L1262] [49:12.72] >> and that's what we set out to do.
[L1263] [49:14.80] >> You know, one thing I thought would be
[L1264] [49:16.00] interesting is in one of the talks that
[L1265] [49:18.32] you gave, you said that you believe that
[L1266] [49:21.84] the speed of your tooling is more
[L1267] [49:24.32] important now because of AI and I want
[L1268] [49:28.24] to hear thoughts on why is that the
[L1269] [49:30.08] case? Well, more and more our workflows
[L1270] [49:32.48] now are are dominated by agents that are
[L1271] [49:35.60] like running away in the background,
[L1272] [49:38.48] right? Right. I mean, like writing code
[L1273] [49:40.40] for you and they make mistakes just like
[L1274] [49:44.24] we do, but they but they but you know,
[L1275] [49:46.24] but you can have as many of them as you
[L1276] [49:47.76] want. So there are like many many more
[L1277] [49:49.76] little workers in the ecosystem writing
[L1278] [49:52.96] much more code, right? And that whole
[L1279] [49:55.60] workflow is like LLMs already have have
[L1280] [49:59.12] performance challenging is and then if
[L1281] [50:00.88] you add like if if you're writing code
[L1282] [50:02.48] in a big project and you have to like
[L1283] [50:04.00] type check it and takes two minutes
[L1284] [50:05.68] every time the LLM writes something. Do
[L1285] [50:07.52] you know what I mean? That's horrible,
[L1286] [50:09.04] right? So So making that go faster is is
[L1287] [50:13.36] a big benefit.
[L1288] [50:14.64] >> Yeah. Absolutely. I guess because it's
[L1289] [50:16.64] it's hammering away.
[L1290] [50:18.08] >> Yeah. Because I mean like like well we
[L1291] [50:21.52] all know LLMs they they like to use GP
[L1292] [50:24.48] and and whatever right but then they're
[L1293] [50:26.56] also smart enough now to realize that if
[L1294] [50:28.64] you're like trying to change this
[L1295] [50:30.48] property called version and like every
[L1296] [50:33.68] other object has a version property. You
[L1297] [50:36.96] can't just grip for version and then go
[L1298] [50:38.96] rename it to something else because like
[L1299] [50:40.72] you're breaking all these other
[L1300] [50:42.80] interfaces that have a version in them,
[L1301] [50:44.64] right? So you got to do semantic search
[L1302] [50:46.72] and the only thing that can do semantic
[L1303] [50:48.40] search is a compiler and so you got to
[L1304] [50:52.00] use the compiler through typically
[L1305] [50:54.56] through LSP through language services or
[L1306] [50:57.12] through our our command line tool that
[L1307] [50:59.36] would give you the equivalent right and
[L1308] [51:01.36] so more and more AI is doing that um and
[L1309] [51:06.56] that means you know compilers run at you
[L1310] [51:09.60] don't you may not even see that they're
[L1311] [51:11.04] running but they're running
[L1312] [51:13.44] and they're doing work on on your
[L1313] [51:14.72] behalf. Yeah.
[L1314] [51:16.40] >> When you talk about AI, it's very
[L1315] [51:20.08] realistic and grounded in the software
[L1316] [51:22.40] engineering. And so I thought it might
[L1317] [51:24.72] be interesting to uh run some common AI
[L1318] [51:28.48] takes that I hear from the internet and
[L1319] [51:31.20] you get your sense of how accurate is
[L1320] [51:33.44] this? What are your thoughts on when or
[L1321] [51:35.68] if it'll be true? Okay. Okay. So the
[L1322] [51:38.16] first one that I've heard um this is
[L1323] [51:40.48] more common at the end of last year is
[L1324] [51:42.24] that you know AI is going to write 90
[L1325] [51:45.36] plus% of the code you know within a
[L1326] [51:47.92] year. Um curious what you think on that.
[L1327] [51:51.52] >> Well for certain classes of apps that
[L1328] [51:54.00] that might like all divide code coded
[L1329] [51:56.24] apps they're writing 100% of the code
[L1330] [51:58.00] right and and there's an awful lot of
[L1331] [51:59.44] that being written.
[L1332] [52:01.60] Are they going to write 90% of the high
[L1333] [52:03.76] quality code on the internet? I don't
[L1334] [52:05.76] know about that. Um so the the thing is
[L1335] [52:09.92] like 90% of what the volume of written
[L1336] [52:12.72] code is just like going like that right
[L1337] [52:15.36] now right because AI writes so much code
[L1338] [52:18.72] so [laughter]
[L1339] [52:19.44] so in a sense that's a self-fulfilling
[L1340] [52:21.68] prophecy right I mean but [snorts] but
[L1341] [52:24.16] but when it comes to like
[L1342] [52:27.76] the super high quality code that no one
[L1343] [52:29.92] has ever written before um it's not
[L1344] [52:32.96] clear to me that AI is going to write
[L1345] [52:34.40] 90% of that. So when you think about
[L1346] [52:36.48] cases that AI is not writing all the
[L1347] [52:40.16] code, maybe some examples of the super
[L1348] [52:42.32] high quality stuff, what is that?
[L1349] [52:44.64] >> Well,
[L1350] [52:46.16] I mean it's it's algorithms that no one
[L1351] [52:48.24] has ever seen before, for example, or or
[L1352] [52:50.72] particular solutions like I mean I I
[L1353] [52:52.88] know that AI could not write our
[L1354] [52:55.36] compiler, the TypeScript compiler. It it
[L1355] [52:57.28] just can't. I mean we've tried it. It it
[L1356] [53:00.72] can't do it. Um and I'm not asking it to
[L1357] [53:03.68] either. I mean, I'm not expecting it to
[L1358] [53:05.76] either. Um, but but our compiler is also
[L1359] [53:10.56] not a typical piece of code. I mean,
[L1360] [53:12.80] that's why it's bad at writing it
[L1361] [53:14.32] because it's seen none of it in the
[L1362] [53:16.16] training set. Well, I've seen some
[L1363] [53:17.36] compilers, but not like this one. Not
[L1364] [53:19.28] with these concepts, not with done the
[L1365] [53:21.60] way that that we're doing it, right? And
[L1366] [53:23.68] so, it's just not a good fit there. AI
[L1367] [53:26.80] we we we can't forget that AI is at
[L1368] [53:30.64] heart a big stochastic machine that has
[L1369] [53:33.36] memorized the entire internet, right?
[L1370] [53:35.36] And and is ability and has an ability to
[L1371] [53:37.76] extrapolate somewhat over what it's
[L1372] [53:40.08] memorized, right? Um but if it hasn't
[L1373] [53:43.04] seen it before, it's it's it's not
[L1374] [53:45.84] necessarily going to be all that good at
[L1375] [53:47.84] at doing it. Um it's getting better. I
[L1376] [53:50.32] mean, I'm not saying it's it's not
[L1377] [53:51.76] impressive. I it's it's wildly
[L1378] [53:53.60] impressive what it can do, but I just
[L1379] [53:57.44] think there's a long way still to it's
[L1380] [54:00.24] doing all of it.
[L1381] [54:02.40] >> And I don't know that we ever get there.
[L1382] [54:04.64] I hope we don't because then what's the
[L1383] [54:06.56] point of humans anymore then? I mean,
[L1384] [54:08.08] it's [laughter]
[L1385] [54:09.60] >> Well, I see this take often, too, is um
[L1386] [54:12.40] you know, you won't need to use an IDE
[L1387] [54:15.92] within the year or you don't need to
[L1388] [54:17.92] read the code anymore.
[L1389] [54:19.44] >> Well, good luck to you. I mean, if
[L1390] [54:21.28] you're going to hand AI the keys,
[L1391] [54:24.40] I mean, then all bets are off, right? I
[L1392] [54:26.24] mean, the minute AI you can't convince
[L1393] [54:28.08] AI to fix this issue or this new feature
[L1394] [54:31.12] that you want built, what are you going
[L1395] [54:32.88] to do? I mean, if you don't understand
[L1396] [54:36.88] what what's below, right, that's one
[L1397] [54:39.84] problem. The other problem is, let's say
[L1398] [54:41.12] a user comes to you and goes, your app
[L1399] [54:43.68] just stole my bank account. I'm well,
[L1400] [54:47.04] it's going to sue you. It's not. They're
[L1401] [54:48.96] going to sue you, not the AI. I mean,
[L1402] [54:50.88] it's like at the end of the day, someone
[L1403] [54:52.96] has to take responsibility for what AI
[L1404] [54:55.20] is doing. And if you're giving it the
[L1405] [54:57.52] keys, well, it's on you, you know, but
[L1406] [55:00.56] but I don't know. I personally would not
[L1407] [55:05.20] feel comfortable. I wouldn't be able to
[L1408] [55:06.88] go to sleep at night. I mean, if I
[L1409] [55:09.04] didn't understand what it is that I am
[L1410] [55:11.12] vouching for.
[L1411] [55:13.28] Why is there such a big difference
[L1412] [55:14.96] between this opinion and what I see from
[L1413] [55:20.00] maybe people who work at Anthropic?
[L1414] [55:22.64] >> Well, the difference is all I'm saying
[L1415] [55:25.04] here is not that AI can't do amazing
[L1416] [55:27.52] things. It does it can it does that
[L1417] [55:30.40] every day. But but people love these
[L1418] [55:34.24] like take it all the way to 100%. Right?
[L1419] [55:36.80] And that's where I get off the bus a
[L1420] [55:39.60] little bit, right? I think, oh yeah,
[L1421] [55:40.96] okay, fine. We can get we can get higher
[L1422] [55:42.88] and higher percentage but there still
[L1423] [55:45.52] has to be someone understanding what's
[L1424] [55:48.32] going on and how it's relevant to our
[L1425] [55:50.08] business problem and how it relates to
[L1426] [55:52.16] what our organization is doing and like
[L1427] [55:54.24] I mean there's so many other things that
[L1428] [55:55.92] have to be connected that it's I think
[L1429] [55:57.68] it's wrong to just view it as AI did it
[L1430] [56:00.88] all and we were completely unnecessary
[L1431] [56:02.88] you know and
[L1432] [56:04.72] >> yeah the next one I was going to ask you
[L1433] [56:06.24] was you know three years from now will
[L1434] [56:08.72] AI replace junior software engineers or
[L1435] [56:11.36] what junior software engineers do today.
[L1436] [56:13.44] >> Well, if it does, then how do you ever
[L1437] [56:15.28] get senior software engineers,
[L1438] [56:18.16] >> right? I mean, it's it's like I don't
[L1439] [56:20.40] think so. Well, I not unless you also
[L1440] [56:22.88] believe that you will be able to do your
[L1441] [56:24.80] business three years later than that
[L1442] [56:27.20] without any senior software engineers,
[L1443] [56:30.16] >> right?
[L1444] [56:30.72] >> Because where are they going to come
[L1445] [56:31.68] from? You got to train them. I mean and
[L1446] [56:35.60] but to me I think maybe one thing that
[L1447] [56:39.76] to some extent has happened is that for
[L1448] [56:41.76] certain classes of programmers the the
[L1449] [56:43.68] the pyramid has narrowed at the bottom
[L1450] [56:45.68] right there are fewer people coming in
[L1451] [56:48.48] um and we are wanting them to advance
[L1452] [56:51.12] higher up faster um so that they can get
[L1453] [56:55.20] to this more supervisory role right I
[L1454] [56:58.16] think the the craft of being a software
[L1455] [57:01.12] engineer is definitely changing from
[L1456] [57:03.92] you're you're typing in lines of code to
[L1457] [57:08.00] you're having agents type in lines of
[L1458] [57:10.16] code and you are reviewing the work of
[L1459] [57:12.16] the agents, right? And so so you do more
[L1460] [57:16.00] reviewing, less typing.
[L1461] [57:18.64] Um, and some people love that, you know,
[L1462] [57:21.60] I mean, and and and and really are
[L1463] [57:23.52] fantastic at at that workflow, right?
[L1464] [57:26.16] But it's it's a change in nature of of
[L1465] [57:28.32] what what the job looks like as a
[L1466] [57:30.56] programmer. And this tool that you now
[L1467] [57:32.96] have in a toolbox is having that impact,
[L1468] [57:35.44] right? But it is but a tool and there
[L1469] [57:38.48] are still programmers involved in the in
[L1470] [57:40.88] the process that I firmly believe.
[L1471] [57:43.12] >> It sounds like you enjoy typing out the
[L1472] [57:45.84] code. Would you be less happy if five
[L1473] [57:48.32] years from now
[L1474] [57:49.12] >> I I I for for 40 50 years I have enjoyed
[L1475] [57:52.80] typing out code. Um
[L1476] [57:55.76] I'm actually there there some and so I
[L1477] [57:59.20] will continue to type certain parts of
[L1478] [58:01.04] the code, you know, but there are other
[L1479] [58:02.80] parts of the code that I don't
[L1480] [58:04.08] particularly care to type. I don't care
[L1481] [58:05.84] to type in tests and follow all the
[L1482] [58:08.32] rigor of the particular testing
[L1483] [58:10.24] framework. Heck no. If I can farm that
[L1484] [58:12.00] out to AI, happy me, you know. Um I do
[L1485] [58:16.72] think reviewing has always been harder
[L1486] [58:18.72] for me. It's harder for me to like spend
[L1487] [58:20.40] time on reviewing other people's code
[L1488] [58:22.16] than it is you know writing the code.
[L1489] [58:24.56] But I also think that over time we will
[L1490] [58:27.04] we can make that process of reviewing
[L1491] [58:29.28] code much more ergonomic than it is
[L1492] [58:32.16] today. Right? I mean often today you
[L1493] [58:34.24] just get here's like the list of the
[L1494] [58:35.52] files that were changed and here are the
[L1495] [58:37.04] deltas. You figure it up, right? I mean
[L1496] [58:40.08] AI could help us more there by
[L1497] [58:41.76] explaining what the changes are and and
[L1498] [58:43.76] whatever. And so I I think we're going
[L1499] [58:45.28] to get better at this. It's going to get
[L1500] [58:46.56] more interesting, but it will change the
[L1501] [58:49.04] nature of of the craft.
[L1502] [58:53.04] You said that you've been writing code
[L1503] [58:55.04] for 40 maybe 50 years.
[L1504] [58:58.80] >> What is the hardest piece of code you've
[L1505] [59:01.44] ever written or what's the most
[L1506] [59:02.56] technically challenging thing you've
[L1507] [59:04.08] ever done?
[L1508] [59:05.76] >> There there are so many things that in
[L1509] [59:08.80] their time were challenging, you know.
[L1510] [59:10.96] Um
[L1511] [59:13.36] I mean this last project we worked on,
[L1512] [59:15.76] we knew that like like you know sort of
[L1513] [59:18.72] the easy part was getting the native
[L1514] [59:20.32] code. it's just like just just move it
[L1515] [59:22.56] to this other language, right? But then
[L1516] [59:25.28] this taming this beast called uh shared
[L1517] [59:29.28] memory concurrency and and getting the
[L1518] [59:33.20] compiler to use like as many CPUs as
[L1519] [59:36.72] there are available on your box, right?
[L1520] [59:40.80] That is not a simple problem to solve in
[L1521] [59:42.88] a in a in a compiler because we're all
[L1522] [59:45.12] taught to write sequential stuff, right?
[L1523] [59:48.16] I mean first you do this then you do
[L1524] [59:49.60] this but how do you do all of this at
[L1525] [59:51.60] the same time and then share the data
[L1526] [59:53.92] structures afterwards without anyone
[L1527] [59:55.60] like accidentally modifying the other
[L1528] [59:57.12] guy's data structure and you know how do
[L1529] [59:59.27] [snorts] you in the cases where you have
[L1530] [01:00:00.72] to do that how do you then synchronize
[L1531] [01:00:02.08] it and avoid deadlocks and race
[L1532] [01:00:03.60] conditions and and and whatever right
[L1533] [01:00:05.52] this it was it was tricky uh there were
[L1534] [01:00:08.72] some good technical problems uh that
[L1535] [01:00:10.56] that we licked that I think we can be
[L1536] [01:00:12.40] proud of you know but
[L1537] [01:00:14.32] >> what about when hardware was more
[L1538] [01:00:16.48] constrained earlier in your career Is
[L1539] [01:00:18.32] there any wacky thing you had to do to
[L1540] [01:00:21.44] kind of, you know, make it work?
[L1541] [01:00:23.76] >> Oh, totally. I mean, when I started it
[L1542] [01:00:26.80] was a like being a programmer was a very
[L1543] [01:00:28.88] very different thing, right? I mean, I
[L1544] [01:00:30.48] started out with with 8-bit micros that
[L1545] [01:00:32.88] had Microsoft basic in ROM, right? And
[L1546] [01:00:35.68] and the basic interpreter and and you
[L1547] [01:00:38.24] could buy these books and type in these
[L1548] [01:00:41.12] Star Wars games or or or whatever. They
[L1549] [01:00:43.68] were all text, you know, there was just
[L1550] [01:00:45.04] scrolling and and telling you there's
[L1551] [01:00:46.64] Klingons over in that C quadrant, you
[L1552] [01:00:48.96] know, and K4, you know, you got to
[L1553] [01:00:51.52] whatever, right? Um,
[L1554] [01:00:55.44] but I got fascinated with understanding
[L1555] [01:00:58.48] how it was all put together and and got
[L1556] [01:01:00.56] and and quickly learned how to write uh
[L1557] [01:01:03.36] assembly code and Turbo Pascal, the
[L1558] [01:01:06.48] first product I worked on, was all
[L1559] [01:01:08.16] written in Z80 assembly code. um the
[L1560] [01:01:11.36] compiler, the editor, the runtime
[L1561] [01:01:12.88] library, everything was assembly. Um and
[L1562] [01:01:16.24] writing structured a compiler in
[L1563] [01:01:18.96] assembly code is like that that was that
[L1564] [01:01:21.20] was like took a lot of fiddling, you
[L1565] [01:01:24.00] know, and I mean and you were counting
[L1566] [01:01:26.16] like okay, I think I can I need to we
[L1567] [01:01:28.72] need to squeeze this into this EPROM and
[L1568] [01:01:30.88] then there's only 12K, you know, and I'm
[L1569] [01:01:33.44] I'm 20 bytes over budget here. Oh, but I
[L1570] [01:01:36.40] can make this jump this long jump
[L1571] [01:01:38.96] instead. I could jump to this short jump
[L1572] [01:01:40.64] and that then jumps to that jump and
[L1573] [01:01:42.40] then I could save one and that's one
[L1574] [01:01:44.00] bite saved. Okay. You know, moving right
[L1575] [01:01:46.32] along. [laughter] I mean, and you you
[L1576] [01:01:48.24] would you would you you were just like
[L1577] [01:01:49.60] sitting there and fiddling, you know, it
[L1578] [01:01:51.84] was it was a craft. It was like
[L1579] [01:01:53.28] woodworking almost. I mean, it was just
[L1580] [01:01:55.52] so different from what we do now, right?
[L1581] [01:01:57.52] Everything is like it's bottomless pits
[L1582] [01:02:00.24] of capacity and and and and bottomless
[L1583] [01:02:02.80] pits of expectation from users, right?
[L1584] [01:02:05.92] Is there a top technical book
[L1585] [01:02:07.44] recommendation you have for software
[L1586] [01:02:09.04] engineers? I usually recommend the same
[L1587] [01:02:10.88] but the the one book that was like the
[L1588] [01:02:13.20] it book for me when I was younger and
[L1589] [01:02:15.76] it's called algorithms plus data
[L1590] [01:02:17.44] structures equals programs by Nicholas V
[L1591] [01:02:20.48] uh the inventor of Pascal and then later
[L1592] [01:02:23.84] modular and Oberon and whatever and it's
[L1593] [01:02:26.16] a
[L1594] [01:02:27.76] it's a book that is
[L1595] [01:02:30.56] light on
[L1596] [01:02:32.96] math and symbolism uh and rich in
[L1597] [01:02:36.64] instructive examples and good
[L1598] [01:02:38.64] explanation. ations about how data
[L1599] [01:02:40.56] structures work. I mean, that's how I
[L1600] [01:02:42.16] learned about hashts, right? I mean,
[L1601] [01:02:44.08] like when you're self-taught, you don't
[L1602] [01:02:46.00] know about hashts. You sort of know
[L1603] [01:02:48.16] about linked lists, right? And fine. So,
[L1604] [01:02:50.72] in the original version of Turop Pascal,
[L1605] [01:02:53.20] all the symbol tables were just well,
[L1606] [01:02:55.04] they were just linked lists, you know,
[L1607] [01:02:57.12] or whatever. And then of course as you
[L1608] [01:02:58.80] had many local variables well you're
[L1609] [01:03:02.40] you're you're you're going exponential
[L1610] [01:03:04.64] in search time to you know and then I
[L1611] [01:03:07.28] read about these hash tables and like
[L1612] [01:03:08.96] wow what you mean I can like just do
[L1613] [01:03:11.20] this and then like it's it's basically
[L1614] [01:03:13.92] like linear lookup time and implemented
[L1615] [01:03:17.12] and the compilement twice as fast right
[L1616] [01:03:19.60] I'm like holy cow [laughter]
[L1617] [01:03:22.08] you know that was useful reading do do
[L1618] [01:03:24.48] you know what I mean so I was always
[L1619] [01:03:25.92] like the engineer it like that that I
[L1620] [01:03:29.12] mean and and understanding how to do
[L1621] [01:03:31.36] error recovery. He explains that in like
[L1622] [01:03:33.20] how you construct a simple compiler and
[L1623] [01:03:35.28] then like you know and it's it's
[L1624] [01:03:38.16] a it was for me a great book but and now
[L1625] [01:03:41.44] it's actually like I mean it's just a
[L1626] [01:03:43.04] big PDF you can download it out there um
[L1627] [01:03:46.48] it's out of print since 40 30 years.
[L1628] [01:03:49.60] Yeah. Last question for you is with all
[L1629] [01:03:52.24] the experience that you have now, if you
[L1630] [01:03:54.48] could go back to yourself when you just
[L1631] [01:03:56.00] entered the industry and give yourself
[L1632] [01:03:57.84] some advice, what would you say?
[L1633] [01:04:01.52] >> Well, I a couple of things maybe like we
[L1634] [01:04:04.08] talked about being a team player, you
[L1635] [01:04:05.84] know, I I I would have probably tried to
[L1636] [01:04:07.76] educate myself a bit more about that to
[L1637] [01:04:09.76] to begin with. Um, I think also
[L1638] [01:04:14.80] one thing in in retrospect is like
[L1639] [01:04:18.88] don't let people tell you that it can't
[L1640] [01:04:20.80] be done. When they tell you it can't be
[L1641] [01:04:23.52] done, it's because they can't do it.
[L1642] [01:04:25.60] That doesn't mean that you couldn't
[L1643] [01:04:27.28] possibly do it. Do do you know what I
[L1644] [01:04:29.12] mean? So, so don't let that discourage
[L1645] [01:04:31.12] you. Is there a project where you
[L1646] [01:04:34.88] someone said you couldn't do it and then
[L1647] [01:04:36.80] you did it and that's how you
[L1648] [01:04:38.24] >> Well, I think the first thing I worked
[L1649] [01:04:39.84] on like Turbo Pascal, people were
[L1650] [01:04:41.44] telling me whenever we told them here's
[L1651] [01:04:43.84] what we have, they said that can't be
[L1652] [01:04:45.28] done. That's like nah, you guys are you
[L1653] [01:04:48.08] full of That's like not possible,
[L1654] [01:04:50.32] you know. [laughter]
[L1655] [01:04:51.52] Well, it was. And I didn't know that it
[L1656] [01:04:54.56] wasn't possible, right?
[L1657] [01:04:56.48] >> Awesome. Well, thank you for your time.
[L1658] [01:04:57.68] I really appreciate it, Andrew.
[L1659] [01:04:58.64] >> You're welcome. No, this is a lot of
[L1660] [01:04:59.92] fun. Hey, thank you for watching this
[L1661] [01:05:01.92] podcast. If you liked it and you want to
[L1662] [01:05:03.52] see the show grow, please support with a
[L1663] [01:05:05.84] comment or a like. Also, if you have any
[L1664] [01:05:08.80] recommendations for people you want me
[L1665] [01:05:10.48] to bring on, please drop a comment.
[L1666] [01:05:13.04] Guests like Barbara Liskoff, Mike
[L1667] [01:05:15.28] Stonereaker, Mark Brooker, these were
[L1668] [01:05:17.68] all people that I brought on because
[L1669] [01:05:19.68] someone left a comment. On another note,
[L1670] [01:05:21.92] aside from the podcast, I'm working on
[L1671] [01:05:23.84] building the ergonomic keyboard that I
[L1672] [01:05:25.76] wish existed. Here's a glance at the
[L1673] [01:05:27.92] prototype. It's a split keyboard, so
[L1674] [01:05:30.16] there's two sides. This is in the case,
[L1675] [01:05:32.56] but yeah, we launched on Kickstarter and
[L1676] [01:05:34.64] we hit our goal within eight hours of
[L1677] [01:05:36.48] launching. I really appreciate it if you
[L1678] [01:05:38.24] were one of the people who grabbed one
[L1679] [01:05:39.68] of the early units. Um, we're now
[L1680] [01:05:41.84] working on the long journey of building
[L1681] [01:05:43.68] the tooling now. And so, if you still
[L1682] [01:05:45.28] want to pick one up, I've left the late
[L1683] [01:05:47.44] pledges open on Kickstarter, so you can
[L1684] [01:05:49.92] grab one there. I'll put a link in the
[L1685] [01:05:51.60] description. Thank you again for
[L1686] [01:05:53.76] watching the podcast and I'll see you in
[L1687] [01:05:56.00] the next
