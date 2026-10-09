# Turing Award Winner: The Invention of Public Key Cryptography | Martin Hellman
Source: source-df9c41442d2b41cf | Chunk 4 of 5
Video: https://www.youtube.com/watch?v=AZLOETBCQM4
All caption text retained; paragraphs merge caption fragments without changing words.

[38:31.56–39:17.72; L1117–L1141] Dorothy the combination, only you know the combination. You pass it to Dorothy, she can't take either lock off. She passes it to me, what can I do? Take off my lock, leaving only your lock. I pass it back to Dorothy, she can't take off your lock, but when you get it, you can, you get the message inside. That's basically how Diffie-Hellman or Diffie-Hellman-Merkle key exchange works. Now, what's critical about this is that I made the strong box big enough for you to put a second lock on it. If I hadn't done that, if I'd only made it big enough for one lock, you could have taken the strong box that you got, and put it in a bigger strong box. But now there's a problem. When I get it, I can't get inside to take my lock off. It has to be what's called commutative. And everybody knows what commu- commutative means, although they may

[39:19.24–40:11.80; L1142–L1165] have forgotten it. Addition is commutative. 3 + 5 is the same as 5 + 3, it doesn't matter which order you do the operations in. You get eight. 3 5 - 3 is 2. 3 - 5 is - 2. You get a different answer. It's not commutative. Subtraction is not commutative. And what what I had to do was find a commutative one-way function, although I didn't know that at the time. And the function I used is a commutative one-way function, it's exponentiation in modular arithmetic. It doesn't matter whether you first raise alpha to the X1 power, and then to the X2 power, or raise it to the X2 power, and then to the X1 power, you get the same result. You get alpha to the X1 X2. Multiplication in the exponent is commutative. And we did this over a finite field, where exponentiation is not a smooth function, which would be easy to invert, it jumps all over the

[40:13.84–41:02.60; L1166–L1191] place. And it But it turns out it still that still works that way. So that is public key exchange, public key distribution. Digital signatures are more complicated. That's something that Whit came up with. It's a called a public key crypto system and then RSA Rivest, Shamir, and Adleman came up with the first in instance of that. Um there you have a public key and a secret key and it doesn't matter which order you operate on them whether you first use the public key and then the secret key or the secret key and then the public key, you get the initial result. They undo one another. There, if I use my secret key, I can sign a message because there's no privacy. But I send the encrypted message to you using my secret key. You use my public key which you get from a public file to verify it. That's how my phone works. It's got a

[41:05.40–41:16.32; L1192–L1198] public key built into it. Apple knows the secret key. Apple can sign software updates. People can take my phone apart and get the public key but that doesn't give them the secret key that will allow them to sign software updates.

[41:18.24–41:23.56; L1199–L1201] >> I see. So in that case Apple is uh signing their updates to your phone.

[41:24.24–41:24.24; L1202–L1202] >> Right.

[41:25.04–41:31.08; L1203–L1206] >> So I I also was reading about symmetric versus asymmetric and what you're describing sounds like asymmetric.

[41:31.84–42:09.24; L1207–L1226] >> Yes. Asymmetric cryptography uses a public key and a secret key. It's asymmetric. Conventional cryptography uses the same secret key to encrypt and decrypt. And that you that requires a courier which is what has was required before public key cryptography. If you were a general in another division I could send you a key. I would send a messenger with a key locked to his wrist. And when you got it, you could open it up and get the key and then you and I could use a radio channel to communicate very cheaply and very fast. But you can't use couriers to communicate keys between a bank and a and a client.

[42:11.84–42:26.48; L1227–L1234] >> Yes, I saw modern systems. It's a It's almost like multiple different mechanisms where there's this asymmetric key exchange at the beginning to establish the connection. And then there's a That gets you that that key symmetric thing.

[42:27.04–43:03.12; L1235–L1251] >> It's just like I described for Apple signing the software update. They don't sign the whole thing. They only sign a hash. In the same way, we could use a public key cryptosystem like RSA to exchange messages, but it's too slow. So, what I do is I send you one use the following key in AES, the Advanced Encryption Standard. And then we use AES very quickly to exchange messages. And that's the difference between asymmetric encryption, which we use at first, where I use the public key to encipher the message and use the secret key to get the key, and then we use a symmetric system to very quickly communicate afterward.

