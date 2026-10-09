Chunk 4; segments 1052–1399. Start may repeat the previous chunk for context.

# How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar

Source ID: source-cfa80c9b2999d9de
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/How_Anthropic_Builds_And_How_Engineering_Will_Change_Soon_Thariq_Shihipar_en.txt
Video: https://www.youtube.com/watch?v=2Kch3tWMnw8

[L1061] [36:16.24] uh let's say you're not a designer.
[L1062] [36:18.16] There's probably Step one is being like,
[L1063] [36:20.68] okay, now I'm not a designer. There's a
[L1064] [36:22.48] lot I don't know about design, you know?
[L1065] [36:25.64] And like there's was lot I don't know
[L1066] [36:26.84] about iteration. I don't even know what
[L1067] [36:29.04] good looks like, right? And I think this
[L1068] [36:30.64] is like part of the art of working with
[L1069] [36:33.36] a designer is like they will just know
[L1070] [36:35.20] what good looks like and they'll be like
[L1071] [36:36.60] this isn't good enough in this way,
[L1072] [36:38.32] right? And they like prompt it. And that
[L1073] [36:40.68] I think is also a skill that will keep
[L1074] [36:42.28] getting valuable and even more valuable
[L1075] [36:45.00] over time is just like what is good
[L1076] [36:47.28] output? What is worth doing, right? Like
[L1077] [36:49.00] I think uh for example with the uh the
[L1078] [36:51.64] Riemann hypothesis, Jared prompted it,
[L1079] [36:54.00] but he had no idea if it was correct
[L1080] [36:56.24] until like Lev who's like, you know,
[L1081] [36:59.16] one of the world's best mathematicians
[L1082] [37:01.32] who was like, you know, okay, like how
[L1083] [37:02.68] do I
[L1084] [37:04.16] is this correct, right? And he worked
[L1085] [37:06.64] with it and he asked it like tons of
[L1086] [37:08.56] follow-up questions.
[L1087] [37:10.36] And we could not follow that at all. We
[L1088] [37:12.28] had no idea what he was saying, right?
[L1089] [37:14.28] But he was like really intrigued. And
[L1090] [37:16.00] and so I think
[L1091] [37:17.12] more and more being that like high-cased
[L1092] [37:19.12] user and like knowing a lot about a
[L1093] [37:21.36] problem in a domain space is how you get
[L1094] [37:23.44] good outputs, right? That's how you
[L1095] [37:25.68] these problems. Uh
[L1096] [37:27.24] otherwise like maybe Claude did solve
[L1097] [37:29.32] like physics or something and but you
[L1098] [37:30.72] just wouldn't know it, right? Like
[L1099] [37:31.76] you're like
[L1100] [37:32.72] uh
[L1101] [37:33.44] you you don't know enough about it. And
[L1102] [37:35.16] so I think when you're talking about
[L1103] [37:37.16] design, the first thing you do is like
[L1104] [37:38.68] how do you become more tasteful with
[L1105] [37:40.20] design, right? And so you can ask Claude
[L1106] [37:42.96] that as well, right? Like you can be
[L1107] [37:44.28] like, "Hey, I'm not a designer. I want
[L1108] [37:46.08] to be better at design. I don't even
[L1109] [37:47.68] have the language. First maybe let's
[L1110] [37:49.52] find some reference sites." And that and
[L1111] [37:51.08] then maybe you pull some reference sites
[L1112] [37:52.64] and then you're like, "This is what I
[L1113] [37:53.88] like or this is what I don't like,
[L1114] [37:55.32] right?" And then you
[L1115] [37:57.16] sort of build up that, you know, those
[L1116] [37:59.44] references and you give Claude it. And
[L1117] [38:01.44] and now maybe you tell it, "Hey, let's
[L1118] [38:03.04] do some exploration. This is sort of my
[L1119] [38:05.04] taste." And then it'll do like a few
[L1120] [38:07.36] different mock-ups, right? And I like to
[L1121] [38:09.36] do these mock-ups all in HTML because
[L1122] [38:10.96] it's all self-contained, easy to edit.
[L1123] [38:13.28] And then once you have that
[L1124] [38:15.48] you know, that reference, now it's a
[L1125] [38:17.56] reference. So now you can be like you
[L1126] [38:19.36] can make a new session and be like,
[L1127] [38:20.64] "Hey, this is a mock-up of a design I
[L1128] [38:22.88] want. Uh start implementing this and,
[L1129] [38:25.76] you know, it will have all of it in code
[L1130] [38:27.68] and you can start getting there." Um but
[L1131] [38:30.12] I think that like the really hard part
[L1132] [38:32.48] is just knowing like, "Oh, when is
[L1133] [38:34.16] something good enough?" You know, uh
[L1134] [38:35.72] versus like when can you, you know, push
[L1135] [38:38.64] harder, right? And you see this with a
[L1136] [38:40.12] lot of the math proofs, too, right? Or
[L1137] [38:41.72] and when like Terence Tao is like,
[L1138] [38:43.48] "Okay, enough with the half-complete
[L1139] [38:45.56] theorems. Just do the full theorem." You
[L1140] [38:47.84] know, and and so I think like it sounds
[L1141] [38:50.28] simple, but it takes a lot of domain
[L1142] [38:52.32] knowledge and expertise to get to the
[L1143] [38:54.60] point to be like, "Okay, like you it
[L1144] [38:56.88] seems like you're smart enough to have
[L1145] [38:58.40] done that. Now do this."
[L1146] [39:00.60] >> When I was a software engineer,
[L1147] [39:03.04] there was a lot of um
[L1148] [39:05.28] I guess it was like glue writing work
[L1149] [39:07.40] kind of where you you finish some work
[L1150] [39:09.84] and you write a launch post or
[L1151] [39:12.44] you are part of some work stream and you
[L1152] [39:14.92] got to post an update every 2 to 4 weeks
[L1153] [39:18.44] or maybe you have a direction doc or
[L1154] [39:21.48] design doc and all this like writing
[L1155] [39:24.44] around the software uh that you actually
[L1156] [39:27.36] write.
[L1157] [39:28.48] And curious your thoughts on if that's
[L1158] [39:31.44] changed at all at Anthropic, how much of
[L1159] [39:34.68] that is written by LLMs and how much of
[L1160] [39:37.24] that is, you know, human-written still.
[L1161] [39:40.28] >> Mhm. My rule of thumb is like if I would
[L1162] [39:42.56] be happy to show someone the prompt, I
[L1163] [39:45.68] would send them the output, right? And
[L1164] [39:47.28] so uh a lot of times the prompt is just
[L1165] [39:51.04] collecting context is the most common
[L1166] [39:52.92] one, right? So, for example, uh before
[L1167] [39:55.88] every one-on-one with my manager, I ask
[L1168] [39:57.88] Claude to, you know, read every Slack
[L1169] [40:00.72] message and GitHub message and, you
[L1170] [40:02.92] know, a
[L1171] [40:03.68] PR and compile like, you know, a report
[L1172] [40:07.48] of what I did, right? And uh that's
[L1173] [40:10.16] context that my manager doesn't have
[L1174] [40:11.72] because, you know, they haven't been
[L1175] [40:13.56] literally reading every PR or something.
[L1176] [40:15.84] And so I don't feel bad if like, you
[L1177] [40:17.92] know,
[L1178] [40:18.80] like my manager could also run this
[L1179] [40:21.08] command, but it doesn't have my context.
[L1180] [40:23.12] And I don't feel bad with them knowing
[L1181] [40:24.88] that this is the prompt I used to
[L1182] [40:26.76] generate this command, right? So,
[L1183] [40:29.24] um I think likewise, like if you're
[L1184] [40:31.16] sharing updates or something like that,
[L1185] [40:33.48] you know, like uh you might want to
[L1186] [40:36.12] prove that you've read it. You know, I
[L1187] [40:38.32] think this is important. And And
[L1188] [40:39.80] sometimes like little edits are ways of
[L1189] [40:42.08] proving that you have also understood
[L1190] [40:44.04] this work, right? And so, if it's just
[L1191] [40:46.12] like a data readout, you know, maybe
[L1192] [40:48.12] you're you're sanity checking like the
[L1193] [40:51.04] numbers make sense and this like these
[L1194] [40:53.00] are all the numbers you intended to
[L1195] [40:54.20] include. And as part of that, maybe you
[L1196] [40:56.20] format it differently or you add like a
[L1197] [40:58.12] little sentence in on your behalf,
[L1198] [41:00.08] right? And but I think ultimately, it's
[L1199] [41:02.12] a data readout.
[L1200] [41:03.68] Everyone knows the prompt you wrote is
[L1201] [41:05.48] like, "Hey, like generate a readout on
[L1202] [41:07.80] this feature based on this." And And
[L1203] [41:09.68] you're fine, right? But like, I think if
[L1204] [41:11.60] you're pitching like a new concept or
[L1205] [41:13.36] new idea and your prompt is like, "Help
[L1206] [41:15.24] me come up with a new concept for, you
[L1207] [41:17.52] know, this product, right?" Like, you
[L1208] [41:19.72] probably at least
[L1209] [41:22.20] people want you to know that want to
[L1210] [41:23.92] know that you've like believed in it,
[L1211] [41:25.60] right? And so, like even if you think
[L1212] [41:27.36] Claude's idea is incredible and just
[L1213] [41:29.56] verbatim you wouldn't change anything,
[L1214] [41:31.08] what I would say is like, I'd be like,
[L1215] [41:32.32] "Hey, Claude generated this. Um but I
[L1216] [41:34.84] think it's great. You know, like I or
[L1217] [41:37.00] I've did like a hundred different
[L1218] [41:38.32] generations and I think this was really
[L1219] [41:39.84] good. And here is like something, you
[L1220] [41:42.24] know, that I want to send you, right?"
[L1221] [41:44.75] >> [snorts]
[L1222] [41:44.88] >> Um and so, I think that like it's good
[L1223] [41:47.76] to be upfront about it, I think, right?
[L1224] [41:49.84] Because I do think what people don't
[L1225] [41:51.76] like is when they feel like they've been
[L1226] [41:53.24] like misled a little bit. Like, "Oh,
[L1227] [41:54.80] like you We thought we you were doing
[L1228] [41:57.52] this work, but, you know,
[L1229] [42:00.00] um it it's really Claude, right?" And I
[L1230] [42:02.08] think that like um
[L1231] [42:04.60] writing sometimes can have a lot of like
[L1232] [42:06.88] there's some parts of writing where
[L1233] [42:08.80] individual words matter. You know, like
[L1234] [42:11.00] funnily like tweets are I of a good
[L1235] [42:12.36] example of this where like the
[L1236] [42:13.80] individual tweet matters, right? So,
[L1237] [42:16.16] um
[L1238] [42:17.08] you like more and more you can't use
[L1239] [42:19.20] Claude to do that because it's like like
[L1240] [42:21.96] every word has some thought that you've
[L1241] [42:23.92] put into it and some intention that
[L1242] [42:25.36] you've put into it. So, like, you know,
[L1243] [42:27.00] yeah, a pitch or an essay or something
[L1244] [42:29.20] like that. We do a lot of like internal
[L1245] [42:30.76] essays at Anthropic being like, "Hey,
[L1246] [42:32.36] this is why I think we should do this."
[L1247] [42:34.08] And that's generally like all
[L1248] [42:35.60] human-written. It's very like looked
[L1249] [42:38.84] down upon, I think, to have like Claude
[L1250] [42:41.28] like your essay written by Claude, you
[L1251] [42:42.72] know what I mean? Um because like every
[L1252] [42:44.84] word is something that you like are
[L1253] [42:47.00] intentional about.
[L1254] [42:48.92] >> So, it sounds like the proportion
[L1255] [42:51.16] of the writing that's all that boring
[L1256] [42:54.24] route writing, like the data readouts,
[L1257] [42:56.44] the
[L1258] [42:57.48] the one-on-one updates, the work stream
[L1259] [42:59.24] updates, that's increasingly becoming
[L1260] [43:01.88] AI, but always reviewed by human. And
[L1261] [43:04.72] then the novel thoughts, novel
[L1262] [43:07.32] direction, is still very human-written.
[L1263] [43:10.28] And And feels like it should remain that
[L1264] [43:12.64] way even if the models were a little bit
[L1265] [43:15.12] better, too.
[L1266] [43:16.60] >> Yeah, I think it's like if you're, you
[L1267] [43:18.84] know, it's a like writing is also way of
[L1268] [43:21.24] thinking, right? And so like maybe if
[L1269] [43:22.68] you need to think about the data stream
[L1270] [43:24.64] or data readout more, then maybe you
[L1271] [43:26.24] need to like summarize it, you know? And
[L1272] [43:27.96] And so,
[L1273] [43:29.04] um but yeah, I I I think like especially
[L1274] [43:30.64] gathering context is one of those things
[L1275] [43:32.44] where no one will ever like hold it
[L1276] [43:34.44] against you, kind of, right? Like uh
[L1277] [43:36.96] oh, like, you know, you did a bunch of
[L1278] [43:39.00] research and, you know, Claude did this,
[L1279] [43:41.16] but yeah, like I don't want to ask my
[L1280] [43:42.76] agent to do the same research. Like, you
[L1281] [43:44.52] know, it's a shortcut, but like just
[L1282] [43:46.52] acknowledging it is good.
[L1283] [43:48.76] >> Someone I also was talking to, they had
[L1284] [43:51.08] this thought of it would be valuable to
[L1285] [43:54.92] have almost like a git blame, but it's
[L1286] [43:57.68] like like a prompt blame of
[L1287] [44:00.56] cuz it would be nice to reverse look up
[L1288] [44:03.28] what was the prompt that generated this
[L1289] [44:05.00] change to kind of debug things. Do you
[L1290] [44:07.44] have any sort of meta version control on
[L1291] [44:11.08] the prompts that generated the software
[L1292] [44:12.96] or is it still very vanilla, you know,
[L1293] [44:15.80] get history?
[L1294] [44:17.68] >> Yeah, that is a little bit tough because
[L1295] [44:19.72] again like, you know, what goes into a
[L1296] [44:21.52] prompt is not just the prompt but also
[L1297] [44:24.08] the context and skills and things like
[L1298] [44:25.76] that. So like maybe, you know, a prompt
[L1299] [44:28.00] might seem basic but isn't. Uh I think
[L1300] [44:31.76] I it's kind of hard to judge. But I do,
[L1301] [44:34.48] you know, like going back to like when
[L1302] [44:36.56] I'm giving a PR, I don't think a PR at
[L1303] [44:38.60] this point is any different than an
[L1304] [44:40.24] artifact or something. Like Claude is
[L1305] [44:41.92] doing basically all the code writing,
[L1306] [44:44.16] right? So if I send someone a PR, I
[L1307] [44:46.08] usually also attach an artifact of every
[L1308] [44:49.92] prompt I sent to Claude,
[L1309] [44:52.00] um including failed like approaches and
[L1310] [44:54.68] things like that, you know?
[L1311] [44:56.28] Um so that they can see like, okay, I've
[L1312] [44:58.56] considered a lot of other things, you
[L1313] [45:00.84] know? And if I haven't, if this is just
[L1314] [45:02.48] a one-shot, I just tell people. I'm
[L1315] [45:04.28] like, "Hey, this is the one-shot
[L1316] [45:06.08] example. This is the prompt I used,
[L1317] [45:07.80] right?" Um
[L1318] [45:09.40] and uh I think that's like usually
[L1319] [45:12.40] impressive and interesting to them as
[L1320] [45:13.84] well because they're like, "Oh, like
[L1321] [45:14.96] it's cool that Claude could one-shot
[L1322] [45:16.36] this." Um but the worst is when you get
[L1323] [45:20.20] like
[L1324] [45:21.24] you know, you you just I'm just trying
[L1325] [45:22.44] to avoid cases where I send in like this
[L1326] [45:24.36] 10,000 line PR and they're like, "Did
[L1327] [45:27.48] you like how much have you like read
[L1328] [45:29.68] this or like, you know, like how much
[L1329] [45:30.96] did you work with Claude on it?" And if
[L1330] [45:33.04] I'm doing like a large PR, I am going to
[L1331] [45:35.08] like show my work as much as possible.
[L1332] [45:39.00] >> On maintaining code because AI can
[L1333] [45:42.08] generate such high volumes of code at
[L1334] [45:45.00] this point, do you have any tips on
[L1335] [45:47.64] what's worked well at Anthropic for code
[L1336] [45:49.84] ownership and maintenance?
[L1337] [45:52.20] >> I do think you have to revisit
[L1338] [45:54.28] like what is important with code
[L1339] [45:56.28] maintenance, right? And so I think that
[L1340] [45:57.84] like there are some things where like
[L1341] [45:59.76] naming used to be really important,
[L1342] [46:02.04] right? Because like it was like how you
[L1343] [46:04.04] as a team thought about this like
[L1344] [46:05.68] abstraction and feature. Um but I think
[L1345] [46:08.48] naming is becoming less and less
[L1346] [46:09.96] important. A lot of stylistic things in
[L1347] [46:12.12] code are becoming less and less
[L1348] [46:13.48] important, you know? And I think that
[L1349] [46:15.56] like this is not the same to me as
[L1350] [46:18.32] maintenance, right? So I think that like
[L1351] [46:21.04] um
[L1352] [46:22.36] if you you might want to sit down and be
[L1353] [46:24.32] like, okay, like what things really
[L1354] [46:26.16] matter now, what don't, what opinions do
[L1355] [46:28.08] we have that don't matter. So that's
[L1356] [46:30.28] one. And then I think on the second on
[L1357] [46:32.12] the maintenance side is sort of like
[L1358] [46:34.04] having good scaffolding, right? So I
[L1359] [46:37.32] think that it's like uh having a good
[L1360] [46:39.72] verification harness, having a good like
[L1361] [46:43.20] uh sort of skills. We use the simplify
[L1362] [46:45.48] skill a lot. I think that like you know,
[L1363] [46:47.92] sometimes even from model perspective,
[L1364] [46:49.96] like it might do a lot of work. And then
[L1365] [46:51.76] like even just giving it permission to
[L1366] [46:53.12] be like, "Hey, I think this is the right
[L1367] [46:55.52] uh idea. Let's simplify it." gives it
[L1368] [46:58.68] that permission to do it, right? But
[L1369] [47:00.00] like you actually don't want a model to
[L1370] [47:02.32] by default do work and then simplify,
[L1371] [47:05.92] right? Because uh maybe it's not
[L1372] [47:07.84] correct, right? Like you don't want it
[L1373] [47:09.28] to simplify work that's not correct.
[L1374] [47:10.76] It's like um you're wasting tokens,
[L1375] [47:13.24] right? And so I think this is also how
[L1376] [47:15.04] humans think, right? They're like you
[L1377] [47:17.28] know, you think generatively, you try an
[L1378] [47:19.08] approach, and then maybe you like
[L1379] [47:20.44] simplify and abstract a little. Um so I
[L1380] [47:23.56] think there's like some work inside your
[L1381] [47:25.68] own code base or like setting up the
[L1382] [47:27.64] skills and that those practices where
[L1383] [47:29.80] you like you know, you're not just
[L1384] [47:31.24] submitting
[L1385] [47:32.84] like the first take, but you've like
[L1386] [47:34.20] simplified it and tried it. Um and then
[L1387] [47:37.36] like yeah, having a really good
[L1388] [47:38.44] verification harness where you feel like
[L1389] [47:40.80] you're catching you know, like you have
[L1390] [47:43.40] a good
[L1391] [47:44.60] belief that Claude is like testing every
[L1392] [47:46.84] part of it.
[L1393] [47:48.20] Uh like you know, when you submit a PR
[L1394] [47:50.00] to Claude code, you get a recording back
[L1395] [47:52.20] of it using the feature and testing it
[L1396] [47:54.00] as an example, right? Um and you can
[L1397] [47:57.04] just get really, really creative with
[L1398] [47:58.88] different ways to like
[L1399] [48:00.80] uh, test stuff. Like I think you should
[L1400] [48:02.32] basically have
[L1401] [48:03.72] on the order of I'd say more like a
[L1402] [48:05.52] hundred times more testing code than
[L1403] [48:07.92] you've ever had before. You know what I
[L1404] [48:09.36] mean? So like,
[L1405] [48:10.88] uh,
[L1406] [48:11.48] you should have
[L1407] [48:12.72] uh, fixtures for everything. You can
[L1408] [48:14.04] just pull production code and create
