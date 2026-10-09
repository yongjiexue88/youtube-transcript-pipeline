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
[L374] [15:56.16] giving you constant feedback about your
[L375] [15:59.20] developments. That's basically the main
[L376] [16:01.60] difference, but the tooling, VS code,
[L377] [16:04.88] everything works the same way. I mean,
[L378] [16:07.28] >> it seems like a programming language is
[L379] [16:09.04] the the fundamental layer and then
[L380] [16:11.12] there's some additional layer on top
[L381] [16:12.88] that keeps
[L382] [16:13.92] >> track. Good question. uh uh in L you
[L383] [16:18.00] have definitions that are your program
[L384] [16:19.52] but you have theorems statements like
[L385] [16:22.88] you're going to say for example uh
[L386] [16:24.56] factorial is always greater than or
[L387] [16:27.04] equal to zero or something like that or
[L388] [16:30.08] if you add two even numbers you get even
[L389] [16:33.04] number you can write statements like
[L390] [16:35.36] that and immediately you can write
[L391] [16:39.52] actually a program that's the proof
[L392] [16:42.64] but most people don't do that they go
[L393] [16:44.80] into something called tactic modes. You
[L394] [16:47.84] can view as a domain specific language
[L395] [16:49.68] for writing proofs in ling. When you
[L396] [16:52.32] write by it switches to this domain
[L397] [16:54.80] specific language and you can you have
[L398] [16:57.92] steps like simplify my goal
[L399] [17:01.68] the state of my proof. You can say oh
[L400] [17:04.72] apply this writing step apply for
[L401] [17:07.84] example we know that x plus 0= x. You
[L402] [17:10.32] can ask ling apply this writing and
[L403] [17:13.04] you're going to see in the info view the
[L404] [17:15.12] state of the proof changing you you get
[L405] [17:18.32] immediate feedback and you get this
[L406] [17:20.72] feeling that you said you you keep
[L407] [17:23.52] telling applying transformations to your
[L408] [17:26.32] proof step by step you can see what's
[L409] [17:28.56] happening until you get no goals left
[L410] [17:32.16] and you are done the proof's complete
[L411] [17:34.48] and some people view this process as a
[L412] [17:37.12] game I I have users that told You built
[L413] [17:40.96] my favorite computer again for me.
[L414] [17:43.08] [laughter]
[L415] [17:45.04] >> That's funny. Is lean itself verified in
[L416] [17:49.04] lean?
[L417] [17:49.92] >> Lean is a massive program. You only have
[L418] [17:52.08] to trust the kernel. The kernel is where
[L419] [17:54.08] the proofs are checked. Lean itself is
[L420] [17:57.68] the kind of program that because there
[L421] [18:00.00] are so many new things we are adding.
[L422] [18:02.16] It's not even clear what is the
[L423] [18:03.76] specification. For example, what is the
[L424] [18:07.04] specification of a simplifier? You you
[L425] [18:09.44] can write general ideas but users they
[L426] [18:12.80] want to be able to customize the
[L427] [18:14.64] behavior. They keep asking they keep
[L428] [18:16.72] changing the specification all the time.
[L429] [18:18.96] I want this, I want that. No add this
[L430] [18:22.32] knob here. So it's really hard to have a
[L431] [18:25.60] full specification of L. But the kernel
[L432] [18:27.92] is possible to have a specification. We
[L433] [18:30.48] have a kernel. The kernel that comes
[L434] [18:32.64] with ling is not verified. But there are
[L435] [18:35.84] other kernels that you can use. One of
[L436] [18:38.88] them is implemented by Mario Kanedo.
[L437] [18:41.60] It's called Ling for Ling and it's
[L438] [18:44.00] implemented in ling and he's very fine
[L439] [18:46.08] is proving that this this kernel has
[L440] [18:48.32] been verified with respect to the
[L441] [18:50.96] semantics of ling. This is a cool
[L442] [18:53.44] project but for us having multiple
[L443] [18:57.44] kernels is the best way to ensure that
[L444] [19:00.40] your results are correct. I mean uh some
[L445] [19:03.12] users implemented their own kernels. We
[L446] [19:05.44] have kernels implemented in rust uh in
[L447] [19:08.40] different programming languages. Uh
[L448] [19:10.88] >> and when you say kernel what's what's
[L449] [19:12.96] the responsibility or what's the inputs
[L450] [19:15.20] and outputs of that portion?
[L451] [19:16.72] >> Yes. And l proof checking is type
[L452] [19:20.00] checking. This kernels they are type
[L453] [19:22.56] checking your programs. I mean basically
[L454] [19:25.52] you can export your lan developments.
[L455] [19:28.72] You got a big blob and you read this
[L456] [19:31.68] blob and they're going to check if
[L457] [19:35.52] when you say we have a proofing link
[L458] [19:37.28] basically you have a thumb that has a
[L459] [19:39.28] type and you're checking if the type of
[L460] [19:41.76] this T matches the type that you claim
[L461] [19:45.60] it has. For example, the example of the
[L462] [19:47.76] even numbers. This is a typing link
[L463] [19:50.40] saying that's uh uh the sum of two even
[L464] [19:53.36] numbers is a even number.
[L465] [19:56.56] You can write you can view that it is
[L466] [19:58.48] exactly a typing link and the proof what
[L467] [20:01.84] the kernel is checking is whether the
[L468] [20:03.76] type of the proof matches the type you
[L469] [20:06.40] claim this thumb has I mean and the the
[L470] [20:09.68] console will check you do this type
[L471] [20:11.44] checking
[L472] [20:13.36] uh the kernels vary between
[L473] [20:18.40] high performance kernel should it's like
[L474] [20:20.72] 5,000 lines of code I mean the goal of
[L475] [20:23.12] the should be something you can write
[L476] [20:26.00] yourself.
[L477] [20:27.60] Uh of course sometimes people put bells
[L478] [20:30.00] and whistles like uh one thing concern
[L479] [20:34.72] people have is like okay
[L480] [20:37.76] but how do I know that I wrote fas
[L481] [20:41.84] in ling how do you know that when you
[L482] [20:45.20] exported it's really theorem it's not 2
[L483] [20:48.64] plus 2 equals four I mean uh and people
[L484] [20:52.40] some external kernels they write print
[L485] [20:55.04] printers I mean they will print the
[L486] [20:57.44] statements that has been proven all the
[L487] [20:59.60] dependencies
[L488] [21:01.12] you can have all the these fancy tools
[L489] [21:03.60] to make sure you're not being misled.
[L490] [21:07.04] >> Lean obviously it's so powerful and I
[L491] [21:10.24] see on social media all these amazing
[L492] [21:13.44] results from formal verification want to
[L493] [21:16.32] know you what are the top ones that you
[L494] [21:18.48] think of or top examples more recently
[L495] [21:21.44] that have impressed you that lean was
[L496] [21:23.84] able to accomplish? Well, there are so
[L497] [21:26.64] many I mean that I thought were was
[L498] [21:28.80] impossible for for example getting a
[L499] [21:30.72] gold medal in the international
[L500] [21:32.56] mathematical olympiad.
[L501] [21:35.04] A few years ago everybody thought was
[L502] [21:37.04] impossible. Now everybody they use it as
[L503] [21:40.40] a benchmark of a easy problem. They say
[L504] [21:42.72] oh this is like a IMO problem. I mean
[L505] [21:45.28] this is easy but it's not. I mean these
[L506] [21:48.16] are really challenging problems. Uh the
[L507] [21:51.28] other conjectures that people close
[L508] [21:54.00] using ling AI with ling also impresses
[L509] [21:58.48] me. Uh there's this unit distance
[L510] [22:02.32] conjecture for others. First open AI
[L511] [22:05.60] prove it using formal right was not
[L512] [22:10.08] formal and we have a system now in ling
[L513] [22:14.16] is a website where we call ling where we
[L514] [22:16.96] collect challenges.
[L515] [22:18.96] uh the same Kim Morrison saw this this
[L516] [22:21.68] this this
[L517] [22:23.68] proof open AI and she puts on Lo as a
[L518] [22:28.00] challenge say okay I want to see someone
[L519] [22:30.40] formalizing we knew it was huge to
[L520] [22:33.20] formalize
[L521] [22:34.88] it's serious math it depends on
[L522] [22:38.48] and Boris Alexi from openi he did his
[L523] [22:42.16] swim it's a one million line proof for
[L524] [22:44.80] for for whole proofing link for this
[L525] [22:46.96] conjecture uh We estimate I mean the the
[L526] [22:50.32] the ground math that is needed for the
[L527] [22:53.20] proof we knew it take months I mean for
[L528] [22:56.48] experts to do by hands. I mean
[L529] [22:59.36] >> uh how long did it take in that case
[L530] [23:01.20] like the time from when the proof came
[L531] [23:03.92] out to when the challenge was solved on
[L532] [23:05.84] the lean?
[L533] [23:06.72] >> I think what was one month?
[L534] [23:08.72] >> Yeah. And after Kim was a few I think
[L535] [23:12.56] less than two weeks after Kim puts as a
[L536] [23:15.84] challenge only vow I took I think two
[L537] [23:18.16] weeks to get the the or or less I mean
[L538] [23:21.36] >> that's that's insane.
[L539] [23:22.80] >> Yes. Yeah. Yeah.
[L540] [23:24.32] >> We talked about verifying programs but
[L541] [23:26.56] also there's using it just directly for
[L542] [23:29.12] mathematics like in this case.
[L543] [23:31.84] How popular is lean in in terms of um
[L544] [23:35.52] when you look at the users of lean? What
[L545] [23:38.08] percent are using it for software
[L546] [23:40.64] engineering? What percent are using it
[L547] [23:42.08] more for just direct math? Well,
[L548] [23:45.04] historically lean be got popular first
[L549] [23:48.24] with math, right? I mean know with the
[L550] [23:52.00] beginning of the le mathematical library
[L551] [23:54.24] in 2017
[L552] [23:56.56] we we had like a big project called
[L553] [23:59.04] liquid stencil experiments.
[L554] [24:01.76] Uh it started beginning of 2020. It was
[L555] [24:06.24] a big deal because it was to verify a
[L556] [24:09.28] result from a fields medalist. Per shows
[L557] [24:11.76] it is a result he was unsure about. He
[L558] [24:14.40] has not published it. uh uh he felt like
[L559] [24:18.32] this was one of the most important
[L560] [24:20.00] results in his career. He wanted to be
[L561] [24:22.96] sure it was correct. It was done
[L562] [24:25.44] manually. The verification
[L563] [24:28.16] uh was a big deal because the team that
[L564] [24:30.88] formalizes led by Yuan Kling
[L565] [24:34.32] they not only formalized the results
[L566] [24:37.12] without fully understanding they do not
[L567] [24:39.20] fully understand the the proof.
[L568] [24:42.08] uh but having this info view helped them
[L569] [24:44.64] guides them step by step
[L570] [24:47.60] they formalized and simplify the proof
[L571] [24:50.24] without fully understanding the proof is
[L572] [24:53.20] mindboggling right I mean how can you
[L573] [24:55.44] simplify a proof from one of the
[L574] [24:58.40] greatest living mathematicians without
[L575] [25:00.80] fully understanding it I mean but you
[L576] [25:02.80] you they manage to simplify it's almost
[L577] [25:05.76] like when people do factoring coding you
[L578] [25:07.76] start changing the codes
[L579] [25:10.24] is faster now But the program doesn't
[L580] [25:13.12] really know why. I mean, it felt like
[L581] [25:15.52] that. It's like you have a gut feeling.
[L582] [25:18.24] I mean, that's you're going the right
[L583] [25:19.84] direction.
[L584] [25:21.84] And this for us at the time, lots of
[L585] [25:24.80] people got excited about link the math
[L586] [25:26.80] community because of this project. it
[L587] [25:29.44] like it's shown that's not about
[L588] [25:31.84] verifying but enabling people to work
[L589] [25:34.16] together in large numbers because you
[L590] [25:36.96] can trust you don't need to trust
[L591] [25:39.28] someone else's proof right they can fill
[L592] [25:42.00] holes for you
[L593] [25:44.24] uh this was
[L594] [25:47.28] I mean what attracts a lots of attention
[L595] [25:49.28] from the math community then came Terren
[L596] [25:51.28] St. He starts using after this project.
[L597] [25:54.96] He has really cool projects with and
[L598] [25:57.92] without AI and he got addicted actually.
[L599] [26:01.92] I think the first time he used it said I
[L600] [26:04.32] don't think I'm going to do it again.
[L601] [26:06.48] The for proof one week later he had
[L602] [26:08.80] another project using ling and he did a
[L603] [26:12.00] new result he had. [laughter]
[L604] [26:13.44] >> When you say addicted you mean because
[L605] [26:15.04] that game that like completion engine.
[L606] [26:17.28] >> Yeah. Some people I I feel we feel like
[L607] [26:20.96] when I talk to professors that use link
[L608] [26:23.68] for teaching
[L609] [26:25.92] they tell me the class is more or less
[L610] [26:27.84] split. Some people love it, some people
[L611] [26:30.24] don't like. But people that like to
[L612] [26:33.76] problem solving, people that get medals
[L613] [26:36.40] in the IMO, they love because you get
[L614] [26:38.88] this excitement of solving. It's like a
[L615] [26:42.16] solving millions of really hard pseudoc
[L616] [26:44.88] problems, right? [laughter] And you can
[L617] [26:47.20] keep solving one and it's easy to get. I
[L618] [26:50.08] mean I'm a lean developer not a lean
[L619] [26:52.40] user but when you're developing ling I'm
[L620] [26:54.64] coding in ling and sometimes I have
[L621] [26:56.88] prove things is really easy to get
[L622] [26:59.76] addicted it gets lost proving things you
[L623] [27:03.28] get this bus every time you prove
[L624] [27:05.52] something [laughter]
[L625] [27:07.92] >> you mentioned the II gold medals how is
[L626] [27:11.20] lean used in that kind of uh I think
[L627] [27:14.08] maybe referring to alpha proof by deep
[L628] [27:16.48] mind or maybe something else
[L629] [27:18.08] >> yes deep mind because they got in 2024
[L630] [27:21.68] was a big surprise in 2024 they got a
[L631] [27:24.56] silver medal and now we have gold medals
[L632] [27:28.80] from startups like a harmonic by dance
[L633] [27:32.48] got a medal I never imagined by dance
[L634] [27:36.64] they they they're behind tick tock right
[L635] [27:40.40] I didn't even know they care about form
[L636] [27:42.40] math but they have a for math team they
[L637] [27:45.20] got medals also the approver is really
[L638] [27:47.60] good
[L639] [27:48.24] >> so how's it work let's say I mean
[L640] [27:49.76] there's a series of math problems lean
[L641] [27:52.80] is just used for verification right so I
[L642] [27:56.00] imagine there's other components there
[L643] [27:58.08] >> yeah there's the AI you can view it's
[L644] [28:00.80] like uh we have go that was very popular
[L645] [28:03.68] with AI the AI is playing the game I
[L646] [28:07.44] told you that many people see lens again
[L647] [28:11.12] it's the same I mean the AI is viewing
[L648] [28:13.12] lens again they have the statements of
[L649] [28:15.28] what you want to prove you have the buy
[L650] [28:18.16] keyword words. Now you have a blank
[L651] [28:21.04] fill. Make sure that you have no goals
[L652] [28:23.44] left, right? It keeps applying steps in
[L653] [28:26.08] this game and seeing the trans the state
[L654] [28:28.96] of the boards, right? That's the info
[L655] [28:31.04] view changing
[L656] [28:33.20] and the AI they use reinforcement
[L657] [28:35.36] learning for for for trying to get to to
[L658] [28:39.28] no goals left. They it's a single player
[L659] [28:42.48] game. Some people play together these
[L660] [28:45.36] days but yeah the AI is learning to play
[L661] [28:48.32] the game.
[L662] [28:49.28] >> So before we were talking about that
[L663] [28:51.36] game it kind of starts with the
[L664] [28:53.28] specification. So in that case then the
[L665] [28:56.56] problem is kind of the specification and
[L666] [28:59.20] then it
[L667] [29:00.40] >> the problem yeah you have basically for
[L668] [29:01.92] each problem in the international
[L669] [29:03.28] mathematical olympiad someone translates
[L670] [29:05.92] to ling the statements. It's super
[L671] [29:08.56] important to have the mathematical
[L672] [29:10.00] library because you want to be able to
[L673] [29:11.92] talk about the problems, right? For
[L674] [29:13.84] example, the problems uses the real
[L675] [29:16.16] numbers. You need a definition in ling
[L676] [29:18.64] and we have it inside of math lib the
[L677] [29:20.72] ling mathematical library. So the first
[L678] [29:23.20] thing you have to be you have to be able
[L679] [29:25.28] to write the problems in lane and this
[L680] [29:29.04] now because of math li it's easy part uh
[L681] [29:33.68] and after that you have to provide the
[L682] [29:35.12] proofs I mean sometimes some problems
[L683] [29:37.92] you have to come up with a definition to
[L684] [29:40.40] some objects you have to to create that
[L685] [29:43.12] has some property but yeah that's how it
[L686] [29:46.72] is. I remember you said one of the first
[L687] [29:50.08] use cases of lean was um this fields
[L688] [29:53.44] medalist had this novel mathematics and
[L689] [29:56.96] then we use lean to verify it but can
[L690] [30:01.28] lean be used with LMS to generate novel
[L691] [30:04.96] mathematics or just verify existing is a
[L692] [30:08.80] good question I mean we don't see lots
[L693] [30:11.84] of evidence we see now evidence it can
[L694] [30:15.52] find novel proofs
[L695] [30:17.60] Right? But coming up with new
[L696] [30:21.04] mathematical concepts is still
[L697] [30:24.32] at the limits. Right? I mean right now
[L698] [30:28.00] in this line of all we have challenges
[L699] [30:29.92] where the AI has to come up with the
[L700] [30:31.84] objects
[L701] [30:33.44] uh themselves right I mean but this is
[L702] [30:36.64] people will keep investing in this area.
[L703] [30:39.12] I I do not batch against AI here. I
[L704] [30:42.64] mean, but we we right now we don't have
[L705] [30:44.96] evidence they can come up with new math.
[L706] [30:47.84] >> Open AAI, Enthropic, Cursor, and
[L707] [30:50.80] Verscell all use this product to make
[L708] [30:52.96] their lives better. And the problem it
[L709] [30:55.20] solves is when you're building SAS or an
[L710] [30:57.44] AI product and you want to sell to other
[L711] [30:59.76] companies, there's all these
[L712] [31:01.28] requirements you need to meet. There's
[L713] [31:03.20] SSO, there's SKIM, there's arbback,
[L714] [31:06.48] there's audit logs. These are all things
[L715] [31:08.32] that take time to integrate but aren't
[L716] [31:10.48] the main focus of your app. Work OS is
[L717] [31:12.64] an API layer that lets you meet all of
[L718] [31:14.56] these requirements in just a few lines
[L719] [31:16.72] of code. So let's say you have a new SAS
[L720] [31:19.12] product and you want to sell to other
[L721] [31:20.72] companies. Work OS will solve all of
[L722] [31:22.96] these critical feature gaps for you. You
[L723] [31:25.68] can check them out at workos.com to
[L724] [31:28.16] learn more and get started. And I
[L725] [31:30.32] appreciate them for supporting my work
[L726] [31:32.00] and sponsoring this podcast. when I see
[L727] [31:34.24] on Twitter this, you know, major
[L728] [31:36.24] conjecture, they made headway on it,
[L729] [31:38.64] it's that they made headway on
[L730] [31:40.80] confirming something
[L731] [31:42.08] >> or or disproving. They also have uh uh
[L732] [31:45.44] this 1 million lines, they shown the
[L733] [31:47.60] conjecture was false. They have a proof
[L734] [31:49.84] showing that it's false, [snorts] but
[L735] [31:51.76] but it's a formal proof. They did not
[L736] [31:55.92] came up with a new
[L737] [31:58.88] theory or anything like that. They're
[L738] [32:01.44] coming up with a proof, right? I mean,
[L739] [32:04.32] >> at what points would you say someone
[L740] [32:06.80] should evaluate formalizing something in
[L741] [32:09.92] lean?
[L742] [32:11.92] >> I I I think if if it's safe if it's
[L743] [32:15.12] critical or if you don't understand
[L744] [32:18.16] really well, I mean this is important
[L745] [32:20.32] part. I don't really understand. Anybody
[L746] [32:23.68] that went through the process of
[L747] [32:25.92] formalizing something understands the
[L748] [32:28.00] subject way better after that. I I
[L749] [32:30.96] almost feel like I remember when I was
[L750] [32:33.44] in college people would say wow after I
[L751] [32:35.92] implement this algorithm now I
[L752] [32:38.48] understand it much better.
[L753] [32:41.36] The next level is that you implement the
[L754] [32:43.36] algorithm you prove the properties you
[L755] [32:46.24] expect
[L756] [32:48.08] your level of understanding grows.
[L757] [32:50.56] Right? I mean, uh, another cool thing is
[L758] [32:53.68] that it enables you to to be much more
[L759] [32:58.00] bold on on your optimizations
[L760] [33:01.04] because sometimes
[L761] [33:02.96] I I've seen that all the time people
[L762] [33:05.12] fear implementing optimization because
[L763] [33:07.04] they don't really understand why the the
[L764] [33:08.88] piece of software works. They feel like
[L765] [33:12.16] if I do that still works and is faster,
[L766] [33:15.12] but they are not confident with proofs.
[L767] [33:18.40] you eliminate this discomfort, right?
[L768] [33:21.36] You you can prove it's again or the AI
[L769] [33:23.68] can prove for you or find a counter
[L770] [33:25.76] example. They're good at both things.
[L771] [33:29.76] But if you were to speculate or draw
[L772] [33:31.92] into the future, maybe 3 to 5 years from
[L773] [33:34.88] now, if the cost of formalizing things
[L774] [33:38.56] goes down, how does that change
[L775] [33:40.88] software? How does that change um you
[L776] [33:44.16] know, handwritten math? Oh, I think
[L777] [33:46.80] we've changed dramatically, right? Uh,
[L778] [33:49.28] we have to keep in mind the big labs,
[L779] [33:52.00] they only start training for formal
[L780] [33:54.80] verification lean very recently, right?
[L781] [33:58.00] Seriously, before that was like, oh, is
[L782] [34:01.12] in the data sets. I mean, you don't
[L783] [34:03.12] really have the the enforcement learning
[L784] [34:06.48] pipelines to to optimize.
[L785] [34:09.28] The behavior we see today that is
[L786] [34:11.20] already amazing will get way better in
[L787] [34:14.00] the future.
[L788] [34:15.92] uh the costs will reduce programming
[L789] [34:19.28] languages like ling and rock will become
[L790] [34:22.32] more mainstream because of that
[L791] [34:25.52] uh many people are not so in the past
[L792] [34:28.08] people say oh functional programming h I
[L793] [34:31.20] don't like it
[L794] [34:33.60] but if I'm not the one that's writing
[L795] [34:35.76] most of the codes anyway
[L796] [34:38.32] it doesn't really matter what matters
[L797] [34:40.16] are the specification level right
[L798] [34:43.84] doesn't really matter how the code has
[L799] [34:46.00] been written. Yeah, I think it will
[L800] [34:48.24] change a lot because of that. At least
[L801] [34:50.40] that's the direction we are pushing
[L802] [34:52.16] into.
[L803] [34:53.52] >> What about let's say you know 10 years
[L804] [34:56.56] from now lean is everything's going
[L805] [34:58.64] really well with lean. Is that the could
[L806] [35:02.32] that be the end of handwritten math or
[L807] [35:05.04] handwritten proofs?
[L808] [35:07.44] >> I think there will be always aspects
[L809] [35:09.36] that is handwritten. The
[L810] [35:12.88] some people like to make a proof look
[L811] [35:17.28] they they want to use the proof as an
[L812] [35:21.12] artifact. You communicate ideas to
[L813] [35:23.60] others. I can't imagine there will
[L814] [35:26.32] always be people polishing making them
[L815] [35:29.36] super easy to understand for for another
[L816] [35:32.48] human to communicate ideas to other
[L817] [35:35.04] people. There will always be people like
[L818] [35:37.36] that. The same way today we have people
[L819] [35:40.08] that uh we have machines that build
[L820] [35:43.12] furniture but people they like to to
[L821] [35:47.20] create them by hands and polish them
[L822] [35:50.00] make them perfect. This will always
[L823] [35:53.04] exist but it will be a mixture. I I
[L824] [35:56.56] would be surprised as if there's someone
[L825] [35:58.80] that's completely
[L826] [36:01.52] AI is not in their workflow somehow
[L827] [36:05.28] right I mean you'll be hybrids many
[L828] [36:08.40] hybrids some people don't like feel this
[L829] [36:11.60] uncomfortable about this future but for
[L830] [36:14.56] me super exciting because I view
[L831] [36:17.36] developing software is super painful
[L832] [36:19.68] process
[L833] [36:21.60] and with AI it's crazy how it bring you
[L834] [36:26.56] awareness of how many steps are just uh
[L835] [36:32.40] repetitive
[L836] [36:34.08] and there's no creativity you're just
[L837] [36:36.64] patching things and AI automates removes
[L838] [36:40.56] lots of this pain right I mean
[L839] [36:44.16] I cannot go back to
[L840] [36:47.28] I'm looking forward to this future you
[L841] [36:49.04] describe
[L842] [36:50.32] >> yeah I guess the thing that gives people
[L843] [36:52.88] I mean I'm guessing The discomfort is
[L844] [36:56.08] the worry that if it kept going then you
[L845] [36:59.84] know then we need less mathematicians or
[L846] [37:02.72] less computer scientists or something
[L847] [37:04.32] like that.
[L848] [37:06.08] People don't see that AI can bring more
[L849] [37:08.08] people. Uh uh there's also the
[L850] [37:10.88] specification. I mean some I've see
[L851] [37:13.52] people saying oh we are going to leave
[L852] [37:16.24] AI we'll come up with new math. But if
[L853] [37:19.84] there's no connection to our world,
[L854] [37:24.88] this is some alien thing that's going by
[L855] [37:27.44] itself. You need an interface. Uh for
[L856] [37:30.80] example, we want to build programs
[L857] [37:32.56] because you want to accomplish
[L858] [37:33.76] something. Uh just something whatever it
[L859] [37:37.04] is has an specification. There will be
[L860] [37:39.84] always humans in the loop saying this is
[L861] [37:41.76] what we need. This is what we want.
[L862] [37:44.80] Right? writing this interface
[L863] [37:47.12] interacting with the AI.
[L864] [37:49.92] The AI will have math libraries and
[L865] [37:52.40] everything to prove things about these
[L866] [37:56.00] these programs we are writing these
[L867] [37:57.68] artifacts this this whatever we are
[L868] [38:00.64] trying to build
[L869] [38:03.20] but we have to be able to interact these
[L870] [38:06.80] libraries we have to understand the
[L871] [38:08.80] abstractions that are there
[L872] [38:12.32] I I don't see humans being eliminated we
[L873] [38:14.56] are always going to be there in the
[L874] [38:16.00] interface
[L875] [38:17.60] righth uh we are telling them what we
[L876] [38:21.04] want right I mean uh specifications will
[L877] [38:24.64] be there I can see people always writing
[L878] [38:27.60] codes
[L879] [38:29.20] uh even another thing a lot of people
[L880] [38:32.48] like to write they say I love coding my
[L881] [38:35.20] interpretation is they love to write
[L882] [38:37.44] prototypes
[L883] [38:38.96] I this is fun this is the fun part to
[L884] [38:41.12] try a new idea but to transform it into
[L885] [38:44.16] a product is never fun I can tell you
[L886] [38:46.88] it's never fun
[L887] [38:49.04] and I can take over these parts and
[L888] [38:51.52] nobody really likes doing
[L889] [38:54.24] >> outside of lean. I I know you worked on
[L890] [38:56.80] the Z3 SMT solver
[L891] [38:59.60] >> and that sounds like a really difficult
[L892] [39:02.40] thing to build. So first, what is that
[L893] [39:05.04] solver in your words? And um yeah, how
[L894] [39:08.32] does it differ from a SAT solver?
[L895] [39:10.64] >> Yeah, I s long is going to be yes 20
[L896] [39:15.04] years ago. I started history. I mean
[L897] [39:17.44] when I joined Microsoft research
[L898] [39:20.56] uh yeah this is a semmit to solver is
[L899] [39:23.28] like a set solver but you have
[L900] [39:24.80] backgrounds theories like you [snorts]
[L901] [39:27.28] have support for arithmetic
[L902] [39:29.44] for arrays uh these are not random
[L903] [39:33.20] choices right this is because we use for
[L904] [39:36.24] doing test case generation in software
[L905] [39:38.56] for doing software verification
[L906] [39:41.20] link fully Z3 is fully automated is a
[L907] [39:44.24] push button although lens Z3 are called
[L908] [39:47.28] ton provers. They are completely
[L909] [39:49.60] different beasts. Z3 is fully automatic.
[L910] [39:52.96] Ling is interactive. Has automation but
[L911] [39:55.60] it's interactive.
[L912] [39:58.96] Tree is not a programming language. It's
[L913] [40:00.96] like you can do is more like a
[L914] [40:02.72] constraint solver.
[L915] [40:04.88] It turns out you can prove simple things
[L916] [40:06.96] about it. Not you cannot do advanced
[L917] [40:09.60] math with abstract math. you can solve
[L918] [40:13.52] constraints with with Z3.
[L919] [40:16.24] >> What's an example of the the inputs to
[L920] [40:18.88] this SMT solver and what you get out
[L921] [40:21.84] from it?
[L922] [40:22.80] >> Oh, I I can give you one. I mean that's
[L923] [40:24.88] even in the Z3 manual. Uh you can encode
[L924] [40:28.40] a sudoko problem as a set of constraints
[L925] [40:31.52] and you can ask Z3 to solve and will
[L926] [40:34.24] give you back the answer
[L927] [40:35.60] instantaneously.
[L928] [40:37.12] For real applications, Z3 was used very
[L929] [40:40.80] successfully for finding bugs in
[L930] [40:42.64] software. Uh people would convert for
[L931] [40:45.60] example suppose that you have a path in
[L932] [40:47.36] your code you know that's has a security
[L933] [40:51.12] vulnerability but you don't know which
[L934] [40:53.60] inputs to the program allow you to
[L935] [40:56.24] execute this path. you can convert that
[L936] [40:59.52] into a set of constraints that you send
[L937] [41:02.24] to Z3 and it will say unsatisfiable
[L938] [41:06.24] which means is impossible to execute
[L939] [41:08.16] this path and you are happy or it gives
[L940] [41:11.28] you back an example saying look with
[L941] [41:13.44] this inputs you're going to be able to
[L942] [41:15.36] do it I mean and people use it for doing
[L943] [41:19.52] software verification
[L944] [41:21.92] uh but because the problem becomes
[L945] [41:24.24] undecidable
[L946] [41:26.48] at that level you have many universal
[L947] [41:28.80] quantifiers for stating properties about
[L948] [41:30.96] your program, your pre and post
[L949] [41:33.28] conditions.
[L950] [41:35.36] The server has heristics
[L951] [41:38.00] and this was all before AI. The
[L952] [41:40.80] heristics were handcoded and they will
[L953] [41:43.20] always fail and for simple things people
[L954] [41:46.64] would be very happy with the push the
[L955] [41:48.32] fact that Z3 is push button. But when
[L956] [41:51.36] the property is not trivial, they would
[L957] [41:53.36] come back saying come on I know the
[L958] [41:55.60] proof. I mean why is it we can't find it
[L959] [41:58.32] that's why ling started I started ling
[L960] [42:01.04] to make sure that we would have a system
[L961] [42:04.24] that's really good for software
[L962] [42:05.76] verification right for Z3 was successful
[L963] [42:09.20] for finding bugs but not so much for
[L964] [42:13.04] software for proving the absence of bugs
[L965] [42:16.96] it was never super successful there but
[L966] [42:20.08] len uh was born to fill this gap
[L967] [42:25.20] >> you that undecidable but in practice in
[L968] [42:27.92] the real world if you run it does it
[L969] [42:31.20] typically terminate?
[L970] [42:32.64] >> Yeah. Yeah. Great question. Uh uh Z3
[L971] [42:36.16] goes the whole complexity level, right?
[L972] [42:38.72] You you have sets uh uh you have NP
[L973] [42:42.24] complete, P space complete, XP complete.
[L974] [42:46.00] You have the whole undecidable, right? I
[L975] [42:48.88] mean uh surprisingly even for sets you
[L976] [42:53.60] can write really tiny set problems that
[L977] [42:56.16] are really hard to solve. No set solver
[L978] [42:58.40] will solve them. But in practice, the
[L979] [43:02.32] problems we get for hardware
[L980] [43:04.56] verification,
[L981] [43:06.40] uh, uh, especially if you bound
[L982] [43:08.40] everything, you say, "Oh, I'm trying to
[L983] [43:09.92] look for a bug in the first 10 steps,
[L984] [43:13.12] right? Everything's bounded. You're not
[L985] [43:15.76] trying to prove, but you're trying to
[L986] [43:18.40] capture a class like a space of
[L987] [43:22.24] scenarios, right?
[L988] [43:24.80] They are very effective than there. I
[L989] [43:27.04] mean there I I I think the lesson there
[L990] [43:30.08] is that programs and hardware
[L991] [43:33.36] they're not correct by esoteric reasons
[L992] [43:36.32] right they they are correct for very
[L993] [43:39.12] simple reasons I mean that's why these
[L994] [43:41.44] tools are super effective they [snorts]
[L995] [43:44.80] um yeah but when you get to undecidable
[L996] [43:48.40] and you're trying to prove even if the
[L997] [43:52.08] property is not trivial there I mean it
[L998] [43:55.60] runs out of team I mean and they time
[L999] [43:58.40] out frequently and [snorts] sometimes
[L1000] [44:01.04] the there's a here a colleague of mine
[L1001] [44:04.56] here at Amazon I mean like chooses the
[L1002] [44:08.00] name proof instability
[L1003] [44:11.12] because sometimes if you change the
[L1004] [44:13.28] problem you just flip I mean you have A
[L1005] [44:16.48] and B you write B and A where B and A
[L1006] [44:18.96] are complicated formulas you may fail to
[L1007] [44:21.68] prove and when she was just trying to
[L1008] [44:24.72] maintain things proof would break if
[L1009] [44:27.44] using this kind of technology. But with
[L1010] [44:29.52] lean, she she switches to lean and super
[L1011] [44:33.60] smooth, right? Because you're
[L1012] [44:35.60] controlling uh the proof
[L1013] [44:38.32] >> in the lean case. Why is it so much more
[L1014] [44:41.76] efficient?
[L1015] [44:43.12] >> Your proof is basically you can view the
[L1016] [44:45.68] sequence of steps for solving the
[L1017] [44:47.52] problem.
[L1018] [44:50.00] In in Z3, you can view that you have
[L1019] [44:51.76] only one proof step. solve, right? I
[L1020] [44:56.24] mean, you're saying you have options to
[L1021] [44:58.56] solve flags, but you have very you don't
[L1022] [45:03.20] you cannot influence what Z3 is going to
[L1023] [45:06.24] do. It's much harder to influence this
[L1024] [45:08.96] kind of system.
[L1025] [45:11.28] In in ling you can if you want to give a
[L1026] [45:13.92] step super detailed stepbystep proof you
[L1027] [45:17.28] can you can use proof automation like is
[L1028] [45:20.00] available in Z3 but you can also break
[L1029] [45:22.96] it down step by step and the fact you
[L1030] [45:26.32] can do that humans can do it but the
[L1031] [45:29.36] happy surprise is that AI can do it
[L1032] [45:32.96] because now you can say step by step why
[L1033] [45:35.68] something is true. the AI can convince
[L1034] [45:39.28] lean that
[L1035] [45:41.52] it can provide a proof. I mean
[L1036] [45:44.32] >> when you were working on Z3 and lean,
[L1037] [45:47.36] what was the most technically
[L1038] [45:49.28] challenging
[L1039] [45:51.44] part that you had to build for for
[L1040] [45:53.60] either project?
[L1041] [45:55.20] >> I understand how much harder ling is in
[L1042] [45:58.96] comparison of Z3 this is or of a
[L1043] [46:01.52] magnitude harder. I mean uh one explan I
[L1044] [46:05.84] I talked to many colleagues about that
[L1045] [46:08.00] why I felt like L was so much harder I I
[L1046] [46:12.72] think it's the surface the interface
[L1047] [46:14.72] with humans is way
[L1048] [46:17.76] for the tree you have defined as a
[L1049] [46:20.24] language for it's called SMT lib it's
[L1050] [46:24.64] very simple language it's not meant for
[L1051] [46:27.60] humans it's meant for tools I mean it is
[L1052] [46:30.16] uses just the back ends of many
[L1053] [46:31.92] different tools
[L1054] [46:33.04] Someone's gener some program is
[L1055] [46:34.88] generating input for Z3 and people
[L1056] [46:38.32] expect a counter example or saying it's
[L1057] [46:41.84] impossible is unsatisfiable to come up
[L1058] [46:43.92] with the counter example. The interface
[L1059] [46:46.88] is really really simple, right? You you
[L1060] [46:50.40] can view it as a command line tool that
[L1061] [46:52.64] you pass this file on this very low
[L1062] [46:55.76] level language that's super easy to
[L1063] [46:57.68] parse and you come back with yes or no.
[L1064] [47:02.08] And l you have is a programming
[L1065] [47:03.84] language. You have libraries. You have
[L1066] [47:06.48] mechanisms. You have interactivity. You
[L1067] [47:08.32] have user interface. You have LSP. You
[L1068] [47:10.72] have build system. You have G. You have
[L1069] [47:12.72] that is so vast. I mean that's
[L1070] [47:18.40] another challenging part for me as I
[L1071] [47:22.00] mentioned Z3 was a back end.
[L1072] [47:24.80] The Z3 users
[L1073] [47:27.04] are very sophisticated software
[L1074] [47:30.08] developers people that speak the same
[L1075] [47:32.96] language I speak. It's way easy easier
[L1076] [47:37.20] to talk to people that speak your the
[L1077] [47:39.60] same language with L is completely
[L1078] [47:42.56] different, right? The B the first users
[L1079] [47:44.72] are all math math people. They have
[L1080] [47:48.00] completely different backgrounds,
[L1081] [47:49.36] different expectations, different
[L1082] [47:52.16] everything and a different community
[L1083] [47:55.60] and then you have people that want to
[L1084] [47:57.84] use L as a programming language. You
[L1085] [48:00.00] have I I I'm not a programming language
[L1086] [48:02.24] person. uh my background is automated
[L1087] [48:05.04] reasoning
[L1088] [48:06.64] and yeah it's different language
[L1089] [48:09.04] different expectations
[L1090] [48:11.20] >> was there like a a singular component
[L1091] [48:14.00] that was just really technically
[L1092] [48:17.52] challenging
[L1093] [48:18.40] >> I I told you that l implemented in ling
[L1094] [48:21.84] of course it was not always like that
[L1095] [48:24.64] right I mean it had to be implemented in
[L1096] [48:27.76] something else at the beginning the
[L1097] [48:30.08] switch from origin origally was C++.
[L1098] [48:35.44] The switch from CC C++ to lean was
[L1099] [48:38.80] extremely painful. Really really uh I
[L1100] [48:43.28] remember I literally want to cry when
[L1101] [48:46.72] when I managed to compile Ling. I was
[L1102] [48:49.76] just uh Sebastian and I at the time were
[L1103] [48:53.68] building L for together
[L1104] [48:56.64] and but this was before we had a
[L1105] [48:58.48] nonprofit for Ling. I remember calling
[L1106] [49:01.76] him and I said, "Wow, man. This is
[L1107] [49:05.28] insane."
[L1108] [49:06.80] Say, "Are you not excited?" He said, he
[L1109] [49:08.72] said, "Yes, I am. I am." I mean, super
[L1110] [49:11.28] excited. [laughter]
[L1111] [49:13.12] >> What What made that switch uh hard?
[L1112] [49:16.88] >> The first thing is is imagine you're
[L1113] [49:20.24] going to implement the language in
[L1114] [49:21.76] itself. The first thing you want is to
[L1115] [49:23.76] reduce to minimize number of features as
[L1116] [49:26.40] much as possible. So you want to
[L1117] [49:28.56] implement ling using barebones
[L1118] [49:31.68] features because you're going to have to
[L1119] [49:33.44] be able to compile it with itself.
[L1120] [49:36.48] uh uh then now you have like 100,000
[L1121] [49:40.96] lines more or less uh I don't know the
[L1122] [49:44.56] exact number but was between 100 around
[L1123] [49:47.20] 100,000 lines and you start trying
[L1124] [49:50.96] compile you fail the first you cannot
[L1125] [49:53.68] even compile the first file in the
[L1126] [49:55.44] pipeline that that more than 1,000 and
[L1127] [49:58.32] the first one fails then you fix the bug
[L1128] [50:00.88] you can compile the first one then you
[L1129] [50:03.76] can compile the second and you keep
[L1130] [50:06.16] moving and you're always finding
[L1131] [50:08.40] discrepancies between the new and the
[L1132] [50:11.68] old one. I mean and you're trying to
[L1133] [50:14.32] reconcile make things easier for the new
[L1134] [50:17.60] one.
[L1135] [50:18.48] because you want to replace the old one
[L1136] [50:20.88] and this process
[L1137] [50:24.88] is pain and l is a complicated language
[L1138] [50:26.88] because of these dependence types and so
[L1139] [50:28.80] on the proofs
[L1140] [50:31.28] for example
[L1141] [50:33.92] when you're implementing ling you you
[L1142] [50:35.60] still need some proofs there I mean
[L1143] [50:38.32] there are some basic proofs you need but
[L1144] [50:41.60] you have to construct these proofs
[L1145] [50:43.20] without no interactivity nothing bare
[L1146] [50:46.08] bones you have to provide the proof
[L1147] [50:47.76] time. It's almost like programming in
[L1148] [50:50.40] assembly. The proof uh this was also
[L1149] [50:53.68] super painful. I mean, my god.
[L1150] [50:56.24] >> Yeah. [laughter]
[L1151] [50:57.36] But it took Yeah. Many people thought we
[L1152] [51:01.36] we were going to fail. Sebastian and I
[L1153] [51:03.28] would not be able to do it.
[L1154] [51:05.44] >> 100,000 lines is a lot. Like all human
[L1155] [51:07.68] written.
[L1156] [51:08.16] >> Yes. All human written. Yeah.
[L1157] [51:10.40] >> We talked a lot about lean and I know
[L1158] [51:12.80] there's competitors to lean. What are
[L1159] [51:15.20] the pros and cons of the different proof
[L1160] [51:17.68] assistants? You know, in what scenarios
[L1161] [51:20.96] is one preferred over the others? For
[L1162] [51:23.36] instance, the first disclaimer, I'm a
[L1163] [51:25.52] completely biased person here, right?
[L1164] [51:28.08] But I can tell you what users tell me. I
[L1165] [51:31.04] mean about for example one thing the
[L1166] [51:33.36] users love is the fact as l is super
[L1167] [51:36.56] extensible because l implemented in ling
[L1168] [51:40.24] you can add extensions to imagine you're
[L1169] [51:43.52] doing your math proof in the middle of
[L1170] [51:45.84] this math proof and say oh I want this
[L1171] [51:47.76] fancy automation here you can write in
[L1172] [51:49.92] the same file or the AI can write for
[L1173] [51:53.12] you the extension for automating a proof
[L1174] [51:57.28] and it will do it I mean even the AI is
[L1175] [52:00.72] they know about the the fact L is
[L1176] [52:03.44] extensible.
[L1177] [52:05.28] If I ask the AI to isolate an issue in
[L1178] [52:09.12] ling, I give the AI a link file, it will
[L1179] [52:13.12] start writing a ling meta program, a
[L1180] [52:16.00] program about the link tunnels to
[L1181] [52:18.96] validate the conjecture it has about why
[L1182] [52:22.56] it doesn't work. It's crazy. I mean the
[L1183] [52:26.08] I keeps writing link meta extension
[L1184] [52:28.32] there. The fact that L extension is
[L1185] [52:31.12] really popular with so many people for
[L1186] [52:33.52] example there is Patrick Masur he's a
[L1187] [52:37.20] French mathematician
[L1188] [52:40.88] uh he wrote something called Labos
[L1189] [52:44.24] Labose you can he uses for teaching we
[L1190] [52:48.00] have this language for writing the
[L1191] [52:50.16] proofs but he made the language look
[L1192] [52:52.80] like English and he has the info view
[L1193] [52:56.48] now is a point and click you can click
[L1194] [52:58.32] there it gives you suggestions about the
[L1195] [53:00.48] next move that's written in structured
[L1196] [53:04.32] English like you find in a textbook. You
[L1197] [53:07.36] see the the the student has a really
[L1198] [53:10.48] good idea on how to write in formal math
[L1199] [53:13.20] proof and he did that without asking me
[L1200] [53:16.56] any questions and he all this stuff the
[L1201] [53:18.96] point and click the the new language the
[L1202] [53:22.48] new interactivity he did all by himself.
[L1203] [53:25.52] He's not a computer scientist. He he's
[L1204] [53:28.16] has a math degree and he did all this
[L1205] [53:30.88] stuff and it's for English and French. I
[L1206] [53:33.52] mean you can choose I mean you can write
[L1207] [53:36.32] the proofs in French
[L1208] [53:38.64] uh and looks a textbook proof. I mean uh
[L1209] [53:42.16] uh the people that write visualizations
[L1210] [53:45.04] right for you want to visual you're
[L1211] [53:47.92] trying to prove something about a math
[L1212] [53:49.60] object you can write extension that
[L1213] [53:52.56] visualize these objects in your info
[L1214] [53:55.12] view right [snorts] that people that
[L1215] [53:57.60] write new domain specific languages
[L1216] [54:00.40] embedded in link for different purposes
[L1217] [54:02.64] for example for protocol verification
[L1218] [54:05.52] there's a language called veil is a link
[L1219] [54:08.88] you open veil you feel like it's a
[L1220] [54:10.56] different system for protocol
[L1221] [54:12.00] verification, but it's just a link file
[L1222] [54:15.60] with these extensions for protocol
[L1223] [54:17.52] verification. The language for this
[L1224] [54:20.48] writing protocol is a very convenient
[L1225] [54:22.80] way.
[L1226] [54:25.36] These folks wrote the whole thing
[L1227] [54:27.44] without ever talking to us. They only
[L1228] [54:30.48] talked to us after they had done it said
[L1229] [54:33.36] look I want this pass of link to be
[L1230] [54:35.04] faster. That's was the only interaction
[L1231] [54:37.28] we had. uh and so interactivity is a big
[L1232] [54:40.64] deal.
[L1233] [54:42.32] Uh another big deal now is the
[L1234] [54:44.48] mathematical library uh is vast. I mean
[L1235] [54:48.16] for stating problems open conjectures
[L1236] [54:51.92] you need a library to with the concept
[L1237] [54:54.48] to even state the problem right. So le
[L1238] [54:57.44] has a massive library and a massive
[L1239] [55:00.64] community.
[L1240] [55:02.16] Uh the community also plays a big role.
[L1241] [55:05.84] people uh before AI I think now most
[L1242] [55:08.56] people ask questions about link to AI
[L1243] [55:10.80] but in the past people would go to the
[L1244] [55:12.88] lens lip channel
[L1245] [55:15.12] ask a question about ling they would get
[L1246] [55:16.96] an answer in five minutes I mean people
[L1247] [55:19.76] would say human based AI I mean people
[L1248] [55:22.64] would be writing answers instantaneously
[L1249] [55:25.52] to your problems the community played a
[L1250] [55:28.40] big role another one was
[L1251] [55:32.96] we listen to to to our users I mean uh
[L1252] [55:37.68] uh the math I mean if you talk for
[L1253] [55:40.00] example Jeremat was the first user I
[L1254] [55:43.76] mean he has math backgrounds
[L1255] [55:47.84] he he you ask him look he said look I
[L1256] [55:52.48] could ask anything any new feature I
[L1257] [55:55.60] would get back the same day I mean this
[L1258] [55:58.16] the fix the new feature the same day and
[L1259] [56:01.60] this attracts people right I mean
[L1260] [56:03.36] because you are making improvements
[L1261] [56:04.80] making sure the system does what they
[L1262] [56:07.76] once uh uh they come back for more. I
[L1263] [56:11.28] mean uh this also has a huge impact in
[L1264] [56:15.04] growing the community. when I was doing
[L1265] [56:17.76] some research there was this idea I
[L1266] [56:19.36] think you mentioned in this conversation
[L1267] [56:20.64] too there's this uh dependent type yes
[L1268] [56:24.64] >> proof assistance and then there's higher
[L1269] [56:26.56] order logic what what is that difference
[L1270] [56:28.88] there
[L1271] [56:29.84] >> at the beginning uh when I start I won't
[L1272] [56:32.56] choose high order logic because it's
[L1273] [56:35.04] much [snorts] easier to implement I mean
[L1274] [56:37.92] uh the pen types is way harder there
[L1275] [56:41.84] uh
[L1276] [56:43.44] but the math community I mean Jeremy is
[L1277] [56:46.32] the one that convinced me that I would
[L1278] [56:48.56] never be able to attract serious
[L1279] [56:51.12] mathematicians like fields medal level
[L1280] [56:53.52] math people with high order logic.
[L1281] [56:56.32] Right? His his point is like how logic
[L1282] [56:59.12] is good for concrete math but if you
[L1283] [57:02.08] want to talk about abstract objects
[L1284] [57:05.28] uh dependent type theory is way more
[L1285] [57:07.76] powerful and is beautiful is easy to
[L1286] [57:11.12] explain why is called dependent. For
[L1287] [57:13.60] example, you can have a structure in
[L1288] [57:15.84] ling when you have several fields like x
[L1289] [57:18.64] and y are natural numbers or integers.
[L1290] [57:20.88] Let's say they're integers.
[L1291] [57:23.36] You can have another field. The type of
[L1292] [57:25.84] the field is a proof that x greater than
[L1293] [57:28.64] y. The type of this field is x let's
[L1294] [57:32.48] call greater
[L1295] [57:34.48] column. You say x greater than y. The
[L1296] [57:37.04] type depends on the value of the
[L1297] [57:39.76] previous fields. That's why it's called
[L1298] [57:41.84] dependence type theory. You can have
[L1299] [57:43.92] types that depends on the values of
[L1300] [57:46.32] other parameters, other fields and so
[L1301] [57:49.60] on. But the beautiful thing about that
[L1302] [57:53.52] that's in this you have this very small
[L1303] [57:56.88] language that is so expressive
[L1304] [57:59.84] for example this fields now that's a
[L1305] [58:02.48] proof [snorts] you you have to provide a
[L1306] [58:04.96] proof you can view it as invariance I
[L1307] [58:07.20] can only build elements of this type if
[L1308] [58:12.48] I give the x and y like in other
[L1309] [58:14.40] programming languages but I have to give
[L1310] [58:16.08] a proof that the x is greater than y is
[L1311] [58:19.44] impossible ble to construct elements
[L1312] [58:21.92] without providing this evidence, right?
[L1313] [58:25.36] Uh you can do this in variance that's
[L1314] [58:28.56] you don't have to invent invariants,
[L1315] [58:30.48] right? the language just the fact you
[L1316] [58:32.32] have these dependencies you can express
[L1317] [58:35.92] uh in the functions you can have a
[L1318] [58:38.40] function for example that says takes a x
[L1319] [58:41.52] a y and a proof that's y is different
[L1320] [58:43.84] from zero right I mean it's impossible
[L1321] [58:47.60] to call the function if you do not
[L1322] [58:49.36] provide evidence that y is different
[L1323] [58:51.60] from zero this was always cool but in
[L1324] [58:55.12] the past people would say wow providing
[L1325] [58:57.20] this proofs is really annoying but with
[L1326] [58:59.92] AI Now the I can synthesize the proofs
[L1327] [59:02.56] for you. Uh and it's really cool.
[L1328] [59:07.28] >> In higher order logic though could you
[L1329] [59:09.28] express the same?
[L1330] [59:10.56] >> No no that's you cannot you don't have
[L1331] [59:12.56] the you lose the dependencies. For
[L1332] [59:14.56] example one thing that you cannot do in
[L1333] [59:16.16] high order logic. Uh in l
[L1334] [59:20.72] in serious math people you have a bunch
[L1335] [59:24.40] of structures they manipulate. you have
[L1336] [59:27.20] like something a field I mean a ring a
[L1337] [59:30.72] group
[L1338] [59:32.96] you can write a function in ling that
[L1339] [59:35.28] takes a group and he turns a new group a
[L1340] [59:39.44] new structure
[L1341] [59:42.16] you're not man you don't really care
[L1342] [59:44.08] about the elements of the structure you
[L1343] [59:45.68] are viewing the structure as a first
[L1344] [59:47.52] class citizen that's something that the
[L1345] [59:50.16] penet can do easily and in order logic
[L1346] [59:53.76] is you have to play in coding tricks is
[L1347] [59:56.88] a mess. I mean, uh, some people say,
[L1348] [01:00:00.64] "Oh, it works for math." None of the
[L1349] [01:00:02.96] mathematicians agree with this
[L1350] [01:00:04.72] statement. None. I mean, you talk to to
[L1351] [01:00:08.40] terish,
[L1352] [01:00:11.36] Jerem,
[L1353] [01:00:12.88] Kevin Buzzard, Patrick Masu, they would
[L1354] [01:00:15.36] say, "No, no, you have to do the pens
[L1355] [01:00:17.68] type theory." I mean,
[L1356] [01:00:22.00] that's another example for me that
[L1357] [01:00:23.68] listening to your users is important. If
[L1358] [01:00:25.84] you want to appeal to this community,
[L1359] [01:00:27.68] it's totally okay to say I don't care
[L1360] [01:00:30.96] about this community. But if you care,
[L1361] [01:00:33.44] listening to what they really want is
[L1362] [01:00:35.68] importance.
[L1363] [01:00:37.36] >> So when we think about the the future of
[L1364] [01:00:40.00] lean, I'm curious to hear your thoughts
[L1365] [01:00:42.64] on where you think lean is going. Um
[L1366] [01:00:46.32] things you're excited about in the
[L1367] [01:00:47.76] future. You know, what might it look
[L1368] [01:00:50.08] like in in a few years?
[L1369] [01:00:51.84] >> Yeah. Yeah. One thing uh we have this
[L1370] [01:00:55.36] nonprofit behind LIN since 2023.
[L1371] [01:00:59.12] I mean L 13 years old uh the first 10
[L1372] [01:01:03.04] years was
[L1373] [01:01:05.36] such project right I mean only when we
[L1374] [01:01:08.40] got the nonprofits behind ling that it
[L1375] [01:01:11.76] became you can view as a product we have
[L1376] [01:01:14.00] a team of engineers
[L1377] [01:01:16.56] and we managed to do it because the
[L1378] [01:01:19.28] impact on math right but Sebastian and I
[L1379] [01:01:23.36] I mean we co-ounded this nonprofit what
[L1380] [01:01:25.84] we are really excited about is le as
[L1381] [01:01:28.72] programming language, a programming
[L1382] [01:01:29.84] language where you can prove things
[L1383] [01:01:31.68] about your programs, right? And that's a
[L1384] [01:01:34.64] direction we are pushing really hard,
[L1385] [01:01:36.96] right? Link to uh uh we are super
[L1386] [01:01:40.72] grateful for AWS,
[L1387] [01:01:43.28] Amazon, they they're making the largest
[L1388] [01:01:46.40] donation so far to these nonprofits
[L1389] [01:01:49.20] where the goal is to accelerate this
[L1390] [01:01:52.32] path. I mean, LIN is doing super well in
[L1391] [01:01:54.32] the math path, but let's make Ling as a
[L1392] [01:01:56.72] programming language. lings a system for
[L1393] [01:01:59.36] social verification, harder
[L1394] [01:02:01.12] verification. Let's push to the extreme.
[L1395] [01:02:04.64] Let's give some love to these people uh
[L1396] [01:02:07.92] uh to this path that's right now we do
[L1397] [01:02:10.24] not really have funing to push seriously
[L1398] [01:02:12.88] this path. That's the nonprofits, right?
[L1399] [01:02:16.64] Uh for me to be in a world where you can
[L1400] [01:02:20.56] reason about your codes uh uh is part of
[L1401] [01:02:23.04] my life. They I'm not writing testes
[L1402] [01:02:25.84] anymore. I'm writing properties and
[L1403] [01:02:29.44] proving them. The AI is proving most of
[L1404] [01:02:32.40] them for me. Uh this is direction we are
[L1405] [01:02:36.32] pushing hard. And one people one thing
[L1406] [01:02:39.44] that people don't realize is that when
[L1407] [01:02:41.92] you have proofs it enables optimizations
[L1408] [01:02:45.60] for free. You can ask the for example
[L1409] [01:02:48.00] today if you ask the AI to optimize you
[L1410] [01:02:50.88] have to inspect the code to make sure no
[L1411] [01:02:53.52] bugs were introduced in the process.
[L1412] [01:02:56.72] But
[L1413] [01:02:58.24] if the AI is telling you, look, I
[L1414] [01:03:00.64] optimize it. It still computes the same
[L1415] [01:03:02.80] thing. Here's the proof.
[L1416] [01:03:05.60] Uh this is a game changer in my points
[L1417] [01:03:09.12] of view.
[L1418] [01:03:10.72] >> Yeah, I've heard multiple people say
[L1419] [01:03:13.60] this decade will be the you the decade
[L1420] [01:03:16.48] of formal verification of software and
[L1421] [01:03:19.28] yeah, maybe, you know, lean will be a
[L1422] [01:03:21.92] huge part of that.
[L1423] [01:03:23.68] >> Yeah. Yeah. We we for sure we're super
[L1424] [01:03:26.24] excited to make it happen. I mean uh we
[L1425] [01:03:30.40] uh
[L1426] [01:03:32.00] scalability is super important, right?
[L1427] [01:03:34.48] Because there's a big difference between
[L1428] [01:03:37.52] math and and social verification. In
[L1429] [01:03:40.80] math the the statements are usually
[L1430] [01:03:43.52] really tiny or small. I mean the is an
[L1431] [01:03:47.12] example. I mean super small but the
[L1432] [01:03:50.80] proofs insanely cheap.
[L1433] [01:03:54.48] for socialification
[L1434] [01:03:56.56] is the opposite right these statements
[L1435] [01:03:58.64] are big I mean but the proofs are
[L1436] [01:04:01.44] shallow the reason why this is true is
[L1437] [01:04:04.24] shallow but you have to manipulate this
[L1438] [01:04:07.28] big objects right
[L1439] [01:04:10.00] >> so for someone who wants to um learn
[L1440] [01:04:14.24] more about formal verification or learn
[L1441] [01:04:16.32] more about lean do you have a top
[L1442] [01:04:19.04] technical book recommendation
[L1443] [01:04:21.36] >> in the lean websites I mean we have uh
[L1444] [01:04:25.28] several books there that's introduce
[L1445] [01:04:27.36] lean functional programming lean theorem
[L1446] [01:04:29.84] proving lean mathematics in lean the
[L1447] [01:04:32.80] mechanics of proof is great for for
[L1448] [01:04:35.12] educational purposes we have we have a
[L1449] [01:04:38.00] collection of books if
[L1450] [01:04:40.96] people go to lind-lang.org or they they
[L1451] [01:04:44.48] you'll find all these books there.
[L1452] [01:04:49.04] But one one thing I I tell people these
[L1453] [01:04:51.68] days is that learning
[L1454] [01:04:54.64] l using AI is super efficient. I mean
[L1455] [01:04:58.64] you you keep talking to AI in natural
[L1456] [01:05:01.20] language asking what do you want asking
[L1457] [01:05:03.92] it to write examples many people split
[L1458] [01:05:07.12] the screen in three now right we had the
[L1459] [01:05:10.56] link codes the info view and on the
[L1460] [01:05:13.12] bottom now many people now using an AI
[L1461] [01:05:15.44] agent there that's writing the codes and
[L1462] [01:05:19.28] explaining natural language what's going
[L1463] [01:05:21.28] on there it's a super effective way I
[L1464] [01:05:24.80] mean Aren style he told me when he
[L1465] [01:05:27.36] learned ling he he uses old version of
[L1466] [01:05:30.48] it was before agents he [snorts] would
[L1467] [01:05:32.96] have the shajp on one window and the
[L1468] [01:05:37.44] visual studio code in the other window
[L1469] [01:05:39.12] and he would copy and paste between them
[L1470] [01:05:41.44] and that's how he learned but now he's
[L1471] [01:05:44.48] even more effective with the AI agents
[L1472] [01:05:49.76] it's easy to pick up I mean just talk to
[L1473] [01:05:52.48] the agent sometimes people say how do I
[L1474] [01:05:54.72] that start talking to the agent. He will
[L1475] [01:05:57.52] help you. here will customize
[L1476] [01:06:00.64] uh right you can explain what you know
[L1477] [01:06:03.84] already right I mean what's your
[L1478] [01:06:05.68] backgrounds and for example if you tell
[L1479] [01:06:08.80] oh I know hasll it's so much easier
[L1480] [01:06:11.92] right you can customize the process
[L1481] [01:06:15.44] >> and then last question for you is you
[L1482] [01:06:17.04] know if you could go back to the
[L1483] [01:06:18.96] beginning of you know building C3
[L1484] [01:06:21.36] building lean and give yourself some
[L1485] [01:06:24.08] advice knowing what you know now what
[L1486] [01:06:25.92] would you
[L1487] [01:06:27.03] >> [laughter]
[L1488] [01:06:28.72] >> No, I'll keep it a secret. I mean, I
[L1489] [01:06:31.60] think ignorance is a bliss. I mean, you
[L1490] [01:06:34.00] don't know how hard things are and when
[L1491] [01:06:36.48] you start the adventure, maybe I'll keep
[L1492] [01:06:39.28] secrets. What I would tell I think one
[L1493] [01:06:42.16] thing, especially before starting I I'm
[L1494] [01:06:45.92] super introverted
[L1495] [01:06:48.00] and I would tell look you should work on
[L1496] [01:06:50.80] your people's skills. I mean, because it
[L1497] [01:06:53.68] helps a lot. I mean when you have to
[L1498] [01:06:55.04] interact with a community with people
[L1499] [01:06:58.16] for me it was hard to to learn that and
[L1500] [01:07:00.88] and I would tell myself look it's really
[L1501] [01:07:03.04] important to have people's skills too.
[L1502] [01:07:07.04] >> Well thank you for your time today
[L1503] [01:07:08.72] appreciate it.
[L1504] [01:07:09.36] >> Thank you.
[L1505] [01:07:10.40] >> Hey thank you for watching this podcast.
[L1506] [01:07:12.00] If you liked it and you want to see the
[L1507] [01:07:13.44] show grow, please support with a comment
[L1508] [01:07:15.84] or a like. Also, if you have any
[L1509] [01:07:18.40] recommendations for people you want me
[L1510] [01:07:20.08] to bring on, please drop a comment.
[L1511] [01:07:22.72] guests like Barbara Liskoff, Mike
[L1512] [01:07:24.88] Stonereaker, Mark Brooker. These were
[L1513] [01:07:27.28] all people that I brought on because
[L1514] [01:07:29.28] someone left a comment. On another note,
[L1515] [01:07:31.52] aside from the podcast, I'm working on
[L1516] [01:07:33.44] building the ergonomic keyboard that I
[L1517] [01:07:35.36] wish existed. Here's a glance at the
[L1518] [01:07:37.52] prototype. It's a split keyboard, so
[L1519] [01:07:39.76] there's two sides. Um, this is in the
[L1520] [01:07:41.92] case, but yeah, we launched on
[L1521] [01:07:43.44] Kickstarter and we hit our goal within
[L1522] [01:07:45.44] eight hours of launching. I really
[L1523] [01:07:47.04] appreciate it if you were one of the
[L1524] [01:07:48.32] people who grabbed one of the early
[L1525] [01:07:49.92] units. Um, we're now working on the long
[L1526] [01:07:52.24] journey of building the tooling now. And
[L1527] [01:07:54.32] so if you still want to pick one up,
[L1528] [01:07:56.00] I've left the late pledges open on
[L1529] [01:07:58.08] Kickstarter, so you can grab one there.
[L1530] [01:08:00.24] I'll put a link in the description.
[L1531] [01:08:02.24] Thank you again for watching the podcast
[L1532] [01:08:04.56] and I'll see you in the next
