Chunk 2; segments 366–740. Start may repeat the previous chunk for context.

# Creator of Lua: What People Get Wrong About Scripting Languages | Roberto Ierusalimschy

Source ID: source-eb789a15ce2c0992
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lua_What_People_Get_Wrong_About_Scripting_Languages_Roberto_Ierusalimschy_en.txt
Video: https://www.youtube.com/watch?v=jCZnFKk6M9A

[L375] [15:41.68] it's machine dependent. It's not very
[L376] [15:44.32] productive. I mean, you you do a lot of
[L377] [15:46.60] work and it only works on that
[L378] [15:48.56] architecture. And then I want to running
[L379] [15:51.20] another architecture. But, Mike Paul he
[L380] [15:54.40] created a kind of
[L381] [15:57.56] pseudo pseudo assembler that he writes
[L382] [16:00.88] in this assembly and then he translates
[L383] [16:03.60] that assembler through real machine
[L384] [16:05.84] pulled of the different machines. So,
[L385] [16:08.16] trying to unify the different
[L386] [16:10.40] architectures. So, there is a a lot of
[L387] [16:12.60] work, but I I don't like it. I I think
[L388] [16:15.04] architecture I
[L389] [16:18.08] I like to study, but I don't like to to
[L390] [16:20.76] to to work with because I think it's
[L391] [16:23.20] very unstable. Each new version they
[L392] [16:25.52] change that or they change that the I
[L393] [16:28.28] mean they they change the ABI for
[L394] [16:30.68] something and then now the stack has to
[L395] [16:32.96] be aligned in in some very
[L396] [16:35.80] particular way. And so
[L397] [16:38.80] And [clears throat] the of course also
[L398] [16:40.40] to to get that performance that he gets
[L399] [16:44.12] he made the what's called the trace
[L400] [16:47.04] compiler. The idea of a trace compiler
[L401] [16:49.96] that instead of a function
[L402] [16:52.72] and compiling a function
[L403] [16:55.24] it could it works like a
[L404] [16:57.88] any legit that it tries to detect things
[L405] [17:00.76] that are executed frequently. And so it
[L406] [17:03.80] starts what's called a trace. It it gets
[L407] [17:07.12] recording everything that the code is
[L408] [17:10.36] doing including function calls, etc.
[L409] [17:14.04] Until it closes the loop.
[L410] [17:17.20] And then it compiles that loop
[L411] [17:20.40] including function calls, etc.
[L412] [17:22.52] Everything in line. It com-
[L413] [17:24.72] compiles that for that specific, for
[L414] [17:27.60] instance, so that number of happened to
[L415] [17:29.92] be an integer, so it compiles after the
[L416] [17:32.96] number will be an integer again, and
[L417] [17:35.48] there is a lot of checks just check if
[L418] [17:37.72] everything is as assumed, and then it
[L419] [17:41.00] executes the loop. And then this is
[L420] [17:43.08] very, very, very fast. But anything that
[L421] [17:46.68] is different, for instance, you call
[L422] [17:48.92] again that you call it frequently with
[L423] [17:51.76] integers, and suddenly you call through
[L424] [17:53.88] with a float, then at some part of the
[L425] [17:56.52] code it's it is
[L426] [17:58.88] it breaks the the the condition, and you
[L427] [18:01.52] have to to return to the interpreter
[L428] [18:04.84] part, and I think that's one of the
[L429] [18:07.04] worst parts is that you you have to
[L430] [18:09.16] translate the state that it's all
[L431] [18:13.24] compressed into registers, etc. For
[L432] [18:16.40] instance, you don't even have a call
[L433] [18:17.92] stack because you didn't
[L434] [18:20.00] do the call you didn't do the calls, you
[L435] [18:22.08] just inlined it. But then, oops,
[L436] [18:24.48] something went wrong. Now you have to
[L437] [18:26.76] continue interpreting, so you have to
[L438] [18:29.20] recreate the stack that you didn't
[L439] [18:31.40] create originally, etc. So, I mean, I
[L440] [18:34.88] even
[L441] [18:36.13] >> [laughter]
[L442] [18:36.36] >> even to think about that I have
[L443] [18:39.36] headaches.
[L444] [18:40.84] >> Standard Lua is portable, but to execute
[L445] [18:43.68] on a machine, it eventually gets
[L446] [18:45.12] converted into machine instructions
[L447] [18:47.56] somewhere. Where in the stack is it
[L448] [18:50.08] eventually translated to machine
[L449] [18:51.76] instructions?
[L450] [18:52.84] >> Lua is written in C. The interpreter is
[L451] [18:55.84] written in C, and then you so you you
[L452] [18:59.32] compile that into machine code, the
[L453] [19:01.96] interpreter, the Lua code. Then the
[L454] [19:04.24] point when you get some some
[L455] [19:06.72] some I mean, the Lua code the Lua
[L456] [19:08.44] interpreter code. When you get some Lua
[L457] [19:10.88] code,
[L458] [19:12.00] you do what is we call a
[L459] [19:13.36] pre-compilation,
[L460] [19:15.08] that is we we translate to an internal
[L461] [19:17.84] language,
[L462] [19:19.24] and then the interpreter is just a big
[L463] [19:21.68] loop.
[L464] [19:22.92] It's a loop with a switch. I mean,
[L465] [19:25.00] that's a a very big simplification, but
[L466] [19:27.28] that that in in general terms, a loop
[L467] [19:30.08] with a switch that get instruction,
[L468] [19:33.24] does a switch, and see all this
[L469] [19:35.16] instruction is the instructions are
[L470] [19:37.88] quite similar to a CPU. Move that, but
[L471] [19:41.96] then instead of creating it executes
[L472] [19:44.84] that structure. Move Move A to B, so it
[L473] [19:48.64] it does a
[L474] [19:49.92] move A to B and executes that, and again
[L475] [19:52.88] repeats, executes the next instruction.
[L476] [19:55.84] So, this is how a interpreter works and
[L477] [20:00.00] basically, so we we precompile a Lua.
[L478] [20:03.64] There is a compilation, but we compile
[L479] [20:05.64] for this virtual machine,
[L480] [20:07.88] and then we have this main
[L481] [20:10.92] interpreter loop that people call that
[L482] [20:13.84] just fetch each instruction. So, a jump
[L483] [20:17.88] is just a jump. You have an array of of
[L484] [20:20.36] byte codes. A jump will just go to that.
[L485] [20:23.40] You have a
[L486] [20:24.64] a counter that tells where you are in
[L487] [20:27.04] this array. A jump you just update that
[L488] [20:30.04] counter. It goes to another position of
[L489] [20:32.08] that array where you're going to So,
[L490] [20:34.40] it's like you s-
[L491] [20:36.40] you emulate the CPU in software. It's
[L492] [20:40.32] written in C,
[L493] [20:41.84] the the interpreter. This main loop is
[L494] [20:44.16] written in C.
[L495] [20:45.96] So, if you compile it in Linux, it will
[L496] [20:48.32] run in Linux or in a
[L497] [20:51.24] X86
[L498] [20:52.84] architecture, it will run in that
[L499] [20:54.80] architecture. If you compile that in the
[L500] [20:56.80] Mac, it will run in the Mac. It's a C
[L501] [20:58.96] program.
[L502] [21:00.56] >> Got it. Okay, so and that's that's the
[L503] [21:02.24] part that's not portable, and the C
[L504] [21:04.04] compiler handles that.
[L505] [21:05.72] >> Yes. Yes. Yes. The all portability of
[L506] [21:08.28] Lua comes on top of portability of C.
[L507] [21:12.16] >> How does JIT compare to ahead-of-time
[L508] [21:14.72] compilation in terms of performance?
[L509] [21:17.72] >> Both ahead-of-time Any kind of
[L510] [21:19.76] compilation is easily not easily, but it
[L511] [21:23.08] can be 10 times faster than interpreting
[L512] [21:26.12] or even 100 times faster than
[L513] [21:28.88] interpreting depending what you were are
[L514] [21:31.20] doing. But 10 times is a very good
[L515] [21:34.56] figure. Between ahead-of-time and
[L516] [21:39.08] trace compilation, then depends a lot of
[L517] [21:42.52] what you are doing.
[L518] [21:44.88] After trace compilation is particularly
[L519] [21:48.60] good for
[L520] [21:50.76] benchmarks.
[L521] [21:53.36] Because you're repeating it more or less
[L522] [21:55.76] they are very uniform. You are doing
[L523] [21:57.72] exactly the same thing again and again
[L524] [21:59.84] and again. So, then trace compilers
[L525] [22:03.48] shine. They I mean this is the best they
[L526] [22:05.84] can do.
[L527] [22:07.16] In real programs, that's
[L528] [22:10.92] depends a lot, but but but you I
[L529] [22:14.24] wouldn't say there is a clear winner
[L530] [22:16.92] between the two. I think depends a lot
[L531] [22:18.96] of the kind of problem.
[L532] [22:20.52] >> Is it possible to write an ahead-of-time
[L533] [22:23.52] compiler for Lua?
[L534] [22:24.68] >> Yes, there are there are
[L535] [22:27.48] several.
[L536] [22:28.92] None I mean I think I don't not sure if
[L537] [22:32.48] there is anyone on production quality,
[L538] [22:35.92] but for research etc. there are several.
[L539] [22:39.44] I I have a student who wrote one like a
[L540] [22:42.44] master thesis. We did
[L541] [22:45.16] simple Lua compiler ahead-of-time Lua
[L542] [22:48.40] compiler or something like that. The
[L543] [22:50.48] exactly because it was just
[L544] [22:52.26] [clears throat] it gets these opcodes
[L545] [22:54.64] and expands into
[L546] [22:56.96] into C code and then you
[L547] [22:59.80] send that through through a C compiler
[L548] [23:02.52] and then you have a head of time comp
[L549] [23:05.08] head of time compiler for Lua and it
[L550] [23:07.84] gave like three five times boosting
[L551] [23:11.44] performance. You very very
[L552] [23:14.52] as the title said it's like ridiculous
[L553] [23:17.68] simple compiler.
[L554] [23:21.28] >> I always hear there's there's compiled
[L555] [23:23.56] languages and there's dynamic or
[L556] [23:26.00] interpreted languages I guess.
[L557] [23:28.08] But really that distinction is in the
[L558] [23:30.76] tool chain not necessarily in the way
[L559] [23:33.00] that the symbols are laid out on the
[L560] [23:34.60] source code. Like I could write compiler
[L561] [23:37.24] or program that takes in Python code and
[L562] [23:40.80] then converts it into machine code and
[L563] [23:44.04] then I would have compiled Python.
[L564] [23:46.08] >> And you can interpret C code too. You
[L565] [23:48.84] can write an interpreter for C.
[L566] [23:51.88] Yes. But the the main difference is
[L567] [23:54.20] exactly what it's easy to For instance,
[L568] [23:56.96] as I said, one of the hallmarks of
[L569] [23:59.60] interpreted languages is the eval. So,
[L570] [24:03.24] if you want to compile the language and
[L571] [24:06.20] keep eval, you have to
[L572] [24:08.44] have a compiler as a library of your
[L573] [24:12.28] of your runtime because you may want to
[L574] [24:14.76] compile things
[L575] [24:16.92] during execution. This is the hallmark
[L576] [24:19.40] of a dynamic language. That's all. You
[L577] [24:21.88] can create code while running code. So,
[L578] [24:26.44] that part is that that's why
[L579] [24:30.92] more much more often than not
[L580] [24:35.00] dynamic languages are interpreted.
[L581] [24:38.52] But you can compile but then sometimes
[L582] [24:40.96] or some compilers do not handle eval at
[L583] [24:44.32] all. They say, "Oh, you can compile as
[L584] [24:46.40] long as your program doesn't have
[L585] [24:48.56] evals." The so there is some
[L586] [24:50.84] restrictions. And as I said, you can
[L587] [24:54.24] interpret C code I mean, but you'll be
[L588] [24:58.08] extremely slowly with it doesn't but
[L589] [25:02.24] >> I think one big difference I when I look
[L590] [25:04.16] at statically or you know static
[L591] [25:06.64] languages or compiled languages
[L592] [25:08.72] they they seem to have type systems in
[L593] [25:10.76] them or the type annotations.
[L594] [25:13.56] What is the role of a type system in the
[L595] [25:16.16] compilation process?
[L596] [25:18.48] >> Depends a lot of the on the type system.
[L597] [25:22.08] The several type systems like in C for
[L598] [25:25.16] instance are written to be an very
[L599] [25:28.04] important part of the compilation
[L600] [25:30.56] process. So if you have the right type
[L601] [25:33.76] system is much much easier to write a
[L602] [25:37.12] compiler.
[L603] [25:38.64] A trivial example is when the space for
[L604] [25:41.56] variables because if you know all this
[L605] [25:44.12] is an integer, this is a float, this is
[L606] [25:46.84] a double, you know exactly how many
[L607] [25:49.28] bytes of memory you need to that.
[L608] [25:52.36] Otherwise it's a massive more often than
[L609] [25:55.32] not you have to keep everything in the
[L610] [25:56.96] heap dynamically allocated and so
[L611] [26:01.48] huge
[L612] [26:03.16] penalty in performance. And for instance
[L613] [26:05.76] when you see it as I said a trivial you
[L614] [26:07.96] have an addition.
[L615] [26:09.80] A plus B. If you know the type of A
[L616] [26:13.84] A plus B, you have the type of A, the
[L617] [26:15.92] type of B, you have a compile time you
[L618] [26:18.36] know all this plus is a
[L619] [26:20.88] I'm adding two integers. I just generate
[L620] [26:23.28] the machine code to add integers and
[L621] [26:26.08] there everything it's fine. In a dynamic
[L622] [26:28.00] language as here plus
[L623] [26:30.44] I don't I I I compile
[L624] [26:32.92] to a virtual in the virtual language it
[L625] [26:35.32] is just piece of plus but then how do I
[L626] [26:38.72] at run time you have to check what is A?
[L627] [26:41.32] Oh, A is an integer, B is a float. Oh, I
[L628] [26:44.04] have to convert or B is a string or
[L629] [26:46.68] depending on the language you're if
[L630] [26:48.84] you're not doing addition you can be
[L631] [26:50.64] doing concatenation or you can just
[L632] [26:53.12] calling some and you have to do all that
[L633] [26:56.04] at runtime. So, types can be very, very
[L634] [26:59.72] important to compile efficiently, but of
[L635] [27:05.00] course you have to
[L636] [27:07.16] have a type system that
[L637] [27:10.00] that there are several language now like
[L638] [27:12.00] type type script that the
[L639] [27:14.84] types are kind of
[L640] [27:16.88] you do not guarantee that everything has
[L641] [27:19.32] the types you said
[L642] [27:21.52] they have. So, then it's impossible to
[L643] [27:24.76] use them to compile because oh, probably
[L644] [27:27.80] will be an integer, but if it's not I
[L645] [27:30.00] mean it's if it I have an integer
[L646] [27:33.08] register to put 20
[L647] [27:35.44] it must be a register or
[L648] [27:38.32] things will not work. So, but if you
[L649] [27:40.48] have the right type system they are
[L650] [27:43.56] essential for a good compilation.
[L651] [27:46.16] >> I know some programming languages have
[L652] [27:47.60] type inference, but if you did you ran
[L653] [27:50.12] type inference and you got a unambiguous
[L654] [27:53.80] set of types and then you use that in
[L655] [27:56.88] compilation. Like could you do that for
[L656] [27:58.88] Lua?
[L657] [28:00.80] >> Nope.
[L658] [28:03.20] I mean that's not computable, but a lot
[L659] [28:06.44] of people tried to to do
[L660] [28:10.08] in type inference for dynamic languages
[L661] [28:13.72] and it's really hard pro problem and
[L662] [28:16.88] it's very difficult to do anything
[L663] [28:18.88] useful in terms of performance. What you
[L664] [28:22.44] sometimes you get but you have a very
[L665] [28:25.68] restrict
[L666] [28:27.32] If you write your program in that
[L667] [28:30.04] specific way use for So, it's like you
[L668] [28:34.04] don't have the type but you write the
[L669] [28:35.96] program thinking about type and then if
[L670] [28:39.40] the program is that very particular
[L671] [28:41.68] format, then you can
[L672] [28:45.24] do type inference and everything goes
[L673] [28:47.68] well. Otherwise, either type inference
[L674] [28:50.60] doesn't work, or I mean, it works, but
[L675] [28:53.56] it actually it infers very generic types
[L676] [28:57.20] for everything, and so you cannot take
[L677] [29:00.12] advantage of of of the types. Because
[L678] [29:03.12] exactly the dynamic nature of the
[L679] [29:05.72] language. This This also happens if Lua
[L680] [29:08.88] JIT, for instance.
[L681] [29:10.60] You can get much much better performance
[L682] [29:13.72] if you have a kind of a type system in
[L683] [29:16.80] your in your mind. Usually, we do that,
[L684] [29:19.76] and you and you follow that type rules
[L685] [29:23.08] even without a type I mean, the compiler
[L686] [29:25.60] the language does not impose them on
[L687] [29:28.28] you, but you assume, "Oh, I'm going to
[L688] [29:30.24] follow those some type discipline. I'm
[L689] [29:33.48] not going to to to use the same variable
[L690] [29:36.20] to store integers and strings, etc." And
[L691] [29:39.56] then you can have much better results.
[L692] [29:43.32] >> OpenAI, [snorts]
[L693] [29:44.36] Anthropic, Cursor, and Vercel all use
[L694] [29:47.64] this product to make their lives better.
[L695] [29:49.84] And the problem it solves is when you're
[L696] [29:51.76] building SaaS or an ad product, and you
[L697] [29:54.40] want to sell to other companies, there's
[L698] [29:56.32] all these requirements you need to meet.
[L699] [29:58.40] There's SSL, there's SCIM, there's RBA,
[L700] [30:02.04] there's audit logs. These are all things
[L701] [30:03.84] that take time to integrate, but aren't
[L702] [30:06.04] the main focus of your app. WorkOS is an
[L703] [30:08.36] API layer that lets you meet all of
[L704] [30:10.00] these requirements in just a few lines
[L705] [30:12.20] of code. So, let's say you have a new
[L706] [30:14.24] SaaS product, and you want to sell to
[L707] [30:15.92] other
[L708] [30:17.04] WorkOS will solve all of these critical
[L709] [30:19.04] feature gaps for you.
[L710] [30:21.04] You can check them out at workos.com to
[L711] [30:23.60] learn more and get started, and I
[L712] [30:25.76] appreciate them for supporting my work
[L713] [30:27.60] and sponsoring this podcast. Earlier you
[L714] [30:30.08] mentioned that Lua can call C, and C
[L715] [30:33.32] could call Lua. And
[L716] [30:36.64] you mentioned we talked about the the
[L717] [30:38.88] compiler and the interpreter, and how do
[L718] [30:41.56] these pieces work together in the case
[L719] [30:43.72] where you're chaining different
[L720] [30:45.36] programming languages?
[L721] [30:47.60] >> Yeah, the the the main trick, I mean,
[L722] [30:49.64] it's not a trick, the technique
[L723] [30:52.24] for Lua calling C is a C pointers.
[L724] [30:57.20] Function pointers. There is a pointer to
[L725] [31:00.16] a function.
[L726] [31:01.48] This is part of the official C
[L727] [31:04.60] language. So, when you start Lua,
[L728] [31:08.64] suppose you are in C, yeah, as I said,
[L729] [31:11.04] you create a library.
[L730] [31:13.60] Uh all right, you create a state, a Lua
[L731] [31:15.88] state, and then you can register, you
[L732] [31:18.48] send to Lua
[L733] [31:20.60] C pointers, so function pointers, I
[L734] [31:22.80] mean, pointers to functions in your C
[L735] [31:25.68] library. Associated with names, Lua
[L736] [31:28.96] stores that in some data structure.
[L737] [31:32.52] Okay, so it says, "Oh, the function sign
[L738] [31:36.04] is associated with that pointer, etc."
[L739] [31:38.80] So, when it's it's doing the
[L740] [31:41.36] interpretation, "Oh, this instruction is
[L741] [31:44.20] call, instruction call. Let's see what
[L742] [31:47.00] it's calling. Oh, it's calling A. What
[L743] [31:49.00] is the value of A? Oh, it's a pointer to
[L744] [31:51.92] and then it calls that pointer." And
[L745] [31:54.20] then we do the call the the the C
[L746] [31:57.28] function to do that.
[L747] [31:59.92] And the when when C wants to call Lua, I
[L748] [32:04.08] I mean,
[L749] [32:04.96] a Lua function is just a data structure
