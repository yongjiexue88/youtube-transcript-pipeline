Chunk 1; segments 1–358. 

# How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar

Source ID: source-cfa80c9b2999d9de
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/How_Anthropic_Builds_And_How_Engineering_Will_Change_Soon_Thariq_Shihipar_en.txt
Video: https://www.youtube.com/watch?v=2Kch3tWMnw8

[L10] [00:00.00] Most software we wrote before LLMs was
[L11] [00:01.92] not very good.
[L12] [00:03.32] >> This is Tariq. He's an engineer at
[L13] [00:05.24] Anthropic on the Claude code team, and I
[L14] [00:07.48] asked him all about how their
[L15] [00:09.08] engineering team makes the most out of
[L16] [00:10.96] the models today.
[L17] [00:12.28] >> Can you move up like a higher
[L18] [00:14.20] abstraction level, you know, like can
[L19] [00:15.40] you build the system that builds a
[L20] [00:16.76] system?
[L21] [00:17.88] >> Is there something that you feel's kind
[L22] [00:19.76] of the next big shift that is going to
[L23] [00:22.44] diffuse into the industry?
[L24] [00:24.48] >> Yeah, I think there are a few different
[L25] [00:27.20] ones.
[L26] [00:28.40] >> Here's the full episode.
[L27] [00:34.24] My goal with this conversation is to ask
[L28] [00:37.20] you as much as I can about how can you
[L29] [00:39.84] get the most out of the models
[L30] [00:41.52] specifically for software engineering so
[L31] [00:44.08] that people in the industry can kind of
[L32] [00:45.80] learn from the best practices where
[L33] [00:48.48] Anthropic's having success. And so to
[L34] [00:51.36] start the conversation off, I'd like to
[L35] [00:53.16] ask you let's say I was coming from a
[L36] [00:57.16] company that's maybe less AI pilled and
[L37] [00:59.88] I was onboarding onto your team, what
[L38] [01:02.24] are the most impactful things that you'd
[L39] [01:04.60] tell me to start doing to successfully
[L40] [01:07.08] onboard?
[L41] [01:08.28] >> I think the number one tip we have for
[L42] [01:10.48] you know, both people inside and and
[L43] [01:12.00] outside Anthropic is that like if you
[L44] [01:13.96] treat Claude like a thought partner and
[L45] [01:15.96] give it like the context that you need,
[L46] [01:18.76] then you can usually figure out the next
[L47] [01:20.60] steps, you know, and and so I think that
[L48] [01:22.24] like starting with okay, can Claude do
[L49] [01:25.12] it? If not, why not, you know, and
[L50] [01:28.80] uh
[L51] [01:29.56] using that as the starting place, I I
[L52] [01:31.48] think it's really important and I think
[L53] [01:33.80] just like always thinking about like
[L54] [01:35.72] okay, what's
[L55] [01:37.40] you know, reflecting on can you move up
[L56] [01:40.28] like a higher abstraction level, you
[L57] [01:41.64] know, like can you uh you know, set up a
[L58] [01:44.56] system? Can you build the system that
[L59] [01:46.24] builds a system, right? Instead of just
[L60] [01:48.04] like building, you know, the the product
[L61] [01:51.12] itself.
[L62] [01:52.52] >> I remember when we used to onboard
[L63] [01:54.12] people you would get assigned an
[L64] [01:56.32] onboarding buddy, so someone who kind of
[L65] [01:59.20] really knows the code base and you can
[L66] [02:01.00] ask all of your trivial setup questions
[L67] [02:03.04] to. It sounds like Claude fills in a lot
[L68] [02:05.88] of those gaps. And in practice, is it
[L69] [02:09.88] 100% you don't need an onboarding buddy
[L70] [02:12.28] and you can just ask the model for
[L71] [02:13.80] everything?
[L72] [02:14.56] >> You do need an onboarding buddy, but
[L73] [02:16.68] more from like a kind of like social and
[L74] [02:19.24] cultural perspective than a technical
[L75] [02:21.08] perspective, you know what I mean? I
[L76] [02:22.56] think like from a technical perspective,
[L77] [02:24.48] you can basically just like work with
[L78] [02:26.56] Claude and you know, if you're like good
[L79] [02:29.08] at it, like you can get what you need to
[L80] [02:30.64] onboard, but I think just like having
[L81] [02:32.88] the context of you know, how to work
[L82] [02:34.48] with a team and also just like how to
[L83] [02:36.96] like, you know, get buying on what
[L84] [02:38.96] you're building or you know, understand
[L85] [02:41.12] like how the team works together or just
[L86] [02:42.92] even like have a friend to work with,
[L87] [02:44.84] you know, I think is really important.
[L88] [02:46.44] So, yeah, we still have onboarding
[L89] [02:47.92] buddies, but not
[L90] [02:49.24] um
[L91] [02:49.88] it's not like nearly as much technical
[L92] [02:52.00] lift as as it used to be.
[L93] [02:53.80] >> There's a big difference between the
[L94] [02:56.08] external perception of the AI
[L95] [02:58.08] capabilities and the internal Anthropic
[L96] [03:01.48] usage. Because I'll talk to friends,
[L97] [03:03.08] they say, yeah, what Boris is saying is
[L98] [03:05.40] the reality. And so, my question is, why
[L99] [03:09.08] is there such a big difference between
[L100] [03:10.88] that that internal perception and that
[L101] [03:13.68] external perception?
[L102] [03:15.60] >> I think we have a good track record kind
[L103] [03:18.36] of of when we make these like claims,
[L104] [03:20.72] you know, you're like, oh, you're you're
[L105] [03:22.28] like it turns out to be true on the long
[L106] [03:25.00] large enough time scale, you know, I
[L107] [03:26.20] think a lot of engineers are not really
[L108] [03:28.24] in the IDE anymore, you know, like yeah,
[L109] [03:31.04] the code being written is like I I
[L110] [03:34.04] talked to large enterprise customers
[L111] [03:35.56] where like, you know, they haven't like
[L112] [03:37.12] typed a line of code themselves in 6
[L113] [03:38.84] months, right? So, we think of it part
[L114] [03:41.04] of our jobs, you know, to figure out how
[L115] [03:43.88] to work at a higher abstraction level.
[L116] [03:45.32] And like if I spend like a day trying to
[L117] [03:48.28] figure out how to get Claude to the
[L118] [03:50.16] like, you know, do this autonomously and
[L119] [03:52.24] I fail, that's like fine, you know, and
[L120] [03:54.56] maybe even good, you know, cuz now I can
[L121] [03:56.00] be like, oh hey, like Claude is not good
[L122] [03:57.96] at this. How do we make it better, you
[L123] [03:59.60] know? But I think if you're working like
[L124] [04:01.12] an average job, you know, your job is to
[L125] [04:03.60] produce the output and like I think
[L126] [04:05.92] automation always has a cost cuz you're
[L127] [04:07.84] like it's an investment and if it works,
[L128] [04:10.08] then great, you'll make, you know, a
[L129] [04:11.88] return on your investment over time.
[L130] [04:14.36] Um but if it doesn't, then you've like
[L131] [04:15.92] wasted all this time. And so I think the
[L132] [04:18.04] nice thing about the models is that
[L133] [04:20.44] you know, generally the chance of the
[L134] [04:22.36] investment working out is higher and
[L135] [04:24.00] higher because like the models are
[L136] [04:26.00] getting smarter and smarter.
[L137] [04:27.72] Uh but you still have to sort of take
[L138] [04:29.04] that leap as an individual. Your boss is
[L139] [04:31.52] not going to be super happy with you if
[L140] [04:32.80] you're like, you know, uh
[L141] [04:35.28] if you've been working on your harness
[L142] [04:36.88] setup the entire time and like not
[L143] [04:38.44] shipping code.
[L144] [04:39.80] Um
[L145] [04:40.76] but yeah, I think it's mostly just like
[L146] [04:42.68] culture and thinking of it as our job to
[L147] [04:45.00] sort of live in the future and then we
[L148] [04:46.12] try and like build it into the product
[L149] [04:47.84] and our harness as well so that you
[L150] [04:49.96] don't have to do as much manual stuff,
[L151] [04:52.64] yeah.
[L152] [04:53.84] >> Are there examples that you come to mind
[L153] [04:56.20] when you think of things you don't see
[L154] [04:58.16] people doing on Twitter that are really
[L155] [05:01.52] having making a big difference at
[L156] [05:03.00] Anthropic that you'd kind of recommend?
[L157] [05:05.64] >> Like using Claude code for knowledge
[L158] [05:07.76] work, I think it's really valuable. The
[L159] [05:09.80] way a technical person does knowledge
[L160] [05:11.64] work, I think is very different than the
[L161] [05:13.56] way a non-technical person does
[L162] [05:14.92] knowledge work um these days because you
[L163] [05:17.04] can get the models to do it. And so I
[L164] [05:19.16] think like you know, increasingly if you
[L165] [05:21.56] can figure out like, hey, this is a
[L166] [05:23.08] task, the task is made up of code-like
[L167] [05:26.92] things, you know, and like how do I tell
[L168] [05:29.40] the model the code
[L169] [05:31.80] steps to take, you know,
[L170] [05:34.04] uh in order to do it, right? Uh
[L171] [05:36.80] you can like
[L172] [05:38.52] uh
[L173] [05:39.08] you know, I think you can do a lot more,
[L174] [05:40.76] right? So I I think I do like a lot of
[L175] [05:42.80] accounting with Claude code using But
[L176] [05:45.36] the personal side using like uh scripts
[L177] [05:48.00] and Python instead of Excel, you know?
[L178] [05:50.24] Or like I do video editing using FFmpeg
[L179] [05:53.60] and these libraries to render visuals
[L180] [05:56.20] and things like that. And so I think
[L181] [05:58.28] most of the knowledge work is like uh
[L182] [06:01.48] reducible to code and coding agents if
[L183] [06:05.00] you like think about it well, you know,
[L184] [06:07.12] and um
[L185] [06:08.88] I think that that's like one I think
[L186] [06:11.20] like big difference
[L187] [06:13.00] uh that I see like
[L188] [06:15.40] other people doing less of, I think.
[L189] [06:18.32] >> We talked a little bit about the the
[L190] [06:20.32] model and the harness. And
[L191] [06:23.60] uh I want to ask you, what's the
[L192] [06:25.40] relationship between the model and the
[L193] [06:27.04] harness in terms of getting the best end
[L194] [06:28.84] results? And obviously the model's
[L195] [06:30.52] important. So how important is the
[L196] [06:32.08] harness? And are there any examples you
[L197] [06:34.20] could kind of share?
[L198] [06:35.96] >> Yeah, I mean, uh the harness is super
[L199] [06:38.12] important. I I think you I I think that
[L200] [06:41.44] sometimes there's this idea that the
[L201] [06:42.76] harness doesn't matter because the
[L202] [06:43.92] models will get better and better. And
[L203] [06:45.28] if the model just does everything
[L204] [06:47.28] perfectly, then why do you need a
[L205] [06:48.80] harness at all, right? And I think that
[L206] [06:51.20] in practice, what we see is like the
[L207] [06:53.36] models get better and better. And so the
[L208] [06:55.04] harness needs to become more and more
[L209] [06:56.92] complicated uh
[L210] [06:58.84] to
[L211] [07:00.12] allow the model to do more things,
[L212] [07:02.44] right? And so um an example of this is
[L213] [07:05.96] uh auto mode. And so auto mode, you
[L214] [07:08.76] know, is a classifier that runs after
[L215] [07:11.48] every, you know, uh task that you
[L216] [07:14.16] normally have to ask a permission uh
[L217] [07:16.04] prompt for for Claude. And back when we
[L218] [07:18.64] were like, you know, Opus 4 or even Opus
[L219] [07:21.08] 4.5 maybe like uh it was not so bad to
[L220] [07:24.20] hit enter on the permission prompts
[L221] [07:25.72] because like you were you know, the
[L222] [07:27.56] turns would only last a few minutes
[L223] [07:29.12] anyways, right? And now Claude is
[L224] [07:31.32] running, you know, can run for hours.
[L225] [07:33.00] And so you really need that ability for
[L226] [07:36.12] it to you know, like do work safely,
[L227] [07:38.68] stick to your instructions. And auto
[L228] [07:40.84] mode is really complicated software, You
[L229] [07:42.92] know, sandboxing is really complicated
[L230] [07:44.48] software.
[L231] [07:45.76] Um and then like, you know, you also
[L232] [07:47.00] think about things like, okay, like
[L233] [07:48.68] Claude could do so much more work now.
[L234] [07:51.24] Um
[L235] [07:52.16] how does it represent the work that it's
[L236] [07:54.12] done? Like, it's worked for like 8 hours
[L237] [07:56.08] and you want to know what it's done in 8
[L238] [07:57.40] hours, right? So,
[L239] [07:59.00] this is what we use artifacts for,
[L240] [08:00.64] right? And artifacts themselves are a
[L241] [08:02.48] form of prompting cuz like, how does
[L242] [08:04.24] Claude represent that in a useful way,
[L243] [08:06.68] right? Like, there's a lot of different
[L244] [08:07.84] ways that it could uh represent that
[L245] [08:09.64] information.
[L246] [08:11.00] Um and so, I think like roughly
[L247] [08:13.48] what we see is like the harness harness
[L248] [08:16.08] engineering is definitely like this like
[L249] [08:18.32] mix of science and art. I think it's
[L250] [08:20.32] very unintuitive in a lot of different
[L251] [08:22.32] ways. Um but I think it has like just
[L252] [08:25.60] big abilities to like unlock new parts
[L253] [08:29.20] of uh you know, like model behavior. And
[L254] [08:33.04] uh yeah, I just see the harnesses get
[L255] [08:34.64] more and more complicated and it's kind
[L256] [08:36.60] of harder and harder to like
[L257] [08:38.96] actually vibe coordinate your own, which
[L258] [08:41.36] is like a little bit unintuitive to me
[L259] [08:42.88] because of like how good the models have
[L260] [08:44.12] gotten. Uh but yeah, things like auto
[L261] [08:47.20] mode and workflows and things like that
[L262] [08:49.04] that which are like actually quite
[L263] [08:50.84] complicated pieces of software
[L264] [08:53.64] become like really load-bearing, I
[L265] [08:55.64] think.
[L266] [08:56.64] >> As LLMs have advanced, more and more of
[L267] [09:00.68] the human part can be taken out of the
[L268] [09:03.40] loop. You know, at Anthropic, what
[L269] [09:05.60] percent of
[L270] [09:07.24] your or your team's changes are fully
[L271] [09:10.36] autonomously made versus actually
[L272] [09:12.72] pairing with a model like people were
[L273] [09:14.60] doing more of like around a year ago?
[L274] [09:18.36] >> Um I think it's very dependent on, you
[L275] [09:21.44] know, what you consider autonomously
[L276] [09:23.08] made or
[L277] [09:25.36] um what
[L278] [09:27.76] uh what team or what function you're
[L279] [09:29.84] working on as well. You know, for
[L280] [09:31.60] example, a designer might give you a
[L281] [09:33.44] Figma file and then you pass the Figma
[L282] [09:36.16] file to Claude Code. Uh Cloud Code is
[L283] [09:38.76] great at using the Figma MCP, but like,
[L284] [09:40.48] you know, the designers put a lot of
[L285] [09:41.72] work in there.
[L286] [09:43.20] Um I think that like roughly
[L287] [09:46.16] um
[L288] [09:46.84] our goal is to sort of get Cloud being
[L289] [09:49.20] able to do all of the like
[L290] [09:51.52] uh
[L291] [09:52.84] the glue work that like ties everything
[L292] [09:55.00] together, right? So, like, okay, you've
[L293] [09:56.08] got like a Figma file. Do I really need
[L294] [09:57.76] to like rewrite that in React or
[L295] [09:59.48] something? Like, probably not, right?
[L296] [10:00.56] Like, I I think like that work has been
[L297] [10:03.08] done once, right? And so, the way I
[L298] [10:05.32] think about it is like, what's the
[L299] [10:06.32] unique work that I need to do every day,
[L300] [10:08.96] right? And uh the more I'm like doing
[L301] [10:13.00] that unique work, the better. And And
[L302] [10:14.96] like, I think there's just a ton of
[L303] [10:16.28] demand for
[L304] [10:17.60] you know, unique work and thinking. And
[L305] [10:19.56] the more I'm doing something I've done
[L306] [10:20.88] before, I'm like, okay, like, can can
[L307] [10:23.20] Cloud do this? Or like, if I'm just
[L308] [10:25.08] translating what someone else has done,
[L309] [10:26.84] you know, I'm like, oh, like, can Cloud
[L310] [10:28.28] do this as well?
[L311] [10:29.68] It's really blurring the lines of like,
[L312] [10:31.88] what what does it mean? Even Even if
[L313] [10:33.52] Cloud has fully generated this PR,
[L314] [10:35.92] you've probably done a lot of
[L315] [10:38.24] uh made a lot of decisions and and add a
[L316] [10:40.00] lot of context along the way, so.
[L317] [10:42.52] >> How close are we to a world where
[L318] [10:43.80] someone just says, "Hey, Cloud,
[L319] [10:45.68] here's the ticket. Just
[L320] [10:47.68] don't tell me till you're done."
[L321] [10:50.88] >> Yeah, so I mean, it depends on how good
[L322] [10:52.44] the ticket is. If someone has like
[L323] [10:54.24] perfectly written out essentially like a
[L324] [10:56.04] software spec for this ticket, then
[L325] [10:58.44] yeah, actually Cloud can probably do
[L326] [11:00.08] that, right? But I think that like um to
[L327] [11:03.84] start, you know, like let's say that we
[L328] [11:05.44] get a GitHub issue, that you know, is
[L329] [11:08.28] this worth fixing? Is this a feature
[L330] [11:10.80] like often times issues are like also
[L331] [11:13.12] feature requests or something where
[L332] [11:14.48] there might be like multiple things
[L333] [11:15.72] happening that maybe you combine
[L334] [11:17.48] together in a different way, you know
[L335] [11:19.12] what I mean? And so, I think that there
[L336] [11:20.48] is
[L337] [11:21.44] a a lot of that work is like, okay,
[L338] [11:23.72] what's the vision for the product? Where
[L339] [11:25.36] Where do we want to go? How do we like,
[L340] [11:27.68] you know,
[L341] [11:28.76] um
[L342] [11:29.36] make sure what we we're building is
[L343] [11:30.68] cohesive. And so, I I think for a
[L344] [11:33.64] specific spec like a specific enough
[L345] [11:36.88] spec, Claude can do it. In practice,
[L346] [11:39.56] people don't have haven't figured out
[L347] [11:43.24] what they really want, you know? And
[L348] [11:45.52] haven't figured out the unknowns or the
[L349] [11:47.64] shape of the problem and things like
[L350] [11:49.24] that. And maybe the way you would have
[L351] [11:51.56] done it before is like you start writing
[L352] [11:53.00] the code and you're like, "Oh, like what
[L353] [11:54.16] am I supposed to do now?" Like or like,
[L354] [11:55.44] you know, like you you figured out that
[L355] [11:56.92] way. Uh now, I think you need like new
[L356] [11:59.20] ways of figuring out what you don't know
[L357] [12:01.08] yet, right? And I think you can still
[L358] [12:02.96] chat to Claude really.
[L359] [12:04.68] Um but I think
[L360] [12:06.32] uh that's the hard part. And I think
[L361] [12:08.36] definitely a failure mode is like
[L362] [12:10.60] you you tag Claude tag and you're like,
[L363] [12:12.60] "Hey, please do this."
[L364] [12:14.52] You know, one sentence or less
[L365] [12:16.16] description, no previous context or
[L366] [12:18.48] memory,
[L367] [12:19.80] um and then it does it and you're like,
