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
[L357] [13:55.36] that's quite quite scary in C++ that you
[L358] [13:58.16] can expand a template and then you get
[L359] [14:00.64] very very complex type errors and very
[L360] [14:03.20] very hard to to to debug things. So, ZIK
[L361] [14:06.08] is I believe is much better because the
[L362] [14:07.84] the inlining mechanism is much ser.
[L363] [14:10.56] >> When you say inlining, can you explain
[L364] [14:12.56] the concept? Inlining just means that uh
[L365] [14:15.52] in in Scala we can write inline in front
[L366] [14:18.24] of a of a function and that means that
[L367] [14:21.28] the compiler will uh before it starts
[L368] [14:25.20] code generating. So during the time when
[L369] [14:28.08] it looks at the type code which are
[L370] [14:30.00] trees it will take the function body
[L371] [14:33.20] when it sees a function call to that
[L372] [14:34.88] function it will take the call and
[L373] [14:36.72] replace it by the body and then it will
[L374] [14:39.12] do some optimizations. it can say okay
[L375] [14:41.36] so here we have essentially an app an
[L376] [14:44.24] application to let's say a value which
[L377] [14:47.44] is a lambda and but I know where the
[L378] [14:49.44] lambda points to so let me forward the
[L379] [14:51.68] call right to the function uh so and and
[L380] [14:54.72] with that you can already do quite a bit
[L381] [14:57.68] of uh essentially optimizations which
[L382] [15:00.40] are guaranteed because the the inliner
[L383] [15:03.92] must inline that's that's not a thing
[L384] [15:06.56] like an optimizer has essentially
[L385] [15:08.80] discretion whether they want to inline
[L386] [15:10.48] things or not and so you can never rely
[L387] [15:12.56] on that but an an inliner which is uh
[L388] [15:15.60] essentially a compile time based on the
[L389] [15:18.16] typer must inline so you can rely on it
[L390] [15:21.04] and const explore by in in zik and C++
[L391] [15:24.08] is essentially very similar
[L392] [15:26.16] >> okay so it's a way to get rid of the
[L393] [15:28.48] function call or the overhead of a
[L394] [15:30.32] function call and tell the compiler you
[L395] [15:33.92] can do more because it's all I guess
[L396] [15:36.72] inline
[L397] [15:37.60] >> yeah you reveal the implementation and
[L398] [15:39.60] That means you you can you can uh the
[L399] [15:43.12] compiler can do something with that.
[L400] [15:45.12] >> When you think about all the dynamically
[L401] [15:46.80] typed languages, um which one stands out
[L402] [15:50.24] as one that you think is kind of the
[L403] [15:52.48] best among them?
[L404] [15:53.68] >> Python is ubiquitous. Um and it has a
[L405] [15:58.08] nice syntax. It uh a lot of the Python
[L406] [16:01.60] programs look like they're very easy to
[L407] [16:04.00] read. So that's definitely an advantage.
[L408] [16:06.88] and and the other one would probably be
[L409] [16:09.76] something like scheme uh which is sort
[L410] [16:12.32] of very grounded in computer science
[L411] [16:14.72] theory and lambda calculus and things
[L412] [16:16.80] like that. So both of them are sort of
[L413] [16:19.20] interesting in their own way but of
[L414] [16:20.72] course Python is 100 times more popular.
[L415] [16:23.76] >> If you compare Scola to Python for
[L416] [16:26.48] instance I guess what are the trade-offs
[L417] [16:28.40] that the two languages took? I think the
[L418] [16:31.36] gap is closing because Python now
[L419] [16:34.00] actually has an optional type syntax and
[L420] [16:37.60] a number of type checkers that check
[L421] [16:39.36] that syntax in Python is getting some of
[L422] [16:42.40] the features that Scala had since the
[L423] [16:44.16] beginning like pattern matching is in
[L424] [16:46.08] one of the the recent Pythons. So I
[L425] [16:48.64] think actually the gap is closing not
[L426] [16:50.40] just between Python and Scala but but
[L427] [16:52.24] between a lot of programming languages
[L428] [16:53.76] in general there sort of all drift to a
[L429] [16:57.44] standard set of features which mostly
[L430] [16:59.84] come from functional programming
[L431] [17:01.20] actually pattern matching for instance
[L432] [17:03.52] strong type systems uh generics
[L433] [17:06.16] polymorphism all these things came from
[L434] [17:09.04] closures all these things came from
[L435] [17:10.64] functional programming and so the gap is
[L436] [17:13.44] closing in that in that sense um Python
[L437] [17:17.52] is um I think the main advantage of
[L438] [17:21.36] Scala over Python is that it is it has a
[L439] [17:24.80] strong type system that is always on and
[L440] [17:27.84] that gives you essentially guarantees uh
[L441] [17:30.24] that essentially certain bad states
[L442] [17:32.64] can't can't can't happen. So, so you
[L443] [17:34.64] really can rely on it. Whereas I think I
[L444] [17:37.20] believe the Python type system, well,
[L445] [17:39.12] it's just syntax. It has a number of
[L446] [17:40.88] type checkers, but in general there's
[L447] [17:44.08] there's le you you have fewer guarantees
[L448] [17:47.12] and I believe it's also the ecosystem
[L449] [17:48.96] and culture that doesn't value types as
[L450] [17:51.28] much in Python. So, I think that's
[L451] [17:52.80] probably the main difference.
[L452] [17:54.80] Fantactically, the two languages I think
[L453] [17:57.12] with Scala 3 are actually also quite
[L454] [17:58.88] close. So, Scala 3 looks a lot like
[L455] [18:01.20] Python. Um, in that sense, uh, you could
[L456] [18:05.04] say well can see it as a
[L457] [18:08.80] as a language that has strong types and,
[L458] [18:12.48] uh, runs on on different runtimes than
[L459] [18:14.88] Python. Or I should say the other thing
[L460] [18:16.80] with Python which is really great is
[L461] [18:18.48] that Python is a fantastic glue language
[L462] [18:20.72] because I can essentially have very very
[L463] [18:23.20] efficient linkages to to high
[L464] [18:25.20] performance C++ libraries. uh uh pandas
[L465] [18:29.52] or numpy or things like that.
[L466] [18:32.00] >> You mentioned that a lot of the
[L467] [18:33.28] programming languages they're kind of uh
[L468] [18:35.52] drifting or kind of being inspired by
[L469] [18:38.24] the other ones and you know adopting new
[L470] [18:40.40] features in the design of Scola. Is
[L471] [18:42.80] there a programming language that you
[L472] [18:44.96] admire most and influences Scola the
[L473] [18:47.84] most? Historically, Scala was
[L474] [18:51.36] essentially you could say it was a blend
[L475] [18:53.28] of Java,
[L476] [18:55.20] Okamel and or standard ML which is close
[L477] [18:58.88] an [snorts] MLike language and and
[L478] [19:00.80] Haskell. Uh so I I I I'm by trade well
[L479] [19:05.44] I'm by trade an imperative program. My
[L480] [19:07.52] PhD is from Nicholas W. So I know
[L481] [19:09.44] Pascal, modular that was sort of my
[L482] [19:11.76] first generation of languages and I
[L483] [19:13.44] liked them a lot and then I became sort
[L484] [19:16.08] of a converted functional programmer. So
[L485] [19:18.48] I I looked very closely at ML, Okl,
[L486] [19:21.44] Haskell and these things and then um the
[L487] [19:25.84] Scala came about sort of there was a
[L488] [19:27.76] predecessor language called pizza and I
[L489] [19:30.32] was working on that with Phil Wadler
[L490] [19:31.92] who's one of the Haskell original
[L491] [19:33.84] designers and the idea was to have
[L492] [19:36.24] essentially an accessible functional
[L493] [19:38.16] language on a very widespread platform
[L494] [19:40.56] which was a JVM at that at that point
[L495] [19:43.92] and um the uh in order to prepare for
[L496] [19:48.40] that I wrote a Java compiler. So that's
[L497] [19:51.36] how I learned a lot about Java and what
[L498] [19:53.20] Java was. And in the end I I had had to
[L499] [19:56.72] say well it's actually quite useful. I I
[L500] [19:58.96] I was quite dismissive at first but
[L501] [20:01.76] afterwards I found it actually quite
[L502] [20:04.00] useful. I mean this was very early Java.
[L503] [20:06.08] This was Java even pre 1.0. So so now
[L504] [20:08.96] Java is is of course even more useful
[L505] [20:11.36] but also a lot bigger than what it was
[L506] [20:13.68] at the time. Um so when we came up with
[L507] [20:17.68] with Scala which was sort of the second
[L508] [20:19.44] iteration after pizza, pizza was the
[L509] [20:21.44] language I did with Phil water. Uh the
[L510] [20:24.80] the
[L511] [20:26.56] ideas came mostly from Java uh Okamel
[L512] [20:30.48] for the modules and the component module
[L513] [20:33.92] and Haskell a lot for the standard
[L514] [20:36.48] libraries. So if you look at the
[L515] [20:38.16] function names of the in the Scala
[L516] [20:40.00] standard library then there's sort of a
[L517] [20:41.84] mixture of Okamel and Haskell you could
[L518] [20:43.76] say but you you recognize a lot of
[L519] [20:45.44] things coming from both of these these
[L520] [20:47.68] languages
[L521] [20:48.72] >> if I recall correctly uh Java was had
[L522] [20:52.64] some sort of licensing with it or was
[L523] [20:54.72] owned by a company. Um how were you able
[L524] [20:58.08] to build on top of Java or did you have
[L525] [21:01.44] to pay for licenses or how how' that
[L526] [21:04.00] ecosystem work? the language standard
[L527] [21:06.48] was open source. Um there were there was
[L528] [21:09.20] a lot of experimentation with Java at
[L529] [21:11.12] the time. Um I think the only thing that
[L530] [21:15.84] Sun was that was the company at the time
[L531] [21:18.48] they're very particular about is that
[L532] [21:20.24] you absolutely if you did something that
[L533] [21:23.44] was using Java and had Java in it you
[L534] [21:25.92] had to call it Java and and and you
[L535] [21:28.88] couldn't have a different name. So
[L536] [21:30.40] that's why initially for instance
[L537] [21:32.24] Microsoft clashed with them. Uh and then
[L538] [21:35.52] Microsoft went went went away and and
[L539] [21:38.00] designed C which was sort of a a Java on
[L540] [21:41.52] some steroids. They they threw in a bit
[L541] [21:44.24] more than what Java had at the time. U
[L542] [21:47.84] the I think the nastiness came Sun was
[L543] [21:50.16] actually quite an open company. Uh so at
[L544] [21:53.04] the time we no we were not worried about
[L545] [21:55.20] that. So that was in the time frame from
[L546] [21:57.12] 1998 to 2004 2005 something like that.
[L547] [22:03.20] Uh and at the time there was no issue. I
[L548] [22:05.28] think the issue came later when Sun was
[L549] [22:07.76] acquired by Oracle and Google forked
[L550] [22:10.32] Scala on Android Java on Android and
[L551] [22:13.04] that's when the fight started but that
[L552] [22:14.80] was much later. So uh when you say that
[L553] [22:17.52] Scola was using the JVM or built on top
[L554] [22:20.32] of it um like concretely in the the tech
[L555] [22:23.76] stack what does it mean that Scola uses
[L556] [22:26.00] the JVM like how does Java source code
[L557] [22:29.84] eventually execute on a machine?
[L558] [22:32.16] >> So the JVM is u essentially defined by
[L559] [22:36.00] its bite code. So the bite code is
[L560] [22:38.16] essentially an intermediate format which
[L561] [22:40.24] you can translate your program into and
[L562] [22:43.68] then the the bite code is run first by
[L563] [22:46.16] an interpreter and then essentially by
[L564] [22:48.72] an optimized compiler just just in time
[L565] [22:51.20] compiler JIT so that's called JIT they
[L566] [22:53.76] they they do that and
[L567] [22:57.60] so if you can if you know how to uh
[L568] [23:01.60] output bite code and that's not very
[L569] [23:04.00] hard then you can run on the JVM so So
[L570] [23:06.72] that's essentially the the idea. The
[L571] [23:09.04] harder part then is interrupt that you
[L572] [23:11.20] say okay I run on the JVM. I have to
[L573] [23:13.60] make sense of all these Java libraries
[L574] [23:15.36] out there. So I have to somehow map a
[L575] [23:18.00] Java concept into a Scala concept
[L576] [23:21.06] [snorts] so that the compiler can
[L577] [23:22.40] understand what it is and I can document
[L578] [23:24.72] what it is in for Scala programmers that
[L579] [23:27.36] maybe don't understand much Java. So so
[L580] [23:29.52] that that is sort of a work that is sort
[L581] [23:32.88] of goes more into the details. That
[L582] [23:35.60] said, I mean that's not the only uh
[L583] [23:38.40] Scala platform. So it was born on the
[L584] [23:40.24] JVM, but now it also exists uh on on
[L585] [23:43.52] JavaScript and NodeJS uh on WAM and and
[L586] [23:47.04] on native. So it's really a
[L587] [23:48.32] multiplatform language. OpenAI, [snorts]
[L588] [23:51.36] Enthropic, Cursor, and Verscell all use
[L589] [23:54.72] this product to make their lives better.
[L590] [23:56.80] And the problem it solves is when you're
[L591] [23:58.96] building SAS or an AI product and you
[L592] [24:01.52] want to sell to other companies, there's
[L593] [24:03.36] all these requirements you need to meet.
[L594] [24:05.52] There's SSO, there's SKIM, there's
[L595] [24:08.00] arbback, there's audit logs. These are
[L596] [24:10.48] all things that take time to integrate
[L597] [24:12.48] but aren't the main focus of your app.
[L598] [24:14.64] Work OS is an API layer that lets you
[L599] [24:16.72] meet all of these requirements in just a
[L600] [24:19.04] few lines of code. So, let's say you
[L601] [24:20.88] have a new SAS product and you want to
[L602] [24:22.80] sell to other companies. Work OS will
[L603] [24:25.04] solve all of these critical feature gaps
[L604] [24:26.96] for you. You can check them out at
[L605] [24:29.44] workos.com to learn more and get
[L606] [24:31.84] started. And I appreciate them for
[L607] [24:33.92] supporting my work and sponsoring this
[L608] [24:35.68] podcast. Jira bytassian isn't just for
[L609] [24:38.88] tracking work anymore. Now you can pick
[L610] [24:40.80] your favorite AI agent to assign tasks
[L611] [24:43.04] to and they'll get access to the rich
[L612] [24:45.12] context that's already in Jira. When the
[L613] [24:47.68] agent is done, it surfaces pull request.
[L614] [24:50.16] That way you can get more done with your
[L615] [24:52.08] favorite agents all in one place. Learn
[L616] [24:54.56] more at jira.dev. That's jir.dev.
[L617] [25:00.00] Appreciate them for sponsoring the
[L618] [25:01.44] podcast. And back to the show. Let's say
[L619] [25:04.00] I write a Scola program. Uh I have the
[L620] [25:06.80] source code. I have to compile it and
[L621] [25:09.44] then I have some Java bite code and then
[L622] [25:13.28] I call I don't know JVM and I pass in
[L623] [25:16.88] this bite code and it just works.
[L624] [25:19.12] >> Yeah. Yeah, exactly. Yeah.
[L625] [25:20.96] >> What would the advantage be of compiling
[L626] [25:23.44] Scola to Java byte code instead of doing
[L627] [25:27.36] something like C and C++ where you
[L628] [25:29.44] compile it all the way to machine code
[L629] [25:32.24] from source?
[L630] [25:33.76] >> We we have that too. And so the Scala
[L631] [25:36.00] native compiles directly using LLVM to
[L632] [25:39.20] to native code. Um the advantages of um
[L633] [25:44.32] compiling to bite code is essentially
[L634] [25:47.20] again the interrupt can use all the Java
[L635] [25:49.44] libraries. Then uh the the garbage
[L636] [25:52.48] collectors. So the the JVM has actually
[L637] [25:54.80] very good garbage collectors, high
[L638] [25:56.40] performance ones. Um and um and the
[L639] [26:00.40] runtime loading. So, so what what I can
[L640] [26:03.92] do on the JVM is I can compile let's say
[L641] [26:07.04] a oneline thing into a little Java bite
[L642] [26:09.76] code and I can immediately load that by
[L643] [26:11.68] code and execute that and that makes it
[L644] [26:13.92] very easy for instance to have a ripple
[L645] [26:16.24] because that's how how how a ripple
[L646] [26:18.56] would work a redevelop print loop so I
[L647] [26:20.64] would just generate a snippet of Scala
[L648] [26:23.04] code to bite code load it into the
[L649] [26:25.20] running JVM process and it gets executed
[L650] [26:28.08] and that's much harder if you go to
[L651] [26:29.76] binaries basically the binary ers don't
[L652] [26:31.52] really have a concept for that.
[L653] [26:33.60] >> You mentioned that you wrote a compiler
[L654] [26:36.08] for Java like before Scola and I I've
[L655] [26:38.96] heard that compilers are notoriously
[L656] [26:41.20] hard to build. Um can you explain the
[L657] [26:43.84] hard parts and why they're hard?
[L658] [26:46.56] >> Compilers are
[L659] [26:49.68] very intricate. Um because uh I think
[L660] [26:53.60] there there a lot of requirements on a
[L661] [26:56.24] compiler. So you have languages which
[L662] [26:58.96] are already complex artifacts. Uh then
[L663] [27:02.72] you have a thing called type inference.
[L664] [27:04.80] So you have a type system but
[L665] [27:06.56] essentially you demand the compiler to
[L666] [27:10.24] essentially infer a lot of types that
[L667] [27:12.88] make sense because you as a programmer
[L668] [27:14.72] thinks well the compiler should know
[L669] [27:16.08] that and it should uh but actually to
[L670] [27:19.04] for the compiler to do that is is quite
[L671] [27:21.20] hard. And then then you of course you
[L672] [27:23.04] also demand that it would would would
[L673] [27:25.20] generate very efficient code for your
[L674] [27:27.12] program because again the compiler
[L675] [27:29.04] should know that right so there's a lot
[L676] [27:30.88] of demands on that plus there's a demand
[L677] [27:33.52] that it should should be very very fast
[L678] [27:35.76] uh and to square all these demands
[L679] [27:38.88] requires quite a bit of work basically
[L680] [27:42.08] there are also things that make it
[L681] [27:43.60] easier for compilers because they're
[L682] [27:46.00] fundamentally deterministic programs. So
[L683] [27:48.80] essentially you run a compiler on a
[L684] [27:50.56] source and you should you always get the
[L685] [27:52.32] same output. So it means they're easier
[L686] [27:54.48] to debug. You can just replay things and
[L687] [27:56.88] repeat things. Whereas if I would have
[L688] [27:59.28] some cloud service or distributed
[L689] [28:01.04] application that has other nightmares,
[L690] [28:03.52] right? That every run is different and
[L691] [28:05.36] how how do you even figure out what goes
[L692] [28:07.12] wrong?
[L693] [28:07.84] >> So when you wrote that compiler uh I
[L694] [28:10.40] think espresso for Java um how long did
[L695] [28:14.16] it take to write that by hand? uh at the
[L696] [28:17.12] time it took me about 3 months I think
[L697] [28:20.24] not full-time maybe half time three
[L698] [28:22.16] months half time something like that but
[L699] [28:23.92] that was a very simple compiler too so
[L700] [28:26.32] that's the other thing with compilers
[L701] [28:27.68] they typically start simple and when
[L702] [28:30.00] you're at the 10 year mark or 20 year
[L703] [28:31.84] mark then there's lots and lots of
[L704] [28:33.68] essentially other requirements to a
[L705] [28:35.20] compiler that make them more complex.
[L706] [28:37.60] Were there libraries that you could rely
[L707] [28:39.84] on to to kind of piece together
[L708] [28:42.00] components of it or did you have to
[L709] [28:43.44] write you know everything from scratch?
[L710] [28:46.56] I wrote there was a library to uh
[L711] [28:48.88] generate uh bite codes I think uh I
[L712] [28:51.84] think I used that in that version. Yeah
[L713] [28:53.76] I did. Yeah. So there was a a library
[L714] [28:55.84] that essentially a high level library to
[L715] [28:57.92] just assemble by codes and and put them
[L716] [29:00.32] in the to the right format and things
[L717] [29:02.16] like that. Uh but that was essentially
[L718] [29:05.04] it. The rest I wrote by hand. Yeah.
[L719] [29:07.60] That's crazy because well I mean these
[L720] [29:10.40] days a lot of people even more so now
[L721] [29:12.88] we're thinking less using AI more to
[L722] [29:15.36] kind of you know write the code. So
[L723] [29:17.60] that's pretty impressive. I saw one of
[L724] [29:19.92] the big I guess moments for Scola was
[L725] [29:22.16] that Twitter adopted it and I wanted to
[L726] [29:24.72] know the story behind that. How did they
[L727] [29:26.88] choose such a obscure language at that
[L728] [29:29.28] time?
[L729] [29:30.08] >> It was very obscure at the time. That's
[L730] [29:32.16] true. Uh so I believe the story was
[L731] [29:35.28] Twitter originally was written in Ruby
[L732] [29:38.48] and um it wasn't very reliable because I
[L733] [29:42.16] believe it's again a problem with
[L734] [29:43.36] garbage collector and memory management
[L735] [29:45.12] and things like that. So uh the uh and
[L736] [29:49.20] it was a small company at the time. So
[L737] [29:51.20] 25 people uh including the ops people
[L738] [29:54.72] and um the uh essentially the the board
[L739] [29:58.72] and the VC investors said you can't go
[L740] [30:01.44] on like this being unreliable like that.
[L741] [30:04.00] You should do Java because Java was sort
[L742] [30:06.40] of the solid choice at the time. But the
[L743] [30:09.04] the the some some of the engineers at at
[L744] [30:12.08] Twitter they wanted essentially
[L745] [30:13.60] something more fancy as a programming
[L746] [30:15.68] language and there were some people who
[L747] [30:17.92] knew Okamo and liked Okamo but of course
[L748] [30:21.12] Okamel didn't run on the JVM and then
[L749] [30:23.92] they found Scala and said well Scala is
[L750] [30:25.60] actually quite a lot like Okamo and we
[L751] [30:28.24] can tell our investors that we do Java
[L752] [30:30.16] because it's not a lie we do JVM JVM by
[L753] [30:33.04] code that's essentially what it what
[L754] [30:35.20] what where what it comes down to. So
[L755] [30:37.36] that's why why they picked it and they
[L756] [30:39.12] were quite the first but once they
[L757] [30:40.56] picked it sort of the floodgates opened
[L758] [30:42.40] because at that time they were very uh
[L759] [30:45.04] interesting company and a lot of people
[L760] [30:46.88] admired them. So a lot of people
[L761] [30:48.48] followed and did the same thing then uh
[L762] [30:51.04] mostly they came from dynamic languages.
[L763] [30:53.60] So Twitter came from Ruby others came
[L764] [30:55.92] from PHP or uh yeah JavaScript uh things
[L765] [30:59.68] like that. I mentioned a little bit that
[L766] [31:02.24] you know AI is kind of generating a lot
[L767] [31:04.24] of code and I wanted to ask you what you
[L768] [31:07.52] thought maybe the future of programming
[L769] [31:09.76] languages might look like if you kind of
[L770] [31:12.24] speculated or drew out further into the
[L771] [31:15.12] future like if AI is generating more of
[L772] [31:17.12] the code. How do you think that might
[L773] [31:19.20] affect the programming language
[L774] [31:20.96] ecosystem?
[L775] [31:22.32] >> Yeah, I think right now we are sort of
[L776] [31:24.08] in an existential crisis, right? So we
[L777] [31:26.96] have [snorts] AI generating the code but
[L778] [31:29.12] uh uh humans being asked impossible
[L779] [31:32.72] tasks like to review all this these
[L780] [31:35.04] mountains of code and things like that
[L781] [31:36.80] which will never work. Um and uh at the
[L782] [31:40.00] same time a AI is also gotten extremely
[L783] [31:42.96] good at exploiting vulnerabilities in
[L784] [31:45.20] code like we we all heard of Fable and
[L785] [31:47.36] and and things like that that you can't
[L786] [31:49.12] use it anymore because it's too
[L787] [31:51.28] dangerous. It will exploit things. So
[L788] [31:55.44] um we are at a moment where it's
[L789] [31:58.64] essentially very dangerous that we lose
[L790] [32:00.48] control as humans of what what actually
[L791] [32:03.04] happens here and uh that's a challenge
[L792] [32:06.64] that I think programming languages can
[L793] [32:09.28] help meet and probably definitely not
[L794] [32:11.92] only programming languages that's no
[L795] [32:13.76] silver bullet but they definitely can
[L796] [32:16.24] help things. Um so I think one of the
[L797] [32:20.24] things is that the focus if the code is
[L798] [32:24.08] AI generated then the focus has to go
[L799] [32:26.32] elsewhere and I think the co focus will
[L800] [32:28.32] go to the interfaces and to the types.
[L801] [32:31.12] So I expect types will become a lot
[L802] [32:33.76] stronger and more precise than than what
[L803] [32:36.40] we had because types is essentially the
[L804] [32:38.88] handle that we can make a contract
[L805] [32:41.44] between the human and the AI that the
[L806] [32:43.68] that the human can understand and that's
[L807] [32:45.60] concise enough to be reviewed and that
[L808] [32:48.48] essentially the AI can keep to uh we
[L809] [32:51.60] have to level our game quite a lot. Uh
[L810] [32:54.48] because right now I mean let's face it
[L811] [32:57.12] type systems are mostly
[L812] [32:59.92] um uh recommendations. Uh they're mostly
[L813] [33:04.16] uh things that uh mostly hold but not
[L814] [33:07.04] always. There are no guarantees because
[L815] [33:08.56] you can always have a cast or well you
[L816] [33:11.76] you use some dirty memory or I mean
[L817] [33:14.16] there there are number of a lot of
[L818] [33:15.84] techniques to sort of undermine the type
[L819] [33:18.08] systems and we have to close all these
[L820] [33:19.76] holes from the beginning because uh once
[L821] [33:22.56] once there is a hole somebody can
[L822] [33:24.00] exploit it. Uh so I think strong types
[L823] [33:27.04] strong highle types will help. Um and
[L824] [33:31.12] then I think the the other part is
[L825] [33:33.92] generally the programmer has to think
[L826] [33:35.60] much more about what are the
[L827] [33:36.80] requirements and what are the
[L828] [33:40.48] essentially the high level
[L829] [33:41.52] specifications
[L830] [33:43.36] uh and be able to leave the code to be
[L831] [33:47.12] generated by somebody else in confidence
[L832] [33:50.24] and uh I think we're not quite there yet
[L833] [33:53.12] but we we we have some ideas how we
[L834] [33:55.68] could get there. uh so one one uh
[L835] [33:59.84] technique that I believe uh we can use
[L836] [34:02.88] and it has been around for a long time
[L837] [34:04.56] but maybe it's time has come now this
[L838] [34:06.56] capabilities capabilities essent
[L839] [34:09.12] essentially was used in operating
[L840] [34:10.64] systems to give very fine grain
[L841] [34:12.32] permissions to to uh entities users
[L842] [34:16.00] programs and things like that and uh I
[L843] [34:19.44] believe that can be used also for agents
[L844] [34:22.48] and the agentic AI to say well once we
[L845] [34:25.84] have agents We have to give agents very
[L846] [34:28.16] precise and fine grain capabilities what
[L847] [34:30.08] they can do and that lets us essentially
[L848] [34:32.56] be confident about what they will not be
[L849] [34:35.52] able to do like they will not be able to
[L850] [34:37.84] leak my API keys or my email or or do do
[L851] [34:42.08] other things right so I think that's
[L852] [34:44.08] that's an important part uh and the
[L853] [34:48.16] existing languages are uh not there yet
[L854] [34:51.60] uh I think Scala is halfway there at
[L855] [34:54.32] least it's there where in essentially
[L856] [34:56.56] stuff we're working on which we have in
[L857] [34:58.08] the lab and we have released as an
[L858] [34:59.60] experimental feature. So I'm quite
[L859] [35:01.60] excited about that. Um the first thing
[L860] [35:04.08] that you have to do is definitely be
[L861] [35:07.28] memory safe. So a language that
[L862] [35:09.44] essentially is is not safe in memory
[L863] [35:11.52] that lets you essentially uh access
[L864] [35:15.04] undefined memory uh is immediately out
[L865] [35:17.60] because you can't you can't guarantee
[L866] [35:19.28] anything. So that's in that sense it's
[L867] [35:22.16] good that there is a drive to use let's
[L868] [35:23.76] say rust as a memory safe language we're
[L869] [35:25.84] even that that was even promoted by the
[L870] [35:28.80] American government I believe so that's
[L871] [35:30.88] definitely a very useful drive but I
[L872] [35:33.04] think you need a lot more because you
[L873] [35:34.88] need much rest talk folks essentially
[L874] [35:37.60] mostly or only about memory you need to
[L875] [35:40.08] talk about a lot more things than memory
[L876] [35:42.48] you need about essentially read
[L877] [35:43.92] permissions write permissions access to
[L878] [35:46.72] secrets all these things that that are
[L879] [35:49.04] that are uh uh that go beyond that and u
[L880] [35:54.48] you could say okay uh that
[L881] [35:57.68] Martin you're totally unrealistic
[L882] [35:59.52] because uh all our software is written
[L883] [36:01.92] in C and C++ and we will not be able to
[L884] [36:04.48] rewrite that uh but that I believe AIS
[L885] [36:08.64] can help there right so AIs are great to
[L886] [36:10.72] re in rewriting software so if we know
[L887] [36:13.76] what to rewrite too I think we could we
[L888] [36:15.76] might be able to get there
[L889] [36:17.44] >> you mentioned some of those experimental
[L890] [36:19.36] features in Scola that um might have
[L891] [36:22.16] some sort of safety guarantees or signal
[L892] [36:25.12] capabilities. Can you explain what that
[L893] [36:27.60] might look like or maybe give an
[L894] [36:29.12] example?
[L895] [36:30.24] >> So, so a simple example would would be
[L896] [36:32.32] let's say somebody gives me a file and
[L897] [36:34.88] um uh and uh I have access to the file
[L898] [36:39.36] let's say a log file or something like
[L899] [36:41.20] that. I have access for a file for a
[L900] [36:43.04] limited time and then I I need to close
[L901] [36:45.20] it. So typically I have a operation that
[L902] [36:48.32] essentially somebody passes I a file to
[L903] [36:51.36] me to an operation that my program
[L904] [36:54.24] provides and the program does something
[L905] [36:56.56] with the file and then the environment
[L906] [36:58.08] will close it. But how do we make sure
[L907] [37:01.12] that I don't hold on to the file after I
[L908] [37:04.40] get it back to the environment or after
[L909] [37:06.16] I I I pretended I'm finished with it
[L910] [37:08.72] because hey I I have a file. I could
[L911] [37:10.56] have stored it in a variable. I could
[L912] [37:12.32] have stored it on the side. I could have
[L913] [37:14.08] gone g come g come g come g come g come
[L914] [37:14.32] g come g come g come g come g come g
[L915] [37:14.40] come g come g come g come g come g come
[L916] [37:14.40] g come g come g come g come comeone back
[L917] [37:14.72] to it and done something with it. So uh
[L918] [37:17.76] capabilities help me prevent that
[L919] [37:19.76] because essentially I I can say okay so
[L920] [37:21.76] this file is a capability and then I can
[L921] [37:24.08] further say well this capability can be
[L922] [37:26.80] used only in a limited scope and the
[L923] [37:29.28] type system will make sure that the
[L924] [37:31.04] capability doesn't escape and the way we
[L925] [37:33.28] do that is that if a type refers to
[L926] [37:36.48] capabilities so if I have a a thing that
[L927] [37:39.04] I say I give you back a a lambda or a a
[L928] [37:43.44] stream and it holds on to the file. So
[L929] [37:45.76] the stream holds on to the file in
[L930] [37:47.44] secret. In our language that won't be a
[L931] [37:50.32] secret anymore because the type has to
[L932] [37:52.48] declare that the thing I return does
[L933] [37:55.28] hold on to the file. The file is a
[L934] [37:56.88] capability and I can't essentially hide
[L935] [37:59.92] capabilities I have access to in my
[L936] [38:02.16] type. I have to be I have to declare
[L937] [38:04.08] them and that gives me essentially this
[L938] [38:06.80] this control that then I can also
[L939] [38:08.96] enforce to say well at this point you're
[L940] [38:11.04] not allowed to have any capability
[L941] [38:12.48] because the type that I enforced you to
[L942] [38:15.04] have is a type that doesn't hold
[L943] [38:16.80] capabilities and that's that way I
[L944] [38:18.56] enforce with the type system something
[L945] [38:20.56] which uh previously hasn't really been
[L946] [38:23.52] enforcable
[L947] [38:25.04] uh with for memory safety it's
[L948] [38:26.96] essentially the same thing with arenas
[L949] [38:29.04] uh that I I have an area where I
[L950] [38:32.00] allocate memory and then I want want to
[L951] [38:33.84] get rid of it. I have to make sure I
[L952] [38:35.60] don't have pointers pointing into it and
[L953] [38:37.92] that's exactly the same the same
[L954] [38:39.68] situation and and let's say for
[L955] [38:43.12] accessing secrets again. So it's a very
[L956] [38:45.04] common pattern that I say in certain
[L957] [38:47.84] situations I want to make sure that you
[L958] [38:51.12] don't have uh or that you only have a
[L959] [38:53.60] set of defined capabilities that I give
[L960] [38:56.08] you and nothing else. You mentioned uh
[L961] [38:58.80] memory safety is an absolute uh table
[L962] [39:01.68] stakes. What are the programming
[L963] [39:03.60] languages that you think of that are not
[L964] [39:05.44] memory safe? I know there's C, but what
[L965] [39:07.36] are the other ones?
[L966] [39:08.80] >> The big ones is C, C++. Um I I don't
[L967] [39:12.56] know about I think Zik or Nim or other
[L968] [39:14.88] low-level systems languages are not
[L969] [39:16.56] memory safe. So that was sort of in Rust
[L970] [39:19.28] the a big achievement that you say you
[L971] [39:21.36] can be a low-level systems languages and
[L972] [39:23.36] be be memory safe. nobody sort of
[L973] [39:26.00] thought that that was possible before
[L974] [39:27.76] Rust came. Uh so so that's why I would
[L975] [39:31.52] think I don't want to say anything wrong
[L976] [39:33.44] but I would think that essentially most
[L977] [39:36.24] other low-level systems languages would
[L978] [39:38.24] not be memory safe. Um but you really
[L979] [39:41.76] need more than memory safe. You really
[L980] [39:43.28] need capability safes that you say you
[L981] [39:46.08] when I essentially hang on tell you I
[L982] [39:48.80] can't sort of forget capabilities to say
[L983] [39:51.04] I hang on to something and I I just
[L984] [39:52.88] conveniently forget that I have access
[L985] [39:54.80] to that and I can't forge capabilities
[L986] [39:57.36] to say well if I need a capability I
[L987] [39:59.84] just make one up. And so these two
[L988] [40:02.16] things need to be prevented and that
[L989] [40:03.84] goes go that goes beyond memory safety.
[L990] [40:07.12] But memory safety without memory safety
[L991] [40:09.44] essentially you have nothing because you
[L992] [40:10.96] can fake everything.
[L993] [40:12.32] >> A lot of programming language design and
[L994] [40:15.12] how we write code in the past is writing
[L995] [40:18.08] the source code so that it's um it's
[L996] [40:21.52] it's nice for humans to read. But if
[L997] [40:24.48] humans are no longer interacting with
[L998] [40:26.16] the code, what kind of things come to
[L999] [40:28.72] mind that we might not care as much
[L1000] [40:31.68] about but are good for machines to read.
[L1001] [40:34.72] For instance,
[L1002] [40:35.76] >> the first thing is uh maybe sometimes
[L1003] [40:38.32] you want to read it uh but you probably
[L1004] [40:40.80] wouldn't have written it. So easy to
[L1005] [40:43.28] write is definitely not not a big
[L1006] [40:45.52] criterion anymore. Easy to read to some
[L1007] [40:48.08] degree. Yes. But that means you don't
[L1008] [40:50.32] need any these these sort of syntactic
[L1009] [40:52.40] hacks like to write plus+ in C or things
[L1010] [40:55.04] like that that's easy to write right. So
[L1011] [40:57.76] but I I don't I mean I'm sure we will
[L1012] [41:00.56] still have that but it doesn't really
[L1013] [41:02.40] matter anymore. I mean whether [snorts]
[L1014] [41:04.32] I write an assignment in in long form or
[L1015] [41:06.80] with X++ whatever. So I think these
[L1016] [41:09.60] things won't won't matter much less. the
[L1017] [41:11.76] things that matter much more are or that
[L1018] [41:14.40] continue to matter and uh are
[L1019] [41:18.00] essentially high level ways to constrain
[L1020] [41:21.68] and specify what my program should do.
[L1021] [41:24.88] So uh constrain what it should not do.
[L1022] [41:27.28] Uh that's that's one of the things and
[L1023] [41:29.44] also specify what it should do. uh and I
[L1024] [41:32.96] mean some people say it's a golden age
[L1025] [41:35.60] for formal verification because we can
[L1026] [41:37.76] be very precise in our specifications
[L1027] [41:40.00] and our AI can actually not just finish
[L1028] [41:43.36] the program but also the proof that the
[L1029] [41:45.76] that the program actually meets the
[L1030] [41:47.52] specification and I think that's true
[L1031] [41:49.68] that's really very exciting in in in a
[L1032] [41:51.68] lot of areas but in the large uh the
[L1033] [41:55.36] problem is you often don't really have
[L1034] [41:57.04] the formal specification or it's just as
[L1035] [42:00.16] hard to write a formal specific
[L1036] [42:01.44] ification than to write a program or
[L1037] [42:03.12] sometimes even harder. So that means
[L1038] [42:05.52] that we will still have live in a world
[L1039] [42:08.40] where we specify things by natural
[L1040] [42:11.52] languages by prompt to the agent and and
[L1041] [42:14.96] the agent then will will do the code.
[L1042] [42:16.88] But I imagine that also the that will be
[L1043] [42:19.76] a lot more
[L1044] [42:21.76] um formal in a way. So, so in a sense
[L1045] [42:25.28] right now the prompts I mean it's
[L1046] [42:27.12] fantastic what they can do with the
[L1047] [42:28.48] prompts but then we throw away the
[L1048] [42:29.84] prompt or the it's hidden in in the chat
[L1049] [42:32.64] history with the agent. So that's really
[L1050] [42:34.40] a shame. So I really should should have
[L1051] [42:36.64] the prompts as first class values in my
[L1052] [42:39.12] program that I can say well essentially
[L1053] [42:41.36] that's what the program is about and if
[L1054] [42:43.12] I change the prompt then the AI will
[L1055] [42:46.08] know essentially what the incremental
[L1056] [42:47.92] change was and change the program
[L1057] [42:49.36] incrementally. these sort of things.
[L1058] [42:51.68] That's another thing that I think we'll
[L1059] [42:53.28] see in future programming languages for
[L1060] [42:55.44] a agentic programming.
[L1061] [42:57.52] >> Maybe like some kind of meta meta
[L1062] [43:00.40] information about the program almost
[L1063] [43:02.08] like a git blame but like a you know
[L1064] [43:05.44] prompt I guess blame of what generated
[L1065] [43:08.24] that that part of the code.
[L1066] [43:11.36] >> You should be able to to to keep that
[L1067] [43:14.08] around and and come back to it. Yeah.
[L1068] [43:16.00] Also because you want you might want to
[L1069] [43:17.60] change, right? You might want to say
[L1070] [43:19.20] well now it's exactly the same but I
[L1071] [43:21.60] want to change this little detail but I
[L1072] [43:24.08] don't want the LLM nondeterministically
[L1073] [43:26.40] to generate a new program because that
[L1074] [43:28.40] way well it might get a lot of other
[L1075] [43:30.32] things wrong that I reviewed already. So
[L1076] [43:32.64] there really should then be an
[L1077] [43:34.00] incremental small change to the code and
[L1078] [43:36.64] that means I keep I need to keep the
[L1079] [43:38.24] prompt as a part of my program.
[L1080] [43:40.80] >> 10 years from now do you think there
[L1081] [43:42.16] will be more software engineers than
[L1082] [43:44.08] today or less?
[L1083] [43:46.96] I think there will be less uh the
[L1084] [43:50.88] uh and it will be a higher um
[L1085] [43:55.52] profession that is essentially has
[L1086] [43:58.24] higher standards. Uh so it will be
[L1087] [44:00.32] harder to become one. You will know be
[L1088] [44:02.80] able to know quite a lot of logics and
[L1089] [44:04.80] maths to be competent at essentially
[L1090] [44:08.00] keeping AI on the good track and things
[L1091] [44:10.16] like that. It's sort of can say it's
[L1092] [44:12.16] sort of like a like a control engineer
[L1093] [44:14.24] for a factory where you don't understand
[L1094] [44:16.72] many things in initially. It means that
[L1095] [44:19.76] there must be more you must be higher
[L1096] [44:22.40] skilled than a a factory worker of uh 50
[L1097] [44:26.00] years ago or something like that and I
[L1098] [44:28.16] think the same will will happen for
[L1099] [44:29.60] software where you will need fewer but
[L1100] [44:32.96] more qualified people. One thing that a
[L1101] [44:35.60] lot of people recommend is to become
[L1102] [44:37.44] better at programming you should learn
[L1103] [44:39.04] multiple languages and I wanted to know
[L1104] [44:42.48] aside from Scola what are the top
[L1105] [44:45.20] programming languages you would
[L1106] [44:46.64] recommend people learn to expand their
[L1107] [44:48.88] mind. So definitely a systems language
[L1108] [44:51.76] uh I think to to know how how how
[L1109] [44:54.80] hardware works and how software links
[L1110] [44:56.80] with hardware I would learn a systems
[L1111] [44:58.40] language and um
[L1112] [45:01.76] I'm sort of torn between C and Rust
[L1113] [45:04.00] there because C has going for it that
[L1114] [45:06.40] it's very simple and very close to a
[L1115] [45:08.72] thing in Rust you have to learn a lot of
[L1116] [45:10.64] abstractions but on the other hand it is
[L1117] [45:12.64] memory safe so I would say probably
[L1118] [45:14.80] initially see to figure out what these
[L1119] [45:17.20] things are and then if If you decide to
[L1120] [45:19.60] become a systems programmer as a career
[L1121] [45:21.68] then you should switch to rest I guess.
[L1122] [45:23.92] So that would be one thing. Uh the other
[L1123] [45:26.56] thing would be something more
[L1124] [45:29.60] uh with a verification improving
[L1125] [45:32.00] background because that will be a lot
[L1126] [45:33.68] more will become a lot more important.
[L1127] [45:37.04] So I would actually do a course in in
[L1128] [45:39.76] lean or or rock or one of these
[L1129] [45:42.08] languages uh to say where we we should
[L1130] [45:45.28] be able to use AI or to to to have to
[L1131] [45:50.56] develop first an intuition what it means
[L1132] [45:52.48] for a program to be correct because I
[L1133] [45:54.48] guess for most people have only a very
[L1134] [45:56.32] very uh fuzzy fuzzy intuition for these
[L1135] [46:00.00] things and and learning one of these
[L1136] [46:02.16] languages would sharpen the mind.
[L1137] [46:05.28] Um yeah, so I think those and then of
[L1138] [46:07.84] course Scala too as a language that
[L1139] [46:10.32] essentially sits right in the middle
[L1140] [46:11.92] where fairly fairly provable strong
[L1141] [46:14.96] types uh high expressivity these sort of
[L1142] [46:17.92] things.
[L1143] [46:18.32] >> Yeah. When you think of a top technical
[L1144] [46:20.16] book that you might recommend people
[L1145] [46:22.16] does anything come to mind?
[L1146] [46:23.84] >> I got a lot out of uh structure and
[L1147] [46:26.08] interpretation of computer programs that
[L1148] [46:28.08] was a book from the '9s. It was the
[L1149] [46:30.80] intro text at MIT at the time uh or 80s
[L1150] [46:34.72] even I think um and in fact this the
[L1151] [46:38.16] courses I taught on Corera and and uh at
[L1152] [46:41.36] DPFL are based quite a lot well to some
[L1153] [46:44.48] degree they're based based on that
[L1154] [46:46.16] material. So of course not the same
[L1155] [46:47.84] language and strong types instead of
[L1156] [46:50.16] dynamically type but still
[L1157] [46:52.16] >> when you look back on your career why
[L1158] [46:54.08] did you choose to work in academia
[L1159] [46:55.84] instead of industry? When I came to the
[L1160] [46:58.24] end of my studies, I uh was asked to do
[L1161] [47:00.80] a research project and the project I
[L1162] [47:04.00] picked or the prof then asked from me to
[L1163] [47:07.20] modulate that a little bit. In the end,
[L1164] [47:09.20] I found it super interesting to say I I
[L1165] [47:11.60] work on something that I don't know
[L1166] [47:12.96] whether it has a solution or not. Uh so
[L1167] [47:16.40] uh it it might be that uh the question
[L1168] [47:18.24] is yes, it might be the question is no.
[L1169] [47:20.40] We have to do research and that's sort
[L1170] [47:22.96] of how it started. And then
[L1171] [47:26.56] then I I believe the the main advantage
[L1172] [47:30.32] of uh being in academia is really the
[L1173] [47:33.20] long term and being independent. So in
[L1174] [47:36.00] the long term I mean ind in industry I'm
[L1175] [47:39.12] sure there are many periods including
[L1176] [47:40.64] now where I could be paid 10 times what
[L1177] [47:42.72] I'm being paid at university if I joined
[L1178] [47:46.16] Google or any of the other companies in
[L1179] [47:48.08] Silicon Valley. But um then times also
[L1180] [47:51.92] change and sometimes essentially what
[L1181] [47:53.28] you do is no longer relevant and then
[L1182] [47:54.96] it's very easy to get fired and to
[L1183] [47:58.32] then you say no big deal I can do
[L1184] [47:59.84] something else but at a university you
[L1185] [48:02.32] have essentially long-term tenure to do
[L1186] [48:04.24] exactly what you want. So no manager you
[L1187] [48:06.64] can do define your own research agenda.
[L1188] [48:09.92] Of course you have to get some money
[L1189] [48:11.92] that that that is uh is hard. You have
[L1190] [48:14.48] to get grants and things like that. you
[L1191] [48:16.16] have to convince students that what you
[L1192] [48:18.32] do is uh is the right thing and but
[L1193] [48:21.12] that's also very rewarding working with
[L1194] [48:23.04] students. So I think I in in the end I'm
[L1195] [48:25.76] I'm very happy that I took the career I
[L1196] [48:27.92] took.
[L1197] [48:28.56] >> What about looking back on Scola? Um you
[L1198] [48:31.44] know do you have so much experience
[L1199] [48:32.96] there. What are some things that went
[L1200] [48:34.96] well or things that didn't go well and
[L1201] [48:37.20] maybe some learnings you could share?
[L1202] [48:39.36] Scala was initially this experiment that
[L1203] [48:41.84] we could uh combine object-oriented and
[L1204] [48:44.56] functional programming and technically
[L1205] [48:47.04] that experiment was a big success uh um
[L1206] [48:51.52] in terms of the ecosystem it had a lot
[L1207] [48:54.00] of challenges. I don't know whether you
[L1208] [48:55.68] know there was a there was a short
[L1209] [48:57.76] incomplete history of programming
[L1210] [48:59.28] languages by James Ivy which is quite
[L1211] [49:01.28] hilarious and there was there's a
[L1212] [49:02.88] scholar entry there that this says I
[L1213] [49:05.04] discovered reef spell sandwiches and I
[L1214] [49:08.16] had an idea to essentially have a
[L1215] [49:10.24] language where you put in both object
[L1216] [49:12.16] and functional and then it ends with
[L1217] [49:14.40] this pieces of both communities and
[L1218] [49:16.48] they're promptly declared jihad and
[L1219] [49:19.04] that's [laughter] at the at the
[L1220] [49:21.20] beginning it was very funny but uh in
[L1221] [49:23.60] retrospect That's to a large degree what
[L1222] [49:25.68] happened. I mean there was there were
[L1223] [49:27.28] there were a lot of fights and cultural
[L1224] [49:28.96] fights and things like that. So um and
[L1225] [49:33.28] um
[L1226] [49:35.20] we might have uh it was a challenge and
[L1227] [49:38.72] I don't know in retrospect I think it
[L1228] [49:43.04] might have been
[L1229] [49:45.76] more prudent to be more careful
[L1230] [49:48.48] introducing functional features because
[L1231] [49:50.32] that sort of was we went in uh
[L1232] [49:53.68] essentially
[L1233] [49:55.52] quite complete. So essentially you can
[L1234] [49:57.20] port most Haskell programs to Scala
[L1235] [49:59.60] maybe that you you find them a bit less
[L1236] [50:02.32] attractive looking but you can do it and
[L1237] [50:05.84] that was that brought in essentially
[L1238] [50:09.60] different cultures very
[L1239] [50:12.08] and it caused a big clash of cultures.
[L1240] [50:14.64] So uh for instance in go Go was a lot
[L1241] [50:18.16] maligned because they didn't even have
[L1242] [50:20.48] generics right and it's it's true it was
[L1243] [50:22.72] a ridiculous language but uh by not
[L1244] [50:25.92] having it initially you sort of form a
[L1245] [50:27.92] culture that when you add it nothing
[L1246] [50:29.92] much will go wrong and people won't
[L1247] [50:31.68] overabstract or things like that and by
[L1248] [50:34.24] essentially going full hog into into it
[L1249] [50:36.64] with Scala from the start we were not
[L1250] [50:38.88] protected against that and people did uh
[L1251] [50:41.76] reach abstraction peaks and over
[L1252] [50:43.44] abstract it and and things like that and
[L1253] [50:45.84] that's they still do it to this very
[L1254] [50:47.68] day. So essentially having fancy
[L1255] [50:49.68] abstractions is great but you have to
[L1256] [50:51.60] use them responsibly and uh that then it
[L1257] [50:54.72] sort of clashes with the natural urge to
[L1258] [50:57.92] just try out all these fancy things and
[L1259] [50:59.92] do do something that in the end maybe
[L1260] [51:02.48] neither no you nor understands very well
[L1261] [51:05.44] and it could have just been a simple map
[L1262] [51:07.92] or things like that but uh yeah why do
[L1263] [51:11.12] use that when it can be complicated? Why
[L1264] [51:13.68] would that upset someone?
[L1265] [51:15.52] >> Because of the library ecosystem. I
[L1266] [51:17.76] think that um
[L1267] [51:20.08] um the
[L1268] [51:22.64] so libraries are are important and
[L1269] [51:26.08] because they sort of set the agenda how
[L1270] [51:28.64] you express your programs and in
[L1271] [51:30.96] particular the the uh the libraries that
[L1272] [51:34.08] come from the Haskell side. They're
[L1273] [51:35.68] essentially monatic frameworks and they
[L1274] [51:37.84] require you to express your whole
[L1275] [51:39.20] program as a monot which is a concept
[L1276] [51:41.52] that works well in functional
[L1277] [51:43.36] programming. I have my reservations. I
[L1278] [51:45.68] wouldn't actually do that in my in my
[L1279] [51:47.44] scholar programs, but by having
[L1280] [51:50.08] prominent libraries out there, uh it's
[L1281] [51:53.28] quite normative that people feel like
[L1282] [51:55.68] they they're being a [snorts] scholar
[L1283] [51:57.60] programmer, they're required to program
[L1284] [51:59.28] this way. And then of course there are
[L1285] [52:01.52] opinion leaders and conferences and all
[L1286] [52:03.84] these things that uh tell you how how
[L1287] [52:06.16] you should be writing your programs
[L1288] [52:09.44] where I would say I I think the most of
[L1289] [52:12.00] the scholar community is actually very
[L1290] [52:13.76] very levelheaded and and and and and I I
[L1291] [52:16.80] think most of the advice is great but uh
[L1292] [52:19.44] then um yeah uh it's it's still a
[L1293] [52:24.56] challenge because it's just too easy to
[L1294] [52:27.04] to mostly it's not really the opinion
[L1295] [52:29.52] leaders is in the in the community. But
[L1296] [52:31.84] let's say it's your boss. You have a
[L1297] [52:33.92] small team in a in a company. Your boss
[L1298] [52:35.68] came from Haskell and says, "Hey, this
[L1299] [52:37.68] is great. We do exactly like Haskell.
[L1300] [52:39.44] The whole thing." And then two years
[L1301] [52:41.20] later, the boss's boss says, "No, nobody
[L1302] [52:43.28] can understand this code. This code and
[L1303] [52:45.12] the project is canled." So these things
[L1304] [52:47.20] happened in in in in the industry. Uh
[L1305] [52:50.32] I'm not saying that they they that all
[L1306] [52:53.28] projects are like that. Not at all. I
[L1307] [52:54.80] mean there are lots of really great
[L1308] [52:56.16] success stories of Scala but that's
[L1309] [52:58.72] essentially a challenge in terms of
[L1310] [53:01.28] tech. Um I I think in the end um I wish
[L1311] [53:08.16] we had been a bit less dependent on the
[L1312] [53:10.56] JVM u uh in the sense that we took a lot
[L1313] [53:14.48] from Java that intuitively makes sense
[L1314] [53:18.16] but in the end and and was very
[L1315] [53:20.72] important for interrupt but in the end
[L1316] [53:22.48] wasn't wasn't
[L1317] [53:24.40] could have been done better. So for
[L1318] [53:26.00] instance uh in in Java being an object-
[L1319] [53:30.40] oriented language you have universal
[L1320] [53:32.08] methods like tworing and equals and hash
[L1321] [53:34.48] code and they're defined for everything
[L1322] [53:36.72] and languages like Rust or or Haskell
[L1323] [53:39.92] there are no more more discriminating.
[L1324] [53:41.76] They have a thing called type classes
[L1325] [53:43.20] where essentially you at compile time
[L1326] [53:45.20] you tell exactly where you have equality
[L1327] [53:47.76] and and hash code and these things and
[L1328] [53:49.52] it's a bit more tedious to set these
[L1329] [53:51.52] things up but it it in the end it's also
[L1330] [53:55.12] safer. So I wish we had that and and we
[L1331] [53:57.84] did we couldn't because we sort of
[L1332] [53:59.76] adapted Java's notion of what what an
[L1333] [54:02.24] object is and it already came with all
[L1334] [54:04.64] these things which is sort of very
[L1335] [54:06.64] convenient but in the end uh caused
[L1336] [54:09.12] friction. If I went back to you at that
[L1337] [54:11.92] time when you were starting it, I said,
[L1338] [54:13.68] "What do you think's going to happen 20
[L1339] [54:15.20] years from now?" What would you have
[L1340] [54:16.40] said?
[L1341] [54:17.36] >> I would probably have said that uh well,
[L1342] [54:19.84] it was a footnote in memory. Uh uh
[L1343] [54:22.64] because I mean, let's face it, you you
[L1344] [54:24.40] do a you do a thing and initially we had
[L1345] [54:26.56] maybe five users or something like that
[L1346] [54:28.72] outside our group, some something like
[L1347] [54:30.88] that, right? So, so and you don't really
[L1348] [54:33.36] expect that it would change a lot. Uh
[L1349] [54:37.84] and so I don't know I think it was was
[L1350] [54:41.92] quite quite by surprise that this
[L1351] [54:43.84] actually happened. Uh
[L1352] [54:46.32] and um I think the reason why it
[L1353] [54:49.36] happened was that at the [clears throat]
[L1354] [54:51.52] time
[L1355] [54:53.20] um Scala was a good
[L1356] [54:56.96] bridge between dynamic languages that
[L1357] [54:59.52] are slow and sometimes they crash and
[L1358] [55:03.28] solid languages, statically typed
[L1359] [55:05.60] languages like Java uh which were at the
[L1360] [55:08.32] time quite cumbersome to write code and
[L1361] [55:10.40] there was a lot of ceremony and things
[L1362] [55:12.48] like that and and Scola to the inferred
[L1363] [55:15.52] types. So you had types but you didn't
[L1364] [55:17.60] see them much. So it felt like a dynamic
[L1365] [55:19.76] language. Uh but it had also the
[L1366] [55:21.92] solidity of essentially a good platform.
[L1367] [55:24.32] And I think that's what made it. And
[L1368] [55:26.56] we've we've been copied a lot by a lot
[L1369] [55:28.96] of other languages that put in in these
[L1370] [55:30.88] features then five or 10 years later or
[L1371] [55:33.12] things like that. But at the time it was
[L1372] [55:34.96] sort of scala that that was the first
[L1373] [55:36.64] one that had it and that's sort of why
[L1374] [55:39.04] it happened. Um but um I wouldn't have
[L1375] [55:42.00] foreseen that by no means.
[L1376] [55:44.08] >> Looking back on your career uh when you
[L1377] [55:46.88] just graduated college and kind of
[L1378] [55:48.88] started your career um knowing what you
[L1379] [55:51.28] know today what advice would you give
[L1380] [55:53.60] your younger self?
[L1381] [55:55.68] >> I I think to take risks be adventurous
[L1382] [55:58.48] paid pay it out. So essentially don't
[L1383] [56:01.84] follow
[L1384] [56:04.24] the the mainstream. Uh if if you take a
[L1385] [56:07.12] fancy to do something wild uh and crazy
[L1386] [56:10.72] technically take the time to do it and
[L1387] [56:13.36] do it. Um uh but I mean yeah so that's
[L1388] [56:16.40] what I would of course I mean you still
[L1389] [56:18.40] need to sort of stay on track somewhat
[L1390] [56:20.48] but uh I don't want to you to exaggerate
[L1391] [56:23.20] that either but [laughter] but yeah so
[L1392] [56:25.20] so basically be a bit non-confirmist.
[L1393] [56:28.72] >> Awesome. Well, thank you so much for
[L1394] [56:30.48] your time, professor. I really
[L1395] [56:31.84] appreciate it.
[L1396] [56:32.80] >> Thank you, Ryan.
[L1397] [56:34.00] >> Hey, thank you for watching this
[L1398] [56:35.12] podcast. If you liked it and you want to
[L1399] [56:36.72] see the show grow, please support with a
[L1400] [56:39.04] comment or a like. Also, if you have any
[L1401] [56:42.00] recommendations for people you want me
[L1402] [56:43.68] to bring on, please drop a comment.
[L1403] [56:46.24] Guests like Barbara Liskoff, Mike
[L1404] [56:48.48] Stonereaker, Mark Brooker, these were
[L1405] [56:50.88] all people that I brought on because
[L1406] [56:52.88] someone left a comment. On another note,
[L1407] [56:55.12] aside from the podcast, I'm working on
[L1408] [56:57.04] building the ergonomic keyboard that I
[L1409] [56:58.96] wish existed. Here's a glance at the
[L1410] [57:01.12] prototype. It's a split keyboard, so
[L1411] [57:03.36] there's two sides. Um, this is in the
[L1412] [57:05.52] case, but yeah, we launched on
[L1413] [57:07.04] Kickstarter and we hit our goal within 8
[L1414] [57:09.28] hours of launching. I really appreciate
[L1415] [57:10.96] it if you were one of the people who
[L1416] [57:12.32] grabbed one of the early units. Um,
[L1417] [57:14.64] we're now working on the long journey of
[L1418] [57:16.48] building the tooling now. So, if you
[L1419] [57:18.32] still want to pick one up, I've left the
[L1420] [57:20.40] late pledges open on Kickstarter, so you
[L1421] [57:22.96] can grab one there. I'll put a link in
[L1422] [57:24.64] the description. Thank you again for
[L1423] [57:26.96] watching the podcast and I'll see you in
[L1424] [57:29.20] the next
