Chunk 3; segments 660–1000. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L669] [23:53.68] had to write like a defense of this
[L670] [23:54.96] because people at the time were saying
[L671] [23:56.56] like oh that they screwed up like this
[L672] [23:58.08] is an example of of how why you wouldn't
[L673] [24:00.00] want to do engineering this way or like
[L674] [24:01.68] you know don't write the code this way
[L675] [24:03.44] and so um again stuff like that always
[L676] [24:06.88] makes me think like the more things
[L677] [24:08.32] change the more they stay the same
[L678] [24:09.92] exactly what would happen on Twitter now
[L679] [24:11.52] right like like some very successful
[L680] [24:13.44] thing that people did right they would
[L681] [24:14.88] just get like slandered and say that it
[L682] [24:17.44] was done wrong and there would be like a
[L683] [24:18.72] flame war and then they'd have to come
[L684] [24:19.92] out and have a thing, you know. So,
[L685] [24:21.68] anyway, uh those are just some examples,
[L686] [24:23.76] but there's so much great stuff in
[L687] [24:26.08] there. I highly recommend anyone who
[L688] [24:27.60] likes this kind of thing, you won't be
[L689] [24:28.96] disappointed if you go if you go
[L690] [24:30.24] dumpster diving, as I call it.
[L691] [24:32.08] >> When you said that you saw the human
[L692] [24:34.64] stories and that Dystra was depressed at
[L693] [24:37.28] that time, what did you see that made
[L694] [24:40.16] you realize that?
[L695] [24:42.32] >> One of the nice things about Dystra is
[L696] [24:44.56] that he's kind of a pretty straight
[L697] [24:46.72] shooter. And so I didn't actually have
[L698] [24:49.76] to do any interpretation. He literally
[L699] [24:52.72] talks about like being depressed. And
[L700] [24:55.28] like he has like a there's a paper uh
[L701] [24:57.76] not a paper like a thing that he did
[L702] [25:00.64] that's like a retrospective
[L703] [25:02.80] um on that's like handwritten by him
[L704] [25:05.52] later on in life and he literally says
[L705] [25:07.92] like in this period I was very depressed
[L706] [25:10.32] because of these reasons. Now he could
[L707] [25:13.28] be wrong about the source of his
[L708] [25:14.80] depression, right? Uh, so I don't want
[L709] [25:16.64] to claim that that just because he said
[L710] [25:18.40] it it's ne necessarily true or something
[L711] [25:20.00] like that. But one of the amazing things
[L712] [25:23.44] I I think one of the the really cool
[L713] [25:26.64] things about academics
[L714] [25:29.04] uh especially that era is they just
[L715] [25:31.60] produced a voluminous amount of material
[L716] [25:34.32] and so we don't have to guess that much
[L717] [25:36.56] in the private sector. I think it'd be a
[L718] [25:38.24] lot harder like if you wanted to know uh
[L719] [25:40.64] what people at you know maybe
[L720] [25:44.08] you know Lockheed or something were
[L721] [25:46.24] thinking or doing at that time I imagine
[L722] [25:47.84] it's much more difficult just because
[L723] [25:49.68] you know things are classified or
[L724] [25:51.28] they're not academics so they're not
[L725] [25:52.32] necessarily going to write them all up
[L726] [25:53.84] uh you know so a lot of the internal
[L727] [25:55.12] stuff when we read up academics don't
[L728] [25:56.64] really have that they don't have an
[L729] [25:57.92] incentive or a prohibition on writing up
[L730] [26:00.48] everything they do so they don't just
[L731] [26:02.16] have to have like a public-f facing
[L732] [26:04.08] statement of what they did or a public
[L733] [26:06.00] facing paper of what they and then oh
[L734] [26:07.76] there's this extra secret stuff. The
[L735] [26:09.52] academics don't have that restriction.
[L736] [26:11.36] They're sort of they benefit from being
[L737] [26:14.00] as forthcoming as possible about what
[L738] [26:16.24] they've accomplished. Usually
[L739] [26:17.76] >> I saw in the in the slides that you
[L740] [26:20.40] looked at go to considered harmful that
[L741] [26:22.80] FEMA. Do you have any sense of the the
[L742] [26:25.36] personal or people side of that?
[L743] [26:27.74] [laughter]
[L744] [26:28.48] Uh, so you're talking about the original
[L745] [26:30.32] like Dystra letter to the editor that's
[L746] [26:32.32] like Ed's Gdystra go-to cons uh
[L747] [26:35.52] statement considered harmful. This okay
[L748] [26:38.64] um the complete story is actually
[L749] [26:40.40] relatively simple. He according to him
[L750] [26:44.64] he was at a uh at a conference um uh in
[L751] [26:49.12] Tennessee
[L752] [26:50.80] where he was talking to Brian Randelle
[L753] [26:54.24] who's another computer science guy. um
[L754] [26:56.56] he he doesn't quite get the same level
[L755] [26:58.56] of uh name recognition as a canth or
[L756] [27:01.28] something like that. Uh but he has a lot
[L757] [27:03.20] of papers at that time. Like you can go
[L758] [27:04.64] find him. He's not an obscure he's not
[L759] [27:06.16] an obscure figure. I wouldn't say uh to
[L760] [27:08.32] anyone who reads the history. You'll see
[L761] [27:10.00] him come up. He's talking to Brian
[L762] [27:11.76] Randell and some other people outside.
[L763] [27:13.84] This is exactly like the same thing that
[L764] [27:15.68] happens at modern conferences. There's
[L765] [27:17.68] like the talks and then there's all the
[L766] [27:20.00] stuff that goes down at the bar, right?
[L767] [27:21.84] It's it's very much that they're
[L768] [27:23.20] outside. talking
[L769] [27:25.52] and according to him he's basically
[L770] [27:28.64] giving the same sort of example of a
[L771] [27:32.72] problem with the goto that he gives in
[L772] [27:34.96] the paper right this idea of enumeration
[L773] [27:37.44] we can talk about that later if but um
[L774] [27:39.68] but the sort of a side note
[L775] [27:42.72] he's sort of saying like here this is
[L776] [27:44.56] kind of a problem with with goto and one
[L777] [27:47.04] of the reasons that maybe it's not such
[L778] [27:48.48] a good idea and the people who are
[L779] [27:51.60] listening to him were like you know
[L780] [27:53.04] Brian and the others were like you
[L781] [27:54.56] should p like you should publish that
[L782] [27:56.48] that would be helpful because you know
[L783] [27:58.32] there's these arguments going on about
[L784] [27:59.60] whether goto is good or bad like that
[L785] [28:01.20] was kind of happening at the time
[L786] [28:02.16] already uh since since around 1959 even
[L787] [28:05.52] I think there'd kind of been a little
[L788] [28:06.80] bit of that had been kind of growing
[L789] [28:09.04] this idea that maybe go-to statements
[L790] [28:10.88] weren't weren't um the best idea
[L791] [28:14.08] uh as a way to structure your programs
[L792] [28:16.32] and so he does he goes back to Einhovven
[L793] [28:20.16] and he writes up this same thing he
[L794] [28:23.04] saying basically and he sends it to to
[L795] [28:25.36] communications of the ACM for
[L796] [28:26.88] publication.
[L797] [28:28.72] uh Nicholas Worth who is like the
[L798] [28:31.44] creator of Pascal right a very prominent
[L799] [28:33.28] figure also uh was very heavily involved
[L800] [28:35.60] in alol and all this sort of stuff like
[L801] [28:37.28] you know language designer guy he is the
[L802] [28:40.24] editor uh who is in charge of like
[L803] [28:43.52] getting this getting this thing
[L804] [28:45.04] published I guess I'm not exactly sure
[L805] [28:46.72] how things work at at the communications
[L806] [28:48.24] of the ACM
[L807] [28:50.08] he doesn't want to wait to have it
[L808] [28:52.96] published he doesn't want to take the
[L809] [28:55.12] time to like go through the referee
[L810] [28:57.36] process or whatever. I don't know like
[L811] [28:59.36] at that time what the requirements were
[L812] [29:01.36] for publishing a article in
[L813] [29:03.68] communications with the ACM but I'm sure
[L814] [29:05.68] that it involved a lot of procedure.
[L815] [29:08.08] wasn't just like, "Oh, hey, I'm, you
[L816] [29:09.84] know, I'm the creator of Pascal."
[L817] [29:11.84] Although that that time he wouldn't have
[L818] [29:13.04] been the creator of Pascal yet because
[L819] [29:14.40] Pascal comes later, I think, but but
[L820] [29:15.92] either way, he's like, "Hey, I'm this
[L821] [29:17.44] important guy. I'm just going to put
[L822] [29:18.72] this whatever I want communication."
[L823] [29:20.40] That's not how it worked. And so he
[L824] [29:22.96] decides that in order to get it
[L825] [29:24.32] published more quickly, he's just going
[L826] [29:25.84] to publish it as a letter to the editor
[L827] [29:27.84] because then there's no pro like any,
[L828] [29:29.68] you know, anything goes there as long as
[L829] [29:31.12] the editors are fine with the content, I
[L830] [29:32.48] assume. Like it doesn't have to be
[L831] [29:33.44] refereed, doesn't have to have any kind
[L832] [29:34.80] of review, it doesn't have to uh etc,
[L833] [29:36.88] etc.
[L834] [29:38.56] So, he turns it into a letter to the
[L835] [29:40.56] editor and he takes the name of the
[L836] [29:43.76] thing that Dystra sent, which was a case
[L837] [29:46.48] against the go-to statement. That was
[L838] [29:48.48] what Dyster wrote at the top of the
[L839] [29:50.24] thing as the title. He changes it for
[L840] [29:53.36] letters to the editor to Edgar Dystra
[L841] [29:57.28] go-to statement considered harm or
[L842] [29:59.76] considered harmful. Right?
[L843] [30:02.00] So, it wasn't it wasn't even Dyster's
[L844] [30:05.44] plan to like have it maybe be that
[L845] [30:08.00] confrontational,
[L846] [30:09.76] but that's what happens. Um, now this is
[L847] [30:13.28] not
[L848] [30:14.80] wellreceived to say the least. Uh, the
[L849] [30:19.20] according to can
[L850] [30:21.44] uh again I'm just trying to say who said
[L851] [30:23.20] what here. According to Canuth, Dystra
[L852] [30:26.16] said he got letters like like angry like
[L853] [30:30.16] threatening letters like uh in much the
[L854] [30:32.64] same way you would today, right? Like he
[L855] [30:34.32] got got people who were uh very abusive
[L856] [30:36.88] and at you know telling him off
[L857] [30:39.84] and I'm sure part of that is because by
[L858] [30:42.00] all accounts Dystra himself was also
[L859] [30:44.40] somebody who liked to push people's
[L860] [30:45.68] buttons. That's well acknowledged. Um I
[L861] [30:47.84] think Alan Kay is probably the best
[L862] [30:49.20] source for this. He talks about uh this
[L863] [30:51.44] uh he liked Dystra and they apparently
[L864] [30:53.44] got along well, but you know he he's
[L865] [30:56.16] often said that Dystra was someone who
[L866] [30:57.68] kind of leaned into the being uh sort of
[L867] [31:01.36] brash about stating things about
[L868] [31:03.36] programming and uh and kind of relished
[L869] [31:06.40] that position. So it probably didn't
[L870] [31:08.40] help that he was already sort of known a
[L871] [31:10.16] little bit in that way. But in general
[L872] [31:12.72] that's that's how it went down. And
[L873] [31:15.29] [clears throat]
[L874] [31:16.72] like I said, that wasn't the initial
[L875] [31:20.24] foray against goto statements by any
[L876] [31:22.96] stretch of the imagination, but it it
[L877] [31:25.44] just kind of
[L878] [31:27.60] maybe you call it the straw that broke
[L879] [31:28.96] the camel's back. It was like a it was
[L880] [31:30.64] like a flash point might be the way to
[L881] [31:32.24] say it. And so, and then the title of
[L882] [31:34.80] course be that Nicholas Berth picked uh
[L883] [31:38.08] is quite the doozy and kind of
[L884] [31:40.08] clickbaited everyone, you know, as I
[L885] [31:41.76] call it into that.
[L886] [31:43.68] It's funny. Yeah. Cuz I mean your social
[L887] [31:45.84] media, it's similar patterns, right?
[L888] [31:47.60] People have very explosive first lines
[L889] [31:50.72] and then the comments are full of all
[L890] [31:52.96] this [laughter] hate and stuff. In in
[L891] [31:55.52] their case, I'm guessing this is all
[L892] [31:57.60] papers. So you submit a letter to that.
[L893] [32:00.00] It's a physical thing and people are
[L894] [32:02.48] reading uh
[L895] [32:03.84] >> maybe a newspaper or something. I don't
[L896] [32:05.04] know what.
[L897] [32:05.36] >> Yeah, it's like a periodical like it
[L898] [32:06.88] comes, you know, as a bound. I mean, I
[L899] [32:08.56] guess there's all the things around us
[L900] [32:10.00] here are hard bound, but it's like
[L901] [32:11.68] usually was soft. It was a you know
[L902] [32:13.36] maybe a perfect binding uh kind of bound
[L903] [32:17.28] thing that has you you open it up table
[L904] [32:19.20] of contents and letters editor right and
[L905] [32:22.08] uh yeah like you can go find there are
[L906] [32:26.00] there are a few if you go look at
[L907] [32:28.16] people's personal papers which like like
[L908] [32:29.76] I said if I did this full-time I'm sure
[L909] [32:32.48] I could find out way more stuff than I
[L910] [32:34.48] did right
[L911] [32:36.32] but some people have gone and looked at
[L912] [32:37.76] the personal papers and occasionally
[L913] [32:39.76] some of them have been able to digitize
[L914] [32:41.52] some of those and put them online that
[L915] [32:42.96] we can look at and you can find for
[L916] [32:45.76] example online right now if you search
[L917] [32:47.52] for it uh
[L918] [32:50.96] there's a there's a back and forth
[L919] [32:52.80] letters personal letters between Dystra
[L920] [32:55.52] and a guy who is kind of into functional
[L921] [32:57.60] programming and promoting that and like
[L922] [32:59.60] you can look at the correspondence and
[L923] [33:01.92] it's kind of it's a little it's a little
[L924] [33:05.36] flame worry like like it it really like
[L925] [33:08.08] that's what they did they they didn't
[L926] [33:09.76] have the ability to do like pathy
[L927] [33:11.20] Twitter replies So it was just on paper.
[L928] [33:15.04] Uh and yeah and Canuth did something
[L929] [33:18.24] similar. It wasn't really a flame
[L930] [33:19.92] because he had a at least when reading
[L931] [33:22.56] it comes through as a tremendous amount
[L932] [33:24.40] of respect for the authors of the book
[L933] [33:26.16] structured programming which is uh
[L934] [33:28.08] Dystra and doll. Um he you know
[L935] [33:32.40] one of the things that he published was
[L936] [33:33.92] a series of open letters to them
[L937] [33:36.48] reviewing the book and talking about the
[L938] [33:38.64] things that he didn't find compelling in
[L939] [33:39.92] it. Right? like very respectful. So, it
[L940] [33:43.04] wasn't that one wasn't a a flame war.
[L941] [33:45.52] But that's what they Yeah, that's what
[L942] [33:46.96] they had to do because they didn't have
[L943] [33:48.48] social media. So, you know, Edgar
[L944] [33:51.20] Dystra's uh he wrote like all these
[L945] [33:53.60] things called EWD with a number. It was
[L946] [33:56.24] it was his initials basically. Um and
[L947] [33:59.28] then a number and that's like this like
[L948] [34:01.52] serialized list of all the things he
[L949] [34:03.28] wrote. And he like labels them this way.
[L950] [34:05.28] Like it's not like some historian
[L951] [34:06.80] characterized it after the fact. just
[L952] [34:08.08] like, "Oh, I'm doing a He's like, "I'm
[L953] [34:10.16] doing EWD 937 now." or whatever, right?
[L954] [34:12.96] It's hilarious. Uh, but anyway,
[L955] [34:17.04] several of those have been put online
[L956] [34:19.36] that are not necessarily technical.
[L957] [34:21.76] Like, for example, his trip reports. You
[L958] [34:24.00] can go read those and you can read about
[L959] [34:25.68] like, oh, like I went and I went and
[L960] [34:27.76] stayed at like such and such's house and
[L961] [34:29.84] like we went to dinner or whatever,
[L962] [34:31.12] right? So, you can find like some nice
[L963] [34:33.04] personal anecdotes in even the publicly
[L964] [34:35.12] available stuff. But in terms of like a
[L965] [34:37.28] real like heart-to-heart conversation, I
[L966] [34:39.92] didn't have access to anything like that
[L967] [34:41.60] that wouldn't have just been in a paper
[L968] [34:43.44] more or less normally. Um, so, you know,
[L969] [34:47.04] it's it's a shame. One of the problems
[L970] [34:49.60] with this stuff, it's so interesting,
[L971] [34:52.40] but it's not a job to do. Like, it's
[L972] [34:55.04] like if somehow it was a job, I probably
[L973] [34:57.12] would almost take that job. like like
[L974] [34:59.44] being the person who crawls through and
[L975] [35:00.88] tries to like redo this whole thing.
[L976] [35:03.04] But, you know, computer historian, no
[L977] [35:05.04] one's no one's hiring. Like that's not
[L978] [35:07.36] no one's interested in paying for that.
[L979] [35:08.88] So,
[L980] [35:10.00] >> you have this other talk and the title
[L981] [35:12.32] was just so catching. It was the big
[L982] [35:14.72] oops anatomy of a 35-year mistake.
[L983] [35:18.24] >> Yes.
[L984] [35:18.72] >> What is that 35-year mistake?
[L985] [35:21.12] >> Um, so this was a this was a kind of
[L986] [35:24.64] funny thing that happened to me that I
[L987] [35:26.88] uh then did a historical lecture on I
[L988] [35:32.32] I had worked on systems in the past that
[L989] [35:35.36] were basically like editors like you
[L990] [35:37.84] know you have to m like three 3D
[L991] [35:39.68] graphics editors like you have to multi
[L992] [35:41.12] select things and move them around and
[L993] [35:43.20] there's a bunch of like architecture
[L994] [35:44.72] things you have to learn to be able to
[L995] [35:46.16] write that kind of code and and certain
[L996] [35:47.92] kinds of problems you have to solve like
[L997] [35:49.68] a a very basic one that I would point
[L998] [35:51.76] out that hopefully most people can
[L999] [35:53.28] relate to would be if I have a bunch of
[L1000] [35:57.04] things on the screen. Uh some of which
[L1001] [35:59.20] have a color. So maybe maybe this is a
[L1002] [36:01.92] drawing program and I've got some text
[L1003] [36:03.60] and I've got some shapes and I've got um
[L1004] [36:05.76] some uh strokes, you know, some some
[L1005] [36:08.64] handdrawn stuff, whatever. And I want to
[L1006] [36:10.80] be able to to select a bunch of them and
[L1007] [36:13.20] I want the user interface to present to
[L1008] [36:15.68] me which things I could edit on these
[L1009] [36:18.40] shapes. So I want to be able to edit the
