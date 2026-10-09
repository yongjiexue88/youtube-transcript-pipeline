Chunk 1; segments 1–345. 

# Creator of C++: Bell Labs, Negative Overhead Abstraction, Mistakes | Bjarne Stroustrup

Source ID: source-cf79d446a56a93e0
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Creator_of_C++_Bell_Labs,_Negative_Overhead_Abstraction,_Mistakes_Bjarne_Stroustrup_en.txt
Video: https://www.youtube.com/watch?v=U46fJ2bJ-co

[L10] [00:00.16] There wasn't a language in the world
[L11] [00:01.92] that could do what I needed.
[L12] [00:04.08] >> This is Bjestro, creator of C++, and we
[L13] [00:07.92] talked about his career starting with
[L14] [00:09.76] Bell Labs. What gave you the conviction
[L15] [00:12.48] to fly on your own tab?
[L16] [00:14.48] >> It was the best place in the world,
[L17] [00:16.40] right? I mean, do I need anymore?
[L18] [00:18.88] >> And I also asked him all about
[L19] [00:20.80] programming language design. What was
[L20] [00:23.04] the most technically challenging part to
[L21] [00:25.44] implement? Everybody asks that question
[L22] [00:28.16] and I think it's a wrong question.
[L23] [00:30.48] >> But I tend to think that more [music]
[L24] [00:32.24] abstraction costs you something.
[L25] [00:33.92] >> It's not the case. We can do negative
[L26] [00:36.08] overhead abstraction.
[L27] [00:38.40] >> Is there any part [music] where you
[L28] [00:40.40] think, "Oh, that that was a mistake.
[L29] [00:42.32] >> I should have fought harder for that."
[L30] [00:44.72] >> Here's the full episode. [music]
[L31] [00:50.88] >> What is the origin story behind C++?
[L32] [00:54.56] Well, let's start from the real
[L33] [00:57.12] beginning. I got a job at Bell Labs,
[L34] [00:59.68] which is a really great place over in
[L35] [01:01.92] New Jersey. It's not like that anymore,
[L36] [01:05.36] but at the time it was the best applied
[L37] [01:08.88] math, applied engineering uh place in
[L38] [01:12.24] the world. I I looked around, you know,
[L39] [01:14.96] the great people who were there. They
[L40] [01:17.36] built Unix, they built C, they did a lot
[L41] [01:22.16] of uh the theory behind it. And I
[L42] [01:26.00] realized I had to do something important
[L43] [01:28.96] otherwise I didn't belong. So uh I
[L44] [01:31.84] decided I was going to build a
[L45] [01:34.08] distributed Unix because it was clear
[L46] [01:37.12] that computers were getting better,
[L47] [01:39.76] networking was getting better. So we we
[L48] [01:42.48] we we need some of those one of those.
[L49] [01:45.68] And uh if I had succeeded it would we
[L50] [01:50.08] would have had Unix clusters 10 years
[L51] [01:52.48] earlier or something like that. But of
[L52] [01:54.96] course I couldn't do it. That's not a
[L53] [01:56.96] oneperson job. But the first thing I
[L54] [02:00.08] realized was I there wasn't a language
[L55] [02:02.80] in the world that could do what I
[L56] [02:04.48] needed. It needed two things. Low-level
[L57] [02:08.96] uh access to hardware. So to memory
[L58] [02:11.84] managers, process uh implementations,
[L59] [02:15.44] process scheduleuler, network drivers,
[L60] [02:18.72] uh device drivers, all that kind of
[L61] [02:21.44] stuff. And then it needed highle things.
[L62] [02:24.40] It says, well, there's a module here and
[L63] [02:27.36] this computer and there's a module there
[L64] [02:29.44] and that computer and uh here's a the
[L65] [02:34.00] communication protocol they're using and
[L66] [02:36.80] things like that. And there's lots of
[L67] [02:39.20] languages that could do either. None
[L68] [02:41.92] that could do both. The obvious language
[L69] [02:44.48] for the low-level stuff was C because
[L70] [02:47.68] well Dennis Richie and Brian Kernan was
[L71] [02:50.00] down the the hall and [snorts] I said
[L72] [02:53.60] distributed Unix because I was in the
[L73] [02:56.88] home where Unix was invented and still
[L74] [03:00.48] being built.
[L75] [03:02.56] And for the high level languages there
[L76] [03:04.88] was a fair number but they were all too
[L77] [03:07.68] slow and they couldn't manipulate
[L78] [03:09.44] hardware. But I had uh learned to use
[L79] [03:14.00] simul. I knew question and yandal that
[L80] [03:18.40] uh invented object-oriented programming
[L81] [03:20.64] and similar. And so I decided I had to
[L82] [03:24.88] merge these two. And the way that was
[L83] [03:28.88] practical was to take the class concept
[L84] [03:32.00] from
[L85] [03:33.60] um from simula and stick it into C so
[L86] [03:36.88] that it could run much much faster and
[L87] [03:39.28] be used for systems programming.
[L88] [03:42.16] And at the same time I made the type
[L89] [03:46.00] system a bit more regular. user defined
[L90] [03:48.56] types classes uh was handled the same
[L91] [03:52.72] way as built-in types and that's
[L92] [03:56.40] basically the start of what neither
[L93] [03:59.04] scene nor simul could do which gets us
[L94] [04:02.16] to generic programming eventually many
[L95] [04:05.20] years later uh I had to add overloading
[L96] [04:09.44] I mean we have always had overloading
[L97] [04:11.92] you can you can add to uh integers you
[L98] [04:14.88] can add to uh floating point numbers.
[L99] [04:17.92] You can add a floatingoint number to an
[L100] [04:20.00] integer with a plus. That's a single uh
[L101] [04:23.84] uh name, right? And so I had to
[L102] [04:26.16] generalize that to be able to have
[L103] [04:28.16] unique set of rules for both built-in
[L104] [04:31.04] and userdefined types. So that's where
[L105] [04:34.72] it came from.
[L106] [04:36.24] >> In one of the lectures that I saw that
[L107] [04:38.24] you gave, you talked about uh rewriting
[L108] [04:41.84] a simulator in BCPL. Is that the
[L109] [04:44.48] distributed Unix work or
[L110] [04:46.56] >> No, no, that's before that. I went to
[L111] [04:49.92] Cambridge, England to get a PhD
[L112] [04:53.28] and uh at some point I decided I needed
[L113] [04:59.20] a simulator or software on a distributed
[L114] [05:03.44] system um to to do the the PhD work on
[L115] [05:09.52] uh distributed systems.
[L116] [05:12.24] And of course the idea of a distributed
[L117] [05:15.20] Unix uh three or four years later came
[L118] [05:19.28] out of the same way of thinking. But um
[L119] [05:23.12] what I did was I wrote a really nice
[L120] [05:25.28] simulator in [snorts]
[L121] [05:27.12] uh Simula. Simula is very good at that.
[L122] [05:29.84] It's misnamed because it was a general
[L123] [05:31.84] purpose programming language and it's
[L124] [05:34.64] having a bad name didn't help it at all.
[L125] [05:37.84] But anyway, I wrote this simulator and I
[L126] [05:40.64] wrote little examples, test cases, etc.,
[L127] [05:44.24] etc. It all worked nicely. Then I tried
[L128] [05:47.36] the first real run um full scale and I
[L129] [05:53.92] took the department's uh mainframe and
[L130] [05:58.56] used it for a very significant time.
[L131] [06:03.04] and well PhD students can't do that. Um
[L132] [06:08.24] that's the chemists and the
[L133] [06:10.08] astrophysicists and such would never
[L134] [06:12.72] accept it. So I was kicked off the
[L135] [06:14.88] machine. Uh and it was clear that simul
[L136] [06:18.96] could write I could write the program in
[L137] [06:21.20] simul
[L138] [06:22.72] but I couldn't afford to run it. So I
[L139] [06:26.08] took the ideas and I moved it to a
[L140] [06:29.20] little used experimental computer which
[L141] [06:32.00] was the CAP computer which had hardware
[L142] [06:34.88] protection and uh capabilities and great
[L143] [06:38.16] stuff for uh hardware and it was
[L144] [06:41.92] somewhat unusual. So the astrophysicists
[L145] [06:44.72] couldn't use it. They they weren't
[L146] [06:47.92] computer scientists as such but but I
[L147] [06:51.12] could. And so the only problem was I
[L148] [06:55.36] couldn't run Simula there because Simul
[L149] [06:59.92] uh was never ported on that kind of
[L150] [07:02.16] machine and it was being used on
[L151] [07:05.20] mainframes and it was proprietary and
[L152] [07:08.56] everything was wrong in the context of
[L153] [07:11.04] the cabin computer. So I basically
[L154] [07:15.52] rewrote my simulator in BCPL
[L155] [07:20.08] and BCPL is a language that will make C
[L156] [07:23.84] look like a highle language
[L157] [07:26.48] and like like it has only one data type
[L158] [07:29.84] the word
[L159] [07:31.84] and um it was a very painful exercise
[L160] [07:36.32] but once I done it my program ran uh I
[L161] [07:40.88] guesstimated about 50 times faster.
[L162] [07:42.80] faster
[L163] [07:44.40] and um I got my data and I got my PhD.
[L164] [07:49.44] So that was good. But I was convinced I
[L165] [07:53.12] would never again attempt a problem
[L166] [07:57.68] with tools that inadequate
[L167] [08:01.28] as I had uh tried it on the main frame
[L168] [08:05.28] in uh Cambridge.
[L169] [08:07.76] And so I I had a list of things that my
[L170] [08:11.44] ideal language should have and well C++
[L171] [08:16.72] simul didn't have all of that but it
[L172] [08:19.68] came closer than any other language that
[L173] [08:22.56] existed. C++ came out of there.
[L174] [08:25.60] >> Yeah. In in that lecture you you said
[L175] [08:27.76] something like that writing that program
[L176] [08:30.16] in BCPL was so difficult you lost half
[L177] [08:33.60] your hair debugging. That's um almost
[L178] [08:37.92] exactly true and I lost the other half
[L179] [08:40.80] getting C++ going but over the years but
[L180] [08:45.28] um anyway it worked.
[L181] [08:47.04] >> You mentioned Bell Labs and I think
[L182] [08:49.12] there's a lot of curiosity about that
[L183] [08:52.16] topic just because it's such a legendary
[L184] [08:54.16] place. when you had graduated um from
[L185] [08:57.12] your PhD and you were thinking about
[L186] [08:59.52] where to work socially, what was what
[L187] [09:02.72] was Bell Labs known as at that time?
[L188] [09:05.12] Bell Labs was the place to go if you
[L189] [09:07.68] wanted to do practical engineering
[L190] [09:10.80] at a large scale at sort of world class
[L191] [09:15.52] and I think it was easily the best. I
[L192] [09:19.20] mean, we probably had twice as many
[L193] [09:22.16] computer scientists as MIT at the time,
[L194] [09:25.68] things like that. And the computer
[L195] [09:28.40] science research center had uh great
[L196] [09:32.24] people
[L197] [09:33.84] and
[L198] [09:35.52] some of them had come from um from
[L199] [09:39.28] Cambridge. Um
[L200] [09:42.48] and um one day in my last year in
[L201] [09:46.96] Cambridge uh one of the people from Bill
[L202] [09:49.92] Labs came along along to give a talk and
[L203] [09:54.00] give a talk and the uh tradition in
[L204] [09:57.60] England and in the computer lab is after
[L205] [10:01.04] um a day's work you go to the pub and
[L206] [10:03.68] you uh chat with other people to see
[L207] [10:06.48] what has been going on. And he says,
[L208] [10:09.04] "Well, when you need a job, give us a
[L209] [10:12.32] buzz." And so I did. And I
[L210] [10:17.04] flew over to uh New Jersey on on my own
[L211] [10:21.36] tab actually. And my later boss, Sandy
[L212] [10:25.36] Fraser, great guy uh working with
[L213] [10:28.16] networking,
[L214] [10:29.68] um told me that I'd come at a wrong
[L215] [10:32.00] time. They didn't have any jobs.
[L216] [10:34.70] >> [snorts]
[L217] [10:34.72] >> This is not what you want to hear when
[L218] [10:36.48] you've just flown over the Atlantic.
[L219] [10:39.12] Anyway, the next day I gave a talk um to
[L220] [10:42.48] a development group, not the research
[L221] [10:44.32] group, and then they changed their minds
[L222] [10:47.52] and took me up to the research group and
[L223] [10:50.00] I worked there for for the next couple
[L224] [10:52.80] of decades.
[L225] [10:54.00] >> What was the interview process like?
[L226] [10:56.40] >> You just talked to some people. I mean
[L227] [11:00.56] um I I remember having a a longish chat
[L228] [11:04.72] with Dennis Chief for instance and I I
[L229] [11:08.40] talked to people doing networking mostly
[L230] [11:12.24] there there wasn't a
[L231] [11:15.20] interview process as such uh they hadn't
[L232] [11:18.64] actually hired anybody new for 5 years
[L233] [11:22.32] so um no they just did it by the seat of
[L234] [11:26.40] the pants
[L235] [11:27.84] >> so it's kind of like the the uh belief
[L236] [11:31.44] and credibility that other people say
[L237] [11:34.24] that you have like Dennis Richie talked
[L238] [11:36.24] to you and that he knew that you knew
[L239] [11:38.40] what you're talking
[L240] [11:39.60] >> Sandy Fraser and such they they just uh
[L241] [11:43.04] talk to you and see what you know and
[L242] [11:45.04] don't know and uh at the end they they
[L243] [11:48.80] go to the director and says in this case
[L244] [11:51.68] we've got a good guy can you give us a
[L245] [11:54.72] let us let us have him I of course
[L246] [11:57.52] didn't know anything about that. I
[L247] [11:59.12] wasn't there. I was out talking to
[L248] [12:01.76] somebody in California and I get a phone
[L249] [12:03.84] call from the director and says, "Uh,
[L250] [12:05.92] would you like to come and work here a
[L251] [12:08.32] week later?"
[L252] [12:10.32] What gave you the conviction to fly on
[L253] [12:12.80] your own tab to go and you there wasn't
[L254] [12:16.24] even a promise of a job yet?
[L255] [12:17.76] >> No. Well, it was the best place in the
[L256] [12:21.12] world, right? I mean, do you need any
[L257] [12:23.36] more?
[L258] [12:25.60] it I mean if it worked it was the best
[L259] [12:28.64] and if it didn't work so what I mean you
[L260] [12:32.96] can't succeed at everything today
[L261] [12:36.40] there's more industries has a stronger
[L262] [12:38.88] pull at that time would it have been IBM
[L263] [12:41.84] or something that would have been the
[L264] [12:42.96] best industry
[L265] [12:43.68] >> I talked to IBM they weren't as good as
[L266] [12:46.00] the bill labs computer science research
[L267] [12:48.00] center I was up at Yorktown heights and
[L268] [12:51.28] I talked to the researchers and I talked
[L269] [12:54.40] to to the young uh researchers and I
[L270] [12:59.12] just didn't think they were doing the
[L271] [13:00.80] right stuff
[L272] [13:02.72] and and not in the right way and they
[L273] [13:05.12] were much more controlled and directed
[L274] [13:08.40] than the uh researchers at Bell Labs.
[L275] [13:13.04] >> At a place like Bell Labs, how does
[L276] [13:15.76] project selection go? Like how does how
[L277] [13:18.72] does all that work once you're employed?
[L278] [13:20.72] Oh um at the time and I think still
[L279] [13:25.44] there there are two philosophies about
[L280] [13:27.28] how to get good research. The one is
[L281] [13:30.32] that you have a well-designed project uh
[L282] [13:34.96] chosen carefully by uh management and
[L283] [13:38.24] higher management uh seriously funded
[L284] [13:42.00] and maybe you do uh put 20 or 30 people
[L285] [13:46.48] at the problem and you solve it and you
[L286] [13:48.96] have something great. [snorts]
[L287] [13:51.36] Um, the other [clears throat] philosophy
[L288] [13:53.36] is you hire the best people you can find
[L289] [13:56.96] and don't tell them what to do. Um, I
[L290] [14:00.80] mean, my job was described as do
[L291] [14:05.20] something interesting
[L292] [14:07.76] in a year's time. Tell us what it you
[L293] [14:10.64] did
[L294] [14:12.48] and if we like it, um, we'll extend
[L295] [14:16.72] we'll give you the same uh, deal next
[L296] [14:18.80] year. And by the way, um the way you
[L297] [14:23.44] tell us you write one sheet of paper uh
[L298] [14:27.36] using more than nine uh nine point font
[L299] [14:30.72] or or more because you if you can't say
[L300] [14:33.92] what you did in fairly briefly uh you
[L301] [14:37.12] probably haven't done something
[L302] [14:38.88] interesting enough
[L303] [14:41.44] >> very unusual. So there um they were
[L304] [14:46.00] actually worrying when they built Unix
[L305] [14:48.24] because it eventually involved five or
[L306] [14:50.88] seven people
[L307] [14:52.96] and it was getting too big for for for
[L308] [14:56.48] that model of the world of individuals
[L309] [14:59.84] doing interesting things.
[L310] [15:03.28] Very different. Uh I would say that on
[L311] [15:06.08] average this fairly anarchic uh
[L312] [15:09.44] organization
[L313] [15:11.36] uh did better than the well organized
[L314] [15:14.88] thing. Most of the things you've heard
[L315] [15:16.96] of from Bell Labs uh came out of out
[L316] [15:20.28] [snorts] of there and then in other part
[L317] [15:23.04] of the building they were doing hardware
[L318] [15:25.68] things. So fibers as we use them today
[L319] [15:30.32] uh came out of there. A lot of the
[L320] [15:32.64] wireless technology came out of there.
[L321] [15:36.16] Um the uh charge coupled devices that
[L322] [15:39.52] are our cameras came out of there. Uh
[L323] [15:43.12] they they tried to do video phones and
[L324] [15:46.16] couldn't get it to work because well
[L325] [15:48.32] hardware hadn't grown up to it but they
[L326] [15:51.12] were trying to do it. Um the system of
[L327] [15:53.92] cells for cell phones came out of not
[L328] [15:58.00] that building but another building for
[L329] [16:00.00] Bell Labs. It's it was just a great
[L330] [16:02.40] place. And so the computer science
[L331] [16:05.52] people tended to talk to people doing
[L332] [16:07.60] other things. So I remember when I was
[L333] [16:11.12] doing simulations,
[L334] [16:13.20] I was helping somebody uh building a
[L335] [16:15.60] simulator for some networking stuff. Uh
[L336] [16:18.96] a lot of early C++ had to do with uh
[L337] [16:23.12] doing things like what happens when a
[L338] [16:25.12] network get overloaded? how do we handle
[L339] [16:27.12] the overload protocols?
[L340] [16:30.16] And in this particular case, they did a
[L341] [16:32.24] a good job and they called me back and
[L342] [16:36.08] um they had a slightly bigger problem.
[L343] [16:39.04] They wanted to simulate the computer
[L344] [16:43.44] traffic of Manhattan.
[L345] [16:45.92] Even then my answer was no. We don't
[L346] [16:50.08] have the compute power to do that. Uh,
[L347] [16:53.92] it doesn't matter how good C++ is, the
[L348] [16:57.92] computers of today can't do it.
[L349] [17:02.40] >> That back then though, but now now they
[L350] [17:05.44] probably could, but of course the
[L351] [17:07.92] computer traffic has become uh much
[L352] [17:10.72] more. So maybe they can't. I don't know.
[L353] [17:13.52] I don't have the numbers now. Then I
[L354] [17:16.08] they gave me the numbers. That was why I
