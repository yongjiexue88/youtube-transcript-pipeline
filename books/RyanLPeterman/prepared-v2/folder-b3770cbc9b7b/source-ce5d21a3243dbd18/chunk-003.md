Chunk 3; segments 651–972. Start may repeat the previous chunk for context.

# Boris Cherny (Creator of Claude Code) On What Grew His Career And Building at Anthropic

Source ID: source-ce5d21a3243dbd18
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Boris_Cherny_(Creator_of_Claude_Code)_On_What_Grew_His_Career_And_Building_at_Anthropic_en.txt
Video: https://www.youtube.com/watch?v=AmdLVWMdjOk

[L660] [21:39.60] particular one I remember was like relay
[L661] [21:41.36] mutations. So like you send API requests
[L662] [21:43.76] and you need some sort of consistency.
[L663] [21:45.76] Um, but there's actually this bug where
[L664] [21:47.44] like let's say there's like a button and
[L665] [21:49.20] you press the button. Every time you
[L666] [21:50.56] press it, you send a post request. And
[L667] [21:52.96] uh every time you press the button, it
[L668] [21:54.24] toggles the state of that button. For
[L669] [21:56.40] really nice UX, what you want is as soon
[L670] [21:58.32] as you press the button, the state
[L671] [21:59.44] should toggle, which means you need an
[L672] [22:01.28] optimistic update. But also, uh when the
[L673] [22:04.16] network request comes back, you need to
[L674] [22:05.52] also update the local cache to make sure
[L675] [22:07.28] it's consistent. And if you're just like
[L676] [22:09.04] mashing that button, what can happen is
[L677] [22:10.88] that the responses come in out of order
[L678] [22:13.28] and you might end up with a different
[L679] [22:14.72] state than what was in the UI. Um and so
[L680] [22:17.04] I wrote a system to kind of queue up
[L681] [22:18.48] mutations. So it was like consistency at
[L682] [22:20.48] the cost of reliability and this was
[L683] [22:21.84] kind of the right trade-off at the time.
[L684] [22:23.76] Uh and everyone ended up using this and
[L685] [22:25.36] this is how I met like Joseona and a
[L686] [22:27.68] bunch of the relay team that was working
[L687] [22:29.20] on the the data stores. Um, and it was
[L688] [22:31.92] just really fun. And this is something
[L689] [22:33.76] that since then and before then and you
[L690] [22:36.96] know whenever I work with engineers, I
[L691] [22:39.36] just love when people go a layer deeper
[L692] [22:41.84] and uh, you know, just try to figure out
[L693] [22:43.60] like what's going on and like just
[L694] [22:44.72] because you're a product engineer
[L695] [22:46.08] doesn't mean you can't build infra. Just
[L696] [22:47.60] because you're an infra engineer doesn't
[L697] [22:49.12] mean you can't go talk to users like
[L698] [22:50.72] just be curious about these other parts
[L699] [22:52.24] of the stack.
[L700] [22:53.36] >> Definitely. and in your agency and
[L701] [22:56.24] getting ahead of comet or this big
[L702] [22:58.56] JavaScript rewrite. You mentioned in
[L703] [23:00.40] your in your writing that you know
[L704] [23:02.40] getting ahead of that actually gave you
[L705] [23:04.24] a lot more control and also dibs on
[L706] [23:06.32] opportunities. So when you talk about
[L707] [23:08.48] opportunities there is is this what
[L708] [23:10.72] you're kind of talking about like
[L709] [23:12.24] building these fundamental pieces of
[L710] [23:13.84] prod infra that are impactful for
[L711] [23:16.24] everyone that's going to take on the new
[L712] [23:18.56] platform?
[L713] [23:19.36] >> Yeah. Yeah, that's an example of it. Um,
[L714] [23:21.60] and then maybe you know like a different
[L715] [23:23.28] kind of example is Comet was a lot
[L716] [23:26.08] higher quality than the thing that came
[L717] [23:27.44] before because it, you know, it's like a
[L718] [23:28.48] single page web app. Um, so it can just
[L719] [23:30.72] feel a lot more polished. But we hadn't
[L720] [23:32.48] yet figured out like what exactly
[L721] [23:34.08] quality means on the product side. And
[L722] [23:36.08] so I wrote a bunch of notes trying to
[L723] [23:37.60] define that and then did a bunch of tech
[L724] [23:39.12] talks trying to just like teach people
[L725] [23:40.72] on other teams like here's what we
[L726] [23:42.40] learned about quality. Um, and just kind
[L727] [23:45.28] of like setting up the conversation
[L728] [23:46.64] about that.
[L729] [23:48.32] you mentioned a big headcount ask for I
[L730] [23:51.60] guess this migration to comment you know
[L731] [23:54.96] I feel like I'd be curious what that
[L732] [23:57.44] would look like in today with these new
[L733] [24:00.96] tools like cloud codeex etc. I'd be
[L734] [24:04.32] curious like knowing what you know now
[L735] [24:06.00] about cloud code and you let's say you
[L736] [24:08.48] were in charge of doing that same
[L737] [24:10.16] scoping for that same job. How many
[L738] [24:12.64] engineers do you think it'd take to do
[L739] [24:14.32] that 12 engineer job?
[L740] [24:16.32] >> Yeah. So I think overall to move
[L741] [24:18.00] Facebook groups it it started with 12
[L742] [24:20.00] engineers but I think at the end it was
[L743] [24:22.08] maybe like 20 or 30 engineers or
[L744] [24:23.84] something for about two years. So it
[L745] [24:25.28] turned out to be a pretty big project.
[L746] [24:27.12] Um I think nowadays it would be maybe
[L747] [24:30.40] I don't know like five engineers for six
[L748] [24:32.40] months something something like that.
[L749] [24:34.48] >> So a fourth of the fourth of the time
[L750] [24:37.36] and um like more than a third or less
[L751] [24:40.48] than a third of the engineers as well.
[L752] [24:42.80] >> Yeah. Yeah. cuz you just like everyone
[L753] [24:44.24] would just have a bunch of quads running
[L754] [24:45.52] in parallel and you know just like let
[L755] [24:47.52] it cook for a couple hours and then it
[L756] [24:48.88] comes back with a PR and then you give
[L757] [24:50.40] it like puppeteer or something so it can
[L758] [24:52.00] kind of see the UI and and adjust and I
[L759] [24:54.56] I think that's pretty much all it would
[L760] [24:55.84] be and then I you know nowadays the
[L761] [24:58.24] world we're in is so different from a
[L762] [24:59.84] coding point of view because the models
[L763] [25:03.04] are moving so quickly that you know if
[L764] [25:06.00] you ask me this question in 3 months or
[L765] [25:07.68] 6 months my answer will be totally
[L766] [25:09.28] different in 6 months the answer might
[L767] [25:11.28] be this is actually one engineer
[L768] [25:13.28] um it's just moving so quickly now it's
[L769] [25:15.60] really hard to to do these estimates or
[L770] [25:17.76] to predict how they're going to change
[L771] [25:18.96] in the future.
[L772] [25:20.08] >> At this point in your career you you had
[L773] [25:22.24] mentioned something maybe it was
[L774] [25:23.52] tongue-in-cheek I'm not sure. You said
[L775] [25:25.60] this was when I learned to always
[L776] [25:27.28] present three options in VP reviews
[L777] [25:29.68] since 80% of the time they'll just pick
[L778] [25:32.16] the middle option and then it says you
[L779] [25:34.48] your VP picked the middle option in
[L780] [25:36.56] frenies. Um what's the thinking behind
[L781] [25:38.96] that?
[L782] [25:40.32] Yeah, this is this is very much tongue
[L783] [25:42.08] andcheek. Um, but maybe this is actually
[L784] [25:44.64] kind of true at Meta at the time.
[L785] [25:45.82] [laughter]
[L786] [25:47.52] Um, I think like decision makers that
[L787] [25:49.76] are far away from the work want to know
[L788] [25:52.64] that you did the due diligence of
[L789] [25:55.44] finding the right options and the right
[L790] [25:57.04] trade-offs and that you did the work,
[L791] [25:58.72] but they also want to contribute somehow
[L792] [26:00.32] to the decision. Um, so, you know, the
[L793] [26:03.12] middle option is kind of the easy way to
[L794] [26:04.72] do that. It's a little tongue-in-cheek
[L795] [26:06.80] because I think not all leaders are like
[L796] [26:08.56] this. A lot of leaders will do their
[L797] [26:10.00] work themselves. They trust their teams
[L798] [26:12.00] more or less. There's sort of there's so
[L799] [26:14.16] many different ways to operate. Um, but
[L800] [26:16.88] at the time I remember we had like a
[L801] [26:18.40] pretty non-technical leader and this was
[L802] [26:20.40] kind of the way to to help her make make
[L803] [26:22.48] decisions. I think at this point in your
[L804] [26:24.40] career you had the most proximity you've
[L805] [26:27.52] had to senior management. It's you said
[L806] [26:30.16] you were reporting to uh a senior
[L807] [26:32.24] director at some point and you were
[L808] [26:34.00] involved in a lot of huge scoping
[L809] [26:36.16] conversations. I'm curious what's the
[L810] [26:38.08] downstream effects of reporting to
[L811] [26:39.68] someone so senior like that.
[L812] [26:41.76] >> Yeah, I think it kind of depends on the
[L813] [26:43.12] engineer and it depends on the company.
[L814] [26:46.24] Um, so for example, like you know, now
[L815] [26:48.40] I'm at Anthropic and I think at
[L816] [26:50.08] anthropic it doesn't matter. Um, it
[L817] [26:52.16] doesn't it doesn't matter which level
[L818] [26:53.28] you report to. There's some of the most
[L819] [26:55.20] senior people at the company report to
[L820] [26:56.80] line managers. Um, a lot of the line
[L821] [26:59.12] managers are like XCTO's and things like
[L822] [27:01.44] this. So um, it actually doesn't matter.
[L823] [27:04.32] So I think this is kind of like a meta
[L824] [27:05.68] it's a very meta-pecific cultural um
[L825] [27:08.72] cultural observation. I think there's
[L826] [27:11.12] sort of like two things going on. So one
[L827] [27:13.84] is you want at meta you needed uh as an
[L828] [27:17.76] engineer you always needed to find
[L829] [27:19.12] scope. Some of this you can find
[L830] [27:21.12] yourself and then some of it your
[L831] [27:22.56] manager helps you find or you know your
[L832] [27:24.40] tech lead or the people you surround
[L833] [27:25.68] yourself with and you know like the PSC
[L834] [27:29.28] process is like growing like famously
[L835] [27:30.96] growing at meta and so you just have to
[L836] [27:33.12] constantly talk about your impact and
[L837] [27:34.64] like scope is like the biggest
[L838] [27:35.84] contributor to that like if you have
[L839] [27:37.44] enough scope and you executed well
[L840] [27:38.72] that's impact that's the formula I think
[L841] [27:41.36] the other part was at meta no one had
[L842] [27:45.12] titles so even the most senior engineers
[L843] [27:47.52] their title was software engineer which
[L844] [27:49.76] I actually really love. And um you know
[L845] [27:52.56] like Bell We L We L We L We L We L We L
[L846] [27:52.96] We L We L We L We Labs had this with
[L847] [27:53.68] like member of technical staff and this
[L848] [27:55.44] is true at anthropic too, but we
[L849] [27:56.88] actually go even further here.
[L850] [27:58.72] Everyone's title is member of technical
[L851] [28:00.72] staff. It doesn't even matter if you're
[L852] [28:02.40] an engineer or a PM or a designer, it's
[L853] [28:04.56] all the same title. Um, and I actually
[L854] [28:06.96] really love it because back to this
[L855] [28:09.68] point of working outside your lane and
[L856] [28:11.84] doing stuff that just should be done
[L857] [28:14.24] and, you know, like are just good things
[L858] [28:15.92] to do regardless of what you are
[L859] [28:17.44] personally expected to do. Um, I think
[L860] [28:20.24] this kind of culture just sets that up.
[L861] [28:22.40] I mean, I I I see a lot of the benefits
[L862] [28:24.56] of the no titles. I could also see a
[L863] [28:27.20] case though where um and maybe this is
[L864] [28:29.52] only true for big companies where you
[L865] [28:31.20] reach out to someone across the company
[L866] [28:33.52] and you say hey I'd like to I don't know
[L867] [28:36.24] do this collaboration and if your title
[L868] [28:38.80] said director or whatever it kind of is
[L869] [28:42.40] like a shortcut for them to understand
[L870] [28:44.64] how seriously to take you or how to
[L871] [28:47.44] interact with you like if you're a
[L872] [28:48.96] designer or some other role. So I mean
[L873] [28:52.08] now anthropics got a bit bigger at this
[L874] [28:54.40] point. Do you see uh any of that? I
[L875] [28:56.88] mean, people probably all know you, so
[L876] [28:58.32] maybe you don't see it as much.
[L877] [29:00.00] >> Yeah, I think I think this is definitely
[L878] [29:01.52] the downside. I think the upside
[L879] [29:03.92] outweighs it, which is you have to earn
[L880] [29:05.68] trust. And I I think this is true. Like,
[L881] [29:08.80] you know, regardless of what company
[L882] [29:10.56] you're at, you got to earn it. And just
[L883] [29:12.88] because you did a cool thing before,
[L884] [29:14.48] doesn't mean that you have you should
[L885] [29:16.08] deserve respect. Well, everyone deserves
[L886] [29:18.08] respect. Doesn't mean that you should
[L887] [29:19.28] deserve authority at a new company in a
[L888] [29:21.60] new setting. Um, so I think even for
[L889] [29:24.16] people coming in with manager titles,
[L890] [29:25.68] you kind of have to earn it. And in some
[L891] [29:26.80] ways, having a manager title makes it a
[L892] [29:28.96] little bit harder to earn this kind of
[L893] [29:30.40] trust. Um, so as an IC, you got to do it
[L894] [29:33.36] either way. And I I think just the lack
[L895] [29:34.88] of titles makes it a little easier. At
[L896] [29:37.20] this point in your career, you were kind
[L897] [29:38.96] of like becoming more and more of a tech
[L898] [29:41.68] lead or Uber tech lead. And I think you
[L899] [29:44.00] had a few stories where you scoped out
[L900] [29:46.40] work for hundreds of engineers. And I
[L901] [29:48.80] was just thinking about how do you do
[L902] [29:51.52] that if there's so much to scope and you
[L903] [29:54.96] know you're one person. How do you go
[L904] [29:56.88] about doing such massive scoping
[L905] [29:59.36] requests for leadership?
[L906] [30:01.12] >> Yeah, this was a totally insane time. So
[L907] [30:03.12] I worked a lot with uh Tina Shutchman
[L908] [30:04.96] who's uh she she's now at Microsoft um
[L909] [30:07.20] but she was she was my manager at the
[L910] [30:08.64] time and then uh Ephe who's who's my
[L911] [30:10.64] manager after and there was a lot more
[L912] [30:13.68] investment going into Facebook groups at
[L913] [30:16.00] the time. So I think the org was maybe
[L914] [30:19.20] 150 or 200 people when I joined and by
[L915] [30:21.52] the time I left to Instagram I think it
[L916] [30:23.12] was like 600 or 800 people something
[L917] [30:24.88] like that. So there's this feeling from
[L918] [30:27.52] Zach that Facebook app should be all
[L919] [30:30.08] about communities and he just wanted us
[L920] [30:32.48] to go like faster and faster to make
[L921] [30:34.08] that a reality and you know as an
[L922] [30:36.72] executive your kind of biggest way to do
[L923] [30:38.48] that is to put the right people in
[L924] [30:40.40] charge of decisions and then uh to give
[L925] [30:42.80] them resources and so like in you know
[L926] [30:44.48] in the case of meta it's it's just
[L927] [30:45.84] engineers um you don't need like GPUs
[L928] [30:47.92] for this you need like engineers to do
[L929] [30:49.52] stuff and so we pitched this project to
[L930] [30:52.40] uh to Zach and it was called communities
[L931] [30:54.24] as the new organizations that was like
[L932] [30:55.60] the internal name and uh he grin just
[L933] [30:58.88] like a a bunch of headcount to go
[L934] [31:00.32] towards this and so we just had to
[L935] [31:01.44] figure out what these people will do and
[L936] [31:04.00] you know for him I I get it it's like if
[L937] [31:06.40] the thing is important you got to put a
[L938] [31:07.76] bunch of people on it in hindsight what
[L939] [31:09.84] I would have done differently is I I
[L940] [31:11.36] would have put way less people on it
[L941] [31:13.44] because what matters is like solving
[L942] [31:15.28] people's problems and building awesome
[L943] [31:17.12] product and this actually has to kind of
[L944] [31:19.76] be bottoms up and you kind of want to
[L945] [31:21.12] like slowly dial this up as you find
[L946] [31:23.04] product market fit for new product lines
[L947] [31:24.96] you can't just do it all at once. And uh
[L948] [31:28.72] yeah, we just had to like scope out all
[L949] [31:30.08] the stuff. Like there were weeks where I
[L950] [31:31.28] had to, you know, do like a scoping dock
[L951] [31:33.28] for like, okay, we're going to put 30
[L952] [31:34.64] engineers on this. Here's like three
[L953] [31:35.92] technical options. We're going to pick
[L954] [31:36.96] this one. Next project, we're going to
[L955] [31:38.48] put 20 engineers on this. Here's three
[L956] [31:39.84] options. We're going to pick this one.
[L957] [31:41.04] Next project we're going to do. And just
[L958] [31:42.64] like doing this like over and over again
[L959] [31:44.08] just to have like, you know, some some
[L960] [31:46.48] sort of confidence that this thing isn't
[L961] [31:47.84] totally crazy. We did some baseline
[L962] [31:49.36] technical scoping roughly matching the
[L963] [31:51.36] number of engineers to the project. And
[L964] [31:54.16] there there's actually some pretty fun
[L965] [31:55.36] stuff like I remember we were trying to
[L966] [31:57.12] merge Facebook groups and uh pages at
[L967] [31:59.76] some point like in the in the data model
[L968] [32:01.28] side and this was this like very gnarly
[L969] [32:03.84] migration it would have been you know to
[L970] [32:06.08] fully do it this is like many years and
[L971] [32:07.84] like probably hundreds of engineers to
[L972] [32:09.68] fully do it because you have to do it
[L973] [32:10.80] across like the data model the product
[L974] [32:12.88] layer integrity systems ad systems
[L975] [32:14.80] there's just all sorts of stuff that has
[L976] [32:16.64] to get merged and at the time Ysef
[L977] [32:18.96] Carver uh he just joined I think he came
[L978] [32:21.52] from either profile or events like a
[L979] [32:23.92] different or that that joined forces
[L980] [32:25.60] with groups to make this happen and he
[L981] [32:28.16] was working on it but he was kind of
