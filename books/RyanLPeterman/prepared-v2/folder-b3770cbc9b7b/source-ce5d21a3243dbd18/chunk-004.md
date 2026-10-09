Chunk 4; segments 965–1289. Start may repeat the previous chunk for context.

# Boris Cherny (Creator of Claude Code) On What Grew His Career And Building at Anthropic

Source ID: source-ce5d21a3243dbd18
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Boris_Cherny_(Creator_of_Claude_Code)_On_What_Grew_His_Career_And_Building_at_Anthropic_en.txt
Video: https://www.youtube.com/watch?v=AmdLVWMdjOk

[L974] [32:12.88] layer integrity systems ad systems
[L975] [32:14.80] there's just all sorts of stuff that has
[L976] [32:16.64] to get merged and at the time Ysef
[L977] [32:18.96] Carver uh he just joined I think he came
[L978] [32:21.52] from either profile or events like a
[L979] [32:23.92] different or that that joined forces
[L980] [32:25.60] with groups to make this happen and he
[L981] [32:28.16] was working on it but he was kind of
[L982] [32:29.20] struggling with a with a decision at the
[L983] [32:30.80] time and I think he was even more senior
[L984] [32:32.16] than I was but he just like wasn't
[L985] [32:33.92] making the decision on the data model
[L986] [32:35.92] and so I just took a bunch of people and
[L987] [32:37.92] I was like all right the tech leads
[L988] [32:39.68] across the entire org we're going to
[L989] [32:41.92] spend the next like 3 hours on this day
[L990] [32:44.16] and we're going to do this like
[L991] [32:45.68] essentially like game where we get to do
[L992] [32:47.92] architecture and so I split everyone up
[L993] [32:50.08] into two teams I think it was like blue
[L994] [32:51.52] team and green team or I I forget what
[L995] [32:53.20] these were. And we gave everyone this
[L996] [32:55.36] like this problem of like how do you
[L997] [32:56.56] merge these data models? Here are the
[L998] [32:58.00] requirements. And then everyone had 3
[L999] [33:00.00] hours in a whiteboard and they had to
[L1000] [33:01.20] come up with a design. And what was cool
[L1001] [33:03.68] is that going into it, we had no idea
[L1002] [33:06.40] how we would do this because it just
[L1003] [33:07.84] seemed too crazy of a problem. But the
[L1004] [33:10.32] going out of it, we had two designs that
[L1005] [33:12.48] were 80% the same. And so it was really
[L1006] [33:15.52] obvious what we could execute on. And
[L1007] [33:16.88] then the 20% where the differences were,
[L1008] [33:18.72] it was very obvious where the risk was.
[L1009] [33:20.64] And so we could kind of front front
[L1010] [33:22.24] frontload a little bit of that risk with
[L1011] [33:23.76] a little bit of technical spikes. Um but
[L1012] [33:25.68] also we can just start execution right
[L1013] [33:27.20] away because we knew exactly what we had
[L1014] [33:28.64] to do.
[L1015] [33:29.92] >> Yeah, that was really interesting when I
[L1016] [33:31.52] saw that it was like a technical design
[L1017] [33:34.40] competition with all the senior
[L1018] [33:36.24] engineers and you just put people in
[L1019] [33:38.88] separate rooms to come up with um I've
[L1020] [33:42.24] never heard anything like that. When you
[L1021] [33:43.76] proposed that idea for this design
[L1022] [33:45.68] competition within the org, were people
[L1023] [33:48.48] excited about it or was it like kind of
[L1024] [33:50.32] a crazy idea?
[L1025] [33:51.60] >> Yeah, it was sort of crazy. I mean, with
[L1026] [33:52.88] this sort of thing, you just have to
[L1027] [33:53.92] kind of do it. So, I just I just kind of
[L1028] [33:55.68] told everyone, "Hey, we're doing this."
[L1029] [33:56.88] And then I just put it on everyone's
[L1030] [33:58.64] calendar and um it just seems fun, you
[L1031] [34:01.20] know? So, like as an engineer, you would
[L1032] [34:02.56] want to do it. But I think this is the
[L1033] [34:04.32] sort of thing where like sometimes you
[L1034] [34:05.60] need consensus and sometimes you just
[L1035] [34:07.12] have to act. And in this case, because
[L1036] [34:09.28] the path was unclear, it was important
[L1037] [34:10.88] to act. But at the same time, I didn't
[L1038] [34:13.20] know how to proceed. So, we had to kind
[L1039] [34:15.04] of get everyone together to build
[L1040] [34:16.40] consensus. And so, I think it's like as
[L1041] [34:18.32] a leader, you're kind of always juggling
[L1042] [34:19.60] these kind of two things.
[L1043] [34:20.80] >> After that experience, just giving being
[L1044] [34:23.12] given hundreds of engineers and scoping
[L1045] [34:25.44] things out, do you have any tips for
[L1046] [34:28.00] someone who's like a tech lead who's
[L1047] [34:30.00] needs to do quick, you know, scoping?
[L1048] [34:32.08] Anything that worked well for you? I
[L1049] [34:34.48] think the biggest thing I think the
[L1050] [34:36.08] biggest foe that I've seen is people
[L1051] [34:37.52] just taking too long and getting too
[L1052] [34:38.88] into the weeds. there's always an
[L1053] [34:40.48] infinite number of details. Just start
[L1054] [34:42.64] with a high level. You know, most
[L1055] [34:44.16] technical scoping you can do within like
[L1056] [34:45.76] 30 minutes very very roughly. Um and if
[L1057] [34:49.12] you don't know the systems like nowadays
[L1058] [34:50.56] you would just use quad code run in the
[L1059] [34:52.40] codebase and just ask it to like you
[L1060] [34:54.24] know like what are all the systems
[L1061] [34:55.28] involved? They can actually just do this
[L1062] [34:56.48] for you. And this is another just
[L1063] [34:58.56] totally insane change. You know I when I
[L1064] [35:01.60] was doing this stuff I never would have
[L1065] [35:02.80] expected that AI could do this for me
[L1066] [35:04.96] now. Um but now it does. in the past. I
[L1067] [35:09.68] think that would have been my biggest
[L1068] [35:10.96] advice though is uh just time box it.
[L1069] [35:14.24] Spend maybe 30 minutes, maybe like
[L1070] [35:15.92] couple hours max. If you have to like
[L1071] [35:17.52] dig through code and stuff, um
[L1072] [35:19.52] definitely reach out to experts and just
[L1073] [35:22.24] make a list of experts. Talk to all of
[L1074] [35:23.68] them. Run the design by them. Don't just
[L1075] [35:25.76] ask them for input. Give them a straw
[L1076] [35:27.36] man cuz then they can actually like give
[L1077] [35:28.88] you feedback on it and it's something to
[L1078] [35:30.64] go off of. Continuing with your career
[L1079] [35:32.96] story, I think the thing that got you
[L1080] [35:35.04] promoted to senior staff or IC7 was um
[L1081] [35:38.80] public groups on Facebook. So I'm
[L1082] [35:41.28] curious like the story behind your
[L1083] [35:42.88] involvement in that and you know
[L1084] [35:44.88] anything interesting that happened at
[L1085] [35:46.32] that point. Yeah. So public groups was
[L1086] [35:48.40] one of these projects that came out of
[L1087] [35:49.76] this uh the scoping for um you know like
[L1088] [35:52.24] making Facebook groups more about
[L1089] [35:53.52] communities. There's this like one very
[L1090] [35:55.60] narrow change that we wanted to make
[L1091] [35:56.88] that seems so simple on the surface, but
[L1092] [35:58.72] it was so complex under it. And it's
[L1093] [36:00.80] just funny like explaining this to
[L1094] [36:02.08] anyone that wasn't there. They're like,
[L1095] [36:03.28] "Wait, this is like a oneline change."
[L1096] [36:04.48] And I'm like, "No, it's not." It's like
[L1097] [36:06.08] it was very difficult to pull it off.
[L1098] [36:08.32] And so the change was in order to
[L1099] [36:10.80] participate in a public Facebook group,
[L1100] [36:12.64] you no longer have to join first.
[L1101] [36:14.72] >> So you're saying um you can just view
[L1102] [36:18.16] like you have read access for all all
[L1103] [36:20.40] groups essentially or public groups?
[L1104] [36:21.92] read access for all groups and for some
[L1105] [36:23.52] groups even comment access. So you can
[L1106] [36:25.20] comment without joining first.
[L1107] [36:27.44] >> Interesting.
[L1108] [36:28.16] >> And this is the thing you know it feels
[L1109] [36:29.60] like a oneline change and it actually
[L1110] [36:31.04] was a oneline change but there's all
[L1111] [36:33.20] these downstream implications that were
[L1112] [36:35.04] so tricky. So one is um you know in the
[L1113] [36:38.16] data model there's essentially a field
[L1114] [36:39.52] in the database that was like group
[L1115] [36:40.80] member and we had this like really
[L1116] [36:43.20] intense technical debate about like
[L1117] [36:45.20] these people that are commenting in a
[L1118] [36:46.80] group are they group members and the
[L1119] [36:49.68] model also changed where before to join
[L1120] [36:52.56] a Facebook group an admin had to approve
[L1121] [36:55.20] you so there's kind of a vote of
[L1122] [36:57.20] confidence that you can be in this group
[L1123] [36:59.12] and then after we switched to this model
[L1124] [37:00.72] where to join a public Facebook group
[L1125] [37:02.40] you just you just essentially press like
[L1126] [37:03.76] follow and we actually went back and
[L1127] [37:05.36] forth should it be join or follow like
[L1128] [37:06.72] what's the right verb to describe this
[L1129] [37:08.40] but it was essentially follow cuz
[L1130] [37:09.76] there's no reciprocal action you know if
[L1131] [37:12.00] you follow a group are you a member like
[L1132] [37:14.64] should you be stored in that same part
[L1133] [37:16.72] of the database and we we just went back
[L1134] [37:19.12] and forth on this for a while and I
[L1135] [37:20.96] remember at the time there was this like
[L1136] [37:22.00] really senior engineer Bob he was kind
[L1137] [37:24.16] of the most senior engineer in the in
[L1138] [37:25.68] the or at the time and he felt very
[L1139] [37:27.68] strongly that it should not be the same
[L1140] [37:29.36] thing and he kind of pushed us pretty
[L1141] [37:30.88] hard um even though it would be a ton of
[L1142] [37:33.28] engineering work to migrate stuff to
[L1143] [37:35.36] make at a different thing. And so we did
[L1144] [37:37.60] this work um because he was actually one
[L1145] [37:39.36] of the early engineers on Facebook
[L1146] [37:40.56] group. So he knew it really well. Um and
[L1147] [37:42.88] he felt pretty strongly. There's a bunch
[L1148] [37:45.04] of these other like downstream changes
[L1149] [37:46.32] around uh like moderation and different
[L1150] [37:48.32] new like admin tooling that admins would
[L1151] [37:50.16] need to handle kind of the influx of
[L1152] [37:52.24] spam and things like this. And I
[L1153] [37:54.64] remember at the time thinking like if
[L1154] [37:56.00] anyone can make a comment, the comments
[L1155] [37:57.52] are just going to be like filled up with
[L1156] [37:58.96] spam. And I had to hard I had a hard
[L1157] [38:01.28] time kind of convincing people of this.
[L1158] [38:02.96] And so at some point I built this like
[L1159] [38:04.24] Monte Carlo like visualization of how
[L1160] [38:06.24] this would work. And it was just like
[L1161] [38:08.16] this like really simple kind of like
[L1162] [38:09.44] scratch pad of you know like a comment
[L1163] [38:11.36] comes in there's a certain probability
[L1164] [38:12.56] of it being good or bad and then like
[L1165] [38:14.48] what actually happens to comments. And I
[L1166] [38:16.72] think that actually did a pretty good
[L1167] [38:18.00] job of convincing the integrity teams to
[L1168] [38:20.00] jump in and help with this. And so at
[L1169] [38:21.84] the time the pages integrity team jumped
[L1170] [38:23.84] in and they helped with a comment
[L1171] [38:25.12] ranking because kind of ranking spam
[L1172] [38:27.20] comments lower was the main technical
[L1173] [38:29.44] mechanism to make it so people don't see
[L1174] [38:31.28] these comments. So there's a bunch of
[L1175] [38:33.28] these like pretty gnarly downstream
[L1176] [38:34.56] implications of uh letting people
[L1177] [38:36.72] participate. There's also this data
[L1178] [38:38.00] model migration that we're doing. And so
[L1179] [38:40.40] to do all this, we had to staff a big
[L1180] [38:42.08] team to um to kind of make this happen.
[L1181] [38:44.24] And so we hired a new director, Yammen,
[L1182] [38:46.48] who um hired a bunch of engineers.
[L1183] [38:49.04] There's a bunch of internal transfers.
[L1184] [38:50.32] So some of the most senior engineers
[L1185] [38:51.68] from the org like uh there was like
[L1186] [38:53.68] Henry Henry Long uh Joe Cham there was
[L1187] [38:57.04] like a few other engineers and they were
[L1188] [38:59.28] all working on this and I was the same
[L1189] [39:01.76] level as them. I was like a you know an
[L1190] [39:03.76] IC6 at the time and so were they and I
[L1191] [39:07.20] remember just feeling this kind of
[L1192] [39:08.40] imposter syndrome of having to kind of
[L1193] [39:11.20] direct them and kind of point them at
[L1194] [39:12.80] work knowing kind of in my mind that
[L1195] [39:15.60] we're the same level even though levels
[L1196] [39:17.12] are hidden. you kind of you know you
[L1197] [39:18.64] know through like rumors and stuff who's
[L1198] [39:20.24] what you know in hindsight I think this
[L1199] [39:22.48] is sort of like misplaced imposttor
[L1200] [39:24.64] syndrome because levels don't matter at
[L1201] [39:27.12] all this is my current view and you know
[L1202] [39:29.28] some people that are very junior can
[L1203] [39:31.52] shoot way higher than that and just give
[L1204] [39:33.20] you amazing results some people that are
[L1205] [39:35.44] very senior can give you terrible
[L1206] [39:36.80] results and so the level actually
[L1207] [39:38.64] doesn't matter that much but at the time
[L1208] [39:41.36] I remember just like really thinking
[L1209] [39:42.80] about this and it it was just kind of
[L1210] [39:44.88] hard to step into this role
[L1211] [39:47.60] And eventually I did it. And it's funny,
[L1212] [39:50.32] eventually the thing that got me the
[L1213] [39:51.84] promo to IC7
[L1214] [39:54.16] was reversing this decision that Bob did
[L1215] [39:56.88] cuz he wanted to do this big migration.
[L1216] [39:58.80] And we did it. And it was just like,
[L1217] [40:00.96] dude, it was so much work. It was like
[L1218] [40:02.24] it was like 6 months or a year of work
[L1219] [40:03.76] or something just migrating just
[L1220] [40:05.60] hundreds and hundreds and hundreds of
[L1221] [40:06.96] call sites to to do this correctly. And
[L1222] [40:09.84] then technically I felt like actually
[L1223] [40:12.24] what we did is we essentially just added
[L1224] [40:13.84] an if else at every single one of these
[L1225] [40:15.44] call sites in the process. We audited
[L1226] [40:17.84] all the call sites. So we kind of knew
[L1227] [40:19.04] that it was safe but uh we didn't
[L1228] [40:21.68] actually change the logic. And so
[L1229] [40:22.88] actually what we learned is that yes
[L1230] [40:24.80] member is the right field to model both
[L1231] [40:26.72] followers and group members. This was
[L1232] [40:28.32] the right decision. And so I pushed the
[L1233] [40:31.12] same engineer that did this to then undo
[L1234] [40:32.80] it. it was the right thing to push this
[L1235] [40:35.20] engineer because it showed maturity on
[L1236] [40:37.28] his part that he said yes and was able
[L1237] [40:38.96] to do it. He also had the most context
[L1238] [40:40.96] technically so he could do it the best.
[L1239] [40:43.20] And I think for Bob it made he he felt
[L1240] [40:47.20] better about me as a technical leader
[L1241] [40:49.28] because he knew that I was wishing I was
[L1242] [40:51.44] willing to pull back to to push back on
[L1243] [40:54.80] um decisions that even senior folks
[L1244] [40:57.84] make. Um and in the end this was the
[L1245] [41:00.08] right thing. So we reversed the
[L1246] [41:01.20] migration. It also took a long time to
[L1247] [41:02.88] do it, but in the end it made it so
[L1248] [41:05.12] everyone building on this info could do
[L1249] [41:06.64] it and everyone wasn't always constantly
[L1250] [41:09.28] bumping into this like should I use this
[L1251] [41:10.96] field or or this field.
[L1252] [41:13.20] >> Yeah, I'm curious about that part cuz
[L1253] [41:15.28] you had a strong technical disagreement
[L1254] [41:17.92] with Bob or senior TL. Um, but the
[L1255] [41:21.76] outcome at the end is actually it seems
[L1256] [41:23.68] like it strengthened the relationship.
[L1257] [41:25.36] He was a champion for you in your your
[L1258] [41:28.16] promotion. So, I'm curious, how would
[L1259] [41:30.72] you recommend going about strong
[L1260] [41:32.88] technical disagreement in a way that
[L1261] [41:34.72] doesn't hurt the relationship?
[L1262] [41:37.12] >> I think the biggest thing is you have to
[L1263] [41:38.48] earn it. Yeah. You just have to earn
[L1264] [41:40.80] trust and it could be as simple as, you
[L1265] [41:43.92] know, like what I did at the beginning,
[L1266] [41:45.20] which is just disagreeing and committing
[L1267] [41:47.12] and showing that I'm willing to do that
[L1268] [41:48.80] and I'm willing to just execute if
[L1269] [41:50.88] someone else thinks it's a good idea and
[L1270] [41:52.16] I kind of look up to them.
[L1271] [41:54.56] But also you have to kind of show that
[L1272] [41:56.72] you have good technical judgment. Um but
[L1273] [41:59.52] you can't really do that until you earn
[L1274] [42:00.96] trust. So take the time to get that
[L1275] [42:02.56] trust first.
[L1276] [42:03.36] >> And then on the imposttor syndrome, um
[L1277] [42:05.36] leading those engineers that were also
[L1278] [42:07.76] very strong. Um do you have any advice
[L1279] [42:10.32] for overcoming imposter syndrome?
[L1280] [42:12.80] >> Yeah, just don't overthink it. You know,
[L1281] [42:14.80] no one really knows what they're doing,
[L1282] [42:16.80] you know, at any level. No one really
[L1283] [42:18.32] knows. We're all just trying to figure
[L1284] [42:19.76] it out.
[L1285] [42:20.16] >> That's easier said than done. Was there
[L1286] [42:22.72] like a an aha moment where you realize
[L1287] [42:25.68] actually maybe I do got this or this
[L1288] [42:28.24] isn't that big of a deal? You know, I
[L1289] [42:30.56] don't I don't think so really. There
[L1290] [42:31.76] wasn't a single moment. It just it kind
[L1291] [42:33.36] of goes away over time. And I think at
[L1292] [42:35.76] every at every level, it doesn't matter
[L1293] [42:37.52] what level you're at, you should always
[L1294] [42:38.88] feel a little bit of imposter syndrome
[L1295] [42:40.88] cuz if you don't, then you're not
[L1296] [42:42.16] pushing yourself hard enough.
[L1297] [42:43.92] >> At this point in your career, you were
[L1298] [42:46.00] like more and more of a tech lead and
