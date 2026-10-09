Chunk 3; segments 695–1058. Start may repeat the previous chunk for context.

# Meta Superintelligence Labs (MSL) Eng Director: Promo Hacking, Industry Shifts, Regrets | John White

Source ID: source-f7b2e4e29d371333
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Meta_Superintelligence_Labs_(MSL)_Eng_Director_Promo_Hacking,_Industry_Shifts,_Regrets_John_White_en.txt
Video: https://www.youtube.com/watch?v=aPfnP4iAIH8

[L704] [21:14.96] a big tech company, and you just give it
[L705] [21:17.32] to everyone in the industry, and it
[L706] [21:19.08] actually creates like a billion-dollar
[L707] [21:20.76] companies pretty I it's it's hard, but
[L708] [21:23.28] at least the product market fit and idea
[L709] [21:25.92] part are relatively solved since it's
[L710] [21:28.16] creating so much value for these big
[L711] [21:29.60] companies. For this podcast, I produce
[L712] [21:31.88] transcripts for every episode for
[L713] [21:33.68] convenient skimming, and I built a
[L714] [21:35.68] custom tool to automate that.
[L715] [21:37.64] Recently, I noticed in the Barbara
[L716] [21:39.44] Liskov transcript, my simple
[L717] [21:41.88] speech-to-text tool was getting a lot of
[L718] [21:43.68] things wrong. For instance, the CLU
[L719] [21:45.60] programming language is spelled all caps
[L720] [21:47.96] c l u, not clue.
[L721] [21:50.56] So, to fix this, I used Cursor 3, picked
[L722] [21:53.40] the strongest version of Opus 4.7 extra
[L723] [21:56.52] high, and had an agent make a plan to
[L724] [21:58.44] fix that. And while I was waiting, I
[L725] [22:00.40] figured I'd trigger a few more agents
[L726] [22:01.84] for code cleanups and front-end
[L727] [22:03.40] improvements.
[L728] [22:04.60] Um it generated a reasonable plan with
[L729] [22:06.60] rich system diagrams. It applied all the
[L730] [22:09.16] changes within minutes, and worked on
[L731] [22:11.20] the first try.
[L732] [22:12.44] So, if you want to build something with
[L733] [22:13.96] the flexibility of sending off a bunch
[L734] [22:15.84] of agents with frontier models of your
[L735] [22:17.72] choice, you can go to cursor.com to try
[L736] [22:20.84] out Cursor 3.
[L737] [22:22.52] You know, I saw before you worked at
[L738] [22:23.80] Meta, you were working on the Julia
[L739] [22:25.72] programming language, and I actually
[L740] [22:27.48] wasn't familiar about it. So, I I read
[L741] [22:29.24] into it a little bit, and looks like it
[L742] [22:30.96] was part of these data science language
[L743] [22:34.00] wars, basically, where there was R
[L744] [22:36.80] versus Julia versus Python. What is
[L745] [22:41.68] Julia, and what what is the context on
[L746] [22:43.80] that war there?
[L747] [22:45.36] >> Yeah, well, certainly, I think I made it
[L748] [22:47.24] more of a part of the war. I don't think
[L749] [22:48.96] it had to necessarily be part of it. Uh
[L750] [22:51.28] although, I do think also, like, the
[L751] [22:52.56] simple fact of the reality is, like,
[L752] [22:54.16] programming languages are products, and
[L753] [22:55.60] products exist in an ecosystem where
[L754] [22:57.12] they're in zero-sum competition, and
[L755] [22:59.16] claiming claiming that they're not in
[L756] [23:00.48] zero-sum competition is like a very cute
[L757] [23:02.12] thing people say is appropriate, but
[L758] [23:03.68] it's clearly false and I think just
[L759] [23:05.44] makes everyone worse by misleading them.
[L760] [23:07.64] Um but like um
[L761] [23:10.12] I mean so Julia for me and it's actually
[L762] [23:12.12] sort of why did Julia so so appealing? I
[L763] [23:14.04] mean
[L764] [23:14.84] for me what Julia's pitch was like we
[L765] [23:17.12] should be able to write code in a
[L766] [23:18.88] high-level language that looks like
[L767] [23:20.40] Python or like MATLAB, which is really
[L768] [23:22.64] the language it was originally designed
[L769] [23:24.12] to destroy. It was really designed to
[L770] [23:25.72] get rid of MATLAB. Uh it was made by MIT
[L771] [23:28.32] math people who wanted to get rid of
[L772] [23:29.84] MATLAB. Um and it really like targeted
[L773] [23:32.88] that market much more than data science.
[L774] [23:34.48] It started in the sort of I think I was
[L775] [23:35.80] involved in pushing it towards data
[L776] [23:37.36] science. But you know, to me the thing I
[L777] [23:39.32] would do when I give talks about Julia
[L778] [23:40.56] if you're like, "Listen, let's look at
[L779] [23:42.44] the R function for distance like compute
[L780] [23:44.92] a distance matrix between a bunch of
[L781] [23:46.96] vectors." So you're like, you know,
[L782] [23:48.00] pairs of vectors and you get all the
[L783] [23:49.40] distance matrix.
[L784] [23:51.20] Um
[L785] [23:52.60] if you look at the like that function
[L786] [23:54.76] and then you actually try to figure out
[L787] [23:55.60] how it's implemented in R, what you find
[L788] [23:58.04] is like C code that is a very reasonable
[L789] [24:01.44] C code that is just a bunch of for loops
[L790] [24:03.52] like you know, loop through all the rows
[L791] [24:05.28] and all the columns and then compute the
[L792] [24:06.92] distance at that row and you're done.
[L793] [24:09.72] If you basically take that code verbatim
[L794] [24:11.96] and just trans like translate it naively
[L795] [24:14.24] into R,
[L796] [24:15.48] you're going to take some type
[L797] [24:16.36] information away. You're going to get
[L798] [24:17.56] rid of some like ints and float
[L799] [24:18.96] signatures, but otherwise you're going
[L800] [24:20.56] to basically write for loops that look
[L801] [24:22.12] exactly the same.
[L802] [24:23.60] The R code is going to be like somewhere
[L803] [24:25.16] between 1,000 to 10,000 times slower
[L804] [24:27.48] than C.
[L805] [24:28.64] And this to me was the thing that just
[L806] [24:29.76] like drove me insane when I'm just like,
[L807] [24:31.36] wait, what? Like these two programs are
[L808] [24:34.20] like 80% the same.
[L809] [24:36.88] Why is one not as fast? And Julia really
[L810] [24:40.12] was all about this notion that like that
[L811] [24:41.64] was unacceptable. And that's what made
[L812] [24:43.16] it so appealing when the first pound
[L813] [24:44.68] like the first post by the original
[L814] [24:46.08] founders went out. I was like, "Oh, you
[L815] [24:48.36] guys are doing the thing I wanted people
[L816] [24:49.80] to do." Which is like
[L817] [24:53.04] not claim that it is impossible to make
[L818] [24:55.40] high-level languages fast.
[L819] [24:57.28] Which is like so much of actually how
[L820] [24:59.04] the Python R community sometimes behave
[L821] [25:01.04] is to be like, "Oh, well,
[L822] [25:02.76] we can't be fast, but also fast isn't
[L823] [25:04.40] important." And to me, like that that
[L824] [25:06.04] double hit of like, "Well, we can't be
[L825] [25:07.64] it, and it's not important." really
[L826] [25:09.08] didn't work for me. So, Julia really
[L827] [25:11.16] resonated. I think I probably as the
[L828] [25:13.92] guilty party of trying to make it more
[L829] [25:15.68] part of the data science world is cuz I
[L830] [25:17.28] was myself a heavy user of R and was
[L831] [25:19.52] just so disappointed in R. Um just so
[L832] [25:23.52] incredibly disappointed in how often I
[L833] [25:25.68] would try to do a project and R just
[L834] [25:28.72] like fought me at every step of the way.
[L835] [25:31.12] Um
[L836] [25:32.36] but Python is also like this. I mean, if
[L837] [25:33.80] you look at all the really great
[L838] [25:34.92] libraries like PyTorch, like, you know,
[L839] [25:36.76] deep down at the end of the day, you're
[L840] [25:38.04] going to look at C++ code or maybe even
[L841] [25:39.84] looking at like handwritten assembly or
[L842] [25:42.00] handwritten like kernels for GPUs.
[L843] [25:45.08] Um or at least you're looking at
[L844] [25:46.32] something written in a much lower-level
[L845] [25:47.92] language. Um and so, Julia was really
[L846] [25:50.52] like about trying to solve that. And I
[L847] [25:52.44] don't think it totally won, which I
[L848] [25:53.88] think is probably why you didn't know
[L849] [25:54.84] about it. I think it was very hip at one
[L850] [25:56.32] point and has become less hip, but it's
[L851] [25:57.96] actually doing okay. Like it's I think
[L852] [25:59.84] it's in the top 25 programming languages
[L853] [26:02.00] by users in the world. So, I think it's
[L854] [26:03.44] a
[L855] [26:04.16] real a real language
[L856] [26:05.92] um that's really out there.
[L857] [26:07.96] But for me, the thing that really
[L858] [26:08.76] matters, even though I don't know that
[L859] [26:10.04] it's killing it, Julia is like the only
[L860] [26:12.12] people still actually fighting that
[L861] [26:13.96] fight.
[L862] [26:15.20] >> What's the intuition behind why R is
[L863] [26:18.24] 10,000 times slower when the code is,
[L864] [26:20.92] you know, the symbols are relatively
[L865] [26:22.24] similar to the C?
[L866] [26:23.72] >> Fundamentally, any code that is slow is
[L867] [26:25.52] slow cuz it's doing stuff it doesn't
[L868] [26:26.80] need to do. Like that's just sort of the
[L869] [26:28.12] most basic fact about slow code is that
[L870] [26:30.24] the reason you're slow is cuz you could
[L871] [26:31.56] have done something else and you did
[L872] [26:33.00] something slower instead. And something
[L873] [26:35.92] like R is doing this pretty easy. It's
[L874] [26:37.84] in Python. It's not quite as dire, but
[L875] [26:39.60] it's still there is
[L876] [26:42.04] you wind up paying an enormous amount of
[L877] [26:44.24] overhead cost for the possibility that
[L878] [26:46.32] someone might do something more dynamic.
[L879] [26:49.48] And because they might do it. And to
[L880] [26:50.96] give you an example, which is really
[L881] [26:52.44] astonishing about R is in R for instance
[L882] [26:55.16] the brace that you use to ins- to find a
[L883] [26:57.60] block is an operator that can be
[L884] [26:59.96] overridden and the user can redefine.
[L885] [27:02.92] So they can make braces mean something
[L886] [27:04.56] else. But so that means when you see a
[L887] [27:06.68] brace in code, you can't just be like, I
[L888] [27:08.56] know what this is, I can move on. You
[L889] [27:10.92] have to be like, no, I need to look up
[L890] [27:12.52] and check did the user redefine this?
[L891] [27:15.36] Um
[L892] [27:16.52] I think it I think it's brace and not
[L893] [27:18.08] parenthesis, but it's been a while, so I
[L894] [27:19.36] haven't double checked. But it may also
[L895] [27:20.72] be parenthesis or it's possible I
[L896] [27:22.16] flipped them. We can like, you know,
[L897] [27:23.60] check offline and see whether my memory
[L898] [27:25.04] is good. But like you just wind up with
[L899] [27:26.72] so much stuff like this that is so like
[L900] [27:29.88] maybe changed and you don't know whether
[L901] [27:32.00] it changed, so you need to go check
[L902] [27:33.96] whether it changed. And the checks are
[L903] [27:35.80] very expensive, especially if you're
[L904] [27:37.36] doing something like adding two 60-bit
[L905] [27:40.04] 64-bit integers. That's like one machine
[L906] [27:43.40] cycle, like it is one machine cycle. But
[L907] [27:46.56] a check like does addition still mean
[L908] [27:48.60] whatever I think it is could be hundreds
[L909] [27:50.20] to thousands of machine cycles. And so
[L910] [27:52.72] you wind up like swapping in things that
[L911] [27:54.32] are very inefficient.
[L912] [27:56.72] Places that you don't need. And this is
[L913] [27:58.08] particularly R is amazing like there's
[L914] [27:59.60] this amazing paper
[L915] [28:01.60] by a couple of students uh and a a
[L916] [28:04.64] senior professor named Jan Vitek, but
[L917] [28:07.12] it's about the design uh called
[L918] [28:08.84] something like uh evaluating design of
[L919] [28:10.76] the R programming language.
[L920] [28:12.44] And one of the things they look at is
[L921] [28:13.80] like especially R has an especially
[L922] [28:15.36] tricky thing, which is unlike Python, R
[L923] [28:17.24] is also a lazily evaluated language,
[L924] [28:20.12] where the arguments to functions are not
[L925] [28:21.84] evaluated before you start the function
[L926] [28:23.48] body. They wait until the function kicks
[L927] [28:25.64] off and they just are passed as promise
[L928] [28:27.80] objects.
[L929] [28:29.00] And what they look at is they look at
[L930] [28:30.72] like, well, how often are these promises
[L931] [28:33.76] could have been effect like eagerly
[L932] [28:35.40] evaluated? And how often is the overhead
[L933] [28:37.28] of these promises worth it? And their
[L934] [28:38.64] conclusion is like 70% or maybe more,
[L935] [28:41.28] maybe it's 90%. I forget the numbers.
[L936] [28:43.72] You basically have no reason you needed
[L937] [28:45.28] to do this. Like almost never do you
[L938] [28:47.04] need this.
[L939] [28:48.12] But, you actually pay like an enormous
[L940] [28:50.00] overhead cost for having agreed to do
[L941] [28:51.68] this. Um and a good example I say in
[L942] [28:53.80] Python also is like
[L943] [28:55.48] in Python
[L944] [28:56.72] you can like manipulate the symbol table
[L945] [28:59.08] using using functions in the inspect
[L946] [29:01.12] module.
[L947] [29:02.52] And so, what that means is like you can
[L948] [29:04.36] never be sure of what something's bound
[L949] [29:06.60] to. You always have to be afraid and
[L950] [29:08.64] check.
[L951] [29:09.64] Um and just sort of general the lack of
[L952] [29:11.44] invariants that like that's what makes a
[L953] [29:13.28] language fast. It's like you have a lots
[L954] [29:14.64] of invariants. What makes your language
[L955] [29:16.08] slow is you have lots of stuff you might
[L956] [29:18.36] have to go confirm at runtime.
[L957] [29:20.84] And R is just incredibly pervasively
[L958] [29:23.32] like this.
[L959] [29:24.40] >> I looked at some of your popular past
[L960] [29:26.80] tweets and I thought maybe we could
[L961] [29:28.56] discuss some of them. So, one of them
[L962] [29:31.04] this is the most popular tweet that I
[L963] [29:33.08] think you ever wrote. And you you said
[L964] [29:35.84] that you're continually continually
[L965] [29:38.96] disappointed by how many grad students
[L966] [29:42.08] and postdocs get the impression that
[L967] [29:44.40] industry is a safe position of last
[L968] [29:46.72] resort that they can always fall back on
[L969] [29:49.40] if things sour in their academic
[L970] [29:51.68] careers. And
[L971] [29:53.48] I thought that was interesting because I
[L972] [29:54.72] thought the
[L973] [29:55.80] I thought the opposite was also very
[L974] [29:57.56] commonly true where people might you
[L975] [29:59.96] know, want to avoid industry so they go
[L976] [30:02.08] and get higher education. So, I'm
[L977] [30:03.56] curious your you know, your thought on
[L978] [30:05.56] this and what what made you think this.
[L979] [30:07.96] >> Really what drove me nuts was there were
[L980] [30:09.92] just a ton of people
[L981] [30:11.92] who fundamentally wanted to be
[L982] [30:13.32] professors or postdocs and were in a PhD
[L983] [30:16.00] program.
[L984] [30:17.24] And they were like, "Well, if I fail
[L985] [30:19.16] out, I'll go into industry."
[L986] [30:21.64] Um
[L987] [30:22.84] and this like
[L988] [30:24.80] one is that you would interact with
[L989] [30:26.16] people during interviews who like
[L990] [30:27.84] clearly didn't want to be there. Just
[L991] [30:29.56] like so unambiguously did not want to be
[L992] [30:32.12] there and clearly viewed this as like a
[L993] [30:34.00] failure that they were interviewing.
[L994] [30:36.04] And you're like, "Well, that's not
[L995] [30:37.44] really like a positive sign that we want
[L996] [30:39.12] to hire someone who like doesn't seem
[L997] [30:40.96] like they're going to enjoy the job.
[L998] [30:43.00] But
[L999] [30:44.16] in addition a bunch of people, and this
[L1000] [30:45.40] is what drove me so insane cuz I think
[L1001] [30:47.00] it's like all parties involved in the
[L1002] [30:48.64] academic system hurt students doing
[L1003] [30:50.40] this,
[L1004] [30:51.28] is that like
[L1005] [30:52.72] so many people just assume that when
[L1006] [30:54.32] they finally decided to get industry
[L1007] [30:56.12] position, it was going to be trivial.
[L1008] [30:58.60] And then they didn't find it trivial. I
[L1009] [31:00.60] think a lot of academic people were
[L1010] [31:01.64] like, well, smart people are in academia
[L1011] [31:03.56] and the dumb people are in industry. So,
[L1012] [31:05.52] if I need to go compete with the dumb
[L1013] [31:06.72] people, it will be easy.
[L1014] [31:08.64] Um and I think there was a lot of that.
[L1015] [31:11.76] Um you know, there was a person who was
[L1016] [31:12.56] I'll give you an example. There was a
[L1017] [31:13.36] person who was like effectively a CS
[L1018] [31:15.28] professor who I interviewed.
[L1019] [31:17.24] And this person like could not figure
[L1020] [31:19.24] out how to pass a values between the
[L1021] [31:20.96] various functions that they were calling
[L1022] [31:22.52] in the interview. Like literally they
[L1023] [31:24.08] were like, what I would do is I would
[L1024] [31:25.36] call this function and it would print
[L1025] [31:26.92] out in the REPL, and then I would read
[L1026] [31:28.88] it as a human, and then I would go like
[L1027] [31:30.96] type it into this other piece of code.
[L1028] [31:33.40] And I was like, oh, you you are better
[L1029] [31:35.92] programming than this, right? Cuz like
[L1030] [31:37.72] you're a professor of computer science.
[L1031] [31:40.28] And they're like, no, no, this is how I
[L1032] [31:41.44] work. And I was like, well,
[L1033] [31:43.52] this is not going to set you up for
[L1034] [31:45.04] success if we actually have to get you
[L1035] [31:46.60] writing code in prod here.
[L1036] [31:48.76] >> I saw a few other popular tweets that
[L1037] [31:51.16] you had. They were about um
[L1038] [31:53.80] like favorite statistics papers and
[L1039] [31:55.88] favorite recommendations of statistical
[L1040] [31:57.92] books that you're saying, oh, everyone's
[L1041] [31:59.44] got to read these.
[L1042] [32:00.88] How come you have such strong
[L1043] [32:02.08] recommendations on statistical uh
[L1044] [32:04.36] literature? And then also, what are
[L1045] [32:06.16] those recommendations?
[L1046] [32:07.60] >> I love statistics. I think I'll never
[L1047] [32:09.40] not love it, but I think it's the
[L1048] [32:10.44] craziest and what I mean by craziest
[L1049] [32:14.04] it's a field that fundamentally sells
[L1050] [32:16.12] people the idea that they can use
[L1051] [32:17.64] statistical methods in real life.
[L1052] [32:20.12] But in reality, what they do is do pure
[L1053] [32:22.28] mathematics and study how statistical
[L1054] [32:24.64] methods work in a idealized theoretical
[L1055] [32:26.92] world.
[L1056] [32:28.12] And
[L1057] [32:29.36] in pure math, like you know, as an
[L1058] [32:30.72] undergraduate I did pure math and I
[L1059] [32:32.00] loved things like number theory. In pure
[L1060] [32:33.84] math, it's just you just pure, it's
[L1061] [32:35.44] pure. You prove it, it's internally
[L1062] [32:37.52] coherent, there's no attempt to like
[L1063] [32:39.40] reconcile with reality. Reality doesn't
[L1064] [32:41.76] even matter. You just like there's a
[L1065] [32:43.12] rules, we follow the rules, we're in
[L1066] [32:44.76] this internally consistent system.
[L1067] [32:47.36] And then in super applied fields like
