Chunk 5; segments 1400–1744. Start may repeat the previous chunk for context.

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

Source ID: source-238007c2e5a842c7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_P_vs_NP,_Zero-Knowledge_Proofs,_Quantum_Computation_Avi_Wigderson_en.txt
Video: https://www.youtube.com/watch?v=5GUcvSAJcJw

[L1409] [01:05:11.28] hard for you to guess but I could have
[L1410] [01:05:13.84] taken the first random bit I pick for
[L1411] [01:05:16.24] the so I generate from many a few one
[L1412] [01:05:21.04] what you want to do is the opposite you
[L1413] [01:05:22.80] want a method that will take a few and
[L1414] [01:05:25.52] we generate many
[L1415] [01:05:28.08] right that's a random generator So, so
[L1416] [01:05:30.48] the random generator starts for a few
[L1417] [01:05:32.80] truly random bits and generates many and
[L1418] [01:05:36.00] for this we need
[L1419] [01:05:38.48] we need other tools. Uh there's
[L1420] [01:05:40.72] something uh that I developed with
[L1421] [01:05:43.12] Nissan
[L1422] [01:05:45.12] because today the NW generator. I like
[L1423] [01:05:48.08] to say that you know people
[L1424] [01:05:51.28] say that making the f first million
[L1425] [01:05:53.44] dollars is easy and afterwards you can
[L1426] [01:05:55.52] make many more millions.
[L1427] [01:05:57.84] You can think of it this way. The
[L1428] [01:05:59.92] hardness in the way I described it allow
[L1429] [01:06:02.48] you to make $1 million. But once you can
[L1430] [01:06:06.56] make one, there are methods to make many
[L1431] [01:06:09.68] more and in fact more than the number of
[L1432] [01:06:13.36] bits you started with. But still their
[L1433] [01:06:15.52] quality depend on the hardness of the
[L1434] [01:06:17.60] function you use. we still use this and
[L1435] [01:06:21.20] uh your your limit you know limitation
[L1436] [01:06:23.92] of you know being running polomial time
[L1437] [01:06:27.44] so it's you cannot solve this hard
[L1438] [01:06:30.08] instance you build many many instances
[L1439] [01:06:33.84] from a short seed you you start from
[L1440] [01:06:37.68] maybe a logarithmically
[L1441] [01:06:39.76] uh long seed you take many subsets of
[L1442] [01:06:43.12] this like n you need n of them and I ask
[L1443] [01:06:46.56] you for the value of the solution to
[L1444] [01:06:48.96] each one. Each one is hard but we want
[L1445] [01:06:51.44] to say that they are simultaneously
[L1446] [01:06:54.00] hard. You cannot tell them apart.
[L1447] [01:06:55.60] There's no correlation you can detect
[L1448] [01:06:57.60] between them even though they're
[L1449] [01:06:59.28] extremely correlated. So yeah, so we
[L1450] [01:07:01.76] have methods to do that as well. So
[L1451] [01:07:04.24] that's the connection you embed having a
[L1452] [01:07:06.48] hard problem to a limited observer means
[L1453] [01:07:10.00] that some uncertainty about the answer.
[L1454] [01:07:12.16] That's a key that's a starting point. So
[L1455] [01:07:15.12] when you say that the quality of the
[L1456] [01:07:18.08] randomness is a function of the
[L1457] [01:07:20.48] computational power of the observer, one
[L1458] [01:07:23.44] thought that comes to mind is imagine I
[L1459] [01:07:26.32] have um maybe infinite compute then then
[L1460] [01:07:31.04] nothing is truly random. Is that is that
[L1461] [01:07:34.48] accurate to say like you know if I had
[L1462] [01:07:36.40] infinite compute I the weather is not
[L1463] [01:07:39.28] random nothing is random. Uh okay. So
[L1464] [01:07:44.80] it points to the fact that you have to
[L1465] [01:07:47.28] really be careful about what question
[L1466] [01:07:49.36] you are asking about the randomness if
[L1467] [01:07:53.20] uh you want uh you know u to apply this
[L1468] [01:07:58.96] to to probabilistic algorithms
[L1469] [01:08:03.20] then it's really important that you are
[L1470] [01:08:05.52] limitless computationally. So if you
[L1471] [01:08:07.28] have infinite compute times you will be
[L1472] [01:08:09.60] able to distinguish
[L1473] [01:08:11.76] a a distribution with full entropy to
[L1474] [01:08:15.36] the random and one with coming from a
[L1475] [01:08:17.84] generator one with low entropy. So you
[L1476] [01:08:20.48] could do that but one thing you cannot
[L1477] [01:08:24.64] do with infinite compute is something
[L1478] [01:08:26.48] that's information theoretic. So there
[L1479] [01:08:29.60] are many other uh things we need to do
[L1480] [01:08:31.84] with random bits than just run probistic
[L1481] [01:08:35.76] algorithms. For example, we want to
[L1482] [01:08:37.44] generate passwords for our you know
[L1483] [01:08:40.40] crypto you know for uh security systems
[L1484] [01:08:46.32] there the very demand is that they are
[L1485] [01:08:50.24] random right I mean Shannon theorem
[L1486] [01:08:52.32] tells you you know the quality of your
[L1487] [01:08:55.04] passport is as good as the entropy in
[L1488] [01:08:57.20] it. So uh the notion of a cir secret
[L1489] [01:09:01.68] rests on the random on the true
[L1490] [01:09:04.72] randomness of the so if I just ask you
[L1491] [01:09:08.64] to produce a random beat or you ask me
[L1492] [01:09:11.04] to produce a random beat uh you know
[L1493] [01:09:14.32] whether you have computational infinite
[L1494] [01:09:17.36] computational power or not doesn't
[L1495] [01:09:20.16] matter I mean to generate this random
[L1496] [01:09:23.04] bit it has to be random I mean you your
[L1497] [01:09:25.44] demand is not that it will succeed in
[L1498] [01:09:27.52] some test you really want the
[L1499] [01:09:29.52] probability of heads to be half, tails
[L1500] [01:09:31.84] to be a half. This you know then this
[L1501] [01:09:35.52] definition or this task of producing
[L1502] [01:09:38.72] randomness
[L1503] [01:09:40.32] is not related to your computational
[L1504] [01:09:42.40] power.
[L1505] [01:09:45.36] So you know lucky or unlucky I don't
[L1506] [01:09:48.00] know for us many times we do have
[L1507] [01:09:51.68] implicit or explicit tests for this
[L1508] [01:09:54.40] randomness you say I can break this you
[L1509] [01:09:57.20] know I can break this system or
[L1510] [01:09:58.96] something and then you can maybe use to
[L1511] [01:10:01.68] the randomness but uh if your very
[L1512] [01:10:04.00] demand is to have a random event then
[L1513] [01:10:06.32] you need to produce a random event. I
[L1514] [01:10:08.56] saw in when I was doing my research that
[L1515] [01:10:12.24] there are ways to uh create higher
[L1516] [01:10:15.20] quality randomness by aggregating weaker
[L1517] [01:10:18.96] sources.
[L1518] [01:10:19.76] >> Yeah.
[L1519] [01:10:20.32] >> Um how how does that work?
[L1520] [01:10:22.72] >> Well, it's another theory. I talked
[L1521] [01:10:25.44] before about the theory of pseudo
[L1522] [01:10:26.96] randomness. There's a whole different
[L1523] [01:10:28.96] theory. They are related in non-trivial
[L1524] [01:10:31.76] ways, but uh um it's called the theory
[L1525] [01:10:35.68] of randomness extraction.
[L1526] [01:10:38.08] and or randomness purification maybe and
[L1527] [01:10:41.28] this is exactly what you asked about. Uh
[L1528] [01:10:44.24] we imagine that the world maybe does not
[L1529] [01:10:46.96] give us perfect randomness. But we have
[L1530] [01:10:48.88] all these events we cannot predict like
[L1531] [01:10:50.80] the weather uh or or various quantum
[L1532] [01:10:54.48] phenomena or sunspots or we cannot
[L1533] [01:10:57.92] predict the you know stock prices right
[L1534] [01:11:01.92] otherwise the market will be but these
[L1535] [01:11:05.36] are not you know even though these are
[L1536] [01:11:07.68] these are unpredictable events they are
[L1537] [01:11:10.40] somewhat predictable. I mean the weather
[L1538] [01:11:12.48] tomorrow is more likely to be similar to
[L1539] [01:11:14.88] the weather today than the opposite of
[L1540] [01:11:17.44] the weather. So there are correlations
[L1541] [01:11:19.84] if you sample this weather for example.
[L1542] [01:11:23.04] There are also biases. I mean sometimes
[L1543] [01:11:24.96] you you know in the spring it's more or
[L1544] [01:11:28.00] in the summer it's likely more likely to
[L1545] [01:11:30.08] be hot than cold.
[L1546] [01:11:33.20] So there are biases correlations. These
[L1547] [01:11:35.60] are called weak random sources and
[L1548] [01:11:37.60] there's a mathematical quantification of
[L1549] [01:11:41.36] uh how weak they are basically talk
[L1550] [01:11:45.68] about the amount of entropy in them. you
[L1551] [01:11:48.48] have n bits potentially you can have
[L1552] [01:11:50.48] entropy n but maybe they were generated
[L1553] [01:11:54.16] from a generator or they came from some
[L1554] [01:11:56.64] source of we don't know uh so it has
[L1555] [01:12:00.00] some entropy in it but you have no idea
[L1556] [01:12:01.76] where I mean maybe half of them are
[L1557] [01:12:04.72] fixed and half of them are cointosis and
[L1558] [01:12:08.72] you don't know which half maybe they are
[L1559] [01:12:10.96] each you know half you know three
[L1560] [01:12:14.80] quarter zero and one quart of you know
[L1561] [01:12:17.68] So tails have a bias that also has lots
[L1562] [01:12:20.48] of enthropy but not full and maybe the
[L1563] [01:12:23.28] correlations are even more complicated.
[L1564] [01:12:26.00] So you can imagine all sorts of
[L1565] [01:12:28.16] situation like this and you
[L1566] [01:12:29.60] mathematically model it by saying okay
[L1567] [01:12:32.88] there are n bits it's a probability
[L1568] [01:12:35.52] distribution n bits which has some
[L1569] [01:12:38.16] entropy let's say square root of n you
[L1570] [01:12:40.16] don't know where and uh you want to use
[L1571] [01:12:43.52] it in a probabilistic algorithm. So it's
[L1572] [01:12:46.16] a basic question. Can we use physical
[L1573] [01:12:48.96] events
[L1574] [01:12:50.56] uh weak sources coming from nature maybe
[L1575] [01:12:53.84] uh in in probabistic algorithms and
[L1576] [01:12:57.52] certainly not obvious. I mean just
[L1577] [01:12:59.28] feeding them to the algorithm as is not
[L1578] [01:13:02.56] going to work. They are very easy to
[L1579] [01:13:04.40] find simple algorithms that will fail
[L1580] [01:13:06.88] that will succeed on perfect randomness
[L1581] [01:13:08.88] and will fail on will always make an
[L1582] [01:13:11.92] error.
[L1583] [01:13:14.24] But uh the theory of randomness
[L1584] [01:13:17.76] purification wants to take this
[L1585] [01:13:21.04] um this um uh sample of n bits with all
[L1586] [01:13:27.04] with some amount of entropy which is not
[L1587] [01:13:29.44] full and someone massage it create from
[L1588] [01:13:32.56] it maybe a shorter string which is u you
[L1589] [01:13:38.56] know of higher quality. Ideally it would
[L1590] [01:13:41.12] be perfect random bits. So ideally you
[L1591] [01:13:43.52] can imagine that if I have n random bits
[L1592] [01:13:46.08] and I have enthropy root n maybe I can
[L1593] [01:13:48.96] massage out of there square root n or
[L1594] [01:13:52.16] maybe just the fourth root of n
[L1595] [01:13:55.28] bits that will be essentially uniformly
[L1596] [01:13:58.88] distributed then if I have an algorithm
[L1597] [01:14:01.20] that just needs this amount that's what
[L1598] [01:14:03.92] I feel it turns out you cannot do that
[L1599] [01:14:08.16] it's impossible but what you can do is
[L1600] [01:14:10.96] not produce one string of length let's
[L1601] [01:14:15.76] say square root 10 but you can com you
[L1602] [01:14:18.96] can produce n to the hund of them
[L1603] [01:14:22.64] okay and what you are guaranteed so this
[L1604] [01:14:25.36] is a this randomness purification uh
[L1605] [01:14:28.32] device is an efficient algorithm that
[L1606] [01:14:30.24] takes any any uh distribution with
[L1607] [01:14:33.60] enthalpy in it and you produce many
[L1608] [01:14:37.12] blocks polomally many blocks of the
[L1609] [01:14:39.76] length roughly the enthalpy what you
[L1610] [01:14:41.92] would hope to be perfect and what you
[L1611] [01:14:45.12] are guaranteed is that 99% of them are
[L1612] [01:14:52.40] truly perfect. So you have many
[L1613] [01:14:57.36] 99% of them are as good as perfect and
[L1614] [01:15:01.92] there's 1% which is bad. You don't know
[L1615] [01:15:03.92] which it is. But that's already solves
[L1616] [01:15:06.00] your problem because run your algorithm
[L1617] [01:15:08.48] on each one of them. take a majority
[L1618] [01:15:11.12] vote. Doing this is extremely
[L1619] [01:15:13.84] complicated. There are many ways of
[L1620] [01:15:15.84] doing it. There are varants of you know
[L1621] [01:15:18.80] various assumptions you can make about
[L1622] [01:15:20.48] the entropy. Maybe you have several weak
[L1623] [01:15:23.28] sources that are not related to each
[L1624] [01:15:25.28] other. There are various
[L1625] [01:15:28.16] um uh yeah the various variants and this
[L1626] [01:15:31.52] theory is very well developed. But we
[L1627] [01:15:34.08] know that uh uh the statement I made
[L1628] [01:15:38.16] essentially is is accurate. If you have
[L1629] [01:15:41.60] one source uh with some entropy in it,
[L1630] [01:15:44.56] you can generate polomially many samples
[L1631] [01:15:47.04] of the length of almost the entropy and
[L1632] [01:15:50.00] most of them will be perfect. So that's
[L1633] [01:15:54.32] as useful as having one. Yeah. I vaguely
[L1634] [01:15:57.12] remember I was skimming a bunch of
[L1635] [01:15:59.28] papers and one of the papers it had this
[L1636] [01:16:01.20] uh had this figure where it was a
[L1637] [01:16:03.92] two-dimensional array of numbers and I
[L1638] [01:16:06.00] think there were like drawing rectangles
[L1639] [01:16:07.92] or something like that. Is that like one
[L1640] [01:16:10.16] of the ideas? Uh so it's a notion of
[L1641] [01:16:12.56] pseudo randomness which is related to uh
[L1642] [01:16:16.72] one particular variant of this
[L1643] [01:16:18.88] extraction problem where you have
[L1644] [01:16:21.76] several weak sources not one one is the
[L1645] [01:16:24.48] hardest because that's yeah but maybe
[L1646] [01:16:27.12] you have a few that are independent and
[L1647] [01:16:30.00] each of them has some entropy in it
[L1648] [01:16:33.68] and uh I think what you're referring to
[L1649] [01:16:35.92] is this sum product theorem this uh uh
[L1650] [01:16:40.08] yeah I cannot draw the pictures of there
[L1651] [01:16:42.56] but uh you don't really need to. So
[L1652] [01:16:45.68] let's just think about this problem. You
[L1653] [01:16:47.44] have uh uh three sources of randomness.
[L1654] [01:16:52.56] They are each weak. So each has just a
[L1655] [01:16:55.12] little bit of entropy in it. And all you
[L1656] [01:16:57.52] want to produce is one source with
[L1657] [01:17:01.20] somewhat larger entropy. So you are
[L1658] [01:17:03.52] losing in the number of sources but you
[L1659] [01:17:06.08] are gaining entropy. If you can repeat
[L1660] [01:17:08.08] this, you eventually get to full
[L1661] [01:17:10.56] entropy. So that's the idea. So what how
[L1662] [01:17:14.40] what combination of weak sources would
[L1663] [01:17:16.64] you take? It's not obvious and the
[L1664] [01:17:20.72] solution. Yeah, this is a certainly
[L1665] [01:17:24.16] there is maybe even this one. Uh there's
[L1666] [01:17:27.28] a paper I have with Barak and Impalato
[L1667] [01:17:29.52] about this particular problem and we are
[L1668] [01:17:32.32] using a result in what's called the
[L1669] [01:17:35.12] arithmetic combinatorics and I can
[L1670] [01:17:37.12] explain it very simply. I think that we
[L1671] [01:17:41.36] learn about addition in second grade and
[L1672] [01:17:44.32] about multiplication third grade maybe
[L1673] [01:17:47.52] and you know the only motivation for
[L1674] [01:17:50.32] multiplication is that it's a way to
[L1675] [01:17:53.68] shortcut repeated addition
[L1676] [01:17:56.72] and that's all we talk about. Then if
[L1677] [01:17:58.56] you go to college you you learn that you
[L1678] [01:18:01.92] know sum and products are the basic
[L1679] [01:18:03.92] operations of fields. You can do it with
[L1680] [01:18:06.48] integers. You can do it with rational
[L1681] [01:18:09.36] numbers, complex numbers, finite fields
[L1682] [01:18:11.84] and so on. So you remember these are the
[L1683] [01:18:14.32] basic but how do they relate to each
[L1684] [01:18:16.56] other?
[L1685] [01:18:18.32] It's not clear. It's not maybe there are
[L1686] [01:18:20.64] many ways to ask this question but one
[L1687] [01:18:23.28] way to ask this question that was
[L1688] [01:18:24.88] suggested by Erdesh and was
[L1689] [01:18:29.28] solved the first time by Erdish and
[L1690] [01:18:31.04] Seamar and then in a much more in a form
[L1691] [01:18:34.40] we really need by
[L1692] [01:18:36.96] Kent to say the following just think of
[L1693] [01:18:40.00] a set of integers
[L1694] [01:18:42.32] and add all pairs so you start with
[L1695] [01:18:44.72] let's say K integers add all pairs how
[L1696] [01:18:47.76] many new integers Do you get this you
[L1697] [01:18:50.64] should think of as entropy increase if
[L1698] [01:18:53.44] you get many more somehow? Yeah. So you
[L1699] [01:18:58.00] have K integers. Well, it depends what
[L1700] [01:19:00.00] they are. I mean if there are the first
[L1701] [01:19:02.88] K integers and you add all pairs up, you
[L1702] [01:19:05.44] get just the number between one and 2 K.
[L1703] [01:19:09.12] That's not much larger. That's a factor
[L1704] [01:19:11.04] or two larger. If you want increase an
[L1705] [01:19:13.12] entropy, you want to get you know uh
[L1706] [01:19:16.56] some power of k bigger than one.
[L1707] [01:19:20.56] Of course, if you take a random set of
[L1708] [01:19:22.24] integers,
[L1709] [01:19:23.76] uh you'll get k square, they will all be
[L1710] [01:19:26.16] distinct k² integers. So somehow you
[L1711] [01:19:30.40] want to say I mean it would be great if
[L1712] [01:19:33.36] for any set when you take all pairs you
[L1713] [01:19:36.48] group but it's not true by this example
[L1714] [01:19:39.84] of the interval. Well, you can not take
[L1715] [01:19:42.96] sums. You can take products.
[L1716] [01:19:46.00] Okay? But also products don't always
[L1717] [01:19:48.08] increase. If you take, you know, one,
[L1718] [01:19:50.88] two, four, eight, you take a geometric
[L1719] [01:19:54.08] progression, you multiply all pairs,
[L1720] [01:19:56.32] you'll just get just twice as many as
[L1721] [01:19:59.28] you start. So that's uh it's also not
[L1722] [01:20:03.68] good. And uh the magic in this sum
[L1723] [01:20:06.80] product theorem is that
[L1724] [01:20:09.36] sums and products are orthogonal to each
[L1725] [01:20:12.64] other. Somehow if one of them fails to
[L1726] [01:20:16.08] grow a set then the other will grow this
[L1727] [01:20:19.04] set.
[L1728] [01:20:21.20] And so this is an amazing result and the
[L1729] [01:20:25.44] way you use it in this context you think
[L1730] [01:20:27.52] of the outcome of your sources as
[L1731] [01:20:29.92] numbers.
[L1732] [01:20:31.60] you let's say multiply the first pair
[L1733] [01:20:35.28] and add them to the third you mix the
[L1734] [01:20:38.64] sum product. So this guarantees even
[L1735] [01:20:42.08] this is not obvious but if you do this
[L1736] [01:20:44.80] it guarantees that you you grow the
[L1737] [01:20:47.68] number of different values you get is
[L1738] [01:20:50.96] significantly more than K maybe it's K
[L1739] [01:20:53.20] to the 1.5 or something entropy does
[L1740] [01:20:56.56] increase and that's that's the source of
[L1741] [01:20:59.92] you need to prove it distributionally
[L1742] [01:21:01.92] it's not just the size the entropy is
[L1743] [01:21:04.00] not just size
[L1744] [01:21:05.92] um along with the size it's more than
[L1745] [01:21:08.24] that but anyway this is behind one
[L1746] [01:21:11.60] solution to one of the problems about
[L1747] [01:21:13.84] purification. It does not solve the one
[L1748] [01:21:17.28] source problem. This you need other
[L1749] [01:21:19.52] tools.
[L1750] [01:21:20.72] >> I saw that um you had done some work in
[L1751] [01:21:23.52] zero knowledge proofs. I was wondering
[L1752] [01:21:25.04] if you could explain you know what is a
[L1753] [01:21:26.96] zero knowledge proof and maybe we talk
