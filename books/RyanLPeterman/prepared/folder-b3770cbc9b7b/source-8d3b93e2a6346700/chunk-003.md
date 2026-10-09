Chunk 3; segments 755–1149. Start may repeat the previous chunk for context.

# Airbnb Staff Eng: Untold Rules of Calibrations and How To Not Get Stuck at Senior

Source ID: source-8d3b93e2a6346700
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Airbnb_Staff_Eng_Untold_Rules_of_Calibrations_and_How_To_Not_Get_Stuck_at_Senior_en.txt
Video: https://www.youtube.com/watch?v=cgQY_1Uz2b8

[L764] [28:06.16] only one. Like pretty much everybody
[L765] [28:08.36] uh disliked that metric even the people
[L766] [28:10.40] who suggested it
[L767] [28:12.32] because we all know it's it's a bad way
[L768] [28:14.64] to evaluate
[L769] [28:16.20] uh
[L770] [28:16.76] engineering output. So instead what I've
[L771] [28:18.56] done
[L772] [28:20.40] is I looked at the journey of when you
[L773] [28:23.28] make a change, when you go from your
[L774] [28:25.12] branch to merging your change, there's a
[L775] [28:28.32] whole journey. How long does it take?
[L776] [28:32.00] What do you do in those phases? Like so
[L777] [28:34.44] first you're thinking, then you're
[L778] [28:35.76] writing your code, then you are sending
[L779] [28:39.04] the code to CI, code review, going back
[L780] [28:41.32] and forth, things like this. And so once
[L781] [28:43.04] you start to look at this and you start
[L782] [28:44.48] to look at the journey of like the
[L783] [28:46.80] changes,
[L784] [28:48.24] you'll notice that you get a lot more
[L785] [28:50.28] interesting data than if you just look
[L786] [28:52.24] at the number of like lines of code or
[L787] [28:54.44] PR. You can see that say in an
[L788] [28:55.88] organization, it takes them twice as
[L789] [28:58.92] long to make a code change than in
[L790] [29:00.72] another organization. And that gives you
[L791] [29:02.60] a lot of lever
[L792] [29:04.16] to like
[L793] [29:05.12] go look into but like why does it take
[L794] [29:07.40] them twice as long? How can you help
[L795] [29:09.64] them? And that reframe the question
[L796] [29:11.24] about like measuring the output
[L797] [29:13.60] which should ultimately be
[L798] [29:15.88] the manager assesses all the work that
[L799] [29:17.92] someone is doing regardless of if it's
[L800] [29:19.60] code or not to the question about like
[L801] [29:22.56] how fast are they at like when they're
[L802] [29:24.96] like
[L803] [29:25.96] doing good, which is much more
[L804] [29:27.04] objective.
[L805] [29:28.20] And I'm not I'm not saying that if
[L806] [29:29.40] you're fast at like shipping code, that
[L807] [29:31.76] means you're very productive and that
[L808] [29:34.36] people who are slow at shipping code are
[L809] [29:36.16] not productive. I'm saying if someone is
[L810] [29:38.68] slow at shipping code and everyone else
[L811] [29:40.96] is fast,
[L812] [29:42.24] then you have to look into why the
[L813] [29:43.40] person is slow because that's very very
[L814] [29:45.60] useful signal. Cuz like maybe they work
[L815] [29:47.88] in a code base that's horrible. Maybe
[L816] [29:49.56] they use like an
[L817] [29:51.20] uh
[L818] [29:52.04] a process that's very inefficient.
[L819] [29:54.56] Before we leave your experience at
[L820] [29:56.80] Airbnb, I'm kind of curious if anything
[L821] [30:00.12] struck you about Airbnb's engineering
[L822] [30:02.80] culture. I know prior to that you had
[L823] [30:05.32] experience at Meta and Apple. So, um
[L824] [30:08.36] what was kind of notable when you got to
[L825] [30:10.44] Airbnb?
[L826] [30:12.00] It was a company that it still is
[L827] [30:15.52] uh led by designers.
[L828] [30:18.48] So, it was harder to explain
[L829] [30:22.60] why
[L830] [30:23.92] the low-level infrastructure
[L831] [30:28.04] thing about the code really matter. It
[L832] [30:30.28] also has some upsides because I think
[L833] [30:32.04] that by virtue of like coming from a
[L834] [30:34.72] different trade, they add
[L835] [30:37.56] uh different ideas that were also very
[L836] [30:39.80] good. So, like one thing that they that
[L837] [30:41.08] they've done at Airbnb that I thought
[L838] [30:42.36] was like really amazing
[L839] [30:44.20] is
[L840] [30:45.40] we were
[L841] [30:46.44] we were having a lot of incidents, a lot
[L842] [30:48.00] of reliability problems. And they said,
[L843] [30:50.76] "You know what is really good at solving
[L844] [30:52.76] those things? People who are like
[L845] [30:54.92] working in emergency situation,
[L846] [30:57.00] firefighters.
[L847] [30:58.52] People who are dealing with like actual
[L848] [31:00.80] real disasters. So, we're going to hire
[L849] [31:02.96] people from that background
[L850] [31:05.40] who are like super good at like the
[L851] [31:06.68] crisis management and we're going to
[L852] [31:08.16] say, 'Now you're in charge of this
[L853] [31:09.92] thing.'
[L854] [31:11.20] And you're going to like change the way
[L855] [31:13.48] we do the internet measurement. That was
[L856] [31:15.04] genius because it's like
[L857] [31:17.24] uh
[L858] [31:17.88] it brought a lot of rigor
[L859] [31:19.92] and interesting practices that then I
[L860] [31:23.08] took at every job I went after that.
[L861] [31:25.08] It's like it's it it's something that's
[L862] [31:27.24] very important to to get right and I
[L863] [31:29.08] think that that mindset of thinking
[L864] [31:31.12] outside of the box like, "Hey, who's
[L865] [31:32.56] good at doing that? Firefighter." Then
[L866] [31:34.68] that worked.
[L867] [31:36.20] You left Airbnb for Meta. It was just a
[L868] [31:38.96] boomerang cuz you'd already been at
[L869] [31:40.36] Meta. I'm curious what made you want to
[L870] [31:42.32] leave Airbnb and go to Meta.
[L871] [31:44.56] Well,
[L872] [31:45.96] uh so like I said, I joined in 2016. It
[L873] [31:48.16] was 2020. 4 years in. So, at that point
[L874] [31:52.68] uh you were getting 4 years grant when
[L875] [31:54.88] you work for like the those tech
[L876] [31:56.04] companies. So, that means I had
[L877] [31:58.40] um
[L878] [32:00.24] a cliff of stock. And so, at that point
[L879] [32:02.76] I started to like
[L880] [32:04.36] uh my earning potential started to
[L881] [32:06.08] decrease.
[L882] [32:07.68] Uh
[L883] [32:08.40] and that's generally what happened at
[L884] [32:09.80] like at like 4 years unless you manage
[L885] [32:12.32] to like score a lot of like stock
[L886] [32:14.72] refreshers. So, I think part of it was
[L887] [32:16.20] like financially motivated. Uh another
[L888] [32:18.76] part was I
[L889] [32:21.92] thought
[L890] [32:23.32] because I worked on tested for I worked
[L891] [32:25.16] on compute, I worked on databases, I
[L892] [32:27.12] worked on all all around like different
[L893] [32:29.60] infra teams that I wanted to be an infra
[L894] [32:31.76] generalist.
[L895] [32:33.76] I was wrong.
[L896] [32:35.12] Uh but I thought I wanted to be.
[L897] [32:37.32] And so, I looked for infra generalist
[L898] [32:39.56] job and that's how I landed the job at
[L899] [32:42.08] Instagram.
[L900] [32:43.44] I got to be on call for
[L901] [32:46.52] the 4th of July for Instagram. And
[L902] [32:50.28] I remember I was trying to like go hang
[L903] [32:53.04] out with my neighbors as we moved to a
[L904] [32:54.56] new place and I kept getting paged and
[L905] [32:56.36] kept going back home across the street
[L906] [32:58.32] to like go and figure out like what what
[L907] [33:00.60] didn't work. And I was like, "I am going
[L908] [33:02.48] to do everything I can to make Instagram
[L909] [33:04.84] as reliable as possible. And I know it's
[L910] [33:07.20] possible because Facebook solved a lot
[L911] [33:09.60] of those problems before and when I see
[L912] [33:11.28] people work on the code at Instagram,
[L913] [33:13.20] they don't use all of those tools
[L914] [33:16.04] that's uh
[L915] [33:17.64] that they use on the on the Facebook
[L916] [33:19.32] side. And I know because I worked
[L917] [33:20.48] there."
[L918] [33:21.28] And so, I went and I pitched it.
[L919] [33:24.44] I went to
[L920] [33:26.36] uh my manager's manager.
[L921] [33:28.12] I said, "Look,
[L922] [33:29.48] we have all those incidents.
[L923] [33:31.40] Uh there's all those tools that at
[L924] [33:33.76] Facebook
[L925] [33:35.00] they've been using for years and solve
[L926] [33:36.76] all of those patterns of incidents. We
[L927] [33:38.48] are not using any of those things. It is
[L928] [33:40.88] time that we partner with them
[L929] [33:44.60] and we unbottle of those tools so that
[L930] [33:46.52] we can dramatically improve the
[L931] [33:47.80] reliability of Instagram."
[L932] [33:49.88] And then that's why I became
[L933] [33:51.84] uh involved in that project.
[L934] [33:54.24] How'd you find out who on the Facebook
[L935] [33:56.44] side to talk to to get the buy-in for
[L936] [33:59.72] such a large uh adoption of their tools?
[L937] [34:03.40] So, basically they they paired me with
[L938] [34:05.80] an IC who was working on the Facebook
[L939] [34:07.48] side. Her name is Arianne.
[L940] [34:09.96] And she was exceptional at getting this
[L941] [34:13.96] buy-in on the Facebook side, bringing
[L942] [34:16.16] the right people to the conversation.
[L943] [34:18.96] And uh it's she's one of the most
[L944] [34:21.72] remarkable tech lead I've seen and
[L945] [34:23.32] worked with in my career.
[L946] [34:24.96] Uh she basically did that.
[L947] [34:26.80] I remember something interesting you
[L948] [34:28.32] told me before is you wanted to be
[L949] [34:32.44] mentored by her and you
[L950] [34:36.32] made an explicit pitch to her actually.
[L951] [34:38.36] I remember you were very you had a lot
[L952] [34:39.96] of agency in actually going to her and
[L953] [34:42.16] and setting it up. And I'm curious if
[L954] [34:44.36] you could tell that story and you know,
[L955] [34:46.92] what you might recommend for others who
[L956] [34:48.48] want to set up mentorships. So, there's
[L957] [34:51.20] several people that I met in my career
[L958] [34:53.12] and then when I met them, I'm like
[L959] [34:55.76] this person's able to be thoughtful, to
[L960] [34:58.84] challenge me
[L961] [35:00.56] and also seems to be
[L962] [35:03.32] uh
[L963] [35:04.12] very
[L964] [35:06.00] it they would just work well with me.
[L965] [35:08.04] They would be able to like make me
[L966] [35:09.52] change my mind on topic and I would
[L967] [35:11.68] relate to them. And so, they don't have
[L968] [35:13.64] to be engineers. This person I met like
[L969] [35:15.28] even outside of like software
[L970] [35:16.88] engineering. Like my current coach for
[L971] [35:18.64] example,
[L972] [35:19.76] uh she has all of those qualities. And
[L973] [35:22.00] so, when I met Arianne, I noticed that
[L974] [35:23.92] like yeah, she had all of those
[L975] [35:25.44] qualities. I'm like, "I really want to
[L976] [35:26.84] work with this person because
[L977] [35:28.84] she was very direct, very helpful,
[L978] [35:31.16] thoughtful,
[L979] [35:32.80] really excellent at like analyzing
[L980] [35:35.08] problem and trying to explain like in
[L981] [35:37.44] what ways I was thinking about the
[L982] [35:39.56] problem the wrong way and like trying to
[L983] [35:41.40] get me to change my mind." She got me to
[L984] [35:43.24] change my mind about a lot of things.
[L985] [35:45.24] And so
[L986] [35:46.48] so so does my coach. I think that's like
[L987] [35:48.32] that's that's
[L988] [35:49.48] a measure for success is like are you
[L989] [35:51.08] able to do you change your mind as a
[L990] [35:52.72] result of coaching or you just do the
[L991] [35:54.12] same thing you are doing before?
[L992] [35:56.16] When you went to Stripe, I'm kind of
[L993] [35:57.64] curious what were your first impressions
[L994] [36:00.12] as an engineer there?
[L995] [36:02.08] Everyone was I think that is like at
[L996] [36:04.36] every job I had the impression like I I
[L997] [36:06.72] often
[L998] [36:07.92] have the impression that I work with
[L999] [36:09.40] very bright people because that's the
[L1000] [36:10.92] case like at at like every job in this
[L1001] [36:12.80] in the Silicon Valley. Uh at Stripe
[L1002] [36:15.28] specifically,
[L1003] [36:16.84] um I like that everyone was very much
[L1004] [36:20.24] focused on making decisions based on
[L1005] [36:24.60] data. And there was like a big culture
[L1006] [36:26.64] around data, collecting data, analyzing
[L1007] [36:29.64] data, and making decision really
[L1008] [36:32.68] uh
[L1009] [36:33.32] using rigor
[L1010] [36:35.28] and science
[L1011] [36:36.96] rather than like
[L1012] [36:39.04] uh
[L1013] [36:40.12] you know, hunches and intuition.
[L1014] [36:42.52] Facebook also has that culture
[L1015] [36:44.60] uh of of like the experimentation. Uh
[L1016] [36:47.36] but Stripe has it to an even bigger
[L1017] [36:50.32] extent in my opinion.
[L1018] [36:52.76] And there is such a strong culture
[L1019] [36:55.88] around metrics. And I love that because
[L1020] [36:57.84] like I love metrics. I love like being
[L1021] [37:00.00] able to measure success and how uh
[L1022] [37:03.32] progress is made. So, I felt right at
[L1023] [37:06.08] home when I joined Stripe for that
[L1024] [37:07.40] reason.
[L1025] [37:08.32] You mentioned you were the TL of this um
[L1026] [37:10.92] dev infra team and eventually the scope
[L1027] [37:13.44] grew. It grew from 35 people to 140
[L1028] [37:17.28] people in this organization. And I kind
[L1029] [37:20.28] of want to learn more about the story as
[L1030] [37:22.08] it grew. So, I joined as like the tech
[L1031] [37:24.44] lead of build test and tooling. So, that
[L1032] [37:26.12] was a group of team
[L1033] [37:27.80] um that were doing
[L1034] [37:31.60] the build so let's say the build system,
[L1035] [37:34.12] Basil, the remote building, the code
[L1036] [37:37.24] management internal
[L1037] [37:39.80] and GitHub,
[L1038] [37:41.44] uh code review,
[L1039] [37:43.36] testing infrastructure,
[L1040] [37:45.60] testing data. So, that was that the the
[L1041] [37:48.60] group of team. And that that was great
[L1042] [37:50.52] for me because that's like the areas of
[L1043] [37:51.96] dev fraud I was like the most familiar
[L1044] [37:54.20] with. And so, initially I was like, "I
[L1045] [37:56.16] need to gain credibility."
[L1046] [37:58.52] Why? Because there's like those 35
[L1047] [37:59.96] engineers have been working here like
[L1048] [38:01.36] most of them a long time and I'm coming
[L1049] [38:03.48] as an outsider. I want to be able to
[L1050] [38:06.12] lead them and I want to be able to do a
[L1051] [38:07.96] good job.
[L1052] [38:10.20] So, I looked back at
[L1053] [38:12.80] when
[L1054] [38:14.08] I was in that situation. When I was in
[L1055] [38:15.68] one of those team and a new tech lead
[L1056] [38:17.12] joined in and think about like what is
[L1057] [38:18.72] it that they've done right and wrong.
[L1058] [38:21.32] And the thing that I came up with was
[L1059] [38:24.64] I think
[L1060] [38:26.00] you're doing it wrong if you use your
[L1061] [38:29.12] past experience all the time to justify
[L1062] [38:31.20] what to do. You're like, "Oh, it worked
[L1063] [38:32.68] at Facebook so it must work here."
[L1064] [38:35.16] Because it like uh belittled the people
[L1065] [38:37.52] and like their their experience.
[L1066] [38:41.04] You need to also not tell people what to
[L1067] [38:42.80] do because that's not how you build
[L1068] [38:46.60] uh
[L1069] [38:47.28] trust in the team. Like say imagine
[L1070] [38:49.20] you're Arianne and be like, "Oh, I've
[L1071] [38:50.24] never seen this thing work at any
[L1072] [38:51.88] company I worked at. So, we're going to
[L1073] [38:53.16] cancel this project."
[L1074] [38:54.84] That that doesn't work. So, I was like,
[L1075] [38:56.84] "I have a rule.
[L1076] [38:58.12] My rule is
[L1077] [39:00.12] I will not
[L1078] [39:02.52] tell people what to do. I will not
[L1079] [39:05.92] uh
[L1080] [39:06.68] reject a design outright.
[L1081] [39:09.12] I will never do that in my whole time.
[L1082] [39:11.36] And at Stripe, I never did that. So,
[L1083] [39:13.20] there's a couple time when I told people
[L1084] [39:15.00] what to do which was in situation of
[L1085] [39:16.56] like urgency when you're like solving an
[L1086] [39:18.44] incident and you're like, 'Yeah, you
[L1087] [39:19.60] have to do this. You have to do that.'
[L1088] [39:21.36] But otherwise, I managed to do all of my
[L1089] [39:23.84] work and all the influence and all the
[L1090] [39:25.64] change of direction
[L1091] [39:27.80] by asking questions.
[L1092] [39:29.96] Simply asking questions
[L1093] [39:32.28] and getting people to change their mind
[L1094] [39:34.44] themselves as opposed to just telling
[L1095] [39:36.68] them like, 'Hey, we have to do this or
[L1096] [39:37.92] we have to do that.'
[L1097] [39:39.16] So, that was my style coming in. That's
[L1098] [39:41.20] what I wanted to do. And I'm like, in
[L1099] [39:42.96] order to build credibility, I need to
[L1100] [39:45.04] need the engineers to know me, to know
[L1101] [39:46.60] my style. So, I'm going to embed in the
[L1102] [39:48.64] different teams. So, I embedded in the
[L1103] [39:50.48] teams.
[L1104] [39:52.88] And started to work with the people on
[L1105] [39:55.24] like uh say I would embed in a team to
[L1106] [39:58.44] go work on a specific project for like a
[L1107] [40:00.24] month. Just to see what the rhythm is
[L1108] [40:02.64] like, how people work together. And so,
[L1109] [40:04.96] after a year, I'd met everyone
[L1110] [40:07.52] in person multiple times. I had like
[L1111] [40:10.04] embedded in like pretty much
[L1112] [40:12.24] all the different parts of the the
[L1113] [40:14.08] group. And I felt like I had a good
[L1114] [40:15.80] grasp.
[L1115] [40:17.32] And then I was like,
[L1116] [40:20.44] "But I know less than every individual
[L1117] [40:23.44] person about their domain."
[L1118] [40:25.48] And that's what leadership is. Like,
[L1119] [40:26.96] unfortunately, like when you are like
[L1120] [40:29.80] say in charge of like a large group, you
[L1121] [40:32.08] by nature know less than every person
[L1122] [40:34.84] about their own domain. And you have to
[L1123] [40:37.76] accept that. And it's very very
[L1124] [40:39.12] different than what happens say when
[L1125] [40:40.32] you're the tech lead of a team, where
[L1126] [40:42.04] you're the person who knows the most.
[L1127] [40:44.04] So, there's that that transition.
[L1128] [40:46.40] And I was able to navigate that
[L1129] [40:47.60] transition by just changing my mindset
[L1130] [40:49.68] and thinking,
[L1131] [40:51.52] "People are experts. I'm supposed to
[L1132] [40:53.88] guide. I'm supposed to ask questions.
[L1133] [40:56.84] And that's how we're going to get there.
[L1134] [40:58.92] And
[L1135] [41:00.20] it's going to work because I know I
[L1136] [41:03.64] I have a good hunch for like how to
[L1137] [41:05.72] solve developer productivity problem. I
[L1138] [41:07.44] worked on that
[L1139] [41:08.88] many many years.
[L1140] [41:10.72] And
[L1141] [41:12.52] just naturally, I always think about
[L1142] [41:14.16] like how to do things better. So, I will
[L1143] [41:16.44] just ask good question, and that's going
[L1144] [41:18.04] to work out." And it did.
[L1145] [41:20.36] Um
[L1146] [41:21.64] after that, the model shifted a little
[L1147] [41:23.92] bit.
[L1148] [41:24.84] Um when the org was like about
[L1149] [41:28.16] 40 50 people,
[L1150] [41:30.24] uh I shifted to a mode of operation
[L1151] [41:32.28] where I would be deployed to go work on
[L1152] [41:34.60] something for like
[L1153] [41:36.92] say
[L1154] [41:38.28] two to eight weeks.
[L1155] [41:40.12] And then go that would not necessarily
[L1156] [41:43.04] be with a team. It could be with like a
[L1157] [41:44.76] group of team, could be with like one or
[L1158] [41:47.04] two individual, it could be with like
