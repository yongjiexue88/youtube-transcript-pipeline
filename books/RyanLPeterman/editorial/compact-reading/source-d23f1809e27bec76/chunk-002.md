# Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov
Source: source-d23f1809e27bec76 | Chunk 2 of 3
Video: https://www.youtube.com/watch?v=T9CGjbPZeaM
All caption text retained; paragraphs merge caption fragments without changing words.

[14:17.60–14:32.96; L404–L411] >> I also noticed like um when you were uh when you came up with abstract data types maybe I mean maybe it's just cuz there wasn't the internet wasn't as, you know, wasn't there that there was also the object-oriented stuff going on on the West Coast.

[14:33.96–15:32.24; L412–L439] >> Yes, Alan Kay was developing Smalltalk at the same time that I was working on Clu, and then at Carnegie Mellon uh Bill Wulf and Mary Shaw were working on Alphard, which was another data abstraction language. And you're right, there was no there was no internet, although there was the ARPANET. You know, so we did but it was like there were two independent streams of research going on and we weren't talking to each other. And so, I wasn't paying much attention to Smalltalk and on the West Coast, I don't think they were paying much attention to data abstraction. And this led to the Liskov substitution principle which I mean, the story is a sort of a cute one because in 1986, I think it was, I was asked to give a keynote at OOPSLA. OOPSLA is the object-oriented programming conference, and this was the second year it was happening. And so, I decided I think I'll read all

[15:35.04–16:33.16; L440–L468] those papers about Smalltalk, and there were other languages being developed that were based on Smalltalk, and see what's going on with them. And I discovered Um so, Smalltalk has this idea of inheritance in it, where you can have a class and a subclass which borrows from the way the class is implemented and changes it a bit. And Clu doesn't have that. Clu just has what we call clusters, and they're all independent. So, I saw that they were talking about this notion of classes and subclasses. And and then I saw that they were also talking about something they called type hierarchy. Where they wanted the type implemented by a class to be related in some way that they didn't understand to the type that was implemented by a subclass. I really thought about modules in terms of their specifications. This partly had to do with a class I developed at MIT that I developed jointly with my

[16:34.44–17:29.28; L469–L495] colleague John Guttag. And in that class, we taught the students how to do design, about modularity, data types, and so forth, but also how to write specifications, how to reason about correctness. And so, it had a big focus on think about the meaning of things first, and the implementation is something that's kind of hidden inside, and you don't worry about it very much. And so, that was a different way of thinking about things than what was going on in the on the West Coast, where they were really thinking in terms of classes and subclasses. And I even saw papers where they would describe the behavior of a class by explaining how its implementation was different from the implementation of the superclass. So, they were kind of focused on implementations in a way that we weren't. And so, when I read these papers about type hierarchy and I saw they just couldn't figure out what it was supposed to mean,

[17:32.12–17:56.52; L496–L508] I was thinking about it from the terms of meaning. And so, I was able to say it has to do with the behavior. And this subclass better behave like the superclass if you use it in an environment where the superclass is expected. And that became what ended up being called the Liskov substitution principle. And ultimately, Jeannette Wing and I wrote a paper on behavioral subtyping, which is the formal definition.

[17:58.84–18:03.96; L509–L512] >> And then, how did it get that name? Cuz you didn't go off on stage and say, "Hey everyone, here's the Liskov substitution principle."

[18:06.32–18:19.20; L513–L520] >> one day in the in the '90s, after the internet had arrived, I got an email saying, "Can you say if this is the correct interpretation of the Liskov substitution principle?" That's when I discovered that

[18:19.76–18:19.76; L521–L521] >> [laughter]

[18:20.44–18:29.92; L522–L527] >> there was such a name. And And I I don't think I had really been aware of how important it was until that point, because I wasn't thinking about this stuff. I was working on other stuff.

[18:32.20–18:56.76; L528–L537] >> In the academic community, it seems very reasonable to have multiple people have similar ideas. But it seems like some ideas stick more than others. For instance, like the Viewstamped Replication versus Paxos. They're the same thing. I'm wondering, like, in that case for instance, why would Paxos be more known than Viewstamped Replication?

[18:57.84–19:03.20; L538–L540] >> Yeah. So, what Leslie says is, "I went around giving all the talks, and she implemented it."

[19:05.61–19:05.61; L541–L541] >> [laughter]

[19:07.88–19:07.88; L542–L542] >> Really?

[19:09.76–19:09.76; L543–L543] >> Something up to that.

