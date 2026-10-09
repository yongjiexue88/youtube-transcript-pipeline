# OpenAI Codex Tech Lead: How His Career Grew And How He Uses Codex | Michael Bolin
Source: source-d89129dbba19118b | Chunk 6 of 8
Video: https://www.youtube.com/watch?v=hN5ZFzWFhhg
All caption text retained; paragraphs merge caption fragments without changing words.

[56:40.64–56:44.40; L1567–L1569] get through these PRs faster, which is good because there was a lot more review to do.

[56:45.28–56:51.36; L1570–L1572] >> That's I mean that's amazing. I feel like and 50% of diffs have like you know almost blank the test plan says you know

[56:55.28–56:56.88; L1573–L1574] >> uh I don't know arc build or whatever the oh I know but [laughter]

[57:00.40–57:49.76; L1575–L1596] >> um I want to talk about the the the codec cli that's that's open source why is it open source you know for something that's that critical to like what's going on on your machine right like that that like that's one of the aspects of open source is that I'm not you know the most um zealous about this sort of thing but I but I I sympathize with it this idea that like hey you're going to put this thing on my machine I care about what it's doing right and I think in this domain in particular it's really important that people can look at it you know and have have an idea of what it's doing um because you know people have a lot of questions about AI agents and that sort of thing um and so I think I think this this this area this domain I think it's actually really important um and also we um you

[57:53.52–58:19.68; L1597–L1609] know we have gotten a lot of uh I think like great compriations and bug reports and things like that that we um would have missed out on um and and and then also I think it's you know um just you know sharing with the world with like how this is done um so we do it through code right I've I've put out um one blog post about how the agent loop works like there is plan to do more of that. I'm actually excited to. It's just, you know, just it's just time is this liming factor.

[58:21.20–58:21.20; L1610–L1610] >> Really, not

[58:22.16–58:34.08; L1611–L1618] >> Yeah. It was funny because I had I had I had two candidates who came through and one's like he's like, "Hey, I wrote it, right?" I was like, "No, no, I I [snorts] wrote it." And another person came in. He's like, "Oh, you can tell that that you know that you did not outsource the

[58:35.36–58:36.64; L1619–L1620] >> Okay, good. Right. I was like, oh, thank you." You know? Um, so yeah,

[58:38.56–58:54.64; L1621–L1628] >> you mentioned the blog post. How does Codeex find what is available to it in its environment? And when I'm running these things, I'll see it's kind of amazing. It's thinking to itself and like discovering all these things in in my uh terminal. So yeah, how does that typically work?

[58:55.52–59:39.60; L1629–L1650] >> Yeah, I mean there's, you know, there's a few. I mean there's obviously what is you know when Codex is based training like it loves to use rip grip. It uses rip grip very well to find all sorts of things. Um, and then there's, you know, if you have your agents MD file and you're say, hey, in this repo, like these tools are really important, right? You should use these, right? Or the readmemes or whatever. Um, or uh obviously if you use MCP and you associate these MCP servers with your um, you know, where you're working on, right, that that that um injects the set of tool definitions like at the start of the the conversation, right? So then uh that kind of Yeah. So that's that's not even like discovery on Codex's part, right? It's kind of just like put front and center there. I see. So some of it's the harness explicitly throwing that

[59:42.72–59:42.72; L1651–L1651] into the context

[59:44.16–59:49.84; L1652–L1655] >> and then there is a big chunk though where the model is just doing all the heavy lifting of finding things. Is that right?

[59:50.16–59:50.16; L1656–L1656] >> Yeah.

[59:50.64–01:00:18.96; L1657–L1669] >> Kind of like reflecting over your career. The breadth and depth of your work if we look across all of it. I mean it's it's insane. you were your javascript front end then you have all these dev tool you know build fuzzy file search you know virtual now you're working on codecs you I'm sure you had to uh continue your engineering educa education to kind of get through all these projects what are the top technical books that have helped you educate yourself

[01:00:20.24–01:01:02.96; L1670–L1691] >> yeah I mean um you know so one was this uh this book on operating systems um it's like a thousand pages or something like this. Uh it's the Addison Wesley book. I'm trying the author, but it was funny because I was when I was working on the virtual file system. So I had actually gotten to that point in my career without ever writing C like undergrad like it was like more theoretical like we just never had to touch it. And then yet I'm like working on a virtual file system project and then like very low operating system. That's why I was, you know, joke that I was kind of the worst engineer of the project. And, you know, and someone said something and I realized I was like, I don't know what they're talking about. This is kind of embarrassing. And I was just like, you know, what book do I have to read? And I think my manager, Aaron

[01:01:04.80–01:01:52.40; L1692–L1712] Kushner at the time was like, he's like, well, there's this thousandpage book. And I was like, done. So, I bought it, read the thing cover to cover. I like took it to Hawaii with me. I took it everywhere until I finished it. It's it's kind of amazing and sad or weird that like how um how far many of us can get like in software engineering without really having a clue how computers work. Like there's just so many of those levels of abstraction. Um but you know one hand it's very freeing and then on the other hand it's a little bananas. And I think that um what I would say to people right now is um is you know actively trying to go like deeper through the layers and understand these things. Um and uh like cuz many times I saw other people do it and now I can do it is that there are problems some other

[01:01:54.24–01:02:40.00; L1713–L1734] people could solve that I couldn't solve because I just didn't know that like there was this croft between these two layers and if you got rid of it, right, you get like a 10x improvement or something like that, right? If you if you're just operating so high up, you don't really know, you know, what you can what you can break down. um you know so that um and so in terms of books like uh I've enjoyed the like the O'Reilly uh the Rust books um I you know big fan of Rust um I think but they're also like well written um and and thorough and then honestly another thing I've been telling people um that's not in the book category but probably more fun and I learned a lot uh actually um are um these CTFs are like capture the flag like security type competitions And just, you know, it helps with like kind of like adversarial mindset. it helps

