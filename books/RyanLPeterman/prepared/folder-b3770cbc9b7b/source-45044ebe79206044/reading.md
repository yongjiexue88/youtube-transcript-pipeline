# AWS Distinguished Eng: Learning From 3000 Incidents And How Engineering Is Changing | Marc Brooker

Source ID: source-45044ebe79206044
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/AWS_Distinguished_Eng_Learning_From_3000_Incidents_And_How_Engineering_Is_Changing_Marc_Brooker_en.txt
Video: https://www.youtube.com/watch?v=u3GjIXP9N0s

[L10] [00:00.00] If you aren't doing it hands-on, your
[L11] [00:02.32] opinion about it is very likely to be
[L12] [00:05.04] completely wrong. This is Mark Brooker.
[L13] [00:07.96] He's a distinguished engineer [music] at
[L14] [00:09.52] AWS, and I interviewed him for technical
[L15] [00:11.76] learnings from his career. 3,000 cloud
[L16] [00:14.84] system postmortems. I want to ask you,
[L17] [00:16.68] what makes a good postmortem? I could
[L18] [00:18.68] spend a lot of time talking about that.
[L19] [00:20.76] You had a tweet that said that there are
[L20] [00:22.88] cases where caches are bad. I prefer to
[L21] [00:26.60] see the teams around me avoiding caching
[L22] [00:28.84] where possible. We also discussed how
[L23] [00:31.12] software engineering is changing. What
[L24] [00:33.72] is important given that code is kind of
[L25] [00:37.20] flowing like water now? The job changes,
[L26] [00:39.76] and and and you do different work.
[L27] [00:42.16] For someone [snorts] who's structuring
[L28] [00:43.80] their career, would you say it's better
[L29] [00:45.60] to be overrated or underrated?
[L30] [00:49.72] Here's the full episode.
[L31] [00:55.88] At some point, when I was a very junior
[L32] [00:59.16] engineer, I looked at the more senior
[L33] [01:01.56] engineers and said, "What what is the
[L34] [01:02.88] difference between you and I? I'm
[L35] [01:04.48] working more hours than you. I'm I'm you
[L36] [01:07.56] know, landing more code than you. Why is
[L37] [01:10.04] it that you're so much more impactful
[L38] [01:11.52] than I am?" And then I realized that
[L39] [01:14.48] kind of the direction of your work, like
[L40] [01:16.44] what is the thing that you're actually
[L41] [01:17.72] shipping, matters more than the volume
[L42] [01:20.20] of your work and your contributions.
[L43] [01:22.08] What would be your advice on how do you
[L44] [01:24.08] find problems that matter?
[L45] [01:27.24] Yeah, I think you have to go super
[L46] [01:28.56] broad. So, I think there's a set of
[L47] [01:30.48] those things that come in from from
[L48] [01:32.80] customers, from the world, right? Like,
[L49] [01:34.72] here is an unsolved problem.
[L50] [01:36.92] You know, I spend a lot of time meeting
[L51] [01:38.40] with AWS customers and listening to them
[L52] [01:40.28] talk about, you know, what are the
[L53] [01:42.00] things they still find difficult in in
[L54] [01:43.92] our space. What are they, you know, what
[L55] [01:45.68] are they investing in? Where are they
[L56] [01:47.16] spending their time? Where would they
[L57] [01:48.68] prefer to be not spending their time and
[L58] [01:51.52] and focus on their core business
[L59] [01:52.96] instead. And so, that's one rich seam
[L60] [01:56.20] of ideas and and and focus on what's you
[L61] [01:58.48] know what's interesting. I think
[L62] [01:59.64] completely at the other level is
[L63] [02:02.64] sort of on looking at the technical
[L64] [02:04.16] trends and you can look at just the the
[L65] [02:06.24] kind of speeds and feeds like wow,
[L66] [02:08.16] networks have gotten faster, storage has
[L67] [02:10.20] gotten faster. You know, we've seen this
[L68] [02:12.32] huge explosion in in multi-core and now
[L69] [02:15.36] in GPUs and you know, so there's a
[L70] [02:18.52] bottom-up innovation trend there too,
[L71] [02:21.00] which which you can also look at and say
[L72] [02:22.76] well, this enables all of these new new
[L73] [02:25.28] things.
[L74] [02:27.08] And
[L75] [02:28.52] um and then broadly kind of
[L76] [02:30.96] across the world like what what are the
[L77] [02:33.00] big trends that are going on? What are
[L78] [02:34.56] the things that are changing in our
[L79] [02:36.04] industry? What are the things that are
[L80] [02:37.24] changing in in the world and really it
[L81] [02:39.44] is those kind of moments of change that
[L82] [02:41.32] have the
[L83] [02:42.64] you know, bring with them the
[L84] [02:43.60] opportunity to to to build things and
[L85] [02:46.92] and and to recognize problems.
[L86] [02:49.52] And so to pick one, you know,
[L87] [02:50.52] concretely, uh you know, when I was in
[L88] [02:54.52] uh working on the Lambda team in in in
[L89] [02:56.08] 2020 and
[L90] [02:58.04] I was talking to a lot of customers
[L91] [02:59.48] about you know, they were super excited
[L92] [03:00.92] about building on serverless, they were
[L93] [03:02.24] super excited about building on
[L94] [03:03.64] containers, there'd been this massive
[L95] [03:05.24] shift and
[L96] [03:07.36] what people were seeing then was wow, I
[L97] [03:10.20] love these serverless products, I love
[L98] [03:12.16] building this way, but the world of data
[L99] [03:15.44] and especially relational data doesn't
[L100] [03:17.16] fit super well into this this paradigm,
[L101] [03:19.56] right? These relational databases are
[L102] [03:20.96] still very serverful, you know,
[L103] [03:22.84] fantastically powerful products, but but
[L104] [03:25.16] not kind of operationally the same. And
[L105] [03:28.60] you know, that thinking was you know,
[L106] [03:30.68] this felt super important to me of like
[L107] [03:33.00] wow, these customers have have brought
[L108] [03:34.76] to me a gift of of understanding
[L109] [03:37.44] something that's really important and
[L110] [03:39.40] and so I joined the Aurora team, we
[L111] [03:41.96] built Aurora Serverless and then we
[L112] [03:43.60] built uh we built the sequel. You know,
[L113] [03:46.04] we've been investing deeply across all
[L114] [03:48.16] of our database products to make them a
[L115] [03:49.80] better fit for these
[L116] [03:51.28] um
[L117] [03:52.72] you know,
[L118] [03:53.60] uh serverless and and and container
[L119] [03:55.24] workloads.
[L120] [03:56.56] And
[L121] [03:58.00] that is an example of of a trend that
[L122] [04:00.36] was brought by, you know, brought by a
[L123] [04:02.68] customer.
[L124] [04:03.88] Um but then also these trends that have
[L125] [04:06.32] been driven by kind of architectural or
[L126] [04:09.80] um by other things going on, right?
[L127] [04:11.92] Faster networks, faster compute, faster
[L128] [04:14.56] connectivity. It's one of the big
[L129] [04:16.52] technical trends in the database world
[L130] [04:18.28] right now is
[L131] [04:20.04] uh this sort of block storage becoming
[L132] [04:22.68] the
[L133] [04:23.76] default back end, the default uh
[L134] [04:25.80] durability layer for uh for databases of
[L135] [04:28.92] all kinds, from analytics workloads to
[L136] [04:30.76] online workloads. And there's been this
[L137] [04:32.80] incredible explosion around that. And so
[L138] [04:35.48] if you look at what we did with Aurora D
[L139] [04:37.84] sequel, for example,
[L140] [04:40.00] you know, that was
[L141] [04:41.52] very much learning from that trend and
[L142] [04:44.08] and taking a lead on that trend and
[L143] [04:45.40] saying, "Well, we're going to make S3,
[L144] [04:47.12] this this block store that we built uh
[L145] [04:48.84] you know, 20 years ago
[L146] [04:50.68] uh sorry, object store that we built 20
[L147] [04:52.72] years ago
[L148] [04:53.92] uh the
[L149] [04:55.48] underlying
[L150] [04:57.28] uh durability layer of this new
[L151] [04:58.96] database. But obviously it doesn't have
[L152] [05:01.12] the latency properties or or or the rich
[L153] [05:03.32] interface that that that an online
[L154] [05:05.08] database needs. And so we're going to
[L155] [05:06.92] build an architecture on top of that
[L156] [05:09.80] that deals with all of these other
[L157] [05:11.04] things
[L158] [05:12.24] in a much better way, but doesn't have
[L159] [05:13.88] to worry about durability.
[L160] [05:16.48] And you know, so that was this perfect
[L161] [05:18.20] collision of a set of things I was
[L162] [05:20.32] hearing from customers and a set of
[L163] [05:22.64] things that were technical trends coming
[L164] [05:25.36] together and thinking, "Wow, we've we've
[L165] [05:26.84] got this opportunity to build something
[L166] [05:28.56] now that is going to be a market leading
[L167] [05:31.96] product um that would be hard to imagine
[L168] [05:34.96] without either of those, you know, input
[L169] [05:37.00] signals."
[L170] [05:38.84] I I saw something that you wrote. You
[L171] [05:41.24] mentioned that you were on call for 15
[L172] [05:43.12] years somewhere in there. And I've heard
[L173] [05:46.32] many stories of more senior engineers
[L174] [05:48.80] negotiating out of on-call because per
[L175] [05:51.48] unit time it could be perceived as not
[L176] [05:53.72] that impactful.
[L177] [05:55.20] And so why did you stay on-call for so
[L178] [05:57.92] long?
[L179] [05:59.28] I would say that the
[L180] [06:01.28] majority of
[L181] [06:04.08] my in-practice knowledge about how to
[L182] [06:06.96] build distributed systems has come from
[L183] [06:09.28] being on-call
[L184] [06:10.72] and
[L185] [06:12.08] analyzing and deeply understanding
[L186] [06:15.24] these postmortems and and and COEs.
[L187] [06:18.28] Um
[L188] [06:19.56] you know, one of the one of the
[L189] [06:20.80] challenges of of, you know, running a
[L190] [06:23.32] company like AWS and and running
[L191] [06:25.56] large-scale systems is that folks come
[L192] [06:27.40] out of college with great often great
[L193] [06:29.92] knowledge of computer science
[L194] [06:31.00] fundamentals, great programming skills,
[L195] [06:33.52] you know, great mathematical skills, all
[L196] [06:35.08] of that stuff is fantastic.
[L197] [06:37.76] But that without the grounded knowledge
[L198] [06:39.12] of what it actually means to run and
[L199] [06:41.56] understand, you know, understand
[L200] [06:43.56] systems.
[L201] [06:45.16] And, you know, on-call is one of the
[L202] [06:48.12] best ways to learn those things, best
[L203] [06:50.20] ways to see,
[L204] [06:52.08] um you know, how do systems really run?
[L205] [06:54.00] How do they really behave? You know, how
[L206] [06:56.20] do customers really use them? What
[L207] [06:58.80] happens when customers use systems in
[L208] [07:00.64] unexpected ways? How can we make systems
[L209] [07:03.36] more resilient to to customers using
[L210] [07:05.52] them in in in different ways?
[L211] [07:07.92] And I think that should be almost a goal
[L212] [07:10.68] of on-call, right? If you have folks in
[L213] [07:12.52] your teams who are on-call and they're
[L214] [07:14.64] just closing the same ticket over and
[L215] [07:16.80] over. Well, you know, that's where you
[L216] [07:18.64] need to just build some automation. And
[L217] [07:21.28] again, building automation is easier
[L218] [07:22.84] than ever, it's more powerful than ever,
[L219] [07:24.32] fantastic.
[L220] [07:25.76] Um but where you really want to spend
[L221] [07:28.36] the time of the deep experts on your
[L222] [07:30.44] team is, you know, here's something
[L223] [07:33.56] unexpected or or unusual that's happened
[L224] [07:36.28] in in the system. Let's deeply
[L225] [07:38.36] understand that and let's bring that
[L226] [07:40.84] knowledge back to both improving that
[L227] [07:43.52] system and communicating broadly to
[L228] [07:47.52] the the company and and and the outside
[L229] [07:49.80] community what we've learned from that.
[L230] [07:53.96] And so one of the most you know one of
[L231] [07:55.36] the most uh
[L232] [07:58.08] powerful things we do at AWS is we have
[L233] [08:01.84] this mechanism of a very broad weekly
[L234] [08:04.88] meeting where we all get together, you
[L235] [08:06.76] know, engineers from across AWS,
[L236] [08:08.76] leaders, senior leaders from across AWS
[L237] [08:11.64] and talk about COEs, these postmortems
[L238] [08:14.96] that we write.
[L239] [08:16.24] And what we can learn from them.
[L240] [08:18.28] And how we can apply those lessons
[L241] [08:20.80] across the whole company. And I think
[L242] [08:23.84] that
[L243] [08:24.68] particular mechanism, that particular
[L244] [08:26.64] kind of in Wednesday morning meeting
[L245] [08:28.80] that we have
[L246] [08:30.24] um is one of the things that has been a
[L247] [08:33.12] core
[L248] [08:34.92] uh almost causal factor behind you know
[L249] [08:37.76] AWS's success.
[L250] [08:40.12] Uh because it has allowed us to and
[L251] [08:43.36] forced us to spend leadership bandwidth,
[L252] [08:46.88] to spend expertise, to spend the time of
[L253] [08:50.28] our best engineers deeply understanding
[L254] [08:53.04] how our systems operate and why they
[L255] [08:54.92] operate the way they do.
[L256] [08:57.20] Um
[L257] [08:58.32] and you know that level of being just
[L258] [09:00.60] extremely grounded in reality
[L259] [09:03.84] uh
[L260] [09:05.04] helps you design better products, help
[L261] [09:06.80] helps you architect better systems.
[L262] [09:09.64] You know, helps you think more clearly
[L263] [09:10.96] about uh the the next round of things,
[L264] [09:13.80] helps you fix, you know, helps you fix
[L265] [09:15.68] issues. And so it's this fundamental
[L266] [09:17.80] kind of learning exercise. It's a real
[L267] [09:19.68] blessing.
[L268] [09:20.84] Um
[L269] [09:21.80] so I would you know I would recommend on
[L270] [09:23.92] call to to anybody who wants to learn
[L271] [09:26.16] about the practice of of distributed
[L272] [09:28.32] systems. And I would certainly recommend
[L273] [09:31.60] spending time reading COEs, reading
[L274] [09:34.36] postmortems, and and deeply reflecting
[L275] [09:37.00] on not only what can we fix tactically,
[L276] [09:39.80] but what can we fix organizationally and
[L277] [09:42.08] strategically and what kind of tools
[L278] [09:44.28] might might need to exist to to prevent
[L279] [09:47.16] this kind of thing happening again.
[L280] [09:49.80] And you know, you asked earlier about,
[L281] [09:51.92] you know, where do ideas come from? This
[L282] [09:53.28] is another, you know, fantastic kind of
[L283] [09:56.00] flow of ideas of saying,
[L284] [09:58.44] "Wow, you know, we seem to be solving
[L285] [10:00.04] the same problem over and over in
[L286] [10:02.08] different ways and getting it slightly
[L287] [10:04.12] wrong every time."
[L288] [10:06.04] Um you know, can we extract a a tool to
[L289] [10:09.32] do that? Can we build a service around
[L290] [10:11.44] that? Can we Can we build a feature
[L291] [10:13.88] around that to make it easier for us to
[L292] [10:15.72] get right and and and easier for our
[L293] [10:17.84] customers to to get right?
[L294] [10:21.12] Yeah, it's interesting because I think
[L295] [10:23.00] if you ask most engineers, they they
[L296] [10:26.00] really avoid on-call, but it sounds like
[L297] [10:28.12] you you kind of go towards it and you've
[L298] [10:30.48] learned a lot from it because it's a
[L299] [10:32.32] major source of customer problems.
[L300] [10:35.52] Yeah, and again, you know, I think for
[L301] [10:36.88] me it comes down to optimizing for
[L302] [10:38.56] finding the most important things to
[L303] [10:40.24] work on and you know, if you aren't
[L304] [10:43.64] close to operating your actual system
[L305] [10:45.92] and you don't know how it's actually
[L306] [10:47.28] working,
[L307] [10:49.04] how are you supposed to identify what to
[L308] [10:50.88] fix, right? You can come up with some
[L309] [10:52.36] theories about those, but they're
[L310] [10:53.60] probably not going to be right.
[L311] [10:56.08] Um
[L312] [10:57.36] and again, like I I I don't think
[L313] [10:59.44] there's a huge amount of value in
[L314] [11:03.40] the rote ticket closing work of on-call.
[L315] [11:06.44] I think automation, you know, should be
[L316] [11:08.20] doing those kinds of work, but I think
[L317] [11:09.80] there's fantastic value in, you know,
[L318] [11:12.20] deep understanding, deep investigations
[L319] [11:15.04] and and deep reflection on what you
[L320] [11:16.88] learn from
[L321] [11:18.60] postmortems and COEs.
[L322] [11:21.56] I tried to estimate uh a couple of
[L323] [11:23.64] months ago for a talk how many industry
[L324] [11:26.08] postmortems and Amazon COEs I'd I'd read
[L325] [11:28.68] over my career.
[L326] [11:30.76] The best estimate I could come up to and
[L327] [11:32.36] this was about a year ago, was was
[L328] [11:33.84] between three and 4,000.
[L329] [11:36.04] Um and so uh you know, even a little bit
[L330] [11:38.84] of lesson from each one and it tends to
[L331] [11:41.08] you know, tends to stick.
[L332] [11:42.80] Yeah, that was my next question
[L333] [11:44.20] actually. I I looked at the slides from
[L334] [11:46.20] that internal presentation and it said,
[L335] [11:48.68] "I've read approximately 3,000 cloud
[L336] [11:51.96] system postmortems from across the
[L337] [11:53.60] industry." And my immediate thought was
[L338] [11:56.92] I want to ask you what makes a good
[L339] [11:58.48] postmortem.
[L340] [12:00.28] So, I think you know, what makes a
[L341] [12:02.00] really great postmortem is first really
[L342] [12:05.00] getting into the details and making sure
[L343] [12:06.64] that you deeply understand what happened
[L344] [12:09.80] rather than just assuming what happened
[L345] [12:12.08] based on on the biases you bring in.
[L346] [12:15.76] Um and so there's a kind of lesson one
[L347] [12:17.84] there is if you can't understand what
[L348] [12:20.76] happened, well that teaches you
[L349] [12:22.04] something about your logging and metrics
[L350] [12:24.56] and observability and you know, and and
[L351] [12:27.32] simulations and all of these other
[L352] [12:28.88] things.
[L353] [12:30.20] And then once you deeply understand what
[L354] [12:31.88] happened, um then the ability then a
[L355] [12:35.24] great postmortem steps through
[L356] [12:38.52] the whys behind that at multiple levels,
[L357] [12:42.20] right? Like why? Well, yeah, there was a
[L358] [12:44.68] code bug. Okay, sure. Code bugs, yes, we
[L359] [12:47.56] can fix that, but we can't stop there,
[L360] [12:49.96] right? Like why was that missed in
[L361] [12:51.76] testing and validation?
[L362] [12:53.84] You know, for these reasons. Uh you
[L363] [12:55.60] know, what can we improve? What can we
[L364] [12:57.20] build around those? Okay, next step you
[L365] [12:59.96] know, why you know,
[L366] [13:02.48] why was our testing and validation where
[L367] [13:04.88] it was? Or you know, why did we assume a
[L368] [13:08.12] certain thing about the behavior of the
[L369] [13:09.64] system that we wouldn't have assumed
[L370] [13:11.84] before?
[L371] [13:13.00] And so as you sort of get through these
[L372] [13:14.72] deeper and deeper layers,
[L373] [13:17.48] a a great postmortem not only identifies
[L374] [13:20.80] kind of fixes to the proximal cause, but
[L375] [13:23.20] also identifies broader fixes to
[L376] [13:25.96] technology, to organizations, to you
[L377] [13:28.40] know, products and and and and so on.
[L378] [13:31.44] Um and so that's a kind of multiple
[L379] [13:33.24] levels thing, right? And you can't get
[L380] [13:35.36] stuck on
[L381] [13:37.28] you know, what is the the the most
[L382] [13:38.80] proximal cause of of an incident, but
[L383] [13:41.08] you also can't get stuck on this, well,
[L384] [13:43.56] you know, things fail sometimes and what
[L385] [13:46.20] are we going to do about it? And
[L386] [13:48.44] um you you have to come up with a set of
[L387] [13:51.84] you know, really concrete action items
[L388] [13:54.64] to fix things at different levels. Fix
[L389] [13:58.20] this particular line in the software
[L390] [14:00.00] that that caused something, you know,
[L391] [14:01.84] fix the testing processes that that
[L392] [14:03.80] didn't catch that, you know, fix the
[L393] [14:06.96] um you know, maybe social or or team
[L394] [14:09.52] processes that led to those technical
[L395] [14:11.56] processes. Um
[L396] [14:14.48] and you know, and then if you're seeing
[L397] [14:16.36] patterns across multiple postmortems,
[L398] [14:19.72] sort of level those up and say, well,
[L399] [14:21.48] clearly there's a hard underlying
[L400] [14:23.08] problem here. You know, can we build a
[L401] [14:25.92] service around that? Can we build a
[L402] [14:27.92] library around that? Can we build a
[L403] [14:31.56] you know, community of practice around
[L404] [14:33.24] that? You know, are there technical
[L405] [14:35.12] changes we can make uh to to avoid whole
[L406] [14:38.60] classes of things?
[L407] [14:40.44] Um
[L408] [14:42.00] So that's quite a long-winded answer,
[L409] [14:43.56] but I I I do think it is it all flows
[L410] [14:46.92] from
[L411] [14:48.12] understanding and understanding at
[L412] [14:50.12] multiple levels. Like understanding
[L413] [14:51.76] immediately like what happened, but also
[L414] [14:54.12] understanding you know, broadly what
[L415] [14:56.12] happened, you know, technologically and
[L416] [14:58.00] organizationally and and and in context.
[L417] [15:01.44] And then the ability to connect that
[L418] [15:03.20] particular event or or postmortem with
[L419] [15:07.60] other ones, you know, and and and and
[L420] [15:09.76] extract those patterns.
[L421] [15:11.48] You know, one of the things that we we
[L422] [15:13.28] did in D SQL was we spent a lot of time
[L423] [15:15.52] as we were designing that looking
[L424] [15:16.84] around, you know, relational database
[L425] [15:19.00] related postmortems and thinking about
[L426] [15:21.52] both our own and our customers and
[L427] [15:23.44] thinking about, you know, how can we
[L428] [15:24.56] design a database that helps people
[L429] [15:26.32] avoid falling into these traps?
[L430] [15:28.92] Um
[L431] [15:30.48] and, you know, a really common kind of
[L432] [15:33.48] outage pattern folks with relational
[L433] [15:35.72] databases is
[L434] [15:37.92] you have a client
[L435] [15:39.56] on a distributed system, starts a
[L436] [15:41.60] transaction, and then goes out to lunch
[L437] [15:44.40] for whatever reason. And, uh, you know,
[L438] [15:46.80] that could be a GC pause or could be a
[L439] [15:48.72] lossy network or it could be a loss of
[L440] [15:50.24] connectivity and now it's holding locks.
[L441] [15:52.60] Um and so, if you look at, you know,
[L442] [15:55.08] relational databases, they don't tend to
[L443] [15:56.84] be resilient to clients misbehaving in
[L444] [15:59.48] that way. And that's a really common
[L445] [16:01.36] cause of
[L446] [16:03.92] uh, operational issues for systems built
[L447] [16:05.88] on relational databases. And so, as we
[L448] [16:08.16] were designing D SQL, we were thinking,
[L449] [16:10.68] how do we avoid
[L450] [16:12.92] uh, broadly that class of problems? And
[L451] [16:16.08] so, folks can say, "Hey, I'm going to
[L452] [16:18.04] build on D SQL and just not have this
[L453] [16:20.00] whole class of problems."
[L454] [16:21.84] Uh, and, you know, I think that's a
[L455] [16:23.64] really kind of powerful
[L456] [16:25.72] outer loop over the postmortem process
[L457] [16:28.08] is to say, "How do we turn all of these
[L458] [16:30.84] lessons into new services and into
[L459] [16:33.08] service improvements?"
[L460] [16:35.56] How do you prevent misbehaving clients
[L461] [16:38.00] from being a problem for the database?
[L462] [16:41.16] Yeah, so in in D SQL's case, um
[L463] [16:44.28] we have uh, we have no pessimistic
[L464] [16:46.48] locking. And so, it the within the scope
[L465] [16:50.12] of a transaction, uh, everything that
[L466] [16:52.32] happens in that transaction, all of the
[L467] [16:54.68] reads happen using this mechanism called
[L468] [16:56.56] multi-version concurrency control, where
[L469] [16:59.72] every row in the database, we sort of
[L470] [17:01.44] store a history of versions. And so, you
[L471] [17:03.84] can read an old version of a row without
[L472] [17:06.12] blocking writers and saying, "Hey, you
[L473] [17:07.64] can't you can't update this cuz I just
[L474] [17:09.24] read it."
[L475] [17:10.24] Um and then, you know, locally within
[L476] [17:13.32] the query processor that's handling a
[L477] [17:15.36] connection, uh, we spool the rights
[L478] [17:17.80] locally and then you get to commit time
[L479] [17:19.56] and we do this optimistic check of uh,
[L480] [17:22.48] you know, can I commit this transaction
[L481] [17:24.20] at at at the transaction commit time.
[L482] [17:27.36] And so, combining those two mechanisms
[L483] [17:29.20] of having multi-version concurrency
[L484] [17:30.84] control and and the scale-out storage
[L485] [17:33.20] that comes with it
[L486] [17:35.08] and the commit time optimistic checks,
[L487] [17:39.84] we can strongly say that, you know,
[L488] [17:42.68] there is no way that a reader of a piece
[L489] [17:44.68] of data can block other writers and
[L490] [17:46.92] there's a no way that that a writer of
[L491] [17:49.00] data can block readers.
[L492] [17:51.44] Um, writers can block writers, but only
[L493] [17:55.00] um,
[L494] [17:56.04] only by changing data, not just by
[L495] [17:57.96] looking at it. And so, you can, you
[L496] [17:59.92] know, you can say, well, you know, I can
[L497] [18:01.96] cause, um, Sorry, writers can't block
[L498] [18:04.92] writers, but they can prevent other
[L499] [18:06.24] writers
[L500] [18:07.24] uh, transactions from eventually
[L501] [18:08.52] committing by making a bunch of changes.
[L502] [18:10.92] And that is
[L503] [18:12.36] inherent to the definition of the
[L504] [18:15.88] particular database isolation level. Out
[L505] [18:18.52] of curiosity, in practice, what percent
[L506] [18:21.64] overhead would you expect for keeping
[L507] [18:24.24] copies of old rows for the sake of those
[L508] [18:26.88] stale reads? Yeah, it's actually
[L509] [18:28.72] surprisingly small. And it's
[L510] [18:30.84] surprisingly small because if you look
[L511] [18:32.72] at the access patterns for most online
[L512] [18:34.64] databases, even ones that do a lot of
[L513] [18:36.92] write traffic, that write traffic tends
[L514] [18:39.36] to be quite concentrated. Uh, and, you
[L515] [18:42.60] know, it's quite unusual for an online
[L516] [18:44.60] database workload or even an analytics
[L517] [18:46.68] workload
[L518] [18:48.00] to
[L519] [18:49.16] make a second version of every row in
[L520] [18:51.76] the database. Typically, what it's doing
[L521] [18:53.56] is making a,
[L522] [18:55.28] you know, first, second, third,
[L523] [18:56.40] hundredth version of this row and a
[L524] [18:58.08] fiftieth version of that row, but the
[L525] [18:59.64] vast majority of data isn't changing.
[L526] [19:02.40] And so, it's super workload dependent,
[L527] [19:04.36] uh, as as is everything in in in the
[L528] [19:06.52] database world, uh, but the overhead
[L529] [19:09.12] tends to be relatively small.
[L530] [19:11.84] Uh,
[L531] [19:12.52] I would say it's unusual for
[L532] [19:16.80] a online database workload for that
[L533] [19:19.80] overhead on storage to be more than
[L534] [19:21.76] about 10%.
[L535] [19:23.56] From my experience, I've seen an
[L536] [19:25.40] interesting dichotomy between teams
[L537] [19:28.08] where some teams they really understand
[L538] [19:29.92] postmortem culture. They tend to be
[L539] [19:31.40] infrastructure teams. They tend to take
[L540] [19:33.64] it really seriously and everyone in on
[L541] [19:36.04] those teams, the tech leads are asking
[L542] [19:37.68] you, "Hey, why why did that happen?" And
[L543] [19:39.92] you know, really follow up and make sure
[L544] [19:41.88] it's it's not a problem. Then I've also
[L545] [19:44.00] noticed on other teams that is less of a
[L546] [19:46.76] strong muscle. For those teams that
[L547] [19:49.40] don't take it too seriously, what would
[L548] [19:51.40] be your your pitch for why they should
[L549] [19:53.72] take it seriously?
[L550] [19:55.44] Yeah, it all comes down to where you
[L551] [19:56.80] want to spend your time, right? Do you
[L552] [19:58.36] want to spend your time improving your
[L553] [20:00.28] product and and making it better or do
[L554] [20:02.08] you want to spend your time
[L555] [20:04.28] uh fighting the same fire over and over?
[L556] [20:07.04] And uh you know, really the
[L557] [20:10.56] culture of building
[L558] [20:13.00] um
[L559] [20:14.36] you know, building great postmortem
[L560] [20:16.36] cultures to make sure that at the the
[L561] [20:18.24] the
[L562] [20:19.44] pros- at the product level and at the
[L563] [20:21.52] organizational level,
[L564] [20:23.64] um
[L565] [20:24.92] you are
[L566] [20:26.96] fixing known issues
[L567] [20:29.52] and you are avoiding having the same
[L568] [20:31.92] problems multiple times.
[L569] [20:34.68] Um and typically when I see teams that
[L570] [20:38.80] have you know, a poor postmortem
[L571] [20:41.24] culture, I think they're
[L572] [20:43.64] probably one of two failure modes there.
[L573] [20:46.28] You know, one of them is a
[L574] [20:49.08] lack of focus on just the outcomes,
[L575] [20:52.04] right? Like, you know, a lack of of of
[L576] [20:54.12] really
[L577] [20:55.44] um
[L578] [20:56.60] I wouldn't say caring enough. I think
[L579] [20:58.52] that's a little bit too too personal,
[L580] [21:00.44] but being really focused on on, you
[L581] [21:03.04] know, is this
[L582] [21:04.24] is this product performing super well?
[L583] [21:06.28] Are we you know, are we really making
[L584] [21:08.44] our customers happy? And that is
[L585] [21:10.32] fundamentally a cultural and and and
[L586] [21:12.32] leadership cultural problem
[L587] [21:14.72] of of setting the right standards. Oh,
[L588] [21:17.00] and by the way, like I don't think, you
[L589] [21:18.52] know, standards should be
[L590] [21:20.56] uh you know, should be uniform, right?
[L591] [21:22.48] Like there are places where you know,
[L592] [21:25.56] the details really really matter where
[L593] [21:28.08] things like durability are just critical
[L594] [21:30.56] and and and you do need to have super
[L595] [21:32.48] high standards in those places.
[L596] [21:34.60] Um
[L597] [21:35.60] and you know, places where
[L598] [21:37.88] you want to optimize for other things
[L599] [21:39.40] and and and maybe have, you know, have
[L600] [21:41.32] have a a higher production defect rate.
[L601] [21:44.04] And I think that's that's okay.
[L602] [21:46.20] Um as long as that's an intentional
[L603] [21:48.76] decision that's being made. So, that's
[L604] [21:50.92] kind of case one, right? Like
[L605] [21:52.80] insufficient focus on the outcome.
[L606] [21:56.72] I think case two, and and this is a
[L607] [21:58.32] harder one to change,
[L608] [22:00.72] is normalization of kind of operational
[L609] [22:03.96] heroics. Like, we don't need to fix
[L610] [22:06.04] these root causes because our on-calls
[L611] [22:08.68] are super heroic and they're going to
[L612] [22:10.04] stay up all night and they're going to,
[L613] [22:12.24] you know, they're going to hack around
[L614] [22:13.40] things and they don't mind being paged
[L615] [22:14.92] 100 times a week. And
[L616] [22:18.60] they can feel from the inside like it's
[L617] [22:20.56] a good culture, right? Like, oh wow,
[L618] [22:22.56] these people are super strong owners.
[L619] [22:24.24] They're super engaged. They really care.
[L620] [22:26.24] They're really working hard on call.
[L621] [22:28.88] And those are all good signals. But then
[L622] [22:31.24] when you look at it from the outside,
[L623] [22:32.48] it's like, well, we're not actually
[L624] [22:33.72] fixing the causes of things. We're just
[L625] [22:35.64] doing this fantastically expensive
[L626] [22:38.68] investment of taking all of these people
[L627] [22:40.64] and their strong ownership and their
[L628] [22:42.44] expertise and spending them just on on
[L629] [22:44.48] on this break-fix cycle.
[L630] [22:46.84] And that's where you need to kind of
[L631] [22:47.84] look at it from the outside and say,
[L632] [22:49.92] well, let's take this energy of this
[L633] [22:51.80] team, fantastic energy, and focus it on
[L634] [22:56.20] uh on on improving the service, getting
[L635] [22:58.56] getting out of the cycle, finding, you
[L636] [23:01.00] know, finding new things to fix, finding
[L637] [23:03.08] new things to build.
[L638] [23:05.00] And that can be hard because it can be
[L639] [23:07.16] hard for, you know, those folks who've
[L640] [23:10.04] been in that mode to look at it and say,
[L641] [23:13.40] "This feels so good. It feels really
[L642] [23:15.72] like we're we're caring about our
[L643] [23:17.20] customers and caring about our product
[L644] [23:18.92] and caring about our business."
[L645] [23:20.92] Uh, to realize that oh, no, we're
[L646] [23:23.32] actually caring about it at the wrong
[L647] [23:24.72] level and we're not serving our business
[L648] [23:27.48] in the best possible way by being so
[L649] [23:30.40] narrowly and tactically focused on this
[L650] [23:32.68] break-fix cycle. And that's where you
[L651] [23:34.68] sort of need to pop them out and say,
[L652] [23:36.56] "Well,
[L653] [23:37.56] let's spend more time thinking about the
[L654] [23:40.84] postmortem. Let's spend more time
[L655] [23:42.80] thinking about the causes of things.
[L656] [23:45.24] Let's let's spend more time addressing
[L657] [23:47.88] these things in a more uh, strategic
[L658] [23:50.52] way." And wow, okay, now you've got so
[L659] [23:52.80] much more time to do that because you've
[L660] [23:54.44] broken the cycle and you can improve
[L661] [23:56.52] your product in different ways. I mean,
[L662] [23:58.92] since you have worked on AWS for almost
[L663] [24:03.08] two decades, uh,
[L664] [24:04.80] I'm sure you have a lot of experience
[L665] [24:06.28] building distributed systems and I think
[L666] [24:09.12] one of the most common advice that you
[L667] [24:10.84] hear, I guess this is maybe in the
[L668] [24:12.40] context of system design, is I I almost
[L669] [24:16.28] hear almost 100% of the time people will
[L670] [24:18.52] say, "Just throw a cache on it." Or you
[L671] [24:21.44] know, you'll have a system design and
[L672] [24:22.80] say, "How do you make it better? Let's
[L673] [24:24.20] put a cache here. Let's put a cache
[L674] [24:25.52] there." And I saw you had a tweet that
[L675] [24:28.04] said that there are cases where caches
[L676] [24:30.56] are are bad despite people saying it's
[L677] [24:32.76] best practice. I was curious if you
[L678] [24:34.48] could explain that. Yeah, so caching's
[L679] [24:36.84] good, right? Like it's hey, I'm I'm
[L680] [24:38.36] going to uh, take the these core ideas
[L681] [24:40.92] from computer science of of temporal and
[L682] [24:42.84] spatial locality and I am going to
[L683] [24:45.44] exploit those to make my system faster,
[L684] [24:48.84] scale better, et cetera. And so, you
[L685] [24:50.92] know, obviously very attractive. But,
[L686] [24:54.72] the downside of caches, especially in
[L687] [24:56.68] distributed systems, is they have this
[L688] [24:58.36] mode, right? Like they have this um you
[L689] [25:01.08] know the there's a mode where the cache
[L690] [25:02.68] is full, and the cache is full of the
[L691] [25:05.04] right data in time and space to perform
[L692] [25:07.52] very well.
[L693] [25:08.84] And there's a mode where the cache is
[L694] [25:10.16] empty or contains the wrong data.
[L695] [25:13.16] And
[L696] [25:14.52] in the first mode, the system is fast
[L697] [25:17.20] and happy and healthy.
[L698] [25:19.56] In the second mode, the system is slow,
[L699] [25:22.40] often down, because now the back end
[L700] [25:25.04] doesn't scale to deal with
[L701] [25:27.40] all of this under-cache traffic.
[L702] [25:29.56] Customers are very disappointed.
[L703] [25:31.88] Um
[L704] [25:33.32] and often it is down in a stable way.
[L705] [25:36.16] And this is this kind of idea of
[L706] [25:37.40] meta-stable failures, where the system
[L707] [25:39.72] has has um
[L708] [25:41.60] switched from state one to state two,
[L709] [25:44.12] and in state two it's still stable,
[L710] [25:45.76] right? Like it's still it's down, but
[L711] [25:48.16] it's not going to come back up under its
[L712] [25:49.72] own energy, because for example, all of
[L713] [25:52.88] this traffic is causing a huge amount of
[L714] [25:54.60] contention in my database, or it's
[L715] [25:57.00] saturating the network, and so I can't
[L716] [25:58.72] even refill the cache. It's not even
[L717] [26:00.80] getting the right kind of data in.
[L718] [26:03.48] And so, you know, when I talk about the
[L719] [26:05.04] downsides of caches, it's really about,
[L720] [26:07.28] you know, how do we avoid that modality
[L721] [26:11.28] between
[L722] [26:12.84] you know, fast and you know, uh the that
[L723] [26:16.60] that failure of caches, and the you
[L724] [26:19.96] know, how do we avoid the state where
[L725] [26:21.12] we're down?
[L726] [26:22.32] Um
[L727] [26:23.56] And so, if I go back to
[L728] [26:26.00] to DSQL, like our answer there is DSQL,
[L729] [26:29.32] what we call the storage tier, is
[L730] [26:30.72] essentially a cache, but it is a
[L731] [26:32.76] complete cache. It contains every row in
[L732] [26:35.64] the database.
[L733] [26:36.96] Um and so, it doesn't have this mode
[L734] [26:38.80] where how do I recover from it being
[L735] [26:41.04] empty or containing the wrong data? It
[L736] [26:43.36] contains all of the data.
[L737] [26:45.64] Um
[L738] [26:47.68] similarly, if you look at a a more,
[L739] [26:50.24] let's say, classical relational database
[L740] [26:52.12] design like Aurora,
[L741] [26:53.96] the Aurora leader is constantly telling
[L742] [26:56.20] the potential failover targets, "Here's
[L743] [26:57.96] something you should cache. Here's
[L744] [26:59.08] something you should cache. Here's
[L745] [27:00.12] something you should cache."
[L746] [27:01.64] So, when a failover happens, the cache
[L747] [27:03.96] is warm on, you know, on on the failover
[L748] [27:06.80] target. Um and so, those are the kinds
[L749] [27:09.68] of things that you can do to avoid those
[L750] [27:11.60] modalities.
[L751] [27:13.28] But, in general,
[L752] [27:14.92] um
[L753] [27:16.20] you know, and I I I wouldn't extract
[L754] [27:17.92] this as a rule or or or
[L755] [27:19.72] or or say that, you know, this applies
[L756] [27:21.64] 100% of the time,
[L757] [27:23.68] but in general, I prefer to see the
[L758] [27:26.44] teams around me avoiding caching where
[L759] [27:28.60] possible.
[L760] [27:29.88] I prefer patterns where you have a,
[L761] [27:33.36] let's say, complete materialized view of
[L762] [27:35.56] the data if you need very fast access to
[L763] [27:37.80] it, especially if it's slow moving. Just
[L764] [27:39.96] pull it down onto your local machine and
[L765] [27:41.48] work with it in memory.
[L766] [27:43.08] You know, if it's only being updated
[L767] [27:44.32] once a week, who cares? Like, just make
[L768] [27:46.08] lots of copies of it.
[L769] [27:47.72] Um
[L770] [27:49.32] Uh so, that's that's one pattern. Or,
[L771] [27:51.60] you know, use a scalable back end, you
[L772] [27:53.80] know,
[L773] [27:54.72] or Dynamo DB or whatever your favorite
[L774] [27:56.84] scalable database is,
[L775] [27:58.88] and keep your database vendor honest
[L776] [28:01.16] about getting to the the scale and
[L777] [28:03.04] performance you need, rather than
[L778] [28:04.44] putting a cache in front of things.
[L779] [28:06.52] So, caching isn't a bad pattern, but it
[L780] [28:08.60] is a pattern with some
[L781] [28:11.16] significant downsides that are, you
[L782] [28:13.32] know, really
[L783] [28:14.88] uh best avoided.
[L784] [28:17.00] In practice, how how often do you see
[L785] [28:19.68] that metastable failure, though? Yeah,
[L786] [28:22.76] you know, this is uh it's not it's not
[L787] [28:24.88] super common, right? Like, you might go
[L788] [28:26.32] years without seeing, you know,
[L789] [28:28.04] something like that. But, if you look
[L790] [28:29.56] across
[L791] [28:31.48] the biggest, most impactful,
[L792] [28:34.36] uh you know, system postmortems across
[L793] [28:36.04] the industry, I would say that these
[L794] [28:38.04] kinds of metastable failures have been
[L795] [28:41.40] an underlying cause in probably a
[L796] [28:44.12] majority of them. And
[L797] [28:47.16] it's super important that, you know, as
[L798] [28:48.88] an industry and as a community of
[L799] [28:50.36] practice, we understand those things
[L800] [28:51.96] deeply because
[L801] [28:53.84] the also those cases where these do
[L802] [28:56.48] happen,
[L803] [28:57.84] you know, tend to be larger-scale
[L804] [29:00.88] issues, longer recovery-time issues, and
[L805] [29:04.48] and and more complex-to-fix issues,
[L806] [29:06.68] right? Where you have to often, you
[L807] [29:09.00] know, turn it off and turn it back on
[L808] [29:10.40] again, which is this very very painful
[L809] [29:12.96] thing for a a a team or an organization
[L810] [29:15.60] to do.
[L811] [29:16.88] Um
[L812] [29:18.20] and you know, and so again, like you you
[L813] [29:20.36] might go years operating a system with
[L814] [29:22.08] seeing nothing like this. And and but if
[L815] [29:24.80] you look at the most impactful issues,
[L816] [29:27.72] it's actually fairly common as an
[L817] [29:30.04] underlying cause for those issues. And
[L818] [29:31.76] so, you know, it's kind of both of these
[L819] [29:33.44] things of being quite uncommon and being
[L820] [29:35.68] being rather common.
[L821] [29:37.20] I was reading your blog and you have a
[L822] [29:39.40] series of posts on how AI may impact the
[L823] [29:43.40] future of software engineering. And I
[L824] [29:44.80] kind of want to pick your brain on that.
[L825] [29:46.60] So, what's your perspective on how you
[L826] [29:49.36] think AI will uh impact software
[L827] [29:52.20] engineering and how it'll change things?
[L828] [29:54.48] Yeah, I mean, it's, you know, hard maybe
[L829] [29:56.44] harder than ever to tell the future. And
[L830] [29:58.36] so, you know, this is a a set of uh
[L831] [30:00.80] maybe guesses uh and and and predictions
[L832] [30:03.44] about about the future. Um
[L833] [30:06.24] So, I'll I'll say the first thing I I,
[L834] [30:08.08] you know, I deeply believe about
[L835] [30:09.64] software is
[L836] [30:12.12] we have only just started to see the
[L837] [30:16.12] impact that software is going to have on
[L838] [30:17.96] the world. There is such an opportunity
[L839] [30:21.16] for
[L840] [30:22.44] more software to exist, bigger software,
[L841] [30:25.16] better software, more personal software.
[L842] [30:28.00] You know, all of these things. And so,
[L843] [30:29.40] software has, throughout its well, its
[L844] [30:32.32] 60-ish-year history, been
[L845] [30:35.52] supply constrained.
[L846] [30:37.84] And, you know, I think that's going to
[L847] [30:39.48] remain true. I think the opportunity for
[L848] [30:42.48] for software in the world is is just,
[L849] [30:44.76] you know, almost almost unbounded.
[L850] [30:47.76] Um and that's really exciting, right?
[L851] [30:49.40] It's really exciting to be at a moment
[L852] [30:51.36] when
[L853] [30:52.44] the economics of building software are
[L854] [30:54.60] changing and and are changing rather
[L855] [30:56.60] quickly.
[L856] [30:57.84] Um and that gives us an opportunity to
[L857] [31:00.72] think about what could we do in the
[L858] [31:02.96] world with a lot more software?
[L859] [31:05.36] Um you know, a lot more
[L860] [31:08.12] software personalization, a lot more
[L861] [31:11.48] just the right software in the right
[L862] [31:13.16] place at the right time.
[L863] [31:15.72] And
[L864] [31:17.72] you know, that gives me a huge amount
[L865] [31:19.52] of, uh, you know, excitement about the
[L866] [31:21.24] future of of this industry,
[L867] [31:23.76] uh, because, you know, we we have a
[L868] [31:26.48] massive opportunity ahead of us, both
[L869] [31:29.16] driven by these changing economics of
[L870] [31:32.48] software development.
[L871] [31:34.76] Um
[L872] [31:35.72] now, also with those changes, there are
[L873] [31:37.84] going to be needs for, you know, us as
[L874] [31:40.64] software practitioners, people who build
[L875] [31:42.36] software, people who who love software
[L876] [31:44.36] to to adapt. And, uh, you know,
[L877] [31:48.56] that that means that that software
[L878] [31:50.28] careers are going to look different. Um
[L879] [31:53.16] uh, they're going to look different
[L880] [31:54.32] early on, they're going to look
[L881] [31:55.36] different later on. I think the software
[L882] [31:57.68] business is going to look different. And
[L883] [32:01.08] the
[L884] [32:02.48] um
[L885] [32:03.56] success of people and organizations over
[L886] [32:05.80] the next, uh,
[L887] [32:07.12] you know, next who knows, 5 years,
[L888] [32:09.92] decade, is going to be largely
[L889] [32:12.12] predicated on their ability to adapt to
[L890] [32:15.08] that change and and to lead that change.
[L891] [32:18.16] You told the story about this guy who
[L892] [32:19.96] bet on analog circuits when, obviously,
[L893] [32:23.20] we know digital became kind of the more
[L894] [32:25.92] more dominant way.
[L895] [32:27.72] Yet, he made he made good money. For the
[L896] [32:29.68] people who maybe don't want to adapt,
[L897] [32:32.44] you could still get by and succeed. It's
[L898] [32:35.76] not going to be like a crazy thing. Is
[L899] [32:38.32] that is that kind of the takeaway and
[L900] [32:40.40] why you brought up that story? Yeah, I I
[L901] [32:42.16] I I I
[L902] [32:42.88] I think that's that's the right
[L903] [32:44.08] takeaway. And so if I sort of break
[L904] [32:45.76] down, you know,
[L905] [32:47.40] the the the world into to three tiers, I
[L906] [32:50.72] you know, I think there's going to
[L907] [32:51.80] remain a huge amount of joy in the craft
[L908] [32:55.72] of software. Um,
[L909] [32:57.52] you know, like the craft of of joinery
[L910] [32:59.48] with, you know, with handsaws, right?
[L911] [33:01.16] Like it's it's a nice way to spend time.
[L912] [33:04.12] It's not a particularly economically
[L913] [33:06.52] interesting activity anymore, but not
[L914] [33:09.16] everything we do has to be an
[L915] [33:10.40] economically interesting opportunity. It
[L916] [33:12.12] can just be something I do because I
[L917] [33:14.28] enjoy it, because I enjoy the product of
[L918] [33:16.24] it, because I enjoy talking to people
[L919] [33:17.96] about it, right? And so there is, you
[L920] [33:20.12] know, I I I don't think that is going to
[L921] [33:21.72] go away. I think we're going to see,
[L922] [33:24.12] you know, a lot of interest in in that.
[L923] [33:25.72] Like there's been interest in in
[L924] [33:26.88] retrocomputing and, you know, people who
[L925] [33:28.96] run an Apple II as their desktop. And
[L926] [33:30.72] like, well, again, it's wildly
[L927] [33:33.56] impractical. It's not economically
[L928] [33:35.20] interesting, but it's fun and something
[L929] [33:36.60] I, you know, could do as a hobby. And
[L930] [33:38.36] so, you know, that's that's going to be
[L931] [33:40.84] a remaining part of of of the world of
[L932] [33:43.28] software for probably forever.
[L933] [33:46.16] Um, and then there's this this, you
[L934] [33:48.32] know,
[L935] [33:49.28] kind of story that that I told in the
[L936] [33:50.88] blog post.
[L937] [33:52.60] And I think this relates to,
[L938] [33:56.08] you know,
[L939] [33:56.76] driving change in the real world it's
[L940] [33:58.56] always harder than it looks from the
[L941] [34:00.20] outside, right? Like as you get into the
[L942] [34:01.92] details things become more difficult.
[L943] [34:04.76] They become more dependent on people.
[L944] [34:06.52] They become more dependent on politics
[L945] [34:08.36] and policy and um,
[L946] [34:10.80] you know, our our various
[L947] [34:11.84] irrationalities as humans. And And so
[L948] [34:14.44] driven by that,
[L949] [34:16.92] you know, there is going to be a
[L950] [34:19.64] huge amount of and a shrinking over time
[L951] [34:23.04] amount, but it but a huge amount of the
[L952] [34:25.92] software industry that is run
[L953] [34:28.60] in what I might call the old way, right?
[L954] [34:31.68] Past techniques, past languages, past
[L955] [34:34.88] technologies.
[L956] [34:36.40] And there's real economic opportunity in
[L957] [34:40.00] engaging with that part of the, you
[L958] [34:42.00] know, part of the world. Um you know, as
[L959] [34:44.48] we saw with with analog electronics,
[L960] [34:46.68] analog electronics will very much exist.
[L961] [34:48.68] In fact, there are
[L962] [34:50.48] parts of the world like, you know, like
[L963] [34:52.64] radio and power systems where there's
[L964] [34:54.60] been incredible technology technological
[L965] [34:56.76] advancement in in in those fields.
[L966] [34:59.44] Uh but they have become more niche, and
[L967] [35:01.12] so, you know, digital became the
[L968] [35:02.56] mainstream. We wouldn't be talking like
[L969] [35:04.40] we are today
[L970] [35:05.92] if it wasn't for this uh you know, 12
[L971] [35:09.84] orders of magnitude or whatever
[L972] [35:11.16] explosion in in digital transistor
[L973] [35:13.04] counts.
[L974] [35:14.88] Um
[L975] [35:17.36] but there's interesting opportunity
[L976] [35:18.76] there, and I think that interesting
[L977] [35:19.92] opportunity is going to change shape and
[L978] [35:22.28] and and become more and more specialized
[L979] [35:24.48] and and and more and more niche and and
[L980] [35:26.48] great careers to be built there.
[L981] [35:28.44] Um and then there is the mainstream,
[L982] [35:30.28] which I think is going to adopt these
[L983] [35:33.04] new technologies from agentic
[L984] [35:34.80] development to AI-powered development
[L985] [35:37.16] to, you know, specification-driven
[L986] [35:39.36] development um and, you know, a whole
[L987] [35:41.92] lot of other, you know, new things whose
[L988] [35:44.08] names we don't even know yet
[L989] [35:46.64] um
[L990] [35:47.68] to build software at a speed and a cost
[L991] [35:52.72] that is unimaginable to do with with old
[L992] [35:56.08] techniques.
[L993] [35:57.80] And I think that is where correctly the
[L994] [36:01.36] majority of the industry is going to be
[L995] [36:03.04] going. I think that's where the majority
[L996] [36:04.76] of careers are going to be built. I
[L997] [36:06.72] think that's where the majority of um
[L998] [36:08.96] economic opportunity is. It's the space
[L999] [36:11.60] I'd be in if I was building a company
[L1000] [36:13.40] today. It's the space I'm in in my role.
[L1001] [36:16.16] Um and you know, the one I would sort of
[L1002] [36:18.36] personally be most excited about.
[L1003] [36:21.12] But yeah, it isn't only one. I think
[L1004] [36:22.68] there's going to be the spectrum of
[L1005] [36:24.16] software practice, and especially where
[L1006] [36:26.52] software engages with the physical
[L1007] [36:28.32] world, uh there are going to be some
[L1008] [36:30.52] really interesting
[L1009] [36:33.48] questions about how do we bring these
[L1010] [36:35.64] new technologies, how do we bring these
[L1011] [36:37.28] new practices into
[L1012] [36:41.24] the various many niches that software is
[L1013] [36:43.48] going to and has, you know, over over
[L1014] [36:45.44] six decades kind of wormed its way into.
[L1015] [36:49.52] It's interesting you mentioned joinery.
[L1016] [36:51.64] I wonder if
[L1017] [36:53.92] down the road
[L1018] [36:55.40] we'll see apps on the app store that
[L1019] [36:56.80] people pay extra for because it's
[L1020] [36:59.44] marketed as this was written by a human
[L1021] [37:02.28] or it's it was written by hand. It's a
[L1022] [37:04.36] bespoke
[L1023] [37:06.04] you know, custom app.
[L1024] [37:08.60] Crazy how the world's going to change.
[L1025] [37:10.16] But so it sounds like you know, change
[L1026] [37:11.88] is obviously the the common case. It's
[L1027] [37:13.80] the one that we should be thinking
[L1028] [37:14.88] about. Maybe we can break up the
[L1029] [37:16.68] conversation into parts. One is for
[L1030] [37:19.20] junior engineers.
[L1031] [37:20.92] What is important given that code is
[L1032] [37:24.88] kind of flowing like water now?
[L1033] [37:27.24] At risk of being a bit meta about our
[L1034] [37:28.80] past conversation, it really is about
[L1035] [37:30.56] finding those problems that matter and
[L1036] [37:32.28] and and doing that early in in a career.
[L1037] [37:35.04] And
[L1038] [37:36.48] you know, that requires an understanding
[L1039] [37:39.52] of customers. It requires an
[L1040] [37:41.00] understanding of the business. It
[L1041] [37:42.32] requires an understanding of of
[L1042] [37:43.96] economics and and and of systems.
[L1043] [37:46.84] And
[L1044] [37:48.84] that can I think that's going to move
[L1045] [37:52.48] from being
[L1046] [37:54.12] you know, almost kind of senior engineer
[L1047] [37:56.12] work of like oh, well, you know, now
[L1048] [37:57.84] you're going to go and talk to customers
[L1049] [37:59.12] and actually understand the context of
[L1050] [38:00.72] the stuff you're building
[L1051] [38:02.52] to being more and more part of
[L1052] [38:06.00] even the earliest steps of an
[L1053] [38:08.12] engineering career. Right? Like here's
[L1054] [38:10.08] the context. Here's the problem. Here's
[L1055] [38:11.88] the customer. Let's go off and work
[L1056] [38:13.40] together and solve
[L1057] [38:15.04] you know, and and and and solve this
[L1058] [38:16.52] problem with all of this context.
[L1059] [38:19.92] And
[L1060] [38:21.76] I think that's going to be
[L1061] [38:25.40] super exciting for one set of folks,
[L1062] [38:28.68] uh, and a little bit frustrating for
[L1063] [38:30.20] people who have come into um,
[L1064] [38:34.92] you know, looking for a pure software
[L1065] [38:36.40] development career, right? Looking for a
[L1066] [38:38.20] career where they sit down, open their
[L1067] [38:40.32] IDE,
[L1068] [38:42.32] start typing and and don't stop for
[L1069] [38:44.28] eight hours. I think that's going to be
[L1070] [38:46.12] a mode that we're going to see fewer
[L1071] [38:48.20] people in and a mode that's going to be
[L1072] [38:50.44] harder and harder to build a career
[L1073] [38:52.64] around. Now, the other mode of, "Oh, I'm
[L1074] [38:55.08] excited to go off and learn from my
[L1075] [38:56.72] customers about what they're building
[L1076] [38:58.12] and what they need." I think that's
[L1077] [38:59.96] going to be ever more highly, you know,
[L1078] [39:01.80] highly valuable. And so, super exciting
[L1079] [39:04.44] opportunity to build,
[L1080] [39:06.44] you know, build careers there.
[L1081] [39:08.72] And then maybe and and this might come
[L1082] [39:10.36] across as being a little bit, um, you
[L1083] [39:12.60] know, paradoxical. I think there's also
[L1084] [39:14.36] a ton of opportunity for, you know,
[L1085] [39:16.80] folks who are extremely technically
[L1086] [39:18.76] deep, um, you know, who are, uh,
[L1087] [39:22.60] you know, deep on optimization problems
[L1088] [39:25.56] or deep on infrastructure problems or
[L1089] [39:28.68] deep on, you know, various scientific
[L1090] [39:31.00] things or deep on databases or deep on,
[L1091] [39:34.40] you know, one of the many, many topics
[L1092] [39:36.40] that are all behind our industry.
[L1093] [39:39.32] Because I think the ability to
[L1094] [39:42.96] ans- ask the right questions is also
[L1095] [39:46.08] much more valuable than it was has ever
[L1096] [39:48.56] been.
[L1097] [39:49.76] And so, I think there is a ton of
[L1098] [39:51.72] opportunity for people coming into the
[L1099] [39:53.64] industry with deep technical or
[L1100] [39:56.04] scientific knowledge to now leverage
[L1101] [39:59.28] that in ways that, you know, maybe were,
[L1102] [40:02.08] um, were hard before, right? There was
[L1103] [40:04.24] too much sort of boiler plate to really,
[L1104] [40:06.20] you know, to really use that leverage
[L1105] [40:08.36] that you have. And so, I think we're
[L1106] [40:10.08] going to see a lot more of of of those
[L1107] [40:11.80] kinds of careers, of really kind of
[L1108] [40:13.32] building expertise in a technical topic,
[L1109] [40:16.08] in a scientific topic, and then be able
[L1110] [40:18.48] to turn that into software and software
[L1111] [40:21.56] products in a way that
[L1112] [40:24.84] was really difficult before, and in some
[L1113] [40:26.60] cases wasn't possible before, and is now
[L1114] [40:29.48] um you know, vastly easier.
[L1115] [40:31.72] If I was to look at a career ladder's
[L1116] [40:33.56] expectation, some of what you described
[L1117] [40:35.60] of maybe engaging with the customers and
[L1118] [40:38.60] understanding the business context,
[L1119] [40:40.80] uniquely in software engineering, it
[L1120] [40:42.28] feels like
[L1121] [40:43.56] the earliest levels are insulated from
[L1122] [40:46.32] all of that. You have your your tech
[L1123] [40:48.24] lead, tech leads handing out tasks, and
[L1124] [40:51.00] then the early level engineers just
[L1125] [40:53.68] given task just convert it into code.
[L1126] [40:56.08] And this sounds like you know, that
[L1127] [40:57.60] part's relatively solved. And if not
[L1128] [41:01.04] now, maybe I I'd be surprised if a year
[L1129] [41:03.68] or two from now wasn't like completely
[L1130] [41:06.32] solved. Um and I I think that could
[L1131] [41:09.64] scare a lot of junior engineers cuz they
[L1132] [41:11.64] they would think you're going to expect
[L1133] [41:13.64] me to graduate from college or start
[L1134] [41:16.84] working as a software engineer, and then
[L1135] [41:18.96] I would have the senior engineer
[L1136] [41:20.68] expectations.
[L1137] [41:22.40] Um what would you say to the the scared
[L1138] [41:25.08] software engineer that's just entering
[L1139] [41:26.68] the industry to all this change?
[L1140] [41:30.04] Yeah, you know, I think um
[L1141] [41:32.76] what I would remind them that, you know,
[L1142] [41:35.84] we as people who hire and build
[L1143] [41:38.44] organizations of software engineers, and
[L1144] [41:40.44] and they as people who have are building
[L1145] [41:42.84] software engineering careers, have have
[L1146] [41:44.72] really
[L1147] [41:46.00] um aligned incentives, right? Like you
[L1148] [41:48.84] know,
[L1149] [41:49.72] it it's not valuable to hire a bunch of
[L1150] [41:52.24] people and set them up to fail. Like
[L1151] [41:54.16] that's
[L1152] [41:55.04] nobody wants that. It's it's it's not an
[L1153] [41:57.28] outcome uh that is good for anybody. And
[L1154] [42:00.64] so, yeah, we're going to need to figure
[L1155] [42:02.72] out how do you support people on on that
[L1156] [42:05.76] path? How do you help people learn those
[L1157] [42:08.60] things? How do you give them the right
[L1158] [42:10.40] guardrails, you know? Hey, that first
[L1159] [42:12.80] time that you go out and talk to a
[L1160] [42:14.20] customer, yeah, it's going to be scary.
[L1161] [42:15.96] My My first time talking to an AWS
[L1162] [42:17.72] customer,
[L1163] [42:19.12] I was you know was
[L1164] [42:21.04] I was was super scary, but you know, I I
[L1165] [42:24.16] I got a bunch of help with that and I
[L1166] [42:25.56] got a bunch of advice and I got a bunch
[L1167] [42:27.16] of mentorship and I got a bunch of
[L1168] [42:28.48] feedback and I got better and better at
[L1169] [42:30.08] that over time and I think that's
[L1170] [42:32.08] exactly what these things look like is,
[L1171] [42:34.44] you know, you start off and you you
[L1172] [42:35.76] start small and and and and you learn,
[L1173] [42:39.00] you know, as you go and and and so that
[L1174] [42:41.00] feedback loop goes faster. And so I
[L1175] [42:43.76] don't expect that people coming in
[L1176] [42:46.36] from college or
[L1177] [42:48.48] you know, will will will come in with
[L1178] [42:49.88] all of this knowledge. I think, you
[L1179] [42:51.56] know, it's never been true that people
[L1180] [42:53.60] coming into technical or engineering
[L1181] [42:55.24] career straight out of college know
[L1182] [42:56.68] everything. Or any career for that
[L1183] [42:58.96] matter, right? Like you talk to to
[L1184] [43:00.68] teachers about, you know, what they've
[L1185] [43:02.68] learned on their job versus what they
[L1186] [43:04.52] learned, you know, studying.
[L1187] [43:06.60] Uh you know, they learn a huge amount in
[L1188] [43:09.00] in in things like internships and and
[L1189] [43:11.36] and so on and and over the course of a
[L1190] [43:13.12] career.
[L1191] [43:14.44] Um or doctors or or anybody in, you
[L1192] [43:16.56] know, in in a field like that. Um
[L1193] [43:19.48] and so yeah, it is going to be about
[L1194] [43:20.84] learning and I think the emphasis on
[L1195] [43:22.36] what people learn is going to be
[L1196] [43:23.92] different.
[L1197] [43:25.20] I think it is going to require,
[L1198] [43:28.88] you know, leaders like me who,
[L1199] [43:31.64] you know, care deeply about, you know,
[L1200] [43:33.32] hiring and and and developing folks
[L1201] [43:35.32] early in their career to be really
[L1202] [43:36.96] thoughtful about what, you know, what
[L1203] [43:38.44] does that new letter look like and
[L1204] [43:40.64] um
[L1205] [43:41.76] and you know, we're we're doing a lot of
[L1206] [43:43.32] that thinking. I think people are doing
[L1207] [43:44.80] that kind of thinking across the
[L1208] [43:46.16] industry.
[L1209] [43:47.52] Uh and uh
[L1210] [43:50.08] yeah, it's changing fast. It's It's
[L1211] [43:51.76] uncertain. It's It's It's an interesting
[L1212] [43:53.68] time to to to be graduating. But again,
[L1213] [43:56.32] like it's a super exciting time. I think
[L1214] [43:58.16] that's just the the the scale of the
[L1215] [43:59.56] opportunity is bigger than it's ever
[L1216] [44:01.04] been.
[L1217] [44:02.48] Sounds like your advice for senior
[L1218] [44:04.20] engineers is different from that of
[L1219] [44:06.40] junior engineers. What What is your
[L1220] [44:08.44] thinking there? Yeah, I mean, I think
[L1221] [44:11.48] you know, I think for for folks there
[L1222] [44:12.96] the challenges is is how do you you
[L1223] [44:15.16] know, how do you retain the value of of
[L1224] [44:17.20] this incredible experience and knowledge
[L1225] [44:19.00] that you've gained over a career
[L1226] [44:21.12] while you know, not falling behind
[L1227] [44:24.28] while learning how to you know, best
[L1228] [44:26.12] best use the tools.
[L1229] [44:28.04] And you know, when I look at
[L1230] [44:31.56] senior folks, this is a is a challenge,
[L1231] [44:34.36] you know, hit of them. I think a lot of
[L1232] [44:36.00] people have found themselves in
[L1233] [44:38.76] influence and and and leadership type
[L1234] [44:40.88] positions where they aren't hands-on
[L1235] [44:43.20] building, you know, every day and I
[L1236] [44:45.04] think it's going to be harder and harder
[L1237] [44:47.52] to be
[L1238] [44:49.12] in that kind of role
[L1239] [44:51.12] and
[L1240] [44:52.36] be able to influence and advise in a
[L1241] [44:56.76] um
[L1242] [44:58.52] in a relevant way in a in a in a
[L1243] [45:00.72] positive way.
[L1244] [45:02.40] Um and so really I think my advice for
[L1245] [45:04.92] folks is is is you kind of got to get
[L1246] [45:06.68] building. Like you got to get back in
[L1247] [45:08.60] get back into it. You need to
[L1248] [45:10.84] deeply understand how the practice of
[L1249] [45:14.40] building software and the practice of
[L1250] [45:16.08] designing software has changed and and
[L1251] [45:19.08] is continuing to change.
[L1252] [45:21.40] And and so the challenge is how do I you
[L1253] [45:25.04] know, really take advantage of all of
[L1254] [45:26.88] this knowledge and expertise that I've
[L1255] [45:28.68] built up in my career
[L1256] [45:30.60] and be super curious and be super
[L1257] [45:33.48] hands-on and really be in the details.
[L1258] [45:36.64] And the good news for that Well, I think
[L1259] [45:38.48] there's two bits of good news. One of
[L1260] [45:39.76] them is because of these new tools, you
[L1261] [45:42.92] know, time spent as a practitioner is is
[L1262] [45:45.96] so much more leveraged than it is today.
[L1263] [45:47.76] You can build
[L1264] [45:49.04] so such cool stuff, you know, in in
[L1265] [45:52.12] during that period of time the the
[L1266] [45:54.60] amount of kind of
[L1267] [45:56.72] wasted time and boilerplate and so on is
[L1268] [45:59.52] is so much smaller and so you really do
[L1269] [46:01.56] have this opportunity.
[L1270] [46:03.52] And the other one is again, like why did
[L1271] [46:05.60] you know,
[L1272] [46:06.52] why did we get into this space? Well,
[L1273] [46:09.68] I didn't get into it so I could go to
[L1274] [46:11.20] meetings and sound smart. I got into it
[L1275] [46:13.20] because I love learning and because I
[L1276] [46:14.68] love building technology and because I
[L1277] [46:16.84] love, you know, solving my customers
[L1278] [46:18.80] problems and because I love, you know,
[L1279] [46:20.72] learning about new, you know, new
[L1280] [46:22.68] technologies and learning new things.
[L1281] [46:24.36] And And there's more opportunity to do
[L1282] [46:26.32] that than ever before. Again, you know,
[L1283] [46:28.12] because of this this new set of tools
[L1284] [46:30.00] and the leverage that comes with them.
[L1285] [46:31.32] And so, really is getting back to,
[L1286] [46:34.40] you know, why are you here? Why did you
[L1287] [46:35.76] get into this career? And I think it
[L1288] [46:37.32] really gets us
[L1289] [46:38.84] as technology-focused people
[L1290] [46:42.00] closer to
[L1291] [46:43.88] the our original answer to that.
[L1292] [46:46.24] It's really obvious to me right now when
[L1293] [46:48.20] I speak to, you know, practitioners,
[L1294] [46:51.32] you know, who and who isn't
[L1295] [46:54.16] using a, you know, modern set of
[L1296] [46:56.40] agentic-powered
[L1297] [46:58.00] developer practices. Right? And the
[L1298] [46:59.80] people who are, um, have these really
[L1299] [47:02.96] interesting things to say about the
[L1300] [47:04.44] strengths and weaknesses of those
[L1301] [47:05.88] approaches and the work that still needs
[L1302] [47:07.64] to be done and the integrations that
[L1303] [47:09.24] still need to be done and the things
[L1304] [47:11.12] that are working and aren't. Uh, and the
[L1305] [47:13.40] people who aren't,
[L1306] [47:14.92] you know, using them hands-on
[L1307] [47:17.60] have such
[L1308] [47:20.56] a poor mental model of how they work,
[L1309] [47:23.88] what they're good at, what they're not
[L1310] [47:25.36] good at, that the things they say about
[L1311] [47:27.80] them tend to vary tend to be essentially
[L1312] [47:30.28] fiction.
[L1313] [47:31.36] Um, and so, you know, I think we are in
[L1314] [47:33.96] this minute that if you aren't doing it
[L1315] [47:36.24] hands-on, your opinion about it is is
[L1316] [47:39.68] very likely to be completely wrong.
[L1317] [47:42.40] And that takes a level of humility to
[L1318] [47:45.44] admit that, you know, is is is tough.
[L1319] [47:48.12] You know, it's it's tough for folks with
[L1320] [47:49.44] fancy titles and it's tough for folks
[L1321] [47:51.08] with with distinguished careers. Uh, but
[L1322] [47:53.72] I I think it's a must.
[L1323] [47:55.48] I I feel like there's a common sentiment
[L1324] [47:58.24] among software engineers when they when
[L1325] [48:00.92] they work with someone who is a you
[L1326] [48:04.12] know, quote unquote tech lead but
[L1327] [48:05.80] they're not really hands-on. So, they've
[L1328] [48:08.00] kind of been in the docks for the last 5
[L1329] [48:10.76] years or or so and there's these minor
[L1330] [48:13.64] things they can tell that this person
[L1331] [48:15.92] doesn't actually understand the
[L1332] [48:17.40] underlying thing and sounds like that
[L1333] [48:19.56] gap will widen with these new tools,
[L1334] [48:22.44] which is if you're you're looking at
[L1335] [48:24.36] things from 1,000 ft up and you're not
[L1336] [48:27.04] actually using the tools, that's just
[L1337] [48:29.20] another thing that separates you from
[L1338] [48:31.72] the people who are actually building
[L1339] [48:33.52] where you'll be very out of touch. And I
[L1340] [48:35.96] I think uh you know, when I look at I
[L1341] [48:39.00] think that's always been true. I think
[L1342] [48:40.36] it is wider than you know, ever before.
[L1343] [48:43.28] Um
[L1344] [48:44.44] and but when I look at the
[L1345] [48:47.24] you know, engineering leaders that I've
[L1346] [48:49.20] really respected and learned a huge
[L1347] [48:50.88] amount from over my career. Uh you know,
[L1348] [48:53.44] for example, some of the folks who who
[L1349] [48:55.80] built S3, you know, 20 years ago,
[L1350] [48:59.64] that was such a successful product
[L1351] [49:02.00] because those folks were so deep in the
[L1352] [49:04.36] details and so grounded on the use cases
[L1353] [49:06.64] and so deep in the economics and and
[L1354] [49:08.60] really just did um
[L1355] [49:10.92] you know, really thought about
[L1356] [49:13.40] uh
[L1357] [49:14.24] both the kind of strategic world of like
[L1358] [49:16.48] how is this cloud thing going to change
[L1359] [49:18.68] the way people want to interact with
[L1360] [49:20.16] storage,
[L1361] [49:21.68] but also the
[L1362] [49:24.16] you know, minute-to-minute details of
[L1363] [49:26.04] what's fast now, what's slow, what's
[L1364] [49:27.92] good, what's bad. And I think you know,
[L1365] [49:30.12] when you think about a extremely
[L1366] [49:32.16] enduring product like S3,
[L1367] [49:35.20] um
[L1368] [49:36.84] at or or EC2, I think it's it's been
[L1369] [49:40.44] that groundedness in the details from
[L1370] [49:42.60] from early on from all levels of
[L1371] [49:44.76] leadership that has made those things
[L1372] [49:47.16] so successful. Um
[L1373] [49:50.04] where you know, other products seemingly
[L1374] [49:52.92] with the same amount of early promise
[L1375] [49:56.60] didn't turn out to be as successful.
[L1376] [49:59.68] I think one of the last topics that I
[L1377] [50:02.48] wanted to ask you about was writing. Um,
[L1378] [50:05.72] you have a ton of awesome posts on your
[L1379] [50:08.76] blog. The style of writing is incredibly
[L1380] [50:11.80] clear.
[L1381] [50:12.92] And I I was curious, why do you write so
[L1382] [50:16.40] much as an engineer?
[L1383] [50:19.36] Writing and and speaking, uh, but
[L1384] [50:21.80] especially writing have this incredible
[L1385] [50:23.76] power.
[L1386] [50:24.84] Um, and
[L1387] [50:26.40] you know, for for technical folks, it's
[L1388] [50:28.28] this incredible multiplier in being able
[L1389] [50:30.44] to take these ideas that's in your head
[L1390] [50:33.28] and share them with the world.
[L1391] [50:35.80] Um,
[L1392] [50:36.88] and you know, you can can take a set of
[L1393] [50:39.44] technical ideas in your head and share
[L1394] [50:41.68] them with the world by building a great
[L1395] [50:43.12] product and that's a fantastic thing to
[L1396] [50:44.76] do.
[L1397] [50:45.64] Uh, you can share them in the world kind
[L1398] [50:47.04] of one-on-one, you know, mentorship,
[L1399] [50:49.40] teach people, learn, small groups, also
[L1400] [50:52.76] a great way to spend time.
[L1401] [50:54.88] But the
[L1402] [50:56.64] multiplication factor of doing a talk or
[L1403] [51:00.24] even more of of writing something is so
[L1404] [51:03.12] much higher, right? Like, there are so
[L1405] [51:05.04] many more people that you can share that
[L1406] [51:07.48] with and it lasts for a much longer
[L1407] [51:10.32] period of time.
[L1408] [51:12.16] Um,
[L1409] [51:13.52] and so just having something written on
[L1410] [51:15.20] my blog even that I wrote like a decade
[L1411] [51:16.96] ago that I can share with someone and
[L1412] [51:18.56] say, you know, here's you know, here's
[L1413] [51:20.60] how to think about this problem, here's
[L1414] [51:22.12] an insight that I I I wanted to share
[L1415] [51:24.04] with you. Or or have people discover
[L1416] [51:26.56] that organically is a super powerful.
[L1417] [51:29.04] And so, writing lets you scale out the
[L1418] [51:31.96] impact of your expertise in in space and
[L1419] [51:34.64] time in a way that's really hard to do
[L1420] [51:37.40] in other media. I think with with video
[L1421] [51:40.00] and with podcasts and so on, you know,
[L1422] [51:41.80] we've seen other ways to do that. But I
[L1423] [51:44.12] think writing remains kind of uniquely
[L1424] [51:46.76] powerful.
[L1425] [51:48.96] And then there's this also this idea,
[L1426] [51:50.44] which is this kind of kind of core
[L1427] [51:52.04] belief culturally at Amazon, and I've
[L1428] [51:54.40] obviously been in
[L1429] [51:55.80] affected by this over the years, that
[L1430] [51:58.32] you know, writing forces a level of
[L1431] [52:00.72] mental clarity that speaking, making
[L1432] [52:04.52] slide decks, etc. doesn't. And you know,
[L1433] [52:08.04] that's something that is also really
[L1434] [52:09.36] been my experience of sitting down
[L1435] [52:12.32] to write something down forces me to
[L1436] [52:14.52] think that through
[L1437] [52:16.68] at a depth that I wouldn't have been
[L1438] [52:18.84] been forced to think it through without
[L1439] [52:20.64] that.
[L1440] [52:21.88] Um and so it's all one of you know, your
[L1441] [52:24.00] early conversations with was with Leslie
[L1442] [52:25.76] Lamport, who kind of takes that a step
[L1443] [52:27.28] further and say, "Hey, you know, it's
[L1444] [52:29.28] formal mathematics that is the next step
[L1445] [52:31.08] there." And I I love that point. Um
[L1446] [52:34.52] but I I I think writing is this really
[L1447] [52:36.28] accessible thing for for people to do
[L1448] [52:38.36] that does force a level of thinking. And
[L1449] [52:40.88] so I do a lot of writing, sometimes just
[L1450] [52:43.08] for myself, right? Like I'll I'll write
[L1451] [52:45.72] not ever intending to share it with
[L1452] [52:48.44] anybody,
[L1453] [52:49.68] but just to sharpen my own thinking on a
[L1454] [52:52.44] on a particular point. And so it's some
[L1455] [52:55.08] of that combination of three things,
[L1456] [52:56.56] right? Like I just I just have something
[L1457] [52:58.80] to say and I want to say it. Um you
[L1458] [53:01.20] know, I have something to say and I want
[L1459] [53:02.52] to scale it out in in time and space.
[L1460] [53:05.08] And I want to sharpen my own thinking on
[L1461] [53:08.04] a on a subject um
[L1462] [53:11.32] or or or the thinking of a small group
[L1463] [53:13.20] on a subject in a way that writing is
[L1464] [53:16.08] just a super powerful tool to to do.
[L1465] [53:20.16] Definitely. Yeah, I remember being
[L1466] [53:22.04] surprised early in my career, I had a
[L1467] [53:25.24] manager tech lead who we would write
[L1468] [53:28.12] these these docs on you know, either the
[L1469] [53:30.28] designs or the strategy, and he said,
[L1470] [53:33.60] "Even if you just wrote it and you threw
[L1471] [53:35.44] it away, it would still be worthwhile
[L1472] [53:37.88] because you'll realize things as you're
[L1473] [53:40.28] writing, and that clarity will save you
[L1474] [53:42.80] a lot of time down the road.
[L1475] [53:44.80] Um and it's interesting to me cuz a lot
[L1476] [53:47.28] of engineers
[L1477] [53:48.68] they complain about writing docs. Docs
[L1478] [53:51.08] and you know, all the stuff around the
[L1479] [53:52.56] code. They kind of they kind of hate
[L1480] [53:54.28] that. They say it's a sign of slow, big
[L1481] [53:57.28] company processes and you know, what
[L1482] [53:59.80] would you say to an engineer like that
[L1483] [54:01.68] who's saying, "I just just let me write
[L1484] [54:03.16] the code." Yeah, and that's a great you
[L1485] [54:05.04] know, it's a great point and I think it
[L1486] [54:06.64] really depends on the level of problem
[L1487] [54:09.48] you're trying to solve. And so, you
[L1488] [54:11.56] know, if I look at
[L1489] [54:14.24] I'm going to pick on UML for a minute
[L1490] [54:16.64] here, right? Like it's a sort of
[L1491] [54:17.88] semi-formal software design process and
[L1492] [54:20.96] not one that I've ever found useful
[L1493] [54:22.76] because I think it just happens at the
[L1494] [54:24.04] wrong semantic level. I think it's
[L1495] [54:26.04] bothered with details at a level that
[L1496] [54:27.96] aren't helpful.
[L1497] [54:29.44] Um
[L1498] [54:30.76] and I think a lot of the let's go off
[L1499] [54:32.64] and document this has has a similar
[L1500] [54:34.76] problem, right? Like does this actually
[L1501] [54:37.20] require that level of reflection and
[L1502] [54:40.72] thinking?
[L1503] [54:41.96] Um
[L1504] [54:43.00] and so I think what, you know, for me
[L1505] [54:45.68] separates a valuable doc writing and and
[L1506] [54:49.52] thinking process from a busy work
[L1507] [54:52.04] process is understanding what you're
[L1508] [54:54.96] getting out of it.
[L1509] [54:56.40] And what you're getting out of it might
[L1510] [54:57.96] be an artifact to share with the future,
[L1511] [55:00.60] which is super valuable.
[L1512] [55:02.48] Um either your future self if you've got
[L1513] [55:04.16] a terrible memory like me or, you know,
[L1514] [55:06.80] new teams, new people, people ex- you
[L1515] [55:09.36] know,
[L1516] [55:10.16] or I want to share something with
[L1517] [55:11.48] customers or I want to share something
[L1518] [55:12.92] with the world. And so that's super
[L1519] [55:14.20] valuable.
[L1520] [55:15.56] Or I want to write down something so I
[L1521] [55:18.76] can think through a really difficult,
[L1522] [55:22.00] often one-way door kind of
[L1523] [55:24.76] un- hard to change technical decision or
[L1524] [55:28.40] API design decision.
[L1525] [55:30.36] And I'm not going to do that every time
[L1526] [55:33.00] I make a technical decision. It's not
[L1527] [55:34.64] worth it because a lot of those
[L1528] [55:35.84] technical decisions are either easy or
[L1529] [55:38.72] or not as critical or can be just be
[L1530] [55:40.44] taken back if we figure out they're
[L1531] [55:42.12] wrong.
[L1532] [55:43.48] But I am going to to spend my time that
[L1533] [55:45.76] way when there are key decisions to
[L1534] [55:49.48] make, when there are key
[L1535] [55:51.92] um
[L1536] [55:52.64] insights to to find.
[L1537] [55:56.12] And
[L1538] [55:57.84] I think, you know, and so
[L1539] [56:00.56] it is that like what is the purpose of
[L1540] [56:02.40] writing?
[L1541] [56:03.56] Uh that
[L1542] [56:04.92] uh is that that separates
[L1543] [56:06.92] well-spent time from
[L1544] [56:09.68] poorly spent time.
[L1545] [56:11.68] Now, there are people who still don't
[L1546] [56:13.28] like writing even when it's well-spent
[L1547] [56:15.16] time, even when it's like
[L1548] [56:17.80] you know, you have to explain this piece
[L1549] [56:19.72] of technology to, you know, to a future
[L1550] [56:21.96] team. Um
[L1551] [56:23.88] I think that's a skill worth developing.
[L1552] [56:25.72] You know, sometimes you you do need to,
[L1553] [56:27.76] you know, uh eat your vegetables, uh you
[L1554] [56:30.40] know, and it's it's it is a skill worth
[L1555] [56:32.36] getting good at.
[L1556] [56:33.96] Um
[L1557] [56:35.56] and you know, especially in
[L1558] [56:39.20] documenting the core kind of technical
[L1559] [56:41.52] decisions behind a design is is so
[L1560] [56:44.60] useful. And that's useful in two ways,
[L1561] [56:46.68] by the way. Like one of them is as we
[L1562] [56:49.16] think about building a big system,
[L1563] [56:51.32] um we make thousands of decisions. And
[L1564] [56:55.44] some of those decisions are very
[L1565] [56:57.96] carefully chosen, very particular, and
[L1566] [57:01.36] very impactful.
[L1567] [57:03.44] And some of those decisions are
[L1568] [57:06.08] the best thing we could guess in the
[L1569] [57:07.64] moment based on having no data to make
[L1570] [57:09.72] that decision.
[L1571] [57:11.24] And it's super useful for people who are
[L1572] [57:13.28] coming in to improve that system down
[L1573] [57:15.76] the line to be able to look at the
[L1574] [57:18.08] design and say which of these things
[L1575] [57:20.24] were very carefully chosen and thought
[L1576] [57:21.88] through, and which of these things were
[L1577] [57:23.72] arbitrary.
[L1578] [57:25.40] And because the arbitrary things like
[L1579] [57:27.56] okay, well, I'm going to change that and
[L1580] [57:29.20] I'm going to just go ahead and change
[L1581] [57:30.44] that cuz I have better data now. I've
[L1582] [57:32.00] watched the system run. I can go and
[L1583] [57:33.48] change those. And these other ones were
[L1584] [57:35.40] like, well, let me really engage with
[L1585] [57:37.36] the reason that we made this decision.
[L1586] [57:38.96] Maybe it was non-obvious. Maybe there
[L1587] [57:40.56] was some some more advanced thinking.
[L1588] [57:42.76] And so, being able to kind of understand
[L1589] [57:45.16] the amount of thought that went into a
[L1590] [57:47.00] decision is almost as important as
[L1591] [57:48.84] understanding what that thought was. You
[L1592] [57:51.40] had a really interesting blog post. This
[L1593] [57:53.32] was um
[L1594] [57:54.60] from a while back. It it's titled the
[L1595] [57:57.56] four hobbies and apparent expertise.
[L1596] [58:01.12] And you introduced this really
[L1597] [58:03.04] interesting idea. It's a 2 by 2 matrix.
[L1598] [58:05.64] And on one side, there's doing versus
[L1599] [58:08.68] discussing. And on the other side,
[L1600] [58:11.08] there's the hobby and the gear. Maybe I
[L1601] [58:13.88] can overlay it for people who want to
[L1602] [58:15.84] see. And then later you you kind of
[L1603] [58:17.52] liken that to your career and how I
[L1604] [58:20.56] guess maybe we can imagine the hobby is
[L1605] [58:23.00] is actually coding. And maybe the gear
[L1606] [58:25.48] is
[L1607] [58:26.44] let's just say it's like your dev setup
[L1608] [58:27.84] or something like that. You talked about
[L1609] [58:29.60] these two aspects of being in in
[L1610] [58:33.00] depending on which quadrant you are,
[L1611] [58:34.48] which is there's this trade-off between
[L1612] [58:36.76] expertise and visibility. Where imagine
[L1613] [58:39.92] you're really into coding and you're
[L1614] [58:41.52] really into doing, you're going to be
[L1615] [58:44.16] phenomenal in terms of expertise, but
[L1616] [58:47.12] maybe not as visible, cuz you're not
[L1617] [58:49.24] talking with everyone about how cool
[L1618] [58:51.64] your setup is and and all of that. And
[L1619] [58:54.40] on the flip side, if you're really into
[L1620] [58:56.80] the gear, or maybe your setup in this
[L1621] [58:58.88] case, and you're really into discussing,
[L1622] [59:01.04] you're you're on all the messaging posts
[L1623] [59:03.60] and that, you might not actually be that
[L1624] [59:05.40] good at at coding, but you're very
[L1625] [59:07.80] visible and you have this apparent
[L1626] [59:10.64] competence.
[L1627] [59:12.12] And I thought that trade-off was really
[L1628] [59:13.68] interesting, because I've seen that so
[L1629] [59:15.44] much in software engineering, too, is
[L1630] [59:17.32] there might be someone who's
[L1631] [59:19.04] really quiet coder. They never write
[L1632] [59:21.12] anything, but they know everything, cuz
[L1633] [59:23.92] they've just been in the weeds all the
[L1634] [59:25.92] time. And then there are people on the
[L1635] [59:28.00] complete opposite end of the spectrum
[L1636] [59:29.48] that writing all the time, speaking all
[L1637] [59:31.92] the time, but maybe not actually
[L1638] [59:34.12] practicing as much. And my question to
[L1639] [59:36.60] you is, how do you strike that balance?
[L1640] [59:38.40] Cuz obviously too far in either
[L1641] [59:39.96] direction is not optimal. So, how do you
[L1642] [59:42.72] strike that balance?
[L1643] [59:44.44] Yeah, that's uh you know, that's that's
[L1644] [59:46.72] something that I reflect on a on a lot.
[L1645] [59:49.28] Uh you know, and I do explicitly think
[L1646] [59:50.92] that sort of being 100% on either of
[L1647] [59:52.80] those ends is a is a is a is a failure
[L1648] [59:55.00] mode. And I think
[L1649] [59:56.60] you know, I I will say that
[L1650] [59:58.96] I have a lot more
[L1651] [01:00:01.72] personal enjoyment working with the
[L1652] [01:00:03.88] people that are 100% on the doing side
[L1653] [01:00:06.56] and and 0% on the talking side. I I I I
[L1654] [01:00:09.28] appreciate and and deeply you know,
[L1655] [01:00:11.28] deeply love their expertise. Um
[L1656] [01:00:14.68] but I I I do think that you know, they
[L1657] [01:00:16.48] they could have more impact and and and
[L1658] [01:00:18.64] leverage if if if they you know, swung a
[L1659] [01:00:20.76] little bit away from that. Um
[L1660] [01:00:23.08] you know, I I tend to not enjoy as much
[L1661] [01:00:25.88] interacting with the people who are 100%
[L1662] [01:00:27.92] on on on on the speaking side. Um
[L1663] [01:00:31.48] Uh but I I
[L1664] [01:00:33.40] and I think they would you know, have a
[L1665] [01:00:35.20] lot more
[L1666] [01:00:37.04] relevant things to say
[L1667] [01:00:39.44] you know, if if if they you know, swung
[L1668] [01:00:42.00] a little bit back towards the center.
[L1669] [01:00:45.56] The other challenge of being on a 100%
[L1670] [01:00:47.36] on the doing side is sort of gets back
[L1671] [01:00:48.92] to that, how do you find the really
[L1672] [01:00:50.28] important problems? And you know, if
[L1673] [01:00:52.48] your head's down in your IDE all day
[L1674] [01:00:56.08] you could very likely be working on the
[L1675] [01:00:58.36] wrong thing.
[L1676] [01:00:59.84] Um you know, something that that isn't
[L1677] [01:01:01.52] as as important, isn't as impactful. Um
[L1678] [01:01:05.52] you know, doesn't have these properties
[L1679] [01:01:06.88] that that people want. So, you know, how
[L1680] [01:01:09.24] how do you find the optimal balance? Uh
[L1681] [01:01:11.52] I don't have a have a recipe for you
[L1682] [01:01:13.80] know, what really is is optimal.
[L1683] [01:01:17.04] I tend to
[L1684] [01:01:19.56] do about let's say 75/25
[L1685] [01:01:23.20] kind of practitioner versus you know
[L1686] [01:01:25.52] teaching and and and and communicating.
[L1687] [01:01:28.28] Maybe 80/20 at times. I found that's
[L1688] [01:01:31.12] about what feels right for me. Um
[L1689] [01:01:36.04] I would say that, you know, the great
[L1690] [01:01:37.88] people I work with, you know, from sort
[L1691] [01:01:40.64] of 90/10 on that scale up to about 50/50
[L1692] [01:01:43.92] on that scale. I think, you know,
[L1693] [01:01:45.48] outside of those, you know, folks tend
[L1694] [01:01:47.64] to
[L1695] [01:01:48.76] um
[L1696] [01:01:50.00] you know, tend to get into trouble
[L1697] [01:01:52.16] um as practitioners, right? Like, you
[L1698] [01:01:54.16] know, there people whose job it is to
[L1699] [01:01:55.60] be, you know, communicators and and
[L1700] [01:01:57.44] that's great as long as they have the
[L1701] [01:01:58.68] curiosity and and are clear about what
[L1702] [01:02:00.88] they, you know, know and and and don't
[L1703] [01:02:02.68] know. Um
[L1704] [01:02:04.92] But you know, I found that sweet spot at
[L1705] [01:02:06.96] that sort of 75/25 point in in in my
[L1706] [01:02:10.36] career and and that's what's what's
[L1707] [01:02:12.44] worked for me. I think
[L1708] [01:02:15.12] um
[L1709] [01:02:16.32] And I I I think in this moment where
[L1710] [01:02:20.08] things are changing so fast, there's so
[L1711] [01:02:21.56] much to learn,
[L1712] [01:02:23.12] um you know, swinging a little bit more
[L1713] [01:02:25.28] towards the practitioner side, I think
[L1714] [01:02:27.08] generally will help people. But again,
[L1715] [01:02:29.36] you don't want to go too far that way
[L1716] [01:02:30.64] because then you lose the
[L1717] [01:02:32.52] um you know, what's important for you
[L1718] [01:02:34.92] that comes with interacting with the
[L1719] [01:02:36.40] outside world. On the doing versus
[L1720] [01:02:38.56] discussing axis, I I kind of view the
[L1721] [01:02:41.60] doing one as if you were too far, you
[L1722] [01:02:44.12] would be underrated. And if you were too
[L1723] [01:02:47.68] far at the discussing, you would be
[L1724] [01:02:50.08] overrated. Mhm. And
[L1725] [01:02:52.80] if for someone who's structuring their
[L1726] [01:02:54.84] career,
[L1727] [01:02:56.12] uh would you say it's better to be
[L1728] [01:02:58.16] overrated or underrated?
[L1729] [01:03:01.24] I think long-term, you know, if if
[L1730] [01:03:03.20] you're if you're using that terminology,
[L1731] [01:03:04.96] it's probably better to be underrated. I
[L1732] [01:03:07.08] think
[L1733] [01:03:08.16] you know, being
[L1734] [01:03:09.68] being overrated can feel great
[L1735] [01:03:12.12] in the moment, um but is rarely
[L1736] [01:03:14.76] sustainable.
[L1737] [01:03:16.40] Uh and and and really sort of gets you
[L1738] [01:03:19.16] where
[L1739] [01:03:20.72] to where you you you you need to be. I
[L1740] [01:03:23.16] really enjoy, you know,
[L1741] [01:03:25.52] uh,
[L1742] [01:03:27.04] you know, things like sports and and
[L1743] [01:03:28.80] and, you know, these sort of creative
[L1744] [01:03:30.36] hobbies and and, uh, you know, crafts
[L1745] [01:03:33.00] because it it it does,
[L1746] [01:03:35.20] you know, turn that, um,
[L1747] [01:03:37.60] let's say perception and reality
[L1748] [01:03:40.24] knob to to very much reality, right?
[L1749] [01:03:43.12] Like as a as a as a sports person, you
[L1750] [01:03:45.36] can't you can't fool the world for very
[L1751] [01:03:47.24] long. Uh, it it it very quickly becomes,
[L1752] [01:03:50.52] uh, you know, very obvious, you know,
[L1753] [01:03:51.96] who who can and who can't. Uh,
[L1754] [01:03:54.36] you know, I think as a as a crafts
[L1755] [01:03:55.84] person, the same, right? It it very
[L1756] [01:03:57.84] quickly becomes,
[L1757] [01:03:59.52] um,
[L1758] [01:04:00.20] obvious [clears throat] who who can and
[L1759] [01:04:01.32] who can't. And I think it takes a little
[L1760] [01:04:03.20] bit longer in a field like ours where
[L1761] [01:04:05.04] there always is so much kind of
[L1762] [01:04:06.84] qualitative stuff that goes on.
[L1763] [01:04:09.16] Um, but I think long-term when I look
[L1764] [01:04:11.12] at, you know, careers that I really
[L1765] [01:04:12.88] admire and people I really admire, uh,
[L1766] [01:04:15.80] they tend to be people who are
[L1767] [01:04:17.64] personally very honest about their level
[L1768] [01:04:20.68] of of knowledge and understanding and
[L1769] [01:04:22.36] skill.
[L1770] [01:04:23.64] So, people who walk the walk, not
[L1771] [01:04:26.44] necessarily talk the talk. I see. Yeah,
[L1772] [01:04:28.92] about engineers that you admire, I'd be
[L1773] [01:04:30.76] curious cuz you have worked at AWS and
[L1774] [01:04:33.76] for such a long time and you have seen
[L1775] [01:04:36.84] so many legendary engineers.
[L1776] [01:04:39.36] Who at AWS do you look up to and and
[L1777] [01:04:41.88] why?
[L1778] [01:04:43.56] Yeah, I mean, you know, just fantastic.
[L1779] [01:04:46.16] One of the blessings of working at a
[L1780] [01:04:47.40] place like AWS is I get to work with so
[L1781] [01:04:49.12] many great people. Um,
[L1782] [01:04:50.96] you know, maybe because he's retired,
[L1783] [01:04:53.20] I'll I'll I'll talk a little bit about
[L1784] [01:04:55.04] Al Vermeulen. Uh, was was one of the
[L1785] [01:04:57.08] sort of early engineers at AWS and,
[L1786] [01:04:59.68] um,
[L1787] [01:05:00.96] original,
[L1788] [01:05:02.64] say, huge contributor to the design of
[L1789] [01:05:05.08] S3, a really big contributor to the
[L1790] [01:05:07.20] design of a lot of a lot of our database
[L1791] [01:05:09.20] services over time.
[L1792] [01:05:11.20] Um, Al was actually the the CTO of
[L1793] [01:05:14.12] Amazon for a for a period of time when
[L1794] [01:05:16.12] he realized, I think,
[L1795] [01:05:17.80] that wasn't the job he wanted to do. Um,
[L1796] [01:05:20.96] but I, you know, what I really admired
[L1797] [01:05:24.08] about uh about Al from early in my
[L1798] [01:05:26.60] career is,
[L1799] [01:05:29.24] you know, very clearly he was somebody
[L1800] [01:05:31.76] who deeply understood the things he was
[L1801] [01:05:33.64] he was doing. And he could work in these
[L1802] [01:05:36.28] two modes, right? Like, you know, I I
[L1803] [01:05:38.64] have a great um memory of a sort of
[L1804] [01:05:42.68] 2010-ish, uh
[L1805] [01:05:44.64] you know, arguing with Al about some of
[L1806] [01:05:46.44] the edge cases in in the the Paxos
[L1807] [01:05:49.20] paper. And, you know, he was super deep
[L1808] [01:05:51.68] at that level, but could also get up to
[L1809] [01:05:53.44] the the really kind of executive level
[L1810] [01:05:55.44] and talk about, you know, cloud strategy
[L1811] [01:05:57.88] and the way we should be explaining
[L1812] [01:05:59.44] things to people and some of the, you
[L1813] [01:06:00.96] know, sort of fundamental things that we
[L1814] [01:06:02.68] need to be building.
[L1815] [01:06:04.12] Um,
[L1816] [01:06:05.44] and I really admired that ability to
[L1817] [01:06:07.40] work sort of almost at at at every
[L1818] [01:06:09.92] level. And I was like, "Wow, you know,
[L1819] [01:06:11.20] this is this is something I aspire to."
[L1820] [01:06:13.88] Um, and uh you know, want to model my
[L1821] [01:06:16.96] want to model my own career after.
[L1822] [01:06:19.88] Um,
[L1823] [01:06:21.92] and so, you know, that's I I think that
[L1824] [01:06:23.68] is uh you know, the kind of person I've
[L1825] [01:06:26.24] really, you know, really enjoyed working
[L1826] [01:06:29.00] with is is people who do have that, you
[L1827] [01:06:31.60] know, do have that breadth. Um,
[L1828] [01:06:34.32] and I think, you know, one of the other
[L1829] [01:06:35.64] things that is you know, really
[L1830] [01:06:39.04] admirable about a lot of these folks is,
[L1831] [01:06:41.76] you know, they
[L1832] [01:06:43.32] they don't want to be celebrities,
[L1833] [01:06:44.56] right? They they they want to do cool
[L1834] [01:06:46.12] work for, you know, have an impact, do
[L1835] [01:06:48.08] great stuff for customers, you know,
[L1836] [01:06:50.12] optimize for having impact. You know,
[L1837] [01:06:52.36] for people who want to continue their
[L1838] [01:06:54.28] engineering education and really remain
[L1839] [01:06:57.32] on top of things, deeply understand the
[L1840] [01:06:59.64] technology, do you have any top
[L1841] [01:07:02.28] technical book recommendations? You
[L1842] [01:07:04.36] know, anybody who's building distributed
[L1843] [01:07:06.48] system things, I I I highly recommend uh
[L1844] [01:07:10.28] Martin Kleppmann's book.
[L1845] [01:07:12.92] I think there's a second edition of that
[L1846] [01:07:14.68] coming out, you know, soon. Um
[L1847] [01:07:18.12] there's a new edition of quantitative
[L1848] [01:07:20.24] systems design book, which I also think
[L1849] [01:07:22.12] is is is great. Sorry, Hennessy and
[L1850] [01:07:24.24] Patterson's computer architecture book.
[L1851] [01:07:26.64] This this is a super super useful one
[L1852] [01:07:29.24] that covers a
[L1853] [01:07:30.52] ton of ground. I read a ton of you know,
[L1854] [01:07:33.56] fiction and and non-fiction and and
[L1855] [01:07:35.64] mostly papers when I'm reading technical
[L1856] [01:07:37.48] things I find you know, I find engaging
[L1857] [01:07:39.56] at that level you know, more more useful
[L1858] [01:07:41.96] for me.
[L1859] [01:07:43.36] And by the way, that's that's become way
[L1860] [01:07:45.20] more accessible now. You know, one of
[L1861] [01:07:47.68] the great ways to dive into a paper is
[L1862] [01:07:50.36] you know, hey
[L1863] [01:07:51.88] you know, hey Claude summarize this for
[L1864] [01:07:53.92] me and then then I can dive into it and
[L1865] [01:07:56.44] and and read you know, the author's
[L1866] [01:07:57.88] words and I I find that mode is great
[L1867] [01:08:00.40] and and this is super accessible for
[L1868] [01:08:02.04] people who haven't been able to read
[L1869] [01:08:04.12] papers in in the past. Um
[L1870] [01:08:08.92] but uh
[L1871] [01:08:11.48] you know, and then there's also a ton of
[L1872] [01:08:12.96] insight in in some really old stuff too.
[L1873] [01:08:16.20] Uh
[L1874] [01:08:16.80] for example
[L1875] [01:08:18.52] um
[L1876] [01:08:19.64] you know, some of the
[L1877] [01:08:22.28] algorithms that we used in in in Lambda
[L1878] [01:08:25.52] to to manage traffic and and manage
[L1879] [01:08:27.68] bursts of traffic come from Erlang's
[L1880] [01:08:29.96] work like a hundred years ago on on
[L1881] [01:08:32.00] managing telephone call centers
[L1882] [01:08:34.44] and and his book about that and um
[L1883] [01:08:38.16] and so you know, folks also shouldn't
[L1884] [01:08:40.04] think that oh well, the industry is
[L1885] [01:08:41.44] changing super fast and so I should only
[L1886] [01:08:43.20] read recent things like there's still
[L1887] [01:08:45.56] incredible insights in some of the you
[L1888] [01:08:48.08] know, older work
[L1889] [01:08:49.88] and in the foundations of
[L1890] [01:08:52.92] computing and infrastructure and and and
[L1891] [01:08:55.32] networking and and computer science that
[L1892] [01:08:57.48] there is um
[L1893] [01:08:59.08] you know, more again more maybe more
[L1894] [01:09:01.96] leverage than ever before you know
[L1895] [01:09:03.72] deeply understanding those topics.
[L1896] [01:09:06.16] And then last question for you is if you
[L1897] [01:09:08.56] could go back to your younger self when
[L1898] [01:09:11.56] you just joined AWS and give yourself
[L1899] [01:09:14.36] some advice what would you say?
[L1900] [01:09:16.36] I think maybe I'd be a little bit
[L1901] [01:09:17.44] bolder. I really loved the team that I
[L1902] [01:09:19.20] worked with and and you know
[L1903] [01:09:21.92] you know especially in EC2 and and in
[L1904] [01:09:23.76] the early days in EBS and I think I was
[L1905] [01:09:26.48] a little bit more hesitant than was
[L1906] [01:09:28.04] optimal about leaving those teams and
[L1907] [01:09:30.20] and looking for the next thing
[L1908] [01:09:32.16] um you know as
[L1909] [01:09:34.36] um
[L1910] [01:09:35.72] you know my
[L1911] [01:09:37.92] own learning and impact kind of you know
[L1912] [01:09:40.32] tapered off a little bit in in in those
[L1913] [01:09:42.80] those places and so
[L1914] [01:09:44.64] you know I think I've changed
[L1915] [01:09:46.04] organizations kind of
[L1916] [01:09:48.56] in a big way four times in my career and
[L1917] [01:09:51.08] maybe five or six would have been
[L1918] [01:09:52.68] optimal not a lot more but but some more
[L1919] [01:09:55.60] uh and so you know don't don't hesitate
[L1920] [01:09:58.44] uh to
[L1921] [01:09:59.84] think about you know what am I learning
[L1922] [01:10:02.20] and who am I learning from and is there
[L1923] [01:10:04.08] a better environment to to to do that
[L1924] [01:10:06.60] you know more quickly and
[L1925] [01:10:08.44] uh and and to learn more things and you
[L1926] [01:10:10.64] know I'm highly personally highly
[L1927] [01:10:12.00] motivated by being able to follow my
[L1928] [01:10:14.48] curiosity and every time I've done that
[L1929] [01:10:17.04] in my career I found that a
[L1930] [01:10:20.08] valuable move
[L1931] [01:10:22.12] uh and uh and something that I've you
[L1932] [01:10:24.60] know personally enjoyed. Awesome. Okay,
[L1933] [01:10:28.24] well thank you so much for your time I I
[L1934] [01:10:30.60] really appreciate it Mark uh thank you
[L1935] [01:10:32.64] for sharing with uh the audience. This
[L1936] [01:10:34.88] has been super fun. Thanks so much.
[L1937] [01:10:37.68] Thank you for listening to the podcast.
[L1938] [01:10:39.32] It's a passion project of mine that I've
[L1939] [01:10:41.48] really enjoyed building. Another passion
[L1940] [01:10:43.56] project that I've been working on kind
[L1941] [01:10:44.96] of in secret is building an ergonomic
[L1942] [01:10:47.44] keyboard that I wish existed and I
[L1943] [01:10:49.68] finally have a prototype so I'd love to
[L1944] [01:10:51.44] show you what we've built. It's ultra
[L1945] [01:10:54.20] low profile and ergonomic and I couldn't
[L1946] [01:10:56.96] find anything like it on the market, so
[L1947] [01:10:58.64] that's why we built it. I'll put a link
[L1948] [01:11:00.48] to the keyboard in the description. You
[L1949] [01:11:02.04] can take a look and learn more about the
[L1950] [01:11:03.56] project there. We could definitely use
[L1951] [01:11:05.32] your support. Also, if you have any
[L1952] [01:11:07.32] feedback for me about the show, I'd love
[L1953] [01:11:09.32] to hear it. Comments on YouTube have led
[L1954] [01:11:11.80] to guests coming on like Ilya Grigoric
[L1955] [01:11:14.52] and David Fowler. I wasn't aware of them
[L1956] [01:11:16.76] until someone dropped a comment. Also,
[L1957] [01:11:18.92] feedback in the comments helped me learn
[L1958] [01:11:20.48] to reduce the number of cliffhangers in
[L1959] [01:11:22.88] the intros. So, your comments definitely
[L1960] [01:11:24.84] make a difference. Please keep letting
[L1961] [01:11:26.24] me know what you'd like to see more of
[L1962] [01:11:27.88] in the show, and I'll see you in the
[L1963] [01:11:29.24] next episode.
