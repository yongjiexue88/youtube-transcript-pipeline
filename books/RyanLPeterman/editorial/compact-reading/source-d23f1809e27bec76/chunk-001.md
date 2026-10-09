# Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov
Source: source-d23f1809e27bec76 | Chunk 1 of 3
Video: https://www.youtube.com/watch?v=T9CGjbPZeaM
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.00–00:00.00; L10–L10] Don't do incremental work.

[00:02.48–00:08.92; L11–L14] >> This is Barbara Liskov. She's a Turing Award winner famous for her fundamental contributions to programming languages and distributed systems.

[00:10.36–00:17.68; L15–L18] >> Encapsulation is a crucial part of making modularity work. Your team is really only as strong as your weakest programmer.

[00:18.84–00:25.84; L19–L22] >> I asked her for stories from her career. That paper was the go-to statements considered harmful. Is Dijkstra in person also like his writing?

[00:28.32–00:30.48; L23–L24] >> He was not always as tactful as he might be.

[00:31.36–00:58.72; L25–L34] >> There were people saying, "Why did she get the Turing Award?" Why do you think that they said that about your work? Here's the full episode. You applied to multiple places and Princeton was one of them and they had rejected you on the grounds of you being a a woman. How did you get into programming in an environment that's so hostile?

[01:00.12–01:58.40; L35–L62] >> Okay, so this was when I got my bachelor's degree. And I applied to several graduate programs in math, which is what I majored in as an undergraduate. And I got this little card back. It was a postcard from Princeton saying, "We do not admit women." Which was surprising. Um I knew they didn't have women in their undergraduate program, but I hadn't realized it extended to the graduate program. Um but you know, it was how it was. So so what happened was I did get into Berkeley, which is where I did my undergraduate work. But I decided I really wasn't ready to do a a PhD in math and that I should get a job instead and just sort of see you know, see how things were. And uh the best job offer I got was as a programmer. So that's how I got computer science by a happy accident.

[02:00.64–02:10.12; L63–L67] >> You were consistently, at least at Berkeley, you were consistently a top student. So, it's it it is odd that you wouldn't even get an opportunity to play in some cases.

[02:11.44–02:51.88; L68–L85] >> But, that's how it was back then. It was just I hadn't realized it was more than an undergraduate thing. And Berkeley was co-ed. So, you know, there what I found was there weren't very many women in my classes. There were lots of women students, but very few of them majoring in math. And there were only maybe a couple of women in my classes. But, the uh the idea that a door was shut and women couldn't do things, that was not what went on at Berkeley. So, it was a different environment. Of course, nowadays in the top schools, the um women are about 50% in computer science.

[02:53.56–03:07.60; L86–L92] >> I want to talk about some of the the core problems that you were solving in your career. And so, I understand that there's the software crisis in the 1970s. And uh I was wondering if you could give the context behind what the problem was at that time.

[03:09.64–04:17.40; L93–L123] >> Well, it was a huge problem at the time because uh people did not know how to build big programs that worked. And so, you would often pick up the newspaper and see an article about some company that had spent uh you know, millions of dollars and hundreds of man-years developing some software system for their company. And then in the end they'd have to throw it away because they it simply didn't work. The problem was that to get a big program that works, you need modularity. And you need to break your program up into small pieces. Each piece provides an interface with a hopefully complete description of what service it provides for you. And then inside is an implementation that's hidden and nobody pays any attention to it on the outside. And if you have a system organized like that, you can actually reason about its correctness one module at a time. But in those days, people didn't know

[04:19.20–04:55.72; L124–L140] how um they couldn't figure out how to design systems that were modular. And the only kind of modularity mechanism present in programming languages was a procedure. And procedures didn't match the kinds of modules you needed. Because if you think about a file system or a database or you know, Amazon or whatever, you know, they they aren't a procedure where you put something in and get something out. They're a much more complicated thing. So, there was no notion of a module that sort of matched the kind of things that people were looking for.

