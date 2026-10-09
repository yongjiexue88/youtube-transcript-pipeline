Chunk 2; segments 351–702. Start may repeat the previous chunk for context.

# How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar

Source ID: source-cfa80c9b2999d9de
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/How_Anthropic_Builds_And_How_Engineering_Will_Change_Soon_Thariq_Shihipar_en.txt
Video: https://www.youtube.com/watch?v=2Kch3tWMnw8

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
