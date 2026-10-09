# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup
Source: source-cf79d446a56a93e0 | Chunk 1 of 7
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.16–00:01.92; L10–L11] There wasn't a language in the world that could do what I needed.

[00:04.08–00:12.48; L12–L15] >> This is Bjestro, creator of C++, and we talked about his career starting with Bell Labs. What gave you the conviction to fly on your own tab?

[00:14.48–00:16.40; L16–L17] >> It was the best place in the world, right? I mean, do I need anymore?

[00:18.88–00:28.16; L18–L22] >> And I also asked him all about programming language design. What was the most technically challenging part to implement? Everybody asks that question and I think it's a wrong question.

[00:30.48–00:32.24; L23–L24] >> But I tend to think that more [music] abstraction costs you something.

[00:33.92–00:36.08; L25–L26] >> It's not the case. We can do negative overhead abstraction.

[00:38.40–00:40.40; L27–L28] >> Is there any part [music] where you think, "Oh, that that was a mistake.

[00:42.32–00:42.32; L29–L29] >> I should have fought harder for that."

[00:44.72–00:44.72; L30–L30] >> Here's the full episode. [music]

[00:50.88–01:54.96; L31–L52] >> What is the origin story behind C++? Well, let's start from the real beginning. I got a job at Bell Labs, which is a really great place over in New Jersey. It's not like that anymore, but at the time it was the best applied math, applied engineering uh place in the world. I I looked around, you know, the great people who were there. They built Unix, they built C, they did a lot of uh the theory behind it. And I realized I had to do something important otherwise I didn't belong. So uh I decided I was going to build a distributed Unix because it was clear that computers were getting better, networking was getting better. So we we we we need some of those one of those. And uh if I had succeeded it would we would have had Unix clusters 10 years earlier or something like that. But of course I couldn't do it. That's not a

[01:56.96–03:07.68; L53–L77] oneperson job. But the first thing I realized was I there wasn't a language in the world that could do what I needed. It needed two things. Low-level uh access to hardware. So to memory managers, process uh implementations, process scheduleuler, network drivers, uh device drivers, all that kind of stuff. And then it needed highle things. It says, well, there's a module here and this computer and there's a module there and that computer and uh here's a the communication protocol they're using and things like that. And there's lots of languages that could do either. None that could do both. The obvious language for the low-level stuff was C because well Dennis Richie and Brian Kernan was down the the hall and [snorts] I said distributed Unix because I was in the home where Unix was invented and still being built. And for the high level languages there was a fair number but they were all too slow and they couldn't manipulate

[03:09.44–04:20.00; L78–L100] hardware. But I had uh learned to use simul. I knew question and yandal that uh invented object-oriented programming and similar. And so I decided I had to merge these two. And the way that was practical was to take the class concept from um from simula and stick it into C so that it could run much much faster and be used for systems programming. And at the same time I made the type system a bit more regular. user defined types classes uh was handled the same way as built-in types and that's basically the start of what neither scene nor simul could do which gets us to generic programming eventually many years later uh I had to add overloading I mean we have always had overloading you can you can add to uh integers you can add to uh floating point numbers. You can add a floatingoint number to an integer with a plus. That's a single uh

[04:23.84–04:34.72; L101–L105] uh name, right? And so I had to generalize that to be able to have unique set of rules for both built-in and userdefined types. So that's where it came from.

[04:36.24–04:44.48; L106–L109] >> In one of the lectures that I saw that you gave, you talked about uh rewriting a simulator in BCPL. Is that the distributed Unix work or

[04:46.56–06:03.04; L110–L131] >> No, no, that's before that. I went to Cambridge, England to get a PhD and uh at some point I decided I needed a simulator or software on a distributed system um to to do the the PhD work on uh distributed systems. And of course the idea of a distributed Unix uh three or four years later came out of the same way of thinking. But um what I did was I wrote a really nice simulator in [snorts] uh Simula. Simula is very good at that. It's misnamed because it was a general purpose programming language and it's having a bad name didn't help it at all. But anyway, I wrote this simulator and I wrote little examples, test cases, etc., etc. It all worked nicely. Then I tried the first real run um full scale and I took the department's uh mainframe and used it for a very significant time. and well PhD students can't do that. Um

[06:08.24–07:23.84; L132–L156] that's the chemists and the astrophysicists and such would never accept it. So I was kicked off the machine. Uh and it was clear that simul could write I could write the program in simul but I couldn't afford to run it. So I took the ideas and I moved it to a little used experimental computer which was the CAP computer which had hardware protection and uh capabilities and great stuff for uh hardware and it was somewhat unusual. So the astrophysicists couldn't use it. They they weren't computer scientists as such but but I could. And so the only problem was I couldn't run Simula there because Simul uh was never ported on that kind of machine and it was being used on mainframes and it was proprietary and everything was wrong in the context of the cabin computer. So I basically rewrote my simulator in BCPL and BCPL is a language that will make C look like a highle language

[07:26.48–08:22.56; L157–L173] and like like it has only one data type the word and um it was a very painful exercise but once I done it my program ran uh I guesstimated about 50 times faster. faster and um I got my data and I got my PhD. So that was good. But I was convinced I would never again attempt a problem with tools that inadequate as I had uh tried it on the main frame in uh Cambridge. And so I I had a list of things that my ideal language should have and well C++ simul didn't have all of that but it came closer than any other language that existed. C++ came out of there.

