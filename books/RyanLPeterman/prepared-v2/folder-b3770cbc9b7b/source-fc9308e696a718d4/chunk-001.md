Chunk 1; segments 1–361. 

# Turing Award Winner: TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC | David Patterson

Source ID: source-fc9308e696a718d4
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_TPU_vs_GPU_vs_CPU,_Computer_Architecture,_RISC_vs_CISC_David_Patterson_en.txt
Video: https://www.youtube.com/watch?v=Pn4ZwlEh5nw

[L10] [00:00.08] Well, if Moore's law puts a lot more
[L11] [00:01.92] transistors in a chip, how come they're
[L12] [00:03.60] not getting hotter and hotter?
[L13] [00:05.36] >> This is David Patterson, Turing [music]
[L14] [00:07.28] award winner, famous for his
[L15] [00:08.72] contributions to computer architecture.
[L16] [00:10.80] And we discussed the historic risk
[L17] [00:12.80] versus CISK debate
[L18] [00:14.16] >> and he said and CISK won. Well, that's a
[L19] [00:16.56] pretty myopic view. Everything is energy
[L20] [00:19.60] bound now. Register [snorts] allocation
[L21] [00:22.00] by the [music] compilers was so poor
[L22] [00:24.48] >> and his thoughts on modern GPU and TPU
[L23] [00:27.12] architecture. What's the highle
[L24] [00:29.28] differences between a CPU, [music]
[L25] [00:31.36] a GPU, and a TPU?
[L26] [00:33.28] >> What they realize for machine learning
[L27] [00:34.96] and AI?
[L28] [00:36.64] >> Here's the full episode.
[L29] [00:42.32] Maybe you could explain risk versus CISK
[L30] [00:45.28] kind of like what that debate was and
[L31] [00:47.36] why was it controversial.
[L32] [00:49.60] What happened is in kind of in you know
[L33] [00:52.40] the microprocessor was invented in the
[L34] [00:54.96] 1970s and but in the beginning it was
[L35] [00:57.20] basically a toy. It'd be something that
[L36] [00:58.80] would go in microwaves and things like
[L37] [01:00.48] that. Those of us who believed in
[L38] [01:02.48] Moore's law believed eventually the uh
[L39] [01:05.76] microprocessor would be the way we did
[L40] [01:07.84] all our computing with the doubling of
[L41] [01:09.68] transistors every year or two.
[L42] [01:11.84] eventually there'd be enough transistors
[L43] [01:14.08] that on one of these microprocessors
[L44] [01:15.76] would be a serious computer.
[L45] [01:19.04] So the people who were designing
[L46] [01:20.80] microprocessors like in Intel and Texas
[L47] [01:23.52] Instruments weren't really computer
[L48] [01:25.52] architects. So they just imitated what
[L49] [01:27.60] the big companies did. So companies
[L50] [01:29.84] leading companies like IBM or at the
[L51] [01:32.56] time digital equipment corporation uh
[L52] [01:34.72] IBM for mainframes digital equipment for
[L53] [01:36.72] what were called minicomp computers they
[L54] [01:38.48] kind of drove the uh architecture the
[L55] [01:41.12] instruction set design. So what they
[L56] [01:43.76] were doing with Morris law was building
[L57] [01:46.08] more and more sophisticated
[L58] [01:48.16] u instructions. They had they had you
[L59] [01:50.80] know mini computers be the size of a a
[L60] [01:53.76] refrigerator or a couple of
[L61] [01:54.88] refrigerators and mainframes would be
[L62] [01:56.96] the size of many of those. So that's
[L63] [01:59.20] what they were doing with more hard
[L64] [02:00.40] sources. And the philosophy at the time
[L65] [02:03.28] was that by having a more sophisticated
[L66] [02:06.32] instruction set you kind of raise the
[L67] [02:08.56] level of abstraction closer to the
[L68] [02:10.24] software. So that had some inherent
[L69] [02:12.40] benefits over having something at a
[L70] [02:15.04] lower level. Now from a c some of us uh
[L71] [02:19.68] who were in that area like my friend
[L72] [02:22.72] John Hennessy at Stanford and I we
[L73] [02:25.52] thought that wasn't necessarily the
[L74] [02:27.52] right thing to do. Compilers would go
[L75] [02:29.60] from programming languages down to the
[L76] [02:31.68] instruction set. So why couldn't
[L77] [02:33.04] compilers hold that? And then the
[L78] [02:34.88] question is what's the right instruction
[L79] [02:36.24] set for this emerging microprocessor?
[L80] [02:39.52] And the prevailing wisdom of these more
[L81] [02:41.76] sophisticated instruction sets, complex
[L82] [02:44.08] instruction sets. And if you think of it
[L83] [02:45.92] like a vocabulary, it was like a having
[L84] [02:49.36] lots of polyelabic words in your
[L85] [02:51.12] vocabulary, you know. And the
[L86] [02:53.52] alternative was going to be what we
[L87] [02:55.60] called the reduced instruction set
[L88] [02:57.12] computer was having lots of reduced
[L89] [02:59.28] instructions like monoselabic words. So
[L90] [03:01.92] you might guess that for a program to
[L91] [03:05.12] execute these instructions, if they're
[L92] [03:06.64] simpler, they take more of them and if
[L93] [03:09.60] they're sophisticated, they take fewer,
[L94] [03:11.68] but the sophisticated ones might take
[L95] [03:13.36] longer to run. So kind of the question
[L96] [03:16.24] came down to what was that ratio? Um,
[L97] [03:18.96] and in the in the beginning in the 1980s
[L98] [03:21.76] when these debates were happening, there
[L99] [03:23.20] was this kind of very viciferous debates
[L100] [03:26.16] partly of like what those ratios are
[L101] [03:27.76] going to do, but a big part was kind of
[L102] [03:29.36] philosophical. Weren't weren't you doing
[L103] [03:32.00] damage to the software industry by
[L104] [03:34.48] lowering the instruction set level? So
[L105] [03:36.40] the gap between the programming
[L106] [03:38.08] languages and the instruction set was
[L107] [03:40.24] larger. That was kind of the ferocity of
[L108] [03:42.48] the debates. Well, after the dust
[L109] [03:44.48] settled a few years later and we started
[L110] [03:46.16] getting numbers, it turned out you
[L111] [03:48.24] needed like maybe 30% 40% more simple
[L112] [03:51.68] instructions to execute in a program,
[L113] [03:54.32] but you could run them four or five
[L114] [03:56.00] times faster. So the net was, you know,
[L115] [03:58.48] or five times faster say. So 3 or 4x
[L116] [04:01.04] speed up was the potential for risk over
[L117] [04:04.16] CISK.
[L118] [04:05.60] >> You mentioned that um I guess
[L119] [04:07.52] philosophical difference like that gap.
[L120] [04:10.08] Why why would that be controversial?
[L121] [04:12.40] >> I mean unfortunately I'd say computer
[L122] [04:14.80] architecture in the 1970s and even 1980s
[L123] [04:18.72] a lot of it was uh was kind of people
[L124] [04:22.96] designed this by using their intuition
[L125] [04:25.28] or using their gut. Their feelings was
[L126] [04:27.36] this is the right thing to do. And even
[L127] [04:30.40] the textbooks of the time were like
[L128] [04:32.72] cataloges. They here's a computer and
[L129] [04:34.64] just list all its features and here's
[L130] [04:36.16] another computer listing all its
[L131] [04:37.84] features. So it's pretty dissatisfying
[L132] [04:40.96] what was going on because these debates
[L133] [04:43.52] it would seem like we ought to be able
[L134] [04:44.88] to sign this, you know, scientifically
[L135] [04:46.72] with with numbers that are there. But
[L136] [04:49.76] absence of that, it was more like a
[L137] [04:51.68] philosophical debate like how many
[L138] [04:53.52] angels on the head of a pin, right? You
[L139] [04:55.12] could you could have arguments
[L140] [04:57.04] qualitatively but you couldn't settle
[L141] [04:59.12] the arguments and because there wasn't
[L142] [05:01.84] ways to settle the arguments
[L143] [05:03.20] quantitatively you know people would
[L144] [05:05.20] just argue about it. Would you say that
[L145] [05:08.24] you know risk versus cisk did one side
[L146] [05:12.08] win the war? Yeah. I was just reading
[L147] [05:14.40] there's some guy online who uh revisited
[L148] [05:17.52] it and he said and CISK won. Well,
[L149] [05:19.76] that's a pretty myopic view is uh in the
[L150] [05:23.28] PC era because of the importance of u
[L151] [05:27.36] distributing software in binary. So once
[L152] [05:30.08] the x86 was established and people the
[L153] [05:32.64] PCs would would ship software in
[L154] [05:34.88] binaries that was very hard to overcome.
[L155] [05:36.88] That was a huge uh impediment to
[L156] [05:39.44] changing the instruction set. So PCs are
[L157] [05:42.00] design defined by the x86 architecture
[L158] [05:44.56] largely.
[L159] [05:46.64] But about also in the 1980s there's this
[L160] [05:50.00] company in England u that wanted to do a
[L161] [05:52.48] personal computer they call it was the
[L162] [05:53.92] acorn personal computer and they decided
[L163] [05:56.80] they wanted to have their own they
[L164] [05:58.24] needed their own instruction set
[L165] [05:59.52] architecture to do that their own chip
[L166] [06:00.88] they were unsatis the chips they had
[L167] [06:02.72] available at the time they were doing it
[L168] [06:04.64] weren't fast enough and they were
[L169] [06:07.36] influenced by the papers that we did at
[L170] [06:09.04] Berkeley and so they built what they
[L171] [06:10.80] called the acorn risk machine
[L172] [06:13.52] and then uh one of the benefits of this
[L173] [06:16.32] kind of reduced instruction set is that
[L174] [06:18.16] it could be simpler, it would take less
[L175] [06:20.24] resources and take less energy to
[L176] [06:22.40] execute. And then several years later
[L177] [06:25.04] when Apple was looking for a
[L178] [06:26.56] microprocessor that could power, you
[L179] [06:29.28] know, one of their personal devices that
[L180] [06:31.68] this one was called the early forerunner
[L181] [06:33.84] of the iPhone called the Newton. They
[L182] [06:36.16] came to this company and said, "Boy, I
[L183] [06:38.72] really like it. Uh, let's get rid of the
[L184] [06:41.12] Acorn name." So they renamed it the
[L185] [06:43.52] acorn wrist machine arm and they
[L186] [06:46.72] recristened it the advanced wrist
[L187] [06:48.40] machine uh because to get rid of the
[L188] [06:50.48] acorn and then Apple used it um in the
[L189] [06:53.92] Newton. Now the new wasn't a commercial
[L190] [06:55.92] success but it demonstrated the benefits
[L191] [06:58.56] for risk architecture for mobile
[L192] [07:00.16] devices. So the Nokia came along just a
[L193] [07:03.20] few years later with their GDM uh
[L194] [07:06.64] cellular phone which is one of the first
[L195] [07:08.16] popular ones and they embraced ARM. And
[L196] [07:10.96] so ever since you know uh ARM has
[L197] [07:13.36] dominated all the mobile devices. So I
[L198] [07:16.32] think I just checked there's been 350
[L199] [07:18.88] billion
[L200] [07:20.48] uh ARM processors microprocessors with
[L201] [07:23.12] ARM technology in it today. So it's like
[L202] [07:25.68] today 99% of all processors in computers
[L203] [07:29.20] are risk
[L204] [07:31.44] even in personal computers. Apple
[L205] [07:33.44] switched over to ARM from from the x86
[L206] [07:37.04] architecture. So even PCs there's um
[L207] [07:41.12] there's a risk architecture is you know
[L208] [07:43.84] is significant and it's trying to
[L209] [07:46.40] starting to get in the cloud. The
[L210] [07:47.52] cloud's largely been defined by the x86
[L211] [07:49.68] server architectures but um Amazon and I
[L212] [07:54.32] think Amazon, Microsoft and Google all
[L213] [07:56.16] have their own development of ARM
[L214] [07:57.68] processors. So ARM is becoming or risk
[L215] [07:59.76] processor becoming more popular in the
[L216] [08:01.44] cloud. So right now you I'd say the x86
[L217] [08:05.28] architecture market is shrinking while
[L218] [08:07.92] the risk architecture market is um you
[L219] [08:10.56] know growing leaps and bounds.
[L220] [08:12.32] >> Well, how how could someone say CISK one
[L221] [08:15.12] when you mentioned like 99%
[L222] [08:17.44] >> Yeah. Well, that's just if you if if
[L223] [08:19.84] they're doing something in history and
[L224] [08:22.08] they define computers as personal
[L225] [08:25.52] computers and maybe servers and they go
[L226] [08:28.00] up through around 2000. If the story
[L227] [08:31.20] ended then you could well it looks like
[L228] [08:33.76] a CISK one but you know uh once we get
[L229] [08:36.96] into this uh postPC era I don't
[L230] [08:39.52] understand how somebody would reach that
[L231] [08:41.20] conclusion. [laughter]
[L232] [08:43.44] >> You mentioned the the energy expenditure
[L233] [08:45.60] so like um you know risk makes sense in
[L234] [08:49.36] places or maybe on mobile devices things
[L235] [08:51.68] like that.
[L236] [08:52.80] >> Well even in the cloud I mean everybody
[L237] [08:54.64] cares about we're we're everything is
[L238] [08:56.48] energy bound now. So it if u you know
[L239] [09:00.32] these days of course you're not dealing
[L240] [09:02.16] with millions of transistors but
[L241] [09:03.60] billions of transistors. So it matters
[L242] [09:06.88] somewhat less today. There's so many
[L243] [09:09.28] things going going on that you can hide
[L244] [09:11.60] that. I mean even what the x86
[L245] [09:13.52] architecture did is to compete is that
[L246] [09:17.60] it translated the x86 instructions in
[L247] [09:20.40] hardware into risk instructions. And so
[L248] [09:22.72] you had to pay that extra overhead of
[L249] [09:24.64] that translation step to get risk
[L250] [09:26.40] instructions and then you could ex any
[L251] [09:28.64] good ideas that the risk people had that
[L252] [09:30.96] the x86 could do. But it was worth it
[L253] [09:34.64] financially for that extra overhead
[L254] [09:36.88] because of the value of the PC software
[L255] [09:39.92] base. So it made a lot of sense for
[L256] [09:42.00] Intel to do that and they did that in
[L257] [09:43.92] the early 2000s. It you know it was a
[L258] [09:46.96] it's a great uh commercial idea. Is
[L259] [09:50.16] there any niche use case where CISK
[L260] [09:52.80] makes sense? Is there any, you know, is
[L261] [09:54.64] this an engineering trade-off or CISK is
[L262] [09:56.88] objectively worse?
[L263] [09:57.84] >> Yeah. So, if you want to, if we want to
[L264] [09:59.20] go kind of one level deeper into all of
[L265] [10:02.08] this, um,
[L266] [10:04.24] the what was actually going on in, you
[L267] [10:07.44] know, in designing computers, the hard
[L268] [10:09.44] part is the control. And so, what
[L269] [10:12.00] happened is in the beginning, it was
[L270] [10:14.00] kind of control was kind of ad hoc. you
[L271] [10:16.64] would figure out uh you put the gates
[L272] [10:18.64] together to make it to work. Uh a uh one
[L273] [10:22.08] of the computing pioneers, Maurice
[L274] [10:23.84] Welks, figured out a more elegant way to
[L275] [10:25.92] design control. And he said, "Well, we
[L276] [10:28.64] could just list all the control signals
[L277] [10:31.04] as the output of a memory and we could
[L278] [10:34.16] have something would keep track of where
[L279] [10:36.16] we were in the memory and and to issue
[L280] [10:39.28] those control signals." And he called
[L281] [10:40.80] this he called the this effort the
[L282] [10:44.88] instruction the the control signals you
[L283] [10:47.36] could think of instructions. So he
[L284] [10:48.48] called that a micro instruction and he
[L285] [10:50.48] called the programming of those
[L286] [10:51.60] instructions microprogramming.
[L287] [10:53.92] So where technology was in the 1960s
[L288] [10:58.24] that made a fair amount of sense and so
[L289] [11:00.96] IBM built these so-called micro program
[L290] [11:04.64] computers. So it was basically an
[L291] [11:07.04] interpreter with very simple
[L292] [11:08.56] instructions that would interpret this
[L293] [11:10.88] much more sophisticated instruction set
[L294] [11:12.96] above it. But you would play this
[L295] [11:14.72] interpretation overhead. And classically
[L296] [11:17.04] you know in computer science
[L297] [11:18.40] interpreting versus compiling uh is
[L298] [11:21.04] something like a factor of five or 10.
[L299] [11:23.60] But given you know the latencies of the
[L300] [11:25.36] memory technologies and the possibility
[L301] [11:27.92] of doing this out of readonly memory it
[L302] [11:30.24] made sense u up until the 60s and 70s
[L303] [11:34.24] and then but then the kind of the
[L304] [11:35.44] question came up as came around 1980 is
[L305] [11:37.68] like is this still a good idea? Should
[L306] [11:39.60] we have this microode interpreter inside
[L307] [11:42.32] there? And so the alternative is to
[L308] [11:45.36] think of well rather than uh we've got
[L309] [11:47.84] this microode interpreter in there why
[L310] [11:49.84] don't we just compile directly into
[L311] [11:51.28] those instructions and that's pretty
[L312] [11:53.28] close to the to the risk ideas. Uh the
[L313] [11:56.88] micro instructions themselves used to be
[L314] [11:58.80] you know like a 100 bits wide and really
[L315] [12:01.36] complicated. So if you if you make them
[L316] [12:03.44] not quite so long you make them kind of
[L317] [12:06.40] more natural still we can we could skip
[L318] [12:09.36] the interpretation step. So with the you
[L319] [12:11.76] know going going this level deeper kind
[L320] [12:14.64] of the question would be today would
[L321] [12:16.16] people invent an instruction set that
[L322] [12:18.64] was so sophisticated and needed a
[L323] [12:20.40] microode interpreter and probably they
[L324] [12:22.40] wouldn't do that. I mean you could do it
[L325] [12:24.64] you nothing prevents you from doing it
[L326] [12:27.52] but you wouldn't want to design an
[L327] [12:28.88] instruction set that was forced to use a
[L328] [12:30.96] micro card interpreter. you it might
[L329] [12:33.04] make sense in some very tiny
[L330] [12:34.64] applications possibly where you have you
[L331] [12:37.84] know thousand tens of thousands of
[L332] [12:39.52] transistors maybe this would a microcode
[L333] [12:41.68] interpret work but I think nobody today
[L334] [12:43.76] I don't think anybody's invented an
[L335] [12:45.28] instruction set in the last 20 years
[L336] [12:47.12] that u has anything that would need a
[L337] [12:50.00] microcoded interpreter
[L338] [12:51.92] >> you mentioned the compiler multiple
[L339] [12:54.56] times here and it seems like that's a
[L340] [12:56.08] critical piece that kind of makes risk
[L341] [12:59.12] work so well can you explain the role of
[L342] [13:01.68] the compiler and how it manages the
[L343] [13:04.16] relationship between software and
[L344] [13:05.76] hardware.
[L345] [13:06.72] >> Well, you you're writing in a
[L346] [13:08.00] programming language like C or C++ or
[L347] [13:11.44] maybe Python and um but the quality of
[L348] [13:14.56] the code that gets generated is is up to
[L349] [13:16.80] the compiler if you and a specific
[L350] [13:19.84] example is that it's useful when you
[L351] [13:22.40] construct computers to have registers
[L352] [13:24.16] and those registers are actually kind of
[L353] [13:25.92] visible in in the assembly language or
[L354] [13:28.08] the machine language programming.
[L355] [13:30.16] It can be 8, 16 or 32 these registers
[L356] [13:33.12] for the people programming that little
[L357] [13:35.92] level to use. Well, it used to be very
[L358] [13:38.88] difficult for compilers to to um
[L359] [13:42.64] allocate registers efficiently when they
[L360] [13:45.36] computers just weren't fast enough. We
[L361] [13:46.96] didn't have the algorithms that we could
[L362] [13:48.72] look at a section of code or a sub
[L363] [13:50.80] routine or something and say how can we
[L364] [13:52.88] most efficiently do registers? In fact,
[L365] [13:55.68] the C programming language which was
[L366] [13:58.48] invented to do systems programming
[L367] [14:02.32] in C before that to write an operating
[L368] [14:04.64] system people wrote them an assembly
[L369] [14:06.08] language believe it or not and but the
[L370] [14:08.72] Unix people showed uh Ken Thompson
