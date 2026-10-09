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
[L368] [12:21.20] "Oh, no, I don't like it." You know, and
[L369] [12:23.00] then you're like, you know, just
[L370] [12:25.00] iterating forever on that, right? Versus
[L371] [12:26.84] like figuring out what you actually want
[L372] [12:28.84] like really quickly.
[L373] [12:30.88] >> When I was working at Meta, like the
[L374] [12:32.92] ambiguity of the task really ranges
[L375] [12:36.60] often times proportional to people's I
[L376] [12:39.04] mean, levels aren't everything in
[L377] [12:41.28] software engineering, but it's roughly
[L378] [12:43.76] senior engineers kind of take that
[L379] [12:46.28] ambiguous uh business need and convert
[L380] [12:49.08] it into something that's a lot more
[L381] [12:51.00] concrete. And then people who are maybe
[L382] [12:53.64] newer in their careers, they kind of do
[L383] [12:55.88] the implementation work. Um and like
[L384] [12:58.56] intern projects were kind of almost line
[L385] [13:01.12] by line specified. If I was still uh
[L386] [13:04.44] working at Meta and I had an intern, I
[L387] [13:06.08] was like
[L388] [13:07.40] just kind of give the give Claude my
[L389] [13:09.96] intern's back and it would kind of do
[L390] [13:11.80] it.
[L391] [13:12.72] What kind of work does an intern do then
[L392] [13:15.20] at Anthropic if Claude can kind of
[L393] [13:17.48] handle it?
[L394] [13:18.64] >> What we see in practice is that there
[L395] [13:21.44] are just so many new types of work that
[L396] [13:23.40] no one has ever done before, right? And
[L397] [13:25.48] I think that like we all have to figure
[L398] [13:27.16] that out and so for example, how do you
[L399] [13:30.00] do an eval, you know what I mean,
[L400] [13:32.12] against like
[L401] [13:34.44] uh these new coding behaviors, right?
[L402] [13:36.24] Like how do you make sure like
[L403] [13:38.68] uh that like, you know, how do you
[L404] [13:40.64] measure Claude's performance across like
[L405] [13:42.96] millions and millions of users, uh
[L406] [13:45.00] million across doing all sorts of tasks.
[L407] [13:47.40] Sometimes these tasks might have
[L408] [13:48.48] trade-offs, you know, so I think there
[L409] [13:49.92] is a lot of new work to be done,
[L410] [13:53.60] especially like in the research side of
[L411] [13:55.40] things and um I think that like it's
[L412] [13:58.96] harder and harder to write those specs,
[L413] [14:01.40] but there's also less and less
[L414] [14:02.88] experience that is relevant, you know
[L415] [14:05.88] what I mean? And so like I think that
[L416] [14:08.00] yes, having some experience means that
[L417] [14:09.88] you can sort of like
[L418] [14:11.32] you know,
[L419] [14:12.52] you know how to get work done and you
[L420] [14:15.08] know how to like learn, but I think you
[L421] [14:17.16] also get those skills out of college and
[L422] [14:19.04] and you know, now I think as an intern
[L423] [14:22.40] trying to figure out like, okay, what
[L424] [14:23.52] are the things that people have not done
[L425] [14:25.28] before and and doing that I think is
[L426] [14:26.88] really exciting and I think that there
[L427] [14:28.76] is um
[L428] [14:30.68] Yeah, I think internships are less write
[L429] [14:32.56] the react code, you know what I mean,
[L430] [14:34.44] and there's so many new problems to
[L431] [14:36.00] solve. We need people to solve them.
[L432] [14:37.96] It's helpful if you have fresh set of
[L433] [14:40.04] eyes on it, you know? Um
[L434] [14:42.60] but it is definitely be more proactive
[L435] [14:44.44] and like opportunistic maybe than uh
[L436] [14:47.16] than before or if you're it was maybe
[L437] [14:48.80] more of like a pipeline.
[L438] [14:51.16] >> We talked a little bit about knowledge
[L439] [14:52.92] work and that makes me think of computer
[L440] [14:55.72] use and browser use and I want to ask
[L441] [14:58.80] you, you know, how far away is that from
[L442] [15:01.72] being widely adopted in the industry and
[L443] [15:05.20] impactful? Maybe you can talk about how
[L444] [15:08.16] Anthropic uses it since it feels like
[L445] [15:09.84] you're always far ahead.
[L446] [15:11.24] >> I I think computer and browser use the
[L447] [15:12.80] models have gone a lot better. Opus 5 I
[L448] [15:15.32] think is like a really good computer use
[L449] [15:16.88] model, but there are like these weird
[L450] [15:18.68] edge cases where like for example, it
[L451] [15:21.04] can't type a password on my behalf
[L452] [15:22.84] because my passwords are in one password
[L453] [15:25.28] or something and
[L454] [15:26.64] you know, it can't access that and so
[L455] [15:28.40] like it gets stuck and um I think
[L456] [15:30.76] there's still like those edge cases
[L457] [15:32.12] which are kind of UXE edge cases. Um
[L458] [15:35.96] and then I think also obviously computer
[L459] [15:37.56] uses also
[L460] [15:39.12] uh you know, the more and more people
[L461] [15:41.24] turn APIs and MCPs into like new ways to
[L462] [15:45.16] use Claude. I think that can also take a
[L463] [15:47.96] lot of the use cases that you're using
[L464] [15:50.48] computers for, right? And so going back
[L465] [15:52.20] to like oh yeah, knowledge work
[L466] [15:53.40] everything is code. I think like you
[L467] [15:56.32] know, there are some things where
[L468] [15:57.84] there's no API, there's no way to
[L469] [16:00.68] execute in code other than just like
[L470] [16:02.60] opening up your browser. But I think
[L471] [16:04.32] increasingly there are more and more
[L472] [16:05.64] ways and I think yeah, Claude tag is a
[L473] [16:07.48] great example of like we've just sort of
[L474] [16:08.88] like tried to
[L475] [16:10.48] roll up all these things into APIs that
[L476] [16:13.36] it can use and so
[L477] [16:15.36] um it feels like it can do a lot of work
[L478] [16:17.40] on your behalf even though even though
[L479] [16:18.84] it's not
[L480] [16:20.52] literally running like a virtual
[L481] [16:21.88] computer and clicking things, you know.
[L482] [16:24.16] >> I have noticed that whenever I use
[L483] [16:26.68] uh any kind of computer use tooling, it
[L484] [16:29.28] feels
[L485] [16:30.36] painfully slow. I I look at the cursor
[L486] [16:32.56] and it's sitting there for 10 seconds,
[L487] [16:34.84] moves over, you know, goes there for 10
[L488] [16:36.80] seconds. What where is all that latency
[L489] [16:39.20] coming from? Do you have a sense?
[L490] [16:41.20] >> I think that like it's hard to make a
[L491] [16:42.88] small model that's really really good at
[L492] [16:44.52] it. I think just cuz there's a lot of
[L493] [16:46.44] knowledge that you need to have about
[L494] [16:48.64] this task and how these things work
[L495] [16:50.44] together and stuff and so
[L496] [16:52.68] um you want like a smart model and smart
[L497] [16:54.44] models, you know, take a little bit
[L498] [16:55.68] longer time. It it's like I think a lot
[L499] [16:58.40] of people thought we'd get here sooner,
[L500] [17:00.28] but I think it's just been a harder task
[L501] [17:01.56] than we expected. Um I think like one
[L502] [17:03.88] thing I've someone's told me about
[L503] [17:05.72] computers before is that like
[L504] [17:08.00] it's a state machine where you don't
[L505] [17:09.76] control the entire state. If you are on
[L506] [17:12.20] the DoorDash website or something you
[L507] [17:13.52] want to add something to the cart and
[L508] [17:15.12] you add it incorrectly, now you have
[L509] [17:17.64] this new flow to like undo it. You know,
[L510] [17:20.24] now you need to go click and now you
[L511] [17:22.16] need to go delete it and you can make a
[L512] [17:23.92] mistake along that side as well, right?
[L513] [17:25.84] Whereas like in code, you can sort of
[L514] [17:27.80] like undo, get, you know, whatever. You
[L515] [17:29.88] control all of the state.
[L516] [17:31.80] Um but for computer use like each action
[L517] [17:34.64] is
[L518] [17:35.72] if not irreversible, it's like
[L519] [17:38.28] uh
[L520] [17:38.84] you know, much harder to review reverse
[L521] [17:40.68] than than others.
[L522] [17:42.48] >> Anthropic,
[L523] [17:44.08] um I get the sense that employees have a
[L524] [17:47.56] lot of budget in terms of the compute to
[L525] [17:50.08] kind of speed up whatever it is they
[L526] [17:52.04] need to do. And so, to if we were to
[L527] [17:54.64] spur the imagination of people who use
[L528] [17:57.56] the models to make them more productive,
[L529] [18:01.16] assuming they had infinite compute, like
[L530] [18:03.44] what what type of workflows would you
[L531] [18:05.96] start telling someone to do if they had
[L532] [18:08.56] infinite compute?
[L533] [18:10.16] >> I I think this difference is slightly
[L534] [18:13.00] more exaggerated than you'd think, I
[L535] [18:15.40] think. You know what I mean? I think
[L536] [18:16.48] that like, for example, I use my Mac sub
[L537] [18:20.92] on the weekends and I have almost never
[L538] [18:24.08] hit a 5-hour limit. I think the models
[L539] [18:26.04] are really smart and I think that like a
[L540] [18:28.96] lot of times when we're spending a lot
[L541] [18:31.48] of compute, we're just trying to find
[L542] [18:34.08] sort of capabilities or we're trying a
[L543] [18:35.96] bunch of different things and and it's
[L544] [18:37.72] more about like us figuring out model
[L545] [18:39.32] possibilities, you know what I mean?
[L546] [18:41.40] Than getting a lot of work done. When
[L547] [18:43.52] we're testing for math, for example,
[L548] [18:45.16] we're trying to understand how smart is
[L549] [18:46.92] the prob the the model and that is
[L550] [18:49.56] useful to us. That's useful output to
[L551] [18:51.16] work and it can also sometimes solve
[L552] [18:53.64] like the Riemann hypothesis or something
[L553] [18:55.36] or like not make progress, you know what
[L554] [18:57.32] I mean? People can replicate what we do
[L555] [19:00.20] at home just by thinking at a higher
[L556] [19:02.16] level of abstraction. For example, I'm
[L557] [19:04.56] trying to like get Claude to draft
[L558] [19:06.48] feedback for you. And so,
[L559] [19:09.32] I want the funnel for like Claude to
[L560] [19:11.76] draft with some feedback to the user has
[L561] [19:13.80] submitted feedback to be really good,
[L562] [19:15.76] right? And so I monitor that funnel and
[L563] [19:18.20] then I ask Claude
[L564] [19:20.24] I I had some ideas, but then I was also
[L565] [19:22.16] like, "Oh, what if I ask Claude to try
[L566] [19:24.76] and improve the funnel, you know?" And
[L567] [19:26.80] it'd be like, "Here are some ideas. Can
[L568] [19:28.16] you come up with some as well? Let's
[L569] [19:29.52] figure it out." All of those things you
[L570] [19:31.96] can kind of do yourself right now, you
[L571] [19:33.60] know, if you're like, "Okay, let me when
[L572] [19:36.12] I'm making a feature, let me like
[L573] [19:38.48] uh annotate it with the events, you
[L574] [19:40.52] know, let me make sure that Claude has
[L575] [19:42.36] access to those events. Uh let me run a
[L576] [19:45.08] loop in the morning every day to check,
[L577] [19:48.12] you know, what events are fired and what
[L578] [19:51.00] changes were made. Maybe even like let
[L579] [19:53.12] me proactively suggest some ideas,
[L580] [19:54.96] right? This can all happen, I think,
[L581] [19:57.08] within a fairly reasonable amount of
[L582] [19:58.60] compute. I actually what I see more
[L583] [20:00.52] often is people running into limits
[L584] [20:02.28] where they've actually done kind of the
[L585] [20:04.08] opposite. They've started with a small
[L586] [20:06.16] mid-scope task, you know, it's like,
[L587] [20:07.84] "Oh, hey, like uh you know, refactor
[L588] [20:10.72] this function in this way." And then
[L589] [20:12.96] Claude does it and and maybe it's like
[L590] [20:15.12] has some follow-on effects cuz like
[L591] [20:16.76] refactoring this has means you have to
[L592] [20:18.40] do some other work, too, and that's not
[L593] [20:20.64] exactly correct or like, you know, you
[L594] [20:22.68] you're iterating there and it's like,
[L595] [20:24.12] you know, you just spent a lot of time
[L596] [20:26.04] whereas
[L597] [20:27.28] uh
[L598] [20:28.16] if you had sort of like stepped up a
[L599] [20:29.64] level, told Claude your goals, then
[L600] [20:32.16] figure out like, "Okay, what are the
[L601] [20:33.52] details
[L602] [20:34.64] you know, do some exploration, uh maybe
[L603] [20:37.44] write out the schema or like, you know,
[L604] [20:39.04] and and then work with it. Then let it
[L605] [20:40.96] run. You could probably get the same
[L606] [20:43.88] output.
[L607] [20:45.12] >> I remember it was going kind of viral
[L608] [20:47.36] this idea of creating loops. Um
[L609] [20:51.28] and I mean that that does feel like a
[L610] [20:53.04] pretty
[L611] [20:54.56] uh expensive sort of thing to set up if
[L612] [20:57.36] you're just asking it to kind of keep
[L613] [20:58.76] hammering away. Maybe first could you
[L614] [21:00.52] define this loop engineering thing and
[L615] [21:03.24] then I'm curious how often do you use it
[L616] [21:05.16] and
[L617] [21:06.08] you know, would you hit limits if you
[L618] [21:08.00] were on a max plan doing that kind of
[L619] [21:09.60] stuff?
[L620] [21:10.72] >> Yeah, so I okay, so loop engineering
[L621] [21:13.96] roughly it's like
[L622] [21:16.48] instead of prompting Claude directly,
[L623] [21:18.64] you're setting up a system that prompts
[L624] [21:20.44] Claude. You know, and
[L625] [21:23.16] you don't have to think of it if you use
[L626] [21:25.40] Claude tag a lot of this comes
[L627] [21:26.84] naturally. You just ask it like, hey,
[L628] [21:29.04] every day do this thing, you know, and
[L629] [21:32.12] that will that's a loop. You can
[L630] [21:35.84] definitely do that sort of work right
[L631] [21:37.16] now, but I think if you're trying to set
[L632] [21:38.84] up like let's let's say like
[L633] [21:40.76] 10 loops or something, you know, that
[L634] [21:42.84] are like uh
[L635] [21:45.24] triaging your feedback and implementing
[L636] [21:48.00] and things like that. We do that sort of
[L637] [21:49.84] work, but we also spend a lot of time
[L638] [21:51.88] making sure our skills and things like
[L639] [21:54.52] that are useful, you know, and like are
[L640] [21:57.24] good at like triaging
[L641] [21:59.52] that we can
[L642] [22:00.96] how we're good at verification and so
[L643] [22:03.36] that we can like make sure that the
[L644] [22:04.48] changes land, you know, and then I think
[L645] [22:07.84] at that level, you know, what it means
[L646] [22:10.28] is like now we have someone monitoring
[L647] [22:12.56] issues that we just could never have
[L648] [22:14.52] kept on top of before, right? And it
[L649] [22:16.96] just like increases our software
[L650] [22:18.20] development velocity and it's worth a
[L651] [22:19.68] lot of value to us. And so yeah, I think
[L652] [22:22.08] that like if you're kind of at the scale
[L653] [22:23.68] of like, okay, you want it to
[L654] [22:25.60] essentially be autonomously running, you
[L655] [22:28.20] know,
[L656] [22:29.36] doing a software engineering job. For
[L657] [22:30.96] certain cases, I think it can do that if
[L658] [22:33.20] you set up the verification well, if you
[L659] [22:35.56] set up your skills well, if you give it
[L660] [22:36.92] the right data sources, but um it is a
[L661] [22:39.28] lot of work, right? And I think that
[L662] [22:40.64] like you have to make sure that that
[L663] [22:42.28] work is valuable to you in the same way
[L664] [22:43.72] that like if you hire someone, you know,
[L665] [22:45.08] you have to make sure that work is
[L666] [22:46.16] valuable.
[L667] [22:47.28] >> We've talked a little bit about
[L668] [22:48.40] Anthropic being kind of
[L669] [22:50.60] just ahead because that's the job of the
[L670] [22:52.48] company on adopting AI. Is there
[L671] [22:55.24] something that you feel is kind of the
[L672] [22:57.04] next big shift that maybe Anthropic's
[L673] [22:59.64] already felt that you feel
[L674] [23:01.88] is going to diffuse into the industry
[L675] [23:04.16] and if so, what might that be?
[L676] [23:06.40] >> Yeah, I think there are few different
[L677] [23:09.12] ones. Obviously, Claude Tag, I think, is
[L678] [23:12.00] our, you know, the way we do a lot of
[L679] [23:13.64] our work right now, right? And I think
[L680] [23:15.28] the way I think about it is that Claude
[L681] [23:17.16] Code is really good at the
[L682] [23:18.72] implementation of code, and Claude Tag
[L683] [23:20.68] is for the rest of the software
[L684] [23:22.56] development life cycle, you know, so
[L685] [23:24.08] like so
[L686] [23:25.72] getting feedback,
[L687] [23:27.48] uh you know, doing code review, like
[L688] [23:30.28] babysitting, building CICD, incidents,
[L689] [23:34.04] like, you know, all of these other
[L690] [23:35.40] things, Claude Tag is really good at.
[L691] [23:37.60] At a high level, turning every part of
[L692] [23:40.28] your software development life cycle
[L693] [23:41.68] into kind of like a a routine or a loop
[L694] [23:45.12] using Claude Tag or something like that,
[L695] [23:47.12] I think is probably where things are
[L696] [23:49.28] headed, you know?
[L697] [23:50.96] Um I think probably generative
[L698] [23:53.64] interfaces are still to come, and I
[L699] [23:55.92] think that like artifacts and, you know,
[L700] [23:59.76] uh yeah, basically artifacts, I think,
[L701] [24:01.72] are going to be like an increasingly
[L702] [24:03.60] large way of how you like interact and
[L703] [24:05.88] read with Claude. And and so I think
[L704] [24:07.56] that, you know, I use artifacts for
[L705] [24:09.04] almost everything, and and so I think
[L706] [24:10.32] that like we're going to see that also
[L707] [24:12.04] become big, and I think that's also ties
[L708] [24:15.12] into Claude Tag, right? So like let's
[L709] [24:16.80] say that you are um on your phone and
[L710] [24:20.00] Claude Tag has done a bunch of work for
[L711] [24:21.28] you. It creates a report. The report is
[L712] [24:23.40] readable, you know, on your phone
[L713] [24:25.16] because it's made the like the artifact
[L714] [24:27.36] look really great.
[L715] [24:28.84] >> Could you explain
[L716] [24:30.40] uh artifacts a little bit or kind of
[L717] [24:31.92] what are they and how do people use
[L718] [24:33.32] them?
[L719] [24:34.28] >> Artifacts are basically
[L720] [24:36.60] um
[L721] [24:37.96] Claude can upload essentially a web app
[L722] [24:40.40] for you to use, you know? And I think
[L723] [24:41.92] that
[L724] [24:42.96] uh
[L725] [24:44.28] you can use it in a really wide range of
[L726] [24:47.88] capabilities. They can now, for example,
[L727] [24:50.20] call your MCP. So you can make an
[L728] [24:52.08] artifact, for example, to read your
[L729] [24:54.52] inbox, you know, and like display it or
[L730] [24:57.20] sort it or tag it, right? As like a one
[L731] [24:59.88] way. You can also use artifact to uh
[L732] [25:02.52] show you a plan for coding, right? And
[L733] [25:04.32] then in that it might show like diagrams
[L734] [25:06.36] and file snippets and code and schemas.
[L735] [25:09.28] Um and so it shows you like sort of uh
[L736] [25:12.12] it's like an interactive
[L737] [25:14.36] display for the tap for the job you're
[L738] [25:16.72] doing right now, you know? And as Claude
[L739] [25:18.52] does more and more, you know, like jobs,
[L740] [25:21.68] we're realizing that like just text in
[L741] [25:24.16] text out is probably not useful for
[L742] [25:26.68] everything, right? And Claude is doing
[L743] [25:29.12] is better and better at creating
[L744] [25:30.64] essentially the exact interface for you
[L745] [25:32.44] at the right time. Um I think that
[L746] [25:35.08] there's like a lot more to do there, and
[L747] [25:37.36] I think
[L748] [25:38.32] it's another one of those things where
[L749] [25:39.48] you have to think about like, oh, like
[L750] [25:41.60] you know, could I be interacting with
[L751] [25:42.84] Claude in a different way, right? Like
[L752] [25:44.44] could I interact with it through an
[L753] [25:45.64] artifact? Could I
[L754] [25:47.68] you know, use it to like learn more or
[L755] [25:49.84] like to understand it better or stay in
[L756] [25:51.28] the loop or
[L757] [25:53.04] um
[L758] [25:54.20] improve some of my like own knowledge
[L759] [25:56.00] work or something. So,
[L760] [25:57.92] um
[L761] [25:58.76] yeah, I I I think it's pretty exciting.
[L762] [25:59.88] We're still kind of early to it.
[L763] [26:01.96] >> Does the daily driver model vary among
[L764] [26:04.84] engineers, or do people typically just
[L765] [26:07.04] pick the most intelligent one that's
[L766] [26:09.28] available at Anthropic?
[L767] [26:11.12] >> I do think, you know, similarly with
[L768] [26:13.20] models, if you use the smart models and
[L769] [26:14.80] you use them well and you give them
[L770] [26:17.04] task where they can, you know, are
[L771] [26:18.76] well-shaped and you've spent some time
[L772] [26:20.16] setting up a good verification harness
[L773] [26:21.76] and things like that, you can get a lot
[L774] [26:23.44] out of them.
[L775] [26:24.60] I don't think it's like choosing which
[L776] [26:26.48] model at the right time, you know? I
[L777] [26:28.72] think it's like, oh, how do you get the
[L778] [26:30.28] most out of the frontier models
[L779] [26:33.84] um because I think technology works the
[L780] [26:36.68] way it does, right? Like everything gets
[L781] [26:37.92] more abundant, more available.
[L782] [26:40.12] Um and so I think we're in this current
[L783] [26:43.52] weird spot where, you know, we don't
[L784] [26:44.92] quite have enough compute for everyone
[L785] [26:47.28] to have Fable at 100% of the rate
[L786] [26:48.80] limits.
[L787] [26:49.88] Um but I don't think this is like a
[L788] [26:51.16] durable skill to build figuring out like
[L789] [26:54.24] oh when do you use Fable and when do you
[L790] [26:55.68] Sonic, right? So
[L791] [26:58.52] I think it's like unintuitive there.
[L792] [27:00.96] But I think in practice if you're today
[L793] [27:03.68] what I would do is like I use Fable for
[L794] [27:05.80] planning, for brainstorming, for finding
[L795] [27:08.36] unknowns, for coming up with the
[L796] [27:09.64] detailed spec and I'd use Opus 5 to
[L797] [27:11.84] implement it.
[L798] [27:13.96] And I would probably use Opus 5 with
[L799] [27:16.12] workflows
[L800] [27:17.60] using like a verification aid like
[L801] [27:19.44] schema or like harness that's built with
[L802] [27:21.28] Fable, right? So I'd use Fable for those
[L803] [27:23.36] high leverage task.
[L804] [27:25.92] And yeah, Opus 5 for the execution and
[L805] [27:29.16] implementation.
[L806] [27:31.32] But yeah, I think increasingly probably
[L807] [27:33.08] next year I I I think you're just not
[L808] [27:34.52] going to be thinking that much about
[L809] [27:36.68] like which model.
[L810] [27:38.48] >> You mentioned that skill of I guess
[L811] [27:40.56] prompting and I've heard some people
[L812] [27:44.56] they say
[L813] [27:46.04] it's not too durable of a skill because
[L814] [27:49.04] it's kind of it's really specific to a
[L815] [27:51.04] model. Like these models they almost
[L816] [27:52.96] have their own unique
[L817] [27:55.60] I guess spiky intelligence. So if you if
[L818] [27:58.04] you knew everything that was very
[L819] [27:59.68] specific to let's say today's Fable and
[L820] [28:02.68] you're a master of today's Fable
[L821] [28:05.00] I mean maybe you don't need to know any
[L822] [28:06.60] of that stuff like a year from now and
[L823] [28:09.60] Fable 3 or 4 or 5 whatever comes out.
[L824] [28:13.08] Let's say you were talking to software
[L825] [28:15.56] engineer who's looking for career advice
[L826] [28:18.00] and they're thinking hey should I really
[L827] [28:20.52] become a master of engineering my
[L828] [28:23.44] prompt?
[L829] [28:24.64] >> I do want to say prompting is like
[L830] [28:26.20] little bit more than just a prompt you
[L831] [28:28.04] put in. It's also you know, you might
[L832] [28:29.84] have done made a skill or you might have
[L833] [28:31.72] like you know, added some data or
[L834] [28:33.12] something. It's not just a prompt you
[L835] [28:34.96] write but it's like everything you've
[L836] [28:36.08] done before that builds up into your
[L837] [28:37.92] context, right? So
[L838] [28:40.28] sometimes people see us write small
[L839] [28:42.08] prompts and they're like oh what is that
[L840] [28:43.80] mean? But we we just spent so much time
[L841] [28:46.04] on
[L842] [28:47.16] the the
[L843] [28:48.44] harness and the verification and and the
[L844] [28:50.24] skills. So,
[L845] [28:51.68] um
[L846] [28:52.36] I think it will be like really valuable
[L847] [28:54.40] to just keep better at prompting. I
[L848] [28:56.60] think to what you're saying about each
[L849] [28:58.48] model is different, you're right. Like I
[L850] [28:59.88] think each model is kind of its owns
[L851] [29:02.68] kind of like almost organic digital
[L852] [29:05.12] thing, you know? And so, there are
[L853] [29:06.76] quirks you have to learn and you do have
[L854] [29:09.48] to unlearn them. So,
[L855] [29:11.56] we recently wrote about like how we
[L856] [29:13.72] removed 80% of the system to prompt from
[L857] [29:15.64] Claude code, right? Um and one of the
[L858] [29:18.56] learnings we had was like we needed to
[L859] [29:20.20] remove examples from the tool
[L860] [29:22.72] descriptions. And you know, this used to
[L861] [29:24.68] be the only way you could get good
[L862] [29:26.40] output from the models was through
[L863] [29:29.00] tools, right? Or or through examples,
[L864] [29:31.16] right? So, you'd have to be like, "Hey,
[L865] [29:32.88] this is the right tool. Use this. Here
[L866] [29:35.24] Here's an example of writing a
[L867] [29:37.88] file well and here's an example of not
[L868] [29:39.56] doing it well."
[L869] [29:40.68] Um
[L870] [29:41.64] and now we found that like examples are
[L871] [29:43.88] mostly negative, I think, unless um
[L872] [29:47.24] you really see Claude doing something
[L873] [29:48.64] you don't like because
[L874] [29:50.32] uh it's just like quite imaginative.
[L875] [29:52.28] It's good at sticking to your intention
[L876] [29:54.00] and working with you. Um and so, we
[L877] [29:55.96] removed a lot of examples. So, in that
[L878] [29:58.32] case, yes, you do have to sort of like
[L879] [30:00.12] adapt, but the skill you're building is
[L880] [30:03.36] the skill to adapt. You learned how to
[L881] [30:05.96] use Fable and now you know a lot about
[L882] [30:08.28] Fable, but you also know how to learn
[L883] [30:10.44] You learned how to work with a model,
[L884] [30:12.68] right? And so, Fable 5.5 comes out, you
[L885] [30:14.92] need to
[L886] [30:15.96] learn how to use it again as well,
[L887] [30:19.24] but you'll be much faster cuz you're
[L888] [30:21.04] better at learning.
[L889] [30:22.52] You're better working with Fable 5, you
[L890] [30:24.36] know? And I think for me, I think the
[L891] [30:26.32] first model I worked with was GPT-2, and
[L892] [30:29.04] I remember like it was it was so hard to
[L893] [30:31.04] get
[L894] [30:32.20] a JSON output out of GPT-2. Like if you
[L895] [30:35.08] could just
[L896] [30:36.08] get it to like choose one of the
[L897] [30:38.36] categories that you gave it, that would
[L898] [30:40.04] be like incredible, you know? And so,
[L899] [30:42.60] um I think that but like
[L900] [30:45.08] building that skill, GPT-2 is such a
[L901] [30:47.56] different model than Fable 5, but I feel
[L902] [30:50.12] like the skill I spent doing that has
[L903] [30:52.92] like helped me be better at prompting
[L904] [30:54.92] Fable 5.
[L905] [30:56.12] >> Is there any like tribal knowledge or
[L906] [30:57.84] quirky tips in today's models where
[L907] [31:00.20] you'd say
[L908] [31:01.40] someone should should know that to get
[L909] [31:03.44] more when they prompt?
[L910] [31:04.80] >> I actually need to counter one I think
[L911] [31:06.52] that people have been saying where it's
[L912] [31:07.84] like, "Oh, just believe in yourself." or
[L913] [31:09.84] something. I I know that
[L914] [31:11.72] Jared
[L915] [31:13.16] Jared's post about the Riemann
[L916] [31:14.40] hypothesis had like he was just like,
[L917] [31:16.32] "Keep going. Just believe in yourself."
[L918] [31:18.48] I think in this case it was mostly just
[L919] [31:20.76] Jared saying it's okay to use compute to
[L920] [31:23.72] solve this problem and I'm giving you
[L921] [31:25.40] permission to do it, you know? And I
[L922] [31:27.76] think that like that's not exactly the
[L923] [31:29.60] same as
[L924] [31:31.04] you know, I believe in you, you know
[L925] [31:34.08] what I mean? It's really just like
[L926] [31:35.84] letting the model use compute. So, I
[L927] [31:38.36] think that that is something I would
[L928] [31:41.04] I like to tell the models right now is
[L929] [31:42.92] like, "Okay, hey, I think this is a hard
[L930] [31:44.56] problem. Use sub agents, you know? Use
[L931] [31:47.00] workflows. Like if you need it, right?
[L932] [31:49.00] So, like I always tell it to like use
[L933] [31:51.00] its own judgment, but I'm giving you
[L934] [31:55.84] permission to do this stuff, right? And
[L935] [31:58.60] I think that
[L936] [31:59.92] uh
[L937] [32:00.72] you have to sort of remember that the
[L938] [32:01.96] models by default, you know, do what
[L939] [32:04.48] maybe the average user wants, which is
[L940] [32:06.08] like they want it to respond and start
[L941] [32:08.36] doing work as fast as possible.
[L942] [32:11.44] Roughly like complete the task, but not
[L943] [32:13.84] spend like a crazy amount of compute on
[L944] [32:15.68] it, you know? And so, I think that like
[L945] [32:18.56] um you have to sort of if you want the
[L946] [32:20.76] model to do it differently, you have to
[L947] [32:22.04] nudge it slightly, right? So, you might
[L948] [32:23.80] have to be like, "Okay, hey, like I
[L949] [32:25.84] don't want you to do any work yet. I
[L950] [32:27.36] want you to brainstorm, you know? I want
[L951] [32:29.20] you to like think with me, right?" Um
[L952] [32:32.12] and if you prompt it that way, it will
[L953] [32:33.40] start doing that. If you want it to
[L954] [32:35.32] spend a lot of compute, if you're like,
[L955] [32:36.72] hey,
[L956] [32:37.52] you know, sometimes I'll say like
[L957] [32:39.72] Yeah, hey, I think this is a hard
[L958] [32:40.64] problem. Uh feel free to use workflows.
[L959] [32:43.16] If I'm running overnight, I might just
[L960] [32:44.56] be like, hey, I'm going to sleep, you
[L961] [32:46.04] know, set the slash goal or something
[L962] [32:47.44] and then
[L963] [32:48.52] uh let it let it run. So,
[L964] [32:51.00] um
[L965] [32:51.76] yeah, I think there is a
[L966] [32:54.36] uh just like giving it permission to do
[L967] [32:56.28] the thing you want.
[L968] [32:57.88] >> When you recently removed so much of the
[L969] [33:00.32] system prompt,
[L970] [33:01.88] uh how did you prove that
[L971] [33:04.32] the end result was better?
[L972] [33:06.44] >> We have a bunch of user metrics just
[L973] [33:08.32] like how, you know, how much do people
[L974] [33:10.40] like the output of Claude? Do you
[L975] [33:12.12] something you get that survey and you
[L976] [33:13.52] see it. Um
[L977] [33:15.24] we run evals against, you know, our
[L978] [33:18.76] internal eval uh and external evals to
[L979] [33:21.64] see like how it performs at these
[L980] [33:23.52] different tasks. Um
[L981] [33:25.44] but I think it is hard like sometimes
[L982] [33:27.44] you don't realize that they're not If
[L983] [33:29.88] Claude is telling the user if it does
[L984] [33:32.16] all its work and then it's like, hey,
[L985] [33:33.80] maybe you should go to sleep, there's no
[L986] [33:35.48] eval for Claude tells you to go to
[L987] [33:36.92] sleep, you know what I mean? And now
[L988] [33:38.04] we're like have to like catch this like
[L989] [33:40.00] new behavior. Um so, it is hard. I think
[L990] [33:42.80] we spent a lot of time
[L991] [33:44.64] basically just um
[L992] [33:46.44] you know, like removing lines in the
[L993] [33:47.68] system prompt, running evals, uh seeing
[L994] [33:50.04] how it works, seeing how people uh
[L995] [33:52.08] reported it internally, and then like
[L996] [33:54.36] adjusting, but it was like a full-time
[L997] [33:56.12] job for several people over long periods
[L998] [33:58.36] of time. And so,
[L999] [34:00.12] I don't think I'd necessarily recommend
[L1000] [34:01.96] everyone do this. I think that's kind of
[L1001] [34:04.36] why we wrote that post about what we
[L1002] [34:06.28] learned from like adjusting the system
[L1003] [34:08.48] prompt. And we think that's pretty
[L1004] [34:10.32] general. So, hopefully you don't have to
[L1005] [34:12.44] like now
[L1006] [34:13.68] go through this like crazy iteration
[L1007] [34:15.32] process.
[L1008] [34:16.72] >> OpenAI, Anthropic, Cursor, and Vercel
[L1009] [34:20.48] all use this product to make their lives
[L1010] [34:22.24] better.
[L1011] [34:23.20] And the problem it solves is when you're
[L1012] [34:25.08] building SaaS or an ad product and you
[L1013] [34:27.72] want to sell to other companies, there's
[L1014] [34:29.60] all these requirements you need to meet.
[L1015] [34:31.80] There's SSL, there's SCIM, there's RBAC,
[L1016] [34:35.44] there's audit logs. These are all things
[L1017] [34:37.24] that take time to integrate, but aren't
[L1018] [34:39.40] the main focus of your app. WorkOS is an
[L1019] [34:41.72] API layer that lets you meet all of
[L1020] [34:43.40] these requirements in just a few lines
[L1021] [34:45.56] of code. So, let's say you have a new
[L1022] [34:47.60] SaaS product and you want to sell to
[L1023] [34:49.28] other companies, WorkOS will solve all
[L1024] [34:51.76] of these critical feature gaps for you.
[L1025] [34:54.48] You can check them out at workos.com to
[L1026] [34:56.96] learn more and get started. And I
[L1027] [34:59.12] appreciate them for supporting my work
[L1028] [35:00.96] and sponsoring this podcast.
[L1029] [35:02.84] >> I think a lot of people
[L1030] [35:05.40] when they use Claude code, they get
[L1031] [35:07.40] excellent results when it's kind of
[L1032] [35:09.88] getting
[L1033] [35:11.44] very objective work done.
[L1034] [35:13.76] But when it's kind of prompting models
[L1035] [35:15.96] to do beautiful or tasteful work, it's
[L1036] [35:18.72] kind of not always, you know, it's
[L1037] [35:20.32] pretty much more hit and miss. And so,
[L1038] [35:23.00] you know, how do you best instill like a
[L1039] [35:25.44] very particular style you're going for
[L1040] [35:27.72] or particular taste in the models
[L1041] [35:30.24] outputs when it's a much more subjective
[L1042] [35:32.88] domain, maybe like front end?
[L1043] [35:35.08] >> The way you do it is sort of like you
[L1044] [35:37.28] stay in the loop. I think you give it
[L1045] [35:39.32] references, right? And I think the more
[L1046] [35:41.16] references you give it with data, the
[L1047] [35:44.36] better. So, like it's better to give an
[L1048] [35:46.80] HTML file than a screenshot, right? It's
[L1049] [35:48.64] better to give a Figma file than like a
[L1050] [35:51.72] raster image or something, right? Cuz
[L1051] [35:53.60] now it if Claude wants to know the
[L1052] [35:55.68] border radius of this thing, it's like,
[L1053] [35:57.20] oh, what's the Figma component border
[L1054] [35:59.80] radius and let me just copy it over. And
[L1055] [36:02.64] so, I think giving it a bunch of
[L1056] [36:04.20] references, ideally in code, is a really
[L1057] [36:07.16] good way, right? Of like getting it to
[L1058] [36:09.28] stick to this. Um
[L1059] [36:11.04] I think if not, you can then ask it to
[L1060] [36:14.40] if you don't have like
[L1061] [36:16.24] uh let's say you're not a designer.
[L1062] [36:18.16] There's probably Step one is being like,
[L1063] [36:20.68] okay, now I'm not a designer. There's a
[L1064] [36:22.48] lot I don't know about design, you know?
[L1065] [36:25.64] And like there's was lot I don't know
[L1066] [36:26.84] about iteration. I don't even know what
[L1067] [36:29.04] good looks like, right? And I think this
[L1068] [36:30.64] is like part of the art of working with
[L1069] [36:33.36] a designer is like they will just know
[L1070] [36:35.20] what good looks like and they'll be like
[L1071] [36:36.60] this isn't good enough in this way,
[L1072] [36:38.32] right? And they like prompt it. And that
[L1073] [36:40.68] I think is also a skill that will keep
[L1074] [36:42.28] getting valuable and even more valuable
[L1075] [36:45.00] over time is just like what is good
[L1076] [36:47.28] output? What is worth doing, right? Like
[L1077] [36:49.00] I think uh for example with the uh the
[L1078] [36:51.64] Riemann hypothesis, Jared prompted it,
[L1079] [36:54.00] but he had no idea if it was correct
[L1080] [36:56.24] until like Lev who's like, you know,
[L1081] [36:59.16] one of the world's best mathematicians
[L1082] [37:01.32] who was like, you know, okay, like how
[L1083] [37:02.68] do I
[L1084] [37:04.16] is this correct, right? And he worked
[L1085] [37:06.64] with it and he asked it like tons of
[L1086] [37:08.56] follow-up questions.
[L1087] [37:10.36] And we could not follow that at all. We
[L1088] [37:12.28] had no idea what he was saying, right?
[L1089] [37:14.28] But he was like really intrigued. And
[L1090] [37:16.00] and so I think
[L1091] [37:17.12] more and more being that like high-cased
[L1092] [37:19.12] user and like knowing a lot about a
[L1093] [37:21.36] problem in a domain space is how you get
[L1094] [37:23.44] good outputs, right? That's how you
[L1095] [37:25.68] these problems. Uh
[L1096] [37:27.24] otherwise like maybe Claude did solve
[L1097] [37:29.32] like physics or something and but you
[L1098] [37:30.72] just wouldn't know it, right? Like
[L1099] [37:31.76] you're like
[L1100] [37:32.72] uh
[L1101] [37:33.44] you you don't know enough about it. And
[L1102] [37:35.16] so I think when you're talking about
[L1103] [37:37.16] design, the first thing you do is like
[L1104] [37:38.68] how do you become more tasteful with
[L1105] [37:40.20] design, right? And so you can ask Claude
[L1106] [37:42.96] that as well, right? Like you can be
[L1107] [37:44.28] like, "Hey, I'm not a designer. I want
[L1108] [37:46.08] to be better at design. I don't even
[L1109] [37:47.68] have the language. First maybe let's
[L1110] [37:49.52] find some reference sites." And that and
[L1111] [37:51.08] then maybe you pull some reference sites
[L1112] [37:52.64] and then you're like, "This is what I
[L1113] [37:53.88] like or this is what I don't like,
[L1114] [37:55.32] right?" And then you
[L1115] [37:57.16] sort of build up that, you know, those
[L1116] [37:59.44] references and you give Claude it. And
[L1117] [38:01.44] and now maybe you tell it, "Hey, let's
[L1118] [38:03.04] do some exploration. This is sort of my
[L1119] [38:05.04] taste." And then it'll do like a few
[L1120] [38:07.36] different mock-ups, right? And I like to
[L1121] [38:09.36] do these mock-ups all in HTML because
[L1122] [38:10.96] it's all self-contained, easy to edit.
[L1123] [38:13.28] And then once you have that
[L1124] [38:15.48] you know, that reference, now it's a
[L1125] [38:17.56] reference. So now you can be like you
[L1126] [38:19.36] can make a new session and be like,
[L1127] [38:20.64] "Hey, this is a mock-up of a design I
[L1128] [38:22.88] want. Uh start implementing this and,
[L1129] [38:25.76] you know, it will have all of it in code
[L1130] [38:27.68] and you can start getting there." Um but
[L1131] [38:30.12] I think that like the really hard part
[L1132] [38:32.48] is just knowing like, "Oh, when is
[L1133] [38:34.16] something good enough?" You know, uh
[L1134] [38:35.72] versus like when can you, you know, push
[L1135] [38:38.64] harder, right? And you see this with a
[L1136] [38:40.12] lot of the math proofs, too, right? Or
[L1137] [38:41.72] and when like Terence Tao is like,
[L1138] [38:43.48] "Okay, enough with the half-complete
[L1139] [38:45.56] theorems. Just do the full theorem." You
[L1140] [38:47.84] know, and and so I think like it sounds
[L1141] [38:50.28] simple, but it takes a lot of domain
[L1142] [38:52.32] knowledge and expertise to get to the
[L1143] [38:54.60] point to be like, "Okay, like you it
[L1144] [38:56.88] seems like you're smart enough to have
[L1145] [38:58.40] done that. Now do this."
[L1146] [39:00.60] >> When I was a software engineer,
[L1147] [39:03.04] there was a lot of um
[L1148] [39:05.28] I guess it was like glue writing work
[L1149] [39:07.40] kind of where you you finish some work
[L1150] [39:09.84] and you write a launch post or
[L1151] [39:12.44] you are part of some work stream and you
[L1152] [39:14.92] got to post an update every 2 to 4 weeks
[L1153] [39:18.44] or maybe you have a direction doc or
[L1154] [39:21.48] design doc and all this like writing
[L1155] [39:24.44] around the software uh that you actually
[L1156] [39:27.36] write.
[L1157] [39:28.48] And curious your thoughts on if that's
[L1158] [39:31.44] changed at all at Anthropic, how much of
[L1159] [39:34.68] that is written by LLMs and how much of
[L1160] [39:37.24] that is, you know, human-written still.
[L1161] [39:40.28] >> Mhm. My rule of thumb is like if I would
[L1162] [39:42.56] be happy to show someone the prompt, I
[L1163] [39:45.68] would send them the output, right? And
[L1164] [39:47.28] so uh a lot of times the prompt is just
[L1165] [39:51.04] collecting context is the most common
[L1166] [39:52.92] one, right? So, for example, uh before
[L1167] [39:55.88] every one-on-one with my manager, I ask
[L1168] [39:57.88] Claude to, you know, read every Slack
[L1169] [40:00.72] message and GitHub message and, you
[L1170] [40:02.92] know, a
[L1171] [40:03.68] PR and compile like, you know, a report
[L1172] [40:07.48] of what I did, right? And uh that's
[L1173] [40:10.16] context that my manager doesn't have
[L1174] [40:11.72] because, you know, they haven't been
[L1175] [40:13.56] literally reading every PR or something.
[L1176] [40:15.84] And so I don't feel bad if like, you
[L1177] [40:17.92] know,
[L1178] [40:18.80] like my manager could also run this
[L1179] [40:21.08] command, but it doesn't have my context.
[L1180] [40:23.12] And I don't feel bad with them knowing
[L1181] [40:24.88] that this is the prompt I used to
[L1182] [40:26.76] generate this command, right? So,
[L1183] [40:29.24] um I think likewise, like if you're
[L1184] [40:31.16] sharing updates or something like that,
[L1185] [40:33.48] you know, like uh you might want to
[L1186] [40:36.12] prove that you've read it. You know, I
[L1187] [40:38.32] think this is important. And And
[L1188] [40:39.80] sometimes like little edits are ways of
[L1189] [40:42.08] proving that you have also understood
[L1190] [40:44.04] this work, right? And so, if it's just
[L1191] [40:46.12] like a data readout, you know, maybe
[L1192] [40:48.12] you're you're sanity checking like the
[L1193] [40:51.04] numbers make sense and this like these
[L1194] [40:53.00] are all the numbers you intended to
[L1195] [40:54.20] include. And as part of that, maybe you
[L1196] [40:56.20] format it differently or you add like a
[L1197] [40:58.12] little sentence in on your behalf,
[L1198] [41:00.08] right? And but I think ultimately, it's
[L1199] [41:02.12] a data readout.
[L1200] [41:03.68] Everyone knows the prompt you wrote is
[L1201] [41:05.48] like, "Hey, like generate a readout on
[L1202] [41:07.80] this feature based on this." And And
[L1203] [41:09.68] you're fine, right? But like, I think if
[L1204] [41:11.60] you're pitching like a new concept or
[L1205] [41:13.36] new idea and your prompt is like, "Help
[L1206] [41:15.24] me come up with a new concept for, you
[L1207] [41:17.52] know, this product, right?" Like, you
[L1208] [41:19.72] probably at least
[L1209] [41:22.20] people want you to know that want to
[L1210] [41:23.92] know that you've like believed in it,
[L1211] [41:25.60] right? And so, like even if you think
[L1212] [41:27.36] Claude's idea is incredible and just
[L1213] [41:29.56] verbatim you wouldn't change anything,
[L1214] [41:31.08] what I would say is like, I'd be like,
[L1215] [41:32.32] "Hey, Claude generated this. Um but I
[L1216] [41:34.84] think it's great. You know, like I or
[L1217] [41:37.00] I've did like a hundred different
[L1218] [41:38.32] generations and I think this was really
[L1219] [41:39.84] good. And here is like something, you
[L1220] [41:42.24] know, that I want to send you, right?"
[L1221] [41:44.75] >> [snorts]
[L1222] [41:44.88] >> Um and so, I think that like it's good
[L1223] [41:47.76] to be upfront about it, I think, right?
[L1224] [41:49.84] Because I do think what people don't
[L1225] [41:51.76] like is when they feel like they've been
[L1226] [41:53.24] like misled a little bit. Like, "Oh,
[L1227] [41:54.80] like you We thought we you were doing
[L1228] [41:57.52] this work, but, you know,
[L1229] [42:00.00] um it it's really Claude, right?" And I
[L1230] [42:02.08] think that like um
[L1231] [42:04.60] writing sometimes can have a lot of like
[L1232] [42:06.88] there's some parts of writing where
[L1233] [42:08.80] individual words matter. You know, like
[L1234] [42:11.00] funnily like tweets are I of a good
[L1235] [42:12.36] example of this where like the
[L1236] [42:13.80] individual tweet matters, right? So,
[L1237] [42:16.16] um
[L1238] [42:17.08] you like more and more you can't use
[L1239] [42:19.20] Claude to do that because it's like like
[L1240] [42:21.96] every word has some thought that you've
[L1241] [42:23.92] put into it and some intention that
[L1242] [42:25.36] you've put into it. So, like, you know,
[L1243] [42:27.00] yeah, a pitch or an essay or something
[L1244] [42:29.20] like that. We do a lot of like internal
[L1245] [42:30.76] essays at Anthropic being like, "Hey,
[L1246] [42:32.36] this is why I think we should do this."
[L1247] [42:34.08] And that's generally like all
[L1248] [42:35.60] human-written. It's very like looked
[L1249] [42:38.84] down upon, I think, to have like Claude
[L1250] [42:41.28] like your essay written by Claude, you
[L1251] [42:42.72] know what I mean? Um because like every
[L1252] [42:44.84] word is something that you like are
[L1253] [42:47.00] intentional about.
[L1254] [42:48.92] >> So, it sounds like the proportion
[L1255] [42:51.16] of the writing that's all that boring
[L1256] [42:54.24] route writing, like the data readouts,
[L1257] [42:56.44] the
[L1258] [42:57.48] the one-on-one updates, the work stream
[L1259] [42:59.24] updates, that's increasingly becoming
[L1260] [43:01.88] AI, but always reviewed by human. And
[L1261] [43:04.72] then the novel thoughts, novel
[L1262] [43:07.32] direction, is still very human-written.
[L1263] [43:10.28] And And feels like it should remain that
[L1264] [43:12.64] way even if the models were a little bit
[L1265] [43:15.12] better, too.
[L1266] [43:16.60] >> Yeah, I think it's like if you're, you
[L1267] [43:18.84] know, it's a like writing is also way of
[L1268] [43:21.24] thinking, right? And so like maybe if
[L1269] [43:22.68] you need to think about the data stream
[L1270] [43:24.64] or data readout more, then maybe you
[L1271] [43:26.24] need to like summarize it, you know? And
[L1272] [43:27.96] And so,
[L1273] [43:29.04] um but yeah, I I I think like especially
[L1274] [43:30.64] gathering context is one of those things
[L1275] [43:32.44] where no one will ever like hold it
[L1276] [43:34.44] against you, kind of, right? Like uh
[L1277] [43:36.96] oh, like, you know, you did a bunch of
[L1278] [43:39.00] research and, you know, Claude did this,
[L1279] [43:41.16] but yeah, like I don't want to ask my
[L1280] [43:42.76] agent to do the same research. Like, you
[L1281] [43:44.52] know, it's a shortcut, but like just
[L1282] [43:46.52] acknowledging it is good.
[L1283] [43:48.76] >> Someone I also was talking to, they had
[L1284] [43:51.08] this thought of it would be valuable to
[L1285] [43:54.92] have almost like a git blame, but it's
[L1286] [43:57.68] like like a prompt blame of
[L1287] [44:00.56] cuz it would be nice to reverse look up
[L1288] [44:03.28] what was the prompt that generated this
[L1289] [44:05.00] change to kind of debug things. Do you
[L1290] [44:07.44] have any sort of meta version control on
[L1291] [44:11.08] the prompts that generated the software
[L1292] [44:12.96] or is it still very vanilla, you know,
[L1293] [44:15.80] get history?
[L1294] [44:17.68] >> Yeah, that is a little bit tough because
[L1295] [44:19.72] again like, you know, what goes into a
[L1296] [44:21.52] prompt is not just the prompt but also
[L1297] [44:24.08] the context and skills and things like
[L1298] [44:25.76] that. So like maybe, you know, a prompt
[L1299] [44:28.00] might seem basic but isn't. Uh I think
[L1300] [44:31.76] I it's kind of hard to judge. But I do,
[L1301] [44:34.48] you know, like going back to like when
[L1302] [44:36.56] I'm giving a PR, I don't think a PR at
[L1303] [44:38.60] this point is any different than an
[L1304] [44:40.24] artifact or something. Like Claude is
[L1305] [44:41.92] doing basically all the code writing,
[L1306] [44:44.16] right? So if I send someone a PR, I
[L1307] [44:46.08] usually also attach an artifact of every
[L1308] [44:49.92] prompt I sent to Claude,
[L1309] [44:52.00] um including failed like approaches and
[L1310] [44:54.68] things like that, you know?
[L1311] [44:56.28] Um so that they can see like, okay, I've
[L1312] [44:58.56] considered a lot of other things, you
[L1313] [45:00.84] know? And if I haven't, if this is just
[L1314] [45:02.48] a one-shot, I just tell people. I'm
[L1315] [45:04.28] like, "Hey, this is the one-shot
[L1316] [45:06.08] example. This is the prompt I used,
[L1317] [45:07.80] right?" Um
[L1318] [45:09.40] and uh I think that's like usually
[L1319] [45:12.40] impressive and interesting to them as
[L1320] [45:13.84] well because they're like, "Oh, like
[L1321] [45:14.96] it's cool that Claude could one-shot
[L1322] [45:16.36] this." Um but the worst is when you get
[L1323] [45:20.20] like
[L1324] [45:21.24] you know, you you just I'm just trying
[L1325] [45:22.44] to avoid cases where I send in like this
[L1326] [45:24.36] 10,000 line PR and they're like, "Did
[L1327] [45:27.48] you like how much have you like read
[L1328] [45:29.68] this or like, you know, like how much
[L1329] [45:30.96] did you work with Claude on it?" And if
[L1330] [45:33.04] I'm doing like a large PR, I am going to
[L1331] [45:35.08] like show my work as much as possible.
[L1332] [45:39.00] >> On maintaining code because AI can
[L1333] [45:42.08] generate such high volumes of code at
[L1334] [45:45.00] this point, do you have any tips on
[L1335] [45:47.64] what's worked well at Anthropic for code
[L1336] [45:49.84] ownership and maintenance?
[L1337] [45:52.20] >> I do think you have to revisit
[L1338] [45:54.28] like what is important with code
[L1339] [45:56.28] maintenance, right? And so I think that
[L1340] [45:57.84] like there are some things where like
[L1341] [45:59.76] naming used to be really important,
[L1342] [46:02.04] right? Because like it was like how you
[L1343] [46:04.04] as a team thought about this like
[L1344] [46:05.68] abstraction and feature. Um but I think
[L1345] [46:08.48] naming is becoming less and less
[L1346] [46:09.96] important. A lot of stylistic things in
[L1347] [46:12.12] code are becoming less and less
[L1348] [46:13.48] important, you know? And I think that
[L1349] [46:15.56] like this is not the same to me as
[L1350] [46:18.32] maintenance, right? So I think that like
[L1351] [46:21.04] um
[L1352] [46:22.36] if you you might want to sit down and be
[L1353] [46:24.32] like, okay, like what things really
[L1354] [46:26.16] matter now, what don't, what opinions do
[L1355] [46:28.08] we have that don't matter. So that's
[L1356] [46:30.28] one. And then I think on the second on
[L1357] [46:32.12] the maintenance side is sort of like
[L1358] [46:34.04] having good scaffolding, right? So I
[L1359] [46:37.32] think that it's like uh having a good
[L1360] [46:39.72] verification harness, having a good like
[L1361] [46:43.20] uh sort of skills. We use the simplify
[L1362] [46:45.48] skill a lot. I think that like you know,
[L1363] [46:47.92] sometimes even from model perspective,
[L1364] [46:49.96] like it might do a lot of work. And then
[L1365] [46:51.76] like even just giving it permission to
[L1366] [46:53.12] be like, "Hey, I think this is the right
[L1367] [46:55.52] uh idea. Let's simplify it." gives it
[L1368] [46:58.68] that permission to do it, right? But
[L1369] [47:00.00] like you actually don't want a model to
[L1370] [47:02.32] by default do work and then simplify,
[L1371] [47:05.92] right? Because uh maybe it's not
[L1372] [47:07.84] correct, right? Like you don't want it
[L1373] [47:09.28] to simplify work that's not correct.
[L1374] [47:10.76] It's like um you're wasting tokens,
[L1375] [47:13.24] right? And so I think this is also how
[L1376] [47:15.04] humans think, right? They're like you
[L1377] [47:17.28] know, you think generatively, you try an
[L1378] [47:19.08] approach, and then maybe you like
[L1379] [47:20.44] simplify and abstract a little. Um so I
[L1380] [47:23.56] think there's like some work inside your
[L1381] [47:25.68] own code base or like setting up the
[L1382] [47:27.64] skills and that those practices where
[L1383] [47:29.80] you like you know, you're not just
[L1384] [47:31.24] submitting
[L1385] [47:32.84] like the first take, but you've like
[L1386] [47:34.20] simplified it and tried it. Um and then
[L1387] [47:37.36] like yeah, having a really good
[L1388] [47:38.44] verification harness where you feel like
[L1389] [47:40.80] you're catching you know, like you have
[L1390] [47:43.40] a good
[L1391] [47:44.60] belief that Claude is like testing every
[L1392] [47:46.84] part of it.
[L1393] [47:48.20] Uh like you know, when you submit a PR
[L1394] [47:50.00] to Claude code, you get a recording back
[L1395] [47:52.20] of it using the feature and testing it
[L1396] [47:54.00] as an example, right? Um and you can
[L1397] [47:57.04] just get really, really creative with
[L1398] [47:58.88] different ways to like
[L1399] [48:00.80] uh, test stuff. Like I think you should
[L1400] [48:02.32] basically have
[L1401] [48:03.72] on the order of I'd say more like a
[L1402] [48:05.52] hundred times more testing code than
[L1403] [48:07.92] you've ever had before. You know what I
[L1404] [48:09.36] mean? So like,
[L1405] [48:10.88] uh,
[L1406] [48:11.48] you should have
[L1407] [48:12.72] uh, fixtures for everything. You can
[L1408] [48:14.04] just pull production code and create
[L1409] [48:15.60] fixtures and mock-ups on the fly for for
[L1410] [48:17.72] databases. You can uh, have storybooks
[L1411] [48:20.52] for front-end and things like that. And
[L1412] [48:22.40] you can have all these different ways of
[L1413] [48:24.08] testing and verifying your code. And
[L1414] [48:25.92] that I think is really valuable for
[L1415] [48:27.36] maintainability, right? It's like um,
[L1416] [48:30.76] just having like all these ways of
[L1417] [48:32.52] verifying it.
[L1418] [48:33.84] Uh, and then uh, yeah, of course like
[L1419] [48:36.32] there's just like the human element of
[L1420] [48:37.76] like where do you want your code base to
[L1421] [48:40.40] go? If you know that's the case,
[L1422] [48:43.36] probably you start thinking about like,
[L1423] [48:45.16] you know, how you'd replay and undo and
[L1424] [48:47.04] redo becomes really important, right?
[L1425] [48:48.60] Like just like that sort of stuff. And
[L1426] [48:51.04] so the but if you're single player only,
[L1427] [48:53.60] that actually matters a little bit less.
[L1428] [48:56.12] You know, like you like the average user
[L1429] [48:58.48] is not going to undo a hundred times or
[L1430] [49:00.80] something, right? And so like, you know,
[L1431] [49:03.00] many like single player applications
[L1432] [49:05.40] undo stop working
[L1433] [49:07.32] pretty quickly. Like, you know, like
[L1434] [49:08.52] after like four or five times, right?
[L1435] [49:10.28] Um, just cuz it's not that important.
[L1436] [49:11.64] But in multiplayer, the ability to
[L1437] [49:13.32] compose different things together is
[L1438] [49:15.00] really important or compose different
[L1439] [49:16.56] operations together is really important.
[L1440] [49:17.80] And so, um,
[L1441] [49:19.44] that's just an example where like if you
[L1442] [49:21.04] know the direction of your code base,
[L1443] [49:22.28] there are things you care about and you
[L1444] [49:23.36] want the models to know. And uh, you
[L1445] [49:25.56] know, you can include that in your
[L1446] [49:26.44] skills. You can also just like
[L1447] [49:28.60] you know, like that's sort of what
[L1448] [49:29.92] maintainability means to me is like
[L1449] [49:31.76] having a vision for what your code base
[L1450] [49:33.12] is good at, where you're where you're
[L1451] [49:34.40] going, you know, keeping it in line.
[L1452] [49:37.52] Um, I do think the models are getting
[L1453] [49:38.88] better and better and better. And like
[L1454] [49:41.32] almost every code base probably I think
[L1455] [49:43.92] will have this moment where you're like,
[L1456] [49:45.24] do you just ask the model to rewrite all
[L1457] [49:47.60] of it? You know?
[L1458] [49:49.48] Um, and like because now you're like,
[L1459] [49:52.80] oh, like I can do it in the most
[L1460] [49:54.28] performant language. I can mix and match
[L1461] [49:57.32] like you know like there's not a reason
[L1462] [49:58.72] that every software in the world
[L1463] [50:00.56] shouldn't run in web assembly in the
[L1464] [50:02.16] browser. You know what I mean? There's
[L1465] [50:03.56] not a reason why
[L1466] [50:05.36] I don't know like your Xbox game can't
[L1467] [50:08.64] run in your browser actually, right?
[L1468] [50:09.96] Like the Xbox like the hardware like the
[L1469] [50:12.64] consoles are much weaker than your
[L1470] [50:14.68] average like MacBook right now. You know
[L1471] [50:16.84] what I mean? But it's just like the code
[L1472] [50:18.64] base, right? [snorts] Um but we could
[L1473] [50:21.64] like and and so I I think probably over
[L1474] [50:23.92] the next year or two like everyone's
[L1475] [50:25.76] going to need to think about that,
[L1476] [50:27.20] right?
[L1477] [50:28.32] And so I I don't think you want to spend
[L1478] [50:30.44] too much time
[L1479] [50:32.20] like worrying about maintainability in
[L1480] [50:34.20] this like way that might not matter
[L1481] [50:35.52] anymore. I'm not saying maintainability
[L1482] [50:37.00] doesn't matter. You just have to update
[L1483] [50:38.20] your mental model of like what does it
[L1484] [50:39.44] mean for like code to be maintainable,
[L1485] [50:42.20] you know?
[L1486] [50:43.92] >> I was talking to this friend um
[L1487] [50:46.48] who was saying that
[L1488] [50:48.20] he leaves tons and tons of tech debt
[L1489] [50:51.80] leaving around because the next you know
[L1490] [50:54.36] the next iteration why why waste time
[L1491] [50:56.44] fixing that now when the next iteration
[L1492] [50:58.56] of Fable's going to one shot all this
[L1493] [51:00.72] tech debt and refactor this for me. So
[L1494] [51:04.12] kind of funny.
[L1495] [51:05.40] >> Yeah, I I don't think that's completely
[L1496] [51:07.32] incorrect. It depends on the
[L1497] [51:09.28] circumstance, right? Like I think this
[L1498] [51:10.64] is also just a classic thing in
[L1499] [51:12.52] startups, right? Where you're like, you
[L1500] [51:14.52] know, even in normal human engineer you
[L1501] [51:16.48] always have this problem of like um
[L1502] [51:18.84] hey, do I refactor or do I do tech debt
[L1503] [51:21.36] or do I deliver more customer value?
[L1504] [51:23.44] Would refactoring help me deliver more
[L1505] [51:25.12] customer value right now? I do think
[L1506] [51:27.36] that like just generally I think you
[L1507] [51:29.28] should think on your projects on shorter
[L1508] [51:31.88] time scales. So you're like okay, how do
[L1509] [51:33.96] I deliver value over the next month or
[L1510] [51:35.96] two? And if you the project you're
[L1511] [51:37.88] talking about is delivering value over
[L1512] [51:39.80] six months or 12 months, you know, then
[L1513] [51:42.92] maybe yeah, maybe like wait for the next
[L1514] [51:44.88] model a little bit, you know, and then
[L1515] [51:46.44] like that like
[L1516] [51:48.64] just deliver value on like the short
[L1517] [51:50.36] time scale scale, make sure it's like,
[L1518] [51:52.56] you know, really good. And if the models
[L1519] [51:54.00] are not quite good
[L1520] [51:55.40] enough, like they might get there soon.
[L1521] [51:57.56] It depends very much on the like
[L1522] [51:58.96] specific case, right? But and I'm not
[L1523] [52:01.28] saying this is true of everything, but
[L1524] [52:02.60] like just something you should keep in
[L1525] [52:04.08] mind.
[L1526] [52:04.96] >> I've talked to some friends who work at
[L1527] [52:06.68] big tech companies like Google,
[L1528] [52:09.12] Facebook, those types of places.
[L1529] [52:11.16] And then they as they've become more and
[L1530] [52:14.28] more AI pilled, one thing that people
[L1531] [52:17.40] have noticed is there's a lot more
[L1532] [52:19.08] incidents or SEVs in in their usage.
[L1533] [52:22.64] And
[L1534] [52:23.68] it's natural in those organizations cuz
[L1535] [52:25.88] they they read the code less and there's
[L1536] [52:27.96] more code flying out. You know, what
[L1537] [52:30.04] countermeasures have worked really well
[L1538] [52:32.04] for Anthropic to prevent breakages given
[L1539] [52:36.04] that the code velocity is so much
[L1540] [52:37.40] higher?
[L1541] [52:38.36] >> Yeah, I I think this is something that
[L1542] [52:40.20] like is a byproduct of moving faster
[L1543] [52:43.40] sometimes and we have to figure it out.
[L1544] [52:45.00] Like I think that
[L1545] [52:46.96] uh you know,
[L1546] [52:48.20] I don't think our uptime is exactly
[L1547] [52:49.76] where we want it to be either, but also
[L1548] [52:52.24] as a company we're a little like almost
[L1549] [52:54.64] 6 years old I think around, right? So
[L1550] [52:56.32] it's like no company has grown this fast
[L1551] [52:58.96] before and a lot of that is because we
[L1552] [53:00.96] were enabled to like create more
[L1553] [53:02.08] products faster than ever before, right?
[L1554] [53:04.36] And so you can use Claude to make your
[L1555] [53:06.84] uptime better, right? And I think that
[L1556] [53:08.48] like the way we think about this is just
[L1557] [53:09.84] like really good what's the dream
[L1558] [53:12.40] testing environment, the dream like you
[L1559] [53:14.96] know, deployment environment. Like can
[L1560] [53:16.92] you like you know, take requests and
[L1561] [53:19.48] replay them across like, you know, mock
[L1562] [53:21.72] databases and fixtures across
[L1563] [53:23.28] everything? Can you chaos monkey
[L1564] [53:24.80] everything, you know?
[L1565] [53:26.96] >> In my personal workflows, I have so many
[L1566] [53:30.28] more custom random tools and scripts
[L1567] [53:33.60] that just make everything faster.
[L1568] [53:35.92] And just curious, you know, on your team
[L1569] [53:39.24] at Anthropic for instance, does everyone
[L1570] [53:41.92] have a set of
[L1571] [53:43.80] miscellaneous tools that help them,
[L1572] [53:46.64] you know, get random things done?
[L1573] [53:48.92] >> Yeah, everyone does for sure. Like I I
[L1574] [53:51.12] think
[L1575] [53:51.92] part of this is is the job. Like I think
[L1576] [53:54.00] that sometimes uh
[L1577] [53:56.08] what we try and do is we play around
[L1578] [53:57.48] with harnesses. Like sometimes some
[L1579] [53:58.96] people on the team build their own
[L1580] [54:00.00] harnesses for a little bit to figure out
[L1581] [54:02.48] like, "Oh, is this like useful or not?"
[L1582] [54:05.28] You know, and then they they figure out
[L1583] [54:06.56] if it works and if not, they like
[L1584] [54:08.00] integrate it, right? So, I think there's
[L1585] [54:09.68] like that's part of the job uh in some
[L1586] [54:12.12] ways. Um
[L1587] [54:13.80] I think like other examples of like sort
[L1588] [54:16.12] of like misc stuff people will do. A lot
[L1589] [54:18.84] of people will have like
[L1590] [54:20.16] uh unique Claude tag setups. I think
[L1591] [54:22.88] Claude tag is one of these things where
[L1592] [54:24.48] like, you know, you can have it like I
[L1593] [54:27.36] have it scheduled my calendar invites,
[L1594] [54:29.08] right? And so like if someone
[L1595] [54:30.72] wants to like schedule something with
[L1596] [54:32.00] me, then I'm just like, "Hey, you can
[L1597] [54:33.08] just like tag Claude here in this
[L1598] [54:34.44] channel and I'll accept whatever it like
[L1599] [54:36.96] puts on my calendar, you know what I
[L1600] [54:38.28] mean?" So, um I think there's like some
[L1601] [54:40.88] stuff like that. I know like a lot of
[L1602] [54:42.76] people use it for like email. I I think
[L1603] [54:45.00] that um
[L1604] [54:46.96] I've seen like some people do like
[L1605] [54:49.84] interesting like multi-Clauding sort of
[L1606] [54:51.84] like
[L1607] [54:52.84] tmuxing like setups, right? Like where
[L1608] [54:55.48] like what's the ideal scenario for you
[L1609] [54:57.48] to like display like 50 different Claude
[L1610] [55:00.00] codes and, you know, what's the best way
[L1611] [55:02.12] to for you to figure out what's going on
[L1612] [55:04.00] at any one time? So, um
[L1613] [55:06.84] yeah, I think there's a lot of different
[L1614] [55:08.80] ways and we're trying to make Claude
[L1615] [55:10.00] code more hackable as well so that like,
[L1616] [55:12.20] you know, more people can
[L1617] [55:14.32] uh sort of like even
[L1618] [55:16.60] uh make their own version of Claude code
[L1619] [55:18.76] like more different and everyone might
[L1620] [55:20.68] have their own little twist on it.
[L1621] [55:24.40] >> Your role at Anthropic's really
[L1622] [55:25.68] interesting cuz of the external
[L1623] [55:27.76] visibility that you have and um I think
[L1624] [55:30.96] a lot of people when they give career
[L1625] [55:32.84] advice,
[L1626] [55:34.20] visibility's a a good thing,
[L1627] [55:36.84] but they don't have this level of
[L1628] [55:38.32] external visibility. And so, do you
[L1629] [55:40.36] recommend to software engineers like
[L1630] [55:42.76] they should be posting on Twitter and X
[L1631] [55:45.04] and, you know, if so, what what advice
[L1632] [55:47.52] would you give in that sense?
[L1633] [55:49.24] >> Generally,
[L1634] [55:50.92] the thing I say to people that you
[L1635] [55:52.40] should share your work
[L1636] [55:54.56] externally as much as you can,
[L1637] [55:55.68] especially
[L1638] [55:56.88] um I think within certain companies like
[L1639] [55:59.84] you might not be able to, but like maybe
[L1640] [56:01.60] you have side projects or something like
[L1641] [56:03.16] that. I think just um before I joined
[L1642] [56:05.80] Anthropic, what I did was like I spent a
[L1643] [56:07.84] bunch of time working with different
[L1644] [56:09.64] companies, building stuff, and writing
[L1645] [56:11.52] about it, and talking about it. Um and
[L1646] [56:14.60] uh like this was really valuable cuz it
[L1647] [56:17.92] like increased my surface area of luck,
[L1648] [56:20.28] you know? And so, I think that like uh
[L1649] [56:24.88] it's really
[L1650] [56:26.56] like the bar is much lower than you
[L1651] [56:28.52] think. Like basically, whenever someone
[L1652] [56:29.96] asked me for advice, I'm like, "Okay,
[L1653] [56:31.88] I I'll I'll sit them down. I'll be like,
[L1654] [56:33.16] "I know statistically I I tell this
[L1655] [56:35.68] advice to a lot of people, and almost no
[L1656] [56:37.68] one does it. Um and everyone who's done
[L1657] [56:40.12] it is like either in a job that they're
[L1658] [56:42.24] pretty excited about or running their
[L1659] [56:43.60] own company.
[L1660] [56:45.04] Um
[L1661] [56:45.64] and there are reasons why you're not
[L1662] [56:46.76] going to want to do it, but like this is
[L1663] [56:48.32] it. Like I'm just going to tell you.
[L1664] [56:49.84] One, like I don't care about your
[L1665] [56:50.80] resume. Like like, you know, don't do
[L1666] [56:52.80] that. Um you have to choose like an
[L1667] [56:54.96] interesting project to work on. You have
[L1668] [56:56.72] to work really hard on it. You have to
[L1669] [56:58.24] like lock in, and then you have to ship
[L1670] [57:01.16] it and write about it. Like you have to
[L1671] [57:02.52] do it. You can't like There's going to
[L1672] [57:04.88] be so many reasons why you don't want
[L1673] [57:06.12] to. It's like not good enough yet, or
[L1674] [57:07.60] like you haven't like you think the
[L1675] [57:09.52] write-up is not very interesting or
[L1676] [57:10.96] something, but you have to do it, and
[L1677] [57:14.24] you can't get discouraged, you know?
[L1678] [57:15.84] Like maybe the first one might not work,
[L1679] [57:17.16] but you have to do it again. Um
[L1680] [57:19.60] and maybe Twitter is not the right
[L1681] [57:20.88] place. Maybe it's Reddit. Uh maybe
[L1682] [57:22.80] there's a specific Reddit or Hacker News
[L1683] [57:24.76] or something like that. Part of what
[L1684] [57:26.24] you're trying to do is you're just
[L1685] [57:27.00] trying to find people who like like what
[L1686] [57:28.88] you're doing, right? But I think that
[L1687] [57:30.76] like people in general want to really
[L1688] [57:35.00] like you know we since consume more
[L1689] [57:37.84] content than ever right and you know
[L1690] [57:39.68] this right like I think that like people
[L1691] [57:42.24] want really high quality content high
[L1692] [57:44.40] quality content as you know is a lot of
[L1693] [57:46.20] work and so I think going back to like
[L1694] [57:48.72] what we said before about like would you
[L1695] [57:50.92] show someone the prompt you did right
[L1696] [57:52.64] like I think a lot of times people are
[L1697] [57:54.40] like oh what's the shortcut like oh like
[L1698] [57:56.48] should I just ask Claude to manage my
[L1699] [57:58.28] Twitter account and is that how I like
[L1700] [58:00.04] grow and and I'm like no like like you
[L1701] [58:02.16] should not do that right like you have
[L1702] [58:03.48] to sort of engage authentically
[L1703] [58:06.16] you have to like post like you know do
[L1704] [58:08.36] good work and talk about it and I think
[L1705] [58:10.16] like build up networks and things like
[L1706] [58:12.40] that but I think that as long as that's
[L1707] [58:14.64] one of your goals and you try hard at it
[L1708] [58:16.96] I've been seeing anyone not succeed at
[L1709] [58:19.44] it but it is really hard it's kind of
[L1710] [58:21.40] like saying like oh I want to like go to
[L1711] [58:23.68] the gym every day or I want to like lose
[L1712] [58:25.68] weight or something you know like there
[L1713] [58:27.04] are simple things that you can do that
[L1714] [58:29.44] take a lot of discipline and are easy to
[L1715] [58:31.36] get discouraged with and
[L1716] [58:33.56] um
[L1717] [58:34.40] but like worth doing if you do it and I
[L1718] [58:36.12] think like posting or more specific more
[L1719] [58:38.60] specifically like writing about your
[L1720] [58:40.28] work is like I think really really
[L1721] [58:41.52] valuable.
[L1722] [58:42.52] >> You mentioned luck surface area. Do you
[L1723] [58:44.84] have an example that kind of illustrates
[L1724] [58:47.68] the value of expanding your luck surface
[L1725] [58:50.40] area?
[L1726] [58:52.20] >> Yeah I mean okay how did I get my job at
[L1727] [58:54.76] Anthropic? I did
[L1728] [58:57.56] a fellowship with a company called Good
[L1729] [58:59.68] Fire where I did like some applied
[L1730] [59:01.72] research and so they they're an
[L1731] [59:03.20] interpretability AI company and I was
[L1732] [59:05.72] trying to figure out like how do I use
[L1733] [59:06.92] interpretability to in like to make
[L1734] [59:08.68] better products and so I learned about
[L1735] [59:10.84] their research
[L1736] [59:12.56] and I uh like felt like I want to work
[L1737] [59:17.12] on a project and it was really important
[L1738] [59:19.44] for me to like share it and so like I
[L1739] [59:21.76] when I agreed to work with them I was
[L1740] [59:23.56] like that's my goal is I want to like
[L1741] [59:25.76] share what I'm building I think that's
[L1742] [59:27.72] good for you as well because good fire
[L1743] [59:29.36] is a startup and you know, people I want
[L1744] [59:31.56] they want people to learn about them.
[L1745] [59:33.56] And so this is what something I'm going
[L1746] [59:34.60] to do. So I built this like
[L1747] [59:35.92] interpretability visualization and I
[L1748] [59:38.16] shared about it. This is my first like
[L1749] [59:39.52] big post on Twitter but it was only 500
[L1750] [59:41.40] likes or something. Like at like now
[L1751] [59:43.52] like you know, that's like not very much
[L1752] [59:45.56] to me but like it's like back then it
[L1753] [59:46.84] was like a huge post and um several
[L1754] [59:49.72] people saw it and like some of them DM'd
[L1755] [59:51.52] me about it and then uh like I then got
[L1756] [59:56.68] an intro into
[L1757] [59:59.00] you know, like uh into a role here and
[L1758] [01:00:01.68] so
[L1759] [01:00:02.60] um
[L1760] [01:00:03.32] I think that like I spent like a month
[L1761] [01:00:05.60] on that project I think in particular.
[L1762] [01:00:07.64] So it wasn't like you know, crazy um
[L1763] [01:00:11.72] and uh yeah, it just like showed people
[L1764] [01:00:15.00] that I could like do interesting work
[L1765] [01:00:17.76] and um
[L1766] [01:00:19.08] and I got paid for it too. So it wasn't
[L1767] [01:00:20.24] like I was doing it for free.
[L1768] [01:00:21.96] Um
[L1769] [01:00:23.24] And and there's plenty of examples of
[L1770] [01:00:24.72] like I think people are happy to do that
[L1771] [01:00:26.80] sort of thing for you. You know, like if
[L1772] [01:00:28.08] you like sort of show that kind of
[L1773] [01:00:30.32] initiative. Um but yeah, you have to
[L1774] [01:00:34.28] like it it it is like you really have to
[L1775] [01:00:36.88] like do interesting and novel work and
[L1776] [01:00:38.44] work work hard and be proud of your work
[L1777] [01:00:40.36] as well. You know, there's not like a
[L1778] [01:00:42.32] shortcut to that I think but
[L1779] [01:00:44.76] um if you do I think everyone is always
[L1780] [01:00:47.12] looking for interesting work and wants
[L1781] [01:00:48.68] to support you and you know, wants to
[L1782] [01:00:50.76] hire you or um
[L1783] [01:00:53.00] yeah, give you money like
[L1784] [01:00:55.48] uh lots of good things.
[L1785] [01:00:57.80] >> I see this tagline going out a lot with
[L1786] [01:01:00.88] some of the stuff Anthropic's been um
[L1787] [01:01:03.64] maybe like I think it's like Boris went
[L1788] [01:01:05.48] on some podcast and the tagline was
[L1789] [01:01:08.20] coding is largely solved. You should
[L1790] [01:01:10.80] people still learn to code if coding is
[L1791] [01:01:13.40] largely solved.
[L1792] [01:01:14.88] >> I think being technical is really really
[L1793] [01:01:16.68] important. Knowing how do computers
[L1794] [01:01:19.12] work, how does like um
[L1795] [01:01:22.04] yeah, how does how do computer programs
[L1796] [01:01:23.60] work? How do languages work? Like what
[L1797] [01:01:25.12] are the hard things and like what's a
[L1798] [01:01:27.12] back-end service? Like what's a cache?
[L1799] [01:01:28.80] Like what's what like like, you know,
[L1800] [01:01:30.28] what like what is memory allocation?
[L1801] [01:01:32.72] Like all of these things are actually
[L1802] [01:01:33.76] kind of really important to learn.
[L1803] [01:01:35.68] Um, I do think it's hard to motivate
[L1804] [01:01:39.08] yourself sometimes to do in the same way
[L1805] [01:01:41.04] that like, you know, doing math by hand
[L1806] [01:01:44.00] was not that motivating to me, you know,
[L1807] [01:01:46.08] but some people just love math and did
[L1808] [01:01:47.64] it. Um, I I think that like that's
[L1809] [01:01:50.80] probably
[L1810] [01:01:52.80] like something that people have to
[L1811] [01:01:53.96] figure out, but I think it is really
[L1812] [01:01:55.28] worth it. Like being technical is really
[L1813] [01:01:57.36] really important. Like we talked about
[L1814] [01:01:59.16] at the start of or like earlier where
[L1815] [01:02:01.44] like, "Oh, the only way you can tell you
[L1816] [01:02:02.84] solved you know, the Riemann hypothesis
[L1817] [01:02:05.84] or like made progress or whatever is
[L1818] [01:02:07.52] like or the Jacobian conjecture is like
[L1819] [01:02:10.20] if you're a great mathematician, right?"
[L1820] [01:02:12.28] And in the same way the only way you can
[L1821] [01:02:14.20] tell if you're like built great software
[L1822] [01:02:16.28] is like if you're a great software
[L1823] [01:02:17.40] engineer. Um,
[L1824] [01:02:19.68] I think that like how do you do that
[L1825] [01:02:22.76] hard, but like we've talked about some
[L1826] [01:02:24.32] of this stuff before just like staying
[L1827] [01:02:25.56] in the loop like, you know, like put
[L1828] [01:02:27.52] like, uh,
[L1829] [01:02:29.20] like putting like reflecting on your
[L1830] [01:02:31.04] process and and getting better and and
[L1831] [01:02:33.00] you can use Claude to learn as well and
[L1832] [01:02:35.08] and sort of explain things to you. So
[L1833] [01:02:36.96] like treating it like a thought partner.
[L1834] [01:02:39.44] Um, but learning like truly I I think
[L1835] [01:02:41.88] like, you know, Kaparthy says like
[L1836] [01:02:43.32] learning should feel like effort, you
[L1837] [01:02:45.00] know, and I think that's like one of the
[L1838] [01:02:46.76] hard things is like a lot of times even
[L1839] [01:02:48.84] if you ask Claude to explain something
[L1840] [01:02:50.16] to you and you might just like nod along
[L1841] [01:02:51.48] and you're like, "Oh, yeah, like I
[L1842] [01:02:52.40] learned it." But you didn't really cuz
[L1843] [01:02:53.72] you didn't put any effort in, right? So
[L1844] [01:02:55.56] I think that like it is really
[L1845] [01:02:57.16] technical. You should learn. It's hard
[L1846] [01:03:00.44] to learn. And and sometimes like what
[L1847] [01:03:02.32] school forces you to do is to learn
[L1848] [01:03:04.00] that. Um, I don't know truly like I'm
[L1849] [01:03:06.96] not learning programming from scratch.
[L1850] [01:03:08.88] So I don't know exactly what how to do
[L1851] [01:03:11.16] it now. I think if short of better ways,
[L1852] [01:03:14.72] I would still like type out and build
[L1853] [01:03:17.40] programs and run them and learn them.
[L1854] [01:03:19.36] You know what I mean?
[L1855] [01:03:20.64] Um there might be better ways that are
[L1856] [01:03:21.80] more cloud informed as well, but I think
[L1857] [01:03:24.00] it's really important.
[L1858] [01:03:25.80] Um
[L1859] [01:03:26.72] I think when Boris says coding is
[L1860] [01:03:28.12] solved, I think it just means like
[L1861] [01:03:30.92] um you know, we don't get stuck in the
[L1862] [01:03:33.28] same ways that we used to before. Like I
[L1863] [01:03:34.88] think coding used to be this very high
[L1864] [01:03:36.44] variability thing where you're like, oh
[L1865] [01:03:38.68] like could this bug take a day or could
[L1866] [01:03:41.40] it take 2 weeks? You have no idea
[L1867] [01:03:43.40] sometimes, you know? And I think like um
[L1868] [01:03:46.20] on the whole coding used to be like in
[L1869] [01:03:49.04] real terms
[L1870] [01:03:50.60] like something that was very rare for
[L1871] [01:03:53.64] something to go well. Do you know what I
[L1872] [01:03:55.48] mean? Like very few people in the entire
[L1873] [01:03:57.84] world could write software and they were
[L1874] [01:04:00.00] very very rare and even if you got them
[L1875] [01:04:02.32] all together, there were so many other
[L1876] [01:04:03.88] reasons why it wouldn't work, right? And
[L1877] [01:04:06.48] coding was this like one of the rarest
[L1878] [01:04:08.64] things in the world where like the
[L1879] [01:04:09.68] chance of software
[L1880] [01:04:11.08] project going well was like
[L1881] [01:04:13.88] on absolute terms very low, you know?
[L1882] [01:04:16.60] Uh and if you were like hiring someone
[L1883] [01:04:18.84] to
[L1884] [01:04:19.84] like make software for you for something
[L1885] [01:04:22.36] that's not like a huge product. Like if
[L1886] [01:04:25.20] you're hiring someone to make software
[L1887] [01:04:26.84] for your car dealership, you were almost
[L1888] [01:04:28.80] certainly not going to get the software
[L1889] [01:04:30.52] you wanted. You're going to get like
[L1890] [01:04:32.16] essentially scammed, you know what I
[L1891] [01:04:33.68] mean? Um not because anyone was trying
[L1892] [01:04:36.04] to scam you. It was just like software
[L1893] [01:04:37.24] was really really hard and you know, it
[L1894] [01:04:39.36] could only be spent on like the most
[L1895] [01:04:41.40] important scalable things in the world.
[L1896] [01:04:43.72] And now that coding is solved, I think
[L1897] [01:04:46.08] what we mean is that like you can use
[L1898] [01:04:47.40] coding to do all these other things that
[L1899] [01:04:50.12] we not done before, but that's not to
[L1900] [01:04:52.96] say that like that's not a lot of work
[L1901] [01:04:54.72] still. Um
[L1902] [01:04:56.64] it's just like it's not this like
[L1903] [01:04:57.88] incredibly rare difficult thing that
[L1904] [01:05:00.28] mostly like just doesn't work and you
[L1905] [01:05:02.72] have to spend like 8 hours a day locked
[L1906] [01:05:05.00] in to do.
[L1907] [01:05:07.16] >> What's really insane, that shows the
[L1908] [01:05:08.96] difference in expectation, is when I
[L1909] [01:05:11.52] used to write software, I would be
[L1910] [01:05:14.20] shocked if it worked on the first try. I
[L1911] [01:05:16.44] was like, "Whoa.
[L1912] [01:05:17.64] >> Wait, why is this working?"
[L1913] [01:05:18.91] >> [laughter]
[L1914] [01:05:19.40] >> And you you'd expect to kind of bash
[L1915] [01:05:21.64] your head against the wall a little bit,
[L1916] [01:05:23.08] and then it it works. Even if it's just
[L1917] [01:05:24.80] like you missed the semicolon or
[L1918] [01:05:26.88] something like that. And now I almost
[L1919] [01:05:29.00] have the flip expectation where it when
[L1920] [01:05:31.28] it doesn't work, I'm like, "Wait, what
[L1921] [01:05:32.60] what why did Claude What what happened
[L1922] [01:05:35.04] here?"
[L1923] [01:05:35.92] Usually, I expect it to work almost uh
[L1924] [01:05:39.36] the opposite
[L1925] [01:05:40.08] >> like on the first try. It's crazy.
[L1926] [01:05:42.20] >> Immediately. Yeah, yeah, I think humans
[L1927] [01:05:43.64] get really used to abundance, right?
[L1928] [01:05:45.28] Like there was this like
[L1929] [01:05:46.92] um article someone shared recently about
[L1930] [01:05:48.80] like going through a modern apartment
[L1931] [01:05:50.80] and talking about all the like wonderful
[L1932] [01:05:52.40] things that we have now that people
[L1933] [01:05:54.32] could not have imagined before. Like
[L1934] [01:05:56.16] something that can play music on demand
[L1935] [01:05:58.20] that's suited for your mood. You know,
[L1936] [01:06:00.44] like before you'd have to like hire a
[L1937] [01:06:02.84] musician, you know, to like go write
[L1938] [01:06:06.36] like, you know, incredible music, right?
[L1939] [01:06:09.12] Um but I'd say on the whole, probably
[L1940] [01:06:11.40] more people are getting paid to make
[L1941] [01:06:13.08] music now than ever before, right? Like
[L1942] [01:06:15.88] um and I think that like music is
[L1943] [01:06:17.68] reaching more people than ever before.
[L1944] [01:06:19.72] And I think probably the same thing will
[L1945] [01:06:21.36] happen with software, will happen with
[L1946] [01:06:23.00] math, will happen with all of these
[L1947] [01:06:24.68] things. Um
[L1948] [01:06:26.76] where you know, when you get abundance,
[L1949] [01:06:28.64] people are like, "Great. Like I want
[L1950] [01:06:29.84] more abundance. I want my software in
[L1951] [01:06:31.72] everything, you know? Like I want my
[L1952] [01:06:33.08] music everywhere, you know?" So, yeah.
[L1953] [01:06:36.00] >> Yeah, one potential other data point for
[L1954] [01:06:38.24] this conversation saying that maybe
[L1955] [01:06:40.40] people should still be technical or
[L1956] [01:06:43.00] learn how to code is I think earlier in
[L1957] [01:06:45.12] the conversation we talked about
[L1958] [01:06:47.04] automating knowledge work, and you
[L1959] [01:06:48.76] mentioned that
[L1960] [01:06:50.48] people who are technical had kind of a
[L1961] [01:06:52.16] leg up cuz they could kind of understood
[L1962] [01:06:54.60] how to coordinate Claude to do a variety
[L1963] [01:06:57.44] thing. Like you're calling FFmpeg to
[L1964] [01:07:00.00] automate some video editing, and like I
[L1965] [01:07:02.76] don't think someone who is not technical
[L1966] [01:07:04.48] would have that thought. So, it does
[L1967] [01:07:07.08] seem like even in this case where models
[L1968] [01:07:09.00] are doing a lot, there's still so much
[L1969] [01:07:11.32] value in being technical.
[L1970] [01:07:13.80] >> Knowing how computers work. You know, in
[L1971] [01:07:15.88] the same way that like like probably
[L1972] [01:07:18.68] like the most technical CEOs are like
[L1973] [01:07:20.92] the best CEOs are technical, right? Like
[L1974] [01:07:22.56] Zuckerberg, Elon, right? But like they
[L1975] [01:07:24.64] probably haven't written like a line of
[L1976] [01:07:26.04] code truly in a long time, but you know,
[L1977] [01:07:29.00] they understand how systems work, they
[L1978] [01:07:30.80] understand you know, constraints and
[L1979] [01:07:32.84] things like that and then that's really
[L1980] [01:07:34.20] really important. And so,
[L1981] [01:07:36.24] um you know, even if all that work is
[L1982] [01:07:38.64] changed, I think like being technical is
[L1983] [01:07:40.28] really really important.
[L1984] [01:07:42.28] >> And then last question for you is if you
[L1985] [01:07:44.40] could go back to when you just entered
[L1986] [01:07:46.32] the industry and give yourself some
[L1987] [01:07:47.72] advice knowing what you know now, what
[L1988] [01:07:49.80] would you say?
[L1989] [01:07:52.28] >> There are like kind of like two wolves
[L1990] [01:07:54.92] sort of I I think like you have to
[L1991] [01:07:57.16] believe in yourself, you know, I think
[L1992] [01:07:58.88] like this is really important and I
[L1993] [01:08:00.36] think that like at least when I joined
[L1994] [01:08:03.08] in the industry, it was rarer to believe
[L1995] [01:08:05.36] in people when they were
[L1996] [01:08:07.72] kind of the younger. Like I think that
[L1997] [01:08:09.00] was like the whole point of Y Combinator
[L1998] [01:08:10.88] or something was like believing in young
[L1999] [01:08:12.44] people early on to do really great
[L2000] [01:08:14.80] things. And so, I think that like you
[L2001] [01:08:16.68] know, even going back to like the intern
[L2002] [01:08:18.68] discussion we had earlier, right? Like I
[L2003] [01:08:20.32] think that like
[L2004] [01:08:22.40] thinking of yourself not as like someone
[L2005] [01:08:23.84] who's like being trained to do
[L2006] [01:08:25.16] something, but someone who can do like
[L2007] [01:08:26.48] something incredible right away, I think
[L2008] [01:08:28.08] is really important, you know? And um
[L2009] [01:08:31.20] I think I wish I had done
[L2010] [01:08:33.92] bigger, bolder things that I'd written
[L2011] [01:08:37.12] and and shared about. I think there were
[L2012] [01:08:38.92] lots of ideas where I was like, "Wow,
[L2013] [01:08:40.56] like I think
[L2014] [01:08:41.92] I think I had like I thought I had done
[L2015] [01:08:44.72] original work that I wish
[L2016] [01:08:47.12] maybe I'd even shared in some form, but
[L2017] [01:08:48.72] maybe not like form that it like
[L2018] [01:08:50.40] survived the internet, you know? And it
[L2019] [01:08:52.84] wasn't like a like goal of mine. And so,
[L2020] [01:08:55.56] I wish I'd like sort of been bolder and
[L2021] [01:08:57.80] like you know,
[L2022] [01:08:59.80] done and shared some of this work, but
[L2023] [01:09:02.28] at the same time you also there is a lot
[L2024] [01:09:04.12] to learn from people, you know what I
[L2025] [01:09:05.76] mean? And like I think that um
[L2026] [01:09:08.92] you like I think when you're young,
[L2027] [01:09:10.68] you're like, you know, you tend to fold
[L2028] [01:09:13.00] fall either you're not bold enough or
[L2029] [01:09:14.68] you're
[L2030] [01:09:15.56] you're not like
[L2031] [01:09:17.36] uh
[L2032] [01:09:18.96] you don't like learn enough, you know,
[L2033] [01:09:20.68] or you're like you're not like you don't
[L2034] [01:09:22.64] like you're too bold and you don't like
[L2035] [01:09:25.12] figure out what people have done before
[L2036] [01:09:26.40] and figure out why it's not working,
[L2037] [01:09:28.00] right? Um and there's this balance and I
[L2038] [01:09:31.00] think uh you everyone has different
[L2039] [01:09:33.40] failure modes, but I think like uh I
[L2040] [01:09:35.68] think I probably didn't take it enough
[L2041] [01:09:37.16] advantage of like, you know, mentors and
[L2042] [01:09:39.92] people who had learned a lot. Um and I
[L2043] [01:09:41.96] think I probably had to like relearn a
[L2044] [01:09:43.72] bunch of things as a result. Um
[L2045] [01:09:46.48] So, there's probably not universal good
[L2046] [01:09:48.56] advice, but just things to think about
[L2047] [01:09:50.76] as you're, you know, as you're entering.
[L2048] [01:09:53.12] >> Awesome. Well, thanks so much for your
[L2049] [01:09:54.52] time, Derek. Really appreciate it.
[L2050] [01:09:56.28] >> Yeah, of course. Thanks, fine. It's fun.
[L2051] [01:09:58.76] >> Hey, thank you for watching this
[L2052] [01:09:59.80] podcast. If you liked it and you want to
[L2053] [01:10:01.44] see the show grow, please support with a
[L2054] [01:10:03.64] comment or a like.
[L2055] [01:10:05.64] Also, if you have any recommendations
[L2056] [01:10:07.48] for people you want me to bring on,
[L2057] [01:10:09.48] please drop a comment. Guests like
[L2058] [01:10:11.64] Barbara Liskov, Mike Stonebraker, Mark
[L2059] [01:10:14.36] Brooker, these were all people that I
[L2060] [01:10:16.40] brought on because someone left a
[L2061] [01:10:18.24] comment. On another note, aside from the
[L2062] [01:10:20.52] podcast, I'm working on building the
[L2063] [01:10:22.32] ergonomic keyboard that I wish existed.
[L2064] [01:10:24.76] Here's a glance at the prototype. It's a
[L2065] [01:10:26.64] split keyboard, so there's two sides. Um
[L2066] [01:10:29.68] this is in the case. But yeah, we
[L2067] [01:10:31.12] launched on Kickstarter and we hit our
[L2068] [01:10:32.92] goal within 8 hours of launching. I
[L2069] [01:10:35.00] really appreciate it if you were one of
[L2070] [01:10:36.40] the people who grabbed one of the early
[L2071] [01:10:38.16] units. Um we're now working on the long
[L2072] [01:10:40.52] journey of building the tooling now, and
[L2073] [01:10:42.64] so if you still want to pick one up,
[L2074] [01:10:44.32] I've left the late pledges open on
[L2075] [01:10:46.32] Kickstarter, so you can grab one there.
[L2076] [01:10:48.56] I'll put a link in the description.
[L2077] [01:10:50.52] Thank you again for watching the podcast
[L2078] [01:10:52.84] and I'll see you in the next episode.
