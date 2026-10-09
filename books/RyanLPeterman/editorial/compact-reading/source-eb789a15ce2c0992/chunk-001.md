# Creator of Lua: What People Get Wrong About Scripting Languages | Roberto Ierusalimschy
Source: source-eb789a15ce2c0992 | Chunk 1 of 5
Video: https://www.youtube.com/watch?v=jCZnFKk6M9A
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.00–00:03.08; L10–L11] It's completely feasible that you won't have programming languages.

[00:04.96–00:09.24; L12–L14] >> This is Roberto, the creator of the Lua programming language, and I asked him all about programming language design.

[00:11.60–00:26.24; L15–L21] >> C++ I think is a good example of a language that is really, really complex. And JavaScript I think it's even worse. I always joke that the JavaScript the good part here a very thin book comparatively official JavaScript book.

[00:28.36–00:31.92; L22–L24] >> Given how [snorts] much AI has been progressing, would you still recommend people learn computer science today?

[00:34.76–00:38.92; L25–L27] >> If you really think about that, it's really difficult to recommend people learning anything.

[00:41.32–01:05.96; L28–L36] >> Here's the full episode. In 2023, Lua was the second highest programming language by growth according to contributors on GitHub. And I saw that it was also used in famous games like World of Warcraft and Roblox. And so, I wanted to ask you what kind of programming language is Lua and what sets it apart?

[01:07.68–02:14.12; L37–L62] >> Lua is a language that you usually use together with combined it with another language like C or C++ and then you have an architecture where Lua takes care of the more dynamic part of your program, things that change more frequently, things that are are not so resource intensive, the the hard parts you have written in C or C++. So, it's typically what is called a scripting language. There is a some confusion I think between scripting languages and dynamic languages. And people just I think consider that a dynamic language to be more or less the same thing as a scripting language. And they are not exactly the same thing. So, for instance, a big difference between Lua and several other scripting languages is that for scripting, you have two typical uses. You can have the the the that I call who has the main loop. So, you can you can have the program written in C

[02:16.44–03:20.43; L63–L86] and calling Lua or you have your program written in Lua calling C. And for several called scripting languages are actually you you don't have to, but it's much more easy to use if you have your program written in the scripting language and C language is only for your libraries. And Lua is very good fit when you want the reverse. You want the the the the program written in C and then you you have calls Lua from time to time. So, the point is that Lua is very good at this that you have the the the main loop the the the program written in C and then it calls Lua for some tasks or for whatever you you you want to do. And for instance, in games, this is very important to keep the the frame ratio of the game. So, for instance, you have the loop the loop keeps the rhythm of [snorts] the game and keeps everything

[03:22.20–04:04.24; L87–L102] and then at every frame it calls Lua Lua's updates all characters all images everything in in the game and then it return to C to do the renderization etc. So, it is a very good fit. But, the main point is that that it people sometimes call this the embedding versus extending. So, you can extend the scripting language with C or you can then can embed the scripting language into C. And so may several languages are very good only for extending while Lua is really good for both embedding and extending.

[04:05.52–04:08.80; L103–L104] >> Why is Lua good for embedding and Python it's almost the opposite?

[04:10.72–04:48.44; L105–L118] >> Because in Lua since the beginning Lua was thought about Lua as a library. Since the beginning Lua was written as a library. So I think that's the the main difference. Lua has a standalone program that I mean you can call Lua in your console, in your common line, but that program is just a client of the official client of the library following the the same API that any other program can use. So this idea of language as a library, I think it's not very common. It's something that is very particular in Lua.

[04:49.12–04:54.96; L119–L121] >> When you design a language as a library, what are the unique, I guess, um, design decisions?

[04:56.28–06:02.76; L122–L148] >> I think that goes a lot of small small and big details. For instance, your your idea of what is your global space or your about scopes of variables, about exception handling. For instance, it's very important that it's very common in Lua that you raise an exception in Lua but catch the exception in C. So all these things about how you do exception handling in the language. Another It's not a big deal but it's a For instance, most dynamic languages, that's almost a definition of a dynamic language. They have an eval function that you can give a piece of code and then it executes that code. In Lua we don't instead of eval we have a function that we call the load. That you give a piece of code and it returns a function an internal function like it was a Lua function that when you call that function, then you execute the the associated code. It does doesn't

[06:07.16–07:05.04; L149–L171] execute immediately. So, you have this clear separation between compiling like the the Lua code that you have and then you can do that in C. So, in C, you can get a piece of Lua code, you can compile it, check if it has errors, etc. Then you call that for instance for instance a different piece or you can even call several times. For instance, you can load functions from Lua into C, you keep them I mean in the Lua space and then you can call that same function again and again. It's not a big difference, of course, because for if you have a value, you can evaluate a function declaration and then returns that function. So, you you can If you have a value, you can do load. If you have load, you can do eval. But I think load it's it's simpler to use for that kind of thing that is when you think about

[07:07.32–08:14.28; L172–L197] libraries for instance. In Lua, you it doesn't have a global state. I think that's a I forgot that that that's a very important difference. When C starts, the first thing it has to do is to call create a new Lua state. And then everything you do, you do on that state. And that state is completely independent of everything else. So, C can for instance create another Lua state and both states are completely independent, completely there is no communication between them. And so this again shows that the And so for instance, C can use a state to do a lot of stuff and then it can close the state and all memory used by Lua released everything that Lua was using is released. For instance, if C doesn't need to use Lua anymore for a program, you release all all resources used by Lua and your program in C continues and then later it can again create another state, etc. So

