Chunk 2; segments 319–653. Start may repeat the previous chunk for context.

# Creator of uv, ty, Ruff: How Software Engineering Is Changing | Charlie Marsh

Source ID: source-e744e4ed615158a6
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_uv,_ty,_Ruff_How_Software_Engineering_Is_Changing_Charlie_Marsh_en.txt
Video: https://www.youtube.com/watch?v=Iw65FD4MGgs

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
