Chunk 3; segments 666–999. Start may repeat the previous chunk for context.

# Sergey Levine: Humanoid Robotics Results, Chinese Labs & Future Timelines

Source ID: source-902fbdda6bccd443
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Sergey_Levine_Humanoid_Robotics_Results,_Chinese_Labs_&_Future_Timelines_en.txt
Video: https://www.youtube.com/watch?v=9OSbaPjv0Rc

[L675] [23:04.24] are thinking about how do you like how
[L676] [23:07.12] do you present something that that
[L677] [23:09.36] somebody can watch and take in kind of
[L678] [23:11.92] at a glance what generalization is. I
[L679] [23:14.00] think you can see a lot of creative
[L680] [23:15.44] steps towards that. Live demos, these
[L681] [23:17.36] kind of like really long time lapses. I
[L682] [23:19.28] think it's a great idea and I think
[L683] [23:20.32] that's a like a a really nice way to
[L684] [23:22.96] move towards elevating the importance of
[L685] [23:25.60] generalization in people's kind of
[L686] [23:27.52] conscious consciousness. Um you know we
[L687] [23:30.40] um when we were working on the um the PI
[L688] [23:33.52] star 6 project the RL project that we
[L689] [23:35.36] did uh late last year we um wanted to do
[L690] [23:39.44] some longer uh horizon experiments. In
[L691] [23:42.80] some case it's obvious like we had our
[L692] [23:44.08] robot assembling boxes at at Dandelion
[L693] [23:45.84] Chocolate Factory. So they're like, you
[L694] [23:47.12] know, it's an actual chocolate factory,
[L695] [23:48.24] so they need the boxes. So we run it for
[L696] [23:50.08] several days. Uh but we had this coffee
[L697] [23:52.16] task which was uh the robot was using an
[L698] [23:54.72] espresso machine to make espresso. So
[L699] [23:56.48] what we did is we ran it for 13 hours
[L700] [23:58.16] making espresso drinks. Uh and we are,
[L701] [24:00.72] you know, we tried to be like very uh I
[L702] [24:02.56] guess um environmentally conscious about
[L703] [24:04.32] this. So we didn't want to like throw
[L704] [24:05.36] out the coffee. So after 13 hours,
[L705] [24:06.80] everyone in the office was like a little
[L706] [24:08.64] wiry cuz someone has to like drink the
[L707] [24:11.04] coffee. But it like it ran for 13 hours
[L708] [24:13.28] and it was pretty cool. But it it
[L709] [24:14.56] screwed up a few times. Like it'll um
[L710] [24:16.48] spill all the the coffee grounds and
[L711] [24:18.24] then it needs to go and get like a cloth
[L712] [24:19.68] and wipe it down. But like it does it
[L713] [24:21.76] and it's you know nothing exploded 13
[L714] [24:23.84] hours went by. Probably the most
[L715] [24:25.76] negative consequence was like loss of
[L716] [24:27.84] sleep from too much caffeination.
[L717] [24:29.60] >> But when it spills the coffee grounds
[L718] [24:31.20] and cleans it up is that's it did that
[L719] [24:33.84] by itself.
[L720] [24:34.80] >> Well, so the way the way that that
[L721] [24:36.48] experiment was done is that there is a
[L722] [24:38.16] high level prompting. So like roughly
[L723] [24:40.16] the prompt is updated maybe every like
[L724] [24:42.00] uh 5 minutes or so like in between
[L725] [24:44.72] semantically coherent tasks. So you tell
[L726] [24:46.48] it like make espresso, clean up the
[L727] [24:48.24] machine etc. So those steps the actual
[L728] [24:50.72] like clean up the the machine was
[L729] [24:52.24] commanded by a person. Um in principle
[L730] [24:54.72] we could automate that. In fact one of
[L731] [24:55.92] the things we're spending a lot of
[L732] [24:57.20] effort now is improving our high level
[L733] [24:58.56] policy that does those commands. But for
[L734] [25:00.24] that experiment yeah like every 5
[L735] [25:01.44] minutes somebody basically updates what
[L736] [25:02.88] is being asked to do. Like the way we
[L737] [25:04.56] intended it was like the commands would
[L738] [25:06.24] be like if you go to to an actual coffee
[L739] [25:07.84] shop, you say like, "Oh, I want a latte.
[L740] [25:09.36] I want an espresso." Like that was
[L741] [25:10.48] supposed to be the prompt. Except then
[L742] [25:12.00] you also have to tell it, "I want you to
[L743] [25:13.12] clean it up before you do the next one."
[L744] [25:15.03] [laughter]
[L745] [25:15.92] >> That makes sense. Open AAI, Enthropic,
[L746] [25:19.28] Cursor, and Versel all use this product
[L747] [25:22.16] to make their lives better. And the
[L748] [25:24.24] problem it solves is when you're
[L749] [25:25.92] building SAS or an AI product and you
[L750] [25:28.48] want to sell to other companies, there's
[L751] [25:30.32] all these requirements you need to meet.
[L752] [25:32.40] There's SSO, there's SKIM, there's
[L753] [25:35.04] arbback, there's audit logs. These are
[L754] [25:37.44] all things that take time to integrate
[L755] [25:39.44] but aren't the main focus of your app.
[L756] [25:41.44] Work OS is an API layer that lets you
[L757] [25:43.60] meet all of these requirements in just a
[L758] [25:45.84] few lines of code. So, let's say you
[L759] [25:47.76] have a new SAS product and you want to
[L760] [25:49.68] sell to other companies. Work OS will
[L761] [25:51.92] solve all of these critical feature gaps
[L762] [25:53.84] for you. You can check them out at
[L763] [25:56.32] workos.com to learn more and get
[L764] [25:58.64] started. and I appreciate them for
[L765] [26:00.80] supporting my work and sponsoring this
[L766] [26:02.48] podcast. It sounds like on the way to
[L767] [26:05.92] generalizing
[L768] [26:07.44] uh data is a very important part of that
[L769] [26:10.40] and I was reading there's different
[L770] [26:11.60] types of data there's simulated data you
[L771] [26:14.72] could uh collect like physical
[L772] [26:16.96] interactive data and I wanted to hear
[L773] [26:20.16] your take on what's the best data to get
[L774] [26:22.72] what's the worst and what are the pros
[L775] [26:24.48] and cons. Uh this is by the way like a
[L776] [26:26.88] question that is uh I guess quite like
[L777] [26:30.00] there's a lot of discussion in the
[L778] [26:31.04] robotics community about this question
[L779] [26:32.48] and some people have like very opposite
[L780] [26:35.12] opinions on it. My own take on this is
[L781] [26:38.24] that um a lot of different data sources
[L782] [26:42.40] are easier for the model to internalize
[L783] [26:44.72] if it can ground them in a thorough
[L784] [26:47.44] physical understanding of the world. So
[L785] [26:49.52] uh let me try to explain what I mean
[L786] [26:50.72] with like a few examples. Um, if you
[L787] [26:54.00] want to learn to fly an airplane, you
[L788] [26:56.24] will probably use a a simulator, at
[L789] [26:58.32] least during part of your training. Uh,
[L790] [27:01.12] but the simulator makes a lot of sense
[L791] [27:03.52] to you because when you start using the
[L792] [27:05.68] simulator, you have a lot of world
[L793] [27:07.52] knowledge that you can use to ground
[L794] [27:09.28] what's going on. Like you know that when
[L795] [27:11.12] you uh are using the flight simulator to
[L796] [27:13.28] learn how to fly the airplane, you're
[L797] [27:14.48] not just like playing a video game.
[L798] [27:15.76] You're trying to acquire knowledge that
[L799] [27:17.36] will then that you will then use with a
[L800] [27:18.72] real airplane. and you understand that
[L801] [27:20.40] there's sort of an abstraction there.
[L802] [27:22.88] Same thing if you um uh if you're
[L803] [27:25.60] playing like a really cartoony like you
[L804] [27:27.68] know Atari game or something right like
[L805] [27:29.36] you know that all the symbols on the
[L806] [27:30.88] screen you can sort of connect them to
[L807] [27:32.56] things that you've experienced in your
[L808] [27:34.00] life and you can make an analogy there.
[L809] [27:35.84] So, a lot of that, like even though it
[L810] [27:38.64] kind of seems like these simulated
[L811] [27:40.08] environments reflect aspects of the real
[L812] [27:42.24] world, to us, they make a lot of sense
[L813] [27:44.08] because we kind of bring to bear a lot
[L814] [27:46.08] of our own prior experience and we fill
[L815] [27:48.00] in the blanks that that the that the
[L816] [27:50.00] that the simulation has. Um, and also if
[L817] [27:53.60] you if you want to use uh data uh you
[L818] [27:56.64] yourself as a person of somebody else
[L819] [27:58.72] doing something, if you you watch
[L820] [28:00.00] someone uh let's say cooking a meal,
[L821] [28:01.76] right? Um, even though you don't
[L822] [28:04.48] experience every movement they're
[L823] [28:05.84] experiencing, you have a lot of that
[L824] [28:07.20] knowledge that you bring to bear and
[L825] [28:08.24] you're like, "Okay, I see they're
[L826] [28:09.12] picking up the salt shaker. Like, I've
[L827] [28:10.48] put salt on things before, so I kind of
[L828] [28:11.84] roughly know what's going on there." And
[L829] [28:13.28] I can file it away at this level
[L830] [28:14.88] abstraction of like add salt without
[L831] [28:16.96] having to like figure out all their
[L832] [28:18.56] muscle movements. So my point with this
[L833] [28:20.40] is that once you have that understanding
[L834] [28:22.48] of how you do things physically with
[L835] [28:23.84] your own body and how you experience the
[L836] [28:25.60] physical world, now all these other
[L837] [28:27.20] sources of knowledge can be connected up
[L838] [28:28.64] to it because that foundation you get
[L839] [28:31.44] from your experience helps you ground
[L840] [28:33.20] everything. So where I'm going with this
[L841] [28:35.44] is that if we have a robotic foundation
[L842] [28:37.84] model that is trained on lots of real
[L843] [28:40.56] embodied data that provides that
[L844] [28:42.08] grounding, it might actually be much
[L845] [28:43.68] better able to absorb other sources of
[L846] [28:45.52] knowledge. And this is actually like a
[L847] [28:47.60] little bit upside down relative to how
[L848] [28:49.12] some people think about it because it's
[L849] [28:50.56] very tempting looking at the success of
[L850] [28:52.80] like internet data for LLMs to say well
[L851] [28:55.44] maybe we should do the opposite. Maybe
[L852] [28:56.80] we should like start with like YouTube
[L853] [28:58.24] videos and then put robot data on top of
[L854] [29:00.16] that. But I think it's actually the
[L855] [29:01.76] other way around. And I actually I even
[L856] [29:03.36] have like a little bit of evidence for
[L857] [29:04.48] this. So my um my colleague uh sir Saraj
[L858] [29:08.16] together with um uh Simar from Georgia
[L859] [29:11.76] Tech they had a project together uh a
[L860] [29:13.92] while back where they took our robot
[L861] [29:16.40] foundation model and they added human
[L862] [29:18.72] video data but they they didn't start
[L863] [29:21.84] with human video data. They actually
[L864] [29:22.96] started with a model train on robot data
[L865] [29:24.40] and then added video data on top of it.
[L866] [29:26.24] And what they did is they looked at the
[L867] [29:27.68] representations inside the model. Uh
[L868] [29:29.52] basically how does the model represent
[L869] [29:31.04] human experience versus robot
[L870] [29:32.56] experience? And they found that if you
[L871] [29:34.80] use a small model with a small amount of
[L872] [29:36.56] robot data, predictably the human
[L873] [29:38.24] experience and the robot experience are
[L874] [29:40.00] fully separated. Meaning that the
[L875] [29:41.28] feature representations are different.
[L876] [29:43.12] But if you train on lots of robot data
[L877] [29:44.88] from lots of different robots, then the
[L878] [29:47.44] features are grouped much more by what
[L879] [29:49.12] task is being done rather than by
[L880] [29:50.88] whether it's a human or a robot. And
[L881] [29:52.96] like when we looked at the feature
[L882] [29:54.24] plots, it was just like mindboggling
[L883] [29:55.84] because we literally when you when you
[L884] [29:57.76] crank up the amount of robot data to
[L885] [29:58.96] 100%, they just line up perfectly. like
[L886] [30:01.28] you you see the you know you do this TC
[L887] [30:03.36] embedding you see the shapes of the
[L888] [30:04.56] embeddings and it's just all task
[L889] [30:07.20] identity and like minimal sensitivity to
[L890] [30:09.44] embodiment and to me that's kind of
[L891] [30:11.44] mind-blowing because like this the base
[L892] [30:13.28] model wasn't trained on any human data
[L893] [30:14.72] at all but once you start adding human
[L894] [30:16.56] data it represents it exactly the same
[L895] [30:18.72] way and I think that's really exciting
[L896] [30:20.96] and I think that that to me is like one
[L897] [30:22.56] one of the strongest indicators that if
[L898] [30:24.24] you have that good foundation of robot
[L899] [30:25.76] experience you can put everything else
[L900] [30:27.28] on top of it and it's actually better at
[L901] [30:28.48] absorbing that
[L902] [30:29.68] >> is it important that that base model has
[L903] [30:33.12] data that was collected using that
[L904] [30:35.60] specific set of motors, specific set of
[L905] [30:37.84] joints. So far, we've uh obviously put a
[L906] [30:42.08] lot of effort into cross embodyment
[L907] [30:43.36] models that can handle many different
[L908] [30:44.56] robot types, but generally you do need
[L909] [30:47.44] data of the robot you're going to be
[L910] [30:48.72] deploying on to get good performance. Uh
[L911] [30:51.68] so kind of the metric of uh of
[L912] [30:53.84] generalization there is not can you zero
[L913] [30:55.52] shot a new robot but it's mostly can you
[L914] [30:57.84] get away with less experience from the
[L915] [30:59.84] new robot and transfer skills from other
[L916] [31:01.60] robots. Okay so that's the current state
[L917] [31:03.36] of things. Now there is a little bit of
[L918] [31:05.04] a kind of surprisingly positive read on
[L919] [31:07.60] that which is even though you need data
[L920] [31:09.76] from these robots um the amount of
[L921] [31:12.56] special stuff that the model is doing is
[L922] [31:15.12] uh kind of minimal. Like when we started
[L923] [31:17.60] doing all of this, I had like a big long
[L924] [31:19.68] list of all the cool research I wanted
[L925] [31:21.36] to do to better accommodate different
[L926] [31:22.64] morphologies like can you like
[L927] [31:24.64] factoriize the model's representation in
[L928] [31:26.80] some way so that there's like a you know
[L929] [31:28.72] a six degree of freedom arm head and a
[L930] [31:30.88] seven degree head and a gripper head
[L931] [31:32.40] etc. We didn't do any of that like we
[L932] [31:33.76] the model just outputs like a big vector
[L933] [31:35.28] of numbers. Uh if the robot has less
[L934] [31:37.44] degrees of freedom than the number it
[L935] [31:39.04] outputs it just zero pads it. There's
[L936] [31:40.56] just like nothing fancy. Uh and that's
[L937] [31:42.96] it. and then it just train on all the
[L938] [31:44.40] robots and outputs the correct actions
[L939] [31:47.04] based on what is seeing through the
[L940] [31:48.08] camera essentially.
[L941] [31:49.84] But now to to your point about whether
[L942] [31:51.68] you can uh handle new robots. Um so so
[L943] [31:56.32] far the thing that we focused on and I
[L944] [31:58.40] think this is showing some promise is to
[L945] [32:01.76] be able to transfer skills between
[L946] [32:03.36] robots and this is actually where
[L947] [32:07.52] the um particular choices in how the
[L948] [32:10.00] model works uh seem to matter. Um for
[L949] [32:13.68] example uh you can have a model that
[L950] [32:17.68] does some intermediate thinking and that
[L951] [32:20.48] thinking can be done in different
[L952] [32:21.52] modalities. So you can think in text and
[L953] [32:23.28] thinking in text is really good for
[L954] [32:24.80] transferring um highle behavioral
[L955] [32:27.12] structure. So that's basically how you
[L956] [32:29.52] understand that hey if I want to like
[L957] [32:31.20] clean the kitchen and put away like the
[L958] [32:33.28] silverware first open the drawer like
[L959] [32:34.88] that's kind of a semantic inference and
[L960] [32:36.08] you can transfer that uh very well
[L961] [32:38.00] because obviously that's like largely
[L962] [32:39.20] agnostic to any embodiment or anything
[L963] [32:40.64] like that. But even lower level things
[L964] [32:42.64] can be transferred if you use the right
[L965] [32:44.64] representation. So one experiment we did
[L966] [32:46.64] is we had a a thinking stage that is
[L967] [32:49.76] expressed in images where you basically
[L968] [32:51.92] like dream up an image of the next
[L969] [32:54.16] milestone in the task. And with that, we
[L970] [32:56.88] could actually get um a robot, the UR5
[L971] [33:00.00] robot to fold a t-shirt, even though we
[L972] [33:02.16] didn't have any t-shirt folding data on
[L973] [33:03.44] the UR5 because while getting the the
[L974] [33:05.52] the arm motions correct is very hard
[L975] [33:07.68] because the robot basically requires
[L976] [33:09.04] very different joint angles to do the
[L977] [33:10.40] task, uh cooking up an image of what it
[L978] [33:12.64] looks like for it to fold a shirt is not
[L979] [33:14.32] that hard because like you've seen the
[L980] [33:15.44] robot arm in all sorts of different
[L981] [33:16.56] poses. You've seen the shirt in all
[L982] [33:18.40] different stages of being folded and
[L983] [33:19.52] unfolded. You know roughly where it
[L984] [33:20.72] should hold it. So getting a good
[L985] [33:22.56] generative model to cook up that image
[L986] [33:24.08] is pretty straightforward. And once you
[L987] [33:25.84] have the image then from that backing
[L988] [33:28.08] out the correct actions is easy too
[L989] [33:30.08] because you can just look at the
[L990] [33:31.36] synthesized arm angle and just like back
[L991] [33:33.44] out what the angle should be. So it it's
[L992] [33:36.16] it's not changing the problem but it's
[L993] [33:37.84] just introducing this intermediate step
[L994] [33:39.84] that makes it easier to solve. Just like
[L995] [33:41.52] if you're solving a math problem if you
[L996] [33:42.96] figure out like the right intermediate
[L997] [33:44.80] step kind of the answer is obvious from
[L998] [33:46.56] that intermediate step. And I think
[L999] [33:48.32] that's really exciting because now now
[L1000] [33:49.76] that shows that this level of
[L1001] [33:51.36] generalization across robots and I'm
[L1002] [33:53.28] sure other generalization too can be
[L1003] [33:54.56] facilitated with thinking just like an
[L1004] [33:56.56] LLMs but with a twist. You have to think
[L1005] [33:58.72] in the right modality.
[L1006] [34:00.56] >> Interesting. So it it outputs a I guess
[L1007] [34:03.12] that image is what its video sensor is
[L1008] [34:07.44] seeing and it's like the next step.
