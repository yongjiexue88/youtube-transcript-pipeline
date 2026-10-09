Chunk 3; segments 762–1151. Start may repeat the previous chunk for context.

# AWS Distinguished Eng: Learning From 3000 Incidents And How Engineering Is Changing | Marc Brooker

Source ID: source-45044ebe79206044
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/AWS_Distinguished_Eng_Learning_From_3000_Incidents_And_How_Engineering_Is_Changing_Marc_Brooker_en.txt
Video: https://www.youtube.com/watch?v=u3GjIXP9N0s

[L771] [27:51.60] you know, use a scalable back end, you
[L772] [27:53.80] know,
[L773] [27:54.72] or Dynamo DB or whatever your favorite
[L774] [27:56.84] scalable database is,
[L775] [27:58.88] and keep your database vendor honest
[L776] [28:01.16] about getting to the the scale and
[L777] [28:03.04] performance you need, rather than
[L778] [28:04.44] putting a cache in front of things.
[L779] [28:06.52] So, caching isn't a bad pattern, but it
[L780] [28:08.60] is a pattern with some
[L781] [28:11.16] significant downsides that are, you
[L782] [28:13.32] know, really
[L783] [28:14.88] uh best avoided.
[L784] [28:17.00] In practice, how how often do you see
[L785] [28:19.68] that metastable failure, though? Yeah,
[L786] [28:22.76] you know, this is uh it's not it's not
[L787] [28:24.88] super common, right? Like, you might go
[L788] [28:26.32] years without seeing, you know,
[L789] [28:28.04] something like that. But, if you look
[L790] [28:29.56] across
[L791] [28:31.48] the biggest, most impactful,
[L792] [28:34.36] uh you know, system postmortems across
[L793] [28:36.04] the industry, I would say that these
[L794] [28:38.04] kinds of metastable failures have been
[L795] [28:41.40] an underlying cause in probably a
[L796] [28:44.12] majority of them. And
[L797] [28:47.16] it's super important that, you know, as
[L798] [28:48.88] an industry and as a community of
[L799] [28:50.36] practice, we understand those things
[L800] [28:51.96] deeply because
[L801] [28:53.84] the also those cases where these do
[L802] [28:56.48] happen,
[L803] [28:57.84] you know, tend to be larger-scale
[L804] [29:00.88] issues, longer recovery-time issues, and
[L805] [29:04.48] and and more complex-to-fix issues,
[L806] [29:06.68] right? Where you have to often, you
[L807] [29:09.00] know, turn it off and turn it back on
[L808] [29:10.40] again, which is this very very painful
[L809] [29:12.96] thing for a a a team or an organization
[L810] [29:15.60] to do.
[L811] [29:16.88] Um
[L812] [29:18.20] and you know, and so again, like you you
[L813] [29:20.36] might go years operating a system with
[L814] [29:22.08] seeing nothing like this. And and but if
[L815] [29:24.80] you look at the most impactful issues,
[L816] [29:27.72] it's actually fairly common as an
[L817] [29:30.04] underlying cause for those issues. And
[L818] [29:31.76] so, you know, it's kind of both of these
[L819] [29:33.44] things of being quite uncommon and being
[L820] [29:35.68] being rather common.
[L821] [29:37.20] I was reading your blog and you have a
[L822] [29:39.40] series of posts on how AI may impact the
[L823] [29:43.40] future of software engineering. And I
[L824] [29:44.80] kind of want to pick your brain on that.
[L825] [29:46.60] So, what's your perspective on how you
[L826] [29:49.36] think AI will uh impact software
[L827] [29:52.20] engineering and how it'll change things?
[L828] [29:54.48] Yeah, I mean, it's, you know, hard maybe
[L829] [29:56.44] harder than ever to tell the future. And
[L830] [29:58.36] so, you know, this is a a set of uh
[L831] [30:00.80] maybe guesses uh and and and predictions
[L832] [30:03.44] about about the future. Um
[L833] [30:06.24] So, I'll I'll say the first thing I I,
[L834] [30:08.08] you know, I deeply believe about
[L835] [30:09.64] software is
[L836] [30:12.12] we have only just started to see the
[L837] [30:16.12] impact that software is going to have on
[L838] [30:17.96] the world. There is such an opportunity
[L839] [30:21.16] for
[L840] [30:22.44] more software to exist, bigger software,
[L841] [30:25.16] better software, more personal software.
[L842] [30:28.00] You know, all of these things. And so,
[L843] [30:29.40] software has, throughout its well, its
[L844] [30:32.32] 60-ish-year history, been
[L845] [30:35.52] supply constrained.
[L846] [30:37.84] And, you know, I think that's going to
[L847] [30:39.48] remain true. I think the opportunity for
[L848] [30:42.48] for software in the world is is just,
[L849] [30:44.76] you know, almost almost unbounded.
[L850] [30:47.76] Um and that's really exciting, right?
[L851] [30:49.40] It's really exciting to be at a moment
[L852] [30:51.36] when
[L853] [30:52.44] the economics of building software are
[L854] [30:54.60] changing and and are changing rather
[L855] [30:56.60] quickly.
[L856] [30:57.84] Um and that gives us an opportunity to
[L857] [31:00.72] think about what could we do in the
[L858] [31:02.96] world with a lot more software?
[L859] [31:05.36] Um you know, a lot more
[L860] [31:08.12] software personalization, a lot more
[L861] [31:11.48] just the right software in the right
[L862] [31:13.16] place at the right time.
[L863] [31:15.72] And
[L864] [31:17.72] you know, that gives me a huge amount
[L865] [31:19.52] of, uh, you know, excitement about the
[L866] [31:21.24] future of of this industry,
[L867] [31:23.76] uh, because, you know, we we have a
[L868] [31:26.48] massive opportunity ahead of us, both
[L869] [31:29.16] driven by these changing economics of
[L870] [31:32.48] software development.
[L871] [31:34.76] Um
[L872] [31:35.72] now, also with those changes, there are
[L873] [31:37.84] going to be needs for, you know, us as
[L874] [31:40.64] software practitioners, people who build
[L875] [31:42.36] software, people who who love software
[L876] [31:44.36] to to adapt. And, uh, you know,
[L877] [31:48.56] that that means that that software
[L878] [31:50.28] careers are going to look different. Um
[L879] [31:53.16] uh, they're going to look different
[L880] [31:54.32] early on, they're going to look
[L881] [31:55.36] different later on. I think the software
[L882] [31:57.68] business is going to look different. And
[L883] [32:01.08] the
[L884] [32:02.48] um
[L885] [32:03.56] success of people and organizations over
[L886] [32:05.80] the next, uh,
[L887] [32:07.12] you know, next who knows, 5 years,
[L888] [32:09.92] decade, is going to be largely
[L889] [32:12.12] predicated on their ability to adapt to
[L890] [32:15.08] that change and and to lead that change.
[L891] [32:18.16] You told the story about this guy who
[L892] [32:19.96] bet on analog circuits when, obviously,
[L893] [32:23.20] we know digital became kind of the more
[L894] [32:25.92] more dominant way.
[L895] [32:27.72] Yet, he made he made good money. For the
[L896] [32:29.68] people who maybe don't want to adapt,
[L897] [32:32.44] you could still get by and succeed. It's
[L898] [32:35.76] not going to be like a crazy thing. Is
[L899] [32:38.32] that is that kind of the takeaway and
[L900] [32:40.40] why you brought up that story? Yeah, I I
[L901] [32:42.16] I I I
[L902] [32:42.88] I think that's that's the right
[L903] [32:44.08] takeaway. And so if I sort of break
[L904] [32:45.76] down, you know,
[L905] [32:47.40] the the the world into to three tiers, I
[L906] [32:50.72] you know, I think there's going to
[L907] [32:51.80] remain a huge amount of joy in the craft
[L908] [32:55.72] of software. Um,
[L909] [32:57.52] you know, like the craft of of joinery
[L910] [32:59.48] with, you know, with handsaws, right?
[L911] [33:01.16] Like it's it's a nice way to spend time.
[L912] [33:04.12] It's not a particularly economically
[L913] [33:06.52] interesting activity anymore, but not
[L914] [33:09.16] everything we do has to be an
[L915] [33:10.40] economically interesting opportunity. It
[L916] [33:12.12] can just be something I do because I
[L917] [33:14.28] enjoy it, because I enjoy the product of
[L918] [33:16.24] it, because I enjoy talking to people
[L919] [33:17.96] about it, right? And so there is, you
[L920] [33:20.12] know, I I I don't think that is going to
[L921] [33:21.72] go away. I think we're going to see,
[L922] [33:24.12] you know, a lot of interest in in that.
[L923] [33:25.72] Like there's been interest in in
[L924] [33:26.88] retrocomputing and, you know, people who
[L925] [33:28.96] run an Apple II as their desktop. And
[L926] [33:30.72] like, well, again, it's wildly
[L927] [33:33.56] impractical. It's not economically
[L928] [33:35.20] interesting, but it's fun and something
[L929] [33:36.60] I, you know, could do as a hobby. And
[L930] [33:38.36] so, you know, that's that's going to be
[L931] [33:40.84] a remaining part of of of the world of
[L932] [33:43.28] software for probably forever.
[L933] [33:46.16] Um, and then there's this this, you
[L934] [33:48.32] know,
[L935] [33:49.28] kind of story that that I told in the
[L936] [33:50.88] blog post.
[L937] [33:52.60] And I think this relates to,
[L938] [33:56.08] you know,
[L939] [33:56.76] driving change in the real world it's
[L940] [33:58.56] always harder than it looks from the
[L941] [34:00.20] outside, right? Like as you get into the
[L942] [34:01.92] details things become more difficult.
[L943] [34:04.76] They become more dependent on people.
[L944] [34:06.52] They become more dependent on politics
[L945] [34:08.36] and policy and um,
[L946] [34:10.80] you know, our our various
[L947] [34:11.84] irrationalities as humans. And And so
[L948] [34:14.44] driven by that,
[L949] [34:16.92] you know, there is going to be a
[L950] [34:19.64] huge amount of and a shrinking over time
[L951] [34:23.04] amount, but it but a huge amount of the
[L952] [34:25.92] software industry that is run
[L953] [34:28.60] in what I might call the old way, right?
[L954] [34:31.68] Past techniques, past languages, past
[L955] [34:34.88] technologies.
[L956] [34:36.40] And there's real economic opportunity in
[L957] [34:40.00] engaging with that part of the, you
[L958] [34:42.00] know, part of the world. Um you know, as
[L959] [34:44.48] we saw with with analog electronics,
[L960] [34:46.68] analog electronics will very much exist.
[L961] [34:48.68] In fact, there are
[L962] [34:50.48] parts of the world like, you know, like
[L963] [34:52.64] radio and power systems where there's
[L964] [34:54.60] been incredible technology technological
[L965] [34:56.76] advancement in in in those fields.
[L966] [34:59.44] Uh but they have become more niche, and
[L967] [35:01.12] so, you know, digital became the
[L968] [35:02.56] mainstream. We wouldn't be talking like
[L969] [35:04.40] we are today
[L970] [35:05.92] if it wasn't for this uh you know, 12
[L971] [35:09.84] orders of magnitude or whatever
[L972] [35:11.16] explosion in in digital transistor
[L973] [35:13.04] counts.
[L974] [35:14.88] Um
[L975] [35:17.36] but there's interesting opportunity
[L976] [35:18.76] there, and I think that interesting
[L977] [35:19.92] opportunity is going to change shape and
[L978] [35:22.28] and and become more and more specialized
[L979] [35:24.48] and and and more and more niche and and
[L980] [35:26.48] great careers to be built there.
[L981] [35:28.44] Um and then there is the mainstream,
[L982] [35:30.28] which I think is going to adopt these
[L983] [35:33.04] new technologies from agentic
[L984] [35:34.80] development to AI-powered development
[L985] [35:37.16] to, you know, specification-driven
[L986] [35:39.36] development um and, you know, a whole
[L987] [35:41.92] lot of other, you know, new things whose
[L988] [35:44.08] names we don't even know yet
[L989] [35:46.64] um
[L990] [35:47.68] to build software at a speed and a cost
[L991] [35:52.72] that is unimaginable to do with with old
[L992] [35:56.08] techniques.
[L993] [35:57.80] And I think that is where correctly the
[L994] [36:01.36] majority of the industry is going to be
[L995] [36:03.04] going. I think that's where the majority
[L996] [36:04.76] of careers are going to be built. I
[L997] [36:06.72] think that's where the majority of um
[L998] [36:08.96] economic opportunity is. It's the space
[L999] [36:11.60] I'd be in if I was building a company
[L1000] [36:13.40] today. It's the space I'm in in my role.
[L1001] [36:16.16] Um and you know, the one I would sort of
[L1002] [36:18.36] personally be most excited about.
[L1003] [36:21.12] But yeah, it isn't only one. I think
[L1004] [36:22.68] there's going to be the spectrum of
[L1005] [36:24.16] software practice, and especially where
[L1006] [36:26.52] software engages with the physical
[L1007] [36:28.32] world, uh there are going to be some
[L1008] [36:30.52] really interesting
[L1009] [36:33.48] questions about how do we bring these
[L1010] [36:35.64] new technologies, how do we bring these
[L1011] [36:37.28] new practices into
[L1012] [36:41.24] the various many niches that software is
[L1013] [36:43.48] going to and has, you know, over over
[L1014] [36:45.44] six decades kind of wormed its way into.
[L1015] [36:49.52] It's interesting you mentioned joinery.
[L1016] [36:51.64] I wonder if
[L1017] [36:53.92] down the road
[L1018] [36:55.40] we'll see apps on the app store that
[L1019] [36:56.80] people pay extra for because it's
[L1020] [36:59.44] marketed as this was written by a human
[L1021] [37:02.28] or it's it was written by hand. It's a
[L1022] [37:04.36] bespoke
[L1023] [37:06.04] you know, custom app.
[L1024] [37:08.60] Crazy how the world's going to change.
[L1025] [37:10.16] But so it sounds like you know, change
[L1026] [37:11.88] is obviously the the common case. It's
[L1027] [37:13.80] the one that we should be thinking
[L1028] [37:14.88] about. Maybe we can break up the
[L1029] [37:16.68] conversation into parts. One is for
[L1030] [37:19.20] junior engineers.
[L1031] [37:20.92] What is important given that code is
[L1032] [37:24.88] kind of flowing like water now?
[L1033] [37:27.24] At risk of being a bit meta about our
[L1034] [37:28.80] past conversation, it really is about
[L1035] [37:30.56] finding those problems that matter and
[L1036] [37:32.28] and and doing that early in in a career.
[L1037] [37:35.04] And
[L1038] [37:36.48] you know, that requires an understanding
[L1039] [37:39.52] of customers. It requires an
[L1040] [37:41.00] understanding of the business. It
[L1041] [37:42.32] requires an understanding of of
[L1042] [37:43.96] economics and and and of systems.
[L1043] [37:46.84] And
[L1044] [37:48.84] that can I think that's going to move
[L1045] [37:52.48] from being
[L1046] [37:54.12] you know, almost kind of senior engineer
[L1047] [37:56.12] work of like oh, well, you know, now
[L1048] [37:57.84] you're going to go and talk to customers
[L1049] [37:59.12] and actually understand the context of
[L1050] [38:00.72] the stuff you're building
[L1051] [38:02.52] to being more and more part of
[L1052] [38:06.00] even the earliest steps of an
[L1053] [38:08.12] engineering career. Right? Like here's
[L1054] [38:10.08] the context. Here's the problem. Here's
[L1055] [38:11.88] the customer. Let's go off and work
[L1056] [38:13.40] together and solve
[L1057] [38:15.04] you know, and and and and solve this
[L1058] [38:16.52] problem with all of this context.
[L1059] [38:19.92] And
[L1060] [38:21.76] I think that's going to be
[L1061] [38:25.40] super exciting for one set of folks,
[L1062] [38:28.68] uh, and a little bit frustrating for
[L1063] [38:30.20] people who have come into um,
[L1064] [38:34.92] you know, looking for a pure software
[L1065] [38:36.40] development career, right? Looking for a
[L1066] [38:38.20] career where they sit down, open their
[L1067] [38:40.32] IDE,
[L1068] [38:42.32] start typing and and don't stop for
[L1069] [38:44.28] eight hours. I think that's going to be
[L1070] [38:46.12] a mode that we're going to see fewer
[L1071] [38:48.20] people in and a mode that's going to be
[L1072] [38:50.44] harder and harder to build a career
[L1073] [38:52.64] around. Now, the other mode of, "Oh, I'm
[L1074] [38:55.08] excited to go off and learn from my
[L1075] [38:56.72] customers about what they're building
[L1076] [38:58.12] and what they need." I think that's
[L1077] [38:59.96] going to be ever more highly, you know,
[L1078] [39:01.80] highly valuable. And so, super exciting
[L1079] [39:04.44] opportunity to build,
[L1080] [39:06.44] you know, build careers there.
[L1081] [39:08.72] And then maybe and and this might come
[L1082] [39:10.36] across as being a little bit, um, you
[L1083] [39:12.60] know, paradoxical. I think there's also
[L1084] [39:14.36] a ton of opportunity for, you know,
[L1085] [39:16.80] folks who are extremely technically
[L1086] [39:18.76] deep, um, you know, who are, uh,
[L1087] [39:22.60] you know, deep on optimization problems
[L1088] [39:25.56] or deep on infrastructure problems or
[L1089] [39:28.68] deep on, you know, various scientific
[L1090] [39:31.00] things or deep on databases or deep on,
[L1091] [39:34.40] you know, one of the many, many topics
[L1092] [39:36.40] that are all behind our industry.
[L1093] [39:39.32] Because I think the ability to
[L1094] [39:42.96] ans- ask the right questions is also
[L1095] [39:46.08] much more valuable than it was has ever
[L1096] [39:48.56] been.
[L1097] [39:49.76] And so, I think there is a ton of
[L1098] [39:51.72] opportunity for people coming into the
[L1099] [39:53.64] industry with deep technical or
[L1100] [39:56.04] scientific knowledge to now leverage
[L1101] [39:59.28] that in ways that, you know, maybe were,
[L1102] [40:02.08] um, were hard before, right? There was
[L1103] [40:04.24] too much sort of boiler plate to really,
[L1104] [40:06.20] you know, to really use that leverage
[L1105] [40:08.36] that you have. And so, I think we're
[L1106] [40:10.08] going to see a lot more of of of those
[L1107] [40:11.80] kinds of careers, of really kind of
[L1108] [40:13.32] building expertise in a technical topic,
[L1109] [40:16.08] in a scientific topic, and then be able
[L1110] [40:18.48] to turn that into software and software
[L1111] [40:21.56] products in a way that
[L1112] [40:24.84] was really difficult before, and in some
[L1113] [40:26.60] cases wasn't possible before, and is now
[L1114] [40:29.48] um you know, vastly easier.
[L1115] [40:31.72] If I was to look at a career ladder's
[L1116] [40:33.56] expectation, some of what you described
[L1117] [40:35.60] of maybe engaging with the customers and
[L1118] [40:38.60] understanding the business context,
[L1119] [40:40.80] uniquely in software engineering, it
[L1120] [40:42.28] feels like
[L1121] [40:43.56] the earliest levels are insulated from
[L1122] [40:46.32] all of that. You have your your tech
[L1123] [40:48.24] lead, tech leads handing out tasks, and
[L1124] [40:51.00] then the early level engineers just
[L1125] [40:53.68] given task just convert it into code.
[L1126] [40:56.08] And this sounds like you know, that
[L1127] [40:57.60] part's relatively solved. And if not
[L1128] [41:01.04] now, maybe I I'd be surprised if a year
[L1129] [41:03.68] or two from now wasn't like completely
[L1130] [41:06.32] solved. Um and I I think that could
[L1131] [41:09.64] scare a lot of junior engineers cuz they
[L1132] [41:11.64] they would think you're going to expect
[L1133] [41:13.64] me to graduate from college or start
[L1134] [41:16.84] working as a software engineer, and then
[L1135] [41:18.96] I would have the senior engineer
[L1136] [41:20.68] expectations.
[L1137] [41:22.40] Um what would you say to the the scared
[L1138] [41:25.08] software engineer that's just entering
[L1139] [41:26.68] the industry to all this change?
[L1140] [41:30.04] Yeah, you know, I think um
[L1141] [41:32.76] what I would remind them that, you know,
[L1142] [41:35.84] we as people who hire and build
[L1143] [41:38.44] organizations of software engineers, and
[L1144] [41:40.44] and they as people who have are building
[L1145] [41:42.84] software engineering careers, have have
[L1146] [41:44.72] really
[L1147] [41:46.00] um aligned incentives, right? Like you
[L1148] [41:48.84] know,
[L1149] [41:49.72] it it's not valuable to hire a bunch of
[L1150] [41:52.24] people and set them up to fail. Like
[L1151] [41:54.16] that's
[L1152] [41:55.04] nobody wants that. It's it's it's not an
[L1153] [41:57.28] outcome uh that is good for anybody. And
[L1154] [42:00.64] so, yeah, we're going to need to figure
[L1155] [42:02.72] out how do you support people on on that
[L1156] [42:05.76] path? How do you help people learn those
[L1157] [42:08.60] things? How do you give them the right
[L1158] [42:10.40] guardrails, you know? Hey, that first
[L1159] [42:12.80] time that you go out and talk to a
[L1160] [42:14.20] customer, yeah, it's going to be scary.