[19:11.56–19:13.20; L544–L545] >> Then he got notoriety for speaking about it.

[19:16.36–19:26.24; L546–L550] >> Yeah, he he he did give lots of talks about it and wrote several papers and so forth and I didn't realize it was the same system. But finally it became clear that they were the same system.

[19:28.28–19:33.44; L551–L553] >> I also wonder how much the name matters because Paxos is kind of catchy, you know.

[19:33.52–19:33.52; L554–L554] >> It is a cute name.

[19:34.48–19:34.48; L555–L555] >> It's a cute name, yeah.

[19:35.40–19:35.40; L556–L556] >> Yeah, right.

[19:36.28–19:38.60; L557–L558] >> So, I I could see maybe it has better marketing around the idea, I guess.

[19:41.48–20:38.24; L559–L584] >> I also think that this approach to solving this problem, which both Leslie and I picked up independently, in my case came from the work I'd been doing with transactions. Because in transactions there's a leader that you know, says now we're going to commit and ask everybody can we commit and if they all say okay, you know, it's but unlike in transactions of in transactions if the leader fails, there's what's called, you know, the this can be a real problem. Here we had to have a way of moving to a new leader if the old leader failed and that's the big step forward that happened in both Viewstamped Replication and and Paxos. Now, there was also Byzantine fault tolerance, which came along later that was developed. So, Viewstamped Replication I developed with my student Brian Oki. It was his PhD thesis. And then Paxos I developed with my student Miguel Castro. It was his PhD

[20:41.20–21:39.64; L585–L614] student thesis. And Miguel got interested in this problem because uh there was a DARPA request for proposals and there was one about this problem on the internet. By then there were Byzantine attacks and you know, malicious attacks and nodes that would purport to be working correctly, but actually they had been compromised and so forth and so Viewstamped application in Paxos only handled crashes and um if there were messages that were had been played with, you could tell when they arrived that they were bad. And that was about the extent of what we dealt with. But these malicious attacks with nodes that purported to be working when they weren't, that was a big step forward. And Miguel saw this request for proposals and he said to me, "Why don't we see whether we can come up with a protocol that works in the presence of Byzantine attacks?" And and I think by the way, Leslie is the

[21:41.24–21:41.24; L615–L615] one that invented the word Byzantine to

[21:43.36–21:43.36; L616–L616] >> I think he did.

[21:43.96–21:43.96; L617–L617] >> Yeah, right.

[21:44.92–21:57.12; L618–L623] >> I saw in the in the software crisis stuff. There's the paper with Dijkstra that you had mentioned was one of the papers you you wrote that said, "We need modularity." And that paper was the go-to statements considered harmful.

[21:59.32–21:59.32; L624–L624] >> Right.

[22:00.16–22:07.16; L625–L628] >> And I'm curious cuz Dijkstra, I mean, when I was studying computer science, you we all know his name. Did you ever meet him or work with him?

[22:08.52–23:06.20; L629–L654] >> Oh, yeah, many ti- I did never worked with him, but I did meet him multiple times. And uh you know, he had very interesting ideas. And that paper, uh go-to statement considered harmful, it's not actually a paper. It was a letter to the editor of the Communications of the ACM. But it was very impactful. And what was really important about that paper was that Dijkstra was talking about how difficult it is to reason about the correctness of code. And this was at a time when in the sciences, computer science was kind of dismissed as nothing much. And anybody can write code. And you know, Dijkstra was trying to make a point, which I think was actually important, that it it's not as trivial as you think it is. It's not trivial at all. Um and he was also pointing out that go-tos can be misused.

[23:08.52–23:08.52; L655–L655] >> And it was controversial at the time.

[23:11.28–23:11.28; L656–L656] >> It was, yeah.

[23:12.12–23:15.20; L657–L658] >> But today I I I don't I mean I've written code for yeah, over a decade.

[23:17.68–23:17.68; L659–L659] >> People don't use go-tos.

[23:18.52–23:23.72; L660–L663] >> have I have I haven't even seen a go-to in the code. So, what why was it controversial at the time?

[23:24.76–24:11.12; L664–L687] >> The programming languages were different then. Um first of all, there were people writing programs in assembler. In assembler, you have to use go-tos. Programming languages didn't have some of the constructs in them that we think of today. And uh so some people were using go-tos cuz they had to. And also um compilers didn't do all the kinds of optimizations that they do today. So, there was a concern if you didn't have go-tos, maybe your program wouldn't be efficient enough. And then uh there were people who used go-tos and wrote really good code, and they weren't offended that Dijkstra was saying your code is bad. So, there was a whole but and and Dijkstra was not the most um diplomatic person. So,

