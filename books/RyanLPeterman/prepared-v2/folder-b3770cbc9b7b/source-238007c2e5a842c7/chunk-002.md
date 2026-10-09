Chunk 2; segments 360–713. Start may repeat the previous chunk for context.

# Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

Source ID: source-238007c2e5a842c7
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_P_vs_NP,_Zero-Knowledge_Proofs,_Quantum_Computation_Avi_Wigderson_en.txt
Video: https://www.youtube.com/watch?v=5GUcvSAJcJw

[L369] [16:33.60] all problems in NP. If you solve one
[L370] [16:36.96] efficiently, you solved all efficiently.
[L371] [16:39.76] If you prove one hard then you proved
[L372] [16:42.80] all of them hard. So they somehow
[L373] [16:44.32] capture the complexity of the class and
[L374] [16:46.64] traveling salesman is an example and
[L375] [16:49.52] protein fodic in this framework of
[L376] [16:52.96] energy minimization is one and
[L377] [16:55.20] banability and so on. Okay. So you want
[L378] [16:59.04] to optimize something and it's np
[L379] [17:01.84] complete np hard. Uh so that's a sign
[L380] [17:07.04] that you shouldn't try to find an
[L381] [17:09.04] algorithm that works always. But one
[L382] [17:11.44] thing you can do is do an approximation.
[L383] [17:13.84] That's a very natural relaxation. You
[L384] [17:15.92] don't want the optimum. You are willing
[L385] [17:17.68] to live with a factor of two from
[L386] [17:19.60] optimum or 10% from optimum or some
[L387] [17:23.04] factor away from optimum.
[L388] [17:25.52] Uh
[L389] [17:27.44] NP completeness was discovered in the
[L390] [17:29.92] early 70s. In the early 90s there was a
[L391] [17:33.12] breakthrough called the PCP theorem. The
[L392] [17:35.76] PCPCOM allows you to argue hardness of
[L393] [17:38.96] even approximation problems.
[L394] [17:41.84] So for example you can show that uh uh
[L395] [17:46.88] satisfiability of banan formulas
[L396] [17:51.60] um you know it's not just so you you
[L397] [17:54.72] want to meet you want to let's say find
[L398] [17:57.28] an assignment to a bunch of constraints
[L399] [18:00.32] let's say bulam constraints let's say on
[L400] [18:02.64] three variables for simplicity
[L401] [18:06.56] uh so you want to satisfy all of them uh
[L402] [18:09.28] the the relaxation would be Okay, I want
[L403] [18:11.60] to satisfy 90% of them or as good a
[L404] [18:15.44] fraction as I can. if I cannot get 100%
[L405] [18:18.48] of them the PCP theorem one way to
[L406] [18:21.76] phrase it and certainly one of the
[L407] [18:23.60] consequence major consequence is that we
[L408] [18:27.28] know that you cannot even achieve a very
[L409] [18:29.84] good approximation and to illustrate how
[L410] [18:33.84] uh uh you know tight this understanding
[L411] [18:37.60] is for some problems is that for the
[L412] [18:40.72] example I gave when there are only three
[L413] [18:43.04] variables per constraint if you just
[L414] [18:46.56] guess at random the values to the
[L415] [18:49.04] variables in the assignment you will
[L416] [18:51.12] satisfy uh 78 of the constraints. This
[L417] [18:55.52] is because each particular constraint is
[L418] [18:58.72] usually the disjunction of three
[L419] [19:00.48] variables will be true with probability
[L420] [19:02.88] it's an or three will be with
[L421] [19:06.48] probability 78. So if you random if you
[L422] [19:09.28] don't think don't look at the formula
[L423] [19:11.20] even you can satisfy
[L424] [19:13.68] 78 of them and the PCP theorem and
[L425] [19:18.48] significant strengthening by hustad
[L426] [19:21.28] hustad tells you that if you want to
[L427] [19:24.56] satisfy 78 plus epsilon
[L428] [19:28.00] that's already npr
[L429] [19:30.24] so we know today to argue the difficulty
[L430] [19:33.84] not only of finding the perfect solution
[L431] [19:36.88] the optim optimal solution. But even uh
[L432] [19:40.08] how close to optimal you can get uh for
[L433] [19:45.92] lots and lots of problems large classes
[L434] [19:48.00] of problems in particular constraint
[L435] [19:50.32] optimization problems uh you know of the
[L436] [19:53.92] type of such fabric. So even if you
[L437] [19:57.92] solve just the slightest epsilon for any
[L438] [20:02.40] trivially small epsilon,
[L439] [20:04.88] >> it's just as hard as doing the full
[L440] [20:06.56] >> as hard as finding the optimum. So
[L441] [20:09.36] >> you mentioned uh MP hard, nplete, you
[L442] [20:12.96] know, NP. I know there's other
[L443] [20:16.00] complexity classes. Maybe you could give
[L444] [20:19.20] some more context on kind of the whole
[L445] [20:21.28] space of complexity classes.
[L446] [20:23.04] >> Yeah. So uh I'm just remark that uh we
[L447] [20:26.48] have a zoo of complexity classes and in
[L448] [20:29.76] fact there's a website called uh yeah
[L449] [20:32.80] the complexity zoo which has in it
[L450] [20:35.52] hundreds of uh hundreds and hundreds of
[L451] [20:39.60] complexity classes of all types
[L452] [20:43.92] websites started by Scott Arson once we
[L453] [20:47.04] realized that there he realizes
[L454] [20:50.56] there's a whole zoo out there we want to
[L455] [20:52.72] know the relationship between these
[L456] [20:54.48] classes. Okay. So what uh what is the
[L457] [20:57.92] point about these classes? Uh like P and
[L458] [21:00.88] NP we want to classify problems by the
[L459] [21:05.36] amount of resources they take. So P
[L460] [21:09.60] polinomial time is a class of problem
[L461] [21:12.48] that can be solved in an amount of time
[L462] [21:15.68] that relates polomially to the size of
[L463] [21:18.64] the data. Of course you expect that you
[L464] [21:21.04] the data there's more data the instance
[L465] [21:23.68] grows you'll spend more time but if it's
[L466] [21:27.12] you know linear time or quadic time or
[L467] [21:29.36] cubic time you say let me call it at
[L468] [21:33.20] least theoretically efficient
[L469] [21:36.00] and uh uh np uh you classify not the
[L470] [21:42.64] time to solve but the time to verify a
[L471] [21:45.12] solution if it was given you want this
[L472] [21:47.20] to be a polomial time. So it's a very
[L473] [21:49.60] different but uh first of all there are
[L474] [21:54.00] you know many more time functions that
[L475] [21:56.40] just polomial and exponential and uh and
[L476] [22:01.92] you know doubly exponential and you can
[L477] [22:04.00] go to finite and uh uh you know one
[L478] [22:09.20] fundamental result starting with
[L479] [22:11.20] Turing's paper is that there are
[L480] [22:13.44] problems that are simply unsolvable by
[L481] [22:16.08] computers. So really the first comp
[L482] [22:18.16] complexity class is a class of solvable
[L483] [22:21.12] problems, decidable problems to ensure
[L484] [22:24.48] that these are not all problems. There
[L485] [22:26.40] are natural problems that are not
[L486] [22:27.84] decidable at all. But time is only one
[L487] [22:31.12] resource and uh we are interested and
[L488] [22:34.40] you know both from practical and
[L489] [22:35.84] theoretical reasons in lots of other
[L490] [22:37.68] resources. Memory is a resource costly
[L491] [22:40.72] resource and we want to minimize space.
[L492] [22:43.04] the space invested in in a computation
[L493] [22:47.28] uh in in problems with several parties.
[L494] [22:50.40] You are interested in the amount of
[L495] [22:51.92] communication exchange. So not the
[L496] [22:55.44] internal computational
[L497] [22:57.92] effort that they exert themselves but
[L498] [23:00.24] how much you know if you talk to a
[L499] [23:02.72] satellite you want to minimize the
[L500] [23:05.44] communication. You can think about
[L501] [23:07.12] energy. You can think about uh yeah
[L502] [23:09.92] there there are plenty of your parallel
[L503] [23:12.48] time. How much can you speed up you know
[L504] [23:16.08] computation of a problem if you work on
[L505] [23:17.92] it not with one computer but with n
[L506] [23:20.64] computers if you your data is of size
[L507] [23:22.96] then you know does it you know allow it
[L508] [23:25.52] to solve it immediately or maybe it
[L509] [23:28.32] doesn't help at all. So there are
[L510] [23:30.88] complexity classes
[L511] [23:33.60] classify problems according to how much
[L512] [23:35.84] resources they need and there are many
[L513] [23:38.08] of these and one important part of so
[L514] [23:40.96] that's a a major theme in the
[L515] [23:43.44] methodology of comp complex complexity
[L516] [23:47.44] theory and uh coming with it is uh
[L517] [23:53.60] attempts to understand complexity
[L518] [23:55.52] classes
[L519] [23:57.28] as problems that relate to each other
[L520] [24:00.24] even if you don't know their complexity.
[L521] [24:02.08] So for example, MP is a class and we
[L522] [24:06.24] don't know the complexity of all
[L523] [24:07.68] problems in this or MP complete
[L524] [24:09.44] problems. We don't know whether they are
[L525] [24:10.80] all easy or or hard but we do know we
[L526] [24:14.08] have efficient algorithms to translate
[L527] [24:16.24] one into the other.
[L528] [24:18.64] So it's not obvious that if you want to
[L529] [24:22.64] uh solve a satisfiability problem you
[L530] [24:24.64] don't know how but you have an algorithm
[L531] [24:27.04] to solve sudoku problems
[L532] [24:29.92] uh without not just 3x3 but also 4 by if
[L533] [24:33.60] you had a an efficient method to solve
[L534] [24:36.48] sudoku problems P equals NP because you
[L535] [24:40.80] can efficiently take an instance of
[L536] [24:44.32] subscribability or so salesman or
[L537] [24:47.28] factoring integer or any of these
[L538] [24:49.68] problems be from it the sudoku problem
[L539] [24:53.84] and from the solution of the sudoku
[L540] [24:56.08] problem you can translate back and get
[L541] [24:59.12] the best solution for your original I
[L542] [25:01.84] know traveling salesman tool so we are
[L543] [25:05.12] interested in uh efficient reductions
[L544] [25:07.68] between problems whose complexity we
[L545] [25:10.24] don't know but we want to relate them to
[L546] [25:12.88] each other we build some kind of partial
[L547] [25:15.12] order of the hardness of uh different
[L548] [25:19.36] problems. So there yeah really yeah you
[L549] [25:23.12] don't want to know how many uh problems
[L550] [25:26.32] we have some arise for constraints that
[L551] [25:28.88] the real world maybe technology
[L552] [25:32.00] imposes or cause for and some are
[L553] [25:34.16] naturally arising mathematically because
[L554] [25:37.12] you know they're interesting.
[L555] [25:39.04] >> You mentioned that these NPcomplete
[L556] [25:40.96] problems they kind of are all equivalent
[L557] [25:43.44] in some way. What's the the proof to you
[L558] [25:47.44] know equate a SAT solving problem to
[L559] [25:50.96] like a graph coloring problem or
[L560] [25:52.64] something like that? Are they all
[L561] [25:54.32] similar in nature or are they kind of
[L562] [25:55.92] bespoke to you know the problem you're
[L563] [25:57.76] going to and from? is a very good
[L564] [25:59.84] question and uh uh you will find that in
[L565] [26:04.08] most of these they call them reductions
[L566] [26:06.96] algorithms to translate one problem to
[L567] [26:09.28] another uh most of them are relatively
[L568] [26:12.72] simple and uh not all and I talked about
[L569] [26:17.44] the PCP theorem before showing that
[L570] [26:19.92] approximation is is all this is very
[L571] [26:23.44] highly non trivial but most computers
[L572] [26:26.00] proof like between coloring and satis
[L573] [26:28.40] satisfiability and it goes both ways.
[L574] [26:31.04] They are both complete. So it goes both
[L575] [26:33.28] ways. It is simple and the first one
[L576] [26:38.08] uh was the satisfiability problem. The
[L577] [26:40.40] you know original papers of cook and
[L578] [26:42.32] leaven defining NP completeness and
[L579] [26:45.44] proving that NP complete problems exist.
[L580] [26:48.88] They both uh the first problem they push
[L581] [26:52.40] complete was satisfiability.
[L582] [26:55.12] Why is this? So why can all these other
[L583] [26:58.56] problems be reduced to satisfiability?
[L584] [27:01.84] The reason is really that computation is
[L585] [27:05.60] local.
[L586] [27:07.68] Uh
[L587] [27:09.20] computation is local. I mean that if you
[L588] [27:12.08] think about your computer, your laptop
[L589] [27:13.84] or any any computational device, usually
[L590] [27:16.96] it manipulates bits uh uh by some local
[L591] [27:22.00] operations. You look at this these two
[L592] [27:24.24] registers and you add them or you take
[L593] [27:27.36] these two bits and exclusive all them or
[L594] [27:30.16] end them or something and you will do a
[L595] [27:32.56] sequence of this sequence of simple
[L596] [27:34.72] operations and you arrive at a
[L597] [27:37.04] conclusion. This locality can be
[L598] [27:39.12] translated
[L599] [27:40.64] to
[L600] [27:42.16] uh a bunch of constraints or what would
[L601] [27:45.04] be consistent sequence of states of your
[L602] [27:47.76] machine. If you look at the time
[L603] [27:50.32] evolution of any computation, you know,
[L604] [27:53.12] memories in some state then in another
[L605] [27:55.76] state and but they change locally. Okay.
[L606] [27:58.88] So if you had the if you could guess and
[L607] [28:01.52] that's the NP part. I mean if somebody
[L608] [28:03.36] provided you the table of computation,
[L609] [28:05.68] you could check that it's consistent by
[L610] [28:08.56] writing a bunch of local constraints. So
[L611] [28:11.36] you know some conjunction of very few
[L612] [28:13.44] variables
[L613] [28:15.04] uh
[L614] [28:17.12] uh on all over this table of computation
[L615] [28:21.68] uh and write down a satisfiability
[L616] [28:24.16] problem. I want this to be true and this
[L617] [28:26.96] to be true and this to be true for some
[L618] [28:29.52] assignment and what does the assignment
[L619] [28:31.84] has to satisfy it should be a table like
[L620] [28:34.64] this all these constraints should be
[L621] [28:36.56] satisfi you know should be true and
[L622] [28:40.16] it has to be consistent with the input
[L623] [28:42.32] given right so some of the input has to
[L624] [28:45.12] match the first time zero uh content of
[L625] [28:49.04] the of the machine so this locality uh
[L626] [28:53.44] allows for many of these translations.
[L627] [28:56.48] If you realize this, you will quickly
[L628] [29:00.24] find a reduction from coloring to satis.
[L629] [29:04.08] It's also I mean it's not clear why
[L630] [29:06.00] coloring is an evolution of computation
[L631] [29:08.48] but it's starts already by local
[L632] [29:12.00] constraints. you want a few colors and
[L633] [29:13.92] that every so some in some it's even
[L634] [29:16.32] easier but uh um the reduction from any
[L635] [29:22.64] NP computation that's that's what NP
[L636] [29:25.12] computers means anything in NP can be
[L637] [29:27.76] translated to satisfiability NP is just
[L638] [29:30.80] a computation of a touring machine say
[L639] [29:35.84] uh only that you don't know what is a
[L640] [29:38.64] computation if somebody guessed it or
[L641] [29:41.44] showed it to you then you all you need
[L642] [29:43.92] is to verify this verification is local
[L643] [29:47.20] and that's the source of many simple uh
[L644] [29:50.56] you know uh MP completeness reductions
[L645] [29:53.84] let let me give you a a really simple
[L646] [29:56.88] example why why uh is factoring integers
[L647] [30:01.76] reducible to
[L648] [30:03.92] uh satisfiability
[L649] [30:07.04] because if I gave you factors of an
[L650] [30:10.56] integer you could just multiply them and
[L651] [30:13.44] check that they equal the input. This
[L652] [30:16.32] multiplication is a is a simple
[L653] [30:19.52] algorithm, right? I mean, we know how to
[L654] [30:22.00] do it from second grade or something. Uh
[L655] [30:24.80] you write down the computation of
[L656] [30:26.48] multiplication in this local way and all
[L657] [30:30.08] you need is that uh somebody will guess
[L658] [30:32.96] for you really the factors. You
[L659] [30:35.68] mentioned time complexity and space
[L660] [30:38.00] complexity and I think intuitively like
[L661] [30:40.96] in software engineering we often trade
[L662] [30:43.68] those off for each other. Is there uh
[L663] [30:46.40] like general theory on that on how these
[L664] [30:48.80] two trade off?
[L665] [30:50.56] >> Yeah. Yeah. We have uh yeah all these
[L666] [30:53.12] questions are natural questions for uh
[L667] [30:55.68] complexity theorist. uh how does two
[L668] [30:58.80] resources relate to each other and
[L669] [31:00.96] whether they they can trade off or maybe
[L670] [31:03.12] you can minimize them both at the same
[L671] [31:05.68] time. Uh and uh it depends on the
[L672] [31:09.92] problem. There are there are problems
[L673] [31:12.00] for which uh we know results like
[L674] [31:15.52] multiply time and space it has to be at
[L675] [31:18.96] least the square of the length of the
[L676] [31:22.48] input. So you can either do it with very
[L677] [31:26.48] small space like logarithmic space but
[L678] [31:29.04] you need to pay maybe quadratic time
[L679] [31:32.56] and uh if you want linear time you have
[L680] [31:36.96] to pay linear space or close to linear
[L681] [31:40.24] space. There are results of this type uh
[L682] [31:43.44] in in various models of computation.
[L683] [31:46.16] That's another thing you play with. Not
[L684] [31:48.80] all of them are you know they are all
[L685] [31:50.24] equivalent in principle but if you care
[L686] [31:52.88] about exact time or exact space are not
[L687] [31:55.60] equivalent. So there are problems for
[L688] [31:57.84] which there is a tradeoff there are
[L689] [32:00.00] problems for uh you know where you can
[L690] [32:02.16] solve them in linear time and
[L691] [32:03.76] logarithmic space. One very important
[L692] [32:07.44] general result that is a breakthrough
[L693] [32:09.44] from last year is a result of Ryan
[L694] [32:12.64] Williams. Uh and I'll tell you what it
[L695] [32:15.36] is, but I first describe what we knew
[L696] [32:17.36] about time and space. There's a clear
[L697] [32:20.48] inequality, right? If you run in time t,
[L698] [32:24.08] you will never use more than space t
[L699] [32:28.00] because you never visit so many cells or
[L700] [32:31.04] registers in your machine. So space is
[L701] [32:34.80] at most time.
[L702] [32:36.96] 50 years ago valant Paul and Piper uh
[L703] [32:40.64] improved this a little bit. They said
[L704] [32:42.32] that if you run time t there's an
[L705] [32:45.12] equivalent computation that will do this
[L706] [32:47.44] in slightly less space than t t over log
[L707] [32:50.96] t. That was a big result. Uh the running
[L708] [32:55.20] time of course will blow up. it will be
[L709] [32:57.52] very very expensive time-wise but at
[L710] [33:00.16] least you can save on space a little bit
[L711] [33:02.56] and uh this was uh believed almost 50
[L712] [33:07.68] years to be the best you can do in fact
[L713] [33:10.32] we had arguments that in certain models
[L714] [33:12.96] in certain stylized models of
[L715] [33:15.04] computation
[L716] [33:16.72] uh you cannot improve that I not
[L717] [33:20.24] describe you know this restricted models
[L718] [33:23.52] but some natural restricted models
[L719] [33:26.40] You cannot beat this.
[L720] [33:29.68] And what Ryan Williams descri
[L721] [33:33.12] found out last year is that in fact much
[L722] [33:36.32] better can be done. Any computation that
