Chunk 2; segments 340–670. Start may repeat the previous chunk for context.

# Creator of Scala: Comparing Languages And How AI Will Impact Them | Martin Odersky

Source ID: source-5f7cf6e81e665bd5
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_Scala_Comparing_Languages_And_How_AI_Will_Impact_Them_Martin_Odersky_en.txt
Video: https://www.youtube.com/watch?v=LdN4sPWM-WY

[L349] [13:34.88] doesn't have and that is that um there
[L350] [13:38.16] cannot be additional type errors after
[L351] [13:40.48] inlining. So the thing is you inline and
[L352] [13:43.12] then the question is is the inline
[L353] [13:44.72] program guaranteed correct uh so type
[L354] [13:47.84] correct or might you have type errors?
[L355] [13:50.40] The typical example where you might have
[L356] [13:52.40] type errors is C++ templates. In fact,
[L357] [13:55.36] that's quite quite scary in C++ that you
[L358] [13:58.16] can expand a template and then you get
[L359] [14:00.64] very very complex type errors and very
[L360] [14:03.20] very hard to to to debug things. So, ZIK
[L361] [14:06.08] is I believe is much better because the
[L362] [14:07.84] the inlining mechanism is much ser.
[L363] [14:10.56] >> When you say inlining, can you explain
[L364] [14:12.56] the concept? Inlining just means that uh
[L365] [14:15.52] in in Scala we can write inline in front
[L366] [14:18.24] of a of a function and that means that
[L367] [14:21.28] the compiler will uh before it starts
[L368] [14:25.20] code generating. So during the time when
[L369] [14:28.08] it looks at the type code which are
[L370] [14:30.00] trees it will take the function body
[L371] [14:33.20] when it sees a function call to that
[L372] [14:34.88] function it will take the call and
[L373] [14:36.72] replace it by the body and then it will
[L374] [14:39.12] do some optimizations. it can say okay
[L375] [14:41.36] so here we have essentially an app an
[L376] [14:44.24] application to let's say a value which
[L377] [14:47.44] is a lambda and but I know where the
[L378] [14:49.44] lambda points to so let me forward the
[L379] [14:51.68] call right to the function uh so and and
[L380] [14:54.72] with that you can already do quite a bit
[L381] [14:57.68] of uh essentially optimizations which
[L382] [15:00.40] are guaranteed because the the inliner
[L383] [15:03.92] must inline that's that's not a thing
[L384] [15:06.56] like an optimizer has essentially
[L385] [15:08.80] discretion whether they want to inline
[L386] [15:10.48] things or not and so you can never rely
[L387] [15:12.56] on that but an an inliner which is uh
[L388] [15:15.60] essentially a compile time based on the
[L389] [15:18.16] typer must inline so you can rely on it
[L390] [15:21.04] and const explore by in in zik and C++
[L391] [15:24.08] is essentially very similar
[L392] [15:26.16] >> okay so it's a way to get rid of the
[L393] [15:28.48] function call or the overhead of a
[L394] [15:30.32] function call and tell the compiler you
[L395] [15:33.92] can do more because it's all I guess
[L396] [15:36.72] inline
[L397] [15:37.60] >> yeah you reveal the implementation and
[L398] [15:39.60] That means you you can you can uh the
[L399] [15:43.12] compiler can do something with that.
[L400] [15:45.12] >> When you think about all the dynamically
[L401] [15:46.80] typed languages, um which one stands out
[L402] [15:50.24] as one that you think is kind of the
[L403] [15:52.48] best among them?
[L404] [15:53.68] >> Python is ubiquitous. Um and it has a
[L405] [15:58.08] nice syntax. It uh a lot of the Python
[L406] [16:01.60] programs look like they're very easy to
[L407] [16:04.00] read. So that's definitely an advantage.
[L408] [16:06.88] and and the other one would probably be
[L409] [16:09.76] something like scheme uh which is sort
[L410] [16:12.32] of very grounded in computer science
[L411] [16:14.72] theory and lambda calculus and things
[L412] [16:16.80] like that. So both of them are sort of
[L413] [16:19.20] interesting in their own way but of
[L414] [16:20.72] course Python is 100 times more popular.
[L415] [16:23.76] >> If you compare Scola to Python for
[L416] [16:26.48] instance I guess what are the trade-offs
[L417] [16:28.40] that the two languages took? I think the
[L418] [16:31.36] gap is closing because Python now
[L419] [16:34.00] actually has an optional type syntax and
[L420] [16:37.60] a number of type checkers that check
[L421] [16:39.36] that syntax in Python is getting some of
[L422] [16:42.40] the features that Scala had since the
[L423] [16:44.16] beginning like pattern matching is in
[L424] [16:46.08] one of the the recent Pythons. So I
[L425] [16:48.64] think actually the gap is closing not
[L426] [16:50.40] just between Python and Scala but but
[L427] [16:52.24] between a lot of programming languages
[L428] [16:53.76] in general there sort of all drift to a
[L429] [16:57.44] standard set of features which mostly
[L430] [16:59.84] come from functional programming
[L431] [17:01.20] actually pattern matching for instance
[L432] [17:03.52] strong type systems uh generics
[L433] [17:06.16] polymorphism all these things came from
[L434] [17:09.04] closures all these things came from
[L435] [17:10.64] functional programming and so the gap is
[L436] [17:13.44] closing in that in that sense um Python
[L437] [17:17.52] is um I think the main advantage of
[L438] [17:21.36] Scala over Python is that it is it has a
[L439] [17:24.80] strong type system that is always on and
[L440] [17:27.84] that gives you essentially guarantees uh
[L441] [17:30.24] that essentially certain bad states
[L442] [17:32.64] can't can't can't happen. So, so you
[L443] [17:34.64] really can rely on it. Whereas I think I
[L444] [17:37.20] believe the Python type system, well,
[L445] [17:39.12] it's just syntax. It has a number of
[L446] [17:40.88] type checkers, but in general there's
[L447] [17:44.08] there's le you you have fewer guarantees
[L448] [17:47.12] and I believe it's also the ecosystem
[L449] [17:48.96] and culture that doesn't value types as
[L450] [17:51.28] much in Python. So, I think that's
[L451] [17:52.80] probably the main difference.
[L452] [17:54.80] Fantactically, the two languages I think
[L453] [17:57.12] with Scala 3 are actually also quite
[L454] [17:58.88] close. So, Scala 3 looks a lot like
[L455] [18:01.20] Python. Um, in that sense, uh, you could
[L456] [18:05.04] say well can see it as a
[L457] [18:08.80] as a language that has strong types and,
[L458] [18:12.48] uh, runs on on different runtimes than
[L459] [18:14.88] Python. Or I should say the other thing
[L460] [18:16.80] with Python which is really great is
[L461] [18:18.48] that Python is a fantastic glue language
[L462] [18:20.72] because I can essentially have very very
[L463] [18:23.20] efficient linkages to to high
[L464] [18:25.20] performance C++ libraries. uh uh pandas
[L465] [18:29.52] or numpy or things like that.
[L466] [18:32.00] >> You mentioned that a lot of the
[L467] [18:33.28] programming languages they're kind of uh
[L468] [18:35.52] drifting or kind of being inspired by
[L469] [18:38.24] the other ones and you know adopting new
[L470] [18:40.40] features in the design of Scola. Is
[L471] [18:42.80] there a programming language that you
[L472] [18:44.96] admire most and influences Scola the
[L473] [18:47.84] most? Historically, Scala was
[L474] [18:51.36] essentially you could say it was a blend
[L475] [18:53.28] of Java,
[L476] [18:55.20] Okamel and or standard ML which is close
[L477] [18:58.88] an [snorts] MLike language and and
[L478] [19:00.80] Haskell. Uh so I I I I'm by trade well
[L479] [19:05.44] I'm by trade an imperative program. My
[L480] [19:07.52] PhD is from Nicholas W. So I know
[L481] [19:09.44] Pascal, modular that was sort of my
[L482] [19:11.76] first generation of languages and I
[L483] [19:13.44] liked them a lot and then I became sort
[L484] [19:16.08] of a converted functional programmer. So
[L485] [19:18.48] I I looked very closely at ML, Okl,
[L486] [19:21.44] Haskell and these things and then um the
[L487] [19:25.84] Scala came about sort of there was a
[L488] [19:27.76] predecessor language called pizza and I
[L489] [19:30.32] was working on that with Phil Wadler
[L490] [19:31.92] who's one of the Haskell original
[L491] [19:33.84] designers and the idea was to have
[L492] [19:36.24] essentially an accessible functional
[L493] [19:38.16] language on a very widespread platform
[L494] [19:40.56] which was a JVM at that at that point
[L495] [19:43.92] and um the uh in order to prepare for
[L496] [19:48.40] that I wrote a Java compiler. So that's
[L497] [19:51.36] how I learned a lot about Java and what
[L498] [19:53.20] Java was. And in the end I I had had to
[L499] [19:56.72] say well it's actually quite useful. I I
[L500] [19:58.96] I was quite dismissive at first but
[L501] [20:01.76] afterwards I found it actually quite
[L502] [20:04.00] useful. I mean this was very early Java.
[L503] [20:06.08] This was Java even pre 1.0. So so now
[L504] [20:08.96] Java is is of course even more useful
[L505] [20:11.36] but also a lot bigger than what it was
[L506] [20:13.68] at the time. Um so when we came up with
[L507] [20:17.68] with Scala which was sort of the second
[L508] [20:19.44] iteration after pizza, pizza was the
[L509] [20:21.44] language I did with Phil water. Uh the
[L510] [20:24.80] the
[L511] [20:26.56] ideas came mostly from Java uh Okamel
[L512] [20:30.48] for the modules and the component module
[L513] [20:33.92] and Haskell a lot for the standard
[L514] [20:36.48] libraries. So if you look at the
[L515] [20:38.16] function names of the in the Scala
[L516] [20:40.00] standard library then there's sort of a
[L517] [20:41.84] mixture of Okamel and Haskell you could
[L518] [20:43.76] say but you you recognize a lot of
[L519] [20:45.44] things coming from both of these these
[L520] [20:47.68] languages
[L521] [20:48.72] >> if I recall correctly uh Java was had
[L522] [20:52.64] some sort of licensing with it or was
[L523] [20:54.72] owned by a company. Um how were you able
[L524] [20:58.08] to build on top of Java or did you have
[L525] [21:01.44] to pay for licenses or how how' that
[L526] [21:04.00] ecosystem work? the language standard
[L527] [21:06.48] was open source. Um there were there was
[L528] [21:09.20] a lot of experimentation with Java at
[L529] [21:11.12] the time. Um I think the only thing that
[L530] [21:15.84] Sun was that was the company at the time
[L531] [21:18.48] they're very particular about is that
[L532] [21:20.24] you absolutely if you did something that
[L533] [21:23.44] was using Java and had Java in it you
[L534] [21:25.92] had to call it Java and and and you
[L535] [21:28.88] couldn't have a different name. So
[L536] [21:30.40] that's why initially for instance
[L537] [21:32.24] Microsoft clashed with them. Uh and then
[L538] [21:35.52] Microsoft went went went away and and
[L539] [21:38.00] designed C which was sort of a a Java on
[L540] [21:41.52] some steroids. They they threw in a bit
[L541] [21:44.24] more than what Java had at the time. U
[L542] [21:47.84] the I think the nastiness came Sun was
[L543] [21:50.16] actually quite an open company. Uh so at
[L544] [21:53.04] the time we no we were not worried about
[L545] [21:55.20] that. So that was in the time frame from
[L546] [21:57.12] 1998 to 2004 2005 something like that.
[L547] [22:03.20] Uh and at the time there was no issue. I
[L548] [22:05.28] think the issue came later when Sun was
[L549] [22:07.76] acquired by Oracle and Google forked
[L550] [22:10.32] Scala on Android Java on Android and
[L551] [22:13.04] that's when the fight started but that
[L552] [22:14.80] was much later. So uh when you say that
[L553] [22:17.52] Scola was using the JVM or built on top
[L554] [22:20.32] of it um like concretely in the the tech
[L555] [22:23.76] stack what does it mean that Scola uses
[L556] [22:26.00] the JVM like how does Java source code
[L557] [22:29.84] eventually execute on a machine?
[L558] [22:32.16] >> So the JVM is u essentially defined by
[L559] [22:36.00] its bite code. So the bite code is
[L560] [22:38.16] essentially an intermediate format which
[L561] [22:40.24] you can translate your program into and
[L562] [22:43.68] then the the bite code is run first by
[L563] [22:46.16] an interpreter and then essentially by
[L564] [22:48.72] an optimized compiler just just in time
[L565] [22:51.20] compiler JIT so that's called JIT they
[L566] [22:53.76] they they do that and
[L567] [22:57.60] so if you can if you know how to uh
[L568] [23:01.60] output bite code and that's not very
[L569] [23:04.00] hard then you can run on the JVM so So
[L570] [23:06.72] that's essentially the the idea. The
[L571] [23:09.04] harder part then is interrupt that you
[L572] [23:11.20] say okay I run on the JVM. I have to
[L573] [23:13.60] make sense of all these Java libraries
[L574] [23:15.36] out there. So I have to somehow map a
[L575] [23:18.00] Java concept into a Scala concept
[L576] [23:21.06] [snorts] so that the compiler can
[L577] [23:22.40] understand what it is and I can document
[L578] [23:24.72] what it is in for Scala programmers that
[L579] [23:27.36] maybe don't understand much Java. So so
[L580] [23:29.52] that that is sort of a work that is sort
[L581] [23:32.88] of goes more into the details. That
[L582] [23:35.60] said, I mean that's not the only uh
[L583] [23:38.40] Scala platform. So it was born on the
[L584] [23:40.24] JVM, but now it also exists uh on on
[L585] [23:43.52] JavaScript and NodeJS uh on WAM and and
[L586] [23:47.04] on native. So it's really a
[L587] [23:48.32] multiplatform language. OpenAI, [snorts]
[L588] [23:51.36] Enthropic, Cursor, and Verscell all use
[L589] [23:54.72] this product to make their lives better.
[L590] [23:56.80] And the problem it solves is when you're
[L591] [23:58.96] building SAS or an AI product and you
[L592] [24:01.52] want to sell to other companies, there's
[L593] [24:03.36] all these requirements you need to meet.
[L594] [24:05.52] There's SSO, there's SKIM, there's
[L595] [24:08.00] arbback, there's audit logs. These are
[L596] [24:10.48] all things that take time to integrate
[L597] [24:12.48] but aren't the main focus of your app.
[L598] [24:14.64] Work OS is an API layer that lets you
[L599] [24:16.72] meet all of these requirements in just a
[L600] [24:19.04] few lines of code. So, let's say you
[L601] [24:20.88] have a new SAS product and you want to
[L602] [24:22.80] sell to other companies. Work OS will
[L603] [24:25.04] solve all of these critical feature gaps
[L604] [24:26.96] for you. You can check them out at
[L605] [24:29.44] workos.com to learn more and get
[L606] [24:31.84] started. And I appreciate them for
[L607] [24:33.92] supporting my work and sponsoring this
[L608] [24:35.68] podcast. Jira bytassian isn't just for
[L609] [24:38.88] tracking work anymore. Now you can pick
[L610] [24:40.80] your favorite AI agent to assign tasks
[L611] [24:43.04] to and they'll get access to the rich
[L612] [24:45.12] context that's already in Jira. When the
[L613] [24:47.68] agent is done, it surfaces pull request.
[L614] [24:50.16] That way you can get more done with your
[L615] [24:52.08] favorite agents all in one place. Learn
[L616] [24:54.56] more at jira.dev. That's jir.dev.
[L617] [25:00.00] Appreciate them for sponsoring the
[L618] [25:01.44] podcast. And back to the show. Let's say
[L619] [25:04.00] I write a Scola program. Uh I have the
[L620] [25:06.80] source code. I have to compile it and
[L621] [25:09.44] then I have some Java bite code and then
[L622] [25:13.28] I call I don't know JVM and I pass in
[L623] [25:16.88] this bite code and it just works.
[L624] [25:19.12] >> Yeah. Yeah, exactly. Yeah.
[L625] [25:20.96] >> What would the advantage be of compiling
[L626] [25:23.44] Scola to Java byte code instead of doing
[L627] [25:27.36] something like C and C++ where you
[L628] [25:29.44] compile it all the way to machine code
[L629] [25:32.24] from source?
[L630] [25:33.76] >> We we have that too. And so the Scala
[L631] [25:36.00] native compiles directly using LLVM to
[L632] [25:39.20] to native code. Um the advantages of um
[L633] [25:44.32] compiling to bite code is essentially
[L634] [25:47.20] again the interrupt can use all the Java
[L635] [25:49.44] libraries. Then uh the the garbage
[L636] [25:52.48] collectors. So the the JVM has actually
[L637] [25:54.80] very good garbage collectors, high
[L638] [25:56.40] performance ones. Um and um and the
[L639] [26:00.40] runtime loading. So, so what what I can
[L640] [26:03.92] do on the JVM is I can compile let's say
[L641] [26:07.04] a oneline thing into a little Java bite
[L642] [26:09.76] code and I can immediately load that by
[L643] [26:11.68] code and execute that and that makes it
[L644] [26:13.92] very easy for instance to have a ripple
[L645] [26:16.24] because that's how how how a ripple
[L646] [26:18.56] would work a redevelop print loop so I
[L647] [26:20.64] would just generate a snippet of Scala
[L648] [26:23.04] code to bite code load it into the
[L649] [26:25.20] running JVM process and it gets executed
[L650] [26:28.08] and that's much harder if you go to
[L651] [26:29.76] binaries basically the binary ers don't
[L652] [26:31.52] really have a concept for that.
[L653] [26:33.60] >> You mentioned that you wrote a compiler
[L654] [26:36.08] for Java like before Scola and I I've
[L655] [26:38.96] heard that compilers are notoriously
[L656] [26:41.20] hard to build. Um can you explain the
[L657] [26:43.84] hard parts and why they're hard?
[L658] [26:46.56] >> Compilers are
[L659] [26:49.68] very intricate. Um because uh I think
[L660] [26:53.60] there there a lot of requirements on a
[L661] [26:56.24] compiler. So you have languages which
[L662] [26:58.96] are already complex artifacts. Uh then
[L663] [27:02.72] you have a thing called type inference.
[L664] [27:04.80] So you have a type system but
[L665] [27:06.56] essentially you demand the compiler to
[L666] [27:10.24] essentially infer a lot of types that
[L667] [27:12.88] make sense because you as a programmer
[L668] [27:14.72] thinks well the compiler should know
[L669] [27:16.08] that and it should uh but actually to
[L670] [27:19.04] for the compiler to do that is is quite
[L671] [27:21.20] hard. And then then you of course you
[L672] [27:23.04] also demand that it would would would
[L673] [27:25.20] generate very efficient code for your
[L674] [27:27.12] program because again the compiler
[L675] [27:29.04] should know that right so there's a lot
[L676] [27:30.88] of demands on that plus there's a demand
[L677] [27:33.52] that it should should be very very fast
[L678] [27:35.76] uh and to square all these demands
[L679] [27:38.88] requires quite a bit of work basically
