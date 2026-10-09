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
[L385] [13:01.68] And I find that a more comfort-
[L386] [13:03.08] comfortable environment within which to
[L387] [13:04.60] work.
[L388] [13:05.72] >> Going to your time in in industry, you
[L389] [13:08.88] know, at Dropbox, you became the most
[L390] [13:10.60] senior engineer at the company. And
[L391] [13:13.04] looking through all the projects that
[L392] [13:14.68] you did, I had a series of just
[L393] [13:18.32] technical curiosities. I saw this idea
[L394] [13:20.76] early in your career about multi-homing,
[L395] [13:22.56] and I wasn't familiar with that concept.
[L396] [13:24.76] What What is multi-homing? What's the
[L397] [13:26.80] problem it
[L398] [13:28.08] >> Yeah, I mean multi-homing is the ability
[L399] [13:30.36] to have data in two locations, two
[L400] [13:32.44] homes. And multi-homing can be valuable
[L401] [13:35.76] for a variety of reasons. Um one is
[L402] [13:39.00] called, you know, primary secondary or,
[L403] [13:41.28] you know,
[L404] [13:42.12] lazily replicated multi-homing whereby
[L405] [13:44.80] all rights commit authoritatively in one
[L406] [13:47.56] region and get replicated to a secondary
[L407] [13:49.96] region. Um and so this is normally used
[L408] [13:53.04] for, you know, business continuity. You
[L409] [13:55.12] know, one thing we did at Dropbox we
[L410] [13:56.64] made sure that if the entire West Coast
[L411] [14:00.04] blew up, you know, which hopefully
[L412] [14:01.52] wouldn't happen, Dropbox would keep
[L413] [14:03.12] running because there would be enough
[L414] [14:04.76] the data would be replicated in other
[L415] [14:05.96] regions. But with a window of
[L416] [14:07.76] vulnerability, with a window of time
[L417] [14:09.32] where there may be some some some data
[L418] [14:11.60] lost.
[L419] [14:12.84] Um so that is, you know, that's kind of
[L420] [14:15.12] primary secondary replication or
[L421] [14:17.00] multi-homing. There's something else
[L422] [14:18.64] called active active multi-homing where
[L423] [14:21.16] there is truly an authoritative copy of
[L424] [14:23.52] the data in multiple locations. So
[L425] [14:25.76] basically when you, for example, write
[L426] [14:27.88] to a system, you don't externalize that
[L427] [14:30.44] right as having succeeded until it has
[L428] [14:32.64] landed in all the regions.
[L429] [14:34.72] Um and so, for example, in the the
[L430] [14:36.68] storage system at Dropbox, the block
[L431] [14:38.16] storage system, we truly had a a
[L432] [14:40.28] multi-region replicated system where we
[L433] [14:42.72] could take down an entire region, say
[L434] [14:44.44] take down the
[L435] [14:45.76] a region in Ashburn, Virginia where
[L436] [14:48.68] everyone's data centers are and there'd
[L437] [14:50.80] be zero downtime for the company and the
[L438] [14:52.56] data was still safe in multiple regions.
[L439] [14:55.12] I think multi-homing
[L440] [14:57.84] is something a lot of engineers aspire
[L441] [14:59.68] to work on cuz it's it seems like
[L442] [15:03.84] the right thing to do.
[L443] [15:05.56] But I think the reality is for most
[L444] [15:07.20] companies it is not.
[L445] [15:09.32] For most companies it's not because
[L446] [15:10.40] there's very high cost there's very high
[L447] [15:12.32] cost latency costs for this. Very high
[L448] [15:14.48] um because the speed of light is just
[L449] [15:16.52] not getting faster. The speed of light
[L450] [15:18.04] is fixed.
[L451] [15:19.24] And if you have to, you know,
[L452] [15:21.12] synchronously write data across multiple
[L453] [15:23.20] regions in the United States, you're
[L454] [15:25.04] going to have, say, 60 milliseconds in
[L455] [15:27.76] the commit path of your protocol, which
[L456] [15:29.72] for most applications is not tenable.
[L457] [15:31.88] Uh, so there is a lot of desire, um, you
[L458] [15:34.44] know,
[L459] [15:35.20] a lot of engineering teams reach out for
[L460] [15:36.80] kind of advice on how to adopt
[L461] [15:38.56] active-active multi-homing for the
[L462] [15:39.96] company. I would normally say, "Don't do
[L463] [15:42.48] it." I would normally say,
[L464] [15:44.76] "Frankly, if US East is down, if Amazon
[L465] [15:47.12] is down that day,
[L466] [15:49.00] that's okay. If Amazon's down that day,
[L467] [15:51.92] your your company will be down. That's a
[L468] [15:54.12] shame, right? But by avoiding that
[L469] [15:57.08] complexity, you're going to be able to
[L470] [15:58.84] move much faster and build a much better
[L471] [16:00.24] product. And so,
[L472] [16:02.04] in my mind, systems is all about
[L473] [16:03.44] trade-offs and making the right ones.
[L474] [16:05.72] I would generally recommend most people
[L475] [16:08.68] do not make the trade-off to have
[L476] [16:10.72] partition tolerance or or or
[L477] [16:12.60] multi-region availability.
[L478] [16:14.48] Even though for a company like Dropbox,
[L479] [16:15.72] yes, that does make sense. When you When
[L480] [16:17.32] you When your When your job is storing
[L481] [16:19.44] data and you have several exabytes of it
[L482] [16:22.00] and and hundreds of millions of
[L483] [16:23.40] customers, I think that's when it's when
[L484] [16:25.20] it starts to make sense.
[L485] [16:26.64] >> So, it's it's just another term for, I
[L486] [16:28.96] guess, data replication and having it
[L487] [16:31.48] available on other regions. Okay. I
[L488] [16:33.88] imagine also, I mean, the cost of
[L489] [16:35.60] storage is a concern. How many replicas
[L490] [16:38.28] would you keep for something? Like,
[L491] [16:40.08] let's just say I stored something in
[L492] [16:41.36] Dropbox. It's my document. Is that
[L493] [16:45.08] on on the order of one or two or is
[L494] [16:47.20] there multiple?
[L495] [16:47.96] >> No, it's on the order of many, many. And
[L496] [16:50.04] so, um,
[L497] [16:51.56] so, if you were to store a file in
[L498] [16:53.84] Dropbox,
[L499] [16:55.92] I modeled the storage to be, as we
[L500] [16:58.08] advertise, at least 12 nines of
[L501] [16:59.68] durability. Internally, the models look
[L502] [17:02.24] around 24 nines of durability. And so,
[L503] [17:04.84] that means the data is secure with
[L504] [17:07.24] 99.99999%
[L505] [17:10.12] where there's 24 nines, right? Which
[L506] [17:12.08] means, at least according to the model,
[L507] [17:15.24] you know, the universe will be extinct
[L508] [17:17.36] before any data is lost. Right. And and
[L509] [17:20.16] the way that is done is by a combination
[L510] [17:22.16] of of what's called erasure coding. So,
[L511] [17:24.52] erasure coding is how you take a
[L512] [17:26.28] several blocks of data and combine them
[L513] [17:27.92] together in it with an encoding scheme
[L514] [17:30.36] and spread them around in in different
[L515] [17:32.12] locations. At that scale, at Dropbox
[L516] [17:34.28] scale, you're you're taking things into
[L517] [17:35.48] consideration like putting data in
[L518] [17:36.80] different racks, different rows of a
[L519] [17:39.60] data center because they're on different
[L520] [17:40.64] power feeds. You're taking into
[L521] [17:42.28] consideration different eras of hard
[L522] [17:45.00] drives and different manufacturers of
[L523] [17:46.64] drives because they can have correlated
[L524] [17:48.04] failure patterns. And then replication
[L525] [17:50.12] across regions.
[L526] [17:51.84] Um so, you know, you you could be
[L527] [17:53.56] looking at
[L528] [17:54.76] 27 fragments, for example. That doesn't
[L529] [17:57.72] mean you're storing 27 times the data.
[L530] [17:59.72] It's it's kind of encoded in in in many
[L531] [18:01.64] regions. But, it's really uh the
[L532] [18:03.60] replication schemes get really quite
[L533] [18:05.24] sophisticated at that point. And we
[L534] [18:06.92] actually had our own
[L535] [18:08.72] custom encoding matrix we had developed.
[L536] [18:10.92] It's called a Vandermonde matrix where
[L537] [18:13.48] you kind of take a bunch of data and you
[L538] [18:15.28] combine it together to produce outputs.
[L539] [18:18.76] And we would plug in some variables like
[L540] [18:21.00] how much do discs cost? How much does
[L541] [18:23.32] network bandwidth cost?
[L542] [18:25.32] Because there's a trade-off. You can
[L543] [18:26.64] either store If you don't want to lose
[L544] [18:27.96] your data, you can store more copies on
[L545] [18:29.84] more discs.
[L546] [18:31.40] Or you can store fewer copies. And
[L547] [18:33.72] anytime a disc fails, you re-replicate
[L548] [18:36.48] it really fast. And re-replicating
[L549] [18:38.52] really fast costs
[L550] [18:40.12] disk band costs network bandwidth.
[L551] [18:42.24] So, these kind of variables go into this
[L552] [18:43.76] equation. Uh it ends up being an
[L553] [18:45.84] extremely complex field of endeavor, but
[L554] [18:48.48] it's kind of abstracted away into a part
[L555] [18:50.36] of the system that doesn't doesn't leak
[L556] [18:51.84] into anywhere else.
[L557] [18:53.28] >> So, with erasure encoding, my my
[L558] [18:55.92] document in Dropbox is fragmented into a
[L559] [18:59.24] bunch of different chunks of data and
[L560] [19:01.12] loaded potentially from many different
[L561] [19:02.64] machines.
[L562] [19:03.48] >> Yes, absolutely.
[L563] [19:04.80] >> It
[L564] [19:05.96] I mean, the the first thought I have is
[L565] [19:08.20] now there's uh I might be waiting there
[L566] [19:10.48] and one of the 27 machines is slow and I
[L567] [19:14.64] can't look at the whole doc. So, how do
[L568] [19:16.44] you prevent against that?
[L569] [19:17.56] >> It's actually faster than not
[L570] [19:19.84] replicated. Because if you imagine I'll
[L571] [19:22.28] I'll pick a
[L572] [19:23.60] uh
[L573] [19:24.36] a simplified example.
[L574] [19:26.04] Imagine this is not the encoding scheme
[L575] [19:28.20] Dropbox uses, but imagine to reconstruct
[L576] [19:30.36] a file, you have to read six out of nine
[L577] [19:33.36] fragments.
[L578] [19:35.08] Right? So, if you read six out of nine
[L579] [19:37.32] fragments, you can just ask all nine
[L580] [19:40.60] and reconstruct and return the data as
[L581] [19:42.28] soon as you've heard from the first six.
[L582] [19:44.64] It's actually
[L583] [19:45.92] faster and you can construct these
[L584] [19:47.68] encoding matrices. So, if it is it's
[L585] [19:49.68] actually faster to have a ratio coded
[L586] [19:51.36] data than than not.
[L587] [19:53.28] >> I see. Okay, so you can
[L588] [19:55.24] like oversubscribe, over request, and
[L589] [19:58.20] then you complete on a portion of them
[L590] [20:01.36] being received.
[L591] [20:02.04] >> Yes. Now,
[L592] [20:03.24] in in practice, it was a bit more
[L593] [20:05.16] complex than that. We'd often have a
[L594] [20:06.52] copy in a single disk to provide fast
[L595] [20:08.64] access. We'd often try to make sure that
[L596] [20:11.04] you could serve your data out of a
[L597] [20:12.64] region close to your home region. So,
[L598] [20:14.88] we'd make sure that your data was mostly
[L599] [20:16.64] served with low latency. But, if that
[L600] [20:19.00] region had failed, you could reconstruct
[L601] [20:20.76] it from the remaining regions. So,
[L602] [20:22.28] there's a lot of um
[L603] [20:24.24] a lot of people, you know, there's a lot
[L604] [20:25.24] of uh talk about building your own
[L605] [20:27.68] infrastructure and and you can save
[L606] [20:29.68] money by moving off the cloud.
[L607] [20:32.08] Um
[L608] [20:32.80] almost definitely you can't. Unless you
[L609] [20:36.24] you unless you either you have very
[L610] [20:37.96] small requirements or very fixed
[L611] [20:40.32] requirements or very very very heavy
[L612] [20:42.96] investment. Cuz if you want to compete
[L613] [20:44.72] with Amazon, if you want to build a more
[L614] [20:46.08] efficient storage system than Amazon,
[L615] [20:48.44] you have to have a supply chain team
[L616] [20:50.12] that's working with you know, Western
[L617] [20:51.96] Digital and Seagate constantly and
[L618] [20:53.96] negotiating on prices of disks and
[L619] [20:55.72] buying shipments at certain time and and
[L620] [20:57.92] capacity teams and and data center
[L621] [21:00.52] teams. Like there's a lot of work that
[L622] [21:02.44] goes into like
[L623] [21:03.88] optimizing this. Because ultimately, our
[L624] [21:06.08] desire was to use the disks to 90-95%
[L625] [21:10.36] of
[L626] [21:11.32] the disk size to to maximize storage
[L627] [21:14.16] efficiency. To put it this way, I mean
[L628] [21:15.92] that was
[L629] [21:16.88] you know, I guess it's a ballpark
[L630] [21:18.20] figure, a billion-dollar project.
[L631] [21:20.32] Right? And was you know, and it I think
[L632] [21:22.76] at the time, as far as I know, was the
[L633] [21:24.44] largest ever data migration in history,
[L634] [21:27.36] I think at the time. And so, extremely
[L635] [21:29.92] large engineering project with very high
[L636] [21:32.92] technical investment. So, yes, if you
[L637] [21:34.84] have that scale and you have the
[L638] [21:36.80] engineering team to do it and you're
[L639] [21:39.88] willing to keep innovating, if you're
[L640] [21:42.12] willing to keep
[L641] [21:43.76] um optimizing and investing effort in
[L642] [21:45.60] it, then yes, you can do it.
[L643] [21:47.64] Um but I think the real I mean, the
[L644] [21:49.40] cloud has been an incredible innovation,
[L645] [21:51.12] right? Most people are not experts at
[L646] [21:52.64] this, and most people should not be
[L647] [21:54.20] experts at this. You know, most people
[L648] [21:55.68] should focus on their applications.
[L649] [21:57.64] >> When you say that most people shouldn't,
[L650] [21:59.76] my immediate thought was but one of the
[L651] [22:02.12] big projects you worked on at Dropbox
[L652] [22:04.40] was my migrating away from S3.
[L653] [22:06.96] >> Yes, yes.
[L654] [22:07.52] >> So,
[L655] [22:08.28] um you know, why why did Dropbox migrate
[L656] [22:10.32] away from S3?
[L657] [22:12.36] >> Yeah, that was a desire of the company
[L658] [22:13.68] for a long time. You know, from even
[L659] [22:15.44] before I was there. So, I started at
[L660] [22:16.88] Dropbox in 20
[L661] [22:18.40] uh 2012. Um and I spoke to to Drew, the
[L662] [22:21.96] Dropbox founder, I think in 2010 about
[L663] [22:24.16] this project. And so, I think there was
[L664] [22:25.92] a desire to
[L665] [22:27.76] um control the destiny of the company
[L666] [22:30.68] from a strategic perspective. I mean, at
[L667] [22:32.12] the time it was before Dropbox kind of
[L668] [22:34.56] reshaped itself as being more about
[L669] [22:36.04] collaboration. You know, at the time it
[L670] [22:37.76] was a file sync and share category. That
[L671] [22:39.64] was that was the that was the that was
[L672] [22:41.24] the market sector, you know? And so, and
[L673] [22:43.80] owning the file system was really
[L674] [22:45.32] valuable to the company.
[L675] [22:47.08] Ultimately, we saved a huge amount of
[L676] [22:48.68] money. I mean, we we And this is before
[L677] [22:51.56] the public company went public. We
[L678] [22:53.28] really drove massive cost efficiencies
[L679] [22:56.20] through the project. Um but it was hard,
[L680] [22:58.48] you know, in a way that I think it'd be
[L681] [22:59.84] very difficult to to emulate without a
[L682] [23:02.00] huge investment.
[L683] [23:03.68] And I do think that there is um
[L684] [23:06.88] there is a benefit to an organization
[L685] [23:09.20] from having hard problems to solve.
[L686] [23:12.32] Because if you have a a company with
[L687] [23:14.04] extremely hard technical challenges, you
[L688] [23:16.48] can attract engineers who like working
[L689] [23:19.00] on those hard technical problems. And
[L690] [23:20.48] when they've solved those problems, they
[L691] [23:23.12] cycle off and work on different parts of
[L692] [23:25.00] the system. So, you know, after we all
[L693] [23:27.04] worked we had a such a great team. It
[L694] [23:28.88] was a very very small engineering team.
[L695] [23:30.72] And after we kind of shipped the the
[L696] [23:33.56] storage system reliably, we all went off
[L697] [23:35.36] and you know, Jamie went and and
[L698] [23:38.04] redesigned the sync protocol, the
[L699] [23:39.72] desktop client, and I worked on the on
[L700] [23:41.88] the file system and the distributed
[L701] [23:43.36] databases. And so, yeah, there's there's
[L702] [23:45.28] value to a business to have
[L703] [23:47.08] um that level of technical investment,
[L704] [23:49.20] but it is uh
[L705] [23:51.04] you know, it's like it's like having a
[L706] [23:52.36] baby and then you have to you've got to
[L707] [23:54.92] raise the baby. You can't just build a
[L708] [23:56.48] system like this and be that's it, we're
[L709] [23:58.16] done.
[L710] [23:59.56] You own it and you have to keep
[L711] [24:01.04] investing in it.
[L712] [24:03.32] >> Did um
[L713] [24:04.72] did S3 do any counter negotiation before
[L714] [24:07.64] you set out to leave them? Did they say
[L715] [24:09.16] like, "Oh, you know, we'll cut you a
[L716] [24:10.36] deal if you
[L717] [24:11.50] >> [laughter]
[L718] [24:12.72] >> I guess I'm allowed to talk about this
[L719] [24:14.00] now. It was a long time ago. Um
[L720] [24:17.04] Yeah, for the longest time they I don't
[L721] [24:18.28] think they were they were particularly
[L722] [24:19.48] aware that this was happening.
[L723] [24:21.40] Um but you know, the the data center
[L724] [24:23.20] folks talk. And uh certainly it was
[L725] [24:26.92] noticed that Dropbox is buying up a lot
[L726] [24:28.68] of data center space. So, yeah, we had
[L727] [24:31.24] we had um obviously at uh at the scales
[L728] [24:34.44] that we were at, I mean, we were
[L729] [24:35.80] negotiating very good rates with Amazon.
[L730] [24:38.52] You know, we weren't paying sticker
[L731] [24:39.60] price, we were paying very very very
[L732] [24:41.36] good discounted rates. Um but yeah, at a
[L733] [24:43.96] certain point they weren't able to meet
[L734] [24:45.36] our cost efficiency. Because it it's it
[L735] [24:47.12] when we launched the system, it really
[L736] [24:48.72] was
[L737] [24:49.96] more efficient than S3.
[L738] [24:51.92] And that's for a variety of reasons. One
[L739] [24:53.68] was that we were using kind of new
[L740] [24:55.32] experimental disks called shingled
[L741] [24:57.24] magnetic recording. We were the first
[L742] [24:59.12] ones, I think, to use these disks at
[L743] [25:00.60] scale.
[L744] [25:01.64] Um and two, we had a very tight
[L745] [25:03.68] understanding of our workloads. So, we
[L746] [25:04.96] were able to design the system
[L747] [25:06.44] specifically optimized for our
[L748] [25:08.20] workloads, whereas S3 has to design the
[L749] [25:10.60] system for everybody. So, you know, it
[L750] [25:13.12] got to the point where, you know, Amazon
[L751] [25:14.76] would not have been able to offer us a
[L752] [25:16.04] more competitive deal because we had a
[L753] [25:18.20] more efficient system.
[L754] [25:20.20] Um
[L755] [25:21.72] I wouldn't recommend another company do
[L756] [25:23.16] this right now.
[L757] [25:24.72] Uh but I think at the time it it
[L758] [25:26.12] certainly made sense for us as a
[L759] [25:27.40] company.
[L760] [25:28.92] >> Can you give an example of uh tight
[L761] [25:31.68] understanding of your workloads leading
[L762] [25:33.52] to like something you could do that S3
[L763] [25:36.24] couldn't?
[L764] [25:36.84] >> Yeah, absolutely. So, for example, I
[L765] [25:38.64] know
[L766] [25:39.88] that um well, I'll try not to leak any
[L767] [25:42.12] confidential data, right? But when you
[L768] [25:44.56] when you upload a file to Dropbox, there
[L769] [25:46.72] is a pattern of access, right? Um so,
[L770] [25:49.76] typically people um access the file very
[L771] [25:52.52] quickly shortly afterwards um because
[L772] [25:55.36] you're sharing it with someone or maybe
[L773] [25:57.44] Dropbox is processing that file to
[L774] [25:59.84] generate an image preview. And then it
[L775] [26:01.64] decays at a certain rate. And so, we
[L776] [26:03.80] understand in general the average block
[L777] [26:06.60] size, and we um understand also the
[L778] [26:09.56] access pattern. So, we could do things
[L779] [26:12.24] like at a certain point we had these two
[L780] [26:14.96] um clusters. One was at One was
[L781] [26:17.48] um designed for kind of temporary
[L782] [26:20.28] storage that was kind of
[L783] [26:21.80] storage-inefficient
[L784] [26:23.44] but access-efficient. So, it was very
[L785] [26:25.96] cheap to read and write to, but it was
[L786] [26:28.04] inefficient to store. And data would get
[L787] [26:30.04] written to there first, and then in the
[L788] [26:32.16] background it would get um moved in bulk
[L789] [26:35.40] to this colder storage system.
[L790] [26:37.68] And this colder storage system was far
[L791] [26:39.20] more static.
[L792] [26:40.80] And so, it was able to have kind of more
[L793] [26:42.40] efficient algorithms and and and be
[L794] [26:44.80] written to in bulk. And if it went down
[L795] [26:47.64] for writes, that was no problems because
[L796] [26:49.64] it wasn't in the live path. And so, we
[L797] [26:51.52] were able to trade off, again, like
[L798] [26:52.84] systems is all about trade-offs. So, we
[L799] [26:54.80] were able to trade off the the live data
[L800] [26:56.68] write path from the long-term read path.
[L801] [26:59.52] Um that's one of many examples where
[L802] [27:02.04] knowing the size of your data, where
[L803] [27:03.84] it's accessed from, how frequently it
[L804] [27:05.48] gets accessed, how um how long it takes
[L805] [27:07.52] to delete that data, you can really tune
[L806] [27:10.12] a system
[L807] [27:11.44] um to your workload. If you know, stuff
[L808] [27:13.68] like looking at
[L809] [27:15.36] um
[L810] [27:16.60] even things down to knowing how much
[L811] [27:18.52] power to put in a rack. You know, you
[L812] [27:20.48] have a rack of hardware, there's a power
[L813] [27:23.08] distribution unit, a PDU, at the top of
[L814] [27:24.72] that rack. It has a circuit breaker
[L815] [27:26.64] which can handle a certain number of
[L816] [27:28.12] amps.
[L817] [27:29.56] We would have to figure out, you know,
[L818] [27:31.56] how many amps are required for that rack
[L819] [27:33.96] based on access patterns. And there were
[L820] [27:35.68] times where we got it slightly wrong.
[L821] [27:37.36] There was times where
[L822] [27:38.84] we got to maybe a bad batch of hardware,
[L823] [27:41.16] and disks were failing too frequently.
[L824] [27:43.20] And as a result, we were re-replicating
[L825] [27:44.68] the data
[L826] [27:45.88] more regularly, and I was getting, you
[L827] [27:47.12] know, messages from the data center team
[L828] [27:48.44] saying, "Hey,
[L829] [27:49.76] we're I'm in the rack's really hot right
[L830] [27:51.28] now." You know? So, that's the level of
[L831] [27:53.56] optimizations you can make when you get
[L832] [27:55.52] to that scale. Um but again, that's
[L833] [27:58.20] multi-exabyte scale. You know,
[L834] [28:01.08] million hard drive scale.
[L835] [28:03.24] >> Yeah, when I was reading about this
[L836] [28:04.48] migration, I saw somewhere in the
[L837] [28:06.20] migration
[L838] [28:07.60] you initially started with Go, and then
[L839] [28:10.84] the racks or something that you're
[L840] [28:12.52] running on the hardware itself was
[L841] [28:14.40] ooming too much or
[L842] [28:16.00] requesting too much memory. And then you
[L843] [28:18.36] migrated to Rust.
[L844] [28:20.12] >> So, initially, the prototype was in
[L845] [28:22.16] Python, if you can believe that.
[L846] [28:24.16] And to be fair, Python is actually
[L847] [28:25.60] pretty efficient for IO. I think people
[L848] [28:27.24] give Python a a bad rap for IO-bound
[L849] [28:30.16] workloads. It's pretty good at IO. Um
[L850] [28:33.08] but obviously, um not great for
[L851] [28:35.08] concurrency, not great for memory
[L852] [28:36.32] management, and um very hard to
[L853] [28:38.44] refactor.
[L854] [28:39.76] And it was critical this system was
[L855] [28:41.24] correct. And so, we migrated everything
[L856] [28:44.36] to Go, and we built most of the storage
[L857] [28:46.12] system in Go. This is before Go was in
[L858] [28:48.92] general availability. I think it was
[L859] [28:50.12] before Go was GA. Um and we built the
[L860] [28:53.20] system in Go. Go is a great language for
[L861] [28:55.52] concurrency, a great language for
[L862] [28:56.96] proxies. You know, it's a really well
[L863] [28:59.24] designed for like servers that moved out
[L864] [29:01.48] of one place to another place.
[L865] [29:03.28] At a certain point though,
[L866] [29:05.00] we would have, you know, let's just pick
[L867] [29:07.08] a number. Let's say a million. Let's say
[L868] [29:08.20] we have a million nodes in the system.
[L869] [29:10.52] And every node has um
[L870] [29:13.92] some amount of memory, some amount of
[L871] [29:15.68] disk, some amount of sheet metal in the
[L872] [29:17.92] chassis, right? And we would itemize all
[L873] [29:20.40] these things. You'd have a pie chart of
[L874] [29:22.72] of how much money is spent on all the
[L875] [29:24.84] things. And it would still have stuff
[L876] [29:26.28] like, yeah, sheet metal and screws and
[L877] [29:27.80] stuff. And so, you're trying to optimize
[L878] [29:30.36] the storage and a big problem for us was
[L879] [29:33.88] the amount of memory um
[L880] [29:36.52] these nodes were using. Not just the
[L881] [29:38.24] memory that we're using, but the
[L882] [29:39.60] unpredictability of it. Uh with, you
[L883] [29:42.40] know, with Go having a runtime and and
[L884] [29:45.80] you know, in a storage system, an out of
[L885] [29:47.64] memory error is pretty bad.
[L886] [29:49.96] Because if a node runs out of memory and
[L887] [29:51.48] restarts, that looks like a disk
[L888] [29:53.16] failure.
[L889] [29:54.60] So, that looks a lot like a disk has
[L890] [29:56.04] failed and has to be re-replicated. And
[L891] [29:57.68] so, a batch of nodes OOMing
[L892] [30:01.12] can lead to cascading failures
[L893] [30:02.76] throughout the system.
[L894] [30:04.28] Because maybe um I remember a time it
[L895] [30:08.24] was a band. It might have been De La
[L896] [30:09.48] Soul. I can't remember. There was a band
[L897] [30:10.88] released an album on Dropbox.
[L898] [30:13.40] So, there was a big spike in load
[L899] [30:15.84] um to a to a
[L900] [30:17.84] a few files. So, it was very, very high
[L901] [30:20.80] um bandwidth and it caused the the
[L902] [30:23.16] machines to OOM. So, the those machines
[L903] [30:25.64] uh OOMed, those disks OOMed. Um and so,
[L904] [30:28.44] as a result, no problems. The system
[L905] [30:30.40] went to try to recover that data from a
[L906] [30:32.48] whole bunch of other replicas, right?
[L907] [30:34.84] Now, all of the sudden you've taken one
[L908] [30:37.08] amount one fire hose worth of load
[L909] [30:39.40] coming in and you've turned this into
[L910] [30:41.00] seven fire hoses worth of load coming,
[L911] [30:42.68] cuz now you have to do a more expensive
[L912] [30:44.28] reconstruction operation, right? So now
[L913] [30:46.36] you've seven x the load. And these are
[L914] [30:48.20] the kind of cyclical kind of behaviors
[L915] [30:51.12] that can lead to something called
[L916] [30:52.04] congestion collapse. Congestion collapse
[L917] [30:53.88] is when
[L918] [30:55.04] workload to a system crosses a threshold
[L919] [30:57.28] where it all kind of collapses.
[L920] [30:59.76] So
[L921] [31:00.80] designing against congestion collapse is
[L922] [31:02.48] really the hardest part or one of the
[L923] [31:04.48] hardest parts of Magic Pocket, which is
[L924] [31:06.00] the name of the storage system. Um so
[L925] [31:08.72] ultimately we switched to Rust for the
[L926] [31:12.20] storage nodes themselves. And this
[L927] [31:13.92] again, this is before Rust was in GA, so
[L928] [31:16.36] that was a bit of a risky move.
[L929] [31:18.16] Uh but we rewrote um
[L930] [31:20.64] the switch to Rust coincided with
[L931] [31:22.64] getting rid of the file system entirely
[L932] [31:24.32] on the disks and directly addressing the
[L933] [31:27.04] the disk disk heads. So there was a
[L934] [31:29.28] there's an instruction set, I think it's
[L935] [31:30.48] called ZBC, zone based block control,
[L936] [31:33.60] something like that. There's there's a
[L937] [31:34.52] there's an instruction set for accessing
[L938] [31:36.08] disks that we were using.
[L939] [31:38.16] The disk manufacturers gave us the draft
[L940] [31:39.96] specs of these new disks and we were
[L941] [31:41.80] operating off the draft specs and
[L942] [31:43.80] directly controlling the the disks. And
[L943] [31:45.80] so
[L944] [31:46.68] all that product was tied up um together
[L945] [31:49.60] um
[L946] [31:50.72] into a product called DiscoTech.
[L947] [31:52.64] It was the disk technology project. Um
[L948] [31:55.44] and ultimately, if you look at that pie
[L949] [31:57.24] chart, one congestion collapse stopped
[L950] [31:59.36] and reliability improved. But if you
[L951] [32:01.08] looked at the pie chart of where all the
[L952] [32:02.56] money was going, it really shifted to be
[L953] [32:05.00] almost all disks. And what we wanted to
[L954] [32:07.16] do is get that pie chart to be
[L955] [32:10.08] almost all the money spent on disks and
[L956] [32:12.48] as little money spent on RAM, on
[L957] [32:14.24] compute, on network, on power, on sheet
[L958] [32:16.60] metal, etc.
[L959] [32:17.88] >> The cascading failure you mentioned, was
[L960] [32:20.00] there So that that happened and then
[L961] [32:22.44] there was a postmortem.
[L962] [32:23.60] >> I don't think we needed a postmortem.
[L963] [32:24.88] Well, I think we we knew as it was
[L964] [32:26.20] happening.
[L965] [32:27.34] >> [laughter]
[L966] [32:28.24] >> I think when I was getting paged in the
[L967] [32:29.88] middle of the night on these things, I
[L968] [32:31.36] would you know, you'd be pretty pretty
[L969] [32:32.92] evident. And so look, this is the again,
[L970] [32:35.52] this is an argument in favor of the
[L971] [32:36.96] cloud. All right. Imagine you've spent
[L972] [32:40.16] hundreds of millions of dollars on a on
[L973] [32:42.60] a storage system and it's out in
[L974] [32:43.96] production and it's on physical
[L975] [32:46.00] hardware.
[L976] [32:47.40] You can't just go and put new memory
[L977] [32:50.24] chips in every one of them. I mean, you
[L978] [32:51.72] can, but you have to pay people to come
[L979] [32:53.80] in and swap them out, you know. And so
[L980] [32:55.76] that That's a tricky place. And so as a
[L981] [32:59.00] And this is what This is what I love
[L982] [33:00.28] about industry. You know, cuz in like
[L983] [33:03.24] some of the more um
[L984] [33:05.08] challenging moments on Magic Pocket were
[L985] [33:07.64] stuff like in one week
[L986] [33:09.84] This is a weird coincidence. Two trucks
[L987] [33:12.16] crashed that were delivering servers. So
[L988] [33:13.84] there's two trucks showing up to deliver
[L989] [33:16.12] racks and then they both crashed. I
[L990] [33:17.32] don't know, you know, the drivers were
[L991] [33:18.44] okay. So we lost capacity for 2 weeks.
[L992] [33:21.72] Uh so the So we lost capacity for for
[L993] [33:23.68] more than 2 weeks. For for for probably
[L994] [33:25.48] 6 weeks.
[L995] [33:26.96] Um
[L996] [33:28.08] What do you do?
[L997] [33:29.84] What happens, you know, is is the
[L998] [33:31.40] equivalent of your disk filling up on
[L999] [33:32.72] your laptop except it's, you know, it's
[L1000] [33:34.68] it's a million disks.
[L1001] [33:36.56] And you can't tell the customers to go
[L1002] [33:38.48] away. You can't delete their files. So a
[L1003] [33:40.48] lot of a lot of tricky um a lot of
[L1004] [33:43.52] tricky capacity work. Um and ultimately
[L1005] [33:46.36] what that what that led to was trying to
[L1006] [33:48.60] build in
[L1007] [33:51.00] all these protections against the
[L1008] [33:52.64] unknowns. You know, making sure we had
[L1009] [33:55.48] the right amount of buffer planned out
[L1010] [33:57.48] for anything bad that could happen.
[L1011] [33:59.00] Making sure we we designed the system so
[L1012] [34:01.32] they couldn't be congestion collapse so
[L1013] [34:02.92] there wouldn't be memory spikes.
[L1014] [34:05.08] Um and
[L1015] [34:06.96] you know, at one point there's a there's
[L1016] [34:08.44] a process called I think it's called
[L1017] [34:09.56] FMEA
[L1018] [34:11.16] which is like a threat modeling process
[L1019] [34:12.80] where you had a big spreadsheet and you
[L1020] [34:14.44] kind of write down every bad thing that
[L1021] [34:16.72] could possibly happen and then, you
[L1022] [34:18.52] know, all the how bad it would be if it
[L1023] [34:20.64] happened.
[L1024] [34:21.84] Existential risk.
[L1025] [34:23.80] Does someone die? You know, if there's a
[L1026] [34:25.20] fire in the data center. All these kind
[L1027] [34:26.56] of things get put into the spreadsheet.
[L1028] [34:28.40] And you kind of do a bit of a almost
[L1029] [34:30.36] pre-mortem kind of work to figure out
[L1030] [34:33.04] all the all the potential failure modes,
[L1031] [34:35.12] and then design around them. And I I
[L1032] [34:36.92] that's I love that work. I I I really um
[L1033] [34:40.56] I don't know. I do like the firefight. I
[L1034] [34:42.40] I like the
[L1035] [34:44.16] I don't I can't say I like getting paged
[L1036] [34:45.88] because
[L1037] [34:47.24] I've spent my whole life on call,
[L1038] [34:49.32] but I do like that rubber hits the road
[L1039] [34:51.80] stuff. I like that
[L1040] [34:54.32] wow, there's congestion collapse and and
[L1041] [34:56.04] there's no one that can help you. And
[L1042] [34:58.28] so, you've [snorts] got to
[L1043] [34:59.84] think through this problem.
[L1044] [35:01.44] >> When I worked on infrastructure at
[L1045] [35:02.84] Instagram, we had this concept of DEFCON
[L1046] [35:04.92] knobs, which are basically these configs
[L1047] [35:08.32] that you could flip that would
[L1048] [35:10.40] gracefully degrade your system, where
[L1049] [35:12.96] you can still operate it, but you know,
[L1050] [35:15.04] maybe in the case of Dropbox, you store
[L1051] [35:17.68] less replicas. So, you take on a
[L1052] [35:20.20] temporary increase of
[L1053] [35:22.80] uh risk in losing data because you need
[L1054] [35:25.24] to. Uh did you have something like that,
[L1055] [35:27.32] and did you flip it in that type of
[L1056] [35:29.04] case?
[L1057] [35:29.52] >> Never when it came to durability. So, I
[L1058] [35:32.00] mean, we just had a just absolute zero
[L1059] [35:34.88] non-negotiable, like there was no room
[L1060] [35:36.88] for negotiation on on user durability.
[L1061] [35:39.52] And so, um
[L1062] [35:41.32] we had those knobs for background
[L1063] [35:42.72] processes, for CPU and and memory, for
[L1064] [35:44.56] example. So, if there was like a spike
[L1065] [35:46.00] in load, you could turn off background
[L1066] [35:48.12] processes and and turn off um you know,
[L1067] [35:50.80] um the the test load, for example, on
[L1068] [35:52.88] the system. Eventually, we we built this
[L1069] [35:55.16] system called
[L1070] [35:57.64] trampoline.
[L1071] [35:58.92] And what trampoline did was um which
[L1072] [36:01.76] actually was a it it saved us a ton of
[L1073] [36:03.60] money, right? When if we ever got too
[L1074] [36:06.44] close to the threshold, we would just
[L1075] [36:08.40] start writing data to S3.
[L1076] [36:10.36] Cuz it's right there, right? So, it's um
[L1077] [36:13.32] you can run your capacity way closer to
[L1078] [36:15.84] the edge if you're willing under worst
[L1079] [36:18.16] case scenarios just to just to dump 30
[L1080] [36:20.84] petabytes on S3, and then move it back
[L1081] [36:23.32] when it's done. And now, it didn't that
[L1082] [36:25.24] didn't happen very often. We would do it
[L1083] [36:26.64] to test it. We would do that to make
[L1084] [36:28.00] sure the system worked.
[L1085] [36:29.68] But um yeah, being able to have a escape
[L1086] [36:32.84] hatch for worst case scenario was really
[L1087] [36:34.80] nice.
[L1088] [36:35.72] >> As you said, S3 is kind of
[L1089] [36:37.92] it's like elastic storage.
[L1090] [36:39.60] >> Exactly.
[L1091] [36:40.84] >> When I looked at this project, it's such
[L1092] [36:44.00] a massive migration and my first thought
[L1093] [36:46.52] is how do you coordinate this whole
[L1094] [36:49.00] project without breaking the system as
[L1095] [36:51.68] it's running?
[L1096] [36:53.20] How Yeah, what are your thoughts on
[L1097] [36:55.80] doing such a large migration without
[L1098] [36:57.64] breaking things?
[L1099] [36:58.28] >> Yeah. Now, I mean in
[L1100] [37:00.40] in terms of the engineers that like
[L1101] [37:02.00] built the initial version of the system,
[L1102] [37:04.20] it was a handful.
[L1103] [37:05.88] Three, four, five, six engineers. It
[L1104] [37:07.48] wasn't a team of a thousand, you know.
[L1105] [37:09.24] It was a very, very small team. And so
[L1106] [37:11.64] um
[L1107] [37:12.68] how do you build such a large system
[L1108] [37:15.60] with a small number of people and then
[L1109] [37:16.84] how do you do a high-risk migration?
[L1110] [37:19.20] Uh
[L1111] [37:21.04] One of these one one thing you do is you
[L1112] [37:22.76] keep things simple. You you try so so so
[L1113] [37:25.44] hard to
[L1114] [37:27.16] build very cleanly abstracted, simple
[L1115] [37:30.28] systems that their failure modes are
[L1116] [37:32.08] very understandable. Um and so they and
[L1117] [37:34.60] they and they decouple so they don't
[L1118] [37:36.16] have congestion, collapse, etc. So,
[L1119] [37:38.24] focusing on simplicity this it gets
[L1120] [37:40.52] tricky by the way with people doing
[L1121] [37:42.56] agentic development. They They're not
[L1122] [37:44.40] the best at building simple systems.
[L1123] [37:45.88] Like simplicity is still the domain of
[L1124] [37:47.88] human beings for now. But um a big focus
[L1125] [37:50.76] on simplicity. The other was um
[L1126] [37:53.76] you know, this this very thick layer of
[L1127] [37:56.24] validation checks during this migration.
[L1128] [37:58.64] And And in fact, um we had uh
[L1129] [38:02.24] when we did the migration off of S3, we
[L1130] [38:04.52] had this um something called the dark
[L1131] [38:06.12] launch where we would you know, be
[L1132] [38:07.56] moving data off of S3, but we were
[L1133] [38:09.80] keeping it in both locations. And we had
[L1134] [38:12.12] to demonstrate to the We had this kind
[L1135] [38:13.68] of contract with the Dropbox founders.
[L1136] [38:17.28] We'd have to kind of keep the system
[L1137] [38:18.92] running with no incidents,
[L1138] [38:21.12] uh no downtime, no data loss, for 6
[L1139] [38:23.24] months before we would delete any of the
[L1140] [38:25.36] data from S3. So, we have double write
[L1141] [38:27.80] it. And, um,
[L1142] [38:30.32] and there's one point in time, halfway
[L1143] [38:32.28] through this process, where there was a
[L1144] [38:33.92] a bug got through to production.
[L1145] [38:35.92] Um, and it didn't nothing bad happened
[L1146] [38:38.16] with the bug. But, it was a it was like
[L1147] [38:39.88] a,
[L1148] [38:41.36] it was it was like a a bug
[L1149] [38:43.44] slipped through our multiple layers of,
[L1150] [38:45.48] you know, release process, etc.
[L1151] [38:47.48] And, um,
[L1152] [38:48.92] so, I went to the VP and I said, "Hey,
[L1153] [38:50.64] you a bug made it through to production,
[L1154] [38:53.12] and we're going to reset the launch
[L1155] [38:55.40] clock.
[L1156] [38:56.64] And, as a result, it's going to launch
[L1157] [38:58.84] later, and it's going to cost us
[L1158] [39:01.36] some amount of money. Let's say
[L1159] [39:02.48] double-digit millions, you know?
[L1160] [39:05.36] And, they were like, "Great.
[L1161] [39:07.56] Thank you. That's good. I trust you."
[L1162] [39:09.32] And, that was that that was a cool
[L1163] [39:10.80] thing. I mean, Dropbox had a lot of
[L1164] [39:11.92] incredible cultural values. But, like,
[L1165] [39:14.04] that was like, "Okay, cool. If you're
[L1166] [39:15.72] prioritizing user safety, that's the
[L1167] [39:17.12] right thing to do." And, um, no one was
[L1168] [39:19.96] mad about that. It was almost like they
[L1169] [39:21.32] were
[L1170] [39:22.68] proud, almost. You know, it was it was
[L1171] [39:24.52] just like a it was like, "Yes, you're
[L1172] [39:26.56] you're operating, uh, in accordance to
[L1173] [39:29.00] the
[L1174] [39:29.76] principles of this company." And, yeah.
[L1175] [39:32.04] >> Okay, so, it it was double writing both
[L1176] [39:33.80] systems for a while, and then
[L1177] [39:35.08] >> For some subset of data, yeah.
[L1178] [39:36.56] >> Uh, okay. And, then you switched over
[L1179] [39:38.16] reads.
[L1180] [39:39.00] >> Once we were sure the system was
[L1181] [39:40.64] durable, and we had all these validators
[L1182] [39:42.24] running in production 24/7, uh, then we
[L1183] [39:44.80] were just migrating as fast as we could.
[L1184] [39:46.28] I think at some point we got up to 700
[L1185] [39:49.12] gigabits per second, 764 gigabits per
[L1186] [39:52.24] second of peering bandwidth between
[L1187] [39:54.24] Amazon servers and ours. Um,
[L1188] [39:57.12] certainly someone on the network team
[L1189] [39:58.60] over there noticed
[L1190] [39:59.92] that [laughter] there was that much data
[L1191] [40:01.00] moving out.
[L1192] [40:02.88] At one point, I got a a slightly nasty
[L1193] [40:05.28] email from someone saying
[L1194] [40:07.15] >> [snorts]
[L1195] [40:07.68] >> it was super weird. I think the phrase
[L1196] [40:09.56] super weird, it's like, "It's super
[L1197] [40:11.40] weird that you're doing so many reads
[L1198] [40:13.16] and not that many writes."
[L1199] [40:14.72] >> Mhm.
[L1200] [40:15.00] >> And, I didn't didn't respond to that
[L1201] [40:17.04] email. But to be fair, like Amazon was
[L1202] [40:19.76] us are a great have been a were a great
[L1203] [40:21.28] partner for Dropbox. And Dropbox still
[L1204] [40:23.04] uses AWS. They always
[L1205] [40:26.04] um
[L1206] [40:26.80] there was no concern that they would do
[L1207] [40:28.04] the wrong thing by us as a company. I
[L1208] [40:29.48] mean, like well we we only had excellent
[L1209] [40:31.88] experience with AWS. Um but yeah, there
[L1210] [40:34.56] was a it was a moment for us, you know,
[L1211] [40:36.68] it was a
[L1212] [40:38.48] it probably strained the relationship
[L1213] [40:40.28] somewhat.
[L1214] [40:41.52] >> You mentioned simplicity and
[L1215] [40:44.16] intuition-wise, it makes sense.
[L1216] [40:46.80] Do you have a concrete example though?
[L1217] [40:49.00] >> Yeah, I've got a concrete example for
[L1218] [40:50.08] you. And it it maybe it shows the
[L1219] [40:51.40] difference between academia and
[L1220] [40:53.08] industry.
[L1221] [40:54.32] Um so um
[L1222] [40:56.76] the storage system is a giant
[L1223] [40:58.56] distributed system with a files stored
[L1224] [41:01.60] in various locations. And so you need a
[L1225] [41:03.76] a mapping from from the file to where it
[L1226] [41:06.28] lives on these disks.
[L1227] [41:08.20] And so all we did was had a cluster of a
[L1228] [41:11.36] thousand MySQL nodes.
[L1229] [41:14.20] All right?
[L1230] [41:15.24] Big giant database, and it was indexed
[L1231] [41:17.76] by the block ID, and it said this block
[L1232] [41:19.92] is on these disks.
[L1233] [41:21.40] And that's a pretty
[L1234] [41:23.84] like simple, it's not sophisticated, you
[L1235] [41:26.20] know? And it And every time we'd hire
[L1236] [41:29.28] someone out of academia, or maybe from
[L1237] [41:32.36] other companies, they'd say, "Oh, this
[L1238] [41:33.52] is not very sophisticated because like
[L1239] [41:35.60] you could use a Patricia trie, or you
[L1240] [41:37.96] could use a distributed hash table, and
[L1241] [41:40.64] that would map um a block to a set of um
[L1242] [41:44.56] of of locations." And I think
[L1243] [41:48.88] that's optimizing for the wrong thing.
[L1244] [41:51.68] Because the really nice thing about
[L1245] [41:52.92] dumping a list of files and their
[L1246] [41:54.68] locations in a giant database is it's
[L1247] [41:56.84] written in one location. If I want to
[L1248] [41:59.00] validate what happened, if I want to
[L1249] [42:00.92] check all the data there is where it's
[L1250] [42:02.52] meant to be, I just walk over the table
[L1251] [42:05.12] and check. And we did. We had services
[L1252] [42:07.20] constantly walking over in the table and
[L1253] [42:08.80] checking. Whereas if it it a distributed
[L1254] [42:10.68] hash table or some giant complex data
[L1255] [42:12.56] structure, it's very hard to to
[L1256] [42:14.28] validate. So, I mean, designing for
[L1257] [42:16.84] validation is very important. Designing
[L1258] [42:18.36] for understanding is very important.
[L1259] [42:19.56] It's not about getting a system to work.
[L1260] [42:22.20] It's what do you do when it doesn't
[L1261] [42:24.12] work, right? And so, having a very
[L1262] [42:26.72] simple boundary That's That's a It's a
[L1263] [42:29.00] very basic example, you know, there's
[L1264] [42:30.44] there's more There's more sophisticated
[L1265] [42:31.96] examples that take more time to explain,
[L1266] [42:33.44] but like something like that is
[L1267] [42:36.76] a lot of engineers will feel, you know,
[L1268] [42:39.36] a lot of engineers will want to do
[L1269] [42:40.76] interesting work. Will want to advance
[L1270] [42:42.24] in their career. They They want to be
[L1271] [42:44.68] seen as a as a intellectual problem
[L1272] [42:48.36] solver.
[L1273] [42:49.64] And so, the tendency can be to design
[L1274] [42:52.68] complex systems. And my argument is
[L1275] [42:55.12] always that like
[L1276] [42:56.56] simple systems are way harder to design
[L1277] [42:59.28] than complex systems.
[L1278] [43:01.52] Like, simplicity is so hard. And I think
[L1279] [43:03.88] to like maybe the untrained eye, a
[L1280] [43:05.72] simple system can seem like obvious. And
[L1281] [43:08.76] the the And the best compliment you
[L1282] [43:10.20] could ever get about anything you design
[L1283] [43:13.00] is people say like, "Oh, isn't that the
[L1284] [43:15.04] Isn't that the obvious way of doing it?"
[L1285] [43:16.56] It's It's like the same as convex, you
[L1286] [43:18.32] know, people say, "Oh, isn't that
[L1287] [43:20.68] What's that? That's just like the
[L1288] [43:21.76] obvious way of structuring?" Like,
[L1289] [43:22.96] great. Because it wasn't obvious when we
[L1290] [43:25.04] did it. No one else was doing it, right?
[L1291] [43:26.76] Everyone thought we were idiots. If
[L1292] [43:28.52] after the fact people think it's
[L1293] [43:30.56] obvious, then you then you really nailed
[L1294] [43:32.00] it. I think um
[L1295] [43:33.72] But I think that's a um it requires a an
[L1296] [43:36.32] understanding that's that that
[L1297] [43:37.44] simplicity is is the hardest thing in
[L1298] [43:39.28] systems. And cuz simplicity is
[L1299] [43:42.12] is scalable. And I don't Yes, simplicity
[L1300] [43:44.20] is scalable in terms of numbers of
[L1301] [43:46.88] queries per second, right? But what I
[L1302] [43:48.76] really mean about scalability is you can
[L1303] [43:50.92] take a simple system
[L1304] [43:53.12] and and have it run for 5 years, and
[L1305] [43:55.64] have people work on it for 5 years, and
[L1306] [43:57.92] have all sorts of features added to it,
[L1307] [44:00.08] and have requirements changed cuz the
[L1308] [44:01.72] company realized the product didn't work
[L1309] [44:03.28] the way it wanted to work, and it wants
[L1310] [44:04.60] to change things, and it still stands
[L1311] [44:07.04] the test of time.
[L1312] [44:08.44] Whereas a complex over-optimized system
[L1313] [44:10.76] will not. And And that's the tough thing
[L1314] [44:12.80] about
[L1315] [44:13.92] distributed systems design, especially
[L1316] [44:16.48] um
[L1317] [44:17.28] LLM augmented distributed systems
[L1318] [44:19.04] design, is just because something works
[L1319] [44:22.68] doesn't mean it's maintainable over a
[L1320] [44:24.36] long period of time. Doesn't mean it's
[L1321] [44:25.56] understandable. Doesn't mean it's
[L1322] [44:26.64] cleanly up architected and abstracted.
[L1323] [44:29.28] That stuff's really very hard.
[L1324] [44:31.52] >> Absolutely. And I agree with you. I
[L1325] [44:34.12] think it's the long-term beneficial
[L1326] [44:35.80] thing to do.
[L1327] [44:37.24] One unusual thing though in the industry
[L1328] [44:39.04] that I I've seen is
[L1329] [44:41.04] the incentive system for engineers is
[L1330] [44:44.04] actually I mean, you mentioned the
[L1331] [44:45.88] desire for an engineer to want to be
[L1332] [44:48.52] seen that they can do something
[L1333] [44:50.16] difficult. There's that, but there's
[L1334] [44:51.68] also the incentive system of promotions.
[L1335] [44:54.76] And I've had many friends whose
[L1336] [44:57.04] promotions were rejected because their
[L1337] [44:59.52] work wasn't complex enough. And so that
[L1338] [45:02.12] kind of forces It's a forces complexity,
[L1339] [45:05.00] which is kind of unusual. I wanted to
[L1340] [45:07.12] know what you thought about that.
[L1341] [45:08.44] >> Yeah. It I mean, almost
[L1342] [45:11.48] angers me. I just like it so much.
[L1343] [45:14.48] Partly why I started my own company, you
[L1344] [45:16.12] know.
[L1345] [45:17.16] Um
[L1346] [45:18.16] I think
[L1347] [45:20.00] the ideal for anyone is to be doing work
[L1348] [45:23.92] where the you're being appreciated for
[L1349] [45:27.32] solving the problem. Like, you know, and
[L1350] [45:29.92] this is
[L1351] [45:31.12] if we get philosophical, this is what it
[L1352] [45:32.44] was like going back to the farming days,
[L1353] [45:34.52] right? There was no incentive to make it
[L1354] [45:36.48] really complicated to milk a cow, cuz
[L1355] [45:38.36] the goal is to like milk the cow, and
[L1356] [45:40.12] then the back The reward is you got
[L1357] [45:41.64] milk, right? And I think at a It sounds
[L1358] [45:44.20] so silly, but at a startup, that's the
[L1359] [45:46.36] same thing. The startup, the goal is to
[L1360] [45:48.20] build the system, have it work, have the
[L1361] [45:49.88] users like it, have it grow, and
[L1362] [45:52.44] everyone gets rewarded and celebrated
[L1363] [45:55.16] for solving the problem.
[L1364] [45:57.92] It gets hard to scale that. So at large
[L1365] [46:00.08] companies
[L1366] [46:01.80] the end up with so many layers of
[L1367] [46:03.96] organization that people end up building
[L1368] [46:06.60] alternative incentive structures, right?
[L1369] [46:08.72] It's like I'm so far away from whatever
[L1370] [46:11.28] the hell we're trying to do over here
[L1371] [46:12.88] that my goal now is to get all green
[L1372] [46:15.80] check marks on my OKR plan.
[L1373] [46:18.64] But who cares about your OKR plan unless
[L1374] [46:20.20] it solves the problem? And so the you
[L1375] [46:22.20] know, the thing that really drives me um
[L1376] [46:25.28] really drives me insane is when people
[L1377] [46:27.48] try to chase
[L1378] [46:29.92] um
[L1379] [46:31.20] artificial goals.
[L1380] [46:32.60] Right? And I And I understand that if
[L1381] [46:34.84] you're in a company with um like this
[L1382] [46:37.36] that you may have no choice in the
[L1383] [46:38.76] matter. But what I want to tell people
[L1384] [46:40.88] there is a better way.
[L1385] [46:43.56] And it you know, and that that better
[L1386] [46:45.64] way may not be available to you. You may
[L1387] [46:47.16] not
[L1388] [46:48.16] have job opportunities near where you
[L1389] [46:50.52] are, for example.
[L1390] [46:51.84] But if you do have the ability to go
[L1391] [46:54.40] work at a company where
[L1392] [46:57.08] like you are being appreciated for
[L1393] [46:58.68] problem solving,
[L1394] [47:00.56] that will make you so much better as an
[L1395] [47:02.36] engineer. Like And I see this when I
[L1396] [47:04.64] when I interview people, you know?
[L1397] [47:06.56] Um and I if if I, you know, do a um
[L1398] [47:09.60] I mean, everyone knows Google has
[L1399] [47:10.84] tremendous engineering and tremendous
[L1400] [47:12.28] engineers. Um a lot of
[L1401] [47:14.68] folks there though, I'm not
[L1402] [47:16.72] that interested in hiring
[L1403] [47:19.68] because
[L1404] [47:21.88] you know, if I'll do a deep dive with
[L1405] [47:23.64] them and they'll say they built a system
[L1406] [47:24.80] and I'll say, "Well, why did you build
[L1407] [47:25.72] it?" And they're like, "I don't know.
[L1408] [47:26.48] The VP told me to." And like, "Oh, how
[L1409] [47:28.92] is this system used?" And they're like,
[L1410] [47:30.00] "I
[L1411] [47:30.84] I don't really know. I think ads uses
[L1412] [47:32.32] it. I'm not sure." And this is a this is
[L1413] [47:34.36] a caricature, but I think it's very,
[L1414] [47:36.16] very hard to do good engineering in that
[L1415] [47:37.80] environment. You can do competent
[L1416] [47:39.88] engineering, but the best engineering
[L1417] [47:41.84] comes from a deep understanding of why.
[L1418] [47:44.60] And this is something we just drill into
[L1419] [47:47.32] you know, the the team here Convex, or
[L1420] [47:48.88] you know, the team embodies so strongly
[L1421] [47:50.44] at Convex is like everything exists for
[L1422] [47:52.44] the why. Do like don't build a a fancy
[L1423] [47:55.76] load balancer unless it's not needed.
[L1424] [47:57.32] Turns out we do need a fancy load
[L1425] [47:58.68] balancer, we're building it right now.
[L1426] [48:00.12] But but you know,
[L1427] [48:01.68] you should always start with why are we
[L1428] [48:02.88] doing this? What's the point?
[L1429] [48:05.04] And
[L1430] [48:06.92] I feel for people stuck in environments
[L1431] [48:09.96] that are not like this. But you know
[L1432] [48:11.52] what? Like I don't know.
[L1433] [48:14.84] Try to fight the system a little bit. I
[L1434] [48:16.52] think I do see a lot of maybe nihilism,
[L1435] [48:19.36] a lot of defeatedness sometimes amongst
[L1436] [48:21.68] junior engineers. A lot of this um
[L1437] [48:23.96] cynicism.
[L1438] [48:25.36] Like you know, what does it matter? Like
[L1439] [48:27.52] who cares? It's just a big organization
[L1440] [48:29.24] and nothing matters and but I think it
[L1441] [48:31.28] does matter. Like
[L1442] [48:33.36] I've just if I think of like the
[L1443] [48:35.12] happiest times in my life, it's been
[L1444] [48:36.84] like just
[L1445] [48:37.96] dedicating myself to a cause and
[L1446] [48:40.60] and
[L1447] [48:41.56] and trying really hard and and trying to
[L1448] [48:43.60] do the right thing and and I felt good
[L1449] [48:45.32] when I went home and and not trying to
[L1450] [48:47.52] get promoted, just trying to do the
[L1451] [48:48.52] right thing and then and then
[L1452] [48:50.52] assume me I'm going to get promoted and
[L1453] [48:51.60] if not go somewhere else. Um I know it
[L1454] [48:54.08] does sound quaint when I'm saying this,
[L1455] [48:55.96] but I think it's possible to do this and
[L1456] [48:57.48] especially possible if you surround
[L1457] [48:59.28] yourself with people like this.
[L1458] [49:01.24] And if someone is in a big company and
[L1459] [49:03.48] they're feeling frustrated by politics,
[L1460] [49:05.84] look around and see if there's a team of
[L1461] [49:07.56] folks who just seem to
[L1462] [49:09.40] want to do the right thing. Just seem to
[L1463] [49:10.76] want to do good stuff. I don't think
[L1464] [49:12.44] that's selling out. I think that's being
[L1465] [49:13.76] true to yourself. Like just
[L1466] [49:15.68] that's what real engineering is.
[L1467] [49:17.72] Not trying to make a complicated fancy
[L1468] [49:19.44] thing to get promoted. Just build the
[L1469] [49:20.56] coolest thing that's solves the problem.
[L1470] [49:23.08] >> This really reminds me of something you
[L1471] [49:24.72] had written and I thought it was really
[L1472] [49:25.92] good writing. And in the writing there
[L1473] [49:28.52] was this idea of system bias.
[L1474] [49:31.88] And
[L1475] [49:32.48] >> Yes.
[L1476] [49:32.96] >> you you have this
[L1477] [49:34.92] uh quote your your writing. It says you
[L1478] [49:36.96] know, here's some examples. It says the
[L1479] [49:38.56] team is spending 6 months to improve
[L1480] [49:40.36] performance by 10% when it was
[L1481] [49:42.40] completely fine to begin with or you
[L1482] [49:44.80] know, the team is trying desperately to
[L1483] [49:46.48] force their tooling on clients who don't
[L1484] [49:48.96] need it or you know, the team is riding
[L1485] [49:51.76] their outdated system to the grave like
[L1486] [49:54.04] the captain going down on the Titanic.
[L1487] [49:57.64] I I've I've definitely seen examples of
[L1488] [49:59.60] all those types of things in industry.
[L1489] [50:02.56] Um
[L1490] [50:03.52] And so
[L1491] [50:04.72] yeah, it I I think it was it was in the
[L1492] [50:06.92] the
[L1493] [50:08.12] It was in the context of your writing
[L1494] [50:10.00] about um what you should orient your
[L1495] [50:13.20] your team around, not systems, but
[L1496] [50:15.68] actually missions. And maybe that's a
[L1497] [50:18.08] way to fight system bias.
[L1498] [50:20.20] >> Yeah, I mean, one of one of my jobs at
[L1499] [50:21.72] Dropbox um
[L1500] [50:23.60] wasn't the most fun job, but it might
[L1501] [50:25.04] have been one of the most impactful
[L1502] [50:26.16] jobs. It was shutting down projects, you
[L1503] [50:28.32] know, looking around and being like,
[L1504] [50:30.80] "Huh, that thing over there that
[L1505] [50:33.20] has had 60 people working on it for 2
[L1506] [50:35.12] years doesn't seem to make a lot of
[L1507] [50:37.12] sense to me." And then I you know, it
[L1508] [50:39.00] wasn't like a um a hostile thing, but
[L1509] [50:41.28] I'd go and chat with the team and I'd
[L1510] [50:42.64] say, "Hey,
[L1511] [50:44.24] what are you all doing? Do you believe
[L1512] [50:45.32] in what you're doing? Does this make
[L1513] [50:46.44] sense?" And the team in private would
[L1514] [50:48.60] say, "Oh, I don't really know. I don't
[L1515] [50:50.32] really But inertia is so strong, you
[L1516] [50:52.56] know, this whole desire to not get in
[L1517] [50:54.60] trouble, you know, to just keep doing
[L1518] [50:57.08] what you were previously doing is so
[L1519] [50:58.72] strong. And it And talented people can
[L1520] [51:00.56] end up doing things that don't make a
[L1521] [51:01.64] lot of sense.
[L1522] [51:02.92] One of the things I said in that article
[L1523] [51:04.52] is it It's kind of a cheesy story, but
[L1524] [51:07.20] when we started um
[L1525] [51:09.44] building the storage system at Dropbox,
[L1526] [51:11.44] the team was called the magic pocket
[L1527] [51:12.88] team cuz that was a silly code name for
[L1528] [51:14.44] the for the for the system we built.
[L1529] [51:17.16] And so the team was oriented around
[L1530] [51:19.00] building that system. But as soon as we
[L1531] [51:21.68] shipped it,
[L1532] [51:23.08] I renamed the team to the storage team.
[L1533] [51:26.44] And that
[L1534] [51:27.44] actually took a bit of work cuz you have
[L1535] [51:28.84] to like rename all the email addresses
[L1536] [51:30.88] and the channels and the repos and the
[L1537] [51:32.76] things. And so it seems like a waste of
[L1538] [51:34.68] time. And um
[L1539] [51:37.00] but my argument to the team was
[L1540] [51:39.52] that the responsibility of the storage
[L1541] [51:42.00] team is not to advocate for magic pocket
[L1542] [51:44.84] the storage system. It's to solve the
[L1543] [51:47.12] needs of storage for the organization,
[L1544] [51:50.20] right? Because who else in the company
[L1545] [51:52.08] knows more about storage than the
[L1546] [51:53.88] storage team, right? And if there was a
[L1547] [51:56.12] point in time where S3 was a better
[L1548] [51:59.68] idea,
[L1549] [52:01.04] it would make sense to move back. Or
[L1550] [52:02.64] maybe there was a different kind of
[L1551] [52:03.76] storage system that you were meant to
[L1552] [52:05.52] use, right? It's the job of the storage
[L1553] [52:08.32] team to advocate for moving back, right?
[L1554] [52:11.64] And so I've seen before, you have like a
[L1555] [52:12.96] team called the
[L1556] [52:14.88] the puppet team, you know, the
[L1557] [52:16.88] people don't really use puppet that much
[L1558] [52:17.84] anymore, but like for you know, the the
[L1559] [52:19.36] puppet the the job manager or puppet
[L1560] [52:21.28] versus chef, and then they'd be kind of
[L1561] [52:22.56] advocating for their team's thing, when
[L1562] [52:24.88] really a team should be oriented around
[L1563] [52:27.48] what problem do they solve? They should
[L1564] [52:28.88] not care about
[L1565] [52:30.92] the system that survives. Because if if
[L1566] [52:33.28] if you are on the magic pocket team,
[L1567] [52:36.12] and someone says we should move back to
[L1568] [52:38.36] S3, that's pretty threatening to your
[L1569] [52:40.92] identity and to your career,
[L1570] [52:43.52] right?
[L1571] [52:44.40] But are you If you're on the storage
[L1572] [52:46.08] team,
[L1573] [52:47.44] and it turns out it makes sense to move
[L1574] [52:49.48] back. I don't think that's the case, but
[L1575] [52:51.08] um
[L1576] [52:52.04] then that's an exciting new product for
[L1577] [52:54.12] you to own.
[L1578] [52:55.32] And so I think it's it seems like such
[L1579] [52:57.20] silly management philosophy, but I think
[L1580] [52:59.64] it's really really important to orient a
[L1581] [53:01.32] team and an identity around solving a
[L1582] [53:03.12] problem and not owning and defending a
[L1583] [53:05.36] system. Cuz you just see this in in big
[L1584] [53:07.52] companies, it's just
[L1585] [53:09.00] inertia is so strong. Yeah, and you see
[L1586] [53:11.28] people doing things they don't believe
[L1587] [53:12.60] in cuz that's just what they do.
[L1588] [53:14.52] >> If the inertia is so strong, how did you
[L1589] [53:17.40] fight it and close down all those
[L1590] [53:19.28] projects?
[L1591] [53:20.52] >> I think I got lucky
[L1592] [53:23.16] in so far as I was there pretty early
[L1593] [53:24.68] on, and I worked hard enough,
[L1594] [53:27.60] you know, I was putting in probably
[L1595] [53:29.08] 16-hour days at the start. I'm not
[L1596] [53:31.08] advocating for that, but I was like I
[L1597] [53:32.36] was dedicating my life to to the
[L1598] [53:34.20] company, and I think it became pretty
[L1599] [53:36.08] obvious to people that I cared, you
[L1600] [53:37.32] know? It This is This is Here's a guy
[L1601] [53:39.24] over here that really wants to do the
[L1602] [53:40.32] right thing and cares about the company.
[L1603] [53:42.16] At that point, you build up enough
[L1604] [53:46.00] confidence capital, you know, um, that
[L1605] [53:48.84] you feel comfortable saying things. You
[L1606] [53:51.32] know, I wasn't At that point, I wasn't
[L1607] [53:52.80] afraid for my career. I just I was
[L1608] [53:55.48] afraid for the wrong decisions getting
[L1609] [53:57.08] made. So, I So, So, I felt, you know,
[L1610] [53:59.68] psychologically comfortable making those
[L1611] [54:01.24] observations. And then, at certain
[L1612] [54:02.76] point, you, um,
[L1613] [54:04.96] you know, that there's another, you
[L1614] [54:06.08] know,
[L1615] [54:08.52] A lot of engineers, so, at one point, I
[L1616] [54:10.68] would mentor, um, you know, all the a
[L1617] [54:13.40] lot of the staff plus engineers at the
[L1618] [54:15.16] company. And And people would sometimes
[L1619] [54:17.56] get grumpy, you know, cuz they were
[L1620] [54:18.76] like, "Oh,
[L1621] [54:20.56] we're not doing the right thing over
[L1622] [54:21.68] here, or this is inefficient." And every
[L1623] [54:23.40] Every engineer listening to this has a
[L1624] [54:25.16] story like this. They're annoyed about
[L1625] [54:26.76] some inefficiency at the company. And my
[L1626] [54:29.00] response was generally like,
[L1627] [54:31.56] "Do you think we should solve this
[L1628] [54:32.72] problem right now?"
[L1629] [54:34.56] Cuz if we should, let me know the team
[L1630] [54:36.52] to take some engineers off,
[L1631] [54:38.36] and the product to shut down, and I can
[L1632] [54:40.16] redirect and we can solve this problem
[L1633] [54:41.92] right now.
[L1634] [54:43.28] And they'll be like, "Oh, well,
[L1635] [54:45.00] we shouldn't shut down any other stuff."
[L1636] [54:46.44] I'm like, "Cool, well, we just have this
[L1637] [54:47.48] many engineers right now. And And so,
[L1638] [54:50.64] if there's anything higher lower
[L1639] [54:53.00] priority, let's stop doing the lower
[L1640] [54:54.08] priority thing and do the higher
[L1641] [54:55.36] priority thing, this thing." And often
[L1642] [54:57.64] times, the answer was, "Oh, no, nothing
[L1643] [54:59.36] else is lower priority."
[L1644] [55:02.36] And then, the answer is we just have to
[L1645] [55:04.36] accept. Just have to accept, right?
[L1646] [55:06.60] There's no point in being angry or upset
[L1647] [55:09.28] that we're not doing the right thing all
[L1648] [55:10.48] the time. So, I think there's a
[L1649] [55:11.68] dimension to you break it, you bought
[L1650] [55:13.68] it. I don't think
[L1651] [55:15.72] Like, when I said part of my job was
[L1652] [55:17.08] shutting products down, it wasn't going
[L1653] [55:18.64] around just causing problems, right?
[L1654] [55:20.52] It's all Ideally, like, solving
[L1655] [55:22.20] problems. Like, "Oh, this product is not
[L1656] [55:24.28] going the right direction. Let's
[L1657] [55:26.04] redirect it and do this alternative
[L1658] [55:27.60] thing." And so, I think the thing that
[L1659] [55:29.16] helped me,
[L1660] [55:30.80] I guess, was was having a a sense of
[L1661] [55:32.76] ownership. That like, instead of
[L1662] [55:36.04] complaining,
[L1663] [55:37.88] I just wanted to go fix problems. And
[L1664] [55:39.24] that was but that was part of the
[L1665] [55:40.08] culture. I mean, there was
[L1666] [55:41.80] when I started at Dropbox
[L1667] [55:43.96] and um
[L1668] [55:45.84] I remember being at Dropbox and infra
[L1669] [55:47.28] was I don't know, seven, eight, nine
[L1670] [55:48.60] people.
[L1671] [55:49.80] And you know, we have someone join
[L1672] [55:51.92] from Google, for example, and they'd
[L1673] [55:54.08] say, "Well, someone should go build I
[L1674] [55:56.16] can't do anything without
[L1675] [55:58.52] this logging framework. Couldn't
[L1676] [55:59.68] possibly do anything without this
[L1677] [56:00.64] logging framework." And I'm like, "Well,
[L1678] [56:01.92] we're going okay without it." So and
[L1679] [56:03.68] then like someone needs to build this
[L1680] [56:04.84] thing. And everyone would be like,
[L1681] [56:06.40] "Well, who is someone?" Right? Because
[L1682] [56:08.20] it's just us. It's just us. We we build
[L1683] [56:10.64] it or we don't build it. And they'd
[L1684] [56:12.44] pretty quickly
[L1685] [56:13.92] come to understand, "Oh, wait, it's just
[L1686] [56:15.76] us. It's just we There's There's no
[L1687] [56:18.12] other idiots out there. We're the
[L1688] [56:19.48] idiots, right?" So
[L1689] [56:21.52] that was I don't know, I loved I loved
[L1690] [56:23.80] that time because it was just a
[L1691] [56:26.04] uh time of accountability that
[L1692] [56:29.24] life gets easier and harder when you
[L1693] [56:32.24] realize that everyone else is not an
[L1694] [56:33.92] idiot.
[L1695] [56:35.00] When you realize everyone else is just
[L1696] [56:37.32] dealing with their own stuff, right?
[L1697] [56:38.83] >> [laughter]
[L1698] [56:39.68] >> And so I think um
[L1699] [56:42.44] I I do not think someone will have good
[L1700] [56:44.60] luck going around complaining about
[L1701] [56:47.08] stuff and and just saying this is a dumb
[L1702] [56:48.96] idea and being negative. I think people
[L1703] [56:51.48] will have a um
[L1704] [56:53.92] Everyone wants problems solved though.
[L1705] [56:55.92] So if you're someone in an organization
[L1706] [56:57.64] who is who's willing to put their head
[L1707] [56:59.28] up and say, "You know what? I think this
[L1708] [57:01.04] thing over here is a bad idea,
[L1709] [57:03.48] but here's a different idea and I'm
[L1710] [57:05.92] willing to own it and put the effort
[L1711] [57:07.28] behind it." I think that's a that's a
[L1712] [57:09.76] recipe for success.
[L1713] [57:11.12] >> From that article, you had a great quote
[L1714] [57:13.08] or I guess a great question to think
[L1715] [57:15.96] through this. It said you went to
[L1716] [57:17.76] everyone or a bunch of people and you
[L1717] [57:19.48] would say "If we could be spending these
[L1718] [57:21.72] resources working on any project at the
[L1719] [57:23.96] company right now, would this still be
[L1720] [57:26.16] the best use of time?" And I feel like
[L1721] [57:28.84] it frames exactly what you just
[L1722] [57:30.60] described really cleanly.
[L1723] [57:32.48] >> Yeah, I mean I guess this is like maybe
[L1724] [57:34.12] a a trick for being a tech lead or a
[L1725] [57:36.04] manager is
[L1726] [57:38.00] almost nothing's a yes or no question.
[L1727] [57:39.84] It's a like it's a prioritization
[L1728] [57:41.52] question. Yeah, it's not like should we
[L1729] [57:43.88] redesign the database? I don't know,
[L1730] [57:45.24] maybe. I guess. Is it the most important
[L1731] [57:47.40] thing to do right now? No. Cool, let's
[L1732] [57:48.84] not do it. Right? I think it's much
[L1733] [57:50.68] easier to have those conversations than
[L1734] [57:52.84] to think about it as a yes or no. You
[L1735] [57:55.08] know, I often hear like, "Oh, my VP
[L1736] [57:56.60] won't let me do blah."
[L1737] [57:58.88] Okay. Well, it could be that your VP is
[L1738] [58:01.72] dumb, but it's probably not, right? It
[L1739] [58:03.80] could be that your VP has a different
[L1740] [58:05.28] set of priorities. Maybe their VP knows
[L1741] [58:06.92] that you need to ship these features and
[L1742] [58:09.08] if you don't, then the company's going
[L1743] [58:10.16] to be struggling. I don't know, but to
[L1744] [58:12.56] to really frame it around
[L1745] [58:14.52] prioritization. And the way I think
[L1746] [58:16.16] about the the career ladder for
[L1747] [58:17.72] engineers
[L1748] [58:19.16] is is I I think um some people, maybe
[L1749] [58:22.84] maybe it's not common, but think that
[L1750] [58:24.12] like being coming a senior senior
[L1751] [58:25.64] engineer means you get better at
[L1752] [58:26.68] programming.
[L1753] [58:27.96] But like I don't know. I think my
[L1754] [58:29.04] programmability is went down from like
[L1755] [58:31.80] level four onwards. You know, I think
[L1756] [58:33.44] once I got to like level four,
[L1757] [58:35.43] >> [laughter]
[L1758] [58:35.48] >> that was peak programmer for me and then
[L1759] [58:37.52] I probably went downhill from there. And
[L1760] [58:39.60] I got wiser, whatever, but I think the
[L1761] [58:42.12] real thing that happened is the scope
[L1762] [58:44.96] that I cared about increased. So, at a
[L1763] [58:47.00] certain point you just think about,
[L1764] [58:48.24] "Cool, what matters most at the company
[L1765] [58:49.96] for the next five years?"
[L1766] [58:51.72] Um and
[L1767] [58:53.72] I don't think uh
[L1768] [58:55.52] junior engineer on their first year of
[L1769] [58:57.28] the job should try to do this.
[L1770] [58:59.88] Cuz you probably don't yet have the
[L1771] [59:02.56] wisdom, insight,
[L1772] [59:04.28] um knowledge to be able to make a good
[L1773] [59:06.56] assessment. And I think it probably
[L1774] [59:07.92] would be a mistake to be like to try to
[L1775] [59:09.56] come up with like
[L1776] [59:11.76] redirecting company strategy. But as you
[L1777] [59:13.96] grow, I think the real key part about
[L1778] [59:16.40] growing is the the the IC6, 7, 8
[L1779] [59:19.92] engineers are not necessarily the best
[L1780] [59:21.68] programmers. It's they're just getting
[L1781] [59:23.48] better at having broad perspective
[L1782] [59:26.44] in decisions within a company.
[L1783] [59:29.28] >> OpenAI, Anthropic, Cursor, and Vercel
[L1784] [59:33.12] all use this product to make their lives
[L1785] [59:34.84] better. And the problem it solves is
[L1786] [59:37.44] when you're building SaaS or an AI
[L1787] [59:39.08] product and you want to sell to other
[L1788] [59:41.08] companies, there's all these
[L1789] [59:42.68] requirements you need to meet. There's
[L1790] [59:44.64] SSL, there's SCIM, there's RBAC, there's
[L1791] [59:48.16] audit logs. These are all things that
[L1792] [59:49.92] take time to integrate, but aren't the
[L1793] [59:52.04] main focus of your app. WorkOS is an API
[L1794] [59:54.64] layer that lets you meet all of these
[L1795] [59:56.16] requirements in just a few lines of
[L1796] [59:58.24] code. So, let's say you have a new SaaS
[L1797] [01:00:00.48] product and you want to sell to other
[L1798] [01:00:02.00] companies, WorkOS will solve all of
[L1799] [01:00:04.40] these critical feature gaps for you.
[L1800] [01:00:07.00] You can check them out at workos.com to
[L1801] [01:00:09.48] learn more and get started. And I
[L1802] [01:00:11.64] appreciate them for supporting my work
[L1803] [01:00:13.52] and sponsoring this podcast.
[L1804] [01:00:15.28] >> You mentioned this idea of do the right
[L1805] [01:00:17.76] thing and then, you know, the byproduct
[L1806] [01:00:19.88] you also get promoted. And I think
[L1807] [01:00:21.24] that's that's the dream, you know, do
[L1808] [01:00:23.40] the right thing, get promoted. But in
[L1809] [01:00:26.28] reality, often times people would have
[L1810] [01:00:28.64] to make the trade-off. Imagine a two by
[L1811] [01:00:31.00] two matrix of doing the right thing,
[L1812] [01:00:33.28] doing the wrong thing,
[L1813] [01:00:34.84] getting promoted, not getting promoted.
[L1814] [01:00:37.48] Obviously, the, you know, do the right
[L1815] [01:00:39.84] thing, get promoted, great. Do the wrong
[L1816] [01:00:42.04] thing, don't get promoted, obviously
[L1817] [01:00:44.04] bad. But I'm curious about the other two
[L1818] [01:00:46.24] quadrants. Which one would you have
[L1819] [01:00:47.96] picked when you were earlier in your
[L1820] [01:00:49.92] career? Let's say I came to you, I said,
[L1821] [01:00:51.28] "Hey, you can do the wrong thing, but
[L1822] [01:00:53.88] you're going to get promoted. Or you can
[L1823] [01:00:56.36] do the right thing and I guarantee
[L1824] [01:00:58.24] you're not going to get promoted. Which
[L1825] [01:00:59.68] one?"
[L1826] [01:01:00.08] >> one.
[L1827] [01:01:00.36] >> Absolutely the second
[L1828] [01:01:00.88] >> The second one.
[L1829] [01:01:01.40] >> So, I'm going to say a really tacky
[L1830] [01:01:02.64] thing, right? Um
[L1831] [01:01:05.00] there are a set of engineers
[L1832] [01:01:07.12] um
[L1833] [01:01:08.32] who at a certain point just make
[L1834] [01:01:10.08] infinity money. Like, the amount of
[L1835] [01:01:12.24] money they can make, you know, going and
[L1836] [01:01:14.56] whatever, going to work at Anthropic is
[L1837] [01:01:16.40] is a huge amount of money, right? And
[L1838] [01:01:18.88] so, there's a certain point where it
[L1839] [01:01:21.00] just doesn't matter anymore. Like the
[L1840] [01:01:22.40] money is whatever, right? But so that So
[L1841] [01:01:26.00] if you really want to
[L1842] [01:01:27.68] If you really want to maximize long-term
[L1843] [01:01:29.72] income, I don't think you should try to
[L1844] [01:01:31.12] do that, but if you wanted to maximize
[L1845] [01:01:32.76] long-term income, if you get to a
[L1846] [01:01:34.88] certain level of experience and skill
[L1847] [01:01:37.20] and seniority, you've made it. That's
[L1848] [01:01:39.36] it. You're done. Money's fine, right?
[L1849] [01:01:41.72] And so I think there's this desire
[L1850] [01:01:44.24] amongst
[L1851] [01:01:45.32] junior engineers early in their career
[L1852] [01:01:47.44] to be kind of over optimizing for
[L1853] [01:01:50.64] promotion and and income and salary,
[L1854] [01:01:53.76] etc.
[L1855] [01:01:55.36] as opposed to investing in themselves.
[L1856] [01:01:58.32] And I guess it's it's They probably
[L1857] [01:02:00.08] don't want to hear me say this cuz it's
[L1858] [01:02:01.44] easier for me as an old old guy to say
[L1859] [01:02:03.52] this, right? But But I think
[L1860] [01:02:06.00] you know, for the longest time at
[L1861] [01:02:07.56] Dropbox, there was a time at Dropbox
[L1862] [01:02:08.92] where like we just didn't have our level
[L1863] [01:02:10.20] system right. I was tech leading the
[L1864] [01:02:11.80] team and I was making the least amount
[L1865] [01:02:13.20] of money of the team. I'm cuz I was at
[L1866] [01:02:14.92] some point a technical manager. I saw
[L1867] [01:02:16.16] everyone's salaries. I was making the
[L1868] [01:02:18.00] least I think the least money, but
[L1869] [01:02:19.44] whatever, right? It all worked out in
[L1870] [01:02:21.24] the end, right? Now that was a happy
[L1871] [01:02:23.12] story, but I do really think
[L1872] [01:02:25.92] I benefit so much from working with the
[L1873] [01:02:28.32] best people. Like if you have two
[L1874] [01:02:30.12] choices, like
[L1875] [01:02:32.00] making 20% more money now or working
[L1876] [01:02:35.12] with like the best people in the world,
[L1877] [01:02:38.08] right? Just be around the best people
[L1878] [01:02:40.40] because like you will be
[L1879] [01:02:43.08] that's going to sit you on like the on
[L1880] [01:02:45.28] the ship to success, right? And now Not
[L1881] [01:02:48.24] everyone wants to do that. Not everyone
[L1882] [01:02:50.16] wants to go on that Like it's There's no
[L1883] [01:02:53.08] shame in just wanting to be have a
[L1884] [01:02:54.84] regular job and just be chilling and
[L1885] [01:02:56.88] just be getting paid and fine.
[L1886] [01:02:59.56] There's There's nothing wrong with that.
[L1887] [01:03:01.48] But if you do want to maximize If you
[L1888] [01:03:03.64] want to maximize your career growth,
[L1889] [01:03:07.28] then the way to maximize that is to
[L1890] [01:03:08.44] maximize your skills, right? Like if
[L1891] [01:03:12.08] And And hopefully you're not so cynical
[L1892] [01:03:14.00] to think that there is no correlation
[L1893] [01:03:15.48] between talent and compensation. Um
[L1894] [01:03:19.20] I don't
[L1895] [01:03:20.64] If you think that's the case, okay, um I
[L1896] [01:03:23.88] don't know what to say. But but but but
[L1897] [01:03:26.16] there is a correlation between talent
[L1898] [01:03:27.92] and compensation and growth. And so, my
[L1899] [01:03:30.96] advice to people early in their career
[L1900] [01:03:32.92] is land at the best company with the
[L1901] [01:03:35.40] best people doing the most important
[L1902] [01:03:36.84] problems, and your life will be great
[L1903] [01:03:39.60] cuz we are so lucky as engineers. Like
[L1904] [01:03:41.88] What what what else could What else can
[L1905] [01:03:43.52] you work solving problems for a job?
[L1906] [01:03:45.92] Like solving puzzles for a job and
[L1907] [01:03:47.48] getting paid so [snorts] well. Like
[L1908] [01:03:49.40] engineers get paid so well compared to
[L1909] [01:03:51.24] most jobs. Um
[L1910] [01:03:53.36] The privilege that the real privilege
[L1911] [01:03:57.08] that we get is to work on something
[L1912] [01:03:59.04] cool.
[L1913] [01:04:00.04] And uh that's what I advocate for.
[L1914] [01:04:02.64] >> I love the idea you mentioned earlier
[L1915] [01:04:05.48] that's kind of counter to the common
[L1916] [01:04:08.56] opinion I I often hear. Like the common
[L1917] [01:04:10.84] opinion I hear they someone working at a
[L1918] [01:04:13.24] big company, they're in this machine,
[L1919] [01:04:15.76] that it's kind of defeatist. They're
[L1920] [01:04:17.36] going, "Ah, I ship this thing, but I
[L1921] [01:04:18.76] hate this or I don't believe in this."
[L1922] [01:04:21.48] And the I I really liked your
[L1923] [01:04:23.32] perspective on you doing the right thing
[L1924] [01:04:26.28] and like
[L1925] [01:04:27.48] basically giving a damn that
[L1926] [01:04:29.76] you know, someone outside of you is
[L1927] [01:04:31.80] doing the right thing, too, and
[L1928] [01:04:33.28] expanding your sense of ownership. And I
[L1929] [01:04:36.60] want to know what is your motivation for
[L1930] [01:04:38.72] that cuz there's so many other people
[L1931] [01:04:40.16] who are faced with the same inputs and
[L1932] [01:04:42.36] they get to a very different conclusion.
[L1933] [01:04:44.08] So, what motivates you to actually do
[L1934] [01:04:47.08] the right thing when
[L1935] [01:04:48.68] the machine doesn't necessarily
[L1936] [01:04:50.32] incentivize you to do so?
[L1937] [01:04:51.72] >> Yeah.
[L1938] [01:04:53.12] Well, I think the machine does
[L1939] [01:04:54.08] incentivize you to do so, but I don't
[L1940] [01:04:55.36] think it's it's visible
[L1941] [01:04:57.28] immediately. Like I think people who
[L1942] [01:04:59.20] sample who who do less job hopping
[L1943] [01:05:01.60] really do grow the most because I was I
[L1944] [01:05:04.64] would say very strongly, if you're not
[L1945] [01:05:06.16] in a job for 3 years, you're not going
[L1946] [01:05:08.36] to see
[L1947] [01:05:09.68] whether your decisions were good. Like
[L1948] [01:05:11.40] you you can get more money as a junior
[L1949] [01:05:13.60] engineer, but you cannot become a senior
[L1950] [01:05:16.48] a very talented senior engineer without
[L1951] [01:05:18.28] being around for long enough to own the
[L1952] [01:05:20.56] consequences of your decisions.
[L1953] [01:05:22.48] It's It's like It's like playing a
[L1954] [01:05:23.92] basketball game and leaving before the
[L1955] [01:05:25.68] game's over. Like, you're just not
[L1956] [01:05:28.52] learning, right? So, so
[L1957] [01:05:31.24] I do think there's an actual structural
[L1958] [01:05:32.88] incentive towards staying in a job. Now,
[L1959] [01:05:34.92] if you're in a bad job, leave the bad
[L1960] [01:05:36.24] job, right? But there's a structural
[L1961] [01:05:37.60] incentive to be able to stay long enough
[L1962] [01:05:39.00] to have an impact.
[L1963] [01:05:41.08] But also, I don't know. I like
[L1964] [01:05:44.32] again, I guess it's easy for me to say.
[L1965] [01:05:46.08] And also, I joined the tech industry
[L1966] [01:05:47.44] when it wasn't like a very lucrative
[L1967] [01:05:49.52] field.
[L1968] [01:05:50.60] Like it you know, it
[L1969] [01:05:52.12] it wasn't like it is now, you know? But
[L1970] [01:05:54.28] I just like it. The reason I left
[L1971] [01:05:55.92] academia
[L1972] [01:05:57.56] was because I wasn't confident I was
[L1973] [01:06:00.08] making the right So, what would happen
[L1974] [01:06:02.12] how I would how I was in academia, I'm
[L1975] [01:06:05.00] not saying everyone was like this, but
[L1976] [01:06:06.76] you So, firstly, you you don't know what
[L1977] [01:06:08.96] to do.
[L1978] [01:06:10.08] So, you have to make up a problem to
[L1979] [01:06:11.16] solve. And then you make up a problem.
[L1980] [01:06:14.16] And then you make up a solution.
[L1981] [01:06:16.04] You know, and hopefully a good one.
[L1982] [01:06:18.44] And then you write a paper where you try
[L1983] [01:06:20.64] to convince everyone that it was a
[L1984] [01:06:21.96] really good idea.
[L1985] [01:06:23.76] >> [laughter]
[L1986] [01:06:24.24] >> And I hated it cuz I didn't want to
[L1987] [01:06:26.24] convince people. I just wanted to build
[L1988] [01:06:28.20] it
[L1989] [01:06:29.04] and see if it was good. Like, I just
[L1990] [01:06:31.48] wanted to build it and ship it and see I
[L1991] [01:06:33.72] didn't want to
[L1992] [01:06:35.16] play pretends and and argue about it was
[L1993] [01:06:37.44] good. Um that's what makes me feel good.
[L1994] [01:06:40.56] I don't know. And like, obviously
[L1995] [01:06:44.08] if you're a engineer who's living
[L1996] [01:06:46.60] paycheck to paycheck,
[L1997] [01:06:48.44] you should maybe ignore what I'm saying.
[L1998] [01:06:50.20] Like, I don't want to come across as
[L1999] [01:06:52.24] unempathetic to anyone who's really
[L2000] [01:06:53.80] struggling financially.
[L2001] [01:06:55.80] But if you are not struggling
[L2002] [01:06:57.28] financially,
[L2003] [01:06:59.44] the
[L2004] [01:07:00.64] best thing you can do for your quality
[L2005] [01:07:02.60] of life
[L2006] [01:07:03.88] is
[L2007] [01:07:05.52] you know, in me enjoying what you do
[L2008] [01:07:07.52] every day.
[L2009] [01:07:08.72] You know, like I don't know, you could
[L2010] [01:07:09.56] have a fancier car
[L2011] [01:07:12.00] or you can enjoy what you do every day.
[L2012] [01:07:14.68] And I love cars, like I'm a I'm a motor
[L2013] [01:07:16.28] head, but I promise that enjoying what
[L2014] [01:07:19.20] you do every day is going to have a much
[L2015] [01:07:20.92] bigger impact on your life. And um
[L2016] [01:07:23.24] personally, I don't enjoy like going to
[L2017] [01:07:25.72] work and and working on projects I don't
[L2018] [01:07:27.52] believe in. Like I can only
[L2019] [01:07:29.72] operate. And so you Jamie, my
[L2020] [01:07:30.72] co-founder, is the same way. Like
[L2021] [01:07:32.92] we we really get along really well in
[L2022] [01:07:34.52] this respect.
[L2023] [01:07:35.72] We can only um
[L2024] [01:07:38.28] we can only put up with doing things we
[L2025] [01:07:39.68] actually care about and
[L2026] [01:07:42.08] and believe in.
[L2027] [01:07:43.40] And I think
[L2028] [01:07:44.92] that's that's the luxury That's more
[L2029] [01:07:47.28] luxury than taking a first-class flight.
[L2030] [01:07:49.04] That's more luxury than going to a
[L2031] [01:07:50.36] three-Michelin-star restaurant.
[L2032] [01:07:52.12] The luxury is you don't get up and have
[L2033] [01:07:54.52] to do a a terrible job, you know, um you
[L2034] [01:07:57.72] get up and go to a place that you like
[L2035] [01:07:59.68] your co-workers, and you solve cool
[L2036] [01:08:02.28] problems, and you go home and feel proud
[L2037] [01:08:03.92] of yourself.
[L2038] [01:08:05.08] If you can If you can construct your
[L2039] [01:08:07.52] career that way, and it's not easy, you
[L2040] [01:08:09.04] have to It requires very active effort,
[L2041] [01:08:11.32] then you're going to have a good life.
[L2042] [01:08:13.40] >> I I saw on your career journey
[L2043] [01:08:16.00] it said that you're occasional manager.
[L2044] [01:08:18.68] And you you seem like someone who really
[L2045] [01:08:20.84] enjoys the the technical aspects of
[L2046] [01:08:22.92] things. So, how did you decide to
[L2047] [01:08:25.28] occasionally dip into management?
[L2048] [01:08:27.64] >> I feel
[L2049] [01:08:29.32] like most people should not want to be
[L2050] [01:08:31.08] managers.
[L2051] [01:08:32.52] And I sometimes think it's a bit of a
[L2052] [01:08:33.80] red flag if someone wants to be a
[L2053] [01:08:35.04] manager too much, right?
[L2054] [01:08:37.28] Cuz um being a manager is a hard job.
[L2055] [01:08:40.12] And uh so, I think most people should go
[L2056] [01:08:42.72] into management because they need to.
[L2057] [01:08:44.52] Cuz it's necessary. And so, what
[L2058] [01:08:45.92] happened every time I went into
[L2059] [01:08:47.24] management, I'm in a management role now
[L2060] [01:08:48.88] as well, cuz you have to, right? Um
[L2061] [01:08:51.80] but um
[L2062] [01:08:53.44] we someone needed to manage the team.
[L2063] [01:08:55.40] And and so, I do genuinely enjoy
[L2064] [01:08:58.08] accountability. I like responsibility. I
[L2065] [01:08:59.92] like
[L2066] [01:09:00.88] I like um having weight on my shoulders,
[L2067] [01:09:03.96] I I suppose.
[L2068] [01:09:05.68] And so I went into management
[L2069] [01:09:07.96] several times.
[L2070] [01:09:09.68] Uh but as soon as I had the opportunity
[L2071] [01:09:10.96] to get out, as soon as someone else
[L2072] [01:09:12.00] would come in and manage the team, I
[L2073] [01:09:13.04] would I would kind of bounce out of that
[L2074] [01:09:14.48] role back into engineering.
[L2075] [01:09:16.24] Um
[L2076] [01:09:17.24] Now, going to management is is is
[L2077] [01:09:18.76] tremendously educational.
[L2078] [01:09:21.16] If um
[L2079] [01:09:22.36] being a manager really lets you see the
[L2080] [01:09:24.44] world in a different way. You realize
[L2081] [01:09:26.48] companies are more complicated than you
[L2082] [01:09:27.68] thought. You realize the engineers are
[L2083] [01:09:29.28] more complicated than you thought. You
[L2084] [01:09:30.24] realize everyone on the team is going
[L2085] [01:09:31.64] through something. And you And you
[L2086] [01:09:33.56] realize, "Oh, wow, now I understand why
[L2087] [01:09:35.48] that thing happened." Um so, being a
[L2088] [01:09:37.20] manager is very educational.
[L2089] [01:09:39.08] One thing I would say I would strongly
[L2090] [01:09:41.28] caution people against is going into
[L2091] [01:09:43.08] management too early in their career.
[L2092] [01:09:45.04] And I see this happen
[L2093] [01:09:47.32] um
[L2094] [01:09:47.96] I see this happen a lot with
[L2095] [01:09:49.52] well-intentioned people
[L2096] [01:09:51.64] who want to push people into management
[L2097] [01:09:53.20] as a means of career advancement, right?
[L2098] [01:09:56.16] I think it's doing people a disservice.
[L2099] [01:09:57.48] I think you should let folks take their
[L2100] [01:10:00.20] time
[L2101] [01:10:01.32] in an organiza- in a in a career
[L2102] [01:10:03.36] journey. I don't think you should be
[L2103] [01:10:04.84] going into management
[L2104] [01:10:06.52] under most circumstances in the first 3
[L2105] [01:10:08.20] years of your career. I think you should
[L2106] [01:10:09.40] get to
[L2107] [01:10:10.64] ideally get to staff engineer before you
[L2108] [01:10:12.48] do that. That's not going to happen for
[L2109] [01:10:13.72] everybody, but ideally you take the time
[L2110] [01:10:15.80] because if you go into management before
[L2111] [01:10:18.12] you're excellent technician,
[L2112] [01:10:20.80] it will limit your ability to influence
[L2113] [01:10:23.12] strategy later in your career.
[L2114] [01:10:24.88] >> How does that play out?
[L2115] [01:10:26.04] >> It plays out with people who um who uh
[L2116] [01:10:29.64] s-
[L2117] [01:10:30.32] stuck or have roles as people managers
[L2118] [01:10:33.00] where, you know, they they see their job
[L2119] [01:10:35.04] as making maybe making a team happy
[L2120] [01:10:37.52] or maybe coordinating a team
[L2121] [01:10:39.60] um or, you know, dealing with all the
[L2122] [01:10:41.68] day-to-day
[L2123] [01:10:43.04] um
[L2124] [01:10:44.20] challenges of like people on a team, but
[L2125] [01:10:46.44] they're not
[L2126] [01:10:47.68] organizational leaders.
[L2127] [01:10:49.52] They're not like pushing the team
[L2128] [01:10:51.80] towards excellence. They They're not
[L2129] [01:10:53.12] like, "Hey, how can we reframe what this
[L2130] [01:10:55.44] team is about? How can we, you know,
[L2131] [01:10:57.72] help influence technical strategy? And
[L2132] [01:10:59.88] um
[L2133] [01:11:01.28] again, people management is a fine job,
[L2134] [01:11:03.48] but I think
[L2135] [01:11:05.12] um the best companies are ones where all
[L2136] [01:11:07.92] the managers are very technical. And so,
[L2137] [01:11:10.12] they're able to make sure the company's
[L2138] [01:11:11.76] doing like at a certain point like if
[L2139] [01:11:13.56] you're not
[L2140] [01:11:14.48] not a particularly technical manager,
[L2141] [01:11:16.28] you're not going to be able to evaluate
[L2142] [01:11:18.04] the work of your team. You're not going
[L2143] [01:11:19.24] to know whether your team is even doing
[L2144] [01:11:20.68] well. And I guess maybe you might
[L2145] [01:11:22.36] contribute towards some of the stuff you
[L2146] [01:11:23.92] were saying about, you know, cynical
[L2147] [01:11:25.84] organizational attitudes where like my
[L2148] [01:11:27.76] manager doesn't understand me. Maybe
[L2149] [01:11:29.68] your manager doesn't understand you
[L2150] [01:11:31.61] >> [laughter]
[L2151] [01:11:31.80] >> if they haven't spent enough time
[L2152] [01:11:33.40] developing technical skills and and and
[L2153] [01:11:35.40] and and struggling.
[L2154] [01:11:36.92] >> Yeah, there's uh another uh piece that
[L2155] [01:11:39.72] you wrote I thought was really good
[L2156] [01:11:41.52] about, you know, leading by example and
[L2157] [01:11:44.20] you actually say it's bad to lead by
[L2158] [01:11:45.64] example, but um
[L2159] [01:11:47.28] there there's a quote in there. It says
[L2160] [01:11:49.96] modern tech workers can be an
[L2161] [01:11:51.68] anti-authoritarian bunch at the best of
[L2162] [01:11:54.04] times. And
[L2163] [01:11:55.72] let's say you're a a tech lead or tech
[L2164] [01:11:57.60] lead manager or manager, you know, how
[L2165] [01:11:59.76] how do you strike that balance so you
[L2166] [01:12:01.24] don't lose credibility as a tech lead?
[L2167] [01:12:03.88] >> Yeah, there there are command and
[L2168] [01:12:05.84] control companies
[L2169] [01:12:07.64] that like the manager just tells people
[L2170] [01:12:09.48] to do things and they just do them.
[L2171] [01:12:12.52] Those typically are not excellent
[L2172] [01:12:14.72] companies. And not every company needs
[L2173] [01:12:16.52] to be excellent, but if you want to have
[L2174] [01:12:19.56] a company where
[L2175] [01:12:21.28] the team's really innovating, like the
[L2176] [01:12:23.00] engineers feel very personally
[L2177] [01:12:24.60] responsible for making really
[L2178] [01:12:25.80] high-quality decisions,
[L2179] [01:12:27.64] you have to have them believe in what
[L2180] [01:12:29.32] you're doing.
[L2181] [01:12:30.44] And so, you you know, at Convex, I'm the
[L2182] [01:12:32.16] founder and CTO.
[L2183] [01:12:34.08] I can't really go to someone's desk and
[L2184] [01:12:35.92] say do this thing.
[L2185] [01:12:37.88] Now, they they might do it just cuz they
[L2186] [01:12:39.24] like me. There's a good chance they
[L2187] [01:12:40.64] would do it, but not because I'm the
[L2188] [01:12:41.88] boss. They'd be like, "Well, why?"
[L2189] [01:12:44.24] Right? And that's that's because that's
[L2190] [01:12:45.56] our culture. I mean, we don't just do
[L2191] [01:12:47.44] things cuz we're told. Like if I want
[L2192] [01:12:49.40] someone to do something, I'll spend time
[L2193] [01:12:51.88] with the team talking about why we're
[L2194] [01:12:53.80] doing it. Where Where the market's
[L2195] [01:12:55.24] trending? Where's the gap in our
[L2196] [01:12:56.48] product? What, you know? And then once
[L2197] [01:12:59.04] we've really well articulated
[L2198] [01:13:01.72] um
[L2199] [01:13:02.68] why something matters, people are just
[L2200] [01:13:04.24] going to do it anyway. Now Now there's a
[L2201] [01:13:06.28] Sometimes you have to have hard
[L2202] [01:13:07.12] conversations, but I think um the way I
[L2203] [01:13:09.76] think about it in terms of certainly in
[L2204] [01:13:11.04] terms of conflict in an organization,
[L2205] [01:13:12.48] there's like this kind of hierarchy of
[L2206] [01:13:14.60] of the values you have, and then why,
[L2207] [01:13:17.20] what, and how.
[L2208] [01:13:18.96] And engineers are very often debating
[L2209] [01:13:20.72] the how. They're very often debating
[L2210] [01:13:22.16] like what algorithm should we use for
[L2211] [01:13:24.40] this? And like, you know, should we use
[L2212] [01:13:26.88] this container service or that container
[L2213] [01:13:28.32] service? And these are kind of like the
[L2214] [01:13:30.12] implementation details.
[L2215] [01:13:32.52] But most times when I see organizational
[L2216] [01:13:34.96] conflict, it's because well-intentioned
[L2217] [01:13:37.20] people
[L2218] [01:13:38.56] uh debating as best they can about how
[L2219] [01:13:40.60] to do something, but they don't agree on
[L2220] [01:13:42.04] why we're doing it.
[L2221] [01:13:43.64] So if if one team thinks the most
[L2222] [01:13:45.28] important thing we can do right now is
[L2223] [01:13:46.80] get more features out to expand our
[L2224] [01:13:48.88] customer base, and the other team thinks
[L2225] [01:13:50.68] the most important thing we can do is
[L2226] [01:13:52.00] increase reliability cuz there's a risk
[L2227] [01:13:53.56] to the business, right? They're both
[L2228] [01:13:55.48] very valid perspectives, but it's going
[L2229] [01:13:57.56] to lead to them doing very different
[L2230] [01:13:59.84] things.
[L2231] [01:14:00.96] And within an organization, I'm a strong
[L2232] [01:14:03.56] believer that everyone needs to have
[L2233] [01:14:04.92] 100% why alignment. So the stuff we
[L2234] [01:14:08.60] argue about or we debate or we talk
[L2235] [01:14:10.48] about ad nauseam is why.
[L2236] [01:14:13.04] And then largely I just trust the team
[L2237] [01:14:14.56] to do the right thing.
[L2238] [01:14:15.88] Um and I think that's the case for any
[L2239] [01:14:17.44] in any tech lead. If you want to have
[L2240] [01:14:18.76] credibility on a team,
[L2241] [01:14:21.24] it's not If you think that you can just
[L2242] [01:14:23.84] tell someone to do something and they'll
[L2243] [01:14:26.32] listen to me cuz I'm the senior guy, and
[L2244] [01:14:28.88] no, they won't. They won't. If they
[L2245] [01:14:30.72] listen to me, it's cuz I've come in and
[L2246] [01:14:32.44] explained it in a way that resonates
[L2247] [01:14:34.08] with them. And again, one of my jobs at
[L2248] [01:14:35.72] Dropbox was to resolve the situations.
[L2249] [01:14:37.96] You know, someone would say, "Oh, that
[L2250] [01:14:39.92] team's an idiot. They won't do blah
[L2251] [01:14:41.56] this." And then I'd go talk to that
[L2252] [01:14:42.80] team. That team was not an idiot, right?
[L2253] [01:14:45.12] And we talked through it, and they would
[L2254] [01:14:46.72] decide to do the project. And it wasn't
[L2255] [01:14:48.36] because
[L2256] [01:14:50.36] they were scared of me. I hope they
[L2257] [01:14:52.00] weren't at least. It was because, you
[L2258] [01:14:54.08] know, I take the time to figure out what
[L2259] [01:14:56.28] their motivations are. And And that's
[L2260] [01:14:57.80] something you really have to learn. If
[L2261] [01:14:59.00] you're a tech lead, you don't really
[L2262] [01:15:00.96] have that much authority over people.
[L2263] [01:15:02.72] And really you have to kind of encourage
[L2264] [01:15:05.72] them and get them to believe in what
[L2265] [01:15:06.92] you're doing.
[L2266] [01:15:08.36] Um and if you are leading through
[L2267] [01:15:10.56] authority, you're not going to have a
[L2268] [01:15:13.44] culture where good ideas arise from
[L2269] [01:15:16.84] within the org. People are just going to
[L2270] [01:15:18.44] do what they're told.
[L2271] [01:15:19.92] >> Influence without authority is huge, and
[L2272] [01:15:22.60] I think there's I mean, even big
[L2273] [01:15:24.40] companies like Meta, they technically
[L2274] [01:15:26.96] don't have titles. Everyone's just a
[L2275] [01:15:28.40] software engineer. Um is that also how
[L2276] [01:15:31.60] Convex is run?
[L2277] [01:15:33.00] >> I mean, we're We're a very flat
[L2278] [01:15:34.72] organization. There are people in tech
[L2279] [01:15:36.12] lead roles.
[L2280] [01:15:37.40] I don't completely buy the everyone's a
[L2281] [01:15:40.48] software engineer thing. It's like, you
[L2282] [01:15:41.84] know, at I is is is
[L2283] [01:15:44.32] you know, Entropic. Like, everyone's a
[L2284] [01:15:45.52] member of technical staff. Because it's
[L2285] [01:15:47.64] kind of like a wink wink thing. You kind
[L2286] [01:15:50.08] of know. It's like no one's mentioned
[L2287] [01:15:52.44] the title, but you kind of know if like
[L2288] [01:15:54.48] the most senior person in the company
[L2289] [01:15:55.88] comes to your desk, you're probably
[L2290] [01:15:57.28] going to notice, you know? And uh and so
[L2291] [01:16:00.36] I think there's no point in in in, you
[L2292] [01:16:02.64] know, playing pretends. People People
[L2293] [01:16:04.60] know, you know? But I will say that you
[L2294] [01:16:06.96] should have a organizational culture
[L2295] [01:16:08.56] where you don't do something just
[L2296] [01:16:10.00] because a senior person says something.
[L2297] [01:16:12.32] Now, I do think that reputation matters.
[L2298] [01:16:15.88] Like, I certainly think that, you know,
[L2299] [01:16:17.20] I don't know. If If If a If a very
[L2300] [01:16:19.64] experienced person at a at a company
[L2301] [01:16:21.40] comes and tries to explain something to
[L2302] [01:16:23.32] you, you probably should listen to them
[L2303] [01:16:25.20] because they probably have some wisdom.
[L2304] [01:16:27.20] There might be something to be learned
[L2305] [01:16:28.32] there. You should be open to it. But
[L2306] [01:16:30.12] ultimately, um
[L2307] [01:16:32.16] yeah, even even the most senior person I
[L2308] [01:16:34.04] don't think um
[L2309] [01:16:36.04] should be leading through authority.
[L2310] [01:16:37.72] They They
[L2311] [01:16:38.96] They They should use the benefit of
[L2312] [01:16:40.24] their experience to be able to artic to
[L2313] [01:16:42.20] win the hearts and minds. And and that's
[L2314] [01:16:44.36] how you in engineering culture is so
[L2315] [01:16:46.92] important. And if you want a culture of
[L2316] [01:16:48.88] of ownership and innovation and and
[L2317] [01:16:51.28] drive and enthusiasm and people trying
[L2318] [01:16:53.28] to do the right thing, not get promoted,
[L2319] [01:16:54.96] right? You have to have a culture where
[L2320] [01:16:56.64] everyone believes in what they're doing.
[L2321] [01:16:58.44] And no one's going to believe in what
[L2322] [01:16:59.64] they're doing if the senior principal
[L2323] [01:17:01.60] engineer comes to the desk and says,
[L2324] [01:17:04.68] "I'm not going to tell you why, but you
[L2325] [01:17:05.68] have to delete this database and do this
[L2326] [01:17:07.04] other thing." And
[L2327] [01:17:08.24] no, that that's not an empowering
[L2328] [01:17:09.96] statement. What the empowering statement
[L2329] [01:17:11.72] is, "Hey, let's spend some time together
[L2330] [01:17:13.84] to talk about where this product's
[L2331] [01:17:15.72] trending and how this is probably not
[L2332] [01:17:17.16] going to work out and how there might be
[L2333] [01:17:18.72] a different way we can solve this
[L2334] [01:17:19.68] problem."
[L2335] [01:17:20.44] >> Uh on the topic of tech leadership, I
[L2336] [01:17:22.16] mean, in that article I mentioned, the
[L2337] [01:17:24.32] you know, the title was don't lead by
[L2338] [01:17:26.20] example. And I think that kind of might
[L2339] [01:17:29.04] be confusing for people. Can you explain
[L2340] [01:17:31.36] why you think you shouldn't lead by
[L2341] [01:17:32.92] example?
[L2342] [01:17:33.72] >> Yeah, leadership by example is a very
[L2343] [01:17:35.16] passive thing to do. And engineers are
[L2344] [01:17:37.60] passive people at the best of times, you
[L2345] [01:17:40.08] know? I think uh that's that's
[L2346] [01:17:42.04] stereotypically a little bit part of
[L2347] [01:17:43.36] their personality. Um so, I mean, the
[L2348] [01:17:45.88] the very concrete example is, you know,
[L2349] [01:17:47.68] when I first started becoming an
[L2350] [01:17:49.36] engineering leader, I was trying to lead
[L2351] [01:17:50.80] by example. So, I I wanted to kind of um
[L2352] [01:17:55.36] demonstrate the behaviors I want
[L2353] [01:17:56.92] everyone else to have. And very
[L2354] [01:17:58.60] specifically, like um
[L2355] [01:18:01.04] with regards to on-call and people
[L2356] [01:18:02.80] getting paged, I want people I want
[L2357] [01:18:04.84] people to have high ownership. I want
[L2358] [01:18:06.12] people to jump on issues as soon as it
[L2359] [01:18:07.52] happened. So, I would do it. I'd be
[L2360] [01:18:09.08] always the first one to respond to a
[L2361] [01:18:10.64] page. I would always be like, you know,
[L2362] [01:18:12.92] writing up the reports. I would always
[L2363] [01:18:14.52] be jumping on all the bugs and stuff.
[L2364] [01:18:16.76] And and like really falling over myself
[L2365] [01:18:19.44] to kind of show how I want people to do
[L2366] [01:18:22.96] to be.
[L2367] [01:18:24.72] But from their perspective, all they see
[L2368] [01:18:26.96] is that the the lead's just doing all
[L2369] [01:18:29.08] these jobs. And they don't know they're
[L2370] [01:18:31.16] like, "Oh, maybe that's James's job." Or
[L2371] [01:18:32.96] maybe James knows how to do it it, I
[L2372] [01:18:35.36] don't know how to do it. Um
[L2373] [01:18:37.68] Turns out I didn't know. I was just kind
[L2374] [01:18:38.92] of figuring out. Or you maybe he likes
[L2375] [01:18:41.24] doing those things. And I think at a
[L2376] [01:18:42.64] certain point
[L2377] [01:18:44.96] being a leader is about understanding
[L2378] [01:18:46.60] human psychology.
[L2379] [01:18:49.00] And I don't think you can just act
[L2380] [01:18:51.28] a certain way in front of people and
[L2381] [01:18:52.88] wait for them to copy you, right? I
[L2382] [01:18:54.80] think you should obviously you should
[L2383] [01:18:56.08] act with integrity and values, and you
[L2384] [01:18:57.76] should you should you know, you
[L2385] [01:18:59.16] shouldn't you should own the values of
[L2386] [01:19:00.60] the team. But you have sometimes have to
[L2387] [01:19:02.04] explain stuff. Sometimes you have to
[L2388] [01:19:03.24] tell people, "Hey,
[L2389] [01:19:04.60] and very very very specifically
[L2390] [01:19:08.68] there's a there's a there's a trajectory
[L2391] [01:19:10.36] almost every leader goes through.
[L2392] [01:19:12.96] Every high-achieving leader where they
[L2393] [01:19:14.92] become a tech lead, and they care so
[L2394] [01:19:17.76] much that they become a micromanager.
[L2395] [01:19:19.32] Like they review every line of code,
[L2396] [01:19:21.12] they're involved in every decision. And
[L2397] [01:19:22.84] at a certain point, um
[L2398] [01:19:24.96] they are the bottleneck for the team. So
[L2399] [01:19:27.04] this person is so overwhelmed, you might
[L2400] [01:19:29.08] have gone through this yourself, you
[L2401] [01:19:30.08] know? They're so overwhelmed, and
[L2402] [01:19:32.00] they're like, "Wait, my team doesn't
[L2403] [01:19:33.44] even seem busy right now, and I'm so
[L2404] [01:19:35.64] busy. I'm reviewing all this code, I'm
[L2405] [01:19:37.16] doing the strategy. What's going on?"
[L2406] [01:19:39.48] And then a manager will come along and
[L2407] [01:19:40.84] say, "Hey, like you're micromanaging.
[L2408] [01:19:42.96] You got to let your team have more
[L2409] [01:19:44.24] ownership."
[L2410] [01:19:45.88] And so
[L2411] [01:19:47.20] the tech lead says, "Okay, sure.
[L2412] [01:19:49.00] Whatever. I'll let them own stuff." And
[L2413] [01:19:51.64] they'll just take their hands off the
[L2414] [01:19:53.12] wheel, and then the team falls apart,
[L2415] [01:19:55.28] right?
[L2416] [01:19:55.97] >> [laughter]
[L2417] [01:19:56.28] >> Because you can't just stop doing the
[L2418] [01:19:58.80] things you're doing, right? You have to
[L2419] [01:20:00.56] go and have a conversation with people.
[L2420] [01:20:02.68] And so So I I see it I see leadership as
[L2421] [01:20:05.52] this kind of slider between oversight
[L2422] [01:20:08.60] and accountability.
[L2423] [01:20:10.24] So when when someone's new to the team,
[L2424] [01:20:12.80] when they're very junior, they're in a
[L2425] [01:20:14.64] mode of oversight. Like you're checking
[L2426] [01:20:16.80] their work, right? But at a certain
[L2427] [01:20:18.92] point, you have to dial down the
[L2428] [01:20:21.40] oversight, and very importantly, dial up
[L2429] [01:20:24.88] the accountability. So instead of
[L2430] [01:20:26.80] saying, "I'm not going to look at what
[L2431] [01:20:28.36] you're doing anymore," you say, "Okay,
[L2432] [01:20:30.48] cool. You've got this project. Let me
[L2433] [01:20:33.24] know when it's going to get done. Next
[L2434] [01:20:34.44] Thursday? Cool. All right. What's the
[L2435] [01:20:36.56] plan? This is going to happen? Okay, how
[L2436] [01:20:38.68] are you going to know it's correct?
[L2437] [01:20:39.84] Great, great, great. It's on you.
[L2438] [01:20:42.04] I expect you to do that. Great. Let me
[L2439] [01:20:44.00] Let me know if there's any issues,
[L2440] [01:20:45.52] right? And then the the ownership
[L2441] [01:20:47.96] relationship is explicitly on them.
[L2442] [01:20:50.48] Because what you want to do is basically
[L2443] [01:20:52.08] encourage ownership within teams.
[L2444] [01:20:55.24] You can't go from owning something to
[L2445] [01:20:56.44] just yourself to not owning something
[L2446] [01:20:58.60] yourself [laughter]
[L2447] [01:20:59.48] and expect that to develop. You have to
[L2448] [01:21:01.08] go have those conversations. You have to
[L2449] [01:21:02.40] go and give people accountability. Now,
[L2450] [01:21:05.16] what I have found, even though that can
[L2451] [01:21:07.68] feel like an awkward conversation, most
[L2452] [01:21:10.24] people genuinely like accountability.
[L2453] [01:21:13.00] Most people like to own their work. Most
[L2454] [01:21:15.52] people like to say, "Hey, this is on
[L2455] [01:21:17.04] you.
[L2456] [01:21:18.36] We're going to We're all going down with
[L2457] [01:21:19.76] the ship, right? If [laughter] this you
[L2458] [01:21:20.80] know
[L2459] [01:21:22.28] I'm not going to leave you high and dry.
[L2460] [01:21:23.60] Like, you know, I'm the tech lead. I
[L2461] [01:21:25.16] still take, you know, responsibility,
[L2462] [01:21:26.44] too.
[L2463] [01:21:27.52] You're accountable to this project.
[L2464] [01:21:29.48] And uh and go for it. And that's how you
[L2465] [01:21:32.40] can develop people in your team. You
[L2466] [01:21:34.44] know, a tech lead shouldn't be about you
[L2467] [01:21:36.56] as the boss and the team is like the
[L2468] [01:21:39.16] people who, you know, do the work or
[L2469] [01:21:41.24] something, right? It's about this kind
[L2470] [01:21:43.24] of flow where you're the more
[L2471] [01:21:45.76] experienced person typically, maybe the
[L2472] [01:21:47.16] more organized person, the more
[L2473] [01:21:48.52] strategic person, and you're working on
[L2474] [01:21:50.48] developing your team members so they can
[L2475] [01:21:52.60] take your job.
[L2476] [01:21:53.92] And then you can do something else.
[L2477] [01:21:55.96] >> That slider you mentioned, what if you
[L2478] [01:21:59.24] give someone accountability and they
[L2479] [01:22:01.08] blow it? Do they go back down the slider
[L2480] [01:22:03.60] to, you know, where you start
[L2481] [01:22:05.24] micromanaging?
[L2482] [01:22:06.16] >> to recognize it, right? So,
[L2483] [01:22:08.88] this is growth. I mean, this is growth,
[L2484] [01:22:10.52] right? It doesn't always work. And so,
[L2485] [01:22:13.52] um
[L2486] [01:22:14.32] I think I had another article about um
[L2487] [01:22:16.52] paper cuts or something. So, you know,
[L2488] [01:22:18.60] we'd call these paper cuts, you know, so
[L2489] [01:22:20.80] um some decisions don't matter that
[L2490] [01:22:23.44] much. You know, you get them wrong and
[L2491] [01:22:25.20] maybe it sets you back a week. You get
[L2492] [01:22:27.20] them wrong and maybe something's a bit
[L2493] [01:22:28.32] suboptimal. And these are great
[L2494] [01:22:30.60] candidates to give people accountability
[L2495] [01:22:32.72] for because they do it and if it doesn't
[L2496] [01:22:34.52] work,
[L2497] [01:22:35.64] they get to experience it and it will
[L2498] [01:22:37.72] feel bad. And
[L2499] [01:22:40.48] I guess that's good. It's It's good to
[L2500] [01:22:42.76] feel bad. You know, you shouldn't be
[L2501] [01:22:44.60] demoralized, but it's good to try
[L2502] [01:22:46.04] something and it doesn't work and you're
[L2503] [01:22:47.24] like, "Oh wow, that's that that didn't
[L2504] [01:22:48.92] work." And that you And then you feed
[L2505] [01:22:50.88] that back into your little, you know,
[L2506] [01:22:52.28] LLM in your brain and you get better
[L2507] [01:22:54.20] next time, right? Uh
[L2508] [01:22:55.88] that's that's a growth experience. I
[L2509] [01:22:57.20] think what you don't want to let people
[L2510] [01:22:58.80] do is like lose their arm. You know,
[L2511] [01:23:00.28] like like paper cuts are fine, but I
[L2512] [01:23:02.76] would not let someone a junior person,
[L2513] [01:23:05.44] especially, design the replication
[L2514] [01:23:07.72] system at Conflux whatever. Like, you
[L2515] [01:23:09.36] know, you have to have safeguards and
[L2516] [01:23:12.36] and one of the arts as a CTO or leader
[L2517] [01:23:15.84] tech lead is figuring out the right
[L2518] [01:23:18.00] level of altitude
[L2519] [01:23:20.44] to how to know whether you can trust
[L2520] [01:23:21.88] someone to take on ownership for
[L2521] [01:23:22.92] something.
[L2522] [01:23:23.76] >> You mentioned, because you were the most
[L2523] [01:23:25.84] senior engineer at Dropbox at some
[L2524] [01:23:27.80] point, that you had to mentor other very
[L2525] [01:23:30.60] senior engineers and
[L2526] [01:23:32.80] you know, when I think about mentoring a
[L2527] [01:23:33.92] junior engineer, it's relatively
[L2528] [01:23:35.76] straightforward patterns. But when I
[L2529] [01:23:37.48] think about, let's say I need to mentor
[L2530] [01:23:40.56] a senior staff engineer or maybe even a
[L2531] [01:23:43.56] a principal engineer, how do you mentor
[L2532] [01:23:46.00] someone like that that's already so
[L2533] [01:23:47.52] polished? They already know how to take
[L2534] [01:23:49.32] ownership. Um yeah, how do you mentor
[L2535] [01:23:52.28] someone so senior?
[L2536] [01:23:53.68] >> Yeah, I mean this in two ways. What One
[L2537] [01:23:55.56] is there is still just a whole bunch of
[L2538] [01:23:57.24] commonality. Everyone goes through the
[L2539] [01:23:59.20] same problems. They They don't know how
[L2540] [01:24:01.40] to deliver harsh feedback. They They
[L2541] [01:24:03.68] don't know, you know,
[L2542] [01:24:05.88] there is a bunch of the standard stuff
[L2543] [01:24:07.76] people working on, but I do think that
[L2544] [01:24:10.32] um
[L2545] [01:24:11.24] that a certain point everyone needs to
[L2546] [01:24:13.20] become the best version of themselves.
[L2547] [01:24:15.56] Sounds so cheesy, right? But there is
[L2548] [01:24:17.12] not an archetype for what, according to
[L2549] [01:24:19.40] me, there's not an archetype for a
[L2550] [01:24:21.12] senior principal engineer.
[L2551] [01:24:23.08] There's you've got to be your own brand
[L2552] [01:24:25.32] of engineer, right? So, you might be for
[L2553] [01:24:26.88] me I'm like the strategic kind of
[L2554] [01:24:29.00] collaboration simplicity abstraction
[L2555] [01:24:30.88] engineer, and my coding just fell off a
[L2556] [01:24:33.64] cliff, you know? Some engineers are like
[L2557] [01:24:35.56] the the deep uh science fiction, you
[L2558] [01:24:38.28] know, the super hardcore science, you
[L2559] [01:24:40.72] know, problem-solving engineer. So,
[L2560] [01:24:42.48] everyone's going to find their own
[L2561] [01:24:43.44] brand. So, often times what I'll be
[L2562] [01:24:44.80] working on them is is a combination of
[L2563] [01:24:47.92] two things. One, finding their their
[L2564] [01:24:51.32] strengths and helping them
[L2565] [01:24:53.24] be more spiky, helping them to to like
[L2566] [01:24:55.28] really um excel in the area that makes
[L2567] [01:24:58.32] them special.
[L2568] [01:25:00.08] At the same time,
[L2569] [01:25:01.76] almost always working on the personal
[L2570] [01:25:04.20] side of being engineering. Like the the
[L2571] [01:25:06.40] organizational personal understanding
[L2572] [01:25:08.36] people, understanding the why. It's just
[L2573] [01:25:10.88] I don't know. We're we're so mathy, you
[L2574] [01:25:12.92] know, as an industry. We think that
[L2575] [01:25:14.72] somehow like even silly things like like
[L2576] [01:25:17.12] for example, I have to tell so many
[L2577] [01:25:19.00] senior engineers
[L2578] [01:25:20.72] that you can't change someone's mind in
[L2579] [01:25:22.68] a meeting.
[L2580] [01:25:23.88] You just can't do it. Like you can you
[L2581] [01:25:26.36] can you can disagree with someone, and
[L2582] [01:25:29.08] they're going to be mad or whatever,
[L2583] [01:25:31.00] right? But like but to change someone's
[L2584] [01:25:33.56] mind involves going through a complex
[L2585] [01:25:35.60] series of like of
[L2586] [01:25:37.92] neurological processes, right? That like
[L2587] [01:25:40.48] that don't happen live in front of 10
[L2588] [01:25:42.76] people in a meeting, right? And so, if
[L2589] [01:25:45.36] you force someone to agree with you
[L2590] [01:25:47.48] about them being wrong, they're just
[L2591] [01:25:49.04] going to go along with it. And and the
[L2592] [01:25:51.08] ego is going to get bruised and
[L2593] [01:25:52.20] whatever. So, so one thing, you know,
[L2594] [01:25:53.92] firstly, meetings aren't generally
[L2595] [01:25:55.72] aren't for decision-making.
[L2596] [01:25:57.68] Most of the time when you identify
[L2597] [01:25:59.80] uh a disagreement, I would point out the
[L2598] [01:26:03.08] disagreement and why
[L2599] [01:26:04.96] and why I I don't agree or, you know,
[L2600] [01:26:07.28] where the problems are, provide enough
[L2601] [01:26:08.72] information, and then let it sit and let
[L2602] [01:26:10.80] them go and reflect on it and like come
[L2603] [01:26:12.88] back and have a conversation a week
[L2604] [01:26:14.16] later after they've after they've gone
[L2605] [01:26:15.88] back and forth about the why, right? And
[L2606] [01:26:17.48] so this this kind of a lot of very
[L2607] [01:26:18.60] psychological, but it's it's it makes no
[L2608] [01:26:20.68] sense to be like, well, they should be
[L2609] [01:26:22.48] able to change their mind. I mean, well,
[L2610] [01:26:23.92] they won't, right? That team should do
[L2611] [01:26:26.60] this, well, they didn't, right? You
[L2612] [01:26:28.28] know, people should like my API, well,
[L2613] [01:26:30.36] they don't, right? And [snorts] I think
[L2614] [01:26:31.96] it's like that whole like it's almost um
[L2615] [01:26:36.08] it's almost like a capital
[L2616] [01:26:38.44] a capitalist attitude towards like
[L2617] [01:26:40.36] interpersonal behaviors, right? It's
[L2618] [01:26:42.52] like doesn't like you know capitalism
[L2619] [01:26:46.08] success, you know, or or or or impact.
[L2620] [01:26:49.20] It doesn't matter how well-intentioned
[L2621] [01:26:51.28] you were if you didn't manage to
[L2622] [01:26:52.68] convince them. That you could be the
[L2623] [01:26:54.00] smartest person in the world, but if you
[L2624] [01:26:56.12] can't change someone's mind, then you
[L2625] [01:26:58.96] are kind of useless, right? And so I
[L2626] [01:27:01.16] think it is a lot of senior engineers
[L2627] [01:27:02.96] still struggle with this. It doesn't
[L2628] [01:27:04.20] matter how smart you are, doesn't matter
[L2629] [01:27:05.40] how right you are. Are you effective?
[L2630] [01:27:07.80] And a lot of being effective at that
[L2631] [01:27:09.92] level is about you know, uncertainty and
[L2632] [01:27:13.64] project management and simplicity blah
[L2633] [01:27:15.40] blah blah blah blah, but also kind of
[L2634] [01:27:17.04] interpersonal dynamics because most hard
[L2635] [01:27:19.20] problems happen with a team.
[L2636] [01:27:21.16] Not always, but generally when you're at
[L2637] [01:27:23.60] that level, you're going to have to have
[L2638] [01:27:25.56] 10 20 people working with you to get
[L2639] [01:27:27.08] something done, and that that's a whole
[L2640] [01:27:28.76] different ballgame.
[L2641] [01:27:30.64] >> On the topic of career advice, the the
[L2642] [01:27:33.24] industry's changed a lot in the last 5
[L2643] [01:27:35.32] years because of all these agentic
[L2644] [01:27:37.04] tools, and I wanted to know if you
[L2645] [01:27:40.76] thought is there any career advice that
[L2646] [01:27:43.88] majorly changed in the last 5 years?
[L2647] [01:27:46.48] Something that you used to say 5 years
[L2648] [01:27:47.92] ago, you don't say anymore or vice
[L2649] [01:27:51.04] versa.
[L2650] [01:27:52.08] >> No, I I I don't know if I've changed my
[L2651] [01:27:55.16] perspective much, but I think the
[L2652] [01:27:56.52] industry has changed its perspective
[L2653] [01:27:57.92] dramatically. I think um I mean, let's
[L2654] [01:28:00.68] just let's just be honest about it. Um
[L2655] [01:28:02.76] there is incredible demand in Silicon
[L2656] [01:28:04.48] Valley for senior engineers, and it is
[L2657] [01:28:06.56] getting harder for junior engineers to
[L2658] [01:28:09.12] succeed and grow.
[L2659] [01:28:10.52] Um for a variety of reasons. Um, why is
[L2660] [01:28:14.32] there demand for senior engineers? Well,
[L2661] [01:28:15.52] because LLMs can't do everything. Well,
[L2662] [01:28:17.68] you know, the architecture and
[L2663] [01:28:19.16] simplicity and design, they're still the
[L2664] [01:28:20.80] domain of human beings, despite what you
[L2665] [01:28:22.76] might hear on Twitter, right? And every
[L2666] [01:28:25.32] company, including the labs, are
[L2667] [01:28:26.80] desperately hiring senior engineers,
[L2668] [01:28:28.64] right? But, junior tasks are getting a
[L2669] [01:28:31.84] little bit commoditized, and that
[L2670] [01:28:32.88] worries me.
[L2671] [01:28:34.32] Because I do think that, um,
[L2672] [01:28:38.32] that learning, it's very you know,
[L2673] [01:28:40.32] wisdom is kind of facts
[L2674] [01:28:42.88] put into practice and then synthesized,
[L2675] [01:28:45.08] you know? And so,
[L2676] [01:28:46.88] a lot of people would argue that, oh,
[L2677] [01:28:48.36] well, you know, it's easy to learn now
[L2678] [01:28:50.56] because of ChatGPT, because you can just
[L2679] [01:28:52.12] go ask it a question about
[L2680] [01:28:55.20] how does two-phase commit work, or
[L2681] [01:28:57.40] what's the difference between snapshot
[L2682] [01:28:59.04] isolation and serializability, and it
[L2683] [01:29:01.16] will give you probably a pretty good
[L2684] [01:29:02.20] answer.
[L2685] [01:29:03.76] But, I think growth as an engineer
[L2686] [01:29:07.40] does require wisdom.
[L2687] [01:29:09.36] And wisdom only really happens when you
[L2688] [01:29:11.24] synthesize it, in my my opinion. And so,
[L2689] [01:29:14.52] I think, um,
[L2690] [01:29:17.16] I'm still very bullish on young people.
[L2691] [01:29:20.64] We're hiring junior engineers at Convex.
[L2692] [01:29:22.64] I'm very excited about, I mean, I love
[L2693] [01:29:25.40] working with junior engineers who are
[L2694] [01:29:26.44] really hungry to grow.
[L2695] [01:29:28.72] But, what I would say is train your
[L2696] [01:29:31.40] mind. Like,
[L2697] [01:29:32.88] do not listen to anyone who tells you
[L2698] [01:29:35.92] that there is an advantage to having
[L2699] [01:29:37.52] less knowledge. Yeah, I'm I'm not sure
[L2700] [01:29:39.24] if you've seen people will say these
[L2701] [01:29:41.00] ludicrous things that like, oh, maybe in
[L2702] [01:29:43.04] the future, like, not knowing
[L2703] [01:29:45.00] engineering will be an advantage cuz you
[L2704] [01:29:46.44] won't have biases and you'll just use
[L2705] [01:29:47.92] Claude. I think these are like ludicrous
[L2706] [01:29:50.20] statements. Like, like,
[L2707] [01:29:52.08] software engineering is an intellectual
[L2708] [01:29:53.96] discipline that helps you think. Like,
[L2709] [01:29:56.48] like, the software engineering, the best
[L2710] [01:29:58.88] software engineering is not about
[L2711] [01:30:00.44] knowing syntax, and it's not about
[L2712] [01:30:02.32] knowing an algorithm. It's being really
[L2713] [01:30:04.68] good at conceptualizing problems and
[L2714] [01:30:07.04] being able to break them down to
[L2715] [01:30:08.16] building blocks and coming up with clean
[L2716] [01:30:10.00] solutions to them.
[L2717] [01:30:11.72] And that requires experience. It
[L2718] [01:30:12.96] requires
[L2719] [01:30:14.44] like it's like doing doing weights with
[L2720] [01:30:16.16] your mind. And just like if you went to
[L2721] [01:30:18.96] the gym and you just like
[L2722] [01:30:21.64] it never hurt. Like if you went to the
[L2723] [01:30:23.36] gym and just picked up really light
[L2724] [01:30:24.76] weights,
[L2725] [01:30:25.88] um you're not growing. And also if you
[L2726] [01:30:28.24] went to the gym and picked up a heavy
[L2727] [01:30:30.36] weight and like, "Okay, cool. I think I
[L2728] [01:30:31.80] can do it." And then you let the robot
[L2729] [01:30:33.80] pick up the weight for you there, you're
[L2730] [01:30:35.48] also not really growing, right? You have
[L2731] [01:30:37.40] to do the reps. And so I would say, and
[L2732] [01:30:39.28] it's tough,
[L2733] [01:30:40.80] but find a way to
[L2734] [01:30:43.76] stress your brain
[L2735] [01:30:45.24] every day.
[L2736] [01:30:46.40] Find a way to to avoid
[L2737] [01:30:49.56] Now, obviously a genetic coding is here,
[L2738] [01:30:52.08] right? Obviously that's, you know, I
[L2739] [01:30:54.20] could never tell someone to like never
[L2740] [01:30:56.00] use the coding agent cuz that'd be
[L2741] [01:30:57.68] silly, you know? But I can say that it
[L2742] [01:31:00.76] is easy
[L2743] [01:31:02.60] to fall into a passivity trap. Like when
[L2744] [01:31:04.96] you're just being passive about your
[L2745] [01:31:06.36] learning. And I do think you need to
[L2746] [01:31:09.00] spend some time in the
[L2747] [01:31:11.20] intellectual wilderness of not being
[L2748] [01:31:13.80] able to solve a problem and struggling.
[L2749] [01:31:16.00] If you I I I would say if you're running
[L2750] [01:31:17.64] into a a new
[L2751] [01:31:19.32] um
[L2752] [01:31:20.24] a new problem, try to think of a
[L2753] [01:31:22.44] solution yourself and then go check with
[L2754] [01:31:25.16] an LLM.
[L2755] [01:31:27.00] It's going to
[L2756] [01:31:28.24] be hard for you. It's almost like
[L2757] [01:31:31.76] for example,
[L2758] [01:31:33.04] I'm not very good at reading anymore. I
[L2759] [01:31:34.68] got to be honest. Like I would find it
[L2760] [01:31:36.52] hard I mean I can read obviously, but I
[L2761] [01:31:38.28] find it hard to sit down and read a book
[L2762] [01:31:40.76] because my brain has been fried by
[L2763] [01:31:44.28] the stimulation economy, right? Like
[L2764] [01:31:46.00] Like I I I find it I go home and I'm
[L2765] [01:31:48.40] tired and I watch a YouTube video. I
[L2766] [01:31:49.92] don't tend to go home and read a novel.
[L2767] [01:31:51.64] I should be better at that.
[L2768] [01:31:53.88] But it takes discipline to do that. I
[L2769] [01:31:55.56] would say similarly
[L2770] [01:31:57.52] it's getting harder to solve a difficult
[L2771] [01:32:00.20] problem without reaching for the help.
[L2772] [01:32:03.24] It's getting harder and harder every day
[L2773] [01:32:04.72] to be faced with a very difficult
[L2774] [01:32:06.32] intellectual problem and not being like,
[L2775] [01:32:07.84] "Well, I'll just I'll just do a Google
[L2776] [01:32:09.24] search or I'll just ask Claude." You
[L2777] [01:32:11.16] know, whatever. I'm still doing the
[L2778] [01:32:12.80] work.
[L2779] [01:32:13.76] I don't know. I I would really encourage
[L2780] [01:32:16.28] people to practice
[L2781] [01:32:18.36] using your brain every day.
[L2782] [01:32:20.20] >> If I was just devil's advocate or just
[L2783] [01:32:22.04] thinking from the junior engineer
[L2784] [01:32:23.76] perspective, I might think, "Well, the
[L2785] [01:32:26.52] proof that Claude can do this work today
[L2786] [01:32:28.96] means that I don't need to know it today
[L2787] [01:32:31.52] or tomorrow or in the future. So, why
[L2788] [01:32:34.80] why even build that skill in the first
[L2789] [01:32:36.52] place? Like and also these agentic
[L2790] [01:32:39.72] tools, they have positive trajectories,
[L2791] [01:32:42.68] too. So,
[L2792] [01:32:44.04] >> Yes. So, firstly, um
[L2793] [01:32:47.44] the agents are not particularly good at
[L2794] [01:32:48.92] a lot of parts of engineering currently.
[L2795] [01:32:51.60] Um and so, probably everyone should
[L2796] [01:32:53.04] agree there's, you know,
[L2797] [01:32:55.48] Claude is not good at designing
[L2798] [01:32:56.92] distributed systems protocols right now,
[L2799] [01:32:58.68] for example. You know, or or managing a
[L2800] [01:33:01.08] a 3 million line code base, you know. Um
[L2801] [01:33:03.60] and so, there are parts of engineering
[L2802] [01:33:05.72] where engineers are valuable. And like I
[L2803] [01:33:07.48] said, you know this because the labs are
[L2804] [01:33:09.28] all hiring engineers. No matter what
[L2805] [01:33:10.68] they say, they're still hiring
[L2806] [01:33:12.20] engineers, right? Desperately hiring
[L2807] [01:33:13.64] engineers. Um really really aggressively
[L2808] [01:33:16.08] hiring engineers.
[L2809] [01:33:17.32] Um
[L2810] [01:33:18.64] So, engineers still have value.
[L2811] [01:33:20.76] And maybe they won't in the future, but
[L2812] [01:33:23.24] I doubt it. I really do think there's a
[L2813] [01:33:25.04] role for human ingenuity in engineering.
[L2814] [01:33:27.52] And so, here's the here's the trade-off
[L2815] [01:33:31.16] I would pose to people. I mean, this
[L2816] [01:33:33.12] there's kind of three paths. One, get
[L2817] [01:33:35.16] out. Get out of engineering, go mow
[L2818] [01:33:37.80] lawns, and do whatever if you want.
[L2819] [01:33:40.92] That's the that's the most nihilistic
[L2820] [01:33:43.12] attitude. I I don't believe in that. I
[L2821] [01:33:45.28] believe I really love engineering and I
[L2822] [01:33:46.96] believe that there's promising roles for
[L2823] [01:33:48.52] human beings in engineering.
[L2824] [01:33:50.20] So, the second is
[L2825] [01:33:52.00] to realize that um
[L2826] [01:33:54.40] there's value right now for humans in
[L2827] [01:33:55.72] engineering. And maybe one day AGI will
[L2828] [01:33:58.32] be here.
[L2829] [01:33:59.92] Let's say in the year's time AGI will be
[L2830] [01:34:01.76] here.
[L2831] [01:34:02.56] And there's two people.
[L2832] [01:34:04.16] One person just gave up on
[L2833] [01:34:05.80] problem-solving right now, and they're
[L2834] [01:34:07.12] just like
[L2835] [01:34:08.52] feeding the machine, and they're running
[L2836] [01:34:09.72] 17 coding agents in parallel, and
[L2837] [01:34:11.52] they're just accepting everything Claude
[L2838] [01:34:13.76] says, and they've given up.
[L2839] [01:34:16.04] Right? And one person said, "You know
[L2840] [01:34:17.92] what? I still want to have an active
[L2841] [01:34:19.40] role in my learning. I want to
[L2842] [01:34:20.64] understand what it's doing. I want to
[L2843] [01:34:22.00] think hard about problem-solving."
[L2844] [01:34:23.32] Right?
[L2845] [01:34:24.40] Play it out 1 year, AGI arrives. Who is
[L2846] [01:34:27.44] going to be better placed for the
[L2847] [01:34:28.40] future?
[L2848] [01:34:29.64] Right?
[L2849] [01:34:30.56] The person who's been training their
[L2850] [01:34:31.72] mind, right? Like there was there's
[L2851] [01:34:34.96] you don't Engineering's not a means to
[L2852] [01:34:36.68] an end. It's a mechanism for a for
[L2853] [01:34:39.00] improving your mental processes. It's
[L2854] [01:34:41.48] It's like like I still do whiteboarding
[L2855] [01:34:43.88] coding interviews. And by the way,
[L2856] [01:34:45.36] Anthropic still does whiteboarding
[L2857] [01:34:46.72] coding interviews. Just in case you were
[L2858] [01:34:48.40] wondering. They don't say like just use
[L2859] [01:34:50.24] Claude, right? So, I still do white
[L2860] [01:34:52.52] whiteboarding coding interviews with
[L2861] [01:34:53.88] candidates.
[L2862] [01:34:55.56] Candidates are getting worse at coding.
[L2863] [01:34:57.00] That's absolutely true.
[L2864] [01:34:58.92] But I don't know any better vehicle for
[L2865] [01:35:01.80] evaluating someone's intellectual
[L2866] [01:35:04.32] capacity for problem-solving than seeing
[L2867] [01:35:06.52] them solve an engineering problem.
[L2868] [01:35:07.80] Right? It's a It's a great mechanism for
[L2869] [01:35:10.08] doing so. It's like you know,
[L2870] [01:35:12.16] um
[L2871] [01:35:13.28] if you were doing a math degree,
[L2872] [01:35:16.04] right?
[L2873] [01:35:17.20] A big part of doing advanced mathematics
[L2874] [01:35:18.80] is proving theorems.
[L2875] [01:35:20.52] And by the way, the theorems are already
[L2876] [01:35:21.92] all proven, right? When
[L2877] [01:35:24.76] by the you know, the exams and is
[L2878] [01:35:27.16] proving a theorem that has already been
[L2879] [01:35:29.48] proven. And so, you might say, "Well,
[L2880] [01:35:30.80] what's the point of proving that
[L2881] [01:35:31.72] theorem? It's already been done." Well,
[L2882] [01:35:33.24] the point is that the act of proving
[L2883] [01:35:35.60] that theorem
[L2884] [01:35:36.88] improves your mind, right? And then you
[L2885] [01:35:38.76] can go and do more innovative stuff. So,
[L2886] [01:35:40.40] I would say sh
[L2887] [01:35:41.76] Sure, you may not I still do think that
[L2888] [01:35:45.64] there is a very, very promising role for
[L2889] [01:35:47.16] human beings in engineering. Maybe not
[L2890] [01:35:48.96] in coding, but coding and engineering
[L2891] [01:35:51.16] are very different things, right? Um,
[L2892] [01:35:53.68] but even if you don't believe me, you
[L2893] [01:35:55.16] can either give up now, but or you can
[L2894] [01:35:56.92] just keep trying to improve your brain
[L2895] [01:35:58.68] and you'll be better off anyway. Imagine
[L2896] [01:36:00.48] if you're wrong. Imagine if you take the
[L2897] [01:36:01.68] defeatist view. Imagine if you say,
[L2898] [01:36:03.56] "Well, AGI is coming next week. Why
[L2899] [01:36:05.52] bother doing anything?" And imagine
[L2900] [01:36:07.20] you're wrong.
[L2901] [01:36:08.64] Oh my god, you just got off the
[L2902] [01:36:11.24] You just got off the
[L2903] [01:36:13.24] >> [laughter]
[L2904] [01:36:14.00] >> off the ride. You got off the ride.
[L2905] [01:36:16.08] There's so much cool stuff. I mean, this
[L2906] [01:36:17.60] is a cool time for engineering, right?
[L2907] [01:36:19.24] This is a really cool time. There's so
[L2908] [01:36:20.48] much cool stuff happening. And I don't
[L2909] [01:36:22.64] And I I I hate this talk about like
[L2910] [01:36:25.76] AI means humans don't have a role
[L2911] [01:36:28.52] anymore. AI means no one's going to have
[L2912] [01:36:30.56] a job. AI means we're going to do
[L2913] [01:36:32.56] nothing else new and there's no one's
[L2914] [01:36:34.56] going to I What I like is, "Hey, look at
[L2915] [01:36:37.16] this all this new cool stuff we can
[L2916] [01:36:38.44] build."
[L2917] [01:36:39.56] Like, look at how there's ways we can
[L2918] [01:36:41.20] make people's lives better. And to be
[L2919] [01:36:42.96] honest, I really wish my peers and and
[L2920] [01:36:45.84] and my cohort would stop it with the
[L2921] [01:36:49.68] the real doomer like um human
[L2922] [01:36:53.28] elimination kind of narrative and
[L2923] [01:36:56.08] because I think there is a little bit of
[L2924] [01:36:57.44] a like a
[L2925] [01:36:59.44] you know, a psychological anchoring, you
[L2926] [01:37:01.36] know?
[L2927] [01:37:02.12] I and as part of Convex want to make the
[L2928] [01:37:05.72] you know, we didn't start Convex to
[L2929] [01:37:06.92] eliminate jobs. We started Convex
[L2930] [01:37:08.72] because we want to make it easier for
[L2931] [01:37:09.56] people to build cool stuff. And And I
[L2932] [01:37:11.20] think the more we as an industry get
[L2933] [01:37:13.44] behind, let's do everything we can to
[L2934] [01:37:16.08] make it possible for people to do more
[L2935] [01:37:17.76] cool things.
[L2936] [01:37:19.16] I think it's a really exciting future we
[L2937] [01:37:20.44] have ahead of us.
[L2938] [01:37:21.64] >> I wanted to talk about what you're
[L2939] [01:37:22.76] working on now or Convex and why did you
[L2940] [01:37:25.16] quit Dropbox to build Convex?
[L2941] [01:37:27.68] >> I Dropbox is a great place. At a certain
[L2942] [01:37:29.16] point I I was there eight years. Uh
[L2943] [01:37:32.64] whether I I don't know if I say I
[L2944] [01:37:34.08] outgrew the company, but I'd been the
[L2945] [01:37:35.88] most senior engineer for a while there.
[L2946] [01:37:38.44] Um
[L2947] [01:37:39.24] you know, at a certain point I
[L2948] [01:37:41.24] I wanted to grow and do my own stuff,
[L2949] [01:37:43.36] you know? And so So I left the company
[L2950] [01:37:45.36] in very amicably. Um, and um,
[L2951] [01:37:49.40] started Convex. Now, why Convex? Convex
[L2952] [01:37:51.92] started pre-agentic era.
[L2953] [01:37:55.08] Cuz my observation was that that um,
[L2954] [01:37:59.08] the real differentiator in the success
[L2955] [01:38:01.32] of a project, especially a large
[L2956] [01:38:02.80] project, is the quality of the
[L2957] [01:38:04.64] abstractions, the quality of the design,
[L2958] [01:38:06.32] the quality of the architecture, right?
[L2959] [01:38:08.20] Systems that thrive over time and are
[L2960] [01:38:10.00] extensible are systems that are
[L2961] [01:38:11.76] architected well.
[L2962] [01:38:13.68] And in my mind, the most difficult
[L2963] [01:38:15.80] challenge in engineering, according to
[L2964] [01:38:17.92] me, is distributed state management. How
[L2965] [01:38:20.80] do we store state reliably and reason
[L2966] [01:38:22.64] about it, you know, modifying it
[L2967] [01:38:24.64] concurrently with other users? And so,
[L2968] [01:38:26.96] so we designed um, a platform for
[L2969] [01:38:30.00] application building based on our
[L2970] [01:38:32.44] experiences building large-scale
[L2971] [01:38:33.80] systems. So, Convex is a is a
[L2972] [01:38:36.20] transactional database where the
[L2973] [01:38:37.72] transactions are written in TypeScript.
[L2974] [01:38:39.28] They run as stored procedures,
[L2975] [01:38:40.40] TypeScript stored procedures, they're
[L2976] [01:38:42.04] serializable. There's, you know,
[L2977] [01:38:43.84] automatic reactivity. So, what the
[L2978] [01:38:45.84] client sees is a consistent view of
[L2979] [01:38:47.80] what's on the on the server.
[L2980] [01:38:50.24] And I would say Convex is a very
[L2981] [01:38:51.92] designed platform cuz Convex is designed
[L2982] [01:38:54.28] to be very composable and fit together
[L2983] [01:38:55.80] well.
[L2984] [01:38:56.64] And so, we designed Convex for
[L2985] [01:38:58.32] developers to use. In particular, we
[L2986] [01:39:00.04] wanted to make it so that application
[L2987] [01:39:02.16] developers were able to build complex
[L2988] [01:39:04.16] full-stack applications. That was the
[L2989] [01:39:06.04] goal of Convex. Now, all of a sudden,
[L2990] [01:39:08.56] agentic development came along.
[L2991] [01:39:10.44] And that's been really interesting for
[L2992] [01:39:12.20] us because it turns out
[L2993] [01:39:14.40] that um,
[L2994] [01:39:15.72] what humans find hard is also what
[L2995] [01:39:18.08] agents find hard. You know,
[L2996] [01:39:20.28] you know, the coding agents are not
[L2997] [01:39:21.84] particularly good with large
[L2998] [01:39:24.16] code bases, they're not particularly
[L2999] [01:39:25.52] good with um, reasoning about um, action
[L3000] [01:39:28.56] at a distance, you know, race conditions
[L3001] [01:39:30.84] across services, they're not
[L3002] [01:39:32.48] particularly good at simple
[L3003] [01:39:34.56] architectures over time. And these are
[L3004] [01:39:36.36] the things that Convex gives you as a
[L3005] [01:39:38.00] developer. So, the idea now, and and
[L3006] [01:39:39.92] almost everyone using Convex is using
[L3007] [01:39:41.64] Convex because they have their coding
[L3008] [01:39:43.40] agent doing their front end, but they
[L3009] [01:39:45.44] need
[L3010] [01:39:46.60] a back end abstraction, a higher level
[L3011] [01:39:48.88] abstraction than something like AWS or
[L3012] [01:39:50.80] something like hosted Postgres, which
[L3013] [01:39:52.68] makes their problems go away. And that's
[L3014] [01:39:54.32] that's the company.
[L3015] [01:39:55.64] >> That was one thing I wanted to ask cuz
[L3016] [01:39:57.36] immediately when I think, oh, I just
[L3017] [01:39:58.48] need a back end or something like that,
[L3018] [01:39:59.88] just go to AWS or, you know, just host
[L3019] [100:02.52] something like that. So, this is the
[L3020] [100:04.72] layer of abstraction on kind of on top
[L3021] [100:06.88] of those types of primitives
[L3022] [100:08.36] >> Yes.
[L3023] [100:08.76] >> that makes it easier for an application
[L3024] [100:10.68] developer.
[L3025] [100:11.28] >> It ties into a lot of the stuff I I said
[L3026] [100:13.68] earlier about making problems go away.
[L3027] [100:15.56] And frankly, I mean, I I watched the
[L3028] [100:17.44] interview you did with Barbara Liskov,
[L3029] [100:18.88] and Barbara was my advisor in grad
[L3030] [100:20.60] school, and and I we worked a lot
[L3031] [100:22.64] together and a lot on abstraction, and
[L3032] [100:25.28] you know, the value in clean designs
[L3033] [100:27.52] that minimize complexity. And so, AWS is
[L3034] [100:30.40] a fine tool.
[L3035] [100:32.16] Postgres is a fine tool.
[L3036] [100:34.36] Although, none of the mainstream
[L3037] [100:35.20] databases are that great, frankly. But
[L3038] [100:37.32] um
[L3039] [100:37.92] they're fine tools, but they're not
[L3040] [100:39.56] they're not making problems go away,
[L3041] [100:41.32] right? And so, the idea of Convex is a
[L3042] [100:43.28] higher level set of abstractions that
[L3043] [100:45.48] you can use and not reason about state
[L3044] [100:47.76] management, not reason about
[L3045] [100:49.44] concurrency, not reason about
[L3046] [100:50.56] scheduling, not reason about
[L3047] [100:52.24] transactions, uh not reason about
[L3048] [100:54.40] polling and data sync and type safety
[L3049] [100:56.92] and all those things. So, Convex is a If
[L3050] [100:59.64] If you think about, you know, the
[L3051] [101:00.72] history of of engineering, over time the
[L3052] [101:03.24] abstraction floor raises. You know, when
[L3053] [101:05.24] Barbara was first starting,
[L3054] [101:07.64] she was using punch cards, you know? Um
[L3055] [101:10.40] I don't I don't know if she mentioned it
[L3056] [101:11.44] to you, but
[L3057] [101:12.40] uh when she started as a programmer, she
[L3058] [101:14.32] never heard the word programmer before,
[L3059] [101:16.16] you know?
[L3060] [101:16.92] Uh that was the first time she heard the
[L3061] [101:18.56] word, right? And then you you went from
[L3062] [101:20.76] punch cards to like, you know, having
[L3063] [101:23.04] proper operating systems and and and uh
[L3064] [101:26.04] you know, then you know,
[L3065] [101:27.64] languages like C and then higher level
[L3066] [101:29.00] languages and and then you had cloud
[L3067] [101:30.88] computing. And over time the abstraction
[L3068] [101:32.96] floor raises, and you largely forget
[L3069] [101:35.20] about what's going on beneath the
[L3070] [101:36.40] surfaces. Most people don't think about
[L3071] [101:38.36] how S3 is implemented. I do, but that's
[L3072] [101:40.68] what I used to work on. But like most
[L3073] [101:42.44] people just use it and it just stores
[L3074] [101:44.00] your data and it gives it back and
[L3075] [101:45.00] that's great.
[L3076] [101:46.56] That's a successful abstraction. But I
[L3077] [101:48.40] do strongly believe that the world
[L3078] [101:50.60] is and has been overdue for a new
[L3079] [101:52.56] abstraction. A one level up the stack.
[L3080] [101:55.48] And especially now that people are doing
[L3081] [101:57.12] agent development, largely they don't
[L3082] [101:59.16] want to own a Postgres instance. Largely
[L3083] [102:00.88] they don't want to think about Kafka
[L3084] [102:02.44] versus RabbitMQ. Uh they don't want to
[L3085] [102:04.48] think about, you know, what set of tools
[L3086] [102:05.96] to use. They want it just to work so
[L3087] [102:08.84] they can focus on building their
[L3088] [102:09.80] application.
[L3089] [102:11.28] >> When you talk about, you know, the
[L3090] [102:13.00] abstraction, there's obviously a lot of
[L3091] [102:14.68] stuff going on behind the scenes in
[L3092] [102:17.00] Convex and the the technical side. And
[L3093] [102:20.68] I, you know, what what is it that Convex
[L3094] [102:23.24] is building behind the scenes that
[L3095] [102:25.44] you're most excited about and why?
[L3096] [102:27.60] >> Basically, Convex is a new
[L3097] [102:30.80] operating system in some respects,
[L3098] [102:33.20] right? So we have the primitives,
[L3099] [102:34.64] queries, mutations, actions,
[L3100] [102:36.68] subscriptions.
[L3101] [102:38.32] What I think is kind of cool is how we
[L3102] [102:39.80] built this, you know? We have our own
[L3103] [102:41.40] database that we built. We have our own
[L3104] [102:42.88] distributed database that, you know,
[L3105] [102:44.72] does, you know, tracks read ranges and
[L3106] [102:46.76] write ranges and does very efficient um
[L3107] [102:49.88] subscriptions over web sockets, etc. So
[L3108] [102:52.28] that's that's the current operating
[L3109] [102:54.68] system set of primitives.
[L3110] [102:56.96] But um
[L3111] [102:58.52] Convex is getting much larger workloads
[L3112] [103:00.84] now and much more interesting workloads
[L3113] [103:02.32] and more high-performance workloads. And
[L3114] [103:04.52] so we're in the process of developing a
[L3115] [103:07.00] slightly lower-level API
[L3116] [103:09.68] for doing very efficient kind of
[L3117] [103:11.52] background processes, singletons,
[L3118] [103:13.92] APIs like fork, like you, you know, in
[L3119] [103:16.28] like operating system primitives. And
[L3120] [103:18.08] I'm pretty excited about launching these
[L3121] [103:21.72] and how much is faster it's going to
[L3122] [103:23.52] make various um Convex components like
[L3123] [103:25.72] the workflow system. Um
[L3124] [103:28.72] And to be honest, the thing I find
[L3125] [103:30.20] exciting every day,
[L3126] [103:31.96] challenging every day. I I still find
[L3127] [103:33.76] Convex very hard. Like
[L3128] [103:36.16] to be honest, like
[L3129] [103:37.72] I struggle every day.
[L3130] [103:39.76] Um I don't find my job easy. I I mean I
[L3131] [103:42.24] I
[L3132] [103:42.88] I feel confident in my job, but it's not
[L3133] [103:44.92] easy. Like designing the new API for
[L3134] [103:47.08] this is super hard. I can't just go ask
[L3135] [103:49.12] ChatGPT. It's not going to give a good
[L3136] [103:50.44] answer, right? And um cuz it's
[L3137] [103:53.52] innovation. It's a It's a new ideas. I
[L3138] [103:55.72] really enjoy it. I find it um stressful
[L3139] [103:58.44] sometimes. I find it um
[L3140] [104:01.24] challenging and tiring, but I also find
[L3141] [104:04.40] it exciting. And and and I would I you
[L3142] [104:06.36] know, I would encourage engineers to try
[L3143] [104:07.76] to find this kind of stuff to work on
[L3144] [104:09.52] where it's like you're on that edge of
[L3145] [104:11.56] like I'm really liking this, but also
[L3146] [104:14.00] it's a bit tricky, you know, it's it's a
[L3147] [104:15.40] bit tough.
[L3148] [104:16.60] >> You mentioned fork and in operating
[L3149] [104:18.72] systems I'm familiar, you know, you just
[L3150] [104:21.16] take the existing process and kind of
[L3151] [104:22.96] split it. What's the idea of fork in a
[L3152] [104:26.28] distributed system?
[L3153] [104:27.96] >> So, Convex almost never has scale issues
[L3154] [104:30.80] with regards to live traffic. You know,
[L3155] [104:32.44] live traffic is like um
[L3156] [104:34.72] typically bound by user-facing
[L3157] [104:36.36] interactions, people clicking on stuff,
[L3158] [104:37.84] running website, you know, acting on
[L3159] [104:39.16] website. Every now and then someone will
[L3160] [104:41.48] come to Convex and want to kick off a
[L3161] [104:42.96] million background jobs to do something,
[L3162] [104:44.88] background processing.
[L3163] [104:46.44] It's a big workload. You
[L3164] [104:47.32] programmatically you can trigger huge
[L3165] [104:49.36] workloads, right? And so the one of
[L3166] [104:51.08] things we have to scale is is kind of
[L3167] [104:52.72] these background workloads and a lot of
[L3168] [104:54.68] them involve things like scheduling.
[L3169] [104:57.24] And there are a lot of workloads in
[L3170] [104:58.44] Convex that would be um
[L3171] [105:01.08] very efficient if you had a background
[L3172] [105:03.32] singleton process to perform things like
[L3173] [105:06.16] aggregates, you know, um
[L3174] [105:09.08] I'll give a very silly example, right?
[L3175] [105:11.44] If you have a let's say you're building
[L3176] [105:13.80] an election on Convex, a voting system,
[L3177] [105:16.40] and every vote is a new uh row in the in
[L3178] [105:19.16] the table and you want to show a tally
[L3179] [105:20.88] of the votes.
[L3180] [105:22.12] You know, one way of doing this is
[L3181] [105:23.56] having a bunch of background processes
[L3182] [105:24.84] or crons adding these things up.
[L3183] [105:26.92] One way is doing a table scan, which is
[L3184] [105:29.16] you know, the obvious way to use
[L3185] [105:30.20] Postgres, which doesn't scale. The other
[L3186] [105:32.40] is to have a background job, which if
[L3187] [105:34.76] there's new votes, it adds them all up,
[L3188] [105:37.20] keeps a tally. If there's no new votes,
[L3189] [105:38.96] it goes to sleep and waits on like a
[L3190] [105:41.16] condition variable to wake up up to wake
[L3191] [105:43.40] up again when there's with a new job to
[L3192] [105:44.72] perform. And so these are the kind of
[L3193] [105:46.40] primitives
[L3194] [105:47.64] that we're working on right now. Most
[L3195] [105:49.16] people won't even know they exist, but
[L3196] [105:50.96] allow us to build these very
[L3197] [105:52.08] high-performance um primitives for
[L3198] [105:54.44] scheduling
[L3199] [105:56.16] um aggregates, you know, background
[L3200] [105:59.04] aggregations, etc. Um and I'm pretty
[L3201] [106:01.48] excited about like the the next
[L3202] [106:03.68] generation of workloads we can support
[L3203] [106:05.12] as a result.
[L3204] [106:06.44] >> When you reflect on your career and you
[L3205] [106:09.08] it sounds like you've done a lot of
[L3206] [106:10.36] gnarly technical work across your PhD,
[L3207] [106:13.80] ca- Dropbox seemed like pretty intense
[L3208] [106:16.04] systems work, and Convex is also doing a
[L3209] [106:19.00] lot of cool stuff. When you look back on
[L3210] [106:20.84] your career, what was the most
[L3211] [106:22.40] technically stimulating work you've ever
[L3212] [106:24.56] done? And you know, why was it hard and
[L3213] [106:27.52] what did you learn from it?
[L3214] [106:29.36] >> There was certainly times in grad school
[L3215] [106:30.76] where we were like um formally mo-
[L3216] [106:32.92] modeling consensus protocols and stuff
[L3217] [106:34.92] and you know, I'd be on the phone with
[L3218] [106:36.44] Barbara on weekends and talking through
[L3219] [106:38.92] um trying to reason about this in our
[L3220] [106:40.64] heads. That was pretty intellectually
[L3221] [106:41.84] stimulating and fun, but I think the
[L3222] [106:43.68] stuff I found most stimulating was stuff
[L3223] [106:46.32] like working on very large storage
[L3224] [106:49.60] system with a team where
[L3225] [106:52.16] you know, things are going wrong. You
[L3226] [106:53.84] know, where where the rubber hits the
[L3227] [106:55.36] road, that's where I find And this is
[L3228] [106:57.44] everyday at Convex. You know, the rubber
[L3229] [106:59.32] hits the road like you know, uh hey, we
[L3230] [107:00.52] have a uh compaction process that runs
[L3231] [107:02.48] in the background, but it's running into
[L3232] [107:04.08] issues. We might have to redesign it
[L3233] [107:05.56] using
[L3234] [107:06.56] partitioning, etc.
[L3235] [107:09.44] I I feel most intellectually stimulated
[L3236] [107:11.72] where where there's a really clear
[L3237] [107:14.44] constraint in front of me.
[L3238] [107:16.56] And um that to me is engineering. Like
[L3239] [107:19.12] if
[L3240] [107:20.36] I I actually know what the definition of
[L3241] [107:21.52] engineering is, but I'm just going to
[L3242] [107:23.40] make it up in my mind, engineering is
[L3243] [107:26.20] science with constraints. It's like It's
[L3244] [107:28.36] like how to How do you
[L3245] [107:31.52] solve problems in the presence of
[L3246] [107:33.36] resource constraints?
[L3247] [107:35.04] I'm not particularly interested in
[L3248] [107:36.44] constraint-free environments. That's
[L3249] [107:38.36] art.
[L3250] [107:39.32] I like craft and engineering. And the
[L3251] [107:43.08] the more visceral and difficult the
[L3252] [107:45.00] constraints, the more fun that is for
[L3253] [107:46.56] me.
[L3254] [107:47.96] And I I've I've been lucky enough to
[L3255] [107:50.96] I don't know whether it's luck or
[L3256] [107:53.24] intention, I don't know, but I I I've
[L3257] [107:55.08] always placed myself in those
[L3258] [107:57.28] environments, you know, like
[L3259] [108:00.80] let's go get on the hardest team and and
[L3260] [108:03.24] own the hardest problem and then
[L3261] [108:05.20] um and then, you know, put the effort
[L3262] [108:07.00] into to to survive.
[L3263] [108:10.20] >> This question might be a little bit off
[L3264] [108:11.80] topic, but you know, I know you were a
[L3265] [108:14.40] consultant for the show the TV show
[L3266] [108:16.80] Silicon Valley.
[L3267] [108:18.28] I love that show and I got to hear how'd
[L3268] [108:20.56] you get involved in that?
[L3269] [108:21.88] >> Yeah, that was a lot of fun. So, um
[L3270] [108:25.20] a lot of folks might not know this. Um
[L3271] [108:28.24] I had nothing to do with season 1. So, a
[L3272] [108:29.92] lot of TV shows, they don't know whether
[L3273] [108:31.40] they're going to survive as a TV show.
[L3274] [108:33.56] So, so, um Mike Judge who started um who
[L3275] [108:37.40] who who wrote Silicon Valley also was of
[L3276] [108:39.64] Beavis and Butt-Head and Office Space
[L3277] [108:41.24] fame. He started his career as a
[L3278] [108:43.12] software engineer at I think Lockheed or
[L3279] [108:45.04] something. So, he actually was a
[L3280] [108:46.48] software engineer that a lot of people
[L3281] [108:48.12] don't realize. And so, Silicon Valley
[L3282] [108:50.20] was like a throwback to the kind of
[L3283] [108:52.56] work he did. And if you anyone's seen
[L3284] [108:53.76] the movie Office Space, you would you
[L3285] [108:55.20] would get this. It's That's a really a
[L3286] [108:57.04] you know, dystopian cubicle era uh tech
[L3287] [108:59.88] uh industry um film.
[L3288] [109:01.48] Um so, they did season 1 of of Silicon
[L3289] [109:04.44] Valley and then it was very popular and
[L3290] [109:06.92] they got picked up and so, they had to
[L3291] [109:08.32] figure out what to do for season 2, but
[L3292] [109:09.80] they didn't know what to do because they
[L3293] [109:11.76] did they'd written a storyline that gets
[L3294] [109:13.84] to the point where there's a compression
[L3295] [109:15.16] algorithm. And And then what happens?
[L3296] [109:18.16] And so they needed to find um
[L3297] [109:21.68] an expert on compression and I guess
[L3298] [109:24.48] ostensibly that was me. And I don't know
[L3299] [109:26.16] whether I was an expert on compression.
[L3300] [109:27.64] I guess I was an expert on storage at
[L3301] [109:28.92] least. And so and so they came to the
[L3302] [109:31.64] office and and uh and we just chat
[L3303] [109:34.76] chatted and it was so much fun, you
[L3304] [109:36.24] know? And so I was involved in um you're
[L3305] [109:38.88] pretty heavily involved in the show. Um
[L3306] [109:42.24] A lot of it was you know storyline and
[L3307] [109:44.64] and so forth. So like yes, sure, what
[L3308] [109:45.76] would you do with the compression
[L3309] [109:46.80] algorithm? What would could you design a
[L3310] [109:48.04] storage system? And and so coming up
[L3311] [109:49.48] with story ideas that that technically
[L3312] [109:51.80] accurate. They were really
[L3313] [109:54.80] you'd be surprised to know how much they
[L3314] [109:56.64] care about accuracy. A lot of um
[L3315] [109:59.48] people I know can't watch that show cuz
[L3316] [110:01.60] it's just so creepily [snorts]
[L3317] [110:04.04] accurate. They find it so cringey. And
[L3318] [110:06.20] partly why Silicon Valley can this TV
[L3319] [110:08.52] show could be so cringey is because
[L3320] [110:11.52] it's it's real. Like those stories are
[L3321] [110:14.12] almost almost
[L3322] [110:16.24] I don't know everyone. So many of the
[L3323] [110:17.96] stories in Silicon Valley are just real
[L3324] [110:19.40] stories. They're just they went to a
[L3325] [110:21.36] bunch of companies just farmed everyone
[L3326] [110:24.12] for like stories of crazy things that
[L3327] [110:26.60] happened in the tech industry and they
[L3328] [110:28.16] wove them into the series. And all the
[L3329] [110:30.20] characters are based on real people and
[L3330] [110:32.52] and real archetypes. Um but they also
[L3331] [110:34.60] cared very much about technical
[L3332] [110:35.68] accuracy. So I would also do technical
[L3333] [110:37.20] consulting and then they'd say stuff
[L3334] [110:38.40] like oh we're
[L3335] [110:40.08] building a data center in our house.
[L3336] [110:41.36] What should the rack look like? And you
[L3337] [110:43.84] know, what should the
[L3338] [110:45.20] diagram on the wall look like? And and
[L3339] [110:47.20] partly, you know, I wanted to be like oh
[L3340] [110:49.12] well it doesn't really matter. No one's
[L3341] [110:50.36] going to care. And they're like no, no,
[L3342] [110:51.68] no, it matters. Like they really cared
[L3343] [110:54.16] to get it right. Um
[L3344] [110:56.20] So yeah, I love the show, but it it can
[L3345] [110:58.44] be hard to watch just because of
[L3346] [111:00.56] oh my god, how how
[L3347] [111:03.04] real it can feel.
[L3348] [111:05.00] >> Are there any Easter eggs where you look
[L3349] [111:08.12] at it and go that's unusually accurate
[L3350] [111:10.24] or or you know, that system diagram
[L3351] [111:12.76] actually is like a very simple
[L3352] [111:15.40] >> I can't I don't think I can even say
[L3353] [111:17.32] them because
[L3354] [111:18.72] there were stories of like early
[L3355] [111:20.64] Dropbox, there were stories of having
[L3356] [111:23.00] ideas ripped off by other companies and
[L3357] [111:25.00] being tricked into having meetings with
[L3358] [111:26.80] folks only to, you know,
[L3359] [111:29.88] it may be even the the competitor's team
[L3360] [111:32.56] there to to steal the information. A lot
[L3361] [111:35.48] a lot of those stories are real, and so
[L3362] [111:37.72] there's people who who what's the
[L3363] [111:39.88] equivalent of value and like, oh wow,
[L3364] [111:41.24] that was that was something I went
[L3365] [111:43.04] through and probably it was because it
[L3366] [111:44.52] was about that situation.
[L3367] [111:46.62] >> [laughter]
[L3368] [111:47.76] >> Uh [snorts] that's that's such a cool
[L3369] [111:49.24] experience. Uh did you get paid for
[L3370] [111:51.28] that, or was just the
[L3371] [111:52.68] >> Yeah, that's a complicated question.
[L3372] [111:54.48] >> [laughter]
[L3373] [111:56.60] >> I got paid because I had to get paid
[L3374] [111:58.32] because it was like a Hollywood union
[L3375] [112:00.20] thing. I didn't want to get paid because
[L3376] [112:02.00] it made my visa more complicated, so
[L3377] [112:04.31] [laughter]
[L3378] [112:05.40] I've got a green card now, I'm all good,
[L3379] [112:06.84] but yeah, but that there was something
[L3380] [112:08.84] where they had to pay me $400. Um
[L3381] [112:11.88] Anyway, I made a grand sum of $400 off
[L3382] [112:13.60] that show.
[L3383] [112:14.79] >> [laughter]
[L3384] [112:16.08] >> Uh looking back on your career, is there
[L3385] [112:18.60] any regret that comes to mind that maybe
[L3386] [112:20.76] other people can learn from?
[L3387] [112:22.76] >> Uh yeah.
[L3388] [112:24.40] I I mean, ooh.
[L3389] [112:26.68] I think I underinvested in my personal
[L3390] [112:28.32] life, to be honest.
[L3391] [112:29.92] I people are probably going to say that
[L3392] [112:30.88] much, you know, because I think you can
[L3393] [112:32.28] be all about like growth, and
[L3394] [112:35.24] you sure I could have grown more. I
[L3395] [112:36.80] could have dropped out of grad school
[L3396] [112:38.20] say three years in or four years in, and
[L3397] [112:40.28] probably would have learned just as
[L3398] [112:41.20] much. I could have taken a job at
[L3399] [112:42.88] Dropbox back, you know, two, three years
[L3400] [112:45.12] earlier and made a lot more money. Um
[L3401] [112:48.44] everyone has been in the industry long
[L3402] [112:49.72] enough has been offered to co-found
[L3403] [112:52.08] several billion-dollar companies. Like,
[L3404] [112:53.84] everyone has a story about the times
[L3405] [112:55.84] they could have been a billionaire
[L3406] [112:56.80] several times over. Um I don't really
[L3407] [112:59.32] regret those. I think um
[L3408] [113:02.96] Yes,
[L3409] [113:03.92] it's been a lot of sacrifice to be
[L3410] [113:06.60] to be blunt. I've been on call my whole
[L3411] [113:09.40] career. You know, I've been I've carried
[L3412] [113:11.68] laptop almost every day.
[L3413] [113:13.60] Um there's many
[L3414] [113:15.56] dinners and parties and events I've had
[L3415] [113:17.76] to skip and there's people in my
[L3416] [113:19.24] personal life who have um suffered as a
[L3417] [113:21.68] result and I really appreciate this
[L3418] [113:23.56] people and they they love and care about
[L3419] [113:25.24] me and they know that I just have a
[L3420] [113:26.32] passion for this and so
[L3421] [113:28.80] you know, they they accept me for who I
[L3422] [113:30.52] am. I think it's um
[L3423] [113:34.00] it's it this is like this is, you know,
[L3424] [113:35.96] this is old person talk. But yeah, I
[L3425] [113:37.36] think everyone has to decide like how
[L3426] [113:39.52] much they want to really drive their
[L3427] [113:41.28] career. Cuz there's a trade-off like
[L3428] [113:43.08] absolutely like
[L3429] [113:44.88] I made a tremendous amount of sacrifices
[L3430] [113:46.72] in my career and I really
[L3431] [113:48.40] prioritized
[L3432] [113:49.92] building as probably the num- number one
[L3433] [113:52.52] I mean values first and then building.
[L3434] [113:54.80] But if yeah, if we went back in time,
[L3435] [113:56.28] yeah, I would have had I had a good
[L3436] [113:57.88] life, but I probably would have done
[L3437] [113:59.88] more vacations and you know, I just
[L3438] [114:02.60] had a bit more of a balanced life. I I
[L3439] [114:04.36] really do think I mean, I see that with
[L3440] [114:05.84] all the 996 stuff and and this kind of
[L3441] [114:08.48] performative like
[L3442] [114:10.24] you know, photos of being in a bar and a
[L3443] [114:12.84] laptop and stuff and I'm like, that's
[L3444] [114:14.72] not that's not real. Like that's not I
[L3445] [114:17.20] mean, I'm sure I was working more than
[L3446] [114:18.52] 996 back then, but like I probably still
[L3447] [114:21.00] do work more than 996, but that's I
[L3448] [114:23.48] but I don't do it like um as a checkbox.
[L3449] [114:26.40] You know, I do it cuz I just really want
[L3450] [114:27.68] to be doing stuff and and so I think
[L3451] [114:29.80] just um
[L3452] [114:31.60] I would have I would caution people
[L3453] [114:33.76] against that hustle culture. I'll I'll
[L3454] [114:36.12] that's not
[L3455] [114:37.60] Firstly, like you you know, you're only
[L3456] [114:39.20] young once. You should you should have
[L3457] [114:41.52] fun. Um you know, I've got quite a few
[L3458] [114:43.96] grays in here, you know. Um but um but
[L3459] [114:47.72] also
[L3460] [114:49.00] that's that's that's acting. I mean,
[L3461] [114:51.24] focus on solving problems, work hard, be
[L3462] [114:53.32] passionate. Yeah.
[L3463] [114:55.00] >> Yeah, well, when I studied your career,
[L3464] [114:56.52] I mean,
[L3465] [114:57.56] there's there's mentions of you working
[L3466] [114:59.36] at 16 hours a week in various
[L3467] [115:01.72] but um
[L3468] [115:02.96] you know you you like on call you like
[L3469] [115:05.72] fires
[L3470] [115:07.68] you like ownership like all those things
[L3471] [115:10.32] are recipe for working obscene hours.
[L3472] [115:13.84] >> Yeah, and you know I go home and I'm
[L3473] [115:15.68] tired and I wind down by building stuff
[L3474] [115:18.24] now like I
[L3475] [115:19.60] I'm lucky enough to have a little
[L3476] [115:20.52] workshop at home and so I go home and I
[L3477] [115:22.40] you know make things with my hands.
[L3478] [115:25.16] That's just you know that's just you
[L3479] [115:26.76] become an infra person.
[L3480] [115:28.68] You become an you become an engineer
[L3481] [115:30.40] like in all aspects of your life
[L3482] [115:33.24] but yeah I would just I would just say
[L3483] [115:35.12] like
[L3484] [115:36.40] the cool thing is
[L3485] [115:38.56] doing cool stuff that humans use.
[L3486] [115:41.72] The cool thing's not working long hours.
[L3487] [115:43.44] The cool thing's not like showing off
[L3488] [115:45.16] about about that you were running a
[L3489] [115:47.40] coding agent all night. Who cares? The
[L3490] [115:49.36] cool stuff's the cool thing's
[L3491] [115:51.40] enjoying
[L3492] [115:53.20] doing important things.
[L3493] [115:54.84] >> Do you have a best technical book
[L3494] [115:57.08] recommendation for our people?
[L3495] [116:00.00] >> I mean I have to be honest I
[L3496] [116:03.56] I haven't read almost any
[L3497] [116:05.72] technical book.
[L3498] [116:07.31] >> [laughter]
[L3499] [116:08.80] >> I mean obviously I was in academia for a
[L3500] [116:10.52] long time so I read a lot of papers.
[L3501] [116:11.96] Read a lot of papers.
[L3502] [116:13.68] Yeah, learning is awesome. Reading's
[L3503] [116:15.24] great but balance it right?
[L3504] [116:17.64] Read something and then go put into
[L3505] [116:19.64] practice and most of my career I have I
[L3506] [116:22.44] mean like sure I did a PhD so I guess
[L3507] [116:24.32] that that is like the academic side but
[L3508] [116:26.60] after that most of my learning's been by
[L3509] [116:28.04] doing. Cuz there's nothing like being
[L3510] [116:30.24] faced with a real problem in your face
[L3511] [116:31.92] to like to really to really develop as
[L3512] [116:34.88] an engineer.
[L3513] [116:36.56] >> Yeah, and I think if I answer the
[L3514] [116:38.20] question I'd probably say the same. I
[L3515] [116:39.92] think learning by doing is that's that's
[L3516] [116:42.52] really where where it matters most.
[L3517] [116:45.04] And then last question for you is if you
[L3518] [116:47.40] could go back to the beginning of your
[L3519] [116:48.68] career and give yourself some advice
[L3520] [116:50.24] what would you say?
[L3521] [116:51.52] >> I'd say
[L3522] [116:53.20] you know what it'll it'll be okay. Like
[L3523] [116:55.08] don't sweat sweat the small stuff as
[L3524] [116:56.92] much. It's hard cuz like my
[L3525] [116:59.80] my whole like engineering brand is about
[L3526] [117:01.88] caring about details and like I I love
[L3527] [117:04.36] like Dieter Rams and like design, you
[L3528] [117:06.88] know, and and and so so being obsessive
[L3529] [117:10.08] is a little bit part of my DNA.
[L3530] [117:13.12] But I think I would go back
[L3531] [117:15.24] and say career's a long I mean there's
[L3532] [117:18.00] just
[L3533] [117:19.28] any story anyone reads about 22-year-old
[L3534] [117:23.52] billionaire blah blah blah just ignore
[L3535] [117:25.40] that story. That's not that's not real.
[L3536] [117:28.24] That's not repeatable. That's not normal
[L3537] [117:30.48] and it's not that healthy and it's not
[L3538] [117:33.52] that good for the people either, right?
[L3539] [117:37.00] You probably won't ideally won't max out
[L3540] [117:41.40] your growth for 20 plus years as an
[L3541] [117:44.12] engineer.
[L3542] [117:45.24] I'm still learning all the time and I've
[L3543] [117:46.60] been an engineer for several decades. Um
[L3544] [117:49.32] so my advice would be don't sweat it.
[L3545] [117:51.92] There's time to grow and I do think that
[L3546] [117:55.08] again is is is a little bit of a
[L3547] [117:57.80] modern phenomenon but there's a feeling
[L3548] [117:59.44] right now I'm not going to AGI come and
[L3549] [118:01.52] better max out my growth
[L3550] [118:04.12] in the next 3 months. Well, guess what?
[L3551] [118:05.36] You ain't going to do it. It's not going
[L3552] [118:07.20] to happen, right? You can't do it. You
[L3553] [118:09.60] can't max your growth out in the next 3
[L3554] [118:11.56] months. It won't happen. You don't have
[L3555] [118:13.16] to running 17 agents at the same time.
[L3556] [118:15.28] All you got to do is
[L3557] [118:17.36] orient your career around learning every
[L3558] [118:21.40] day and getting better at what you're
[L3559] [118:22.48] doing and trying to solve things in the
[L3560] [118:23.80] most simple ways.
[L3561] [118:25.76] >> Yeah, I mean on Twitter I I see this
[L3562] [118:28.16] take all the time of this permanent
[L3563] [118:30.04] underclass idea where
[L3564] [118:32.68] you know, if you if you don't make it in
[L3565] [118:34.48] time for AGI then you know, you're going
[L3566] [118:36.88] to be part of this permanent underclass.
[L3567] [118:39.36] >> Yeah. I mean look it's a bit challenging
[L3568] [118:41.76] economic times for a lot of folks and I
[L3569] [118:43.16] don't want to be I don't want to be
[L3570] [118:45.16] unsympathetic to people who are you
[L3571] [118:47.00] know, having financial difficulties.
[L3572] [118:49.08] At the same time it's just not an
[L3573] [118:51.04] instructive attitude. There's not much
[L3574] [118:52.88] you can do with that information other
[L3575] [118:54.28] than feel bad about yourself. And and
[L3576] [118:57.12] and I and I don't and I and someone will
[L3577] [118:59.12] tell someone will argue back, "No, what
[L3578] [119:01.08] you can do is get really good at using
[L3579] [119:02.72] Claude." Well, guess what? It's not very
[L3580] [119:04.56] hard to use Claude. It's not like grab
[L3581] [119:07.20] some Sometimes people tell me like, "Oh
[L3582] [119:09.00] my god, I'm I'm finding it hard to keep
[L3583] [119:11.44] up with all the new models, the new
[L3584] [119:12.92] model drops." I don't even know what the
[L3585] [119:14.64] new models are. Like I I use them, but I
[L3586] [119:17.52] forget the latest model cuz it it
[L3587] [119:19.56] doesn't doesn't matter, right? Like
[L3588] [119:21.84] Like there was this thing called Ralph,
[L3589] [119:24.04] right? I guess it's still Ralph. It's
[L3590] [119:25.16] like a loop thing. I don't really know
[L3591] [119:27.44] what Ralph is, and I haven't heard
[L3592] [119:29.20] anyone mention Ralph in the past few
[L3593] [119:30.68] weeks, but it was the biggest thing in
[L3594] [119:32.52] the in Twitter for like a month.
[L3595] [119:34.92] And it just doesn't this is noise.
[L3596] [119:37.56] Somehow sometimes I feel like it's like
[L3597] [119:39.72] um it's like tech tabloids. It's like
[L3598] [119:42.64] people think that they're learning by
[L3599] [119:45.80] somehow knowing like listening to what
[L3600] [119:47.76] Jensen said today, or like, "Oh my god,
[L3601] [119:50.96] Boris said that Claude writes itself."
[L3602] [119:54.08] I don't think people you're learn That's
[L3603] [119:56.20] like it's just like reading about
[L3604] [119:58.24] Beyoncé, but you're a nerd and so you're
[L3605] [120:01.68] reading about Jensen, right? But like it
[L3606] [120:04.08] doesn't [laughter] matter. You're not
[L3607] [120:05.40] growing. Like you don't have to know.
[L3608] [120:07.08] It's okay.
[L3609] [120:08.28] The new coding agent could come out and
[L3610] [120:10.16] you could miss it. And then next year
[L3611] [120:13.72] if if it turns out it's the big one,
[L3612] [120:15.40] you'll just use it. Like it's not hard.
[L3613] [120:17.16] Like I haven't seen any skill so far. I
[L3614] [120:19.92] guess there's some skill, but it's not a
[L3615] [120:21.64] hard skill. If you're good at
[L3616] [120:23.36] engineering, you can figure out how to
[L3617] [120:24.92] use Claude code, right? Or open code.
[L3618] [120:26.92] So, just watch out for tech tabloidism.
[L3619] [120:31.64] It doesn't matter. Just Just be building
[L3620] [120:34.08] stuff. Just Just Just do real crap.
[L3621] [120:36.84] >> Uh I love I love that mindset and um
[L3622] [120:40.64] yeah. Well, that you know, thank you for
[L3623] [120:42.64] >> I'm on Twitter, too. Like I'm you know,
[L3624] [120:44.40] I'm part of the thing. You know, but
[L3625] [120:45.52] like
[L3626] [120:46.40] but just ignore me, too. Like
[L3627] [120:48.97] >> [laughter]
[L3628] [120:51.16] >> Oh god. All right. Well, thank you so
[L3629] [120:53.16] much for your time, James. I really
[L3630] [120:54.44] appreciate it. This was a lot of fun.
[L3631] [120:56.12] >> All right. It was great. Thank you.
[L3632] [120:57.76] >> Hey, thank you for watching this
[L3633] [120:58.80] podcast. If you liked it and you want to
[L3634] [121:00.44] see the show grow, please support with a
[L3635] [121:02.60] comment or a like.
[L3636] [121:04.60] Also, if you have any recommendations
[L3637] [121:06.48] for people you want me to bring on,
[L3638] [121:08.48] please drop a comment. Guests like
[L3639] [121:10.60] Barbara Liskov, Mike Stonebreaker, Mark
[L3640] [121:13.32] Brooker, these were all people that I
[L3641] [121:15.40] brought on because someone left a
[L3642] [121:17.24] comment. On another note, aside from the
[L3643] [121:19.48] podcast, I'm working on building the
[L3644] [121:21.28] ergonomic keyboard that I wish existed.
[L3645] [121:23.76] Here's a glance at the prototype. It's a
[L3646] [121:25.64] split keyboard, so there's two sides. Um
[L3647] [121:28.68] this is in the case. But yeah, we
[L3648] [121:30.12] launched on Kickstarter and we hit our
[L3649] [121:31.92] goal within 8 hours of launching. I
[L3650] [121:34.00] really appreciate it if you were one of
[L3651] [121:35.40] the people who grabbed one of the early
[L3652] [121:37.16] units. Um we're now working on the long
[L3653] [121:39.48] journey of building the tooling now. And
[L3654] [121:41.60] so, if you still want to pick one up,
[L3655] [121:43.28] I've left the late pledges open
[L3656] [121:46.36] so you can grab one there. I'll put a
[L3657] [121:47.88] link in the description. Thank you again
[L3658] [121:50.44] for watching the podcast, and I'll see
[L3659] [121:52.52] you in the next episode.