[04:58.16–05:00.28; L141–L142] >> So, when you saw that problem, you know, what were the early solutions like?

[05:02.60–05:51.40; L143–L167] >> Well, so people were proposing modularity and they were talking about how important modularity was. They didn't exactly know what a module was. And so, it wasn't like they could give you a rule, this is a module. It was just a chunk of code. In fact, there were papers written that talked about how big a module should be or and stuff like that, just a chunk of code. That's not going to work because you need to design these systems. So, you need a way of thinking of a design that sort of fits into this notion of modularity. They also didn't really know what the rules should be for modularity. And um it turned out that in some of the early work I did after grad school when I was working at Mitre, um I had already invented a notion of modularity that was sort of more complete than what people had been talking about just because I had a small

[05:54.80–06:46.80; L168–L190] team of programmers. We were building a complicated system and I wanted to keep us out of trouble. And so I had that sort of sitting there when I started to work on this topic. Um, and it enabled me to see this idea of data abstraction all of a sudden. I sort of saw that this thing I had, this kind of modularity mechanism, which consisted of basically what I just described, a a a bunch of code providing you with an access through a number of what I called operations. So you could call it in various ways and then inside was all hidden and whatever data it was using was not accessible to the outside. And then at some point I saw I could see this as a data abstraction. It could be a set, it could be a sequence, it could be, you know, and so forth. And um, and that meant we had a new type of

[06:48.68–07:05.28; L191–L199] module. Now when I look back at the papers from the time, I see that idea is almost there except people hadn't managed to pick it out. And so it was probably I think this happens in science a lot. There's sort of a time when an idea is ready and I happened to see it.

[07:07.48–07:16.72; L200–L204] >> You pieced these together and you put it into the Clue programming language that you're working on. How did you see it influencing the industry?

[07:17.64–08:15.04; L205–L232] >> The first thing that happened was I wrote a paper with um, a a a a man who was a graduate student at MIT, Steve Zilles, about this idea of data abstraction and it sketched a notion of what abstract data types would be and how a programming language could support them. And this was a very um, is a very impactful paper. And so there was a a big impact on the research community. And then Clu came along and that involved a lot of additional research in the in the programming language area. The next thing that happened, so people were watching this in the research community, but of course people who are in companies that want to write programs, they need a programming language. And I decided I wasn't going to try and turn Clu into a product because that would have required working in a company. In those days you didn't just put software out on the

[08:16.52–09:00.24; L233–L253] internet and people used it. There wasn't an internet yet for one thing. And and I was much more interested in doing research than in you know, working in a company. So I put Clu on the side. It had a user base. But I it but for companies to use a programming language in those days, they wanted a company behind that language. The next thing that happened was the government uh put out a call for uh a programming language they could use. This led to the Ada programming language. That um so you know, that was already a big impact if you think about it. That there there was a language explicitly being uh designed to have data abstraction in it. And then finally in the '90s Java came along.

[09:03.48–09:14.60; L254–L260] >> I thought it'd be interesting cuz you you worked on Clu. You designed that programming language to ask you about other programming languages. You said somewhere that there's something wrong with Python and I was curious to hear your thoughts of why.

[09:16.36–10:16.68; L261–L287] >> Python has modules, but it doesn't have encapsulation. So it allows code on the outside to muck around with what's going on on the inside of a module. And that's all I was talking about. Encapsulation is a is a crucial part of making modularity work. And when you're building big programs, so you have many programmers working on them, your team is really only as strong as your weakest programmer. So, it's nice if the compiler can enforce things and make certain kinds of bad behavior not possible. I mean, Python is you know, has another intended use. It's helping naive programmers learn quickly how to write programs and stuff like that. And people in the programming language world do think about issues like this. Like, you know, how to make languages safer and so forth. But, since I stopped working in that area, I'm no longer an expert in programming languages.

[10:17.76–10:17.76; L288–L288] >> What got you into distributed computing?

