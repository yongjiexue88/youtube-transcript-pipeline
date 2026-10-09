Chunk 4; segments 993–1335. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L1002] [36:01.92] drawing program and I've got some text
[L1003] [36:03.60] and I've got some shapes and I've got um
[L1004] [36:05.76] some uh strokes, you know, some some
[L1005] [36:08.64] handdrawn stuff, whatever. And I want to
[L1006] [36:10.80] be able to to select a bunch of them and
[L1007] [36:13.20] I want the user interface to present to
[L1008] [36:15.68] me which things I could edit on these
[L1009] [36:18.40] shapes. So I want to be able to edit the
[L1010] [36:19.84] color and I want it to apply to all of
[L1011] [36:21.28] them. Right? This is just a basic
[L1012] [36:23.36] architectural problem that you have to
[L1013] [36:24.72] solve if you're going to write one of
[L1014] [36:25.68] these programs and you want it to be any
[L1015] [36:26.72] good. oftentimes you will see programs
[L1016] [36:29.12] where the person didn't solve this
[L1017] [36:30.32] problem and you can't do that. It's very
[L1018] [36:32.00] frustrating, right? So a good program
[L1019] [36:34.40] someone has solved that architectural
[L1020] [36:35.84] problem in some way
[L1021] [36:38.56] and I was watching um I just happened to
[L1022] [36:41.36] be watching because sometimes I do like
[L1023] [36:42.96] I like to watch old videos of computer
[L1024] [36:45.60] science pioneer stuff and I was watching
[L1025] [36:48.08] a a demo of Sketchpad. I'd seen it
[L1026] [36:50.24] before, but I was watching a de demo of
[L1027] [36:52.16] Ivan Southern Sketchpad. And Sketchpad,
[L1028] [36:54.16] for those who don't know, is a
[L1029] [36:55.44] groundbreaking computer graphics
[L1030] [36:57.28] program. It's done with a light pen. Uh,
[L1031] [37:01.28] and it was done in the early 60s. And
[L1032] [37:03.36] you could draw things like you do in a
[L1033] [37:05.84] modern CAD program and you could do
[L1034] [37:08.64] stuff that even a lot of modern CAD
[L1035] [37:10.88] programs don't really offer or only
[L1036] [37:13.04] offered recently. I think in the talk I
[L1037] [37:14.64] said in 2007 was the first time that
[L1038] [37:16.64] like AutoCAD got some of these features.
[L1039] [37:19.20] You could do stuff like say these two
[L1040] [37:21.04] shapes like this line has to be
[L1041] [37:22.88] perpendicular to that line, constrain
[L1042] [37:24.80] it, and you could just do whatever you
[L1043] [37:26.08] want with the drawing and it would like
[L1044] [37:27.36] resolve for like making that happen. And
[L1045] [37:29.52] these are very rare in programs even to
[L1046] [37:31.60] this day. Like that's just not a common
[L1047] [37:33.20] operation you would see in a drawing
[L1048] [37:34.48] package today. So [clears throat]
[L1049] [37:38.00] I was looking at this and I was like,
[L1050] [37:40.64] how the heck did he solve this
[L1051] [37:43.52] architectural problem? like how did he
[L1052] [37:47.60] do this stuff in the early 1960s like in
[L1053] [37:51.68] assembly language with no editing tools,
[L1054] [37:55.76] no debugging tools. I mean, this would
[L1055] [37:57.52] have been like, you know, either punch
[L1056] [38:00.48] cards or one step away from punch cards.
[L1057] [38:02.32] Like, it it would have been hard to
[L1058] [38:05.12] develop this stuff.
[L1059] [38:07.28] And when I went back and I went through
[L1060] [38:09.20] his thesis and I looked at the code,
[L1061] [38:11.28] it's actually documented how he did it.
[L1062] [38:13.20] And I realized like, oh crap, this is
[L1063] [38:16.32] actually like an entity component system
[L1064] [38:18.80] basically like what we would now
[L1065] [38:21.12] consider sort of stateofthe-art
[L1066] [38:24.72] of real time architecture for doing
[L1067] [38:28.40] these kind of operations meaning
[L1068] [38:30.32] crosscutting like operating on this kind
[L1069] [38:33.76] of property across many things at once
[L1070] [38:36.64] that are all kind of different.
[L1071] [38:39.68] And this was something that
[L1072] [38:41.28] object-oriented programming, I'm
[L1073] [38:42.80] editorializing now. Bunch of people will
[L1074] [38:44.80] complain that I'm saying this, but this
[L1075] [38:46.00] is just my opinion. Object-oriented
[L1076] [38:48.32] programming and the pedagogy around it
[L1077] [38:50.88] really struggled with that problem for a
[L1078] [38:52.80] long time because there were teaching
[L1079] [38:54.64] despite people who will now claim
[L1080] [38:56.48] otherwise. I document it very completely
[L1081] [38:58.08] in the talk. So I I don't think they
[L1082] [39:00.08] have any leg to stand on. But the
[L1083] [39:01.84] pedagogy at the time was all about build
[L1084] [39:03.76] a domain model. The domain model looks
[L1085] [39:06.32] like your hierarchy basically like I've
[L1086] [39:08.56] got employees and employees I've got
[L1087] [39:10.96] contractors and I've got derived like is
[L1088] [39:13.52] this a full-time employee or a part-time
[L1089] [39:15.20] employee like that was how they
[L1090] [39:17.44] suggested these things should be
[L1091] [39:19.28] implemented right and that kind of
[L1092] [39:21.52] architecture doesn't work for these
[L1093] [39:24.08] kinds of operations that I'm talking
[L1094] [39:26.16] about identity component systems do and
[L1095] [39:28.88] generally that kind of sort of uh
[L1096] [39:31.28] rotated architecture I might call it uh
[L1097] [39:33.92] does work for these.
[L1098] [39:36.16] And so what I call the 35 mistake is the
[L1099] [39:38.88] fact that
[L1100] [39:41.04] I very ironically in my opinion
[L1101] [39:44.32] sketchpad sort of showed in its
[L1102] [39:46.72] architecture how you could solve this
[L1103] [39:48.56] problem and how you could solve it in
[L1104] [39:50.24] arguably an object-oriented way. I think
[L1105] [39:52.72] if you squint at it, a person who does
[L1106] [39:54.56] object-oriented programming could easily
[L1107] [39:56.16] make an argument that you could do an
[L1108] [39:57.44] object-oriented version of this. You
[L1109] [39:59.04] don't have to violate any particular
[L1110] [40:00.64] principles to do it. It's just not the
[L1111] [40:03.84] hierarchy domain model way that people
[L1112] [40:07.44] were conceptualizing it through a lot of
[L1113] [40:09.36] the, you know, 80s and 90s, let's say,
[L1114] [40:12.40] and even unfortunately to this day, but,
[L1115] [40:14.24] you know, I think a lot of object
[L1116] [40:15.60] ordering programs don't do that anymore.
[L1117] [40:18.00] Ironically, that was in Sketchpad. The
[L1118] [40:20.40] DNA was there and we could have had it
[L1119] [40:22.32] right away because Ivan Sutherland
[L1120] [40:24.24] figured it out. But weirdly enough, the
[L1121] [40:27.60] whole idea of this sort of uh
[L1122] [40:29.76] inheritance hierarchy with lots of
[L1123] [40:31.68] encapsulation around it
[L1124] [40:34.48] grew in part out of Sketchpad because
[L1125] [40:37.52] like Alan K looked at it and said like,
[L1126] [40:39.68] "Oh, the interesting part of this is the
[L1127] [40:42.40] fact that you could take a a shape and
[L1128] [40:44.64] not know what it was and just have this
[L1129] [40:46.80] like draw a circle call on it or
[L1130] [40:48.48] something." That was the part they took
[L1131] [40:50.08] away from it, which is much less
[L1132] [40:51.20] interesting in my opinion and not that
[L1133] [40:52.72] architecturally useful in most cases.
[L1134] [40:55.60] So in kind of this amusing way,
[L1135] [40:57.84] Sketchpad contained in if if you know
[L1136] [41:00.48] I'm editorializing it contained what I
[L1137] [41:03.28] consider to be a good architectural
[L1138] [41:05.04] idea, but the takeaway from it was a bad
[L1139] [41:07.68] architectural idea is is how I would say
[L1140] [41:09.68] it. And saying bad architectural idea is
[L1141] [41:11.60] a little bit strong because as I say in
[L1142] [41:13.20] the talk, I think there are times when
[L1143] [41:15.04] you do want to think like a very high
[L1144] [41:17.04] level, you might want to think about
[L1145] [41:18.24] things in kind of the way that you know
[L1146] [41:20.88] small talk thinks about them. Um, so I
[L1147] [41:23.28] don't want to say bad idea in the
[L1148] [41:24.48] absolute sense, but bad in the way it
[L1149] [41:26.08] ended up being uh, you know, applied,
[L1150] [41:28.88] let's say.
[L1151] [41:29.84] >> Why is that class hierarchy not work for
[L1152] [41:32.32] this problem?
[L1153] [41:33.36] >> It's it's pretty easy to understand
[L1154] [41:34.96] actually. So when you think through an
[L1155] [41:38.00] inheritance hierarchy that's based on
[L1156] [41:39.76] sort of what you see in the real world
[L1157] [41:42.32] or what you're trying to model. So you
[L1158] [41:44.40] say like uh the typical example and it's
[L1159] [41:46.88] brought up tons of times by uh people
[L1160] [41:49.44] who wrote the oop literature like be
[L1161] [41:51.36] true strip uh like the small talk people
[L1162] [41:54.64] is the idea is uh keeping it with a
[L1163] [41:57.04] sketch pad example I'm going to have a
[L1164] [41:58.32] shape from the shape I'm going to derive
[L1165] [42:00.40] like triangle or circle and the
[L1166] [42:04.40] encapsulation is around that thing. So a
[L1167] [42:07.28] circle has a radius but shapes don't
[L1168] [42:10.48] have radiuses. shapes don't necessarily
[L1169] [42:13.28] know what that is, right? So, it tends
[L1170] [42:15.20] to get deferred down and the
[L1171] [42:16.48] encapsulation boundary is drawn around
[L1172] [42:19.52] that sort of derived class that's like
[L1173] [42:21.60] the most derived version of whatever
[L1174] [42:23.76] this thing is, right?
[L1175] [42:25.92] The problem is that creates a lot of
[L1176] [42:29.04] headaches when now something that wants
[L1177] [42:31.12] to work across a lot of shapes needs to
[L1178] [42:34.40] actually do something intelligent with
[L1179] [42:37.92] modifying say the scale of something or
[L1180] [42:41.12] wanting to change its color because it
[L1181] [42:43.28] doesn't really have a way to know what's
[L1182] [42:45.44] going on in these highly encapsulated
[L1183] [42:47.60] things.
[L1184] [42:49.52] So typically what you end up having to
[L1185] [42:51.12] do in those sit in those situations is
[L1186] [42:53.20] you then have to take this inheritance
[L1187] [42:54.64] hierarchy and kind of in a sense throw
[L1188] [42:56.56] away the benefits of it. you end up
[L1189] [42:58.56] having to make at the top all of these
[L1190] [43:00.80] accessor iterator things that allow you
[L1191] [43:03.12] to probe into that like lower class and
[L1192] [43:07.20] say tell me all of the colors that you
[L1193] [43:09.68] might be using and a name for them,
[L1194] [43:11.92] right? Or and so in a sense what you end
[L1195] [43:14.40] up having to do when you want the
[L1196] [43:16.00] architecture to work is you have to
[L1197] [43:17.68] rebuild the sketchpad version on top of
[L1198] [43:21.12] the inheritance hierarchy version which
[L1199] [43:22.80] doesn't really do anything for you,
[L1200] [43:24.08] right? And it's not to say that there
[L1201] [43:25.84] isn't some benefit that you can derive
[L1202] [43:28.56] from having derived is kind of a pun
[L1203] [43:30.64] here I guess that you can derive from
[L1204] [43:32.32] having this idea of saying this thing is
[L1205] [43:35.60] like this other thing. Please give me
[L1206] [43:37.60] some of the implementation of it. That's
[L1207] [43:39.52] not necessarily a bad thing in practice.
[L1208] [43:41.92] The problem is when you teach people
[L1209] [43:43.60] that this is how it's going to work.
[L1210] [43:45.04] Like you just make this hierarchy and
[L1211] [43:46.40] then your architecture is just supposed
[L1212] [43:47.76] to work. it really illprepares them for
[L1213] [43:50.56] the reality that like that's actually
[L1214] [43:52.16] not going to solve most of most of the
[L1215] [43:53.76] problems that you have are not going to
[L1216] [43:54.88] be solved that way. Um and again it just
[L1217] [43:57.28] comes from this fact that typically when
[L1218] [43:58.88] we're working with computer programs
[L1219] [44:01.04] most of the time what we need to do is
[L1220] [44:03.28] create crosscutting operations that work
[L1221] [44:06.72] with a lot of the data that's inside
[L1222] [44:08.80] these derived classes. that's actually
[L1223] [44:10.80] the thing that we want to do and it's
[L1224] [44:13.04] really cumbersome and typically a bad
[L1225] [44:15.52] fit for the problem space to put that
[L1226] [44:17.92] into some virtual functions that are
[L1227] [44:20.16] sitting at the top of this very uh sort
[L1228] [44:22.24] of tall hierarchy. It's usually much
[L1229] [44:24.40] better to do uh again even if you're
[L1230] [44:27.44] doing object programming you don't have
[L1231] [44:28.96] to stop doing objecting program you just
[L1232] [44:30.48] have to think about it differently you
[L1233] [44:32.56] have to think about what the objects are
[L1234] [44:34.24] differently uh where you're drawing the
[L1235] [44:35.92] encapsulation boundaries it just helps
[L1236] [44:37.76] to think about it differently and say
[L1237] [44:39.52] actually the more important things to
[L1238] [44:40.88] model are what are the things that stuff
[L1239] [44:42.88] is built out of how do I build a circle
[L1240] [44:46.24] out of objects right what are those
[L1241] [44:48.88] things a radius property a center
[L1242] [44:51.28] property those maybe should be the
[L1243] [44:53.28] objects that I'm thinking of as more
[L1244] [44:55.36] first class citizens and this
[L1245] [44:57.12] inheritance hierarchy stuff about what
[L1246] [44:58.64] the objects are that I see on the screen
[L1247] [45:00.00] like triangle and circle that's a
[L1248] [45:02.00] distraction that's not the proper way to
[L1249] [45:03.84] model the problem um and again I don't
[L1250] [45:06.72] think I would be pissing off any
[L1251] [45:08.16] object-oriented programmers by saying
[L1252] [45:09.84] that today because I think a lot of them
[L1253] [45:12.08] use architectures that do think about
[L1254] [45:15.04] objects in that sort of rotated sense
[L1255] [45:17.84] and not in the domain model hierarchy
[L1256] [45:19.76] sense not that there aren't still people
[L1257] [45:21.04] who are doing that but you know It's
[L1258] [45:22.96] it's not the only way to to go nowadays.
[L1259] [45:25.52] It's not the only way it's promulgated.
[L1260] [45:28.56] Yeah, because I guess my immediate
[L1261] [45:29.76] thought would have been in in that case
[L1262] [45:32.56] the the base class has the notion of a
[L1263] [45:35.44] color or some shared thing and we just
[L1264] [45:38.32] operate if you're a shape then we assume
[L1265] [45:40.80] you have a color and we but you're
[L1266] [45:42.64] saying refactoring and putting up in
[L1267] [45:45.20] there's suboptimal and there's you want
[L1268] [45:48.32] all these uh subasses to have some
[L1269] [45:51.84] handle to some radius property or
[L1270] [45:54.40] something like that. is that
[L1271] [45:55.68] >> what you just described is what tends to
[L1272] [45:57.84] happen in systems that are architected
[L1273] [45:59.44] this way. you end up with your derived
[L1274] [46:01.20] class not really being very much of
[L1275] [46:03.20] anything because in order to edit stuff
[L1276] [46:05.44] you had to migrate it all up to the top
[L1277] [46:08.08] and that there was actually terms for
[L1278] [46:09.76] this uh in the old days I don't still
[L1279] [46:11.20] use like fatty base classes right are
[L1280] [46:13.36] things like that's like it just ends up
[L1281] [46:14.96] your base class has like every type of
[L1282] [46:16.72] property that any derived class might
[L1283] [46:18.56] ever have like you have like get primary
[L1284] [46:20.64] color get secondary color get tertiary
[L1285] [46:22.16] color get right because it's like
[L1286] [46:23.36] something needed three different colors
[L1287] [46:24.72] or whatever uh and most things don't use
[L1288] [46:27.04] those colors and all these other sorts
[L1289] [46:28.72] of things
[L1290] [46:29.92] And so um there's certainly nothing
[L1291] [46:32.08] wrong with running a program that way.
[L1292] [46:33.44] It's just again why did you bother with
[L1293] [46:35.20] the hierarchy? Like you're not getting
[L1294] [46:36.88] any actual encapsulation benefits from
[L1295] [46:38.88] it because you just forced everything to
[L1296] [46:40.56] the base class anyway. So why didn't you
[L1297] [46:42.00] just make that be your thing? Just make
[L1298] [46:43.76] one class called shape and be done.
[L1299] [46:46.16] Right? So uh in terms of the the ECS
[L1300] [46:50.24] style of implementation and I don't
[L1301] [46:51.84] necessarily want to advocate for it or
[L1302] [46:53.76] not because uh I I don't actually
[L1303] [46:55.76] personally use ECS's or anything like
[L1304] [46:57.44] that but they are very common. Now
[L1305] [47:00.32] the idea there is to just turn it on its
[L1306] [47:02.16] side and say look typically what we want
[L1307] [47:04.88] to do is do things like okay there's
[L1308] [47:07.20] stuff that has like physics on it like
[L1309] [47:09.44] you know I'm I'm doing this thing and
[L1310] [47:10.56] and I want to have like physical
[L1311] [47:12.00] simulation of of entities. Well, the
[L1312] [47:14.64] physics system is the thing that
[L1313] [47:15.92] probably knows how that should be
[L1314] [47:17.12] stored. So rather than having that be
[L1315] [47:19.68] data in my derived class that is
[L1316] [47:22.24] encapsulated around the derived class.
[L1317] [47:24.24] Instead, why don't I just have the
[L1318] [47:25.84] physics system knows what physics is.
[L1319] [47:28.72] And then if you want to make something
[L1320] [47:30.32] that participates in physics, you just
[L1321] [47:32.56] have a handle for whatever this thing
[L1322] [47:34.72] is, like a handle for my shape. That
[L1323] [47:36.64] handle is valid in all the systems. So I
[L1324] [47:38.96] can go look up the physics properties of
[L1325] [47:41.04] the shape and gather it when I want to
[L1326] [47:43.84] actually do something with it. But
[L1327] [47:45.36] generally speaking, the encapsulation
[L1328] [47:47.20] stays around the system. So physics
[L1329] [47:49.84] properties are defined by the physics
[L1330] [47:51.60] system because hey, that's who knows how
[L1331] [47:53.76] physics should work and I just ask about
[L1332] [47:57.12] my physics when I need to do something
[L1333] [47:58.64] with it. And this kind of gets you out
[L1334] [48:00.32] of that problem. And then now you can
[L1335] [48:02.24] just compose things. Oh, I want to make
[L1336] [48:04.16] something that has several physics
[L1337] [48:05.68] elements in it. Fine. I can just have
[L1338] [48:07.36] multiple physics handles if that's what
[L1339] [48:08.64] I need or something like this. I can
[L1340] [48:10.00] very flexibly like merge these things
[L1341] [48:11.76] together. I want something to not have
[L1342] [48:13.52] physics. I just don't ever insert the,
[L1343] [48:15.92] you know, I don't ever ask the physics
[L1344] [48:17.12] system to have a valid, you know, piece