[43:05.32–43:15.56; L1252–L1256] >> I was reading about RSA versus the Diffie-Hellman key exchange and um it it seems like there was a lot of um patents or something like that, patent wars. What what's the context behind that?

[43:18.44–43:48.96; L1257–L1270] >> I didn't know how patents worked uh when I when we wrote the first patent uh on public key cryptography. If I'd known, we could have covered RSA. We would have made a lot of money. Uh basically, uh RSA made sold their company for $250 million. We made $250 million. We made nothing for virtually nothing from our patents in cryptography. There was a patent fight between RSA and us. Uh MIT and Stanford uh or between their licensees and uh uh Basically, MIT won that that that fight.

[43:52.47–43:52.47; L1271–L1271] >> [laughter]

[43:55.04–44:47.44; L1272–L1295] >> And I was pissed at RSA for a long time. And I was pissed with Jim Bidzos, the president of RSA Data Security. And around 1990 around 2000, sometime around there, I realized it was inconsistent with my approach to life to be pissed at RSA. They'd won. The fight was over. And so, I went I approached Jim Bidzos and I said, "Look, Jim, I told him that. And I said, "Let's be friends. Let's bury the hatchet." And we essentially have. And friends are better than enemies. I'm not sure, but I think Ron Rivest might have actually nominated Whit Me for the Turing Award. Now, he wouldn't have done that if he didn't think we deserved it, but he wouldn't do it if he was pissed at us. And friends are better than enemies. That's not why I did it. That's not why I became friends with them. But again, but it it it it worked out very well.

[44:49.08–44:52.60; L1296–L1297] >> How did they win the patent war if your ideas came first?

[44:54.36–45:22.00; L1298–L1314] >> I remember I told you I didn't know how patents worked. It's only the claims that matter. And so, if I'd known that, we could have written a claim that would have covered RSA. Cuz easily. Uh Uh and but we didn't. Uh and so, um the patent was written very badly. Stanford didn't want to invest a lot of money in this patent. So, it had a law school intern write the patent instead of a patent attorney. Uh we made a lot of mistakes.

[45:24.04–45:42.60; L1315–L1322] >> You mentioned friends are better than enemies. I think Yeah, a lot of people would agree with you, but I also think most people wouldn't be able to get over losing a $250 million outcome. How How did you kind of get over that and kind of establish friendship?

[45:44.04–46:33.80; L1323–L1346] >> Well, some of it is is in my genes, but some of it I a lot of it comes from my wife. Basically, my wife and I have been married 59 years last March. Uh and we were madly in love when we met. We We followed society's rules and we we we developed a toxic relationship. 10 years later, my wife was ready to leave me, but I didn't know it cuz I had blinders on the way many husbands do. And fortunately, when she met me she decided I was the one. And 15 year 10-15 years ago 10-15 years after we're married roughly 50 years ago, she says, "He's still the one, although life with him's impossible." And life with her was no picnic. So, she went around looking for catalysts, uh ways to improve our relationship. And she eventually found a group uh I won't go into all the details there. I I I tend to do that. Uh that

[46:36.48–47:28.52; L1347–L1370] worked on the international and the interpersonal at the same time. It was founded by Professor Harry Rathbun, who was a professor here at Stanford, born in the 1890s, so he's no longer alive. I knew him late in his life. And that's how I that it was based on the teachings of Jesus, which was a problem for me as a Jew because it was okay not to go to synagogue, which I didn't do, but it was not okay to study the teachings of Jesus. That was traitorous. But eventually Dorothy dragged me to enough meetings that over years time I came to see that these people, Creative Initiative as the group was called at the time, knew something I had to learn if my marriage was going to survive. And I surprised myself by being willing to do things that seemed crazy to me. The most important things were accepting ideas that Dorothy had that seemed crazy to me

