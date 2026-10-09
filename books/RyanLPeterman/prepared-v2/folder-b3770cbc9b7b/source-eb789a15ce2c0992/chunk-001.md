Chunk 1; segments 1–373. 

# Creator of Lua: What People Get Wrong About Scripting Languages | Roberto Ierusalimschy

Source ID: source-eb789a15ce2c0992
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lua_What_People_Get_Wrong_About_Scripting_Languages_Roberto_Ierusalimschy_en.txt
Video: https://www.youtube.com/watch?v=jCZnFKk6M9A

[L10] [00:00.00] It's completely feasible that you won't
[L11] [00:03.08] have programming languages.
[L12] [00:04.96] >> This is Roberto, the creator of the Lua
[L13] [00:07.40] programming language, and I asked him
[L14] [00:09.24] all about programming language design.
[L15] [00:11.60] >> C++ I think is a good example of a
[L16] [00:14.00] language that is really, really complex.
[L17] [00:16.64] And JavaScript I think it's even worse.
[L18] [00:19.28] I always joke that the JavaScript the
[L19] [00:21.16] good part here
[L20] [00:22.64] a very thin book comparatively official
[L21] [00:26.24] JavaScript book.
[L22] [00:28.36] >> Given how [snorts] much AI has been
[L23] [00:29.96] progressing, would you still recommend
[L24] [00:31.92] people learn computer science today?
[L25] [00:34.76] >> If you really think about that, it's
[L26] [00:37.08] really difficult to recommend people
[L27] [00:38.92] learning anything.
[L28] [00:41.32] >> Here's the full episode.
[L29] [00:46.48] In 2023, Lua was the second highest
[L30] [00:50.36] programming language by growth according
[L31] [00:52.44] to contributors on GitHub.
[L32] [00:55.40] And I saw that it was also used in
[L33] [00:58.28] famous games like World of Warcraft and
[L34] [01:00.36] Roblox. And so, I wanted to ask you what
[L35] [01:03.80] kind of programming language is Lua and
[L36] [01:05.96] what sets it apart?
[L37] [01:07.68] >> Lua is a language that you usually use
[L38] [01:10.88] together with combined it with another
[L39] [01:13.04] language like C or C++ and then you have
[L40] [01:16.60] an architecture where
[L41] [01:18.48] Lua takes care of the more dynamic part
[L42] [01:22.28] of your program, things that change more
[L43] [01:24.64] frequently, things that are are not so
[L44] [01:29.40] resource intensive, the the hard parts
[L45] [01:33.08] you have written in C or C++. So, it's
[L46] [01:36.24] typically what is called a scripting
[L47] [01:38.48] language.
[L48] [01:39.80] There is a some confusion I think
[L49] [01:42.08] between scripting languages and dynamic
[L50] [01:44.88] languages. And people just I think
[L51] [01:47.28] consider that a dynamic language to be
[L52] [01:49.52] more or less the same thing as a
[L53] [01:51.32] scripting language.
[L54] [01:53.04] And they are not exactly the same thing.
[L55] [01:55.32] So, for instance, a big difference
[L56] [01:58.08] between Lua and several other scripting
[L57] [02:01.96] languages is that
[L58] [02:03.52] for scripting, you have two typical
[L59] [02:05.76] uses. You can have the the the that I
[L60] [02:08.72] call who has the main loop.
[L61] [02:11.64] So, you can you can have the program
[L62] [02:14.12] written in C
[L63] [02:16.44] and calling Lua
[L64] [02:18.32] or you have your program written in Lua
[L65] [02:20.96] calling C.
[L66] [02:23.52] And for several
[L67] [02:26.36] called scripting languages are actually
[L68] [02:29.00] you
[L69] [02:30.00] you don't have to, but it's much more
[L70] [02:32.92] easy to use if you have your program
[L71] [02:35.56] written in the scripting language and C
[L72] [02:39.16] language is only for your libraries.
[L73] [02:42.32] And Lua is very good fit when you want
[L74] [02:44.92] the reverse. You want the the the the
[L75] [02:46.96] program written in C and then you you
[L76] [02:51.32] have calls Lua from time to time. So,
[L77] [02:55.60] the point is that Lua is very good at
[L78] [02:57.48] this that you have the the the main loop
[L79] [03:00.08] the the the program written in C and
[L80] [03:03.08] then it calls Lua for some tasks or for
[L81] [03:06.96] whatever you you you want to do. And for
[L82] [03:09.88] instance, in games, this is very
[L83] [03:12.32] important to keep the the frame ratio of
[L84] [03:16.64] the game. So, for instance, you have the
[L85] [03:18.48] loop the loop keeps the rhythm of
[L86] [03:20.43] [snorts] the game and keeps everything
[L87] [03:22.20] and then at every frame it calls Lua
[L88] [03:25.16] Lua's updates all characters all images
[L89] [03:28.32] everything in in the game and then it
[L90] [03:31.40] return to C to do the renderization etc.
[L91] [03:36.04] So,
[L92] [03:37.32] it is a very good fit. But, the main
[L93] [03:39.36] point is that that it people sometimes
[L94] [03:41.64] call this the embedding
[L95] [03:44.40] versus extending. So, you can extend the
[L96] [03:47.92] scripting language with C or you can
[L97] [03:50.32] then can embed the scripting language
[L98] [03:52.92] into C.
[L99] [03:55.44] And so may several languages are very
[L100] [03:58.44] good only for extending while Lua is
[L101] [04:01.32] really good for both embedding and
[L102] [04:04.24] extending.
[L103] [04:05.52] >> Why is Lua good for embedding and Python
[L104] [04:08.80] it's almost the opposite?
[L105] [04:10.72] >> Because in Lua since the beginning Lua
[L106] [04:13.20] was thought about Lua as a library.
[L107] [04:16.56] Since the beginning Lua was written as a
[L108] [04:19.28] library. So I think that's the the main
[L109] [04:22.40] difference. Lua has a standalone program
[L110] [04:25.44] that I mean you can call Lua in your
[L111] [04:27.52] console, in your common line, but that
[L112] [04:30.72] program is just a client of the official
[L113] [04:34.20] client of the library following the the
[L114] [04:36.80] same API that any other program can use.
[L115] [04:40.08] So this idea of language as a library, I
[L116] [04:43.40] think it's not very common. It's
[L117] [04:45.60] something that is very particular in
[L118] [04:48.44] Lua.
[L119] [04:49.12] >> When you design a language as a library,
[L120] [04:51.80] what are the unique, I guess, um,
[L121] [04:54.96] design decisions?
[L122] [04:56.28] >> I think that goes
[L123] [04:59.20] a lot of small
[L124] [05:01.28] small and big details. For instance,
[L125] [05:03.64] your your idea of what is your global
[L126] [05:06.60] space or your about scopes of variables,
[L127] [05:11.16] about exception handling. For instance,
[L128] [05:13.92] it's very important that it's very
[L129] [05:15.60] common in Lua that you raise an
[L130] [05:17.72] exception in Lua but catch the exception
[L131] [05:21.72] in C. So all these things about how you
[L132] [05:25.28] do exception handling in the language.
[L133] [05:28.08] Another
[L134] [05:29.48] It's not a big deal but it's a For
[L135] [05:31.20] instance, most dynamic languages, that's
[L136] [05:33.28] almost a
[L137] [05:34.24] definition of a dynamic language. They
[L138] [05:36.40] have an eval
[L139] [05:38.32] function that you can give a piece of
[L140] [05:41.00] code and then it executes that code.
[L141] [05:44.64] In Lua we don't instead of eval we have
[L142] [05:47.84] a function that we call the load.
[L143] [05:50.68] That you give a piece of code and it
[L144] [05:52.76] returns a function
[L145] [05:55.72] an internal function like it was a Lua
[L146] [05:58.24] function that when you call that
[L147] [06:00.04] function, then you execute
[L148] [06:02.76] the the associated code. It does doesn't
[L149] [06:07.16] execute immediately. So, you have this
[L150] [06:09.96] clear separation between
[L151] [06:13.04] compiling like the the Lua code that you
[L152] [06:16.40] have and then you can do that in C. So,
[L153] [06:18.48] in C, you can get a piece of Lua code,
[L154] [06:21.40] you can compile it, check if it has
[L155] [06:23.76] errors, etc. Then you call that for
[L156] [06:27.68] instance for instance a different piece
[L157] [06:29.32] or you can even call several times. For
[L158] [06:31.40] instance, you can load functions from
[L159] [06:33.84] Lua into C, you keep them I mean in the
[L160] [06:36.96] Lua
[L161] [06:38.68] space and then you can call that same
[L162] [06:41.24] function again and again. It's not a big
[L163] [06:44.28] difference, of course, because for if
[L164] [06:47.20] you have a value, you can evaluate a
[L165] [06:49.44] function declaration and then returns
[L166] [06:52.56] that function. So, you you can If you
[L167] [06:55.16] have a value, you can do load. If you
[L168] [06:57.20] have load, you can do eval. But I think
[L169] [07:00.84] load it's
[L170] [07:02.72] it's simpler to use for that kind of
[L171] [07:05.04] thing that is when you think about
[L172] [07:07.32] libraries for instance. In Lua, you it
[L173] [07:10.96] doesn't have a global state. I think
[L174] [07:12.92] that's a I forgot that that that's a
[L175] [07:14.96] very important difference.
[L176] [07:17.08] When C starts, the first thing it has to
[L177] [07:20.60] do is to call create a new Lua state.
[L178] [07:25.56] And then everything you do, you do on
[L179] [07:28.16] that state.
[L180] [07:30.28] And that state is completely
[L181] [07:33.28] independent
[L182] [07:35.00] of everything else. So, C can for
[L183] [07:37.88] instance create another Lua state and
[L184] [07:40.80] both states are completely independent,
[L185] [07:43.64] completely there is no communication
[L186] [07:46.80] between them. And so this again shows
[L187] [07:49.68] that the
[L188] [07:51.28] And so for instance, C can use a state
[L189] [07:53.56] to do a lot of stuff and then it can
[L190] [07:55.20] close the state and all memory used by
[L191] [07:58.60] Lua released everything that Lua was
[L192] [08:01.04] using is released. For instance, if C
[L193] [08:03.92] doesn't need to use Lua anymore for a
[L194] [08:06.56] program, you release all
[L195] [08:09.04] all resources used by Lua and your
[L196] [08:11.88] program in C continues and then later it
[L197] [08:14.28] can again create another state, etc. So
[L198] [08:18.64] there's as I said there is several small
[L199] [08:21.36] or not so small decisions in the
[L200] [08:24.04] language but all the time we think about
[L201] [08:26.84] the language as
[L202] [08:28.28] is that good for embedding? Is that
[L203] [08:30.92] possible to to do embedding and things
[L204] [08:33.96] like that?
[L205] [08:35.36] >> When you think of the programming
[L206] [08:36.76] community generally, everyone is quite
[L207] [08:40.08] familiar with Python but not as familiar
[L208] [08:42.92] with Lua. I thought it might be
[L209] [08:44.80] interesting
[L210] [08:46.24] to compare the two languages. So if you
[L211] [08:48.44] compared Lua to Python, what are the
[L212] [08:51.56] pros and cons of each language design?
[L213] [08:54.96] >> Lua is a language that is intended to be
[L214] [08:57.96] used
[L215] [08:59.68] in in this idea for of
[L216] [09:03.40] scripting architecture.
[L217] [09:05.44] So the Lua for instance, it doesn't try
[L218] [09:08.60] having a lot of different libraries.
[L219] [09:11.60] If you have something that oh I want to
[L220] [09:13.28] write a a quick program for something
[L221] [09:15.44] that Python is much better. It has all
[L222] [09:18.08] the libraries you can dream about it. It
[L223] [09:20.72] has a lot of libraries built-in
[L224] [09:23.52] already into the language. So that the
[L225] [09:25.56] language is huge. It's I mean the the
[L226] [09:28.44] installation it's it's a huge so
[L227] [09:31.24] the
[L228] [09:32.84] download etc. But it
[L229] [09:35.92] it has exactly oh I need that. Oh, it's
[L230] [09:38.08] there. I need that. It's there. And Lua
[L231] [09:40.36] is almost the opposite. Some very
[L232] [09:42.36] minimalistic language because they did
[L233] [09:44.84] that thing embed Lua into your program.
[L234] [09:47.24] It doesn't use almost any resources.
[L235] [09:50.44] Most of the libraries, the important
[L236] [09:52.36] libraries that you you will use will be
[L237] [09:55.48] provided by the program itself. It will
[L238] [09:57.96] be the commands like you move a
[L239] [09:59.56] character or do some speech or things
[L240] [10:02.48] like that from the engine of of the game
[L241] [10:05.48] for in for instance if you think about
[L242] [10:07.20] games, but whatever it is. So, Lua is I
[L243] [10:10.44] think that's the the main big
[L244] [10:12.68] difference. It's They they have very
[L245] [10:14.76] different goals.
[L246] [10:16.48] >> I saw some benchmarks and I saw that Lua
[L247] [10:18.68] is much faster than Python. Why is that?
[L248] [10:22.48] >> That that
[L249] [10:23.80] Those benchmarks are are not exactly,
[L250] [10:27.20] but I think that the main point is
[L251] [10:29.04] exactly One things that Lua does have
[L252] [10:32.64] these
[L253] [10:34.08] focus on on performance. Again, in the
[L254] [10:37.60] realm of scripting languages doesn't
[L255] [10:40.44] want to compete with C or C++. But in
[L256] [10:43.56] the realm of dynamic mostly now it's
[L257] [10:46.36] dynamic language, not scripting
[L258] [10:48.08] languages. We have some focus on
[L259] [10:50.52] performance. So, I think this is a a
[L260] [10:53.24] first difference. Python is exactly is
[L261] [10:55.32] much more I think that it's a a decision
[L262] [10:58.24] that they make. Performance is not that
[L263] [11:00.08] important. It's more important to be
[L264] [11:01.84] flexible, to be easy to do whatever you
[L265] [11:04.72] want to do. That in Lua sometimes we do
[L266] [11:07.72] not put some features because we think
[L267] [11:10.44] that there is no way to implement that
[L268] [11:12.60] efficiently. But also I think some part
[L269] [11:16.04] of that performance difference comes
[L270] [11:17.92] exactly because of the the size of Lua.
[L271] [11:21.04] So, most of the virtual machine fits in
[L272] [11:25.00] your cache for instance. I think there
[L273] [11:28.00] is these two big things. One is that Lua
[L274] [11:31.48] doesn't have so many features. It's not
[L275] [11:34.00] so dynamic as Python. So, in Python
[L276] [11:37.12] there is a lot of in the interactions
[L277] [11:39.12] because everything can mean something
[L278] [11:41.48] else. In Ruby, we are a little more
[L279] [11:44.20] conservative on that side. And but I
[L280] [11:47.24] think also this thing of being small
[L281] [11:49.52] also makes it naturally faster.
[L282] [11:52.96] >> So, on the distinction between scripting
[L283] [11:55.52] languages and dynamic or I guess it
[L284] [11:57.44] seems like dynamic language is a
[L285] [11:58.76] superset. Scripting language is a is a
[L286] [12:01.32] subset of that. Am I understanding that
[L287] [12:04.40] JavaScript is a dynamic language, not a
[L288] [12:08.32] scripting language from your
[L289] [12:09.60] perspective?
[L290] [12:10.72] >> Yes, exactly. Yes, exactly. Because the
[L291] [12:13.36] scripting it came the the the the the
[L292] [12:16.24] original scripting language it was bash
[L293] [12:18.92] or the shells from Unix. Of this idea
[L294] [12:22.24] that there's a language that coordinates
[L295] [12:25.04] other stuff. So, for instance, it can be
[L296] [12:27.84] extending again, you can use But the
[L297] [12:30.72] this idea that you have
[L298] [12:32.88] two different language for instance, in
[L299] [12:34.52] in the shell is only useful because you
[L300] [12:37.28] have a lot of programs written in C
[L301] [12:41.28] that are controlled by shell. So, the
[L302] [12:43.64] scripting language has this very strong
[L303] [12:45.76] idea that you have this idea of a dual
[L304] [12:48.16] language architecture. This is So,
[L305] [12:50.68] scripting means it's like it is it's the
[L306] [12:52.72] name scripting. It means you it's like a
[L307] [12:54.84] the you coordinator. You you give a
[L308] [12:57.48] script to be executed by
[L309] [13:00.84] those other other things.
[L310] [13:04.64] >> You gave a talk a while ago and someone
[L311] [13:06.92] asked you a question of, you know, what
[L312] [13:09.04] books do you recommend for, you know,
[L313] [13:11.56] studying programming languages? And you
[L314] [13:13.08] said actually
[L315] [13:14.40] that you enjoyed studying the language
[L316] [13:16.24] design of other programming languages.
[L317] [13:18.52] >> I like reading books that describe the
[L318] [13:21.16] design of
[L319] [13:23.08] of the languages. I I think the
[L320] [13:26.00] best books are those written by the
[L321] [13:28.56] author of a language about the design of
[L322] [13:31.52] that language.
[L323] [13:32.64] >> What book recommendation do you think is
[L324] [13:35.12] best on language design?
[L325] [13:37.32] >> JavaScript the good parts, for instance.
[L326] [13:40.40] The the the it's
[L327] [13:42.08] kind of old now, but I think that's I
[L328] [13:44.68] think it's a very interesting book.
[L329] [13:47.64] Although I always joke that the
[L330] [13:49.24] JavaScript the good part
[L331] [13:51.40] a very thin book comparatively.
[L332] [13:54.88] >> Official JavaScript books like
[L333] [13:57.56] >> one hand of the language is the good
[L334] [13:59.64] parts.
[L335] [14:01.36] But but I I think that book is really
[L336] [14:03.84] interesting like because exactly it it
[L337] [14:06.68] discussed the language it discusses in
[L338] [14:08.60] the bad parts and it focus on the good
[L339] [14:10.88] parts but then explains why it's there,
[L340] [14:13.80] why it it was made that way, etc. That
[L341] [14:17.44] is a book that I like.
[L342] [14:20.08] >> When we were talking about Lua, it
[L343] [14:21.80] sounds like one of the things that sets
[L344] [14:23.44] Lua apart is the performance and how
[L345] [14:26.72] minimal it is.
[L346] [14:28.24] And when I was reading about Lua, I saw
[L347] [14:30.16] that there's Lua Jit. How does the Lua
[L348] [14:33.28] Jit work?
[L349] [14:34.64] >> Lua Jit
[L350] [14:35.96] the first thing that's completely
[L351] [14:37.72] different project. It doesn't have
[L352] [14:40.08] anything to do with us. But it's a
[L353] [14:42.76] incredible piece of of software that is
[L354] [14:46.64] is a just-in-time compiler for Lua
[L355] [14:48.84] that's and I think exactly one of the
[L356] [14:52.04] reasons
[L357] [14:53.40] it works so well on top of Lua is
[L358] [14:56.00] because of the simplicity
[L359] [14:58.32] of
[L360] [14:59.04] Lua. It's a very regular language. I
[L361] [15:01.44] mean it has a very as I said it doesn't
[L362] [15:03.96] have many exceptions or too many
[L363] [15:07.48] indirections or things that so it's not
[L364] [15:11.64] that dynamic. I mean everything can mean
[L365] [15:14.56] something completely different. So that
[L366] [15:17.40] I think that gives a very good language
[L367] [15:20.56] for a Jit. But the the the the the Mike
[L368] [15:22.68] Paul is the name of the the the guy that
[L369] [15:25.52] made the the in the I think he's still
[L370] [15:28.28] working on that on the first legit. He's
[L371] [15:31.08] It's unbelievable his work.
[L372] [15:33.52] >> What makes writing a legit difficult?
[L373] [15:36.56] >> The first thing that for me I don't want
[L374] [15:39.36] to get involved with legit is because
[L375] [15:41.68] it's machine dependent. It's not very
[L376] [15:44.32] productive. I mean, you you do a lot of
[L377] [15:46.60] work and it only works on that
[L378] [15:48.56] architecture. And then I want to running
[L379] [15:51.20] another architecture. But, Mike Paul he
[L380] [15:54.40] created a kind of
[L381] [15:57.56] pseudo pseudo assembler that he writes
[L382] [16:00.88] in this assembly and then he translates
