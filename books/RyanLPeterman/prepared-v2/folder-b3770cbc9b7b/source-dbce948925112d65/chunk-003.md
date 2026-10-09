Chunk 3; segments 748–1119. Start may repeat the previous chunk for context.

# Dropbox’s Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling

Source ID: source-dbce948925112d65
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Dropbox’s_Former_Most_Senior_Eng_Building_Great_Systems_and_Advice_for_the_AI_Era_James_Cowling_en.txt
Video: https://www.youtube.com/watch?v=3XkmNSuHFmY

[L757] [25:24.72] Uh but I think at the time it it
[L758] [25:26.12] certainly made sense for us as a
[L759] [25:27.40] company.
[L760] [25:28.92] >> Can you give an example of uh tight
[L761] [25:31.68] understanding of your workloads leading
[L762] [25:33.52] to like something you could do that S3
[L763] [25:36.24] couldn't?
[L764] [25:36.84] >> Yeah, absolutely. So, for example, I
[L765] [25:38.64] know
[L766] [25:39.88] that um well, I'll try not to leak any
[L767] [25:42.12] confidential data, right? But when you
[L768] [25:44.56] when you upload a file to Dropbox, there
[L769] [25:46.72] is a pattern of access, right? Um so,
[L770] [25:49.76] typically people um access the file very
[L771] [25:52.52] quickly shortly afterwards um because
[L772] [25:55.36] you're sharing it with someone or maybe
[L773] [25:57.44] Dropbox is processing that file to
[L774] [25:59.84] generate an image preview. And then it
[L775] [26:01.64] decays at a certain rate. And so, we
[L776] [26:03.80] understand in general the average block
[L777] [26:06.60] size, and we um understand also the
[L778] [26:09.56] access pattern. So, we could do things
[L779] [26:12.24] like at a certain point we had these two
[L780] [26:14.96] um clusters. One was at One was
[L781] [26:17.48] um designed for kind of temporary
[L782] [26:20.28] storage that was kind of
[L783] [26:21.80] storage-inefficient
[L784] [26:23.44] but access-efficient. So, it was very
[L785] [26:25.96] cheap to read and write to, but it was
[L786] [26:28.04] inefficient to store. And data would get
[L787] [26:30.04] written to there first, and then in the
[L788] [26:32.16] background it would get um moved in bulk
[L789] [26:35.40] to this colder storage system.
[L790] [26:37.68] And this colder storage system was far
[L791] [26:39.20] more static.
[L792] [26:40.80] And so, it was able to have kind of more
[L793] [26:42.40] efficient algorithms and and and be
[L794] [26:44.80] written to in bulk. And if it went down
[L795] [26:47.64] for writes, that was no problems because
[L796] [26:49.64] it wasn't in the live path. And so, we
[L797] [26:51.52] were able to trade off, again, like
[L798] [26:52.84] systems is all about trade-offs. So, we
[L799] [26:54.80] were able to trade off the the live data
[L800] [26:56.68] write path from the long-term read path.
[L801] [26:59.52] Um that's one of many examples where
[L802] [27:02.04] knowing the size of your data, where
[L803] [27:03.84] it's accessed from, how frequently it
[L804] [27:05.48] gets accessed, how um how long it takes
[L805] [27:07.52] to delete that data, you can really tune
[L806] [27:10.12] a system
[L807] [27:11.44] um to your workload. If you know, stuff
[L808] [27:13.68] like looking at
[L809] [27:15.36] um
[L810] [27:16.60] even things down to knowing how much
[L811] [27:18.52] power to put in a rack. You know, you
[L812] [27:20.48] have a rack of hardware, there's a power
[L813] [27:23.08] distribution unit, a PDU, at the top of
[L814] [27:24.72] that rack. It has a circuit breaker
[L815] [27:26.64] which can handle a certain number of
[L816] [27:28.12] amps.
[L817] [27:29.56] We would have to figure out, you know,
[L818] [27:31.56] how many amps are required for that rack
[L819] [27:33.96] based on access patterns. And there were
[L820] [27:35.68] times where we got it slightly wrong.
[L821] [27:37.36] There was times where
[L822] [27:38.84] we got to maybe a bad batch of hardware,
[L823] [27:41.16] and disks were failing too frequently.
[L824] [27:43.20] And as a result, we were re-replicating
[L825] [27:44.68] the data
[L826] [27:45.88] more regularly, and I was getting, you
[L827] [27:47.12] know, messages from the data center team
[L828] [27:48.44] saying, "Hey,
[L829] [27:49.76] we're I'm in the rack's really hot right
[L830] [27:51.28] now." You know? So, that's the level of
[L831] [27:53.56] optimizations you can make when you get
[L832] [27:55.52] to that scale. Um but again, that's
[L833] [27:58.20] multi-exabyte scale. You know,
[L834] [28:01.08] million hard drive scale.
[L835] [28:03.24] >> Yeah, when I was reading about this
[L836] [28:04.48] migration, I saw somewhere in the
[L837] [28:06.20] migration
[L838] [28:07.60] you initially started with Go, and then
[L839] [28:10.84] the racks or something that you're
[L840] [28:12.52] running on the hardware itself was
[L841] [28:14.40] ooming too much or
[L842] [28:16.00] requesting too much memory. And then you
[L843] [28:18.36] migrated to Rust.
[L844] [28:20.12] >> So, initially, the prototype was in
[L845] [28:22.16] Python, if you can believe that.
[L846] [28:24.16] And to be fair, Python is actually
[L847] [28:25.60] pretty efficient for IO. I think people
[L848] [28:27.24] give Python a a bad rap for IO-bound
[L849] [28:30.16] workloads. It's pretty good at IO. Um
[L850] [28:33.08] but obviously, um not great for
[L851] [28:35.08] concurrency, not great for memory
[L852] [28:36.32] management, and um very hard to
[L853] [28:38.44] refactor.
[L854] [28:39.76] And it was critical this system was
[L855] [28:41.24] correct. And so, we migrated everything
[L856] [28:44.36] to Go, and we built most of the storage
[L857] [28:46.12] system in Go. This is before Go was in
[L858] [28:48.92] general availability. I think it was
[L859] [28:50.12] before Go was GA. Um and we built the
[L860] [28:53.20] system in Go. Go is a great language for
[L861] [28:55.52] concurrency, a great language for
[L862] [28:56.96] proxies. You know, it's a really well
[L863] [28:59.24] designed for like servers that moved out
[L864] [29:01.48] of one place to another place.
[L865] [29:03.28] At a certain point though,
[L866] [29:05.00] we would have, you know, let's just pick
[L867] [29:07.08] a number. Let's say a million. Let's say
[L868] [29:08.20] we have a million nodes in the system.
[L869] [29:10.52] And every node has um
[L870] [29:13.92] some amount of memory, some amount of
[L871] [29:15.68] disk, some amount of sheet metal in the
[L872] [29:17.92] chassis, right? And we would itemize all
[L873] [29:20.40] these things. You'd have a pie chart of
[L874] [29:22.72] of how much money is spent on all the
[L875] [29:24.84] things. And it would still have stuff
[L876] [29:26.28] like, yeah, sheet metal and screws and
[L877] [29:27.80] stuff. And so, you're trying to optimize
[L878] [29:30.36] the storage and a big problem for us was
[L879] [29:33.88] the amount of memory um
[L880] [29:36.52] these nodes were using. Not just the
[L881] [29:38.24] memory that we're using, but the
[L882] [29:39.60] unpredictability of it. Uh with, you
[L883] [29:42.40] know, with Go having a runtime and and
[L884] [29:45.80] you know, in a storage system, an out of
[L885] [29:47.64] memory error is pretty bad.
[L886] [29:49.96] Because if a node runs out of memory and
[L887] [29:51.48] restarts, that looks like a disk
[L888] [29:53.16] failure.
[L889] [29:54.60] So, that looks a lot like a disk has
[L890] [29:56.04] failed and has to be re-replicated. And
[L891] [29:57.68] so, a batch of nodes OOMing
[L892] [30:01.12] can lead to cascading failures
[L893] [30:02.76] throughout the system.
[L894] [30:04.28] Because maybe um I remember a time it
[L895] [30:08.24] was a band. It might have been De La
[L896] [30:09.48] Soul. I can't remember. There was a band
[L897] [30:10.88] released an album on Dropbox.
[L898] [30:13.40] So, there was a big spike in load
[L899] [30:15.84] um to a to a
[L900] [30:17.84] a few files. So, it was very, very high
[L901] [30:20.80] um bandwidth and it caused the the
[L902] [30:23.16] machines to OOM. So, the those machines
[L903] [30:25.64] uh OOMed, those disks OOMed. Um and so,
[L904] [30:28.44] as a result, no problems. The system
[L905] [30:30.40] went to try to recover that data from a
[L906] [30:32.48] whole bunch of other replicas, right?
[L907] [30:34.84] Now, all of the sudden you've taken one
[L908] [30:37.08] amount one fire hose worth of load
[L909] [30:39.40] coming in and you've turned this into
[L910] [30:41.00] seven fire hoses worth of load coming,
[L911] [30:42.68] cuz now you have to do a more expensive
[L912] [30:44.28] reconstruction operation, right? So now
[L913] [30:46.36] you've seven x the load. And these are
[L914] [30:48.20] the kind of cyclical kind of behaviors
[L915] [30:51.12] that can lead to something called
[L916] [30:52.04] congestion collapse. Congestion collapse
[L917] [30:53.88] is when
[L918] [30:55.04] workload to a system crosses a threshold
[L919] [30:57.28] where it all kind of collapses.
[L920] [30:59.76] So
[L921] [31:00.80] designing against congestion collapse is
[L922] [31:02.48] really the hardest part or one of the
[L923] [31:04.48] hardest parts of Magic Pocket, which is
[L924] [31:06.00] the name of the storage system. Um so
[L925] [31:08.72] ultimately we switched to Rust for the
[L926] [31:12.20] storage nodes themselves. And this
[L927] [31:13.92] again, this is before Rust was in GA, so
[L928] [31:16.36] that was a bit of a risky move.
[L929] [31:18.16] Uh but we rewrote um
[L930] [31:20.64] the switch to Rust coincided with
[L931] [31:22.64] getting rid of the file system entirely
[L932] [31:24.32] on the disks and directly addressing the
[L933] [31:27.04] the disk disk heads. So there was a
[L934] [31:29.28] there's an instruction set, I think it's
[L935] [31:30.48] called ZBC, zone based block control,
[L936] [31:33.60] something like that. There's there's a
[L937] [31:34.52] there's an instruction set for accessing
[L938] [31:36.08] disks that we were using.
[L939] [31:38.16] The disk manufacturers gave us the draft
[L940] [31:39.96] specs of these new disks and we were
[L941] [31:41.80] operating off the draft specs and
[L942] [31:43.80] directly controlling the the disks. And
[L943] [31:45.80] so
[L944] [31:46.68] all that product was tied up um together
[L945] [31:49.60] um
[L946] [31:50.72] into a product called DiscoTech.
[L947] [31:52.64] It was the disk technology project. Um
[L948] [31:55.44] and ultimately, if you look at that pie
[L949] [31:57.24] chart, one congestion collapse stopped
[L950] [31:59.36] and reliability improved. But if you
[L951] [32:01.08] looked at the pie chart of where all the
[L952] [32:02.56] money was going, it really shifted to be
[L953] [32:05.00] almost all disks. And what we wanted to
[L954] [32:07.16] do is get that pie chart to be
[L955] [32:10.08] almost all the money spent on disks and
[L956] [32:12.48] as little money spent on RAM, on
[L957] [32:14.24] compute, on network, on power, on sheet
[L958] [32:16.60] metal, etc.
[L959] [32:17.88] >> The cascading failure you mentioned, was
[L960] [32:20.00] there So that that happened and then
[L961] [32:22.44] there was a postmortem.
[L962] [32:23.60] >> I don't think we needed a postmortem.
[L963] [32:24.88] Well, I think we we knew as it was
[L964] [32:26.20] happening.
[L965] [32:27.34] >> [laughter]
[L966] [32:28.24] >> I think when I was getting paged in the
[L967] [32:29.88] middle of the night on these things, I
[L968] [32:31.36] would you know, you'd be pretty pretty
[L969] [32:32.92] evident. And so look, this is the again,
[L970] [32:35.52] this is an argument in favor of the
[L971] [32:36.96] cloud. All right. Imagine you've spent
[L972] [32:40.16] hundreds of millions of dollars on a on
[L973] [32:42.60] a storage system and it's out in
[L974] [32:43.96] production and it's on physical
[L975] [32:46.00] hardware.
[L976] [32:47.40] You can't just go and put new memory
[L977] [32:50.24] chips in every one of them. I mean, you
[L978] [32:51.72] can, but you have to pay people to come
[L979] [32:53.80] in and swap them out, you know. And so
[L980] [32:55.76] that That's a tricky place. And so as a
[L981] [32:59.00] And this is what This is what I love
[L982] [33:00.28] about industry. You know, cuz in like
[L983] [33:03.24] some of the more um
[L984] [33:05.08] challenging moments on Magic Pocket were
[L985] [33:07.64] stuff like in one week
[L986] [33:09.84] This is a weird coincidence. Two trucks
[L987] [33:12.16] crashed that were delivering servers. So
[L988] [33:13.84] there's two trucks showing up to deliver
[L989] [33:16.12] racks and then they both crashed. I
[L990] [33:17.32] don't know, you know, the drivers were
[L991] [33:18.44] okay. So we lost capacity for 2 weeks.
[L992] [33:21.72] Uh so the So we lost capacity for for
[L993] [33:23.68] more than 2 weeks. For for for probably
[L994] [33:25.48] 6 weeks.
[L995] [33:26.96] Um
[L996] [33:28.08] What do you do?
[L997] [33:29.84] What happens, you know, is is the
[L998] [33:31.40] equivalent of your disk filling up on
[L999] [33:32.72] your laptop except it's, you know, it's
[L1000] [33:34.68] it's a million disks.
[L1001] [33:36.56] And you can't tell the customers to go
[L1002] [33:38.48] away. You can't delete their files. So a
[L1003] [33:40.48] lot of a lot of tricky um a lot of
[L1004] [33:43.52] tricky capacity work. Um and ultimately
[L1005] [33:46.36] what that what that led to was trying to
[L1006] [33:48.60] build in
[L1007] [33:51.00] all these protections against the
[L1008] [33:52.64] unknowns. You know, making sure we had
[L1009] [33:55.48] the right amount of buffer planned out
[L1010] [33:57.48] for anything bad that could happen.
[L1011] [33:59.00] Making sure we we designed the system so
[L1012] [34:01.32] they couldn't be congestion collapse so
[L1013] [34:02.92] there wouldn't be memory spikes.
[L1014] [34:05.08] Um and
[L1015] [34:06.96] you know, at one point there's a there's
[L1016] [34:08.44] a process called I think it's called
[L1017] [34:09.56] FMEA
[L1018] [34:11.16] which is like a threat modeling process
[L1019] [34:12.80] where you had a big spreadsheet and you
[L1020] [34:14.44] kind of write down every bad thing that
[L1021] [34:16.72] could possibly happen and then, you
[L1022] [34:18.52] know, all the how bad it would be if it
[L1023] [34:20.64] happened.
[L1024] [34:21.84] Existential risk.
[L1025] [34:23.80] Does someone die? You know, if there's a
[L1026] [34:25.20] fire in the data center. All these kind
[L1027] [34:26.56] of things get put into the spreadsheet.
[L1028] [34:28.40] And you kind of do a bit of a almost
[L1029] [34:30.36] pre-mortem kind of work to figure out
[L1030] [34:33.04] all the all the potential failure modes,
[L1031] [34:35.12] and then design around them. And I I
[L1032] [34:36.92] that's I love that work. I I I really um
[L1033] [34:40.56] I don't know. I do like the firefight. I
[L1034] [34:42.40] I like the
[L1035] [34:44.16] I don't I can't say I like getting paged
[L1036] [34:45.88] because
[L1037] [34:47.24] I've spent my whole life on call,
[L1038] [34:49.32] but I do like that rubber hits the road
[L1039] [34:51.80] stuff. I like that
[L1040] [34:54.32] wow, there's congestion collapse and and
[L1041] [34:56.04] there's no one that can help you. And
[L1042] [34:58.28] so, you've [snorts] got to
[L1043] [34:59.84] think through this problem.
[L1044] [35:01.44] >> When I worked on infrastructure at
[L1045] [35:02.84] Instagram, we had this concept of DEFCON
[L1046] [35:04.92] knobs, which are basically these configs
[L1047] [35:08.32] that you could flip that would
[L1048] [35:10.40] gracefully degrade your system, where
[L1049] [35:12.96] you can still operate it, but you know,
[L1050] [35:15.04] maybe in the case of Dropbox, you store
[L1051] [35:17.68] less replicas. So, you take on a
[L1052] [35:20.20] temporary increase of
[L1053] [35:22.80] uh risk in losing data because you need
[L1054] [35:25.24] to. Uh did you have something like that,
[L1055] [35:27.32] and did you flip it in that type of
[L1056] [35:29.04] case?
[L1057] [35:29.52] >> Never when it came to durability. So, I
[L1058] [35:32.00] mean, we just had a just absolute zero
[L1059] [35:34.88] non-negotiable, like there was no room
[L1060] [35:36.88] for negotiation on on user durability.
[L1061] [35:39.52] And so, um
[L1062] [35:41.32] we had those knobs for background
[L1063] [35:42.72] processes, for CPU and and memory, for
[L1064] [35:44.56] example. So, if there was like a spike
[L1065] [35:46.00] in load, you could turn off background
[L1066] [35:48.12] processes and and turn off um you know,
[L1067] [35:50.80] um the the test load, for example, on
[L1068] [35:52.88] the system. Eventually, we we built this
[L1069] [35:55.16] system called
[L1070] [35:57.64] trampoline.
[L1071] [35:58.92] And what trampoline did was um which
[L1072] [36:01.76] actually was a it it saved us a ton of
[L1073] [36:03.60] money, right? When if we ever got too
[L1074] [36:06.44] close to the threshold, we would just
[L1075] [36:08.40] start writing data to S3.
[L1076] [36:10.36] Cuz it's right there, right? So, it's um
[L1077] [36:13.32] you can run your capacity way closer to
[L1078] [36:15.84] the edge if you're willing under worst
[L1079] [36:18.16] case scenarios just to just to dump 30
[L1080] [36:20.84] petabytes on S3, and then move it back
[L1081] [36:23.32] when it's done. And now, it didn't that
[L1082] [36:25.24] didn't happen very often. We would do it
[L1083] [36:26.64] to test it. We would do that to make
[L1084] [36:28.00] sure the system worked.
[L1085] [36:29.68] But um yeah, being able to have a escape
[L1086] [36:32.84] hatch for worst case scenario was really
[L1087] [36:34.80] nice.
[L1088] [36:35.72] >> As you said, S3 is kind of
[L1089] [36:37.92] it's like elastic storage.
[L1090] [36:39.60] >> Exactly.
[L1091] [36:40.84] >> When I looked at this project, it's such
[L1092] [36:44.00] a massive migration and my first thought
[L1093] [36:46.52] is how do you coordinate this whole
[L1094] [36:49.00] project without breaking the system as
[L1095] [36:51.68] it's running?
[L1096] [36:53.20] How Yeah, what are your thoughts on
[L1097] [36:55.80] doing such a large migration without
[L1098] [36:57.64] breaking things?
[L1099] [36:58.28] >> Yeah. Now, I mean in
[L1100] [37:00.40] in terms of the engineers that like
[L1101] [37:02.00] built the initial version of the system,
[L1102] [37:04.20] it was a handful.
[L1103] [37:05.88] Three, four, five, six engineers. It
[L1104] [37:07.48] wasn't a team of a thousand, you know.
[L1105] [37:09.24] It was a very, very small team. And so
[L1106] [37:11.64] um
[L1107] [37:12.68] how do you build such a large system
[L1108] [37:15.60] with a small number of people and then
[L1109] [37:16.84] how do you do a high-risk migration?
[L1110] [37:19.20] Uh
[L1111] [37:21.04] One of these one one thing you do is you
[L1112] [37:22.76] keep things simple. You you try so so so
[L1113] [37:25.44] hard to
[L1114] [37:27.16] build very cleanly abstracted, simple
[L1115] [37:30.28] systems that their failure modes are
[L1116] [37:32.08] very understandable. Um and so they and
[L1117] [37:34.60] they and they decouple so they don't
[L1118] [37:36.16] have congestion, collapse, etc. So,
[L1119] [37:38.24] focusing on simplicity this it gets
[L1120] [37:40.52] tricky by the way with people doing
[L1121] [37:42.56] agentic development. They They're not
[L1122] [37:44.40] the best at building simple systems.
[L1123] [37:45.88] Like simplicity is still the domain of
[L1124] [37:47.88] human beings for now. But um a big focus
[L1125] [37:50.76] on simplicity. The other was um
[L1126] [37:53.76] you know, this this very thick layer of
[L1127] [37:56.24] validation checks during this migration.
[L1128] [37:58.64] And And in fact, um we had uh
