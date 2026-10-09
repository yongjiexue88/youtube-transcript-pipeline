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
[L383] [16:03.60] that assembler through real machine
[L384] [16:05.84] pulled of the different machines. So,
[L385] [16:08.16] trying to unify the different
[L386] [16:10.40] architectures. So, there is a a lot of
[L387] [16:12.60] work, but I I don't like it. I I think
[L388] [16:15.04] architecture I
[L389] [16:18.08] I like to study, but I don't like to to
[L390] [16:20.76] to to work with because I think it's
[L391] [16:23.20] very unstable. Each new version they
[L392] [16:25.52] change that or they change that the I
[L393] [16:28.28] mean they they change the ABI for
[L394] [16:30.68] something and then now the stack has to
[L395] [16:32.96] be aligned in in some very
[L396] [16:35.80] particular way. And so
[L397] [16:38.80] And [clears throat] the of course also
[L398] [16:40.40] to to get that performance that he gets
[L399] [16:44.12] he made the what's called the trace
[L400] [16:47.04] compiler. The idea of a trace compiler
[L401] [16:49.96] that instead of a function
[L402] [16:52.72] and compiling a function
[L403] [16:55.24] it could it works like a
[L404] [16:57.88] any legit that it tries to detect things
[L405] [17:00.76] that are executed frequently. And so it
[L406] [17:03.80] starts what's called a trace. It it gets
[L407] [17:07.12] recording everything that the code is
[L408] [17:10.36] doing including function calls, etc.
[L409] [17:14.04] Until it closes the loop.
[L410] [17:17.20] And then it compiles that loop
[L411] [17:20.40] including function calls, etc.
[L412] [17:22.52] Everything in line. It com-
[L413] [17:24.72] compiles that for that specific, for
[L414] [17:27.60] instance, so that number of happened to
[L415] [17:29.92] be an integer, so it compiles after the
[L416] [17:32.96] number will be an integer again, and
[L417] [17:35.48] there is a lot of checks just check if
[L418] [17:37.72] everything is as assumed, and then it
[L419] [17:41.00] executes the loop. And then this is
[L420] [17:43.08] very, very, very fast. But anything that
[L421] [17:46.68] is different, for instance, you call
[L422] [17:48.92] again that you call it frequently with
[L423] [17:51.76] integers, and suddenly you call through
[L424] [17:53.88] with a float, then at some part of the
[L425] [17:56.52] code it's it is
[L426] [17:58.88] it breaks the the the condition, and you
[L427] [18:01.52] have to to return to the interpreter
[L428] [18:04.84] part, and I think that's one of the
[L429] [18:07.04] worst parts is that you you have to
[L430] [18:09.16] translate the state that it's all
[L431] [18:13.24] compressed into registers, etc. For
[L432] [18:16.40] instance, you don't even have a call
[L433] [18:17.92] stack because you didn't
[L434] [18:20.00] do the call you didn't do the calls, you
[L435] [18:22.08] just inlined it. But then, oops,
[L436] [18:24.48] something went wrong. Now you have to
[L437] [18:26.76] continue interpreting, so you have to
[L438] [18:29.20] recreate the stack that you didn't
[L439] [18:31.40] create originally, etc. So, I mean, I
[L440] [18:34.88] even
[L441] [18:36.13] >> [laughter]
[L442] [18:36.36] >> even to think about that I have
[L443] [18:39.36] headaches.
[L444] [18:40.84] >> Standard Lua is portable, but to execute
[L445] [18:43.68] on a machine, it eventually gets
[L446] [18:45.12] converted into machine instructions
[L447] [18:47.56] somewhere. Where in the stack is it
[L448] [18:50.08] eventually translated to machine
[L449] [18:51.76] instructions?
[L450] [18:52.84] >> Lua is written in C. The interpreter is
[L451] [18:55.84] written in C, and then you so you you
[L452] [18:59.32] compile that into machine code, the
[L453] [19:01.96] interpreter, the Lua code. Then the
[L454] [19:04.24] point when you get some some
[L455] [19:06.72] some I mean, the Lua code the Lua
[L456] [19:08.44] interpreter code. When you get some Lua
[L457] [19:10.88] code,
[L458] [19:12.00] you do what is we call a
[L459] [19:13.36] pre-compilation,
[L460] [19:15.08] that is we we translate to an internal
[L461] [19:17.84] language,
[L462] [19:19.24] and then the interpreter is just a big
[L463] [19:21.68] loop.
[L464] [19:22.92] It's a loop with a switch. I mean,
[L465] [19:25.00] that's a a very big simplification, but
[L466] [19:27.28] that that in in general terms, a loop
[L467] [19:30.08] with a switch that get instruction,
[L468] [19:33.24] does a switch, and see all this
[L469] [19:35.16] instruction is the instructions are
[L470] [19:37.88] quite similar to a CPU. Move that, but
[L471] [19:41.96] then instead of creating it executes
[L472] [19:44.84] that structure. Move Move A to B, so it
[L473] [19:48.64] it does a
[L474] [19:49.92] move A to B and executes that, and again
[L475] [19:52.88] repeats, executes the next instruction.
[L476] [19:55.84] So, this is how a interpreter works and
[L477] [20:00.00] basically, so we we precompile a Lua.
[L478] [20:03.64] There is a compilation, but we compile
[L479] [20:05.64] for this virtual machine,
[L480] [20:07.88] and then we have this main
[L481] [20:10.92] interpreter loop that people call that
[L482] [20:13.84] just fetch each instruction. So, a jump
[L483] [20:17.88] is just a jump. You have an array of of
[L484] [20:20.36] byte codes. A jump will just go to that.
[L485] [20:23.40] You have a
[L486] [20:24.64] a counter that tells where you are in
[L487] [20:27.04] this array. A jump you just update that
[L488] [20:30.04] counter. It goes to another position of
[L489] [20:32.08] that array where you're going to So,
[L490] [20:34.40] it's like you s-
[L491] [20:36.40] you emulate the CPU in software. It's
[L492] [20:40.32] written in C,
[L493] [20:41.84] the the interpreter. This main loop is
[L494] [20:44.16] written in C.
[L495] [20:45.96] So, if you compile it in Linux, it will
[L496] [20:48.32] run in Linux or in a
[L497] [20:51.24] X86
[L498] [20:52.84] architecture, it will run in that
[L499] [20:54.80] architecture. If you compile that in the
[L500] [20:56.80] Mac, it will run in the Mac. It's a C
[L501] [20:58.96] program.
[L502] [21:00.56] >> Got it. Okay, so and that's that's the
[L503] [21:02.24] part that's not portable, and the C
[L504] [21:04.04] compiler handles that.
[L505] [21:05.72] >> Yes. Yes. Yes. The all portability of
[L506] [21:08.28] Lua comes on top of portability of C.
[L507] [21:12.16] >> How does JIT compare to ahead-of-time
[L508] [21:14.72] compilation in terms of performance?
[L509] [21:17.72] >> Both ahead-of-time Any kind of
[L510] [21:19.76] compilation is easily not easily, but it
[L511] [21:23.08] can be 10 times faster than interpreting
[L512] [21:26.12] or even 100 times faster than
[L513] [21:28.88] interpreting depending what you were are
[L514] [21:31.20] doing. But 10 times is a very good
[L515] [21:34.56] figure. Between ahead-of-time and
[L516] [21:39.08] trace compilation, then depends a lot of
[L517] [21:42.52] what you are doing.
[L518] [21:44.88] After trace compilation is particularly
[L519] [21:48.60] good for
[L520] [21:50.76] benchmarks.
[L521] [21:53.36] Because you're repeating it more or less
[L522] [21:55.76] they are very uniform. You are doing
[L523] [21:57.72] exactly the same thing again and again
[L524] [21:59.84] and again. So, then trace compilers
[L525] [22:03.48] shine. They I mean this is the best they
[L526] [22:05.84] can do.
[L527] [22:07.16] In real programs, that's
[L528] [22:10.92] depends a lot, but but but you I
[L529] [22:14.24] wouldn't say there is a clear winner
[L530] [22:16.92] between the two. I think depends a lot
[L531] [22:18.96] of the kind of problem.
[L532] [22:20.52] >> Is it possible to write an ahead-of-time
[L533] [22:23.52] compiler for Lua?
[L534] [22:24.68] >> Yes, there are there are
[L535] [22:27.48] several.
[L536] [22:28.92] None I mean I think I don't not sure if
[L537] [22:32.48] there is anyone on production quality,
[L538] [22:35.92] but for research etc. there are several.
[L539] [22:39.44] I I have a student who wrote one like a
[L540] [22:42.44] master thesis. We did
[L541] [22:45.16] simple Lua compiler ahead-of-time Lua
[L542] [22:48.40] compiler or something like that. The
[L543] [22:50.48] exactly because it was just
[L544] [22:52.26] [clears throat] it gets these opcodes
[L545] [22:54.64] and expands into
[L546] [22:56.96] into C code and then you
[L547] [22:59.80] send that through through a C compiler
[L548] [23:02.52] and then you have a head of time comp
[L549] [23:05.08] head of time compiler for Lua and it
[L550] [23:07.84] gave like three five times boosting
[L551] [23:11.44] performance. You very very
[L552] [23:14.52] as the title said it's like ridiculous
[L553] [23:17.68] simple compiler.
[L554] [23:21.28] >> I always hear there's there's compiled
[L555] [23:23.56] languages and there's dynamic or
[L556] [23:26.00] interpreted languages I guess.
[L557] [23:28.08] But really that distinction is in the
[L558] [23:30.76] tool chain not necessarily in the way
[L559] [23:33.00] that the symbols are laid out on the
[L560] [23:34.60] source code. Like I could write compiler
[L561] [23:37.24] or program that takes in Python code and
[L562] [23:40.80] then converts it into machine code and
[L563] [23:44.04] then I would have compiled Python.
[L564] [23:46.08] >> And you can interpret C code too. You
[L565] [23:48.84] can write an interpreter for C.
[L566] [23:51.88] Yes. But the the main difference is
[L567] [23:54.20] exactly what it's easy to For instance,
[L568] [23:56.96] as I said, one of the hallmarks of
[L569] [23:59.60] interpreted languages is the eval. So,
[L570] [24:03.24] if you want to compile the language and
[L571] [24:06.20] keep eval, you have to
[L572] [24:08.44] have a compiler as a library of your
[L573] [24:12.28] of your runtime because you may want to
[L574] [24:14.76] compile things
[L575] [24:16.92] during execution. This is the hallmark
[L576] [24:19.40] of a dynamic language. That's all. You
[L577] [24:21.88] can create code while running code. So,
[L578] [24:26.44] that part is that that's why
[L579] [24:30.92] more much more often than not
[L580] [24:35.00] dynamic languages are interpreted.
[L581] [24:38.52] But you can compile but then sometimes
[L582] [24:40.96] or some compilers do not handle eval at
[L583] [24:44.32] all. They say, "Oh, you can compile as
[L584] [24:46.40] long as your program doesn't have
[L585] [24:48.56] evals." The so there is some
[L586] [24:50.84] restrictions. And as I said, you can
[L587] [24:54.24] interpret C code I mean, but you'll be
[L588] [24:58.08] extremely slowly with it doesn't but
[L589] [25:02.24] >> I think one big difference I when I look
[L590] [25:04.16] at statically or you know static
[L591] [25:06.64] languages or compiled languages
[L592] [25:08.72] they they seem to have type systems in
[L593] [25:10.76] them or the type annotations.
[L594] [25:13.56] What is the role of a type system in the
[L595] [25:16.16] compilation process?
[L596] [25:18.48] >> Depends a lot of the on the type system.
[L597] [25:22.08] The several type systems like in C for
[L598] [25:25.16] instance are written to be an very
[L599] [25:28.04] important part of the compilation
[L600] [25:30.56] process. So if you have the right type
[L601] [25:33.76] system is much much easier to write a
[L602] [25:37.12] compiler.
[L603] [25:38.64] A trivial example is when the space for
[L604] [25:41.56] variables because if you know all this
[L605] [25:44.12] is an integer, this is a float, this is
[L606] [25:46.84] a double, you know exactly how many
[L607] [25:49.28] bytes of memory you need to that.
[L608] [25:52.36] Otherwise it's a massive more often than
[L609] [25:55.32] not you have to keep everything in the
[L610] [25:56.96] heap dynamically allocated and so
[L611] [26:01.48] huge
[L612] [26:03.16] penalty in performance. And for instance
[L613] [26:05.76] when you see it as I said a trivial you
[L614] [26:07.96] have an addition.
[L615] [26:09.80] A plus B. If you know the type of A
[L616] [26:13.84] A plus B, you have the type of A, the
[L617] [26:15.92] type of B, you have a compile time you
[L618] [26:18.36] know all this plus is a
[L619] [26:20.88] I'm adding two integers. I just generate
[L620] [26:23.28] the machine code to add integers and
[L621] [26:26.08] there everything it's fine. In a dynamic
[L622] [26:28.00] language as here plus
[L623] [26:30.44] I don't I I I compile
[L624] [26:32.92] to a virtual in the virtual language it
[L625] [26:35.32] is just piece of plus but then how do I
[L626] [26:38.72] at run time you have to check what is A?
[L627] [26:41.32] Oh, A is an integer, B is a float. Oh, I
[L628] [26:44.04] have to convert or B is a string or
[L629] [26:46.68] depending on the language you're if
[L630] [26:48.84] you're not doing addition you can be
[L631] [26:50.64] doing concatenation or you can just
[L632] [26:53.12] calling some and you have to do all that
[L633] [26:56.04] at runtime. So, types can be very, very
[L634] [26:59.72] important to compile efficiently, but of
[L635] [27:05.00] course you have to
[L636] [27:07.16] have a type system that
[L637] [27:10.00] that there are several language now like
[L638] [27:12.00] type type script that the
[L639] [27:14.84] types are kind of
[L640] [27:16.88] you do not guarantee that everything has
[L641] [27:19.32] the types you said
[L642] [27:21.52] they have. So, then it's impossible to
[L643] [27:24.76] use them to compile because oh, probably
[L644] [27:27.80] will be an integer, but if it's not I
[L645] [27:30.00] mean it's if it I have an integer
[L646] [27:33.08] register to put 20
[L647] [27:35.44] it must be a register or
[L648] [27:38.32] things will not work. So, but if you
[L649] [27:40.48] have the right type system they are
[L650] [27:43.56] essential for a good compilation.
[L651] [27:46.16] >> I know some programming languages have
[L652] [27:47.60] type inference, but if you did you ran
[L653] [27:50.12] type inference and you got a unambiguous
[L654] [27:53.80] set of types and then you use that in
[L655] [27:56.88] compilation. Like could you do that for
[L656] [27:58.88] Lua?
[L657] [28:00.80] >> Nope.
[L658] [28:03.20] I mean that's not computable, but a lot
[L659] [28:06.44] of people tried to to do
[L660] [28:10.08] in type inference for dynamic languages
[L661] [28:13.72] and it's really hard pro problem and
[L662] [28:16.88] it's very difficult to do anything
[L663] [28:18.88] useful in terms of performance. What you
[L664] [28:22.44] sometimes you get but you have a very
[L665] [28:25.68] restrict
[L666] [28:27.32] If you write your program in that
[L667] [28:30.04] specific way use for So, it's like you
[L668] [28:34.04] don't have the type but you write the
[L669] [28:35.96] program thinking about type and then if
[L670] [28:39.40] the program is that very particular
[L671] [28:41.68] format, then you can
[L672] [28:45.24] do type inference and everything goes
[L673] [28:47.68] well. Otherwise, either type inference
[L674] [28:50.60] doesn't work, or I mean, it works, but
[L675] [28:53.56] it actually it infers very generic types
[L676] [28:57.20] for everything, and so you cannot take
[L677] [29:00.12] advantage of of of the types. Because
[L678] [29:03.12] exactly the dynamic nature of the
[L679] [29:05.72] language. This This also happens if Lua
[L680] [29:08.88] JIT, for instance.
[L681] [29:10.60] You can get much much better performance
[L682] [29:13.72] if you have a kind of a type system in
[L683] [29:16.80] your in your mind. Usually, we do that,
[L684] [29:19.76] and you and you follow that type rules
[L685] [29:23.08] even without a type I mean, the compiler
[L686] [29:25.60] the language does not impose them on
[L687] [29:28.28] you, but you assume, "Oh, I'm going to
[L688] [29:30.24] follow those some type discipline. I'm
[L689] [29:33.48] not going to to to use the same variable
[L690] [29:36.20] to store integers and strings, etc." And
[L691] [29:39.56] then you can have much better results.
[L692] [29:43.32] >> OpenAI, [snorts]
[L693] [29:44.36] Anthropic, Cursor, and Vercel all use
[L694] [29:47.64] this product to make their lives better.
[L695] [29:49.84] And the problem it solves is when you're
[L696] [29:51.76] building SaaS or an ad product, and you
[L697] [29:54.40] want to sell to other companies, there's
[L698] [29:56.32] all these requirements you need to meet.
[L699] [29:58.40] There's SSL, there's SCIM, there's RBA,
[L700] [30:02.04] there's audit logs. These are all things
[L701] [30:03.84] that take time to integrate, but aren't
[L702] [30:06.04] the main focus of your app. WorkOS is an
[L703] [30:08.36] API layer that lets you meet all of
[L704] [30:10.00] these requirements in just a few lines
[L705] [30:12.20] of code. So, let's say you have a new
[L706] [30:14.24] SaaS product, and you want to sell to
[L707] [30:15.92] other
[L708] [30:17.04] WorkOS will solve all of these critical
[L709] [30:19.04] feature gaps for you.
[L710] [30:21.04] You can check them out at workos.com to
[L711] [30:23.60] learn more and get started, and I
[L712] [30:25.76] appreciate them for supporting my work
[L713] [30:27.60] and sponsoring this podcast. Earlier you
[L714] [30:30.08] mentioned that Lua can call C, and C
[L715] [30:33.32] could call Lua. And
[L716] [30:36.64] you mentioned we talked about the the
[L717] [30:38.88] compiler and the interpreter, and how do
[L718] [30:41.56] these pieces work together in the case
[L719] [30:43.72] where you're chaining different
[L720] [30:45.36] programming languages?
[L721] [30:47.60] >> Yeah, the the the main trick, I mean,
[L722] [30:49.64] it's not a trick, the technique
[L723] [30:52.24] for Lua calling C is a C pointers.
[L724] [30:57.20] Function pointers. There is a pointer to
[L725] [31:00.16] a function.
[L726] [31:01.48] This is part of the official C
[L727] [31:04.60] language. So, when you start Lua,
[L728] [31:08.64] suppose you are in C, yeah, as I said,
[L729] [31:11.04] you create a library.
[L730] [31:13.60] Uh all right, you create a state, a Lua
[L731] [31:15.88] state, and then you can register, you
[L732] [31:18.48] send to Lua
[L733] [31:20.60] C pointers, so function pointers, I
[L734] [31:22.80] mean, pointers to functions in your C
[L735] [31:25.68] library. Associated with names, Lua
[L736] [31:28.96] stores that in some data structure.
[L737] [31:32.52] Okay, so it says, "Oh, the function sign
[L738] [31:36.04] is associated with that pointer, etc."
[L739] [31:38.80] So, when it's it's doing the
[L740] [31:41.36] interpretation, "Oh, this instruction is
[L741] [31:44.20] call, instruction call. Let's see what
[L742] [31:47.00] it's calling. Oh, it's calling A. What
[L743] [31:49.00] is the value of A? Oh, it's a pointer to
[L744] [31:51.92] and then it calls that pointer." And
[L745] [31:54.20] then we do the call the the the C
[L746] [31:57.28] function to do that.
[L747] [31:59.92] And the when when C wants to call Lua, I
[L748] [32:04.08] I mean,
[L749] [32:04.96] a Lua function is just a data structure
[L750] [32:08.20] from the point of view of of C, just an
[L751] [32:10.88] array of byte codes of up codes, and
[L752] [32:14.48] then it's calls the Lua interpreter
[L753] [32:17.72] function, "Oh,
[L754] [32:19.48] please interpret that function for me."
[L755] [32:22.92] So, C can call Lua to interpret that
[L756] [32:25.56] function, and that function is running,
[L757] [32:27.64] and then can call a C function using a
[L758] [32:30.68] pointer, and you can have that in the
[L759] [32:33.04] stack several levels. So, you are
[L760] [32:35.08] running a Lua function that calls C, and
[L761] [32:37.48] C calls Lua again, and Lua calls C, and
[L762] [32:40.72] you have recursive stuff in that, etc.
[L763] [32:43.92] And everything works and it's just
[L764] [32:46.72] just works.
[L765] [32:48.60] >> In one of your talks on Lua, you
[L766] [32:50.88] mentioned that there's security benefits
[L767] [32:52.88] to using a scripting language. What are
[L768] [32:55.48] those benefits and how does it protect
[L769] [32:57.36] the hardware?
[L770] [32:58.40] >> It's not only hardware. Once I I I gave
[L771] [33:01.92] a talk here in in Brazil. I was called
[L772] [33:05.32] it to to give a talk in a PyCon
[L773] [33:09.16] a PyCon they they called the Python
[L774] [33:11.40] conference in Brazil. They called me for
[L775] [33:14.04] a talk. At the end of the talk I said,
[L776] [33:16.20] "Oh, Lua is we use it as a scripting
[L777] [33:18.16] language." As I said, emphasizing that
[L778] [33:21.28] thing that you have this dual language
[L779] [33:24.00] architecture and we I I know of case of
[L780] [33:27.44] Lua being used with C, with C++,
[L781] [33:30.84] with Fortran, with several different
[L782] [33:33.12] languages. And then someone in the
[L783] [33:35.08] audience says, "Oh, we also
[L784] [33:37.72] use Lua for scripting Python programs."
[L785] [33:41.08] And what what's that the case? They they
[L786] [33:43.08] they have a huge Python program
[L787] [33:45.80] for financial stuff that has a do a lot
[L788] [33:49.32] of financial transactions, etc. And they
[L789] [33:52.56] wanted to do script I mean to have a
[L790] [33:55.08] like
[L791] [33:56.00] a common line where you could write
[L792] [33:58.24] instructions to be executed by the the
[L793] [34:02.76] at runtime, for instance, for debugging
[L794] [34:05.04] or for inspecting, for
[L795] [34:07.20] whatever you need some kind of end-user
[L796] [34:10.44] programming.
[L797] [34:11.68] But they said exactly what I was talking
[L798] [34:14.28] about spaces. In Python,
[L799] [34:17.68] basically, if you have a common line
[L800] [34:20.56] then you're going to run Python, that
[L801] [34:22.96] Python can do whatever it wants to do
[L802] [34:27.68] in your program. There is no way to
[L803] [34:29.40] protect. So, if you gave that to the
[L804] [34:32.16] user, the user could do whatever it
[L805] [34:34.48] wanted to do.
[L806] [34:36.60] I mean
[L807] [34:37.72] for the program. And so, the program
[L808] [34:39.36] would break a lot of invariants of a lot
[L809] [34:41.76] of important stuff in the files it kept,
[L810] [34:44.04] etc. And so, what they did, they gave
[L811] [34:47.76] the thinking Lua because as I said, as
[L812] [34:50.08] Lua you create a state. For instance, as
[L813] [34:52.72] I just mentioned, you can only call C
[L814] [34:55.68] functions.
[L815] [34:57.32] That's is true in Python again, but the
[L816] [35:00.00] particularity You can only call C
[L817] [35:03.04] functions if you give the C pointer
[L818] [35:06.16] to Lua.
[L819] [35:07.40] So, have a very strict or any there
[L820] [35:10.00] there is very little as I said, there is
[L821] [35:12.00] a library. When you create a Lua state,
[L822] [35:14.44] it has
[L823] [35:15.72] no functions at all.
[L824] [35:18.28] There is nothing. I mean, you cannot
[L825] [35:19.80] open files. Everything there are we call
[L826] [35:22.96] standard libraries. Usually, you open
[L827] [35:26.68] a state and you register those standard
[L828] [35:29.84] libraries in Lua. So, you have the the
[L829] [35:32.52] minimum like you have mathematical
[L830] [35:34.44] functions, etc. But you can open a state
[L831] [35:37.12] and has no functions at all in Lua.
[L832] [35:40.84] It can only do things calling those
[L833] [35:43.32] specific functions you you you gave. So,
[L834] [35:46.84] they they used Lua to have this kind of
[L835] [35:49.16] control. You can write Lua code here,
[L836] [35:51.76] but that Lua code can only do very
[L837] [35:54.32] specific things in the Python program.
[L838] [35:57.44] You cannot call any Python function or I
[L839] [36:01.36] mean, build any kind of Python data
[L840] [36:03.76] structure, etc. So, was this a a nice
[L841] [36:07.16] example. In the case of hardware, it's
[L842] [36:09.40] the same thing. You cannot just go in
[L843] [36:12.44] the For instance, there is a a port a
[L844] [36:15.16] hardware port that controls the speed of
[L845] [36:18.32] the fan
[L846] [36:19.72] that that keeps the temperature of the
[L847] [36:22.04] CPU. And if you put that very low, you
[L848] [36:25.32] can really burn the CPU. I mean, because
[L849] [36:27.84] the CPU gets very hot. And so, we've you
[L850] [36:30.60] have a seat you cannot call C directly.
[L851] [36:33.32] You must call Bingo, and only Lua has
[L852] [36:36.40] access to that. So, if you can only
[L853] [36:39.00] program in Lua, it's a doll Lua, then
[L854] [36:41.24] you you check whether the the numbers
[L855] [36:44.36] you are giving are are precise or
[L856] [36:46.92] whatever it has to check, and then it
[L857] [36:49.84] calls
[L858] [36:51.12] >> It's kind of like a sandbox environment.
[L859] [36:53.56] >> Yes, exactly. Yes, sandbox is the exact
[L860] [36:57.36] word for that.
[L861] [36:58.84] >> I saw there's this, I guess, paper,
[L862] [37:01.20] maybe it was a
[L863] [37:02.92] article you wrote on the history of Lua
[L864] [37:05.28] with several other people, and I thought
[L865] [37:07.48] there were some interesting quotes in
[L866] [37:08.80] there I kind of wanted to ask you about.
[L867] [37:10.40] So, um one of them
[L868] [37:13.40] it says that there's this old joke that
[L869] [37:16.20] says that a camel is a horse designed by
[L870] [37:19.16] a committee.
[L871] [37:20.28] >> Yes, that's not mine. That's a real
[L872] [37:24.16] old joke.
[L873] [37:25.92] >> Does that mean that you think the best
[L874] [37:28.32] programming languages are designed by as
[L875] [37:31.16] few people as possible?
[L876] [37:33.04] >> Yes, I do think. Yes.
[L877] [37:35.40] Because there's one thing that that it's
[L878] [37:38.52] easy to to observe it it's is is this.
[L879] [37:41.76] If you have a committee
[L880] [37:44.00] writing a language,
[L881] [37:46.48] everyone wants to put something
[L882] [37:50.60] from themselves into the language. So,
[L883] [37:53.76] you have that your favorite mechanism,
[L884] [37:56.84] and you will fight whatever it takes to
[L885] [37:59.72] put your favorite mechanism into the
[L886] [38:02.32] language. And very few people will fight
[L887] [38:06.84] against
[L888] [38:08.40] putting anything in the language.
[L889] [38:11.48] I mean, some people say, "Oh, no, this
[L890] [38:13.40] is too much. This is too complicated."
[L891] [38:15.24] But people fight much more fiercely for
[L892] [38:19.52] to for put something they you in the
[L893] [38:21.84] language, then
[L894] [38:23.44] against putting something in the
[L895] [38:25.60] language. So, when you have a committee,
[L896] [38:28.32] the the tendency is so let's
[L897] [38:30.96] keep adding stuff to let's keep adding
[L898] [38:33.28] stuff, and people sometimes even do not
[L899] [38:36.04] understand. I mean, they were not sure
[L900] [38:37.84] if everybody there is really
[L901] [38:40.92] know the language
[L902] [38:43.04] well. Oh, well, I'm not putting that,
[L903] [38:45.00] but that fits with all the parts of the
[L904] [38:47.36] Oh, I didn't even know the language has
[L905] [38:49.12] this other part. I mean, so
[L906] [38:51.68] things sometimes do not fit together
[L907] [38:53.96] very well, etc. So, first you have a
[L908] [38:56.76] what's called a conceptual integrity.
[L909] [38:59.92] It's a name that give that everything
[L910] [39:02.12] fits together, everything
[L911] [39:04.88] it's designed if
[L912] [39:07.00] everything else in mind, etc. It's much
[L913] [39:09.84] easier to Yeah, I'm not saying I mean,
[L914] [39:11.76] Lua has several
[L915] [39:14.08] wrong stuff regarding because of with
[L916] [39:17.48] time, etc. There you make mistakes, but
[L917] [39:20.88] it's much easier to get things
[L918] [39:24.08] right if you have a small group of
[L919] [39:27.08] people that everybody knows what
[L920] [39:29.16] everybody else is thinking. I mean, you
[L921] [39:32.04] are deciding whether to put something in
[L922] [39:34.36] the language or not. It's much easier to
[L923] [39:37.36] change your mind
[L924] [39:39.44] if you do not put something, and then
[L925] [39:41.88] later you decide to add it to the
[L926] [39:44.72] language, than to add something, and
[L927] [39:47.44] then later you decide, "Oh, I shouldn't
[L928] [39:49.92] have
[L929] [39:51.16] that was not a good idea." So, when in
[L930] [39:54.28] doubt, our default is always don't put
[L931] [39:57.76] it. If you're not very sure, don't put
[L932] [40:00.36] it. We can always add that later, and so
[L933] [40:03.76] keep the door open through to
[L934] [40:06.80] change your mind.
[L935] [40:08.72] >> I saw in the original Lua programming
[L936] [40:11.16] language that there was no Boolean type,
[L937] [40:13.20] and I've never seen that before. Why was
[L938] [40:16.76] there no Boolean in the original Lua?
[L939] [40:19.56] >> Well, C doesn't have Booleans.
[L940] [40:22.32] I mean, the the the the original C and
[L941] [40:24.56] C90 up to C99
[L942] [40:28.32] using integers. If it's zero, it's
[L943] [40:30.68] false. If it's different from zero, it's
[L944] [40:33.64] true. And
[L945] [40:36.20] and people lived quite well with
[L946] [40:39.08] with that Lisp. I mean, there are
[L947] [40:41.60] several languages that don't have
[L948] [40:43.48] Booleans. And actually, we only put
[L949] [40:46.96] Booleans in Lua
[L950] [40:48.88] because we wanted false. True is
[L951] [40:51.72] completely useless in Lua. Nobody used
[L952] [40:54.20] true. And nobody such a joke, but it's
[L953] [40:56.64] too strong, but
[L954] [40:58.28] it's it's not very useful. You can use
[L955] [41:01.56] almost any other value for true.
[L956] [41:04.20] But the the the the the problem is that
[L957] [41:05.92] the in Lua the the
[L958] [41:08.40] nil, that special value nil,
[L959] [41:12.68] is in a table. It is equivalent to the
[L960] [41:16.44] key not being present.
[L961] [41:20.16] You all think better that was a good
[L962] [41:22.08] that
[L963] [41:23.04] decision, but it's very embedded in the
[L964] [41:26.52] design of the language. And it has with
[L965] [41:28.88] this strong concept that a table
[L966] [41:32.36] a key that is not present in
[L967] [41:35.20] in a table that is an associative array,
[L968] [41:38.24] it has a nil value. It's completely
[L969] [41:40.52] indistinguishable
[L970] [41:42.48] whether it's absent. I mean, absent
[L971] [41:44.80] means it has a nil value. Nil valent
[L972] [41:47.36] means it's absent. And so, sometimes you
[L973] [41:50.40] want to have a false value. And but you
[L974] [41:53.56] want to know what it is there in the
[L975] [41:55.84] table. And so, we needed a false. To
[L976] [41:58.92] have a false, you can put in the table
[L977] [42:01.80] and it's completely different from being
[L978] [42:04.20] absent. You know, there is a key and the
[L979] [42:07.12] key has a false value. So, we needed a a
[L980] [42:11.72] value. And if you're going to have a
[L981] [42:13.32] false, then
[L982] [42:15.24] we added true to maybe it would make
[L983] [42:17.84] sense to have false without true, but
[L984] [42:19.76] with true it's almost useless.
[L985] [42:22.76] >> Why not use zero as false if you're okay
[L986] [42:25.48] with one as true?
[L987] [42:27.16] >> It could be we could have used it, but
[L988] [42:29.40] that
[L989] [42:30.64] Among other things, that would be a a
[L990] [42:33.04] big change because exactly it didn't was
[L991] [42:36.20] that way, so we we added that late here
[L992] [42:40.16] in the language, so changing zero to
[L993] [42:42.64] false would be a very big
[L994] [42:45.24] incompatibility.
[L995] [42:47.56] But it could be for instance in in in
[L996] [42:50.12] Python, I think a lot of stuff are are
[L997] [42:53.80] false. I mean, zero is false, empty list
[L998] [42:56.68] is false, empty In JavaScript, I think
[L999] [42:59.52] it's even worse. I I don't re-
[L1000] [43:02.12] don't recall exactly, but I mean
[L1001] [43:05.24] This is kind of arbitrary. I mean, you
[L1002] [43:07.84] we could have for instance
[L1003] [43:10.36] nil, false, zero, empty string. I mean,
[L1004] [43:14.20] it
[L1005] [43:14.96] It just depends the kind of test that
[L1006] [43:17.12] you use.
[L1007] [43:18.48] It's not
[L1008] [43:19.76] In dynamic languages, it's very easy.
[L1009] [43:22.56] >> Python has the like you're describing
[L1010] [43:24.76] the truthy values and the falsy values,
[L1011] [43:28.24] or I guess they can be interpreted as
[L1012] [43:30.32] false. And but it's it's more implicit,
[L1013] [43:34.36] less explicit, and I know JavaScript is
[L1014] [43:37.44] even further on that spectrum where you
[L1015] [43:39.56] can do some really weird stuff that
[L1016] [43:41.68] implicitly has some behavior. Do you
[L1017] [43:44.48] think that design direction is good or
[L1018] [43:47.76] bad?
[L1019] [43:48.72] >> It's like a small compact, it's more
[L1020] [43:52.24] easy to write stuff. And but you always
[L1021] [43:55.24] have this balance in any language is
[L1022] [43:57.16] almost anything. The more flexible you
[L1023] [44:00.32] you
[L1024] [44:01.04] the more flexibility you have,
[L1025] [44:03.56] the less
[L1026] [44:05.92] protection you have. In C, you have
[L1027] [44:08.40] something like like that. People do not
[L1028] [44:10.60] notice, but
[L1029] [44:12.12] because C's typed.
[L1030] [44:14.16] But, you can check whether an integer
[L1031] [44:17.80] is true or false.
[L1032] [44:19.48] You can check whether a float
[L1033] [44:21.88] is true or false directly because again
[L1034] [44:24.28] it checks whether the float is zero or
[L1035] [44:26.72] different from zero. You can check
[L1036] [44:29.12] whether a pointer is nil or different
[L1037] [44:32.96] from nil because in C nil is a magic
[L1038] [44:36.48] zero.
[L1039] [44:37.52] So, it's kind of if you do not write any
[L1040] [44:40.56] test, it has an implicit test like
[L1041] [44:43.28] different from zero.
[L1042] [44:45.00] And this zero can be a integer, can be a
[L1043] [44:48.88] float, can be a pointer. So, in C also
[L1044] [44:52.20] you have this kind of
[L1045] [44:53.88] flexibility. It's just that you have to
[L1046] [44:56.44] be more explicit usually.
[L1047] [44:59.28] This
[L1048] [45:00.08] avoids errors, but
[L1049] [45:02.08] so this you have always this balance
[L1050] [45:04.16] between
[L1051] [45:05.96] easy to write and
[L1052] [45:07.92] easy to make mistakes.
[L1053] [45:10.08] >> I saw that
[L1054] [45:11.76] Lua is one indexed instead of zero
[L1055] [45:14.44] indexed, and I I had never seen a
[L1056] [45:17.16] programming language like that in my
[L1057] [45:18.88] experience.
[L1058] [45:20.16] >> There was a lot of programming languages
[L1059] [45:22.64] like that.
[L1060] [45:23.92] >> So, yeah, why why is it one indexed?
[L1061] [45:26.68] >> Because everything in the real world are
[L1062] [45:29.60] one indexed. If you have a book, you
[L1063] [45:31.88] have the the chapter one, chapter two.
[L1064] [45:34.52] Nobody number chapters as zero, one,
[L1065] [45:37.80] two, three. Only program- programmers
[L1066] [45:40.48] are the only Even mathematicians, if you
[L1067] [45:43.16] get a mathematic book, a book of
[L1068] [45:45.52] mathematic, any sequence, it's A1 and
[L1069] [45:49.04] A2, A3. If you get a matrix, the first
[L1070] [45:52.68] element is A11, A12, and then A
[L1071] [45:56.52] Everything
[L1072] [45:57.92] is written with a Only
[L1073] [46:00.52] in programming language that is this of
[L1074] [46:02.68] zero.
[L1075] [46:03.64] And the funniest part is that for
[L1076] [46:06.12] instance Fortran
[L1077] [46:07.88] that now it's it's very old language,
[L1078] [46:10.04] but to index it from one. In Pascal you
[L1079] [46:13.40] can choose I mean you write an array,
[L1080] [46:16.40] you can say this array means index it
[L1081] [46:18.44] from minus five to five. And so it's
[L1082] [46:22.08] it's index it from whatever value you
[L1083] [46:24.24] want to whatever value
[L1084] [46:26.68] you want.
[L1085] [46:28.40] Zero became
[L1086] [46:30.64] extremely popular
[L1087] [46:33.16] because of C.
[L1088] [46:35.08] C uses zero and a lot of languages copy
[L1089] [46:39.80] kind of inspired by by by C. They have
[L1090] [46:42.80] the same operators, the same syntax for
[L1091] [46:45.72] expressions.
[L1092] [46:47.36] The Boolean
[L1093] [46:48.88] operators for instance that is not
[L1094] [46:51.20] standard mathematics. Almost all
[L1095] [46:53.72] languages chose the same operator A to Z
[L1096] [46:57.92] they are written in C.
[L1097] [47:00.68] And so a lot of language copied C and
[L1098] [47:03.24] then zero index it became very popular.
[L1099] [47:07.32] And what is funny
[L1100] [47:09.48] is that in C there is no indexing. In C
[L1101] [47:13.08] indexing is just an illusion
[L1102] [47:15.96] because what you have is pointer
[L1103] [47:17.72] arithmetic.
[L1104] [47:20.80] And C when you write A index it by I
[L1105] [47:23.68] actually what you are saying get the
[L1106] [47:25.84] contents of A plus Y.
[L1107] [47:29.72] And so because in C you don't have
[L1108] [47:32.80] indexing, you have
[L1109] [47:34.84] this
[L1110] [47:36.44] displacements or deltas I don't know how
[L1111] [47:38.96] offsets.
[L1112] [47:40.24] Then it must have index it by zero
[L1113] [47:42.68] because of that because then the first
[L1114] [47:45.00] element is the element that is at the
[L1115] [47:46.92] the original address. So
[L1116] [47:50.16] C doesn't have index indexing. So when
[L1117] [47:53.40] you say A is index by zero, it doesn't
[L1118] [47:56.24] index by zero because it doesn't index
[L1119] [47:58.44] by anything. But it it have this
[L1120] [48:01.00] illusion of indexing and then it's easy
[L1121] [48:03.96] to think that it
[L1122] [48:05.36] And then a lot of language that do not
[L1123] [48:07.52] use pointer arithmetic do not have this
[L1124] [48:10.28] restriction, do not have this semantics,
[L1125] [48:13.16] copy it C and kept the the zero indexing
[L1126] [48:17.92] as the thing. If you got a 12-year-old
[L1127] [48:21.16] and try to explain to them
[L1128] [48:24.12] the zero indexing,
[L1129] [48:26.12] I I assure it's much much easier for
[L1130] [48:29.04] them
[L1131] [48:30.16] to write, "Oh, I I have a list of the
[L1132] [48:32.88] first element." I always joke that is
[L1133] [48:35.00] the first element is zero. And you write
[L1134] [48:38.80] first you for one, but the first element
[L1135] [48:41.84] one
[L1136] [48:42.92] is not one, is zero.
[L1137] [48:45.84] So,
[L1138] [48:46.80] it has advantages zero for this first
[L1139] [48:49.48] some specific operators mathematically.
[L1140] [48:53.12] For instance, you want to do a circular
[L1141] [48:55.28] buffer, zero is better. There are some
[L1142] [48:58.40] small advantage, but it's much much more
[L1143] [49:01.84] confusing.
[L1144] [49:03.16] And as mIRC has this idea of end user
[L1145] [49:05.88] programming,
[L1146] [49:07.40] we always joke it's much easier to make
[L1147] [49:09.64] life easier for the non-programmers.
[L1148] [49:14.12] And I am sure that programmers can
[L1149] [49:18.44] program whatever index they have to do
[L1150] [49:21.00] because they are supposedly they are
[L1151] [49:23.04] professional. They can learn that all
[L1152] [49:26.12] indexing is from them to put all the end
[L1153] [49:30.00] user the burden and of using something
[L1154] [49:32.84] completely different from them indexing
[L1155] [49:35.20] by zero. What does it mean the element
[L1156] [49:37.48] index zero? They never saw and oh, are
[L1157] [49:40.24] the chapters in the book? Yes, the first
[L1158] [49:42.04] chapter is at zero, the second chapter
[L1159] [49:44.56] is at one. It
[L1160] [49:46.24] No, I'm not joking. When you try to
[L1161] [49:48.04] explain that to non-programmer, even
[L1162] [49:50.28] though
[L1163] [49:51.20] they don't need to be 12
[L1164] [49:53.60] I mean, just get anyone that is not
[L1165] [49:56.48] an internet programmer think, "Oh, I
[L1166] [49:58.24] have the absolute I mean, but they are
[L1167] [50:00.28] grown-up. You are
[L1168] [50:02.28] I mean, okay, you are a Christian. You
[L1169] [50:04.84] are
[L1170] [50:05.96] If zero and sure you can learn through
[L1171] [50:08.24] truth to program if one or minus one or
[L1172] [50:11.72] whatever it is the the base you have to
[L1173] [50:14.48] use them. Sure.
[L1174] [50:16.16] >> But do you think you see a lot of bugs
[L1175] [50:19.04] cuz um
[L1176] [50:20.52] maybe someone thinks it's zero.
[L1177] [50:22.52] >> Unfortunately, I see some bugs.
[L1178] [50:25.96] But as I always say, that's are the kind
[L1179] [50:28.40] of bugs that
[L1180] [50:30.76] just shows that you will be then do
[L1181] [50:34.32] minimum testing.
[L1182] [50:36.60] Because that kind of bug is not a kind
[L1183] [50:39.24] of that kind of bug that always you
[L1184] [50:43.12] try to anything you try to do
[L1185] [50:46.40] in a the way.
[L1186] [50:48.56] If you
[L1187] [50:49.52] start from zero or start from one, you
[L1188] [50:52.36] have a bug.
[L1189] [50:53.64] So, the the most simple test that you
[L1190] [50:56.60] can imagine to test anything related to
[L1191] [51:00.48] an array, to a list, etc. And if you if
[L1192] [51:03.24] you
[L1193] [51:04.12] mistake zero to one, you you detect
[L1194] [51:07.60] that. So, if you
[L1195] [51:09.84] have that kind of bug, it just shows
[L1196] [51:12.20] that you didn't
[L1197] [51:14.76] test that code at all.
[L1198] [51:17.40] >> There was this talk that you gave on the
[L1199] [51:19.28] cost of adding uh
[L1200] [51:21.32] language features to Lua and how there's
[L1201] [51:23.56] a lot of hidden costs. And I think it
[L1202] [51:26.36] today
[L1203] [51:27.72] um implementation cost of software is
[L1204] [51:29.96] going down due to, you know, AI code
[L1205] [51:32.76] generation or LLMs.
[L1206] [51:35.24] And I was wondering if that changes your
[L1207] [51:36.88] thinking on
[L1208] [51:38.52] um I guess the cost of adding features
[L1209] [51:41.04] to a programming language.
[L1210] [51:43.44] >> AI is something that
[L1211] [51:45.92] we don't really know what is going to
[L1212] [51:49.16] happen. If you go to an extreme
[L1213] [51:53.00] it's com- completely feasible
[L1214] [51:56.84] that we
[L1215] [51:58.12] we won't have programming languages. And
[L1216] [52:00.72] I mean
[L1217] [52:01.88] because if you did the AI is writing all
[L1218] [52:05.00] your code and is checking all your code
[L1219] [52:07.20] and doing everything, in a few years
[L1220] [52:09.92] maybe we don't need programming. AI can
[L1221] [52:12.00] write machine code directly, it doesn't
[L1222] [52:14.00] need programming languages. It
[L1223] [52:17.08] It's easier for for them to compile or
[L1224] [52:19.64] even generate the code directly. I mean,
[L1225] [52:22.00] I don't know what is going to happen in
[L1226] [52:23.84] a few years. So,
[L1227] [52:27.12] I
[L1228] [52:28.00] think it's very hard for me to
[L1229] [52:31.60] talk anything about AI because I have
[L1230] [52:35.04] and I think nobody have a clear idea
[L1231] [52:38.24] what I mean, people have a maybe a clear
[L1232] [52:41.28] idea what it happens in 1 year or 2
[L1233] [52:43.96] years, but in 5 years, I I mean, anyone
[L1234] [52:47.60] that says, "Oh, that's going to happen
[L1235] [52:49.48] in 5 years." It's just
[L1236] [52:51.68] I mean,
[L1237] [52:52.80] it's
[L1238] [52:53.56] just guess.
[L1239] [52:54.96] So,
[L1240] [52:56.32] I I think it's hard to to say anything.
[L1241] [52:59.72] This is all because of AI. So,
[L1242] [53:03.60] keeping the meaning thing, I mean, that
[L1243] [53:06.00] is still have the for instance the Oh,
[L1244] [53:07.88] why you still use programming languages?
[L1245] [53:10.44] Because if you want the the user or the
[L1246] [53:13.76] some
[L1247] [53:14.92] human to be able to check the result of
[L1248] [53:18.08] what the AI is doing etc. So, I still
[L1249] [53:21.96] think that most of the things about
[L1250] [53:24.80] programming language still hold. For
[L1251] [53:27.20] instance, the the the cost of complexity
[L1252] [53:29.72] of you understanding I mean, AI create a
[L1253] [53:32.48] code for you and then you really
[L1254] [53:34.64] understanding what that code does. I
[L1255] [53:37.32] mean, it's even worse. I mean, it's much
[L1256] [53:39.60] more important that the language should
[L1257] [53:42.56] be clear and and has a
[L1258] [53:46.20] not no hidden mechanisms because they I
[L1259] [53:50.76] may use a hidden mechanism it doesn't
[L1260] [53:52.88] have the concept oh that will be
[L1261] [53:54.68] difficult for a human to understand that
[L1262] [53:57.68] what is really happening here is is
[L1263] [54:00.52] something it's a something that for
[L1264] [54:02.04] instance oh I can use that but I'm for
[L1265] [54:04.48] sure it's going to put a comment here
[L1266] [54:07.24] because I'm sure that someone that reads
[L1267] [54:09.48] that in 1 month it's not going to
[L1268] [54:12.28] understand.
[L1269] [54:14.12] AI doesn't have that kind of
[L1270] [54:16.60] of
[L1271] [54:17.56] of thinking and so it just use that that
[L1272] [54:20.56] trick or that thing and it's so I think
[L1273] [54:24.12] the AI if you think about this idea of
[L1274] [54:26.64] AI generating code I think it's even
[L1275] [54:28.92] more important for the language to be
[L1276] [54:31.04] simple to be understandable for you to
[L1277] [54:34.36] be able to really understand that the
[L1278] [54:36.56] code that you are seeing does what you
[L1279] [54:39.32] think it should it should do it it
[L1280] [54:41.72] really understand what the code is
[L1281] [54:44.04] doing. So this thing about simplicity I
[L1282] [54:47.36] think it's it's very important. And
[L1283] [54:50.76] I think
[L1284] [54:52.28] the other part from the need maybe I may
[L1285] [54:55.20] facilitate documentation I'm not sure if
[L1286] [54:58.32] I need this thing about conceptual
[L1287] [55:00.80] integrity for instance to keep things oh
[L1288] [55:03.68] that makes sense etc. I really think
[L1289] [55:06.76] that one of the main costs is that it
[L1290] [55:09.40] it's the the the burden you put on the
[L1291] [55:11.68] user to learn
[L1292] [55:14.08] one more thing about it
[L1293] [55:16.20] your language.
[L1294] [55:17.64] So there's the other possibility I have
[L1295] [55:20.24] said that implementation is the that is
[L1296] [55:23.00] the the the part that AI can really
[L1297] [55:25.84] help you.
[L1298] [55:27.76] It's not a really re-
[L1299] [55:31.20] really important cost.
[L1300] [55:32.88] >> If you think about like a spectrum of
[L1301] [55:34.84] simple to complex, what programming
[L1302] [55:37.64] languages are, you know, the most simple
[L1303] [55:40.28] ones that you think of that are easy to
[L1304] [55:42.16] understand, less confusing side effects,
[L1305] [55:45.08] and what programming languages are the
[L1306] [55:47.20] most complex and have the most foot
[L1307] [55:49.40] guns?
[L1308] [55:50.40] >> This this famous quote comes from, I
[L1309] [55:53.36] don't know from whom, that the simplest
[L1310] [55:57.52] possible, but not simpler than that.
[L1311] [56:00.88] Because you see, if you go to the
[L1312] [56:02.40] extreme of simplicity, you could get for
[L1313] [56:05.84] instance lambda calculus or Turing
[L1314] [56:08.00] machines and say, "Oh, that's really
[L1315] [56:10.48] simple." I mean, this is really simple,
[L1316] [56:12.92] but it's completely impossible to to
[L1317] [56:15.56] write any program in that. I mean, if
[L1318] [56:18.08] you have really simple stuff, I think
[L1319] [56:20.64] the extremes would be like that, but you
[L1320] [56:23.08] don't want to be there. But for the
[L1321] [56:25.28] other side,
[L1322] [56:26.60] I think C++ I think is a good example of
[L1323] [56:29.52] a language that I think it's really
[L1324] [56:31.72] really complex.
[L1325] [56:33.44] >> A question that comes up a lot is
[L1326] [56:35.92] given how much AI has been progressing,
[L1327] [56:38.72] you know, would you still recommend
[L1328] [56:40.08] people learn computer science today?
[L1329] [56:43.52] >> If you really think about that, it's
[L1330] [56:45.84] really difficult to recommend people
[L1331] [56:47.68] learning anything
[L1332] [56:49.52] for a profession. I mean, we have no
[L1333] [56:51.92] idea what AI will do in 5 years. If
[L1334] [56:55.20] someone is entering university now, they
[L1335] [56:58.16] are going to graduate in 4 years, 5
[L1336] [57:00.60] years, or
[L1337] [57:02.40] I think maybe three three and a half
[L1338] [57:05.04] years or
[L1339] [57:06.16] then
[L1340] [57:07.32] nobody have
[L1341] [57:08.88] any idea what it's what the world is the
[L1342] [57:13.08] your profession will be like in in 4
[L1343] [57:15.92] years from now. So, it's really hard to
[L1344] [57:18.52] I mean to say, "Oh, yes, you can you
[L1345] [57:20.92] still going to have me." Because now
[L1346] [57:22.48] people say, "Oh, no." The the the
[L1347] [57:26.40] manual tasks, the AI is very good, but
[L1348] [57:29.08] it's you needed the the whole
[L1349] [57:30.76] architecture, you needed the
[L1350] [57:33.12] like a software engineer to do to
[L1351] [57:35.80] see the big picture, etc. That it's now,
[L1352] [57:38.56] but it you have no idea that that will
[L1353] [57:41.20] be true in 4 years and or 5 years. So, I
[L1354] [57:45.60] think I mean I like I enjoy programming.
[L1355] [57:49.24] I I could do I mean some people say,
[L1356] [57:51.28] "Oh, use the AI for that." I mean I
[L1357] [57:52.96] program because I like that. But exactly
[L1358] [57:55.52] but so if choose something that you
[L1359] [57:57.84] like, but really for if you are really
[L1360] [58:00.04] thinking about how am I going to live
[L1361] [58:02.36] with that? I have no idea it's really I
[L1362] [58:05.60] think it's a really
[L1363] [58:08.52] hard time to
[L1364] [58:11.52] to be choosing a profession.
[L1365] [58:13.84] >> Yeah, I mean you've worked on Lua for
[L1366] [58:15.64] such a long time. When you look back on
[L1367] [58:17.96] it, what went well and what didn't go
[L1368] [58:21.24] well?
[L1369] [58:22.32] >> We had this privilege
[L1370] [58:24.56] of
[L1371] [58:25.64] not having to satisfy clients.
[L1372] [58:29.08] So, we are the we don't have as I said
[L1373] [58:31.16] for instance, you can choose to add some
[L1374] [58:33.08] feature to the language because you do
[L1375] [58:34.80] not have a pressure, "Oh, we need that
[L1376] [58:36.84] feature that feature whatever it takes
[L1377] [58:40.24] or etc." So, we have this privilege of,
[L1378] [58:43.44] "Oh, we are not sure whether to put
[L1379] [58:45.48] that, we don't put that, we can wait 1
[L1380] [58:47.56] year or so." I think that it's it's much
[L1381] [58:50.40] easier to do a
[L1382] [58:52.80] a good project, a beautiful project. So,
[L1383] [58:55.92] I'm not I'm not sure this is a
[L1384] [58:57.52] recommendation.
[L1385] [58:59.20] Try to work with
[L1386] [59:01.16] without much pressure.
[L1387] [59:03.16] People usually do not have
[L1388] [59:05.36] this choice.
[L1389] [59:07.24] >> What was your measure of success if
[L1390] [59:09.76] you're working on a programming
[L1391] [59:11.00] language? Like,
[L1392] [59:12.36] you know, how did you know it was good?
[L1393] [59:14.72] >> It's more important to receive sometimes
[L1394] [59:17.44] that good people that I recognize that
[L1395] [59:21.24] as we like the the result than a lot of
[L1396] [59:25.20] people that I have no idea what they who
[L1397] [59:28.92] they are etc. Like so I I
[L1398] [59:31.60] I think this metric of quantity that is
[L1399] [59:34.24] the standard metric nowadays in
[L1400] [59:37.44] in the web it's got much worse that
[L1401] [59:39.84] everything is just in the number of
[L1402] [59:41.52] followers that me doesn't care who is
[L1403] [59:44.36] following you just as as many people as
[L1404] [59:47.16] possible. So sometimes for me it's much
[L1405] [59:49.52] more important if someone that I really
[L1406] [59:51.96] admire of thing all this that say
[L1407] [59:55.04] something good about Lua than oh we have
[L1408] [59:57.68] that many
[L1409] [01:00:00.24] But of course it's good also to have
[L1410] [01:00:02.56] some number of users and to be
[L1411] [01:00:04.40] recognized but I think it says a balance
[L1412] [01:00:08.44] between all of this.
[L1413] [01:00:10.28] >> Do you recommend people study other
[L1414] [01:00:11.96] programming languages to get better at
[L1415] [01:00:14.24] programming? And so question is you know
[L1416] [01:00:17.40] what are the top three programming
[L1417] [01:00:19.12] languages that you think every engineer
[L1418] [01:00:21.52] should learn in 2026 to kind of become
[L1419] [01:00:24.92] better at programming?
[L1420] [01:00:26.96] >> Haskell
[L1421] [01:00:28.68] I think it's a
[L1422] [01:00:31.12] it's an incredible language that it has
[L1423] [01:00:33.64] everything you need to
[L1424] [01:00:35.44] really learn about functional
[L1425] [01:00:37.84] programming.
[L1426] [01:00:39.76] I think one of the main benefits is much
[L1427] [01:00:43.52] there is a old joke
[L1428] [01:00:45.80] seen in the Haskell community that
[L1429] [01:00:50.28] if you write a program in in
[L1430] [01:00:53.32] Haskell and in C
[L1431] [01:00:56.12] in C
[L1432] [01:00:57.68] really spend one week
[L1433] [01:00:59.76] to make it efficient
[L1434] [01:01:02.24] and then you spend one year to make it
[L1435] [01:01:04.68] correct.
[L1436] [01:01:07.44] In Haskell you spend one week to make it
[L1437] [01:01:10.20] correct and then you may spend one year
[L1438] [01:01:13.12] to make it efficient.
[L1439] [01:01:15.68] Again it's not my joke but
[L1440] [01:01:18.12] I it has some truth not
[L1441] [01:01:20.84] always true etc. but I think it gives
[L1442] [01:01:23.36] the the idea. I think this is
[L1443] [01:01:26.24] maybe the the the main the most
[L1444] [01:01:28.68] important lesson of Haskell. But,
[L1445] [01:01:31.08] Haskell has many other
[L1446] [01:01:33.64] validity this thing about type
[L1447] [01:01:35.44] inference, for instance, that I mean the
[L1448] [01:01:37.36] entire language is built is
[L1449] [01:01:41.24] types are optional everywhere, and yet
[L1450] [01:01:44.52] it can do type inference for everything.
[L1451] [01:01:47.68] It can infer the types correctly, etc.
[L1452] [01:01:51.52] C or some
[L1453] [01:01:53.56] low language I mean, you can also have a
[L1454] [01:01:57.40] to learn some assembler or I mean to to
[L1455] [01:01:59.96] see you. But, assemblers now are
[L1456] [01:02:02.04] becoming too much complex. It would be
[L1457] [01:02:04.40] to learn like the
[L1458] [01:02:06.28] the 8080 assembler, very old assembler
[L1459] [01:02:09.64] of a very
[L1460] [01:02:10.88] but to have this exactly this idea of
[L1461] [01:02:13.28] what a machine does, how it does stuff
[L1462] [01:02:16.20] it exactly the basic level to have this
[L1463] [01:02:18.80] understanding.
[L1464] [01:02:20.28] Scheme is a language that I I like very
[L1465] [01:02:22.64] much because of this exactly this
[L1466] [01:02:25.32] economy of of ideas, very very few
[L1467] [01:02:29.00] concepts, and it can do some amazing
[L1468] [01:02:32.40] things with the
[L1469] [01:02:34.12] with very few concepts. The one language
[L1470] [01:02:36.96] that this is very very very old, but I
[L1471] [01:02:40.84] still think it is Snowball.
[L1472] [01:02:43.64] What was the first I think it was the
[L1473] [01:02:45.04] first languages to have pattern matching
[L1474] [01:02:47.36] and this idea of doing I mean, it's
[L1475] [01:02:50.32] really strong patterns, etc. And I think
[L1476] [01:02:54.52] it's sometimes it's interesting to see
[L1477] [01:02:57.08] old languages because exactly nowadays a
[L1478] [01:03:00.60] lot of languages tend to like I said,
[L1479] [01:03:02.64] the zero indexing that people
[L1480] [01:03:05.24] they copy a lot of they they tend to be
[L1481] [01:03:08.76] too uniform in some aspects. And so,
[L1482] [01:03:12.24] it's interesting to see some older
[L1483] [01:03:14.28] languages that have some ideas that may
[L1484] [01:03:17.72] maybe not even good ideas, but it's very
[L1485] [01:03:20.16] interesting.
[L1486] [01:03:21.44] >> Last question for you is
[L1487] [01:03:23.88] you know, knowing everything you know
[L1488] [01:03:25.08] now,
[L1489] [01:03:26.20] if you could go back to when you had
[L1490] [01:03:29.28] just started your career and give
[L1491] [01:03:31.76] yourself some advice, what would you
[L1492] [01:03:33.60] say?
[L1493] [01:03:34.76] >> To know a lot of stuff, you really have
[L1494] [01:03:36.72] to study a lot of stuff and it takes
[L1495] [01:03:39.36] time it's the
[L1496] [01:03:40.92] I I also joke about that people say,
[L1497] [01:03:43.40] "Oh, learn Lua in 30 minutes or learn
[L1498] [01:03:46.40] learn Python in 5 minutes or and I
[L1499] [01:03:50.20] always say that I wanted to
[L1500] [01:03:52.20] learn programming in 5 years."
[L1501] [01:03:57.80] That's it.
[L1502] [01:03:59.16] Really learn take our time. You have to
[L1503] [01:04:02.00] learn that and that there is a lot of
[L1504] [01:04:03.80] stuff
[L1505] [01:04:04.80] stuff to learn. There is no magic. There
[L1506] [01:04:06.72] is no
[L1507] [01:04:07.76] You really have to learn I mean a lot of
[L1508] [01:04:10.76] different things.
[L1509] [01:04:12.68] >> Thank you so much for your time
[L1510] [01:04:13.64] Professor. I really appreciate it. It
[L1511] [01:04:15.52] was a lot of fun.
[L1512] [01:04:16.72] >> Thank you.
[L1513] [01:04:17.96] It's all my pleasure.
[L1514] [01:04:19.80] >> Hey, thank you for watching this
[L1515] [01:04:20.80] podcast. If you liked it and you want to
[L1516] [01:04:22.44] see the show grow, please support with a
[L1517] [01:04:24.64] comment or a like.
[L1518] [01:04:26.64] Also, if you have any recommendations
[L1519] [01:04:28.48] for people you want me to bring on,
[L1520] [01:04:30.44] please drop a comment. Guests like
[L1521] [01:04:32.64] Barbara Liskov, Mike Stonebraker, Mark
[L1522] [01:04:35.36] Brooker, these were all people that I
[L1523] [01:04:37.40] brought on because someone left a
[L1524] [01:04:39.24] comment. On another note, aside from the
[L1525] [01:04:41.48] podcast, I'm working on building the
[L1526] [01:04:43.32] ergonomic keyboard that I wish existed.
[L1527] [01:04:45.80] Here's a glance at the prototype. It's a
[L1528] [01:04:47.64] split keyboard, so there's two sides.
[L1529] [01:04:50.64] This is in the case. But yeah, we
[L1530] [01:04:52.12] launched on Kickstarter and we hit our
[L1531] [01:04:53.92] goal within 8 hours of launching. I
[L1532] [01:04:56.04] really appreciate it if you were one of
[L1533] [01:04:57.40] the people who grabbed one of the early
[L1534] [01:04:59.16] units.
[L1535] [01:05:00.28] We're now working on the long journey of
[L1536] [01:05:02.16] building the tooling now. And so if you
[L1537] [01:05:03.92] still want to pick one up, I've left the
[L1538] [01:05:06.12] late pledges open on Kickstarter, so you
[L1539] [01:05:08.60] can grab one there. I'll put a link in
[L1540] [01:05:10.20] the description. Thank you again for
[L1541] [01:05:12.64] watching the podcast, and I'll see you
[L1542] [01:05:14.80] in the next episode.
