Chunk 2; segments 354–708. Start may repeat the previous chunk for context.

# Turing Award Winner: TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC | David Patterson

Source ID: source-fc9308e696a718d4
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_TPU_vs_GPU_vs_CPU,_Computer_Architecture,_RISC_vs_CISC_David_Patterson_en.txt
Video: https://www.youtube.com/watch?v=Pn4ZwlEh5nw

[L363] [13:50.80] routine or something and say how can we
[L364] [13:52.88] most efficiently do registers? In fact,
[L365] [13:55.68] the C programming language which was
[L366] [13:58.48] invented to do systems programming
[L367] [14:02.32] in C before that to write an operating
[L368] [14:04.64] system people wrote them an assembly
[L369] [14:06.08] language believe it or not and but the
[L370] [14:08.72] Unix people showed uh Ken Thompson
[L371] [14:11.20] Dennis Richie showed that we could if we
[L372] [14:13.68] had a low-level language pretty
[L373] [14:15.28] low-level language we get the benefits
[L374] [14:17.12] of writing in something that it's much
[L375] [14:18.72] easier for humans to understand and
[L376] [14:20.24] debug
[L377] [14:22.24] because register allocation by the
[L378] [14:24.48] compilers was was so poor, they had to
[L379] [14:27.68] put in the ability for the programmer to
[L380] [14:30.08] give hints of what variables should go
[L381] [14:31.60] in registers. It was just easier for
[L382] [14:33.68] them to have the programmer step in and
[L383] [14:36.40] say, if the machine had eight registers,
[L384] [14:38.08] I want these six variables to be in
[L385] [14:39.84] these registers. Don't leave them in
[L386] [14:41.20] memory because it runs so much slower.
[L387] [14:43.12] Registers are so much faster. So, a big
[L388] [14:46.48] part of u the the CISK the risk argument
[L389] [14:50.56] was the compiler algorithms are getting
[L390] [14:52.64] better. they could handle these
[L391] [14:53.92] low-level instructions, they could
[L392] [14:55.60] allocate registers efficiently.
[L393] [14:58.16] Uh, and that was, you know, another
[L394] [15:00.24] reason in these debates about why it
[L395] [15:02.40] made sense to have a simpler
[L396] [15:03.92] architecture. What we did in the risk
[L397] [15:06.24] architectures, well, if registers are
[L398] [15:08.16] really important, uh, register
[L399] [15:10.16] allocation really important. One way to
[L400] [15:11.60] make it easier for the compiler was just
[L401] [15:13.76] to have a lot more of them. So,
[L402] [15:15.68] typically the CISK architectures of
[L403] [15:17.44] times would have eight or maybe 16
[L404] [15:19.20] registers. So, we we put in 32 and That
[L405] [15:23.44] was one of the arguments, right, is
[L406] [15:25.52] well, if it's hard to efficiently use a
[L407] [15:27.84] small number, let's give them plenty.
[L408] [15:29.28] So, even if it wasn't that good,
[L409] [15:31.44] there'll be enough registers. So, most
[L410] [15:32.72] of the time and and registers weren't
[L411] [15:34.48] that much more expensive to include in
[L412] [15:36.32] machines because of MOR's law. I saw
[L413] [15:38.72] somewhere in in uh one of the talks that
[L414] [15:41.20] he had given that somehow the compiler
[L415] [15:44.88] it's it's more easy for it to optimize
[L416] [15:46.80] the code for risk but in CISK there were
[L417] [15:49.68] these complex bigger ones and it almost
[L418] [15:52.64] never used them. Is that a shortcoming
[L419] [15:54.56] of the compiler? So what happened if we
[L420] [15:57.36] go back in the compiler days there's
[L421] [15:59.84] this argument is that by having more
[L422] [16:01.60] sophisticated instructions this would
[L423] [16:03.84] raise the level of extraction. that'll
[L424] [16:05.52] be a smaller gap. They'll make it easy
[L425] [16:07.36] for the compiler. But that was a
[L426] [16:08.56] philosophical argument. It it wasn't
[L427] [16:10.88] something that necessarily compiler
[L428] [16:12.72] people um could work. Compiler people
[L429] [16:16.88] weren't making that argument. It was the
[L430] [16:18.72] architects were making that argument.
[L431] [16:20.80] And as it turned out when we looked at
[L432] [16:22.48] the programs when we were doing the
[L433] [16:24.32] early research on CISK in versus risk is
[L434] [16:28.08] the compilers didn't really use those
[L435] [16:29.52] instructions. Often the compiler
[L436] [16:30.96] writers, the architects would come up
[L437] [16:32.64] with a sophisticated instruction and the
[L438] [16:34.88] compiler writers would say, "Well, we
[L439] [16:36.56] don't need that." In fact, we found
[L440] [16:38.80] examples where like for a procedure
[L441] [16:40.80] entry, there'd be a special instruction
[L442] [16:43.04] built in to do all this work that what
[L443] [16:45.12] the architects thought the compilers
[L444] [16:46.48] wanted and the compiler designers say,
[L445] [16:48.16] "Well, we don't need that. It's it's
[L446] [16:50.64] faster. It's actually faster for to use
[L447] [16:52.96] it with separate instructions than use
[L448] [16:55.04] your sophisticated instruction." And so,
[L449] [16:56.96] we found a bunch of examples like that.
[L450] [16:58.96] So you pay the extra overhead of the
[L451] [17:00.88] microode interpreter to have these
[L452] [17:02.48] sophisticated instructions and then the
[L453] [17:04.32] compiler doesn't even use them. Right?
[L454] [17:06.32] So th this is kind of a nonsensical
[L455] [17:08.88] situation that that we're in. uh and you
[L456] [17:12.64] know this is kind of like you know why
[L457] [17:14.64] why are there startups or why are there
[L458] [17:17.36] scientific you know breaking points like
[L459] [17:20.40] that as we looked at all the
[L460] [17:21.60] technologies with Moore's law you know
[L461] [17:24.00] ideas like caches with where compilers
[L462] [17:27.20] were in using sophisticated instructions
[L463] [17:28.80] the ability to allocate register more
[L464] [17:30.64] efficiently it made sense to change the
[L465] [17:33.12] directions away from these microcoded
[L466] [17:34.88] instruction set architectures to these
[L467] [17:36.80] simpler architectures
[L468] [17:38.32] >> when we talk about instruction sets I
[L469] [17:40.24] mean we're kind assuming that we're
[L470] [17:42.00] talking about these general purpose
[L471] [17:44.24] computer are these CPUs and I know GPUs
[L472] [17:47.20] are kind of talked about a lot and maybe
[L473] [17:50.08] there's other forms of computing are
[L474] [17:52.32] there instruction sets for those types
[L475] [17:54.80] of machines as well.
[L476] [17:56.00] >> So what happened is around 2000 is when
[L477] [17:59.04] GPUs came along and these were what we
[L478] [18:02.00] called domain specific architectures. So
[L479] [18:03.92] a GPU is a graphics processing unit. It
[L480] [18:06.56] had one job. it it didn't need to do
[L481] [18:09.60] everything that a general purpose
[L482] [18:10.80] processor needs to. Didn't have to
[L483] [18:12.72] support virtual memory. Uh it didn't
[L484] [18:15.36] have to support a compiler which is you
[L485] [18:17.36] know a pretty radical idea for
[L486] [18:19.44] architectures. It was just for graphics.
[L487] [18:22.16] And so around 2000 is when Nvidia and
[L488] [18:25.76] the other GPUs out there because they
[L489] [18:27.44] were trying to do you know the give you
[L490] [18:30.32] the graphics for games and give you the
[L491] [18:31.76] graphics for movies. So it was a niche
[L492] [18:33.76] product.
[L493] [18:35.28] So what happened kind of in the computer
[L494] [18:37.36] industry is it was driven by Moore's law
[L495] [18:40.88] which I've mentioned many times and also
[L496] [18:43.44] this lesserk known law called dinard
[L497] [18:45.76] scaling which is because kind of an
[L498] [18:48.16] interesting question well if Moore's law
[L499] [18:49.92] puts a lot more transistors on a chip
[L500] [18:52.40] how come they're not getting hotter and
[L501] [18:54.24] hotter as we double the number of
[L502] [18:55.92] transistors every year and the reason
[L503] [18:57.52] was this observation made by Bob Dinard
[L504] [19:01.36] that what as you added more transistors
[L505] [19:04.80] People would also lower the threshold
[L506] [19:06.56] voltage which the distinction between a
[L507] [19:08.40] zero and one and that had like a squared
[L508] [19:11.52] effect. So you would end up doubling
[L509] [19:13.92] them transistors but you'd lower the
[L510] [19:15.60] threshold voltage. So microprocessors
[L511] [19:17.92] stayed at like 20 or 30 watts. In fact
[L512] [19:22.56] uh we did a John and I eventually did a
[L513] [19:25.28] textbook and I was just checking and
[L514] [19:27.36] that came out in 1990 and we didn't even
[L515] [19:29.04] talk about power as an issue for the
[L516] [19:31.12] first three editions. You know, the the
[L517] [19:32.96] third one came out in 2000. Power wasn't
[L518] [19:35.28] even a topic because micro dinard
[L519] [19:37.68] scaling was going on and so
[L520] [19:39.04] microprocessors stayed in the tens of
[L521] [19:41.44] watts even as they got faster and
[L522] [19:43.12] faster. What happened is about 2005 or
[L523] [19:46.64] so, Dinard scaling stopped working and
[L524] [19:49.20] that was a shock, right? So, and Intel
[L525] [19:52.08] actually had a microprocessor that
[L526] [19:55.04] failed one of their generations because
[L527] [19:57.68] they just couldn't get the power down
[L528] [19:59.68] enough. it was too hot to be able to do
[L529] [20:01.68] that. Um and then so then what that
[L530] [20:05.68] forced us to go to multicore is that uh
[L531] [20:09.52] before that it was easiest for the
[L532] [20:11.28] programmer for everybody if there was
[L533] [20:12.72] one very sophisticated processor that
[L534] [20:14.96] did everything but we couldn't do that
[L535] [20:16.96] anymore. So it went from one
[L536] [20:18.72] sophisticated processor to two and then
[L537] [20:21.28] four and then eight simpler processors.
[L538] [20:23.12] Then it was up to the programmer to
[L539] [20:25.44] deliver on the potential of Morris law
[L540] [20:27.44] by paralyzing their code. So we stayed
[L541] [20:30.80] that way for about another 10 years and
[L542] [20:34.16] then Moore's law started slowing down.
[L543] [20:36.96] Uh so that the general purpose
[L544] [20:38.80] microprocessor was barely improving. It
[L545] [20:40.96] got a little better but it wasn't
[L546] [20:42.32] getting dramatically better. Um, in the,
[L547] [20:45.44] you know, in the 1980s, 1990s, 2000s,
[L548] [20:50.88] you you have a laptop and your friend's
[L549] [20:52.96] laptop would be like four times as fast
[L550] [20:55.36] as yours. And, you know, you were
[L551] [20:56.88] jealous. So, you would throw away
[L552] [20:59.04] perfectly good hardware because your
[L553] [21:01.36] friend's thing was so much faster
[L554] [21:03.60] because of the rapid change in
[L555] [21:05.04] performance. Well, that all ended in the
[L556] [21:08.32] 2010s where the you never you wouldn't
[L557] [21:10.64] throw away a laptop because the new ones
[L558] [21:12.56] were hardly that much faster than the
[L559] [21:14.40] old ones. You throw them away when they
[L560] [21:15.76] break and slow down. Nevertheless,
[L561] [21:18.16] programmers were used to this dramatic
[L562] [21:20.56] improvement in performance every few
[L563] [21:22.96] years because they could add more
[L564] [21:24.48] features to their software and stuff
[L565] [21:25.68] like that. So, what were architects
[L566] [21:27.36] going to do? They'd already done the the
[L567] [21:29.12] multicore trick in 2005 or so. So around
[L568] [21:33.76] 2015 the idea was we would do domain
[L569] [21:36.24] specific architectures like the GPUs. So
[L570] [21:38.96] we if we if you tell me I only have to
[L571] [21:41.68] run a narrow class of programs and I
[L572] [21:44.08] don't have to necessarily run all the
[L573] [21:46.32] operating systems everything else. Well
[L574] [21:48.16] yes I could shuffle those resources and
[L575] [21:51.12] do something much more efficient for
[L576] [21:53.12] something well. So you could do some
[L577] [21:54.72] things well and there's other things
[L578] [21:56.64] either you do poorly or not even at all.
[L579] [21:59.04] So then the question is okay what
[L580] [22:00.80] domain? So just coincidentally where we
[L581] [22:04.00] were technologically right around 2012
[L582] [22:07.92] 2015 is when machine learning AI burst
[L583] [22:11.12] on the scene. Um and so that was it was
[L584] [22:15.12] evident what domain should we do and the
[L585] [22:17.84] domain was machine learning AI. So just
[L586] [22:20.00] coincidentally where we were
[L587] [22:21.20] technologically
[L588] [22:22.96] uh this new domain came along and then I
[L589] [22:25.76] I would say you know I I work for Google
[L590] [22:28.08] but I think it's fair to say Google was
[L591] [22:30.56] the one who really uh saw it was the
[L592] [22:33.36] certainly the first big company who
[L593] [22:35.76] understood the potential of machine
[L594] [22:37.20] learning AI and um and bet that they or
[L595] [22:42.00] feared that they were going to be
[L596] [22:43.44] swamped with demand and needed to do
[L597] [22:45.92] custom hardware. So the the translate
[L598] [22:49.76] tensor processing unit GPU that Google
[L599] [22:52.80] debuted in 2016 really kind of shocked
[L600] [22:56.24] the world and got people to realize that
[L601] [22:58.96] we should be uh designing hardware for
[L602] [23:01.28] machine learning and we could continue
[L603] [23:04.16] to improve performance dramatically for
[L604] [23:06.48] that one domain.
[L605] [23:08.08] >> What's the high level differences
[L606] [23:09.84] between a CPU, a GPU and a TPU? the the
[L607] [23:14.72] CPU has got to be this general purpose
[L608] [23:16.72] thing. And basically um even today they
[L609] [23:20.40] have these general purpose cores that
[L610] [23:23.12] each core is very similar to what the
[L611] [23:25.84] instruction sets or used to be like 20
[L612] [23:29.12] years before that. It's not a surprising
[L613] [23:31.20] design and it's just got lots of cores
[L614] [23:32.96] and modern ones today could have a h you
[L615] [23:35.28] know 50 or 100 cores in there. So that's
[L616] [23:37.76] that's the feature for graphics. uh what
[L617] [23:40.80] they decided to do which to do the
[L618] [23:43.52] graphics job is they need to get a lot
[L619] [23:45.36] of performance on the memory system. So
[L620] [23:46.96] they went to multi-threading. So they
[L621] [23:49.28] have hardware threads that you would
[L622] [23:51.36] send a memory request out and you the
[L623] [23:53.76] hardware would switch over to do
[L624] [23:54.96] something else while the when memory is
[L625] [23:57.04] coming out. So it's this highly threaded
[L626] [23:59.28] architecture and that's what they
[L627] [24:01.04] developed and could could run well for
[L628] [24:03.28] graphics.
[L629] [24:04.80] um a and graphics. It turns out um
[L630] [24:08.48] doesn't need very s doesn't need
[L631] [24:11.60] powerful floating point. It needs
[L632] [24:14.32] doesn't need wide floating point. So
[L633] [24:15.84] 32-bit floating point is plenty for
[L634] [24:17.68] graphics even 16 bit. So they were doing
[L635] [24:20.56] pushing graphics with 16 and 32-bit
[L636] [24:22.80] floating point in this multi-threaded
[L637] [24:24.80] kind of architecture. And because it was
[L638] [24:27.04] kind of its own unique thing, it has its
[L639] [24:28.64] own own set of terminology
[L640] [24:31.44] um all to itself. it wasn't kind of out
[L641] [24:33.76] of the main branch of computer
[L642] [24:35.20] architecture. Uh so when you look at our
[L643] [24:38.00] textbooks, we have kind of like a
[L644] [24:39.44] Rosetta Stone which says here's the
[L645] [24:42.32] terms that Nvidia uses to describe DP2s.
[L646] [24:45.12] This is what it means in kind of normal
[L647] [24:48.08] um well normal in the mainstream
[L648] [24:50.24] processor design. So they were this
[L649] [24:52.32] niche product that happened to do pretty
[L650] [24:54.96] fast um single precision floating point
[L651] [24:58.24] and uh even half precision floating
[L652] [25:00.24] point and they were pretty cheap. They
[L653] [25:02.64] were like hundreds of dollars.
[L654] [25:05.12] Um
[L655] [25:07.04] so when people uh so kind of uh but some
[L656] [25:12.24] people were thinking boy for some
[L657] [25:13.76] applications if I could turn my program
[L658] [25:16.64] into like uh pretend that it was doing
[L659] [25:20.16] creating an image if I could turn my
[L660] [25:22.48] problem into image generation I could
[L661] [25:24.16] use these pretty cheap GPUs which had
[L662] [25:27.20] very good floatingoint performance per
[L663] [25:29.28] dollar compared to anything else. And so
[L664] [25:31.76] people started playing around with that.
[L665] [25:33.68] Uh and uh the founder CEO Jensen Wang
[L666] [25:38.16] really liked that idea. So in 2006,
[L667] [25:42.72] he funded an effort to create a
[L668] [25:45.28] programming language that that would
[L669] [25:47.28] kind of handle this multi-threaded
[L670] [25:49.60] hardware architecture that's for
[L671] [25:50.96] graphics to make it easier to program.
[L672] [25:53.12] And so that led to the invention of uh
[L673] [25:56.16] CUDA uh which I can't remember its
[L674] [25:58.56] acronym but it's really a a proprietary
[L675] [26:01.44] programming language for the
[L676] [26:02.72] multi-threaded GPU architecture to make
[L677] [26:05.60] it kind of easier to program. It was a
[L678] [26:07.84] it was a C like language but you can't
[L679] [26:10.56] just compile C programs and run it but
[L680] [26:12.56] it was C like but people actually liked
[L681] [26:14.88] it. You know it was certainly much
[L682] [26:16.24] better than trying to turn your program
[L683] [26:17.84] into an image generation but people
[L684] [26:20.40] liked it. But uh Jensen Wang his vision
[L685] [26:22.80] was try to get these teenagers in the
[L686] [26:25.12] basement who are playing the games to
[L687] [26:26.40] learn how to program these things. And
[L688] [26:28.00] he had a couple of markets that he was
[L689] [26:29.76] interested in like um you know uh some
[L690] [26:33.20] of the department of energy labs like uh
[L691] [26:35.60] fluid flow and some of things like you
[L692] [26:37.76] know some and he would build special
[L693] [26:39.44] purpose libraries that could handle that
[L694] [26:41.28] domain and then use his GPUs to do that
[L695] [26:44.48] kind of uh special purpose computing but
[L696] [26:47.28] breaking out of graphics. But that's
[L697] [26:49.76] kind of the heritage there. Now for the
[L698] [26:51.52] TPU program um and and so what's
[L699] [26:54.88] happened uh people started right from
[L700] [26:56.88] the very beginning people started using
[L701] [26:58.24] GPUs because they had much better single
[L702] [27:00.64] precision floatingoint performance than
[L703] [27:03.52] um than the CPUs. They had a lot more
[L704] [27:06.24] processors on them. So we had the
[L705] [27:08.24] potentially much more performance. So
[L706] [27:09.76] they're kind of one of the breakthrough
[L707] [27:11.20] moments moments in it was in 2012 when
[L708] [27:16.88] uh within the machine learning community
[L709] [27:18.96] this neural networking piece which had a
[L710] [27:21.76] few advocates but a lot of people didn't
[L711] [27:23.44] believe in it they went into a
[L712] [27:25.44] competition to see who could do the best
[L713] [27:27.92] image recognition in 2012 the so-called
[L714] [27:31.60] AlexNet beat all the competition this
[L715] [27:33.92] was this uh historic moment in the in
[L716] [27:37.68] the in machine learning learning in
[L717] [27:39.68] neural networking and once they did it
