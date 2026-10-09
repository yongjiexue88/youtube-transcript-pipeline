Chunk 1; segments 1–402. 

# Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov

Source ID: source-d23f1809e27bec76
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Data_Abstraction,_Dijkstra,_Distributed_Systems_Barbara_Liskov_en.txt
Video: https://www.youtube.com/watch?v=T9CGjbPZeaM

[L10] [00:00.00] Don't do incremental work.
[L11] [00:02.48] >> This is Barbara Liskov. She's a Turing
[L12] [00:04.80] Award winner famous for her fundamental
[L13] [00:06.88] contributions to programming languages
[L14] [00:08.92] and distributed systems.
[L15] [00:10.36] >> Encapsulation is a crucial part of
[L16] [00:12.84] making modularity work. Your team is
[L17] [00:15.64] really only as strong as your weakest
[L18] [00:17.68] programmer.
[L19] [00:18.84] >> I asked her for stories from her career.
[L20] [00:21.24] That paper was the go-to statements
[L21] [00:23.48] considered harmful. Is Dijkstra in
[L22] [00:25.84] person also like his writing?
[L23] [00:28.32] >> He was not always as tactful as he might
[L24] [00:30.48] be.
[L25] [00:31.36] >> There were people saying, "Why did she
[L26] [00:34.84] get the Turing Award?" Why do you think
[L27] [00:37.08] that they said that about your work?
[L28] [00:40.64] Here's the full episode.
[L29] [00:46.88] You applied to multiple places and
[L30] [00:50.16] Princeton was one of them and they had
[L31] [00:52.20] rejected you on the grounds of you being
[L32] [00:54.20] a a woman. How did you get into
[L33] [00:56.72] programming in an environment that's so
[L34] [00:58.72] hostile?
[L35] [01:00.12] >> Okay, so this was when I got my
[L36] [01:01.96] bachelor's degree.
[L37] [01:04.04] And I applied to several graduate
[L38] [01:07.72] programs
[L39] [01:09.24] in math, which is what I majored in as
[L40] [01:11.32] an undergraduate.
[L41] [01:13.04] And
[L42] [01:14.48] I got this little card back. It was a
[L43] [01:16.72] postcard from Princeton saying, "We do
[L44] [01:19.00] not admit women."
[L45] [01:20.72] Which was surprising.
[L46] [01:23.32] Um I knew they didn't have women in
[L47] [01:24.68] their undergraduate program, but I
[L48] [01:26.28] hadn't realized it extended to the
[L49] [01:28.28] graduate program.
[L50] [01:30.20] Um
[L51] [01:31.36] but you know, it was how it was. So so
[L52] [01:34.12] what happened was I did get into
[L53] [01:36.56] Berkeley, which is where I did my
[L54] [01:38.08] undergraduate work. But I decided I
[L55] [01:41.28] really wasn't ready to do a a PhD in
[L56] [01:43.76] math and that I should get a job instead
[L57] [01:46.96] and just sort of see you know, see how
[L58] [01:49.48] things were.
[L59] [01:50.84] And uh the best job offer I got was as a
[L60] [01:54.48] programmer.
[L61] [01:56.04] So that's how I got computer science by
[L62] [01:58.40] a happy accident.
[L63] [02:00.64] >> You were consistently, at least at
[L64] [02:02.28] Berkeley, you were consistently a top
[L65] [02:04.56] student. So, it's it it is odd that you
[L66] [02:08.08] wouldn't even get an opportunity to play
[L67] [02:10.12] in some cases.
[L68] [02:11.44] >> But, that's how it was back then. It was
[L69] [02:13.32] just I hadn't realized it was more than
[L70] [02:15.72] an undergraduate thing. And Berkeley was
[L71] [02:18.44] co-ed. So, you know, there
[L72] [02:21.60] what I found was there weren't very many
[L73] [02:24.00] women in my classes. There were lots of
[L74] [02:25.96] women students,
[L75] [02:27.72] but very few of them majoring in math.
[L76] [02:30.88] And there were only maybe a couple of
[L77] [02:33.20] women in my classes.
[L78] [02:35.24] But,
[L79] [02:36.40] the uh the idea that a door was shut and
[L80] [02:38.76] women couldn't do things, that was not
[L81] [02:40.68] what went on at Berkeley.
[L82] [02:42.60] So, it was a different environment. Of
[L83] [02:45.28] course, nowadays in the top schools, the
[L84] [02:49.28] um women are about 50% in computer
[L85] [02:51.88] science.
[L86] [02:53.56] >> I want to talk about some of the the
[L87] [02:55.60] core problems that you were solving in
[L88] [02:57.12] your career. And so, I understand that
[L89] [03:00.44] there's the software crisis in the
[L90] [03:02.20] 1970s. And uh I was wondering if you
[L91] [03:04.92] could give the context behind what the
[L92] [03:07.60] problem was at that time.
[L93] [03:09.64] >> Well, it was a huge problem at the time
[L94] [03:11.60] because
[L95] [03:13.12] uh people did not know how to build big
[L96] [03:15.72] programs that worked.
[L97] [03:17.64] And so, you would often pick up the
[L98] [03:20.32] newspaper and see an article about some
[L99] [03:22.56] company
[L100] [03:23.88] that had spent
[L101] [03:25.80] uh
[L102] [03:26.72] you know,
[L103] [03:27.68] millions of
[L104] [03:29.08] dollars and hundreds of man-years
[L105] [03:32.92] developing some software system for
[L106] [03:35.32] their company. And then in the end
[L107] [03:37.68] they'd have to throw it away because
[L108] [03:39.04] they it simply didn't work.
[L109] [03:41.36] The problem was
[L110] [03:44.44] that to get a big program that works,
[L111] [03:46.36] you need modularity.
[L112] [03:48.36] And you need to break your program up
[L113] [03:49.96] into small pieces.
[L114] [03:52.40] Each piece provides an interface with a
[L115] [03:57.88] hopefully complete description of what
[L116] [04:00.32] service it provides for you.
[L117] [04:02.56] And then inside is an implementation
[L118] [04:05.32] that's hidden and nobody pays any
[L119] [04:06.76] attention to it on the outside.
[L120] [04:09.16] And if you have a system organized like
[L121] [04:12.04] that, you can actually reason about its
[L122] [04:13.80] correctness one module at a time.
[L123] [04:17.40] But in those days, people didn't know
[L124] [04:19.20] how
[L125] [04:20.44] um
[L126] [04:21.56] they couldn't figure out how to design
[L127] [04:23.00] systems that were modular.
[L128] [04:25.16] And the only kind of modularity
[L129] [04:27.76] mechanism present in programming
[L130] [04:29.40] languages was a procedure.
[L131] [04:31.92] And procedures didn't match the kinds of
[L132] [04:35.08] modules you needed. Because if you think
[L133] [04:37.68] about a file system or a database or you
[L134] [04:41.52] know, Amazon or whatever, you know, they
[L135] [04:44.72] they aren't a procedure where you put
[L136] [04:46.36] something in and get something out.
[L137] [04:48.08] They're a much more complicated thing.
[L138] [04:51.04] So, there was no notion of a module that
[L139] [04:53.92] sort of matched the kind of things that
[L140] [04:55.72] people were looking for.
[L141] [04:58.16] >> So, when you saw that problem, you know,
[L142] [05:00.28] what were the early solutions like?
[L143] [05:02.60] >> Well, so people were proposing
[L144] [05:04.12] modularity and they were talking about
[L145] [05:06.44] how important modularity was.
[L146] [05:09.36] They didn't exactly know what a module
[L147] [05:11.12] was.
[L148] [05:12.40] And so, it wasn't like they could give
[L149] [05:14.16] you a rule, this is a module. It was
[L150] [05:15.80] just a chunk of code. In fact, there
[L151] [05:18.36] were papers written that talked about
[L152] [05:20.00] how big a module should be or and stuff
[L153] [05:21.88] like that, just a chunk of code. That's
[L154] [05:24.32] not going to work because you need
[L155] [05:26.80] to design these systems. So, you need a
[L156] [05:28.52] way of thinking of a design that sort of
[L157] [05:30.84] fits into this notion of modularity.
[L158] [05:34.24] They also didn't really know what the
[L159] [05:35.88] rules should be for modularity.
[L160] [05:38.56] And um
[L161] [05:40.40] it turned out that in some of the early
[L162] [05:42.20] work I did after grad school when I was
[L163] [05:44.36] working at Mitre,
[L164] [05:45.92] um I had already invented a notion of
[L165] [05:48.16] modularity that was sort of more
[L166] [05:49.92] complete than what people had been
[L167] [05:51.40] talking about just because I had a small
[L168] [05:54.80] team of programmers. We were building a
[L169] [05:56.40] complicated system
[L170] [05:58.32] and I wanted to keep us out of trouble.
[L171] [06:02.04] And so I had that sort of sitting there
[L172] [06:04.36] when I started to work on this topic.
[L173] [06:08.04] Um,
[L174] [06:08.92] and it enabled me to see this idea of
[L175] [06:11.84] data abstraction
[L176] [06:13.72] all of a sudden. I sort of saw that this
[L177] [06:16.20] thing I had, this kind of modularity
[L178] [06:18.28] mechanism, which consisted of basically
[L179] [06:21.64] what I just described,
[L180] [06:23.64] a a a bunch of code providing you with
[L181] [06:26.56] an access through a number of what I
[L182] [06:29.00] called operations. So you could call it
[L183] [06:30.88] in various ways and then inside was all
[L184] [06:32.88] hidden and whatever data it was using
[L185] [06:35.08] was not accessible to the outside.
[L186] [06:37.80] And then at some point I saw I could see
[L187] [06:39.84] this as a data abstraction. It could be
[L188] [06:41.72] a set, it could be a sequence, it could
[L189] [06:43.84] be, you know, and so forth. And um,
[L190] [06:46.80] and that meant we had a new type of
[L191] [06:48.68] module.
[L192] [06:50.24] Now when I look back at the papers from
[L193] [06:52.04] the time, I see that idea is almost
[L194] [06:54.32] there except people hadn't managed to
[L195] [06:57.16] pick it out.
[L196] [06:58.80] And so it was probably I think this
[L197] [07:00.80] happens in science a lot. There's sort
[L198] [07:02.72] of a time when an idea is ready and I
[L199] [07:05.28] happened to see it.
[L200] [07:07.48] >> You pieced these together and you put it
[L201] [07:10.84] into the Clue programming language that
[L202] [07:13.24] you're working on.
[L203] [07:14.64] How did you see it influencing the
[L204] [07:16.72] industry?
[L205] [07:17.64] >> The first thing that happened was I
[L206] [07:19.56] wrote a paper with um,
[L207] [07:22.20] a a a
[L208] [07:23.48] a man who was a graduate student at MIT,
[L209] [07:25.40] Steve Zilles, about this idea of data
[L210] [07:27.80] abstraction and it sketched a notion of
[L211] [07:29.88] what abstract data types would be and
[L212] [07:31.64] how a programming language could support
[L213] [07:33.40] them. And this was a very um,
[L214] [07:36.44] is a very impactful paper.
[L215] [07:38.88] And so there was a a big impact on the
[L216] [07:42.32] research community.
[L217] [07:44.24] And then
[L218] [07:46.24] Clu came along and that involved a lot
[L219] [07:48.64] of additional research in the in the
[L220] [07:50.60] programming language area.
[L221] [07:52.64] The next thing that happened, so people
[L222] [07:55.12] were watching this in the research
[L223] [07:56.80] community, but of course people who are
[L224] [07:58.72] in companies that want to write
[L225] [08:00.16] programs,
[L226] [08:01.52] they need a programming language.
[L227] [08:04.20] And
[L228] [08:05.52] I decided I wasn't going to try and turn
[L229] [08:08.64] Clu into a
[L230] [08:10.52] product because that would have required
[L231] [08:13.00] working in a company. In those days you
[L232] [08:15.04] didn't just put software out on the
[L233] [08:16.52] internet and people used it. There
[L234] [08:19.04] wasn't an internet yet for one thing.
[L235] [08:21.80] And and I was much more interested in
[L236] [08:23.96] doing research than in
[L237] [08:26.68] you know, working in a company. So I put
[L238] [08:28.96] Clu on the side. It had a user base.
[L239] [08:32.04] But I it but for companies to use a
[L240] [08:34.48] programming language in those days, they
[L241] [08:36.00] wanted a company behind that language.
[L242] [08:39.08] The next thing that happened was the
[L243] [08:40.52] government uh put out a call for uh a
[L244] [08:44.24] programming language they could use.
[L245] [08:45.84] This led to the Ada programming
[L246] [08:47.44] language.
[L247] [08:48.76] That um
[L248] [08:50.04] so you know, that was already a big
[L249] [08:51.96] impact if you think about it. That there
[L250] [08:54.16] there was a language explicitly being uh
[L251] [08:56.64] designed to have data abstraction in it.
[L252] [08:59.04] And then
[L253] [09:00.24] finally in the '90s Java came along.
[L254] [09:03.48] >> I thought it'd be interesting cuz you
[L255] [09:04.96] you worked on Clu. You designed that
[L256] [09:07.32] programming language to ask you about
[L257] [09:09.00] other programming languages. You said
[L258] [09:11.28] somewhere that there's something wrong
[L259] [09:13.16] with Python and I was curious to hear
[L260] [09:14.60] your thoughts of why.
[L261] [09:16.36] >> Python
[L262] [09:18.00] has modules, but it doesn't have
[L263] [09:20.68] encapsulation. So it allows code on the
[L264] [09:24.04] outside to muck around with what's going
[L265] [09:26.08] on on the inside of a module. And that's
[L266] [09:28.40] all I was talking about. Encapsulation
[L267] [09:30.64] is a is a crucial part of making
[L268] [09:33.72] modularity work.
[L269] [09:36.04] And when you're building big programs,
[L270] [09:38.32] so you have many programmers working on
[L271] [09:40.16] them,
[L272] [09:41.08] your team is really only as strong as
[L273] [09:43.32] your weakest programmer.
[L274] [09:45.44] So, it's nice if the compiler can
[L275] [09:48.48] enforce things and make certain kinds of
[L276] [09:51.08] bad behavior not possible. I mean,
[L277] [09:53.64] Python is you know, has another intended
[L278] [09:56.40] use. It's helping naive programmers
[L279] [09:59.16] learn quickly how to write programs and
[L280] [10:00.96] stuff like that.
[L281] [10:02.60] And people in the programming language
[L282] [10:04.32] world do think about issues like this.
[L283] [10:07.04] Like, you know, how to make
[L284] [10:10.24] languages safer and so forth. But, since
[L285] [10:12.36] I stopped working in that area, I'm no
[L286] [10:15.08] longer an expert in programming
[L287] [10:16.68] languages.
[L288] [10:17.76] >> What got you into distributed computing?
[L289] [10:20.32] >> I read a paper by Bob Kahn, who was with
[L290] [10:24.00] then Cerf considered to be, you know,
[L291] [10:25.84] the founders of the internet.
[L292] [10:28.12] And Bob talked about
[L293] [10:30.80] um
[L294] [10:31.84] his dream of distributed computing,
[L295] [10:34.44] where you would have a program composed
[L296] [10:36.20] of pieces on different computers
[L297] [10:38.12] connected by a network.
[L298] [10:40.24] And nobody knew how to build those
[L299] [10:42.56] programs. And so, I just thought, great
[L300] [10:44.84] problem.
[L301] [10:46.49] >> [laughter]
[L302] [10:47.76] >> And [snorts] I was looking for a new
[L303] [10:49.00] problem, so I jumped into distributed
[L304] [10:50.92] computing.
[L305] [10:52.16] And the first project was actually a
[L306] [10:53.76] programming language to write
[L307] [10:55.12] distributed programs in.
[L308] [10:57.72] And and then I started looking at other
[L309] [11:00.44] problems in the distributed systems
[L310] [11:02.12] area.
[L311] [11:03.12] >> What was that first programming language
[L312] [11:05.20] that
[L313] [11:05.32] >> It was called Argus. It was It was very
[L314] [11:07.72] strongly influenced by Clu.
[L315] [11:10.04] It was an object-oriented language.
[L316] [11:12.80] Had a special kind of object called a
[L317] [11:14.80] guardian,
[L318] [11:16.20] which was a module sitting at a single
[L319] [11:18.56] computer.
[L320] [11:20.08] And then guardians could compute
[L321] [11:22.20] communicate through remote procedure
[L322] [11:23.72] calls.
[L323] [11:25.16] One of the things you run into in
[L324] [11:26.48] distributed computing
[L325] [11:28.84] um is if you have a computation that
[L326] [11:31.40] starts at one guardian and then makes
[L327] [11:33.92] use of other guardians at other nodes in
[L328] [11:35.72] the network, in the end, you want that
[L329] [11:38.60] computation to either complete entirely
[L330] [11:41.96] or have no effect at all.
[L331] [11:44.56] And how do you do that? Well, I borrowed
[L332] [11:47.72] the notion of transactions coming out of
[L333] [11:49.68] the database field.
[L334] [11:52.36] And that was part of how Argus worked.
[L335] [11:54.56] It ran computations as atomic
[L336] [11:56.36] transactions.
[L337] [11:57.80] >> Oh, interesting. Like distributed
[L338] [12:00.20] transactions across those nodes.
[L339] [12:03.20] >> And I think it led right into the work I
[L340] [12:05.00] did on um viewstamp replication, which
[L341] [12:07.64] was
[L342] [12:08.60] um that was the beginning of cloud
[L343] [12:10.68] storage. I was thinking in terms of a
[L344] [12:12.76] file system, but it doesn't really
[L345] [12:14.32] matter what it is. You know, how do you
[L346] [12:16.00] have data out on the internet stored at
[L347] [12:20.04] multiple sites
[L348] [12:22.08] with correct behavior
[L349] [12:24.84] and always accessible as long as enough
[L350] [12:28.80] nodes are up and running and the network
[L351] [12:30.68] is working.
[L352] [12:32.12] >> I see. And what is viewstamp in this
[L353] [12:34.24] context?
[L354] [12:35.44] >> Oh, that had to do with some details of
[L355] [12:37.52] how the system worked. And it was a way
[L356] [12:39.88] of noticing when some nodes failed and
[L357] [12:43.12] other nodes had to take over, you could
[L358] [12:45.36] figure out which ones had the most
[L359] [12:46.88] recent state in them, so you could pick
[L360] [12:48.72] up and not lose anything that had not
[L361] [12:51.40] had that had happened in the past.
[L362] [12:53.60] >> Uh what what if the clocks are out of
[L363] [12:55.60] sync? Like
[L364] [12:56.84] >> Uh it had nothing to do with clocks
[L365] [12:58.80] because it was just numbers.
[L366] [13:01.28] In other words, we were in view 25, the
[L367] [13:03.44] next view was 26. So
[L368] [13:05.44] >> Oh, okay. Just incrementing some numbers
[L369] [13:07.68] that are passed around.
[L370] [13:09.52] >> This reminds me a lot of uh Leslie
[L371] [13:11.56] Lamport's work.
[L372] [13:12.68] >> Actually, yes.
[L373] [13:14.40] >> Did you ever work with him or
[L374] [13:17.28] >> No. Leslie and I developed what is
[L375] [13:19.60] essentially the same idea independently.
[L376] [13:22.52] And he had the system he called Paxos
[L377] [13:25.52] and I had this thing called view stamp
[L378] [13:27.08] replication.
[L379] [13:28.56] >> Oh, interesting. And they're essentially
[L380] [13:31.68] the same thing.
[L381] [13:32.44] >> They are. Yeah.
[L382] [13:33.80] >> Oh, are there pros and cons of the two
[L383] [13:36.08] approaches?
[L384] [13:37.28] >> Yeah, I mean that when you do this kind
[L385] [13:39.68] of system, there's a lots of little
[L386] [13:41.16] details you can play around with. So,
[L387] [13:42.84] you could, you know, decide to do it it
[L388] [13:45.52] gets technical, but you know, there's
[L389] [13:46.96] tiny differences. But no, they're
[L390] [13:48.76] basically the same. In fact, what
[L391] [13:50.28] happened was
[L392] [13:51.88] uh the first time that
[L393] [13:54.68] I was aware of that this was actually
[L394] [13:56.52] used in a real system was when the
[L395] [13:59.08] Google file system came along.
[L396] [14:01.72] And
[L397] [14:03.08] one of my former students who was a I
[L398] [14:05.72] think he was a consultant at Google
[L399] [14:07.64] looked at what was going on in there and
[L400] [14:09.04] he said, "Oh, he says that's view stamp
[L401] [14:10.56] replication." So, the people at Google
[L402] [14:12.60] seemed to think it was Paxos, but in
[L403] [14:15.08] fact, they are the same system.
[L404] [14:17.60] >> I also noticed like um when you were
[L405] [14:20.60] uh when you came up with abstract data
[L406] [14:22.32] types
[L407] [14:24.16] maybe I mean maybe it's just cuz there
[L408] [14:25.72] wasn't the internet wasn't as, you know,
[L409] [14:28.68] wasn't there that there was also the
[L410] [14:30.72] object-oriented stuff going on on the
[L411] [14:32.96] West Coast.
