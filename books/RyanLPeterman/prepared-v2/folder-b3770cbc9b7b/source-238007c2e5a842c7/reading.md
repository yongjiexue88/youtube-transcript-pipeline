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
[L377] [16:55.20] banability and so on. Okay. So you want
[L378] [16:59.04] to optimize something and it's np
[L379] [17:01.84] complete np hard. Uh so that's a sign
[L380] [17:07.04] that you shouldn't try to find an
[L381] [17:09.04] algorithm that works always. But one
[L382] [17:11.44] thing you can do is do an approximation.
[L383] [17:13.84] That's a very natural relaxation. You
[L384] [17:15.92] don't want the optimum. You are willing
[L385] [17:17.68] to live with a factor of two from
[L386] [17:19.60] optimum or 10% from optimum or some
[L387] [17:23.04] factor away from optimum.
[L388] [17:25.52] Uh
[L389] [17:27.44] NP completeness was discovered in the
[L390] [17:29.92] early 70s. In the early 90s there was a
[L391] [17:33.12] breakthrough called the PCP theorem. The
[L392] [17:35.76] PCPCOM allows you to argue hardness of
[L393] [17:38.96] even approximation problems.
[L394] [17:41.84] So for example you can show that uh uh
[L395] [17:46.88] satisfiability of banan formulas
[L396] [17:51.60] um you know it's not just so you you
[L397] [17:54.72] want to meet you want to let's say find
[L398] [17:57.28] an assignment to a bunch of constraints
[L399] [18:00.32] let's say bulam constraints let's say on
[L400] [18:02.64] three variables for simplicity
[L401] [18:06.56] uh so you want to satisfy all of them uh
[L402] [18:09.28] the the relaxation would be Okay, I want
[L403] [18:11.60] to satisfy 90% of them or as good a
[L404] [18:15.44] fraction as I can. if I cannot get 100%
[L405] [18:18.48] of them the PCP theorem one way to
[L406] [18:21.76] phrase it and certainly one of the
[L407] [18:23.60] consequence major consequence is that we
[L408] [18:27.28] know that you cannot even achieve a very
[L409] [18:29.84] good approximation and to illustrate how
[L410] [18:33.84] uh uh you know tight this understanding
[L411] [18:37.60] is for some problems is that for the
[L412] [18:40.72] example I gave when there are only three
[L413] [18:43.04] variables per constraint if you just
[L414] [18:46.56] guess at random the values to the
[L415] [18:49.04] variables in the assignment you will
[L416] [18:51.12] satisfy uh 78 of the constraints. This
[L417] [18:55.52] is because each particular constraint is
[L418] [18:58.72] usually the disjunction of three
[L419] [19:00.48] variables will be true with probability
[L420] [19:02.88] it's an or three will be with
[L421] [19:06.48] probability 78. So if you random if you
[L422] [19:09.28] don't think don't look at the formula
[L423] [19:11.20] even you can satisfy
[L424] [19:13.68] 78 of them and the PCP theorem and
[L425] [19:18.48] significant strengthening by hustad
[L426] [19:21.28] hustad tells you that if you want to
[L427] [19:24.56] satisfy 78 plus epsilon
[L428] [19:28.00] that's already npr
[L429] [19:30.24] so we know today to argue the difficulty
[L430] [19:33.84] not only of finding the perfect solution
[L431] [19:36.88] the optim optimal solution. But even uh
[L432] [19:40.08] how close to optimal you can get uh for
[L433] [19:45.92] lots and lots of problems large classes
[L434] [19:48.00] of problems in particular constraint
[L435] [19:50.32] optimization problems uh you know of the
[L436] [19:53.92] type of such fabric. So even if you
[L437] [19:57.92] solve just the slightest epsilon for any
[L438] [20:02.40] trivially small epsilon,
[L439] [20:04.88] >> it's just as hard as doing the full
[L440] [20:06.56] >> as hard as finding the optimum. So
[L441] [20:09.36] >> you mentioned uh MP hard, nplete, you
[L442] [20:12.96] know, NP. I know there's other
[L443] [20:16.00] complexity classes. Maybe you could give
[L444] [20:19.20] some more context on kind of the whole
[L445] [20:21.28] space of complexity classes.
[L446] [20:23.04] >> Yeah. So uh I'm just remark that uh we
[L447] [20:26.48] have a zoo of complexity classes and in
[L448] [20:29.76] fact there's a website called uh yeah
[L449] [20:32.80] the complexity zoo which has in it
[L450] [20:35.52] hundreds of uh hundreds and hundreds of
[L451] [20:39.60] complexity classes of all types
[L452] [20:43.92] websites started by Scott Arson once we
[L453] [20:47.04] realized that there he realizes
[L454] [20:50.56] there's a whole zoo out there we want to
[L455] [20:52.72] know the relationship between these
[L456] [20:54.48] classes. Okay. So what uh what is the
[L457] [20:57.92] point about these classes? Uh like P and
[L458] [21:00.88] NP we want to classify problems by the
[L459] [21:05.36] amount of resources they take. So P
[L460] [21:09.60] polinomial time is a class of problem
[L461] [21:12.48] that can be solved in an amount of time
[L462] [21:15.68] that relates polomially to the size of
[L463] [21:18.64] the data. Of course you expect that you
[L464] [21:21.04] the data there's more data the instance
[L465] [21:23.68] grows you'll spend more time but if it's
[L466] [21:27.12] you know linear time or quadic time or
[L467] [21:29.36] cubic time you say let me call it at
[L468] [21:33.20] least theoretically efficient
[L469] [21:36.00] and uh uh np uh you classify not the
[L470] [21:42.64] time to solve but the time to verify a
[L471] [21:45.12] solution if it was given you want this
[L472] [21:47.20] to be a polomial time. So it's a very
[L473] [21:49.60] different but uh first of all there are
[L474] [21:54.00] you know many more time functions that
[L475] [21:56.40] just polomial and exponential and uh and
[L476] [22:01.92] you know doubly exponential and you can
[L477] [22:04.00] go to finite and uh uh you know one
[L478] [22:09.20] fundamental result starting with
[L479] [22:11.20] Turing's paper is that there are
[L480] [22:13.44] problems that are simply unsolvable by
[L481] [22:16.08] computers. So really the first comp
[L482] [22:18.16] complexity class is a class of solvable
[L483] [22:21.12] problems, decidable problems to ensure
[L484] [22:24.48] that these are not all problems. There
[L485] [22:26.40] are natural problems that are not
[L486] [22:27.84] decidable at all. But time is only one
[L487] [22:31.12] resource and uh we are interested and
[L488] [22:34.40] you know both from practical and
[L489] [22:35.84] theoretical reasons in lots of other
[L490] [22:37.68] resources. Memory is a resource costly
[L491] [22:40.72] resource and we want to minimize space.
[L492] [22:43.04] the space invested in in a computation
[L493] [22:47.28] uh in in problems with several parties.
[L494] [22:50.40] You are interested in the amount of
[L495] [22:51.92] communication exchange. So not the
[L496] [22:55.44] internal computational
[L497] [22:57.92] effort that they exert themselves but
[L498] [23:00.24] how much you know if you talk to a
[L499] [23:02.72] satellite you want to minimize the
[L500] [23:05.44] communication. You can think about
[L501] [23:07.12] energy. You can think about uh yeah
[L502] [23:09.92] there there are plenty of your parallel
[L503] [23:12.48] time. How much can you speed up you know
[L504] [23:16.08] computation of a problem if you work on
[L505] [23:17.92] it not with one computer but with n
[L506] [23:20.64] computers if you your data is of size
[L507] [23:22.96] then you know does it you know allow it
[L508] [23:25.52] to solve it immediately or maybe it
[L509] [23:28.32] doesn't help at all. So there are
[L510] [23:30.88] complexity classes
[L511] [23:33.60] classify problems according to how much
[L512] [23:35.84] resources they need and there are many
[L513] [23:38.08] of these and one important part of so
[L514] [23:40.96] that's a a major theme in the
[L515] [23:43.44] methodology of comp complex complexity
[L516] [23:47.44] theory and uh coming with it is uh
[L517] [23:53.60] attempts to understand complexity
[L518] [23:55.52] classes
[L519] [23:57.28] as problems that relate to each other
[L520] [24:00.24] even if you don't know their complexity.
[L521] [24:02.08] So for example, MP is a class and we
[L522] [24:06.24] don't know the complexity of all
[L523] [24:07.68] problems in this or MP complete
[L524] [24:09.44] problems. We don't know whether they are
[L525] [24:10.80] all easy or or hard but we do know we
[L526] [24:14.08] have efficient algorithms to translate
[L527] [24:16.24] one into the other.
[L528] [24:18.64] So it's not obvious that if you want to
[L529] [24:22.64] uh solve a satisfiability problem you
[L530] [24:24.64] don't know how but you have an algorithm
[L531] [24:27.04] to solve sudoku problems
[L532] [24:29.92] uh without not just 3x3 but also 4 by if
[L533] [24:33.60] you had a an efficient method to solve
[L534] [24:36.48] sudoku problems P equals NP because you
[L535] [24:40.80] can efficiently take an instance of
[L536] [24:44.32] subscribability or so salesman or
[L537] [24:47.28] factoring integer or any of these
[L538] [24:49.68] problems be from it the sudoku problem
[L539] [24:53.84] and from the solution of the sudoku
[L540] [24:56.08] problem you can translate back and get
[L541] [24:59.12] the best solution for your original I
[L542] [25:01.84] know traveling salesman tool so we are
[L543] [25:05.12] interested in uh efficient reductions
[L544] [25:07.68] between problems whose complexity we
[L545] [25:10.24] don't know but we want to relate them to
[L546] [25:12.88] each other we build some kind of partial
[L547] [25:15.12] order of the hardness of uh different
[L548] [25:19.36] problems. So there yeah really yeah you
[L549] [25:23.12] don't want to know how many uh problems
[L550] [25:26.32] we have some arise for constraints that
[L551] [25:28.88] the real world maybe technology
[L552] [25:32.00] imposes or cause for and some are
[L553] [25:34.16] naturally arising mathematically because
[L554] [25:37.12] you know they're interesting.
[L555] [25:39.04] >> You mentioned that these NPcomplete
[L556] [25:40.96] problems they kind of are all equivalent
[L557] [25:43.44] in some way. What's the the proof to you
[L558] [25:47.44] know equate a SAT solving problem to
[L559] [25:50.96] like a graph coloring problem or
[L560] [25:52.64] something like that? Are they all
[L561] [25:54.32] similar in nature or are they kind of
[L562] [25:55.92] bespoke to you know the problem you're
[L563] [25:57.76] going to and from? is a very good
[L564] [25:59.84] question and uh uh you will find that in
[L565] [26:04.08] most of these they call them reductions
[L566] [26:06.96] algorithms to translate one problem to
[L567] [26:09.28] another uh most of them are relatively
[L568] [26:12.72] simple and uh not all and I talked about
[L569] [26:17.44] the PCP theorem before showing that
[L570] [26:19.92] approximation is is all this is very
[L571] [26:23.44] highly non trivial but most computers
[L572] [26:26.00] proof like between coloring and satis
[L573] [26:28.40] satisfiability and it goes both ways.
[L574] [26:31.04] They are both complete. So it goes both
[L575] [26:33.28] ways. It is simple and the first one
[L576] [26:38.08] uh was the satisfiability problem. The
[L577] [26:40.40] you know original papers of cook and
[L578] [26:42.32] leaven defining NP completeness and
[L579] [26:45.44] proving that NP complete problems exist.
[L580] [26:48.88] They both uh the first problem they push
[L581] [26:52.40] complete was satisfiability.
[L582] [26:55.12] Why is this? So why can all these other
[L583] [26:58.56] problems be reduced to satisfiability?
[L584] [27:01.84] The reason is really that computation is
[L585] [27:05.60] local.
[L586] [27:07.68] Uh
[L587] [27:09.20] computation is local. I mean that if you
[L588] [27:12.08] think about your computer, your laptop
[L589] [27:13.84] or any any computational device, usually
[L590] [27:16.96] it manipulates bits uh uh by some local
[L591] [27:22.00] operations. You look at this these two
[L592] [27:24.24] registers and you add them or you take
[L593] [27:27.36] these two bits and exclusive all them or
[L594] [27:30.16] end them or something and you will do a
[L595] [27:32.56] sequence of this sequence of simple
[L596] [27:34.72] operations and you arrive at a
[L597] [27:37.04] conclusion. This locality can be
[L598] [27:39.12] translated
[L599] [27:40.64] to
[L600] [27:42.16] uh a bunch of constraints or what would
[L601] [27:45.04] be consistent sequence of states of your
[L602] [27:47.76] machine. If you look at the time
[L603] [27:50.32] evolution of any computation, you know,
[L604] [27:53.12] memories in some state then in another
[L605] [27:55.76] state and but they change locally. Okay.
[L606] [27:58.88] So if you had the if you could guess and
[L607] [28:01.52] that's the NP part. I mean if somebody
[L608] [28:03.36] provided you the table of computation,
[L609] [28:05.68] you could check that it's consistent by
[L610] [28:08.56] writing a bunch of local constraints. So
[L611] [28:11.36] you know some conjunction of very few
[L612] [28:13.44] variables
[L613] [28:15.04] uh
[L614] [28:17.12] uh on all over this table of computation
[L615] [28:21.68] uh and write down a satisfiability
[L616] [28:24.16] problem. I want this to be true and this
[L617] [28:26.96] to be true and this to be true for some
[L618] [28:29.52] assignment and what does the assignment
[L619] [28:31.84] has to satisfy it should be a table like
[L620] [28:34.64] this all these constraints should be
[L621] [28:36.56] satisfi you know should be true and
[L622] [28:40.16] it has to be consistent with the input
[L623] [28:42.32] given right so some of the input has to
[L624] [28:45.12] match the first time zero uh content of
[L625] [28:49.04] the of the machine so this locality uh
[L626] [28:53.44] allows for many of these translations.
[L627] [28:56.48] If you realize this, you will quickly
[L628] [29:00.24] find a reduction from coloring to satis.
[L629] [29:04.08] It's also I mean it's not clear why
[L630] [29:06.00] coloring is an evolution of computation
[L631] [29:08.48] but it's starts already by local
[L632] [29:12.00] constraints. you want a few colors and
[L633] [29:13.92] that every so some in some it's even
[L634] [29:16.32] easier but uh um the reduction from any
[L635] [29:22.64] NP computation that's that's what NP
[L636] [29:25.12] computers means anything in NP can be
[L637] [29:27.76] translated to satisfiability NP is just
[L638] [29:30.80] a computation of a touring machine say
[L639] [29:35.84] uh only that you don't know what is a
[L640] [29:38.64] computation if somebody guessed it or
[L641] [29:41.44] showed it to you then you all you need
[L642] [29:43.92] is to verify this verification is local
[L643] [29:47.20] and that's the source of many simple uh
[L644] [29:50.56] you know uh MP completeness reductions
[L645] [29:53.84] let let me give you a a really simple
[L646] [29:56.88] example why why uh is factoring integers
[L647] [30:01.76] reducible to
[L648] [30:03.92] uh satisfiability
[L649] [30:07.04] because if I gave you factors of an
[L650] [30:10.56] integer you could just multiply them and
[L651] [30:13.44] check that they equal the input. This
[L652] [30:16.32] multiplication is a is a simple
[L653] [30:19.52] algorithm, right? I mean, we know how to
[L654] [30:22.00] do it from second grade or something. Uh
[L655] [30:24.80] you write down the computation of
[L656] [30:26.48] multiplication in this local way and all
[L657] [30:30.08] you need is that uh somebody will guess
[L658] [30:32.96] for you really the factors. You
[L659] [30:35.68] mentioned time complexity and space
[L660] [30:38.00] complexity and I think intuitively like
[L661] [30:40.96] in software engineering we often trade
[L662] [30:43.68] those off for each other. Is there uh
[L663] [30:46.40] like general theory on that on how these
[L664] [30:48.80] two trade off?
[L665] [30:50.56] >> Yeah. Yeah. We have uh yeah all these
[L666] [30:53.12] questions are natural questions for uh
[L667] [30:55.68] complexity theorist. uh how does two
[L668] [30:58.80] resources relate to each other and
[L669] [31:00.96] whether they they can trade off or maybe
[L670] [31:03.12] you can minimize them both at the same
[L671] [31:05.68] time. Uh and uh it depends on the
[L672] [31:09.92] problem. There are there are problems
[L673] [31:12.00] for which uh we know results like
[L674] [31:15.52] multiply time and space it has to be at
[L675] [31:18.96] least the square of the length of the
[L676] [31:22.48] input. So you can either do it with very
[L677] [31:26.48] small space like logarithmic space but
[L678] [31:29.04] you need to pay maybe quadratic time
[L679] [31:32.56] and uh if you want linear time you have
[L680] [31:36.96] to pay linear space or close to linear
[L681] [31:40.24] space. There are results of this type uh
[L682] [31:43.44] in in various models of computation.
[L683] [31:46.16] That's another thing you play with. Not
[L684] [31:48.80] all of them are you know they are all
[L685] [31:50.24] equivalent in principle but if you care
[L686] [31:52.88] about exact time or exact space are not
[L687] [31:55.60] equivalent. So there are problems for
[L688] [31:57.84] which there is a tradeoff there are
[L689] [32:00.00] problems for uh you know where you can
[L690] [32:02.16] solve them in linear time and
[L691] [32:03.76] logarithmic space. One very important
[L692] [32:07.44] general result that is a breakthrough
[L693] [32:09.44] from last year is a result of Ryan
[L694] [32:12.64] Williams. Uh and I'll tell you what it
[L695] [32:15.36] is, but I first describe what we knew
[L696] [32:17.36] about time and space. There's a clear
[L697] [32:20.48] inequality, right? If you run in time t,
[L698] [32:24.08] you will never use more than space t
[L699] [32:28.00] because you never visit so many cells or
[L700] [32:31.04] registers in your machine. So space is
[L701] [32:34.80] at most time.
[L702] [32:36.96] 50 years ago valant Paul and Piper uh
[L703] [32:40.64] improved this a little bit. They said
[L704] [32:42.32] that if you run time t there's an
[L705] [32:45.12] equivalent computation that will do this
[L706] [32:47.44] in slightly less space than t t over log
[L707] [32:50.96] t. That was a big result. Uh the running
[L708] [32:55.20] time of course will blow up. it will be
[L709] [32:57.52] very very expensive time-wise but at
[L710] [33:00.16] least you can save on space a little bit
[L711] [33:02.56] and uh this was uh believed almost 50
[L712] [33:07.68] years to be the best you can do in fact
[L713] [33:10.32] we had arguments that in certain models
[L714] [33:12.96] in certain stylized models of
[L715] [33:15.04] computation
[L716] [33:16.72] uh you cannot improve that I not
[L717] [33:20.24] describe you know this restricted models
[L718] [33:23.52] but some natural restricted models
[L719] [33:26.40] You cannot beat this.
[L720] [33:29.68] And what Ryan Williams descri
[L721] [33:33.12] found out last year is that in fact much
[L722] [33:36.32] better can be done. Any computation that
[L723] [33:40.32] runs in time t can be simulated by
[L724] [33:42.48] another algorithm that uses only square
[L725] [33:44.96] root of t space far far less than you
[L726] [33:48.56] know before. And uh the algorithm is
[L727] [33:52.08] quite uh uh sophisticated and uses an
[L728] [33:56.64] earlier result of uh James Cook, the son
[L729] [33:59.92] of Steve Cook of MP completeness and Ian
[L730] [34:03.44] Mer that was you know an essential
[L731] [34:06.48] technical ingredient but anyway uh you
[L732] [34:10.00] can you know there's a a really
[L733] [34:13.12] interesting uh way to to save space very
[L734] [34:16.96] very non-trivial way to save space.
[L735] [34:19.52] Again this algorithm will run in a lot
[L736] [34:22.16] of time but at least you you have a
[L737] [34:23.84] sense that uh yeah there the two
[L738] [34:26.48] parameters are related in a highly
[L739] [34:28.16] non-trivial way.
[L740] [34:29.36] >> Is this for a a general problem or
[L741] [34:31.76] >> general problem for touring machines?
[L742] [34:34.16] >> Okay.
[L743] [34:34.64] >> It may not work on random access
[L744] [34:36.40] machines or Yeah. What's the the trick I
[L745] [34:40.24] if you could explain intuitively or is
[L746] [34:42.24] it too deep to explain in
[L747] [34:45.28] >> it is
[L748] [34:47.12] you know really technically explaining
[L749] [34:49.36] it it's too deep but let me I'll give
[L750] [34:52.08] you a much earlier result which sort of
[L751] [34:55.60] indicates that really mysterious things
[L752] [34:58.72] can be done in small space.
[L753] [35:01.68] uh again it's uh probably yeah over 40
[L754] [35:04.96] years ago people discovered the
[L755] [35:06.72] following Dave Barington discovered the
[L756] [35:09.52] following really interesting uh
[L757] [35:12.00] phenomena. So suppose all you want is to
[L758] [35:14.32] count. I give you a sequence of bits and
[L759] [35:17.36] bits and you you want to count. You say
[L760] [35:21.28] you want to know whether there are more
[L761] [35:22.88] zeros than ones like the majority
[L762] [35:25.20] problem. Who wants the vote? Zeros or
[L763] [35:27.68] ones. Okay. Well, you can count. You can
[L764] [35:31.52] just add them up. And this takes
[L765] [35:33.84] logarithmic space.
[L766] [35:36.16] And it seems that the best you can do. I
[L767] [35:37.84] mean you want to count up to n
[L768] [35:40.64] to represent n takes login bits right I
[L769] [35:44.40] mean whatever n or the sum any number
[L770] [35:46.40] between one and takes login bit it seems
[L771] [35:49.20] essential
[L772] [35:51.52] it turns out that there's an algorithm
[L773] [35:54.88] I have to define exactly how it works it
[L774] [35:59.76] um I I will not define let me I will not
[L775] [36:02.80] define exactly how it works but it solve
[L776] [36:05.52] this problem in constant space. It seems
[L777] [36:08.96] like you can count arbitrarily high.
[L778] [36:12.40] All you need is access to whatever bit
[L779] [36:14.56] you like whenever you like. I want the
[L780] [36:16.56] 17th one. I want the 81st one. I want if
[L781] [36:20.56] you can uh have random access to the
[L782] [36:23.68] bits, even if you have constant space,
[L783] [36:26.72] you can tell whether there are more
[L784] [36:28.72] zeros than ones or ones and zeros
[L785] [36:31.36] regardless how long the input is. The
[L786] [36:34.16] trick is that somehow you use
[L787] [36:36.48] non-commutive algebra. You use something
[L788] [36:40.72] you know non-commutive algebra is not a
[L789] [36:42.88] because everybody's familiar with
[L790] [36:44.56] non-commutive things. I mean you we
[L791] [36:47.36] usually put the cars behind the horse
[L792] [36:49.92] and not in front of the horse. It
[L793] [36:51.60] matters or in software engineering we do
[L794] [36:54.72] this before that or it's very important.
[L795] [36:57.28] The order of things matter. uh uh so you
[L796] [37:02.40] can think about uh uh
[L797] [37:06.48] applying permutations one after the
[L798] [37:09.12] other you know if I rotate
[L799] [37:12.72] a circle and then take a mirror image it
[L800] [37:16.24] will give me the so these are two
[L801] [37:18.16] permutations right I mean say I have end
[L802] [37:20.32] points in a circle can shift it by one
[L803] [37:23.60] or I can uh you know let's say flip it
[L804] [37:26.40] around some uh diameter
[L805] [37:30.48] There are two permutations and and they
[L806] [37:33.12] don't commute. I mean if I first flip
[L807] [37:35.36] and then rotate I'll get something else
[L808] [37:37.52] if I first rotated and yeah think of all
[L809] [37:41.12] the points as colored by yeah so it's
[L810] [37:44.24] they don't commute. Bington is using uh
[L811] [37:48.08] you know he's somehow encoding the bits
[L812] [37:50.08] in the input by permutations
[L813] [37:53.60] not large permutations permutations of
[L814] [37:55.84] size five and somehow when he sees a one
[L815] [37:58.88] he maybe rotates and when he sees a zero
[L816] [38:01.60] he flips and the non-commutivity of this
[L817] [38:07.12] um u of these operations
[L818] [38:11.20] allow me to carry out a general formula
[L819] [38:15.52] a formula of ns and os and knots you
[L820] [38:19.44] know uh any formula like this formula
[L821] [38:23.12] that uh let's say of some size s uh it
[L822] [38:28.80] allows him to carry out this computation
[L823] [38:31.68] to really simulate the ends and os and
[L824] [38:34.32] not in this uh formula by rotations and
[L825] [38:38.08] flips of this uh you know five
[L826] [38:41.84] side sided pentagon Okay. And uh so just
[L827] [38:47.12] to remember the configuration of this
[L828] [38:49.52] pentagon, you need I don't know five
[L829] [38:51.92] bits or right. So you need constant
[L830] [38:56.00] space. How this captures the you know
[L831] [39:00.48] the computation? I can tell you you know
[L832] [39:02.80] one more sentence maybe it will not be
[L833] [39:05.76] uh clear to um
[L834] [39:10.00] everybody but
[L835] [39:12.32] you this non-commuting things
[L836] [39:16.08] uh you can you can do the following type
[L837] [39:18.48] of operation
[L838] [39:20.24] uh do rotate do flip then rotate back
[L839] [39:24.80] and flip back. This is called the
[L840] [39:27.92] commutator and it it can simulate an
[L841] [39:31.44] endgate
[L842] [39:33.60] the you know I can
[L843] [39:36.64] it's too much to describe in words
[L844] [39:38.56] without a board how it does it but
[L845] [39:41.28] there's a very famous analogy which is a
[L846] [39:44.08] riddle uh which if nobody I mean it's a
[L847] [39:47.68] good riddle to to think about uh which
[L848] [39:50.88] really captures this uh endgate problem.
[L849] [39:53.84] You you want to hang a painting in the
[L850] [39:57.20] following way. You have a painting uh
[L851] [40:00.00] it's the it has a string connecting the
[L852] [40:02.96] the two side but you want to hang it not
[L853] [40:05.76] on one nail but on two nails. Okay.
[L854] [40:09.52] There are two nails on the wall and you
[L855] [40:12.72] can do with the string whatever you want
[L856] [40:14.88] and the property you want
[L857] [40:17.68] is that if the two nails are there it's
[L858] [40:21.68] hanging every everybody's happy. If you
[L859] [40:24.72] pull out one nail doesn't matter which
[L860] [40:28.96] the picture falls to the floor.
[L861] [40:32.48] How would you loop the string around
[L862] [40:34.40] these nails so that you know this
[L863] [40:36.88] happens? Clearly this is an end gate or
[L864] [40:38.96] an O gate. Right. If one Yeah. And this
[L865] [40:43.04] has to do I mean if anybody finds a
[L866] [40:45.52] solution they realize what
[L867] [40:47.92] non-commutivity I'm talking about. And
[L868] [40:51.12] uh yeah it's a nice middle. Anyway so
[L869] [40:54.08] this type of trick where you can really
[L870] [40:57.36] um um this type of result you can really
[L871] [41:01.28] do uh in small space things you wouldn't
[L872] [41:04.40] imagine possible. It's a striking
[L873] [41:06.32] example. It's really when I heard this
[L874] [41:09.20] result first time I was the postto
[L875] [41:12.56] um and somebody told me uh uh and I just
[L876] [41:17.28] didn't believe it's possible. I mean you
[L877] [41:18.96] cannot count arbit high with a yeah. So
[L878] [41:22.96] yeah so the the trick that cook and
[L879] [41:26.56] merits have in their algorithm is a
[L880] [41:29.52] solution to a natural problem in much
[L881] [41:32.80] less space than you would think
[L882] [41:36.24] uh and uh it uses
[L883] [41:40.24] some sense tricks of this nature.
[L884] [41:44.00] So if you're counting arbitrarily large
[L885] [41:46.64] that is information and you're saying
[L886] [41:50.08] like maybe the intuition is that
[L887] [41:51.76] information is encoded in the sequence
[L888] [41:53.84] of operations. It is encoded. Yeah, of
[L889] [41:57.52] course you are not you are not
[L890] [41:59.12] delivering the final count. You just say
[L891] [42:01.92] whether there are more zeros than ones.
[L892] [42:04.08] If you have to write down of course you
[L893] [42:05.92] need if the answer takes
[L894] [42:09.12] some number of bits long then you need
[L895] [42:11.52] this this number to write it down. If
[L896] [42:14.48] you have a decision problem say like yes
[L897] [42:18.24] or no like are there more zeros than
[L898] [42:20.48] ones then you can do it for any any size
[L899] [42:24.00] input in constant space. Yeah
[L900] [42:26.64] >> that's incredible.
[L901] [42:27.68] >> It's pretty pretty incredible. Yeah. And
[L902] [42:30.56] by the way, this is a highly applicable
[L903] [42:32.72] result. It's used in cryptography in a
[L904] [42:34.80] fun in fundamental ways. It's useful.
[L905] [42:37.92] Yeah, it's used in various places and
[L906] [42:41.12] it's yeah, an extremely useful result
[L907] [42:44.48] here. By the way, unlike the Ryan
[L908] [42:46.72] Williams result, if you have a formula
[L909] [42:48.72] of size S, you can do it in constant
[L910] [42:51.36] space and the time of this algorithm
[L911] [42:54.48] does not blow up really a lot. It's just
[L912] [42:57.68] quadratic. So it's quadratic time. So
[L913] [43:00.48] this is something actually doable,
[L914] [43:02.64] useful, efficient and yeah, and it's
[L915] [43:05.52] also magical.
[L916] [43:06.80] >> We talked about the equivalence between
[L917] [43:09.12] um these MPMPlete problems and then I
[L918] [43:11.68] know in practice a lot of people to
[L919] [43:14.80] solve the other problems they just use
[L920] [43:16.48] SAT solvers.
[L921] [43:17.44] >> Yeah,
[L922] [43:18.80] >> I would have thought that would be less
[L923] [43:20.80] efficient though because you got to kind
[L924] [43:22.16] of translate it and then you're doing it
[L925] [43:23.68] in almost like a different problem
[L926] [43:25.52] space. Yeah, you you usually also
[L927] [43:27.60] enlarge the instance. Usually in
[L928] [43:30.88] translation you enlarge the instance. So
[L929] [43:33.20] what your question is why do people use
[L930] [43:35.84] cell service? I would say that uh
[L931] [43:38.80] there's no problem other than
[L932] [43:42.32] satisfiability that people uh uh thought
[L933] [43:46.96] so hard about
[L934] [43:49.12] really uh optimizing the huristics
[L935] [43:53.92] that uh efficiently work on many
[L936] [43:56.40] instances. There are very very clever
[L937] [43:58.72] ways in which you can um you know try
[L938] [44:03.76] start I mean you are not going to guess
[L939] [44:05.92] all the end bits but you want to start
[L940] [44:09.76] by guessing some bits that seem more
[L941] [44:11.92] pivotal that if you like in dominoes
[L942] [44:14.88] maybe when you set them to one value
[L943] [44:17.92] they force many other many other other
[L944] [44:20.72] values to be set and if that happens you
[L945] [44:23.60] cut down your search space. So there are
[L946] [44:26.08] many heristics of this type and also
[L947] [44:28.80] more clever than this that allow to
[L948] [44:31.28] solve such liability problems. If they
[L949] [44:34.32] have such structure again the worst case
[L950] [44:37.60] it will not will not help you. There is
[L951] [44:41.68] in fact a conjecture
[L952] [44:44.24] uh this is much stronger somehow than
[L953] [44:46.40] npmpleteness
[L954] [44:48.32] uh you know np complete problems taking
[L955] [44:50.48] exponential time. He said that uh we
[L956] [44:53.68] don't expect
[L957] [44:55.52] any savings. We we expect satisfiability
[L958] [44:58.48] problems to require really uh two to
[L959] [45:02.88] some constant times n. It's not it's not
[L960] [45:06.16] going to be two to the square root n or
[L961] [45:08.80] or n to the log or something like this
[L962] [45:10.96] is you know so yeah. So but the worst
[L963] [45:14.08] case may be hard but people optimize
[L964] [45:17.12] uh attacks on many many such formulas
[L965] [45:22.16] that somehow have all sorts of
[L966] [45:24.88] structural properties arising maybe in
[L967] [45:27.52] practice and I think that's the main
[L968] [45:30.00] reason that uh they are used it's also
[L969] [45:32.56] convenient I mean uh it's very you know
[L970] [45:36.16] people do it for uh testing
[L971] [45:39.36] specification that programs protocols
[L972] [45:42.96] meet specification. They're usually the
[L973] [45:46.08] specification are usually easily
[L974] [45:48.16] translated into simple constraints and
[L975] [45:51.20] that's almost a susceptibility problem.
[L976] [45:53.84] >> We talked about all the different types
[L977] [45:55.84] of resources in an algorithm and in one
[L978] [45:59.36] of your talks you said something where
[L979] [46:02.32] you you consider randomness another
[L980] [46:05.20] resource for an algorithm. What do you
[L981] [46:07.12] mean when you say randomness is a
[L982] [46:09.12] resource for an algorithm? In the early
[L983] [46:12.48] 70s,
[L984] [46:14.24] of course, randomized algorithms existed
[L985] [46:16.88] since antiquity and everybody was
[L986] [46:19.52] tossing coins for lots of reasons and of
[L987] [46:22.32] course statisticians
[L988] [46:24.32] uh you know do sampling and use
[L989] [46:26.32] randomness for but when when
[L990] [46:29.52] algorithmics you know designing
[L991] [46:31.44] efficient algorithms became big once we
[L992] [46:34.64] have had computers uh people realized
[L993] [46:37.36] that it can really enhance all sorts of
[L994] [46:39.52] uh uh computation for example we had no
[L995] [46:43.76] idea how to test primality of a number
[L996] [46:46.80] and in the 70s uh both microabin and uh
[L997] [46:50.96] survey and sass and found proistic
[L998] [46:53.04] algorithms which are fast to test
[L999] [46:55.60] primality okay so what does it mean a
[L1000] [46:58.48] probabistic algorithm it's an algorithm
[L1001] [47:00.80] that's allowed to make random choices so
[L1002] [47:03.36] you can think that there's an internal
[L1003] [47:06.32] uh you know little person or device
[L1004] [47:08.40] inside that tosses coins Of course,
[L1005] [47:10.80] that's not what happens. There's no
[L1006] [47:12.96] little person sitting in your laptop. So
[L1007] [47:16.16] the question is where do you get these
[L1008] [47:18.08] random bits? But it's very important to
[L1009] [47:20.40] stress that in all these um probabistic
[L1010] [47:24.64] algorithms, the underlying assumption is
[L1011] [47:27.52] that the bits you get are perfect. They
[L1012] [47:29.52] are half half each one and independent
[L1013] [47:33.44] of each other. It's like a uniform
[L1014] [47:35.20] distribution on all possibilities.
[L1015] [47:38.32] Now, where do you get this? I mean,
[L1016] [47:41.12] where seriously do you get this? I mean,
[L1017] [47:42.88] if you run a probabistic algorithm of
[L1018] [47:44.88] your laptop, since it doesn't have this
[L1019] [47:47.52] person inside tossing coins, it does
[L1020] [47:50.32] something.
[L1021] [47:52.32] Well, high quality randomness of this
[L1022] [47:54.88] type uh
[L1023] [47:57.84] costs money like time and like memory.
[L1024] [48:01.52] What do I mean by cost money? You can
[L1025] [48:03.92] have a very cheap solution. you can just
[L1026] [48:06.72] I don't know measure the thermal noise
[L1027] [48:08.88] in your computer or have one of the
[L1028] [48:10.72] Intel chips uh you know um you can
[L1029] [48:14.64] measure internet traffic and sample it
[L1030] [48:16.96] and believe it's random and and all of
[L1031] [48:19.36] these things are used you can do
[L1032] [48:21.44] something mathematical have some simple
[L1033] [48:24.16] procedure that is actually deterministic
[L1034] [48:27.36] like a linear congren generator
[L1035] [48:30.24] something like this and believe it's
[L1036] [48:31.92] random or you take can take the digits
[L1037] [48:33.92] of pi it's also So you know looks random
[L1038] [48:36.80] in some sense. So there are many things
[L1039] [48:38.96] you can use but you don't know they are
[L1040] [48:41.36] random. If you want them to be random
[L1041] [48:43.20] you know one source even this is not a
[L1042] [48:46.00] perfect source but we have quantum
[L1043] [48:48.56] mechanics. People believe you know
[L1044] [48:51.12] people believe it works in in life. It
[L1045] [48:53.44] seems like a cool theory of nature.
[L1046] [48:56.08] There are all sorts of arguments about
[L1047] [48:58.48] it but let's um put them aside. They
[L1048] [49:02.40] predict that if if you measure photons
[L1049] [49:05.68] coming out from some source and you
[L1050] [49:08.80] measure their spin whether it's up or
[L1051] [49:10.72] down, the prediction is that each one is
[L1052] [49:13.44] half half and it's independent of each
[L1053] [49:16.32] other. That's very nice. But if you are
[L1054] [49:18.24] going to build this device, it's going
[L1055] [49:19.92] to cost you a lot of money
[L1056] [49:22.48] and let alone that it will not be
[L1057] [49:24.64] perfect. But let's leave this aside
[L1058] [49:27.12] anyway. Since you want high quality
[L1059] [49:29.60] randomness or you have some way of
[L1060] [49:31.36] guaranteeing I mean you are running it
[L1061] [49:33.04] really on your laptop you it's not you
[L1062] [49:35.12] know okay the paper was written we can
[L1063] [49:38.00] test primality with probabistic
[L1064] [49:39.76] algorithm now we want to run it what do
[L1065] [49:41.44] you use so it makes sense to ask lots of
[L1066] [49:44.88] questions about randomness but to
[L1067] [49:46.64] guarantee the quality of the randomness
[L1068] [49:49.92] um and maybe you can minimize the is the
[L1069] [49:53.36] use of randomness by the way another
[L1070] [49:55.76] issue with randomness is that
[L1071] [49:58.24] you know the outcome is a random
[L1072] [49:59.92] variable and it's not always correct
[L1073] [50:02.40] right the whole point in most of these
[L1074] [50:04.08] algorithms you just have some small
[L1075] [50:06.32] probability of error if you have a
[L1076] [50:08.48] deterministic algorithm there's no error
[L1077] [50:11.20] so you also don't like the error so
[L1078] [50:14.48] treating it as a resource is simply a
[L1079] [50:16.88] convenient complexity theoretic way of
[L1080] [50:19.20] saying how do we understand you know uh
[L1081] [50:23.28] the amount of this resource we have to
[L1082] [50:25.52] invest or the number of bits we have to
[L1083] [50:27.28] invest
[L1084] [50:28.24] their quality and so on. So it's uh yeah
[L1085] [50:31.76] it's it's almost automatic for if you
[L1086] [50:34.96] think like a like a complexity theories.
[L1087] [50:37.60] How do we minimize for particular
[L1088] [50:39.68] algorithm like primarity testing
[L1089] [50:42.64] you know do you really need this? Do you
[L1090] [50:44.88] need them to be independent? Maybe you
[L1091] [50:46.72] can generate them in a you know maybe
[L1092] [50:49.20] you can you need n bits but you can
[L1093] [50:51.20] start from square n bits or from log n
[L1094] [50:53.68] bits that are really random and make
[L1095] [50:56.16] from them in some deterministic way uh
[L1096] [51:00.40] you know sort of pseudo random sequence
[L1097] [51:02.56] you can call it which is a good name
[L1098] [51:04.64] actually uh that will for this purpose
[L1099] [51:07.68] of this algorithm will look as if it was
[L1100] [51:11.76] random.
[L1101] [51:13.36] If you could do that, you don't need all
[L1102] [51:15.28] these bits. You can use much fewer. And
[L1103] [51:18.24] this whole theory of you know reducing
[L1104] [51:21.36] randomness, dandomization, removing
[L1105] [51:23.60] randomness is a huge field. And uh
[L1106] [51:27.12] people are you know there there are many
[L1107] [51:30.00] u problems and many ways of doing it and
[L1108] [51:33.04] uh uh the story with primality is
[L1109] [51:35.92] actually fascinating. So I mentioned
[L1110] [51:39.28] these two algorithms that were invented
[L1111] [51:41.20] and people were wondering about the
[L1112] [51:43.36] deterministic algorithm for primality.
[L1113] [51:45.36] It's a problem that has been articulated
[L1114] [51:48.32] already by Gaus in the most you know
[L1115] [51:51.84] complex theoretic way you can you know
[L1116] [51:55.92] uh back in his days hundreds of years
[L1117] [51:58.96] ago and uh maybe 150 I don't know
[L1118] [52:03.84] he was asking for an indefatigable
[L1119] [52:07.12] calculator
[L1120] [52:08.72] of course is a person but
[L1121] [52:11.36] he wanted this to be efficient that's
[L1122] [52:13.84] bas basically what
[L1123] [52:15.76] uh was looking for a primality test for
[L1124] [52:18.48] large numbers because they really wanted
[L1125] [52:20.16] to know about numbers maybe only few
[L1126] [52:22.72] tens of digits. They wanted to know
[L1127] [52:24.40] whether they are prime or not. There was
[L1128] [52:26.72] no efficient algorithm. Anyway, uh you
[L1129] [52:30.24] can wonder about this survey s and
[L1130] [52:32.80] algorithm.
[L1131] [52:34.56] Maybe you can use less randomness or
[L1132] [52:36.88] structural randomness that you can
[L1133] [52:38.48] generate from fewer bits and nobody had
[L1134] [52:41.76] any good idea. And then in the early
[L1135] [52:44.16] 2000s
[L1136] [52:46.00] Agaral Kay and Fenna
[L1137] [52:48.80] uh devised a different probabilistic
[L1138] [52:52.08] primality test and it's different. So
[L1139] [52:55.52] the analysis of randomness in it is
[L1140] [52:58.40] different and once you understand how
[L1141] [53:01.04] randomness is used,
[L1142] [53:03.44] you can maybe say ah we don't need to be
[L1143] [53:06.16] really totally independent bits. it's
[L1144] [53:08.56] it's okay if it has some structure and
[L1145] [53:12.24] then they found using number theoretic
[L1146] [53:15.04] ways uh a method to to generate this
[L1147] [53:20.40] pseudo you know pseudo randomly
[L1148] [53:22.32] generated from very few bits and that's
[L1149] [53:25.76] that's how the so often I don't know
[L1150] [53:28.72] often but sometimes deterministic
[L1151] [53:31.04] versions of probabistic algorithms are
[L1152] [53:34.00] discovered in simply understanding the
[L1153] [53:37.36] way in which the algorithm is using the
[L1154] [53:39.52] randomness understanding the analysis of
[L1155] [53:41.76] the algorithm
[L1156] [53:43.20] >> and saying okay it doesn't use all that
[L1157] [53:47.60] much
[L1158] [53:49.04] >> you you mentioned a few times the
[L1159] [53:51.20] quality of the randomness
[L1160] [53:52.96] >> how do you quantify the quality of
[L1161] [53:55.60] random bits
[L1162] [53:56.64] >> this basically a question about what
[L1163] [54:00.64] sudo randomness is and the general
[L1164] [54:02.72] answer is that it depends
[L1165] [54:05.84] uh you want
[L1166] [54:08.32] to fool a particular algorithm let's say
[L1167] [54:10.64] for primality.
[L1168] [54:12.40] So you want the randomness to fool the
[L1169] [54:15.04] this you want the al this algorithm not
[L1170] [54:18.00] to notice that you switched from perfect
[L1171] [54:21.20] randomness to something that's really
[L1172] [54:24.00] far less random has far less entropy but
[L1173] [54:26.96] the analysis works nonetheless.
[L1174] [54:29.60] Another algorithm maybe you need you a
[L1175] [54:32.64] completely different type of pseudo
[L1176] [54:34.40] randomness for it. There are there's a
[L1177] [54:36.80] set of examples of uh algorithmic
[L1178] [54:39.52] problems for which when you look at the
[L1179] [54:41.60] analysis they are much simpler than this
[L1180] [54:43.52] primality uh testing. When you look at
[L1181] [54:45.92] the analysis it seems to use not the
[L1182] [54:49.44] independence of all the n bits. You
[L1183] [54:52.00] really need only every pair of them to
[L1184] [54:54.16] be independent or every triple and
[L1185] [54:58.40] spaces of random variables which have
[L1186] [55:00.96] this property are much smaller. you can
[L1187] [55:03.92] generate them from login bits and so you
[L1188] [55:07.52] can fool them with this stuff. So the
[L1189] [55:09.20] quality of randomness there's a phrase I
[L1190] [55:12.00] like that it's the quality of randomness
[L1191] [55:14.64] is in the eye of the beholder
[L1192] [55:17.28] uh or in the computational power of the
[L1193] [55:19.36] beholder. You really need it to be just
[L1194] [55:22.48] as good as the tests that are applied to
[L1195] [55:26.16] it. You know you just want to be
[L1196] [55:28.48] completely pragmatic. You don't care
[L1197] [55:31.04] whether it's random or not. You just
[L1198] [55:32.72] care that an observer of a particular
[L1199] [55:36.32] structure or particular computational
[L1200] [55:38.72] power will not distinguish the
[L1201] [55:42.56] pseudo random distribution which have
[L1202] [55:44.56] may have less much less randomness in it
[L1203] [55:47.04] than the perfect one.
[L1204] [55:48.64] >> In one of your lectures actually you you
[L1205] [55:50.80] mentioned that and you gave a good
[L1206] [55:52.08] example and I was wondering if you could
[L1207] [55:54.32] um give the intuitive example of why
[L1208] [55:57.12] randomness is a function of the
[L1209] [55:58.96] observer's computational power.
[L1210] [56:00.96] >> Yeah. So I uh if you watch this talk you
[L1211] [56:04.08] know what the the example I give is an
[L1212] [56:06.48] example that's taken from this
[L1213] [56:08.64] fundamental paper of Manuel Blum and
[L1214] [56:12.96] Sylvia Malli. They tell you to consider
[L1215] [56:16.08] three experiments and the experiments go
[L1216] [56:20.16] as follows. They always between you and
[L1217] [56:22.56] me. You are the observer. I am the coin
[L1218] [56:24.80] tosser. I have a coin on my finger and I
[L1219] [56:28.08] toss it and just as it leaves my finger
[L1220] [56:31.84] you are supposed to predict what the
[L1221] [56:34.24] value will be when it falls on the floor
[L1222] [56:36.48] like in two seconds you have to
[L1223] [56:39.12] immediately say heads or tails. Okay
[L1224] [56:42.24] before you have to predict before it
[L1225] [56:44.00] falls. Uh well this is the first
[L1226] [56:47.92] experiment and uh you know what I ask
[L1227] [56:50.08] and what they ask you know what do you
[L1228] [56:52.00] think is a success your success what are
[L1229] [56:55.20] your chances of predicting it and the
[L1230] [56:57.52] obvious answer is you know one half you
[L1231] [56:59.60] know what uh how can it help you know
[L1232] [57:02.64] how what what can you do
[L1233] [57:05.44] the second is when you sit there but you
[L1234] [57:07.68] have a laptop like you have now and uh
[L1235] [57:11.12] yeah what what can you you will yeah I
[L1236] [57:13.68] don't know that you can how fast you
[L1237] [57:15.36] type, but the coin will be on the floor
[L1238] [57:19.28] in a second. The third experiment is
[L1239] [57:22.72] where your laptop is connected to a Cray
[L1240] [57:25.44] superco computer and the Cray superco
[L1241] [57:27.28] computer is connected to a bunch of
[L1242] [57:29.60] sensors and cameras and whatever devices
[L1243] [57:33.12] you want. They are all trained on my
[L1244] [57:35.20] finger.
[L1245] [57:36.72] Okay? And so as it leaves my finger the
[L1246] [57:39.44] coin the this apparatus certainly is
[L1247] [57:44.00] more than enough to calculate all the
[L1248] [57:46.88] you know angular momentum of the coin
[L1249] [57:49.44] and the distance to the floor and the
[L1250] [57:51.36] humidity in the air and whatever
[L1251] [57:52.96] parameters that completely determine its
[L1252] [57:56.64] motion in particular how it will land in
[L1253] [57:59.68] a split second far less than the time
[L1254] [58:02.40] needed to. So the the real point in this
[L1255] [58:07.04] example is
[L1256] [58:09.68] that the experiment the random cointos
[L1257] [58:14.48] this cointos did not change in all of
[L1258] [58:16.64] them. It is the same what you know
[L1259] [58:21.36] masses of people in math and physics and
[L1260] [58:24.32] philosophy and you know defined
[L1261] [58:26.64] randomness in various ways. There are
[L1262] [58:28.40] many definitions of of randomness and
[L1263] [58:31.36] they all focus on this event on the
[L1264] [58:34.48] cointos or sequence of cointoses. We in
[L1265] [58:37.52] complexity theory starting from this
[L1266] [58:39.60] paper
[L1267] [58:41.52] don't care about this event. I mean the
[L1268] [58:43.76] event stays the same and all it focuses
[L1269] [58:46.08] on the observer and it the only thing
[L1270] [58:49.12] that changed in these three experiments
[L1271] [58:51.36] is the computational power. So we want
[L1272] [58:54.64] to know how much enthropy is in the
[L1273] [58:56.40] coin. If you don't have enough
[L1274] [58:58.32] computational power, it seems to be full
[L1275] [59:00.96] entropy. It's a half half, right? You
[L1276] [59:03.52] don't know what it will be. If you have
[L1277] [59:05.60] enough computational power, you can
[L1278] [59:07.44] predict it completely and then it has
[L1279] [59:10.72] zero entropy.
[L1280] [59:12.56] So what changed is the observer. So the
[L1281] [59:16.00] observer is this algorithm we talked
[L1282] [59:18.00] about before. And uh any test that's
[L1283] [59:20.00] applied to you know uh to a set of to a
[L1284] [59:24.88] distribution to test the quality of
[L1285] [59:27.04] randomness depending on the test you
[L1286] [59:29.20] want to just make sure you you you want
[L1287] [59:33.04] to use as little true randomness uh in a
[L1288] [59:36.24] way that the observer will not notice.
[L1289] [59:38.96] And this is the source of many of the
[L1290] [59:41.44] important theorems that
[L1291] [59:44.00] um you know show that you can remove
[L1292] [59:47.76] remove randomness or reduce randomness
[L1293] [59:50.88] uh uh in probabilistic algorithms with
[L1294] [59:54.00] or without assumptions and uh uh really
[L1295] [59:57.68] are behind this understanding that we
[L1296] [59:59.60] have today. Randomness in algorithms is
[L1297] [01:00:01.84] not as powerful as we thought it is.
[L1298] [01:00:04.40] Like if if you know that something like
[L1299] [01:00:06.96] P is [clears throat] different than NP
[L1300] [01:00:08.56] or you have a hardware sing salesman is
[L1301] [01:00:11.44] exponentially hard or sus. If you know
[L1302] [01:00:14.72] that then in fact I can give you a sud
[L1303] [01:00:18.56] random generator that will dandomize any
[L1304] [01:00:22.64] probabistic algorithms. We know that
[L1305] [01:00:24.64] under this assumption we have what we
[L1306] [01:00:26.56] call P= BPP. Anything that has an
[L1307] [01:00:29.52] efficient probabistic algorithm also has
[L1308] [01:00:32.24] a probab
[L1309] [01:00:34.00] an efficient deterministic algorithm.
[L1310] [01:00:36.40] You just need to know that there is a
[L1311] [01:00:39.12] hard function somewhere. Under what
[L1312] [01:00:41.12] assumptions do we know P equals BPP? uh
[L1313] [01:00:45.44] the assumption uh the very natural is
[L1314] [01:00:50.64] that one of these NPR problems or in
[L1315] [01:00:54.24] fact even problems in higher classes
[L1316] [01:00:57.92] requires a lot of hardware require
[L1317] [01:01:00.56] exponential size circuits to solve okay
[L1318] [01:01:04.32] we believe that it's like P versus NP
[L1319] [01:01:07.92] strengthened you cannot cut down the
[L1320] [01:01:10.88] exponential search space
[L1321] [01:01:13.44] Um and uh so maybe people are you know
[L1322] [01:01:19.12] happier with with with this assumption
[L1323] [01:01:21.20] but this assumption about uh time
[L1324] [01:01:24.72] complexity it has no randomness in it.
[L1325] [01:01:28.56] It's sort of at first it's shocking uh
[L1326] [01:01:32.00] that it's actually related to the
[L1327] [01:01:34.24] problem of removing randomness from
[L1328] [01:01:36.72] algorithms. So that's one fundament
[L1329] [01:01:39.60] fundamental connection. It's this
[L1330] [01:01:42.00] hardness versus randomness paradigm.
[L1331] [01:01:45.76] But we know even more. We know that it
[L1332] [01:01:49.20] goes both ways. We know that if you are
[L1333] [01:01:52.96] trying to remove randomness for some
[L1334] [01:01:55.12] algorithms, if you can do that, then you
[L1335] [01:01:59.68] found the hard function.
[L1336] [01:02:02.32] So there's really a an almost it's not
[L1337] [01:02:05.28] an exact if and only if but
[L1338] [01:02:08.96] uh again and there are many variants of
[L1339] [01:02:11.76] this in some variants is if and only if
[L1340] [01:02:14.32] is stronger but we really know that it's
[L1341] [01:02:16.72] really one of the other and since it's
[L1342] [01:02:19.60] hard to believe that all these hard
[L1343] [01:02:21.84] problems are easy or the similing the
[L1344] [01:02:23.92] hard problem like P= NP we tend much
[L1345] [01:02:26.72] more to believe the other alternative
[L1346] [01:02:28.64] name is that randomness in algorithms is
[L1347] [01:02:31.12] weak and you can remove it.
[L1348] [01:02:33.52] >> Open AAI, Enthropic, Cursor, and
[L1349] [01:02:36.48] Verscell all use this product to make
[L1350] [01:02:38.64] their lives better. And the problem it
[L1351] [01:02:40.80] solves is when you're building SAS or an
[L1352] [01:02:43.12] AI product, and you want to sell to
[L1353] [01:02:45.20] other companies, there's all these
[L1354] [01:02:46.96] requirements you need to meet. There's
[L1355] [01:02:48.88] SSO, there's SKIM, there's arbback,
[L1356] [01:02:52.16] there's audit logs. These are all things
[L1357] [01:02:53.92] that take time to integrate, but aren't
[L1358] [01:02:56.16] the main focus of your app. Work OS is
[L1359] [01:02:58.32] an API layer that lets you meet all of
[L1360] [01:03:00.16] these requirements in just a few lines
[L1361] [01:03:02.40] of code. So let's say you have a new SAS
[L1362] [01:03:04.80] product and you want to sell to other
[L1363] [01:03:06.40] companies. Work OS will solve all of
[L1364] [01:03:08.56] these critical feature gaps for you. You
[L1365] [01:03:11.36] can check them out at workos.com to
[L1366] [01:03:13.84] learn more and get started. And I
[L1367] [01:03:16.00] appreciate them for supporting my work
[L1368] [01:03:17.68] and sponsoring this podcast. Is [snorts]
[L1369] [01:03:19.92] there an intuitive explanation for the
[L1370] [01:03:22.08] relationship between problem hardness
[L1371] [01:03:24.48] and randomness? Yeah. [laughter]
[L1372] [01:03:27.44] Yeah. There's almost always an intuitive
[L1373] [01:03:29.76] explanation for Yeah. So what's the hard
[L1374] [01:03:33.20] what's the hard problem? I give you the
[L1375] [01:03:35.84] input. You you are a limited computer.
[L1376] [01:03:38.48] You are a polinomial time algorithm. I
[L1377] [01:03:41.12] give you the input. Let's say it's a
[L1378] [01:03:43.28] traveling salesman problem or you don't
[L1379] [01:03:46.48] know the answer. So you there's some
[L1380] [01:03:48.72] entropy in the answer, right? It's in
[L1381] [01:03:51.52] the same sense we discussed before
[L1382] [01:03:54.08] there's some entropy tiny entropy maybe
[L1383] [01:03:56.40] exponentially small entropy because
[L1384] [01:03:58.32] maybe the you know if the input is
[L1385] [01:04:00.40] random maybe only few instances are hard
[L1386] [01:04:04.08] and all the others you can solve but at
[L1387] [01:04:06.56] least you see a hint of a relationship
[L1388] [01:04:09.84] between hardness and entropy. This of
[L1389] [01:04:13.36] course is not satisfactory because we
[L1390] [01:04:15.20] want half we want the you know we want
[L1391] [01:04:18.48] uh that for you the answer will be like
[L1392] [01:04:21.12] a cointos not like a very biased
[L1393] [01:04:23.68] cointos.
[L1394] [01:04:25.28] So we need to find ways to amplify
[L1395] [01:04:28.88] this uh uncertainty for you. They
[L1396] [01:04:31.68] amplify the hardness. We want not just
[L1397] [01:04:33.60] that some instances will be hard but
[L1398] [01:04:36.40] that the random instance
[L1399] [01:04:39.44] whether the answer is yes or no for
[L1400] [01:04:42.80] polomial time observer will be half you
[L1401] [01:04:47.28] will not be able to gain an epsilon
[L1402] [01:04:49.60] advantage over a random guess.
[L1403] [01:04:54.00] So for this there we developed all sorts
[L1404] [01:04:56.24] of methods that amplify amplify
[L1405] [01:04:59.44] randomness. Now this doesn't solve the
[L1406] [01:05:02.24] problem at all because I managed to take
[L1407] [01:05:05.28] you know n bits a random instance of a
[L1408] [01:05:07.60] problem and manufacture one bit that's
[L1409] [01:05:11.28] hard for you to guess but I could have
[L1410] [01:05:13.84] taken the first random bit I pick for
[L1411] [01:05:16.24] the so I generate from many a few one
[L1412] [01:05:21.04] what you want to do is the opposite you
[L1413] [01:05:22.80] want a method that will take a few and
[L1414] [01:05:25.52] we generate many
[L1415] [01:05:28.08] right that's a random generator So, so
[L1416] [01:05:30.48] the random generator starts for a few
[L1417] [01:05:32.80] truly random bits and generates many and
[L1418] [01:05:36.00] for this we need
[L1419] [01:05:38.48] we need other tools. Uh there's
[L1420] [01:05:40.72] something uh that I developed with
[L1421] [01:05:43.12] Nissan
[L1422] [01:05:45.12] because today the NW generator. I like
[L1423] [01:05:48.08] to say that you know people
[L1424] [01:05:51.28] say that making the f first million
[L1425] [01:05:53.44] dollars is easy and afterwards you can
[L1426] [01:05:55.52] make many more millions.
[L1427] [01:05:57.84] You can think of it this way. The
[L1428] [01:05:59.92] hardness in the way I described it allow
[L1429] [01:06:02.48] you to make $1 million. But once you can
[L1430] [01:06:06.56] make one, there are methods to make many
[L1431] [01:06:09.68] more and in fact more than the number of
[L1432] [01:06:13.36] bits you started with. But still their
[L1433] [01:06:15.52] quality depend on the hardness of the
[L1434] [01:06:17.60] function you use. we still use this and
[L1435] [01:06:21.20] uh your your limit you know limitation
[L1436] [01:06:23.92] of you know being running polomial time
[L1437] [01:06:27.44] so it's you cannot solve this hard
[L1438] [01:06:30.08] instance you build many many instances
[L1439] [01:06:33.84] from a short seed you you start from
[L1440] [01:06:37.68] maybe a logarithmically
[L1441] [01:06:39.76] uh long seed you take many subsets of
[L1442] [01:06:43.12] this like n you need n of them and I ask
[L1443] [01:06:46.56] you for the value of the solution to
[L1444] [01:06:48.96] each one. Each one is hard but we want
[L1445] [01:06:51.44] to say that they are simultaneously
[L1446] [01:06:54.00] hard. You cannot tell them apart.
[L1447] [01:06:55.60] There's no correlation you can detect
[L1448] [01:06:57.60] between them even though they're
[L1449] [01:06:59.28] extremely correlated. So yeah, so we
[L1450] [01:07:01.76] have methods to do that as well. So
[L1451] [01:07:04.24] that's the connection you embed having a
[L1452] [01:07:06.48] hard problem to a limited observer means
[L1453] [01:07:10.00] that some uncertainty about the answer.
[L1454] [01:07:12.16] That's a key that's a starting point. So
[L1455] [01:07:15.12] when you say that the quality of the
[L1456] [01:07:18.08] randomness is a function of the
[L1457] [01:07:20.48] computational power of the observer, one
[L1458] [01:07:23.44] thought that comes to mind is imagine I
[L1459] [01:07:26.32] have um maybe infinite compute then then
[L1460] [01:07:31.04] nothing is truly random. Is that is that
[L1461] [01:07:34.48] accurate to say like you know if I had
[L1462] [01:07:36.40] infinite compute I the weather is not
[L1463] [01:07:39.28] random nothing is random. Uh okay. So
[L1464] [01:07:44.80] it points to the fact that you have to
[L1465] [01:07:47.28] really be careful about what question
[L1466] [01:07:49.36] you are asking about the randomness if
[L1467] [01:07:53.20] uh you want uh you know u to apply this
[L1468] [01:07:58.96] to to probabilistic algorithms
[L1469] [01:08:03.20] then it's really important that you are
[L1470] [01:08:05.52] limitless computationally. So if you
[L1471] [01:08:07.28] have infinite compute times you will be
[L1472] [01:08:09.60] able to distinguish
[L1473] [01:08:11.76] a a distribution with full entropy to
[L1474] [01:08:15.36] the random and one with coming from a
[L1475] [01:08:17.84] generator one with low entropy. So you
[L1476] [01:08:20.48] could do that but one thing you cannot
[L1477] [01:08:24.64] do with infinite compute is something
[L1478] [01:08:26.48] that's information theoretic. So there
[L1479] [01:08:29.60] are many other uh things we need to do
[L1480] [01:08:31.84] with random bits than just run probistic
[L1481] [01:08:35.76] algorithms. For example, we want to
[L1482] [01:08:37.44] generate passwords for our you know
[L1483] [01:08:40.40] crypto you know for uh security systems
[L1484] [01:08:46.32] there the very demand is that they are
[L1485] [01:08:50.24] random right I mean Shannon theorem
[L1486] [01:08:52.32] tells you you know the quality of your
[L1487] [01:08:55.04] passport is as good as the entropy in
[L1488] [01:08:57.20] it. So uh the notion of a cir secret
[L1489] [01:09:01.68] rests on the random on the true
[L1490] [01:09:04.72] randomness of the so if I just ask you
[L1491] [01:09:08.64] to produce a random beat or you ask me
[L1492] [01:09:11.04] to produce a random beat uh you know
[L1493] [01:09:14.32] whether you have computational infinite
[L1494] [01:09:17.36] computational power or not doesn't
[L1495] [01:09:20.16] matter I mean to generate this random
[L1496] [01:09:23.04] bit it has to be random I mean you your
[L1497] [01:09:25.44] demand is not that it will succeed in
[L1498] [01:09:27.52] some test you really want the
[L1499] [01:09:29.52] probability of heads to be half, tails
[L1500] [01:09:31.84] to be a half. This you know then this
[L1501] [01:09:35.52] definition or this task of producing
[L1502] [01:09:38.72] randomness
[L1503] [01:09:40.32] is not related to your computational
[L1504] [01:09:42.40] power.
[L1505] [01:09:45.36] So you know lucky or unlucky I don't
[L1506] [01:09:48.00] know for us many times we do have
[L1507] [01:09:51.68] implicit or explicit tests for this
[L1508] [01:09:54.40] randomness you say I can break this you
[L1509] [01:09:57.20] know I can break this system or
[L1510] [01:09:58.96] something and then you can maybe use to
[L1511] [01:10:01.68] the randomness but uh if your very
[L1512] [01:10:04.00] demand is to have a random event then
[L1513] [01:10:06.32] you need to produce a random event. I
[L1514] [01:10:08.56] saw in when I was doing my research that
[L1515] [01:10:12.24] there are ways to uh create higher
[L1516] [01:10:15.20] quality randomness by aggregating weaker
[L1517] [01:10:18.96] sources.
[L1518] [01:10:19.76] >> Yeah.
[L1519] [01:10:20.32] >> Um how how does that work?
[L1520] [01:10:22.72] >> Well, it's another theory. I talked
[L1521] [01:10:25.44] before about the theory of pseudo
[L1522] [01:10:26.96] randomness. There's a whole different
[L1523] [01:10:28.96] theory. They are related in non-trivial
[L1524] [01:10:31.76] ways, but uh um it's called the theory
[L1525] [01:10:35.68] of randomness extraction.
[L1526] [01:10:38.08] and or randomness purification maybe and
[L1527] [01:10:41.28] this is exactly what you asked about. Uh
[L1528] [01:10:44.24] we imagine that the world maybe does not
[L1529] [01:10:46.96] give us perfect randomness. But we have
[L1530] [01:10:48.88] all these events we cannot predict like
[L1531] [01:10:50.80] the weather uh or or various quantum
[L1532] [01:10:54.48] phenomena or sunspots or we cannot
[L1533] [01:10:57.92] predict the you know stock prices right
[L1534] [01:11:01.92] otherwise the market will be but these
[L1535] [01:11:05.36] are not you know even though these are
[L1536] [01:11:07.68] these are unpredictable events they are
[L1537] [01:11:10.40] somewhat predictable. I mean the weather
[L1538] [01:11:12.48] tomorrow is more likely to be similar to
[L1539] [01:11:14.88] the weather today than the opposite of
[L1540] [01:11:17.44] the weather. So there are correlations
[L1541] [01:11:19.84] if you sample this weather for example.
[L1542] [01:11:23.04] There are also biases. I mean sometimes
[L1543] [01:11:24.96] you you know in the spring it's more or
[L1544] [01:11:28.00] in the summer it's likely more likely to
[L1545] [01:11:30.08] be hot than cold.
[L1546] [01:11:33.20] So there are biases correlations. These
[L1547] [01:11:35.60] are called weak random sources and
[L1548] [01:11:37.60] there's a mathematical quantification of
[L1549] [01:11:41.36] uh how weak they are basically talk
[L1550] [01:11:45.68] about the amount of entropy in them. you
[L1551] [01:11:48.48] have n bits potentially you can have
[L1552] [01:11:50.48] entropy n but maybe they were generated
[L1553] [01:11:54.16] from a generator or they came from some
[L1554] [01:11:56.64] source of we don't know uh so it has
[L1555] [01:12:00.00] some entropy in it but you have no idea
[L1556] [01:12:01.76] where I mean maybe half of them are
[L1557] [01:12:04.72] fixed and half of them are cointosis and
[L1558] [01:12:08.72] you don't know which half maybe they are
[L1559] [01:12:10.96] each you know half you know three
[L1560] [01:12:14.80] quarter zero and one quart of you know
[L1561] [01:12:17.68] So tails have a bias that also has lots
[L1562] [01:12:20.48] of enthropy but not full and maybe the
[L1563] [01:12:23.28] correlations are even more complicated.
[L1564] [01:12:26.00] So you can imagine all sorts of
[L1565] [01:12:28.16] situation like this and you
[L1566] [01:12:29.60] mathematically model it by saying okay
[L1567] [01:12:32.88] there are n bits it's a probability
[L1568] [01:12:35.52] distribution n bits which has some
[L1569] [01:12:38.16] entropy let's say square root of n you
[L1570] [01:12:40.16] don't know where and uh you want to use
[L1571] [01:12:43.52] it in a probabilistic algorithm. So it's
[L1572] [01:12:46.16] a basic question. Can we use physical
[L1573] [01:12:48.96] events
[L1574] [01:12:50.56] uh weak sources coming from nature maybe
[L1575] [01:12:53.84] uh in in probabistic algorithms and
[L1576] [01:12:57.52] certainly not obvious. I mean just
[L1577] [01:12:59.28] feeding them to the algorithm as is not
[L1578] [01:13:02.56] going to work. They are very easy to
[L1579] [01:13:04.40] find simple algorithms that will fail
[L1580] [01:13:06.88] that will succeed on perfect randomness
[L1581] [01:13:08.88] and will fail on will always make an
[L1582] [01:13:11.92] error.
[L1583] [01:13:14.24] But uh the theory of randomness
[L1584] [01:13:17.76] purification wants to take this
[L1585] [01:13:21.04] um this um uh sample of n bits with all
[L1586] [01:13:27.04] with some amount of entropy which is not
[L1587] [01:13:29.44] full and someone massage it create from
[L1588] [01:13:32.56] it maybe a shorter string which is u you
[L1589] [01:13:38.56] know of higher quality. Ideally it would
[L1590] [01:13:41.12] be perfect random bits. So ideally you
[L1591] [01:13:43.52] can imagine that if I have n random bits
[L1592] [01:13:46.08] and I have enthropy root n maybe I can
[L1593] [01:13:48.96] massage out of there square root n or
[L1594] [01:13:52.16] maybe just the fourth root of n
[L1595] [01:13:55.28] bits that will be essentially uniformly
[L1596] [01:13:58.88] distributed then if I have an algorithm
[L1597] [01:14:01.20] that just needs this amount that's what
[L1598] [01:14:03.92] I feel it turns out you cannot do that
[L1599] [01:14:08.16] it's impossible but what you can do is
[L1600] [01:14:10.96] not produce one string of length let's
[L1601] [01:14:15.76] say square root 10 but you can com you
[L1602] [01:14:18.96] can produce n to the hund of them
[L1603] [01:14:22.64] okay and what you are guaranteed so this
[L1604] [01:14:25.36] is a this randomness purification uh
[L1605] [01:14:28.32] device is an efficient algorithm that
[L1606] [01:14:30.24] takes any any uh distribution with
[L1607] [01:14:33.60] enthalpy in it and you produce many
[L1608] [01:14:37.12] blocks polomally many blocks of the
[L1609] [01:14:39.76] length roughly the enthalpy what you
[L1610] [01:14:41.92] would hope to be perfect and what you
[L1611] [01:14:45.12] are guaranteed is that 99% of them are
[L1612] [01:14:52.40] truly perfect. So you have many
[L1613] [01:14:57.36] 99% of them are as good as perfect and
[L1614] [01:15:01.92] there's 1% which is bad. You don't know
[L1615] [01:15:03.92] which it is. But that's already solves
[L1616] [01:15:06.00] your problem because run your algorithm
[L1617] [01:15:08.48] on each one of them. take a majority
[L1618] [01:15:11.12] vote. Doing this is extremely
[L1619] [01:15:13.84] complicated. There are many ways of
[L1620] [01:15:15.84] doing it. There are varants of you know
[L1621] [01:15:18.80] various assumptions you can make about
[L1622] [01:15:20.48] the entropy. Maybe you have several weak
[L1623] [01:15:23.28] sources that are not related to each
[L1624] [01:15:25.28] other. There are various
[L1625] [01:15:28.16] um uh yeah the various variants and this
[L1626] [01:15:31.52] theory is very well developed. But we
[L1627] [01:15:34.08] know that uh uh the statement I made
[L1628] [01:15:38.16] essentially is is accurate. If you have
[L1629] [01:15:41.60] one source uh with some entropy in it,
[L1630] [01:15:44.56] you can generate polomially many samples
[L1631] [01:15:47.04] of the length of almost the entropy and
[L1632] [01:15:50.00] most of them will be perfect. So that's
[L1633] [01:15:54.32] as useful as having one. Yeah. I vaguely
[L1634] [01:15:57.12] remember I was skimming a bunch of
[L1635] [01:15:59.28] papers and one of the papers it had this
[L1636] [01:16:01.20] uh had this figure where it was a
[L1637] [01:16:03.92] two-dimensional array of numbers and I
[L1638] [01:16:06.00] think there were like drawing rectangles
[L1639] [01:16:07.92] or something like that. Is that like one
[L1640] [01:16:10.16] of the ideas? Uh so it's a notion of
[L1641] [01:16:12.56] pseudo randomness which is related to uh
[L1642] [01:16:16.72] one particular variant of this
[L1643] [01:16:18.88] extraction problem where you have
[L1644] [01:16:21.76] several weak sources not one one is the
[L1645] [01:16:24.48] hardest because that's yeah but maybe
[L1646] [01:16:27.12] you have a few that are independent and
[L1647] [01:16:30.00] each of them has some entropy in it
[L1648] [01:16:33.68] and uh I think what you're referring to
[L1649] [01:16:35.92] is this sum product theorem this uh uh
[L1650] [01:16:40.08] yeah I cannot draw the pictures of there
[L1651] [01:16:42.56] but uh you don't really need to. So
[L1652] [01:16:45.68] let's just think about this problem. You
[L1653] [01:16:47.44] have uh uh three sources of randomness.
[L1654] [01:16:52.56] They are each weak. So each has just a
[L1655] [01:16:55.12] little bit of entropy in it. And all you
[L1656] [01:16:57.52] want to produce is one source with
[L1657] [01:17:01.20] somewhat larger entropy. So you are
[L1658] [01:17:03.52] losing in the number of sources but you
[L1659] [01:17:06.08] are gaining entropy. If you can repeat
[L1660] [01:17:08.08] this, you eventually get to full
[L1661] [01:17:10.56] entropy. So that's the idea. So what how
[L1662] [01:17:14.40] what combination of weak sources would
[L1663] [01:17:16.64] you take? It's not obvious and the
[L1664] [01:17:20.72] solution. Yeah, this is a certainly
[L1665] [01:17:24.16] there is maybe even this one. Uh there's
[L1666] [01:17:27.28] a paper I have with Barak and Impalato
[L1667] [01:17:29.52] about this particular problem and we are
[L1668] [01:17:32.32] using a result in what's called the
[L1669] [01:17:35.12] arithmetic combinatorics and I can
[L1670] [01:17:37.12] explain it very simply. I think that we
[L1671] [01:17:41.36] learn about addition in second grade and
[L1672] [01:17:44.32] about multiplication third grade maybe
[L1673] [01:17:47.52] and you know the only motivation for
[L1674] [01:17:50.32] multiplication is that it's a way to
[L1675] [01:17:53.68] shortcut repeated addition
[L1676] [01:17:56.72] and that's all we talk about. Then if
[L1677] [01:17:58.56] you go to college you you learn that you
[L1678] [01:18:01.92] know sum and products are the basic
[L1679] [01:18:03.92] operations of fields. You can do it with
[L1680] [01:18:06.48] integers. You can do it with rational
[L1681] [01:18:09.36] numbers, complex numbers, finite fields
[L1682] [01:18:11.84] and so on. So you remember these are the
[L1683] [01:18:14.32] basic but how do they relate to each
[L1684] [01:18:16.56] other?
[L1685] [01:18:18.32] It's not clear. It's not maybe there are
[L1686] [01:18:20.64] many ways to ask this question but one
[L1687] [01:18:23.28] way to ask this question that was
[L1688] [01:18:24.88] suggested by Erdesh and was
[L1689] [01:18:29.28] solved the first time by Erdish and
[L1690] [01:18:31.04] Seamar and then in a much more in a form
[L1691] [01:18:34.40] we really need by
[L1692] [01:18:36.96] Kent to say the following just think of
[L1693] [01:18:40.00] a set of integers
[L1694] [01:18:42.32] and add all pairs so you start with
[L1695] [01:18:44.72] let's say K integers add all pairs how
[L1696] [01:18:47.76] many new integers Do you get this you
[L1697] [01:18:50.64] should think of as entropy increase if
[L1698] [01:18:53.44] you get many more somehow? Yeah. So you
[L1699] [01:18:58.00] have K integers. Well, it depends what
[L1700] [01:19:00.00] they are. I mean if there are the first
[L1701] [01:19:02.88] K integers and you add all pairs up, you
[L1702] [01:19:05.44] get just the number between one and 2 K.
[L1703] [01:19:09.12] That's not much larger. That's a factor
[L1704] [01:19:11.04] or two larger. If you want increase an
[L1705] [01:19:13.12] entropy, you want to get you know uh
[L1706] [01:19:16.56] some power of k bigger than one.
[L1707] [01:19:20.56] Of course, if you take a random set of
[L1708] [01:19:22.24] integers,
[L1709] [01:19:23.76] uh you'll get k square, they will all be
[L1710] [01:19:26.16] distinct k² integers. So somehow you
[L1711] [01:19:30.40] want to say I mean it would be great if
[L1712] [01:19:33.36] for any set when you take all pairs you
[L1713] [01:19:36.48] group but it's not true by this example
[L1714] [01:19:39.84] of the interval. Well, you can not take
[L1715] [01:19:42.96] sums. You can take products.
[L1716] [01:19:46.00] Okay? But also products don't always
[L1717] [01:19:48.08] increase. If you take, you know, one,
[L1718] [01:19:50.88] two, four, eight, you take a geometric
[L1719] [01:19:54.08] progression, you multiply all pairs,
[L1720] [01:19:56.32] you'll just get just twice as many as
[L1721] [01:19:59.28] you start. So that's uh it's also not
[L1722] [01:20:03.68] good. And uh the magic in this sum
[L1723] [01:20:06.80] product theorem is that
[L1724] [01:20:09.36] sums and products are orthogonal to each
[L1725] [01:20:12.64] other. Somehow if one of them fails to
[L1726] [01:20:16.08] grow a set then the other will grow this
[L1727] [01:20:19.04] set.
[L1728] [01:20:21.20] And so this is an amazing result and the
[L1729] [01:20:25.44] way you use it in this context you think
[L1730] [01:20:27.52] of the outcome of your sources as
[L1731] [01:20:29.92] numbers.
[L1732] [01:20:31.60] you let's say multiply the first pair
[L1733] [01:20:35.28] and add them to the third you mix the
[L1734] [01:20:38.64] sum product. So this guarantees even
[L1735] [01:20:42.08] this is not obvious but if you do this
[L1736] [01:20:44.80] it guarantees that you you grow the
[L1737] [01:20:47.68] number of different values you get is
[L1738] [01:20:50.96] significantly more than K maybe it's K
[L1739] [01:20:53.20] to the 1.5 or something entropy does
[L1740] [01:20:56.56] increase and that's that's the source of
[L1741] [01:20:59.92] you need to prove it distributionally
[L1742] [01:21:01.92] it's not just the size the entropy is
[L1743] [01:21:04.00] not just size
[L1744] [01:21:05.92] um along with the size it's more than
[L1745] [01:21:08.24] that but anyway this is behind one
[L1746] [01:21:11.60] solution to one of the problems about
[L1747] [01:21:13.84] purification. It does not solve the one
[L1748] [01:21:17.28] source problem. This you need other
[L1749] [01:21:19.52] tools.
[L1750] [01:21:20.72] >> I saw that um you had done some work in
[L1751] [01:21:23.52] zero knowledge proofs. I was wondering
[L1752] [01:21:25.04] if you could explain you know what is a
[L1753] [01:21:26.96] zero knowledge proof and maybe we talk
[L1754] [01:21:28.48] about its significance.
[L1755] [01:21:30.40] >> Sure. Yeah. Z knowledge proof it's
[L1756] [01:21:32.72] pretty amazing that it became a
[L1757] [01:21:34.32] household word. I mean it was in the
[L1758] [01:21:38.64] domain of theorists for a long time. Uh
[L1759] [01:21:42.40] the original definition of zero
[L1760] [01:21:44.80] knowledge proof came in a paper seminar
[L1761] [01:21:47.04] paper of
[L1762] [01:21:48.96] uh Goldster Mi and Rakov
[L1763] [01:21:52.72] which also contained the definition of
[L1764] [01:21:55.04] interactive proof. So even before zero
[L1765] [01:21:57.44] knowledge uh they conceived of the
[L1766] [01:22:00.72] notion that proofs don't have to be
[L1767] [01:22:02.96] written down like in mathematical
[L1768] [01:22:04.64] papers.
[L1769] [01:22:07.04] people can have a discussion a
[L1770] [01:22:08.64] randomized discussion in which I'll try
[L1771] [01:22:10.64] to convince you of something or I I want
[L1772] [01:22:13.68] to prove to you something like I know
[L1773] [01:22:15.44] the uh you know the proof of the Roman
[L1774] [01:22:18.40] hypothesis or I can solve this suduku
[L1775] [01:22:20.56] puzzle and uh we can do it interactively
[L1776] [01:22:24.80] with the rand you know we are randomized
[L1777] [01:22:26.88] in particular you the verifier of my
[L1778] [01:22:30.24] claim are allowed to be randomized so
[L1779] [01:22:32.48] it's like in randomized algorithms but
[L1780] [01:22:34.56] Now the prover there's a prover it's not
[L1781] [01:22:37.52] just an algorith it's a prover like in
[L1782] [01:22:39.52] NP someone who knows the solution but
[L1783] [01:22:42.32] the convincing has this interactive
[L1784] [01:22:45.28] uh form so this model was suggested in
[L1785] [01:22:47.92] this paper and also in a paper of babai
[L1786] [01:22:51.52] parallel in the same time from different
[L1787] [01:22:54.24] motivations
[L1788] [01:22:56.08] uh
[L1789] [01:22:57.84] basically it offers a generalization of
[L1790] [01:23:00.32] the notion of np
[L1791] [01:23:03.84] is That's when I send you a message and
[L1792] [01:23:06.00] it convinces you. You verify it and it
[L1793] [01:23:08.16] convinces you. Now we allow an
[L1794] [01:23:10.96] interaction and we allow you you know a
[L1795] [01:23:14.80] small chance because you are randomized.
[L1796] [01:23:16.48] We allow small chance that you will uh
[L1797] [01:23:19.44] you know I will convince you of a false
[L1798] [01:23:21.28] claim but this error can be reduced like
[L1799] [01:23:24.32] in probabilistic algorithms can be
[L1800] [01:23:26.08] reduced arbitrarily. You want one in a
[L1801] [01:23:28.00] billion you can get one in a billion
[L1802] [01:23:30.08] whatever. Yeah. Anyway, so there's a
[L1803] [01:23:32.72] notion of an interactive proof and then
[L1804] [01:23:37.04] uh in the gold mali of paper they
[L1805] [01:23:40.32] suggested
[L1806] [01:23:41.84] another
[L1807] [01:23:43.68] notion of interactive proof which is
[L1808] [01:23:45.52] more restricted. You want to prove
[L1809] [01:23:47.60] something but the zero knowledge means
[L1810] [01:23:51.36] that you want the verifier to learn
[L1811] [01:23:54.88] nothing absolutely nothing about the
[L1812] [01:23:56.72] proof except that it's true.
[L1813] [01:24:01.04] Now this sounds really totally
[L1814] [01:24:03.36] ridiculous. I mean if you think about
[L1815] [01:24:05.20] the last time you convince somebody
[L1816] [01:24:08.16] uh to change their mind about anything
[L1817] [01:24:10.24] without providing them any any knowledge
[L1818] [01:24:13.60] any new things they didn't know. Say
[L1819] [01:24:15.92] what what are you talking about? This
[L1820] [01:24:18.08] such proofs don't exist for anything
[L1821] [01:24:20.64] there. No zero knowledge for anything.
[L1822] [01:24:23.52] Uh they were not thinking about you know
[L1823] [01:24:26.88] uh convincing someone of you know
[L1824] [01:24:29.20] political opinion. they were thinking
[L1825] [01:24:31.12] about cryptography of course you know
[L1826] [01:24:35.20] they've created the foundation of
[L1827] [01:24:37.28] cryptography in many in many other
[L1828] [01:24:39.28] papers um but they are imagining uh uh
[L1829] [01:24:44.24] cryptographic protocols in which you
[L1830] [01:24:46.08] have secrets and you you use these
[L1831] [01:24:48.80] secrets in your computation
[L1832] [01:24:51.12] and you have you know the protocol tells
[L1833] [01:24:54.32] you to do things that if you don't then
[L1834] [01:24:57.76] you know you're violating the protocol.
[L1835] [01:25:00.08] So the others don't want you to cheat.
[L1836] [01:25:02.88] They want to make sure you perform the
[L1837] [01:25:04.88] right operations on your secrets.
[L1838] [01:25:07.68] Uh for example, you are supposed to pick
[L1839] [01:25:09.68] a a public key by multiplying two uh
[L1840] [01:25:14.40] prime numbers. If you multiply three
[L1841] [01:25:18.56] or something else,
[L1842] [01:25:20.88] then you you are violating the protocol
[L1843] [01:25:23.44] and maybe security is not guaranteed. So
[L1844] [01:25:25.84] I would like to convince you that the
[L1845] [01:25:27.52] number I give you is actually a product
[L1846] [01:25:29.92] of two primes. I certainly don't want to
[L1847] [01:25:32.24] give you the two primes. So what I
[L1848] [01:25:35.36] really want to convince you of is that I
[L1849] [01:25:38.32] computed this number by multiplying two
[L1850] [01:25:42.08] primes. And you learn from this
[L1851] [01:25:44.88] interaction
[L1852] [01:25:46.80] absolutely nothing except you are
[L1853] [01:25:48.64] convinced with very high probability
[L1854] [01:25:51.20] that I did multiply two primes and not
[L1855] [01:25:53.52] any other number and I didn't do
[L1856] [01:25:55.20] anything else that I shouldn't have. And
[L1857] [01:25:57.76] you can think about lots of other
[L1858] [01:26:00.24] cryptographic protocols where people are
[L1859] [01:26:03.12] doing things like multi-party
[L1860] [01:26:04.80] computation very complex things they are
[L1861] [01:26:07.28] confusing with their secrets and they
[L1862] [01:26:10.80] don't want to reveal them whereas the
[L1863] [01:26:13.04] others want to make sure that they did
[L1864] [01:26:14.80] what they should. So there are any
[L1865] [01:26:17.12] number of you know applications to this
[L1866] [01:26:19.76] idea. The only problem is it sounds
[L1867] [01:26:22.40] ridiculous because it sounds impossible
[L1868] [01:26:24.88] in mathematics terms. If
[L1869] [01:26:28.08] uh you know some somebody came here and
[L1870] [01:26:30.64] said that P you know they prove P
[L1871] [01:26:33.68] different than NP you know I I would
[L1872] [01:26:36.64] want to see the proof and then tell me
[L1873] [01:26:38.56] okay I prove it to you in zero. How can
[L1874] [01:26:40.56] anybody convince me that they have a
[L1875] [01:26:43.76] proof of P different than NP and I come
[L1876] [01:26:46.16] out you know congratulating them and you
[L1877] [01:26:49.68] know
[L1878] [01:26:51.84] uh amazed by them and nevertheless I
[L1879] [01:26:55.04] know absolutely nothing about the way
[L1880] [01:26:56.88] they proved it. I'm I just know that
[L1881] [01:26:58.80] they did this. So it really sounds
[L1882] [01:27:01.76] ridiculous
[L1883] [01:27:03.68] and uh yeah certainly one of my favorite
[L1884] [01:27:08.56] papers maybe my favorite is the zero
[L1885] [01:27:11.68] paper which came a year later is joined
[L1886] [01:27:14.32] with Od and Sylvio Mikalli where we saw
[L1887] [01:27:18.56] that it's not only not ridiculous it's
[L1888] [01:27:21.04] universal
[L1889] [01:27:22.72] namely anything which has a proof a
[L1890] [01:27:25.28] mathematical proof also has a zero
[L1891] [01:27:28.64] knowledge interactive proof Anything
[L1892] [01:27:30.96] like P different than NP or that I
[L1893] [01:27:34.00] multiply two primes or anything that you
[L1894] [01:27:36.56] can prove revealing your secret you can
[L1895] [01:27:39.60] prove without revealing your secret and
[L1896] [01:27:41.92] convince beyond any reasonable doubt. So
[L1897] [01:27:45.60] that's possible.
[L1898] [01:27:46.72] >> What's the intuition behind that? Like
[L1899] [01:27:49.44] let's say I have a proof for P= MP and
[L1900] [01:27:51.84] we want to convert it to a zero
[L1901] [01:27:53.52] knowledge proof. How does that work?
[L1902] [01:27:55.44] >> How does this work? Well, first of all,
[L1903] [01:27:57.60] it assumes cryptography. So we assume we
[L1904] [01:28:00.00] have some oneway functions. We we assume
[L1905] [01:28:03.12] that some you know problem like factor
[L1906] [01:28:05.52] integers or this logarithm or any number
[L1907] [01:28:09.28] of oneway believed oneway functions uh
[L1908] [01:28:13.28] exist. So oneway functions if people
[L1909] [01:28:16.00] don't know functions that are easy to
[L1910] [01:28:18.64] compute in one way but are hard to
[L1911] [01:28:21.20] invert. For example multiplying numbers
[L1912] [01:28:23.28] is easy.
[L1913] [01:28:25.44] Finally the factors of a number which is
[L1914] [01:28:27.44] the inverse problem the prime factor is
[L1915] [01:28:30.72] believed to be hard of course we never
[L1916] [01:28:33.36] we can never we don't know any hard
[L1917] [01:28:36.00] problem that's the previous entry
[L1918] [01:28:37.60] question we don't know but we believe
[L1919] [01:28:40.16] about many problems and we the belief is
[L1920] [01:28:42.48] actually the whole world believe because
[L1921] [01:28:44.64] the whole world is using cryptographic
[L1922] [01:28:48.00] systems which rest on this all
[L1923] [01:28:50.80] electronic commerce assumes this so we
[L1924] [01:28:53.52] assume this so assume we
[L1925] [01:28:56.32] uh oneway functions uh oneway functions
[L1926] [01:28:59.68] allow you to uh create uh basically
[L1927] [01:29:04.08] garbled message commitments. I can uh
[L1928] [01:29:08.80] you know I have a number in my head I
[L1929] [01:29:12.72] don't want to tell you what the number
[L1930] [01:29:14.24] is. It's a number between one and 100. I
[L1931] [01:29:17.28] can write down another number
[L1932] [01:29:21.84] which looks like a random number to you.
[L1933] [01:29:25.20] And on the one hand you have no idea
[L1934] [01:29:29.52] I claim this encodes my secret. Okay.
[L1935] [01:29:33.28] And this commitment scheme which is
[L1936] [01:29:35.76] built very simply for one for monary
[L1937] [01:29:38.08] functions uh guarantees two properties.
[L1938] [01:29:40.96] A you cannot tell what is my secret even
[L1939] [01:29:44.32] though you can see this number this
[L1940] [01:29:45.92] other number I gave you. And uh on the
[L1941] [01:29:50.24] other hand I cannot change my mind about
[L1942] [01:29:53.36] my secret. It really commits me to the
[L1943] [01:29:56.96] uh so I can later provide you with a
[L1944] [01:29:59.92] certificate that I was thinking about 17
[L1945] [01:30:03.76] and I can only do it for 17. I cannot do
[L1946] [01:30:06.40] it for any other number. Okay. In fact a
[L1947] [01:30:10.32] very simple example is really using
[L1948] [01:30:12.00] factoring. uh in some sense the product
[L1949] [01:30:15.44] of two primes this number
[L1950] [01:30:19.60] uh you know it's easy you know this
[L1951] [01:30:23.12] number
[L1952] [01:30:24.72] uh commits it to its factors it uniquely
[L1953] [01:30:27.76] defines its factors right the only
[L1954] [01:30:30.24] problem is this is not exactly random
[L1955] [01:30:32.48] products of primes it's yeah but you can
[L1956] [01:30:35.28] do so you can do this okay so now uh
[L1957] [01:30:39.76] that we have to take commitments are
[L1958] [01:30:41.84] possible that's veryant important
[L1959] [01:30:44.64] uh so I'm I'm describing very high level
[L1960] [01:30:47.36] I'm hiding lots of things and even the
[L1961] [01:30:49.28] definition of zero knowledge the formal
[L1962] [01:30:52.08] definition is quite intricate it's not
[L1963] [01:30:55.20] the intuition is obvious and I said it
[L1964] [01:30:58.32] uh but actually formally defining is
[L1965] [01:31:00.64] non-trivial but at a high level I I'll
[L1966] [01:31:03.28] give you some idea about how a zero
[L1967] [01:31:05.20] knows proof looks like now we have to
[L1968] [01:31:07.76] think about what theorems am I proving
[L1969] [01:31:09.84] to you and it was very important to us
[L1970] [01:31:13.36] to uh figure out what problem to uh
[L1971] [01:31:16.56] think about even though today you can do
[L1972] [01:31:19.20] it for others but we were thinking about
[L1973] [01:31:22.56] uh theorems of the type here's the graph
[L1974] [01:31:25.44] we can color it in three colors it's
[L1975] [01:31:28.40] also a formal mathematical statement
[L1976] [01:31:30.32] either it's doable or not right and we
[L1977] [01:31:32.88] want we uh simply focus on proving in
[L1978] [01:31:36.64] zero knowledge claims of this type okay
[L1979] [01:31:40.88] the graph we both know I claim I can
[L1980] [01:31:43.36] colorize with three colors. You don't
[L1981] [01:31:45.84] believe me. You want to [clears throat]
[L1982] [01:31:46.80] be convinced of this fact and you don't
[L1983] [01:31:50.00] want me to cheat you. You don't want me
[L1984] [01:31:51.76] to be able to you know should be an
[L1985] [01:31:54.08] interactive proof and moreover we want
[L1986] [01:31:57.20] it I want it to be zero energy. I don't
[L1987] [01:31:59.36] want you to have a slightest idea of
[L1988] [01:32:01.60] what my coloring is or what anything you
[L1989] [01:32:04.32] didn't know before is okay. So roughly
[L1990] [01:32:08.32] the uh way it works the honor is proof
[L1991] [01:32:11.52] for this particular set of claims that
[L1992] [01:32:14.72] are certainly not all claims they are
[L1993] [01:32:17.20] very structured claims we look like the
[L1994] [01:32:20.00] following we iteratively repeat the
[L1995] [01:32:23.28] following procedure
[L1996] [01:32:25.52] I put commitments for the coloring
[L1997] [01:32:30.88] on every vertx I tell you you know I
[L1998] [01:32:33.36] don't tell you it's green red or blue
[L1999] [01:32:35.68] but I put a commitment to one of them on
[L2000] [01:32:39.04] each vertex.
[L2001] [01:32:41.12] You will choose at random an edge of the
[L2002] [01:32:45.44] graph and ask me to open these two
[L2003] [01:32:48.96] envelopes
[L2004] [01:32:50.96] to decommit.
[L2005] [01:32:53.28] And you will check that the colors you
[L2006] [01:32:55.60] see first of all are in this set. They
[L2007] [01:32:57.68] are not gray or orange. They are either
[L2008] [01:33:00.16] red, green or blue. And that they are
[L2009] [01:33:02.40] different.
[L2010] [01:33:04.24] This should give you some maybe slight
[L2011] [01:33:06.96] uh you know slight advantage or slight
[L2012] [01:33:10.72] uh support to the belief that maybe I'm
[L2013] [01:33:12.96] not cheating you. Of course, it's a very
[L2014] [01:33:15.04] limited one because I can cheat you in
[L2015] [01:33:17.12] some corner other. Yeah. So we have to
[L2016] [01:33:20.56] to establish two things. We will repeat
[L2017] [01:33:23.20] this again and again. We have to
[L2018] [01:33:25.52] establish that it's a you know that it's
[L2019] [01:33:28.00] a proof. It's an interactive proof that
[L2020] [01:33:30.40] I cannot cheat you. And we have to argue
[L2021] [01:33:32.48] the zon part. Okay. So let's do one at a
[L2022] [01:33:36.00] time. Uh to uh
[L2023] [01:33:42.88] do the the correctness that I cannot
[L2024] [01:33:45.60] fool you is very simple is the
[L2025] [01:33:48.16] following.
[L2026] [01:33:49.68] If the graph is not three colorable
[L2027] [01:33:52.40] whatever I commit for there's one place
[L2028] [01:33:55.28] which is an error. Either it has the
[L2029] [01:33:57.20] wrong color and not allowed color or two
[L2030] [01:33:59.76] colors are equal. you have some nonrival
[L2031] [01:34:03.04] chance of catching this with your random
[L2032] [01:34:06.00] guess right I mean it's one over the
[L2033] [01:34:07.84] number of edges not so small if you
[L2034] [01:34:10.56] graph on on you know with 100 edges it's
[L2035] [01:34:14.08] one in 100 if thousands if we repeat it
[L2036] [01:34:17.60] not thousand but 10,000 times the
[L2037] [01:34:20.48] probability that you don't catch me in
[L2038] [01:34:22.56] any of them drops exponentially to zero
[L2039] [01:34:26.48] right so
[L2040] [01:34:28.32] uh of Because there's a Okay, so this
[L2041] [01:34:32.56] this establishes that I cannot fool you.
[L2042] [01:34:36.08] The zeon knowledge is a more serious
[L2043] [01:34:38.40] problem because if I keep using the same
[L2044] [01:34:41.92] coloring,
[L2045] [01:34:43.52] you will ask me about this edge and this
[L2046] [01:34:45.68] edge and then eventually you'll know the
[L2047] [01:34:47.36] coloring of all colors.
[L2048] [01:34:50.16] Here's something that's really special
[L2049] [01:34:52.00] to the coloring that is being used. If I
[L2050] [01:34:55.60] have one coloring of the graph, I really
[L2051] [01:34:58.32] have six because I can peruse the name
[L2052] [01:35:01.36] there. I can replace red and green and
[L2053] [01:35:03.28] it's another valid coloring.
[L2054] [01:35:06.08] So what I do really in each one of these
[L2055] [01:35:08.48] iterations is not using the same
[L2056] [01:35:10.40] coloring but using a random one of these
[L2057] [01:35:13.44] possible six
[L2058] [01:35:15.84] that they are legal. They are all legal
[L2059] [01:35:18.08] and I I just use one of these six.
[L2060] [01:35:21.20] What's the advantage of this? when you
[L2061] [01:35:23.52] open a pair of vertices under this
[L2062] [01:35:26.24] distribution one of the six what you
[L2063] [01:35:28.48] will see if I do have a coloring and
[L2064] [01:35:30.96] that's the only I want to stress we only
[L2065] [01:35:33.36] have to establish zero knowledge if I
[L2066] [01:35:35.12] really can prove the theorem so if I if
[L2067] [01:35:37.60] I do know the solution the proof I want
[L2068] [01:35:40.64] to protect my knowledge
[L2069] [01:35:43.44] what happens when I reveal to you
[L2070] [01:35:46.80] two of these colors on the adjacent
[L2071] [01:35:49.76] vertices of the graph
[L2072] [01:35:52.64] It will be two in this distribution when
[L2073] [01:35:55.44] you restrict it to two vertices. It will
[L2074] [01:35:58.00] simply be two different random colors.
[L2075] [01:36:01.04] Right? This is what you get by all
[L2076] [01:36:02.72] permutations. This experimentation
[L2077] [01:36:05.20] what did you learn from this? Nothing.
[L2078] [01:36:07.68] You could have picked two random
[L2079] [01:36:09.28] different colors. You didn't need me for
[L2080] [01:36:11.44] that. So you didn't learn anything. So
[L2081] [01:36:14.24] in each iteration you learn nothing.
[L2082] [01:36:17.60] So this is the idea of the proof. Well,
[L2083] [01:36:20.96] this is the the end of the proof that I
[L2084] [01:36:24.00] can you know that showing that there's
[L2085] [01:36:26.40] there are zero knowledge proofs for all
[L2086] [01:36:29.68] u graph coloring three coloring
[L2087] [01:36:32.08] problems. What about all the rimonite
[L2088] [01:36:34.64] processes and the previous npn factoring
[L2089] [01:36:37.68] and all these other things I want to
[L2090] [01:36:39.20] claim to you and prove with zero and
[L2091] [01:36:40.96] everything here is very simple. You use
[L2092] [01:36:44.16] np completeness. This is an NP complete
[L2093] [01:36:46.80] problem. Anything can be that can be
[L2094] [01:36:49.68] proved is really something in NP. Right?
[L2095] [01:36:52.64] This is the definition. So you reduce it
[L2096] [01:36:55.68] to three color. You prove it in zero
[L2097] [01:36:57.52] knowledge. And and the main point about
[L2098] [01:37:00.80] reductions in NP is that they don't only
[L2099] [01:37:05.04] uh convert the you know the yes no
[L2100] [01:37:07.20] answer in a consistent way that if this
[L2101] [01:37:10.08] sort of this sable but actually if you
[L2102] [01:37:12.56] have a a witness if you have a proof for
[L2103] [01:37:15.84] I don't know whatever it will become a a
[L2104] [01:37:20.48] a legal three coloring of the graph you
[L2105] [01:37:22.80] generate. So if you have a proof you can
[L2106] [01:37:24.88] also have the three coloring. is very
[L2107] [01:37:26.80] important that the reduction
[L2108] [01:37:30.40] also provides a translation not just
[L2109] [01:37:33.04] between the instances but also between
[L2110] [01:37:35.36] the proofs. So NP completeness theory
[L2111] [01:37:38.48] gives you for free that if you solve the
[L2112] [01:37:40.56] problem for graph coloring instances you
[L2113] [01:37:43.92] solve it for any you can prove anything
[L2114] [01:37:46.24] in zero knowledge.
[L2115] [01:37:47.44] >> So um with the zero knowledge proofs you
[L2116] [01:37:50.80] can never be 100% sure. No
[L2117] [01:37:53.60] >> okay but practically I mean
[L2118] [01:37:56.32] exponentially approaching
[L2119] [01:37:57.84] >> you can make you can make the
[L2120] [01:37:59.68] completeness
[L2121] [01:38:01.60] uh 100% namely if I do have a proof you
[L2122] [01:38:05.04] will be yeah there will be no error in
[L2123] [01:38:07.20] your but there is a slight possibility
[L2124] [01:38:09.92] that the graph is not three coloring not
[L2125] [01:38:12.40] three colorable and you will not catch
[L2126] [01:38:14.08] me you can make this exponentially small
[L2127] [01:38:16.72] you cannot make it zero
[L2128] [01:38:18.40] >> when I think of cryptography oneway
[L2129] [01:38:20.56] functions there's this idea of you
[L2130] [01:38:22.96] quantum computation that's kind of
[L2131] [01:38:25.28] changed uh complexity theory a bit and
[L2132] [01:38:28.64] >> big time. Yeah.
[L2133] [01:38:30.24] >> Yeah. And I wanted to ask your thoughts
[L2134] [01:38:32.16] on you know how quantum computation or
[L2135] [01:38:35.36] that model of uh computation is changing
[L2136] [01:38:39.76] uh complexity theory like what are the
[L2137] [01:38:41.60] big takeaways?
[L2138] [01:38:43.12] >> Okay, let me say what it is first of
[L2139] [01:38:44.96] all. I mean uh yeah uh quantum mechanics
[L2140] [01:38:48.16] is a theory of nature that you know
[L2141] [01:38:50.80] seems to be everybody believes and
[L2142] [01:38:53.52] accepts. So uh like with randomness we
[L2143] [01:38:57.44] can ask why not enhance computers with
[L2144] [01:39:00.80] you know this physical knowledge. We
[L2145] [01:39:02.72] allow uh our computers to operate in the
[L2146] [01:39:06.56] you know ways that quantum mechanics
[L2147] [01:39:09.52] dictates namely manipulate
[L2148] [01:39:12.24] bits in superposition using unitary
[L2149] [01:39:14.80] operations whatever this means but you
[L2150] [01:39:17.84] know according to the rules of uh
[L2151] [01:39:20.32] quantum mechanics and uh really strange
[L2152] [01:39:24.32] things happen in quantum mechanics I'm
[L2153] [01:39:26.24] sure many many people know because you
[L2154] [01:39:28.96] know you can there are all these
[L2155] [01:39:30.96] interference pattern turns you. Yeah, it
[L2156] [01:39:34.16] seems that uh you know you can uh u
[L2157] [01:39:38.56] basically you are working with
[L2158] [01:39:39.84] probability theory with negative
[L2159] [01:39:41.60] numbers. Events cannot uh you know
[L2160] [01:39:44.88] aggregate only they can cancel each
[L2161] [01:39:47.04] other and uh okay so it's a model of
[L2162] [01:39:51.28] computation. It's a generalization of uh
[L2163] [01:39:54.56] touring machines. In fact it's
[L2164] [01:39:55.92] generalization of randomized touring
[L2165] [01:39:58.08] machine. It's very easy to see that uh a
[L2166] [01:40:02.40] quantum computer is at least as strong
[L2167] [01:40:04.40] as a proistic computer. How do you see
[L2168] [01:40:06.96] it? You just measure the quantum bits
[L2169] [01:40:09.20] before you start. You measure them. This
[L2170] [01:40:12.08] what I mentioned about the photons in
[L2171] [01:40:14.00] the beginning. If you you have a some
[L2172] [01:40:16.72] basic superposition on I mean quantum
[L2173] [01:40:19.68] quantum bit if you measure it you get a
[L2174] [01:40:22.16] random bit. So because of that quantum
[L2175] [01:40:25.12] computers are at least as strong as
[L2176] [01:40:27.52] proistic computers. uh okay so it's a
[L2177] [01:40:31.44] model of computation and uh it was
[L2178] [01:40:34.56] suggested in the 80s fineman
[L2179] [01:40:38.96] uh and man and others
[L2180] [01:40:41.84] uh suggested you know letting algorithms
[L2181] [01:40:46.64] use these quantum mechanical operations
[L2182] [01:40:50.08] mainly in originally for just simulating
[L2183] [01:40:52.88] quantum systems rather than building
[L2184] [01:40:55.68] bigger apparatus to yeah like we
[L2185] [01:40:58.40] simulate other things turbulence I don't
[L2186] [01:41:00.48] know what's the power of quantum
[L2187] [01:41:02.64] algorithms again let's say running in
[L2188] [01:41:05.52] polinomial time or efficient quantum
[L2189] [01:41:07.36] algorithm can they do more than
[L2190] [01:41:09.92] efficient classical ones deterministic
[L2191] [01:41:12.64] or probabilistic and it wasn't clear for
[L2192] [01:41:15.68] a while and there were
[L2193] [01:41:18.08] a few examples that were very stylized
[L2194] [01:41:20.40] but were not for concrete natural
[L2195] [01:41:22.88] problems we care about and then in 94
[L2196] [01:41:26.00] Peter saw sort of Yeah, created an
[L2197] [01:41:30.56] earthquake or an avalanche. Uh he uh
[L2198] [01:41:35.44] found quantum algorithms that are
[L2199] [01:41:37.44] efficient, the factual integers and also
[L2200] [01:41:41.44] complete discrete logarithms. The two
[L2201] [01:41:43.44] most basic uh underpinnings of all
[L2202] [01:41:46.56] security systems that exist and this set
[L2203] [01:41:49.60] the world on fire, right? So uh lots of
[L2204] [01:41:53.28] people try to do a lot of things. uh of
[L2205] [01:41:56.40] course you know people want to you have
[L2206] [01:41:59.92] them these algorithms they implement
[L2207] [01:42:02.08] maybe they want to break or other people
[L2208] [01:42:04.96] skip the system. So as you know since
[L2209] [01:42:07.52] then billions were invested by companies
[L2210] [01:42:10.64] by governments by uh lots of people
[L2211] [01:42:14.80] trying to to build the technological
[L2212] [01:42:17.92] infrastructure and this is extremely
[L2213] [01:42:20.40] complicated. holding beats in superp
[L2214] [01:42:23.12] position is extremely complicated.
[L2215] [01:42:25.92] There's things that are called the
[L2216] [01:42:28.24] there's the noise. I mean when people
[L2217] [01:42:31.28] build classical computers like for noman
[L2218] [01:42:33.76] here in the
[L2219] [01:42:35.68] uh building next door u u you know noise
[L2220] [01:42:40.88] was one of the serious problems because
[L2221] [01:42:42.64] the bits were really in vacuum tubes and
[L2222] [01:42:45.76] uh they had to contend and in fact he
[L2223] [01:42:48.56] built a nice theory of uh classical
[L2224] [01:42:51.84] computers that have errors noise they
[L2225] [01:42:54.48] have to cope with errors some of their
[L2226] [01:42:56.16] components can be faulty but this today
[L2227] [01:42:59.84] is hardware you know has no errors to
[L2228] [01:43:02.56] speak of. We don't I mean there are
[L2229] [01:43:04.40] error correcting mechanisms but uh we
[L2230] [01:43:07.44] don't need them for classical computing.
[L2231] [01:43:10.24] Intel chips don't have you know I think
[L2232] [01:43:12.88] error correction in them. Hardware is
[L2233] [01:43:15.12] very reliable. When you move to quantum
[L2234] [01:43:18.32] there is this the coherence noise
[L2235] [01:43:21.76] in quantum mechanics everything depends
[L2236] [01:43:23.92] on everything. the world can influence
[L2237] [01:43:27.12] uh the computation in your laptop and uh
[L2238] [01:43:31.68] and protecting from this is very hard.
[L2239] [01:43:34.00] There are quantum correcting codes and
[L2240] [01:43:36.08] that's part of the solutions. That's
[L2241] [01:43:38.40] only one of the problems. Just holding
[L2242] [01:43:40.32] bits in superp position is hard and
[L2243] [01:43:42.72] there are many hard technological issues
[L2244] [01:43:45.44] and there's progress on that. So this is
[L2245] [01:43:47.68] one line of huge investment.
[L2246] [01:43:50.88] Uh the other line comes from
[L2247] [01:43:52.40] cryptography because of course everybody
[L2248] [01:43:55.04] should be worried right. I mean you know
[L2249] [01:43:57.76] forget quantum computers if tomorrow uh
[L2250] [01:44:00.96] I mean really tomorrow uh somebody finds
[L2251] [01:44:04.48] even a classical factory algorithms in
[L2252] [01:44:07.36] algorithm in polinomial time I think
[L2253] [01:44:09.20] there'll be chaos in the world because
[L2254] [01:44:11.76] nobody nobody can do any transactions
[L2255] [01:44:14.80] because most security systems still rely
[L2256] [01:44:17.04] on
[L2257] [01:44:19.52] um
[L2258] [01:44:21.04] and so of course uh we want to change
[L2259] [01:44:25.12] these
[L2260] [01:44:26.08] We want to change the underlying
[L2261] [01:44:27.76] assumptions of security. We want to rely
[L2262] [01:44:31.68] the whole revolution in cryptography was
[L2263] [01:44:33.84] that we rest cryptography on
[L2264] [01:44:35.84] computationally hard assumptions and
[L2265] [01:44:38.56] with this we build all the wonderful
[L2266] [01:44:40.48] public key systems and you know all the
[L2267] [01:44:45.04] magical things you can do with
[L2268] [01:44:48.00] under uh by assuming that players are
[L2269] [01:44:52.24] computationally limited.
[L2270] [01:44:54.56] uh but now if they are the the
[L2271] [01:44:57.04] adversaries are quantum computers
[L2272] [01:44:59.44] certainly they can break this assumption
[L2273] [01:45:02.00] you want to find other mathematical
[L2274] [01:45:04.24] problems computational problems
[L2275] [01:45:07.84] uh which are somehow hard even to
[L2276] [01:45:11.68] quantum computers.
[L2277] [01:45:13.84] So that's a the whole field this change
[L2278] [01:45:16.48] complexity theory and cryptography there
[L2279] [01:45:19.52] is an army of people who are just uh
[L2280] [01:45:23.12] trying to invent problems. I maybe
[L2281] [01:45:26.08] should stress one way functions are easy
[L2282] [01:45:28.08] to find. I mean most problems you most
[L2283] [01:45:31.44] processes in nature are not easily
[L2284] [01:45:33.84] reversible. You make an omelette from an
[L2285] [01:45:36.72] egg, you know, reversing this is
[L2286] [01:45:40.16] doesn't take the same amount of time.
[L2287] [01:45:44.24] That's the usual example of a physical
[L2288] [01:45:46.40] one function. But trap door functions
[L2289] [01:45:49.28] like factoring
[L2290] [01:45:51.20] problems for which from which you can
[L2291] [01:45:53.12] build public key systems and that's the
[L2292] [01:45:56.00] most really basic thing for electronic
[L2293] [01:45:58.72] commerce
[L2294] [01:46:00.32] uh are few. We don't know many. So we
[L2295] [01:46:03.04] know this I mentioned factoring discrete
[L2296] [01:46:05.44] log in the 90s
[L2297] [01:46:08.48] it and created this another type of step
[L2298] [01:46:13.12] function from uh problems on latises in
[L2299] [01:46:16.48] high dimensions I will not describe it
[L2300] [01:46:18.48] but it's another problem and then people
[L2301] [01:46:20.80] refined and got a few more similar of
[L2302] [01:46:23.68] similar nature and it turned out when
[L2303] [01:46:26.40] Peter Sh discovered this people
[L2304] [01:46:28.48] immediately tried to solve other
[L2305] [01:46:30.24] problems with quantum computers in Fact
[L2306] [01:46:33.04] even today we cannot solve too many
[L2307] [01:46:34.96] other problems with quantum computers.
[L2308] [01:46:37.52] These are special. The special thing
[L2309] [01:46:40.40] about them is that somehow you can
[L2310] [01:46:42.16] reduce them to finding periods in a
[L2311] [01:46:45.52] signal and periods is like fel
[L2312] [01:46:47.52] transform. A f transform turns out to in
[L2313] [01:46:50.88] exponential space but f transform you
[L2314] [01:46:53.92] can do somehow with quantum computers
[L2315] [01:46:57.12] with interference. the latis problems
[L2316] [01:46:59.84] and problems related to it some called
[L2317] [01:47:03.52] learning with arrows and similar uh you
[L2318] [01:47:07.28] know to this day nobody found an
[L2319] [01:47:10.96] efficient quantum algorithm for them so
[L2320] [01:47:13.52] there's no even theory forget building
[L2321] [01:47:15.52] quantum computers we don't know how to
[L2322] [01:47:18.24] solve them and so uh what the world is
[L2323] [01:47:21.52] not just complexity theory is the whole
[L2324] [01:47:23.20] physical world of you know uh security
[L2325] [01:47:26.88] systems
[L2326] [01:47:28.32] And also governments like the NSA,
[L2327] [01:47:31.84] you know, is you know supporting or you
[L2328] [01:47:35.28] know asking the world to produce
[L2329] [01:47:38.88] assumptions that may be resilient to
[L2330] [01:47:42.32] quantum attacks. And so this is a huge
[L2331] [01:47:46.08] change. There's a major change in the
[L2332] [01:47:48.48] interaction between computer scientists
[L2333] [01:47:50.88] and physicists which grew tremendously
[L2334] [01:47:54.08] since this discovery
[L2335] [01:47:56.40] and it's reached in in many many ways
[L2336] [01:47:58.80] that are not the the influence of the
[L2337] [01:48:02.72] algorithmic thinking of uh on on
[L2338] [01:48:06.16] physical theories including today
[L2339] [01:48:08.88] theories in quantum gravity, black holes
[L2340] [01:48:11.04] and so is immense and yeah we have new
[L2341] [01:48:14.32] sources of problems and new models and
[L2342] [01:48:16.56] complexity classes etc etc and uh
[L2343] [01:48:20.96] there's a a fantastic fantastic
[L2344] [01:48:23.60] interaction
[L2345] [01:48:25.36] um
[L2346] [01:48:26.96] and uh it's also in complexity theory
[L2347] [01:48:30.80] uh in that it turns out that you can
[L2348] [01:48:34.72] discover quantum algorithms and maybe
[L2349] [01:48:37.04] then dequantize them in special cases
[L2350] [01:48:40.32] like I mentioned factoring before the
[L2351] [01:48:43.28] randomizing
[L2352] [01:48:44.80] and so sometimes It's a way, it's a road
[L2353] [01:48:47.60] to discover new algorithms.
[L2354] [01:48:50.48] It reveals connections between problems.
[L2355] [01:48:52.88] It's it's extremely rich. But one of the
[L2356] [01:48:55.84] maybe most amazing consequences is that
[L2357] [01:48:59.76] people I mean we being what we are, we
[L2358] [01:49:02.88] make up models and uh study them. And uh
[L2359] [01:49:07.44] the interactive proofs I mentioned
[L2360] [01:49:09.20] before uh turns out that uh even before
[L2361] [01:49:12.80] quantum they were generalized to
[L2362] [01:49:15.20] interactive proofs with not with one
[L2363] [01:49:17.20] prover but with many provers which seem
[L2364] [01:49:19.68] to be you know weird but turns out to be
[L2365] [01:49:22.88] very important in itself because it led
[L2366] [01:49:25.52] to this PCP theorem. Then people said
[L2367] [01:49:29.12] okay let's allow quantum verifiers
[L2368] [01:49:31.36] quantum provers and see what they can.
[L2369] [01:49:34.88] So one amazing result which is about
[L2370] [01:49:37.04] five years ago is the acronyms. Of
[L2371] [01:49:40.72] course we have acquames for all these
[L2372] [01:49:42.40] complexity classes. It's MIP star equal.
[L2373] [01:49:46.48] You may have seen it maybe you didn't.
[L2374] [01:49:49.20] And it looks weird but I'll tell you
[L2375] [01:49:50.96] what what it says really. It says that
[L2376] [01:49:54.16] there is a weird really weird uh proof
[L2377] [01:49:58.16] system with quantum provers
[L2378] [01:50:01.04] that uh you know trying to convince
[L2379] [01:50:03.92] verifiers an efficient verifier and it
[L2380] [01:50:07.12] turns out you know you ask for which
[L2381] [01:50:08.72] problems can they do it? Forget their
[L2382] [01:50:10.24] own knowledge just convince. And it
[L2383] [01:50:12.72] turns out they can do it for the holding
[L2384] [01:50:15.52] problem for for problems that are not
[L2385] [01:50:18.32] computable. Things that are not
[L2386] [01:50:20.56] computable are verifiable
[L2387] [01:50:24.48] by efficient verifiers if the provers
[L2388] [01:50:27.84] are quantum and they are entangled and
[L2389] [01:50:30.00] whatever. But it's a weird proof system.
[L2390] [01:50:33.12] Very weird. But it does something that
[L2391] [01:50:35.92] looks totally, you know, ridiculous.
[L2392] [01:50:38.72] things that are uncomputable by any any
[L2393] [01:50:41.68] classical are verifiable in this
[L2394] [01:50:45.12] interactive probabistic sense by uh
[L2395] [01:50:49.04] efficient verifier.
[L2396] [01:50:51.84] So what I like to say in talking about
[L2397] [01:50:55.52] this is that it seems that the best
[L2398] [01:50:58.08] reaction, best hypothetical reaction of
[L2399] [01:51:00.96] anybody who hears this. Okay, you
[L2400] [01:51:03.60] complexity theorist, you you plain your
[L2401] [01:51:06.48] sandbox and you build all these sand
[L2402] [01:51:08.80] casters and make up all these models
[L2403] [01:51:10.96] that have nothing to do with anything
[L2404] [01:51:13.28] just because you can and you get once
[L2405] [01:51:15.68] you weird enough, you get weird enough,
[L2406] [01:51:18.48] you know, consequences. So one message
[L2407] [01:51:21.28] which I think is very powerful is that
[L2408] [01:51:24.48] this result has absolutely fundamental
[L2409] [01:51:28.40] impact on math and physics. It turns out
[L2410] [01:51:32.00] that it implies and this was already
[L2411] [01:51:35.12] done in the initial paper.
[L2412] [01:51:39.12] It implies resolution of well-known
[L2413] [01:51:43.20] conjectures in math and physics.
[L2414] [01:51:46.00] It turns out that the you know weird as
[L2415] [01:51:48.72] it is it's a new mathematical technique
[L2416] [01:51:52.40] to solve problems that nobody had any
[L2417] [01:51:55.04] idea famous problems important problems
[L2418] [01:51:57.36] that fields were dedicated to are
[L2419] [01:52:00.80] resolved by this result by the
[L2420] [01:52:02.80] techniques of this result. So you ask
[L2421] [01:52:05.60] the impact of you see the impact is
[L2422] [01:52:09.20] many generations over with for different
[L2423] [01:52:12.24] motivations and uh developments but all
[L2424] [01:52:16.40] of them following the methodology of
[L2425] [01:52:19.44] complexity theory of understanding the
[L2426] [01:52:21.52] power of you know composational models,
[L2427] [01:52:24.24] proof systems and so on has magically
[L2428] [01:52:27.44] led to such a consequence
[L2429] [01:52:30.80] and this is just we are in the beginning
[L2430] [01:52:33.44] of this right this type of proof
[L2431] [01:52:35.20] technique is now being explored and used
[L2432] [01:52:37.84] and there are more results you know
[L2433] [01:52:41.04] using this type of techniques to
[L2434] [01:52:42.88] longstanding problems pretty amazing
[L2435] [01:52:45.68] >> that's incredible yeah I mean in
[L2436] [01:52:47.60] complexity theory you know there's these
[L2437] [01:52:49.60] um what do you call them I guess like
[L2438] [01:52:52.08] ven diagrams of all possible problems
[L2439] [01:52:55.68] and you know the implicit assumption in
[L2440] [01:52:58.64] this picture is that these are these are
[L2441] [01:53:01.44] >> decidable problems
[L2442] [01:53:04.00] In some of these diagrams there's a
[L2443] [01:53:06.16] little in the corner there's a
[L2444] [01:53:07.68] >> unidable
[L2445] [01:53:08.40] >> undecidable ones and
[L2446] [01:53:09.76] >> unreachable. Yeah.
[L2447] [01:53:10.88] >> Right. And it's just uh I I can't I
[L2448] [01:53:15.36] don't even understand how you could
[L2449] [01:53:17.44] verify an undecidable.
[L2450] [01:53:19.52] >> It's a 200page paper. It builds on 10
[L2451] [01:53:22.32] years of understanding which is both a
[L2452] [01:53:25.92] lot of development in the quantum
[L2453] [01:53:29.20] algorithms and quantum proof systems
[L2454] [01:53:32.24] sphere but also relying on techniques
[L2455] [01:53:35.12] from classical proof systems which have
[L2456] [01:53:37.76] to do with coding theory and uh various
[L2457] [01:53:41.36] algebraic stuff that is used to prove
[L2458] [01:53:43.44] for example the PCP theorem that I
[L2459] [01:53:45.52] mentioned it's you know it's a huge body
[L2460] [01:53:48.80] of work and on top of this they all this
[L2461] [01:53:52.00] 200page paper in which they had to
[L2462] [01:53:54.16] develop many more tools and uh yeah
[L2463] [01:53:57.52] there you have it.
[L2464] [01:53:58.64] >> Wow. I mean when someone produces 200
[L2465] [01:54:02.16] pages of such complicated work that
[L2466] [01:54:05.68] makes such a outrageous claim how how
[L2467] [01:54:10.00] does that get verified by people? It's a
[L2468] [01:54:12.88] very good question. This tool for any uh
[L2469] [01:54:15.84] mathematical result that is complicated
[L2470] [01:54:19.20] and of course you you know that uh um of
[L2471] [01:54:23.92] course proofs of PES NP and the Roman
[L2472] [01:54:26.40] hypothesis are are generated very
[L2473] [01:54:29.76] frequently but some of them were
[L2474] [01:54:31.92] generated by very serious people and
[L2475] [01:54:35.28] took a long time to refute in these two
[L2476] [01:54:39.20] cases.
[L2477] [01:54:40.64] Um
[L2478] [01:54:42.32] and uh but others like you know the
[L2479] [01:54:45.76] permanent proof of the poner conjecture
[L2480] [01:54:48.16] one of the clay millennium problem
[L2481] [01:54:50.40] million dollar problems was another one
[L2482] [01:54:52.72] like that and this took several years to
[L2483] [01:54:54.80] verify and fix small bugs in and you
[L2484] [01:54:57.60] know books expositing this proof were
[L2485] [01:55:00.16] written and eventually this particular
[L2486] [01:55:03.20] paper is uh is for some reason still in
[L2487] [01:55:06.96] the referring stages in the analys of
[L2488] [01:55:09.20] mathematics.
[L2489] [01:55:10.72] now probably almost six years it will be
[L2490] [01:55:14.00] done. You know it's it's robust in the
[L2491] [01:55:15.92] sense that already new papers were
[L2492] [01:55:17.76] written with this type of tools in fact
[L2493] [01:55:20.16] giving somewhat alternative proofs of
[L2494] [01:55:23.20] the same same statements and stronger
[L2495] [01:55:25.28] statements in order to resolve other
[L2496] [01:55:27.68] mathematical conjectures but yeah it's a
[L2497] [01:55:31.44] it's a serious thing and in fact the
[L2498] [01:55:33.28] original paper had a bug like the
[L2499] [01:55:36.72] original paper with FMA
[L2500] [01:55:39.28] by wires FMA theorem also had a bug and
[L2501] [01:55:42.32] it was fixed and this was fixed. This
[L2502] [01:55:44.80] was very early on just when it came out
[L2503] [01:55:47.68] very quickly uh fixed. So it's any any
[L2504] [01:55:52.00] mathematical claim uh you know your your
[L2505] [01:55:55.12] question is you know very important for
[L2506] [01:55:58.56] in general mathematics is a and
[L2507] [01:56:01.44] mathematical truth is a social construct
[L2508] [01:56:04.48] that's what mathematicians believe.
[L2509] [01:56:07.36] Maybe we are moving into a world in
[L2510] [01:56:09.12] which we have lean proofs of uh you know
[L2511] [01:56:11.60] we have formal way of writing proofs and
[L2512] [01:56:14.72] there you can maybe formally verify them
[L2513] [01:56:18.32] but uh anyway uh I think that this
[L2514] [01:56:21.52] community is uh is quite certain about
[L2515] [01:56:24.96] yeah
[L2516] [01:56:25.84] >> in complexity theory it's very
[L2517] [01:56:28.40] mathematical in nature when I read the
[L2518] [01:56:30.08] papers but obviously it has implications
[L2519] [01:56:33.20] in computer science what's the
[L2520] [01:56:35.68] relationship between math and computer
[L2521] [01:56:38.00] science to you?
[L2522] [01:56:39.52] >> Well, I think uh the theory of computer
[L2523] [01:56:42.64] science, my field, complexity theory,
[L2524] [01:56:44.96] algorithms, this theoretical side
[L2525] [01:56:48.32] uh is
[L2526] [01:56:50.88] really lucky to have these two parents.
[L2527] [01:56:54.24] It lives in both spaces. It uh it is a
[L2528] [01:56:58.96] mathematical field in the sense that
[L2529] [01:57:00.72] most of what we generate are theoreans
[L2530] [01:57:03.04] and proofs in the mathematic sense.
[L2531] [01:57:06.24] uh on the other hand it's related to
[L2532] [01:57:08.40] computation because the kind of
[L2533] [01:57:09.84] questions we ask ourselves the problems
[L2534] [01:57:11.60] we are trying to solve are motivated
[L2535] [01:57:15.20] partly motivated by and trying to
[L2536] [01:57:17.52] understand computation. So you can think
[L2537] [01:57:19.68] of theoretical computer science very
[L2538] [01:57:22.24] much like you can think about analysis
[L2539] [01:57:24.32] and algebra and topology.
[L2540] [01:57:27.04] There are notions you know in in algebra
[L2541] [01:57:29.68] you're trying to understand equations or
[L2542] [01:57:31.84] systems of equations
[L2543] [01:57:34.08] and uh in in analysis you are trying to
[L2544] [01:57:36.80] understand very generally speaking
[L2545] [01:57:39.20] inequalities
[L2546] [01:57:41.52] um and continuous spaces right so there
[L2547] [01:57:45.68] are there are these notions you are
[L2548] [01:57:47.28] trying to understand computation is one
[L2549] [01:57:50.48] of these notions you are trying to
[L2550] [01:57:52.24] understand what can you produce by an
[L2551] [01:57:54.72] evolution of simple local steps
[L2552] [01:57:58.00] uh to a given environment the input you
[L2553] [01:58:00.96] know and this can be uh you know
[L2554] [01:58:03.68] sequence of bits or it can be the you
[L2555] [01:58:06.80] know the DNA of a you know of a person
[L2556] [01:58:10.00] which is being you know you know from
[L2557] [01:58:13.36] which you produce proteins using
[L2558] [01:58:15.12] computation or you produce a new baby
[L2559] [01:58:18.08] using the evolution of you know
[L2560] [01:58:21.20] fertilized egg uh or the weather or you
[L2561] [01:58:24.48] know so computation is sort of
[L2562] [01:58:26.24] everywhere
[L2563] [01:58:27.92] and you we are trying to understand it
[L2564] [01:58:30.32] in in ways that are different as we care
[L2565] [01:58:33.84] about resources how much resources are
[L2566] [01:58:37.28] exerted in any uh such computation and
[L2567] [01:58:41.20] uh you know trying to model it try to
[L2568] [01:58:44.08] you know understand the algorithms that
[L2569] [01:58:46.32] they underlying natural phenomena. So we
[L2570] [01:58:48.96] live in both spaces. We have a lot of
[L2571] [01:58:51.92] input of problems and models from you
[L2572] [01:58:55.84] know industry technology
[L2573] [01:58:58.96] uh systems and so on and we have all the
[L2574] [01:59:02.24] mathematics that is uh you know so we
[L2575] [01:59:04.88] have the rigorous side coming from and
[L2576] [01:59:07.92] the aesthetic side I would say you know
[L2577] [01:59:10.56] like creating models of poof systems
[L2578] [01:59:14.96] because they are nice because they are
[L2579] [01:59:16.64] interesting because yeah not because
[L2580] [01:59:18.88] they are implementable necessarily. So
[L2581] [01:59:21.76] this uh living in these two spaces uh um
[L2582] [01:59:26.40] uh you know is extremely beneficial to
[L2583] [01:59:28.80] this uh theory of composition.
[L2584] [01:59:32.24] >> You mentioned earlier that some people
[L2585] [01:59:34.56] might have the perspective and of
[L2586] [01:59:36.88] complexity theory that it's kind of you
[L2587] [01:59:39.60] solving problems for problems sake. I
[L2588] [01:59:41.76] read in another interview you did that
[L2589] [01:59:44.24] you were never motivated by application
[L2590] [01:59:47.44] and then my natural thought was what
[L2591] [01:59:50.24] motivates you to solve all these really
[L2592] [01:59:52.24] tricky complicated problems.
[L2593] [01:59:54.32] >> Okay. So let me say one thing about your
[L2594] [01:59:57.04] the beginning of your question. It says
[L2595] [01:59:58.88] about solving problems. I think that
[L2596] [02:00:00.48] what we do more much more is modeling
[L2597] [02:00:04.24] things. I mean modeling things then give
[L2598] [02:00:06.64] rise to problems that you want to uh you
[L2599] [02:00:10.00] want to understand. So I think the
[L2600] [02:00:12.00] modeling part in the theory of
[L2601] [02:00:13.52] computation modeling various forms of
[L2602] [02:00:16.24] computation is a large part of uh
[L2603] [02:00:19.76] theoretical computer science manifests
[L2604] [02:00:21.76] itself in particular in cryptography
[L2605] [02:00:23.84] where there are models of you know
[L2606] [02:00:25.84] adversary in distributed computation.
[L2607] [02:00:28.32] There are many you know I think modeling
[L2608] [02:00:30.80] just asking questions is you know and
[L2609] [02:00:34.24] creating making definitions
[L2610] [02:00:37.92] uh is a very central part of the field
[L2611] [02:00:41.36] and it happens more than in mathematics
[L2612] [02:00:44.80] maybe because they are more ancient than
[L2613] [02:00:47.20] maybe definitions happened earlier but I
[L2614] [02:00:50.08] want to stress this that's a very
[L2615] [02:00:52.00] important thing for example we discussed
[L2616] [02:00:54.00] randomness and our definition of
[L2617] [02:00:56.16] randomness is totally different and it
[L2618] [02:00:58.88] gives rise to you know very you know
[L2619] [02:01:02.24] surprising and interesting practically
[L2620] [02:01:05.28] theorems. Okay. Uh now that we settled
[L2621] [02:01:08.48] that uh what what motivates me or what
[L2622] [02:01:11.60] motivates other people uh of course
[L2623] [02:01:14.40] everybody has their own motivation. I am
[L2624] [02:01:16.96] a product of computer science education.
[L2625] [02:01:20.32] I uh all my you know undergrad and grad
[L2626] [02:01:24.48] school and postto and everything were in
[L2627] [02:01:27.44] computer science. So I think that I uh I
[L2628] [02:01:32.08] suddenly uh am sorry that I didn't take
[L2629] [02:01:35.60] many more math courses because then I
[L2630] [02:01:37.60] wouldn't have to learn things later in
[L2631] [02:01:39.76] life. But uh that aside, I think that
[L2632] [02:01:42.56] the focus on computation which is what
[L2633] [02:01:46.00] computer science education gives you
[L2634] [02:01:48.56] different you know different systems and
[L2635] [02:01:50.88] different uh uh issues are of course
[L2636] [02:01:54.08] algorithms in databases and algorithms
[L2637] [02:01:56.40] in uh you know programming languages and
[L2638] [02:01:59.12] in fact famous algorithms uh in other
[L2639] [02:02:01.92] other fields there are models and
[L2640] [02:02:04.16] algorithms in so computation is
[L2641] [02:02:06.80] something that I'm interested
[L2642] [02:02:08.80] intrinsically I'm more over the years
[L2643] [02:02:11.60] realizing that computation you know the
[L2644] [02:02:14.80] field expanded to interact with all the
[L2645] [02:02:16.96] sciences and that computation happened
[L2646] [02:02:19.76] everywhere in various forms in physics
[L2647] [02:02:22.48] and biology and so on you know makes it
[L2648] [02:02:24.96] a fundamental object of study and for me
[L2649] [02:02:28.00] given the way I was brought up I guess
[L2650] [02:02:30.00] in particular is fascinating in itself
[L2651] [02:02:33.36] uh I know from just experience
[L2652] [02:02:37.84] that lot of the theorems We prove not
[L2653] [02:02:40.64] many but probably with much higher
[L2654] [02:02:42.88] proportion than in other areas of mass
[L2655] [02:02:45.52] are impactful in you know in the world
[L2656] [02:02:49.92] in the in real systems in security
[L2657] [02:02:52.24] systems in blockchains in the real
[L2658] [02:02:54.24] world. But that this side this
[L2659] [02:02:57.44] particular side of um seeing exactly how
[L2660] [02:03:01.84] you translate your algorithm into
[L2661] [02:03:04.88] into a system or your uh you know zero
[L2662] [02:03:08.24] knowledge proof. I I predicted when we
[L2663] [02:03:11.04] came up with a zero knowledge proof that
[L2664] [02:03:13.44] it will never be implemented because the
[L2665] [02:03:15.84] protocol that I described more or less
[L2666] [02:03:17.92] to you is very costly. I mean you want
[L2667] [02:03:21.12] to prove that I I'm producing a product
[L2668] [02:03:24.08] of two primes and I convert it to a map
[L2669] [02:03:26.40] and then I do all this complicated
[L2670] [02:03:28.40] procedure many times. So doesn't seem
[L2671] [02:03:30.80] that anybody would ever use such a thing
[L2672] [02:03:33.52] but I was wrong. I mean I I didn't
[L2673] [02:03:37.68] realize how motivated people can be and
[L2674] [02:03:40.00] how important applications of zero
[L2675] [02:03:42.00] knowledge can be in the real world not
[L2676] [02:03:43.68] in theory of protocol design uh and they
[L2677] [02:03:47.44] did simplify maybe other using more
[L2678] [02:03:50.40] assumptions
[L2679] [02:03:52.08] uh different assumptions there's a
[L2680] [02:03:54.88] recent breakthrough of a postto here
[L2681] [02:03:58.56] I elango you may have heard because it
[L2682] [02:04:00.48] got some publicity in front and so on
[L2683] [02:04:03.04] where he introduced into The assumptions
[L2684] [02:04:05.60] of cryptography not just hard
[L2685] [02:04:07.92] computational problems but also uh
[L2686] [02:04:10.88] things of the nature of G theorem that
[L2687] [02:04:14.40] something is unprovable in some you know
[L2688] [02:04:18.32] mathematical proof system like Frank
[L2689] [02:04:21.92] whatever mathematicians use some using
[L2690] [02:04:24.88] that they can get zero knowledge that's
[L2691] [02:04:26.80] non-interactive
[L2692] [02:04:28.56] you can get yeah it's an amazing thing
[L2693] [02:04:30.88] it's get you know things get richer What
[L2694] [02:04:34.64] I what I want to say is that um
[L2695] [02:04:39.04] again from experience I have 45 years of
[L2696] [02:04:41.76] experience of this working in this field
[L2697] [02:04:44.56] which have been fascinating. Uh
[L2698] [02:04:49.20] you know I I mentioned to you uh in the
[L2699] [02:04:52.56] email you know there's
[L2700] [02:04:55.04] extra benefits to this field. I think
[L2701] [02:04:57.60] the community is amazing. Not just that
[L2702] [02:04:59.76] it has so many brilliant minds and young
[L2703] [02:05:02.88] brilliant minds are entering the field
[L2704] [02:05:04.72] all the time [clears throat] but also uh
[L2705] [02:05:06.88] very lively and interactive and
[L2706] [02:05:08.80] collaborative and uh you know just uh uh
[L2707] [02:05:14.08] yeah many of my best friends are also
[L2708] [02:05:16.64] colleagues. So it's it's fantastic but
[L2709] [02:05:19.76] the understanding that the theoretical
[L2710] [02:05:23.12] understanding of many things that we uh
[L2711] [02:05:27.04] maybe ask ourselves for aesthetical
[L2712] [02:05:29.12] reasons that are mathematical that we
[L2713] [02:05:32.24] generalize something for generalization
[L2714] [02:05:34.80] sake which may not have a counterpart in
[L2715] [02:05:38.40] in industry. In fact, show us work on
[L2716] [02:05:41.52] quantum algorithms. You can say why why
[L2717] [02:05:44.88] do that? There are no quantum
[L2718] [02:05:48.32] computers. Maybe let's wait till
[L2719] [02:05:50.80] somebody built once and we understand
[L2720] [02:05:52.72] why you know. So no, the answer is no.
[L2721] [02:05:56.00] No, you should try to understand
[L2722] [02:05:58.56] whatever is natural for you to
[L2723] [02:06:00.24] understand. This field has already
[L2724] [02:06:04.00] uh you know maybe it was not clear 40
[L2725] [02:06:06.48] years ago but certainly clear now that
[L2726] [02:06:09.20] all you know that
[L2727] [02:06:11.84] lots of theoretical understanding is not
[L2728] [02:06:14.16] just productions of mathematical
[L2729] [02:06:18.16] results but because it is about
[L2730] [02:06:21.92] computation
[L2731] [02:06:23.44] it is meaningful
[L2732] [02:06:25.68] I don't know often enough or whatever in
[L2733] [02:06:29.68] in uh in the real world. There are many
[L2734] [02:06:32.32] many other examples besides crypto and
[L2735] [02:06:34.40] quantum encoding theory and you know the
[L2736] [02:06:37.20] field revolutionized coding theory
[L2737] [02:06:40.16] mainly because of the PCP theorem tools
[L2738] [02:06:42.56] needed for
[L2739] [02:06:45.12] so you know there are lots of examples
[L2740] [02:06:47.68] and this eventually went into systems
[L2741] [02:06:50.96] you know for memory schemes or whatever
[L2742] [02:06:54.64] look I'm interested in P versus NP this
[L2743] [02:06:58.00] is a question about impossibility
[L2744] [02:07:01.36] Right. This is a problem. We still
[L2745] [02:07:03.68] didn't get closer in this at least
[L2746] [02:07:05.36] certainly the the years I've been at it.
[L2747] [02:07:08.08] Uh we are not much closer to showing
[L2748] [02:07:11.12] hardness for anything. We don't know
[L2749] [02:07:13.04] that multiplication is harder than
[L2750] [02:07:14.96] addition. It's a basic question.
[L2751] [02:07:18.16] U so uh this this kind of question by
[L2752] [02:07:22.56] itself is certainly not practical. I
[L2753] [02:07:25.28] mean it's not clear. Well, it is a
[L2754] [02:07:27.60] little clear because if you find out
[L2755] [02:07:29.76] functions, maybe you can substantiate
[L2756] [02:07:32.24] cryptography on a theorem rather than on
[L2757] [02:07:34.72] assumption. But anyway, uh there there
[L2758] [02:07:38.32] are questions in the field that uh don't
[L2759] [02:07:41.36] directly relate and will not directly
[L2760] [02:07:43.52] relate to uh implementations of any
[L2761] [02:07:46.80] system.
[L2762] [02:07:48.32] But they are all part of trying to
[L2763] [02:07:50.80] understand what efficient computation
[L2764] [02:07:53.76] can do and what it cannot or when can
[L2765] [02:07:57.12] you minimize resources of some type and
[L2766] [02:07:59.84] when you cannot and how do different
[L2767] [02:08:01.52] problems relate to each other. Uh this
[L2768] [02:08:05.68] basic methodology of the field that
[L2769] [02:08:07.68] created some wonderful edifice and I
[L2770] [02:08:11.04] would say that we are still in the
[L2771] [02:08:13.04] embryo stage of understanding
[L2772] [02:08:15.44] computation. You mentioned a few times
[L2773] [02:08:17.84] in this conversation um you know some
[L2774] [02:08:20.48] people made a major discovery and then
[L2775] [02:08:22.48] it you know kind of broke some
[L2776] [02:08:24.64] assumption that was maybe 50 years ago
[L2777] [02:08:27.04] and um you know researchers make these
[L2778] [02:08:29.84] advances and I know in your career
[L2779] [02:08:31.76] you've made a few as well and the time
[L2780] [02:08:35.12] space between payouts is sometimes
[L2781] [02:08:37.52] decades you know where you make a major
[L2782] [02:08:39.92] >> sometime
[L2783] [02:08:40.56] >> because a lot of people's career is like
[L2784] [02:08:42.48] maybe you know if you're just an
[L2785] [02:08:44.08] engineer you just you got your ship
[L2786] [02:08:46.00] shipping projects every year.
[L2787] [02:08:48.88] >> Um, but in in your case, like let's say
[L2788] [02:08:50.96] you imagine you discovered P equals MP
[L2789] [02:08:55.20] or something like that.
[L2790] [02:08:56.56] >> Yeah. How like how do you feel when you
[L2791] [02:08:58.32] make those discoveries, those sparse
[L2792] [02:09:00.88] discoveries in your career?
[L2793] [02:09:02.80] >> Well, it's great. [laughter]
[L2794] [02:09:06.08] Yeah, it happens. The big ones happen
[L2795] [02:09:08.16] rarely. uh I think of science I mean
[L2796] [02:09:10.72] realistically science and math is a you
[L2797] [02:09:14.16] know a community of ants work I mean
[L2798] [02:09:16.96] most progress we have this conferences
[L2799] [02:09:20.40] theor conferences
[L2800] [02:09:22.32] uh stock and forks and then we have all
[L2801] [02:09:24.32] sort of uh you know satellite
[L2802] [02:09:26.72] conferences and there are hundreds of
[L2803] [02:09:28.40] papers in them satellite I mean focused
[L2804] [02:09:31.44] on concrete area learning theory crypto
[L2805] [02:09:34.16] I know online algorithms you there are
[L2806] [02:09:37.12] many many there are thousands
[L2807] [02:09:38.88] researchers are working in this I don't
[L2808] [02:09:41.20] know maybe and uh they are producing
[L2809] [02:09:45.60] many papers a year and most papers are
[L2810] [02:09:50.08] and most of my papers are you know we
[L2811] [02:09:53.20] make a little progress in understanding
[L2812] [02:09:55.04] something usually it's not a big problem
[L2813] [02:09:57.84] you know we discover a variant of a
[L2814] [02:09:59.76] technique or we can strengthen a bound
[L2815] [02:10:02.16] on some
[L2816] [02:10:04.00] and I find this essential I think this
[L2817] [02:10:06.08] is true in in science in general
[L2818] [02:10:08.80] And uh bigger understandings come more
[L2819] [02:10:12.48] early and they uh suddenly you know they
[L2820] [02:10:15.76] they send the shock wave to everybody
[L2821] [02:10:18.00] learns them and uh and uses them. But of
[L2822] [02:10:21.04] course you know uh those bigger
[L2823] [02:10:24.56] understanding it doesn't have to be a
[L2824] [02:10:26.00] resolution of 50 years old paper. it can
[L2825] [02:10:28.48] be something that you know when barring
[L2826] [02:10:31.36] discovered his algorithm for counting
[L2827] [02:10:33.52] that I mentioned
[L2828] [02:10:35.60] he was trying to actually prove that
[L2829] [02:10:37.36] it's impossible
[L2830] [02:10:39.52] and it was not like somebody asked this
[L2831] [02:10:41.84] question the answer was obvious it's
[L2832] [02:10:43.76] impossible right so when you have an
[L2833] [02:10:46.96] insight of this this type it's uh you
[L2834] [02:10:50.40] know amazing so whenever you you realize
[L2835] [02:10:52.72] something really new for you and and you
[L2836] [02:10:56.56] know for the communities is a phenomenal
[L2837] [02:10:59.76] result. It's rare. I tell all my
[L2838] [02:11:01.84] students and posttos that yeah it's not
[L2839] [02:11:05.20] uh you know you don't work for the
[L2840] [02:11:07.28] million dollar. A million dollar is
[L2841] [02:11:08.96] nothing of course for this some of these
[L2842] [02:11:11.44] problems. Uh but yeah you you work
[L2843] [02:11:14.48] because you enjoy the practice of it.
[L2844] [02:11:17.60] You enjoy thinking about these problems.
[L2845] [02:11:19.60] In fact, most days in the life of my
[L2846] [02:11:24.08] life, mathematician's life is unlike a
[L2847] [02:11:27.60] systems person. You go in the morning,
[L2848] [02:11:30.80] you come back in the evening and you
[L2849] [02:11:32.32] fail to do what you wanted to do. You
[L2850] [02:11:35.04] just couldn't you just thought more and
[L2851] [02:11:37.68] yeah and I think that uh it's really
[L2852] [02:11:40.96] important. It's not so it's not for
[L2853] [02:11:42.80] everybody
[L2854] [02:11:45.04] clearly. It's not satisfying if you you
[L2855] [02:11:47.28] know this happens every day and every
[L2856] [02:11:49.36] week and you know uh it's not for
[L2857] [02:11:52.24] everybody but uh you know you uh it's
[L2858] [02:11:55.84] for the people who for whom this
[L2859] [02:11:58.16] activity of trying to think of throwing
[L2860] [02:12:00.80] ideas or failing but learning from the
[L2861] [02:12:03.68] failures people don't realize that often
[L2862] [02:12:06.48] you learn I mean the fact that you
[L2863] [02:12:08.32] failed is is not just a wasted day there
[L2864] [02:12:12.64] is something that you gain from is maybe
[L2865] [02:12:15.68] subconsciously that will help you later.
[L2866] [02:12:18.00] So unless you enjoy this activity maybe
[L2867] [02:12:20.88] this field is not for you
[L2868] [02:12:23.52] and uh yeah and then you see something
[L2869] [02:12:26.48] and that's even if it's small sometimes
[L2870] [02:12:28.80] it's very satisfaction.
[L2871] [02:12:31.12] Last question for you and I think you
[L2872] [02:12:33.04] know people in the field might be
[L2873] [02:12:35.28] curious because you have so much
[L2874] [02:12:37.04] experience is you know if you could go
[L2875] [02:12:39.92] back to the beginning of your career
[L2876] [02:12:41.44] when you just started you know becoming
[L2877] [02:12:43.36] a researcher is there any advice that
[L2878] [02:12:45.44] you'd give yourself?
[L2879] [02:12:48.08] Uh I think I was lucky enough not to
[L2880] [02:12:53.76] think that I would change anything. I
[L2881] [02:12:55.76] think I was lucky enough and many people
[L2882] [02:12:57.68] are lucky in this field because the
[L2883] [02:12:59.20] field is uh so so accommodating to young
[L2884] [02:13:02.80] people. there's uh it's completely
[L2885] [02:13:05.84] leveled uh you know there's no
[L2886] [02:13:07.84] hierarchies people would go to
[L2887] [02:13:10.40] conferences and meet I remember my first
[L2888] [02:13:13.12] conference meeting Darp who was you know
[L2889] [02:13:19.04] uh go in in the field and invented you
[L2890] [02:13:21.92] know did all these complete things and I
[L2891] [02:13:24.85] [snorts] was a first year graduate
[L2892] [02:13:26.48] student and somebody introduced me to
[L2893] [02:13:28.72] him and he immediately asked me what I'm
[L2894] [02:13:30.56] doing and I said I prove that some some
[L2895] [02:13:33.76] problem was NP complete and he was
[L2896] [02:13:35.68] actually interested
[L2897] [02:13:38.48] me. I I was lucky to have phenomenal
[L2898] [02:13:41.12] mentors as an undergrad as a graduate
[L2899] [02:13:43.44] student. I was lucky to have
[L2900] [02:13:45.76] unbelievable collaborators over the
[L2901] [02:13:47.92] years and you know you learn from uh uh
[L2902] [02:13:51.92] all this. So uh
[L2903] [02:13:55.92] it's not a very informative advice to
[L2904] [02:13:58.88] people to tell them to be lucky. uh I
[L2905] [02:14:01.52] think this environment exists. I think
[L2906] [02:14:03.68] that one piece of advice I I give
[L2907] [02:14:06.48] everybody is that uh uh in the early
[L2908] [02:14:09.84] stages is uh to work on things they
[L2909] [02:14:14.40] enjoy the most. So when you are
[L2910] [02:14:16.32] discovering your talents as a researcher
[L2911] [02:14:19.44] one one direction maybe you know these
[L2912] [02:14:21.68] are problems if you solve them then you
[L2913] [02:14:24.08] you but maybe that's not your problems
[L2914] [02:14:26.40] maybe it's not your affinity to them.
[L2915] [02:14:28.96] You have to experiment with the type of
[L2916] [02:14:30.80] problems. It's good to have a variety of
[L2917] [02:14:33.68] areas and papers to read in these areas
[L2918] [02:14:35.92] or problems to understand. It's always
[L2919] [02:14:37.92] good to start with a few to sort of
[L2920] [02:14:40.16] better understand your your capabilities
[L2921] [02:14:42.88] and often uh what you like most is what
[L2922] [02:14:46.48] you are better at.
[L2923] [02:14:48.16] >> Thank you so much for your time. I
[L2924] [02:14:49.76] really appreciate it.
[L2925] [02:14:50.64] >> Yeah.
[L2926] [02:14:51.44] >> Hey, thank you for watching this
[L2927] [02:14:52.56] podcast. If you liked it and you want to
[L2928] [02:14:54.16] see the show grow, please support with a
[L2929] [02:14:56.48] comment or a like. Also, if you have any
[L2930] [02:14:59.44] recommendations for people you want me
[L2931] [02:15:01.12] to bring on, please drop a comment.
[L2932] [02:15:03.68] Guests like Barbara Liskoff, Mike
[L2933] [02:15:05.92] Stonereaker, Mark Brooker, these were
[L2934] [02:15:08.32] all people that I brought on because
[L2935] [02:15:10.32] someone left a comment. On another note,
[L2936] [02:15:12.56] aside from the podcast, I'm working on
[L2937] [02:15:14.48] building the ergonomic keyboard that I
[L2938] [02:15:16.40] wish existed. Here's a glance at the
[L2939] [02:15:18.56] prototype. It's a split keyboard, so
[L2940] [02:15:20.80] there's two sides. Um, this is in the
[L2941] [02:15:22.96] case, but yeah, we launched on
[L2942] [02:15:24.48] Kickstarter and we hit our goal within 8
[L2943] [02:15:26.72] hours of launching. I really appreciate
[L2944] [02:15:28.40] it if you were one of the people who
[L2945] [02:15:29.76] grabbed one of the early units. Um,
[L2946] [02:15:32.08] we're now working on the long journey of
[L2947] [02:15:33.92] building the tooling now and so if you
[L2948] [02:15:35.76] still want to pick one up, I've left the
[L2949] [02:15:37.84] late pledges open on Kickstarter, so you
[L2950] [02:15:40.40] can grab one there. I'll put a link in
[L2951] [02:15:42.08] the description. Thank you again for
[L2952] [02:15:44.40] watching the podcast and I'll see you in
[L2953] [02:15:46.64] the next