[24:12.81–24:12.81; L688–L688] >> [laughter]

[24:13.84–24:41.56; L689–L703] >> you know, so he he didn't write it in the you know, nice not you can imagine writing that paper more nicely where you said um So, it that but there were many reasons why it was controversial. You know, people were offended, but then there were also concerns about like programming languages don't have these features I need, what am I supposed to do? And then there were concerns about what the compiler was doing. And so, the world is very different now. But clearly, Dijkstra won the day.

[24:43.56–24:43.56; L704–L704] >> Yeah, he did.

[24:44.12–24:45.20; L705–L706] >> Because no go-tos.

[24:46.87–24:46.87; L707–L707] >> [laughter]

[24:49.00–24:52.00; L708–L709] >> And is Dijkstra in person also like his writing?

[24:55.40–24:57.56; L710–L711] >> Uh he was not always as tactful as he might be.

[24:58.66–24:58.66; L712–L712] >> [laughter]

[25:00.00–25:02.56; L713–L714] >> Yeah, but you know, he was a a very uh, distinguished researcher.

[25:04.28–25:11.56; L715–L718] >> Computer science has had such a huge impact on the industry. Why did you choose to stay in academia instead of going into industry?

[25:14.00–26:15.04; L719–L745] >> So, I like doing research. And I enjoy working with students. And I teaching was never my favorite thing, but I always felt teaching and research were very closely connected. Um, but also it was a different time. So, this business about how professors are all forming companies and so forth, which goes on today, that wasn't happening 20 years ago. Or maybe it was happening 20 years ago, but 30 years ago it wasn't. So, when I was young, it wasn't the thing that you did. It was sort of a either or sort of thing. So, I wasn't even thinking about doing stuff like that. I did work in a startup briefly at the end of the '90s. I didn't like it. I much prefer doing research and as a professor you have this it's it's a gift and a curse. The gift is you can do whatever you want. The curse is you have to figure

[26:17.12–26:31.28; L746–L752] out what it is that you're doing. But I like that freedom. And the fact that I just could go off in any I mean, my career is full of these interesting zigzags where I would switch to something else. I had the freedom to do that.

[26:32.28–26:34.72; L753–L754] >> What stops you from going off in a very useless direction?

[26:36.32–26:36.32; L755–L755] >> Uh, you won't get tenure.

[26:38.87–26:38.87; L756–L756] >> [laughter]

[26:40.32–26:40.32; L757–L757] >> Who's the judge?

[26:41.84–27:06.04; L758–L770] >> The community. Yeah, it's not you know, what what the way that you're viewed at your university has mostly to do with um, one a very important facet of it is how are you viewed in your research community. So, because that's one of the important things they want from their faculty if you're in a research university.

[27:07.84–27:13.96; L771–L774] >> You mentioned earlier that research and teaching were heavily related in your opinion. Why is that?

[27:15.04–27:29.20; L775–L781] >> Because when you teach, you have to teach from first principles. And if you're doing good research, you need to understand deeply what's working, what's not working, what assumptions you're making. It's It's really the same thought process.

[27:31.88–27:58.92; L782–L794] >> It's It sounds like in research I mean, and this is true in every walk of life. There's the I guess the direction that you take and then the work that you do towards that direction. And it sounds like for research the the direction is maybe the most important thing cuz you could have a phenomenal researcher doing an idea that has no you know, even if you did it at 100% it's not going to lead to anything.

[28:01.52–28:30.68; L795–L809] >> So, you you know, I you tell students graduate students don't do incremental work. Don't you know, you've got you you can't just keep working on the same thing over and over just making little teeny improvements. You need to find You're right, you have to find a good problem, but you also have to find a problem that's amenable to a solution and one that matches your skill set. And you have to recognize when you're going in a good direction versus not going in a good direction.

[28:32.40–28:40.80; L810–L813] >> Looking back on your career, you say that it was luck and that it seems like things just fit together.

[28:42.08–29:10.88; L814–L824] >> I feel there was luck involved. There was a lot of hard work involved. There was um not allowing uh something negative to you know, cause you great difficulty. So, for example, when I finished my PhD, I would have liked a faculty position. But, I didn't have any good offers. So, I went back to Mitre, the company I
