Chunk 3; segments 695–1059. Start may repeat the previous chunk for context.

# How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar

Source ID: source-cfa80c9b2999d9de
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/How_Anthropic_Builds_And_How_Engineering_Will_Change_Soon_Thariq_Shihipar_en.txt
Video: https://www.youtube.com/watch?v=2Kch3tWMnw8

[L704] [24:07.56] that, you know, I use artifacts for
[L705] [24:09.04] almost everything, and and so I think
[L706] [24:10.32] that like we're going to see that also
[L707] [24:12.04] become big, and I think that's also ties
[L708] [24:15.12] into Claude Tag, right? So like let's
[L709] [24:16.80] say that you are um on your phone and
[L710] [24:20.00] Claude Tag has done a bunch of work for
[L711] [24:21.28] you. It creates a report. The report is
[L712] [24:23.40] readable, you know, on your phone
[L713] [24:25.16] because it's made the like the artifact
[L714] [24:27.36] look really great.
[L715] [24:28.84] >> Could you explain
[L716] [24:30.40] uh artifacts a little bit or kind of
[L717] [24:31.92] what are they and how do people use
[L718] [24:33.32] them?
[L719] [24:34.28] >> Artifacts are basically
[L720] [24:36.60] um
[L721] [24:37.96] Claude can upload essentially a web app
[L722] [24:40.40] for you to use, you know? And I think
[L723] [24:41.92] that
[L724] [24:42.96] uh
[L725] [24:44.28] you can use it in a really wide range of
[L726] [24:47.88] capabilities. They can now, for example,
[L727] [24:50.20] call your MCP. So you can make an
[L728] [24:52.08] artifact, for example, to read your
[L729] [24:54.52] inbox, you know, and like display it or
[L730] [24:57.20] sort it or tag it, right? As like a one
[L731] [24:59.88] way. You can also use artifact to uh
[L732] [25:02.52] show you a plan for coding, right? And
[L733] [25:04.32] then in that it might show like diagrams
[L734] [25:06.36] and file snippets and code and schemas.
[L735] [25:09.28] Um and so it shows you like sort of uh
[L736] [25:12.12] it's like an interactive
[L737] [25:14.36] display for the tap for the job you're
[L738] [25:16.72] doing right now, you know? And as Claude
[L739] [25:18.52] does more and more, you know, like jobs,
[L740] [25:21.68] we're realizing that like just text in
[L741] [25:24.16] text out is probably not useful for
[L742] [25:26.68] everything, right? And Claude is doing
[L743] [25:29.12] is better and better at creating
[L744] [25:30.64] essentially the exact interface for you
[L745] [25:32.44] at the right time. Um I think that
[L746] [25:35.08] there's like a lot more to do there, and
[L747] [25:37.36] I think
[L748] [25:38.32] it's another one of those things where
[L749] [25:39.48] you have to think about like, oh, like
[L750] [25:41.60] you know, could I be interacting with
[L751] [25:42.84] Claude in a different way, right? Like
[L752] [25:44.44] could I interact with it through an
[L753] [25:45.64] artifact? Could I
[L754] [25:47.68] you know, use it to like learn more or
[L755] [25:49.84] like to understand it better or stay in
[L756] [25:51.28] the loop or
[L757] [25:53.04] um
[L758] [25:54.20] improve some of my like own knowledge
[L759] [25:56.00] work or something. So,
[L760] [25:57.92] um
[L761] [25:58.76] yeah, I I I think it's pretty exciting.
[L762] [25:59.88] We're still kind of early to it.
[L763] [26:01.96] >> Does the daily driver model vary among
[L764] [26:04.84] engineers, or do people typically just
[L765] [26:07.04] pick the most intelligent one that's
[L766] [26:09.28] available at Anthropic?
[L767] [26:11.12] >> I do think, you know, similarly with
[L768] [26:13.20] models, if you use the smart models and
[L769] [26:14.80] you use them well and you give them
[L770] [26:17.04] task where they can, you know, are
[L771] [26:18.76] well-shaped and you've spent some time
[L772] [26:20.16] setting up a good verification harness
[L773] [26:21.76] and things like that, you can get a lot
[L774] [26:23.44] out of them.
[L775] [26:24.60] I don't think it's like choosing which
[L776] [26:26.48] model at the right time, you know? I
[L777] [26:28.72] think it's like, oh, how do you get the
[L778] [26:30.28] most out of the frontier models
[L779] [26:33.84] um because I think technology works the
[L780] [26:36.68] way it does, right? Like everything gets
[L781] [26:37.92] more abundant, more available.
[L782] [26:40.12] Um and so I think we're in this current
[L783] [26:43.52] weird spot where, you know, we don't
[L784] [26:44.92] quite have enough compute for everyone
[L785] [26:47.28] to have Fable at 100% of the rate
[L786] [26:48.80] limits.
[L787] [26:49.88] Um but I don't think this is like a
[L788] [26:51.16] durable skill to build figuring out like
[L789] [26:54.24] oh when do you use Fable and when do you
[L790] [26:55.68] Sonic, right? So
[L791] [26:58.52] I think it's like unintuitive there.
[L792] [27:00.96] But I think in practice if you're today
[L793] [27:03.68] what I would do is like I use Fable for
[L794] [27:05.80] planning, for brainstorming, for finding
[L795] [27:08.36] unknowns, for coming up with the
[L796] [27:09.64] detailed spec and I'd use Opus 5 to
[L797] [27:11.84] implement it.
[L798] [27:13.96] And I would probably use Opus 5 with
[L799] [27:16.12] workflows
[L800] [27:17.60] using like a verification aid like
[L801] [27:19.44] schema or like harness that's built with
[L802] [27:21.28] Fable, right? So I'd use Fable for those
[L803] [27:23.36] high leverage task.
[L804] [27:25.92] And yeah, Opus 5 for the execution and
[L805] [27:29.16] implementation.
[L806] [27:31.32] But yeah, I think increasingly probably
[L807] [27:33.08] next year I I I think you're just not
[L808] [27:34.52] going to be thinking that much about
[L809] [27:36.68] like which model.
[L810] [27:38.48] >> You mentioned that skill of I guess
[L811] [27:40.56] prompting and I've heard some people
[L812] [27:44.56] they say
[L813] [27:46.04] it's not too durable of a skill because
[L814] [27:49.04] it's kind of it's really specific to a
[L815] [27:51.04] model. Like these models they almost
[L816] [27:52.96] have their own unique
[L817] [27:55.60] I guess spiky intelligence. So if you if
[L818] [27:58.04] you knew everything that was very
[L819] [27:59.68] specific to let's say today's Fable and
[L820] [28:02.68] you're a master of today's Fable
[L821] [28:05.00] I mean maybe you don't need to know any
[L822] [28:06.60] of that stuff like a year from now and
[L823] [28:09.60] Fable 3 or 4 or 5 whatever comes out.
[L824] [28:13.08] Let's say you were talking to software
[L825] [28:15.56] engineer who's looking for career advice
[L826] [28:18.00] and they're thinking hey should I really
[L827] [28:20.52] become a master of engineering my
[L828] [28:23.44] prompt?
[L829] [28:24.64] >> I do want to say prompting is like
[L830] [28:26.20] little bit more than just a prompt you
[L831] [28:28.04] put in. It's also you know, you might
[L832] [28:29.84] have done made a skill or you might have
[L833] [28:31.72] like you know, added some data or
[L834] [28:33.12] something. It's not just a prompt you
[L835] [28:34.96] write but it's like everything you've
[L836] [28:36.08] done before that builds up into your
[L837] [28:37.92] context, right? So
[L838] [28:40.28] sometimes people see us write small
[L839] [28:42.08] prompts and they're like oh what is that
[L840] [28:43.80] mean? But we we just spent so much time
[L841] [28:46.04] on
[L842] [28:47.16] the the
[L843] [28:48.44] harness and the verification and and the
[L844] [28:50.24] skills. So,
[L845] [28:51.68] um
[L846] [28:52.36] I think it will be like really valuable
[L847] [28:54.40] to just keep better at prompting. I
[L848] [28:56.60] think to what you're saying about each
[L849] [28:58.48] model is different, you're right. Like I
[L850] [28:59.88] think each model is kind of its owns
[L851] [29:02.68] kind of like almost organic digital
[L852] [29:05.12] thing, you know? And so, there are
[L853] [29:06.76] quirks you have to learn and you do have
[L854] [29:09.48] to unlearn them. So,
[L855] [29:11.56] we recently wrote about like how we
[L856] [29:13.72] removed 80% of the system to prompt from
[L857] [29:15.64] Claude code, right? Um and one of the
[L858] [29:18.56] learnings we had was like we needed to
[L859] [29:20.20] remove examples from the tool
[L860] [29:22.72] descriptions. And you know, this used to
[L861] [29:24.68] be the only way you could get good
[L862] [29:26.40] output from the models was through
[L863] [29:29.00] tools, right? Or or through examples,
[L864] [29:31.16] right? So, you'd have to be like, "Hey,
[L865] [29:32.88] this is the right tool. Use this. Here
[L866] [29:35.24] Here's an example of writing a
[L867] [29:37.88] file well and here's an example of not
[L868] [29:39.56] doing it well."
[L869] [29:40.68] Um
[L870] [29:41.64] and now we found that like examples are
[L871] [29:43.88] mostly negative, I think, unless um
[L872] [29:47.24] you really see Claude doing something
[L873] [29:48.64] you don't like because
[L874] [29:50.32] uh it's just like quite imaginative.
[L875] [29:52.28] It's good at sticking to your intention
[L876] [29:54.00] and working with you. Um and so, we
[L877] [29:55.96] removed a lot of examples. So, in that
[L878] [29:58.32] case, yes, you do have to sort of like
[L879] [30:00.12] adapt, but the skill you're building is
[L880] [30:03.36] the skill to adapt. You learned how to
[L881] [30:05.96] use Fable and now you know a lot about
[L882] [30:08.28] Fable, but you also know how to learn
[L883] [30:10.44] You learned how to work with a model,
[L884] [30:12.68] right? And so, Fable 5.5 comes out, you
[L885] [30:14.92] need to
[L886] [30:15.96] learn how to use it again as well,
[L887] [30:19.24] but you'll be much faster cuz you're
[L888] [30:21.04] better at learning.
[L889] [30:22.52] You're better working with Fable 5, you
[L890] [30:24.36] know? And I think for me, I think the
[L891] [30:26.32] first model I worked with was GPT-2, and
[L892] [30:29.04] I remember like it was it was so hard to
[L893] [30:31.04] get
[L894] [30:32.20] a JSON output out of GPT-2. Like if you
[L895] [30:35.08] could just
[L896] [30:36.08] get it to like choose one of the
[L897] [30:38.36] categories that you gave it, that would
[L898] [30:40.04] be like incredible, you know? And so,
[L899] [30:42.60] um I think that but like
[L900] [30:45.08] building that skill, GPT-2 is such a
[L901] [30:47.56] different model than Fable 5, but I feel
[L902] [30:50.12] like the skill I spent doing that has
[L903] [30:52.92] like helped me be better at prompting
[L904] [30:54.92] Fable 5.
[L905] [30:56.12] >> Is there any like tribal knowledge or
[L906] [30:57.84] quirky tips in today's models where
[L907] [31:00.20] you'd say
[L908] [31:01.40] someone should should know that to get
[L909] [31:03.44] more when they prompt?
[L910] [31:04.80] >> I actually need to counter one I think
[L911] [31:06.52] that people have been saying where it's
[L912] [31:07.84] like, "Oh, just believe in yourself." or
[L913] [31:09.84] something. I I know that
[L914] [31:11.72] Jared
[L915] [31:13.16] Jared's post about the Riemann
[L916] [31:14.40] hypothesis had like he was just like,
[L917] [31:16.32] "Keep going. Just believe in yourself."
[L918] [31:18.48] I think in this case it was mostly just
[L919] [31:20.76] Jared saying it's okay to use compute to
[L920] [31:23.72] solve this problem and I'm giving you
[L921] [31:25.40] permission to do it, you know? And I
[L922] [31:27.76] think that like that's not exactly the
[L923] [31:29.60] same as
[L924] [31:31.04] you know, I believe in you, you know
[L925] [31:34.08] what I mean? It's really just like
[L926] [31:35.84] letting the model use compute. So, I
[L927] [31:38.36] think that that is something I would
[L928] [31:41.04] I like to tell the models right now is
[L929] [31:42.92] like, "Okay, hey, I think this is a hard
[L930] [31:44.56] problem. Use sub agents, you know? Use
[L931] [31:47.00] workflows. Like if you need it, right?
[L932] [31:49.00] So, like I always tell it to like use
[L933] [31:51.00] its own judgment, but I'm giving you
[L934] [31:55.84] permission to do this stuff, right? And
[L935] [31:58.60] I think that
[L936] [31:59.92] uh
[L937] [32:00.72] you have to sort of remember that the
[L938] [32:01.96] models by default, you know, do what
[L939] [32:04.48] maybe the average user wants, which is
[L940] [32:06.08] like they want it to respond and start
[L941] [32:08.36] doing work as fast as possible.
[L942] [32:11.44] Roughly like complete the task, but not
[L943] [32:13.84] spend like a crazy amount of compute on
[L944] [32:15.68] it, you know? And so, I think that like
[L945] [32:18.56] um you have to sort of if you want the
[L946] [32:20.76] model to do it differently, you have to
[L947] [32:22.04] nudge it slightly, right? So, you might
[L948] [32:23.80] have to be like, "Okay, hey, like I
[L949] [32:25.84] don't want you to do any work yet. I
[L950] [32:27.36] want you to brainstorm, you know? I want
[L951] [32:29.20] you to like think with me, right?" Um
[L952] [32:32.12] and if you prompt it that way, it will
[L953] [32:33.40] start doing that. If you want it to
[L954] [32:35.32] spend a lot of compute, if you're like,
[L955] [32:36.72] hey,
[L956] [32:37.52] you know, sometimes I'll say like
[L957] [32:39.72] Yeah, hey, I think this is a hard
[L958] [32:40.64] problem. Uh feel free to use workflows.
[L959] [32:43.16] If I'm running overnight, I might just
[L960] [32:44.56] be like, hey, I'm going to sleep, you
[L961] [32:46.04] know, set the slash goal or something
[L962] [32:47.44] and then
[L963] [32:48.52] uh let it let it run. So,
[L964] [32:51.00] um
[L965] [32:51.76] yeah, I think there is a
[L966] [32:54.36] uh just like giving it permission to do
[L967] [32:56.28] the thing you want.
[L968] [32:57.88] >> When you recently removed so much of the
[L969] [33:00.32] system prompt,
[L970] [33:01.88] uh how did you prove that
[L971] [33:04.32] the end result was better?
[L972] [33:06.44] >> We have a bunch of user metrics just
[L973] [33:08.32] like how, you know, how much do people
[L974] [33:10.40] like the output of Claude? Do you
[L975] [33:12.12] something you get that survey and you
[L976] [33:13.52] see it. Um
[L977] [33:15.24] we run evals against, you know, our
[L978] [33:18.76] internal eval uh and external evals to
[L979] [33:21.64] see like how it performs at these
[L980] [33:23.52] different tasks. Um
[L981] [33:25.44] but I think it is hard like sometimes
[L982] [33:27.44] you don't realize that they're not If
[L983] [33:29.88] Claude is telling the user if it does
[L984] [33:32.16] all its work and then it's like, hey,
[L985] [33:33.80] maybe you should go to sleep, there's no
[L986] [33:35.48] eval for Claude tells you to go to
[L987] [33:36.92] sleep, you know what I mean? And now
[L988] [33:38.04] we're like have to like catch this like
[L989] [33:40.00] new behavior. Um so, it is hard. I think
[L990] [33:42.80] we spent a lot of time
[L991] [33:44.64] basically just um
[L992] [33:46.44] you know, like removing lines in the
[L993] [33:47.68] system prompt, running evals, uh seeing
[L994] [33:50.04] how it works, seeing how people uh
[L995] [33:52.08] reported it internally, and then like
[L996] [33:54.36] adjusting, but it was like a full-time
[L997] [33:56.12] job for several people over long periods
[L998] [33:58.36] of time. And so,
[L999] [34:00.12] I don't think I'd necessarily recommend
[L1000] [34:01.96] everyone do this. I think that's kind of
[L1001] [34:04.36] why we wrote that post about what we
[L1002] [34:06.28] learned from like adjusting the system
[L1003] [34:08.48] prompt. And we think that's pretty
[L1004] [34:10.32] general. So, hopefully you don't have to
[L1005] [34:12.44] like now
[L1006] [34:13.68] go through this like crazy iteration
[L1007] [34:15.32] process.
[L1008] [34:16.72] >> OpenAI, Anthropic, Cursor, and Vercel
[L1009] [34:20.48] all use this product to make their lives
[L1010] [34:22.24] better.
[L1011] [34:23.20] And the problem it solves is when you're
[L1012] [34:25.08] building SaaS or an ad product and you
[L1013] [34:27.72] want to sell to other companies, there's
[L1014] [34:29.60] all these requirements you need to meet.
[L1015] [34:31.80] There's SSL, there's SCIM, there's RBAC,
[L1016] [34:35.44] there's audit logs. These are all things
[L1017] [34:37.24] that take time to integrate, but aren't
[L1018] [34:39.40] the main focus of your app. WorkOS is an
[L1019] [34:41.72] API layer that lets you meet all of
[L1020] [34:43.40] these requirements in just a few lines
[L1021] [34:45.56] of code. So, let's say you have a new
[L1022] [34:47.60] SaaS product and you want to sell to
[L1023] [34:49.28] other companies, WorkOS will solve all
[L1024] [34:51.76] of these critical feature gaps for you.
[L1025] [34:54.48] You can check them out at workos.com to
[L1026] [34:56.96] learn more and get started. And I
[L1027] [34:59.12] appreciate them for supporting my work
[L1028] [35:00.96] and sponsoring this podcast.
[L1029] [35:02.84] >> I think a lot of people
[L1030] [35:05.40] when they use Claude code, they get
[L1031] [35:07.40] excellent results when it's kind of
[L1032] [35:09.88] getting
[L1033] [35:11.44] very objective work done.
[L1034] [35:13.76] But when it's kind of prompting models
[L1035] [35:15.96] to do beautiful or tasteful work, it's
[L1036] [35:18.72] kind of not always, you know, it's
[L1037] [35:20.32] pretty much more hit and miss. And so,
[L1038] [35:23.00] you know, how do you best instill like a
[L1039] [35:25.44] very particular style you're going for
[L1040] [35:27.72] or particular taste in the models
[L1041] [35:30.24] outputs when it's a much more subjective
[L1042] [35:32.88] domain, maybe like front end?
[L1043] [35:35.08] >> The way you do it is sort of like you
[L1044] [35:37.28] stay in the loop. I think you give it
[L1045] [35:39.32] references, right? And I think the more
[L1046] [35:41.16] references you give it with data, the
[L1047] [35:44.36] better. So, like it's better to give an
[L1048] [35:46.80] HTML file than a screenshot, right? It's
[L1049] [35:48.64] better to give a Figma file than like a
[L1050] [35:51.72] raster image or something, right? Cuz
[L1051] [35:53.60] now it if Claude wants to know the
[L1052] [35:55.68] border radius of this thing, it's like,
[L1053] [35:57.20] oh, what's the Figma component border
[L1054] [35:59.80] radius and let me just copy it over. And
[L1055] [36:02.64] so, I think giving it a bunch of
[L1056] [36:04.20] references, ideally in code, is a really
[L1057] [36:07.16] good way, right? Of like getting it to
[L1058] [36:09.28] stick to this. Um
[L1059] [36:11.04] I think if not, you can then ask it to
[L1060] [36:14.40] if you don't have like
[L1061] [36:16.24] uh let's say you're not a designer.
[L1062] [36:18.16] There's probably Step one is being like,
[L1063] [36:20.68] okay, now I'm not a designer. There's a
[L1064] [36:22.48] lot I don't know about design, you know?
[L1065] [36:25.64] And like there's was lot I don't know
[L1066] [36:26.84] about iteration. I don't even know what
[L1067] [36:29.04] good looks like, right? And I think this
[L1068] [36:30.64] is like part of the art of working with
