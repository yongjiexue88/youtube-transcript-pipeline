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
[L354] [11:49.12] United States has sort of uh you know
[L355] [11:50.56] let things go a little bit. Uh and I
[L356] [11:52.64] think that what we should do is we
[L357] [11:54.08] should look at what's going on in the
[L358] [11:55.68] world look at the uh some of the uh
[L359] [11:59.28] excellent results uh that uh Chinese
[L360] [12:01.68] labs are doing that labs in other
[L361] [12:03.28] countries are doing and we should take
[L362] [12:04.24] away that lesson that we should strive
[L363] [12:05.84] to build a healthier ecosystem and that
[L364] [12:07.36] means investing in all the different
[L365] [12:09.20] facets uh that contribute to this. So
[L366] [12:12.00] you know I'm not like I'm not much of a
[L367] [12:13.84] business person. I'm not much of a
[L368] [12:15.12] investment person. So I don't I can't
[L369] [12:17.28] claim to know how to do this, but I
[L370] [12:18.72] think that it's important to sort of
[L371] [12:20.48] fully embrace that this is like a
[L372] [12:22.24] holistic thing and not something where
[L373] [12:23.52] we can do just like one piece of it and
[L374] [12:24.88] like outsource everything else basically
[L375] [12:27.28] >> of all that the pieces of the ecosystem
[L376] [12:30.72] are there parts of it as a robotics
[L377] [12:33.04] researcher in the US if it was better
[L378] [12:36.00] that would have the biggest impact on
[L379] [12:37.76] the advancement of robotics? Yeah, I I
[L380] [12:39.92] think certainly um availability of
[L381] [12:42.96] reliable lowcost hardware is a big deal
[L382] [12:45.68] and right now I mean certainly for uh
[L383] [12:48.32] hardware used for robotics research a
[L384] [12:50.64] lot of that does come from China and
[L385] [12:52.00] it's it's good it's uh relatively
[L386] [12:54.56] inexpensive it's of high quality and uh
[L387] [12:56.80] meets the uh standards that people
[L388] [12:59.28] generally need. Uh but it would be
[L389] [13:01.28] awfully nice to be able to uh source all
[L390] [13:03.52] that domestically as well. And I I I
[L391] [13:05.76] don't think there's anything impossible
[L392] [13:06.80] about that. I think it's just a matter
[L393] [13:08.00] of sort of uh embracing the fact that
[L394] [13:10.32] that entire uh ecosystem needs to be
[L395] [13:13.20] supported rather than just one piece of
[L396] [13:14.72] it.
[L397] [13:15.52] >> You can imagine that the lab that is
[L398] [13:18.96] first to get to scale will be the first
[L399] [13:22.16] to break out there. There may be this
[L400] [13:24.48] exponential growth effect where once you
[L401] [13:27.12] deploy deployment helps you grow faster
[L402] [13:29.44] and growing faster helps you deploy and
[L403] [13:31.84] you know this this flywheel and so do
[L404] [13:35.04] you uh believe that that will happen in
[L405] [13:37.92] this industry where one lab whether in
[L406] [13:40.80] US or China will hit some breakout point
[L407] [13:44.00] and they'll kind of jump everyone else.
[L408] [13:47.36] >> There is a lot of um uh truth to that. I
[L409] [13:50.40] think that there's an important detail
[L410] [13:51.84] to keep in mind. Um the detail is that
[L411] [13:55.12] um you kind of have to like scale the
[L412] [13:56.48] right thing. Um so I think that
[L413] [13:59.68] basically the statement that like the
[L414] [14:02.80] way that I would phrase this is
[L415] [14:05.60] having an effective um positive feedback
[L416] [14:08.88] loop where more deployed robots
[L417] [14:11.20] translates to more model capability.
[L418] [14:13.36] That's kind of the key. Uh and like that
[L419] [14:16.16] that makes total sense. the the trick is
[L420] [14:19.84] that there are lots of ways that um that
[L421] [14:22.56] it can be done wrong. So, I'll tell you
[L422] [14:24.32] like a few obvious ones. Like one
[L423] [14:25.52] obvious one is um let's say that uh I um
[L424] [14:29.84] you know I'm a car company and I have a
[L425] [14:32.08] robotic arm that is welding cars and
[L426] [14:34.64] it's like there on the uh on the
[L427] [14:36.40] assembly line and it welds cars every
[L428] [14:38.32] day and it gets like you know a million
[L429] [14:39.68] welds every month and so on.
[L430] [14:42.80] If I just use that as my data flywheel,
[L431] [14:45.84] I'm unlikely to get something more
[L432] [14:47.44] capable than a robot that welds cars.
[L433] [14:49.44] So, since the robot is already there and
[L434] [14:51.12] it's already welding cars, like
[L435] [14:52.16] presumably the marginal improvement for
[L436] [14:53.44] that is not all that valuable. So,
[L437] [14:55.84] that's an example of how you kind of
[L438] [14:57.04] have to like scale the right thing
[L439] [14:58.48] because data is not like um it's not
[L440] [15:01.12] quite as funible like it's not like uh
[L441] [15:03.20] electricity or oil. You can't just like
[L442] [15:04.80] buy more of it. It has to be
[L443] [15:05.68] heterogeneous. So I I think that
[L444] [15:08.08] basically it's right but you have to
[L445] [15:09.44] scale the right thing with the right
[L446] [15:10.64] technology and the right kind of source
[L447] [15:12.56] of diverse learning like data is more
[L448] [15:15.04] like an education program for your robot
[L449] [15:16.96] than it is a funible commodity.
[L450] [15:19.44] >> If you think about that data flywheel
[L451] [15:22.16] and I guess putting out the the proper
[L452] [15:24.72] platform that would generate data that
[L453] [15:26.88] matters that would then improve that
[L454] [15:28.40] platform. When do you first see this
[L455] [15:32.00] kind of happening in the world? I think
[L456] [15:34.72] on the technology side like things are
[L457] [15:36.64] advancing very rapidly towards that and
[L458] [15:38.88] I think that maybe um a particular
[L459] [15:40.72] balancing act to strike that would
[L460] [15:42.40] significantly determine that timeline is
[L461] [15:44.88] kind of how much structure somebody's
[L462] [15:47.12] willing to admit. So, you know, on the
[L463] [15:49.04] one on the one extreme, you could
[L464] [15:51.04] imagine like jumping straight to fully
[L465] [15:52.88] unstructured deployment domains like
[L466] [15:54.48] home robots and that could be really
[L467] [15:56.16] exciting because then you have a lot of
[L468] [15:57.68] diversity like right off the bat, but
[L469] [15:59.68] the bar is a lot higher to uh be
[L470] [16:02.08] effective enough in that domain to be
[L471] [16:03.68] safe enough like you know safety is much
[L472] [16:05.04] bigger issue there because it's around
[L473] [16:07.04] um uh people in their home. On the other
[L474] [16:09.92] extreme, you could imagine much more
[L475] [16:11.60] structured tasks. Maybe not quite the
[L476] [16:13.12] welding robot, but sort of like, you
[L477] [16:14.80] know, maybe the robot down the hall that
[L478] [16:16.72] does something more unstructured, right?
[L479] [16:18.32] And that could be a much easier domain
[L480] [16:20.00] in the sense that there's much less uh
[L481] [16:21.84] safety concerns because it might be
[L482] [16:23.44] around trained uh humans. Uh the task
[L483] [16:26.56] might be more uh predictable and so on,
[L484] [16:28.64] but there is uh um the marginal value of
[L485] [16:32.64] each bit of data you get in that domain
[L486] [16:34.00] is lower because there's less variety.
[L487] [16:35.76] Um, so it's like you could take off
[L488] [16:37.52] earlier but with a smaller slope or
[L489] [16:39.20] later but with a larger slope. And you
[L490] [16:40.88] kind of have to like calibrate that. But
[L491] [16:42.56] my sense is that whichever end of that
[L492] [16:44.40] extreme we're talking about, it's in the
[L493] [16:47.20] uh singledigit years rather than the
[L494] [16:48.88] double digit years at this point. So it
[L495] [16:51.12] could be that the more structured ones
[L496] [16:52.40] might be happening like now or next
[L497] [16:54.40] year. The less structured ones might be
[L498] [16:56.00] a few more years out, but probably not
[L499] [16:58.00] like a decade.
[L500] [16:59.44] >> A lot of people talk about timelines and
[L501] [17:01.28] it's kind of more uh nebulous. And I'm
[L502] [17:04.32] I'm wondering if if you were to put down
[L503] [17:06.96] a I guess somewhat of a road map, but
[L504] [17:09.44] not so concrete, but just milestones
[L505] [17:12.48] towards that north star of
[L506] [17:15.12] >> robot in my home doing.
[L507] [17:16.72] >> Yeah. Yeah, that's a really good
[L508] [17:18.00] question. So um maybe to to preface this
[L509] [17:21.84] answer, I think that there's one thing
[L510] [17:23.36] that is very important to say about
[L511] [17:25.28] robotics that is very easy to miss um
[L512] [17:28.72] from kind of like I guess like the hype
[L513] [17:30.64] cycle and the demos that people put out,
[L514] [17:32.40] which is that the the hard thing in
[L515] [17:34.48] robotics was always um generalization.
[L516] [17:38.72] But when somebody shows a demonstration
[L517] [17:41.04] of their system, you know, the
[L518] [17:43.12] demonstration alone usually doesn't make
[L519] [17:45.76] it clear what level of generalization is
[L520] [17:47.52] being shown. the uh highly acrobatic
[L521] [17:50.40] robot demos for example are really
[L522] [17:51.92] exciting to look at. But typically if
[L523] [17:53.76] it's uh something that is like a little
[L524] [17:55.68] bit more staged like sometimes it's
[L525] [17:57.12] literally on stage if it's like a show
[L526] [17:58.48] like you know that that is obviously
[L527] [18:01.12] like rehearsed and that's okay because
[L528] [18:02.96] it's like literally just a show but it's
[L529] [18:05.12] not the same as doing a task every time
[L530] [18:08.40] reliably in any home. And the
[L531] [18:12.16] generalization piece often doesn't look
[L532] [18:15.60] that impressive when viewed in isolation
[L533] [18:17.36] because generalization is sort of a
[L534] [18:18.56] property of many trials, not of one
[L535] [18:20.40] trial. So you might see the robot doing
[L536] [18:22.00] something fairly mundane and
[L537] [18:23.92] unimpressive. But what's exciting about
[L538] [18:25.84] it is that it's doing with an object
[L539] [18:27.44] that it's never seen before in an
[L540] [18:29.20] environment that has never been tested
[L541] [18:30.48] in before. And that's actually harder
[L542] [18:32.40] than like doing a acrobatic backflip
[L543] [18:34.72] that it's practiced like a millions of
[L544] [18:37.12] times. So um with that said uh my answer
[L545] [18:41.44] to your question is that the road map is
[L546] [18:44.00] all about both achieving better
[L547] [18:46.00] generalization and uh kind of that
[L548] [18:48.64] second order effect of having a
[L549] [18:50.16] mechanism to get more generalization as
[L550] [18:52.48] you generalize. So one of the steps on
[L551] [18:54.96] that road map is to have a very concrete
[L552] [18:58.40] demonstration of a robotic system that
[L553] [19:00.88] gets better with autonomous experience
[L554] [19:03.36] that is collected in in a setting that
[L555] [19:06.80] it wasn't originally trained for. So I I
[L556] [19:09.52] do whatever I do on on on the back end,
[L557] [19:11.36] you know, in the lab in and whatever. I
[L558] [19:13.44] get my model, I get my uh adaptation
[L559] [19:15.60] algorithm, I put it in a new setting.
[L560] [19:18.80] Maybe it's a home, maybe it's a factor,
[L561] [19:20.16] whatever it is, something where it's
[L562] [19:21.28] doing something real. uh and it does
[L563] [19:23.68] okay, but then over time it gets better
[L564] [19:25.68] and better and it gets better and better
[L565] [19:27.92] to the point where it reaches sort of
[L566] [19:30.16] practically relevant levels of
[L567] [19:31.36] robustness without sort of capping out
[L568] [19:33.04] at like 50%. Like that I think would be
[L569] [19:35.04] a major milestone. Uh because now that
[L570] [19:37.44] that says okay if this is truly an
[L571] [19:39.20] automated process, it's improving, it's
[L572] [19:40.80] getting better even as it's collecting
[L573] [19:42.56] useful experience. Now I can take it and
[L574] [19:44.16] I can put it in lots of different
[L575] [19:45.52] domains, collect useful experience, do
[L576] [19:47.68] something that people actually want and
[L577] [19:49.60] it'll improve the model. So that I think
[L578] [19:51.84] is a really major step uh on that road.
[L579] [19:54.56] I think another really major step is to
[L580] [19:57.36] demonstrate a very concrete and
[L581] [20:01.12] practically useful way to transfer
[L582] [20:03.92] knowledge to transfer common sense to
[L583] [20:05.92] achieve robustness. So that's like the u
[L584] [20:08.88] kind of the the other scenario where you
[L585] [20:10.40] don't get to practice. If you're driving
[L586] [20:11.52] your car on the road and you see a fire
[L587] [20:13.04] truck and you see like a bunch of
[L588] [20:14.40] traffic cones, even if you've never been
[L589] [20:16.16] in that situation before, like your
[L590] [20:17.68] common sense tells you like, "Hey, I
[L591] [20:19.12] should like slow down." like what what
[L592] [20:20.56] maybe I don't know how to react
[L593] [20:21.52] optimally, but I shouldn't just like
[L594] [20:22.64] barrel on through the cones and like you
[L595] [20:24.56] know uh upset the firefighters and so
[L596] [20:26.48] on. Like so that's common sense. And if
[L597] [20:28.32] you can apply that common sense to
[L598] [20:30.64] effectively recover from unexpected
[L599] [20:32.48] situations like when the robot put the
[L600] [20:34.48] spatula in the oven like you know it
[L601] [20:36.24] should probably open it up, take it out
[L602] [20:37.84] like it knows that this is not the thing
[L603] [20:39.44] you do semantically. That I think is
[L604] [20:41.36] like another important step because that
[L605] [20:42.72] tells us that we can use common sense to
[L606] [20:44.88] fix mistakes. I could imagine um a more
[L607] [20:48.56] narrowly scoped robot. Let's say it's a
[L608] [20:51.28] humanoid robot. That's one step in
[L609] [20:54.88] assembly line in manufacturing. In my
[L610] [20:57.52] understanding, you're less interested in
[L611] [20:59.12] that because that's not really a step
[L612] [21:01.36] towards that general intelligence. What
[L613] [21:03.92] I would say, it's not that I'm less
[L614] [21:05.52] interested in it. It's that um I think
[L615] [21:08.00] that the real world has these leaky
[L616] [21:10.64] abstractions that make that kind of
[L617] [21:12.80] stuff a lot more complex than it seems.
[L618] [21:15.92] Um let me try to explain this with an
[L619] [21:17.92] analogy. So in the in the '9s um when
[L620] [21:21.44] people were like really started working
[L621] [21:24.00] uh kind of full steam on autonomous
[L622] [21:25.52] driving, there was this idea that we
[L623] [21:27.36] could avoid a lot of the hard problems
[L624] [21:29.20] by kind of instrumenting the environment
[L625] [21:30.96] a little bit. like we'll have like
[L626] [21:32.00] magnetic sensors along the highway and
[L627] [21:33.84] so on. And cars will have like a little
[L628] [21:36.40] uh you know uh sensor on them and a
[L629] [21:38.64] little um transmitter so they can tell
[L630] [21:40.80] where each of the cars are. Kind of like
[L631] [21:42.56] the way you do it with aircraft
[L632] [21:43.92] basically. Uh and then people thought
[L633] [21:45.52] well we don't really need like fancy AI.
[L634] [21:47.20] We'll just like have these sensors and
[L635] [21:48.56] and it'll just work. And that just
[L636] [21:50.48] basically didn't go anywhere because the
[L637] [21:53.12] real world has so many messy exceptions
[L638] [21:55.36] and special cases that even if 99% of
[L639] [21:57.20] the time like the magnetic sensors and
[L640] [21:58.64] all that stuff just allow the car to
[L641] [21:59.92] drive, the 1% when like someone steps in
[L642] [22:02.16] the middle of the road or there's like a
[L643] [22:03.44] piece of trash or whatever, it just
[L644] [22:04.96] messes everything up. So the thing that
[L645] [22:07.52] actually worked was when said like,
[L646] [22:09.84] "Hey, we're going to not try to avoid
[L647] [22:11.68] the hard problem. we're going to
[L648] [22:12.64] actually try to deploy our cars not in
[L649] [22:14.64] like middle of nowhere but in San
[L650] [22:16.00] Francisco like very messy and let's just
[L651] [22:18.40] let's just deal with it head-on and that
[L652] [22:20.48] allowed the that community to make
[L653] [22:22.88] progress and I think robotic
[L654] [22:24.40] manipulation is going to be the same way
[L655] [22:25.52] that that um past the fully structured
[L656] [22:29.60] world of the factory if you want to go
[L657] [22:30.88] even a little bit outside of that even
[L658] [22:32.72] if 99% of the time it's all like pretty
[L659] [22:34.88] straightforward that 1% when something
[L660] [22:36.48] weird happens means that you really need
[L661] [22:38.24] to the full scope of the problem
[L662] [22:39.68] basically to be addressed. This kind of
[L663] [22:41.84] reminds me I remember Figure had this
[L664] [22:43.84] demo where they live streamed the robot
[L665] [22:46.32] kind of sorting packages when you
[L666] [22:48.64] watched that demo. Is that a did is does
[L667] [22:51.44] it demonstrate generalization in your
[L668] [22:53.92] opinion?
[L669] [22:54.64] >> Yeah. Yeah, I think it does. And by the
[L670] [22:57.04] way, this is something that I find very
[L671] [22:58.16] encouraging is that like I mentioned
[L672] [23:00.00] that it's hard to show generalization in
[L673] [23:01.76] a video. And it's clear that lots of
[L674] [23:03.04] people are thinking about that and that
[L675] [23:04.24] are thinking about how do you like how
[L676] [23:07.12] do you present something that that
[L677] [23:09.36] somebody can watch and take in kind of
[L678] [23:11.92] at a glance what generalization is. I
[L679] [23:14.00] think you can see a lot of creative
[L680] [23:15.44] steps towards that. Live demos, these
[L681] [23:17.36] kind of like really long time lapses. I
[L682] [23:19.28] think it's a great idea and I think
[L683] [23:20.32] that's a like a a really nice way to
[L684] [23:22.96] move towards elevating the importance of
[L685] [23:25.60] generalization in people's kind of
[L686] [23:27.52] conscious consciousness. Um you know we
[L687] [23:30.40] um when we were working on the um the PI
[L688] [23:33.52] star 6 project the RL project that we
[L689] [23:35.36] did uh late last year we um wanted to do
[L690] [23:39.44] some longer uh horizon experiments. In
[L691] [23:42.80] some case it's obvious like we had our
[L692] [23:44.08] robot assembling boxes at at Dandelion
[L693] [23:45.84] Chocolate Factory. So they're like, you
[L694] [23:47.12] know, it's an actual chocolate factory,
[L695] [23:48.24] so they need the boxes. So we run it for
[L696] [23:50.08] several days. Uh but we had this coffee
[L697] [23:52.16] task which was uh the robot was using an
[L698] [23:54.72] espresso machine to make espresso. So
[L699] [23:56.48] what we did is we ran it for 13 hours
[L700] [23:58.16] making espresso drinks. Uh and we are,
[L701] [24:00.72] you know, we tried to be like very uh I
[L702] [24:02.56] guess um environmentally conscious about
[L703] [24:04.32] this. So we didn't want to like throw
[L704] [24:05.36] out the coffee. So after 13 hours,
[L705] [24:06.80] everyone in the office was like a little
[L706] [24:08.64] wiry cuz someone has to like drink the
[L707] [24:11.04] coffee. But it like it ran for 13 hours
[L708] [24:13.28] and it was pretty cool. But it it
[L709] [24:14.56] screwed up a few times. Like it'll um
[L710] [24:16.48] spill all the the coffee grounds and
[L711] [24:18.24] then it needs to go and get like a cloth
[L712] [24:19.68] and wipe it down. But like it does it
[L713] [24:21.76] and it's you know nothing exploded 13
[L714] [24:23.84] hours went by. Probably the most
[L715] [24:25.76] negative consequence was like loss of
[L716] [24:27.84] sleep from too much caffeination.
[L717] [24:29.60] >> But when it spills the coffee grounds
[L718] [24:31.20] and cleans it up is that's it did that
[L719] [24:33.84] by itself.
[L720] [24:34.80] >> Well, so the way the way that that
[L721] [24:36.48] experiment was done is that there is a
[L722] [24:38.16] high level prompting. So like roughly
[L723] [24:40.16] the prompt is updated maybe every like
[L724] [24:42.00] uh 5 minutes or so like in between
[L725] [24:44.72] semantically coherent tasks. So you tell
[L726] [24:46.48] it like make espresso, clean up the
[L727] [24:48.24] machine etc. So those steps the actual
[L728] [24:50.72] like clean up the the machine was
[L729] [24:52.24] commanded by a person. Um in principle
[L730] [24:54.72] we could automate that. In fact one of
[L731] [24:55.92] the things we're spending a lot of
[L732] [24:57.20] effort now is improving our high level
[L733] [24:58.56] policy that does those commands. But for
[L734] [25:00.24] that experiment yeah like every 5
[L735] [25:01.44] minutes somebody basically updates what
[L736] [25:02.88] is being asked to do. Like the way we
[L737] [25:04.56] intended it was like the commands would
[L738] [25:06.24] be like if you go to to an actual coffee
[L739] [25:07.84] shop, you say like, "Oh, I want a latte.
[L740] [25:09.36] I want an espresso." Like that was
[L741] [25:10.48] supposed to be the prompt. Except then
[L742] [25:12.00] you also have to tell it, "I want you to
[L743] [25:13.12] clean it up before you do the next one."
[L744] [25:15.03] [laughter]
[L745] [25:15.92] >> That makes sense. Open AAI, Enthropic,
[L746] [25:19.28] Cursor, and Versel all use this product
[L747] [25:22.16] to make their lives better. And the
[L748] [25:24.24] problem it solves is when you're
[L749] [25:25.92] building SAS or an AI product and you
[L750] [25:28.48] want to sell to other companies, there's
[L751] [25:30.32] all these requirements you need to meet.
[L752] [25:32.40] There's SSO, there's SKIM, there's
[L753] [25:35.04] arbback, there's audit logs. These are
[L754] [25:37.44] all things that take time to integrate
[L755] [25:39.44] but aren't the main focus of your app.
[L756] [25:41.44] Work OS is an API layer that lets you
[L757] [25:43.60] meet all of these requirements in just a
[L758] [25:45.84] few lines of code. So, let's say you
[L759] [25:47.76] have a new SAS product and you want to
[L760] [25:49.68] sell to other companies. Work OS will
[L761] [25:51.92] solve all of these critical feature gaps
[L762] [25:53.84] for you. You can check them out at
[L763] [25:56.32] workos.com to learn more and get
[L764] [25:58.64] started. and I appreciate them for
[L765] [26:00.80] supporting my work and sponsoring this
[L766] [26:02.48] podcast. It sounds like on the way to
[L767] [26:05.92] generalizing
[L768] [26:07.44] uh data is a very important part of that
[L769] [26:10.40] and I was reading there's different
[L770] [26:11.60] types of data there's simulated data you
[L771] [26:14.72] could uh collect like physical
[L772] [26:16.96] interactive data and I wanted to hear
[L773] [26:20.16] your take on what's the best data to get
[L774] [26:22.72] what's the worst and what are the pros
[L775] [26:24.48] and cons. Uh this is by the way like a
[L776] [26:26.88] question that is uh I guess quite like
[L777] [26:30.00] there's a lot of discussion in the
[L778] [26:31.04] robotics community about this question
[L779] [26:32.48] and some people have like very opposite
[L780] [26:35.12] opinions on it. My own take on this is
[L781] [26:38.24] that um a lot of different data sources
[L782] [26:42.40] are easier for the model to internalize
[L783] [26:44.72] if it can ground them in a thorough
[L784] [26:47.44] physical understanding of the world. So
[L785] [26:49.52] uh let me try to explain what I mean
[L786] [26:50.72] with like a few examples. Um, if you
[L787] [26:54.00] want to learn to fly an airplane, you
[L788] [26:56.24] will probably use a a simulator, at
[L789] [26:58.32] least during part of your training. Uh,
[L790] [27:01.12] but the simulator makes a lot of sense
[L791] [27:03.52] to you because when you start using the
[L792] [27:05.68] simulator, you have a lot of world
[L793] [27:07.52] knowledge that you can use to ground
[L794] [27:09.28] what's going on. Like you know that when
[L795] [27:11.12] you uh are using the flight simulator to
[L796] [27:13.28] learn how to fly the airplane, you're
[L797] [27:14.48] not just like playing a video game.
[L798] [27:15.76] You're trying to acquire knowledge that
[L799] [27:17.36] will then that you will then use with a
[L800] [27:18.72] real airplane. and you understand that
[L801] [27:20.40] there's sort of an abstraction there.
[L802] [27:22.88] Same thing if you um uh if you're
[L803] [27:25.60] playing like a really cartoony like you
[L804] [27:27.68] know Atari game or something right like
[L805] [27:29.36] you know that all the symbols on the
[L806] [27:30.88] screen you can sort of connect them to
[L807] [27:32.56] things that you've experienced in your
[L808] [27:34.00] life and you can make an analogy there.
[L809] [27:35.84] So, a lot of that, like even though it
[L810] [27:38.64] kind of seems like these simulated
[L811] [27:40.08] environments reflect aspects of the real
[L812] [27:42.24] world, to us, they make a lot of sense
[L813] [27:44.08] because we kind of bring to bear a lot
[L814] [27:46.08] of our own prior experience and we fill
[L815] [27:48.00] in the blanks that that the that the
[L816] [27:50.00] that the simulation has. Um, and also if
[L817] [27:53.60] you if you want to use uh data uh you
[L818] [27:56.64] yourself as a person of somebody else
[L819] [27:58.72] doing something, if you you watch
[L820] [28:00.00] someone uh let's say cooking a meal,
[L821] [28:01.76] right? Um, even though you don't
[L822] [28:04.48] experience every movement they're
[L823] [28:05.84] experiencing, you have a lot of that
[L824] [28:07.20] knowledge that you bring to bear and
[L825] [28:08.24] you're like, "Okay, I see they're
[L826] [28:09.12] picking up the salt shaker. Like, I've
[L827] [28:10.48] put salt on things before, so I kind of
[L828] [28:11.84] roughly know what's going on there." And
[L829] [28:13.28] I can file it away at this level
[L830] [28:14.88] abstraction of like add salt without
[L831] [28:16.96] having to like figure out all their
[L832] [28:18.56] muscle movements. So my point with this
[L833] [28:20.40] is that once you have that understanding
[L834] [28:22.48] of how you do things physically with
[L835] [28:23.84] your own body and how you experience the
[L836] [28:25.60] physical world, now all these other
[L837] [28:27.20] sources of knowledge can be connected up
[L838] [28:28.64] to it because that foundation you get
[L839] [28:31.44] from your experience helps you ground
[L840] [28:33.20] everything. So where I'm going with this
[L841] [28:35.44] is that if we have a robotic foundation
[L842] [28:37.84] model that is trained on lots of real
[L843] [28:40.56] embodied data that provides that
[L844] [28:42.08] grounding, it might actually be much
[L845] [28:43.68] better able to absorb other sources of
[L846] [28:45.52] knowledge. And this is actually like a
[L847] [28:47.60] little bit upside down relative to how
[L848] [28:49.12] some people think about it because it's
[L849] [28:50.56] very tempting looking at the success of
[L850] [28:52.80] like internet data for LLMs to say well
[L851] [28:55.44] maybe we should do the opposite. Maybe
[L852] [28:56.80] we should like start with like YouTube
[L853] [28:58.24] videos and then put robot data on top of
[L854] [29:00.16] that. But I think it's actually the
[L855] [29:01.76] other way around. And I actually I even
[L856] [29:03.36] have like a little bit of evidence for
[L857] [29:04.48] this. So my um my colleague uh sir Saraj
[L858] [29:08.16] together with um uh Simar from Georgia
[L859] [29:11.76] Tech they had a project together uh a
[L860] [29:13.92] while back where they took our robot
[L861] [29:16.40] foundation model and they added human
[L862] [29:18.72] video data but they they didn't start
[L863] [29:21.84] with human video data. They actually
[L864] [29:22.96] started with a model train on robot data
[L865] [29:24.40] and then added video data on top of it.
[L866] [29:26.24] And what they did is they looked at the
[L867] [29:27.68] representations inside the model. Uh
[L868] [29:29.52] basically how does the model represent
[L869] [29:31.04] human experience versus robot
[L870] [29:32.56] experience? And they found that if you
[L871] [29:34.80] use a small model with a small amount of
[L872] [29:36.56] robot data, predictably the human
[L873] [29:38.24] experience and the robot experience are
[L874] [29:40.00] fully separated. Meaning that the
[L875] [29:41.28] feature representations are different.
[L876] [29:43.12] But if you train on lots of robot data
[L877] [29:44.88] from lots of different robots, then the
[L878] [29:47.44] features are grouped much more by what
[L879] [29:49.12] task is being done rather than by
[L880] [29:50.88] whether it's a human or a robot. And
[L881] [29:52.96] like when we looked at the feature
[L882] [29:54.24] plots, it was just like mindboggling
[L883] [29:55.84] because we literally when you when you
[L884] [29:57.76] crank up the amount of robot data to
[L885] [29:58.96] 100%, they just line up perfectly. like
[L886] [30:01.28] you you see the you know you do this TC
[L887] [30:03.36] embedding you see the shapes of the
[L888] [30:04.56] embeddings and it's just all task
[L889] [30:07.20] identity and like minimal sensitivity to
[L890] [30:09.44] embodiment and to me that's kind of
[L891] [30:11.44] mind-blowing because like this the base
[L892] [30:13.28] model wasn't trained on any human data
[L893] [30:14.72] at all but once you start adding human
[L894] [30:16.56] data it represents it exactly the same
[L895] [30:18.72] way and I think that's really exciting
[L896] [30:20.96] and I think that that to me is like one
[L897] [30:22.56] one of the strongest indicators that if
[L898] [30:24.24] you have that good foundation of robot
[L899] [30:25.76] experience you can put everything else
[L900] [30:27.28] on top of it and it's actually better at
[L901] [30:28.48] absorbing that
[L902] [30:29.68] >> is it important that that base model has
[L903] [30:33.12] data that was collected using that
[L904] [30:35.60] specific set of motors, specific set of
[L905] [30:37.84] joints. So far, we've uh obviously put a
[L906] [30:42.08] lot of effort into cross embodyment
[L907] [30:43.36] models that can handle many different
[L908] [30:44.56] robot types, but generally you do need
[L909] [30:47.44] data of the robot you're going to be
[L910] [30:48.72] deploying on to get good performance. Uh
[L911] [30:51.68] so kind of the metric of uh of
[L912] [30:53.84] generalization there is not can you zero
[L913] [30:55.52] shot a new robot but it's mostly can you
[L914] [30:57.84] get away with less experience from the
[L915] [30:59.84] new robot and transfer skills from other
[L916] [31:01.60] robots. Okay so that's the current state
[L917] [31:03.36] of things. Now there is a little bit of
[L918] [31:05.04] a kind of surprisingly positive read on
[L919] [31:07.60] that which is even though you need data
[L920] [31:09.76] from these robots um the amount of
[L921] [31:12.56] special stuff that the model is doing is
[L922] [31:15.12] uh kind of minimal. Like when we started
[L923] [31:17.60] doing all of this, I had like a big long
[L924] [31:19.68] list of all the cool research I wanted
[L925] [31:21.36] to do to better accommodate different
[L926] [31:22.64] morphologies like can you like
[L927] [31:24.64] factoriize the model's representation in
[L928] [31:26.80] some way so that there's like a you know
[L929] [31:28.72] a six degree of freedom arm head and a
[L930] [31:30.88] seven degree head and a gripper head
[L931] [31:32.40] etc. We didn't do any of that like we
[L932] [31:33.76] the model just outputs like a big vector
[L933] [31:35.28] of numbers. Uh if the robot has less
[L934] [31:37.44] degrees of freedom than the number it
[L935] [31:39.04] outputs it just zero pads it. There's
[L936] [31:40.56] just like nothing fancy. Uh and that's
[L937] [31:42.96] it. and then it just train on all the
[L938] [31:44.40] robots and outputs the correct actions
[L939] [31:47.04] based on what is seeing through the
[L940] [31:48.08] camera essentially.
[L941] [31:49.84] But now to to your point about whether
[L942] [31:51.68] you can uh handle new robots. Um so so
[L943] [31:56.32] far the thing that we focused on and I
[L944] [31:58.40] think this is showing some promise is to
[L945] [32:01.76] be able to transfer skills between
[L946] [32:03.36] robots and this is actually where
[L947] [32:07.52] the um particular choices in how the
[L948] [32:10.00] model works uh seem to matter. Um for
[L949] [32:13.68] example uh you can have a model that
[L950] [32:17.68] does some intermediate thinking and that
[L951] [32:20.48] thinking can be done in different
[L952] [32:21.52] modalities. So you can think in text and
[L953] [32:23.28] thinking in text is really good for
[L954] [32:24.80] transferring um highle behavioral
[L955] [32:27.12] structure. So that's basically how you
[L956] [32:29.52] understand that hey if I want to like
[L957] [32:31.20] clean the kitchen and put away like the
[L958] [32:33.28] silverware first open the drawer like
[L959] [32:34.88] that's kind of a semantic inference and
[L960] [32:36.08] you can transfer that uh very well
[L961] [32:38.00] because obviously that's like largely
[L962] [32:39.20] agnostic to any embodiment or anything
[L963] [32:40.64] like that. But even lower level things
[L964] [32:42.64] can be transferred if you use the right
[L965] [32:44.64] representation. So one experiment we did
[L966] [32:46.64] is we had a a thinking stage that is
[L967] [32:49.76] expressed in images where you basically
[L968] [32:51.92] like dream up an image of the next
[L969] [32:54.16] milestone in the task. And with that, we
[L970] [32:56.88] could actually get um a robot, the UR5
[L971] [33:00.00] robot to fold a t-shirt, even though we
[L972] [33:02.16] didn't have any t-shirt folding data on
[L973] [33:03.44] the UR5 because while getting the the
[L974] [33:05.52] the arm motions correct is very hard
[L975] [33:07.68] because the robot basically requires
[L976] [33:09.04] very different joint angles to do the
[L977] [33:10.40] task, uh cooking up an image of what it
[L978] [33:12.64] looks like for it to fold a shirt is not
[L979] [33:14.32] that hard because like you've seen the
[L980] [33:15.44] robot arm in all sorts of different
[L981] [33:16.56] poses. You've seen the shirt in all
[L982] [33:18.40] different stages of being folded and
[L983] [33:19.52] unfolded. You know roughly where it
[L984] [33:20.72] should hold it. So getting a good
[L985] [33:22.56] generative model to cook up that image
[L986] [33:24.08] is pretty straightforward. And once you
[L987] [33:25.84] have the image then from that backing
[L988] [33:28.08] out the correct actions is easy too
[L989] [33:30.08] because you can just look at the
[L990] [33:31.36] synthesized arm angle and just like back
[L991] [33:33.44] out what the angle should be. So it it's
[L992] [33:36.16] it's not changing the problem but it's
[L993] [33:37.84] just introducing this intermediate step
[L994] [33:39.84] that makes it easier to solve. Just like
[L995] [33:41.52] if you're solving a math problem if you
[L996] [33:42.96] figure out like the right intermediate
[L997] [33:44.80] step kind of the answer is obvious from
[L998] [33:46.56] that intermediate step. And I think
[L999] [33:48.32] that's really exciting because now now
[L1000] [33:49.76] that shows that this level of
[L1001] [33:51.36] generalization across robots and I'm
[L1002] [33:53.28] sure other generalization too can be
[L1003] [33:54.56] facilitated with thinking just like an
[L1004] [33:56.56] LLMs but with a twist. You have to think
[L1005] [33:58.72] in the right modality.
[L1006] [34:00.56] >> Interesting. So it it outputs a I guess
[L1007] [34:03.12] that image is what its video sensor is
[L1008] [34:07.44] seeing and it's like the next step.
[L1009] [34:09.84] >> Yeah. You can almost think of it like
[L1010] [34:10.88] image editing. You can do the same thing
[L1011] [34:12.56] with video. You can do it with video
[L1012] [34:13.76] prediction. But the key is to like
[L1013] [34:15.36] imagine what it would look like to
[L1014] [34:18.08] progress on this task. Like that seems
[L1015] [34:20.32] like a very human thing to do, right?
[L1016] [34:21.84] You know, some things you can you you
[L1017] [34:23.68] plan semantically and some things you
[L1018] [34:25.76] plan spatially. Like if you're doing
[L1019] [34:27.28] rock climbing, you're probably not
[L1020] [34:28.64] thinking like, hey, left arm to rock 37
[L1021] [34:31.28] cm to the left. You're probably more
[L1022] [34:32.56] like imagining your arm reaching for the
[L1023] [34:34.08] rock. Earlier in the conversation, you
[L1024] [34:36.48] mentioned that Whimo was very inspiring
[L1025] [34:40.32] and um you know their kind of path to
[L1026] [34:43.84] productionization is proof that you can
[L1027] [34:45.84] do real world generalized robotics. And
[L1028] [34:49.68] if I recall correctly when I was, you
[L1029] [34:52.48] know, a lot younger, it was kind of this
[L1030] [34:54.96] early promise of this is going to happen
[L1031] [34:58.16] and then in reality it took a lot
[L1032] [35:01.04] longer. And so I guess my question is in
[L1033] [35:04.72] the case of humanoid robotics,
[L1034] [35:07.60] what would make you say singledigit
[L1035] [35:10.32] years it's coming versus a long tail and
[L1036] [35:14.16] you know policy challenges as well. I
[L1037] [35:16.08] could imagine.
[L1038] [35:17.28] >> I think one big difference between how
[L1039] [35:21.04] robotic foundation models address the
[L1040] [35:22.96] problem and how more traditional
[L1041] [35:24.56] engineered systems address the problem
[L1042] [35:26.00] is that the stack is really thin. So
[L1043] [35:28.40] it's not easy to train a foundation
[L1044] [35:30.08] model. You need to uh obviously you need
[L1045] [35:32.08] to get the right data. There's a lot of
[L1046] [35:33.36] work that goes into curating, labeling,
[L1047] [35:35.12] all that other kind of stuff. But the
[L1048] [35:36.88] actual software that runs on the robot
[L1049] [35:40.08] is very very simple. Uh so uh you know
[L1050] [35:43.52] you might have some kind of thinking or
[L1051] [35:45.04] reasoning stage. You might have uh you
[L1052] [35:47.68] might have the model produce actions. It
[L1053] [35:49.44] needs to be fast enough. But the like
[L1054] [35:52.56] just if you think about in terms of raw
[L1055] [35:54.16] lines of code, it's much much lower than
[L1056] [35:57.52] a more traditional AV stack. Uh and you
[L1057] [36:01.60] know, partly that's because modern
[L1058] [36:05.36] autonomous vehicles, the work on that
[L1059] [36:07.20] started a lot earlier with very
[L1060] [36:08.48] different technologies and evolved over
[L1061] [36:10.00] time. Partly it's also because the
[L1062] [36:12.08] problem is more safety critical. Like
[L1063] [36:13.84] yes, you don't want uh a robotic
[L1064] [36:15.60] manipulator to like drop a fragile
[L1065] [36:17.52] object, but at the end of the day,
[L1066] [36:19.76] that's a lot less bad than having a car
[L1067] [36:22.08] hit somebody. So that is not to say that
[L1068] [36:24.56] the safety challenges with robots are uh
[L1069] [36:28.16] are not real. They're very real and it's
[L1070] [36:29.84] very important to tackle them. In fact,
[L1071] [36:30.96] it's probably one of the harder ends of
[L1072] [36:32.48] the problem. But they are not as much of
[L1073] [36:35.36] a hard stop to practical deployments
[L1074] [36:39.28] because you can come up with tasks and
[L1075] [36:41.68] environments and domains and also
[L1076] [36:43.04] physical hardware where those problems
[L1077] [36:44.88] are a lot less uh severe. So uh I think
[L1078] [36:48.56] that that that combination radically
[L1079] [36:50.96] simpler software stack plus uh less uh
[L1080] [36:55.04] drastic software challenges I think
[L1081] [36:56.64] actually make it a lot easier and
[L1082] [36:58.08] because you know to your earlier point
[L1083] [37:00.16] uh that there is this kind of flywheel
[L1084] [37:01.68] effect that there's a positive feedback
[L1085] [37:03.04] loop that uh you know starting to get
[L1086] [37:05.28] things out in the world even under some
[L1087] [37:06.96] constraints will actually facilitate
[L1088] [37:08.72] getting them out more and more. I think
[L1089] [37:10.72] a lot of people are familiar with this
[L1090] [37:12.24] idea of a post-mortem,
[L1091] [37:14.72] you know, looking back on why something
[L1092] [37:17.04] failed. But in this case, I'm curious,
[L1093] [37:19.84] what would you say to a a premortem? And
[L1094] [37:23.04] in the sense of if humanoid robotics did
[L1095] [37:26.24] not succeed in single-digit years, what
[L1096] [37:28.96] do you think would be the most likely
[L1097] [37:30.48] reason why humanoid robotics failed?
[L1098] [37:34.48] Ultimately, for these things to to be
[L1099] [37:37.04] truly useful, they do need to reach a
[L1100] [37:39.28] level of reliability and robustness and
[L1101] [37:41.36] generalization that is higher than what
[L1102] [37:43.28] we typically expect from LLMs for
[L1103] [37:46.08] example uh or uh you know generative AI
[L1104] [37:48.88] for like images and video because
[L1105] [37:50.40] typically like these tools they are very
[L1106] [37:52.56] much human interactive tools like you
[L1107] [37:54.48] you get an LLM to do something and it
[L1108] [37:56.56] doesn't do quite what you want so you
[L1109] [37:58.00] sort of revise your prompt and you you
[L1110] [37:59.44] basically like you iterate with it and
[L1111] [38:01.12] and that's why like even the earlier um
[L1112] [38:03.92] LM tools like the first version of Chad
[L1113] [38:05.92] GPT, even though they were much more
[L1114] [38:07.84] primitive than what we have now, they
[L1115] [38:08.96] were still already useful because
[L1116] [38:10.32] somebody could just like keep hammering
[L1117] [38:11.84] out until it it basically solves their
[L1118] [38:14.00] problem. You know, just like if if
[L1119] [38:15.52] you're using a search engine, like you
[L1120] [38:16.64] type something into the search engine,
[L1121] [38:17.44] you don't get quite what you want. You
[L1122] [38:18.56] revise your query and then you get what
[L1123] [38:19.84] you want. Whereas with a robot, like the
[L1124] [38:22.48] the full value of it is unlocked when
[L1125] [38:24.24] it's actually doing the thing
[L1126] [38:25.04] autonomously. So it's it's having to
[L1127] [38:28.08] have somebody like constantly iterate
[L1128] [38:29.92] for every single task is almost like
[L1129] [38:31.36] antithetical to the benefit that you're
[L1130] [38:32.72] getting. So I think a lot of the risk
[L1131] [38:35.20] has to do with how easy is it to get
[L1132] [38:37.60] that level of reliability and
[L1133] [38:39.44] robustness. And that's again where some
[L1134] [38:41.44] of the demos might be like a little bit
[L1135] [38:42.96] misleading because if someone shows a
[L1136] [38:44.88] demo of the robot doing something cool I
[L1137] [38:46.80] mean you know obviously if if everything
[L1138] [38:48.56] is presented in a forthright way that's
[L1139] [38:50.88] that could still be very good indicator
[L1140] [38:52.08] of progress but it doesn't make it
[L1141] [38:54.40] obvious how far or how close it is to
[L1142] [38:57.52] reaching that practically relevant level
[L1143] [38:59.36] of robustness. So, I'm personally a big
[L1144] [39:02.24] believer in uh using uh techniques like
[L1145] [39:06.24] reinforcement learning that can actually
[L1146] [39:08.00] benefit from autonomous experience to
[L1147] [39:10.24] kind of fine-tune that last few
[L1148] [39:11.68] percentage points to make it go from
[L1149] [39:13.44] like 95 to actually 100%. But that's
[L1150] [39:16.16] really important and it's not yet a
[L1151] [39:17.36] solved problem.
[L1152] [39:18.48] >> If it did take longer than expected,
[L1153] [39:21.44] it's because the bar is higher. because
[L1154] [39:23.28] the bar is higher and in particular like
[L1155] [39:25.04] those last few uh the kind of the last
[L1156] [39:27.68] inch so to speak is something that
[L1157] [39:30.24] requires not just really good models but
[L1158] [39:32.56] also new innovations in technology. I
[L1159] [39:35.36] mean I don't think that you know I'm not
[L1160] [39:38.00] the kind of person that would say like
[L1161] [39:39.12] oh we should like throw out everything
[L1162] [39:40.32] that we know about foundation models and
[L1163] [39:41.60] start over. I don't think it's that at
[L1164] [39:42.56] all. I think that roughly the puzzle
[L1165] [39:44.64] pieces that we have are actually very
[L1166] [39:45.92] good puzzle pieces. But still we should
[L1167] [39:47.68] acknowledge that right now the methods
[L1168] [39:50.40] and the models need more work to cross
[L1169] [39:53.92] that level of robustness.
[L1170] [39:55.44] >> In LLMs it feels like everyone is doing
[L1171] [39:58.40] kind of the same thing but different
[L1172] [40:00.48] flavors in the robotics industry. Is it
[L1173] [40:04.48] is everyone doing kind of the same
[L1174] [40:05.92] thing? Are there any hottake
[L1175] [40:07.60] architectures that are different
[L1176] [40:09.04] direction? I actually think that there's
[L1177] [40:10.88] a lot more heterogeneity than it might
[L1178] [40:12.48] seem. Um, one big dividing line that I
[L1179] [40:15.52] think is maybe not as obvious uh from
[L1180] [40:18.56] just kind of looking at the results is
[L1181] [40:20.72] the distinction between kind of fully
[L1182] [40:23.12] embracing the foundation model ethos so
[L1183] [40:25.68] to speak versus uh focusing on spec
[L1184] [40:29.68] specific like kind of vertical areas.
[L1185] [40:32.40] And I think this is like kind of hard to
[L1186] [40:35.04] tease out sometimes because obviously
[L1187] [40:36.32] like you know everyone's going to say
[L1188] [40:37.28] like oh I'm doing the thing that LM did
[L1189] [40:39.12] like because like that's the cool thing
[L1190] [40:41.04] but you know the foundational model
[L1191] [40:42.80] ethos fundamentally is something like
[L1192] [40:45.36] this that if you have a particular
[L1193] [40:47.76] problem you want to solve it is better
[L1194] [40:49.68] to train a more general model that can
[L1195] [40:52.24] use data from a breadth of problems and
[L1196] [40:54.88] if you do it right it'll actually be
[L1197] [40:56.40] better at the specialized problem you
[L1198] [40:57.84] want to solve than a narrow specialist.
[L1199] [41:00.24] So you know to again to come back to the
[L1200] [41:01.92] LM analogy if you want to do machine
[L1201] [41:03.28] translation don't build a machine
[L1202] [41:05.12] translation system build a language
[L1203] [41:06.40] model that understands all language
[L1204] [41:08.08] tasks and then throw it at machine
[L1205] [41:09.36] translation
[L1206] [41:10.96] and in robotics I think that is like
[L1207] [41:12.48] actually very deeply uncomfortable to
[L1208] [41:14.00] people because if someone is actually
[L1209] [41:15.76] like working on an application like
[L1210] [41:17.12] they're doing like warehouse automation
[L1211] [41:18.96] it is very awkward to then to to like
[L1212] [41:21.84] think like oh if I want to do warehouse
[L1213] [41:23.76] automation let me like collect data of
[L1214] [41:25.44] like putting away silverware in
[L1215] [41:26.72] kitchens. It just it just sounds
[L1216] [41:28.40] bizarre. But that is the foundation
[L1217] [41:31.04] model lesson that if you have enough
[L1218] [41:32.40] breadth, if you collect data from a wide
[L1219] [41:34.96] range of different tasks, then you will
[L1220] [41:36.72] acquire those generalizable skills and
[L1221] [41:39.28] if your model is is is built correctly,
[L1222] [41:41.20] it will repurpose those skills for
[L1223] [41:42.96] whatever situation it encounters. So I
[L1224] [41:45.52] think it is actually true that if even
[L1225] [41:46.88] if you want to build a warehousing
[L1226] [41:48.16] robot, you're better off collecting a
[L1227] [41:50.08] breath of data and will be better at
[L1228] [41:51.84] handling all the weird edge cases you
[L1229] [41:53.44] might encounter even in that warehouse
[L1230] [41:54.80] domain. But this is not something that's
[L1231] [41:56.32] easy for people to accept because it's
[L1232] [41:57.84] just so like antithetical to the uh
[L1233] [42:00.96] principle of building kind of a a
[L1234] [42:03.12] traditional vertically integrated
[L1235] [42:04.40] robotic system.
[L1236] [42:05.76] >> I noticed this this uh new interesting
[L1237] [42:09.52] phenomenon with these AI companies which
[L1238] [42:12.48] is if they are wildly successful it
[L1239] [42:16.64] creates this um I guess worry or new set
[L1240] [42:19.84] of things. So for instance when
[L1241] [42:22.08] enthropic became had a very powerful
[L1242] [42:24.16] model then the government comes in and
[L1243] [42:27.60] there's these you know worries about
[L1244] [42:30.08] safety and and risk and all that and I'm
[L1245] [42:33.84] I'm curious how you think about that
[L1246] [42:35.68] like if if physical intelligence this
[L1247] [42:38.40] year had a phenomenal incredibly capable
[L1248] [42:42.08] generalized model how do you think about
[L1249] [42:45.52] those kinds of topics that might come up
[L1250] [42:48.16] >> working on AI safety is not a new uh my
[L1251] [42:50.64] my colleague at UC Berkeley Stuart
[L1252] [42:52.16] Russell was talking about this stuff
[L1253] [42:53.84] like over a decade ago and lots of
[L1254] [42:55.92] people spent a lot of time working on
[L1255] [42:57.28] it. It's just that the trouble is when
[L1256] [42:59.76] the technology moves so fast the
[L1257] [43:02.08] important problems are not just a
[L1258] [43:03.60] function of like you know the core
[L1259] [43:05.92] principles it's also a function of how
[L1260] [43:07.28] society reacts to it what kind of tools
[L1261] [43:09.12] are adopted and so on um and I think
[L1262] [43:12.64] that's very very hard to anticipate so
[L1263] [43:15.52] um I don't have like a very satisfying
[L1264] [43:17.60] answer here in terms of how we are
[L1265] [43:21.04] approaching it our philosophy around all
[L1266] [43:23.28] this stuff is
[L1267] [43:26.24] basically one of empirical
[L1268] [43:28.08] experimentation like let's get stuff out
[L1269] [43:30.00] there. Let's see what happens in the
[L1270] [43:31.36] real world. Let's see what goes right
[L1271] [43:32.64] and what goes wrong so that we have as
[L1272] [43:34.88] much of a preview for you know what the
[L1273] [43:37.68] technology can do, what are its
[L1274] [43:39.60] weaknesses, what are its strengths uh
[L1275] [43:42.00] and and so on. But you know at the end
[L1276] [43:44.32] of the day you kind of have to just like
[L1277] [43:45.84] keep your eyes open, see what happens
[L1278] [43:47.44] and adjust as you go. It's it's very
[L1279] [43:49.12] hard to anticipate. And you know, I
[L1280] [43:51.44] think your question though is very
[L1281] [43:52.80] spoton even though I don't have a great
[L1282] [43:54.72] answer for you because like yeah, if
[L1283] [43:57.28] we're having like this much um concern
[L1284] [44:00.24] and and uh issues with AI systems that
[L1285] [44:04.96] are basically limited to using
[L1286] [44:06.32] computers, we're presumably going to
[L1287] [44:08.32] have strictly more concerns and issues
[L1288] [44:10.40] with AI systems that can do everything
[L1289] [44:12.88] in the physical world that we can do,
[L1290] [44:14.72] right? So the issues are real. It's
[L1291] [44:16.08] just, you know, you kind of have to like
[L1292] [44:17.60] see what happens and then adjust. And
[L1293] [44:19.44] that's kind of in the the scary path.
[L1294] [44:21.68] But in the in the happy path, if
[L1295] [44:24.32] everything goes well and we have
[L1296] [44:26.00] incredibly capable models and uh robots
[L1297] [44:31.04] in 10 years, is the north star that
[L1298] [44:34.88] that's the end of human labor. I believe
[L1299] [44:38.40] it's a mistake to think of robots as
[L1300] [44:41.44] mechanical people, right? like um you
[L1301] [44:44.32] know computers at some level are kind of
[L1302] [44:45.92] like mechanical brains but when personal
[L1303] [44:48.88] computers like really took off in the
[L1304] [44:50.72] '9s early 2000s etc. It's not like the
[L1305] [44:54.08] first thing that happened is that you
[L1306] [44:55.76] know people replaced their brains with
[L1307] [44:57.28] computers rather what we saw is actually
[L1308] [44:58.96] a proliferation of very different kinds
[L1309] [45:00.56] of computers. We saw kind of like uh
[L1310] [45:02.48] ubiquitous computing. So you would have
[L1311] [45:04.16] a computer on your desk but you might
[L1312] [45:05.52] also have one in your pocket. You might
[L1313] [45:06.96] have one in your refrigerator and in
[L1314] [45:08.32] your car like because computing became
[L1315] [45:10.32] so accessible, you could have a little
[L1316] [45:12.40] bit of computing in everything. And you
[L1317] [45:14.80] know, I don't think that that's what
[L1318] [45:15.84] like the the people that first started
[L1319] [45:19.04] thinking about this stuff in the 40s and
[L1320] [45:20.40] 50s would have imagined. They would have
[L1321] [45:21.60] imagined like, you know, roomsiz
[L1322] [45:22.96] computers that whose job it is to like
[L1323] [45:25.20] control the the the you know, the policy
[L1324] [45:28.16] of an entire country or something rather
[L1325] [45:30.00] than like a little bit of computer in
[L1326] [45:31.28] everybody's refrigerator. So I think
[L1327] [45:33.04] it's it's you know by analogy of that we
[L1328] [45:34.80] might imagine there might be like a
[L1329] [45:36.08] little bit of physical actuation in
[L1330] [45:37.84] everything and it might just be like
[L1331] [45:40.08] lots of everyday things that you have to
[L1332] [45:42.24] do yourself now you get like a little
[L1333] [45:44.16] bit of help with it. I think the other
[L1334] [45:47.76] example that's worth thinking about is
[L1335] [45:50.32] um modern coding agents, right? So I I
[L1336] [45:52.96] think that you know this is something
[L1337] [45:53.84] where of course the jury is still out as
[L1338] [45:55.20] to what the endgame of coding agents is,
[L1339] [45:57.60] but certainly uh from the experience of
[L1340] [46:01.44] uh software engineers today. Like it
[L1341] [46:03.04] kind of seems like probably fair to say
[L1342] [46:05.68] that most would consider coding agents
[L1343] [46:07.28] to be more empowering them rather than
[L1344] [46:10.56] like uh you know uh somehow causing them
[L1345] [46:13.28] to have a panic. I mean, obviously some
[L1346] [46:15.28] people might might have a panic, but in
[L1347] [46:16.64] general, at least from the software
[L1348] [46:19.04] engineers that that I've talked to and
[L1349] [46:20.88] from my own experience, it's more
[L1350] [46:22.32] empowering to have to kind of be able to
[L1351] [46:23.92] amplify how much work you can do uh with
[L1352] [46:27.12] AI tools. So, I think from that and and
[L1353] [46:29.60] that maybe is like a pretty direct
[L1354] [46:30.80] analogy because that is straight up an
[L1355] [46:32.40] example of an actual real job where AI
[L1356] [46:35.20] has entered into it and has actually
[L1357] [46:37.04] provided more leverage to people doing
[L1358] [46:38.56] that job. So I think that's another
[L1359] [46:40.00] example that we can look to but you know
[L1360] [46:41.60] the truth is that I think it remains to
[L1361] [46:43.28] be seen.
[L1362] [46:44.72] >> So in in LLM's there's a few seinal
[L1363] [46:47.36] papers that if you read those papers you
[L1364] [46:50.08] kind of get a sense of the lineage of
[L1365] [46:51.92] the breakthroughs that mattered and
[L1366] [46:54.08] understanding where we are today in the
[L1367] [46:56.80] robotics industry. Are there a set of
[L1368] [47:00.08] top papers that you really think kind of
[L1369] [47:03.52] show the breakthroughs that people
[L1370] [47:05.28] should know about if they're curious
[L1371] [47:07.20] about the state-of-the-art in terms of
[L1372] [47:09.84] uh humanoid robotics? One thing I would
[L1373] [47:12.64] point out um uh and this is like partly
[L1374] [47:15.44] a shameless plug because I am a
[L1375] [47:16.56] co-author on that paper though candidly
[L1376] [47:18.16] like uh like 99.9% of the work on this
[L1377] [47:21.36] was done by by um Tony who was lead
[L1378] [47:23.84] author is the uh the original ACT paper
[L1379] [47:26.32] the Aloha paper. It's kind it's an
[L1380] [47:28.24] interesting example because in some ways
[L1381] [47:31.04] the ideas weren't really that new but
[L1382] [47:33.12] they were illustrated in a really nice
[L1383] [47:34.72] way and the idea was that hey um if you
[L1384] [47:38.08] set up the right kind of lowcost robot
[L1385] [47:40.72] setup in in his case it was based on um
[L1386] [47:44.40] these robot arms from Trusson Robotics
[L1387] [47:46.24] that they're like $7,000 hobbyist arms.
[L1388] [47:48.88] He set them up in a banual setup with a
[L1389] [47:51.44] leader follower to the operation device.
[L1390] [47:53.84] And he showed that actually if you do it
[L1391] [47:55.60] right without really any particularly
[L1392] [47:56.96] fancy tricks, you could easily collect
[L1393] [47:59.28] the operation data of extremely dextrous
[L1394] [48:01.04] tasks that people had previously thought
[L1395] [48:02.64] would require like very sophisticated
[L1396] [48:04.24] hardware and all sorts of like really
[L1397] [48:05.60] expensive stuff and then set up like a
[L1398] [48:08.00] fairly
[L1399] [48:09.52] straightforward transformer-based model
[L1400] [48:11.52] and it could actually do a lot of those
[L1401] [48:12.88] tasks. And it's kind of like an
[L1402] [48:14.96] interesting thing because usually in
[L1403] [48:16.00] academic research we put a big premium
[L1404] [48:18.00] on like you know do you have some like
[L1405] [48:19.60] sophisticated new mathematical thing or
[L1406] [48:21.28] some sophisticated like uh technical
[L1407] [48:23.60] insight and in that paper which I think
[L1408] [48:26.80] at this point has been hugely
[L1409] [48:27.84] influential. The insight is really just
[L1410] [48:29.84] like yeah just put together the right
[L1411] [48:31.76] pieces and have a little bit more faith
[L1412] [48:35.36] in what a simple robot could do so to
[L1413] [48:37.28] speak equipped with a good intent
[L1414] [48:38.80] learning system. and he showed like
[L1415] [48:40.64] things like um uh replacing batteries in
[L1416] [48:43.20] a remote control. Uh he even had he even
[L1417] [48:45.92] got like a little like a mannequin foot
[L1418] [48:48.08] and he showed that you could put a shoe
[L1419] [48:49.20] on it like for like an assistive task
[L1420] [48:51.04] sort of like you know some some people
[L1421] [48:52.48] need help getting their shoes on so
[L1422] [48:53.68] that's good. Um but like what what
[L1423] [48:56.48] people find found I think so interesting
[L1424] [48:58.88] about that paper is just how far you
[L1425] [49:00.48] could get with like relatively simple
[L1426] [49:02.32] building blocks. And at this point the
[L1427] [49:04.32] the a like he he open sourced the code
[L1428] [49:06.32] for it and the act code has been used by
[L1429] [49:08.08] like lots of people sort of like if
[L1430] [49:09.60] someone wants a very basic starter kit
[L1431] [49:13.04] for like robotic learning that's usually
[L1432] [49:14.80] what they grab and I think that it's
[L1433] [49:18.48] worth for somebody who wants to get into
[L1434] [49:20.16] the field to go through that paper and
[L1435] [49:22.88] really understand what's going on there
[L1436] [49:24.16] because even though in some ways it's
[L1437] [49:26.16] not that sophisticated
[L1438] [49:28.08] I think it provides like a bit of
[L1439] [49:29.36] calibration on what matters right like
[L1440] [49:31.68] you know the details matter But the
[L1441] [49:33.60] details don't have to be complicated.
[L1442] [49:35.92] >> Before all this uh large model robotics
[L1443] [49:39.36] kind of uh wave prior to that um Boston
[L1444] [49:43.92] Dynamics had these really impressive
[L1445] [49:46.56] demonstrations and tons of um mind
[L1446] [49:50.16] share. I guess I wasn't even in the
[L1447] [49:52.08] field by saying wow they're really doing
[L1448] [49:55.20] incredible robotics. And then in the
[L1449] [49:58.16] last I don't know how many years I don't
[L1450] [50:00.88] really hear about them much anymore. Um
[L1451] [50:04.64] is there some shift in the industry that
[L1452] [50:08.08] made that so or you know is that
[L1453] [50:10.32] something you could explain?
[L1454] [50:12.16] >> So the way I would explain it is this
[L1455] [50:13.68] that um there are you know robotics
[L1456] [50:18.24] at at some level is about building
[L1457] [50:19.68] complex systems. So um even though it
[L1458] [50:23.52] kind of it's very tempting to say like
[L1459] [50:25.36] oh there's different areas of AI there's
[L1460] [50:27.60] like LLMs and vision and robotics one of
[L1461] [50:30.08] those is not like the others because for
[L1462] [50:31.44] robots you actually need like all the
[L1463] [50:32.88] parts everything from like how you you
[L1464] [50:36.00] know uh how you wire up the robot what
[L1465] [50:38.32] the power source is what does the
[L1466] [50:39.68] actuator look like all the way to how
[L1467] [50:42.08] does it do like high level planning to
[L1468] [50:43.76] determine like what task to do next and
[L1469] [50:47.68] even though it's kind even though we
[L1470] [50:49.12] could look at these things and say like
[L1471] [50:50.24] oh all of these different videos and
[L1472] [50:52.24] different companies and different demos.
[L1473] [50:53.44] They're all robotics. They're really
[L1474] [50:55.04] kind of a different parts of the stack.
[L1475] [50:57.36] Um,
[L1476] [50:58.96] a lot of what the classic Boston
[L1477] [51:01.28] Dynamics results show is um, very
[L1478] [51:04.72] sophisticated hardware, very carefully
[L1479] [51:06.80] designed hardware with a uh, traditional
[L1480] [51:10.80] control approach with very smart
[L1481] [51:12.96] controls engineers setting everything
[L1482] [51:14.24] up, but with comparatively less emphasis
[L1483] [51:17.28] on the kind of decision-m aspect and I
[L1484] [51:20.56] think that there, you know, at a
[L1485] [51:21.84] particular point in time that actually
[L1486] [51:22.88] made a lot of sense because we can't
[L1487] [51:24.16] build the physical body like it doesn't
[L1488] [51:26.00] matter what kind of decision making
[L1489] [51:27.12] system is running on it. Um
[L1490] [51:30.32] but uh to our earlier discussion about
[L1491] [51:32.64] generalization,
[L1492] [51:34.16] you know, at this point we're at a stage
[L1493] [51:36.24] in the development of these things that
[L1494] [51:39.68] even though we can do more on hardware,
[L1495] [51:42.16] in many ways it's good enough. And the
[L1496] [51:44.24] big challenge is how to have the
[L1497] [51:45.84] decision-making loop that actually works
[L1498] [51:47.84] and that reacts intelligently to
[L1499] [51:50.64] everything in the environment. And the
[L1500] [51:52.40] way and the place where I would draw the
[L1501] [51:53.76] the dividing line between those is
[L1502] [51:56.80] it's like decision-m loop doesn't mean
[L1503] [51:58.80] symbolic decisions. It could mean
[L1504] [52:00.08] low-level decisions. The question is do
[L1505] [52:02.32] you need to take the rest of the
[L1506] [52:03.36] environment into account or are you just
[L1507] [52:05.28] dealing with the robot? So if you want
[L1508] [52:06.80] to do a backflip on flat ground, you
[L1509] [52:08.56] most have to deal with the robot. But if
[L1510] [52:10.48] you want to pick up a coffee cup off of
[L1511] [52:12.64] a table, even though that's maybe in
[L1512] [52:14.64] some ways simpler than doing a backflip,
[L1513] [52:16.24] you really have to understand what's
[L1514] [52:17.36] going on in the rest of the world rather
[L1515] [52:18.80] than just your own body. And that
[L1516] [52:21.36] dividing line, I think the way the
[L1517] [52:23.04] technology has panned out, I think it's
[L1518] [52:25.60] fair to say that that is the dividing
[L1519] [52:26.96] line between AI and controls. Like
[L1520] [52:29.44] controls is when you have to control the
[L1521] [52:32.16] robot body. AI is when you have to take
[L1522] [52:34.08] into account what goes on outside of the
[L1523] [52:36.08] robot.
[L1524] [52:37.84] and and and I think that that's why you
[L1525] [52:39.52] see this divide because I think a lot of
[L1526] [52:41.20] the demos where you mostly needed to
[L1527] [52:44.00] deal with the robot itself and not the
[L1528] [52:45.52] rest of the world really good controls
[L1529] [52:48.32] could allow you to could admit a very
[L1530] [52:49.92] good solution there a and you know
[L1531] [52:51.84] another thing I would say here is like
[L1532] [52:53.76] okay if there's a lot of controls work
[L1533] [52:55.44] that goes into doing some particular
[L1534] [52:58.16] skill well there is actually something
[L1535] [53:00.00] to learn from that because if you can
[L1536] [53:03.52] handdesign a controller that performs a
[L1537] [53:05.60] sophisticated behavior very likely you
[L1538] [53:07.60] can also learn that controller. So like
[L1539] [53:09.28] just that proof of existence that the
[L1540] [53:11.04] thing is possible and not only possible
[L1541] [53:13.36] but also simple enough that a person
[L1542] [53:15.04] could build it because remember people
[L1543] [53:16.72] are you know at the end of the day even
[L1544] [53:18.80] even with code these days the kind of
[L1545] [53:20.64] complexity that people can handle is not
[L1546] [53:22.08] as high as the kind of complexity the AI
[L1547] [53:23.60] can handle. So if a person can
[L1548] [53:24.72] handdesign something uh to do a backflip
[L1549] [53:27.36] or do some acrobatics that's a really
[L1550] [53:29.84] great proof of existence that there
[L1551] [53:31.20] exists some relatively parsimmonious
[L1552] [53:32.96] control law for doing that skill and
[L1553] [53:34.72] parsimonious does mean generalizable. So
[L1554] [53:36.88] if it's simple enough for a person to
[L1555] [53:38.32] design, probably there's something
[L1556] [53:39.68] fairly general in there and if you can
[L1557] [53:41.12] learn it uh and automate it without
[L1558] [53:43.04] having to have the human controls
[L1559] [53:44.64] engineers in the loop, that's that's
[L1560] [53:46.80] good news.
[L1561] [53:48.00] >> And then last question for you is you if
[L1562] [53:50.48] you could go back to when you just
[L1563] [53:52.00] entered the industry and give yourself
[L1564] [53:53.84] some advice knowing everything you know
[L1565] [53:55.60] now, what would you say?
[L1566] [53:57.76] One thing that I've learned uh over the
[L1567] [53:59.84] last uh few years um which I think is a
[L1568] [54:03.12] little different than kind of my
[L1569] [54:04.08] original mindset is I think that
[L1570] [54:06.64] addressing robotics effectively requires
[L1571] [54:09.52] using um very broad prior knowledge. And
[L1572] [54:14.00] I think that there there's this idea
[L1573] [54:15.36] that a lot of people in robotic learning
[L1574] [54:18.16] have which I think I I shared initially
[L1575] [54:19.84] that you know since people learn things
[L1576] [54:22.64] kind of from scratch maybe robots should
[L1577] [54:24.64] learn things from scratch too. Um so uh
[L1578] [54:27.20] like for example uh in um some of our
[L1579] [54:30.24] early work on large scale robotic
[L1580] [54:31.76] learning at Google we uh we had this uh
[L1581] [54:34.72] what we call the the arm farm project
[L1582] [54:36.88] like we set up a bunch of robot arms in
[L1583] [54:38.96] a in a conference room actually because
[L1584] [54:41.12] we didn't have a proper lab but it was a
[L1585] [54:43.12] conference room and we had them all like
[L1586] [54:44.64] grasping objects and the idea was well
[L1587] [54:46.88] if they grasp like millions of objects
[L1588] [54:48.72] they'll learn very general like grasping
[L1589] [54:50.40] strategies and it basically worked like
[L1590] [54:52.64] they could learn to grasp objects but it
[L1591] [54:54.40] was very hard to like take get further
[L1592] [54:56.08] from that to the next level. So, okay,
[L1593] [54:57.44] now I can pick up anything, but like so
[L1594] [54:58.88] what? Uh can like it it didn't serve as
[L1595] [55:01.52] a very good stepping stone for more
[L1596] [55:02.88] complex skills. And I think part of that
[L1597] [55:04.88] was that we were approaching this like
[L1598] [55:06.40] very blank slate like let's start from
[L1599] [55:08.16] zero and see if knowing nothing in
[L1600] [55:10.00] advance the robot could start picking up
[L1601] [55:11.68] behaviors. But I think that it's much
[L1602] [55:14.64] much more practical to get all this to
[L1603] [55:16.40] work if you can combine robot experience
[L1604] [55:18.56] with knowledge that you can pull in from
[L1605] [55:20.00] other sources. Like for example, I was
[L1606] [55:21.68] very skeptical initially about the
[L1607] [55:23.76] utility of language and I think
[L1608] [55:26.80] scientifically this is defensible which
[L1609] [55:28.56] is that like hey um you know like
[L1610] [55:31.20] animals can do some pretty impressive
[L1611] [55:32.56] things like monkeys can do really cool
[L1612] [55:34.08] stuff but monkeys as far as I know can't
[L1613] [55:36.64] speak at least not very eloquently um so
[L1614] [55:39.36] maybe our robots should also be able to
[L1615] [55:40.72] do stuff and they don't necessarily need
[L1616] [55:42.00] to understand language but I think the
[L1617] [55:44.40] subtlety there is what's important is
[L1618] [55:46.24] not language it's it's
[L1619] [55:49.36] prior knowledge that you can put in as a
[L1620] [55:51.52] scaffold on your learning process. And
[L1621] [55:54.00] you can pull in that knowledge in all
[L1622] [55:55.28] sorts of ways. Like, you know, humans
[L1623] [55:56.72] don't necessarily pull that in entirely
[L1624] [55:58.16] through language. Humans all and monkeys
[L1625] [56:00.08] certainly don't. Uh they do it from
[L1626] [56:02.24] observation, from observing other
[L1627] [56:03.92] people, other creatures and so on. So,
[L1628] [56:05.36] there's lots of sources of prior
[L1629] [56:06.24] knowledge. But the point is that you got
[L1630] [56:07.20] to get that prior knowledge in there.
[L1631] [56:08.64] Otherwise, you're actually faced with a
[L1632] [56:09.92] harder problem than what humans and
[L1633] [56:11.84] animals have to solve. Because like, you
[L1634] [56:13.92] know, if a person had to figure out how
[L1635] [56:15.68] to like assemble IKEA furniture, but
[L1636] [56:17.60] they've never actually encountered any
[L1637] [56:19.44] article of furniture in their entire
[L1638] [56:20.88] life, like [laughter]
[L1639] [56:22.56] okay, that would be like pretty
[L1640] [56:23.52] difficult because they don't even know
[L1641] [56:24.48] what like what the point of this is or
[L1642] [56:26.40] what the the endgame looks like. Uh so
[L1643] [56:28.80] yeah, prior knowledge is important. And
[L1644] [56:30.40] while I'm still a big fan of learning
[L1645] [56:32.40] things through experience, I think that,
[L1646] [56:34.16] you know, my advice to myself would have
[L1647] [56:35.76] been take prior knowledge more
[L1648] [56:37.12] seriously.
[L1649] [56:38.16] >> Awesome. Well, thank you so much for
[L1650] [56:39.68] your time, Sergey. I really appreciate
[L1651] [56:40.88] it.
[L1652] [56:41.12] >> Yeah, thank you for your questions. Hey,
[L1653] [56:42.80] thank you for watching this podcast. If
[L1654] [56:44.32] you liked it and you want to see the
[L1655] [56:45.60] show grow, please support with a comment
[L1656] [56:47.92] or a like. Also, if you have any
[L1657] [56:50.56] recommendations for people you want me
[L1658] [56:52.24] to bring on, please drop a comment.
[L1659] [56:54.80] Guests like Barbara Liskov, Mike
[L1660] [56:56.96] Stonereaker, Mark Brooker, these were
[L1661] [56:59.44] all people that I brought on because
[L1662] [57:01.44] someone left a comment. On another note,
[L1663] [57:03.68] aside from the podcast, I'm working on
[L1664] [57:05.60] building the ergonomic keyboard that I
[L1665] [57:07.44] wish existed. Here's a glance at the
[L1666] [57:09.68] prototype. It's a split keyboard, so
[L1667] [57:11.92] there's two sides. This is in the case,
[L1668] [57:14.32] but yeah, we launched on Kickstarter and
[L1669] [57:16.40] we hit our goal within eight hours of
[L1670] [57:18.24] launching. I really appreciate it if you
[L1671] [57:20.00] were one of the people who grabbed one
[L1672] [57:21.44] of the early units. Um, we're now
[L1673] [57:23.60] working on the long journey of building
[L1674] [57:25.36] the tooling now. And so, if you still
[L1675] [57:27.04] want to pick one up, I've left the late
[L1676] [57:29.20] pledges open on Kickstarter, so you can
[L1677] [57:31.60] grab one there. I'll put a link in the
[L1678] [57:33.36] description. Thank you again for
[L1679] [57:35.52] watching the podcast and I'll see you in
[L1680] [57:37.76] the next
