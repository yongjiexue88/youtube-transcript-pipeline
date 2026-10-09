Chunk 1; segments 1–116. 

# Creator of Postgres (Turing Award): "One Size Fits None", Leveraging GPUs, Difficult Implementations

Source ID: source-054cafd98518a73a
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Postgres_(Turing_Award)_One_Size_Fits_None_,_Leveraging_GPUs,_Difficult_Implementations_en.txt
Video: https://www.youtube.com/watch?v=qCKgWsexY6c

[L10] [00:00.08] talk and I think there's also a paper
[L11] [00:01.60] behind it of this idea that uh one
[L12] [00:05.20] sizefits all database systems not
[L13] [00:07.76] optimal one size actually fits none and
[L14] [00:10.88] that what you really want is database
[L15] [00:14.00] solutions that target specific needs
[L16] [00:17.44] what database offerings you see today
[L17] [00:19.36] that are one-sizefits-all in 2004 when I
[L18] [00:22.96] wrote the paper we had an academic
[L19] [00:25.28] project which was building what became
[L20] [00:28.56] streambase
[L21] [00:29.68] And so a stream processing engine looks
[L22] [00:32.24] nothing like a relational database.
[L23] [00:36.00] And we had the gist of an idea for
[L24] [00:39.84] column stores for the for data
[L25] [00:41.84] warehouses which was popularized by
[L26] [00:44.80] Vertica looks nothing like a row store.
[L27] [00:48.40] So here were three wildly different
[L28] [00:50.80] implementations that had no resemblance
[L29] [00:53.36] to each other and in each case they were
[L30] [00:56.48] an order of magnitude faster than the
[L31] [00:59.36] other guys. So it's pretty clear that
[L32] [01:02.08] one side, you know, that in with those
[L33] [01:04.72] three instances,
[L34] [01:06.96] you give up an order of magnitude
[L35] [01:09.84] uh when you're running a database system
[L36] [01:12.96] that isn't
[L37] [01:14.96] that isn't architected for your kind of
[L38] [01:17.12] stuff. I think that's still true. I
[L39] [01:20.88] mean, I think Clickhouse is a column
[L40] [01:23.36] store. Pine cone is faster than
[L41] [01:28.80] userdefined types
[L42] [01:31.60] on on textbased vector processing.
[L43] [01:36.48] And so I think it's it's still very much
[L44] [01:39.52] the case [snorts] and I think
[L45] [01:43.44] there's no difficulty
[L46] [01:46.24] putting a common parser on top of
[L47] [01:48.72] multiple implementations.
[L48] [01:51.84] uh Postgress has so far chosen not to do
[L49] [01:54.88] that. they don't implement a column
[L50] [01:57.84] store
[L51] [01:59.44] and so I think they are not they are not
[L52] [02:01.92] competitive you know on sizable data
[L53] [02:05.92] warehouses
[L54] [02:07.76] they also don't have multi-node support
[L55] [02:11.28] again for people with big data
[L56] [02:13.12] warehouses that's table stakes so I
[L57] [02:16.48] think it's just as true today as it ever
[L58] [02:18.48] was I think that
[L59] [02:22.32] what is true
[L60] [02:24.48] is that if you want to get going, you
[L61] [02:26.96] have a database problem,
[L62] [02:29.68] you know, the answer is choose Postgress
[L63] [02:32.62] [snorts] and there's a huge programming
[L64] [02:34.88] community, all kinds of all kinds of,
[L65] [02:38.00] you know, data type implementations.
[L66] [02:40.80] it's free uh and you can find Postgress
[L67] [02:46.32] talent easily and get going
[L68] [02:49.76] and and so I think it's it's it's a
[L69] [02:52.72] great choice for lowest common
[L70] [02:54.32] denominator
[L71] [02:56.32] and until you're trying to do [snorts] a
[L72] [03:00.80] million transactions a second it works
[L73] [03:02.80] just fine until you're trying to support
[L74] [03:06.08] a pedibyte data warehouse it it I say at
[L75] [03:08.88] the low end it it's absolutely
[L76] [03:10.40] Absolutely the right one sizefits all at
[L77] [03:12.96] the low end it's postgress at the high
[L78] [03:15.76] end that's just not true
[L79] [03:18.08] >> GPUs do they make available some new
[L80] [03:21.60] opportunities to optimize databases
[L81] [03:24.40] probably but I think the the big
[L82] [03:27.04] challenge is that GPUs are
[L83] [03:32.24] you know sumd sim you know single
[L84] [03:34.88] instruction multi- data and that's
[L85] [03:37.68] that's the anathema of indexing
[L86] [03:41.12] And so whenever indexing is the right
[L87] [03:43.36] answer,
[L88] [03:44.88] they're probably not a good idea.
[L89] [03:48.40] And I think uh also you've got to
[L90] [03:52.72] architect them so that the so that the
[L91] [03:56.48] bandwidth
[L92] [03:58.48] so that the bandwidth from storage is is
[L93] [04:02.80] not not the bottleneck. And so if
[L94] [04:06.56] they're an add-on to the CPU as often as
[L95] [04:09.12] not the bus connecting it to the the GPU
[L96] [04:12.72] to the CPU is a bottleneck.
[L97] [04:15.04] >> Can you explain why indexing would be
[L98] [04:18.56] not as effective when there's SIMD?
[L99] [04:22.80] >> So let's let's say I'm I'm [snorts]
[L100] [04:26.56] looking for Ryan's
[L101] [04:29.36] I'm looking for Ryan's salary and I have
[L102] [04:31.60] a B tree.
[L103] [04:33.60] So you go to the root of the B tree.
[L104] [04:37.28] You find you find the divider that has
[L105] [04:41.12] both sides of Ryan.
[L106] [04:43.52] You follow the pointer.
[L107] [04:46.08] That's a memory access for sure. Then
[L108] [04:49.28] you do it all again and you do this like
[L109] [04:52.08] three or four times.
[L110] [04:54.24] So that doesn't parallelize well. So the
[L111] [04:57.04] answer is indexing doesn't parallelize
[L112] [04:59.20] well. You mentioned B trees. When you
[L113] [05:01.68] first implemented
[L114] [05:03.52] uh that first version of ingress, did
[L115] [05:06.40] you write all of that by hand? Because I
[L116] [05:08.88] imagine there's probably not some
[L117] [05:10.48] existing B tree library or something.
[L118] [05:13.12] >> Yeah, we wrote the original version of
[L119] [05:15.36] ingress was all written from scratch.
[L120] [05:17.92] >> What was the hardest part of that
[L121] [05:19.20] implementation?
[L122] [05:21.52] >> Uh query optimizer.
[L123] [05:23.52] >> And why was that hard?
[L124] [05:25.28] >> It's tough. It's it's just
[L125] [05:29.44] algorithmically difficult.
