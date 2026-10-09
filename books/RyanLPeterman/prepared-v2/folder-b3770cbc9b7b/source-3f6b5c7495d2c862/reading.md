# Co-Creator of Haskell: Useless vs Useful Languages, Rust vs C, Functional Programming | Simon Jones

Source ID: source-3f6b5c7495d2c862
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Co-Creator_of_Haskell_Useless_vs_Useful_Languages,_Rust_vs_C,_Functional_Programming_Simon_Jones_en.txt
Video: https://www.youtube.com/watch?v=xcB_LF3cdqw

[L10] [00:00.00] Why is the internet so insecure?
[L11] [00:02.12] Primarily, because all of our software
[L12] [00:03.88] infrastructure is written in unsafe
[L13] [00:05.04] languages.
[L14] [00:06.08] >> This is Simon Peyton Jones, co-creator
[L15] [00:08.44] of the functional programming language
[L16] [00:10.08] Haskell, and I asked him all about
[L17] [00:12.28] programming language design.
[L18] [00:14.00] >> If we rewrote all of our software
[L19] [00:15.72] infrastructure in Rust, things would be
[L20] [00:17.40] way, way better.
[L21] [00:19.12] I think that statically typed languages
[L22] [00:21.52] are huge boon for LLMs. I do large-scale
[L23] [00:26.20] systematic refactorings fearlessly
[L24] [00:28.36] because the type system keeps me safe.
[L25] [00:29.80] In fact,
[L26] [00:30.96] >> Would you recommend people learn how to
[L27] [00:33.88] program today?
[L28] [00:35.00] >> I think people have a right to be
[L29] [00:35.88] worried in the sense that I think
[L30] [00:36.88] there's going to be considerable
[L31] [00:38.24] dislocation.
[L32] [00:39.96] >> Here's the full episode.
[L33] [00:45.76] I wanted to start by asking you, what is
[L34] [00:48.84] functional programming in your words,
[L35] [00:50.88] and why does it matter to people who
[L36] [00:53.84] might use the other languages, the
[L37] [00:55.68] imperative languages?
[L38] [00:57.24] >> Functional programming is about
[L39] [00:58.24] programming with values instead of
[L40] [01:00.44] mutation. Um, so, uh, in a conventional
[L41] [01:04.56] imperative programming, computation
[L42] [01:05.92] proceeds by, um, like if I want to add
[L43] [01:07.80] up the numbers between 1 and 100, um, I
[L44] [01:10.16] have a a mutable cell containing a
[L45] [01:12.04] running total, and then, as computation
[L46] [01:14.68] proceeds, I keep adding, you know, I I I
[L47] [01:17.52] I I keep adding to my running total. So,
[L48] [01:19.40] there's a cell that changes its value
[L49] [01:20.92] over time. Computation proceeds step by
[L50] [01:23.32] step. There's a program counter.
[L51] [01:25.12] Now, that's very unlike mathematics. If
[L52] [01:26.64] I say 3 + 4 * 7, you don't think of a
[L53] [01:29.80] mutable cell that changes its value over
[L54] [01:31.52] time. You think, well, 3 + 4 is 7, 7 * 7
[L55] [01:34.72] is 49. That just The answer is 49. So,
[L56] [01:37.68] in a sense, it's more declarative than
[L57] [01:40.72] imperative. Um, another way to think of
[L58] [01:44.00] it is it's more like what a spreadsheet
[L59] [01:45.12] does. In a spreadsheet formula, if you
[L60] [01:46.64] put in a cell, you'd say,
[L61] [01:49.32] in A1, you put the formula equals A2 *
[L62] [01:52.96] A3 + 7,
[L63] [01:55.44] well, then, that's just a formula that
[L64] [01:57.52] is evaluated and you expect to compute
[L65] [01:59.60] the values of A2 and A3 automatically
[L66] [02:01.64] before computing A1. It wouldn't make
[L67] [02:03.72] any sense
[L68] [02:05.00] to compute A1 from the old values of A2
[L69] [02:07.80] and A3, right? So, and there's no notion
[L70] [02:10.40] of a program counter. There's no notion
[L71] [02:11.88] of do this and then do that.
[L72] [02:13.84] It wouldn't be sensible to say equals
[L73] [02:15.92] print X plus three.
[L74] [02:18.72] Because who knows when or even whether
[L75] [02:20.64] that cell will ever that formula will
[L76] [02:22.12] ever be evaluated. And then the surprise
[L77] [02:24.36] is
[L78] [02:25.56] that it is possible to do useful things
[L79] [02:27.72] in such a limited language. When I would
[L80] [02:29.92] learn programming, I learned it by
[L81] [02:32.36] writing machine code in which the
[L82] [02:34.00] fundamental mode of computation is
[L83] [02:36.00] registers and program counters, right?
[L84] [02:38.44] And mutation of registers as you go
[L85] [02:40.12] along and memory. Like computation and
[L86] [02:42.84] mutation seem to be inextricably
[L87] [02:45.48] interwoven, right? That's how
[L88] [02:46.92] computation gets done. Um so, it was a
[L89] [02:49.48] surprise to me when I learned that well,
[L90] [02:51.52] um it is possible to do useful things
[L91] [02:54.56] with functional programs.
[L92] [02:56.76] I still remember that amazing
[L93] [02:58.36] revelation. Now, um
[L94] [03:01.28] uh
[L95] [03:02.24] In fact, one way to look at it is this.
[L96] [03:05.60] Right back in the late 1920s, early
[L97] [03:08.24] 1930s,
[L98] [03:10.12] Alan Turing was doing a PhD in Princeton
[L99] [03:13.52] under the supervision of Alonzo Church.
[L100] [03:16.64] Now, Alan Turing, as we all know,
[L101] [03:17.96] invented the Turing machine, which is
[L102] [03:19.84] fundamentally about mutation.
[L103] [03:22.36] Right? It has a little tape and you you
[L104] [03:24.56] can read things on the tape and then you
[L105] [03:25.96] write back new things onto the tape and
[L106] [03:27.44] it has an immutable program, right?
[L107] [03:30.36] Now, Alonzo Church at the very same time
[L108] [03:32.84] was working on something he called the
[L109] [03:34.12] lambda calculus, in which there's no
[L110] [03:35.92] notion of mutation. This is it the
[L111] [03:37.84] lambda calculus is like the essence of
[L112] [03:39.72] functional programming.
[L113] [03:42.20] Programs execute just by reduction. Um
[L114] [03:45.16] now, so these were two different models
[L115] [03:47.04] of computation. You might ask, what can
[L116] [03:49.36] you compute with the Turing machine and
[L117] [03:51.56] what can can
[L118] [03:52.72] with a lambda term. And the astonishing
[L119] [03:54.88] thing that turned out, which is
[L120] [03:56.00] completely non-obvious,
[L121] [03:58.32] is that anything you compute with a
[L122] [04:00.48] lambda term, you can compute with a
[L123] [04:01.80] Turing machine, and anything you compute
[L124] [04:03.52] with a Turing machine, you can compute
[L125] [04:04.76] with lambda calculus.
[L126] [04:06.24] So, that means that the two are
[L127] [04:07.84] identical from the point of view of
[L128] [04:09.12] their computational power.
[L129] [04:11.60] Big surprise to me.
[L130] [04:13.72] Okay, so they're equally powerful, and
[L131] [04:15.76] then then the question is, um
[L132] [04:17.80] you know, which which which might you
[L133] [04:19.36] want to choose? As I say, I started life
[L134] [04:22.00] from the my baseline of imperative
[L135] [04:23.88] programming, and of course that's the
[L136] [04:25.12] way you write programs, and functional
[L137] [04:26.96] programming is a kind of weird,
[L138] [04:28.68] anomalous, rather nerdy, academic thing.
[L139] [04:32.16] But,
[L140] [04:34.28] I became hooked on the idea that by
[L141] [04:37.64] excluding side effects by default, that
[L142] [04:40.36] is imperative programming has side
[L143] [04:41.80] effects by default, by excluding side
[L144] [04:43.16] effects by default, we could make
[L145] [04:44.56] programs that are easier to write,
[L146] [04:46.08] easier to maintain, easier to reason
[L147] [04:47.80] about.
[L148] [04:48.84] And then the question is, um
[L149] [04:51.20] uh what are the practical obstacles? Is
[L150] [04:53.60] it slower? Is it less convenient? And so
[L151] [04:55.52] forth. So, in effect, I've devoted my
[L152] [04:57.44] research life to exploring that
[L153] [04:59.40] hypothesis. The wonderful thing about
[L154] [05:01.28] being a researcher is you can take
[L155] [05:02.92] something which at the time, this is
[L156] [05:04.68] back in 19
[L157] [05:07.76] 80
[L158] [05:09.28] back in 1980, uh functional programming
[L159] [05:11.40] was very nerdy, geeky, academic, um but
[L160] [05:14.08] I was allowed to
[L161] [05:16.08] spend my professional life just saying,
[L162] [05:18.20] "What would happen if you took that one
[L163] [05:19.76] idea, programming with values,
[L164] [05:22.40] and just ran with it? Where would you
[L165] [05:23.88] get?"
[L166] [05:24.76] Um and I think we've got somebody
[L167] [05:26.40] somewhere pretty interesting. I don't
[L168] [05:28.00] want to say that it's better
[L169] [05:30.24] fundamentally, because after all, uh
[L170] [05:32.32] Haskell on that journey started with
[L171] [05:34.20] functional programming, then we learned
[L172] [05:35.60] how to mix functional imperative
[L173] [05:37.04] programming together in a way that we
[L174] [05:38.36] might talk about later, right? So, it's
[L175] [05:40.32] not really an either or, it's more of a
[L176] [05:42.48] both and in the end.
[L177] [05:44.56] But, my uh position now is, as often
[L178] [05:48.64] say, when the limestone of imperative
[L179] [05:52.40] programming is worn away, the granite of
[L180] [05:55.16] functional programming will be revealed
[L181] [05:56.72] underneath.
[L182] [05:57.80] >> And why do you say that?
[L183] [05:59.40] >> Well, functional programming is the
[L184] [06:00.36] language of mathematics.
[L185] [06:01.96] Right, that's that's how we
[L186] [06:04.32] we fundamentally think about things when
[L187] [06:06.00] we want to be formal. Indeed, if we want
[L188] [06:08.04] to reason about and say what does this
[L189] [06:09.68] imperative program do, we have to wheel
[L190] [06:11.32] out a lot of mathematics and you know,
[L191] [06:13.40] whole triples and so forth. But that's
[L192] [06:14.96] all in the world of math, which is
[L193] [06:16.44] functional programming.
[L194] [06:17.72] Functional programming is just
[L195] [06:18.56] mathematics brought to life and made
[L196] [06:20.04] executable.
[L197] [06:22.76] So,
[L198] [06:23.96] you might wonder
[L199] [06:25.36] I suppose um
[L200] [06:27.60] you maybe saying, well, isn't imperative
[L201] [06:30.76] programming just enough?
[L202] [06:32.88] And I think that
[L203] [06:34.96] there you have to have to um
[L204] [06:37.36] uh just look at the broad sweep of
[L205] [06:39.92] things. I think what's happened is that
[L206] [06:41.72] from the world of functional
[L207] [06:42.68] programming, lots of ideas have got
[L208] [06:44.44] adopted into the imperative arena. Like
[L209] [06:46.76] so they grew up over here in functional
[L210] [06:48.52] programming
[L211] [06:49.88] and then they have been adopted by the
[L212] [06:52.64] imperative programming
[L213] [06:54.20] things. So, you I think garbage
[L214] [06:55.60] collection, you might think lambdas, you
[L215] [06:57.16] might think language integrated query,
[L216] [06:59.60] you might think about lots about type
[L217] [07:01.04] systems,
[L218] [07:02.64] polymorphism and static typing, tons of
[L219] [07:05.20] that. So, at least it has been an
[L220] [07:07.64] intellectually interesting experiment
[L221] [07:09.04] that has been a very fertile laboratory
[L222] [07:11.32] which to grow up ideas that can infect
[L223] [07:13.28] the mainstream. Now,
[L224] [07:14.84] um
[L225] [07:15.60] my
[L226] [07:17.28] instincts now is that we should start
[L227] [07:20.04] from functional programming and do
[L228] [07:22.04] imperative programming where necessary.
[L229] [07:24.24] I think probably the mainstream is we
[L230] [07:26.24] should start with imperative programming
[L231] [07:28.12] and sort of add bits of functional
[L232] [07:29.64] programming where possible.
[L233] [07:31.64] But and I'm not going to say that
[L234] [07:33.48] they're wrong to do that, just to say
[L235] [07:35.28] that I think there's a pretty
[L236] [07:36.20] interesting dialogue.
[L237] [07:38.20] Um now,
[L238] [07:39.80] you You to do have to think very
[L239] [07:41.52] differently about the act of
[L240] [07:42.68] programming, right? You do have to
[L241] [07:43.76] rewire your brain quite a bit. Um but
[L242] [07:45.88] just let me this is something we might
[L243] [07:47.00] want to come back to. I said easier to
[L244] [07:48.60] maintain.
[L245] [07:50.40] As programs get old, well just think of
[L246] [07:52.00] a 10-year-old program.
[L247] [07:54.28] Right? If you have um a piece of
[L248] [07:56.48] 10-year-old code written by somebody
[L249] [07:57.76] who's long since left your company that
[L250] [08:00.28] mutates some more or less global
[L251] [08:02.08] variables,
[L252] [08:03.60] then you might be a little bit a bit a
[L253] [08:04.60] little bit afraid about Oh, and there's
[L254] [08:06.40] other bits of code scattered about that
[L255] [08:08.56] also read or write those mutual those um
[L256] [08:11.52] global variables, then you might be a
[L257] [08:13.56] little cautious about making
[L258] [08:14.92] modifications, right? Lest Oh, if I put
[L259] [08:18.32] these two things if I do B and then A
[L260] [08:19.96] instead of A and then B,
[L261] [08:21.64] maybe,
[L262] [08:22.84] you know, the global variable that I
[L263] [08:24.20] read in read somewhere deep inside the
[L264] [08:26.52] code is now not have the value that it
[L265] [08:29.20] was expected to. So,
[L266] [08:31.20] reading and writing um shared variables
[L267] [08:34.36] that are visible, you know, outside the
[L268] [08:35.96] scope sort of somewhat global variables
[L269] [08:38.40] is a form of coupling between bits of
[L270] [08:40.76] code that is very invisible.
[L271] [08:42.92] Right? Very invisible. So, functional
[L272] [08:44.56] programming forces that to become
[L273] [08:46.08] visible.
[L274] [08:47.40] It forces it into the open. And by the
[L275] [08:49.68] act of forcing it into the open, that
[L276] [08:51.40] strongly encourages a style of
[L277] [08:53.12] programming which you would don't have
[L278] [08:54.36] such interactions because they are
[L279] [08:56.20] painful to manage.
[L280] [08:57.72] Um so,
[L281] [08:59.32] um it encourages a uh
[L282] [09:03.44] uh a style in which programs execute in
[L283] [09:05.48] modular box without interacting. Now,
[L284] [09:07.12] every imperative programmer would want
[L285] [09:08.80] to do that. But I want them to do that
[L286] [09:11.60] in a provably secure way.
[L287] [09:13.84] So, you can know that these programs
[L288] [09:15.64] don't interact rather than just say,
[L289] [09:17.44] "I've done my best."
[L290] [09:18.96] >> Then I guess on the on the flip side
[L291] [09:20.68] then, what are the downsides of
[L292] [09:23.00] functional programming language?
[L293] [09:25.40] >> Oh, well, it can be very tiresome and
[L294] [09:28.20] inconvenient, right? So, you're
[L295] [09:29.68] somewhere deep in the ball you know, a a
[L296] [09:32.00] a subroutine of a subroutine of a
[L297] [09:33.28] subroutine of a some soft software
[L298] [09:34.88] stack, and you want to reach out and I
[L299] [09:36.88] don't know, grab the time of day.
[L300] [09:40.16] Oh dear.
[L301] [09:41.56] That's a side effect.
[L302] [09:43.16] But when in a pure functional language,
[L303] [09:44.48] the time of and it did there's a good
[L304] [09:46.32] reason because everybody else higher in
[L305] [09:48.56] the stack is assuming that if I call
[L306] [09:50.36] this function applied to, you know,
[L307] [09:51.88] seven, it will give me the same answer
[L308] [09:53.80] if I call it call it again applied to
[L309] [09:55.72] seven. But if it can interrogate the
[L310] [09:57.40] time of day, suddenly it might give a
[L311] [09:58.52] different answer.
[L312] [10:00.40] Right? So, this a simple a thing as look
[L313] [10:03.52] as asking for the time of day
[L314] [10:05.40] invalidates all set of assumptions and
[L315] [10:07.24] so is not by default allowed at all. And
[L316] [10:10.16] that can be a convenient because you all
[L317] [10:11.48] you say, "Look guys, all I want to do is
[L318] [10:13.28] get hold of the time of day. Don't give
[L319] [10:14.60] me grief."
[L320] [10:16.40] And so every functional programming
[L321] [10:17.76] language including Haskell um provides
[L322] [10:19.72] you with a little trapdoor.
[L323] [10:21.48] Haskell's is called unsafePerformIO.
[L324] [10:25.64] And it says,
[L325] [10:26.92] "Trust me. I'm going to do something
[L326] [10:28.68] that has side effects, but you can
[L327] [10:30.56] pretend there weren't any."
[L328] [10:33.40] All right. So, and it's called it is
[L329] [10:35.88] literally spelled u n s a f e perform
[L330] [10:38.16] i/o. It's the long name that has unsafe
[L331] [10:40.92] in the title so that you the programmer
[L332] [10:42.56] taking on the obligation to make sure
[L333] [10:44.72] that what you're doing is okay.
[L334] [10:46.92] Whereas in an imperative language,
[L335] [10:48.72] everything you do could be
[L336] [10:50.36] unsafePerformIO-ish.
[L337] [10:53.04] >> [laughter]
[L338] [10:53.32] >> I was watching one of your lectures and
[L339] [10:55.72] you did go over a little bit the history
[L340] [10:58.12] of functional programming languages
[L341] [11:00.92] and you mentioned somewhere that there
[L342] [11:04.16] was this idea of people building
[L343] [11:06.00] hardware for functional programming
[L344] [11:08.20] languages.
[L345] [11:09.72] This just made me curious because I
[L346] [11:11.20] didn't I only know the Von Neumann
[L347] [11:14.44] architecture. Do you have any idea what
[L348] [11:17.00] that might look like and some high-level
[L349] [11:18.96] thoughts?
[L350] [11:20.68] >> Well, I did it. Um and now I think it's
[L351] [11:23.08] probably a bad idea.
[L352] [11:24.96] Um but back in 19 when was Backus's
[L353] [11:28.84] Turing Award lecture? I I it was 1978 or
[L354] [11:31.60] there about.
[L355] [11:32.76] What was it called? Um
[L356] [11:34.24] >> Can programming be liberated from the
[L357] [11:36.68] von Neumann style?
[L358] [11:38.32] >> That's it. Now, he was saying two
[L359] [11:39.88] things. Firstly,
[L360] [11:41.56] he, the designer of Fortran, a
[L361] [11:44.00] quintessentially imperative language,
[L362] [11:46.28] the designer of Fortran was saying,
[L363] [11:48.40] "Guys, we should do functional
[L364] [11:49.76] programming."
[L365] [11:51.68] That was the That was what the talk was
[L366] [11:53.12] about. Um and um
[L367] [11:56.24] uh
[L368] [11:57.40] he introduced a language called FP
[L369] [12:00.20] for functional programming. It was a
[L370] [12:01.16] very particular, somewhat idiosyncratic
[L371] [12:03.08] functional programming language, but
[L372] [12:04.12] there was. So, that was rather amazing,
[L373] [12:06.04] right? This was 1977.
[L374] [12:09.12] Um
[L375] [12:10.44] he was saying, "Guys, give up on
[L376] [12:12.00] imperative programming. Just do
[L377] [12:13.60] functional programming. Here's how you
[L378] [12:14.56] do it."
[L379] [12:15.60] But, he also said in the same lecture,
[L380] [12:18.32] um
[L381] [12:19.44] "We might imagine designing new hardware
[L382] [12:21.64] to execute this new kind of language."
[L383] [12:23.36] So, if you like, we've got Turing
[L384] [12:24.76] machines, they let give rise to register
[L385] [12:26.72] machines and microprocessors and so
[L386] [12:28.24] forth. Maybe lambda calculus, perhaps if
[L387] [12:30.68] we designed a machine from the ground up
[L388] [12:32.88] to do lambda calculus,
[L389] [12:35.52] it would look different.
[L390] [12:37.56] So, that was of course very exciting.
[L391] [12:40.64] And
[L392] [12:41.68] um
[L393] [12:42.80] uh similar kind of thinking led to an
[L394] [12:44.92] actual commercial machine called the
[L395] [12:46.28] Lisp machine. That was a piece of
[L396] [12:48.24] hardware that was designed by Symbolics
[L397] [12:50.52] to execute Lisp programs. Lisp is a
[L398] [12:53.12] mostly functional programming language.
[L399] [12:55.28] Um
[L400] [12:56.36] And so, at the time I was, you know, in
[L401] [12:58.92] my early 20s, we were thinking, "Oh,
[L402] [13:01.40] crumbs, what would a piece of hardware
[L403] [13:03.36] look like that could was primarily
[L404] [13:05.08] designed to execute functional programs?
[L405] [13:06.68] Would it have a different kind of
[L406] [13:07.44] instruction set and architecture?" So,
[L407] [13:09.96] um
[L408] [13:11.08] the nearest we got to it actually was
[L409] [13:12.64] although it was a big strand of work
[L410] [13:14.28] then that was the um called the MIT data
[L411] [13:17.36] flow project. So, data flow languages,
[L412] [13:19.76] functional languages, they're definitely
[L413] [13:21.00] the same kind of category, right? And
[L414] [13:23.84] so, um
[L415] [13:25.56] the MIT had this great group led by
[L416] [13:28.76] Arvind called the MIT data flow group
[L417] [13:30.68] and they designed in the end a machine
[L418] [13:33.04] called monsoon.
[L419] [13:35.00] It was specifically designed to execute
[L420] [13:37.12] data flow programs, that is functional
[L421] [13:38.52] programs.
[L422] [13:39.60] It was based on uh you know a token
[L423] [13:41.48] store and matching and tokens flowing
[L424] [13:43.44] around and getting matched up and
[L425] [13:44.92] executing. You can imagine data flowing
[L426] [13:47.60] through a graph. When three arrives at a
[L427] [13:49.80] plus node and four arrives at the other
[L428] [13:51.56] input of the plus node, bam you can fire
[L429] [13:53.36] that plus node, right? And that hardware
[L430] [13:55.40] did all of that.
[L431] [13:58.32] At a similar kind of time in England my
[L432] [14:00.72] um
[L433] [14:01.64] colleagues uh Thomas Clark, Joe Stoy and
[L434] [14:03.80] others um built something called the SKI
[L435] [14:05.88] machine, SKIM.
[L436] [14:07.36] There's a paper about this in the
[L437] [14:09.20] um uh FDC conference. And SKIM was
[L438] [14:12.48] designed to execute SK combinators. So
[L439] [14:15.28] at the time
[L440] [14:17.16] David Turner has written a lovely paper
[L441] [14:19.04] in which he described how to take lambda
[L442] [14:21.24] calculus programs and translate them
[L443] [14:23.32] into SK combinators. So you can read
[L444] [14:25.80] about that in my book. It's a very
[L445] [14:28.00] simple translation that you can give the
[L446] [14:29.44] whole translation in half a dozen lines.
[L447] [14:31.80] But um then you have this message of
[L448] [14:34.36] this message of S's and K's. And S and K
[L449] [14:37.16] reduction is very very easy.
[L450] [14:40.00] Um so it's like the machine code of
[L451] [14:42.64] functional program. That's one way to
[L452] [14:44.16] think of it.
[L453] [14:45.20] >> What is a SK combinator just for
[L454] [14:48.56] context?
[L455] [14:49.68] >> There are three combinators, SK and I.
[L456] [14:51.84] So and they have simple reduction rules.
[L457] [14:53.64] Here they are.
[L458] [14:54.88] IX = X. KXY = X. SXYZ is X of Z applied
[L459] [15:00.32] to Y of Z. End of story. That's all.
[L460] [15:03.12] So it's very simple, right? So now all I
[L461] [15:05.08] got to do is take to take my lambda
[L462] [15:06.72] translate it into a giant tree of SK
[L463] [15:09.68] combinators, right? S applied to K
[L464] [15:11.92] applied to I of um
[L465] [15:14.28] three and um S of Z of just a huge tree
[L466] [15:18.12] of S's and K's.
[L467] [15:19.72] Right? Now simply apply the rewrite
[L468] [15:21.44] rules I gave you.
[L469] [15:22.72] And you have That's That is program
[L470] [15:24.08] execution.
[L471] [15:25.24] It's rather astonishing that that can
[L472] [15:26.44] execute arbitrarily complicated
[L473] [15:28.44] programs, but it can.
[L474] [15:30.76] Do you think that's rather amazing?
[L475] [15:33.20] Now, then I can take an arbitrary
[L476] [15:34.88] Haskell program, I can translate it into
[L477] [15:37.76] lambda terms, and I can translate those
[L478] [15:39.88] lambda terms into S and K, very simple
[L479] [15:41.92] transformation, and I can just write
[L480] [15:43.80] those Run those three rules, and it'll
[L481] [15:45.68] produce the output of the Haskell
[L482] [15:46.80] program. That's pretty amazing. And
[L483] [15:48.68] indeed, there is an implementation of
[L484] [15:50.08] Haskell that uses exactly this. It's
[L485] [15:51.68] called microHS, and my colleague Lennart
[L486] [15:53.76] Augustsson um has built it, and its
[L487] [15:56.40] execution mechanism is SK combinator
[L488] [15:58.84] reduction. And if you sit in microHS,
[L489] [16:01.16] you can ask it to show you the S's and
[L490] [16:02.88] K's that it produces. If we had a, you
[L491] [16:05.04] know, shared screen, I could probably
[L492] [16:06.32] show you. Um
[L493] [16:08.80] Uh So, long story short then, um
[L494] [16:12.16] uh
[L495] [16:13.28] the SKI machine was designed to take SK
[L496] [16:16.84] trees, big trees of S's and K
[L497] [16:18.84] combinators, and just execute them
[L498] [16:20.44] directly. So, it was built
[L499] [16:22.96] in hardware, and it ran perfectly well,
[L500] [16:26.12] um reasonably fast.
[L501] [16:27.84] Now, why didn't this catch on? Why don't
[L502] [16:29.92] we have
[L503] [16:31.28] um functional programming machines? I
[L504] [16:32.64] mean, at the time, it was a big idea. We
[L505] [16:34.28] even had a conference called
[L506] [16:36.48] Functional Programming Computer
[L507] [16:37.80] Architecture, FPCA. It was right there
[L508] [16:40.92] in the title of the conference.
[L509] [16:43.96] But slowly, we became aware that
[L510] [16:47.28] what was really happening is we were
[L511] [16:49.28] doing at run time what we could do
[L512] [16:51.24] instead at compile time.
[L513] [16:53.72] And that is always a bad idea.
[L514] [16:56.28] Imagine an interpreter for, I don't
[L515] [16:58.04] know, um Pascal or something.
[L516] [17:01.44] It'd be Or uh for Java. Like, we can
[L517] [17:03.80] compile Java to bytecode, and we could
[L518] [17:05.76] interpret the bytecode.
[L519] [17:08.80] Right? So, then we are We're doing
[L520] [17:10.88] something at run time. At run time, the
[L521] [17:12.76] interpreter is looking at the bytecode
[L522] [17:14.32] saying, dispatching to say which
[L523] [17:15.80] instruction, blah blah blah. right?
[L524] [17:18.32] Now, what does a JIT do? It takes a
[L525] [17:20.08] sequence of bytecode and says, "Oh, no,
[L526] [17:21.48] no.
[L527] [17:22.64] I'm going to take that sequence of
[L528] [17:24.08] bytecode and compile it to a sequence of
[L529] [17:25.60] machine instructions that, when
[L530] [17:27.40] executed, will do the same thing,
[L531] [17:28.96] right?"
[L532] [17:30.80] Much faster.
[L533] [17:34.00] Because it can take advantage of common
[L534] [17:35.48] of bytecode sequences, for example, to
[L535] [17:37.36] say, you know, if you swap and then
[L536] [17:39.20] swap, it's a no-op or something like
[L537] [17:40.52] that, right?
[L538] [17:43.96] So, what In fact, it turned out is this
[L539] [17:46.64] whole SKI business, and any other And
[L540] [17:49.32] indeed dataflow machines also, was
[L541] [17:51.40] simply doing at runtime what you could
[L542] [17:53.36] do better at compile time. We were
[L543] [17:55.24] building an interpreter in hardware.
[L544] [17:58.92] So, don't build the interpreter in
[L545] [18:00.20] hardware. Instead, build a compiler
[L546] [18:02.56] that translates
[L547] [18:04.44] your lambda term into a sequence of
[L548] [18:06.52] machine instructions that, when
[L549] [18:08.32] executed,
[L550] [18:09.96] will behave as if you had
[L551] [18:12.36] done this uh reduction business.
[L552] [18:14.96] And then you might think, well, machine
[L553] [18:17.00] instructions for what machine?
[L554] [18:19.56] Well,
[L555] [18:20.56] from a practical point of view, it was
[L556] [18:22.76] very hard to compete with Intel.
[L557] [18:25.76] Right? They were just spending
[L558] [18:27.24] Brazilians of man-years on making x86s
[L559] [18:29.80] go faster.
[L560] [18:31.24] And ARM likewise for ARMs. So, um we can
[L561] [18:34.28] leverage all of that work by compiling
[L562] [18:36.00] into their instruction set.
[L563] [18:38.48] But even if you say you are God, you are
[L564] [18:41.32] the chief executive in Intel, and can
[L565] [18:43.44] tell them to add new instructions or
[L566] [18:46.24] mechanisms to support functional
[L567] [18:47.84] programming, what would you add?
[L568] [18:50.12] Not very much.
[L569] [18:53.48] Little bits to do with um
[L570] [18:55.60] uh garbage collection barriers, I think.
[L571] [18:58.40] And and such like, but nothing major.
[L572] [19:03.72] So, in other words, I think the whole
[L573] [19:07.00] build hardware to execute functional
[L574] [19:08.68] programming directly turned out to be a
[L575] [19:10.52] mistake. Inspiring mistake, fun mistake,
[L576] [19:13.36] I had a great time, but a mistake.
[L577] [19:15.60] It's better to build a compiler.
[L578] [19:17.84] >> I would have thought there might be some
[L579] [19:19.72] unique opportunities for parallelism
[L580] [19:23.12] given the immutability in these
[L581] [19:25.20] functional programming languages. So,
[L582] [19:27.84] I Yeah, you described that that graph or
[L583] [19:30.08] that SK combinator graph. I imagine you
[L584] [19:33.72] could,
[L585] [19:34.72] you know,
[L586] [19:35.68] execute that all in parallel assuming
[L587] [19:37.68] there's no connections across
[L588] [19:39.84] the graph.
[L589] [19:40.52] >> And indeed, that was the data flow
[L590] [19:41.96] machine. The MIT data flow machine was
[L591] [19:43.56] all based on that idea. It's saying just
[L592] [19:45.28] throw the whole graph into the token
[L593] [19:46.88] store and just run all the nodes that
[L594] [19:48.96] are runnable.
[L595] [19:50.48] Right?
[L596] [19:51.36] But that's incredibly fine grained.
[L597] [19:53.12] You've got to imagine this big tree of a
[L598] [19:55.64] million nodes and your processor is sort
[L599] [19:58.00] of wandering around over it doing little
[L600] [19:59.72] things in parallel. There's a lot of
[L601] [20:01.64] memory traffic going on there. And if
[L602] [20:03.16] this these these little, you know,
[L603] [20:04.40] threads have to, you know, are operating
[L604] [20:06.04] on the same bit of tree, then the
[L605] [20:07.16] synchronization costs,
[L606] [20:08.88] um so, very, very fine grained computer
[L607] [20:12.68] parallel computation like this turns out
[L608] [20:14.48] to be impractical.
[L609] [20:17.00] Like or not impractical. You could do
[L610] [20:18.64] it, but it's very slow.
[L611] [20:20.88] Right? So, the data flow people, their
[L612] [20:23.32] history, if you look at the history of
[L613] [20:24.72] the MIT data flow project, they started
[L614] [20:26.80] with micro parallelism. Every individual
[L615] [20:30.48] instruction was a separate parallel
[L616] [20:32.60] computation that might take place and
[L617] [20:34.80] the token store would match it up.
[L618] [20:36.40] Right? And then they built more and more
[L619] [20:38.56] compiler technology that grouped these
[L620] [20:40.28] things together into larger units. So,
[L621] [20:42.68] they expanded from micro threads of
[L622] [20:44.88] single instruction threads into 10
[L623] [20:46.80] instruction threads or 100 instruction
[L624] [20:48.32] threads. Right?
[L625] [20:49.88] But even that never really caught on.
[L626] [20:51.68] So,
[L627] [20:53.12] you're right, though,
[L628] [20:54.44] that if I say in a Haskell program, E1 +
[L629] [20:57.52] E2,
[L630] [20:58.96] then I can do E1 and E2 in parallel. And
[L631] [21:01.92] GHC does support you in doing that, but
[L632] [21:04.08] you nowadays, rather than expecting the
[L633] [21:06.24] compiler to do that automatically for
[L634] [21:08.56] every sub-expression,
[L635] [21:10.28] you can spark a computation. You say E1
[L636] [21:13.32] par E2, and that says do E1 and E2 in
[L637] [21:16.80] parallel. There's a project at Carnegie
[L638] [21:19.32] Mellon
[L639] [21:20.56] for a strict parallel strict language
[L640] [21:22.32] called ML
[L641] [21:24.08] that has a very good variant of parallel
[L642] [21:26.16] ML going in a similar way. So,
[L643] [21:28.24] essentially we've moved away from the
[L644] [21:30.24] the dream of
[L645] [21:31.80] automatically getting parallel at very,
[L646] [21:34.52] very fine grain
[L647] [21:36.44] to programmer
[L648] [21:37.72] we give programmer clues about where
[L649] [21:39.24] it's a good idea to do parallelism, but
[L650] [21:41.64] um
[L651] [21:42.20] uh and still the compiler will try not
[L652] [21:44.40] to fork to too tiny grains.
[L653] [21:47.16] >> I was searching on YouTube and I've
[L654] [21:49.32] searched your name and this video came
[L655] [21:51.16] up and it said "Haskell is useless,
[L656] [21:54.96] Simon Peyton Jones."
[L657] [21:56.57] >> [laughter]
[L658] [21:56.72] >> And it's it's a video from a long time
[L659] [21:58.84] ago. It's someone's got a low-quality
[L660] [22:01.52] and a handheld camera. There's group of
[L661] [22:04.40] researchers that are all talking. Butler
[L662] [22:06.68] Lampson is across the table and it's
[L663] [22:08.44] it's a fun little video. And in the
[L664] [22:10.40] video, you lay out this two-dimensional
[L665] [22:14.36] graph where on on one dimension
[L666] [22:17.04] there is the useful versus useless axis
[L667] [22:22.44] and then on the other dimension there is
[L668] [22:24.28] the safe versus dangerous. And then
[L669] [22:27.00] you're placing programming languages on
[L670] [22:29.36] this two-dimensional graph and I think
[L671] [22:32.12] you started by putting C as it's very
[L672] [22:36.08] useful, but it's incredibly dangerous.
[L673] [22:39.52] And then you put Haskell on the the
[L674] [22:41.84] polar opposite side. It's You said it's
[L675] [22:44.08] useless,
[L676] [22:45.40] but it's very safe. What are the least
[L677] [22:48.04] safe and most useful languages and why
[L678] [22:50.48] do you place them there like C for
[L679] [22:52.28] instance?
[L680] [22:52.64] >> Well, yeah. So, um
[L681] [22:54.56] let's see. In C, you program by
[L682] [22:56.60] mutation. So,
[L683] [22:58.40] it's unsafe in the sense that any
[L684] [22:59.56] function can mutate any variable at any
[L685] [23:01.24] time. It has a lot, you you pass
[L686] [23:02.68] pointers around a lot and functions
[L687] [23:04.68] mutate the memory pointed to by those
[L688] [23:06.80] pointers. And moreover,
[L689] [23:08.28] typically they can mutate it anywhere.
[L690] [23:09.76] There's no array bounds checks or
[L691] [23:11.36] anything. So, it's kind of like super
[L692] [23:13.36] unsafe in the fact that this is
[L693] [23:14.40] demonstrated by the fact Can you imagine
[L694] [23:16.64] that that like all of these exploits
[L695] [23:18.32] that we get every day, right? Um
[L696] [23:21.28] that uh you know, MSRC is discovering in
[L697] [23:23.44] huge numbers, but but we've had you
[L698] [23:25.00] know,
[L699] [23:25.84] why is the internet so insecure?
[L700] [23:28.32] Primarily because all of our software
[L701] [23:30.04] infrastructure is written in unsafe
[L702] [23:31.24] languages. If we I mean
[L703] [23:34.08] if we'd written all of our
[L704] [23:35.88] you know, internet software and
[L705] [23:37.60] operating systems in Haskell or maybe in
[L706] [23:39.92] OCaml or ML,
[L707] [23:41.92] 99% of all these exploits would be
[L708] [23:44.20] removed by construction.
[L709] [23:47.64] Like it's like we've built a boat out of
[L710] [23:52.28] paper clips and we're surprised that
[L711] [23:53.96] it's leaky.
[L712] [23:55.16] I mean, you shouldn't build boats out of
[L713] [23:56.56] paper clips, right? Because they have
[L714] [23:58.12] holes in them. You should build it out
[L715] [23:59.96] of a secure substance, right? But then
[L716] [24:02.12] it's too late. So, we spend incredible
[L717] [24:05.04] amounts of human ingenuity and effort
[L718] [24:06.92] patching the holes in our boat built of
[L719] [24:09.20] paper clips. It's tragic. It's tragic
[L720] [24:12.96] how much effort and ingenuity and money
[L721] [24:16.00] has been lost and waste of resources
[L722] [24:18.36] just because we wrote our um you know,
[L723] [24:21.84] computational infrastructure for the
[L724] [24:23.24] world in an insecure language. That's
[L725] [24:25.76] what I mean by unsafe.
[L726] [24:27.56] >> I mean, are there not vulnerabilities?
[L727] [24:29.16] Like if I wrote something in Haskell, I
[L728] [24:31.40] mean,
[L729] [24:32.36] there's got to be some new type of
[L730] [24:34.32] >> there are vulnerabilities. I just said
[L731] [24:35.44] 99%. I didn't say 100.
[L732] [24:37.60] If I write a Haskell program that says,
[L733] [24:40.56] "Receive message. If the message says,
[L734] [24:43.20] 'Tell me everything,' then spit out my
[L735] [24:46.96] entire database in reply."
[L736] [24:49.28] No language can stop you doing that,
[L737] [24:51.08] right?
[L738] [24:52.20] But, if you look at the program and it
[L739] [24:53.84] doesn't have any such things,
[L740] [24:55.64] right?
[L741] [24:56.69] >> [laughter]
[L742] [24:58.48] >> So, I mean
[L743] [24:59.80] So, you know, nothing can prevent you
[L744] [25:01.40] against high-level attacks to insecure
[L745] [25:03.12] programs. Or, I mean, another example
[L746] [25:04.84] might be deadlock, right? Two services,
[L747] [25:07.76] no matter how securely written, if A
[L748] [25:10.24] waits for B and B waits for A, deadlock.
[L749] [25:12.76] Sorry.
[L750] [25:15.48] No and no language is going to stop you
[L751] [25:17.68] doing that.
[L752] [25:18.88] Um you might hope for some high-level
[L753] [25:20.68] verification tools.
[L754] [25:22.48] But it's like
[L755] [25:25.16] Surely, if you're trying to do something
[L756] [25:27.32] hard, like prove that that doesn't
[L757] [25:29.16] happen, you want to have a foundation
[L758] [25:31.08] that is, you know, in which you've got
[L759] [25:32.96] some bedrock to stand on. If you're
[L760] [25:34.80] standing on sand and trying to prove
[L761] [25:36.84] some advanced property, it's very, very
[L762] [25:38.88] difficult. But, good point. I'm not
[L763] [25:41.12] talking about 100% security. Absolutely
[L764] [25:43.08] not. But, uh how many how many of how
[L765] [25:45.72] many uh exploits are based on buffer
[L766] [25:47.80] overruns?
[L767] [25:49.36] Or, you know, pointer manipulation
[L768] [25:51.20] that's gone wrong.
[L769] [25:52.44] If you couldn't have a buffer overrun,
[L770] [25:53.92] you couldn't do pointer manipulations
[L771] [25:55.28] gone wrong. Those Those exploits just
[L772] [25:57.08] wouldn't exist.
[L773] [25:58.80] >> So, I mean, C is maybe half a century
[L774] [26:02.08] old now.
[L775] [26:03.44] Um
[L776] [26:04.00] what about more modern versions of those
[L777] [26:07.32] lower-level languages like Rust?
[L778] [26:09.72] >> Much, much better. Much, much, much
[L779] [26:11.64] better, right? If we rewrote all of our
[L780] [26:14.12] software infrastructure in Rust,
[L781] [26:16.40] things would be way, way better.
[L782] [26:18.92] I I'm not actually even sure whether
[L783] [26:20.64] Rust has array bounds checks built in,
[L784] [26:22.80] but suppose it but it must have the
[L785] [26:24.56] ability
[L786] [26:25.00] >> to
[L787] [26:26.44] >> uh
[L788] [26:27.56] promise that you're not uh and actually
[L789] [26:29.04] not bound. I don't quite know quite know
[L790] [26:30.24] how, but if you compile all your code
[L791] [26:31.36] with that switched on,
[L792] [26:32.76] you're a way better situation. Way
[L793] [26:34.88] better.
[L794] [26:37.24] So, yes, this is not just functional
[L795] [26:38.84] programming, but you did ask about why I
[L796] [26:41.00] thought C was an insecure, unsafe
[L797] [26:42.76] language.
[L798] [26:44.11] >> [laughter]
[L799] [26:44.84] >> If we imagine that graph, there's that
[L800] [26:47.08] the upper right quadrant, which is
[L801] [26:49.52] useful and safe. And you know, you
[L802] [26:52.40] described that as Nirvana in the in in
[L803] [26:55.36] the video. And I guess maybe over time,
[L804] [26:58.28] I mean C's you know, somewhat really
[L805] [26:59.84] unsafe, really useful.
[L806] [27:01.36] >> Yes, so C I mean Rust has moved along
[L807] [27:03.72] the axis
[L808] [27:05.00] from
[L809] [27:06.16] useful but very unsafe
[L810] [27:08.60] to stay useful and become safer.
[L811] [27:11.68] Now, Haskell started life as being very
[L812] [27:13.68] safe but useless.
[L813] [27:15.64] So, it's worth just you know, rehearsing
[L814] [27:17.16] that because in the first version of
[L815] [27:18.64] Haskell, there was no IO.
[L816] [27:21.00] The only that a Haskell program was a
[L817] [27:23.24] function of type string to string.
[L818] [27:25.52] It's functional programming after all.
[L819] [27:27.36] It could do no IO. All it could do was
[L820] [27:29.20] take a string and produce a string.
[L821] [27:31.88] So, obviously that's not very useful.
[L822] [27:34.76] It's a little bit more useful. A
[L823] [27:35.92] language that is very very safe
[L824] [27:38.12] and completely useless is no-op
[L825] [27:40.68] that does nothing ever.
[L826] [27:42.36] Very safe
[L827] [27:43.80] but very useless. Haskell was a bit
[L828] [27:45.24] better, right? At least it lets you um
[L829] [27:48.40] apply a function to a string and get
[L830] [27:49.80] back another string.
[L831] [27:52.28] So, of course we then worked on how
[L832] [27:53.92] could we do IO in Haskell in a safe way.
[L833] [27:56.16] That will lead to, you know, monads and
[L834] [27:57.88] stuff. But But so, just as uh uh
[L835] [28:01.04] the you know, we're moving from C
[L836] [28:03.24] horizontally to go safer and safer
[L837] [28:06.24] um but
[L838] [28:07.52] uh but staying useful. So, from Haskell
[L839] [28:10.48] we're moving sort of vertically to get
[L840] [28:12.48] more and more useful without stopping
[L841] [28:14.12] being safe.
[L842] [28:16.08] And Nirvana is when we sort of meet up,
[L843] [28:18.36] right? So, but the point is not to say
[L844] [28:20.48] one is better than the other, but just
[L845] [28:22.00] to say that we both seek things that are
[L846] [28:23.76] useful and safe.
[L847] [28:26.00] >> And when I think of functional languages
[L848] [28:28.68] um in I guess in the mainstream or you
[L849] [28:30.88] know, what people are kind of thinking
[L850] [28:32.12] about, I hear Haskell. I also hear
[L851] [28:34.84] OCaml. Uh how do these two programming
[L852] [28:37.32] languages compare if someone was trying
[L853] [28:38.96] to pick a functional language to work
[L854] [28:40.72] with?
[L855] [28:41.64] >> So, OCaml is um a strict language that
[L856] [28:44.12] is called by value.
[L857] [28:46.00] So, when you say F applied to 3 + 4,
[L858] [28:48.52] it'll add 3 + 4 and then call F
[L859] [28:51.16] to get 7, right? In Haskell, if you say
[L860] [28:52.64] F of 3 + 4, it'll build a little
[L861] [28:54.60] suspension that says, "Well, if you ever
[L862] [28:55.96] need this 3 + 4,
[L863] [28:57.84] you can evaluate it, but maybe you'll
[L864] [28:59.20] never need it." And then it calls F.
[L865] [29:01.28] That's a lazy language. Right? Now, uh
[L866] [29:05.00] so because OCaml is strict, it has a
[L867] [29:08.12] defined order of evaluation.
[L868] [29:11.48] So if you say F of 3 + 4 and a second
[L869] [29:14.52] parameter 8 + 9, it'll evaluate 3 + 4
[L870] [29:17.12] and then 8 + 9 in that order.
[L871] [29:20.04] Right? So it makes sense to say you can
[L872] [29:22.16] say F of print hello, {comma} print
[L873] [29:25.00] goodbye.
[L874] [29:27.60] Right? Because you'll get hello and then
[L875] [29:29.56] goodbye printed.
[L876] [29:31.24] So once you have a defined order of
[L877] [29:32.80] evaluation, then it's pretty easy to
[L878] [29:34.92] incorporate IO.
[L879] [29:37.44] Right? Even though it's {quotes} a
[L880] [29:39.04] functional language,
[L881] [29:41.24] OCaml allows you to do IO without, you
[L882] [29:44.60] know, without saying unsafe before my IO
[L883] [29:46.32] or anything. In fact,
[L884] [29:48.20] it has a defined order of evaluation and
[L885] [29:49.88] it's perfectly kosher to do that.
[L886] [29:52.40] As a sort of unintended consequence of
[L887] [29:55.36] being called by value, it was also by
[L888] [29:57.88] default impure. Now, good Haskell good
[L889] [30:00.12] OCaml programmers won't use many side
[L890] [30:01.80] effects, but
[L891] [30:04.80] OCaml doesn't prevent you.
[L892] [30:07.44] Haskell prevents you. Why does it
[L893] [30:09.24] prevent you? Because if we'd allowed you
[L894] [30:11.80] to say F of print hello, {comma} print
[L895] [30:14.60] goodbye,
[L896] [30:16.68] those would be thunks, right? Not yet
[L897] [30:18.36] evaluated.
[L898] [30:20.56] Right? So if F happened to evaluate its
[L899] [30:22.60] first argument and then its second,
[L900] [30:25.68] we'd print hello and then goodbye. If it
[L901] [30:27.44] evaluated its second and then its first,
[L902] [30:29.00] we'd print goodbye and then hello. If it
[L903] [30:30.24] didn't evaluate either, we wouldn't
[L904] [30:31.32] print either of them.
[L905] [30:32.76] That doesn't sound very good from a uh
[L906] [30:34.52] you know, if you want to control what IO
[L907] [30:35.84] is happening. Right? Laziness forced
[L908] [30:39.08] Haskell to stay pure. Strictness allowed
[L909] [30:42.20] OCaml, which grew out of the ML
[L910] [30:44.20] tradition by the way, ML is another
[L911] [30:46.04] functional language that predated
[L912] [30:47.28] Haskell.
[L913] [30:48.28] It was always strict and it always had
[L914] [30:50.40] IO by default.
[L915] [30:52.48] Um
[L916] [30:53.60] it wasn't a goal, but that's just the
[L917] [30:55.20] way it worked out. At the time, nobody
[L918] [30:57.04] thought about it. It was just obvious.
[L919] [31:00.28] So, that's a big difference between
[L920] [31:01.36] OCaml and Haskell, right? Is that um
[L921] [31:04.68] Now then, since then they've both grown
[L922] [31:06.52] up. Haskell's gained sort of monads and
[L923] [31:09.04] I uh OCaml has gained lots of uh lots of
[L924] [31:11.80] fancy type systems. Some of them uh
[L925] [31:13.96] Haskell and OCaml have learned from each
[L926] [31:15.44] other. Um OCaml has gained an
[L927] [31:17.56] interesting effect system recently and a
[L928] [31:19.36] whole lot of new extensions. It's an
[L929] [31:20.96] absolute hotbed of innovation at the
[L930] [31:23.00] moment OCaml. So, I view OCaml and and
[L931] [31:26.08] Haskell as kind of um siblings.
[L932] [31:28.28] Um brothers and sisters, right? We love
[L933] [31:30.28] each other, we learn from each other, um
[L934] [31:32.44] we compete with each other, all of the
[L935] [31:34.04] things that siblings do.
[L936] [31:35.60] But, they're not the same, right? So,
[L937] [31:37.40] siblings don't say, "I'm I'm just better
[L938] [31:39.60] than you. You shouldn't exist." We say,
[L939] [31:41.68] "Let's Let's enjoy our life together."
[L940] [31:43.28] And that's what it That's the way it is.
[L941] [31:44.92] >> You described the laziness and the
[L942] [31:46.56] strict and as a programmer I my initial
[L943] [31:50.24] thought is I would like to control the
[L944] [31:52.76] order of execution. And when I say
[L945] [31:55.68] print X, I and then print Y, I I want it
[L946] [31:59.32] to happen that order, otherwise it would
[L947] [32:01.04] be a little unintuitive. What is the
[L948] [32:03.52] main benefit of laziness?
[L949] [32:05.80] >> Why is laziness good? Well, um
[L950] [32:08.80] uh John Hughes did did this rather well
[L951] [32:11.16] way ago, 1980 something. He wrote a
[L952] [32:14.08] program called Why Functional
[L953] [32:15.12] Programming Matters.
[L954] [32:16.64] Um
[L955] [32:17.40] and one of its main thesis was that lazy
[L956] [32:19.20] evaluation lets you um
[L957] [32:21.96] uh compose programs in a particularly
[L958] [32:24.44] modular way.
[L959] [32:25.80] So, imagine a program that is I mean,
[L960] [32:27.68] his classic example is a program that
[L961] [32:29.08] plays chess,
[L962] [32:30.52] right? So, one thing you could do is you
[L963] [32:32.60] could imagine building a tree of all
[L964] [32:35.32] possible moves starting from the
[L965] [32:36.92] position we're at.
[L966] [32:38.36] It would be a very, very big tree.
[L967] [32:40.68] You know, OCaml, it would be too big.
[L968] [32:43.12] Because first of all, I compute the
[L969] [32:44.52] tree,
[L970] [32:45.64] and then I'd start deciding what move to
[L971] [32:47.12] do. I couldn't possibly do that. But if
[L972] [32:49.20] the tree of all possible moves, you
[L973] [32:50.64] know, has more nodes in it than the
[L974] [32:51.84] number protons in the universe.
[L975] [32:54.36] So, let's not do that. Now,
[L976] [32:56.76] if instead you could build the tree Oh,
[L977] [32:58.96] having got this tree, supposing you had
[L978] [33:00.76] it, you could then walk over the tree
[L979] [33:02.32] saying, "Ah, let me do some mini-maxing
[L980] [33:04.64] and see Oh, this is looks like a good
[L981] [33:06.48] Let me go this way." I could explore the
[L982] [33:08.20] tree, right? Um
[L983] [33:10.36] Now then, so
[L984] [33:12.52] if you you know, OCaml, then you would
[L985] [33:14.32] have to put the tree generation and the
[L986] [33:16.08] tree exploration in one function.
[L987] [33:19.72] Right? In Haskell, with lazy evaluation,
[L988] [33:22.00] you can generate an infinite tree,
[L989] [33:24.44] and then the explorer that prunes the
[L990] [33:26.68] tree and explores just the bits of it
[L991] [33:28.72] that is necessary is completely
[L992] [33:30.92] modularly separated.
[L993] [33:32.72] Right? I can build a different generator
[L994] [33:34.60] and a different pruner. They're just
[L995] [33:36.36] completely separate programs.
[L996] [33:38.68] So, lazy evaluation is very powerful
[L997] [33:40.80] glue that lets you glue together um
[L998] [33:45.48] uh two programs that you'd like to be
[L999] [33:48.16] distinct. Strict evaluation forces you
[L1000] [33:50.80] to merge them together.
[L1001] [33:53.24] >> Yeah, this reminds me I mean um
[L1002] [33:55.48] so, in Python, for instance, they have
[L1003] [33:57.64] the idea of a generator where
[L1004] [33:59.56] >> Yes.
[L1005] [34:00.00] >> you can lazily retrieve things.
[L1006] [34:01.92] >> Every strict language, every, you know,
[L1007] [34:04.24] serious strict language has lazy
[L1008] [34:06.40] evaluation in it. They're called
[L1009] [34:07.72] iterators or generators.
[L1010] [34:10.16] And so does OCaml.
[L1011] [34:11.72] All right?
[L1012] [34:12.68] But in Haskell, that's the default.
[L1013] [34:15.84] Now, instead in Haskell, so this is a
[L1014] [34:17.40] bit like Again, the two are converging
[L1015] [34:19.20] on the middle, right? Haskell, lazy by
[L1016] [34:21.44] default, but you can make things strict.
[L1017] [34:23.64] You can put in exclamation marks to say,
[L1018] [34:25.48] "Please evaluate this before the call."
[L1019] [34:28.36] All right?
[L1020] [34:29.28] Or the IO monad know how say evaluate,
[L1021] [34:30.84] but that's a a more brutal strict strict
[L1022] [34:32.92] annotation. So, in Haskell you can make
[L1023] [34:34.64] things stricter.
[L1024] [34:36.64] In OCaml you can make things lazier.
[L1025] [34:40.60] All right? So, it really boils down to
[L1026] [34:43.32] is what's the default.
[L1027] [34:45.76] We both want to have a mixture of the
[L1028] [34:47.68] two.
[L1029] [34:49.24] And then it becomes a bit cultural as to
[L1030] [34:50.88] which you prefer. Um
[L1031] [34:52.92] I I don't know. Uh some people sometimes
[L1032] [34:54.92] ask me, they say, "Well, if you were
[L1033] [34:56.76] designing Haskell again, would you make
[L1034] [34:58.28] it strict by default
[L1035] [35:00.56] with really good support for laziness?"
[L1036] [35:02.96] And I often say, "Well, I might."
[L1037] [35:05.52] Uh yeah, that seemed attractive because
[L1038] [35:07.16] frequently I found myself cursing
[L1039] [35:09.20] laziness as an implementer.
[L1040] [35:11.32] But, I strongly suspect that 10 years
[L1041] [35:13.48] after that I'd be thinking,
[L1042] [35:15.16] "Man, if only it was lazy by default."
[L1043] [35:19.68] Oh, when I say strict by default I would
[L1044] [35:21.32] or definitely mean strict but pure.
[L1045] [35:24.68] Like, no side effects.
[L1046] [35:26.72] >> A few times in our conversation you've
[L1047] [35:28.68] mentioned the word monad. And it seems
[L1048] [35:31.60] like it allows us to do the side effects
[L1049] [35:33.84] and
[L1050] [35:34.72] um
[L1051] [35:35.80] what is a monad and yeah, how does it
[L1052] [35:38.52] help us do side effects and preserve
[L1053] [35:40.44] ordering?
[L1054] [35:41.48] >> One
[L1055] [35:42.60] way to think about it that's very um
[L1056] [35:45.52] easy to understand and use is just to
[L1057] [35:47.36] imagine that the do notation is somehow
[L1058] [35:50.00] built into Haskell. So, you can say do
[L1059] [35:52.76] print X semicolon print Y.
[L1060] [35:56.28] And that has type
[L1061] [35:59.08] IO unit.
[L1062] [36:00.56] So,
[L1063] [36:01.48] a value of type IO unit means I do some
[L1064] [36:04.56] do some input output and return a value
[L1065] [36:06.44] of type unit.
[L1066] [36:08.52] An expression of type IO int
[L1067] [36:11.00] is an expression that when you run it
[L1068] [36:13.28] will do some
[L1069] [36:14.56] IO and return an int.
[L1070] [36:17.32] Okay? So, do let's you combine um
[L1071] [36:21.20] IO performing computations together. So,
[L1072] [36:23.88] uh
[L1073] [36:24.56] print three
[L1074] [36:26.56] has type
[L1075] [36:28.08] IO unit.
[L1076] [36:30.56] It does some IO,
[L1077] [36:32.20] namely printing three, um
[L1078] [36:34.20] get char
[L1079] [36:36.60] has type IO char. It does some IO,
[L1080] [36:39.56] namely reading a character from standard
[L1081] [36:41.32] input, and returns a character.
[L1082] [36:44.44] All right?
[L1083] [36:46.20] Notice that's different from just char.
[L1084] [36:48.08] So, you know, {quotes} x {quote} that
[L1085] [36:50.80] has type char.
[L1086] [36:53.36] It's just a character pure, right?
[L1087] [36:56.84] Get char, the IO performing operation,
[L1088] [36:58.56] has type
[L1089] [36:59.64] IO char. It does some input output,
[L1090] [37:02.12] and returns a character. Okay.
[L1091] [37:05.16] The do notation lets you combine
[L1092] [37:07.20] together,
[L1093] [37:08.36] um
[L1094] [37:09.44] IO performing computations.
[L1095] [37:12.52] So, if you could say do,
[L1096] [37:14.44] and then you say x {left arrow} get
[L1097] [37:16.64] char,
[L1098] [37:18.04] semicolon,
[L1099] [37:21.32] put char x,
[L1100] [37:23.80] then that x {left arrow} get char, that
[L1101] [37:26.00] says run the get char computation,
[L1102] [37:28.84] and get me the character, call it x.
[L1103] [37:31.64] The put char x says
[L1104] [37:33.64] run the put char computation to put x,
[L1105] [37:35.24] and we combine them together with the do
[L1106] [37:36.60] notation, and it combines two
[L1107] [37:39.04] uh two computations to make one IO
[L1108] [37:41.56] performing computation.
[L1109] [37:43.64] Right?
[L1110] [37:45.52] So, but these things are completely
[L1111] [37:47.00] first class. That's what's new about
[L1112] [37:48.84] monads compared to just make it into
[L1113] [37:51.08] into C.
[L1114] [37:52.64] x {left arrow} get char semicolon put
[L1115] [37:54.40] char x.
[L1116] [37:56.12] That's a computation whose type is IO
[L1117] [37:57.96] unit.
[L1118] [37:59.84] Right? Let me give it a name, so I can
[L1119] [38:01.44] say let foo
[L1120] [38:03.24] with type IO unit equals that do.
[L1121] [38:06.16] Now, I can pass foo as an argument to
[L1122] [38:08.16] something. I could put foo in a data
[L1123] [38:09.88] structure. I could return foo as a
[L1124] [38:11.68] result.
[L1125] [38:13.00] It's a value just as much as three
[L1126] [38:16.60] or plus.
[L1127] [38:21.08] In particular, for example, I could say,
[L1128] [38:23.04] "Do foo semicolon foo."
[L1129] [38:27.60] That takes foo, uses it twice. Each time
[L1130] [38:31.44] do foo semicolon foo says, "Do foo." and
[L1131] [38:33.68] then do foo again.
[L1132] [38:35.92] Right? So, I'll read a character and put
[L1133] [38:37.24] it and then read a character and put it
[L1134] [38:38.28] again.
[L1135] [38:40.00] So, these values of type IO T for some
[L1136] [38:44.28] type T are first-class values.
[L1137] [38:48.48] Right?
[L1138] [38:49.64] In C, I can't take X colon equals three
[L1139] [38:52.64] semicolon, you know, Y plus four
[L1140] [38:55.96] and pass that as an argument to
[L1141] [38:58.08] something and expect it to happen
[L1142] [38:59.84] wherever it's used, right? It's not a
[L1143] [39:01.44] first-class value.
[L1144] [39:03.40] >> When I first was learning this this
[L1145] [39:05.24] monad idea, it seems like you've you've
[L1146] [39:07.96] said in a few places it's a way to do
[L1147] [39:10.44] the side effects, but keeps the language
[L1148] [39:12.28] pure. But, when I saw it, my first
[L1149] [39:15.84] thought was it's almost like this little
[L1150] [39:19.44] you know, place where we segregate the
[L1151] [39:22.04] dirty things we want to do, I guess.
[L1152] [39:23.80] But, then how does that keep the
[L1153] [39:25.20] language pure?
[L1154] [39:26.60] >> Oh.
[L1155] [39:27.52] Because because I mean yeah, we are
[L1156] [39:29.36] lying here, but look, if your function
[L1157] [39:31.16] has type int to int, can it do any IO
[L1158] [39:33.68] any IO?
[L1159] [39:34.96] >> No.
[L1160] [39:35.88] >> No.
[L1161] [39:37.08] If it has type int to IO int, it could
[L1162] [39:39.44] do arbitrary IO.
[L1163] [39:42.64] So, yes. So, it's nice pure int to int
[L1164] [39:45.88] function or dirty int to int function.
[L1165] [39:49.00] So, you might say, perhaps you're about
[L1166] [39:50.48] to say, that's a bit of a blunt
[L1167] [39:51.76] instrument.
[L1168] [39:53.88] Either completely pure or completely
[L1169] [39:55.68] dirty, right?
[L1170] [39:59.16] It gets you a awfully long way.
[L1171] [40:03.08] But, nevertheless, it would be cool if
[L1172] [40:05.40] you could um say, "Oh, I am a int to um
[L1173] [40:11.08] effectful
[L1174] [40:12.84] doing reading of files only int."
[L1175] [40:17.92] Right? So, you'd like to in the type
[L1176] [40:20.36] you'd like to say what kind of effects
[L1177] [40:22.48] can it have.
[L1178] [40:25.12] Can it throw exceptions?
[L1179] [40:27.36] Can it, you know, spawn new threads?
[L1180] [40:31.20] So, you'd like to enumerate the effects
[L1181] [40:34.20] this
[L1182] [40:35.48] computation could have, right? That
[L1183] [40:37.24] would be cool.
[L1184] [40:38.44] That's called an effect system.
[L1185] [40:40.40] And there's, you know, Brazilian
[L1186] [40:41.68] programming language papers about effect
[L1187] [40:43.32] systems. And it turns out that you can
[L1188] [40:45.76] indeed in the type system of Haskell
[L1189] [40:48.40] and indeed OCaml is is rapidly becoming
[L1190] [40:50.80] same. Uh you can express
[L1191] [40:53.20] just not just all or nothing, does it do
[L1192] [40:55.72] IO
[L1193] [40:56.80] game over
[L1194] [40:58.36] but rather
[L1195] [40:59.84] which particular effects does it do?
[L1196] [41:03.04] Including no effects at all, that's
[L1197] [41:05.12] pure.
[L1198] [41:05.92] Right?
[L1199] [41:07.92] A good place to start is a library
[L1200] [41:09.52] called Bluefin, which my um colleague
[L1201] [41:11.80] Tom Ellis has designed. It's a very nice
[L1202] [41:14.36] take on how to do effect systems in
[L1203] [41:16.00] Haskell.
[L1204] [41:17.60] >> I guess the purity comes from that this
[L1205] [41:21.44] is this this dirty stuff is signaled
[L1206] [41:24.36] through the type system. So
[L1207] [41:25.68] >> Correct.
[L1208] [41:26.96] >> Okay.
[L1209] [41:27.32] >> Correct. So, we can do it, but here it
[L1210] [41:28.80] is and be aware.
[L1211] [41:31.56] Yep. And because you have to thread, you
[L1212] [41:34.24] know, because the type system gets in
[L1213] [41:35.64] your face, you know, you you were trying
[L1214] [41:37.32] to
[L1215] [41:38.48] um
[L1216] [41:39.32] uh like map, say.
[L1217] [41:41.16] No.
[L1218] [41:42.20] Map says I apply a function to every
[L1219] [41:43.44] element of the list. Well, um
[L1220] [41:45.84] uh
[L1221] [41:46.56] so, it has type A to B to list of A to
[L1222] [41:48.32] list of B. If you were to apply an
[L1223] [41:50.24] IO-performing function, so it the
[L1224] [41:52.24] function you're applying has type like
[L1225] [41:53.80] int to IO of char
[L1226] [41:57.60] you could map that over a list, but you
[L1227] [41:58.92] just get a list of IO of chars.
[L1228] [42:01.40] That hasn't done any IO yet, right?
[L1229] [42:04.64] You want something that says, "Take a
[L1230] [42:06.52] list of IO chars and perform those
[L1231] [42:09.08] actions one at a time." So, I want a
[L1232] [42:10.32] function that goes type from type list
[L1233] [42:12.60] of IO char
[L1234] [42:14.12] to IO of list of char.
[L1235] [42:17.40] Right? And you might want to perform all
[L1236] [42:19.36] those actions
[L1237] [42:21.12] top to bottom, or maybe bottom to top.
[L1238] [42:23.16] Who knows? That's what this
[L1239] [42:25.52] function of type, you know, so yes, so
[L1240] [42:27.40] you could do it in various ways.
[L1241] [42:29.20] So, sometimes it gets in the way, right?
[L1242] [42:30.72] You say, "Oh, you know, can't I
[L1243] [42:32.16] just use map?"
[L1244] [42:33.87] >> [laughter]
[L1245] [42:34.48] >> Well, in Haskell, no, sorry.
[L1246] [42:36.92] You you're going to have to do a little
[L1247] [42:38.40] bit more work to tell me in what
[L1248] [42:39.92] sequence you want your effects to
[L1249] [42:41.28] happen.
[L1250] [42:43.40] Because by default, Haskell does not
[L1251] [42:45.52] specify sequence.
[L1252] [42:47.40] Um so,
[L1253] [42:49.00] the, you know, adding, uh, you know,
[L1254] [42:51.12] monads to control effects does get in
[L1255] [42:52.96] your face a bit.
[L1256] [42:54.36] And that's a that's the tax we pay. In
[L1257] [42:56.56] effect, that's part of the big
[L1258] [42:57.76] experiment that Haskell is doing is to
[L1259] [42:59.92] say, "Suppose we up front say we can
[L1260] [43:02.32] we're willing to pay that tax."
[L1261] [43:04.80] You know, how many followers can we get?
[L1262] [43:09.04] Uh, and the more but I'm I will note
[L1263] [43:12.00] that monads have infected quite a lot of
[L1264] [43:13.64] other languages, like F Sharp is
[L1265] [43:15.04] definitely a call by value impure
[L1266] [43:16.60] language, and yet F Sharp had these
[L1267] [43:18.32] workflows that were definitely monads,
[L1268] [43:20.08] right? Um,
[L1269] [43:21.44] and um,
[L1270] [43:22.52] monads have, you know, appeared in Scala
[L1271] [43:24.20] and in many other many other languages.
[L1272] [43:25.68] So, something that's very monad-like has
[L1273] [43:27.44] appeared lots elsewhere. It's been a
[L1274] [43:29.08] very unifying concept.
[L1275] [43:31.48] >> OpenAI, Anthropic, Cursor, and Vercel
[L1276] [43:35.24] all use this product to make their lives
[L1277] [43:37.00] better.
[L1278] [43:37.96] And the problem it solves is when you're
[L1279] [43:39.84] building SaaS or an ad product and you
[L1280] [43:42.48] want to sell to other companies, there's
[L1281] [43:44.36] all these requirements you need to meet.
[L1282] [43:46.52] There's SSL, there's SCIM, there's RBAC,
[L1283] [43:50.12] there's audit logs. These are all things
[L1284] [43:51.92] that take time to integrate, but aren't
[L1285] [43:54.08] the main focus of your app. WorkOS is an
[L1286] [43:56.40] API layer that lets you meet all of
[L1287] [43:58.08] these requirements in just a few lines
[L1288] [44:00.24] of code. So, let's say you have a new
[L1289] [44:02.32] SaaS product and you want to sell to
[L1290] [44:03.96] other companies, WorkOS will solve all
[L1291] [44:06.44] of these critical feature gaps for you.
[L1292] [44:09.12] You can check them out at workos.com to
[L1293] [44:11.68] learn more and get started. And I
[L1294] [44:13.84] appreciate them for supporting my work
[L1295] [44:15.72] and sponsoring this podcast.
[L1296] [44:17.52] >> When I read [snorts] about Haskell and
[L1297] [44:19.60] people's perception of Haskell, one
[L1298] [44:21.76] thing that keeps coming up is that the
[L1299] [44:24.12] type system is really powerful. And so,
[L1300] [44:27.12] I kind of want to ask you maybe just
[L1301] [44:30.16] even on the highest level, what is a
[L1302] [44:32.32] type system in your words?
[L1303] [44:35.28] >> Okay, so what does a type system do? It
[L1304] [44:37.88] lets you reject silly programs
[L1305] [44:41.04] up front.
[L1306] [44:43.52] So, if I have a function that adds one
[L1307] [44:46.96] to things
[L1308] [44:48.28] and I apply it to a character or to an
[L1309] [44:51.00] IO computation
[L1310] [44:54.36] I'd like to that's going to fail at run
[L1311] [44:56.40] time.
[L1312] [44:58.40] All right? Because I can't add one to a
[L1313] [44:59.64] character. Or maybe you overload plus,
[L1314] [45:01.60] maybe I maybe I reverse reverse a list
[L1315] [45:03.68] or something. If I give If I've got a
[L1316] [45:05.36] list reverse I give it to somebody that
[L1317] [45:06.84] just isn't a list
[L1318] [45:09.12] then it's a bit silly to allow that and
[L1319] [45:10.84] only fail at run time.
[L1320] [45:13.20] So, fundamentally
[L1321] [45:15.08] type systems are about rejecting at
[L1322] [45:17.36] compile time programs that you do not
[L1323] [45:20.00] want to run because they will fail
[L1324] [45:21.96] at run time.
[L1325] [45:23.76] Okay.
[L1326] [45:24.72] Now
[L1327] [45:26.32] um we've had static type systems for a
[L1328] [45:27.96] long time um like uh you know, uh going
[L1329] [45:31.24] back to Pascal um and and earlier uh but
[L1330] [45:35.52] simple type systems are annoying because
[L1331] [45:38.76] they get in the way.
[L1332] [45:40.08] Imagine a function that reverses a list.
[L1333] [45:42.96] In Pascal, you could write a function
[L1334] [45:44.72] that reverses a list of integers.
[L1335] [45:46.80] But if you wanted to reverse a list of
[L1336] [45:48.12] characters
[L1337] [45:49.52] sorry
[L1338] [45:52.08] you can't that that function that
[L1339] [45:53.84] reverses a list of integers it has type
[L1340] [45:56.20] list of int list of int. So, you can't
[L1341] [45:58.12] apply it to a list of characters.
[L1342] [46:00.88] Game over.
[L1343] [46:02.88] You have to write another copy of the
[L1344] [46:04.28] code with a different type.
[L1345] [46:06.72] That's a bit annoying.
[L1346] [46:08.52] So, what are we going to do? We need
[L1347] [46:10.80] polymorphism. We need a more powerful
[L1348] [46:13.04] type system.
[L1349] [46:14.28] We want to give reverse the type for all
[L1350] [46:16.56] A
[L1351] [46:17.52] list of A to list of A. So, that up
[L1352] [46:19.88] front says, I work for any type A.
[L1353] [46:23.36] You give me a list of integers, fine.
[L1354] [46:24.80] I'll produce a list of integers. You
[L1355] [46:25.88] give me a list of characters, fine. I'll
[L1356] [46:27.04] produce a list of characters.
[L1357] [46:29.72] Notice that's much better than just list
[L1358] [46:31.32] to list.
[L1359] [46:32.56] I want to keep the fact there's a list
[L1360] [46:33.84] of integers, so I know if I apply, you
[L1361] [46:36.32] know, when I look inside of this, I know
[L1362] [46:38.00] I've got an integer.
[L1363] [46:39.28] Um but also, if I just list to list, I
[L1364] [46:41.16] might get back a a list of some
[L1365] [46:42.40] completely different type, but I know
[L1366] [46:43.60] that reverse returns a list with the
[L1367] [46:45.60] same type of things.
[L1368] [46:47.60] Right?
[L1369] [46:48.28] So, parametric polymorphism, super
[L1370] [46:50.64] valuable.
[L1371] [46:52.52] Right? If you want a static type system,
[L1372] [46:54.44] you must have parametric polymorphism.
[L1373] [46:57.36] The message is,
[L1374] [46:59.64] if your type system is too simple, it
[L1375] [47:01.76] gets in the way. Very important lesson,
[L1376] [47:03.88] because
[L1377] [47:04.88] it means that we cannot really say is a
[L1378] [47:08.28] type system useful or not unless we say
[L1379] [47:10.52] which one, because we know that
[L1380] [47:12.72] weak type systems are very inconvenient.
[L1381] [47:16.56] It must at least have parametric
[L1382] [47:18.32] polymorphism.
[L1383] [47:19.56] And that is another idea that was born
[L1384] [47:21.76] in the world of functional programming.
[L1385] [47:23.20] It was born in ML, incidentally, Robin
[L1386] [47:25.08] Milner's um
[L1387] [47:26.48] famous dictum, well-typed programs don't
[L1388] [47:27.88] go wrong. ML was a the first I think the
[L1389] [47:30.08] first parametrically polymorphic
[L1390] [47:31.60] function programming language, but
[L1391] [47:33.68] generics in Java and object-oriented
[L1392] [47:36.16] programming more generally is exactly
[L1393] [47:37.60] the same idea.
[L1394] [47:38.92] Right?
[L1395] [47:39.84] So, there's an idea that was born in
[L1396] [47:41.24] functional programming and made its way
[L1397] [47:42.44] into the mainstream.
[L1398] [47:44.24] >> And you mentioned polymorphism, and so
[L1399] [47:46.16] there's this parametric polymorphism in
[L1400] [47:47.92] the type system, but uh in the example
[L1401] [47:51.00] you mentioned where maybe you want to do
[L1402] [47:54.00] an operation on a list, and then the
[L1403] [47:55.92] type of the input changes. Uh I was
[L1404] [47:58.88] think just thinking what about when
[L1405] [48:00.40] people do polymorphism
[L1406] [48:02.52] in the classes?
[L1407] [48:04.04] >> Yeah, okay. But so now you're into a
[L1408] [48:05.76] whole more complicated world, right? So,
[L1409] [48:07.52] as soon as you say class, you're talking
[L1410] [48:09.36] static type system again, right? Um and
[L1411] [48:11.40] so object-oriented programming is is
[L1412] [48:14.24] another approach to polymorphism. So,
[L1413] [48:17.28] in an object-oriented language, we say
[L1414] [48:20.72] if we have a uh Ford that is a car and a
[L1415] [48:24.88] car is a vehicle,
[L1416] [48:26.84] then anything that works on vehicles
[L1417] [48:28.76] should also work on cars and should also
[L1418] [48:30.48] work on Fords.
[L1419] [48:31.84] So,
[L1420] [48:33.12] um the code that we write for cars works
[L1421] [48:36.36] unchanged
[L1422] [48:38.60] for
[L1423] [48:39.72] vehicles and for Fords.
[L1424] [48:41.24] Okay?
[L1425] [48:43.16] Now, that's a form of polymorphism. Not
[L1426] [48:45.40] parametric polymorphism, that's called
[L1427] [48:47.08] what you might call object-oriented
[L1428] [48:48.68] polymor- or subtype polymorphism.
[L1429] [48:51.36] Okay. So, now we but polymorphism in the
[L1430] [48:53.48] sense that the same code
[L1431] [48:57.24] the same executable code, actually the
[L1432] [48:59.00] same machine instructions, work on
[L1433] [49:00.88] values of different types.
[L1434] [49:03.96] Okay? In both cases.
[L1435] [49:05.92] Both reverse a list, same machine
[L1436] [49:07.76] instructions. Code that works on
[L1437] [49:09.56] vehicles works on uh things on Fords,
[L1438] [49:11.04] same machine instructions, right?
[L1439] [49:12.96] Okay.
[L1440] [49:14.40] That's what polymorphism in general
[L1441] [49:15.92] means. Parametric polymorphism means
[L1442] [49:17.92] this for all A, list of A's to list of
[L1443] [49:19.72] A's stuff.
[L1444] [49:20.76] Subtype polymorphism means if it works
[L1445] [49:22.76] on vehicles, it works on any subtype of
[L1446] [49:24.16] vehicles. Okay?
[L1447] [49:26.20] Now, the interaction of the two, which
[L1448] [49:28.72] you get by adding generics to an
[L1449] [49:31.32] object-oriented language,
[L1450] [49:33.36] is pretty complicated.
[L1451] [49:36.52] Oh, and by the way, adding side effects
[L1452] [49:38.00] as well.
[L1453] [49:39.36] And that's why you'll that that and uh
[L1454] [49:41.36] so
[L1455] [49:42.36] uh your question involving classes and
[L1456] [49:44.56] superclasses and so forth is smack in
[L1457] [49:46.88] that complicated world.
[L1458] [49:48.68] And I'm not sure it'll be very fruitful
[L1459] [49:50.68] for us to you know, we'd we'd we'd have
[L1460] [49:52.12] to get a lot more details of the type
[L1461] [49:53.60] system sorted out and know what to say.
[L1462] [49:56.16] Um but at this very high-level overview,
[L1463] [49:58.68] my my sort of the big point I'm trying
[L1464] [50:00.72] to make is weak type systems
[L1465] [50:03.84] get in the way. Type systems are meant
[L1466] [50:05.76] to reject programs that will go wrong,
[L1467] [50:07.72] but my function that reverses a list
[L1468] [50:10.68] of integers, it will also reverse the
[L1469] [50:12.36] list of characters. So, it's tiresome to
[L1470] [50:14.04] be told, "No, that is a bad program."
[L1471] [50:16.68] Right? I want to be able to write that
[L1472] [50:17.88] as that for a list of A to list of A.
[L1473] [50:20.12] So,
[L1474] [50:21.12] the idea of making type system more
[L1475] [50:22.76] complicated is to say uh programs that
[L1476] [50:25.64] you want to run, you can still write in
[L1477] [50:28.44] your static type system. Now, um you
[L1478] [50:30.64] might say, "Well, blimey, if that's all
[L1479] [50:32.64] if that's all, why don't we just get rid
[L1480] [50:33.88] of the static type system altogether?"
[L1481] [50:35.96] Now, we could run all of those programs,
[L1482] [50:37.76] but the trouble is you can run too many
[L1483] [50:39.08] programs now. You can run programs that
[L1484] [50:41.20] will crash at run time, and that's very,
[L1485] [50:43.48] very, very bad, and we all know
[L1486] [50:46.08] the costs of uh programs that that crash
[L1487] [50:48.60] at deployment that you could have
[L1488] [50:50.60] crashed before you even started to run
[L1489] [50:53.04] them, let alone before you even run your
[L1490] [50:54.52] first test.
[L1491] [50:56.52] Right?
[L1492] [50:57.68] Before you even linked it into an
[L1493] [50:59.24] executable,
[L1494] [51:00.60] that's really good. But, the biggest
[L1495] [51:02.68] benefit of a static type system, in my
[L1496] [51:04.60] humble opinion, is maintainability. If
[L1497] [51:07.40] you have a program written in um I don't
[L1498] [51:09.36] know, Pearl or Ruby,
[L1499] [51:11.28] um or um
[L1500] [51:13.44] Lisp in its inner basic form, um and it
[L1501] [51:16.92] was written 15 years ago, and the
[L1502] [51:18.88] original author has left, um and all of
[L1503] [51:21.56] the people who were involved at the time
[L1504] [51:22.80] it was written have left,
[L1505] [51:24.64] then that program is very difficult to
[L1506] [51:26.84] maintain.
[L1507] [51:29.16] And it it becomes almost immutable.
[L1508] [51:31.20] Nobody dares change it anymore. What
[L1509] [51:33.08] they do is it's an immutable piece of
[L1510] [51:34.84] software, and you do that stuff around
[L1511] [51:36.24] the edges to impedance match what you
[L1512] [51:38.40] really want to do to this now immutable
[L1513] [51:40.40] blob.
[L1514] [51:41.48] Now, of course, you have lots of tests.
[L1515] [51:43.44] So, test-driven development, I'm totally
[L1516] [51:45.32] with it. I love all any of all of that.
[L1517] [51:46.84] But,
[L1518] [51:47.84] still
[L1519] [51:49.64] GHC, for example, is itself written in
[L1520] [51:51.96] Haskell. It's 35 years old, and yet I do
[L1521] [51:55.00] large-scale systematic refactorings of
[L1522] [51:57.48] it,
[L1523] [51:58.52] you know,
[L1524] [51:59.60] fearlessly,
[L1525] [52:01.00] because the type system keeps me safe.
[L1526] [52:02.40] In fact, often what I'll do is I'll
[L1527] [52:04.32] change a few types and then start
[L1528] [52:05.68] compiling,
[L1529] [52:07.36] and then a sort of wave of changes
[L1530] [52:09.04] propagate through forced by, you know, I
[L1531] [52:10.84] just get type errors. So, I know what to
[L1532] [52:12.36] do.
[L1533] [52:13.60] Whereas the thought that I've changed
[L1534] [52:15.60] the representation of this data
[L1535] [52:16.72] structure a little bit, but I've added a
[L1536] [52:17.84] field to this data structure, where in
[L1537] [52:20.68] the entire compiler might that field be
[L1538] [52:22.80] read, written, or or freshly allocated?
[L1539] [52:27.12] I can't imagine how anybody maintains
[L1540] [52:29.12] 30-year-old software and makes
[L1541] [52:30.96] large-scale changes like that
[L1542] [52:33.08] without a type system. It's
[L1543] [52:34.12] unimaginable. So, for me,
[L1544] [52:36.04] the benefit of type systems is
[L1545] [52:38.24] maintainability. Oh, and designability,
[L1546] [52:40.28] right? So, a type um I often write the
[L1547] [52:42.84] types of my programs up front. I write
[L1548] [52:45.12] the type, you know, the data types are
[L1549] [52:47.24] super perspicuous.
[L1550] [52:49.84] You know, if I say uh it's a bit like
[L1551] [52:52.16] writing the classes of a of an of an
[L1552] [52:54.04] object-oriented language, right? But, if
[L1553] [52:55.68] you have no types, no classes, nothing,
[L1554] [52:57.88] just, I don't know, S-expressions,
[L1555] [53:00.72] >> [laughter]
[L1556] [53:02.00] >> uh
[L1557] [53:02.60] types are the way I design language.
[L1558] [53:04.36] They're they're the way that I start
[L1559] [53:05.72] writing my designs.
[L1560] [53:07.20] >> I'm trying to understand uh other
[L1561] [53:09.04] mindset, like let's say C, for instance,
[L1562] [53:11.24] where I remember a lot of stuff when I
[L1563] [53:13.76] was learning it in college, for
[L1564] [53:14.96] instance,
[L1565] [53:16.32] uh many times where I I'd add a
[L1566] [53:18.68] character to a pointer or something, and
[L1567] [53:20.72] it it just works cuz
[L1568] [53:22.60] it interprets the character as a number.
[L1569] [53:25.64] Um and so, is there any value to having
[L1570] [53:29.80] that kind of type system, or is that
[L1571] [53:31.88] just strictly unredeemable?
[L1572] [53:34.96] >> Just use stronger.
[L1573] [53:37.00] I think there's no benefit to weaker.
[L1574] [53:39.40] >> Just off the top of my head, one thing I
[L1575] [53:41.64] think of is there is a set of programs
[L1576] [53:44.72] that will work but don't satisfy the
[L1577] [53:48.88] type system.
[L1578] [53:49.84] >> that's right.
[L1579] [53:50.64] >> That and but those are
[L1580] [53:52.92] I mean, I don't know if they're good.
[L1581] [53:54.16] That's subjective.
[L1582] [53:54.88] >> they may be good. So So So So uh uh that
[L1583] [53:58.72] like I like we started, if you have
[L1584] [54:01.00] Pascal
[L1585] [54:02.48] and you write a function to reverse a
[L1586] [54:04.04] list of integers, then if you apply it
[L1587] [54:05.92] to a list of characters, the same
[L1588] [54:07.40] machine instructions would work but it
[L1589] [54:09.96] is rejected, right?
[L1590] [54:12.08] So, we have rejected a perfectly decent
[L1591] [54:14.32] program, bad,
[L1592] [54:16.12] right? Our goal is to expand the
[L1593] [54:20.20] collection of the programs that satisfy
[L1594] [54:21.84] the type system
[L1595] [54:23.64] to include as many as possible of the
[L1596] [54:25.88] programs we want to run
[L1597] [54:27.84] without including any of the bad
[L1598] [54:29.60] programs that we don't want to run.
[L1599] [54:32.20] Okay?
[L1600] [54:33.68] Parametric polymorphism is a big step in
[L1601] [54:35.80] that direction.
[L1602] [54:38.16] Um other, you know, type system
[L1603] [54:40.00] innovations are a big step in that
[L1604] [54:41.44] direction, but there will always be some
[L1605] [54:43.92] programs
[L1606] [54:45.48] that would run perfectly well
[L1607] [54:50.04] that the type system rejects.
[L1608] [54:53.72] Imagine a tree that is um uh contains
[L1609] [54:58.04] integers at every node.
[L1610] [55:00.32] But
[L1611] [55:02.16] if you are 17 deep in the tree or 34 or
[L1612] [55:06.92] 51
[L1613] [55:09.12] if you're in a multiple of 17 deep, the
[L1614] [55:11.16] integers can be characters instead. Or
[L1615] [55:13.80] the integers all turn out to be
[L1616] [55:14.80] characters, right?
[L1617] [55:17.28] Now,
[L1618] [55:18.32] you could write a program that generated
[L1619] [55:20.04] such trees and you could write a program
[L1620] [55:21.76] that consumed such trees knowing that
[L1621] [55:23.64] every 17th
[L1622] [55:25.00] um layer we switch to characters
[L1623] [55:27.12] but most static type systems would make
[L1624] [55:29.40] it pretty hard for you to accept that
[L1625] [55:31.16] program. And yet, it will run.
[L1626] [55:35.96] Now, you might say, "Oh, but I really
[L1627] [55:37.68] want to write that program, guys. You
[L1628] [55:39.04] know, don't get in my way." Well,
[L1629] [55:41.36] then
[L1630] [55:42.44] um
[L1631] [55:43.40] uh then we should provide a way for you
[L1632] [55:45.88] to bail out into dynamic typing.
[L1633] [55:48.72] Right?
[L1634] [55:49.80] What I'd like to do is to say, "Okay, so
[L1635] [55:52.12] if all else fails, then at least you
[L1636] [55:54.24] can, as it were, pair up a value with
[L1637] [55:56.72] its type representation." As one reason
[L1638] [55:58.72] we don't want to interpret an integer as
[L1639] [56:01.08] a double-precision float, for example,
[L1640] [56:03.84] is that, you know, they don't even have
[L1641] [56:05.44] the same representation, which is just
[L1642] [56:06.96] just nonsense. Right?
[L1643] [56:09.04] One possible way, which it untyped
[L1644] [56:10.96] languages let you do, is to tag every
[L1645] [56:12.92] integer and every double-precision float
[L1646] [56:14.88] with the fact, "I'm an integer. I'm a
[L1647] [56:16.36] double-precision float." But that has a
[L1648] [56:17.56] lot of overhead.
[L1649] [56:19.56] So, one merit, and it's not I think it's
[L1650] [56:22.12] not the biggest single merit, is a major
[L1651] [56:23.96] merit of static type systems, is you
[L1652] [56:25.52] have no tags.
[L1653] [56:27.60] You know that if it says it's an
[L1654] [56:29.36] integer, it's going to be an integer.
[L1655] [56:30.68] You know that if it's a double-precision
[L1656] [56:32.44] float, it's going to be double-precision
[L1657] [56:33.48] float. Right?
[L1658] [56:35.12] But if you're not sure, um maybe we
[L1659] [56:37.52] could make a way to make a pair of a
[L1660] [56:40.92] type representation and this value. The
[L1661] [56:43.32] type representation is now like a
[L1662] [56:45.32] runtime tag. It's like a little runtime
[L1663] [56:47.20] data structure that describes the type.
[L1664] [56:49.60] And then in your program, you could say,
[L1665] [56:51.20] "Now I want to say, uh I've got this
[L1666] [56:53.48] type dynamic. We'll call this pair a
[L1667] [56:55.84] value of type dynamic." Now, when I want
[L1668] [56:58.80] to take a value of type dynamic and
[L1669] [57:00.48] treat it as a character, we'll say, "Ah,
[L1670] [57:02.88] look Look at the type dynamic. See if it
[L1671] [57:05.52] says it's character. If it is, return
[L1672] [57:06.84] the character. If not, crash." Right?
[L1673] [57:08.80] Runtime failure.
[L1674] [57:10.40] That's fine. You can do that. So, um
[L1675] [57:12.84] and uh Haskell has good support for
[L1676] [57:15.00] dynamic typing where necessary. So, my
[L1677] [57:17.48] uh my my story would be static typing
[L1678] [57:20.76] should expand as as to carry as much as
[L1679] [57:23.12] possible.
[L1680] [57:24.20] And where you absolutely cannot do it,
[L1681] [57:26.40] sorry, then use dynamic typing, and
[L1682] [57:28.56] we'll provide facilities to support
[L1683] [57:29.84] that.
[L1684] [57:30.92] >> One thing I wanted to to talk with you
[L1685] [57:32.96] about is the compiler. How does the GHC
[L1686] [57:35.68] work on a on a high level?
[L1687] [57:37.48] >> So,
[L1688] [57:38.52] GHC takes a string like like any other
[L1689] [57:40.84] compiler that the source code of the
[L1690] [57:42.40] program, parses it.
[L1691] [57:45.32] Um and then it um
[L1692] [57:48.44] uh type checks it.
[L1693] [57:49.96] Because that is this a type correct
[L1694] [57:51.00] program.
[L1695] [57:52.56] Then it converts it to lambda calculus.
[L1696] [57:58.32] Now,
[L1697] [57:59.28] Haskell the Haskell AST, the original
[L1698] [58:01.80] source tree, has
[L1699] [58:04.04] 50 different data types, 50 different
[L1700] [58:06.12] kinds of nodes, some of which have 30 or
[L1701] [58:08.52] 40 different variants.
[L1702] [58:10.80] So, it's a really big, diverse,
[L1703] [58:13.80] complicated data structure.
[L1704] [58:16.08] The AST.
[L1705] [58:17.92] Lambda calculus has this
[L1706] [58:19.80] variant of the lambda calculus has
[L1707] [58:21.04] eight.
[L1708] [58:24.00] One to data type that maybe two or three
[L1709] [58:25.64] data types with eight constructors.
[L1710] [58:27.80] So, it's like taking a gigantic language
[L1711] [58:31.76] and squeezing it down into a tiny one.
[L1712] [58:36.32] And that tiny one we can then optimize,
[L1713] [58:38.20] right? That's the optimizer works on
[L1714] [58:39.48] that. So, the front end
[L1715] [58:41.72] does parse, rename, type check, desugar
[L1716] [58:44.88] into lambda calculus. That's the front
[L1717] [58:46.68] end.
[L1718] [58:48.80] The lambda calculus, particular
[L1719] [58:50.08] language, is called GHC's core language.
[L1720] [58:52.88] I'm quite proud of it cuz it's been very
[L1721] [58:55.32] very stable.
[L1722] [58:57.76] It's 35 years old and it has barely
[L1723] [59:00.84] changed since birth.
[L1724] [59:02.40] That's amazing, right? Because Haskell
[L1725] [59:04.12] has changed a lot, a lot.
[L1726] [59:07.60] Right? So, almost all of the innovation
[L1727] [59:10.48] in Haskell
[L1728] [59:12.40] has been in the front end.
[L1729] [59:14.64] Very little
[L1730] [59:16.24] in core.
[L1731] [59:18.56] Now, the back end, the core optimizer,
[L1732] [59:20.60] has changed a lot, too.
[L1733] [59:22.24] But all of the changes that were useful
[L1734] [59:23.84] there would have been useful 30 years
[L1735] [59:25.08] ago, right?
[L1736] [59:26.68] Yeah. So, they're two completely
[L1737] [59:28.36] separable things. So, I'm quite proud
[L1738] [59:29.44] about that. Core then we do a lot of
[L1739] [59:31.36] core-to-core passes that simply take
[L1740] [59:33.08] core program core program programs,
[L1741] [59:35.00] right? Lots and lots. Long pipeline.
[L1742] [59:37.92] Then we convert it um
[L1743] [59:40.84] uh to C-- which is a prototypical
[L1744] [59:44.20] imperative language. Think of it as a
[L1745] [59:46.12] portable assembly code.
[L1746] [59:48.28] Right? So, that bit is meant to be
[L1747] [59:50.28] platform independent.
[L1748] [59:52.32] So, it's simply that's the compiler that
[L1749] [59:54.48] take your program I said if you take
[L1750] [59:55.68] lambda calculus and compile it that's
[L1751] [59:57.92] that step, right? I want to compile the
[L1752] [01:00:00.08] lambda calculus into
[L1753] [01:00:02.04] you know, machine instructions really.
[L1754] [01:00:04.32] But I don't really mean machine instruc-
[L1755] [01:00:05.56] I mean portable machine instructions.
[L1756] [01:00:07.68] That's called C--
[L1757] [01:00:09.88] Then I want to convert C-- into actual
[L1758] [01:00:12.12] machine instructions for various
[L1759] [01:00:13.24] platforms. And then we could either do
[L1760] [01:00:15.04] that directly with a native code backend
[L1761] [01:00:16.64] or go via LLVM.
[L1762] [01:00:18.76] >> Interesting. I've never heard of C--
[L1763] [01:00:21.52] What Why not just go directly to I would
[L1764] [01:00:23.80] have thought maybe assembly or something
[L1765] [01:00:25.44] like that?
[L1766] [01:00:26.40] >> what happens in assembly in which for
[L1767] [01:00:28.08] which processor, please?
[L1768] [01:00:30.92] >> Oh, I see.
[L1769] [01:00:32.02] >> [laughter]
[L1770] [01:00:32.44] >> I guess it's the I would have thought
[L1771] [01:00:34.28] the lambda calculus part was already
[L1772] [01:00:35.96] portable. So, you just
[L1773] [01:00:37.08] >> It is, yeah. You could go straight but
[L1774] [01:00:39.88] but but so, there's work to go from
[L1775] [01:00:41.64] lambda calculus you could go all the way
[L1776] [01:00:43.08] to x86.
[L1777] [01:00:44.92] Then throw all that away and now go from
[L1778] [01:00:46.64] lambda calculus to pal PC.
[L1779] [01:00:49.32] Oh dear, I've just duplicated a lot of
[L1780] [01:00:50.96] work.
[L1781] [01:00:53.36] By going from lambda calculus to C-- and
[L1782] [01:00:56.12] then from C-- to x86 C-- We've set We've
[L1783] [01:00:59.60] We've avoided duplicating
[L1784] [01:01:02.24] the work that went from lambda calculus
[L1785] [01:01:04.32] to C-- right?
[L1786] [01:01:06.04] When you see it like that it's pretty
[L1787] [01:01:07.08] obvious, isn't it? Like you got to You
[L1788] [01:01:09.00] want to make the platform specific bit
[L1789] [01:01:11.84] as small as possible.
[L1790] [01:01:14.16] You would like to have as it were like a
[L1791] [01:01:16.16] generic architecture. One that can do
[L1792] [01:01:18.24] addition and has a program counter and a
[L1793] [01:01:19.96] stack and so forth.
[L1794] [01:01:21.72] That's all C-- just a portable assembly
[L1795] [01:01:23.80] language.
[L1796] [01:01:24.84] And then you say, "Oh, the nitty-gritty
[L1797] [01:01:26.32] of, you know, whether you have double
[L1798] [01:01:28.68] precision add and set the floating-point
[L1799] [01:01:30.72] bit here and there." That, well, that's
[L1800] [01:01:32.12] platform specific. The core is itself
[L1801] [01:01:34.16] statically typed. You know, but it's
[L1802] [01:01:36.08] always a surprising because no other
[L1803] [01:01:37.56] compiler does has this property, no
[L1804] [01:01:39.16] other production compiler.
[L1805] [01:01:40.88] By core statically typed, I don't just
[L1806] [01:01:42.56] mean that the initial the initial
[L1807] [01:01:43.80] program was type correct.
[L1808] [01:01:45.84] I mean that a core program, you can run
[L1809] [01:01:48.00] a type checker on that. And I might say,
[L1810] [01:01:49.88] "Why do you need to? Because after all,
[L1811] [01:01:51.44] if GHC is correct, it started with a
[L1812] [01:01:53.76] type correct core program
[L1813] [01:01:55.76] because it came from a type correct
[L1814] [01:01:56.68] Haskell program, assuming the desugaring
[L1815] [01:01:58.40] was right, and all the optimizations, if
[L1816] [01:02:00.60] they're right, will generate a type
[L1817] [01:02:02.48] correct core program. So, why do you
[L1818] [01:02:04.00] need to type check it?"
[L1819] [01:02:05.80] Answer:
[L1820] [01:02:06.92] to discover bugs in GHC.
[L1821] [01:02:09.28] Now, these are serious bugs, right? If
[L1822] [01:02:11.12] you ever take a type correct core
[L1823] [01:02:13.92] program and an optimization pass
[L1824] [01:02:15.32] produces a type incorrect
[L1825] [01:02:17.52] core program,
[L1826] [01:02:19.36] what will happen?
[L1827] [01:02:21.04] If we don't have the type checker for
[L1828] [01:02:22.44] core,
[L1829] [01:02:23.64] we'll generate machine code and we'll
[L1830] [01:02:25.04] run it and we'll get a seg fault.
[L1831] [01:02:28.96] Now, we have to backtrack for any
[L1832] [01:02:30.52] particular test program that now
[L1833] [01:02:31.96] crashes,
[L1834] [01:02:34.20] all the way to back up the pipeline, up
[L1835] [01:02:36.56] the pipeline, up the pipeline, up the
[L1836] [01:02:37.80] pipeline. Oh, it was this pass
[L1837] [01:02:41.08] of GHC that was faulty.
[L1838] [01:02:43.52] That's super hard to do because, you
[L1839] [01:02:45.60] know, you're getting out GDB on some
[L1840] [01:02:47.60] runtime failure
[L1841] [01:02:49.60] that is an indirect and perhaps distant
[L1842] [01:02:51.40] consequence
[L1843] [01:02:52.88] of the fact you just generated a type,
[L1844] [01:02:55.40] you know, you just made a you had a bug
[L1845] [01:02:57.28] in the optimizer.
[L1846] [01:02:59.48] So, it is amazing
[L1847] [01:03:01.76] to have a type checker for core.
[L1848] [01:03:04.36] Now,
[L1849] [01:03:05.20] why does nobody else do this? Well, it's
[L1850] [01:03:07.28] because their intermediate language,
[L1851] [01:03:08.76] typically, and this I really am talking
[L1852] [01:03:10.36] typically because I know of no other
[L1853] [01:03:11.88] compiler that has this property, none,
[L1854] [01:03:14.12] production compiler,
[L1855] [01:03:16.28] typically then they're, you know,
[L1856] [01:03:17.20] complex complex syntax trees decorated
[L1857] [01:03:19.40] with all sorts of pragmatic information
[L1858] [01:03:21.24] and things hanging on it onto it here
[L1859] [01:03:23.20] and there and
[L1860] [01:03:24.76] um
[L1861] [01:03:26.44] um you know, there's no there's no type
[L1862] [01:03:28.80] checker for it at all.
[L1863] [01:03:31.12] And there's no hope of one.
[L1864] [01:03:33.20] So, I'm very proud of the fact that core
[L1865] [01:03:35.20] is statically typed and I'm also also
[L1866] [01:03:38.76] think it's a
[L1867] [01:03:40.72] The most delightful thing is that the
[L1868] [01:03:42.88] way that it is statically typed it is a
[L1869] [01:03:45.00] It's an implementation of something
[L1870] [01:03:46.16] called system F.
[L1871] [01:03:48.44] So, system F when I said lambda calculus
[L1872] [01:03:50.24] lambda calculus as Alonzo Church had it
[L1873] [01:03:52.36] was untyped had no type system at all.
[L1874] [01:03:55.48] But Girard defined defined something
[L1875] [01:03:57.60] called system F which is a statically
[L1876] [01:03:59.80] typed lambda calculus a rather powerful
[L1877] [01:04:01.88] one. And core is essentially system F.
[L1878] [01:04:06.16] So, we literally adopted something from
[L1879] [01:04:08.12] the nerdy theoretical computer science
[L1880] [01:04:10.88] you know, logic community logic and
[L1881] [01:04:13.48] mathematics community and adopted it
[L1882] [01:04:15.24] directly in a in a production
[L1883] [01:04:17.00] implementation.
[L1884] [01:04:18.72] So,
[L1885] [01:04:19.84] I'm very proud of that.
[L1886] [01:04:21.32] Um I think core is
[L1887] [01:04:23.52] and the fact that we can do we have 35
[L1888] [01:04:26.20] years of worth of development that has
[L1889] [01:04:27.48] been not just not impeding but actively
[L1890] [01:04:29.76] aided by statically typed intermediate
[L1891] [01:04:31.20] language is really
[L1892] [01:04:32.68] a big marker in the ground.
[L1893] [01:04:35.00] >> You know, watching all your talks,
[L1894] [01:04:36.24] reading everything. One of the
[L1895] [01:04:38.00] interesting data points that you brought
[L1896] [01:04:39.72] up was that uh Haskell is talked about
[L1897] [01:04:43.60] more than used when you compared Stack
[L1898] [01:04:46.76] Overflow volume and you know, actually
[L1899] [01:04:49.12] GitHub volume. Like who's actually using
[L1900] [01:04:50.96] the programming language? Why do you
[L1901] [01:04:52.76] think that is?
[L1902] [01:04:55.00] >> So,
[L1903] [01:04:56.12] Haskell embodies one
[L1904] [01:04:59.20] key idea.
[L1905] [01:05:01.04] Immutability changes everything. There's
[L1906] [01:05:03.24] a quote from Pat Helland's talk that I
[L1907] [01:05:04.68] think you also paper which I think you
[L1908] [01:05:06.64] also looked at or read. Um So, it says
[L1909] [01:05:08.76] programming with values changes
[L1910] [01:05:10.32] everything about the way you think about
[L1911] [01:05:11.76] programming.
[L1912] [01:05:13.08] It's just
[L1913] [01:05:14.60] mind-changing. It's not necessarily
[L1914] [01:05:16.24] better, but it is different. And so,
[L1915] [01:05:18.96] Haskell takes that idea and runs with
[L1916] [01:05:20.76] it. Everything is driven by that one
[L1917] [01:05:22.60] idea. Everything else is incidental.
[L1918] [01:05:25.24] Uh in the early days, that meant we just
[L1919] [01:05:27.40] said, "Well, guys, suck it up, you know,
[L1920] [01:05:28.96] we'll keep um changing the language, and
[L1921] [01:05:31.24] if it breaks your programs, too bad." Um
[L1922] [01:05:34.20] so, it is, you know, a bit peculiar, and
[L1923] [01:05:35.96] therefore, um oh also, it felt a bit
[L1924] [01:05:37.96] academic, cuz initially, it was really
[L1925] [01:05:39.40] not very powerful. It was taking the key
[L1926] [01:05:41.00] idea, but you couldn't do very much with
[L1927] [01:05:42.60] it. We talked about that, right?
[L1928] [01:05:44.48] So, over time, GHC and on Haskell in in
[L1929] [01:05:47.44] general has become more and more
[L1930] [01:05:48.64] powerful. The type system has become
[L1931] [01:05:49.88] less and less in your way, and more and
[L1932] [01:05:51.84] more useful. The you know, all the
[L1933] [01:05:53.60] obstacles that make functional
[L1934] [01:05:54.84] programming harder become better. The
[L1935] [01:05:56.44] compiler generates faster code, it
[L1936] [01:05:57.96] compiles faster, and so forth. So, um
[L1937] [01:06:01.60] uh
[L1938] [01:06:02.80] So, it has become less, uh if you like,
[L1939] [01:06:05.04] peculiar. Um so, we've become more and
[L1940] [01:06:07.32] more taking into account the the um the
[L1941] [01:06:10.80] uh the needs of our users. But in a way,
[L1942] [01:06:13.08] the sort of cultural heritage is we
[L1943] [01:06:15.12] never give up on the one core principle.
[L1944] [01:06:17.48] We're just not going to give you
[L1945] [01:06:18.80] unrestricted side effects. Sorry.
[L1946] [01:06:20.80] Right?
[L1947] [01:06:21.72] You want to say I'm fully before I am,
[L1948] [01:06:23.32] and put up with the consequences. So,
[L1949] [01:06:25.36] we're going to stick to one core
[L1950] [01:06:26.52] principle, and then we'll we'll do lots
[L1951] [01:06:28.52] of work around the edges to make that
[L1952] [01:06:29.56] better. Right, so, um
[L1953] [01:06:31.96] that does limit our community somewhat,
[L1954] [01:06:33.80] right? It does mean you have to You
[L1955] [01:06:35.52] really have to think in a different way.
[L1956] [01:06:37.12] Immutability changes everything. That
[L1957] [01:06:38.60] means you'd have to think a different
[L1958] [01:06:39.56] way about about programming. Maybe you
[L1959] [01:06:41.28] don't want to think in a different way.
[L1960] [01:06:42.36] That's fine. Then don't use Haskell,
[L1961] [01:06:44.20] right? So, uh so, in a way, we've um we
[L1962] [01:06:47.96] we started from a very small user
[L1963] [01:06:49.44] community, uh very sort of pure and
[L1964] [01:06:51.16] nerdy one, and going going larger and
[L1965] [01:06:52.64] larger, but all slowly, slowly, but all
[L1966] [01:06:54.80] the time main- maintaining uh
[L1967] [01:06:56.40] faithfulness to this core principle.
[L1968] [01:06:58.08] >> I thought that was
[L1969] [01:06:59.64] very unique about Haskell, because I
[L1970] [01:07:02.28] feel a lot of the other programming
[L1971] [01:07:04.36] languages are user-centric. I mean, if
[L1972] [01:07:07.48] if people something, they work on it,
[L1973] [01:07:09.80] they add it. Whereas, Haskell feels more
[L1974] [01:07:13.04] principled or it's it's all starting
[L1975] [01:07:15.32] from these ideas. And if you don't
[L1976] [01:07:19.48] satisfy these ideas as a user, yeah,
[L1977] [01:07:22.16] well, we yeah, that's that's fine.
[L1978] [01:07:24.92] Um for instance, in one of your talks,
[L1979] [01:07:26.60] you mentioned somewhere that there was a
[L1980] [01:07:28.64] release of the compiler where if a file
[L1981] [01:07:32.20] wasn't type correct, then the compiler
[L1982] [01:07:35.36] would delete the file.
[L1983] [01:07:37.52] >> Oh, wait. It would report with the error
[L1984] [01:07:38.60] message first.
[L1985] [01:07:39.88] >> Yeah, it reports there. But, I thought
[L1986] [01:07:41.64] that was that was absurd. I mean, very
[L1987] [01:07:44.68] hostile, I guess, to the I mean, well,
[L1988] [01:07:46.80] it's it's if you're type safe, no
[L1989] [01:07:48.68] problems. But,
[L1990] [01:07:50.08] >> Oh, it was a mistake, right? It was a
[L1991] [01:07:51.80] bug. It wasn't deliberate.
[L1992] [01:07:54.15] >> [laughter]
[L1993] [01:07:55.24] >> And it only happened, you know, how did
[L1994] [01:07:56.72] the bug get, you know, get out? Because,
[L1995] [01:07:58.16] of course, if it always did that, we'd
[L1996] [01:07:59.52] have noticed.
[L1997] [01:08:00.84] Um how did it get into a release? Well,
[L1998] [01:08:02.60] it was because it was only on Windows
[L1999] [01:08:04.04] and only when you compile a module that
[L2000] [01:08:05.48] was not in the current directory.
[L2001] [01:08:07.64] But, at that stage, our um
[L2002] [01:08:09.60] our users were very forgiving. And, you
[L2003] [01:08:11.08] know, somebody wrote to us and said,
[L2004] [01:08:12.24] "Well, by the way, Simon, you might like
[L2005] [01:08:13.56] to know that, you know, GHC does this.
[L2006] [01:08:14.92] But, hey, don't worry about it, you
[L2007] [01:08:16.00] know, I just copy all my files somewhere
[L2008] [01:08:17.68] else before I compile and then I copy
[L2009] [01:08:19.44] them back."
[L2010] [01:08:21.72] So, of course, those days are long gone.
[L2011] [01:08:23.56] We pay a lot more attention to our users
[L2012] [01:08:25.20] and have much more rigorous CI testing
[L2013] [01:08:27.04] than ever we did, right? So, um
[L2014] [01:08:29.44] that's a that's a a story from a long
[L2015] [01:08:31.04] time ago, but it's a good cultural story
[L2016] [01:08:32.80] because it suggests that we've cared
[L2017] [01:08:34.92] about our users very much, but we we we
[L2018] [01:08:37.76] care about users who want in the in
[L2019] [01:08:39.72] their hearts want to be principled.
[L2020] [01:08:41.40] We're trying to appeal to One One of the
[L2021] [01:08:43.24] things I like best about Haskell is
[L2022] [01:08:44.72] people often say, "I just enjoy writing
[L2023] [01:08:47.64] Haskell."
[L2024] [01:08:48.72] Right? It's fun, right? My boss doesn't
[L2025] [01:08:51.60] allow me to because, you know, it
[L2026] [01:08:55.00] somehow doesn't fit with my production
[L2027] [01:08:56.52] shop. And And I but but for me, I would
[L2028] [01:08:59.16] go for I love writing this stuff every
[L2029] [01:09:02.24] time. Every time. Yeah,
[L2030] [01:09:04.76] that's that's very rewarding to me.
[L2031] [01:09:07.00] >> There's also this interesting, I don't
[L2032] [01:09:09.16] know if it's a cultural value, but it's
[L2033] [01:09:10.96] a statement that you say often in the
[L2034] [01:09:13.12] context of these older talks. You say
[L2035] [01:09:16.12] that you avoid success at all costs.
[L2036] [01:09:19.68] Could Could you explain what you mean by
[L2037] [01:09:21.20] that phrase?
[L2038] [01:09:21.92] >> Oh, yeah, this was just a little a
[L2039] [01:09:23.44] little play on words.
[L2040] [01:09:25.56] It was in a retrospective on Haskell I
[L2041] [01:09:27.48] gave as an invited talk at and um
[L2042] [01:09:30.28] Popple in a long time ago, probably 20
[L2043] [01:09:32.72] years ago. Uh so, it's a it's a little
[L2044] [01:09:35.08] play on words because it you can read it
[L2045] [01:09:36.84] as either avoid success at all costs.
[L2046] [01:09:41.60] And that's what we've been discussing.
[L2047] [01:09:43.20] Success at all costs means compromise
[L2048] [01:09:44.96] your principles in order to satisfy your
[L2049] [01:09:47.08] users or think that you're satisfying
[L2050] [01:09:48.84] users, you know, uh give them what they
[L2051] [01:09:51.24] say they want. Uh where more if we build
[L2052] [01:09:53.52] it, they will come kind of deal, right?
[L2053] [01:09:55.48] So,
[L2054] [01:09:56.48] avoid success at all costs. Or if you
[L2055] [01:09:59.36] parenthesize the other way, it says
[L2056] [01:10:00.76] avoid success
[L2057] [01:10:02.32] at all costs.
[L2058] [01:10:05.44] Or at all costs avoid success. And
[L2059] [01:10:07.84] that's saying uh that's a little joke,
[L2060] [01:10:10.04] but it says if you're too successful and
[L2061] [01:10:12.28] have too many users, it becomes more
[L2062] [01:10:14.24] difficult to make changes.
[L2063] [01:10:17.72] And we experience that right now. So, I
[L2064] [01:10:19.84] devote many many more of my personal
[L2065] [01:10:22.28] cycles to backward compati-
[L2066] [01:10:25.00] compatibility issues than ever I did.
[L2067] [01:10:28.24] I've devoted hundreds of uh you know, uh
[L2068] [01:10:30.72] hours and hours and well,
[L2069] [01:10:32.68] days and days, weeks and weeks in the
[L2070] [01:10:33.88] last year or two to the following what
[L2071] [01:10:36.88] seems to be a very simple property. If
[L2072] [01:10:40.68] if you can compile a program, a package,
[L2073] [01:10:43.60] in a whole program with GHC 10.0 and we
[L2074] [01:10:46.12] release GHC 10.2, you should be able to
[L2075] [01:10:48.32] compile that same package unchanged with
[L2076] [01:10:50.64] GHC 10.2.
[L2077] [01:10:53.36] Seems reasonable, right?
[L2078] [01:10:55.72] After all, 10.2 should just be better.
[L2079] [01:10:58.76] But, no.
[L2080] [01:10:59.88] GHC has never had that property.
[L2081] [01:11:02.20] And making it have that property has
[L2082] [01:11:03.64] turned out to be very, very
[L2083] [01:11:04.92] time-consuming. Previously, we just
[L2084] [01:11:06.48] never cared.
[L2085] [01:11:08.24] Then we started to care, but thought it
[L2086] [01:11:10.20] was a lot of work, and now we're
[L2087] [01:11:11.52] investing the work.
[L2088] [01:11:13.08] >> I guess that was from a long time ago. I
[L2089] [01:11:15.32] think nowadays, software engineering,
[L2090] [01:11:18.08] there's been a major shift in the last
[L2091] [01:11:19.68] year where a lot of code is being
[L2092] [01:11:21.88] generated by these models or these LLMs.
[L2093] [01:11:25.84] How do you see programming language
[L2094] [01:11:27.52] design shifting to accommodate a world
[L2095] [01:11:30.24] where a lot of the code is no longer
[L2096] [01:11:32.48] written by humans?
[L2097] [01:11:34.12] >> I think it may be the best thing that's
[L2098] [01:11:36.36] happened to statically typed languages
[L2099] [01:11:38.08] for a long time.
[L2100] [01:11:40.20] Because, as we've been discussing,
[L2101] [01:11:43.16] with a static type system, you cut down
[L2102] [01:11:46.04] the space of programs that the LLM can
[L2103] [01:11:48.24] generate.
[L2104] [01:11:50.16] Because it is perfectly capable of
[L2105] [01:11:51.96] running the compiler and saying, "Oh,
[L2106] [01:11:53.04] darn, that was a bad program. Better fix
[L2107] [01:11:54.64] it."
[L2108] [01:11:56.24] Right? So, a zillion iterations get done
[L2109] [01:11:59.60] behind the scenes.
[L2110] [01:12:01.92] Whereas in an untyped language, the
[L2111] [01:12:03.24] first one it coughed up, you'd have had
[L2112] [01:12:04.68] to run or run against its test suite, or
[L2113] [01:12:06.76] who knows what, but it's it drastically
[L2114] [01:12:09.36] tightens up that cycle.
[L2115] [01:12:11.36] Right?
[L2116] [01:12:12.32] So, I think that statically typed
[L2117] [01:12:15.08] languages are huge boon for LLMs.
[L2118] [01:12:18.48] Because it's too easy to
[L2119] [01:12:19.92] Programs are just strings, right? We
[L2120] [01:12:21.24] could um
[L2121] [01:12:23.28] They can just generate the next
[L2122] [01:12:24.68] plausible word, uh and you want you want
[L2123] [01:12:27.12] to make any implausible programs,
[L2124] [01:12:28.64] programs that really shouldn't run. You
[L2125] [01:12:29.96] want to make them not run right away.
[L2126] [01:12:31.60] Yeah.
[L2127] [01:12:32.56] >> If there's a slider on, I guess, the
[L2128] [01:12:34.68] strength of a type system, and you know,
[L2129] [01:12:37.68] the other side is weak. What what do you
[L2130] [01:12:39.56] see as the absolute strongest type
[L2131] [01:12:41.48] systems among programming languages?
[L2132] [01:12:43.68] >> Oh, Haskells, I think.
[L2133] [01:12:45.28] Haskell is exploring the bleeding edge.
[L2134] [01:12:48.28] There's an exception, which is that
[L2135] [01:12:49.80] module systems
[L2136] [01:12:52.12] are a um
[L2137] [01:12:54.40] and in particular sort of a functor
[L2138] [01:12:56.12] style module systems are explored much
[L2139] [01:12:59.36] more deeply in um the ML OCaml world.
[L2140] [01:13:04.08] And in the Haskell world we've
[L2141] [01:13:05.44] essentially never gone there. But
[L2142] [01:13:07.36] otherwise I think Haskell's right up
[L2143] [01:13:08.84] there. Now, of course, a language like
[L2144] [01:13:11.04] Scala
[L2145] [01:13:12.36] um
[L2146] [01:13:13.28] is also as the Scala has almost
[L2147] [01:13:17.12] everything Haskell has. I think not
[L2148] [01:13:19.04] quite. Um but it also has subtyping and
[L2149] [01:13:22.24] object oriented type object object
[L2150] [01:13:23.72] orientation. So that's a lot more
[L2151] [01:13:25.40] complicated, a lot more complicated I
[L2152] [01:13:28.08] think.
[L2153] [01:13:29.08] um
[L2154] [01:13:30.80] And they pay a price for it. I think
[L2155] [01:13:32.96] well, you know, Martin Odetsky would
[L2156] [01:13:34.24] agree that they pay a price for it. So
[L2157] [01:13:37.16] uh in complexity it's probably more
[L2158] [01:13:39.40] complicated than Haskell's.
[L2159] [01:13:42.28] um
[L2160] [01:13:44.12] Uh and maybe in terms of power. So maybe
[L2161] [01:13:46.08] I should have said Haskell and Scala are
[L2162] [01:13:47.60] the two lead Haskell, Scala, OCaml.
[L2163] [01:13:49.96] Perhaps I'll just put them in an
[L2164] [01:13:50.84] equivalence class for now. They're not
[L2165] [01:13:52.44] strictly comparable. They all have
[L2166] [01:13:54.16] things that we we in which they're more
[L2167] [01:13:55.56] powerful than the other probably.
[L2168] [01:13:57.52] >> What do you think are, you know, the
[L2169] [01:13:58.96] important problems to solve in the
[L2170] [01:14:01.40] future of programming languages today?
[L2171] [01:14:03.00] Maybe, you know, what are the unsolved
[L2172] [01:14:05.12] problems in the domain that are top of
[L2173] [01:14:07.12] mind for you?
[L2174] [01:14:08.36] >> I think it's actually hard to identify,
[L2175] [01:14:10.08] you know, to say here's a problem we
[L2176] [01:14:11.72] ought to solve, let's try to solve it.
[L2177] [01:14:13.16] But I think
[L2178] [01:14:14.56] another way to tackle is to say what are
[L2179] [01:14:16.60] interesting, you know, new languages out
[L2180] [01:14:19.24] there that are exploring very different
[L2181] [01:14:20.80] parts of the design space. And there I
[L2182] [01:14:22.68] think I do I do have a a candidate. So
[L2183] [01:14:25.20] um the language that is my day job,
[L2184] [01:14:27.24] right? I work for Epic and we're
[L2185] [01:14:28.84] designing a a programming language
[L2186] [01:14:30.16] called Verse.
[L2187] [01:14:32.04] Now Verse is a very exotic language.
[L2188] [01:14:34.28] It's it's really uh a functional logic
[L2189] [01:14:37.56] language. Um
[L2190] [01:14:39.16] So it's yet more expressive than
[L2191] [01:14:40.56] Haskell. It has a static type system but
[L2192] [01:14:42.16] a very different one to Haskell's. So if
[L2193] [01:14:44.80] you like uh the way I think of it is
[L2194] [01:14:46.20] like this. If you look at
[L2195] [01:14:48.00] um
[L2196] [01:14:48.88] uh C and Fortran, they look pretty
[L2197] [01:14:50.52] different if you're an imperative
[L2198] [01:14:52.08] programmer. But if you look at them, if
[L2199] [01:14:53.92] you zoom out so you can see functional
[L2200] [01:14:56.12] languages, then C and Fortran are pretty
[L2201] [01:14:57.72] close together.
[L2202] [01:14:59.24] Um you know, along with object-oriented
[L2203] [01:15:01.20] languages, they're all in a clump,
[L2204] [01:15:02.24] right? And then there's some functional
[L2205] [01:15:03.96] languages, you know, Haskell and ML and
[L2206] [01:15:05.28] OCaml and Scala out here. If you zoom
[L2207] [01:15:07.44] out still further,
[L2208] [01:15:09.04] then um the imperative languages and
[L2209] [01:15:11.24] functional languages are all together,
[L2210] [01:15:12.32] and Verse is way out here.
[L2211] [01:15:15.04] Right? So Verse is exploring a very new
[L2212] [01:15:17.52] point in the design space.
[L2213] [01:15:19.36] But just like functional programming
[L2214] [01:15:21.20] back in 1980,
[L2215] [01:15:23.48] it seems sufficiently interesting and
[L2216] [01:15:25.04] cool and unusual and weird that it's
[L2217] [01:15:27.04] worth exploring, right? So back in 1980,
[L2218] [01:15:30.96] nobody would said, "We're definitely
[L2219] [01:15:32.52] going to do functional programming, and
[L2220] [01:15:33.68] it's going to be useful for practical
[L2221] [01:15:34.68] applications." They said, "That's pretty
[L2222] [01:15:35.72] weird." Uh you know, by all means give
[L2223] [01:15:37.36] it a try, guys. And that's kind of where
[L2224] [01:15:38.96] I'm with Verse. Um Uh one difference is
[L2225] [01:15:41.48] that back in 1980, we were purely
[L2226] [01:15:43.00] academics. And now but Verse is being
[L2227] [01:15:45.12] developed by well, Epic Games.
[L2228] [01:15:47.52] Um so we've got some, you know, much
[L2229] [01:15:49.08] more muscle behind it um than um
[L2230] [01:15:52.28] uh you know, was behind functional
[L2231] [01:15:53.36] programming to begin with. So we'll see.
[L2232] [01:15:54.88] It's a very interesting intellectual
[L2233] [01:15:56.40] endeavor.
[L2234] [01:15:57.80] Adventure, I should say.
[L2235] [01:16:00.08] >> Yeah, I think a lot of people, like
[L2236] [01:16:01.40] students, they may be worried about AI
[L2237] [01:16:04.00] or you know, studying computer science.
[L2238] [01:16:06.28] Would you recommend people learn how to
[L2239] [01:16:09.12] program today given that AI is uh
[L2240] [01:16:12.00] starting to write reasonable code now?
[L2241] [01:16:13.88] >> Oh, yeah. Yeah. So I think people are
[L2242] [01:16:16.16] right to be worried in the sense that I
[L2243] [01:16:17.32] think there's going to be considerable
[L2244] [01:16:18.88] dislocation.
[L2245] [01:16:20.64] Right?
[L2246] [01:16:21.76] It's like, you know,
[L2247] [01:16:22.88] if you were in the industrial
[L2248] [01:16:23.84] revolution, then lots of people lost
[L2249] [01:16:25.52] their jobs as, you know, spinners and
[L2250] [01:16:27.32] weavers. Um
[L2251] [01:16:29.00] and it wasn't easy for them to get a new
[L2252] [01:16:30.48] job in the new economy. Now, the new
[L2253] [01:16:31.88] economy had in the end had more jobs,
[L2254] [01:16:34.36] but
[L2255] [01:16:35.44] there was if you were one of the people
[L2256] [01:16:37.08] who just lost their job, that was not a
[L2257] [01:16:38.32] happy place to be.
[L2258] [01:16:39.96] From our perspective, you know, Olympian
[L2259] [01:16:41.44] perspective of a few hundred years
[L2260] [01:16:42.88] later, we think, well, it's just a blip,
[L2261] [01:16:44.64] right? If you're part of the blip,
[L2262] [01:16:46.76] problem, right? So, I think they're
[L2263] [01:16:49.16] right to be worried.
[L2264] [01:16:51.80] Um we don't know how things will shake
[L2265] [01:16:53.68] out. I'm actually optimistic that in the
[L2266] [01:16:56.20] medium term, if we don't, you know,
[L2267] [01:16:57.36] destroy ourselves with some truly
[L2268] [01:16:59.20] existential thing, but from an
[L2269] [01:17:00.64] employment market point of view, I'm
[L2270] [01:17:02.36] optimistic that in the end, you know,
[L2271] [01:17:04.44] we'll just be in a higher place that AIs
[L2272] [01:17:06.84] will just be a
[L2273] [01:17:08.72] a bigger power tool. I mean,
[L2274] [01:17:10.84] everyone, we like using compilers,
[L2275] [01:17:12.48] right? We don't like machine code
[L2276] [01:17:13.48] anymore. Compilers make us more
[L2277] [01:17:14.96] productive. Maybe LLMs can make us more
[L2278] [01:17:17.24] productive. That's what I hope. I sort
[L2279] [01:17:19.36] of believe modulo dislocation effects.
[L2280] [01:17:22.52] Now,
[L2281] [01:17:24.36] um
[L2282] [01:17:25.84] should we
[L2283] [01:17:27.44] teach children or even undergraduates
[L2284] [01:17:29.76] how to program? So, I think still yes.
[L2285] [01:17:32.76] Um
[L2286] [01:17:33.48] um the reason is because
[L2287] [01:17:36.20] um
[L2288] [01:17:37.32] uh like one way to say it is co-pilots
[L2289] [01:17:40.04] need pilots.
[L2290] [01:17:42.40] Right? I think co-pilot is quite a good
[L2291] [01:17:43.84] title that Microsoft gave their tools,
[L2292] [01:17:46.24] right? Because it encourages you to
[L2293] [01:17:47.88] believe it's your partner, not your
[L2294] [01:17:49.20] boss.
[L2295] [01:17:50.36] Um
[L2296] [01:17:51.20] if LLMs spit out a pile of goop, and we
[L2297] [01:17:54.08] literally do not understand what it
[L2298] [01:17:55.52] does, we just try it and it kind of
[L2299] [01:17:56.72] works,
[L2300] [01:17:57.92] that might be okay if we're just
[L2301] [01:17:59.00] throwing up a quick visualization. It
[L2302] [01:18:00.92] might be less okay if the quick
[L2303] [01:18:02.40] visualization is going to drive our
[L2304] [01:18:03.80] policy um choices about as a nation
[L2305] [01:18:06.72] whether to go into lockdown because of
[L2306] [01:18:08.04] COVID, um or if this program is going to
[L2307] [01:18:11.56] run my airplane or train signaling
[L2308] [01:18:13.56] system.
[L2309] [01:18:15.32] So, now those are, you know, extreme
[L2310] [01:18:17.32] ends of the spectrum, you know, from
[L2311] [01:18:19.16] quick and dirty things it really doesn't
[L2312] [01:18:20.68] matter if it doesn't work, uh
[L2313] [01:18:22.84] but it kind of does a lot of the time,
[L2314] [01:18:24.56] absolutely fine, to
[L2315] [01:18:27.12] this is a 30-year code base, it's going
[L2316] [01:18:28.84] to last a long time. I really want to
[L2317] [01:18:30.56] make sure that it like putting new stuff
[L2318] [01:18:32.52] into GHC. If somebody sends me a pile of
[L2319] [01:18:34.72] AI-generated code to put into GHC, I'm
[L2320] [01:18:36.60] not going to put it in. Unless I've
[L2321] [01:18:38.24] reviewed it, or somebody's reviewed it,
[L2322] [01:18:40.00] because in 10 years time, I'm going to
[L2323] [01:18:42.24] want to change that code. How do I even
[L2324] [01:18:43.60] know what it does? If it's simply a
[L2325] [01:18:45.28] magic incantation that somebody's done
[L2326] [01:18:46.92] that kind of worked on the test they
[L2327] [01:18:48.52] did, but maybe won't work in deployment,
[L2328] [01:18:50.44] that's no good. So,
[L2329] [01:18:52.12] I really want
[L2330] [01:18:53.84] uh long-lived maintainable code to be
[L2331] [01:18:55.96] well reviewed. Sorry. Um so, and to do
[L2332] [01:18:58.52] that, I need reviewers who can write
[L2333] [01:19:00.08] code, who know
[L2334] [01:19:01.36] Um let me mention one other
[L2335] [01:19:03.84] perspective. Um
[L2336] [01:19:06.04] If you think about what every child
[L2337] [01:19:07.64] should know,
[L2338] [01:19:09.44] um
[L2339] [01:19:10.28] when I um
[L2340] [01:19:12.24] uh think about whatever a child should
[L2341] [01:19:14.00] know about computing, I would include
[L2342] [01:19:16.12] binary and bits.
[L2343] [01:19:19.08] Not Oh, just as for physics, I would
[L2344] [01:19:21.12] include atoms and molecules.
[L2345] [01:19:23.84] Now, it's not that in real life anybody
[L2346] [01:19:25.64] manipulates atoms or molecules, or takes
[L2347] [01:19:27.92] decisions which are based directly on
[L2348] [01:19:30.08] their knowledge of atom knowledge, but
[L2349] [01:19:31.64] somehow knowledge that all matter is
[L2350] [01:19:33.84] made up of atoms.
[L2351] [01:19:35.64] You know, constituted of a finite number
[L2352] [01:19:37.20] of elements that atoms could block
[L2353] [01:19:38.28] together with. That knowledge underpins
[L2354] [01:19:40.68] everything we understand about the
[L2355] [01:19:41.88] natural world. If you literally have
[L2356] [01:19:43.76] never been told that,
[L2357] [01:19:46.48] you are sort of emasculated
[L2358] [01:19:48.68] as a even as a citizen, let alone as a
[L2359] [01:19:50.88] scientist. So,
[L2360] [01:19:52.56] if you literally do not know that
[L2361] [01:19:54.32] everything is composed of bits, that
[L2362] [01:19:55.72] words and music and text and LLMs and
[L2363] [01:19:58.44] everything's all just bits,
[L2364] [01:20:00.32] I think you're crippled.
[L2365] [01:20:01.92] So, I want every child to learn uh you
[L2366] [01:20:04.48] know, it's like I want you to learn the
[L2367] [01:20:05.56] bottom that they It's It's all bits,
[L2368] [01:20:08.04] nothing else. It's all just bits.
[L2369] [01:20:11.40] I give a talk. The talk is called Bits
[L2370] [01:20:14.16] with Soul.
[L2371] [01:20:17.00] Um they're easy to grab for. It's a talk
[L2372] [01:20:19.36] I gave to an audience that was not
[L2373] [01:20:20.88] computer science audience at all. It was
[L2374] [01:20:22.48] a completely lay audience, ranging from
[L2375] [01:20:24.36] 14-year-olds to professors of quantum
[L2376] [01:20:26.04] mechanics. Pretty difficult audience to
[L2377] [01:20:28.76] address. Um and it was meant to be about
[L2378] [01:20:30.72] um
[L2379] [01:20:31.68] all about uh codes and coding and bits.
[L2380] [01:20:33.80] So, um,
[L2381] [01:20:35.12] and so it tries to get at the essence of
[L2382] [01:20:37.76] why why do I think it's important that
[L2383] [01:20:39.68] every every child, every person, every
[L2384] [01:20:41.84] human being should understand something
[L2385] [01:20:44.00] about the computational universe that
[L2386] [01:20:45.40] surrounds them. And that's founded in
[L2387] [01:20:46.60] bits. Now, just to to develop the
[L2388] [01:20:48.44] analogy a bit further, I would then say,
[L2389] [01:20:49.72] "And it also, I think I want them to
[L2390] [01:20:52.28] also know about programming programs. I
[L2391] [01:20:55.32] want them to know that computers
[L2392] [01:20:56.72] fundamentally execute by following
[L2393] [01:20:58.40] machine instructions blindly. Right?
[L2394] [01:21:00.68] There is not magic. It's not hocus
[L2395] [01:21:02.36] pocus. It's just remorseless and very
[L2396] [01:21:05.84] dumb.
[L2397] [01:21:07.04] Right? It's incredibly empowering then.
[L2398] [01:21:09.52] Um,
[L2399] [01:21:10.32] and also to learn the basics about how
[L2400] [01:21:12.04] neural networks work. In the same talk,
[L2401] [01:21:14.56] I explain how a a one neuron neural
[L2402] [01:21:17.20] network works.
[L2403] [01:21:18.60] Um,
[L2404] [01:21:19.56] and that's enough. Uh, then then it's
[L2405] [01:21:21.60] actually true to say, not distorting the
[L2406] [01:21:23.56] facts to say, "Chat GPT is just a
[L2407] [01:21:25.28] trillion of those
[L2408] [01:21:27.36] wired together."
[L2409] [01:21:28.72] Um, and astonishingly, that very simple
[L2410] [01:21:31.76] So, so all Chat GPT is is
[L2411] [01:21:34.44] a trillion floating point numbers and a
[L2412] [01:21:36.08] lot of floating point arithmetic.
[L2413] [01:21:38.28] That helps you to make sense of a
[L2414] [01:21:40.12] question like,
[L2415] [01:21:42.12] "Can Chat GPT have feelings?"
[L2416] [01:21:47.28] Well,
[L2417] [01:21:48.64] it gives you
[L2418] [01:21:49.96] a I mean, of course that's a
[L2419] [01:21:51.00] philosophical question, but informs
[L2420] [01:21:53.08] your, you know, your discussion about it
[L2421] [01:21:54.92] if you know that all it is
[L2422] [01:21:57.36] is trillion floats and a lot of floating
[L2423] [01:21:59.48] point arithmetic. That's all. Nothing
[L2424] [01:22:01.44] more.
[L2425] [01:22:03.04] Anyway, sorry, long answer to your
[L2426] [01:22:04.04] question. But, so I I So, yes, basic
[L2427] [01:22:06.80] programming, absolutely. Yeah. Becoming
[L2428] [01:22:09.28] very skilled in how to use, you know,
[L2429] [01:22:12.72] web Django framework 2.7, maybe not so
[L2430] [01:22:16.32] much.
[L2431] [01:22:17.80] Maybe. I think one thing that LLMs are
[L2432] [01:22:19.40] very good at is knowing the arcane and
[L2433] [01:22:22.72] complicated APIs that many of these
[L2434] [01:22:25.48] frameworks present. When you There's
[L2435] [01:22:27.48] just, you know, 10,000 functions you've
[L2436] [01:22:29.08] got to know, and if an LLM's really good
[L2437] [01:22:32.00] at knowing that, I don't want to learn
[L2438] [01:22:33.36] them.
[L2439] [01:22:34.24] >> You mentioned somewhere someone asked
[L2440] [01:22:36.00] you, you know, what's your favorite
[L2441] [01:22:37.20] programming language? And obviously
[L2442] [01:22:38.76] Haskell's got to be number one.
[L2443] [01:22:40.20] >> Yeah.
[L2444] [01:22:40.76] >> But for your second favorite programming
[L2445] [01:22:42.96] language, you said it was Excel.
[L2446] [01:22:45.48] At that time, why was Excel your
[L2447] [01:22:47.80] favorite programming language?
[L2448] [01:22:49.24] >> Oh, because it's the world's most widely
[L2449] [01:22:51.04] used functional programming language.
[L2450] [01:22:52.80] The formula language is a functional
[L2451] [01:22:54.36] language, isn't it?
[L2452] [01:22:56.28] Doesn't have any side effects. You
[L2453] [01:22:58.04] program entirely with values.
[L2454] [01:22:59.92] So, the formula language of Excel is
[L2455] [01:23:03.44] a functional programming language, a
[L2456] [01:23:05.60] very weak one.
[L2457] [01:23:08.08] It doesn't even let you define new
[L2458] [01:23:09.48] functions.
[L2459] [01:23:10.72] And it has a very limited collection of
[L2460] [01:23:12.12] data types,
[L2461] [01:23:13.68] namely just, you know, flat arrays and
[L2462] [01:23:15.52] numbers and strings.
[L2463] [01:23:17.48] So,
[L2464] [01:23:19.00] when I was working for Microsoft, I took
[L2465] [01:23:20.56] it as my
[L2466] [01:23:21.96] uh my uh what's the word? Uh
[L2467] [01:23:24.40] um war cry to say, "Let's take that
[L2468] [01:23:27.44] idea. Excel is the world's most widely
[L2469] [01:23:29.80] used functional language by three orders
[L2470] [01:23:32.12] of magnitude."
[L2471] [01:23:35.12] And oh, not it's the world's most widely
[L2472] [01:23:37.84] used programming language by three
[L2473] [01:23:39.16] orders of magnitude, not just functional
[L2474] [01:23:40.68] language.
[L2475] [01:23:42.04] Excel is used by many, many more
[L2476] [01:23:44.04] programmers, users, domain experts than
[L2477] [01:23:47.80] any any imperative language.
[L2478] [01:23:51.40] Right?
[L2479] [01:23:52.60] Imperative language has a few million
[L2480] [01:23:53.92] users.
[L2481] [01:23:55.84] Excel, hundreds of millions of users,
[L2482] [01:23:58.48] right?
[L2483] [01:23:59.84] Even if you just restricted users who
[L2484] [01:24:01.36] are using formulae.
[L2485] [01:24:03.96] So, how can we delight those users?
[L2486] [01:24:05.88] Answer, take ideas from functional
[L2487] [01:24:07.92] programming and use them to make Excel's
[L2488] [01:24:10.80] formula language more powerful.
[L2489] [01:24:13.80] It took me 20 years, but Excel did
[L2490] [01:24:16.72] finally add lambda to Excel.
[L2491] [01:24:20.12] Look it up. There are blog posts about
[L2492] [01:24:22.16] it and and many YouTube videos about it.
[L2493] [01:24:25.00] So, you can now program in Excel using
[L2494] [01:24:27.20] full lambda as Alonzo Church originally
[L2495] [01:24:29.84] defined it.
[L2496] [01:24:31.92] You can write anything like because it
[L2497] [01:24:34.76] lambda is computationally complete. You
[L2498] [01:24:36.52] can write any computation in Excel now.
[L2499] [01:24:38.88] It would be a bit slow, but you can.
[L2500] [01:24:41.20] And much more practically, you can take
[L2501] [01:24:44.92] formulae that previously you just copy
[L2502] [01:24:46.72] pasted here and there
[L2503] [01:24:48.88] and you wanted to make reusable, wrap
[L2504] [01:24:50.72] them up in a lambda and now you can just
[L2505] [01:24:52.08] call the lambda.
[L2506] [01:24:53.56] And now, it is a proper grown-up
[L2507] [01:24:56.28] functional language that is Turing
[L2508] [01:24:57.64] complete.
[L2509] [01:24:59.80] Just search for lambda Excel. Those two
[L2510] [01:25:02.00] keywords will get you lots of raw
[L2511] [01:25:03.24] material.
[L2512] [01:25:04.52] >> Last question for you is knowing
[L2513] [01:25:06.44] everything that you know now from your
[L2514] [01:25:08.08] career, if you could go back to when you
[L2515] [01:25:10.32] just graduated from college and give
[L2516] [01:25:12.52] yourself some advice, what would you
[L2517] [01:25:13.96] say?
[L2518] [01:25:15.00] >> All of these people who you see very
[L2519] [01:25:17.80] successful wandering around looking as
[L2520] [01:25:19.60] if they made it. I guess you might class
[L2521] [01:25:22.16] me among them now. Um Uh
[L2522] [01:25:24.60] they are all of them just making it up
[L2523] [01:25:27.12] as they go along.
[L2524] [01:25:28.56] They feel insecure, uncertain, not sure
[L2525] [01:25:31.44] what to do next, um not sure of what
[L2526] [01:25:33.92] their next steps are, not sure of what
[L2527] [01:25:35.56] next problem they're going to tackle,
[L2528] [01:25:37.52] unsure about whether they what they're
[L2529] [01:25:38.68] doing is going to be successful or not.
[L2530] [01:25:40.36] Um and so, all of their confidence is I
[L2531] [01:25:43.12] mean they project confidence maybe.
[L2532] [01:25:44.88] That's partly a life skill. Um
[L2533] [01:25:46.96] but often they're not. Um
[L2534] [01:25:49.12] and so, the fact that, you know, in my
[L2535] [01:25:51.52] in those days, of course, I felt very
[L2536] [01:25:52.84] not confident. I would say, you know,
[L2537] [01:25:55.88] since all of these um successful people
[L2538] [01:25:58.88] are making it up as they go along, it
[L2539] [01:26:00.44] it's fine for you to be as well.
[L2540] [01:26:02.40] Um
[L2541] [01:26:03.40] And they've been lucky, moreover.
[L2542] [01:26:05.56] They've been lucky. Uh they've had some
[L2543] [01:26:08.36] uh
[L2544] [01:26:09.08] but if you want to be lucky,
[L2545] [01:26:11.00] you do need to put yourself in a
[L2546] [01:26:12.28] position where uh
[L2547] [01:26:14.52] accidents can happen to you.
[L2548] [01:26:18.04] And that means taking risks. So, if you
[L2549] [01:26:20.48] want to be lucky, you need to be in a
[L2550] [01:26:22.60] put yourself in positions where lucky
[L2551] [01:26:25.48] things could happen.
[L2552] [01:26:27.12] Right. Um and that means taking some
[L2553] [01:26:29.44] kind of risk. So, if you're very
[L2554] [01:26:30.56] conservative and have to take any risk,
[L2555] [01:26:31.88] then it's very unlikely that the
[L2556] [01:26:33.40] accident that is life-transforming will
[L2557] [01:26:34.92] happen. That's a balance, of course. Um
[L2558] [01:26:38.04] but it means that accidents are not so
[L2559] [01:26:39.24] bad. And of course,
[L2560] [01:26:40.76] um dying is bad, but
[L2561] [01:26:42.84] lots of accidents may change your life
[L2562] [01:26:44.28] in in in a way that might be surprising
[L2563] [01:26:46.60] to you, but turns out to be not so bad
[L2564] [01:26:48.40] in when retrospect.
[L2565] [01:26:50.16] >> Awesome. Well, yeah, thank you so much
[L2566] [01:26:51.72] for your time. I really appreciate it,
[L2567] [01:26:53.20] Professor Jones.
[L2568] [01:26:54.24] >> We will let you know if that's okay with
[L2569] [01:26:55.08] you. Uh thanks. Bye.
[L2570] [01:26:56.64] >> Hey, thank you for watching this
[L2571] [01:26:57.64] podcast. If you liked it and you want to
[L2572] [01:26:59.28] see the show grow, please support with a
[L2573] [01:27:01.48] comment or a like.
[L2574] [01:27:03.48] Also, if you have any recommendations
[L2575] [01:27:05.28] for people you want me to bring on,
[L2576] [01:27:07.28] please drop a comment. Guests like
[L2577] [01:27:09.48] Barbara Liskov, Mike Stonebreaker, Mark
[L2578] [01:27:12.20] Brooker, these were all people that I
[L2579] [01:27:14.24] brought on because someone left a
[L2580] [01:27:16.08] comment. On another note, aside from the
[L2581] [01:27:18.36] podcast, I'm working on building the
[L2582] [01:27:20.16] ergonomic keyboard that I wish existed.
[L2583] [01:27:22.64] Here's a glance at the prototype. It's a
[L2584] [01:27:24.48] split keyboard, so there's two sides. Um
[L2585] [01:27:27.52] this is in the case. But yeah, we
[L2586] [01:27:29.00] launched on Kickstarter and we hit our
[L2587] [01:27:30.80] goal within 8 hours of launching. I
[L2588] [01:27:32.88] really appreciate it if you were one of
[L2589] [01:27:34.28] the people who grabbed one of the early
[L2590] [01:27:36.04] units. Um we're now working on the long
[L2591] [01:27:38.36] journey of building the tooling now. And
[L2592] [01:27:40.48] so, if you still want to pick one up,
[L2593] [01:27:42.16] I've left the late pledges open on
[L2594] [01:27:44.16] Kickstarter, so you can grab one there.
[L2595] [01:27:46.36] I'll put a link in the description.
[L2596] [01:27:48.32] Thank you again for watching the
[L2597] [01:27:49.88] podcast, and I'll see you in the next
[L2598] [01:27:52.08] episode.
