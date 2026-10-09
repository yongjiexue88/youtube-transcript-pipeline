Chunk 2; segments 338–683. Start may repeat the previous chunk for context.

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L347] [16:53.92] it doesn't matter how good C++ is, the
[L348] [16:57.92] computers of today can't do it.
[L349] [17:02.40] >> That back then though, but now now they
[L350] [17:05.44] probably could, but of course the
[L351] [17:07.92] computer traffic has become uh much
[L352] [17:10.72] more. So maybe they can't. I don't know.
[L353] [17:13.52] I don't have the numbers now. Then I
[L354] [17:16.08] they gave me the numbers. That was why I
[L355] [17:19.28] I declined to to to help them because it
[L356] [17:23.28] was impossible.
[L357] [17:24.80] >> I saw somewhere when I was doing
[L358] [17:26.72] research that you you said you had
[L359] [17:28.88] gotten lunch with Dennis Richie once a
[L360] [17:32.08] week for like 16 years or something like
[L361] [17:34.16] that.
[L362] [17:35.20] >> Um and you know he's uh also a very
[L363] [17:38.24] legendary name. And I was curious, you
[L364] [17:40.56] know, if there's anything that you you
[L365] [17:43.12] learned from him or anything that
[L366] [17:44.56] impressed you about him that maybe
[L367] [17:46.80] influenced you or C++.
[L368] [17:49.36] >> He was a great guy and we talked about a
[L369] [17:51.44] lot of things. He never said anything uh
[L370] [17:55.52] rude or or negative about um C++.
[L371] [17:59.60] Actually, in his Hubble paper, he points
[L372] [18:01.92] to C++ as the obvious successor to C.
[L373] [18:07.12] Um, so all of these
[L374] [18:10.72] C versus C++ language wars are
[L375] [18:13.84] ridiculous.
[L376] [18:15.36] Um, they should never have happened and
[L377] [18:18.16] they certainly didn't happen uh because
[L378] [18:21.76] well I I knew Dennis. We we were not
[L379] [18:24.96] fighting. Um I still know Brian Kernan.
[L380] [18:28.80] I was talking to him this Friday. Um
[L381] [18:33.84] we're good friends and uh yeah language
[L382] [18:37.76] walls are are silly. Um Dennis helped me
[L383] [18:42.32] uh design const for instance for uh C++.
[L384] [18:46.80] It used to be called read only and write
[L385] [18:48.96] only but uh the C guys couldn't handle
[L386] [18:52.00] two words and they were too long. Um so
[L387] [18:56.32] we we got what we got but that's one
[L388] [18:59.36] specific thing I remember. Dennis uh
[L389] [19:03.20] being helpful with uh he was a bit
[L390] [19:06.08] worried that about
[L391] [19:09.60] overloading because you had to look at
[L392] [19:12.56] the
[L393] [19:14.88] de declarations of functions uh before
[L394] [19:18.32] you knew what the meaning of a call was.
[L395] [19:21.28] Um but that's a very eable way of
[L396] [19:24.88] thinking. It's just happens that it it
[L397] [19:28.24] works and anybody who writes C today are
[L398] [19:33.52] using my handiwork essentially all of
[L399] [19:36.48] the time because the the modern syntax
[L400] [19:40.72] for function definitions and function
[L401] [19:43.20] declarations
[L402] [19:44.72] and the call semantics uh came out of
[L403] [19:48.40] the early um C++ early classes work of
[L404] [19:53.60] mine. So when when people start ranting
[L405] [19:57.20] um they they they should remember that
[L406] [19:59.68] they're actually doing my using my
[L407] [20:01.52] handiwork every day. [laughter]
[L408] [20:04.80] >> You had written these uh uh almost like
[L409] [20:08.16] historical accountings of the history of
[L410] [20:10.16] C++ like maybe three really long papers
[L411] [20:13.92] um I think for some conference I forgot
[L412] [20:16.08] the exact and so in there there was one
[L413] [20:19.60] anecdote about Dennis Richie. It was it
[L414] [20:22.88] was about this this concept where he
[L415] [20:25.44] proposed uh to the C standard committee
[L416] [20:28.08] this idea of a fat pointer where it uh
[L417] [20:31.76] you know also has it it stores its size
[L418] [20:34.40] as well and you mentioned the C
[L419] [20:37.12] committee didn't approve and I was
[L420] [20:38.40] curious if you could like tell that
[L421] [20:40.80] >> um
[L422] [20:42.64] so Dennis did see but he didn't take
[L423] [20:46.64] part in the standards committee and I've
[L424] [20:49.20] even heard people from the C standards
[L425] [20:51.52] committees He says, "No, Dennis isn't a
[L426] [20:53.84] C expert. He's not ever come to
[L427] [20:56.48] meetings."
[L428] [20:58.48] Um, very strange attitude, but anyway,
[L429] [21:03.12] um, we knew the problem about um about
[L430] [21:08.88] buffer overflow and range errors. And
[L431] [21:11.20] the obvious solution is to use what
[L432] [21:14.72] Dennis called a fat pointer which is a
[L433] [21:17.52] pointer with its number of elements it
[L434] [21:21.84] points to attached to it. But that's two
[L435] [21:25.20] words and uh that's probably no that is
[L436] [21:29.44] why it wasn't used on the early se uh
[L437] [21:32.96] because then they had 48k of memory and
[L438] [21:37.60] when when I had this discussion with
[L439] [21:39.44] Dennis I think we had a whole megabyte
[L440] [21:42.72] um and when I started with C++ we had
[L441] [21:46.32] 256
[L442] [21:47.84] kilobytes and I knew that uh we we were
[L443] [21:52.48] going to get um get a megabyte and and
[L444] [21:56.72] we were talking about it and he he
[L445] [21:58.40] called them fat pointers and today in
[L446] [22:01.84] C++ they're called span and um the span
[L447] [22:06.24] came out of uh my work with others on
[L448] [22:09.76] the C++ core guidelines and we needed
[L449] [22:13.68] something like that we couldn't provide
[L450] [22:16.40] the degree of control and safety that uh
[L451] [22:19.60] we needed so we built span and it came
[L452] [22:23.36] into the standard a bit later.
[L453] [22:26.64] But some of these ideas are very old.
[L454] [22:30.40] >> When you put together really impressive
[L455] [22:32.96] people like you know the world's
[L456] [22:34.80] greatest people that you look around and
[L457] [22:37.76] you see how great the other people are
[L458] [22:39.92] and even though each individual is great
[L459] [22:43.36] just the greatness of others can give
[L460] [22:45.28] people this feeling of imposter syndrome
[L461] [22:47.44] that's not necessarily founded. Is that
[L462] [22:49.92] something that you ever felt or saw at
[L463] [22:52.00] >> Bell? Definitely. Um maybe I still got a
[L464] [22:55.76] bit of it, but certainly when I came to
[L465] [22:58.16] Bell Labs and saw the names on the doors
[L466] [23:00.80] and I'd read the papers and it created
[L467] [23:04.24] the fields I like to work in. Yeah. I I
[L468] [23:08.32] thought I have to up my game. I have to
[L469] [23:11.20] do something uh bigger and better than
[L470] [23:15.12] what I had imagined. Um also you talk to
[L471] [23:19.12] them and you learn things. I mean, I
[L472] [23:21.52] learned a lot over lunch where there's a
[L473] [23:24.48] bunch of them uh talking about what
[L474] [23:28.00] they're doing and why they are doing it.
[L475] [23:31.20] There are some places that that has that
[L476] [23:34.16] effect on on people and has this density
[L477] [23:37.68] of talent. Um Cambridge University was
[L478] [23:42.00] computer science was one of those
[L479] [23:43.76] places. I learned a lot there and u the
[L480] [23:47.28] doors were always open. Uh it was sort
[L481] [23:51.12] of almost a policy uh that we kept the
[L482] [23:54.80] doors open because how else would people
[L483] [23:59.28] be able to come and and talk?
[L484] [24:02.32] >> When we talk about a programming
[L485] [24:04.24] language and just generally like
[L486] [24:06.16] language design, if I was to want to
[L487] [24:09.04] build a programming language today, what
[L488] [24:12.00] are all the pieces that you'd need to to
[L489] [24:14.88] build to make a programming language?
[L490] [24:17.76] Well, that's a relatively easy
[L491] [24:22.80] question to answer and everybody asks
[L492] [24:25.84] that question and I think it's a wrong
[L493] [24:28.16] question. Uh what you need is a problem
[L494] [24:31.76] that needs a solution. A lot of people
[L495] [24:35.04] just want to build a language that is
[L496] [24:37.52] better that at what they are doing now
[L497] [24:40.72] and what they particularly are doing.
[L498] [24:43.76] And most of the time that can be done
[L499] [24:47.04] reasonably well with existing languages.
[L500] [24:50.40] And
[L501] [24:52.00] if you build a very specialized language
[L502] [24:54.96] that's fine. But if we're talking about
[L503] [24:57.28] more general purpose languages,
[L504] [24:59.92] uh you you're then building something
[L505] [25:02.24] that when you want to work with somebody
[L506] [25:04.88] else, it's not ideal for them. So um I'm
[L507] [25:09.84] sometimes asked why C++ is so big and uh
[L508] [25:14.08] complicated
[L509] [25:15.68] and uh there's two reasons. One is
[L510] [25:18.40] history. Um I could not build the C++ I
[L511] [25:22.72] wanted uh back in the 80s. um for a
[L512] [25:27.60] variety of reasons, partly uh
[L513] [25:29.76] technology, partly uh computers,
[L514] [25:33.28] um and partly because I didn't know
[L515] [25:35.12] enough and I had to learn. So you do the
[L516] [25:38.64] standard engineering thing, you do the
[L517] [25:40.64] best you can, then you see what works
[L518] [25:43.36] and what doesn't work and you try and
[L519] [25:46.56] fix the problems and then you repeat.
[L520] [25:50.32] And that's how C++ grew. And so there's
[L521] [25:53.52] some
[L522] [25:55.44] leftover things that just gets into the
[L523] [25:57.60] people's way. Now you have spans. You
[L524] [26:01.68] very rarely use pointers and you should
[L525] [26:04.48] certainly not use pointers as resource
[L526] [26:07.04] handles. Uh that was already built in
[L527] [26:09.76] with C classes in 79, but people didn't
[L528] [26:13.36] get it. Um and so there's teaching to do
[L529] [26:18.80] it. But anyway, uh once you figure out
[L530] [26:21.84] that you have a problem that require a
[L531] [26:24.16] new language,
[L532] [26:25.92] then uh you start looking what there is
[L533] [26:30.24] and uh you have lots of help, lots of uh
[L534] [26:35.92] books about analysis and about
[L535] [26:40.56] um code generation. You have frameworks
[L536] [26:44.08] like LLVM that most of the modern
[L537] [26:47.68] languages uses to generate decent code.
[L538] [26:51.36] So most of the languages that compete
[L539] [26:53.76] with C++ does it by uh using a C++
[L540] [26:57.60] infrastructure. It's it's highly
[L541] [26:59.84] amusing. Um but but anyway, focus on the
[L542] [27:04.80] problem and don't think you're the only
[L543] [27:07.36] user. If you think you're the only user,
[L544] [27:10.00] you build a special purpose programming
[L545] [27:11.92] language and that's fine. Uh domain
[L546] [27:16.08] specific languages are great when you
[L547] [27:18.40] find the right
[L548] [27:20.56] uh solution to the right problem, but
[L549] [27:24.48] identify the problem first. Uh in my
[L550] [27:27.76] case, the problem was I needed high and
[L551] [27:30.40] low-level facilities
[L552] [27:32.64] in the same language. Otherwise, I had
[L553] [27:34.88] to use two languages and I had to have
[L554] [27:38.72] them communicate uh properly. High level
[L555] [27:42.48] languages at the time uh tended to uh
[L556] [27:46.00] use interfaces that took away
[L557] [27:48.40] performance. Uh quite often they
[L558] [27:51.12] required garbage collection which is not
[L559] [27:53.36] very good for device drivers for
[L560] [27:56.00] instance or for building garbage
[L561] [27:58.56] collectors. Um so yes identify the
[L562] [28:03.92] problem and uh try and solve it.
[L563] [28:06.24] >> Back when you were creating C++ and you
[L564] [28:08.48] had identified the problem and so then
[L565] [28:10.72] you went off to build C++ and you know
[L566] [28:13.76] there's all these pieces right there's
[L567] [28:15.52] the compiler there's a there's a linker
[L568] [28:18.80] there's you know in the implementations
[L569] [28:21.12] of those there's uh like a parser alexer
[L570] [28:24.48] and you know all those things. uh when
[L571] [28:27.36] you were building the original thing,
[L572] [28:30.00] what was the most technically
[L573] [28:31.76] challenging part to implement?
[L574] [28:34.08] >> I don't think any part was particularly
[L575] [28:38.40] challenging. It was more that there was
[L576] [28:40.16] many parts as you point out. One of the
[L577] [28:43.52] things I decided that caused trouble uh
[L578] [28:48.32] later was that I wasn't going to touch
[L579] [28:50.72] the linker. And it came simply because I
[L580] [28:54.32] asked around and I realized people were
[L581] [28:56.64] using about 25 uh different linkers in
[L582] [29:00.16] in Bell Labs just just in Bell Labs. And
[L583] [29:03.76] so if I wanted to serve uh my obvious
[L584] [29:07.44] initial uses, I would have to write
[L585] [29:10.48] interfaces or modifications to 25
[L586] [29:13.68] linkers. And nobody wants you to touch
[L587] [29:16.48] their linker because if you make a
[L588] [29:18.88] mistake, everything breaks.
[L589] [29:21.76] So I decided a rule don't mess with the
[L590] [29:25.76] linker. Later people have messed with
[L591] [29:28.64] the linkers and made them better for C++
[L592] [29:31.20] but that was after C++ became a major
[L593] [29:33.92] issue. Uh the other thing was that there
[L594] [29:38.88] was many different optimizers.
[L595] [29:42.72] every
[L596] [29:44.48] um computer uh from different sources
[L597] [29:48.88] had a different optimizer and again I
[L598] [29:52.72] couldn't write u a dozen optimizers.
[L599] [29:56.72] I mean I'm I'm going to write a language
[L600] [29:59.84] here right and I can't if I wanted to be
[L601] [30:03.28] a optimizer specialist for uh deck
[L602] [30:07.04] computers say um I can become that I
[L603] [30:11.36] have the background I have the training
[L604] [30:13.68] but that wasn't what I wanted to do I
[L605] [30:16.00] wanted to build first a distributed
[L606] [30:19.76] system and then when my friends and
[L607] [30:21.84] colleagues started using seu classes um
[L608] [30:25.20] I wanted to help them uh and they were
[L609] [30:28.24] doing things like network simulations,
[L610] [30:31.52] hardware layout,
[L611] [30:33.84] uh positioning of satellites,
[L612] [30:37.76] all kinds of interesting stuff. So that
[L613] [30:40.32] was worth doing. And [snorts] so I
[L614] [30:42.80] decided that actually there was a common
[L615] [30:45.36] interface to all these optimizers and uh
[L616] [30:49.44] code generators. It's called C. So let's
[L617] [30:53.68] use C as the assembler.
[L618] [30:56.80] And that worked nicely. C was very good
[L619] [31:00.32] at the low level was part of the reason
[L620] [31:02.40] I chose it. So let's use it for the low
[L621] [31:05.52] level. And I could have hidden C and re
[L622] [31:10.48] uh created a probably a better
[L623] [31:12.72] interface. But I decided that uh
[L624] [31:17.92] I'll just use C have C compatibility.
[L625] [31:21.28] Uh at the time what I said was that well
[L626] [31:25.76] we can have Dennis's mistakes which we
[L627] [31:28.48] know and we can have my mistakes which
[L628] [31:31.36] we don't know yet. Um so uh we'll take
[L629] [31:34.72] Dennis's that's u much more manageable
[L630] [31:38.00] and understandable and I don't have to
[L631] [31:40.80] teach people how to write a for loop and
[L632] [31:43.60] things like that. So
[L633] [31:46.48] that's C compatibility came in that way
[L634] [31:49.76] partly as an implementation technique
[L635] [31:52.72] partly uh to get into the culture and uh
[L636] [31:57.04] tool support and such.
[L637] [32:00.00] I saw somewhere in in my research that
[L638] [32:03.12] um you know C++
[L639] [32:05.52] was used to write some part of uh the
[L640] [32:10.16] the language tool chain and to me
[L641] [32:12.88] immediately I have this thought of
[L642] [32:14.08] there's this chicken and egg problem
[L643] [32:15.60] because how do you use this language to
[L644] [32:18.88] build something that it is using itself
[L645] [32:21.84] h how does that work
[L646] [32:23.60] >> this is bootstrapping and it's uh it it
[L647] [32:27.92] was not an unusual ual thing. So I
[L648] [32:31.36] started with C and in C I wrote a um a
[L649] [32:36.32] pre-processor that did some of the
[L650] [32:39.20] fundamental things in uh in in in what
[L651] [32:43.60] became C++
[L652] [32:45.68] uh classes and fairly simple inheritance
[L653] [32:49.04] and overloading and such. And then I
[L654] [32:54.40] in that I wrote a a simple compiler for
[L655] [32:59.92] again what was a subset of uh of of C++.
[L656] [33:06.48] And uh now I can use uh operator
[L657] [33:10.96] overloading and overloading in general
[L658] [33:13.52] classes. So I can build a a scope class
[L659] [33:17.52] that handles look up and naming and
[L660] [33:20.56] things like that. And then then you work
[L661] [33:23.68] from there. Um
[L662] [33:27.12] just writing the next version in the
[L663] [33:30.48] previous version. You keep keep going
[L664] [33:33.60] and uh after a couple of years you have
[L665] [33:37.44] something that became known to the world
[L666] [33:40.56] as C++. and I wrote a book about it and
[L667] [33:43.92] a compiler um came out in the world. But
[L668] [33:47.84] I didn't invent this technique. This was
[L669] [33:50.48] known as bootstrapping. Um I think I was
[L670] [33:53.92] taught it as an undergrad that you could
[L671] [33:56.32] do things like that.
[L672] [33:58.40] >> Most people they look at C++ and they
[L673] [34:01.68] think that's an object-oriented
[L674] [34:03.28] language. And I've heard you say
[L675] [34:05.60] multiple times that that's not the case
[L676] [34:08.32] or that's not your immediate thought.
[L677] [34:09.76] And why is that? Yeah, I I never called
[L678] [34:12.24] it an object-oriented
[L679] [34:14.40] uh programming language. If you look at
[L680] [34:17.12] the C++ programming language, the first
[L681] [34:19.52] edition, um the closest I come is to say
[L682] [34:24.88] uh some some some people call these
[L683] [34:27.60] techniques object- based.
[L684] [34:30.40] Actually, it's more focused on classes.
[L685] [34:32.96] It's type oriented, class oriented. uh
[L686] [34:36.64] it actually supports the techniques of
[L687] [34:39.20] object orientation very well and it in
[L688] [34:43.76] particular follows similar's model of uh
[L689] [34:48.72] defining types defining classes and
[L690] [34:52.24] defining class hierarchies to uh handle
[L691] [34:56.96] uh groups of related uh classes but that
[L692] [35:00.88] was never all it was for instance I do
