Chunk 5; segments 1352–1512. Start may repeat the previous chunk for context.

# Turing Award Winner: TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC | David Patterson

Source ID: source-fc9308e696a718d4
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_TPU_vs_GPU_vs_CPU,_Computer_Architecture,_RISC_vs_CISC_David_Patterson_en.txt
Video: https://www.youtube.com/watch?v=Pn4ZwlEh5nw

[L1361] [53:08.16] just let them get away with it and then
[L1362] [53:10.72] um and then and you know it's a little
[L1363] [53:13.92] bit confrontational
[L1364] [53:15.12] But, you know, as long as people all
[L1365] [53:17.28] agree that, you know, this is for the
[L1366] [53:18.88] greater good, we're going to we we need
[L1367] [53:20.64] to get the right ideas out there. And
[L1368] [53:22.56] so, let's argue about the ideas to to
[L1369] [53:25.04] see uh you know, polish them to make
[L1370] [53:28.16] them stronger. Uh I think that's
[L1371] [53:30.64] important in science, in engineering, um
[L1372] [53:33.44] and kind of uh in life too. There's a
[L1373] [53:36.64] lot of stuff going on right now in the
[L1374] [53:40.00] country that uh is worrisome and uh I've
[L1375] [53:44.00] certainly stood up and wrote opeds about
[L1376] [53:47.20] things that I think are wrong and need
[L1377] [53:48.96] to be corrected and uh you know if
[L1378] [53:51.36] people are afraid to do that
[L1379] [53:54.00] it's hard to be um optimistic about the
[L1380] [53:56.72] future if people are afraid to stand up
[L1381] [53:58.24] when when there's wrongs and uh try and
[L1382] [54:01.36] stop them. You also mentioned optimism
[L1383] [54:04.08] in the talk and you had this story I
[L1384] [54:06.16] wonder if you're willing to
[L1385] [54:07.52] >> sure. [laughter] So I would say in
[L1386] [54:09.84] engineering uh you know it's it's hard
[L1387] [54:12.80] to know right uh but I think you need to
[L1388] [54:14.88] be kind of optimistic or positive have a
[L1389] [54:17.52] positive outlook because so many things
[L1390] [54:19.28] could go wrong and then so my story
[L1391] [54:21.84] personal story that illustrates it's
[L1392] [54:23.36] going back to high school when I'm 16
[L1393] [54:25.76] I'm dating this very attractive girl and
[L1394] [54:28.08] I screw up my courage and ask her if we
[L1395] [54:31.60] would be exclusive at the time we the
[L1396] [54:33.60] phrase we used was going steady and she
[L1397] [54:36.08] looked at me and said And you know, she
[L1398] [54:38.56] was 16. She had dated other guys and
[L1399] [54:41.20] thought we were pretty young. And she
[L1400] [54:42.64] said, "Well, Dave, you're such a nice
[L1401] [54:44.48] guy. I don't know how to say no." For
[L1402] [54:46.56] me, as a logical person, I don't know.
[L1403] [54:48.96] Sounded like a yes. And so I hugged her
[L1404] [54:51.52] and said, "Great." And so she uh she in
[L1405] [54:55.20] her mind, she thought, "Well, I'll let
[L1406] [54:56.72] him down gently later." But we've been
[L1407] [54:58.72] married 59 years now, and she she hasn't
[L1408] [55:03.20] let me down yet. So that was a case
[L1409] [55:04.96] where optimism uh paid off.
[L1410] [55:07.20] >> I think everyone that hears a a healthy
[L1411] [55:10.24] relationship for that long, they might
[L1412] [55:11.92] wonder how you did it.
[L1413] [55:13.60] >> I used to tell people uh you know if you
[L1414] [55:16.56] go to if you go to weddings, the
[L1415] [55:18.48] marriage vows are really great, right?
[L1416] [55:20.96] But nobody can remember their wedding
[L1417] [55:22.08] vows. I used to say remember your
[L1418] [55:23.12] wedding vows, but nobody remembered
[L1419] [55:24.08] that. So we boiled it down to nine magic
[L1420] [55:26.48] words and it's just three sentences and
[L1421] [55:28.88] they start IU, I got to say all three
[L1422] [55:31.52] and it's I was wrong. you were right. I
[L1423] [55:34.80] love you. Okay, those are the those nine
[L1424] [55:37.20] words. And this applies to both both
[L1425] [55:40.40] partners in a relationship, not just one
[L1426] [55:42.64] partner. Uh but yeah, if you can say
[L1427] [55:44.96] them all and no substitutions, I was
[L1428] [55:46.64] wrong, you're right, you're a jerk. You
[L1429] [55:48.08] know, you can't do that. It's if you can
[L1430] [55:50.32] remember those nine words, that can help
[L1431] [55:51.68] you have a a long relationship like uh
[L1432] [55:54.96] my wife and I have. And then last
[L1433] [55:57.44] question for you, like knowing
[L1434] [55:59.20] everything you know now from your
[L1435] [56:00.88] career, if you could go back to yourself
[L1436] [56:03.36] when you had just entered the industry
[L1437] [56:05.76] and give yourself advice, what would you
[L1438] [56:08.08] say?
[L1439] [56:09.44] >> I mean, I think when I got here because
[L1440] [56:12.08] you know the imposttor syndrome, I was a
[L1441] [56:14.32] UCLA
[L1442] [56:15.92] graduate student and suddenly I'm a
[L1443] [56:17.36] Berkeley professor. So that just doesn't
[L1444] [56:19.36] seem like that was very intimidating.
[L1445] [56:22.16] But I after a while I just thought well
[L1446] [56:24.16] I'm probably not gonna get tenure so I
[L1447] [56:25.60] should just have a good time. So I think
[L1448] [56:26.96] I already I already had a right attitude
[L1449] [56:31.52] about it. I think that first year I
[L1450] [56:33.68] think it it was very stressful for my
[L1451] [56:36.48] while I was trying to handle the
[L1452] [56:38.32] imposttor syndrome and be a Berkeley
[L1453] [56:39.92] professor but I think after that I
[L1454] [56:41.44] handled it pretty well. I you know I I
[L1455] [56:44.00] did all the things with the kids and
[L1456] [56:45.20] stuff. So uh there's a version of that
[L1457] [56:48.16] question is like is there anything I
[L1458] [56:49.76] would do over again? There's one thing I
[L1459] [56:51.44] would have I was chair of the u of this
[L1460] [56:55.36] the architecture community the sig arch
[L1461] [56:57.68] as it's called and they have an annual
[L1462] [56:59.44] conference of the year and I was this
[L1463] [57:02.24] was in the 1990s I think I was the chair
[L1464] [57:06.88] and what I wasn't aware is at these
[L1465] [57:09.44] conferences there were men who were
[L1466] [57:11.20] harassing young women at this uh
[L1467] [57:14.00] conference I just didn't think you know
[L1468] [57:18.16] people like you know young people people
[L1469] [57:21.04] like me nobody would do that only an
[L1470] [57:23.36] idiot would do that can't possibly be
[L1471] [57:25.20] happening but it was happening and I
[L1472] [57:27.12] wish I somebody had said something to me
[L1473] [57:29.92] about it uh and because I would have I
[L1474] [57:33.04] would have straightened out any man
[L1475] [57:34.72] doing I would have threatened his life
[L1476] [57:37.20] if he were to do that today the only
[L1477] [57:39.44] comforting thing is Serita a who is a
[L1478] [57:42.96] famous computer architect uh she said
[L1479] [57:45.60] she also was not aware that that was
[L1480] [57:47.84] going on it became clear later you know
[L1481] [57:50.32] I mean uh uh five or 10 years later it
[L1482] [57:52.96] became more clear that this was going on
[L1483] [57:54.40] and there were mechanisms but that's the
[L1484] [57:56.48] one thing I wish you know if I could go
[L1485] [57:58.40] back in time I would have figured that
[L1486] [58:01.36] out and I would have straightened men
[L1487] [58:03.68] out who were doing that and they
[L1488] [58:05.68] wouldn't that would have stopped I
[L1489] [58:07.04] believe that would have stopped them
[L1490] [58:08.48] >> yeah [laughter]
[L1491] [58:10.16] thank you so much for your time today I
[L1492] [58:11.76] really appreciate it
[L1493] [58:13.04] >> all right and thanks for the interview
[L1494] [58:15.28] >> hey thank you for watching this podcast
[L1495] [58:16.88] if you liked it and you want to see the
[L1496] [58:18.32] show grow Please support with a comment
[L1497] [58:20.72] or a like. Also, if you have any
[L1498] [58:23.28] recommendations for people you want me
[L1499] [58:24.96] to bring on, please drop a comment.
[L1500] [58:27.60] Guests like Barbara Liskoff, Mike
[L1501] [58:29.76] Stonereaker, Mark Brooker, these were
[L1502] [58:32.24] all people that I brought on because
[L1503] [58:34.16] someone left a comment. On another note,
[L1504] [58:36.48] aside from the podcast, I'm working on
[L1505] [58:38.32] building the ergonomic keyboard that I
[L1506] [58:40.24] wish existed. Here's a glance at the
[L1507] [58:42.40] prototype. It's a split keyboard, so
[L1508] [58:44.64] there's two sides. um this isn't the
[L1509] [58:46.88] case, but yeah, we launched on
[L1510] [58:48.32] Kickstarter and we hit our goal within 8
[L1511] [58:50.56] hours of launching. I really appreciate
[L1512] [58:52.32] it if you were one of the people who
[L1513] [58:53.68] grabbed one of the early units. Um we're
[L1514] [58:56.16] now working on the long journey of
[L1515] [58:57.84] building the tooling now and so if you
[L1516] [58:59.60] still want to pick one up, I've left the
[L1517] [59:01.68] late pledges open on Kickstarter, so you
[L1518] [59:04.32] can grab one there. I'll put a link in
[L1519] [59:05.92] the description. Thank you again for
[L1520] [59:08.24] watching the podcast and I'll see you in
[L1521] [59:10.48] the next
