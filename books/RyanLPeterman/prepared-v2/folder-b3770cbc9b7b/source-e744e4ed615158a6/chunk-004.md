Chunk 4; segments 975–1307. Start may repeat the previous chunk for context.

# Creator of uv, ty, Ruff: How Software Engineering Is Changing | Charlie Marsh

Source ID: source-e744e4ed615158a6
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_uv,_ty,_Ruff_How_Software_Engineering_Is_Changing_Charlie_Marsh_en.txt
Video: https://www.youtube.com/watch?v=Iw65FD4MGgs

[L984] [35:37.76] faster than what was available at the
[L985] [35:39.92] time.
[L986] [35:41.12] >> How much of a difference did Rust make
[L987] [35:44.08] on that graph?
[L988] [35:45.92] >> I think it so it depends a bit on the
[L989] [35:48.00] project. Um I think I think in rough
[L990] [35:52.32] a lot of it was just Rust. Um and then
[L991] [35:56.80] over time I think we've
[L992] [35:59.68] um
[L993] [36:01.28] improved on that a lot because
[L994] [36:04.48] uh because you can even look at the
[L995] [36:06.80] history of the project like the project
[L996] [36:09.36] I mean hopefully no one like hopefully
[L997] [36:11.36] this is still true but like basically
[L998] [36:12.80] over time the project gets faster um and
[L999] [36:16.24] sometimes that regresses but like uh you
[L1000] [36:18.64] know you basically maybe I put it
[L1001] [36:20.16] differently you could write rough you
[L1002] [36:24.08] know in like a couple different ways all
[L1003] [36:27.04] in rust and they could have really
[L1004] [36:28.80] different performance characteristics.
[L1005] [36:30.16] So that's just to say that like I I
[L1006] [36:32.24] generally think of rust as like the the
[L1007] [36:35.44] floor or the uh the sort of like the
[L1008] [36:39.36] baseline performance that you get is
[L1009] [36:40.88] going to be significantly better. But
[L1010] [36:42.64] you still have to you still get a lot
[L1011] [36:44.80] more out of like thinking deeply about
[L1012] [36:46.64] performance and design. Like if you take
[L1013] [36:48.64] the same program in Rust and in Python
[L1014] [36:50.72] like exact same implementation to to the
[L1015] [36:52.88] closest approximation you can get like
[L1016] [36:54.72] the Rust one will be faster but you can
[L1017] [36:56.88] then take that program and you can
[L1018] [36:58.08] probably optimize it another like 10x um
[L1019] [37:00.40] I don't know about 10x but my point is
[L1020] [37:02.48] even within being written in Rust
[L1021] [37:04.16] there's like a ton of room for how to
[L1022] [37:06.64] make things more performant how to write
[L1023] [37:08.08] really performant software and like
[L1024] [37:09.60] again when I started working on Rough um
[L1025] [37:12.72] part of my my goal was to learn Rust and
[L1026] [37:14.80] so I wrote I did write a lot of like bad
[L1027] [37:16.80] code Um, which is fine. Like I shipped
[L1028] [37:20.24] something out that was really helpful to
[L1029] [37:21.44] people. Um, but it's gotten a lot better
[L1030] [37:23.20] I think over time and like we've made it
[L1031] [37:24.88] more and more performant. Um I think in
[L1032] [37:27.52] UV
[L1033] [37:29.28] there was more um sort of like
[L1034] [37:32.88] architectural innovation beyond just
[L1035] [37:35.20] being in Rust especially because UV like
[L1036] [37:37.68] so as a package manager um you're doing
[L1037] [37:39.68] a ton of IO like downloading f and you
[L1038] [37:42.80] know downloading files over the network
[L1039] [37:44.56] unzipping things like writing them to
[L1040] [37:46.48] disk moving them around the llinter
[L1041] [37:49.04] doesn't have to do as much of that I
[L1042] [37:50.56] mean it has to read all your files but
[L1043] [37:52.88] there's there's not like a sign a huge
[L1044] [37:54.72] amount of IO
[L1045] [37:55.92] the package manager is like mostly IO.
[L1046] [37:58.16] It's like and then you're trying to do
[L1047] [38:00.08] things like very efficiently. So um
[L1048] [38:01.84] there it was more I mean rust was
[L1049] [38:04.56] important but I I do think that in UV
[L1050] [38:07.68] there's more um you know architectural
[L1051] [38:10.80] things that we did or like ways that we
[L1052] [38:12.72] thought a lot about performance like the
[L1053] [38:14.00] c the design of the cache is like very
[L1054] [38:16.72] very intentional um and makes it so that
[L1055] [38:21.12] um
[L1056] [38:22.96] like repeated installs of the same
[L1057] [38:25.84] package on your machine are like are
[L1058] [38:28.32] like near instant because of the way
[L1059] [38:30.16] that we like lay out the cache and the
[L1060] [38:31.92] way that we install from the cache into
[L1061] [38:33.68] your projects. Um, it basically means
[L1062] [38:35.36] that if you've installed a package
[L1063] [38:36.64] before, installing it again is extremely
[L1064] [38:39.52] cheap. Um, and both in terms of disc
[L1065] [38:42.16] space and time. Um, and so that was like
[L1066] [38:44.64] that's like a very different design than
[L1067] [38:46.64] um, any of the other like Python package
[L1068] [38:48.48] managers had. Uh, so again, it kind of
[L1069] [38:50.80] depends on the project. Um, I do tend to
[L1070] [38:53.60] think that like whether you're writing
[L1071] [38:55.36] code in Rust or in Python, there's like
[L1072] [38:57.12] always room to like be thinking about
[L1073] [38:58.72] performance. like you can always make
[L1074] [39:01.52] things faster or slower. Like even if
[L1075] [39:03.04] you're writing in Python, like you can
[L1076] [39:04.48] still make things like much much faster
[L1077] [39:06.72] um by like thinking harder about
[L1078] [39:09.12] performance and design. Um so it's some
[L1079] [39:11.84] mix but it depends on the project.
[L1080] [39:14.80] >> Open AAI, Enthropic, Cursor, and
[L1081] [39:17.76] Verscell all use this product to make
[L1082] [39:19.92] their lives better. And the problem it
[L1083] [39:22.08] solves is when you're building SAS or an
[L1084] [39:24.32] AI product and you want to sell to other
[L1085] [39:26.64] companies, there's all these
[L1086] [39:28.16] requirements you need to meet. There's
[L1087] [39:30.08] SSO, there's skim, there's arbback,
[L1088] [39:33.36] there's audit logs. These are all things
[L1089] [39:35.20] that take time to integrate, but aren't
[L1090] [39:37.36] the main focus of your app. Work OS is
[L1091] [39:39.52] an API layer that lets you meet all of
[L1092] [39:41.44] these requirements in just a few lines
[L1093] [39:43.60] of code. So, let's say you have a new
[L1094] [39:45.60] SAS product and you want to sell to
[L1095] [39:47.36] other companies. work OS will solve all
[L1096] [39:49.76] of these critical feature gaps for you.
[L1097] [39:52.48] You can check them out at workos.com to
[L1098] [39:55.12] learn more and get started and I
[L1099] [39:57.28] appreciate them for supporting my work
[L1100] [39:58.96] and sponsoring this podcast over the
[L1101] [40:01.36] course of the project. Do you have a you
[L1102] [40:04.56] know top few things that were
[L1103] [40:06.72] implementing the project that were
[L1104] [40:08.80] technically challenging or most
[L1105] [40:10.32] interesting to you? I really like this
[L1106] [40:12.80] optimization that Andrew on our team um
[L1107] [40:16.64] who goes by burnt sushi. He's uh he's
[L1108] [40:19.60] the author of Rip Grap and bunch of
[L1109] [40:22.16] other things. He's like really amazing
[L1110] [40:23.76] engineer. He did this really cool
[L1111] [40:26.16] optimization around how we represent
[L1112] [40:27.68] versions. It's pretty cool. I mean
[L1113] [40:29.36] basically like if you think about
[L1114] [40:30.64] resolving and installing like a very
[L1115] [40:32.32] complex Python project um we we it turns
[L1116] [40:36.00] out that we have to like parse and
[L1117] [40:39.04] create lots of versions like as in 1.0.1
[L1118] [40:43.12] 1.0.2 to like we just like version
[L1119] [40:45.76] objects within the program like we end
[L1120] [40:47.60] up parsing and creating a lot of those
[L1121] [40:49.84] and it turns out that actually like
[L1122] [40:51.68] allocating that memory um was expensive
[L1123] [40:54.88] um given like the scale like the number
[L1124] [40:57.20] of times we were doing it and he came up
[L1125] [40:59.44] with a representation where we can
[L1126] [41:01.36] represent um like 90 something% of
[L1127] [41:04.00] versions with a single U64 integer. So
[L1128] [41:06.96] it's just like way more efficient. Um
[L1129] [41:08.72] and uh the benchmarks around that and
[L1130] [41:10.72] the implementation were were very cool.
[L1131] [41:12.40] It's like one of the coolest PRs I've
[L1132] [41:13.68] read, I think. Um, in TY, which our type
[L1133] [41:17.44] checker, there's a lot of like very
[L1134] [41:19.84] interesting performance work that's
[L1135] [41:22.24] happening, especially to make it um
[L1136] [41:25.36] incremental. So like uh uh TY is
[L1137] [41:29.52] designed to be um a type checker and a
[L1138] [41:31.68] language server. And
[L1139] [41:34.64] the whole system is like highly
[L1140] [41:36.00] incremental. So the idea there is like
[L1141] [41:38.16] if you're in an a text editor and you
[L1142] [41:40.56] open up like one file, you don't
[L1143] [41:43.04] necessarily want to like have to type
[L1144] [41:45.04] check your entire project like all your
[L1145] [41:47.04] dependencies, every file in the project
[L1146] [41:48.48] just to get analysis for that file. Um
[L1147] [41:51.92] like because you don't need to. Um so so
[L1148] [41:55.68] how do you make that work? That's like
[L1149] [41:56.88] that's sort of like uh I would that
[L1150] [41:58.72] would be like lazy. You want to be lazy.
[L1151] [42:01.36] Um, but the other piece to that is like
[L1152] [42:02.96] if you have a file open and you edit it,
[L1153] [42:06.24] um, or you have like two files open, you
[L1154] [42:08.08] edit one of them. Um, you only want to
[L1155] [42:11.44] recmp compute like exactly what you need
[L1156] [42:12.96] to recomputee. Like you don't want to
[L1157] [42:14.32] have to go and retype check like the
[L1158] [42:15.92] entire codebase again. Um, especially
[L1159] [42:18.08] because maybe you're working in a big
[L1160] [42:19.28] project like PyTorch and it's like you
[L1161] [42:21.28] have two files open, you edit one of
[L1162] [42:22.64] them, you don't want it to like and then
[L1163] [42:24.16] you save, you don't want it to take like
[L1164] [42:25.36] two seconds to like retype check the
[L1165] [42:26.96] project and like give you a new
[L1166] [42:28.00] analysis. So the whole system is built
[L1167] [42:31.04] around queries um which is pretty
[L1168] [42:33.28] interesting. This is more of like a
[L1169] [42:34.32] macro design thing. Um but uh we built
[L1170] [42:37.20] it on top of a framework called Salsa
[L1171] [42:39.04] which is um also what Rust Analyzer uses
[L1172] [42:41.60] which is like the popular Rust language
[L1173] [42:43.28] server. Um and now we've
[L1174] [42:47.28] intentionally or inadvertently become
[L1175] [42:48.96] like like very large contributors to
[L1176] [42:51.60] Salsa. Um but but the whole the whole
[L1177] [42:54.16] system is built around that which has
[L1178] [42:55.44] been like very interesting
[L1179] [42:56.32] architecturally.
[L1180] [42:57.60] >> Interesting. So it's it's lazy so it
[L1181] [43:00.00] doesn't type check the whole codebase
[L1182] [43:01.76] and it's incremental. So
[L1183] [43:03.04] >> yeah the incremental part is the thing
[L1184] [43:04.32] that's hard because you kind of need a
[L1185] [43:05.76] way to basically like uh it needs to be
[L1186] [43:08.64] able to model kind of like a dependency
[L1187] [43:10.08] graph of like everything that's
[L1188] [43:11.36] happening in the code. Um and so then
[L1189] [43:13.36] when you change something we want to
[L1190] [43:14.72] just like flow the data back through all
[L1191] [43:16.64] the different pieces like only the
[L1192] [43:18.00] pieces. Yeah. Um so that took a lot of
[L1193] [43:21.68] work. um but uh is it has come together
[L1194] [43:25.28] um and I've been doing a lot of
[L1195] [43:27.92] optimization lately with codecs um
[L1196] [43:32.32] because
[L1197] [43:34.96] it tends to be very good um at
[L1198] [43:37.68] especially at like micro optimizations
[L1199] [43:39.68] like if I'm like and in TY in particular
[L1200] [43:43.44] we also need to think a lot about memory
[L1201] [43:45.92] um not just speed because if you work on
[L1202] [43:49.20] a very large project like you don't want
[L1203] [43:50.72] it to take like many many many gigabytes
[L1204] [43:53.52] of you know just to like run your
[L1205] [43:55.60] language server like ideally you want it
[L1206] [43:57.04] to be like relatively efficient. Um, so
[L1207] [43:59.28] like I spend a lot of time now kind of
[L1208] [44:01.52] like continuously optimizing like memory
[L1209] [44:03.68] usage and performance and I can just set
[L1210] [44:05.36] a goal that's like try to reduce memory
[L1211] [44:07.76] like salsa memory by like 1% on this
[L1212] [44:11.04] project and like you can't do like these
[L1213] [44:13.84] these things that you might like like
[L1214] [44:16.08] try to do. Um,
[L1215] [44:18.24] and it's very good at just like coming
[L1216] [44:19.76] up with um like very reasonable things.
[L1217] [44:22.88] And so I I don't know. I find that very
[L1218] [44:24.96] cool because it's kind of like you can
[L1219] [44:26.24] almost have like continuously op I won't
[L1220] [44:28.16] say self optimizing that's like a built
[L1221] [44:29.76] grandiose but you can kind of be like
[L1222] [44:31.68] continuously like just like optimizing
[L1223] [44:33.60] your software. Um so uh I've been
[L1224] [44:36.48] enjoying that a lot. Um but uh but most
[L1225] [44:40.56] of those are like um yeah trying to find
[L1226] [44:43.28] ways to like represent things uh that
[L1227] [44:45.28] take up less memory um or uh trying to
[L1228] [44:49.12] come up with like sometimes it's like
[L1229] [44:50.56] trying to come up with broader redesigns
[L1230] [44:51.92] to like fix pathological performance.
[L1231] [44:55.12] >> That one optimization where with the
[L1232] [44:57.20] version numbering and seeing that
[L1233] [45:00.32] you can limit it just to like use 64. If
[L1234] [45:04.08] you think back to some of these more
[L1235] [45:05.76] creative optimizations that were done
[L1236] [45:08.16] that was in the human era, do you think
[L1237] [45:10.88] if you just I don't know ran codeex and
[L1238] [45:13.36] you're like hey just don't break things
[L1239] [45:14.96] but lower do you have faith that it
[L1240] [45:17.20] would come up with that or is that kind
[L1241] [45:18.64] of a a step above what
[L1242] [45:20.56] >> that's a very interesting question. If
[L1243] [45:22.24] you just at least in my experience like
[L1244] [45:24.00] if you just ask these things to reduce
[L1245] [45:25.36] memory or improve performance by some
[L1246] [45:28.48] you know moderate percentage it will
[L1247] [45:30.80] typically come up with things around the
[L1248] [45:32.48] edges um as opposed to like larger
[L1249] [45:35.84] uh redesigns or reconsiderations but you
[L1250] [45:38.48] can get to those larger redesigns if you
[L1251] [45:42.72] prompt and collaborate with the agent.
[L1252] [45:44.56] And so if you sort of ask like well like
[L1253] [45:48.32] should we be thinking a bit bigger about
[L1254] [45:49.84] like why we have to represent the data
[L1255] [45:51.76] this way like you can you can get to
[L1256] [45:53.84] like bigger ideas. And so that might be
[L1257] [45:56.48] an idea that you could have gotten to
[L1258] [45:58.08] with prompting if you were like um you
[L1259] [46:01.52] know okay let's start by like profiling
[L1260] [46:02.80] and figuring out where we're spending a
[L1261] [46:03.84] lot of time and then maybe the you know
[L1262] [46:06.00] would eventually come back to you and
[L1263] [46:07.60] say like we're spending a lot of time in
[L1264] [46:08.88] like version parsing and like version
[L1265] [46:10.96] like ball like version drop and version
[L1266] [46:12.88] allocation like blah blah and we' be
[L1267] [46:14.72] like okay well like how could we
[L1268] [46:15.84] represent these like more compactly and
[L1269] [46:17.44] it would probably start by finding like
[L1270] [46:19.20] micro optimizations in the
[L1271] [46:20.64] representation of like well this field
[L1272] [46:22.96] like you combine these two fields like
[L1273] [46:25.04] if you buy it's like blah blah blah but
[L1274] [46:26.88] I think if you kept pushing it like it's
[L1275] [46:28.56] plausible it would get there um but
[L1276] [46:30.88] that's not the thing it's going to come
[L1277] [46:31.92] up with by default. Mitchell Hashimoto
[L1278] [46:34.88] um who was like one of the Hashiore
[L1279] [46:37.68] founders works on Ghosty um he had a
[L1280] [46:40.96] post that was insightful I thought last
[L1281] [46:43.76] week or this weekend about a renderer he
[L1282] [46:46.48] wrote where it was like a really
[L1283] [46:47.44] terrible renderer. I'll probably butcher
[L1284] [46:49.28] the the tweet, but it was like it was a
[L1285] [46:51.04] really terrible renderer and then he
[L1286] [46:52.40] hadn't like intentionally and then he
[L1287] [46:53.68] had an LM like optimize it and it made
[L1288] [46:55.28] it like 10 times faster and he's like
[L1289] [46:57.04] great, right? Actually, no. like my
[L1290] [46:58.80] handwritten version was like a hundred
[L1291] [47:00.24] times faster and it's like you know like
[L1292] [47:02.64] you lose if you're not like using your
[L1293] [47:04.32] brain to like think about from first
[L1294] [47:06.96] principles like how fast should it be
[L1295] [47:08.48] and like how should the system work like
[L1296] [47:10.16] then you just like ship all this these
[L1297] [47:12.32] like accumulated like I mean I I won't
[L1298] [47:15.36] necessarily call it slop but it's like
[L1299] [47:16.88] you just ship these like things and
[L1300] [47:18.16] you're like yeah oh my god I made it 10
[L1301] [47:19.36] times faster but really it should be
[L1302] [47:20.64] like 100 times faster and so I think I
[L1303] [47:24.48] don't know it shouldn't be controversial
[L1304] [47:25.68] there's still a lot of room for like
[L1305] [47:26.64] using your brain Right. And like uh uh
[L1306] [47:30.40] but I do I do think it's like I struggle
[L1307] [47:33.12] with this stuff a lot. I mean like I'm
[L1308] [47:34.48] changing how I write software a lot and
[L1309] [47:36.80] um you know I've had people on my team
[L1310] [47:38.64] like because I'm using agents a lot and
[L1311] [47:40.80] and also was you know to some degree
[L1312] [47:43.04] trying to like
[L1313] [47:45.76] push our team to like use agents more. I
[L1314] [47:49.44] mean I mean some of that for me came
[L1315] [47:50.72] from a place of like we build tools for
[L1316] [47:53.52] software engineers and a lot of our
