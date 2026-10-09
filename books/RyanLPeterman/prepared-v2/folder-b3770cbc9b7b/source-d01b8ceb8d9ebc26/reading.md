# MIT Professor: Leetcode, P vs NP, SAT Solvers | Ryan Williams

Source ID: source-d01b8ceb8d9ebc26
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/MIT_Professor_Leetcode,_P_vs_NP,_SAT_Solvers_Ryan_Williams_en.txt
Video: https://www.youtube.com/watch?v=AaK1SL2i_4Y

[L10] [00:00.00] Hypotheses which are at the edge of our
[L11] [00:01.88] understanding can be enlightening.
[L12] [00:04.88] >> This is Ryan Williams. He's a professor
[L13] [00:07.08] at MIT who won the Gödel Prize for
[L14] [00:09.16] theoretical computer science, and I
[L15] [00:11.08] started by asking him a LeetCode
[L16] [00:13.00] question. So, the question is three-sum.
[L17] [00:16.00] Can you do better than n squared for
[L18] [00:17.92] this?
[L19] [00:18.36] >> Yeah, you actually can do better than n
[L20] [00:20.28] squared, and this is um not at all
[L21] [00:22.44] obvious.
[L22] [00:23.56] >> He also had contrarian takes on popular
[L23] [00:25.96] hypotheses.
[L24] [00:26.92] >> I think I'm on the record as not
[L25] [00:28.76] believing this hypothesis. We really
[L26] [00:31.64] don't understand polynomial time
[L27] [00:34.16] computation as deeply as we think we do.
[L28] [00:42.08] >> All right, I want to start by asking you
[L29] [00:44.00] the most popular LeetCode question. So,
[L30] [00:46.92] the question is three-sum.
[L31] [00:49.80] Given a list of numbers, and we want to
[L32] [00:53.56] find three numbers such that they sum to
[L33] [00:57.20] zero.
[L34] [00:57.76] >> Yes.
[L35] [00:58.64] >> And so, what are your thoughts on the
[L36] [01:01.88] brute-force solution for this? We can
[L37] [01:03.36] start there.
[L38] [01:04.64] >> So, the obvious brute-force solution
[L39] [01:08.08] takes if you you've got n numbers n
[L40] [01:10.72] cubed time. Just try all the triples of
[L41] [01:13.24] numbers, sum them up, see if they sum to
[L42] [01:15.80] zero. There is a faster uh solution. So,
[L43] [01:19.44] one way to get
[L44] [01:21.00] an order n squared time algorithm for
[L45] [01:23.64] three-sum is to first start by sorting
[L46] [01:27.40] the numbers.
[L47] [01:28.48] And then, you go through the numbers one
[L48] [01:31.68] by one. Say like, you're looking at a
[L49] [01:34.24] number A.
[L50] [01:35.80] And you want to know,
[L51] [01:37.44] is there a B and a C in the rest of the
[L52] [01:39.52] list um
[L53] [01:41.80] whose sum with A is going to be zero?
[L54] [01:45.24] Okay, so,
[L55] [01:46.84] the way
[L56] [01:48.20] this works is
[L57] [01:50.40] after you sort the numbers, you you do
[L58] [01:53.08] what's called a finger search. So, you
[L59] [01:55.28] put um
[L60] [01:57.12] the finger from your left hand on the
[L61] [01:59.76] minimum element and finger from your
[L62] [02:02.40] right hand on the maximum element. So
[L63] [02:04.32] you start there. And you check like,
[L64] [02:06.32] okay, are these my B and C?
[L65] [02:08.76] Right? So you you add them min and max
[L66] [02:11.36] and check if adding that with A gets you
[L67] [02:14.92] zero. Okay?
[L68] [02:17.24] And um if you're lucky, okay, then
[L69] [02:19.84] you're done, but typically you're not
[L70] [02:21.64] lucky. And so this sum of the min and
[L71] [02:25.24] the max is either
[L72] [02:27.40] um larger than your target value minus A
[L73] [02:31.32] or it's smaller.
[L74] [02:33.00] Okay? If it's larger, then you need to
[L75] [02:36.84] decrease the larger number. So you take
[L76] [02:39.28] your right finger, which is sitting on
[L77] [02:40.72] the maximum element, and you move it to
[L78] [02:42.44] the left one slot. Okay? So you decrease
[L79] [02:45.56] the larger one.
[L80] [02:47.08] All right? If the sum is smaller than
[L81] [02:50.84] your target, you need to take the
[L82] [02:52.08] smaller number and make it a little bit
[L83] [02:53.40] bigger. So you move the you move your
[L84] [02:56.36] left finger sitting on the minimum over
[L85] [02:58.76] one slot. Okay? And you you keep doing
[L86] [03:01.28] this. You keep checking
[L87] [03:03.08] whether, you know, your left finger and
[L88] [03:04.60] right finger are pointing at a solution.
[L89] [03:06.84] And if they aren't, then you adjust it.
[L90] [03:09.08] If they do, they ever do sum up to
[L91] [03:11.88] exactly what you want, you're done.
[L92] [03:14.76] And so after each comparison like this,
[L93] [03:18.28] right? One of your fingers moved. Okay?
[L94] [03:21.52] If the fingers ever cross, then you
[L95] [03:23.72] don't have a solution. Like there's just
[L96] [03:25.36] there just can't be a solution.
[L97] [03:27.24] And so the number of times you move, you
[L98] [03:29.20] know, your fingers in total is like N.
[L99] [03:32.36] So so you have a order N solution for
[L100] [03:35.20] finding that extra pair.
[L101] [03:37.52] And you do this for each of the numbers
[L102] [03:40.08] A.
[L103] [03:41.28] Okay? So then you get a order N squared
[L104] [03:43.68] uh solution overall. You do it N times.
[L105] [03:46.64] Each finger search
[L106] [03:48.36] uh takes order N time.
[L107] [03:50.32] >> And that is the popular solution. think.
[L108] [03:53.80] >> solution, yes.
[L109] [03:54.56] >> of people know when we're in these
[L110] [03:57.04] algorithmic LeetCode interviews.
[L111] [04:00.40] And I know a lot of your research is
[L112] [04:02.96] kind of about pushing lower bounds, so
[L113] [04:04.96] maybe we can
[L114] [04:06.32] start that conversation off by can you
[L115] [04:08.40] do better than n squared for this?
[L116] [04:10.48] >> Yeah, you actually can do better than n
[L117] [04:12.40] squared. And this is um
[L118] [04:14.88] uh not at all obvious.
[L119] [04:17.00] In in fact, it it stems from
[L120] [04:19.68] um taking this finger search idea and
[L121] [04:22.52] pushing it in a different direction.
[L122] [04:24.68] So, what you do is you take your sorted
[L123] [04:28.00] list, okay, and you
[L124] [04:30.64] break
[L125] [04:31.80] uh the sorted list up into little groups
[L126] [04:34.36] of contiguous elements. So, let's say
[L127] [04:36.72] your little group is like log n size or
[L128] [04:39.20] square root log n. It's like a really
[L129] [04:41.04] small little group, okay?
[L130] [04:43.00] So, you've got either n over log n
[L131] [04:45.60] groups total or n over square root log n
[L132] [04:47.68] groups total depending on how you
[L133] [04:49.76] break up your groups.
[L134] [04:51.44] And then the idea is you're going to
[L135] [04:54.16] perform the same kind of finger search,
[L136] [04:56.56] but you're going to set things up so
[L137] [04:59.00] that you're comparing two pairs of
[L138] [05:01.40] groups. Your finger's always pointing at
[L139] [05:03.48] an entire group.
[L140] [05:05.28] So, like the left hand and right hand
[L141] [05:07.16] are pointing at two groups and you want
[L142] [05:08.64] to know if there's a three sum solution
[L143] [05:09.92] in that group.
[L144] [05:11.84] And
[L145] [05:13.24] you can set up a kind of fast data
[L146] [05:15.96] structure to check a small group, okay?
[L147] [05:19.76] And this data structure will take much
[L148] [05:22.16] less than
[L149] [05:23.76] um the number of elements in the two
[L150] [05:26.20] groups squared. So, you set up some
[L151] [05:29.00] kind of fancy data structure. And
[L152] [05:31.00] because you set your group size so
[L153] [05:32.52] small, it's like a pre-processing that
[L154] [05:34.60] you do over all the possible
[L155] [05:37.40] inputs you could send from a pair of
[L156] [05:39.36] groups.
[L157] [05:40.64] And so, you have some data structure and
[L158] [05:42.92] it will, you know, let's say it takes
[L159] [05:44.48] you n to the 1.5 time to prepare this
[L160] [05:47.48] data structure, this fancy data
[L161] [05:49.04] structure. But now, when you're looking
[L162] [05:51.28] at
[L163] [05:52.36] a pair of groups,
[L164] [05:54.04] you can look at the answer much faster
[L165] [05:56.84] than what finger search would have
[L166] [05:58.16] taken. I guess finger search through
[L167] [05:59.92] like a group of length G and another
[L168] [06:01.20] group of length G would take about order
[L169] [06:03.72] G time, and you can do actually do
[L170] [06:05.20] faster by by this kind of look up. This
[L171] [06:07.56] kind of table look up. I think it is
[L172] [06:09.48] kind of like you you take
[L173] [06:12.40] uh
[L174] [06:12.96] this list of length N
[L175] [06:15.32] and you
[L176] [06:16.96] uh kind of shrink it into like N over
[L177] [06:20.16] num uh N over N over group size uh
[L178] [06:23.92] number of things. And these are more
[L179] [06:25.52] complicated objects.
[L180] [06:27.32] And then you do And now like you you're
[L181] [06:29.12] trying to you're trying to speed up like
[L182] [06:30.84] the check over these like small uh
[L183] [06:34.00] complicated objects. For like, should I
[L184] [06:36.12] move my finger to the right? Like, is
[L185] [06:38.48] there nothing in this group? Would
[L186] [06:39.84] finger search just just go straight
[L187] [06:41.88] through this group or not? Is basically
[L188] [06:43.88] what you're asking.
[L189] [06:45.08] >> So, the unit that you're operating on is
[L190] [06:46.92] not a single integer, it's a
[L191] [06:49.08] a group.
[L192] [06:49.88] >> Yeah, it's like a group of them. So, you
[L193] [06:51.40] use some kind of table look up. Uh
[L194] [06:53.64] And so, well, it's it's it's much
[L195] [06:55.12] fancier than a table look up, actually.
[L196] [06:56.68] It's
[L197] [06:57.44] It goes through some other model called
[L198] [06:59.72] the linear decision tree model. Like, so
[L199] [07:02.20] it's like in some weird model where you
[L200] [07:03.80] can actually get a faster three some
[L201] [07:05.52] solution. You can get a N to the 1.5
[L202] [07:07.64] solution. And there's It's a really
[L203] [07:09.84] interesting and sophisticated solution,
[L204] [07:11.36] but what I want to emphasize is it
[L205] [07:12.84] starts from
[L206] [07:14.52] the finger search solution. And sort of
[L207] [07:16.84] like figuring out how to like
[L208] [07:19.08] process finger moves faster.
[L209] [07:21.84] Uh sort of do pre-processing so that
[L210] [07:23.28] finger moves can can go faster.
[L211] [07:26.52] >> Yeah, I saw the the time complexity
[L212] [07:28.68] this. It's N squared divided by
[L213] [07:32.08] log N divided by log log N all raised to
[L214] [07:36.04] the 2/3.
[L215] [07:37.60] What Is there any intuition behind I
[L216] [07:39.20] mean, that's just crazy.
[L217] [07:40.24] >> So, there are several algorithms of this
[L218] [07:41.68] kind, and they all work by doing some
[L219] [07:44.80] modification on what I was talking about
[L220] [07:46.96] because you can sort of reduce to a
[L221] [07:48.48] different model. Like a like a
[L222] [07:51.24] a different kind of look up table, a
[L223] [07:53.36] different kind of set of tricks.
[L224] [07:55.56] And you know, maybe there is some
[L225] [07:57.08] savings you can do here and there by
[L226] [07:59.48] sort of compressing things a little
[L227] [08:00.76] differently. Um so, that yeah, there are
[L228] [08:03.36] several algorithms that beat the n
[L229] [08:05.40] squared running time bound,
[L230] [08:07.48] and they all, to my knowledge, kind of
[L231] [08:10.04] work in a similar type of of way. Like
[L232] [08:13.12] they
[L233] [08:13.92] they're they're taking this n squared
[L234] [08:16.12] time algorithm and finding little ways
[L235] [08:17.80] to like pre-process
[L236] [08:20.24] and then optimize like based on the
[L237] [08:21.92] pre-processing. Like make finger
[L238] [08:24.08] searches faster and things like that.
[L239] [08:26.04] Sort of yeah.
[L240] [08:27.88] >> A lot of your research is on this this
[L241] [08:30.60] topic of fine-grained complexity or kind
[L242] [08:32.44] of lowering lower bounds. So, um maybe
[L243] [08:35.76] you can explain
[L244] [08:37.16] what is fine-grained
[L245] [08:37.80] >> Lowering lower bounds, I like that.
[L246] [08:38.96] >> Yeah, lowering
[L247] [08:39.42] >> [laughter]
[L248] [08:40.16] >> Um the idea behind fine-grained
[L249] [08:41.96] complexity is we have a variety
[L250] [08:45.40] of problems, canonical problems that
[L251] [08:50.28] we teach to undergrads.
[L252] [08:52.92] Um we have canonical algorithms for
[L253] [08:55.84] these problems. These algorithms have
[L254] [08:59.08] resisted any major improvements in
[L255] [09:02.96] decades, and so, we wonder, are these
[L256] [09:07.32] algorithms optimal?
[L257] [09:09.08] And what does a theory of optimality
[L258] [09:11.08] look like in terms of time complexity?
[L259] [09:13.72] So, what if we just focus solely on the
[L260] [09:16.60] time complexity of a problem? Like the
[L261] [09:18.72] fastest algorithm that will solve that
[L262] [09:21.00] problem.
[L263] [09:22.24] What does complexity look like then?
[L264] [09:25.92] Because like P versus NP is not about
[L265] [09:28.36] time I mean, it's about time complexity
[L266] [09:30.00] but on a coarse
[L267] [09:31.36] grained level where P is just
[L268] [09:34.76] polynomial time. But that polynomial
[L269] [09:36.68] could be n to the 10 into the billion
[L270] [09:39.12] whatever and so like showing that
[L271] [09:41.08] something's not in P is is showing that
[L272] [09:43.44] it needs some super polynomial amount of
[L273] [09:45.56] time. Whereas here we we are concerned
[L274] [09:48.08] with there's a canonical problem it
[L275] [09:50.88] takes
[L276] [09:52.36] n cubed time with some very
[L277] [09:55.80] elegant canonical algorithm. We want to
[L278] [09:58.00] know
[L279] [09:59.12] could you do any better? Could you
[L280] [10:00.20] improve that exponent to n to the 3
[L281] [10:03.00] minus epsilon for some epsilon?
[L282] [10:05.96] And then you ask, well
[L283] [10:08.08] suppose I have a problem over here
[L284] [10:10.36] and it has a quadratic time algorithm.
[L285] [10:13.56] And I want to know
[L286] [10:15.92] if I can improve that quadratic time
[L287] [10:17.84] algorithm by a little bit. Then you
[L288] [10:19.12] start asking questions like, well,
[L289] [10:21.08] suppose I improve this algorithm by a
[L290] [10:24.04] little bit.
[L291] [10:25.28] Can I improve this algorithm over here
[L292] [10:27.72] by a little bit?
[L293] [10:29.56] And this is naturally a notion of
[L294] [10:30.88] reduction like saying that like
[L295] [10:33.44] I want to have some reduction from
[L296] [10:34.80] problem A to problem B
[L297] [10:37.12] so that if I can improve the algorithm
[L298] [10:40.52] for problem B just a little bit
[L299] [10:42.76] then I can also improve the algorithm
[L300] [10:44.16] for for problem A by just a little bit.
[L301] [10:47.40] This actually leads to a different
[L302] [10:49.68] notion of complexity. You can even take
[L303] [10:52.04] an NP-complete problem
[L304] [10:54.28] and a P problem
[L305] [10:56.40] and reduce the NP problem to the P
[L306] [10:58.00] problem and the question still makes
[L307] [10:59.56] sense.
[L308] [11:00.88] So
[L309] [11:02.08] for example,
[L310] [11:03.56] uh you could talk about the subset sum
[L311] [11:05.80] uh problem, okay? So the subset sum
[L312] [11:08.40] problem
[L313] [11:09.52] you've uh got n numbers
[L314] [11:13.48] and a target value.
[L315] [11:15.88] And you want to know if there's a subset
[L316] [11:18.00] of those numbers that sum to a
[L317] [11:20.36] particular target value, okay?
[L318] [11:22.60] Now you got n numbers, there's two to
[L319] [11:24.60] the n possible subsets.
[L320] [11:27.64] The obvious algorithm takes two to the n
[L321] [11:29.24] time.
[L322] [11:30.20] Okay?
[L323] [11:32.04] But you can actually do better than
[L324] [11:34.16] this. And the way you do better than
[L325] [11:36.48] this is to reduce to a polynomial time
[L326] [11:39.00] solvable problem.
[L327] [11:41.04] So,
[L328] [11:42.16] you can get a algorithm which runs in
[L329] [11:45.36] square root of 2 to the n time for the
[L330] [11:48.84] subset sum problem. You can avoid
[L331] [11:51.08] enumerating over all the possible
[L332] [11:52.56] subsets in a substantial way. And this
[L333] [11:54.76] is in fact known um
[L334] [11:57.84] commonly in cryptanalysis by
[L335] [12:00.08] um I guess a like a meet in the middle
[L336] [12:02.80] uh type approach. Like So, people do
[L337] [12:06.08] this sort of thing all the time.
[L338] [12:08.20] The idea is you partition the set of all
[L339] [12:12.12] the numbers into two halves, n over two,
[L340] [12:15.04] n over two.
[L341] [12:16.20] You enumerate all the subset sums on the
[L342] [12:18.76] two halves. So, you have 2 to the n over
[L343] [12:21.04] two possible sums for like the first
[L344] [12:24.40] half, 2 to the n over two possible sums
[L345] [12:27.08] for the second half. Then you want to
[L346] [12:28.84] know, is there a number from the first
[L347] [12:32.16] half,
[L348] [12:33.40] you know, from this huge list,
[L349] [12:35.68] plus another number from the second
[L350] [12:37.72] half, this huge list, that sums to the
[L351] [12:39.84] target.
[L352] [12:41.04] Now, this is the two sum problem.
[L353] [12:44.04] This is really nothing more than the two
[L354] [12:45.36] sum problem, which you can solve by
[L355] [12:48.00] sorting
[L356] [12:49.16] and binary search.
[L357] [12:51.16] And this is a reduction. We have shown
[L358] [12:53.84] how to solve a subset sum problem
[L359] [12:57.76] like which would normally take 2 to the
[L360] [12:59.44] n time
[L361] [13:00.64] in square root of 2 to the n time. An
[L362] [13:02.48] NP-complete problem by reducing it to a
[L363] [13:05.88] problem like two sum. The obvious
[L364] [13:09.12] algorithm there takes n squared time
[L365] [13:11.40] trying all the pairs of numbers to see
[L366] [13:13.16] if they sum to a target, and using an n
[L367] [13:16.36] log n time algorithm for that.
[L368] [13:18.92] So, so fine-grained complexity can
[L369] [13:22.24] can relate problems that would not be
[L370] [13:24.88] relatable at all in the traditional P
[L371] [13:27.20] versus NP theory. Like one problem is NP
[L372] [13:29.52] complete, the other problem is not, so
[L373] [13:30.88] they
[L374] [13:31.60] they should not have a polynomial time
[L375] [13:33.12] reduction between them, like in general,
[L376] [13:34.84] right? But so but if you just look at
[L377] [13:37.00] the time complexity and you focus on
[L378] [13:39.20] okay, I have an algorithm, 2 to the n
[L379] [13:41.00] algorithm, is it the best possible?
[L380] [13:43.92] Then um
[L381] [13:45.40] and then I have a n squared algorithm,
[L382] [13:47.08] is it the best possible? And you then
[L383] [13:48.84] you can relate the two problems.
[L384] [13:50.88] And this is a general phenomenon that
[L385] [13:52.72] you can relate problems that look
[L386] [13:55.52] like they should have nothing to do with
[L387] [13:57.28] each other.
[L388] [13:58.52] >> So you talked about
[L389] [14:00.24] you talked about reducing subset sum to
[L390] [14:03.40] two sum
[L391] [14:04.64] and but subset sum is n arbitrary
[L392] [14:08.68] integers that sum to
[L393] [14:10.68] the target sum, right?
[L394] [14:11.92] >> Yeah, so the idea is um
[L395] [14:14.88] nobody said I had to use a polynomial
[L396] [14:17.00] time reduction or something like that to
[L397] [14:19.68] reduce one problem to another.
[L398] [14:21.96] So so what's what happened what happened
[L399] [14:24.68] the trick was I took this subset sum
[L400] [14:27.84] problem that had n numbers
[L401] [14:30.04] and then I blew it up
[L402] [14:32.48] to an instance of this two sum problem.
[L403] [14:35.04] But that two sum problem has about
[L404] [14:37.24] square root of 2 to the n numbers.
[L405] [14:40.00] Now I can solve two sum in linear time.
[L406] [14:42.92] So that so solving that instance gives
[L407] [14:45.52] me a square root of 2 to the n time
[L408] [14:47.76] algorithm for the original problem.
[L409] [14:49.64] But yeah, in in the meantime, going from
[L410] [14:52.24] one problem to the other, I blew it up.
[L411] [14:54.48] And I but by blowing it up, I I'm able
[L412] [14:56.92] to improve the time complexity of the
[L413] [14:59.36] obvious algorithm for subset sum.
[L414] [15:02.00] >> I get it. Okay, so the reduction
[L415] [15:04.36] it it's kind of like the
[L416] [15:06.76] if you solve the subset sum, you have
[L417] [15:09.44] some time complexity, and if you
[L418] [15:11.56] translate it to the other problem, you
[L419] [15:13.36] lose a little bit of time complexity,
[L420] [15:14.92] but less than the aggregate.
[L421] [15:17.32] >> So all you want to make sure is when all
[L422] [15:19.48] the dust is cleared and settled, you
[L423] [15:21.44] want to be able to say, "Look, if I can
[L424] [15:23.64] improve
[L425] [15:25.00] the obvious algorithm for two sum,
[L426] [15:27.28] then I can improve the obvious algorithm
[L427] [15:28.92] for subset sum." And that's what this
[L428] [15:30.36] thing achieves.
[L429] [15:31.96] Right? Because I know because I know how
[L430] [15:33.68] to get a faster algorithm for two sum,
[L431] [15:36.52] I can get one for subset sum. So, so you
[L432] [15:39.64] just want your your reduction between
[L433] [15:42.00] two problems to have this property. If I
[L434] [15:43.60] can improve
[L435] [15:44.84] one problem by a little bit in running
[L436] [15:46.88] time, I can improve the other problem by
[L437] [15:48.80] a little bit.
[L438] [15:50.04] >> In one of your talks, you you mentioned
[L439] [15:52.52] preserving magic between Okay, so this
[L440] [15:55.36] is that.
[L441] [15:56.20] >> this is exactly like preserving magic
[L442] [15:58.16] because
[L443] [15:58.88] >> Well, I mean,
[L444] [15:59.80] >> once you see the two sum solution, it's
[L445] [16:01.52] not so magical anymore. But, imagine
[L446] [16:04.83] >> [laughter]
[L447] [16:05.12] >> that you didn't know about sorting and
[L448] [16:08.00] binary search and the like, and someone
[L449] [16:10.72] just says, "Find a pair of things with a
[L450] [16:13.76] certain property, and there are n
[L451] [16:15.72] things."
[L452] [16:16.92] And you're like, "Well, I mean, all the
[L453] [16:19.04] number of possible pairs
[L454] [16:21.00] is about n squared, so maybe it'll take
[L455] [16:23.04] me n squared."
[L456] [16:24.32] In this particular case, because they're
[L457] [16:26.56] numbers and you're summing them,
[L458] [16:28.52] there's an n log n time algorithm. It is
[L459] [16:30.96] a It is a surprise when you first see
[L460] [16:33.72] that no, you don't have to try all of
[L461] [16:36.48] the pairs of numbers. There is a
[L462] [16:38.44] shortcut. There is a clear shortcut that
[L463] [16:41.24] lets you find a pair much faster.
[L464] [16:44.12] And then, you can use that uh
[L465] [16:47.04] surprise um
[L466] [16:49.28] or magic, if you will, and get something
[L467] [16:53.00] for a subset sum. Get a algorithm for
[L468] [16:54.68] subset sum that avoids trying all of the
[L469] [16:58.24] two to the n subsets.
[L470] [17:00.12] >> So, I understand one of the the driving
[L471] [17:03.32] motives for pursuing this, I guess,
[L472] [17:06.08] lowering of lower bounds
[L473] [17:08.12] is that
[L474] [17:09.76] um
[L475] [17:10.76] strong exponential time hypothesis, or I
[L476] [17:12.96] see it, you know, SETH.
[L477] [17:15.68] Um could you explain that and its
[L478] [17:17.72] significance?
[L479] [17:18.80] >> Strong ETH is like a severe
[L480] [17:21.08] strengthening
[L481] [17:22.60] of the P versus NP question.
[L482] [17:25.56] So,
[L483] [17:26.72] P versus NP
[L484] [17:28.24] is um, asking whether the SAT problem
[L485] [17:32.88] um,
[L486] [17:34.04] has a polynomial time algorithm or not.
[L487] [17:37.88] Right? And
[L488] [17:39.24] strong ETH
[L489] [17:40.96] is basically saying that
[L490] [17:44.40] for the SAT problem,
[L491] [17:46.72] uh, you cannot solve it
[L492] [17:48.96] faster
[L493] [17:50.56] than much faster than two to the end.
[L494] [17:53.16] So, there's no 1.999
[L495] [17:56.52] to the end time algorithm.
[L496] [17:58.48] For every string of nines, there is no
[L497] [18:01.00] 1.9999 to the end time algorithm.
[L498] [18:05.04] Um, to say the hypothesis totally
[L499] [18:07.64] precisely, it has to do with the K-SAT
[L500] [18:09.88] problem
[L501] [18:11.12] and you're looking at
[L502] [18:13.52] clauses of
[L503] [18:15.24] length K for arbitrary K, but
[L504] [18:19.00] um,
[L505] [18:20.12] those details don't matter so much. It's
[L506] [18:22.08] a canonically NP-complete problem. SAT
[L507] [18:24.92] is solved all the time in practice. It's
[L508] [18:29.88] extremely useful for a verification
[L509] [18:32.64] nowadays. It's an It's an engine
[L510] [18:35.56] for verification. Um, so it can be
[L511] [18:38.48] solved fairly well in practice.
[L512] [18:41.40] However, in the worst case, we still
[L513] [18:43.80] don't know how to solve it uh,
[L514] [18:46.12] significantly faster than two to the
[L515] [18:48.44] end.
[L516] [18:49.28] So, the hypothesis that it needs, say,
[L517] [18:52.00] 1.99999
[L518] [18:53.68] to the end time for all strings of nines
[L519] [18:56.44] is a very strong
[L520] [18:58.72] exponential time hypothesis. It's way
[L521] [19:01.28] stronger than P versus NP. It says, "Uh,
[L522] [19:03.32] no, no, no, no. It's not super
[L523] [19:04.88] polynomial. It's actually darn near two
[L524] [19:07.24] to the end time that you need."
[L525] [19:09.32] Right?
[L526] [19:09.80] >> And so, do you think that hypothesis is
[L527] [19:12.80] true and you know, why or why not?
[L528] [19:15.76] >> I think I'm on the record as not
[L529] [19:17.60] believing this hypothesis. Yeah. Um
[L530] [19:22.12] Yeah, why don't I believe this
[L531] [19:23.84] hypothesis?
[L532] [19:25.16] Um
[L533] [19:26.88] Well, I started thinking about this
[L534] [19:28.12] hypothesis
[L535] [19:30.48] maybe already as an
[L536] [19:32.72] undergrad, but certainly starting
[L537] [19:35.92] in grad school.
[L538] [19:37.56] Like early in grad school I was thinking
[L539] [19:39.20] about this. So, before it was even
[L540] [19:41.32] called strong ETH, I guess that shows
[L541] [19:43.80] how old I am.
[L542] [19:45.04] I was trying to think about how to solve
[L543] [19:48.52] the so-called CNF SAT problem faster
[L544] [19:51.36] than 2 to the n.
[L545] [19:52.80] And
[L546] [19:54.32] well, at the time
[L547] [19:56.16] there were a number of other NP-complete
[L548] [19:59.28] problems that had faster algorithms like
[L549] [20:01.88] subset sum.
[L550] [20:03.64] So, I thought, well, there's not I mean,
[L551] [20:06.68] what's so special about SAT? Like, if
[L552] [20:09.32] all these other problems have faster
[L553] [20:11.40] algorithms um why not SAT as well? Like
[L554] [20:15.92] if you restrict to the 3-SAT problem
[L555] [20:19.52] like So, this is where
[L556] [20:21.72] you have an AND of these clauses, each
[L557] [20:25.44] clause has like is an OR of three
[L558] [20:29.36] variables some of the variables may be
[L559] [20:31.52] negated.
[L560] [20:32.84] You want to know if there's a way to set
[L561] [20:34.12] all the variables to make all the
[L562] [20:35.80] clauses simultaneously true. Um there is
[L563] [20:38.84] a faster algorithm for that.
[L564] [20:40.68] Um but this is a more general version of
[L565] [20:43.20] SAT. Um
[L566] [20:45.40] So, at first I just thought, well,
[L567] [20:47.24] there's no good reason to think in a
[L568] [20:49.20] lower bound these other related problems
[L569] [20:50.76] have upper bounds.
[L570] [20:52.68] So, why not?
[L571] [20:54.08] But then
[L572] [20:55.48] um over time I would have different
[L573] [20:58.24] attacks
[L574] [20:59.92] on strong ETH, like trying to refute it.
[L575] [21:02.40] Always trying to refute it in different
[L576] [21:04.96] ways, these attacks would fail
[L577] [21:08.36] in some completely catastrophic and
[L578] [21:12.72] ridiculous way, like um they would like
[L579] [21:16.68] have no chance of
[L580] [21:18.64] actually solving the original problem.
[L581] [21:21.44] But by sort of staring at my failure and
[L582] [21:24.56] trying to think, well, there's something
[L583] [21:26.52] interesting happening here. What can I
[L584] [21:28.08] do with this? Like there's something
[L585] [21:30.80] interesting. Yeah, it doesn't refute uh
[L586] [21:34.28] the strong ETH thing.
[L587] [21:36.44] What does it do? So, by trying to pivot
[L588] [21:39.28] and and figure out, okay, what can I do
[L589] [21:41.12] with my failure?
[L590] [21:42.76] I was able to solve a like a variety of
[L591] [21:45.80] other problems instead.
[L592] [21:47.80] And so, after a while, I realized the
[L593] [21:50.68] truth value
[L594] [21:52.32] of strong ETH to me
[L595] [21:54.68] is almost irrelevant. Like because if I
[L596] [21:57.28] believe that it's false, then I get good
[L597] [22:00.24] ideas.
[L598] [22:01.68] I get I get good ideas. Like
[L599] [22:04.28] And so, by trying to think about, okay,
[L600] [22:08.64] what would an algorithm that breaks
[L601] [22:11.60] through the end look like? What could it
[L602] [22:13.72] look like?
[L603] [22:15.40] I I sort of force myself to think in a
[L604] [22:18.00] different way.
[L605] [22:19.44] Like I I I have to like discard
[L606] [22:21.92] other natural algorithmic possibilities
[L607] [22:24.04] because we know they they won't work.
[L608] [22:27.20] Um
[L609] [22:27.88] and I have to think in a in a different
[L610] [22:31.40] direction. And and so,
[L611] [22:33.32] because it kind of like sends my brain
[L612] [22:36.00] in a different direction, sends me
[L613] [22:37.56] thinking a different way,
[L614] [22:39.76] it's very useful for research.
[L615] [22:42.28] You know, you you
[L616] [22:43.36] I mean, even even though I still haven't
[L617] [22:45.40] refuted it or whatever, like it's very
[L618] [22:48.24] useful for me to believe that it's
[L619] [22:50.24] false. Like operationally.
[L620] [22:52.68] So, the truth value, well, I mean
[L621] [22:55.96] I believe this is a minority opinion,
[L622] [22:57.64] right? Why why would they go against I
[L623] [23:00.08] mean, I think um
[L624] [23:02.64] for example, Russell and Piazzo, good
[L625] [23:05.48] friend of mine who uh, helped propose
[L626] [23:08.04] this.
[L627] [23:08.92] I mean, he always emphasizes to me,
[L628] [23:11.12] "Well, this this is a hip hypothesis.
[L629] [23:13.52] It, you know, we didn't We explicitly
[L630] [23:15.08] did not name it a conjecture."
[L631] [23:17.20] We wanted to sort of put forth
[L632] [23:19.96] some lower bound that would get you to
[L633] [23:22.28] think about it. Like something that's
[L634] [23:24.96] maybe a little more controversial than
[L635] [23:27.20] the other types of things like P = NP or
[L636] [23:30.52] whatever. Or, you know, like other
[L637] [23:32.36] things that people more nor- normally
[L638] [23:33.92] believe. So, like hypothesis, which are
[L639] [23:36.28] at the edge of our understanding,
[L640] [23:39.04] can be enlightening to think about. Like
[L641] [23:41.80] where we truly don't know what the
[L642] [23:45.28] answer might be based on our intuition.
[L643] [23:48.48] Um,
[L644] [23:49.92] so this this is, I guess, one reason why
[L645] [23:52.32] it was
[L646] [23:53.36] proposed, but one reason why you might
[L647] [23:56.64] believe that strong ETH is true is
[L648] [23:59.16] because believing it implies a lot of
[L649] [24:01.76] other lower bounds for you conveniently
[L650] [24:04.80] because you can reduce the SAT problem
[L651] [24:07.16] to a bunch of other problems that seem
[L652] [24:09.00] totally unrelated like edit distance,
[L653] [24:12.80] um, various pattern matching problems.
[L654] [24:17.20] Um, they have natural
[L655] [24:20.52] polynomial time solutions if you can
[L656] [24:22.28] improve on the algorithms for any of
[L657] [24:24.92] those, you would improve the one for SAT
[L658] [24:27.52] as well. You would get something better
[L659] [24:28.84] than 2 to the n. So, believing in it
[L660] [24:31.60] sort of makes a convenient world view.
[L661] [24:34.28] It shows that all these different
[L662] [24:35.80] textbook algorithms are indeed optimal.
[L663] [24:38.44] >> We've talked about SAT or we've
[L664] [24:39.88] mentioned SAT so many times in this
[L665] [24:42.16] conversation. I know there's so many
[L666] [24:44.12] forms of that problem. What are all the
[L667] [24:46.88] different forms? And I know there's
[L668] [24:48.36] there's clause width, also this idea of
[L669] [24:50.36] depth, too.
[L670] [24:51.52] >> Um, the most common
[L671] [24:54.08] representation of a of a SAT formula is
[L672] [24:58.32] the conjunctive normal form, so-called
[L673] [25:00.88] CNF representation. And this is what
[L674] [25:04.00] modern SAT solvers get as input. They
[L675] [25:06.92] They get their file in in so-called
[L676] [25:09.32] DIMACS CNF form. And this is
[L677] [25:13.52] just every line of my file, I give you a
[L678] [25:17.76] list of
[L679] [25:19.48] uh variables, possibly with negations,
[L680] [25:22.08] and each one is a clause. And I'm
[L681] [25:24.24] supposed to take the or
[L682] [25:26.36] of those uh
[L683] [25:28.04] uh variables or negations. These are
[L684] [25:29.96] Variables or negations, they're often
[L685] [25:30.92] called literals. Okay, so I take an or
[L686] [25:32.64] of these literals.
[L687] [25:34.08] And
[L688] [25:35.16] the width
[L689] [25:36.36] of that clause is the number of literals
[L690] [25:38.60] in it.
[L691] [25:39.88] Okay?
[L692] [25:41.04] And
[L693] [25:42.32] um I'm supposed to take the and over all
[L694] [25:45.96] those lines, each line in my DIMACS CNF
[L695] [25:49.20] file.
[L696] [25:50.28] And so it's an and
[L697] [25:52.08] of a bunch of ors, and each or has
[L698] [25:57.20] some small number of literals in it.
[L699] [25:59.08] Call it K. So usually the the width is
[L700] [26:01.28] called K.
[L701] [26:02.52] And so the K-SAT problem is to find an
[L702] [26:05.56] assignment to all the variables that
[L703] [26:07.68] satisfies all the clauses when each
[L704] [26:10.60] clause has width K
[L705] [26:13.28] or width at most K.
[L706] [26:14.96] It could be smaller.
[L707] [26:16.60] Um so that's the most popular
[L708] [26:20.08] uh version. That's what
[L709] [26:22.16] SAT solvers, you know, turn on.
[L710] [26:25.00] And that's what is behind uh strong ETH.
[L711] [26:28.28] That's the representation there.
[L712] [26:30.60] Um but there are other ways uh to
[L713] [26:33.32] represent
[L714] [26:34.80] a Boolean formula. You could just simply
[L715] [26:36.80] represent it as some arbitrary
[L716] [26:39.32] expression
[L717] [26:40.68] made out made up of ors and ands and
[L718] [26:44.28] negations. It could just be some
[L719] [26:46.00] arbitrary expression with nested
[L720] [26:47.28] parentheses
[L721] [26:48.76] and all that mess. Um
[L722] [26:51.12] you could ask you know, given a formula
[L723] [26:53.64] in this representation with a bunch of
[L724] [26:56.04] variables, is there a way to set the
[L725] [26:57.72] variables to make this true? That's
[L726] [26:59.84] formula SAT.
[L727] [27:01.44] Um, you could also look at
[L728] [27:06.04] at circuits of bounded depth, as you
[L729] [27:09.04] mentioned. So,
[L730] [27:10.76] there is this
[L731] [27:12.40] um, this class of circuits that people
[L732] [27:14.56] study
[L733] [27:15.68] called uh AC uh circuits for alternating
[L734] [27:19.24] circuits. Um, it doesn't mean
[L735] [27:21.68] alternation in terms of electricity, it
[L736] [27:24.52] means alternation in terms of
[L737] [27:27.04] uh ORs and ANDs. So, these circuits are
[L738] [27:30.20] made up of uh ORs and ANDs like in
[L739] [27:34.92] layers. So, the CNF representation is a
[L740] [27:38.00] special case where I have an an AND
[L741] [27:40.84] of ORs like uh
[L742] [27:43.36] like a AND of a bunch of clauses and
[L743] [27:45.08] then ORs of the literals.
[L744] [27:47.00] But, you can go further. You can have an
[L745] [27:48.92] AND of OR of ANDs
[L746] [27:51.72] of variables with negations and things
[L747] [27:53.68] like that. And so, these are uh constant
[L748] [27:57.12] depth AC circuits. And because the idea
[L749] [28:00.60] is
[L750] [28:01.56] uh you only have some constant number of
[L751] [28:03.40] layers of these ANDs and ORs. And you
[L752] [28:05.40] can look at the SAT problem
[L753] [28:07.84] on circuits like that as well, for
[L754] [28:09.44] example. Those are Those are two
[L755] [28:11.84] uh other versions that people look at.
[L756] [28:13.80] >> Yeah, strong ETH is on K-SAT, and I saw
[L757] [28:17.16] on less than or I guess, you know,
[L758] [28:20.56] 2-SAT, 3-SAT, 4-SAT, 5-SAT. There exists
[L759] [28:23.84] solutions that are asymptotically better
[L760] [28:26.32] than 2 to the N. So, I guess it it you
[L761] [28:29.84] know, the
[L762] [28:30.96] the larger K can be, the more difficult
[L763] [28:33.24] the the problem is.
[L764] [28:34.64] >> That That is the intuition.
[L765] [28:36.20] >> I'm curious, have you ever plotted that
[L766] [28:37.84] curve? Like, is it Does it drop off, you
[L767] [28:40.60] know, exponentially or
[L768] [28:41.96] >> Yeah. Yeah. Um, th- yeah, that's what's
[L769] [28:44.68] so interesting uh about the current
[L770] [28:48.28] state of the art in K-SAT algorithms. As
[L771] [28:52.04] K increases,
[L772] [28:53.88] all of them
[L773] [28:55.40] all of the different types of algorithms
[L774] [28:56.88] you might try to run, they all approach
[L775] [29:00.88] a 2 to the n exponent. Like, as K grows
[L776] [29:04.28] and grows and grows, they get 1.99,
[L777] [29:06.88] 1.999, and so on. And yeah, it it drops
[L778] [29:12.20] I mean, it get In other words, it will
[L779] [29:13.32] like it goes towards
[L780] [29:15.32] uh pretty quickly
[L781] [29:17.16] actually. And like so we we understand
[L782] [29:19.40] like how the exponent behaves pretty
[L783] [29:22.04] well for the known algorithms we have.
[L784] [29:24.24] >> And then um for for something like
[L785] [29:26.48] 3-SAT, what is the intuition behind
[L786] [29:29.56] speeding up an exponential time search?
[L787] [29:32.52] >> Yeah, so for 3-SAT, um
[L788] [29:35.44] let's just look at a a single clause,
[L789] [29:37.60] okay? A clause that's got
[L790] [29:39.80] three variables in it, okay?
[L791] [29:42.12] We know that if
[L792] [29:43.68] uh if we set all those three variables
[L793] [29:46.16] wrong, it's going to be false. Okay, so
[L794] [29:48.20] we have to avoid one of those
[L795] [29:50.20] assignments, okay?
[L796] [29:52.04] Well, that means that there are seven
[L797] [29:54.56] out of the eight possible assignments,
[L798] [29:56.68] so there's like three variables,
[L799] [29:58.52] two to the three, eight possible
[L800] [30:00.44] assignments, seven of them could be a
[L801] [30:03.20] satisfying assignment. They uh they
[L802] [30:04.96] could be part of a satisfying
[L803] [30:06.16] assignment, we don't know. But one of
[L804] [30:07.68] them is definitely not.
[L805] [30:09.48] So the one easy way to see that 2-SAT
[L806] [30:14.20] can be solved in less than 2 to the n
[L807] [30:15.88] time is just take any clause,
[L808] [30:19.00] try one of the seven possible
[L809] [30:21.36] assignments,
[L810] [30:23.28] and plug them in,
[L811] [30:25.40] and then recurse
[L812] [30:27.20] on the remaining formula.
[L813] [30:29.52] Now, let's think about what we did. If
[L814] [30:31.44] we were just trying all the possible 2
[L815] [30:33.92] to the n assignments,
[L816] [30:35.64] and we we would like plug in,
[L817] [30:38.40] you know,
[L818] [30:39.44] uh one of eight possible assignments
[L819] [30:42.32] for each of those three variables. And
[L820] [30:44.04] so we'd have eight recursive calls.
[L821] [30:47.28] Well, we instead, because we're clever
[L822] [30:49.20] and we looked at the clauses, we have
[L823] [30:51.00] seven recursive calls.
[L824] [30:53.12] And that that's the difference. So so we
[L825] [30:55.24] reduced
[L826] [30:56.68] by three variables at the cost of seven
[L827] [30:58.92] recursive calls as opposed to eight.
[L828] [31:02.32] And this gets you a slight improvement.
[L829] [31:04.80] This gets you about
[L830] [31:06.28] uh 1.9
[L831] [31:08.40] two to the end.
[L832] [31:09.76] Something slightly better than
[L833] [31:11.80] than
[L834] [31:13.04] uh two to the end.
[L835] [31:14.20] Okay, but you can do better than this.
[L836] [31:16.76] Um
[L837] [31:17.48] But this is this is sort of like the
[L838] [31:19.84] idea. You try to look at ways to plug in
[L839] [31:23.12] variables that will force constraints so
[L840] [31:26.76] you can rule out a large portion of the
[L841] [31:29.44] possible assignments.
[L842] [31:30.84] >> When I was thinking about circuits, it
[L843] [31:33.56] and you know, the different widths and
[L844] [31:35.16] depths, I I don't know if this is uh
[L845] [31:37.60] unusual question, but it it reminds me
[L846] [31:41.08] of neural nets, but the operators are
[L847] [31:43.44] different and the space of the
[L848] [31:47.36] uh the literals is different. So instead
[L849] [31:49.16] of booleans, it's maybe floating points.
[L850] [31:51.96] And so it just made me wonder about uh
[L851] [31:55.08] the algorithms that you might apply on a
[L852] [31:56.76] neural net. Is there, you know, analogs
[L853] [31:59.64] in between these two spaces?
[L854] [32:01.16] >> Yes. Yes. So
[L855] [32:03.08] um
[L856] [32:04.88] Yeah, if we look at
[L857] [32:07.04] say I want to model a neural network
[L858] [32:10.48] on So I want to compute say it's still a
[L859] [32:13.44] boolean function,
[L860] [32:15.04] but I want to do it with like a neural
[L861] [32:16.72] network. So like I want to
[L862] [32:19.28] use, let's say
[L863] [32:21.40] uh relus or
[L864] [32:23.56] um sign activation functions or or what
[L865] [32:26.92] what have you. Um
[L866] [32:29.20] There is
[L867] [32:30.36] a slightly more general like gate that
[L868] [32:33.32] we can use instead of ors and ands. That
[L869] [32:36.12] turns out to basically be equivalent.
[L870] [32:39.00] So, if instead of using ORs and ANDs, we
[L871] [32:42.52] use a so-called majority gate,
[L872] [32:45.04] which outputs one if and only if at
[L873] [32:47.84] least half of its inputs are one.
[L874] [32:51.92] Using this and negations, we can
[L875] [32:54.12] actually simulate
[L876] [32:56.24] uh neural nets, like the usual types of
[L877] [32:58.84] neural nets that you think of with the
[L878] [33:01.60] usual types of activation functions. So,
[L879] [33:04.04] if they have a constant number of layers
[L880] [33:06.88] of neurons, we can get a constant number
[L881] [33:09.16] of layers
[L882] [33:10.48] of majority gates and and negations.
[L883] [33:14.68] So, once you go So, this is so-called TC
[L884] [33:16.84] circuits for threshold circuits.
[L885] [33:19.52] Uh yeah, so once you allow threshold
[L886] [33:21.00] circuits, you can start to model uh
[L887] [33:23.12] neural networks.
[L888] [33:24.40] >> Still using booleans. It's just
[L889] [33:26.04] >> We're still looking at boolean inputs
[L890] [33:27.40] though, yes. So, once you allow your
[L891] [33:30.20] input space
[L892] [33:32.08] to
[L893] [33:33.44] to be larger and like have floating
[L894] [33:36.12] points, then
[L895] [33:37.84] um you can you can prove a lot
[L896] [33:40.96] uh
[L897] [33:41.60] more in terms of lower bounds. You can
[L898] [33:43.48] find like things that take like depth
[L899] [33:46.24] three
[L900] [33:47.36] in a neural net that's, you know, can't
[L901] [33:48.92] be done in depth two and so on.
[L902] [33:51.20] Um
[L903] [33:52.68] So, yeah, once you go
[L904] [33:54.92] past that and you start looking at just
[L905] [33:56.72] arbitrary real domain, it it becomes a
[L906] [34:00.40] a a totally different picture than from
[L907] [34:02.64] a discrete domain.
[L908] [34:04.84] >> OpenAI, Anthropic, Cursor, and Vercel
[L909] [34:08.60] all use this product to make their lives
[L910] [34:10.36] better.
[L911] [34:11.32] And the problem it solves is when you're
[L912] [34:13.20] building SaaS or an ad product and you
[L913] [34:15.88] want to sell to other companies, there's
[L914] [34:17.72] all these requirements you need to meet.
[L915] [34:19.84] There's SSO, there's SCIM, there's RBAC,
[L916] [34:23.48] there's audit logs. These are all things
[L917] [34:25.28] that take time to integrate, but aren't
[L918] [34:27.48] the main focus of your app. WorkOS is an
[L919] [34:29.80] API layer that lets you meet all of
[L920] [34:31.44] these requirements in just a few lines
[L921] [34:33.68] of code. So, let's say you have a new
[L922] [34:35.72] SaaS product and you want to sell to
[L923] [34:37.40] other companies, WorkOS will solve all
[L924] [34:39.88] of these critical feature gaps for you.
[L925] [34:42.60] You can check them out at workos.com to
[L926] [34:45.04] learn more and get started. And I
[L927] [34:47.20] appreciate them for supporting my work
[L928] [34:49.08] and sponsoring this podcast. One topic I
[L929] [34:51.64] thought might be fun to go over is you
[L930] [34:53.76] you wrote this paper about the
[L931] [34:55.76] likelihoods of these various conjectures
[L932] [34:58.72] in complexity theory and
[L933] [35:01.52] I I pulled a few of these that were kind
[L934] [35:04.24] of a minority opinions or maybe, you
[L935] [35:06.96] know, less less common takes. So, I'm
[L936] [35:09.36] curious to hear your rationale. So,
[L937] [35:11.74] >> [laughter]
[L938] [35:12.28] >> uh one of them the well-known one, you P
[L939] [35:15.28] P not equal to NP or, you know, P versus
[L940] [35:17.76] NP.
[L941] [35:18.84] Um
[L942] [35:20.20] you assigned an 80% confidence that
[L943] [35:22.60] they're not the same. And I think most
[L944] [35:25.64] people say much higher confidence. So,
[L945] [35:28.44] why do you why would you assign such a
[L946] [35:29.92] low confidence that they're not the
[L947] [35:31.32] same?
[L948] [35:32.68] >> It's interesting because I think I
[L949] [35:34.20] originally had something like
[L950] [35:36.56] 75%
[L951] [35:38.92] but then uh my college classmate Scott
[L952] [35:41.84] Aaronson was like, "How dare you?" kind
[L953] [35:44.08] of you know,
[L954] [35:44.92] he was
[L955] [35:45.15] >> [laughter]
[L956] [35:45.52] >> he was he he sort of called me out and
[L957] [35:47.44] I'm like, "Okay, fine. For you 80%
[L958] [35:49.48] fine."
[L959] [35:50.40] I guess that my point is that
[L960] [35:53.80] we really don't understand polynomial
[L961] [35:56.64] time computation
[L962] [35:58.76] as deeply
[L963] [36:00.12] as we think we do. And
[L964] [36:02.92] there are
[L965] [36:03.92] surprises like all the time
[L966] [36:07.16] in the power of algorithms.
[L967] [36:10.08] There are very few surprises in terms of
[L968] [36:12.92] lower bounds. Like, when we are able to
[L969] [36:15.24] prove a lower bound,
[L970] [36:17.36] typically it's something we
[L971] [36:20.20] very much expected to be true
[L972] [36:22.40] but it was hard to prove. It was hard to
[L973] [36:24.72] prove.
[L974] [36:26.16] Somehow we pulled it off, we got what we
[L975] [36:28.00] expected to be true.
[L976] [36:29.68] But all the time in algorithms
[L977] [36:31.88] people are finding algorithms where
[L978] [36:35.00] it's just like surprising. Just
[L979] [36:37.56] Wait. What? How How do you get something
[L980] [36:42.16] that fast? You're right. So
[L981] [36:44.80] uh this just happens over and over.
[L982] [36:47.48] When I was younger
[L983] [36:49.44] um when I was first thinking about P
[L984] [36:51.04] versus NP
[L985] [36:53.44] I
[L986] [36:55.72] like I had an intuition for what should
[L987] [36:57.92] be.
[L988] [36:59.24] And
[L989] [37:01.00] what I've understood over the years is
[L990] [37:02.56] that
[L991] [37:03.52] my intuition for what should be
[L992] [37:06.04] is often just wrong. And I'm I'm having
[L993] [37:09.36] to revise my intuitions uh all the time.
[L994] [37:13.28] So when something like this happens
[L995] [37:16.40] often enough
[L996] [37:18.28] you start asking yourself, "What do I
[L997] [37:20.84] really understand?
[L998] [37:23.84] Uh do I really understand P versus NP?"
[L999] [37:26.56] Like I mean, I understand the the the
[L1000] [37:29.24] statement, right? Like it's just one of
[L1001] [37:31.32] those problems where
[L1002] [37:33.76] somehow it is not so difficult to to
[L1003] [37:37.28] make formal, to write down
[L1004] [37:38.92] mathematically.
[L1005] [37:40.48] But to actually know what the answer is
[L1006] [37:43.72] is just orders of magnitude more
[L1007] [37:46.52] difficult than it is to phrase the
[L1008] [37:48.96] problem. And complexity theory in
[L1009] [37:50.84] particular is littered with
[L1010] [37:54.32] statements like this where
[L1011] [37:56.68] um
[L1012] [37:58.28] the the space of algorithms is just that
[L1013] [38:00.28] vast. Um
[L1014] [38:01.84] so if you just if you're just keep
[L1015] [38:03.72] getting surprised over time, you're just
[L1016] [38:05.16] like, "Well, what
[L1017] [38:06.68] what do I understand?" Maybe it was just
[L1018] [38:08.36] misplaced confidence.
[L1019] [38:10.36] >> Okay, what about this one? So
[L1020] [38:12.60] EXP not equal to NEXP or would you say
[L1021] [38:15.88] NEXP?
[L1022] [38:16.80] >> Oh, NEXP. Yeah. EXP versus NEXP. So this
[L1023] [38:19.36] is like the exponential time
[L1024] [38:22.12] of P versus NP.
[L1025] [38:24.40] >> For X not equal to NX or NEXP,
[L1026] [38:29.40] you gave it a 45% chance. And if this is
[L1027] [38:32.18] >> [laughter]
[L1028] [38:32.40] >> the P not equal to NP
[L1029] [38:34.96] equivalent, but for exponential time,
[L1030] [38:36.84] why is your
[L1031] [38:37.68] >> Yeah.
[L1032] [38:38.16] >> Why is it so low?
[L1033] [38:39.40] >> Oh, because exponential time algorithms
[L1034] [38:41.80] are even more powerful.
[L1035] [38:43.64] Did I really say 45%? I mean,
[L1036] [38:45.96] >> You did.
[L1037] [38:47.28] >> versus X or NX versus co-NX.
[L1038] [38:50.16] >> Yeah, NX not equal to X 45%.
[L1039] [38:53.14] >> [laughter]
[L1040] [38:53.16] >> I have it.
[L1041] [38:53.92] It's in this table.
[L1042] [38:55.20] >> So, so in other words, I believe NX
[L1043] [38:57.60] equals X more
[L1044] [38:59.68] than I believe they're different, right?
[L1045] [39:01.92] So,
[L1046] [39:03.64] um yeah, let me try to explain why. So,
[L1047] [39:06.60] you can think of the NX versus X
[L1048] [39:10.00] question
[L1049] [39:11.68] as
[L1050] [39:13.16] um some special case
[L1051] [39:15.32] of P versus NP,
[L1052] [39:17.24] where instead of looking at the
[L1053] [39:19.40] arbitrary SAT problem,
[L1054] [39:21.88] I'm looking at a SAT problem which is
[L1055] [39:24.84] extremely compressible.
[L1056] [39:27.56] So, there's like a really small little
[L1057] [39:30.12] computer
[L1058] [39:32.04] that is exponentially smaller than the
[L1059] [39:34.40] length of the instance, and it just
[L1060] [39:36.52] outputs the character
[L1061] [39:38.72] uh on the line number and the column
[L1062] [39:40.52] number for the for the DIMACS CNF, like
[L1063] [39:42.68] the the CNF file, okay? So, it's like a
[L1064] [39:45.56] extreme compression
[L1065] [39:47.96] of like some file.
[L1066] [39:49.76] So, it's like you zipped it down to like
[L1067] [39:51.56] something like exponentially smaller
[L1068] [39:53.96] than its original length, okay?
[L1069] [39:56.60] So, it's like some super compressed,
[L1070] [39:58.28] extremely highly regular
[L1071] [40:00.60] SAT instance. So, I give you that, and I
[L1072] [40:03.48] ask you,
[L1073] [40:05.44] uh when you unpack this thing,
[L1074] [40:07.76] decompress it,
[L1075] [40:09.60] is the result going to be satisfiable or
[L1076] [40:11.92] not?
[L1077] [40:13.12] And I want you to solve this
[L1078] [40:15.96] in time polynomial in the decompressed
[L1079] [40:18.80] representation.
[L1080] [40:20.84] Okay.
[L1081] [40:21.92] Okay. So, the point is that like this is
[L1082] [40:24.00] SAT, but
[L1083] [40:25.88] in the some very special case where the
[L1084] [40:27.72] thing is extremely structured.
[L1085] [40:30.20] So, the idea
[L1086] [40:31.88] um one conjecture for why SAT solvers
[L1087] [40:37.52] work
[L1088] [40:38.72] um
[L1089] [40:39.32] in practice.
[L1090] [40:40.80] Like one I mean this is
[L1091] [40:42.96] I mean conjecture maybe overkill because
[L1092] [40:46.24] I mean this is just this is not even a
[L1093] [40:48.32] well-formed mathematical statement. So,
[L1094] [40:50.92] one hypothesis for why SAT solvers work
[L1095] [40:53.72] in practice is because
[L1096] [40:55.80] um the real world is highly structured.
[L1097] [40:58.60] The real world is governed by physical
[L1098] [41:01.08] laws
[L1099] [41:02.24] that are not random. They're not
[L1100] [41:04.04] arbitrary. Like from a very small number
[L1101] [41:06.88] of rules, we can recreate so much of
[L1102] [41:09.32] science.
[L1103] [41:10.84] So,
[L1104] [41:12.08] what arises in practice from designs of
[L1105] [41:15.32] hardware and things like this are often
[L1106] [41:17.56] extremely compressible. They have to be
[L1107] [41:19.88] extremely compressible.
[L1108] [41:22.56] And
[L1109] [41:23.92] so maybe it's true that you know, every
[L1110] [41:27.68] uh SAT which has
[L1111] [41:29.60] uh a highly compact representation can
[L1112] [41:32.36] just be solved uh efficiently. This is
[L1113] [41:35.32] This is the idea of whether, you know,
[L1114] [41:37.68] NEXP equals EXP.
[L1115] [41:39.64] Um that it when it's really really
[L1116] [41:41.44] structured like that and super
[L1117] [41:42.88] compressible, there is some advantage.
[L1118] [41:45.24] It's not like a completely random and
[L1119] [41:47.88] since it's not like something arbitrary,
[L1120] [41:49.44] it's No, it's in fact very very special.
[L1121] [41:51.92] >> The other one is 80% likelihood on NEXP
[L1122] [41:56.24] equal to coNEXP,
[L1123] [41:58.60] and you wrote why would a
[L1124] [42:00.28] self-respecting complexity theory do
[L1125] [42:02.68] that?
[L1126] [42:03.74] >> [laughter]
[L1127] [42:04.68] >> Yeah, I was curious why that's such a
[L1128] [42:06.60] contentious statement.
[L1129] [42:08.36] >> So, NEXP versus coNEXP. Let's Let's
[L1130] [42:10.48] first talk about NP versus co-NP.
[L1131] [42:13.84] So, co-NP
[L1132] [42:15.64] um
[L1133] [42:17.12] is like the class of sort of complements
[L1134] [42:20.56] of NP-complete problems like
[L1135] [42:23.00] like UNSAT, like checking whether
[L1136] [42:24.72] something's UNSAT.
[L1137] [42:26.44] Now, from the time complexity point of
[L1138] [42:28.28] view
[L1139] [42:29.36] there's no difference between checking
[L1140] [42:31.20] SAT and UNSAT. You can always flip the
[L1141] [42:32.84] answer.
[L1142] [42:34.00] But from the complexity point of view,
[L1143] [42:35.88] if I if I ask you does co-NP equal NP?
[L1144] [42:40.20] What I'm asking you is, could you prove
[L1145] [42:42.72] to me
[L1146] [42:43.84] that a formula is unsatisfiable
[L1147] [42:46.96] with a short proof?
[L1148] [42:48.72] When it's satisfiable I can give you a
[L1149] [42:51.16] short proof. I can just give you the
[L1150] [42:52.60] satisfying assignment. You plug it in,
[L1151] [42:55.00] check that it works. But if it's
[L1152] [42:56.68] unsatisfiable, if there no assignment
[L1153] [42:59.08] works
[L1154] [43:00.36] we're saying for all assignments
[L1155] [43:02.80] the formula is not true. Can you flip
[L1156] [43:04.44] that to an existential statement and
[L1157] [43:06.64] say, "Oh, there exists this little proof
[L1158] [43:08.96] makes it work." So
[L1159] [43:10.44] people don't believe that NP is equal to
[L1160] [43:13.88] co-NP
[L1161] [43:15.40] and in fact like NP different from co-NP
[L1162] [43:19.24] implies P different from NP.
[L1163] [43:21.36] Um
[L1164] [43:22.16] But so this is the exponential time
[L1165] [43:24.08] version
[L1166] [43:25.56] of NP versus co-NP. So it's co-NEX
[L1167] [43:29.84] uh
[L1168] [43:30.40] versus NEX.
[L1169] [43:32.32] The reason why I think
[L1170] [43:35.24] these are likely to be equal
[L1171] [43:38.00] is that
[L1172] [43:39.72] if a little birdie
[L1173] [43:41.72] sat on an NEX machine's shoulder and
[L1174] [43:44.72] gave it a little bit of advice
[L1175] [43:47.20] about what the co-NEX thing is doing
[L1176] [43:50.84] then
[L1177] [43:51.88] the an NEX
[L1178] [43:53.80] uh algorithm
[L1179] [43:55.28] can actually solve co-NEX problems.
[L1180] [43:58.36] And so let let me explain
[L1181] [44:00.16] uh let me explain why Yeah, what's the
[L1182] [44:01.52] little birdie What the heck is the
[L1183] [44:02.76] little birdie saying? So
[L1184] [44:04.80] because NEX problems can run in 2 to the
[L1185] [44:07.92] end time and two to the N squared time
[L1186] [44:10.32] and things like that.
[L1187] [44:12.04] Running an exhaustive search over all
[L1188] [44:14.56] possible inputs of length N is no
[L1189] [44:16.72] problem
[L1190] [44:17.88] for NX.
[L1191] [44:19.08] So, what a little birdie can do is say,
[L1192] [44:21.76] "Okay, suppose um
[L1193] [44:24.52] like I want to verify that
[L1194] [44:27.88] this particular
[L1195] [44:30.04] um instance
[L1196] [44:32.36] like let's say let we can talk about
[L1197] [44:33.88] like an unsat but like the you know some
[L1198] [44:36.04] compressible unsat problem or something.
[L1199] [44:38.40] Suppose I want to prove that this
[L1200] [44:39.56] compressible unsat instance
[L1201] [44:42.44] um
[L1202] [44:43.04] is a yes. Okay? How am I going to do
[L1203] [44:45.32] that uh
[L1204] [44:47.16] with NX?
[L1205] [44:48.56] The little birdie will tell me
[L1206] [44:51.12] the total number of inputs of length N
[L1207] [44:54.04] which are a yes.
[L1208] [44:56.60] Okay?
[L1209] [44:57.56] So, it it will it will just tell me some
[L1210] [44:59.64] string which says, "Here's the total
[L1211] [45:01.52] number of inputs of length N. You gave
[L1212] [45:03.60] me a length N input. Here's the total
[L1213] [45:05.24] number of inputs of length N
[L1214] [45:07.96] uh
[L1215] [45:08.56] that are a yes. Okay?
[L1216] [45:11.40] Okay? So,
[L1217] [45:13.84] um this this advice this little you know
[L1218] [45:18.08] birdie's advice doesn't take very much
[L1219] [45:20.36] like to encode a count. It's like order
[L1220] [45:22.80] N bits to encode a count uh of things.
[L1221] [45:26.60] So,
[L1222] [45:27.96] um so, what does the NX thing do to
[L1223] [45:31.12] prove a co-NX thing? What it does is it
[L1224] [45:33.88] guesses
[L1225] [45:35.56] the things which are a no.
[L1226] [45:38.04] So, I'm trying to prove unsat. So, unsat
[L1227] [45:40.16] means yes, sat means no.
[L1228] [45:42.64] So, the NX thing guesses those things
[L1229] [45:44.96] which are no.
[L1230] [45:46.16] The no things it can answer, right? If
[L1231] [45:48.28] it's a sat thing, it can just guess the
[L1232] [45:50.40] answer to each of the nos.
[L1233] [45:53.36] Okay?
[L1234] [45:54.44] So, it guesses the answer to each of the
[L1235] [45:56.36] nos. It verifies all those answers, and
[L1236] [45:59.40] then it checks that the number of things
[L1237] [46:01.64] it guessed is what the birdie told it.
[L1238] [46:04.88] Once it's done that, all the no's have
[L1239] [46:08.12] been covered, so everything else must be
[L1240] [46:10.88] a yes.
[L1241] [46:12.36] So that so so it can actually prove a
[L1242] [46:14.88] yes by just exhaustively finding all the
[L1243] [46:18.24] no's and ruling out any other no's.
[L1244] [46:21.72] >> But the big question in my mind is where
[L1245] [46:23.92] do you get the little birdie?
[L1246] [46:24.84] >> Where do you get the little birdie
[L1247] [46:25.68] advice from? Yeah, yeah. So
[L1248] [46:27.84] yeah, so this I studied yeah, this um
[L1249] [46:31.52] what the little birdie gives you
[L1250] [46:33.76] and it seems to me that it it is
[L1251] [46:36.56] possible that this little birdie itself
[L1252] [46:39.96] can be constructed in NX.
[L1253] [46:42.64] And if so, then we'd just be done. Like
[L1254] [46:45.20] in NX, you figure out what the little
[L1255] [46:47.28] birdie would tell you and then use that
[L1256] [46:49.72] to just flip the answer. So it guess
[L1257] [46:53.04] Let's sort of guess all the things which
[L1258] [46:55.00] are no, so what remains must be a yes
[L1259] [46:57.12] and
[L1260] [46:58.64] we talked a lot about time
[L1261] [47:00.00] >> complexity. And you mentioned a little
[L1262] [47:01.96] bit this advice I guess kind of space
[L1263] [47:03.56] complexity. And I know you had a major
[L1264] [47:06.12] result relating space and time
[L1265] [47:08.76] complexity. You're basically simulating
[L1266] [47:11.40] time complexity with space complexity,
[L1267] [47:13.84] but lower than it's been done prior.
[L1268] [47:17.12] Could you explain
[L1269] [47:19.12] what it was before your breakthrough
[L1270] [47:21.32] result and then maybe the intuition
[L1271] [47:23.40] behind your breakthrough result?
[L1272] [47:25.32] >> Uh in general, the problem is the
[L1273] [47:27.56] following. I give you
[L1274] [47:29.92] an algorithm that runs in time T
[L1275] [47:33.16] and I want to know
[L1276] [47:35.64] um is there another algorithm that uses
[L1277] [47:38.24] space much less than T? Uses amount of
[L1278] [47:41.64] memory like you know, units of memory
[L1279] [47:43.60] much less
[L1280] [47:44.92] than T
[L1281] [47:46.36] and still solve the problem completely.
[L1282] [47:48.72] Still completely simulates the thing
[L1283] [47:50.60] perfectly.
[L1284] [47:52.00] Um
[L1285] [47:53.56] one intuition for why you
[L1286] [47:56.76] might think um
[L1287] [47:58.84] this
[L1288] [47:59.68] question just
[L1289] [48:01.04] can't be solved or some problems there's
[L1290] [48:02.28] just no
[L1291] [48:03.64] way to improve on the spaces if you
[L1292] [48:05.96] think of like
[L1293] [48:07.60] the pro like a lot of problems in
[L1294] [48:09.16] dynamic programming like let's say I
[L1295] [48:11.88] have
[L1296] [48:13.56] um
[L1297] [48:14.36] some logic circuit that I want to
[L1298] [48:16.32] evaluate and all of the gates are
[L1299] [48:18.92] provided to me in a row and all the
[L1300] [48:22.20] wires sort of flow from left to right.
[L1301] [48:25.32] And the you know I start with
[L1302] [48:26.36] information on the left.
[L1303] [48:28.56] I want to compute the information on the
[L1304] [48:31.04] far right.
[L1305] [48:32.44] And all the you know all the bits are
[L1306] [48:33.92] flowing left to right by wires.
[L1307] [48:36.64] The natural way to evaluate such a
[L1308] [48:38.84] circuit is you start with say the inputs
[L1309] [48:40.60] on the left.
[L1310] [48:41.92] For each gate in turn in the the line
[L1311] [48:45.68] you look at its inputs. Its inputs have
[L1312] [48:47.76] been determined if there's some bits.
[L1313] [48:50.04] You use that to compute the value of
[L1314] [48:51.96] that gate. You pass the values of that
[L1315] [48:55.12] of you know the output of that gate
[L1316] [48:56.48] forward.
[L1317] [48:57.40] Okay?
[L1318] [48:58.60] But if
[L1319] [48:59.80] that uh circuit you know has
[L1320] [49:02.88] T gates in it you know it will take
[L1321] [49:04.60] about T time to solve but it will
[L1322] [49:06.72] definitely also take about T space in
[L1323] [49:08.88] general.
[L1324] [49:10.00] All right? Like the circuit could be
[L1325] [49:11.60] wired up in some wild way and there just
[L1326] [49:14.28] might not be a way to save uh space for
[L1327] [49:16.96] an arbitrary uh circuit.
[L1328] [49:19.44] But already in 1975
[L1329] [49:25.24] people were studying this kind of of
[L1330] [49:27.08] question and finding counterintuitive
[L1331] [49:29.76] answers to it.
[L1332] [49:31.28] So
[L1333] [49:31.96] um Hopcroft, Paul, and Valiant uh based
[L1334] [49:35.20] on work of Patterson and Valiant
[L1335] [49:38.24] uh showed that
[L1336] [49:41.00] time T algorithms at least in this
[L1337] [49:43.84] so-called multi-tape Turing machine uh
[L1338] [49:46.24] model very powerful model uh can be
[L1339] [49:49.28] simulated in space T divided by log of
[L1340] [49:52.80] T. So I mean it's like a like you you
[L1341] [49:56.08] get some space savings but it's only
[L1342] [49:57.84] like a log T factor. Okay.
[L1343] [50:00.52] Um
[L1344] [50:01.92] and
[L1345] [50:03.20] the way this is done is is quite
[L1346] [50:06.80] counterintuitive. Uh it was I mean like
[L1347] [50:10.00] even though there's a only a log factor
[L1348] [50:12.12] there it was
[L1349] [50:13.20] uh
[L1350] [50:13.84] pretty shocking.
[L1351] [50:15.76] That development was
[L1352] [50:18.16] extended to random access models of
[L1353] [50:20.76] computation
[L1354] [50:22.24] um later
[L1355] [50:24.08] and and in more general models of
[L1356] [50:26.84] computation. So like in in the late '70s
[L1357] [50:29.44] and early '80s.
[L1358] [50:30.84] Um
[L1359] [50:32.08] so so it was known for like a pretty
[L1360] [50:35.40] much any reasonable model of computation
[L1361] [50:37.28] that time T can be simulated in space
[L1362] [50:40.12] about T over log T.
[L1363] [50:42.28] But there was a hidden maybe not so
[L1364] [50:45.00] hidden um gotcha in the space efficient
[L1365] [50:48.68] simulation. It needs
[L1366] [50:51.12] an exponential amount of time
[L1367] [50:53.20] to run. So like you there's a time space
[L1368] [50:55.56] trade-off. Okay, if you really want to
[L1369] [50:57.20] save some space you got to blow up the
[L1370] [50:59.44] time by a lot.
[L1371] [51:02.04] Nevertheless
[L1372] [51:03.48] um yeah, it was kind of commonly
[L1373] [51:06.12] conjectured that
[L1374] [51:08.60] this T over log T space was about the
[L1375] [51:11.96] best you could do and you
[L1376] [51:14.16] and that you were probably not going to
[L1377] [51:16.24] get T to the 0.9
[L1378] [51:19.68] space or you know something something
[L1379] [51:22.28] much more efficient. Um
[L1380] [51:25.36] so yeah, it was a big surprise to me uh
[L1381] [51:29.84] like that you can actually put time T in
[L1382] [51:33.08] space about square root
[L1383] [51:35.64] of T.
[L1384] [51:36.80] Again, there's an exponential
[L1385] [51:38.92] running time just to you know give the
[L1386] [51:41.20] full caveat out there.
[L1387] [51:43.28] But
[L1388] [51:44.52] um
[L1389] [51:45.28] but it's still very surprising. Like
[L1390] [51:47.16] this holds for
[L1391] [51:48.88] any kind of time T
[L1392] [51:51.16] uh algorithm. Like, including something
[L1393] [51:52.48] that might be outputting, you know,
[L1394] [51:54.56] something pseudo random, some you know,
[L1395] [51:57.40] something from cryptography,
[L1396] [51:59.60] you know, like it's not at all obvious
[L1397] [52:01.80] that every such process could be
[L1398] [52:04.28] compressed
[L1399] [52:05.76] to only be need like square root of T
[L1400] [52:09.04] uh space and still get the job done,
[L1401] [52:10.76] still compute whatever function was
[L1402] [52:12.96] being computed.
[L1403] [52:14.12] >> I mean, I know it's probably super
[L1404] [52:15.48] involved, but if you could just a high
[L1405] [52:17.64] level, what's the trick? How'd you do
[L1406] [52:19.16] it?
[L1407] [52:19.48] >> Well, the trick for me was to read
[L1408] [52:23.00] um James Cook and Ian Mertz's paper on
[L1409] [52:26.20] tree evaluation very, very carefully.
[L1410] [52:28.40] That
[L1411] [52:29.36] I mean, and just knowing um the P the
[L1412] [52:33.84] landscape around P versus P space and
[L1413] [52:35.84] knowing what Hopcroft, Paul, and Valiant
[L1414] [52:38.36] did. Um
[L1415] [52:41.12] Yeah, so but I I can give you a very
[L1416] [52:43.52] high-level idea of
[L1417] [52:46.32] kind of what's going on and how what
[L1418] [52:49.68] they did uh is useful.
[L1419] [52:52.44] So,
[L1420] [52:54.04] Hopcroft, Paul, and Valiant, the way
[L1421] [52:55.64] they were modeling
[L1422] [52:57.48] uh space-bounded computation was in a
[L1423] [52:59.96] particular way that seemed pretty
[L1424] [53:01.60] general uh at the time, but turned out
[L1425] [53:05.12] to be restrictive
[L1426] [53:07.20] uh
[L1427] [53:08.32] in ways that we just didn't anticipate.
[L1428] [53:10.48] So, the way they thought of it was
[L1429] [53:14.52] um I'm going to take like certain I'm
[L1430] [53:17.28] going to break the computation up into
[L1431] [53:18.52] little pieces
[L1432] [53:20.16] and I'm going to
[L1433] [53:23.80] like write I'm going to write pieces of
[L1434] [53:27.52] the computation like little bits into
[L1435] [53:29.56] the memory, but I'm only going to do
[L1436] [53:31.20] that over blank space. I mean, this is
[L1437] [53:33.64] something that sounds natural, right?
[L1438] [53:35.00] Like, so like I'm going to erase pieces
[L1439] [53:38.48] of memory and then I'm going to
[L1440] [53:40.20] overwrite that blank space with a piece
[L1441] [53:42.92] of memory. So, I'm being very
[L1442] [53:44.32] destructive in a certain sense. Like but
[L1443] [53:47.04] this is a natural thing you do, right?
[L1444] [53:48.68] Like if you want to replace you know,
[L1445] [53:50.76] swap something with something else,
[L1446] [53:53.52] you often just erase. But there are ways
[L1447] [53:57.00] to swap
[L1448] [53:58.56] without uh erasing, right? So, there's
[L1449] [54:01.68] like a common
[L1450] [54:03.24] little trick that is taught in uh CS
[L1451] [54:06.04] courses.
[L1452] [54:07.12] So, like if you
[L1453] [54:08.72] um if you require everything to be
[L1454] [54:11.44] written into a blank uh
[L1455] [54:14.04] register,
[L1456] [54:15.36] then if you want to swap the contents of
[L1457] [54:17.68] two variables like X and Y,
[L1458] [54:20.16] then you've
[L1459] [54:21.32] you've got to have a temporary register.
[L1460] [54:23.12] Like you move one into the temp, you
[L1461] [54:25.12] erase it, you move Y into the
[L1462] [54:27.52] into there and then so on, right?
[L1463] [54:29.72] But if you don't want a temp, you can
[L1464] [54:33.04] achieve the same thing uh with just
[L1465] [54:36.56] XORing the the registers bitwise. Or if
[L1466] [54:39.88] you've got numbers, you can add and
[L1467] [54:41.36] subtract, okay? In three instructions,
[L1468] [54:44.92] clever instructions, adding,
[L1469] [54:46.36] subtracting, or XORing,
[L1470] [54:48.44] you can actually swap the contents of
[L1471] [54:50.48] two registers without needing a third.
[L1472] [54:53.92] Okay? This is kind of the starting point
[L1473] [54:56.12] for thinking about like, well, why does
[L1474] [54:57.96] it matter
[L1475] [54:59.48] if you're always writing into erased
[L1476] [55:02.40] memory?
[L1477] [55:03.60] So,
[L1478] [55:04.56] so what
[L1479] [55:05.80] uh
[L1480] [55:06.44] James Cook and Ian Mertz showed
[L1481] [55:09.68] uh at a very high level was
[L1482] [55:12.08] they they were studying a certain
[L1483] [55:14.44] problem
[L1484] [55:15.88] called tree evaluation, whatever that
[L1485] [55:18.00] is,
[L1486] [55:18.92] and they were the problem had an
[L1487] [55:21.36] algorithm where you're all you had a
[L1488] [55:24.32] little stack
[L1489] [55:25.68] and you're always sort of like
[L1490] [55:29.20] um you know,
[L1491] [55:30.52] popping and and uh pushing on the stack,
[L1492] [55:33.52] but you were always, you know, writing
[L1493] [55:36.32] uh
[L1494] [55:37.80] writing computation contents into erase
[L1495] [55:41.72] memory, okay? What they realized was
[L1496] [55:44.28] that if you allow computations to XOR
[L1497] [55:48.44] bits of memory into existing memory,
[L1498] [55:51.12] then you can save a lot of space.
[L1499] [55:53.56] So, if you're really, really careful
[L1500] [55:56.48] about how you XOR things, you can
[L1501] [55:59.40] basically recover uh you like what's in
[L1502] [56:03.00] your memory without storing all of it at
[L1503] [56:05.24] once. You sort of offload things to
[L1504] [56:07.44] computation,
[L1505] [56:09.00] and you XOR on top of things very, very
[L1506] [56:11.76] cleverly. You can get like nice
[L1507] [56:13.52] cancellations of things you don't want,
[L1508] [56:16.20] and and keep around things you do want.
[L1509] [56:18.92] Yeah, so
[L1510] [56:20.36] I mean, that is a high-level uh idea of
[L1511] [56:23.56] how this stuff works. And then going to
[L1512] [56:25.60] square root, is it just an extension of
[L1513] [56:27.80] that, or is it a completely different?
[L1514] [56:29.48] So, the the way it works with square
[L1515] [56:30.92] root, a square root just happens to be
[L1516] [56:32.52] kind of like the optimal trade-off
[L1517] [56:35.48] in this uh tree evaluation business. So,
[L1518] [56:39.24] so
[L1519] [56:40.80] um what you do is you break the
[L1520] [56:42.32] computation into square root of T time
[L1521] [56:45.60] intervals,
[L1522] [56:46.84] and each time interval has about square
[L1523] [56:48.44] root of T
[L1524] [56:49.76] um steps in it.
[L1525] [56:52.48] And then what you do is you you give a a
[L1526] [56:54.52] particular way of simulating this thing,
[L1527] [56:58.96] so that you're only kind of holding
[L1528] [57:01.36] about a constant number
[L1529] [57:04.00] of blocks or like of these time
[L1530] [57:06.28] intervals in memory at any point in
[L1531] [57:08.24] time.
[L1532] [57:09.20] Like you're only holding a small number
[L1533] [57:11.60] of these
[L1534] [57:13.08] uh
[L1535] [57:13.68] time intervals, like a records of time
[L1536] [57:15.92] intervals in memory at any any point in
[L1537] [57:18.28] time.
[L1538] [57:19.24] Which is entirely not obvious how you
[L1539] [57:21.64] would do it. But but it's some sort of
[L1540] [57:23.96] like it's some sort of sweet spot to set
[L1541] [57:26.32] the square root of T. It's a way to It's
[L1542] [57:27.84] like the
[L1543] [57:28.76] the minimum setting of like trade-off.
[L1544] [57:31.00] Like say I have like
[L1545] [57:32.68] I want to break the computational
[L1546] [57:34.16] intervals, and the intervals have a
[L1547] [57:36.44] certain number of steps. If I If I set
[L1548] [57:38.32] it to be square root of T, then the
[L1549] [57:39.92] number of intervals and the number of
[L1550] [57:41.64] steps in each interval is about the
[L1551] [57:43.36] same.
[L1552] [57:44.64] >> So, I mean, that was a long-held result.
[L1553] [57:47.28] I mean, you you mentioned it was 1975.
[L1554] [57:49.72] That's maybe Yeah, almost 50 years where
[L1555] [57:52.88] if you come up with something like that
[L1556] [57:54.44] and you you I guess you're writing it
[L1557] [57:56.32] out, you're thinking through, and then
[L1558] [57:58.04] you see it. What is that moment like?
[L1559] [58:00.60] >> So, I you know, I'm I've been around
[L1560] [58:02.68] long enough to have been deceived by
[L1561] [58:05.36] myself many many many many times.
[L1562] [58:09.16] So,
[L1563] [58:10.36] yeah, I guess the the first two or three
[L1564] [58:12.72] times I thought about this,
[L1565] [58:16.32] um
[L1566] [58:17.08] I just thought this is another one of
[L1567] [58:18.60] those ideas that can't possibly work.
[L1568] [58:21.80] There's no way. There's just no way this
[L1569] [58:23.36] works.
[L1570] [58:24.28] Um
[L1571] [58:26.08] so, I would just kind of leave it
[L1572] [58:28.72] and then come back to it sometimes when
[L1573] [58:30.40] I was
[L1574] [58:32.20] bored of whatever else I was working on.
[L1575] [58:34.32] Um
[L1576] [58:35.36] like I I It was a pretty slow process of
[L1577] [58:38.44] convincing myself that this could
[L1578] [58:40.40] possibly be true. Like, I
[L1579] [58:42.80] I thought there was
[L1580] [58:45.16] either a bug in what
[L1581] [58:49.08] James and Ian
[L1582] [58:50.72] was doing somewhere,
[L1583] [58:52.92] or there was a bug in
[L1584] [58:55.52] my interpretation of what's happening.
[L1585] [58:58.36] Um I thought
[L1586] [59:00.16] there had to be a mistake for a long
[L1587] [59:02.32] time.
[L1588] [59:03.60] And the only way I got over that was
[L1589] [59:05.52] just
[L1590] [59:06.64] writing it down
[L1591] [59:08.64] uh over and over and over in different
[L1592] [59:10.80] ways, sort of writing and rewriting and
[L1593] [59:13.04] writing and rewriting and adding more
[L1594] [59:14.68] detail,
[L1595] [59:15.96] and then maybe finding a different way
[L1596] [59:17.40] of explaining it and it erasing and, you
[L1597] [59:20.64] know, writing something shorter,
[L1598] [59:22.48] and just sort of re-explaining it to
[L1599] [59:24.04] myself over and over and over.
[L1600] [59:27.00] And even then, like when I submitted it
[L1601] [59:28.80] to the
[L1602] [59:29.92] um stock conference where it was where
[L1603] [59:32.64] it appeared, um I wasn't entirely
[L1604] [59:36.04] confident that it was correct. I was
[L1605] [59:38.20] just exhausted from like thinking about
[L1606] [59:40.72] it for so long and just thought that
[L1607] [59:42.44] maybe someone else will find the mistake
[L1608] [59:44.32] for me. Like I'm Like I Like I At this
[L1609] [59:46.56] point, like
[L1610] [59:47.84] I I was just like desperate. Like I had
[L1611] [59:50.12] actually sent it
[L1612] [59:51.72] to two
[L1613] [59:53.20] colleagues that I trust,
[L1614] [59:55.44] you know, privately and asked them,
[L1615] [59:58.48] "Can you help me find the mistake?" Or
[L1616] [01:00:01.24] whatever. "Can you help me understand
[L1617] [01:00:02.76] this?" And one of them just said, like
[L1618] [01:00:05.76] they Basically, they just didn't read
[L1619] [01:00:07.60] past the abstract. They're like, "I'm
[L1620] [01:00:09.52] not I'm sorry. I'm not going to
[L1621] [01:00:12.92] I'm like they just didn't believe it,
[L1622] [01:00:14.40] period. Just like me. I mean, they
[L1623] [01:00:15.92] didn't believe it.
[L1624] [01:00:17.24] And
[L1625] [01:00:18.68] uh another one said,
[L1626] [01:00:21.60] after a long time, "Well,
[L1627] [01:00:24.80] I didn't quite
[L1628] [01:00:26.52] um
[L1629] [01:00:27.08] follow it, but
[L1630] [01:00:28.64] there was a footnote that you put
[L1631] [01:00:31.56] like in in the bottom of some page.
[L1632] [01:00:34.04] After that after that footnote,
[L1633] [01:00:36.68] then I began to believe it."
[L1634] [01:00:39.52] So then what I did was I just took that
[L1635] [01:00:41.00] footnote and elaborated it in in like a
[L1636] [01:00:43.80] later revision, sort of made it the what
[L1637] [01:00:45.64] I called the warm-up. I'm going to
[L1638] [01:00:47.28] because I was like, yeah, I I've got to
[L1639] [01:00:49.28] do I've got to write this thing in a way
[L1640] [01:00:52.36] that is airtight so that other people
[L1641] [01:00:54.28] will actually believe believe this
[L1642] [01:00:56.68] because
[L1643] [01:00:58.08] yeah, I it took me a long time to get
[L1644] [01:01:00.56] used to it, to believe it. Yeah.
[L1645] [01:01:02.04] >> Wow. Uh what What motivates you to solve
[L1646] [01:01:06.00] these
[L1647] [01:01:07.04] hard problems? I mean, what keeps you
[L1648] [01:01:10.44] driven? Cuz you kind of sounds like you
[L1649] [01:01:13.60] got to just bash your head against the
[L1650] [01:01:15.56] wall and
[L1651] [01:01:17.96] maybe you get there, maybe you don't.
[L1652] [01:01:20.76] >> I try not to bash my head against the
[L1653] [01:01:24.16] wall. Um and if I'm going to do it,
[L1654] [01:01:27.84] it's going to be, you know, a
[L1655] [01:01:29.72] comfortable wall. It's going to be, you
[L1656] [01:01:32.08] know, when it's like
[L1657] [01:01:33.92] high-end and luxurious or something.
[L1658] [01:01:36.68] Like I'm going to enjoy
[L1659] [01:01:39.52] uh the process is what I mean. Like if
[L1660] [01:01:43.00] if I don't enjoy the process of really
[L1661] [01:01:47.60] grinding and trying to understand
[L1662] [01:01:49.04] something,
[L1663] [01:01:50.44] I'm just I'm not going to do it. Like uh
[L1664] [01:01:52.68] So, I think that
[L1665] [01:01:54.80] if, you know, if anything is
[L1666] [01:01:56.80] uh one thing that I that I like I I like
[L1667] [01:01:59.68] to involve myself in
[L1668] [01:02:01.60] working on problems where
[L1669] [01:02:03.56] the the grind is actually joyous and and
[L1670] [01:02:07.12] fun. Yeah. Um for the other things, uh
[L1671] [01:02:11.12] they're just they're mainly
[L1672] [01:02:12.20] opportunistic. They're mainly me just
[L1673] [01:02:15.36] taking something that new that I see and
[L1674] [01:02:18.60] just fully integrating it with
[L1675] [01:02:20.48] everything I know and following
[L1676] [01:02:22.08] everything to the logical conclusion.
[L1677] [01:02:24.80] And just seeing what happens. Like and
[L1678] [01:02:26.68] not not trying not to get emotional,
[L1679] [01:02:28.68] trying not to whatever, just trying to
[L1680] [01:02:30.96] follow everything one step after
[L1681] [01:02:33.72] another. Yeah.
[L1682] [01:02:35.32] How do you pick good research direction?
[L1683] [01:02:38.00] The best kind of research direction,
[L1684] [01:02:40.28] which is very hard to um
[L1685] [01:02:43.32] it's very hard to come across,
[L1686] [01:02:45.60] is a direction where you
[L1687] [01:02:48.16] you've set yourself up in a way that you
[L1688] [01:02:49.68] can't lose.
[L1689] [01:02:51.12] That like I have a hypothesis
[L1690] [01:02:54.28] H
[L1691] [01:02:55.40] and one of two things is going to
[L1692] [01:02:57.56] happen. Like either I
[L1693] [01:02:59.60] prove H is true
[L1694] [01:03:01.44] or I refute H, prove not H. What I would
[L1695] [01:03:04.92] like to have is a situation where
[L1696] [01:03:09.08] um if H is true,
[L1697] [01:03:11.36] then good things happen. If not H is
[L1698] [01:03:13.68] true,
[L1699] [01:03:15.08] good things still happen. Other other
[L1700] [01:03:16.84] good things. Like um the I like I like
[L1701] [01:03:20.20] to look at things where Yeah, it's a
[L1702] [01:03:23.04] win-win.
[L1703] [01:03:24.24] Kind of if if you can
[L1704] [01:03:27.12] find opportunities like this, this is
[L1705] [01:03:29.60] important. Like I think often I'm not
[L1706] [01:03:33.76] looking at a specific uh problem.
[L1707] [01:03:37.16] I'm looking at a method. I'm looking at
[L1708] [01:03:40.80] the technique.
[L1709] [01:03:42.40] You know, I'm looking at not the
[L1710] [01:03:43.44] specific proof, but like like the space
[L1711] [01:03:46.68] of ideas, and I'm trying to understand
[L1712] [01:03:49.48] what else can be done in the space of
[L1713] [01:03:51.48] ideas.
[L1714] [01:03:52.92] Like so so often I solve problems just
[L1715] [01:03:55.64] by by just taking some idea and putting
[L1716] [01:03:58.28] it somewhere somewhere else.
[L1717] [01:03:59.88] >> Do you have a concrete example of where
[L1718] [01:04:02.20] you you've pursued something knowing
[L1719] [01:04:04.04] that if you succeed, good. If you
[L1720] [01:04:07.48] succeed in other direction, also good.
[L1721] [01:04:09.80] >> I have some particular research program
[L1722] [01:04:13.76] for which if it materializes, would
[L1723] [01:04:16.80] actually
[L1724] [01:04:18.16] show that something called the
[L1725] [01:04:19.56] orthogonal vectors problem
[L1726] [01:04:21.80] can be solved in nearly linear time.
[L1727] [01:04:24.00] Okay? Now,
[L1728] [01:04:26.04] this um
[L1729] [01:04:27.60] Now, if that's true, then the SAT
[L1730] [01:04:30.48] problem can be solved
[L1731] [01:04:32.44] in about the same time as subset sum. It
[L1732] [01:04:35.04] could be solved in like square root of 2
[L1733] [01:04:36.60] the n. So, this would like
[L1734] [01:04:38.88] truly break uh strong ETH in like a
[L1735] [01:04:42.12] radical way. Okay?
[L1736] [01:04:44.52] And
[L1737] [01:04:46.04] um
[L1738] [01:04:46.68] I did a lot of work uh in the past
[L1739] [01:04:49.72] showing how if
[L1740] [01:04:52.44] uh you can improve on the running time
[L1741] [01:04:55.60] of SAT,
[L1742] [01:04:56.88] then you can somehow use that
[L1743] [01:04:59.48] to prove circuit complexity lower
[L1744] [01:05:01.56] bounds. You can take an algorithm for
[L1745] [01:05:04.24] analyzing circuits
[L1746] [01:05:06.28] that's non-trivial and interesting and
[L1747] [01:05:09.36] turn that into a limitation on what
[L1748] [01:05:12.20] those circuits can compute. Okay?
[L1749] [01:05:15.44] So
[L1750] [01:05:16.52] So this hypothesis
[L1751] [01:05:18.64] Let me Maybe maybe I won't exactly say
[L1752] [01:05:20.96] what it is. It's It's a pretty
[L1753] [01:05:23.16] technical statement, but the point is
[L1754] [01:05:25.04] that if the hypothesis is true
[L1755] [01:05:28.96] then I get this fantastic algorithm for
[L1756] [01:05:32.32] this orthogonal vectors problem. I get
[L1757] [01:05:34.72] this algorithm for SAT. I get circuit
[L1758] [01:05:36.96] complexity lower bounds from that. I get
[L1759] [01:05:38.96] to somehow prove limitations on what
[L1760] [01:05:40.92] circuits can do.
[L1761] [01:05:43.04] If the hypothesis is false
[L1762] [01:05:45.52] I can use that hypothesis to actually
[L1763] [01:05:47.44] show another circuit complexity lower
[L1764] [01:05:50.32] bound of a different flavor.
[L1765] [01:05:53.20] So So regardless of whether or not like
[L1766] [01:05:56.16] the hypothesis is true or false, like
[L1767] [01:05:57.92] I'm going to make progress in complexity
[L1768] [01:05:59.80] theory. I'm going to prove a new
[L1769] [01:06:01.00] limitation one way or the other.
[L1770] [01:06:04.48] Right? So
[L1771] [01:06:05.92] it So sometimes like I mean this can be
[L1772] [01:06:08.96] difficult to do, but um
[L1773] [01:06:13.28] usually what has happened instead of
[L1774] [01:06:14.88] something so clean
[L1775] [01:06:16.52] is that I have
[L1776] [01:06:18.32] I I read about some idea
[L1777] [01:06:21.04] or whatever. I try to apply the idea. I
[L1778] [01:06:23.52] read about some magical algorithm. I try
[L1779] [01:06:25.88] to apply the magical algorithm to solve
[L1780] [01:06:27.60] something like SAT.
[L1781] [01:06:29.44] It doesn't work. But I look at my
[L1782] [01:06:32.20] approach. I stare really hard at it. I
[L1783] [01:06:34.12] try to pivot. You know, I try to
[L1784] [01:06:36.56] just extract what I can, and then I get
[L1785] [01:06:38.68] some other type of algorithm.
[L1786] [01:06:41.36] Right? I mean, this is essentially how I
[L1787] [01:06:43.32] proved
[L1788] [01:06:44.92] um
[L1789] [01:06:46.16] like the circuit complexity lower bounds
[L1790] [01:06:47.72] that that first got me a job at Stanford
[L1791] [01:06:50.68] was I was trying to solve SAT faster
[L1792] [01:06:54.08] with some algorithm. It didn't work, but
[L1793] [01:06:56.20] then I realized that that algorithm
[L1794] [01:06:58.24] worked for a large class of circuits,
[L1795] [01:07:00.32] including ones we didn't know lower
[L1796] [01:07:01.72] bounds for.
[L1797] [01:07:02.92] So then I used that to prove
[L1798] [01:07:04.84] a lower a lower bounds.
[L1799] [01:07:07.08] Yeah. so I mean
[L1800] [01:07:08.92] um this is just a general principle that
[L1801] [01:07:12.52] that I've had.
[L1802] [01:07:13.72] >> What would be your book recommendation
[L1803] [01:07:15.84] if someone wants to learn more on
[L1804] [01:07:18.08] complexity theory?
[L1805] [01:07:19.32] >> Yeah, so it sort of depends on how deep
[L1806] [01:07:21.84] uh
[L1807] [01:07:22.60] you want to go. There's Avi's book.
[L1808] [01:07:25.56] Yeah, Avi's book is really nice. If
[L1809] [01:07:27.72] you're looking for something a little
[L1810] [01:07:29.28] more gentle of an introduction,
[L1811] [01:07:31.96] um
[L1812] [01:07:33.08] I would say like you could read the
[L1813] [01:07:34.68] early chapters of Lance Fortnow's uh The
[L1814] [01:07:37.84] Golden Ticket.
[L1815] [01:07:39.40] Like trying to imagine what a world
[L1816] [01:07:41.84] would be like if P equaled NP.
[L1817] [01:07:44.52] Um I it I I like that imagination
[L1818] [01:07:48.20] exercise that that Lance uh
[L1819] [01:07:50.96] did.
[L1820] [01:07:52.92] On a more technical level, you know, if
[L1821] [01:07:55.28] you're looking um
[L1822] [01:07:57.16] for something slightly more technical,
[L1823] [01:07:59.72] you could look at The Nature of
[L1824] [01:08:01.32] Computation by um Mertens and Moore,
[L1825] [01:08:05.36] I think. So, this is
[L1826] [01:08:06.88] this is
[L1827] [01:08:07.88] still
[L1828] [01:08:09.12] uh not, you know, very technical, but
[L1829] [01:08:13.12] um but a lot but it is a textbook,
[L1830] [01:08:15.44] right? Yeah, um
[L1831] [01:08:17.96] and then of course
[L1832] [01:08:19.96] uh
[L1833] [01:08:20.68] Sipser's uh Introduction to the Theory
[L1834] [01:08:23.08] of Computation is like
[L1835] [01:08:25.32] um a fairly concise and very
[L1836] [01:08:28.48] well-written uh textbook. Yeah.
[L1837] [01:08:32.12] >> Last question for you is if you could go
[L1838] [01:08:33.84] back to the beginning of your career
[L1839] [01:08:35.32] knowing what you know now, what advice
[L1840] [01:08:37.44] would you give yourself?
[L1841] [01:08:38.72] >> So, I guess like one thing that I did
[L1842] [01:08:42.44] um by accident, I guess, uh which I
[L1843] [01:08:45.48] think
[L1844] [01:08:46.76] uh people
[L1845] [01:08:48.52] should keep in mind is that you don't
[L1846] [01:08:50.84] need uh permission
[L1847] [01:08:53.12] to work on very tough problems. Like
[L1848] [01:08:56.52] in fact, the tougher the problem, like
[L1849] [01:08:59.32] in complexity theory, there are all
[L1850] [01:09:00.48] these problems where
[L1851] [01:09:02.16] like, really nobody
[L1852] [01:09:04.12] has a very good clue of what to do
[L1853] [01:09:06.68] beyond like a few
[L1854] [01:09:09.04] simple structural results. Like,
[L1855] [01:09:12.08] so that kind of levels the playing field
[L1856] [01:09:14.60] a bit and
[L1857] [01:09:15.92] yeah, like you just you don't need
[L1858] [01:09:17.80] permission to think about these
[L1859] [01:09:19.48] problems. You don't need like, you know,
[L1860] [01:09:21.08] anybody's uh say-so or whatever.
[L1861] [01:09:24.04] Um
[L1862] [01:09:25.32] I mean, that's that's one thing that I
[L1863] [01:09:27.16] would would like younger people uh to
[L1864] [01:09:29.44] keep in mind that I mean, this knowledge
[L1865] [01:09:32.72] is open to the world and it's open to
[L1866] [01:09:34.44] you and and you can just go learn it and
[L1867] [01:09:37.12] think about it and
[L1868] [01:09:38.80] you don't Yeah, you don't need any
[L1869] [01:09:40.44] anybody's permission, especially not
[L1870] [01:09:41.92] mine. Um
[L1871] [01:09:44.08] Yeah, like
[L1872] [01:09:45.60] um another thing
[L1873] [01:09:48.40] I think is uh to avoid inertia
[L1874] [01:09:53.04] in the sense that like, you know, if you
[L1875] [01:09:55.84] if you don't think about
[L1876] [01:09:58.60] and reflect like, where am I going
[L1877] [01:10:01.24] and what am I doing?
[L1878] [01:10:02.88] Um
[L1879] [01:10:03.92] you can, you know, you can just end up
[L1880] [01:10:06.12] coasting in a certain direction.
[L1881] [01:10:09.56] And I think it's important for people to
[L1882] [01:10:14.00] sit down and truly reflect and think
[L1883] [01:10:16.92] from time to time
[L1884] [01:10:18.72] like, okay, if I keep going in this
[L1885] [01:10:21.20] direction
[L1886] [01:10:22.88] is this going to lead to a place that I
[L1887] [01:10:24.84] want to be?
[L1888] [01:10:26.36] Um
[L1889] [01:10:27.52] and you know, this sort of advice
[L1890] [01:10:30.24] is good for all aspects of life, really.
[L1891] [01:10:33.32] Like,
[L1892] [01:10:34.52] like, if I keep if I keep, you know,
[L1893] [01:10:36.68] just allowing things to be the way they
[L1894] [01:10:39.32] are, am I going to be okay with that? Or
[L1895] [01:10:41.68] do I need to do something? Do I need to
[L1896] [01:10:43.68] So, it's like a little interrupts, you
[L1897] [01:10:45.12] know, in your
[L1898] [01:10:46.56] life reflection and just sort of
[L1899] [01:10:49.08] like, okay, is this is this where I Do I
[L1900] [01:10:51.32] Do I need to be coasting here? Like, do
[L1901] [01:10:53.08] I need to Yeah, I think
[L1902] [01:10:55.20] um
[L1903] [01:10:57.00] like in research for me, I was
[L1904] [01:11:00.44] always reevaluating like, okay,
[L1905] [01:11:03.64] you know, what I do last year and what I
[L1906] [01:11:05.16] do the year before and, you know,
[L1907] [01:11:07.92] could you know, like what do I know now
[L1908] [01:11:09.96] that I didn't know then and like, you
[L1909] [01:11:11.56] know, am I progressing? I think like
[L1910] [01:11:14.60] like that sort of self-evaluation
[L1911] [01:11:17.08] uh is crucial when you're in grad school
[L1912] [01:11:19.24] because, you know, once you're in a PhD
[L1913] [01:11:21.76] program,
[L1914] [01:11:23.44] there are no more like easy metrics to
[L1915] [01:11:26.56] gauge like how good or bad you're doing
[L1916] [01:11:29.88] and the truth is
[L1917] [01:11:31.64] you're just doing like, you know, like
[L1918] [01:11:33.88] like there there just isn't such a
[L1919] [01:11:35.44] metric. So, all you can really do is
[L1920] [01:11:38.60] evaluate your past self with your
[L1921] [01:11:41.12] present self
[L1922] [01:11:42.80] and compare and contrast
[L1923] [01:11:45.24] to to see if you're making progress with
[L1924] [01:11:47.92] whatever it is you want to do.
[L1925] [01:11:49.72] Thank you so much for your time,
[L1926] [01:11:50.68] Professor Williams. I really appreciate
[L1927] [01:11:52.08] it. Yeah, I appreciate you having me
[L1928] [01:11:53.96] here. Been fun. Thanks.
[L1929] [01:11:56.20] >> Hey, thank you for watching this
[L1930] [01:11:57.28] podcast. If you liked it and you want to
[L1931] [01:11:58.92] see the show grow, please support with a
[L1932] [01:12:01.08] comment or a like.
[L1933] [01:12:03.04] Also, if you have any recommendations
[L1934] [01:12:04.92] for people you want me to bring on,
[L1935] [01:12:06.92] please drop a comment. Guests like
[L1936] [01:12:09.08] Barbara Liskov, Mike Stonebraker, Mark
[L1937] [01:12:11.80] Booker, these were all people that I
[L1938] [01:12:13.84] brought on because someone left a
[L1939] [01:12:15.68] comment. On another note, aside from the
[L1940] [01:12:17.96] podcast, I'm working on building the
[L1941] [01:12:19.76] ergonomic keyboard that I wish existed.
[L1942] [01:12:22.24] Here's a glance at the prototype. It's a
[L1943] [01:12:24.12] split keyboard, so there's two sides. Um
[L1944] [01:12:27.12] this is in the case. But yeah, we
[L1945] [01:12:28.60] launched on Kickstarter and we hit our
[L1946] [01:12:30.40] goal within eight hours of launching. I
[L1947] [01:12:32.48] really appreciate it if you were one of
[L1948] [01:12:33.88] the people who grabbed one of the early
[L1949] [01:12:35.60] units. Um we're now working on the long
[L1950] [01:12:37.96] journey of building the tooling now. And
[L1951] [01:12:40.08] so, if you still want to pick one up,
[L1952] [01:12:41.80] I've left the late pledges open on
[L1953] [01:12:43.80] Kickstarter, so you can grab one there.
[L1954] [01:12:46.00] I'll put a link in the description.
[L1955] [01:12:47.92] Thank you again for watching the podcast
[L1956] [01:12:50.32] and I'll see you in the next episode.
