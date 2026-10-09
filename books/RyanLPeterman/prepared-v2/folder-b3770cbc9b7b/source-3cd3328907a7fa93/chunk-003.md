Chunk 3; segments 780–1178. Start may repeat the previous chunk for context.

# Google DeepMind Distinguished Eng (L9): How To Land a Job at a Frontier Lab | Vlad Feinberg

Source ID: source-3cd3328907a7fa93
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Google_DeepMind_Distinguished_Eng_(L9)_How_To_Land_a_Job_at_a_Frontier_Lab_Vlad_Feinberg_en.txt
Video: https://www.youtube.com/watch?v=cDyi91onoJ8

[L789] [30:10.68] um
[L790] [30:11.40] that's that's really
[L791] [30:13.92] the only thing you should be doing,
[L792] [30:15.24] right? Like, you know, worrying about it
[L793] [30:16.72] is not going to not going to help you.
[L794] [30:18.44] And so, part of why I wanted to write
[L795] [30:20.48] this post is is in response to that.
[L796] [30:23.72] Uh because it it it was something that I
[L797] [30:26.08] could see echoed, you know, I gave the a
[L798] [30:29.44] lecture at Princeton a while back and,
[L799] [30:31.36] you know, a big question that came up is
[L800] [30:32.92] like, you know, how do I work at
[L801] [30:34.80] DeepMind? And And it's something that
[L802] [30:36.68] like uh yeah, just when people find out
[L803] [30:39.12] what I do, that's the top question
[L804] [30:40.48] people ask. So, I figured it would be
[L805] [30:42.72] helpful to add a little bit more
[L806] [30:45.08] constructive
[L807] [30:47.16] you know, direction to the discourse
[L808] [30:48.88] here.
[L809] [30:49.84] >> One last thing on the post cuz, you
[L810] [30:52.12] know, if you think about getting a role,
[L811] [30:54.24] there's obviously the skills and we
[L812] [30:56.56] talked a lot about the skills and your
[L813] [30:58.40] fitness for the role, but there's also
[L814] [31:00.44] kind of the
[L815] [31:02.00] signaling for that role and like what is
[L816] [31:04.60] kind of valued if you were to be saying
[L817] [31:07.24] marketing yourself to one of these
[L818] [31:09.00] frontier labs, what signals
[L819] [31:11.96] matter most?
[L820] [31:13.48] >> Actual evidence that you've created
[L821] [31:15.88] something of uh
[L822] [31:18.96] of use to other people along the line of
[L823] [31:21.92] kernels, right? Like you can take any of
[L824] [31:25.28] the many open source LLMs that we have
[L825] [31:27.88] and optimize them. You don't have to
[L826] [31:30.12] make them better in every case. You
[L827] [31:31.68] could show that oh, I have an
[L828] [31:32.80] improvement for this and that setting.
[L829] [31:35.16] It doesn't even have to be something
[L830] [31:36.68] that speeds up the model on GPU. There's
[L831] [31:39.44] all sorts of open source stacks like
[L832] [31:41.60] vLLM. There's a lot of other
[L833] [31:44.60] things that you can do besides
[L834] [31:46.48] accelerating the LLM inference on
[L835] [31:48.68] device. The serving stack that surrounds
[L836] [31:51.44] LLMs is a very sophisticated distributed
[L837] [31:54.36] system that has to maintain
[L838] [31:56.96] this KB cache memory and deal with
[L839] [32:01.16] all sorts of like load balancing and
[L840] [32:04.88] request queuing and and very common
[L841] [32:06.96] problems for for back-end servers. And
[L842] [32:10.48] these projects are always looking for
[L843] [32:11.60] help. So, you know, contributions to
[L844] [32:14.68] vLLM or SG Lang
[L845] [32:17.32] or demonstrations with TensorRT.
[L846] [32:20.64] They have I think a
[L847] [32:22.32] a distributed system called Dynamo that
[L848] [32:24.56] allows for disaggregated serving
[L849] [32:27.80] where
[L850] [32:29.04] you could show that you you made a
[L851] [32:30.40] project using these components, you
[L852] [32:32.20] improved these components. Like that
[L853] [32:34.64] would be an extremely positive signal
[L854] [32:37.16] for any candidate that I'm looking at
[L855] [32:39.64] and and a very welcome contribution to
[L856] [32:42.04] open source.
[L857] [32:43.88] >> I think also a lot of what we said is
[L858] [32:45.68] kind of assuming the path of external
[L859] [32:49.00] hire into Frontier Lab.
[L860] [32:51.88] But a lot of these Frontier Labs have
[L861] [32:55.08] large organizations that aren't
[L862] [32:56.52] necessarily doing the cutting edge
[L863] [32:58.60] Frontier work. So let's say yeah, for
[L864] [33:00.96] instance, I mean, you know, Google
[L865] [33:02.48] DeepMind versus
[L866] [33:04.88] let's say there's some infrastructure
[L867] [33:06.40] eng that's working on search and they
[L868] [33:09.08] have the back-end skillset, maybe not as
[L869] [33:11.04] much domain context and they try to
[L870] [33:13.80] internal transfer to Google DeepMind.
[L871] [33:16.32] Does any of your advice differ in that
[L872] [33:18.16] kind of case for like an internal
[L873] [33:19.56] transfer versus
[L874] [33:21.56] someone who's coming from external?
[L875] [33:23.68] >> There's someone who I worked with
[L876] [33:26.52] closely on the search side
[L877] [33:29.16] who actually did transfer to my team
[L878] [33:32.40] Nate Lidzén and he's amazing and now he
[L879] [33:34.56] owns so much of
[L880] [33:36.88] like what we do on my team in terms of
[L881] [33:40.44] inference code design for
[L882] [33:42.80] like flash and flashlight and
[L883] [33:46.00] I would say like he's a really great
[L884] [33:47.44] example of this where
[L885] [33:49.84] his approach was, you know, how do I
[L886] [33:52.80] help my PA, my product area
[L887] [33:57.36] adopt this technology as effectively as
[L888] [33:59.44] possible. So I think there's, you know,
[L889] [34:02.24] definitely
[L890] [34:03.76] if you're
[L891] [34:05.16] in
[L892] [34:06.72] organization that isn't directly
[L893] [34:08.96] generating these models, but in some way
[L894] [34:10.80] trying to leverage them there's
[L895] [34:13.88] a very big gap in terms of applying
[L896] [34:16.36] these LLMs effectively, serving them
[L897] [34:18.56] effectively
[L898] [34:20.64] within
[L899] [34:22.16] your organization
[L900] [34:24.36] and becoming someone who does that
[L901] [34:26.96] really effectively not only creates a
[L902] [34:29.40] ton of value
[L903] [34:31.12] in terms of like
[L904] [34:33.80] the uh you know specific business need
[L905] [34:36.60] for your org which will definitely
[L906] [34:38.08] elevate you and your org
[L907] [34:39.92] but it'll also be the case that you're
[L908] [34:42.36] going to just naturally become the
[L909] [34:44.28] partner that we work with
[L910] [34:46.16] on the research side to make sure that
[L911] [34:48.84] our models are effective within your org
[L912] [34:51.08] and so at that point you know you may or
[L913] [34:53.16] may not want to transfer definitely if
[L914] [34:56.04] you transfer we you know be happy to
[L915] [34:57.88] work with you but like
[L916] [35:00.32] at that point I think you're you're
[L917] [35:01.68] you're already doing something that is
[L918] [35:03.28] cutting edge which is
[L919] [35:04.96] integrating this new technology into
[L920] [35:08.00] you know a real product that people use
[L921] [35:09.76] and so
[L922] [35:11.80] yeah that'd be my advice there.
[L923] [35:13.80] >> As it towards the end of this post as we
[L924] [35:15.76] as we leave this topic you had the
[L925] [35:18.68] concrete invitation cuz I know you were
[L926] [35:21.08] hiring
[L927] [35:22.28] do you want to say what that was?
[L928] [35:23.80] >> Yeah so I was just trying to think of
[L929] [35:25.76] like you know you know how do I put my
[L930] [35:28.04] money where my mouth is
[L931] [35:30.00] um
[L932] [35:30.64] how do I demonstrate look this is good
[L933] [35:33.56] way to show that you have you know at
[L934] [35:36.60] least some evidence of of like the the
[L935] [35:38.60] skills that I called out as important
[L936] [35:40.32] you know intent mathematical maturity
[L937] [35:42.44] grit
[L938] [35:43.80] and so I listed out a couple of
[L939] [35:46.04] exercises that demonstrate you know some
[L940] [35:48.88] initial knowledge of scaling laws some
[L941] [35:51.00] willingness to get into the weeds
[L942] [35:53.08] engineering wise in terms of
[L943] [35:54.48] implementing a real transformer
[L944] [35:56.96] and
[L945] [35:58.20] sort of willingness to pick up the kind
[L946] [36:00.44] of bread and butter bread and butter
[L947] [36:01.76] math that we use every day to size these
[L948] [36:06.28] LLMs
[L949] [36:07.48] and you know I won't I won't recall the
[L950] [36:10.44] full list of like the exercises that I
[L951] [36:12.40] expected here but like you know if if
[L952] [36:14.80] you do the detailed like handwritten
[L953] [36:18.16] version of the scaling book exercises
[L954] [36:20.56] and you know send me a video of yourself
[L955] [36:22.20] doing them along with the transformer
[L956] [36:24.20] exercise on my post
[L957] [36:26.56] then that's something if you can work in
[L958] [36:28.44] the uh New York office, I would love to,
[L959] [36:31.32] you know, interview you for. And quite a
[L960] [36:34.32] few people reached out to me about that.
[L961] [36:36.28] I actually already have had a couple
[L962] [36:37.76] submissions and we're proceeding with
[L963] [36:39.88] the loop with those people. So,
[L964] [36:43.04] yeah, it's it's quite a bit of work, but
[L965] [36:45.28] uh impressively, I got a response within
[L966] [36:47.36] like, I think,
[L967] [36:48.72] a week of posting. So,
[L968] [36:51.84] uh it's definitely doable.
[L969] [36:54.60] Uh
[L970] [36:55.68] yeah, I mean, I don't have unlimited
[L971] [36:57.24] head count, so I mean, the offer's on
[L972] [36:59.28] the table, but the, you know,
[L973] [37:01.56] I can only hire so many people. The good
[L974] [37:03.96] thing is, though, that is such a strong
[L975] [37:05.96] sign of,
[L976] [37:07.84] you know, self-development
[L977] [37:09.60] that uh
[L978] [37:11.20] not only is this a something that you
[L979] [37:12.64] should be doing for its own sake,
[L980] [37:14.32] regardless of whether or not you will
[L981] [37:16.20] get a job at at DeepMind specifically,
[L982] [37:20.04] but I think it'll be something that's,
[L983] [37:22.08] you know,
[L984] [37:23.20] lets you basically prepare for
[L985] [37:25.56] interviews in other places.
[L986] [37:27.68] Uh certainly, if you reach out to me
[L987] [37:29.16] with these uh exercises completed, like,
[L988] [37:32.44] even if, you know, I do all my hiring,
[L989] [37:35.08] there's tons of people who I know who
[L990] [37:37.56] are hiring as well, and I'd be happy to
[L991] [37:39.44] refer people as well.
[L992] [37:41.60] >> OpenAI, [snorts]
[L993] [37:42.52] Anthropic, Cursor, and Vercel all use
[L994] [37:45.80] this product to make their lives better.
[L995] [37:48.04] And the problem it solves is when you're
[L996] [37:49.96] building SaaS or an ad product, and you
[L997] [37:52.60] want to sell to other companies, there's
[L998] [37:54.52] all these requirements you need to meet.
[L999] [37:56.60] There's SSL, there's SCIM, there's RBA,
[L1000] [38:00.24] there's audit logs. These are all things
[L1001] [38:02.04] that take time to integrate, but aren't
[L1002] [38:04.20] the main focus of your app. WorkOS is an
[L1003] [38:06.52] API layer that lets you meet all of
[L1004] [38:08.20] these requirements in just a few lines
[L1005] [38:10.36] of code. So, let's say you have a new
[L1006] [38:12.44] SaaS product, and you want to sell to
[L1007] [38:14.08] other companies, WorkOS will solve all
[L1008] [38:16.56] of these critical feature gaps for you.
[L1009] [38:19.32] You can check them out at workos.com to
[L1010] [38:21.80] learn more and get started. And I
[L1011] [38:23.96] appreciate them for supporting my work
[L1012] [38:25.84] and sponsoring this podcast.
[L1013] [38:27.84] On the next [snorts] topic, I mean, uh I
[L1014] [38:29.80] saw you're the the the area lead for
[L1015] [38:32.20] pre-training on Gemini, and I just
[L1016] [38:34.84] thought it might be interesting to hear
[L1017] [38:36.20] you give um
[L1018] [38:37.84] uh kind of like a high-level overview of
[L1019] [38:39.96] what pre-training is or in your words,
[L1020] [38:42.04] and maybe what are the the high-level
[L1021] [38:44.16] challenges in the area. I mean, we can
[L1022] [38:46.00] talk about that.
[L1023] [38:46.88] >> Yeah, so
[L1024] [38:48.72] there's there's quite a lot of work that
[L1025] [38:50.16] we do in pre-training. Um as an area
[L1026] [38:53.56] lead for it,
[L1027] [38:55.76] the specific things that my team is
[L1028] [38:57.68] responsible for delivering uh include uh
[L1029] [39:01.56] the flash model, the flashlight model.
[L1030] [39:04.48] These are models that get used for AI
[L1031] [39:06.20] overviews and AI mode in the search bar,
[L1032] [39:09.12] uh as well as some other uh 1P models
[L1033] [39:11.80] that are used by different orgs like ads
[L1034] [39:14.40] and YouTube.
[L1035] [39:16.20] Besides this, we're also key technical
[L1036] [39:18.68] POCs for the uh Google-Apple
[L1037] [39:21.48] partnership, uh and so we do technical
[L1038] [39:23.56] work there.
[L1039] [39:25.88] Those are the actual
[L1040] [39:27.88] like product-level deliverables
[L1041] [39:30.28] uh from my team.
[L1042] [39:31.52] Uh beyond that, we do research to make
[L1043] [39:35.64] sure that these deliverables are
[L1044] [39:37.24] state-of-the-art.
[L1045] [39:38.72] And also, we do general pre-training re-
[L1046] [39:40.60] research that contributes to the Pro
[L1047] [39:42.32] Series model as well.
[L1048] [39:44.16] And the nature of the research, I would
[L1049] [39:48.16] say generally breaks down into three
[L1050] [39:49.84] different verticals. There's
[L1051] [39:51.88] distillation, which I mentioned earlier.
[L1052] [39:55.16] There's what I like to call inference
[L1053] [39:57.20] co-design. So, uh
[L1054] [39:59.60] creating neural architectures that are
[L1055] [40:02.40] efficient
[L1056] [40:03.92] uh to run inference on. So, coming up
[L1057] [40:06.56] with the network topology, the shapes of
[L1058] [40:10.32] the matrices that the matmuls uh
[L1059] [40:14.32] uh use uh inside of uh
[L1060] [40:16.92] uh gating and linear layers for this
[L1061] [40:18.28] Transformer as well as the attention
[L1062] [40:20.00] shapes, num heads, that kind of thing.
[L1063] [40:22.92] So, that that is effectively utilizing
[L1064] [40:24.88] the hardware that you're serving on.
[L1065] [40:27.32] And then, the final
[L1066] [40:29.52] uh pillar here is new quantization
[L1067] [40:31.76] methods. And so,
[L1068] [40:34.12] quantization is just something that's uh
[L1069] [40:36.12] been near and dear to my heart that I've
[L1070] [40:37.68] been working on the research side for
[L1071] [40:39.84] ever since I joined Google, and it
[L1072] [40:42.08] really changes what's feasible for uh
[L1073] [40:47.44] the first two. So,
[L1074] [40:49.60] uh that's why,
[L1075] [40:51.08] you know, furthering the state of the
[L1076] [40:52.48] art in terms of how you can compress
[L1077] [40:54.44] models is is also a very important
[L1078] [40:57.04] pillar in the research that my team
[L1079] [40:58.88] does. Generally, uh
[L1080] [41:01.16] uh quantization uh refers to reducing,
[L1081] [41:05.28] in some sense, the size that the neural
[L1082] [41:07.72] nets take up uh in order to represent
[L1083] [41:10.40] their weights. So, typically, a neural
[L1084] [41:13.40] net, when you're training it, uh is
[L1085] [41:16.32] represented as a
[L1086] [41:17.92] uh series of numbers that make up the
[L1087] [41:19.60] matrices inside of the neural net uh
[L1088] [41:21.88] that are stored in FP32, 32-bit
[L1089] [41:24.92] floating-point weights.
[L1090] [41:26.40] Um it turns out that, when you do these
[L1091] [41:30.24] computations, you don't need all of that
[L1092] [41:32.44] extra precision to still maintain the
[L1093] [41:34.24] quality of your neural net. And you can,
[L1094] [41:37.08] with pretty simple methods, reduce the
[L1095] [41:40.20] precision at which you store these
[L1096] [41:42.32] weights down to 4-bits. So, uh all of a
[L1097] [41:45.92] sudden, this huge range of numbers uh
[L1098] [41:49.64] that we would take, you know, this float
[L1099] [41:51.88] 32 to represent, uh something that gets
[L1100] [41:54.40] you down to like, you know, seven digits
[L1101] [41:56.76] of precision,
[L1102] [41:58.28] uh can,
[L1103] [42:00.12] you know, with somewhat high fidelity,
[L1104] [42:02.76] uh still be um
[L1105] [42:04.76] represented well by
[L1106] [42:07.16] 4-bit ints, which, you know, just cover
[L1107] [42:09.08] this uh tiny range of like minus eight
[L1108] [42:11.08] to seven. And
[L1109] [42:13.52] um
[L1110] [42:14.08] it's it's kind of a miracle that you can
[L1111] [42:15.60] do this.
[L1112] [42:17.24] But what's even more of a miracle is
[L1113] [42:19.36] that you can apply these kind of
[L1114] [42:21.68] quantization transforms to the runtime
[L1115] [42:25.00] activations that the neural net
[L1116] [42:26.28] processes. And as soon as you do that,
[L1117] [42:29.40] the actual math that you're performing,
[L1118] [42:31.52] because you're taking much smaller
[L1119] [42:34.16] operands to your matmul than what you
[L1120] [42:36.32] were doing before,
[L1121] [42:37.88] the amount of electricity that it takes
[L1122] [42:39.36] to compute the neural net drops
[L1123] [42:41.32] significantly.
[L1124] [42:42.56] And what's interesting is that
[L1125] [42:44.92] like 99% of the total cost of operation
[L1126] [42:48.12] for
[L1127] [42:49.36] AI hardware comes from the
[L1128] [42:53.20] uh power that it takes to run these
[L1129] [42:54.56] chips. And so, if you can do these
[L1130] [42:57.00] operations, you could just make neural
[L1131] [42:58.96] nets run more cheaply, run more
[L1132] [43:00.52] efficiently.
[L1133] [43:02.56] That helps
[L1134] [43:04.28] uh
[L1135] [43:04.84] uh in terms of like serving more
[L1136] [43:05.96] requests, and it helps in terms of
[L1137] [43:07.72] latency.
[L1138] [43:09.76] So, the name of the game for quant
[L1139] [43:11.80] research is how do we push the frontier
[L1140] [43:13.64] beyond like this like four-bit range?
[L1141] [43:16.48] >> There's this take that I see on Twitter
[L1142] [43:18.64] all the time, um which is just talking
[L1143] [43:21.00] about MFU, and someone who's not in the
[L1144] [43:23.08] space, or model flops utilization.
[L1145] [43:26.08] Someone who's not in the space, they see
[L1146] [43:27.52] a number in the low 10s, and they think,
[L1147] [43:30.24] "Wow, they're wasting all of those GPU
[L1148] [43:32.04] resources."
[L1149] [43:33.48] Um I was curious if you could just
[L1150] [43:36.16] clarify that for people why a low MFU,
[L1151] [43:39.52] or I guess naively low, is actually not
[L1152] [43:42.04] low at all. And maybe also explain what
[L1153] [43:43.88] MFU is.
[L1154] [43:44.76] >> Yeah, so
[L1155] [43:46.60] when we compute MFU, you want to divide
[L1156] [43:50.28] the actual number of flops that the
[L1157] [43:52.60] neural net is performing here by the
[L1158] [43:55.08] total number of flops that the
[L1159] [43:56.56] accelerator could have done in the time
[L1160] [43:58.64] of your request. And so, in some sense,
[L1161] [44:01.64] this is giving us the
[L1162] [44:04.20] uh percent of time that we're usefully
[L1163] [44:07.36] utilizing the flops rate of the
[L1164] [44:09.56] accelerator. And to get to 100% MFU, you
[L1165] [44:13.40] would just need be need to be fully
[L1166] [44:15.00] utilizing uh the matmul unit of uh
[L1167] [44:17.92] whatever accelerator uh you're doing
[L1168] [44:20.00] here. So, it would just have to be doing
[L1169] [44:21.20] like a bunch of matmuls in a loop
[L1170] [44:23.96] uh without reading any memory or doing
[L1171] [44:25.92] any other operations.
[L1172] [44:28.12] That's not a very useful computation. Uh
[L1173] [44:30.92] and in practice,
[L1174] [44:33.72] neural nets have to apply activation
[L1175] [44:37.64] functions or do attention or write
[L1176] [44:41.56] intermediate outputs back to uh HBM. And
[L1177] [44:45.04] all of those different operations
[L1178] [44:47.88] will require utilizing the memory bus or
[L1179] [44:50.56] utilizing vector processing units
[L1180] [44:53.28] uh or simply they might be a
[L1181] [44:56.08] mathematical operations that
[L1182] [44:59.20] the underlying hardware performs more
[L1183] [45:02.00] slowly than they uh than uh it might
[L1184] [45:05.16] perform a matmul.
[L1185] [45:06.49] >> [snorts]
[L1186] [45:06.52] >> And so, all of those things contribute
[L1187] [45:08.48] to not running at the full speed that