[01:02:42.32–01:03:12.00; L1735–L1748] with I think uh they're usually just like it's like a it's like a dicath like a computer dicathlon I feel like right because like like there'll be multiple challenges and maybe this one you need to like understand assembly and this one you need to understand like what someone's like janky PHP admin pages do all this sort of thing and it and it just forces this um breadth on you uh in a way that's kind of hard to to generate otherwise and it's also you know just more fun because it's like a game and that sort of thing.

[01:03:12.72–01:03:58.24; L1749–L1770] >> Can you give some context on what CTF is? Yeah. So, it's it's it can be a number of things, but uh it's it's usually a competition usually in like the infosc the security domain and there'll be a set of uh there's like the Jeopardy style one which is like there's a bunch of challenges um and like you know designed like crafted ahead of time and they all have point values associated with them and so you know there's usually some fixed amount of time and it could be individual it could be with a team and you're trying to solve these things and and there's a flag there's always like a secret, you know, um, piece of text um, in there that usually has some format. And the way is that you basically if you can discover the secret piece of text, that means that you have the the challenge is set up that you would only have gotten

[01:03:59.44–01:04:18.72; L1771–L1783] that if you had figured out, you know, reverse engineered or whatever you were supposed to do and then you get submit that piece of text and that's your, you know, token to demonstrate that you had solved the challenge. And so it could be like a race to like solve everything first or get the most points in a certain amount of time or different things like that. So it's like it's kind of like an escape room but in your terminal you use only computers to figure everything out.

[01:04:19.76–01:04:19.76; L1784–L1784] >> Yes.

[01:04:20.48–01:04:31.20; L1785–L1790] >> I see. Okay. And your recommendation is people who want to become better engineers they should invest in doing some of these CTF because they make you solve problems that make you a better engineer.

[01:04:31.92–01:04:47.68; L1791–L1799] >> Yeah. and you know and then you you know also develop skills and things that you just wouldn't have you know if you're just like a you know writing react every day like you're probably not going to like open up GDB and like reverse a you know a tic-tac-toe game but like I did that because of you know a CTF challenge was to do you know exactly that

[01:04:49.76–01:04:49.76; L1800–L1800] >> right

[01:04:50.48–01:05:14.24; L1801–L1812] >> um and but then it's like but then I learned how to use GDB and like and and then then you start you know when you're faced with other problems you're like oh my my just toolkit of of ways to solve things is just much broader broader a lot of people especially earlier in their career they see the power of codeex doing everything for them in the terminal and I just imagine them saying oh well I don't need to learn GDB because uh Codex knows it so

[01:05:17.44–01:05:23.68; L1813–L1816] >> um would what would your advice be given the landscape of these AI tools for people thinking about their engineering education

[01:05:24.56–01:06:09.44; L1817–L1837] >> yeah no that's I mean I think everyone's like struggling to answer that uh question right now um I do think about it you a a lot and I I don't have a great answer. I I I kind of personally come back to my thing about like um I still think like trying to forcefully kind of go through the levels of of abstraction and just understand um you know more like at a deeper level how things work um is going to be important. I mean I think this will change. I'm sure this will change over time, but right now it's still kind of like, you know, the questions that you asked the agent is going to affect the quality of the thing that you get out, right? So, if you're not asking the right questions, you're not maybe going to get the best engineering solution out the other side. You know, as things go on,

[01:06:11.92–01:06:53.20; L1838–L1859] perhaps that will also be, you know, another layer that's removed. I mean, I think, you know, that's certainly where we're going. I don't know what time frame we'll get there. things do seem to be happening faster than we expect. But um yeah, I think in general, but learning how to ask what the right question is and I and I haven't, you know, for myself even like totally pinned down what that means for for someone who's like starting out new, right? You fortunately have experience to to fall back on or like that's where that that that taste or that um intuition of what to ask has has developed. But, you know, if you're if you're starting out, um, I'm still not sure yet. And it's also hard to say because we we don't really know 100% where everything's going.

[01:06:54.96–01:07:15.84; L1860–L1868] >> Yeah. When you reflect over your career, the expectations at these really high levels is kind of crazy. I mean, it's like already for most people, this E7 or senior staff level is this unattainable level of impact. So someone who gets promoted to that level is thinking, I gotta really work super hard now because the bar is like up here.

[01:07:18.16–01:08:02.08; L1869–L1890] >> And then you went two levels past that. And so I I'm curious like in the day-to-day now, what what are your thoughts on these like crazy expectations? Is it stressful for you? I mean it never it was never not stressful I think um for me because I really I think also because I sat in calibrations right and I um you know so for a bunch of other people you know you talk about their level you talk about their impact and you know you wanted to be really fair and have this integrity around well this level means this thing and this is the impact like that's what it means all is that's what exceeds this and then knowing that like then you're you know playing it out in your mind like well someone's sitting in my calibration and talking about this thing and they want to be fair, right? And and it is a little scary like you know you

[01:08:03.76–01:08:05.28; L1891–L1892] get to E8 and you're like oh you know it's a D1 a director

[01:08:07.28–01:08:11.20; L1893–L1895] >> and you're like how do I have as much impact as a person who has maybe like over a hundred people

[01:08:12.96–01:08:17.84; L1896–L1898] >> in their or so that's hard a lot of people do it again a lot of people who are I see who do it do it more by
