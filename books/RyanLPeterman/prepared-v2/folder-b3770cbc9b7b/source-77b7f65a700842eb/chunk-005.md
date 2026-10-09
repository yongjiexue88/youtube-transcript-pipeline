Chunk 5; segments 1259–1606. Start may repeat the previous chunk for context.

# Instagram iOS Principal Eng (IC8): Building IG Stories, 1 Promo Per Half, Small Teams

Source ID: source-77b7f65a700842eb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Instagram_iOS_Principal_Eng_(IC8)_Building_IG_Stories,_1_Promo_Per_Half,_Small_Teams_en.txt
Video: https://www.youtube.com/watch?v=gpVETZnY9Y0

[L1268] [51:50.88] talented group um great engineers, great
[L1269] [51:53.68] designers. Uh we moved super quickly. I
[L1270] [51:57.36] mean the product doesn't exist anymore
[L1271] [51:58.96] today. it didn't it didn't end up doing
[L1272] [52:00.96] that well. And it's kind of interesting
[L1273] [52:02.64] to reflect on why I think like it had
[L1274] [52:05.28] some things that uh ended up becoming
[L1275] [52:08.56] the future like vertical video is very
[L1276] [52:10.80] much a thing today. Um but it was kind
[L1277] [52:13.28] of trying to mix like this long form
[L1278] [52:15.84] YouTube style content into this vertical
[L1279] [52:18.24] format and maybe that was a bit of a
[L1280] [52:20.16] mismatch. Uh people just weren't
[L1281] [52:23.12] producing highquality long form in the
[L1282] [52:26.80] vertical format. We tried some
[L1283] [52:30.80] interesting AI techniques to take
[L1284] [52:33.20] landscape content and reformat it for
[L1285] [52:35.84] vertical. I've got a patent on that.
[L1286] [52:37.84] That's kind of one of my more
[L1287] [52:39.20] interesting patents. Um [clears throat]
[L1288] [52:41.92] but uh we showed that to create video
[L1289] [52:45.20] creators and they were like horrified.
[L1290] [52:46.88] They were like, "You're destroying my
[L1291] [52:48.40] content. Like why? I've spent so long
[L1292] [52:50.16] making this nice landscape video now.
[L1293] [52:52.32] You've just ruined it." So, we tried to
[L1294] [52:54.48] push people to produce this original
[L1295] [52:56.72] long- form vertical video. And I think
[L1296] [52:58.40] the inventory just never really showed
[L1297] [53:00.88] up. And there was maybe a little bit of
[L1298] [53:02.88] hubris. It was like, you know, Instagram
[L1299] [53:05.60] can just change the industry. We can
[L1300] [53:07.76] just people will just start making this
[L1301] [53:10.08] because we have this platform, this
[L1302] [53:11.92] audience. And that didn't totally
[L1303] [53:14.16] materialize. So, I think it probably did
[L1304] [53:17.36] inform a lot of like, you know, what
[L1305] [53:19.20] ultimately shipped as as reals. Um but
[L1306] [53:23.52] uh yeah, IGTV itself didn't didn't
[L1307] [53:26.64] totally work out.
[L1308] [53:27.92] >> Yeah, I was cuz I was working on the
[L1309] [53:29.92] like video infrastructure team at the
[L1310] [53:31.76] time. So actually that was one of the
[L1311] [53:33.76] things that I got plugged into at some
[L1312] [53:35.36] point. I remember the energy in the San
[L1313] [53:38.24] Francisco office and the war rooms etc.
[L1314] [53:41.12] >> Yeah, totally.
[L1315] [53:42.40] >> You mentioned antitrust and what's the
[L1316] [53:45.12] antirust component you're talking about?
[L1317] [53:47.44] a lot of the sort of internal
[L1318] [53:50.08] communication has now become public
[L1319] [53:52.00] through this antirust uh lawsuit where
[L1320] [53:56.96] um the Justice Department I think is is
[L1321] [54:00.24] suing Facebook to unwind the Instagram
[L1322] [54:03.44] acquisition. Um, and so certain things
[L1323] [54:07.44] that were kind of confusing to me at the
[L1324] [54:09.36] time, like why why were certain things
[L1325] [54:11.76] happening, um, are less confusing now
[L1326] [54:14.96] that I read some of the the internal
[L1327] [54:17.84] communications that was previously
[L1328] [54:19.28] private, including private to me. You
[L1329] [54:21.20] know, I didn't I wasn't exposed, uh, to
[L1330] [54:24.00] it. But, um, yeah, I mean, I think
[L1331] [54:26.32] basically
[L1332] [54:27.84] Instagram, you know, had been acquired.
[L1333] [54:30.24] It was it was smaller,
[L1334] [54:33.28] certainly small relative to Facebook and
[L1335] [54:36.00] then had gone through several years of
[L1336] [54:38.00] just incredible growth and now was kind
[L1337] [54:43.12] of more of like a peer to Facebook and
[L1338] [54:46.88] was kind of like the new popular kid
[L1339] [54:50.32] terms of like you know the Instagram
[L1340] [54:51.92] stories was received better than the
[L1341] [54:54.48] stories in Facebook. And so I think that
[L1342] [54:58.24] created some tension between the
[L1343] [55:00.80] Instagram leadership and the Facebook
[L1344] [55:02.40] leadership. And there was concerns about
[L1345] [55:05.68] Instagram cannibalizing or taking users
[L1346] [55:08.40] from Facebook. Um
[L1347] [55:11.60] which yeah just kind of guided some of
[L1348] [55:14.40] the the
[L1349] [55:16.64] strategy decisions I guess. I remember
[L1350] [55:19.12] that too because I was I mean I was also
[L1351] [55:20.88] on the Instagram team and I remember
[L1352] [55:23.04] there was some confusion about you know
[L1353] [55:25.36] why are we turning off the I guess
[L1354] [55:28.72] somehow like followers were being
[L1355] [55:30.48] forwarded from Facebook to Instagram or
[L1356] [55:33.20] was like cross sharing or something like
[L1357] [55:35.12] the direction from Facebook to Instagram
[L1358] [55:37.68] was getting turned off or something like
[L1359] [55:39.28] that and yeah I think I read the same
[L1360] [55:41.92] thing you read because I was like oh
[L1361] [55:43.44] this makes so much sense it's like Mark
[L1362] [55:45.44] Zuckerberg's internal memo on you know
[L1363] [55:48.56] all of that and all the tensions between
[L1364] [55:51.84] you know the Instagram founders Mark and
[L1365] [55:54.24] he's saying
[L1366] [55:55.04] >> he wants to keep them and they're great
[L1367] [55:56.88] at building products but you know he's
[L1368] [55:59.52] like trying to navigate his side of the
[L1369] [56:01.92] equation. Super interesting.
[L1370] [56:03.92] >> It'd be really interesting to know how
[L1371] [56:06.80] you know how he thinks about it today.
[L1372] [56:09.36] Uh that was now seven years ago.
[L1373] [56:12.64] >> Mark or the Instagram founders? Mark. Um
[L1374] [56:16.64] because I sense in those communications
[L1375] [56:20.40] like something of a very understandable
[L1376] [56:23.92] emotional attachment to the Facebook
[L1377] [56:25.84] product, right? This was like kind of
[L1378] [56:27.60] the thing that he created and Instagram.
[L1379] [56:30.40] He deserves all the credit for acquiring
[L1380] [56:32.56] it, but it was a little bit less his
[L1381] [56:34.56] thing. Um,
[L1382] [56:37.12] and yeah, I just wonder, uh, does he
[L1383] [56:40.80] view that differently today than he did
[L1384] [56:44.40] now? Uh, you know, seven years on, um,
[L1385] [56:48.16] he owns both of these things. Um, I
[L1386] [56:51.76] always had the view that like the best
[L1387] [56:54.72] the way to get the best outcome for the
[L1388] [56:57.84] overall company was actually to have
[L1389] [57:00.56] these things compete with each other
[L1390] [57:02.24] because it's like you own both. they're
[L1391] [57:04.24] going to make each other better and you
[L1392] [57:06.08] know one of them will win versus like if
[L1393] [57:07.84] you don't if you [clears throat] kind of
[L1394] [57:09.44] stifle that competition
[L1395] [57:11.60] somebody from the outside is like more
[L1396] [57:13.68] likely to come up with something better
[L1397] [57:15.60] and and take over. [snorts] Um but uh
[L1398] [57:20.32] yeah I don't know I mean he's the one
[L1399] [57:22.64] running a multi-trillion dollar company
[L1400] [57:24.56] and [laughter] I'm not so arm armchair
[L1401] [57:27.76] CEOing over here.
[L1402] [57:30.24] >> Yeah. Maybe one day if this podcast
[L1403] [57:32.72] scales up and I ever have Mark on, I'll
[L1404] [57:35.28] I'll ask him that. [laughter]
[L1405] [57:37.36] >> And then lastly at Instagram, I know you
[L1406] [57:40.40] started a group called IG Labs. I'm
[L1407] [57:42.96] curious the story behind you starting
[L1408] [57:45.04] that group and I also understand this is
[L1409] [57:47.52] your promo to IC8 or like director
[L1410] [57:50.72] equivalent at Instagram. So yeah, what's
[L1411] [57:53.28] the story behind IGLabs? after IGTV. Um,
[L1412] [57:59.04] definitely spent some time like Thomas
[L1413] [58:02.32] Simpson has this phrase like wandering
[L1414] [58:04.00] the impact desert like just looking for
[L1415] [58:08.08] for things to do and and not necessarily
[L1416] [58:11.68] finding anything great. Um, and I was
[L1417] [58:14.48] actually pretty close to to leaving the
[L1418] [58:17.04] company at that time. Um, [snorts]
[L1419] [58:20.32] and kind of the new effort became reals
[L1420] [58:24.08] and I didn't feel good about working on
[L1421] [58:26.72] like passive video consumption. Um, my
[L1422] [58:29.28] manager was was over the reals or so, so
[L1423] [58:32.72] it, you know, would have made sense for
[L1424] [58:34.32] me to work on it, but I was I was fairly
[L1425] [58:36.96] certain I I I didn't want to work on
[L1426] [58:39.04] that. I I helped the team a bit, but
[L1427] [58:41.20] like um yeah, it wasn't going to be my
[L1428] [58:43.92] project. Through that time, there was a
[L1429] [58:46.32] lot of like culture change. the founders
[L1430] [58:48.48] had left. Um, you know, the leadership
[L1431] [58:51.60] kind of came over from Facebook,
[L1432] [58:55.28] uh, the new leadership. Um, a lot of
[L1433] [58:58.56] kind of like the old Instagram culture,
[L1434] [59:00.72] it felt like was being kind of pushed
[L1435] [59:02.56] out.
[L1436] [59:04.08] And I was talking with like the the new
[L1437] [59:08.64] head of engineering um [snorts] about
[L1438] [59:12.80] trying to bring back some of that energy
[L1439] [59:15.28] that I think had made product
[L1440] [59:17.12] development at Instagram special, small
[L1441] [59:20.08] teams, attention to craft, uh and also
[L1442] [59:23.60] really expanding
[L1443] [59:25.60] kind of the
[L1444] [59:27.68] the scope of what we worked on. So, you
[L1445] [59:32.40] know, we were very focused on like the
[L1446] [59:34.96] existing Instagram app and the existing
[L1447] [59:36.96] features within Instagram and just kind
[L1448] [59:38.88] of like iterative features on that, very
[L1449] [59:41.92] like incremental improvements. And I
[L1450] [59:45.68] kind of made this pitch that like we
[L1451] [59:47.12] have this great brand um we could do
[L1452] [59:50.00] other things under the Instagram brand
[L1453] [59:51.92] like let's let's go try that. let's, you
[L1454] [59:54.88] know, explore like location ideas, maps
[L1455] [59:58.64] ideas, uh, places. Um, and again, paire
[L1456] [01:00:03.92] paired with a really awesome designer,
[L1457] [01:00:06.64] uh, Vivian Wong. And, um, we, yeah, made
[L1458] [01:00:10.88] the pitch to to start this team. It was
[L1459] [01:00:12.88] just her and myself in the beginning.
[L1460] [01:00:15.36] And uh the idea was just to have kind of
[L1461] [01:00:18.64] this like Delta Force like small group,
[L1462] [01:00:21.68] very high talent density that would work
[L1463] [01:00:23.84] on new product initiatives and things
[L1464] [01:00:26.00] that just didn't slot cleanly into the
[L1465] [01:00:28.64] org. Like Instagram had grown to such a
[L1466] [01:00:31.60] size where you really needed like a lot
[L1467] [01:00:34.80] of structure in the org just to keep
[L1468] [01:00:37.04] things sane. But that meant that
[L1469] [01:00:40.08] projects that like didn't slot cleanly
[L1470] [01:00:42.88] into one of those orgs were probably
[L1471] [01:00:45.28] underinvested in. And so part of the
[L1472] [01:00:47.84] idea of this team was that we would span
[L1473] [01:00:49.84] across, you know, we wouldn't have a
[L1474] [01:00:52.08] focus area. We could kind of work work
[L1475] [01:00:54.64] across many things. Um
[L1476] [01:00:57.44] we we tried a lot. I mean, a lot of it
[L1477] [01:00:59.68] didn't ship or tested. Um, probably one
[L1478] [01:01:02.96] of the more lasting impactful things, it
[L1479] [01:01:06.80] it seems small, but I think it actually
[L1480] [01:01:08.40] gets used quite a bit is the
[L1481] [01:01:09.60] collaborative post feature where uh you
[L1482] [01:01:12.48] can have multiple authors on a post. Um,
[L1483] [01:01:15.28] it's another of the more interesting
[L1484] [01:01:17.76] patents I have is is on that one. Um and
[L1485] [01:01:22.32] uh and so yeah, I think I think we found
[L1486] [01:01:24.24] good impact and then we were also this
[L1487] [01:01:25.68] concentration of talent that like when
[L1488] [01:01:27.28] there was a new important initiative
[L1489] [01:01:29.60] ultimately ended up being threads um you
[L1490] [01:01:32.88] had this group that that could go work
[L1491] [01:01:34.40] on it and uh and yeah just trying to uh
[L1492] [01:01:38.64] I don't know kind of encourage
[L1493] [01:01:40.80] innovation trying new things and and
[L1494] [01:01:43.20] push that at the company. The last thing
[L1495] [01:01:45.44] at your on your Instagram journey was
[L1496] [01:01:47.68] that you tried management at some point
[L1497] [01:01:50.32] or as an ICA you switched to I guess
[L1498] [01:01:53.20] TLDD or tech lead director. What was
[L1499] [01:01:56.96] your thinking behind that and how'd it
[L1500] [01:01:58.40] go?
[L1501] [01:01:58.96] >> It's a very unusual or rare role within
[L1502] [01:02:02.48] Facebook. Um even like TLM I think is
[L1503] [01:02:05.28] quite rare or was at the time um than
[L1504] [01:02:09.92] like tech lead director probably even
[L1505] [01:02:11.92] even more so. Um, [snorts]
[L1506] [01:02:15.44] it kind of happened mostly because I had
[L1507] [01:02:18.32] started this group and at some point it
[L1508] [01:02:21.36] just made a lot more sense for me to
[L1509] [01:02:23.20] manage the people in that group rather
[L1510] [01:02:25.68] than my manager who was over the reals
[L1511] [01:02:29.36] or um just less connected to to their
[L1512] [01:02:33.92] work. You know, I could probably
[L1513] [01:02:35.12] represent them better in calibrations. I
[L1514] [01:02:36.88] mean, I was in the calibrations anyways,
[L1515] [01:02:38.80] so I was kind of like doing a lot of
[L1516] [01:02:40.32] this work. So um yeah, in some ways it
[L1517] [01:02:43.52] was just kind of like a formal
[L1518] [01:02:45.04] recognition of like what I was doing
[L1519] [01:02:47.12] already. Um to to have these people
[L1520] [01:02:50.48] report to me. Um Facebook is is very
[L1521] [01:02:54.24] much of the school of thought of like
[L1522] [01:02:57.36] individual contributors and management
[L1523] [01:02:59.04] should be separate and I don't subscribe
[L1524] [01:03:02.88] to that. Um, other companies work
[L1525] [01:03:05.84] differently. Like my wife is a senior
[L1526] [01:03:07.68] staff engineer at Tesla and like um
[L1527] [01:03:10.96] they're very flexible. It's like
[L1528] [01:03:13.92] IC's have people report to them all the
[L1529] [01:03:15.68] time. Um, managers are expected to be
[L1530] [01:03:18.80] like pretty competent uh technical
[L1531] [01:03:22.08] contributors and like doing individual
[L1532] [01:03:23.92] contributions.
[L1533] [01:03:25.44] Um, and I think I prefer that model. Um,
[L1534] [01:03:30.80] and so it was interesting for me to to
[L1535] [01:03:34.00] try it. I think like another one of my
[L1536] [01:03:37.52] sort of controversial opinions is like I
[L1537] [01:03:39.60] think senior engineers should be
[L1538] [01:03:41.36] involved in coding. Um, [clears throat]
[L1539] [01:03:44.16] there's overlap between that thought and
[L1540] [01:03:46.48] like the thought that like um managers
[L1541] [01:03:49.28] should be still somewhat involved.
[L1542] [01:03:52.24] There's
[L1543] [01:03:54.00] an author I I really like, Nasim Talb.
[L1544] [01:03:56.56] Um and he talks about having skin in the
[L1545] [01:04:00.40] game and um yeah, I think like if you're
[L1546] [01:04:03.76] a senior IC who has to do some coding,
[L1547] [01:04:06.32] like you have more skin in the game.
[L1548] [01:04:07.76] Like you're not going to come up with
[L1549] [01:04:09.20] some architecture that like you just
[L1550] [01:04:11.52] hand off to somebody else and it's their
[L1551] [01:04:13.28] problem now, right? Like you're going to
[L1552] [01:04:15.04] be involved. You're going to see more
[L1553] [01:04:17.52] hands-on what the issues are. Um, and I
[L1554] [01:04:21.44] think like similarly like if you're
[L1555] [01:04:23.12] managing a team and you're much more
[L1556] [01:04:24.96] like with them in the day-to-day stuff,
[L1557] [01:04:28.80] uh, I think that you will operate
[L1558] [01:04:31.12] better. So, um, yeah, it's,
[L1559] [01:04:33.71] [clears throat] you know, maybe a bit
[L1560] [01:04:35.52] against the grain at Facebook. Um, but
[L1561] [01:04:38.88] it [clears throat] was a philosophy I
[L1562] [01:04:40.56] had and I wanted to to try it out. Um,
[L1563] [01:04:43.44] and then there was an upside to it as
[L1564] [01:04:46.24] well in a company that grew so much and
[L1565] [01:04:48.72] was so big where
[L1566] [01:04:52.48] at Facebook the levels are are private,
[L1567] [01:04:55.12] right? So you're just a software
[L1568] [01:04:56.80] engineer through through your whole IC
[L1569] [01:05:00.16] time. And in some ways I like that for
[L1570] [01:05:03.28] like engineering discussions that
[L1571] [01:05:04.80] there's no like pulling of rank like hey
[L1572] [01:05:06.64] I'm more senior you know just take my
[L1573] [01:05:08.88] idea like it's a little bit more
[L1574] [01:05:10.88] meritocratic perhaps but in cross
[L1575] [01:05:13.52] functional situations say you're working
[L1576] [01:05:15.44] with like a PM like I'm trying to ship
[L1577] [01:05:18.00] this um [snorts] collaborative post
[L1578] [01:05:20.88] thing and I have to like meet with PM
[L1579] [01:05:24.15] [snorts] all these different PMs on
[L1580] [01:05:25.52] these different teams. Um, there was an
[L1581] [01:05:28.24] element where having a little bit higher
[L1582] [01:05:30.72] of a title I think just made those
[L1583] [01:05:33.36] conversations easier. Like I had a
[L1584] [01:05:35.28] higher baseline where they were like,
[L1585] [01:05:37.12] "Okay, this person like maybe they like
[L1586] [01:05:39.84] know something. They they've been here a
[L1587] [01:05:42.24] bit like they're not just um, you know,
[L1588] [01:05:44.80] totally new." And um you know you you
[L1589] [01:05:48.32] build up some reputation in a company
[L1590] [01:05:50.16] but when it gets so big and there's new
[L1591] [01:05:51.68] people joining all the time like you're
[L1592] [01:05:54.08] actually having to like reestablish that
[L1593] [01:05:55.76] a lot with with folks. So um yeah I
[L1594] [01:05:59.68] think like it it it was somewhat helpful
[L1595] [01:06:01.84] to have that title. There would be
[L1596] [01:06:03.84] discussions in the in the senior
[L1597] [01:06:05.44] engineering group about like should
[L1598] [01:06:07.76] should there be some form of of public
[L1599] [01:06:10.72] levels um within the company and I was
[L1600] [01:06:14.08] supportive of like maybe like a two
[L1601] [01:06:17.04] maybe not like the full level is is
[L1602] [01:06:18.96] public but like there's like a senior
[L1603] [01:06:21.28] designation or something. Um
[L1604] [01:06:23.76] [clears throat] just uh yeah I think
[L1605] [01:06:25.84] largely for like when you're working
[L1606] [01:06:28.08] with people outside of your normal
[L1607] [01:06:30.56] working group so that they start from a
[L1608] [01:06:32.72] slightly better baseline on you know
[L1609] [01:06:35.52] whether whether you know what you're
[L1610] [01:06:37.04] talking about. The [clears throat]
[L1611] [01:06:38.48] number one thing I hear people say is
[L1612] [01:06:40.32] the this is not optimal because it's
[L1613] [01:06:44.88] you're doing two jobs at once and you're
[L1614] [01:06:47.44] gonna drown and your career will not
[L1615] [01:06:49.52] flourish in either direction. What do
