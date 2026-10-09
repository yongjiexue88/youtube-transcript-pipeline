Chunk 4; segments 983–1319. Start may repeat the previous chunk for context.

# Creator of Scala: Comparing Languages And How AI Will Impact Them | Martin Odersky

Source ID: source-5f7cf6e81e665bd5
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Scala_Comparing_Languages_And_How_AI_Will_Impact_Them_Martin_Odersky_en.txt
Video: https://www.youtube.com/watch?v=LdN4sPWM-WY

[L992] [40:10.96] can fake everything.
[L993] [40:12.32] >> A lot of programming language design and
[L994] [40:15.12] how we write code in the past is writing
[L995] [40:18.08] the source code so that it's um it's
[L996] [40:21.52] it's nice for humans to read. But if
[L997] [40:24.48] humans are no longer interacting with
[L998] [40:26.16] the code, what kind of things come to
[L999] [40:28.72] mind that we might not care as much
[L1000] [40:31.68] about but are good for machines to read.
[L1001] [40:34.72] For instance,
[L1002] [40:35.76] >> the first thing is uh maybe sometimes
[L1003] [40:38.32] you want to read it uh but you probably
[L1004] [40:40.80] wouldn't have written it. So easy to
[L1005] [40:43.28] write is definitely not not a big
[L1006] [40:45.52] criterion anymore. Easy to read to some
[L1007] [40:48.08] degree. Yes. But that means you don't
[L1008] [40:50.32] need any these these sort of syntactic
[L1009] [40:52.40] hacks like to write plus+ in C or things
[L1010] [40:55.04] like that that's easy to write right. So
[L1011] [40:57.76] but I I don't I mean I'm sure we will
[L1012] [41:00.56] still have that but it doesn't really
[L1013] [41:02.40] matter anymore. I mean whether [snorts]
[L1014] [41:04.32] I write an assignment in in long form or
[L1015] [41:06.80] with X++ whatever. So I think these
[L1016] [41:09.60] things won't won't matter much less. the
[L1017] [41:11.76] things that matter much more are or that
[L1018] [41:14.40] continue to matter and uh are
[L1019] [41:18.00] essentially high level ways to constrain
[L1020] [41:21.68] and specify what my program should do.
[L1021] [41:24.88] So uh constrain what it should not do.
[L1022] [41:27.28] Uh that's that's one of the things and
[L1023] [41:29.44] also specify what it should do. uh and I
[L1024] [41:32.96] mean some people say it's a golden age
[L1025] [41:35.60] for formal verification because we can
[L1026] [41:37.76] be very precise in our specifications
[L1027] [41:40.00] and our AI can actually not just finish
[L1028] [41:43.36] the program but also the proof that the
[L1029] [41:45.76] that the program actually meets the
[L1030] [41:47.52] specification and I think that's true
[L1031] [41:49.68] that's really very exciting in in in a
[L1032] [41:51.68] lot of areas but in the large uh the
[L1033] [41:55.36] problem is you often don't really have
[L1034] [41:57.04] the formal specification or it's just as
[L1035] [42:00.16] hard to write a formal specific
[L1036] [42:01.44] ification than to write a program or
[L1037] [42:03.12] sometimes even harder. So that means
[L1038] [42:05.52] that we will still have live in a world
[L1039] [42:08.40] where we specify things by natural
[L1040] [42:11.52] languages by prompt to the agent and and
[L1041] [42:14.96] the agent then will will do the code.
[L1042] [42:16.88] But I imagine that also the that will be
[L1043] [42:19.76] a lot more
[L1044] [42:21.76] um formal in a way. So, so in a sense
[L1045] [42:25.28] right now the prompts I mean it's
[L1046] [42:27.12] fantastic what they can do with the
[L1047] [42:28.48] prompts but then we throw away the
[L1048] [42:29.84] prompt or the it's hidden in in the chat
[L1049] [42:32.64] history with the agent. So that's really
[L1050] [42:34.40] a shame. So I really should should have
[L1051] [42:36.64] the prompts as first class values in my
[L1052] [42:39.12] program that I can say well essentially
[L1053] [42:41.36] that's what the program is about and if
[L1054] [42:43.12] I change the prompt then the AI will
[L1055] [42:46.08] know essentially what the incremental
[L1056] [42:47.92] change was and change the program
[L1057] [42:49.36] incrementally. these sort of things.
[L1058] [42:51.68] That's another thing that I think we'll
[L1059] [42:53.28] see in future programming languages for
[L1060] [42:55.44] a agentic programming.
[L1061] [42:57.52] >> Maybe like some kind of meta meta
[L1062] [43:00.40] information about the program almost
[L1063] [43:02.08] like a git blame but like a you know
[L1064] [43:05.44] prompt I guess blame of what generated
[L1065] [43:08.24] that that part of the code.
[L1066] [43:11.36] >> You should be able to to to keep that
[L1067] [43:14.08] around and and come back to it. Yeah.
[L1068] [43:16.00] Also because you want you might want to
[L1069] [43:17.60] change, right? You might want to say
[L1070] [43:19.20] well now it's exactly the same but I
[L1071] [43:21.60] want to change this little detail but I
[L1072] [43:24.08] don't want the LLM nondeterministically
[L1073] [43:26.40] to generate a new program because that
[L1074] [43:28.40] way well it might get a lot of other
[L1075] [43:30.32] things wrong that I reviewed already. So
[L1076] [43:32.64] there really should then be an
[L1077] [43:34.00] incremental small change to the code and
[L1078] [43:36.64] that means I keep I need to keep the
[L1079] [43:38.24] prompt as a part of my program.
[L1080] [43:40.80] >> 10 years from now do you think there
[L1081] [43:42.16] will be more software engineers than
[L1082] [43:44.08] today or less?
[L1083] [43:46.96] I think there will be less uh the
[L1084] [43:50.88] uh and it will be a higher um
[L1085] [43:55.52] profession that is essentially has
[L1086] [43:58.24] higher standards. Uh so it will be
[L1087] [44:00.32] harder to become one. You will know be
[L1088] [44:02.80] able to know quite a lot of logics and
[L1089] [44:04.80] maths to be competent at essentially
[L1090] [44:08.00] keeping AI on the good track and things
[L1091] [44:10.16] like that. It's sort of can say it's
[L1092] [44:12.16] sort of like a like a control engineer
[L1093] [44:14.24] for a factory where you don't understand
[L1094] [44:16.72] many things in initially. It means that
[L1095] [44:19.76] there must be more you must be higher
[L1096] [44:22.40] skilled than a a factory worker of uh 50
[L1097] [44:26.00] years ago or something like that and I
[L1098] [44:28.16] think the same will will happen for
[L1099] [44:29.60] software where you will need fewer but
[L1100] [44:32.96] more qualified people. One thing that a
[L1101] [44:35.60] lot of people recommend is to become
[L1102] [44:37.44] better at programming you should learn
[L1103] [44:39.04] multiple languages and I wanted to know
[L1104] [44:42.48] aside from Scola what are the top
[L1105] [44:45.20] programming languages you would
[L1106] [44:46.64] recommend people learn to expand their
[L1107] [44:48.88] mind. So definitely a systems language
[L1108] [44:51.76] uh I think to to know how how how
[L1109] [44:54.80] hardware works and how software links
[L1110] [44:56.80] with hardware I would learn a systems
[L1111] [44:58.40] language and um
[L1112] [45:01.76] I'm sort of torn between C and Rust
[L1113] [45:04.00] there because C has going for it that
[L1114] [45:06.40] it's very simple and very close to a
[L1115] [45:08.72] thing in Rust you have to learn a lot of
[L1116] [45:10.64] abstractions but on the other hand it is
[L1117] [45:12.64] memory safe so I would say probably
[L1118] [45:14.80] initially see to figure out what these
[L1119] [45:17.20] things are and then if If you decide to
[L1120] [45:19.60] become a systems programmer as a career
[L1121] [45:21.68] then you should switch to rest I guess.
[L1122] [45:23.92] So that would be one thing. Uh the other
[L1123] [45:26.56] thing would be something more
[L1124] [45:29.60] uh with a verification improving
[L1125] [45:32.00] background because that will be a lot
[L1126] [45:33.68] more will become a lot more important.
[L1127] [45:37.04] So I would actually do a course in in
[L1128] [45:39.76] lean or or rock or one of these
[L1129] [45:42.08] languages uh to say where we we should
[L1130] [45:45.28] be able to use AI or to to to have to
[L1131] [45:50.56] develop first an intuition what it means
[L1132] [45:52.48] for a program to be correct because I
[L1133] [45:54.48] guess for most people have only a very
[L1134] [45:56.32] very uh fuzzy fuzzy intuition for these
[L1135] [46:00.00] things and and learning one of these
[L1136] [46:02.16] languages would sharpen the mind.
[L1137] [46:05.28] Um yeah, so I think those and then of
[L1138] [46:07.84] course Scala too as a language that
[L1139] [46:10.32] essentially sits right in the middle
[L1140] [46:11.92] where fairly fairly provable strong
[L1141] [46:14.96] types uh high expressivity these sort of
[L1142] [46:17.92] things.
[L1143] [46:18.32] >> Yeah. When you think of a top technical
[L1144] [46:20.16] book that you might recommend people
[L1145] [46:22.16] does anything come to mind?
[L1146] [46:23.84] >> I got a lot out of uh structure and
[L1147] [46:26.08] interpretation of computer programs that
[L1148] [46:28.08] was a book from the '9s. It was the
[L1149] [46:30.80] intro text at MIT at the time uh or 80s
[L1150] [46:34.72] even I think um and in fact this the
[L1151] [46:38.16] courses I taught on Corera and and uh at
[L1152] [46:41.36] DPFL are based quite a lot well to some
[L1153] [46:44.48] degree they're based based on that
[L1154] [46:46.16] material. So of course not the same
[L1155] [46:47.84] language and strong types instead of
[L1156] [46:50.16] dynamically type but still
[L1157] [46:52.16] >> when you look back on your career why
[L1158] [46:54.08] did you choose to work in academia
[L1159] [46:55.84] instead of industry? When I came to the
[L1160] [46:58.24] end of my studies, I uh was asked to do
[L1161] [47:00.80] a research project and the project I
[L1162] [47:04.00] picked or the prof then asked from me to
[L1163] [47:07.20] modulate that a little bit. In the end,
[L1164] [47:09.20] I found it super interesting to say I I
[L1165] [47:11.60] work on something that I don't know
[L1166] [47:12.96] whether it has a solution or not. Uh so
[L1167] [47:16.40] uh it it might be that uh the question
[L1168] [47:18.24] is yes, it might be the question is no.
[L1169] [47:20.40] We have to do research and that's sort
[L1170] [47:22.96] of how it started. And then
[L1171] [47:26.56] then I I believe the the main advantage
[L1172] [47:30.32] of uh being in academia is really the
[L1173] [47:33.20] long term and being independent. So in
[L1174] [47:36.00] the long term I mean ind in industry I'm
[L1175] [47:39.12] sure there are many periods including
[L1176] [47:40.64] now where I could be paid 10 times what
[L1177] [47:42.72] I'm being paid at university if I joined
[L1178] [47:46.16] Google or any of the other companies in
[L1179] [47:48.08] Silicon Valley. But um then times also
[L1180] [47:51.92] change and sometimes essentially what
[L1181] [47:53.28] you do is no longer relevant and then
[L1182] [47:54.96] it's very easy to get fired and to
[L1183] [47:58.32] then you say no big deal I can do
[L1184] [47:59.84] something else but at a university you
[L1185] [48:02.32] have essentially long-term tenure to do
[L1186] [48:04.24] exactly what you want. So no manager you
[L1187] [48:06.64] can do define your own research agenda.
[L1188] [48:09.92] Of course you have to get some money
[L1189] [48:11.92] that that that is uh is hard. You have
[L1190] [48:14.48] to get grants and things like that. you
[L1191] [48:16.16] have to convince students that what you
[L1192] [48:18.32] do is uh is the right thing and but
[L1193] [48:21.12] that's also very rewarding working with
[L1194] [48:23.04] students. So I think I in in the end I'm
[L1195] [48:25.76] I'm very happy that I took the career I
[L1196] [48:27.92] took.
[L1197] [48:28.56] >> What about looking back on Scola? Um you
[L1198] [48:31.44] know do you have so much experience
[L1199] [48:32.96] there. What are some things that went
[L1200] [48:34.96] well or things that didn't go well and
[L1201] [48:37.20] maybe some learnings you could share?
[L1202] [48:39.36] Scala was initially this experiment that
[L1203] [48:41.84] we could uh combine object-oriented and
[L1204] [48:44.56] functional programming and technically
[L1205] [48:47.04] that experiment was a big success uh um
[L1206] [48:51.52] in terms of the ecosystem it had a lot
[L1207] [48:54.00] of challenges. I don't know whether you
[L1208] [48:55.68] know there was a there was a short
[L1209] [48:57.76] incomplete history of programming
[L1210] [48:59.28] languages by James Ivy which is quite
[L1211] [49:01.28] hilarious and there was there's a
[L1212] [49:02.88] scholar entry there that this says I
[L1213] [49:05.04] discovered reef spell sandwiches and I
[L1214] [49:08.16] had an idea to essentially have a
[L1215] [49:10.24] language where you put in both object
[L1216] [49:12.16] and functional and then it ends with
[L1217] [49:14.40] this pieces of both communities and
[L1218] [49:16.48] they're promptly declared jihad and
[L1219] [49:19.04] that's [laughter] at the at the
[L1220] [49:21.20] beginning it was very funny but uh in
[L1221] [49:23.60] retrospect That's to a large degree what
[L1222] [49:25.68] happened. I mean there was there were
[L1223] [49:27.28] there were a lot of fights and cultural
[L1224] [49:28.96] fights and things like that. So um and
[L1225] [49:33.28] um
[L1226] [49:35.20] we might have uh it was a challenge and
[L1227] [49:38.72] I don't know in retrospect I think it
[L1228] [49:43.04] might have been
[L1229] [49:45.76] more prudent to be more careful
[L1230] [49:48.48] introducing functional features because
[L1231] [49:50.32] that sort of was we went in uh
[L1232] [49:53.68] essentially
[L1233] [49:55.52] quite complete. So essentially you can
[L1234] [49:57.20] port most Haskell programs to Scala
[L1235] [49:59.60] maybe that you you find them a bit less
[L1236] [50:02.32] attractive looking but you can do it and
[L1237] [50:05.84] that was that brought in essentially
[L1238] [50:09.60] different cultures very
[L1239] [50:12.08] and it caused a big clash of cultures.
[L1240] [50:14.64] So uh for instance in go Go was a lot
[L1241] [50:18.16] maligned because they didn't even have
[L1242] [50:20.48] generics right and it's it's true it was
[L1243] [50:22.72] a ridiculous language but uh by not
[L1244] [50:25.92] having it initially you sort of form a
[L1245] [50:27.92] culture that when you add it nothing
[L1246] [50:29.92] much will go wrong and people won't
[L1247] [50:31.68] overabstract or things like that and by
[L1248] [50:34.24] essentially going full hog into into it
[L1249] [50:36.64] with Scala from the start we were not
[L1250] [50:38.88] protected against that and people did uh
[L1251] [50:41.76] reach abstraction peaks and over
[L1252] [50:43.44] abstract it and and things like that and
[L1253] [50:45.84] that's they still do it to this very
[L1254] [50:47.68] day. So essentially having fancy
[L1255] [50:49.68] abstractions is great but you have to
[L1256] [50:51.60] use them responsibly and uh that then it
[L1257] [50:54.72] sort of clashes with the natural urge to
[L1258] [50:57.92] just try out all these fancy things and
[L1259] [50:59.92] do do something that in the end maybe
[L1260] [51:02.48] neither no you nor understands very well
[L1261] [51:05.44] and it could have just been a simple map
[L1262] [51:07.92] or things like that but uh yeah why do
[L1263] [51:11.12] use that when it can be complicated? Why
[L1264] [51:13.68] would that upset someone?
[L1265] [51:15.52] >> Because of the library ecosystem. I
[L1266] [51:17.76] think that um
[L1267] [51:20.08] um the
[L1268] [51:22.64] so libraries are are important and
[L1269] [51:26.08] because they sort of set the agenda how
[L1270] [51:28.64] you express your programs and in
[L1271] [51:30.96] particular the the uh the libraries that
[L1272] [51:34.08] come from the Haskell side. They're
[L1273] [51:35.68] essentially monatic frameworks and they
[L1274] [51:37.84] require you to express your whole
[L1275] [51:39.20] program as a monot which is a concept
[L1276] [51:41.52] that works well in functional
[L1277] [51:43.36] programming. I have my reservations. I
[L1278] [51:45.68] wouldn't actually do that in my in my
[L1279] [51:47.44] scholar programs, but by having
[L1280] [51:50.08] prominent libraries out there, uh it's
[L1281] [51:53.28] quite normative that people feel like
[L1282] [51:55.68] they they're being a [snorts] scholar
[L1283] [51:57.60] programmer, they're required to program
[L1284] [51:59.28] this way. And then of course there are
[L1285] [52:01.52] opinion leaders and conferences and all
[L1286] [52:03.84] these things that uh tell you how how
[L1287] [52:06.16] you should be writing your programs
[L1288] [52:09.44] where I would say I I think the most of
[L1289] [52:12.00] the scholar community is actually very
[L1290] [52:13.76] very levelheaded and and and and and I I
[L1291] [52:16.80] think most of the advice is great but uh
[L1292] [52:19.44] then um yeah uh it's it's still a
[L1293] [52:24.56] challenge because it's just too easy to
[L1294] [52:27.04] to mostly it's not really the opinion
[L1295] [52:29.52] leaders is in the in the community. But
[L1296] [52:31.84] let's say it's your boss. You have a
[L1297] [52:33.92] small team in a in a company. Your boss
[L1298] [52:35.68] came from Haskell and says, "Hey, this
[L1299] [52:37.68] is great. We do exactly like Haskell.
[L1300] [52:39.44] The whole thing." And then two years
[L1301] [52:41.20] later, the boss's boss says, "No, nobody
[L1302] [52:43.28] can understand this code. This code and
[L1303] [52:45.12] the project is canled." So these things
[L1304] [52:47.20] happened in in in in the industry. Uh
[L1305] [52:50.32] I'm not saying that they they that all
[L1306] [52:53.28] projects are like that. Not at all. I
[L1307] [52:54.80] mean there are lots of really great
[L1308] [52:56.16] success stories of Scala but that's
[L1309] [52:58.72] essentially a challenge in terms of
[L1310] [53:01.28] tech. Um I I think in the end um I wish
[L1311] [53:08.16] we had been a bit less dependent on the
[L1312] [53:10.56] JVM u uh in the sense that we took a lot
[L1313] [53:14.48] from Java that intuitively makes sense
[L1314] [53:18.16] but in the end and and was very
[L1315] [53:20.72] important for interrupt but in the end
[L1316] [53:22.48] wasn't wasn't
[L1317] [53:24.40] could have been done better. So for
[L1318] [53:26.00] instance uh in in Java being an object-
[L1319] [53:30.40] oriented language you have universal
[L1320] [53:32.08] methods like tworing and equals and hash
[L1321] [53:34.48] code and they're defined for everything
[L1322] [53:36.72] and languages like Rust or or Haskell
[L1323] [53:39.92] there are no more more discriminating.
[L1324] [53:41.76] They have a thing called type classes
[L1325] [53:43.20] where essentially you at compile time
[L1326] [53:45.20] you tell exactly where you have equality
[L1327] [53:47.76] and and hash code and these things and
[L1328] [53:49.52] it's a bit more tedious to set these
