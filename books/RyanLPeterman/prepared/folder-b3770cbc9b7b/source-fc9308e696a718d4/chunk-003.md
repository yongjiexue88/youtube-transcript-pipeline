Chunk 3; segments 701–1047. Start may repeat the previous chunk for context.

# Turing Award Winner: TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC | David Patterson

Source ID: source-fc9308e696a718d4
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_TPU_vs_GPU_vs_CPU,_Computer_Architecture,_RISC_vs_CISC_David_Patterson_en.txt
Video: https://www.youtube.com/watch?v=Pn4ZwlEh5nw

[L710] [27:21.76] few advocates but a lot of people didn't
[L711] [27:23.44] believe in it they went into a
[L712] [27:25.44] competition to see who could do the best
[L713] [27:27.92] image recognition in 2012 the so-called
[L714] [27:31.60] AlexNet beat all the competition this
[L715] [27:33.92] was this uh historic moment in the in
[L716] [27:37.68] the in machine learning learning in
[L717] [27:39.68] neural networking and once they did it
[L718] [27:42.48] and the guy who did that had taken a
[L719] [27:44.24] cuda course at the University of Toronto
[L720] [27:46.48] to learned how to use it and so he says
[L721] [27:47.76] well as long as I'm doing this I'll do
[L722] [27:49.04] it on a GPU so he was able to explore a
[L723] [27:51.84] lot more space on this cheap fast GPU so
[L724] [27:55.28] he entered it in the competition 2012
[L725] [27:58.08] and within he was the only one using
[L726] [28:00.08] neural networks and he crushed the
[L727] [28:01.92] competition and within a few years
[L728] [28:03.76] everybody switched over and not only
[L729] [28:06.16] they were doing neural networks but
[L730] [28:07.44] they're using GPUs
[L731] [28:09.28] So GPUs have this um heritage of being a
[L732] [28:12.64] graphics in graphics engine but more
[L733] [28:16.40] programmable and uh it started getting
[L734] [28:19.52] used for machine learning. When Google
[L735] [28:22.08] came along uh they decided you know it
[L736] [28:24.72] was a clean slate. They didn't they
[L737] [28:26.24] didn't care about graphics. So the at
[L738] [28:28.96] the heart of neural networking is a
[L739] [28:31.04] matrix multiply. That's the that's the
[L740] [28:33.20] thing. So they designed a a processor
[L741] [28:36.00] for at the time microp processor at the
[L742] [28:37.68] time had a giant matrix multiplying
[L743] [28:39.84] unit. That was the main thing and then
[L744] [28:41.92] they threw a bunch of stuff out that
[L745] [28:43.28] they didn't need. So a lot of general
[L746] [28:45.52] purpose computing is what's on the chip
[L747] [28:47.76] is maybe three levels of caches to try
[L748] [28:50.88] and have so you don't spend all your
[L749] [28:52.88] time going to the relatively slow
[L750] [28:54.32] memory. Well, for machine learning, they
[L751] [28:56.32] knew when their memory accesses were so
[L752] [28:58.08] they could schedule that. So they didn't
[L753] [29:00.32] a a hardware cache didn't make any
[L754] [29:02.32] sense. they would just have a memory
[L755] [29:04.00] that the software understood would
[L756] [29:05.36] transfer in time. So those were some of
[L757] [29:07.28] the innovations. Also they innovated on
[L758] [29:09.36] the floatingoint format. You didn't need
[L759] [29:12.32] uh uh you know scientific computing
[L760] [29:15.60] cares a lot about precision. They have
[L761] [29:18.00] you know most of it's done in 64-bit
[L762] [29:19.76] floating point where the exponent is you
[L763] [29:22.40] know less than 10 bits and most of it is
[L764] [29:25.20] is the uh precision you know the
[L765] [29:27.52] fraction can be 50 some bits. Well, they
[L766] [29:30.56] what they realized for machine learning
[L767] [29:32.16] and AI, they don't need all that
[L768] [29:33.92] precision. They needed the range. So,
[L769] [29:35.76] Google did the first floatingoint format
[L770] [29:38.48] where the exponent was bigger than the
[L771] [29:40.16] fraction. That's that was a radical idea
[L772] [29:42.24] that so-called brain float 16, the part
[L773] [29:45.04] of Google that was doing this was the
[L774] [29:47.28] brain research group. So, they brought
[L775] [29:49.76] out this architecture. They had this
[L776] [29:52.48] narrow floating point format. They had
[L777] [29:54.80] big matrix multiply unit. It only had
[L778] [29:56.80] one one processor in it. uh unlike the
[L779] [29:59.68] other ones, it was just dedicated
[L780] [30:01.36] machine learning and it just kind of
[L781] [30:02.64] blew the doors off of everybody in the
[L782] [30:05.52] field. It was uh you know like 30 times
[L783] [30:08.32] better at inference than the
[L784] [30:10.48] contemporary GPU and 80 times better
[L785] [30:12.40] than CPU by having this dedicated one.
[L786] [30:15.20] So when uh Google made this announcement
[L787] [30:17.76] at their annual retreat a year or so
[L788] [30:20.64] after um after they had deployed it
[L789] [30:23.84] inside uh it just shook everybody up.
[L790] [30:26.40] Intel started buying companies. Um you
[L791] [30:29.52] know Nvidia started modifying the design
[L792] [30:33.12] uh for to be mach
[L793] [30:36.00] learning and then a bunch of other
[L794] [30:37.84] competitors uh started uh uh
[L795] [30:41.12] hyperscalers started doing their own
[L796] [30:42.48] effort. So I think that was the watersh
[L797] [30:44.16] I think the TPU announcement was the
[L798] [30:46.16] watershed moment there.
[L799] [30:48.32] >> So it's it's almost like uh levels of
[L800] [30:51.12] specialization like the CPU is the most
[L801] [30:53.20] general. Well yeah if we could still if
[L802] [30:55.36] you know if we still had dinard scaling
[L803] [30:57.84] if we you know Morris law and dinard
[L804] [30:59.52] scaling where we be today with general
[L805] [31:02.64] purpose processors we should have 100
[L806] [31:04.32] terahertz
[L807] [31:05.92] you know microprocessors if we could
[L808] [31:07.92] build 100 terahertz microprocessors
[L809] [31:09.84] that's what we do we would the GPUs
[L810] [31:12.40] would still be a niche you know if we
[L811] [31:14.16] could do that it you know it raises all
[L812] [31:16.40] boats that would be fantastic if we
[L813] [31:18.40] could do that but that that's long in
[L814] [31:21.36] the history we haven't been able to do
[L815] [31:23.36] that for 20 years and so you know there
[L816] [31:25.60] were probably two or three gigahertz
[L817] [31:27.76] microprocessors in 2005 and that's kind
[L818] [31:31.04] of where they are barely improved today
[L819] [31:33.60] so we can't do that. So there's still
[L820] [31:36.16] areas where it's important to have CPUs.
[L821] [31:38.64] They're the right, you know, you need
[L822] [31:40.56] operating systems, compilers and things.
[L823] [31:43.04] Uh that they're the right solution, but
[L824] [31:45.36] things have been specialized. And then
[L825] [31:47.84] now in terms of industry terms, huge
[L826] [31:50.80] emphasis is being put into the AI
[L827] [31:53.20] accelerators or just AI in general is
[L828] [31:56.24] where the money is being invested. And
[L829] [31:58.08] so the question for any processor
[L830] [32:00.32] designers was how does my processor
[L831] [32:03.44] design fit into this AI universe and um
[L832] [32:08.32] what should I do? How should I change it
[L833] [32:10.08] for this important application?
[L834] [32:12.48] >> So you mentioned that kind of Moore's
[L835] [32:14.64] laws slowing down and I watched this
[L836] [32:17.36] other talk from Jim Keller saying that
[L837] [32:20.72] Moore's law isn't isn't dead. But is it
[L838] [32:23.68] controversial to say that it's slow? Oh,
[L839] [32:25.52] I mean not not to real engineers. The
[L840] [32:28.80] the Morris law is very simple. It says
[L841] [32:30.88] in a in a chip the number of transistors
[L842] [32:33.92] will double originally said every year
[L843] [32:35.92] and then he mended it uh to every two
[L844] [32:38.72] years. Just just look do the chips are
[L845] [32:41.68] the number of transistors doubled and no
[L846] [32:44.24] now I think what people assume that
[L847] [32:47.68] means if trans if we are no longer on
[L848] [32:50.08] Morris law that technology is not
[L849] [32:52.16] improving. That's not the same thing.
[L850] [32:54.32] it's not improving at the rate that
[L851] [32:56.00] Moore projected. And what was amazing
[L852] [32:58.40] about Moors law which lasted 50 years is
[L853] [33:01.76] that it it guided the investment of
[L854] [33:04.32] semigtory manufacturing. We need to
[L855] [33:06.56] deliver on doubling transistors every
[L856] [33:08.48] year or two. How are we going to do
[L857] [33:10.72] that? How are we going to build the
[L858] [33:12.32] equipment to do it? So it was a
[L859] [33:13.52] guideline for the whole industry which
[L860] [33:15.84] was kind of remarkable. So what we are
[L861] [33:18.40] doing now is there's pieces of the
[L862] [33:21.20] technology to get better and there's
[L863] [33:22.64] pieces that uh that don't improve at
[L864] [33:25.76] all. So one of the big pieces important
[L865] [33:28.80] pieces on a chip is the static RAM
[L866] [33:31.44] SRAMM. So that's hardly improving at
[L867] [33:33.76] all.
[L868] [33:35.44] Logic gates still continue to improve.
[L869] [33:37.60] They are the gates are getting better.
[L870] [33:39.44] So if you're doing like uh adders or
[L871] [33:42.08] multipliers, those are getting better.
[L872] [33:43.36] those pieces. It's not uniform
[L873] [33:45.60] improvement anymore. And we're also
[L874] [33:47.76] going to more exotic packaging to be
[L875] [33:50.72] able to deliver it. Uh so people not uh
[L876] [33:54.00] it, you know, forever it was a single
[L877] [33:56.72] chip was the best way to package
[L878] [34:00.32] everything fits on one chip and that's
[L879] [34:02.16] what we're going to build. And now
[L880] [34:03.84] there's these ideas of chiplets or
[L881] [34:06.08] packaging multiple chips together. the
[L882] [34:08.08] latest GPUs and I think the latest TPUs
[L883] [34:11.20] has actually two what are called full
[L884] [34:13.44] reticle design dyes package put into a
[L885] [34:17.36] package and uh so a full reticle design
[L886] [34:20.72] is uh the maximum you can build on a on
[L887] [34:23.92] a semiconductor it they have a step and
[L888] [34:26.24] repeat motor and there's you know in the
[L889] [34:28.24] old days you'd have many chips inside
[L890] [34:29.92] that now there's just one so two maximum
[L891] [34:33.12] reticle designs form a node so they're
[L892] [34:35.84] using packaging so if you from outside
[L893] [34:38.72] you can say well there look there's look
[L894] [34:40.40] how many transistors are it's quote
[L895] [34:42.48] Moore's law is continuing but if you see
[L896] [34:44.96] what's inside the chip you know that's
[L897] [34:47.04] that has tapered off and I think part of
[L898] [34:48.96] it is for a fair amount of the industry
[L899] [34:52.24] if you were in a semiconductor
[L900] [34:54.00] manufacturer and people ask you what you
[L901] [34:55.76] do is I make Moors law I I make I
[L902] [34:59.28] sustain Morris law what I do and if
[L903] [35:01.12] you've been doing that for decades and
[L904] [35:02.48] somebody says Morris law is over it's
[L905] [35:04.08] like it my my career is
[L906] [35:06.96] So I think there's an emotional side of
[L907] [35:08.64] it but you know just look at the data
[L908] [35:11.20] the data doesn't back up what Keller
[L909] [35:12.96] says but I also didn't say that the
[L910] [35:16.32] technology is not improving the
[L911] [35:18.64] technology is continuing to improve and
[L912] [35:21.04] specifically domain specific
[L913] [35:22.64] architectures but if you look at the
[L914] [35:24.24] general purpose architectures or even
[L915] [35:26.48] other memory technologies you know it
[L916] [35:29.20] used to be the DRAMs would improve by a
[L917] [35:31.52] factor of four in density every 3 years
[L918] [35:33.44] like clockwork and now it's maybe 10
[L919] [35:36.40] years between factors for so you can see
[L920] [35:38.16] plenty of evidence that Moore's law no
[L921] [35:40.40] longer applies.
[L922] [35:41.92] >> Is there um some new version or some
[L923] [35:46.80] analog to Mo's law that is kind of
[L924] [35:48.72] guiding uh you know microprocessor
[L925] [35:52.24] design and architecture these days? I I
[L926] [35:54.88] guess a question is uh both Nvidia and
[L927] [35:59.60] Google are continuing to deliver much
[L928] [36:02.08] faster processors for machine learning,
[L929] [36:04.72] tremendously better. What are they
[L930] [36:06.48] doing? Well, part of it is what I said
[L931] [36:10.24] about uh packaging, you know, to getting
[L932] [36:12.88] uh to to be able to get more transistors
[L933] [36:15.28] and you keep them closer together
[L934] [36:16.88] because distance matters. Uh part of it
[L935] [36:19.20] is innovating on the floatingpoint
[L936] [36:20.64] formats. So it you know unlike the
[L937] [36:23.52] supercomputers of 64-bit
[L938] [36:26.08] it's not even 64-bit not even 32-bit not
[L939] [36:28.80] even 16 bit but 8bit and 4bit floating
[L940] [36:31.68] point is as is going on so narrowing of
[L941] [36:34.16] the data types um the uh you know having
[L942] [36:40.08] kind of what's called the matrix
[L943] [36:42.08] multiply instructions so these powerful
[L944] [36:44.88] units that are put in there that can
[L945] [36:46.72] that can uh do special purpose
[L946] [36:49.20] applications that are very important get
[L947] [36:51.28] making those bigger and faster. So those
[L948] [36:53.52] are the things that are going on. But we
[L949] [36:56.24] don't have this simplifying guideline
[L950] [36:59.68] kind of underlying all this. You have to
[L951] [37:02.00] be aware of each piece of the
[L952] [37:04.08] technology, gauge how fast it's
[L953] [37:06.64] improving, how whether it's they can
[L954] [37:09.52] deliver on what's going on and then you
[L955] [37:12.24] assemble that together and make your
[L956] [37:14.48] bets. We're, you know, there's a paper
[L957] [37:16.64] that we've just got approved that I
[L958] [37:18.96] think we're going to put on archive
[L959] [37:20.16] soon, which is, uh, talking about the
[L960] [37:23.12] Google TPU line and pretty remarkably,
[L961] [37:26.24] uh, the Google TPU line particularly for
[L962] [37:28.32] training has stayed pretty constant in
[L963] [37:31.36] the basic architecture design, uh,
[L964] [37:34.32] things have gotten bigger and faster,
[L965] [37:36.80] but the if you look at the the the
[L966] [37:39.28] design of it, going back to the first
[L967] [37:41.36] training TPU, it's that block diagram
[L968] [37:44.00] still works.
[L969] [37:45.12] uh all these you know a decade later. So
[L970] [37:47.84] it you know the people who designed that
[L971] [37:50.08] in whatever 2015 or two did a really
[L972] [37:52.80] great job. Uh but the main components of
[L973] [37:55.76] a a big matrix multiply unit the
[L974] [37:57.84] so-called high bandwidth memory um uh a
[L975] [38:01.84] vector unit to go with the matrix unit
[L976] [38:03.92] and the basic building blocks are still
[L977] [38:06.08] there. I think in your career with the
[L978] [38:08.64] CPUs, benchmarks were a huge they played
[L979] [38:11.12] a huge role in in measuring which
[L980] [38:14.80] computer architectures were performant
[L981] [38:16.40] and not in this this new space of uh
[L982] [38:20.00] floatingoint operations for AI. Is there
[L983] [38:22.56] a benchmark that people use for GPUs and
[L984] [38:25.20] can you also apply it for TPUs?
[L985] [38:27.84] >> I was you know I and some friends were
[L986] [38:30.64] helped involved in called the ML Perf
[L987] [38:32.72] effort. So it was inspired by the spec
[L988] [38:36.40] CPU effort was the spec benchmarks that
[L989] [38:40.00] there were these competing companies and
[L990] [38:41.68] they'd all make claims about theirs was
[L991] [38:44.00] better than the others and they realized
[L992] [38:45.12] that wasn't good for the industry. So
[L993] [38:47.20] they agreed on a set of benchmarks. So
[L994] [38:49.20] the ML Perf effort is uh that's run now
[L995] [38:52.48] but what's called ML comments is an
[L996] [38:53.92] attempt to do that is if we're going to
[L997] [38:56.08] do this comparisons
[L998] [38:58.24] let's um let's let's not argue about
[L999] [39:01.52] what the benchmarks are. So that's a
[L1000] [39:03.84] serious effort in that kind of
[L1001] [39:05.68] interestingly what's happened I'd say is
[L1002] [39:08.80] because
[L1003] [39:10.72] uh there's two pieces to u the design
[L1004] [39:14.00] there's the the machine learning
[L1005] [39:15.76] libraries that are uh to implement a lot
[L1006] [39:19.20] of features that you need for for these
[L1007] [39:21.84] applications and the libraries will even
[L1008] [39:24.40] be rewritten for specific applications
[L1009] [39:27.20] rather than just having general
[L1010] [39:28.80] libraries. This has turned out to be a
[L1011] [39:31.12] big advantage for Nvidia because they
[L1012] [39:32.80] have a large corporation with lots of
[L1013] [39:35.04] people that are available, lots of
[L1014] [39:37.12] engineers who could build these
[L1015] [39:38.48] libraries for them. So, it's turned out
[L1016] [39:41.60] um um not quite a it's not a it's not a
[L1017] [39:45.36] neutral evaluation, right? It's it's the
[L1018] [39:49.12] architecture plus the the libraries that
[L1019] [39:53.36] go with it and the compiler too, but
[L1020] [39:56.24] specifically the libraries that you
[L1021] [39:58.00] tailor each time. So Nvidia brings out
[L1022] [40:00.80] when they announce the new architecture
[L1023] [40:02.88] they create a new set of they modify the
[L1024] [40:05.44] libraries to run that really well or to
[L1025] [40:08.24] run applications really well. So that's
[L1026] [40:10.80] a powerful combination kind of in
[L1027] [40:13.20] business terms people referred to
[L1028] [40:15.36] Nvidia's having this CUDA moat but and
[L1029] [40:19.36] part of it is CUDA the programming
[L1030] [40:21.20] language but a big part of it is the
[L1031] [40:22.64] libraries that Nvidia Nvidia makes. So
[L1032] [40:25.84] this has made it difficult for for
[L1033] [40:27.76] startups to be able to compete with
[L1034] [40:29.36] Nvidia partly because
[L1035] [40:32.80] you know they didn't put enough emphasis
[L1036] [40:35.04] in the software and partly because you
[L1037] [40:37.52] know Nvidia just has many more engineers
[L1038] [40:40.40] than they do to be able to tailor the
[L1039] [40:42.00] libraries. So it's the libraries plus
[L1040] [40:44.80] the architecture that's this this
[L1041] [40:47.04] powerful advantage why most people do
[L1042] [40:50.00] things on GPUs. Now Google has been able
[L1043] [40:52.96] to develop their own libraries. Uh they
[L1044] [40:55.52] don't have as many engineers. They use
[L1045] [40:57.68] compilers more uh than I think Nvidia
[L1046] [41:00.96] does. So they they have a set of
[L1047] [41:02.80] libraries that they can do. But up until
[L1048] [41:05.28] recently, Google has
[L1049] [41:07.84] it's all been internal. It's just for
[L1050] [41:09.44] Google to use or you could use it via
[L1051] [41:11.44] the cloud. Um but uh you these startups
[L1052] [41:15.36] have u you know have to have a
[L1053] [41:18.00] difficulty as a result. That's why the
[L1054] [41:20.72] ML Perf hasn't been as popular. Not
[L1055] [41:22.96] everybody runs them because uh Nvidia
[L1056] [41:25.68] runs them really well, really better
