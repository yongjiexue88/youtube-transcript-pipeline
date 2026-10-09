Chunk 2; segments 345–696. Start may repeat the previous chunk for context.

# Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg

Source ID: source-fd3381490fc526e5
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_TypeScript_10x_Faster_Typescript,_Why_AI_Won't_Replace_SWEs_Anders_Hejlsberg_en.txt
Video: https://www.youtube.com/watch?v=cywK3XYYJ2o

[L354] [13:52.48] There is, but it it but it comes often
[L355] [13:55.44] with a whole bunch of restrictions and
[L356] [13:57.84] and and it doesn't come necessarily with
[L357] [14:00.80] the safety guarantees that we were
[L358] [14:02.32] looking for. I mean, like Go is type
[L359] [14:04.72] safe and memory safe. uh meaning that
[L360] [14:07.36] you don't get to just like have stray
[L361] [14:10.32] pointers or or whatever where Rust you
[L362] [14:13.36] can do ref counting or you can do you
[L363] [14:15.44] can do all sorts of different strategies
[L364] [14:17.52] but there's always like that little bit
[L365] [14:20.24] of unsafe where you have to like do this
[L366] [14:22.64] in order to make it all work you know uh
[L367] [14:25.36] where where if garbage collection is
[L368] [14:28.56] engineered into the language it really
[L369] [14:30.56] is a a separate concern that is you you
[L370] [14:33.36] you don't you don't have to do anything
[L371] [14:35.92] special in I mean of course you you have
[L372] [14:39.04] to like not hold on to data that you no
[L373] [14:41.60] longer need and whatever you know but
[L374] [14:43.36] that's true of ref counting as well
[L375] [14:45.04] right but but it is inherent in in the
[L376] [14:48.32] language
[L377] [14:49.84] when you ported it from JavaScript to go
[L378] [14:52.64] I'm curious how much LLMs were used in
[L379] [14:55.68] that process because I know famously
[L380] [14:58.88] there's some major projects that have
[L381] [15:00.64] been doing uh rewrites of their entire
[L382] [15:03.20] codebase I know there's this JavaScript
[L383] [15:05.44] project called bun
[L384] [15:06.80] >> that rewrote everything from Zigg into
[L385] [15:09.44] Rust and so
[L386] [15:10.80] >> seems like a pretty useful tactic and
[L387] [15:13.20] I'm curious if you leverage that in this
[L388] [15:16.00] process.
[L389] [15:16.80] >> Not a whole lot but it also has to do
[L390] [15:18.96] with timing. Uh we started this project
[L391] [15:21.36] two years ago and two years ago LLMs
[L392] [15:23.68] were nowhere near as good as they are
[L393] [15:25.04] now. I mean that's how crazy fast it
[L394] [15:27.36] it's all moved, right? Um,
[L395] [15:31.84] so what we did though is we we certainly
[L396] [15:34.72] had
[L397] [15:36.48] a bunch of tools that aided us in the in
[L398] [15:39.12] the in the the port. I'd say the
[L399] [15:42.32] prototypes we wrote, the scanner and the
[L400] [15:43.92] parser we wrote manually. Um, and at
[L401] [15:47.60] that point we could convince ourselves,
[L402] [15:49.20] wow, we can actually get 10x out of
[L403] [15:51.04] this. Now what do we do with the rest of
[L404] [15:53.84] this codebase? And what we did was we
[L405] [15:56.80] wrote a tool that syntactically
[L406] [15:58.96] translates TypeScript into Go.
[L407] [16:03.20] This Go that comes out of it, it has no
[L408] [16:05.20] syntax errors in it, but it doesn't
[L409] [16:06.72] compile either because it's full of, you
[L410] [16:09.92] know, like it uses types as if they were
[L411] [16:12.56] TypeScript, which they're not in Go. And
[L412] [16:14.88] so all of that had to be refactored. We
[L413] [16:17.12] had to redo all the data structures or
[L414] [16:18.80] whatever, but we got the same code base
[L415] [16:21.52] out of it. And then we can sort of bang
[L416] [16:23.12] on that. and then in a more localized
[L417] [16:25.60] fashion maybe use AI occasionally to
[L418] [16:28.24] help us do the transformation. So it was
[L419] [16:30.40] sort of manual and automated
[L420] [16:34.88] and a little bit of AI. Now if we were
[L421] [16:38.32] to start the project today would we do
[L422] [16:41.04] it differently? Possibly. Um although I
[L423] [16:43.76] will say if if we just let AI loose on
[L424] [16:48.08] you know what is it like half a million
[L425] [16:49.44] lines of code that we have in the old
[L426] [16:50.80] compiler or somewhere between half a
[L427] [16:52.32] million and a million right uh and asked
[L428] [16:54.72] it to translate it all. Well I don't
[L429] [16:57.28] know that that would absolve us from
[L430] [16:58.88] then having go in and carefully
[L431] [17:00.48] examining every line that came out of it
[L432] [17:02.32] to make sure that there were no
[L433] [17:03.44] hallucinations. Right? Unless you have
[L434] [17:05.60] 100% perfect test coverage, you probably
[L435] [17:08.24] still got to go check all of that. Now I
[L436] [17:11.76] think a a a better approach quite
[L437] [17:14.00] honestly would be enlist AI to write a
[L438] [17:17.92] program that helps you translate from
[L439] [17:20.40] Typescript to Go because at that point
[L440] [17:23.28] you can park the stochasticness in that
[L441] [17:25.76] program and then you can get
[L442] [17:27.60] deterministic behavior whenever you run
[L443] [17:29.76] the program which means you get the same
[L444] [17:31.60] transformation every time you run it
[L445] [17:34.48] right that's always the thing about AI
[L446] [17:36.64] that people forget it's not
[L447] [17:37.92] deterministic right so you can't really
[L448] [17:40.00] trust that it's going to do the same
[L449] [17:41.52] thing twice.
[L450] [17:43.68] Um, [snorts]
[L451] [17:44.72] so, so we might have done it that way,
[L452] [17:47.44] but AI was not ready to do it at the
[L453] [17:49.60] time. Now, that doesn't mean that we
[L454] [17:50.88] don't use AI. I mean, like now down the
[L455] [17:53.44] line, we use AI a lot in our in our
[L456] [17:56.24] internal processes around like the the
[L457] [17:58.24] compiler as everyone does, right? Like
[L458] [18:00.40] help it to write tests and to move pull
[L459] [18:03.04] requests and what what what have you.
[L460] [18:05.36] and and whenever an issue is logged, we
[L461] [18:08.08] first thing we do is put copilot on and
[L462] [18:09.84] see if it can fix it for us, right? I
[L463] [18:11.44] mean, and so yeah,
[L464] [18:13.04] >> in that approach where you you use the
[L465] [18:15.68] LM to generate uh tooling and then you
[L466] [18:19.12] know the tooling is deterministic,
[L467] [18:21.12] >> but you'd still have to validate that
[L468] [18:23.52] thing.
[L469] [18:23.92] >> Yes. But that's that's a lot smaller
[L470] [18:25.92] surface area that you have to validate,
[L471] [18:27.76] right? And honestly, I I've seen that
[L472] [18:30.48] even with friends that are like we did
[L473] [18:32.64] some trip together and there was like
[L474] [18:34.08] some some accounting of they go, well,
[L475] [18:36.48] he paid for the hotel rooms or we paid
[L476] [18:38.16] for this and whatever and we needed to
[L477] [18:39.68] like sort it all out, right? And so, so,
[L478] [18:42.16] okay, well, here's what all the costs
[L479] [18:43.76] were and here were the pie and like have
[L480] [18:45.44] AI fix it for us, right? Or like tell
[L481] [18:47.52] who owes who what and it very
[L482] [18:50.64] authoritatively came up with the wrong
[L483] [18:52.56] answer, right? [laughter]
[L484] [18:54.96] Because it just forgot like about some
[L485] [18:57.04] of the settlements, right? And but if we
[L486] [18:59.20] had asked it to write a spreadsheet,
[L487] [19:02.16] which is really that's just a program,
[L488] [19:03.92] right? Then we would have gotten the
[L489] [19:05.36] right answer because it's very good at
[L490] [19:06.88] writing programs. So it's kind of funny
[L491] [19:09.60] how you you you don't sometimes you you
[L492] [19:12.24] don't ask AI for the for the answer. You
[L493] [19:14.64] ask it for a program that computes the
[L494] [19:16.48] answer.
[L495] [19:17.84] >> What are the potential benefits that you
[L496] [19:20.00] left on the table by doing a port
[L497] [19:21.84] instead of a full rewrite?
[L498] [19:23.52] >> To be honest, I don't think there are
[L499] [19:25.20] any. Um, and I don't think we would
[L500] [19:27.52] consider uh a rewrite. We were quite
[L501] [19:29.76] happy we're quite happy with the way
[L502] [19:31.52] this codebase works. Uh, and we're and
[L503] [19:34.00] we certainly I don't think we're leaving
[L504] [19:36.56] any any money on the on the table
[L505] [19:38.64] currently. Um, and and as I said
[L506] [19:41.28] earlier, rewrites are toxic often for
[L507] [19:44.40] ecosystems because they sacrifice
[L508] [19:47.68] compatibility because you never rewrite
[L509] [19:50.32] and you get you never get back to
[L510] [19:52.08] exactly what you had before, right? Oh,
[L511] [19:54.24] but oh, but in the name of making it
[L512] [19:56.16] better or prettier or whatever, we
[L513] [19:57.84] change this and that and this and that
[L514] [19:59.20] and the other, right? And then well, all
[L515] [20:01.44] the users get to suffer through that,
[L516] [20:03.12] right? So, so backwards compatibility is
[L517] [20:05.92] super important if you want to keep your
[L518] [20:08.08] ecosystem happy. Uh, and and and we we
[L519] [20:10.64] do want that. [laughter]
[L520] [20:12.72] In studying for this interview, I I just
[L521] [20:15.20] keep reading about JavaScript and the
[L522] [20:17.68] the strange semantics of the language.
[L523] [20:20.24] And I think throughout my career too,
[L524] [20:22.24] people have typically
[L525] [20:24.56] not been super satisfied or happy with
[L526] [20:27.44] JavaScript for some reason or the other,
[L527] [20:29.84] >> right?
[L528] [20:30.72] >> And my question is why is it so popular
[L529] [20:34.64] despite that?
[L530] [20:36.24] >> So first of all, I I don't think
[L531] [20:38.24] JavaScript is as bad of a lang of a
[L532] [20:40.56] language as as some people make it out
[L533] [20:42.32] to be. I I I will say in in like the
[L534] [20:44.64] three about three four weeks that
[L535] [20:46.32] Brendan Ike had to create this language
[L536] [20:48.32] back in the mid 90s, he did a lot of
[L537] [20:51.12] things right. Um and thank God that he
[L538] [20:54.24] had been educated on functional
[L539] [20:55.92] programming and and got first class
[L540] [20:58.16] functions done right where you can have
[L541] [21:00.00] functions within functions and the inner
[L542] [21:02.32] functions can access the outer function
[L543] [21:04.16] state and you can pass functions around
[L544] [21:07.04] as first class values.
[L545] [21:10.00] that is super powerful and JavaScript
[L546] [21:12.16] actually got that very right. Um, now
[L547] [21:15.92] there's some quirks in the language too,
[L548] [21:18.08] like all of the automatic conversions
[L549] [21:20.64] and all of the bizarre differences
[L550] [21:22.32] between double equals and triple equals
[L551] [21:24.40] are just like drives everyone mad,
[L552] [21:27.04] right? But that's exactly what type
[L553] [21:28.88] checkers are happy to do. They can like
[L554] [21:30.48] they can far it out all the little
[L555] [21:32.32] differences because they understand the
[L556] [21:34.56] all the deep semantics of the language
[L557] [21:36.40] that no one seems to be able to keep in
[L558] [21:38.40] their mind, right? So, and I think
[L559] [21:40.88] that's part of why Typescript has become
[L560] [21:42.72] so popular, right? It's like it can
[L561] [21:44.48] actually like truly bring out the best
[L562] [21:46.80] parts of JavaScript uh and leave the bad
[L563] [21:49.28] stuff behind. And of course, you can't
[L564] [21:52.88] like like the thing about JavaScript is
[L565] [21:55.52] it is the crossplatform language. Like
[L566] [21:58.32] even Java that was engineered and
[L567] [22:00.64] intended to be the way to write
[L568] [22:02.40] crossplatform applications, it's not
[L569] [22:04.80] really crossplatform. It doesn't run in
[L570] [22:07.36] the browser, you I mean it doesn't it
[L571] [22:09.20] doesn't run everywhere, right?
[L572] [22:10.32] JavaScript runs everywhere. Um, so there
[L573] [22:15.20] are a lot of there are a lot of reasons
[L574] [22:16.80] why you should like JavaScript and and
[L575] [22:20.16] with TypeScript, I think we've managed
[L576] [22:22.00] to sort of capture all the badness and
[L577] [22:25.76] park it.
[L578] [22:27.76] I saw there were some projects. I don't
[L579] [22:29.84] know if you're familiar with Dart or
[L580] [22:32.72] CoffeeScript and
[L581] [22:34.64] >> it seems like these were some effort to
[L582] [22:37.68] replace JavaScript or improve it and
[L583] [22:40.96] >> right
[L584] [22:41.44] >> but they're not popular today. So I'm
[L585] [22:43.36] curious what happened.
[L586] [22:44.72] >> I mean I think coffecript was mostly
[L587] [22:49.28] it's a different syntax for JavaScript.
[L588] [22:51.60] So, so it doesn't really change the the
[L589] [22:53.68] semantics and it doesn't it didn't
[L590] [22:55.52] provide any additional tooling and and
[L591] [22:57.68] whatever. And and Dart was also in a
[L592] [23:00.08] sense about fixing JavaScript, right?
[L593] [23:03.12] But if you can fix something by fixing
[L594] [23:06.88] it instead of trying to replace it with
[L595] [23:09.92] something else, then you're doing the
[L596] [23:13.84] ecosystem a much bigger favor, I think.
[L597] [23:16.56] Right. And that's what we set out to do
[L598] [23:18.32] with TypeScript. We weren't trying to
[L599] [23:19.84] change JavaScript. we were trying to
[L600] [23:21.60] improve JavaScript. Um, and I think
[L601] [23:24.80] that's ultimately why we why we
[L602] [23:26.80] succeeded.
[L603] [23:28.24] >> I mean, in this new age where it's very
[L604] [23:31.92] feasible that maybe AI could rewrite
[L605] [23:34.24] code bases,
[L606] [23:36.08] um, I imagine people will start to go
[L607] [23:39.36] towards the the desired languages rather
[L608] [23:42.40] than the ones that are the incumbent
[L609] [23:43.84] languages.
[L610] [23:45.44] And I'm curious if you think that
[L611] [23:47.36] JavaScript might become less used in the
[L612] [23:49.84] future.
[L613] [23:51.52] >> See, I I don't think so. I I what I've
[L614] [23:54.16] observed is that AI
[L615] [23:58.40] is best at the languages if seen the
[L616] [24:01.68] most of in its training set, right? And
[L617] [24:04.48] AI gets trained on all the code that
[L618] [24:06.40] exists in the world. Um,
[L619] [24:09.68] which means there's an awful lot of
[L620] [24:11.28] JavaScript, an awful lot of TypeScript,
[L621] [24:12.96] an awful lot of Python. And therefore,
[L622] [24:15.20] AI is good at JavaScript and TypeScript
[L623] [24:17.36] and Python. And it is less good at my
[L624] [24:20.72] favorite little language that I just
[L625] [24:22.32] invented. In fact, there's none of it in
[L626] [24:23.92] the training set, which means you have
[L627] [24:25.52] to sacrifice God knows how many tokens
[L628] [24:27.60] in the prompt to teach AI the language
[L629] [24:31.84] before you can even ask it a question
[L630] [24:33.52] about the language. Do you know what I
[L631] [24:35.20] mean? So in that sense I think incumbent
[L632] [24:38.96] languages are actually if anything going
[L633] [24:41.20] to flourish uh because of AI and we're
[L634] [24:44.00] sort of seeing that right now with with
[L635] [24:45.76] TypeScript too right there there's a
[L636] [24:47.84] noticeable knee in the curve of
[L637] [24:49.52] TypeScript adoption that coincides with
[L638] [24:52.88] the advent of AI. I do think the
[L639] [24:55.52] incumbent languages are actually if
[L640] [24:57.52] anything getting stronger.
[L641] [24:59.12] >> What percent of all JavaScript is
[L642] [25:02.24] written in Typescript?
[L643] [25:04.80] Well, so, so in the last year,
[L644] [25:08.08] Typescript uh became the number one used
[L645] [25:11.92] language on GitHub. Um, so there's
[L646] [25:14.96] JavaScript more than JavaScript.
[L647] [25:16.72] >> So, so more than 50% on GitHub at least
[L648] [25:20.56] >> is is is written in in Typescript. Um,
[L649] [25:23.68] so so we're actually like larger now
[L650] [25:25.84] than the language that we set out to
[L651] [25:27.68] improve.
[L652] [25:28.96] >> Wow.
[L653] [25:29.52] >> Yeah. And larger than Python. If you
[L654] [25:32.00] were to just draw that out in the
[L655] [25:33.28] future, do you think that eventually
[L656] [25:35.76] TypeScript would become the default and
[L657] [25:37.92] almost 100% of all JavaScript would be
[L658] [25:40.40] typed?
[L659] [25:41.60] >> Well, certainly, I mean, if you're
[L660] [25:43.36] having AI write it, I I almost challenge
[L661] [25:46.56] you to find a tool that writes
[L662] [25:48.16] JavaScript. They all write TypeScript.
[L663] [25:50.40] Uh because it helps AI write better code
[L664] [25:53.92] because the type annotations guide the
[L665] [25:56.64] LLM towards writing or to write making
[L666] [25:59.84] fewer mistakes. and the ability for us
[L667] [26:02.80] to statically validate the code before
[L668] [26:06.16] you run it. I mean, that's the
[L669] [26:08.24] distinction, right? The only way you can
[L670] [26:09.76] validate JavaScript is by running it,
[L671] [26:12.88] which means you have to set up a runtime
[L672] [26:14.48] environment, which might not be possible
[L673] [26:16.24] for AI to do because AI lives in a
[L674] [26:18.72] sandbox, right? But AI can run through
[L675] [26:21.68] tools, the compiler, and check the code
[L676] [26:24.72] that it just generated and be told, "Oh,
[L677] [26:26.64] you made a mistake. Oh, well, let me fix
[L678] [26:28.24] it then before I even tell anyone that I
[L679] [26:30.08] made the mistake, right? [laughter]
[L680] [26:32.32] [snorts]
[L681] [26:32.96] >> After learning about the this 10x
[L682] [26:35.12] improvement in performance from uh
[L683] [26:37.68] rewriting in native, I makes me wonder
[L684] [26:40.96] why anyone would use JavaScript on the
[L685] [26:44.00] back end. Why not just always use native
[L686] [26:47.28] languages on the back end?
[L687] [26:48.48] >> Well, it depends on your problem. Uh I
[L688] [26:51.20] think because the thing that that
[L689] [26:52.96] overlooks is
[L690] [26:55.36] what kind of thing am I going to write
[L691] [26:56.72] on the back end, you know, like like
[L692] [26:58.40] there are an awful lot of very very good
[L693] [27:02.00] web server frameworks for example that
[L694] [27:04.72] that use TypeScript or JavaScript,
[L695] [27:07.12] right? So, so if there are like
[L696] [27:10.00] frameworks in your ecosystem that gets
[L697] [27:11.84] you to a solution quicker than if you
[L698] [27:14.64] had to write that because your native
[L699] [27:16.72] language wasn't really intended to
[L700] [27:18.96] target that particular community. So, I
[L701] [27:22.32] think it very much depends on
[L702] [27:25.44] your what what your problem is
[L703] [27:27.28] affinitized with. Um, and and often PF
[L704] [27:31.60] of your code isn't the bottleneck. I
[L705] [27:34.40] mean, like look at Python. I mean right
