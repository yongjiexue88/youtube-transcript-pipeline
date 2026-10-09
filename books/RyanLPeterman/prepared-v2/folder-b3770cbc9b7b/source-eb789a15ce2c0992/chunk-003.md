Chunk 3; segments 733–1113. Start may repeat the previous chunk for context.

# Creator of Lua: What People Get Wrong About Scripting Languages | Roberto Ierusalimschy

Source ID: source-eb789a15ce2c0992
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Lua_What_People_Get_Wrong_About_Scripting_Languages_Roberto_Ierusalimschy_en.txt
Video: https://www.youtube.com/watch?v=jCZnFKk6M9A

[L742] [31:47.00] it's calling. Oh, it's calling A. What
[L743] [31:49.00] is the value of A? Oh, it's a pointer to
[L744] [31:51.92] and then it calls that pointer." And
[L745] [31:54.20] then we do the call the the the C
[L746] [31:57.28] function to do that.
[L747] [31:59.92] And the when when C wants to call Lua, I
[L748] [32:04.08] I mean,
[L749] [32:04.96] a Lua function is just a data structure
[L750] [32:08.20] from the point of view of of C, just an
[L751] [32:10.88] array of byte codes of up codes, and
[L752] [32:14.48] then it's calls the Lua interpreter
[L753] [32:17.72] function, "Oh,
[L754] [32:19.48] please interpret that function for me."
[L755] [32:22.92] So, C can call Lua to interpret that
[L756] [32:25.56] function, and that function is running,
[L757] [32:27.64] and then can call a C function using a
[L758] [32:30.68] pointer, and you can have that in the
[L759] [32:33.04] stack several levels. So, you are
[L760] [32:35.08] running a Lua function that calls C, and
[L761] [32:37.48] C calls Lua again, and Lua calls C, and
[L762] [32:40.72] you have recursive stuff in that, etc.
[L763] [32:43.92] And everything works and it's just
[L764] [32:46.72] just works.
[L765] [32:48.60] >> In one of your talks on Lua, you
[L766] [32:50.88] mentioned that there's security benefits
[L767] [32:52.88] to using a scripting language. What are
[L768] [32:55.48] those benefits and how does it protect
[L769] [32:57.36] the hardware?
[L770] [32:58.40] >> It's not only hardware. Once I I I gave
[L771] [33:01.92] a talk here in in Brazil. I was called
[L772] [33:05.32] it to to give a talk in a PyCon
[L773] [33:09.16] a PyCon they they called the Python
[L774] [33:11.40] conference in Brazil. They called me for
[L775] [33:14.04] a talk. At the end of the talk I said,
[L776] [33:16.20] "Oh, Lua is we use it as a scripting
[L777] [33:18.16] language." As I said, emphasizing that
[L778] [33:21.28] thing that you have this dual language
[L779] [33:24.00] architecture and we I I know of case of
[L780] [33:27.44] Lua being used with C, with C++,
[L781] [33:30.84] with Fortran, with several different
[L782] [33:33.12] languages. And then someone in the
[L783] [33:35.08] audience says, "Oh, we also
[L784] [33:37.72] use Lua for scripting Python programs."
[L785] [33:41.08] And what what's that the case? They they
[L786] [33:43.08] they have a huge Python program
[L787] [33:45.80] for financial stuff that has a do a lot
[L788] [33:49.32] of financial transactions, etc. And they
[L789] [33:52.56] wanted to do script I mean to have a
[L790] [33:55.08] like
[L791] [33:56.00] a common line where you could write
[L792] [33:58.24] instructions to be executed by the the
[L793] [34:02.76] at runtime, for instance, for debugging
[L794] [34:05.04] or for inspecting, for
[L795] [34:07.20] whatever you need some kind of end-user
[L796] [34:10.44] programming.
[L797] [34:11.68] But they said exactly what I was talking
[L798] [34:14.28] about spaces. In Python,
[L799] [34:17.68] basically, if you have a common line
[L800] [34:20.56] then you're going to run Python, that
[L801] [34:22.96] Python can do whatever it wants to do
[L802] [34:27.68] in your program. There is no way to
[L803] [34:29.40] protect. So, if you gave that to the
[L804] [34:32.16] user, the user could do whatever it
[L805] [34:34.48] wanted to do.
[L806] [34:36.60] I mean
[L807] [34:37.72] for the program. And so, the program
[L808] [34:39.36] would break a lot of invariants of a lot
[L809] [34:41.76] of important stuff in the files it kept,
[L810] [34:44.04] etc. And so, what they did, they gave
[L811] [34:47.76] the thinking Lua because as I said, as
[L812] [34:50.08] Lua you create a state. For instance, as
[L813] [34:52.72] I just mentioned, you can only call C
[L814] [34:55.68] functions.
[L815] [34:57.32] That's is true in Python again, but the
[L816] [35:00.00] particularity You can only call C
[L817] [35:03.04] functions if you give the C pointer
[L818] [35:06.16] to Lua.
[L819] [35:07.40] So, have a very strict or any there
[L820] [35:10.00] there is very little as I said, there is
[L821] [35:12.00] a library. When you create a Lua state,
[L822] [35:14.44] it has
[L823] [35:15.72] no functions at all.
[L824] [35:18.28] There is nothing. I mean, you cannot
[L825] [35:19.80] open files. Everything there are we call
[L826] [35:22.96] standard libraries. Usually, you open
[L827] [35:26.68] a state and you register those standard
[L828] [35:29.84] libraries in Lua. So, you have the the
[L829] [35:32.52] minimum like you have mathematical
[L830] [35:34.44] functions, etc. But you can open a state
[L831] [35:37.12] and has no functions at all in Lua.
[L832] [35:40.84] It can only do things calling those
[L833] [35:43.32] specific functions you you you gave. So,
[L834] [35:46.84] they they used Lua to have this kind of
[L835] [35:49.16] control. You can write Lua code here,
[L836] [35:51.76] but that Lua code can only do very
[L837] [35:54.32] specific things in the Python program.
[L838] [35:57.44] You cannot call any Python function or I
[L839] [36:01.36] mean, build any kind of Python data
[L840] [36:03.76] structure, etc. So, was this a a nice
[L841] [36:07.16] example. In the case of hardware, it's
[L842] [36:09.40] the same thing. You cannot just go in
[L843] [36:12.44] the For instance, there is a a port a
[L844] [36:15.16] hardware port that controls the speed of
[L845] [36:18.32] the fan
[L846] [36:19.72] that that keeps the temperature of the
[L847] [36:22.04] CPU. And if you put that very low, you
[L848] [36:25.32] can really burn the CPU. I mean, because
[L849] [36:27.84] the CPU gets very hot. And so, we've you
[L850] [36:30.60] have a seat you cannot call C directly.
[L851] [36:33.32] You must call Bingo, and only Lua has
[L852] [36:36.40] access to that. So, if you can only
[L853] [36:39.00] program in Lua, it's a doll Lua, then
[L854] [36:41.24] you you check whether the the numbers
[L855] [36:44.36] you are giving are are precise or
[L856] [36:46.92] whatever it has to check, and then it
[L857] [36:49.84] calls
[L858] [36:51.12] >> It's kind of like a sandbox environment.
[L859] [36:53.56] >> Yes, exactly. Yes, sandbox is the exact
[L860] [36:57.36] word for that.
[L861] [36:58.84] >> I saw there's this, I guess, paper,
[L862] [37:01.20] maybe it was a
[L863] [37:02.92] article you wrote on the history of Lua
[L864] [37:05.28] with several other people, and I thought
[L865] [37:07.48] there were some interesting quotes in
[L866] [37:08.80] there I kind of wanted to ask you about.
[L867] [37:10.40] So, um one of them
[L868] [37:13.40] it says that there's this old joke that
[L869] [37:16.20] says that a camel is a horse designed by
[L870] [37:19.16] a committee.
[L871] [37:20.28] >> Yes, that's not mine. That's a real
[L872] [37:24.16] old joke.
[L873] [37:25.92] >> Does that mean that you think the best
[L874] [37:28.32] programming languages are designed by as
[L875] [37:31.16] few people as possible?
[L876] [37:33.04] >> Yes, I do think. Yes.
[L877] [37:35.40] Because there's one thing that that it's
[L878] [37:38.52] easy to to observe it it's is is this.
[L879] [37:41.76] If you have a committee
[L880] [37:44.00] writing a language,
[L881] [37:46.48] everyone wants to put something
[L882] [37:50.60] from themselves into the language. So,
[L883] [37:53.76] you have that your favorite mechanism,
[L884] [37:56.84] and you will fight whatever it takes to
[L885] [37:59.72] put your favorite mechanism into the
[L886] [38:02.32] language. And very few people will fight
[L887] [38:06.84] against
[L888] [38:08.40] putting anything in the language.
[L889] [38:11.48] I mean, some people say, "Oh, no, this
[L890] [38:13.40] is too much. This is too complicated."
[L891] [38:15.24] But people fight much more fiercely for
[L892] [38:19.52] to for put something they you in the
[L893] [38:21.84] language, then
[L894] [38:23.44] against putting something in the
[L895] [38:25.60] language. So, when you have a committee,
[L896] [38:28.32] the the tendency is so let's
[L897] [38:30.96] keep adding stuff to let's keep adding
[L898] [38:33.28] stuff, and people sometimes even do not
[L899] [38:36.04] understand. I mean, they were not sure
[L900] [38:37.84] if everybody there is really
[L901] [38:40.92] know the language
[L902] [38:43.04] well. Oh, well, I'm not putting that,
[L903] [38:45.00] but that fits with all the parts of the
[L904] [38:47.36] Oh, I didn't even know the language has
[L905] [38:49.12] this other part. I mean, so
[L906] [38:51.68] things sometimes do not fit together
[L907] [38:53.96] very well, etc. So, first you have a
[L908] [38:56.76] what's called a conceptual integrity.
[L909] [38:59.92] It's a name that give that everything
[L910] [39:02.12] fits together, everything
[L911] [39:04.88] it's designed if
[L912] [39:07.00] everything else in mind, etc. It's much
[L913] [39:09.84] easier to Yeah, I'm not saying I mean,
[L914] [39:11.76] Lua has several
[L915] [39:14.08] wrong stuff regarding because of with
[L916] [39:17.48] time, etc. There you make mistakes, but
[L917] [39:20.88] it's much easier to get things
[L918] [39:24.08] right if you have a small group of
[L919] [39:27.08] people that everybody knows what
[L920] [39:29.16] everybody else is thinking. I mean, you
[L921] [39:32.04] are deciding whether to put something in
[L922] [39:34.36] the language or not. It's much easier to
[L923] [39:37.36] change your mind
[L924] [39:39.44] if you do not put something, and then
[L925] [39:41.88] later you decide to add it to the
[L926] [39:44.72] language, than to add something, and
[L927] [39:47.44] then later you decide, "Oh, I shouldn't
[L928] [39:49.92] have
[L929] [39:51.16] that was not a good idea." So, when in
[L930] [39:54.28] doubt, our default is always don't put
[L931] [39:57.76] it. If you're not very sure, don't put
[L932] [40:00.36] it. We can always add that later, and so
[L933] [40:03.76] keep the door open through to
[L934] [40:06.80] change your mind.
[L935] [40:08.72] >> I saw in the original Lua programming
[L936] [40:11.16] language that there was no Boolean type,
[L937] [40:13.20] and I've never seen that before. Why was
[L938] [40:16.76] there no Boolean in the original Lua?
[L939] [40:19.56] >> Well, C doesn't have Booleans.
[L940] [40:22.32] I mean, the the the the original C and
[L941] [40:24.56] C90 up to C99
[L942] [40:28.32] using integers. If it's zero, it's
[L943] [40:30.68] false. If it's different from zero, it's
[L944] [40:33.64] true. And
[L945] [40:36.20] and people lived quite well with
[L946] [40:39.08] with that Lisp. I mean, there are
[L947] [40:41.60] several languages that don't have
[L948] [40:43.48] Booleans. And actually, we only put
[L949] [40:46.96] Booleans in Lua
[L950] [40:48.88] because we wanted false. True is
[L951] [40:51.72] completely useless in Lua. Nobody used
[L952] [40:54.20] true. And nobody such a joke, but it's
[L953] [40:56.64] too strong, but
[L954] [40:58.28] it's it's not very useful. You can use
[L955] [41:01.56] almost any other value for true.
[L956] [41:04.20] But the the the the the problem is that
[L957] [41:05.92] the in Lua the the
[L958] [41:08.40] nil, that special value nil,
[L959] [41:12.68] is in a table. It is equivalent to the
[L960] [41:16.44] key not being present.
[L961] [41:20.16] You all think better that was a good
[L962] [41:22.08] that
[L963] [41:23.04] decision, but it's very embedded in the
[L964] [41:26.52] design of the language. And it has with
[L965] [41:28.88] this strong concept that a table
[L966] [41:32.36] a key that is not present in
[L967] [41:35.20] in a table that is an associative array,
[L968] [41:38.24] it has a nil value. It's completely
[L969] [41:40.52] indistinguishable
[L970] [41:42.48] whether it's absent. I mean, absent
[L971] [41:44.80] means it has a nil value. Nil valent
[L972] [41:47.36] means it's absent. And so, sometimes you
[L973] [41:50.40] want to have a false value. And but you
[L974] [41:53.56] want to know what it is there in the
[L975] [41:55.84] table. And so, we needed a false. To
[L976] [41:58.92] have a false, you can put in the table
[L977] [42:01.80] and it's completely different from being
[L978] [42:04.20] absent. You know, there is a key and the
[L979] [42:07.12] key has a false value. So, we needed a a
[L980] [42:11.72] value. And if you're going to have a
[L981] [42:13.32] false, then
[L982] [42:15.24] we added true to maybe it would make
[L983] [42:17.84] sense to have false without true, but
[L984] [42:19.76] with true it's almost useless.
[L985] [42:22.76] >> Why not use zero as false if you're okay
[L986] [42:25.48] with one as true?
[L987] [42:27.16] >> It could be we could have used it, but
[L988] [42:29.40] that
[L989] [42:30.64] Among other things, that would be a a
[L990] [42:33.04] big change because exactly it didn't was
[L991] [42:36.20] that way, so we we added that late here
[L992] [42:40.16] in the language, so changing zero to
[L993] [42:42.64] false would be a very big
[L994] [42:45.24] incompatibility.
[L995] [42:47.56] But it could be for instance in in in
[L996] [42:50.12] Python, I think a lot of stuff are are
[L997] [42:53.80] false. I mean, zero is false, empty list
[L998] [42:56.68] is false, empty In JavaScript, I think
[L999] [42:59.52] it's even worse. I I don't re-
[L1000] [43:02.12] don't recall exactly, but I mean
[L1001] [43:05.24] This is kind of arbitrary. I mean, you
[L1002] [43:07.84] we could have for instance
[L1003] [43:10.36] nil, false, zero, empty string. I mean,
[L1004] [43:14.20] it
[L1005] [43:14.96] It just depends the kind of test that
[L1006] [43:17.12] you use.
[L1007] [43:18.48] It's not
[L1008] [43:19.76] In dynamic languages, it's very easy.
[L1009] [43:22.56] >> Python has the like you're describing
[L1010] [43:24.76] the truthy values and the falsy values,
[L1011] [43:28.24] or I guess they can be interpreted as
[L1012] [43:30.32] false. And but it's it's more implicit,
[L1013] [43:34.36] less explicit, and I know JavaScript is
[L1014] [43:37.44] even further on that spectrum where you
[L1015] [43:39.56] can do some really weird stuff that
[L1016] [43:41.68] implicitly has some behavior. Do you
[L1017] [43:44.48] think that design direction is good or
[L1018] [43:47.76] bad?
[L1019] [43:48.72] >> It's like a small compact, it's more
[L1020] [43:52.24] easy to write stuff. And but you always
[L1021] [43:55.24] have this balance in any language is
[L1022] [43:57.16] almost anything. The more flexible you
[L1023] [44:00.32] you
[L1024] [44:01.04] the more flexibility you have,
[L1025] [44:03.56] the less
[L1026] [44:05.92] protection you have. In C, you have
[L1027] [44:08.40] something like like that. People do not
[L1028] [44:10.60] notice, but
[L1029] [44:12.12] because C's typed.
[L1030] [44:14.16] But, you can check whether an integer
[L1031] [44:17.80] is true or false.
[L1032] [44:19.48] You can check whether a float
[L1033] [44:21.88] is true or false directly because again
[L1034] [44:24.28] it checks whether the float is zero or
[L1035] [44:26.72] different from zero. You can check
[L1036] [44:29.12] whether a pointer is nil or different
[L1037] [44:32.96] from nil because in C nil is a magic
[L1038] [44:36.48] zero.
[L1039] [44:37.52] So, it's kind of if you do not write any
[L1040] [44:40.56] test, it has an implicit test like
[L1041] [44:43.28] different from zero.
[L1042] [44:45.00] And this zero can be a integer, can be a
[L1043] [44:48.88] float, can be a pointer. So, in C also
[L1044] [44:52.20] you have this kind of
[L1045] [44:53.88] flexibility. It's just that you have to
[L1046] [44:56.44] be more explicit usually.
[L1047] [44:59.28] This
[L1048] [45:00.08] avoids errors, but
[L1049] [45:02.08] so this you have always this balance
[L1050] [45:04.16] between
[L1051] [45:05.96] easy to write and
[L1052] [45:07.92] easy to make mistakes.
[L1053] [45:10.08] >> I saw that
[L1054] [45:11.76] Lua is one indexed instead of zero
[L1055] [45:14.44] indexed, and I I had never seen a
[L1056] [45:17.16] programming language like that in my
[L1057] [45:18.88] experience.
[L1058] [45:20.16] >> There was a lot of programming languages
[L1059] [45:22.64] like that.
[L1060] [45:23.92] >> So, yeah, why why is it one indexed?
[L1061] [45:26.68] >> Because everything in the real world are
[L1062] [45:29.60] one indexed. If you have a book, you
[L1063] [45:31.88] have the the chapter one, chapter two.
[L1064] [45:34.52] Nobody number chapters as zero, one,
[L1065] [45:37.80] two, three. Only program- programmers
[L1066] [45:40.48] are the only Even mathematicians, if you
[L1067] [45:43.16] get a mathematic book, a book of
[L1068] [45:45.52] mathematic, any sequence, it's A1 and
[L1069] [45:49.04] A2, A3. If you get a matrix, the first
[L1070] [45:52.68] element is A11, A12, and then A
[L1071] [45:56.52] Everything
[L1072] [45:57.92] is written with a Only
[L1073] [46:00.52] in programming language that is this of
[L1074] [46:02.68] zero.
[L1075] [46:03.64] And the funniest part is that for
[L1076] [46:06.12] instance Fortran
[L1077] [46:07.88] that now it's it's very old language,
[L1078] [46:10.04] but to index it from one. In Pascal you
[L1079] [46:13.40] can choose I mean you write an array,
[L1080] [46:16.40] you can say this array means index it
[L1081] [46:18.44] from minus five to five. And so it's
[L1082] [46:22.08] it's index it from whatever value you
[L1083] [46:24.24] want to whatever value
[L1084] [46:26.68] you want.
[L1085] [46:28.40] Zero became
[L1086] [46:30.64] extremely popular
[L1087] [46:33.16] because of C.
[L1088] [46:35.08] C uses zero and a lot of languages copy
[L1089] [46:39.80] kind of inspired by by by C. They have
[L1090] [46:42.80] the same operators, the same syntax for
[L1091] [46:45.72] expressions.
[L1092] [46:47.36] The Boolean
[L1093] [46:48.88] operators for instance that is not
[L1094] [46:51.20] standard mathematics. Almost all
[L1095] [46:53.72] languages chose the same operator A to Z
[L1096] [46:57.92] they are written in C.
[L1097] [47:00.68] And so a lot of language copied C and
[L1098] [47:03.24] then zero index it became very popular.
[L1099] [47:07.32] And what is funny
[L1100] [47:09.48] is that in C there is no indexing. In C
[L1101] [47:13.08] indexing is just an illusion
[L1102] [47:15.96] because what you have is pointer
[L1103] [47:17.72] arithmetic.
[L1104] [47:20.80] And C when you write A index it by I
[L1105] [47:23.68] actually what you are saying get the
[L1106] [47:25.84] contents of A plus Y.
[L1107] [47:29.72] And so because in C you don't have
[L1108] [47:32.80] indexing, you have
[L1109] [47:34.84] this
[L1110] [47:36.44] displacements or deltas I don't know how
[L1111] [47:38.96] offsets.
[L1112] [47:40.24] Then it must have index it by zero
[L1113] [47:42.68] because of that because then the first
[L1114] [47:45.00] element is the element that is at the
[L1115] [47:46.92] the original address. So
[L1116] [47:50.16] C doesn't have index indexing. So when
[L1117] [47:53.40] you say A is index by zero, it doesn't
[L1118] [47:56.24] index by zero because it doesn't index
[L1119] [47:58.44] by anything. But it it have this
[L1120] [48:01.00] illusion of indexing and then it's easy
[L1121] [48:03.96] to think that it
[L1122] [48:05.36] And then a lot of language that do not
