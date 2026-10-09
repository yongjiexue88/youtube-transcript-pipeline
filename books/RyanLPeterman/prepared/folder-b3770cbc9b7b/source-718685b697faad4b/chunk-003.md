Chunk 3; segments 771–1161. Start may repeat the previous chunk for context.

# Turing Award Winner: Disagreeing with Google, Postgres, Future Problems | Mike Stonebraker

Source ID: source-718685b697faad4b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Disagreeing_with_Google,_Postgres,_Future_Problems_Mike_Stonebraker_en.txt
Video: https://www.youtube.com/watch?v=YPObBOwIrHk

[L780] [36:59.44] earlier is very much get and get leaf
[L781] [37:04.16] level programmers
[L782] [37:06.32] interested.
[L783] [37:07.92] So it's been very much uh you know tell
[L784] [37:11.84] us leaf level programmer tell us what
[L785] [37:14.56] you need that we don't have get it
[L786] [37:17.44] quickly
[L787] [37:19.28] and convince people to try it and
[L788] [37:24.72] we've been very very successful with
[L789] [37:26.72] other with other startups who want to
[L790] [37:29.44] choose the best thing and we're starting
[L791] [37:32.40] to be to be successful with the the big
[L792] [37:35.20] boys. So it's it's an interesting
[L793] [37:39.36] interesting market and I think the key
[L794] [37:42.16] thing so far it's
[L795] [37:46.88] probably twothirds of the customers are
[L796] [37:50.16] doing agentic AI which means that they
[L797] [37:54.16] have a large language model surrounded
[L798] [37:56.56] by a bunch of stuff that that adds more
[L799] [38:00.88] signal
[L800] [38:02.48] and so far
[L801] [38:05.76] Most of Agentic AI is read only,
[L802] [38:10.00] meaning uh you want to produce a
[L803] [38:12.96] prediction
[L804] [38:14.56] for whether Ryan is is going to be a
[L805] [38:17.20] good customer or not. And so that just
[L806] [38:20.64] runs some stuff and then produces a new
[L807] [38:23.52] thing that's given to somebody. So
[L808] [38:27.92] basically read only which means that uh
[L809] [38:33.28] you're not you're not actually updating
[L810] [38:37.28] Ryan's credit rating or and so I think
[L811] [38:42.24] fairly quickly this the whole world is
[L812] [38:45.60] going to move to using
[L813] [38:48.00] you know agents to do read write
[L814] [38:50.64] applications
[L815] [38:52.24] and that's going to make that's going to
[L816] [38:54.48] make them very very databasey
[L817] [38:58.48] and DeBoss does that stuff really really
[L818] [39:01.92] well. And so, you know, for instance, if
[L819] [39:06.16] you want to write an agent or two agents
[L820] [39:10.24] that move a $100 from my account to your
[L821] [39:14.08] account.
[L822] [39:15.60] And so you debit my account, you
[L823] [39:17.92] increment your account
[L824] [39:20.24] and these two agents have to agree to
[L825] [39:23.76] commit
[L826] [39:25.60] or you have to back everything out,
[L827] [39:29.12] which is to say the workflow [snorts]
[L828] [39:31.92] needs to be what I called atomic, which
[L829] [39:34.48] is it all happens or it looks like it
[L830] [39:37.20] never happened. And so I think the the
[L831] [39:40.32] demands on in this market will escalate
[L832] [39:45.28] with with things with people wanting
[L833] [39:47.84] stuff to be read, right? And so I think
[L834] [39:50.72] that that will bode well for the market
[L835] [39:54.16] and bode well for deboss.
[L836] [39:57.20] And this this what's being offered in
[L837] [39:59.36] the market today to application
[L838] [40:01.52] developers differs from the original
[L839] [40:04.00] research project where that was actually
[L840] [40:06.16] swapping out the guts of an operating
[L841] [40:08.24] system with a database. I see that's I
[L842] [40:11.68] mean that's really cool. I never
[L843] [40:12.96] imagined replacing all the state of a of
[L844] [40:16.16] an operating system with a database.
[L845] [40:18.32] What's the there there's got to be some
[L846] [40:20.80] trade-off there.
[L847] [40:22.88] Well, a file system written on top of a
[L848] [40:25.68] DBMS is faster than than the Linux file
[L849] [40:30.16] system. The scheduling engine is
[L850] [40:33.36] competitive with other scheduling
[L851] [40:35.20] engines. You can make everything fail
[L852] [40:38.16] over. So, you get high availability
[L853] [40:41.12] without having to do anything else. The
[L854] [40:44.48] answer is there there's really no
[L855] [40:47.28] downside.
[L856] [40:49.84] Then why wouldn't Linux
[L857] [40:52.08] incorporate that and upgrade itself with
[L858] [40:55.12] this? You hope they would. In other
[L859] [40:58.24] words, you should you should keep all
[L860] [41:00.56] the device driver junk down at the
[L861] [41:02.56] bottom because that's there's a lot of
[L862] [41:04.96] it and no one wants to do that and
[L863] [41:08.48] replace everything else with the
[L864] [41:10.00] database implementation.
[L865] [41:12.40] Is that something that you've mentioned
[L866] [41:14.08] to Linux people and what's their typical
[L867] [41:16.64] reaction
[L868] [41:17.84] >> back in the academic project when I'd
[L869] [41:20.32] mentioned that to operating system folks
[L870] [41:23.76] they would get very very threatened
[L871] [41:26.48] which is this is the database guys
[L872] [41:28.96] trying to take over their turf
[L873] [41:32.32] and I think the programming language
[L874] [41:34.40] guys ditto you know which is you know
[L875] [41:37.52] the the the
[L876] [41:40.32] way to implement the runtime for a
[L877] [41:42.72] programming environment is with a
[L878] [41:44.72] database.
[L879] [41:46.48] >> That's uh that's interesting. I mean, if
[L880] [41:48.96] it's objectively true, then maybe it
[L881] [41:50.80] will take over.
[L882] [41:53.04] >> Well, I mean, it took Java 10 years to
[L883] [41:56.08] become widely accepted. I just think the
[L884] [41:59.12] time constant is substantial. I think we
[L885] [42:02.80] talked a lot about the past of databases
[L886] [42:05.20] and I'm curious your thoughts on
[L887] [42:07.76] unsolved problems in databases and what
[L888] [42:10.80] you think the future might look like.
[L889] [42:13.12] >> Okay. So I think two different things
[L890] [42:15.60] that I'd like to talk about. The first
[L891] [42:18.48] one is
[L892] [42:20.40] like everyone else
[L893] [42:23.44] three years ago we started to look at
[L894] [42:26.56] what were large language models good
[L895] [42:28.64] for. So, we've been trying to get what's
[L896] [42:33.60] now called text to SQL
[L897] [42:36.64] uh to we've been we've been trying to
[L898] [42:39.92] make it work
[L899] [42:42.72] on real world databases,
[L900] [42:46.88] especially real world data warehouses.
[L901] [42:50.48] So we've been trying the technology
[L902] [42:54.08] on four different production databases
[L903] [42:57.28] warehouses
[L904] [42:59.04] where we've gotten the workload the
[L905] [43:02.00] actual workload that's run
[L906] [43:05.20] and
[L907] [43:06.96] you know from the actual users using the
[L908] [43:10.08] system
[L909] [43:11.86] [clears throat] and we've gotten them to
[L910] [43:14.48] reverse engineer the text that
[L911] [43:17.20] corresponds to that sequence. So we have
[L912] [43:20.64] text and SQL for we have four
[L913] [43:25.04] benchmarks.
[L914] [43:26.40] >> When you say text to SQL, you mean uh
[L915] [43:28.64] like a human prompting model or
[L916] [43:31.12] something like I would just in English
[L917] [43:33.68] that text would be you know everyone
[L918] [43:36.32] over four years old. Tell me all the
[L919] [43:38.96] professors at MIT who won the touring
[L920] [43:41.76] award. And so an LLM is supposedly good
[L921] [43:45.44] at that.
[L922] [43:48.48] And so uh the text to SQL benchmarks
[L923] [43:52.72] there's a one called spider another one
[L924] [43:54.72] called bird
[L925] [43:56.80] and the best LLM systems are pretty good
[L926] [43:59.60] at those benchmarks you know like 80%
[L927] [44:02.64] accuracy or better
[L928] [44:04.40] >> so not superhuman
[L929] [44:06.80] >> not superhuman but they're pretty good
[L930] [44:09.04] like you would consider using them a and
[L931] [44:12.64] you know like current current
[L932] [44:14.40] leaderboard is something like 85% %
[L933] [44:16.96] accuracy, which I mean it's getting
[L934] [44:19.36] there. You say maybe it's not quite
[L935] [44:21.52] ready for prime time, but it's simply it
[L936] [44:23.76] certainly
[L937] [44:25.28] looks looks pretty good.
[L938] [44:28.24] Well, on our benchmarks,
[L939] [44:30.80] uh, large language models get 0%. And if
[L940] [44:35.60] you enhance them with rag and and all
[L941] [44:38.72] the tricks goes to 10%. And if you give
[L942] [44:42.72] as a prompt the from clause, in other
[L943] [44:46.08] words, all the actual tables that need
[L944] [44:48.24] to be accessed [snorts] and all the
[L945] [44:51.28] actual join clauses that need to be
[L946] [44:53.60] joined, then accuracy goes to about 35%.
[L947] [45:00.16] So the definition of this stuff doesn't
[L948] [45:04.08] is not ready for prime time and not
[L949] [45:07.52] going to be for a while, if ever.
[L950] [45:10.48] So what what's the difference? Uh number
[L951] [45:13.52] one, data wareh you know LL LLMs are
[L952] [45:17.36] trained on the pile.
[L953] [45:20.00] Data warehouse data is not in the pile.
[L954] [45:23.20] And there's an adage that if you haven't
[L955] [45:25.44] seen the data a couple times before, you
[L956] [45:29.12] have no chance of regurgitating it.
[L957] [45:32.88] That's number one. Uh number two uh
[L958] [45:37.76] query complexity on spider and bird is
[L959] [45:40.80] maybe 10 to 20 lines of SQL. Real world
[L960] [45:45.44] data warehouses it's 100 lines of SQL.
[L961] [45:49.36] Complexity is bigger.
[L962] [45:51.76] Number three the schema in spider and
[L963] [45:55.84] bird is clean.
[L964] [45:58.24] You know the table names are are mmonic.
[L965] [46:02.08] The column names are pneummonic and
[L966] [46:04.24] there's no duplication.
[L967] [46:06.80] In data warehouses, people have
[L968] [46:08.96] materialized views all the time. It
[L969] [46:11.68] means there's redundancy
[L970] [46:14.16] and and column names are often
[L971] [46:18.16] underscore
[L972] [46:19.68] Zuppers blah. And so they're not mmonic.
[L973] [46:24.80] So that makes it a lot harder. uh and
[L974] [46:28.08] then they also have idiosyncratic data.
[L975] [46:31.76] So J term is popular thing at MIT. It's
[L976] [46:35.84] a one-month term in January.
[L977] [46:39.44] Not unique to to MIT but not very
[L978] [46:43.12] popular.
[L979] [46:44.88] So not in the pile
[L980] [46:47.52] idiosyncratic data simple queries schema
[L981] [46:53.44] schema is a mess.
[L982] [46:56.64] make make it not work. And those are
[L983] [46:59.44] true of every data warehouse I know of.
[L984] [47:03.20] And so I think the the technology simply
[L985] [47:08.08] doesn't work and isn't going to work
[L986] [47:09.84] anytime soon.
[L987] [47:12.56] So we've been So what do you do? So well
[L988] [47:16.64] first of all we published our benchmark.
[L989] [47:19.12] It's a thing called Beaver, which is an
[L990] [47:21.92] anonymized
[L991] [47:23.60] and abstracted version of these four
[L992] [47:25.84] data warehouses.
[L993] [47:27.92] And so if you think you're really good
[L994] [47:30.16] at doing text to SQL, try a real
[L995] [47:33.20] benchmark, not a fake one.
[L996] [47:36.32] So number two, uh,
[L997] [47:40.40] borrowing from what I just said, if you
[L998] [47:43.28] don't have all the join terms and you
[L999] [47:45.12] don't have the from clause, you're
[L1000] [47:48.16] toast.
[L1001] [47:50.64] What's more, if you don't break down the
[L1002] [47:52.48] query into simpler pieces, you're toast.
[L1003] [47:57.20] So that says to me that uh you want to
[L1004] [48:04.72] give
[L1005] [48:06.80] your retrieval system simpler pieces
[L1006] [48:10.56] which include the from clause and
[L1007] [48:12.32] include join terms. That's number one.
[L1008] [48:15.76] Uh number two, the minute you want to
[L1009] [48:19.52] talk to two different structured
[L1010] [48:22.16] databases, you know, like your data
[L1011] [48:24.64] warehouse and your CRM system,
[L1012] [48:28.56] then it's pretty clear to me that doing
[L1013] [48:31.44] a structured data join using an LLM is a
[L1014] [48:35.92] bad idea. It's just you're much better
[L1015] [48:38.96] off
[L1016] [48:40.80] you leaving them as tables and doing a
[L1017] [48:43.20] join in SQL.
[L1018] [48:45.52] So our point of view is we are trying
[L1019] [48:47.76] out
[L1020] [48:49.28] turning everything into tables. You
[L1021] [48:51.60] know, we're we're working with the
[L1022] [48:54.16] Department of Transportation in the city
[L1023] [48:56.72] of Munich, Germany,
[L1024] [48:58.96] and they have six people full-time who
[L1025] [49:02.40] are answering citizens
[L1026] [49:05.12] complaints,
[L1027] [49:06.72] queries,
[L1028] [49:08.56] which are of the form, how come I don't
[L1029] [49:11.84] have enough time to cross this
[L1030] [49:14.80] intersection next to my house before the
[L1031] [49:17.68] light turns? All kinds of stuff. How
[L1032] [49:20.96] come the trolley doesn't stop for enough
[L1033] [49:23.68] time for me to get on the trolley? You
[L1034] [49:25.92] know, it's How come the trolley doesn't
[L1035] [49:28.32] come uh more than once an hour? I mean,
[L1036] [49:33.28] it's all this stuff. Their database is
[L1037] [49:36.80] the trolley schedule, that's SQL. The
[L1038] [49:39.44] light sequencing, that's SQL.
[L1039] [49:42.88] The intersections, that's CAD.
[L1040] [49:46.80] the federal
[L1041] [49:50.08] you know country of Germany regulations
[L1042] [49:52.96] of this stuff that's text city of Munich
[L1043] [49:57.68] regulations for this stuff which is text
[L1044] [50:01.20] so you got to join SQL SQL CAD text and
[L1045] [50:05.52] text so our point of view is turn it all
[L1046] [50:08.64] into SQL all into tables and do a join
[L1047] [50:12.56] with what amounts to a query optimizer
[L1048] [50:16.40] So that's what we're working on. I think
[L1049] [50:18.96] other people will have other ideas but I
[L1050] [50:21.68] think it's extremely fertile area
[L1051] [50:24.24] because people really want to do it.
[L1052] [50:27.76] So that's number one. Uh number two we
[L1053] [50:30.56] talked earlier about agentic AI. The
[L1054] [50:33.84] minute this becomes read write it's a
[L1055] [50:35.76] distributed database problem and you
[L1056] [50:38.56] want atomicity
[L1057] [50:40.96] consistency all that stuff. I think a
[L1058] [50:43.68] very interesting area. So that's pretty
[L1059] [50:47.84] much what I what I am what I'm working
[L1060] [50:50.40] on now
[L1061] [50:52.24] >> on that benchmark where it's 0% right
[L1062] [50:54.56] now. What percent is human? Like if you
[L1063] [50:58.48] took someone who really knows SQL, what
[L1064] [51:00.80] would they score like the average human?
[L1065] [51:03.04] So once you disambiguate the the text,
[L1066] [51:07.12] a a knowledgeable SQL user programmer
[L1067] [51:11.28] with the schema will do will will get
[L1068] [51:13.76] very high accuracy.
[L1069] [51:15.68] >> Okay. Like 90% or something at least.
[L1070] [51:18.72] >> Okay. Okay. Wow. It's I'm surprised that
[L1071] [51:22.16] the LM so score so lowly on on this kind
[L1072] [51:25.36] of benchmark. Maybe when this goes out,
[L1073] [51:27.76] someone who works at Anthropic will
[L1074] [51:29.60] reach out to you or something and say,
[L1075] [51:31.28] "Let's
[L1076] [51:31.92] >> I'd love to I'd love to find out because
[L1077] [51:35.04] I mean it's a terrific success story
[L1078] [51:38.32] >> for people who want to deeply understand
[L1079] [51:40.64] databases and they're looking for some
[L1080] [51:43.92] material to study. Is there a book that
[L1081] [51:46.72] you recommend that's a top technical
[L1082] [51:48.72] book to learn databases
[L1083] [51:50.88] >> papers in the literature?"
[L1084] [51:53.84] I think uh Joey Helerstein and I
[L1085] [51:56.56] published a red book what's called the
[L1086] [51:58.88] red book which is called readings and
[L1087] [52:01.28] database systems. It's now
[L1088] [52:05.92] eight years old. I mean I think that
[L1089] [52:08.80] that would be a great set of readings
[L1090] [52:10.88] for eight years ago
[L1091] [52:13.20] and beyond that uh papers
[L1092] [52:17.20] popular papers from the literature. If
[L1093] [52:20.24] you could go back to yourself when you
[L1094] [52:22.16] just graduated, give yourself some
[L1095] [52:24.56] advice knowing what you know today, what
[L1096] [52:26.40] would you say?
[L1097] [52:28.08] >> Back at when I first took the job at
[L1098] [52:30.56] Berkeley and without thinking about it
[L1099] [52:33.04] much, we said, "Let's write a database
[L1100] [52:34.80] system." And we we knew nothing about
[L1101] [52:37.20] databases,
[L1102] [52:39.20] nothing about implementations. We were
[L1103] [52:41.52] not skilled programmers
[L1104] [52:44.00] like Bill Joy. So starting off doing
[L1105] [52:47.84] something that was that crazy
[L1106] [52:50.64] was really pretty crazy.
[L1107] [52:53.28] And and you know you you effort and you
[L1108] [52:57.20] make stuff work and you learn along the
[L1109] [52:59.76] way. And so I think the answer is
[L1110] [53:03.84] think outside the box.
[L1111] [53:06.40] Think crazy thoughts
[L1112] [53:08.64] and try and do them.
[L1113] [53:11.12] And I think
[L1114] [53:13.60] to me it's not at all obvious. The the
[L1115] [53:17.36] better question is if you were starting
[L1116] [53:20.00] out today, what would you major in? Uh
[L1117] [53:23.28] because I think, you know, computer
[L1118] [53:26.00] science may well not be a growth
[L1119] [53:27.92] industry going forward. And I'm not sure
[L1120] [53:31.12] I would recommend 18 year olds to major
[L1121] [53:34.40] in computer science.
[L1122] [53:36.64] I mean, I think health health care and
[L1123] [53:38.80] and the building trades are are are safe
[L1124] [53:42.32] bets and everything else looks much
[L1125] [53:45.28] riskier. Uh, if if you're about to get
[L1126] [53:48.96] your PhD and are trying to decide what
[L1127] [53:51.28] to do,
[L1128] [53:53.04] then I think life is pretty easy. you
[L1129] [53:55.52] know, take take the most prestigious job
[L1130] [53:58.08] you can get
[L1131] [54:00.24] and find a mentor who's willing to help
[L1132] [54:03.60] you
[L1133] [54:05.28] and then pick some area that isn't, you
[L1134] [54:10.08] know, like our our stuff, you know,
[L1135] [54:12.56] which is called Rubicon, is definitely
[L1136] [54:14.88] not going with the flow. So, choose
[L1137] [54:18.40] something that's not that isn't going
[L1138] [54:20.96] with the flow
[L1139] [54:22.88] and try and make it work. Both my wife
[L1140] [54:25.20] and I said, "F follow your passion.
[L1141] [54:28.56] Somehow the money will work out." And I
[L1142] [54:31.68] don't believe that for a minute, but I
[L1143] [54:33.76] think that's what you have to tell your
[L1144] [54:35.20] kids. [laughter]
[L1145] [54:36.96] >> And your grandkids.
[L1146] [54:38.56] >> If you don't believe that, then uh why
[L1147] [54:41.04] do you have to tell them that?
[L1148] [54:42.90] [clears throat]
[L1149] [54:43.04] >> My wife is is a good example. So she has
[L1150] [54:46.16] an she has a master's degree in computer
[L1151] [54:49.04] science, undergraduate degree in
[L1152] [54:50.80] computer science, and she wanted to be a
[L1153] [54:54.16] teacher, you know, you know, K K12
[L1154] [54:57.84] teacher. And her parents said, "You
[L1155] [55:00.00] can't do that. It doesn't pay enough
[L1156] [55:01.60] money."
[L1157] [55:03.60] And so I think and I think she ever
[L1158] [55:06.48] since that time has regretted
[L1159] [55:09.52] that decision. She wasn't passionate
[L1160] [55:12.48] about doing computer science. it was
[L1161] [55:14.40] simply a trade.
[L1162] [55:17.20] And so I think find something you're
[L1163] [55:19.60] passionate about and and you will, you
[L1164] [55:23.04] know, either
[L1165] [55:25.20] you won't starve. You may not make a lot
[L1166] [55:27.76] of money, but I think chances are you'll
[L1167] [55:30.96] be happier than if you do something
[L1168] [55:33.28] you're not passionate about. Because I
[L1169] [55:35.60] think a lot of people I know view their
[L1170] [55:38.80] job as simply a job and life is what