[08:18.64–08:33.96; L198–L204] there's as I said there is several small or not so small decisions in the language but all the time we think about the language as is that good for embedding? Is that possible to to do embedding and things like that?

[08:35.36–08:51.56; L205–L212] >> When you think of the programming community generally, everyone is quite familiar with Python but not as familiar with Lua. I thought it might be interesting to compare the two languages. So if you compared Lua to Python, what are the pros and cons of each language design?

[08:54.96–09:57.96; L213–L238] >> Lua is a language that is intended to be used in in this idea for of scripting architecture. So the Lua for instance, it doesn't try having a lot of different libraries. If you have something that oh I want to write a a quick program for something that Python is much better. It has all the libraries you can dream about it. It has a lot of libraries built-in already into the language. So that the language is huge. It's I mean the the installation it's it's a huge so the download etc. But it it has exactly oh I need that. Oh, it's there. I need that. It's there. And Lua is almost the opposite. Some very minimalistic language because they did that thing embed Lua into your program. It doesn't use almost any resources. Most of the libraries, the important libraries that you you will use will be provided by the program itself. It will be the commands like you move a

[09:59.56–10:14.76; L239–L245] character or do some speech or things like that from the engine of of the game for in for instance if you think about games, but whatever it is. So, Lua is I think that's the the main big difference. It's They they have very different goals.

[10:16.48–10:18.68; L246–L247] >> I saw some benchmarks and I saw that Lua is much faster than Python. Why is that?

[10:22.48–11:25.00; L248–L272] >> That that Those benchmarks are are not exactly, but I think that the main point is exactly One things that Lua does have these focus on on performance. Again, in the realm of scripting languages doesn't want to compete with C or C++. But in the realm of dynamic mostly now it's dynamic language, not scripting languages. We have some focus on performance. So, I think this is a a first difference. Python is exactly is much more I think that it's a a decision that they make. Performance is not that important. It's more important to be flexible, to be easy to do whatever you want to do. That in Lua sometimes we do not put some features because we think that there is no way to implement that efficiently. But also I think some part of that performance difference comes exactly because of the the size of Lua. So, most of the virtual machine fits in your cache for instance. I think there

[11:28.00–11:49.52; L273–L281] is these two big things. One is that Lua doesn't have so many features. It's not so dynamic as Python. So, in Python there is a lot of in the interactions because everything can mean something else. In Ruby, we are a little more conservative on that side. And but I think also this thing of being small also makes it naturally faster.

[11:52.96–12:09.60; L282–L289] >> So, on the distinction between scripting languages and dynamic or I guess it seems like dynamic language is a superset. Scripting language is a is a subset of that. Am I understanding that JavaScript is a dynamic language, not a scripting language from your perspective?

[12:10.72–13:00.84; L290–L309] >> Yes, exactly. Yes, exactly. Because the scripting it came the the the the the original scripting language it was bash or the shells from Unix. Of this idea that there's a language that coordinates other stuff. So, for instance, it can be extending again, you can use But the this idea that you have two different language for instance, in in the shell is only useful because you have a lot of programs written in C that are controlled by shell. So, the scripting language has this very strong idea that you have this idea of a dual language architecture. This is So, scripting means it's like it is it's the name scripting. It means you it's like a the you coordinator. You you give a script to be executed by those other other things.

[13:04.64–13:16.24; L310–L316] >> You gave a talk a while ago and someone asked you a question of, you know, what books do you recommend for, you know, studying programming languages? And you said actually that you enjoyed studying the language design of other programming languages.

[13:18.52–13:31.52; L317–L322] >> I like reading books that describe the design of of the languages. I I think the best books are those written by the author of a language about the design of that language.

[13:32.64–13:35.12; L323–L324] >> What book recommendation do you think is best on language design?

[13:37.32–13:51.40; L325–L331] >> JavaScript the good parts, for instance. The the the it's kind of old now, but I think that's I think it's a very interesting book. Although I always joke that the JavaScript the good part a very thin book comparatively.

[13:54.88–13:54.88; L332–L332] >> Official JavaScript books like

[13:57.56–14:17.44; L333–L341] >> one hand of the language is the good parts. But but I I think that book is really interesting like because exactly it it discussed the language it discusses in the bad parts and it focus on the good parts but then explains why it's there, why it it was made that way, etc. That is a book that I like.

[14:20.08–14:33.28; L342–L348] >> When we were talking about Lua, it sounds like one of the things that sets Lua apart is the performance and how minimal it is. And when I was reading about Lua, I saw that there's Lua Jit. How does the Lua Jit work?

[14:34.64–15:31.08; L349–L371] >> Lua Jit the first thing that's completely different project. It doesn't have anything to do with us. But it's a incredible piece of of software that is is a just-in-time compiler for Lua that's and I think exactly one of the reasons it works so well on top of Lua is because of the simplicity of Lua. It's a very regular language. I mean it has a very as I said it doesn't have many exceptions or too many indirections or things that so it's not that dynamic. I mean everything can mean something completely different. So that I think that gives a very good language for a Jit. But the the the the the Mike Paul is the name of the the the guy that made the the in the I think he's still working on that on the first legit. He's It's unbelievable his work.

[15:33.52–15:33.52; L372–L372] >> What makes writing a legit difficult?

[15:36.56–16:00.88; L373–L382] >> The first thing that for me I don't want to get involved with legit is because it's machine dependent. It's not very productive. I mean, you you do a lot of work and it only works on that architecture. And then I want to running another architecture. But, Mike Paul he created a kind of pseudo pseudo assembler that he writes in this assembly and then he translates
