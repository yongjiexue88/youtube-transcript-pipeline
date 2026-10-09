# Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg
Source: source-fd3381490fc526e5 | Chunk 2 of 5
Video: https://www.youtube.com/watch?v=cywK3XYYJ2o
All caption text retained; paragraphs merge caption fragments without changing words.

[13:52.48–14:43.36; L354–L374] There is, but it it but it comes often with a whole bunch of restrictions and and and it doesn't come necessarily with the safety guarantees that we were looking for. I mean, like Go is type safe and memory safe. uh meaning that you don't get to just like have stray pointers or or whatever where Rust you can do ref counting or you can do you can do all sorts of different strategies but there's always like that little bit of unsafe where you have to like do this in order to make it all work you know uh where where if garbage collection is engineered into the language it really is a a separate concern that is you you you don't you don't have to do anything special in I mean of course you you have to like not hold on to data that you no longer need and whatever you know but that's true of ref counting as well

[14:45.04–15:05.44; L375–L383] right but but it is inherent in in the language when you ported it from JavaScript to go I'm curious how much LLMs were used in that process because I know famously there's some major projects that have been doing uh rewrites of their entire codebase I know there's this JavaScript project called bun

[15:06.80–15:09.44; L384–L385] >> that rewrote everything from Zigg into Rust and so

[15:10.80–15:16.00; L386–L388] >> seems like a pretty useful tactic and I'm curious if you leverage that in this process.

[15:16.80–16:09.92; L389–L410] >> Not a whole lot but it also has to do with timing. Uh we started this project two years ago and two years ago LLMs were nowhere near as good as they are now. I mean that's how crazy fast it it's all moved, right? Um, so what we did though is we we certainly had a bunch of tools that aided us in the in the in the the port. I'd say the prototypes we wrote, the scanner and the parser we wrote manually. Um, and at that point we could convince ourselves, wow, we can actually get 10x out of this. Now what do we do with the rest of this codebase? And what we did was we wrote a tool that syntactically translates TypeScript into Go. This Go that comes out of it, it has no syntax errors in it, but it doesn't compile either because it's full of, you know, like it uses types as if they were

[16:12.56–17:00.48; L411–L431] TypeScript, which they're not in Go. And so all of that had to be refactored. We had to redo all the data structures or whatever, but we got the same code base out of it. And then we can sort of bang on that. and then in a more localized fashion maybe use AI occasionally to help us do the transformation. So it was sort of manual and automated and a little bit of AI. Now if we were to start the project today would we do it differently? Possibly. Um although I will say if if we just let AI loose on you know what is it like half a million lines of code that we have in the old compiler or somewhere between half a million and a million right uh and asked it to translate it all. Well I don't know that that would absolve us from then having go in and carefully examining every line that came out of it

[17:02.32–17:53.44; L432–L455] to make sure that there were no hallucinations. Right? Unless you have 100% perfect test coverage, you probably still got to go check all of that. Now I think a a a better approach quite honestly would be enlist AI to write a program that helps you translate from Typescript to Go because at that point you can park the stochasticness in that program and then you can get deterministic behavior whenever you run the program which means you get the same transformation every time you run it right that's always the thing about AI that people forget it's not deterministic right so you can't really trust that it's going to do the same thing twice. Um, [snorts] so, so we might have done it that way, but AI was not ready to do it at the time. Now, that doesn't mean that we don't use AI. I mean, like now down the line, we use AI a lot in our in our

[17:56.24–18:11.44; L456–L463] internal processes around like the the compiler as everyone does, right? Like help it to write tests and to move pull requests and what what what have you. and and whenever an issue is logged, we first thing we do is put copilot on and see if it can fix it for us, right? I mean, and so yeah,

[18:13.04–18:19.12; L464–L466] >> in that approach where you you use the LM to generate uh tooling and then you know the tooling is deterministic,

[18:21.12–18:23.52; L467–L468] >> but you'd still have to validate that thing.

