Chunk 1; segments 1–387. 

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
