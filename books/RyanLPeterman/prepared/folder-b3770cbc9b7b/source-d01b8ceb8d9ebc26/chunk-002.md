Chunk 2; segments 384–791. Start may repeat the previous chunk for context.

# MIT Professor: Leetcode, P vs NP, SAT Solvers | Ryan Williams

Source ID: source-d01b8ceb8d9ebc26
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/MIT_Professor_Leetcode,_P_vs_NP,_SAT_Solvers_Ryan_Williams_en.txt
Video: https://www.youtube.com/watch?v=AaK1SL2i_4Y

[L393] [14:10.68] the target sum, right?
[L394] [14:11.92] >> Yeah, so the idea is um
[L395] [14:14.88] nobody said I had to use a polynomial
[L396] [14:17.00] time reduction or something like that to
[L397] [14:19.68] reduce one problem to another.
[L398] [14:21.96] So so what's what happened what happened
[L399] [14:24.68] the trick was I took this subset sum
[L400] [14:27.84] problem that had n numbers
[L401] [14:30.04] and then I blew it up
[L402] [14:32.48] to an instance of this two sum problem.
[L403] [14:35.04] But that two sum problem has about
[L404] [14:37.24] square root of 2 to the n numbers.
[L405] [14:40.00] Now I can solve two sum in linear time.
[L406] [14:42.92] So that so solving that instance gives
[L407] [14:45.52] me a square root of 2 to the n time
[L408] [14:47.76] algorithm for the original problem.
[L409] [14:49.64] But yeah, in in the meantime, going from
[L410] [14:52.24] one problem to the other, I blew it up.
[L411] [14:54.48] And I but by blowing it up, I I'm able
[L412] [14:56.92] to improve the time complexity of the
[L413] [14:59.36] obvious algorithm for subset sum.
[L414] [15:02.00] >> I get it. Okay, so the reduction
[L415] [15:04.36] it it's kind of like the
[L416] [15:06.76] if you solve the subset sum, you have
[L417] [15:09.44] some time complexity, and if you
[L418] [15:11.56] translate it to the other problem, you
[L419] [15:13.36] lose a little bit of time complexity,
[L420] [15:14.92] but less than the aggregate.
[L421] [15:17.32] >> So all you want to make sure is when all
[L422] [15:19.48] the dust is cleared and settled, you
[L423] [15:21.44] want to be able to say, "Look, if I can
[L424] [15:23.64] improve
[L425] [15:25.00] the obvious algorithm for two sum,
[L426] [15:27.28] then I can improve the obvious algorithm
[L427] [15:28.92] for subset sum." And that's what this
[L428] [15:30.36] thing achieves.
[L429] [15:31.96] Right? Because I know because I know how
[L430] [15:33.68] to get a faster algorithm for two sum,
[L431] [15:36.52] I can get one for subset sum. So, so you
[L432] [15:39.64] just want your your reduction between
[L433] [15:42.00] two problems to have this property. If I
[L434] [15:43.60] can improve
[L435] [15:44.84] one problem by a little bit in running
[L436] [15:46.88] time, I can improve the other problem by
[L437] [15:48.80] a little bit.
[L438] [15:50.04] >> In one of your talks, you you mentioned
[L439] [15:52.52] preserving magic between Okay, so this
[L440] [15:55.36] is that.
[L441] [15:56.20] >> this is exactly like preserving magic
[L442] [15:58.16] because
[L443] [15:58.88] >> Well, I mean,
[L444] [15:59.80] >> once you see the two sum solution, it's
[L445] [16:01.52] not so magical anymore. But, imagine
[L446] [16:04.83] >> [laughter]
[L447] [16:05.12] >> that you didn't know about sorting and
[L448] [16:08.00] binary search and the like, and someone
[L449] [16:10.72] just says, "Find a pair of things with a
[L450] [16:13.76] certain property, and there are n
[L451] [16:15.72] things."
[L452] [16:16.92] And you're like, "Well, I mean, all the
[L453] [16:19.04] number of possible pairs
[L454] [16:21.00] is about n squared, so maybe it'll take
[L455] [16:23.04] me n squared."
[L456] [16:24.32] In this particular case, because they're
[L457] [16:26.56] numbers and you're summing them,
[L458] [16:28.52] there's an n log n time algorithm. It is
[L459] [16:30.96] a It is a surprise when you first see
[L460] [16:33.72] that no, you don't have to try all of
[L461] [16:36.48] the pairs of numbers. There is a
[L462] [16:38.44] shortcut. There is a clear shortcut that
[L463] [16:41.24] lets you find a pair much faster.
[L464] [16:44.12] And then, you can use that uh
[L465] [16:47.04] surprise um
[L466] [16:49.28] or magic, if you will, and get something
[L467] [16:53.00] for a subset sum. Get a algorithm for
[L468] [16:54.68] subset sum that avoids trying all of the
[L469] [16:58.24] two to the n subsets.
[L470] [17:00.12] >> So, I understand one of the the driving
[L471] [17:03.32] motives for pursuing this, I guess,
[L472] [17:06.08] lowering of lower bounds
[L473] [17:08.12] is that
[L474] [17:09.76] um
[L475] [17:10.76] strong exponential time hypothesis, or I
[L476] [17:12.96] see it, you know, SETH.
[L477] [17:15.68] Um could you explain that and its
[L478] [17:17.72] significance?
[L479] [17:18.80] >> Strong ETH is like a severe
[L480] [17:21.08] strengthening
[L481] [17:22.60] of the P versus NP question.
[L482] [17:25.56] So,
[L483] [17:26.72] P versus NP
[L484] [17:28.24] is um, asking whether the SAT problem
[L485] [17:32.88] um,
[L486] [17:34.04] has a polynomial time algorithm or not.
[L487] [17:37.88] Right? And
[L488] [17:39.24] strong ETH
[L489] [17:40.96] is basically saying that
[L490] [17:44.40] for the SAT problem,
[L491] [17:46.72] uh, you cannot solve it
[L492] [17:48.96] faster
[L493] [17:50.56] than much faster than two to the end.
[L494] [17:53.16] So, there's no 1.999
[L495] [17:56.52] to the end time algorithm.
[L496] [17:58.48] For every string of nines, there is no
[L497] [18:01.00] 1.9999 to the end time algorithm.
[L498] [18:05.04] Um, to say the hypothesis totally
[L499] [18:07.64] precisely, it has to do with the K-SAT
[L500] [18:09.88] problem
[L501] [18:11.12] and you're looking at
[L502] [18:13.52] clauses of
[L503] [18:15.24] length K for arbitrary K, but
[L504] [18:19.00] um,
[L505] [18:20.12] those details don't matter so much. It's
[L506] [18:22.08] a canonically NP-complete problem. SAT
[L507] [18:24.92] is solved all the time in practice. It's
[L508] [18:29.88] extremely useful for a verification
[L509] [18:32.64] nowadays. It's an It's an engine
[L510] [18:35.56] for verification. Um, so it can be
[L511] [18:38.48] solved fairly well in practice.
[L512] [18:41.40] However, in the worst case, we still
[L513] [18:43.80] don't know how to solve it uh,
[L514] [18:46.12] significantly faster than two to the
[L515] [18:48.44] end.
[L516] [18:49.28] So, the hypothesis that it needs, say,
[L517] [18:52.00] 1.99999
[L518] [18:53.68] to the end time for all strings of nines
[L519] [18:56.44] is a very strong
[L520] [18:58.72] exponential time hypothesis. It's way
[L521] [19:01.28] stronger than P versus NP. It says, "Uh,
[L522] [19:03.32] no, no, no, no. It's not super
[L523] [19:04.88] polynomial. It's actually darn near two
[L524] [19:07.24] to the end time that you need."
[L525] [19:09.32] Right?
[L526] [19:09.80] >> And so, do you think that hypothesis is
[L527] [19:12.80] true and you know, why or why not?
[L528] [19:15.76] >> I think I'm on the record as not
[L529] [19:17.60] believing this hypothesis. Yeah. Um
[L530] [19:22.12] Yeah, why don't I believe this
[L531] [19:23.84] hypothesis?
[L532] [19:25.16] Um
[L533] [19:26.88] Well, I started thinking about this
[L534] [19:28.12] hypothesis
[L535] [19:30.48] maybe already as an
[L536] [19:32.72] undergrad, but certainly starting
[L537] [19:35.92] in grad school.
[L538] [19:37.56] Like early in grad school I was thinking
[L539] [19:39.20] about this. So, before it was even
[L540] [19:41.32] called strong ETH, I guess that shows
[L541] [19:43.80] how old I am.
[L542] [19:45.04] I was trying to think about how to solve
[L543] [19:48.52] the so-called CNF SAT problem faster
[L544] [19:51.36] than 2 to the n.
[L545] [19:52.80] And
[L546] [19:54.32] well, at the time
[L547] [19:56.16] there were a number of other NP-complete
[L548] [19:59.28] problems that had faster algorithms like
[L549] [20:01.88] subset sum.
[L550] [20:03.64] So, I thought, well, there's not I mean,
[L551] [20:06.68] what's so special about SAT? Like, if
[L552] [20:09.32] all these other problems have faster
[L553] [20:11.40] algorithms um why not SAT as well? Like
[L554] [20:15.92] if you restrict to the 3-SAT problem
[L555] [20:19.52] like So, this is where
[L556] [20:21.72] you have an AND of these clauses, each
[L557] [20:25.44] clause has like is an OR of three
[L558] [20:29.36] variables some of the variables may be
[L559] [20:31.52] negated.
[L560] [20:32.84] You want to know if there's a way to set
[L561] [20:34.12] all the variables to make all the
[L562] [20:35.80] clauses simultaneously true. Um there is
[L563] [20:38.84] a faster algorithm for that.
[L564] [20:40.68] Um but this is a more general version of
[L565] [20:43.20] SAT. Um
[L566] [20:45.40] So, at first I just thought, well,
[L567] [20:47.24] there's no good reason to think in a
[L568] [20:49.20] lower bound these other related problems
[L569] [20:50.76] have upper bounds.
[L570] [20:52.68] So, why not?
[L571] [20:54.08] But then
[L572] [20:55.48] um over time I would have different
[L573] [20:58.24] attacks
[L574] [20:59.92] on strong ETH, like trying to refute it.
[L575] [21:02.40] Always trying to refute it in different
[L576] [21:04.96] ways, these attacks would fail
[L577] [21:08.36] in some completely catastrophic and
[L578] [21:12.72] ridiculous way, like um they would like
[L579] [21:16.68] have no chance of
[L580] [21:18.64] actually solving the original problem.
[L581] [21:21.44] But by sort of staring at my failure and
[L582] [21:24.56] trying to think, well, there's something
[L583] [21:26.52] interesting happening here. What can I
[L584] [21:28.08] do with this? Like there's something
[L585] [21:30.80] interesting. Yeah, it doesn't refute uh
[L586] [21:34.28] the strong ETH thing.
[L587] [21:36.44] What does it do? So, by trying to pivot
[L588] [21:39.28] and and figure out, okay, what can I do
[L589] [21:41.12] with my failure?
[L590] [21:42.76] I was able to solve a like a variety of
[L591] [21:45.80] other problems instead.
[L592] [21:47.80] And so, after a while, I realized the
[L593] [21:50.68] truth value
[L594] [21:52.32] of strong ETH to me
[L595] [21:54.68] is almost irrelevant. Like because if I
[L596] [21:57.28] believe that it's false, then I get good
[L597] [22:00.24] ideas.
[L598] [22:01.68] I get I get good ideas. Like
[L599] [22:04.28] And so, by trying to think about, okay,
[L600] [22:08.64] what would an algorithm that breaks
[L601] [22:11.60] through the end look like? What could it
[L602] [22:13.72] look like?
[L603] [22:15.40] I I sort of force myself to think in a
[L604] [22:18.00] different way.
[L605] [22:19.44] Like I I I have to like discard
[L606] [22:21.92] other natural algorithmic possibilities
[L607] [22:24.04] because we know they they won't work.
[L608] [22:27.20] Um
[L609] [22:27.88] and I have to think in a in a different
[L610] [22:31.40] direction. And and so,
[L611] [22:33.32] because it kind of like sends my brain
[L612] [22:36.00] in a different direction, sends me
[L613] [22:37.56] thinking a different way,
[L614] [22:39.76] it's very useful for research.
[L615] [22:42.28] You know, you you
[L616] [22:43.36] I mean, even even though I still haven't
[L617] [22:45.40] refuted it or whatever, like it's very
[L618] [22:48.24] useful for me to believe that it's
[L619] [22:50.24] false. Like operationally.
[L620] [22:52.68] So, the truth value, well, I mean
[L621] [22:55.96] I believe this is a minority opinion,
[L622] [22:57.64] right? Why why would they go against I
[L623] [23:00.08] mean, I think um
[L624] [23:02.64] for example, Russell and Piazzo, good
[L625] [23:05.48] friend of mine who uh, helped propose
[L626] [23:08.04] this.
[L627] [23:08.92] I mean, he always emphasizes to me,
[L628] [23:11.12] "Well, this this is a hip hypothesis.
[L629] [23:13.52] It, you know, we didn't We explicitly
[L630] [23:15.08] did not name it a conjecture."
[L631] [23:17.20] We wanted to sort of put forth
[L632] [23:19.96] some lower bound that would get you to
[L633] [23:22.28] think about it. Like something that's
[L634] [23:24.96] maybe a little more controversial than
[L635] [23:27.20] the other types of things like P = NP or
[L636] [23:30.52] whatever. Or, you know, like other
[L637] [23:32.36] things that people more nor- normally
[L638] [23:33.92] believe. So, like hypothesis, which are
[L639] [23:36.28] at the edge of our understanding,
[L640] [23:39.04] can be enlightening to think about. Like
[L641] [23:41.80] where we truly don't know what the
[L642] [23:45.28] answer might be based on our intuition.
[L643] [23:48.48] Um,
[L644] [23:49.92] so this this is, I guess, one reason why
[L645] [23:52.32] it was
[L646] [23:53.36] proposed, but one reason why you might
[L647] [23:56.64] believe that strong ETH is true is
[L648] [23:59.16] because believing it implies a lot of
[L649] [24:01.76] other lower bounds for you conveniently
[L650] [24:04.80] because you can reduce the SAT problem
[L651] [24:07.16] to a bunch of other problems that seem
[L652] [24:09.00] totally unrelated like edit distance,
[L653] [24:12.80] um, various pattern matching problems.
[L654] [24:17.20] Um, they have natural
[L655] [24:20.52] polynomial time solutions if you can
[L656] [24:22.28] improve on the algorithms for any of
[L657] [24:24.92] those, you would improve the one for SAT
[L658] [24:27.52] as well. You would get something better
[L659] [24:28.84] than 2 to the n. So, believing in it
[L660] [24:31.60] sort of makes a convenient world view.
[L661] [24:34.28] It shows that all these different
[L662] [24:35.80] textbook algorithms are indeed optimal.
[L663] [24:38.44] >> We've talked about SAT or we've
[L664] [24:39.88] mentioned SAT so many times in this
[L665] [24:42.16] conversation. I know there's so many
[L666] [24:44.12] forms of that problem. What are all the
[L667] [24:46.88] different forms? And I know there's
[L668] [24:48.36] there's clause width, also this idea of
[L669] [24:50.36] depth, too.
[L670] [24:51.52] >> Um, the most common
[L671] [24:54.08] representation of a of a SAT formula is
[L672] [24:58.32] the conjunctive normal form, so-called
[L673] [25:00.88] CNF representation. And this is what
[L674] [25:04.00] modern SAT solvers get as input. They
[L675] [25:06.92] They get their file in in so-called
[L676] [25:09.32] DIMACS CNF form. And this is
[L677] [25:13.52] just every line of my file, I give you a
[L678] [25:17.76] list of
[L679] [25:19.48] uh variables, possibly with negations,
[L680] [25:22.08] and each one is a clause. And I'm
[L681] [25:24.24] supposed to take the or
[L682] [25:26.36] of those uh
[L683] [25:28.04] uh variables or negations. These are
[L684] [25:29.96] Variables or negations, they're often
[L685] [25:30.92] called literals. Okay, so I take an or
[L686] [25:32.64] of these literals.
[L687] [25:34.08] And
[L688] [25:35.16] the width
[L689] [25:36.36] of that clause is the number of literals
[L690] [25:38.60] in it.
[L691] [25:39.88] Okay?
[L692] [25:41.04] And
[L693] [25:42.32] um I'm supposed to take the and over all
[L694] [25:45.96] those lines, each line in my DIMACS CNF
[L695] [25:49.20] file.
[L696] [25:50.28] And so it's an and
[L697] [25:52.08] of a bunch of ors, and each or has
[L698] [25:57.20] some small number of literals in it.
[L699] [25:59.08] Call it K. So usually the the width is
[L700] [26:01.28] called K.
[L701] [26:02.52] And so the K-SAT problem is to find an
[L702] [26:05.56] assignment to all the variables that
[L703] [26:07.68] satisfies all the clauses when each
[L704] [26:10.60] clause has width K
[L705] [26:13.28] or width at most K.
[L706] [26:14.96] It could be smaller.
[L707] [26:16.60] Um so that's the most popular
[L708] [26:20.08] uh version. That's what
[L709] [26:22.16] SAT solvers, you know, turn on.
[L710] [26:25.00] And that's what is behind uh strong ETH.
[L711] [26:28.28] That's the representation there.
[L712] [26:30.60] Um but there are other ways uh to
[L713] [26:33.32] represent
[L714] [26:34.80] a Boolean formula. You could just simply
[L715] [26:36.80] represent it as some arbitrary
[L716] [26:39.32] expression
[L717] [26:40.68] made out made up of ors and ands and
[L718] [26:44.28] negations. It could just be some
[L719] [26:46.00] arbitrary expression with nested
[L720] [26:47.28] parentheses
[L721] [26:48.76] and all that mess. Um
[L722] [26:51.12] you could ask you know, given a formula
[L723] [26:53.64] in this representation with a bunch of
[L724] [26:56.04] variables, is there a way to set the
[L725] [26:57.72] variables to make this true? That's
[L726] [26:59.84] formula SAT.
[L727] [27:01.44] Um, you could also look at
[L728] [27:06.04] at circuits of bounded depth, as you
[L729] [27:09.04] mentioned. So,
[L730] [27:10.76] there is this
[L731] [27:12.40] um, this class of circuits that people
[L732] [27:14.56] study
[L733] [27:15.68] called uh AC uh circuits for alternating
[L734] [27:19.24] circuits. Um, it doesn't mean
[L735] [27:21.68] alternation in terms of electricity, it
[L736] [27:24.52] means alternation in terms of
[L737] [27:27.04] uh ORs and ANDs. So, these circuits are
[L738] [27:30.20] made up of uh ORs and ANDs like in
[L739] [27:34.92] layers. So, the CNF representation is a
[L740] [27:38.00] special case where I have an an AND
[L741] [27:40.84] of ORs like uh
[L742] [27:43.36] like a AND of a bunch of clauses and
[L743] [27:45.08] then ORs of the literals.
[L744] [27:47.00] But, you can go further. You can have an
[L745] [27:48.92] AND of OR of ANDs
[L746] [27:51.72] of variables with negations and things
[L747] [27:53.68] like that. And so, these are uh constant
[L748] [27:57.12] depth AC circuits. And because the idea
[L749] [28:00.60] is
[L750] [28:01.56] uh you only have some constant number of
[L751] [28:03.40] layers of these ANDs and ORs. And you
[L752] [28:05.40] can look at the SAT problem
[L753] [28:07.84] on circuits like that as well, for
[L754] [28:09.44] example. Those are Those are two
[L755] [28:11.84] uh other versions that people look at.
[L756] [28:13.80] >> Yeah, strong ETH is on K-SAT, and I saw
[L757] [28:17.16] on less than or I guess, you know,
[L758] [28:20.56] 2-SAT, 3-SAT, 4-SAT, 5-SAT. There exists
[L759] [28:23.84] solutions that are asymptotically better
[L760] [28:26.32] than 2 to the N. So, I guess it it you
[L761] [28:29.84] know, the
[L762] [28:30.96] the larger K can be, the more difficult
[L763] [28:33.24] the the problem is.
[L764] [28:34.64] >> That That is the intuition.
[L765] [28:36.20] >> I'm curious, have you ever plotted that
[L766] [28:37.84] curve? Like, is it Does it drop off, you
[L767] [28:40.60] know, exponentially or
[L768] [28:41.96] >> Yeah. Yeah. Um, th- yeah, that's what's
[L769] [28:44.68] so interesting uh about the current
[L770] [28:48.28] state of the art in K-SAT algorithms. As
[L771] [28:52.04] K increases,
[L772] [28:53.88] all of them
[L773] [28:55.40] all of the different types of algorithms
[L774] [28:56.88] you might try to run, they all approach
[L775] [29:00.88] a 2 to the n exponent. Like, as K grows
[L776] [29:04.28] and grows and grows, they get 1.99,
[L777] [29:06.88] 1.999, and so on. And yeah, it it drops
[L778] [29:12.20] I mean, it get In other words, it will
[L779] [29:13.32] like it goes towards
[L780] [29:15.32] uh pretty quickly
[L781] [29:17.16] actually. And like so we we understand
[L782] [29:19.40] like how the exponent behaves pretty
[L783] [29:22.04] well for the known algorithms we have.
[L784] [29:24.24] >> And then um for for something like
[L785] [29:26.48] 3-SAT, what is the intuition behind
[L786] [29:29.56] speeding up an exponential time search?
[L787] [29:32.52] >> Yeah, so for 3-SAT, um
[L788] [29:35.44] let's just look at a a single clause,
[L789] [29:37.60] okay? A clause that's got
[L790] [29:39.80] three variables in it, okay?
[L791] [29:42.12] We know that if
[L792] [29:43.68] uh if we set all those three variables
[L793] [29:46.16] wrong, it's going to be false. Okay, so
[L794] [29:48.20] we have to avoid one of those
[L795] [29:50.20] assignments, okay?
[L796] [29:52.04] Well, that means that there are seven
[L797] [29:54.56] out of the eight possible assignments,
[L798] [29:56.68] so there's like three variables,
[L799] [29:58.52] two to the three, eight possible
[L800] [30:00.44] assignments, seven of them could be a
