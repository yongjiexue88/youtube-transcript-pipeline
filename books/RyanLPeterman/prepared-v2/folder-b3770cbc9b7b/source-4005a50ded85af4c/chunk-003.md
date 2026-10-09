Chunk 3; segments 690–1034. Start may repeat the previous chunk for context.

# Turing Award Winner: Thinking Clearly, Paxos vs Raft, Working With Dijkstra | Leslie Lamport

Source ID: source-4005a50ded85af4c
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Thinking_Clearly,_Paxos_vs_Raft,_Working_With_Dijkstra_Leslie_Lamport_en.txt
Video: https://www.youtube.com/watch?v=U719vQz-WFs

[L699] [32:59.12] fork between you know each fork would be
[L700] [33:01.68] shared with two people and uh but and I
[L701] [33:04.64] think realized it was because of that
[L702] [33:06.80] cute story that that problem was was
[L703] [33:09.76] popular. And so I decided that you know
[L704] [33:13.60] this this our work needed a cute story
[L705] [33:17.36] you know a nice story and I in invented
[L706] [33:19.52] Byzantine generals with the idea being
[L707] [33:21.84] that you have a group of you know for
[L708] [33:24.56] the for the one failure case you have
[L709] [33:27.12] four generals who have to agree whether
[L710] [33:29.04] or not to attack. uh and if they all
[L711] [33:32.48] attack
[L712] [33:34.00] uh they'll win the battle. But if only
[L713] [33:37.76] some of them attack or if even if three
[L714] [33:39.92] of them attack they'll win the battle.
[L715] [33:42.24] But if only two attack you know they
[L716] [33:44.88] would lose. But one of the the generals
[L717] [33:48.32] might be uh a traitor. And so how could
[L718] [33:52.00] you you know solve this problem? And so
[L719] [33:54.56] so it's phrased in terms of these
[L720] [33:56.40] generals having to communicate and
[L721] [33:58.24] decide whether to make the single
[L722] [34:00.32] decision whether to uh attack or or
[L723] [34:04.24] retreat. Um and you know I called it the
[L724] [34:08.88] Byzantine generals uh problem.
[L725] [34:11.76] >> I saw in your your uh notes about the
[L726] [34:15.36] problem that there was maybe a subset of
[L727] [34:18.32] the problem or a prior version that was
[L728] [34:20.16] called the Chinese general's problem or
[L729] [34:22.48] something like that.
[L730] [34:22.96] >> Oh yeah. that yeah I was uh there was a
[L731] [34:26.00] different problem that uh Jim Gray uh
[L732] [34:32.00] described uh as an impossibility result
[L733] [34:36.56] basically it's called the Chinese
[L734] [34:38.16] generals problem and I I won't bother
[L735] [34:40.56] going into what it is and so that gave
[L736] [34:43.12] me the idea of generals uh I actually
[L737] [34:46.80] initially thought of the idea of
[L738] [34:49.12] Albanian generals because at that time
[L739] [34:52.16] Albania was a black hole as far as the
[L740] [34:55.04] rest of the world was concerned. It was
[L741] [34:56.64] a communist regime, a part of the the
[L742] [34:58.88] Soviet uh block, but it was even more
[L743] [35:03.04] Soviet than the Soviet Republic and and
[L744] [35:05.28] and you know, more restrictive. So
[L745] [35:08.40] someone uh my boss said, "Well, you
[L746] [35:11.52] know, there are Albanians in the world,
[L747] [35:13.44] so shouldn't that so should have a
[L748] [35:15.92] different name?" And then I I realized
[L749] [35:18.08] that Byzantine there aren't any
[L750] [35:19.60] Byzantiums Byzantines around and that
[L751] [35:23.28] was the perfect name. So
[L752] [35:25.36] >> it's interesting to me in the story that
[L753] [35:27.84] because this isn't the first time the
[L754] [35:30.16] problem was specified but it was the
[L755] [35:33.04] first time that you had named it uh um
[L756] [35:36.08] gave it a good catchy name essentially
[L757] [35:38.00] and and uh you know added some
[L758] [35:40.08] additional results. What was it that you
[L759] [35:42.72] saw in that problem that made it
[L760] [35:44.80] interesting? Or rather like how do you
[L761] [35:46.64] know that a problem is worth putting
[L762] [35:49.36] extra time into? Oh, well this one it
[L763] [35:51.68] was because you know the it was obvious
[L764] [35:54.96] that people were going to be building
[L765] [35:56.88] that computers were going to fly our
[L766] [35:58.72] airplane fly airplanes and the reason in
[L767] [36:01.28] fact because was was that this was
[L768] [36:03.92] during the the time of the oil crisis in
[L769] [36:06.16] the 70s and that they knew people knew
[L770] [36:10.96] that they could build more
[L771] [36:12.56] energyefficient planes by reducing the
[L772] [36:15.84] size the the size of the control
[L773] [36:17.68] surfaces.
[L774] [36:19.20] But that made the plane aerodynamically
[L775] [36:21.44] unstable. Uh and a a pilot couldn't make
[L776] [36:25.44] the all the adjustments needed to, you
[L777] [36:28.08] know, to keep it flying, but a computer
[L778] [36:30.32] could. So it was clear the future was,
[L779] [36:33.76] you know, airplanes were going to be
[L780] [36:35.60] flying be flown by computers as they
[L781] [36:38.00] are, you know, today. uh and
[L782] [36:42.32] uh people didn't realize they thought
[L783] [36:45.44] that oh if you want to be able to
[L784] [36:47.92] tolerate one fault you just use three
[L785] [36:50.16] computers
[L786] [36:51.68] and they didn't realize that you know
[L787] [36:53.84] with arbitrary faults you need four and
[L788] [36:56.80] so that was a really important result
[L789] [36:58.80] and that's why I believe that it it
[L790] [37:00.64] needed to to be well known
[L791] [37:03.44] >> generally when you look at the problems
[L792] [37:05.04] that you are solving with your work Um,
[L793] [37:09.68] how'd you decide? Cuz if you're working
[L794] [37:11.44] at a company, you can decide based off
[L795] [37:13.84] of maybe the I guess the impact to the
[L796] [37:16.32] company like is it going to make more
[L797] [37:18.00] money or save cost or something like
[L798] [37:19.68] that. But I wonder in your work across
[L799] [37:22.32] your career um you know think about the
[L800] [37:27.04] bakery problem or some of your later
[L801] [37:29.92] work as well. How do you know it's it's
[L802] [37:32.72] so open-ended. How do you know which
[L803] [37:34.16] problems are uh the ones worthwhile?
[L804] [37:37.44] Throughout my career, I worked for
[L805] [37:39.60] private companies, you know, not, you
[L806] [37:42.16] know, not in academia or or for the
[L807] [37:44.96] government. Uh, and so some problems
[L808] [37:49.04] arose because of, you know, sometimes,
[L809] [37:53.20] you know, an engineer would have a
[L810] [37:54.72] problem and come come to me. And so, uh,
[L811] [37:58.56] you know, DIS Paxos, for example, was
[L812] [38:01.04] was a case of that that somebody
[L813] [38:02.88] actually wanted an algorithm to do what
[L814] [38:05.04] it did. You mentioned earlier Paxos and
[L815] [38:09.04] I know that's one of your your most
[L816] [38:11.20] famous uh works. Curious about the story
[L817] [38:14.40] behind maybe that paper and the problem
[L818] [38:17.04] you're solving.
[L819] [38:17.84] >> Well, the problem I was trying is
[L820] [38:19.68] exactly the same problem as I was
[L821] [38:21.68] solving in the the Byzantine general's
[L822] [38:24.32] work uh basically building a a fault
[L823] [38:28.48] tolerant state machine. But by that time
[L824] [38:32.16] it was you know the in the faults that
[L825] [38:34.96] interested industry were ones where
[L826] [38:37.76] failure meant that the computer just
[L827] [38:39.36] stopped the not not that it did
[L828] [38:42.32] arbitrary things. So uh the paxos is an
[L829] [38:46.40] algorithm for uh
[L830] [38:49.76] for for building fault tolerance systems
[L831] [38:52.72] for handling that class of faults. uh
[L832] [38:56.24] and
[L833] [38:57.84] the people I was working at was which
[L834] [39:01.12] the it was the deck circ
[L835] [39:04.88] was in which I joined in 1985 and they
[L836] [39:07.84] built a
[L837] [39:09.84] uh
[L838] [39:11.60] one of the first operating systems that
[L839] [39:15.28] uh was a a distributed operating system.
[L840] [39:20.16] Uh so that
[L841] [39:23.28] um basically everybody had the they
[L842] [39:26.72] basically these are the people who had
[L843] [39:28.88] come from Xerox Park and had invented
[L844] [39:31.44] personal computing but they also had the
[L845] [39:34.16] notion of distributed personal computing
[L846] [39:36.56] and they invented the Ethernet uh you
[L847] [39:39.60] know for that. So they basically all of
[L848] [39:42.48] the uh computers in the building were on
[L849] [39:46.96] a single Ethernet network and shared a
[L850] [39:50.64] common storage uh and they had an
[L851] [39:53.92] algorithm for maintaining consistency of
[L852] [39:56.00] that storage and I didn't believe well
[L853] [39:58.16] they didn't have an algorithm they had
[L854] [40:00.08] an operating system with code that did
[L855] [40:02.88] that um and
[L856] [40:06.56] I didn't believe that what they what
[L857] [40:09.76] they did was possible. Uh,
[L858] [40:13.76] namely I I didn't think um
[L859] [40:19.60] well I forget exactly why I didn't think
[L860] [40:22.56] it was possible but at any rate I
[L861] [40:25.44] started you know trying to uh come up
[L862] [40:27.84] with a a an impossibility proof and
[L863] [40:31.12] start solidity proof well and an
[L864] [40:33.36] algorithm to solve this would have to do
[L865] [40:35.12] this and in order to do this it would
[L866] [40:37.12] have to do that and at some point I
[L867] [40:39.84] stopped and said oh this isn't a proof.
[L868] [40:42.16] It it can't. This is an algorithm that
[L869] [40:43.92] does it.
[L870] [40:46.00] >> You said that they had code but not an
[L871] [40:49.68] algorithm.
[L872] [40:50.40] >> Yeah.
[L873] [40:51.12] >> Um what do you mean by that? when most
[L874] [40:54.16] people sit down and start writing
[L875] [40:55.76] programs that you know they start by
[L876] [40:58.24] thinking in terms of code
[L877] [41:01.04] and one of the things I learned fairly
[L878] [41:04.56] early in my career I don't remember
[L879] [41:06.48] exactly when that back in in the days
[L880] [41:10.24] when I started writing algorithms people
[L881] [41:13.44] talked about people were calling them
[L882] [41:15.68] programs and I was probably calling them
[L883] [41:18.32] programs too I mean I remember then at
[L884] [41:20.16] some point I realized that that wasn't
[L885] [41:22.40] wasn't talking about programs. I was
[L886] [41:25.84] talking about al interested in
[L887] [41:27.36] algorithms.
[L888] [41:28.88] Uh and an algorithm is something that's
[L889] [41:32.08] more abstract than a pro than than a
[L890] [41:34.08] program. U an algorithm can be you know
[L891] [41:37.44] a program is written in in some
[L892] [41:39.52] particular code. But an algorithm can be
[L893] [41:42.56] implemented if programs written in any
[L894] [41:45.12] any kinds of code. It's it's something
[L895] [41:46.72] that's that's at a higher level of of of
[L896] [41:50.88] abstraction. And of course I like that
[L897] [41:53.52] because abstraction is something I'm I
[L898] [41:55.52] was good at, you know, even without
[L899] [41:57.36] realizing that that's what I was doing.
[L900] [41:59.76] Uh
[L901] [42:01.76] and so
[L902] [42:05.04] what I've spent a large part of my
[L903] [42:07.68] career basically from maybe about you
[L904] [42:11.36] know 2000 or so onward uh was
[L905] [42:16.08] getting people who build concurrent
[L906] [42:18.08] systems
[L907] [42:20.08] uh to not just write code but to have an
[L908] [42:24.72] algorithm. Now a system does lots of
[L909] [42:27.60] things but there should be some kernel
[L910] [42:32.08] of the of the program that's that's
[L911] [42:36.80] involved with synchronizing the
[L912] [42:39.28] different processes
[L913] [42:41.92] or the distributed system the different
[L914] [42:43.68] computers and that code
[L915] [42:48.08] you know is very hard to get you know
[L916] [42:50.16] the you know that correct so you you
[L917] [42:53.36] don't want to think in terms of code
[L918] [42:54.96] because static coding, you know,
[L919] [42:57.60] conflates, you know, a lot of issues
[L920] [43:00.08] that are irrelevant to the concurrency
[L921] [43:02.48] aspect. And so you should be thinking,
[L922] [43:05.76] you know, first get an algorithm that
[L923] [43:08.40] does that synchronization and then
[L924] [43:10.72] implement that algorithm. I was looking
[L925] [43:14.24] at the Paxos paper and uh some of your
[L926] [43:17.20] notes about it and I saw that um there's
[L927] [43:20.96] a there's an eight-year gap between when
[L928] [43:24.24] you came up with the algorithm and when
[L929] [43:26.08] the the paper was actually published
[L930] [43:28.08] called Part-Time Parliament is the name
[L931] [43:30.32] of the paper. Why why is there an
[L932] [43:32.16] eight-year gap? Oh, well
[L933] [43:35.76] the re the referees originally said well
[L934] [43:38.88] this paper is okay you know not terribly
[L935] [43:41.44] important but fortunately Butler Lamson
[L936] [43:44.64] realized the importance of the algorithm
[L937] [43:48.08] and together with the idea of you know I
[L938] [43:51.28] guess you can implement anything because
[L939] [43:53.04] it's implementing a state machine uh and
[L940] [43:56.72] you know went about proceed uh
[L941] [43:58.72] procilitizing
[L942] [44:00.48] uh building your systems you know using
[L943] [44:03.52] paxos uh you know and and thinking in
[L944] [44:07.04] terms of state machines and uh so you
[L945] [44:11.28] know I wasn't uh so the idea was getting
[L946] [44:15.20] out so you know I was in no hurry to
[L947] [44:17.60] publish so you know I just let the paper
[L948] [44:20.96] sit and eventually uh there was a new
[L949] [44:24.48] editor that came along and uh
[L950] [44:29.04] uh
[L951] [44:30.72] he said that you know I think the status
[L952] [44:32.96] of the paper was that it was just uh you
[L953] [44:35.36] know it had been accepted but had no and
[L954] [44:37.76] needed revision and uh so he decided
[L955] [44:41.44] that yeah let's you know to to publish
[L956] [44:43.76] it and uh it was eventually published
[L957] [44:46.96] with little some a few things that uh to
[L958] [44:52.24] take well to to mention work that had
[L959] [44:55.28] been done in the in the in the uh
[L960] [44:58.00] interim and what I got is uh got a Keith
[L961] [45:03.76] Marzulo uh you know to do that part for
[L962] [45:07.44] me. Uh and uh so the story was that this
[L963] [45:11.36] manuscript this was that well the story
[L964] [45:13.76] about Paxos was that you know was a this
[L965] [45:16.32] happened you know centuries ago and you
[L966] [45:18.24] know this manuscript and uh I used that
[L967] [45:21.04] to the effect that you know when
[L968] [45:22.80] something you know the tales of
[L969] [45:24.48] something were I considered obvious and
[L970] [45:28.00] you know not interesting you know the
[L971] [45:30.40] the paper would say it's not clear how
[L972] [45:33.12] the Paxons what the Paxons did you know
[L973] [45:36.08] at this point but Um at any rate and uh
[L974] [45:40.16] so uh
[L975] [45:42.96] and Keith you know kept up the that idea
[L976] [45:47.36] that you know this was a you know a
[L977] [45:51.04] description of this ancient thing and
[L978] [45:52.96] and he wrote a you know a little prefix
[L979] [45:56.16] or a preface or something to to it and
[L980] [45:59.04] uh you know added maybe I think some uh
[L981] [46:02.00] references. I saw in your writing too
[L982] [46:04.88] when you were talking about presenting
[L983] [46:06.80] the paper initially,
[L984] [46:08.56] >> you even uh dressed up in like an
[L985] [46:10.96] Indiana Jones style archaeologist. Well,
[L986] [46:13.60] how did that go when you presented about
[L987] [46:15.36] this Paxos uh paper and algorithm?
[L988] [46:18.08] >> Well, I think the the lecture may have
[L989] [46:20.48] gone well, but uh I think nobody
[L990] [46:23.44] understood the algorithm where nobody
[L991] [46:24.96] understood the significance of the
[L992] [46:26.40] algorithm.
[L993] [46:27.44] >> It sounds like no one understood it
[L994] [46:29.04] except for Butler Lamson. What what did
[L995] [46:32.24] he see that made him unique? I guess.
[L996] [46:35.76] >> Well, he had a good understanding of
[L997] [46:37.68] building systems, you know, he really
[L998] [46:40.72] deserved his touring award. He was one
[L999] [46:43.12] of the original people at Xerox Park who
[L1000] [46:45.68] were building distributed uh personal
[L1001] [46:48.32] computing.
[L1002] [46:49.92] He and Chuck Thacker, I think, were
[L1003] [46:52.80] probably the two senior people, you
[L1004] [46:55.92] know, in that lab. I saw later there was
[L1005] [46:59.20] a paper which describes a new algorithm
[L1006] [47:02.80] which seems to solve the same problem.
[L1007] [47:04.80] The raft paper. I was wondering if you
[L1008] [47:07.84] read that and what your thoughts were on
[L1009] [47:09.52] on that versus Paxos. The authors of
[L1010] [47:12.88] that actually sent me a draft of the
[L1011] [47:15.20] original paper and I looked at it and
[L1012] [47:17.84] said uh I forget whether I said send it
[L1013] [47:23.20] back to me when you have an algorithm or
[L1014] [47:25.52] send that back to me when you have a
[L1015] [47:26.96] proof. I I forget which one it was and
[L1016] [47:30.40] uh you got the idea and they really they
[L1017] [47:32.88] they did write you know add a proof in
[L1018] [47:35.92] the paper or not. Uh yeah and I never
[L1019] [47:39.60] read future later versions and someone
[L1020] [47:42.80] whose judgment I value said you know had
[L1021] [47:45.92] read it and said that it's basically
[L1022] [47:47.76] it's it's the Paxos paper but no but
[L1023] [47:50.88] with some of the the tales left
[L1024] [47:55.28] unfinished by the Paxos paper uh by uh
[L1025] [47:59.52] you know filled some of the tales filled
[L1026] [48:01.76] in but they you know described it in a
[L1027] [48:06.16] in a very different Hey, the basic idea
[L1028] [48:09.44] of the what Paxos works is it's two
[L1029] [48:12.48] phases and you're trying to implement a
[L1030] [48:15.84] sequence of you know of decisions and it
[L1031] [48:20.00] turns out you can do the first phase
[L1032] [48:22.88] once
[L1033] [48:24.48] for a whole it involves a leader. So um
[L1034] [48:30.00] and the leader has to get elected. Uh so
[L1035] [48:33.60] but it turns out that you can do the
[L1036] [48:35.84] first uh phase once
[L1037] [48:39.84] uh and you don't have to do it again as
[L1038] [48:43.28] long as you have the same leader. Uh but
[L1039] [48:46.56] it's only the second part that you have
[L1040] [48:49.20] to do and then you have to elect the the
[L1041] [48:52.16] new leader if a new leader fails and do
[L1042] [48:55.04] the first part. So think about it in
[L1043] [48:57.44] those two phases. But the way people the
