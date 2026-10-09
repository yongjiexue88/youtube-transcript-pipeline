Chunk 2; segments 317–634. Start may repeat the previous chunk for context.

# Instagram iOS Principal Eng (IC8): Building IG Stories, 1 Promo Per Half, Small Teams

Source ID: source-77b7f65a700842eb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Instagram_iOS_Principal_Eng_(IC8)_Building_IG_Stories,_1_Promo_Per_Half,_Small_Teams_en.txt
Video: https://www.youtube.com/watch?v=gpVETZnY9Y0

[L326] [12:38.96] something you'd built before you were at
[L327] [12:40.72] the company, which is really cool. I'm
[L328] [12:42.96] curious, did building something like
[L329] [12:44.80] that and open sourcing it have some
[L330] [12:47.28] unexpected, you know, butterfly effect
[L331] [12:49.68] on your career in some way?
[L332] [12:51.28] >> In some ways it did. In some ways, I
[L333] [12:53.04] thought maybe it would have more um
[L334] [12:55.84] impact than than it did. So an example
[L335] [12:59.04] of that is um when I came to interview
[L336] [13:02.00] at Instagram uh I had already released
[L337] [13:05.52] this open source and so I was like you
[L338] [13:07.36] know here's here's my code you want to
[L339] [13:09.12] see what I can do like this is a thing
[L340] [13:11.04] that I built that you can go look at and
[L341] [13:13.44] and none of my interviewers had any
[L342] [13:15.20] interest in in in looking at it you know
[L343] [13:17.84] they were like we want to know if you
[L344] [13:19.12] can do this phone number sorting thing
[L345] [13:21.84] um and so that was like pretty
[L346] [13:23.52] frustrating to me I was like you know
[L347] [13:25.36] you you can see my work here and you and
[L348] [13:27.76] you choosing not to look at it. Other
[L349] [13:30.00] people who are kind of slightly outside
[L350] [13:32.32] of the interview loop but part of the
[L351] [13:33.84] recruiting process um like uh Jonathan
[L352] [13:37.68] Dan was this guy who worked at uh
[L353] [13:40.48] Facebook on the iOS team. He kind of I
[L354] [13:43.52] think he actually did the file new
[L355] [13:46.08] project in Xcode for the Facebook iOS
[L356] [13:48.32] app. [laughter] Um, so he'd kind of
[L357] [13:50.08] started that and uh he was the one who
[L358] [13:53.12] who got me to interview in the first
[L359] [13:55.04] place and and that was all through him
[L360] [13:57.60] seeing this tool and what it could do
[L361] [13:59.92] and yeah and I think he advocated in the
[L362] [14:02.96] candidate review or whatever cuz I I
[L363] [14:04.64] think I had kind of a mixed mixed
[L364] [14:06.64] interview loop. Um yeah, I mentioned
[L365] [14:09.04] before like I was uh was very nervous in
[L366] [14:12.00] my in my uh internship interview. Um,
[L367] [14:15.76] and uh the I did something for my
[L368] [14:19.28] full-time interview that um it's maybe
[L369] [14:21.60] helpful to to some people out there uh
[L370] [14:24.56] that get nervous in interview
[L371] [14:26.24] situations. Um there's something called
[L372] [14:28.24] beta blockers which uh they they block
[L373] [14:32.16] adrenaline. So when you have kind of the
[L374] [14:35.84] physical effects of being nervous like
[L375] [14:38.56] pounding heart or you know sweaty palms,
[L376] [14:41.20] that type of thing, you can start to
[L377] [14:42.96] feel those and and it can create this
[L378] [14:45.44] feedback loop where you kind of spiral
[L379] [14:47.20] down and really starts to like block
[L380] [14:49.52] your performance. Um and so what a beta
[L381] [14:52.40] blocker does is it just stops that
[L382] [14:55.52] adrenaline from firing and so you can
[L383] [14:58.40] kind of stay calm and never end up in
[L384] [15:01.04] that spiral. So, um, I got a
[L385] [15:03.20] prescription for that for for my
[L386] [15:04.88] interview, um, interview
[L387] [15:06.48] performance-enhancing drugs, I guess,
[L388] [15:08.64] and, uh, and I took that and it was very
[L389] [15:11.28] helpful for me. So, I was able to to
[L390] [15:12.96] stay calm. Um, I think performers
[L391] [15:15.20] sometimes use this, uh, you know,
[L392] [15:18.08] comedians or whatever, um, just to to
[L393] [15:20.88] kind of like, you know, be able to stay
[L394] [15:23.28] themselves and not um, end up in this in
[L395] [15:26.24] this nervous loop. So I did that, but
[L396] [15:28.16] you know, I was still like kind of elite
[L397] [15:30.16] code style interview loop, which which I
[L398] [15:32.72] um don't do that well at. So I think I
[L399] [15:35.44] had like a few like absolute confidence
[L400] [15:37.92] hire uh interviews and probably a few no
[L401] [15:40.48] hires. Um somehow I managed to to get
[L402] [15:43.36] through. Um but I think that also
[L403] [15:46.32] contributed to I came into to Facebook
[L404] [15:50.48] as a IC4. Um I guess one level up from
[L405] [15:54.88] new grad engineer and um I would say
[L406] [15:59.04] like I was underleveled higher. I think
[L407] [16:01.76] you know part of that would have came
[L408] [16:03.04] from my interview loop. And when you use
[L409] [16:05.68] the beta blockers, I'm curious, is it
[L410] [16:07.92] basically completely removed the nerves
[L411] [16:10.72] component for you or is it just kind of
[L412] [16:12.56] like helps a little bit?
[L413] [16:14.16] >> I've only used them a handful of times.
[L414] [16:16.08] Um, but it pretty much completely, you
[L415] [16:19.44] know, like no noticeable kind of nervous
[L416] [16:23.20] effects. I mean, I think you can still
[L417] [16:25.44] be in your head for sure about um what
[L418] [16:29.20] you're saying, but um it takes away a
[L419] [16:31.68] lot of those physical effects. Um, so no
[L420] [16:34.40] no pounding hard or or you know
[L421] [16:36.32] sweating, that type of thing.
[L422] [16:37.58] [clears throat]
[L423] [16:37.84] >> After you passed the interview for
[L424] [16:39.20] full-time, you started working on the
[L425] [16:41.92] Instagram team working on iOS and I'm
[L426] [16:45.60] curious what the what the environment
[L427] [16:48.16] was like at the time. You know, what was
[L428] [16:49.92] the size of the team?
[L429] [16:51.20] >> Um, yes. So I came in and I think there
[L430] [16:53.84] were about 10 iOS engineers working on
[L431] [16:56.72] Instagram then. Um, which was actually
[L432] [16:59.68] the team size had come down. So the the
[L433] [17:03.60] way the story's been told to me is um
[L434] [17:06.40] there were maybe about 20 iOS engineers
[L435] [17:09.68] and there was kind of this internal war
[L436] [17:12.56] over um the direction of the the
[L437] [17:17.04] codebase like the infrastructure how how
[L438] [17:19.36] the Instagram iOS app would be built.
[L439] [17:22.48] And there was a really talented uh iOS
[L440] [17:24.96] engineer uh Scott Goodson who was
[L441] [17:26.96] managing the team and he had made this
[L442] [17:30.32] framework for the Facebook paper app
[L443] [17:33.44] called Async Display Kit and it was kind
[L444] [17:36.48] of a different approach towards how you
[L445] [17:39.84] manage um writing iOS. Uh, and I guess
[L446] [17:45.20] there were kind of like waring factions
[L447] [17:46.80] like some people were, you know, very
[L448] [17:48.24] pro async display kit and other people
[L449] [17:50.64] were like, "No, we should just stick to
[L450] [17:52.24] vanilla iOS, how Apple builds apps." The
[L451] [17:55.36] way it was told to me is like these two
[L452] [17:57.20] factions like they fought each other and
[L453] [17:59.04] they destroyed each side destroyed each
[L454] [18:01.04] other. Everyone just left and nobody
[L455] [18:03.28] won. So, um, so I came into kind of like
[L456] [18:07.12] this uh this team. I mean, I got to I I
[L457] [18:11.04] feel like not many engineers had been
[L458] [18:13.68] there more than, you know, 6 months to a
[L459] [18:16.00] year. It was like a pretty new team.
[L460] [18:19.52] Um, and because of that, there was
[L461] [18:23.28] actually like a lot of lowhanging fruit.
[L462] [18:25.28] Um, a lot [clears throat] of places to
[L463] [18:26.96] to have impact. One of the first things
[L464] [18:29.28] I did was just to put the app into uh a
[L465] [18:33.12] tool called the time profiler. Most iOS
[L466] [18:35.68] developers will will know this in Xcode.
[L467] [18:38.56] um or in instruments um and just looked
[L468] [18:41.68] at you know okay what is happening on
[L469] [18:43.68] cold start and there was a bunch in in
[L470] [18:47.68] kind of the startup path there was a
[L471] [18:49.12] bunch of work happening for the profile
[L472] [18:50.80] tab which you know many people will
[L473] [18:52.96] never tap into and um if they do you can
[L474] [18:56.00] kind of do that work at that time so it
[L475] [18:58.08] was like a very easy win to shave 20%
[L476] [19:01.20] off our cold start time just by
[L477] [19:03.12] deferring that work until later. Another
[L478] [19:05.76] example was we had this networking
[L479] [19:08.32] library uh AF networking and there's
[L480] [19:11.84] something um I mean I guess most
[L481] [19:14.40] programmers are familiar with assertions
[L482] [19:17.28] um in iOS the way assertions are
[L483] [19:20.08] typically handled is it's something that
[L484] [19:22.80] you run when the app is in debug mode to
[L485] [19:25.44] kind of crash and and alert you to a
[L486] [19:28.00] problem. uh but you kind of have
[L487] [19:30.88] fallback behavior for production and you
[L488] [19:33.60] don't actually crash the app and so this
[L489] [19:36.56] networking library was building being
[L490] [19:38.48] built with assertions on and it was
[L491] [19:42.72] crashing the app for like benign
[L492] [19:44.32] failures like a network failure right
[L493] [19:46.08] where the app could recover we were just
[L494] [19:48.32] crashing um and so that cut our crash
[L495] [19:50.80] rate by 80%. Um and uh you know it was
[L496] [19:54.40] just like a one on one line change just
[L497] [19:55.92] NS block assertions but it's a pretty
[L498] [19:58.32] significant impact on on the functioning
[L499] [20:01.52] of the app. Uh and we uh Instagram had
[L500] [20:05.04] this this cool tradition uh where every
[L501] [20:08.72] week they would give what was called the
[L502] [20:12.24] axe and it wasn't getting fired which it
[L503] [20:15.60] sounds like um if you got the axe it was
[L504] [20:18.40] like you did something of outsiz impact.
[L505] [20:21.20] Um, and it was actually across all
[L506] [20:23.36] functions. Didn't have to be
[L507] [20:24.64] engineering, could be product, design,
[L508] [20:26.64] whatever. And so for that 80% crash,
[L509] [20:30.16] crash reduction. I won the axe. And um
[L510] [20:33.44] it was this big physical axe uh that you
[L511] [20:36.16] got to carry around for a week. At
[L512] [20:37.52] first, I thought you got to take like I
[L513] [20:38.96] was like, "Oh, I get this axe."
[L514] [20:40.58] [laughter]
[L515] [20:40.80] >> Yeah.
[L516] [20:41.28] >> I had it at my desk for a week and I was
[L517] [20:43.04] like, "Oh, no. There's just one axe.
[L518] [20:44.72] Somebody else is going to get it next
[L519] [20:46.24] week." Um but yeah,
[L520] [20:48.80] >> I remember the axe. What's the story
[L521] [20:50.96] behind that? Is that something the
[L522] [20:52.64] Instagram founders like had done?
[L523] [20:55.36] >> At some point, they had been asked by
[L524] [20:57.04] like GQ or some men's magazine to do
[L525] [21:00.64] like a holiday gift guide and I think
[L526] [21:03.60] they just kind of came up with like
[L527] [21:05.20] random gifts and um one of them was like
[L528] [21:08.32] they found this service that was making
[L529] [21:10.08] like bespoke axes.
[L530] [21:13.60] you you could get this axe. And then one
[L531] [21:16.64] of their investors like read that
[L532] [21:18.16] article and then they sent them this
[L533] [21:19.76] huge axe. Um, and apparently Facebook
[L534] [21:23.44] security was like pretty unhappy about
[L535] [21:25.92] this axe, this weapon in the office, so
[L536] [21:29.20] they made them put it on a plaque. Uh,
[L537] [21:31.04] it was like mounted to the plaque. You
[L538] [21:32.72] couldn't take it off. Uh, but it was
[L539] [21:35.44] Yeah, it was it was a cool tradition.
[L540] [21:37.28] Um, you know, later, uh, in my time
[L541] [21:40.56] there, they ended the axe as like a very
[L542] [21:43.04] intentional thing. They were like, I
[L543] [21:44.64] guess they thought people were feeling
[L544] [21:46.16] excluded because it was like a weapon
[L545] [21:48.16] that was being given or something like
[L546] [21:49.76] that. But I I was kind of sad when that
[L547] [21:51.68] happened cuz it felt like, you know, at
[L548] [21:53.52] that time the founders were were gone
[L549] [21:55.44] and it was like this piece of like early
[L550] [21:57.76] Instagram culture that they were kind of
[L551] [21:59.36] like sweeping under the rug. So,
[L552] [22:02.32] >> so I guess going into your first major
[L553] [22:04.40] project after all those lowh hanging
[L554] [22:05.92] fruit, I understand there was a big
[L555] [22:08.48] redesign of the Instagram app called
[L556] [22:10.32] White Out. Can you talk about the story
[L557] [22:13.04] behind that project?
[L558] [22:14.16] >> Yeah, it was a couple months into my
[L559] [22:15.84] time there and it kind of got word that
[L560] [22:18.16] um we were working on a new icon which
[L561] [22:20.24] ended up being very controversial. Um,
[L562] [22:22.88] and as part of that, we were going to do
[L563] [22:24.80] like this kind of uh redesign of the
[L564] [22:27.20] app, a big visual refresh. And I don't
[L565] [22:31.60] remember exactly what I did, but I
[L566] [22:33.36] remember being like, I have to work on
[L567] [22:35.12] this thing. This is like, this sounds so
[L568] [22:37.20] cool. This is what I want to do. And,
[L569] [22:39.76] you know, I told my manager, I was like
[L570] [22:41.52] meeting the designers that were working
[L571] [22:42.96] on it. Um, so I basically just
[L572] [22:44.96] maneuvered myself in into working on
[L573] [22:47.68] this project. And uh the the main
[L574] [22:51.04] designer on it, Joy Vincent, um who was
[L575] [22:53.92] just like yeah, just an incredible
[L576] [22:56.88] talent and the nicest guy ever. Really
[L577] [22:59.68] sad. He he passed away while we were at
[L578] [23:01.84] Instagram. Um but um I sat in a war room
[L579] [23:07.28] um you know just like a conference room
[L580] [23:10.08] basically uh with him for I think
[L581] [23:14.08] probably two or three months and just
[L582] [23:16.32] every day we'd be like okay new screen
[L583] [23:18.48] and app we'd go look at it. He'd be like
[L584] [23:20.64] all right I want to do this this this
[L585] [23:22.08] and I would do that and I' you know pass
[L586] [23:23.68] the phone over to him and just back and
[L587] [23:26.40] forth like that. Um, you know, we
[L588] [23:28.27] [clears throat] we did kind of a whole
[L589] [23:30.40] new color palette for the app, new
[L590] [23:32.24] icons. Um, and one of the goals was to
[L591] [23:38.00] really make all of the focus in
[L592] [23:39.92] Instagram on the content on the photos
[L593] [23:42.16] and the videos and to take all the color
[L594] [23:44.88] out of the chrome. And it's basically,
[L595] [23:47.84] you know, how Instagram looks today. But
[L596] [23:49.60] at that time, you know, we had this kind
[L597] [23:51.60] of dark blue and black chrome everywhere
[L598] [23:54.64] in the app. and uh things were have a
[L599] [23:57.44] lot heavier um and uh yeah so we just
[L600] [24:01.12] tried to to really simplify it down and
[L601] [24:03.76] make all the color come from the content
[L602] [24:05.84] itself.
[L603] [24:06.88] >> Was it a gated launch or was it a just
[L604] [24:09.28] launch it all at once kind of project?
[L605] [24:11.68] >> So AB testing was like pretty new at
[L606] [24:13.92] Instagram at that point. Um you Facebook
[L607] [24:16.40] was was doing a lot of it and Instagram
[L608] [24:18.72] was kind of more the like oh we know
[L609] [24:20.24] what's good so we'll just ship it. And
[L610] [24:23.76] uh when I started working on on this
[L611] [24:26.56] project, the the CTO and co-founder of
[L612] [24:28.80] Mike Creger, he he was like, "You know
[L613] [24:31.28] what? Don't don't worry about trying to
[L614] [24:32.88] AB test this thing." He's like, "Just
[L615] [24:35.44] just ship it. Like build it and ship
[L616] [24:37.28] it." Um, and actually at that time like
[L617] [24:41.44] they were still sort of using branching
[L618] [24:43.36] as like a way to to build big features,
[L619] [24:46.00] but I had seen some longived branches
[L620] [24:50.08] uh like the the um direct messaging
[L621] [24:53.36] feature had been built as a as a longive
[L622] [24:56.32] branch and it was a nightmare merging it
[L623] [24:58.72] back in because they branched off for
[L624] [25:00.08] like 3 months and weren't really
[L625] [25:01.92] rebasing and then they you know merge
[L626] [25:03.52] this thing back in. It was it was I
[L627] [25:05.60] think pretty awful and and this redesign
[L628] [25:07.60] touched literally every surface of of
[L629] [25:09.68] the app. Um so I was kind of like well
[L630] [25:12.16] this is not going to be a good way to
[L631] [25:14.00] build it. So I put it behind kind of a
[L632] [25:16.00] feature flag and was constantly merging
[L633] [25:18.24] it and had to build abstractions like
[L634] [25:21.52] all the colors became semantic colors.
[L635] [25:23.76] So you know um it's like instead of
[L636] [25:27.60] saying that icon is black it's like it's
[L637] [25:29.68] icon color or something like that. um or
[L638] [25:32.80] it's disabled icon color and then you
[L639] [25:35.60] could switch inside of that function for
[L640] [25:38.32] you know are we on the new design or the
[L641] [25:40.08] old design. Um [snorts] and so that
[L642] [25:42.56] ended up being just kind of a much
[L643] [25:44.16] easier way to to build it incrementally.
