# Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura
Source: source-70f1e2ca6c128ddc | Chunk 1 of 5
Video: https://www.youtube.com/watch?v=KzdYKeAqWhY
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.40–00:59.20; L10–L34] LLMs paired with the lean proof assistant have led to breakthroughs in competition math and more recently the verification of frontier math results. Lean is a critical part of this process because it helps validate the candidate proofs the LLM spits out. In this conversation, I asked the creator of LEAN about how it works [music] and how it will affect the future of math and software verification. Could that be the end of handwritten math? Here's the full episode. There's this famous Dysterra quote I want to start the conversation with. It's that, you know, program testing can be used to show the presence of bugs, but never to show their absence. And in my understanding is that lean and formalizing proofs can be used to show the absence of bugs. And so in your words, what is lean and how do people use it to show bugs can't occur in programs? L is a programming language. You can

[01:01.28–01:26.96; L35–L45] write code, but you can also write proofs. You can reason about your code. You can write state properties about your code and prove them. LIN gives you machine checkable proofs. You can check your proofs and get absolute assurance they are correct. You have uh many checkers, independent checkers. But you should view LIN as a platform. You can write code. You can write properties about your codes and you can prove them.

[01:30.56–01:40.96; L46–L50] >> So could you give a concrete example? Because when I think of a proof, I think of what I learned in math. But then how do you couple that with the software that we write?

[01:42.32–02:44.48; L51–L77] >> Yeah, it's a great question. It's not that different from math proof. L is actually very popular for math. But for for software verification, right? uh there are two very different use cases. You can reason about lin programs. LIN is a programming language. You can write programs in ling itself. Then a link program is not that different from a definition you have in math. The techniques are very similar. But when you if you want to verify programs written in a different programming language that basically two different approaches. One of them they translate it's called shallow embedding. They translate for rust. This happens today. We have a tool called that maps rust into ling and you can verify the ling translation right. uh and there's another technique called jeep badging where you have the semantics you you write a semantics of the programming language of C in ling and now you have a you have a data

[02:46.56–02:55.12; L78–L81] structure that represents a C program and you can state properties about it is almost like your programs become lean objects right that you can reason about

[02:58.40–03:08.32; L82–L86] >> to make it really concrete to give someone a sense of you know here's this thing I want to prove about a simple C program maybe like no buffer overrun or something like that.

[03:09.68–03:11.92; L87–L88] >> What's a step by step where we could use lean to prove that?

[03:13.84–04:00.00; L89–L105] >> Yeah. Yeah. Let's get array. You're trying to access an array in C. You want to make sure the index is in bounds. You're not accessing elements that your array for example has 10 elements. You're not trying to access elements 11. Right? uh basically can you can write that you can write in link that uh the value of i at this point in your program is going to be greater than or equal to zero and less than 10 right you you can write that as a mathematical statement right uh another way to view is that if you can express in math what you care about your program you can verify using l Right? That's another way to view it.

[04:02.32–04:10.64; L106–L109] >> So I have my my C source files and then somehow there's an equivalent lean proof that's almost like metadata on top of the C program.

[04:11.68–04:11.68; L110–L110] >> Yes.

[04:12.32–04:14.40; L111–L112] >> And that's a line by line proof and lean will go

[04:15.28–04:15.28; L113–L113] >> yes and check.

[04:16.64–05:07.60; L114–L133] >> Exactly. People will build automation for automating the process. uh they're going to use techniques like triples that says like uh we have a precondition some mathematical facts that should be true before executing that statement the statement and what is true after right and then we will have a lot of automation to to process makes your proof modeler right I mean uh complexity is a challenge in software verification handling the complexity is a big deal And there were all all these frameworks for very fine programs. They're trying to manage the complexity make your proofs modeler even with AI now AI can prove things automatically for us but they have to be modeler to the proofs if you want them to scale

[05:08.96–05:40.16; L134–L145] >> and what you're saying sounds similar to in software where you have to write it cleanly. It needs to be easy to edit and reason about. So it's almost like a second software layer on top of the software. Yes. Yes. You can view this way. You can also flip and imagine a future where you're writing the what you want mathematically precisely and AI synthesizing the codes and approve that the code that was synthesized meets your specification right.

[05:42.40–05:48.64; L146–L148] >> Oh interesting. So you could start by writing what you want to be true and then

[05:49.36–05:54.32; L149–L151] >> ask the AI please. AI is going to just go and hammer at it till the lean proof says you're good.

[05:55.92–06:58.80; L152–L174] >> Yes. Yes. It feels like science fiction. Six months ago I would say this is science fiction but for example now a colleague of mine Kin Morrison she a few months ago she started a project I thought was was six months ago I would say it's not possible at all. She said uh we have Z lib this s this compression library written in C and she said she creates a very complicated prompt for AI saying I want you to translate to ling ensure the lan version passes the test suite for for zib then I want you to prove that if you compress data and you decompress you get the original data back it's a really strong property right a and believe it or not they after one week succeeded doing the whole thing and now it's just asking to optimize the codes but you cannot break the proofs I mean you have to keep still proved all the

[07:01.28–07:15.92; L175–L180] properties you care about I mean compressing and decompressing getting the data back is a really important property for a compression engine right yeah This is enrich now. I mean, it's surreal. I mean,

[07:17.12–07:42.40; L181–L189] >> it's I mean, it's crazy. And I hear in the industry a lot of people, they use a really comprehensive test suite coupled with AI to do some really amazing rewrites cuz they have some more confidence that the rewrite is accurate and the AI can check itself. And it sounds like a specification is even better than a comprehensive test suite.

