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
[L385] [11:58.52] opinion?
[L386] [11:59.72] >> Yeah, well, I mean, I think that what
[L387] [12:01.24] what even this I would say there's two
[L388] [12:02.32] things two I have two answers to that.
[L389] [12:04.76] Um one is advice that I've always given
[L390] [12:06.72] to every single um
[L391] [12:09.48] person that's ever worked for me, which
[L392] [12:11.20] is
[L393] [12:12.36] I believe you can hide
[L394] [12:14.24] order 10% of your effort from your
[L395] [12:16.20] management,
[L396] [12:17.44] right? So, like
[L397] [12:20.24] you know,
[L398] [12:21.88] there's a there you have slack. You have
[L399] [12:23.52] the ability to slack, no matter what,
[L400] [12:26.44] right? Um
[L401] [12:28.64] and you know, as you get a bigger and
[L402] [12:30.36] bigger org, actually the percent that
[L403] [12:31.88] what you can do with that 10% actually
[L404] [12:34.28] increases. Um and a lot of really good
[L405] [12:37.12] of really influential good ideas that
[L406] [12:39.00] I've had have come out of that. I mean,
[L407] [12:41.28] it's another I mean, it's kind of a flip
[L408] [12:42.88] way of saying, "I want to empower people
[L409] [12:45.48] locally to make local decisions that
[L410] [12:47.16] they think are optimal for the business
[L411] [12:49.28] without having to consult up the chain,
[L412] [12:51.28] without having to ask permission,
[L413] [12:53.12] right?
[L414] [12:54.04] And you tell people while when you tell
[L415] [12:55.56] them that, you're like, "By the way,
[L416] [12:57.92] you're also going to make a bunch of bad
[L417] [12:59.24] decisions in your going to waste a bunch
[L418] [13:00.80] of time.
[L419] [13:02.08] And so, like you have to be comfortable
[L420] [13:03.52] with this idea of like, "I'm going to
[L421] [13:05.16] try some ideas, some of them are going
[L422] [13:06.68] to fail, some of them are going to
[L423] [13:07.76] succeed. When I look back
[L424] [13:09.20] retrospectively, the ones that have
[L425] [13:10.40] failed were effectively a waste of
[L426] [13:12.00] time."
[L427] [13:13.52] Um
[L428] [13:14.88] you know, and it might be the difference
[L429] [13:16.32] between a exceeded expectations and a
[L430] [13:18.32] met expectations,
[L431] [13:20.40] right? Like you don't want to drop below
[L432] [13:21.72] meets expectations, but like it might be
[L433] [13:23.16] the difference between an exceeded
[L434] [13:24.36] expectations and a meets expectations,
[L435] [13:25.92] and you have to be comfortable with the
[L436] [13:27.24] notion that
[L437] [13:29.56] you're going to bet five times, and the
[L438] [13:32.40] payout from one of them hitting is going
[L439] [13:34.28] to be way better than the grinding to
[L440] [13:37.68] get that exceeds every single time.
[L441] [13:40.20] Um
[L442] [13:41.56] and you know, I mean I I I think it's I
[L443] [13:42.96] think there's equally valid paths where
[L444] [13:44.28] you don't do that, right? And I think
[L445] [13:45.52] that you have to be the right kind of
[L446] [13:46.40] person who's willing to take that kind
[L447] [13:48.00] of chance.
[L448] [13:49.12] Um
[L449] [13:50.60] so and then that's not everybody, and
[L450] [13:52.52] that's okay.
[L451] [13:53.68] Um
[L452] [13:54.52] And I think the other side of it that I
[L453] [13:55.60] but I always remind everybody also
[L454] [13:56.80] though is like
[L455] [13:58.36] you know, people say things like that to
[L456] [13:59.32] me sometimes, and I'm like, "So, do you
[L457] [14:01.64] play Call of Duty?
[L458] [14:03.84] Do you watch Netflix?
[L459] [14:05.80] Do you watch YouTube?" You know, because
[L460] [14:08.20] like I'm pretty sure there's probably
[L461] [14:10.00] 10, 15, 20 hours in your week at least
[L462] [14:13.44] when you're doing something that's not
[L463] [14:14.80] work,
[L464] [14:15.96] right?
[L465] [14:17.24] And I can tell you in that time period,
[L466] [14:19.00] I wasn't doing anything except for this
[L467] [14:20.64] and work,
[L468] [14:21.96] right? And a little bit of family, like
[L469] [14:24.32] and sleeping.
[L470] [14:25.52] Right? And so like sometimes it's also
[L471] [14:27.32] about saying like, "Well, what are you
[L472] [14:28.64] willing to give up?"
[L473] [14:31.08] You know, to to have the space to do
[L474] [14:32.96] that.
[L475] [14:34.36] Um
[L476] [14:35.36] and you know, I'm not a big like I've I
[L477] [14:37.40] I I'm not a big like work all night kind
[L478] [14:38.96] of person, but like it does mean like
[L479] [14:40.44] maybe not going to watch YouTube for a
[L480] [14:41.84] while, maybe not going to watch, you
[L481] [14:43.32] know, sporting events for a while. That
[L482] [14:45.04] makes sense. And I mean, on that second
[L483] [14:46.48] point,
[L484] [14:47.64] in this case, I mean, it was such a
[L485] [14:51.28] the returns of this project were
[L486] [14:54.00] exponential. They're obscene. I mean, if
[L487] [14:56.68] you put in two times the the time for a
[L488] [15:00.28] year, but you you get 20 times the the
[L489] [15:03.92] impact. So,
[L490] [15:05.76] I I it just kind of makes sense in terms
[L491] [15:07.60] of investment of time.
[L492] [15:08.80] >> also I think I mean, I found personally
[L493] [15:10.76] that like
[L494] [15:12.40] the it was addictive,
[L495] [15:15.48] right? I mean, I think I benefited from
[L496] [15:16.88] two things. One is I really like to
[L497] [15:17.92] write code,
[L498] [15:19.44] right? Like I I I enjoy it as an
[L499] [15:21.72] activity.
[L500] [15:23.04] Um
[L501] [15:24.32] and uh uh and so like if I'm choosing
[L502] [15:26.76] between Netflix and coding, I'm actually
[L503] [15:28.16] pretty happy just coding.
[L504] [15:30.12] You know, so that's a benefit um for me.
[L505] [15:33.28] Um
[L506] [15:34.76] and then for me anyway, like once people
[L507] [15:36.48] start using it and they're excited about
[L508] [15:38.08] the project and they're putting issues
[L509] [15:39.56] on GitHub and all of this kind of stuff,
[L510] [15:41.60] like I'm just addicted to it.
[L511] [15:44.08] Like I just want to close that issue. I
[L512] [15:45.92] want to help that person out. I want to
[L513] [15:47.72] like I'm going to I'm going to go till
[L514] [15:49.68] I'm falling asleep on my laptop. Um
[L515] [15:53.20] and and that's just because that's I
[L516] [15:55.52] enjoy that. Like that's why I'm in the
[L517] [15:56.96] industry.
[L518] [15:58.08] Um
[L519] [15:58.64] so even in the moment I wasn't I mean,
[L520] [16:01.16] you're I was definitely not thinking
[L521] [16:02.92] about like, "Oh, here's this payout that
[L522] [16:04.24] I'm going to get for the rest of my
[L523] [16:05.12] career." Um
[L524] [16:07.24] I was definitely in the like "Wow, I
[L525] [16:09.68] just want to keep this thing going. I
[L526] [16:11.08] want to keep this, you know, I want to
[L527] [16:12.20] keep this rush going."
[L528] [16:13.76] >> Well, cuz it sounds like it it took a
[L529] [16:15.56] while for you guys to get buy-in from
[L530] [16:17.40] leadership.
[L531] [16:18.08] >> I think there was a solid 6 months of
[L532] [16:19.72] going from
[L533] [16:21.16] a very hacky prototype
[L534] [16:24.12] to something that like legitimately we
[L535] [16:27.08] thought somebody could take and use.
[L536] [16:30.04] And laying down the right kind of
[L537] [16:31.80] groundwork for that. Um
[L538] [16:34.96] you know, there's a lot of little
[L539] [16:36.16] details that you have to get right along
[L540] [16:37.88] the way. Um
[L541] [16:40.44] and and it's always nice also because,
[L542] [16:42.84] you know, a lot of
[L543] [16:44.36] uh
[L544] [16:45.88] a lot of the people who we brought in in
[L545] [16:47.92] the early days um had built similar
[L546] [16:51.04] systems before.
[L547] [16:52.92] And so they were having this
[L548] [16:53.80] opportunity, this kind of clean It's
[L549] [16:55.32] rare in your life as an engineer to get
[L550] [16:57.28] a clean room opportunity to rebuild
[L551] [16:59.36] something that you have ideas about how
[L552] [17:00.88] it could be better. It's like getting a
[L553] [17:02.48] second chance.
[L554] [17:03.88] You know, and and so that was also I
[L555] [17:06.92] think really attractive to people cuz
[L556] [17:08.44] it's suddenly like
[L557] [17:10.08] "Oh wow, like this is a clean room. We
[L558] [17:11.56] don't have any users right now.
[L559] [17:13.60] So like we don't have to be fixing bugs
[L560] [17:16.12] cuz some, you know, big company is who
[L561] [17:18.08] pays us a lot of money is asking for
[L562] [17:19.60] something or whatever. We've got this
[L563] [17:21.96] clean room time and
[L564] [17:24.56] we've all spent a lot of time thinking
[L565] [17:26.32] about what the system could look like.
[L566] [17:29.04] And so now we get to like go and just
[L567] [17:30.80] build the thing that we imagined.
[L568] [17:33.52] >> You mentioned that first point on hiding
[L569] [17:35.60] maybe 10% of your bandwidth from
[L570] [17:37.40] management. And I mean that's that's
[L571] [17:40.16] super interesting to me. What does that
[L572] [17:42.24] look like in practice?
[L573] [17:44.84] >> Um
[L574] [17:45.92] well, I mean I think that it what it
[L575] [17:47.28] means is that you should always have
[L576] [17:48.80] sort of a like a side project that you
[L577] [17:50.56] think is relevant.
[L578] [17:52.92] Right? Like you should always have
[L579] [17:54.44] something that is that nobody told you
[L580] [17:56.60] to do.
[L581] [17:58.08] But that you think is important that
[L582] [17:59.84] you're working on.
[L583] [18:01.80] >> I see. So it's kind of like I remember
[L584] [18:03.76] Google, I don't know if they still do
[L585] [18:04.88] this, but at the time there was 20%
[L586] [18:06.80] time.
[L587] [18:07.36] >> Yeah, that's similar to that kind of
[L588] [18:09.00] idea. Yeah. Yeah, exactly.
[L589] [18:11.28] >> Okay, so when you say when you say hide,
[L590] [18:13.72] you don't mean hide, you say
[L591] [18:15.52] manage expectations so that your manager
[L592] [18:18.68] is also okay with you working on another
[L593] [18:20.24] project.
[L594] [18:20.80] >> Oh no, I actually do mean hide, right?
[L595] [18:22.60] Like don't ask permission.
[L596] [18:24.32] Right?
[L597] [18:25.36] Like sooner or later you'll show it to
[L598] [18:26.72] them.
[L599] [18:27.92] But like it's pretty like you need a
[L600] [18:29.16] solid, I don't know, couple months or
[L601] [18:31.08] whatever to get to like a place where
[L602] [18:32.40] it's something you could show to
[L603] [18:33.48] somebody, right? And so like it's all
[L604] [18:36.36] about saying like I'm not going to ask
[L605] [18:37.76] permission.
[L606] [18:39.24] I'm going to go build something that I
[L607] [18:41.20] think is important and useful.
[L608] [18:43.36] And then obviously when it comes time to
[L609] [18:44.72] launch it or whatever or put it out
[L610] [18:46.84] there, like then you do have to ask
[L611] [18:48.56] permission.
[L612] [18:50.12] Right? Um
[L613] [18:52.60] and and so then yeah, you say like hey,
[L614] [18:54.60] I built this thing. But but you've had
[L615] [18:55.76] that time to like
[L616] [18:57.76] get it from cuz I I I mean I don't know.
[L617] [18:59.72] I feel like
[L618] [19:01.80] it's hard to articulate the value of
[L619] [19:04.04] something
[L620] [19:05.40] like in a doc or in a PowerPoint. It's
[L621] [19:08.04] way more effective if it's like a
[L622] [19:10.12] running thing that you can like somebody
[L623] [19:12.16] can interact with, right? So, getting
[L624] [19:14.48] that time to basically build it up into
[L625] [19:16.92] something that's real
[L626] [19:18.92] and could ship. Cuz also like in some
[L627] [19:20.84] sense your manager is always assessing
[L628] [19:22.20] like, well, should you
[L629] [19:24.60] spend your time on that or should you
[L630] [19:26.00] spend your time on this, right?
[L631] [19:28.72] And by building it, you kind of like
[L632] [19:30.40] force their hand.
[L633] [19:32.08] Cuz it's no longer like should you to
[L634] [19:33.56] spend time building this or should I you
[L635] [19:35.20] spend time building this? It's like,
[L636] [19:36.60] I've already built this.
[L637] [19:38.80] Like, do you want to ship it? And and
[L638] [19:40.76] that's in some ways a much easier
[L639] [19:42.24] decision. Like, I don't know about
[L640] [19:43.60] easier, but like it's like it's not an
[L641] [19:45.60] either/or, it suddenly becomes it's just
[L642] [19:47.16] sort of about like is your idea good?
[L643] [19:49.56] Right? Cuz the work is done.
[L644] [19:51.60] >> I mean, in the happy path, I feel like
[L645] [19:53.64] it's it's a great idea. You launch this
[L646] [19:56.00] thing, has impact, it's great. What
[L647] [19:58.48] about in the case that you work on this
[L648] [20:00.28] thing and you didn't tell anyone about
[L649] [20:01.52] it and then it
[L650] [20:03.40] no one cares when you launch it or it's
[L651] [20:05.04] not as good as we thought.
[L652] [20:06.96] >> Yeah, and and then like that's the flip
[L653] [20:09.04] side, right? Like
[L654] [20:11.20] you have to be comfortable I mean, as I
[L655] [20:13.16] said, like you have to be comfortable
[L656] [20:14.40] with that idea that
[L657] [20:16.44] um
[L658] [20:17.44] you know, you're going to waste some
[L659] [20:18.52] time. Uh and maybe it'll be a waste time
[L660] [20:22.20] in the sense of like, wow, I could have
[L661] [20:23.24] been like watching Netflix or, you know,
[L662] [20:25.16] whatever.
[L663] [20:26.48] Uh and I instead I wrote a bunch of code
[L664] [20:28.08] that nobody liked. Um it could be
[L665] [20:30.08] wasting time in the sense of like, wow,
[L666] [20:32.04] I could have, you know, could have
[L667] [20:32.96] gotten promoted. I could have done
[L668] [20:34.16] enough work to get promoted and I didn't
[L669] [20:36.64] because I thought this was the great
[L670] [20:38.08] idea that was going to get me over the
[L671] [20:39.32] hump, but it wasn't.
[L672] [20:41.00] Um
[L673] [20:42.36] and I think you just have to be
[L674] [20:44.04] comfortable with that.
[L675] [20:45.80] Like, you know, it's it's taking I mean,
[L676] [20:48.56] it is taking a risk. It's not unlike in
[L677] [20:50.60] some sense like
[L678] [20:52.04] doing a startup or something like that.
[L679] [20:53.56] It's taking a risk.
[L680] [20:55.08] So, you know, I think I think and you
[L681] [20:56.72] can't and you can't assume I think
[L682] [20:57.72] sometimes people are like go into any of
[L683] [20:59.84] these sorts of things and they're like,
[L684] [21:00.92] oh, I will have the idea and it will be
[L685] [21:02.44] amazing and then it will hockey stick
[L686] [21:03.80] and like
[L687] [21:05.60] I think if if that's your mindset when
[L688] [21:07.24] you go in, you're probably setting
[L689] [21:08.88] yourself up for some disappointment.
[L690] [21:11.04] You know, you have to go in with that
[L691] [21:11.96] mindset of like, I think this is good.
[L692] [21:13.36] I'm going to try, but I'm okay if I
[L693] [21:15.68] fail.
[L694] [21:16.68] Right? Like I know that I may I'm making
[L695] [21:18.16] an explicit choice here.
[L696] [21:20.20] >> I also imagine at at some point at the
[L697] [21:22.76] highest levels of uh engineering
[L698] [21:26.24] ladders, you you need to take that risk
[L699] [21:29.20] to get promoted to higher levels. For
[L700] [21:31.68] instance, like if you're a staff
[L701] [21:33.44] engineer or senior staff engineer and
[L702] [21:36.04] you ask your manager, how do I get
[L703] [21:37.88] promoted? They'll often tell you, you
[L704] [21:40.20] need to figure out what that project is
[L705] [21:42.40] cuz I don't I can't just hand this to
[L706] [21:44.28] you cuz it's starting to become more
[L707] [21:45.92] ambiguous.
[L708] [21:47.08] >> Oh, yeah, for sure.
[L709] [21:48.44] >> Yeah, I could totally see that this
[L710] [21:49.80] becomes a necessity at some point. Uh if
[L711] [21:51.96] you want to kind of grow and I mean this
[L712] [21:54.48] this project also got you promoted as
[L713] [21:56.16] well at Google, right? From uh from
[L714] [21:58.08] staff at some point.
[L715] [21:59.60] >> Uh yeah, I know I've certainly my career
[L716] [22:00.96] absolutely benefited from the success
[L717] [22:02.40] there. Absolutely, right? But uh and I
[L718] [22:04.64] think you're right that like there
[L719] [22:05.88] there's also this aspect of at a certain
[L720] [22:08.08] point like
[L721] [22:09.44] you're just expected to be the person
[L722] [22:11.28] who knows enough to come up with the
[L723] [22:12.56] really good ideas.
[L724] [22:14.40] A- and and that's just the expectation.
[L725] [22:15.84] Like it's no longer about like can you
[L726] [22:17.32] execute on the ideas that other people
[L727] [22:18.84] give you? You know, and and and that's a
[L728] [22:21.12] big that's a big part of it as well. And
[L729] [22:22.76] I think there's also like dispro- I
[L730] [22:24.08] mean, I was the other thing I tell
[L731] [22:25.44] people sometimes when um they're
[L732] [22:27.60] thinking about getting promoted is um
[L733] [22:31.32] if you create the idea yourself
[L734] [22:33.52] entirely, it's like blindingly obvious
[L735] [22:36.84] that it was you who did it.
[L736] [22:39.52] Right? If you succeed and have impact in
[L737] [22:42.36] something that is a bigger project or
[L738] [22:44.40] someone else's idea,
[L739] [22:46.24] um you can still have a very successful
[L740] [22:48.44] career, but it's a little bit harder for
[L741] [22:50.32] it to like be directly attributable to
[L742] [22:52.36] you.
[L743] [22:53.48] Right? Um
[L744] [22:55.20] and
[L745] [22:57.04] but again, I mean, I I think that again,
[L746] [22:59.16] it's it's a roll of the dice, right? And
[L747] [23:00.84] so like at some level like there're
[L748] [23:02.40] probably are people out there who've
[L749] [23:03.92] tried over and over and over again and
[L750] [23:05.92] just have never had the right idea.
[L751] [23:08.08] Right? Or just had the right idea at the
[L752] [23:09.56] wrong time. I mean, I think one of the
[L753] [23:10.88] other things that is interesting about
[L754] [23:12.84] innovation that is disruptive is that
[L755] [23:16.48] it's a combination of
[L756] [23:19.36] being the person who has the idea and
[L757] [23:21.84] being in a time in which the idea can
[L758] [23:24.52] take off.
[L759] [23:25.92] Right? And it's So, you could have the
[L760] [23:27.80] idea, but it could just be the wrong
[L761] [23:29.20] time.
[L762] [23:30.32] And it won't do the same and it won't go
[L763] [23:32.24] in the same direction.
[L764] [23:33.56] >> That point on promotions, I think I
[L765] [23:36.64] mean, if you create the scope, not only
[L766] [23:38.88] is it is it obvious that that the credit
[L767] [23:41.96] should go to you, but it also feels kind
[L768] [23:44.44] of permissionless. Like you don't need
[L769] [23:46.00] to wait for
[L770] [23:47.48] um I guess management or someone to give
[L771] [23:50.40] you the opportunity. You can kind of
[L772] [23:52.00] create it, and so you have a lot more
[L773] [23:53.92] control in that in that process. One
[L774] [23:56.44] thing on the the business strategy, I
[L775] [23:58.48] guess before we leave that for
[L776] [23:59.80] Kubernetes, is at that time, Borg to me
[L777] [24:03.56] felt like a competitive advantage for
[L778] [24:05.52] Google. Like some secret infrastructure
[L779] [24:07.56] sauce.
[L780] [24:08.84] I would have thought people would be
[L781] [24:10.96] kind of worried about
[L782] [24:12.96] giving away any part of that to the
[L783] [24:14.68] industry. So, what was the the thinking
[L784] [24:17.32] there? How how would you convince people
[L785] [24:19.20] that hey,
[L786] [24:20.36] it's okay?
[L787] [24:21.28] >> Yeah, I mean, I think that there was a
[L788] [24:22.68] little bit of that.
[L789] [24:24.08] Um
[L790] [24:24.76] and I think you know, to to be a little
[L791] [24:27.56] bit make it into a little bit of a joke
[L792] [24:29.16] or whatever, I sort of one of the things
[L793] [24:31.08] I said to people was, you know, it's not
[L794] [24:32.84] like you Men in Black flash people as
[L795] [24:34.96] they leave Google.
[L796] [24:36.56] Right? Like, you know, it's not like
[L797] [24:38.24] everybody comes to Google and they just
[L798] [24:39.28] stays there forever, right? And so, and
[L799] [24:41.28] in fact, as we talked to people at
[L800] [24:42.56] Facebook, as we talked to people at
[L801] [24:43.92] Twitter, we talked to people at other,
[L802] [24:46.36] you know, scale-out tech companies, like
[L803] [24:47.92] they were all building this stuff.
[L804] [24:49.72] The the this it wasn't really a secret.
[L805] [24:52.52] And there was also, I mean, like Mesos
[L806] [24:54.04] at the time was
[L807] [24:55.96] you know, not the same, but similar and
[L808] [24:58.24] like you could just see that there was
[L809] [25:00.64] going to be an open and and so in some
[L810] [25:02.60] sense you part of the argument was like
[L811] [25:04.12] look there's going to be an open source
[L812] [25:05.56] solution. Do you want it to be one that
[L813] [25:07.48] we can influence or not? It's not like
[L814] [25:09.88] do you want there to not to be an open
[L815] [25:11.12] source one or not? It's there's going to
[L816] [25:13.00] be an open source one.
[L817] [25:15.16] Do you want it to be ours or do you want
[L818] [25:16.96] it to be someone else's?
[L819] [25:19.48] And it's just reframing the choice,
[L820] [25:20.84] right? And making it clear that people
[L821] [25:22.48] understand that that is the choice,
[L822] [25:23.76] right? That that you don't get to choose
[L823] [25:25.52] the proprietary option because it's just
[L824] [25:27.32] not viable.
[L825] [25:28.96] >> When you were building that that MVP for
[L826] [25:31.52] the orchestrator,
[L827] [25:33.36] well, how did you decide cuz there were
[L828] [25:35.04] no customers or anything like that? So
[L829] [25:36.64] how did you decide this is the minimum
[L830] [25:39.00] set of features that we need for this to
[L831] [25:41.44] before we launch it?
[L832] [25:42.68] >> Sure. Well, I mean I think absolutely,
[L833] [25:44.44] you know, we benefit from the fact that
[L834] [25:45.84] there were three of us working on it,
[L835] [25:47.16] right? So Craig was a a great product
[L836] [25:49.28] manager and Joe was a great engineer and
[L837] [25:52.36] and and fantastic at API design. Um and
[L838] [25:56.44] and I could write code fast basically I
[L839] [25:58.72] think is sort of the the the you know,
[L840] [26:00.20] like if I if I had to sort of stereotype
[L841] [26:02.60] all of us, you know, that's the like
[L842] [26:05.68] Craig was the product business guy and
[L843] [26:07.36] Joe is the like I know how to design
[L844] [26:09.92] really good at design kind of person and
[L845] [26:11.96] and I was basically like I can hack
[L846] [26:14.24] prototypes like there's no wasted like
[L847] [26:15.60] no tomorrow.
[L848] [26:17.32] Um and
[L849] [26:20.20] and and I think we reflected a lot about
[L850] [26:22.36] our own experiences.
[L851] [26:24.56] Um and also we had seen the pain of
[L852] [26:28.64] people deploying um into traditional EVM
[L853] [26:33.04] infrastructure and so we had that that
[L854] [26:34.52] kind of knowledge of the pain that
[L855] [26:35.76] people are going through. And then
[L856] [26:37.96] you know, at the time there were people
[L857] [26:40.52] like Netflix who were talking about
[L858] [26:42.12] immutable infrastructure and they were
[L859] [26:43.56] kind of advancing some of the similar
[L860] [26:45.16] some similar concepts.
[L861] [26:47.00] And so there was also kind of like a
[L862] [26:50.00] broader movement happening that we were
[L863] [26:52.68] taking part in. Um and so
[L864] [26:55.96] you know, obviously there were no there
[L865] [26:57.12] were literally no customers, but in some
[L866] [26:59.08] sense there there were customers. They
[L867] [27:00.64] just weren't customers yet.
[L868] [27:02.96] Um so it's not like creating something
[L869] [27:05.32] brand new, I guess is in some sense.
[L870] [27:07.76] Right? Like Like I feel I really don't
[L871] [27:10.08] feel like Kubernetes was something that
[L872] [27:11.80] was brand new.
[L873] [27:13.28] I feel like it was a coalescing of a lot
[L874] [27:15.40] of ideas that were kind of circulating
[L875] [27:17.00] in the in the industry at the time. And
[L876] [27:19.44] it just became an anchor point and a
[L877] [27:20.80] really good expression of those ideas.
[L878] [27:23.36] >> So when you talk about I guess you wrote
[L879] [27:26.04] a lot of code quickly,
[L880] [27:28.04] it did you write most of the code I
[L881] [27:30.72] guess for this initial initial MVP?
[L882] [27:34.64] >> Yeah, I I don't know what the number is,
[L883] [27:36.32] but high 80 high 80s percentage maybe
[L884] [27:39.40] more of of the original code. Um and I
[L885] [27:43.20] think I'm still number I mean I haven't
[L886] [27:44.44] contributed significantly to Kubernetes
[L887] [27:46.28] in a while and I'm still I think number
[L888] [27:47.76] five on the all over overall
[L889] [27:50.32] contributor, you know, overall
[L890] [27:51.32] contributor list on the GitHub commits.
[L891] [27:53.48] And I was never I was number one for a
[L892] [27:54.80] long time.
[L893] [27:55.96] >> I mean after writing that much code for
[L894] [27:58.04] Kubernetes, which part of this system
[L895] [28:01.32] was the hardest to build?
[L896] [28:03.44] >> I I think I'm going to say like cuz I
[L897] [28:04.72] don't think any of the specific code was
[L898] [28:07.80] that hard. Um
[L899] [28:11.20] I think that the
[L900] [28:13.84] core the hard part was the decision that
[L901] [28:15.72] we made early on that it was going to be
[L902] [28:17.28] a really loosely coupled system.
[L903] [28:20.00] And so it's very
[L904] [28:22.80] um
[L905] [28:23.44] which is great for resiliency. Like we
[L906] [28:25.20] made this decision around very loose
[L907] [28:27.24] coupling, a lot of independent actors
[L908] [28:29.88] taking actions. There's all these
[L909] [28:31.12] control loops running all over the
[L910] [28:32.44] place.
[L911] [28:33.76] Which is really good for resiliency.
[L912] [28:35.88] Um
[L913] [28:36.92] but when things go wrong, it's really
[L914] [28:39.48] hard to figure out
[L915] [28:41.28] why they went wrong. Because you've got,
[L916] [28:43.76] you know, 15 different processes that
[L917] [28:45.64] are all having to work together to
[L918] [28:47.12] achieve an outcome. And so you can see
[L919] [28:49.16] that the outcome wasn't achieved.
[L920] [28:51.36] Right? But then you're like, okay, but
[L921] [28:53.24] like what happened?
[L922] [28:54.92] And now I have to sift through a bunch
[L923] [28:56.84] of different logs and a bunch of
[L924] [28:58.20] different operations of executables and
[L925] [29:00.72] sort of reconstruct in time what
[L926] [29:02.96] happened and and especially early on we
[L927] [29:04.84] didn't have very good
[L928] [29:06.60] we didn't have very much consistency
[L929] [29:07.92] around logging, we didn't have very good
[L930] [29:10.00] consistency about event like events and
[L931] [29:12.32] things like that. Um
[L932] [29:14.84] And so I think the hardest part and I
[L933] [29:16.68] mean it's the hardest part of anything I
[L934] [29:17.84] guess, but like it's when something went
[L935] [29:19.32] wrong figuring out like why it went
[L936] [29:21.20] wrong.
[L937] [29:22.16] >> Because your logs are all distributed
[L938] [29:23.68] everywhere and
[L939] [29:25.00] >> Yeah, and everything's out of time sync
[L940] [29:26.48] and I mean and hopefully you logged the
[L941] [29:27.88] right things, but a lot of time early on
[L942] [29:30.00] like you didn't log it. Like you know,
[L943] [29:32.60] and and and and because it's a
[L944] [29:34.68] interaction effect
[L945] [29:36.44] it's hard to reproduce.
[L946] [29:38.60] Um often times it's hard often times
[L947] [29:40.32] it's hard to reproduce the problem. Like
[L948] [29:41.72] if it's a problem reproduces easily then
[L949] [29:43.52] it's pretty easy to fix even if you
[L950] [29:44.96] don't have the logs because you just go
[L951] [29:46.32] and add the logs and then you do it
[L952] [29:48.36] again and you see what happens. Um
[L953] [29:52.00] But for problems that are transient
[L954] [29:54.72] uh that because of it's just, you know,
[L955] [29:56.80] race condition between two or three
[L956] [29:58.32] different things happening, you can go
[L957] [30:00.28] in and add the extra logs, but then you
[L958] [30:01.84] have to figure out how to make it
[L959] [30:03.00] happen.
[L960] [30:04.36] Right? Um and that's that can be pretty
[L961] [30:07.92] tricky. Um and also I mean I'll say the
[L962] [30:10.48] other thing is like we were all learning
[L963] [30:11.60] Go.
[L964] [30:12.56] So maybe the other thing was like
[L965] [30:13.64] there's some gotchas in Go lang and we
[L966] [30:15.64] were all kind of like learning all the
[L967] [30:17.60] gotchas on the fly.
[L968] [30:19.84] >> I would have thought there's something
[L969] [30:21.24] that's controlling everything, right?
[L970] [30:22.48] Like there's some leader or maybe some
[L971] [30:25.40] nodes that are looking at one of them to
[L972] [30:28.56] kind of coordinate everything. Like
[L973] [30:30.56] leader election, if the leader goes
[L974] [30:32.60] down, I would have thought would be some
[L975] [30:35.20] really challenging problem.
[L976] [30:37.76] >> Yeah, I mean well, I think what what the
[L977] [30:39.72] reason it wasn't that big a deal was
[L978] [30:41.36] because
[L979] [30:42.56] um
[L980] [30:43.72] we relied pretty exclusively on etcd to
[L981] [30:48.16] to do that for us.
[L982] [30:50.52] >> Also, etcd is another
[L983] [30:53.20] framework or open source?
[L984] [30:54.68] >> Uh yeah, etcd is an open source I mean
[L985] [30:56.76] it's kind of really part of
[L986] [30:59.20] Kubernetes now, but at the time it was a
[L987] [31:01.68] um
[L988] [31:02.28] it's a a raft raft-based consensus uh
[L989] [31:06.76] system key value store.
[L990] [31:09.00] Um and so it was a pre-existing piece of
[L991] [31:11.76] software that that CoreOS had written um
[L992] [31:15.56] that implemented the raft protocol cuz
[L993] [31:17.68] at the time like cuz Paxos is was the
[L994] [31:20.00] original for this and Paxos is really
[L995] [31:21.48] hard to implement cuz the algorithm is
[L996] [31:22.96] really complicated
[L997] [31:24.56] uh and nobody understands it. Well,
[L998] [31:25.88] probably somebody understands it, but
[L999] [31:27.48] not a lot of people understand it. So
[L1000] [31:29.28] then
[L1001] [31:30.40] but it's provable, right? Um
[L1002] [31:33.88] and then right around that time frame
[L1003] [31:36.60] people had come up with raft, which is a
[L1004] [31:39.80] provably correct consensus algorithm,
[L1005] [31:43.24] but it's way easier to implement. etcd
[L1006] [31:46.20] implemented the raft protocol and then
[L1007] [31:48.24] gave you this consensus reliable um
[L1008] [31:51.96] store so that uh
[L1009] [31:54.60] you could do um
[L1010] [31:57.12] uh it had you had multiple replicas and
[L1011] [31:59.12] it would do it would do the consensus
[L1012] [32:00.48] there and it doesn't do leader election
[L1013] [32:02.00] exactly, but it allows but it gives you
[L1014] [32:04.36] enough primitives that doing leader
[L1015] [32:06.56] election is relatively
[L1016] [32:09.24] um straight forward. Um
[L1017] [32:12.32] and and I guess I would also say that I
[L1018] [32:14.48] mean two things about that. One is we
[L1019] [32:15.80] decided to force all of the access
[L1020] [32:19.28] through an API server.
[L1021] [32:21.36] So no nobody had and this was actually
[L1022] [32:23.48] something I pushed really hard initially
[L1023] [32:26.00] um but we I think we had general
[L1024] [32:27.36] agreement, but I definitely pushed for
[L1025] [32:28.80] it um was that nobody got to use store.
[L1026] [32:31.48] Everything had to be remote store.
[L1027] [32:34.04] Like nobody got to write stuff to disk
[L1028] [32:36.00] themselves.
[L1029] [32:37.32] Every every piece of the system had to
[L1030] [32:40.00] use the API server and had to use etcd
[L1031] [32:42.84] behind the API server as the way that it
[L1032] [32:45.00] did any sort of persistence.
[L1033] [32:48.20] >> What's the main benefit of that?
[L1034] [32:49.96] >> The main benefit of that is that
[L1035] [32:51.24] everybody gets to restart all the time
[L1036] [32:53.32] and they just come up and they work. So
[L1037] [32:55.20] you don't have to worry about
[L1038] [32:56.12] corruptions, you don't have to worry
[L1039] [32:57.36] about schema changes, you don't have to
[L1040] [32:59.32] worry about any of the like everybody
[L1041] [33:01.20] was effectively stateless
[L1042] [33:03.12] except for the database. Like there was
[L1043] [33:05.16] there's the etcd consensus algorithm
[L1044] [33:07.28] database
[L1045] [33:08.40] and that's the only place where there
[L1046] [33:09.76] was state.
[L1047] [33:11.36] And and so as a result
[L1048] [33:13.64] um
[L1049] [33:14.64] the the whole system was just a lot
[L1050] [33:17.20] easier to um
[L1051] [33:19.16] to to make stable. Um
[L1052] [33:21.48] the the downside of it is it it leads to
[L1053] [33:23.44] this like loosely couple like loose
[L1054] [33:25.12] coupling, right? Where it's a bunch of
[L1055] [33:26.72] independent loops mediating everything
[L1056] [33:29.08] through this storage layer.
[L1057] [33:31.36] Um
[L1058] [33:32.64] and and which made the debugging part
[L1059] [33:34.28] harder.
[L1060] [33:34.88] >> Right. So like the those are the sort of
[L1061] [33:36.52] the trade-offs is like if you have a
[L1062] [33:37.88] complete log of like I'm in
[L1063] [33:40.08] you know, if you think of it as a state
[L1064] [33:41.28] machine, like it's much easier to
[L1065] [33:42.88] understand where you are
[L1066] [33:44.84] and where you got to
[L1067] [33:46.60] if you're in a state machine.
[L1068] [33:49.04] Um
[L1069] [33:49.96] but state machines are a nightmare to
[L1070] [33:51.44] make reliable.
[L1071] [33:54.16] And so like they're easy to they're easy
[L1072] [33:55.76] to debug, but they're hard to make
[L1073] [33:57.40] stable. Whereas the system we built was
[L1074] [33:59.44] like designed to be stable
[L1075] [34:01.52] but hard to debug.
[L1076] [34:03.24] The trouble with the state machine is a
[L1077] [34:04.52] state machine says the world looks like
[L1078] [34:06.96] this.
[L1079] [34:08.52] And unless you get it exactly right
[L1080] [34:11.20] sometimes the world looks like something
[L1081] [34:12.64] you didn't imagine.
[L1082] [34:14.48] And at that point you're kind of screwed
[L1083] [34:16.68] because like your state machine doesn't
[L1084] [34:18.24] know what to do.
[L1085] [34:19.68] Right? Whereas because we have these
[L1086] [34:22.36] control loops that were based on a
[L1087] [34:24.40] desired state and a current state and
[L1088] [34:26.44] trying to drive the current state to the
[L1089] [34:28.12] desired state
[L1090] [34:30.16] like no matter where you woke up and
[L1091] [34:31.72] found yourself,
[L1092] [34:33.28] you kind of knew where you were supposed
[L1093] [34:34.80] to drive to. And that And that And
[L1094] [34:36.64] that's the stable part. That's the
[L1095] [34:37.88] stable part of it is that like it didn't
[L1096] [34:40.40] really matter what what where the system
[L1097] [34:42.68] got itself.
[L1098] [34:44.68] It was always trying to drive towards uh
[L1099] [34:47.08] the the desired state. You know,
[L1100] [34:49.28] inspired honestly a lot by like control
[L1101] [34:51.00] theory from robotics, actually. Like
[L1102] [34:53.44] >> Oh, like uh PID.
[L1103] [34:54.80] >> Yeah, the same same idea, right? Like,
[L1104] [34:57.48] you know, you could imagine if you tried
[L1105] [34:58.76] to write a PID controller to balance a
[L1106] [35:00.40] beam with a bunch of if else loops, it
[L1107] [35:03.16] like it just doesn't work very well.
[L1108] [35:04.84] >> And that this kind of reminds me cuz I
[L1109] [35:06.52] was reading like in some of the design
[L1110] [35:08.48] uh like a large I guess it's a feature
[L1111] [35:10.48] of Kubernetes is that it's declarative
[L1112] [35:13.56] rather than imperative. So, you kind of
[L1113] [35:15.12] just say, "I want this to be true. I
[L1114] [35:17.40] don't care how you get there." instead
[L1115] [35:18.92] of saying, "Just do X, Y, and Z." Um I'm
[L1116] [35:22.24] curious like the pros and cons of that
[L1117] [35:25.00] that design decision.
[L1118] [35:26.64] >> Um well, yeah. I mean, and that was
[L1119] [35:28.24] something that was happening broadly in
[L1120] [35:29.56] the industry. Like, that's a part of the
[L1121] [35:31.44] whole like infrastructure as code
[L1122] [35:33.12] movement that was happening at the time.
[L1123] [35:35.36] Um so, we're not the only ones who said
[L1124] [35:37.16] that, but we definitely embraced it. Um
[L1125] [35:40.36] I you know, I mean, I think the benefit
[L1126] [35:42.20] is, you know, you have clarity about the
[L1127] [35:45.16] way you want the world to work.
[L1128] [35:47.12] Right? It's not Like, if you if you if
[L1129] [35:49.96] you execute a bunch of instructions,
[L1130] [35:52.24] start this, run that, do this, like
[L1131] [35:55.76] you've done a bunch of stuff in pursuit
[L1132] [35:58.24] of some objective.
[L1133] [36:01.04] But you never wrote down what the
[L1134] [36:02.24] objective was.
[L1135] [36:03.96] Right? There's no record of like what
[L1136] [36:05.52] you were trying to achieve. I'm trying
[L1137] [36:07.04] to create a website. Well, you didn't
[L1138] [36:08.16] write that down. You just took a bunch
[L1139] [36:09.48] of steps.
[L1140] [36:11.28] Right? With a declarative with a
[L1141] [36:13.00] declarative approach, you actually write
[L1142] [36:14.32] it down. You say like, "I'm trying to
[L1143] [36:15.84] create a reliable website, and here's
[L1144] [36:17.88] what a reliable website looks like."
[L1145] [36:20.00] "Hey system, could you take the steps to
[L1146] [36:22.72] get there?"
[L1147] [36:23.88] Right? And so, you have that record. Um
[L1148] [36:26.88] and it obviously makes it easier for
[L1149] [36:28.40] things to be self-healing because if
[L1150] [36:31.16] you've written it down, now I know where
[L1151] [36:33.44] I'm supposed to go back if like if I get
[L1152] [36:34.68] perturbed from that state, if something
[L1153] [36:36.24] fails, if something restarts, well, I
[L1154] [36:38.16] know where I'm supposed to go back to.
[L1155] [36:40.20] Um
[L1156] [36:41.44] and similarly, like it has ans- it has
[L1157] [36:44.76] side benefits of like once I write it
[L1158] [36:47.08] down, well, I can apply code review to
[L1159] [36:49.20] it.
[L1160] [36:50.08] I can apply unit tests to it.
[L1161] [36:52.32] Like there's a lot of like the the
[L1162] [36:53.96] mechanics of how we do software
[L1163] [36:55.48] development that apply once you write
[L1164] [36:57.72] down that declaration.
[L1165] [37:00.16] Um so like a lot of those are the
[L1166] [37:01.48] benefits. I think the downside is
[L1167] [37:02.96] probably just complexity.
[L1168] [37:05.48] Right?
[L1169] [37:06.52] You know, in comparison to go and click
[L1170] [37:08.04] click click through a wizard or
[L1171] [37:09.84] whatever, you know, in a GUI. Um
[L1172] [37:12.96] learning and you know, everybody
[L1173] [37:14.32] complains about the YAML and I have to
[L1174] [37:16.40] learn all this stuff and you know, like
[L1175] [37:19.24] it does introduce a
[L1176] [37:22.04] a learning curve.
[L1177] [37:23.60] Um now, I think fortunately at this
[L1178] [37:25.28] point there's enough educational
[L1179] [37:26.20] material out there that it's not and and
[L1180] [37:28.00] GenAI, too, for that matter, that it's
[L1181] [37:30.40] not that bad a learning curve.
[L1182] [37:32.52] Um but certainly in comparison to what
[L1183] [37:35.48] people have done before, that's probably
[L1184] [37:36.84] the biggest downside. But I don't know.
[L1185] [37:38.28] I think that the upsides are
[L1186] [37:40.04] like up here and the downsides are like
[L1187] [37:41.80] way down like there's there's not a lot
[L1188] [37:43.36] of downside.
[L1189] [37:45.08] >> I see. Yeah, I could also see that being
[L1190] [37:47.32] helpful for I guess if you want to
[L1191] [37:49.48] optimize anything under the hood cuz
[L1192] [37:51.80] you're just making a promise to people
[L1193] [37:53.56] that this is going to happen, but if you
[L1194] [37:55.92] want to do it in a more efficient way or
[L1195] [37:57.60] something like that, then I guess it
[L1196] [38:00.20] just gives you all the the power to do
[L1197] [38:02.04] so.
[L1198] [38:02.52] >> Yeah, well, I mean, then that does make
[L1199] [38:03.76] things like machines failing a lot
[L1200] [38:05.20] easier.
[L1201] [38:06.36] Right? Because people don't say run this
[L1202] [38:08.56] on this machine. They just say, "I want
[L1203] [38:10.76] three of this to be somewhere."
[L1204] [38:13.20] And if a machine fails, well, it just
[L1205] [38:15.20] moves somewhere else, right? Because the
[L1206] [38:16.84] application isn't tied cuz I can't In
[L1207] [38:19.32] some ways, I don't know your intent,
[L1208] [38:20.72] right? If you log into a machine and you
[L1209] [38:22.84] start a process on that machine,
[L1210] [38:25.72] is it because you wanted a process?
[L1211] [38:28.00] Or is it because you wanted a process on
[L1212] [38:29.68] that machine?
[L1213] [38:31.52] I don't know. You didn't tell me.
[L1214] [38:33.68] And so if that machine fails,
[L1215] [38:36.24] what should I do? Well, I don't know,
[L1216] [38:38.28] right? But if I But if I know you said,
[L1217] [38:40.16] "Hey, I just want three replicas."
[L1218] [38:41.96] Well, then I know it doesn't matter that
[L1219] [38:43.36] it's on that machine. It could be on a
[L1220] [38:44.92] different machine. You'd be just as
[L1221] [38:46.08] happy.
[L1222] [38:47.04] >> I want to shift a little bit to kind of
[L1223] [38:49.64] when Kubernetes was was scaling and it
[L1224] [38:53.68] sounds like a a large part of this was
[L1225] [38:55.44] getting buy-in from other companies and
[L1226] [38:57.44] other people.
[L1227] [38:58.72] And so, you know, how how did you get
[L1228] [39:01.12] the buy-in from I know OpenShift was an
[L1229] [39:04.40] important part of Yeah, Red Hat
[L1230] [39:07.12] um and other companies that that joined
[L1231] [39:09.16] on. Like, how did you sell those
[L1232] [39:10.44] companies that Kubernetes is what you
[L1233] [39:12.44] want to use?
[L1234] [39:14.16] >> Well, I think I think for a lot of them,
[L1235] [39:15.56] especially in the early days, it was
[L1236] [39:17.28] kind of that quote around uh
[L1237] [39:18.88] undifferentiated heavy lifting.
[L1238] [39:21.52] Right? Like, they had some other
[L1239] [39:22.80] objective. Like, OpenShift was trying to
[L1240] [39:24.40] build a platform as a service.
[L1241] [39:26.60] Um or, you know, they were
[L1242] [39:29.20] you know, a lot of our early users who
[L1243] [39:30.84] were also contributors, you know, they
[L1244] [39:32.60] were trying to build some sort of
[L1245] [39:33.56] reliable web service or something like
[L1246] [39:35.28] that, right? And so, it was like, "Well,
[L1247] [39:38.56] we're going to have to build this thing
[L1248] [39:39.64] anyway.
[L1249] [39:40.80] Why don't we all build it together?
[L1250] [39:42.84] And we don't really care cuz we don't
[L1251] [39:44.00] think that's our value. Like, our we
[L1252] [39:45.36] don't think our value is tied up in that
[L1253] [39:47.68] layer.
[L1254] [39:48.72] So, we'll go contribute to your thing
[L1255] [39:50.64] cuz we're going to get more value out of
[L1256] [39:52.24] the collective than out of trying to do
[L1257] [39:54.16] it ourselves."
[L1258] [39:55.72] Um
[L1259] [39:57.16] and and so for a lot of the early
[L1260] [39:58.48] partners, that was a big part of the
[L1261] [39:59.80] argument was was like,
[L1262] [40:02.24] "Hey, we'll let you in." And And part of
[L1263] [40:03.80] that is making sure that they understand
[L1264] [40:04.96] that they're going to like that they're
[L1265] [40:06.72] going to be equal partners.
[L1266] [40:08.60] Right? Where it's not like cuz it's it's
[L1267] [40:10.40] one thing to take a dependency on
[L1268] [40:11.64] something, but then you're kind of like
[L1269] [40:13.96] taking dependency on someone else's road
[L1270] [40:15.76] map.
[L1271] [40:17.40] And so, it was really important also to
[L1272] [40:19.56] say, "Hey, like
[L1273] [40:21.72] you can come take a dependency on us,
[L1274] [40:24.36] but also we'll give you a seat at the
[L1275] [40:26.32] design table. So, when you need new
[L1276] [40:27.88] features,
[L1277] [40:29.12] you can, you know, contribute those
[L1278] [40:30.76] features. And And here's what we're
[L1279] [40:32.16] trying to achieve. And And And it
[L1280] [40:33.76] matches up with your road map. And you
[L1281] [40:35.88] know, that kind of stuff." So, I think
[L1282] [40:37.68] that's how we we approached it. And
[L1283] [40:39.00] then,
[L1284] [40:39.80] uh over time, you know, people became
[L1285] [40:42.88] more and more interested in being part
[L1286] [40:44.40] of it because there was a growing
[L1287] [40:45.76] ecosystem.
[L1288] [40:47.04] So, when you look at like networking
[L1289] [40:48.32] providers or storage providers, you
[L1290] [40:50.76] know, as their users were starting to
[L1291] [40:52.48] become Kubernetes users,
[L1292] [40:54.48] um they were motivated to make sure that
[L1293] [40:56.76] their networking system worked well with
[L1294] [40:58.96] Kubernetes or their storage system
[L1295] [41:00.60] worked well with Kubernetes and things
[L1296] [41:02.20] like that. Um so, that was sort of a
[L1297] [41:03.80] secondary layer of partner discussions
[L1298] [41:05.44] that we had.
[L1299] [41:06.84] >> Right. And that's not downstream of
[L1300] [41:08.80] becoming the dominant player. And I
[L1301] [41:10.40] guess that's validating the open source
[L1302] [41:12.32] strategy, which is you become dominant,
[L1303] [41:14.64] everyone's kind of got a
[L1304] [41:16.44] um integrate with you and all of that.
[L1305] [41:18.56] How did you prevent Google from
[L1306] [41:20.48] dominating in the the road map or I
[L1307] [41:23.28] guess controlling what Kubernetes would
[L1308] [41:25.04] be, given that it started at Google,
[L1309] [41:27.96] funded largely by Google?
[L1310] [41:30.28] >> Yeah, I mean, I think that was really
[L1311] [41:31.28] important. Um and and I think it was a
[L1312] [41:33.04] critical part of gaining adoption,
[L1313] [41:35.36] right? Um
[L1314] [41:36.72] and and and becoming the industry
[L1315] [41:38.04] standard and was was giving it
[L1316] [41:40.60] independence. Um and I think, you know,
[L1317] [41:42.92] there's two pieces to that. The first is
[L1318] [41:45.40] um getting it to foundation. So, the
[L1319] [41:48.12] creation uh it was only a year in that
[L1320] [41:51.68] we created the Cloud Native Compute
[L1321] [41:53.28] Foundation, that we donated all of
[L1322] [41:55.64] Kubernetes to the Cloud Native Compute
[L1323] [41:57.16] Foundation. Um and so, getting the
[L1324] [41:59.84] project, the logos, all of the legal
[L1325] [42:03.32] stuff, trademarks, all of that stuff,
[L1326] [42:06.00] um
[L1327] [42:07.04] into a independent software foundation
[L1328] [42:09.48] um with the Linux Foundation was
[L1329] [42:11.44] critical, right? Cuz cuz it's hard to
[L1330] [42:13.84] partner if you know, somebody else has
[L1331] [42:15.44] trademarks on the Kubernetes logo or
[L1332] [42:17.04] whatever.
[L1333] [42:18.08] Um
[L1334] [42:19.80] and then I think the other piece that
[L1335] [42:22.00] was important that came a little bit
[L1336] [42:23.32] later um
[L1337] [42:24.96] was writing down the governance rules.
[L1338] [42:27.88] So, you know, for the first time for
[L1339] [42:32.08] first for a few years, Kubernetes didn't
[L1340] [42:34.88] have any really governance rules written
[L1341] [42:36.60] down.
[L1342] [42:37.64] Um it was a mistake I would say, right?
[L1343] [42:39.44] Like we didn't realize how
[L1344] [42:41.80] it was really it was something we should
[L1345] [42:43.04] have done earlier, but we didn't. Um
[L1346] [42:46.48] and so we sat down in 2016 to write the
[L1347] [42:50.88] governance rules
[L1348] [42:52.72] um
[L1349] [42:53.52] and I think all of us were aligned and
[L1350] [42:56.60] on this idea that we didn't want any one
[L1351] [42:59.24] company to be able to take control of
[L1352] [43:00.88] the community.
[L1353] [43:02.56] Um and we really built the community and
[L1354] [43:05.52] the govern the rules of governance to be
[L1355] [43:07.64] democratic. Um
[L1356] [43:10.04] you know, we never I mean I think that's
[L1357] [43:11.56] an aesthetic from Craig and Joe and I.
[L1358] [43:13.12] We never set out to be like a benevolent
[L1359] [43:14.68] dictator for life style project. We
[L1360] [43:16.84] always set out to be a distributed
[L1361] [43:19.52] uh you know, distributed ownership
[L1362] [43:21.52] democratic kind of project. Um and we
[L1363] [43:24.96] codified we codified a lot of that into
[L1364] [43:27.36] the governance docs that you know,
[L1365] [43:29.16] continue to this day. So, um I think
[L1366] [43:31.60] both those things together really helped
[L1367] [43:34.16] make sure that it was a an industry
[L1368] [43:36.08] standard not a and not any one
[L1369] [43:37.76] particular company standard.
[L1370] [43:40.00] But also I think were critical to its
[L1371] [43:41.28] success. Like I think they're they're
[L1372] [43:43.16] they're jewels of each other, right?
[L1373] [43:44.52] Like you can't have one without the
[L1374] [43:45.68] other.
[L1375] [43:46.40] >> People wouldn't have come on if they
[L1376] [43:48.72] didn't see that it was uh governed well
[L1377] [43:51.36] and open.
[L1378] [43:52.24] >> Yeah, I mean cuz obviously like you're
[L1379] [43:53.56] thinking about adopting it or you're
[L1380] [43:54.88] thinking about you know, putting it in
[L1381] [43:57.08] your service like the thing the thing
[L1382] [43:58.64] you're worried about is like whose road
[L1383] [44:00.56] map am I betting on?
[L1384] [44:02.16] >> Um when you said governance, is that I
[L1385] [44:04.80] mean mean, that literally like uh like
[L1386] [44:06.52] when I think of government, like there's
[L1387] [44:07.84] a constitution somewhere?
[L1388] [44:09.76] >> That's literally what we wrote.
[L1389] [44:11.36] >> Did you write that yourself or is that
[L1390] [44:12.52] something that like lawyers do or
[L1391] [44:14.44] >> Uh no, no, we wrote it ourselves, yeah.
[L1392] [44:16.48] Um
[L1393] [44:18.12] in the span of about uh it was a couple
[L1394] [44:20.92] of free couple free fairly intense
[L1395] [44:22.64] meetings amongst amongst like six or
[L1396] [44:24.44] seven of us. We got together um
[L1397] [44:27.44] and uh
[L1398] [44:29.28] and just kind of talked it through.
[L1399] [44:31.08] And and and looked at a bunch of other
[L1400] [44:34.68] communities and kind of like what had
[L1401] [44:37.48] worked, what had not worked, what were
[L1402] [44:39.24] we worried about, what were we trying to
[L1403] [44:41.16] achieve.
[L1404] [44:42.52] Um some of it was codifying stuff that
[L1405] [44:44.68] already existed.
[L1406] [44:46.48] Um so we had some loose organization
[L1407] [44:49.00] stuff that already existed in sort of a
[L1408] [44:51.24] de facto way, but didn't it exist in a
[L1409] [44:53.76] explicit way.
[L1410] [44:55.20] Um some of it was, you know, uh we we
[L1411] [44:58.68] created the steering committee
[L1412] [45:00.88] uh that had never existed before, right?
[L1413] [45:03.04] And we just basically uh and we were
[L1414] [45:05.88] lucky, I think, that we were able to
[L1415] [45:07.76] gather
[L1416] [45:09.12] uh so the people that came together, we
[L1417] [45:10.44] called it the bootstrap committee.
[L1418] [45:12.52] Um
[L1419] [45:13.88] you know, we we were lucky in the sense
[L1420] [45:15.52] that we had enough people
[L1421] [45:18.04] in who kind of were
[L1422] [45:20.16] not who who the entire community would
[L1423] [45:22.84] look at as being leaders.
[L1424] [45:25.76] And and and they worked we weren't
[L1425] [45:27.44] fighting with each other, you know, we
[L1426] [45:28.88] weren't in fighting, so we were all kind
[L1427] [45:30.20] of aligned. And we kind of got
[L1428] [45:32.04] everybody. So we didn't have to be like,
[L1429] [45:33.76] oh, you know, we grabbed this side and
[L1430] [45:35.64] not that side. We kind of we grabbed we
[L1431] [45:37.60] were able in
[L1432] [45:38.96] it was like seven people, I think, seven
[L1433] [45:40.28] or eight people. Um
[L1434] [45:42.04] we were able to pull together
[L1435] [45:44.68] a group of people that really
[L1436] [45:46.04] represented everybody and that everybody
[L1437] [45:48.00] kind of all respected each other and
[L1438] [45:50.08] respected each other as leaders in the
[L1439] [45:51.52] space. Um and a lot of credit there, I
[L1440] [45:53.80] think, goes to I mean, everybody deserve
[L1441] [45:55.56] who is involved deserves a lot of
[L1442] [45:56.76] credit, but um
[L1443] [45:58.56] Sarah Novotny, who was the um
[L1444] [46:01.36] uh our community leader at the time
[L1445] [46:03.48] deserves I think a ton of credit for
[L1446] [46:05.08] bringing that bringing that thing
[L1447] [46:06.68] together.
[L1448] [46:07.64] >> When you look back on on Kubernetes, cuz
[L1449] [46:11.52] with an open source project, there's
[L1450] [46:13.52] obviously the the read aspect, which is
[L1451] [46:15.84] everyone can use and duplicate this code
[L1452] [46:18.68] and execute it. But there's also I guess
[L1453] [46:21.00] the writing part, which is people making
[L1454] [46:22.84] contributions.
[L1455] [46:24.40] What percent of the contributions
[L1456] [46:25.80] actually come from the community and
[L1457] [46:27.48] what percent is actually just the main
[L1458] [46:30.16] stakeholder companies just putting in
[L1459] [46:32.16] their code?
[L1460] [46:33.60] >> Um yeah, I don't have the specific
[L1461] [46:35.04] numbers for Kubernetes, but my
[L1462] [46:36.24] experience in open source says it's like
[L1463] [46:38.40] 80 to 80 90% the core contributors.
[L1464] [46:41.96] And like less than 10%
[L1465] [46:44.80] other people. It It's It's It's hard I
[L1466] [46:47.52] think in general. It's really hard to
[L1467] [46:49.00] get people to contribute. Um part of it
[L1468] [46:52.72] is companies, honestly, right? Like you
[L1469] [46:55.12] know, companies like Microsoft, uh
[L1470] [46:57.56] we make a commitment to contributing to
[L1471] [47:00.24] open source. And so, you know, we at a
[L1472] [47:02.32] leadership level, we've decided that
[L1473] [47:04.16] this is something that we want to invest
[L1474] [47:05.56] in.
[L1475] [47:06.36] Um and so we're willing to have teams of
[L1476] [47:08.08] people who specialize in working in
[L1477] [47:10.20] upstream open source projects.
[L1478] [47:12.04] Um
[L1479] [47:13.00] but for a lot of users of Kubernetes,
[L1480] [47:15.48] you know, they're a retailer or they're
[L1481] [47:17.08] a banking industry or they're like
[L1482] [47:19.76] it's tech isn't their core thing that
[L1483] [47:21.64] they're doing. Tech is a means to an end
[L1484] [47:23.88] to deliver an app for their user. And in
[L1485] [47:26.16] that world, it's pretty hard to justify
[L1486] [47:29.04] well, I'm going to take
[L1487] [47:30.56] 10% of my people and I'm just going to
[L1488] [47:32.12] do upstream open source contributions.
[L1489] [47:34.96] Right? Um and especially if the
[L1490] [47:37.08] leadership is like not a technical
[L1491] [47:39.76] leadership, and so they didn't
[L1492] [47:41.00] necessarily grow up in those
[L1493] [47:42.12] communities. And if you grow up in
[L1494] [47:43.28] finance, it's hard to explain like
[L1495] [47:45.32] what's the value of contributing to the
[L1496] [47:47.40] I mean, the value of taking the open
[L1497] [47:48.96] source is very clear, right? It's free.
[L1498] [47:51.32] Um but the value of contributing back,
[L1499] [47:53.96] it's harder to explain. And
[L1500] [47:55.76] um or legally, like I've we ran into
[L1501] [47:58.04] people even today. It's getting better I
[L1502] [48:00.12] think but like even today I've run into
[L1503] [48:01.96] people who say like we would really love
[L1504] [48:03.60] to contribute.
[L1505] [48:05.00] Our engineering leadership is aligned
[L1506] [48:07.28] that we would want to contribute. But
[L1507] [48:09.88] our legal team is worried that if we
[L1508] [48:11.76] contribute we'll be liable if we
[L1509] [48:13.56] introduce bugs.
[L1510] [48:15.96] Right? So like if
[L1511] [48:17.52] >> Would someone sue them or?
[L1512] [48:18.84] >> Yeah, I think that's what they're
[L1513] [48:19.60] worried about. I I don't it doesn't hold
[L1514] [48:21.56] water legally and I think the Linux
[L1515] [48:23.20] Foundation can give you plenty of like
[L1516] [48:26.12] case law and things like that to show
[L1517] [48:27.88] why it doesn't hold water.
[L1518] [48:29.84] Um
[L1519] [48:30.96] but sometimes that's enough to block
[L1520] [48:34.00] uh
[L1521] [48:34.72] someone from contributing.
[L1522] [48:36.68] Okay?
[L1523] [48:37.08] >> I I never thought someone would get sued
[L1524] [48:39.52] for adding a bug. I mean everyone adds
[L1525] [48:42.00] bugs on accident.
[L1526] [48:44.36] >> Well, but I mean but on the other hand
[L1527] [48:46.00] like if you write a proprietary piece of
[L1528] [48:47.76] software and you sell it to somebody and
[L1529] [48:49.16] it has a bug and it causes your house to
[L1530] [48:50.76] burn down. Like you can imagine you're
[L1531] [48:53.08] going to sue the you're going to sue the
[L1532] [48:54.32] people, right? So like
[L1533] [48:56.08] it is sort of a legit worry at some
[L1534] [48:58.24] level of like if I wrote the JPEG open
[L1535] [49:01.08] source JPEG library that ended up in the
[L1536] [49:02.84] smoke detector that caused the house
[L1537] [49:04.36] Yeah, like
[L1538] [49:06.00] you can sort of imagine the chain of
[L1539] [49:07.76] logic that gets you there. I don't think
[L1540] [49:09.12] it's true. I don't think it would hold
[L1541] [49:10.64] up. I think a lot of the licenses, you
[L1542] [49:12.84] know, a lot of the
[L1543] [49:14.24] open source licenses include
[L1544] [49:16.00] indemnification language that basically
[L1545] [49:18.52] says
[L1546] [49:19.60] if you use this you're using it under
[L1547] [49:21.40] your own risk and like you can't sue us
[L1548] [49:23.36] if it burns down your house. Um
[L1549] [49:26.28] but
[L1550] [49:27.52] I think that that's a worry for I mean
[L1551] [49:29.12] what I've heard No, I don't think. I've
[L1552] [49:30.24] heard from people that that that that
[L1553] [49:32.24] their companies do have that worry. Um
[L1554] [49:34.92] and again in some sense it's because
[L1555] [49:36.20] they're like well, what's the value?
[L1556] [49:39.32] If I see this potential risk and I don't
[L1557] [49:41.32] necessarily see the value. And I mean
[L1558] [49:43.24] and like also like again if it's not a
[L1559] [49:44.80] core thing, if you're not a tech
[L1560] [49:46.32] company,
[L1561] [49:47.64] you know, is that developer really
[L1562] [49:49.12] capable of like arguing with legal
[L1563] [49:51.60] arguing with legal about what you can
[L1564] [49:53.40] and can't do. Yeah, probably not, right?
[L1565] [49:55.36] Like they're probably just going to fade
[L1566] [49:56.36] away, right?
[L1567] [49:57.72] Um so, you know, there's that aspect
[L1568] [50:00.20] too.
[L1569] [50:01.24] >> I remember this is many years ago, I
[L1570] [50:04.16] read this blog post that OpenAI put out
[L1571] [50:06.52] before I think OpenAI was kind of huge
[L1572] [50:09.36] and it says, "Here's how we scaled
[L1573] [50:11.20] Kubernetes to 7,500 nodes or something
[L1574] [50:14.72] crazy." I forgot exactly
[L1575] [50:15.60] >> On ours, yeah.
[L1576] [50:16.80] >> Yeah, yeah.
[L1577] [50:18.32] And so, I I I want to know um you know,
[L1578] [50:21.88] there's this new
[L1579] [50:23.52] these new workloads coming in for AI.
[L1580] [50:25.72] There's training, which is this huge I
[L1581] [50:29.00] guess all at once workload and then
[L1582] [50:30.96] there's inference, which is latency
[L1583] [50:32.72] sensitive and
[L1584] [50:34.36] you kind of need it to to come out
[L1585] [50:35.92] instantly. I guess how does how has
[L1586] [50:38.44] Kubernetes adjusted over the years to
[L1587] [50:40.84] handle these kinds of workloads?
[L1588] [50:43.60] >> Yeah, I mean, I remember when you know,
[L1589] [50:45.28] like we couldn't really handle more than
[L1590] [50:47.12] about 100 uh more than about 100 nodes.
[L1591] [50:49.76] So,
[L1592] [50:51.12] uh it's definitely been a lot of
[L1593] [50:52.88] optimization in the in the core systems
[L1594] [50:56.00] and there's places where the
[L1595] [50:58.08] APIs were pretty noisy.
[L1596] [51:00.24] Um and we needed to reduce the noise
[L1597] [51:04.28] level or we needed to extract
[L1598] [51:07.28] components into in another component so
[L1599] [51:09.12] that you could scale etcd in particular
[L1600] [51:10.80] actually is one of the could be the main
[L1601] [51:12.68] bottleneck to that kind of scale. And
[L1602] [51:14.76] so, figuring out how to run etcd really
[L1603] [51:16.56] well is a core part of figuring out how
[L1604] [51:18.88] to run Kubernetes really well at scale.
[L1605] [51:21.64] Um
[L1606] [51:23.44] I I mean, I don't think it's that
[L1607] [51:24.40] different than like learning how to run
[L1608] [51:25.56] a database or anything else like that at
[L1609] [51:27.04] scale. Like large scale is just weird
[L1610] [51:29.12] and you just have to
[L1611] [51:31.16] you know, run it, see where it breaks,
[L1612] [51:33.92] figure out how to fix it, or well, rinse
[L1613] [51:36.36] and repeat, you know. Um
[L1614] [51:39.20] And uh I do think what's interesting is
[L1615] [51:41.96] that while, you know, AI training as an
[L1616] [51:44.44] example is is a really large large
[L1617] [51:46.84] cluster or scale kind of thing. Um
[L1618] [51:50.48] you know, I think by virtue of being in
[L1619] [51:51.56] the cloud, a lot of our users actually
[L1620] [51:53.44] have much much smaller clusters.
[L1621] [51:55.60] But lots of them.
[L1622] [51:57.20] Right? So, hundreds or thousands of
[L1623] [51:59.24] clusters where each cluster itself is a
[L1624] [52:01.20] little bit smaller.
[L1625] [52:02.68] Um and I think that's not something we
[L1626] [52:04.84] anticipated cuz we came from a world of
[L1627] [52:06.72] like physical data centers where
[L1628] [52:09.68] you know, you only want one because like
[L1629] [52:11.40] you don't want to have to set it up a
[L1630] [52:12.44] bunch of times, right? You just want to
[L1631] [52:13.92] set one up for the entire data center,
[L1632] [52:15.48] call it a day. Um but because of the
[L1633] [52:17.88] cloud, because AKS you know, you press a
[L1634] [52:20.28] button
[L1635] [52:21.32] pops up in 2 minutes, right? Like it's
[L1636] [52:23.28] really easy to get yourself a cluster.
[L1637] [52:25.08] So, people create lots of clusters. Um
[L1638] [52:28.24] and and so I think we've also invested a
[L1639] [52:30.28] lot in the Kubernetes community and in
[L1640] [52:32.48] Azure as well on um managing lots of
[L1641] [52:36.32] clusters. How do I manage clusters at
[L1642] [52:38.40] scale? Um
[L1643] [52:40.08] you know, I think one of the jokes we
[L1644] [52:41.76] sort of like we spent a lot of time
[L1645] [52:43.72] talking about containers as replacing
[L1646] [52:45.44] snowflake servers.
[L1647] [52:47.44] Not snowflake the company, but like you
[L1648] [52:49.00] know, specially handcrafted servers.
[L1649] [52:52.24] Um
[L1650] [52:53.68] and now we just have a bunch of
[L1651] [52:55.20] snowflake clusters. So, the VMs all look
[L1652] [52:57.32] the same, but the clusters are all
[L1653] [52:58.72] weird. So, like we have to
[L1654] [53:00.28] provide people with tools to make sure
[L1655] [53:01.80] that the monitoring software is the same
[L1656] [53:03.20] on all of them and that the you know,
[L1657] [53:05.24] all of the Kubernetes versions are the
[L1658] [53:06.60] same and like you know, all this admin
[L1659] [53:09.24] users are the same and like all this
[L1660] [53:10.92] kind of stuff, right?
[L1661] [53:12.36] Um so, that's another aspect of scale
[L1662] [53:14.24] out that I think we didn't anticipate
[L1663] [53:15.88] that we had to go and and build, which
[L1664] [53:18.00] is num number of clusters as opposed to
[L1665] [53:20.52] size of cluster.
[L1666] [53:22.04] >> I always hear in the news that I mean,
[L1667] [53:24.32] this the anticipated scale is even
[L1668] [53:27.04] higher than today's unprecedented scale.
[L1669] [53:30.36] And I see people are purchasing GPUs
[L1670] [53:33.72] like crazy.
[L1671] [53:35.20] I'm curious, is there any upper bound
[L1672] [53:37.04] where Kubernetes just
[L1673] [53:39.08] it cannot handle that that um
[L1674] [53:42.32] that load? Like, let's say you you 10x
[L1675] [53:44.76] it from where it is today.
[L1676] [53:46.80] Is it Is it going to break down at some
[L1677] [53:49.20] point and you need something more
[L1678] [53:50.24] custom?
[L1679] [53:51.28] >> Uh well, I mean, I think it all comes
[L1680] [53:52.60] down It all comes back to the to the to
[L1681] [53:54.76] the storage layer that cuz everything
[L1682] [53:57.00] again cuz there was this design decision
[L1683] [53:59.36] that everything routes around the um
[L1684] [54:02.68] the storage layer.
[L1685] [54:04.32] Um everything else is basically
[L1686] [54:06.60] horizontally scalable. So, you you have
[L1687] [54:09.56] more API requests coming in from more
[L1688] [54:11.20] nodes, well, you just need more API
[L1689] [54:12.56] servers.
[L1690] [54:13.64] Um you know, you want to do scheduling
[L1691] [54:15.72] faster, well, you need to just have more
[L1692] [54:18.24] schedulers.
[L1693] [54:19.36] Um
[L1694] [54:21.20] so everything else more or less you can
[L1695] [54:22.88] just horizontally scale out.
[L1696] [54:25.04] Um
[L1697] [54:26.48] it's the it's it's the storage layer
[L1698] [54:28.48] that is the is the the bottleneck. Um
[L1699] [54:31.76] and that's where the work comes. And so,
[L1700] [54:33.32] you want to say go 10x up, well, you're
[L1701] [54:34.80] going to have to probably figure out um
[L1702] [54:37.84] if you can make etcd scale that way or
[L1703] [54:39.68] if you need to replace etcd with
[L1704] [54:41.08] something else that has the same
[L1705] [54:42.04] characteristics but can operate at
[L1706] [54:43.96] scale. Um
[L1707] [54:45.84] So, so I don't think there's anything
[L1708] [54:47.20] like inherent in the design that would
[L1709] [54:49.72] prevent it. Um but obviously
[L1710] [54:52.64] you know, there's a famous quote that
[L1711] [54:54.68] that every time you change an order of
[L1712] [54:56.20] magnitude, the problem moves. Um and so,
[L1713] [54:58.72] I think that's really true. Is every
[L1714] [55:00.08] time you increase by an order of
[L1715] [55:01.04] magnitude, what you thought was the main
[L1716] [55:02.96] problem is going to become easy and then
[L1717] [55:05.60] like the problem moves somewhere else.
[L1718] [55:07.64] So, you were never constrained, now
[L1719] [55:08.92] you're CPU constrained. You were never
[L1720] [55:10.20] constrained, now you're network
[L1721] [55:11.40] constrained.
[L1722] [55:12.24] >> Yeah, that'll be cool to watch how I
[L1723] [55:14.00] mean, cuz it seems like everyone wants
[L1724] [55:15.64] to
[L1725] [55:16.24] >> Yeah, I think it's definitely it's
[L1726] [55:17.20] definitely the case that people continue
[L1727] [55:18.44] to try and push the limits of scale. Um
[L1728] [55:21.32] and uh
[L1729] [55:23.20] but I think like anything else, like
[L1730] [55:24.68] when there's motivation
[L1731] [55:26.40] people go and figure it out.
[L1732] [55:28.36] All right, as long as there's not
[L1733] [55:29.24] something inherent in the design.
[L1734] [55:31.20] >> But the last part of this conversation,
[L1735] [55:32.56] I just wanted to reflect over your
[L1736] [55:34.56] career a a bit and maybe ask you a few
[L1737] [55:36.40] questions about things, and
[L1738] [55:39.16] uh you mentioned that you had a PhD in
[L1739] [55:40.84] robotics, and I hear a lot of people say
[L1740] [55:43.56] they don't recommend PhDs. Some people
[L1741] [55:45.52] do. I'm curious what your take on on
[L1742] [55:47.88] getting a PhD is.
[L1743] [55:49.12] >> Yeah, that's probably like like if I had
[L1744] [55:51.04] to have a top 10 questions or top five
[L1745] [55:52.88] questions that people ask me, uh that's
[L1746] [55:54.92] definitely in the top five top 10
[L1747] [55:56.32] questions. Um and I guess I'll I'll I'll
[L1748] [55:59.32] answer it with two different stories.
[L1749] [56:01.60] Um
[L1750] [56:02.32] one story is that uh
[L1751] [56:05.04] at one point in my career I ran into a
[L1752] [56:08.12] guy at same company, this guy who I went
[L1753] [56:10.88] to undergrad with.
[L1754] [56:12.52] Um and he'd gone off and done startups,
[L1755] [56:15.64] and you know, done the tech industry
[L1756] [56:17.56] thing, and ended up in the same company
[L1757] [56:19.44] that I was working at. And I'd gone off
[L1758] [56:21.16] and done my PhD, and come back into the
[L1759] [56:23.20] industry, and and we were the exact same
[L1760] [56:25.20] level. We graduated the exact same year,
[L1761] [56:27.12] same degree, and we were at the exact
[L1762] [56:29.08] same level in this company. And so I
[L1763] [56:31.68] guess that's one way of me saying like,
[L1764] [56:33.40] "Eh?"
[L1765] [56:34.88] You know, like it probably doesn't
[L1766] [56:36.16] matter. It probably doesn't matter one
[L1767] [56:37.64] way or the other. Um
[L1768] [56:40.92] but I'll also turn it around and say,
[L1769] [56:43.24] "A, I had a lot of fun."
[L1770] [56:45.24] Right? So like I had a lot of fun doing
[L1771] [56:47.12] a PhD in robotics. So
[L1772] [56:49.24] that's worth it to me. Um
[L1773] [56:52.44] and then two, I think I learned a lot
[L1774] [56:55.52] about how to um I think from the PhD and
[L1775] [56:59.28] my PhD advisor, I learned a lot about
[L1776] [57:01.16] how to write and put my ideas forth in
[L1777] [57:04.20] both written and presentation form.
[L1778] [57:07.68] That you don't necessarily learn in the
[L1779] [57:09.00] industry.
[L1780] [57:10.20] Um and I think that benefited me. I
[L1781] [57:11.92] think I benefited my ability to, you
[L1782] [57:14.52] know, argue We talked about that
[L1783] [57:15.92] six-month period where we were arguing
[L1784] [57:17.60] for like why we should be allowed to
[L1785] [57:19.36] open source this thing.
[L1786] [57:20.88] Um
[L1787] [57:21.44] I think the thing The skills I learned
[L1788] [57:22.88] in terms of presentation and in terms of
[L1789] [57:24.60] writing
[L1790] [57:25.72] um benefited me uh during that time. Uh
[L1791] [57:29.60] and have continued to benefit me.
[L1792] [57:31.72] Um
[L1793] [57:32.52] and and then I think
[L1794] [57:34.36] you know, when I went out as a professor
[L1795] [57:35.76] for a couple of years, um teaching CS
[L1796] [57:38.76] 101 and having to like explain stuff to
[L1797] [57:41.12] students who didn't really know anything
[L1798] [57:42.72] about computers,
[L1799] [57:44.04] um
[L1800] [57:45.40] I think really helped me organize the
[L1801] [57:48.12] the in the initial parts of the
[L1802] [57:50.20] Kubernetes project so that somebody
[L1803] [57:51.44] could learn about Kubernetes cuz people
[L1804] [57:52.76] were coming in and being like, "What is
[L1805] [57:54.16] a container? What is orchestration? How
[L1806] [57:55.64] do I do this?" Like there's a lot of
[L1807] [57:57.36] like just teaching that you had to do.
[L1808] [57:59.44] And and I think that experience as a
[L1809] [58:00.96] professor thinking about how do I teach
[L1810] [58:03.08] students something really helped me do a
[L1811] [58:05.84] good job um
[L1812] [58:07.48] with you know, teaching Kubernetes to
[L1813] [58:09.32] people. Um and so I think those things
[L1814] [58:11.88] were really beneficial. And so I guess
[L1815] [58:13.40] there's there's you know, the two
[L1816] [58:14.32] different arguments which is one is like
[L1817] [58:17.84] it doesn't matter. The other is I
[L1818] [58:19.16] learned a ton of stuff that I think was
[L1819] [58:20.88] pretty useful to my career.
[L1820] [58:22.72] Um and I had some fun.
[L1821] [58:24.84] >> Earlier you said uh top questions that
[L1822] [58:27.16] people ask you and I'm kind of curious,
[L1823] [58:29.20] what's the top question?
[L1824] [58:31.28] >> I think the one the other one that I get
[L1825] [58:33.60] a lot um
[L1826] [58:35.44] is uh
[L1827] [58:37.28] how do I know what I should learn?
[L1828] [58:39.72] Like a lot of a lot of especially when I
[L1829] [58:41.20] talk to the interns for the first couple
[L1830] [58:43.00] of years,
[L1831] [58:44.40] you know, a lot of the questions are
[L1832] [58:45.44] right revolving around like "AI seems
[L1833] [58:47.68] really hot right now, but I'm really
[L1834] [58:49.04] interested in systems. Like should I
[L1835] [58:51.12] like go learn AI cuz it's hot or should
[L1836] [58:53.20] I learn systems cuz I think systems are
[L1837] [58:55.52] interesting?" Actually kind of don't
[L1838] [58:57.12] care what you learn. I care that you're
[L1839] [58:58.88] learning.
[L1840] [59:00.04] Um and and so the most important thing
[L1841] [59:03.00] is to find something that you're excited
[L1842] [59:04.40] about and energized about
[L1843] [59:06.48] um because you know, you'll do that
[L1844] [59:09.04] instead of watching YouTube. Uh
[L1845] [59:11.12] you know, so if you're not excited about
[L1846] [59:12.32] AI, like well, you're probably not going
[L1847] [59:14.28] to do a very good job learning AI. Which
[L1848] [59:16.76] means that you're kind of going to waste
[L1849] [59:17.92] your time.
[L1850] [59:19.16] Um but if you're really excited about
[L1851] [59:21.00] systems, you probably put a lot of
[L1852] [59:22.60] passion and energy into it. And you
[L1853] [59:24.80] know, we still need systems engineers.
[L1854] [59:26.24] Like so,
[L1855] [59:28.16] um
[L1856] [59:29.12] I you know, I think that's the that's
[L1857] [59:31.04] kind of a pretty popular question. I
[L1858] [59:33.00] think there's a lot of I I sense anyway
[L1859] [59:35.24] a lot of like
[L1860] [59:36.64] fear [snorts] of making the wrong
[L1861] [59:37.92] decision.
[L1862] [59:39.88] And,
[L1863] [59:41.56] uh
[L1864] [59:42.24] I will tell everybody like there was no
[L1865] [59:43.44] plan.
[L1866] [59:44.56] I've never had a plan for my career.
[L1867] [59:46.28] Like, never ever ever.
[L1868] [59:48.28] Like, I've always just chased after
[L1869] [59:50.04] things that I thought were useful and or
[L1870] [59:51.52] fun and interesting.
[L1871] [59:53.64] Um
[L1872] [59:54.72] and
[L1873] [59:56.36] uh and, you know, obviously like that
[L1874] [59:58.80] can work out badly for people. I'm sure
[L1875] [01:00:00.44] it's good to have a plan probably for
[L1876] [01:00:01.88] some people, but like I also want to
[L1877] [01:00:03.28] make sure people understand that like
[L1878] [01:00:05.32] when you look back
[L1879] [01:00:07.12] sometimes the things you think were
[L1880] [01:00:08.44] mistakes or dead ends, like
[L1881] [01:00:10.96] actually were critical things that
[L1882] [01:00:12.28] taught you stuff.
[L1883] [01:00:13.64] Um
[L1884] [01:00:15.16] and so like worrying about did I choose
[L1885] [01:00:17.00] the wrong thing? Am I going to choose
[L1886] [01:00:18.40] the wrong thing? Like, eh,
[L1887] [01:00:20.36] as long as you're learning, you're
[L1888] [01:00:21.68] probably doing okay.
[L1889] [01:00:23.12] >> I mean, what you're describing it
[L1890] [01:00:24.56] reminds me of I don't know if you've
[L1891] [01:00:25.80] seen that Steve Jobs commencement
[L1892] [01:00:27.76] speech, but he
[L1893] [01:00:29.36] he literally says exactly that. You
[L1894] [01:00:32.08] wrote down somewhere I I don't fully
[L1895] [01:00:34.52] remember where you wrote this down, but
[L1896] [01:00:35.88] I have this in my notes. It says,
[L1897] [01:00:37.84] "The inevitable trajectory of software
[L1898] [01:00:40.20] is death."
[L1899] [01:00:41.52] And I just can't imagine Kubernetes
[L1900] [01:00:44.04] dying, but I how do you see that
[L1901] [01:00:46.48] happening and you know, what what do you
[L1902] [01:00:48.20] think about that if it did?
[L1903] [01:00:50.52] >> I mean, I definitely stick by that uh
[L1904] [01:00:53.56] that statement. Um
[L1905] [01:00:55.48] Although I think that the the the the
[L1906] [01:00:57.12] the sense before I said that was you
[L1907] [01:00:59.96] really should never fall in love with
[L1908] [01:01:01.48] your software
[L1909] [01:01:03.04] because the inevitable
[L1910] [01:01:04.96] trajectory of software is death. I am
[L1911] [01:01:08.00] It's which means don't stick with it
[L1912] [01:01:09.32] don't stick with it past when it's
[L1913] [01:01:11.04] dying, right? Um
[L1914] [01:01:13.40] like you should always be willing to
[L1915] [01:01:14.40] throw away stuff. Just don't stick with
[L1916] [01:01:15.96] it just cuz you wrote it. You should
[L1917] [01:01:17.32] always be willing to throw it away.
[L1918] [01:01:19.36] But, like obviously I think if you look
[L1919] [01:01:21.88] historically across the industry, it's
[L1920] [01:01:23.44] it's true, too, right? Like like
[L1921] [01:01:26.72] Um and and quite frankly, like even
[L1922] [01:01:28.52] within Kubernetes, like
[L1923] [01:01:30.40] the source code that I wrote has been
[L1924] [01:01:32.40] rewritten a number of times.
[L1925] [01:01:34.44] Um
[L1926] [01:01:36.24] over the 10-plus years history of the
[L1927] [01:01:37.88] project. Um
[L1928] [01:01:39.28] so, what does it look like? I mean, I
[L1929] [01:01:40.56] think it looks like uh
[L1930] [01:01:42.48] something coming along that achieves
[L1931] [01:01:44.92] similar things, but easier with more uh
[L1932] [01:01:49.20] you know, you with with less complexity
[L1933] [01:01:50.92] and and more utility. Um and and I think
[L1934] [01:01:53.64] that
[L1935] [01:01:54.96] you know, I can imagine what that looks
[L1936] [01:01:56.72] like. Like I think some of these natural
[L1937] [01:01:58.64] language stuff, if you could actually
[L1938] [01:02:00.56] really get it to be an interface that
[L1939] [01:02:01.92] worked 100% of the time, like obviously,
[L1940] [01:02:04.64] it's way easier to come in and say
[L1941] [01:02:07.12] I would like a reliable web service than
[L1942] [01:02:08.80] it is to say "YAML YAML YAML YAML YAML."
[L1943] [01:02:11.60] You know, I I think sometimes I I think
[L1944] [01:02:13.16] it's sort of your two different
[L1945] [01:02:14.12] trajectories. Like sometimes the
[L1946] [01:02:15.16] trajectory is
[L1947] [01:02:16.88] it it goes away. Sometimes it just
[L1948] [01:02:18.36] becomes so hidden that nobody sees it.
[L1949] [01:02:20.92] Right? Like underneath Linux, there's
[L1950] [01:02:24.16] I mean, excuse me, underneath
[L1951] [01:02:24.96] Kubernetes, there's Linux. And
[L1952] [01:02:26.20] underneath Linux, there's a processor.
[L1953] [01:02:28.40] But, you know, people don't pay much
[L1954] [01:02:29.44] attention to that. Um
[L1955] [01:02:31.60] and there's a lot of attention now on
[L1956] [01:02:32.72] AI, and underneath a lot of the AI is
[L1957] [01:02:34.72] Linux, but it could be that people focus
[L1958] [01:02:36.28] so much on the AI that they forget about
[L1959] [01:02:38.64] the Kubernetes part.
[L1960] [01:02:40.36] Um
[L1961] [01:02:41.40] and I think that's happening already,
[L1962] [01:02:42.60] honestly. Like I feel like
[L1963] [01:02:44.56] if I look at the volume of changes and
[L1964] [01:02:46.56] things like that, like I think it's you
[L1965] [01:02:48.20] know, I think we've sort of plateaued in
[L1966] [01:02:49.44] terms of like the amount of change
[L1967] [01:02:51.60] that's driving through the system. Um
[L1968] [01:02:54.20] stuff needed to support AI is kind of
[L1969] [01:02:55.92] like the
[L1970] [01:02:57.20] exception to that category.
[L1971] [01:02:59.12] Um
[L1972] [01:03:01.00] but, you know, I I I
[L1973] [01:03:03.56] I'd be shocked. I mean, I guess I'll put
[L1974] [01:03:04.80] it this way. Like let me take the long
[L1975] [01:03:05.88] view and say
[L1976] [01:03:07.28] in 100 years,
[L1977] [01:03:09.12] is Kubernetes still going to be running?
[L1978] [01:03:10.56] I'd be pretty surprised.
[L1979] [01:03:12.49] >> [laughter]
[L1980] [01:03:12.96] >> Right?
[L1981] [01:03:14.24] It's hard to imagine, right?
[L1982] [01:03:16.52] Um that that that would be true. I mean,
[L1983] [01:03:18.24] I don't know. We haven't had computing
[L1984] [01:03:19.36] systems for long enough to maybe know
[L1985] [01:03:20.76] for certain.
[L1986] [01:03:21.96] Um
[L1987] [01:03:24.08] and there are things that we still use.
[L1988] [01:03:26.00] I mean, there is some stuff that we
[L1989] [01:03:27.64] still use from back then. Plugs are
[L1990] [01:03:29.24] still the same shape-ish, stuff like
[L1991] [01:03:31.36] that.
[L1992] [01:03:32.28] Um
[L1993] [01:03:33.48] so maybe.
[L1994] [01:03:34.64] But even like something like x86, like
[L1995] [01:03:36.12] if you'd asked me 6 years ago and said,
[L1996] [01:03:38.24] "Is the x86 processor going away?"
[L1997] [01:03:41.04] I'd say like, "Well, maybe on I mean,
[L1998] [01:03:43.16] obviously on mobile it did, but like in
[L1999] [01:03:45.60] the server?
[L2000] [01:03:47.36] Maybe not." Um but now two things have
[L2001] [01:03:50.44] happened. One is all the processing is
[L2002] [01:03:51.76] on GPU now.
[L2003] [01:03:53.08] And two, like arm 64 is now pretty
[L2004] [01:03:56.40] important platform on the server for
[L2005] [01:03:57.88] energy usage and other reasons, right?
[L2006] [01:04:00.44] And so
[L2007] [01:04:02.04] it's pretty dangerous to predict the
[L2008] [01:04:03.28] future cuz like
[L2009] [01:04:05.20] it has a tendency of show up sooner than
[L2010] [01:04:06.96] you you you predict. So, or or longer
[L2011] [01:04:09.60] than you predict, too, right?
[L2012] [01:04:10.80] Self-driving cars, like I've heard I've
[L2013] [01:04:12.52] heard self-driving cars were 5 years
[L2014] [01:04:14.20] away for like the last 15 years.
[L2015] [01:04:16.68] >> [laughter]
[L2016] [01:04:16.84] >> Yeah. Uh,
[L2017] [01:04:18.32] me too. I I don't know if you read books
[L2018] [01:04:21.48] for career's sake, but if you do, is
[L2019] [01:04:24.12] there a book that impacted your career
[L2020] [01:04:26.08] the most?
[L2021] [01:04:27.44] >> Well, I mean, I would say like early on
[L2022] [01:04:29.08] the book that that impacted my career
[L2023] [01:04:30.72] the most was a book uh was the gang of
[L2024] [01:04:32.72] four book. Was it software engineering
[L2025] [01:04:35.04] designs and patterns or whatever? Like
[L2026] [01:04:36.48] it's a software engineering book.
[L2027] [01:04:37.92] >> I I see it. It's design patterns,
[L2028] [01:04:39.88] elements of reusable object-oriented
[L2029] [01:04:42.80] software.
[L2030] [01:04:43.48] >> Yeah, there you go. So, that like early
[L2031] [01:04:44.88] on that was a very influential book.
[L2032] [01:04:46.28] It's like a late '90s or mid '90s kind
[L2033] [01:04:48.16] of book. Uh there's a much more recent
[L2034] [01:04:50.56] book called uh Leadership on the Line
[L2035] [01:04:53.44] that as I've become sort of a large org
[L2036] [01:04:55.04] leader, that's uh I really like that
[L2037] [01:04:57.52] book. And then there's this What's this
[L2038] [01:04:59.32] book? It's called I think Five
[L2039] [01:05:00.32] Dysfunctions of Teams, I think. That's a
[L2040] [01:05:02.52] really good book, too, for uh from a
[L2041] [01:05:04.16] like a how teams operate perspective.
[L2042] [01:05:07.68] >> If I'm understanding if you're an if
[L2043] [01:05:09.08] you're an engineer,
[L2044] [01:05:10.40] check out that first book. If you're a
[L2045] [01:05:11.92] manager or a leader, check out the
[L2046] [01:05:13.80] second two books. Yeah, that's probably
[L2047] [01:05:15.40] about right. Yeah, I think that's I
[L2048] [01:05:16.88] think that's right. And then, you know,
[L2049] [01:05:17.80] it's an evolution over time, right? So,
[L2050] [01:05:19.28] like, maybe you'll do both.
[L2051] [01:05:21.88] Uh last question for you is
[L2052] [01:05:23.92] um if you could go back to yourself when
[L2053] [01:05:26.00] you just graduated college and give
[L2054] [01:05:28.12] yourself some advice,
[L2055] [01:05:29.84] what would you say?
[L2056] [01:05:31.60] >> Uh keep better notes.
[L2057] [01:05:33.64] You know, I feel like there's a great
[L2058] [01:05:35.12] MBA thesis or a great like book
[L2059] [01:05:38.36] in the whole Kubernetes journey and
[L2060] [01:05:40.88] beyond and like
[L2061] [01:05:42.56] I you know, like I don't I just don't
[L2062] [01:05:43.84] have enough notes to
[L2063] [01:05:45.64] uh to to do that, to write it down. You
[L2064] [01:05:48.32] know, I like we we went through a lot
[L2065] [01:05:49.76] like a lot of different stuff happened,
[L2066] [01:05:51.28] and I remember some of it, and I don't
[L2067] [01:05:53.16] remember a lot of it, and it would I
[L2068] [01:05:55.04] would have been nicer if I'd kept better
[L2069] [01:05:56.52] notes, I feel like.
[L2070] [01:05:57.88] >> All right. Well, well, you got all the
[L2071] [01:05:59.00] code there. Maybe an LLM can parse it or
[L2072] [01:06:01.48] something. You can reach out
[L2073] [01:06:02.96] >> more It's not so much about the notes
[L2074] [01:06:04.48] part. It's not so much about the code
[L2075] [01:06:05.64] part. It's like all of the Like the
[L2076] [01:06:07.36] stuff you were talking about, like all
[L2077] [01:06:08.40] the partner discussions and all of the
[L2078] [01:06:11.00] like interpersonal stuff and, you know,
[L2079] [01:06:13.72] all that kind of stuff. And like I
[L2080] [01:06:15.64] remember a lot of it, but I don't
[L2081] [01:06:16.88] remember all of it.
[L2082] [01:06:18.20] >> Cool. Well, thank you so much for your
[L2083] [01:06:19.64] time, Brendan. I really appreciate it.
[L2084] [01:06:21.12] >> Yeah, for sure. Thank you.
[L2085] [01:06:22.88] >> Thank you for listening to the podcast.
[L2086] [01:06:24.56] It's a passion project of mine that I've
[L2087] [01:06:26.72] really enjoyed building. Another passion
[L2088] [01:06:28.80] project that I've been working on kind
[L2089] [01:06:30.16] of in secret is building an ergonomic
[L2090] [01:06:32.68] keyboard that I wish existed, and I
[L2091] [01:06:34.92] finally have a prototype, so I'd love to
[L2092] [01:06:36.64] show you what we've built. It's ultra
[L2093] [01:06:39.44] low profile and ergonomic, and I
[L2094] [01:06:41.96] couldn't find anything like it on the
[L2095] [01:06:43.16] market, so that's why we built it. I'll
[L2096] [01:06:45.16] put a link to the keyboard in the
[L2097] [01:06:46.36] description. You can take a look and
[L2098] [01:06:47.96] learn more about the project there. We
[L2099] [01:06:49.80] could definitely use your support. Also,
[L2100] [01:06:51.80] if you have any feedback for me about
[L2101] [01:06:53.44] the show, I'd love to hear it. Comments
[L2102] [01:06:55.88] on YouTube have led to guests coming on
[L2103] [01:06:57.88] like Ilya Grigorik and David Fowler. I
[L2104] [01:07:00.92] wasn't aware of them until someone
[L2105] [01:07:02.76] dropped a comment. Also, feedback in the
[L2106] [01:07:04.64] comments helped me learn to reduce the
[L2107] [01:07:06.32] number of cliff hangers in the intros.
[L2108] [01:07:08.96] So, your comments definitely make a
[L2109] [01:07:10.24] difference. Please keep letting me know
[L2110] [01:07:11.92] what you'd like to see more of in the
[L2111] [01:07:13.28] show, and I'll see you in the next
[L2112] [01:07:14.68] episode.