[47:30.40–48:05.76; L1371–L1391] that weren't crazy. Because what happened when she had an idea that seemed crazy to me? I treated her like she was crazy. What did that do? It drove her crazy. What did that do? It convinced me I was right that she was crazy. Kept the whole cycle going. By the way, the same happens internationally. We treat countries in ways that they don't like. They react in ways that seem crazy to us. We treat them like they're crazy. And it keeps the whole cycle going. So, that's how I came that and so it's based on the Gospels and while I'm not a Christian, I see Jesus as a Jewish reformer rather than as a Christian Messiah. I I view myself as a follower of Jesus.

[48:08.28–48:19.32; L1392–L1397] >> When I was researching the discovery that you had, it seems like all of a sudden many of the similar discoveries were happening all at the same time. So, for instance, you mentioned

[48:20.52–48:20.52; L1398–L1398] >> Ralph Merkle Ralph Merkle and us?

[48:22.76–48:22.76; L1399–L1399] >> Yes.

[48:23.08–48:35.32; L1400–L1407] >> Oh, and GCHQ claims that they invented it uh maybe just a couple years before us, but they only have half of it, which is if they're right, which is uh the privacy part. They didn't have anything on digital signatures, but they claim everything.

[48:36.40–48:38.04; L1408–L1409] >> Right. And then there's also the MIT folks.

[48:38.68–49:18.96; L1410–L1429] >> The MIT folks now. Yeah, so I have a theory about that. I'm going to tell it as a joke, but it it is more to this joke than I than I think is just just a joke. There's a muse that whispers in our ears. There's a muse of poetry. There's a muse of calculus who whispered in Newton's ear and Leibniz's ear about the same time. There's a muse that whispered in uh Ralph's ear about the same time that she whispered in my in our ears. Uh most people don't pay attention to this muse because she sounds crazy. A few people do. And so that's why I think uh there's something in the air. I mean, it's not necessarily a muse, but there's something in the air that comes to people.

[49:20.76–49:44.72; L1430–L1440] >> But why, you know, why why didn't it come 50 years earlier or why like how come it seemed like they all came very similar? I noticed the I I interviewed um uh Barbara Liskov as well who uh did a lot in um like data abstraction and modularity. And there also it was like on the West Coast and the East Coast without even communicating they had the same discovery very similar.

[49:46.88–49:59.24; L1441–L1449] >> I think my joke might actually have something to say about that, but also there's something that goes on technologically. We didn't have the computing power to do public key cryptography. If someone had come up with it 50 years before, it would have been a nice idea that couldn't be implemented.

[50:00.08–50:09.64; L1450–L1455] >> So, there there's uh uh like a logistical part to this, which is just the tools weren't there. And once they were there, it kind of inspired the the right thinking.

[50:10.56–50:20.56; L1456–L1461] >> Yeah, but calculus, I mean, why that occurred to Leibniz and Newton about the same time. Oh, and Darwin and someone else thought of evolution about the same time. So, I don't know. It is It is It

[50:22.72–50:22.72; L1462–L1462] >> Yeah.

[50:23.12–50:26.56; L1463–L1465] >> And maybe we maybe we should treat it as that. Even though I'm a scientist, I believe in the mystical side of life.

[50:29.12–50:43.92; L1466–L1472] >> There's the cryptography work that you're doing, and then I think later in your career, I saw this uh rethinking national security, and I was curious how you got into this um I guess area, this body of work, and you know, what's the problem you're trying to solve?

[50:46.36–51:03.00; L1473–L1484] >> Well, the problem we're trying to solve is simple. We're going to kill ourselves. Uh I mean, right now, I estimate that a child born today has probably worse than even odds of living out his or her natural life as a result of nuclear weapons all by themselves, without climate change, without AI, without any of this other stuff.

[51:05.20–51:06.64; L1485–L1486] >> What are you talking about with this AI threat?

[51:07.80–51:36.92; L1487–L1499] >> Well, there's the debate on that. Uh Geoffrey Hinton, uh Yoshua Bengio uh think that who won the ACIA the Turing Award uh for their work in artificial intelligence think that AI may actually kill human beings off, something like that. I mean, because it'll say, "Why do I need these stupid people?" Uh whereas uh Ed Feigenbaum and Raj Reddy, who won the Turing Award uh 30 years ago for their work in artificial intelligence, have both told me and given me permission to quote them, so
