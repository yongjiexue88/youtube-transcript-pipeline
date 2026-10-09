Chunk 4; segments 1027–1372. Start may repeat the previous chunk for context.

# Turing Award Winner: Thinking Clearly, Paxos vs Raft, Working With Dijkstra | Leslie Lamport

Source ID: source-4005a50ded85af4c
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Thinking_Clearly,_Paxos_vs_Raft,_Working_With_Dijkstra_Leslie_Lamport_en.txt
Video: https://www.youtube.com/watch?v=U719vQz-WFs

[L1036] [48:35.84] first uh phase once
[L1037] [48:39.84] uh and you don't have to do it again as
[L1038] [48:43.28] long as you have the same leader. Uh but
[L1039] [48:46.56] it's only the second part that you have
[L1040] [48:49.20] to do and then you have to elect the the
[L1041] [48:52.16] new leader if a new leader fails and do
[L1042] [48:55.04] the first part. So think about it in
[L1043] [48:57.44] those two phases. But the way people the
[L1044] [49:00.32] way engineers you know like to think
[L1045] [49:02.64] about it is well you do this you know
[L1046] [49:06.40] you talking about the first part the the
[L1047] [49:08.96] second phase you keep doing this uh
[L1048] [49:11.44] until the leader fa fails and then you
[L1049] [49:14.16] go back then you have to do this thing
[L1050] [49:16.00] so it's explaining it in the in the
[L1051] [49:19.52] opposite order uh and in fact you know
[L1052] [49:22.32] when you start it from from fresh the uh
[L1053] [49:25.92] you don't have to do the first uh uh the
[L1054] [49:29.68] first phase you can you basically what
[L1055] [49:32.32] what's done in the first phase could be
[L1056] [49:34.00] just built in into the initial state but
[L1057] [49:37.92] you know I think that that's the right
[L1058] [49:39.60] you know of those two phases the way to
[L1059] [49:41.68] understand it uh but you know the raft
[L1060] [49:46.80] people also had this idea that you know
[L1061] [49:48.96] raft is better because it's simpler and
[L1062] [49:51.76] I I must say that a lot of people say
[L1063] [49:53.52] that uh Paxos is hard to understand and
[L1064] [49:56.72] I don't understand why. I mean, I've
[L1065] [49:58.64] explained it to some people in five
[L1066] [50:00.48] minutes and they understood it. At any
[L1067] [50:02.56] rate, the raft people said that one of
[L1068] [50:04.32] the ideas were simpler because and they
[L1069] [50:07.52] even have, you know, taught, you know,
[L1070] [50:09.60] Paxos to one class and and uh the raft
[L1071] [50:13.92] to another and they took and then yes,
[L1072] [50:16.08] the people all the students said that
[L1073] [50:18.00] yes, it was more understandable. Uh the
[L1074] [50:21.12] interesting thing about it though is
[L1075] [50:22.96] that uh there was a bug discovered in
[L1076] [50:26.56] raft and fixed but I believe that the
[L1077] [50:31.44] algorithm that they found more
[L1078] [50:33.12] understandable was one with that bug.
[L1079] [50:37.04] So uh made me realize that uh you know
[L1080] [50:41.44] what most people you know what does
[L1081] [50:43.12] understanding mean and for me
[L1082] [50:47.04] understanding means you know you can
[L1083] [50:49.12] write a proof of it but what
[L1084] [50:51.60] understanding means for most people is
[L1085] [50:54.08] warm fuzzy feeling and you know the raft
[L1086] [50:57.84] description gave them you know more of a
[L1087] [51:00.00] warm fuzzy feeling because you know you
[L1088] [51:03.44] know that that was seems to be the way
[L1089] [51:06.00] you know programmers, you know, like to
[L1090] [51:08.32] think about the the algorithm, you know,
[L1091] [51:11.28] you know, the second phase, you know,
[L1092] [51:13.84] first until, you know, you get a failure
[L1093] [51:16.88] and uh
[L1094] [51:18.96] but the way I describe it is one that
[L1095] [51:22.72] helps you get a better understanding of
[L1096] [51:24.96] why it actually works.
[L1097] [51:26.96] >> So, yeah, we talked about a lot of your
[L1098] [51:28.56] papers. I know one of your other uh
[L1099] [51:31.12] contributions whether you knew it or not
[L1100] [51:33.44] at the time was latte and uh building
[L1101] [51:37.04] that and something that has impacted the
[L1102] [51:40.24] entire academic community. What's the
[L1103] [51:42.96] story behind wanting to build latte?
[L1104] [51:46.88] >> Oh, that was uh very simple. Um,
[L1105] [51:52.24] I was wanted I was in the process of
[L1106] [51:57.44] starting to write a book and uh
[L1107] [52:02.24] it was clear that tech was the basic uh
[L1108] [52:06.08] type setting system that one had to use.
[L1109] [52:08.80] But you know I felt that I would need
[L1110] [52:13.04] macros uh to make tech do what I wanted
[L1111] [52:16.48] it to do. And uh so
[L1112] [52:21.92] I decide figured with uh been a little
[L1113] [52:25.44] extra effort uh I could make the macros
[L1114] [52:28.48] usable by other people. The system I had
[L1115] [52:31.28] been using before tech it's called
[L1116] [52:32.96] scribe and uh that really had the basic
[L1117] [52:38.48] idea of scribe was that
[L1118] [52:43.28] you describe the logical structure of of
[L1119] [52:46.80] the document
[L1120] [52:48.96] not and the
[L1121] [52:51.44] and scribe will do the formatting. Well,
[L1122] [52:54.80] scribe didn't do that great a job of
[L1123] [52:56.48] formatting. Uh so, uh but
[L1124] [53:01.04] obviously, you know, I like the idea
[L1125] [53:04.32] abstraction that it's the ideas that
[L1126] [53:07.68] matter, not the text that ma, you know,
[L1127] [53:10.40] the the writing that matters, not the
[L1128] [53:13.12] type setting. And so,
[L1129] [53:16.48] um, I actually
[L1130] [53:21.36] at some point, uh, I met Peter Gordon,
[L1131] [53:24.80] Addison Wesley, uh, I'm not sure what
[L1132] [53:27.20] what you would call him, but he looks
[L1133] [53:28.64] for, you know, books to publish. And,
[L1134] [53:31.04] uh, he convinced me that I should write
[L1135] [53:34.24] a book on it. And those days, it never
[L1136] [53:37.84] occurred to me people would actually
[L1137] [53:39.20] spend money for a book about software.
[L1138] [53:41.92] But you know what the hell? And what he
[L1139] [53:45.60] did was he introduced me to uh a
[L1140] [53:50.80] typographic designer at uh Addison
[L1141] [53:53.20] Wesley who was responsible for really
[L1142] [53:56.72] for the typographic design that's in the
[L1143] [53:59.76] standard uh latex styles. You know,
[L1144] [54:03.20] basically I just did that in my quote
[L1145] [54:05.92] spare time. You know, took me six or
[L1146] [54:08.88] nine months or so. I I suppose the uh
[L1147] [54:12.32] statute of limitations has run out, but
[L1148] [54:14.40] I was really, you know, spent some time
[L1149] [54:16.64] working on that when I was allegedly,
[L1150] [54:19.60] you know, billing the time to some
[L1151] [54:22.32] project that had nothing to do with it.
[L1152] [54:26.32] >> On the topic of writing, you have a
[L1153] [54:28.96] quote that I really enjoy. It's if
[L1154] [54:31.04] you're if you're thinking without
[L1155] [54:32.88] writing, you only think you're thinking.
[L1156] [54:35.84] And I was curious to hear your thoughts
[L1157] [54:38.16] on what you mean by that.
[L1158] [54:40.80] >> Well, it was really meant for, you know,
[L1159] [54:43.76] people building computer systems. You
[L1160] [54:46.32] have an idea and you think it's going to
[L1161] [54:47.84] work. Uh or you have something that, you
[L1162] [54:50.48] know, you think is something that
[L1163] [54:52.24] somebody else will you want to use.
[L1164] [54:54.64] Well, write a description of it. Uh
[L1165] [54:56.88] there's an old maxim that I don't I
[L1166] [55:00.24] heard uh that is you know write the
[L1167] [55:04.16] instruction manual before you write the
[L1168] [55:06.08] program. a great advice. Uh I did not do
[L1169] [55:11.76] that uh with latte but it I definitely
[L1170] [55:16.08] when I was writing the book and I
[L1171] [55:19.84] discovered that something was hard to to
[L1172] [55:22.48] describe hard to explain that needed to
[L1173] [55:25.44] be changed and I made you know a number
[L1174] [55:27.84] of uh of changes to it uh as a result of
[L1175] [55:31.28] that but uh I didn't start at the
[L1176] [55:34.40] beginning with the instruction manual.
[L1177] [55:36.72] Why is writing conducive to good
[L1178] [55:39.20] thinking?
[L1179] [55:41.52] >> Because it's very easy to
[L1180] [55:45.20] uh
[L1181] [55:47.36] it's very easy to fool yourself.
[L1182] [55:50.08] Uh I mean that underlies my uh my whole
[L1183] [55:56.16] idea of of writing proofs. One thing I
[L1184] [55:59.44] learned is that you had to write a a
[L1185] [56:02.00] correctness proof of an concurrent
[L1186] [56:03.68] algorithm.
[L1187] [56:05.20] And when my algorithm was starting to
[L1188] [56:08.80] get more complicated,
[L1189] [56:11.20] the proofs started I started writ
[L1190] [56:14.56] PhD in math. I knew how to write proofs
[L1191] [56:16.96] and I was starting writing the proofs
[L1192] [56:18.96] the way I would normally do. And I
[L1193] [56:22.00] realized it just didn't work because
[L1194] [56:24.48] there were just so many details involved
[L1195] [56:27.28] and I just couldn't keep track of them
[L1196] [56:28.88] and whether I had done it. And so as a
[L1197] [56:32.56] computer science know how to deal with
[L1198] [56:34.24] concurrency
[L1199] [56:35.76] uh it's hierarchical structure and so I
[L1200] [56:39.36] devised this hierarchical structure
[L1201] [56:41.20] where a proof is uh you know is a
[L1202] [56:44.64] sequence of steps each of which has a
[L1203] [56:47.12] proof and the proof is either a par well
[L1204] [56:51.28] a proof is either a paragraph or a
[L1205] [56:53.60] statement a sequence of steps each with
[L1206] [56:55.84] its proof and that proof can be either a
[L1207] [56:59.60] parag graph or a sequence of steps with
[L1208] [57:01.84] its proof and you know so you break the
[L1209] [57:04.08] whole problem up into these smaller
[L1210] [57:05.76] pieces. So there's never any question of
[L1211] [57:08.72] you know where is this coming from. You
[L1212] [57:10.56] know you're stating that this step
[L1213] [57:12.56] follows from you know this step this
[L1214] [57:14.64] step this step this step and if it does
[L1215] [57:16.72] not follow from that step your proof is
[L1216] [57:19.04] wrong. The theorem might be correct but
[L1217] [57:21.20] but means your proof is wrong. Um well
[L1218] [57:24.96] you know so I've discovered that worked
[L1219] [57:27.04] great on writing my proofs of programs
[L1220] [57:30.16] but I decided to really you know I also
[L1221] [57:33.36] write proofs of theorems you know you
[L1222] [57:35.44] know uh you know think proofs that are
[L1223] [57:38.56] things that are you know more like
[L1224] [57:39.84] ordinary math and I started trying that
[L1225] [57:42.40] on them and I discovered it worked
[L1226] [57:45.84] beautifully. So when I started to to try
[L1227] [57:49.44] to convince mathematicians to write
[L1228] [57:50.96] these proofs uh I started in one small
[L1229] [57:55.28] seminar I went you know won't describe
[L1230] [57:57.28] what it was about but uh and I I
[L1231] [57:59.68] described this this proof through maybe
[L1232] [58:02.24] uh 20 mathematicians or something their
[L1233] [58:05.76] reaction shocked me
[L1234] [58:08.80] they became angry
[L1235] [58:11.44] I really thought that they might
[L1236] [58:14.24] physically attack me. So
[L1237] [58:17.68] I believe that what's going on is that
[L1238] [58:20.56] when pe I mean I believe that's totally
[L1239] [58:22.16] irrational and when people act
[L1240] [58:24.32] irrationally
[L1241] [58:26.16] it tends to be out of fear
[L1242] [58:29.20] and what I believe people are afraid of
[L1243] [58:32.48] is that mathematicians are afraid of is
[L1244] [58:35.76] that they're going to have to write
[L1245] [58:37.20] their proofs to convince a a computer
[L1246] [58:40.32] program and and in fact you know and I
[L1247] [58:44.72] give it a one of those talks I gave you
[L1248] [58:47.28] know I say very clearly this doesn't
[L1249] [58:49.52] have to be you don't have to be any more
[L1250] [58:51.28] formal than you do you can write the
[L1251] [58:54.24] exact same thing proof you know but it's
[L1252] [58:56.72] just a matter of organizing things and
[L1253] [58:58.88] it's very simple you know hierarchical
[L1254] [59:00.80] structure and then when you're using a
[L1255] [59:02.88] fact mention that you're using that
[L1256] [59:05.36] nothing about formalism or anything you
[L1257] [59:08.72] know after I gave that talk someone got
[L1258] [59:12.48] up and said I don't want to have to
[L1259] [59:14.56] write my proof my my proofs for a
[L1260] [59:17.12] computer program.
[L1261] [59:20.00] And in fact, it's more work doing that
[L1262] [59:23.04] because the reason it's more work is
[L1263] [59:26.48] that it reveals what you haven't said
[L1264] [59:30.48] and that there's steps in there that you
[L1265] [59:34.56] know, you may think they're obvious, but
[L1266] [59:36.80] you haven't written them down.
[L1267] [59:39.68] And if you believe something is correct
[L1268] [59:43.36] but don't really if you if you think you
[L1269] [59:46.32] know something but don't write it down,
[L1270] [59:49.36] you only think you know it. And that's
[L1271] [59:52.00] where errors come in. You know, that's
[L1272] [59:53.68] where that one-third of your paper's
[L1273] [59:55.52] errors can, you know, you know, uh, come
[L1274] [59:58.72] in because it really makes you honest.
[L1275] [01:00:02.24] When I look across your career, I think
[L1276] [01:00:04.72] you had a lot of contributions people
[L1277] [01:00:06.80] might expect might come from academia,
[L1278] [01:00:10.00] these papers and things, but you did uh
[L1279] [01:00:12.64] all of your work in industry. Why did
[L1280] [01:00:15.44] you not see yourself as a academic and
[L1281] [01:00:18.00] more of uh working for industry? Well, I
[L1282] [01:00:21.28] started out programming
[L1283] [01:00:23.84] uh and I eventually got jobs where took
[L1284] [01:00:27.92] me into what we now call computer
[L1285] [01:00:30.56] science. At the time I never even
[L1286] [01:00:32.88] realized that uh there was you know
[L1287] [01:00:35.76] there could be a computer a science of
[L1288] [01:00:37.60] computing. Uh it wasn't until you know
[L1289] [01:00:41.68] maybe until
[L1290] [01:00:43.60] mid to late '7s that I realized yes
[L1291] [01:00:47.12] there was a computer science and know as
[L1292] [01:00:49.12] a computer scientist. Um but it never
[L1293] [01:00:52.96] seemed to me that like computer science
[L1294] [01:00:55.28] was a an academic subject. At some point
[L1295] [01:00:58.64] I, you know, had to make a choice
[L1296] [01:01:00.88] between doing computer science and
[L1297] [01:01:03.84] without calling it computer science or
[L1298] [01:01:06.00] or teaching math at a at a university.
[L1299] [01:01:08.56] And I I chose for random fairly random
[L1300] [01:01:13.84] reasons to you do computer science. Uh
[L1301] [01:01:18.24] so it you know for the first
[L1302] [01:01:22.64] I don't know
[L1303] [01:01:26.40] well till maybe the mid80s or something
[L1304] [01:01:28.96] it just didn't seem to me that you know
[L1305] [01:01:31.20] you know computer science was something
[L1306] [01:01:33.76] that people needed to go to to a
[L1307] [01:01:36.88] university to learn. And uh I suppose
[L1308] [01:01:41.12] afterwards that I was sort of I guess I
[L1309] [01:01:45.04] I just didn't think it would be fun
[L1310] [01:01:46.64] teaching computer science. So
[L1311] [01:01:49.28] >> I saw in your your writing you had a
[L1312] [01:01:51.36] footnote that said somewhere that you
[L1313] [01:01:53.36] you you felt like a a failure at some
[L1314] [01:01:56.00] point because you you wanted to develop
[L1315] [01:01:58.64] this grand theory of concurrency and you
[L1316] [01:02:02.16] never discovered it. Um do do you still
[L1317] [01:02:05.04] feel that way or what are your thoughts
[L1318] [01:02:06.88] on that that footnote? lots of people
[L1319] [01:02:09.44] who you know a large percentage of the
[L1320] [01:02:11.20] people who were doing things like I was
[L1321] [01:02:12.80] doing which is not a large number of
[L1322] [01:02:14.16] people uh there's this notion that uh
[L1323] [01:02:19.28] they're looking for the touring machine
[L1324] [01:02:21.76] of concurrency you know the touring
[L1325] [01:02:24.32] machine was this abstraction which
[L1326] [01:02:27.12] really captured what computing was
[L1327] [01:02:30.96] uh and
[L1328] [01:02:34.00] they were looking for something that
[L1329] [01:02:36.40] would be the you know the touring
[L1330] [01:02:38.64] machine of of
[L1331] [01:02:41.68] concurrent computing
[L1332] [01:02:44.40] and
[L1333] [01:02:48.08] you know nobody succeeded. I mean there
[L1334] [01:02:50.56] are some people who think they've
[L1335] [01:02:51.68] succeeded. Uh the patronets are are
[L1336] [01:02:55.04] something that uh I guess I don't have
[L1337] [01:02:57.20] time to to explain but uh there was a
[L1338] [01:03:00.80] big it was big in the 70s. Uh, and I was
[L1339] [01:03:05.52] actually surprised to think that there's
[L1340] [01:03:06.96] still a large community of people doing
[L1341] [01:03:09.28] uh, patriets. But what I now realize is
[L1342] [01:03:12.80] that patriets and
[L1343] [01:03:15.68] most of the things that people were
[L1344] [01:03:17.12] doing was really language-based.
[L1345] [01:03:19.84] And I was never interested in languages.
[L1346] [01:03:22.32] I'm interested in what the language is
[L1347] [01:03:25.20] expressing.
[L1348] [01:03:27.12] And you know I realized in some sense
[L1349] [01:03:30.64] you know maybe I've realized what the
[L1350] [01:03:32.48] touring machine of of of computing is
[L1351] [01:03:35.12] state machines. Uh state machines are a
[L1352] [01:03:38.72] little bit different the way I now
[L1353] [01:03:39.76] describe them. They don't have commands.
[L1354] [01:03:41.52] They just have a state and a and a next
[L1355] [01:03:44.24] state relation. Uh even simpler than
[L1356] [01:03:47.60] talking about commands and and and
[L1357] [01:03:50.24] values and stuff. Uh and you know to me
[L1358] [01:03:54.88] you know that's the uh that's the
[L1359] [01:03:57.04] touring machine of of con of concurrency
[L1360] [01:04:00.16] but it
[L1361] [01:04:03.44] uh it it doesn't have the function that
[L1362] [01:04:06.56] that touring machines offer because it
[L1363] [01:04:09.36] it doesn't what touring machines do is
[L1364] [01:04:13.28] uh describe what's you know what's
[L1365] [01:04:16.40] possible
[L1366] [01:04:18.08] uh and state machines can describe
[L1367] [01:04:21.68] anything
[L1368] [01:04:23.20] including things that are not possible.
[L1369] [01:04:26.24] Uh and and in fact uh the there's a good
[L1370] [01:04:32.56] reason for that. Um
[L1371] [01:04:35.60] for example
[L1372] [01:04:37.36] uh when I describe a uh an algorithm I
[L1373] [01:04:42.40] will talk about you know the values of a
[L1374] [01:04:45.04] variable you know can be any integer.
[L1375] [01:04:48.48] Now you can implement the program where
[L1376] [01:04:50.24] you have any integer
[L1377] [01:04:52.32] uh but that makes the but talking about
[L1378] [01:04:58.88] you know computer integers would
[L1379] [01:05:00.88] complicate things unnecessarily.
[L1380] [01:05:03.28] The people have this funny idea that you
[L1381] [01:05:05.68] know because something is infinite it's
