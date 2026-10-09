Chunk 3; segments 627–951. Start may repeat the previous chunk for context.

# Instagram iOS Principal Eng (IC8): Building IG Stories, 1 Promo Per Half, Small Teams

Source ID: source-77b7f65a700842eb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Instagram_iOS_Principal_Eng_(IC8)_Building_IG_Stories,_1_Promo_Per_Half,_Small_Teams_en.txt
Video: https://www.youtube.com/watch?v=gpVETZnY9Y0

[L636] [25:27.60] saying that icon is black it's like it's
[L637] [25:29.68] icon color or something like that. um or
[L638] [25:32.80] it's disabled icon color and then you
[L639] [25:35.60] could switch inside of that function for
[L640] [25:38.32] you know are we on the new design or the
[L641] [25:40.08] old design. Um [snorts] and so that
[L642] [25:42.56] ended up being just kind of a much
[L643] [25:44.16] easier way to to build it incrementally.
[L644] [25:46.80] And then it also actually opened up the
[L645] [25:48.96] possibility of testing it. Um and so we
[L646] [25:52.56] we went to to ship it and it was going
[L647] [25:55.52] to be just like a 2% hold out. So, like,
[L648] [25:58.88] you know, we were going to ship the new
[L649] [26:00.40] icon. Um, it 98% of people were going to
[L650] [26:04.08] have the new design and then we were
[L651] [26:06.40] just going to have like 2% of people,
[L652] [26:08.96] you know, with the old design just to
[L653] [26:11.20] make sure that like nothing was was
[L654] [26:13.20] broken or changed drastically. And uh I
[L655] [26:16.56] had submitted the app to Apple. I I
[L656] [26:18.80] dropped in the new icon. You know, we
[L657] [26:20.40] were ready to go. People had champagne
[L658] [26:22.24] ready for the launch party. And it was
[L659] [26:23.68] like the night before we were supposed
[L660] [26:25.60] to to launch this thing. And um someone
[L661] [26:30.64] kind of in the Facebook executive ex
[L662] [26:32.96] executive team above uh Instagram came
[L663] [26:37.04] in and was like no [snorts] you guys are
[L664] [26:39.04] not doing this.
[L665] [26:41.04] Um I guess they Facebook had had a
[L666] [26:43.52] redesign that went poorly. Um and they
[L667] [26:47.36] just saw this as the same thing and uh
[L668] [26:50.64] and so they were like you need to run AB
[L669] [26:52.56] tests of this up front. Um, so I I was
[L670] [26:55.60] up at like 1:00 a.m. just like backing
[L671] [26:57.60] things out and trying to like resubmit
[L672] [26:59.44] the app to Apple and uh we we tested it.
[L673] [27:03.84] I actually tested really well. Um
[L674] [27:06.38] [clears throat] was a little bit sad
[L675] [27:07.52] because it kind of crushed like the
[L676] [27:09.20] launch that we we had planned. Um you
[L677] [27:12.08] know cuz then there are all these
[L678] [27:13.76] articles about this new UI that
[L679] [27:15.76] Instagram's maybe going to do. Um
[L680] [27:18.17] [snorts] but uh but yeah, I mean it all
[L681] [27:20.80] worked out. Um but I I did have a a
[L682] [27:24.48] takeaway from that which is like um I
[L683] [27:27.28] mean testing definitely has a a place.
[L684] [27:30.80] It's extremely useful even in our
[L685] [27:32.64] startup you know we test things where
[L686] [27:35.36] you sometimes get counterintuitive
[L687] [27:37.44] results um things in our onboarding flow
[L688] [27:40.56] how people convert on things um it's
[L689] [27:43.44] extremely useful to run AB tests for
[L690] [27:45.36] that I think for like highle product
[L691] [27:48.24] direction and like what you want the
[L692] [27:49.84] thing to be I I prefer to come in with a
[L693] [27:52.56] a stronger opinion and not just kind of
[L694] [27:55.12] like um look at the look at the data and
[L695] [27:58.88] only let the the data guide the
[L696] [28:01.20] decisions.
[L697] [28:02.72] Um, so I I think there's a risk if you
[L698] [28:06.24] do too much experimentation that you get
[L699] [28:08.00] trapped in kind of incrementalism.
[L700] [28:10.24] So it's, you know, easy to get those 1%
[L701] [28:12.40] wins, but you're never going to get that
[L702] [28:14.24] 50% uh jump.
[L703] [28:16.64] >> On the major redesign case though, if
[L704] [28:19.20] you just went for it though too, there's
[L705] [28:21.60] also the other side risk though, right?
[L706] [28:23.36] which is your product taste might be off
[L707] [28:26.96] and people hate it and then it's a a
[L708] [28:29.76] pain to come back.
[L709] [28:31.28] >> Yeah. Yeah, for sure. Um I I think we we
[L710] [28:36.80] had enough confidence I guess in in
[L711] [28:38.96] using it. I mean it felt really good
[L712] [28:40.80] internally and um I think at least on
[L713] [28:45.36] the inter in kind of redesigning the
[L714] [28:47.76] app, we we thought that would be good.
[L715] [28:49.84] Um the icon was definitely a little bit
[L716] [28:51.76] more controversial and then when we
[L717] [28:54.24] shipped that people hated it. I mean it
[L718] [28:57.36] was like I say it's the last time I
[L719] [28:58.88] looked at Twitter after our product
[L720] [29:00.24] launch because I went on and you know it
[L721] [29:02.80] was supposed to be the celebratory day.
[L722] [29:04.32] We had worked so hard on this thing. it
[L723] [29:05.76] went out and we were just getting raked
[L724] [29:08.16] on Twitter and uh yeah I mean it was it
[L725] [29:12.24] was kind of sad but I think you know
[L726] [29:14.88] change is hard. Um especially I think
[L727] [29:18.24] people feel ownership over their home
[L728] [29:20.32] screens and and all of a sudden this
[L729] [29:22.64] thing just changed on them. Um and
[L730] [29:25.24] [snorts] it was kind of like a a little
[L731] [29:27.44] bit more of a bleeding edge design
[L732] [29:28.96] direction too. Like I think the the flat
[L733] [29:31.20] icon and the gradient, you know, today
[L734] [29:33.52] feels very at home, but at that time a
[L735] [29:36.16] lot of the icons were pretty skephic and
[L736] [29:38.08] 3D. Yeah. So so it was a bit rough. The
[L737] [29:41.60] the funny other thing from that, you
[L738] [29:44.00] know, we could see from the data
[L739] [29:45.60] actually that uh this icon change uh it
[L740] [29:49.76] materially improved how many people a
[L741] [29:52.48] day open the app. Um, and we've actually
[L742] [29:56.32] seen this in in um the app of my new
[L743] [30:00.16] company called Retro, but actually like
[L744] [30:02.80] the icon uh can impact whether people
[L745] [30:06.48] open the app like how visible it is to
[L746] [30:08.40] them on on the screen. So, it became
[L747] [30:10.64] more noticeable I think amongst the
[L748] [30:12.32] other icons and people actually uh
[L749] [30:15.84] tapped it more often. It reminds me of I
[L750] [30:18.80] think some of Thomas Dimson's work on
[L751] [30:21.36] the ranking versus chronological
[L752] [30:25.36] like the public perception is so
[L753] [30:27.52] different from how actually people are
[L754] [30:30.48] voting with their usage. Like people are
[L755] [30:32.88] using it a lot more when it's when it's
[L756] [30:34.88] ranked but you know for some reason
[L757] [30:37.20] there's this like very vocal minority
[L758] [30:39.20] that is saying I absolutely hate this.
[L759] [30:42.40] >> Totally. Yeah. that that actually um the
[L760] [30:45.12] feed ranking um shipped about the same
[L761] [30:47.76] time as as this redesign and
[L762] [30:51.44] uh I mean I was actually skeptical of it
[L763] [30:53.92] as well. Um the the metric that changed
[L764] [30:58.40] my mind on the ranking which I think the
[L765] [31:01.20] story might be a little bit different
[L766] [31:02.40] today but um [snorts]
[L767] [31:04.72] at the time uh one of the things that
[L768] [31:07.12] moved was actually how often people
[L769] [31:09.20] shared to Instagram. So people that had
[L770] [31:12.56] this uh feed ranking experience were
[L771] [31:15.04] actually creating more themselves. They
[L772] [31:16.96] were sharing more. Um and it was partly
[L773] [31:19.92] because the feed ranking allowed uh
[L774] [31:22.88] Instagram to show them their friends
[L775] [31:25.28] more often. Um and so you saw content
[L776] [31:30.08] from people like you and I think you
[L777] [31:32.96] wanted to have that mutual connection so
[L778] [31:34.56] you would actually share more yourself.
[L779] [31:36.72] And so that kind of was an insight that
[L780] [31:39.36] flipped it in my mind where, you know,
[L781] [31:42.08] cuz people would say, "Oh, I'm just
[L782] [31:43.60] using the app more because like you're
[L783] [31:45.04] not showing me the things I want, so I'm
[L784] [31:46.64] scrolling further or whatever." But I
[L785] [31:48.80] was kind of like, "Okay, they're
[L786] [31:49.84] actually like creating more content."
[L787] [31:51.36] That that's kind of hard to dispute.
[L788] [31:53.36] Like that's that's probably a good
[L789] [31:55.12] thing. Um I I really liked uh kind of
[L790] [32:00.00] the mission the original mission of
[L791] [32:01.60] Instagram was like capture and share the
[L792] [32:03.44] world's moments. And I I really liked it
[L793] [32:05.36] as a way to kind of encourage people to
[L794] [32:08.40] be creative and see beauty in the world.
[L795] [32:11.36] And that was just a mission I felt like
[L796] [32:13.28] I could get behind. And so something
[L797] [32:15.76] like this where people were actually
[L798] [32:17.84] creating more, I was like, "Okay, yeah,
[L799] [32:19.36] that that that's probably a good thing."
[L800] [32:21.28] I think at this leg of your career, I
[L801] [32:23.28] think one thing that you wrote you wrote
[L802] [32:25.44] about is that, you know, finding an
[L803] [32:27.68] amazing designer was like a big part of
[L804] [32:29.60] it for you. And so I'm curious, how did
[L805] [32:32.56] you find the amazing designer that you
[L806] [32:35.12] did work with and what makes a great
[L807] [32:37.52] designer great?
[L808] [32:38.72] >> Yeah, I've always just tried to, you
[L809] [32:40.24] know, be be the engineer that like the
[L810] [32:42.40] top designers want to work with. Um, and
[L811] [32:47.28] yeah, it's just an incredible
[L812] [32:48.96] opportunity if you work at these types
[L813] [32:50.32] of companies where you can just have
[L814] [32:52.56] their work kind of flow through you. Um,
[L815] [32:55.12] be a part of it. Um so that for product
[L816] [32:58.56] engineers that that's one piece of
[L817] [33:00.24] advice I often give is like um your
[L818] [33:03.38] [clears throat] impact can be multiplied
[L819] [33:05.20] so much by finding a good designer and
[L820] [33:08.56] and creating a really good working
[L821] [33:10.40] relationship with them.
[L822] [33:11.76] >> Is there a reason why you say
[L823] [33:14.48] specifically the design function versus
[L824] [33:16.64] the engineering function? Like imagine I
[L825] [33:19.04] I identify some very senior engineer
[L826] [33:22.16] that has some engineering design and I
[L827] [33:24.80] just devote myself to it and kind of
[L828] [33:26.88] attach to them. What's the difference
[L829] [33:28.96] between doing that versus the really
[L830] [33:31.12] talented designer? So I should make a
[L831] [33:33.68] bit of a distinction between like if
[L832] [33:35.52] you're in sort of a product engineering
[L833] [33:37.60] um function where you're you're working
[L834] [33:39.28] on like the features for users, the
[L835] [33:41.52] interface kind of the front end then I
[L836] [33:43.36] think like you know that's where you
[L837] [33:45.20] really want to pair with a designer. If
[L838] [33:47.20] you're in a more infrastructure role,
[L839] [33:49.28] maybe the analogy is like finding that
[L840] [33:51.76] really talented um super senior engineer
[L841] [33:55.44] uh and and being the engineer they want
[L842] [33:58.32] to work with. Um you know, they've got
[L843] [34:01.20] great ideas and you can kind of
[L844] [34:03.20] implement that. So yeah, probably
[L845] [34:04.88] different depending on kind of uh what
[L846] [34:07.28] role you have.
[L847] [34:08.88] >> And so this white out project was in
[L848] [34:10.96] 2016. I'm kind of surprised in the same
[L849] [34:13.76] year you also built stories with Tiger
[L850] [34:17.68] Squad of some very famous people I'm
[L851] [34:19.44] aware of. Can you tell me the story
[L852] [34:21.28] about you know building stories for
[L853] [34:23.92] Instagram?
[L854] [34:24.64] >> Uh the redesign wrapped up and um I had
[L855] [34:28.56] actually been kind of kicked off my my
[L856] [34:31.44] uh previous team. Um right after I
[L857] [34:35.20] joined they said we're moving the team
[L858] [34:36.64] to New York. Do you want to move to New
[L859] [34:38.08] York? And I was like no.
[L860] [34:41.68] I I kind of I'm okay here in California.
[L861] [34:44.24] They're like, "Okay, that's fine. Well,
[L862] [34:45.44] you just have to find a new team." I was
[L863] [34:46.96] like, "Okay, I I kind of wanted to be on
[L864] [34:49.84] this team." Um so, um I kind of like
[L865] [34:53.60] delayed it. I worked on this uh redesign
[L866] [34:56.16] project and um then I joined the search
[L867] [34:59.52] and explore team. Um, and I was only on
[L868] [35:04.56] the team for a couple of weeks and a
[L869] [35:08.40] friend of mine, um, who was also an iOS
[L870] [35:11.60] engineer at the company decided to quit
[L871] [35:14.16] and he had been working on what was
[L872] [35:16.08] called the creation team and leading the
[L873] [35:18.96] project that would become stories. And
[L874] [35:22.56] uh my manager um was like, "Hey, you
[L875] [35:27.12] know, this is actually a really
[L876] [35:28.72] important effort for the company. Like,
[L877] [35:31.84] I don't necessarily want you to lead my
[L878] [35:33.76] team, but like I think this is a good
[L879] [35:35.12] opportunity for you." And um I really
[L880] [35:37.76] believed in in what this team was trying
[L881] [35:39.60] to do. Um, at that time it it's sort of
[L882] [35:44.56] surprising in hindsight given how big
[L883] [35:46.56] Instagram is today, but it actually felt
[L884] [35:49.04] in some ways like Instagram was dying
[L885] [35:51.60] because a lot of the sort of everyday
[L886] [35:54.32] sharing uh from people you knew, normal
[L887] [35:57.36] people was evaporating. It was kind of
[L888] [36:01.44] being replaced by creators and
[L889] [36:03.76] influencers.
[L890] [36:05.28] And uh some of that everyday sharing was
[L891] [36:08.24] going to Snapchat which had this
[L892] [36:09.76] ephemeral format. Um [snorts] and so we
[L893] [36:13.12] were tasked with just you know how do we
[L894] [36:15.60] get kind of normal people to feel
[L895] [36:18.16] comfortable sharing to Instagram again.
[L896] [36:20.80] So I I went over to to lead the iOS team
[L897] [36:24.40] on stories and
[L898] [36:27.28] uh one of the first things we did after
[L899] [36:30.48] I joined the team is we actually cut the
[L900] [36:32.48] team size significantly. So there had
[L901] [36:35.12] been a lot of people working on it. It
[L902] [36:36.80] had been pretty churny. Um they had
[L903] [36:39.20] tried different product directions. Uh a
[L904] [36:41.92] lot of them didn't really feel that
[L905] [36:44.32] great. They weren't working out. And in
[L906] [36:47.84] some ways they were working on things to
[L907] [36:49.84] have work for people to do um or or
[L908] [36:54.00] there was just like not um not enough
[L909] [36:56.64] space for the people that were there.
[L910] [36:58.08] And we just decided, hey, we can
[L911] [36:59.76] actually move a lot faster if we go down
[L912] [37:02.00] to a smaller team. So, uh, it was myself
[L913] [37:05.12] and one other iOS engineer was kind of
[L914] [37:06.88] like the core team, and then we'd get
[L915] [37:08.40] some help from other iOS engineers, two
[L916] [37:11.04] Android engineers, and we didn't even
[L917] [37:12.88] have a dedicated server engineer. It was
[L918] [37:15.76] the infrastructure team, or like you can
[L919] [37:18.00] have half a person. Um, it's half their
[L920] [37:21.04] time. Uh, which, you know, for what
[L921] [37:24.48] stories has become, it's it seems kind
[L922] [37:26.32] of crazy. Uh, but it it really allowed
[L923] [37:28.80] us to to move quickly. Um, you had
[L924] [37:31.92] ownership over the whole thing. So, it's
[L925] [37:33.60] never like a question of am I working on
[L926] [37:35.92] something that someone else is working
[L927] [37:37.28] on, am I going to step on their toes?
[L928] [37:39.52] You know, if there's a bug, it's like,
[L929] [37:41.28] okay, that's that's my bug. I got to go
[L930] [37:43.20] fix it. And uh and there was less
[L931] [37:47.76] discussion around decisions, we could
[L932] [37:49.68] just make them more quickly. I say like
[L933] [37:51.92] if you want to go fast, go small. Uh and
[L934] [37:54.56] I'm a a strong believer in small teams
[L935] [37:57.12] as like really the best way to operate.
[L936] [37:59.68] Um it's definitely not the only way to
[L937] [38:02.32] operate, but it's my preferred way. And
[L938] [38:04.72] uh yeah, so we we went through that and
[L939] [38:07.36] um we built it just over two to three
[L940] [38:10.32] months. Was pretty quick. I
[L941] [38:14.72] never worked so hard in my life. I was
[L942] [38:18.56] working Yes. like 16 18 hour days, 7
[L943] [38:22.00] days a week. Uh in the office every
[L944] [38:25.04] weekend.
[L945] [38:26.64] Yeah. I would like leave at like 1 or 2
[L946] [38:29.68] a.m. to go home. I was driving back and
[L947] [38:31.92] forth from San Francisco. I I was really
[L948] [38:34.48] determined to not sleep in the office. I
[L949] [38:36.48] was like, you know what? I'm always
[L950] [38:37.84] going to go home, see my girlfriend. And
[L951] [38:40.56] it was kind of silly because I was
[L952] [38:42.08] spending this extra time driving. I
[L953] [38:43.60] really should have just slept in the
[L954] [38:44.88] office. Uh but um yeah, it was intense,
[L955] [38:49.52] but it was fun. It felt like we were
[L956] [38:51.20] building something really important and
[L957] [38:54.72] we were using the product ourselves. We
[L958] [38:57.36] were really enjoying it. It also was
[L959] [38:59.60] like this bonding experience amongst
[L960] [39:01.44] this small team. So our PM on the
