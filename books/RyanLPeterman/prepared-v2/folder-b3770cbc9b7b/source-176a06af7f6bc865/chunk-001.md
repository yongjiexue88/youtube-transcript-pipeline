Chunk 1; segments 1–375. 

# The Co-Creator of Kubernetes: Engineering-Led Direction and Convincing Management | Brendan Burns

Source ID: source-176a06af7f6bc865
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/The_Co-Creator_of_Kubernetes_Engineering-Led_Direction_and_Convincing_Management_Brendan_Burns_en.txt
Video: https://www.youtube.com/watch?v=FKijpCEH9D8

[L10] [00:00.00] There's going to be an open source one.
[L11] [00:02.08] Do you want it to be ours or do you want
[L12] [00:03.92] it to be someone else's?
[L13] [00:05.56] >> This is Brendan [music] Burns, the
[L14] [00:07.28] co-creator of Kubernetes, and I asked
[L15] [00:09.64] him about the stories behind building
[L16] [00:11.48] it. [music]
[L17] [00:11.84] >> The hardest part actually of the project
[L18] [00:13.76] was actually articulating that.
[L19] [00:15.96] >> How long did that initial MVP take to
[L20] [00:18.92] build?
[L21] [00:19.64] >> I don't know, a little under a week,
[L22] [00:20.76] maybe.
[L23] [00:21.52] >> He had interesting career advice
[L24] [00:23.40] grounded in his career story.
[L25] [00:25.24] >> I believe you can hide order 10% of your
[L26] [00:27.84] effort from your management.
[L27] [00:29.96] >> Is there any upper bound where
[L28] [00:31.56] Kubernetes just cannot handle that load?
[L29] [00:34.40] >> Every time you change an order of
[L30] [00:35.68] magnitude, the problem moves.
[L31] [00:37.68] >> Here's the full episode.
[L32] [00:43.44] I mean, let's start with Kubernetes cuz
[L33] [00:45.12] that's super interesting. I don't I
[L34] [00:47.96] don't fully understand the business
[L35] [00:49.56] motivation. Like, let's say I was your
[L36] [00:52.60] director or something like that and you
[L37] [00:54.60] you came to me with this and you said,
[L38] [00:55.84] "Hey, let's let's do this for everyone."
[L39] [00:58.92] I don't fully understand what would be
[L40] [01:00.32] in that strategy doc or that What would
[L41] [01:02.56] you say in that meeting that would say,
[L42] [01:04.56] "Here's the impact for Google if we
[L43] [01:06.80] invest in building this for the the
[L44] [01:09.24] industry?"
[L45] [01:09.96] >> Yeah, it's funny cuz like the hardest
[L46] [01:11.24] part actually of the project I would say
[L47] [01:13.08] that in those early days was actually
[L48] [01:15.44] articulating that.
[L49] [01:17.16] Um and I think it was really clear in
[L50] [01:18.76] our heads, but like figuring out how to
[L51] [01:21.60] convince people
[L52] [01:23.32] um
[L53] [01:24.20] uh was tricky. Um and you know, I think
[L54] [01:28.24] there was there were a variety of
[L55] [01:29.52] different ways that we articulated why
[L56] [01:31.60] it was important.
[L57] [01:33.32] Um
[L58] [01:33.96] one of them was uh related to the uh
[L59] [01:37.72] MapReduce white paper.
[L60] [01:39.76] Right? So, MapReduce at the time,
[L61] [01:42.00] especially like Hadoop and big data were
[L62] [01:44.24] were were a big deal. I think that, you
[L63] [01:45.84] know, other things have kind of replaced
[L64] [01:47.40] them at this point, but like MapReduce
[L65] [01:49.52] was a big deal. Um and the the big data
[L66] [01:51.72] revolution or whatever they called it.
[L67] [01:53.96] Um
[L68] [01:54.76] and you know, Google had written the
[L69] [01:57.60] original white paper.
[L70] [01:59.24] Um but Hadoop was an open source project
[L71] [02:02.88] that Google had nothing to do with.
[L72] [02:05.52] And got no credit for
[L73] [02:07.36] it. And and and they just read the white
[L74] [02:09.72] paper and they re-implemented it and
[L75] [02:11.36] it's not the same. It's similar, but
[L76] [02:13.08] it's not the same, right? Because
[L77] [02:14.52] anytime you re-implement something, it's
[L78] [02:15.96] not the same. And so part of the
[L79] [02:17.40] argument was like, "Look, like
[L80] [02:19.48] we have this cloud and we want to like
[L81] [02:22.60] be influencing the technology
[L82] [02:24.28] technological landscape if all we do is
[L83] [02:26.64] kick out white papers,
[L84] [02:28.84] we're not like if it doesn't run, if
[L85] [02:30.88] it's not something that people can run,
[L86] [02:33.00] they're not we're not going to be in the
[L87] [02:35.48] driver's seat.
[L88] [02:36.96] Um and so that was one of the one of the
[L89] [02:39.84] one of the arguments. I think, you know,
[L90] [02:41.32] the other couple arguments were like,
[L91] [02:42.36] "Why containers? Why not why
[L92] [02:44.80] why not you know, people are using VMs,
[L93] [02:46.76] why containers?" And you know, a lot of
[L94] [02:48.80] that was talking about like, "Look,
[L95] [02:50.80] the demands of writing software and we
[L96] [02:53.04] know internally, we know from doing this
[L97] [02:54.92] internally that the demands of writing
[L98] [02:56.52] reliable software necessitate having
[L99] [02:59.68] systems that are sort of like autopilots
[L100] [03:02.00] for your
[L101] [03:03.12] um
[L102] [03:04.32] you know, for your application. And and
[L103] [03:06.96] we know that this is something that as
[L104] [03:09.36] software becomes more and more critical
[L105] [03:10.80] to more and more businesses, this is
[L106] [03:12.24] something that you they're just going to
[L107] [03:13.60] have to have, right? And so that's sort
[L108] [03:15.68] of the why containers part. Um
[L109] [03:18.68] and then
[L110] [03:20.04] you know, I think that the third part
[L111] [03:21.28] was the like why open source, right? And
[L112] [03:23.32] in some sense, that's like the most
[L113] [03:24.52] interesting conversation because people
[L114] [03:26.76] are like, "Wow, this would be you know,
[L115] [03:27.88] you've convinced me, right? Like you've
[L116] [03:29.64] convinced me we should build it, we
[L117] [03:30.88] should make it available to the world.
[L118] [03:32.20] It's something that they're going to
[L119] [03:33.08] find useful. Um but wouldn't it be so
[L120] [03:35.92] much better if they could only use it on
[L121] [03:38.20] our platform?"
[L122] [03:40.08] And you're like, "Yeah, that's
[L123] [03:40.84] absolutely the case,
[L124] [03:42.60] but
[L125] [03:43.84] you can't win if you make it only on
[L126] [03:46.04] your platform."
[L127] [03:47.84] >> Well, why is that?
[L128] [03:49.44] >> Well, because there's other platforms
[L129] [03:51.12] out there, right? And so, if you make it
[L130] [03:53.40] an exclusive, then
[L131] [03:56.40] the people who for other reasons are on
[L132] [03:58.52] other clouds or on on-premise,
[L133] [04:01.56] they're shut out.
[L134] [04:03.32] And
[L135] [04:04.80] so, they're going to just go build an
[L136] [04:05.92] alternative.
[L137] [04:07.32] Right? Like the like the the open source
[L138] [04:09.52] the it's it's sort of like a Linux, you
[L139] [04:11.40] know, uh the reason Linux won, right?
[L140] [04:13.16] It's because Linux could go anywhere.
[L141] [04:15.20] Right? The whole reason that open tech
[L142] [04:17.56] and open ecosystems win is because
[L143] [04:20.60] you the majority of people
[L144] [04:23.80] are going to be not on your plat like if
[L145] [04:25.80] you're if you're not the leader, and we
[L146] [04:27.76] and you know, GCP was not the leader,
[L147] [04:29.96] then the majority of people are not
[L148] [04:31.16] going to be on your platform.
[L149] [04:33.20] And so, if you make it such that the
[L150] [04:34.56] majority of people can't use your thing,
[L151] [04:36.12] they're just going to ignore you, and
[L152] [04:37.16] then they're going to go build their
[L153] [04:38.08] own.
[L154] [04:39.12] Right? Whereas, if you go and build it
[L155] [04:41.00] and you build it for everybody, but you
[L156] [04:42.32] make sure that it's awesome on your
[L157] [04:43.52] platform, then you have a chance of
[L158] [04:46.32] attracting people attracting more people
[L159] [04:48.32] to your platform,
[L160] [04:49.92] uh than otherwise. And and then I mean,
[L161] [04:51.76] also in some ways it's just like the
[L162] [04:52.92] aesthetic of the time, also, right? It's
[L163] [04:54.80] like if everybody's using Linux, and
[L164] [04:57.12] everybody's using Docker, and
[L165] [04:58.48] everybody's using these programming
[L166] [05:00.28] languages that are all open, like if
[L167] [05:01.96] everything else is open source,
[L168] [05:03.88] you don't want to be the thing that's
[L169] [05:05.16] not.
[L170] [05:06.52] Right? And and there's only a few places
[L171] [05:08.72] where like
[L172] [05:10.60] where that hasn't been true historically
[L173] [05:12.24] in technology, where you could be
[L174] [05:13.64] different and still succeed, and you
[L175] [05:15.28] have to be so differentiated
[L176] [05:17.56] that and I don't think that we were
[L177] [05:19.20] different that differentiated. You have
[L178] [05:20.92] to be so differentiated such that people
[L179] [05:22.84] are like, "Oh, actually, I want that
[L180] [05:24.48] thing so bad, I don't care that it's
[L181] [05:26.12] closed."
[L182] [05:26.96] >> So, at the time just thinking what was
[L183] [05:29.24] the competitive landscape, I guess
[L184] [05:31.96] if I if I remember, it was I mean, AWS
[L185] [05:34.76] was dominant. They were there first and
[L186] [05:36.52] doing very well. GCP at that time
[L187] [05:39.48] probably an up-and-coming company uh or
[L188] [05:42.88] I guess offering.
[L189] [05:44.20] And so, am I understanding then that the
[L190] [05:46.52] idea is let's pull market share away by
[L191] [05:49.72] giving kind of open source distributing
[L192] [05:52.64] Kubernetes to more and more developers
[L193] [05:56.36] and then they'll be more open to kind of
[L194] [05:58.16] migrating or using GCP because you'll
[L195] [06:00.28] make a
[L196] [06:00.96] >> They'll pay attention. Right, they'll
[L197] [06:02.24] pay attention. And also like you change
[L198] [06:04.04] the dialogue too, right? Like tail light
[L199] [06:05.56] chasing is hard.
[L200] [06:07.16] Right? Like if if someone else has built
[L201] [06:08.92] VMs and everybody's using VMs and all
[L202] [06:11.24] you're doing is saying like, "Well,
[L203] [06:12.60] we're building the same thing that they
[L204] [06:14.40] have
[L205] [06:15.56] only maybe it's a little bit better
[L206] [06:17.20] because we do something else over here
[L207] [06:18.96] or you know, whatever." Like that's a
[L208] [06:20.52] hard market strategy to articulate. But
[L209] [06:22.96] if you create a brand new playing field
[L210] [06:25.12] where you are the thought leader
[L211] [06:28.60] um
[L212] [06:30.08] suddenly like people are listening to
[L213] [06:31.48] you. Even if they're not using it on
[L214] [06:32.76] your platform, they're listening to you
[L215] [06:34.12] and that gives you way more voice. You
[L216] [06:35.96] get you get a lot more voice in the
[L217] [06:37.28] market. It changes the narrative. It
[L218] [06:38.92] changes who people are listening to.
[L219] [06:41.72] Um and so that control of of
[L220] [06:44.44] the story is an important aspect of of
[L221] [06:47.12] of how I think how you
[L222] [06:49.24] break through that or you try to break
[L223] [06:50.84] through that dynamic. Obviously, like
[L224] [06:53.56] you know, they're still in third at this
[L225] [06:54.80] point. So like
[L226] [06:56.44] didn't work out, but um I mean, I
[L227] [06:59.12] wouldn't say it didn't work out. I think
[L228] [07:00.16] it worked out in general, but it's still
[L229] [07:01.56] hard. Like overcoming those kinds of
[L230] [07:03.08] market dynamics is hard and you know, I
[L231] [07:05.12] think the other thing that happened is
[L232] [07:06.08] everybody in the cloud consolidated
[L233] [07:08.08] around it and so now Kubernetes is just
[L234] [07:09.88] sort of a utility everywhere.
[L235] [07:12.32] >> You you mentioned that I guess that
[L236] [07:13.88] perception benefit of being at the
[L237] [07:16.72] dominant offering. Um which I mean, if
[L238] [07:19.96] you if you look at what happened in
[L239] [07:21.88] hindsight, it makes a lot of sense. I
[L240] [07:23.44] mean, that is what happened and it's
[L241] [07:25.48] it's uh a wonderful benefit. But I guess
[L242] [07:28.00] when you were looking forward and you
[L243] [07:30.04] were talking to leadership were you
[L244] [07:32.68] cognizant of those benefits and saying,
[L245] [07:35.24] "We need to do this because
[L246] [07:37.20] we're going to kind of become the
[L247] [07:39.40] dominant offering and it's going to have
[L248] [07:41.40] all these
[L249] [07:42.64] uh optics benefits.
[L250] [07:44.88] >> I mean, I think we absolutely wanted to
[L251] [07:46.48] make sure that we were front and center
[L252] [07:47.76] in terms of thought leadership and we
[L253] [07:49.32] definitely articulated that. Right?
[L254] [07:51.72] Absolutely right. Like being being in a
[L255] [07:53.76] thought leadership position is value is
[L256] [07:55.84] valuable.
[L257] [07:56.96] >> It's interesting cuz um I feel like it's
[L258] [07:59.20] hard to quantify. I mean, if I was in
[L259] [08:01.72] that meeting and we're trying to make a
[L260] [08:02.88] call
[L261] [08:03.76] >> Yeah, yeah, yeah.
[L262] [08:04.32] >> how much is that worth?
[L263] [08:06.08] >> Yeah. Well, I think you have to also
[L264] [08:07.32] realize that at the time like it was
[L265] [08:08.44] pretty cheap, right? It was like eight
[L266] [08:09.92] or nine engineers.
[L267] [08:11.44] And and we kind of and this is in some
[L268] [08:12.92] sense I mean it's both a blessing and a
[L269] [08:14.32] curse. Like part of the reason why we
[L270] [08:15.96] articulated and argued for having such a
[L271] [08:18.80] distinct brand
[L272] [08:21.20] where the Kubernetes brand was separated
[L273] [08:23.64] from the Google brand um
[L274] [08:26.32] was that it kind of gave us freedom to
[L275] [08:28.16] fail also. It was like, "Hey, if these
[L276] [08:30.24] eight people go off and you know, do
[L277] [08:32.76] something and and it turns out to be
[L278] [08:34.60] stupid, like
[L279] [08:36.56] we'll just kill it off and it won't have
[L280] [08:38.68] like it won't you know, it won't um it
[L281] [08:41.28] won't damage the broader perception of
[L282] [08:43.24] the cloud. And so I think there's
[L283] [08:44.28] there's that benefit of the open source
[L284] [08:45.60] part of it, too.
[L285] [08:47.20] Um it helped with adoption, right? Like
[L286] [08:48.84] it helped
[L287] [08:50.28] it helped us and especially as we went
[L288] [08:51.76] to like the Linux Foundation and things
[L289] [08:53.48] like that and truly established like an
[L290] [08:55.28] independent entity, it helped ensure
[L291] [08:57.56] that you know, people like Red Hat or
[L292] [08:59.36] Azure or AWS could take a bet on
[L293] [09:01.92] Kubernetes and feel confident in that
[L294] [09:03.68] bet. Um but it also was an insurance
[L295] [09:06.60] policy against failure. And and also to
[L296] [09:08.84] be honest like it was it it simplified a
[L297] [09:10.44] lot of things, too, because
[L298] [09:12.12] you know, we were competing against
[L299] [09:13.16] startups, right? Like at the time Docker
[L300] [09:14.68] is a startup. They can be way more agile
[L301] [09:16.84] than a big company and so by virtue of
[L302] [09:19.48] sort of like
[L303] [09:21.04] being a separate entity uh we could be a
[L304] [09:24.12] little bit more agile, also.
[L305] [09:26.08] >> I mean, the earliest conception of this
[L306] [09:27.76] project was you and two others kind of
[L307] [09:30.84] hacking something together.
[L308] [09:32.40] >> Yeah, it was a demo. I mean, it was sort
[L309] [09:33.56] of a demo almost. It was like, "Look
[L310] [09:35.00] look what we can do if we just smash a
[L311] [09:36.92] bunch of existing open source tech
[L312] [09:38.44] together.
[L313] [09:39.44] >> Well, what did that demo do?
[L314] [09:42.00] >> Uh I mean, it was basically like a basic
[L315] [09:44.28] cube control.
[L316] [09:45.92] It was like, "Hey, here's like here's a
[L317] [09:47.36] container I built." I mean, at the time
[L318] [09:49.44] you had to explain Docker to people. You
[L319] [09:50.80] were like, "Hey, here's Docker. I used
[L320] [09:52.48] it to like build this container image."
[L321] [09:54.68] Um
[L322] [09:55.72] and and then you could run it and deploy
[L323] [09:57.88] it and see that it had gotten
[L324] [09:59.40] distributed across a bunch of machines
[L325] [10:01.60] and that you could, you know, load
[L326] [10:02.64] balance to it cuz you you'd hit a single
[L327] [10:04.76] endpoint and it would go, "I'm replica
[L328] [10:06.32] one." And then you'd hit reload and go,
[L329] [10:07.88] "I'm replica three." And, you know, so
[L330] [10:09.76] it like showed that it was replicated
[L331] [10:12.24] and then
[L332] [10:13.24] um
[L333] [10:14.00] basic health checking. So, like if you
[L334] [10:15.72] killed it, it would come back and uh a
[L335] [10:17.88] V2 to V or a V1 to V2 upgrade. That was
[L336] [10:20.32] about it.
[L337] [10:21.12] >> How How long did that that initial MVP
[L338] [10:24.40] take to build?
[L339] [10:25.92] >> Uh I wrote it in, I don't know, a little
[L340] [10:28.48] under a week, maybe. Something like
[L341] [10:30.12] that.
[L342] [10:31.08] I mean, like I don't don't work on the
[L343] [10:32.52] weekends, so maybe 5 days, 4 days, 5
[L344] [10:34.56] days.
[L345] [10:35.76] >> Did And did you drop all of your
[L346] [10:36.96] existing work? Cuz I'm imagining your
[L347] [10:39.56] you had existing project work and this
[L348] [10:42.00] is kind of extra credit stuff that you
[L349] [10:44.20] were working on.
[L350] [10:45.60] >> Yeah, well, I mean, I wouldn't say I
[L351] [10:48.32] I dropped it, but like in in a time
[L352] [10:50.80] scale of that time scale, like
[L353] [10:53.40] you can kind of like slack on it a
[L354] [10:55.12] little bit. You know, like
[L355] [10:57.44] like you could be sick for a week. I
[L356] [10:58.64] mean, I guess the thing is like you
[L357] [10:59.40] could be sick for a week, you know? And
[L358] [11:01.12] I'm not saying that I That's not what we
[L359] [11:02.40] did. That's not what I did, but like but
[L360] [11:04.84] but there was enough flexibility in in
[L361] [11:06.76] the system that like you could hack it
[L362] [11:08.88] together. Um And I mean, believe me, it
[L363] [11:11.60] was hacked together, right? Like every
[L364] [11:13.52] possible shortcut to take and every And,
[L365] [11:16.64] you know, I think one of the things I've
[L366] [11:17.48] been good at historically is um
[L367] [11:20.28] integrating other open source projects
[L368] [11:22.12] together, seeing how you can take stuff
[L369] [11:23.92] off the shelf and put it together. And
[L370] [11:26.08] so, you know,
[L371] [11:28.04] a lot of the nuts and bolts were
[L372] [11:31.76] pieces that we could take from other
[L373] [11:33.64] open-source projects and um
[L374] [11:35.96] and kind of combine together with a
[L375] [11:37.36] little with glue and glue code to
[L376] [11:40.48] they'll you know to to give the feel of
[L377] [11:42.00] it. So, that helps, too.
[L378] [11:43.56] >> I think a lot of software engineers when
[L379] [11:45.36] they hear this kind of story,
[L380] [11:47.72] they think, "Oh, I have my existing
[L381] [11:50.16] responsibilities and I can't necessarily
[L382] [11:52.52] go off and build this thing, even though
[L383] [11:54.36] I think it's a great idea." Do you have
[L384] [11:56.44] any advice for someone who has that
