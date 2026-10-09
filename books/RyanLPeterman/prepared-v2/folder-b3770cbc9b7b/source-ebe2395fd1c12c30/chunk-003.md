Chunk 3; segments 679–1031. Start may repeat the previous chunk for context.

# Mozilla Firefox CTO: Chrome vs Firefox and Distinguished Eng Promos

Source ID: source-ebe2395fd1c12c30
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Mozilla_Firefox_CTO_Chrome_vs_Firefox_and_Distinguished_Eng_Promos_en.txt
Video: https://www.youtube.com/watch?v=KhJgI9u47kI

[L688] [25:16.24] without thinking too hard I fired off an
[L689] [25:18.08] email to this guy being like hey like
[L690] [25:19.92] you're you're double crossing us right
[L691] [25:21.28] like you're not supposed to sell these
[L692] [25:22.80] things if you report them to us and he
[L693] [25:26.48] got back to me and the thing about
[L694] [25:27.44] security researchers is that they're
[L695] [25:28.72] extremely paranoid he's like no no no I
[L696] [25:30.48] didn't this must mean that my devices
[L697] [25:33.20] must be compromised at a very deep
[L698] [25:34.56] level. And the only thing I can think to
[L699] [25:36.72] do here is to go off the grid. And
[L700] [25:40.88] we then discovered a basically like an
[L701] [25:44.40] hour later that actually it was Mozilla
[L702] [25:46.80] that had been compromised that Bugzilla,
[L703] [25:48.40] our bug tracker, had been compromised by
[L704] [25:49.92] a thread actor. And I tried to write
[L705] [25:51.84] back to the researcher, but at that
[L706] [25:52.96] point he'd already gone offline and we
[L707] [25:54.80] couldn't reach him. And so it was
[L708] [25:57.28] several weeks later that we got a phone
[L709] [25:59.36] call from a bowling alley in upstate New
[L710] [26:01.76] York where this researcher had gone into
[L711] [26:03.92] hiding and was trying to, you know,
[L712] [26:06.32] throw off the people that were after
[L713] [26:07.60] him. And we managed to explain that
[L714] [26:09.36] actually, sorry, this was our bad and
[L715] [26:11.20] had to help him get back on his feet.
[L716] [26:13.36] But it was a really big problem that
[L717] [26:16.72] Bugzilla had been compromised because
[L718] [26:19.60] that is where you have the records of
[L719] [26:22.96] all of the interesting security attacks
[L720] [26:25.04] that people have discovered against the
[L721] [26:26.32] browser. But the amazing thing was that
[L722] [26:29.20] Slaughterhouse had just wrapped up and
[L723] [26:31.28] that out of I think 45 of the I don't
[L724] [26:35.52] know something on the order of 45 of the
[L725] [26:37.36] bugs that the thread actor had um
[L726] [26:40.48] excfiltrated, we had fixed all but two
[L727] [26:43.04] of them. And with this sort of new
[L728] [26:45.20] architecture that basically fixed it.
[L729] [26:47.04] And so that really impressed upon me the
[L730] [26:50.00] importance of getting ahead of things on
[L731] [26:52.32] security and making sure that you have
[L732] [26:53.68] the right architecture because sometimes
[L733] [26:55.36] you find you're in a self a situation
[L734] [26:57.28] where you don't have the luxury of the
[L735] [26:58.80] time to fix it.
[L736] [27:00.40] >> How'd you know that that security
[L737] [27:02.40] researcher wrote that vulnerability?
[L738] [27:05.36] >> People have very particular styles and
[L739] [27:08.56] in this particular area of security or
[L740] [27:12.00] of exploits which is which is different
[L741] [27:13.36] than other kinds. Um, there was just a
[L742] [27:16.48] lot of people's fingerprints on it,
[L743] [27:18.64] right? You could tell because these were
[L744] [27:20.24] things that were handwritten logic
[L745] [27:23.28] attacks where you were using very
[L746] [27:25.76] particular parts of like I'm going to
[L747] [27:27.04] take this API and then I'm going to bind
[L748] [27:28.80] this function to it and then I'm going
[L749] [27:30.56] to send this call like around async
[L750] [27:32.56] through the event loop twice and then
[L751] [27:34.24] I'm going to do this, right? Like there
[L752] [27:35.68] was a very particular way and these were
[L753] [27:37.20] all handwritten. There is a different
[L754] [27:39.76] type of security attack that was also a
[L755] [27:42.96] major issue at the time which were
[L756] [27:45.44] memory safety vulnerabilities and these
[L757] [27:48.08] were much less of a artisal thing and
[L758] [27:51.92] more things that you would produce by
[L759] [27:53.12] tools particularly by fuzzing tools. And
[L760] [27:56.08] so this was also a major issue that um
[L761] [27:59.92] Mozilla was grappling with because he
[L762] [28:01.52] would have people who would run these
[L763] [28:02.72] fuzzers against the codebase and the
[L764] [28:04.80] codebase was written in C++ and there
[L765] [28:07.92] are lots of ways to have memory hazards
[L766] [28:09.44] in C++ and really any one of them is the
[L767] [28:12.32] sort of like web page takes over your
[L768] [28:13.84] computer situation and so we were really
[L769] [28:18.88] struggling to find ways to deal with
[L770] [28:21.20] that in a robust manner. Um, and that
[L771] [28:24.40] was really one of the things that
[L772] [28:25.68] motivated Mozilla's investment in Rust.
[L773] [28:28.96] >> So I could see and I'm just trying to
[L774] [28:31.28] understand here the the security issue
[L775] [28:33.44] here is there's some front-end code that
[L776] [28:37.04] abuses or does some special path in
[L777] [28:39.68] Firefox and then can take over Firefox
[L778] [28:42.64] in that case in the past. But how does
[L779] [28:44.96] it take over the computer? Wouldn't the
[L780] [28:46.88] operating system kind of shield um
[L781] [28:49.84] ideally from Firefox doing crazy stuff?
[L782] [28:53.84] >> So certainly not at the time like
[L783] [28:55.92] originally particularly on Windows
[L784] [28:58.00] applications largely ran with system
[L785] [28:59.76] privileges and if you took over the you
[L786] [29:02.24] know the the classic thing that security
[L787] [29:03.92] researchers would do to prove that
[L788] [29:05.20] they'd pawned your machine was to launch
[L789] [29:06.72] the calculator um like the Windows
[L790] [29:08.72] calculator right and so you'd run this
[L791] [29:10.40] exploit you really have to trust the
[L792] [29:12.00] person who sent it to you that it wasn't
[L793] [29:13.36] going to do anything bad but you know
[L794] [29:14.56] calc.exe exe that was that was the
[L795] [29:16.56] proof. As time went on and you know
[L796] [29:19.92] Chrome had a major hand in improving the
[L797] [29:24.08] table stakes of how browsers worked,
[L798] [29:26.40] there were additional layers of
[L799] [29:27.60] protection that were put on, right? And
[L800] [29:29.20] so some of these include inprocess
[L801] [29:30.80] sandboxing um as well as operating
[L802] [29:33.44] system level sandboxing. And so the
[L803] [29:36.96] architecture that browsers like Firefox
[L804] [29:39.60] and Chrome have today involves a very
[L805] [29:43.28] you know defense in-depth multiple level
[L806] [29:45.28] of uh multiple levels of protection
[L807] [29:48.80] including operating system level
[L808] [29:50.32] sandboxing that is applied um to things
[L809] [29:52.88] like you know the the rendering and
[L810] [29:54.32] content processes.
[L811] [29:56.24] That said, this was all bolted on over
[L812] [29:58.96] time on Windows. And Windows, unlike an,
[L813] [30:02.40] you know, a platform like iOS. Um, iOS
[L814] [30:05.84] is designed from the beginning with an
[L815] [30:07.44] an with an application sandboxing model
[L816] [30:09.60] where applications are just applications
[L817] [30:11.28] and they have their own little world.
[L818] [30:13.12] That was not how Windows worked. And so
[L819] [30:15.84] evolving Windows and evolving the
[L820] [30:17.60] security critical applications that sit
[L821] [30:19.36] on top of Windows like browsers to deal
[L822] [30:22.00] with these sorts of attacks is honestly
[L823] [30:23.44] an ongoing challenge. Did you ever
[L824] [30:25.12] figure out how a Bugzilla was
[L825] [30:26.56] compromised?
[L826] [30:27.76] >> I I think it was a credential leak from
[L827] [30:30.08] an employee like that. I I'm 85% sure
[L828] [30:33.60] that that's what it was. And that was I
[L829] [30:35.28] think before we had things like
[L830] [30:36.40] two-factor authentication um for logging
[L831] [30:38.24] into Bugzilla. You know, Bugzilla was a
[L832] [30:39.60] very old tool that dated back into the
[L833] [30:41.12] 90s. And so similarly, it was something
[L834] [30:42.80] that had to evolve with the threats over
[L835] [30:44.40] time.
[L836] [30:45.52] >> One thing that I was curious about is as
[L837] [30:48.24] an organization,
[L838] [30:50.16] how do you prioritize security? Because
[L839] [30:53.20] for instance at the time there was also
[L840] [30:55.68] these big investments in performance and
[L841] [30:58.56] I'm sure there was a bunch of other
[L842] [30:59.76] things
[L843] [31:00.64] >> for sure. Yeah. Security is one of those
[L844] [31:03.44] long-term things that is very easy to
[L845] [31:06.00] take a short-term perspective on and
[L846] [31:07.76] ignore and that is perhaps a decision
[L847] [31:11.68] that some products will make uh given
[L848] [31:14.72] where they are but it's not something
[L849] [31:16.00] that you can do as a long-term browser.
[L850] [31:18.24] And so honestly from my perspective it's
[L851] [31:20.24] a cultural thing at Mozilla that from
[L852] [31:22.64] the very beginning back before there was
[L853] [31:24.48] any sort of management structure and
[L854] [31:26.40] performance measurement and you know
[L855] [31:28.56] company objectives it was just
[L856] [31:31.36] understood that we had an obligation to
[L857] [31:34.40] protect our users and to keep them safe
[L858] [31:36.80] and I think that persists
[L859] [31:40.16] that means that there's a lot of I would
[L860] [31:42.08] say ongoing bottomup energy towards
[L861] [31:44.96] making sure that we improve security And
[L862] [31:47.84] there's a lot of pride that people at
[L863] [31:49.76] Mosilla take in the security of Firefox.
[L864] [31:52.72] Um because Firefox does not have you
[L865] [31:55.52] know I think that the Chrome security
[L866] [31:56.88] org you know on its own is like on the
[L867] [31:59.68] order of you know 70 plus people and we
[L868] [32:02.40] don't have anything close to that but it
[L869] [32:04.08] is considered to be a shared
[L870] [32:05.12] responsibility and we have a lot of
[L871] [32:06.40] people who are very dedicated to that
[L872] [32:08.24] and trying to think ahead right like
[L873] [32:10.24] slaughterhouse the project that I led
[L874] [32:12.24] that was not any kind of top- down edict
[L875] [32:14.64] of we need to go fix this it was that I
[L876] [32:16.40] was responsible for the code and I felt
[L877] [32:18.80] that this was important that we needed
[L878] [32:20.72] to get it right And one of the things
[L879] [32:23.36] that I'm very proud of at Mozilla today
[L880] [32:25.28] is that um there are there's an annual
[L881] [32:28.96] security um competition called Pone to
[L882] [32:31.84] Own where researchers show up and
[L883] [32:36.40] test their exploits and receive prizes
[L884] [32:38.40] for compromising the browsers. And
[L885] [32:39.92] generally speaking, they always find a
[L886] [32:41.36] way to compromise every browser, right?
[L887] [32:42.88] Like no browser is perfectly secure. And
[L888] [32:46.56] Firefox for the last two years has won
[L889] [32:48.88] the award of being fastest to patch um
[L890] [32:51.60] within you know on the order of 24
[L891] [32:54.16] hours. And this is only possible because
[L892] [32:57.20] we have people literally in time zones
[L893] [32:58.96] around the world uh who are just working
[L894] [33:01.44] non-stop to get it out. Um and it's not
[L895] [33:04.00] something that we ask people to do. It's
[L896] [33:05.76] there's no management edict that
[L897] [33:07.20] somebody needs to stay up late or work
[L898] [33:08.48] on a weekend to do it. People are just
[L899] [33:10.16] motivated to do it because they care.
[L900] [33:12.00] You mentioned no performance reviews and
[L901] [33:14.24] this uh scrappy bottoms up culture. How
[L902] [33:17.20] does that kind of culture work?
[L903] [33:19.28] >> I think in the world of prior to being
[L904] [33:22.16] much management, it was just uneven. I
[L905] [33:25.76] think as you would as you would guess,
[L906] [33:27.36] right? And I think that it was generally
[L907] [33:30.96] things worked well because the caliber
[L908] [33:33.92] and dedication was very high, but it was
[L909] [33:36.32] very much a bottoms up culture, right?
[L910] [33:37.84] And if there was somebody who was owning
[L911] [33:39.84] that particular part of the code that
[L912] [33:41.36] wasn't doing a good job, everybody just
[L913] [33:43.60] kind of lived with that. And um there
[L914] [33:46.96] also I would say there was very much a
[L915] [33:48.80] notion of people having ownership of
[L916] [33:51.04] areas and that being um somewhat final,
[L917] [33:55.52] right? Mozilla had a governance
[L918] [33:57.60] structure that was very much insulated
[L919] [33:59.20] against any sort of executive power. uh
[L920] [34:01.44] it was this module system and people
[L921] [34:03.20] were owners of the modules and uh even
[L922] [34:05.76] the initial access control system I
[L923] [34:07.28] think was called desperate um and it was
[L924] [34:10.96] very much a notion of distributed and
[L925] [34:14.40] decentralized decision-m
[L926] [34:16.56] I think that that culture was very
[L927] [34:19.28] powerful and there are still elements of
[L928] [34:21.12] that culture that I think are important
[L929] [34:22.32] to preserve today but there are also
[L930] [34:25.36] ways in which it fell short and needed
[L931] [34:28.24] to change and one of the things that I
[L932] [34:31.20] have spent a lot of thought on over you
[L933] [34:33.12] know recent years is finding myself in a
[L934] [34:34.72] leadership position is how do we
[L935] [34:36.40] preserve those aspects of the technical
[L936] [34:38.72] culture that make it great while also
[L937] [34:40.88] addressing some of the shortcomings.
[L938] [34:42.56] >> You mentioned a little bit about C++ and
[L939] [34:45.12] memory safety issues. That's a very
[L940] [34:46.96] classic thing and I know that Rust was
[L941] [34:49.52] developed at Mozilla to tackle those
[L942] [34:52.32] problems in large part. So I'm curious
[L943] [34:55.28] um can you tell me a little bit about
[L944] [34:56.88] the adoption of Rust and you know how it
[L945] [34:59.20] solves the problem?
[L946] [35:00.64] >> Right.
[L947] [35:01.04] >> So in the early 2010s it was pretty
[L948] [35:03.84] clear that Mozilla and Firefox the code
[L949] [35:09.44] had some real structural issues and a
[L950] [35:14.72] lot of these were issues that we could
[L951] [35:17.36] address through sheer hard work. Right?
[L952] [35:19.76] This included building a multipprocess
[L953] [35:22.48] architecture um and evolving our
[L954] [35:25.36] extension architecture such that stuff
[L955] [35:27.44] you know didn't have its tendrils into
[L956] [35:29.44] all the undocumented interfaces within
[L957] [35:31.44] the browser um and building uh native
[L958] [35:36.16] video playback so that we didn't have to
[L959] [35:38.56] rely on Adobe Flash anymore. Like these
[L960] [35:40.48] were all large but incremental projects
[L961] [35:42.88] to address specific architectural
[L962] [35:44.56] issues. But there were two architectural
[L963] [35:46.56] issues that were very difficult to
[L964] [35:48.24] address in that way. And the first one I
[L965] [35:50.00] already mentioned is memory safety,
[L966] [35:51.68] right? Because when you have a codebase
[L967] [35:52.88] that's written in C++,
[L968] [35:55.28] a large portion of the defects that you
[L969] [35:59.04] can make are the sort of defects that
[L970] [36:01.04] compromise the browser and without sac
[L971] [36:02.88] and in the absence of sandboxing
[L972] [36:04.64] compromise the computer. Um, and that
[L973] [36:07.68] was just a very difficult thing to deal
[L974] [36:10.88] with uh in a non-whackole fashion.
[L975] [36:14.40] And there's another piece which was that
[L976] [36:16.80] particularly at the time there was a
[L977] [36:19.60] increase in the number of cores that
[L978] [36:22.48] were shipping on devices. But browsers
[L979] [36:24.56] were still largely
[L980] [36:26.72] singlethreaded. And this meant that you
[L981] [36:29.52] were leaving a lot of the available
[L982] [36:31.12] performance on the table if you didn't
[L983] [36:32.56] have multi-threaded code. But if you did
[L984] [36:34.24] have multi-threaded code, especially in
[L985] [36:35.68] C++, you just had all sorts of very
[L986] [36:38.48] difficult nondeterministic bugs that
[L987] [36:40.16] were very difficult to track down. And
[L988] [36:41.84] some of these also became memory safety
[L989] [36:43.60] issues that became exploitable defects.
[L990] [36:46.00] And there was this notion that both of
[L991] [36:48.72] these were rooted in deficiencies of the
[L992] [36:51.68] C++ programming language. And all
[L993] [36:53.28] browsers are written in C++. But you
[L994] [36:56.00] know in 2010 Firefox had just taken on
[L995] [36:58.64] the world and opened up the web and
[L996] [37:01.52] there was a sense that we could do the
[L997] [37:02.80] impossible. And so we began an effort um
[L998] [37:07.04] you know sponsoring some research that
[L999] [37:09.68] uh some people internally had around
[L1000] [37:12.24] building a new programming language and
[L1001] [37:14.56] this programming language was Rust and
[L1002] [37:15.92] the idea of Rust eventually became that
[L1003] [37:18.96] we would have a programming language
[L1004] [37:20.64] that had static guarantees at compile
[L1005] [37:22.40] time that number one you didn't have
[L1006] [37:23.92] memory safety issues and number two that
[L1007] [37:25.84] you didn't have race conditions. And
[L1008] [37:29.28] this idea was that first we would build
[L1009] [37:32.48] a new programming language with these
[L1010] [37:34.08] properties which was difficult to do.
[L1011] [37:36.16] And then we would use this programming
[L1012] [37:37.68] language to build a new browser engine
[L1013] [37:40.56] for Firefox. And so the Rust project
[L1014] [37:44.56] co-evolved with this project called
[L1015] [37:46.32] servo which was
[L1016] [37:49.52] a ongoing evolving test bed for the rest
[L1017] [37:53.36] programming language with the intention
[L1018] [37:55.04] of building a browser that was memory
[L1019] [37:56.80] safe but more importantly was parallel
[L1020] [37:59.04] because there was a sense that we could
[L1021] [38:02.24] solve these architectural issues and
[L1022] [38:04.40] close the gap with Chrome but that also
[L1023] [38:06.48] we needed something to leaprog Chrome
[L1024] [38:08.64] and there was a belief that concurrency
[L1025] [38:11.20] and safe concurrency powered by a new
[L1026] [38:13.20] programming language was the way to do
[L1027] [38:14.64] that.
[L1028] [38:15.92] >> Yeah. I want to talk about the
[L1029] [38:17.52] competition with Chrome at the time
[L1030] [38:19.28] because you said they launched with a uh
[L1031] [38:23.04] more performant browser and also they
[L1032] [38:25.52] were hammering you guys with uh
[L1033] [38:27.84] distribution advantages. I'm curious
[L1034] [38:30.00] what was the strategy at that time from
[L1035] [38:31.52] the Mozilla team to compete with Chrome.
[L1036] [38:35.60] So the strategy to compete with Chrome
[L1037] [38:37.76] was
[L1038] [38:39.92] multifaceted.
[L1039] [38:42.00] One of the parts was a recognition. I
[L1040] [38:44.40] think there was a little bit of denial