[18:23.92–19:06.88; L469–L490] >> Yes. But that's that's a lot smaller surface area that you have to validate, right? And honestly, I I've seen that even with friends that are like we did some trip together and there was like some some accounting of they go, well, he paid for the hotel rooms or we paid for this and whatever and we needed to like sort it all out, right? And so, so, okay, well, here's what all the costs were and here were the pie and like have AI fix it for us, right? Or like tell who owes who what and it very authoritatively came up with the wrong answer, right? [laughter] Because it just forgot like about some of the settlements, right? And but if we had asked it to write a spreadsheet, which is really that's just a program, right? Then we would have gotten the right answer because it's very good at writing programs. So it's kind of funny

[19:09.60–19:16.48; L491–L494] how you you you don't sometimes you you don't ask AI for the for the answer. You ask it for a program that computes the answer.

[19:17.84–19:21.84; L495–L497] >> What are the potential benefits that you left on the table by doing a port instead of a full rewrite?

[19:23.52–20:12.72; L498–L520] >> To be honest, I don't think there are any. Um, and I don't think we would consider uh a rewrite. We were quite happy we're quite happy with the way this codebase works. Uh, and we're and we certainly I don't think we're leaving any any money on the on the table currently. Um, and and as I said earlier, rewrites are toxic often for ecosystems because they sacrifice compatibility because you never rewrite and you get you never get back to exactly what you had before, right? Oh, but oh, but in the name of making it better or prettier or whatever, we change this and that and this and that and the other, right? And then well, all the users get to suffer through that, right? So, so backwards compatibility is super important if you want to keep your ecosystem happy. Uh, and and and we we do want that. [laughter] In studying for this interview, I I just

[20:15.20–20:27.44; L521–L526] keep reading about JavaScript and the the strange semantics of the language. And I think throughout my career too, people have typically not been super satisfied or happy with JavaScript for some reason or the other,

[20:29.84–20:29.84; L527–L527] >> right?

[20:30.72–20:34.64; L528–L529] >> And my question is why is it so popular despite that?

[20:36.24–21:28.88; L530–L553] >> So first of all, I I don't think JavaScript is as bad of a lang of a language as as some people make it out to be. I I I will say in in like the three about three four weeks that Brendan Ike had to create this language back in the mid 90s, he did a lot of things right. Um and thank God that he had been educated on functional programming and and got first class functions done right where you can have functions within functions and the inner functions can access the outer function state and you can pass functions around as first class values. that is super powerful and JavaScript actually got that very right. Um, now there's some quirks in the language too, like all of the automatic conversions and all of the bizarre differences between double equals and triple equals are just like drives everyone mad, right? But that's exactly what type checkers are happy to do. They can like

[21:30.48–22:25.76; L554–L577] they can far it out all the little differences because they understand the all the deep semantics of the language that no one seems to be able to keep in their mind, right? So, and I think that's part of why Typescript has become so popular, right? It's like it can actually like truly bring out the best parts of JavaScript uh and leave the bad stuff behind. And of course, you can't like like the thing about JavaScript is it is the crossplatform language. Like even Java that was engineered and intended to be the way to write crossplatform applications, it's not really crossplatform. It doesn't run in the browser, you I mean it doesn't it doesn't run everywhere, right? JavaScript runs everywhere. Um, so there are a lot of there are a lot of reasons why you should like JavaScript and and with TypeScript, I think we've managed to sort of capture all the badness and park it.

[22:27.76–22:32.72; L578–L580] I saw there were some projects. I don't know if you're familiar with Dart or CoffeeScript and

[22:34.64–22:37.68; L581–L582] >> it seems like these were some effort to replace JavaScript or improve it and

[22:40.96–22:40.96; L583–L583] >> right

[22:41.44–22:43.36; L584–L585] >> but they're not popular today. So I'm curious what happened.

