Chunk 2; segments 326–662. Start may repeat the previous chunk for context.

# Meta Distinguished Eng (IC9): Influencing Engs, Failures, and Learnings | Adam Ernst

Source ID: source-c5e5981897b441a1
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Meta_Distinguished_Eng_(IC9)_Influencing_Engs,_Failures,_and_Learnings_Adam_Ernst_en.txt
Video: https://www.youtube.com/watch?v=YA_OYJF3Mmw

[L335] [11:01.84] Here's my concern." And then either
[L336] [11:04.08] like, "I'm gonna let you do what you
[L337] [11:05.52] want if you really feel strongly, but
[L338] [11:07.52] here's what I would do differently next
[L339] [11:08.72] time." Or I'd be like, "Let's talk about
[L340] [11:10.88] how to redo your work to accomplish
[L341] [11:14.08] whatever concern I have." basically hold
[L342] [11:16.96] their hand through the process if if I
[L343] [11:18.72] can because I feel like that's a great
[L344] [11:20.80] way to, you know, now they're gonna
[L345] [11:23.60] hopefully if they're convinced by my
[L346] [11:25.28] argument, they're going to hold that
[L347] [11:27.28] same change in how they operate for
[L348] [11:30.00] their own future work and in all the
[L349] [11:31.52] future code review they do. It's like
[L350] [11:32.88] viral, right? And you see this would
[L351] [11:34.80] would spread through the code reviews
[L352] [11:36.16] that they did. So, I thought it was a
[L353] [11:38.32] really great way to like get my opinions
[L354] [11:40.40] out there and have those debates in a
[L355] [11:42.24] really structured format.
[L356] [11:43.76] >> Given that you've done just such an
[L357] [11:45.44] absurd volume of diff reviews, what
[L358] [11:47.76] makes a good diff comment versus a bad
[L359] [11:50.72] one in your opinion?
[L360] [11:52.08] >> Talk through why you care about what you
[L361] [11:55.12] are nitpicking and not just what to
[L362] [11:57.84] change, right? Don't say change X to Y.
[L363] [11:59.92] Say, hey, X has some problems, so I
[L364] [12:02.72] really want you to use Y instead. But if
[L365] [12:04.72] you really feel strongly if there's
[L366] [12:06.00] something I'm missing, then you can go
[L367] [12:07.20] ahead and use X. Right? The other thing
[L368] [12:09.12] I was always open to in different review
[L369] [12:10.64] comments was the fact that I might be
[L370] [12:12.00] missing context. And that's still the
[L371] [12:13.44] diff author's fault, maybe because like
[L372] [12:16.56] your diff should contain enough context
[L373] [12:18.56] for anyone to review it on its own
[L374] [12:20.40] merits, but I'd often be like, "Hey, I
[L375] [12:22.56] don't understand why you're doing it
[L376] [12:23.68] this way. I want you to do it this way
[L377] [12:25.68] instead, but is there some missing
[L378] [12:27.60] context that would change my mind? If
[L379] [12:29.04] so, fill me in and put it in your diff
[L380] [12:31.12] summary." which again I feel like makes
[L381] [12:33.60] sure that if I'm making a stupid mistake
[L382] [12:35.44] which happens I don't look like a total
[L383] [12:38.40] idiot who's just like getting it wrong.
[L384] [12:41.12] It really helps. So moving on to like
[L385] [12:43.76] you know E7 promo or the senior staff
[L386] [12:46.08] promo. I know that the main project that
[L387] [12:48.48] kind of drove that was component kit.
[L388] [12:50.80] Can you give some context on the story
[L389] [12:53.04] behind component kit?
[L390] [12:54.96] >> The years all blur together at this
[L391] [12:56.80] point but this was like 2014 maybe. We
[L392] [12:59.52] had a very large and complex product,
[L393] [13:02.32] Facebook newsfeed, which was growing and
[L394] [13:04.80] growing and growing so fast because the
[L395] [13:07.04] company hired lots of new engineers and
[L396] [13:08.96] they stuffed everyone on newsfeed
[L397] [13:10.56] because that was the hot product at the
[L398] [13:11.92] time. So it was basically falling apart,
[L399] [13:14.16] right? We had constant crashes, constant
[L400] [13:16.80] layout bugs where like content would be
[L401] [13:18.64] overlapping in weird ways and it was a
[L402] [13:21.20] struggle to keep performance good. I
[L403] [13:23.92] can't claim credit for the idea again
[L404] [13:25.60] here. It was Lee Byron who was I think
[L405] [13:28.40] my manager at the time but was for a
[L406] [13:30.96] long time a very senior engineer at the
[L407] [13:32.64] company and co-invented GraphQL and he
[L408] [13:36.32] had done a lot of work with React on the
[L409] [13:38.24] web which was relatively new then too
[L410] [13:40.48] even on the web it was new and he was
[L411] [13:42.32] like you know what we really need this
[L412] [13:45.04] React concept but for iOS development at
[L413] [13:48.08] this time React Native either didn't
[L414] [13:50.24] exist or was just a prototype and so Lee
[L415] [13:53.60] told me like why don't you just take
[L416] [13:55.04] some time and think about how would the
[L417] [13:57.28] concepts of react work in an iOS first
[L418] [14:01.12] way and component kit was my answer to
[L419] [14:04.00] that question. So it uses the same
[L420] [14:06.56] concepts of like components
[L421] [14:07.92] immutability, rerender everything
[L422] [14:10.48] conceptually at least when anything
[L423] [14:12.40] changes
[L424] [14:13.92] view reconciliation, right? So you're
[L425] [14:15.68] not directly managing UI views. You're
[L426] [14:17.76] instead just stating, hey, I want there
[L427] [14:19.60] to be a button that has this caption.
[L428] [14:21.76] The framework takes care of creating the
[L429] [14:23.44] actual button view. And I'm pretty proud
[L430] [14:26.40] of the balance that it struck in terms
[L431] [14:28.72] of the syntax was appealing, the
[L432] [14:30.64] performance was amazing, and it allowed
[L433] [14:33.84] us to solve a problem that we really
[L434] [14:35.44] needed to solve as a business. And
[L435] [14:37.60] again, this was 2014, so years before
[L436] [14:39.92] Swift UI. Swift didn't exist yet. Swift
[L437] [14:42.00] UI didn't exist yet. React Native didn't
[L438] [14:44.16] exist yet. It was a very early on the
[L439] [14:46.08] scene. And it did take some convincing
[L440] [14:49.44] of other iOS engineers because it was
[L441] [14:51.76] still a very alien way to write code on
[L442] [14:53.92] iOS. But once convinced, everybody loved
[L443] [14:56.64] it. Everybody thought this is a really
[L444] [14:57.92] great way to write the UI for a complex
[L445] [15:00.72] product like Facebook newsfeed. So the
[L446] [15:03.44] big challenge there was inventing the
[L447] [15:04.72] framework, getting it adopted in
[L448] [15:06.40] newsfeed and then getting it adopted
[L449] [15:08.24] everywhere else. So I had lots of lots
[L450] [15:10.16] of work to do. How did you convince
[L451] [15:12.24] people because you know this declarative
[L452] [15:14.08] framework was such a different way of
[L453] [15:16.40] doing things. I imagine there was a lot
[L454] [15:18.16] of push back. How did you you drive
[L455] [15:21.20] those difficult conversations?
[L456] [15:23.68] Tons of push back. Um some people were
[L457] [15:26.16] convinced when they saw concrete
[L458] [15:27.84] examples of hey here's what the same
[L459] [15:31.60] code would look like in component kit.
[L460] [15:33.28] It's now like a third as much code. Some
[L461] [15:36.48] people were convinced when they could
[L462] [15:37.44] see the performance, right? Oh, look, it
[L463] [15:38.96] allows us to render all the viewed
[L464] [15:41.68] hierarchies on a background thread and
[L465] [15:43.36] then only do the minimal amount of work
[L466] [15:44.72] on the main thread. And they were like,
[L467] [15:45.76] that's really cool. But there were
[L468] [15:47.52] plenty of people who were hold outs even
[L469] [15:49.12] then and we had to call in mediators,
[L470] [15:51.92] right? Basically, like there were other
[L471] [15:53.12] senior engineers at the time because
[L472] [15:54.72] when I was inventing component kit, I
[L473] [15:56.16] was an IC6. there were other more senior
[L474] [15:58.40] engineers who would you know get us to
[L475] [16:00.96] huddle up and try to talk through how do
[L476] [16:03.92] we find a path forward that we can all
[L477] [16:06.40] agree on and I think Lee Byron was very
[L478] [16:08.72] involved in these conversations. I know
[L479] [16:10.72] uh Alan Kennaro was a senior engineer at
[L480] [16:12.72] the time who was very involved in this
[L481] [16:14.32] helping us like mediate between these
[L482] [16:16.40] different groups but I think the fact
[L483] [16:18.56] that React had a lot of cred as a
[L484] [16:20.96] framework at the company on the web
[L485] [16:22.32] really helped right because we could
[L486] [16:23.44] point and be like look at what React is
[L487] [16:25.04] doing on the web. We want to do the same
[L488] [16:26.40] on iOS. There aren't any really good
[L489] [16:28.88] reasons why we can't do it. It's not
[L490] [16:30.56] impossible to do on the platform. We we
[L491] [16:32.08] have proven we can. So get on board. And
[L492] [16:35.20] I acknowledge the downsides of component
[L493] [16:36.80] kit, right? It's by now it's very creaky
[L494] [16:39.28] and old because it was a C++ objective
[L495] [16:42.16] C++ framework. Now we have a Swift API
[L496] [16:44.64] for it. That's great. But still at the
[L497] [16:47.28] time the weirdnesses of component kit
[L498] [16:49.60] were even then somewhat unappealing. But
[L499] [16:52.64] my pitch was always, yes, it's a little
[L500] [16:54.88] weird. It's not the usual way of writing
[L501] [16:56.56] code in iOS, but here's all the amazing
[L502] [16:58.56] things we get. That's why you should do
[L503] [17:00.40] it. So that's the pitch that we had to
[L504] [17:03.12] make again and again and again to
[L505] [17:04.64] skeptical iOS engineers. Is there
[L506] [17:06.40] anything that you learned in trying to
[L507] [17:08.48] convince these people that were very
[L508] [17:10.40] against this this approach that is kind
[L509] [17:13.12] of useful and general learning for
[L510] [17:15.28] anyone that's trying to have some new
[L511] [17:17.60] developer offering and convince people
[L512] [17:19.52] to use it? Allies are super useful,
[L513] [17:21.76] right? Um, I still remember uh there
[L514] [17:23.52] were some engineers like Clement Gendmer
[L515] [17:25.28] and Greg Mech who carried a lot of
[L516] [17:27.92] weight in the company and they saw it
[L517] [17:29.84] and liked it. So great, I wasn't alone
[L518] [17:31.68] and they could help convince other
[L519] [17:33.20] people because, you know, I have one way
[L520] [17:35.20] of convincing people which isn't always
[L521] [17:36.72] effective and they have other ways of
[L522] [17:37.92] convincing people which often were more
[L523] [17:39.52] effective. And so it was nice to be able
[L524] [17:41.44] to break it down and like, you know, see
[L525] [17:42.96] the different ways that this discussion
[L526] [17:44.64] happened over time. There were
[L527] [17:46.16] opportunities for compromise. The other
[L528] [17:48.00] big alternative out there was this
[L529] [17:49.60] framework called panels which hadn't
[L530] [17:50.96] really gotten off the ground yet but was
[L531] [17:52.32] supposed to be like the next way to
[L532] [17:53.76] write UI at Facebook and I knew them
[L533] [17:57.52] really well because one of them was like
[L534] [17:58.88] my mentor and so I you know was very
[L535] [18:01.36] very close to Jonathan Dan the guy
[L536] [18:03.44] behind panels and boy they had a really
[L537] [18:05.92] hard time because they felt like they
[L538] [18:07.20] were developing the next thing and then
[L539] [18:08.32] I came along was like actually let's do
[L540] [18:09.60] component kit wasn't so good but we
[L541] [18:12.08] found a way to compromise and we adopted
[L542] [18:13.68] some of the panels data source
[L543] [18:15.68] technology to power component kit which
[L544] [18:17.44] was a good compromise and allowed us all
[L545] [18:18.88] to feel like we had a win. Instead of
[L546] [18:20.56] sticking to your guns and every little
[L547] [18:21.76] thing, if you can find a way to bring
[L548] [18:23.36] people into your fold, into the tent,
[L549] [18:25.52] that's really really helpful.
[L550] [18:26.80] >> With all that push back, did you ever
[L551] [18:28.80] doubt the direction that you're going
[L552] [18:30.48] in?
[L553] [18:31.60] >> No, I was very convinced that this was
[L554] [18:33.12] the right call for Facebook newsfeed. I
[L555] [18:35.20] will say, and this goes for all
[L556] [18:36.80] declarative UI frameworks, React, Swift
[L557] [18:38.64] UI, component kit. They're really good
[L558] [18:41.20] at some things, like a Facebook newsfeed
[L559] [18:42.88] is the perfect thing for it because it's
[L560] [18:44.64] like a scrolling list of complicated
[L561] [18:47.28] multi-level nesting and it's mostly
[L562] [18:49.76] static, right? There's some animation
[L563] [18:51.04] and cool stuff, but mostly it just is
[L564] [18:52.56] like a list of stuff. That's the perfect
[L565] [18:55.04] application for it. When you look at
[L566] [18:57.20] like a super dynamic drag and drop
[L567] [18:58.96] interface, h maybe not the right thing
[L568] [19:01.68] for it, right? Maybe not the ideal case
[L569] [19:03.60] anyway. you can make it work, but it's
[L570] [19:05.04] not going to be incredibly natural. So,
[L571] [19:07.20] I'm very aware that like there are
[L572] [19:09.20] trade-offs to these different paradigms.
[L573] [19:12.32] And I wasn't drinking the Kool-Aid in
[L574] [19:14.56] terms of telling everyone component
[L575] [19:15.76] kit's the only way to write UIs on
[L576] [19:17.28] Facebook. Like that should be the, you
[L577] [19:18.64] know, our only option is component kit.
[L578] [19:21.04] Uh, no. But in general, for what we
[L579] [19:23.36] wanted to use it for, yes, I was very
[L580] [19:24.80] convinced that it was the right path
[L581] [19:26.24] forward. You know, the next project you
[L582] [19:28.08] worked on was component script. What was
[L583] [19:31.04] the motivation behind that project? And
[L584] [19:34.00] you know what's the story behind it?
[L585] [19:36.16] >> So component script was interesting
[L586] [19:37.44] because it was a total and complete
[L587] [19:38.96] failure and I worked on it for like two
[L588] [19:40.80] years. At the time, my manager was a guy
[L589] [19:44.64] named Ari Grant who was a force of
[L590] [19:46.72] nature, right? He was like all over the
[L591] [19:48.32] place, very busy,
[L592] [19:50.96] carried a lot of influence. And Ari felt
[L593] [19:53.36] really strongly that we needed to get
[L594] [19:54.88] out of the perplatform silo, right? So
[L595] [19:57.68] like iOS had component kit, Android had
[L596] [19:59.92] a React and Component kit inspired by
[L597] [20:02.16] then called WHO. But this meant we were
[L598] [20:04.16] writing everything multiple times,
[L599] [20:05.36] right? We had to write it in component
[L600] [20:06.56] kit for iOS, we had to write it in
[L601] [20:07.92] Android. He wanted to have a
[L602] [20:09.20] crossplatform solution. React Native was
[L603] [20:11.20] not that solution and we knew that at
[L604] [20:13.20] this time we had tried React Native and
[L605] [20:14.64] it didn't go well. The reason was in my
[L606] [20:16.88] opinion, this is just my opinion, React
[L607] [20:18.80] Native is designed to be in charge of
[L608] [20:20.40] the entire app. It works really well if
[L609] [20:22.08] your entire app is React Native or if
[L610] [20:24.40] you have entire app React Native and
[L611] [20:25.92] then small little pieces on the very
[L612] [20:27.76] bottom are native or bridged. Where it
[L613] [20:30.72] doesn't work is the way we wrote
[L614] [20:32.80] software at that time which was we had
[L615] [20:35.44] this large complex native app and we
[L616] [20:38.16] wanted to slot in small pieces of
[L617] [20:40.32] crossplatform in different areas right
[L618] [20:42.56] so like oh maybe this little square on
[L619] [20:44.48] this screen is rendered using JavaScript
[L620] [20:47.36] maybe this tab is rendered in JavaScript
[L621] [20:50.48] and this tab is native React Native
[L622] [20:52.24] could not do that for us at the time
[L623] [20:54.48] they've done a lot of architectural
[L624] [20:55.60] changes to React Native in the last 10
[L625] [20:57.52] years since then and maybe it's better
[L626] [20:58.88] at it now but at the
[L627] [21:00.32] didn't really work. So we wanted
[L628] [21:02.72] crossplatform. We knew React Native was
[L629] [21:04.72] not it. What could we do? And so Ari
[L630] [21:07.12] asked me to go and work on this. And I
[L631] [21:09.28] at the time it was like okay this is the
[L632] [21:10.80] next nudge, right? Like we Byron nudged
[L633] [21:12.80] me to work on React for iOS. That was
[L634] [21:15.28] component kit. Great. This is the next
[L635] [21:16.80] nudge work on crossplatform for our UI
[L636] [21:20.32] rendering frameworks that we use on iOS
[L637] [21:21.76] and Android. And so I came up with a
[L638] [21:23.76] framework called component script. The
[L639] [21:26.08] idea was basically at first I took the
[L640] [21:28.08] React APIs, the actual React
[L641] [21:30.16] implementation. I said, "What if we just
[L642] [21:31.44] made a different React Native, right?"
[L643] [21:32.72] So exactly like React Native except that
[L644] [21:34.40] it works on top of component kit and
[L645] [21:35.68] width because that's what we already
[L646] [21:36.96] have. This turned out to be too
[L647] [21:38.72] difficult. React had a really large
[L648] [21:40.88] surface area and a very complex surface
[L649] [21:42.80] area and trying to make that work on on
[L650] [21:45.44] component kit and with it was too
[L651] [21:46.80] challenging. So I was like, "All right,
[L652] [21:48.16] I'll do a smaller paired down API that
[L653] [21:51.76] feels just like React, but actually is
[L654] [21:54.08] simpler and make that work on top of
[L655] [21:56.08] component kit and litho." And I made it
[L656] [21:57.84] work. It was a real framework. People
[L657] [21:59.60] built real features on it. You could
[L658] [22:01.28] build full screens. You could build
[L659] [22:02.72] individual units. You could do all kinds
[L660] [22:04.56] of, you know, birectional embeddings.
[L661] [22:06.48] You could have a native screen that had
[L662] [22:07.52] a component script unit which had a
[L663] [22:09.84] native component inside of that. You
[L664] [22:11.52] could have a component script screen
[L665] [22:12.88] which had a native section. All this
[L666] [22:14.80] stuff, really cool features.
[L667] [22:17.04] And for me, it was a real learning
[L668] [22:19.12] experience because I learned that just
[L669] [22:20.80] because it was technically excellent
[L670] [22:22.72] didn't mean it was going to win. It
[L671] [22:25.68] checked all the boxes we needed in terms
