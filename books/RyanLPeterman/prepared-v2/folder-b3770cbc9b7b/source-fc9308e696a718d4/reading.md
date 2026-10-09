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
[L371] [14:11.20] Dennis Richie showed that we could if we
[L372] [14:13.68] had a low-level language pretty
[L373] [14:15.28] low-level language we get the benefits
[L374] [14:17.12] of writing in something that it's much
[L375] [14:18.72] easier for humans to understand and
[L376] [14:20.24] debug
[L377] [14:22.24] because register allocation by the
[L378] [14:24.48] compilers was was so poor, they had to
[L379] [14:27.68] put in the ability for the programmer to
[L380] [14:30.08] give hints of what variables should go
[L381] [14:31.60] in registers. It was just easier for
[L382] [14:33.68] them to have the programmer step in and
[L383] [14:36.40] say, if the machine had eight registers,
[L384] [14:38.08] I want these six variables to be in
[L385] [14:39.84] these registers. Don't leave them in
[L386] [14:41.20] memory because it runs so much slower.
[L387] [14:43.12] Registers are so much faster. So, a big
[L388] [14:46.48] part of u the the CISK the risk argument
[L389] [14:50.56] was the compiler algorithms are getting
[L390] [14:52.64] better. they could handle these
[L391] [14:53.92] low-level instructions, they could
[L392] [14:55.60] allocate registers efficiently.
[L393] [14:58.16] Uh, and that was, you know, another
[L394] [15:00.24] reason in these debates about why it
[L395] [15:02.40] made sense to have a simpler
[L396] [15:03.92] architecture. What we did in the risk
[L397] [15:06.24] architectures, well, if registers are
[L398] [15:08.16] really important, uh, register
[L399] [15:10.16] allocation really important. One way to
[L400] [15:11.60] make it easier for the compiler was just
[L401] [15:13.76] to have a lot more of them. So,
[L402] [15:15.68] typically the CISK architectures of
[L403] [15:17.44] times would have eight or maybe 16
[L404] [15:19.20] registers. So, we we put in 32 and That
[L405] [15:23.44] was one of the arguments, right, is
[L406] [15:25.52] well, if it's hard to efficiently use a
[L407] [15:27.84] small number, let's give them plenty.
[L408] [15:29.28] So, even if it wasn't that good,
[L409] [15:31.44] there'll be enough registers. So, most
[L410] [15:32.72] of the time and and registers weren't
[L411] [15:34.48] that much more expensive to include in
[L412] [15:36.32] machines because of MOR's law. I saw
[L413] [15:38.72] somewhere in in uh one of the talks that
[L414] [15:41.20] he had given that somehow the compiler
[L415] [15:44.88] it's it's more easy for it to optimize
[L416] [15:46.80] the code for risk but in CISK there were
[L417] [15:49.68] these complex bigger ones and it almost
[L418] [15:52.64] never used them. Is that a shortcoming
[L419] [15:54.56] of the compiler? So what happened if we
[L420] [15:57.36] go back in the compiler days there's
[L421] [15:59.84] this argument is that by having more
[L422] [16:01.60] sophisticated instructions this would
[L423] [16:03.84] raise the level of extraction. that'll
[L424] [16:05.52] be a smaller gap. They'll make it easy
[L425] [16:07.36] for the compiler. But that was a
[L426] [16:08.56] philosophical argument. It it wasn't
[L427] [16:10.88] something that necessarily compiler
[L428] [16:12.72] people um could work. Compiler people
[L429] [16:16.88] weren't making that argument. It was the
[L430] [16:18.72] architects were making that argument.
[L431] [16:20.80] And as it turned out when we looked at
[L432] [16:22.48] the programs when we were doing the
[L433] [16:24.32] early research on CISK in versus risk is
[L434] [16:28.08] the compilers didn't really use those
[L435] [16:29.52] instructions. Often the compiler
[L436] [16:30.96] writers, the architects would come up
[L437] [16:32.64] with a sophisticated instruction and the
[L438] [16:34.88] compiler writers would say, "Well, we
[L439] [16:36.56] don't need that." In fact, we found
[L440] [16:38.80] examples where like for a procedure
[L441] [16:40.80] entry, there'd be a special instruction
[L442] [16:43.04] built in to do all this work that what
[L443] [16:45.12] the architects thought the compilers
[L444] [16:46.48] wanted and the compiler designers say,
[L445] [16:48.16] "Well, we don't need that. It's it's
[L446] [16:50.64] faster. It's actually faster for to use
[L447] [16:52.96] it with separate instructions than use
[L448] [16:55.04] your sophisticated instruction." And so,
[L449] [16:56.96] we found a bunch of examples like that.
[L450] [16:58.96] So you pay the extra overhead of the
[L451] [17:00.88] microode interpreter to have these
[L452] [17:02.48] sophisticated instructions and then the
[L453] [17:04.32] compiler doesn't even use them. Right?
[L454] [17:06.32] So th this is kind of a nonsensical
[L455] [17:08.88] situation that that we're in. uh and you
[L456] [17:12.64] know this is kind of like you know why
[L457] [17:14.64] why are there startups or why are there
[L458] [17:17.36] scientific you know breaking points like
[L459] [17:20.40] that as we looked at all the
[L460] [17:21.60] technologies with Moore's law you know
[L461] [17:24.00] ideas like caches with where compilers
[L462] [17:27.20] were in using sophisticated instructions
[L463] [17:28.80] the ability to allocate register more
[L464] [17:30.64] efficiently it made sense to change the
[L465] [17:33.12] directions away from these microcoded
[L466] [17:34.88] instruction set architectures to these
[L467] [17:36.80] simpler architectures
[L468] [17:38.32] >> when we talk about instruction sets I
[L469] [17:40.24] mean we're kind assuming that we're
[L470] [17:42.00] talking about these general purpose
[L471] [17:44.24] computer are these CPUs and I know GPUs
[L472] [17:47.20] are kind of talked about a lot and maybe
[L473] [17:50.08] there's other forms of computing are
[L474] [17:52.32] there instruction sets for those types
[L475] [17:54.80] of machines as well.
[L476] [17:56.00] >> So what happened is around 2000 is when
[L477] [17:59.04] GPUs came along and these were what we
[L478] [18:02.00] called domain specific architectures. So
[L479] [18:03.92] a GPU is a graphics processing unit. It
[L480] [18:06.56] had one job. it it didn't need to do
[L481] [18:09.60] everything that a general purpose
[L482] [18:10.80] processor needs to. Didn't have to
[L483] [18:12.72] support virtual memory. Uh it didn't
[L484] [18:15.36] have to support a compiler which is you
[L485] [18:17.36] know a pretty radical idea for
[L486] [18:19.44] architectures. It was just for graphics.
[L487] [18:22.16] And so around 2000 is when Nvidia and
[L488] [18:25.76] the other GPUs out there because they
[L489] [18:27.44] were trying to do you know the give you
[L490] [18:30.32] the graphics for games and give you the
[L491] [18:31.76] graphics for movies. So it was a niche
[L492] [18:33.76] product.
[L493] [18:35.28] So what happened kind of in the computer
[L494] [18:37.36] industry is it was driven by Moore's law
[L495] [18:40.88] which I've mentioned many times and also
[L496] [18:43.44] this lesserk known law called dinard
[L497] [18:45.76] scaling which is because kind of an
[L498] [18:48.16] interesting question well if Moore's law
[L499] [18:49.92] puts a lot more transistors on a chip
[L500] [18:52.40] how come they're not getting hotter and
[L501] [18:54.24] hotter as we double the number of
[L502] [18:55.92] transistors every year and the reason
[L503] [18:57.52] was this observation made by Bob Dinard
[L504] [19:01.36] that what as you added more transistors
[L505] [19:04.80] People would also lower the threshold
[L506] [19:06.56] voltage which the distinction between a
[L507] [19:08.40] zero and one and that had like a squared
[L508] [19:11.52] effect. So you would end up doubling
[L509] [19:13.92] them transistors but you'd lower the
[L510] [19:15.60] threshold voltage. So microprocessors
[L511] [19:17.92] stayed at like 20 or 30 watts. In fact
[L512] [19:22.56] uh we did a John and I eventually did a
[L513] [19:25.28] textbook and I was just checking and
[L514] [19:27.36] that came out in 1990 and we didn't even
[L515] [19:29.04] talk about power as an issue for the
[L516] [19:31.12] first three editions. You know, the the
[L517] [19:32.96] third one came out in 2000. Power wasn't
[L518] [19:35.28] even a topic because micro dinard
[L519] [19:37.68] scaling was going on and so
[L520] [19:39.04] microprocessors stayed in the tens of
[L521] [19:41.44] watts even as they got faster and
[L522] [19:43.12] faster. What happened is about 2005 or
[L523] [19:46.64] so, Dinard scaling stopped working and
[L524] [19:49.20] that was a shock, right? So, and Intel
[L525] [19:52.08] actually had a microprocessor that
[L526] [19:55.04] failed one of their generations because
[L527] [19:57.68] they just couldn't get the power down
[L528] [19:59.68] enough. it was too hot to be able to do
[L529] [20:01.68] that. Um and then so then what that
[L530] [20:05.68] forced us to go to multicore is that uh
[L531] [20:09.52] before that it was easiest for the
[L532] [20:11.28] programmer for everybody if there was
[L533] [20:12.72] one very sophisticated processor that
[L534] [20:14.96] did everything but we couldn't do that
[L535] [20:16.96] anymore. So it went from one
[L536] [20:18.72] sophisticated processor to two and then
[L537] [20:21.28] four and then eight simpler processors.
[L538] [20:23.12] Then it was up to the programmer to
[L539] [20:25.44] deliver on the potential of Morris law
[L540] [20:27.44] by paralyzing their code. So we stayed
[L541] [20:30.80] that way for about another 10 years and
[L542] [20:34.16] then Moore's law started slowing down.
[L543] [20:36.96] Uh so that the general purpose
[L544] [20:38.80] microprocessor was barely improving. It
[L545] [20:40.96] got a little better but it wasn't
[L546] [20:42.32] getting dramatically better. Um, in the,
[L547] [20:45.44] you know, in the 1980s, 1990s, 2000s,
[L548] [20:50.88] you you have a laptop and your friend's
[L549] [20:52.96] laptop would be like four times as fast
[L550] [20:55.36] as yours. And, you know, you were
[L551] [20:56.88] jealous. So, you would throw away
[L552] [20:59.04] perfectly good hardware because your
[L553] [21:01.36] friend's thing was so much faster
[L554] [21:03.60] because of the rapid change in
[L555] [21:05.04] performance. Well, that all ended in the
[L556] [21:08.32] 2010s where the you never you wouldn't
[L557] [21:10.64] throw away a laptop because the new ones
[L558] [21:12.56] were hardly that much faster than the
[L559] [21:14.40] old ones. You throw them away when they
[L560] [21:15.76] break and slow down. Nevertheless,
[L561] [21:18.16] programmers were used to this dramatic
[L562] [21:20.56] improvement in performance every few
[L563] [21:22.96] years because they could add more
[L564] [21:24.48] features to their software and stuff
[L565] [21:25.68] like that. So, what were architects
[L566] [21:27.36] going to do? They'd already done the the
[L567] [21:29.12] multicore trick in 2005 or so. So around
[L568] [21:33.76] 2015 the idea was we would do domain
[L569] [21:36.24] specific architectures like the GPUs. So
[L570] [21:38.96] we if we if you tell me I only have to
[L571] [21:41.68] run a narrow class of programs and I
[L572] [21:44.08] don't have to necessarily run all the
[L573] [21:46.32] operating systems everything else. Well
[L574] [21:48.16] yes I could shuffle those resources and
[L575] [21:51.12] do something much more efficient for
[L576] [21:53.12] something well. So you could do some
[L577] [21:54.72] things well and there's other things
[L578] [21:56.64] either you do poorly or not even at all.
[L579] [21:59.04] So then the question is okay what
[L580] [22:00.80] domain? So just coincidentally where we
[L581] [22:04.00] were technologically right around 2012
[L582] [22:07.92] 2015 is when machine learning AI burst
[L583] [22:11.12] on the scene. Um and so that was it was
[L584] [22:15.12] evident what domain should we do and the
[L585] [22:17.84] domain was machine learning AI. So just
[L586] [22:20.00] coincidentally where we were
[L587] [22:21.20] technologically
[L588] [22:22.96] uh this new domain came along and then I
[L589] [22:25.76] I would say you know I I work for Google
[L590] [22:28.08] but I think it's fair to say Google was
[L591] [22:30.56] the one who really uh saw it was the
[L592] [22:33.36] certainly the first big company who
[L593] [22:35.76] understood the potential of machine
[L594] [22:37.20] learning AI and um and bet that they or
[L595] [22:42.00] feared that they were going to be
[L596] [22:43.44] swamped with demand and needed to do
[L597] [22:45.92] custom hardware. So the the translate
[L598] [22:49.76] tensor processing unit GPU that Google
[L599] [22:52.80] debuted in 2016 really kind of shocked
[L600] [22:56.24] the world and got people to realize that
[L601] [22:58.96] we should be uh designing hardware for
[L602] [23:01.28] machine learning and we could continue
[L603] [23:04.16] to improve performance dramatically for
[L604] [23:06.48] that one domain.
[L605] [23:08.08] >> What's the high level differences
[L606] [23:09.84] between a CPU, a GPU and a TPU? the the
[L607] [23:14.72] CPU has got to be this general purpose
[L608] [23:16.72] thing. And basically um even today they
[L609] [23:20.40] have these general purpose cores that
[L610] [23:23.12] each core is very similar to what the
[L611] [23:25.84] instruction sets or used to be like 20
[L612] [23:29.12] years before that. It's not a surprising
[L613] [23:31.20] design and it's just got lots of cores
[L614] [23:32.96] and modern ones today could have a h you
[L615] [23:35.28] know 50 or 100 cores in there. So that's
[L616] [23:37.76] that's the feature for graphics. uh what
[L617] [23:40.80] they decided to do which to do the
[L618] [23:43.52] graphics job is they need to get a lot
[L619] [23:45.36] of performance on the memory system. So
[L620] [23:46.96] they went to multi-threading. So they
[L621] [23:49.28] have hardware threads that you would
[L622] [23:51.36] send a memory request out and you the
[L623] [23:53.76] hardware would switch over to do
[L624] [23:54.96] something else while the when memory is
[L625] [23:57.04] coming out. So it's this highly threaded
[L626] [23:59.28] architecture and that's what they
[L627] [24:01.04] developed and could could run well for
[L628] [24:03.28] graphics.
[L629] [24:04.80] um a and graphics. It turns out um
[L630] [24:08.48] doesn't need very s doesn't need
[L631] [24:11.60] powerful floating point. It needs
[L632] [24:14.32] doesn't need wide floating point. So
[L633] [24:15.84] 32-bit floating point is plenty for
[L634] [24:17.68] graphics even 16 bit. So they were doing
[L635] [24:20.56] pushing graphics with 16 and 32-bit
[L636] [24:22.80] floating point in this multi-threaded
[L637] [24:24.80] kind of architecture. And because it was
[L638] [24:27.04] kind of its own unique thing, it has its
[L639] [24:28.64] own own set of terminology
[L640] [24:31.44] um all to itself. it wasn't kind of out
[L641] [24:33.76] of the main branch of computer
[L642] [24:35.20] architecture. Uh so when you look at our
[L643] [24:38.00] textbooks, we have kind of like a
[L644] [24:39.44] Rosetta Stone which says here's the
[L645] [24:42.32] terms that Nvidia uses to describe DP2s.
[L646] [24:45.12] This is what it means in kind of normal
[L647] [24:48.08] um well normal in the mainstream
[L648] [24:50.24] processor design. So they were this
[L649] [24:52.32] niche product that happened to do pretty
[L650] [24:54.96] fast um single precision floating point
[L651] [24:58.24] and uh even half precision floating
[L652] [25:00.24] point and they were pretty cheap. They
[L653] [25:02.64] were like hundreds of dollars.
[L654] [25:05.12] Um
[L655] [25:07.04] so when people uh so kind of uh but some
[L656] [25:12.24] people were thinking boy for some
[L657] [25:13.76] applications if I could turn my program
[L658] [25:16.64] into like uh pretend that it was doing
[L659] [25:20.16] creating an image if I could turn my
[L660] [25:22.48] problem into image generation I could
[L661] [25:24.16] use these pretty cheap GPUs which had
[L662] [25:27.20] very good floatingoint performance per
[L663] [25:29.28] dollar compared to anything else. And so
[L664] [25:31.76] people started playing around with that.
[L665] [25:33.68] Uh and uh the founder CEO Jensen Wang
[L666] [25:38.16] really liked that idea. So in 2006,
[L667] [25:42.72] he funded an effort to create a
[L668] [25:45.28] programming language that that would
[L669] [25:47.28] kind of handle this multi-threaded
[L670] [25:49.60] hardware architecture that's for
[L671] [25:50.96] graphics to make it easier to program.
[L672] [25:53.12] And so that led to the invention of uh
[L673] [25:56.16] CUDA uh which I can't remember its
[L674] [25:58.56] acronym but it's really a a proprietary
[L675] [26:01.44] programming language for the
[L676] [26:02.72] multi-threaded GPU architecture to make
[L677] [26:05.60] it kind of easier to program. It was a
[L678] [26:07.84] it was a C like language but you can't
[L679] [26:10.56] just compile C programs and run it but
[L680] [26:12.56] it was C like but people actually liked
[L681] [26:14.88] it. You know it was certainly much
[L682] [26:16.24] better than trying to turn your program
[L683] [26:17.84] into an image generation but people
[L684] [26:20.40] liked it. But uh Jensen Wang his vision
[L685] [26:22.80] was try to get these teenagers in the
[L686] [26:25.12] basement who are playing the games to
[L687] [26:26.40] learn how to program these things. And
[L688] [26:28.00] he had a couple of markets that he was
[L689] [26:29.76] interested in like um you know uh some
[L690] [26:33.20] of the department of energy labs like uh
[L691] [26:35.60] fluid flow and some of things like you
[L692] [26:37.76] know some and he would build special
[L693] [26:39.44] purpose libraries that could handle that
[L694] [26:41.28] domain and then use his GPUs to do that
[L695] [26:44.48] kind of uh special purpose computing but
[L696] [26:47.28] breaking out of graphics. But that's
[L697] [26:49.76] kind of the heritage there. Now for the
[L698] [26:51.52] TPU program um and and so what's
[L699] [26:54.88] happened uh people started right from
[L700] [26:56.88] the very beginning people started using
[L701] [26:58.24] GPUs because they had much better single
[L702] [27:00.64] precision floatingoint performance than
[L703] [27:03.52] um than the CPUs. They had a lot more
[L704] [27:06.24] processors on them. So we had the
[L705] [27:08.24] potentially much more performance. So
[L706] [27:09.76] they're kind of one of the breakthrough
[L707] [27:11.20] moments moments in it was in 2012 when
[L708] [27:16.88] uh within the machine learning community
[L709] [27:18.96] this neural networking piece which had a
[L710] [27:21.76] few advocates but a lot of people didn't
[L711] [27:23.44] believe in it they went into a
[L712] [27:25.44] competition to see who could do the best
[L713] [27:27.92] image recognition in 2012 the so-called
[L714] [27:31.60] AlexNet beat all the competition this
[L715] [27:33.92] was this uh historic moment in the in
[L716] [27:37.68] the in machine learning learning in
[L717] [27:39.68] neural networking and once they did it
[L718] [27:42.48] and the guy who did that had taken a
[L719] [27:44.24] cuda course at the University of Toronto
[L720] [27:46.48] to learned how to use it and so he says
[L721] [27:47.76] well as long as I'm doing this I'll do
[L722] [27:49.04] it on a GPU so he was able to explore a
[L723] [27:51.84] lot more space on this cheap fast GPU so
[L724] [27:55.28] he entered it in the competition 2012
[L725] [27:58.08] and within he was the only one using
[L726] [28:00.08] neural networks and he crushed the
[L727] [28:01.92] competition and within a few years
[L728] [28:03.76] everybody switched over and not only
[L729] [28:06.16] they were doing neural networks but
[L730] [28:07.44] they're using GPUs
[L731] [28:09.28] So GPUs have this um heritage of being a
[L732] [28:12.64] graphics in graphics engine but more
[L733] [28:16.40] programmable and uh it started getting
[L734] [28:19.52] used for machine learning. When Google
[L735] [28:22.08] came along uh they decided you know it
[L736] [28:24.72] was a clean slate. They didn't they
[L737] [28:26.24] didn't care about graphics. So the at
[L738] [28:28.96] the heart of neural networking is a
[L739] [28:31.04] matrix multiply. That's the that's the
[L740] [28:33.20] thing. So they designed a a processor
[L741] [28:36.00] for at the time microp processor at the
[L742] [28:37.68] time had a giant matrix multiplying
[L743] [28:39.84] unit. That was the main thing and then
[L744] [28:41.92] they threw a bunch of stuff out that
[L745] [28:43.28] they didn't need. So a lot of general
[L746] [28:45.52] purpose computing is what's on the chip
[L747] [28:47.76] is maybe three levels of caches to try
[L748] [28:50.88] and have so you don't spend all your
[L749] [28:52.88] time going to the relatively slow
[L750] [28:54.32] memory. Well, for machine learning, they
[L751] [28:56.32] knew when their memory accesses were so
[L752] [28:58.08] they could schedule that. So they didn't
[L753] [29:00.32] a a hardware cache didn't make any
[L754] [29:02.32] sense. they would just have a memory
[L755] [29:04.00] that the software understood would
[L756] [29:05.36] transfer in time. So those were some of
[L757] [29:07.28] the innovations. Also they innovated on
[L758] [29:09.36] the floatingoint format. You didn't need
[L759] [29:12.32] uh uh you know scientific computing
[L760] [29:15.60] cares a lot about precision. They have
[L761] [29:18.00] you know most of it's done in 64-bit
[L762] [29:19.76] floating point where the exponent is you
[L763] [29:22.40] know less than 10 bits and most of it is
[L764] [29:25.20] is the uh precision you know the
[L765] [29:27.52] fraction can be 50 some bits. Well, they
[L766] [29:30.56] what they realized for machine learning
[L767] [29:32.16] and AI, they don't need all that
[L768] [29:33.92] precision. They needed the range. So,
[L769] [29:35.76] Google did the first floatingoint format
[L770] [29:38.48] where the exponent was bigger than the
[L771] [29:40.16] fraction. That's that was a radical idea
[L772] [29:42.24] that so-called brain float 16, the part
[L773] [29:45.04] of Google that was doing this was the
[L774] [29:47.28] brain research group. So, they brought
[L775] [29:49.76] out this architecture. They had this
[L776] [29:52.48] narrow floating point format. They had
[L777] [29:54.80] big matrix multiply unit. It only had
[L778] [29:56.80] one one processor in it. uh unlike the
[L779] [29:59.68] other ones, it was just dedicated
[L780] [30:01.36] machine learning and it just kind of
[L781] [30:02.64] blew the doors off of everybody in the
[L782] [30:05.52] field. It was uh you know like 30 times
[L783] [30:08.32] better at inference than the
[L784] [30:10.48] contemporary GPU and 80 times better
[L785] [30:12.40] than CPU by having this dedicated one.
[L786] [30:15.20] So when uh Google made this announcement
[L787] [30:17.76] at their annual retreat a year or so
[L788] [30:20.64] after um after they had deployed it
[L789] [30:23.84] inside uh it just shook everybody up.
[L790] [30:26.40] Intel started buying companies. Um you
[L791] [30:29.52] know Nvidia started modifying the design
[L792] [30:33.12] uh for to be mach
[L793] [30:36.00] learning and then a bunch of other
[L794] [30:37.84] competitors uh started uh uh
[L795] [30:41.12] hyperscalers started doing their own
[L796] [30:42.48] effort. So I think that was the watersh
[L797] [30:44.16] I think the TPU announcement was the
[L798] [30:46.16] watershed moment there.
[L799] [30:48.32] >> So it's it's almost like uh levels of
[L800] [30:51.12] specialization like the CPU is the most
[L801] [30:53.20] general. Well yeah if we could still if
[L802] [30:55.36] you know if we still had dinard scaling
[L803] [30:57.84] if we you know Morris law and dinard
[L804] [30:59.52] scaling where we be today with general
[L805] [31:02.64] purpose processors we should have 100
[L806] [31:04.32] terahertz
[L807] [31:05.92] you know microprocessors if we could
[L808] [31:07.92] build 100 terahertz microprocessors
[L809] [31:09.84] that's what we do we would the GPUs
[L810] [31:12.40] would still be a niche you know if we
[L811] [31:14.16] could do that it you know it raises all
[L812] [31:16.40] boats that would be fantastic if we
[L813] [31:18.40] could do that but that that's long in
[L814] [31:21.36] the history we haven't been able to do
[L815] [31:23.36] that for 20 years and so you know there
[L816] [31:25.60] were probably two or three gigahertz
[L817] [31:27.76] microprocessors in 2005 and that's kind
[L818] [31:31.04] of where they are barely improved today
[L819] [31:33.60] so we can't do that. So there's still
[L820] [31:36.16] areas where it's important to have CPUs.
[L821] [31:38.64] They're the right, you know, you need
[L822] [31:40.56] operating systems, compilers and things.
[L823] [31:43.04] Uh that they're the right solution, but
[L824] [31:45.36] things have been specialized. And then
[L825] [31:47.84] now in terms of industry terms, huge
[L826] [31:50.80] emphasis is being put into the AI
[L827] [31:53.20] accelerators or just AI in general is
[L828] [31:56.24] where the money is being invested. And
[L829] [31:58.08] so the question for any processor
[L830] [32:00.32] designers was how does my processor
[L831] [32:03.44] design fit into this AI universe and um
[L832] [32:08.32] what should I do? How should I change it
[L833] [32:10.08] for this important application?
[L834] [32:12.48] >> So you mentioned that kind of Moore's
[L835] [32:14.64] laws slowing down and I watched this
[L836] [32:17.36] other talk from Jim Keller saying that
[L837] [32:20.72] Moore's law isn't isn't dead. But is it
[L838] [32:23.68] controversial to say that it's slow? Oh,
[L839] [32:25.52] I mean not not to real engineers. The
[L840] [32:28.80] the Morris law is very simple. It says
[L841] [32:30.88] in a in a chip the number of transistors
[L842] [32:33.92] will double originally said every year
[L843] [32:35.92] and then he mended it uh to every two
[L844] [32:38.72] years. Just just look do the chips are
[L845] [32:41.68] the number of transistors doubled and no
[L846] [32:44.24] now I think what people assume that
[L847] [32:47.68] means if trans if we are no longer on
[L848] [32:50.08] Morris law that technology is not
[L849] [32:52.16] improving. That's not the same thing.
[L850] [32:54.32] it's not improving at the rate that
[L851] [32:56.00] Moore projected. And what was amazing
[L852] [32:58.40] about Moors law which lasted 50 years is
[L853] [33:01.76] that it it guided the investment of
[L854] [33:04.32] semigtory manufacturing. We need to
[L855] [33:06.56] deliver on doubling transistors every
[L856] [33:08.48] year or two. How are we going to do
[L857] [33:10.72] that? How are we going to build the
[L858] [33:12.32] equipment to do it? So it was a
[L859] [33:13.52] guideline for the whole industry which
[L860] [33:15.84] was kind of remarkable. So what we are
[L861] [33:18.40] doing now is there's pieces of the
[L862] [33:21.20] technology to get better and there's
[L863] [33:22.64] pieces that uh that don't improve at
[L864] [33:25.76] all. So one of the big pieces important
[L865] [33:28.80] pieces on a chip is the static RAM
[L866] [33:31.44] SRAMM. So that's hardly improving at
[L867] [33:33.76] all.
[L868] [33:35.44] Logic gates still continue to improve.
[L869] [33:37.60] They are the gates are getting better.
[L870] [33:39.44] So if you're doing like uh adders or
[L871] [33:42.08] multipliers, those are getting better.
[L872] [33:43.36] those pieces. It's not uniform
[L873] [33:45.60] improvement anymore. And we're also
[L874] [33:47.76] going to more exotic packaging to be
[L875] [33:50.72] able to deliver it. Uh so people not uh
[L876] [33:54.00] it, you know, forever it was a single
[L877] [33:56.72] chip was the best way to package
[L878] [34:00.32] everything fits on one chip and that's
[L879] [34:02.16] what we're going to build. And now
[L880] [34:03.84] there's these ideas of chiplets or
[L881] [34:06.08] packaging multiple chips together. the
[L882] [34:08.08] latest GPUs and I think the latest TPUs
[L883] [34:11.20] has actually two what are called full
[L884] [34:13.44] reticle design dyes package put into a
[L885] [34:17.36] package and uh so a full reticle design
[L886] [34:20.72] is uh the maximum you can build on a on
[L887] [34:23.92] a semiconductor it they have a step and
[L888] [34:26.24] repeat motor and there's you know in the
[L889] [34:28.24] old days you'd have many chips inside
[L890] [34:29.92] that now there's just one so two maximum
[L891] [34:33.12] reticle designs form a node so they're
[L892] [34:35.84] using packaging so if you from outside
[L893] [34:38.72] you can say well there look there's look
[L894] [34:40.40] how many transistors are it's quote
[L895] [34:42.48] Moore's law is continuing but if you see
[L896] [34:44.96] what's inside the chip you know that's
[L897] [34:47.04] that has tapered off and I think part of
[L898] [34:48.96] it is for a fair amount of the industry
[L899] [34:52.24] if you were in a semiconductor
[L900] [34:54.00] manufacturer and people ask you what you
[L901] [34:55.76] do is I make Moors law I I make I
[L902] [34:59.28] sustain Morris law what I do and if
[L903] [35:01.12] you've been doing that for decades and
[L904] [35:02.48] somebody says Morris law is over it's
[L905] [35:04.08] like it my my career is
[L906] [35:06.96] So I think there's an emotional side of
[L907] [35:08.64] it but you know just look at the data
[L908] [35:11.20] the data doesn't back up what Keller
[L909] [35:12.96] says but I also didn't say that the
[L910] [35:16.32] technology is not improving the
[L911] [35:18.64] technology is continuing to improve and
[L912] [35:21.04] specifically domain specific
[L913] [35:22.64] architectures but if you look at the
[L914] [35:24.24] general purpose architectures or even
[L915] [35:26.48] other memory technologies you know it
[L916] [35:29.20] used to be the DRAMs would improve by a
[L917] [35:31.52] factor of four in density every 3 years
[L918] [35:33.44] like clockwork and now it's maybe 10
[L919] [35:36.40] years between factors for so you can see
[L920] [35:38.16] plenty of evidence that Moore's law no
[L921] [35:40.40] longer applies.
[L922] [35:41.92] >> Is there um some new version or some
[L923] [35:46.80] analog to Mo's law that is kind of
[L924] [35:48.72] guiding uh you know microprocessor
[L925] [35:52.24] design and architecture these days? I I
[L926] [35:54.88] guess a question is uh both Nvidia and
[L927] [35:59.60] Google are continuing to deliver much
[L928] [36:02.08] faster processors for machine learning,
[L929] [36:04.72] tremendously better. What are they
[L930] [36:06.48] doing? Well, part of it is what I said
[L931] [36:10.24] about uh packaging, you know, to getting
[L932] [36:12.88] uh to to be able to get more transistors
[L933] [36:15.28] and you keep them closer together
[L934] [36:16.88] because distance matters. Uh part of it
[L935] [36:19.20] is innovating on the floatingpoint
[L936] [36:20.64] formats. So it you know unlike the
[L937] [36:23.52] supercomputers of 64-bit
[L938] [36:26.08] it's not even 64-bit not even 32-bit not
[L939] [36:28.80] even 16 bit but 8bit and 4bit floating
[L940] [36:31.68] point is as is going on so narrowing of
[L941] [36:34.16] the data types um the uh you know having
[L942] [36:40.08] kind of what's called the matrix
[L943] [36:42.08] multiply instructions so these powerful
[L944] [36:44.88] units that are put in there that can
[L945] [36:46.72] that can uh do special purpose
[L946] [36:49.20] applications that are very important get
[L947] [36:51.28] making those bigger and faster. So those
[L948] [36:53.52] are the things that are going on. But we
[L949] [36:56.24] don't have this simplifying guideline
[L950] [36:59.68] kind of underlying all this. You have to
[L951] [37:02.00] be aware of each piece of the
[L952] [37:04.08] technology, gauge how fast it's
[L953] [37:06.64] improving, how whether it's they can
[L954] [37:09.52] deliver on what's going on and then you
[L955] [37:12.24] assemble that together and make your
[L956] [37:14.48] bets. We're, you know, there's a paper
[L957] [37:16.64] that we've just got approved that I
[L958] [37:18.96] think we're going to put on archive
[L959] [37:20.16] soon, which is, uh, talking about the
[L960] [37:23.12] Google TPU line and pretty remarkably,
[L961] [37:26.24] uh, the Google TPU line particularly for
[L962] [37:28.32] training has stayed pretty constant in
[L963] [37:31.36] the basic architecture design, uh,
[L964] [37:34.32] things have gotten bigger and faster,
[L965] [37:36.80] but the if you look at the the the
[L966] [37:39.28] design of it, going back to the first
[L967] [37:41.36] training TPU, it's that block diagram
[L968] [37:44.00] still works.
[L969] [37:45.12] uh all these you know a decade later. So
[L970] [37:47.84] it you know the people who designed that
[L971] [37:50.08] in whatever 2015 or two did a really
[L972] [37:52.80] great job. Uh but the main components of
[L973] [37:55.76] a a big matrix multiply unit the
[L974] [37:57.84] so-called high bandwidth memory um uh a
[L975] [38:01.84] vector unit to go with the matrix unit
[L976] [38:03.92] and the basic building blocks are still
[L977] [38:06.08] there. I think in your career with the
[L978] [38:08.64] CPUs, benchmarks were a huge they played
[L979] [38:11.12] a huge role in in measuring which
[L980] [38:14.80] computer architectures were performant
[L981] [38:16.40] and not in this this new space of uh
[L982] [38:20.00] floatingoint operations for AI. Is there
[L983] [38:22.56] a benchmark that people use for GPUs and
[L984] [38:25.20] can you also apply it for TPUs?
[L985] [38:27.84] >> I was you know I and some friends were
[L986] [38:30.64] helped involved in called the ML Perf
[L987] [38:32.72] effort. So it was inspired by the spec
[L988] [38:36.40] CPU effort was the spec benchmarks that
[L989] [38:40.00] there were these competing companies and
[L990] [38:41.68] they'd all make claims about theirs was
[L991] [38:44.00] better than the others and they realized
[L992] [38:45.12] that wasn't good for the industry. So
[L993] [38:47.20] they agreed on a set of benchmarks. So
[L994] [38:49.20] the ML Perf effort is uh that's run now
[L995] [38:52.48] but what's called ML comments is an
[L996] [38:53.92] attempt to do that is if we're going to
[L997] [38:56.08] do this comparisons
[L998] [38:58.24] let's um let's let's not argue about
[L999] [39:01.52] what the benchmarks are. So that's a
[L1000] [39:03.84] serious effort in that kind of
[L1001] [39:05.68] interestingly what's happened I'd say is
[L1002] [39:08.80] because
[L1003] [39:10.72] uh there's two pieces to u the design
[L1004] [39:14.00] there's the the machine learning
[L1005] [39:15.76] libraries that are uh to implement a lot
[L1006] [39:19.20] of features that you need for for these
[L1007] [39:21.84] applications and the libraries will even
[L1008] [39:24.40] be rewritten for specific applications
[L1009] [39:27.20] rather than just having general
[L1010] [39:28.80] libraries. This has turned out to be a
[L1011] [39:31.12] big advantage for Nvidia because they
[L1012] [39:32.80] have a large corporation with lots of
[L1013] [39:35.04] people that are available, lots of
[L1014] [39:37.12] engineers who could build these
[L1015] [39:38.48] libraries for them. So, it's turned out
[L1016] [39:41.60] um um not quite a it's not a it's not a
[L1017] [39:45.36] neutral evaluation, right? It's it's the
[L1018] [39:49.12] architecture plus the the libraries that
[L1019] [39:53.36] go with it and the compiler too, but
[L1020] [39:56.24] specifically the libraries that you
[L1021] [39:58.00] tailor each time. So Nvidia brings out
[L1022] [40:00.80] when they announce the new architecture
[L1023] [40:02.88] they create a new set of they modify the
[L1024] [40:05.44] libraries to run that really well or to
[L1025] [40:08.24] run applications really well. So that's
[L1026] [40:10.80] a powerful combination kind of in
[L1027] [40:13.20] business terms people referred to
[L1028] [40:15.36] Nvidia's having this CUDA moat but and
[L1029] [40:19.36] part of it is CUDA the programming
[L1030] [40:21.20] language but a big part of it is the
[L1031] [40:22.64] libraries that Nvidia Nvidia makes. So
[L1032] [40:25.84] this has made it difficult for for
[L1033] [40:27.76] startups to be able to compete with
[L1034] [40:29.36] Nvidia partly because
[L1035] [40:32.80] you know they didn't put enough emphasis
[L1036] [40:35.04] in the software and partly because you
[L1037] [40:37.52] know Nvidia just has many more engineers
[L1038] [40:40.40] than they do to be able to tailor the
[L1039] [40:42.00] libraries. So it's the libraries plus
[L1040] [40:44.80] the architecture that's this this
[L1041] [40:47.04] powerful advantage why most people do
[L1042] [40:50.00] things on GPUs. Now Google has been able
[L1043] [40:52.96] to develop their own libraries. Uh they
[L1044] [40:55.52] don't have as many engineers. They use
[L1045] [40:57.68] compilers more uh than I think Nvidia
[L1046] [41:00.96] does. So they they have a set of
[L1047] [41:02.80] libraries that they can do. But up until
[L1048] [41:05.28] recently, Google has
[L1049] [41:07.84] it's all been internal. It's just for
[L1050] [41:09.44] Google to use or you could use it via
[L1051] [41:11.44] the cloud. Um but uh you these startups
[L1052] [41:15.36] have u you know have to have a
[L1053] [41:18.00] difficulty as a result. That's why the
[L1054] [41:20.72] ML Perf hasn't been as popular. Not
[L1055] [41:22.96] everybody runs them because uh Nvidia
[L1056] [41:25.68] runs them really well, really better
[L1057] [41:28.24] than everybody else. And the startups
[L1058] [41:30.00] have a hard time showing off what they
[L1059] [41:31.76] can do uh given they don't have the the
[L1060] [41:36.00] engineering effort going into the
[L1061] [41:37.20] libraries that you need to do well in ML
[L1062] [41:39.36] Perf. you gave this popular talk about
[L1063] [41:42.40] how to have a bad career and it's kind
[L1064] [41:44.88] of uh the negation of advice to kind of
[L1065] [41:49.04] have a good career and I was just
[L1066] [41:51.84] wondering if you could kind of summarize
[L1067] [41:53.92] maybe the the top three things that you
[L1068] [41:56.64] kind of think people should take away.
[L1069] [41:58.16] >> Yeah. So, yeah. Well, there's been a few
[L1070] [42:00.24] things. So, the story is early in my
[L1071] [42:02.72] career my f a good friend and I said,
[L1072] [42:04.40] "How can we teach grad students how to
[L1073] [42:05.84] give a good talk?" And we thought it'd
[L1074] [42:07.60] be funny to explain how to give a bad
[L1075] [42:09.76] talk and then if you didn't want to give
[L1076] [42:11.76] a bad talk, this is so this is how to do
[L1077] [42:14.16] it badly and if you don't here's the
[L1078] [42:15.76] things to do not to do it badly. And so
[L1079] [42:17.92] then I later did a how to have a bad
[L1080] [42:19.52] career that's pretty much focused
[L1081] [42:21.04] towards uh academia you know so for
[L1082] [42:23.68] researchers to be able to do that. I
[L1083] [42:25.92] later did a how to have a bad uh
[L1084] [42:30.40] how to build a bad research center, how
[L1085] [42:32.08] to build a bad research lab. And then
[L1086] [42:33.76] recently I've been giving how to give AI
[L1087] [42:36.00] a bad carbon footprint. That's my latest
[L1088] [42:37.92] one. But I think the thing that might be
[L1089] [42:40.08] more relevant is uh at the end of my
[L1090] [42:42.40] talks I would I would kind of reflect on
[L1091] [42:44.24] my career and talk about lessons
[L1092] [42:45.92] learned. So I've written a paper called
[L1093] [42:48.64] uh lesson I think it's lessons life
[L1094] [42:51.84] lessons from the first half century of
[L1095] [42:53.84] my career. I wrote that recently. And so
[L1096] [42:56.24] those those are divided up into kind of
[L1097] [42:58.72] career advice and personal advice there.
[L1098] [43:02.00] On the the personal side, I'd say uh if
[L1099] [43:05.20] you have a family, you know, make sure
[L1100] [43:06.80] your families first, keep your family
[L1101] [43:08.96] first. Um the technology we've invented
[L1102] [43:11.60] makes it really easy for your, you know,
[L1103] [43:14.24] to take your work home with you and not
[L1104] [43:16.48] pay attention to your family. Uh, I had
[L1105] [43:18.40] a when I was first here at Berkeley, I
[L1106] [43:20.96] gave a senior faculty member a ride
[L1107] [43:23.28] home, dropped him off late at night
[L1108] [43:24.96] coming up from Silicon Valley and he
[L1109] [43:26.56] said, "Well, Dave, if I had to do it
[L1110] [43:28.08] over all over again, I wish I'd spent
[L1111] [43:31.20] more time with the family." And I never
[L1112] [43:33.68] wanted to say that. And nobody on their
[L1113] [43:35.68] deathbed says, you know, I wish I'd
[L1114] [43:37.20] spent more time in the office. So, so
[L1115] [43:39.76] you got to, you know, whenever it's easy
[L1116] [43:41.36] to kind of, you know, let the let your
[L1117] [43:44.80] career overcome the needs of your
[L1118] [43:48.08] family, but you just you got to just
[L1119] [43:49.84] remember that. Uh, I would say in my
[L1120] [43:53.44] life and kind of growing up in the 50s,
[L1121] [43:56.56] you know, the idea was to be happy, you
[L1122] [43:58.56] had to be wealthy. But those are
[L1123] [44:00.24] actually two different goals, wealthy
[L1124] [44:01.52] and happiness. So, I always made
[L1125] [44:03.20] decisions towards happiness versus
[L1126] [44:05.12] wealth. You come down with it. And I
[L1127] [44:07.20] felt very good about that. Uh I and even
[L1128] [44:10.56] now like why would I pick why would I
[L1129] [44:13.52] pick something that made me wealthy and
[L1130] [44:15.12] unhappy? Why would you do that? And so
[L1131] [44:18.80] uh and in the field that we're in it
[L1132] [44:21.52] turned out there was a lot of wealth to
[L1133] [44:23.60] go with it. So you know optimizing
[L1134] [44:26.08] happiness didn't mean you had to suffer
[L1135] [44:29.36] uh beyond that. Um I think it's
[L1136] [44:32.00] important to have fun. Personally, I
[L1137] [44:34.16] think when you're a kid, you don't have
[L1138] [44:35.52] to tell kids to play, but as an adult,
[L1139] [44:37.12] you get so busy. You you don't think you
[L1140] [44:40.32] have time to have fun. Uh, but you know,
[L1141] [44:42.48] you only get to do this once. So, uh, so
[L1142] [44:45.28] I right now I play soccer, I run my
[L1143] [44:47.20] bicycle to the interview, uh, I lift
[L1144] [44:49.28] weights, I body surf, I, you know, do
[L1145] [44:51.84] things with my wife and family and my
[L1146] [44:53.68] son. So, it it's important to have fun.
[L1147] [44:56.96] I think uh on the career side is one of
[L1148] [45:01.28] the uh pieces of advice is uh by a he
[L1149] [45:06.00] wrote this book the habits of very
[L1150] [45:09.92] effective people I think and he has a
[L1151] [45:12.08] little quadrant and he divides it of
[L1152] [45:15.68] urgent and not urgent and important and
[L1153] [45:17.84] unimportant and kind of there's so many
[L1154] [45:20.96] things in our technology like email and
[L1155] [45:22.88] texting to for you to focus on the
[L1156] [45:25.36] urgent things but you really shouldn't
[L1157] [45:26.56] shouldn't be spending a lot of time on
[L1158] [45:28.56] the unimportant urgent things. And it
[L1159] [45:30.72] takes self-discipline to set aside time
[L1160] [45:33.76] for the uh important non-urgent things.
[L1161] [45:37.76] But if you don't block that out, you can
[L1162] [45:39.52] just not have time to do anything. I get
[L1163] [45:41.68] to see other people's calendars at
[L1164] [45:43.76] Google and there's managers that every
[L1165] [45:45.52] half hour from 8 to 6, five days a week
[L1166] [45:48.24] are scheduled and I don't see how you
[L1167] [45:50.64] have time to think and reflect on things
[L1168] [45:53.52] like that.
[L1169] [45:54.96] Um, other career advice things is, uh, I
[L1170] [45:59.44] remember, uh, I kind of woke up one
[L1171] [46:02.00] morning and it was like God spoke to me.
[L1172] [46:04.00] I was like thunder struck. And it says
[L1173] [46:05.84] it's not how many things you start, it's
[L1174] [46:07.52] how many things you finish.
[L1175] [46:09.68] It seems relatively obvious, but you
[L1176] [46:11.76] know, I that's not the way I was acting.
[L1177] [46:13.76] I had they had many things going on. But
[L1178] [46:16.24] after that, it was like there's one main
[L1179] [46:18.08] thing I'm doing at time. So when
[L1180] [46:19.44] Hennessy and I wrote our textbook, that
[L1181] [46:21.92] was the main thing. when I was
[L1182] [46:23.36] department here, head here, that was the
[L1183] [46:25.68] main thing I did. Uh I would do some
[L1184] [46:28.16] other little things there. And John
[L1185] [46:30.32] Hennessy, he he wrote a book too, a kind
[L1186] [46:32.64] of a a career advice book based on his
[L1187] [46:35.76] presidency. And one of the things he
[L1188] [46:37.76] said in there, you know, you're only
[L1189] [46:39.04] going to be remembered for the five or
[L1190] [46:41.04] six things you've done in your life, not
[L1191] [46:42.56] for the hundreds of little things. So to
[L1192] [46:44.96] give yourself a chance to uh have some
[L1193] [46:47.84] things you're really proud of, it's
[L1194] [46:49.92] better to concentrate on a few of them
[L1195] [46:51.92] hoping that some of them will turn out
[L1196] [46:53.44] to be a big deal rather than scatter
[L1197] [46:55.92] yourself to to um many things. But if
[L1198] [46:59.44] you're interested, you can yeah, if you
[L1199] [47:01.04] look for life lessons, David Patterson
[L1200] [47:04.40] first half century, you can see the
[L1201] [47:06.00] whole list of I think there's 16 lessons
[L1202] [47:10.16] altogether.
[L1203] [47:11.84] you mentioned that uh you you didn't
[L1204] [47:13.92] want to reflect back on your life and
[L1205] [47:15.52] feel like you didn't have enough family
[L1206] [47:17.84] time and yeah, I've I don't think I've
[L1207] [47:20.80] ever heard anyone say the opposite. Why
[L1208] [47:23.68] do you think that is? Why is it that
[L1209] [47:26.24] everyone looks back on their life and
[L1210] [47:28.08] they never regret, you know, a lot of
[L1211] [47:31.36] family time? I I imagine there's got to
[L1212] [47:34.00] be at least one person that says, "I
[L1213] [47:35.76] spent too much time with my family.
[L1214] [47:37.80] [laughter]
[L1215] [47:38.24] >> My career suffered."
[L1216] [47:39.20] >> Yeah, my career suffered.
[L1217] [47:41.28] Well, you know what's you know what's
[L1218] [47:43.04] it's it's pretty philosophical. I mean
[L1219] [47:44.88] what's what's what's life all about?
[L1220] [47:47.12] What's success? Right? You have to you
[L1221] [47:49.52] have to figure out what that means for
[L1222] [47:50.88] you. I mean if if you have uh I don't
[L1223] [47:53.52] know if you have financial goals of
[L1224] [47:56.00] being a you know a millionaire or
[L1225] [47:58.80] billionaire or something like that and
[L1226] [48:00.24] that's how you judge your life.
[L1227] [48:03.28] Okay. Good luck. You know it's pretty
[L1228] [48:06.00] hard to make it. Uh it's pretty hard to
[L1229] [48:08.40] do. Um but I think it's the you know I
[L1230] [48:12.00] when I was finishing my PhD I read this
[L1231] [48:13.92] book by studs Turkl called working where
[L1232] [48:16.56] he interviewed all these people in his
[L1233] [48:17.92] careers and they look back and what they
[L1234] [48:19.68] liked and what they didn't like what
[L1235] [48:21.04] what they felt about their careers and
[L1236] [48:22.24] what I got out of it the people who
[L1237] [48:23.84] worked with people like ministers or
[L1238] [48:25.76] teachers or doctors uh felt really good
[L1239] [48:28.88] about what they did with their careers
[L1240] [48:30.08] and the people who did more ephemeral
[L1241] [48:31.76] stuff um you know like uh you know
[L1242] [48:35.44] technology things or airplanes or
[L1243] [48:37.92] something like that are long gone didn't
[L1244] [48:39.52] feel as good about it. It was the people
[L1245] [48:40.96] that they worked with that they really
[L1246] [48:42.88] cared about. And I went out with a
[L1247] [48:45.04] retired engineering dean here and he uh
[L1248] [48:47.36] into a meeting who I knew and he said,
[L1249] [48:49.36] you know, Dave, as I flinked my ear, it
[L1250] [48:51.68] was it wasn't the projects, it was the
[L1251] [48:53.36] people that I worked at the matter and I
[L1252] [48:54.80] thought I knew that from a long time
[L1253] [48:57.36] ago. So that's I mean this is kind of
[L1254] [48:59.52] senior persons offering advice. my I
[L1255] [49:02.32] think you're going to care more about
[L1256] [49:04.32] the people you've worked with uh and the
[L1257] [49:06.48] people you've helped will be a bigger
[L1258] [49:08.40] deal. That's part of and you know one of
[L1259] [49:10.08] the other things about personal
[L1260] [49:11.20] happiness is they studied happiness.
[L1261] [49:13.12] Psychologists used to just study crazy
[L1262] [49:15.12] people but they started like why are
[L1263] [49:16.48] people happy and they know what the
[L1264] [49:18.96] reasons are you know uh have a job that
[L1265] [49:21.68] you like you know have friends and
[L1266] [49:23.84] family helping other people helping
[L1267] [49:26.08] other people makes you happy that they
[L1268] [49:27.92] they know this having something kind of
[L1269] [49:31.12] either a religious side of it doesn't
[L1270] [49:33.52] have to be a formal religion but like
[L1271] [49:35.92] contact with nature the grandeur of
[L1272] [49:37.52] nature but the the kind of the list of
[L1273] [49:39.68] things you need to do to be happy is
[L1274] [49:41.04] well understood And uh and you know
[L1275] [49:44.40] there these h and there's our world is
[L1276] [49:47.04] filled with unhappy billionaires, right?
[L1277] [49:49.36] If money was the thing that made you
[L1278] [49:51.12] happy, why are these people very wealthy
[L1279] [49:53.68] people so mad about things. So yeah,
[L1280] [49:57.76] this is me passing on advice. In one of
[L1281] [50:00.56] your talks, you had uh it said what
[L1282] [50:02.88] worked well for me and it was kind of
[L1283] [50:05.04] some reflections and one of the things
[L1284] [50:07.04] in there I thought was unique and
[L1285] [50:08.96] interesting. You mentioned that courage
[L1286] [50:12.08] was a big part of your career and I I
[L1287] [50:15.04] don't hear that too often. I was curious
[L1288] [50:16.56] why you
[L1289] [50:17.60] >> uh say courage is so important in a
[L1290] [50:19.44] career. Yeah, I I I think that's I mean
[L1291] [50:22.40] that might be partially my personal
[L1292] [50:24.96] makeup, but you know I was uh I was I
[L1293] [50:29.12] was kind of the youngest kid in my class
[L1294] [50:30.80] and kind of small. It took me a while to
[L1295] [50:33.36] grow despite age. So I was always small
[L1296] [50:36.88] but I my parents encouraged me to go out
[L1297] [50:38.96] for wrestling and uh wrestling gives you
[L1298] [50:41.92] self-con physical self-confidence
[L1299] [50:43.68] because you you know spend years doing
[L1300] [50:45.76] that. that I did in high school and
[L1301] [50:47.12] college. And so I think uh partly you
[L1302] [50:51.20] know technically
[L1303] [50:52.88] uh you know having courage to do things
[L1304] [50:54.72] it kind of goes along with the advice is
[L1305] [50:57.28] fortune favors the bold. Uh that's this
[L1306] [50:59.92] that goes that's advice is 2,000 years
[L1307] [51:02.64] old. I mean it's hard to figure this
[L1308] [51:04.88] out. U Helen Keller wrote you know e
[L1309] [51:08.08] even even trying to play it safe you
[L1310] [51:11.12] still get caught. And so it turns out
[L1311] [51:13.52] you might as well you might fail no
[L1312] [51:16.08] matter what. And if you take a big
[L1313] [51:18.88] chance if that's you can succeed if you
[L1314] [51:21.92] don't take the chance you probably won't
[L1315] [51:23.36] succeed if you play it safe. So fortune
[L1316] [51:25.52] favors the gold. And I think it takes
[L1317] [51:26.96] courage to do that. I think also it just
[L1318] [51:30.16] for me intellectually I feel like if
[L1319] [51:33.52] there's something not right I need to
[L1320] [51:35.60] stand up and confront it. And I think
[L1321] [51:37.68] that kind of ironically comes from the
[L1322] [51:39.92] wrestling side of my personality where
[L1323] [51:42.16] if I see something somebody getting
[L1324] [51:45.28] picked on or something like that, I'm
[L1325] [51:46.88] I'm going to stand and try and stop it.
[L1326] [51:48.80] And I feel that that same responsibility
[L1327] [51:51.28] intellectually if people are making bad
[L1328] [51:54.16] arguments or doing doing something that
[L1329] [51:56.48] we need to stand up and do it. And I
[L1330] [51:58.24] feel good about that. The cautionary
[L1331] [52:00.08] part about that is uh as because I guess
[L1332] [52:03.68] one of my senior faculty members saw
[L1333] [52:05.92] this nature of me. He said one of the
[L1334] [52:08.16] sayings is friends come and go but
[L1335] [52:10.40] enemies accumulate. This is an old
[L1336] [52:13.04] saying. So if you think about it you
[L1337] [52:14.48] kind of people you went to high school
[L1338] [52:15.60] with a while friends you kind of forget
[L1339] [52:17.44] but somebody who you really does dislike
[L1340] [52:19.60] you never forget that you dislike that
[L1341] [52:21.92] person. So standing up when it's
[L1342] [52:24.72] important, but be careful when you make
[L1343] [52:26.24] enemies because you know they're going
[L1344] [52:27.52] to stick around for a long time.
[L1345] [52:29.44] >> When you say something's gone bad
[L1346] [52:32.00] technically, do you mean uh someone was
[L1347] [52:34.88] incorrect?
[L1348] [52:35.68] >> Yeah. When you know when they're weak,
[L1349] [52:37.36] you know, either politically or, you
[L1350] [52:40.56] know, or or technically when it's you
[L1351] [52:43.20] it's a weak argument, right? that that I
[L1352] [52:45.68] I think give us I think I really like
[L1353] [52:48.56] there to be a marketplace of ideas and
[L1354] [52:50.56] we hone the ideas by arguing them and so
[L1355] [52:54.00] if it's a if it's a specious argument
[L1356] [52:56.40] even if a person is you know a leader of
[L1357] [52:59.36] a company and it just doesn't make sense
[L1358] [53:01.12] I feel it's kind of the responsibil it's
[L1359] [53:04.08] better for the company if somebody
[L1360] [53:05.68] stands up and points that out than to
[L1361] [53:08.16] just let them get away with it and then
[L1362] [53:10.72] um and then and you know it's a little
[L1363] [53:13.92] bit confrontational
[L1364] [53:15.12] But, you know, as long as people all
[L1365] [53:17.28] agree that, you know, this is for the
[L1366] [53:18.88] greater good, we're going to we we need
[L1367] [53:20.64] to get the right ideas out there. And
[L1368] [53:22.56] so, let's argue about the ideas to to
[L1369] [53:25.04] see uh you know, polish them to make
[L1370] [53:28.16] them stronger. Uh I think that's
[L1371] [53:30.64] important in science, in engineering, um
[L1372] [53:33.44] and kind of uh in life too. There's a
[L1373] [53:36.64] lot of stuff going on right now in the
[L1374] [53:40.00] country that uh is worrisome and uh I've
[L1375] [53:44.00] certainly stood up and wrote opeds about
[L1376] [53:47.20] things that I think are wrong and need
[L1377] [53:48.96] to be corrected and uh you know if
[L1378] [53:51.36] people are afraid to do that
[L1379] [53:54.00] it's hard to be um optimistic about the
[L1380] [53:56.72] future if people are afraid to stand up
[L1381] [53:58.24] when when there's wrongs and uh try and
[L1382] [54:01.36] stop them. You also mentioned optimism
[L1383] [54:04.08] in the talk and you had this story I
[L1384] [54:06.16] wonder if you're willing to
[L1385] [54:07.52] >> sure. [laughter] So I would say in
[L1386] [54:09.84] engineering uh you know it's it's hard
[L1387] [54:12.80] to know right uh but I think you need to
[L1388] [54:14.88] be kind of optimistic or positive have a
[L1389] [54:17.52] positive outlook because so many things
[L1390] [54:19.28] could go wrong and then so my story
[L1391] [54:21.84] personal story that illustrates it's
[L1392] [54:23.36] going back to high school when I'm 16
[L1393] [54:25.76] I'm dating this very attractive girl and
[L1394] [54:28.08] I screw up my courage and ask her if we
[L1395] [54:31.60] would be exclusive at the time we the
[L1396] [54:33.60] phrase we used was going steady and she
[L1397] [54:36.08] looked at me and said And you know, she
[L1398] [54:38.56] was 16. She had dated other guys and
[L1399] [54:41.20] thought we were pretty young. And she
[L1400] [54:42.64] said, "Well, Dave, you're such a nice
[L1401] [54:44.48] guy. I don't know how to say no." For
[L1402] [54:46.56] me, as a logical person, I don't know.
[L1403] [54:48.96] Sounded like a yes. And so I hugged her
[L1404] [54:51.52] and said, "Great." And so she uh she in
[L1405] [54:55.20] her mind, she thought, "Well, I'll let
[L1406] [54:56.72] him down gently later." But we've been
[L1407] [54:58.72] married 59 years now, and she she hasn't
[L1408] [55:03.20] let me down yet. So that was a case
[L1409] [55:04.96] where optimism uh paid off.
[L1410] [55:07.20] >> I think everyone that hears a a healthy
[L1411] [55:10.24] relationship for that long, they might
[L1412] [55:11.92] wonder how you did it.
[L1413] [55:13.60] >> I used to tell people uh you know if you
[L1414] [55:16.56] go to if you go to weddings, the
[L1415] [55:18.48] marriage vows are really great, right?
[L1416] [55:20.96] But nobody can remember their wedding
[L1417] [55:22.08] vows. I used to say remember your
[L1418] [55:23.12] wedding vows, but nobody remembered
[L1419] [55:24.08] that. So we boiled it down to nine magic
[L1420] [55:26.48] words and it's just three sentences and
[L1421] [55:28.88] they start IU, I got to say all three
[L1422] [55:31.52] and it's I was wrong. you were right. I
[L1423] [55:34.80] love you. Okay, those are the those nine
[L1424] [55:37.20] words. And this applies to both both
[L1425] [55:40.40] partners in a relationship, not just one
[L1426] [55:42.64] partner. Uh but yeah, if you can say
[L1427] [55:44.96] them all and no substitutions, I was
[L1428] [55:46.64] wrong, you're right, you're a jerk. You
[L1429] [55:48.08] know, you can't do that. It's if you can
[L1430] [55:50.32] remember those nine words, that can help
[L1431] [55:51.68] you have a a long relationship like uh
[L1432] [55:54.96] my wife and I have. And then last
[L1433] [55:57.44] question for you, like knowing
[L1434] [55:59.20] everything you know now from your
[L1435] [56:00.88] career, if you could go back to yourself
[L1436] [56:03.36] when you had just entered the industry
[L1437] [56:05.76] and give yourself advice, what would you
[L1438] [56:08.08] say?
[L1439] [56:09.44] >> I mean, I think when I got here because
[L1440] [56:12.08] you know the imposttor syndrome, I was a
[L1441] [56:14.32] UCLA
[L1442] [56:15.92] graduate student and suddenly I'm a
[L1443] [56:17.36] Berkeley professor. So that just doesn't
[L1444] [56:19.36] seem like that was very intimidating.
[L1445] [56:22.16] But I after a while I just thought well
[L1446] [56:24.16] I'm probably not gonna get tenure so I
[L1447] [56:25.60] should just have a good time. So I think
[L1448] [56:26.96] I already I already had a right attitude
[L1449] [56:31.52] about it. I think that first year I
[L1450] [56:33.68] think it it was very stressful for my
[L1451] [56:36.48] while I was trying to handle the
[L1452] [56:38.32] imposttor syndrome and be a Berkeley
[L1453] [56:39.92] professor but I think after that I
[L1454] [56:41.44] handled it pretty well. I you know I I
[L1455] [56:44.00] did all the things with the kids and
[L1456] [56:45.20] stuff. So uh there's a version of that
[L1457] [56:48.16] question is like is there anything I
[L1458] [56:49.76] would do over again? There's one thing I
[L1459] [56:51.44] would have I was chair of the u of this
[L1460] [56:55.36] the architecture community the sig arch
[L1461] [56:57.68] as it's called and they have an annual
[L1462] [56:59.44] conference of the year and I was this
[L1463] [57:02.24] was in the 1990s I think I was the chair
[L1464] [57:06.88] and what I wasn't aware is at these
[L1465] [57:09.44] conferences there were men who were
[L1466] [57:11.20] harassing young women at this uh
[L1467] [57:14.00] conference I just didn't think you know
[L1468] [57:18.16] people like you know young people people
[L1469] [57:21.04] like me nobody would do that only an
[L1470] [57:23.36] idiot would do that can't possibly be
[L1471] [57:25.20] happening but it was happening and I
[L1472] [57:27.12] wish I somebody had said something to me
[L1473] [57:29.92] about it uh and because I would have I
[L1474] [57:33.04] would have straightened out any man
[L1475] [57:34.72] doing I would have threatened his life
[L1476] [57:37.20] if he were to do that today the only
[L1477] [57:39.44] comforting thing is Serita a who is a
[L1478] [57:42.96] famous computer architect uh she said
[L1479] [57:45.60] she also was not aware that that was
[L1480] [57:47.84] going on it became clear later you know
[L1481] [57:50.32] I mean uh uh five or 10 years later it
[L1482] [57:52.96] became more clear that this was going on
[L1483] [57:54.40] and there were mechanisms but that's the
[L1484] [57:56.48] one thing I wish you know if I could go
[L1485] [57:58.40] back in time I would have figured that
[L1486] [58:01.36] out and I would have straightened men
[L1487] [58:03.68] out who were doing that and they
[L1488] [58:05.68] wouldn't that would have stopped I
[L1489] [58:07.04] believe that would have stopped them
[L1490] [58:08.48] >> yeah [laughter]
[L1491] [58:10.16] thank you so much for your time today I
[L1492] [58:11.76] really appreciate it
[L1493] [58:13.04] >> all right and thanks for the interview
[L1494] [58:15.28] >> hey thank you for watching this podcast
[L1495] [58:16.88] if you liked it and you want to see the
[L1496] [58:18.32] show grow Please support with a comment
[L1497] [58:20.72] or a like. Also, if you have any
[L1498] [58:23.28] recommendations for people you want me
[L1499] [58:24.96] to bring on, please drop a comment.
[L1500] [58:27.60] Guests like Barbara Liskoff, Mike
[L1501] [58:29.76] Stonereaker, Mark Brooker, these were
[L1502] [58:32.24] all people that I brought on because
[L1503] [58:34.16] someone left a comment. On another note,
[L1504] [58:36.48] aside from the podcast, I'm working on
[L1505] [58:38.32] building the ergonomic keyboard that I
[L1506] [58:40.24] wish existed. Here's a glance at the
[L1507] [58:42.40] prototype. It's a split keyboard, so
[L1508] [58:44.64] there's two sides. um this isn't the
[L1509] [58:46.88] case, but yeah, we launched on
[L1510] [58:48.32] Kickstarter and we hit our goal within 8
[L1511] [58:50.56] hours of launching. I really appreciate
[L1512] [58:52.32] it if you were one of the people who
[L1513] [58:53.68] grabbed one of the early units. Um we're
[L1514] [58:56.16] now working on the long journey of
[L1515] [58:57.84] building the tooling now and so if you
[L1516] [58:59.60] still want to pick one up, I've left the
[L1517] [59:01.68] late pledges open on Kickstarter, so you
[L1518] [59:04.32] can grab one there. I'll put a link in
[L1519] [59:05.92] the description. Thank you again for
[L1520] [59:08.24] watching the podcast and I'll see you in
[L1521] [59:10.48] the next