[22:44.72–23:26.80; L586–L602] >> I mean I think coffecript was mostly it's a different syntax for JavaScript. So, so it doesn't really change the the semantics and it doesn't it didn't provide any additional tooling and and whatever. And and Dart was also in a sense about fixing JavaScript, right? But if you can fix something by fixing it instead of trying to replace it with something else, then you're doing the ecosystem a much bigger favor, I think. Right. And that's what we set out to do with TypeScript. We weren't trying to change JavaScript. we were trying to improve JavaScript. Um, and I think that's ultimately why we why we succeeded.

[23:28.24–23:49.84; L603–L612] >> I mean, in this new age where it's very feasible that maybe AI could rewrite code bases, um, I imagine people will start to go towards the the desired languages rather than the ones that are the incumbent languages. And I'm curious if you think that JavaScript might become less used in the future.

[23:51.52–24:44.00; L613–L634] >> See, I I don't think so. I I what I've observed is that AI is best at the languages if seen the most of in its training set, right? And AI gets trained on all the code that exists in the world. Um, which means there's an awful lot of JavaScript, an awful lot of TypeScript, an awful lot of Python. And therefore, AI is good at JavaScript and TypeScript and Python. And it is less good at my favorite little language that I just invented. In fact, there's none of it in the training set, which means you have to sacrifice God knows how many tokens in the prompt to teach AI the language before you can even ask it a question about the language. Do you know what I mean? So in that sense I think incumbent languages are actually if anything going to flourish uh because of AI and we're sort of seeing that right now with with

[24:45.76–24:57.52; L635–L640] TypeScript too right there there's a noticeable knee in the curve of TypeScript adoption that coincides with the advent of AI. I do think the incumbent languages are actually if anything getting stronger.

[24:59.12–25:14.96; L641–L646] >> What percent of all JavaScript is written in Typescript? Well, so, so in the last year, Typescript uh became the number one used language on GitHub. Um, so there's JavaScript more than JavaScript.

[25:16.72–25:16.72; L647–L647] >> So, so more than 50% on GitHub at least

[25:20.56–25:27.68; L648–L651] >> is is is written in in Typescript. Um, so so we're actually like larger now than the language that we set out to improve.

[25:28.96–25:28.96; L652–L652] >> Wow.

[25:29.52–25:40.40; L653–L658] >> Yeah. And larger than Python. If you were to just draw that out in the future, do you think that eventually TypeScript would become the default and almost 100% of all JavaScript would be typed?

[25:41.60–26:32.32; L659–L680] >> Well, certainly, I mean, if you're having AI write it, I I almost challenge you to find a tool that writes JavaScript. They all write TypeScript. Uh because it helps AI write better code because the type annotations guide the LLM towards writing or to write making fewer mistakes. and the ability for us to statically validate the code before you run it. I mean, that's the distinction, right? The only way you can validate JavaScript is by running it, which means you have to set up a runtime environment, which might not be possible for AI to do because AI lives in a sandbox, right? But AI can run through tools, the compiler, and check the code that it just generated and be told, "Oh, you made a mistake. Oh, well, let me fix it then before I even tell anyone that I made the mistake, right? [laughter] [snorts]

[26:32.96–26:47.28; L681–L686] >> After learning about the this 10x improvement in performance from uh rewriting in native, I makes me wonder why anyone would use JavaScript on the back end. Why not just always use native languages on the back end?

[26:48.48–27:34.40; L687–L705] >> Well, it depends on your problem. Uh I think because the thing that that overlooks is what kind of thing am I going to write on the back end, you know, like like there are an awful lot of very very good web server frameworks for example that that use TypeScript or JavaScript, right? So, so if there are like frameworks in your ecosystem that gets you to a solution quicker than if you had to write that because your native language wasn't really intended to target that particular community. So, I think it very much depends on your what what your problem is affinitized with. Um, and and often PF of your code isn't the bottleneck. I mean, like look at Python. I mean right
