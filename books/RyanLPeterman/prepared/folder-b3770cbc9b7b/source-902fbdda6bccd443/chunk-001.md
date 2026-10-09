Chunk 1; segments 1–344. 

# Sergey Levine: Humanoid Robotics Results, Chinese Labs & Future Timelines

Source ID: source-902fbdda6bccd443
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Sergey_Levine_Humanoid_Robotics_Results,_Chinese_Labs_&_Future_Timelines_en.txt
Video: https://www.youtube.com/watch?v=9OSbaPjv0Rc

[L10] [00:00.16] To me, that's kind of mind-blowing
[L11] [00:01.28] because like the base model wasn't
[L12] [00:02.56] trained on any human data at all.
[L13] [00:04.40] >> This is Sergey Lavine, one of the
[L14] [00:06.32] world's leading robotics researchers,
[L15] [00:08.16] and I asked him all about the current
[L16] [00:09.84] state of humanoid robotics. What are the
[L17] [00:12.24] most astonishing emergent capabilities
[L18] [00:14.72] you've seen so far?
[L19] [00:15.92] >> I don't think anybody watching that eval
[L20] [00:17.60] thought that the robot was going to do
[L21] [00:19.12] this.
[L22] [00:20.32] >> I have some questions here on China.
[L23] [00:22.32] There's no avoiding it sometimes.
[L24] [00:25.04] If humanoid robotics did not succeed in
[L25] [00:27.52] singledigit years, what do you think
[L26] [00:29.76] would be the most likely reason why
[L27] [00:31.84] humanoid robotics failed?
[L28] [00:35.12] Here's the full episode.
[L29] [00:40.24] LLMs have caused unprecedented impact
[L30] [00:43.68] and investment in that area. Physical AI
[L31] [00:46.72] and humanoid robots could potentially be
[L32] [00:49.92] even bigger. And so I wanted to ask you
[L33] [00:52.24] today about where are we today with
[L34] [00:55.20] humanoid robotics and how do you foresee
[L35] [00:58.16] this technology actually being deployed
[L36] [01:00.80] into the world. I guess with machine
[L37] [01:03.36] learning uh what we've learned over the
[L38] [01:05.28] last few years over the last decade
[L39] [01:07.12] rather is that um it works when you do
[L40] [01:10.32] it at scale and this is like very
[L41] [01:11.92] obvious now but it wasn't always
[L42] [01:13.28] obvious. Uh but there's a caveat which
[L43] [01:15.60] is you have to like scale the right
[L44] [01:17.12] thing and uh you know initially when
[L45] [01:20.08] people started working on um models for
[L46] [01:22.88] language for example the dominant uh
[L47] [01:25.28] design was uh LSTMs um some people
[L48] [01:28.64] remember what those are. They were like
[L49] [01:30.80] kind of okay they were a lot better than
[L50] [01:32.24] what came before that but they didn't
[L51] [01:33.84] really scale as well. And then the the
[L52] [01:35.52] big thing with transformers was not that
[L53] [01:37.04] transformers were somehow like uh
[L54] [01:39.04] particularly um you know mathematically
[L55] [01:41.36] elegant or anything like that. It's just
[L56] [01:42.40] that they scaled better. So they were
[L57] [01:43.84] easier to train a very large amounts of
[L58] [01:45.28] data with lots of parameters. So the
[L59] [01:47.28] technology proceeds in phases. First you
[L60] [01:48.96] figure out what you can scale basically
[L61] [01:50.56] what is the scalable technology and then
[L62] [01:52.48] you pour on a lot more of kind of an
[L63] [01:54.48] industrial scale effort adding lots of
[L64] [01:56.48] data adding to model size and that's
[L65] [01:58.72] when kind of the magic happens. So when
[L66] [02:01.36] we're doing kind of more fundamental
[L67] [02:02.80] technology development the key is to
[L68] [02:04.08] understand like what are those scalable
[L69] [02:05.92] levers. So figure out the design, figure
[L70] [02:08.00] out like roughly the mixtures and and
[L71] [02:10.56] that by itself does something pretty
[L72] [02:12.32] cool, but not like uh but that's that's
[L73] [02:15.04] not the thing that actually changes the
[L74] [02:16.24] world. It's like when you start pulling
[L75] [02:17.28] that lever that things actually change.
[L76] [02:19.04] So with LLMs um when uh like the first
[L77] [02:23.36] GPT models came out uh with GPT2 like it
[L78] [02:27.20] did some stuff but it was sort of like
[L79] [02:28.80] um like a parlor shook, right? So you
[L80] [02:30.80] you could like get it to synthesize a
[L81] [02:32.40] story about like unicorns in Peru or
[L82] [02:35.04] something and it was like coherent
[L83] [02:36.24] English but it wasn't like a thing that
[L84] [02:37.76] would solve lots of real world problems.
[L85] [02:39.84] But the folks that worked on this kind
[L86] [02:41.52] of recognized that like hey there's
[L87] [02:43.12] something kind of magical that happens
[L88] [02:44.48] because uh as you add uh more data and
[L89] [02:47.12] you make the model bigger like you know
[L90] [02:48.40] this stuff gets more coherent and more
[L91] [02:49.68] effective. So they they they could see
[L92] [02:51.12] that if we do a lot more of that then
[L93] [02:53.28] it'll become a lot more powerful. So uh
[L94] [02:55.76] to come back to your question what I
[L95] [02:58.24] would say about robotics is that it's
[L96] [03:00.32] not in the in the like GPT4 to GPT5
[L97] [03:03.76] stage where it's like an industrial
[L98] [03:05.44] scale effort to kind of make the model
[L99] [03:07.20] bigger and and u get more capability out
[L100] [03:10.16] it. It's in that stage where we're
[L101] [03:11.44] establishing the fundamental
[L102] [03:12.56] technologies and because of that what uh
[L103] [03:16.16] one should expect to see right now is
[L104] [03:18.56] not necessarily that like you know each
[L105] [03:21.20] month the model gets bigger and more
[L106] [03:23.36] powerful by some predictable uh kind of
[L107] [03:25.60] scaling curve. It's that the I guess the
[L108] [03:28.72] scaling properties themselves are
[L109] [03:30.00] evolving as we develop the right
[L110] [03:31.28] technologies. So, uh, to to bring this
[L111] [03:33.68] back to something like closer to
[L112] [03:35.04] reality, um, I'm very happy with like
[L113] [03:37.92] the demos that we're doing here at
[L114] [03:39.28] physical intelligence, and I think that
[L115] [03:40.64] a lot of the results that other people
[L116] [03:42.16] are coming out with are really cool, but
[L117] [03:43.52] these are to put them in context, we
[L118] [03:46.00] should not expect these to be the things
[L119] [03:47.60] that are actually illustrating the power
[L120] [03:48.80] of scale. We should expect them to be
[L121] [03:50.40] developing the fundamental technologies
[L122] [03:52.16] that will be scaled up after that. So,
[L123] [03:55.52] so where I think we're at now is that
[L124] [03:57.04] we're actually kind of getting all those
[L125] [03:59.12] puzzle pieces in place. And I think it's
[L126] [04:00.80] actually very close. I think a lot of
[L127] [04:01.92] the puzzle pieces are falling in place.
[L128] [04:03.52] Uh but it's not like uh what makes it so
[L129] [04:06.88] hard to prognosticate about where the
[L130] [04:08.48] technology is going to go is that it's
[L131] [04:10.00] not yet at that predictable scaling
[L132] [04:11.60] stage. It's at the stage where we're
[L133] [04:12.88] figuring out the puzzle pieces, which I
[L134] [04:15.12] think is really exciting, but it means
[L135] [04:16.56] that it's also very very hard to foresee
[L136] [04:18.24] like you know sort of what the
[L137] [04:19.04] coefficients on that will be.
[L138] [04:20.72] >> What are the most astonishing emerging
[L139] [04:23.12] capabilities you've seen so far? that
[L140] [04:25.60] that is the thing that is the most fun
[L141] [04:27.12] and and certainly we've seen a a lot
[L142] [04:30.32] more of that happening as we progress.
[L143] [04:32.40] Um like you know in the very beginning
[L144] [04:35.04] it was like it was kind of little things
[L145] [04:36.72] but they were kind of magical because
[L146] [04:39.12] you know in robotics basically prior to
[L147] [04:41.60] like 2024 the stuff like never happened.
[L148] [04:43.92] Uh so the little things that happen and
[L149] [04:45.60] this was maybe like at this point about
[L150] [04:47.76] two years back we would see things like
[L151] [04:49.92] okay we train our policy for folding
[L152] [04:51.44] laundry and it takes out like individual
[L153] [04:53.76] shirts out of the hamper and tries to
[L154] [04:55.20] fold them and then um um one very vivid
[L155] [04:59.20] memory I have uh in late 2024 is we we
[L156] [05:02.00] were watching one of the evals and it
[L157] [05:03.60] takes out like two shirts at the same
[L158] [05:04.88] time and I'm I'm watching this I'm like
[L159] [05:06.72] okay like like it's done for like
[L160] [05:09.20] there's no way it can possibly do this
[L161] [05:10.72] and then it puts the two shirts on the
[L162] [05:13.04] table disentangles and puts one of them
[L163] [05:14.80] back and then starts folding the other
[L164] [05:16.40] one. It's like wow like that. Okay, like
[L165] [05:18.64] in retrospect you can do some like
[L166] [05:20.00] detective work and figure out where it
[L167] [05:21.44] got that from some piece of training
[L168] [05:22.72] data, but that was like one of those
[L169] [05:24.56] moments where I don't think anybody
[L170] [05:26.00] watching that eval thought that like the
[L171] [05:28.16] robot was going to do this. It's like a
[L172] [05:30.00] little thing. It's like exhibiting the
[L173] [05:31.36] common sense you expect people to have.
[L174] [05:33.20] Um but actually the thing that I find
[L175] [05:34.88] more interesting recently is um uh some
[L176] [05:37.76] of the mistakes because one of the
[L177] [05:39.76] things that's uh that was pretty
[L178] [05:41.92] remarkable about LLMs is that once they
[L179] [05:44.08] got good enough even the mistakes kind
[L180] [05:46.08] of made sense in the sense that they
[L181] [05:47.36] weren't like crazy mistakes where just
[L182] [05:48.72] outputs like ZZZ all the time but they
[L183] [05:51.12] were mistakes that sort of semantically
[L184] [05:52.40] are sensible. Uh we had uh an evaluation
[L185] [05:55.68] uh last year for pio5 where the robot
[L186] [05:58.08] was uh uh cleaning up a kitchen and it's
[L187] [06:00.96] told like put away all the all the
[L188] [06:02.48] utensils. Like there's like some some
[L189] [06:03.76] spoons, spatulas, etc. And uh it tries
[L190] [06:07.36] to open the drawer where it thinks the
[L191] [06:08.64] silverware goes and it can't get the
[L192] [06:09.92] drawer open. So it slides over and opens
[L193] [06:11.84] the oven which is right next to it and
[L194] [06:13.76] then starts putting this stuff in the
[L195] [06:14.96] oven. [laughter] It's like, you know,
[L196] [06:16.80] you can sort of imagine that if you ask
[L197] [06:18.00] like a child to clean stuff up and put
[L198] [06:19.36] it away, like they might they might
[L199] [06:20.56] decide to do that because, okay, it's
[L200] [06:21.60] like a container and you can put stuff
[L201] [06:22.72] there and nobody sees it. Um, another
[L202] [06:25.04] experiment we had is uh uh washing all
[L203] [06:27.28] the plates. So, it would like pick up
[L204] [06:29.12] the plates, wash them with a sponge, and
[L205] [06:30.80] put them on the drying rack. Uh, and uh
[L206] [06:32.96] this was an experiment on memory because
[L207] [06:34.80] it has to keep track of everything that
[L208] [06:36.00] it's doing. It has like a scratch pad
[L209] [06:37.44] kind of memory where it's writing down
[L210] [06:38.64] like, hey, you know, I had three plates.
[L211] [06:40.32] I cleaned the gray one. I cleaned the
[L212] [06:41.84] green one. And then it drops one of them
[L213] [06:43.44] on the floor and drives the base over.
[L214] [06:45.68] so you can't see. I was like, "Okay,
[L215] [06:46.72] I've cleaned the the gray plate. It's
[L216] [06:48.64] it's [laughter] done."
[L217] [06:50.56] Um, so I mean, obviously like these are
[L218] [06:52.80] not the things that we want to see, but
[L219] [06:54.32] it's kind of interesting that some of
[L220] [06:55.68] the mistakes, they're almost like what
[L221] [06:57.52] you would associate with like a child
[L222] [06:59.44] trying to do the task. So now now now it
[L223] [07:01.92] just needs to grow up.
[L224] [07:03.44] >> You mentioned uh the advancements.
[L225] [07:05.92] They're kind of happening all over the
[L226] [07:08.24] industry. And I I know there's a lot of
[L227] [07:10.64] people building humanoid robots. There's
[L228] [07:13.04] Figure, there's there's Tesla and
[L229] [07:14.80] there's many other competitors and you
[L230] [07:17.68] have the expertise of what is hard and
[L231] [07:19.92] what isn't. When you look at the
[L232] [07:21.84] competitors, has there been any
[L233] [07:24.40] advancement or achievement where you
[L234] [07:26.56] think, "Oh, that's really admirable and
[L235] [07:28.48] that's impressive." actually think that
[L236] [07:31.12] one of the most inspiring things to me
[L237] [07:33.12] in the industry is to see the um the
[L238] [07:36.24] kind of takeoff that autonomous driving
[L239] [07:37.84] systems have had because you know like
[L240] [07:39.84] one of the criticisms that is sometimes
[L241] [07:42.00] leveled against robotics researchers is
[L242] [07:44.48] uh you know it's it's like uh you know
[L243] [07:46.24] same as like nuclear fusion like it's
[L244] [07:47.92] it's the technology of the future but
[L245] [07:49.28] it's always in the future but that's
[L246] [07:50.72] what people said about autonomous
[L247] [07:51.84] driving too and now like you know we're
[L248] [07:53.28] in San Francisco you can go outside you
[L249] [07:54.80] can take a Whimo and it will actually
[L250] [07:56.24] like take you to your destination and
[L251] [07:57.52] there's no driver sitting there So I
[L252] [08:00.16] like you know without getting too much
[L253] [08:02.16] into the technical details I think
[L254] [08:03.44] what's really inspiring about that is
[L255] [08:04.72] just like this case and point that yes
[L256] [08:07.84] you can actually have one of these
[L257] [08:09.12] technologies of the future and it
[L258] [08:10.56] actually does land and I think it's not
[L259] [08:12.40] an accident that it's landing now in the
[L260] [08:14.96] mid 2020s because a lot of the puzzle
[L261] [08:17.44] pieces for largecale ML are getting to
[L262] [08:20.40] the level where we can put them together
[L263] [08:23.12] with like actual physical systems and
[L264] [08:25.20] there's a lot of differences between
[L265] [08:26.32] driving and robotic manipulation of
[L266] [08:27.92] course but I think the illustration that
[L267] [08:30.40] like yeah we can actually land uh
[L268] [08:32.40] learning based technologies in the real
[L269] [08:34.16] physical world I think that's really
[L270] [08:35.36] inspiring
[L271] [08:36.56] >> if openthropic
[L272] [08:38.32] started investing you know more heavily
[L273] [08:40.64] into robotics how do you think that
[L274] [08:43.12] would impact the industry do you think
[L275] [08:45.44] competitors would be you know worried
[L276] [08:47.44] about that robotics is um is an area
[L277] [08:52.16] where
[L278] [08:53.92] maybe to be fair like the ecosystem
[L279] [08:55.60] hasn't been as healthy as it has in
[L280] [08:57.20] other areas of machine learning And what
[L281] [08:58.64] I mean by that is that um like computer
[L282] [09:01.60] vision and NLP are things that sort of
[L283] [09:03.60] lend themselves naturally to a machine
[L284] [09:07.28] learning based ecosystem because there's
[L285] [09:09.20] freely available data. Uh people kind of
[L286] [09:11.76] have a a general acceptance that they're
[L287] [09:13.52] going to be using learning. You know,
[L288] [09:15.12] there aren't concerns as severe concerns
[L289] [09:17.84] about like safety, at least physical
[L290] [09:19.76] safety, right? You know, people
[L291] [09:21.12] rightfully are concerned about AI
[L292] [09:22.96] safety, but it's not the same as like a
[L293] [09:24.48] physical device uh causing some physical
[L294] [09:26.64] harm. um and uh because of that I think
[L295] [09:29.68] it's a bit easier to spin up a very
[L296] [09:32.08] serious large scale ML effort in those
[L297] [09:33.84] areas. Robotics is not like that.
[L298] [09:35.52] Robotics traditionally is not a
[L299] [09:38.64] discipline that um you know really
[L300] [09:41.60] embraces sharing of data for example. So
[L301] [09:44.16] I think that the more activity there is
[L302] [09:46.88] around learning in robotics, the more I
[L303] [09:49.12] think it'll shift people's thinking
[L304] [09:50.88] towards this kind of future where we
[L305] [09:52.88] accept that robots will be controlled by
[L306] [09:54.56] learned models, not by handdesigned
[L307] [09:56.64] controllers, that there will be data
[L308] [09:58.48] that data will need to be shared because
[L309] [10:00.24] there's no way that somebody can uh
[L310] [10:02.16] build out a true foundation model in a
[L311] [10:03.92] single vertical uh and basically kind of
[L312] [10:06.00] like shift the entire thinking around
[L313] [10:07.36] robotics to look more like how we think
[L314] [10:09.12] about vision and NLP as opposed to
[L315] [10:10.96] traditional factory automation. So I
[L316] [10:13.04] think in that sense like you know much
[L317] [10:15.04] as I'm like proud of the work that we're
[L318] [10:16.40] doing in physical intelligence I think
[L319] [10:18.24] it'll take more than one company to kind
[L320] [10:20.24] of like shift every everyone's thinking
[L321] [10:21.84] in that direction. As a bystander I see
[L322] [10:24.40] on Twitter these really impressive
[L323] [10:26.48] demonstrations of Chinese robotics. It
[L324] [10:28.80] it almost feels like they're ahead in
[L325] [10:31.84] some sense but I don't have that uh deep
[L326] [10:35.12] domain expertise. And so I was curious
[L327] [10:37.60] your thoughts on, you know, what do you
[L328] [10:39.76] think of China's robotics and, you know,
[L329] [10:43.28] are are they further along?
[L330] [10:45.52] >> I think that one thing that um
[L331] [10:49.60] is very useful and constructive for for
[L332] [10:52.00] us to do uh those of us that uh work on
[L333] [10:54.96] these things in the United States and in
[L334] [10:56.64] Europe, uh is to
[L335] [10:59.92] ask what is the lesson to learn? And to
[L336] [11:02.80] me one lesson is that it's important to
[L337] [11:06.08] have a healthy ecosystem
[L338] [11:08.32] and ecosystem means that there should be
[L339] [11:11.76] um you know obviously good researchers,
[L340] [11:14.48] good engineers working on these things.
[L341] [11:16.88] there should be like healthy open source
[L342] [11:18.88] but it also means that the different
[L343] [11:22.08] industries that contribute to robotics
[L344] [11:25.60] need to individually be very healthy and
[L345] [11:28.08] those industries are not just the um you
[L346] [11:30.40] know computer science ML and and model
[L347] [11:32.80] building stuff it's also uh supply
[L348] [11:35.52] chains manufacturing
[L349] [11:38.08] hardware R&D like these are all very
[L350] [11:40.00] important things and
[L351] [11:42.72] aspects of those things are things that
[L352] [11:45.28] uh the United States does quite Other
[L353] [11:47.52] aspects of them are things where the
