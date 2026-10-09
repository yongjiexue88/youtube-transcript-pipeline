Chunk 6; segments 1737–2090. Start may repeat the previous chunk for context.

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

Source ID: source-238007c2e5a842c7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_P_vs_NP,_Zero-Knowledge_Proofs,_Quantum_Computation_Avi_Wigderson_en.txt
Video: https://www.youtube.com/watch?v=5GUcvSAJcJw

[L1746] [01:21:11.60] solution to one of the problems about
[L1747] [01:21:13.84] purification. It does not solve the one
[L1748] [01:21:17.28] source problem. This you need other
[L1749] [01:21:19.52] tools.
[L1750] [01:21:20.72] >> I saw that um you had done some work in
[L1751] [01:21:23.52] zero knowledge proofs. I was wondering
[L1752] [01:21:25.04] if you could explain you know what is a
[L1753] [01:21:26.96] zero knowledge proof and maybe we talk
[L1754] [01:21:28.48] about its significance.
[L1755] [01:21:30.40] >> Sure. Yeah. Z knowledge proof it's
[L1756] [01:21:32.72] pretty amazing that it became a
[L1757] [01:21:34.32] household word. I mean it was in the
[L1758] [01:21:38.64] domain of theorists for a long time. Uh
[L1759] [01:21:42.40] the original definition of zero
[L1760] [01:21:44.80] knowledge proof came in a paper seminar
[L1761] [01:21:47.04] paper of
[L1762] [01:21:48.96] uh Goldster Mi and Rakov
[L1763] [01:21:52.72] which also contained the definition of
[L1764] [01:21:55.04] interactive proof. So even before zero
[L1765] [01:21:57.44] knowledge uh they conceived of the
[L1766] [01:22:00.72] notion that proofs don't have to be
[L1767] [01:22:02.96] written down like in mathematical
[L1768] [01:22:04.64] papers.
[L1769] [01:22:07.04] people can have a discussion a
[L1770] [01:22:08.64] randomized discussion in which I'll try
[L1771] [01:22:10.64] to convince you of something or I I want
[L1772] [01:22:13.68] to prove to you something like I know
[L1773] [01:22:15.44] the uh you know the proof of the Roman
[L1774] [01:22:18.40] hypothesis or I can solve this suduku
[L1775] [01:22:20.56] puzzle and uh we can do it interactively
[L1776] [01:22:24.80] with the rand you know we are randomized
[L1777] [01:22:26.88] in particular you the verifier of my
[L1778] [01:22:30.24] claim are allowed to be randomized so
[L1779] [01:22:32.48] it's like in randomized algorithms but
[L1780] [01:22:34.56] Now the prover there's a prover it's not
[L1781] [01:22:37.52] just an algorith it's a prover like in
[L1782] [01:22:39.52] NP someone who knows the solution but
[L1783] [01:22:42.32] the convincing has this interactive
[L1784] [01:22:45.28] uh form so this model was suggested in
[L1785] [01:22:47.92] this paper and also in a paper of babai
[L1786] [01:22:51.52] parallel in the same time from different
[L1787] [01:22:54.24] motivations
[L1788] [01:22:56.08] uh
[L1789] [01:22:57.84] basically it offers a generalization of
[L1790] [01:23:00.32] the notion of np
[L1791] [01:23:03.84] is That's when I send you a message and
[L1792] [01:23:06.00] it convinces you. You verify it and it
[L1793] [01:23:08.16] convinces you. Now we allow an
[L1794] [01:23:10.96] interaction and we allow you you know a
[L1795] [01:23:14.80] small chance because you are randomized.
[L1796] [01:23:16.48] We allow small chance that you will uh
[L1797] [01:23:19.44] you know I will convince you of a false
[L1798] [01:23:21.28] claim but this error can be reduced like
[L1799] [01:23:24.32] in probabilistic algorithms can be
[L1800] [01:23:26.08] reduced arbitrarily. You want one in a
[L1801] [01:23:28.00] billion you can get one in a billion
[L1802] [01:23:30.08] whatever. Yeah. Anyway, so there's a
[L1803] [01:23:32.72] notion of an interactive proof and then
[L1804] [01:23:37.04] uh in the gold mali of paper they
[L1805] [01:23:40.32] suggested
[L1806] [01:23:41.84] another
[L1807] [01:23:43.68] notion of interactive proof which is
[L1808] [01:23:45.52] more restricted. You want to prove
[L1809] [01:23:47.60] something but the zero knowledge means
[L1810] [01:23:51.36] that you want the verifier to learn
[L1811] [01:23:54.88] nothing absolutely nothing about the
[L1812] [01:23:56.72] proof except that it's true.
[L1813] [01:24:01.04] Now this sounds really totally
[L1814] [01:24:03.36] ridiculous. I mean if you think about
[L1815] [01:24:05.20] the last time you convince somebody
[L1816] [01:24:08.16] uh to change their mind about anything
[L1817] [01:24:10.24] without providing them any any knowledge
[L1818] [01:24:13.60] any new things they didn't know. Say
[L1819] [01:24:15.92] what what are you talking about? This
[L1820] [01:24:18.08] such proofs don't exist for anything
[L1821] [01:24:20.64] there. No zero knowledge for anything.
[L1822] [01:24:23.52] Uh they were not thinking about you know
[L1823] [01:24:26.88] uh convincing someone of you know
[L1824] [01:24:29.20] political opinion. they were thinking
[L1825] [01:24:31.12] about cryptography of course you know
[L1826] [01:24:35.20] they've created the foundation of
[L1827] [01:24:37.28] cryptography in many in many other
[L1828] [01:24:39.28] papers um but they are imagining uh uh
[L1829] [01:24:44.24] cryptographic protocols in which you
[L1830] [01:24:46.08] have secrets and you you use these
[L1831] [01:24:48.80] secrets in your computation
[L1832] [01:24:51.12] and you have you know the protocol tells
[L1833] [01:24:54.32] you to do things that if you don't then
[L1834] [01:24:57.76] you know you're violating the protocol.
[L1835] [01:25:00.08] So the others don't want you to cheat.
[L1836] [01:25:02.88] They want to make sure you perform the
[L1837] [01:25:04.88] right operations on your secrets.
[L1838] [01:25:07.68] Uh for example, you are supposed to pick
[L1839] [01:25:09.68] a a public key by multiplying two uh
[L1840] [01:25:14.40] prime numbers. If you multiply three
[L1841] [01:25:18.56] or something else,
[L1842] [01:25:20.88] then you you are violating the protocol
[L1843] [01:25:23.44] and maybe security is not guaranteed. So
[L1844] [01:25:25.84] I would like to convince you that the
[L1845] [01:25:27.52] number I give you is actually a product
[L1846] [01:25:29.92] of two primes. I certainly don't want to
[L1847] [01:25:32.24] give you the two primes. So what I
[L1848] [01:25:35.36] really want to convince you of is that I
[L1849] [01:25:38.32] computed this number by multiplying two
[L1850] [01:25:42.08] primes. And you learn from this
[L1851] [01:25:44.88] interaction
[L1852] [01:25:46.80] absolutely nothing except you are
[L1853] [01:25:48.64] convinced with very high probability
[L1854] [01:25:51.20] that I did multiply two primes and not
[L1855] [01:25:53.52] any other number and I didn't do
[L1856] [01:25:55.20] anything else that I shouldn't have. And
[L1857] [01:25:57.76] you can think about lots of other
[L1858] [01:26:00.24] cryptographic protocols where people are
[L1859] [01:26:03.12] doing things like multi-party
[L1860] [01:26:04.80] computation very complex things they are
[L1861] [01:26:07.28] confusing with their secrets and they
[L1862] [01:26:10.80] don't want to reveal them whereas the
[L1863] [01:26:13.04] others want to make sure that they did
[L1864] [01:26:14.80] what they should. So there are any
[L1865] [01:26:17.12] number of you know applications to this
[L1866] [01:26:19.76] idea. The only problem is it sounds
[L1867] [01:26:22.40] ridiculous because it sounds impossible
[L1868] [01:26:24.88] in mathematics terms. If
[L1869] [01:26:28.08] uh you know some somebody came here and
[L1870] [01:26:30.64] said that P you know they prove P
[L1871] [01:26:33.68] different than NP you know I I would
[L1872] [01:26:36.64] want to see the proof and then tell me
[L1873] [01:26:38.56] okay I prove it to you in zero. How can
[L1874] [01:26:40.56] anybody convince me that they have a
[L1875] [01:26:43.76] proof of P different than NP and I come
[L1876] [01:26:46.16] out you know congratulating them and you
[L1877] [01:26:49.68] know
[L1878] [01:26:51.84] uh amazed by them and nevertheless I
[L1879] [01:26:55.04] know absolutely nothing about the way
[L1880] [01:26:56.88] they proved it. I'm I just know that
[L1881] [01:26:58.80] they did this. So it really sounds
[L1882] [01:27:01.76] ridiculous
[L1883] [01:27:03.68] and uh yeah certainly one of my favorite
[L1884] [01:27:08.56] papers maybe my favorite is the zero
[L1885] [01:27:11.68] paper which came a year later is joined
[L1886] [01:27:14.32] with Od and Sylvio Mikalli where we saw
[L1887] [01:27:18.56] that it's not only not ridiculous it's
[L1888] [01:27:21.04] universal
[L1889] [01:27:22.72] namely anything which has a proof a
[L1890] [01:27:25.28] mathematical proof also has a zero
[L1891] [01:27:28.64] knowledge interactive proof Anything
[L1892] [01:27:30.96] like P different than NP or that I
[L1893] [01:27:34.00] multiply two primes or anything that you
[L1894] [01:27:36.56] can prove revealing your secret you can
[L1895] [01:27:39.60] prove without revealing your secret and
[L1896] [01:27:41.92] convince beyond any reasonable doubt. So
[L1897] [01:27:45.60] that's possible.
[L1898] [01:27:46.72] >> What's the intuition behind that? Like
[L1899] [01:27:49.44] let's say I have a proof for P= MP and
[L1900] [01:27:51.84] we want to convert it to a zero
[L1901] [01:27:53.52] knowledge proof. How does that work?
[L1902] [01:27:55.44] >> How does this work? Well, first of all,
[L1903] [01:27:57.60] it assumes cryptography. So we assume we
[L1904] [01:28:00.00] have some oneway functions. We we assume
[L1905] [01:28:03.12] that some you know problem like factor
[L1906] [01:28:05.52] integers or this logarithm or any number
[L1907] [01:28:09.28] of oneway believed oneway functions uh
[L1908] [01:28:13.28] exist. So oneway functions if people
[L1909] [01:28:16.00] don't know functions that are easy to
[L1910] [01:28:18.64] compute in one way but are hard to
[L1911] [01:28:21.20] invert. For example multiplying numbers
[L1912] [01:28:23.28] is easy.
[L1913] [01:28:25.44] Finally the factors of a number which is
[L1914] [01:28:27.44] the inverse problem the prime factor is
[L1915] [01:28:30.72] believed to be hard of course we never
[L1916] [01:28:33.36] we can never we don't know any hard
[L1917] [01:28:36.00] problem that's the previous entry
[L1918] [01:28:37.60] question we don't know but we believe
[L1919] [01:28:40.16] about many problems and we the belief is
[L1920] [01:28:42.48] actually the whole world believe because
[L1921] [01:28:44.64] the whole world is using cryptographic
[L1922] [01:28:48.00] systems which rest on this all
[L1923] [01:28:50.80] electronic commerce assumes this so we
[L1924] [01:28:53.52] assume this so assume we
[L1925] [01:28:56.32] uh oneway functions uh oneway functions
[L1926] [01:28:59.68] allow you to uh create uh basically
[L1927] [01:29:04.08] garbled message commitments. I can uh
[L1928] [01:29:08.80] you know I have a number in my head I
[L1929] [01:29:12.72] don't want to tell you what the number
[L1930] [01:29:14.24] is. It's a number between one and 100. I
[L1931] [01:29:17.28] can write down another number
[L1932] [01:29:21.84] which looks like a random number to you.
[L1933] [01:29:25.20] And on the one hand you have no idea
[L1934] [01:29:29.52] I claim this encodes my secret. Okay.
[L1935] [01:29:33.28] And this commitment scheme which is
[L1936] [01:29:35.76] built very simply for one for monary
[L1937] [01:29:38.08] functions uh guarantees two properties.
[L1938] [01:29:40.96] A you cannot tell what is my secret even
[L1939] [01:29:44.32] though you can see this number this
[L1940] [01:29:45.92] other number I gave you. And uh on the
[L1941] [01:29:50.24] other hand I cannot change my mind about
[L1942] [01:29:53.36] my secret. It really commits me to the
[L1943] [01:29:56.96] uh so I can later provide you with a
[L1944] [01:29:59.92] certificate that I was thinking about 17
[L1945] [01:30:03.76] and I can only do it for 17. I cannot do
[L1946] [01:30:06.40] it for any other number. Okay. In fact a
[L1947] [01:30:10.32] very simple example is really using
[L1948] [01:30:12.00] factoring. uh in some sense the product
[L1949] [01:30:15.44] of two primes this number
[L1950] [01:30:19.60] uh you know it's easy you know this
[L1951] [01:30:23.12] number
[L1952] [01:30:24.72] uh commits it to its factors it uniquely
[L1953] [01:30:27.76] defines its factors right the only
[L1954] [01:30:30.24] problem is this is not exactly random
[L1955] [01:30:32.48] products of primes it's yeah but you can
[L1956] [01:30:35.28] do so you can do this okay so now uh
[L1957] [01:30:39.76] that we have to take commitments are
[L1958] [01:30:41.84] possible that's veryant important
[L1959] [01:30:44.64] uh so I'm I'm describing very high level
[L1960] [01:30:47.36] I'm hiding lots of things and even the
[L1961] [01:30:49.28] definition of zero knowledge the formal
[L1962] [01:30:52.08] definition is quite intricate it's not
[L1963] [01:30:55.20] the intuition is obvious and I said it
[L1964] [01:30:58.32] uh but actually formally defining is
[L1965] [01:31:00.64] non-trivial but at a high level I I'll
[L1966] [01:31:03.28] give you some idea about how a zero
[L1967] [01:31:05.20] knows proof looks like now we have to
[L1968] [01:31:07.76] think about what theorems am I proving
[L1969] [01:31:09.84] to you and it was very important to us
[L1970] [01:31:13.36] to uh figure out what problem to uh
[L1971] [01:31:16.56] think about even though today you can do
[L1972] [01:31:19.20] it for others but we were thinking about
[L1973] [01:31:22.56] uh theorems of the type here's the graph
[L1974] [01:31:25.44] we can color it in three colors it's
[L1975] [01:31:28.40] also a formal mathematical statement
[L1976] [01:31:30.32] either it's doable or not right and we
[L1977] [01:31:32.88] want we uh simply focus on proving in
[L1978] [01:31:36.64] zero knowledge claims of this type okay
[L1979] [01:31:40.88] the graph we both know I claim I can
[L1980] [01:31:43.36] colorize with three colors. You don't
[L1981] [01:31:45.84] believe me. You want to [clears throat]
[L1982] [01:31:46.80] be convinced of this fact and you don't
[L1983] [01:31:50.00] want me to cheat you. You don't want me
[L1984] [01:31:51.76] to be able to you know should be an
[L1985] [01:31:54.08] interactive proof and moreover we want
[L1986] [01:31:57.20] it I want it to be zero energy. I don't
[L1987] [01:31:59.36] want you to have a slightest idea of
[L1988] [01:32:01.60] what my coloring is or what anything you
[L1989] [01:32:04.32] didn't know before is okay. So roughly
[L1990] [01:32:08.32] the uh way it works the honor is proof
[L1991] [01:32:11.52] for this particular set of claims that
[L1992] [01:32:14.72] are certainly not all claims they are
[L1993] [01:32:17.20] very structured claims we look like the
[L1994] [01:32:20.00] following we iteratively repeat the
[L1995] [01:32:23.28] following procedure
[L1996] [01:32:25.52] I put commitments for the coloring
[L1997] [01:32:30.88] on every vertx I tell you you know I
[L1998] [01:32:33.36] don't tell you it's green red or blue
[L1999] [01:32:35.68] but I put a commitment to one of them on
[L2000] [01:32:39.04] each vertex.
[L2001] [01:32:41.12] You will choose at random an edge of the
[L2002] [01:32:45.44] graph and ask me to open these two
[L2003] [01:32:48.96] envelopes
[L2004] [01:32:50.96] to decommit.
[L2005] [01:32:53.28] And you will check that the colors you
[L2006] [01:32:55.60] see first of all are in this set. They
[L2007] [01:32:57.68] are not gray or orange. They are either
[L2008] [01:33:00.16] red, green or blue. And that they are
[L2009] [01:33:02.40] different.
[L2010] [01:33:04.24] This should give you some maybe slight
[L2011] [01:33:06.96] uh you know slight advantage or slight
[L2012] [01:33:10.72] uh support to the belief that maybe I'm
[L2013] [01:33:12.96] not cheating you. Of course, it's a very
[L2014] [01:33:15.04] limited one because I can cheat you in
[L2015] [01:33:17.12] some corner other. Yeah. So we have to
[L2016] [01:33:20.56] to establish two things. We will repeat
[L2017] [01:33:23.20] this again and again. We have to
[L2018] [01:33:25.52] establish that it's a you know that it's
[L2019] [01:33:28.00] a proof. It's an interactive proof that
[L2020] [01:33:30.40] I cannot cheat you. And we have to argue
[L2021] [01:33:32.48] the zon part. Okay. So let's do one at a
[L2022] [01:33:36.00] time. Uh to uh
[L2023] [01:33:42.88] do the the correctness that I cannot
[L2024] [01:33:45.60] fool you is very simple is the
[L2025] [01:33:48.16] following.
[L2026] [01:33:49.68] If the graph is not three colorable
[L2027] [01:33:52.40] whatever I commit for there's one place
[L2028] [01:33:55.28] which is an error. Either it has the
[L2029] [01:33:57.20] wrong color and not allowed color or two
[L2030] [01:33:59.76] colors are equal. you have some nonrival
[L2031] [01:34:03.04] chance of catching this with your random
[L2032] [01:34:06.00] guess right I mean it's one over the
[L2033] [01:34:07.84] number of edges not so small if you
[L2034] [01:34:10.56] graph on on you know with 100 edges it's
[L2035] [01:34:14.08] one in 100 if thousands if we repeat it
[L2036] [01:34:17.60] not thousand but 10,000 times the
[L2037] [01:34:20.48] probability that you don't catch me in
[L2038] [01:34:22.56] any of them drops exponentially to zero
[L2039] [01:34:26.48] right so
[L2040] [01:34:28.32] uh of Because there's a Okay, so this
[L2041] [01:34:32.56] this establishes that I cannot fool you.
[L2042] [01:34:36.08] The zeon knowledge is a more serious
[L2043] [01:34:38.40] problem because if I keep using the same
[L2044] [01:34:41.92] coloring,
[L2045] [01:34:43.52] you will ask me about this edge and this
[L2046] [01:34:45.68] edge and then eventually you'll know the
[L2047] [01:34:47.36] coloring of all colors.
[L2048] [01:34:50.16] Here's something that's really special
[L2049] [01:34:52.00] to the coloring that is being used. If I
[L2050] [01:34:55.60] have one coloring of the graph, I really
[L2051] [01:34:58.32] have six because I can peruse the name
[L2052] [01:35:01.36] there. I can replace red and green and
[L2053] [01:35:03.28] it's another valid coloring.
[L2054] [01:35:06.08] So what I do really in each one of these
[L2055] [01:35:08.48] iterations is not using the same
[L2056] [01:35:10.40] coloring but using a random one of these
[L2057] [01:35:13.44] possible six
[L2058] [01:35:15.84] that they are legal. They are all legal
[L2059] [01:35:18.08] and I I just use one of these six.
[L2060] [01:35:21.20] What's the advantage of this? when you
[L2061] [01:35:23.52] open a pair of vertices under this
[L2062] [01:35:26.24] distribution one of the six what you
[L2063] [01:35:28.48] will see if I do have a coloring and
[L2064] [01:35:30.96] that's the only I want to stress we only
[L2065] [01:35:33.36] have to establish zero knowledge if I
[L2066] [01:35:35.12] really can prove the theorem so if I if
[L2067] [01:35:37.60] I do know the solution the proof I want
[L2068] [01:35:40.64] to protect my knowledge
[L2069] [01:35:43.44] what happens when I reveal to you
[L2070] [01:35:46.80] two of these colors on the adjacent
[L2071] [01:35:49.76] vertices of the graph
[L2072] [01:35:52.64] It will be two in this distribution when
[L2073] [01:35:55.44] you restrict it to two vertices. It will
[L2074] [01:35:58.00] simply be two different random colors.
[L2075] [01:36:01.04] Right? This is what you get by all
[L2076] [01:36:02.72] permutations. This experimentation
[L2077] [01:36:05.20] what did you learn from this? Nothing.
[L2078] [01:36:07.68] You could have picked two random
[L2079] [01:36:09.28] different colors. You didn't need me for
[L2080] [01:36:11.44] that. So you didn't learn anything. So
[L2081] [01:36:14.24] in each iteration you learn nothing.
[L2082] [01:36:17.60] So this is the idea of the proof. Well,
[L2083] [01:36:20.96] this is the the end of the proof that I
[L2084] [01:36:24.00] can you know that showing that there's
[L2085] [01:36:26.40] there are zero knowledge proofs for all
[L2086] [01:36:29.68] u graph coloring three coloring
[L2087] [01:36:32.08] problems. What about all the rimonite
[L2088] [01:36:34.64] processes and the previous npn factoring
[L2089] [01:36:37.68] and all these other things I want to
[L2090] [01:36:39.20] claim to you and prove with zero and
[L2091] [01:36:40.96] everything here is very simple. You use
[L2092] [01:36:44.16] np completeness. This is an NP complete
[L2093] [01:36:46.80] problem. Anything can be that can be
[L2094] [01:36:49.68] proved is really something in NP. Right?
[L2095] [01:36:52.64] This is the definition. So you reduce it
[L2096] [01:36:55.68] to three color. You prove it in zero
[L2097] [01:36:57.52] knowledge. And and the main point about
[L2098] [01:37:00.80] reductions in NP is that they don't only
[L2099] [01:37:05.04] uh convert the you know the yes no
