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
[L367] [17:09.28] event can influence another by things
[L368] [17:12.96] traveling at the speed of light, it's
[L369] [17:15.36] whether the first event could have
[L370] [17:18.00] affected the other by information sent
[L371] [17:21.12] over messages that were actually sent in
[L372] [17:23.68] the system. The thing that you know blew
[L373] [17:27.20] people away was this this definition of
[L374] [17:29.92] of happens before in a distributed
[L375] [17:32.08] system with also this was the first
[L376] [17:35.12] paper I would call like you know had a
[L377] [17:38.40] scientific result about distributed
[L378] [17:41.12] systems. I made perhaps you know mistake
[L379] [17:45.12] that I was warned against at some point
[L380] [17:47.28] of having two ideas in in one paper. The
[L381] [17:52.00] other thing that I realized was that
[L382] [17:55.52] there was an an algorithm that would
[L383] [17:57.60] show whether one event that it would
[L384] [18:00.72] produce an ordering that satisfied this
[L385] [18:04.32] that condition that if some if one event
[L386] [18:06.88] happened the other before the other then
[L387] [18:08.96] that first event would be ordered before
[L388] [18:10.80] the other. And I realized that if you
[L389] [18:14.08] had an algorithm to do that, you could
[L390] [18:17.20] use it to basically provide the the
[L391] [18:21.04] synchronization you needed for any
[L392] [18:22.80] distributed system
[L393] [18:25.04] because you could describe that system
[L394] [18:27.04] in terms of a state machine. And a state
[L395] [18:30.80] machine as as I described it then is
[L396] [18:32.80] something that has a state and process
[L397] [18:36.80] executes you know uh commands that need
[L398] [18:40.72] to be executed in order and the command
[L399] [18:43.76] simply is something that makes a change
[L400] [18:47.36] of the state and and produces a value.
[L401] [18:50.56] And so you can just describe this state
[L402] [18:53.04] machine as just you know how event how
[L403] [18:56.16] commands affect the state and and how
[L404] [18:58.80] they produce and what you know what the
[L405] [19:00.88] new state is as a function of the
[L406] [19:02.40] original state and what the value is as
[L407] [19:04.64] a function of the original state. It it
[L408] [19:07.44] turned out that this was very obvious to
[L409] [19:10.00] me, but that's really in practice
[L410] [19:13.52] the important idea in that paper
[L411] [19:17.60] because it showed that this method of
[L412] [19:21.44] building distributed systems by thinking
[L413] [19:23.84] in terms of state machine and and can
[L414] [19:27.20] thinking about concurrent systems in
[L415] [19:30.00] terms of state machines.
[L416] [19:32.24] Um but that part was completely ignored.
[L417] [19:37.20] As a matter of fact, twice I talked to
[L418] [19:39.92] people about that paper and they said
[L419] [19:43.84] there was nothing in that paper about
[L420] [19:45.76] state machines and I had to go back and
[L421] [19:48.72] reread and reread the paper to be sure I
[L422] [19:51.28] wasn't going crazy and it really did
[L423] [19:53.20] talk about state machines. It's
[L424] [19:55.92] important uh for another reason. uh if
[L425] [19:59.28] you're trying to understand a concurrent
[L426] [20:01.44] program you concurrent programs are
[L427] [20:04.00] written the bakery algorithm is really
[L428] [20:06.08] an exception uh concurrent programs are
[L429] [20:08.96] written assuming atomic actions so that
[L430] [20:12.88] you assume that the execution behaves
[L431] [20:15.12] like a a sequence you you can assume
[L432] [20:19.12] that the execution proceeds as a
[L433] [20:21.12] sequence of events. It turns out that
[L434] [20:24.64] the way to understand, you know, why why
[L435] [20:28.00] does a program produce the right answer?
[L436] [20:30.72] Well, the answer is well, you it you
[L437] [20:32.56] give it the uh the you know the right
[L438] [20:34.72] input. You give it the input and then it
[L439] [20:37.20] produces the right answer. Well, but by
[L440] [20:40.40] the time you're in the middle of
[L441] [20:41.60] execution,
[L442] [20:43.28] what it was given at the beginning is
[L443] [20:45.68] ancient history. The only thing that
[L444] [20:48.88] that tells the program what to do next
[L445] [20:51.28] is its current state.
[L446] [20:53.68] And the way to understand
[L447] [20:56.72] uh a program, you know, a simple program
[L448] [20:59.12] that just, you know, takes input and
[L449] [21:01.04] produces an answer is to say what is the
[L450] [21:04.80] property of the state at each point that
[L451] [21:09.04] ensures that the answer it produces is
[L452] [21:12.40] correct is going to be correct. And that
[L453] [21:15.20] property which is mathematically a fun a
[L454] [21:20.00] boolean valued function of the state is
[L455] [21:23.20] called an invariant.
[L456] [21:25.12] And understanding the invariant
[L457] [21:28.08] is the way to understand the system. You
[L458] [21:30.96] know the the program and I realized that
[L459] [21:34.40] the same thing is true of concurrent
[L460] [21:36.16] systems and concurrent programs. People
[L461] [21:38.40] like to write proof you know behavioral
[L462] [21:40.32] proofs reasoning about sequences.
[L463] [21:43.04] And the problem with that is that the
[L464] [21:46.64] number of sequences possible sequences
[L465] [21:50.40] you know is exponential in the length of
[L466] [21:52.40] the sequence
[L467] [21:54.16] while the com so your complexity of your
[L468] [21:57.76] reasoning gets to be very complicated.
[L469] [22:00.16] It's very easy to to miss cases. Um but
[L470] [22:03.76] the complexity of an invariance proof
[L471] [22:06.16] the complexity of the invariant
[L472] [22:08.24] basically
[L473] [22:09.92] is well oh god it's the number of
[L474] [22:13.52] possible executions is exponential in
[L475] [22:16.48] the number of processes
[L476] [22:19.12] but the
[L477] [22:22.32] uh
[L478] [22:23.84] the behavior of the proof of a an
[L479] [22:26.72] invariance proof is quadratic in the
[L480] [22:29.76] number of processes. you know that's
[L481] [22:32.00] basically why invariance proofs are
[L482] [22:34.24] better but you know there's still for a
[L483] [22:37.28] long time that you know people you know
[L484] [22:40.88] doing uh distributed systems theory are
[L485] [22:44.16] trying to do it uh you know develop you
[L486] [22:47.36] know methods and formalism something
[L487] [22:49.60] that are based on partial orderings and
[L488] [22:51.76] that they've you know published a lot of
[L489] [22:54.00] papers but it's just you know not the
[L490] [22:56.88] way if you want to do it in practice
[L491] [22:58.40] that's that's not the way to do it and I
[L492] [23:00.72] shouldn't say you know it's not the way
[L493] [23:03.12] uh you know there are algorithms like
[L494] [23:05.36] the bakery algorithm that you know you
[L495] [23:10.08] know thinking in partial orderings is in
[L496] [23:12.24] fact a very good way of doing it but
[L497] [23:14.88] those are the exceptions the the work
[L498] [23:17.60] the method that works you know that you
[L499] [23:20.64] can be sure will will will work is the
[L500] [23:24.48] use of invariance
[L501] [23:26.16] >> I want to talk about the I guess the
[L502] [23:27.92] next paper which uh is the Byzantines
[L503] [23:31.60] general's problem. I think that's
[L504] [23:32.96] something that we hear about and we
[L505] [23:34.88] learn about when you're going through
[L506] [23:37.04] college and computer science and the
[L507] [23:39.60] name is great and I want to know the the
[L508] [23:41.84] story behind that problem. After I wrote
[L509] [23:45.36] that time clocks paper that was a tells
[L510] [23:48.88] you how to build a distributed system
[L511] [23:51.20] but assuming no failures and it was
[L512] [23:54.40] obvious that um
[L513] [23:57.92] you know distributed one reason for a
[L514] [23:59.60] distributed systems is you have multiple
[L515] [24:01.60] computers so if one fails you can you
[L516] [24:03.52] know keep going. in particular
[L517] [24:06.88] uh that was the problem that
[L518] [24:11.04] it was being solved at SRRI when I uh
[L519] [24:15.04] when I joined it but before I got to
[L520] [24:17.84] SRRI and I started working on that
[L521] [24:20.16] problem and I uh there's no notion of
[L522] [24:25.36] idea of you know what I should think
[L523] [24:27.12] about is you know what what can a
[L524] [24:28.80] failure do so I assume that you know the
[L525] [24:32.32] worst possible case that a failed
[L526] [24:34.00] process might do absolutely anything.
[L527] [24:37.04] And I came up with an algorithm that
[L528] [24:41.04] basically would uh implement a state
[L529] [24:44.16] machine uh
[L530] [24:47.84] under that assumption and that the
[L531] [24:50.56] algorithm I came out with used digital
[L532] [24:52.80] signatures. Yeah. So that it used the
[L533] [24:55.20] fact that a faulty process might do
[L534] [24:57.92] anything but it could not forge the
[L535] [25:00.00] signature of another process
[L536] [25:02.16] >> which just means that the message can be
[L537] [25:05.60] trusted that it came from a private
[L538] [25:07.68] >> right so that you can relay messages and
[L539] [25:10.56] the people know can check that the
[L540] [25:12.80] relayed message is actually the one that
[L541] [25:14.96] was originally sent uh and so that a
[L542] [25:18.72] solution using that when I got to SRRI I
[L543] [25:22.88] realized that the people were were
[L544] [25:26.00] trying to solve the same problem. Uh but
[L545] [25:29.76] there are two differences. First of all,
[L546] [25:32.24] at the time I did this was you know
[L547] [25:34.24] 1975.
[L548] [25:36.48] very few people know knew about digital
[L549] [25:38.24] signatures and in fact I don't remember
[L550] [25:40.16] when the Diffy Helman paper was
[L551] [25:42.40] published but it was around 1975
[L552] [25:46.08] and I happen to know about digital
[L553] [25:48.24] signatures because Whit Diffy who was
[L554] [25:51.44] one of the author two authors of that
[L555] [25:53.12] paper uh was a friend of mine and in
[L556] [25:58.16] fact at one point we were at a coffee
[L557] [26:00.88] house uh and he was describing these
[L558] [26:03.28] things that he said we have this problem
[L559] [26:05.12] of building digital signatures uh you
[L560] [26:08.40] know we haven't solved and I said oh
[L561] [26:10.32] that seems easy enough and uh and I sat
[L562] [26:13.20] down and literally on a napkin I wrote
[L563] [26:15.68] out a a you know the first digital
[L564] [26:18.80] signature algorithm. It was not
[L565] [26:20.80] practical at the time because it it
[L566] [26:23.84] required basically something like uh
[L567] [26:27.84] you know 128 bits to sign one bit of the
[L568] [26:32.88] you know of of the thing you they're
[L569] [26:34.88] signing. It's not quite that bad because
[L570] [26:37.44] you know as you might think because you
[L571] [26:39.04] could use sign not a
[L572] [26:42.88] the entire dent document but a hash of
[L573] [26:45.68] that document which you assume you know
[L574] [26:48.80] people cannot forge uh
[L575] [26:52.72] >> the hash they can't reverse
[L576] [26:54.72] >> yeah you can't reverse you go take a
[L577] [26:57.04] hash and and you know you find some
[L578] [26:59.36] other hash that you know or some other
[L579] [27:02.00] document that satisfies that hash. But
[L580] [27:04.72] anyway, that's why I had, you know,
[L581] [27:06.80] digital signatures were part of my
[L582] [27:08.88] toolkit. Uh, so the people at SRRI
[L583] [27:12.16] didn't have that, but they also had a
[L584] [27:15.60] nicer abstraction
[L585] [27:17.76] of it. Instead of getting agreement on a
[L586] [27:20.88] sequence among the processes on a
[L587] [27:23.04] sequence of commands,
[L588] [27:25.92] uh they would agree have an algorithm
[L589] [27:30.40] for agreement on a single command and
[L590] [27:34.00] then that algorithm would be uh executed
[L591] [27:38.08] multiple times to and you know that was
[L592] [27:41.04] a nicer way of of describing
[L593] [27:44.64] uh you know what you're doing than than
[L594] [27:47.52] the than than my method. So the first
[L595] [27:50.80] paper that was published uh use gave
[L596] [27:53.60] both the their original oh so but since
[L597] [27:58.32] they didn't have digital
[L598] [28:00.48] signatures they used a different
[L599] [28:02.40] algorithm uh and they had the property
[L600] [28:05.52] that to tolerate one faulty process uh
[L601] [28:10.00] you needed four processes whereas if you
[L602] [28:13.44] used digital signatures you only needed
[L603] [28:15.76] three processes. So the original paper
[L604] [28:18.96] contained both algorithms and so I was
[L605] [28:22.24] one of the authors. The other algorithm
[L606] [28:25.60] without digital signatures is is more
[L607] [28:28.40] complicated and the general one for end
[L608] [28:32.00] processes was really a work of genius.
[L609] [28:37.04] Uh it was almost incomprehensible. You
[L610] [28:39.84] just had to read in this complicated
[L611] [28:42.08] proof that uh you know for the arbitrary
[L612] [28:45.60] case of an arbitrary number of processes
[L613] [28:47.84] you need n pro for to tolerate n faults
[L614] [28:50.64] you needed four n processes whereas with
[L615] [28:53.68] digital signatures you need three n
[L616] [28:55.68] processes and the the algorithm for
[L617] [28:58.40] single fault wasn't hard but the one for
[L618] [29:01.12] multiple four parts was uh Marshall Peas
[L619] [29:04.88] was the one who did it and just
[L620] [29:07.20] brilliant uh Later in a in a later paper
[L621] [29:11.36] I uh I discovered uh a simpler proof one
[L622] [29:16.00] that was an inductive proofly proof that
[L623] [29:19.36] if it works for n minus one you know you
[L624] [29:23.28] it worked for n with 3 n if it works for
[L625] [29:27.04] 3 n * n minus one the original paper was
[L626] [29:30.72] uh you know the original one was just
[L627] [29:32.72] brilliant uh who would have discovered
[L628] [29:35.52] it anyway um so we published that paper
[L629] [29:40.24] and I realized that this was this the
[L630] [29:44.00] whole idea of Byzantine fault. So the
[L631] [29:46.16] thing is that Byzantine well Byzantine
[L632] [29:48.00] fault is one that where process assume a
[L633] [29:50.96] process can do anything. Now I was
[L634] [29:54.40] assuming that you know processing can do
[L635] [29:56.32] anything because you know I didn't know
[L636] [29:57.68] what to assume but the people at SRRI
[L637] [30:01.28] had the contract for building a
[L638] [30:03.52] multipprocess multi- computer system for
[L639] [30:06.64] flying airplanes and so they were the
[L640] [30:10.16] ones who appreciated the need for
[L641] [30:13.36] solving processes that can do malicious
[L642] [30:15.92] things because they they really couldn't
[L643] [30:18.08] assume what it would do. And every time
[L644] [30:21.84] you would get an algorithm and you you'd
[L645] [30:24.48] see, oh, uh, well, this algorithm, you
[L646] [30:28.48] know, try to get an algorithm with three
[L647] [30:30.08] processes, you know, for one fault, you
[L648] [30:32.40] know, you'd find that, you know, oh, you
[L649] [30:35.44] know, this this works and it must be,
[L650] [30:37.84] you know, really couldn't happen in
[L651] [30:39.28] practice. And then you'd be able to find
[L652] [30:41.76] some sequence of plausible failures that
[L653] [30:45.12] would lead the algorithm to be defeated
[L654] [30:48.16] if there were a faulty process. So you
[L655] [30:51.20] needed four uh and for some reason you
[L656] [30:55.20] know I thought that digital signatures
[L657] [30:59.28] was almost a metaphor in the algorithm
[L658] [31:02.24] that it should be possible
[L659] [31:04.80] you know since we weren't worried about
[L660] [31:07.20] malicious failures but but you know just
[L661] [31:10.96] things that happen randomly that there
[L662] [31:13.76] should be some way of of writing a
[L663] [31:17.12] digital signature algorithm that uh you
[L664] [31:22.00] know would have a sufficiently low
[L665] [31:23.60] probability of of failing but
[L666] [31:28.40] I never worked on that and nobody else
[L667] [31:30.64] ever did. So that those that algorithm
[L668] [31:33.04] was was pretty much ignored because
[L669] [31:36.00] digital signatures were very expensive
[L670] [31:37.84] in those days. I don't know what's being
[L671] [31:40.16] done now because you know computers are
[L672] [31:43.60] digital signatures are just computing
[L673] [31:45.60] and computing is you know is cheap. Uh
[L674] [31:49.68] but uh I remember at some point I
[L675] [31:53.04] happened to be communicating with
[L676] [31:55.20] someone who was an engineer at Boeing
[L677] [31:58.08] and I asked whether they knew about
[L678] [32:00.16] those results and he said yes when that
[L679] [32:04.64] he in fact uh was the one at Boeing who
[L680] [32:08.48] would read that paper and his reaction
[L681] [32:11.60] was oh we need four
[L682] [32:16.64] four computers.
[L683] [32:18.24] Uh but at any rate I realized that this
[L684] [32:21.04] was an important result and it should be
[L685] [32:24.48] well known and I had learned one thing
[L686] [32:27.92] from Dystra.
[L687] [32:29.76] uh Dy, you know, one of the things I
[L688] [32:31.52] learned from Dystra, he wrote this paper
[L689] [32:33.76] called the the dining philosophers
[L690] [32:35.92] problem. And that paper got a lot of
[L691] [32:39.04] attention, but the dining philosophers
[L692] [32:42.16] problem, I won't go into what it is, but
[L693] [32:43.92] I think the basic problem uh was not
[L694] [32:47.28] particularly interesting, but it had a
[L695] [32:49.52] cute story to it. It involved a bunch of
[L696] [32:52.56] philosophers sitting around a table with
[L697] [32:55.12] uh some funny kind of spaghetti that it
[L698] [32:57.28] required two forks and there was one
[L699] [32:59.12] fork between you know each fork would be
[L700] [33:01.68] shared with two people and uh but and I
[L701] [33:04.64] think realized it was because of that
[L702] [33:06.80] cute story that that problem was was
[L703] [33:09.76] popular. And so I decided that you know
[L704] [33:13.60] this this our work needed a cute story
[L705] [33:17.36] you know a nice story and I in invented
[L706] [33:19.52] Byzantine generals with the idea being
[L707] [33:21.84] that you have a group of you know for
[L708] [33:24.56] the for the one failure case you have
[L709] [33:27.12] four generals who have to agree whether
[L710] [33:29.04] or not to attack. uh and if they all
[L711] [33:32.48] attack
[L712] [33:34.00] uh they'll win the battle. But if only
[L713] [33:37.76] some of them attack or if even if three
[L714] [33:39.92] of them attack they'll win the battle.
[L715] [33:42.24] But if only two attack you know they
[L716] [33:44.88] would lose. But one of the the generals
[L717] [33:48.32] might be uh a traitor. And so how could
[L718] [33:52.00] you you know solve this problem? And so
[L719] [33:54.56] so it's phrased in terms of these
[L720] [33:56.40] generals having to communicate and
[L721] [33:58.24] decide whether to make the single
[L722] [34:00.32] decision whether to uh attack or or
[L723] [34:04.24] retreat. Um and you know I called it the
[L724] [34:08.88] Byzantine generals uh problem.
[L725] [34:11.76] >> I saw in your your uh notes about the
[L726] [34:15.36] problem that there was maybe a subset of
[L727] [34:18.32] the problem or a prior version that was
[L728] [34:20.16] called the Chinese general's problem or
[L729] [34:22.48] something like that.
[L730] [34:22.96] >> Oh yeah. that yeah I was uh there was a
[L731] [34:26.00] different problem that uh Jim Gray uh
[L732] [34:32.00] described uh as an impossibility result
[L733] [34:36.56] basically it's called the Chinese
[L734] [34:38.16] generals problem and I I won't bother
[L735] [34:40.56] going into what it is and so that gave
[L736] [34:43.12] me the idea of generals uh I actually
[L737] [34:46.80] initially thought of the idea of
[L738] [34:49.12] Albanian generals because at that time
[L739] [34:52.16] Albania was a black hole as far as the
[L740] [34:55.04] rest of the world was concerned. It was
[L741] [34:56.64] a communist regime, a part of the the
[L742] [34:58.88] Soviet uh block, but it was even more
[L743] [35:03.04] Soviet than the Soviet Republic and and
[L744] [35:05.28] and you know, more restrictive. So
[L745] [35:08.40] someone uh my boss said, "Well, you
[L746] [35:11.52] know, there are Albanians in the world,
[L747] [35:13.44] so shouldn't that so should have a
[L748] [35:15.92] different name?" And then I I realized
[L749] [35:18.08] that Byzantine there aren't any
[L750] [35:19.60] Byzantiums Byzantines around and that
[L751] [35:23.28] was the perfect name. So
[L752] [35:25.36] >> it's interesting to me in the story that
[L753] [35:27.84] because this isn't the first time the
[L754] [35:30.16] problem was specified but it was the
[L755] [35:33.04] first time that you had named it uh um
[L756] [35:36.08] gave it a good catchy name essentially
[L757] [35:38.00] and and uh you know added some
[L758] [35:40.08] additional results. What was it that you
[L759] [35:42.72] saw in that problem that made it
[L760] [35:44.80] interesting? Or rather like how do you
[L761] [35:46.64] know that a problem is worth putting
[L762] [35:49.36] extra time into? Oh, well this one it
[L763] [35:51.68] was because you know the it was obvious
[L764] [35:54.96] that people were going to be building
[L765] [35:56.88] that computers were going to fly our
[L766] [35:58.72] airplane fly airplanes and the reason in
[L767] [36:01.28] fact because was was that this was
[L768] [36:03.92] during the the time of the oil crisis in
[L769] [36:06.16] the 70s and that they knew people knew
[L770] [36:10.96] that they could build more
[L771] [36:12.56] energyefficient planes by reducing the
[L772] [36:15.84] size the the size of the control
[L773] [36:17.68] surfaces.
[L774] [36:19.20] But that made the plane aerodynamically
[L775] [36:21.44] unstable. Uh and a a pilot couldn't make
[L776] [36:25.44] the all the adjustments needed to, you
[L777] [36:28.08] know, to keep it flying, but a computer
[L778] [36:30.32] could. So it was clear the future was,
[L779] [36:33.76] you know, airplanes were going to be
[L780] [36:35.60] flying be flown by computers as they
[L781] [36:38.00] are, you know, today. uh and
[L782] [36:42.32] uh people didn't realize they thought
[L783] [36:45.44] that oh if you want to be able to
[L784] [36:47.92] tolerate one fault you just use three
[L785] [36:50.16] computers
[L786] [36:51.68] and they didn't realize that you know
[L787] [36:53.84] with arbitrary faults you need four and
[L788] [36:56.80] so that was a really important result
[L789] [36:58.80] and that's why I believe that it it
[L790] [37:00.64] needed to to be well known
[L791] [37:03.44] >> generally when you look at the problems
[L792] [37:05.04] that you are solving with your work Um,
[L793] [37:09.68] how'd you decide? Cuz if you're working
[L794] [37:11.44] at a company, you can decide based off
[L795] [37:13.84] of maybe the I guess the impact to the
[L796] [37:16.32] company like is it going to make more
[L797] [37:18.00] money or save cost or something like
[L798] [37:19.68] that. But I wonder in your work across
[L799] [37:22.32] your career um you know think about the
[L800] [37:27.04] bakery problem or some of your later
[L801] [37:29.92] work as well. How do you know it's it's
[L802] [37:32.72] so open-ended. How do you know which
[L803] [37:34.16] problems are uh the ones worthwhile?
[L804] [37:37.44] Throughout my career, I worked for
[L805] [37:39.60] private companies, you know, not, you
[L806] [37:42.16] know, not in academia or or for the
[L807] [37:44.96] government. Uh, and so some problems
[L808] [37:49.04] arose because of, you know, sometimes,
[L809] [37:53.20] you know, an engineer would have a
[L810] [37:54.72] problem and come come to me. And so, uh,
[L811] [37:58.56] you know, DIS Paxos, for example, was
[L812] [38:01.04] was a case of that that somebody
[L813] [38:02.88] actually wanted an algorithm to do what
[L814] [38:05.04] it did. You mentioned earlier Paxos and
[L815] [38:09.04] I know that's one of your your most
[L816] [38:11.20] famous uh works. Curious about the story
[L817] [38:14.40] behind maybe that paper and the problem
[L818] [38:17.04] you're solving.
[L819] [38:17.84] >> Well, the problem I was trying is
[L820] [38:19.68] exactly the same problem as I was
[L821] [38:21.68] solving in the the Byzantine general's
[L822] [38:24.32] work uh basically building a a fault
[L823] [38:28.48] tolerant state machine. But by that time
[L824] [38:32.16] it was you know the in the faults that
[L825] [38:34.96] interested industry were ones where
[L826] [38:37.76] failure meant that the computer just
[L827] [38:39.36] stopped the not not that it did
[L828] [38:42.32] arbitrary things. So uh the paxos is an
[L829] [38:46.40] algorithm for uh
[L830] [38:49.76] for for building fault tolerance systems
[L831] [38:52.72] for handling that class of faults. uh
[L832] [38:56.24] and
[L833] [38:57.84] the people I was working at was which
[L834] [39:01.12] the it was the deck circ
[L835] [39:04.88] was in which I joined in 1985 and they
[L836] [39:07.84] built a
[L837] [39:09.84] uh
[L838] [39:11.60] one of the first operating systems that
[L839] [39:15.28] uh was a a distributed operating system.
[L840] [39:20.16] Uh so that
[L841] [39:23.28] um basically everybody had the they
[L842] [39:26.72] basically these are the people who had
[L843] [39:28.88] come from Xerox Park and had invented
[L844] [39:31.44] personal computing but they also had the
[L845] [39:34.16] notion of distributed personal computing
[L846] [39:36.56] and they invented the Ethernet uh you
[L847] [39:39.60] know for that. So they basically all of
[L848] [39:42.48] the uh computers in the building were on
[L849] [39:46.96] a single Ethernet network and shared a
[L850] [39:50.64] common storage uh and they had an
[L851] [39:53.92] algorithm for maintaining consistency of
[L852] [39:56.00] that storage and I didn't believe well
[L853] [39:58.16] they didn't have an algorithm they had
[L854] [40:00.08] an operating system with code that did
[L855] [40:02.88] that um and
[L856] [40:06.56] I didn't believe that what they what
[L857] [40:09.76] they did was possible. Uh,
[L858] [40:13.76] namely I I didn't think um
[L859] [40:19.60] well I forget exactly why I didn't think
[L860] [40:22.56] it was possible but at any rate I
[L861] [40:25.44] started you know trying to uh come up
[L862] [40:27.84] with a a an impossibility proof and
[L863] [40:31.12] start solidity proof well and an
[L864] [40:33.36] algorithm to solve this would have to do
[L865] [40:35.12] this and in order to do this it would
[L866] [40:37.12] have to do that and at some point I
[L867] [40:39.84] stopped and said oh this isn't a proof.
[L868] [40:42.16] It it can't. This is an algorithm that
[L869] [40:43.92] does it.
[L870] [40:46.00] >> You said that they had code but not an
[L871] [40:49.68] algorithm.
[L872] [40:50.40] >> Yeah.
[L873] [40:51.12] >> Um what do you mean by that? when most
[L874] [40:54.16] people sit down and start writing
[L875] [40:55.76] programs that you know they start by
[L876] [40:58.24] thinking in terms of code
[L877] [41:01.04] and one of the things I learned fairly
[L878] [41:04.56] early in my career I don't remember
[L879] [41:06.48] exactly when that back in in the days
[L880] [41:10.24] when I started writing algorithms people
[L881] [41:13.44] talked about people were calling them
[L882] [41:15.68] programs and I was probably calling them
[L883] [41:18.32] programs too I mean I remember then at
[L884] [41:20.16] some point I realized that that wasn't
[L885] [41:22.40] wasn't talking about programs. I was
[L886] [41:25.84] talking about al interested in
[L887] [41:27.36] algorithms.
[L888] [41:28.88] Uh and an algorithm is something that's
[L889] [41:32.08] more abstract than a pro than than a
[L890] [41:34.08] program. U an algorithm can be you know
[L891] [41:37.44] a program is written in in some
[L892] [41:39.52] particular code. But an algorithm can be
[L893] [41:42.56] implemented if programs written in any
[L894] [41:45.12] any kinds of code. It's it's something
[L895] [41:46.72] that's that's at a higher level of of of
[L896] [41:50.88] abstraction. And of course I like that
[L897] [41:53.52] because abstraction is something I'm I
[L898] [41:55.52] was good at, you know, even without
[L899] [41:57.36] realizing that that's what I was doing.
[L900] [41:59.76] Uh
[L901] [42:01.76] and so
[L902] [42:05.04] what I've spent a large part of my
[L903] [42:07.68] career basically from maybe about you
[L904] [42:11.36] know 2000 or so onward uh was
[L905] [42:16.08] getting people who build concurrent
[L906] [42:18.08] systems
[L907] [42:20.08] uh to not just write code but to have an
[L908] [42:24.72] algorithm. Now a system does lots of
[L909] [42:27.60] things but there should be some kernel
[L910] [42:32.08] of the of the program that's that's
[L911] [42:36.80] involved with synchronizing the
[L912] [42:39.28] different processes
[L913] [42:41.92] or the distributed system the different
[L914] [42:43.68] computers and that code
[L915] [42:48.08] you know is very hard to get you know
[L916] [42:50.16] the you know that correct so you you
[L917] [42:53.36] don't want to think in terms of code
[L918] [42:54.96] because static coding, you know,
[L919] [42:57.60] conflates, you know, a lot of issues
[L920] [43:00.08] that are irrelevant to the concurrency
[L921] [43:02.48] aspect. And so you should be thinking,
[L922] [43:05.76] you know, first get an algorithm that
[L923] [43:08.40] does that synchronization and then
[L924] [43:10.72] implement that algorithm. I was looking
[L925] [43:14.24] at the Paxos paper and uh some of your
[L926] [43:17.20] notes about it and I saw that um there's
[L927] [43:20.96] a there's an eight-year gap between when
[L928] [43:24.24] you came up with the algorithm and when
[L929] [43:26.08] the the paper was actually published
[L930] [43:28.08] called Part-Time Parliament is the name
[L931] [43:30.32] of the paper. Why why is there an
[L932] [43:32.16] eight-year gap? Oh, well
[L933] [43:35.76] the re the referees originally said well
[L934] [43:38.88] this paper is okay you know not terribly
[L935] [43:41.44] important but fortunately Butler Lamson
[L936] [43:44.64] realized the importance of the algorithm
[L937] [43:48.08] and together with the idea of you know I
[L938] [43:51.28] guess you can implement anything because
[L939] [43:53.04] it's implementing a state machine uh and
[L940] [43:56.72] you know went about proceed uh
[L941] [43:58.72] procilitizing
[L942] [44:00.48] uh building your systems you know using
[L943] [44:03.52] paxos uh you know and and thinking in
[L944] [44:07.04] terms of state machines and uh so you
[L945] [44:11.28] know I wasn't uh so the idea was getting
[L946] [44:15.20] out so you know I was in no hurry to
[L947] [44:17.60] publish so you know I just let the paper
[L948] [44:20.96] sit and eventually uh there was a new
[L949] [44:24.48] editor that came along and uh
[L950] [44:29.04] uh
[L951] [44:30.72] he said that you know I think the status
[L952] [44:32.96] of the paper was that it was just uh you
[L953] [44:35.36] know it had been accepted but had no and
[L954] [44:37.76] needed revision and uh so he decided
[L955] [44:41.44] that yeah let's you know to to publish
[L956] [44:43.76] it and uh it was eventually published
[L957] [44:46.96] with little some a few things that uh to
[L958] [44:52.24] take well to to mention work that had
[L959] [44:55.28] been done in the in the in the uh
[L960] [44:58.00] interim and what I got is uh got a Keith
[L961] [45:03.76] Marzulo uh you know to do that part for
[L962] [45:07.44] me. Uh and uh so the story was that this
[L963] [45:11.36] manuscript this was that well the story
[L964] [45:13.76] about Paxos was that you know was a this
[L965] [45:16.32] happened you know centuries ago and you
[L966] [45:18.24] know this manuscript and uh I used that
[L967] [45:21.04] to the effect that you know when
[L968] [45:22.80] something you know the tales of
[L969] [45:24.48] something were I considered obvious and
[L970] [45:28.00] you know not interesting you know the
[L971] [45:30.40] the paper would say it's not clear how
[L972] [45:33.12] the Paxons what the Paxons did you know
[L973] [45:36.08] at this point but Um at any rate and uh
[L974] [45:40.16] so uh
[L975] [45:42.96] and Keith you know kept up the that idea
[L976] [45:47.36] that you know this was a you know a
[L977] [45:51.04] description of this ancient thing and
[L978] [45:52.96] and he wrote a you know a little prefix
[L979] [45:56.16] or a preface or something to to it and
[L980] [45:59.04] uh you know added maybe I think some uh
[L981] [46:02.00] references. I saw in your writing too
[L982] [46:04.88] when you were talking about presenting
[L983] [46:06.80] the paper initially,
[L984] [46:08.56] >> you even uh dressed up in like an
[L985] [46:10.96] Indiana Jones style archaeologist. Well,
[L986] [46:13.60] how did that go when you presented about
[L987] [46:15.36] this Paxos uh paper and algorithm?
[L988] [46:18.08] >> Well, I think the the lecture may have
[L989] [46:20.48] gone well, but uh I think nobody
[L990] [46:23.44] understood the algorithm where nobody
[L991] [46:24.96] understood the significance of the
[L992] [46:26.40] algorithm.
[L993] [46:27.44] >> It sounds like no one understood it
[L994] [46:29.04] except for Butler Lamson. What what did
[L995] [46:32.24] he see that made him unique? I guess.
[L996] [46:35.76] >> Well, he had a good understanding of
[L997] [46:37.68] building systems, you know, he really
[L998] [46:40.72] deserved his touring award. He was one
[L999] [46:43.12] of the original people at Xerox Park who
[L1000] [46:45.68] were building distributed uh personal
[L1001] [46:48.32] computing.
[L1002] [46:49.92] He and Chuck Thacker, I think, were
[L1003] [46:52.80] probably the two senior people, you
[L1004] [46:55.92] know, in that lab. I saw later there was
[L1005] [46:59.20] a paper which describes a new algorithm
[L1006] [47:02.80] which seems to solve the same problem.
[L1007] [47:04.80] The raft paper. I was wondering if you
[L1008] [47:07.84] read that and what your thoughts were on
[L1009] [47:09.52] on that versus Paxos. The authors of
[L1010] [47:12.88] that actually sent me a draft of the
[L1011] [47:15.20] original paper and I looked at it and
[L1012] [47:17.84] said uh I forget whether I said send it
[L1013] [47:23.20] back to me when you have an algorithm or
[L1014] [47:25.52] send that back to me when you have a
[L1015] [47:26.96] proof. I I forget which one it was and
[L1016] [47:30.40] uh you got the idea and they really they
[L1017] [47:32.88] they did write you know add a proof in
[L1018] [47:35.92] the paper or not. Uh yeah and I never
[L1019] [47:39.60] read future later versions and someone
[L1020] [47:42.80] whose judgment I value said you know had
[L1021] [47:45.92] read it and said that it's basically
[L1022] [47:47.76] it's it's the Paxos paper but no but
[L1023] [47:50.88] with some of the the tales left
[L1024] [47:55.28] unfinished by the Paxos paper uh by uh
[L1025] [47:59.52] you know filled some of the tales filled
[L1026] [48:01.76] in but they you know described it in a
[L1027] [48:06.16] in a very different Hey, the basic idea
[L1028] [48:09.44] of the what Paxos works is it's two
[L1029] [48:12.48] phases and you're trying to implement a
[L1030] [48:15.84] sequence of you know of decisions and it
[L1031] [48:20.00] turns out you can do the first phase
[L1032] [48:22.88] once
[L1033] [48:24.48] for a whole it involves a leader. So um
[L1034] [48:30.00] and the leader has to get elected. Uh so
[L1035] [48:33.60] but it turns out that you can do the
[L1036] [48:35.84] first uh phase once
[L1037] [48:39.84] uh and you don't have to do it again as
[L1038] [48:43.28] long as you have the same leader. Uh but
[L1039] [48:46.56] it's only the second part that you have
[L1040] [48:49.20] to do and then you have to elect the the
[L1041] [48:52.16] new leader if a new leader fails and do
[L1042] [48:55.04] the first part. So think about it in
[L1043] [48:57.44] those two phases. But the way people the
[L1044] [49:00.32] way engineers you know like to think
[L1045] [49:02.64] about it is well you do this you know
[L1046] [49:06.40] you talking about the first part the the
[L1047] [49:08.96] second phase you keep doing this uh
[L1048] [49:11.44] until the leader fa fails and then you
[L1049] [49:14.16] go back then you have to do this thing
[L1050] [49:16.00] so it's explaining it in the in the
[L1051] [49:19.52] opposite order uh and in fact you know
[L1052] [49:22.32] when you start it from from fresh the uh
[L1053] [49:25.92] you don't have to do the first uh uh the
[L1054] [49:29.68] first phase you can you basically what
[L1055] [49:32.32] what's done in the first phase could be
[L1056] [49:34.00] just built in into the initial state but
[L1057] [49:37.92] you know I think that that's the right
[L1058] [49:39.60] you know of those two phases the way to
[L1059] [49:41.68] understand it uh but you know the raft
[L1060] [49:46.80] people also had this idea that you know
[L1061] [49:48.96] raft is better because it's simpler and
[L1062] [49:51.76] I I must say that a lot of people say
[L1063] [49:53.52] that uh Paxos is hard to understand and
[L1064] [49:56.72] I don't understand why. I mean, I've
[L1065] [49:58.64] explained it to some people in five
[L1066] [50:00.48] minutes and they understood it. At any
[L1067] [50:02.56] rate, the raft people said that one of
[L1068] [50:04.32] the ideas were simpler because and they
[L1069] [50:07.52] even have, you know, taught, you know,
[L1070] [50:09.60] Paxos to one class and and uh the raft
[L1071] [50:13.92] to another and they took and then yes,
[L1072] [50:16.08] the people all the students said that
[L1073] [50:18.00] yes, it was more understandable. Uh the
[L1074] [50:21.12] interesting thing about it though is
[L1075] [50:22.96] that uh there was a bug discovered in
[L1076] [50:26.56] raft and fixed but I believe that the
[L1077] [50:31.44] algorithm that they found more
[L1078] [50:33.12] understandable was one with that bug.
[L1079] [50:37.04] So uh made me realize that uh you know
[L1080] [50:41.44] what most people you know what does
[L1081] [50:43.12] understanding mean and for me
[L1082] [50:47.04] understanding means you know you can
[L1083] [50:49.12] write a proof of it but what
[L1084] [50:51.60] understanding means for most people is
[L1085] [50:54.08] warm fuzzy feeling and you know the raft
[L1086] [50:57.84] description gave them you know more of a
[L1087] [51:00.00] warm fuzzy feeling because you know you
[L1088] [51:03.44] know that that was seems to be the way
[L1089] [51:06.00] you know programmers, you know, like to
[L1090] [51:08.32] think about the the algorithm, you know,
[L1091] [51:11.28] you know, the second phase, you know,
[L1092] [51:13.84] first until, you know, you get a failure
[L1093] [51:16.88] and uh
[L1094] [51:18.96] but the way I describe it is one that
[L1095] [51:22.72] helps you get a better understanding of
[L1096] [51:24.96] why it actually works.
[L1097] [51:26.96] >> So, yeah, we talked about a lot of your
[L1098] [51:28.56] papers. I know one of your other uh
[L1099] [51:31.12] contributions whether you knew it or not
[L1100] [51:33.44] at the time was latte and uh building
[L1101] [51:37.04] that and something that has impacted the
[L1102] [51:40.24] entire academic community. What's the
[L1103] [51:42.96] story behind wanting to build latte?
[L1104] [51:46.88] >> Oh, that was uh very simple. Um,
[L1105] [51:52.24] I was wanted I was in the process of
[L1106] [51:57.44] starting to write a book and uh
[L1107] [52:02.24] it was clear that tech was the basic uh
[L1108] [52:06.08] type setting system that one had to use.
[L1109] [52:08.80] But you know I felt that I would need
[L1110] [52:13.04] macros uh to make tech do what I wanted
[L1111] [52:16.48] it to do. And uh so
[L1112] [52:21.92] I decide figured with uh been a little
[L1113] [52:25.44] extra effort uh I could make the macros
[L1114] [52:28.48] usable by other people. The system I had
[L1115] [52:31.28] been using before tech it's called
[L1116] [52:32.96] scribe and uh that really had the basic
[L1117] [52:38.48] idea of scribe was that
[L1118] [52:43.28] you describe the logical structure of of
[L1119] [52:46.80] the document
[L1120] [52:48.96] not and the
[L1121] [52:51.44] and scribe will do the formatting. Well,
[L1122] [52:54.80] scribe didn't do that great a job of
[L1123] [52:56.48] formatting. Uh so, uh but
[L1124] [53:01.04] obviously, you know, I like the idea
[L1125] [53:04.32] abstraction that it's the ideas that
[L1126] [53:07.68] matter, not the text that ma, you know,
[L1127] [53:10.40] the the writing that matters, not the
[L1128] [53:13.12] type setting. And so,
[L1129] [53:16.48] um, I actually
[L1130] [53:21.36] at some point, uh, I met Peter Gordon,
[L1131] [53:24.80] Addison Wesley, uh, I'm not sure what
[L1132] [53:27.20] what you would call him, but he looks
[L1133] [53:28.64] for, you know, books to publish. And,
[L1134] [53:31.04] uh, he convinced me that I should write
[L1135] [53:34.24] a book on it. And those days, it never
[L1136] [53:37.84] occurred to me people would actually
[L1137] [53:39.20] spend money for a book about software.
[L1138] [53:41.92] But you know what the hell? And what he
[L1139] [53:45.60] did was he introduced me to uh a
[L1140] [53:50.80] typographic designer at uh Addison
[L1141] [53:53.20] Wesley who was responsible for really
[L1142] [53:56.72] for the typographic design that's in the
[L1143] [53:59.76] standard uh latex styles. You know,
[L1144] [54:03.20] basically I just did that in my quote
[L1145] [54:05.92] spare time. You know, took me six or
[L1146] [54:08.88] nine months or so. I I suppose the uh
[L1147] [54:12.32] statute of limitations has run out, but
[L1148] [54:14.40] I was really, you know, spent some time
[L1149] [54:16.64] working on that when I was allegedly,
[L1150] [54:19.60] you know, billing the time to some
[L1151] [54:22.32] project that had nothing to do with it.
[L1152] [54:26.32] >> On the topic of writing, you have a
[L1153] [54:28.96] quote that I really enjoy. It's if
[L1154] [54:31.04] you're if you're thinking without
[L1155] [54:32.88] writing, you only think you're thinking.
[L1156] [54:35.84] And I was curious to hear your thoughts
[L1157] [54:38.16] on what you mean by that.
[L1158] [54:40.80] >> Well, it was really meant for, you know,
[L1159] [54:43.76] people building computer systems. You
[L1160] [54:46.32] have an idea and you think it's going to
[L1161] [54:47.84] work. Uh or you have something that, you
[L1162] [54:50.48] know, you think is something that
[L1163] [54:52.24] somebody else will you want to use.
[L1164] [54:54.64] Well, write a description of it. Uh
[L1165] [54:56.88] there's an old maxim that I don't I
[L1166] [55:00.24] heard uh that is you know write the
[L1167] [55:04.16] instruction manual before you write the
[L1168] [55:06.08] program. a great advice. Uh I did not do
[L1169] [55:11.76] that uh with latte but it I definitely
[L1170] [55:16.08] when I was writing the book and I
[L1171] [55:19.84] discovered that something was hard to to
[L1172] [55:22.48] describe hard to explain that needed to
[L1173] [55:25.44] be changed and I made you know a number
[L1174] [55:27.84] of uh of changes to it uh as a result of
[L1175] [55:31.28] that but uh I didn't start at the
[L1176] [55:34.40] beginning with the instruction manual.
[L1177] [55:36.72] Why is writing conducive to good
[L1178] [55:39.20] thinking?
[L1179] [55:41.52] >> Because it's very easy to
[L1180] [55:45.20] uh
[L1181] [55:47.36] it's very easy to fool yourself.
[L1182] [55:50.08] Uh I mean that underlies my uh my whole
[L1183] [55:56.16] idea of of writing proofs. One thing I
[L1184] [55:59.44] learned is that you had to write a a
[L1185] [56:02.00] correctness proof of an concurrent
[L1186] [56:03.68] algorithm.
[L1187] [56:05.20] And when my algorithm was starting to
[L1188] [56:08.80] get more complicated,
[L1189] [56:11.20] the proofs started I started writ
[L1190] [56:14.56] PhD in math. I knew how to write proofs
[L1191] [56:16.96] and I was starting writing the proofs
[L1192] [56:18.96] the way I would normally do. And I
[L1193] [56:22.00] realized it just didn't work because
[L1194] [56:24.48] there were just so many details involved
[L1195] [56:27.28] and I just couldn't keep track of them
[L1196] [56:28.88] and whether I had done it. And so as a
[L1197] [56:32.56] computer science know how to deal with
[L1198] [56:34.24] concurrency
[L1199] [56:35.76] uh it's hierarchical structure and so I
[L1200] [56:39.36] devised this hierarchical structure
[L1201] [56:41.20] where a proof is uh you know is a
[L1202] [56:44.64] sequence of steps each of which has a
[L1203] [56:47.12] proof and the proof is either a par well
[L1204] [56:51.28] a proof is either a paragraph or a
[L1205] [56:53.60] statement a sequence of steps each with
[L1206] [56:55.84] its proof and that proof can be either a
[L1207] [56:59.60] parag graph or a sequence of steps with
[L1208] [57:01.84] its proof and you know so you break the
[L1209] [57:04.08] whole problem up into these smaller
[L1210] [57:05.76] pieces. So there's never any question of
[L1211] [57:08.72] you know where is this coming from. You
[L1212] [57:10.56] know you're stating that this step
[L1213] [57:12.56] follows from you know this step this
[L1214] [57:14.64] step this step this step and if it does
[L1215] [57:16.72] not follow from that step your proof is
[L1216] [57:19.04] wrong. The theorem might be correct but
[L1217] [57:21.20] but means your proof is wrong. Um well
[L1218] [57:24.96] you know so I've discovered that worked
[L1219] [57:27.04] great on writing my proofs of programs
[L1220] [57:30.16] but I decided to really you know I also
[L1221] [57:33.36] write proofs of theorems you know you
[L1222] [57:35.44] know uh you know think proofs that are
[L1223] [57:38.56] things that are you know more like
[L1224] [57:39.84] ordinary math and I started trying that
[L1225] [57:42.40] on them and I discovered it worked
[L1226] [57:45.84] beautifully. So when I started to to try
[L1227] [57:49.44] to convince mathematicians to write
[L1228] [57:50.96] these proofs uh I started in one small
[L1229] [57:55.28] seminar I went you know won't describe
[L1230] [57:57.28] what it was about but uh and I I
[L1231] [57:59.68] described this this proof through maybe
[L1232] [58:02.24] uh 20 mathematicians or something their
[L1233] [58:05.76] reaction shocked me
[L1234] [58:08.80] they became angry
[L1235] [58:11.44] I really thought that they might
[L1236] [58:14.24] physically attack me. So
[L1237] [58:17.68] I believe that what's going on is that
[L1238] [58:20.56] when pe I mean I believe that's totally
[L1239] [58:22.16] irrational and when people act
[L1240] [58:24.32] irrationally
[L1241] [58:26.16] it tends to be out of fear
[L1242] [58:29.20] and what I believe people are afraid of
[L1243] [58:32.48] is that mathematicians are afraid of is
[L1244] [58:35.76] that they're going to have to write
[L1245] [58:37.20] their proofs to convince a a computer
[L1246] [58:40.32] program and and in fact you know and I
[L1247] [58:44.72] give it a one of those talks I gave you
[L1248] [58:47.28] know I say very clearly this doesn't
[L1249] [58:49.52] have to be you don't have to be any more
[L1250] [58:51.28] formal than you do you can write the
[L1251] [58:54.24] exact same thing proof you know but it's
[L1252] [58:56.72] just a matter of organizing things and
[L1253] [58:58.88] it's very simple you know hierarchical
[L1254] [59:00.80] structure and then when you're using a
[L1255] [59:02.88] fact mention that you're using that
[L1256] [59:05.36] nothing about formalism or anything you
[L1257] [59:08.72] know after I gave that talk someone got
[L1258] [59:12.48] up and said I don't want to have to
[L1259] [59:14.56] write my proof my my proofs for a
[L1260] [59:17.12] computer program.
[L1261] [59:20.00] And in fact, it's more work doing that
[L1262] [59:23.04] because the reason it's more work is
[L1263] [59:26.48] that it reveals what you haven't said
[L1264] [59:30.48] and that there's steps in there that you
[L1265] [59:34.56] know, you may think they're obvious, but
[L1266] [59:36.80] you haven't written them down.
[L1267] [59:39.68] And if you believe something is correct
[L1268] [59:43.36] but don't really if you if you think you
[L1269] [59:46.32] know something but don't write it down,
[L1270] [59:49.36] you only think you know it. And that's
[L1271] [59:52.00] where errors come in. You know, that's
[L1272] [59:53.68] where that one-third of your paper's
[L1273] [59:55.52] errors can, you know, you know, uh, come
[L1274] [59:58.72] in because it really makes you honest.
[L1275] [01:00:02.24] When I look across your career, I think
[L1276] [01:00:04.72] you had a lot of contributions people
[L1277] [01:00:06.80] might expect might come from academia,
[L1278] [01:00:10.00] these papers and things, but you did uh
[L1279] [01:00:12.64] all of your work in industry. Why did
[L1280] [01:00:15.44] you not see yourself as a academic and
[L1281] [01:00:18.00] more of uh working for industry? Well, I
[L1282] [01:00:21.28] started out programming
[L1283] [01:00:23.84] uh and I eventually got jobs where took
[L1284] [01:00:27.92] me into what we now call computer
[L1285] [01:00:30.56] science. At the time I never even
[L1286] [01:00:32.88] realized that uh there was you know
[L1287] [01:00:35.76] there could be a computer a science of
[L1288] [01:00:37.60] computing. Uh it wasn't until you know
[L1289] [01:00:41.68] maybe until
[L1290] [01:00:43.60] mid to late '7s that I realized yes
[L1291] [01:00:47.12] there was a computer science and know as
[L1292] [01:00:49.12] a computer scientist. Um but it never
[L1293] [01:00:52.96] seemed to me that like computer science
[L1294] [01:00:55.28] was a an academic subject. At some point
[L1295] [01:00:58.64] I, you know, had to make a choice
[L1296] [01:01:00.88] between doing computer science and
[L1297] [01:01:03.84] without calling it computer science or
[L1298] [01:01:06.00] or teaching math at a at a university.
[L1299] [01:01:08.56] And I I chose for random fairly random
[L1300] [01:01:13.84] reasons to you do computer science. Uh
[L1301] [01:01:18.24] so it you know for the first
[L1302] [01:01:22.64] I don't know
[L1303] [01:01:26.40] well till maybe the mid80s or something
[L1304] [01:01:28.96] it just didn't seem to me that you know
[L1305] [01:01:31.20] you know computer science was something
[L1306] [01:01:33.76] that people needed to go to to a
[L1307] [01:01:36.88] university to learn. And uh I suppose
[L1308] [01:01:41.12] afterwards that I was sort of I guess I
[L1309] [01:01:45.04] I just didn't think it would be fun
[L1310] [01:01:46.64] teaching computer science. So
[L1311] [01:01:49.28] >> I saw in your your writing you had a
[L1312] [01:01:51.36] footnote that said somewhere that you
[L1313] [01:01:53.36] you you felt like a a failure at some
[L1314] [01:01:56.00] point because you you wanted to develop
[L1315] [01:01:58.64] this grand theory of concurrency and you
[L1316] [01:02:02.16] never discovered it. Um do do you still
[L1317] [01:02:05.04] feel that way or what are your thoughts
[L1318] [01:02:06.88] on that that footnote? lots of people
[L1319] [01:02:09.44] who you know a large percentage of the
[L1320] [01:02:11.20] people who were doing things like I was
[L1321] [01:02:12.80] doing which is not a large number of
[L1322] [01:02:14.16] people uh there's this notion that uh
[L1323] [01:02:19.28] they're looking for the touring machine
[L1324] [01:02:21.76] of concurrency you know the touring
[L1325] [01:02:24.32] machine was this abstraction which
[L1326] [01:02:27.12] really captured what computing was
[L1327] [01:02:30.96] uh and
[L1328] [01:02:34.00] they were looking for something that
[L1329] [01:02:36.40] would be the you know the touring
[L1330] [01:02:38.64] machine of of
[L1331] [01:02:41.68] concurrent computing
[L1332] [01:02:44.40] and
[L1333] [01:02:48.08] you know nobody succeeded. I mean there
[L1334] [01:02:50.56] are some people who think they've
[L1335] [01:02:51.68] succeeded. Uh the patronets are are
[L1336] [01:02:55.04] something that uh I guess I don't have
[L1337] [01:02:57.20] time to to explain but uh there was a
[L1338] [01:03:00.80] big it was big in the 70s. Uh, and I was
[L1339] [01:03:05.52] actually surprised to think that there's
[L1340] [01:03:06.96] still a large community of people doing
[L1341] [01:03:09.28] uh, patriets. But what I now realize is
[L1342] [01:03:12.80] that patriets and
[L1343] [01:03:15.68] most of the things that people were
[L1344] [01:03:17.12] doing was really language-based.
[L1345] [01:03:19.84] And I was never interested in languages.
[L1346] [01:03:22.32] I'm interested in what the language is
[L1347] [01:03:25.20] expressing.
[L1348] [01:03:27.12] And you know I realized in some sense
[L1349] [01:03:30.64] you know maybe I've realized what the
[L1350] [01:03:32.48] touring machine of of of computing is
[L1351] [01:03:35.12] state machines. Uh state machines are a
[L1352] [01:03:38.72] little bit different the way I now
[L1353] [01:03:39.76] describe them. They don't have commands.
[L1354] [01:03:41.52] They just have a state and a and a next
[L1355] [01:03:44.24] state relation. Uh even simpler than
[L1356] [01:03:47.60] talking about commands and and and
[L1357] [01:03:50.24] values and stuff. Uh and you know to me
[L1358] [01:03:54.88] you know that's the uh that's the
[L1359] [01:03:57.04] touring machine of of con of concurrency
[L1360] [01:04:00.16] but it
[L1361] [01:04:03.44] uh it it doesn't have the function that
[L1362] [01:04:06.56] that touring machines offer because it
[L1363] [01:04:09.36] it doesn't what touring machines do is
[L1364] [01:04:13.28] uh describe what's you know what's
[L1365] [01:04:16.40] possible
[L1366] [01:04:18.08] uh and state machines can describe
[L1367] [01:04:21.68] anything
[L1368] [01:04:23.20] including things that are not possible.
[L1369] [01:04:26.24] Uh and and in fact uh the there's a good
[L1370] [01:04:32.56] reason for that. Um
[L1371] [01:04:35.60] for example
[L1372] [01:04:37.36] uh when I describe a uh an algorithm I
[L1373] [01:04:42.40] will talk about you know the values of a
[L1374] [01:04:45.04] variable you know can be any integer.
[L1375] [01:04:48.48] Now you can implement the program where
[L1376] [01:04:50.24] you have any integer
[L1377] [01:04:52.32] uh but that makes the but talking about
[L1378] [01:04:58.88] you know computer integers would
[L1379] [01:05:00.88] complicate things unnecessarily.
[L1380] [01:05:03.28] The people have this funny idea that you
[L1381] [01:05:05.68] know because something is infinite it's
[L1382] [01:05:07.36] more complicated. They got it backwards.
[L1383] [01:05:10.08] Infinity was introduced to simplify
[L1384] [01:05:13.04] things. You know the first thing you
[L1385] [01:05:15.84] learn is arithmetic.
[L1386] [01:05:18.00] You're learning arithmetic with an
[L1387] [01:05:19.60] infinite number of integers because if
[L1388] [01:05:22.72] you restricted to a finite set of
[L1389] [01:05:24.96] integers, arithmetic becomes much more
[L1390] [01:05:27.28] complicated.
[L1391] [01:05:29.04] So you know the abstractions of
[L1392] [01:05:32.08] mathematics
[L1393] [01:05:34.24] uh which people find you know because
[L1394] [01:05:38.24] they don't have the proper training in
[L1395] [01:05:40.16] mathematics find you know difficult uh
[L1396] [01:05:44.00] are really what's simplifying things and
[L1397] [01:05:46.56] that's what you what you use this
[L1398] [01:05:48.24] mathematics the state machine is
[L1399] [01:05:50.40] described for me by me using mathematics
[L1400] [01:05:54.64] that's the right you know the the most
[L1401] [01:05:57.28] powerful way of doing
[L1402] [01:05:59.44] But
[L1403] [01:06:01.20] computer people and computer scientists
[L1404] [01:06:03.12] and programmers are really hung up on
[L1405] [01:06:06.40] languages
[L1406] [01:06:08.24] and so they are looking for you know
[L1407] [01:06:11.60] they invent all sorts of languages and
[L1408] [01:06:14.00] they're all describable and in fact if
[L1409] [01:06:17.44] you want to give them a semantics you
[L1410] [01:06:19.04] would do it in terms of a state machine
[L1411] [01:06:21.60] and they just think that this uh you
[L1412] [01:06:27.36] know this language ES improves your
[L1413] [01:06:29.60] thinking.
[L1414] [01:06:31.28] uh it doesn't you may I mean there are
[L1415] [01:06:35.12] reasons why you use computer languages
[L1416] [01:06:38.24] and you don't write your your programs
[L1417] [01:06:40.32] code in math and they involve basically
[L1418] [01:06:44.08] efficiency
[L1419] [01:06:45.92] but for understanding you know you can't
[L1420] [01:06:48.32] build math you can't beat math and you
[L1421] [01:06:52.48] know attempts to uh do it by something
[L1422] [01:06:56.32] that looks like a programming language
[L1423] [01:06:59.04] uh is is just the wrong way to to to
[L1424] [01:07:03.60] deal when you're trying to deal with
[L1425] [01:07:05.20] concurrency.
[L1426] [01:07:06.40] >> When I look at uh everything that you've
[L1427] [01:07:09.04] written and all the stories, there's
[L1428] [01:07:10.64] these little anecdotes. There's things
[L1429] [01:07:12.96] where you say things like you you never
[L1430] [01:07:15.44] considered yourself smart, but you
[L1431] [01:07:18.00] noticed that other kids had an awful
[L1432] [01:07:20.72] time understanding things or yeah,
[L1433] [01:07:22.96] there's a problem that you solved where
[L1434] [01:07:24.96] someone else had difficulties, but you
[L1435] [01:07:28.08] don't view your contribution as a
[L1436] [01:07:30.40] brilliant one or anything like that. And
[L1437] [01:07:33.52] that that uh doesn't connect with me
[L1438] [01:07:36.80] because you've also won a touring award
[L1439] [01:07:38.32] and done all these amazing things. So,
[L1440] [01:07:40.40] how could that be that you, you know,
[L1441] [01:07:43.84] just merely discover things and are are
[L1442] [01:07:46.24] not smart yet you've achieved so much?
[L1443] [01:07:48.80] >> Well, this general thing that, you know,
[L1444] [01:07:51.92] psychologists talk about uh is that when
[L1445] [01:07:58.48] someone is good at something, they don't
[L1446] [01:08:01.60] realize how they're good they are at it
[L1447] [01:08:04.24] because it's simple to them.
[L1448] [01:08:08.00] There's the opposite one that uh people
[L1449] [01:08:11.44] who are bad at something think they're
[L1450] [01:08:13.52] better than they are because they're bad
[L1451] [01:08:15.76] at it.
[L1452] [01:08:17.60] Or to put uh a little bit more
[L1453] [01:08:21.04] concisely,
[L1454] [01:08:22.72] stupid people think they're smart
[L1455] [01:08:24.32] because they're too stupid to realize
[L1456] [01:08:25.84] they're not. Uh my the gift that I have
[L1457] [01:08:30.32] is not in some sense raw intelligence.
[L1458] [01:08:33.60] It's abstraction
[L1459] [01:08:35.44] and it's only recently, you know, the
[L1460] [01:08:39.12] last 10 or so years
[L1461] [01:08:42.96] that I realized how much better I am at
[L1462] [01:08:46.24] that than other people, most other
[L1463] [01:08:48.88] people. At this point, you've
[L1464] [01:08:51.28] experienced so much and you when you
[L1465] [01:08:53.60] look back on your career. If you could
[L1466] [01:08:56.96] go back to yourself when you just
[L1467] [01:08:58.56] graduated college and give yourself some
[L1468] [01:09:01.20] advice knowing what you know now, what
[L1469] [01:09:03.76] would you say?
[L1470] [01:09:05.92] >> One thing I've learned fairly early in
[L1471] [01:09:08.80] my life is that I shouldn't waste time
[L1472] [01:09:14.48] trying to answer questions that I don't
[L1473] [01:09:16.56] have to answer.
[L1474] [01:09:18.48] I don't think about, you know, what I
[L1475] [01:09:20.24] should have done because uh that's a
[L1476] [01:09:22.72] question that I don't have to answer.
[L1477] [01:09:25.76] >> Thank you for listening to the podcast.
[L1478] [01:09:27.52] It's a passion project of mine that I've
[L1479] [01:09:29.76] really enjoyed building. Another passion
[L1480] [01:09:31.84] project that I've been working on kind
[L1481] [01:09:33.12] of in secret is building an ergonomic
[L1482] [01:09:35.68] keyboard that I wish existed and I
[L1483] [01:09:37.92] finally have a prototype. So, I'd love
[L1484] [01:09:39.60] to show you what we've built. It's ultra
[L1485] [01:09:42.40] low profile and ergonomic. and I
[L1486] [01:09:44.96] couldn't find anything like it on the
[L1487] [01:09:46.32] market. So, that's why we built it. I'll
[L1488] [01:09:48.16] put a link to the keyboard in the
[L1489] [01:09:49.52] description. You can take a look and
[L1490] [01:09:50.96] learn more about the project there. We
[L1491] [01:09:52.80] could definitely use your support. Also,
[L1492] [01:09:54.80] if you have any feedback for me about
[L1493] [01:09:56.40] the show, I'd love to hear it. Comments
[L1494] [01:09:58.80] on YouTube have led to guests coming on
[L1495] [01:10:00.88] like Ilia Gregoric and David Fowler. I
[L1496] [01:10:04.00] wasn't aware of them until someone
[L1497] [01:10:05.76] dropped a comment. Also, feedback in the
[L1498] [01:10:07.76] comments helped me learn to reduce the
[L1499] [01:10:09.44] number of cliffhers in the intros. So,
[L1500] [01:10:12.08] your comments definitely make a
[L1501] [01:10:13.36] difference. Please keep letting me know
[L1502] [01:10:14.80] what you'd like to see more of in the
[L1503] [01:10:16.32] show, and I'll see you in the next
[L1504] [01:10:17.68] episode.
