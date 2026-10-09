Chunk 1; segments 1–367. 

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

Source ID: source-238007c2e5a842c7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_P_vs_NP,_Zero-Knowledge_Proofs,_Quantum_Computation_Avi_Wigderson_en.txt
Video: https://www.youtube.com/watch?v=5GUcvSAJcJw

[L10] [00:00.08] If tomorrow somebody finds even a
[L11] [00:02.64] classical factoring algorithm in
[L12] [00:04.40] polinomial time, I think there'll be
[L13] [00:05.92] chaos in the world.
[L14] [00:07.76] >> This is Avi Wigerson Turing award and
[L15] [00:10.40] Abel Prize winner and I interviewed him
[L16] [00:12.72] all about his field.
[L17] [00:14.16] >> The question of P versus ZP is whether
[L18] [00:16.96] we can solve all the problems we really
[L19] [00:19.68] want to solve. The quality of randomness
[L20] [00:22.16] is in the eye of the beholder or in the
[L21] [00:24.32] computational power of the beholder. How
[L22] [00:27.04] can anybody convince me that they have a
[L23] [00:29.36] proof of P different than NP? And
[L24] [00:31.44] nevertheless, I know absolutely nothing
[L25] [00:33.84] about the way they proved it. And it
[L26] [00:36.16] turns out they can do it for the
[L27] [00:38.40] wholeing problem. For problems that are
[L28] [00:40.40] not computable, you know, if tomorrow
[L29] [00:43.20] somebody finds an efficient algorithm
[L30] [00:45.04] for NP complete problems, you know what
[L31] [00:47.68] do you do?
[L32] [00:49.04] >> Here's the full episode.
[L33] [00:54.00] In one of your lectures, you mentioned
[L34] [00:55.84] that P= NP is philosophically about the
[L35] [01:00.32] fundamental limits of human knowledge.
[L36] [01:02.80] What is P= NP and how does it relate to
[L37] [01:07.36] human knowledge?
[L38] [01:08.88] >> Well, in the simplest way and I will
[L39] [01:11.92] talk at the high level. Uh we are
[L40] [01:15.44] interested in various problems in life
[L41] [01:18.88] in all sorts of problems, mathematical
[L42] [01:20.96] problems, scientific problems, medical
[L43] [01:24.40] problems, personal problems,
[L44] [01:25.84] intellectual problems. We are in the
[L45] [01:27.92] business in computer science of solving
[L46] [01:29.76] problems by computers. Now uh we would
[L47] [01:34.40] like to somehow classify
[L48] [01:37.52] uh those problems that we can solve
[L49] [01:41.36] right to know what we can know. Well,
[L50] [01:43.60] the problems we can solve are the things
[L51] [01:45.28] we will know, we will understand. So,
[L52] [01:48.00] there are all the problems that we want
[L53] [01:50.80] to understand. There are many of them.
[L54] [01:54.08] Uh, and the problems that we can
[L55] [01:56.48] understand, can solve. Okay. In a very
[L56] [02:00.56] basic way, the first class is NP. All
[L57] [02:03.20] the problems we want to solve are really
[L58] [02:05.68] NP problems. So, it's a class of
[L59] [02:08.16] problems.
[L60] [02:10.08] uh a subset of it is the problems we can
[L61] [02:12.64] solve. They're the problems we can
[L62] [02:14.72] currently solve. But we are interested
[L63] [02:16.96] in all the problems we can solve in
[L64] [02:20.08] principle we can ever you know really
[L65] [02:23.12] solve. So the question of P versus NP is
[L66] [02:27.60] whether we can solve all the problems we
[L67] [02:30.48] really want to solve. Whether we can
[L68] [02:32.08] know everything we want to know.
[L69] [02:35.68] This is basically about the limits of
[L70] [02:38.40] our knowledge. Of course, I have to
[L71] [02:41.12] justify why you know these classes which
[L72] [02:44.72] are mathematically defined actually are
[L73] [02:47.12] captured by this intuitive
[L74] [02:49.60] u intuitive meanings I'm giving them. P
[L75] [02:53.36] is very easy to justify what we can
[L76] [02:55.28] solve is what we can uh you know solve
[L77] [02:58.32] in our lifetime using whatever we have
[L78] [03:00.80] let's say all computers that we uh have
[L79] [03:04.64] using efficient algorithms. So problems
[L80] [03:07.28] we can solve are problems you see in our
[L81] [03:09.52] apps in our phones, right? If there's a
[L82] [03:12.56] navigation app, it means somebody
[L83] [03:14.56] invented an algorithm that's efficient
[L84] [03:16.64] enough to solve any, you know, shortest
[L85] [03:19.92] path problem between any two places in
[L86] [03:23.12] any kind of map.
[L87] [03:25.60] Okay. Uh where all the problems we want
[L88] [03:29.36] to solve are NP problems.
[L89] [03:32.32] What is NP? NP is a class of problem.
[L90] [03:35.68] the mathematical definition
[L91] [03:38.08] uh problems so that you know whether
[L92] [03:41.84] they are easy or hard to solve we don't
[L93] [03:43.68] know but if somebody hands us a solution
[L94] [03:47.92] then we can easily check that indeed it
[L95] [03:50.48] is a good solution now why are all
[L96] [03:54.64] problems we humanity is interested in of
[L97] [03:57.44] this nature you can think there's no
[L98] [03:59.60] limit to what we may want to know but I
[L99] [04:02.24] claim that essentially in any human
[L100] [04:04.56] endeavor
[L101] [04:05.68] The
[L102] [04:07.28] if you are embarking on any problem, if
[L103] [04:09.28] you really seriously want to solve a
[L104] [04:11.12] problem, the least you want to know is
[L105] [04:14.32] that when you hit upon a solution,
[L106] [04:16.48] you'll recognize it as a solution. And
[L107] [04:19.28] why would you ever start on looking for
[L108] [04:21.92] something if you will never recognize it
[L109] [04:23.92] as what you looked for? So you think
[L110] [04:27.44] mathematicians are looking for proofs of
[L111] [04:30.32] theorems. Certainly if somebody gives a
[L112] [04:32.88] proof you know wrote a paper about it we
[L113] [04:35.36] can verify if a scientist wants to
[L114] [04:38.48] explain data
[L115] [04:40.72] uh you know about the planets or about I
[L116] [04:43.12] don't know
[L117] [04:45.44] bacteria or whatever uh you know want to
[L118] [04:50.08] develop a theory so that's what we are
[L119] [04:52.16] searching for in this case and yeah we
[L120] [04:56.32] again scientists write papers about
[L121] [04:58.32] their theories have to be consistent
[L122] [05:00.08] with the data We have a way of of
[L123] [05:02.40] recognizing that this is a good
[L124] [05:04.48] solution. Engineers
[L125] [05:07.68] uh you know are usually tasked with
[L126] [05:10.16] creating something bridge or phone or
[L127] [05:13.44] you know something uh under some
[L128] [05:17.04] constraints. It can be monetary
[L129] [05:19.28] constraints, physical constraints, all
[L130] [05:21.36] sorts of you can use this but not this
[L131] [05:23.68] and so on. Anyway, if an engineer
[L132] [05:26.08] designed something, whoever gave them
[L133] [05:28.48] the task can look at it and say, "Well,
[L134] [05:30.72] you you violated some constraints." Oh,
[L135] [05:33.60] no, it's good. You you you really
[L136] [05:35.92] delivered what we were looking for. So,
[L137] [05:38.56] I'm giving you examples. I mean, I can
[L138] [05:40.64] give many more. Detectives are supposed
[L139] [05:42.72] to solve crimes and you know, we know
[L140] [05:45.28] from detective books, you know, they
[L141] [05:47.04] eventually provide them. So these are
[L142] [05:50.24] examples of uh very fundamental human
[L143] [05:52.88] endeavors that are you know encompass
[L144] [05:55.76] almost everything I can think of. In all
[L145] [05:58.00] of them what people are searching for
[L146] [06:00.32] have the property that when a solution
[L147] [06:03.12] is found it is easily recognized.
[L148] [06:06.88] So
[L149] [06:09.04] repeating in the beginning NP are all
[L150] [06:12.00] problems that we can honestly say we
[L151] [06:14.96] really want to solve and P are those
[L152] [06:17.52] that we can solve. whether they are
[L153] [06:19.92] equal. You know, if they are equal, then
[L154] [06:21.76] everything we would want to know, cure
[L155] [06:23.36] for cancer,
[L156] [06:25.20] uh you know, anything you imagine uh can
[L157] [06:28.72] be, you know, just the very fact that
[L158] [06:32.32] a solution can be easily recognized
[L159] [06:34.56] would imply that it can be efficiently
[L160] [06:37.12] found. That means that we can know
[L161] [06:39.68] everything we ever want to know. It's a
[L162] [06:41.44] fundamental question about human
[L163] [06:43.04] knowledge.
[L164] [06:44.40] So, I know this is one of those um
[L165] [06:47.52] Millennium Prize problems. There's a
[L166] [06:49.60] million-dollar prize if you can provide
[L167] [06:52.32] a proof for for this. You know, I can
[L168] [06:55.04] imagine you could prove that they're
[L169] [06:57.44] equivalent. You could also prove that
[L170] [06:59.44] they're not. If you had to guess like
[L171] [07:02.80] when and if a proof comes, which
[L172] [07:05.04] direction would your intuition say it
[L173] [07:07.04] goes and why? I think that my intuition
[L174] [07:09.92] and that's probably hold for almost all
[L175] [07:12.72] members of the theoretical
[L176] [07:15.92] computer science community is that they
[L177] [07:17.92] are different. I think there are several
[L178] [07:20.72] reasons for that and I will already tell
[L179] [07:22.88] you now that they you know they are not
[L180] [07:25.36] that convincing. [laughter]
[L181] [07:27.92] One is I think intuition that most of us
[L182] [07:31.28] have that you know finding something is
[L183] [07:35.20] really hard and just checking that it's
[L184] [07:37.52] there. If you lost your keys or your
[L185] [07:40.56] phone and you know you have no idea
[L186] [07:42.72] where to look but you know somebody
[L187] [07:45.04] points out oh you left it on the window
[L188] [07:48.16] seal or something like this. Yes. Ah
[L189] [07:50.08] yeah I did. So we have this uh
[L190] [07:53.28] experience from life that finding is
[L191] [07:56.64] typically a harder task than just
[L192] [07:58.88] checking that it is what we look for.
[L193] [08:03.52] Another is that
[L194] [08:05.92] real NP problems occur all over the
[L195] [08:09.20] place. occur in optimization, in logic,
[L196] [08:12.48] in other aspects in mathematics, in
[L197] [08:16.96] verifying that algorithms and protocols
[L198] [08:20.08] and security systems actually work all
[L199] [08:22.88] sorts of uh and
[L200] [08:26.88] uh in this generality these optimization
[L201] [08:29.52] problems that are NP problems maybe NP
[L202] [08:31.84] hard problems uh people try to solve for
[L203] [08:36.32] completely
[L204] [08:37.84] you know egocentric to make their
[L205] [08:40.32] company richer or to uh and there are
[L206] [08:43.92] thousands of these and they have they
[L207] [08:46.16] manifest themselves in many different
[L208] [08:48.16] forms and so over the maybe
[L209] [08:52.80] 50 60 70 years. Uh people seriously look
[L210] [08:56.56] for algorithms for these very different
[L211] [08:58.56] ones and couldn't find any.
[L212] [09:02.48] This you know may seem like there's no
[L213] [09:05.68] such solution
[L214] [09:07.76] and in a uh getting a bit more technical
[L215] [09:12.80] u NP problems NP complete problems in
[L216] [09:16.40] particular are uh seem to require search
[L217] [09:20.96] over an exponential exponentially large
[L218] [09:23.68] space
[L219] [09:25.52] like all the all the possible uh you
[L220] [09:28.80] know solutions to some u system of
[L221] [09:32.24] equations for example
[L222] [09:35.52] and uh somehow P versus NP is about
[L223] [09:39.52] having a general method for cutting down
[L224] [09:42.56] this exponentially search space into
[L225] [09:45.44] searching over something much smaller in
[L226] [09:47.84] a clever way and this should apply to
[L227] [09:50.00] all these problems so that would be P
[L228] [09:53.60] equal NP and people don't think that
[L229] [09:55.68] there is such a way but as I said you
[L230] [09:58.96] know these are
[L231] [10:01.52] uh yeah these are intuitions that are
[L232] [10:04.48] you know maybe pretty strong and uh yeah
[L233] [10:08.88] I think that's the only you know if
[L234] [10:10.80] tomorrow somebody finds an algorithm for
[L235] [10:13.68] an efficient algorithm for complete
[L236] [10:15.84] problems using some new idea that nobody
[L237] [10:18.96] ever thought of you know what do you do
[L238] [10:21.60] [laughter]
[L239] [10:22.40] >> that would change the world in software
[L240] [10:24.96] engineering we we use algorithms all the
[L241] [10:28.64] time and they often have these very
[L242] [10:31.04] satisfying properties where the solution
[L243] [10:34.48] you know we we use space or some
[L244] [10:37.44] algorithm that can take something where
[L245] [10:39.68] the brute force is uh something much
[L246] [10:42.16] larger to down to something that's
[L247] [10:44.64] polomial time or something very
[L248] [10:46.32] reasonable but in all these NP problems
[L249] [10:50.40] it's pretty unsatisfying that the best
[L250] [10:53.20] we could do is brute force is am I
[L251] [10:56.00] understanding that correctly
[L252] [10:57.52] >> yeah you're yeah you're understanding it
[L253] [11:00.00] perfectly correctly. I think that maybe
[L254] [11:01.76] what you are getting at is that
[L255] [11:05.44] NPcomplete problems are you know a
[L256] [11:08.72] particular NP complete problem is really
[L257] [11:11.68] a family of instances right I mean you
[L258] [11:14.72] want to to find the Hamiltonian tour
[L259] [11:18.80] some traveling salesman to through
[L260] [11:21.20] through some map you know there's this
[L261] [11:23.44] map and that map and this network and
[L262] [11:25.76] other network and you know there are
[L263] [11:27.68] many many instances when we talk about
[L264] [11:30.64] an algorithm for them. Typically we say
[L265] [11:33.52] an algorithm is efficient if it's
[L266] [11:35.36] efficient and correct on all of them.
[L267] [11:38.56] In software engineering and many aspects
[L268] [11:41.28] of uh you know optimization in many uh
[L269] [11:45.92] real world problems the instances is a
[L270] [11:49.44] much more restricted set.
[L271] [11:52.16] you know they come from uh you know
[L272] [11:54.64] trying to verify a particular protocol
[L273] [11:57.92] or
[L274] [11:59.76] I don't know protein folding if you want
[L275] [12:01.60] to think about the biological example uh
[L276] [12:05.04] the way it is phrased as an NP uh hard
[L277] [12:08.80] problem is
[L278] [12:11.36] you want to minimize the energy of a
[L279] [12:14.40] system under some various constraints
[L280] [12:16.72] which have to relate to the chemistry of
[L281] [12:18.64] the various uh molecules and atoms
[L282] [12:21.92] appear in in the protein. [snorts] Uh
[L283] [12:25.20] and this kind of optimization problem
[L284] [12:27.20] one can easily prove is np hard and
[L285] [12:30.00] nevertheless our body faults our
[L286] [12:33.68] proteins all the time you know in
[L287] [12:38.16] extremely efficiently. Now why is that?
[L288] [12:41.04] Of course, I don't know really why is
[L289] [12:42.72] that, but it would seem that evolution
[L290] [12:47.36] uh designed proteins in such a way that
[L291] [12:50.16] this, you know, folding them only them.
[L292] [12:52.80] We don't have that many proteins. There
[L293] [12:54.64] are not exponentially many proteins in
[L294] [12:56.64] the body. There are only a few that
[L295] [13:00.56] maybe are more prone to efficient energy
[L296] [13:04.56] minimization. So uh and more generally I
[L297] [13:08.40] think in software engineer you or at
[L298] [13:11.60] least in verification and testing you
[L299] [13:14.40] often want to check that something meets
[L300] [13:16.48] the specifications.
[L301] [13:18.64] Uh you usually translate it into a
[L302] [13:21.52] satisfiability
[L303] [13:23.28] uh question of bulan formulas. the
[L304] [13:26.08] formulas that you get or the instances
[L305] [13:28.96] that you get out of these uh have some
[L306] [13:33.12] structure and may maybe for them various
[L307] [13:36.56] greedy approaches or clever not just
[L308] [13:39.20] greedy but clever uh but efficient
[L309] [13:43.12] methods work. In other words is making
[L310] [13:45.76] it short uh instances that come up are
[L311] [13:49.68] not the worst case instances. We have
[L312] [13:52.24] many examples of this that we can
[L313] [13:54.88] actually prove this. For example, early
[L314] [13:57.36] on it was recognized that uh the simplex
[L315] [14:00.56] method which is an algorithm to solve
[L316] [14:02.72] linear programs
[L317] [14:05.60] uh on the one hand uh requires
[L318] [14:08.88] exponential time for you know worst case
[L319] [14:13.36] system of inequalities.
[L320] [14:15.44] Uh but uh in practice it seems to run in
[L321] [14:19.68] linear time. So evidently the sets of
[L322] [14:22.64] linear systems that we tackle in real
[L323] [14:25.44] life are you know have some extra
[L324] [14:27.76] structure that allow this particular
[L325] [14:29.60] algorithm to uh to solve them
[L326] [14:33.20] efficiently. Of course, today we know an
[L327] [14:36.64] algorithm that's efficient for all in
[L328] [14:38.64] our programs, but it's much more
[L329] [14:40.08] complicated and people don't or I don't
[L330] [14:42.48] know how much it's used in practice, but
[L331] [14:44.96] the simplex method is a very simple to
[L332] [14:48.16] run and yeah, usually it works. You
[L333] [14:51.60] mentioned the protein folding and I mean
[L334] [14:53.60] yeah that's an interesting one because
[L335] [14:55.84] it's it's an NP problem but it was
[L336] [14:59.84] solved to a acceptable extent and you
[L337] [15:03.84] when I was reading about it it it wasn't
[L338] [15:06.40] solved for 100% of cases it provides a
[L339] [15:09.52] solution and a confidence score but it
[L340] [15:12.32] doesn't give you the answer 100%
[L341] [15:15.28] accurate you fully computed and so when
[L342] [15:19.60] you think about these NP P problems.
[L343] [15:21.84] What if you relaxed the the criteria of
[L344] [15:25.84] being correct? Could the asmtoic
[L345] [15:29.20] complexity be less than the exponential
[L346] [15:32.96] that we're talking about?
[L347] [15:34.00] >> Yeah, it's a very natural and good
[L348] [15:35.68] problem. So in the in the uh protein
[L349] [15:38.64] folding you were talking about alpha
[L350] [15:40.40] fold I guess which is an algorithm a
[L351] [15:42.32] uristic
[L352] [15:44.00] that was learned from existing proteins
[L353] [15:46.80] and uh is working very well on you know
[L354] [15:51.04] on instances it didn't see but are still
[L355] [15:53.36] proteins coming from the body even if it
[L356] [15:56.48] did perfectly on these not just that
[L357] [16:00.64] would still be for in the discussion I
[L358] [16:04.00] mentioned before because the instances
[L359] [16:06.72] it is trying to sort of come from real
[L360] [16:08.64] life and probably have extra structure
[L361] [16:10.88] that allow efficient solution. But you
[L362] [16:14.40] are right there. That's one of the
[L363] [16:15.60] things that people naturally do when
[L364] [16:18.72] they cannot solve a an optimization
[L365] [16:22.00] problem exactly because it's NP complete
[L366] [16:24.32] or NP hard. Maybe I should say NP
[L367] [16:27.52] complete NP out problems are those
[L368] [16:29.92] problems in NP that are are as hard as
[L369] [16:33.60] all problems in NP. If you solve one
[L370] [16:36.96] efficiently, you solved all efficiently.
[L371] [16:39.76] If you prove one hard then you proved
[L372] [16:42.80] all of them hard. So they somehow
[L373] [16:44.32] capture the complexity of the class and
[L374] [16:46.64] traveling salesman is an example and
[L375] [16:49.52] protein fodic in this framework of
[L376] [16:52.96] energy minimization is one and
