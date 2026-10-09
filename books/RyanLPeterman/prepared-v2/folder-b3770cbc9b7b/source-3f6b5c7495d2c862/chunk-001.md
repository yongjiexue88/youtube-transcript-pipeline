Chunk 1; segments 1–413. 

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
