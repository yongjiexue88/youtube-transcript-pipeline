# Creator of TypeScript: Why We Chose Go For Our Rewrite | Anders Hejlsberg

Source ID: source-a0de28000368bd2f
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_TypeScript_Why_We_Chose_Go_For_Our_Rewrite_Anders_Hejlsberg_en.txt
Video: https://www.youtube.com/watch?v=rX9kkMonrG8

[L10] [00:00.16] So with the the native rewrite of this
[L11] [00:03.20] originally fully JavaScript compiler,
[L12] [00:06.40] what was the problem you were trying to
[L13] [00:08.08] solve with the rewrite and why did you
[L14] [00:10.96] end up write rewriting it in native
[L15] [00:12.96] code?
[L16] [00:13.84] >> Well, I mean the the problem we were
[L17] [00:15.60] trying to solve it's real simple
[L18] [00:17.12] performance and scalability.
[L19] [00:18.64] >> JavaScript was never really optimized
[L20] [00:21.92] for compute inensive workloads like
[L21] [00:24.24] compilers, right? JavaScript is more
[L22] [00:26.88] about creating UI that runs in a
[L23] [00:29.20] browser. Was originally intended for
[L24] [00:31.60] just like maybe a 100 lines of code, but
[L25] [00:34.08] now of course it's gotten to be a lot
[L26] [00:35.68] more. Um, but it's not it's not a place
[L27] [00:39.52] that that you would optimize for um for
[L28] [00:43.92] the kind of workload that that we are.
[L29] [00:46.96] So in JavaScript, first of all, you pay
[L30] [00:49.52] a 2 to 3x perf penalty compared to
[L31] [00:52.40] native code. I mean it depends on on the
[L32] [00:54.48] workload you know but that's but if if
[L33] [00:56.72] you're doing compute that's about where
[L34] [00:58.64] it's at. Um and then secondly in
[L35] [01:02.08] JavaScript there are a lot of
[L36] [01:04.24] restrictions around use of concurrency.
[L37] [01:06.72] Uh JavaScript was always engineered in
[L38] [01:09.92] fact to be a single threaded language.
[L39] [01:11.76] That's why we have callbacks and async
[L40] [01:13.84] and and and whatever. It's because you
[L41] [01:15.60] can't spin up threads. Um, and that's a
[L42] [01:19.12] good thing mostly because concurrency in
[L43] [01:22.56] a language with mutable data is very
[L44] [01:25.60] very hard because you can have races and
[L45] [01:27.36] deadlocks and all of this good stuff,
[L46] [01:29.28] right? That's why functional programming
[L47] [01:31.76] languages are easier with concurrency
[L48] [01:34.24] because all the data is immutable and
[L49] [01:36.00] it's much easier to reason about. Um
[L50] [01:40.00] so JavaScript doesn't give you access to
[L51] [01:43.20] concurrency other than web workers and
[L52] [01:46.32] but web workers can't share data between
[L53] [01:49.12] each other other than by remoting it. So
[L54] [01:51.20] you can you can have one web worker
[L55] [01:53.20] compute some something but if it wants
[L56] [01:54.96] to give it to some other web worker it
[L57] [01:57.36] has to turn it into JSON or it can't
[L58] [01:59.76] just hand it objects and that means you
[L59] [02:03.20] can't have one worker compute some data
[L60] [02:06.88] structure and then have someone else use
[L61] [02:09.04] it. In other words, you can't have
[L62] [02:10.96] shared memory concurrency. And really
[L63] [02:13.44] that's what we wanted in order to gain
[L64] [02:16.96] all of the perf that we were leaving on
[L65] [02:19.04] the table by not utilizing multi-core
[L66] [02:21.36] CPUs that everyone has today, right?
[L67] [02:24.00] Because Moore's law has stopped giving
[L68] [02:25.68] us faster CPUs. It's giving us more CPUs
[L69] [02:29.92] and we got to like find ways to use them
[L70] [02:31.84] in our in our compute intensive
[L71] [02:33.44] workloads or else we're leaving money on
[L72] [02:35.04] the table. And so we were leaving money
[L73] [02:36.48] on the table in multiple ways, right?
[L74] [02:39.28] And so native code and that was why we
[L75] [02:42.16] we looked for a language that
[L76] [02:45.84] would get us out of both of those binds.
[L77] [02:48.08] It had to be native and it had to have
[L78] [02:50.00] access to shared memory concurrency.
[L79] [02:52.40] >> I saw for the language choice you went
[L80] [02:54.32] with Go. And when I think of all the
[L81] [02:57.04] systems languages, the ones that are
[L82] [02:58.72] often hot or maybe you know Rust or
[L83] [03:01.76] Zigg, why did you choose Go for the
[L84] [03:04.88] native rewrite? I think the decision
[L85] [03:07.12] process was actually pretty structured.
[L86] [03:10.32] You know, the first decision we made was
[L87] [03:13.76] we're not going to rewrite. We're going
[L88] [03:15.36] to port because only by porting can we
[L89] [03:18.80] preserve the semantics and the
[L90] [03:20.56] algorithms and the exact behavior of our
[L91] [03:23.68] existing compiler which everyone depends
[L92] [03:25.68] on for backwards compatibility. Now we
[L93] [03:28.24] could have we could have cleaned the
[L94] [03:30.32] slate and started completely from
[L95] [03:31.84] scratch but we would have come we would
[L96] [03:33.60] have come up with a different language
[L97] [03:34.88] in the sense that it would give you
[L98] [03:36.88] different errors or behave differently
[L99] [03:38.64] in certain situations where it has to
[L100] [03:40.64] make choices between multiple
[L101] [03:43.44] possibilities and and what have you.
[L102] [03:45.44] Right? So we wanted to port and that
[L103] [03:48.56] meant our code makes certain assumptions
[L104] [03:51.84] like our code for example assumes the
[L105] [03:53.68] existence of garbage collection. It
[L106] [03:56.80] assumes the existence of first class um
[L107] [04:01.76] uh treatment of functions. You know, you
[L108] [04:03.76] can have functions within functions and
[L109] [04:05.20] you can close over over out of state and
[L110] [04:07.60] so forth. Um and as we evaluated all of
[L111] [04:11.28] these,
[L112] [04:12.80] go was was the one that checked the most
[L113] [04:14.88] boxes. You know, it gives us it gives us
[L114] [04:19.28] very robust and mature native code
[L115] [04:21.92] generation on all major platforms. It
[L116] [04:25.04] has garbage collection and it has access
[L117] [04:28.80] excellent access to shared memory
[L118] [04:30.56] concurrency. Um, and those were like the
[L119] [04:33.04] high order bits that we wanted to check.
[L120] [04:34.96] And every other language had something
[L121] [04:39.44] that kind of worked against those
[L122] [04:40.96] objectives. So for this particular
[L123] [04:42.72] workload, Go was the right was the right
[L124] [04:44.56] choice for us and it's worked out well.
[L125] [04:47.04] >> If you think about Rusk, what didn't it
[L126] [04:50.24] have that if it had it, you would have
[L127] [04:52.56] picked it? I mean I think there are
[L128] [04:54.00] there are there are two things um it
[L129] [04:56.72] doesn't have uh garbage collection
[L130] [05:00.32] it's done manually you know uh well or
[L131] [05:03.84] it's done through the borrow checker but
[L132] [05:05.76] the borrow checker doesn't allow
[L133] [05:07.44] circular data structures and our
[L134] [05:10.00] compiler is chalk full of circular data
[L135] [05:12.88] structures we have trees with parent
[L136] [05:14.64] pointers we have types that are
[L137] [05:16.08] recursive we have symbols that refer I
[L138] [05:18.48] mean it's everywhere and like I said if
[L139] [05:20.96] we had chosen to rewrite we could
[L140] [05:22.88] probably solved all of that, but it
[L141] [05:25.68] wouldn't have been just porting the
[L142] [05:27.28] code. It would also have been like
[L143] [05:28.56] solving a whole bunch of new problems
[L144] [05:30.32] that we had bought ourselves by by going
[L145] [05:32.24] that route. We tried [laughter]
[L146] [05:35.44] and it just wasn't feasible, you know,
[L147] [05:38.00] uh and and and so so we were we were
[L148] [05:40.40] just trying to optimize for, you know,
[L149] [05:43.28] doing as little work as possible to get
[L150] [05:45.44] us to the payout, which is which and
[L151] [05:49.20] honestly, Rust is no better when it
[L152] [05:51.28] comes to like the quality of the
[L153] [05:52.72] generated code or the or the the
[L154] [05:55.04] concurrency gains that we could have
[L155] [05:56.48] gotten out of it.
[L156] [05:58.56] Go just it's great. I mean, so so we got
[L157] [06:02.48] we got all the bennies with for less
[L158] [06:04.32] work by by going that route.
[L159] [06:06.40] >> I know some languages they're when you
[L160] [06:08.64] say they're garbage collected, they
[L161] [06:11.12] >> there's something in the the language
[L162] [06:13.44] itself that is doing garbage collection,
[L163] [06:15.76] but um there's also independent
[L164] [06:19.28] libraries that can provide garbage
[L165] [06:21.20] collection, right?
[L166] [06:23.20] There is, but it it but it comes often
[L167] [06:26.08] with a whole bunch of restrictions and
[L168] [06:28.48] and and it doesn't come necessarily with
[L169] [06:31.52] the safety guarantees that we were
[L170] [06:33.04] looking for. I mean like Go is type safe
[L171] [06:35.68] and memory safe. uh meaning that you
[L172] [06:38.40] don't get to just like have stray
[L173] [06:40.96] pointers or or whatever where rust you
[L174] [06:44.08] can do ref counting or you can do you
[L175] [06:46.08] can do all sorts of different strategies
[L176] [06:48.24] but there's always like that little bit
[L177] [06:50.88] of unsafe where you have to like do this
[L178] [06:53.36] in order to make it all work you know uh
[L179] [06:56.00] where where if garbage collection is
[L180] [06:59.28] engineered into the language it really
[L181] [07:01.28] is a a separate concern that is you you
[L182] [07:04.08] you don't you don't have to do anything
[L183] [07:06.56] special in I mean of course you you you
[L184] [07:09.60] have to like not hold on to data that
[L185] [07:11.92] you no longer need and whatever you know
[L186] [07:13.84] but that's true of ref counting as well
[L187] [07:15.76] right but but it is inherent in in the
[L188] [07:18.96] language
