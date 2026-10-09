Chunk 4; segments 1247–1658. Start may repeat the previous chunk for context.

# Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy

Source ID: source-fba2cff234dd0aeb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_OCaml_Functional_Programming,_Formal_Verification,_Programming_Languages_Xavier_Leroy_en.txt
Video: https://www.youtube.com/watch?v=9Cswiqrq6So

[L1256] [45:29.48] predictions, impossible predictions,
[L1257] [45:31.48] where where the past depends on the
[L1258] [45:32.96] future.
[L1259] [45:34.66] >> [snorts]
[L1260] [45:34.84] >> Crazy, really crazy stuff.
[L1261] [45:37.04] Uh then C C++ 11 did a little better,
[L1262] [45:40.16] but still extremely complex memory
[L1263] [45:42.36] model. And so, when we wanted to add
[L1264] [45:44.72] when the especially the OCaml Labs
[L1265] [45:46.84] people wanted to add uh shared memory
[L1266] [45:48.88] concurrency to OCaml, we had to also
[L1267] [45:51.36] agree on a memory model
[L1268] [45:53.24] that would be
[L1269] [45:54.68] exposed to the programmers.
[L1270] [45:56.64] And and that's also took quite a bit of
[L1271] [45:58.92] a design uh quite a bit of time to come
[L1272] [46:01.24] up with a good design. Uh
[L1273] [46:03.28] And I
[L1274] [46:04.16] I think it's it's
[L1275] [46:05.80] better and easier to understand and use
[L1276] [46:08.36] than the one of Java, but the the OCaml
[L1277] [46:11.36] memory model is still quite complicated.
[L1278] [46:14.32] And
[L1279] [46:15.72] And sometimes I feel sorry our users are
[L1280] [46:18.00] are exposed to that. Okay. Uh
[L1281] [46:21.20] Uh
[L1282] [46:22.08] So, that that that explains why it took
[L1283] [46:24.16] so long.
[L1284] [46:25.76] Solving the
[L1285] [46:27.32] engineering challenges, but also
[L1286] [46:30.36] having a
[L1287] [46:31.56] agreeing on the memory model and what
[L1288] [46:33.32] kind of guarantees we're going to give
[L1289] [46:34.96] to programmers.
[L1290] [46:36.56] Oh, yeah. I forgot to say one thing,
[L1291] [46:38.76] which is that
[L1292] [46:40.36] So, C and C++ there's a lot of things
[L1293] [46:42.92] you can say, "Oh, it's just undefined
[L1294] [46:44.40] behavior or anything can happen."
[L1295] [46:46.52] In type-safe languages like Java and
[L1296] [46:48.44] OCaml, you want to give stronger
[L1297] [46:49.92] guarantees. Okay. Maybe many things can
[L1298] [46:53.00] happen, but your data should should
[L1299] [46:55.68] remain well-typed.
[L1300] [46:57.56] Okay. Typically, you don't want to
[L1301] [46:59.56] expose an object to another thread
[L1302] [47:02.04] before it's been fully initialized, for
[L1303] [47:03.68] instance.
[L1304] [47:04.84] Um And And that's that's actually very
[L1305] [47:08.20] hard to guarantee in your memory model.
[L1306] [47:10.84] And then
[L1307] [47:12.16] you have to implement that memory model,
[L1308] [47:13.60] so your compiler also needs to take
[L1309] [47:15.28] extra
[L1310] [47:16.48] precautions to to to guarantee this. So,
[L1311] [47:19.48] yeah, type safety in the presence of
[L1312] [47:22.84] shared memory concurrency is is not
[L1313] [47:25.80] obvious at all.
[L1314] [47:27.60] And so, that's why it took so long.
[L1315] [47:30.20] >> So, in Python, I know there's the famous
[L1316] [47:32.68] GIL or the global interpreter lock. What
[L1317] [47:35.80] is that lock protecting? Is it the the
[L1318] [47:37.92] cleanup of objects on the heap or is it
[L1319] [47:40.88] something else?
[L1320] [47:41.92] >> Among other things, yes. So, yeah, we we
[L1321] [47:44.52] had the same thing in OCaml before
[L1322] [47:46.80] before
[L1323] [47:47.96] multicore OCaml with
[L1324] [47:50.24] >> [snorts]
[L1325] [47:51.16] >> with Marstin. So, yeah, well, basically,
[L1326] [47:53.80] the idea that when when your runtime
[L1327] [47:55.36] system is not thread-safe, as we said,
[L1328] [47:57.92] you can protect the non-thread safe
[L1329] [47:59.84] functions by your lock so that
[L1330] [48:02.24] they will never be executed
[L1331] [48:03.40] concurrently.
[L1332] [48:04.72] But if you take the lock at every
[L1333] [48:06.32] allocation and release it,
[L1334] [48:08.80] you take and release the lock for every
[L1335] [48:10.20] allocation and it's just too slow
[L1336] [48:11.80] anyway.
[L1337] [48:12.96] And so the idea is that
[L1338] [48:15.24] you take the lock when you enter Python
[L1339] [48:18.32] code, let's say, and you start executing
[L1340] [48:20.88] Python code.
[L1341] [48:22.48] But you can still release it when you do
[L1342] [48:25.00] input output for instance, when you're
[L1343] [48:26.36] going to block for a long time.
[L1344] [48:28.60] Or when you're calling into C code that
[L1345] [48:31.40] that
[L1346] [48:32.80] that is thread safe and is not going to
[L1347] [48:34.60] use your runtime system.
[L1348] [48:36.60] Then you can release the lock and some
[L1349] [48:38.20] other
[L1350] [48:39.44] Python thread can take it and execute.
[L1351] [48:42.52] So you get a little bit of concurrency.
[L1352] [48:44.32] You can overlap computations in your
[L1353] [48:47.40] high-level language with IO or
[L1354] [48:49.40] computation is a low-level language in
[L1355] [48:51.60] another language.
[L1356] [48:53.16] But you still have mutual exclusion
[L1357] [48:54.84] between your
[L1358] [48:56.76] between two threads running Python or
[L1359] [48:59.28] running OCaml before before multicore
[L1360] [49:01.52] OCaml.
[L1361] [49:03.64] So so you get some benefits like
[L1362] [49:07.04] concurrent IO, but you don't get any
[L1363] [49:08.64] parallelism.
[L1364] [49:09.92] Okay, yeah. You don't get a speed up for
[L1365] [49:12.48] computations.
[L1366] [49:14.64] And so so yeah, so we used to have this
[L1367] [49:17.28] this this GIL in in in OCaml as well.
[L1368] [49:20.88] And
[L1369] [49:22.48] so you can get rid of it, but in
[L1370] [49:24.72] general, you need to redesign at least
[L1371] [49:26.96] the garbage collector and and memory
[L1372] [49:29.52] allocator.
[L1373] [49:32.80] There's probably a few places in the
[L1374] [49:34.44] OCaml runtime system that still use
[L1375] [49:36.08] locks to
[L1376] [49:38.24] to to ensure mutual exclusion like in
[L1377] [49:40.04] the IO subsystem.
[L1378] [49:44.60] And and some phases of the garbage
[L1379] [49:46.16] collector, I think that there's a phase
[L1380] [49:48.24] which is kind of stop the world where
[L1381] [49:50.12] you need to make sure that everyone
[L1382] [49:53.28] no no no camel code is is running.
[L1383] [49:56.16] So for a short time you need to make
[L1384] [49:57.68] sure that everyone is stopped and then
[L1385] [49:59.72] do a little bit of work to finish the GC
[L1386] [50:02.08] and then you can restart everyone.
[L1387] [50:04.56] Um so yeah, that these are tricky things
[L1388] [50:07.08] and I don't know what the Python people
[L1389] [50:08.76] are up to with their GIL if if they
[L1390] [50:10.96] finally managed to remove it or
[L1391] [50:13.68] they're still working on it but I I I've
[L1392] [50:15.52] heard they're making progress. So.
[L1393] [50:17.96] >> Yeah, you mentioned Python calling into
[L1394] [50:21.08] C and I've seen that pattern before of a
[L1395] [50:24.48] higher level language interfacing with a
[L1396] [50:26.64] lower level one. How does that binding
[L1397] [50:29.72] typically work?
[L1398] [50:31.60] >> Oh, it's another can of worms.
[L1399] [50:33.68] Um
[L1400] [50:36.24] Um
[L1401] [50:38.40] Well, there are two aspects. There are
[L1402] [50:39.48] there are the the control flow and there
[L1403] [50:41.12] are the
[L1404] [50:42.40] the data.
[L1405] [50:43.92] So the control part is is
[L1406] [50:47.00] not that hard. So yes, you need you need
[L1407] [50:49.08] a mechanism so that your your Python
[L1408] [50:51.28] interpreter or your OCaml compiled code
[L1409] [50:53.72] will actually jump to the C function.
[L1410] [50:57.04] Uh so for OCaml basically you you tell
[L1411] [50:59.40] your OCaml compiler that this function
[L1412] [51:01.20] is not implemented in OCaml, it's
[L1413] [51:03.12] actually implemented by a C function and
[L1414] [51:05.12] you give its name and then the compiler
[L1415] [51:07.04] will emit a call to the C function using
[L1416] [51:09.60] the C calling conventions which are not
[L1417] [51:11.44] exactly the same as the OCaml calling
[L1418] [51:13.16] convention but
[L1419] [51:14.64] the compiler knows about that. And so it
[L1420] [51:17.24] will
[L1421] [51:18.16] call the C function maybe through a
[L1422] [51:19.64] little bit of glue code or whatever and
[L1423] [51:22.32] then the C function will execute and and
[L1424] [51:25.28] return back to the OCaml code.
[L1425] [51:28.12] Um
[L1426] [51:30.28] That's relatively easy. Uh now the hard
[L1427] [51:33.40] part is uh data
[L1428] [51:35.64] uh like function arguments and function
[L1429] [51:37.68] results
[L1430] [51:39.40] because OCaml and C have different data
[L1431] [51:42.20] representations.
[L1432] [51:43.92] Uh for instance, a floating point number
[L1433] [51:45.72] in in OCaml is generally boxed, so it's
[L1434] [51:48.88] allocated in the heap and handled
[L1435] [51:50.40] through a pointer. So, it's more like a
[L1436] [51:52.64] double star in in C
[L1437] [51:55.32] and it's not a double, which is not
[L1438] [51:57.68] allocated.
[L1439] [51:59.32] Just it's in a register.
[L1440] [52:01.72] Um so
[L1441] [52:03.88] so typically the C code needs to use a
[L1442] [52:06.32] so-called foreign function interface, so
[L1443] [52:08.20] some C function and macros provided by
[L1444] [52:10.36] OCaml to access the OCaml data, the
[L1445] [52:13.48] OCaml arguments, you know, extract the
[L1446] [52:15.72] part that it needs, the the numbers, the
[L1447] [52:19.44] uh
[L1448] [52:20.08] uh yeah, another example is arrays. Um
[L1449] [52:23.20] in OCaml when you have
[L1450] [52:25.44] a two-dimensional array, it's actually
[L1451] [52:26.96] an array of arrays. So, viewed from C,
[L1452] [52:29.20] it's an array of pointers to arrays.
[L1453] [52:31.48] While in C, an array of arrays is
[L1454] [52:33.60] there's no intermediate pointer, so it's
[L1455] [52:35.08] not the same representation. And so, you
[L1456] [52:37.24] have to explain to C or give C some
[L1457] [52:39.76] functions and macros to to access uh
[L1458] [52:43.12] elements in OCaml arrays. Uh it's not
[L1459] [52:45.56] exactly the same code that that that
[L1460] [52:48.32] that that you would do to access a C
[L1461] [52:50.48] array from C.
[L1462] [52:52.88] Okay, so you need accessors, but now if
[L1463] [52:55.60] you want to uh
[L1464] [52:57.48] if your C code wants to return some
[L1465] [52:59.36] complex results like a list, an array,
[L1466] [53:02.72] and so on, it needs to allocate it in
[L1467] [53:04.76] the OCaml heap. So, it needs to ask the
[L1468] [53:08.04] runtime system to do some heap
[L1469] [53:10.00] allocation and then fill the uh
[L1470] [53:12.51] >> [snorts]
[L1471] [53:12.96] >> heap blocks correctly. And then this
[L1472] [53:15.56] allocation can can trigger a garbage
[L1473] [53:17.52] collection, so the C code that also kind
[L1474] [53:20.00] of cooperate with a garbage collection
[L1475] [53:23.48] with registration mechanisms, etc., etc.
[L1476] [53:26.36] So, so there's quite a bit of work to to
[L1477] [53:28.32] be done.
[L1478] [53:29.48] And and uh and then different foreign
[L1479] [53:32.60] function interfaces
[L1480] [53:34.76] arrange this work differently. So,
[L1481] [53:36.76] there's a base FFI for OCaml, basically
[L1482] [53:39.64] uh it's a C code that must do all the
[L1483] [53:41.28] work.
[L1484] [53:42.36] But but then it can be very fast and
[L1485] [53:45.04] quite optimized.
[L1486] [53:46.60] Uh but there are other FFIs like the C
[L1487] [53:49.08] types FFI in OCaml where most of these
[L1488] [53:51.52] data conversion and and mediating
[L1489] [53:53.88] between two data formats is automated.
[L1490] [53:56.88] Uh you start basically with a
[L1491] [53:58.60] description of the the the the the C
[L1492] [54:00.96] type of the C function and and you can
[L1493] [54:03.32] automate some of those conversions. But
[L1494] [54:05.32] sometimes it can be tricky it can be
[L1495] [54:06.92] expensive. For instance, [snorts] you
[L1496] [54:08.60] may end up copying the whole array while
[L1497] [54:12.16] your C code only needs to access two or
[L1498] [54:13.96] three elements in it.
[L1499] [54:15.60] Um okay. So there's lots of trade-offs.
[L1500] [54:18.92] And quite frankly it it's a dirty part
[L1501] [54:22.32] of of programming language
[L1502] [54:23.44] implementation. Uh the the OCaml FFI is
[L1503] [54:27.92] not that clean, but if you look at the
[L1504] [54:29.92] Java FFI for instance, it's also quite
[L1505] [54:31.96] complicated. And for Python I've I've
[L1506] [54:34.52] never tried. Uh so I I don't know what
[L1507] [54:37.40] it looks like.
[L1508] [54:39.28] Uh
[L1509] [54:39.96] but yeah, it's a it's a necessity.
[L1510] [54:42.36] Uh but but it can be quite hard because
[L1511] [54:44.60] the data models are different between
[L1512] [54:47.44] the two languages.
[L1513] [54:49.28] >> So to kind of get the big picture, on
[L1514] [54:52.32] the OCaml side, there's an interpreter
[L1515] [54:55.36] which is a program running in
[L1516] [54:57.16] application space that is interpreting
[L1517] [55:00.56] your OCaml code. And then at some point
[L1518] [55:03.52] in the OCaml code, it says
[L1519] [55:06.48] do some, you know, load this C program.
[L1520] [55:09.60] And the C program is a binary somewhere.
[L1521] [55:12.48] And the OCaml interpreter then starts to
[L1522] [55:16.08] load those instructions and execute
[L1523] [55:17.84] them.
[L1524] [55:18.36] >> Okay. So actually this is the third
[L1525] [55:20.52] aspect that I didn't touch.
[L1526] [55:22.88] So so OCaml well, there's an interpreter
[L1527] [55:25.72] mode, but in general we compile. We
[L1528] [55:28.08] compile to assembly code and then
[L1529] [55:30.60] machine code.
[L1530] [55:32.08] And so
[L1531] [55:33.48] so in in in compiled mode,
[L1532] [55:36.48] what what you say is
[L1533] [55:39.00] how you put together the OCaml code and
[L1534] [55:41.56] the C code is done by the the linker,
[L1535] [55:44.08] the C linker. So so
[L1536] [55:46.76] So basically someone else is doing that
[L1537] [55:48.92] for us. And and and it's not that
[L1538] [55:51.80] different from linking together two
[L1539] [55:55.32] object files produced by C or two object
[L1540] [55:58.32] files produced by OCaml.
[L1541] [56:00.96] But you write that for for more
[L1542] [56:02.60] interpreted
[L1543] [56:04.12] languages, there's also the question of
[L1544] [56:05.68] how you load the C code.
[L1545] [56:07.88] Generally you know you use the dynamic
[L1546] [56:10.04] loading like interface dlopen for
[L1547] [56:12.56] instance in in in Unix.
[L1548] [56:17.12] So and and and then there's a little bit
[L1549] [56:19.72] of introspection. So so at at run time
[L1550] [56:22.40] the interpreter will query the C
[L1551] [56:24.08] libraries and where is the address of a
[L1552] [56:26.60] function named foo? And then it will
[L1553] [56:29.28] find the address and use that to
[L1554] [56:30.92] manufacture a call. So yeah, if you're
[L1555] [56:34.24] in an interpreted setting or
[L1556] [56:36.60] or bytecode compiled setting like
[L1557] [56:38.04] Python, it's there's this additional
[L1558] [56:40.56] level of complexity on top of it.
[L1559] [56:44.28] >> I see. I see. Okay, so if I had a mixed
[L1560] [56:48.00] OCaml C program
[L1561] [56:50.84] to my computer it's just one binary or
[L1562] [56:54.68] one one blob.
[L1563] [56:56.16] >> In in in the simplest case, yes.
[L1564] [57:00.36] There are also dynamic loading
[L1565] [57:02.20] facilities in OCaml, but I don't want to
[L1566] [57:04.16] get into that because I'm a firm
[L1567] [57:06.08] believer in static linking. I think
[L1568] [57:08.64] programs should be statically linked so
[L1569] [57:11.04] that there's no surprise when you run
[L1570] [57:13.44] them. Okay, like oh, where is this DLL
[L1571] [57:16.28] or DLL not found for instance problems.
[L1572] [57:19.36] But
[L1573] [57:21.64] of course you lose a little bit in
[L1574] [57:22.88] flexibility.
[L1575] [57:26.00] But yeah, I think the static static
[L1576] [57:28.00] linking has a lot to
[L1577] [57:31.96] is is actually quite useful in in that
[L1578] [57:34.36] it it guarantees a lot of things. It
[L1579] [57:36.08] checks a lot of things at link time that
[L1580] [57:37.84] you
[L1581] [57:38.80] don't have to check again at run time.
[L1582] [57:41.48] >> We mentioned earlier in the conversation
[L1583] [57:43.44] talking a little bit about LLM generated
[L1584] [57:45.36] code. I thought that might be
[L1585] [57:46.40] interesting to cover. Um and in one
[L1586] [57:49.80] interview you talked about the danger of
[L1587] [57:53.00] almost correct code. So, plausible code
[L1588] [57:55.96] but it's it's wrong that an LLM can
[L1589] [57:57.84] produce. And what are your thoughts on
[L1590] [58:01.00] you know how to address that kind of
[L1591] [58:02.72] problem?
[L1592] [58:04.72] >> It's it's it's a tough problem. I mean
[L1593] [58:07.00] you
[L1594] [58:08.28] um
[L1595] [58:09.36] globally I'm a little bit skeptical
[L1596] [58:11.08] about generative AI. Oh, of course they
[L1597] [58:14.16] they they
[L1598] [58:15.40] they can do amazing things that were
[L1599] [58:17.72] unthinkable like a few years ago.
[L1600] [58:20.48] But there's also
[L1601] [58:22.92] there's always some errors. Okay. It's
[L1602] [58:25.52] it's
[L1603] [58:26.36] you can't really trust
[L1604] [58:28.56] oh
[L1605] [58:29.64] what's what's being produced by by
[L1606] [58:31.60] generative AI.
[L1607] [58:33.08] And so
[L1608] [58:35.00] the the
[L1609] [58:37.64] uh
[L1610] [58:38.68] in principle humans should be there to
[L1611] [58:41.76] check the output and
[L1612] [58:44.20] and fix errors or ask the LLM to fix its
[L1613] [58:48.08] own errors
[L1614] [58:49.32] until the result is actually usable. But
[L1615] [58:52.60] of course it's very hard because well
[L1616] [58:54.48] there's a slot problem. Okay.
[L1617] [58:56.72] AI's produce so much it's so it's so
[L1618] [58:59.76] easy to produce
[L1619] [59:01.44] uh
[L1620] [59:02.00] to produce large number large quantities
[L1621] [59:04.96] of text of code or pictures or whatever
[L1622] [59:08.88] that that that in the end
[L1623] [59:10.92] there's there's there's no human
[L1624] [59:14.60] no no no human time to to check it all.
[L1625] [59:18.68] So,
[L1626] [59:20.08] recently I heard a
[L1627] [59:22.40] uh well someone working in an AI startup
[L1628] [59:24.52] who was enthusiastic about
[L1629] [59:27.24] uh
[L1630] [59:28.32] AI generated code thing that thanks to
[L1631] [59:30.28] Genady AI is a cost of programming is
[L1632] [59:33.04] dropping to zero.
[L1633] [59:35.08] But well, the cost of writing code
[L1634] [59:37.12] maybe, but
[L1635] [59:39.32] what about you know checking it,
[L1636] [59:42.24] making sure it is correct, um
[L1637] [59:45.28] that it does what we want, that
[L1638] [59:47.76] well, that cost is not zero at all.
[L1639] [59:50.12] >> Uh-huh.
[L1640] [59:50.92] >> And and for me
[L1641] [59:52.44] every new line of code is a liability.
[L1642] [59:54.96] So you you have to test it, you have to
[L1643] [59:57.76] check it, maybe you have to do formal
[L1644] [59:59.20] verification. You have to
[L1645] [01:00:02.04] evolve it, maintain it later. So so no,
[L1646] [01:00:05.84] I don't want huge amounts of code, okay?
[L1647] [01:00:07.92] I want I want
[L1648] [01:00:09.12] 50 lines of code that have been
[L1649] [01:00:11.48] thought that have been polished over the
[L1650] [01:00:13.56] years.
[L1651] [01:00:14.64] So anyway, I'm not getting that with AI.
[L1652] [01:00:18.92] And and and I think that's the problem.
[L1653] [01:00:22.52] And this idea that humans will be there
[L1654] [01:00:24.60] to check the output of Genady AI is just
[L1655] [01:00:28.00] wrong.
[L1656] [01:00:29.32] No, they they they are not available for
[L1657] [01:00:31.72] that. They
[L1658] [01:00:32.96] There's too much of it and it's
[L1659] [01:00:35.04] and it's [snorts] not it's not pleasant
[L1660] [01:00:37.72] either, okay? I mean, I don't think it's
[L1661] [01:00:39.64] a good way to to to split the work
[L1662] [01:00:41.64] between machines and and humans.
[L1663] [01:00:44.68] So anyway, so maybe there will be some
[L1664] [01:00:46.88] social
[L1665] [01:00:48.16] solution like big
[L1666] [01:00:51.01] >> [snorts]
[L1667] [01:00:51.04] >> no to AI slop movements. So we we we're
