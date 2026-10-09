Chunk 1; segments 1–337. 

# Testing Neetcode With 3 Leetcode Hards (Live Whiteboarding)

Source ID: source-0ff73d892aeb9a09
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Testing_Neetcode_With_3_Leetcode_Hards_(Live_Whiteboarding)_en.txt
Video: https://www.youtube.com/watch?v=rbtO3a6Qb00

[L10] [00:00.08] In this problem, given two strings, I
[L11] [00:03.84] let's call it word one and word two. I
[L12] [00:06.80] want you to return the minimum number of
[L13] [00:09.52] operations required to convert word one
[L14] [00:12.88] into word two. And the operations you
[L15] [00:15.84] can perform are either inserting a
[L16] [00:18.08] character, deleting a character, or
[L17] [00:20.80] replacing a character. How would you do
[L18] [00:22.88] this problem? Okay. So, I guess I'm just
[L19] [00:26.40] thinking in terms of like an example
[L20] [00:28.40] right now, but I do know like what this
[L21] [00:30.80] question is and I know like the patterns
[L22] [00:32.56] it falls into. Um, but I don't know like
[L23] [00:36.40] all the details. But, um, I do know off
[L24] [00:39.28] the top of my head that this problem can
[L25] [00:40.72] be solved with recursion and then that
[L26] [00:42.96] can like lend itself into the DP
[L27] [00:44.72] solution. So basically as I would go
[L28] [00:48.00] through this um I guess it's not
[L29] [00:49.92] necessarily true that they're going to
[L30] [00:51.04] be the same length and they don't have
[L31] [00:52.88] to be since we're we can insert, delete
[L32] [00:54.64] or modify. So it's 100% true that we can
[L33] [00:58.08] convert one to the other. It's just a
[L34] [00:59.52] matter of like the operations which I
[L35] [01:00.88] think you mentioned as part of the
[L36] [01:02.40] question. Um, so I guess uh there's
[L37] [01:06.72] three uh possibilities or maybe there's
[L38] [01:10.16] only two, but one is that they're equal.
[L39] [01:12.88] Um, in which case you just shift the
[L40] [01:15.84] pointer. So you can kind of just ignore
[L41] [01:17.20] that. And then same thing here. Now here
[L42] [01:20.56] where uh they're different, this is
[L43] [01:23.52] where it gets interesting because unless
[L44] [01:25.20] we can like predict the future, we don't
[L45] [01:26.48] really know which one would result in
[L46] [01:28.88] the minimum. So in terms of like the
[L47] [01:30.80] decision tree, it's just going to be a
[L48] [01:32.40] matter of like brute forcing. So
[L49] [01:36.40] um one would be to like delete the
[L50] [01:40.24] character, one would be to insert, and
[L51] [01:44.24] the other I guess would be to just
[L52] [01:45.92] modify. And in this case, we're trying
[L53] [01:47.52] to turn this word into that one. So we
[L54] [01:50.64] would modify this one. And
[L55] [01:54.72] that's going to be edit.
[L56] [01:57.04] And then so among these
[L57] [01:59.76] I guess the recursive way would be to
[L58] [02:01.92] just uh solve this recursively and then
[L59] [02:04.64] add like a cache which is dynamic
[L60] [02:06.88] programming. Um but what I would do if I
[L61] [02:10.08] was going to skip that recursive
[L62] [02:11.20] solution what I would do is just kind of
[L63] [02:12.88] roughly look at this try to figure out
[L64] [02:14.88] what like the equation would be. And
[L65] [02:16.72] when I say equation I mean like result
[L66] [02:19.68] is going to equal like some uh DP call
[L67] [02:22.96] maybe like the maximum of these three.
[L68] [02:25.84] And then so uh if I was going to do the
[L69] [02:29.04] actual DP solution which I think would
[L70] [02:31.84] end up being like n * m time complexity
[L71] [02:35.28] based on like the dimensions of this
[L72] [02:36.80] grid uh you can kind of imagine like you
[L73] [02:40.00] could take these two words and like
[L74] [02:44.32] make like a grid out of them and then
[L75] [02:46.48] you just like fill in that grid and it
[L76] [02:48.72] would tell you the solution.
[L77] [02:49.76] >> But what's the what's a cell in that
[L78] [02:52.40] grid represent?
[L79] [02:53.60] >> Yeah. So that's the hard part [laughter]
[L80] [02:55.44] and it depends on how you set it up. I
[L81] [02:57.92] always set it up a way that like most
[L82] [02:59.68] people don't like, but I guess so if
[L83] [03:02.88] this is the zero end, it would basically
[L84] [03:05.44] be like, okay, what's the edit distance
[L85] [03:07.60] of like the first character of each word
[L86] [03:10.08] that's over here? Over here, it would be
[L87] [03:11.84] a bit more interesting where it's like,
[L88] [03:13.20] okay, this portion of the word and this
[L89] [03:15.60] portion of the word. And so as you keep
[L90] [03:17.92] filling these in, what you notice is
[L91] [03:19.52] that like to if we're doing these three
[L92] [03:22.40] calls, uh to fill in the last cell, it
[L93] [03:25.28] would just be a matter of like looking
[L94] [03:28.72] um in whatever direction. So uh like if
[L95] [03:34.72] we were deleting a character from word
[L96] [03:36.88] one, then we'd probably just look that
[L97] [03:38.96] way. Uh yeah, or maybe I'm that
[L98] [03:42.80] opposite. But anyways, this is where it
[L99] [03:45.68] gets hard and this is where you actually
[L100] [03:46.96] have to start thinking and they usually
[L101] [03:48.96] I'll start writing the code at this
[L102] [03:50.24] point. Um because that actually does
[L103] [03:53.36] help me, but for some people maybe
[L104] [03:55.04] they'll figure it out in their head
[L105] [03:56.40] first. But if you go from the recursive
[L106] [03:58.24] solution to DP, it's a lot easier. I
[L107] [04:01.12] see. Okay. So the cell is the answer for
[L108] [04:05.36] the substring up until that uh N and M.
[L109] [04:09.92] And you you're saying you would give a
[L110] [04:13.36] formula for how to build up the next
[L111] [04:16.48] solution out of the existing ones that
[L112] [04:19.28] you've done so far.
[L113] [04:20.32] >> Yeah, that's right. And that kind of
[L114] [04:21.92] like I'd probably spend more time on
[L115] [04:23.52] this part just to make sure that I
[L116] [04:25.12] really like understand what's going on
[L117] [04:26.80] in terms of like the exact sub problem
[L118] [04:30.08] because we're allowed to delete, insert,
[L119] [04:32.40] or edit.
[L120] [04:34.32] So I assume that they're all valid. I
[L121] [04:36.64] assume like one of them like they they'd
[L122] [04:38.72] all be necessary at some point unless
[L123] [04:40.80] I'm like missing something off the top
[L124] [04:42.32] of my head right now. Maybe like there's
[L125] [04:43.68] a case where you'd never delete or you'd
[L126] [04:45.52] never insert. Um but
[L127] [04:49.84] like in this problem just going through
[L128] [04:51.20] the example I can see that we just edit
[L129] [04:52.72] twice. We'd edit here and then edit
[L130] [04:54.48] here. We wouldn't do any delete or
[L131] [04:56.24] insert. But maybe if I change the
[L132] [04:57.60] example, um,
[L133] [05:00.40] if I do this,
[L134] [05:04.16] uh, well, maybe I should have done the
[L135] [05:06.32] other way. But the idea is that like we
[L136] [05:08.72] delete one character from from one
[L137] [05:10.64] substring to get the other one.
[L138] [05:12.16] >> I see. Okay. Yeah. I mean, I think I I
[L139] [05:15.84] get what you're saying. You're clearly
[L140] [05:17.36] going in the the right direction here.
[L141] [05:19.44] We just would have to spend a bunch of
[L142] [05:20.88] time figuring out the case analysis.
[L143] [05:23.44] Um, okay. Let's let's try uh okay how
[L144] [05:28.40] about this one? I know this is a a very
[L145] [05:31.76] famous difficult problem which is um
[L146] [05:35.44] let's say I give you uh two sorted
[L147] [05:39.36] arrays and I want you to find the median
[L148] [05:43.44] number among the two sorted arrays. How
[L149] [05:47.84] would you how would you do that one?
[L150] [05:49.84] >> Okay, this one's always annoying. Um, so
[L151] [05:52.56] I'm going to like just try to craft an
[L152] [05:54.40] example that hopefully
[L153] [05:56.80] I can try to like derive the solution.
[L154] [05:59.84] Even though I kind of know it off the
[L155] [06:01.20] top of my head, I think you can reason
[L156] [06:03.44] about the general idea.
[L157] [06:07.20] Wonder if I can get a better.
[L158] [06:09.84] Okay, so I picked these two arrays. I
[L159] [06:12.48] might need to change the example because
[L160] [06:14.08] the example is going to tell us like
[L161] [06:15.68] what the solution is because I know
[L162] [06:17.84] there's going to be edge cases.
[L163] [06:20.16] For example, what if there's duplicates
[L164] [06:22.00] like between the two arrays? What if
[L165] [06:24.08] like one is further than the other? So,
[L166] [06:25.76] I might like modify this, but uh we have
[L167] [06:28.40] a couple duplicates and we have like
[L168] [06:30.16] this one is going to be there. So, we
[L169] [06:33.68] have like an array that's like kind of
[L170] [06:35.84] overlapping.
[L171] [06:37.44] Um I guess just for like
[L172] [06:40.48] so this the fact that I don't know how
[L173] [06:42.24] to solve this problem now. I'm already
[L174] [06:43.60] thinking like okay, how do I manage my
[L175] [06:45.12] time in a real interview? Because what I
[L176] [06:47.12] want to do is like create a line with
[L177] [06:50.00] all these elements. And maybe if I have
[L178] [06:51.92] extra time, I'd even like color code to
[L179] [06:54.16] help me think. But I know that the
[L180] [06:57.12] solution is going to be some form of
[L181] [06:58.64] binary search. And so I want to know
[L182] [07:02.40] like if I can figure out the trick
[L183] [07:06.32] because if I can do that, then I'll have
[L184] [07:07.76] a chance of solving it. And if I can't
[L185] [07:09.84] then I probably won't. I know it's going
[L186] [07:12.48] to be a matter of like setting up the
[L187] [07:14.16] pointers initially, left and right here,
[L188] [07:17.36] and then left and right here, because
[L189] [07:19.60] what we want to do right now
[L190] [07:22.72] is eliminate part of the array.
[L191] [07:26.32] But I don't remember how to do that.
[L192] [07:28.02] [laughter]
[L193] [07:28.88] So, okay, if I just had one array, what
[L194] [07:31.36] I would do, and you gave me a target,
[L195] [07:33.68] right?
[L196] [07:34.00] >> Yeah.
[L197] [07:35.20] >> So,
[L198] [07:37.44] I want to know
[L199] [07:38.72] >> Oh, wait. No, just find the median.
[L200] [07:40.32] >> Oh, yeah. Median. media yet. Okay,
[L201] [07:42.72] actually that I think that actually
[L202] [07:44.08] makes it easier because maybe it
[L203] [07:45.84] wouldn't be possible otherwise.
[L204] [07:48.32] Okay, so median. So what that means is
[L205] [07:51.20] we'd want like literally the middle
[L206] [07:53.04] number. Okay, so the clue now that I
[L207] [07:56.32] have is that like uh we have nine
[L208] [07:59.92] elements total at least in this example.
[L209] [08:02.80] So how can I like eliminate something?
[L210] [08:05.60] Can I like do I know for sure that like
[L211] [08:09.12] at least these three are not the median?
[L212] [08:13.68] Not really. Because if we have nine
[L213] [08:16.64] elements, I know the fifth one is the
[L214] [08:18.48] median and these like technically we
[L215] [08:22.08] could have like some elements here and
[L216] [08:24.08] then maybe that could be the median. So
[L217] [08:25.84] that's not going to work. So now I I
[L218] [08:27.92] know for sure that to solve this problem
[L219] [08:30.40] at each step we're going to have to look
[L220] [08:32.40] at both arrays. But I still don't know
[L221] [08:35.12] how to do. [laughter]
[L222] [08:37.76] And so um I'll probably go through an
[L223] [08:41.28] example. So now I'm thinking like can I
[L224] [08:42.96] just go through this example like
[L225] [08:44.32] without even trying to worry about the
[L226] [08:45.68] solution just like somehow like on pen
[L227] [08:47.92] and paper just like solve this problem
[L228] [08:49.52] by like eliminating like portions of the
[L229] [08:52.00] array at a time. I don't need to
[L230] [08:54.64] eliminate from both arrays. I'd really
[L231] [08:56.56] only need to do it from one array. Okay.
[L232] [08:59.36] So how can I do it? So knowing that this
[L233] [09:01.20] is the entire thing somehow can I like
[L234] [09:04.24] look at three or like look at the median
[L235] [09:06.56] in one of these to figure that out. I
[L236] [09:08.56] think probably that's it. I think
[L237] [09:10.16] probably I'd have to look at the median
[L238] [09:11.76] here and the median here do some kind of
[L239] [09:15.20] comparison
[L240] [09:16.96] to figure out what I was talking about
[L241] [09:18.48] earlier where like if we have like
[L242] [09:21.68] nine elements the fifth one is like the
[L243] [09:24.96] median that we're trying to find. And so
[L244] [09:26.72] really all we want to know is like are
[L245] [09:28.00] we here or are we here? So, I'm getting
[L246] [09:30.40] closer, [laughter] but um
[L247] [09:35.28] yeah, I know there's going to be some
[L248] [09:36.80] off like some off by ones here because
[L249] [09:39.20] like if there's just two elements, the
[L250] [09:41.52] median is different where if it's just
[L251] [09:43.04] like one element in the middle. So,
[L252] [09:46.88] this is where I'd get like a coffee,
[L253] [09:48.85] [laughter]
[L254] [09:50.24] but I'm definitely close. Like I I do
[L255] [09:52.32] not even remember this problem. I think
[L256] [09:53.76] it's been like 5 years since I made the
[L257] [09:55.44] video for it. I don't think I ever
[L258] [09:57.36] solved it again. But you can see that
[L259] [09:59.28] like from first principles you can
[L260] [10:01.36] actually like get like a little bit
[L261] [10:03.92] closer. [laughter]
[L262] [10:06.00] Okay, let's let's make things a little
[L263] [10:08.08] bit harder. So this question um given a
[L264] [10:13.68] n byn chessboard I want you to figure
[L265] [10:18.48] out the uh number of orientations
[L266] [10:23.76] where you could place n queens such that
[L267] [10:27.52] none of the queens are attacking each
[L268] [10:29.28] other. So you know queens they attack in
[L269] [10:32.48] all c cardinal directions and the
[L270] [10:35.12] diagonals.
[L271] [10:36.88] uh you need to find a number of distinct
[L272] [10:40.48] solutions where you could place n queens
[L273] [10:42.96] on this this board and none of them are
[L274] [10:46.64] um hitting one another.
[L275] [10:49.76] Okay, so
[L276] [10:52.08] I'm just setting up the grid because
[L277] [10:53.92] that's going to be like the most
[L278] [10:55.04] important part to like visualize this
[L279] [10:56.96] and I know that there's going to be
[L280] [11:00.00] a trick involved. So
[L281] [11:04.72] um okay so off the top of my head how do
[L282] [11:06.48] we like break down this problem? One is
[L283] [11:08.32] like we need to know are any queens
[L284] [11:10.80] attacking each other in terms of like
[L285] [11:13.28] the brute force solution the best way to
[L286] [11:15.52] do that would be some kind of just like
[L287] [11:17.04] trial and error like backtracking
[L288] [11:18.56] approach. I think that's the best way to
[L289] [11:20.56] do this uh problem from memory. Um, and
[L290] [11:25.44] then what what's straightforward is that
[L291] [11:28.24] if a queen is in the same like vertical
[L292] [11:31.60] or horizontal
[L293] [11:34.00] as another queen, it's pretty
[L294] [11:35.84] straightforward because we can literally
[L295] [11:38.56] just use some kind of like hash data
[L296] [11:40.16] structure just to keep track of like the
[L297] [11:43.12] row or like the column if it's going
[L298] [11:47.04] that way. Um, but the hard thing is the
[L299] [11:49.36] diagonals obviously because that's
[L300] [11:52.64] changing. Like there's no like diagonal
[L301] [11:54.80] here that tells you you're on like that
[L302] [11:56.48] diagonal. But there's a trick. And so
[L303] [11:59.20] people always ask, how would you know
[L304] [12:00.64] this? Um, that's a good question. I
[L305] [12:03.92] definitely didn't come up with it, but
[L306] [12:05.28] the trick is this that okay because so
[L307] [12:08.24] let's say I'm I'm on this square. Uh,
[L308] [12:11.92] this is row one and column one. And if
[L309] [12:16.16] I'm going along this diagonal,
[L310] [12:19.28] uh, okay, I drew that wrong. But if I'm
[L311] [12:21.68] going along that diagonal,
[L312] [12:24.40] uh, if I go this way, I just increased
[L313] [12:28.24] the row by one and I decreased the
[L314] [12:31.36] column by one. If I go that way, I just
[L315] [12:35.52] increased the column by one, but I like
[L316] [12:39.12] decrease the row by one. So the trick is
[L317] [12:43.44] that if I can like redraw this I guess
[L318] [12:48.96] uh this diagonal one + one is going to
[L319] [12:54.08] be two here. So like the sum of those
[L320] [12:56.08] values can be used to define the
[L321] [12:57.68] diagonal is basically uh the trick. So I
[L322] [13:01.36] would solve this problem
[L323] [13:03.52] pretty easily I guess just by having uh
[L324] [13:07.60] four hash data structures and the key
[L325] [13:10.48] for those uh data structures well two of
[L326] [13:13.28] them are just going to be like a row or
[L327] [13:14.72] and column set the other one is going to
[L328] [13:16.24] be different it's going to be uh this
[L329] [13:18.80] diagonal but also the other diagonal as
[L330] [13:20.72] well which will have I think the
[L331] [13:22.56] opposite
[L332] [13:24.32] uh like okay as we go this way
[L333] [13:29.20] it's just getting bigger. Um,
[L334] [13:33.28] okay. I actually don't remember that.
[L335] [13:35.28] But, um,
[L336] [13:38.96] okay. So, now I'm thinking about it. Let
[L337] [13:40.80] me just take like one second. [laughter]
[L338] [13:49.04] Um,
[L339] [13:53.04] >> so you're just trying to get quick
[L340] [13:55.04] diagonal membership like given, you
[L341] [13:58.00] know, is that is that occupied or not?
[L342] [14:00.00] >> Yeah, exactly. It's just like a key
[L343] [14:01.28] value lookup.
[L344] [14:02.16] >> Yeah.
[L345] [14:02.64] >> So,
[L346] [14:04.64] um,
