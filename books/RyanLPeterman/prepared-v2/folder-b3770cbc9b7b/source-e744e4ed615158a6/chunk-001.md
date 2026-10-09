Chunk 1; segments 1–326. 

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
