# Creator of uv, ty, Ruff: How Software Engineering Is Changing | Charlie Marsh

Source ID: source-e744e4ed615158a6
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_uv,_ty,_Ruff_How_Software_Engineering_Is_Changing_Charlie_Marsh_en.txt
Video: https://www.youtube.com/watch?v=Iw65FD4MGgs

[L10] [00:00.08] It's such an interesting time to be
[L11] [00:01.36] building software because things are
[L12] [00:02.80] just changing like so fast.
[L13] [00:04.88] >> This is Charlie Marsh, founder of
[L14] [00:06.72] Astral, the Python DevTools startup that
[L15] [00:08.96] was acquired by OpenAI. And I
[L16] [00:10.88] interviewed him about how software
[L17] [00:12.72] engineering is changing.
[L18] [00:14.16] >> Now it's like when you put up a PR, I
[L19] [00:16.00] actually have to review it really
[L20] [00:17.12] closely because you're not like writing
[L21] [00:19.20] it anymore. It's like the agent. The
[L22] [00:21.20] cost of putting up a plausible PR has
[L23] [00:22.96] gone to zero while the cost to like
[L24] [00:25.12] review has remained the same. if they're
[L25] [00:28.40] building so heavily with agents, like to
[L26] [00:30.24] what degree do they need to understand
[L27] [00:31.76] different parts of the code? I do think
[L28] [00:33.76] it would be like really hard to be an
[L29] [00:36.24] early career software engineer right
[L30] [00:37.76] now. Here's the full episode.
[L31] [00:44.56] What was the space like when you were
[L32] [00:46.72] first getting into building these these
[L33] [00:48.48] dev tools? Like why did you think it
[L34] [00:50.08] could be better? Before I started
[L35] [00:52.72] Astral, I was at a computational biology
[L36] [00:55.68] company and I was like the second
[L37] [00:57.20] engineer. I had no bio background and no
[L38] [00:59.92] like ML background and so I was building
[L39] [01:01.60] all the like software systems to like do
[L40] [01:04.32] machine learning. Um, and so that was
[L41] [01:06.56] like all Python. So I was like learning
[L42] [01:08.64] Python. Then we had some Go and some
[L43] [01:10.00] Rust. And so I just worked across lots
[L44] [01:11.84] of different ecosystems. And you know I
[L45] [01:14.96] think Python at the time like when I was
[L46] [01:17.28] in that position I we were trying to do
[L47] [01:20.88] a lot as a small team. So we had like a
[L48] [01:23.28] very I mean not compared to large code
[L49] [01:27.20] bases but we had a comparatively large
[L50] [01:28.80] code base and it was really a small
[L51] [01:30.48] group of us that were software engineers
[L52] [01:32.16] trying to serve the rest of the team
[L53] [01:33.76] whether they were like machine learning
[L54] [01:34.96] researchers or scientists. So I had kind
[L55] [01:37.36] of like worked across a bunch of
[L56] [01:38.72] different ecosystems, seen a lot of the
[L57] [01:40.16] tooling and now I was like working on
[L58] [01:42.00] Python and we kept trying to get lots of
[L59] [01:45.04] leverage out of the tools whether it was
[L60] [01:46.56] like the type checker or the llinter or
[L61] [01:48.32] the package manager like things were
[L62] [01:50.16] scaling up. We were a small team. We
[L63] [01:51.84] wanted to have like really good static
[L64] [01:53.20] analysis, really good tooling. Um and we
[L65] [01:56.40] kept running into like limitations
[L66] [01:57.92] around it. I mean, I think there were
[L67] [01:59.44] some I kind of like looked at the Python
[L68] [02:01.68] ecosystem and I just didn't see the same
[L69] [02:05.36] amount of like experimentation
[L70] [02:07.92] that I saw in other ecosystems like in
[L71] [02:10.16] the web ecosystem.
[L72] [02:12.16] Um, there were a lot of things going on
[L73] [02:14.40] that seemed pretty crazy. Um, and there
[L74] [02:16.72] was a very intense focus on perform I
[L75] [02:19.36] don't know about very intense, but there
[L76] [02:20.56] was more of a focus on performance. Um,
[L77] [02:23.28] and that started with like ESB build and
[L78] [02:25.76] then which was in Go and then you had
[L79] [02:27.76] like SWC and Rust and then you know bun
[L80] [02:30.56] and and Dino and all these other tools
[L81] [02:32.96] that came around and this idea that you
[L82] [02:35.60] could have to native tooling for
[L83] [02:38.40] JavaScript was like became very accepted
[L84] [02:41.60] um especially as applications became
[L85] [02:43.28] bigger and people were doing like more
[L86] [02:44.72] and more stuff on their machine um and
[L87] [02:47.36] that wasn't really happening in Python.
[L88] [02:49.20] And so that to me was kind of like the
[L89] [02:51.92] um the key question was like why can't
[L90] [02:54.00] we have that? Um because I was seeing
[L91] [02:56.32] all the stuff that was happening in web
[L92] [02:58.72] um and I had I had done some rust I'd
[L93] [03:01.36] done some Go. I'd like seen these
[L94] [03:02.88] different tool chains and like how they
[L95] [03:04.32] work what the experience is like the
[L96] [03:05.76] user experience right mostly in those
[L97] [03:07.52] cases. Um and then I saw Python and it
[L98] [03:10.16] was like we had a smaller set of tools.
[L99] [03:13.04] Um there were lots of interesting ideas
[L100] [03:15.20] from other ecosystems that I didn't see
[L101] [03:16.72] like represented. Um and uh they were
[L102] [03:20.24] really all written in Python. And so
[L103] [03:22.40] that to me was kind of like the
[L104] [03:23.68] interesting question. Um, and it was the
[L105] [03:25.28] first
[L106] [03:27.52] uh it was sort of like the first thing I
[L107] [03:29.68] uh I I asked when I started working on
[L108] [03:31.84] this like when I released rough
[L109] [03:34.40] um the title of the blog post was
[L110] [03:36.32] something like Python tooling could be
[L111] [03:37.68] like much much faster and and for me it
[L112] [03:40.24] was really like this is a hypothesis
[L113] [03:42.16] like could Python tooling be much faster
[L114] [03:44.16] and then I built a prototype and then
[L115] [03:46.16] that prototype was like yes I think it
[L116] [03:48.08] could be. you wrote a post kind of like
[L117] [03:50.96] exploring My Pi or publishing your
[L118] [03:53.68] results using My Pi and the date on that
[L119] [03:57.44] like nine days later you you published
[L120] [04:00.00] the post that one that you mentioned
[L121] [04:01.60] like it could be so much faster or
[L122] [04:03.36] >> No, that's funny. I didn't even realize
[L123] [04:04.96] that. Yeah. That those were so close
[L124] [04:06.40] together.
[L125] [04:07.04] >> Did you build that that proof of concept
[L126] [04:09.12] in those nine days? Yeah, I wrote that I
[L127] [04:11.12] wrote that blog post about basically
[L128] [04:12.24] type checking at scale because I was
[L129] [04:14.24] trying to think of what are things that
[L130] [04:15.44] I learned that people haven't written
[L131] [04:17.44] much about and then I started with a l
[L132] [04:20.48] building a llinter because I thought it
[L133] [04:23.04] would be much easier. I I think it
[L134] [04:24.48] actually is a lot easier than building a
[L135] [04:26.88] type checker. We're now building a type
[L136] [04:28.56] checker and we have a type we have a
[L137] [04:30.08] type checker. Um and so I can I can say
[L138] [04:32.56] that I think building a type checker is
[L139] [04:34.16] much harder. Um, but I started with a
[L140] [04:36.16] llinter because I thought it would let
[L141] [04:37.28] me like prove a lot of the same ideas
[L142] [04:39.68] but in a smaller form factor like
[L143] [04:42.56] building a startup or or just building
[L144] [04:45.84] like a tool. You want to try to like get
[L145] [04:49.92] something into people's hands that they
[L146] [04:51.44] can actually use and that actually
[L147] [04:52.64] proves out value like as quickly as
[L148] [04:54.24] possible and also that lets you iterate
[L149] [04:56.96] very quickly. And a llinter weirdly
[L150] [04:59.60] ended up being like kind of the perfect
[L151] [05:02.08] form factor for it because it it has
[L152] [05:05.36] like a pretty simple core, but it's you
[L153] [05:08.72] know then you have like tons and tons of
[L154] [05:10.08] rules, right? And so it's like
[L155] [05:11.76] extensible in a lot of different ways,
[L156] [05:13.60] but people can get value very quickly
[L157] [05:16.00] from a small core plus like some number
[L158] [05:18.88] of rules. And so we were able to like
[L159] [05:20.80] get something out there and then like
[L160] [05:22.56] iterate and like ship like more rules
[L161] [05:24.16] and more functionality and people could
[L162] [05:25.76] like use it alongside other tools. Like
[L163] [05:27.92] it was useful immediately which I think
[L164] [05:29.92] is extremely helpful as opposed to
[L165] [05:32.96] something like um I mean actually the
[L166] [05:35.28] type checker would be a good example
[L167] [05:36.96] like a type checker that's like 75% done
[L168] [05:40.72] like isn't very useful. Um, same with
[L169] [05:43.68] the package manager. Like these things
[L170] [05:45.36] have to be I mean there are ways like I
[L171] [05:48.16] think I would challenge those as like
[L172] [05:49.44] blanket statements. But the point is
[L173] [05:51.20] it's harder to ship something uh
[L174] [05:53.60] iteratively that's like still useful to
[L175] [05:55.52] users. Um, and I think that's like uh
[L176] [05:58.08] one of the key properties and actually
[L177] [05:59.68] like building momentum uh as like a tool
[L178] [06:03.04] or something else.
[L179] [06:04.24] >> When you posted that writing, what was
[L180] [06:06.72] the reception? I mean the the blog post
[L181] [06:09.12] itself like I published it and then it
[L182] [06:11.92] was on Hacker News and it got tweeted
[L183] [06:13.92] about a lot and it just created some um
[L184] [06:17.60] you know some amount of uh excitement
[L185] [06:20.56] and interest around it and those things
[L186] [06:23.44] um I mean especially being on the front
[L187] [06:25.68] page of hacker news I have a lot of
[L188] [06:27.12] thoughts about I mean it's certainly not
[L189] [06:30.08] uh it's like some percent luck um and
[L190] [06:33.44] then some percent skill and uh it is
[L191] [06:38.16] like a helpful thing but not a requisite
[L192] [06:41.12] to success. Um, and it also doesn't like
[L193] [06:44.24] guarantee success just because you got
[L194] [06:45.92] something on the front page of Hacker
[L195] [06:47.36] News. Um, like it's great. It's great if
[L196] [06:49.60] you can, but um, there's a lot of
[L197] [06:51.28] randomness to it. Um, I do think though
[L198] [06:54.56] that
[L199] [06:56.40] uh, well maybe a couple things. So one
[L200] [07:00.48] after that happened like some people
[L201] [07:03.28] started pay actually paying attention to
[L202] [07:04.64] the project and so um I really tried to
[L203] [07:07.44] like capitalize on that um by basically
[L204] [07:10.40] by being like very engaged and so when
[L205] [07:12.88] people would file issues I would like
[L206] [07:14.48] aggressively try to like acknowledge the
[L207] [07:17.12] issue as quickly as possible fix it and
[L208] [07:18.88] ship a release like if you can do that
[L209] [07:20.80] like within one day it's like a very
[L210] [07:22.48] very powerful loop like you gain
[L211] [07:25.20] supporters and like create more momentum
[L212] [07:26.88] around the
[L213] [07:28.00] Um, and there were also a couple like
[L214] [07:29.52] high-profile people in the ecosystem
[L215] [07:31.20] that started paying attention to the
[L216] [07:33.36] project like Sebastian Ramirez who did
[L217] [07:35.20] fast uh does fast API and you know a
[L218] [07:37.68] bunch of other things. Um, and he's been
[L219] [07:39.68] a great supporter of our projects too.
[L220] [07:41.28] But like early on he was like oh this is
[L221] [07:42.96] interesting. I'd like to use it and I
[L222] [07:44.48] was like I basically asked myself well
[L223] [07:46.80] what would it take for him to use it?
[L224] [07:47.92] And then I just like tried to do all
[L225] [07:49.20] those things. Um, so I tried to
[L226] [07:51.68] capitalize on that. Um I think the other
[L227] [07:55.20] is though um I do think a lot about like
[L228] [07:59.28] developer marketing and um
[L229] [08:04.00] it's sort of like a dirty word or like a
[L230] [08:06.08] dirty expression like I I think like I
[L231] [08:07.76] think a lot of engineers like want
[L232] [08:09.84] technical products and tools to just
[L233] [08:12.64] like win on their merits. Like the best
[L234] [08:14.40] technical solution should just be the
[L235] [08:16.00] one that like wins and grows. But um I
[L236] [08:19.92] actually I I mean I have this sort of
[L237] [08:21.52] like stupid hypothesis that there's all
[L238] [08:23.84] these like there's like thousands of
[L239] [08:25.60] like really amazing projects on GitHub
[L240] [08:27.60] that like basically don't know how to
[L241] [08:29.28] market themselves and so never like
[L242] [08:31.04] never get discovered and never go
[L243] [08:32.40] anywhere. Um, and I don't actually know
[L244] [08:34.56] if that's true, but it's like sort of
[L245] [08:35.84] how I feel about a lot of technical work
[L246] [08:38.48] where it's like it's actually worth
[L247] [08:41.04] looking at a project like Rough.
[L248] [08:44.32] And um, when I think about like what to
[L249] [08:47.04] put in the blog post or this extends to
[L250] [08:49.76] like what to put in the read me or like
[L251] [08:51.76] what to put in the you don't need like a
[L252] [08:53.60] million emojis and like and like a
[L253] [08:56.16] million screenshots of like everything.
[L254] [08:57.92] What you need is like, okay, someone's
[L255] [09:00.64] going to like like land on this page and
[L256] [09:04.24] I have like 10 seconds to get them
[L257] [09:07.60] interested in what I'm doing and help
[L258] [09:09.04] them understand like why it might matter
[L259] [09:10.64] to them and like why it's useful. And so
[L260] [09:12.56] like that was like that's like the key
[L261] [09:14.24] idea that I try to bring basically to
[L262] [09:17.12] everything. I mean it's a little bit
[L263] [09:18.56] depressing because it's like okay I only
[L264] [09:19.92] have like 10 but like people people
[L265] [09:21.28] really don't have like like this is like
[L266] [09:23.12] the attention economy, right? It's like
[L267] [09:25.76] um it's same thing with a blog post like
[L268] [09:28.40] um ironically I used to look at a lot of
[L269] [09:31.04] the OpenAI blog posts when I was at
[L270] [09:34.32] Spring and we were trying to we were
[L271] [09:36.16] doing like machine learning in bio and
[L272] [09:38.32] we were trying to publish material to
[L273] [09:40.56] like explain what we do but but we had
[L274] [09:42.96] all these interesting insights like we
[L275] [09:44.80] looked at the OpenAI blog posts
[L276] [09:46.16] especially like the Dolly ones like the
[L277] [09:47.60] older ones and we were all we were like
[L278] [09:49.84] wow that's an amazing blog post because
[L279] [09:52.00] if you read none of the text, you still
[L280] [09:55.36] understand what they did and you're
[L281] [09:56.96] still impressed by it. Like if someone
[L282] [09:58.48] just goes on the page, they leave with
[L283] [10:00.96] an impression and they have some
[L284] [10:02.56] understanding. And I was like, "Wow,
[L285] [10:03.76] that's like a really amazing thing." And
[L286] [10:05.20] so when I write blog posts now, I'm
[L287] [10:08.08] like, if someone just lands on this
[L288] [10:09.52] page, I have to be prepared for the for
[L289] [10:12.08] the large number of people who will only
[L290] [10:14.00] read maybe the TLDDR, maybe look at the
[L291] [10:16.08] first image, maybe read the headline.
[L292] [10:18.40] Some people will read the full thing.
[L293] [10:19.84] And so I should care painstakingly about
[L294] [10:22.16] every word and everything it says, but
[L295] [10:24.24] most people will read like almost none
[L296] [10:25.76] of it. And so again, sorry it's a little
[L297] [10:27.92] bit like it's a little bit depressing,
[L298] [10:29.12] but like I do think it's worth thinking
[L299] [10:31.20] about your audience and like how do you
[L300] [10:33.84] how do you explain to them like why they
[L301] [10:35.44] should care about what you're doing in a
[L302] [10:36.96] way that's honest and genuine like not
[L303] [10:38.96] like not like deceptive. Um but you do
[L304] [10:41.36] have to think hard about um how do you
[L305] [10:44.56] communicate like why something matters
[L306] [10:45.92] to people very quickly. Could you give
[L307] [10:48.40] an example of like what you did in your
[L308] [10:51.20] case?
[L309] [10:51.84] >> I think like for rough specifically, we
[L310] [10:53.84] had a really good graph uh of the
[L311] [10:57.28] benchmarks
[L312] [10:58.80] >> um that we put in the blog post and that
[L313] [11:01.12] like went it was like on Twitter and
[L314] [11:03.52] like that that was like a priceless
[L315] [11:05.20] graph basically. Um sorry, not in terms
[L316] [11:08.32] of like monetary value. I just mean in
[L317] [11:09.68] terms of like attention, right? It was
[L318] [11:11.28] like oh that's like that's like really
[L319] [11:13.20] obvious like what's happening there. I
[L320] [11:14.56] think graphs of benchmarks can be uh
[L321] [11:16.72] like a really powerful thing. Um all
[L322] [11:19.92] benchmarks are bad and wrong in some way
[L323] [11:22.32] and so there's a lot like there's a lot
[L324] [11:24.48] more to like say about that like but um
[L325] [11:26.96] but I do think like having a visual hook
[L326] [11:29.28] that explains to people why they should
[L327] [11:30.80] care and like what something is. um and
[L328] [11:33.28] having a really strong tagline like I
[L329] [11:36.40] would have to look back at what we had
[L330] [11:37.84] but we were like okay we're going to be
[L331] [11:39.76] like compatible with your existing stuff
[L332] [11:42.80] and much faster and uh that's kind of it
[L333] [11:47.12] and it's like okay well if it's
[L334] [11:48.80] compatible and it's much faster like
[L335] [11:50.08] that was like I was like why should you
[L336] [11:51.52] care like it can be orders of magnitude
[L337] [11:53.44] faster and it'll give you the same
[L338] [11:54.88] experience you try to convey that like
[L339] [11:57.12] as quickly as possible
[L340] [11:58.64] >> right and even the I mean that blog post
[L341] [12:01.76] header I mean, Python tooling should
[L342] [12:04.40] could be much faster. Should be much
[L343] [12:06.00] >> foc
[L344] [12:08.32] provocative, I guess. Yeah.
[L345] [12:10.96] >> I mean, I'm pretty against like uh
[L346] [12:13.52] clickbait or like trying to be
[L347] [12:15.12] misleading in like anything that we do.
[L348] [12:17.28] Like we we you basically want to want to
[L349] [12:20.80] balance like
[L350] [12:23.04] creating like effective like effectively
[L351] [12:26.16] communicating like the most interesting
[L352] [12:28.00] pieces to people. Um, but you have to do
[L353] [12:30.72] it in a way that like you believe is
[L354] [12:32.32] like true and authentic. Um, like you
[L355] [12:35.04] could lie about a bunch of stuff and
[L356] [12:36.24] like post interesting things that are
[L357] [12:37.52] like clearly provocative, but like I
[L358] [12:39.52] don't know. To me that's just like why
[L359] [12:41.04] why would I ever do that? That's like
[L360] [12:42.32] such a losing battle.
[L361] [12:44.00] >> What What do you think about I mean so
[L362] [12:46.00] you have that graph and
[L363] [12:47.92] >> I'm I don't know if the I see this a lot
[L364] [12:50.56] though where the axis is not zeroed.
[L365] [12:53.20] >> Oh yeah.
[L366] [12:53.60] >> So it's you know it's it's all within
[L367] [12:55.20] the range of like 50 to
[L368] [12:56.96] >> chart crimes. Yeah. Chart crime. Yeah. I
[L369] [12:59.20] wouldn't do that. Yeah. Yeah. I do think
[L370] [13:01.84] like benchmarks are pretty um
[L371] [13:04.80] complicated and controversial though.
[L372] [13:06.48] And um maybe most people don't even see
[L373] [13:09.52] this controversy, but like I do because
[L374] [13:11.36] it's like it's just very like
[L375] [13:14.40] performance is very nuanced. Um and
[L376] [13:20.16] uh you know like like an you know you
[L377] [13:24.16] have to think about like okay uh with
[L378] [13:26.88] caching or without caching um those are
[L379] [13:29.20] like pretty different or like uh
[L380] [13:31.76] depending on the project that you're
[L381] [13:33.12] running on uh the performance
[L382] [13:35.20] characteristics will be like totally
[L383] [13:36.72] different and like we see this like in
[L384] [13:38.40] UV this is really hard because like
[L385] [13:40.72] sometimes um you know UV is really fast
[L386] [13:43.60] but sometimes your package install is
[L387] [13:45.44] actually bottlenecked on um like a C++
[L388] [13:49.28] build that's like totally out of band
[L389] [13:51.12] and it's like okay well so how do you
[L390] [13:53.20] like accur it's like I mean it's sort of
[L391] [13:54.80] impossible to like accurately capture
[L392] [13:56.64] like all of the different scenarios um
[L393] [14:00.72] and so but it's also like a disservice
[L394] [14:02.80] to users like not to try to communicate
[L395] [14:05.84] to them
[L396] [14:07.52] like the importance or like a real
[L397] [14:09.84] representation of like what will the
[L398] [14:12.32] difference in performance look like and
[L399] [14:13.52] why does it matter and so you have to
[L400] [14:15.20] balance those things. Um, which I think
[L401] [14:17.20] is actually quite hard. Um, and a lot of
[L402] [14:19.68] people tend to get it wrong. Um, and
[L403] [14:21.52] maybe we've gotten it wrong a few times,
[L404] [14:22.88] too. I'm like I'm happy to accept that.
[L405] [14:24.72] Um, but I do think it's it's more
[L406] [14:26.24] complicated than people think. Um, but
[L407] [14:29.76] it's also I think a huge disservice not
[L408] [14:31.52] to include like some way to try to
[L409] [14:33.12] convey to people quickly like what
[L410] [14:34.40] things feel like.
[L411] [14:35.84] >> I think one of the things I'm most
[L412] [14:37.20] interested in is like you you mentioned
[L413] [14:39.68] that graph. I see that graph and like
[L414] [14:41.92] you know the engineer in me is like how
[L415] [14:43.68] how did you make it so much faster and
[L416] [14:46.32] one of the things in the tagline is
[L417] [14:48.56] Python dev tooling written in rust and
[L418] [14:51.04] so I guess one of the first thing I'm
[L419] [14:52.56] curious about is why did you choose rust
[L420] [14:55.28] and what are the pros and cons of that
[L421] [14:57.68] >> I would say I largely chose chose rust
[L422] [14:59.92] for that project because of hype um like
[L423] [15:04.96] I don't think at the time I was that
[L424] [15:06.48] informed about a lot of the technical
[L425] [15:09.20] trade-offs between those different
[L426] [15:10.72] ecosystems. Um, and I hadn't really done
[L427] [15:13.76] a lot of systems programming. And so
[L428] [15:15.20] that's that's like the honest answer is
[L429] [15:17.04] like I was seeing it in a lot of places
[L430] [15:18.56] and it was growing a lot and people said
[L431] [15:21.12] it was like it appeared to be sort of
[L432] [15:22.80] like an accessible way to write my
[L433] [15:24.80] impression was that it was an accessible
[L434] [15:26.96] way to write uh high performance
[L435] [15:29.20] software. Um, and and so I started for
[L436] [15:32.40] that reason. Um,
[L437] [15:34.64] in hindsight,
[L438] [15:37.04] uh, I think it was, uh, an amazing
[L439] [15:39.92] decision and I wouldn't absolutely not
[L440] [15:42.40] do it differently and I think it was
[L441] [15:43.76] like the best choice for what we're
[L442] [15:45.84] building. Um, and and now I have a lot
[L443] [15:49.12] more experience uh, writing Rust. it.
[L444] [15:51.44] But it is funny because like I I do sort
[L445] [15:54.80] of think that um if I had tried to write
[L446] [15:58.64] this in like C or C++, I think I
[L447] [16:00.40] probably would have given up because I
[L448] [16:01.92] find those even now I find those
[L449] [16:04.16] ecosystems
[L450] [16:05.76] much more like intimidating, hard to
[L451] [16:09.04] hard to access, hard to learn. I I have
[L452] [16:12.08] often felt that like one of the great or
[L453] [16:14.48] like underrated advantages of Rust is
[L454] [16:17.52] basically like the tooling. Um cuz like
[L455] [16:20.48] you drop in and you use cargo and that's
[L456] [16:23.68] how you do like everything. And uh if
[L457] [16:26.48] you clone, this isn't always true, but
[L458] [16:28.32] like you know there are exceptions as
[L459] [16:29.76] projects get sufficiently advanced, but
[L460] [16:31.68] like if there's like a crate out there
[L461] [16:34.40] um that we use and maybe I want to
[L462] [16:36.24] submit a PR to it, I'm like extremely
[L463] [16:39.04] confident that I can clone it and figure
[L464] [16:40.96] out how to run and build it without
[L465] [16:42.56] having to do like any work. like being
[L466] [16:44.72] able to just clone and run like cargo
[L467] [16:46.32] run or cargo build or cargo test. That's
[L468] [16:48.56] actually like really amazing. Um
[L469] [16:50.56] especially for someone like me who was
[L470] [16:51.84] like new to systems programming and I
[L471] [16:53.28] didn't want to have to figure out like
[L472] [16:54.88] my whole like C++ like tool chain and
[L473] [16:56.96] like build system like all this stuff. C
[L474] [16:59.60] Rust was like opinionated about all
[L475] [17:01.44] these things and so there were a lot of
[L476] [17:04.00] things that were hard to learn. Um, but
[L477] [17:07.44] uh but I was allowed to like basically I
[L478] [17:10.72] was allowed to spend my time focusing on
[L479] [17:12.16] the things that that like actually
[L480] [17:13.84] should be hard to learn as opposed to
[L481] [17:15.92] like all the other uh basically all the
[L482] [17:19.60] that like you don't want to
[L483] [17:21.04] spend time on like how do I get this
[L484] [17:23.20] thing to actually like build and run and
[L485] [17:24.56] blah blah blah. I think it has been an
[L486] [17:27.04] extremely good bet for us. um like it's
[L487] [17:30.48] scaled very well with the project and I
[L488] [17:33.92] I mean we at OpenAI too are like we use
[L489] [17:36.96] a lot of Rust and they're like betting
[L490] [17:38.40] heavily on Rust and then you know me as
[L491] [17:41.12] someone who builds software for uh
[L492] [17:43.36] builds developer tools like tries to
[L493] [17:44.96] build software for people to build
[L494] [17:46.24] software I'm like very bullish on Rust
[L495] [17:49.36] um uh like it's grown um enormously and
[L496] [17:53.04] I think it will actually just like keep
[L497] [17:54.72] growing enormously um at the same time
[L498] [17:57.76] like I said this at the start I've never
[L499] [17:59.36] been someone who's like super dogmatic
[L500] [18:01.20] about ecosystems. Like I I think that
[L501] [18:03.12] like all of those ecosystems have like
[L502] [18:05.12] lots of redeeming qualities. Like I
[L503] [18:06.56] think what's happening in Zigg is like
[L504] [18:07.92] very interesting and like I wish I had
[L505] [18:09.84] more time to like go deep on it and like
[L506] [18:12.40] develop more nuanced opinions about like
[L507] [18:14.08] what it does better. Like I'm sure it
[L508] [18:15.36] does a bunch of things better than Rust.
[L509] [18:16.72] Um and there I'm sure there are things
[L510] [18:18.00] for Rust to learn from that ecosystem.
[L511] [18:19.92] Um similarly people have a ton of
[L512] [18:21.44] success building stuff in Go. I think
[L513] [18:22.88] that's great too. I think like I think
[L514] [18:24.72] all this stuff is great. Um, but I have
[L515] [18:27.04] loved like using Rust and um, I have
[L516] [18:29.84] complaints about it, but I view those
[L517] [18:31.36] complaints as like things that we should
[L518] [18:34.40] improve. Um, especially as like the way
[L519] [18:37.04] we build software changes with with with
[L520] [18:39.12] LMS.
[L521] [18:40.08] >> So if sounds like you're saying C and
[L522] [18:42.64] C++
[L523] [18:44.48] today, you would not consider them
[L524] [18:46.88] because their tooling is insufficient.
[L525] [18:48.72] But Zigg, Rust, and Go are all, you
[L526] [18:53.68] know, some spectrum of tradeoffs or
[L527] [18:55.76] different things that
[L528] [18:56.64] >> Yeah. I mean, I think I think a lot of
[L529] [18:58.00] people would disagree with me, but like
[L530] [18:59.36] I don't really understand like why
[L531] [19:01.60] unless there are like very specific
[L532] [19:03.28] technical
[L533] [19:04.80] reasons um
[L534] [19:08.16] uh or you're working with existing
[L535] [19:10.00] software like basically I don't really
[L536] [19:11.60] know why I would start a net new project
[L537] [19:14.00] in C or C++. Um I I certainly would not
[L538] [19:18.88] like at a personal level. Um I guess if
[L539] [19:21.20] they're like the ecosystems you know
[L540] [19:22.88] really well like that's then it makes a
[L541] [19:24.96] lot of sense to do it. Um but if I was
[L542] [19:27.36] like a new a programmer like looking to
[L543] [19:29.84] learn systems or um if I knew those
[L544] [19:32.16] languages equally well like I guess I
[L545] [19:34.00] just don't understand like why I would
[L546] [19:35.76] do that which I'm sure I'll get like
[L547] [19:37.20] roasted for but I uh but I I just don't
[L548] [19:40.08] really care. Like I now I actually care
[L549] [19:42.16] about a lot of things that Rust gives me
[L550] [19:43.44] that I didn't care about as much before
[L551] [19:44.88] like memory safety. I don't think I even
[L552] [19:46.56] understood or cared about what memory
[L553] [19:47.68] safety was when I started working on
[L554] [19:48.72] Rough to be honest with you. And now I
[L555] [19:50.40] like I think it's like a pretty amazing
[L556] [19:52.00] thing. Um is like you know memory I want
[L557] [19:54.64] to build things that are like safe uh
[L558] [19:56.48] that don't crash on users that are
[L559] [19:58.24] really fast, really performant, um that
[L560] [20:00.72] don't have to make compromises
[L561] [20:02.48] basically. And like I feel like I can do
[L562] [20:03.92] that in Rust. And so for me it's like I
[L563] [20:06.56] don't know it's kind of like the perfect
[L564] [20:07.68] language. I mean it's not the perfect
[L565] [20:09.12] language but it is my favorite language
[L566] [20:10.72] to use right now.
[L567] [20:12.16] >> In today's world it's not unreasonable
[L568] [20:15.04] that you could almost completely
[L569] [20:18.80] transpile or convert your existing
[L570] [20:21.52] codebase into any language of your
[L571] [20:23.20] choice.
[L572] [20:24.00] >> Like I saw I think it was the on bun I
[L573] [20:27.52] forgot I think it was zigg to rust.
[L574] [20:29.36] >> Yes.
[L575] [20:29.92] >> Like all in one go. So like if you
[L576] [20:34.24] studied some other language and you
[L577] [20:36.32] thought it was better, you could totally
[L578] [20:38.64] rewrite everything from Rust into I
[L579] [20:41.28] don't know Zigg or Go, would you ever
[L580] [20:43.44] consider doing that for uh the dev tools
[L581] [20:46.24] that you've built for instance?
[L582] [20:47.60] >> Yeah, it's such an interesting time to
[L583] [20:49.28] be building software because things are
[L584] [20:50.96] changing. This is not a novel comment,
[L585] [20:53.60] but things are just changing like so
[L586] [20:55.36] fast. like I I didn't I didn't really
[L587] [20:58.40] program with agents at all until like
[L588] [21:00.32] Christmas, like December break basically
[L589] [21:03.44] of this year. Um and or of last year
[L590] [21:06.56] rather and like that's really not that
[L591] [21:08.00] long ago. Like I mean I was like using
[L592] [21:09.44] cursor and stuff but like I wasn't like
[L593] [21:11.92] now like I I haven't edited code in an
[L594] [21:14.80] editor in a very long time. Like I
[L595] [21:16.88] everything I do goes through codecs and
[L596] [21:19.36] like even if it's like small edits I'm
[L597] [21:21.44] just prompting and kind of like it's
[L598] [21:23.12] like it's it's completely different. Um,
[L599] [21:25.44] and that's not that long of a time,
[L600] [21:26.80] right? And so, uh, I don't know what's
[L601] [21:28.64] going to look like in six months. hard
[L602] [21:29.92] to say. But so that you know the reason
[L603] [21:31.84] that I mentioned that is
[L604] [21:34.40] like I think bun
[L605] [21:37.52] uh like doing that rewrite it's like I
[L606] [21:41.76] wouldn't do that right now but I'm
[L607] [21:44.72] actually like I'm glad that they are
[L608] [21:48.64] like pushing that they are experimenting
[L609] [21:51.36] and pushing the envelope of like what's
[L610] [21:53.04] possible and and they're doing it in the
[L611] [21:55.04] face of like a lot of criticism and um
[L612] [21:58.40] it will be interesting to how it plays
[L613] [22:00.00] out for users because I think a few
[L614] [22:02.08] different things I thought about is like
[L615] [22:03.44] oh reasons not to do that like one is
[L616] [22:07.20] okay uh maybe you don't understand the
[L617] [22:09.36] code anymore right like if the code got
[L618] [22:11.76] completely rewritten quote unquote then
[L619] [22:14.08] as a human like you may not understand
[L620] [22:15.92] any of the code anymore um and that can
[L621] [22:18.16] be a big problem um I I think there are
[L622] [22:21.20] mitigating factors around that which are
[L623] [22:23.44] like they tried to do a very direct
[L624] [22:24.96] transpolation quote unquote I mean it's
[L625] [22:26.72] not exactly a translation but they tried
[L626] [22:28.16] to do like very onetoone on. Um, and so
[L627] [22:31.20] that hopefully helps with like
[L628] [22:32.72] understanding all the abstractions. If
[L629] [22:34.56] they're building so heavily with agents,
[L630] [22:36.24] like does it even matter like to what
[L631] [22:39.52] degree do they need to understand
[L632] [22:40.80] different parts of the code? I actually
[L633] [22:42.32] don't know the answer to that, which is
[L634] [22:43.68] where my everything's changing so
[L635] [22:45.36] quickly comes from. It's like it's
[L636] [22:47.44] actually a little bit hard for me to say
[L637] [22:48.80] right now how much that actually matters
[L638] [22:51.52] anymore of um if they did transpile the
[L639] [22:54.32] whole codebase like how well do they
[L640] [22:55.84] need to understand things at different
[L641] [22:56.96] levels of abstraction like they should
[L642] [22:58.80] you know it's it's actually a very like
[L643] [23:00.64] I think a complicated question um so one
[L644] [23:03.68] reason is like how well you understand
[L645] [23:05.20] the code that's confusing thing the
[L646] [23:06.96] other is like you're kind of trading
[L647] [23:10.40] like when you do a rewrite like that
[L648] [23:13.12] you're trading
[L649] [23:15.76] known ISS issues for like new unknown
[L650] [23:18.08] issues. Like imagine you merge that and
[L651] [23:20.56] it closes like 50 open issues on GitHub
[L652] [23:22.96] in a literal sense. Okay, that's great.
[L653] [23:25.28] But you may have now caused like 50 new
[L654] [23:27.68] issues that didn't exist before that you
[L655] [23:29.36] don't know about. Um because your test
[L656] [23:32.72] suite is even a great test suite is only
[L657] [23:37.36] like an approximation of like your
[L658] [23:39.12] program's correctness. Um there's like
[L659] [23:42.72] Hyram's law which is like anything
[L660] [23:46.32] uh I'll get the phrasing wrong, but I
[L661] [23:47.92] mean the gist is basically any like
[L662] [23:49.76] implementation detail in your software
[L663] [23:51.92] of someone eventually becomes to rely on
[L664] [23:53.92] that. Um and so even things that aren't
[L665] [23:55.92] encoded as behavior become part of your
[L666] [23:58.48] API whether you like it or not. Um which
[L667] [24:00.80] is a scary thought, but basically that
[L668] [24:02.88] means that even if you pass your whole
[L669] [24:04.16] test suite, there's probably like lots
[L670] [24:05.44] of behavior that was like implicitly
[L671] [24:07.36] encoded in your program that's like
[L672] [24:09.04] changed. Um, and the unfortunate thing
[L673] [24:12.16] is you end up pushing that onto users.
[L674] [24:15.12] Like they are the ones that have to run
[L675] [24:16.32] into that and then report it and figure
[L676] [24:17.52] out what went wrong. And so that's like
[L677] [24:18.80] that's actually like my main area of
[L678] [24:20.00] concern with an automated rewrite. I
[L679] [24:21.44] actually trust the models enough that I
[L680] [24:24.24] would consider allowing them to do it,
[L681] [24:27.20] but the scarier thing for me is
[L682] [24:29.04] basically what's the impact for users?
[L683] [24:30.96] Like how do you and how do you roll that
[L684] [24:32.64] out safely? So um I don't know. It's
[L685] [24:35.60] kind of a we we're not going to like we
[L686] [24:37.52] don't have anything planned to like do
[L687] [24:38.88] that for any of our own projects, but it
[L688] [24:40.48] is like an interesting question. I mean
[L689] [24:42.80] I I think maybe like the third piece
[L690] [24:44.40] that I do think about especially right
[L691] [24:46.64] now where like everything's changing so
[L692] [24:48.24] quickly and
[L693] [24:51.36] there's you know the basically the
[L694] [24:53.92] spectrum of like how you write software
[L695] [24:56.56] um has like uh gotten like way wider.
[L696] [25:00.24] This is a terrible analogy, but there's
[L697] [25:01.84] like so many different ways to build
[L698] [25:03.52] software now. Like there's like the true
[L699] [25:06.48] like Andre Carpathy definition of vibe
[L700] [25:08.56] coding where you're like don't look at
[L701] [25:09.92] the code at all. Um all the way to like
[L702] [25:12.72] you know don't use LLMs and and blah
[L703] [25:14.56] blah. There's like a lot of different
[L704] [25:15.68] stuff in between. Um and I actually
[L705] [25:18.16] think that like right now I have pretty
[L706] [25:21.20] different approaches to different
[L707] [25:22.72] projects in terms of what I do. like we
[L708] [25:26.08] like I built, you know, a tool uh last
[L709] [25:31.84] week that was it's basically personal
[L710] [25:34.48] software. It's like a custom Rustliner
[L711] [25:38.08] to help us enforce certain things in our
[L712] [25:41.12] projects that I've like always wanted to
[L713] [25:43.12] enforce but didn't fit into existing
[L714] [25:45.04] tools. And I didn't read any of the
[L715] [25:47.12] code. Um like GPT55 did the whole thing.
[L716] [25:49.84] And um and it's like okay I can have a
[L717] [25:53.04] really different standard for that than
[L718] [25:55.20] UV because that project we are the only
[L719] [25:58.16] users. It's uh it's easy to tell if it's
[L720] [26:02.40] correct or not you know not to go too
[L721] [26:04.72] deep into the weeds on like what the
[L722] [26:05.92] project does but like we know if the
[L723] [26:08.08] output is like incorrect um and uh and
[L724] [26:12.72] there's no other users. UV is relied on
[L725] [26:16.08] by millions of you know millions of
[L726] [26:18.56] engineers and like all the like every
[L727] [26:21.20] single company and so it's like we want
[L728] [26:23.20] to be really careful about like what we
[L729] [26:24.64] ship there and how. Um but there's a lot
[L730] [26:27.12] of room right now I think for exploring
[L731] [26:28.72] like how we build software. Um you do
[L732] [26:31.12] have to be careful like what is your
[L733] [26:33.36] what what project are you working on and
[L734] [26:35.20] like what responsibility do you have to
[L735] [26:36.96] users and that's not meant to be a a
[L736] [26:38.72] subweet on like what Bun did. It's just
[L737] [26:40.88] like how I think about how do we want to
[L738] [26:43.60] push the envelope in like different
[L739] [26:44.80] places,
[L740] [26:45.52] >> right? I mean, to me that just reminds
[L741] [26:48.32] me of the prelim trade-off, the like
[L742] [26:51.12] navigating the I guess the risk of the
[L743] [26:53.52] code change and how much you verify it
[L744] [26:55.76] cuz
[L745] [26:57.44] if it's not risky, like it's a internal
[L746] [27:00.00] dev tool that only you and I are using.
[L747] [27:02.40] >> Yeah.
[L748] [27:02.80] >> Yeah. Yeah.
[L749] [27:03.28] >> Yeah. Maybe I just I ship it with I
[L750] [27:06.32] just, hey, stamp it. It's don't worry
[L751] [27:08.24] about it. It's not going to break
[L752] [27:09.28] anything. But if it's, you know, the the
[L753] [27:12.00] critical thing that's blocking customers
[L754] [27:15.20] from checking out or something, maybe we
[L755] [27:17.20] maybe we have two people reviewing it
[L756] [27:18.72] and there's like a lot of checks in that
[L757] [27:20.80] part of the codebase. So I it feels like
[L758] [27:23.68] the similar spectrum is just now like
[L759] [27:27.28] there's a new level of trying less which
[L760] [27:29.60] is not just like a human doesn't even
[L761] [27:32.72] interact with it. just, you know, ship
[L762] [27:35.84] it and maybe you just stamp it and no
[L763] [27:37.92] one ever even looked at it,
[L764] [27:39.36] >> right?
[L765] [27:40.08] >> Um whereas before at least to have
[L766] [27:42.72] written it a human would have had to do
[L767] [27:46.00] it.
[L768] [27:46.24] >> Yeah. Yeah. Yeah. Yeah. I mean I think
[L769] [27:49.84] >> well okay a lot of reactions to that.
[L770] [27:52.24] So, one I I guess like the other thing I
[L771] [27:54.08] would just say quickly about is like um
[L772] [27:58.72] sometimes I go over to their repo and
[L773] [28:01.28] it's like it's just so different than
[L774] [28:03.84] our repo and it's very interesting to
[L775] [28:05.44] look at because if you look like
[L776] [28:06.64] basically the number one contributor is
[L777] [28:08.16] like the the Robo bot and sometimes
[L778] [28:10.40] you'll click on PRs by humans and
[L779] [28:12.16] there's like human accounts talking back
[L780] [28:14.48] and forth but it's clear that all the
[L781] [28:15.76] comments were written by agents and
[L782] [28:17.36] you're like wow this is like very and so
[L783] [28:18.88] I look at that but my perspective on
[L784] [28:20.40] that is basically like Okay, I'm glad
[L785] [28:22.56] that people are like that they are like
[L786] [28:24.64] experimenting with like different ways
[L787] [28:27.28] to like build software. Like I don't
[L788] [28:28.96] know that I'm ready to do that but like
[L789] [28:31.36] but like I but I do think that like a
[L790] [28:33.28] lot of basically a lot of things are
[L791] [28:34.40] going to change and I think it's very
[L792] [28:35.52] interesting to be experimenting. So I'm
[L793] [28:37.12] glad that they are experimenting with
[L794] [28:38.40] things is my sorry is my like conclusion
[L795] [28:40.16] there.
[L796] [28:40.80] >> Do you block like if people are just
[L797] [28:43.44] submitting a full agent stuff on your
[L798] [28:46.08] repos is that
[L799] [28:47.20] >> we do. Yeah. So we have an AI policy
[L800] [28:49.68] now. um which isn't intended to be like
[L801] [28:52.96] anti-AI but it's really like intended to
[L802] [28:56.32] um because I mean we develop like very
[L803] [28:58.24] heavily with LLMs um like that is true
[L804] [29:01.28] um but it's it's more intended to be
[L805] [29:04.32] like how do we um
[L806] [29:08.32] how do we
[L807] [29:11.52] like retain like useful contributions
[L808] [29:14.16] while filtering out like net negative
[L809] [29:17.36] interactions from the repo Because like
[L810] [29:21.04] a contributor coming in and
[L811] [29:24.72] uh you know posting a comment that their
[L812] [29:26.40] agent wrote and then we like ask them a
[L813] [29:28.16] question and then they just paste like
[L814] [29:30.40] the agent response back like there's
[L815] [29:32.24] like very little value in that, right?
[L816] [29:34.24] Like we could just like ask the question
[L817] [29:36.64] to to the agent, right? And so the
[L818] [29:38.72] things like we want to retain the things
[L819] [29:40.00] that are useful from like human
[L820] [29:41.92] contributors which is like you know like
[L821] [29:44.40] insight like ways to reproduce like the
[L822] [29:47.04] information we would need to like plug
[L823] [29:48.48] it into our agent because there's no
[L824] [29:49.92] point in just like having a conversation
[L825] [29:51.68] with an LLM on a GitHub issue right like
[L826] [29:53.92] it doesn't really do anything for us. Um
[L827] [29:57.04] and uh so we we you know our policy is
[L828] [30:00.48] roughly um you should you should like
[L829] [30:04.00] you need to like understand like what
[L830] [30:05.68] you're pasting in u or or what you are
[L831] [30:09.12] submitting right which I sounds like a
[L832] [30:10.64] low bar um but it's not and uh
[L833] [30:13.28] >> how do you police that
[L834] [30:15.44] >> if we can't tell and it is agent written
[L835] [30:18.00] then I guess that's fine right
[L836] [30:22.88] um but you know at least right Now,
[L837] [30:25.76] there are just lots of tells and like um
[L838] [30:29.12] uh you know, being way more thorough
[L839] [30:31.60] than a human would ever be, including
[L840] [30:33.04] way too much detail, way more
[L841] [30:34.96] formatting,
[L842] [30:36.56] um using terminology that a human
[L843] [30:38.40] wouldn't use, like inventing random
[L844] [30:40.24] jargon, um tons of links, like I guess
[L845] [30:43.60] the broad sign would be like putting in
[L846] [30:45.60] way more effort in ways that aren't
[L847] [30:47.04] necessary in a way that a human wouldn't
[L848] [30:49.04] is like almost always agent authored.
[L849] [30:52.00] But it's been Yeah, it's been
[L850] [30:54.48] challenging. I mean, I think the hard
[L851] [30:55.60] thing Zigg has a much more strict LLM
[L852] [30:58.24] policy, which is like no LLM written
[L853] [30:59.92] code or no LLM assisted code at all in
[L854] [31:01.76] the project, which is very different
[L855] [31:02.96] than us. I mean, like all of my PRs now
[L856] [31:05.68] are are LLM written, right? LLM written.
[L857] [31:08.24] Um uh and they had a blog post about
[L858] [31:11.92] this idea of like they saw called it
[L859] [31:14.32] something along the lines of like
[L860] [31:15.28] contributor poker where it's like you're
[L861] [31:17.76] kind of trying to place like bets on
[L862] [31:19.04] contributors like like historically in
[L863] [31:20.72] open source when a contributor came
[L864] [31:22.40] around um they might be like new to the
[L865] [31:25.20] project but they could show like signs
[L866] [31:26.40] of promise or like they're really
[L867] [31:28.00] engaged or really interested and like
[L868] [31:29.60] you give them feedback they take the
[L869] [31:31.76] feedback and they fix up their PR and
[L870] [31:34.40] then the next time they put up PR
[L871] [31:35.60] they've learned from that feedback right
[L872] [31:37.12] it's the same way as like mentoring a
[L873] [31:38.56] new engineer who joins your team. It's
[L874] [31:40.24] like they learn from feedback, it
[L875] [31:42.48] compounds, they get better, and then
[L876] [31:43.76] they can actually mentor someone else in
[L877] [31:45.20] the future, right? And so you're making
[L878] [31:47.68] investments in people in a way. It's the
[L879] [31:50.08] same for open source. It's like you want
[L880] [31:51.60] to um I thought about this a lot
[L881] [31:53.28] historically. It's like you want to like
[L882] [31:55.04] invest in good contributors who are
[L883] [31:56.88] going to grow to help others and be
[L884] [31:58.80] maintainers in their own right. that's
[L885] [32:00.80] kind of gone um if for PRs especially
[L886] [32:04.56] that are written by agents because
[L887] [32:06.16] people don't really learn anything like
[L888] [32:08.16] someone can put up a PR that's written
[L889] [32:09.44] by an agent and you leave comments and
[L890] [32:12.24] then they take your comments and put
[L891] [32:13.44] them into the agent and then update the
[L892] [32:15.12] PR and then merge it and it's like that
[L893] [32:17.28] there's no compounding feedback. Um and
[L894] [32:20.00] so I actually do like understand that
[L895] [32:22.00] perspective a lot um of uh like the the
[L896] [32:25.52] contract between like maintainers and
[L897] [32:27.92] contributors is like pretty different
[L898] [32:29.20] now. Um and you know relatedly again not
[L899] [32:33.12] a novel insight but the cost of putting
[L900] [32:35.12] up a plausible PR has gone to zero. Um
[L901] [32:38.24] while the cost to like review and vet
[L902] [32:41.28] applausible PR has remained the same and
[L903] [32:44.48] um is very high like especially for the
[L904] [32:47.04] projects that we work on where
[L905] [32:50.00] um
[L906] [32:52.32] you know I'm not trying to like
[L907] [32:53.52] overstate it. They're just like hard
[L908] [32:54.80] projects. Like TY is our type checker.
[L909] [32:57.36] Probably hard hardest project I've
[L910] [32:58.80] worked on technically to like get a
[L911] [33:00.16] change merged because of the like
[L912] [33:03.36] complexity in the architecture but also
[L913] [33:05.68] like the problem space like it's just
[L914] [33:07.20] very very hard. Um and so if someone
[L915] [33:09.44] puts up a plausible PR to to TY it might
[L916] [33:11.84] take them two minutes and then it could
[L917] [33:14.08] take us you know an hour to understand
[L918] [33:15.92] it. And so it's created like very poor
[L919] [33:19.20] dynamics
[L920] [33:20.88] in open source. And um I I don't know
[L921] [33:24.00] how we've solved that. Um I think it
[L922] [33:26.48] will like continue to get worse um until
[L923] [33:29.44] hopefully it gets better in some way
[L924] [33:31.28] like we find ways to solve this. Um but
[L925] [33:33.92] it's certainly something we've
[L926] [33:34.88] experienced in our projects,
[L927] [33:36.32] >> right? It sounds like review is becoming
[L928] [33:39.12] more and more of a bottleneck. Is for
[L929] [33:41.60] that bun rewrite. Do you know if it was
[L930] [33:43.84] human like humans read that code or that
[L931] [33:46.32] was just kind of
[L932] [33:46.96] >> No, I don't think it was human reviewed.
[L933] [33:48.40] Yeah. So, it's just YOLO rewrite the
[L934] [33:50.80] whole thing. And
[L935] [33:51.68] >> yeah, I mean, in a way, I think it's
[L936] [33:53.28] like I think they did have and I'm
[L937] [33:55.52] excited for like at least at time of at
[L938] [33:58.08] time of recording, quote unquote, you
[L939] [33:59.60] know, Jared hasn't published the blog
[L940] [34:01.12] post yet, which is like I mean, he keeps
[L941] [34:03.28] making jokes about how like the blog
[L942] [34:04.88] post taking way longer than the rewrite.
[L943] [34:06.56] Um, but I'm actually really interested
[L944] [34:08.16] in the blog post because I think they
[L945] [34:09.60] did have a pretty
[L946] [34:11.60] like sophisticated approach to like how
[L947] [34:13.84] the rewrite worked. Um, which will be
[L948] [34:16.24] interesting to read about. like it
[L949] [34:17.36] wasn't just like they had one prompt
[L950] [34:18.48] that was like rewrite this in in Rust.
[L951] [34:20.32] It was like they tried to have um at
[L952] [34:22.80] least my impression from looking at the
[L953] [34:24.48] PR is like there were um there were
[L954] [34:27.36] actually like different phases of the
[L955] [34:29.84] rewrite and like each file had to go
[L956] [34:31.52] through like a couple different phases
[L957] [34:33.36] that had like ways to validate whether
[L958] [34:34.88] it was correct or not. So um uh the
[L959] [34:38.64] answer is no though. I like I don't
[L960] [34:40.16] think a human was reading like
[L961] [34:41.76] significant amounts of that code. Like
[L962] [34:43.12] it's just not possible basically.
[L963] [34:45.68] What if we we both agreed today that
[L964] [34:48.24] Zigg was objectively better than Rust
[L965] [34:50.80] and then someone on your team said, you
[L966] [34:53.84] know, I can do this rewrite into Zigg.
[L967] [34:56.96] Would Would you block it if
[L968] [34:59.04] >> I think I would block it? I I think
[L969] [35:02.64] um I I don't know whether I'd be right
[L970] [35:04.64] to do so, but I think like we as a team
[L971] [35:06.96] like aren't there yet. Um and uh and
[L972] [35:11.84] maybe we will like get there and that's
[L973] [35:13.44] how we will feel eventually. But like
[L974] [35:15.04] right now I I think we just feel like
[L975] [35:17.52] right now um there's still a lot of
[L976] [35:21.36] value in like deeply understanding like
[L977] [35:23.36] our code and our tool chain and like the
[L978] [35:25.52] ecosystem. And so I would say we don't
[L979] [35:28.72] want to do that. Um but
[L980] [35:31.68] might depend on the project. I don't
[L981] [35:33.20] know.
[L982] [35:34.72] all the things that you've built,
[L983] [35:35.92] they're like an order of magnitude
[L984] [35:37.76] faster than what was available at the
[L985] [35:39.92] time.
[L986] [35:41.12] >> How much of a difference did Rust make
[L987] [35:44.08] on that graph?
[L988] [35:45.92] >> I think it so it depends a bit on the
[L989] [35:48.00] project. Um I think I think in rough
[L990] [35:52.32] a lot of it was just Rust. Um and then
[L991] [35:56.80] over time I think we've
[L992] [35:59.68] um
[L993] [36:01.28] improved on that a lot because
[L994] [36:04.48] uh because you can even look at the
[L995] [36:06.80] history of the project like the project
[L996] [36:09.36] I mean hopefully no one like hopefully
[L997] [36:11.36] this is still true but like basically
[L998] [36:12.80] over time the project gets faster um and
[L999] [36:16.24] sometimes that regresses but like uh you
[L1000] [36:18.64] know you basically maybe I put it
[L1001] [36:20.16] differently you could write rough you
[L1002] [36:24.08] know in like a couple different ways all
[L1003] [36:27.04] in rust and they could have really
[L1004] [36:28.80] different performance characteristics.
[L1005] [36:30.16] So that's just to say that like I I
[L1006] [36:32.24] generally think of rust as like the the
[L1007] [36:35.44] floor or the uh the sort of like the
[L1008] [36:39.36] baseline performance that you get is
[L1009] [36:40.88] going to be significantly better. But
[L1010] [36:42.64] you still have to you still get a lot
[L1011] [36:44.80] more out of like thinking deeply about
[L1012] [36:46.64] performance and design. Like if you take
[L1013] [36:48.64] the same program in Rust and in Python
[L1014] [36:50.72] like exact same implementation to to the
[L1015] [36:52.88] closest approximation you can get like
[L1016] [36:54.72] the Rust one will be faster but you can
[L1017] [36:56.88] then take that program and you can
[L1018] [36:58.08] probably optimize it another like 10x um
[L1019] [37:00.40] I don't know about 10x but my point is
[L1020] [37:02.48] even within being written in Rust
[L1021] [37:04.16] there's like a ton of room for how to
[L1022] [37:06.64] make things more performant how to write
[L1023] [37:08.08] really performant software and like
[L1024] [37:09.60] again when I started working on Rough um
[L1025] [37:12.72] part of my my goal was to learn Rust and
[L1026] [37:14.80] so I wrote I did write a lot of like bad
[L1027] [37:16.80] code Um, which is fine. Like I shipped
[L1028] [37:20.24] something out that was really helpful to
[L1029] [37:21.44] people. Um, but it's gotten a lot better
[L1030] [37:23.20] I think over time and like we've made it
[L1031] [37:24.88] more and more performant. Um I think in
[L1032] [37:27.52] UV
[L1033] [37:29.28] there was more um sort of like
[L1034] [37:32.88] architectural innovation beyond just
[L1035] [37:35.20] being in Rust especially because UV like
[L1036] [37:37.68] so as a package manager um you're doing
[L1037] [37:39.68] a ton of IO like downloading f and you
[L1038] [37:42.80] know downloading files over the network
[L1039] [37:44.56] unzipping things like writing them to
[L1040] [37:46.48] disk moving them around the llinter
[L1041] [37:49.04] doesn't have to do as much of that I
[L1042] [37:50.56] mean it has to read all your files but
[L1043] [37:52.88] there's there's not like a sign a huge
[L1044] [37:54.72] amount of IO
[L1045] [37:55.92] the package manager is like mostly IO.
[L1046] [37:58.16] It's like and then you're trying to do
[L1047] [38:00.08] things like very efficiently. So um
[L1048] [38:01.84] there it was more I mean rust was
[L1049] [38:04.56] important but I I do think that in UV
[L1050] [38:07.68] there's more um you know architectural
[L1051] [38:10.80] things that we did or like ways that we
[L1052] [38:12.72] thought a lot about performance like the
[L1053] [38:14.00] c the design of the cache is like very
[L1054] [38:16.72] very intentional um and makes it so that
[L1055] [38:21.12] um
[L1056] [38:22.96] like repeated installs of the same
[L1057] [38:25.84] package on your machine are like are
[L1058] [38:28.32] like near instant because of the way
[L1059] [38:30.16] that we like lay out the cache and the
[L1060] [38:31.92] way that we install from the cache into
[L1061] [38:33.68] your projects. Um, it basically means
[L1062] [38:35.36] that if you've installed a package
[L1063] [38:36.64] before, installing it again is extremely
[L1064] [38:39.52] cheap. Um, and both in terms of disc
[L1065] [38:42.16] space and time. Um, and so that was like
[L1066] [38:44.64] that's like a very different design than
[L1067] [38:46.64] um, any of the other like Python package
[L1068] [38:48.48] managers had. Uh, so again, it kind of
[L1069] [38:50.80] depends on the project. Um, I do tend to
[L1070] [38:53.60] think that like whether you're writing
[L1071] [38:55.36] code in Rust or in Python, there's like
[L1072] [38:57.12] always room to like be thinking about
[L1073] [38:58.72] performance. like you can always make
[L1074] [39:01.52] things faster or slower. Like even if
[L1075] [39:03.04] you're writing in Python, like you can
[L1076] [39:04.48] still make things like much much faster
[L1077] [39:06.72] um by like thinking harder about
[L1078] [39:09.12] performance and design. Um so it's some
[L1079] [39:11.84] mix but it depends on the project.
[L1080] [39:14.80] >> Open AAI, Enthropic, Cursor, and
[L1081] [39:17.76] Verscell all use this product to make
[L1082] [39:19.92] their lives better. And the problem it
[L1083] [39:22.08] solves is when you're building SAS or an
[L1084] [39:24.32] AI product and you want to sell to other
[L1085] [39:26.64] companies, there's all these
[L1086] [39:28.16] requirements you need to meet. There's
[L1087] [39:30.08] SSO, there's skim, there's arbback,
[L1088] [39:33.36] there's audit logs. These are all things
[L1089] [39:35.20] that take time to integrate, but aren't
[L1090] [39:37.36] the main focus of your app. Work OS is
[L1091] [39:39.52] an API layer that lets you meet all of
[L1092] [39:41.44] these requirements in just a few lines
[L1093] [39:43.60] of code. So, let's say you have a new
[L1094] [39:45.60] SAS product and you want to sell to
[L1095] [39:47.36] other companies. work OS will solve all
[L1096] [39:49.76] of these critical feature gaps for you.
[L1097] [39:52.48] You can check them out at workos.com to
[L1098] [39:55.12] learn more and get started and I
[L1099] [39:57.28] appreciate them for supporting my work
[L1100] [39:58.96] and sponsoring this podcast over the
[L1101] [40:01.36] course of the project. Do you have a you
[L1102] [40:04.56] know top few things that were
[L1103] [40:06.72] implementing the project that were
[L1104] [40:08.80] technically challenging or most
[L1105] [40:10.32] interesting to you? I really like this
[L1106] [40:12.80] optimization that Andrew on our team um
[L1107] [40:16.64] who goes by burnt sushi. He's uh he's
[L1108] [40:19.60] the author of Rip Grap and bunch of
[L1109] [40:22.16] other things. He's like really amazing
[L1110] [40:23.76] engineer. He did this really cool
[L1111] [40:26.16] optimization around how we represent
[L1112] [40:27.68] versions. It's pretty cool. I mean
[L1113] [40:29.36] basically like if you think about
[L1114] [40:30.64] resolving and installing like a very
[L1115] [40:32.32] complex Python project um we we it turns
[L1116] [40:36.00] out that we have to like parse and
[L1117] [40:39.04] create lots of versions like as in 1.0.1
[L1118] [40:43.12] 1.0.2 to like we just like version
[L1119] [40:45.76] objects within the program like we end
[L1120] [40:47.60] up parsing and creating a lot of those
[L1121] [40:49.84] and it turns out that actually like
[L1122] [40:51.68] allocating that memory um was expensive
[L1123] [40:54.88] um given like the scale like the number
[L1124] [40:57.20] of times we were doing it and he came up
[L1125] [40:59.44] with a representation where we can
[L1126] [41:01.36] represent um like 90 something% of
[L1127] [41:04.00] versions with a single U64 integer. So
[L1128] [41:06.96] it's just like way more efficient. Um
[L1129] [41:08.72] and uh the benchmarks around that and
[L1130] [41:10.72] the implementation were were very cool.
[L1131] [41:12.40] It's like one of the coolest PRs I've
[L1132] [41:13.68] read, I think. Um, in TY, which our type
[L1133] [41:17.44] checker, there's a lot of like very
[L1134] [41:19.84] interesting performance work that's
[L1135] [41:22.24] happening, especially to make it um
[L1136] [41:25.36] incremental. So like uh uh TY is
[L1137] [41:29.52] designed to be um a type checker and a
[L1138] [41:31.68] language server. And
[L1139] [41:34.64] the whole system is like highly
[L1140] [41:36.00] incremental. So the idea there is like
[L1141] [41:38.16] if you're in an a text editor and you
[L1142] [41:40.56] open up like one file, you don't
[L1143] [41:43.04] necessarily want to like have to type
[L1144] [41:45.04] check your entire project like all your
[L1145] [41:47.04] dependencies, every file in the project
[L1146] [41:48.48] just to get analysis for that file. Um
[L1147] [41:51.92] like because you don't need to. Um so so
[L1148] [41:55.68] how do you make that work? That's like
[L1149] [41:56.88] that's sort of like uh I would that
[L1150] [41:58.72] would be like lazy. You want to be lazy.
[L1151] [42:01.36] Um, but the other piece to that is like
[L1152] [42:02.96] if you have a file open and you edit it,
[L1153] [42:06.24] um, or you have like two files open, you
[L1154] [42:08.08] edit one of them. Um, you only want to
[L1155] [42:11.44] recmp compute like exactly what you need
[L1156] [42:12.96] to recomputee. Like you don't want to
[L1157] [42:14.32] have to go and retype check like the
[L1158] [42:15.92] entire codebase again. Um, especially
[L1159] [42:18.08] because maybe you're working in a big
[L1160] [42:19.28] project like PyTorch and it's like you
[L1161] [42:21.28] have two files open, you edit one of
[L1162] [42:22.64] them, you don't want it to like and then
[L1163] [42:24.16] you save, you don't want it to take like
[L1164] [42:25.36] two seconds to like retype check the
[L1165] [42:26.96] project and like give you a new
[L1166] [42:28.00] analysis. So the whole system is built
[L1167] [42:31.04] around queries um which is pretty
[L1168] [42:33.28] interesting. This is more of like a
[L1169] [42:34.32] macro design thing. Um but uh we built
[L1170] [42:37.20] it on top of a framework called Salsa
[L1171] [42:39.04] which is um also what Rust Analyzer uses
[L1172] [42:41.60] which is like the popular Rust language
[L1173] [42:43.28] server. Um and now we've
[L1174] [42:47.28] intentionally or inadvertently become
[L1175] [42:48.96] like like very large contributors to
[L1176] [42:51.60] Salsa. Um but but the whole the whole
[L1177] [42:54.16] system is built around that which has
[L1178] [42:55.44] been like very interesting
[L1179] [42:56.32] architecturally.
[L1180] [42:57.60] >> Interesting. So it's it's lazy so it
[L1181] [43:00.00] doesn't type check the whole codebase
[L1182] [43:01.76] and it's incremental. So
[L1183] [43:03.04] >> yeah the incremental part is the thing
[L1184] [43:04.32] that's hard because you kind of need a
[L1185] [43:05.76] way to basically like uh it needs to be
[L1186] [43:08.64] able to model kind of like a dependency
[L1187] [43:10.08] graph of like everything that's
[L1188] [43:11.36] happening in the code. Um and so then
[L1189] [43:13.36] when you change something we want to
[L1190] [43:14.72] just like flow the data back through all
[L1191] [43:16.64] the different pieces like only the
[L1192] [43:18.00] pieces. Yeah. Um so that took a lot of
[L1193] [43:21.68] work. um but uh is it has come together
[L1194] [43:25.28] um and I've been doing a lot of
[L1195] [43:27.92] optimization lately with codecs um
[L1196] [43:32.32] because
[L1197] [43:34.96] it tends to be very good um at
[L1198] [43:37.68] especially at like micro optimizations
[L1199] [43:39.68] like if I'm like and in TY in particular
[L1200] [43:43.44] we also need to think a lot about memory
[L1201] [43:45.92] um not just speed because if you work on
[L1202] [43:49.20] a very large project like you don't want
[L1203] [43:50.72] it to take like many many many gigabytes
[L1204] [43:53.52] of you know just to like run your
[L1205] [43:55.60] language server like ideally you want it
[L1206] [43:57.04] to be like relatively efficient. Um, so
[L1207] [43:59.28] like I spend a lot of time now kind of
[L1208] [44:01.52] like continuously optimizing like memory
[L1209] [44:03.68] usage and performance and I can just set
[L1210] [44:05.36] a goal that's like try to reduce memory
[L1211] [44:07.76] like salsa memory by like 1% on this
[L1212] [44:11.04] project and like you can't do like these
[L1213] [44:13.84] these things that you might like like
[L1214] [44:16.08] try to do. Um,
[L1215] [44:18.24] and it's very good at just like coming
[L1216] [44:19.76] up with um like very reasonable things.
[L1217] [44:22.88] And so I I don't know. I find that very
[L1218] [44:24.96] cool because it's kind of like you can
[L1219] [44:26.24] almost have like continuously op I won't
[L1220] [44:28.16] say self optimizing that's like a built
[L1221] [44:29.76] grandiose but you can kind of be like
[L1222] [44:31.68] continuously like just like optimizing
[L1223] [44:33.60] your software. Um so uh I've been
[L1224] [44:36.48] enjoying that a lot. Um but uh but most
[L1225] [44:40.56] of those are like um yeah trying to find
[L1226] [44:43.28] ways to like represent things uh that
[L1227] [44:45.28] take up less memory um or uh trying to
[L1228] [44:49.12] come up with like sometimes it's like
[L1229] [44:50.56] trying to come up with broader redesigns
[L1230] [44:51.92] to like fix pathological performance.
[L1231] [44:55.12] >> That one optimization where with the
[L1232] [44:57.20] version numbering and seeing that
[L1233] [45:00.32] you can limit it just to like use 64. If
[L1234] [45:04.08] you think back to some of these more
[L1235] [45:05.76] creative optimizations that were done
[L1236] [45:08.16] that was in the human era, do you think
[L1237] [45:10.88] if you just I don't know ran codeex and
[L1238] [45:13.36] you're like hey just don't break things
[L1239] [45:14.96] but lower do you have faith that it
[L1240] [45:17.20] would come up with that or is that kind
[L1241] [45:18.64] of a a step above what
[L1242] [45:20.56] >> that's a very interesting question. If
[L1243] [45:22.24] you just at least in my experience like
[L1244] [45:24.00] if you just ask these things to reduce
[L1245] [45:25.36] memory or improve performance by some
[L1246] [45:28.48] you know moderate percentage it will
[L1247] [45:30.80] typically come up with things around the
[L1248] [45:32.48] edges um as opposed to like larger
[L1249] [45:35.84] uh redesigns or reconsiderations but you
[L1250] [45:38.48] can get to those larger redesigns if you
[L1251] [45:42.72] prompt and collaborate with the agent.
[L1252] [45:44.56] And so if you sort of ask like well like
[L1253] [45:48.32] should we be thinking a bit bigger about
[L1254] [45:49.84] like why we have to represent the data
[L1255] [45:51.76] this way like you can you can get to
[L1256] [45:53.84] like bigger ideas. And so that might be
[L1257] [45:56.48] an idea that you could have gotten to
[L1258] [45:58.08] with prompting if you were like um you
[L1259] [46:01.52] know okay let's start by like profiling
[L1260] [46:02.80] and figuring out where we're spending a
[L1261] [46:03.84] lot of time and then maybe the you know
[L1262] [46:06.00] would eventually come back to you and
[L1263] [46:07.60] say like we're spending a lot of time in
[L1264] [46:08.88] like version parsing and like version
[L1265] [46:10.96] like ball like version drop and version
[L1266] [46:12.88] allocation like blah blah and we' be
[L1267] [46:14.72] like okay well like how could we
[L1268] [46:15.84] represent these like more compactly and
[L1269] [46:17.44] it would probably start by finding like
[L1270] [46:19.20] micro optimizations in the
[L1271] [46:20.64] representation of like well this field
[L1272] [46:22.96] like you combine these two fields like
[L1273] [46:25.04] if you buy it's like blah blah blah but
[L1274] [46:26.88] I think if you kept pushing it like it's
[L1275] [46:28.56] plausible it would get there um but
[L1276] [46:30.88] that's not the thing it's going to come
[L1277] [46:31.92] up with by default. Mitchell Hashimoto
[L1278] [46:34.88] um who was like one of the Hashiore
[L1279] [46:37.68] founders works on Ghosty um he had a
[L1280] [46:40.96] post that was insightful I thought last
[L1281] [46:43.76] week or this weekend about a renderer he
[L1282] [46:46.48] wrote where it was like a really
[L1283] [46:47.44] terrible renderer. I'll probably butcher
[L1284] [46:49.28] the the tweet, but it was like it was a
[L1285] [46:51.04] really terrible renderer and then he
[L1286] [46:52.40] hadn't like intentionally and then he
[L1287] [46:53.68] had an LM like optimize it and it made
[L1288] [46:55.28] it like 10 times faster and he's like
[L1289] [46:57.04] great, right? Actually, no. like my
[L1290] [46:58.80] handwritten version was like a hundred
[L1291] [47:00.24] times faster and it's like you know like
[L1292] [47:02.64] you lose if you're not like using your
[L1293] [47:04.32] brain to like think about from first
[L1294] [47:06.96] principles like how fast should it be
[L1295] [47:08.48] and like how should the system work like
[L1296] [47:10.16] then you just like ship all this these
[L1297] [47:12.32] like accumulated like I mean I I won't
[L1298] [47:15.36] necessarily call it slop but it's like
[L1299] [47:16.88] you just ship these like things and
[L1300] [47:18.16] you're like yeah oh my god I made it 10
[L1301] [47:19.36] times faster but really it should be
[L1302] [47:20.64] like 100 times faster and so I think I
[L1303] [47:24.48] don't know it shouldn't be controversial
[L1304] [47:25.68] there's still a lot of room for like
[L1305] [47:26.64] using your brain Right. And like uh uh
[L1306] [47:30.40] but I do I do think it's like I struggle
[L1307] [47:33.12] with this stuff a lot. I mean like I'm
[L1308] [47:34.48] changing how I write software a lot and
[L1309] [47:36.80] um you know I've had people on my team
[L1310] [47:38.64] like because I'm using agents a lot and
[L1311] [47:40.80] and also was you know to some degree
[L1312] [47:43.04] trying to like
[L1313] [47:45.76] push our team to like use agents more. I
[L1314] [47:49.44] mean I mean some of that for me came
[L1315] [47:50.72] from a place of like we build tools for
[L1316] [47:53.52] software engineers and a lot of our
[L1317] [47:56.64] users are now using agents and so if we
[L1318] [47:59.84] like if I if everything good that we do
[L1319] [48:02.88] that's an exaggeration but if everything
[L1320] [48:04.16] good that we do comes from like
[L1321] [48:05.28] understanding our users very well and
[L1322] [48:06.80] like how they work then like we should
[L1323] [48:08.56] probably be like using agents that we
[L1324] [48:10.00] understand like what it's like to build
[L1325] [48:11.20] software for with them so that we can
[L1326] [48:12.96] build better tools for our users. That
[L1327] [48:14.56] was part of my motivation. Um, and part
[L1328] [48:16.64] of it was just kind of seeing how it can
[L1329] [48:19.68] change like how you work. And I don't
[L1330] [48:21.60] know, I think I'm shipping a lot more.
[L1331] [48:23.68] Um, but but it has been like um it has
[L1332] [48:27.52] been like a a difficult process. Like
[L1333] [48:29.04] I've had people on the team tell me um
[L1334] [48:32.72] uh which I think is great that they tell
[L1335] [48:34.48] me this. Um but they're like, "Oh, it
[L1336] [48:36.80] used to be the case that like whenever
[L1337] [48:38.32] you put up a PR, I could like review it
[L1338] [48:40.00] pretty minimally because I had a lot of
[L1339] [48:41.36] confidence in it and like your work. And
[L1340] [48:43.44] now it's like when you put up a PR I
[L1341] [48:45.20] actually have to review it really
[L1342] [48:46.32] closely because you're not like writing
[L1343] [48:48.40] it anymore. It's like the agent and I
[L1344] [48:50.00] was like wow that's like that's like
[L1345] [48:51.84] very interesting to they're completely
[L1346] [48:53.44] right which is and like and the same
[L1347] [48:56.08] thing happens to me. It's like if I go
[L1348] [48:58.64] to sleep and then wake up in the morning
[L1349] [48:59.76] and look at one of the PRs I put up and
[L1350] [49:01.12] I'm like wait this is terrible. You know
[L1351] [49:02.32] what I mean? It's like you can it's it
[L1352] [49:04.40] it's just uh it is easy to trick
[L1353] [49:07.36] yourself into like
[L1354] [49:10.40] basically believing work that isn't at
[L1355] [49:13.52] the same standard as what you would do
[L1356] [49:14.88] before. And I don't think I think we
[L1357] [49:16.56] have we don't really know what to do
[L1358] [49:17.84] with that. Um, and I'm kind of learning
[L1359] [49:20.00] and getting better and like I mean this
[L1360] [49:21.44] was I think I'm doing a lot better job
[L1361] [49:23.28] now than I was in like probably you know
[L1362] [49:25.52] like February or something where I was
[L1363] [49:27.60] like I was just like you know fully
[L1364] [49:30.56] agent killed and I'm like now I'm like a
[L1365] [49:33.04] little bit more like um but so my point
[L1366] [49:36.40] is like that was like a par powerful
[L1367] [49:38.08] kind of like moment for me when someone
[L1368] [49:39.52] on the team said that and I was like wow
[L1369] [49:41.12] like you're right and I and I see that
[L1370] [49:42.96] in other people on the team's work too
[L1371] [49:44.16] like it's not just limited to me but
[L1372] [49:45.44] it's like um you know it really guys
[L1373] [49:48.32] throw a lot of things on their head.
[L1374] [49:50.48] >> If you generate pure slop, that's that's
[L1375] [49:53.52] easy. But I think there's this gray area
[L1376] [49:55.44] where you you generate partially AI slop
[L1377] [49:59.36] or it's, you know, it's it's acceptable,
[L1378] [50:01.52] but it's not at the bar that you used to
[L1379] [50:03.44] have. Do you What are the tactics that
[L1380] [50:06.08] you've used on the team that have worked
[L1381] [50:08.24] for combating this kind of gray area AI
[L1382] [50:11.28] slop?
[L1383] [50:12.88] I'd like to get to a world.
[L1384] [50:15.76] We're not here and I don't know if we'll
[L1385] [50:17.68] ever get there. I'd like to get to a
[L1386] [50:19.68] world where if you put up a PR and it's
[L1387] [50:24.00] all green, then the odds of it getting
[L1388] [50:27.76] merged are like extremely high, right?
[L1389] [50:31.36] Um because that would mean that like you
[L1390] [50:33.44] have automated verification for like
[L1391] [50:35.44] most of what matters. Um and we have a
[L1392] [50:38.24] lot of that in our projects and we've
[L1393] [50:39.28] tried to add more over time and I think
[L1394] [50:40.64] it's helpful. Like we have like in TY
[L1395] [50:42.40] especially we have um
[L1396] [50:44.96] uh tons of like benchmarks like that run
[L1397] [50:47.44] under val grind like um through through
[L1398] [50:49.68] co cod speed like on every PR. So we get
[L1399] [50:51.84] like and that includes memory. So we
[L1400] [50:53.36] benchmark like memory usage and um uh
[L1401] [50:57.20] simulation time and wall time like on
[L1402] [50:58.96] every PR. And then we also have a really
[L1403] [51:02.24] big suite of ecosystem
[L1404] [51:05.36] um tests. So basically every time you
[L1405] [51:07.68] put up a PR we run before and after on
[L1406] [51:10.64] like a bunch of projects in the
[L1407] [51:12.00] ecosystem and then we create this report
[L1408] [51:14.72] of the diff of all the diagnostics like
[L1409] [51:17.20] the errors that got removed and added
[L1410] [51:18.96] and everything. So we have like over
[L1411] [51:20.72] time we've tried to do like more and
[L1412] [51:22.00] more uh these are important honestly
[L1413] [51:24.16] even before we had agents like these
[L1414] [51:25.52] were like we basically couldn't build
[L1415] [51:26.64] without these things but the point is
[L1416] [51:28.40] like I want to have like more automated
[L1417] [51:30.48] verification um and try to get better at
[L1418] [51:32.80] that um and that includes things too
[L1419] [51:36.16] like um we basically assume now that
[L1420] [51:42.56] anyone on the team that puts up a PR has
[L1421] [51:46.00] already run that through codeex review
[L1422] [51:48.00] like probably several times. Um, and
[L1423] [51:50.16] that's basically an assumption. Um, I
[L1424] [51:52.00] mean, we could automate that process,
[L1425] [51:53.20] but
[L1426] [51:53.52] >> codeex review is just an agent reviewing
[L1427] [51:55.36] the code and double checking.
[L1428] [51:56.48] >> Yeah, it's just running codeex and then
[L1429] [51:57.60] just doing slash review.
[L1430] [51:58.56] >> I see.
[L1431] [51:59.04] >> That's it. Yeah, it's not that fancy. I
[L1432] [52:00.32] mean, it's not sorry, it's not that
[L1433] [52:01.36] sophisticated, but it's just like
[L1434] [52:03.04] because now it's like if if a
[L1435] [52:04.32] contributor puts up a PR, that's the
[L1436] [52:05.44] first thing that we do,
[L1437] [52:06.40] >> right?
[L1438] [52:07.84] >> Um because it tends to find good things.
[L1439] [52:10.16] Um, you know, I think I think the things
[L1440] [52:12.40] that I've uh so so like basically I
[L1441] [52:15.28] think one bucket is like how do you um
[L1442] [52:21.52] create more like automated systems that
[L1443] [52:24.16] just help get things make sure things
[L1444] [52:26.72] are right. Um, and that also includes
[L1445] [52:29.52] things like trying to improve your like
[L1446] [52:31.44] agents.mmd file over time. Like if there
[L1447] [52:33.52] are things if there's feedback you're
[L1448] [52:34.72] giving in a review that the agent's not
[L1449] [52:36.56] respecting, try to find a way to help
[L1450] [52:37.92] the agent learn that. even learn um uh
[L1451] [52:41.36] skills like we have some shared skills
[L1452] [52:42.80] on the team stuff like that like none of
[L1453] [52:44.48] this stuff is very sophisticated by the
[L1454] [52:45.68] way it's like pretty simple um the other
[L1455] [52:48.80] piece is like how do I make sure that I
[L1456] [52:52.16] put in the work to ensure that I'm
[L1457] [52:54.24] creating a good PR um and so for me
[L1458] [52:58.08] that's like
[L1459] [53:00.96] I really should understand it's again it
[L1460] [53:03.20] sounds like a really not it really
[L1461] [53:05.44] sounds like a low bar but I should
[L1462] [53:07.52] understand like each line in the PR.
[L1463] [53:10.96] I know it's crazy. Um uh but also I do I
[L1464] [53:16.72] do try to um review each PR myself in
[L1465] [53:21.92] the GitHub UI. This is something I've
[L1466] [53:23.60] always found really helpful. Like if you
[L1467] [53:25.84] actually just like open up your PR and
[L1468] [53:28.48] click files and read through it as if
[L1469] [53:30.48] you were a reviewer, you tend to find
[L1470] [53:32.00] things that you would miss if you were
[L1471] [53:33.28] just looking at your local diff. I find
[L1472] [53:34.88] that very useful. And then the other is
[L1473] [53:37.92] trying to like encode skill. I guess
[L1474] [53:41.20] this is a little bit more in the first
[L1475] [53:42.48] category, but trying to encode skills um
[L1476] [53:45.68] or trying to encode in skills uh things
[L1477] [53:48.48] I'm contin consistently getting wrong
[L1478] [53:50.80] that the agent is getting wrong. Like I
[L1479] [53:52.32] had like a recent example would be I I
[L1480] [53:56.48] found that I was often getting feedback
[L1481] [53:58.16] on PRs that was of the form
[L1482] [54:02.56] what you know this condition here this
[L1483] [54:04.32] like if statement what case is this
[L1484] [54:06.96] intended to catch because if I comment
[L1485] [54:08.96] it out all the tests pass and so I was
[L1486] [54:12.00] like okay I should probably have a pass
[L1487] [54:14.40] before I put up any PR where I have the
[L1488] [54:17.52] agent like go through and check like are
[L1489] [54:19.76] these conditions still relevant or are
[L1490] [54:21.28] they left over from a product refactor
[L1491] [54:22.72] or something else. So, um I I don't
[L1492] [54:25.28] know. I'm not I'm still learning, but
[L1493] [54:27.36] those are some of the things I've been
[L1494] [54:28.64] doing. Yeah, it's again I think it's
[L1495] [54:30.32] like a it's a pretty hard time to be
[L1496] [54:31.60] like building software, but I felt for a
[L1497] [54:34.00] long time or I had a fear that AI was
[L1498] [54:36.80] going to make us more productive, but
[L1499] [54:40.00] that programming would be like a lot
[L1500] [54:41.44] less fun. Um because I just like love I
[L1501] [54:45.60] just like love programming. Um uh and I
[L1502] [54:49.36] was like, "Oh, now I'm going to have to
[L1503] [54:50.48] spend all my time like reviewing code
[L1504] [54:53.36] and like prompting this like idiot agent
[L1505] [54:56.80] to like that's like keeps getting things
[L1506] [54:58.56] wrong and like but ultimately like is
[L1507] [55:00.72] probably more productive." Um I actually
[L1508] [55:03.60] feel way better about that right now
[L1509] [55:05.52] than I did like a few months ago. And I
[L1510] [55:08.64] don't I don't exactly know why. Like I
[L1511] [55:10.88] think
[L1512] [55:12.48] I think it's because
[L1513] [55:15.44] well I think the agents getting better
[L1514] [55:17.04] and the tooling getting better and me
[L1515] [55:18.64] getting more comfortable with it is one
[L1516] [55:20.40] factor. I think the other is um I've
[L1517] [55:24.08] grown to appreciate more of
[L1518] [55:27.68] the the the kinds of things that like
[L1519] [55:29.76] working with agents has unlocked like
[L1520] [55:31.28] the cost of running an experiment is
[L1521] [55:32.96] incredibly low. There's so many things
[L1522] [55:34.72] I've wanted to try or like questions
[L1523] [55:36.96] I've wanted to answer that I could now
[L1524] [55:39.44] answer like almost instantly. Like I
[L1525] [55:42.40] like a sort of a dumb example, we UV in
[L1526] [55:45.52] UV um everything is snapshot tested. So
[L1527] [55:48.80] like basically all of our testing is
[L1528] [55:51.60] effectively
[L1529] [55:53.20] running UV and verifying the output.
[L1530] [55:56.16] That's how we test like basically the
[L1531] [55:57.52] entire program. Um and so that mean we
[L1532] [56:00.64] have a lot of tests that means we have a
[L1533] [56:02.32] lot of test output and the test output
[L1534] [56:06.00] is um it actually ends up in the test
[L1535] [56:09.12] files. So we have rust files like we
[L1536] [56:11.68] have a file called like lock rs that
[L1537] [56:14.40] tests all our UV lock. It's all our UV
[L1538] [56:16.40] lock tests and it's very very long in
[L1539] [56:18.40] part because it has all the lock output
[L1540] [56:20.40] snapshotted in the test. And I was like
[L1541] [56:22.56] hm like what if we stored the snapshots
[L1542] [56:25.20] in separate files?
[L1543] [56:27.44] like would that somehow make our like
[L1544] [56:30.40] compiles faster because then you don't
[L1545] [56:33.04] have technically that's like rust code
[L1546] [56:35.12] and so it's like would that all
[L1547] [56:36.48] disappear and like would that make like
[L1548] [56:38.16] our builds faster or blah blah blah and
[L1549] [56:41.44] I'd always want to do that but it
[L1550] [56:42.56] sounded like like to do that to do that
[L1551] [56:44.40] experiment as a human would be like
[L1552] [56:45.60] extremely painful because you have to
[L1553] [56:47.04] convert all of those tests and I just
[L1554] [56:49.12] had an agent do it in the background
[L1555] [56:50.00] while I did a bunch of other things and
[L1556] [56:51.04] I got a bunch of data on it and the
[L1557] [56:52.72] answer is no but but it's like I you
[L1558] [56:55.52] know what I mean like I I I mean, sorry,
[L1559] [56:57.68] the answer is a little bit more nuanced.
[L1560] [56:59.04] It actually does have a good impact if
[L1561] [57:00.80] um if you're just iterating on the
[L1562] [57:02.64] snapshot outputs, you no longer have to
[L1563] [57:04.40] recompile your program at all because
[L1564] [57:06.16] this outputs are stored somewhere else.
[L1565] [57:07.84] Anyway, that's the thing that makes a
[L1566] [57:09.20] difference on. But my point is I'm just
[L1567] [57:11.04] like running experiments like that like
[L1568] [57:12.56] all day like like trying things that
[L1569] [57:14.48] were used to be hard like used to cost a
[L1570] [57:17.20] lot to um to answer. Uh the work of then
[L1571] [57:21.12] going from that to like production,
[L1572] [57:22.88] there's still like real work there. Um,
[L1573] [57:25.28] but so you know, I think one piece is
[L1574] [57:28.32] the tools and the agents getting better.
[L1575] [57:29.92] The other is things that I just wouldn't
[L1576] [57:32.64] have been able to do before that I can
[L1577] [57:34.00] now do like incredibly easily. And then
[L1578] [57:36.80] um and then the third is I think I'm
[L1579] [57:39.44] more and more realizing that like a lot
[L1580] [57:40.80] of the value I get from building
[L1581] [57:42.24] software is not uh is retained because
[L1582] [57:47.52] some of it is like thinking hard about
[L1583] [57:49.20] like the not it doesn't have to be
[L1584] [57:50.80] typing out the code but it's like
[L1585] [57:52.08] thinking hard about like the layout of a
[L1586] [57:53.52] data structure. A lot of it is merging a
[L1587] [57:56.00] PR that closes a user issue. I get a lot
[L1588] [57:58.08] of satisfaction from actually like like
[L1589] [58:00.64] fixing and improving something. It's not
[L1590] [58:02.24] necessarily just from typing out the
[L1591] [58:03.60] code. So, I I do feel for people a lot
[L1592] [58:06.48] who
[L1593] [58:08.24] feel like they're losing something by
[L1594] [58:09.92] like working with agents because I do
[L1595] [58:11.76] feel that myself. Um, but I feel better
[L1596] [58:14.80] now than I did a few months ago about
[L1597] [58:18.56] my like like what it's like to work as a
[L1598] [58:21.68] software engineer with agents.
[L1599] [58:23.92] You mentioned in the like one of the
[L1600] [58:25.76] performance optimization examples you
[L1601] [58:27.92] said if you just unleash codecs it kind
[L1602] [58:30.16] of does this local optimizations and
[L1603] [58:31.92] it's very
[L1604] [58:32.96] >> good at that but it's not
[L1605] [58:34.88] >> great at kind of like some of the I mean
[L1606] [58:37.44] today it's more human ingenuity of like
[L1607] [58:39.68] system level um
[L1608] [58:41.76] >> optimizations and it kind of reminded me
[L1609] [58:44.48] of this tweet that you had you said it
[L1610] [58:47.04] says I I'm slightly concerned by how
[L1611] [58:49.84] much garbage I would be turnurning out
[L1612] [58:51.60] if I was trying to use these tools
[L1613] [58:53.68] without significant software engineering
[L1614] [58:55.68] experience.
[L1615] [58:57.44] >> I remain concerned about that.
[L1616] [58:58.96] >> Yeah, it it it reminds me and similar to
[L1617] [59:02.56] what uh the Mitchell Hashimoto tweet
[L1618] [59:05.04] that you said. It was like there's a
[L1619] [59:06.56] very big difference between Codex go and
[L1620] [59:09.52] do this versus um you know, you are like
[L1621] [59:13.20] wielding it like this tool and you're
[L1622] [59:14.88] kind of like proddding in the right
[L1623] [59:16.08] direction.
[L1624] [59:16.80] >> Yeah. Um, but yeah, I was curious your
[L1625] [59:19.12] thoughts on that because it seemed like
[L1626] [59:20.56] it went pretty viral and I think a lot
[L1627] [59:22.32] of people are thinking about that.
[L1628] [59:24.32] >> Like being a great software engineer is
[L1629] [59:26.96] like uh
[L1630] [59:30.00] like more like useful than ever. like I
[L1631] [59:32.56] I don't like it's um you know it's still
[L1632] [59:36.72] the case that I I think that the people
[L1633] [59:38.88] on our team who are like the strongest
[L1634] [59:41.44] like software have the strongest
[L1635] [59:43.04] engineering skills are like the most
[L1636] [59:44.72] effective like even at using agents um
[L1637] [59:48.00] and uh you know it's funny because
[L1638] [59:50.80] there's a lot of talk about like token
[L1639] [59:53.28] maxing I don't know if you're familiar
[L1640] [59:54.56] with this right yeah the idea of like
[L1641] [59:56.24] should you have a leaderboard for
[L1642] [59:57.68] example this is getting tweeted about a
[L1643] [59:59.36] lot companies that have token
[L1644] [01:00:00.40] leaderboards and it's like how do
[L1645] [01:00:02.08] like creates terrible incentives to just
[L1646] [01:00:04.24] like use as much tokens as possible. And
[L1647] [01:00:06.64] it's funny because we do uh that does
[L1648] [01:00:09.28] get tracked or sorry there's not a
[L1649] [01:00:11.68] leaderboard but like token usage is
[L1650] [01:00:14.08] something you can like look up for
[L1651] [01:00:15.52] example you know internally I mean and
[L1652] [01:00:17.84] um it's interesting to look at because I
[L1653] [01:00:20.00] I don't care like who on the team is
[L1654] [01:00:21.60] using the most tokens like and there are
[L1655] [01:00:24.16] people on the team who are like I'm like
[L1656] [01:00:25.76] actively trying not to care about that
[L1657] [01:00:28.16] like being where I am on the token
[L1658] [01:00:29.68] leaderboard which I think is like great
[L1659] [01:00:31.52] like I I don't care like they don't have
[L1660] [01:00:33.28] like they should just do like do a great
[L1661] [01:00:35.44] job and like that's fine. I don't care
[L1662] [01:00:36.72] if they use a lot of tokens or not. But
[L1663] [01:00:38.08] it is interesting to look at the token
[L1664] [01:00:39.60] leaderboard because um some of the
[L1665] [01:00:42.56] people on the team who are most
[L1666] [01:00:43.52] productive are like using like a lot of
[L1667] [01:00:45.84] tokens, right? It's like like there is
[L1668] [01:00:48.00] like a correlation. I'm not saying it's
[L1669] [01:00:49.20] causal, but I'm saying like I do think
[L1670] [01:00:51.04] that a lot of great engineers like are
[L1671] [01:00:53.60] able to like use agents very effectively
[L1672] [01:00:55.84] and like to hopefully to like multiply
[L1673] [01:00:57.60] their skills. Um, so I uh I do think it
[L1674] [01:01:02.96] would be like
[L1675] [01:01:05.12] really hard to be an early career
[L1676] [01:01:07.04] software engineer right now. And um I'm
[L1677] [01:01:11.04] not spending that much time with early
[L1678] [01:01:13.20] career engineers right now just based on
[L1679] [01:01:15.28] like at Astral we're just a very small
[L1680] [01:01:17.52] team um and we tended to hire very
[L1681] [01:01:19.52] senior. Um but uh it's it is sort of
[L1682] [01:01:25.20] hard for me to think about like what
[L1683] [01:01:27.68] what would we uh like how would I learn
[L1684] [01:01:30.80] basically like what would the iteration
[L1685] [01:01:32.48] loop be um I would be like learning from
[L1686] [01:01:36.88] codecs I guess um as opposed to
[L1687] [01:01:41.36] uh like
[L1688] [01:01:44.32] um
[L1689] [01:01:45.92] the other way around basically I mean
[L1690] [01:01:47.76] like like a lot of the times I'm
[L1691] [01:01:48.80] actually like instructing codecs right?
[L1692] [01:01:50.40] And like trying to correct it and
[L1693] [01:01:51.52] providing a safeguard on it. Um or opus
[L1694] [01:01:54.24] or whatever you're using. Um and so uh
[L1695] [01:01:57.68] yeah, I think I just don't know like
[L1696] [01:02:00.24] where you would get it would just be way
[L1697] [01:02:03.36] too easy to fall prey to like a lot of
[L1698] [01:02:05.92] the bad things that happen when you use
[L1699] [01:02:07.60] agents. You built this proof of concept
[L1700] [01:02:10.24] in uh in Rust and it was really
[L1701] [01:02:12.64] wellreceived, but why did you start a
[L1702] [01:02:15.52] company around it and how did the like
[L1703] [01:02:17.68] the raising go and all of that? What was
[L1704] [01:02:19.28] the motivation there?
[L1705] [01:02:20.72] >> Yeah. Yeah. So, um I left Spring um I
[L1706] [01:02:24.64] was actually convinced to leave by a
[L1707] [01:02:26.88] friend who uh very close friend who um
[L1708] [01:02:31.20] left Meta around the same time and he
[L1709] [01:02:33.52] was like, "We should start a company
[L1710] [01:02:34.56] together." And I was like, "Okay, fine."
[L1711] [01:02:36.64] Um I mean, it wasn't quite, you know,
[L1712] [01:02:38.88] that simple. Uh but uh but I did, you
[L1713] [01:02:41.76] know, I left and and then we we kind of
[L1714] [01:02:43.76] went into the, you know, the quote
[L1715] [01:02:45.04] unquote idea maze of like what do we
[L1716] [01:02:47.44] want to build? like we we went into it
[L1717] [01:02:49.20] not knowing what we wanted to build and
[L1718] [01:02:50.64] we spent a bunch of time exploring the
[L1719] [01:02:53.44] ven diagram of ideas of like there were
[L1720] [01:02:56.00] things he was interested in that I
[L1721] [01:02:57.76] thought was were not interesting and and
[L1722] [01:02:59.60] vice versa and there was some stuff in
[L1723] [01:03:01.84] the middle and we spent time exploring
[L1724] [01:03:03.76] the stuff in the middle but then in all
[L1725] [01:03:05.84] my spare time I was working on like
[L1726] [01:03:07.60] developer tools and because that's what
[L1727] [01:03:09.36] I thought was really interesting and he
[L1728] [01:03:10.72] it wasn't quite like a fit for him
[L1729] [01:03:12.64] basically um but around then I was
[L1730] [01:03:16.16] working on rough I was working on a a
[L1731] [01:03:17.92] couple other projects that you can see
[L1732] [01:03:19.84] in my GitHub that are like I don't know
[L1733] [01:03:22.40] probably not as interesting but they
[L1734] [01:03:23.76] were like I was like experimenting with
[L1735] [01:03:25.04] like lots of different things at the
[L1736] [01:03:26.24] time like I was pretty interested in web
[L1737] [01:03:28.16] assembly. Um I wrote a sort of like a
[L1738] [01:03:33.68] CI/CD
[L1739] [01:03:36.08] toolkit in Typescript. It's sort of like
[L1740] [01:03:38.24] you wrote pipelines in Typescript and it
[L1741] [01:03:40.08] transpiled them to Docker. And I was
[L1742] [01:03:41.68] like, "Oh, this could be cool." Like,
[L1743] [01:03:42.80] well, I don't know. I was like building
[L1744] [01:03:43.92] a lot of stuff. And at that point in
[L1745] [01:03:47.04] time, I I decided I wanted to start
[L1746] [01:03:49.52] developing relationships with investors,
[L1747] [01:03:52.00] but that I wasn't ready to raise money
[L1748] [01:03:53.52] because I didn't know what I was
[L1749] [01:03:54.32] actually going to build. And so, my
[L1750] [01:03:55.60] thinking was I'm going to try to like
[L1751] [01:03:57.20] get connected to some people who like to
[L1752] [01:03:59.28] invest in this kind of stuff. Um, with
[L1753] [01:04:01.76] an eye towards reaching back out to them
[L1754] [01:04:03.68] in like like 3 to six months and being
[L1755] [01:04:06.32] like, "Hey, we had a great conversation.
[L1756] [01:04:07.76] Now I'm working on X." So, that was my
[L1757] [01:04:10.08] thinking. So I got connected to a couple
[L1758] [01:04:12.24] investors who invest in inf like
[L1759] [01:04:14.00] software infrastructure and developer
[L1760] [01:04:15.20] tools. Um and I had some good
[L1761] [01:04:18.64] conversations and then like the problem
[L1762] [01:04:20.48] is things just can move really quickly
[L1763] [01:04:22.88] and so I didn't actually expect to like
[L1764] [01:04:24.72] start raising so soon but I effectively
[L1765] [01:04:27.44] got convinced and and at the same time
[L1766] [01:04:29.44] rough was growing a lot and so I
[L1767] [01:04:31.44] effectively got convinced that there was
[L1768] [01:04:33.04] enough there to start a company which is
[L1769] [01:04:34.72] a very interesting process. I was like I
[L1770] [01:04:36.96] was like I don't know quite know how
[L1771] [01:04:38.32] this becomes a company but I was
[L1772] [01:04:40.24] effectively convinced that there was
[L1773] [01:04:42.32] enough there to build a company which is
[L1774] [01:04:44.40] interesting
[L1775] [01:04:44.80] >> by the investors.
[L1776] [01:04:45.92] >> Yeah.
[L1777] [01:04:46.64] >> Yeah. Yeah.
[L1778] [01:04:47.92] >> Um which I'm grateful for.
[L1779] [01:04:51.20] >> The other thing I was convinced of um uh
[L1780] [01:04:54.24] was uh uh which is funny is um if I
[L1781] [01:04:59.12] hated it, I could stop in like six
[L1782] [01:05:01.60] months. It's like if you decide it's not
[L1783] [01:05:03.44] for you, you could like give the money
[L1784] [01:05:04.64] back. actually said that.
[L1785] [01:05:06.00] >> Yes. Which I actually think was
[L1786] [01:05:07.12] brilliant cuz like I was probably never
[L1787] [01:05:08.80] going to do that but it did make me feel
[L1788] [01:05:10.96] like there was less pressure.
[L1789] [01:05:13.68] Um so uh sorry very round very very like
[L1790] [01:05:16.64] weird roundabout details but um but
[L1791] [01:05:18.88] basically like uh I was like working on
[L1792] [01:05:22.16] rough more like full-time eventually and
[L1793] [01:05:24.80] then um uh it was kind of like uh I
[L1794] [01:05:28.72] would say collaborative with like the
[L1795] [01:05:30.24] potential early investors where it was
[L1796] [01:05:32.08] like we would just have like long
[L1797] [01:05:33.20] conversations about like my ideas and
[L1798] [01:05:34.96] then um it basically become clear that
[L1799] [01:05:36.96] it was like there's enough here like you
[L1800] [01:05:38.88] and I like wrote out kind of like a
[L1801] [01:05:40.24] product roadmap which honestly like a
[L1802] [01:05:42.32] lot of it stayed true to like what we
[L1803] [01:05:43.76] ended up building um what we've ended up
[L1804] [01:05:46.08] building so far at least and um and from
[L1805] [01:05:49.92] there it basically became like uh yeah
[L1806] [01:05:52.00] we want to fund you like here are the
[L1807] [01:05:53.60] terms that we would do and I was like oh
[L1808] [01:05:55.20] wow okay so I guess this is happening so
[L1809] [01:05:58.08] so uh it was it was just an interesting
[L1810] [01:06:00.40] and I had never done anything like this
[L1811] [01:06:02.64] before I mean I was just I was just you
[L1812] [01:06:05.04] know an IC software engineer my whole
[L1813] [01:06:06.64] career um and then I uh suddenly I was
[L1814] [01:06:08.88] like starting a company and Um,
[L1815] [01:06:12.88] it's funny cuz I actually think like the
[L1816] [01:06:16.08] decision to like go all in and like
[L1817] [01:06:18.32] start the company
[L1818] [01:06:21.12] wasn't that stressful. I actually think
[L1819] [01:06:23.52] a lot of the stress came later as the
[L1820] [01:06:26.40] company started to succeed. Um because
[L1821] [01:06:28.40] at the beginning I had I kind of had
[L1822] [01:06:29.84] nothing to lose. But then as the company
[L1823] [01:06:32.32] started to succeed um you know I was
[L1824] [01:06:34.96] like oh wow like the company's kind of
[L1825] [01:06:36.48] working like what's going to happen from
[L1826] [01:06:37.92] here and I had a team of 20 people who
[L1827] [01:06:41.20] were depending on me and so um I don't
[L1828] [01:06:43.76] know just for me as a founder it was
[L1829] [01:06:45.28] like um I'm pretty like riskaverse but I
[L1830] [01:06:48.08] actually found that starting the company
[L1831] [01:06:50.08] was
[L1832] [01:06:51.68] uh an easier it was it was an easier
[L1833] [01:06:54.48] decision than maybe some of the
[L1834] [01:06:55.92] stressful things that came later uh to
[L1835] [01:06:58.08] navigate. Um, but it happened very
[L1836] [01:07:01.12] quickly and sort of unintentionally and
[L1837] [01:07:03.68] in in a symbiotic way with investors
[L1838] [01:07:06.64] which was which I I I hadn't really
[L1839] [01:07:08.40] anticipated.
[L1840] [01:07:09.68] >> I didn't expect the the investors I mean
[L1841] [01:07:12.64] cuz I thought the founders hungry for
[L1842] [01:07:14.80] the fundraising and go please fund me
[L1843] [01:07:17.20] but the investors were like
[L1844] [01:07:19.36] >> I think it can happen a million
[L1845] [01:07:20.40] different ways and like
[L1846] [01:07:22.56] >> um
[L1847] [01:07:24.00] >> actually I mean we did three fundraises.
[L1848] [01:07:26.00] We did a C series A and a series B. Um,
[L1849] [01:07:29.76] we actually never even announced the
[L1850] [01:07:32.08] series A or the series B. They were I
[L1851] [01:07:34.64] mean they were announced in the
[L1852] [01:07:36.00] acquisition blog post, but we sort of
[L1853] [01:07:38.72] complicated. It's like we we basically
[L1854] [01:07:40.40] just never got around to it. Um, and uh
[L1855] [01:07:43.36] >> why don't you guys publish it? Because
[L1856] [01:07:44.56] isn't that good marketing for talent?
[L1857] [01:07:46.96] >> It's good marketing, but basically like
[L1858] [01:07:49.20] we there kept being like reasons that we
[L1859] [01:07:51.68] like wanted to wait a little bit and
[L1860] [01:07:53.76] it's also like to me it always felt like
[L1861] [01:07:56.00] a lot of work. And then I was like, it
[L1862] [01:07:58.64] just never I honestly just never felt
[L1863] [01:08:00.24] like the most important thing because we
[L1864] [01:08:01.92] were like building a lot of stuff and
[L1865] [01:08:03.52] like the company was going well and I
[L1866] [01:08:05.12] was like I don't we don't need the
[L1867] [01:08:07.68] marketing. Uh we did finally plan to
[L1868] [01:08:10.16] announce it but then we got bought so
[L1869] [01:08:12.08] didn't happen. But um but uh each of
[L1870] [01:08:15.68] those
[L1871] [01:08:18.00] each of those fundraises was um uh was
[L1872] [01:08:21.44] like preemptive basically like like
[L1873] [01:08:23.68] initiated by investors. Um which was uh
[L1874] [01:08:27.20] which is like uh I mean it's like
[L1875] [01:08:28.80] fortunate because like the company was
[L1876] [01:08:30.32] like going well and people wanted to
[L1877] [01:08:31.84] invest. Um but it was also just like a
[L1878] [01:08:35.04] funny position to for me to be in I
[L1879] [01:08:37.20] guess. Um, uh, I think I, uh, I think I
[L1880] [01:08:40.96] was just always a little bit
[L1881] [01:08:41.76] conservative and I wasn't super
[L1882] [01:08:44.00] aggressive about trying to go out and
[L1883] [01:08:45.28] raise money. Um, and, uh, but but we
[L1884] [01:08:48.24] were lucky enough to be building things
[L1885] [01:08:49.36] that people really, um, had a lot of
[L1886] [01:08:51.20] confidence in or had a lot of belief in.
[L1887] [01:08:53.04] >> That probably gave you a lot of
[L1888] [01:08:54.40] negotiating leverage because like one of
[L1889] [01:08:57.28] the best positions you'd be in is that
[L1890] [01:08:59.44] you you're willing to walk away. You
[L1891] [01:09:01.92] don't need it. And by definition, you
[L1892] [01:09:03.60] didn't even come there to begin with.
[L1893] [01:09:04.96] They came to you and said, "Please take
[L1894] [01:09:06.56] the money."
[L1895] [01:09:08.00] >> That's true. Yeah. Yeah. I wouldn't say
[L1896] [01:09:09.60] I'm a great negotiator, but um yeah, I
[L1897] [01:09:12.40] guess at least I had a strong hand. But
[L1898] [01:09:14.64] we were very lucky with investors. We
[L1899] [01:09:16.08] had we had amazing investors. Um like
[L1900] [01:09:18.48] super supportive and really like aligned
[L1901] [01:09:21.92] with how I wanted to build the company.
[L1902] [01:09:24.24] Um like never any
[L1903] [01:09:28.16] conflict, never any like pressure to do
[L1904] [01:09:30.88] anything specific. um like just support
[L1905] [01:09:34.08] and um maybe the only thing maybe the
[L1906] [01:09:37.52] only piece of consistent feedback is
[L1907] [01:09:38.96] that I could have been more aggressive
[L1908] [01:09:41.76] uh and but I I don't know it's like uh
[L1909] [01:09:43.84] just in terms of like scaling and
[L1910] [01:09:45.20] growing and doing more but I liked the
[L1911] [01:09:47.36] way that we operated and um yeah we just
[L1912] [01:09:49.76] had such good we had such good
[L1913] [01:09:51.12] experiences with our investors too so I
[L1914] [01:09:52.64] felt lucky about that because it can
[L1915] [01:09:54.24] easily go the other way. I imagine if
[L1916] [01:09:56.88] someone invests there's a promise of
[L1917] [01:09:58.80] future revenue but how how does this
[L1918] [01:10:01.52] company make money because you guys give
[L1919] [01:10:03.68] away your software for free right so
[L1920] [01:10:05.44] >> yeah we launched a commercial product in
[L1921] [01:10:08.48] like August of last year
[L1922] [01:10:12.16] >> um and it was sort of it was called py
[L1923] [01:10:15.28] it was kind of like a hosted
[L1924] [01:10:17.52] um counterpart to UV so like a lot of
[L1925] [01:10:21.04] our a lot of UV users will purchase like
[L1926] [01:10:23.28] a private registry software instead of
[L1927] [01:10:25.44] using in the public registries either
[L1928] [01:10:26.80] for like security or maybe they need to
[L1929] [01:10:29.04] publish their own private artifacts,
[L1930] [01:10:30.64] things like that. And we basically built
[L1931] [01:10:32.88] our own private registry that had some
[L1932] [01:10:34.72] first class support for you for UV. Um,
[L1933] [01:10:37.84] and it let us solve a bunch of problems
[L1934] [01:10:40.08] that we saw, you know, in our issue
[L1935] [01:10:41.68] tracker around users using other
[L1936] [01:10:43.68] solutions. Um, also let us build
[L1937] [01:10:45.92] something really fast because we like
[L1938] [01:10:47.36] vertically integrated the client and the
[L1939] [01:10:49.44] server. There were like special things
[L1940] [01:10:51.04] they could do to be like really fast and
[L1941] [01:10:52.64] really easy to use and and all that. And
[L1942] [01:10:55.44] we spent a while um selling that uh and
[L1943] [01:11:00.48] um our revenue actually grew like pretty
[L1944] [01:11:02.24] well. Um I mean it wasn't like I think
[L1945] [01:11:05.12] in this era of AI you're constantly
[L1946] [01:11:06.72] hearing about fastest company to go to
[L1947] [01:11:08.40] 100 million in revenue and and things
[L1948] [01:11:10.08] like that. It wasn't it didn't look like
[L1949] [01:11:11.60] that. Um but we were definitely able to
[L1950] [01:11:13.44] sell this to like some big enterprises.
[L1951] [01:11:15.28] Um and I mean the cool thing was we had
[L1952] [01:11:17.44] very good because we built the open
[L1953] [01:11:19.44] source and everyone was using our open
[L1954] [01:11:21.28] source. We had a really good funnel like
[L1955] [01:11:24.88] like we had a small number of extremely
[L1956] [01:11:26.80] high quality coh customers is the way I
[L1957] [01:11:29.84] would put it. Um so the general idea for
[L1958] [01:11:33.20] like how we wanted to make money was
[L1959] [01:11:35.84] keep uh like build open source and like
[L1960] [01:11:38.56] the tooling the tooling remains like
[L1961] [01:11:40.56] free open- source like entirely
[L1962] [01:11:42.72] non-commercial and then we build
[L1963] [01:11:44.80] software that's kind of like the natural
[L1964] [01:11:46.24] next thing you need when you're using
[L1965] [01:11:47.52] our tooling. So if you're using UV you
[L1966] [01:11:50.08] there are probably sol problem there are
[L1967] [01:11:51.76] likely problems we can solve for you
[L1968] [01:11:53.12] with like a private registry. Um and
[L1969] [01:11:55.04] then the funnel is like people using UV
[L1970] [01:11:57.20] they have these problems and then we
[L1971] [01:11:58.48] sell them the registry and the registry
[L1972] [01:12:00.32] was meant to be like one piece of a
[L1973] [01:12:02.24] platform of like a bunch of different
[L1974] [01:12:03.68] things we sell like a Python cloud. Um,
[L1975] [01:12:06.48] so that's what we were like building
[L1976] [01:12:07.76] towards. Um, uh, I mean part of the cool
[L1977] [01:12:11.04] thing about the, um, acquisition is
[L1978] [01:12:16.16] we'll be able to take parts of that
[L1979] [01:12:19.04] platform and make it basically freely
[L1980] [01:12:21.28] available. Um like we did just as an
[L1981] [01:12:24.72] example a a big part of that was um
[L1982] [01:12:29.68] uh we did a lot of like in Python um you
[L1983] [01:12:33.68] know there's a big part of the community
[L1984] [01:12:34.80] that uses Python with GPUs like PyTorch
[L1985] [01:12:37.52] and and then there's like a whole
[L1986] [01:12:39.44] ecosystem around PyTorch of like
[L1987] [01:12:41.12] software that kind of like builds
[L1988] [01:12:42.88] against PyTorch. Um and we that's for a
[L1989] [01:12:46.96] variety of reasons the ergonomics around
[L1990] [01:12:48.96] that are are not great. um like it can
[L1991] [01:12:52.40] be kind of hard to work with, hard to
[L1992] [01:12:54.56] install, hard to get hard to install the
[L1993] [01:12:56.48] right version. Depends on the GPU that
[L1994] [01:12:58.40] you have and like what version of CUDA
[L1995] [01:13:00.08] you have installed and like all this
[L1996] [01:13:01.28] stuff. And so we we kind of tried to
[L1997] [01:13:03.52] solve that in a in a certain way. Um
[L1998] [01:13:06.64] where we built our own distribution, you
[L1999] [01:13:09.36] could think of it kind of like a Linux
[L2000] [01:13:10.48] in the sense of like a Linux
[L2001] [01:13:11.36] distribution like we pre-built a lot of
[L2002] [01:13:12.96] things like that that all worked
[L2003] [01:13:14.16] together and made that available to
[L2004] [01:13:15.76] customers. And so now we can actually
[L2005] [01:13:17.60] take that and just make that like freely
[L2006] [01:13:19.12] available to everyone because we're no
[L2007] [01:13:21.04] longer uh we no longer are trying to
[L2008] [01:13:23.60] build like an independent business.
[L2009] [01:13:24.88] We're just trying to build uh great
[L2010] [01:13:26.80] tools that like grow a broader
[L2011] [01:13:28.24] ecosystem. So I mean more more to come
[L2012] [01:13:30.80] on that, but that's been kind of like
[L2013] [01:13:32.00] one cool thing that I'm I'm excited
[L2014] [01:13:33.60] about. as a first-time founder,
[L2015] [01:13:36.00] especially with the engineering
[L2016] [01:13:37.20] background, was there anything that kind
[L2017] [01:13:39.44] of like a surprising learning or
[L2018] [01:13:41.60] something where you would share that
[L2019] [01:13:43.52] with someone if they were an engineer
[L2020] [01:13:44.88] and they were going down that founder
[L2021] [01:13:46.56] path?
[L2022] [01:13:48.32] >> There are so many different ways to do
[L2023] [01:13:49.84] it. Like I I'm actually like not a huge
[L2024] [01:13:53.12] fan of people giving startup advice in
[L2025] [01:13:55.04] general because so much of this industry
[L2026] [01:13:57.68] is like um survivorship bias of like you
[L2027] [01:14:02.56] could give the exact same advice to like
[L2028] [01:14:04.56] you know like basically you can go to
[L2029] [01:14:05.92] like two talks and people give you like
[L2030] [01:14:07.28] two like incredibly successful founders
[L2031] [01:14:08.80] give you like completely contradictory
[L2032] [01:14:10.08] advice and you're like I don't really
[L2033] [01:14:11.12] know what to do. Um and I I tend to view
[L2034] [01:14:13.44] that as like you've got to figure out
[L2035] [01:14:14.96] what's true to you. Um, and so, you
[L2036] [01:14:17.92] know, like there's all these decisions
[L2037] [01:14:19.20] you have to make like in person versus
[L2038] [01:14:20.80] remote, right? Like have a principle and
[L2039] [01:14:24.64] like stick to it. Like either one can be
[L2040] [01:14:27.68] great. Like we built the whole company
[L2041] [01:14:29.12] remotely. It went super well. Like it
[L2042] [01:14:31.20] was great. Um, do I think there are
[L2043] [01:14:32.80] benefits to being in person? Of course.
[L2044] [01:14:34.48] Um, would I have been able to hire the
[L2045] [01:14:36.24] team that we put together if we were in
[L2046] [01:14:37.60] person? Absolutely not. And so like, you
[L2047] [01:14:39.44] know, there are trade-offs to all these
[L2048] [01:14:40.64] things. You just have to like be
[L2049] [01:14:41.76] principled and figure out like what's
[L2050] [01:14:43.36] what resonates with you. um you know
[L2051] [01:14:46.32] like uh and there's there's like a
[L2052] [01:14:48.16] million of those decisions that you have
[L2053] [01:14:49.44] to think through. I feel fortunate in a
[L2054] [01:14:51.44] lot of the ways I got to run the
[L2055] [01:14:52.56] company. Like I I tried to spend like
[L2056] [01:14:54.16] very minimal time fundraising and with
[L2057] [01:14:57.20] investors and I tried to optimize for
[L2058] [01:14:59.44] investors I really trusted as opposed to
[L2059] [01:15:02.56] trying to talk to a billion different
[L2060] [01:15:04.80] investors and like pit them all against
[L2061] [01:15:06.32] each other to get the best terms. like
[L2062] [01:15:07.68] my my goal was always like find a
[L2063] [01:15:09.44] partner that I really trust and get good
[L2064] [01:15:10.88] terms and then move quickly to spend as
[L2065] [01:15:12.56] little time on fundraising as possible.
[L2066] [01:15:14.72] Um, and so, you know, think about think
[L2067] [01:15:17.28] about what you care about and focus on
[L2068] [01:15:19.20] that. There's no right answer to a lot
[L2069] [01:15:20.96] of this stuff. I got a lot of advice to
[L2070] [01:15:23.68] get a co-founder when I first started
[L2071] [01:15:25.68] the company and I basically ignored
[L2072] [01:15:28.56] that. I mean, I I like Well, sorry. I
[L2073] [01:15:30.96] did ignore it because I didn't get a
[L2074] [01:15:32.00] co-founder, I guess. But like I for me,
[L2075] [01:15:35.04] it was kind of like um
[L2076] [01:15:37.76] uh I kind of knew they were right
[L2077] [01:15:40.32] probably, but I didn't really have
[L2078] [01:15:43.04] someone in mind. I didn't want to force
[L2079] [01:15:44.24] it and so I just didn't. And um you
[L2080] [01:15:47.28] know, over time I felt like it would
[L2081] [01:15:48.88] have been helpful
[L2082] [01:15:50.72] to have someone to uh that's kind of
[L2083] [01:15:53.28] like in like in the trenches with you in
[L2084] [01:15:55.20] the same way. Um, but you know, you find
[L2085] [01:15:57.52] other ways to acco um to compensate for
[L2086] [01:16:00.32] it. Like I don't know, I lean on my wife
[L2087] [01:16:02.80] a lot, probably more than I, you know,
[L2088] [01:16:04.64] more than I should. Um, probably more
[L2089] [01:16:06.72] open with my employees than I otherwise
[L2090] [01:16:08.48] would be, which is, I think, which can
[L2091] [01:16:10.72] be good or bad, but it's like I share a
[L2092] [01:16:12.72] lot with of, you know, with with the
[L2093] [01:16:14.16] early team, like especially when I need
[L2094] [01:16:15.68] advice on things. Um, try to build a
[L2095] [01:16:18.16] network of like other founders. Um,
[L2096] [01:16:20.00] especially here in New York, I have like
[L2097] [01:16:21.28] a pretty good group of um, there's like
[L2098] [01:16:23.20] six or seven of us who we try to get
[L2099] [01:16:25.12] dinner twice a year. Doesn't sound like
[L2100] [01:16:27.28] a lot, but everyone's busy.
[L2101] [01:16:28.80] >> Yeah. Yeah. Yeah.
[L2102] [01:16:30.16] >> Um and and that's been like a really um
[L2103] [01:16:33.44] Yeah, that's been like a really helpful
[L2104] [01:16:34.80] like support system. So, you just find
[L2105] [01:16:36.72] other ways to to compensate, but um
[L2106] [01:16:40.16] yeah, it's uh I don't know, there's no I
[L2107] [01:16:42.48] really don't I really think there's not
[L2108] [01:16:44.24] one right way to do it. Um
[L2109] [01:16:47.84] yeah, and it extends everywhere. I mean
[L2110] [01:16:49.52] like also I don't know everyone on X is
[L2111] [01:16:52.00] talking about like um you know like
[L2112] [01:16:55.28] should everyone in your company be
[L2113] [01:16:56.64] working seven days a week this kind of
[L2114] [01:16:58.56] thing and it's like
[L2115] [01:17:01.12] I don't know like we just built a very
[L2116] [01:17:02.72] different company and we were able to do
[L2117] [01:17:03.84] it like that was not I mean I work I
[L2118] [01:17:06.88] work basically all the time um and
[L2119] [01:17:09.20] that's a choice I made um and that I'm
[L2120] [01:17:12.56] like very happy with but I don't expect
[L2121] [01:17:14.64] people on the team to work all the time
[L2122] [01:17:16.16] and I want it to be a company where um
[L2123] [01:17:19.44] you know you can be highly highly
[L2124] [01:17:21.36] successful working normal hours um but
[L2125] [01:17:24.72] also where you're rewarded for you know
[L2126] [01:17:27.20] your output and your performance um and
[L2127] [01:17:29.12] I try to keep all those things in sync
[L2128] [01:17:30.72] but like again there's no one right one
[L2129] [01:17:32.96] way to do it there's no one right way to
[L2130] [01:17:35.28] do it like other companies that is their
[L2131] [01:17:37.60] culture and that's what they want to do
[L2132] [01:17:38.80] and like sure whatever like if that's
[L2133] [01:17:40.16] what you sign up for like just make sure
[L2134] [01:17:41.52] that you're honest about like what
[L2135] [01:17:42.72] you're doing so I don't know I just
[L2136] [01:17:44.40] think figure out what you care about and
[L2137] [01:17:47.52] in my opinion And don't focus too much
[L2138] [01:17:49.12] on how you think you should be doing
[L2139] [01:17:51.04] things. Think about how you want to be
[L2140] [01:17:52.80] doing things and what actually fits with
[L2141] [01:17:54.32] how you want to work.
[L2142] [01:17:55.84] >> What's your top book recommendation?
[L2143] [01:17:57.92] Whether technical or maybe something
[L2144] [01:17:59.76] that helped you as a founder.
[L2145] [01:18:01.68] >> I don't read a lot of like technical
[L2146] [01:18:04.40] material. I have definitely watched a
[L2147] [01:18:06.80] few talks that were very influential to
[L2148] [01:18:09.04] me, which is a little bit different.
[L2149] [01:18:10.72] >> What are those talks?
[L2150] [01:18:13.12] the Zigg creator uh Andrew Kelly um had
[L2151] [01:18:17.36] a really good talk about like data
[L2152] [01:18:18.56] oriented design that like I learned a
[L2153] [01:18:20.64] lot from. I mean even apart from
[L2154] [01:18:22.16] learning things, it sort of inspired me
[L2155] [01:18:23.52] to like look at software quite
[L2156] [01:18:24.88] differently. Um and so I think about
[L2157] [01:18:26.56] that talk a lot. Um interesting.
[L2158] [01:18:28.64] >> Yeah, things like that.
[L2159] [01:18:30.00] >> It's really good. Yeah, it's about um
[L2160] [01:18:32.24] well, I haven't watched it in a while,
[L2161] [01:18:33.44] so I'm probably mess it up, but it's
[L2162] [01:18:35.12] like uh a lot of it's about basically
[L2163] [01:18:37.36] design decisions they made in like the
[L2164] [01:18:38.64] Zig compiler and um and uh just like
[L2165] [01:18:42.64] thinking about like memory and
[L2166] [01:18:43.60] allocation and all this stuff. And I was
[L2167] [01:18:45.20] like, I watched that when I was pretty
[L2168] [01:18:46.64] early in my career of like systems
[L2169] [01:18:48.00] programming and I was like, "Wow, like
[L2170] [01:18:50.56] these people really care about what
[L2171] [01:18:52.00] they're doing." And I was like, "That's
[L2172] [01:18:53.20] cool."
[L2173] [01:18:55.60] Yeah.
[L2174] [01:18:56.56] >> Yeah. And then last question is, if you
[L2175] [01:18:59.20] could go back to the beginning of your
[L2176] [01:19:00.56] career, like right when you graduated
[L2177] [01:19:02.24] college, what advice would you give
[L2178] [01:19:04.00] yourself knowing what you know now?
[L2179] [01:19:07.60] >> I don't know. It's so hard to give
[L2180] [01:19:08.80] myself advice without feeling like I
[L2181] [01:19:10.24] have all this hindsight bias, you know?
[L2182] [01:19:11.84] I mean, I think
[L2183] [01:19:14.08] I guess I guess there are some things
[L2184] [01:19:15.52] where I'd basically like tell myself
[L2185] [01:19:17.52] that it is the right decision and I
[L2186] [01:19:20.32] shouldn't worry so much, but it's hard
[L2187] [01:19:22.08] to know how that would have played out,
[L2188] [01:19:23.76] you know, if I did it a thousand times
[L2189] [01:19:25.44] over. Um, but for example, like I think
[L2190] [01:19:27.68] when I left school and I went to work at
[L2191] [01:19:30.24] Khan Academy, part of me was definitely
[L2192] [01:19:32.72] like, wow, should I be taking more of
[L2193] [01:19:34.56] like a big tech job and am I going to
[L2194] [01:19:36.96] really regret not having that experience
[L2195] [01:19:39.04] or like um or like I mean the like like
[L2196] [01:19:45.12] the the Khan Academy like pay was good,
[L2197] [01:19:47.36] but it was like the big tech pay was was
[L2198] [01:19:48.96] certainly like better and I was seeing
[L2199] [01:19:50.24] my friends get like huge bonuses and
[L2200] [01:19:51.92] like all this stuff and I was like I
[L2201] [01:19:53.20] felt sort of insecure about should I be
[L2202] [01:19:55.20] doing that and I think it actually, you
[L2203] [01:19:57.60] know, in the long term really paid off.
[L2204] [01:19:59.92] Like I think I mean maybe it would have
[L2205] [01:20:01.36] been great but like the experience I had
[L2206] [01:20:02.80] was really what I wanted and I thought I
[L2207] [01:20:05.36] made that decision for the right reason.
[L2208] [01:20:06.80] So I think some of these things are like
[L2209] [01:20:10.64] I don't know everything happens for a
[L2210] [01:20:13.36] reason you know and it's like have some
[L2211] [01:20:16.16] faith in like what you're doing for the
[L2212] [01:20:17.68] right you know for the uh if you're
[L2213] [01:20:20.48] making decisions based on principles
[L2214] [01:20:22.16] like I think it can it can work out.
[L2215] [01:20:24.48] when we started this conversation, you
[L2216] [01:20:26.08] said, you know, the the reason you got
[L2217] [01:20:28.24] into what you got into is because you
[L2218] [01:20:30.08] tried all these different ecosystems and
[L2219] [01:20:32.00] you had a a broader perspective. I
[L2220] [01:20:34.80] imagine if you went to Google and you
[L2221] [01:20:37.60] just kind of I don't know used Google's
[L2222] [01:20:40.32] closed thing and then you might not have
[L2223] [01:20:42.32] had the same insight.
[L2224] [01:20:43.68] >> Yeah. And you know I I I I think about
[L2225] [01:20:46.16] this with Spring too because Spring like
[L2226] [01:20:48.08] I was there for four and a half years
[L2227] [01:20:49.92] and um and then I left right as they
[L2228] [01:20:53.68] decided to do like you know like a pivot
[L2229] [01:20:55.76] and then they ended up uh like joining
[L2230] [01:20:57.92] Janentech. But we had set out to build
[L2231] [01:21:00.24] like this kind of crazy drug discovery
[L2232] [01:21:03.68] company. We were focused on aging and it
[L2233] [01:21:06.00] was all with like computer vision. It
[L2234] [01:21:07.76] was like very very ambitious what we
[L2235] [01:21:09.20] were trying to do. Yeah. Yeah. And then
[L2236] [01:21:11.04] afterwards I was like ah like the
[L2237] [01:21:12.64] company didn't like it didn't have like
[L2238] [01:21:14.64] the huge exit or like the huge you know
[L2239] [01:21:16.96] we didn't achieve like all of our dreams
[L2240] [01:21:18.48] like did I waste all my time and
[L2241] [01:21:21.44] ultimately I was like no because I
[L2242] [01:21:24.16] learned by being an early employee even
[L2243] [01:21:26.40] and like seeing all these stages I
[L2244] [01:21:28.00] learned so much about how to run like my
[L2245] [01:21:29.60] own company and also all the technical
[L2246] [01:21:31.76] learnings that I rolled into my own
[L2247] [01:21:33.20] company. So again I feel bad I feel
[L2248] [01:21:35.92] weird giving this advice because it's
[L2249] [01:21:37.28] like everything work everything has
[L2250] [01:21:38.72] worked out really well. But I like I I
[L2251] [01:21:41.36] feel like there are moments in time
[L2252] [01:21:42.56] where I sort of doubted some of my
[L2253] [01:21:44.00] career decisions. And then in hindsight,
[L2254] [01:21:46.00] like you can only connect the dots
[L2255] [01:21:47.52] looking backwards. Like it like
[L2256] [01:21:48.96] everything kind of added up to finding
[L2257] [01:21:51.28] the thing I really love, which is like
[L2258] [01:21:52.72] building tools and um and feeding into
[L2259] [01:21:55.04] that.
[L2260] [01:21:56.00] >> Awesome. Well, thank you so much for
[L2261] [01:21:57.44] your time, Charlie. I really appreciate
[L2262] [01:21:58.48] it.
[L2263] [01:21:58.72] >> Yeah, thank you. No, it was super fun.
[L2264] [01:22:00.72] >> Hey, thank you for watching this
[L2265] [01:22:01.84] podcast. If you liked it and you want to
[L2266] [01:22:03.52] see the show grow, please support with a
[L2267] [01:22:05.76] comment or a like. Also, if you have any
[L2268] [01:22:08.64] recommendations for people you want me
[L2269] [01:22:10.32] to bring on, please drop a comment.
[L2270] [01:22:12.96] Guests like Barbara Liskoff, Mike
[L2271] [01:22:15.12] Stonereaker, Mark Brooker, these were
[L2272] [01:22:17.52] all people that I brought on because
[L2273] [01:22:19.52] someone left a comment. On another note,
[L2274] [01:22:21.76] aside from the podcast, I'm working on
[L2275] [01:22:23.68] building the ergonomic keyboard that I
[L2276] [01:22:25.60] wish existed. Here's a glance at the
[L2277] [01:22:27.76] prototype. It's a split keyboard, so
[L2278] [01:22:30.00] there's two sides. Um, this is in the
[L2279] [01:22:32.16] case, but yeah, we launched on
[L2280] [01:22:33.68] Kickstarter and we hit our goal within
[L2281] [01:22:35.68] eight hours of launching. I really
[L2282] [01:22:37.44] appreciate it if you were one of the
[L2283] [01:22:38.64] people who grabbed one of the early
[L2284] [01:22:40.24] units. Um, we're now working on the long
[L2285] [01:22:42.56] journey of building the tooling now and
[L2286] [01:22:44.64] so if you still want to pick one up,
[L2287] [01:22:46.32] I've left the late pledges open on
[L2288] [01:22:48.40] Kickstarter, so you can grab one there.
[L2289] [01:22:50.56] I'll put a link in the description.
[L2290] [01:22:52.56] Thank you again for watching the podcast
[L2291] [01:22:54.88] and I'll see you in the next
