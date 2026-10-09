Chunk 1; segments 1–217. 

# Creator of Scala: Rust, Zig, Python vs Scala | Martin Odersky

Source ID: source-7f09fb95f7d0e9d0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Scala_Rust,_Zig,_Python_vs_Scala_Martin_Odersky_en.txt
Video: https://www.youtube.com/watch?v=SyltKRA8ErU

[L10] [00:00.08] when you compare you know Rust or Go
[L11] [00:03.44] with Scola what are the pros and cons of
[L12] [00:06.72] the different language designs what's
[L13] [00:08.56] something that Rust does better than
[L14] [00:10.40] Scola something that Scola does better
[L15] [00:12.56] than Rust
[L16] [00:13.44] >> so Rust is closer to the metal you have
[L17] [00:15.68] better performance guarantees I guess uh
[L18] [00:18.88] the fact that Scala is a garbage
[L19] [00:20.32] collected language means that you always
[L20] [00:22.56] have some pauses I mean garbage
[L21] [00:24.64] collection collectors have become quite
[L22] [00:26.64] quite capable I mean they're brilliant
[L23] [00:28.96] and the pauses are really very very
[L24] [00:30.72] small but it's fact it's it's a fact
[L25] [00:32.96] that you do need a big chunk of memory
[L26] [00:36.16] to run fast and I guess Rust could could
[L27] [00:39.60] run in much much smaller memory so I
[L28] [00:41.92] believe that's that's better for
[L29] [00:43.68] embedded systems and things like that I
[L30] [00:46.08] believe right now rust is actually
[L31] [00:47.76] overused because a lot of people push
[L32] [00:50.16] sort of rush rust for things higher
[L33] [00:52.48] higher up in the stack where you a
[L34] [00:55.28] garbage collector is fine but uh
[L35] [00:57.52] essentially you you still want to write
[L36] [00:59.60] code without and that is for me a bit an
[L37] [01:04.16] exercise in
[L38] [01:06.64] uh I don't know just intellectual that I
[L39] [01:09.44] can do it I I don't think really think
[L40] [01:11.52] there's a there's a big sense in it that
[L41] [01:13.92] if you have the memory for a garbage
[L42] [01:15.52] collector you should absolutely use one
[L43] [01:17.36] because it makes a lot of things uh
[L44] [01:19.68] simpler so yes of course if given enough
[L45] [01:23.60] uh brains I can write code around and I
[L46] [01:26.72] can do that but why should you I I mean
[L47] [01:28.80] it it it it can be much simpler.
[L48] [01:31.60] So that was for R. Uh for go is um sort
[L49] [01:36.00] of a language a bit that that lags
[L50] [01:39.52] behind. I mean was intentionally
[L51] [01:41.28] designed to be to be very very small and
[L52] [01:44.08] essentially to be the standards of the
[L53] [01:45.68] languages in the '9s. Uh so now they
[L54] [01:48.40] have gotten generics which is a big
[L55] [01:50.48] step. So I believe that sort of is sort
[L56] [01:53.68] of a step forward for that but it's
[L57] [01:56.16] still a fairly limited language what you
[L58] [01:58.32] can do which has an advantage that
[L59] [02:01.60] essentially it is forces a very uniform
[L60] [02:04.56] style because there's not much of
[L61] [02:06.64] different things you can do and that's
[L62] [02:08.80] probably it a culture foster to do
[L63] [02:11.12] things in a certain way which makes it
[L64] [02:13.76] easier to essentially read one's other's
[L65] [02:15.92] programs and and essentially jump in a
[L66] [02:18.08] new code base and things like that. So I
[L67] [02:20.24] think that would be my main advantage of
[L68] [02:22.64] go that I see there.
[L69] [02:24.32] >> Is it possible to turn off the garbage
[L70] [02:27.12] collector in Scola?
[L71] [02:28.48] >> Not in production. Uh so we have some
[L72] [02:31.04] research that uh would let you use
[L73] [02:34.48] essentially your own memory allocators
[L74] [02:36.64] and things like that. Uh uh the the way
[L75] [02:39.76] let's say Zigg does it. The problem with
[L76] [02:42.00] that is always that you uh you you can
[L77] [02:45.12] leak references into memory that you
[L78] [02:47.60] reclaim and then all hell breaks use
[L79] [02:50.48] lose essentially your your pointers
[L80] [02:53.04] point to memory that's undefined and and
[L81] [02:56.00] so but in in Scala we we now have a very
[L82] [02:59.68] good way to actually track these
[L83] [03:01.20] references so we can actually prevent
[L84] [03:03.20] that statically by the type system that
[L85] [03:05.20] this will never happen and you can still
[L86] [03:06.88] have your own allocator. That said, we
[L87] [03:09.84] haven't really shipped that in
[L88] [03:11.04] production yet. So, right now, I would
[L89] [03:12.72] say you use the garbage collector,
[L90] [03:14.08] escala. Yeah,
[L91] [03:15.52] >> I see uh a lot on the internet people
[L92] [03:18.00] comparing Rust and Zigg or kind of a
[L93] [03:20.56] fierce debate on which one is better.
[L94] [03:24.00] When you think about Rust versus Zigg,
[L95] [03:26.48] what are the merits of the two compared
[L96] [03:29.36] comparing to each other? So what I can
[L97] [03:31.84] see is ZIK has a really nifty uh compile
[L98] [03:35.04] time uh uh uh construct uh essentially
[L99] [03:39.20] inlining where the compiler does smart
[L100] [03:41.84] inlining and and and that is quite clean
[L101] [03:46.40] and quite powerful and [snorts] Rust has
[L102] [03:49.28] has macros but I think they're more
[L103] [03:50.96] clunky than there is than the zik
[L104] [03:52.80] version. Um in Scala we have something
[L105] [03:55.60] quite close to zik. We also have
[L106] [03:57.92] essentially very a thing that's based on
[L107] [04:00.64] on inlinining and optimizations by the
[L108] [04:03.20] compiler. Uh but we have a restriction
[L109] [04:06.32] which I believe sik doesn't have and
[L110] [04:08.88] that [snorts] is that um there cannot be
[L111] [04:11.44] additional type errors after inlining.
[L112] [04:13.76] So the thing is you inline and then the
[L113] [04:16.08] question is is the inline program
[L114] [04:17.84] guaranteed correct uh so type correct or
[L115] [04:21.60] might you have type errors. The typical
[L116] [04:23.76] example where you might have type errors
[L117] [04:25.52] is C++ templates. In fact that's quite
[L118] [04:28.64] quite scary in C++ that you can expand a
[L119] [04:32.08] template and then you get very very
[L120] [04:34.08] complex type errors and very very hard
[L121] [04:36.32] to to to debug things. So ZIK is I
[L122] [04:39.04] believe is much better because the the
[L123] [04:40.80] inlining mechanism is much ser.
[L124] [04:43.12] >> When you say inlining can you explain
[L125] [04:45.20] the concept? Inlining just means that uh
[L126] [04:48.08] in in Scala we can write inline in front
[L127] [04:50.88] of a of a function and that means that
[L128] [04:53.92] the compiler will uh before it starts
[L129] [04:57.76] code generating. So during the time when
[L130] [05:00.72] it looks at the type code which are
[L131] [05:02.56] trees it will take the function body
[L132] [05:05.76] when it sees a function call to that
[L133] [05:07.44] function it will take the call and
[L134] [05:09.28] replace it by the body and then it will
[L135] [05:11.76] do some optimizations. it can say okay
[L136] [05:14.00] so here we have essentially an app an
[L137] [05:16.80] application to let's say a value which
[L138] [05:20.00] is a lambda and but I know where the
[L139] [05:22.00] lambda points to so let me forward the
[L140] [05:24.24] call right to the function uh so and and
[L141] [05:27.36] with that you can already do quite a bit
[L142] [05:30.24] of uh essentially optimizations which
[L143] [05:33.04] are guaranteed because the the inliner
[L144] [05:36.56] must inline that's not a thing like an
[L145] [05:39.60] optimizer has essentially discretion
[L146] [05:41.84] whether they want to inline things or
[L147] [05:43.52] not and so you can never rely on that
[L148] [05:45.68] but an an inliner which is uh
[L149] [05:48.16] essentially a compile time based on the
[L150] [05:50.80] typer must inline so you can rely on it
[L151] [05:53.60] and const explore by in in zik and C++
[L152] [05:56.64] is essentially very similar
[L153] [05:58.72] >> okay so it's a way to get rid of the
[L154] [06:01.04] function call or the overhead of a
[L155] [06:02.88] function call and tell the compiler you
[L156] [06:06.48] can do more because it's all I guess in
[L157] [06:09.60] line
[L158] [06:10.24] >> yeah you reveal the implementation and
[L159] [06:12.24] That means you you can you can uh the
[L160] [06:15.76] compiler can do something with that.
[L161] [06:17.68] >> When you think about all the dynamically
[L162] [06:19.36] typed languages, um which one stands out
[L163] [06:22.80] as one that you think is kind of the
[L164] [06:25.12] best among them?
[L165] [06:26.32] >> Python is ubiquitous. Um and it has a
[L166] [06:30.72] nice syntax. It uh a lot of the Python
[L167] [06:34.24] programs look like they're very easy to
[L168] [06:36.56] read. So that's definitely an advantage.
[L169] [06:39.52] and and the other one would probably be
[L170] [06:42.32] something like scheme uh which is sort
[L171] [06:44.88] of very grounded in computer science
[L172] [06:47.36] theory and lambda calculus and things
[L173] [06:49.36] like that. So both of them are sort of
[L174] [06:51.84] interesting in their own way but of
[L175] [06:53.36] course Python is 100 times more popular.
[L176] [06:56.32] >> If you compare Scola to Python for
[L177] [06:59.04] instance I guess what are the trade-offs
[L178] [07:01.04] that the two languages took? I think the
[L179] [07:04.00] gap is closing because Python now
[L180] [07:06.64] actually has an optional type syntax and
[L181] [07:10.00] and a number of type checkers that check
[L182] [07:11.92] that syntax in Python is getting some of
[L183] [07:14.96] the features that Scala had since the
[L184] [07:16.80] beginning like pattern matching is in
[L185] [07:18.64] one of the the recent Pythons. So I
[L186] [07:21.20] think actually the gap is closing not
[L187] [07:22.96] just between Python and Scala but
[L188] [07:24.80] between a lot of programming languages
[L189] [07:26.40] in general. There sort of all drift to a
[L190] [07:30.00] standard set of features which mostly
[L191] [07:32.48] come from functional programming
[L192] [07:33.76] actually pattern matching for instance
[L193] [07:36.08] strong type systems uh generics
[L194] [07:38.72] polymorphism all these things came from
[L195] [07:41.60] closures all these things came from
[L196] [07:43.28] functional programming and so the gap is
[L197] [07:46.08] closing in that in that sense. Um,
[L198] [07:49.28] Python is um I think the main advantage
[L199] [07:53.60] of Scala over Python is that it is it
[L200] [07:56.80] has a strong type system that is always
[L201] [07:59.52] on and that gives you essentially
[L202] [08:01.68] guarantees uh that essentially certain
[L203] [08:04.40] bad states can't can't can't happen. So
[L204] [08:06.96] so really can rely on it whereas I think
[L205] [08:09.60] I believe the Python type system well
[L206] [08:11.76] it's just syntax. it has a number of
[L207] [08:13.44] type checkers, but in general there's
[L208] [08:16.72] there's le you you have fewer guarantees
[L209] [08:19.76] and I believe it's also the ecosystem
[L210] [08:21.60] and culture that doesn't value types as
[L211] [08:23.84] much in Python. So I think that's
[L212] [08:25.36] probably the main difference. F
[L213] [08:27.36] syntactically the two languages I think
[L214] [08:29.68] with Scala 3 are actually also quite
[L215] [08:31.44] close. So Scala 3 looks a lot like
[L216] [08:33.76] Python. Um in that sense uh you could
[L217] [08:37.60] say well can see it as a
[L218] [08:41.44] is a language that has uh strong types
[L219] [08:44.16] and uh runs on on different runtimes
[L220] [08:47.28] than Python or I should say the other
[L221] [08:49.28] thing with Python which is really great
[L222] [08:50.88] is that Python is a fantastic glue
[L223] [08:52.80] language because I can essentially have
[L224] [08:55.28] very very efficient linkages to to high
[L225] [08:57.76] performance C++ libraries uh uh pandas
[L226] [09:02.16] or numpy or things like
