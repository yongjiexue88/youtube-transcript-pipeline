Chunk 5; segments 1365–1495. Start may repeat the previous chunk for context.

# Turing Award Winner: Thinking Clearly, Paxos vs Raft, Working With Dijkstra | Leslie Lamport

Source ID: source-4005a50ded85af4c
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Thinking_Clearly,_Paxos_vs_Raft,_Working_With_Dijkstra_Leslie_Lamport_en.txt
Video: https://www.youtube.com/watch?v=U719vQz-WFs

[L1374] [01:04:45.04] variable you know can be any integer.
[L1375] [01:04:48.48] Now you can implement the program where
[L1376] [01:04:50.24] you have any integer
[L1377] [01:04:52.32] uh but that makes the but talking about
[L1378] [01:04:58.88] you know computer integers would
[L1379] [01:05:00.88] complicate things unnecessarily.
[L1380] [01:05:03.28] The people have this funny idea that you
[L1381] [01:05:05.68] know because something is infinite it's
[L1382] [01:05:07.36] more complicated. They got it backwards.
[L1383] [01:05:10.08] Infinity was introduced to simplify
[L1384] [01:05:13.04] things. You know the first thing you
[L1385] [01:05:15.84] learn is arithmetic.
[L1386] [01:05:18.00] You're learning arithmetic with an
[L1387] [01:05:19.60] infinite number of integers because if
[L1388] [01:05:22.72] you restricted to a finite set of
[L1389] [01:05:24.96] integers, arithmetic becomes much more
[L1390] [01:05:27.28] complicated.
[L1391] [01:05:29.04] So you know the abstractions of
[L1392] [01:05:32.08] mathematics
[L1393] [01:05:34.24] uh which people find you know because
[L1394] [01:05:38.24] they don't have the proper training in
[L1395] [01:05:40.16] mathematics find you know difficult uh
[L1396] [01:05:44.00] are really what's simplifying things and
[L1397] [01:05:46.56] that's what you what you use this
[L1398] [01:05:48.24] mathematics the state machine is
[L1399] [01:05:50.40] described for me by me using mathematics
[L1400] [01:05:54.64] that's the right you know the the most
[L1401] [01:05:57.28] powerful way of doing
[L1402] [01:05:59.44] But
[L1403] [01:06:01.20] computer people and computer scientists
[L1404] [01:06:03.12] and programmers are really hung up on
[L1405] [01:06:06.40] languages
[L1406] [01:06:08.24] and so they are looking for you know
[L1407] [01:06:11.60] they invent all sorts of languages and
[L1408] [01:06:14.00] they're all describable and in fact if
[L1409] [01:06:17.44] you want to give them a semantics you
[L1410] [01:06:19.04] would do it in terms of a state machine
[L1411] [01:06:21.60] and they just think that this uh you
[L1412] [01:06:27.36] know this language ES improves your
[L1413] [01:06:29.60] thinking.
[L1414] [01:06:31.28] uh it doesn't you may I mean there are
[L1415] [01:06:35.12] reasons why you use computer languages
[L1416] [01:06:38.24] and you don't write your your programs
[L1417] [01:06:40.32] code in math and they involve basically
[L1418] [01:06:44.08] efficiency
[L1419] [01:06:45.92] but for understanding you know you can't
[L1420] [01:06:48.32] build math you can't beat math and you
[L1421] [01:06:52.48] know attempts to uh do it by something
[L1422] [01:06:56.32] that looks like a programming language
[L1423] [01:06:59.04] uh is is just the wrong way to to to
[L1424] [01:07:03.60] deal when you're trying to deal with
[L1425] [01:07:05.20] concurrency.
[L1426] [01:07:06.40] >> When I look at uh everything that you've
[L1427] [01:07:09.04] written and all the stories, there's
[L1428] [01:07:10.64] these little anecdotes. There's things
[L1429] [01:07:12.96] where you say things like you you never
[L1430] [01:07:15.44] considered yourself smart, but you
[L1431] [01:07:18.00] noticed that other kids had an awful
[L1432] [01:07:20.72] time understanding things or yeah,
[L1433] [01:07:22.96] there's a problem that you solved where
[L1434] [01:07:24.96] someone else had difficulties, but you
[L1435] [01:07:28.08] don't view your contribution as a
[L1436] [01:07:30.40] brilliant one or anything like that. And
[L1437] [01:07:33.52] that that uh doesn't connect with me
[L1438] [01:07:36.80] because you've also won a touring award
[L1439] [01:07:38.32] and done all these amazing things. So,
[L1440] [01:07:40.40] how could that be that you, you know,
[L1441] [01:07:43.84] just merely discover things and are are
[L1442] [01:07:46.24] not smart yet you've achieved so much?
[L1443] [01:07:48.80] >> Well, this general thing that, you know,
[L1444] [01:07:51.92] psychologists talk about uh is that when
[L1445] [01:07:58.48] someone is good at something, they don't
[L1446] [01:08:01.60] realize how they're good they are at it
[L1447] [01:08:04.24] because it's simple to them.
[L1448] [01:08:08.00] There's the opposite one that uh people
[L1449] [01:08:11.44] who are bad at something think they're
[L1450] [01:08:13.52] better than they are because they're bad
[L1451] [01:08:15.76] at it.
[L1452] [01:08:17.60] Or to put uh a little bit more
[L1453] [01:08:21.04] concisely,
[L1454] [01:08:22.72] stupid people think they're smart
[L1455] [01:08:24.32] because they're too stupid to realize
[L1456] [01:08:25.84] they're not. Uh my the gift that I have
[L1457] [01:08:30.32] is not in some sense raw intelligence.
[L1458] [01:08:33.60] It's abstraction
[L1459] [01:08:35.44] and it's only recently, you know, the
[L1460] [01:08:39.12] last 10 or so years
[L1461] [01:08:42.96] that I realized how much better I am at
[L1462] [01:08:46.24] that than other people, most other
[L1463] [01:08:48.88] people. At this point, you've
[L1464] [01:08:51.28] experienced so much and you when you
[L1465] [01:08:53.60] look back on your career. If you could
[L1466] [01:08:56.96] go back to yourself when you just
[L1467] [01:08:58.56] graduated college and give yourself some
[L1468] [01:09:01.20] advice knowing what you know now, what
[L1469] [01:09:03.76] would you say?
[L1470] [01:09:05.92] >> One thing I've learned fairly early in
[L1471] [01:09:08.80] my life is that I shouldn't waste time
[L1472] [01:09:14.48] trying to answer questions that I don't
[L1473] [01:09:16.56] have to answer.
[L1474] [01:09:18.48] I don't think about, you know, what I
[L1475] [01:09:20.24] should have done because uh that's a
[L1476] [01:09:22.72] question that I don't have to answer.
[L1477] [01:09:25.76] >> Thank you for listening to the podcast.
[L1478] [01:09:27.52] It's a passion project of mine that I've
[L1479] [01:09:29.76] really enjoyed building. Another passion
[L1480] [01:09:31.84] project that I've been working on kind
[L1481] [01:09:33.12] of in secret is building an ergonomic
[L1482] [01:09:35.68] keyboard that I wish existed and I
[L1483] [01:09:37.92] finally have a prototype. So, I'd love
[L1484] [01:09:39.60] to show you what we've built. It's ultra
[L1485] [01:09:42.40] low profile and ergonomic. and I
[L1486] [01:09:44.96] couldn't find anything like it on the
[L1487] [01:09:46.32] market. So, that's why we built it. I'll
[L1488] [01:09:48.16] put a link to the keyboard in the
[L1489] [01:09:49.52] description. You can take a look and
[L1490] [01:09:50.96] learn more about the project there. We
[L1491] [01:09:52.80] could definitely use your support. Also,
[L1492] [01:09:54.80] if you have any feedback for me about
[L1493] [01:09:56.40] the show, I'd love to hear it. Comments
[L1494] [01:09:58.80] on YouTube have led to guests coming on
[L1495] [01:10:00.88] like Ilia Gregoric and David Fowler. I
[L1496] [01:10:04.00] wasn't aware of them until someone
[L1497] [01:10:05.76] dropped a comment. Also, feedback in the
[L1498] [01:10:07.76] comments helped me learn to reduce the
[L1499] [01:10:09.44] number of cliffhers in the intros. So,
[L1500] [01:10:12.08] your comments definitely make a
[L1501] [01:10:13.36] difference. Please keep letting me know
[L1502] [01:10:14.80] what you'd like to see more of in the
[L1503] [01:10:16.32] show, and I'll see you in the next
[L1504] [01:10:17.68] episode.
