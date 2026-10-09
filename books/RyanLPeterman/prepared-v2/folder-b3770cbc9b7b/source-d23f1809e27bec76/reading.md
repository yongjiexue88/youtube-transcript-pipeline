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
[L412] [14:33.96] >> Yes, Alan Kay was developing Smalltalk
[L413] [14:37.28] at the same time that I was working on
[L414] [14:39.20] Clu, and then at Carnegie Mellon uh Bill
[L415] [14:43.00] Wulf and Mary Shaw were working on
[L416] [14:44.48] Alphard, which was another data
[L417] [14:46.04] abstraction language.
[L418] [14:48.80] And you're right, there was no there was
[L419] [14:50.36] no internet, although there was the
[L420] [14:51.68] ARPANET.
[L421] [14:53.20] You know, so we did but it was like
[L422] [14:55.76] there were two independent streams of
[L423] [14:57.64] research going on and we weren't talking
[L424] [14:59.56] to each other.
[L425] [15:01.00] And so, I wasn't paying much attention
[L426] [15:03.24] to Smalltalk and
[L427] [15:05.40] on the West Coast, I don't think they
[L428] [15:06.76] were paying much attention to data
[L429] [15:08.16] abstraction.
[L430] [15:10.00] And this led to the Liskov substitution
[L431] [15:13.20] principle
[L432] [15:14.76] which I mean, the story is a sort of a
[L433] [15:17.16] cute one because
[L434] [15:19.08] in 1986, I think it was, I was asked to
[L435] [15:22.80] give a keynote at OOPSLA.
[L436] [15:25.00] OOPSLA is the object-oriented
[L437] [15:26.68] programming conference, and this was the
[L438] [15:29.80] second year it was happening.
[L439] [15:32.24] And so, I decided I think I'll read all
[L440] [15:35.04] those papers about Smalltalk, and there
[L441] [15:37.08] were other languages being developed
[L442] [15:38.76] that were based on Smalltalk, and see
[L443] [15:40.36] what's going on with them. And I
[L444] [15:42.40] discovered
[L445] [15:44.08] Um so, Smalltalk has this idea of
[L446] [15:46.36] inheritance in it, where you can have a
[L447] [15:48.32] class and a subclass which borrows from
[L448] [15:51.04] the way the class is implemented and
[L449] [15:52.68] changes it a bit.
[L450] [15:54.68] And Clu doesn't have that. Clu just has
[L451] [15:57.20] what we call clusters, and they're all
[L452] [15:58.84] independent.
[L453] [16:00.64] So, I saw that they were talking about
[L454] [16:03.92] this notion of classes and subclasses.
[L455] [16:07.08] And
[L456] [16:08.36] and then I saw that they were also
[L457] [16:09.88] talking about something they called type
[L458] [16:11.56] hierarchy.
[L459] [16:13.28] Where they wanted the type implemented
[L460] [16:15.92] by a class
[L461] [16:17.80] to be related in some way that they
[L462] [16:20.16] didn't understand to the type that was
[L463] [16:22.00] implemented by a subclass.
[L464] [16:24.24] I really thought about modules in terms
[L465] [16:26.20] of their specifications.
[L466] [16:28.92] This partly had to do with a class I
[L467] [16:31.20] developed at MIT
[L468] [16:33.16] that I developed jointly with my
[L469] [16:34.44] colleague John Guttag.
[L470] [16:36.48] And in that class, we taught the
[L471] [16:38.16] students how to do design, about
[L472] [16:39.92] modularity, data types, and so forth,
[L473] [16:42.00] but also how to write specifications,
[L474] [16:44.56] how to reason about correctness.
[L475] [16:46.88] And so, it had a big focus on think
[L476] [16:50.40] about the meaning of things first, and
[L477] [16:53.20] the implementation is something that's
[L478] [16:54.64] kind of hidden inside, and you don't
[L479] [16:55.84] worry about it very much. And so,
[L480] [16:59.28] that was a different way of thinking
[L481] [17:00.60] about things than what was going on in
[L482] [17:02.36] the
[L483] [17:03.92] on the West Coast, where they were
[L484] [17:05.24] really thinking in terms of
[L485] [17:07.44] classes and subclasses. And I even saw
[L486] [17:09.72] papers where they would describe the
[L487] [17:12.28] behavior of a class by explaining how
[L488] [17:14.32] its implementation was different from
[L489] [17:16.12] the implementation of the superclass.
[L490] [17:18.32] So, they were kind of focused on
[L491] [17:19.84] implementations in a way that we
[L492] [17:21.40] weren't. And so,
[L493] [17:24.76] when I read these papers about type
[L494] [17:27.00] hierarchy and I saw they just couldn't
[L495] [17:29.28] figure out what it was supposed to mean,
[L496] [17:32.12] I was thinking about it from the terms
[L497] [17:33.92] of meaning. And so, I was able to say it
[L498] [17:36.84] has to do with the behavior.
[L499] [17:39.16] And this subclass better behave like the
[L500] [17:41.56] superclass if you use it in an
[L501] [17:43.68] environment where the superclass is
[L502] [17:45.56] expected.
[L503] [17:47.56] And that became what ended up being
[L504] [17:49.88] called the Liskov substitution
[L505] [17:51.40] principle.
[L506] [17:52.60] And ultimately, Jeannette Wing and I
[L507] [17:54.28] wrote a paper on behavioral subtyping,
[L508] [17:56.52] which is the formal definition.
[L509] [17:58.84] >> And then, how did it get that name? Cuz
[L510] [18:00.64] you didn't go off on stage and say, "Hey
[L511] [18:02.56] everyone, here's the Liskov substitution
[L512] [18:03.96] principle."
[L513] [18:06.32] >> one day in the
[L514] [18:07.80] in the '90s, after the internet had
[L515] [18:10.00] arrived, I got an email saying, "Can you
[L516] [18:12.80] say if this is the correct
[L517] [18:14.20] interpretation of the Liskov
[L518] [18:15.52] substitution principle?" That's when I
[L519] [18:17.76] discovered
[L520] [18:19.20] that
[L521] [18:19.76] >> [laughter]
[L522] [18:20.44] >> there was such a name.
[L523] [18:22.40] And And I
[L524] [18:24.64] I don't think I had really been aware of
[L525] [18:26.32] how important it was until that point,
[L526] [18:28.48] because I wasn't thinking about this
[L527] [18:29.92] stuff. I was working on other stuff.
[L528] [18:32.20] >> In the academic community, it seems very
[L529] [18:35.04] reasonable to have multiple people have
[L530] [18:37.76] similar ideas. But it seems like some
[L531] [18:40.56] ideas stick
[L532] [18:43.04] more than others. For instance, like the
[L533] [18:46.04] Viewstamped Replication versus Paxos.
[L534] [18:48.92] They're the same thing. I'm wondering,
[L535] [18:51.84] like, in that case for instance, why
[L536] [18:53.68] would Paxos be more known than
[L537] [18:56.76] Viewstamped Replication?
[L538] [18:57.84] >> Yeah. So, what Leslie says is,
[L539] [19:00.80] "I went around giving all the talks, and
[L540] [19:03.20] she implemented it."
[L541] [19:05.61] >> [laughter]
[L542] [19:07.88] >> Really?
[L543] [19:09.76] >> Something up to that.
[L544] [19:11.56] >> Then he
[L545] [19:13.20] got notoriety for speaking about it.
[L546] [19:16.36] >> Yeah, he he he did give lots of talks
[L547] [19:18.44] about it and wrote several papers and so
[L548] [19:20.60] forth and I didn't realize it was the
[L549] [19:23.36] same system. But finally it became clear
[L550] [19:26.24] that they were the same system.
[L551] [19:28.28] >> I also wonder how much the name matters
[L552] [19:31.20] because Paxos is kind of catchy, you
[L553] [19:33.44] know.
[L554] [19:33.52] >> It is a cute name.
[L555] [19:34.48] >> It's a cute name, yeah.
[L556] [19:35.40] >> Yeah, right.
[L557] [19:36.28] >> So, I I could see maybe it has better
[L558] [19:38.60] marketing around the idea, I guess.
[L559] [19:41.48] >> I also think that
[L560] [19:43.64] this approach to solving this problem,
[L561] [19:45.96] which both Leslie and I picked up
[L562] [19:47.44] independently, in my case came from the
[L563] [19:49.84] work I'd been doing with transactions.
[L564] [19:52.44] Because in transactions there's a leader
[L565] [19:55.60] that
[L566] [19:56.64] you know, says now we're going to commit
[L567] [19:58.40] and ask everybody can we commit and if
[L568] [20:00.44] they all say okay, you know, it's
[L569] [20:02.76] but unlike in transactions
[L570] [20:06.00] of in transactions if the leader fails,
[L571] [20:08.28] there's what's called, you know, the
[L572] [20:10.16] this can be a real problem. Here we had
[L573] [20:12.40] to have a way of moving to a new leader
[L574] [20:15.16] if the old leader failed and that's the
[L575] [20:17.28] big step forward that happened in both
[L576] [20:19.88] Viewstamped Replication and and Paxos.
[L577] [20:22.92] Now, there was also Byzantine fault
[L578] [20:25.52] tolerance, which came along later that
[L579] [20:28.72] was developed. So,
[L580] [20:30.28] Viewstamped Replication I developed with
[L581] [20:32.08] my student Brian Oki. It was his PhD
[L582] [20:34.84] thesis.
[L583] [20:36.24] And then Paxos I developed with my
[L584] [20:38.24] student Miguel Castro. It was his PhD
[L585] [20:41.20] student thesis.
[L586] [20:43.20] And
[L587] [20:44.40] Miguel got interested in this problem
[L588] [20:46.40] because
[L589] [20:47.80] uh there was a DARPA request for
[L590] [20:50.04] proposals
[L591] [20:51.68] and there was one about this problem on
[L592] [20:53.96] the internet. By then there were
[L593] [20:55.44] Byzantine attacks and you know,
[L594] [20:57.08] malicious attacks and
[L595] [20:59.40] nodes that would
[L596] [21:01.00] purport to be working correctly, but
[L597] [21:02.80] actually they had been compromised and
[L598] [21:04.76] so forth and so
[L599] [21:06.88] Viewstamped application in Paxos only
[L600] [21:09.04] handled crashes and um
[L601] [21:13.00] if there were messages that were had
[L602] [21:15.20] been played with, you could tell when
[L603] [21:16.88] they arrived that they were bad. And
[L604] [21:18.24] that was about the extent of what we
[L605] [21:19.76] dealt with.
[L606] [21:21.12] But these malicious attacks with nodes
[L607] [21:23.24] that purported to be working when they
[L608] [21:25.52] weren't, that was a big step forward.
[L609] [21:28.68] And Miguel saw this request for
[L610] [21:30.68] proposals and he said to me, "Why don't
[L611] [21:33.00] we see whether we can come up with a
[L612] [21:34.52] protocol that works in the presence of
[L613] [21:36.92] Byzantine attacks?" And
[L614] [21:39.64] and I think by the way, Leslie is the
[L615] [21:41.24] one that invented the word Byzantine to
[L616] [21:43.36] >> I think he did.
[L617] [21:43.96] >> Yeah, right.
[L618] [21:44.92] >> I saw in the in the software crisis
[L619] [21:46.68] stuff. There's the paper with Dijkstra
[L620] [21:48.68] that you had mentioned was one of the
[L621] [21:51.88] papers you you wrote that said, "We need
[L622] [21:54.60] modularity." And that paper was the
[L623] [21:57.12] go-to statements considered harmful.
[L624] [21:59.32] >> Right.
[L625] [22:00.16] >> And I'm curious cuz Dijkstra, I mean,
[L626] [22:02.88] when I was studying computer science,
[L627] [22:04.24] you we all know his name. Did you ever
[L628] [22:07.16] meet him or work with him?
[L629] [22:08.52] >> Oh, yeah, many ti- I did never worked
[L630] [22:10.04] with him, but I did meet him multiple
[L631] [22:12.20] times. And uh you know, he had very
[L632] [22:15.08] interesting ideas. And that
[L633] [22:18.24] paper, uh go-to statement considered
[L634] [22:20.84] harmful, it's not actually a paper. It
[L635] [22:23.56] was a letter to the editor of the
[L636] [22:25.12] Communications of the ACM.
[L637] [22:27.72] But it was very impactful. And
[L638] [22:31.04] what was really important about that
[L639] [22:32.88] paper was that Dijkstra was talking
[L640] [22:35.52] about
[L641] [22:37.20] how difficult it is to reason about the
[L642] [22:39.96] correctness of code.
[L643] [22:42.04] And this was at a time when
[L644] [22:44.92] in the sciences,
[L645] [22:47.20] computer science was kind of dismissed
[L646] [22:49.20] as nothing much.
[L647] [22:51.00] And anybody can write code.
[L648] [22:53.76] And you know, Dijkstra was trying to
[L649] [22:55.68] make a point, which I think was actually
[L650] [22:58.08] important, that it it's not as trivial
[L651] [23:00.76] as you think it is. It's not trivial at
[L652] [23:03.12] all.
[L653] [23:04.32] Um and he was also pointing out that
[L654] [23:06.20] go-tos can be misused.
[L655] [23:08.52] >> And it was controversial at the time.
[L656] [23:11.28] >> It was, yeah.
[L657] [23:12.12] >> But today I I I don't I mean I've
[L658] [23:15.20] written code for yeah, over a decade.
[L659] [23:17.68] >> People don't use go-tos.
[L660] [23:18.52] >> have I have I haven't even seen a go-to
[L661] [23:20.20] in the code.
[L662] [23:21.56] So, what why was it controversial at the
[L663] [23:23.72] time?
[L664] [23:24.76] >> The programming languages were different
[L665] [23:26.36] then.
[L666] [23:27.52] Um first of all, there were people
[L667] [23:29.12] writing programs in assembler.
[L668] [23:31.88] In assembler, you have to use go-tos.
[L669] [23:34.40] Programming languages didn't have
[L670] [23:36.76] some of the constructs in them that we
[L671] [23:38.36] think of today.
[L672] [23:40.20] And uh so some people were using go-tos
[L673] [23:43.40] cuz they had to.
[L674] [23:45.00] And also
[L675] [23:47.24] um compilers didn't do all the kinds of
[L676] [23:49.72] optimizations that they do today. So,
[L677] [23:51.96] there was a concern if you didn't have
[L678] [23:53.60] go-tos, maybe your program wouldn't be
[L679] [23:55.28] efficient enough.
[L680] [23:57.12] And then
[L681] [23:58.72] uh there were people who used go-tos and
[L682] [24:00.64] wrote really good code, and they weren't
[L683] [24:02.40] offended that Dijkstra was saying your
[L684] [24:04.92] code is bad.
[L685] [24:06.64] So, there was a whole but and and
[L686] [24:08.32] Dijkstra was not the most um diplomatic
[L687] [24:11.12] person. So,
[L688] [24:12.81] >> [laughter]
[L689] [24:13.84] >> you know, so he he didn't write it in
[L690] [24:15.72] the you know, nice
[L691] [24:17.32] not you can imagine writing that paper
[L692] [24:18.96] more nicely where you said um
[L693] [24:22.16] So, it that but there were many reasons
[L694] [24:24.72] why it was controversial. You know,
[L695] [24:26.08] people were offended, but then there
[L696] [24:27.96] were also concerns about
[L697] [24:31.16] like programming languages don't have
[L698] [24:32.60] these features I need, what am I
[L699] [24:33.96] supposed to do?
[L700] [24:35.56] And then there were concerns about what
[L701] [24:37.80] the compiler was doing. And so, the
[L702] [24:39.76] world is very different now. But
[L703] [24:41.56] clearly, Dijkstra won the day.
[L704] [24:43.56] >> Yeah, he did.
[L705] [24:44.12] >> Because
[L706] [24:45.20] no go-tos.
[L707] [24:46.87] >> [laughter]
[L708] [24:49.00] >> And is Dijkstra in person
[L709] [24:52.00] also like his writing?
[L710] [24:55.40] >> Uh he was not always as tactful as he
[L711] [24:57.56] might be.
[L712] [24:58.66] >> [laughter]
[L713] [25:00.00] >> Yeah, but you know, he was a a very uh,
[L714] [25:02.56] distinguished researcher.
[L715] [25:04.28] >> Computer science has had such a huge
[L716] [25:06.92] impact on the industry.
[L717] [25:09.24] Why did you choose to stay in academia
[L718] [25:11.56] instead of going into industry?
[L719] [25:14.00] >> So,
[L720] [25:15.60] I like doing research.
[L721] [25:18.52] And I enjoy working with students.
[L722] [25:21.40] And
[L723] [25:23.16] I teaching was never my favorite thing,
[L724] [25:26.04] but I always felt teaching and research
[L725] [25:28.16] were very closely connected.
[L726] [25:30.60] Um, but also it was a different time.
[L727] [25:33.40] So,
[L728] [25:35.60] this business about how professors are
[L729] [25:38.36] all forming companies and so forth,
[L730] [25:40.80] which goes on today, that wasn't
[L731] [25:42.24] happening 20 years ago.
[L732] [25:44.92] Or maybe it was happening 20 years ago,
[L733] [25:47.52] but 30 years ago it wasn't. So, when I
[L734] [25:49.52] was young, it wasn't the thing that you
[L735] [25:51.68] did. It was sort of a
[L736] [25:53.92] either or sort of thing. So, I wasn't
[L737] [25:56.52] even thinking about doing stuff like
[L738] [25:58.24] that.
[L739] [25:59.32] I did work in a startup briefly at the
[L740] [26:01.60] end of the '90s. I didn't like it.
[L741] [26:05.52] I much prefer doing research and as a
[L742] [26:08.60] professor you have this it's it's a gift
[L743] [26:11.56] and a curse.
[L744] [26:13.04] The gift is you can do whatever you
[L745] [26:15.04] want. The curse is you have to figure
[L746] [26:17.12] out what it is that you're doing.
[L747] [26:19.36] But I like that freedom. And the fact
[L748] [26:22.68] that I just could go off in any I mean,
[L749] [26:25.36] my career is full of these interesting
[L750] [26:27.72] zigzags where I would switch to
[L751] [26:29.52] something else. I had the freedom to do
[L752] [26:31.28] that.
[L753] [26:32.28] >> What stops you from going off in a very
[L754] [26:34.72] useless direction?
[L755] [26:36.32] >> Uh, you won't get tenure.
[L756] [26:38.87] >> [laughter]
[L757] [26:40.32] >> Who's the judge?
[L758] [26:41.84] >> The community.
[L759] [26:43.92] Yeah, it's not you know, what what the
[L760] [26:46.52] way that you're viewed at your
[L761] [26:47.96] university
[L762] [26:49.56] has mostly to do with um,
[L763] [26:52.76] one a very important facet of it is how
[L764] [26:55.44] are you viewed in your research
[L765] [26:56.76] community.
[L766] [26:58.92] So,
[L767] [27:00.00] because that's one of the important
[L768] [27:02.40] things they want
[L769] [27:04.40] from their faculty if you're in a
[L770] [27:06.04] research university.
[L771] [27:07.84] >> You mentioned earlier that
[L772] [27:09.68] research and teaching were heavily
[L773] [27:12.20] related in your opinion.
[L774] [27:13.96] Why is that?
[L775] [27:15.04] >> Because when you teach, you have to
[L776] [27:18.04] teach from first principles.
[L777] [27:20.72] And if you're doing good research, you
[L778] [27:22.60] need to understand deeply
[L779] [27:25.12] what's working, what's not working, what
[L780] [27:26.96] assumptions you're making. It's It's
[L781] [27:29.20] really the same thought process.
[L782] [27:31.88] >> It's It sounds like in research
[L783] [27:34.00] I mean, and this is true in every walk
[L784] [27:36.84] of life. There's the I guess the
[L785] [27:38.64] direction that you take
[L786] [27:40.60] and then the work that you do towards
[L787] [27:42.16] that direction. And it sounds like for
[L788] [27:44.20] research the
[L789] [27:45.80] the direction is
[L790] [27:48.36] maybe the most important thing cuz you
[L791] [27:51.08] could have a phenomenal researcher
[L792] [27:54.92] doing an idea that
[L793] [27:56.64] has no you know, even if you did it at
[L794] [27:58.92] 100% it's not going to lead to anything.
[L795] [28:01.52] >> So, you you know, I you tell students
[L796] [28:04.04] graduate students don't do incremental
[L797] [28:05.92] work.
[L798] [28:07.32] Don't you know, you've got you you can't
[L799] [28:09.08] just keep working on the same thing over
[L800] [28:10.76] and over just making little teeny
[L801] [28:12.48] improvements. You need to find You're
[L802] [28:14.44] right, you have to find a good problem,
[L803] [28:16.36] but you also have to find a problem
[L804] [28:18.64] that's amenable to a solution and one
[L805] [28:21.92] that matches your skill set.
[L806] [28:24.80] And
[L807] [28:26.00] you have to recognize when you're going
[L808] [28:28.80] in a good direction versus not going in
[L809] [28:30.68] a good direction.
[L810] [28:32.40] >> Looking back on your career, you say
[L811] [28:34.68] that it was luck and that it seems like
[L812] [28:39.08] things just
[L813] [28:40.80] fit together.
[L814] [28:42.08] >> I feel there was luck involved.
[L815] [28:45.28] There was a lot of hard work involved.
[L816] [28:48.68] There was
[L817] [28:50.60] um not allowing
[L818] [28:54.28] uh something negative to
[L819] [28:57.04] you know, cause you great difficulty.
[L820] [29:00.60] So, for example, when I
[L821] [29:03.88] finished my PhD, I would have liked a
[L822] [29:05.80] faculty position.
[L823] [29:08.04] But, I didn't have any good offers.
[L824] [29:10.88] So, I went back to Mitre, the company I
[L825] [29:13.28] had worked for initially as a
[L826] [29:15.72] researcher.
[L827] [29:17.52] Um in other words, I just kept on
[L828] [29:19.48] marching along and it turned out to be a
[L829] [29:22.88] very good choice because I was switching
[L830] [29:25.48] from AI to systems and this gave me I
[L831] [29:28.40] worked there for 4 years. Gave me 4
[L832] [29:31.16] years to make that transition without
[L833] [29:34.12] having to uh worry about students and
[L834] [29:37.24] teaching and all the other stuff, you
[L835] [29:39.00] know, so it worked out well.
[L836] [29:41.04] But, it also meant that I didn't, you
[L837] [29:43.24] know, feel really sorry for myself that
[L838] [29:45.64] I didn't get a job. It meant I just kept
[L839] [29:47.68] on going.
[L840] [29:49.08] And then, Title IX was about to be
[L841] [29:51.56] passed and finally
[L842] [29:53.36] academia was opening up to women and I
[L843] [29:56.12] was ready.
[L844] [29:58.12] But, I think, you know, when I talk to
[L845] [30:00.20] other people about their careers, they
[L846] [30:01.84] talk about doors opening and doors
[L847] [30:04.16] closing. So,
[L848] [30:06.00] um
[L849] [30:07.00] I didn't get the academic job I wanted,
[L850] [30:09.16] but I had this other opportunity. I
[L851] [30:12.56] majored in math and fortunately, I was
[L852] [30:16.12] offered a programming job. I mean,
[L853] [30:18.80] doors opened and then you have to
[L854] [30:20.44] decide, am I going to step through? And
[L855] [30:23.16] this is a pattern that people see in
[L856] [30:25.28] their careers. It's not just me, many
[L857] [30:27.64] people have
[L858] [30:29.08] have those kinds of choices that you
[L859] [30:31.64] make along the way, opportunities and
[L860] [30:34.44] things that aren't so great, you know,
[L861] [30:36.08] and you're sort of working your way
[L862] [30:37.44] through.
[L863] [30:39.04] >> I've interviewed a few people who have
[L864] [30:41.16] won Turing Awards and I've done research
[L865] [30:44.04] and
[L866] [30:45.12] watched a lot of these speeches that
[L867] [30:47.08] people give after they receive the award
[L868] [30:49.80] and I noticed something
[L869] [30:51.76] different in in your speech or some of
[L870] [30:54.76] the stuff that I read about uh your work
[L871] [30:57.36] which is that in yours it seems like
[L872] [30:59.96] when you got the Turing Award
[L873] [31:02.08] there were people saying
[L874] [31:05.12] why did she get the Turing Award? It was
[L875] [31:07.56] kind of negative commentary on that.
[L876] [31:10.32] And I didn't see that in the other
[L877] [31:12.04] cases. Why do you think that they said
[L878] [31:14.92] that about your work?
[L879] [31:16.68] >> So, I'm I'm not so sure this doesn't
[L880] [31:18.84] happen to other people by the way. It
[L881] [31:20.44] was just that my husband was out on the
[L882] [31:22.16] internet By the way, there was an
[L883] [31:23.36] internet by then.
[L884] [31:24.48] >> Okay.
[L885] [31:24.92] >> Okay. [laughter]
[L886] [31:25.92] As you know, the internet is not
[L887] [31:27.40] necessarily nice.
[L888] [31:30.04] >> I know that.
[L889] [31:30.68] >> Right.
[L890] [31:31.92] And um
[L891] [31:33.48] so
[L892] [31:34.92] I I can imagine that other people might
[L893] [31:36.84] have had the similar a similar
[L894] [31:38.80] experience had they bothered to look.
[L895] [31:41.48] Um
[L896] [31:42.72] but I also think that
[L897] [31:46.32] the world had changed so much and
[L898] [31:49.76] the work that I had done was so basic to
[L899] [31:53.28] what was going on
[L900] [31:55.40] that people really didn't understand
[L901] [31:58.32] that there was a before.
[L902] [32:00.16] I mean, my graduate students really
[L903] [32:02.04] didn't understand that there was a
[L904] [32:03.60] before because I discovered that at the
[L905] [32:06.56] time I got the award. It really hadn't
[L906] [32:08.60] struck them that data abstraction didn't
[L907] [32:11.00] always exist.
[L908] [32:13.12] So, I think that
[L909] [32:15.32] I mean, I viewed it as
[L910] [32:18.20] a in a way a huge compliment
[L911] [32:21.16] not really just to me, but to the group
[L912] [32:23.60] of researchers who you know, all
[L913] [32:25.76] together got us to the point where we
[L914] [32:28.40] had uh these modular programming
[L915] [32:31.08] languages and we understood about
[L916] [32:33.64] abstract data types and we understood
[L917] [32:35.48] about how to reason about correctness.
[L918] [32:37.04] All that stuff was so fundamental
[L919] [32:40.24] that people thought there was no time
[L920] [32:42.52] when it hadn't already existed.
[L921] [32:44.40] >> So, they took it for granted.
[L922] [32:45.64] >> They took it for granted. I mean, the
[L923] [32:47.28] Byzantine fault tolerance, you look at
[L924] [32:49.08] that, there's a protocol.
[L925] [32:51.28] And
[L926] [32:53.24] you can understand that there was a
[L927] [32:54.68] protocol, somebody invented that
[L928] [32:56.12] protocol.
[L929] [32:57.48] Um you know, so you get the credit for
[L930] [33:00.00] that. This was much more fundamental.
[L931] [33:02.28] This was the whole mindset you had about
[L932] [33:04.68] how to develop programs. And that's what
[L933] [33:07.20] people were talking about.
[L934] [33:09.28] And things had changed so much
[L935] [33:11.84] that all these inventions of mine and
[L936] [33:14.32] others were just there in the woodwork
[L937] [33:17.60] and people didn't realize that there was
[L938] [33:19.76] a time before.
[L939] [33:21.28] >> That's validating then. That it's it's
[L940] [33:23.92] so impactful and
[L941] [33:26.16] everyone uses all the time that they
[L942] [33:27.92] don't even know what it was like before
[L943] [33:29.68] what you did.
[L944] [33:30.32] >> So, I thought, you know, it's a huge The
[L945] [33:32.08] person who said it didn't mean it
[L946] [33:33.48] nicely, but I thought
[L947] [33:35.56] really it's a huge a huge compliment.
[L948] [33:39.16] And and a statement about where we are
[L949] [33:41.20] now as opposed to where we were then.
[L950] [33:43.12] So,
[L951] [33:45.08] >> Okay, well, that's all the questions I
[L952] [33:46.52] have for you. Thank you so much for for
[L953] [33:48.44] your time. Really appreciate it.
[L954] [33:49.68] >> You're welcome.
[L955] [33:51.12] >> Thank you for listening to the podcast.
[L956] [33:52.76] It's a passion project of mine that I've
[L957] [33:54.92] really enjoyed building. Another passion
[L958] [33:57.04] project that I've been working on kind
[L959] [33:58.40] of in secret is building an ergonomic
[L960] [34:00.88] keyboard that I wish existed and I
[L961] [34:03.16] finally have a prototype, so I'd love to
[L962] [34:04.92] show you what we've built. It's
[L963] [34:07.28] ultra-low profile and ergonomic and I
[L964] [34:10.16] couldn't find anything like it on the
[L965] [34:11.44] market, so that's why we built it. I'll
[L966] [34:13.40] put a link to the keyboard in the
[L967] [34:14.60] description. You can take a look and
[L968] [34:16.20] learn more about the project there. We
[L969] [34:18.04] could definitely use your support. Also,
[L970] [34:20.04] if you have any feedback for me about
[L971] [34:21.68] the show, I'd love to hear it. Comments
[L972] [34:24.12] on YouTube have led to guests coming on
[L973] [34:26.12] like Ilya Grigorik and David Fowler. I
[L974] [34:29.16] wasn't aware of them until someone
[L975] [34:31.00] dropped a comment. Also, feedback in the
[L976] [34:32.96] comments helped me learn to reduce the
[L977] [34:34.60] number of cliffhangers in the intros.
[L978] [34:37.20] So, your comments definitely make a
[L979] [34:38.48] difference. Please keep letting me know
[L980] [34:40.16] what you'd like to see more of in the
[L981] [34:41.52] show, and I'll see you in the next
[L982] [34:42.92] episode.
