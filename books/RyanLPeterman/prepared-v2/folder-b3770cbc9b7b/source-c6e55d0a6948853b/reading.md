# Meta Principal Eng (IC8) On His Senior Staff Promo Story

Source ID: source-c6e55d0a6948853b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Meta_Principal_Eng_(IC8)_On_His_Senior_Staff_Promo_Story_en.txt
Video: https://www.youtube.com/watch?v=ii060zK5gLY

[L10] [00:00.52] Can you talk about the story behind your
[L11] [00:03.00] IC7 or senior staff promo?
[L12] [00:05.68] >> So I got roped into this project to
[L13] [00:07.72] count the number of people using one of
[L14] [00:09.32] Facebook's property. I'm not going to
[L15] [00:10.72] spend a lot of time talking about it,
[L16] [00:11.84] but in the process of doing that, that
[L17] [00:13.44] was around 2015 or so, we had to do a
[L18] [00:16.64] bunch of data processing, we had to do a
[L19] [00:18.60] bunch of machine learning uh and
[L20] [00:21.36] inference. And the tools we had were
[L21] [00:23.52] just icky. They didn't really work well.
[L22] [00:26.12] Like the developer experience was
[L23] [00:28.08] horrible. Uh we would have to like, you
[L24] [00:30.44] know, work within like one data
[L25] [00:31.84] pipelining framework and then move to
[L26] [00:33.56] like another thing to do the machine
[L27] [00:35.04] learning and the inference and then go
[L28] [00:36.44] back and forth.
[L29] [00:38.32] And I was like, this is this is not fun.
[L30] [00:40.24] I'm like wasting so much time just going
[L31] [00:41.96] back and forth. Uh so I started building
[L32] [00:44.20] this little library that essentially let
[L33] [00:46.72] you do data pipelining within the
[L34] [00:48.88] machine learning orchestration
[L35] [00:50.32] framework. And at first that was just
[L36] [00:52.24] like me writing a bunch of helper
[L37] [00:53.44] scripts for myself cuz I didn't want to
[L38] [00:55.40] have to go back and forth. I didn't want
[L39] [00:56.92] to have like deal with landing code in
[L40] [00:58.88] two different code bases and like
[L41] [01:00.20] synchronizing all of that. I was like, I
[L42] [01:01.52] want my code to live in one thing and do
[L43] [01:03.16] all of my thing in this code base and
[L44] [01:05.60] then I'll be happy. But in the process
[L45] [01:07.44] of doing that, I just started tinkering
[L46] [01:10.00] a little. And I was like, why is it
[L47] [01:13.48] whenever I need to write a data
[L48] [01:14.80] pipeline, I have to like write the same
[L49] [01:17.20] boilerplate over and over again? It's
[L50] [01:19.40] always the same thing. Why can't I set
[L51] [01:21.72] those things to be the defaults? And so,
[L52] [01:23.92] you know, I kind of like whittled away a
[L53] [01:26.48] lot of the boilerplate that you had to
[L54] [01:28.04] write. And so, I put together this
[L55] [01:29.92] library where if you were building a
[L56] [01:32.12] data pipeline in the machine learning
[L57] [01:34.40] orchestration framework, if you're in
[L58] [01:35.88] Airflow, what would take you say 300
[L59] [01:39.00] lines of code in like the canonical data
[L60] [01:41.08] pipelining system, would probably take
[L61] [01:43.28] you 20 lines of code.
[L62] [01:45.28] had this escape hatch to like add all of
[L63] [01:46.92] the all of the configuration, but by
[L64] [01:49.20] default it did the right thing. And at
[L65] [01:51.36] that point, I was hooked. I was like, I
[L66] [01:53.36] am building a thing that can make
[L67] [01:54.56] people's lives easier. Forget about this
[L68] [01:56.84] like counting number of people on
[L69] [01:58.04] Facebook. Other people are going to
[L70] [01:59.68] figure that out. I want to help those
[L71] [02:01.20] people move faster. And so then I
[L72] [02:02.92] started looking at like other things
[L73] [02:04.72] where people were wasting time. And at
[L74] [02:06.72] the time, if you were a data scientist,
[L75] [02:10.36] like as a product analyst,
[L76] [02:12.44] if you were a machine learning engineer,
[L77] [02:15.12] the way you worked was by building or
[L78] [02:17.44] setting up your own tools. Half of the
[L79] [02:19.32] company was using Jupiter for notebooks.
[L80] [02:22.36] The other half of the company was using
[L81] [02:23.76] RStudio, which uses this like
[L82] [02:26.20] statistical programming language R. And
[L83] [02:28.28] the way you would set that up is you you
[L84] [02:30.48] would look at one of like 10 different
[L85] [02:32.52] wikis that were all outdated, and you
[L86] [02:34.80] would have to like set that up either on
[L87] [02:36.24] a dev server or on your machine, a lot
[L88] [02:38.52] of manual steps. And I was like, that's
[L89] [02:40.48] kind of silly.
[L90] [02:42.40] We should just make it so everyone has a
[L91] [02:44.80] Jupiter instance running if they want,
[L92] [02:47.16] and they don't have to configure it. And
[L93] [02:48.84] so I just just kind of like started
[L94] [02:50.28] building that. I remember telling my
[L95] [02:51.72] manager, you know, it was probably
[L96] [02:53.92] February, and I was like, "Hey, this is
[L97] [02:55.60] the beginning of the half. I'm going to
[L98] [02:56.88] take two, three months just hack on
[L99] [02:58.36] this.
[L100] [02:59.56] And if it doesn't pan out come, you
[L101] [03:01.68] know,
[L102] [03:02.48] April,
[L103] [03:03.84] I'll just find another project to like
[L104] [03:05.20] save the half and like, you know, not
[L105] [03:06.88] get sent to meet those." And so I
[L106] [03:08.20] started hacking on this, roped in a
[L107] [03:10.00] couple more people,
[L108] [03:12.04] and we built what eventually became the
[L109] [03:14.92] very first version of Bento, which is
[L110] [03:16.80] the noble platform based on Jupiter
[L111] [03:18.84] that's used all across the company. And
[L112] [03:20.88] at first, Bento was really, really dumb.
[L113] [03:22.96] It was just a script that would set up
[L114] [03:24.96] Jupiter for you. But we had this vision
[L115] [03:27.00] behind it. What if, instead of just
[L116] [03:29.36] being this like external tool that you
[L117] [03:31.44] have to set up that doesn't communicate
[L118] [03:32.96] with anything at the company,
[L119] [03:35.32] we integrated that better within the
[L120] [03:37.64] rest of the tooling. What if you could
[L121] [03:39.64] just open a browser, type Bento, and now
[L122] [03:42.08] you have a notebook that's running? And
[L123] [03:44.64] you already have the libraries that are
[L124] [03:46.88] built within
[L125] [03:48.56] the company that you can reuse instead
[L126] [03:50.36] of having to like figure out how to do
[L127] [03:51.88] manually. But if you could have like
[L128] [03:53.68] other programming languages, eventually,
[L129] [03:55.92] you know, people will start hacking hack
[L130] [03:58.24] into that. And so over the course of
[L131] [04:00.08] about a year or so,
[L132] [04:02.12] we started like putting the system
[L133] [04:03.76] together. A big thing that I worked on
[L134] [04:06.44] it after that was building Bento on
[L135] [04:08.68] demand where instead of having a dev
[L136] [04:12.36] server where we would set up the system
[L137] [04:14.52] for you, you could just request an
[L138] [04:17.08] on-demand instance. You could work on
[L139] [04:19.20] that and then release it.
[L140] [04:21.28] Cuz we're doing that for like
[L141] [04:22.92] development environment or like, "Yeah,
[L142] [04:24.32] that makes a lot of sense. You don't
[L143] [04:25.96] have to maintain a dev server." And so
[L144] [04:27.84] in the process of doing that, I, you
[L145] [04:29.24] know,
[L146] [04:30.40] I helped lead the development of the
[L147] [04:31.92] platform, but more importantly, I put
[L148] [04:33.88] the team together. I transitioned into a
[L149] [04:36.72] tech lead manager role. I started
[L150] [04:38.84] building a team.
[L151] [04:40.76] And the way I built the team was
[L152] [04:42.88] hiring people who were very excited
[L153] [04:44.76] about the tooling world. Actually, I
[L154] [04:46.84] just hired a bunch of people who were
[L155] [04:47.96] already building tooling on the side in
[L156] [04:50.16] their spare time. I was like, "Hey, do
[L157] [04:51.88] you want this to be your full-time job?
[L158] [04:53.20] Sounds like you like to do this thing.
[L159] [04:55.52] It's super impactful. Do you want to do
[L160] [04:57.52] this full-time?" And so, you know, I
[L161] [04:59.60] brought in like a bunch of like amazing
[L162] [05:01.08] people. So good team like
[L163] [05:04.04] six, seven, eight people.
[L164] [05:06.64] And so I got promoted to
[L165] [05:09.12] TLM2 mostly on my IC work and the vision
[L166] [05:12.44] I had for Bento.
[L167] [05:13.56] >> And TLM2 for people who are outside of
[L168] [05:16.08] the company is equivalent to senior
[L169] [05:18.20] manager, which is equivalent to senior
[L170] [05:20.68] staff engineer
[L171] [05:22.36] in the industry. And when you hear these
[L172] [05:24.20] great stories of new infrastructure
[L173] [05:26.36] tooling that everyone takes for granted
[L174] [05:28.20] today, what I want to know is what is
[L175] [05:30.56] the step-by-step process on how you
[L176] [05:33.28] actually get the tooling from an idea to
[L177] [05:35.80] something that everyone is using?
[L178] [05:38.12] >> So for Bento, the notebook platform,
[L179] [05:41.60] the answer is we didn't really try to
[L180] [05:45.32] get adoption within people's existing
[L181] [05:48.88] workflows.
[L182] [05:50.00] What I did was twofold. One, we targeted
[L183] [05:53.20] boot camp and data camp. So, boot camp
[L184] [05:56.12] and data camp for non-Facebookers is
[L185] [05:58.84] where you
[L186] [05:59.84] the thing you go through when you
[L187] [06:01.24] onboard at the company. And you we just
[L188] [06:04.16] went to data camp and we told everyone
[L189] [06:06.12] who was working with data, this is the
[L190] [06:07.76] way you set up your developer
[L191] [06:09.40] environment. You just use this thing. Or
[L192] [06:12.20] you can also just like go do it manually
[L193] [06:14.12] if you want. Uh but you can also just
[L194] [06:17.16] like type this one word and you have
[L195] [06:18.72] your developer environment. The company
[L196] [06:20.56] was growing like crazy at the time,
[L197] [06:22.40] right? And so when you have this like
[L198] [06:23.68] amount of insane growth and you know,
[L199] [06:25.92] the company is going to say like double
[L200] [06:27.48] in size within like a year or two, you
[L201] [06:30.16] you get your growth from like all of
[L202] [06:31.60] those newcomers who don't know the
[L203] [06:34.08] legacy systems.
[L204] [06:36.08] And then you get the stragglers because
[L205] [06:38.68] everyone else around them then use the
[L206] [06:41.12] new system. So that was like a lot of
[L207] [06:42.72] the growth strategy behind Bento. The
[L208] [06:44.76] other thing we did with Bento was
[L209] [06:47.56] provide support and maintenance for the
[L210] [06:50.88] legacy systems.
[L211] [06:52.60] Uh and so you know, we built trust with
[L212] [06:54.00] users like that way. So if you were
[L213] [06:56.00] installing Jupiter by yourself, you
[L214] [06:58.16] could go to that group that was
[L215] [07:00.40] unmonitored before us. And we're
[L216] [07:02.92] providing help and we're providing
[L217] [07:03.84] support. Uh and then over time, you
[L218] [07:06.00] know, after building that trust, we
[L219] [07:07.56] started encouraging people and be like,
[L220] [07:09.56] yeah, you know, this like thing you want
[L221] [07:10.92] to do, I can give you a recipe that's
[L222] [07:13.36] going to take 25 steps to do that. Or
[L223] [07:15.68] we've it in Bento. It doesn't really
[L224] [07:18.00] change your workflow. It'll just make
[L225] [07:19.80] your life easier. Uh
[L226] [07:21.80] you'll move to that. So to summarize,
[L227] [07:24.16] you know, step one, find an easy way of
[L228] [07:26.56] getting a bunch of users because network
[L229] [07:28.44] effects work. Step two, for the people
[L230] [07:31.32] who are on the legacy systems, just
[L231] [07:33.00] provide value to them.
[L232] [07:34.68] >> That's super interesting because when I
[L233] [07:36.96] think of these developer offerings, I
[L234] [07:39.64] just always assume that you're going to
[L235] [07:41.56] have to influence a group of people that
[L236] [07:43.92] is using something today to switch off
[L237] [07:46.28] of something. In this particular case,
[L238] [07:49.36] in a growing company, there's this whole
[L239] [07:51.88] new user base. It's like all these
[L240] [07:53.28] people coming in. They're They're
[L241] [07:55.16] deciding from a fresh slate, and it
[L242] [07:57.60] sounds like your offering was a superior
[L243] [07:59.44] product in a sense, so it was a pretty
[L244] [08:01.76] easy sell.
[L245] [08:02.60] >> And then the other thing we did, too,
[L246] [08:03.88] was go to, you know, Alex Schultz, who's
[L247] [08:06.08] now the CMO of the company, but I was
[L248] [08:07.88] head of analytics at the time, and Brady
[L249] [08:10.36] Brady Laubach.
[L250] [08:12.04] Uh and we just told them, "Hey, we know
[L251] [08:14.92] that there's a lot of pain within your
[L252] [08:17.16] teams.
[L253] [08:18.40] We want to help. We think that this is
[L254] [08:20.24] the first step." And, you know, I
[L255] [08:22.12] remember Brady saying, "Yeah, this is
[L256] [08:23.96] This is a good first step. There's like
[L257] [08:25.24] those like 20 other things you need to
[L258] [08:26.64] go fix." I was like, "Okay, let's take
[L259] [08:28.72] it one step at a time. Uh and let's
[L260] [08:31.04] Let's start talking more."
[L261] [08:33.20] There was no team at the time really
[L262] [08:35.40] building tools for data science and
[L263] [08:37.92] machine learning. Uh and so this is when
[L264] [08:40.12] I actually ended up leaving the core
[L265] [08:42.40] data science team, and I reorged myself
[L266] [08:45.12] into the dev infra organization to start
[L267] [08:47.80] that team really focused on data
[L268] [08:49.88] developer tools.
[L269] [08:51.04] >> Yeah, at the beginning of this story,
[L270] [08:52.56] you mentioned you took on some
[L271] [08:54.36] performance system risk. You You
[L272] [08:56.40] literally told your manager, "Hey,
[L273] [08:58.44] I'm going to take on and build something
[L274] [09:00.40] that has a lot of potential, but also it
[L275] [09:02.72] might flop entirely, and then we can
[L276] [09:05.00] scramble to figure out performance of
[L277] [09:07.08] that, you know, you don't get a below um
[L278] [09:10.00] meets all rating." I'm curious cuz at
[L279] [09:13.08] that time like the industry was not as
[L280] [09:16.04] intense when it comes to churning out
[L281] [09:18.04] short-term results. Do you think that
[L282] [09:21.08] trying to do something like that today
[L283] [09:22.84] would be more difficult, and do you have
[L284] [09:24.92] any advice on
[L285] [09:26.40] more generally how to take on risk to
[L286] [09:28.60] pursue these higher rewards?
[L287] [09:30.96] >> I think the consequences of
[L288] [09:33.68] underperforming now are more drastic
[L289] [09:35.72] than they were 10 years ago, for sure. I
[L290] [09:38.16] think the strategies, when you want to
[L291] [09:39.88] take risks, is the same. Make sure
[L292] [09:41.68] you're on the same page with your
[L293] [09:43.64] hierarchy and your manager. Uh at the
[L294] [09:46.00] end of the day, like, you know, we are
[L295] [09:47.28] all evaluated based on our expectations.
[L296] [09:50.76] If you're not aligned on what is
[L297] [09:52.00] expected of you with your manager, then
[L298] [09:54.92] that is a problem. Now, you know, I was
[L299] [09:57.00] on a team whose job was to provide help
[L300] [10:00.16] with data I was data consultant in a
[L301] [10:02.84] way, right?
[L302] [10:04.24] Now, the thing I was building was
[L303] [10:05.56] tooling and infrastructure, not at all
[L304] [10:08.16] data to consulting. So, the first thing
[L305] [10:09.68] I did was like, "Hey manager,
[L306] [10:12.04] I'm not going to do what my job is and
[L307] [10:14.44] what the team is doing because I think
[L308] [10:16.52] there's an opportunity there. Are you
[L309] [10:18.52] okay with me doing this? Can we make it
[L310] [10:20.72] so, you know, we carve out two, three
[L311] [10:22.40] months for me to go explore that and
[L312] [10:24.32] make that part of my expectation? If it
[L313] [10:26.32] pans out, great. If it doesn't pan out,
[L314] [10:28.48] well, I was expected to go explore this.
[L315] [10:30.72] It was a calculated risk. We all agreed
[L316] [10:33.96] as a team, my manager, my skip, myself,
[L317] [10:36.96] that like that was a thing I was going
[L318] [10:38.52] to do.
[L319] [10:39.68] And at that point, you know, there's an
[L320] [10:41.08] agreement this is the job you're going
[L321] [10:42.28] to do. Everyone is on the same page. Uh
[L322] [10:45.28] I think it is a lot riskier to go and do
[L323] [10:49.28] your own thing, you know, you you lock
[L324] [10:51.96] yourself in a room, do your thing for
[L325] [10:53.60] three months, show up and you like, "I
[L326] [10:55.56] did this thing." And then everyone is
[L327] [10:57.68] like, "Yeah, but no one knew that you
[L328] [10:59.48] were doing this thing."
[L329] [11:00.76] Over-communicate, I think, is really the
[L330] [11:03.16] strategy I would recommend.
[L331] [11:05.00] And also be ready to hear no. Like, I
[L332] [11:07.00] was very lucky to have a manager that
[L333] [11:08.48] said, "Yeah, you know, I think that
[L334] [11:10.28] makes it's risky, but it makes sense. Go
[L335] [11:12.12] do that." Uh I've had, you know,
[L336] [11:14.48] instances later on in my career where I
[L337] [11:17.16] wanted to go do a thing and I tried
[L338] [11:18.76] building that consensus and what I was
[L339] [11:20.64] told was, "No, don't do that."
[L340] [11:23.04] >> Hey, thanks for watching that clip. If
[L341] [11:24.52] you thought it was interesting, it's
[L342] [11:25.80] part of a longer conversation, which you
[L343] [11:27.48] can find right here, right now. And as
[L344] [11:29.80] always, if you have any feedback for me,
[L345] [11:31.36] I'd love to hear it. You can leave a
[L346] [11:33.04] comment on YouTube. I read every single
[L347] [11:35.04] one that I get.
