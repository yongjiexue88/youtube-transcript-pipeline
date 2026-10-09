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
[L355] [17:19.28] I declined to to to help them because it
[L356] [17:23.28] was impossible.
[L357] [17:24.80] >> I saw somewhere when I was doing
[L358] [17:26.72] research that you you said you had
[L359] [17:28.88] gotten lunch with Dennis Richie once a
[L360] [17:32.08] week for like 16 years or something like
[L361] [17:34.16] that.
[L362] [17:35.20] >> Um and you know he's uh also a very
[L363] [17:38.24] legendary name. And I was curious, you
[L364] [17:40.56] know, if there's anything that you you
[L365] [17:43.12] learned from him or anything that
[L366] [17:44.56] impressed you about him that maybe
[L367] [17:46.80] influenced you or C++.
[L368] [17:49.36] >> He was a great guy and we talked about a
[L369] [17:51.44] lot of things. He never said anything uh
[L370] [17:55.52] rude or or negative about um C++.
[L371] [17:59.60] Actually, in his Hubble paper, he points
[L372] [18:01.92] to C++ as the obvious successor to C.
[L373] [18:07.12] Um, so all of these
[L374] [18:10.72] C versus C++ language wars are
[L375] [18:13.84] ridiculous.
[L376] [18:15.36] Um, they should never have happened and
[L377] [18:18.16] they certainly didn't happen uh because
[L378] [18:21.76] well I I knew Dennis. We we were not
[L379] [18:24.96] fighting. Um I still know Brian Kernan.
[L380] [18:28.80] I was talking to him this Friday. Um
[L381] [18:33.84] we're good friends and uh yeah language
[L382] [18:37.76] walls are are silly. Um Dennis helped me
[L383] [18:42.32] uh design const for instance for uh C++.
[L384] [18:46.80] It used to be called read only and write
[L385] [18:48.96] only but uh the C guys couldn't handle
[L386] [18:52.00] two words and they were too long. Um so
[L387] [18:56.32] we we got what we got but that's one
[L388] [18:59.36] specific thing I remember. Dennis uh
[L389] [19:03.20] being helpful with uh he was a bit
[L390] [19:06.08] worried that about
[L391] [19:09.60] overloading because you had to look at
[L392] [19:12.56] the
[L393] [19:14.88] de declarations of functions uh before
[L394] [19:18.32] you knew what the meaning of a call was.
[L395] [19:21.28] Um but that's a very eable way of
[L396] [19:24.88] thinking. It's just happens that it it
[L397] [19:28.24] works and anybody who writes C today are
[L398] [19:33.52] using my handiwork essentially all of
[L399] [19:36.48] the time because the the modern syntax
[L400] [19:40.72] for function definitions and function
[L401] [19:43.20] declarations
[L402] [19:44.72] and the call semantics uh came out of
[L403] [19:48.40] the early um C++ early classes work of
[L404] [19:53.60] mine. So when when people start ranting
[L405] [19:57.20] um they they they should remember that
[L406] [19:59.68] they're actually doing my using my
[L407] [20:01.52] handiwork every day. [laughter]
[L408] [20:04.80] >> You had written these uh uh almost like
[L409] [20:08.16] historical accountings of the history of
[L410] [20:10.16] C++ like maybe three really long papers
[L411] [20:13.92] um I think for some conference I forgot
[L412] [20:16.08] the exact and so in there there was one
[L413] [20:19.60] anecdote about Dennis Richie. It was it
[L414] [20:22.88] was about this this concept where he
[L415] [20:25.44] proposed uh to the C standard committee
[L416] [20:28.08] this idea of a fat pointer where it uh
[L417] [20:31.76] you know also has it it stores its size
[L418] [20:34.40] as well and you mentioned the C
[L419] [20:37.12] committee didn't approve and I was
[L420] [20:38.40] curious if you could like tell that
[L421] [20:40.80] >> um
[L422] [20:42.64] so Dennis did see but he didn't take
[L423] [20:46.64] part in the standards committee and I've
[L424] [20:49.20] even heard people from the C standards
[L425] [20:51.52] committees He says, "No, Dennis isn't a
[L426] [20:53.84] C expert. He's not ever come to
[L427] [20:56.48] meetings."
[L428] [20:58.48] Um, very strange attitude, but anyway,
[L429] [21:03.12] um, we knew the problem about um about
[L430] [21:08.88] buffer overflow and range errors. And
[L431] [21:11.20] the obvious solution is to use what
[L432] [21:14.72] Dennis called a fat pointer which is a
[L433] [21:17.52] pointer with its number of elements it
[L434] [21:21.84] points to attached to it. But that's two
[L435] [21:25.20] words and uh that's probably no that is
[L436] [21:29.44] why it wasn't used on the early se uh
[L437] [21:32.96] because then they had 48k of memory and
[L438] [21:37.60] when when I had this discussion with
[L439] [21:39.44] Dennis I think we had a whole megabyte
[L440] [21:42.72] um and when I started with C++ we had
[L441] [21:46.32] 256
[L442] [21:47.84] kilobytes and I knew that uh we we were
[L443] [21:52.48] going to get um get a megabyte and and
[L444] [21:56.72] we were talking about it and he he
[L445] [21:58.40] called them fat pointers and today in
[L446] [22:01.84] C++ they're called span and um the span
[L447] [22:06.24] came out of uh my work with others on
[L448] [22:09.76] the C++ core guidelines and we needed
[L449] [22:13.68] something like that we couldn't provide
[L450] [22:16.40] the degree of control and safety that uh
[L451] [22:19.60] we needed so we built span and it came
[L452] [22:23.36] into the standard a bit later.
[L453] [22:26.64] But some of these ideas are very old.
[L454] [22:30.40] >> When you put together really impressive
[L455] [22:32.96] people like you know the world's
[L456] [22:34.80] greatest people that you look around and
[L457] [22:37.76] you see how great the other people are
[L458] [22:39.92] and even though each individual is great
[L459] [22:43.36] just the greatness of others can give
[L460] [22:45.28] people this feeling of imposter syndrome
[L461] [22:47.44] that's not necessarily founded. Is that
[L462] [22:49.92] something that you ever felt or saw at
[L463] [22:52.00] >> Bell? Definitely. Um maybe I still got a
[L464] [22:55.76] bit of it, but certainly when I came to
[L465] [22:58.16] Bell Labs and saw the names on the doors
[L466] [23:00.80] and I'd read the papers and it created
[L467] [23:04.24] the fields I like to work in. Yeah. I I
[L468] [23:08.32] thought I have to up my game. I have to
[L469] [23:11.20] do something uh bigger and better than
[L470] [23:15.12] what I had imagined. Um also you talk to
[L471] [23:19.12] them and you learn things. I mean, I
[L472] [23:21.52] learned a lot over lunch where there's a
[L473] [23:24.48] bunch of them uh talking about what
[L474] [23:28.00] they're doing and why they are doing it.
[L475] [23:31.20] There are some places that that has that
[L476] [23:34.16] effect on on people and has this density
[L477] [23:37.68] of talent. Um Cambridge University was
[L478] [23:42.00] computer science was one of those
[L479] [23:43.76] places. I learned a lot there and u the
[L480] [23:47.28] doors were always open. Uh it was sort
[L481] [23:51.12] of almost a policy uh that we kept the
[L482] [23:54.80] doors open because how else would people
[L483] [23:59.28] be able to come and and talk?
[L484] [24:02.32] >> When we talk about a programming
[L485] [24:04.24] language and just generally like
[L486] [24:06.16] language design, if I was to want to
[L487] [24:09.04] build a programming language today, what
[L488] [24:12.00] are all the pieces that you'd need to to
[L489] [24:14.88] build to make a programming language?
[L490] [24:17.76] Well, that's a relatively easy
[L491] [24:22.80] question to answer and everybody asks
[L492] [24:25.84] that question and I think it's a wrong
[L493] [24:28.16] question. Uh what you need is a problem
[L494] [24:31.76] that needs a solution. A lot of people
[L495] [24:35.04] just want to build a language that is
[L496] [24:37.52] better that at what they are doing now
[L497] [24:40.72] and what they particularly are doing.
[L498] [24:43.76] And most of the time that can be done
[L499] [24:47.04] reasonably well with existing languages.
[L500] [24:50.40] And
[L501] [24:52.00] if you build a very specialized language
[L502] [24:54.96] that's fine. But if we're talking about
[L503] [24:57.28] more general purpose languages,
[L504] [24:59.92] uh you you're then building something
[L505] [25:02.24] that when you want to work with somebody
[L506] [25:04.88] else, it's not ideal for them. So um I'm
[L507] [25:09.84] sometimes asked why C++ is so big and uh
[L508] [25:14.08] complicated
[L509] [25:15.68] and uh there's two reasons. One is
[L510] [25:18.40] history. Um I could not build the C++ I
[L511] [25:22.72] wanted uh back in the 80s. um for a
[L512] [25:27.60] variety of reasons, partly uh
[L513] [25:29.76] technology, partly uh computers,
[L514] [25:33.28] um and partly because I didn't know
[L515] [25:35.12] enough and I had to learn. So you do the
[L516] [25:38.64] standard engineering thing, you do the
[L517] [25:40.64] best you can, then you see what works
[L518] [25:43.36] and what doesn't work and you try and
[L519] [25:46.56] fix the problems and then you repeat.
[L520] [25:50.32] And that's how C++ grew. And so there's
[L521] [25:53.52] some
[L522] [25:55.44] leftover things that just gets into the
[L523] [25:57.60] people's way. Now you have spans. You
[L524] [26:01.68] very rarely use pointers and you should
[L525] [26:04.48] certainly not use pointers as resource
[L526] [26:07.04] handles. Uh that was already built in
[L527] [26:09.76] with C classes in 79, but people didn't
[L528] [26:13.36] get it. Um and so there's teaching to do
[L529] [26:18.80] it. But anyway, uh once you figure out
[L530] [26:21.84] that you have a problem that require a
[L531] [26:24.16] new language,
[L532] [26:25.92] then uh you start looking what there is
[L533] [26:30.24] and uh you have lots of help, lots of uh
[L534] [26:35.92] books about analysis and about
[L535] [26:40.56] um code generation. You have frameworks
[L536] [26:44.08] like LLVM that most of the modern
[L537] [26:47.68] languages uses to generate decent code.
[L538] [26:51.36] So most of the languages that compete
[L539] [26:53.76] with C++ does it by uh using a C++
[L540] [26:57.60] infrastructure. It's it's highly
[L541] [26:59.84] amusing. Um but but anyway, focus on the
[L542] [27:04.80] problem and don't think you're the only
[L543] [27:07.36] user. If you think you're the only user,
[L544] [27:10.00] you build a special purpose programming
[L545] [27:11.92] language and that's fine. Uh domain
[L546] [27:16.08] specific languages are great when you
[L547] [27:18.40] find the right
[L548] [27:20.56] uh solution to the right problem, but
[L549] [27:24.48] identify the problem first. Uh in my
[L550] [27:27.76] case, the problem was I needed high and
[L551] [27:30.40] low-level facilities
[L552] [27:32.64] in the same language. Otherwise, I had
[L553] [27:34.88] to use two languages and I had to have
[L554] [27:38.72] them communicate uh properly. High level
[L555] [27:42.48] languages at the time uh tended to uh
[L556] [27:46.00] use interfaces that took away
[L557] [27:48.40] performance. Uh quite often they
[L558] [27:51.12] required garbage collection which is not
[L559] [27:53.36] very good for device drivers for
[L560] [27:56.00] instance or for building garbage
[L561] [27:58.56] collectors. Um so yes identify the
[L562] [28:03.92] problem and uh try and solve it.
[L563] [28:06.24] >> Back when you were creating C++ and you
[L564] [28:08.48] had identified the problem and so then
[L565] [28:10.72] you went off to build C++ and you know
[L566] [28:13.76] there's all these pieces right there's
[L567] [28:15.52] the compiler there's a there's a linker
[L568] [28:18.80] there's you know in the implementations
[L569] [28:21.12] of those there's uh like a parser alexer
[L570] [28:24.48] and you know all those things. uh when
[L571] [28:27.36] you were building the original thing,
[L572] [28:30.00] what was the most technically
[L573] [28:31.76] challenging part to implement?
[L574] [28:34.08] >> I don't think any part was particularly
[L575] [28:38.40] challenging. It was more that there was
[L576] [28:40.16] many parts as you point out. One of the
[L577] [28:43.52] things I decided that caused trouble uh
[L578] [28:48.32] later was that I wasn't going to touch
[L579] [28:50.72] the linker. And it came simply because I
[L580] [28:54.32] asked around and I realized people were
[L581] [28:56.64] using about 25 uh different linkers in
[L582] [29:00.16] in Bell Labs just just in Bell Labs. And
[L583] [29:03.76] so if I wanted to serve uh my obvious
[L584] [29:07.44] initial uses, I would have to write
[L585] [29:10.48] interfaces or modifications to 25
[L586] [29:13.68] linkers. And nobody wants you to touch
[L587] [29:16.48] their linker because if you make a
[L588] [29:18.88] mistake, everything breaks.
[L589] [29:21.76] So I decided a rule don't mess with the
[L590] [29:25.76] linker. Later people have messed with
[L591] [29:28.64] the linkers and made them better for C++
[L592] [29:31.20] but that was after C++ became a major
[L593] [29:33.92] issue. Uh the other thing was that there
[L594] [29:38.88] was many different optimizers.
[L595] [29:42.72] every
[L596] [29:44.48] um computer uh from different sources
[L597] [29:48.88] had a different optimizer and again I
[L598] [29:52.72] couldn't write u a dozen optimizers.
[L599] [29:56.72] I mean I'm I'm going to write a language
[L600] [29:59.84] here right and I can't if I wanted to be
[L601] [30:03.28] a optimizer specialist for uh deck
[L602] [30:07.04] computers say um I can become that I
[L603] [30:11.36] have the background I have the training
[L604] [30:13.68] but that wasn't what I wanted to do I
[L605] [30:16.00] wanted to build first a distributed
[L606] [30:19.76] system and then when my friends and
[L607] [30:21.84] colleagues started using seu classes um
[L608] [30:25.20] I wanted to help them uh and they were
[L609] [30:28.24] doing things like network simulations,
[L610] [30:31.52] hardware layout,
[L611] [30:33.84] uh positioning of satellites,
[L612] [30:37.76] all kinds of interesting stuff. So that
[L613] [30:40.32] was worth doing. And [snorts] so I
[L614] [30:42.80] decided that actually there was a common
[L615] [30:45.36] interface to all these optimizers and uh
[L616] [30:49.44] code generators. It's called C. So let's
[L617] [30:53.68] use C as the assembler.
[L618] [30:56.80] And that worked nicely. C was very good
[L619] [31:00.32] at the low level was part of the reason
[L620] [31:02.40] I chose it. So let's use it for the low
[L621] [31:05.52] level. And I could have hidden C and re
[L622] [31:10.48] uh created a probably a better
[L623] [31:12.72] interface. But I decided that uh
[L624] [31:17.92] I'll just use C have C compatibility.
[L625] [31:21.28] Uh at the time what I said was that well
[L626] [31:25.76] we can have Dennis's mistakes which we
[L627] [31:28.48] know and we can have my mistakes which
[L628] [31:31.36] we don't know yet. Um so uh we'll take
[L629] [31:34.72] Dennis's that's u much more manageable
[L630] [31:38.00] and understandable and I don't have to
[L631] [31:40.80] teach people how to write a for loop and
[L632] [31:43.60] things like that. So
[L633] [31:46.48] that's C compatibility came in that way
[L634] [31:49.76] partly as an implementation technique
[L635] [31:52.72] partly uh to get into the culture and uh
[L636] [31:57.04] tool support and such.
[L637] [32:00.00] I saw somewhere in in my research that
[L638] [32:03.12] um you know C++
[L639] [32:05.52] was used to write some part of uh the
[L640] [32:10.16] the language tool chain and to me
[L641] [32:12.88] immediately I have this thought of
[L642] [32:14.08] there's this chicken and egg problem
[L643] [32:15.60] because how do you use this language to
[L644] [32:18.88] build something that it is using itself
[L645] [32:21.84] h how does that work
[L646] [32:23.60] >> this is bootstrapping and it's uh it it
[L647] [32:27.92] was not an unusual ual thing. So I
[L648] [32:31.36] started with C and in C I wrote a um a
[L649] [32:36.32] pre-processor that did some of the
[L650] [32:39.20] fundamental things in uh in in in what
[L651] [32:43.60] became C++
[L652] [32:45.68] uh classes and fairly simple inheritance
[L653] [32:49.04] and overloading and such. And then I
[L654] [32:54.40] in that I wrote a a simple compiler for
[L655] [32:59.92] again what was a subset of uh of of C++.
[L656] [33:06.48] And uh now I can use uh operator
[L657] [33:10.96] overloading and overloading in general
[L658] [33:13.52] classes. So I can build a a scope class
[L659] [33:17.52] that handles look up and naming and
[L660] [33:20.56] things like that. And then then you work
[L661] [33:23.68] from there. Um
[L662] [33:27.12] just writing the next version in the
[L663] [33:30.48] previous version. You keep keep going
[L664] [33:33.60] and uh after a couple of years you have
[L665] [33:37.44] something that became known to the world
[L666] [33:40.56] as C++. and I wrote a book about it and
[L667] [33:43.92] a compiler um came out in the world. But
[L668] [33:47.84] I didn't invent this technique. This was
[L669] [33:50.48] known as bootstrapping. Um I think I was
[L670] [33:53.92] taught it as an undergrad that you could
[L671] [33:56.32] do things like that.
[L672] [33:58.40] >> Most people they look at C++ and they
[L673] [34:01.68] think that's an object-oriented
[L674] [34:03.28] language. And I've heard you say
[L675] [34:05.60] multiple times that that's not the case
[L676] [34:08.32] or that's not your immediate thought.
[L677] [34:09.76] And why is that? Yeah, I I never called
[L678] [34:12.24] it an object-oriented
[L679] [34:14.40] uh programming language. If you look at
[L680] [34:17.12] the C++ programming language, the first
[L681] [34:19.52] edition, um the closest I come is to say
[L682] [34:24.88] uh some some some people call these
[L683] [34:27.60] techniques object- based.
[L684] [34:30.40] Actually, it's more focused on classes.
[L685] [34:32.96] It's type oriented, class oriented. uh
[L686] [34:36.64] it actually supports the techniques of
[L687] [34:39.20] object orientation very well and it in
[L688] [34:43.76] particular follows similar's model of uh
[L689] [34:48.72] defining types defining classes and
[L690] [34:52.24] defining class hierarchies to uh handle
[L691] [34:56.96] uh groups of related uh classes but that
[L692] [35:00.88] was never all it was for instance I do
[L693] [35:05.04] not want object object oriented complex
[L694] [35:07.20] numbers. I don't want to say two dot uh
[L695] [35:12.80] uh something to
[L696] [35:16.64] uh to to get to uh some parts of uh
[L697] [35:22.00] numbers. I really want to say uh two two
[L698] [35:27.04] plus uh zed. Um, and I want that to be
[L699] [35:31.76] the end up being roughly the same as set
[L700] [35:35.76] plus two. And um, no dots, no arrows.
[L701] [35:40.88] Uh, math has developed a notation over
[L702] [35:44.48] the last 300 years or so. Uh, Decard
[L703] [35:47.60] was, I think, the first one to to use
[L704] [35:50.16] this notation and it is very good. Uh,
[L705] [35:53.84] so I I didn't want everything to to be
[L706] [35:56.72] object-oriented.
[L707] [35:58.24] Uh furthermore, I wanted
[L708] [36:02.48] things that did not require inheritance
[L709] [36:05.20] that did not require runtime resolution
[L710] [36:09.04] not to use it. Um so for arithmetic
[L711] [36:14.72] and for complex numbers and such I
[L712] [36:17.60] wanted for compatibility.
[L713] [36:20.08] I mean I was rather keen on what's
[L714] [36:22.32] called use reuse in those days but I saw
[L715] [36:26.16] it slightly different from a lot of
[L716] [36:28.08] researchers. A lot of researchers wanted
[L717] [36:30.96] to build a language a system that
[L718] [36:35.20] allowed res um reuse. I wanted to re re
[L719] [36:40.32] use things that existed. I mean forran
[L720] [36:44.08] was there uh with some great uh
[L721] [36:47.44] software. uh C was there with some great
[L722] [36:50.96] uh system software and actually helped
[L723] [36:54.40] with with compilers and such and there
[L724] [36:57.12] was a simpler that was used a fair bit
[L725] [37:00.08] too. So I wanted to reuse that and I
[L726] [37:02.64] wanted to make sure that worked and that
[L727] [37:05.68] meant I couldn't go too far away from
[L728] [37:07.84] the hardware. I couldn't build uh all of
[L729] [37:10.96] the things that was considered ideal or
[L730] [37:15.04] even the things I would consider ideal.
[L731] [37:18.48] Um this is the real world. This is the
[L732] [37:22.00] real set of problems you are attacking.
[L733] [37:24.56] And so you have to respect the
[L734] [37:26.80] constraints uh that comes with with that
[L735] [37:29.44] view of the of what you're doing. at the
[L736] [37:32.96] time that you wrote C++, C was already
[L737] [37:35.28] there and it had a weaker type system
[L738] [37:37.68] than what C++ eventually had. And I was
[L739] [37:40.88] guess your thoughts on, you know, the
[L740] [37:42.56] trade-offs behind that and why did you
[L741] [37:44.48] choose to make the typing system
[L742] [37:46.16] stronger in C++?
[L743] [37:47.92] >> Because we needed it. Um uh the weakness
[L744] [37:51.52] in the type system is one of the most
[L745] [37:54.72] obvious sources of uh errors and it's
[L746] [37:59.68] certainly one of the sources of um
[L747] [38:03.84] endless testing and uh debugging. I hate
[L748] [38:09.12] debugging. I would much rather do
[L749] [38:11.36] design. And so you can't really have
[L750] [38:15.44] either design or debugging. Some people
[L751] [38:18.72] claim they can but they can't. Uh so I
[L752] [38:22.08] want to move the the arrow over towards
[L753] [38:25.84] more design uh that helps the debugging
[L754] [38:29.44] and makes fewer uh mistakes at runtime.
[L755] [38:33.76] And uh the type system is is one of
[L756] [38:36.24] them. And uh actually what you get in C
[L757] [38:39.44] today to a large extent is stronger well
[L758] [38:43.12] no it is much stronger uh type than it
[L759] [38:45.68] was in those days and partly because of
[L760] [38:48.64] C++.
[L761] [38:50.64] Um also there's things you can't express
[L762] [38:53.68] unless you have a strong type system. Um
[L763] [38:56.40] I mentioned overloading before. Uh
[L764] [38:59.20] overloading is essential for generic
[L765] [39:01.44] programming. And if you want to write
[L766] [39:03.68] say a vector of T where T is a parameter
[L767] [39:06.72] type, you have to have overloading
[L768] [39:08.96] because you can only operate on T's
[L769] [39:11.76] providing all the T's have the same
[L770] [39:14.08] interface
[L771] [39:15.68] uh for what you need. So you you need
[L772] [39:19.04] the type system to resolve those things
[L773] [39:22.08] and that can be resolved at compile
[L774] [39:24.40] time. So the compiler gets a bit more
[L775] [39:27.52] complicated probably a bit slower
[L776] [39:30.88] but you don't do so much debugging. Um
[L777] [39:34.88] there was a largecale
[L778] [39:37.76] experiment done in Bell Labs in Chicago
[L779] [39:41.68] where they had
[L780] [39:44.16] some groups using C++ switching to C++
[L781] [39:49.04] and they wanted to know whether they
[L782] [39:52.40] were more or less uh productive.
[L783] [39:57.76] And some people claimed that the slower
[L784] [40:00.32] compilation slowed them down.
[L785] [40:03.28] And uh somebody simply measured how much
[L786] [40:06.80] compile time was used uh before after
[L787] [40:10.24] switching to C++. And they found that
[L788] [40:13.76] the amount of [snorts]
[L789] [40:17.28] commulation time of compute power was
[L790] [40:20.72] roughly identical. that is C++ was
[L791] [40:24.16] slower but you uh by about a factor of
[L792] [40:27.12] two at that time but the C people
[L793] [40:31.28] compiled twice as often.
[L794] [40:34.72] Um this is just one experiment. the
[L795] [40:38.16] factor of two is is is just one
[L796] [40:40.88] experiment but um
[L797] [40:44.96] I wanted to move towards using more
[L798] [40:48.00] compile uh compile time resolution still
[L799] [40:52.48] doing that
[L800] [40:53.92] >> I mean for every language there's this
[L801] [40:56.40] um you know dichotomy of having it being
[L802] [40:59.52] statically typed versus dynamically
[L803] [41:01.44] typed and C++ is one of the most famous
[L804] [41:04.08] statically typed languages why did you
[L805] [41:06.48] choose statically typed language
[L806] [41:09.92] >> because of the problems I wanted to um
[L807] [41:14.48] to attack. Um what do you do when you
[L808] [41:18.48] get a runtime error and
[L809] [41:22.40] in something like small talk? You go
[L810] [41:25.04] into the debugger
[L811] [41:27.52] and that makes a lot of sense if there's
[L812] [41:30.24] a programmer sitting at a screen uh
[L813] [41:32.64] getting the error. It doesn't make any
[L814] [41:34.80] sense if a telephone switch um finds a a
[L815] [41:38.72] runtime error and then you have to
[L816] [41:40.80] resolve it. Furthermore, you want
[L817] [41:43.44] performance and you want small programs
[L818] [41:46.16] to fit into memories. This is true even
[L819] [41:49.28] today because as I think 99% of all
[L820] [41:54.48] computers are embedded systems and they
[L821] [41:57.20] tend to be uh memory rest constraint
[L822] [42:01.44] and um again if you do runtime
[L823] [42:06.00] resolution you need to have enough
[L824] [42:08.24] information enough data to do the
[L825] [42:11.04] runtime resolution and I wanted to fit
[L826] [42:13.92] into small memories. uh small meaning
[L827] [42:17.92] 100 uh
[L828] [42:20.56] 120k 250k 1 megabyte things like that
[L829] [42:26.56] and I think it's still relevant uh for
[L830] [42:29.92] for many systems uh you can build a a
[L831] [42:35.12] camera like that it can still have
[L832] [42:37.12] several megabytes of memory but uh if
[L833] [42:41.20] you put in a lot of memory it gets
[L834] [42:43.28] bigger and it cost more and the battery
[L835] [42:46.56] um runs out uh quicker. So, we don't do
[L836] [42:50.80] that. Um phones and cameras and things
[L837] [42:55.36] like that are still memory constraint.
[L838] [42:58.40] And um static type languages, languages
[L839] [43:02.24] optimized for memory consumption are
[L840] [43:05.68] just better at that, which is why we use
[L841] [43:07.92] it. We're using it right now. I suspect
[L842] [43:11.52] that the microphones have uh chips in
[L843] [43:13.92] them, too. And there's a lot of C++ in
[L844] [43:17.60] that uh world.
[L845] [43:20.16] Uh the composition there is C and
[L846] [43:23.44] assembler.
[L847] [43:24.48] >> And you mentioned the the research that
[L848] [43:27.20] was done on the the compile time on you
[L849] [43:31.68] know if you catch things earlier you
[L850] [43:34.40] compile less often but maybe it takes
[L851] [43:36.64] longer. In this case, I I could see a
[L852] [43:39.28] similar analogy where um you catch
[L853] [43:42.48] errors way earlier if you have a
[L854] [43:44.16] statically typed language because the
[L855] [43:46.00] compiler is yelling at you before you
[L856] [43:48.48] put together that final thing. Whereas
[L857] [43:50.88] in dynamically typed language, the
[L858] [43:53.44] errors may come later. Comparing for a
[L859] [43:55.84] developer like which one is more time
[L860] [43:58.24] efficient.
[L861] [43:59.28] >> I I don't know any solid research on
[L862] [44:02.64] that, but you can look at it. uh
[L863] [44:07.44] JavaScript and Pythons are very are very
[L864] [44:10.48] uh popular and they are um runtime
[L865] [44:14.96] uh checked and they run much slower. I
[L866] [44:18.88] mean raw uh Python runs something like
[L867] [44:21.60] 70 times slower than raw C++ and the
[L868] [44:26.00] reason it's viable is that a lot of key
[L869] [44:30.08] uh Python libraries are written in C or
[L870] [44:32.56] C++ to get the performance and so you
[L871] [44:36.16] get the performance by actually getting
[L872] [44:39.84] to the point that I was starting out
[L873] [44:42.80] with you need a highle stuff and you
[L874] [44:45.36] need the thing that can manipulate
[L875] [44:47.44] hardware.
[L876] [44:48.56] uh here they are using two languages but
[L877] [44:51.68] uh still the same uh needs fundamental
[L878] [44:56.00] needs
[L879] [44:57.52] and uh it's easier to uh try out things
[L880] [45:01.92] in a dynamically uh check language
[L881] [45:04.48] because you don't have to know enough
[L882] [45:06.56] about the language. You don't have to
[L883] [45:08.32] know about type systems and your average
[L884] [45:12.00] uh web developer or astrophysicist
[L885] [45:16.16] is not a computer scientist and don't
[L886] [45:18.24] want to become one. So there's
[L887] [45:20.80] advantages there. But the problem is
[L888] [45:23.60] that errors that are found by the type
[L889] [45:26.08] system in a statically typed language is
[L890] [45:28.72] found at runtime later. And so as
[L891] [45:34.80] systems grow
[L892] [45:37.20] uh the performance problems uh start
[L893] [45:41.60] furthermore you find it get harder to
[L894] [45:44.64] write reliable
[L895] [45:46.64] uh software. uh you need much more unit
[L896] [45:50.40] testing for instance in a dynamic uh
[L897] [45:53.92] language because it's um
[L898] [45:58.24] well
[L899] [46:00.08] the compiler doesn't do it for you. And
[L900] [46:02.64] if you want things to guarantee to work
[L901] [46:07.60] like the telephone switch mustn't crash,
[L902] [46:10.24] your car mustn't crash, your plane
[L903] [46:12.64] mustn't crash. You want guarantees and
[L904] [46:15.68] they're harder to provide in a very
[L905] [46:18.24] flexible dynamic type system.
[L906] [46:21.04] >> One thing that I think C++ is uh
[L907] [46:25.04] infamous for is kind of like memory
[L908] [46:27.44] safety issues or kind of foot guns that
[L909] [46:30.64] exist there.
[L910] [46:31.44] >> I'm so tired of that. Um I haven't had
[L911] [46:34.80] those problems for years. Um, and
[L912] [46:38.56] somebody did a a study of
[L913] [46:42.88] the obvious problems with buffer
[L914] [46:45.28] overflows and um
[L915] [46:49.20] people hacking in using that kind of
[L916] [46:52.16] stuff and uh
[L917] [46:56.08] almost all of the uh these cases when
[L918] [46:59.12] people writing C style code or in C
[L919] [47:02.88] and uh Herb Server has a a talk with
[L920] [47:07.68] with actual numbers and they they are
[L921] [47:11.12] quite significant. It's it's sort of
[L922] [47:15.68] that kind of problems
[L923] [47:18.24] more than 90% are for people that don't
[L924] [47:21.28] write modern C++.
[L925] [47:23.52] They they use raw pointers to pass
[L926] [47:27.76] things around without
[L927] [47:30.40] um the number of elements. No fat
[L928] [47:32.64] pointers, no spans.
[L929] [47:35.04] um you you have them in C++. You can use
[L930] [47:38.16] them. You can use uh vectors. We have
[L931] [47:42.24] hardened libraries. Everybody has
[L932] [47:44.24] hardened libraries that that does the
[L933] [47:46.72] runtime checking. Uh Apple has it.
[L934] [47:50.00] Google has it. Microsoft has it. It's
[L935] [47:52.72] just not standard till now. C++ 26 has a
[L936] [47:58.40] hardened option that are standard. uh
[L937] [48:02.32] and the work I'm doing on profiles will
[L938] [48:05.84] give you a way of guaranteeing that you
[L939] [48:08.24] don't do the stupid things.
[L940] [48:10.88] Um
[L941] [48:12.56] so anyway, uh fundamentally
[L942] [48:16.64] theoretically the problem was solved
[L943] [48:18.72] many years ago and people just do what
[L944] [48:23.20] they've always done and get the problems
[L945] [48:25.20] they've always had. And uh that makes me
[L946] [48:28.64] sad and uh it's one of the things that
[L947] [48:32.32] makes me work on uh coding guidelines
[L948] [48:35.76] and on enforced profiles and on
[L949] [48:38.24] education.
[L950] [48:40.40] >> I mean education is one way to solve the
[L951] [48:42.48] problem. Is there a way to get the
[L952] [48:45.04] compiler to just prevent people from
[L953] [48:47.92] doing all those risky things?
[L954] [48:50.08] >> And is that enabled by default in modern
[L955] [48:52.48] C++ today?
[L956] [48:53.68] >> No, but it should be. I'm proposing that
[L957] [48:56.24] for C++ 29. Uh the simpler versions of
[L958] [49:00.00] that should have been in in in uh C++
[L959] [49:04.40] 26, but there are still a lot of people
[L960] [49:07.04] even in the C++ standards committee that
[L961] [49:09.76] are very devoted to uh their old code
[L962] [49:12.64] and their old ways of doing things. Um
[L963] [49:16.64] there's people who says you should only
[L964] [49:18.24] standardize what is common in industry.
[L965] [49:21.60] But when the bugs are common in
[L966] [49:23.76] industry, you should do something else.
[L967] [49:26.80] >> The standards committee is a a topic I
[L968] [49:29.04] want to talk about actually. It's
[L969] [49:30.24] interesting. I mean the language is now
[L970] [49:32.00] run um you know by a democracy and one
[L971] [49:36.40] question I want to ask you is if it was
[L972] [49:39.20] a dictatorship so you just had full say
[L973] [49:42.64] what what language features would be in
[L974] [49:45.60] that you know maybe a harder to get by
[L975] [49:47.84] >> f first of all it never was a
[L976] [49:51.52] dictatorship uh I I never had full
[L977] [49:54.56] control once you have some users in my
[L978] [49:58.48] opinion you gain some responsibility for
[L979] [50:02.40] making sure that they're helped and
[L980] [50:04.80] their stuff works. You can't keep
[L981] [50:07.44] breaking the language. That's what
[L982] [50:10.40] academic language development does. They
[L983] [50:12.80] they they break to improve all the time
[L984] [50:16.00] and then they can't maintain a user
[L985] [50:18.32] population. I didn't actually choose to
[L986] [50:20.96] have a standards committee. I I chose
[L987] [50:24.72] responsibility to the commuter to the uh
[L988] [50:28.08] to the community. But one day um two
[L989] [50:32.48] guys came in uh representing uh IBM and
[L990] [50:37.12] HP
[L991] [50:38.64] and I can't remember if it was Sun or
[L992] [50:42.32] Deck that was the third thing they
[L993] [50:44.56] represented but anyway the biggest
[L994] [50:47.52] computer and software uh suppliers in
[L995] [50:50.64] the world at the time they come into my
[L996] [50:53.20] office in it was uh
[L997] [50:56.88] ah it's 89 n and they say well pian you
[L998] [51:02.40] want to help us standardize C++ under
[L999] [51:05.92] ISO rules
[L1000] [51:08.56] and I said no I can't do that I'm still
[L1001] [51:11.04] doing experiments it's still not
[L1002] [51:13.92] complete
[L1003] [51:15.44] so they said no B you don't get it
[L1004] [51:19.68] our
[L1005] [51:22.16] organizations cannot use a language
[L1006] [51:24.64] that's not standardized
[L1007] [51:27.28] they cannot use a language that's owned
[L1008] [51:30.00] by a corporation that we might compete
[L1009] [51:33.36] with and we do sometimes.
[L1010] [51:36.72] Okay, we we we trust you of course but
[L1011] [51:40.00] not your employer.
[L1012] [51:42.48] We compete with them sometimes and you
[L1013] [51:45.44] can get run over by a boss. This uh No,
[L1014] [51:48.88] no, no. We need a standards and we need
[L1015] [51:50.64] a standards committee. So this goes on
[L1016] [51:53.44] for about an hour and they twist my arm.
[L1017] [51:55.84] Ow ow ow. And in the end they said okay
[L1018] [51:58.64] I I I I will uh standardize C++ under
[L1019] [52:02.16] anti- rules uh just like you suggest and
[L1020] [52:05.04] you need the the computer community
[L1021] [52:08.16] needs that and u by the way what's NI
[L1022] [52:13.84] rules for standardization
[L1023] [52:17.12] and um so they told me and we started a
[L1024] [52:20.08] year later but um this this was the way
[L1025] [52:23.92] it came about some very important
[L1026] [52:26.64] important organizations wanted that
[L1027] [52:29.12] standardization.
[L1028] [52:30.80] C was on the track to get standard
[L1029] [52:33.60] standardized
[L1030] [52:35.12] and AT&T being primarily a user of
[L1031] [52:39.92] software was also in favor of
[L1032] [52:42.16] standardization I found out and so they
[L1033] [52:45.20] supported it and the documentation I had
[L1034] [52:49.68] written was bases on it. Actually, I
[L1035] [52:52.72] rewrote the documentation that became
[L1036] [52:55.36] the the ARM, the annotated C++ standards
[L1037] [52:59.52] uh manual that uh gave the definition
[L1038] [53:04.48] the manual of the language and for every
[L1039] [53:08.96] feature some rationale and some way it
[L1040] [53:13.04] could be implemented or was implemented
[L1041] [53:16.44] [snorts]
[L1042] [53:16.96] and that became the the foundation
[L1043] [53:19.04] document for the standardization.
[L1044] [53:21.68] when they were strongarmming you, what
[L1045] [53:23.84] if you had just said no? Like what would
[L1046] [53:25.76] have happened? I think well I think C++
[L1047] [53:31.60] would have faded into becoming an
[L1048] [53:35.44] academic
[L1049] [53:37.04] um
[L1050] [53:38.96] cute uh language that
[L1051] [53:42.64] was loved by some small community and it
[L1052] [53:46.96] would have disappeared out of the
[L1053] [53:48.40] mainstream of uh
[L1054] [53:51.68] of computing. And uh there are people
[L1055] [53:55.92] who say this stronger than I I do. Um
[L1056] [53:59.44] they say that C++ is spread and uses is
[L1057] [54:05.44] that it has a standard. It's not owned
[L1058] [54:07.52] by a corporation. It is one of the
[L1059] [54:10.16] things that sometimes blocks the um the
[L1060] [54:14.64] the the the wannabe C++ killers. I
[L1061] [54:19.12] remember the ads for Java and people
[L1062] [54:22.72] standing up saying we'll kill absolutely
[L1063] [54:25.12] kill C++ in two years. I thought that
[L1064] [54:28.72] was rude. Um and anyway, we have
[L1065] [54:34.72] 10 12 times more C++ developers today
[L1066] [54:38.88] than we had when they said it. So, uh
[L1067] [54:42.32] didn't work.
[L1068] [54:44.00] How is it that um C++ and not not
[L1069] [54:47.68] exactly that it's a war but just if we
[L1070] [54:49.84] looked at um adoption you know clearly
[L1071] [54:53.52] C++
[L1072] [54:55.04] gained a lot more adoption than Java yet
[L1073] [54:57.92] I know C or Java had the backing of uh
[L1074] [55:01.44] you know a big company that's putting a
[L1075] [55:03.76] lot of marketing dollars in and C++ was
[L1076] [55:06.96] kind of I I think you've said that it
[L1077] [55:09.28] had almost zero you know next to zero
[L1078] [55:11.92] marketing done for
[L1079] [55:13.36] uh next to zero was $5,000
[L1080] [55:16.96] to be used over three years
[L1081] [55:20.00] and uh son used
[L1082] [55:24.48] much more money on advertising and
[L1083] [55:27.28] marketing uh Java than was ever used in
[L1084] [55:31.28] C++ uh development.
[L1085] [55:34.56] Um and to this day the standards
[L1086] [55:37.12] committee has a problem. government has
[L1087] [55:38.64] no funding
[L1088] [55:40.48] and uh that means that it's hard to do
[L1089] [55:43.44] experiments. It's hard to deploy things
[L1090] [55:46.08] and uh other language communities keep
[L1091] [55:51.52] um sort of stealing uh C++ uh compiler
[L1092] [55:56.08] and tool developers because they're
[L1093] [55:58.16] good. Uh but it's makes it hard to to to
[L1094] [56:02.80] predict how fast we can implement things
[L1095] [56:06.64] today. Last I checked, the C++ standards
[L1096] [56:10.00] committee had 527
[L1097] [56:13.36] members and we work on consensus.
[L1098] [56:18.24] Uh because if you don't have consensus
[L1099] [56:21.20] then you get dialects. Um, we don't want
[L1100] [56:24.88] to have a feature in that's voted in um,
[L1101] [56:28.64] say 60 to uh, 40 or even worse 52 to 48.
[L1102] [56:35.36] No uh, percent. We we we don't do that
[L1103] [56:40.16] and uh, that's painful and tedious and
[L1104] [56:44.24] good.
[L1105] [56:45.20] >> When you say consensus that 100% need to
[L1106] [56:47.84] approve
[L1107] [56:48.40] >> 100% is not uh necessary. We we don't
[L1108] [56:52.96] need unanimity. We need a massive
[L1109] [56:56.48] majority and basically I would like to
[L1110] [57:00.00] see 90%.
[L1111] [57:01.76] And we often do 80% I start to worry.
[L1112] [57:06.80] And what's the lower bound that's coded
[L1113] [57:10.08] into the rules?
[L1114] [57:11.12] >> There's no lower bound coded into the
[L1115] [57:13.28] rules. The rule says that the convenor
[L1116] [57:17.60] or of the ISO committee um determines
[L1117] [57:21.04] what is consensus.
[L1118] [57:23.36] So
[L1119] [57:24.88] pure numbers doesn't say it. Could you
[L1120] [57:27.44] imagine you had
[L1121] [57:30.48] a vote [snorts] 95%
[L1122] [57:35.20] versus 5%.
[L1123] [57:38.00] But the implementers of C++
[L1124] [57:42.08] compiler and standard libraries from
[L1125] [57:45.52] Google, Apple, Microsoft uh and uh
[L1126] [57:52.08] others were all in the 5%. Is that
[L1127] [57:55.84] consensus? I can reassure you that no
[L1128] [57:59.44] convenor would call that consensus.
[L1129] [58:02.24] >> And that makes sense intuitively. I kind
[L1130] [58:04.96] of wonder with democratic decisions
[L1131] [58:08.08] there needs to be objective rules. So
[L1132] [58:10.48] like what if the convenor made the wrong
[L1133] [58:12.80] decision? It happens but
[L1134] [58:17.44] you you can't just have numeric rules.
[L1135] [58:20.08] Uh not everybody cares for the whole
[L1136] [58:22.72] language. Not everybody uh understands
[L1137] [58:25.92] what's going on. You can vote at your
[L1138] [58:29.04] third meeting. So you you might have uh
[L1139] [58:32.72] somebody with a vote that has uh
[L1140] [58:37.36] well eight months of experience with the
[L1141] [58:39.84] standardization and don't understand
[L1142] [58:41.84] standardization and knows only what they
[L1143] [58:46.40] known from their development
[L1144] [58:48.56] organization that they have been part of
[L1145] [58:51.44] which might be a small one. um you you
[L1146] [58:55.20] you need some some judgment and you hope
[L1147] [58:58.96] that the convenor has that judgment. the
[L1148] [59:02.48] convenor uh always uh asks the national
[L1149] [59:06.56] representatives
[L1150] [59:08.48] um I mean the other way of getting a
[L1151] [59:11.76] consensus is that you have a massive
[L1152] [59:14.08] consensus but you have 10 countries that
[L1153] [59:18.48] where the representatives didn't agree
[L1154] [59:21.84] that's not consensus and even when there
[L1155] [59:25.52] looks if there is a
[L1156] [59:29.68] look if everybody body is for, if it's
[L1157] [59:33.20] massive and all of that, there's not a
[L1158] [59:35.20] problem. But if there's a problem, the
[L1159] [59:38.80] convenor
[L1160] [59:40.32] asks the national body heads, he asks
[L1161] [59:42.72] the implementers,
[L1162] [59:44.64] uh, sort of key people that are
[L1163] [59:47.76] necessary for getting the
[L1164] [59:51.84] voted change
[L1165] [59:54.16] uh, into real use. sometimes educators
[L1166] [59:57.84] also uh before they make that decision.
[L1167] [01:00:01.44] Uh not everybody weighs equally uh once
[L1168] [01:00:04.88] there's a disagreement. For this podcast
[L1169] [01:00:08.24] I produced transcripts for every episode
[L1170] [01:00:10.24] for convenient skimming and I built a
[L1171] [01:00:12.48] custom tool to automate that. Recently I
[L1172] [01:00:14.96] noticed in the Barbara Liskoff
[L1173] [01:00:16.72] transcript my simple speechtoext tool
[L1174] [01:00:19.76] was getting a lot of things wrong. For
[L1175] [01:00:21.44] instance, the clue programming language
[L1176] [01:00:23.36] is spelled all caps clu, not clue. So to
[L1177] [01:00:27.76] fix this, I used cursor 3, picked the
[L1178] [01:00:30.64] strongest version of opus 4.7 extra high
[L1179] [01:00:33.84] and had an agent make a plan to fix
[L1180] [01:00:35.52] that. And while I was waiting, I figured
[L1181] [01:00:37.44] I'd trigger a few more agents for code
[L1182] [01:00:39.04] cleanups and front-end improvements. Um,
[L1183] [01:00:41.60] it generated a reasonable plan with rich
[L1184] [01:00:43.76] system diagrams. It applied all the
[L1185] [01:00:46.08] changes within minutes and worked on the
[L1186] [01:00:48.16] first try. So if you want to build
[L1187] [01:00:50.24] something with the flexibility of
[L1188] [01:00:51.76] sending off a bunch of agents with
[L1189] [01:00:53.52] frontier models of your choice, you can
[L1190] [01:00:55.68] go to cursor.com to try out cursor 3.
[L1191] [01:00:59.28] OpenAI, [snorts]
[L1192] [01:01:00.24] Enthropic, Cursor, and Verscell all use
[L1193] [01:01:03.60] this product to make their lives better.
[L1194] [01:01:05.76] And the problem it solves is when you're
[L1195] [01:01:07.84] building SAS or an AI product and you
[L1196] [01:01:10.40] want to sell to other companies, there's
[L1197] [01:01:12.24] all these requirements you need to meet.
[L1198] [01:01:14.32] There's SSO, there's SKIM, there's
[L1199] [01:01:16.96] arbback, there's audit logs. These are
[L1200] [01:01:19.36] all things that take time to integrate
[L1201] [01:01:21.44] but aren't the main focus of your app.
[L1202] [01:01:23.36] Work OS is an API layer that lets you
[L1203] [01:01:25.52] meet all of these requirements in just a
[L1204] [01:01:27.76] few lines of code. So, let's say you
[L1205] [01:01:29.68] have a new SAS product and you want to
[L1206] [01:01:31.60] sell to other companies. Work OS will
[L1207] [01:01:33.84] solve all of these critical feature gaps
[L1208] [01:01:35.76] for you. You can check them out at
[L1209] [01:01:38.24] workos.com to learn more and get
[L1210] [01:01:40.56] started. and I appreciate them for
[L1211] [01:01:42.72] supporting my work and sponsoring this
[L1212] [01:01:44.48] podcast.
[L1213] [01:01:45.36] >> About the standards committee, I I saw
[L1214] [01:01:47.84] in some of your writing, you said um one
[L1215] [01:01:50.56] of the most negatively received ideas
[L1216] [01:01:52.80] you'd ever presented was uh auto. And I
[L1217] [01:01:56.00] know auto eventually made its way in
[L1218] [01:01:57.68] there, but what's the story behind why
[L1219] [01:01:59.44] it was so, you know, negatively received
[L1220] [01:02:02.24] at that time?
[L1221] [01:02:03.68] >> It was just unusual. people thought was
[L1222] [01:02:06.00] weakening the type system.
[L1223] [01:02:08.96] And uh also it opens the door to fairly
[L1224] [01:02:14.64] general generic programming that is not
[L1225] [01:02:17.60] heavily uh syntax based. And auto is the
[L1226] [01:02:23.20] beginning of concepts which is the um
[L1227] [01:02:27.36] ability to put constraints on uh generic
[L1228] [01:02:32.24] code. And auto is just the simplest
[L1229] [01:02:35.12] constraint. It must be a type as opposed
[L1230] [01:02:38.24] to a say a value seven. [snorts]
[L1231] [01:02:42.40] And uh maybe I didn't explain this well
[L1232] [01:02:46.24] enough uh and there's a variety of
[L1233] [01:02:50.80] backgrounds and in the committee and
[L1234] [01:02:54.64] maybe they they didn't know languages of
[L1235] [01:02:57.76] the uh generic types uh ML hasll things
[L1236] [01:03:03.60] like that. So it it was it was horrible
[L1237] [01:03:09.44] uh
[L1238] [01:03:11.36] um so anyway we still got it um because
[L1239] [01:03:17.20] we we needed something like that but it
[L1240] [01:03:19.68] wasn't enough. I have looked at
[L1241] [01:03:21.92] industrial software and problems with
[L1242] [01:03:24.56] overuse of auto. You should only use
[L1243] [01:03:28.32] auto when you have an idea about what is
[L1244] [01:03:32.64] needed there. It's good in generic code
[L1245] [01:03:35.76] where there's uh you you you go and
[L1246] [01:03:39.60] eventually you check the the type is
[L1247] [01:03:42.40] correct that auto has resolved to
[L1248] [01:03:45.28] something that supports the uh
[L1249] [01:03:47.76] operations that you're going to do on it
[L1250] [01:03:50.56] and that's what concept formalizes but
[L1251] [01:03:54.08] it was always checked at the end and I
[L1252] [01:03:57.44] noticed a group of people that was
[L1253] [01:03:59.28] overusing auto in a
[L1254] [01:04:02.96] actually in a framework for um
[L1255] [01:04:06.16] networking.
[L1256] [01:04:07.76] And they were saying that they were
[L1257] [01:04:10.24] being slowed down, not so much with
[L1258] [01:04:13.12] bugs, but they had to look up the
[L1259] [01:04:16.08] functions being called to see what that
[L1260] [01:04:19.52] auto could possibly bind to.
[L1261] [01:04:22.96] And then they had to put in comments
[L1262] [01:04:25.28] that says what the the um what the auto
[L1263] [01:04:30.08] uh was meant. So you you have auto and
[L1264] [01:04:32.80] the comment says uh must be an input
[L1265] [01:04:36.00] channel.
[L1266] [01:04:38.56] Now you simply define input channel and
[L1267] [01:04:42.48] then instead of saying auto you say
[L1268] [01:04:45.20] input channel auto
[L1269] [01:04:48.24] fine that's what the system is uh my
[L1270] [01:04:51.76] design of that simply said that auto is
[L1271] [01:04:54.96] the simplest concept and you should
[L1272] [01:04:57.28] simply only set input channel uh C
[L1273] [01:05:01.04] equals blah blah blah but anyway the the
[L1274] [01:05:05.20] committee wanted a an indicator that
[L1275] [01:05:08.40] this was going on.
[L1276] [01:05:10.96] Oh, well,
[L1277] [01:05:11.76] >> I saw another anecdote in kind of the
[L1278] [01:05:14.24] standards committee being heated at some
[L1279] [01:05:16.56] times. You mentioned there's this thing
[L1280] [01:05:18.88] about shuttle diplomacy between two
[L1281] [01:05:21.60] corners of the room because I think it
[L1282] [01:05:24.16] was IBM and Intel. They both needed
[L1283] [01:05:26.88] different support.
[L1284] [01:05:27.92] >> That's right.
[L1285] [01:05:28.64] >> What's the story behind that? And I was
[L1286] [01:05:31.12] actually talking to Brian Mcnite who
[L1287] [01:05:35.28] were the IBM rep at the time and it was
[L1288] [01:05:39.68] last week and we were we were discussing
[L1289] [01:05:42.64] some of the things that was happening
[L1290] [01:05:44.24] then. So it it's still remembered. So
[L1291] [01:05:48.08] basically IBM was doing the uh what's
[L1292] [01:05:52.80] that architecture called? Uh
[L1293] [01:05:54.96] >> uh power PC. Power PC and um
[L1294] [01:05:58.24] >> the X86
[L1295] [01:05:59.12] >> and the Intel was doing well Intel and
[L1296] [01:06:01.60] they have different models of the
[L1297] [01:06:03.84] underlying hardware especially uh
[L1298] [01:06:07.44] coordination with the uh caches and
[L1299] [01:06:11.12] things like that. And basically
[L1300] [01:06:16.16] yeah and uh the guy representing Intel
[L1301] [01:06:19.92] wasn't actually an Intel guy. that was
[L1302] [01:06:22.48] uh uh he he he and any anyway
[L1303] [01:06:27.60] also a good guy. I use some of his
[L1304] [01:06:29.36] slides in my presentations. It's uh so I
[L1305] [01:06:32.32] knew these guys but they were totally
[L1306] [01:06:35.12] deadlocked. I mean this these are
[L1307] [01:06:39.36] massive again massive organizations with
[L1308] [01:06:42.96] massive amounts of code out there and um
[L1309] [01:06:48.80] uh
[L1310] [01:06:50.61] [sighs]
[L1311] [01:06:51.36] basically
[L1312] [01:06:56.96] some things could be done but
[L1313] [01:07:02.80] the the IBM guy Brian
[L1314] [01:07:05.76] said that they had a lot of software
[L1315] [01:07:09.68] mostly in the lowest level even down in
[L1316] [01:07:14.24] the the microode uh that was relying on
[L1317] [01:07:18.88] the way they have done it and the people
[L1318] [01:07:22.56] who had done it had left the company.
[L1319] [01:07:25.20] They they was done a long time ago and
[L1320] [01:07:28.48] they just couldn't rewrite all of that
[L1321] [01:07:31.36] code and get it right even if the intel
[L1322] [01:07:35.52] guys was right.
[L1323] [01:07:38.40] Okay. And the intel guys had similar uh
[L1324] [01:07:42.00] arguments and similar uh points. This is
[L1325] [01:07:45.04] better. We are using it. And so I was
[L1326] [01:07:48.32] shuffling. They were definitely they
[L1327] [01:07:49.92] were in different corners of a large
[L1328] [01:07:52.24] room. And so I go up to the Intel guy,
[L1329] [01:07:56.64] um, the guy representing Intel here and
[L1330] [01:08:01.44] what's the problem here? Tell him tell
[L1331] [01:08:03.84] me about it. Explain it. I go down,
[L1332] [01:08:06.08] explain he's saying this. They say,
[L1333] [01:08:08.00] "Well, there's this, this, this." And I
[L1334] [01:08:10.16] go back again. And I spent a couple of
[L1335] [01:08:12.48] hours literally doing shuttle diplomacy,
[L1336] [01:08:15.28] walking from one corner of the room to
[L1337] [01:08:17.44] the other. And um we we reached an
[L1338] [01:08:21.68] agreement and that's in uh C++ 11.
[L1339] [01:08:26.40] And a couple of years later they both uh
[L1340] [01:08:30.16] agreed that they were now using a
[L1341] [01:08:33.20] combination of what they had before and
[L1342] [01:08:35.84] what the other guys brought in. So we
[L1343] [01:08:39.20] they actually the result was uh was
[L1344] [01:08:42.56] improvement
[L1345] [01:08:44.16] cross-pollination.
[L1346] [01:08:45.76] >> That's funny. Why did you have to do
[L1347] [01:08:47.76] shuttle diplomacy? Why not just a group
[L1348] [01:08:49.92] conversation with
[L1349] [01:08:51.12] >> Because they've been trying that for
[L1350] [01:08:53.20] days and probably for meetings before
[L1351] [01:08:55.68] that and it didn't work.
[L1352] [01:08:58.80] So I I guess I was just translating and
[L1353] [01:09:02.16] asking questions.
[L1354] [01:09:04.64] I mean those were experts. I don't
[L1355] [01:09:06.40] consider myself expert at that level. Um
[L1356] [01:09:10.08] I mean I've done hardware. I've done
[L1357] [01:09:11.92] microode. So I'm I'm not an amateur, but
[L1358] [01:09:15.52] but these guys are really good. Um,
[L1359] [01:09:19.95] [snorts]
[L1360] [01:09:21.52] so the the the the IBM guy is now the
[L1361] [01:09:25.84] guy doing most of the synchronization
[L1362] [01:09:28.00] under Linux.
[L1363] [01:09:30.08] We're we're still using his stuff uh
[L1364] [01:09:32.88] today. He has a C version of it so he
[L1365] [01:09:35.84] can get it into the but it's a bottom of
[L1366] [01:09:38.32] the uh Linux kernel. When I was reading
[L1367] [01:09:41.44] your writing in these papers, there's
[L1368] [01:09:43.68] this part where it seems like in 1995,
[L1369] [01:09:47.84] you had this idea to introduce uh some
[L1370] [01:09:50.96] form of automatic garbage collection
[L1371] [01:09:53.44] into C++. And that kind of surprised me
[L1372] [01:09:56.24] because when I when I think about C++,
[L1373] [01:09:58.72] my one of my immediate thoughts is no
[L1374] [01:10:00.72] garbage collector. We're going to man
[L1375] [01:10:03.12] manually or you know manage the memory
[L1376] [01:10:05.28] ourselves. How how would that even work?
[L1377] [01:10:08.40] Um
[L1378] [01:10:10.24] there's two things there. One, I wanted
[L1379] [01:10:13.60] to automate
[L1380] [01:10:15.60] resource management in general, not just
[L1381] [01:10:18.08] garbage and not just memory. And uh for
[L1382] [01:10:21.68] that you have constructors, destructors
[L1383] [01:10:24.08] and the techniques that was later later
[L1384] [01:10:26.40] known as uh our AI resource acquisition
[L1385] [01:10:30.32] is initialization
[L1386] [01:10:32.16] which is probably my worst naming ever.
[L1387] [01:10:36.16] But um I was busy at the time. Um so
[L1388] [01:10:42.56] in the standards committee those people
[L1389] [01:10:44.64] that insisted that we needed to be able
[L1390] [01:10:48.24] to do garbage collection
[L1391] [01:10:51.04] and there was garbage collectors out uh
[L1392] [01:10:55.04] there. Oh that was Hans Berm. He was the
[L1393] [01:10:57.76] one that representing the internal model
[L1394] [01:11:00.00] of stuff. He he has a conservative
[L1395] [01:11:03.44] garbage collector still used today and
[L1396] [01:11:07.68] we thought we needed an interface so
[L1397] [01:11:10.00] that uh it could be standard how you
[L1398] [01:11:12.64] used such a garbage collector
[L1399] [01:11:16.72] and so basically I was listening to the
[L1400] [01:11:19.36] users expert users and they thought it
[L1401] [01:11:23.36] was necessary. I thought that support
[L1402] [01:11:26.80] for
[L1403] [01:11:28.72] memory management, resource management
[L1404] [01:11:31.52] was important. I've thought that from
[L1405] [01:11:34.08] the beginning. I didn't think garbage
[L1406] [01:11:36.24] collection was appropriate for a lot of
[L1407] [01:11:38.56] what I was doing, but certainly um
[L1408] [01:11:42.32] automating
[L1409] [01:11:43.92] uh the management was ideal.
[L1410] [01:11:48.56] And so after a long set of discussions
[L1411] [01:11:52.72] we found an interface that people agreed
[L1412] [01:11:55.92] on and uh we put it into C++ 11. And
[L1413] [01:12:02.32] what we found was over the next 10
[L1414] [01:12:05.44] years,
[L1415] [01:12:07.04] the amount of usage of garbage
[L1416] [01:12:09.20] collection decreased
[L1417] [01:12:11.92] as um our AI, the uh resource management
[L1418] [01:12:17.44] that had been there all the time got
[L1419] [01:12:20.08] more and better understood and was used
[L1420] [01:12:23.44] more.
[L1421] [01:12:24.96] Furthermore, the people who still used
[L1422] [01:12:27.04] the garbage collectors didn't use the
[L1423] [01:12:29.36] standard interface because they had
[L1424] [01:12:32.08] figured out ways of doing it better. And
[L1425] [01:12:35.36] so today, there are still a few people
[L1426] [01:12:37.76] doing garbage collection, but it's not
[L1427] [01:12:40.32] part of the standard.
[L1428] [01:12:43.04] >> How does that work? Is it kind of like a
[L1429] [01:12:45.04] wrapper around the uh memory allocation
[L1430] [01:12:48.24] methods?
[L1431] [01:12:49.04] >> Yeah.
[L1432] [01:12:49.76] >> Okay. you you have you have a a
[L1433] [01:12:53.20] different implementation of
[L1434] [01:12:56.72] uh new or maloc or operator new or
[L1435] [01:13:00.64] whatever it is you're using at your
[L1436] [01:13:02.48] lowest level and then um delete becomes
[L1437] [01:13:09.28] something slightly different too.
[L1438] [01:13:11.68] there's this cautionary tale in the C++
[L1439] [01:13:14.48] community about uh this ship Vasa and I
[L1440] [01:13:18.88] was kind of curious like why that's
[L1441] [01:13:20.64] popular and
[L1442] [01:13:21.76] >> oh um
[L1443] [01:13:24.64] we had a meeting in Stockholm at some
[L1444] [01:13:28.00] point and they have a wonderful ship
[L1445] [01:13:31.12] that if you ever get to Stockholm you
[L1446] [01:13:32.96] should see the Vasa. It's a battleship
[L1447] [01:13:35.92] from the 1600s. There's a story to that
[L1448] [01:13:38.96] and that's the one I tell people. Um
[L1449] [01:13:43.12] the king was building was was ordering
[L1450] [01:13:49.12] built a battleship that should be the
[L1451] [01:13:53.12] best and most beautiful battleship
[L1452] [01:13:57.28] around. Uh it was going to be a good
[L1453] [01:14:00.96] fighting battleship and it was going to
[L1454] [01:14:02.72] be used for diplomatic uh visits. So it
[L1455] [01:14:05.60] should be beautiful. [snorts]
[L1456] [01:14:07.60] And uh they laid down the keel and they
[L1457] [01:14:09.92] started building it. And then they heard
[L1458] [01:14:12.24] that a likely opponent was building
[L1459] [01:14:14.96] battleships with two gun decks.
[L1460] [01:14:17.84] And this was an then old-fashioned
[L1461] [01:14:22.48] battleship with only one gun deck. And
[L1462] [01:14:25.12] if you put a two gun a one gun deck
[L1463] [01:14:28.80] battleship next to a two gun deck
[L1464] [01:14:30.72] battleship, the highly predictable
[L1465] [01:14:33.52] result is a lot of holes in the one um
[L1466] [01:14:38.00] gun deck battleship and it it's gone.
[L1467] [01:14:42.08] So the king orders that this ship should
[L1468] [01:14:44.88] now have two gun decks
[L1469] [01:14:48.72] and um they've already started building
[L1470] [01:14:52.00] it.
[L1471] [01:14:54.00] So they add another Glend, they add
[L1472] [01:14:56.48] cannons up there. And the king also
[L1473] [01:14:59.44] wants now the ship is bigger. They want
[L1474] [01:15:02.32] more statues and beautiful things. So it
[L1475] [01:15:06.56] becomes a bit topheavy.
[L1476] [01:15:10.00] And uh rumor has it I've never checked
[L1477] [01:15:13.36] this rumor so it might be wrong. Uh is
[L1478] [01:15:16.08] that the ship designer committed suicide
[L1479] [01:15:19.68] uh out of horror. Um I also a thing that
[L1480] [01:15:25.68] I don't believe is just a rumor was when
[L1481] [01:15:28.64] they was built they tested it for
[L1482] [01:15:31.04] stability. And the way you test a st a
[L1483] [01:15:36.58] [snorts]
[L1484] [01:15:37.12] and ship like that for stability is you
[L1485] [01:15:39.60] take the whole crew and you run them
[L1486] [01:15:41.28] from one side to the other back forth
[L1487] [01:15:44.64] get harmonic uh stair and if you can do
[L1488] [01:15:47.60] that 14 times then uh it'll stand up to
[L1489] [01:15:52.00] the Baltic and the North Sea.
[L1490] [01:15:55.76] Rumor has it actually as I said I think
[L1491] [01:15:59.44] it's a fact um that they did it seven
[L1492] [01:16:02.64] times and then they stopped because it
[L1493] [01:16:05.12] looked dangerous.
[L1494] [01:16:07.92] So um
[L1495] [01:16:11.76] this was
[L1496] [01:16:13.84] 1624
[L1497] [01:16:16.48] I think. Um, the ship gets finished. Uh,
[L1498] [01:16:22.16] it's sailing out. The most wonderful
[L1499] [01:16:24.80] ship you've ever seen. It's sailing out
[L1500] [01:16:27.44] in uh Stockholm Harbor. Trumpets, uh,
[L1501] [01:16:31.28] blaring flags flying, uh, families of
[L1502] [01:16:35.68] crews on board, the whole thing. It gets
[L1503] [01:16:37.84] halfway across the, uh, harbor, a gust
[L1504] [01:16:40.96] of wind comes, it kills the war, and
[L1505] [01:16:43.20] it's gone. And it ends down in some
[L1506] [01:16:46.88] place where there's not much um
[L1507] [01:16:50.16] much oxygen. So it was well preserved
[L1508] [01:16:52.40] and they fished it up again. Uh and you
[L1509] [01:16:54.64] can see it. And so I tell this story to
[L1510] [01:16:58.88] the standards committee and I point out
[L1511] [01:17:01.44] there's something they did wrong. They
[L1512] [01:17:04.56] built more features on top without
[L1513] [01:17:07.20] improving the foundation.
[L1514] [01:17:09.84] always improve the foundation to make
[L1515] [01:17:12.08] sure that it's just not a a random set
[L1516] [01:17:14.64] of features that you have added because
[L1517] [01:17:16.88] that's complexity.
[L1518] [01:17:19.12] Furthermore,
[L1519] [01:17:20.64] do not um compromise your testing.
[L1520] [01:17:26.48] That's really dangerous. And
[L1521] [01:17:29.60] furthermore, uh you you've all noticed
[L1522] [01:17:32.72] when your high bosses say something
[L1523] [01:17:34.96] should be done and the high bosses don't
[L1524] [01:17:37.52] always know what's right. Uh sometimes
[L1525] [01:17:40.64] the professional thing is to say no, we
[L1526] [01:17:43.12] are not doing this. We have to take it
[L1527] [01:17:45.60] easy. If they had said, okay, we'll
[L1528] [01:17:49.12] build a one uh gun battleship. We'll
[L1529] [01:17:52.72] just not call it the Vasa. Call it
[L1530] [01:17:55.44] something neutral. And then next year
[L1531] [01:17:58.32] you can have a battleship that's been
[L1532] [01:18:00.08] designed from the bottom up to be a two
[L1533] [01:18:02.96] gun battleship. You wouldn't have any
[L1534] [01:18:05.52] problems with that. But the high
[L1535] [01:18:08.64] management, meaning the king who was in
[L1536] [01:18:11.04] Poland at the time, so he couldn't even
[L1537] [01:18:12.88] see it, says, "Nope, must be delivered
[L1538] [01:18:15.68] on time." And so they delivered
[L1539] [01:18:18.80] something on time that just couldn't do
[L1540] [01:18:20.96] the job.
[L1541] [01:18:22.32] But go see the ship. It's great.
[L1542] [01:18:25.20] >> At some point uh someone demonstrated
[L1543] [01:18:28.72] that the C++ template instantiation
[L1544] [01:18:32.32] mechanism was turning complete. So you
[L1545] [01:18:36.24] know what the compiler is going to do to
[L1546] [01:18:38.72] kind of pre-process that C++ program can
[L1547] [01:18:42.08] actually be used for computation just uh
[L1548] [01:18:45.12] and I was just trying to understand h
[L1549] [01:18:48.08] how is that possible like how it it was
[L1550] [01:18:50.40] mentioned something about he uh
[L1551] [01:18:53.04] calculated prime numbers at compile
[L1552] [01:18:55.04] time. How does that work?
[L1553] [01:18:57.28] >> Well that's I mean the prime number
[L1554] [01:18:59.52] thing was was just a a curiosity. it uh
[L1555] [01:19:03.12] used the error messages to report the
[L1556] [01:19:06.56] result. But um when you build something
[L1557] [01:19:11.28] uh you can get Turing completeness um
[L1558] [01:19:14.64] you you you need some form of uh iterate
[L1559] [01:19:20.00] or recurse and you need a um [snorts] a
[L1560] [01:19:24.56] comparison and that's about it. then you
[L1561] [01:19:27.84] can get true to incompleteness and the
[L1562] [01:19:31.76] at least some of the theoreticians says
[L1563] [01:19:36.24] we can't do that it'll run forever and
[L1564] [01:19:40.24] um the guy who uh
[L1565] [01:19:43.36] who came up with with the first example
[L1566] [01:19:45.84] of this uh actually thought I should
[L1567] [01:19:49.52] prohibit it somehow I should ban it and
[L1568] [01:19:52.64] my reaction was this looks useful Great.
[L1569] [01:19:57.76] And uh I think I was right. Furthermore,
[L1570] [01:20:01.28] nothing runs forever. If you have a
[L1571] [01:20:03.84] Turing machine, you have the tape
[L1572] [01:20:06.80] and the tape has to be infinite.
[L1573] [01:20:09.76] So if if you imagine building a real
[L1574] [01:20:12.40] cheing machine the way Turing designed
[L1575] [01:20:15.28] it, you have to have a bunch of navies
[L1576] [01:20:18.08] building track all the time when it gets
[L1577] [01:20:20.72] out there. Of course, we don't do that.
[L1578] [01:20:24.00] The point is that the compiler will run
[L1579] [01:20:26.08] out of resources long before we get into
[L1580] [01:20:28.88] real problems. Machines are finite
[L1581] [01:20:33.04] and so the problem does
[L1582] [01:20:36.72] doesn't become real in in unless there's
[L1583] [01:20:39.92] bugs and the bugs get caught guaranteed.
[L1584] [01:20:43.84] So not a problem. What happened though
[L1585] [01:20:47.20] was that people were misusing
[L1586] [01:20:50.16] templates to do simple calculations.
[L1587] [01:20:53.28] like prime numbers or your trust is yeah
[L1588] [01:20:56.48] your sustenance is se or u calculating
[L1589] [01:21:00.88] factorials and such and it's so awful
[L1590] [01:21:05.28] and it's so expensive and it uses up so
[L1591] [01:21:08.80] much memory that it becomes a problem so
[L1592] [01:21:12.88] that was why I and Gabidas re uh built
[L1593] [01:21:16.88] constexer which basically says you can
[L1594] [01:21:20.24] calculate perfectly ordinary code at
[L1595] [01:21:23.12] compile time and it is much simpler,
[L1596] [01:21:27.36] much more what we're used to and much
[L1597] [01:21:32.00] faster to compile uh and giving usually
[L1598] [01:21:35.76] much faster code and um you have that
[L1599] [01:21:39.60] today and you have constant value if you
[L1600] [01:21:41.52] want to guarantee that this is done
[L1601] [01:21:44.70] [snorts]
[L1602] [01:21:45.28] and uh so that takes care of the obvious
[L1603] [01:21:49.52] misuses of the idea of uh templates
[L1604] [01:21:53.28] being during complete it turns them into
[L1605] [01:21:56.24] ordinary functions.
[L1606] [01:21:58.08] >> Generally with programming languages
[L1607] [01:22:00.16] there's this um you know high level
[L1608] [01:22:02.56] intuition that the closer to the machine
[L1609] [01:22:05.12] you are the higher the performance is
[L1610] [01:22:07.76] and um you know I I tend to see C as
[L1611] [01:22:12.16] closer to the machine than C++ for
[L1612] [01:22:14.48] instance. Um no that's not the case.
[L1613] [01:22:17.44] >> It's not the case. It's not as good as
[L1614] [01:22:19.60] compile time calculation at C++ is. And
[L1615] [01:22:23.92] anyway, we have exactly the same machine
[L1616] [01:22:26.24] model because uh um C borrowed the C++
[L1617] [01:22:31.12] 11 machine model. Um so if you write the
[L1618] [01:22:36.00] same code in both languages, it's you
[L1619] [01:22:38.88] get the same result except uh the C++
[L1620] [01:22:42.64] compilers can do more at compile time.
[L1621] [01:22:46.56] And so C++ runs as fast or faster than C
[L1622] [01:22:51.28] in most cases. There's more information
[L1623] [01:22:55.20] if if uh if you give a optimizer more
[L1624] [01:22:58.32] information, it can do a better job.
[L1625] [01:23:00.64] >> Ah, okay. Yeah, because that was what I
[L1626] [01:23:02.64] was going to ask you was you had said
[L1627] [01:23:05.52] somewhere that C++ can be more
[L1628] [01:23:07.36] performant than C, but I tend to think
[L1629] [01:23:10.16] that more abstraction costs you
[L1630] [01:23:12.00] something. But
[L1631] [01:23:12.72] >> it's compiled away. This is why I talk
[L1632] [01:23:15.20] about zero overhead abstraction and
[L1633] [01:23:18.48] people are beginning to take me to task
[L1634] [01:23:20.88] for that because that's underestimating
[L1635] [01:23:24.00] the uh and understating the ability of
[L1636] [01:23:27.12] the C++ compiler. We can do negative
[L1637] [01:23:30.48] overhead uh abstraction.
[L1638] [01:23:34.40] >> What if I was really good at writing
[L1639] [01:23:36.40] assembly and I had all the time in the
[L1640] [01:23:38.40] world to write it. Could that how about
[L1641] [01:23:40.72] how does that compare? If you are very
[L1642] [01:23:43.84] smart and you have infinite time, uh you
[L1643] [01:23:47.68] can do better.
[L1644] [01:23:50.00] Um by and large we are not as smart as
[L1645] [01:23:53.60] the um optimizers anymore and we don't
[L1646] [01:23:57.92] have infinite time.
[L1647] [01:24:00.16] So if we are uh smart enough, we can
[L1648] [01:24:03.52] only do a small piece of code. And now
[L1649] [01:24:07.36] um the question is did we get enough
[L1650] [01:24:10.48] time to use our smarts.
[L1651] [01:24:13.28] Uh this is even starting to affect
[L1652] [01:24:18.40] uh clever code.
[L1653] [01:24:21.04] I gave a talk to uh Slack last year
[L1654] [01:24:24.56] which is a group of uh very performant
[L1655] [01:24:28.32] uh interested people from the finance
[L1656] [01:24:31.04] industry
[L1657] [01:24:32.72] and my title was don't be clever.
[L1658] [01:24:37.20] Actually the written title was don't be
[L1659] [01:24:39.20] too clever but I can't pronounce
[L1660] [01:24:41.12] parenthesis.
[L1661] [01:24:42.80] Um and I got out alive.
[L1662] [01:24:46.72] Um, and my main point was that C++ is
[L1663] [01:24:50.96] good enough
[L1664] [01:24:52.72] for uh more than 98% of your code. So if
[L1665] [01:24:57.28] you want time to be clever,
[L1666] [01:25:00.16] you use these techniques and I showed
[L1667] [01:25:02.16] modern C++
[L1668] [01:25:04.56] and that way you get time so you can do
[L1669] [01:25:07.36] all the clever optimizations. The
[L1670] [01:25:09.52] problem is clever optimizations these
[L1671] [01:25:11.92] days tend to be machine dependent. That
[L1672] [01:25:15.44] is if you get a new
[L1673] [01:25:18.96] computer or if you get a new version of
[L1674] [01:25:21.60] the compiler, you might actually have
[L1675] [01:25:24.08] pessimized your code. I've seen this
[L1676] [01:25:26.96] repeatedly ever since the uh the 80s. uh
[L1677] [01:25:32.64] and there there there's people who does
[L1678] [01:25:35.20] nothing but uh u using different
[L1679] [01:25:39.12] optimizations on the next generation
[L1680] [01:25:41.44] hardware
[L1681] [01:25:43.12] and u my standard techniques for um for
[L1682] [01:25:48.08] for improving things actually is to
[L1683] [01:25:51.68] first throw away the clever stuff
[L1684] [01:25:54.80] and then see if you run faster or
[L1685] [01:25:57.60] slower. Usually you run faster because
[L1686] [01:26:01.28] clever stuff tends and at least 1990s
[L1687] [01:26:05.92] story style clever stuff which is
[L1688] [01:26:07.68] there's a lot of it still today because
[L1689] [01:26:10.48] the techniques uh carry on in people's
[L1690] [01:26:13.44] heads and uh some of the code remains uh
[L1691] [01:26:18.16] tend to use a right nest of pointers
[L1692] [01:26:21.36] and that uh gives the compilers and
[L1693] [01:26:24.72] optimizers problems.
[L1694] [01:26:27.36] They also sometimes use uh more
[L1695] [01:26:30.48] allocations
[L1696] [01:26:32.16] which is not good. You want to minimize
[L1697] [01:26:34.40] memory access. You want to maximize uh
[L1698] [01:26:38.32] your cache performance and things like
[L1699] [01:26:41.12] that. And compilers are getting very
[L1700] [01:26:43.76] good at that. And I have seen th this
[L1701] [01:26:47.84] kind of thinking. I wrote a paper about
[L1702] [01:26:50.56] it together with a friend of mine in
[L1703] [01:26:52.72] Spain doing flu fluid dynamics and uh uh
[L1704] [01:26:57.92] we we we threw away uh the clever stuff
[L1705] [01:27:01.20] for a uh
[L1706] [01:27:05.04] actually a performance uh test suite
[L1707] [01:27:08.88] example. So it was not toy and we got
[L1708] [01:27:12.96] only 20% improvement
[L1709] [01:27:16.40] by reducing the code to about 80% of
[L1710] [01:27:20.00] what it was before and so some people
[L1711] [01:27:24.00] didn't think that was significant. I
[L1712] [01:27:26.48] thought it was significant proof that
[L1713] [01:27:28.80] the technique was appropriate. You apply
[L1714] [01:27:31.84] optimizations only when you need them.
[L1715] [01:27:35.68] Kuth says don't do premature
[L1716] [01:27:38.00] optimization but he also pointed out
[L1717] [01:27:40.48] that two to 3% is where you uh where you
[L1718] [01:27:44.32] should optimize which is exactly the
[L1719] [01:27:46.64] number I'm using
[L1720] [01:27:49.44] and so first build the stuff using high
[L1721] [01:27:53.44] level facilities
[L1722] [01:27:55.36] see if it's good enough and if it isn't
[L1723] [01:27:58.56] uh and you have to time it you don't
[L1724] [01:28:00.88] guess you time uh then you uh up then
[L1725] [01:28:05.76] you figure out where the time is spent
[L1726] [01:28:07.60] and then you optimize that
[L1727] [01:28:10.24] but a lot of the time you don't need to
[L1728] [01:28:12.64] go to that stage it's it's fast enough
[L1729] [01:28:16.00] >> I see so when you say cleverness here
[L1730] [01:28:18.16] it's um like human level a manual
[L1731] [01:28:21.60] management to ek out performance
[L1732] [01:28:23.84] >> yes
[L1733] [01:28:24.32] >> and you're saying that actually if you
[L1734] [01:28:26.72] don't do that the compile you're giving
[L1735] [01:28:28.48] the compiler more to optimize and it can
[L1736] [01:28:30.88] do a good job
[L1737] [01:28:32.08] >> and it's much much better than it used
[L1738] [01:28:34.24] to
[L1739] [01:28:35.28] code that was cleverly and correctly
[L1740] [01:28:38.32] optimized in the 1990s
[L1741] [01:28:42.00] are often pessimized today
[L1742] [01:28:45.68] because machine architectures have
[L1743] [01:28:47.60] changed
[L1744] [01:28:49.12] and the compilers have improved. When I
[L1745] [01:28:52.00] look at the industry today, um more and
[L1746] [01:28:55.12] more of code is being written by
[L1747] [01:28:58.24] machines than humans. And I I feel like
[L1748] [01:29:01.04] a lot of programming language design is
[L1749] [01:29:03.60] thinking about how do you make it u
[L1750] [01:29:07.12] amendable to humans solving problems and
[L1751] [01:29:09.44] writing the code. And I'm curious if you
[L1752] [01:29:11.60] have any thoughts on if you think
[L1753] [01:29:13.44] programming language design will change
[L1754] [01:29:15.36] if more and more of the code is written
[L1755] [01:29:17.92] by you know models and machines. I
[L1756] [01:29:23.28] think that in the field I'm mostly
[L1757] [01:29:26.32] interested in,
[L1758] [01:29:28.56] code will still be written by humans
[L1759] [01:29:31.92] and they will use abstraction.
[L1760] [01:29:34.40] The examples I've seen of attempts for
[L1761] [01:29:39.20] AI to generate code in this domain
[L1762] [01:29:43.12] uh has not been successful.
[L1763] [01:29:45.60] it uh they generate more bugs, more
[L1764] [01:29:49.12] security holes. They have uh bloated
[L1765] [01:29:52.48] code which pessimize again because you
[L1766] [01:29:56.08] use more memory
[L1767] [01:29:58.32] and um it's hard to validate
[L1768] [01:30:03.04] and the senior developers that would be
[L1769] [01:30:06.00] needed to validate it um I've seen some
[L1770] [01:30:10.00] of them starting to retire because they
[L1771] [01:30:12.80] don't want to deal with the validation
[L1772] [01:30:14.96] of something that changes every time you
[L1773] [01:30:17.20] make a change in your code in your
[L1774] [01:30:19.28] prompts.
[L1775] [01:30:20.88] And furthermore, a lot of the things I
[L1776] [01:30:24.16] think about um there's regulatory
[L1777] [01:30:27.76] bodies, there's validation. You have to
[L1778] [01:30:30.40] be able to validate what you changed
[L1779] [01:30:32.48] when you make a change. And the AIS the
[L1780] [01:30:36.16] the tools change the uh even if you make
[L1781] [01:30:39.92] a slight different prompt, the uh a lot
[L1782] [01:30:43.04] of the code will change and you have to
[L1783] [01:30:45.44] now check it again.
[L1784] [01:30:47.92] all of the code that was generated and
[L1785] [01:30:49.84] know there's more code generated than if
[L1786] [01:30:51.68] it was written by humans. And when a
[L1787] [01:30:54.80] human make a change, it it'll make a
[L1788] [01:30:57.44] change that's localized and you can look
[L1789] [01:31:00.08] for the effects of that localized
[L1790] [01:31:02.56] change. If an AI writes it, uh it uh it
[L1791] [01:31:07.52] you don't actually know where it's
[L1792] [01:31:09.12] changed. You have to try and figure that
[L1793] [01:31:11.12] out. So if you're doing something that
[L1794] [01:31:14.40] has been done many times before, you
[L1795] [01:31:17.28] write a standard web app, uh what you
[L1796] [01:31:20.24] say is correct. Um also AI is not
[L1797] [01:31:24.48] useless. That's not what I'm saying. It
[L1798] [01:31:26.96] can be used to write uh documentation.
[L1799] [01:31:30.32] Again, it has to be humanly validated,
[L1800] [01:31:33.52] but it helps write uh things. It's good
[L1801] [01:31:36.80] at text.
[L1802] [01:31:38.72] It's not
[L1803] [01:31:41.92] at least now good at
[L1804] [01:31:46.32] um
[L1805] [01:31:48.16] safety critical performance critical uh
[L1806] [01:31:51.44] code. Now
[L1807] [01:31:54.24] let's say that 70 or 80% of the code of
[L1808] [01:31:57.76] the world's code doesn't fit that
[L1809] [01:31:59.76] pattern but it's the that 10 20% of the
[L1810] [01:32:05.68] code that I'm interested in and there
[L1811] [01:32:08.88] it's not there and I don't see it coming
[L1812] [01:32:11.60] with the LLM model. Furthermore, ILM
[L1813] [01:32:17.04] when fed with training data
[L1814] [01:32:22.48] has to be trained with old code.
[L1815] [01:32:25.68] And my job as I see it is to make sure
[L1816] [01:32:30.96] people write new things and use new
[L1817] [01:32:33.44] techniques that are improvement over the
[L1818] [01:32:35.92] old code. So I find that LLM based code
[L1819] [01:32:42.72] is imitating old code and getting old
[L1820] [01:32:47.04] performance and old bugs.
[L1821] [01:32:50.24] Uh again maybe you can improve that. I
[L1822] [01:32:53.76] hear rumors of Biana apps being written.
[L1823] [01:32:57.36] Uh that's fed my uh writings, but even
[L1824] [01:33:01.60] that is problematic because I'm not
[L1825] [01:33:03.68] saying exactly the same as I did 20
[L1826] [01:33:06.32] years ago. But anyway, we we'll we'll
[L1827] [01:33:08.64] see. Um
[L1828] [01:33:11.36] also even Dystra was looking into the
[L1829] [01:33:14.96] possibility and he claimed that um the
[L1830] [01:33:18.88] idea of having natural languages being
[L1831] [01:33:23.44] the programming language was idiotic. He
[L1832] [01:33:26.56] is less polite than I am. And um I think
[L1833] [01:33:31.44] that a language like English is very
[L1834] [01:33:34.64] flexible and what we say is often very
[L1835] [01:33:38.96] ambiguous. We need a programming
[L1836] [01:33:41.20] language that's precise that's that's
[L1837] [01:33:43.92] engineering that's math. It's not
[L1838] [01:33:46.56] English.
[L1839] [01:33:48.48] And for that code that is uh performance
[L1840] [01:33:51.68] or safety critical I imagine there will
[L1841] [01:33:54.64] be some uh group of people that is using
[L1842] [01:33:57.60] uh LLM for that and I guess based off
[L1843] [01:34:00.56] what you're saying is the intuition that
[L1844] [01:34:02.80] you would foresee more breakages and
[L1845] [01:34:06.08] bugs and uh you know because it's not
[L1846] [01:34:09.76] valid
[L1847] [01:34:10.16] >> and the people that are really good at
[L1848] [01:34:12.64] that kind of stuff uh tend to to not
[L1849] [01:34:17.12] want to spend all their time validating.
[L1850] [01:34:20.08] Another problem is that they want to
[L1851] [01:34:22.24] eliminate
[L1852] [01:34:23.76] junior programmers because there's lots
[L1853] [01:34:26.08] of them. But if you do that, where do
[L1854] [01:34:29.60] you get the senior programmers from?
[L1855] [01:34:32.88] We will see. I mean, you can ask me the
[L1856] [01:34:34.88] same question again in 10 years and
[L1857] [01:34:36.72] there will be more knowledge and uh
[L1858] [01:34:39.84] undoubtedly some of what I said will not
[L1859] [01:34:41.92] be correct and my guess is some of what
[L1860] [01:34:44.32] I say will be correct in 10 years. I'm
[L1861] [01:34:47.76] always told by AI uh proponents that
[L1862] [01:34:53.20] uh either the problem has already been
[L1863] [01:34:55.12] solved or it'll be solved in the next
[L1864] [01:34:57.04] release.
[L1865] [01:34:58.72] But I I hear anthropic 4.7 is having
[L1866] [01:35:04.48] more problems than 4.6
[L1867] [01:35:07.28] uh for reasons I don't understand. But
[L1868] [01:35:11.20] the the idea that the next version will
[L1869] [01:35:15.12] solve the problem uh is is always a a
[L1870] [01:35:18.32] dangerous assumption. Furthermore,
[L1871] [01:35:21.44] it's getting more and more expensive. If
[L1872] [01:35:23.76] you have to build a hundred million uh
[L1873] [01:35:26.56] dollar um
[L1874] [01:35:29.04] center and use and run the electricity
[L1875] [01:35:32.24] for it, how many junior developers uh
[L1876] [01:35:35.60] does it take to be cheaper?
[L1877] [01:35:39.52] um they they're starting to uh need
[L1878] [01:35:42.00] money. It's it's not un problematic and
[L1879] [01:35:47.20] I'm in a sub field where it is probably
[L1880] [01:35:50.08] more problematic than most.
[L1881] [01:35:54.56] One thing I saw in in a profile that you
[L1882] [01:35:57.44] did is they asked you what keeps you
[L1883] [01:36:00.40] going on C++ or what motivates you and
[L1884] [01:36:03.36] you said one is the fun of kind of
[L1885] [01:36:06.72] building the the future and the second
[L1886] [01:36:09.52] thing was the obligation to make sure
[L1887] [01:36:13.12] C++ moves forward and like when you
[L1888] [01:36:16.00] started C++ I can't imagine you knew
[L1889] [01:36:19.04] that you were embarking on a journey for
[L1890] [01:36:21.04] decades and so
[L1891] [01:36:22.64] >> not not decades But I knew it was a
[L1892] [01:36:25.36] longer journey because I knew I couldn't
[L1893] [01:36:27.68] build the language I wanted. I could
[L1894] [01:36:30.64] build a a subset of it. And there was
[L1895] [01:36:33.76] two reasons for that. One was well, I
[L1896] [01:36:36.24] was a I was a team that did it. Um
[L1897] [01:36:39.76] secondly, um so lack of resources, lack
[L1898] [01:36:43.04] of time, and secondly, I didn't have the
[L1899] [01:36:46.08] input needed to make sure that what I
[L1900] [01:36:50.32] designed was right. And so we have the
[L1901] [01:36:53.84] engineering issue. Build what you can,
[L1902] [01:36:56.96] see what works, improve it. And so I
[L1903] [01:37:00.56] knew I was getting into something like
[L1904] [01:37:03.52] that. I knew I was building a language
[L1905] [01:37:06.32] meant to evolve. And meant to evolve
[L1906] [01:37:09.20] means that you make certain decisions in
[L1907] [01:37:12.80] um knowing that that is different. For
[L1908] [01:37:16.16] instance, I that's one reason C++ wasn't
[L1909] [01:37:20.40] just a uh object-oriented programming
[L1910] [01:37:23.52] language because I could see in the
[L1911] [01:37:26.56] world that there was things that didn't
[L1912] [01:37:29.28] seem to fit that paradigm.
[L1913] [01:37:32.16] And so I I knew we would evolve. The
[L1914] [01:37:35.92] other half of that answer to that
[L1915] [01:37:37.92] question, what keeps me going is
[L1916] [01:37:40.16] applications.
[L1917] [01:37:42.00] It's really nice to see interesting uses
[L1918] [01:37:45.44] and in such. So I was at JPL and uh I
[L1919] [01:37:50.40] talked to the people was doing the Mars
[L1920] [01:37:52.16] rovers. That's cool stuff. I've been to
[L1921] [01:37:54.96] J uh I've been to CERN. I'm going to
[L1922] [01:37:57.76] CERN this summer to see how you do high
[L1923] [01:38:00.64] energy physics. I don't know anything
[L1924] [01:38:02.88] about high energy physics. Well,
[L1925] [01:38:05.68] probably more than the average, but but
[L1926] [01:38:08.08] nowhere near being a physicist. And so
[L1927] [01:38:10.80] you can go there and see they do
[L1928] [01:38:12.48] interesting things and there's things
[L1929] [01:38:14.88] that surprise you. So I was talking to a
[L1930] [01:38:18.16] guy in CERN some years ago and
[L1931] [01:38:20.96] [clears throat] his job was to open and
[L1932] [01:38:23.60] close doors.
[L1933] [01:38:27.36] These doors weigh a couple of tons and
[L1934] [01:38:30.64] are made of lead and they move across to
[L1935] [01:38:34.56] close off an area to protect against
[L1936] [01:38:38.16] radiation or something like that. I
[L1937] [01:38:40.08] don't know the details, but the point is
[L1938] [01:38:42.40] he has to start up this door, which is
[L1939] [01:38:45.44] not too hard. You have engines, but then
[L1940] [01:38:47.68] you have to make sure you stop it
[L1941] [01:38:49.52] because when you have a couple of tons
[L1942] [01:38:52.40] uh this wide going into a wall, it will
[L1943] [01:38:56.32] not stop normally. Uh you have to write
[L1944] [01:38:59.04] and the code for that was was
[L1945] [01:39:01.12] interesting. I learned something and uh
[L1946] [01:39:04.08] I still travel around and uh talk to
[L1947] [01:39:07.68] people and see what C++ is being used
[L1948] [01:39:10.56] for and what it can be used for and what
[L1949] [01:39:13.28] it can't be used for. Just learning and
[L1950] [01:39:16.48] learning is fun.
[L1951] [01:39:18.48] >> There's a a few quotes that you have
[L1952] [01:39:20.80] which I thought would be interesting
[L1953] [01:39:22.80] kind of if you could just give some
[L1954] [01:39:24.24] context behind them. Well, one of the
[L1955] [01:39:26.64] quotes is C makes it easy to shoot
[L1956] [01:39:29.84] yourself in the foot. C++ makes it
[L1957] [01:39:32.64] harder, but when you do it, it blows
[L1958] [01:39:34.72] your whole leg off.
[L1959] [01:39:36.16] >> Yeah. Yeah. I I um somebody asked a
[L1960] [01:39:39.20] question at a talk I was given in uh
[L1961] [01:39:43.20] Boston back in the 80s and I shot that
[L1962] [01:39:46.56] one back. Well, not not not thinking. Um
[L1963] [01:39:50.64] but it's a good quote and it's correct.
[L1964] [01:39:53.68] Um,
[L1965] [01:39:55.28] Arnold Penes
[L1966] [01:39:57.28] got in the Nobel Prize in physics, so
[L1967] [01:39:59.12] he's not a nobody, was one trying to
[L1968] [100:01.76] explain to a large group of uh, Bell
[L1969] [100:07.60] Labs managers about C++.
[L1970] [100:11.44] And he says, you can't have a power tool
[L1971] [100:16.16] without knowing how to use it. So if you
[L1972] [100:19.20] have a saw, you saw like this. If you
[L1973] [100:23.04] have a power saw and you try and do
[L1974] [100:26.40] that, it'll bounce
[L1975] [100:29.12] and you will have to be very lucky not
[L1976] [100:31.84] to get hurt.
[L1977] [100:34.00] Notice it's roughly the same story.
[L1978] [100:37.76] Uh and so what is behind that is if you
[L1979] [100:41.92] get a power tool and you misuse it, you
[L1980] [100:45.36] will get more uh problems. Get a car
[L1981] [100:48.80] that accelerate faster and it can wrap
[L1982] [100:51.68] you around the tree uh in a way a
[L1983] [100:55.52] old-fashioned slow accelerating car
[L1984] [100:58.72] can't. It's fundamental to having power
[L1985] [101:01.68] tools.
[L1986] [101:03.28] >> You also have this other great quote.
[L1987] [101:04.80] It's um nobody should call themselves a
[L1988] [101:07.68] professional if they only know one
[L1989] [101:09.60] language. I obviously you'd recommend
[L1990] [101:12.08] people learn C++, but if they had to
[L1991] [101:14.96] know a second or a third language for
[L1992] [101:17.04] the sake of you know being a better
[L1993] [101:19.68] engineer or programmer, what would you
[L1994] [101:21.60] recommend?
[L1995] [101:22.72] >> Yeah. And uh if you've heard if you've
[L1996] [101:26.72] seen that interview, you'll know I
[L1997] [101:28.48] waffle on that deliberately.
[L1998] [101:32.24] uh it is not so much which other
[L1999] [101:34.56] languages you know but that you get a
[L2000] [101:38.56] set of ideas that are embedded in those
[L2001] [101:42.08] languages. So what you should do is to
[L2002] [101:45.68] learn languages that are different from
[L2003] [101:48.08] yours
[L2004] [101:49.92] and um I'm not too
[L2005] [101:54.72] fuzzy about which languages they are. I
[L2006] [101:57.60] think I said uh learn learn a scripting
[L2007] [102:02.32] language today that would be Python or
[L2008] [102:05.76] JavaScript. Uh then I guess it was Unix
[L2009] [102:09.20] shell or something like that. Um have a
[L2010] [102:12.72] look at a functional language uh ML or
[L2011] [102:16.72] hasll would be obvious uh solutions or
[L2012] [102:20.72] just pick something
[L2013] [102:23.12] different. The point is that you mustn't
[L2014] [102:26.24] get stuck with just what's in your
[L2015] [102:29.04] language. It It's like it's not good for
[L2016] [102:32.08] you to be monogl
[L2017] [102:34.88] you you know what you call somebody who
[L2018] [102:37.12] knows three languages triilingual who
[L2019] [102:39.76] knows two languages bilingual
[L2020] [102:42.56] uh one language American [laughter]
[L2021] [102:45.68] is a a very popular joke at least
[L2022] [102:48.08] outside America.
[L2023] [102:50.16] Um, and it's the same idea with
[L2024] [102:52.72] programming languages, but it's more
[L2025] [102:54.56] important with programming languages, I
[L2026] [102:56.64] think. Um, because uh you you're you're
[L2027] [103:01.28] building things and you shouldn't you
[L2028] [103:03.92] you should broaden your mind uh with
[L2029] [103:06.80] ideas and techniques.
[L2030] [103:08.88] >> Another quote is people people who think
[L2031] [103:11.12] they know everything really annoy those
[L2032] [103:14.08] of us who know we don't. And I was
[L2033] [103:17.12] curious the context behind that or your
[L2034] [103:19.20] thoughts on
[L2035] [103:20.00] >> Well, that's I mean that's that's very
[L2036] [103:22.08] simple. It's there's so many people who
[L2037] [103:26.72] who who think there simple solutions to
[L2038] [103:29.52] just about everything in the world. Uh
[L2039] [103:32.00] in this context they they'll come and
[L2040] [103:34.32] tell me how how much simpler C++ could
[L2041] [103:37.12] be. And this is true. Um if you only
[L2042] [103:42.00] want to do one thing usually the one
[L2043] [103:44.32] they have in mind you can make a much
[L2044] [103:47.12] simp simpler language but
[L2045] [103:50.64] this is like uh if we throw away this
[L2046] [103:53.36] part of C++ it will be much simpler
[L2047] [103:56.40] nicer usually they want to throw away
[L2048] [103:58.96] things like C. So but then you annoy a
[L2049] [104:02.56] few million people
[L2050] [104:04.88] and you don't actually succeed because
[L2051] [104:06.96] they'll stick to the old stuff. So um
[L2052] [104:10.88] it's a it's a way of expressing my
[L2053] [104:15.12] frustration with people who
[L2054] [104:16.64] oversimplify.
[L2055] [104:18.64] Uh people think they can program without
[L2056] [104:21.92] being learning to program. Uh they think
[L2057] [104:25.36] they can be engineers without learning
[L2058] [104:27.60] engineering. They think they can be
[L2059] [104:30.24] politicians without knowing how to run a
[L2060] [104:33.76] company or a country. Um it's it's
[L2061] [104:37.92] oversimplification annoys me and I
[L2062] [104:41.12] probably shouldn't express annoyance. I
[L2063] [104:43.36] very rarely do but uh in this particular
[L2064] [104:46.96] case it my my frustration showed.
[L2065] [104:50.56] >> Yeah. I think I saw somewhere kind of in
[L2066] [104:52.80] response to C++ being difficult for some
[L2067] [104:56.48] people people who have the perspective
[L2068] [104:58.56] of you know programming should be
[L2069] [105:00.80] approachable and you know anyone can
[L2070] [105:03.20] learn programming. And I think you you
[L2071] [105:05.52] expressed the opinion that C++ is not
[L2072] [105:09.20] necessarily for everyone. It's for
[L2073] [105:10.96] serious programmers.
[L2074] [105:12.16] >> Yeah. I mean uh the the first
[L2075] [105:16.96] line of the C++ programming language uh
[L2076] [105:21.52] version one first edition was uh C++ is
[L2077] [105:28.24] designed to make life more pleasant for
[L2078] [105:32.08] the serious programmer and I took away
[L2079] [105:36.08] the first version which was professional
[L2080] [105:38.40] because I saw amateurs that was really
[L2081] [105:40.56] really good. So a serious programmer is
[L2082] [105:45.12] probably programming for somebody else.
[L2083] [105:48.80] If you program for yourself, it doesn't
[L2084] [105:50.88] matter. It's your it's it's you. Uh and
[L2085] [105:55.28] that's your problem. If you do it for
[L2086] [105:57.84] your friends, you can lose friends. If
[L2087] [106:00.32] you build something for a million
[L2088] [106:02.32] people, you can do harm in the world.
[L2089] [106:05.60] And so that's what it's for. Um
[L2090] [106:10.96] I uh I mean Gildolf and Russen built um
[L2091] [106:15.36] built Python with the explicit aim of
[L2092] [106:18.64] allowing many people or even or
[L2093] [106:21.20] everybody to program and he succeeded.
[L2094] [106:25.76] I designed C++ to be a really good tool
[L2095] [106:29.92] for serious programmers, for engineers
[L2096] [106:32.72] and mathematicians and such and I
[L2097] [106:35.52] succeeded too.
[L2098] [106:37.76] Um, it's just not the same problem.
[L2099] [106:40.88] Remember where we started? I said the
[L2100] [106:43.28] problem look at the problem and then
[L2101] [106:45.20] learn from uh what worked and what
[L2102] [106:47.52] doesn't. Looking back on C++ and the
[L2103] [106:50.88] whole journey, is there any part where
[L2104] [106:53.76] you think oh that that was a mistake or
[L2105] [106:55.84] something that you learned from in the
[L2106] [106:57.76] design?
[L2107] [107:00.24] >> Many many uh times I learned something.
[L2108] [107:04.96] Um
[L2109] [107:08.32] I think most of the things never made it
[L2110] [107:12.00] into C++.
[L2111] [107:14.08] That is that's what you have experiments
[L2112] [107:16.72] for.
[L2113] [107:18.48] And that's what you have initial uses
[L2114] [107:21.92] for.
[L2115] [107:24.56] I think I got the major part of the
[L2116] [107:28.24] language right
[L2117] [107:30.80] and I think I could improve every single
[L2118] [107:34.32] detail.
[L2119] [107:36.56] But
[L2120] [107:38.16] stability, compatibility
[L2121] [107:41.04] is essential.
[L2122] [107:42.96] If you make an insignificant change, it
[L2123] [107:45.44] will annoy a few people and it wouldn't
[L2124] [107:47.28] matter. If you make a significant
[L2125] [107:50.08] change, you will annoy a lot of people
[L2126] [107:52.32] and it will not work because uh say a
[L2127] [107:56.08] million people will stick to the old
[L2128] [107:57.84] way.
[L2129] [108:00.16] So, um I I try to
[L2130] [108:04.64] grow the language without breaking it.
[L2131] [108:08.72] Um I have this thing that happens again
[L2132] [108:11.04] and again. and I explain it. People come
[L2133] [108:14.24] up and say to me C++ is too complicated.
[L2134] [108:18.96] Yeah. Um you you you must simplify it.
[L2135] [108:25.28] And I need these two features. I need
[L2136] [108:28.56] them yesterday. You must when you're
[L2137] [108:30.72] doing this. Give me these two features.
[L2138] [108:34.24] Yes.
[L2139] [108:36.16] And whatever you do, don't break my
[L2140] [108:38.08] code. I have a million lines of it.
[L2141] [108:42.16] That doesn't work. That's impossible.
[L2142] [108:45.68] And so that is why I'm working on coding
[L2143] [108:48.08] guidelines and on profiles which is
[L2144] [108:51.20] enforced guidelines. That way you can
[L2145] [108:54.48] design a profile that ensures that you
[L2146] [108:59.68] can use the libraries that you need and
[L2147] [109:02.96] ensure that you don't misuse the
[L2148] [109:05.28] features that are
[L2149] [109:08.32] unnecessary. and dangerous in your
[L2150] [109:11.44] field. for anyone who wants to um you
[L2151] [109:15.44] know learn C++ I think a common question
[L2152] [109:17.68] is like what is the you know top
[L2153] [109:20.48] technical book recommendation that you
[L2154] [109:22.40] would have
[L2155] [109:24.24] learn modern C++
[L2156] [109:26.72] there's a book I wrote when I was
[L2157] [109:29.12] teaching undergrads this this is
[L2158] [109:30.88] accidental I didn't mean it to be there
[L2159] [109:33.20] but anyway this is a second edition of
[L2160] [109:36.32] uh programming principles and practice
[L2161] [109:38.40] using C++ this is a big fat book um
[L2162] [109:42.64] written for undergrads. The third
[L2163] [109:45.44] edition is not as thick because the
[L2164] [109:48.72] language has improved and uh I can
[L2165] [109:51.36] actually um get the ideas across uh
[L2166] [109:55.28] better with less text. Um but use the
[L2167] [110:00.88] latest uh C++ learn the modern way
[L2168] [110:04.00] first. Don't start learning all the bad
[L2169] [110:07.28] ways of writing C as the starter. And a
[L2170] [110:10.88] lot of courses still says you learn C
[L2171] [110:14.08] first. So you learn some issues maloc
[L2172] [110:17.12] and uh pointers and uh then
[L2173] [110:21.76] later you can learn how to use a vector
[L2174] [110:23.92] on a string and not have the problems.
[L2175] [110:27.04] But
[L2176] [110:28.56] yeah, profiles are there
[L2177] [110:32.72] to be able to have compiler and static
[L2178] [110:36.08] analyzer support for that kind of
[L2179] [110:38.96] thinking.
[L2180] [110:40.40] And educators are asking for something
[L2181] [110:42.48] like that too. A lot of people think the
[L2182] [110:45.12] profile simply is to deal with memory
[L2183] [110:48.00] safety and performance. No, it it has to
[L2184] [110:52.08] give people a better tool uh both for
[L2185] [110:55.44] learning and for doing specific kinds of
[L2186] [110:58.08] work.
[L2187] [110:59.28] >> And then last question for you is if you
[L2188] [111:01.68] could go back to the beginning of your
[L2189] [111:03.60] career and give yourself some advice,
[L2190] [111:05.36] what would you say?
[L2191] [111:06.88] >> Oh dear. Yeah, that's a time machine
[L2192] [111:08.88] question. I I sometimes set that for uh
[L2193] [111:12.88] my students.
[L2194] [111:14.72] Uh you have a time machine. Go back and
[L2195] [111:17.36] uh give Dennis some advice and uh once
[L2196] [111:19.84] you've done that uh uh step 10 years uh
[L2197] [111:24.24] for forward and give me some advice.
[L2198] [111:27.44] It's a it's a good exercise. I usually I
[L2199] [111:30.24] usually get some really good stories out
[L2200] [111:32.32] of it, some suggestions.
[L2201] [111:35.04] Um,
[L2202] [111:39.68] I think
[L2203] [111:43.12] a lot of
[L2204] [111:47.60] I I I tried to avoid the two-way
[L2205] [111:52.16] conversions in of the built-in types and
[L2206] [111:55.28] C.
[L2207] [111:57.20] I should have fought harder for that. I
[L2208] [111:59.36] tried but uh was stopped by the people
[L2209] [112:02.80] in in in Bell Labs. Um and these were
[L2210] [112:07.76] more experienced people than me and
[L2211] [112:09.76] such. Now I I should have should have
[L2212] [112:12.72] gone further there. Furthermore, I
[L2213] [112:15.52] should have delayed the release of C++
[L2214] [112:20.08] till I could have something template
[L2215] [112:22.48] like so I could do a better uh standard
[L2216] [112:25.12] library.
[L2217] [112:27.44] um it wouldn't have been good enough,
[L2218] [112:30.08] but it would have gotten people into the
[L2219] [112:32.24] habit of of using a standard. Everybody
[L2220] [112:35.20] was building standard libraries and we
[L2221] [112:37.20] got saved by uh Alex Stefanov with the
[L2222] [112:40.48] STL. Uh but that was that was real luck
[L2223] [112:45.12] because I made a mistake in in not
[L2224] [112:48.56] delaying till I could have built a a a
[L2225] [112:52.00] good vector and uh class hierarchy. uh
[L2226] [112:56.80] stuff.
[L2227] [112:58.32] And then finally,
[L2228] [113:01.12] if I'd known what I know now about
[L2229] [113:04.40] standards committees and bloated
[L2230] [113:06.96] bureaucracies and we have more subgroups
[L2231] [113:10.56] now than we had members to start out
[L2232] [113:12.88] with, I would have tried very hard to
[L2233] [113:16.48] set up a
[L2234] [113:19.44] um some kind of
[L2235] [113:23.44] steering group so that people could make
[L2236] [113:27.04] suggestions. But
[L2237] [113:29.76] we wouldn't have a vote with say 500
[L2238] [113:33.76] people. We would have suggestions from a
[L2239] [113:36.56] community of 500 people and we would
[L2240] [113:39.28] have maybe a group of five or six people
[L2241] [113:44.40] uh with vast experience and cared for
[L2242] [113:47.20] the whole language who made the
[L2243] [113:49.76] decisions based on what was proposed.
[L2244] [113:52.80] Something like that. But I did not have
[L2245] [113:55.92] the experience or the knowledge to make
[L2246] [113:57.92] such a suggestion.
[L2247] [114:00.00] Uh notice that I did not mention tools.
[L2248] [114:03.68] C++ has a weakness in tools
[L2249] [114:07.20] and that was because it grew up early in
[L2250] [114:12.24] a time with limited tools, limited uh
[L2251] [114:19.92] compute power, limited memory. So I
[L2252] [114:22.96] couldn't have done it. One constraint on
[L2253] [114:25.84] the exercise I give to the uh students
[L2254] [114:28.80] for time machines is try and make sure
[L2255] [114:31.92] that it would be possible to follow your
[L2256] [114:33.92] advice.
[L2257] [114:35.92] And uh if I just said I want this then a
[L2258] [114:40.56] lot of the things couldn't be done till
[L2259] [114:44.72] uh 20 years later and therefore would
[L2260] [114:48.00] never have happened. There's a lot of
[L2261] [114:50.00] languages designed to be perfect
[L2262] [114:53.52] uh for the future uh computers and the
[L2263] [114:56.64] future programmers. Most of them die
[L2264] [115:00.40] because by the time 10 years later they
[L2265] [115:03.28] get the language, the world has changed
[L2266] [115:07.20] >> on that first one. I imagine that would
[L2267] [115:09.76] have been really tough to do because the
[L2268] [115:12.40] the Bell Labs people were so senior.
[L2269] [115:15.36] >> I I failed. I tried. Um, but it's it's
[L2270] [115:19.12] obvious that you don't want narrowing
[L2271] [115:21.60] conversions. I even wrote a paper about
[L2272] [115:24.40] how to get rid of them uh today in a
[L2273] [115:26.96] library
[L2274] [115:28.48] uh last year. But it is a fundamental
[L2275] [115:34.80] flaw in the type system of C and C++.
[L2276] [115:38.48] And it came because they needed they
[L2277] [115:42.56] being people like Dennis Richie and the
[L2278] [115:45.12] Unix team and so they needed to be able
[L2279] [115:47.76] to handle both integers and floating
[L2280] [115:49.76] point and they didn't think of explicit
[L2281] [115:54.48] type conversion and they thought
[L2282] [115:56.56] explicit type conversion was too clunky.
[L2283] [115:59.84] They didn't actually get casts till
[L2284] [116:02.24] about 5 years after they got floating
[L2285] [116:05.44] point integers. And of course you have
[L2286] [116:08.72] to be able to turn a floating point into
[L2287] [116:10.64] an integer, right? And so that you get
[L2288] [116:14.72] implicit conversions whenever you can.
[L2289] [116:18.24] Also things like integers into
[L2290] [116:20.24] characters
[L2291] [116:22.56] uh problematic. But since you are
[L2292] [116:24.80] writing fundamental software, you didn't
[L2293] [116:27.20] want to write something
[L2294] [116:29.60] complicated and you didn't want to have
[L2295] [116:32.48] runtime checking. You couldn't afford
[L2296] [116:34.48] that.
[L2297] [116:36.24] And uh well so it was established uh
[L2298] [116:40.80] long before I came and my my attempts to
[L2299] [116:45.12] to deal with that failed.
[L2300] [116:47.28] >> It sounds like it wasn't for no reason.
[L2301] [116:49.76] It um you know saves resources maybe are
[L2302] [116:53.20] very limited.
[L2303] [116:54.00] >> They didn't have the resources to to
[L2304] [116:56.08] deal with it. They built lint the static
[L2305] [117:00.08] cheer to deal with some of it and uh
[L2306] [117:04.40] small machines. Another thing was that
[L2307] [117:07.68] that group of programmers was
[L2308] [117:09.76] significantly smarter and significantly
[L2309] [117:12.00] more experienced than the average
[L2310] [117:13.76] developer today. We have the law of
[L2311] [117:17.76] large numbers.
[L2312] [117:19.68] uh I think the last num the latest
[L2313] [117:22.24] estimate I've seen on the number of
[L2314] [117:24.08] software developers in the world is 47
[L2315] [117:26.96] million
[L2316] [117:28.64] and at that time with Unix the number of
[L2317] [117:34.24] uh programmers
[L2318] [117:36.72] probably was a few dozen and the ones
[L2319] [117:41.36] that didn't have a PhD in uh from a good
[L2320] [117:45.52] university were geniuses.
[L2321] [117:47.92] it's easier to get a PhD and being a
[L2322] [117:50.08] genius. And so they were for a different
[L2323] [117:54.32] set of problems with a different set of
[L2324] [117:56.48] machines and a different set of people.
[L2325] [117:59.04] Boy, it was a pain and still is.
[L2326] [118:02.32] >> Awesome. Well, thank you so much for
[L2327] [118:03.60] your time, professor. I really
[L2328] [118:05.04] appreciate it.
[L2329] [118:05.84] >> Okay. Thank you.
[L2330] [118:07.04] >> Hey, thank you for watching this
[L2331] [118:08.16] podcast. If you liked it and you want to
[L2332] [118:09.84] see the show grow, please support with a
[L2333] [118:12.16] comment or a like. Also, if you have any
[L2334] [118:15.04] recommendations for people you want me
[L2335] [118:16.72] to bring on, please drop a comment.
[L2336] [118:19.36] Guests like Barbara Liskoff, Mike
[L2337] [118:21.52] Stonereaker, Mark Brooker, these were
[L2338] [118:24.00] all people that I brought on because
[L2339] [118:25.92] someone left a comment. On another note,
[L2340] [118:28.24] aside from the podcast, I'm working on
[L2341] [118:30.08] building the ergonomic keyboard that I
[L2342] [118:32.00] wish existed. Here's a glance at the
[L2343] [118:34.16] prototype. It's a split keyboard, so
[L2344] [118:36.40] there's two sides. Um, this is in the
[L2345] [118:38.56] case, but yeah, we launched on
[L2346] [118:40.08] Kickstarter and we hit our goal within 8
[L2347] [118:42.32] hours of launching. I really appreciate
[L2348] [118:44.00] it if you were one of the people who
[L2349] [118:45.44] grabbed one of the early units. Um,
[L2350] [118:47.68] we're now working on the long journey of
[L2351] [118:49.60] building the tooling now and so if you
[L2352] [118:51.36] still want to pick one up, I've left the
[L2353] [118:53.44] late pledges open on Kickstarter, so you
[L2354] [118:56.08] can grab one there. I'll put a link in
[L2355] [118:57.68] the description. Thank you again for
[L2356] [119:00.00] watching the podcast and I'll see you in
[L2357] [119:02.24] the next
