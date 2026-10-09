Chunk 2; segments 357–705. Start may repeat the previous chunk for context.

# Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura

Source ID: source-70f1e2ca6c128ddc
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lean_Handwritten_Math_Will_Change_Dramatically_Leonardo_de_Moura_en.txt
Video: https://www.youtube.com/watch?v=KzdYKeAqWhY

[L366] [15:34.24] to get all the intellisense
[L367] [15:36.80] one big difference is that we have
[L368] [15:38.48] something called the info view in ling
[L369] [15:41.36] your screens usually is going to be
[L370] [15:42.88] split in two you have your your file on
[L371] [15:47.20] the right hand side you have the info
[L372] [15:49.04] view that tells you information about
[L373] [15:50.72] your proofs, about your codes, uh is
[L374] [15:56.16] giving you constant feedback about your
[L375] [15:59.20] developments. That's basically the main
[L376] [16:01.60] difference, but the tooling, VS code,
[L377] [16:04.88] everything works the same way. I mean,
[L378] [16:07.28] >> it seems like a programming language is
[L379] [16:09.04] the the fundamental layer and then
[L380] [16:11.12] there's some additional layer on top
[L381] [16:12.88] that keeps
[L382] [16:13.92] >> track. Good question. uh uh in L you
[L383] [16:18.00] have definitions that are your program
[L384] [16:19.52] but you have theorems statements like
[L385] [16:22.88] you're going to say for example uh
[L386] [16:24.56] factorial is always greater than or
[L387] [16:27.04] equal to zero or something like that or
[L388] [16:30.08] if you add two even numbers you get even
[L389] [16:33.04] number you can write statements like
[L390] [16:35.36] that and immediately you can write
[L391] [16:39.52] actually a program that's the proof
[L392] [16:42.64] but most people don't do that they go
[L393] [16:44.80] into something called tactic modes. You
[L394] [16:47.84] can view as a domain specific language
[L395] [16:49.68] for writing proofs in ling. When you
[L396] [16:52.32] write by it switches to this domain
[L397] [16:54.80] specific language and you can you have
[L398] [16:57.92] steps like simplify my goal
[L399] [17:01.68] the state of my proof. You can say oh
[L400] [17:04.72] apply this writing step apply for
[L401] [17:07.84] example we know that x plus 0= x. You
[L402] [17:10.32] can ask ling apply this writing and
[L403] [17:13.04] you're going to see in the info view the
[L404] [17:15.12] state of the proof changing you you get
[L405] [17:18.32] immediate feedback and you get this
[L406] [17:20.72] feeling that you said you you keep
[L407] [17:23.52] telling applying transformations to your
[L408] [17:26.32] proof step by step you can see what's
[L409] [17:28.56] happening until you get no goals left
[L410] [17:32.16] and you are done the proof's complete
[L411] [17:34.48] and some people view this process as a
[L412] [17:37.12] game I I have users that told You built
[L413] [17:40.96] my favorite computer again for me.
[L414] [17:43.08] [laughter]
[L415] [17:45.04] >> That's funny. Is lean itself verified in
[L416] [17:49.04] lean?
[L417] [17:49.92] >> Lean is a massive program. You only have
[L418] [17:52.08] to trust the kernel. The kernel is where
[L419] [17:54.08] the proofs are checked. Lean itself is
[L420] [17:57.68] the kind of program that because there
[L421] [18:00.00] are so many new things we are adding.
[L422] [18:02.16] It's not even clear what is the
[L423] [18:03.76] specification. For example, what is the
[L424] [18:07.04] specification of a simplifier? You you
[L425] [18:09.44] can write general ideas but users they
[L426] [18:12.80] want to be able to customize the
[L427] [18:14.64] behavior. They keep asking they keep
[L428] [18:16.72] changing the specification all the time.
[L429] [18:18.96] I want this, I want that. No add this
[L430] [18:22.32] knob here. So it's really hard to have a
[L431] [18:25.60] full specification of L. But the kernel
[L432] [18:27.92] is possible to have a specification. We
[L433] [18:30.48] have a kernel. The kernel that comes
[L434] [18:32.64] with ling is not verified. But there are
[L435] [18:35.84] other kernels that you can use. One of
[L436] [18:38.88] them is implemented by Mario Kanedo.
[L437] [18:41.60] It's called Ling for Ling and it's
[L438] [18:44.00] implemented in ling and he's very fine
[L439] [18:46.08] is proving that this this kernel has
[L440] [18:48.32] been verified with respect to the
[L441] [18:50.96] semantics of ling. This is a cool
[L442] [18:53.44] project but for us having multiple
[L443] [18:57.44] kernels is the best way to ensure that
[L444] [19:00.40] your results are correct. I mean uh some
[L445] [19:03.12] users implemented their own kernels. We
[L446] [19:05.44] have kernels implemented in rust uh in
[L447] [19:08.40] different programming languages. Uh
[L448] [19:10.88] >> and when you say kernel what's what's
[L449] [19:12.96] the responsibility or what's the inputs
[L450] [19:15.20] and outputs of that portion?
[L451] [19:16.72] >> Yes. And l proof checking is type
[L452] [19:20.00] checking. This kernels they are type
[L453] [19:22.56] checking your programs. I mean basically
[L454] [19:25.52] you can export your lan developments.
[L455] [19:28.72] You got a big blob and you read this
[L456] [19:31.68] blob and they're going to check if
[L457] [19:35.52] when you say we have a proofing link
[L458] [19:37.28] basically you have a thumb that has a
[L459] [19:39.28] type and you're checking if the type of
[L460] [19:41.76] this T matches the type that you claim
[L461] [19:45.60] it has. For example, the example of the
[L462] [19:47.76] even numbers. This is a typing link
[L463] [19:50.40] saying that's uh uh the sum of two even
[L464] [19:53.36] numbers is a even number.
[L465] [19:56.56] You can write you can view that it is
[L466] [19:58.48] exactly a typing link and the proof what
[L467] [20:01.84] the kernel is checking is whether the
[L468] [20:03.76] type of the proof matches the type you
[L469] [20:06.40] claim this thumb has I mean and the the
[L470] [20:09.68] console will check you do this type
[L471] [20:11.44] checking
[L472] [20:13.36] uh the kernels vary between
[L473] [20:18.40] high performance kernel should it's like
[L474] [20:20.72] 5,000 lines of code I mean the goal of
[L475] [20:23.12] the should be something you can write
[L476] [20:26.00] yourself.
[L477] [20:27.60] Uh of course sometimes people put bells
[L478] [20:30.00] and whistles like uh one thing concern
[L479] [20:34.72] people have is like okay
[L480] [20:37.76] but how do I know that I wrote fas
[L481] [20:41.84] in ling how do you know that when you
[L482] [20:45.20] exported it's really theorem it's not 2
[L483] [20:48.64] plus 2 equals four I mean uh and people
[L484] [20:52.40] some external kernels they write print
[L485] [20:55.04] printers I mean they will print the
[L486] [20:57.44] statements that has been proven all the
[L487] [20:59.60] dependencies
[L488] [21:01.12] you can have all the these fancy tools
[L489] [21:03.60] to make sure you're not being misled.
[L490] [21:07.04] >> Lean obviously it's so powerful and I
[L491] [21:10.24] see on social media all these amazing
[L492] [21:13.44] results from formal verification want to
[L493] [21:16.32] know you what are the top ones that you
[L494] [21:18.48] think of or top examples more recently
[L495] [21:21.44] that have impressed you that lean was
[L496] [21:23.84] able to accomplish? Well, there are so
[L497] [21:26.64] many I mean that I thought were was
[L498] [21:28.80] impossible for for example getting a
[L499] [21:30.72] gold medal in the international
[L500] [21:32.56] mathematical olympiad.
[L501] [21:35.04] A few years ago everybody thought was
[L502] [21:37.04] impossible. Now everybody they use it as
[L503] [21:40.40] a benchmark of a easy problem. They say
[L504] [21:42.72] oh this is like a IMO problem. I mean
[L505] [21:45.28] this is easy but it's not. I mean these
[L506] [21:48.16] are really challenging problems. Uh the
[L507] [21:51.28] other conjectures that people close
[L508] [21:54.00] using ling AI with ling also impresses
[L509] [21:58.48] me. Uh there's this unit distance
[L510] [22:02.32] conjecture for others. First open AI
[L511] [22:05.60] prove it using formal right was not
[L512] [22:10.08] formal and we have a system now in ling
[L513] [22:14.16] is a website where we call ling where we
[L514] [22:16.96] collect challenges.
[L515] [22:18.96] uh the same Kim Morrison saw this this
[L516] [22:21.68] this this
[L517] [22:23.68] proof open AI and she puts on Lo as a
[L518] [22:28.00] challenge say okay I want to see someone
[L519] [22:30.40] formalizing we knew it was huge to
[L520] [22:33.20] formalize
[L521] [22:34.88] it's serious math it depends on
[L522] [22:38.48] and Boris Alexi from openi he did his
[L523] [22:42.16] swim it's a one million line proof for
[L524] [22:44.80] for for whole proofing link for this
[L525] [22:46.96] conjecture uh We estimate I mean the the
[L526] [22:50.32] the ground math that is needed for the
[L527] [22:53.20] proof we knew it take months I mean for
[L528] [22:56.48] experts to do by hands. I mean
[L529] [22:59.36] >> uh how long did it take in that case
[L530] [23:01.20] like the time from when the proof came
[L531] [23:03.92] out to when the challenge was solved on
[L532] [23:05.84] the lean?
[L533] [23:06.72] >> I think what was one month?
[L534] [23:08.72] >> Yeah. And after Kim was a few I think
[L535] [23:12.56] less than two weeks after Kim puts as a
[L536] [23:15.84] challenge only vow I took I think two
[L537] [23:18.16] weeks to get the the or or less I mean
[L538] [23:21.36] >> that's that's insane.
[L539] [23:22.80] >> Yes. Yeah. Yeah.
[L540] [23:24.32] >> We talked about verifying programs but
[L541] [23:26.56] also there's using it just directly for
[L542] [23:29.12] mathematics like in this case.
[L543] [23:31.84] How popular is lean in in terms of um
[L544] [23:35.52] when you look at the users of lean? What
[L545] [23:38.08] percent are using it for software
[L546] [23:40.64] engineering? What percent are using it
[L547] [23:42.08] more for just direct math? Well,
[L548] [23:45.04] historically lean be got popular first
[L549] [23:48.24] with math, right? I mean know with the
[L550] [23:52.00] beginning of the le mathematical library
[L551] [23:54.24] in 2017
[L552] [23:56.56] we we had like a big project called
[L553] [23:59.04] liquid stencil experiments.
[L554] [24:01.76] Uh it started beginning of 2020. It was
[L555] [24:06.24] a big deal because it was to verify a
[L556] [24:09.28] result from a fields medalist. Per shows
[L557] [24:11.76] it is a result he was unsure about. He
[L558] [24:14.40] has not published it. uh uh he felt like
[L559] [24:18.32] this was one of the most important
[L560] [24:20.00] results in his career. He wanted to be
[L561] [24:22.96] sure it was correct. It was done
[L562] [24:25.44] manually. The verification
[L563] [24:28.16] uh was a big deal because the team that
[L564] [24:30.88] formalizes led by Yuan Kling
[L565] [24:34.32] they not only formalized the results
[L566] [24:37.12] without fully understanding they do not
[L567] [24:39.20] fully understand the the proof.
[L568] [24:42.08] uh but having this info view helped them
[L569] [24:44.64] guides them step by step
[L570] [24:47.60] they formalized and simplify the proof
[L571] [24:50.24] without fully understanding the proof is
[L572] [24:53.20] mindboggling right I mean how can you
[L573] [24:55.44] simplify a proof from one of the
[L574] [24:58.40] greatest living mathematicians without
[L575] [25:00.80] fully understanding it I mean but you
[L576] [25:02.80] you they manage to simplify it's almost
[L577] [25:05.76] like when people do factoring coding you
[L578] [25:07.76] start changing the codes
[L579] [25:10.24] is faster now But the program doesn't
[L580] [25:13.12] really know why. I mean, it felt like
[L581] [25:15.52] that. It's like you have a gut feeling.
[L582] [25:18.24] I mean, that's you're going the right
[L583] [25:19.84] direction.
[L584] [25:21.84] And this for us at the time, lots of
[L585] [25:24.80] people got excited about link the math
[L586] [25:26.80] community because of this project. it
[L587] [25:29.44] like it's shown that's not about
[L588] [25:31.84] verifying but enabling people to work
[L589] [25:34.16] together in large numbers because you
[L590] [25:36.96] can trust you don't need to trust
[L591] [25:39.28] someone else's proof right they can fill
[L592] [25:42.00] holes for you
[L593] [25:44.24] uh this was
[L594] [25:47.28] I mean what attracts a lots of attention
[L595] [25:49.28] from the math community then came Terren
[L596] [25:51.28] St. He starts using after this project.
[L597] [25:54.96] He has really cool projects with and
[L598] [25:57.92] without AI and he got addicted actually.
[L599] [26:01.92] I think the first time he used it said I
[L600] [26:04.32] don't think I'm going to do it again.
[L601] [26:06.48] The for proof one week later he had
[L602] [26:08.80] another project using ling and he did a
[L603] [26:12.00] new result he had. [laughter]
[L604] [26:13.44] >> When you say addicted you mean because
[L605] [26:15.04] that game that like completion engine.
[L606] [26:17.28] >> Yeah. Some people I I feel we feel like
[L607] [26:20.96] when I talk to professors that use link
[L608] [26:23.68] for teaching
[L609] [26:25.92] they tell me the class is more or less
[L610] [26:27.84] split. Some people love it, some people
[L611] [26:30.24] don't like. But people that like to
[L612] [26:33.76] problem solving, people that get medals
[L613] [26:36.40] in the IMO, they love because you get
[L614] [26:38.88] this excitement of solving. It's like a
[L615] [26:42.16] solving millions of really hard pseudoc
[L616] [26:44.88] problems, right? [laughter] And you can
[L617] [26:47.20] keep solving one and it's easy to get. I
[L618] [26:50.08] mean I'm a lean developer not a lean
[L619] [26:52.40] user but when you're developing ling I'm
[L620] [26:54.64] coding in ling and sometimes I have
[L621] [26:56.88] prove things is really easy to get
[L622] [26:59.76] addicted it gets lost proving things you
[L623] [27:03.28] get this bus every time you prove
[L624] [27:05.52] something [laughter]
[L625] [27:07.92] >> you mentioned the II gold medals how is
[L626] [27:11.20] lean used in that kind of uh I think
[L627] [27:14.08] maybe referring to alpha proof by deep
[L628] [27:16.48] mind or maybe something else
[L629] [27:18.08] >> yes deep mind because they got in 2024
[L630] [27:21.68] was a big surprise in 2024 they got a
[L631] [27:24.56] silver medal and now we have gold medals
[L632] [27:28.80] from startups like a harmonic by dance
[L633] [27:32.48] got a medal I never imagined by dance
[L634] [27:36.64] they they they're behind tick tock right
[L635] [27:40.40] I didn't even know they care about form
[L636] [27:42.40] math but they have a for math team they
[L637] [27:45.20] got medals also the approver is really
[L638] [27:47.60] good
[L639] [27:48.24] >> so how's it work let's say I mean
[L640] [27:49.76] there's a series of math problems lean
[L641] [27:52.80] is just used for verification right so I
[L642] [27:56.00] imagine there's other components there
[L643] [27:58.08] >> yeah there's the AI you can view it's
[L644] [28:00.80] like uh we have go that was very popular
[L645] [28:03.68] with AI the AI is playing the game I
[L646] [28:07.44] told you that many people see lens again
[L647] [28:11.12] it's the same I mean the AI is viewing
[L648] [28:13.12] lens again they have the statements of
[L649] [28:15.28] what you want to prove you have the buy
[L650] [28:18.16] keyword words. Now you have a blank
[L651] [28:21.04] fill. Make sure that you have no goals
[L652] [28:23.44] left, right? It keeps applying steps in
[L653] [28:26.08] this game and seeing the trans the state
[L654] [28:28.96] of the boards, right? That's the info
[L655] [28:31.04] view changing
[L656] [28:33.20] and the AI they use reinforcement
[L657] [28:35.36] learning for for for trying to get to to
[L658] [28:39.28] no goals left. They it's a single player
[L659] [28:42.48] game. Some people play together these
[L660] [28:45.36] days but yeah the AI is learning to play
[L661] [28:48.32] the game.
[L662] [28:49.28] >> So before we were talking about that
[L663] [28:51.36] game it kind of starts with the
[L664] [28:53.28] specification. So in that case then the
[L665] [28:56.56] problem is kind of the specification and
[L666] [28:59.20] then it
[L667] [29:00.40] >> the problem yeah you have basically for
[L668] [29:01.92] each problem in the international
[L669] [29:03.28] mathematical olympiad someone translates
[L670] [29:05.92] to ling the statements. It's super
[L671] [29:08.56] important to have the mathematical
[L672] [29:10.00] library because you want to be able to
[L673] [29:11.92] talk about the problems, right? For
[L674] [29:13.84] example, the problems uses the real
[L675] [29:16.16] numbers. You need a definition in ling
[L676] [29:18.64] and we have it inside of math lib the
[L677] [29:20.72] ling mathematical library. So the first
[L678] [29:23.20] thing you have to be you have to be able
[L679] [29:25.28] to write the problems in lane and this
[L680] [29:29.04] now because of math li it's easy part uh
[L681] [29:33.68] and after that you have to provide the
[L682] [29:35.12] proofs I mean sometimes some problems
[L683] [29:37.92] you have to come up with a definition to
[L684] [29:40.40] some objects you have to to create that
[L685] [29:43.12] has some property but yeah that's how it
[L686] [29:46.72] is. I remember you said one of the first
[L687] [29:50.08] use cases of lean was um this fields
[L688] [29:53.44] medalist had this novel mathematics and
[L689] [29:56.96] then we use lean to verify it but can
[L690] [30:01.28] lean be used with LMS to generate novel
[L691] [30:04.96] mathematics or just verify existing is a
[L692] [30:08.80] good question I mean we don't see lots
[L693] [30:11.84] of evidence we see now evidence it can
[L694] [30:15.52] find novel proofs
[L695] [30:17.60] Right? But coming up with new
[L696] [30:21.04] mathematical concepts is still
[L697] [30:24.32] at the limits. Right? I mean right now
[L698] [30:28.00] in this line of all we have challenges
[L699] [30:29.92] where the AI has to come up with the
[L700] [30:31.84] objects
[L701] [30:33.44] uh themselves right I mean but this is
[L702] [30:36.64] people will keep investing in this area.
[L703] [30:39.12] I I do not batch against AI here. I
[L704] [30:42.64] mean, but we we right now we don't have
[L705] [30:44.96] evidence they can come up with new math.
[L706] [30:47.84] >> Open AAI, Enthropic, Cursor, and
[L707] [30:50.80] Verscell all use this product to make
[L708] [30:52.96] their lives better. And the problem it
[L709] [30:55.20] solves is when you're building SAS or an
[L710] [30:57.44] AI product and you want to sell to other
[L711] [30:59.76] companies, there's all these
[L712] [31:01.28] requirements you need to meet. There's
[L713] [31:03.20] SSO, there's SKIM, there's arbback,
[L714] [31:06.48] there's audit logs. These are all things
