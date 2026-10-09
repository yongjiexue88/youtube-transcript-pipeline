Chunk 4; segments 1211–1615. Start may repeat the previous chunk for context.

# Co-Creator of Haskell: Useless vs Useful Languages, Rust vs C, Functional Programming | Simon Jones

Source ID: source-3f6b5c7495d2c862
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Co-Creator_of_Haskell_Useless_vs_Useful_Languages,_Rust_vs_C,_Functional_Programming_Simon_Jones_en.txt
Video: https://www.youtube.com/watch?v=xcB_LF3cdqw

[L1220] [41:45.84] uh
[L1221] [41:46.56] so, it has type A to B to list of A to
[L1222] [41:48.32] list of B. If you were to apply an
[L1223] [41:50.24] IO-performing function, so it the
[L1224] [41:52.24] function you're applying has type like
[L1225] [41:53.80] int to IO of char
[L1226] [41:57.60] you could map that over a list, but you
[L1227] [41:58.92] just get a list of IO of chars.
[L1228] [42:01.40] That hasn't done any IO yet, right?
[L1229] [42:04.64] You want something that says, "Take a
[L1230] [42:06.52] list of IO chars and perform those
[L1231] [42:09.08] actions one at a time." So, I want a
[L1232] [42:10.32] function that goes type from type list
[L1233] [42:12.60] of IO char
[L1234] [42:14.12] to IO of list of char.
[L1235] [42:17.40] Right? And you might want to perform all
[L1236] [42:19.36] those actions
[L1237] [42:21.12] top to bottom, or maybe bottom to top.
[L1238] [42:23.16] Who knows? That's what this
[L1239] [42:25.52] function of type, you know, so yes, so
[L1240] [42:27.40] you could do it in various ways.
[L1241] [42:29.20] So, sometimes it gets in the way, right?
[L1242] [42:30.72] You say, "Oh, you know, can't I
[L1243] [42:32.16] just use map?"
[L1244] [42:33.87] >> [laughter]
[L1245] [42:34.48] >> Well, in Haskell, no, sorry.
[L1246] [42:36.92] You you're going to have to do a little
[L1247] [42:38.40] bit more work to tell me in what
[L1248] [42:39.92] sequence you want your effects to
[L1249] [42:41.28] happen.
[L1250] [42:43.40] Because by default, Haskell does not
[L1251] [42:45.52] specify sequence.
[L1252] [42:47.40] Um so,
[L1253] [42:49.00] the, you know, adding, uh, you know,
[L1254] [42:51.12] monads to control effects does get in
[L1255] [42:52.96] your face a bit.
[L1256] [42:54.36] And that's a that's the tax we pay. In
[L1257] [42:56.56] effect, that's part of the big
[L1258] [42:57.76] experiment that Haskell is doing is to
[L1259] [42:59.92] say, "Suppose we up front say we can
[L1260] [43:02.32] we're willing to pay that tax."
[L1261] [43:04.80] You know, how many followers can we get?
[L1262] [43:09.04] Uh, and the more but I'm I will note
[L1263] [43:12.00] that monads have infected quite a lot of
[L1264] [43:13.64] other languages, like F Sharp is
[L1265] [43:15.04] definitely a call by value impure
[L1266] [43:16.60] language, and yet F Sharp had these
[L1267] [43:18.32] workflows that were definitely monads,
[L1268] [43:20.08] right? Um,
[L1269] [43:21.44] and um,
[L1270] [43:22.52] monads have, you know, appeared in Scala
[L1271] [43:24.20] and in many other many other languages.
[L1272] [43:25.68] So, something that's very monad-like has
[L1273] [43:27.44] appeared lots elsewhere. It's been a
[L1274] [43:29.08] very unifying concept.
[L1275] [43:31.48] >> OpenAI, Anthropic, Cursor, and Vercel
[L1276] [43:35.24] all use this product to make their lives
[L1277] [43:37.00] better.
[L1278] [43:37.96] And the problem it solves is when you're
[L1279] [43:39.84] building SaaS or an ad product and you
[L1280] [43:42.48] want to sell to other companies, there's
[L1281] [43:44.36] all these requirements you need to meet.
[L1282] [43:46.52] There's SSL, there's SCIM, there's RBAC,
[L1283] [43:50.12] there's audit logs. These are all things
[L1284] [43:51.92] that take time to integrate, but aren't
[L1285] [43:54.08] the main focus of your app. WorkOS is an
[L1286] [43:56.40] API layer that lets you meet all of
[L1287] [43:58.08] these requirements in just a few lines
[L1288] [44:00.24] of code. So, let's say you have a new
[L1289] [44:02.32] SaaS product and you want to sell to
[L1290] [44:03.96] other companies, WorkOS will solve all
[L1291] [44:06.44] of these critical feature gaps for you.
[L1292] [44:09.12] You can check them out at workos.com to
[L1293] [44:11.68] learn more and get started. And I
[L1294] [44:13.84] appreciate them for supporting my work
[L1295] [44:15.72] and sponsoring this podcast.
[L1296] [44:17.52] >> When I read [snorts] about Haskell and
[L1297] [44:19.60] people's perception of Haskell, one
[L1298] [44:21.76] thing that keeps coming up is that the
[L1299] [44:24.12] type system is really powerful. And so,
[L1300] [44:27.12] I kind of want to ask you maybe just
[L1301] [44:30.16] even on the highest level, what is a
[L1302] [44:32.32] type system in your words?
[L1303] [44:35.28] >> Okay, so what does a type system do? It
[L1304] [44:37.88] lets you reject silly programs
[L1305] [44:41.04] up front.
[L1306] [44:43.52] So, if I have a function that adds one
[L1307] [44:46.96] to things
[L1308] [44:48.28] and I apply it to a character or to an
[L1309] [44:51.00] IO computation
[L1310] [44:54.36] I'd like to that's going to fail at run
[L1311] [44:56.40] time.
[L1312] [44:58.40] All right? Because I can't add one to a
[L1313] [44:59.64] character. Or maybe you overload plus,
[L1314] [45:01.60] maybe I maybe I reverse reverse a list
[L1315] [45:03.68] or something. If I give If I've got a
[L1316] [45:05.36] list reverse I give it to somebody that
[L1317] [45:06.84] just isn't a list
[L1318] [45:09.12] then it's a bit silly to allow that and
[L1319] [45:10.84] only fail at run time.
[L1320] [45:13.20] So, fundamentally
[L1321] [45:15.08] type systems are about rejecting at
[L1322] [45:17.36] compile time programs that you do not
[L1323] [45:20.00] want to run because they will fail
[L1324] [45:21.96] at run time.
[L1325] [45:23.76] Okay.
[L1326] [45:24.72] Now
[L1327] [45:26.32] um we've had static type systems for a
[L1328] [45:27.96] long time um like uh you know, uh going
[L1329] [45:31.24] back to Pascal um and and earlier uh but
[L1330] [45:35.52] simple type systems are annoying because
[L1331] [45:38.76] they get in the way.
[L1332] [45:40.08] Imagine a function that reverses a list.
[L1333] [45:42.96] In Pascal, you could write a function
[L1334] [45:44.72] that reverses a list of integers.
[L1335] [45:46.80] But if you wanted to reverse a list of
[L1336] [45:48.12] characters
[L1337] [45:49.52] sorry
[L1338] [45:52.08] you can't that that function that
[L1339] [45:53.84] reverses a list of integers it has type
[L1340] [45:56.20] list of int list of int. So, you can't
[L1341] [45:58.12] apply it to a list of characters.
[L1342] [46:00.88] Game over.
[L1343] [46:02.88] You have to write another copy of the
[L1344] [46:04.28] code with a different type.
[L1345] [46:06.72] That's a bit annoying.
[L1346] [46:08.52] So, what are we going to do? We need
[L1347] [46:10.80] polymorphism. We need a more powerful
[L1348] [46:13.04] type system.
[L1349] [46:14.28] We want to give reverse the type for all
[L1350] [46:16.56] A
[L1351] [46:17.52] list of A to list of A. So, that up
[L1352] [46:19.88] front says, I work for any type A.
[L1353] [46:23.36] You give me a list of integers, fine.
[L1354] [46:24.80] I'll produce a list of integers. You
[L1355] [46:25.88] give me a list of characters, fine. I'll
[L1356] [46:27.04] produce a list of characters.
[L1357] [46:29.72] Notice that's much better than just list
[L1358] [46:31.32] to list.
[L1359] [46:32.56] I want to keep the fact there's a list
[L1360] [46:33.84] of integers, so I know if I apply, you
[L1361] [46:36.32] know, when I look inside of this, I know
[L1362] [46:38.00] I've got an integer.
[L1363] [46:39.28] Um but also, if I just list to list, I
[L1364] [46:41.16] might get back a a list of some
[L1365] [46:42.40] completely different type, but I know
[L1366] [46:43.60] that reverse returns a list with the
[L1367] [46:45.60] same type of things.
[L1368] [46:47.60] Right?
[L1369] [46:48.28] So, parametric polymorphism, super
[L1370] [46:50.64] valuable.
[L1371] [46:52.52] Right? If you want a static type system,
[L1372] [46:54.44] you must have parametric polymorphism.
[L1373] [46:57.36] The message is,
[L1374] [46:59.64] if your type system is too simple, it
[L1375] [47:01.76] gets in the way. Very important lesson,
[L1376] [47:03.88] because
[L1377] [47:04.88] it means that we cannot really say is a
[L1378] [47:08.28] type system useful or not unless we say
[L1379] [47:10.52] which one, because we know that
[L1380] [47:12.72] weak type systems are very inconvenient.
[L1381] [47:16.56] It must at least have parametric
[L1382] [47:18.32] polymorphism.
[L1383] [47:19.56] And that is another idea that was born
[L1384] [47:21.76] in the world of functional programming.
[L1385] [47:23.20] It was born in ML, incidentally, Robin
[L1386] [47:25.08] Milner's um
[L1387] [47:26.48] famous dictum, well-typed programs don't
[L1388] [47:27.88] go wrong. ML was a the first I think the
[L1389] [47:30.08] first parametrically polymorphic
[L1390] [47:31.60] function programming language, but
[L1391] [47:33.68] generics in Java and object-oriented
[L1392] [47:36.16] programming more generally is exactly
[L1393] [47:37.60] the same idea.
[L1394] [47:38.92] Right?
[L1395] [47:39.84] So, there's an idea that was born in
[L1396] [47:41.24] functional programming and made its way
[L1397] [47:42.44] into the mainstream.
[L1398] [47:44.24] >> And you mentioned polymorphism, and so
[L1399] [47:46.16] there's this parametric polymorphism in
[L1400] [47:47.92] the type system, but uh in the example
[L1401] [47:51.00] you mentioned where maybe you want to do
[L1402] [47:54.00] an operation on a list, and then the
[L1403] [47:55.92] type of the input changes. Uh I was
[L1404] [47:58.88] think just thinking what about when
[L1405] [48:00.40] people do polymorphism
[L1406] [48:02.52] in the classes?
[L1407] [48:04.04] >> Yeah, okay. But so now you're into a
[L1408] [48:05.76] whole more complicated world, right? So,
[L1409] [48:07.52] as soon as you say class, you're talking
[L1410] [48:09.36] static type system again, right? Um and
[L1411] [48:11.40] so object-oriented programming is is
[L1412] [48:14.24] another approach to polymorphism. So,
[L1413] [48:17.28] in an object-oriented language, we say
[L1414] [48:20.72] if we have a uh Ford that is a car and a
[L1415] [48:24.88] car is a vehicle,
[L1416] [48:26.84] then anything that works on vehicles
[L1417] [48:28.76] should also work on cars and should also
[L1418] [48:30.48] work on Fords.
[L1419] [48:31.84] So,
[L1420] [48:33.12] um the code that we write for cars works
[L1421] [48:36.36] unchanged
[L1422] [48:38.60] for
[L1423] [48:39.72] vehicles and for Fords.
[L1424] [48:41.24] Okay?
[L1425] [48:43.16] Now, that's a form of polymorphism. Not
[L1426] [48:45.40] parametric polymorphism, that's called
[L1427] [48:47.08] what you might call object-oriented
[L1428] [48:48.68] polymor- or subtype polymorphism.
[L1429] [48:51.36] Okay. So, now we but polymorphism in the
[L1430] [48:53.48] sense that the same code
[L1431] [48:57.24] the same executable code, actually the
[L1432] [48:59.00] same machine instructions, work on
[L1433] [49:00.88] values of different types.
[L1434] [49:03.96] Okay? In both cases.
[L1435] [49:05.92] Both reverse a list, same machine
[L1436] [49:07.76] instructions. Code that works on
[L1437] [49:09.56] vehicles works on uh things on Fords,
[L1438] [49:11.04] same machine instructions, right?
[L1439] [49:12.96] Okay.
[L1440] [49:14.40] That's what polymorphism in general
[L1441] [49:15.92] means. Parametric polymorphism means
[L1442] [49:17.92] this for all A, list of A's to list of
[L1443] [49:19.72] A's stuff.
[L1444] [49:20.76] Subtype polymorphism means if it works
[L1445] [49:22.76] on vehicles, it works on any subtype of
[L1446] [49:24.16] vehicles. Okay?
[L1447] [49:26.20] Now, the interaction of the two, which
[L1448] [49:28.72] you get by adding generics to an
[L1449] [49:31.32] object-oriented language,
[L1450] [49:33.36] is pretty complicated.
[L1451] [49:36.52] Oh, and by the way, adding side effects
[L1452] [49:38.00] as well.
[L1453] [49:39.36] And that's why you'll that that and uh
[L1454] [49:41.36] so
[L1455] [49:42.36] uh your question involving classes and
[L1456] [49:44.56] superclasses and so forth is smack in
[L1457] [49:46.88] that complicated world.
[L1458] [49:48.68] And I'm not sure it'll be very fruitful
[L1459] [49:50.68] for us to you know, we'd we'd we'd have
[L1460] [49:52.12] to get a lot more details of the type
[L1461] [49:53.60] system sorted out and know what to say.
[L1462] [49:56.16] Um but at this very high-level overview,
[L1463] [49:58.68] my my sort of the big point I'm trying
[L1464] [50:00.72] to make is weak type systems
[L1465] [50:03.84] get in the way. Type systems are meant
[L1466] [50:05.76] to reject programs that will go wrong,
[L1467] [50:07.72] but my function that reverses a list
[L1468] [50:10.68] of integers, it will also reverse the
[L1469] [50:12.36] list of characters. So, it's tiresome to
[L1470] [50:14.04] be told, "No, that is a bad program."
[L1471] [50:16.68] Right? I want to be able to write that
[L1472] [50:17.88] as that for a list of A to list of A.
[L1473] [50:20.12] So,
[L1474] [50:21.12] the idea of making type system more
[L1475] [50:22.76] complicated is to say uh programs that
[L1476] [50:25.64] you want to run, you can still write in
[L1477] [50:28.44] your static type system. Now, um you
[L1478] [50:30.64] might say, "Well, blimey, if that's all
[L1479] [50:32.64] if that's all, why don't we just get rid
[L1480] [50:33.88] of the static type system altogether?"
[L1481] [50:35.96] Now, we could run all of those programs,
[L1482] [50:37.76] but the trouble is you can run too many
[L1483] [50:39.08] programs now. You can run programs that
[L1484] [50:41.20] will crash at run time, and that's very,
[L1485] [50:43.48] very, very bad, and we all know
[L1486] [50:46.08] the costs of uh programs that that crash
[L1487] [50:48.60] at deployment that you could have
[L1488] [50:50.60] crashed before you even started to run
[L1489] [50:53.04] them, let alone before you even run your
[L1490] [50:54.52] first test.
[L1491] [50:56.52] Right?
[L1492] [50:57.68] Before you even linked it into an
[L1493] [50:59.24] executable,
[L1494] [51:00.60] that's really good. But, the biggest
[L1495] [51:02.68] benefit of a static type system, in my
[L1496] [51:04.60] humble opinion, is maintainability. If
[L1497] [51:07.40] you have a program written in um I don't
[L1498] [51:09.36] know, Pearl or Ruby,
[L1499] [51:11.28] um or um
[L1500] [51:13.44] Lisp in its inner basic form, um and it
[L1501] [51:16.92] was written 15 years ago, and the
[L1502] [51:18.88] original author has left, um and all of
[L1503] [51:21.56] the people who were involved at the time
[L1504] [51:22.80] it was written have left,
[L1505] [51:24.64] then that program is very difficult to
[L1506] [51:26.84] maintain.
[L1507] [51:29.16] And it it becomes almost immutable.
[L1508] [51:31.20] Nobody dares change it anymore. What
[L1509] [51:33.08] they do is it's an immutable piece of
[L1510] [51:34.84] software, and you do that stuff around
[L1511] [51:36.24] the edges to impedance match what you
[L1512] [51:38.40] really want to do to this now immutable
[L1513] [51:40.40] blob.
[L1514] [51:41.48] Now, of course, you have lots of tests.
[L1515] [51:43.44] So, test-driven development, I'm totally
[L1516] [51:45.32] with it. I love all any of all of that.
[L1517] [51:46.84] But,
[L1518] [51:47.84] still
[L1519] [51:49.64] GHC, for example, is itself written in
[L1520] [51:51.96] Haskell. It's 35 years old, and yet I do
[L1521] [51:55.00] large-scale systematic refactorings of
[L1522] [51:57.48] it,
[L1523] [51:58.52] you know,
[L1524] [51:59.60] fearlessly,
[L1525] [52:01.00] because the type system keeps me safe.
[L1526] [52:02.40] In fact, often what I'll do is I'll
[L1527] [52:04.32] change a few types and then start
[L1528] [52:05.68] compiling,
[L1529] [52:07.36] and then a sort of wave of changes
[L1530] [52:09.04] propagate through forced by, you know, I
[L1531] [52:10.84] just get type errors. So, I know what to
[L1532] [52:12.36] do.
[L1533] [52:13.60] Whereas the thought that I've changed
[L1534] [52:15.60] the representation of this data
[L1535] [52:16.72] structure a little bit, but I've added a
[L1536] [52:17.84] field to this data structure, where in
[L1537] [52:20.68] the entire compiler might that field be
[L1538] [52:22.80] read, written, or or freshly allocated?
[L1539] [52:27.12] I can't imagine how anybody maintains
[L1540] [52:29.12] 30-year-old software and makes
[L1541] [52:30.96] large-scale changes like that
[L1542] [52:33.08] without a type system. It's
[L1543] [52:34.12] unimaginable. So, for me,
[L1544] [52:36.04] the benefit of type systems is
[L1545] [52:38.24] maintainability. Oh, and designability,
[L1546] [52:40.28] right? So, a type um I often write the
[L1547] [52:42.84] types of my programs up front. I write
[L1548] [52:45.12] the type, you know, the data types are
[L1549] [52:47.24] super perspicuous.
[L1550] [52:49.84] You know, if I say uh it's a bit like
[L1551] [52:52.16] writing the classes of a of an of an
[L1552] [52:54.04] object-oriented language, right? But, if
[L1553] [52:55.68] you have no types, no classes, nothing,
[L1554] [52:57.88] just, I don't know, S-expressions,
[L1555] [53:00.72] >> [laughter]
[L1556] [53:02.00] >> uh
[L1557] [53:02.60] types are the way I design language.
[L1558] [53:04.36] They're they're the way that I start
[L1559] [53:05.72] writing my designs.
[L1560] [53:07.20] >> I'm trying to understand uh other
[L1561] [53:09.04] mindset, like let's say C, for instance,
[L1562] [53:11.24] where I remember a lot of stuff when I
[L1563] [53:13.76] was learning it in college, for
[L1564] [53:14.96] instance,
[L1565] [53:16.32] uh many times where I I'd add a
[L1566] [53:18.68] character to a pointer or something, and
[L1567] [53:20.72] it it just works cuz
[L1568] [53:22.60] it interprets the character as a number.
[L1569] [53:25.64] Um and so, is there any value to having
[L1570] [53:29.80] that kind of type system, or is that
[L1571] [53:31.88] just strictly unredeemable?
[L1572] [53:34.96] >> Just use stronger.
[L1573] [53:37.00] I think there's no benefit to weaker.
[L1574] [53:39.40] >> Just off the top of my head, one thing I
[L1575] [53:41.64] think of is there is a set of programs
[L1576] [53:44.72] that will work but don't satisfy the
[L1577] [53:48.88] type system.
[L1578] [53:49.84] >> that's right.
[L1579] [53:50.64] >> That and but those are
[L1580] [53:52.92] I mean, I don't know if they're good.
[L1581] [53:54.16] That's subjective.
[L1582] [53:54.88] >> they may be good. So So So So uh uh that
[L1583] [53:58.72] like I like we started, if you have
[L1584] [54:01.00] Pascal
[L1585] [54:02.48] and you write a function to reverse a
[L1586] [54:04.04] list of integers, then if you apply it
[L1587] [54:05.92] to a list of characters, the same
[L1588] [54:07.40] machine instructions would work but it
[L1589] [54:09.96] is rejected, right?
[L1590] [54:12.08] So, we have rejected a perfectly decent
[L1591] [54:14.32] program, bad,
[L1592] [54:16.12] right? Our goal is to expand the
[L1593] [54:20.20] collection of the programs that satisfy
[L1594] [54:21.84] the type system
[L1595] [54:23.64] to include as many as possible of the
[L1596] [54:25.88] programs we want to run
[L1597] [54:27.84] without including any of the bad
[L1598] [54:29.60] programs that we don't want to run.
[L1599] [54:32.20] Okay?
[L1600] [54:33.68] Parametric polymorphism is a big step in
[L1601] [54:35.80] that direction.
[L1602] [54:38.16] Um other, you know, type system
[L1603] [54:40.00] innovations are a big step in that
[L1604] [54:41.44] direction, but there will always be some
[L1605] [54:43.92] programs
[L1606] [54:45.48] that would run perfectly well
[L1607] [54:50.04] that the type system rejects.
[L1608] [54:53.72] Imagine a tree that is um uh contains
[L1609] [54:58.04] integers at every node.
[L1610] [55:00.32] But
[L1611] [55:02.16] if you are 17 deep in the tree or 34 or
[L1612] [55:06.92] 51
[L1613] [55:09.12] if you're in a multiple of 17 deep, the
[L1614] [55:11.16] integers can be characters instead. Or
[L1615] [55:13.80] the integers all turn out to be
[L1616] [55:14.80] characters, right?
[L1617] [55:17.28] Now,
[L1618] [55:18.32] you could write a program that generated
[L1619] [55:20.04] such trees and you could write a program
[L1620] [55:21.76] that consumed such trees knowing that
[L1621] [55:23.64] every 17th
[L1622] [55:25.00] um layer we switch to characters
[L1623] [55:27.12] but most static type systems would make
[L1624] [55:29.40] it pretty hard for you to accept that
