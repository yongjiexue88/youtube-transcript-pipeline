Chunk 1; segments 1–357. 

# Turing Award Winner: Thinking Clearly, Paxos vs Raft, Working With Dijkstra | Leslie Lamport

Source ID: source-4005a50ded85af4c
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Thinking_Clearly,_Paxos_vs_Raft,_Working_With_Dijkstra_Leslie_Lamport_en.txt
Video: https://www.youtube.com/watch?v=U719vQz-WFs

[L10] [00:00.16] If you think you know something but
[L11] [00:02.72] don't write it down, you only think you
[L12] [00:05.28] know it.
[L13] [00:06.32] >> This is Leslie Lamport. He's a Turing
[L14] [00:08.40] Award winner famous for his
[L15] [00:09.76] contributions to distributed systems.
[L16] [00:11.84] And I interviewed him for the stories
[L17] [00:13.36] behind his papers.
[L18] [00:15.04] >> Their reaction shocked me. They became
[L19] [00:18.48] angry. I really thought they might
[L20] [00:21.12] physically attack me.
[L21] [00:22.88] >> What was it about Dystra's old solution
[L22] [00:26.08] that you felt was unsatisfactory? It was
[L23] [00:29.04] not an obvious idea to most people that
[L24] [00:31.52] had actually impressed Dystra.
[L25] [00:34.00] >> As the inventor of the Paxus algorithm,
[L26] [00:36.16] I asked them his thoughts on the
[L27] [00:37.52] competing raft algorithm.
[L28] [00:39.04] >> There was a bug discovered in Raft and
[L29] [00:41.36] fixed, but I believe the algorithm that
[L30] [00:44.48] they found more understandable was one
[L31] [00:46.72] with that bug.
[L32] [00:48.00] >> I also enjoyed reflecting over his
[L33] [00:49.84] 50-year career. You say things like,
[L34] [00:51.92] "You never considered yourself smart.
[L35] [00:54.24] How could that be?" Stupid people think
[L36] [00:56.56] they're smart because they're too stupid
[L37] [00:58.16] to realize they're not.
[L38] [01:00.56] >> You felt like a failure at some point
[L39] [01:02.80] because you wanted to develop this grand
[L40] [01:05.04] theory of concurrency and you never
[L41] [01:08.08] discovered it. Do you still feel that
[L42] [01:10.00] way?
[L43] [01:11.84] Here's the full episode.
[L44] [01:17.36] I wanted to start with the bakery
[L45] [01:18.80] algorithm. What is the problem that the
[L46] [01:21.36] bakery algorithm solves? And you know
[L47] [01:23.44] how did you discover the problem?
[L48] [01:25.52] >> Well uh the problem was invented or
[L49] [01:29.04] discovered by Edkar Dystra in a 1965 I
[L50] [01:34.00] think it was 1965 paper and that began I
[L51] [01:38.80] consider that really the beginning of
[L52] [01:41.84] the theory of uh concurrency concurrent
[L53] [01:45.84] programming. He was the first one who
[L54] [01:49.68] really
[L55] [01:51.20] made use of the idea of of concurrency
[L56] [01:54.80] as a way of structuring programs as a as
[L57] [01:58.24] a collection of semi-independent tasks
[L58] [02:02.64] and the processes have to uh synchronize
[L59] [02:06.56] with one another. Uh one of the
[L60] [02:08.64] processes or you know among the
[L61] [02:10.88] processes would be well this was in the
[L62] [02:13.68] days of time sharing uh you know right
[L63] [02:16.56] at really at the beginning of beginnings
[L64] [02:19.04] of time sharing and the idea of multiple
[L65] [02:23.20] people using the same computer. People
[L66] [02:26.00] realized that computers were worked
[L67] [02:28.64] faster than humans and so and computers
[L68] [02:32.08] were very expensive in those days. So uh
[L69] [02:35.12] they wanted they could use a computer to
[L70] [02:38.32] simultaneously
[L71] [02:40.40] to be used simultaneously by multiple
[L72] [02:43.20] people. The program that each user was
[L73] [02:46.88] running you know was a separate program
[L74] [02:49.84] but sometimes you know there were
[L75] [02:52.16] resources that got shared. for example,
[L76] [02:54.64] a printer, two people trying to print on
[L77] [02:57.68] the same printer at the same time. Well,
[L78] [03:00.40] the result would be, you know, not very
[L79] [03:02.64] satisfactory. So uh he realized there
[L80] [03:06.00] was this problem of uh synchronizing
[L81] [03:10.32] um multiple processes via the idea of
[L82] [03:12.96] what he called a critical section or
[L83] [03:15.20] some piece of code in each of the
[L84] [03:16.96] processes so that at most one process
[L85] [03:20.64] can be executing that piece of code at
[L86] [03:22.96] any particular time. So that code might
[L87] [03:25.68] be the code that prints something on the
[L88] [03:28.24] printer. So the problem was how to get
[L89] [03:31.04] the uh processes to synchronize among
[L90] [03:34.32] themselves so that at most one process
[L91] [03:37.36] was executing its critical section at a
[L92] [03:39.68] time. And
[L93] [03:42.48] um it was in 1972 that I learned about
[L94] [03:47.12] the problem because there was an article
[L95] [03:50.40] giving a solution to it um in the CACM
[L96] [03:55.44] communications of the ACM
[L97] [03:58.08] and uh I mean I used to program and I
[L98] [04:02.16] liked little programming problems you
[L99] [04:04.80] know uh and this was just a very nice
[L100] [04:09.52] little programming problem.
[L101] [04:11.92] And so I looked at the solution, which
[L102] [04:15.36] is fairly complicated, and I said, "Oh,
[L103] [04:17.20] gee, that shouldn't be so hard." And so
[L104] [04:20.00] I whipped off a very simple uh algorithm
[L105] [04:24.24] for two processes and submitted it to
[L106] [04:28.00] CACM. And a couple of weeks later, I
[L107] [04:31.60] received uh a letter from the editor uh
[L108] [04:35.68] pointing out the bug in my program. So
[L109] [04:38.72] that had two effects.
[L110] [04:41.36] The first was that I realized that
[L111] [04:45.28] concurrent programs were hard to get
[L112] [04:47.28] right and that you needed a proof that
[L113] [04:52.56] they were correct. And second uh was
[L114] [04:56.88] that made me feel I'm gonna solve that
[L115] [04:59.44] damn problem. And I came up with the
[L116] [05:02.96] bakery algorithm which was inspired by
[L117] [05:07.28] uh the idea came from you know what now
[L118] [05:11.60] called the deli problem where you have a
[L119] [05:15.04] deli counter and that collects you know
[L120] [05:18.72] tickets a roll of tickets and every
[L121] [05:21.28] customer would come in and take a ticket
[L122] [05:23.60] and then the the next person s to to be
[L123] [05:26.96] served would be the one with the highest
[L124] [05:29.60] the lowest numbered ticket uh that
[L125] [05:31.52] hadn't been served yet. And basically
[L126] [05:34.64] that I took that idea uh but since uh
[L127] [05:38.64] there was no central server uh or at
[L128] [05:42.56] least the the problem is as specified by
[L129] [05:45.92] Dystra involved no central control. Each
[L130] [05:50.88] process basically had to choose their
[L131] [05:53.52] own ticket. That was you know the basic
[L132] [05:55.68] idea and the algorithm was you know
[L133] [05:58.08] quite simple. And I wrote a a proof of
[L134] [06:02.00] correctness.
[L135] [06:03.68] And uh the proof of correctness revealed
[L136] [06:07.04] to me that
[L137] [06:09.92] this algorithm was had this very
[L138] [06:13.28] interesting property.
[L139] [06:15.76] There was a general feeling in fact
[L140] [06:18.56] somebody published in a in a book or
[L141] [06:20.72] paper saying you know that it was
[L142] [06:23.68] impossible to implement mutual exclusion
[L143] [06:27.28] like this without using some lower level
[L144] [06:30.88] mutual exclusion.
[L145] [06:32.80] And the way most the mutual exclusion
[L146] [06:36.64] that was assumed generally was that of
[L147] [06:41.52] shared registers. you know, shared
[L148] [06:43.36] pieces of memory that could be written
[L149] [06:46.56] and write and uh read by different
[L150] [06:49.76] processes. And the idea is that, you
[L151] [06:52.48] know, you couldn't have one process, you
[L152] [06:54.88] know, two processes writing at the same
[L153] [06:56.64] time or one process reading while the
[L154] [06:58.80] other process was writing. People
[L155] [07:01.60] assumed that those actions were atomic.
[L156] [07:04.80] They always performed as if they
[L157] [07:07.20] occurred in some specific order. But the
[L158] [07:09.84] amazing thing about the bakery algorithm
[L159] [07:13.12] was that it didn't require that
[L160] [07:14.80] assumption. It it used uh each shared
[L161] [07:19.36] memory a piece of memory was only
[L162] [07:21.76] written by a single process. So it
[L163] [07:24.08] didn't have to worry about two processes
[L164] [07:26.64] interfering with each other. The only
[L165] [07:29.44] problem that you might come is that
[L166] [07:31.68] somebody reading the uh value while it
[L167] [07:36.16] was being written might get you know
[L168] [07:37.92] some unknown value but the algorithm
[L169] [07:41.04] worked anyway.
[L170] [07:43.20] If somebody read if one process read
[L171] [07:45.92] while the registers was being written
[L172] [07:48.40] that process reading process could get
[L173] [07:50.72] absolutely any value and the algorithm
[L174] [07:53.44] still worked. I saw in your your writing
[L175] [07:56.72] about this problem that you shared it
[L176] [07:59.36] with a colleague named Anatol Hol and
[L177] [08:03.76] the proof was so remarkable that uh they
[L178] [08:07.76] didn't believe it and
[L179] [08:08.88] >> well the the result was so remarkable.
[L180] [08:11.04] >> Yes. Yes. that didn't believe it.
[L181] [08:13.36] >> And uh you know I wrote the proof on the
[L182] [08:16.88] on the
[L183] [08:18.72] whiteboard for him and you know he
[L184] [08:20.80] couldn't find it but he went home and
[L185] [08:22.72] saying there must be something wrong
[L186] [08:24.16] with it and uh he obviously never found
[L187] [08:27.28] anything wrong with it.
[L188] [08:28.40] >> Right. I saw the name of the paper is a
[L189] [08:31.68] new solution of Dystra's concurrent
[L190] [08:34.08] programming problem.
[L191] [08:35.84] What was it about Dystra's old solution
[L192] [08:39.28] that you felt was unsatisfactory and
[L193] [08:42.08] made you want to solve this problem?
[L194] [08:44.16] >> Uh well, there was an unsatisfactory
[L195] [08:47.44] aspect of his original solution that had
[L196] [08:51.20] the property that if there were a lot of
[L197] [08:53.76] if processes kept trying to uh enter
[L198] [08:56.88] their critical section uh an individual
[L199] [09:00.32] process might be starved. might never
[L200] [09:02.72] get access to to the critical section
[L201] [09:06.40] that was solved uh by you know the next
[L202] [09:10.24] solution I think was Don Kuth's the
[L203] [09:14.64] condition that was
[L204] [09:17.84] desired or that that measured that what
[L205] [09:20.96] was considered the uh the efficiency of
[L206] [09:24.64] it was how long a process might have to
[L207] [09:27.44] wait and I believe that the bakery
[L208] [09:31.20] algorith of them was the first one that
[L209] [09:34.48] was really first come first served. That
[L210] [09:37.52] is if one process came if what it meant
[L211] [09:40.64] is if one process chose its number
[L212] [09:43.92] before another process tried to enter
[L213] [09:47.12] the first process would enter the
[L214] [09:48.96] critical section before the other
[L215] [09:50.40] process did. And I believe the bakery
[L216] [09:52.72] algorithm was the first one with that uh
[L217] [09:55.84] with that property. And also I think it
[L218] [09:58.48] was simpler than uh other uh solutions
[L219] [10:03.12] >> in a lot of the writing. I see that you
[L220] [10:05.68] worked with Dystra and I saw in 1976
[L221] [10:11.12] you actually worked for a month in the
[L222] [10:13.52] Netherlands and you worked with them.
[L223] [10:15.68] Can you talk about that a little bit?
[L224] [10:18.00] >> Dyster used to had the things they're
[L225] [10:20.80] called EWDs his initials.
[L226] [10:23.36] little papers, things that when he he
[L227] [10:26.16] thought of something, had some idea, he
[L228] [10:28.16] would write it down and send it out to
[L229] [10:30.40] people. Well, one of those EWDs was
[L230] [10:32.80] about he and uh some
[L231] [10:37.04] associates or actually sort of mentees I
[L232] [10:40.96] guess you would call them wrote this
[L233] [10:43.36] this algorithm. It was the first
[L234] [10:44.48] concurrent garbage collection algorithm.
[L235] [10:46.48] a way of writing programs evolved where
[L236] [10:49.84] there was a pool of memory
[L237] [10:53.36] uh that when a program would need a
[L238] [10:56.32] piece of memory, it would ask some
[L239] [10:59.20] server for it and be given this piece of
[L240] [11:01.60] memory. Uh but at some point it would
[L241] [11:04.72] stop using that memory. But the program
[L242] [11:08.24] itself wouldn't know that the one the
[L243] [11:11.28] particular process that created this
[L244] [11:13.44] memory you know wouldn't know whether
[L245] [11:15.84] some other process is using that memory
[L246] [11:17.84] or not. So there was an additional
[L247] [11:20.08] process called the garbage collector
[L248] [11:22.72] which would go around examining the
[L249] [11:24.88] memory and decide which pieces of memory
[L250] [11:28.80] were no longer being used and then put
[L251] [11:31.44] them back on the it's called the free
[L252] [11:33.52] list and in which uh the uh server that
[L253] [11:37.60] the process that was giving out the uh
[L254] [11:40.40] uh memory would be able to to take it. I
[L255] [11:43.76] looked at it and I realized that uh I
[L256] [11:46.32] could simplify the algorithm. Uh because
[L257] [11:49.84] he had some some spe the the handling of
[L258] [11:53.36] the free list was done by a special
[L259] [11:56.48] process that you know which had it to
[L260] [11:58.96] worry about its own coordination with
[L261] [12:01.20] the uh uh the processes that were using
[L262] [12:04.40] the memory. And I realized that that
[L263] [12:07.52] free list could just be made part of the
[L264] [12:11.20] regular data structure.
[L265] [12:13.36] uh so it didn't need special handling
[L266] [12:16.08] and that seemed to me like a very uh
[L267] [12:19.84] simple idea and a very obvious idea and
[L268] [12:22.96] I sent it to him and then when I get got
[L269] [12:26.40] the next version of the paper I
[L270] [12:28.16] discovered he had made me an author and
[L271] [12:31.52] I thought that was very generous of him
[L272] [12:35.44] uh to have to have done that because it
[L273] [12:37.92] seemed like very simple idea
[L274] [12:40.72] and I mean very obvious vious idea and
[L275] [12:45.52] I later realized much later that it was
[L276] [12:50.08] not an obvious idea to most people
[L277] [12:53.36] uh and that that had actually impressed
[L278] [12:56.64] uh Dystra
[L279] [12:58.80] when that was the only thing I actually
[L280] [13:00.48] did with Dystra many years later he said
[L281] [13:03.92] that I had uh a remarkable ability at
[L282] [13:07.44] abstraction
[L283] [13:08.96] only in very recent years I mean Maybe
[L284] [13:13.44] maybe after I got the touring award that
[L285] [13:17.20] I realized that the reason for my
[L286] [13:20.72] success and the reason I got it wind up
[L287] [13:23.20] wound up getting a touring award was not
[L288] [13:26.00] that I was particularly that smart but
[L289] [13:28.80] that I had this gift of abstraction and
[L290] [13:32.08] Dystra
[L291] [13:33.68] was smart enough to realize that I was
[L292] [13:37.28] invited to uh spend a month uh but not
[L293] [13:41.84] with Dysterra, with a colleague of his,
[L294] [13:43.84] Carl Carl Holton. Only one thing that
[L295] [13:47.68] was ever published came out of that.
[L296] [13:50.08] Carl and I would uh meet with Dystra
[L297] [13:54.16] once a week. Uh in the in the course of
[L298] [13:56.40] that discussion, the idea somehow came
[L299] [13:59.44] up that led to uh a variant of the
[L300] [14:03.28] bakery algorithm that I wrote up and
[L301] [14:05.36] published. Uh so that was the the one
[L302] [14:09.52] tangible result that that came from my
[L303] [14:11.92] month in uh the Netherlands.
[L304] [14:14.24] >> Yeah. I I saw that you wrote that. Yeah.
[L305] [14:16.64] You you spent one afternoon a week
[L306] [14:19.28] working, talking and drinking beer at
[L307] [14:21.52] Dextrous House and you kind of don't
[L308] [14:24.32] remember exactly who was uh you know in
[L309] [14:27.36] charge of uh what on that paper, but
[L310] [14:29.92] >> yeah. Well, I don't think I was really
[L311] [14:32.00] could have gotten that drunk because uh
[L312] [14:34.56] I probably drove to the meeting and back
[L313] [14:37.36] from the meeting. So,
[L314] [14:38.64] >> Right. Right.
[L315] [14:39.52] >> The the Dutch beer that I was drinking
[L316] [14:41.68] was not very alcoholic.
[L317] [14:44.88] >> I wanted to talk about your most cited
[L318] [14:46.96] paper, the one titled time clocks and
[L319] [14:49.68] the ordering of events and distributed
[L320] [14:51.84] systems. What's the story behind the
[L321] [14:54.40] paper and the problem you were solving
[L322] [14:56.08] with it?
[L323] [14:57.04] >> The origin was simple. uh it well
[L324] [15:00.56] somebody sent me a paper on building
[L325] [15:03.92] distributed databases and so where
[L326] [15:06.80] you'll have well multiple copies of the
[L327] [15:09.28] data in different places and you need to
[L328] [15:11.84] keep them synchronized in some way. I
[L329] [15:15.12] looked at it and I realized that their
[L330] [15:19.36] solution had this problem
[L331] [15:21.92] that the se that it it had the property
[L332] [15:24.56] that things would be executed as if they
[L333] [15:26.40] occurred in subsequence but that
[L334] [15:28.56] sequence could be different from the
[L335] [15:30.96] sequence in which they actually
[L336] [15:32.72] happened. The notion of of what you know
[L337] [15:36.80] happening before means is not obvious or
[L338] [15:40.72] not obvious to most people but I happen
[L339] [15:45.12] to
[L340] [15:46.96] you know learn about you know special
[L341] [15:49.44] relativity in particular uh what's known
[L342] [15:53.44] as the it's the space-time view of of
[L343] [15:56.80] special relativity where you basically
[L344] [16:00.88] consider space and time together just
[L345] [16:03.12] one four-dimensional thing and that was
[L346] [16:06.56] Einstein wrote his paper in 1905 and and
[L347] [16:09.44] in I think it was 1909
[L348] [16:12.32] uh somebody whose name I'm blocking on
[L349] [16:15.52] provided this four-dimensional view and
[L350] [16:18.72] that four-dimensional view has the the
[L351] [16:21.12] particular notion of what it means for
[L352] [16:24.08] one pro one event to occur before
[L353] [16:26.64] another and that notion is that one
[L354] [16:31.44] event happens before another. If a a
[L355] [16:36.16] signal
[L356] [16:38.00] uh was emitted from the first event and
[L357] [16:42.08] received by the whoever did that second
[L358] [16:44.56] event before that second event happened,
[L359] [16:47.44] but the communication could not travel
[L360] [16:49.76] faster than the speed of light because
[L361] [16:51.44] nothing can travel faster than the speed
[L362] [16:52.96] of light. Well, I realized there was an
[L363] [16:55.84] obvious analogy.
[L364] [16:58.56] Uh the notion of happens before is
[L365] [17:02.32] exactly the same as in relativity except
[L366] [17:06.00] instead of being whether something one
