Chunk 4; segments 951–1275. Start may repeat the previous chunk for context.

# Instagram Principal Engineer (IC8): Promotions, Breaking Prod, Tech Leading | Jake Bolam

Source ID: source-e4725309875844e7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Instagram_Principal_Engineer_(IC8)_Promotions,_Breaking_Prod,_Tech_Leading_Jake_Bolam_en.txt
Video: https://www.youtube.com/watch?v=QUhC5BDZt-E

[L960] [33:13.44] your diff is going to blow up
[L961] [33:14.72] production,
[L962] [33:16.40] I will I will comment on it and be like,
[L963] [33:18.08] "This is going to blow up production."
[L964] [33:20.16] And then accept it and be like, "Yeah,
[L965] [33:21.68] make sure you fix that first." Right.
[L966] [33:23.68] And I've never had a case where
[L967] [33:25.28] someone's like landed it with a comment
[L968] [33:28.00] on it that says, "Hey, this is going to
[L969] [33:29.20] blow up production." Cuz you can imagine
[L970] [33:31.04] like sitting in review or something and
[L971] [33:32.88] someone's like, "The diff had a comment
[L972] [33:34.80] on it. This is going to blow up
[L973] [33:36.00] production." And it blow up. That's wild
[L974] [33:38.72] that. Yeah. Except I just trust them to
[L975] [33:40.88] fix it, right? Like Yeah. Yeah. Yeah.
[L976] [33:42.56] Fix it the right way. Once again, if
[L977] [33:44.40] they have trust, if it's like a new
[L978] [33:45.92] person on the team and I'm not sure if
[L979] [33:47.36] they're going to fix it the right way,
[L980] [33:49.36] right? I might be like, "Ping me again
[L981] [33:50.96] when it's like ready." Yeah. Yeah. But
[L982] [33:52.88] yeah, 99% of the time I'll just like
[L983] [33:54.56] accept and go. And yeah, haven't had to
[L984] [33:57.36] do the thing where I pull back because
[L985] [33:58.72] I've never had one that's been shipped
[L986] [34:00.80] accidentally exploded.
[L987] [34:03.60] And that's actually a little bit of a
[L988] [34:04.80] philosophy I use across like I guess
[L989] [34:07.12] building these systems, judging how fast
[L990] [34:09.04] I'm moving. Yeah. If I'm doing something
[L991] [34:11.36] and it's not I'm not getting feedback
[L992] [34:13.52] that it's like broken or I'm not seeing
[L993] [34:15.36] negative effects from it, right? Even if
[L994] [34:17.12] it is controversial and crazy, I'll keep
[L995] [34:19.36] pushing the boundary on it, right? U
[L996] [34:21.76] same as our rollouts like if we're at 1%
[L997] [34:23.84] we're getting like very little feedback
[L998] [34:25.36] and like metrics are looking good and we
[L999] [34:28.32] might move to like 10% the next day and
[L1000] [34:30.24] people like that's crazy like step to
[L1001] [34:31.60] like two three five things it's like
[L1002] [34:33.60] well not we're not getting any like
[L1003] [34:35.60] signals that it's not going poorly as
[L1004] [34:37.76] soon as we get signals that it's going
[L1005] [34:39.12] poorly we start pulling back but
[L1006] [34:41.44] otherwise I find you like move too
[L1007] [34:43.20] slowly right you want to be moving at
[L1008] [34:45.44] like the fastest speed you can without
[L1009] [34:47.84] ruining things right so if you're not
[L1010] [34:50.16] getting if you're not making anything
[L1011] [34:52.00] worse like keep trying to find that
[L1012] [34:53.60] edge. Yeah. Yeah. Yeah. I I had a tech
[L1013] [34:56.80] lead early in my career and I had taken
[L1014] [34:59.44] down prod or something and I was talking
[L1015] [35:02.24] to him about it and he you know at one
[L1016] [35:05.44] on one end you shouldn't break prod
[L1017] [35:07.48] generally but he also said if you never
[L1018] [35:10.56] break
[L1019] [35:11.88] prod that's probably not also optimal
[L1020] [35:15.12] like there there should be some level of
[L1021] [35:18.88] risk otherwise you're moving too slowly
[L1022] [35:20.88] and so yeah exactly yeah try not to
[L1023] [35:22.88] break prod But if you never break it,
[L1024] [35:26.16] you're probably like very slow and Yeah.
[L1025] [35:28.48] And if you're breaking it every day,
[L1026] [35:30.00] you're probably going way too fast.
[L1027] [35:32.00] Yeah. Exactly. Exactly. Need to fix
[L1028] [35:33.92] something. Do you use um AI at all? Yes.
[L1029] [35:36.56] So, I've been I use it. I use chat GPT
[L1030] [35:39.04] like I don't know 10 times a day outside
[L1031] [35:41.76] of work and then internally we have like
[L1032] [35:43.36] own things that I use too. But I think
[L1033] [35:45.12] it's great, right? Like just like
[L1034] [35:46.48] harness the tools that are coming. They
[L1035] [35:49.04] have a bunch of caveats and they make
[L1036] [35:50.72] mistakes and stuff, but like I don't
[L1037] [35:52.64] know. I had to use if someone said,
[L1038] [35:54.96] "Don't use a calculator," I'd be like,
[L1039] [35:56.32] "What the fuck?" Use the to use the
[L1040] [35:58.08] tool. The tool's there. Figure out a way
[L1041] [36:00.00] to use it, right? Yeah. Then maybe we
[L1042] [36:01.76] won't get replaced if we become masters
[L1043] [36:03.44] of the tools. Yeah. Yeah. Yeah. Exactly.
[L1044] [36:05.76] Exactly. Yeah. I wanted to talk about
[L1045] [36:08.56] being a tech lead a bit because I feel
[L1046] [36:10.16] like that's one superpower that you have
[L1047] [36:12.72] to start. What would you say is the role
[L1048] [36:14.16] of a tech lead? Like what are the
[L1049] [36:15.44] important things to do and how do you
[L1050] [36:17.44] see that role? Yeah. So yeah, people
[L1051] [36:21.12] probably have a different opinion on
[L1052] [36:22.24] this all over the place, but yeah, mine
[L1053] [36:23.68] is just like, okay, you're the tech
[L1054] [36:25.20] lead. You're responsible for this
[L1055] [36:26.72] project now, right? Like do whatever it
[L1056] [36:28.48] takes to get this project done. Usually
[L1057] [36:31.20] the highest leverage thing you can be
[L1058] [36:32.64] doing is like making sure everyone else
[L1059] [36:34.16] is like contributing to the project and
[L1060] [36:36.32] moving in the right direction, right?
[L1061] [36:38.56] But sometimes you might have to switch
[L1062] [36:39.84] and do other things like writing code or
[L1063] [36:42.32] jump into fixer mode. There's been a few
[L1064] [36:43.84] times where I've had to like no one else
[L1065] [36:45.68] can debug what this thing's doing. So, I
[L1066] [36:47.52] spent two weeks chasing like the
[L1067] [36:48.96] craziest bug through the system to like
[L1068] [36:50.88] find that line of code that's messing
[L1069] [36:52.80] up. At this point, you've probably
[L1070] [36:54.80] coached tech leads because you're in a
[L1071] [36:57.52] position with leverage. Yeah. What's the
[L1072] [36:59.76] most common mistake you see people make
[L1073] [37:01.92] if they're transitioning into more of a
[L1074] [37:03.76] leadership role? I think getting like
[L1075] [37:06.24] kind of disconnected from what the what
[L1076] [37:08.96] the goal is of the project, right? So
[L1077] [37:10.72] easy to get caught up in the day-to-day
[L1078] [37:12.32] operations of like we need to be doing
[L1079] [37:14.00] this and we need to be doing Y and like
[L1080] [37:16.08] lose track of the fact that like the
[L1081] [37:18.80] direction we're heading in might have
[L1082] [37:19.92] actually shifted a little bit and it's
[L1083] [37:21.20] like your responsibility like shift the
[L1084] [37:23.12] team towards towards the goal again.
[L1085] [37:25.68] Right. Right. I know at Meta regardless
[L1086] [37:28.56] of how high level you are you're
[L1087] [37:30.24] expected to make technical
[L1088] [37:32.24] contributions. Yeah. But generally there
[L1089] [37:34.64] is a sentiment of as you become a higher
[L1090] [37:37.12] and higher tech lead you get further and
[L1091] [37:39.20] further from the code. Yeah. And more in
[L1092] [37:41.44] doc work and leadership meetings and
[L1093] [37:43.60] things. How do you strike that balance?
[L1094] [37:46.96] Yeah. So it's definitely is uh a hard
[L1095] [37:49.76] balance to strike but I'll still I'll
[L1096] [37:52.00] still write code probably nearly nearly
[L1097] [37:54.88] every week even if it's like a smaller
[L1098] [37:57.28] amount of code because then I'm using
[L1099] [37:58.64] the full tool chain. Often it's because
[L1100] [38:01.28] no one else wants to do it or it's
[L1101] [38:03.36] something that, you know, maybe I'm
[L1102] [38:05.52] going to do it 10 times faster cuz I
[L1103] [38:07.20] know know that thing and I don't want
[L1104] [38:09.60] them to waste a week on it. So I'll go
[L1105] [38:11.28] and do it, right? Yeah. So I just I'll
[L1106] [38:13.36] just like find the time and those focus
[L1107] [38:14.88] blocks and stuff help with that too.
[L1108] [38:16.48] Right. And it might if it gets to
[L1109] [38:17.76] Wednesday and I haven't written code and
[L1110] [38:19.20] nothing's come up, I might go and do
[L1111] [38:21.36] that. Yeah. This is all caveed on the
[L1112] [38:23.52] fact that I'm always trying to work on
[L1113] [38:25.20] what I think is the most important
[L1114] [38:26.48] thing, right? Mhm. Like if it was saving
[L1115] [38:28.16] that person, you know, their whole week
[L1116] [38:30.72] of doing it, it's going to take me an
[L1117] [38:31.84] hour. I'll go and do Yeah. But there
[L1118] [38:33.60] might be periods of time where we're
[L1119] [38:34.80] doing a big review or, you know, we're
[L1120] [38:36.88] going to get a headcount injection or
[L1121] [38:39.76] I don't know, we need to be doing X, Y,
[L1122] [38:41.12] or Z and then that's way higher leverage
[L1123] [38:43.44] for me to be spending my time on and I
[L1124] [38:44.96] won't code for a few weeks. Right.
[L1125] [38:46.64] Right. How do you I think this is more,
[L1126] [38:49.52] you know, junior people lack this, but
[L1127] [38:51.44] how do you develop that skill of seeing
[L1128] [38:53.84] what is impactful with your time? I
[L1129] [38:55.76] mean, where's the ROI? Where'd you learn
[L1130] [38:58.08] that? Yeah, I think it's uh I don't
[L1131] [39:00.80] know, just like practice. Practice makes
[L1132] [39:03.60] perfect. And you've seen a lot of
[L1133] [39:04.80] scenarios, so you kind of know, right,
[L1134] [39:06.88] which one after a while. Yeah. But yeah,
[L1135] [39:08.88] when I didn't have that gauge, and I
[L1136] [39:10.64] still use this a little bit now, it's
[L1137] [39:12.08] always like, what do I what do I think
[L1138] [39:14.72] myself is really important that no one
[L1139] [39:16.64] else is willing to work on? Yeah. Um and
[L1140] [39:18.96] that's usually the area I would go to.
[L1141] [39:21.24] Before I had developed like a good sense
[L1142] [39:23.60] of it because now there'll be sometimes
[L1143] [39:24.88] where I'm like oh no one's working on it
[L1144] [39:27.68] because it's stupid but like if I really
[L1145] [39:30.32] think it's really important I will like
[L1146] [39:32.72] find a way to work on it. Yeah. Oh
[L1147] [39:34.40] interesting. Um there's a famous essay
[L1148] [39:37.92] inside a workplace somewhere and the
[L1149] [39:40.32] title of it is like go where you're rare
[L1150] [39:42.96] or something like that. Oh and this kind
[L1151] [39:45.04] of reminds me of that. It's a scarce
[L1152] [39:47.84] thing that you could solve that problem.
[L1153] [39:49.92] And yeah, you know, it makes sense, man.
[L1154] [39:51.92] I haven't seen that essay. I love that.
[L1155] [39:53.68] Yeah. Yeah. There's a lot of gold in
[L1156] [39:55.76] workplace actually. A lot of people
[L1157] [39:57.76] sleep on on the like the alltime essays
[L1158] [40:00.72] in in workplace. Yeah. They're buried
[L1159] [40:03.28] somewhere in there. There's another one
[L1160] [40:05.28] from one of our like I don't know ICT
[L1161] [40:07.44] 10s that we have at the company who
[L1162] [40:08.88] talks about the
[L1163] [40:11.04] 20% of the time he just works on stuff
[L1164] [40:13.04] that like he's never going to get
[L1165] [40:15.04] credited for, right? Right. It's like
[L1166] [40:16.64] the kind of org contributions or if you
[L1167] [40:18.96] get very senior, it might be the code
[L1168] [40:20.48] contributions cuz like they don't really
[L1169] [40:21.84] care if I code Yeah. or not anymore,
[L1170] [40:24.40] right? What's the rationale that if
[L1171] [40:26.72] you're always if you spend 100% of your
[L1172] [40:28.56] time working on stuff that you get
[L1173] [40:30.32] credited for, you're probably dropping a
[L1174] [40:32.88] lot of stuff, right? And I see I see it
[L1175] [40:34.32] happen like someone might come and be
[L1176] [40:36.16] like, "Hey, can you like help me with
[L1177] [40:37.44] this thing or something like that?" And
[L1178] [40:40.16] I'll be like, "Well, I I'm know I'm
[L1179] [40:41.68] never going to get credit for this, so I
[L1180] [40:42.88] just say no to But there was actually a
[L1181] [40:44.24] lot of value in helping that person. I'm
[L1182] [40:47.36] just like when performance comes around,
[L1183] [40:49.20] no one's going to be like, "Oh, he
[L1184] [40:50.32] helped this person. Cool." So, I
[L1185] [40:52.32] actually like that kind of mindset and
[L1186] [40:54.08] it was kind of how I was operating
[L1187] [40:55.36] before I read this, too. But like, yeah.
[L1188] [40:57.36] 20 or 30% of my time. Yeah. I'll just do
[L1189] [41:00.08] things that I know I'm not going to get
[L1190] [41:01.28] credited for. Yeah. Yeah. PSC is all
[L1191] [41:03.36] about doing things that are measurable.
[L1192] [41:05.76] And there can be a hundred little things
[L1193] [41:08.80] that you help people with that made them
[L1194] [41:11.76] 5% better or something and that's not
[L1195] [41:14.88] going to be in your PSC because your PSC
[L1196] [41:16.48] is probably just giant migration item,
[L1197] [41:18.88] giant, you know, this, giant that. Not
[L1198] [41:21.04] all those little things. Not all the
[L1199] [41:22.56] little things. And like those 20 or 30%
[L1200] [41:24.48] you want them to from your point of
[L1201] [41:26.40] view, you think they're valuable, right?
[L1202] [41:27.92] But just no one else is going to think
[L1203] [41:29.04] they're valuable. Like I think helping
[L1204] [41:30.80] that person is valuable. I think doing
[L1205] [41:32.24] things for the org, the wider or is
[L1206] [41:34.72] valable. I think having some coding time
[L1207] [41:36.40] is valuable, right? But yeah, a lot of
[L1208] [41:38.48] people like probably not. Yeah. Yeah. I
[L1209] [41:41.28] think also early in my career, I I
[L1210] [41:43.92] worked so much extra hours just doing
[L1211] [41:46.56] whatever people gave me that I do think
[L1212] [41:49.52] it actually became valuable at a later
[L1213] [41:51.76] time. Like, you know, I was kn credible
[L1214] [41:54.00] and known as someone who's just going to
[L1215] [41:55.68] like unblock you no matter what. Like,
[L1216] [41:58.24] I'll be responding late or whatever just
[L1217] [42:00.48] cuz I was into it. Yeah. So there's a
[L1218] [42:03.20] hidden things outside of PSC that Yeah.
[L1219] [42:05.68] And then that becomes valuable, right?
[L1220] [42:07.20] Yeah. And then that becomes value. Yeah.
[L1221] [42:08.96] Like a lot of people appreciate the fact
[L1222] [42:10.48] that I'm a senior engineer who still
[L1223] [42:12.24] codes. I think we talked about the work
[L1224] [42:14.20] diary thing. I wrote something about how
[L1225] [42:17.12] it's important to have some
[L1226] [42:19.36] documentation of the things you're
[L1227] [42:20.88] landing or the state of investigations
[L1228] [42:23.68] etc. and the value of writing. What's
[L1229] [42:25.76] your process for keeping track of your
[L1230] [42:28.24] work in writing? Oh yeah. So basically I
[L1231] [42:32.24] have a really good note takingaking
[L1232] [42:34.00] system because I'm terrible at
[L1233] [42:35.92] remembering things. So and my
[L1234] [42:37.92] note-taking system is actually in VS
[L1235] [42:39.44] Code. Oh really? Yeah. So I just have
[L1236] [42:41.28] another VS Code instance spun up so I
[L1237] [42:44.24] can have two running or whatever. Is it
[L1238] [42:45.84] just a text? It's just a text. Yeah. And
[L1239] [42:48.72] uh so I'll have it and I don't I don't
[L1240] [42:50.72] actually use multiple monitors. So I
[L1241] [42:52.72] just have like the workspace thing or
[L1242] [42:54.64] whatever on Mac where I can just use a
[L1243] [42:56.08] couple of fingers and it just flicks
[L1244] [42:57.20] across. Oh, like that. Okay. So it's
[L1245] [42:58.72] always very easily accessible and I'll
[L1246] [43:01.36] just dive across and I'll have I'll
[L1247] [43:03.04] create a new readme file in one folder.
[L1248] [43:06.48] I don't have the whole I don't have a
[L1249] [43:07.92] folder archive. It's just one folder and
[L1250] [43:10.96] I'll have like Yeah. like current
[L1251] [43:13.12] project name or something just saved in
[L1252] [43:14.96] there. Yeah. And that way I can like
[L1253] [43:16.80] search for a file name in like two or
[L1254] [43:19.52] three characters and jump between file
[L1255] [43:21.28] names. So I have now on there there's
[L1256] [43:23.28] probably like tens of thousands of files
[L1257] [43:25.20] cuz I have notes for everything on
[L1258] [43:26.80] there. Yeah. But I this is my like index
[L1259] [43:29.60] way of like sort of jumping between lots
[L1260] [43:32.64] of thoughts. Yeah. And writing them
[L1261] [43:34.24] down. And then I have like keyboard
[L1262] [43:35.20] shortcuts for inserting like the current
[L1263] [43:37.52] date and time. Yeah. Right. So I can
[L1264] [43:39.84] like kind of index it on that. Oh wow.
[L1265] [43:42.48] It's like an extension of your brain.
[L1266] [43:44.24] Just like you're just constantly noting
[L1267] [43:46.88] things down at all. Constantly noting it
[L1268] [43:48.56] down and I don't have to spend any time
[L1269] [43:49.92] organizing it, right? Cuz there is no
[L1270] [43:51.44] folder structure. Just one giant thing.
[L1271] [43:53.92] The only thing that it's organized by is
[L1272] [43:55.68] like searching for a file name. Or you
[L1273] [43:57.28] can use word search, right, if you need
[L1274] [43:59.92] to. F. Yeah. Crl+ F. But most of the
[L1275] [44:02.48] time I'm like have a pretty good idea of
[L1276] [44:04.16] what thing I saved it under. Right.
[L1277] [44:06.00] Yeah. So every oneonone there's like a a
[L1278] [44:08.24] name of a person, right? Like Right.
[L1279] [44:10.00] Right. Right. Every project there's one
[L1280] [44:11.84] I have like a couple of root level ones
[L1281] [44:13.84] like
[L1282] [44:14.68] priorities. For work there's priorities.
[L1283] [44:16.64] So then in there I'll have use the time
[L1284] [44:18.72] stamp each day. These are the priority
