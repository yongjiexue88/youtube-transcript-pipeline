Chunk 1; segments 1–391. 

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
