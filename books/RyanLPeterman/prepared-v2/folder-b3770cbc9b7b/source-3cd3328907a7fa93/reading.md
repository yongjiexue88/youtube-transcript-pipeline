# Google DeepMind Distinguished Eng (L9): How To Land a Job at a Frontier Lab | Vlad Feinberg

Source ID: source-3cd3328907a7fa93
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Google_DeepMind_Distinguished_Eng_(L9)_How_To_Land_a_Job_at_a_Frontier_Lab_Vlad_Feinberg_en.txt
Video: https://www.youtube.com/watch?v=cDyi91onoJ8

[L10] [00:00.00] Every single time you go up for a
[L11] [00:01.52] pre-training run, you're about to put in
[L12] [00:03.60] more flops into this run than you've
[L13] [00:05.20] ever done before.
[L14] [00:06.64] >> This is Vlad Feinberg. He's Google
[L15] [00:08.80] DeepMind's [music] pre-training area
[L16] [00:10.12] lead, and I asked him all about how to
[L17] [00:12.52] get a job at a frontier lab.
[L18] [00:14.44] >> That was a particular skill that I see
[L19] [00:16.80] voracious demand for across all the
[L20] [00:18.56] different labs. The research skill set
[L21] [00:21.40] is going to become increasingly
[L22] [00:23.08] important. If you do the scaling book
[L23] [00:25.88] exercises and, you know, send me a video
[L24] [00:28.04] of yourself doing them, I would love to,
[L25] [00:30.60] you know, interview you.
[L26] [00:32.28] >> Here's the full episode.
[L27] [00:37.76] You wrote this post that was titled "How
[L28] [00:40.68] to get a job at a frontier lab." What
[L29] [00:43.12] are the skills that are kind of in
[L30] [00:45.08] demand on frontier labs? Maybe we can
[L31] [00:47.24] talk about the shape of the work.
[L32] [00:49.24] There's quite a range of different
[L33] [00:52.48] things that frontier labs require.
[L34] [00:56.00] At this point, LLMs are artifacts that
[L35] [00:59.56] are connected to,
[L36] [01:01.72] uh, research and product in ways that
[L37] [01:05.88] machine learning really hasn't been as
[L38] [01:08.00] connected to before. And so, it it
[L39] [01:11.52] really touches on so many different
[L40] [01:13.04] things. The goal of my post was to
[L41] [01:15.08] propose just a couple tangible
[L42] [01:17.88] directions in which labs could require a
[L43] [01:21.24] certain set of skills not not to be
[L44] [01:23.00] fully exhaustive.
[L45] [01:24.60] And really the ones that I I dive into
[L46] [01:28.36] have to do with uh kernel development
[L47] [01:31.20] and low-level engineering to accelerate
[L48] [01:35.52] the runtime for these LLMs, uh, in
[L49] [01:38.20] practice. And so, that that was a
[L50] [01:41.00] particular skill that I see voracious
[L51] [01:43.76] demand for across all the different
[L52] [01:45.36] labs, uh, and uh among different
[L53] [01:48.36] projects within the labs. So, that that
[L54] [01:51.08] seemed like a very sharp one to call out
[L55] [01:53.24] as, uh,
[L56] [01:54.64] uh an overall need. Uh, and so
[L57] [01:57.84] specifically
[L58] [01:59.28] whenever we're doing a research project
[L59] [02:02.44] that involves
[L60] [02:03.80] changing the architecture for the neural
[L61] [02:05.32] net in a particular way or rethinking
[L62] [02:08.40] how we might do serving to
[L63] [02:11.40] uh you know, do better KV caching or
[L64] [02:13.32] something like that.
[L65] [02:15.44] Again, across the stack, you just need
[L66] [02:17.44] to be able to implement these new
[L67] [02:19.40] techniques in efficient ways and
[L68] [02:23.00] uh the inner loop of all of these
[L69] [02:25.96] different changes is creating software
[L70] [02:28.64] artifacts that can function at large
[L71] [02:30.72] scales with high throughput, low
[L72] [02:32.84] latency.
[L73] [02:34.20] Uh and this is just fundamental work
[L74] [02:36.64] that's tied to classical back-end
[L75] [02:39.04] engineering thinking.
[L76] [02:40.76] Uh so, yeah, it seemed like a very
[L77] [02:43.92] open thing for people to specialize in.
[L78] [02:46.40] >> My friends that work at OpenAI and
[L79] [02:48.60] Anthropic, there's this distinction of
[L80] [02:52.48] an applied org and the research org. I
[L81] [02:56.52] was wondering if DeepMind has a similar
[L82] [02:59.36] uh distinction and if you could speak
[L83] [03:01.28] about what that difference is.
[L84] [03:03.56] >> Uh so, we we have different focus areas
[L85] [03:07.44] and like
[L86] [03:09.08] you know, for instance, within GDM,
[L87] [03:10.76] there's a team that focuses on how
[L88] [03:15.08] uh we can use our Gemini LLMs to better
[L89] [03:19.00] inform search results. And so, like that
[L90] [03:20.96] might be
[L91] [03:22.24] some, you know,
[L92] [03:24.00] you know, in some way like an applied
[L93] [03:25.96] version of the LLMs, but I I
[L94] [03:29.44] am hesitant to, you know, make a very
[L95] [03:31.96] sharp distinction here because there's
[L96] [03:34.40] so much
[L97] [03:35.84] actual like hard research that has to go
[L98] [03:38.16] into
[L99] [03:39.68] this kind of level of product
[L100] [03:41.16] integration. Like specifically for the
[L101] [03:42.92] one I mentioned, uh quite a lot of work
[L102] [03:44.96] goes into making sure that these LLMs
[L103] [03:47.24] are factual and can cite sources uh to
[L104] [03:50.80] have very precise grounded answers,
[L105] [03:53.80] assessing the quality of these sources
[L106] [03:55.92] to make sure that you're not referring
[L107] [03:57.16] to anything that's like sarcastic or a
[L108] [03:58.76] joke.
[L109] [04:00.88] This is
[L110] [04:02.16] I guess a good example of how even in
[L111] [04:05.20] like product specific quote unquote
[L112] [04:07.68] applied AI verticals, you're still doing
[L113] [04:09.88] research.
[L114] [04:11.28] That being said, there's definitely
[L115] [04:14.24] what I would say is like very classical
[L116] [04:16.08] LLM research teams, pre-training,
[L117] [04:18.76] post-training.
[L118] [04:20.64] These are things that are still
[L119] [04:22.32] stand-alone teams inside of GDM that are
[L120] [04:25.28] focused on
[L121] [04:27.44] what I would say is like, you know,
[L122] [04:28.84] creating soda models, you know, pure
[L123] [04:31.24] research.
[L124] [04:33.12] Again, the caveat is
[L125] [04:34.72] the the pure research that we do, like
[L126] [04:37.24] the extent that it matters is the extent
[L127] [04:39.08] to which we can realize it. And so, you
[L128] [04:41.68] know, we're just as responsible with uh
[L129] [04:45.20] delivering these models and making sure
[L130] [04:47.04] they train stably and actually
[L131] [04:49.84] being like the SREs of sorts for the
[L132] [04:52.52] training run to make sure that the model
[L133] [04:54.16] training is going smoothly
[L134] [04:56.00] as we are for coming up with the recipes
[L135] [04:57.64] to make these LLMs.
[L136] [04:59.44] And you can't separate those two roles.
[L137] [05:01.52] It's it's really crucial to kind of wear
[L138] [05:03.96] both of those hats. So,
[L139] [05:07.24] yeah, I think you can you can draw up a
[L140] [05:08.96] spectrum between research and applied,
[L141] [05:11.40] but no matter what in today's world, I
[L142] [05:14.08] think
[L143] [05:15.28] everyone needs to be fluid across that
[L144] [05:18.20] spectrum.
[L145] [05:19.40] >> I notice there's also another spectrum
[L146] [05:21.36] of software engineer to pure AI
[L147] [05:24.60] researcher and like how do you think of
[L148] [05:27.24] that spectrum? Like software engineering
[L149] [05:29.24] versus like AI researcher roles?
[L150] [05:31.56] >> So, I guess in
[L151] [05:34.16] in in my case specifically, I think a
[L152] [05:36.72] lot of
[L153] [05:38.44] what we do
[L154] [05:40.48] and a lot of the new techniques that we
[L155] [05:43.20] develop,
[L156] [05:45.20] the groundwork is laid in infrastructure
[L157] [05:49.40] investment. So, um I
[L158] [05:53.36] can walk through what my team does a
[L159] [05:54.60] little bit more detail later, but
[L160] [05:57.64] one of the verticals is distillation.
[L161] [06:00.44] And in order to do uh distillation, it's
[L162] [06:04.12] it's some way of uh
[L163] [06:06.44] transferring the knowledge or some form
[L164] [06:09.92] of statistics about the underlying data
[L165] [06:12.80] set through a teacher model into the
[L166] [06:15.00] student model to make the student model
[L167] [06:16.40] better than if it hadn't ever seen these
[L168] [06:18.80] auxiliary statistics from the teacher.
[L169] [06:20.80] And when you're talking about statistics
[L170] [06:24.16] derived from a massive LLM applied to
[L171] [06:27.56] trillions and trillions of tokens,
[L172] [06:29.76] uh you're talking about a level of flops
[L173] [06:32.92] investment that, you know, is
[L174] [06:35.96] you know, millions and millions of
[L175] [06:37.00] dollars. And
[L176] [06:40.08] that in turn
[L177] [06:42.40] means that you have to be able to think
[L178] [06:45.12] through
[L179] [06:46.32] how do you
[L180] [06:48.00] uh
[L181] [06:48.80] optimize the system to be as efficient
[L182] [06:50.36] as possible because every operation that
[L183] [06:52.72] we're performing is is multiplied by
[L184] [06:54.48] such a large factor that every second
[L185] [06:57.16] counts, every byte of storage counts,
[L186] [06:59.88] and
[L187] [07:01.40] quite a bit of that work
[L188] [07:03.52] is
[L189] [07:04.96] you know, good old-fashioned software
[L190] [07:06.80] engineering. And so,
[L191] [07:08.80] uh in particular,
[L192] [07:10.28] the infrastructure for distillation has
[L193] [07:13.28] evolved
[L194] [07:15.48] through maybe three [snorts] to four
[L195] [07:18.24] generations at this point.
[L196] [07:20.40] And in each one,
[L197] [07:22.48] we've taken a step back, looked at what
[L198] [07:25.92] kind of research methods have we been
[L199] [07:27.28] applying for distillation holistically,
[L200] [07:29.72] thought about how do we broaden what the
[L201] [07:33.40] infrastructure is capable of, and
[L202] [07:36.28] there's definitely a couple discrete
[L203] [07:37.72] points where rethinking the system
[L204] [07:41.56] design of how we perform distillation
[L205] [07:44.84] enables us to do research on
[L206] [07:47.04] distillation methods much more quickly.
[L207] [07:49.44] And so it's this kind of investment that
[L208] [07:52.40] like okay, this like four-month or
[L209] [07:54.64] whatever rewrite of our distillation
[L210] [07:56.96] infrastructure
[L211] [07:58.68] then results in a dramatically new and
[L212] [08:02.48] understanding of distillation scaling
[L213] [08:04.32] laws that translates to really strong
[L214] [08:08.08] models. So
[L215] [08:09.76] it really just work across the stack and
[L216] [08:12.96] I you know, I can't
[L217] [08:15.08] Yeah, I can't imagine that we would have
[L218] [08:16.52] gotten results like flash 3.0 without
[L219] [08:19.44] having made those distillation
[L220] [08:21.40] infrastructure investments that are at
[L221] [08:23.40] the end of the day things that started
[L222] [08:25.00] with a good old-fashioned design doc and
[L223] [08:26.80] thinking about what the right
[L224] [08:27.56] abstractions are for
[L225] [08:29.56] generating these teacher statistics,
[L226] [08:31.20] coming up with the right storage system
[L227] [08:33.20] for them, thinking through what could
[L228] [08:35.48] support the reading and writing across
[L229] [08:39.00] multiple different data centers at the
[L230] [08:40.92] scale.
[L231] [08:42.60] Really classical distributed systems
[L232] [08:44.48] problems.
[L233] [08:45.32] >> Yeah, I mean it sounds like there's
[L234] [08:46.92] there's a lot of software engineering
[L235] [08:48.76] back-end infra type problems given just
[L236] [08:51.96] the scale of the computer at this point.
[L237] [08:54.24] It still feels like though there at some
[L238] [08:56.88] point in that spectrum there's some
[L239] [08:59.40] crossover where there's these new skills
[L240] [09:02.00] like somewhere where if you had you took
[L241] [09:05.08] arbitrary back-end engineer and you
[L242] [09:07.28] place them to I don't know, adjust the
[L243] [09:10.72] model architecture or something. Like
[L244] [09:12.80] there that is like a bit of a jump more
[L245] [09:14.56] than the infra work.
[L246] [09:16.48] Like how do you see that distinction?
[L247] [09:18.16] >> Yeah, so I think there is a crossover
[L248] [09:20.52] point in terms of doing research where
[L249] [09:24.20] research is an endeavor where the
[L250] [09:30.24] payoffs become a lot higher risk higher
[L251] [09:33.32] reward and
[L252] [09:36.08] we have this notion of
[L253] [09:37.84] uh kind of research taste, which is, you
[L254] [09:40.00] know, some high-level intuition about
[L255] [09:42.08] what path you should be proceeding
[L256] [09:44.32] through the DAG of the multiple uh
[L257] [09:46.60] different milestones that you need to
[L258] [09:48.24] accomplish in a particular project.
[L259] [09:51.16] In some sense, we can view software
[L260] [09:52.92] engineering projects through a similar
[L261] [09:54.48] DAG where, you know, you have all of
[L262] [09:56.56] these intermediate artifacts that you
[L263] [09:58.52] want to hit in a software program to uh
[L264] [10:01.36] get to the final result. But, in the
[L265] [10:04.84] software engineering case, the DAG is
[L266] [10:07.12] more or less deterministic where you,
[L267] [10:09.88] you know, build one service, then a
[L268] [10:11.24] different service, then a third service,
[L269] [10:13.04] and you know, you figure out your
[L270] [10:14.36] storage infrastructure layer first, uh
[L271] [10:16.68] that kind of thing, and you can just
[L272] [10:17.96] make monotone progress. But, in the
[L273] [10:19.72] research case, you have to
[L274] [10:22.84] uh kind of explore this DAG, which is
[L275] [10:25.20] now stochastic, cuz some of the nodes,
[L276] [10:27.52] which might be some research ideas or
[L277] [10:29.20] some, you know, aspect of getting to a
[L278] [10:31.72] final goal, uh may or may not work out.
[L279] [10:35.76] And I think that requires a bit of a
[L280] [10:37.88] mindset shift.
[L281] [10:40.64] And that that kind of mindset shift
[L282] [10:42.68] takes a while to learn, and it takes
[L283] [10:44.28] specialized skills to learn.
[L284] [10:46.20] Uh this would be the kind of skills you
[L285] [10:47.44] pick up in a PhD, for instance.
[L286] [10:49.52] One succinct way I could put it,
[L287] [10:53.00] there's a really excellent post by
[L288] [10:56.48] this uh Professor Jacob Steinhardt, and
[L289] [10:58.60] I I love to frame a lot of the research
[L290] [11:01.76] work that I do in this way, and it's
[L291] [11:03.60] research as an MDP.
[L292] [11:05.32] So, MDP here, Markov decision process,
[L293] [11:08.68] uh it's again, we have this high-level
[L294] [11:11.44] idea of a stochastic dependency graph
[L295] [11:14.56] between different milestones in a
[L296] [11:16.16] research project where you might need to
[L297] [11:18.76] have a pertinent certain kind of result
[L298] [11:20.60] or prove a certain kind of theorem
[L299] [11:21.84] before you get to a certain kind of
[L300] [11:23.04] conclusion. Uh similarly, for a machine
[L301] [11:25.96] learning research project, you might
[L302] [11:27.60] need to have this and that
[L303] [11:28.52] featureization working before where can
[L304] [11:30.32] get this and that
[L305] [11:32.12] ImageNet accuracy or something like
[L306] [11:33.60] that. Um
[L307] [11:35.56] and expanding those nodes in this graph,
[L308] [11:38.24] it it's this stochastic endeavor where
[L309] [11:40.92] these approaches may or may not work
[L310] [11:42.20] out, and whether or not
[L311] [11:44.60] one works out opens up a set of new
[L312] [11:47.00] possibilities for you.
[L313] [11:48.60] And so
[L314] [11:50.24] the approach that you might have in
[L315] [11:54.04] the software engineering case where
[L316] [11:56.52] you could fully write out here are all
[L317] [11:58.16] the paths to the goal
[L318] [12:00.16] across walking this graph, what's the
[L319] [12:02.36] shortest path to your goal?
[L320] [12:04.20] That approach is not optimal in the
[L321] [12:06.72] research case because if all of a sudden
[L322] [12:09.76] the transitions between the edges in
[L323] [12:12.20] this graph become unreliable, and uh
[L324] [12:16.12] some of the nodes you might not even
[L325] [12:18.72] be aware of. It might be a hidden MDP.
[L326] [12:21.08] Then, the way that you might approach
[L327] [12:23.00] this problem
[L328] [12:24.44] would really differ. And in particular,
[L329] [12:26.52] you have to factor in the success rate
[L330] [12:29.52] and the time investment that you're
[L331] [12:30.96] going to be putting into
[L332] [12:32.92] uh these different research ideas,
[L333] [12:35.32] as well as
[L334] [12:37.20] a priori estimating what those different
[L335] [12:40.40] rates are. And that's a very different
[L336] [12:42.60] exercise than writing up what the, you
[L337] [12:45.72] know, design for your software
[L338] [12:47.36] engineering project might be. And it's
[L339] [12:49.36] it it's this skill set of of building an
[L340] [12:51.32] intuition of how likely an approach is
[L341] [12:53.52] to work out without having yet done that
[L342] [12:56.16] approach
[L343] [12:57.52] that I think people
[L344] [12:59.48] often you know, correlate with this uh
[L345] [13:01.68] research taste notion.
[L346] [13:04.60] But that's exactly the one that you need
[L347] [13:06.00] to build up in order to properly
[L348] [13:08.52] uh traverse this MDP.
[L349] [13:11.12] >> For the the research projects, and just
[L350] [13:13.12] like generally the nature of the
[L351] [13:14.44] research work, I mean, it sounds like
[L352] [13:16.28] you're you're saying that there's a lot
[L353] [13:18.04] more uncertainty here. I'm still trying
[L354] [13:21.24] to get a sense of the the nature of the
[L355] [13:23.12] work. If you threw this back-end
[L356] [13:25.64] engineer into a team that's doing
[L357] [13:28.40] research. Like, what are those like
[L358] [13:30.96] concrete examples where they fall short?
[L359] [13:34.52] >> Like, I think the the very first thing
[L360] [13:37.00] that comes to mind is having the right
[L361] [13:39.60] context for the research landscape in
[L362] [13:43.72] which you're operating. So,
[L363] [13:45.96] quite a bit of research work involves
[L364] [13:50.52] like
[L365] [13:51.64] almost uh
[L366] [13:53.32] this kind of
[L367] [13:55.20] um you have to take on this like very
[L368] [13:57.84] humble viewpoint of there's been quite a
[L369] [14:00.28] lot of investment in related work in the
[L370] [14:02.96] past. And until I know
[L371] [14:07.32] the sum total of humanity's bleeding
[L372] [14:10.20] edge in this topic, I'm definitely not
[L373] [14:12.72] going to be able to further that
[L374] [14:14.44] bleeding edge. So, building up uh
[L375] [14:18.44] a solid understanding of of past work uh
[L376] [14:21.68] in a particular area
[L377] [14:23.48] uh and doing that related literature
[L378] [14:25.12] review is maybe the first thing that I
[L379] [14:27.16] would imagine people might stumble on is
[L380] [14:29.92] uh
[L381] [14:30.52] having read and having the skills to
[L382] [14:32.88] effectively traverse, you know,
[L383] [14:35.08] historical uh citation tree for a
[L384] [14:37.96] particular topic. Because you don't have
[L385] [14:40.88] the time to read all of these different
[L386] [14:42.56] papers. You need to build up a sense of
[L387] [14:44.88] uh what are the high value papers and
[L388] [14:47.16] what are the ways in which I can assess
[L389] [14:49.56] if a paper's worth reading without fully
[L390] [14:51.32] reading it. That's like the first thing
[L391] [14:53.68] that comes to mind as the you know,
[L392] [14:56.32] skill that people need to build up. Even
[L393] [14:58.16] to be able to read these research-level
[L394] [14:59.76] papers, you have to have a background in
[L395] [15:04.00] machine learning, in um some, you know,
[L396] [15:07.84] computer science, and
[L397] [15:10.28] uh
[L398] [15:10.92] you know, depending on the paper and
[L399] [15:12.24] depending on the domain, there might be
[L400] [15:13.64] all sorts of prerequisites in terms of
[L401] [15:15.48] like the underlying math and
[L402] [15:18.20] coursework that you would want to have
[L403] [15:19.84] to properly understand. So,
[L404] [15:23.16] that's that's quite important to be able
[L405] [15:25.12] to have a deep understanding of what
[L406] [15:27.56] methodology is available because you
[L407] [15:29.56] really won't have
[L408] [15:31.08] a lot of hope of improving upon the
[L409] [15:33.04] methodology if you don't understand
[L410] [15:34.28] what's there already. So, so I think I
[L411] [15:36.80] like mentioned earlier, one of the
[L412] [15:38.60] things that my team works on is is
[L413] [15:41.36] distillation.
[L414] [15:42.76] And in order to
[L415] [15:45.40] advance our
[L416] [15:48.04] understanding in uh distillation for
[L417] [15:50.76] large language models,
[L418] [15:52.92] you have to have a good understanding of
[L419] [15:54.92] like what we're trying to do with LLMs.
[L420] [15:57.92] And uh just to give a cursory overview
[L421] [16:01.12] here, the name of the game for LLM
[L422] [16:04.52] research is
[L423] [16:06.92] especially in pre-training is uh is
[L424] [16:08.88] scaling laws. And so,
[L425] [16:11.24] what are scaling laws? People focus a
[L426] [16:13.12] lot about like, you know, this power law
[L427] [16:15.04] structure and the fact that like you,
[L428] [16:17.96] you know, have this and that exponent,
[L429] [16:19.52] but like what matters is less so the
[L430] [16:21.92] functional form. What matters is
[L431] [16:24.16] for a given recipe of scaling up your
[L432] [16:27.20] LLM, so as you invest more and more
[L433] [16:29.76] flops into the pre-training run of an
[L434] [16:31.48] LLM,
[L435] [16:32.88] you have to be able to predict what the
[L436] [16:35.24] final test loss of this LLM is going to
[L437] [16:39.16] be. And why why do we care about this
[L438] [16:41.72] question? Why do we care about
[L439] [16:42.72] predicting what our uh generalization
[L440] [16:44.88] error is?
[L441] [16:46.08] In the classical machine learning world,
[L442] [16:49.76] like say we're trying to, you know, win
[L443] [16:52.00] ImageNet.
[L444] [16:53.68] We have our test loss, which is our
[L445] [16:55.56] classification uh error for, you know, a
[L446] [16:58.40] thousand different classes and uh you
[L447] [17:00.92] run your VGG or your ResNet proposal to
[L448] [17:04.32] get that uh classification error. That's
[L449] [17:06.80] an estimate of how well that model does
[L450] [17:08.60] at classifying
[L451] [17:10.72] amongst those thousand classes uh
[L452] [17:13.08] various different images.
[L453] [17:15.12] We can estimate how good our method's
[L454] [17:16.76] going to be by taking a validation set
[L455] [17:19.12] and then whenever we have an
[L456] [17:20.20] architecture idea for a neural net, we
[L457] [17:21.88] just train it and then we
[L458] [17:24.32] uh do a bunch of uh validation set runs
[L459] [17:26.76] and we get a cross-validation error that
[L460] [17:28.56] is itself an estimator of our final test
[L461] [17:30.56] error. And so in this way you can just
[L462] [17:32.00] iterate on different ideas
[L463] [17:34.28] uh through this process.
[L464] [17:35.84] But what's different in LLM world is
[L465] [17:38.40] every single time you go up for a
[L466] [17:39.84] pre-training run, you're about to put in
[L467] [17:42.36] more flops into this run than you've
[L468] [17:43.92] ever done before.
[L469] [17:45.72] So, it's in some sense like a one-shot
[L470] [17:48.04] version of this ImageNet problem. You
[L471] [17:49.52] never get to see the full ImageNet
[L472] [17:51.80] training data set. You have to practice
[L473] [17:53.84] on MNIST and then CIFAR and then maybe
[L474] [17:55.92] based off of those, you try to come up
[L475] [17:58.20] with a method that just works right off
[L476] [17:59.76] the bat on ImageNet. And if you were to
[L477] [18:02.96] just do that by itself, as I'm sure many
[L478] [18:05.88] people have tried, uh like certainly
[L479] [18:07.56] when I was learning how to do all of
[L480] [18:08.88] those different things, you get
[L481] [18:10.20] something, it works really great on
[L482] [18:11.60] MNIST, it maybe even works on CIFAR, and
[L483] [18:13.88] then all of a sudden it breaks on
[L484] [18:15.00] ImageNet.
[L485] [18:16.40] You'll find out that like things don't
[L486] [18:18.56] just generalize easily across scale like
[L487] [18:20.40] this. And
[L488] [18:22.52] so much of what we do for LLMs is coming
[L489] [18:25.12] up with recipes, where a recipe is this
[L490] [18:28.40] function that goes from number of flops
[L491] [18:30.60] you'd like to train on to a training
[L492] [18:32.56] routine for this LLM. And if you can
[L493] [18:35.60] couple this recipe with a prediction
[L494] [18:38.08] rule that can predict accurately what
[L495] [18:40.40] your LLM accuracy is going to be, then
[L496] [18:43.24] um you're able to make decisions about
[L497] [18:45.92] how to improve your recipe cuz you can
[L498] [18:47.60] use that prediction.
[L499] [18:49.32] That is all a ton of context on what uh
[L500] [18:52.20] LLM research looks like in general, but
[L501] [18:54.96] that's like a an understanding that we
[L502] [18:57.00] got to, that we even thought was
[L503] [18:59.12] feasible, thanks to so much uh
[L504] [19:02.84] initial LLM scaling work that we've seen
[L505] [19:06.24] across the Kaplan paper, across
[L506] [19:09.00] Chinchilla.
[L507] [19:11.16] Since those two papers, there's been a
[L508] [19:13.72] lot more work in terms of like what
[L509] [19:15.64] other factors are there beyond uh number
[L510] [19:17.92] of params and um
[L511] [19:20.28] number of tokens that you train on that
[L512] [19:22.52] influence your prediction accuracy.
[L513] [19:25.12] Uh like number of unique tokens for
[L514] [19:26.64] instance.
[L515] [19:28.12] But like I would say like those two
[L516] [19:31.08] foundational papers for LLMs, uh those
[L517] [19:33.88] are informed by uh an even even longer
[L518] [19:36.48] line of uh different uh scaling works
[L519] [19:39.64] going back to like say the original uh
[L520] [19:42.20] GPTs and then Google has had a ton of
[L521] [19:44.48] scaling work across its Palm papers.
[L522] [19:47.36] This is just a set of works that have
[L523] [19:51.44] informed that viewpoint that I described
[L524] [19:53.40] earlier that
[L525] [19:55.84] you you kind of just need to build up by
[L526] [19:58.36] having gone through that literature
[L527] [20:00.20] review yourself.
[L528] [20:01.60] >> If you were for instance, if uh
[L529] [20:04.08] you were trying to pick someone that was
[L530] [20:05.76] going on your team and the the way that
[L531] [20:09.12] you would judge their fitness to help
[L532] [20:11.00] you push the frontier is their
[L533] [20:13.80] understanding of the frontier including
[L534] [20:16.12] the existing literature which requires
[L535] [20:18.56] all these prerequisite. I think you
[L536] [20:20.72] called it mathematical maturity in your
[L537] [20:22.76] post.
[L538] [20:23.84] >> Yeah, so I think I I
[L539] [20:26.52] I think it's
[L540] [20:28.52] easy to read and understand those papers
[L541] [20:30.56] once you have mathematical maturity.
[L542] [20:33.24] So I guess the ones I mentioned in
[L543] [20:35.96] particular nowadays they're table
[L544] [20:37.56] stakes. So I I would expect candidates
[L545] [20:39.44] to be familiar with them. Um
[L546] [20:42.84] I think um
[L547] [20:45.20] the the general skill set is being able
[L548] [20:47.80] to dive in to
[L549] [20:49.80] uh a paper of that level and then
[L550] [20:52.16] understanding it.
[L551] [20:54.28] Uh
[L552] [20:55.16] you know being able to take a research
[L553] [20:57.48] idea uh from a paper and implementing it
[L554] [21:01.32] yourself. Like that's that's just a a
[L555] [21:04.04] very important skill set to be able to
[L556] [21:05.52] have. Like we get, you know,
[L557] [21:08.40] all sorts of uh uh different ideas
[L558] [21:10.44] presented, you know,
[L559] [21:12.40] they might not all directly apply to our
[L560] [21:14.80] domain, but if you can deeply understand
[L561] [21:16.64] them, then you can iterate on them, and
[L562] [21:17.80] you can improve them inside of
[L563] [21:19.84] uh inside of our domain. And so, when we
[L564] [21:22.52] assess for people who can work with the
[L565] [21:26.40] mathematical concepts in these machine
[L566] [21:28.00] learning papers, that's that's I guess
[L567] [21:30.04] the the key skill there that would be
[L568] [21:32.24] evidence that you can go pick up this
[L569] [21:34.68] arbitrary paper and see to what extent
[L570] [21:37.96] these ideas carry over uh in the Google
[L571] [21:40.24] setting.
[L572] [21:41.40] >> This probably won't be exhaustive, but
[L573] [21:43.24] I'd be curious to hear other domains
[L574] [21:46.64] that maybe people could dig into to see
[L575] [21:49.80] what kind of matters in frontier AI
[L576] [21:51.68] research. So, you'd mentioned
[L577] [21:53.88] distillation, you also mentioned
[L578] [21:55.32] kernels, it sounds like kernels are
[L579] [21:56.56] helpful everywhere. Um but are there
[L580] [21:59.28] other areas that come to mind if you
[L581] [22:00.72] were just raffle off areas that are not
[L582] [22:02.92] necessarily exhaustive?
[L583] [22:05.12] >> One thing that I think is is quite
[L584] [22:07.56] powerful is uh actually
[L585] [22:10.48] programming language research. So, by
[L586] [22:13.44] looking into how we can create
[L587] [22:15.52] abstractions at the programming language
[L588] [22:17.24] level, we could facilitate kernel
[L589] [22:19.08] development. I think ThunderKittens is a
[L590] [22:21.36] really good example of this. Like,
[L591] [22:23.24] coming up with an
[L592] [22:24.56] an abstraction that allows you to write
[L593] [22:26.36] kernels through four functions instead
[L594] [22:28.40] of arbitrary globs of C++ code uh
[L595] [22:31.96] allows you to move really quickly uh in
[L596] [22:35.24] uh developing algorithms that fully
[L597] [22:37.68] utilize hardware.
[L598] [22:40.08] So, like, it it at that point it it's um
[L599] [22:44.36] it's not about the PL research itself,
[L600] [22:45.88] it's about having a passion for,
[L601] [22:49.36] you know, these kind of programming
[L602] [22:50.36] language abstractions and and working
[L603] [22:52.20] with uh low-level hardware.
[L604] [22:54.48] Um you know, uh people who, you know,
[L605] [22:57.88] are interested in and will
[L606] [23:00.04] try to work with like cute DSL, the this
[L607] [23:02.92] kind of thing where there's a lot of
[L608] [23:05.20] hardware specific domain specific
[L609] [23:07.40] languages. Uh one other thing that comes
[L610] [23:09.60] to mind besides PL and uh scaling law
[L611] [23:13.48] literature would be reinforcement
[L612] [23:15.80] learning literature.
[L613] [23:17.24] Uh so in particular ever since uh RLHF,
[L614] [23:21.28] uh I think we've seen that
[L615] [23:23.36] deep RL algorithms uh like PPO do have a
[L616] [23:27.16] place in production systems and you
[L617] [23:29.48] know, there was a time where
[L618] [23:31.44] that was in question, but uh now it's
[L619] [23:34.16] you know,
[L620] [23:35.24] uh pretty unanimous that we see these
[L621] [23:37.28] kind of algorithms applied to real
[L622] [23:39.36] production systems and
[L623] [23:42.24] the uh theory behind that uh you kind of
[L624] [23:46.40] have to start with the basics for
[L625] [23:48.80] reinforcement learning and work their
[L626] [23:50.80] way up to
[L627] [23:52.84] you know, the myriad uh value-based
[L628] [23:55.20] methods and and uh policy gradient
[L629] [23:57.36] methods that we have today.
[L630] [24:00.32] That's that's another domain that I
[L631] [24:01.92] think is just like a very rich
[L632] [24:03.12] literature tree to crawl. Um and then
[L633] [24:06.60] for more of the back end engineer folks,
[L634] [24:08.64] just beyond just the kernels themselves,
[L635] [24:11.92] there's I think
[L636] [24:13.64] a pretty fun overlap between distributed
[L637] [24:16.16] systems and optimization work where uh
[L638] [24:19.92] figuring out how to design neural net
[L639] [24:23.08] training algorithms that allow for
[L640] [24:26.20] training across
[L641] [24:28.24] many GPUs.
[L642] [24:31.08] There's all sorts of fun challenges
[L643] [24:34.08] between asynchronicity, how up-to-date
[L644] [24:37.04] your gradients are,
[L645] [24:38.88] how
[L646] [24:40.84] pipelining affects the staleness,
[L647] [24:43.44] uh all of these system choices that you
[L648] [24:45.36] could make in your training algorithm
[L649] [24:47.68] design will impact convergence and the
[L650] [24:49.64] final quality of your neural net. And uh
[L651] [24:52.00] those are things that can be analyzed
[L652] [24:53.36] independently of the LLM setting
[L653] [24:55.48] uh and have been for a while. So,
[L654] [24:58.92] uh, you know, especially if you're kind
[L655] [25:00.12] of more infra-inclined, then having a
[L656] [25:02.56] good understanding of like,
[L657] [25:04.68] uh, how those different algorithms works
[L658] [25:06.28] work is a is a really good place to
[L659] [25:07.84] start.
[L660] [25:09.20] >> Do you see any difference between the
[L661] [25:11.68] the demands of the different frontier
[L662] [25:13.60] labs? So, for instance, if someone wants
[L663] [25:15.32] to work at DeepMind, is there like a
[L664] [25:17.64] particular area that you see DeepMind
[L665] [25:20.76] cares about more than Anthropic, for
[L666] [25:22.88] instance?
[L667] [25:24.08] >> I think in terms of the skill set, it's
[L668] [25:25.80] probably pretty similar. Yeah, I think I
[L669] [25:28.20] think there's maybe differences in like
[L670] [25:31.96] business strategy and, uh, you know, the
[L671] [25:36.08] set of offerings that's a function of,
[L672] [25:40.00] uh, the specialties of the labs and,
[L673] [25:43.52] uh, like the kind of different, uh, you
[L674] [25:45.92] know, customers that the labs could
[L675] [25:47.04] have. Uh, but
[L676] [25:49.48] uh, I would say that there's there's
[L677] [25:51.76] quite a lot of overlap between the labs
[L678] [25:53.92] in terms of what people look for. And
[L679] [25:56.04] like, yeah, like when I posted, uh, my
[L680] [25:58.08] post, you would you would see like, you
[L681] [25:59.64] know, people from both OpenAI and
[L682] [26:01.64] Anthropic saying like, yeah, like we
[L683] [26:03.40] agree with this advice. And so, you
[L684] [26:05.04] know, I think, um,
[L685] [26:07.52] that that's just a little bit of
[L686] [26:08.72] evidence towards that.
[L687] [26:09.96] >> I think one reason for the the huge
[L688] [26:12.08] demand for wanting to go closer to AI
[L689] [26:14.56] research is because people are thinking
[L690] [26:17.36] of software engineering is not going to
[L691] [26:18.92] be as important in the future. Is there
[L692] [26:21.08] a similar thought in when it comes to
[L693] [26:23.72] research where LLMs is also going to
[L694] [26:26.28] handle a lot of that work as well, so
[L695] [26:28.68] there's no reason to favor AI research
[L696] [26:31.36] versus software engineering?
[L697] [26:33.04] >> Um,
[L698] [26:34.28] so I think the the research skill set is
[L699] [26:36.84] going to become increasingly important.
[L700] [26:39.92] Uh, so I would say like being able to
[L701] [26:42.84] handle stochastic components in the
[L702] [26:45.80] planning of your work
[L703] [26:47.76] is is just going to be a larger and
[L704] [26:50.96] larger part of how we approach our jobs.
[L705] [26:56.20] Figuring out how to leverage AI in
[L706] [26:58.96] whatever thing you work on, which
[L707] [27:01.28] doesn't even have to be software
[L708] [27:02.40] related, is just an important muscle to
[L709] [27:04.64] start building right away.
[L710] [27:06.76] Um because these components aren't
[L711] [27:08.64] deterministic and thinking about how do
[L712] [27:10.64] I construct systems around these LLMs to
[L713] [27:13.28] do my job more effectively,
[L714] [27:15.24] uh that's that's going to be the thing
[L715] [27:16.68] that sets you apart in the future. And I
[L716] [27:18.60] think that's true no matter what you're
[L717] [27:19.64] going to be doing. Look, I think I think
[L718] [27:21.92] there's there's fud everywhere,
[L719] [27:23.88] especially with with some of the
[L720] [27:25.76] approach to marketing that some people
[L721] [27:28.00] have in terms of AI. It's fud that is
[L722] [27:31.44] being intentionally leveraged. And so, I
[L723] [27:34.12] I feel like
[L724] [27:36.16] people should really just focus on
[L725] [27:37.76] themselves and and trying to uh be more
[L726] [27:40.60] productive themselves.
[L727] [27:42.32] I I don't think that like AI is going to
[L728] [27:45.88] replace all of our roles. And so, the
[L729] [27:48.16] reason for that is that
[L730] [27:51.24] one of the important aspects of what we
[L731] [27:54.32] do as humans in an organization, which
[L732] [27:56.88] is really this web of trust,
[L733] [28:00.76] from like, you know, this organization
[L734] [28:03.92] that is, you know, this pool of
[L735] [28:05.12] resources and this pool of people that
[L736] [28:06.96] manages these resources.
[L737] [28:09.12] One of the important things that we do
[L738] [28:11.16] is we allocate those resources towards
[L739] [28:13.44] cer- certain goals.
[L740] [28:15.04] And um
[L741] [28:17.76] even when
[L742] [28:19.20] we can accelerate
[L743] [28:21.08] our execution,
[L744] [28:23.00] there's an element of making decisions
[L745] [28:25.96] around how we allocate these resources
[L746] [28:28.12] that will always be
[L747] [28:30.48] something that needs to be attributable
[L748] [28:31.84] to a human making that decision.
[L749] [28:34.16] And uh that's simply because
[L750] [28:36.92] you can't hand off blame to AI.
[L751] [28:39.92] So,
[L752] [28:41.12] we at this point have LLMs that really
[L753] [28:44.08] deeply understand law. And they could,
[L754] [28:45.92] you know, review your contract for you
[L755] [28:47.36] or something like that.
[L756] [28:48.92] But, they can't represent you in court
[L757] [28:51.28] because they can't be disbarred.
[L758] [28:53.92] And so, that's that's I think like a
[L759] [28:56.16] really, you know, sharp way that I might
[L760] [28:58.68] describe like, okay, this is why the
[L761] [29:00.76] legal profession will go on even though
[L762] [29:03.88] LLMs are really good at recalling
[L763] [29:06.04] precedent is
[L764] [29:07.88] you want to have someone who is
[L765] [29:10.20] responsible who can validate the output
[L766] [29:12.52] of AI to perform
[L767] [29:16.44] uh
[L768] [29:17.00] legal work more effectively for you
[L769] [29:19.72] rather than
[L770] [29:21.24] hand off
[L771] [29:23.88] your legal defense to an LLM.
[L772] [29:26.00] >> Yeah, I think the FUD, that was actually
[L773] [29:28.60] the original motivation for your post.
[L774] [29:30.76] >> Yeah, I mean, I I really think that the
[L775] [29:33.20] mindset that people should have is is a
[L776] [29:35.52] constructive one. And so, there was a
[L777] [29:38.48] tweet that I saw, I think by Didi, that
[L778] [29:41.00] was like some long-form, you know,
[L779] [29:44.24] fear-mongering about, you know, uh
[L780] [29:47.16] uh
[L781] [29:48.04] AI permanent underclass or something
[L782] [29:50.04] like that. And uh
[L783] [29:51.96] it's easy to get stuck in that loop, but
[L784] [29:54.64] I think the important thing to think
[L785] [29:58.16] about is like we all have agency over
[L786] [30:01.56] our future and we can start investing in
[L787] [30:05.20] uh skills that matter for tomorrow
[L788] [30:08.36] today. And
[L789] [30:10.68] um
[L790] [30:11.40] that's that's really
[L791] [30:13.92] the only thing you should be doing,
[L792] [30:15.24] right? Like, you know, worrying about it
[L793] [30:16.72] is not going to not going to help you.
[L794] [30:18.44] And so, part of why I wanted to write
[L795] [30:20.48] this post is is in response to that.
[L796] [30:23.72] Uh because it it it was something that I
[L797] [30:26.08] could see echoed, you know, I gave the a
[L798] [30:29.44] lecture at Princeton a while back and,
[L799] [30:31.36] you know, a big question that came up is
[L800] [30:32.92] like, you know, how do I work at
[L801] [30:34.80] DeepMind? And And it's something that
[L802] [30:36.68] like uh yeah, just when people find out
[L803] [30:39.12] what I do, that's the top question
[L804] [30:40.48] people ask. So, I figured it would be
[L805] [30:42.72] helpful to add a little bit more
[L806] [30:45.08] constructive
[L807] [30:47.16] you know, direction to the discourse
[L808] [30:48.88] here.
[L809] [30:49.84] >> One last thing on the post cuz, you
[L810] [30:52.12] know, if you think about getting a role,
[L811] [30:54.24] there's obviously the skills and we
[L812] [30:56.56] talked a lot about the skills and your
[L813] [30:58.40] fitness for the role, but there's also
[L814] [31:00.44] kind of the
[L815] [31:02.00] signaling for that role and like what is
[L816] [31:04.60] kind of valued if you were to be saying
[L817] [31:07.24] marketing yourself to one of these
[L818] [31:09.00] frontier labs, what signals
[L819] [31:11.96] matter most?
[L820] [31:13.48] >> Actual evidence that you've created
[L821] [31:15.88] something of uh
[L822] [31:18.96] of use to other people along the line of
[L823] [31:21.92] kernels, right? Like you can take any of
[L824] [31:25.28] the many open source LLMs that we have
[L825] [31:27.88] and optimize them. You don't have to
[L826] [31:30.12] make them better in every case. You
[L827] [31:31.68] could show that oh, I have an
[L828] [31:32.80] improvement for this and that setting.
[L829] [31:35.16] It doesn't even have to be something
[L830] [31:36.68] that speeds up the model on GPU. There's
[L831] [31:39.44] all sorts of open source stacks like
[L832] [31:41.60] vLLM. There's a lot of other
[L833] [31:44.60] things that you can do besides
[L834] [31:46.48] accelerating the LLM inference on
[L835] [31:48.68] device. The serving stack that surrounds
[L836] [31:51.44] LLMs is a very sophisticated distributed
[L837] [31:54.36] system that has to maintain
[L838] [31:56.96] this KB cache memory and deal with
[L839] [32:01.16] all sorts of like load balancing and
[L840] [32:04.88] request queuing and and very common
[L841] [32:06.96] problems for for back-end servers. And
[L842] [32:10.48] these projects are always looking for
[L843] [32:11.60] help. So, you know, contributions to
[L844] [32:14.68] vLLM or SG Lang
[L845] [32:17.32] or demonstrations with TensorRT.
[L846] [32:20.64] They have I think a
[L847] [32:22.32] a distributed system called Dynamo that
[L848] [32:24.56] allows for disaggregated serving
[L849] [32:27.80] where
[L850] [32:29.04] you could show that you you made a
[L851] [32:30.40] project using these components, you
[L852] [32:32.20] improved these components. Like that
[L853] [32:34.64] would be an extremely positive signal
[L854] [32:37.16] for any candidate that I'm looking at
[L855] [32:39.64] and and a very welcome contribution to
[L856] [32:42.04] open source.
[L857] [32:43.88] >> I think also a lot of what we said is
[L858] [32:45.68] kind of assuming the path of external
[L859] [32:49.00] hire into Frontier Lab.
[L860] [32:51.88] But a lot of these Frontier Labs have
[L861] [32:55.08] large organizations that aren't
[L862] [32:56.52] necessarily doing the cutting edge
[L863] [32:58.60] Frontier work. So let's say yeah, for
[L864] [33:00.96] instance, I mean, you know, Google
[L865] [33:02.48] DeepMind versus
[L866] [33:04.88] let's say there's some infrastructure
[L867] [33:06.40] eng that's working on search and they
[L868] [33:09.08] have the back-end skillset, maybe not as
[L869] [33:11.04] much domain context and they try to
[L870] [33:13.80] internal transfer to Google DeepMind.
[L871] [33:16.32] Does any of your advice differ in that
[L872] [33:18.16] kind of case for like an internal
[L873] [33:19.56] transfer versus
[L874] [33:21.56] someone who's coming from external?
[L875] [33:23.68] >> There's someone who I worked with
[L876] [33:26.52] closely on the search side
[L877] [33:29.16] who actually did transfer to my team
[L878] [33:32.40] Nate Lidzén and he's amazing and now he
[L879] [33:34.56] owns so much of
[L880] [33:36.88] like what we do on my team in terms of
[L881] [33:40.44] inference code design for
[L882] [33:42.80] like flash and flashlight and
[L883] [33:46.00] I would say like he's a really great
[L884] [33:47.44] example of this where
[L885] [33:49.84] his approach was, you know, how do I
[L886] [33:52.80] help my PA, my product area
[L887] [33:57.36] adopt this technology as effectively as
[L888] [33:59.44] possible. So I think there's, you know,
[L889] [34:02.24] definitely
[L890] [34:03.76] if you're
[L891] [34:05.16] in
[L892] [34:06.72] organization that isn't directly
[L893] [34:08.96] generating these models, but in some way
[L894] [34:10.80] trying to leverage them there's
[L895] [34:13.88] a very big gap in terms of applying
[L896] [34:16.36] these LLMs effectively, serving them
[L897] [34:18.56] effectively
[L898] [34:20.64] within
[L899] [34:22.16] your organization
[L900] [34:24.36] and becoming someone who does that
[L901] [34:26.96] really effectively not only creates a
[L902] [34:29.40] ton of value
[L903] [34:31.12] in terms of like
[L904] [34:33.80] the uh you know specific business need
[L905] [34:36.60] for your org which will definitely
[L906] [34:38.08] elevate you and your org
[L907] [34:39.92] but it'll also be the case that you're
[L908] [34:42.36] going to just naturally become the
[L909] [34:44.28] partner that we work with
[L910] [34:46.16] on the research side to make sure that
[L911] [34:48.84] our models are effective within your org
[L912] [34:51.08] and so at that point you know you may or
[L913] [34:53.16] may not want to transfer definitely if
[L914] [34:56.04] you transfer we you know be happy to
[L915] [34:57.88] work with you but like
[L916] [35:00.32] at that point I think you're you're
[L917] [35:01.68] you're already doing something that is
[L918] [35:03.28] cutting edge which is
[L919] [35:04.96] integrating this new technology into
[L920] [35:08.00] you know a real product that people use
[L921] [35:09.76] and so
[L922] [35:11.80] yeah that'd be my advice there.
[L923] [35:13.80] >> As it towards the end of this post as we
[L924] [35:15.76] as we leave this topic you had the
[L925] [35:18.68] concrete invitation cuz I know you were
[L926] [35:21.08] hiring
[L927] [35:22.28] do you want to say what that was?
[L928] [35:23.80] >> Yeah so I was just trying to think of
[L929] [35:25.76] like you know you know how do I put my
[L930] [35:28.04] money where my mouth is
[L931] [35:30.00] um
[L932] [35:30.64] how do I demonstrate look this is good
[L933] [35:33.56] way to show that you have you know at
[L934] [35:36.60] least some evidence of of like the the
[L935] [35:38.60] skills that I called out as important
[L936] [35:40.32] you know intent mathematical maturity
[L937] [35:42.44] grit
[L938] [35:43.80] and so I listed out a couple of
[L939] [35:46.04] exercises that demonstrate you know some
[L940] [35:48.88] initial knowledge of scaling laws some
[L941] [35:51.00] willingness to get into the weeds
[L942] [35:53.08] engineering wise in terms of
[L943] [35:54.48] implementing a real transformer
[L944] [35:56.96] and
[L945] [35:58.20] sort of willingness to pick up the kind
[L946] [36:00.44] of bread and butter bread and butter
[L947] [36:01.76] math that we use every day to size these
[L948] [36:06.28] LLMs
[L949] [36:07.48] and you know I won't I won't recall the
[L950] [36:10.44] full list of like the exercises that I
[L951] [36:12.40] expected here but like you know if if
[L952] [36:14.80] you do the detailed like handwritten
[L953] [36:18.16] version of the scaling book exercises
[L954] [36:20.56] and you know send me a video of yourself
[L955] [36:22.20] doing them along with the transformer
[L956] [36:24.20] exercise on my post
[L957] [36:26.56] then that's something if you can work in
[L958] [36:28.44] the uh New York office, I would love to,
[L959] [36:31.32] you know, interview you for. And quite a
[L960] [36:34.32] few people reached out to me about that.
[L961] [36:36.28] I actually already have had a couple
[L962] [36:37.76] submissions and we're proceeding with
[L963] [36:39.88] the loop with those people. So,
[L964] [36:43.04] yeah, it's it's quite a bit of work, but
[L965] [36:45.28] uh impressively, I got a response within
[L966] [36:47.36] like, I think,
[L967] [36:48.72] a week of posting. So,
[L968] [36:51.84] uh it's definitely doable.
[L969] [36:54.60] Uh
[L970] [36:55.68] yeah, I mean, I don't have unlimited
[L971] [36:57.24] head count, so I mean, the offer's on
[L972] [36:59.28] the table, but the, you know,
[L973] [37:01.56] I can only hire so many people. The good
[L974] [37:03.96] thing is, though, that is such a strong
[L975] [37:05.96] sign of,
[L976] [37:07.84] you know, self-development
[L977] [37:09.60] that uh
[L978] [37:11.20] not only is this a something that you
[L979] [37:12.64] should be doing for its own sake,
[L980] [37:14.32] regardless of whether or not you will
[L981] [37:16.20] get a job at at DeepMind specifically,
[L982] [37:20.04] but I think it'll be something that's,
[L983] [37:22.08] you know,
[L984] [37:23.20] lets you basically prepare for
[L985] [37:25.56] interviews in other places.
[L986] [37:27.68] Uh certainly, if you reach out to me
[L987] [37:29.16] with these uh exercises completed, like,
[L988] [37:32.44] even if, you know, I do all my hiring,
[L989] [37:35.08] there's tons of people who I know who
[L990] [37:37.56] are hiring as well, and I'd be happy to
[L991] [37:39.44] refer people as well.
[L992] [37:41.60] >> OpenAI, [snorts]
[L993] [37:42.52] Anthropic, Cursor, and Vercel all use
[L994] [37:45.80] this product to make their lives better.
[L995] [37:48.04] And the problem it solves is when you're
[L996] [37:49.96] building SaaS or an ad product, and you
[L997] [37:52.60] want to sell to other companies, there's
[L998] [37:54.52] all these requirements you need to meet.
[L999] [37:56.60] There's SSL, there's SCIM, there's RBA,
[L1000] [38:00.24] there's audit logs. These are all things
[L1001] [38:02.04] that take time to integrate, but aren't
[L1002] [38:04.20] the main focus of your app. WorkOS is an
[L1003] [38:06.52] API layer that lets you meet all of
[L1004] [38:08.20] these requirements in just a few lines
[L1005] [38:10.36] of code. So, let's say you have a new
[L1006] [38:12.44] SaaS product, and you want to sell to
[L1007] [38:14.08] other companies, WorkOS will solve all
[L1008] [38:16.56] of these critical feature gaps for you.
[L1009] [38:19.32] You can check them out at workos.com to
[L1010] [38:21.80] learn more and get started. And I
[L1011] [38:23.96] appreciate them for supporting my work
[L1012] [38:25.84] and sponsoring this podcast.
[L1013] [38:27.84] On the next [snorts] topic, I mean, uh I
[L1014] [38:29.80] saw you're the the the area lead for
[L1015] [38:32.20] pre-training on Gemini, and I just
[L1016] [38:34.84] thought it might be interesting to hear
[L1017] [38:36.20] you give um
[L1018] [38:37.84] uh kind of like a high-level overview of
[L1019] [38:39.96] what pre-training is or in your words,
[L1020] [38:42.04] and maybe what are the the high-level
[L1021] [38:44.16] challenges in the area. I mean, we can
[L1022] [38:46.00] talk about that.
[L1023] [38:46.88] >> Yeah, so
[L1024] [38:48.72] there's there's quite a lot of work that
[L1025] [38:50.16] we do in pre-training. Um as an area
[L1026] [38:53.56] lead for it,
[L1027] [38:55.76] the specific things that my team is
[L1028] [38:57.68] responsible for delivering uh include uh
[L1029] [39:01.56] the flash model, the flashlight model.
[L1030] [39:04.48] These are models that get used for AI
[L1031] [39:06.20] overviews and AI mode in the search bar,
[L1032] [39:09.12] uh as well as some other uh 1P models
[L1033] [39:11.80] that are used by different orgs like ads
[L1034] [39:14.40] and YouTube.
[L1035] [39:16.20] Besides this, we're also key technical
[L1036] [39:18.68] POCs for the uh Google-Apple
[L1037] [39:21.48] partnership, uh and so we do technical
[L1038] [39:23.56] work there.
[L1039] [39:25.88] Those are the actual
[L1040] [39:27.88] like product-level deliverables
[L1041] [39:30.28] uh from my team.
[L1042] [39:31.52] Uh beyond that, we do research to make
[L1043] [39:35.64] sure that these deliverables are
[L1044] [39:37.24] state-of-the-art.
[L1045] [39:38.72] And also, we do general pre-training re-
[L1046] [39:40.60] research that contributes to the Pro
[L1047] [39:42.32] Series model as well.
[L1048] [39:44.16] And the nature of the research, I would
[L1049] [39:48.16] say generally breaks down into three
[L1050] [39:49.84] different verticals. There's
[L1051] [39:51.88] distillation, which I mentioned earlier.
[L1052] [39:55.16] There's what I like to call inference
[L1053] [39:57.20] co-design. So, uh
[L1054] [39:59.60] creating neural architectures that are
[L1055] [40:02.40] efficient
[L1056] [40:03.92] uh to run inference on. So, coming up
[L1057] [40:06.56] with the network topology, the shapes of
[L1058] [40:10.32] the matrices that the matmuls uh
[L1059] [40:14.32] uh use uh inside of uh
[L1060] [40:16.92] uh gating and linear layers for this
[L1061] [40:18.28] Transformer as well as the attention
[L1062] [40:20.00] shapes, num heads, that kind of thing.
[L1063] [40:22.92] So, that that is effectively utilizing
[L1064] [40:24.88] the hardware that you're serving on.
[L1065] [40:27.32] And then, the final
[L1066] [40:29.52] uh pillar here is new quantization
[L1067] [40:31.76] methods. And so,
[L1068] [40:34.12] quantization is just something that's uh
[L1069] [40:36.12] been near and dear to my heart that I've
[L1070] [40:37.68] been working on the research side for
[L1071] [40:39.84] ever since I joined Google, and it
[L1072] [40:42.08] really changes what's feasible for uh
[L1073] [40:47.44] the first two. So,
[L1074] [40:49.60] uh that's why,
[L1075] [40:51.08] you know, furthering the state of the
[L1076] [40:52.48] art in terms of how you can compress
[L1077] [40:54.44] models is is also a very important
[L1078] [40:57.04] pillar in the research that my team
[L1079] [40:58.88] does. Generally, uh
[L1080] [41:01.16] uh quantization uh refers to reducing,
[L1081] [41:05.28] in some sense, the size that the neural
[L1082] [41:07.72] nets take up uh in order to represent
[L1083] [41:10.40] their weights. So, typically, a neural
[L1084] [41:13.40] net, when you're training it, uh is
[L1085] [41:16.32] represented as a
[L1086] [41:17.92] uh series of numbers that make up the
[L1087] [41:19.60] matrices inside of the neural net uh
[L1088] [41:21.88] that are stored in FP32, 32-bit
[L1089] [41:24.92] floating-point weights.
[L1090] [41:26.40] Um it turns out that, when you do these
[L1091] [41:30.24] computations, you don't need all of that
[L1092] [41:32.44] extra precision to still maintain the
[L1093] [41:34.24] quality of your neural net. And you can,
[L1094] [41:37.08] with pretty simple methods, reduce the
[L1095] [41:40.20] precision at which you store these
[L1096] [41:42.32] weights down to 4-bits. So, uh all of a
[L1097] [41:45.92] sudden, this huge range of numbers uh
[L1098] [41:49.64] that we would take, you know, this float
[L1099] [41:51.88] 32 to represent, uh something that gets
[L1100] [41:54.40] you down to like, you know, seven digits
[L1101] [41:56.76] of precision,
[L1102] [41:58.28] uh can,
[L1103] [42:00.12] you know, with somewhat high fidelity,
[L1104] [42:02.76] uh still be um
[L1105] [42:04.76] represented well by
[L1106] [42:07.16] 4-bit ints, which, you know, just cover
[L1107] [42:09.08] this uh tiny range of like minus eight
[L1108] [42:11.08] to seven. And
[L1109] [42:13.52] um
[L1110] [42:14.08] it's it's kind of a miracle that you can
[L1111] [42:15.60] do this.
[L1112] [42:17.24] But what's even more of a miracle is
[L1113] [42:19.36] that you can apply these kind of
[L1114] [42:21.68] quantization transforms to the runtime
[L1115] [42:25.00] activations that the neural net
[L1116] [42:26.28] processes. And as soon as you do that,
[L1117] [42:29.40] the actual math that you're performing,
[L1118] [42:31.52] because you're taking much smaller
[L1119] [42:34.16] operands to your matmul than what you
[L1120] [42:36.32] were doing before,
[L1121] [42:37.88] the amount of electricity that it takes
[L1122] [42:39.36] to compute the neural net drops
[L1123] [42:41.32] significantly.
[L1124] [42:42.56] And what's interesting is that
[L1125] [42:44.92] like 99% of the total cost of operation
[L1126] [42:48.12] for
[L1127] [42:49.36] AI hardware comes from the
[L1128] [42:53.20] uh power that it takes to run these
[L1129] [42:54.56] chips. And so, if you can do these
[L1130] [42:57.00] operations, you could just make neural
[L1131] [42:58.96] nets run more cheaply, run more
[L1132] [43:00.52] efficiently.
[L1133] [43:02.56] That helps
[L1134] [43:04.28] uh
[L1135] [43:04.84] uh in terms of like serving more
[L1136] [43:05.96] requests, and it helps in terms of
[L1137] [43:07.72] latency.
[L1138] [43:09.76] So, the name of the game for quant
[L1139] [43:11.80] research is how do we push the frontier
[L1140] [43:13.64] beyond like this like four-bit range?
[L1141] [43:16.48] >> There's this take that I see on Twitter
[L1142] [43:18.64] all the time, um which is just talking
[L1143] [43:21.00] about MFU, and someone who's not in the
[L1144] [43:23.08] space, or model flops utilization.
[L1145] [43:26.08] Someone who's not in the space, they see
[L1146] [43:27.52] a number in the low 10s, and they think,
[L1147] [43:30.24] "Wow, they're wasting all of those GPU
[L1148] [43:32.04] resources."
[L1149] [43:33.48] Um I was curious if you could just
[L1150] [43:36.16] clarify that for people why a low MFU,
[L1151] [43:39.52] or I guess naively low, is actually not
[L1152] [43:42.04] low at all. And maybe also explain what
[L1153] [43:43.88] MFU is.
[L1154] [43:44.76] >> Yeah, so
[L1155] [43:46.60] when we compute MFU, you want to divide
[L1156] [43:50.28] the actual number of flops that the
[L1157] [43:52.60] neural net is performing here by the
[L1158] [43:55.08] total number of flops that the
[L1159] [43:56.56] accelerator could have done in the time
[L1160] [43:58.64] of your request. And so, in some sense,
[L1161] [44:01.64] this is giving us the
[L1162] [44:04.20] uh percent of time that we're usefully
[L1163] [44:07.36] utilizing the flops rate of the
[L1164] [44:09.56] accelerator. And to get to 100% MFU, you
[L1165] [44:13.40] would just need be need to be fully
[L1166] [44:15.00] utilizing uh the matmul unit of uh
[L1167] [44:17.92] whatever accelerator uh you're doing
[L1168] [44:20.00] here. So, it would just have to be doing
[L1169] [44:21.20] like a bunch of matmuls in a loop
[L1170] [44:23.96] uh without reading any memory or doing
[L1171] [44:25.92] any other operations.
[L1172] [44:28.12] That's not a very useful computation. Uh
[L1173] [44:30.92] and in practice,
[L1174] [44:33.72] neural nets have to apply activation
[L1175] [44:37.64] functions or do attention or write
[L1176] [44:41.56] intermediate outputs back to uh HBM. And
[L1177] [44:45.04] all of those different operations
[L1178] [44:47.88] will require utilizing the memory bus or
[L1179] [44:50.56] utilizing vector processing units
[L1180] [44:53.28] uh or simply they might be a
[L1181] [44:56.08] mathematical operations that
[L1182] [44:59.20] the underlying hardware performs more
[L1183] [45:02.00] slowly than they uh than uh it might
[L1184] [45:05.16] perform a matmul.
[L1185] [45:06.49] >> [snorts]
[L1186] [45:06.52] >> And so, all of those things contribute
[L1187] [45:08.48] to not running at the full speed that
[L1188] [45:12.36] the processor is rated at.
[L1189] [45:14.80] Uh and so, that's why you might not see
[L1190] [45:16.44] 100% MFU all the time is cuz,
[L1191] [45:19.00] you know, part of the time your neural
[L1192] [45:20.16] net was, you know, reading and writing
[L1193] [45:21.68] to memory or part of the time it was
[L1194] [45:24.08] doing an operation that uh you know,
[L1195] [45:26.72] fundamentally runs slower than certain
[L1196] [45:29.08] other units on your
[L1197] [45:31.56] on your device. And
[L1198] [45:34.40] I think quite a bit of this inference
[L1199] [45:36.64] co-design work that I talked about
[L1200] [45:38.12] earlier is
[L1201] [45:39.76] across all of the different
[L1202] [45:42.36] um
[L1203] [45:43.32] capabilities of the chip. So, uh
[L1204] [45:45.48] communication to other chips,
[L1205] [45:47.96] um memory bandwidth, the the speed at
[L1206] [45:49.68] which we can read parameters from
[L1207] [45:51.40] memory,
[L1208] [45:53.76] flops, of course. Uh
[L1209] [45:55.84] this can be matmul flops. This can be
[L1210] [45:58.52] flops for processing uh
[L1211] [46:01.24] vectors. So, like things like doing
[L1212] [46:02.88] activations.
[L1213] [46:04.16] Uh all of these have different rates in
[L1214] [46:06.52] the hardware.
[L1215] [46:07.64] And a given computation isn't going to
[L1216] [46:09.68] match the natural hardware's rate
[L1217] [46:13.48] uh of each of those operations. So, when
[L1218] [46:17.04] you design a neural net, you want to be
[L1219] [46:19.60] able to choose shapes for this neural
[L1220] [46:21.96] net that fully saturate all of those
[L1221] [46:25.48] hardware units to get you as high of an
[L1222] [46:27.36] MFU as possible
[L1223] [46:29.24] um when you are doing uh inference here.
[L1224] [46:32.60] What makes this
[L1225] [46:34.56] more than just an algebra problem is
[L1226] [46:37.00] that those choices translate to
[L1227] [46:39.52] different quality outcomes when you
[L1228] [46:41.24] actually train this neural net.
[L1229] [46:43.44] So, the process of this kind of
[L1230] [46:45.24] inference co-design is how do we come up
[L1231] [46:49.24] with neural architectures that
[L1232] [46:51.92] scale predictably
[L1233] [46:54.16] have a good prediction, so are high
[L1234] [46:55.80] quality
[L1235] [46:57.04] and still
[L1236] [46:58.64] make the MFU as large as possible during
[L1237] [47:00.56] inference. And so, this kind of joint
[L1238] [47:02.88] optimization is what makes inference
[L1239] [47:05.08] co-design really fun.
[L1240] [47:07.00] Uh and also this kind of evergreen
[L1241] [47:08.36] problem because as the hardware changes
[L1242] [47:11.44] all of those relative constants of flops
[L1243] [47:14.16] to memory bandwidth to communication
[L1244] [47:16.44] bandwidth change and those will have
[L1245] [47:18.44] different implications to what's the
[L1246] [47:21.00] optimal neural net shape should be.
[L1247] [47:23.20] >> On another topic
[L1248] [47:25.24] Google has this idea of a spot bonus
[L1249] [47:27.80] where someone can kind of give you uh a
[L1250] [47:30.24] one-off
[L1251] [47:31.72] lump sum of money as a thank you for
[L1252] [47:34.40] like good performance. And I I saw on
[L1253] [47:36.72] your resume that Jeff Dean, the legend
[L1254] [47:39.28] himself, gave you a spot bonus. And you
[L1255] [47:41.72] know, if you can tell that story, I'd
[L1256] [47:43.00] love to hear why did he give you a spot
[L1257] [47:44.96] bonus?
[L1258] [47:46.08] >> Yeah, so that one actually was at the
[L1259] [47:48.20] very beginning of the Gemini program.
[L1260] [47:53.16] Uh he gave out a spot bonus to people
[L1261] [47:54.88] who
[L1262] [47:55.92] hopped on and launched the first version
[L1263] [47:58.44] of Bard. And like I had a you know a
[L1264] [48:01.48] very small contribution to a very very
[L1265] [48:03.44] large project at the time.
[L1266] [48:05.76] Uh I helped with uh SFT for
[L1267] [48:08.44] uh one of the first versions uh of
[L1268] [48:11.32] uh supervised fine-tuning for one of the
[L1269] [48:12.88] first versions of uh
[L1270] [48:14.64] Bard that got released like right, you
[L1271] [48:16.80] know.
[L1272] [48:17.80] The biggest lesson
[L1273] [48:19.76] out of
[L1274] [48:20.76] uh that experience was
[L1275] [48:23.08] you know, at that time
[L1276] [48:25.44] I was just doing like pure research in
[L1277] [48:28.68] um uh Google Brain.
[L1278] [48:30.48] And I was super focused on just how do I
[L1279] [48:33.52] maximize the number of first author
[L1280] [48:35.04] papers at uh NeurIPS, ICML, ICLR. And
[L1281] [48:41.28] I remember distinctly thinking like I I
[L1282] [48:44.20] had this instinct of like oh like, you
[L1283] [48:47.08] know, should I just keep my head down
[L1284] [48:48.92] and try to write more papers? And
[L1285] [48:51.32] Luckily at the time uh my my manager
[L1286] [48:54.68] Rohan Aneja, like he really encouraged
[L1287] [48:56.96] all of us to get involved in
[L1288] [49:00.20] uh you know, this space.
[L1289] [49:02.28] And
[L1290] [49:03.96] that was just the right motivation that
[L1291] [49:06.36] I needed to like roll up sleeves, do a
[L1292] [49:09.08] bunch of hyperparameter tuning and
[L1293] [49:11.48] engineering work to get uh this uh model
[L1294] [49:15.00] running on uh uh some like really old
[L1295] [49:18.36] TPUs to get some extra you know, cycles
[L1296] [49:21.72] in for for
[L1297] [49:23.24] uh SFT attempts.
[L1298] [49:25.40] That very small initial engagement that
[L1299] [49:27.88] was recognized by Jeff Dean, I I think
[L1300] [49:30.40] blossomed into more and more investments
[L1301] [49:33.48] on the LLM side by me and
[L1302] [49:36.16] ultimately led me to where I am today.
[L1303] [49:39.40] Uh so
[L1304] [49:40.60] yeah, I would say
[L1305] [49:42.04] you know, it it's less so about you
[L1306] [49:44.20] know, [snorts]
[L1307] [49:45.04] you know, how much that like SFT helped
[L1308] [49:47.40] the initial release and it's much more
[L1309] [49:48.96] about uh
[L1310] [49:50.48] uh recognizing that like
[L1311] [49:53.52] there's there's quite a bit of work,
[L1312] [49:55.44] some of it not glamorous, some of it
[L1313] [49:56.92] just like, you know, hyperparameter
[L1314] [49:58.20] tuning and,
[L1315] [49:59.68] uh, golfing the XLA compiler to make
[L1316] [50:02.68] your program fit in a certain memory
[L1317] [50:04.60] amount
[L1318] [50:05.88] that contributes to a wider business
[L1319] [50:07.76] goal that
[L1320] [50:08.92] is is really quite important for
[L1321] [50:11.56] getting involved in in very high-value
[L1322] [50:13.80] projects.
[L1323] [50:14.96] >> You've been working on Gemini for a
[L1324] [50:16.44] while now, and because it's a top
[L1325] [50:18.08] priority, there has to be some, you
[L1326] [50:21.00] know, incidents or war stories that
[L1327] [50:23.12] you've been involved in. So, I'm
[L1328] [50:24.80] curious, you know, what's your favorite,
[L1329] [50:27.68] uh, war story when working on Gemini?
[L1330] [50:30.80] >> So, I think my all-time favorite
[L1331] [50:33.56] would have to be
[L1332] [50:36.96] Flash 2.0.
[L1333] [50:39.52] Uh, so this one this one was quite a
[L1334] [50:42.36] challenge and a very long journey to get
[L1335] [50:44.36] there.
[L1336] [50:45.80] But,
[L1337] [50:47.28] uh, one of the
[L1338] [50:49.04] main things that we were optimizing for,
[L1339] [50:51.92] which which Flash 1.5 established, is
[L1340] [50:54.36] this category of very fast, low-latency
[L1341] [50:57.60] model
[L1342] [50:59.08] that's still
[L1343] [51:00.40] quite good. Um, and, you know,
[L1344] [51:04.04] in particular, it has to be fast because
[L1345] [51:06.44] it's it's used by search to serve,
[L1346] [51:09.04] uh,
[L1347] [51:09.72] responses in in AI mode, uh, very
[L1348] [51:11.96] quickly.
[L1349] [51:14.16] Because of that,
[L1350] [51:16.24] uh, for Flash 1.5 and before, we we
[L1351] [51:18.48] focused on dense models, which, uh,
[L1352] [51:21.24] allow you to respond very quickly.
[L1353] [51:25.16] Even though at the time we we knew about
[L1354] [51:26.68] MoE models and how they increase
[L1355] [51:28.12] capacity.
[L1356] [51:29.44] And so, I think, um,
[L1357] [51:32.40] one thing that like came up was, okay,
[L1358] [51:35.72] like
[L1359] [51:37.04] we sure would like to use this new
[L1360] [51:38.44] architecture, but it it's difficult to
[L1361] [51:41.36] just simply switch to an MoE because
[L1362] [51:44.08] what happens with an MoE is it it uses a
[L1363] [51:45.88] lot more parameters in general
[L1364] [51:48.40] and because it uses more parameters, it
[L1365] [51:50.16] takes up more HBM.
[L1366] [51:52.68] These chips that we serve on have a
[L1367] [51:54.68] finite amount of HBM, so you have to
[L1368] [51:56.56] shard the MOE across
[L1369] [51:59.76] multiple different chips. So, if you
[L1370] [52:01.52] have, you know, whatever NX birds then
[L1371] [52:04.56] you might chart it across N chips or,
[L1372] [52:06.40] you know, some factor of N.
[L1373] [52:08.64] And what this causes is a lot of
[L1374] [52:11.80] communication in the middle of the
[L1375] [52:13.80] model. When you have a token that needs
[L1376] [52:17.16] to be routed to an expert and that token
[L1377] [52:19.84] might live on the first TPU, but it
[L1378] [52:21.36] needs to go to the last TPU, that's a
[L1379] [52:23.36] lot of communication that you're
[L1380] [52:24.60] inducing in the forward pass. So, the
[L1381] [52:27.56] latency of this operation
[L1382] [52:31.48] like increases dramatically with N.
[L1383] [52:35.04] And
[L1384] [52:36.16] you know, the challenge with MOEs is
[L1385] [52:37.44] they increase N. So,
[L1386] [52:39.68] that that that like kind of really
[L1387] [52:41.76] bottleneck this approach.
[L1388] [52:44.68] And one interesting thing that happened
[L1389] [52:47.44] was we we definitely knew about pipeline
[L1390] [52:51.60] serving for a while.
[L1391] [52:53.96] It's just in the dense case
[L1392] [52:55.96] it never really ended up mattering. Like
[L1393] [52:58.08] I distinctly remember a very early
[L1394] [52:59.76] conversation I had with Sholto about it
[L1395] [53:01.64] and Sholto's like, "Oh yeah, you're like
[L1396] [53:03.64] so flop bound and so pipelining is just
[L1397] [53:06.20] not going to change your prefill
[L1398] [53:07.12] profile." And then he was right. I
[L1399] [53:08.68] tested it out and like then abandoned
[L1400] [53:10.36] the idea.
[L1401] [53:12.20] But what's interesting is
[L1402] [53:15.48] I I had a very small team at the time
[L1403] [53:17.28] and and one of my reports, Gangyan,
[L1404] [53:20.48] had a very nice idea. He was working
[L1405] [53:22.24] with Rahul Arya and a couple folks from
[L1406] [53:25.16] the Israel team at Google.
[L1407] [53:27.16] And that was to apply pipeline prefill
[L1408] [53:29.24] to MOEs.
[L1409] [53:31.44] And pipelining is
[L1410] [53:35.04] a technique where instead of
[L1411] [53:36.76] parallelizing
[L1412] [53:38.28] those N machines experts across those N
[L1413] [53:40.64] machines, you parallel layers across
[L1414] [53:43.68] those end machines. So, instead of on a
[L1415] [53:46.64] particular layer, you have to route
[L1416] [53:48.24] tokens from machine to machine, now one
[L1417] [53:51.24] layer does the computation for one
[L1418] [53:53.92] subset of your pre-fill request, and
[L1419] [53:56.32] then hands off the processed tokens to
[L1420] [53:59.72] the next machine to process the second
[L1421] [54:01.88] layer, and then the third layer, and the
[L1422] [54:03.12] fourth layer.
[L1423] [54:04.28] And
[L1424] [54:06.12] all of the experts can then stay
[L1425] [54:08.00] resident to a single machine or a
[L1426] [54:09.56] smaller set of machines. So,
[L1427] [54:12.64] what this does effectively is it changes
[L1428] [54:15.64] the communication pattern from something
[L1429] [54:17.72] that required a lot of token exchange on
[L1430] [54:20.96] every single layer to
[L1431] [54:23.68] something that's
[L1432] [54:25.68] actually can be hidden behind other
[L1433] [54:28.16] computation because you can do this
[L1434] [54:31.16] pipeline pre-fill across different parts
[L1435] [54:33.32] of your request.
[L1436] [54:35.00] So,
[L1437] [54:36.16] while layer two is working on the
[L1438] [54:38.84] first thousand tokens of your request,
[L1439] [54:41.44] layer one on the first chip is
[L1440] [54:43.88] processing
[L1441] [54:45.24] the second thousand tokens of your
[L1442] [54:46.80] request. So, it was a way of
[L1443] [54:50.48] breaking this HBM constraint by moving
[L1444] [54:53.92] layers across the machines rather than
[L1445] [54:55.84] moving experts across these machines.
[L1446] [54:58.04] And because of that, the communication
[L1447] [55:00.40] overhead has gone down, and all of a
[L1448] [55:02.52] sudden, MoE latency looks really
[L1449] [55:04.80] attractive now. This, you know, the the
[L1450] [55:07.76] Gemini 2.0 report says like it's an MoE
[L1451] [55:10.60] series of models, and the thing that
[L1452] [55:12.80] made that possible is, you know, or one
[L1453] [55:14.68] of the things that made that possible is
[L1454] [55:16.12] is this
[L1455] [55:18.08] you know, serving time innovation.
[L1456] [55:21.44] Dwarak and Reiner have an amazing post
[L1457] [55:23.44] about exactly this
[L1458] [55:26.40] optimization that you can write up in
[L1459] [55:29.20] the algebra of the scaling book. And
[L1460] [55:31.08] it's just a wonderful example of how
[L1461] [55:33.92] this kind of
[L1462] [55:35.88] change can
[L1463] [55:38.04] uh have really dramatic implications on
[L1464] [55:40.48] LLM quality. What really made Flash 2.0
[L1465] [55:43.44] rewarding is
[L1466] [55:45.16] this, you know, giant MoE decision. It
[L1467] [55:48.16] sounds like a small technical decision
[L1468] [55:49.80] at the time, but
[L1469] [55:51.20] people were really worried about whether
[L1470] [55:53.24] or not the latency of this MoE would
[L1471] [55:55.88] actually be reasonable. Luckily,
[L1472] [55:58.56] I was able to run like a very
[L1473] [55:59.92] transparent technical process to get to
[L1474] [56:01.96] the bottom of this. And by the end of
[L1475] [56:04.24] it, uh uh uh you know, we we made the
[L1476] [56:06.84] right call, uh but then we had to train
[L1477] [56:08.72] it. So,
[L1478] [56:10.92] this was a bigger model than we've ever
[L1479] [56:14.20] trained before at the flash scale, and
[L1480] [56:16.80] like we knew this would be the right
[L1481] [56:18.12] call, but it was just going to be 40
[L1482] [56:20.32] days of grueling work for like a really,
[L1483] [56:22.80] really small team. Like we probably had
[L1484] [56:24.48] like five people on the rotation for
[L1485] [56:28.04] training this model. I remember, you
[L1486] [56:30.56] know, all of us just kind of like
[L1487] [56:32.64] rotated day by day, handing off like,
[L1488] [56:36.00] you know,
[L1489] [56:37.32] all of this like SRE style work of uh
[L1490] [56:40.92] keeping the training job alive, which at
[L1491] [56:43.00] the time was was
[L1492] [56:44.96] a very interactive thing cuz uh you had
[L1493] [56:47.64] to make sure that everything was moving
[L1494] [56:49.16] stably, that, you know, you have tuned
[L1495] [56:51.28] data iterators that aren't slowing down
[L1496] [56:53.76] your job, that, you know, if there's
[L1497] [56:56.36] like a gap in the data somewhere or an
[L1498] [56:58.88] indexing issue, you have to like really
[L1499] [57:01.00] quickly put up a fix because it's, you
[L1500] [57:03.00] know, wasting all of this GPU time. Um
[L1501] [57:05.72] >> What about at night time and on the
[L1502] [57:07.32] weekends?
[L1503] [57:08.28] >> So, yeah, like I think, you know, for
[L1504] [57:10.64] those 40 days, we did not do a lot of
[L1505] [57:12.68] sleeping. Like we had to
[L1506] [57:15.16] like do like kind of these dual shifts
[L1507] [57:17.68] across like the Paris office and
[L1508] [57:19.40] Mountain View, and like the thing that
[L1509] [57:22.64] makes it so rewarding was when this
[L1510] [57:25.44] model came out, like around the same
[L1511] [57:27.68] time, uh DeepSeek V3 came out. And uh
[L1512] [57:32.12] the Wall Street Journal put out this
[L1513] [57:33.64] article that was like this giant red
[L1514] [57:35.52] scare article about how China's going to
[L1515] [57:37.28] take over AI with open source models and
[L1516] [57:41.36] I remember my friend sent me a
[L1517] [57:42.76] screenshot of this table of the LMSYS
[L1518] [57:46.52] Arena leaderboard. And you know, all the
[L1519] [57:49.40] way at the top right you've got
[L1520] [57:52.48] chat GPT and
[L1521] [57:54.80] and DeepSeek right behind it. And like,
[L1522] [57:57.20] oh, DeepSeek was trained for whatever
[L1523] [57:59.92] few million dollars, you know, and and
[L1524] [58:01.88] like they're right there.
[L1525] [58:03.44] And then my friend was like, oh, like
[L1526] [58:06.60] you know, Gemini is so behind cuz they
[L1527] [58:08.80] had, you know, a version of like I think
[L1528] [58:10.68] 1.5 Pro or something in that table at
[L1529] [58:13.24] the very bottom.
[L1530] [58:14.92] And then I looked at it and was like,
[L1531] [58:16.00] oh, that's really interesting. I was
[L1532] [58:17.36] just looking at this leaderboard cuz we
[L1533] [58:20.36] just released a model and it definitely
[L1534] [58:23.44] doesn't look like that when you go to
[L1535] [58:24.96] the website. So, turns out there was
[L1536] [58:28.32] kind of some ill-written rows on the
[L1537] [58:31.92] Wall Street Journal article. And so now
[L1538] [58:35.04] if you go to that article today, you can
[L1539] [58:37.28] see, you know, what at the time was the
[L1540] [58:40.56] state of the art model
[L1541] [58:42.92] you know, Flash 2.0 thinking
[L1542] [58:45.72] up in the top right corner way far ahead
[L1543] [58:47.96] of DeepSeek V3.
[L1544] [58:50.44] Might be messing with the open source
[L1545] [58:52.24] narrative that they were trying to
[L1546] [58:53.36] publish there, but it was a really
[L1547] [58:55.56] important accomplishment for for the
[L1548] [58:57.80] team.
[L1549] [58:59.36] >> Last question for you is if you could go
[L1550] [59:01.76] back to yourself when you just graduated
[L1551] [59:04.84] college, I guess undergrad, and give
[L1552] [59:07.08] yourself some advice knowing what you
[L1553] [59:08.64] know now, what would you say?
[L1554] [59:12.00] >> You you got to chase the problems that
[L1555] [59:16.60] people are facing
[L1556] [59:18.60] like
[L1557] [59:19.64] in the world today. Like like go after
[L1558] [59:23.12] the challenges that people see in
[L1559] [59:25.64] everyday life and don't be afraid to
[L1560] [59:31.56] tackle a smaller part of this problem or
[L1561] [59:34.12] maybe a more menial sounding part of
[L1562] [59:36.04] this problem, even if it's not fancy
[L1563] [59:38.32] research math or something like that.
[L1564] [59:40.12] Like, trust that by working on what's
[L1565] [59:43.24] important, even if it's a smaller part
[L1566] [59:46.16] of a larger project for what's
[L1567] [59:47.40] important, you're going to get to see
[L1568] [59:50.04] what really matters in terms of moving
[L1569] [59:52.36] the frontier forward.
[L1570] [59:53.96] And it's it's this kind of, I guess,
[L1571] [59:58.28] humility maybe in your
[L1572] [01:00:00.72] problem approach that that you should
[L1573] [01:00:03.32] really be chasing.
[L1574] [01:00:05.00] Um that's one piece of advice. I think
[L1575] [01:00:07.68] the other bit that I would give, like
[L1576] [01:00:10.20] maybe as professional advice, perhaps,
[L1577] [01:00:13.92] would be
[L1578] [01:00:16.36] be the kind of co-worker
[L1579] [01:00:19.20] that
[L1580] [01:00:20.72] people would want to see succeed.
[L1581] [01:00:24.84] Uh and so, like what I mean by that is
[L1582] [01:00:28.12] there's this this like conception of
[L1583] [01:00:30.32] like
[L1584] [01:00:31.32] workplace psychopath or Machiavellian
[L1585] [01:00:33.68] leaders or or whatever, people who like
[L1586] [01:00:36.76] will do anything at all costs to get the
[L1587] [01:00:39.24] results they want. And they they they
[L1588] [01:00:41.04] they might be able to squeeze people to
[L1589] [01:00:42.88] get some short-term gain.
[L1590] [01:00:44.84] But,
[L1591] [01:00:46.56] you know, having interacted with a
[L1592] [01:00:48.36] variety of people professionally for so
[L1593] [01:00:51.00] long,
[L1594] [01:00:52.64] what is interesting to me is there have
[L1595] [01:00:55.16] been
[L1596] [01:00:56.52] a select few,
[L1597] [01:00:58.96] you know, one in particular is is
[L1598] [01:01:00.88] probably a very dear friend and and
[L1599] [01:01:04.04] mentor of mine, Todd Lipkin, who first
[L1600] [01:01:06.16] got me into computer science.
[L1601] [01:01:08.12] Um
[L1602] [01:01:09.20] that are just so
[L1603] [01:01:12.96] like kind and
[L1604] [01:01:16.52] like people that you can learn from
[L1605] [01:01:19.52] and uh
[L1606] [01:01:21.20] you know, someone that I can
[L1607] [01:01:24.52] follow and be successful by following.
[L1608] [01:01:28.20] That just genuinely inspire me to want
[L1609] [01:01:31.40] to help them succeed. Uh, and so in
[L1610] [01:01:35.08] particular, if you
[L1611] [01:01:37.76] are the kind of person who
[L1612] [01:01:40.20] helps people succeed in their projects,
[L1613] [01:01:43.20] comes up with projects that can leverage
[L1614] [01:01:46.00] other people's complementary skills in
[L1615] [01:01:48.92] ways that help them shine,
[L1616] [01:01:50.88] people will notice that. People will
[L1617] [01:01:52.36] want to contribute to
[L1618] [01:01:55.40] projects that you come up with in the
[L1619] [01:01:56.76] future
[L1620] [01:01:57.96] and in general will want to support you
[L1621] [01:02:00.48] going forward.
[L1622] [01:02:01.80] And so, you know,
[L1623] [01:02:03.96] you people can get really cynical
[L1624] [01:02:05.84] thinking about the game theory of how to
[L1625] [01:02:07.88] interact at work.
[L1626] [01:02:09.44] Uh, but I found that this kind of more
[L1627] [01:02:13.60] amicable approach
[L1628] [01:02:16.08] generally like it it creates like this
[L1629] [01:02:19.20] this deep sense of collaboration and
[L1630] [01:02:23.60] you know, willingness to help that like
[L1631] [01:02:26.68] is so important to get very large
[L1632] [01:02:28.72] projects that require multiple people
[L1633] [01:02:30.60] and multiple skill sets
[L1634] [01:02:32.72] uh, over the line.
[L1635] [01:02:34.56] And so,
[L1636] [01:02:36.00] yeah, I think if if I could give any
[L1637] [01:02:38.04] kind of like inner you know,
[L1638] [01:02:39.32] interpersonal feedback or professional
[L1639] [01:02:41.24] feedback or whatever to
[L1640] [01:02:43.76] earlier version of myself, it's it's to
[L1641] [01:02:45.80] be that guy. It's to to be the kind of
[L1642] [01:02:47.64] person that other people want to see
[L1643] [01:02:50.16] succeed.
[L1644] [01:02:51.24] >> I love that this advice combats the
[L1645] [01:02:54.12] cynical advice. And I also love that
[L1646] [01:02:56.48] your original post combats the doomer,
[L1647] [01:03:00.00] you know, permanent underclass stuff.
[L1648] [01:03:01.60] So, um, yeah, thank you so much for your
[L1649] [01:03:04.00] time. It's a lot of fun. Really
[L1650] [01:03:05.12] appreciate it.
[L1651] [01:03:05.80] >> Thanks for having me, Ryan.
[L1652] [01:03:07.48] >> Hey, thank you for watching this
[L1653] [01:03:08.48] podcast. If you liked it and you want to
[L1654] [01:03:10.16] see the show grow, please support with a
[L1655] [01:03:12.32] comment or a like.
[L1656] [01:03:14.32] Also, if you Do you any recommendations
[L1657] [01:03:16.16] for people you want me to bring on?
[L1658] [01:03:18.16] Please drop a comment. Guests like
[L1659] [01:03:20.36] Barbara Liskov, Mike Stonebreaker, Mark
[L1660] [01:03:23.08] Brooker, these were all people that I
[L1661] [01:03:25.12] brought on because someone left a
[L1662] [01:03:26.96] comment. On another note, aside from the
[L1663] [01:03:29.20] podcast, I'm working on building the
[L1664] [01:03:31.00] ergonomic keyboard that I wish existed.
[L1665] [01:03:33.48] Here's a glance at the prototype. It's a
[L1666] [01:03:35.36] split keyboard, so there's two sides. Um
[L1667] [01:03:38.36] this is in the case. But yeah, we
[L1668] [01:03:39.84] launched on Kickstarter and we hit our
[L1669] [01:03:41.64] goal within 8 hours of launching. I
[L1670] [01:03:43.72] really appreciate it if you were one of
[L1671] [01:03:45.08] the people who grabbed one of the early
[L1672] [01:03:46.84] units.
[L1673] [01:03:47.96] Um we're now working on the long journey
[L1674] [01:03:49.64] of building the tooling now. And so, if
[L1675] [01:03:51.52] you still want to pick one up, I've left
[L1676] [01:03:53.56] the late pledges open on Kickstarter, so
[L1677] [01:03:56.20] you can grab one there. I'll put a link
[L1678] [01:03:57.80] in the description. Thank you again for
[L1679] [01:04:00.32] watching the podcast, and I'll see you
[L1680] [01:04:02.44] in the next episode.
