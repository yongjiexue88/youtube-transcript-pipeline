Chunk 1; segments 1–142. 

# Creator of Lua: You Can Interpret C And Compile Python | Roberto Ierusalimschy

Source ID: source-83ff6425ab4f55d4
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lua_You_Can_Interpret_C_And_Compile_Python_Roberto_Ierusalimschy_en.txt
Video: https://www.youtube.com/watch?v=4cWFOQQjLvk

[L10] [00:00.00] I always hear there's there's compiled
[L11] [00:02.28] languages and there's dynamic or
[L12] [00:04.72] interpreted languages, I guess.
[L13] [00:06.80] But really that distinction is in the
[L14] [00:09.44] tool chain, not necessarily in the way
[L15] [00:11.72] that the symbols are laid out in the
[L16] [00:13.28] source code. Like I could write compiler
[L17] [00:15.92] or program that takes in Python code and
[L18] [00:19.52] then converts it into machine code and
[L19] [00:22.76] then I would have compiled Python.
[L20] [00:24.80] >> And you can interpret C code, too. You
[L21] [00:27.52] can write an interpreter for C.
[L22] [00:30.60] Yes. But the the main difference is
[L23] [00:32.92] actually what it's easy to For instance,
[L24] [00:35.68] as I said, one of the hallmarks of
[L25] [00:38.28] interpreted languages eval. So,
[L26] [00:41.96] if you want to compile the language and
[L27] [00:44.92] keep eval, you have to have a compiler
[L28] [00:48.60] as a library of your
[L29] [00:51.00] of your runtime because you may want to
[L30] [00:53.48] compile things
[L31] [00:55.68] during execution. This is the hallmark
[L32] [00:58.12] of a dynamic language. That's So, you
[L33] [01:00.60] can create code while running code. So,
[L34] [01:05.16] that part is that that's why
[L35] [01:08.24] in
[L36] [01:09.64] more much more often than not
[L37] [01:13.72] dynamic languages are interpreted.
[L38] [01:17.20] But you can compile but then sometimes
[L39] [01:19.68] or some compilers do not handle eval at
[L40] [01:23.04] all. They say, "Oh, you can compile as
[L41] [01:25.12] long as your program doesn't have
[L42] [01:27.28] evals." The so there is some
[L43] [01:29.56] restrictions. And as I said, you can
[L44] [01:32.96] interpret C code, I mean, but you'll be
[L45] [01:36.72] extremely slowly with it. It doesn't but
[L46] [01:40.96] >> I think one big difference I mean, when
[L47] [01:42.56] I look at statically you know, static
[L48] [01:45.32] languages or compiled languages,
[L49] [01:47.40] they they seem to have type systems in
[L50] [01:49.44] them or the type annotations.
[L51] [01:52.24] What is the role of a type system in the
[L52] [01:54.84] compilation process?
[L53] [01:57.20] >> Depends a lot of the on the type system.
[L54] [02:00.84] Several type systems like in C for
[L55] [02:03.80] instance are written to be an very
[L56] [02:06.72] important part of the compilation
[L57] [02:09.28] process. So, if you have the right type
[L58] [02:12.48] system, it's much much easier to write a
[L59] [02:15.84] compiler.
[L60] [02:17.16] A trivial example is one of the space
[L61] [02:20.04] for variables because if you know all
[L62] [02:22.56] this is an integer, this is a float,
[L63] [02:25.20] this is a double, you know exactly how
[L64] [02:27.64] many bytes of memory you need to that.
[L65] [02:31.08] Otherwise, it's a mess of more often
[L66] [02:33.84] than not you have to keep everything in
[L67] [02:35.52] the heap dynamically allocated. And so,
[L68] [02:40.16] huge
[L69] [02:41.88] penalty in performance. And for
[L70] [02:44.12] instance, when you see it as I said, a
[L71] [02:46.00] trivial you have an addition.
[L72] [02:48.52] A plus B. If you know the type of A
[L73] [02:52.52] A plus B, you have the type of A, the
[L74] [02:54.64] type of B, you have a compile time, you
[L75] [02:57.08] know all this plus is a
[L76] [02:59.60] I'm adding two integers, I just generate
[L77] [03:02.00] the machine code to add integers, and
[L78] [03:04.76] there everything is fine. In a dynamic
[L79] [03:06.72] language, I see a plus,
[L80] [03:09.16] I don't I I I compile
[L81] [03:11.60] to a virtual in the virtual language it
[L82] [03:14.00] is just piece of plus, but then how do I
[L83] [03:17.44] at run time you have to check what is A
[L84] [03:20.00] or A is an integer, B is a float, oh
[L85] [03:22.60] yeah, I have to convert or B is a string
[L86] [03:25.16] or depending on the language, you're
[L87] [03:27.68] you're not doing addition, it can be
[L88] [03:29.32] doing concatenation, or you can just
[L89] [03:31.80] calling someone, and you have to do all
[L90] [03:33.80] that
[L91] [03:34.72] at run time. So, types can be very very
[L92] [03:38.44] important to compile efficiently, but of
[L93] [03:43.72] course you have to
[L94] [03:45.84] have a type system that
[L95] [03:48.68] that there are several language now like
[L96] [03:50.68] type type script that
[L97] [03:53.56] types are kind of
[L98] [03:55.68] you do not guarantee that everything has
[L99] [03:58.08] the types you said
[L100] [04:00.20] they have. So, then it's impossible to
[L101] [04:03.44] use them to compile because oh, thread
[L102] [04:05.84] the BA will be an integer, but if it's
[L103] [04:08.36] not I mean it's if it I have an an
[L104] [04:11.28] integer register to put 40
[L105] [04:14.12] it must be a register or
[L106] [04:17.00] things do not work. So, but if you have
[L107] [04:19.36] the right type system they are essential
[L108] [04:23.04] for a good compilation.
[L109] [04:24.88] >> I know some programming languages have
[L110] [04:26.28] type inference. What if you did you run
[L111] [04:28.84] type inference and you got a unambiguous
[L112] [04:32.48] set of types and then you use that in
[L113] [04:35.56] compilation. Like could you do that for
[L114] [04:37.56] Lua?
[L115] [04:39.48] >> No.
[L116] [04:41.92] I I mean that's not computable, but a
[L117] [04:44.84] lot of people tried to
[L118] [04:47.16] to do
[L119] [04:48.76] in type inference for dynamic languages
[L120] [04:52.40] and it's really hard pro- problem and
[L121] [04:55.60] it's very difficult to do anything
[L122] [04:57.60] useful in terms of performance. What you
[L123] [05:01.16] sometimes you get, but you have a very
[L124] [05:04.40] restrict
[L125] [05:06.00] Oh, if you write your program in that
[L126] [05:08.72] specific way use for So, it's like you
[L127] [05:12.72] don't have the type, but you write the
[L128] [05:14.68] program thinking about type and then if
[L129] [05:18.08] the program is that very particular
[L130] [05:20.40] format, then you can
[L131] [05:23.92] do type inference and everything goes
[L132] [05:26.36] well. Otherwise, either type inference
[L133] [05:29.28] doesn't work or I mean it works, but it
[L134] [05:32.48] actually it infers very generic types
[L135] [05:35.88] for everything and so you cannot take
[L136] [05:38.80] advantage of of of the types because
[L137] [05:41.80] exactly the dynamic nature of the
[L138] [05:44.36] language. This is also happens with
[L139] [05:47.56] legit for instance.
[L140] [05:49.40] You can get much much better performance
[L141] [05:52.44] if you have a kind of a type system in
[L142] [05:55.48] your in your mind. Usually we do that
[L143] [05:58.52] and you and you follow that type rules
[L144] [06:01.84] even without that. I mean the compiler
[L145] [06:04.36] the language does not impose them on
[L146] [06:07.00] you, but you assume or I'm going to
[L147] [06:08.96] follow those
[L148] [06:10.36] sometime discipline. I'm not going to to
[L149] [06:13.52] to use the same variable to store
[L150] [06:15.48] integers and strings etc. And then you
[L151] [06:18.60] can have much better results.
