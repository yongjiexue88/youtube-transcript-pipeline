Chunk 4; segments 1040–1359. Start may repeat the previous chunk for context.

# Turing Award Winner: TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC | David Patterson

Source ID: source-fc9308e696a718d4
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_TPU_vs_GPU_vs_CPU,_Computer_Architecture,_RISC_vs_CISC_David_Patterson_en.txt
Video: https://www.youtube.com/watch?v=Pn4ZwlEh5nw

[L1049] [41:07.84] it's all been internal. It's just for
[L1050] [41:09.44] Google to use or you could use it via
[L1051] [41:11.44] the cloud. Um but uh you these startups
[L1052] [41:15.36] have u you know have to have a
[L1053] [41:18.00] difficulty as a result. That's why the
[L1054] [41:20.72] ML Perf hasn't been as popular. Not
[L1055] [41:22.96] everybody runs them because uh Nvidia
[L1056] [41:25.68] runs them really well, really better
[L1057] [41:28.24] than everybody else. And the startups
[L1058] [41:30.00] have a hard time showing off what they
[L1059] [41:31.76] can do uh given they don't have the the
[L1060] [41:36.00] engineering effort going into the
[L1061] [41:37.20] libraries that you need to do well in ML
[L1062] [41:39.36] Perf. you gave this popular talk about
[L1063] [41:42.40] how to have a bad career and it's kind
[L1064] [41:44.88] of uh the negation of advice to kind of
[L1065] [41:49.04] have a good career and I was just
[L1066] [41:51.84] wondering if you could kind of summarize
[L1067] [41:53.92] maybe the the top three things that you
[L1068] [41:56.64] kind of think people should take away.
[L1069] [41:58.16] >> Yeah. So, yeah. Well, there's been a few
[L1070] [42:00.24] things. So, the story is early in my
[L1071] [42:02.72] career my f a good friend and I said,
[L1072] [42:04.40] "How can we teach grad students how to
[L1073] [42:05.84] give a good talk?" And we thought it'd
[L1074] [42:07.60] be funny to explain how to give a bad
[L1075] [42:09.76] talk and then if you didn't want to give
[L1076] [42:11.76] a bad talk, this is so this is how to do
[L1077] [42:14.16] it badly and if you don't here's the
[L1078] [42:15.76] things to do not to do it badly. And so
[L1079] [42:17.92] then I later did a how to have a bad
[L1080] [42:19.52] career that's pretty much focused
[L1081] [42:21.04] towards uh academia you know so for
[L1082] [42:23.68] researchers to be able to do that. I
[L1083] [42:25.92] later did a how to have a bad uh
[L1084] [42:30.40] how to build a bad research center, how
[L1085] [42:32.08] to build a bad research lab. And then
[L1086] [42:33.76] recently I've been giving how to give AI
[L1087] [42:36.00] a bad carbon footprint. That's my latest
[L1088] [42:37.92] one. But I think the thing that might be
[L1089] [42:40.08] more relevant is uh at the end of my
[L1090] [42:42.40] talks I would I would kind of reflect on
[L1091] [42:44.24] my career and talk about lessons
[L1092] [42:45.92] learned. So I've written a paper called
[L1093] [42:48.64] uh lesson I think it's lessons life
[L1094] [42:51.84] lessons from the first half century of
[L1095] [42:53.84] my career. I wrote that recently. And so
[L1096] [42:56.24] those those are divided up into kind of
[L1097] [42:58.72] career advice and personal advice there.
[L1098] [43:02.00] On the the personal side, I'd say uh if
[L1099] [43:05.20] you have a family, you know, make sure
[L1100] [43:06.80] your families first, keep your family
[L1101] [43:08.96] first. Um the technology we've invented
[L1102] [43:11.60] makes it really easy for your, you know,
[L1103] [43:14.24] to take your work home with you and not
[L1104] [43:16.48] pay attention to your family. Uh, I had
[L1105] [43:18.40] a when I was first here at Berkeley, I
[L1106] [43:20.96] gave a senior faculty member a ride
[L1107] [43:23.28] home, dropped him off late at night
[L1108] [43:24.96] coming up from Silicon Valley and he
[L1109] [43:26.56] said, "Well, Dave, if I had to do it
[L1110] [43:28.08] over all over again, I wish I'd spent
[L1111] [43:31.20] more time with the family." And I never
[L1112] [43:33.68] wanted to say that. And nobody on their
[L1113] [43:35.68] deathbed says, you know, I wish I'd
[L1114] [43:37.20] spent more time in the office. So, so
[L1115] [43:39.76] you got to, you know, whenever it's easy
[L1116] [43:41.36] to kind of, you know, let the let your
[L1117] [43:44.80] career overcome the needs of your
[L1118] [43:48.08] family, but you just you got to just
[L1119] [43:49.84] remember that. Uh, I would say in my
[L1120] [43:53.44] life and kind of growing up in the 50s,
[L1121] [43:56.56] you know, the idea was to be happy, you
[L1122] [43:58.56] had to be wealthy. But those are
[L1123] [44:00.24] actually two different goals, wealthy
[L1124] [44:01.52] and happiness. So, I always made
[L1125] [44:03.20] decisions towards happiness versus
[L1126] [44:05.12] wealth. You come down with it. And I
[L1127] [44:07.20] felt very good about that. Uh I and even
[L1128] [44:10.56] now like why would I pick why would I
[L1129] [44:13.52] pick something that made me wealthy and
[L1130] [44:15.12] unhappy? Why would you do that? And so
[L1131] [44:18.80] uh and in the field that we're in it
[L1132] [44:21.52] turned out there was a lot of wealth to
[L1133] [44:23.60] go with it. So you know optimizing
[L1134] [44:26.08] happiness didn't mean you had to suffer
[L1135] [44:29.36] uh beyond that. Um I think it's
[L1136] [44:32.00] important to have fun. Personally, I
[L1137] [44:34.16] think when you're a kid, you don't have
[L1138] [44:35.52] to tell kids to play, but as an adult,
[L1139] [44:37.12] you get so busy. You you don't think you
[L1140] [44:40.32] have time to have fun. Uh, but you know,
[L1141] [44:42.48] you only get to do this once. So, uh, so
[L1142] [44:45.28] I right now I play soccer, I run my
[L1143] [44:47.20] bicycle to the interview, uh, I lift
[L1144] [44:49.28] weights, I body surf, I, you know, do
[L1145] [44:51.84] things with my wife and family and my
[L1146] [44:53.68] son. So, it it's important to have fun.
[L1147] [44:56.96] I think uh on the career side is one of
[L1148] [45:01.28] the uh pieces of advice is uh by a he
[L1149] [45:06.00] wrote this book the habits of very
[L1150] [45:09.92] effective people I think and he has a
[L1151] [45:12.08] little quadrant and he divides it of
[L1152] [45:15.68] urgent and not urgent and important and
[L1153] [45:17.84] unimportant and kind of there's so many
[L1154] [45:20.96] things in our technology like email and
[L1155] [45:22.88] texting to for you to focus on the
[L1156] [45:25.36] urgent things but you really shouldn't
[L1157] [45:26.56] shouldn't be spending a lot of time on
[L1158] [45:28.56] the unimportant urgent things. And it
[L1159] [45:30.72] takes self-discipline to set aside time
[L1160] [45:33.76] for the uh important non-urgent things.
[L1161] [45:37.76] But if you don't block that out, you can
[L1162] [45:39.52] just not have time to do anything. I get
[L1163] [45:41.68] to see other people's calendars at
[L1164] [45:43.76] Google and there's managers that every
[L1165] [45:45.52] half hour from 8 to 6, five days a week
[L1166] [45:48.24] are scheduled and I don't see how you
[L1167] [45:50.64] have time to think and reflect on things
[L1168] [45:53.52] like that.
[L1169] [45:54.96] Um, other career advice things is, uh, I
[L1170] [45:59.44] remember, uh, I kind of woke up one
[L1171] [46:02.00] morning and it was like God spoke to me.
[L1172] [46:04.00] I was like thunder struck. And it says
[L1173] [46:05.84] it's not how many things you start, it's
[L1174] [46:07.52] how many things you finish.
[L1175] [46:09.68] It seems relatively obvious, but you
[L1176] [46:11.76] know, I that's not the way I was acting.
[L1177] [46:13.76] I had they had many things going on. But
[L1178] [46:16.24] after that, it was like there's one main
[L1179] [46:18.08] thing I'm doing at time. So when
[L1180] [46:19.44] Hennessy and I wrote our textbook, that
[L1181] [46:21.92] was the main thing. when I was
[L1182] [46:23.36] department here, head here, that was the
[L1183] [46:25.68] main thing I did. Uh I would do some
[L1184] [46:28.16] other little things there. And John
[L1185] [46:30.32] Hennessy, he he wrote a book too, a kind
[L1186] [46:32.64] of a a career advice book based on his
[L1187] [46:35.76] presidency. And one of the things he
[L1188] [46:37.76] said in there, you know, you're only
[L1189] [46:39.04] going to be remembered for the five or
[L1190] [46:41.04] six things you've done in your life, not
[L1191] [46:42.56] for the hundreds of little things. So to
[L1192] [46:44.96] give yourself a chance to uh have some
[L1193] [46:47.84] things you're really proud of, it's
[L1194] [46:49.92] better to concentrate on a few of them
[L1195] [46:51.92] hoping that some of them will turn out
[L1196] [46:53.44] to be a big deal rather than scatter
[L1197] [46:55.92] yourself to to um many things. But if
[L1198] [46:59.44] you're interested, you can yeah, if you
[L1199] [47:01.04] look for life lessons, David Patterson
[L1200] [47:04.40] first half century, you can see the
[L1201] [47:06.00] whole list of I think there's 16 lessons
[L1202] [47:10.16] altogether.
[L1203] [47:11.84] you mentioned that uh you you didn't
[L1204] [47:13.92] want to reflect back on your life and
[L1205] [47:15.52] feel like you didn't have enough family
[L1206] [47:17.84] time and yeah, I've I don't think I've
[L1207] [47:20.80] ever heard anyone say the opposite. Why
[L1208] [47:23.68] do you think that is? Why is it that
[L1209] [47:26.24] everyone looks back on their life and
[L1210] [47:28.08] they never regret, you know, a lot of
[L1211] [47:31.36] family time? I I imagine there's got to
[L1212] [47:34.00] be at least one person that says, "I
[L1213] [47:35.76] spent too much time with my family.
[L1214] [47:37.80] [laughter]
[L1215] [47:38.24] >> My career suffered."
[L1216] [47:39.20] >> Yeah, my career suffered.
[L1217] [47:41.28] Well, you know what's you know what's
[L1218] [47:43.04] it's it's pretty philosophical. I mean
[L1219] [47:44.88] what's what's what's life all about?
[L1220] [47:47.12] What's success? Right? You have to you
[L1221] [47:49.52] have to figure out what that means for
[L1222] [47:50.88] you. I mean if if you have uh I don't
[L1223] [47:53.52] know if you have financial goals of
[L1224] [47:56.00] being a you know a millionaire or
[L1225] [47:58.80] billionaire or something like that and
[L1226] [48:00.24] that's how you judge your life.
[L1227] [48:03.28] Okay. Good luck. You know it's pretty
[L1228] [48:06.00] hard to make it. Uh it's pretty hard to
[L1229] [48:08.40] do. Um but I think it's the you know I
[L1230] [48:12.00] when I was finishing my PhD I read this
[L1231] [48:13.92] book by studs Turkl called working where
[L1232] [48:16.56] he interviewed all these people in his
[L1233] [48:17.92] careers and they look back and what they
[L1234] [48:19.68] liked and what they didn't like what
[L1235] [48:21.04] what they felt about their careers and
[L1236] [48:22.24] what I got out of it the people who
[L1237] [48:23.84] worked with people like ministers or
[L1238] [48:25.76] teachers or doctors uh felt really good
[L1239] [48:28.88] about what they did with their careers
[L1240] [48:30.08] and the people who did more ephemeral
[L1241] [48:31.76] stuff um you know like uh you know
[L1242] [48:35.44] technology things or airplanes or
[L1243] [48:37.92] something like that are long gone didn't
[L1244] [48:39.52] feel as good about it. It was the people
[L1245] [48:40.96] that they worked with that they really
[L1246] [48:42.88] cared about. And I went out with a
[L1247] [48:45.04] retired engineering dean here and he uh
[L1248] [48:47.36] into a meeting who I knew and he said,
[L1249] [48:49.36] you know, Dave, as I flinked my ear, it
[L1250] [48:51.68] was it wasn't the projects, it was the
[L1251] [48:53.36] people that I worked at the matter and I
[L1252] [48:54.80] thought I knew that from a long time
[L1253] [48:57.36] ago. So that's I mean this is kind of
[L1254] [48:59.52] senior persons offering advice. my I
[L1255] [49:02.32] think you're going to care more about
[L1256] [49:04.32] the people you've worked with uh and the
[L1257] [49:06.48] people you've helped will be a bigger
[L1258] [49:08.40] deal. That's part of and you know one of
[L1259] [49:10.08] the other things about personal
[L1260] [49:11.20] happiness is they studied happiness.
[L1261] [49:13.12] Psychologists used to just study crazy
[L1262] [49:15.12] people but they started like why are
[L1263] [49:16.48] people happy and they know what the
[L1264] [49:18.96] reasons are you know uh have a job that
[L1265] [49:21.68] you like you know have friends and
[L1266] [49:23.84] family helping other people helping
[L1267] [49:26.08] other people makes you happy that they
[L1268] [49:27.92] they know this having something kind of
[L1269] [49:31.12] either a religious side of it doesn't
[L1270] [49:33.52] have to be a formal religion but like
[L1271] [49:35.92] contact with nature the grandeur of
[L1272] [49:37.52] nature but the the kind of the list of
[L1273] [49:39.68] things you need to do to be happy is
[L1274] [49:41.04] well understood And uh and you know
[L1275] [49:44.40] there these h and there's our world is
[L1276] [49:47.04] filled with unhappy billionaires, right?
[L1277] [49:49.36] If money was the thing that made you
[L1278] [49:51.12] happy, why are these people very wealthy
[L1279] [49:53.68] people so mad about things. So yeah,
[L1280] [49:57.76] this is me passing on advice. In one of
[L1281] [50:00.56] your talks, you had uh it said what
[L1282] [50:02.88] worked well for me and it was kind of
[L1283] [50:05.04] some reflections and one of the things
[L1284] [50:07.04] in there I thought was unique and
[L1285] [50:08.96] interesting. You mentioned that courage
[L1286] [50:12.08] was a big part of your career and I I
[L1287] [50:15.04] don't hear that too often. I was curious
[L1288] [50:16.56] why you
[L1289] [50:17.60] >> uh say courage is so important in a
[L1290] [50:19.44] career. Yeah, I I I think that's I mean
[L1291] [50:22.40] that might be partially my personal
[L1292] [50:24.96] makeup, but you know I was uh I was I
[L1293] [50:29.12] was kind of the youngest kid in my class
[L1294] [50:30.80] and kind of small. It took me a while to
[L1295] [50:33.36] grow despite age. So I was always small
[L1296] [50:36.88] but I my parents encouraged me to go out
[L1297] [50:38.96] for wrestling and uh wrestling gives you
[L1298] [50:41.92] self-con physical self-confidence
[L1299] [50:43.68] because you you know spend years doing
[L1300] [50:45.76] that. that I did in high school and
[L1301] [50:47.12] college. And so I think uh partly you
[L1302] [50:51.20] know technically
[L1303] [50:52.88] uh you know having courage to do things
[L1304] [50:54.72] it kind of goes along with the advice is
[L1305] [50:57.28] fortune favors the bold. Uh that's this
[L1306] [50:59.92] that goes that's advice is 2,000 years
[L1307] [51:02.64] old. I mean it's hard to figure this
[L1308] [51:04.88] out. U Helen Keller wrote you know e
[L1309] [51:08.08] even even trying to play it safe you
[L1310] [51:11.12] still get caught. And so it turns out
[L1311] [51:13.52] you might as well you might fail no
[L1312] [51:16.08] matter what. And if you take a big
[L1313] [51:18.88] chance if that's you can succeed if you
[L1314] [51:21.92] don't take the chance you probably won't
[L1315] [51:23.36] succeed if you play it safe. So fortune
[L1316] [51:25.52] favors the gold. And I think it takes
[L1317] [51:26.96] courage to do that. I think also it just
[L1318] [51:30.16] for me intellectually I feel like if
[L1319] [51:33.52] there's something not right I need to
[L1320] [51:35.60] stand up and confront it. And I think
[L1321] [51:37.68] that kind of ironically comes from the
[L1322] [51:39.92] wrestling side of my personality where
[L1323] [51:42.16] if I see something somebody getting
[L1324] [51:45.28] picked on or something like that, I'm
[L1325] [51:46.88] I'm going to stand and try and stop it.
[L1326] [51:48.80] And I feel that that same responsibility
[L1327] [51:51.28] intellectually if people are making bad
[L1328] [51:54.16] arguments or doing doing something that
[L1329] [51:56.48] we need to stand up and do it. And I
[L1330] [51:58.24] feel good about that. The cautionary
[L1331] [52:00.08] part about that is uh as because I guess
[L1332] [52:03.68] one of my senior faculty members saw
[L1333] [52:05.92] this nature of me. He said one of the
[L1334] [52:08.16] sayings is friends come and go but
[L1335] [52:10.40] enemies accumulate. This is an old
[L1336] [52:13.04] saying. So if you think about it you
[L1337] [52:14.48] kind of people you went to high school
[L1338] [52:15.60] with a while friends you kind of forget
[L1339] [52:17.44] but somebody who you really does dislike
[L1340] [52:19.60] you never forget that you dislike that
[L1341] [52:21.92] person. So standing up when it's
[L1342] [52:24.72] important, but be careful when you make
[L1343] [52:26.24] enemies because you know they're going
[L1344] [52:27.52] to stick around for a long time.
[L1345] [52:29.44] >> When you say something's gone bad
[L1346] [52:32.00] technically, do you mean uh someone was
[L1347] [52:34.88] incorrect?
[L1348] [52:35.68] >> Yeah. When you know when they're weak,
[L1349] [52:37.36] you know, either politically or, you
[L1350] [52:40.56] know, or or technically when it's you
[L1351] [52:43.20] it's a weak argument, right? that that I
[L1352] [52:45.68] I think give us I think I really like
[L1353] [52:48.56] there to be a marketplace of ideas and
[L1354] [52:50.56] we hone the ideas by arguing them and so
[L1355] [52:54.00] if it's a if it's a specious argument
[L1356] [52:56.40] even if a person is you know a leader of
[L1357] [52:59.36] a company and it just doesn't make sense
[L1358] [53:01.12] I feel it's kind of the responsibil it's
[L1359] [53:04.08] better for the company if somebody
[L1360] [53:05.68] stands up and points that out than to
[L1361] [53:08.16] just let them get away with it and then
[L1362] [53:10.72] um and then and you know it's a little
[L1363] [53:13.92] bit confrontational
[L1364] [53:15.12] But, you know, as long as people all
[L1365] [53:17.28] agree that, you know, this is for the
[L1366] [53:18.88] greater good, we're going to we we need
[L1367] [53:20.64] to get the right ideas out there. And
[L1368] [53:22.56] so, let's argue about the ideas to to
