Chunk 2; segments 406–817. Start may repeat the previous chunk for context.

# Co-Creator of Haskell: Useless vs Useful Languages, Rust vs C, Functional Programming | Simon Jones

Source ID: source-3f6b5c7495d2c862
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Co-Creator_of_Haskell_Useless_vs_Useful_Languages,_Rust_vs_C,_Functional_Programming_Simon_Jones_en.txt
Video: https://www.youtube.com/watch?v=xcB_LF3cdqw

[L415] [13:25.56] the MIT had this great group led by
[L416] [13:28.76] Arvind called the MIT data flow group
[L417] [13:30.68] and they designed in the end a machine
[L418] [13:33.04] called monsoon.
[L419] [13:35.00] It was specifically designed to execute
[L420] [13:37.12] data flow programs, that is functional
[L421] [13:38.52] programs.
[L422] [13:39.60] It was based on uh you know a token
[L423] [13:41.48] store and matching and tokens flowing
[L424] [13:43.44] around and getting matched up and
[L425] [13:44.92] executing. You can imagine data flowing
[L426] [13:47.60] through a graph. When three arrives at a
[L427] [13:49.80] plus node and four arrives at the other
[L428] [13:51.56] input of the plus node, bam you can fire
[L429] [13:53.36] that plus node, right? And that hardware
[L430] [13:55.40] did all of that.
[L431] [13:58.32] At a similar kind of time in England my
[L432] [14:00.72] um
[L433] [14:01.64] colleagues uh Thomas Clark, Joe Stoy and
[L434] [14:03.80] others um built something called the SKI
[L435] [14:05.88] machine, SKIM.
[L436] [14:07.36] There's a paper about this in the
[L437] [14:09.20] um uh FDC conference. And SKIM was
[L438] [14:12.48] designed to execute SK combinators. So
[L439] [14:15.28] at the time
[L440] [14:17.16] David Turner has written a lovely paper
[L441] [14:19.04] in which he described how to take lambda
[L442] [14:21.24] calculus programs and translate them
[L443] [14:23.32] into SK combinators. So you can read
[L444] [14:25.80] about that in my book. It's a very
[L445] [14:28.00] simple translation that you can give the
[L446] [14:29.44] whole translation in half a dozen lines.
[L447] [14:31.80] But um then you have this message of
[L448] [14:34.36] this message of S's and K's. And S and K
[L449] [14:37.16] reduction is very very easy.
[L450] [14:40.00] Um so it's like the machine code of
[L451] [14:42.64] functional program. That's one way to
[L452] [14:44.16] think of it.
[L453] [14:45.20] >> What is a SK combinator just for
[L454] [14:48.56] context?
[L455] [14:49.68] >> There are three combinators, SK and I.
[L456] [14:51.84] So and they have simple reduction rules.
[L457] [14:53.64] Here they are.
[L458] [14:54.88] IX = X. KXY = X. SXYZ is X of Z applied
[L459] [15:00.32] to Y of Z. End of story. That's all.
[L460] [15:03.12] So it's very simple, right? So now all I
[L461] [15:05.08] got to do is take to take my lambda
[L462] [15:06.72] translate it into a giant tree of SK
[L463] [15:09.68] combinators, right? S applied to K
[L464] [15:11.92] applied to I of um
[L465] [15:14.28] three and um S of Z of just a huge tree
[L466] [15:18.12] of S's and K's.
[L467] [15:19.72] Right? Now simply apply the rewrite
[L468] [15:21.44] rules I gave you.
[L469] [15:22.72] And you have That's That is program
[L470] [15:24.08] execution.
[L471] [15:25.24] It's rather astonishing that that can
[L472] [15:26.44] execute arbitrarily complicated
[L473] [15:28.44] programs, but it can.
[L474] [15:30.76] Do you think that's rather amazing?
[L475] [15:33.20] Now, then I can take an arbitrary
[L476] [15:34.88] Haskell program, I can translate it into
[L477] [15:37.76] lambda terms, and I can translate those
[L478] [15:39.88] lambda terms into S and K, very simple
[L479] [15:41.92] transformation, and I can just write
[L480] [15:43.80] those Run those three rules, and it'll
[L481] [15:45.68] produce the output of the Haskell
[L482] [15:46.80] program. That's pretty amazing. And
[L483] [15:48.68] indeed, there is an implementation of
[L484] [15:50.08] Haskell that uses exactly this. It's
[L485] [15:51.68] called microHS, and my colleague Lennart
[L486] [15:53.76] Augustsson um has built it, and its
[L487] [15:56.40] execution mechanism is SK combinator
[L488] [15:58.84] reduction. And if you sit in microHS,
[L489] [16:01.16] you can ask it to show you the S's and
[L490] [16:02.88] K's that it produces. If we had a, you
[L491] [16:05.04] know, shared screen, I could probably
[L492] [16:06.32] show you. Um
[L493] [16:08.80] Uh So, long story short then, um
[L494] [16:12.16] uh
[L495] [16:13.28] the SKI machine was designed to take SK
[L496] [16:16.84] trees, big trees of S's and K
[L497] [16:18.84] combinators, and just execute them
[L498] [16:20.44] directly. So, it was built
[L499] [16:22.96] in hardware, and it ran perfectly well,
[L500] [16:26.12] um reasonably fast.
[L501] [16:27.84] Now, why didn't this catch on? Why don't
[L502] [16:29.92] we have
[L503] [16:31.28] um functional programming machines? I
[L504] [16:32.64] mean, at the time, it was a big idea. We
[L505] [16:34.28] even had a conference called
[L506] [16:36.48] Functional Programming Computer
[L507] [16:37.80] Architecture, FPCA. It was right there
[L508] [16:40.92] in the title of the conference.
[L509] [16:43.96] But slowly, we became aware that
[L510] [16:47.28] what was really happening is we were
[L511] [16:49.28] doing at run time what we could do
[L512] [16:51.24] instead at compile time.
[L513] [16:53.72] And that is always a bad idea.
[L514] [16:56.28] Imagine an interpreter for, I don't
[L515] [16:58.04] know, um Pascal or something.
[L516] [17:01.44] It'd be Or uh for Java. Like, we can
[L517] [17:03.80] compile Java to bytecode, and we could
[L518] [17:05.76] interpret the bytecode.
[L519] [17:08.80] Right? So, then we are We're doing
[L520] [17:10.88] something at run time. At run time, the
[L521] [17:12.76] interpreter is looking at the bytecode
[L522] [17:14.32] saying, dispatching to say which
[L523] [17:15.80] instruction, blah blah blah. right?
[L524] [17:18.32] Now, what does a JIT do? It takes a
[L525] [17:20.08] sequence of bytecode and says, "Oh, no,
[L526] [17:21.48] no.
[L527] [17:22.64] I'm going to take that sequence of
[L528] [17:24.08] bytecode and compile it to a sequence of
[L529] [17:25.60] machine instructions that, when
[L530] [17:27.40] executed, will do the same thing,
[L531] [17:28.96] right?"
[L532] [17:30.80] Much faster.
[L533] [17:34.00] Because it can take advantage of common
[L534] [17:35.48] of bytecode sequences, for example, to
[L535] [17:37.36] say, you know, if you swap and then
[L536] [17:39.20] swap, it's a no-op or something like
[L537] [17:40.52] that, right?
[L538] [17:43.96] So, what In fact, it turned out is this
[L539] [17:46.64] whole SKI business, and any other And
[L540] [17:49.32] indeed dataflow machines also, was
[L541] [17:51.40] simply doing at runtime what you could
[L542] [17:53.36] do better at compile time. We were
[L543] [17:55.24] building an interpreter in hardware.
[L544] [17:58.92] So, don't build the interpreter in
[L545] [18:00.20] hardware. Instead, build a compiler
[L546] [18:02.56] that translates
[L547] [18:04.44] your lambda term into a sequence of
[L548] [18:06.52] machine instructions that, when
[L549] [18:08.32] executed,
[L550] [18:09.96] will behave as if you had
[L551] [18:12.36] done this uh reduction business.
[L552] [18:14.96] And then you might think, well, machine
[L553] [18:17.00] instructions for what machine?
[L554] [18:19.56] Well,
[L555] [18:20.56] from a practical point of view, it was
[L556] [18:22.76] very hard to compete with Intel.
[L557] [18:25.76] Right? They were just spending
[L558] [18:27.24] Brazilians of man-years on making x86s
[L559] [18:29.80] go faster.
[L560] [18:31.24] And ARM likewise for ARMs. So, um we can
[L561] [18:34.28] leverage all of that work by compiling
[L562] [18:36.00] into their instruction set.
[L563] [18:38.48] But even if you say you are God, you are
[L564] [18:41.32] the chief executive in Intel, and can
[L565] [18:43.44] tell them to add new instructions or
[L566] [18:46.24] mechanisms to support functional
[L567] [18:47.84] programming, what would you add?
[L568] [18:50.12] Not very much.
[L569] [18:53.48] Little bits to do with um
[L570] [18:55.60] uh garbage collection barriers, I think.
[L571] [18:58.40] And and such like, but nothing major.
[L572] [19:03.72] So, in other words, I think the whole
[L573] [19:07.00] build hardware to execute functional
[L574] [19:08.68] programming directly turned out to be a
[L575] [19:10.52] mistake. Inspiring mistake, fun mistake,
[L576] [19:13.36] I had a great time, but a mistake.
[L577] [19:15.60] It's better to build a compiler.
[L578] [19:17.84] >> I would have thought there might be some
[L579] [19:19.72] unique opportunities for parallelism
[L580] [19:23.12] given the immutability in these
[L581] [19:25.20] functional programming languages. So,
[L582] [19:27.84] I Yeah, you described that that graph or
[L583] [19:30.08] that SK combinator graph. I imagine you
[L584] [19:33.72] could,
[L585] [19:34.72] you know,
[L586] [19:35.68] execute that all in parallel assuming
[L587] [19:37.68] there's no connections across
[L588] [19:39.84] the graph.
[L589] [19:40.52] >> And indeed, that was the data flow
[L590] [19:41.96] machine. The MIT data flow machine was
[L591] [19:43.56] all based on that idea. It's saying just
[L592] [19:45.28] throw the whole graph into the token
[L593] [19:46.88] store and just run all the nodes that
[L594] [19:48.96] are runnable.
[L595] [19:50.48] Right?
[L596] [19:51.36] But that's incredibly fine grained.
[L597] [19:53.12] You've got to imagine this big tree of a
[L598] [19:55.64] million nodes and your processor is sort
[L599] [19:58.00] of wandering around over it doing little
[L600] [19:59.72] things in parallel. There's a lot of
[L601] [20:01.64] memory traffic going on there. And if
[L602] [20:03.16] this these these little, you know,
[L603] [20:04.40] threads have to, you know, are operating
[L604] [20:06.04] on the same bit of tree, then the
[L605] [20:07.16] synchronization costs,
[L606] [20:08.88] um so, very, very fine grained computer
[L607] [20:12.68] parallel computation like this turns out
[L608] [20:14.48] to be impractical.
[L609] [20:17.00] Like or not impractical. You could do
[L610] [20:18.64] it, but it's very slow.
[L611] [20:20.88] Right? So, the data flow people, their
[L612] [20:23.32] history, if you look at the history of
[L613] [20:24.72] the MIT data flow project, they started
[L614] [20:26.80] with micro parallelism. Every individual
[L615] [20:30.48] instruction was a separate parallel
[L616] [20:32.60] computation that might take place and
[L617] [20:34.80] the token store would match it up.
[L618] [20:36.40] Right? And then they built more and more
[L619] [20:38.56] compiler technology that grouped these
[L620] [20:40.28] things together into larger units. So,
[L621] [20:42.68] they expanded from micro threads of
[L622] [20:44.88] single instruction threads into 10
[L623] [20:46.80] instruction threads or 100 instruction
[L624] [20:48.32] threads. Right?
[L625] [20:49.88] But even that never really caught on.
[L626] [20:51.68] So,
[L627] [20:53.12] you're right, though,
[L628] [20:54.44] that if I say in a Haskell program, E1 +
[L629] [20:57.52] E2,
[L630] [20:58.96] then I can do E1 and E2 in parallel. And
[L631] [21:01.92] GHC does support you in doing that, but
[L632] [21:04.08] you nowadays, rather than expecting the
[L633] [21:06.24] compiler to do that automatically for
[L634] [21:08.56] every sub-expression,
[L635] [21:10.28] you can spark a computation. You say E1
[L636] [21:13.32] par E2, and that says do E1 and E2 in
[L637] [21:16.80] parallel. There's a project at Carnegie
[L638] [21:19.32] Mellon
[L639] [21:20.56] for a strict parallel strict language
[L640] [21:22.32] called ML
[L641] [21:24.08] that has a very good variant of parallel
[L642] [21:26.16] ML going in a similar way. So,
[L643] [21:28.24] essentially we've moved away from the
[L644] [21:30.24] the dream of
[L645] [21:31.80] automatically getting parallel at very,
[L646] [21:34.52] very fine grain
[L647] [21:36.44] to programmer
[L648] [21:37.72] we give programmer clues about where
[L649] [21:39.24] it's a good idea to do parallelism, but
[L650] [21:41.64] um
[L651] [21:42.20] uh and still the compiler will try not
[L652] [21:44.40] to fork to too tiny grains.
[L653] [21:47.16] >> I was searching on YouTube and I've
[L654] [21:49.32] searched your name and this video came
[L655] [21:51.16] up and it said "Haskell is useless,
[L656] [21:54.96] Simon Peyton Jones."
[L657] [21:56.57] >> [laughter]
[L658] [21:56.72] >> And it's it's a video from a long time
[L659] [21:58.84] ago. It's someone's got a low-quality
[L660] [22:01.52] and a handheld camera. There's group of
[L661] [22:04.40] researchers that are all talking. Butler
[L662] [22:06.68] Lampson is across the table and it's
[L663] [22:08.44] it's a fun little video. And in the
[L664] [22:10.40] video, you lay out this two-dimensional
[L665] [22:14.36] graph where on on one dimension
[L666] [22:17.04] there is the useful versus useless axis
[L667] [22:22.44] and then on the other dimension there is
[L668] [22:24.28] the safe versus dangerous. And then
[L669] [22:27.00] you're placing programming languages on
[L670] [22:29.36] this two-dimensional graph and I think
[L671] [22:32.12] you started by putting C as it's very
[L672] [22:36.08] useful, but it's incredibly dangerous.
[L673] [22:39.52] And then you put Haskell on the the
[L674] [22:41.84] polar opposite side. It's You said it's
[L675] [22:44.08] useless,
[L676] [22:45.40] but it's very safe. What are the least
[L677] [22:48.04] safe and most useful languages and why
[L678] [22:50.48] do you place them there like C for
[L679] [22:52.28] instance?
[L680] [22:52.64] >> Well, yeah. So, um
[L681] [22:54.56] let's see. In C, you program by
[L682] [22:56.60] mutation. So,
[L683] [22:58.40] it's unsafe in the sense that any
[L684] [22:59.56] function can mutate any variable at any
[L685] [23:01.24] time. It has a lot, you you pass
[L686] [23:02.68] pointers around a lot and functions
[L687] [23:04.68] mutate the memory pointed to by those
[L688] [23:06.80] pointers. And moreover,
[L689] [23:08.28] typically they can mutate it anywhere.
[L690] [23:09.76] There's no array bounds checks or
[L691] [23:11.36] anything. So, it's kind of like super
[L692] [23:13.36] unsafe in the fact that this is
[L693] [23:14.40] demonstrated by the fact Can you imagine
[L694] [23:16.64] that that like all of these exploits
[L695] [23:18.32] that we get every day, right? Um
[L696] [23:21.28] that uh you know, MSRC is discovering in
[L697] [23:23.44] huge numbers, but but we've had you
[L698] [23:25.00] know,
[L699] [23:25.84] why is the internet so insecure?
[L700] [23:28.32] Primarily because all of our software
[L701] [23:30.04] infrastructure is written in unsafe
[L702] [23:31.24] languages. If we I mean
[L703] [23:34.08] if we'd written all of our
[L704] [23:35.88] you know, internet software and
[L705] [23:37.60] operating systems in Haskell or maybe in
[L706] [23:39.92] OCaml or ML,
[L707] [23:41.92] 99% of all these exploits would be
[L708] [23:44.20] removed by construction.
[L709] [23:47.64] Like it's like we've built a boat out of
[L710] [23:52.28] paper clips and we're surprised that
[L711] [23:53.96] it's leaky.
[L712] [23:55.16] I mean, you shouldn't build boats out of
[L713] [23:56.56] paper clips, right? Because they have
[L714] [23:58.12] holes in them. You should build it out
[L715] [23:59.96] of a secure substance, right? But then
[L716] [24:02.12] it's too late. So, we spend incredible
[L717] [24:05.04] amounts of human ingenuity and effort
[L718] [24:06.92] patching the holes in our boat built of
[L719] [24:09.20] paper clips. It's tragic. It's tragic
[L720] [24:12.96] how much effort and ingenuity and money
[L721] [24:16.00] has been lost and waste of resources
[L722] [24:18.36] just because we wrote our um you know,
[L723] [24:21.84] computational infrastructure for the
[L724] [24:23.24] world in an insecure language. That's
[L725] [24:25.76] what I mean by unsafe.
[L726] [24:27.56] >> I mean, are there not vulnerabilities?
[L727] [24:29.16] Like if I wrote something in Haskell, I
[L728] [24:31.40] mean,
[L729] [24:32.36] there's got to be some new type of
[L730] [24:34.32] >> there are vulnerabilities. I just said
[L731] [24:35.44] 99%. I didn't say 100.
[L732] [24:37.60] If I write a Haskell program that says,
[L733] [24:40.56] "Receive message. If the message says,
[L734] [24:43.20] 'Tell me everything,' then spit out my
[L735] [24:46.96] entire database in reply."
[L736] [24:49.28] No language can stop you doing that,
[L737] [24:51.08] right?
[L738] [24:52.20] But, if you look at the program and it
[L739] [24:53.84] doesn't have any such things,
[L740] [24:55.64] right?
[L741] [24:56.69] >> [laughter]
[L742] [24:58.48] >> So, I mean
[L743] [24:59.80] So, you know, nothing can prevent you
[L744] [25:01.40] against high-level attacks to insecure
[L745] [25:03.12] programs. Or, I mean, another example
[L746] [25:04.84] might be deadlock, right? Two services,
[L747] [25:07.76] no matter how securely written, if A
[L748] [25:10.24] waits for B and B waits for A, deadlock.
[L749] [25:12.76] Sorry.
[L750] [25:15.48] No and no language is going to stop you
[L751] [25:17.68] doing that.
[L752] [25:18.88] Um you might hope for some high-level
[L753] [25:20.68] verification tools.
[L754] [25:22.48] But it's like
[L755] [25:25.16] Surely, if you're trying to do something
[L756] [25:27.32] hard, like prove that that doesn't
[L757] [25:29.16] happen, you want to have a foundation
[L758] [25:31.08] that is, you know, in which you've got
[L759] [25:32.96] some bedrock to stand on. If you're
[L760] [25:34.80] standing on sand and trying to prove
[L761] [25:36.84] some advanced property, it's very, very
[L762] [25:38.88] difficult. But, good point. I'm not
[L763] [25:41.12] talking about 100% security. Absolutely
[L764] [25:43.08] not. But, uh how many how many of how
[L765] [25:45.72] many uh exploits are based on buffer
[L766] [25:47.80] overruns?
[L767] [25:49.36] Or, you know, pointer manipulation
[L768] [25:51.20] that's gone wrong.
[L769] [25:52.44] If you couldn't have a buffer overrun,
[L770] [25:53.92] you couldn't do pointer manipulations
[L771] [25:55.28] gone wrong. Those Those exploits just
[L772] [25:57.08] wouldn't exist.
[L773] [25:58.80] >> So, I mean, C is maybe half a century
[L774] [26:02.08] old now.
[L775] [26:03.44] Um
[L776] [26:04.00] what about more modern versions of those
[L777] [26:07.32] lower-level languages like Rust?
[L778] [26:09.72] >> Much, much better. Much, much, much
[L779] [26:11.64] better, right? If we rewrote all of our
[L780] [26:14.12] software infrastructure in Rust,
[L781] [26:16.40] things would be way, way better.
[L782] [26:18.92] I I'm not actually even sure whether
[L783] [26:20.64] Rust has array bounds checks built in,
[L784] [26:22.80] but suppose it but it must have the
[L785] [26:24.56] ability
[L786] [26:25.00] >> to
[L787] [26:26.44] >> uh
[L788] [26:27.56] promise that you're not uh and actually
[L789] [26:29.04] not bound. I don't quite know quite know
[L790] [26:30.24] how, but if you compile all your code
[L791] [26:31.36] with that switched on,
[L792] [26:32.76] you're a way better situation. Way
[L793] [26:34.88] better.
[L794] [26:37.24] So, yes, this is not just functional
[L795] [26:38.84] programming, but you did ask about why I
[L796] [26:41.00] thought C was an insecure, unsafe
[L797] [26:42.76] language.
[L798] [26:44.11] >> [laughter]
[L799] [26:44.84] >> If we imagine that graph, there's that
[L800] [26:47.08] the upper right quadrant, which is
[L801] [26:49.52] useful and safe. And you know, you
[L802] [26:52.40] described that as Nirvana in the in in
[L803] [26:55.36] the video. And I guess maybe over time,
[L804] [26:58.28] I mean C's you know, somewhat really
[L805] [26:59.84] unsafe, really useful.
[L806] [27:01.36] >> Yes, so C I mean Rust has moved along
[L807] [27:03.72] the axis
[L808] [27:05.00] from
[L809] [27:06.16] useful but very unsafe
[L810] [27:08.60] to stay useful and become safer.
[L811] [27:11.68] Now, Haskell started life as being very
[L812] [27:13.68] safe but useless.
[L813] [27:15.64] So, it's worth just you know, rehearsing
[L814] [27:17.16] that because in the first version of
[L815] [27:18.64] Haskell, there was no IO.
[L816] [27:21.00] The only that a Haskell program was a
[L817] [27:23.24] function of type string to string.
[L818] [27:25.52] It's functional programming after all.
[L819] [27:27.36] It could do no IO. All it could do was
[L820] [27:29.20] take a string and produce a string.
[L821] [27:31.88] So, obviously that's not very useful.
[L822] [27:34.76] It's a little bit more useful. A
[L823] [27:35.92] language that is very very safe
[L824] [27:38.12] and completely useless is no-op
[L825] [27:40.68] that does nothing ever.
[L826] [27:42.36] Very safe
