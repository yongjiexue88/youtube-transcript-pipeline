Chunk 4; segments 942–1258. Start may repeat the previous chunk for context.

# OpenAI Codex Tech Lead: How His Career Grew And How He Uses Codex | Michael Bolin

Source ID: source-d89129dbba19118b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/OpenAI_Codex_Tech_Lead_How_His_Career_Grew_And_How_He_Uses_Codex_Michael_Bolin_en.txt
Video: https://www.youtube.com/watch?v=hN5ZFzWFhhg

[L951] [33:30.16] So that you would be in your editor, you
[L952] [33:31.68] know, typing. And so that was way faster
[L953] [33:34.16] than uh I think than you know, like what
[L954] [33:36.48] Xcode or or like VSS code or something
[L955] [33:38.48] like would give you um out of the box.
[L956] [33:41.76] And uh so so that was you know, so like
[L957] [33:44.08] it was solving a problem for Eden that
[L958] [33:47.12] was the name of the file system
[L959] [33:48.00] originally, the virtual file system. um
[L960] [33:51.12] you know in anticipation before it was
[L961] [33:53.12] even ready um but then it was so fast um
[L962] [33:56.48] and it was available as a trip service
[L963] [33:58.08] internally like people started using it
[L964] [33:59.84] for all sorts of other things I think
[L965] [34:01.28] when I left like I don't know I think
[L966] [34:03.36] there were these like 30 servers running
[L967] [34:04.88] mile like spread around the globe
[L968] [34:06.90] [laughter] so clearly that was more than
[L969] [34:08.88] just people like personally searching
[L970] [34:10.64] for files and then you did that much you
[L971] [34:12.32] know capacity
[L972] [34:13.36] >> interesting yeah I mean when you talked
[L973] [34:14.72] about I guess the implementation details
[L974] [34:18.56] most most people They they don't use
[L975] [34:20.88] leak code on the job. But that sounds
[L976] [34:23.76] like I was thinking about the I don't I
[L977] [34:26.56] don't even know how you put that. Is it
[L978] [34:27.84] like a tree like a try thing?
[L979] [34:29.92] >> No. So that's what's funny that Yeah. Um
[L980] [34:33.04] this was this was pretty cool in that um
[L981] [34:35.92] we we had kind of like two parallel
[L982] [34:39.28] arrays. One was like the file contents
[L983] [34:42.56] and one was uh maybe an integer into
[L984] [34:45.28] that um index. I forget. And then we had
[L985] [34:48.96] a we had a 64-bit um
[L986] [34:53.60] uh mask that was like it was like so you
[L987] [34:56.00] had like 26 lowercase 26 capital 10
[L988] [35:00.08] digits and like maybe dash and whatever.
[L989] [35:02.32] And uh and it would and it was uh every
[L990] [35:04.72] bit was set if the um if that character
[L991] [35:08.80] was used at all in the file that you
[L992] [35:10.80] were searching. And so the first thing
[L993] [35:11.92] was we could like blow through that list
[L994] [35:15.60] and um you know exclude a bunch of
[L995] [35:17.84] things like right off the top. But we
[L996] [35:20.32] was also like very designed like all
[L997] [35:21.92] these arrays were in parallel to each
[L998] [35:23.76] other so that
[L999] [35:25.12] >> for like cache wise we knew it' be very
[L1000] [35:27.12] efficient for for the CPU to to like
[L1001] [35:30.08] read memory you know linearly and then
[L1002] [35:32.48] it lend itself to you could just
[L1003] [35:33.92] partition that array it, you know, lend
[L1004] [35:35.92] itself to parallelism. Um, so it was
[L1005] [35:38.96] really Yeah, I should really probably
[L1006] [35:40.48] write it up at some point because I that
[L1007] [35:42.48] is really cool. It was It was f because
[L1008] [35:44.56] it wasn't just kind of like out of the
[L1009] [35:46.16] textbook. That's that's for sure.
[L1010] [35:48.00] >> I understand that. Um, yeah, you worked
[L1011] [35:50.40] on Eden and then obviously there's Miles
[L1012] [35:52.72] as well.
[L1013] [35:53.92] >> Um, and then these eventually led to
[L1014] [35:55.92] another promotion and um, but prior to
[L1015] [35:58.72] that promotion, there was some learnings
[L1016] [36:00.88] you might have had about influence and
[L1017] [36:02.88] conflict in org. So maybe if you want to
[L1018] [36:05.04] share that. Yeah, I mean that's
[L1019] [36:09.04] one of the things I guess about being an
[L1020] [36:11.12] E8 um who primarily writes code, right?
[L1021] [36:15.44] Um there's other people I'd say actually
[L1022] [36:18.08] the majority of people that level or
[L1023] [36:19.52] higher are not writing code, right?
[L1024] [36:22.24] They're they're actually kind of
[L1025] [36:23.52] exclusively spent doing more like
[L1026] [36:25.92] influence or working across teams, you
[L1027] [36:28.08] know, writing the big Google doc and
[L1028] [36:30.08] getting everyone on board and all that
[L1029] [36:32.24] um sort of stuff. And so, you know,
[L1030] [36:37.04] as an E8 trying to have that level,
[L1031] [36:39.20] like, you know, that level of impact
[L1032] [36:40.72] that you're expected to have, it's like,
[L1033] [36:42.64] oh, it's hard to do that just writing
[L1034] [36:44.00] code. So, it's like I need to spend at
[L1035] [36:45.28] least some time probably probably
[L1036] [36:49.52] influencing other people. That would
[L1037] [36:50.88] probably be be good for me. That would
[L1038] [36:52.32] probably make my manager happy. Um, and
[L1039] [36:56.96] I think
[L1040] [36:59.12] uh
[L1041] [37:00.80] you know sometimes you're just so
[L1042] [37:03.76] uh confident in in some uh insights you
[L1043] [37:07.52] have that or certainly I was that I
[L1044] [37:10.40] would just I I just came down like way
[L1045] [37:12.32] too hard I would say and uh and that did
[L1046] [37:16.16] not go well for me and yeah and so like
[L1047] [37:18.88] like uh promo got delayed because I was
[L1048] [37:21.92] very excited are anxious about uh when
[L1049] [37:27.52] Microsoft acquired GitHub
[L1050] [37:31.36] and uh oh yeah because new Clyde was
[L1051] [37:33.36] built on this um you know primarily
[L1052] [37:34.96] GitHub technology and I was like that's
[L1053] [37:36.80] going to go away because VS Code's going
[L1054] [37:38.72] to not make them be a project anymore
[L1055] [37:40.96] which was true which did happen and I
[L1056] [37:44.48] was just so
[L1057] [37:46.64] uh anxious that that this was like now a
[L1058] [37:49.52] risk right and I was pushing people but
[L1059] [37:51.28] you know people were I didn't really
[L1060] [37:54.16] account for the fact uh that people were
[L1061] [37:56.88] happy with what they were doing at the
[L1062] [37:58.40] moment and like didn't want their cheese
[L1063] [38:00.40] moved, you know, like uh right out from
[L1064] [38:02.48] under them. And so um you know, I got
[L1065] [38:05.36] like a little bit of a talking to, you
[L1066] [38:06.80] know, I had to wait a little bit for
[L1067] [38:08.08] promo and things like that. But I you
[L1068] [38:10.08] know, I actually got some coaching I
[L1069] [38:12.88] think after that point. I can't remember
[L1070] [38:14.08] the exact chronology um to to work on
[L1071] [38:16.64] that like specifically. What's the
[L1072] [38:19.04] number one thing you learned about
[L1073] [38:20.32] coaching? I would say for me is like um
[L1074] [38:25.84] I think I'm more aware of like things
[L1075] [38:27.52] that trigger me like know be technical
[L1076] [38:30.48] decisions or what have you and recognize
[L1077] [38:33.20] when that's happening and be like okay
[L1078] [38:34.88] let's not act in that moment or you know
[L1079] [38:37.76] if I if I don't think I can have the
[L1080] [38:39.92] conversation like uh or I'm not the in
[L1081] [38:42.96] the best place to have it like maybe I
[L1082] [38:44.96] go talk to the person's manager instead
[L1083] [38:46.64] rather than like you know like bull and
[L1084] [38:48.40] china shop to the engineer and be
[L1085] [38:50.80] So, I have this thing. I'm thinking
[L1086] [38:52.08] about it this way. I'm kind of riled up
[L1087] [38:53.76] about it. Like, help me like how can I,
[L1088] [38:56.40] you know, work with your team or or
[L1089] [38:58.24] whatever like that's happened to you.
[L1090] [39:00.08] >> Well, it's interesting to me in your
[L1091] [39:02.32] career because the promo got postponed
[L1092] [39:05.92] and you were you were seeing that VS
[L1093] [39:08.48] Code was going to come up and the thing
[L1094] [39:10.32] that new cloud was built on was going to
[L1095] [39:12.56] go down and you were actually right in
[L1096] [39:16.64] hindsight too. like in the future that
[L1097] [39:19.12] is what happened and
[L1098] [39:21.44] >> you were battling for what was right yet
[L1099] [39:24.40] you were told calm down a little bit and
[L1100] [39:27.44] this so I mean what are your thoughts
[L1101] [39:29.44] when you saw things play out and you go
[L1102] [39:31.12] actually I was right the whole
[L1103] [39:32.72] >> um I did have some conversations like
[L1104] [39:35.20] about a year later and I was like hey
[L1105] [39:37.68] [laughter]
[L1106] [39:38.16] >> can we balance the ledger a little bit
[L1107] [39:39.92] like it didn't be pretty hard for that
[L1108] [39:41.84] thing and it was kind of good and we we
[L1109] [39:44.24] worked it out I would say
[L1110] [39:46.40] >> okay so I guess that the learning is
[L1111] [39:48.16] just
[L1112] [39:49.28] >> how you went about it, not what you were
[L1113] [39:51.52] like.
[L1114] [39:52.48] >> Yeah. Yeah. Um I would say that's true.
[L1115] [39:56.48] >> You seem to have a great time at Meta
[L1116] [39:58.96] and eventually you left. So what was the
[L1117] [40:01.60] thing that drew you to OpenAI?
[L1118] [40:04.00] >> Yeah, I mean um a number of things. I
[L1119] [40:06.72] mean one was uh so I I interviewed at
[L1120] [40:09.28] the end of 2023 with OpenAI I believe
[L1121] [40:12.40] and um and I had spent 2023 at Meta um
[L1122] [40:16.00] trying to do LM based developer tools
[L1123] [40:19.12] right with uh there's a you know we had
[L1124] [40:20.72] our own light version even met like
[L1125] [40:23.12] little version of uh GitHub copilot
[L1126] [40:25.28] right that one did like a paper and a
[L1127] [40:27.36] talk on that one was a code compose
[L1128] [40:29.44] right that was code compose yeah
[L1129] [40:31.20] >> and um you know we uh like now uh
[L1130] [40:36.00] there's a lot of uh uh enthusiasm around
[L1131] [40:40.00] you know delivering quickly and pushing
[L1132] [40:42.00] the boundaries of that sort of stuff and
[L1133] [40:44.48] uh you know I mean truthfully I mean you
[L1134] [40:47.76] know we get feedback on some of these
[L1135] [40:49.04] things it's like why is this not you
[L1136] [40:50.40] know GBT4 and I was like well we're on
[L1137] [40:52.40] like llama 2 it's not the same thing and
[L1138] [40:55.76] uh you know I was not not a researcher
[L1139] [40:58.96] right I was like but I and I you know
[L1140] [41:01.12] just wanted to to build the experiences
[L1141] [41:03.52] right and that sort of thing And um and
[L1142] [41:08.40] so so that was that was one thing was
[L1143] [41:10.16] that like I wanted to build stuff and I
[L1144] [41:11.84] wanted to go to the place where I could
[L1145] [41:13.12] actually build with the best model. Um
[L1146] [41:15.68] you know two again was um similar to
[L1147] [41:18.00] like you know Google originally like
[L1148] [41:20.16] seeing the people who were coming here
[L1149] [41:22.00] to open AAI and I was like well those
[L1150] [41:23.76] are people I really respect. I was like
[L1151] [41:25.28] those are I could actually work with
[L1152] [41:26.64] more senior people you know like meta
[L1153] [41:30.08] eights and nines at open I felt like
[L1154] [41:32.40] that I could where I was um and um you
[L1155] [41:37.60] know third was just like this also seems
[L1156] [41:40.08] like uh and it has been just a very
[L1157] [41:42.96] special place at at the point in time.
[L1158] [41:45.68] So I told a lot of people I was like,
[L1159] [41:47.04] you know, I felt like this would be like
[L1160] [41:49.20] the most similar to starting at Google
[L1161] [41:52.24] in 2000. So not not to 1998, but like
[L1162] [41:54.96] let's say 2000, right? Like they kind of
[L1163] [41:56.72] got some footing and got some, you know,
[L1164] [41:58.56] product market fit. And so like just as
[L1165] [42:00.40] a personal level, that was just a very
[L1166] [42:02.24] exciting thing.
[L1167] [42:03.60] >> Um and um you know, the last one was
[L1168] [42:06.72] that u funny thing is that when I I
[L1169] [42:10.64] really enjoyed calendar because I it was
[L1170] [42:12.64] consumer and I shipped to a lot of
[L1171] [42:14.00] people. I went to Facebook because I
[L1172] [42:15.60] thought huge consumer place. Ended up
[L1173] [42:19.12] not doing consumer at all, right? Ended
[L1174] [42:20.80] up doing developer tools, but like you
[L1175] [42:23.04] know my users were my friends at work.
[L1176] [42:24.64] It was just like 20,000 people, not like
[L1177] [42:26.24] a billion people, but it was good enough
[L1178] [42:27.60] for me at the time. And then, you know,
[L1179] [42:30.08] thinking about OpenAI and then the
[L1180] [42:32.00] chance to actually, you know, come back
[L1181] [42:33.76] to to consumer um or at least like have
[L1182] [42:37.20] a large user base, right? And so now
[L1183] [42:39.52] working on codecs um you know I wonder
[L1184] [42:42.24] if like over a million weeklyies or I
[L1185] [42:44.16] forget how much it is right now um and
[L1186] [42:46.16] and just keeps growing like like you
[L1187] [42:49.20] know hockey stick or more like vertical
[L1188] [42:50.64] line than hockey stick even um that uh
[L1189] [42:54.64] you know so it's like way more than the
[L1190] [42:56.88] 20 to 40,000 developers you know you
[L1191] [42:59.28] could affect at meta.
[L1192] [43:00.80] >> Yeah absolutely and dev tooling for the
[L1193] [43:03.44] industry almost.
[L1194] [43:04.64] >> Yeah. Um, Meta when I think of the
[L1195] [43:06.80] company it's kind of engineering driven
[L1196] [43:10.80] like engineers are king and queen I
[L1197] [43:13.60] guess and they kind of like drive
[L1198] [43:15.20] everything. It's very bottoms up from
[L1199] [43:16.64] that sense. And I feel like a lot of the
[L1200] [43:19.28] lab companies are also like that but on
[L1201] [43:22.48] the research side. So rather than
[L1202] [43:24.32] engineer is the first class citizen it's
[L1203] [43:27.20] like let's make sure the research goes
[L1204] [43:29.04] well and for good reason right like
[L1205] [43:30.32] that's also part of why you came is the
[L1206] [43:31.92] models are good. But as an engineer, you
[L1207] [43:34.96] mentioned you weren't doing research.
[L1208] [43:36.96] Um, what are your thoughts on that
[L1209] [43:38.40] researchled culture versus engineering
[L1210] [43:40.48] le culture?
[L1211] [43:41.36] >> I mean, it was certainly an adjustment,
[L1212] [43:42.80] right? I mean, I think if anyone who
[L1213] [43:44.32] comes here and says otherwise is a liar,
[L1214] [43:46.40] but [laughter]
[L1215] [43:47.52] um, you know, if you've been at like the
[L1216] [43:48.72] fangs or whatever. Um, and uh, but you
[L1217] [43:52.64] know, they are, you know, when you talk
[L1218] [43:55.04] about impact, right, which I think is
[L1219] [43:56.56] important, like a real like you
[L1220] [43:57.68] genuinely, you know, mean it. um like I
[L1221] [44:02.32] you know I love the work that I do on
[L1222] [44:03.44] Codex on the harness and I think we do a
[L1223] [44:05.04] lot of very meaningful things um but you
[L1224] [44:08.80] know if the model weren't very good it
[L1225] [44:10.56] wouldn't really matter what we did you
[L1226] [44:12.08] know on the harness right and so um so I
[L1227] [44:14.88] don't uh
[L1228] [44:17.44] so you know that that's how it is I
[L1229] [44:20.40] would say um but I you know I feel
[L1230] [44:23.52] really great like you know we we sit
[L1231] [44:25.04] right next to the the research team uh
[L1232] [44:27.12] work really closely with And um and so
[L1233] [44:30.16] that relationship that we have that we
[L1234] [44:32.08] get to co-develop the thing. I mean that
[L1235] [44:34.40] that was another reason you know leaving
[L1236] [44:36.16] leaving Meta I mean was that for for for
[L1237] [44:39.12] in the LM space was like you know I want
[L1238] [44:41.92] to build the product with the people who
[L1239] [44:44.16] are building the model so we can do this
[L1240] [44:45.68] thing together. I mean may you know
[L1241] [44:46.88] maybe you could do that there sort of
[L1242] [44:48.48] but not anyway the the the impact was
[L1243] [44:51.92] not you know quite quite the same. So
[L1244] [44:54.16] you mentioned I mean when you got here
[L1245] [44:55.44] it sounds like you were working on
[L1246] [44:56.40] codecs and starting uh that project up.
[L1247] [44:59.28] So I understand with the initial launch
[L1248] [45:01.36] of Codex CLI it was uh not exactly what
[L1249] [45:04.72] you hoped for like in terms of the how
[L1250] [45:07.28] it was received but um later it kind of
[L1251] [45:10.72] really all came together. Can you tell
[L1252] [45:12.96] that story?
[L1253] [45:13.84] >> Yeah sure. I mean it's been a wild ride.
[L1254] [45:16.56] So Codeex CLI we launched it in April
[L1255] [45:20.40] 2025. It was kind of like this like one
[L1256] [45:23.20] more thing moment at the end of the 03
[L1257] [45:25.20] uh 04 mini uh live stream and uh so we
[L1258] [45:28.80] demoed it live. We open sourced it, you
[L1259] [45:30.80] know, called 3o at that point. Uh a lot
[L1260] [45:33.20] of people tried it out, you know,
[L1261] [45:34.24] everyone was excited to try a new um
[L1262] [45:36.48] coding agent, you know, and it was and
[L1263] [45:38.56] it was pretty good, but it was it was
[L1264] [45:40.40] pretty rushed um to get it out the door,
[L1265] [45:42.80] right? There was um which in some ways
[L1266] [45:45.28] was good for engagement because now
[L1267] [45:46.48] we're open source. we were getting poll
