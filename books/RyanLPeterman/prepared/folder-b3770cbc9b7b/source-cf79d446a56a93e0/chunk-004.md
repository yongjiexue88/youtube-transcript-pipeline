Chunk 4; segments 1028–1401. Start may repeat the previous chunk for context.

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L1037] [52:59.52] uh manual that uh gave the definition
[L1038] [53:04.48] the manual of the language and for every
[L1039] [53:08.96] feature some rationale and some way it
[L1040] [53:13.04] could be implemented or was implemented
[L1041] [53:16.44] [snorts]
[L1042] [53:16.96] and that became the the foundation
[L1043] [53:19.04] document for the standardization.
[L1044] [53:21.68] when they were strongarmming you, what
[L1045] [53:23.84] if you had just said no? Like what would
[L1046] [53:25.76] have happened? I think well I think C++
[L1047] [53:31.60] would have faded into becoming an
[L1048] [53:35.44] academic
[L1049] [53:37.04] um
[L1050] [53:38.96] cute uh language that
[L1051] [53:42.64] was loved by some small community and it
[L1052] [53:46.96] would have disappeared out of the
[L1053] [53:48.40] mainstream of uh
[L1054] [53:51.68] of computing. And uh there are people
[L1055] [53:55.92] who say this stronger than I I do. Um
[L1056] [53:59.44] they say that C++ is spread and uses is
[L1057] [54:05.44] that it has a standard. It's not owned
[L1058] [54:07.52] by a corporation. It is one of the
[L1059] [54:10.16] things that sometimes blocks the um the
[L1060] [54:14.64] the the the wannabe C++ killers. I
[L1061] [54:19.12] remember the ads for Java and people
[L1062] [54:22.72] standing up saying we'll kill absolutely
[L1063] [54:25.12] kill C++ in two years. I thought that
[L1064] [54:28.72] was rude. Um and anyway, we have
[L1065] [54:34.72] 10 12 times more C++ developers today
[L1066] [54:38.88] than we had when they said it. So, uh
[L1067] [54:42.32] didn't work.
[L1068] [54:44.00] How is it that um C++ and not not
[L1069] [54:47.68] exactly that it's a war but just if we
[L1070] [54:49.84] looked at um adoption you know clearly
[L1071] [54:53.52] C++
[L1072] [54:55.04] gained a lot more adoption than Java yet
[L1073] [54:57.92] I know C or Java had the backing of uh
[L1074] [55:01.44] you know a big company that's putting a
[L1075] [55:03.76] lot of marketing dollars in and C++ was
[L1076] [55:06.96] kind of I I think you've said that it
[L1077] [55:09.28] had almost zero you know next to zero
[L1078] [55:11.92] marketing done for
[L1079] [55:13.36] uh next to zero was $5,000
[L1080] [55:16.96] to be used over three years
[L1081] [55:20.00] and uh son used
[L1082] [55:24.48] much more money on advertising and
[L1083] [55:27.28] marketing uh Java than was ever used in
[L1084] [55:31.28] C++ uh development.
[L1085] [55:34.56] Um and to this day the standards
[L1086] [55:37.12] committee has a problem. government has
[L1087] [55:38.64] no funding
[L1088] [55:40.48] and uh that means that it's hard to do
[L1089] [55:43.44] experiments. It's hard to deploy things
[L1090] [55:46.08] and uh other language communities keep
[L1091] [55:51.52] um sort of stealing uh C++ uh compiler
[L1092] [55:56.08] and tool developers because they're
[L1093] [55:58.16] good. Uh but it's makes it hard to to to
[L1094] [56:02.80] predict how fast we can implement things
[L1095] [56:06.64] today. Last I checked, the C++ standards
[L1096] [56:10.00] committee had 527
[L1097] [56:13.36] members and we work on consensus.
[L1098] [56:18.24] Uh because if you don't have consensus
[L1099] [56:21.20] then you get dialects. Um, we don't want
[L1100] [56:24.88] to have a feature in that's voted in um,
[L1101] [56:28.64] say 60 to uh, 40 or even worse 52 to 48.
[L1102] [56:35.36] No uh, percent. We we we don't do that
[L1103] [56:40.16] and uh, that's painful and tedious and
[L1104] [56:44.24] good.
[L1105] [56:45.20] >> When you say consensus that 100% need to
[L1106] [56:47.84] approve
[L1107] [56:48.40] >> 100% is not uh necessary. We we don't
[L1108] [56:52.96] need unanimity. We need a massive
[L1109] [56:56.48] majority and basically I would like to
[L1110] [57:00.00] see 90%.
[L1111] [57:01.76] And we often do 80% I start to worry.
[L1112] [57:06.80] And what's the lower bound that's coded
[L1113] [57:10.08] into the rules?
[L1114] [57:11.12] >> There's no lower bound coded into the
[L1115] [57:13.28] rules. The rule says that the convenor
[L1116] [57:17.60] or of the ISO committee um determines
[L1117] [57:21.04] what is consensus.
[L1118] [57:23.36] So
[L1119] [57:24.88] pure numbers doesn't say it. Could you
[L1120] [57:27.44] imagine you had
[L1121] [57:30.48] a vote [snorts] 95%
[L1122] [57:35.20] versus 5%.
[L1123] [57:38.00] But the implementers of C++
[L1124] [57:42.08] compiler and standard libraries from
[L1125] [57:45.52] Google, Apple, Microsoft uh and uh
[L1126] [57:52.08] others were all in the 5%. Is that
[L1127] [57:55.84] consensus? I can reassure you that no
[L1128] [57:59.44] convenor would call that consensus.
[L1129] [58:02.24] >> And that makes sense intuitively. I kind
[L1130] [58:04.96] of wonder with democratic decisions
[L1131] [58:08.08] there needs to be objective rules. So
[L1132] [58:10.48] like what if the convenor made the wrong
[L1133] [58:12.80] decision? It happens but
[L1134] [58:17.44] you you can't just have numeric rules.
[L1135] [58:20.08] Uh not everybody cares for the whole
[L1136] [58:22.72] language. Not everybody uh understands
[L1137] [58:25.92] what's going on. You can vote at your
[L1138] [58:29.04] third meeting. So you you might have uh
[L1139] [58:32.72] somebody with a vote that has uh
[L1140] [58:37.36] well eight months of experience with the
[L1141] [58:39.84] standardization and don't understand
[L1142] [58:41.84] standardization and knows only what they
[L1143] [58:46.40] known from their development
[L1144] [58:48.56] organization that they have been part of
[L1145] [58:51.44] which might be a small one. um you you
[L1146] [58:55.20] you need some some judgment and you hope
[L1147] [58:58.96] that the convenor has that judgment. the
[L1148] [59:02.48] convenor uh always uh asks the national
[L1149] [59:06.56] representatives
[L1150] [59:08.48] um I mean the other way of getting a
[L1151] [59:11.76] consensus is that you have a massive
[L1152] [59:14.08] consensus but you have 10 countries that
[L1153] [59:18.48] where the representatives didn't agree
[L1154] [59:21.84] that's not consensus and even when there
[L1155] [59:25.52] looks if there is a
[L1156] [59:29.68] look if everybody body is for, if it's
[L1157] [59:33.20] massive and all of that, there's not a
[L1158] [59:35.20] problem. But if there's a problem, the
[L1159] [59:38.80] convenor
[L1160] [59:40.32] asks the national body heads, he asks
[L1161] [59:42.72] the implementers,
[L1162] [59:44.64] uh, sort of key people that are
[L1163] [59:47.76] necessary for getting the
[L1164] [59:51.84] voted change
[L1165] [59:54.16] uh, into real use. sometimes educators
[L1166] [59:57.84] also uh before they make that decision.
[L1167] [01:00:01.44] Uh not everybody weighs equally uh once
[L1168] [01:00:04.88] there's a disagreement. For this podcast
[L1169] [01:00:08.24] I produced transcripts for every episode
[L1170] [01:00:10.24] for convenient skimming and I built a
[L1171] [01:00:12.48] custom tool to automate that. Recently I
[L1172] [01:00:14.96] noticed in the Barbara Liskoff
[L1173] [01:00:16.72] transcript my simple speechtoext tool
[L1174] [01:00:19.76] was getting a lot of things wrong. For
[L1175] [01:00:21.44] instance, the clue programming language
[L1176] [01:00:23.36] is spelled all caps clu, not clue. So to
[L1177] [01:00:27.76] fix this, I used cursor 3, picked the
[L1178] [01:00:30.64] strongest version of opus 4.7 extra high
[L1179] [01:00:33.84] and had an agent make a plan to fix
[L1180] [01:00:35.52] that. And while I was waiting, I figured
[L1181] [01:00:37.44] I'd trigger a few more agents for code
[L1182] [01:00:39.04] cleanups and front-end improvements. Um,
[L1183] [01:00:41.60] it generated a reasonable plan with rich
[L1184] [01:00:43.76] system diagrams. It applied all the
[L1185] [01:00:46.08] changes within minutes and worked on the
[L1186] [01:00:48.16] first try. So if you want to build
[L1187] [01:00:50.24] something with the flexibility of
[L1188] [01:00:51.76] sending off a bunch of agents with
[L1189] [01:00:53.52] frontier models of your choice, you can
[L1190] [01:00:55.68] go to cursor.com to try out cursor 3.
[L1191] [01:00:59.28] OpenAI, [snorts]
[L1192] [01:01:00.24] Enthropic, Cursor, and Verscell all use
[L1193] [01:01:03.60] this product to make their lives better.
[L1194] [01:01:05.76] And the problem it solves is when you're
[L1195] [01:01:07.84] building SAS or an AI product and you
[L1196] [01:01:10.40] want to sell to other companies, there's
[L1197] [01:01:12.24] all these requirements you need to meet.
[L1198] [01:01:14.32] There's SSO, there's SKIM, there's
[L1199] [01:01:16.96] arbback, there's audit logs. These are
[L1200] [01:01:19.36] all things that take time to integrate
[L1201] [01:01:21.44] but aren't the main focus of your app.
[L1202] [01:01:23.36] Work OS is an API layer that lets you
[L1203] [01:01:25.52] meet all of these requirements in just a
[L1204] [01:01:27.76] few lines of code. So, let's say you
[L1205] [01:01:29.68] have a new SAS product and you want to
[L1206] [01:01:31.60] sell to other companies. Work OS will
[L1207] [01:01:33.84] solve all of these critical feature gaps
[L1208] [01:01:35.76] for you. You can check them out at
[L1209] [01:01:38.24] workos.com to learn more and get
[L1210] [01:01:40.56] started. and I appreciate them for
[L1211] [01:01:42.72] supporting my work and sponsoring this
[L1212] [01:01:44.48] podcast.
[L1213] [01:01:45.36] >> About the standards committee, I I saw
[L1214] [01:01:47.84] in some of your writing, you said um one
[L1215] [01:01:50.56] of the most negatively received ideas
[L1216] [01:01:52.80] you'd ever presented was uh auto. And I
[L1217] [01:01:56.00] know auto eventually made its way in
[L1218] [01:01:57.68] there, but what's the story behind why
[L1219] [01:01:59.44] it was so, you know, negatively received
[L1220] [01:02:02.24] at that time?
[L1221] [01:02:03.68] >> It was just unusual. people thought was
[L1222] [01:02:06.00] weakening the type system.
[L1223] [01:02:08.96] And uh also it opens the door to fairly
[L1224] [01:02:14.64] general generic programming that is not
[L1225] [01:02:17.60] heavily uh syntax based. And auto is the
[L1226] [01:02:23.20] beginning of concepts which is the um
[L1227] [01:02:27.36] ability to put constraints on uh generic
[L1228] [01:02:32.24] code. And auto is just the simplest
[L1229] [01:02:35.12] constraint. It must be a type as opposed
[L1230] [01:02:38.24] to a say a value seven. [snorts]
[L1231] [01:02:42.40] And uh maybe I didn't explain this well
[L1232] [01:02:46.24] enough uh and there's a variety of
[L1233] [01:02:50.80] backgrounds and in the committee and
[L1234] [01:02:54.64] maybe they they didn't know languages of
[L1235] [01:02:57.76] the uh generic types uh ML hasll things
[L1236] [01:03:03.60] like that. So it it was it was horrible
[L1237] [01:03:09.44] uh
[L1238] [01:03:11.36] um so anyway we still got it um because
[L1239] [01:03:17.20] we we needed something like that but it
[L1240] [01:03:19.68] wasn't enough. I have looked at
[L1241] [01:03:21.92] industrial software and problems with
[L1242] [01:03:24.56] overuse of auto. You should only use
[L1243] [01:03:28.32] auto when you have an idea about what is
[L1244] [01:03:32.64] needed there. It's good in generic code
[L1245] [01:03:35.76] where there's uh you you you go and
[L1246] [01:03:39.60] eventually you check the the type is
[L1247] [01:03:42.40] correct that auto has resolved to
[L1248] [01:03:45.28] something that supports the uh
[L1249] [01:03:47.76] operations that you're going to do on it
[L1250] [01:03:50.56] and that's what concept formalizes but
[L1251] [01:03:54.08] it was always checked at the end and I
[L1252] [01:03:57.44] noticed a group of people that was
[L1253] [01:03:59.28] overusing auto in a
[L1254] [01:04:02.96] actually in a framework for um
[L1255] [01:04:06.16] networking.
[L1256] [01:04:07.76] And they were saying that they were
[L1257] [01:04:10.24] being slowed down, not so much with
[L1258] [01:04:13.12] bugs, but they had to look up the
[L1259] [01:04:16.08] functions being called to see what that
[L1260] [01:04:19.52] auto could possibly bind to.
[L1261] [01:04:22.96] And then they had to put in comments
[L1262] [01:04:25.28] that says what the the um what the auto
[L1263] [01:04:30.08] uh was meant. So you you have auto and
[L1264] [01:04:32.80] the comment says uh must be an input
[L1265] [01:04:36.00] channel.
[L1266] [01:04:38.56] Now you simply define input channel and
[L1267] [01:04:42.48] then instead of saying auto you say
[L1268] [01:04:45.20] input channel auto
[L1269] [01:04:48.24] fine that's what the system is uh my
[L1270] [01:04:51.76] design of that simply said that auto is
[L1271] [01:04:54.96] the simplest concept and you should
[L1272] [01:04:57.28] simply only set input channel uh C
[L1273] [01:05:01.04] equals blah blah blah but anyway the the
[L1274] [01:05:05.20] committee wanted a an indicator that
[L1275] [01:05:08.40] this was going on.
[L1276] [01:05:10.96] Oh, well,
[L1277] [01:05:11.76] >> I saw another anecdote in kind of the
[L1278] [01:05:14.24] standards committee being heated at some
[L1279] [01:05:16.56] times. You mentioned there's this thing
[L1280] [01:05:18.88] about shuttle diplomacy between two
[L1281] [01:05:21.60] corners of the room because I think it
[L1282] [01:05:24.16] was IBM and Intel. They both needed
[L1283] [01:05:26.88] different support.
[L1284] [01:05:27.92] >> That's right.
[L1285] [01:05:28.64] >> What's the story behind that? And I was
[L1286] [01:05:31.12] actually talking to Brian Mcnite who
[L1287] [01:05:35.28] were the IBM rep at the time and it was
[L1288] [01:05:39.68] last week and we were we were discussing
[L1289] [01:05:42.64] some of the things that was happening
[L1290] [01:05:44.24] then. So it it's still remembered. So
[L1291] [01:05:48.08] basically IBM was doing the uh what's
[L1292] [01:05:52.80] that architecture called? Uh
[L1293] [01:05:54.96] >> uh power PC. Power PC and um
[L1294] [01:05:58.24] >> the X86
[L1295] [01:05:59.12] >> and the Intel was doing well Intel and
[L1296] [01:06:01.60] they have different models of the
[L1297] [01:06:03.84] underlying hardware especially uh
[L1298] [01:06:07.44] coordination with the uh caches and
[L1299] [01:06:11.12] things like that. And basically
[L1300] [01:06:16.16] yeah and uh the guy representing Intel
[L1301] [01:06:19.92] wasn't actually an Intel guy. that was
[L1302] [01:06:22.48] uh uh he he he and any anyway
[L1303] [01:06:27.60] also a good guy. I use some of his
[L1304] [01:06:29.36] slides in my presentations. It's uh so I
[L1305] [01:06:32.32] knew these guys but they were totally
[L1306] [01:06:35.12] deadlocked. I mean this these are
[L1307] [01:06:39.36] massive again massive organizations with
[L1308] [01:06:42.96] massive amounts of code out there and um
[L1309] [01:06:48.80] uh
[L1310] [01:06:50.61] [sighs]
[L1311] [01:06:51.36] basically
[L1312] [01:06:56.96] some things could be done but
[L1313] [01:07:02.80] the the IBM guy Brian
[L1314] [01:07:05.76] said that they had a lot of software
[L1315] [01:07:09.68] mostly in the lowest level even down in
[L1316] [01:07:14.24] the the microode uh that was relying on
[L1317] [01:07:18.88] the way they have done it and the people
[L1318] [01:07:22.56] who had done it had left the company.
[L1319] [01:07:25.20] They they was done a long time ago and
[L1320] [01:07:28.48] they just couldn't rewrite all of that
[L1321] [01:07:31.36] code and get it right even if the intel
[L1322] [01:07:35.52] guys was right.
[L1323] [01:07:38.40] Okay. And the intel guys had similar uh
[L1324] [01:07:42.00] arguments and similar uh points. This is
[L1325] [01:07:45.04] better. We are using it. And so I was
[L1326] [01:07:48.32] shuffling. They were definitely they
[L1327] [01:07:49.92] were in different corners of a large
[L1328] [01:07:52.24] room. And so I go up to the Intel guy,
[L1329] [01:07:56.64] um, the guy representing Intel here and
[L1330] [01:08:01.44] what's the problem here? Tell him tell
[L1331] [01:08:03.84] me about it. Explain it. I go down,
[L1332] [01:08:06.08] explain he's saying this. They say,
[L1333] [01:08:08.00] "Well, there's this, this, this." And I
[L1334] [01:08:10.16] go back again. And I spent a couple of
[L1335] [01:08:12.48] hours literally doing shuttle diplomacy,
[L1336] [01:08:15.28] walking from one corner of the room to
[L1337] [01:08:17.44] the other. And um we we reached an
[L1338] [01:08:21.68] agreement and that's in uh C++ 11.
[L1339] [01:08:26.40] And a couple of years later they both uh
[L1340] [01:08:30.16] agreed that they were now using a
[L1341] [01:08:33.20] combination of what they had before and
[L1342] [01:08:35.84] what the other guys brought in. So we
[L1343] [01:08:39.20] they actually the result was uh was
[L1344] [01:08:42.56] improvement
[L1345] [01:08:44.16] cross-pollination.
[L1346] [01:08:45.76] >> That's funny. Why did you have to do
[L1347] [01:08:47.76] shuttle diplomacy? Why not just a group
[L1348] [01:08:49.92] conversation with
[L1349] [01:08:51.12] >> Because they've been trying that for
[L1350] [01:08:53.20] days and probably for meetings before
[L1351] [01:08:55.68] that and it didn't work.
[L1352] [01:08:58.80] So I I guess I was just translating and
[L1353] [01:09:02.16] asking questions.
[L1354] [01:09:04.64] I mean those were experts. I don't
[L1355] [01:09:06.40] consider myself expert at that level. Um
[L1356] [01:09:10.08] I mean I've done hardware. I've done
[L1357] [01:09:11.92] microode. So I'm I'm not an amateur, but
[L1358] [01:09:15.52] but these guys are really good. Um,
[L1359] [01:09:19.95] [snorts]
[L1360] [01:09:21.52] so the the the the IBM guy is now the
[L1361] [01:09:25.84] guy doing most of the synchronization
[L1362] [01:09:28.00] under Linux.
[L1363] [01:09:30.08] We're we're still using his stuff uh
[L1364] [01:09:32.88] today. He has a C version of it so he
[L1365] [01:09:35.84] can get it into the but it's a bottom of
[L1366] [01:09:38.32] the uh Linux kernel. When I was reading
[L1367] [01:09:41.44] your writing in these papers, there's
[L1368] [01:09:43.68] this part where it seems like in 1995,
[L1369] [01:09:47.84] you had this idea to introduce uh some
[L1370] [01:09:50.96] form of automatic garbage collection
[L1371] [01:09:53.44] into C++. And that kind of surprised me
[L1372] [01:09:56.24] because when I when I think about C++,
[L1373] [01:09:58.72] my one of my immediate thoughts is no
[L1374] [01:10:00.72] garbage collector. We're going to man
[L1375] [01:10:03.12] manually or you know manage the memory
[L1376] [01:10:05.28] ourselves. How how would that even work?
[L1377] [01:10:08.40] Um
[L1378] [01:10:10.24] there's two things there. One, I wanted
[L1379] [01:10:13.60] to automate
[L1380] [01:10:15.60] resource management in general, not just
[L1381] [01:10:18.08] garbage and not just memory. And uh for
[L1382] [01:10:21.68] that you have constructors, destructors
[L1383] [01:10:24.08] and the techniques that was later later
[L1384] [01:10:26.40] known as uh our AI resource acquisition
[L1385] [01:10:30.32] is initialization
[L1386] [01:10:32.16] which is probably my worst naming ever.
[L1387] [01:10:36.16] But um I was busy at the time. Um so
[L1388] [01:10:42.56] in the standards committee those people
[L1389] [01:10:44.64] that insisted that we needed to be able
[L1390] [01:10:48.24] to do garbage collection
[L1391] [01:10:51.04] and there was garbage collectors out uh
[L1392] [01:10:55.04] there. Oh that was Hans Berm. He was the
[L1393] [01:10:57.76] one that representing the internal model
[L1394] [01:11:00.00] of stuff. He he has a conservative
[L1395] [01:11:03.44] garbage collector still used today and
[L1396] [01:11:07.68] we thought we needed an interface so
[L1397] [01:11:10.00] that uh it could be standard how you
[L1398] [01:11:12.64] used such a garbage collector
[L1399] [01:11:16.72] and so basically I was listening to the
[L1400] [01:11:19.36] users expert users and they thought it
[L1401] [01:11:23.36] was necessary. I thought that support
[L1402] [01:11:26.80] for
[L1403] [01:11:28.72] memory management, resource management
[L1404] [01:11:31.52] was important. I've thought that from
[L1405] [01:11:34.08] the beginning. I didn't think garbage
[L1406] [01:11:36.24] collection was appropriate for a lot of
[L1407] [01:11:38.56] what I was doing, but certainly um
[L1408] [01:11:42.32] automating
[L1409] [01:11:43.92] uh the management was ideal.
[L1410] [01:11:48.56] And so after a long set of discussions
