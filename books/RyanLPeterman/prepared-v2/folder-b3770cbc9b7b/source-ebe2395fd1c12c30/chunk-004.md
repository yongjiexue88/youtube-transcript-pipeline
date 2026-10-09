Chunk 4; segments 1024–1358. Start may repeat the previous chunk for context.

# Mozilla Firefox CTO: Chrome vs Firefox and Distinguished Eng Promos

Source ID: source-ebe2395fd1c12c30
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Mozilla_Firefox_CTO_Chrome_vs_Firefox_and_Distinguished_Eng_Promos_en.txt
Video: https://www.youtube.com/watch?v=KhJgI9u47kI

[L1033] [38:27.84] distribution advantages. I'm curious
[L1034] [38:30.00] what was the strategy at that time from
[L1035] [38:31.52] the Mozilla team to compete with Chrome.
[L1036] [38:35.60] So the strategy to compete with Chrome
[L1037] [38:37.76] was
[L1038] [38:39.92] multifaceted.
[L1039] [38:42.00] One of the parts was a recognition. I
[L1040] [38:44.40] think there was a little bit of denial
[L1041] [38:46.16] in the very early days about the deep
[L1042] [38:49.44] value that some of Chrome's
[L1043] [38:50.64] architectural advantages would provide.
[L1044] [38:52.96] And this was, you know, they came out
[L1045] [38:55.92] with a JavaScript engine with what's
[L1046] [38:57.68] referred to as a method JIT. We had a
[L1047] [38:59.76] tracing JIT. We thought the tracing jit
[L1048] [39:01.60] was good and was going to be better, but
[L1049] [39:04.72] in the end it wasn't. Chrome came out
[L1050] [39:07.20] with multipprocess architecture. I
[L1051] [39:10.40] remember the first thing that I heard
[L1052] [39:11.84] was, "Yeah, good luck doing that on
[L1053] [39:13.20] Mac." And then they figured out how to
[L1054] [39:15.12] do it on Mac. And there was a belief
[L1055] [39:17.36] that some of these things were not
[L1056] [39:19.36] possible until they were. And then once
[L1057] [39:21.76] they were, that they weren't the most
[L1058] [39:23.04] important thing. But eventually it
[L1059] [39:24.88] became clear that uh things like a
[L1060] [39:27.20] multipprocess architecture and things
[L1061] [39:28.64] like native video playback were really
[L1062] [39:30.96] essential and we had this issue
[L1063] [39:33.04] particularly on video playback where
[L1064] [39:35.04] because Chrome first had a better
[L1065] [39:36.72] plug-in architecture uh for Adobe Flash
[L1066] [39:39.20] and then was also early to introduce
[L1067] [39:40.80] native video playback they were able to
[L1068] [39:43.84] have a much more stable experience on
[L1069] [39:46.88] YouTube which was blowing up at the
[L1070] [39:48.32] time. Whereas Firefox on YouTube, which
[L1071] [39:51.20] was what everybody wanted to do on the
[L1072] [39:52.72] internet, was just crashing left and
[L1073] [39:54.56] right. And it wasn't stuff that we could
[L1074] [39:56.32] fix, it was Adobe's fault, and we really
[L1075] [40:00.00] couldn't do anything about it. And so we
[L1076] [40:02.72] had to work on
[L1077] [40:05.92] a lot of these really hard but discreet
[L1078] [40:08.48] challenges um of closing the gap with
[L1079] [40:12.08] Chrome. But then at the same time, there
[L1080] [40:14.08] was a desire of you can't just close the
[L1081] [40:15.60] gap. have to do something new and you
[L1082] [40:17.60] have to do something that is better and
[L1083] [40:20.08] rust and servo were our strategy for
[L1084] [40:23.36] doing better.
[L1085] [40:24.80] >> So you mentioned the strategy with servo
[L1086] [40:27.52] and the rewrite and rust. How did it go?
[L1087] [40:30.88] Was it successful? Well, we we know that
[L1088] [40:33.52] Google's distribution eventually
[L1089] [40:35.12] dominated, but how did the efforts with
[L1090] [40:37.12] servo go?
[L1091] [40:39.20] So on the one hand, servo and rust had
[L1092] [40:43.76] against all odds captured something
[L1093] [40:46.32] really real and servo as a browser
[L1094] [40:49.92] engine prototype had a lot of really
[L1095] [40:53.04] amazing stuff in it, right? It was not
[L1096] [40:56.00] complete, but it did have the skeleton
[L1097] [40:59.20] of certain features that had never been
[L1098] [41:01.12] done before, including a multi-threaded
[L1099] [41:03.20] CSS engine. But the problem was that we
[L1100] [41:07.44] had a team of you know a dozen people
[L1101] [41:09.84] working on rust and servo. Google had
[L1102] [41:12.96] hundreds and hundreds and hundreds of
[L1103] [41:14.48] engineers who were working on chromium.
[L1104] [41:16.80] We had less than that but still most of
[L1105] [41:19.28] Mozilla's efforts were directed towards
[L1106] [41:22.56] Gecko and Firefox because that was the
[L1107] [41:24.88] product that we had in market. So we had
[L1108] [41:26.72] this situation where in order to build a
[L1109] [41:29.52] competitive browser engine, it's not
[L1110] [41:32.00] like you need to just do this one time.
[L1111] [41:34.88] It's the accumulation of all of the work
[L1112] [41:37.76] over all of these years of hundreds of
[L1113] [41:39.60] engineers working on improving it and
[L1114] [41:42.24] improving the architecture, improving
[L1115] [41:43.44] the performance, improving the features.
[L1116] [41:45.36] And so every year there was more and
[L1117] [41:48.08] more stuff that server would have to
[L1118] [41:49.44] catch up with. And I think if you just
[L1119] [41:51.28] look at it, there's it's was very
[L1120] [41:53.68] difficult to believe that we would ever
[L1121] [41:55.44] end up in a situation where servo would
[L1122] [41:57.76] be competitive with a regular um
[L1123] [42:01.28] production browser engine. And so circa
[L1124] [42:04.16] like 2014 2015 that was a situation
[L1125] [42:07.28] where there was really a sense that we
[L1126] [42:09.36] needed to deliver a fully refreshed
[L1127] [42:12.96] version of Firefox that really got us
[L1128] [42:15.04] back in the game. that included this
[L1129] [42:18.00] parallel CSS engine that we uplifted
[L1130] [42:21.04] from servo and this was a project that I
[L1131] [42:25.68] personally led and was really the
[L1132] [42:28.40] highlight of my career working on it
[L1133] [42:30.48] because it was so exciting to be doing
[L1134] [42:32.96] something really new in a new
[L1135] [42:34.24] programming language that and every step
[L1136] [42:36.40] of the way there was this notion that
[L1137] [42:37.92] like that's definitely never going to
[L1138] [42:39.20] work right like how are you even going
[L1139] [42:41.12] to like hook this thing up and then we
[L1140] [42:42.40] hooked it up and we had it traversing
[L1141] [42:43.84] the DOM over C++ plus um you know we
[L1142] [42:46.64] have a C++ DOM and we're having this
[L1143] [42:48.96] Rust CSS engine and how you get these
[L1144] [42:52.00] two things to work together. There was
[L1145] [42:53.44] no tooling for it. We had to build it
[L1146] [42:54.80] all ourselves. At the end of the day it
[L1147] [42:56.88] was really a dramatic performance
[L1148] [42:58.96] improvement. I think it improved like
[L1149] [43:02.00] rendering time on Amazon.com by on the
[L1150] [43:04.80] order of 25%. which is just enormous in
[L1151] [43:07.36] terms of um web performance. And because
[L1152] [43:11.04] it was parallel and it can run on all of
[L1153] [43:13.12] your cores, it was and still is the
[L1154] [43:15.52] fastest CSS engine in the market.
[L1155] [43:17.52] Firefox really got back in the game and
[L1156] [43:20.24] was really performance competitive with
[L1157] [43:22.40] everything else out there. And that was
[L1158] [43:24.72] a really exciting moment for everybody
[L1159] [43:27.20] and realizing that if we just coordinate
[L1160] [43:28.88] and we do all the technical effort and
[L1161] [43:30.48] we make the right bets, we can win.
[L1162] [43:33.12] >> Okay. Okay. So, you mentioned that this
[L1163] [43:34.40] was one of the most proud moments of
[L1164] [43:37.04] your career and like a major launch,
[L1165] [43:38.88] very exciting project. I'm kind of
[L1166] [43:40.64] curious to talk about the career parts
[L1167] [43:42.16] of it. So, where were you in your career
[L1168] [43:44.24] at this point? And maybe you can talk
[L1169] [43:46.16] about how it grew um as you worked on
[L1170] [43:48.56] these projects.
[L1171] [43:50.00] >> Sure. So, I think when I started, I
[L1172] [43:53.20] don't know if Mozilla had levels. Um I
[L1173] [43:56.96] certainly wasn't aware of them if they
[L1174] [43:58.40] existed. Uh it was a culture of choose
[L1175] [44:00.96] your own title. Uh the title that I
[L1176] [44:02.88] chose for myself was negative entropy.
[L1177] [44:04.88] Uh that was sort of what I wanted to do
[L1178] [44:07.20] on this incredibly complex and gnarly
[L1179] [44:08.88] codebase. As a fun fact, my favorite
[L1180] [44:11.20] intern uh made his title entropy. Um but
[L1181] [44:14.24] we were really on the same side. Uh I
[L1182] [44:17.36] think by the time we were shipping
[L1183] [44:19.36] Firefox Quantum, Mozilla had developed I
[L1184] [44:22.48] would say a more industry standard um uh
[L1185] [44:26.16] career progression. And so, you know,
[L1186] [44:28.08] you had you come in as, you know, just
[L1187] [44:31.04] title of engineer and then you've got
[L1188] [44:32.64] senior staff, senior staff. At the time
[L1189] [44:36.72] when I was working on quantum CSS, uh I
[L1190] [44:40.80] believe I was um my I had reached the
[L1191] [44:44.00] level of senior staff and upon the
[L1192] [44:46.96] successful launch of Firefox Quantum, I
[L1193] [44:50.96] and the engineer who led the other half
[L1194] [44:53.44] of Quantum Quantum Flow uh were promoted
[L1195] [44:56.80] to the level of principal engineer. Um
[L1196] [44:58.96] and at the time that was there were not
[L1197] [45:00.96] very many principal engineers, you know,
[L1198] [45:02.56] like probably fewer than five. Um, and
[L1199] [45:05.84] so that was um, a pretty significant
[L1200] [45:09.68] jump, but my long-term
[L1201] [45:12.40] dream was to be like Boris Sabarski. And
[L1202] [45:14.80] Boris Sabarski was one of Mozilla's
[L1203] [45:16.72] three distinguished engineers. And so
[L1204] [45:18.80] that was really what I had my sights on
[L1205] [45:20.96] in terms of the level of impact that I
[L1206] [45:22.56] wanted to have. And the way that I
[L1207] [45:27.36] really aimed at having this impact was
[L1208] [45:30.40] by trying to contribute to as many parts
[L1209] [45:33.76] of the code as possible and just be
[L1210] [45:37.04] prolific. And so after um working on
[L1211] [45:40.32] quantum CSS, I went and worked on web
[L1212] [45:43.28] render and I worked on mobile and
[L1213] [45:44.80] multipprocess and layout and all sorts
[L1214] [45:47.68] of different parts of the
[L1215] [45:50.96] uh of the code. And I remember my
[L1216] [45:54.24] manager at the time, Joe Hilderbrand,
[L1217] [45:55.76] who ran engineering, told me that he
[L1218] [45:58.56] wanted me to spend one day a week when I
[L1219] [46:02.56] didn't open my terminal. And I was just
[L1220] [46:04.80] shocked. I was like, what? What are you
[L1221] [46:06.96] what are you asking me to do here,
[L1222] [46:08.32] right? You're asking me to not work for
[L1223] [46:09.76] an entire day. And he was encouraging me
[L1224] [46:12.88] to start thinking about it in the impact
[L1225] [46:15.44] that I could have in a much broader way
[L1226] [46:17.44] as opposed to direct contributions to
[L1227] [46:19.28] the code. And so this was something that
[L1228] [46:21.12] I started to think about, but it was
[L1229] [46:23.04] really not the natural way that I
[L1230] [46:26.08] thought to work.
[L1231] [46:27.36] >> When you talk about the individual
[L1232] [46:29.12] contributions, because you mentioned
[L1233] [46:30.88] that was your way of having a lot of
[L1234] [46:32.96] impact. Do you have a way of thinking
[L1235] [46:35.28] about which contributions are more
[L1236] [46:37.44] impactful than others?
[L1237] [46:39.20] >> I was very much motivated to work on
[L1238] [46:41.76] whatever felt like the biggest problem.
[L1239] [46:44.24] And so that was early on that felt like
[L1240] [46:46.80] the DOM bindings and XP connect and all
[L1241] [46:48.80] the security stuff. And then at some
[L1242] [46:51.36] point it was the media playback to solve
[L1243] [46:52.96] the YouTube problem. And then it was
[L1244] [46:55.20] multipprocess. And then it was this uh
[L1245] [46:58.32] rest and servo CSS stuff. And after that
[L1246] [47:01.68] I thought that web render which was the
[L1247] [47:03.92] new graphics back end that we were
[L1248] [47:05.44] uplifting from uh servo. So I went and
[L1249] [47:08.56] worked on that. Then mobile. So I was
[L1250] [47:11.44] always drawn, I think, to what felt like
[L1251] [47:14.16] the most pressing problem. And my model
[L1252] [47:18.40] of how to have impact on that was to
[L1253] [47:20.96] jump in and learn all of the code in the
[L1254] [47:22.88] most pressing problem and help work on
[L1255] [47:25.84] it. And not just necessarily typing all
[L1256] [47:27.76] of the code myself, but working with the
[L1257] [47:29.84] other leaders in those areas on figuring
[L1258] [47:32.64] out what the right things to do would be
[L1259] [47:35.68] and reviewing code and setting direction
[L1260] [47:37.60] and setting priorities. So there were
[L1261] [47:39.76] aspects of leadership, but it was all
[L1262] [47:41.28] very much oriented around the code that
[L1263] [47:43.28] needed the most help.
[L1264] [47:44.80] >> So you were prolific, but it was a
[L1265] [47:47.44] guided search specifically on the
[L1266] [47:50.32] biggest problems for the organization.
[L1267] [47:52.56] >> That was how I thought about it. Yes.
[L1268] [47:54.88] >> One thing that I'm curious about because
[L1269] [47:56.32] in the industry when it comes to career
[L1270] [47:58.64] growth, I often hear two methodologies.
[L1271] [48:02.72] One is where people they focus on the
[L1272] [48:06.00] promo first and foremost. And as a
[L1273] [48:08.72] byproduct to get the promo they you know
[L1274] [48:11.76] grow in level or skills and various
[L1275] [48:14.08] other things behaviors and in the other
[L1276] [48:17.76] school of thought it's ignore the promos
[L1277] [48:20.56] but focus on the behaviors focus on the
[L1278] [48:23.28] skills and then the promos will come.
[L1279] [48:26.16] I'm curious your thought between the two
[L1280] [48:28.56] methodologies and which one you think is
[L1281] [48:30.40] better for structuring an engineering
[L1282] [48:32.16] career.
[L1283] [48:34.00] >> I have pretty strong opinions about
[L1284] [48:35.44] this. I am very much of the mind that it
[L1285] [48:38.88] is important to focus on impact and not
[L1286] [48:42.08] the title and I think there are a number
[L1287] [48:44.80] of reasons for this but that is
[L1288] [48:47.52] certainly what I look for now that I'm
[L1289] [48:49.76] in a situation when I am helping people
[L1290] [48:51.52] with their careers and I am often in the
[L1291] [48:53.92] decision of you know figuring out you
[L1292] [48:56.88] know who's the right person to advance
[L1293] [48:59.68] and what I am looking for is I am
[L1294] [49:02.88] looking for the impact And my general
[L1295] [49:06.64] philosophy is that if you are having
[L1296] [49:08.08] that level of impact, you don't need to
[L1297] [49:12.64] sell yourself in that way. Um or sell
[L1298] [49:16.00] yourself is not quite the right word,
[L1299] [49:17.60] but there is a particular philosophy
[L1300] [49:19.68] where you want to promo hack, right? You
[L1301] [49:21.52] want to pin your management chain down
[L1302] [49:23.76] on what are the things that I need to do
[L1303] [49:26.16] to receive this promotion. And
[L1304] [49:30.72] that just speaking frankly is very
[L1305] [49:33.20] annoying, right? Um there are aspects to
[L1306] [49:36.24] this that I think are just intuitive to
[L1307] [49:38.72] how I at least as a person perceive
[L1308] [49:40.32] things. You know like I'm a father of
[L1309] [49:41.76] kids and when my daughter asks me like
[L1310] [49:46.48] when you know I ask her to do something
[L1311] [49:48.00] and she's like uh you know will you give
[L1312] [49:49.68] me this if I do that right it's it just
[L1313] [49:52.40] does not um land well with me. But I
[L1314] [49:55.20] think that there's also a substantive
[L1315] [49:56.64] aspect to it which is that if you are
[L1316] [49:59.20] really focused on the impact that is how
[L1317] [50:01.92] you are really going to achieve things
[L1318] [50:03.52] right whereas if you're focused on
[L1319] [50:04.80] checking some boxes that somebody has
[L1320] [50:06.72] presented to you then you're in this
[L1321] [50:08.40] awkward situation where it's like well I
[L1322] [50:09.92] did technically say that if you did this
[L1323] [50:13.36] you know that would maybe make a case
[L1324] [50:14.88] for this next level but the way in which
[L1325] [50:17.60] you did it and was very sort of focused
[L1326] [50:20.08] on checking the box as opposed to having
[L1327] [50:21.52] the impact and at the end of the day
[L1328] [50:23.12] impact is what matters and impact which
[L1329] [50:24.56] is what needs to be recognized and
[L1330] [50:26.40] rewarded.
[L1331] [50:27.36] >> One thing that I hear often because I
[L1332] [50:29.36] think this is a failure mode for
[L1333] [50:32.24] engineers that are a little more
[L1334] [50:33.92] softspoken is they're great at writing
[L1335] [50:36.88] code and landing it and having impact,
[L1336] [50:40.16] but they're a little weaker on the, you
[L1337] [50:43.44] know, selling yourself or kind of
[L1338] [50:45.12] marketing your work. And so that kind of
[L1339] [50:47.60] bites people. So sometimes I hear career
[L1340] [50:51.28] advice that is focused on, you know,
[L1341] [50:54.08] hey, make sure you create a brag
[L1342] [50:56.80] document and you share the wins when you
[L1343] [51:00.16] land the thing. And and I think a lot of
[L1344] [51:02.48] those people don't have an ulterior
[L1345] [51:04.32] motive of let me, you know, kind of
[L1346] [51:08.48] connive my way into the promo. Um, but I
[L1347] [51:11.84] think there is this this real thing of
[L1348] [51:14.24] promos are decided by people and there's
[L1349] [51:18.08] some value in I guess a balance because
[L1350] [51:21.44] obviously if you were completely
[L1351] [51:23.76] conniving you say hey I'm going to talk
[L1352] [51:25.84] to my manager and sell my work to him.
[L1353] [51:28.72] That's kind of not ideal. But you know
[L1354] [51:31.12] making posts or sharing it and thinking
[L1355] [51:33.12] about the levels and stuff seems to be a
[L1356] [51:36.64] good way for those um little quieter or
[L1357] [51:40.48] less proactive engineers and structuring
[L1358] [51:42.56] their career. So you know how would you
[L1359] [51:44.72] kind of balance those two frames of
[L1360] [51:46.80] thinking? I think there are often
[L1361] [51:48.64] multiple ways to frame similar
[L1362] [51:51.52] activities,
[L1363] [51:53.04] but that the framing of how you think
[L1364] [51:55.28] about it is going to have a big impact
[L1365] [51:59.20] on how you carry it out and therefore
[L1366] [52:02.08] what it actually achieves. And so I
[L1367] [52:04.24] think a good example of this is this
