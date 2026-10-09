Chunk 5; segments 1328–1671. Start may repeat the previous chunk for context.

# Sergey Levine: Humanoid Robotics Results, Chinese Labs & Future Timelines

Source ID: source-902fbdda6bccd443
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Sergey_Levine_Humanoid_Robotics_Results,_Chinese_Labs_&_Future_Timelines_en.txt
Video: https://www.youtube.com/watch?v=9OSbaPjv0Rc

[L1337] [45:53.84] where of course the jury is still out as
[L1338] [45:55.20] to what the endgame of coding agents is,
[L1339] [45:57.60] but certainly uh from the experience of
[L1340] [46:01.44] uh software engineers today. Like it
[L1341] [46:03.04] kind of seems like probably fair to say
[L1342] [46:05.68] that most would consider coding agents
[L1343] [46:07.28] to be more empowering them rather than
[L1344] [46:10.56] like uh you know uh somehow causing them
[L1345] [46:13.28] to have a panic. I mean, obviously some
[L1346] [46:15.28] people might might have a panic, but in
[L1347] [46:16.64] general, at least from the software
[L1348] [46:19.04] engineers that that I've talked to and
[L1349] [46:20.88] from my own experience, it's more
[L1350] [46:22.32] empowering to have to kind of be able to
[L1351] [46:23.92] amplify how much work you can do uh with
[L1352] [46:27.12] AI tools. So, I think from that and and
[L1353] [46:29.60] that maybe is like a pretty direct
[L1354] [46:30.80] analogy because that is straight up an
[L1355] [46:32.40] example of an actual real job where AI
[L1356] [46:35.20] has entered into it and has actually
[L1357] [46:37.04] provided more leverage to people doing
[L1358] [46:38.56] that job. So I think that's another
[L1359] [46:40.00] example that we can look to but you know
[L1360] [46:41.60] the truth is that I think it remains to
[L1361] [46:43.28] be seen.
[L1362] [46:44.72] >> So in in LLM's there's a few seinal
[L1363] [46:47.36] papers that if you read those papers you
[L1364] [46:50.08] kind of get a sense of the lineage of
[L1365] [46:51.92] the breakthroughs that mattered and
[L1366] [46:54.08] understanding where we are today in the
[L1367] [46:56.80] robotics industry. Are there a set of
[L1368] [47:00.08] top papers that you really think kind of
[L1369] [47:03.52] show the breakthroughs that people
[L1370] [47:05.28] should know about if they're curious
[L1371] [47:07.20] about the state-of-the-art in terms of
[L1372] [47:09.84] uh humanoid robotics? One thing I would
[L1373] [47:12.64] point out um uh and this is like partly
[L1374] [47:15.44] a shameless plug because I am a
[L1375] [47:16.56] co-author on that paper though candidly
[L1376] [47:18.16] like uh like 99.9% of the work on this
[L1377] [47:21.36] was done by by um Tony who was lead
[L1378] [47:23.84] author is the uh the original ACT paper
[L1379] [47:26.32] the Aloha paper. It's kind it's an
[L1380] [47:28.24] interesting example because in some ways
[L1381] [47:31.04] the ideas weren't really that new but
[L1382] [47:33.12] they were illustrated in a really nice
[L1383] [47:34.72] way and the idea was that hey um if you
[L1384] [47:38.08] set up the right kind of lowcost robot
[L1385] [47:40.72] setup in in his case it was based on um
[L1386] [47:44.40] these robot arms from Trusson Robotics
[L1387] [47:46.24] that they're like $7,000 hobbyist arms.
[L1388] [47:48.88] He set them up in a banual setup with a
[L1389] [47:51.44] leader follower to the operation device.
[L1390] [47:53.84] And he showed that actually if you do it
[L1391] [47:55.60] right without really any particularly
[L1392] [47:56.96] fancy tricks, you could easily collect
[L1393] [47:59.28] the operation data of extremely dextrous
[L1394] [48:01.04] tasks that people had previously thought
[L1395] [48:02.64] would require like very sophisticated
[L1396] [48:04.24] hardware and all sorts of like really
[L1397] [48:05.60] expensive stuff and then set up like a
[L1398] [48:08.00] fairly
[L1399] [48:09.52] straightforward transformer-based model
[L1400] [48:11.52] and it could actually do a lot of those
[L1401] [48:12.88] tasks. And it's kind of like an
[L1402] [48:14.96] interesting thing because usually in
[L1403] [48:16.00] academic research we put a big premium
[L1404] [48:18.00] on like you know do you have some like
[L1405] [48:19.60] sophisticated new mathematical thing or
[L1406] [48:21.28] some sophisticated like uh technical
[L1407] [48:23.60] insight and in that paper which I think
[L1408] [48:26.80] at this point has been hugely
[L1409] [48:27.84] influential. The insight is really just
[L1410] [48:29.84] like yeah just put together the right
[L1411] [48:31.76] pieces and have a little bit more faith
[L1412] [48:35.36] in what a simple robot could do so to
[L1413] [48:37.28] speak equipped with a good intent
[L1414] [48:38.80] learning system. and he showed like
[L1415] [48:40.64] things like um uh replacing batteries in
[L1416] [48:43.20] a remote control. Uh he even had he even
[L1417] [48:45.92] got like a little like a mannequin foot
[L1418] [48:48.08] and he showed that you could put a shoe
[L1419] [48:49.20] on it like for like an assistive task
[L1420] [48:51.04] sort of like you know some some people
[L1421] [48:52.48] need help getting their shoes on so
[L1422] [48:53.68] that's good. Um but like what what
[L1423] [48:56.48] people find found I think so interesting
[L1424] [48:58.88] about that paper is just how far you
[L1425] [49:00.48] could get with like relatively simple
[L1426] [49:02.32] building blocks. And at this point the
[L1427] [49:04.32] the a like he he open sourced the code
[L1428] [49:06.32] for it and the act code has been used by
[L1429] [49:08.08] like lots of people sort of like if
[L1430] [49:09.60] someone wants a very basic starter kit
[L1431] [49:13.04] for like robotic learning that's usually
[L1432] [49:14.80] what they grab and I think that it's
[L1433] [49:18.48] worth for somebody who wants to get into
[L1434] [49:20.16] the field to go through that paper and
[L1435] [49:22.88] really understand what's going on there
[L1436] [49:24.16] because even though in some ways it's
[L1437] [49:26.16] not that sophisticated
[L1438] [49:28.08] I think it provides like a bit of
[L1439] [49:29.36] calibration on what matters right like
[L1440] [49:31.68] you know the details matter But the
[L1441] [49:33.60] details don't have to be complicated.
[L1442] [49:35.92] >> Before all this uh large model robotics
[L1443] [49:39.36] kind of uh wave prior to that um Boston
[L1444] [49:43.92] Dynamics had these really impressive
[L1445] [49:46.56] demonstrations and tons of um mind
[L1446] [49:50.16] share. I guess I wasn't even in the
[L1447] [49:52.08] field by saying wow they're really doing
[L1448] [49:55.20] incredible robotics. And then in the
[L1449] [49:58.16] last I don't know how many years I don't
[L1450] [50:00.88] really hear about them much anymore. Um
[L1451] [50:04.64] is there some shift in the industry that
[L1452] [50:08.08] made that so or you know is that
[L1453] [50:10.32] something you could explain?
[L1454] [50:12.16] >> So the way I would explain it is this
[L1455] [50:13.68] that um there are you know robotics
[L1456] [50:18.24] at at some level is about building
[L1457] [50:19.68] complex systems. So um even though it
[L1458] [50:23.52] kind of it's very tempting to say like
[L1459] [50:25.36] oh there's different areas of AI there's
[L1460] [50:27.60] like LLMs and vision and robotics one of
[L1461] [50:30.08] those is not like the others because for
[L1462] [50:31.44] robots you actually need like all the
[L1463] [50:32.88] parts everything from like how you you
[L1464] [50:36.00] know uh how you wire up the robot what
[L1465] [50:38.32] the power source is what does the
[L1466] [50:39.68] actuator look like all the way to how
[L1467] [50:42.08] does it do like high level planning to
[L1468] [50:43.76] determine like what task to do next and
[L1469] [50:47.68] even though it's kind even though we
[L1470] [50:49.12] could look at these things and say like
[L1471] [50:50.24] oh all of these different videos and
[L1472] [50:52.24] different companies and different demos.
[L1473] [50:53.44] They're all robotics. They're really
[L1474] [50:55.04] kind of a different parts of the stack.
[L1475] [50:57.36] Um,
[L1476] [50:58.96] a lot of what the classic Boston
[L1477] [51:01.28] Dynamics results show is um, very
[L1478] [51:04.72] sophisticated hardware, very carefully
[L1479] [51:06.80] designed hardware with a uh, traditional
[L1480] [51:10.80] control approach with very smart
[L1481] [51:12.96] controls engineers setting everything
[L1482] [51:14.24] up, but with comparatively less emphasis
[L1483] [51:17.28] on the kind of decision-m aspect and I
[L1484] [51:20.56] think that there, you know, at a
[L1485] [51:21.84] particular point in time that actually
[L1486] [51:22.88] made a lot of sense because we can't
[L1487] [51:24.16] build the physical body like it doesn't
[L1488] [51:26.00] matter what kind of decision making
[L1489] [51:27.12] system is running on it. Um
[L1490] [51:30.32] but uh to our earlier discussion about
[L1491] [51:32.64] generalization,
[L1492] [51:34.16] you know, at this point we're at a stage
[L1493] [51:36.24] in the development of these things that
[L1494] [51:39.68] even though we can do more on hardware,
[L1495] [51:42.16] in many ways it's good enough. And the
[L1496] [51:44.24] big challenge is how to have the
[L1497] [51:45.84] decision-making loop that actually works
[L1498] [51:47.84] and that reacts intelligently to
[L1499] [51:50.64] everything in the environment. And the
[L1500] [51:52.40] way and the place where I would draw the
[L1501] [51:53.76] the dividing line between those is
[L1502] [51:56.80] it's like decision-m loop doesn't mean
[L1503] [51:58.80] symbolic decisions. It could mean
[L1504] [52:00.08] low-level decisions. The question is do
[L1505] [52:02.32] you need to take the rest of the
[L1506] [52:03.36] environment into account or are you just
[L1507] [52:05.28] dealing with the robot? So if you want
[L1508] [52:06.80] to do a backflip on flat ground, you
[L1509] [52:08.56] most have to deal with the robot. But if
[L1510] [52:10.48] you want to pick up a coffee cup off of
[L1511] [52:12.64] a table, even though that's maybe in
[L1512] [52:14.64] some ways simpler than doing a backflip,
[L1513] [52:16.24] you really have to understand what's
[L1514] [52:17.36] going on in the rest of the world rather
[L1515] [52:18.80] than just your own body. And that
[L1516] [52:21.36] dividing line, I think the way the
[L1517] [52:23.04] technology has panned out, I think it's
[L1518] [52:25.60] fair to say that that is the dividing
[L1519] [52:26.96] line between AI and controls. Like
[L1520] [52:29.44] controls is when you have to control the
[L1521] [52:32.16] robot body. AI is when you have to take
[L1522] [52:34.08] into account what goes on outside of the
[L1523] [52:36.08] robot.
[L1524] [52:37.84] and and and I think that that's why you
[L1525] [52:39.52] see this divide because I think a lot of
[L1526] [52:41.20] the demos where you mostly needed to
[L1527] [52:44.00] deal with the robot itself and not the
[L1528] [52:45.52] rest of the world really good controls
[L1529] [52:48.32] could allow you to could admit a very
[L1530] [52:49.92] good solution there a and you know
[L1531] [52:51.84] another thing I would say here is like
[L1532] [52:53.76] okay if there's a lot of controls work
[L1533] [52:55.44] that goes into doing some particular
[L1534] [52:58.16] skill well there is actually something
[L1535] [53:00.00] to learn from that because if you can
[L1536] [53:03.52] handdesign a controller that performs a
[L1537] [53:05.60] sophisticated behavior very likely you
[L1538] [53:07.60] can also learn that controller. So like
[L1539] [53:09.28] just that proof of existence that the
[L1540] [53:11.04] thing is possible and not only possible
[L1541] [53:13.36] but also simple enough that a person
[L1542] [53:15.04] could build it because remember people
[L1543] [53:16.72] are you know at the end of the day even
[L1544] [53:18.80] even with code these days the kind of
[L1545] [53:20.64] complexity that people can handle is not
[L1546] [53:22.08] as high as the kind of complexity the AI
[L1547] [53:23.60] can handle. So if a person can
[L1548] [53:24.72] handdesign something uh to do a backflip
[L1549] [53:27.36] or do some acrobatics that's a really
[L1550] [53:29.84] great proof of existence that there
[L1551] [53:31.20] exists some relatively parsimmonious
[L1552] [53:32.96] control law for doing that skill and
[L1553] [53:34.72] parsimonious does mean generalizable. So
[L1554] [53:36.88] if it's simple enough for a person to
[L1555] [53:38.32] design, probably there's something
[L1556] [53:39.68] fairly general in there and if you can
[L1557] [53:41.12] learn it uh and automate it without
[L1558] [53:43.04] having to have the human controls
[L1559] [53:44.64] engineers in the loop, that's that's
[L1560] [53:46.80] good news.
[L1561] [53:48.00] >> And then last question for you is you if
[L1562] [53:50.48] you could go back to when you just
[L1563] [53:52.00] entered the industry and give yourself
[L1564] [53:53.84] some advice knowing everything you know
[L1565] [53:55.60] now, what would you say?
[L1566] [53:57.76] One thing that I've learned uh over the
[L1567] [53:59.84] last uh few years um which I think is a
[L1568] [54:03.12] little different than kind of my
[L1569] [54:04.08] original mindset is I think that
[L1570] [54:06.64] addressing robotics effectively requires
[L1571] [54:09.52] using um very broad prior knowledge. And
[L1572] [54:14.00] I think that there there's this idea
[L1573] [54:15.36] that a lot of people in robotic learning
[L1574] [54:18.16] have which I think I I shared initially
[L1575] [54:19.84] that you know since people learn things
[L1576] [54:22.64] kind of from scratch maybe robots should
[L1577] [54:24.64] learn things from scratch too. Um so uh
[L1578] [54:27.20] like for example uh in um some of our
[L1579] [54:30.24] early work on large scale robotic
[L1580] [54:31.76] learning at Google we uh we had this uh
[L1581] [54:34.72] what we call the the arm farm project
[L1582] [54:36.88] like we set up a bunch of robot arms in
[L1583] [54:38.96] a in a conference room actually because
[L1584] [54:41.12] we didn't have a proper lab but it was a
[L1585] [54:43.12] conference room and we had them all like
[L1586] [54:44.64] grasping objects and the idea was well
[L1587] [54:46.88] if they grasp like millions of objects
[L1588] [54:48.72] they'll learn very general like grasping
[L1589] [54:50.40] strategies and it basically worked like
[L1590] [54:52.64] they could learn to grasp objects but it
[L1591] [54:54.40] was very hard to like take get further
[L1592] [54:56.08] from that to the next level. So, okay,
[L1593] [54:57.44] now I can pick up anything, but like so
[L1594] [54:58.88] what? Uh can like it it didn't serve as
[L1595] [55:01.52] a very good stepping stone for more
[L1596] [55:02.88] complex skills. And I think part of that
[L1597] [55:04.88] was that we were approaching this like
[L1598] [55:06.40] very blank slate like let's start from
[L1599] [55:08.16] zero and see if knowing nothing in
[L1600] [55:10.00] advance the robot could start picking up
[L1601] [55:11.68] behaviors. But I think that it's much
[L1602] [55:14.64] much more practical to get all this to
[L1603] [55:16.40] work if you can combine robot experience
[L1604] [55:18.56] with knowledge that you can pull in from
[L1605] [55:20.00] other sources. Like for example, I was
[L1606] [55:21.68] very skeptical initially about the
[L1607] [55:23.76] utility of language and I think
[L1608] [55:26.80] scientifically this is defensible which
[L1609] [55:28.56] is that like hey um you know like
[L1610] [55:31.20] animals can do some pretty impressive
[L1611] [55:32.56] things like monkeys can do really cool
[L1612] [55:34.08] stuff but monkeys as far as I know can't
[L1613] [55:36.64] speak at least not very eloquently um so
[L1614] [55:39.36] maybe our robots should also be able to
[L1615] [55:40.72] do stuff and they don't necessarily need
[L1616] [55:42.00] to understand language but I think the
[L1617] [55:44.40] subtlety there is what's important is
[L1618] [55:46.24] not language it's it's
[L1619] [55:49.36] prior knowledge that you can put in as a
[L1620] [55:51.52] scaffold on your learning process. And
[L1621] [55:54.00] you can pull in that knowledge in all
[L1622] [55:55.28] sorts of ways. Like, you know, humans
[L1623] [55:56.72] don't necessarily pull that in entirely
[L1624] [55:58.16] through language. Humans all and monkeys
[L1625] [56:00.08] certainly don't. Uh they do it from
[L1626] [56:02.24] observation, from observing other
[L1627] [56:03.92] people, other creatures and so on. So,
[L1628] [56:05.36] there's lots of sources of prior
[L1629] [56:06.24] knowledge. But the point is that you got
[L1630] [56:07.20] to get that prior knowledge in there.
[L1631] [56:08.64] Otherwise, you're actually faced with a
[L1632] [56:09.92] harder problem than what humans and
[L1633] [56:11.84] animals have to solve. Because like, you
[L1634] [56:13.92] know, if a person had to figure out how
[L1635] [56:15.68] to like assemble IKEA furniture, but
[L1636] [56:17.60] they've never actually encountered any
[L1637] [56:19.44] article of furniture in their entire
[L1638] [56:20.88] life, like [laughter]
[L1639] [56:22.56] okay, that would be like pretty
[L1640] [56:23.52] difficult because they don't even know
[L1641] [56:24.48] what like what the point of this is or
[L1642] [56:26.40] what the the endgame looks like. Uh so
[L1643] [56:28.80] yeah, prior knowledge is important. And
[L1644] [56:30.40] while I'm still a big fan of learning
[L1645] [56:32.40] things through experience, I think that,
[L1646] [56:34.16] you know, my advice to myself would have
[L1647] [56:35.76] been take prior knowledge more
[L1648] [56:37.12] seriously.
[L1649] [56:38.16] >> Awesome. Well, thank you so much for
[L1650] [56:39.68] your time, Sergey. I really appreciate
[L1651] [56:40.88] it.
[L1652] [56:41.12] >> Yeah, thank you for your questions. Hey,
[L1653] [56:42.80] thank you for watching this podcast. If
[L1654] [56:44.32] you liked it and you want to see the
[L1655] [56:45.60] show grow, please support with a comment
[L1656] [56:47.92] or a like. Also, if you have any
[L1657] [56:50.56] recommendations for people you want me
[L1658] [56:52.24] to bring on, please drop a comment.
[L1659] [56:54.80] Guests like Barbara Liskov, Mike
[L1660] [56:56.96] Stonereaker, Mark Brooker, these were
[L1661] [56:59.44] all people that I brought on because
[L1662] [57:01.44] someone left a comment. On another note,
[L1663] [57:03.68] aside from the podcast, I'm working on
[L1664] [57:05.60] building the ergonomic keyboard that I
[L1665] [57:07.44] wish existed. Here's a glance at the
[L1666] [57:09.68] prototype. It's a split keyboard, so
[L1667] [57:11.92] there's two sides. This is in the case,
[L1668] [57:14.32] but yeah, we launched on Kickstarter and
[L1669] [57:16.40] we hit our goal within eight hours of
[L1670] [57:18.24] launching. I really appreciate it if you
[L1671] [57:20.00] were one of the people who grabbed one
[L1672] [57:21.44] of the early units. Um, we're now
[L1673] [57:23.60] working on the long journey of building
[L1674] [57:25.36] the tooling now. And so, if you still
[L1675] [57:27.04] want to pick one up, I've left the late
[L1676] [57:29.20] pledges open on Kickstarter, so you can
[L1677] [57:31.60] grab one there. I'll put a link in the
[L1678] [57:33.36] description. Thank you again for
[L1679] [57:35.52] watching the podcast and I'll see you in
[L1680] [57:37.76] the next
