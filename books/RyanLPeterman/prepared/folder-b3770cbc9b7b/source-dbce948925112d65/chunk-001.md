Chunk 1; segments 1–375. 

# Dropbox’s Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling

Source ID: source-dbce948925112d65
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Dropbox’s_Former_Most_Senior_Eng_Building_Great_Systems_and_Advice_for_the_AI_Era_James_Cowling_en.txt
Video: https://www.youtube.com/watch?v=3XkmNSuHFmY

[L10] [00:00.00] The best engineering comes from a deep
[L11] [00:01.96] understanding of why.
[L12] [00:04.16] >> This is James Cowling, formerly the most
[L13] [00:06.64] senior engineer at Dropbox, and now CTO
[L14] [00:09.04] at Convex, and we dived into all the
[L15] [00:11.20] technical work of his career.
[L16] [00:12.92] >> It's not about getting a system to work.
[L17] [00:15.64] It's what do you do when it doesn't
[L18] [00:17.56] work? Simple systems are way harder to
[L19] [00:20.64] design than complex systems.
[L20] [00:22.24] >> He also had some interesting takes on
[L21] [00:24.16] technical leadership.
[L22] [00:25.44] >> Really, a team should be oriented around
[L23] [00:28.00] what problem do they solve? They should
[L24] [00:29.44] not care about the system that survives.
[L25] [00:31.92] >> I've had many friends whose promotions
[L26] [00:34.20] were rejected because their work wasn't
[L27] [00:36.56] complex enough.
[L28] [00:37.44] >> Yeah, it I mean, it almost angers me. I
[L29] [00:40.76] just like it so much.
[L30] [00:42.24] >> Is there any career advice that majorly
[L31] [00:45.24] changed in the last 5 years?
[L32] [00:47.04] >> Someone will argue back, "No, what you
[L33] [00:48.84] can do is get really good at using
[L34] [00:50.32] Cloud." Well, guess what? It's not very
[L35] [00:52.20] hard to use Cloud.
[L36] [00:53.84] >> Here's the full episode.
[L37] [00:55.67] >> [music]
[L38] [00:59.76] >> Well, first off, your PhD thesis was
[L39] [01:01.88] huge. It was It's 156 pages. I didn't
[L40] [01:04.76] know uh
[L41] [01:06.60] like theses I thought papers, you know,
[L42] [01:08.44] maybe 10 pages or something like that.
[L43] [01:10.28] It's its own book. Um
[L44] [01:12.88] >> It's very similar to Spanner,
[L45] [01:14.84] ultimately. And it was um what's funny
[L46] [01:17.36] is I did that work. It came out a little
[L47] [01:18.72] bit before Spanner, so I got a citation
[L48] [01:20.40] in the Spanner paper. But then Spanner
[L49] [01:22.44] came out and then everyone kind of
[L50] [01:24.68] everyone forgot about my paper.
[L51] [01:26.46] >> [laughter]
[L52] [01:27.88] >> You know, about the research, like if
[L53] [01:29.80] you could kind of describe the the
[L54] [01:31.96] problem that Granola was solving, and
[L55] [01:35.36] you know, how it solved it, those types
[L56] [01:37.40] of things. Could we talk about that?
[L57] [01:38.88] >> Yeah, absolutely. So, I mean, my my
[L58] [01:41.00] interest in my career has been um two
[L59] [01:44.32] two parallel threads. Um one has been
[L60] [01:47.24] just abstractions in general. The idea
[L61] [01:49.04] about how to build simple models for
[L62] [01:51.20] complex problems, and and I find that a
[L63] [01:53.04] very, very difficult and very
[L64] [01:54.48] intellectually was like um design
[L65] [01:57.04] exercise. How to design APIs, basically.
[L66] [01:59.52] And the other has been large-scale
[L67] [02:01.68] transactional systems. Um, big fan of of
[L68] [02:05.00] transactions. And transaction, you know,
[L69] [02:07.12] is do a bunch of things at once. And and
[L70] [02:10.36] again, I think transactions are just one
[L71] [02:12.00] of the most incredible abstractions
[L72] [02:13.76] we've invented because it allows us to
[L73] [02:15.80] to to manage the
[L74] [02:17.60] probably the most difficult problem in
[L75] [02:19.08] computer science, which is which is
[L76] [02:20.76] concurrency.
[L77] [02:22.20] Um, and so Granola is a um, you know,
[L78] [02:25.68] that was a long time ago in my life now,
[L79] [02:27.32] but it was a it was a it was an
[L80] [02:28.80] algorithm for how to do
[L81] [02:30.60] um, distributed transaction
[L82] [02:31.92] coordination. Um, and in particular,
[L83] [02:34.68] transactions that I described at the
[L84] [02:36.48] time as one-shot transactions. I'm not
[L85] [02:39.44] actually sure if that was a standard
[L86] [02:41.00] term at the time or whether I made it
[L87] [02:42.32] up. But, um, a one-shot transaction
[L88] [02:44.88] meaning you kind of send some code to
[L89] [02:47.52] the server and say run this function,
[L90] [02:50.60] all these reads, all these writes on
[L91] [02:52.96] two, three, whatever nodes at once.
[L92] [02:55.80] And how to make sure this commits
[L93] [02:56.96] atomically across multiple shards in a
[L94] [02:58.72] distributed system.
[L95] [03:00.40] But yeah, that was my my PhD thesis and
[L96] [03:02.76] my master's thesis was on a on a um,
[L97] [03:05.92] on on Byzantine fault tolerance. Uh, so
[L98] [03:08.52] a consensus protocol
[L99] [03:10.64] uh, in the presence of uh, malicious
[L100] [03:13.32] nodes. So, how to how to achieve
[L101] [03:14.72] agreement in state across multiple
[L102] [03:16.48] parties when there's um, malicious
[L103] [03:18.40] entities. And
[L104] [03:20.08] I guess the most well-known work I did
[L105] [03:22.44] um,
[L106] [03:23.32] as part of grad school was work on this
[L107] [03:25.24] paper called Viewstamped Replication
[L108] [03:26.80] Revisited. And that was uh, that was a
[L109] [03:29.16] paper on um,
[L110] [03:31.40] redefining a protocol called Viewstamped
[L111] [03:33.52] Replication, which was a
[L112] [03:35.24] predated Paxos a little bit. Very
[L113] [03:37.16] similar algorithm, Paxos, Raft,
[L114] [03:39.84] VR, they're all basic virtual synchrony,
[L115] [03:42.72] all basically the same thing. Um, and
[L116] [03:45.20] that was a that was a paper I wrote at
[L117] [03:46.88] the time, which ended up being I guess
[L118] [03:48.76] influential to a to a
[L119] [03:50.72] a few really great companies like Tiger
[L120] [03:52.16] Beetle.
[L121] [03:53.28] >> You mentioned transactions, and I saw in
[L122] [03:56.04] the paper there's this idea of an
[L123] [03:58.36] independent transaction. And I if I'm
[L124] [04:02.20] you know, understanding correctly, a lot
[L125] [04:03.80] of the efficiency in a in a distributed
[L126] [04:07.32] system is lost by needing to get
[L127] [04:10.00] consensus and to vote for consensus. And
[L128] [04:12.72] it I saw that in your research, you
[L129] [04:14.96] found out a way to avoid needing to vote
[L130] [04:17.24] to reach consensus. And uh you know, how
[L131] [04:19.28] did you do that?
[L132] [04:20.36] >> Yes. I mean, um a lot of people I think
[L133] [04:22.64] think about performance maybe from the
[L134] [04:24.84] wrong angle cuz they think of
[L135] [04:26.40] performance as a factor of just of this
[L136] [04:28.72] raw horsepower. You know, how fast are
[L137] [04:30.72] your disks? How fast is your network,
[L138] [04:32.44] etc.? And And no one has particularly
[L139] [04:35.40] faster disks or memory than anybody
[L140] [04:37.16] else. Um what really matters to um
[L141] [04:40.56] performance in a large-scale system is
[L142] [04:42.16] eliminating points of coordination.
[L143] [04:44.68] So, it's how to uh allow systems to
[L144] [04:46.92] progress
[L145] [04:48.44] without having um without having
[L146] [04:50.96] contention between parties. You know,
[L147] [04:53.32] where like you're basically reducing
[L148] [04:55.32] parallel throughput to serial throughput
[L149] [04:57.12] across large um numbers of transactions.
[L150] [04:59.40] And so, in Granola, we had this idea
[L151] [05:01.88] called a independent transaction. Again,
[L152] [05:04.24] that was the terminology of the time um
[L153] [05:06.80] where there were, you know, two entities
[L154] [05:09.24] are basically processing pure functions.
[L155] [05:11.64] So, they have independent state, and
[L156] [05:13.52] they will both come to the same
[L157] [05:14.80] conclusion as a result. And all they
[L158] [05:16.96] need to do then is serialize those
[L159] [05:19.08] transactions. So, they have to decide if
[L160] [05:21.24] it was to happen atomically across
[L161] [05:22.72] multiple nodes,
[L162] [05:24.48] what timestamp should it get? And And
[L163] [05:26.68] Granola, the paper was mostly about how
[L164] [05:28.64] to exchange these timestamps very
[L165] [05:30.44] efficiently. So, how to how to have
[L166] [05:32.56] multiple parties each propose a
[L167] [05:34.52] timestamp, and then choose, you know,
[L168] [05:37.40] the maximum of these, basically. So, you
[L169] [05:39.84] could safely serialize the transaction.
[L170] [05:42.28] Um and there's a lot more complexity
[L171] [05:43.56] that goes into this. But really, the
[L172] [05:45.32] focus there was about how to maximize
[L173] [05:47.52] throughput in a large distributed system
[L174] [05:49.76] with without resulting in the
[L175] [05:51.16] alternative, which is two-phase commit
[L176] [05:52.92] and two-phase locking.
[L177] [05:54.76] And two-phase commit uh with two-phase
[L178] [05:56.88] locking is basically the standard
[L179] [05:58.24] approach for when you want to have
[L180] [05:59.92] multiple nodes agreeing on the same
[L181] [06:02.72] thing where they both agree to lock
[L182] [06:04.40] their state, not process any other data,
[L183] [06:06.80] and then and then and then commit uh the
[L184] [06:08.80] transaction. Two-phase commit can be
[L185] [06:11.32] quite um one, it's can be low
[L186] [06:14.44] performance because you're blocking
[L187] [06:16.12] basically the systems for the duration
[L188] [06:17.44] of the transaction, and it can be high
[L189] [06:19.20] risk, too, because you are taking a
[L190] [06:21.56] dependency on another node. You
[L191] [06:23.88] basically blocked waiting for another
[L192] [06:25.32] node to return. And so, that was what
[L193] [06:27.28] Granola was. Now, um
[L194] [06:30.60] I've kind of, you know, it's funny you
[L195] [06:31.88] asked about Granola cuz I forgot about
[L196] [06:33.28] it. You know, that's so far in my in my
[L197] [06:35.44] history, I kind of forgot about that
[L198] [06:36.80] work, and I even forgot the phrase
[L199] [06:38.80] independent transactions, to be honest.
[L200] [06:40.60] So, it's it's it's great to hear you
[L201] [06:41.80] bring it up again, but I guess all this
[L202] [06:43.56] stuff does feed into all the work you do
[L203] [06:45.56] later on in interesting ways.
[L204] [06:47.96] >> When I think about distributed systems,
[L205] [06:50.52] I think about you're at a big company
[L206] [06:52.76] and you got a bunch of machines, but
[L207] [06:55.04] when you were at MIT building this
[L208] [06:56.72] thing, how did you build and test it?
[L209] [06:59.36] Did you
[L210] [07:00.84] you know, were there spare machines that
[L211] [07:02.84] the college had or was this in the
[L212] [07:04.64] cloud?
[L213] [07:05.28] >> Yeah, it's it's this was a long time ago
[L214] [07:07.36] now. I'm I'm showing my age. This was
[L215] [07:08.96] pretty early in the days of AWS, and so
[L216] [07:12.36] we had a a rack of servers in our office
[L217] [07:15.04] that we could use, and I was fortunate
[L218] [07:16.60] enough to be at MIT where we could
[L219] [07:18.08] afford a rack. Um and there was also um
[L220] [07:22.48] a service called PlanetLab, and
[L221] [07:23.92] PlanetLab was like a big communal set of
[L222] [07:26.20] nodes that um you could academics could
[L223] [07:29.60] use to run to run uh tests on. But,
[L224] [07:32.04] PlanetLab was a communal system, and so
[L225] [07:34.48] it was continually having problems. I
[L226] [07:36.88] mean, it's just a free-for-all. And so,
[L227] [07:38.88] for the longest time, I would just sleep
[L228] [07:40.44] next to my desk and
[L229] [07:42.96] wake up whenever Planet Lab was free cuz
[L230] [07:45.32] you know, you need to run some
[L231] [07:46.36] benchmarks. These days you just spin
[L232] [07:48.52] something up on AWS, but then I would
[L233] [07:50.20] yeah, I would sleep next to my desk and
[L234] [07:52.32] I would wake up in the middle of the
[L235] [07:53.52] night or random times and check Planet
[L236] [07:55.64] Lab status and then kick off a
[L237] [07:57.16] benchmarking job.
[L238] [07:58.68] Now,
[L239] [07:59.76] this was right at the cusp
[L240] [08:02.96] at when I think in some respects Google
[L241] [08:04.68] ruined systems research.
[L242] [08:06.48] And I say that with affection and
[L243] [08:08.12] respect to Google
[L244] [08:09.52] um because before then
[L245] [08:12.00] most of the research was coming out of
[L246] [08:14.56] academia.
[L247] [08:15.72] And a lot of distributed systems
[L248] [08:16.72] research was done on smaller scales and
[L249] [08:18.80] a lot of the um the value prop was the
[L250] [08:21.76] ideas.
[L251] [08:22.92] So like hey, I wrote a paper. Here's an
[L252] [08:24.60] interesting new idea and yeah, it's all
[L253] [08:27.20] in theory. And so the the value that
[L254] [08:29.76] came out of it was the idea.
[L255] [08:31.96] Around about this time you started
[L256] [08:33.24] seeing papers out of Google, Amazon and
[L257] [08:35.08] these various companies where it wasn't
[L258] [08:38.00] necessarily a paper about an idea. It
[L259] [08:40.08] was a paper about a system. Hey, I built
[L260] [08:42.40] this giant system. It has a whole bunch
[L261] [08:44.64] of features, some of which are
[L262] [08:46.08] interesting, some of which are not and
[L263] [08:47.84] by the way it powers Gmail or whatever.
[L264] [08:52.28] And that that um kicked off a pretty
[L265] [08:55.04] interesting transition because at that
[L266] [08:57.04] point then
[L267] [08:58.40] you know, um program committees
[L268] [09:00.16] reviewing papers started to expect to
[L269] [09:02.04] see realistic benchmarks.
[L270] [09:04.56] That frankly grad students are not able
[L271] [09:06.20] to at least at the time produce. I mean,
[L272] [09:08.44] we I wasn't running Gmail on my system.
[L273] [09:11.88] Um and I think it did in some respects
[L274] [09:14.80] obscure
[L275] [09:16.48] intellectual ideas, right? Because I'm
[L276] [09:18.76] all for like papers about systems, but I
[L277] [09:21.28] think there's also value in a paper
[L278] [09:22.48] about an idea.
[L279] [09:23.68] You know, it's not we built this big
[L280] [09:25.24] thing and it works and up to you to
[L281] [09:27.28] figure out what's interesting about it,
[L282] [09:29.00] but instead here's a new thing you know,
[L283] [09:30.36] there's a paper you know, an old paper
[L284] [09:32.60] just called leases,
[L285] [09:34.32] right? Where someone invented the idea
[L286] [09:36.20] of a time-based lock, and it's just a
[L287] [09:37.84] paper called leases.
[L288] [09:39.92] And though that was a cool era of
[L289] [09:41.60] systems research. I think a lot of it
[L290] [09:43.52] now has shifted towards uh industrial
[L291] [09:46.20] research, which is you know, people are
[L292] [09:47.32] building stuff
[L293] [09:48.84] with, you know, for practical purposes.
[L294] [09:51.32] Whereas I think it's hard for academia
[L295] [09:53.00] to compete on pragmatism. And you know,
[L296] [09:55.68] academia is really a great place to do
[L297] [09:58.04] impractical work.
[L298] [09:59.76] >> When you look back on, you know, you
[L299] [10:01.84] getting the PhD in academia, being
[L300] [10:04.16] enabled to completely explore an idea
[L301] [10:06.92] versus going into industry, but maybe
[L302] [10:09.20] doing
[L303] [10:10.44] you know, maybe you worked on Spanner at
[L304] [10:11.84] Google or something like that. You know,
[L305] [10:14.36] when you look back, which path do you
[L306] [10:16.48] think would be better and why?
[L307] [10:18.52] >> I think there's a bit of a misconception
[L308] [10:19.76] a lot of folks have about PhD programs.
[L309] [10:22.24] I think a lot of students are like
[L310] [10:23.60] high-achieving students in college, and
[L311] [10:25.60] they think that the PhD program is like
[L312] [10:27.28] college plus plus. It's like, "Hey, I
[L313] [10:29.32] like learning things, and so I'm going
[L314] [10:31.48] to go do a PhD." But it's not. A PhD is
[L315] [10:34.68] training to be a researcher.
[L316] [10:37.16] And for most people, they shouldn't do
[L317] [10:40.00] that. If someone wants to be a
[L318] [10:40.92] professional software engineer,
[L319] [10:42.96] they probably shouldn't spend their time
[L320] [10:44.68] training to be a researcher.
[L321] [10:46.84] But with a really important caveat.
[L322] [10:49.84] I think there's a really um interesting
[L323] [10:52.16] and challenging developmental experience
[L324] [10:53.92] you go through in in a in the PhD
[L325] [10:55.80] program at a top university at least,
[L326] [10:58.00] which is you get to a certain point in
[L327] [10:59.44] time when you have a problem that you're
[L328] [11:01.40] facing that no one else in the world
[L329] [11:03.68] knows the answer to.
[L330] [11:05.00] You have a problem that you are the
[L331] [11:06.96] world expert on, and you can't you know,
[L332] [11:08.76] you can chat about it with folks, but
[L333] [11:10.28] you can't ask your advisor cuz your
[L334] [11:11.68] advisor doesn't know either, right? So
[L335] [11:13.56] you're faced with these difficult
[L336] [11:14.88] challenges that there's you can't read a
[L337] [11:16.96] book, you can't, you know, you can't ask
[L338] [11:19.44] chat GPT, right? And so you're forced to
[L339] [11:21.80] go through a quite difficult and frankly
[L340] [11:24.20] emotionally challenging experience of
[L341] [11:27.28] being unsure, being uncertain, and and
[L342] [11:30.00] learning to think for yourself.
[L343] [11:32.16] I think that is really valuable for all
[L344] [11:35.60] engineers. I think that was really
[L345] [11:37.52] really valuable in my career.
[L346] [11:39.40] Um I do see a lot of folks early in
[L347] [11:42.16] their career
[L348] [11:43.52] um
[L349] [11:44.56] think that all knowledge comes from
[L350] [11:46.56] reading or you know, absorbing it from
[L351] [11:49.12] someone else or that there's a right way
[L352] [11:50.64] to do things. But I think being in a PhD
[L353] [11:53.20] program um
[L354] [11:55.32] or being faced with really demanding
[L355] [11:57.44] open questions does train your mind to
[L356] [12:00.16] be comfortable with that discomfort. Um
[L357] [12:03.32] I mean, look
[L358] [12:05.04] I feel um
[L359] [12:06.92] I feel a little bit lucky that I went
[L360] [12:08.60] through a grad school without LLMs
[L361] [12:10.80] existing.
[L362] [12:12.08] Because I had to deal with this
[L363] [12:13.52] uncertainty. I I There was There was no
[L364] [12:15.92] There was no crutch to help me out,
[L365] [12:17.44] which I think was very valuable. So, um
[L366] [12:21.44] Ah, I mean, a lot of a lot of
[L367] [12:24.28] you know, if you want to If you want to
[L368] [12:25.28] be a researcher, go go do a PhD.
[L369] [12:28.40] If you want to build stuff, go build
[L370] [12:30.88] stuff.
[L371] [12:31.96] You know? And I And you know,
[L372] [12:34.68] since leaving academia, I've done a lot
[L373] [12:36.88] of work that I I guess one could call
[L374] [12:38.92] innovative. Like it it advanced the
[L375] [12:41.20] industry in certain ways and did novel
[L376] [12:43.64] stuff, but our goal was never research.
[L377] [12:46.16] Our goal was just to solve problems. And
[L378] [12:48.04] I think that's the difference. I mean,
[L379] [12:49.64] in academia, your goal is to advance
[L380] [12:51.96] knowledge. Um in in industry, your goal
[L381] [12:54.96] is to solve problems.
[L382] [12:56.72] Um and
[L383] [12:58.40] I gravitate more towards the solving
[L384] [13:00.68] problems.