[07:45.44–08:33.12; L190–L207] >> Yes. Yes. Because with well your quotes from Dystra captures perfectly, right? With a test suites you can show the presence of bugs but not the absence. It's almost like with the a good test suite is you you may say well probably there are no bugs here but is you you may have a really corner case that's not covered by your test suite but with a proof you're covering all possible cases a and it connects so property based testing is really popular now people are writing properties they want to to ensure they are true but they are checking with testing, right? But now we can prove them and you say, "Look, there's no point testing anymore. I prove it."

[08:34.56–08:55.76; L208–L214] >> It seems like having a a well-written specification is a superset of a test suite. But in terms of the human labor required to create a a reasonable test suite versus a reasonable specification um you know how much more work is it to come up with a great specification

[08:58.80–10:08.56; L215–L238] >> varies a lot I mean uh the programs in many it's not uncommon for someone to start developing a piece of software and they don't know exactly what the spec is right but you know properties property usually their properties are very clear in your mind another thing that I tell people to keep in mind that inefficient program can give you this specification usually writing in efficient program is way easier than writing the super efficient one that does has many clever tricks you can write a very this is what I want in a very naive way and you Ask the AI look generate efficient version and optimize and prove that it's equivalent to my inefficient one. There are many scenarios. I mean I will not say this specifications are always easy to come up with but properties usually the developers have good ideas about properties they care about. uh as inefficient programmer is a spec rights you can view as a specification

[10:11.92–10:18.08; L239–L241] and the technology form of verification complements testing rights I think your code from extra captures perfectly

[10:21.52–10:26.96; L242–L244] >> and I think I saw this on Twitter because uh Jane Street was more heavily investing in formal verification

[10:28.96–10:28.96; L245–L245] >> yes

[10:29.28–10:37.20; L246–L249] >> and I read their post and they talked about this I think it was a sell for some software that was entirely formally verified.

[10:38.16–10:38.16; L250–L250] >> Yes.

[10:38.80–10:47.68; L251–L254] >> And the main drawback to why it wasn't, you know, how much more time would it take writing a program versus verifying it?

[10:48.48–11:49.44; L255–L277] >> Your example cell 4 is a great example. This was a major milestone. It's a micro kernel. They verified done manually was before AI. This project was done before AI was a big deal. And it's a lot. The cost is super expensive, right? At AWS, we have been using formal verification for a decade, but only for the super safety critical components because it's expensive until now, right? With AI, it changes the game. You have to come up with the spec. But this is not not the most painful part. The most painful part is to develop the proofs manually if you have to before. for AI and maintain the proofs as you change the codes. Imagine your I I've seen people complaining that oh I I change the program right now I have a bunch of failures in my test suite and I have to patch go one by one imagine with proofs you is the same process you have

[11:51.28–13:00.24; L278–L303] to fix the proofs uh sometimes you don't remember anymore why the pro what what's the story behind this proof is a lot but we AI is extremely good at proving uh writing formal proofs, maintaining formal proofs. For example, yesterday I was changing something. I want to modify some proofs for technical reasons and I I didn't even know what the proofs were about. Someone else wrote then I said, "Look, I want you to I asked the write these proofs without using this feature because I'm going to change it. I don't want to break the libraries instantaneous. It came up with the new proofs for me. I mean it's really good [snorts] and this is crucial for making formal verification mainstream because otherwise maintaining the proofs. It was almost like if your program took x amount of time to do the formal verification in the past would take 10x. That would be normal. But imagine if your program is changing.

[13:02.48–13:12.24; L304–L307] That's something that's really common. Now you have to keep maintaining the proofs too. It's a lot of work. But AI eliminates uh this pain for us.

[13:15.36–13:18.32; L308–L309] >> You mentioned that lean is because I I hear it as a proof assistant. But

[13:20.64–13:22.40; L310–L311] >> and then you also said it's a programming language. Yeah.

[13:23.76–14:14.56; L312–L333] >> Is that typical for proof assistants to be both a programming language and a proof assistant? Some of them especially the ones that are based on dependence type theory uh they are like rock and le are programming languages and proof assistance right I mean uh uh you can write definitions uh like uh when we're defining concepts in math but some of these definitions can be programs I mean and you have types you have structures is a programming language but is in that the family of called functional programming language I mean is a specific kind of programming language for people that are familiar with programming languages like Haskell ling is close to Haskell I mean but with the support for proofs that that's a way to to view ling

[14:16.16–14:19.84; L334–L336] >> are there major use cases where people use it as programming language but not as a proof assistant

[14:21.60–15:04.56; L337–L354] >> well the first big use case is link implemented in l we have many of our tooling is implemented in l like the the documentation authoring system called vers is implemented in ling. The build system that's called lake. It's like ling make lake is implemented in ling. Uh at AWS we have a compiler for AI acceler accelerators. It's half million lines of ling and it's using ling as a programming language. They're proving some properties about the program using ling. But the main goal is choose ling use ling as a programming language in this project. The proofs are like a a bonus right that you can get the proofs and find problems in the design.

[15:06.24–15:17.20; L355–L359] >> I think most people are familiar with programming languages and the tool chains they have and but um what are all the major components that you would need for a proof assistant?

[15:19.68–15:50.72; L360–L373] >> This is not that different. I mean if you're used to modern programming language like Rust the tooling for example lake is is our cargo right I mean uh you're going to open v visual studio codes same way and you're going to get all the intellisense one big difference is that we have something called the info view in ling your screens usually is going to be split in two you have your your file on the right hand side you have the info view that tells you information about your proofs, about your codes, uh is
