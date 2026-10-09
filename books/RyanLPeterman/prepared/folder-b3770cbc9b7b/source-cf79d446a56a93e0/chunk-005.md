Chunk 5; segments 1394–1758. Start may repeat the previous chunk for context.

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L1403] [01:11:28.72] memory management, resource management
[L1404] [01:11:31.52] was important. I've thought that from
[L1405] [01:11:34.08] the beginning. I didn't think garbage
[L1406] [01:11:36.24] collection was appropriate for a lot of
[L1407] [01:11:38.56] what I was doing, but certainly um
[L1408] [01:11:42.32] automating
[L1409] [01:11:43.92] uh the management was ideal.
[L1410] [01:11:48.56] And so after a long set of discussions
[L1411] [01:11:52.72] we found an interface that people agreed
[L1412] [01:11:55.92] on and uh we put it into C++ 11. And
[L1413] [01:12:02.32] what we found was over the next 10
[L1414] [01:12:05.44] years,
[L1415] [01:12:07.04] the amount of usage of garbage
[L1416] [01:12:09.20] collection decreased
[L1417] [01:12:11.92] as um our AI, the uh resource management
[L1418] [01:12:17.44] that had been there all the time got
[L1419] [01:12:20.08] more and better understood and was used
[L1420] [01:12:23.44] more.
[L1421] [01:12:24.96] Furthermore, the people who still used
[L1422] [01:12:27.04] the garbage collectors didn't use the
[L1423] [01:12:29.36] standard interface because they had
[L1424] [01:12:32.08] figured out ways of doing it better. And
[L1425] [01:12:35.36] so today, there are still a few people
[L1426] [01:12:37.76] doing garbage collection, but it's not
[L1427] [01:12:40.32] part of the standard.
[L1428] [01:12:43.04] >> How does that work? Is it kind of like a
[L1429] [01:12:45.04] wrapper around the uh memory allocation
[L1430] [01:12:48.24] methods?
[L1431] [01:12:49.04] >> Yeah.
[L1432] [01:12:49.76] >> Okay. you you have you have a a
[L1433] [01:12:53.20] different implementation of
[L1434] [01:12:56.72] uh new or maloc or operator new or
[L1435] [01:13:00.64] whatever it is you're using at your
[L1436] [01:13:02.48] lowest level and then um delete becomes
[L1437] [01:13:09.28] something slightly different too.
[L1438] [01:13:11.68] there's this cautionary tale in the C++
[L1439] [01:13:14.48] community about uh this ship Vasa and I
[L1440] [01:13:18.88] was kind of curious like why that's
[L1441] [01:13:20.64] popular and
[L1442] [01:13:21.76] >> oh um
[L1443] [01:13:24.64] we had a meeting in Stockholm at some
[L1444] [01:13:28.00] point and they have a wonderful ship
[L1445] [01:13:31.12] that if you ever get to Stockholm you
[L1446] [01:13:32.96] should see the Vasa. It's a battleship
[L1447] [01:13:35.92] from the 1600s. There's a story to that
[L1448] [01:13:38.96] and that's the one I tell people. Um
[L1449] [01:13:43.12] the king was building was was ordering
[L1450] [01:13:49.12] built a battleship that should be the
[L1451] [01:13:53.12] best and most beautiful battleship
[L1452] [01:13:57.28] around. Uh it was going to be a good
[L1453] [01:14:00.96] fighting battleship and it was going to
[L1454] [01:14:02.72] be used for diplomatic uh visits. So it
[L1455] [01:14:05.60] should be beautiful. [snorts]
[L1456] [01:14:07.60] And uh they laid down the keel and they
[L1457] [01:14:09.92] started building it. And then they heard
[L1458] [01:14:12.24] that a likely opponent was building
[L1459] [01:14:14.96] battleships with two gun decks.
[L1460] [01:14:17.84] And this was an then old-fashioned
[L1461] [01:14:22.48] battleship with only one gun deck. And
[L1462] [01:14:25.12] if you put a two gun a one gun deck
[L1463] [01:14:28.80] battleship next to a two gun deck
[L1464] [01:14:30.72] battleship, the highly predictable
[L1465] [01:14:33.52] result is a lot of holes in the one um
[L1466] [01:14:38.00] gun deck battleship and it it's gone.
[L1467] [01:14:42.08] So the king orders that this ship should
[L1468] [01:14:44.88] now have two gun decks
[L1469] [01:14:48.72] and um they've already started building
[L1470] [01:14:52.00] it.
[L1471] [01:14:54.00] So they add another Glend, they add
[L1472] [01:14:56.48] cannons up there. And the king also
[L1473] [01:14:59.44] wants now the ship is bigger. They want
[L1474] [01:15:02.32] more statues and beautiful things. So it
[L1475] [01:15:06.56] becomes a bit topheavy.
[L1476] [01:15:10.00] And uh rumor has it I've never checked
[L1477] [01:15:13.36] this rumor so it might be wrong. Uh is
[L1478] [01:15:16.08] that the ship designer committed suicide
[L1479] [01:15:19.68] uh out of horror. Um I also a thing that
[L1480] [01:15:25.68] I don't believe is just a rumor was when
[L1481] [01:15:28.64] they was built they tested it for
[L1482] [01:15:31.04] stability. And the way you test a st a
[L1483] [01:15:36.58] [snorts]
[L1484] [01:15:37.12] and ship like that for stability is you
[L1485] [01:15:39.60] take the whole crew and you run them
[L1486] [01:15:41.28] from one side to the other back forth
[L1487] [01:15:44.64] get harmonic uh stair and if you can do
[L1488] [01:15:47.60] that 14 times then uh it'll stand up to
[L1489] [01:15:52.00] the Baltic and the North Sea.
[L1490] [01:15:55.76] Rumor has it actually as I said I think
[L1491] [01:15:59.44] it's a fact um that they did it seven
[L1492] [01:16:02.64] times and then they stopped because it
[L1493] [01:16:05.12] looked dangerous.
[L1494] [01:16:07.92] So um
[L1495] [01:16:11.76] this was
[L1496] [01:16:13.84] 1624
[L1497] [01:16:16.48] I think. Um, the ship gets finished. Uh,
[L1498] [01:16:22.16] it's sailing out. The most wonderful
[L1499] [01:16:24.80] ship you've ever seen. It's sailing out
[L1500] [01:16:27.44] in uh Stockholm Harbor. Trumpets, uh,
[L1501] [01:16:31.28] blaring flags flying, uh, families of
[L1502] [01:16:35.68] crews on board, the whole thing. It gets
[L1503] [01:16:37.84] halfway across the, uh, harbor, a gust
[L1504] [01:16:40.96] of wind comes, it kills the war, and
[L1505] [01:16:43.20] it's gone. And it ends down in some
[L1506] [01:16:46.88] place where there's not much um
[L1507] [01:16:50.16] much oxygen. So it was well preserved
[L1508] [01:16:52.40] and they fished it up again. Uh and you
[L1509] [01:16:54.64] can see it. And so I tell this story to
[L1510] [01:16:58.88] the standards committee and I point out
[L1511] [01:17:01.44] there's something they did wrong. They
[L1512] [01:17:04.56] built more features on top without
[L1513] [01:17:07.20] improving the foundation.
[L1514] [01:17:09.84] always improve the foundation to make
[L1515] [01:17:12.08] sure that it's just not a a random set
[L1516] [01:17:14.64] of features that you have added because
[L1517] [01:17:16.88] that's complexity.
[L1518] [01:17:19.12] Furthermore,
[L1519] [01:17:20.64] do not um compromise your testing.
[L1520] [01:17:26.48] That's really dangerous. And
[L1521] [01:17:29.60] furthermore, uh you you've all noticed
[L1522] [01:17:32.72] when your high bosses say something
[L1523] [01:17:34.96] should be done and the high bosses don't
[L1524] [01:17:37.52] always know what's right. Uh sometimes
[L1525] [01:17:40.64] the professional thing is to say no, we
[L1526] [01:17:43.12] are not doing this. We have to take it
[L1527] [01:17:45.60] easy. If they had said, okay, we'll
[L1528] [01:17:49.12] build a one uh gun battleship. We'll
[L1529] [01:17:52.72] just not call it the Vasa. Call it
[L1530] [01:17:55.44] something neutral. And then next year
[L1531] [01:17:58.32] you can have a battleship that's been
[L1532] [01:18:00.08] designed from the bottom up to be a two
[L1533] [01:18:02.96] gun battleship. You wouldn't have any
[L1534] [01:18:05.52] problems with that. But the high
[L1535] [01:18:08.64] management, meaning the king who was in
[L1536] [01:18:11.04] Poland at the time, so he couldn't even
[L1537] [01:18:12.88] see it, says, "Nope, must be delivered
[L1538] [01:18:15.68] on time." And so they delivered
[L1539] [01:18:18.80] something on time that just couldn't do
[L1540] [01:18:20.96] the job.
[L1541] [01:18:22.32] But go see the ship. It's great.
[L1542] [01:18:25.20] >> At some point uh someone demonstrated
[L1543] [01:18:28.72] that the C++ template instantiation
[L1544] [01:18:32.32] mechanism was turning complete. So you
[L1545] [01:18:36.24] know what the compiler is going to do to
[L1546] [01:18:38.72] kind of pre-process that C++ program can
[L1547] [01:18:42.08] actually be used for computation just uh
[L1548] [01:18:45.12] and I was just trying to understand h
[L1549] [01:18:48.08] how is that possible like how it it was
[L1550] [01:18:50.40] mentioned something about he uh
[L1551] [01:18:53.04] calculated prime numbers at compile
[L1552] [01:18:55.04] time. How does that work?
[L1553] [01:18:57.28] >> Well that's I mean the prime number
[L1554] [01:18:59.52] thing was was just a a curiosity. it uh
[L1555] [01:19:03.12] used the error messages to report the
[L1556] [01:19:06.56] result. But um when you build something
[L1557] [01:19:11.28] uh you can get Turing completeness um
[L1558] [01:19:14.64] you you you need some form of uh iterate
[L1559] [01:19:20.00] or recurse and you need a um [snorts] a
[L1560] [01:19:24.56] comparison and that's about it. then you
[L1561] [01:19:27.84] can get true to incompleteness and the
[L1562] [01:19:31.76] at least some of the theoreticians says
[L1563] [01:19:36.24] we can't do that it'll run forever and
[L1564] [01:19:40.24] um the guy who uh
[L1565] [01:19:43.36] who came up with with the first example
[L1566] [01:19:45.84] of this uh actually thought I should
[L1567] [01:19:49.52] prohibit it somehow I should ban it and
[L1568] [01:19:52.64] my reaction was this looks useful Great.
[L1569] [01:19:57.76] And uh I think I was right. Furthermore,
[L1570] [01:20:01.28] nothing runs forever. If you have a
[L1571] [01:20:03.84] Turing machine, you have the tape
[L1572] [01:20:06.80] and the tape has to be infinite.
[L1573] [01:20:09.76] So if if you imagine building a real
[L1574] [01:20:12.40] cheing machine the way Turing designed
[L1575] [01:20:15.28] it, you have to have a bunch of navies
[L1576] [01:20:18.08] building track all the time when it gets
[L1577] [01:20:20.72] out there. Of course, we don't do that.
[L1578] [01:20:24.00] The point is that the compiler will run
[L1579] [01:20:26.08] out of resources long before we get into
[L1580] [01:20:28.88] real problems. Machines are finite
[L1581] [01:20:33.04] and so the problem does
[L1582] [01:20:36.72] doesn't become real in in unless there's
[L1583] [01:20:39.92] bugs and the bugs get caught guaranteed.
[L1584] [01:20:43.84] So not a problem. What happened though
[L1585] [01:20:47.20] was that people were misusing
[L1586] [01:20:50.16] templates to do simple calculations.
[L1587] [01:20:53.28] like prime numbers or your trust is yeah
[L1588] [01:20:56.48] your sustenance is se or u calculating
[L1589] [01:21:00.88] factorials and such and it's so awful
[L1590] [01:21:05.28] and it's so expensive and it uses up so
[L1591] [01:21:08.80] much memory that it becomes a problem so
[L1592] [01:21:12.88] that was why I and Gabidas re uh built
[L1593] [01:21:16.88] constexer which basically says you can
[L1594] [01:21:20.24] calculate perfectly ordinary code at
[L1595] [01:21:23.12] compile time and it is much simpler,
[L1596] [01:21:27.36] much more what we're used to and much
[L1597] [01:21:32.00] faster to compile uh and giving usually
[L1598] [01:21:35.76] much faster code and um you have that
[L1599] [01:21:39.60] today and you have constant value if you
[L1600] [01:21:41.52] want to guarantee that this is done
[L1601] [01:21:44.70] [snorts]
[L1602] [01:21:45.28] and uh so that takes care of the obvious
[L1603] [01:21:49.52] misuses of the idea of uh templates
[L1604] [01:21:53.28] being during complete it turns them into
[L1605] [01:21:56.24] ordinary functions.
[L1606] [01:21:58.08] >> Generally with programming languages
[L1607] [01:22:00.16] there's this um you know high level
[L1608] [01:22:02.56] intuition that the closer to the machine
[L1609] [01:22:05.12] you are the higher the performance is
[L1610] [01:22:07.76] and um you know I I tend to see C as
[L1611] [01:22:12.16] closer to the machine than C++ for
[L1612] [01:22:14.48] instance. Um no that's not the case.
[L1613] [01:22:17.44] >> It's not the case. It's not as good as
[L1614] [01:22:19.60] compile time calculation at C++ is. And
[L1615] [01:22:23.92] anyway, we have exactly the same machine
[L1616] [01:22:26.24] model because uh um C borrowed the C++
[L1617] [01:22:31.12] 11 machine model. Um so if you write the
[L1618] [01:22:36.00] same code in both languages, it's you
[L1619] [01:22:38.88] get the same result except uh the C++
[L1620] [01:22:42.64] compilers can do more at compile time.
[L1621] [01:22:46.56] And so C++ runs as fast or faster than C
[L1622] [01:22:51.28] in most cases. There's more information
[L1623] [01:22:55.20] if if uh if you give a optimizer more
[L1624] [01:22:58.32] information, it can do a better job.
[L1625] [01:23:00.64] >> Ah, okay. Yeah, because that was what I
[L1626] [01:23:02.64] was going to ask you was you had said
[L1627] [01:23:05.52] somewhere that C++ can be more
[L1628] [01:23:07.36] performant than C, but I tend to think
[L1629] [01:23:10.16] that more abstraction costs you
[L1630] [01:23:12.00] something. But
[L1631] [01:23:12.72] >> it's compiled away. This is why I talk
[L1632] [01:23:15.20] about zero overhead abstraction and
[L1633] [01:23:18.48] people are beginning to take me to task
[L1634] [01:23:20.88] for that because that's underestimating
[L1635] [01:23:24.00] the uh and understating the ability of
[L1636] [01:23:27.12] the C++ compiler. We can do negative
[L1637] [01:23:30.48] overhead uh abstraction.
[L1638] [01:23:34.40] >> What if I was really good at writing
[L1639] [01:23:36.40] assembly and I had all the time in the
[L1640] [01:23:38.40] world to write it. Could that how about
[L1641] [01:23:40.72] how does that compare? If you are very
[L1642] [01:23:43.84] smart and you have infinite time, uh you
[L1643] [01:23:47.68] can do better.
[L1644] [01:23:50.00] Um by and large we are not as smart as
[L1645] [01:23:53.60] the um optimizers anymore and we don't
[L1646] [01:23:57.92] have infinite time.
[L1647] [01:24:00.16] So if we are uh smart enough, we can
[L1648] [01:24:03.52] only do a small piece of code. And now
[L1649] [01:24:07.36] um the question is did we get enough
[L1650] [01:24:10.48] time to use our smarts.
[L1651] [01:24:13.28] Uh this is even starting to affect
[L1652] [01:24:18.40] uh clever code.
[L1653] [01:24:21.04] I gave a talk to uh Slack last year
[L1654] [01:24:24.56] which is a group of uh very performant
[L1655] [01:24:28.32] uh interested people from the finance
[L1656] [01:24:31.04] industry
[L1657] [01:24:32.72] and my title was don't be clever.
[L1658] [01:24:37.20] Actually the written title was don't be
[L1659] [01:24:39.20] too clever but I can't pronounce
[L1660] [01:24:41.12] parenthesis.
[L1661] [01:24:42.80] Um and I got out alive.
[L1662] [01:24:46.72] Um, and my main point was that C++ is
[L1663] [01:24:50.96] good enough
[L1664] [01:24:52.72] for uh more than 98% of your code. So if
[L1665] [01:24:57.28] you want time to be clever,
[L1666] [01:25:00.16] you use these techniques and I showed
[L1667] [01:25:02.16] modern C++
[L1668] [01:25:04.56] and that way you get time so you can do
[L1669] [01:25:07.36] all the clever optimizations. The
[L1670] [01:25:09.52] problem is clever optimizations these
[L1671] [01:25:11.92] days tend to be machine dependent. That
[L1672] [01:25:15.44] is if you get a new
[L1673] [01:25:18.96] computer or if you get a new version of
[L1674] [01:25:21.60] the compiler, you might actually have
[L1675] [01:25:24.08] pessimized your code. I've seen this
[L1676] [01:25:26.96] repeatedly ever since the uh the 80s. uh
[L1677] [01:25:32.64] and there there there's people who does
[L1678] [01:25:35.20] nothing but uh u using different
[L1679] [01:25:39.12] optimizations on the next generation
[L1680] [01:25:41.44] hardware
[L1681] [01:25:43.12] and u my standard techniques for um for
[L1682] [01:25:48.08] for improving things actually is to
[L1683] [01:25:51.68] first throw away the clever stuff
[L1684] [01:25:54.80] and then see if you run faster or
[L1685] [01:25:57.60] slower. Usually you run faster because
[L1686] [01:26:01.28] clever stuff tends and at least 1990s
[L1687] [01:26:05.92] story style clever stuff which is
[L1688] [01:26:07.68] there's a lot of it still today because
[L1689] [01:26:10.48] the techniques uh carry on in people's
[L1690] [01:26:13.44] heads and uh some of the code remains uh
[L1691] [01:26:18.16] tend to use a right nest of pointers
[L1692] [01:26:21.36] and that uh gives the compilers and
[L1693] [01:26:24.72] optimizers problems.
[L1694] [01:26:27.36] They also sometimes use uh more
[L1695] [01:26:30.48] allocations
[L1696] [01:26:32.16] which is not good. You want to minimize
[L1697] [01:26:34.40] memory access. You want to maximize uh
[L1698] [01:26:38.32] your cache performance and things like
[L1699] [01:26:41.12] that. And compilers are getting very
[L1700] [01:26:43.76] good at that. And I have seen th this
[L1701] [01:26:47.84] kind of thinking. I wrote a paper about
[L1702] [01:26:50.56] it together with a friend of mine in
[L1703] [01:26:52.72] Spain doing flu fluid dynamics and uh uh
[L1704] [01:26:57.92] we we we threw away uh the clever stuff
[L1705] [01:27:01.20] for a uh
[L1706] [01:27:05.04] actually a performance uh test suite
[L1707] [01:27:08.88] example. So it was not toy and we got
[L1708] [01:27:12.96] only 20% improvement
[L1709] [01:27:16.40] by reducing the code to about 80% of
[L1710] [01:27:20.00] what it was before and so some people
[L1711] [01:27:24.00] didn't think that was significant. I
[L1712] [01:27:26.48] thought it was significant proof that
[L1713] [01:27:28.80] the technique was appropriate. You apply
[L1714] [01:27:31.84] optimizations only when you need them.
[L1715] [01:27:35.68] Kuth says don't do premature
[L1716] [01:27:38.00] optimization but he also pointed out
[L1717] [01:27:40.48] that two to 3% is where you uh where you
[L1718] [01:27:44.32] should optimize which is exactly the
[L1719] [01:27:46.64] number I'm using
[L1720] [01:27:49.44] and so first build the stuff using high
[L1721] [01:27:53.44] level facilities
[L1722] [01:27:55.36] see if it's good enough and if it isn't
[L1723] [01:27:58.56] uh and you have to time it you don't
[L1724] [01:28:00.88] guess you time uh then you uh up then
[L1725] [01:28:05.76] you figure out where the time is spent
[L1726] [01:28:07.60] and then you optimize that
[L1727] [01:28:10.24] but a lot of the time you don't need to
[L1728] [01:28:12.64] go to that stage it's it's fast enough
[L1729] [01:28:16.00] >> I see so when you say cleverness here
[L1730] [01:28:18.16] it's um like human level a manual
[L1731] [01:28:21.60] management to ek out performance
[L1732] [01:28:23.84] >> yes
[L1733] [01:28:24.32] >> and you're saying that actually if you
[L1734] [01:28:26.72] don't do that the compile you're giving
[L1735] [01:28:28.48] the compiler more to optimize and it can
[L1736] [01:28:30.88] do a good job
[L1737] [01:28:32.08] >> and it's much much better than it used
[L1738] [01:28:34.24] to
[L1739] [01:28:35.28] code that was cleverly and correctly
[L1740] [01:28:38.32] optimized in the 1990s
[L1741] [01:28:42.00] are often pessimized today
[L1742] [01:28:45.68] because machine architectures have
[L1743] [01:28:47.60] changed
[L1744] [01:28:49.12] and the compilers have improved. When I
[L1745] [01:28:52.00] look at the industry today, um more and
[L1746] [01:28:55.12] more of code is being written by
[L1747] [01:28:58.24] machines than humans. And I I feel like
[L1748] [01:29:01.04] a lot of programming language design is
[L1749] [01:29:03.60] thinking about how do you make it u
[L1750] [01:29:07.12] amendable to humans solving problems and
[L1751] [01:29:09.44] writing the code. And I'm curious if you
[L1752] [01:29:11.60] have any thoughts on if you think
[L1753] [01:29:13.44] programming language design will change
[L1754] [01:29:15.36] if more and more of the code is written
[L1755] [01:29:17.92] by you know models and machines. I
[L1756] [01:29:23.28] think that in the field I'm mostly
[L1757] [01:29:26.32] interested in,
[L1758] [01:29:28.56] code will still be written by humans
[L1759] [01:29:31.92] and they will use abstraction.
[L1760] [01:29:34.40] The examples I've seen of attempts for
[L1761] [01:29:39.20] AI to generate code in this domain
[L1762] [01:29:43.12] uh has not been successful.
[L1763] [01:29:45.60] it uh they generate more bugs, more
[L1764] [01:29:49.12] security holes. They have uh bloated
[L1765] [01:29:52.48] code which pessimize again because you
[L1766] [01:29:56.08] use more memory
[L1767] [01:29:58.32] and um it's hard to validate