[08:25.60–08:45.28; L174–L180] >> Yeah. In in that lecture you you said something like that writing that program in BCPL was so difficult you lost half your hair debugging. That's um almost exactly true and I lost the other half getting C++ going but over the years but um anyway it worked.

[08:47.04–09:57.60; L181–L204] >> You mentioned Bell Labs and I think there's a lot of curiosity about that topic just because it's such a legendary place. when you had graduated um from your PhD and you were thinking about where to work socially, what was what was Bell Labs known as at that time? Bell Labs was the place to go if you wanted to do practical engineering at a large scale at sort of world class and I think it was easily the best. I mean, we probably had twice as many computer scientists as MIT at the time, things like that. And the computer science research center had uh great people and some of them had come from um from Cambridge. Um and um one day in my last year in Cambridge uh one of the people from Bill Labs came along along to give a talk and give a talk and the uh tradition in England and in the computer lab is after

[10:01.04–10:32.00; L205–L215] um a day's work you go to the pub and you uh chat with other people to see what has been going on. And he says, "Well, when you need a job, give us a buzz." And so I did. And I flew over to uh New Jersey on on my own tab actually. And my later boss, Sandy Fraser, great guy uh working with networking, um told me that I'd come at a wrong time. They didn't have any jobs.

[10:34.70–10:34.70; L216–L216] >> [snorts]

[10:34.72–10:52.80; L217–L224] >> This is not what you want to hear when you've just flown over the Atlantic. Anyway, the next day I gave a talk um to a development group, not the research group, and then they changed their minds and took me up to the research group and I worked there for for the next couple of decades.

[10:54.00–10:54.00; L225–L225] >> What was the interview process like?

[10:56.40–11:26.40; L226–L234] >> You just talked to some people. I mean um I I remember having a a longish chat with Dennis Chief for instance and I I talked to people doing networking mostly there there wasn't a interview process as such uh they hadn't actually hired anybody new for 5 years so um no they just did it by the seat of the pants

[11:27.84–11:38.40; L235–L239] >> so it's kind of like the the uh belief and credibility that other people say that you have like Dennis Richie talked to you and that he knew that you knew what you're talking

[11:39.60–12:16.24; L240–L254] >> Sandy Fraser and such they they just uh talk to you and see what you know and don't know and uh at the end they they go to the director and says in this case we've got a good guy can you give us a let us let us have him I of course didn't know anything about that. I wasn't there. I was out talking to somebody in California and I get a phone call from the director and says, "Uh, would you like to come and work here a week later?" What gave you the conviction to fly on your own tab to go and you there wasn't even a promise of a job yet?

[12:17.76–12:42.96; L255–L264] >> No. Well, it was the best place in the world, right? I mean, do you need any more? it I mean if it worked it was the best and if it didn't work so what I mean you can't succeed at everything today there's more industries has a stronger pull at that time would it have been IBM or something that would have been the best industry

[12:43.68–13:08.40; L265–L274] >> I talked to IBM they weren't as good as the bill labs computer science research center I was up at Yorktown heights and I talked to the researchers and I talked to to the young uh researchers and I just didn't think they were doing the right stuff and and not in the right way and they were much more controlled and directed than the uh researchers at Bell Labs.

[13:13.04–14:23.44; L275–L297] >> At a place like Bell Labs, how does project selection go? Like how does how does all that work once you're employed? Oh um at the time and I think still there there are two philosophies about how to get good research. The one is that you have a well-designed project uh chosen carefully by uh management and higher management uh seriously funded and maybe you do uh put 20 or 30 people at the problem and you solve it and you have something great. [snorts] Um, the other [clears throat] philosophy is you hire the best people you can find and don't tell them what to do. Um, I mean, my job was described as do something interesting in a year's time. Tell us what it you did and if we like it, um, we'll extend we'll give you the same uh, deal next year. And by the way, um the way you tell us you write one sheet of paper uh

[14:27.36–14:38.88; L298–L302] using more than nine uh nine point font or or more because you if you can't say what you did in fairly briefly uh you probably haven't done something interesting enough

[14:41.44–15:51.12; L303–L326] >> very unusual. So there um they were actually worrying when they built Unix because it eventually involved five or seven people and it was getting too big for for for that model of the world of individuals doing interesting things. Very different. Uh I would say that on average this fairly anarchic uh organization uh did better than the well organized thing. Most of the things you've heard of from Bell Labs uh came out of out [snorts] of there and then in other part of the building they were doing hardware things. So fibers as we use them today uh came out of there. A lot of the wireless technology came out of there. Um the uh charge coupled devices that are our cameras came out of there. Uh they they tried to do video phones and couldn't get it to work because well hardware hadn't grown up to it but they were trying to do it. Um the system of

[15:53.92–16:57.92; L327–L348] cells for cell phones came out of not that building but another building for Bell Labs. It's it was just a great place. And so the computer science people tended to talk to people doing other things. So I remember when I was doing simulations, I was helping somebody uh building a simulator for some networking stuff. Uh a lot of early C++ had to do with uh doing things like what happens when a network get overloaded? how do we handle the overload protocols? And in this particular case, they did a a good job and they called me back and um they had a slightly bigger problem. They wanted to simulate the computer traffic of Manhattan. Even then my answer was no. We don't have the compute power to do that. Uh, it doesn't matter how good C++ is, the computers of today can't do it.

[17:02.40–17:16.08; L349–L354] >> That back then though, but now now they probably could, but of course the computer traffic has become uh much more. So maybe they can't. I don't know. I don't have the numbers now. Then I they gave me the numbers. That was why I
