Chunk 4; segments 1171–1572. Start may repeat the previous chunk for context.

# Google DeepMind Distinguished Eng (L9): How To Land a Job at a Frontier Lab | Vlad Feinberg

Source ID: source-3cd3328907a7fa93
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Google_DeepMind_Distinguished_Eng_(L9)_How_To_Land_a_Job_at_a_Frontier_Lab_Vlad_Feinberg_en.txt
Video: https://www.youtube.com/watch?v=cDyi91onoJ8

[L1180] [44:53.28] uh or simply they might be a
[L1181] [44:56.08] mathematical operations that
[L1182] [44:59.20] the underlying hardware performs more
[L1183] [45:02.00] slowly than they uh than uh it might
[L1184] [45:05.16] perform a matmul.
[L1185] [45:06.49] >> [snorts]
[L1186] [45:06.52] >> And so, all of those things contribute
[L1187] [45:08.48] to not running at the full speed that
[L1188] [45:12.36] the processor is rated at.
[L1189] [45:14.80] Uh and so, that's why you might not see
[L1190] [45:16.44] 100% MFU all the time is cuz,
[L1191] [45:19.00] you know, part of the time your neural
[L1192] [45:20.16] net was, you know, reading and writing
[L1193] [45:21.68] to memory or part of the time it was
[L1194] [45:24.08] doing an operation that uh you know,
[L1195] [45:26.72] fundamentally runs slower than certain
[L1196] [45:29.08] other units on your
[L1197] [45:31.56] on your device. And
[L1198] [45:34.40] I think quite a bit of this inference
[L1199] [45:36.64] co-design work that I talked about
[L1200] [45:38.12] earlier is
[L1201] [45:39.76] across all of the different
[L1202] [45:42.36] um
[L1203] [45:43.32] capabilities of the chip. So, uh
[L1204] [45:45.48] communication to other chips,
[L1205] [45:47.96] um memory bandwidth, the the speed at
[L1206] [45:49.68] which we can read parameters from
[L1207] [45:51.40] memory,
[L1208] [45:53.76] flops, of course. Uh
[L1209] [45:55.84] this can be matmul flops. This can be
[L1210] [45:58.52] flops for processing uh
[L1211] [46:01.24] vectors. So, like things like doing
[L1212] [46:02.88] activations.
[L1213] [46:04.16] Uh all of these have different rates in
[L1214] [46:06.52] the hardware.
[L1215] [46:07.64] And a given computation isn't going to
[L1216] [46:09.68] match the natural hardware's rate
[L1217] [46:13.48] uh of each of those operations. So, when
[L1218] [46:17.04] you design a neural net, you want to be
[L1219] [46:19.60] able to choose shapes for this neural
[L1220] [46:21.96] net that fully saturate all of those
[L1221] [46:25.48] hardware units to get you as high of an
[L1222] [46:27.36] MFU as possible
[L1223] [46:29.24] um when you are doing uh inference here.
[L1224] [46:32.60] What makes this
[L1225] [46:34.56] more than just an algebra problem is
[L1226] [46:37.00] that those choices translate to
[L1227] [46:39.52] different quality outcomes when you
[L1228] [46:41.24] actually train this neural net.
[L1229] [46:43.44] So, the process of this kind of
[L1230] [46:45.24] inference co-design is how do we come up
[L1231] [46:49.24] with neural architectures that
[L1232] [46:51.92] scale predictably
[L1233] [46:54.16] have a good prediction, so are high
[L1234] [46:55.80] quality
[L1235] [46:57.04] and still
[L1236] [46:58.64] make the MFU as large as possible during
[L1237] [47:00.56] inference. And so, this kind of joint
[L1238] [47:02.88] optimization is what makes inference
[L1239] [47:05.08] co-design really fun.
[L1240] [47:07.00] Uh and also this kind of evergreen
[L1241] [47:08.36] problem because as the hardware changes
[L1242] [47:11.44] all of those relative constants of flops
[L1243] [47:14.16] to memory bandwidth to communication
[L1244] [47:16.44] bandwidth change and those will have
[L1245] [47:18.44] different implications to what's the
[L1246] [47:21.00] optimal neural net shape should be.
[L1247] [47:23.20] >> On another topic
[L1248] [47:25.24] Google has this idea of a spot bonus
[L1249] [47:27.80] where someone can kind of give you uh a
[L1250] [47:30.24] one-off
[L1251] [47:31.72] lump sum of money as a thank you for
[L1252] [47:34.40] like good performance. And I I saw on
[L1253] [47:36.72] your resume that Jeff Dean, the legend
[L1254] [47:39.28] himself, gave you a spot bonus. And you
[L1255] [47:41.72] know, if you can tell that story, I'd
[L1256] [47:43.00] love to hear why did he give you a spot
[L1257] [47:44.96] bonus?
[L1258] [47:46.08] >> Yeah, so that one actually was at the
[L1259] [47:48.20] very beginning of the Gemini program.
[L1260] [47:53.16] Uh he gave out a spot bonus to people
[L1261] [47:54.88] who
[L1262] [47:55.92] hopped on and launched the first version
[L1263] [47:58.44] of Bard. And like I had a you know a
[L1264] [48:01.48] very small contribution to a very very
[L1265] [48:03.44] large project at the time.
[L1266] [48:05.76] Uh I helped with uh SFT for
[L1267] [48:08.44] uh one of the first versions uh of
[L1268] [48:11.32] uh supervised fine-tuning for one of the
[L1269] [48:12.88] first versions of uh
[L1270] [48:14.64] Bard that got released like right, you
[L1271] [48:16.80] know.
[L1272] [48:17.80] The biggest lesson
[L1273] [48:19.76] out of
[L1274] [48:20.76] uh that experience was
[L1275] [48:23.08] you know, at that time
[L1276] [48:25.44] I was just doing like pure research in
[L1277] [48:28.68] um uh Google Brain.
[L1278] [48:30.48] And I was super focused on just how do I
[L1279] [48:33.52] maximize the number of first author
[L1280] [48:35.04] papers at uh NeurIPS, ICML, ICLR. And
[L1281] [48:41.28] I remember distinctly thinking like I I
[L1282] [48:44.20] had this instinct of like oh like, you
[L1283] [48:47.08] know, should I just keep my head down
[L1284] [48:48.92] and try to write more papers? And
[L1285] [48:51.32] Luckily at the time uh my my manager
[L1286] [48:54.68] Rohan Aneja, like he really encouraged
[L1287] [48:56.96] all of us to get involved in
[L1288] [49:00.20] uh you know, this space.
[L1289] [49:02.28] And
[L1290] [49:03.96] that was just the right motivation that
[L1291] [49:06.36] I needed to like roll up sleeves, do a
[L1292] [49:09.08] bunch of hyperparameter tuning and
[L1293] [49:11.48] engineering work to get uh this uh model
[L1294] [49:15.00] running on uh uh some like really old
[L1295] [49:18.36] TPUs to get some extra you know, cycles
[L1296] [49:21.72] in for for
[L1297] [49:23.24] uh SFT attempts.
[L1298] [49:25.40] That very small initial engagement that
[L1299] [49:27.88] was recognized by Jeff Dean, I I think
[L1300] [49:30.40] blossomed into more and more investments
[L1301] [49:33.48] on the LLM side by me and
[L1302] [49:36.16] ultimately led me to where I am today.
[L1303] [49:39.40] Uh so
[L1304] [49:40.60] yeah, I would say
[L1305] [49:42.04] you know, it it's less so about you
[L1306] [49:44.20] know, [snorts]
[L1307] [49:45.04] you know, how much that like SFT helped
[L1308] [49:47.40] the initial release and it's much more
[L1309] [49:48.96] about uh
[L1310] [49:50.48] uh recognizing that like
[L1311] [49:53.52] there's there's quite a bit of work,
[L1312] [49:55.44] some of it not glamorous, some of it
[L1313] [49:56.92] just like, you know, hyperparameter
[L1314] [49:58.20] tuning and,
[L1315] [49:59.68] uh, golfing the XLA compiler to make
[L1316] [50:02.68] your program fit in a certain memory
[L1317] [50:04.60] amount
[L1318] [50:05.88] that contributes to a wider business
[L1319] [50:07.76] goal that
[L1320] [50:08.92] is is really quite important for
[L1321] [50:11.56] getting involved in in very high-value
[L1322] [50:13.80] projects.
[L1323] [50:14.96] >> You've been working on Gemini for a
[L1324] [50:16.44] while now, and because it's a top
[L1325] [50:18.08] priority, there has to be some, you
[L1326] [50:21.00] know, incidents or war stories that
[L1327] [50:23.12] you've been involved in. So, I'm
[L1328] [50:24.80] curious, you know, what's your favorite,
[L1329] [50:27.68] uh, war story when working on Gemini?
[L1330] [50:30.80] >> So, I think my all-time favorite
[L1331] [50:33.56] would have to be
[L1332] [50:36.96] Flash 2.0.
[L1333] [50:39.52] Uh, so this one this one was quite a
[L1334] [50:42.36] challenge and a very long journey to get
[L1335] [50:44.36] there.
[L1336] [50:45.80] But,
[L1337] [50:47.28] uh, one of the
[L1338] [50:49.04] main things that we were optimizing for,
[L1339] [50:51.92] which which Flash 1.5 established, is
[L1340] [50:54.36] this category of very fast, low-latency
[L1341] [50:57.60] model
[L1342] [50:59.08] that's still
[L1343] [51:00.40] quite good. Um, and, you know,
[L1344] [51:04.04] in particular, it has to be fast because
[L1345] [51:06.44] it's it's used by search to serve,
[L1346] [51:09.04] uh,
[L1347] [51:09.72] responses in in AI mode, uh, very
[L1348] [51:11.96] quickly.
[L1349] [51:14.16] Because of that,
[L1350] [51:16.24] uh, for Flash 1.5 and before, we we
[L1351] [51:18.48] focused on dense models, which, uh,
[L1352] [51:21.24] allow you to respond very quickly.
[L1353] [51:25.16] Even though at the time we we knew about
[L1354] [51:26.68] MoE models and how they increase
[L1355] [51:28.12] capacity.
[L1356] [51:29.44] And so, I think, um,
[L1357] [51:32.40] one thing that like came up was, okay,
[L1358] [51:35.72] like
[L1359] [51:37.04] we sure would like to use this new
[L1360] [51:38.44] architecture, but it it's difficult to
[L1361] [51:41.36] just simply switch to an MoE because
[L1362] [51:44.08] what happens with an MoE is it it uses a
[L1363] [51:45.88] lot more parameters in general
[L1364] [51:48.40] and because it uses more parameters, it
[L1365] [51:50.16] takes up more HBM.
[L1366] [51:52.68] These chips that we serve on have a
[L1367] [51:54.68] finite amount of HBM, so you have to
[L1368] [51:56.56] shard the MOE across
[L1369] [51:59.76] multiple different chips. So, if you
[L1370] [52:01.52] have, you know, whatever NX birds then
[L1371] [52:04.56] you might chart it across N chips or,
[L1372] [52:06.40] you know, some factor of N.
[L1373] [52:08.64] And what this causes is a lot of
[L1374] [52:11.80] communication in the middle of the
[L1375] [52:13.80] model. When you have a token that needs
[L1376] [52:17.16] to be routed to an expert and that token
[L1377] [52:19.84] might live on the first TPU, but it
[L1378] [52:21.36] needs to go to the last TPU, that's a
[L1379] [52:23.36] lot of communication that you're
[L1380] [52:24.60] inducing in the forward pass. So, the
[L1381] [52:27.56] latency of this operation
[L1382] [52:31.48] like increases dramatically with N.
[L1383] [52:35.04] And
[L1384] [52:36.16] you know, the challenge with MOEs is
[L1385] [52:37.44] they increase N. So,
[L1386] [52:39.68] that that that like kind of really
[L1387] [52:41.76] bottleneck this approach.
[L1388] [52:44.68] And one interesting thing that happened
[L1389] [52:47.44] was we we definitely knew about pipeline
[L1390] [52:51.60] serving for a while.
[L1391] [52:53.96] It's just in the dense case
[L1392] [52:55.96] it never really ended up mattering. Like
[L1393] [52:58.08] I distinctly remember a very early
[L1394] [52:59.76] conversation I had with Sholto about it
[L1395] [53:01.64] and Sholto's like, "Oh yeah, you're like
[L1396] [53:03.64] so flop bound and so pipelining is just
[L1397] [53:06.20] not going to change your prefill
[L1398] [53:07.12] profile." And then he was right. I
[L1399] [53:08.68] tested it out and like then abandoned
[L1400] [53:10.36] the idea.
[L1401] [53:12.20] But what's interesting is
[L1402] [53:15.48] I I had a very small team at the time
[L1403] [53:17.28] and and one of my reports, Gangyan,
[L1404] [53:20.48] had a very nice idea. He was working
[L1405] [53:22.24] with Rahul Arya and a couple folks from
[L1406] [53:25.16] the Israel team at Google.
[L1407] [53:27.16] And that was to apply pipeline prefill
[L1408] [53:29.24] to MOEs.
[L1409] [53:31.44] And pipelining is
[L1410] [53:35.04] a technique where instead of
[L1411] [53:36.76] parallelizing
[L1412] [53:38.28] those N machines experts across those N
[L1413] [53:40.64] machines, you parallel layers across
[L1414] [53:43.68] those end machines. So, instead of on a
[L1415] [53:46.64] particular layer, you have to route
[L1416] [53:48.24] tokens from machine to machine, now one
[L1417] [53:51.24] layer does the computation for one
[L1418] [53:53.92] subset of your pre-fill request, and
[L1419] [53:56.32] then hands off the processed tokens to
[L1420] [53:59.72] the next machine to process the second
[L1421] [54:01.88] layer, and then the third layer, and the
[L1422] [54:03.12] fourth layer.
[L1423] [54:04.28] And
[L1424] [54:06.12] all of the experts can then stay
[L1425] [54:08.00] resident to a single machine or a
[L1426] [54:09.56] smaller set of machines. So,
[L1427] [54:12.64] what this does effectively is it changes
[L1428] [54:15.64] the communication pattern from something
[L1429] [54:17.72] that required a lot of token exchange on
[L1430] [54:20.96] every single layer to
[L1431] [54:23.68] something that's
[L1432] [54:25.68] actually can be hidden behind other
[L1433] [54:28.16] computation because you can do this
[L1434] [54:31.16] pipeline pre-fill across different parts
[L1435] [54:33.32] of your request.
[L1436] [54:35.00] So,
[L1437] [54:36.16] while layer two is working on the
[L1438] [54:38.84] first thousand tokens of your request,
[L1439] [54:41.44] layer one on the first chip is
[L1440] [54:43.88] processing
[L1441] [54:45.24] the second thousand tokens of your
[L1442] [54:46.80] request. So, it was a way of
[L1443] [54:50.48] breaking this HBM constraint by moving
[L1444] [54:53.92] layers across the machines rather than
[L1445] [54:55.84] moving experts across these machines.
[L1446] [54:58.04] And because of that, the communication
[L1447] [55:00.40] overhead has gone down, and all of a
[L1448] [55:02.52] sudden, MoE latency looks really
[L1449] [55:04.80] attractive now. This, you know, the the
[L1450] [55:07.76] Gemini 2.0 report says like it's an MoE
[L1451] [55:10.60] series of models, and the thing that
[L1452] [55:12.80] made that possible is, you know, or one
[L1453] [55:14.68] of the things that made that possible is
[L1454] [55:16.12] is this
[L1455] [55:18.08] you know, serving time innovation.
[L1456] [55:21.44] Dwarak and Reiner have an amazing post
[L1457] [55:23.44] about exactly this
[L1458] [55:26.40] optimization that you can write up in
[L1459] [55:29.20] the algebra of the scaling book. And
[L1460] [55:31.08] it's just a wonderful example of how
[L1461] [55:33.92] this kind of
[L1462] [55:35.88] change can
[L1463] [55:38.04] uh have really dramatic implications on
[L1464] [55:40.48] LLM quality. What really made Flash 2.0
[L1465] [55:43.44] rewarding is
[L1466] [55:45.16] this, you know, giant MoE decision. It
[L1467] [55:48.16] sounds like a small technical decision
[L1468] [55:49.80] at the time, but
[L1469] [55:51.20] people were really worried about whether
[L1470] [55:53.24] or not the latency of this MoE would
[L1471] [55:55.88] actually be reasonable. Luckily,
[L1472] [55:58.56] I was able to run like a very
[L1473] [55:59.92] transparent technical process to get to
[L1474] [56:01.96] the bottom of this. And by the end of
[L1475] [56:04.24] it, uh uh uh you know, we we made the
[L1476] [56:06.84] right call, uh but then we had to train
[L1477] [56:08.72] it. So,
[L1478] [56:10.92] this was a bigger model than we've ever
[L1479] [56:14.20] trained before at the flash scale, and
[L1480] [56:16.80] like we knew this would be the right
[L1481] [56:18.12] call, but it was just going to be 40
[L1482] [56:20.32] days of grueling work for like a really,
[L1483] [56:22.80] really small team. Like we probably had
[L1484] [56:24.48] like five people on the rotation for
[L1485] [56:28.04] training this model. I remember, you
[L1486] [56:30.56] know, all of us just kind of like
[L1487] [56:32.64] rotated day by day, handing off like,
[L1488] [56:36.00] you know,
[L1489] [56:37.32] all of this like SRE style work of uh
[L1490] [56:40.92] keeping the training job alive, which at
[L1491] [56:43.00] the time was was
[L1492] [56:44.96] a very interactive thing cuz uh you had
[L1493] [56:47.64] to make sure that everything was moving
[L1494] [56:49.16] stably, that, you know, you have tuned
[L1495] [56:51.28] data iterators that aren't slowing down
[L1496] [56:53.76] your job, that, you know, if there's
[L1497] [56:56.36] like a gap in the data somewhere or an
[L1498] [56:58.88] indexing issue, you have to like really
[L1499] [57:01.00] quickly put up a fix because it's, you
[L1500] [57:03.00] know, wasting all of this GPU time. Um
[L1501] [57:05.72] >> What about at night time and on the
[L1502] [57:07.32] weekends?
[L1503] [57:08.28] >> So, yeah, like I think, you know, for
[L1504] [57:10.64] those 40 days, we did not do a lot of
[L1505] [57:12.68] sleeping. Like we had to
[L1506] [57:15.16] like do like kind of these dual shifts
[L1507] [57:17.68] across like the Paris office and
[L1508] [57:19.40] Mountain View, and like the thing that
[L1509] [57:22.64] makes it so rewarding was when this
[L1510] [57:25.44] model came out, like around the same
[L1511] [57:27.68] time, uh DeepSeek V3 came out. And uh
[L1512] [57:32.12] the Wall Street Journal put out this
[L1513] [57:33.64] article that was like this giant red
[L1514] [57:35.52] scare article about how China's going to
[L1515] [57:37.28] take over AI with open source models and
[L1516] [57:41.36] I remember my friend sent me a
[L1517] [57:42.76] screenshot of this table of the LMSYS
[L1518] [57:46.52] Arena leaderboard. And you know, all the
[L1519] [57:49.40] way at the top right you've got
[L1520] [57:52.48] chat GPT and
[L1521] [57:54.80] and DeepSeek right behind it. And like,
[L1522] [57:57.20] oh, DeepSeek was trained for whatever
[L1523] [57:59.92] few million dollars, you know, and and
[L1524] [58:01.88] like they're right there.
[L1525] [58:03.44] And then my friend was like, oh, like
[L1526] [58:06.60] you know, Gemini is so behind cuz they
[L1527] [58:08.80] had, you know, a version of like I think
[L1528] [58:10.68] 1.5 Pro or something in that table at
[L1529] [58:13.24] the very bottom.
[L1530] [58:14.92] And then I looked at it and was like,
[L1531] [58:16.00] oh, that's really interesting. I was
[L1532] [58:17.36] just looking at this leaderboard cuz we
[L1533] [58:20.36] just released a model and it definitely
[L1534] [58:23.44] doesn't look like that when you go to
[L1535] [58:24.96] the website. So, turns out there was
[L1536] [58:28.32] kind of some ill-written rows on the
[L1537] [58:31.92] Wall Street Journal article. And so now
[L1538] [58:35.04] if you go to that article today, you can
[L1539] [58:37.28] see, you know, what at the time was the
[L1540] [58:40.56] state of the art model
[L1541] [58:42.92] you know, Flash 2.0 thinking
[L1542] [58:45.72] up in the top right corner way far ahead
[L1543] [58:47.96] of DeepSeek V3.
[L1544] [58:50.44] Might be messing with the open source
[L1545] [58:52.24] narrative that they were trying to
[L1546] [58:53.36] publish there, but it was a really
[L1547] [58:55.56] important accomplishment for for the
[L1548] [58:57.80] team.
[L1549] [58:59.36] >> Last question for you is if you could go
[L1550] [59:01.76] back to yourself when you just graduated
[L1551] [59:04.84] college, I guess undergrad, and give
[L1552] [59:07.08] yourself some advice knowing what you
[L1553] [59:08.64] know now, what would you say?
[L1554] [59:12.00] >> You you got to chase the problems that
[L1555] [59:16.60] people are facing
[L1556] [59:18.60] like
[L1557] [59:19.64] in the world today. Like like go after
[L1558] [59:23.12] the challenges that people see in
[L1559] [59:25.64] everyday life and don't be afraid to
[L1560] [59:31.56] tackle a smaller part of this problem or
[L1561] [59:34.12] maybe a more menial sounding part of
[L1562] [59:36.04] this problem, even if it's not fancy
[L1563] [59:38.32] research math or something like that.
[L1564] [59:40.12] Like, trust that by working on what's
[L1565] [59:43.24] important, even if it's a smaller part
[L1566] [59:46.16] of a larger project for what's
[L1567] [59:47.40] important, you're going to get to see
[L1568] [59:50.04] what really matters in terms of moving
[L1569] [59:52.36] the frontier forward.
[L1570] [59:53.96] And it's it's this kind of, I guess,
[L1571] [59:58.28] humility maybe in your
[L1572] [01:00:00.72] problem approach that that you should
[L1573] [01:00:03.32] really be chasing.
[L1574] [01:00:05.00] Um that's one piece of advice. I think
[L1575] [01:00:07.68] the other bit that I would give, like
[L1576] [01:00:10.20] maybe as professional advice, perhaps,
[L1577] [01:00:13.92] would be
[L1578] [01:00:16.36] be the kind of co-worker
[L1579] [01:00:19.20] that
[L1580] [01:00:20.72] people would want to see succeed.
[L1581] [01:00:24.84] Uh and so, like what I mean by that is