[10:20.32–10:44.84; L289–L300] >> I read a paper by Bob Kahn, who was with then Cerf considered to be, you know, the founders of the internet. And Bob talked about um his dream of distributed computing, where you would have a program composed of pieces on different computers connected by a network. And nobody knew how to build those programs. And so, I just thought, great problem.

[10:46.49–10:46.49; L301–L301] >> [laughter]

[10:47.76–11:02.12; L302–L310] >> And [snorts] I was looking for a new problem, so I jumped into distributed computing. And the first project was actually a programming language to write distributed programs in. And and then I started looking at other problems in the distributed systems area.

[11:03.12–11:05.20; L311–L312] >> What was that first programming language that

[11:05.32–11:56.36; L313–L336] >> It was called Argus. It was It was very strongly influenced by Clu. It was an object-oriented language. Had a special kind of object called a guardian, which was a module sitting at a single computer. And then guardians could compute communicate through remote procedure calls. One of the things you run into in distributed computing um is if you have a computation that starts at one guardian and then makes use of other guardians at other nodes in the network, in the end, you want that computation to either complete entirely or have no effect at all. And how do you do that? Well, I borrowed the notion of transactions coming out of the database field. And that was part of how Argus worked. It ran computations as atomic transactions.

[11:57.80–12:00.20; L337–L338] >> Oh, interesting. Like distributed transactions across those nodes.

[12:03.20–12:30.68; L339–L351] >> And I think it led right into the work I did on um viewstamp replication, which was um that was the beginning of cloud storage. I was thinking in terms of a file system, but it doesn't really matter what it is. You know, how do you have data out on the internet stored at multiple sites with correct behavior and always accessible as long as enough nodes are up and running and the network is working.

[12:32.12–12:34.24; L352–L353] >> I see. And what is viewstamp in this context?

[12:35.44–12:51.40; L354–L361] >> Oh, that had to do with some details of how the system worked. And it was a way of noticing when some nodes failed and other nodes had to take over, you could figure out which ones had the most recent state in them, so you could pick up and not lose anything that had not had that had happened in the past.

[12:53.60–12:55.60; L362–L363] >> Uh what what if the clocks are out of sync? Like

[12:56.84–13:03.44; L364–L367] >> Uh it had nothing to do with clocks because it was just numbers. In other words, we were in view 25, the next view was 26. So

[13:05.44–13:07.68; L368–L369] >> Oh, okay. Just incrementing some numbers that are passed around.

[13:09.52–13:11.56; L370–L371] >> This reminds me a lot of uh Leslie Lamport's work.

[13:12.68–13:12.68; L372–L372] >> Actually, yes.

[13:14.40–13:14.40; L373–L373] >> Did you ever work with him or

[13:17.28–13:27.08; L374–L378] >> No. Leslie and I developed what is essentially the same idea independently. And he had the system he called Paxos and I had this thing called view stamp replication.

[13:28.56–13:31.68; L379–L380] >> Oh, interesting. And they're essentially the same thing.

[13:32.44–13:32.44; L381–L381] >> They are. Yeah.

[13:33.80–13:36.08; L382–L383] >> Oh, are there pros and cons of the two approaches?

[13:37.28–14:15.08; L384–L403] >> Yeah, I mean that when you do this kind of system, there's a lots of little details you can play around with. So, you could, you know, decide to do it it gets technical, but you know, there's tiny differences. But no, they're basically the same. In fact, what happened was uh the first time that I was aware of that this was actually used in a real system was when the Google file system came along. And one of my former students who was a I think he was a consultant at Google looked at what was going on in there and he said, "Oh, he says that's view stamp replication." So, the people at Google seemed to think it was Paxos, but in fact, they are the same system.

[14:17.60–14:32.96; L404–L411] >> I also noticed like um when you were uh when you came up with abstract data types maybe I mean maybe it's just cuz there wasn't the internet wasn't as, you know, wasn't there that there was also the object-oriented stuff going on on the West Coast.
