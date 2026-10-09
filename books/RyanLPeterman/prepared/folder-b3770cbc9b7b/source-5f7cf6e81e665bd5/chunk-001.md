Chunk 1; segments 1–347. 

# Creator of Scala: Comparing Languages And How AI Will Impact Them | Martin Odersky

Source ID: source-5f7cf6e81e665bd5
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Scala_Comparing_Languages_And_How_AI_Will_Impact_Them_Martin_Odersky_en.txt
Video: https://www.youtube.com/watch?v=LdN4sPWM-WY

[L10] [00:00.16] We are at a moment where it's
[L11] [00:02.56] essentially very dangerous that we lose
[L12] [00:04.32] control as humans.
[L13] [00:06.32] >> This is Martin Oderski, the creator of
[L14] [00:08.72] Scola, and I asked him all about
[L15] [00:10.56] programming languages and how they're
[L16] [00:12.40] going to change in the future.
[L17] [00:13.84] >> I believe right now Rust is actually
[L18] [00:15.76] overused. So Zik is I believe is much
[L19] [00:18.32] better because the the inlining
[L20] [00:20.00] mechanism is much ser. This pisses off
[L21] [00:22.80] both communities and they're promptly
[L22] [00:24.64] declared jihad. If the code is AI
[L23] [00:27.76] generated, then the focus has to go
[L24] [00:29.52] elsewhere. And I think the focus will go
[L25] [00:31.36] to the interfaces and to the types.
[L26] [00:33.92] >> 10 [snorts] years from now, do you think
[L27] [00:35.04] there will be more software engineers
[L28] [00:36.96] than today or less? Here's the full
[L29] [00:39.92] episode.
[L30] [00:45.04] What is functional programming and why
[L31] [00:47.52] should an imperative programmer care
[L32] [00:49.92] about the functional way of programming?
[L33] [00:52.64] So functional programming is programming
[L34] [00:56.08] with values. Uh so you don't have state
[L35] [01:00.08] that changes like mutable variables that
[L36] [01:02.56] change or arrays that change. You have
[L37] [01:05.04] values and you have functions and the
[L38] [01:06.96] functions transform these values into
[L39] [01:08.72] other values. So it's a very restricted
[L40] [01:11.28] form of programming and most real
[L41] [01:13.76] functional programming languages uh are
[L42] [01:16.08] impure in the sense that yes of course
[L43] [01:18.64] at some point you have to touch state
[L44] [01:20.40] and change things and write to standard
[L45] [01:22.96] out and things like that but the idea is
[L46] [01:25.36] to do that sort of uh very late. So to
[L47] [01:28.56] have the largest part of your program
[L48] [01:31.60] represented as values and functions that
[L49] [01:33.84] transform values and the benefit you get
[L50] [01:36.48] from that is essentially much better
[L51] [01:39.04] predictability and fewer bugs because
[L52] [01:42.08] these side effects to let's say a global
[L53] [01:44.16] variable or a field in some object graph
[L54] [01:46.48] or things like that they can really uh
[L55] [01:49.04] trip you up. Uh they can they can
[L56] [01:51.92] essentially they're an undocumented
[L57] [01:53.52] effect of your function. So it's not
[L58] [01:55.44] reflected anywhere typically but may
[L59] [01:57.92] maybe you have a comment if if things
[L60] [02:00.24] are good uh and and these things are
[L61] [02:03.84] very hard to keep in your head and
[L62] [02:06.32] generally reason about. So the advice
[L63] [02:08.88] from functional programming is
[L64] [02:10.32] essentially to keep these things to the
[L65] [02:12.64] bare minimum and possibly to nothing if
[L66] [02:15.44] your function maps into these things. Um
[L67] [02:19.52] the other reason why function
[L68] [02:20.80] programming is nice is that it's very
[L69] [02:23.44] directly linked to mathematics. Uh so in
[L70] [02:26.48] mathematics you have theories of let's
[L71] [02:28.80] say polomials or strings or lists or
[L72] [02:32.56] things like that. And in none of these
[L73] [02:35.04] theories you will find the concept of
[L74] [02:37.04] mutation. It just doesn't exist. So you
[L75] [02:39.52] can take a polomial and you can
[L76] [02:41.20] transform it into a new polomial but you
[L77] [02:43.52] can't change a coefficient coefficient
[L78] [02:45.60] at 3 at the third coefficient and
[L79] [02:48.48] pretend it's the same polomial. It's not
[L80] [02:50.64] in mathematics, right? It's clearly
[L81] [02:52.08] something different. So functional
[L82] [02:53.60] programming you could say follows quite
[L83] [02:56.08] closely the way mathematics sees things.
[L84] [02:58.88] >> What would you say to someone that
[L85] [03:01.04] doesn't do functional programming
[L86] [03:02.32] because it's not convenient? I
[L87] [03:04.24] >> I guess two things. one is uh uh it's
[L88] [03:07.68] it's a learning uh uh curve. Uh so
[L89] [03:11.60] initially you you're sort of your brain
[L90] [03:14.08] is wired to be to do imperative
[L91] [03:16.32] programming from when you were very
[L92] [03:18.00] young. I imagine most people learned an
[L93] [03:19.60] imperative language first and then it's
[L94] [03:22.00] hard to see how you would express things
[L95] [03:25.04] differently.
[L96] [03:26.64] uh but if you persist in that a little
[L97] [03:29.20] bit and it doesn't really take much then
[L98] [03:31.20] you will essentially reap the benefits
[L99] [03:33.04] very quickly that you say well I
[L100] [03:34.80] actually my program got a lot clearer I
[L101] [03:36.88] can understand it better uh I don't
[L102] [03:39.12] really have to track uh some uh steps go
[L103] [03:43.36] step by step through through my program
[L104] [03:44.96] with a debugger or things like that to
[L105] [03:46.64] to figure out what it does typically I
[L106] [03:49.04] don't need a debugger when I write
[L107] [03:50.72] functional code that that's really not
[L108] [03:52.64] not uh not not necessary
[L109] [03:55.12] u the The other thing is to essentially
[L110] [03:58.64] know when to stop. So uh there is a
[L111] [04:02.72] strand of functional programming called
[L112] [04:04.40] pure function programming which tries to
[L113] [04:06.72] express as much as possible in pure
[L114] [04:09.36] functions and to sort of delay the side
[L115] [04:11.52] effects uh to and wrap them up in monuts
[L116] [04:14.80] or whatnot and that can get very
[L117] [04:17.84] inconvenient very quickly. Uh so uh the
[L118] [04:21.84] my answer to that would be it really
[L119] [04:24.48] depends and in most cases it's
[L120] [04:25.92] completely okay to have your side
[L121] [04:28.40] effects as long as these are well
[L122] [04:30.16] documented and and you you you use them.
[L123] [04:32.88] So basically use these things in
[L124] [04:34.48] moderation. I would say functional
[L125] [04:36.48] programming is great for 95% of your
[L126] [04:38.64] program and if you need some side effect
[L127] [04:41.04] some imperative uh feature for the last
[L128] [04:43.20] 5% that's also okay. Is there any
[L129] [04:46.80] quantitative measure of the um I guess
[L130] [04:50.88] the correctness benefits that functional
[L131] [04:52.88] programming gives you over imperative?
[L132] [04:55.52] >> Um I I think there are some studies. Uh
[L133] [05:01.68] it's not quite clear how significant
[L134] [05:04.00] they are. I think people criticize them
[L135] [05:06.00] a lot. The [snorts] studies tend to say
[L136] [05:08.40] that a language like Scala would have
[L137] [05:10.48] fewer bucks than a language like C or
[L138] [05:12.08] C++. But uh I don't really want to sort
[L139] [05:16.32] of insist on that because these studies
[L140] [05:18.96] are very hard to do and the methodology
[L141] [05:21.20] is very hard to get right. I believe the
[L142] [05:23.52] effects come uh are uh become more
[L143] [05:26.56] important in large programs than in
[L144] [05:28.00] small ones. For small ones you can do
[L145] [05:30.16] anything really. You can write it with
[L146] [05:31.92] you can write a loop, you can write a
[L147] [05:33.44] recursive function. It doesn't really
[L148] [05:34.88] matter and it's [snorts] it's very much
[L149] [05:36.96] a matter of taste which one you prefer.
[L150] [05:39.36] But in a large system I believe so I
[L151] [05:42.00] believe that let's say static types have
[L152] [05:46.08] certainly proven their worth and even
[L153] [05:47.84] that we don't really have a conclusive
[L154] [05:49.84] study that shows it. I mean I can point
[L155] [05:51.60] you to a study and if you're a dynamic
[L156] [05:54.08] typing enthusiast and you can point you
[L157] [05:56.48] will point to another that essentially
[L158] [05:58.08] claims the opposite. So it's very very
[L159] [06:00.16] hard to do empirical software
[L160] [06:01.60] engineering on that scale. Um and uh so
[L161] [06:05.60] I'm afraid I I can't really give a good
[L162] [06:08.00] answer. I just have the feeling that
[L163] [06:11.52] mostly functional statically typed
[L164] [06:13.60] languages is sort of a sweet spot for
[L165] [06:16.40] for getting programs right. Maybe the
[L166] [06:19.04] other thing is when you really need to
[L167] [06:20.80] get them absolutely right like with with
[L168] [06:23.44] proofs and things like that. Uh if you
[L169] [06:25.76] do rock or lean or any of these things
[L170] [06:28.00] these are all functional languages. So
[L171] [06:30.24] people wouldn't wouldn't even attempt to
[L172] [06:32.40] do something like C C++ here. When you
[L173] [06:36.00] think about Scola in the environment of
[L174] [06:39.04] all programming languages, what sets
[L175] [06:41.36] Scola apart? Or maybe put in another
[L176] [06:43.84] way, why should someone learn Scola in
[L177] [06:46.24] 2026?
[L178] [06:47.92] >> Well, Scala is the only functional
[L179] [06:50.56] language that is also a very capable
[L180] [06:54.32] object-oriented language. In fact, it
[L181] [06:56.72] was born uh by the idea that we can
[L182] [06:59.84] actually make a fusion of the two in a
[L183] [07:01.92] way which is not a side by side but
[L184] [07:03.84] which really combines the features in a
[L185] [07:06.48] in a nice synthesis. So that was what
[L186] [07:08.96] what Scala was about. That's what I
[L187] [07:10.72] wanted to show and I think that's been
[L188] [07:13.04] largely successful. So you can write
[L189] [07:15.84] really beautiful programs in this
[L190] [07:17.76] combination. uh object-oriented
[L191] [07:20.08] programming comes in when you talk about
[L192] [07:22.72] components and modules and uh
[L193] [07:25.04] essentially encapsulation these sort of
[L194] [07:26.80] things where functional programming
[L195] [07:28.72] typically doesn't really have a very
[L196] [07:30.72] strong story. I mean there are languages
[L197] [07:32.96] like standard ML or or camel that do
[L198] [07:35.28] have very capable module systems but
[L199] [07:37.84] other functional languages don't and and
[L200] [07:40.08] people when they think of functional
[L201] [07:41.36] programming they don't really think much
[L202] [07:43.60] about components and interfaces and
[L203] [07:46.16] these sort of things which are things
[L204] [07:47.92] that I believe also matter very much.
[L205] [07:50.40] >> Could you give an example maybe um like
[L206] [07:53.04] an object-oriented thing that you could
[L207] [07:55.12] do in Scola but you couldn't do in
[L208] [07:57.92] Haskell which is pure functional. it's
[L209] [08:00.96] sort of ingrained. It's in the whole
[L210] [08:03.12] fabric of the things that everything is
[L211] [08:05.04] essentially objects what what you do. Um
[L212] [08:09.36] so so one thing that you get is what I
[L213] [08:12.24] think Simon Pton Jones called the power
[L214] [08:14.00] of the dot uh that you say it's super
[L215] [08:16.40] convenient. You have an object and then
[L216] [08:17.92] you do dot and then you have the
[L217] [08:20.00] environment that immediately tells you
[L218] [08:21.44] what are the methods and fields of that
[L219] [08:23.36] object that they can use them. So it
[L220] [08:25.36] focuses your mind. Whereas in function
[L221] [08:27.20] programming, it's typically you have a
[L222] [08:28.72] sea of functions that can uh be be
[L223] [08:31.36] applied to arguments and you have to
[L224] [08:32.96] figure out what they are.
[L225] [08:34.56] >> When you think about the systems
[L226] [08:35.92] programming languages like Rust, Zigg,
[L227] [08:38.48] Go, C, C++, uh in your opinion, which
[L228] [08:41.84] one would you say is kind of the best
[L229] [08:44.16] one and then maybe we can compare it to
[L230] [08:45.84] Scala?
[L231] [08:46.88] >> In this day and age, a systems
[L232] [08:48.48] programming languages needs to be memory
[L233] [08:50.32] safe, guaranteed memory safe. So that
[L234] [08:52.88] would already exclude quite a few of
[L235] [08:54.96] them but it would leave Rust and Go I
[L236] [08:57.52] think and Rust and Go are at different
[L237] [09:00.08] levels. Go is really not not a sort of a
[L238] [09:04.08] nuts and bolt systems programming
[L239] [09:05.84] languages is more language in which you
[L240] [09:07.84] would write let's say an application
[L241] [09:09.20] server or some middleware or some cloud
[L242] [09:11.44] infrastructure or things like that. It's
[L243] [09:13.52] not something you would use for embedded
[L244] [09:15.60] say which which you would would use Rust
[L245] [09:17.76] for. So I think in their domain both of
[L246] [09:20.40] them are are probably the ones that that
[L247] [09:24.00] are the leading ones that I would take
[L248] [09:25.76] most seriously.
[L249] [09:27.04] >> And then when you compare you know Rust
[L250] [09:30.08] or Go with Scola what are the pros and
[L251] [09:33.60] cons of the different language designs?
[L252] [09:35.68] What's something that Rust does better
[L253] [09:37.52] than Scala? Something that Scola does
[L254] [09:39.76] better than Rust
[L255] [09:40.80] >> so Rust is closer to the metal. you have
[L256] [09:43.12] better performance guarantees I guess uh
[L257] [09:46.24] the fact that Scala is a garbage
[L258] [09:47.76] collected language means that you always
[L259] [09:50.00] have some pauses I mean garbage
[L260] [09:52.08] collection colle collectors have become
[L261] [09:53.68] quite quite capable I mean they're
[L262] [09:55.44] brilliant and the pauses are really very
[L263] [09:57.68] very small but it's fact it's it's a
[L264] [10:00.24] fact that you do need a big chunk of
[L265] [10:03.20] memory to run fast and I guess Rust
[L266] [10:06.16] could could run in much much smaller
[L267] [10:08.40] memory so I believe that's that's better
[L268] [10:10.88] for embedded systems and things like
[L269] [10:12.56] that. I believe right now rust is
[L270] [10:14.72] actually overused because a lot of
[L271] [10:16.48] people push sort of rush rust for things
[L272] [10:19.52] higher higher up in the stack where you
[L273] [10:22.64] garbage collector is fine but uh
[L274] [10:24.88] essentially you you still want to write
[L275] [10:26.96] code without and that is for me a bit an
[L276] [10:31.60] exercise in
[L277] [10:34.00] uh I don't know just intellectual that I
[L278] [10:36.80] can do it I I don't think really think
[L279] [10:38.96] there's a there's a big sense in it that
[L280] [10:41.28] if you have the memory for a garbage
[L281] [10:42.88] collector, you should absolutely use one
[L282] [10:44.72] because it makes a lot of things uh
[L283] [10:47.04] simpler. So yes, of course, if given
[L284] [10:50.32] enough uh brains, I can write code
[L285] [10:53.28] around and I can do that. But why should
[L286] [10:55.52] you? I mean, it it it can be much
[L287] [10:57.52] simpler.
[L288] [10:59.04] So that was for Rust. Uh for Go, go is
[L289] [11:02.96] um sort of a language a bit that that
[L290] [11:06.48] lags behind. I mean was intentionally
[L291] [11:08.64] designed to be to be very very small and
[L292] [11:11.44] essentially to be the standards of the
[L293] [11:13.12] languages in the '9s. U so now they have
[L294] [11:16.08] gotten generics which is a big step. So
[L295] [11:18.88] I believe that sort of is sort of a step
[L296] [11:22.08] forward for that but it's still a fairly
[L297] [11:24.48] limited language what you can do which
[L298] [11:27.28] has an advantage that essentially it is
[L299] [11:30.56] forces a very uniform style because
[L300] [11:32.72] there's not much of different things you
[L301] [11:34.88] can do and that's probably it a culture
[L302] [11:37.76] fostered to do things in a certain way
[L303] [11:40.08] which makes it easier to essentially
[L304] [11:42.40] read one's other's programs and and
[L305] [11:44.56] essentially jump in a new code base and
[L306] [11:46.40] things like that. So I think that would
[L307] [11:48.16] be my main advantage of go that I see
[L308] [11:50.88] there.
[L309] [11:51.68] >> Is it possible to turn off the garbage
[L310] [11:54.56] collector in Scola?
[L311] [11:55.92] >> Not in production. Uh so we have some
[L312] [11:58.48] research that uh would let you use
[L313] [12:01.92] essentially your own memory allocators
[L314] [12:04.08] and things like that. Uh uh the the way
[L315] [12:07.20] let's say Zigg does it. The problem with
[L316] [12:09.36] that is always that you uh you you can
[L317] [12:12.48] leak references into memory that you
[L318] [12:15.04] reclaim and then all hell breaks use
[L319] [12:17.92] lose essentially your your pointers
[L320] [12:20.48] point to memory that's undefined and and
[L321] [12:23.44] so but in in Scala we we now have a very
[L322] [12:27.04] good way to actually track these
[L323] [12:28.56] references so we can actually prevent
[L324] [12:30.64] that statically by the type system that
[L325] [12:32.64] this will never happen and you can still
[L326] [12:34.32] have your own allocator. That said, we
[L327] [12:37.28] haven't really shipped that in
[L328] [12:38.48] production yet. So, right now, I would
[L329] [12:40.08] say you use the garbage collector,
[L330] [12:41.52] escala. Yeah,
[L331] [12:42.96] >> I see uh a lot on the internet people
[L332] [12:45.44] comparing Rust and Zigg or kind of a
[L333] [12:48.00] fierce debate on which one is better.
[L334] [12:51.44] When you think about Rust versus Zigg,
[L335] [12:53.92] what are the merits of the two compared
[L336] [12:56.80] comparing to each other? So what I can
[L337] [12:59.28] see is Zik has a really nifty uh compile
[L338] [13:02.40] time uh uh uh construct uh essentially
[L339] [13:06.64] inlining where the compiler does smart
[L340] [13:09.28] inlining and and and that is quite clean
[L341] [13:13.84] and quite powerful and Rust has has
[L342] [13:16.96] macros but I think they're more clunky
[L343] [13:18.80] than there is than the zik version. Um
[L344] [13:21.76] in Scala we have something quite close
[L345] [13:23.76] to zik. We also have essentially very a
[L346] [13:27.12] thing that's based on on inlining and
[L347] [13:29.36] optimizations by the compiler. Uh but we
[L348] [13:32.48] have a restriction which I believe sik
[L349] [13:34.88] doesn't have and that is that um there
[L350] [13:38.16] cannot be additional type errors after
[L351] [13:40.48] inlining. So the thing is you inline and
[L352] [13:43.12] then the question is is the inline
[L353] [13:44.72] program guaranteed correct uh so type
[L354] [13:47.84] correct or might you have type errors?
[L355] [13:50.40] The typical example where you might have
[L356] [13:52.40] type errors is C++ templates. In fact,
