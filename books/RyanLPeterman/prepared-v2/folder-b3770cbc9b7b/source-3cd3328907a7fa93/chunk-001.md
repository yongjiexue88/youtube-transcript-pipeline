Chunk 1; segments 1–404. 

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
