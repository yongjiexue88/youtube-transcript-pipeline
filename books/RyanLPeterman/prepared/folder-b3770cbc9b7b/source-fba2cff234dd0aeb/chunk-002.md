Chunk 2; segments 419–834. Start may repeat the previous chunk for context.

# Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy

Source ID: source-fba2cff234dd0aeb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_OCaml_Functional_Programming,_Formal_Verification,_Programming_Languages_Xavier_Leroy_en.txt
Video: https://www.youtube.com/watch?v=9Cswiqrq6So

[L428] [15:27.36] Um and and yeah, so so Jane Street for
[L429] [15:30.72] instance and and some of those use OCaml
[L430] [15:33.04] as a filter on on who who they want to
[L431] [15:35.36] hire.
[L432] [15:36.96] Yeah, they have fewer applicants, but in
[L433] [15:39.20] general they have more interesting
[L434] [15:40.92] backgrounds. So
[L435] [15:42.88] um
[L436] [15:44.64] And perhaps one last thing I would like
[L437] [15:46.24] to say, Python is 50% functional
[L438] [15:48.80] language.
[L439] [15:49.88] Okay. Uh
[L440] [15:51.04] a lot of good Python code looks like
[L441] [15:53.32] functional uh code with comprehensions.
[L442] [15:56.32] So I think uh uh
[L443] [15:58.36] people are already halfway uh through
[L444] [16:00.48] through functional programming uh when
[L445] [16:02.64] when when they are comfortable with
[L446] [16:04.12] Python.
[L447] [16:05.72] >> Yeah, when I was learning OCaml in
[L448] [16:07.88] college, I think one thing that really
[L449] [16:10.48] stood out to me and I thought was
[L450] [16:11.96] interesting was this concept of type
[L451] [16:13.96] inference
[L452] [16:15.12] where the compiler is
[L453] [16:17.08] kind of uh it knows the types of
[L454] [16:19.00] everything implicitly in the the way
[L455] [16:21.80] that the code is written.
[L456] [16:23.36] Um can you explain uh type inference and
[L457] [16:25.92] what the advantages are?
[L458] [16:27.88] >> Well, the the basic idea is that uh you
[L459] [16:30.48] don't have to declare the type of every
[L460] [16:32.96] variable you introduce, every function
[L461] [16:35.20] parameter, every local variable because
[L462] [16:37.96] quite often the type can be deduced from
[L463] [16:39.64] the uses of the variable. Okay? Uh like
[L464] [16:43.40] if you do uh I don't know X equals
[L465] [16:45.68] string length of S, uh then you kind of
[L466] [16:48.80] know that S is a string and X is an
[L467] [16:51.16] integer, right? Because that's what the
[L468] [16:52.96] string length function uh that's the
[L469] [16:55.20] type of string length and it it tells
[L470] [16:57.16] you that.
[L471] [16:59.56] Um so so that's the basic idea. Uh
[L472] [17:03.20] now the the actual realization is a
[L473] [17:05.92] little more complicated. Basically, you
[L474] [17:07.60] need to collect a number of con- the
[L475] [17:09.36] compiler needs to collect a number of
[L476] [17:11.24] constraints and then try to solve them.
[L477] [17:14.24] Uh see uh
[L478] [17:16.16] well, if there's no solution, then it's
[L479] [17:17.84] a type error. But, sometimes there are
[L480] [17:19.88] several solutions and you must find good
[L481] [17:22.68] criteria to choose one, otherwise you're
[L482] [17:25.00] I mean, it also needs to be predictable
[L483] [17:27.04] for for programmers.
[L484] [17:28.88] Um, and often also you can you
[L485] [17:32.24] um you can still put type annotation as
[L486] [17:34.12] a programmer you can still put type
[L487] [17:35.44] annotations if that makes the code
[L488] [17:37.12] clearer.
[L489] [17:38.52] So, I think the the the main advantage
[L490] [17:40.56] is precisely to have less verbose code,
[L491] [17:43.28] less verbose code. Well, you don't
[L492] [17:46.68] you don't need to put types everywhere,
[L493] [17:49.08] but only where they help uh
[L494] [17:51.08] documentation and and documenting the
[L495] [17:53.96] code and and making the making it easier
[L496] [17:57.36] to read. Okay.
[L497] [17:59.32] Uh, but quite often you
[L498] [18:02.20] um for for like small local functions,
[L499] [18:05.04] for uh short-lived temporary variables,
[L500] [18:07.76] you you
[L501] [18:09.32] the type is obvious from the context, so
[L502] [18:11.40] let's just omit it.
[L503] [18:13.08] >> If I'm trying to figure out how this
[L504] [18:14.32] type inference works, the intuitive
[L505] [18:16.32] example you said makes sense. But, uh
[L506] [18:18.84] you mentioned it seems to be some sort
[L507] [18:20.28] of system of equations that you solve or
[L508] [18:23.04] something like that. Can you give a uh
[L509] [18:25.32] concrete example maybe, you know, what
[L510] [18:27.36] does that look like to the compiler?
[L511] [18:29.32] >> Okay. Well, for a slightly more complex
[L512] [18:31.48] example, say you have um
[L513] [18:34.32] function with two parameters X and Y,
[L514] [18:36.24] and then you do if X equals Y.
[L515] [18:40.16] So, that tells you that X and Y have the
[L516] [18:41.88] same type, but that still doesn't tell
[L517] [18:43.72] you which type it is, uh assuming a
[L518] [18:46.00] polymorphic uh equality comparison.
[L519] [18:49.76] So, you've learned something about X and
[L520] [18:51.28] Y, that they have the same type, but you
[L521] [18:53.12] still don't know what the type is.
[L522] [18:55.20] And later maybe you will learn something
[L523] [18:56.80] about the type of X.
[L524] [18:58.80] And now you will have determined the
[L525] [19:00.64] type of Y as well.
[L526] [19:02.60] So, so that's the kind of constraints
[L527] [19:04.52] you you you accumulate and solve, um
[L528] [19:07.40] little bit like, you know, Sudoku or uh
[L529] [19:10.56] those kind of puzzles. And then there's
[L530] [19:12.56] the interesting case where you don't
[L531] [19:14.64] have enough constraints to find
[L532] [19:17.04] a unique type.
[L533] [19:18.72] So maybe in the end X and Y will be you
[L534] [19:21.88] know they have the same type but it's
[L535] [19:23.04] still unconstrained.
[L536] [19:24.60] And and then that's where you
[L537] [19:26.68] automatically get polymorphism for free.
[L538] [19:29.28] Okay, the type checker said, "Okay,
[L539] [19:31.00] those types are unconstrained so it can
[L540] [19:33.20] work for any type."
[L541] [19:35.44] So my function can take an X of any type
[L542] [19:37.84] and a Y of the same type. Again, any
[L543] [19:40.68] type and it's a polymorphic function.
[L544] [19:43.36] So there's there's this beautiful I
[L545] [19:45.84] think
[L546] [19:47.48] phenomena phenomenon that that
[L547] [19:50.04] polymorphism can be discovered
[L548] [19:52.92] just by running type inference and
[L549] [19:54.80] noticing that oh there are no
[L550] [19:56.32] constraints so it must be polymorphic.
[L551] [19:59.68] And and that was a great insight by
[L552] [20:01.96] Robin Milner, the British computer
[L553] [20:03.72] scientist pioneer who invented this ML
[L554] [20:05.76] family of languages and and and this
[L555] [20:08.68] kind of type inference in the 70s.
[L556] [20:11.00] Polymorphism
[L557] [20:12.68] was was
[L558] [20:14.56] was not very well understood at the time
[L559] [20:16.64] and so the fact that that he could have
[L560] [20:19.52] he could introduce polymorphism so
[L561] [20:21.64] easily in his language just as a
[L562] [20:23.68] consequence of type inference
[L563] [20:26.08] was a beautiful discovery.
[L564] [20:28.56] >> So for type inference it seems like the
[L565] [20:30.88] benefit is
[L566] [20:33.40] you know the code is going to be a lot
[L567] [20:34.96] more concise because we don't need to
[L568] [20:37.52] write out all the types which seems
[L569] [20:39.04] nice. But what are the tradeoffs of
[L570] [20:41.56] adding type inference to a programming
[L571] [20:43.12] language?
[L572] [20:43.96] >> Well, as I said error messages can be
[L573] [20:46.80] type error messages can be very
[L574] [20:48.56] confusing
[L575] [20:49.96] because
[L576] [20:51.64] they not always point to the actual
[L577] [20:54.08] source of the type error.
[L578] [20:55.84] Okay.
[L579] [20:58.96] The system may have done some some wrong
[L580] [21:00.92] inferences and and and will report
[L581] [21:03.92] though some of those inferences instead
[L582] [21:05.84] of reporting the source the actual
[L583] [21:07.88] source of the type error. So, it's been
[L584] [21:09.84] it's been
[L585] [21:11.04] the subject of much research.
[L586] [21:13.16] And and there's there's no very
[L587] [21:16.24] well-defined idea of the the source of a
[L588] [21:18.60] type error, basically.
[L589] [21:20.72] Um so, yeah. So, errors can be an issue.
[L590] [21:24.08] Some features of type systems
[L591] [21:26.32] are easy to combine with type inference,
[L592] [21:28.20] to handle with type inference, and some
[L593] [21:29.76] are harder.
[L594] [21:31.56] Uh for instance, when it comes to
[L595] [21:32.68] genericity, so I mentioned the
[L596] [21:35.04] polymorphic parameter uh parametric
[L597] [21:36.96] polymorphism, which which is very well
[L598] [21:38.60] handled, but subtyping, the kind of
[L599] [21:42.36] uh
[L600] [21:42.92] thing you have in object-oriented
[L601] [21:44.36] languages, is actually harder to to
[L602] [21:46.76] combine with with type inference for
[L603] [21:50.48] super technical reasons that I'm not
[L604] [21:52.04] going to to go into.
[L605] [21:53.92] Um so, so sometimes uh you have to make
[L606] [21:57.00] a choice. Either you have type
[L607] [21:58.40] inference, but it is less powerful,
[L608] [22:02.00] uh or you you have uh full type
[L609] [22:05.28] inference, but more restrictive type
[L610] [22:07.24] system.
[L611] [22:08.28] Uh
[L612] [22:09.24] And and that that that that choice is
[L613] [22:11.36] part of the language design, actually.
[L614] [22:14.32] >> You mentioning this uh solver kind of
[L615] [22:17.00] reminds me of the topic of formal
[L616] [22:19.16] verification. Could you explain what
[L617] [22:21.20] formal verification is?
[L618] [22:23.32] >> Woo.
[L619] [22:25.68] Well, it's the idea that um
[L620] [22:28.08] um
[L621] [22:29.48] you for for some programs, you want you
[L622] [22:31.84] want strong guarantees that that that
[L623] [22:34.08] the program is correct. Well, and and
[L624] [22:36.08] guarantees that are hard to get just
[L625] [22:37.76] with testing and and reviews, code
[L626] [22:40.48] reviews.
[L627] [22:41.96] Uh you know, there's uh this famous
[L628] [22:43.56] quote by
[L629] [22:44.92] uh Dijkstra, the the Dutch computer
[L630] [22:47.08] pioneer,
[L631] [22:48.52] uh which is which goes something like uh
[L632] [22:51.52] testing can only show the presence of
[L633] [22:53.40] bugs, but not their complete absence.
[L634] [22:56.40] Uh because in general, there's an
[L635] [22:57.80] infinite infinitely many inputs to your
[L636] [23:00.04] program, and you cannot test them all.
[L637] [23:03.08] So, you only test in your sample and
[L638] [23:04.80] then sometimes you have surprises.
[L639] [23:07.08] So, what if you want to make sure that
[L640] [23:09.00] program is correct for an infinite
[L641] [23:10.68] number of inputs?
[L642] [23:12.28] And that's where you need to turn to
[L643] [23:14.60] those so-called formal methods. So,
[L644] [23:16.52] you're using mathematical reasoning,
[L645] [23:18.28] you're using the uh
[L646] [23:20.80] uh
[L647] [23:21.64] static analysis algorithms on your on
[L648] [23:23.68] your program to
[L649] [23:26.08] really analyze all possible executions
[L650] [23:28.76] of a piece of code and making sure that
[L651] [23:32.12] it matches a specification.
[L652] [23:35.12] The specification can be very simple
[L653] [23:36.88] like the code will never crash
[L654] [23:39.84] given well-formed inputs.
[L655] [23:41.96] So, that that's a fairly simple
[L656] [23:44.12] property, but still extremely useful
[L657] [23:46.00] because code that crashes is always code
[L658] [23:48.24] that can be attacked. It's always is
[L659] [23:50.56] often security hole.
[L660] [23:52.50] >> [sighs and gasps]
[L661] [23:52.80] >> Um
[L662] [23:54.32] so, for instance, all accesses within
[L663] [23:56.56] array
[L664] [23:58.12] all array accesses are within bounds.
[L665] [24:01.20] That's a very simple property and it's
[L666] [24:03.92] very hard to to ensure just by a type
[L667] [24:06.88] system or just by testing. So, that's
[L668] [24:09.53] [snorts] where you need some more
[L669] [24:11.04] advanced formal verification.
[L670] [24:12.88] And then there are
[L671] [24:14.16] there are much more powerful specific
[L672] [24:15.76] much more precise specifications that
[L673] [24:17.40] you may want to check that can be where
[L674] [24:19.20] the program always terminates. It can be
[L675] [24:21.04] the program
[L676] [24:22.28] doesn't [snorts] leak
[L677] [24:23.72] confidential data. It can even be where
[L678] [24:26.84] the program computes this mathematical
[L679] [24:29.28] function
[L680] [24:30.49] >> [snorts]
[L681] [24:30.52] >> uh with
[L682] [24:31.72] with an error floating point error under
[L683] [24:35.36] I don't know, 10 to the minus six. Okay.
[L684] [24:38.60] Something like that. Something very
[L685] [24:39.96] precise like that.
[L686] [24:42.72] And so, it's it's been really hot topic
[L687] [24:45.04] in in
[L688] [24:46.24] in in software sciences since the
[L689] [24:49.88] uh since the '70s, I would say. There's
[L690] [24:51.92] lots of techniques.
[L691] [24:53.60] Some are just fully automatic like
[L692] [24:56.64] static analysis, uh
[L693] [24:58.88] but they're already pretty good at
[L694] [25:00.20] finding bugs and making sure that some
[L695] [25:02.48] bugs like array out of bounds are not
[L696] [25:04.68] there.
[L697] [25:06.12] And some
[L698] [25:07.56] are a lot more interactive and and
[L699] [25:09.44] require a lot more formal assistance to
[L700] [25:11.68] write specifications and then do can so
[L701] [25:15.16] called program proofs. So proving
[L702] [25:17.24] mathematical statements about the
[L703] [25:18.72] program.
[L704] [25:19.96] >> I hear about it a lot more now which is
[L705] [25:22.44] lean and these theorem provers.
[L706] [25:24.92] Um what are those in this context and
[L707] [25:28.24] how how are they used?
[L708] [25:30.36] >> Uh so yeah so lean is is an example an
[L709] [25:34.24] instance of the so called
[L710] [25:36.96] provers or proof assistants.
[L711] [25:40.68] Um so originally those were developed to
[L712] [25:43.44] do mathematics on the computer. So not
[L713] [25:46.76] nothing with
[L714] [25:48.56] not formal verification of programs but
[L715] [25:51.16] but they can also be used for formal
[L716] [25:52.64] verification of programs. But the
[L717] [25:54.52] initial motivation was really to do
[L718] [25:56.04] mathematics with the help of the
[L719] [25:57.24] computer.
[L720] [25:59.08] Um where originally everyone focused on
[L721] [26:02.88] automatic theorem proving. So having the
[L722] [26:05.08] machine find proofs from
[L723] [26:07.92] all by itself.
[L724] [26:09.40] But that's very very difficult
[L725] [26:12.64] and not necessarily what what
[L726] [26:15.12] mathematicians need.
[L727] [26:17.72] And so those proof assistants are more
[L728] [26:20.84] like
[L729] [26:22.36] where formal language is like like
[L730] [26:24.32] programming languages but where you can
[L731] [26:26.20] write mathematic definition mathematical
[L732] [26:28.12] definitions mathematical statements
[L733] [26:31.00] and they will help you prove. So so some
[L734] [26:34.32] small proof steps they will do
[L735] [26:35.68] automatically and for others the the
[L736] [26:38.88] user still has to guide the prover
[L737] [26:41.16] through through the major steps.
[L738] [26:43.72] But the good thing is that the proof is
[L739] [26:45.00] recorded also in a format that the
[L740] [26:46.72] machine can understand and recheck.
[L741] [26:50.08] So when you complete a proof in lean or
[L742] [26:52.64] Coq, or Isabelle, or one of those tools,
[L743] [26:55.64] and and it is rechecked, and and the
[L744] [26:58.48] computer makes sure that all inferences
[L745] [27:00.88] are justified, that you didn't forget
[L746] [27:02.96] any case, that you uh you didn't use a
[L747] [27:05.96] conclusion as an hypothesis, or where
[L748] [27:08.08] all all kind of
[L749] [27:09.84] problems you can have with a pencil and
[L750] [27:11.64] paper proof.
[L751] [27:13.04] And so, in the end, you get proofs that
[L752] [27:15.04] are extremely uh
[L753] [27:16.80] reliable, extremely credible.
[L754] [27:20.08] Um and and it's been so so those tools
[L755] [27:23.40] have been used a little bit uh
[L756] [27:27.28] for well for for for some um
[L757] [27:30.32] uh some big mathematical results, where
[L758] [27:32.64] where the proofs are so big that that
[L759] [27:34.84] that they can't be done just by humans.
[L760] [27:37.16] They really need uh
[L761] [27:38.76] computer assistance.
[L762] [27:40.48] Uh
[L763] [27:41.20] I think there's a recent example with a
[L764] [27:43.40] weak uh Goldbach conjecture. Uh so, part
[L765] [27:46.64] of the proof involved checking a whole
[L766] [27:48.64] lot of inequality, maybe a thousand
[L767] [27:50.80] inequalities involving several real
[L768] [27:53.40] variables, and blah blah blah. And so,
[L769] [27:56.88] um
[L770] [27:57.80] computer assistance was really needed uh
[L771] [27:59.88] to make sure that that everything was
[L772] [28:01.72] checked, and and there was no no human
[L773] [28:04.20] mistakes uh left.
[L774] [28:07.12] And and maybe we'll talk about
[L775] [28:09.32] generative AI later, but there's there's
[L776] [28:11.60] also now a lot of interest in
[L777] [28:13.80] conjunction with generative AI.
[L778] [28:16.12] Uh AI is pretty good as that coming up
[L779] [28:18.56] with plausible proofs.
[L780] [28:20.88] Okay, but then they have to be checked
[L781] [28:22.88] by humans.
[L782] [28:25.36] Unless uh
[L783] [28:26.96] AI writes a proof in one of those formal
[L784] [28:29.04] languages like Lean, in which case it
[L785] [28:31.36] can be checked by a machine, and that's
[L786] [28:34.32] much more much more effective.
[L787] [28:37.48] Um
[L788] [28:38.80] So, yeah. So, it's it's the idea of of
[L789] [28:41.40] using the machine to help you write
[L790] [28:43.24] proofs and recheck proofs that you've
[L791] [28:45.60] written yourself, or maybe with some
[L792] [28:47.24] help from an AI.
[L793] [28:49.24] And now those tools can also be used to
[L794] [28:51.48] prove properties about programs.
[L795] [28:54.92] And so so I I spent uh
[L796] [28:58.16] many [clears throat] years uh uh
[L797] [29:00.32] proving the correctness of a compiler, C
[L798] [29:02.92] compiler,
[L799] [29:04.24] uh using one of those tools, the the
[L800] [29:06.16] Rock uh proof assistant.
[L801] [29:09.44] Um so so basically um
[L802] [29:12.80] when I'm proving about the compiler, so
[L803] [29:14.76] it takes C code, it produces assembly
[L804] [29:16.72] code, and
[L805] [29:18.04] um proving that the assembly code is
[L806] [29:19.52] faithful to the C code. So so there's no
[L807] [29:21.72] miscompilation. The the compiler didn't
[L808] [29:23.80] introduce a bug in the program that
[L809] [29:25.88] wasn't there originally.
[L810] [29:28.64] And and it's a fairly big proof because
[L811] [29:31.08] compilers do complicated things about
[L812] [29:32.72] programs, and then you have to define
[L813] [29:34.36] exactly what it means to preserve the
[L814] [29:36.32] semantics of a program. So you have to
[L815] [29:37.96] define the semantics of your programming
[L816] [29:39.64] languages. And and so so it's all a very
[L817] [29:42.68] good use of those uh uh machines
[L818] [29:46.08] uh of those proof assistants. Uh
[L819] [29:49.08] the the same work could be done on
[L820] [29:50.48] paper, but I mean this would be a proof
[L821] [29:52.76] of several thousand pages, and nobody
[L822] [29:55.28] would want to read it.
[L823] [29:57.32] Nobody would trust it. It's just too
[L824] [29:59.00] big. Uh and and it would be very hard to
[L825] [30:01.60] evolve. Um
[L826] [30:03.92] One good thing about
[L827] [30:05.76] um those um
[L828] [30:07.36] mechanized verifications of of programs
[L829] [30:09.56] is that
[L830] [30:10.44] uh
[L831] [30:11.12] it can also help you evolve the program.
[L832] [30:13.44] Okay? You can add new features and so
[L833] [30:15.24] on, and and adapt your proofs, and be
[L834] [30:17.24] really sure that you haven't introduced
[L835] [30:19.12] a regression or things like that.
[L836] [30:23.20] Um so yeah, so it's really uh
[L837] [30:24.84] programming taken to a higher level. Um
[L838] [30:28.84] And and today it's quite expensive. Um
[L839] [30:31.76] it takes a lot more time to to prove a
[L840] [30:34.16] program than to write it in the first
[L841] [30:36.16] place. But maybe this is getting a
[L842] [30:38.08] little better.
[L843] [30:39.48] Um
