Chunk 3; segments 646–982. Start may repeat the previous chunk for context.

# Creator of uv, ty, Ruff: How Software Engineering Is Changing | Charlie Marsh

Source ID: source-e744e4ed615158a6
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_uv,_ty,_Ruff_How_Software_Engineering_Is_Changing_Charlie_Marsh_en.txt
Video: https://www.youtube.com/watch?v=Iw65FD4MGgs

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
