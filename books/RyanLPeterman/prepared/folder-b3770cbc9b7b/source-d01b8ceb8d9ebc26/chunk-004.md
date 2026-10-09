Chunk 4; segments 1218–1638. Start may repeat the previous chunk for context.

# MIT Professor: Leetcode, P vs NP, SAT Solvers | Ryan Williams

Source ID: source-d01b8ceb8d9ebc26
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/MIT_Professor_Leetcode,_P_vs_NP,_SAT_Solvers_Ryan_Williams_en.txt
Video: https://www.youtube.com/watch?v=AaK1SL2i_4Y

[L1227] [45:40.16] means yes, sat means no.
[L1228] [45:42.64] So, the NX thing guesses those things
[L1229] [45:44.96] which are no.
[L1230] [45:46.16] The no things it can answer, right? If
[L1231] [45:48.28] it's a sat thing, it can just guess the
[L1232] [45:50.40] answer to each of the nos.
[L1233] [45:53.36] Okay?
[L1234] [45:54.44] So, it guesses the answer to each of the
[L1235] [45:56.36] nos. It verifies all those answers, and
[L1236] [45:59.40] then it checks that the number of things
[L1237] [46:01.64] it guessed is what the birdie told it.
[L1238] [46:04.88] Once it's done that, all the no's have
[L1239] [46:08.12] been covered, so everything else must be
[L1240] [46:10.88] a yes.
[L1241] [46:12.36] So that so so it can actually prove a
[L1242] [46:14.88] yes by just exhaustively finding all the
[L1243] [46:18.24] no's and ruling out any other no's.
[L1244] [46:21.72] >> But the big question in my mind is where
[L1245] [46:23.92] do you get the little birdie?
[L1246] [46:24.84] >> Where do you get the little birdie
[L1247] [46:25.68] advice from? Yeah, yeah. So
[L1248] [46:27.84] yeah, so this I studied yeah, this um
[L1249] [46:31.52] what the little birdie gives you
[L1250] [46:33.76] and it seems to me that it it is
[L1251] [46:36.56] possible that this little birdie itself
[L1252] [46:39.96] can be constructed in NX.
[L1253] [46:42.64] And if so, then we'd just be done. Like
[L1254] [46:45.20] in NX, you figure out what the little
[L1255] [46:47.28] birdie would tell you and then use that
[L1256] [46:49.72] to just flip the answer. So it guess
[L1257] [46:53.04] Let's sort of guess all the things which
[L1258] [46:55.00] are no, so what remains must be a yes
[L1259] [46:57.12] and
[L1260] [46:58.64] we talked a lot about time
[L1261] [47:00.00] >> complexity. And you mentioned a little
[L1262] [47:01.96] bit this advice I guess kind of space
[L1263] [47:03.56] complexity. And I know you had a major
[L1264] [47:06.12] result relating space and time
[L1265] [47:08.76] complexity. You're basically simulating
[L1266] [47:11.40] time complexity with space complexity,
[L1267] [47:13.84] but lower than it's been done prior.
[L1268] [47:17.12] Could you explain
[L1269] [47:19.12] what it was before your breakthrough
[L1270] [47:21.32] result and then maybe the intuition
[L1271] [47:23.40] behind your breakthrough result?
[L1272] [47:25.32] >> Uh in general, the problem is the
[L1273] [47:27.56] following. I give you
[L1274] [47:29.92] an algorithm that runs in time T
[L1275] [47:33.16] and I want to know
[L1276] [47:35.64] um is there another algorithm that uses
[L1277] [47:38.24] space much less than T? Uses amount of
[L1278] [47:41.64] memory like you know, units of memory
[L1279] [47:43.60] much less
[L1280] [47:44.92] than T
[L1281] [47:46.36] and still solve the problem completely.
[L1282] [47:48.72] Still completely simulates the thing
[L1283] [47:50.60] perfectly.
[L1284] [47:52.00] Um
[L1285] [47:53.56] one intuition for why you
[L1286] [47:56.76] might think um
[L1287] [47:58.84] this
[L1288] [47:59.68] question just
[L1289] [48:01.04] can't be solved or some problems there's
[L1290] [48:02.28] just no
[L1291] [48:03.64] way to improve on the spaces if you
[L1292] [48:05.96] think of like
[L1293] [48:07.60] the pro like a lot of problems in
[L1294] [48:09.16] dynamic programming like let's say I
[L1295] [48:11.88] have
[L1296] [48:13.56] um
[L1297] [48:14.36] some logic circuit that I want to
[L1298] [48:16.32] evaluate and all of the gates are
[L1299] [48:18.92] provided to me in a row and all the
[L1300] [48:22.20] wires sort of flow from left to right.
[L1301] [48:25.32] And the you know I start with
[L1302] [48:26.36] information on the left.
[L1303] [48:28.56] I want to compute the information on the
[L1304] [48:31.04] far right.
[L1305] [48:32.44] And all the you know all the bits are
[L1306] [48:33.92] flowing left to right by wires.
[L1307] [48:36.64] The natural way to evaluate such a
[L1308] [48:38.84] circuit is you start with say the inputs
[L1309] [48:40.60] on the left.
[L1310] [48:41.92] For each gate in turn in the the line
[L1311] [48:45.68] you look at its inputs. Its inputs have
[L1312] [48:47.76] been determined if there's some bits.
[L1313] [48:50.04] You use that to compute the value of
[L1314] [48:51.96] that gate. You pass the values of that
[L1315] [48:55.12] of you know the output of that gate
[L1316] [48:56.48] forward.
[L1317] [48:57.40] Okay?
[L1318] [48:58.60] But if
[L1319] [48:59.80] that uh circuit you know has
[L1320] [49:02.88] T gates in it you know it will take
[L1321] [49:04.60] about T time to solve but it will
[L1322] [49:06.72] definitely also take about T space in
[L1323] [49:08.88] general.
[L1324] [49:10.00] All right? Like the circuit could be
[L1325] [49:11.60] wired up in some wild way and there just
[L1326] [49:14.28] might not be a way to save uh space for
[L1327] [49:16.96] an arbitrary uh circuit.
[L1328] [49:19.44] But already in 1975
[L1329] [49:25.24] people were studying this kind of of
[L1330] [49:27.08] question and finding counterintuitive
[L1331] [49:29.76] answers to it.
[L1332] [49:31.28] So
[L1333] [49:31.96] um Hopcroft, Paul, and Valiant uh based
[L1334] [49:35.20] on work of Patterson and Valiant
[L1335] [49:38.24] uh showed that
[L1336] [49:41.00] time T algorithms at least in this
[L1337] [49:43.84] so-called multi-tape Turing machine uh
[L1338] [49:46.24] model very powerful model uh can be
[L1339] [49:49.28] simulated in space T divided by log of
[L1340] [49:52.80] T. So I mean it's like a like you you
[L1341] [49:56.08] get some space savings but it's only
[L1342] [49:57.84] like a log T factor. Okay.
[L1343] [50:00.52] Um
[L1344] [50:01.92] and
[L1345] [50:03.20] the way this is done is is quite
[L1346] [50:06.80] counterintuitive. Uh it was I mean like
[L1347] [50:10.00] even though there's a only a log factor
[L1348] [50:12.12] there it was
[L1349] [50:13.20] uh
[L1350] [50:13.84] pretty shocking.
[L1351] [50:15.76] That development was
[L1352] [50:18.16] extended to random access models of
[L1353] [50:20.76] computation
[L1354] [50:22.24] um later
[L1355] [50:24.08] and and in more general models of
[L1356] [50:26.84] computation. So like in in the late '70s
[L1357] [50:29.44] and early '80s.
[L1358] [50:30.84] Um
[L1359] [50:32.08] so so it was known for like a pretty
[L1360] [50:35.40] much any reasonable model of computation
[L1361] [50:37.28] that time T can be simulated in space
[L1362] [50:40.12] about T over log T.
[L1363] [50:42.28] But there was a hidden maybe not so
[L1364] [50:45.00] hidden um gotcha in the space efficient
[L1365] [50:48.68] simulation. It needs
[L1366] [50:51.12] an exponential amount of time
[L1367] [50:53.20] to run. So like you there's a time space
[L1368] [50:55.56] trade-off. Okay, if you really want to
[L1369] [50:57.20] save some space you got to blow up the
[L1370] [50:59.44] time by a lot.
[L1371] [51:02.04] Nevertheless
[L1372] [51:03.48] um yeah, it was kind of commonly
[L1373] [51:06.12] conjectured that
[L1374] [51:08.60] this T over log T space was about the
[L1375] [51:11.96] best you could do and you
[L1376] [51:14.16] and that you were probably not going to
[L1377] [51:16.24] get T to the 0.9
[L1378] [51:19.68] space or you know something something
[L1379] [51:22.28] much more efficient. Um
[L1380] [51:25.36] so yeah, it was a big surprise to me uh
[L1381] [51:29.84] like that you can actually put time T in
[L1382] [51:33.08] space about square root
[L1383] [51:35.64] of T.
[L1384] [51:36.80] Again, there's an exponential
[L1385] [51:38.92] running time just to you know give the
[L1386] [51:41.20] full caveat out there.
[L1387] [51:43.28] But
[L1388] [51:44.52] um
[L1389] [51:45.28] but it's still very surprising. Like
[L1390] [51:47.16] this holds for
[L1391] [51:48.88] any kind of time T
[L1392] [51:51.16] uh algorithm. Like, including something
[L1393] [51:52.48] that might be outputting, you know,
[L1394] [51:54.56] something pseudo random, some you know,
[L1395] [51:57.40] something from cryptography,
[L1396] [51:59.60] you know, like it's not at all obvious
[L1397] [52:01.80] that every such process could be
[L1398] [52:04.28] compressed
[L1399] [52:05.76] to only be need like square root of T
[L1400] [52:09.04] uh space and still get the job done,
[L1401] [52:10.76] still compute whatever function was
[L1402] [52:12.96] being computed.
[L1403] [52:14.12] >> I mean, I know it's probably super
[L1404] [52:15.48] involved, but if you could just a high
[L1405] [52:17.64] level, what's the trick? How'd you do
[L1406] [52:19.16] it?
[L1407] [52:19.48] >> Well, the trick for me was to read
[L1408] [52:23.00] um James Cook and Ian Mertz's paper on
[L1409] [52:26.20] tree evaluation very, very carefully.
[L1410] [52:28.40] That
[L1411] [52:29.36] I mean, and just knowing um the P the
[L1412] [52:33.84] landscape around P versus P space and
[L1413] [52:35.84] knowing what Hopcroft, Paul, and Valiant
[L1414] [52:38.36] did. Um
[L1415] [52:41.12] Yeah, so but I I can give you a very
[L1416] [52:43.52] high-level idea of
[L1417] [52:46.32] kind of what's going on and how what
[L1418] [52:49.68] they did uh is useful.
[L1419] [52:52.44] So,
[L1420] [52:54.04] Hopcroft, Paul, and Valiant, the way
[L1421] [52:55.64] they were modeling
[L1422] [52:57.48] uh space-bounded computation was in a
[L1423] [52:59.96] particular way that seemed pretty
[L1424] [53:01.60] general uh at the time, but turned out
[L1425] [53:05.12] to be restrictive
[L1426] [53:07.20] uh
[L1427] [53:08.32] in ways that we just didn't anticipate.
[L1428] [53:10.48] So, the way they thought of it was
[L1429] [53:14.52] um I'm going to take like certain I'm
[L1430] [53:17.28] going to break the computation up into
[L1431] [53:18.52] little pieces
[L1432] [53:20.16] and I'm going to
[L1433] [53:23.80] like write I'm going to write pieces of
[L1434] [53:27.52] the computation like little bits into
[L1435] [53:29.56] the memory, but I'm only going to do
[L1436] [53:31.20] that over blank space. I mean, this is
[L1437] [53:33.64] something that sounds natural, right?
[L1438] [53:35.00] Like, so like I'm going to erase pieces
[L1439] [53:38.48] of memory and then I'm going to
[L1440] [53:40.20] overwrite that blank space with a piece
[L1441] [53:42.92] of memory. So, I'm being very
[L1442] [53:44.32] destructive in a certain sense. Like but
[L1443] [53:47.04] this is a natural thing you do, right?
[L1444] [53:48.68] Like if you want to replace you know,
[L1445] [53:50.76] swap something with something else,
[L1446] [53:53.52] you often just erase. But there are ways
[L1447] [53:57.00] to swap
[L1448] [53:58.56] without uh erasing, right? So, there's
[L1449] [54:01.68] like a common
[L1450] [54:03.24] little trick that is taught in uh CS
[L1451] [54:06.04] courses.
[L1452] [54:07.12] So, like if you
[L1453] [54:08.72] um if you require everything to be
[L1454] [54:11.44] written into a blank uh
[L1455] [54:14.04] register,
[L1456] [54:15.36] then if you want to swap the contents of
[L1457] [54:17.68] two variables like X and Y,
[L1458] [54:20.16] then you've
[L1459] [54:21.32] you've got to have a temporary register.
[L1460] [54:23.12] Like you move one into the temp, you
[L1461] [54:25.12] erase it, you move Y into the
[L1462] [54:27.52] into there and then so on, right?
[L1463] [54:29.72] But if you don't want a temp, you can
[L1464] [54:33.04] achieve the same thing uh with just
[L1465] [54:36.56] XORing the the registers bitwise. Or if
[L1466] [54:39.88] you've got numbers, you can add and
[L1467] [54:41.36] subtract, okay? In three instructions,
[L1468] [54:44.92] clever instructions, adding,
[L1469] [54:46.36] subtracting, or XORing,
[L1470] [54:48.44] you can actually swap the contents of
[L1471] [54:50.48] two registers without needing a third.
[L1472] [54:53.92] Okay? This is kind of the starting point
[L1473] [54:56.12] for thinking about like, well, why does
[L1474] [54:57.96] it matter
[L1475] [54:59.48] if you're always writing into erased
[L1476] [55:02.40] memory?
[L1477] [55:03.60] So,
[L1478] [55:04.56] so what
[L1479] [55:05.80] uh
[L1480] [55:06.44] James Cook and Ian Mertz showed
[L1481] [55:09.68] uh at a very high level was
[L1482] [55:12.08] they they were studying a certain
[L1483] [55:14.44] problem
[L1484] [55:15.88] called tree evaluation, whatever that
[L1485] [55:18.00] is,
[L1486] [55:18.92] and they were the problem had an
[L1487] [55:21.36] algorithm where you're all you had a
[L1488] [55:24.32] little stack
[L1489] [55:25.68] and you're always sort of like
[L1490] [55:29.20] um you know,
[L1491] [55:30.52] popping and and uh pushing on the stack,
[L1492] [55:33.52] but you were always, you know, writing
[L1493] [55:36.32] uh
[L1494] [55:37.80] writing computation contents into erase
[L1495] [55:41.72] memory, okay? What they realized was
[L1496] [55:44.28] that if you allow computations to XOR
[L1497] [55:48.44] bits of memory into existing memory,
[L1498] [55:51.12] then you can save a lot of space.
[L1499] [55:53.56] So, if you're really, really careful
[L1500] [55:56.48] about how you XOR things, you can
[L1501] [55:59.40] basically recover uh you like what's in
[L1502] [56:03.00] your memory without storing all of it at
[L1503] [56:05.24] once. You sort of offload things to
[L1504] [56:07.44] computation,
[L1505] [56:09.00] and you XOR on top of things very, very
[L1506] [56:11.76] cleverly. You can get like nice
[L1507] [56:13.52] cancellations of things you don't want,
[L1508] [56:16.20] and and keep around things you do want.
[L1509] [56:18.92] Yeah, so
[L1510] [56:20.36] I mean, that is a high-level uh idea of
[L1511] [56:23.56] how this stuff works. And then going to
[L1512] [56:25.60] square root, is it just an extension of
[L1513] [56:27.80] that, or is it a completely different?
[L1514] [56:29.48] So, the the way it works with square
[L1515] [56:30.92] root, a square root just happens to be
[L1516] [56:32.52] kind of like the optimal trade-off
[L1517] [56:35.48] in this uh tree evaluation business. So,
[L1518] [56:39.24] so
[L1519] [56:40.80] um what you do is you break the
[L1520] [56:42.32] computation into square root of T time
[L1521] [56:45.60] intervals,
[L1522] [56:46.84] and each time interval has about square
[L1523] [56:48.44] root of T
[L1524] [56:49.76] um steps in it.
[L1525] [56:52.48] And then what you do is you you give a a
[L1526] [56:54.52] particular way of simulating this thing,
[L1527] [56:58.96] so that you're only kind of holding
[L1528] [57:01.36] about a constant number
[L1529] [57:04.00] of blocks or like of these time
[L1530] [57:06.28] intervals in memory at any point in
[L1531] [57:08.24] time.
[L1532] [57:09.20] Like you're only holding a small number
[L1533] [57:11.60] of these
[L1534] [57:13.08] uh
[L1535] [57:13.68] time intervals, like a records of time
[L1536] [57:15.92] intervals in memory at any any point in
[L1537] [57:18.28] time.
[L1538] [57:19.24] Which is entirely not obvious how you
[L1539] [57:21.64] would do it. But but it's some sort of
[L1540] [57:23.96] like it's some sort of sweet spot to set
[L1541] [57:26.32] the square root of T. It's a way to It's
[L1542] [57:27.84] like the
[L1543] [57:28.76] the minimum setting of like trade-off.
[L1544] [57:31.00] Like say I have like
[L1545] [57:32.68] I want to break the computational
[L1546] [57:34.16] intervals, and the intervals have a
[L1547] [57:36.44] certain number of steps. If I If I set
[L1548] [57:38.32] it to be square root of T, then the
[L1549] [57:39.92] number of intervals and the number of
[L1550] [57:41.64] steps in each interval is about the
[L1551] [57:43.36] same.
[L1552] [57:44.64] >> So, I mean, that was a long-held result.
[L1553] [57:47.28] I mean, you you mentioned it was 1975.
[L1554] [57:49.72] That's maybe Yeah, almost 50 years where
[L1555] [57:52.88] if you come up with something like that
[L1556] [57:54.44] and you you I guess you're writing it
[L1557] [57:56.32] out, you're thinking through, and then
[L1558] [57:58.04] you see it. What is that moment like?
[L1559] [58:00.60] >> So, I you know, I'm I've been around
[L1560] [58:02.68] long enough to have been deceived by
[L1561] [58:05.36] myself many many many many times.
[L1562] [58:09.16] So,
[L1563] [58:10.36] yeah, I guess the the first two or three
[L1564] [58:12.72] times I thought about this,
[L1565] [58:16.32] um
[L1566] [58:17.08] I just thought this is another one of
[L1567] [58:18.60] those ideas that can't possibly work.
[L1568] [58:21.80] There's no way. There's just no way this
[L1569] [58:23.36] works.
[L1570] [58:24.28] Um
[L1571] [58:26.08] so, I would just kind of leave it
[L1572] [58:28.72] and then come back to it sometimes when
[L1573] [58:30.40] I was
[L1574] [58:32.20] bored of whatever else I was working on.
[L1575] [58:34.32] Um
[L1576] [58:35.36] like I I It was a pretty slow process of
[L1577] [58:38.44] convincing myself that this could
[L1578] [58:40.40] possibly be true. Like, I
[L1579] [58:42.80] I thought there was
[L1580] [58:45.16] either a bug in what
[L1581] [58:49.08] James and Ian
[L1582] [58:50.72] was doing somewhere,
[L1583] [58:52.92] or there was a bug in
[L1584] [58:55.52] my interpretation of what's happening.
[L1585] [58:58.36] Um I thought
[L1586] [59:00.16] there had to be a mistake for a long
[L1587] [59:02.32] time.
[L1588] [59:03.60] And the only way I got over that was
[L1589] [59:05.52] just
[L1590] [59:06.64] writing it down
[L1591] [59:08.64] uh over and over and over in different
[L1592] [59:10.80] ways, sort of writing and rewriting and
[L1593] [59:13.04] writing and rewriting and adding more
[L1594] [59:14.68] detail,
[L1595] [59:15.96] and then maybe finding a different way
[L1596] [59:17.40] of explaining it and it erasing and, you
[L1597] [59:20.64] know, writing something shorter,
[L1598] [59:22.48] and just sort of re-explaining it to
[L1599] [59:24.04] myself over and over and over.
[L1600] [59:27.00] And even then, like when I submitted it
[L1601] [59:28.80] to the
[L1602] [59:29.92] um stock conference where it was where
[L1603] [59:32.64] it appeared, um I wasn't entirely
[L1604] [59:36.04] confident that it was correct. I was
[L1605] [59:38.20] just exhausted from like thinking about
[L1606] [59:40.72] it for so long and just thought that
[L1607] [59:42.44] maybe someone else will find the mistake
[L1608] [59:44.32] for me. Like I'm Like I Like I At this
[L1609] [59:46.56] point, like
[L1610] [59:47.84] I I was just like desperate. Like I had
[L1611] [59:50.12] actually sent it
[L1612] [59:51.72] to two
[L1613] [59:53.20] colleagues that I trust,
[L1614] [59:55.44] you know, privately and asked them,
[L1615] [59:58.48] "Can you help me find the mistake?" Or
[L1616] [01:00:01.24] whatever. "Can you help me understand
[L1617] [01:00:02.76] this?" And one of them just said, like
[L1618] [01:00:05.76] they Basically, they just didn't read
[L1619] [01:00:07.60] past the abstract. They're like, "I'm
[L1620] [01:00:09.52] not I'm sorry. I'm not going to
[L1621] [01:00:12.92] I'm like they just didn't believe it,
[L1622] [01:00:14.40] period. Just like me. I mean, they
[L1623] [01:00:15.92] didn't believe it.
[L1624] [01:00:17.24] And
[L1625] [01:00:18.68] uh another one said,
[L1626] [01:00:21.60] after a long time, "Well,
[L1627] [01:00:24.80] I didn't quite
[L1628] [01:00:26.52] um
[L1629] [01:00:27.08] follow it, but
[L1630] [01:00:28.64] there was a footnote that you put
[L1631] [01:00:31.56] like in in the bottom of some page.
[L1632] [01:00:34.04] After that after that footnote,
[L1633] [01:00:36.68] then I began to believe it."
[L1634] [01:00:39.52] So then what I did was I just took that
[L1635] [01:00:41.00] footnote and elaborated it in in like a
[L1636] [01:00:43.80] later revision, sort of made it the what
[L1637] [01:00:45.64] I called the warm-up. I'm going to
[L1638] [01:00:47.28] because I was like, yeah, I I've got to
[L1639] [01:00:49.28] do I've got to write this thing in a way
[L1640] [01:00:52.36] that is airtight so that other people
[L1641] [01:00:54.28] will actually believe believe this
[L1642] [01:00:56.68] because
[L1643] [01:00:58.08] yeah, I it took me a long time to get
[L1644] [01:01:00.56] used to it, to believe it. Yeah.
[L1645] [01:01:02.04] >> Wow. Uh what What motivates you to solve
[L1646] [01:01:06.00] these
[L1647] [01:01:07.04] hard problems? I mean, what keeps you
