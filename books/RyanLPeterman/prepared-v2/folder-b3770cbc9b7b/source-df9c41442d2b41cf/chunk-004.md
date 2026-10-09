Chunk 4; segments 1108–1490. Start may repeat the previous chunk for context.

# Turing Award Winner: The Invention of Public Key Cryptography | Martin Hellman

Source ID: source-df9c41442d2b41cf
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_The_Invention_of_Public_Key_Cryptography_Martin_Hellman_en.txt
Video: https://www.youtube.com/watch?v=AZLOETBCQM4

[L1117] [38:31.56] Dorothy the combination, only you know
[L1118] [38:33.20] the combination. You pass it to Dorothy,
[L1119] [38:35.24] she can't take either lock off.
[L1120] [38:37.56] She passes it to me, what can I do?
[L1121] [38:39.92] Take off my lock, leaving only your
[L1122] [38:42.36] lock. I pass it back to Dorothy, she
[L1123] [38:45.32] can't take off your lock, but when you
[L1124] [38:46.84] get it, you can, you get the message
[L1125] [38:48.40] inside. That's basically how
[L1126] [38:50.52] Diffie-Hellman
[L1127] [38:51.96] or Diffie-Hellman-Merkle key exchange
[L1128] [38:53.72] works.
[L1129] [38:54.88] Now, what's critical about this is that
[L1130] [38:56.44] I made the strong box big enough for you
[L1131] [38:58.52] to put a second lock on it.
[L1132] [39:00.56] If I hadn't done that, if I'd only made
[L1133] [39:02.72] it big enough for one lock, you could
[L1134] [39:04.64] have taken the strong box that you got,
[L1135] [39:06.40] and put it in a bigger strong box.
[L1136] [39:09.00] But now there's a problem. When I get
[L1137] [39:10.76] it, I can't get inside to take my lock
[L1138] [39:12.64] off. It has to be what's called
[L1139] [39:14.60] commutative.
[L1140] [39:16.28] And everybody knows what commu-
[L1141] [39:17.72] commutative means, although they may
[L1142] [39:19.24] have forgotten it. Addition is
[L1143] [39:21.24] commutative. 3 + 5 is the same as 5 + 3,
[L1144] [39:24.52] it doesn't matter which order you do the
[L1145] [39:26.04] operations in. You get eight.
[L1146] [39:29.32] 3 5 - 3 is 2.
[L1147] [39:32.08] 3 - 5 is - 2. You get a different
[L1148] [39:35.04] answer. It's not commutative.
[L1149] [39:36.76] Subtraction is not commutative.
[L1150] [39:38.96] And what what I had to do was find a
[L1151] [39:41.12] commutative one-way function, although I
[L1152] [39:42.76] didn't know that at the time.
[L1153] [39:44.72] And the function I used is a commutative
[L1154] [39:47.12] one-way function, it's exponentiation in
[L1155] [39:49.00] modular arithmetic. It doesn't matter
[L1156] [39:51.20] whether you first raise alpha to the X1
[L1157] [39:53.00] power, and then to the X2 power, or
[L1158] [39:55.40] raise it to the X2 power, and then to
[L1159] [39:57.08] the X1 power, you get the same result.
[L1160] [39:59.48] You get alpha to the X1 X2.
[L1161] [40:02.04] Multiplication in the exponent is
[L1162] [40:04.12] commutative. And we did this over a
[L1163] [40:06.84] finite field, where exponentiation is
[L1164] [40:10.40] not a smooth function, which would be
[L1165] [40:11.80] easy to invert, it jumps all over the
[L1166] [40:13.84] place.
[L1167] [40:14.84] And it But it turns out it still that
[L1168] [40:16.40] still works that way. So that is public
[L1169] [40:18.24] key exchange, public key distribution.
[L1170] [40:21.60] Digital signatures are more complicated.
[L1171] [40:23.88] That's something that Whit came up with.
[L1172] [40:25.56] It's a called a public key crypto system
[L1173] [40:27.64] and then RSA Rivest, Shamir, and Adleman
[L1174] [40:29.64] came up with the first in instance of
[L1175] [40:31.40] that.
[L1176] [40:32.44] Um
[L1177] [40:33.60] there you have a public key and a secret
[L1178] [40:35.84] key and it doesn't matter which order
[L1179] [40:37.32] you operate on them whether you first
[L1180] [40:39.28] use the public key and then the secret
[L1181] [40:40.80] key or the secret key and then the
[L1182] [40:42.12] public key, you get the initial result.
[L1183] [40:45.28] They undo one another. There, if I use
[L1184] [40:48.12] my secret key, I can sign a message
[L1185] [40:50.60] because
[L1186] [40:51.68] there's no privacy.
[L1187] [40:53.32] But I send the encrypted message to you
[L1188] [40:55.92] using my secret key. You use my public
[L1189] [40:57.96] key which you get from a
[L1190] [40:59.48] public file to verify it. That's how my
[L1191] [41:02.60] phone works. It's got a
[L1192] [41:05.40] public key built into it.
[L1193] [41:07.40] Apple knows the secret key.
[L1194] [41:09.40] Apple can sign software updates. People
[L1195] [41:11.76] can take my phone apart and get the
[L1196] [41:13.08] public key but that doesn't give them
[L1197] [41:14.64] the secret key that will allow them to
[L1198] [41:16.32] sign software updates.
[L1199] [41:18.24] >> I see. So in that case
[L1200] [41:20.16] Apple is uh signing their updates to
[L1201] [41:23.56] your phone.
[L1202] [41:24.24] >> Right.
[L1203] [41:25.04] >> So I I also was reading about symmetric
[L1204] [41:27.60] versus asymmetric and
[L1205] [41:29.68] what you're describing sounds like
[L1206] [41:31.08] asymmetric.
[L1207] [41:31.84] >> Yes. Asymmetric cryptography uses a
[L1208] [41:33.76] public key and a secret key. It's
[L1209] [41:35.48] asymmetric. Conventional cryptography
[L1210] [41:37.76] uses the same secret key to encrypt and
[L1211] [41:39.76] decrypt.
[L1212] [41:40.96] And that you that requires a courier
[L1213] [41:43.84] which is what has was required before
[L1214] [41:45.96] public key cryptography.
[L1215] [41:47.88] If you were a general in another
[L1216] [41:49.48] division
[L1217] [41:50.88] I could send you a key. I would send a
[L1218] [41:53.64] messenger with a key locked to his
[L1219] [41:55.92] wrist.
[L1220] [41:56.92] And when you got it, you could open it
[L1221] [41:58.64] up and get the key and then you and I
[L1222] [42:00.52] could use a radio channel to communicate
[L1223] [42:03.04] very cheaply and very fast.
[L1224] [42:05.48] But
[L1225] [42:06.64] you can't use couriers to communicate
[L1226] [42:09.24] keys between a bank and a and a client.
[L1227] [42:11.84] >> Yes, I saw modern systems. It's a It's
[L1228] [42:14.36] almost like multiple different
[L1229] [42:15.76] mechanisms where there's this asymmetric
[L1230] [42:18.36] key exchange at the beginning to
[L1231] [42:20.32] establish the connection. And then
[L1232] [42:22.36] there's a
[L1233] [42:23.60] That gets you that that key symmetric
[L1234] [42:26.48] thing.
[L1235] [42:27.04] >> It's just like I described for Apple
[L1236] [42:29.04] signing the software update. They don't
[L1237] [42:30.56] sign the whole thing. They only sign a
[L1238] [42:32.12] hash. In the same way, we could use a
[L1239] [42:34.64] public key cryptosystem like RSA to
[L1240] [42:37.52] exchange messages, but it's too slow.
[L1241] [42:39.72] So, what I do is I send you one use the
[L1242] [42:42.08] following key in AES, the Advanced
[L1243] [42:44.24] Encryption Standard. And then we use AES
[L1244] [42:46.52] very quickly to exchange messages.
[L1245] [42:50.40] And that's the difference between
[L1246] [42:52.96] asymmetric encryption, which we use at
[L1247] [42:54.80] first, where I use the public key to
[L1248] [42:56.72] encipher the message and use the secret
[L1249] [42:58.92] key to get the key, and then we use a
[L1250] [43:00.84] symmetric system to very quickly
[L1251] [43:03.12] communicate afterward.
[L1252] [43:05.32] >> I was reading about RSA versus the
[L1253] [43:07.52] Diffie-Hellman key exchange and um it it
[L1254] [43:10.80] seems like there was a lot of um patents
[L1255] [43:13.60] or something like that, patent wars.
[L1256] [43:15.56] What what's the context behind that?
[L1257] [43:18.44] >> I didn't know how patents worked uh when
[L1258] [43:20.60] I when we wrote the first patent uh on
[L1259] [43:23.40] public key cryptography. If I'd known,
[L1260] [43:25.64] we could have covered RSA.
[L1261] [43:27.64] We would have made a lot of money. Uh
[L1262] [43:29.08] basically, uh RSA made sold their
[L1263] [43:31.60] company for $250 million. We made $250
[L1264] [43:33.56] million. We made nothing
[L1265] [43:35.68] for virtually nothing from our
[L1266] [43:37.92] patents in cryptography. There was a
[L1267] [43:39.68] patent fight between RSA and us.
[L1268] [43:42.76] Uh MIT and Stanford uh or between their
[L1269] [43:46.00] licensees and uh uh
[L1270] [43:48.96] Basically, MIT won that that that fight.
[L1271] [43:52.47] >> [laughter]
[L1272] [43:55.04] >> And I was pissed at RSA for a long time.
[L1273] [43:58.16] And I was pissed with Jim Bidzos, the
[L1274] [43:59.96] president of RSA Data Security.
[L1275] [44:02.56] And around 1990 around 2000, sometime
[L1276] [44:06.24] around there, I realized it was
[L1277] [44:07.84] inconsistent with my approach to life to
[L1278] [44:09.80] be pissed at RSA. They'd won. The fight
[L1279] [44:12.84] was over.
[L1280] [44:14.52] And so, I went I approached Jim Bidzos
[L1281] [44:17.44] and I said, "Look, Jim,
[L1282] [44:19.24] I told him that. And I said, "Let's be
[L1283] [44:21.20] friends. Let's bury the hatchet." And we
[L1284] [44:23.60] essentially have. And friends are better
[L1285] [44:26.04] than enemies. I'm not sure, but I think
[L1286] [44:28.16] Ron Rivest might have actually nominated
[L1287] [44:30.72] Whit Me for the Turing Award.
[L1288] [44:33.60] Now, he wouldn't have done that if he
[L1289] [44:34.84] didn't think we deserved it, but he
[L1290] [44:36.08] wouldn't do it if he was pissed at us.
[L1291] [44:38.20] And friends are better than enemies.
[L1292] [44:40.60] That's not why I did it. That's not why
[L1293] [44:42.20] I became friends with them. But again,
[L1294] [44:44.84] but it it it
[L1295] [44:47.44] it worked out very well.
[L1296] [44:49.08] >> How did they win the patent war if your
[L1297] [44:52.60] ideas came first?
[L1298] [44:54.36] >> I remember I told you I didn't know how
[L1299] [44:55.60] patents worked. It's only the claims
[L1300] [44:57.48] that matter.
[L1301] [44:58.88] And so, if I'd known that, we could have
[L1302] [45:00.32] written a claim that would have covered
[L1303] [45:01.48] RSA.
[L1304] [45:02.76] Cuz
[L1305] [45:03.72] easily.
[L1306] [45:04.88] Uh Uh and but we didn't. Uh and so,
[L1307] [45:09.08] um
[L1308] [45:09.68] the patent was written very badly.
[L1309] [45:11.92] Stanford didn't want to invest a lot of
[L1310] [45:13.60] money in this patent. So, it had a law
[L1311] [45:16.12] school intern
[L1312] [45:18.20] write the patent instead of a patent
[L1313] [45:20.32] attorney.
[L1314] [45:22.00] Uh we made a lot of mistakes.
[L1315] [45:24.04] >> You mentioned friends are better than
[L1316] [45:26.12] enemies. I think Yeah, a lot of people
[L1317] [45:28.48] would agree with you, but I also think
[L1318] [45:31.20] most people wouldn't be able to get over
[L1319] [45:34.52] losing a $250 million outcome. How How
[L1320] [45:38.72] did you
[L1321] [45:40.32] kind of get over that and kind of
[L1322] [45:42.60] establish friendship?
[L1323] [45:44.04] >> Well, some of it is is in my genes, but
[L1324] [45:46.36] some of it I a lot of it comes from my
[L1325] [45:48.48] wife. Basically, my wife and I have been
[L1326] [45:50.80] married 59 years last March. Uh
[L1327] [45:54.48] and we were madly in love when we met.
[L1328] [45:57.56] We We followed society's rules and we we
[L1329] [46:00.00] we developed a toxic relationship. 10
[L1330] [46:02.56] years later, my wife was ready to leave
[L1331] [46:04.16] me, but I didn't know it cuz I had
[L1332] [46:05.68] blinders on the way many husbands do.
[L1333] [46:08.16] And fortunately, when she met me she
[L1334] [46:10.92] decided I was the one.
[L1335] [46:12.84] And
[L1336] [46:14.20] 15 year 10-15 years ago 10-15 years
[L1337] [46:16.60] after we're married roughly 50 years
[L1338] [46:18.76] ago,
[L1339] [46:19.60] she says, "He's still the one, although
[L1340] [46:21.60] life with him's impossible." And life
[L1341] [46:23.00] with her was no picnic. So, she went
[L1342] [46:24.92] around looking for catalysts, uh ways to
[L1343] [46:28.32] improve our relationship. And she
[L1344] [46:30.12] eventually found a group
[L1345] [46:32.24] uh I won't go into all the details
[L1346] [46:33.80] there. I I I tend to do that. Uh that
[L1347] [46:36.48] worked on the international and the
[L1348] [46:37.80] interpersonal at the same time. It was
[L1349] [46:39.84] founded by Professor Harry Rathbun, who
[L1350] [46:41.80] was a professor here at Stanford, born
[L1351] [46:43.92] in the 1890s, so he's no longer alive. I
[L1352] [46:46.48] knew him late in his life. And that's
[L1353] [46:48.92] how I that it was based on the teachings
[L1354] [46:51.80] of Jesus, which was a problem for me as
[L1355] [46:54.04] a Jew because it was okay not to go to
[L1356] [46:56.80] synagogue, which I didn't do,
[L1357] [46:58.88] but it was not okay to study the
[L1358] [47:00.24] teachings of Jesus. That was traitorous.
[L1359] [47:03.20] But
[L1360] [47:04.40] eventually Dorothy dragged me to enough
[L1361] [47:06.56] meetings that over years time I came to
[L1362] [47:08.80] see that these people, Creative
[L1363] [47:11.16] Initiative as the group was called at
[L1364] [47:13.16] the time, knew something I had to learn
[L1365] [47:15.56] if my marriage was going to survive.
[L1366] [47:17.76] And I surprised myself by being willing
[L1367] [47:20.60] to do things that seemed crazy to me.
[L1368] [47:22.88] The most important things were accepting
[L1369] [47:25.88] ideas that Dorothy had
[L1370] [47:28.52] that seemed crazy to me
[L1371] [47:30.40] that weren't crazy.
[L1372] [47:31.96] Because what happened when she had an
[L1373] [47:33.36] idea that seemed crazy to me?
[L1374] [47:35.40] I treated her like she was crazy.
[L1375] [47:37.40] What did that do? It drove her crazy.
[L1376] [47:39.44] What did that do? It convinced me I was
[L1377] [47:40.56] right that she was crazy. Kept the whole
[L1378] [47:42.12] cycle going.
[L1379] [47:43.40] By the way, the same happens
[L1380] [47:44.36] internationally.
[L1381] [47:45.80] We treat countries in ways that they
[L1382] [47:48.44] don't like. They react in ways that seem
[L1383] [47:50.40] crazy to us. We treat them like they're
[L1384] [47:51.76] crazy. And it keeps the whole cycle
[L1385] [47:54.20] going.
[L1386] [47:55.48] So, that's how I came that and so it's
[L1387] [47:57.64] based on the Gospels and while I'm not a
[L1388] [47:59.96] Christian,
[L1389] [48:01.16] I see Jesus as a Jewish reformer rather
[L1390] [48:03.12] than as a Christian Messiah. I I view
[L1391] [48:05.76] myself as a follower of Jesus.
[L1392] [48:08.28] >> When I was researching the discovery
[L1393] [48:09.88] that you had, it seems like
[L1394] [48:12.84] all of a sudden many of the similar
[L1395] [48:15.60] discoveries were happening all at the
[L1396] [48:17.08] same time. So, for instance, you
[L1397] [48:19.32] mentioned
[L1398] [48:20.52] >> Ralph Merkle Ralph Merkle and us?
[L1399] [48:22.76] >> Yes.
[L1400] [48:23.08] >> Oh, and GCHQ claims that they invented
[L1401] [48:25.28] it
[L1402] [48:26.24] uh maybe just a couple years before us,
[L1403] [48:27.60] but they only have half of it, which is
[L1404] [48:29.64] if they're right, which is uh the
[L1405] [48:31.88] privacy part. They didn't have anything
[L1406] [48:33.28] on digital signatures, but they claim
[L1407] [48:35.32] everything.
[L1408] [48:36.40] >> Right. And then there's also the MIT
[L1409] [48:38.04] folks.
[L1410] [48:38.68] >> The MIT folks now. Yeah, so I have a
[L1411] [48:40.60] theory about that.
[L1412] [48:42.12] I'm going to tell it as a joke, but it
[L1413] [48:44.00] it is more to this joke than I than I
[L1414] [48:45.76] think is just just a joke.
[L1415] [48:48.60] There's a muse that whispers in our
[L1416] [48:50.16] ears. There's a muse of poetry. There's
[L1417] [48:52.60] a muse of calculus who whispered in
[L1418] [48:54.88] Newton's ear and Leibniz's ear about the
[L1419] [48:56.80] same time. There's a muse that whispered
[L1420] [48:59.56] in uh Ralph's ear about the same time
[L1421] [49:02.24] that she whispered in my in our ears. Uh
[L1422] [49:05.40] most people don't pay attention to this
[L1423] [49:06.84] muse because she sounds crazy.
[L1424] [49:09.80] A few people do.
[L1425] [49:11.44] And so that's why I think uh
[L1426] [49:14.32] there's something in the air. I mean,
[L1427] [49:15.76] it's not necessarily a muse, but there's
[L1428] [49:17.32] something in the air that comes to
[L1429] [49:18.96] people.
[L1430] [49:20.76] >> But why, you know, why why didn't it
[L1431] [49:23.68] come 50 years earlier or why like how
[L1432] [49:26.28] come it seemed like they all came very
[L1433] [49:27.80] similar? I noticed the I I interviewed
[L1434] [49:30.80] um uh
[L1435] [49:32.36] Barbara Liskov as well who uh did a lot
[L1436] [49:35.12] in um like data abstraction and
[L1437] [49:37.56] modularity. And there also it was like
[L1438] [49:41.60] on the West Coast and the East Coast
[L1439] [49:43.08] without even communicating they had the
[L1440] [49:44.72] same discovery very similar.
[L1441] [49:46.88] >> I think my joke might actually have
[L1442] [49:48.24] something to say about that, but also
[L1443] [49:50.64] there's something that goes on
[L1444] [49:51.60] technologically. We didn't have the
[L1445] [49:53.36] computing power to do public key
[L1446] [49:54.92] cryptography. If someone had come up
[L1447] [49:56.40] with it 50 years before, it would have
[L1448] [49:57.68] been a nice idea that couldn't be
[L1449] [49:59.24] implemented.
[L1450] [50:00.08] >> So, there there's uh
[L1451] [50:02.00] uh like a
[L1452] [50:03.60] logistical part to this, which is just
[L1453] [50:05.68] the tools weren't there. And once they
[L1454] [50:07.36] were there, it kind of inspired the the
[L1455] [50:09.64] right thinking.
[L1456] [50:10.56] >> Yeah, but calculus, I mean, why that
[L1457] [50:12.32] occurred to Leibniz and Newton about the
[L1458] [50:14.48] same time. Oh, and Darwin and someone
[L1459] [50:16.88] else thought of evolution about the same
[L1460] [50:18.48] time. So, I don't know.
[L1461] [50:20.56] It is It is It
[L1462] [50:22.72] >> Yeah.
[L1463] [50:23.12] >> And maybe we maybe we should treat it as
[L1464] [50:24.60] that. Even though I'm a scientist, I
[L1465] [50:26.56] believe in the mystical side of life.
[L1466] [50:29.12] >> There's the cryptography work that
[L1467] [50:30.56] you're doing, and then I think later in
[L1468] [50:32.68] your career, I saw this uh rethinking
[L1469] [50:35.20] national security, and I was curious how
[L1470] [50:38.00] you got into this um I guess area, this
[L1471] [50:42.04] body of work, and you know, what's the
[L1472] [50:43.92] problem you're trying to solve?
[L1473] [50:46.36] >> Well, the problem we're trying to solve
[L1474] [50:47.40] is simple. We're going to kill
[L1475] [50:48.56] ourselves.
[L1476] [50:49.72] Uh
[L1477] [50:50.68] I mean, right now, I estimate that a
[L1478] [50:52.76] child born today
[L1479] [50:54.48] has
[L1480] [50:55.60] probably worse than even odds of living
[L1481] [50:57.32] out his or her natural life as a result
[L1482] [50:59.04] of nuclear weapons all by themselves,
[L1483] [51:01.00] without climate change, without AI,
[L1484] [51:03.00] without any of this other stuff.
[L1485] [51:05.20] >> What are you talking about with this AI
[L1486] [51:06.64] threat?
[L1487] [51:07.80] >> Well, there's the debate on that. Uh
[L1488] [51:10.56] Geoffrey Hinton, uh Yoshua Bengio uh
[L1489] [51:14.08] think that who won the ACIA the Turing
[L1490] [51:16.56] Award uh for their work in artificial
[L1491] [51:18.68] intelligence think that AI may actually
[L1492] [51:21.84] kill human beings off, something like
[L1493] [51:23.68] that. I mean, because it'll say, "Why do
[L1494] [51:25.60] I need these stupid people?"
[L1495] [51:28.36] Uh whereas uh Ed Feigenbaum and Raj
[L1496] [51:31.40] Reddy, who won the Turing Award uh 30
[L1497] [51:33.56] years ago for their work in artificial
[L1498] [51:35.20] intelligence, have both told me and
[L1499] [51:36.92] given me permission to quote them, so
