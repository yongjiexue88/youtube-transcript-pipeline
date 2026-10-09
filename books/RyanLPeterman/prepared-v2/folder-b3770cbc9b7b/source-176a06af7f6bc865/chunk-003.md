Chunk 3; segments 743–1115. Start may repeat the previous chunk for context.

# The Co-Creator of Kubernetes: Engineering-Led Direction and Convincing Management | Brendan Burns

Source ID: source-176a06af7f6bc865
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/The_Co-Creator_of_Kubernetes_Engineering-Led_Direction_and_Convincing_Management_Brendan_Burns_en.txt
Video: https://www.youtube.com/watch?v=FKijpCEH9D8

[L752] [23:09.56] wrong time. I mean, I think one of the
[L753] [23:10.88] other things that is interesting about
[L754] [23:12.84] innovation that is disruptive is that
[L755] [23:16.48] it's a combination of
[L756] [23:19.36] being the person who has the idea and
[L757] [23:21.84] being in a time in which the idea can
[L758] [23:24.52] take off.
[L759] [23:25.92] Right? And it's So, you could have the
[L760] [23:27.80] idea, but it could just be the wrong
[L761] [23:29.20] time.
[L762] [23:30.32] And it won't do the same and it won't go
[L763] [23:32.24] in the same direction.
[L764] [23:33.56] >> That point on promotions, I think I
[L765] [23:36.64] mean, if you create the scope, not only
[L766] [23:38.88] is it is it obvious that that the credit
[L767] [23:41.96] should go to you, but it also feels kind
[L768] [23:44.44] of permissionless. Like you don't need
[L769] [23:46.00] to wait for
[L770] [23:47.48] um I guess management or someone to give
[L771] [23:50.40] you the opportunity. You can kind of
[L772] [23:52.00] create it, and so you have a lot more
[L773] [23:53.92] control in that in that process. One
[L774] [23:56.44] thing on the the business strategy, I
[L775] [23:58.48] guess before we leave that for
[L776] [23:59.80] Kubernetes, is at that time, Borg to me
[L777] [24:03.56] felt like a competitive advantage for
[L778] [24:05.52] Google. Like some secret infrastructure
[L779] [24:07.56] sauce.
[L780] [24:08.84] I would have thought people would be
[L781] [24:10.96] kind of worried about
[L782] [24:12.96] giving away any part of that to the
[L783] [24:14.68] industry. So, what was the the thinking
[L784] [24:17.32] there? How how would you convince people
[L785] [24:19.20] that hey,
[L786] [24:20.36] it's okay?
[L787] [24:21.28] >> Yeah, I mean, I think that there was a
[L788] [24:22.68] little bit of that.
[L789] [24:24.08] Um
[L790] [24:24.76] and I think you know, to to be a little
[L791] [24:27.56] bit make it into a little bit of a joke
[L792] [24:29.16] or whatever, I sort of one of the things
[L793] [24:31.08] I said to people was, you know, it's not
[L794] [24:32.84] like you Men in Black flash people as
[L795] [24:34.96] they leave Google.
[L796] [24:36.56] Right? Like, you know, it's not like
[L797] [24:38.24] everybody comes to Google and they just
[L798] [24:39.28] stays there forever, right? And so, and
[L799] [24:41.28] in fact, as we talked to people at
[L800] [24:42.56] Facebook, as we talked to people at
[L801] [24:43.92] Twitter, we talked to people at other,
[L802] [24:46.36] you know, scale-out tech companies, like
[L803] [24:47.92] they were all building this stuff.
[L804] [24:49.72] The the this it wasn't really a secret.
[L805] [24:52.52] And there was also, I mean, like Mesos
[L806] [24:54.04] at the time was
[L807] [24:55.96] you know, not the same, but similar and
[L808] [24:58.24] like you could just see that there was
[L809] [25:00.64] going to be an open and and so in some
[L810] [25:02.60] sense you part of the argument was like
[L811] [25:04.12] look there's going to be an open source
[L812] [25:05.56] solution. Do you want it to be one that
[L813] [25:07.48] we can influence or not? It's not like
[L814] [25:09.88] do you want there to not to be an open
[L815] [25:11.12] source one or not? It's there's going to
[L816] [25:13.00] be an open source one.
[L817] [25:15.16] Do you want it to be ours or do you want
[L818] [25:16.96] it to be someone else's?
[L819] [25:19.48] And it's just reframing the choice,
[L820] [25:20.84] right? And making it clear that people
[L821] [25:22.48] understand that that is the choice,
[L822] [25:23.76] right? That that you don't get to choose
[L823] [25:25.52] the proprietary option because it's just
[L824] [25:27.32] not viable.
[L825] [25:28.96] >> When you were building that that MVP for
[L826] [25:31.52] the orchestrator,
[L827] [25:33.36] well, how did you decide cuz there were
[L828] [25:35.04] no customers or anything like that? So
[L829] [25:36.64] how did you decide this is the minimum
[L830] [25:39.00] set of features that we need for this to
[L831] [25:41.44] before we launch it?
[L832] [25:42.68] >> Sure. Well, I mean I think absolutely,
[L833] [25:44.44] you know, we benefit from the fact that
[L834] [25:45.84] there were three of us working on it,
[L835] [25:47.16] right? So Craig was a a great product
[L836] [25:49.28] manager and Joe was a great engineer and
[L837] [25:52.36] and and fantastic at API design. Um and
[L838] [25:56.44] and I could write code fast basically I
[L839] [25:58.72] think is sort of the the the you know,
[L840] [26:00.20] like if I if I had to sort of stereotype
[L841] [26:02.60] all of us, you know, that's the like
[L842] [26:05.68] Craig was the product business guy and
[L843] [26:07.36] Joe is the like I know how to design
[L844] [26:09.92] really good at design kind of person and
[L845] [26:11.96] and I was basically like I can hack
[L846] [26:14.24] prototypes like there's no wasted like
[L847] [26:15.60] no tomorrow.
[L848] [26:17.32] Um and
[L849] [26:20.20] and and I think we reflected a lot about
[L850] [26:22.36] our own experiences.
[L851] [26:24.56] Um and also we had seen the pain of
[L852] [26:28.64] people deploying um into traditional EVM
[L853] [26:33.04] infrastructure and so we had that that
[L854] [26:34.52] kind of knowledge of the pain that
[L855] [26:35.76] people are going through. And then
[L856] [26:37.96] you know, at the time there were people
[L857] [26:40.52] like Netflix who were talking about
[L858] [26:42.12] immutable infrastructure and they were
[L859] [26:43.56] kind of advancing some of the similar
[L860] [26:45.16] some similar concepts.
[L861] [26:47.00] And so there was also kind of like a
[L862] [26:50.00] broader movement happening that we were
[L863] [26:52.68] taking part in. Um and so
[L864] [26:55.96] you know, obviously there were no there
[L865] [26:57.12] were literally no customers, but in some
[L866] [26:59.08] sense there there were customers. They
[L867] [27:00.64] just weren't customers yet.
[L868] [27:02.96] Um so it's not like creating something
[L869] [27:05.32] brand new, I guess is in some sense.
[L870] [27:07.76] Right? Like Like I feel I really don't
[L871] [27:10.08] feel like Kubernetes was something that
[L872] [27:11.80] was brand new.
[L873] [27:13.28] I feel like it was a coalescing of a lot
[L874] [27:15.40] of ideas that were kind of circulating
[L875] [27:17.00] in the in the industry at the time. And
[L876] [27:19.44] it just became an anchor point and a
[L877] [27:20.80] really good expression of those ideas.
[L878] [27:23.36] >> So when you talk about I guess you wrote
[L879] [27:26.04] a lot of code quickly,
[L880] [27:28.04] it did you write most of the code I
[L881] [27:30.72] guess for this initial initial MVP?
[L882] [27:34.64] >> Yeah, I I don't know what the number is,
[L883] [27:36.32] but high 80 high 80s percentage maybe
[L884] [27:39.40] more of of the original code. Um and I
[L885] [27:43.20] think I'm still number I mean I haven't
[L886] [27:44.44] contributed significantly to Kubernetes
[L887] [27:46.28] in a while and I'm still I think number
[L888] [27:47.76] five on the all over overall
[L889] [27:50.32] contributor, you know, overall
[L890] [27:51.32] contributor list on the GitHub commits.
[L891] [27:53.48] And I was never I was number one for a
[L892] [27:54.80] long time.
[L893] [27:55.96] >> I mean after writing that much code for
[L894] [27:58.04] Kubernetes, which part of this system
[L895] [28:01.32] was the hardest to build?
[L896] [28:03.44] >> I I think I'm going to say like cuz I
[L897] [28:04.72] don't think any of the specific code was
[L898] [28:07.80] that hard. Um
[L899] [28:11.20] I think that the
[L900] [28:13.84] core the hard part was the decision that
[L901] [28:15.72] we made early on that it was going to be
[L902] [28:17.28] a really loosely coupled system.
[L903] [28:20.00] And so it's very
[L904] [28:22.80] um
[L905] [28:23.44] which is great for resiliency. Like we
[L906] [28:25.20] made this decision around very loose
[L907] [28:27.24] coupling, a lot of independent actors
[L908] [28:29.88] taking actions. There's all these
[L909] [28:31.12] control loops running all over the
[L910] [28:32.44] place.
[L911] [28:33.76] Which is really good for resiliency.
[L912] [28:35.88] Um
[L913] [28:36.92] but when things go wrong, it's really
[L914] [28:39.48] hard to figure out
[L915] [28:41.28] why they went wrong. Because you've got,
[L916] [28:43.76] you know, 15 different processes that
[L917] [28:45.64] are all having to work together to
[L918] [28:47.12] achieve an outcome. And so you can see
[L919] [28:49.16] that the outcome wasn't achieved.
[L920] [28:51.36] Right? But then you're like, okay, but
[L921] [28:53.24] like what happened?
[L922] [28:54.92] And now I have to sift through a bunch
[L923] [28:56.84] of different logs and a bunch of
[L924] [28:58.20] different operations of executables and
[L925] [29:00.72] sort of reconstruct in time what
[L926] [29:02.96] happened and and especially early on we
[L927] [29:04.84] didn't have very good
[L928] [29:06.60] we didn't have very much consistency
[L929] [29:07.92] around logging, we didn't have very good
[L930] [29:10.00] consistency about event like events and
[L931] [29:12.32] things like that. Um
[L932] [29:14.84] And so I think the hardest part and I
[L933] [29:16.68] mean it's the hardest part of anything I
[L934] [29:17.84] guess, but like it's when something went
[L935] [29:19.32] wrong figuring out like why it went
[L936] [29:21.20] wrong.
[L937] [29:22.16] >> Because your logs are all distributed
[L938] [29:23.68] everywhere and
[L939] [29:25.00] >> Yeah, and everything's out of time sync
[L940] [29:26.48] and I mean and hopefully you logged the
[L941] [29:27.88] right things, but a lot of time early on
[L942] [29:30.00] like you didn't log it. Like you know,
[L943] [29:32.60] and and and and because it's a
[L944] [29:34.68] interaction effect
[L945] [29:36.44] it's hard to reproduce.
[L946] [29:38.60] Um often times it's hard often times
[L947] [29:40.32] it's hard to reproduce the problem. Like
[L948] [29:41.72] if it's a problem reproduces easily then
[L949] [29:43.52] it's pretty easy to fix even if you
[L950] [29:44.96] don't have the logs because you just go
[L951] [29:46.32] and add the logs and then you do it
[L952] [29:48.36] again and you see what happens. Um
[L953] [29:52.00] But for problems that are transient
[L954] [29:54.72] uh that because of it's just, you know,
[L955] [29:56.80] race condition between two or three
[L956] [29:58.32] different things happening, you can go
[L957] [30:00.28] in and add the extra logs, but then you
[L958] [30:01.84] have to figure out how to make it
[L959] [30:03.00] happen.
[L960] [30:04.36] Right? Um and that's that can be pretty
[L961] [30:07.92] tricky. Um and also I mean I'll say the
[L962] [30:10.48] other thing is like we were all learning
[L963] [30:11.60] Go.
[L964] [30:12.56] So maybe the other thing was like
[L965] [30:13.64] there's some gotchas in Go lang and we
[L966] [30:15.64] were all kind of like learning all the
[L967] [30:17.60] gotchas on the fly.
[L968] [30:19.84] >> I would have thought there's something
[L969] [30:21.24] that's controlling everything, right?
[L970] [30:22.48] Like there's some leader or maybe some
[L971] [30:25.40] nodes that are looking at one of them to
[L972] [30:28.56] kind of coordinate everything. Like
[L973] [30:30.56] leader election, if the leader goes
[L974] [30:32.60] down, I would have thought would be some
[L975] [30:35.20] really challenging problem.
[L976] [30:37.76] >> Yeah, I mean well, I think what what the
[L977] [30:39.72] reason it wasn't that big a deal was
[L978] [30:41.36] because
[L979] [30:42.56] um
[L980] [30:43.72] we relied pretty exclusively on etcd to
[L981] [30:48.16] to do that for us.
[L982] [30:50.52] >> Also, etcd is another
[L983] [30:53.20] framework or open source?
[L984] [30:54.68] >> Uh yeah, etcd is an open source I mean
[L985] [30:56.76] it's kind of really part of
[L986] [30:59.20] Kubernetes now, but at the time it was a
[L987] [31:01.68] um
[L988] [31:02.28] it's a a raft raft-based consensus uh
[L989] [31:06.76] system key value store.
[L990] [31:09.00] Um and so it was a pre-existing piece of
[L991] [31:11.76] software that that CoreOS had written um
[L992] [31:15.56] that implemented the raft protocol cuz
[L993] [31:17.68] at the time like cuz Paxos is was the
[L994] [31:20.00] original for this and Paxos is really
[L995] [31:21.48] hard to implement cuz the algorithm is
[L996] [31:22.96] really complicated
[L997] [31:24.56] uh and nobody understands it. Well,
[L998] [31:25.88] probably somebody understands it, but
[L999] [31:27.48] not a lot of people understand it. So
[L1000] [31:29.28] then
[L1001] [31:30.40] but it's provable, right? Um
[L1002] [31:33.88] and then right around that time frame
[L1003] [31:36.60] people had come up with raft, which is a
[L1004] [31:39.80] provably correct consensus algorithm,
[L1005] [31:43.24] but it's way easier to implement. etcd
[L1006] [31:46.20] implemented the raft protocol and then
[L1007] [31:48.24] gave you this consensus reliable um
[L1008] [31:51.96] store so that uh
[L1009] [31:54.60] you could do um
[L1010] [31:57.12] uh it had you had multiple replicas and
[L1011] [31:59.12] it would do it would do the consensus
[L1012] [32:00.48] there and it doesn't do leader election
[L1013] [32:02.00] exactly, but it allows but it gives you
[L1014] [32:04.36] enough primitives that doing leader
[L1015] [32:06.56] election is relatively
[L1016] [32:09.24] um straight forward. Um
[L1017] [32:12.32] and and I guess I would also say that I
[L1018] [32:14.48] mean two things about that. One is we
[L1019] [32:15.80] decided to force all of the access
[L1020] [32:19.28] through an API server.
[L1021] [32:21.36] So no nobody had and this was actually
[L1022] [32:23.48] something I pushed really hard initially
[L1023] [32:26.00] um but we I think we had general
[L1024] [32:27.36] agreement, but I definitely pushed for
[L1025] [32:28.80] it um was that nobody got to use store.
[L1026] [32:31.48] Everything had to be remote store.
[L1027] [32:34.04] Like nobody got to write stuff to disk
[L1028] [32:36.00] themselves.
[L1029] [32:37.32] Every every piece of the system had to
[L1030] [32:40.00] use the API server and had to use etcd
[L1031] [32:42.84] behind the API server as the way that it
[L1032] [32:45.00] did any sort of persistence.
[L1033] [32:48.20] >> What's the main benefit of that?
[L1034] [32:49.96] >> The main benefit of that is that
[L1035] [32:51.24] everybody gets to restart all the time
[L1036] [32:53.32] and they just come up and they work. So
[L1037] [32:55.20] you don't have to worry about
[L1038] [32:56.12] corruptions, you don't have to worry
[L1039] [32:57.36] about schema changes, you don't have to
[L1040] [32:59.32] worry about any of the like everybody
[L1041] [33:01.20] was effectively stateless
[L1042] [33:03.12] except for the database. Like there was
[L1043] [33:05.16] there's the etcd consensus algorithm
[L1044] [33:07.28] database
[L1045] [33:08.40] and that's the only place where there
[L1046] [33:09.76] was state.
[L1047] [33:11.36] And and so as a result
[L1048] [33:13.64] um
[L1049] [33:14.64] the the whole system was just a lot
[L1050] [33:17.20] easier to um
[L1051] [33:19.16] to to make stable. Um
[L1052] [33:21.48] the the downside of it is it it leads to
[L1053] [33:23.44] this like loosely couple like loose
[L1054] [33:25.12] coupling, right? Where it's a bunch of
[L1055] [33:26.72] independent loops mediating everything
[L1056] [33:29.08] through this storage layer.
[L1057] [33:31.36] Um
[L1058] [33:32.64] and and which made the debugging part
[L1059] [33:34.28] harder.
[L1060] [33:34.88] >> Right. So like the those are the sort of
[L1061] [33:36.52] the trade-offs is like if you have a
[L1062] [33:37.88] complete log of like I'm in
[L1063] [33:40.08] you know, if you think of it as a state
[L1064] [33:41.28] machine, like it's much easier to
[L1065] [33:42.88] understand where you are
[L1066] [33:44.84] and where you got to
[L1067] [33:46.60] if you're in a state machine.
[L1068] [33:49.04] Um
[L1069] [33:49.96] but state machines are a nightmare to
[L1070] [33:51.44] make reliable.
[L1071] [33:54.16] And so like they're easy to they're easy
[L1072] [33:55.76] to debug, but they're hard to make
[L1073] [33:57.40] stable. Whereas the system we built was
[L1074] [33:59.44] like designed to be stable
[L1075] [34:01.52] but hard to debug.
[L1076] [34:03.24] The trouble with the state machine is a
[L1077] [34:04.52] state machine says the world looks like
[L1078] [34:06.96] this.
[L1079] [34:08.52] And unless you get it exactly right
[L1080] [34:11.20] sometimes the world looks like something
[L1081] [34:12.64] you didn't imagine.
[L1082] [34:14.48] And at that point you're kind of screwed
[L1083] [34:16.68] because like your state machine doesn't
[L1084] [34:18.24] know what to do.
[L1085] [34:19.68] Right? Whereas because we have these
[L1086] [34:22.36] control loops that were based on a
[L1087] [34:24.40] desired state and a current state and
[L1088] [34:26.44] trying to drive the current state to the
[L1089] [34:28.12] desired state
[L1090] [34:30.16] like no matter where you woke up and
[L1091] [34:31.72] found yourself,
[L1092] [34:33.28] you kind of knew where you were supposed
[L1093] [34:34.80] to drive to. And that And that And
[L1094] [34:36.64] that's the stable part. That's the
[L1095] [34:37.88] stable part of it is that like it didn't
[L1096] [34:40.40] really matter what what where the system
[L1097] [34:42.68] got itself.
[L1098] [34:44.68] It was always trying to drive towards uh
[L1099] [34:47.08] the the desired state. You know,
[L1100] [34:49.28] inspired honestly a lot by like control
[L1101] [34:51.00] theory from robotics, actually. Like
[L1102] [34:53.44] >> Oh, like uh PID.
[L1103] [34:54.80] >> Yeah, the same same idea, right? Like,
[L1104] [34:57.48] you know, you could imagine if you tried
[L1105] [34:58.76] to write a PID controller to balance a
[L1106] [35:00.40] beam with a bunch of if else loops, it
[L1107] [35:03.16] like it just doesn't work very well.
[L1108] [35:04.84] >> And that this kind of reminds me cuz I
[L1109] [35:06.52] was reading like in some of the design
[L1110] [35:08.48] uh like a large I guess it's a feature
[L1111] [35:10.48] of Kubernetes is that it's declarative
[L1112] [35:13.56] rather than imperative. So, you kind of
[L1113] [35:15.12] just say, "I want this to be true. I
[L1114] [35:17.40] don't care how you get there." instead
[L1115] [35:18.92] of saying, "Just do X, Y, and Z." Um I'm
[L1116] [35:22.24] curious like the pros and cons of that
[L1117] [35:25.00] that design decision.
[L1118] [35:26.64] >> Um well, yeah. I mean, and that was
[L1119] [35:28.24] something that was happening broadly in
[L1120] [35:29.56] the industry. Like, that's a part of the
[L1121] [35:31.44] whole like infrastructure as code
[L1122] [35:33.12] movement that was happening at the time.
[L1123] [35:35.36] Um so, we're not the only ones who said
[L1124] [35:37.16] that, but we definitely embraced it. Um
