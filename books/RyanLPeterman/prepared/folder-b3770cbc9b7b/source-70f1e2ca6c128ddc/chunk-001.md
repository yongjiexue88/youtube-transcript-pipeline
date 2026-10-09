Chunk 1; segments 1–364. 

# Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura

Source ID: source-70f1e2ca6c128ddc
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lean_Handwritten_Math_Will_Change_Dramatically_Leonardo_de_Moura_en.txt
Video: https://www.youtube.com/watch?v=KzdYKeAqWhY

[L10] [00:00.40] LLMs paired with the lean proof
[L11] [00:02.48] assistant have led to breakthroughs in
[L12] [00:04.40] competition math and more recently the
[L13] [00:07.12] verification of frontier math results.
[L14] [00:10.32] Lean is a critical part of this process
[L15] [00:12.64] because it helps validate the candidate
[L16] [00:14.72] proofs the LLM spits out. In this
[L17] [00:16.80] conversation, I asked the creator of
[L18] [00:18.40] LEAN about how it works [music] and how
[L19] [00:20.56] it will affect the future of math and
[L20] [00:22.72] software verification. Could that be the
[L21] [00:24.88] end of handwritten math? Here's the full
[L22] [00:28.48] episode.
[L23] [00:32.88] There's this famous Dysterra quote I
[L24] [00:34.72] want to start the conversation with.
[L25] [00:36.16] It's that, you know, program testing can
[L26] [00:38.64] be used to show the presence of bugs,
[L27] [00:41.36] but never to show their absence. And in
[L28] [00:44.48] my understanding is that lean and
[L29] [00:46.24] formalizing proofs can be used to show
[L30] [00:49.20] the absence of bugs. And so in your
[L31] [00:52.64] words, what is lean and how do people
[L32] [00:55.84] use it to show bugs can't occur in
[L33] [00:58.08] programs?
[L34] [00:59.20] L is a programming language. You can
[L35] [01:01.28] write code, but you can also write
[L36] [01:03.36] proofs. You can reason about your code.
[L37] [01:05.84] You can write state properties about
[L38] [01:08.00] your code and prove them. LIN gives you
[L39] [01:10.96] machine checkable proofs. You can check
[L40] [01:13.84] your proofs and get absolute assurance
[L41] [01:15.92] they are correct. You have uh many
[L42] [01:18.56] checkers, independent checkers. But you
[L43] [01:21.84] should view LIN as a platform. You can
[L44] [01:24.48] write code. You can write properties
[L45] [01:26.96] about your codes and you can prove them.
[L46] [01:30.56] >> So could you give a concrete example?
[L47] [01:32.56] Because when I think of a proof, I think
[L48] [01:35.68] of what I learned in math. But then how
[L49] [01:38.56] do you couple that with the software
[L50] [01:40.96] that we write?
[L51] [01:42.32] >> Yeah, it's a great question. It's not
[L52] [01:44.48] that different from math proof. L is
[L53] [01:46.80] actually very popular for math. But for
[L54] [01:49.28] for software verification, right? uh
[L55] [01:53.36] there are two
[L56] [01:55.92] very different use cases. You can reason
[L57] [01:58.48] about lin programs. LIN is a programming
[L58] [02:00.40] language. You can write programs in ling
[L59] [02:02.16] itself.
[L60] [02:03.76] Then
[L61] [02:05.36] a link program is not that different
[L62] [02:06.96] from a definition you have in math. The
[L63] [02:10.40] techniques are very similar. But when
[L64] [02:13.44] you if you want to verify programs
[L65] [02:15.28] written in a different programming
[L66] [02:16.56] language that basically two different
[L67] [02:18.80] approaches.
[L68] [02:20.32] One of them they translate it's called
[L69] [02:22.08] shallow embedding. They translate for
[L70] [02:24.56] rust. This happens today. We have a tool
[L71] [02:26.72] called that maps rust into ling and you
[L72] [02:30.88] can verify the ling translation right.
[L73] [02:35.04] uh and there's another technique called
[L74] [02:36.56] jeep badging where you have the
[L75] [02:38.72] semantics you you write a semantics of
[L76] [02:41.28] the programming language of C in ling
[L77] [02:44.48] and now you have a you have a data
[L78] [02:46.56] structure that represents a C program
[L79] [02:49.52] and you can state properties about it is
[L80] [02:52.40] almost like your programs become lean
[L81] [02:55.12] objects right that you can reason about
[L82] [02:58.40] >> to make it really concrete to give
[L83] [03:00.00] someone a sense of you know here's this
[L84] [03:02.24] thing I want to prove about a simple C
[L85] [03:04.72] program maybe like no buffer overrun or
[L86] [03:08.32] something like that.
[L87] [03:09.68] >> What's a step by step where we could use
[L88] [03:11.92] lean to prove that?
[L89] [03:13.84] >> Yeah. Yeah. Let's get array. You're
[L90] [03:17.60] trying to access an array in C. You want
[L91] [03:19.76] to make sure the index is in bounds.
[L92] [03:22.24] You're not accessing elements that your
[L93] [03:24.48] array for example has 10 elements.
[L94] [03:26.72] You're not trying to access elements 11.
[L95] [03:30.16] Right?
[L96] [03:31.36] uh basically can you can write that you
[L97] [03:33.76] can write in link that uh the value of i
[L98] [03:37.60] at this point in your program is going
[L99] [03:40.00] to be greater than or equal to zero and
[L100] [03:42.40] less than 10 right you you can write
[L101] [03:45.84] that as a mathematical statement right
[L102] [03:49.36] uh another way to view is that if you
[L103] [03:52.80] can express in math what you care about
[L104] [03:56.32] your program you can verify using l
[L105] [04:00.00] Right? That's another way to view it.
[L106] [04:02.32] >> So I have my my C source files and then
[L107] [04:05.12] somehow there's an equivalent lean proof
[L108] [04:08.24] that's almost like metadata on top of
[L109] [04:10.64] the C program.
[L110] [04:11.68] >> Yes.
[L111] [04:12.32] >> And that's a line by line proof and lean
[L112] [04:14.40] will go
[L113] [04:15.28] >> yes and check.
[L114] [04:16.64] >> Exactly. People will build automation
[L115] [04:19.76] for automating the process. uh they're
[L116] [04:22.88] going to use techniques like triples
[L117] [04:25.52] that says like uh we have a precondition
[L118] [04:29.28] some mathematical facts that should be
[L119] [04:31.12] true before executing that statement the
[L120] [04:34.40] statement and what is true after right
[L121] [04:37.92] and then we will have a lot of
[L122] [04:39.44] automation to to process makes your
[L123] [04:42.24] proof modeler right I mean uh complexity
[L124] [04:45.36] is a challenge in software verification
[L125] [04:48.88] handling the complexity is a big deal
[L126] [04:51.76] And there were all all these frameworks
[L127] [04:53.92] for very fine programs. They're trying
[L128] [04:55.60] to manage the complexity make your
[L129] [04:57.92] proofs modeler
[L130] [05:00.48] even with AI now AI can prove things
[L131] [05:02.72] automatically for us but they have to be
[L132] [05:05.12] modeler to the proofs if you want them
[L133] [05:07.60] to scale
[L134] [05:08.96] >> and what you're saying sounds similar to
[L135] [05:10.48] in software where you have to write it
[L136] [05:12.56] cleanly. It needs to be easy to edit and
[L137] [05:15.76] reason about. So it's almost like a
[L138] [05:18.32] second software layer on top of the
[L139] [05:20.24] software. Yes. Yes. You can view this
[L140] [05:23.04] way. You can also flip and imagine a
[L141] [05:26.40] future where you're writing the what you
[L142] [05:30.16] want mathematically precisely and AI
[L143] [05:33.84] synthesizing the codes and approve that
[L144] [05:37.36] the code that was synthesized meets your
[L145] [05:40.16] specification right.
[L146] [05:42.40] >> Oh interesting. So you could start by
[L147] [05:45.44] writing what you want to be true and
[L148] [05:48.64] then
[L149] [05:49.36] >> ask the AI please. AI is going to just
[L150] [05:51.52] go and hammer at it till the lean proof
[L151] [05:54.32] says you're good.
[L152] [05:55.92] >> Yes. Yes. It feels like science fiction.
[L153] [06:00.32] Six months ago I would say this is
[L154] [06:01.84] science fiction but for example now a
[L155] [06:04.72] colleague of mine Kin Morrison
[L156] [06:07.60] she a few months ago she started a
[L157] [06:09.60] project I thought was was six months ago
[L158] [06:12.48] I would say it's not possible at all.
[L159] [06:14.56] She said uh we have Z lib this s this
[L160] [06:18.08] compression library written in C and she
[L161] [06:21.52] said she creates a very complicated
[L162] [06:24.08] prompt for AI saying I want you to
[L163] [06:26.64] translate to ling
[L164] [06:28.96] ensure the lan version passes the test
[L165] [06:32.24] suite for for zib then I want you to
[L166] [06:35.68] prove that if you compress data and you
[L167] [06:39.36] decompress you get the original data
[L168] [06:42.08] back it's a really strong property right
[L169] [06:46.16] a and believe it or not they after one
[L170] [06:49.44] week succeeded doing the whole thing and
[L171] [06:52.64] now it's just asking to optimize the
[L172] [06:54.80] codes
[L173] [06:56.72] but you cannot break the proofs I mean
[L174] [06:58.80] you have to keep still proved all the
[L175] [07:01.28] properties you care about I mean
[L176] [07:03.28] compressing and decompressing getting
[L177] [07:05.44] the data back is a really important
[L178] [07:08.48] property for a compression engine right
[L179] [07:12.96] yeah This is enrich now. I mean, it's
[L180] [07:15.92] surreal. I mean,
[L181] [07:17.12] >> it's I mean, it's crazy. And I hear in
[L182] [07:20.00] the industry a lot of people, they use a
[L183] [07:24.48] really comprehensive test suite coupled
[L184] [07:26.96] with AI to do some really amazing
[L185] [07:30.16] rewrites cuz they have some more
[L186] [07:33.44] confidence that the rewrite is accurate
[L187] [07:35.84] and the AI can check itself. And it
[L188] [07:38.32] sounds like a specification is even
[L189] [07:42.40] better than a comprehensive test suite.
[L190] [07:45.44] >> Yes. Yes. Because with well your quotes
[L191] [07:48.40] from Dystra captures perfectly, right?
[L192] [07:51.04] With a test suites you can show the
[L193] [07:53.20] presence of bugs but not the absence.
[L194] [07:56.08] It's almost like with the a good test
[L195] [07:58.40] suite is you you may say well probably
[L196] [08:00.80] there are no bugs here but is you you
[L197] [08:05.44] may have a really corner case that's not
[L198] [08:07.92] covered by your test suite but with a
[L199] [08:10.00] proof you're covering all possible cases
[L200] [08:14.08] a and it connects so property based
[L201] [08:18.08] testing is really popular now people are
[L202] [08:20.80] writing properties they want to to
[L203] [08:24.00] ensure they are true but they are
[L204] [08:26.64] checking with testing, right? But now we
[L205] [08:29.28] can prove them and you say, "Look,
[L206] [08:31.28] there's no point testing anymore. I
[L207] [08:33.12] prove it."
[L208] [08:34.56] >> It seems like having a a well-written
[L209] [08:38.64] specification is a superset of a test
[L210] [08:41.76] suite. But in terms of the human labor
[L211] [08:45.84] required to create a a reasonable test
[L212] [08:49.36] suite versus a reasonable specification
[L213] [08:52.80] um you know how much more work is it to
[L214] [08:55.76] come up with a great specification
[L215] [08:58.80] >> varies a lot I mean uh the programs
[L216] [09:04.24] in many it's not uncommon for someone to
[L217] [09:07.84] start developing a piece of software and
[L218] [09:09.76] they don't know exactly what the spec is
[L219] [09:12.96] right but you know properties property
[L220] [09:15.36] usually their properties are very clear
[L221] [09:17.44] in your mind another thing that I tell
[L222] [09:19.92] people to keep in mind that inefficient
[L223] [09:22.88] program can give you this specification
[L224] [09:25.92] usually writing in efficient program is
[L225] [09:29.12] way easier than writing the super
[L226] [09:31.44] efficient one that does has many clever
[L227] [09:34.48] tricks you can write a very this is what
[L228] [09:38.56] I want in a very naive way and you Ask
[L229] [09:41.92] the AI look generate efficient version
[L230] [09:45.12] and optimize and prove that it's
[L231] [09:46.96] equivalent to my inefficient one.
[L232] [09:51.28] There are many scenarios. I mean I will
[L233] [09:53.60] not say this specifications are always
[L234] [09:55.92] easy to come up with but properties
[L235] [09:59.68] usually the developers have good ideas
[L236] [10:01.84] about properties they care about.
[L237] [10:04.96] uh as inefficient programmer is a spec
[L238] [10:08.56] rights you can view as a specification
[L239] [10:11.92] and the technology form of verification
[L240] [10:14.80] complements testing rights I think your
[L241] [10:18.08] code from extra captures perfectly
[L242] [10:21.52] >> and I think I saw this on Twitter
[L243] [10:23.36] because uh Jane Street was more heavily
[L244] [10:26.96] investing in formal verification
[L245] [10:28.96] >> yes
[L246] [10:29.28] >> and I read their post and they talked
[L247] [10:30.88] about this I think it was a sell for
[L248] [10:33.84] some software that was entirely formally
[L249] [10:37.20] verified.
[L250] [10:38.16] >> Yes.
[L251] [10:38.80] >> And the main drawback to why it wasn't,
[L252] [10:42.48] you know, how much more time would it
[L253] [10:44.32] take writing a program versus verifying
[L254] [10:47.68] it?
[L255] [10:48.48] >> Your example cell 4 is a great example.
[L256] [10:51.44] This was a major milestone. It's a micro
[L257] [10:54.16] kernel. They verified done manually was
[L258] [10:57.36] before AI. This project was done before
[L259] [10:59.84] AI was a big deal.
[L260] [11:02.48] And it's a lot. The cost is super
[L261] [11:04.40] expensive, right? At AWS, we have been
[L262] [11:07.20] using formal verification for a decade,
[L263] [11:10.56] but only for the super safety critical
[L264] [11:13.60] components because it's expensive until
[L265] [11:16.32] now, right? With AI, it changes the
[L266] [11:19.12] game.
[L267] [11:21.44] You have to come up with the spec. But
[L268] [11:23.04] this is not not the most painful part.
[L269] [11:26.16] The most painful part is to develop the
[L270] [11:29.20] proofs manually if you have to before.
[L271] [11:31.84] for AI and maintain the proofs as you
[L272] [11:34.96] change the codes. Imagine your
[L273] [11:37.84] I I've seen people complaining that oh I
[L274] [11:40.32] I change the program right now I have a
[L275] [11:43.36] bunch of failures in my test suite and I
[L276] [11:46.08] have to patch go one by one imagine with
[L277] [11:49.44] proofs you is the same process you have
[L278] [11:51.28] to fix the proofs uh sometimes you don't
[L279] [11:54.88] remember anymore why
[L280] [11:57.60] the pro what what's the story behind
[L281] [11:59.92] this proof is a lot but we AI is
[L282] [12:03.68] extremely good at proving
[L283] [12:06.64] uh writing formal proofs, maintaining
[L284] [12:09.36] formal proofs. For example, yesterday I
[L285] [12:13.12] was
[L286] [12:15.52] changing something. I want to modify
[L287] [12:18.00] some proofs for technical reasons and I
[L288] [12:21.12] I didn't even know what the proofs were
[L289] [12:22.64] about. Someone else wrote then I said,
[L290] [12:24.64] "Look, I want you to I asked the write
[L291] [12:28.08] these proofs without using this feature
[L292] [12:30.00] because I'm going to change it. I don't
[L293] [12:31.84] want to break the libraries
[L294] [12:34.56] instantaneous. It came up with the new
[L295] [12:36.40] proofs for me. I mean it's really good
[L296] [12:39.81] [snorts] and this is crucial for making
[L297] [12:42.72] formal verification mainstream because
[L298] [12:45.12] otherwise maintaining the proofs. It was
[L299] [12:48.32] almost like if your program took x
[L300] [12:52.00] amount of time to do the formal
[L301] [12:54.32] verification in the past would take 10x.
[L302] [12:57.04] That would be normal.
[L303] [13:00.24] But imagine if your program is changing.
[L304] [13:02.48] That's something that's really common.
[L305] [13:05.12] Now you have to keep maintaining the
[L306] [13:07.68] proofs too. It's a lot of work. But AI
[L307] [13:12.24] eliminates uh this pain for us.
[L308] [13:15.36] >> You mentioned that lean is because I I
[L309] [13:18.32] hear it as a proof assistant. But
[L310] [13:20.64] >> and then you also said it's a
[L311] [13:22.40] programming language. Yeah.
[L312] [13:23.76] >> Is that typical for proof assistants to
[L313] [13:25.84] be both a programming language and a
[L314] [13:29.20] proof assistant? Some of them especially
[L315] [13:31.68] the ones that are based on dependence
[L316] [13:33.20] type theory
[L317] [13:35.28] uh they are like rock and le are
[L318] [13:37.92] programming languages and proof
[L319] [13:39.52] assistance right I mean uh uh you can
[L320] [13:42.56] write definitions
[L321] [13:44.56] uh like uh when we're defining concepts
[L322] [13:47.76] in math but some of these definitions
[L323] [13:49.84] can be programs I mean and you have
[L324] [13:52.48] types you have structures
[L325] [13:55.84] is a programming language but is in that
[L326] [13:58.56] the family of called functional
[L327] [14:00.40] programming language I mean is a
[L328] [14:02.16] specific kind of programming language
[L329] [14:04.08] for people that are familiar with
[L330] [14:05.84] programming languages like Haskell ling
[L331] [14:09.04] is close to Haskell I mean but with the
[L332] [14:11.84] support for proofs that that's a way to
[L333] [14:14.56] to view ling
[L334] [14:16.16] >> are there major use cases where people
[L335] [14:17.84] use it as programming language but not
[L336] [14:19.84] as a proof assistant
[L337] [14:21.60] >> well the first big use case is link
[L338] [14:23.68] implemented in l we have many of our
[L339] [14:26.00] tooling is implemented in l like the the
[L340] [14:29.12] documentation authoring system called
[L341] [14:31.36] vers is implemented in ling. The build
[L342] [14:33.92] system that's called lake. It's like
[L343] [14:36.00] ling make lake is implemented in ling.
[L344] [14:39.60] Uh at AWS we have a compiler for AI
[L345] [14:43.84] acceler accelerators.
[L346] [14:46.24] It's half million lines of ling and it's
[L347] [14:48.16] using ling as a programming language.
[L348] [14:50.40] They're proving some properties about
[L349] [14:52.96] the program using ling. But the main
[L350] [14:55.52] goal is choose ling use ling as a
[L351] [14:57.84] programming language in this project.
[L352] [14:59.60] The proofs are like a a bonus right that
[L353] [15:02.56] you can get the proofs and find problems
[L354] [15:04.56] in the design.
[L355] [15:06.24] >> I think most people are familiar with
[L356] [15:08.56] programming languages and the tool
[L357] [15:10.72] chains they have and but um what are all
[L358] [15:14.00] the major components that you would need
[L359] [15:17.20] for a proof assistant?
[L360] [15:19.68] >> This is not that different. I mean if
[L361] [15:21.68] you're used to modern programming
[L362] [15:23.04] language like Rust the tooling for
[L363] [15:25.92] example lake is is our cargo right I
[L364] [15:29.28] mean uh you're going to open v visual
[L365] [15:31.76] studio codes same way and you're going
[L366] [15:34.24] to get all the intellisense
[L367] [15:36.80] one big difference is that we have
[L368] [15:38.48] something called the info view in ling
[L369] [15:41.36] your screens usually is going to be
[L370] [15:42.88] split in two you have your your file on
[L371] [15:47.20] the right hand side you have the info
[L372] [15:49.04] view that tells you information about
[L373] [15:50.72] your proofs, about your codes, uh is
