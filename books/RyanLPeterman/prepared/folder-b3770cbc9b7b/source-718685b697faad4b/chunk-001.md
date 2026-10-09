Chunk 1; segments 1–389. 

# Turing Award Winner: Disagreeing with Google, Postgres, Future Problems | Mike Stonebraker

Source ID: source-718685b697faad4b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Turing_Award_Winner_Disagreeing_with_Google,_Postgres,_Future_Problems_Mike_Stonebraker_en.txt
Video: https://www.youtube.com/watch?v=YPObBOwIrHk

[L10] [00:00.16] Computer science may well not be a
[L11] [00:02.16] growth industry going forward.
[L12] [00:04.56] >> This is Mike Stonbreaker. He's a touring
[L13] [00:06.72] award winner famous for his fundamental
[L14] [00:08.80] contributions to database systems like
[L15] [00:10.88] creating Postgress and more. What was
[L16] [00:13.20] the hardest part of that?
[L17] [00:15.20] >> Uh query optimizer. [music] It's just
[L18] [00:17.28] algorithmically difficult.
[L19] [00:19.28] >> How do you identify the people who
[L20] [00:21.12] aren't smart?
[L21] [00:22.24] >> Well, I mean it's it's very easy.
[L22] [00:24.64] >> He shared interesting technical takes
[L23] [00:26.56] from his experience
[L24] [00:27.68] >> on our benchmarks. large language models
[L25] [00:30.72] get [music] 0%.
[L26] [00:32.48] >> Why did you disagree so much with map
[L27] [00:35.04] produce?
[L28] [00:35.68] >> That wasn't the only thing Google was
[L29] [00:37.68] stupid about.
[L30] [00:39.36] >> I'm curious your thoughts on unsolved
[L31] [00:41.92] problems in databases and what you think
[L32] [00:44.72] the future might look like.
[L33] [00:47.36] Here's the full episode.
[L34] [00:52.72] The first thing I want to go over is the
[L35] [00:54.80] story of how Postgress got started. But
[L36] [00:58.32] for that I kind of want to start at the
[L37] [00:59.84] beginning. How did you get into building
[L38] [01:01.76] database systems? When I graduated I had
[L39] [01:05.92] the good fortune of being hired at
[L40] [01:07.68] Berkeley
[L41] [01:09.36] and I it was clear I had to you know
[L42] [01:12.08] continuing what I did for my PhD was not
[L43] [01:15.04] going to go anywhere then as well as
[L44] [01:18.16] today. Uh you're way ahead if you get
[L45] [01:22.16] adopted by a mentor
[L46] [01:24.80] who knows the robes. So Gene Wong, who
[L47] [01:29.04] who is still alive and still
[L48] [01:32.88] still kicking, uh took me under his wing
[L49] [01:36.24] and said, "Well, let's do something
[L50] [01:37.84] together."
[L51] [01:40.40] And this was 1971,
[L52] [01:44.00] which was the year after Ted Cod wrote
[L53] [01:46.88] his pioneering paper in in CACM. Gene
[L54] [01:50.32] Wong said, "Well, let's let's take a
[L55] [01:51.92] look at database stuff." And
[L56] [01:55.84] at the time the the competitors were a
[L57] [02:00.00] thing called the Kotil proposal which
[L58] [02:02.80] you're probably too young to have ever
[L59] [02:04.64] heard of. And so it was a low-level
[L60] [02:08.56] spaghetti network proposal
[L61] [02:11.28] uh where you where you executed queries
[L62] [02:14.88] by following pointers
[L63] [02:17.20] and then the the alternative was the IBM
[L64] [02:20.24] proposal which was a hier thing called
[L65] [02:22.40] IMS which is still available and it's
[L66] [02:26.16] hierarchical data. It's a tree. You're
[L67] [02:29.12] organized your data as trees.
[L68] [02:32.40] And even at the time, IBM realized that
[L69] [02:36.80] trees were not general enough to to
[L70] [02:40.32] solve many people's problems.
[L71] [02:44.56] So they hacked on a a way to make it a
[L72] [02:47.92] limited network structure.
[L73] [02:51.52] So it was clear that was a horrible
[L74] [02:53.52] hack. The Kodasil proposal had all kinds
[L75] [02:58.08] of bad properties. Uh besides being
[L76] [03:01.52] low-level and and really hard to debug,
[L77] [03:04.80] uh it also had the property that if
[L78] [03:07.28] anything changed in your what's now
[L79] [03:09.76] called your schema, you basically had to
[L80] [03:12.08] throw away everything and do it all
[L81] [03:13.76] again because it was absolutely rooted
[L82] [03:16.32] of the physical level.
[L83] [03:18.88] Whereas Ted Cod stuff made perfect
[L84] [03:21.28] sense. And so Jean said, "Well, let's
[L85] [03:24.08] build one of these puppies. That's
[L86] [03:25.52] clearly the the next thing to try."
[L87] [03:28.72] So we started building Ingress in 1972
[L88] [03:33.12] while I was an assistant professor at
[L89] [03:34.96] Berkeley. As you know, if you're an
[L90] [03:37.52] assistant professor,
[L91] [03:39.76] you have to you have about you get five
[L92] [03:42.00] years to prove that you're a big
[L93] [03:44.72] and they fire you or they give you
[L94] [03:46.64] tenure. So, Ingress was my ticket to
[L95] [03:50.40] getting tenure which happened in 1976.
[L96] [03:55.44] That was where it started. And then
[L97] [03:58.56] again, you know, happen stance.
[L98] [04:01.68] Uh, at the time, you know, a lot of
[L99] [04:04.48] people would build prototypes which were
[L100] [04:06.72] sort of studenty like code, which means
[L101] [04:10.32] you could get it to run, but if you gave
[L102] [04:12.56] it to anybody else, they couldn't.
[L103] [04:15.60] So we put in the first 90% to get
[L104] [04:18.96] something we could run and then for
[L105] [04:22.08] whatever reason we put in the next 90%
[L106] [04:26.08] to get it to where it really worked.
[L107] [04:29.12] So the University of California version
[L108] [04:31.60] of of Ingress was really worked.
[L109] [04:35.76] And so over the next couple years about
[L110] [04:38.96] a hundred universities started running
[L111] [04:40.96] it because Unix became the big thing.
[L112] [04:46.80] And so this was a database a free
[L113] [04:49.52] database system that ran on Unix.
[L114] [04:52.64] And so it was quite popular in in the
[L115] [04:55.76] academic world. And so we got started
[L116] [04:59.36] getting you know lots of visitors at
[L117] [05:01.52] Berkeley who would say gee this is
[L118] [05:04.16] really nifty looking stuff what's the
[L119] [05:07.20] biggest biggest day incorous application
[L120] [05:10.00] you have
[L121] [05:12.40] and we'd be forced to say not very big
[L122] [05:15.92] and so this was brought home
[L123] [05:19.84] uh in spades when Arizona [snorts]
[L124] [05:22.80] State University
[L125] [05:25.04] considered running Ingress
[L126] [05:27.36] on their student records data, all
[L127] [05:29.68] 40,000 students worth.
[L128] [05:32.64] And they could get over that they had to
[L129] [05:34.56] get an unsupported operating system from
[L130] [05:38.16] Bell Labs.
[L131] [05:40.24] They could also get over they had to uh
[L132] [05:43.44] run an unsupported op unsupported
[L133] [05:45.76] database system from these guys at
[L134] [05:48.32] Berkeley.
[L135] [05:49.92] But the project went down in flames when
[L136] [05:52.48] they realized there was no cobalt
[L137] [05:54.32] available for Unix. and they were a
[L138] [05:57.04] cobalt shop. So unsupported operating
[L139] [06:00.24] system, unsupported database system, no
[L140] [06:02.40] Cobalt doomed us to, you know,
[L141] [06:06.32] irrelevance.
[L142] [06:08.32] And it was clear the only way out of
[L143] [06:10.40] that was to start a company. And so in
[L144] [06:14.64] 1980 uh we got venture capital as it
[L145] [06:18.40] existed then
[L146] [06:20.56] and started Ingress Corporation
[L147] [06:23.52] to move uh Ingress to uh to Dex uh VMS
[L148] [06:32.00] uh you know a real a real operating
[L149] [06:35.60] system and we had a real company that
[L150] [06:38.72] would support Ingress and that was the
[L151] [06:40.80] start of the commercial journey.
[L152] [06:43.36] I saw that Ingress was competing with uh
[L153] [06:47.12] Larry Ellison's offering at Oracle.
[L154] [06:50.16] >> Yes,
[L155] [06:51.04] >> I saw that uh Ingress was was certainly
[L156] [06:54.48] better than what they were offering, but
[L157] [06:58.00] they were still competing somehow. How
[L158] [07:00.08] how did they compete?
[L159] [07:02.16] Uh Larry Ellison is a fabulous salesman
[L160] [07:05.92] and he at the time he he would he made
[L161] [07:10.24] present tense and future tense
[L162] [07:12.64] indistinguishable
[L163] [07:14.16] and so he basically lied to customers.
[L164] [07:17.44] He would ship stuff that didn't work
[L165] [07:21.36] and h have his initial customers help
[L166] [07:23.84] him debug it. So I think he he he
[L167] [07:27.36] engaged in what I consider very shady
[L168] [07:30.88] business practices.
[L169] [07:33.20] But lying to customers I think is is you
[L170] [07:36.48] know unconscionable.
[L171] [07:39.04] So for instance
[L172] [07:42.80] uh there's a thing called referential
[L173] [07:44.72] integrity
[L174] [07:46.72] which is if you I if you fire an
[L175] [07:50.32] employee
[L176] [07:52.08] and he's the last person in a given
[L177] [07:54.80] department do you want to delete the
[L178] [07:57.28] department or do you want to have it be
[L179] [07:59.76] a department ghost department? It's it's
[L180] [08:02.40] all that kind of stuff. And so Ingress
[L181] [08:05.52] Corporation implemented referential
[L182] [08:08.08] integrity. Uh Oracle Corporation wrote
[L183] [08:11.44] two manual pages that said here's the
[L184] [08:14.24] definition of referential integrity
[L185] [08:16.72] which everybody agreed to. And then he
[L186] [08:19.84] then down at the bottom it said not yet
[L187] [08:22.16] implemented.
[L188] [08:24.36] [laughter]
[L189] [08:25.60] >> Interesting. Yeah. I had interviewed
[L190] [08:27.44] someone who worked at Sun Micros
[L191] [08:29.60] Systemystems and they had a similar
[L192] [08:32.24] opinion that they
[L193] [08:34.48] Larry Ellison was a little bit shady. So
[L194] [08:37.52] it seems to be a commonality.
[L195] [08:40.72] Um I also saw somewhere else in
[L196] [08:43.28] something that you had said was that um
[L197] [08:47.28] when Oracle acquired my SQL that
[L198] [08:50.88] everyone kind of got afraid of that and
[L199] [08:53.84] moved to Postgress. That was the genesis
[L200] [08:58.56] of Postgress replacing MySQL as the
[L201] [09:02.96] preferred open-source relational
[L202] [09:05.04] database system.
[L203] [09:07.04] So you you created ingress and there was
[L204] [09:09.76] a lot of technical innovations in it so
[L205] [09:12.48] that it was better than the the
[L206] [09:14.24] incumbents but ultimately it it went
[L207] [09:18.00] away and you developed Postcrest. What
[L208] [09:20.00] what was the thing that Ingress didn't
[L209] [09:21.76] do that Postgress would do? Uh the big
[L210] [09:25.36] thing that guided us at the very
[L211] [09:26.96] beginning
[L212] [09:29.20] was the the original reasoning
[L213] [09:32.48] for
[L214] [09:34.08] the academic version of Ingress was we
[L215] [09:37.20] were going to support a geographic
[L216] [09:40.08] information system that the neighboring
[L217] [09:43.84] professor Pine Veriah wanted.
[L218] [09:47.20] And so to support a GIS system, you need
[L219] [09:51.12] points, lines, polygons, line groups,
[L220] [09:54.48] that sort of stuff.
[L221] [09:56.72] And it was clear that Ingress couldn't
[L222] [10:00.16] do it because the data types we put into
[L223] [10:04.00] Ingress were the standard ones,
[L224] [10:06.32] integers, floats, uh, text, strings, and
[L225] [10:11.52] you couldn't support, you couldn't
[L226] [10:13.92] efficiently support
[L227] [10:16.24] uh, GIS types on top of that. So, as a
[L228] [10:21.28] GIS, the academic version of Incorus was
[L229] [10:24.48] a complete failure.
[L230] [10:27.12] And that was in the back of of our mind.
[L231] [10:31.04] The other thing that happened, this is a
[L232] [10:33.20] little out of chronic chronological
[L233] [10:35.52] sequence, but it helps make the point is
[L234] [10:39.12] that the commercial version of Ingress I
[L235] [10:42.64] think around
[L236] [10:44.56] 1985.
[L237] [10:46.88] uh you know there was ANIE had just
[L238] [10:49.36] proposed
[L239] [10:50.88] uh a date and time standard for
[L240] [10:53.28] relational databases
[L241] [10:55.44] and so uh commercial Ingress implemented
[L242] [10:59.44] date and time
[L243] [11:01.52] uh you know using the standard Gregorian
[L244] [11:04.64] calendar and so I was associated with
[L245] [11:08.56] the commercial version of Ingress as
[L246] [11:10.48] well as I was still at the University of
[L247] [11:13.84] California as a professor so I I got a
[L248] [11:16.64] call from from an Ingress customer who
[L249] [11:21.12] said, you know, you implemented date and
[L250] [11:23.20] time wrong. And I said, huh? We
[L251] [11:26.96] implemented the Gregorian calendar and
[L252] [11:29.28] you can subtract
[L253] [11:31.36] uh and you know if it has, you know,
[L254] [11:34.48] days have 30 or 31 months except for
[L255] [11:37.12] February, except for leap years. So
[L256] [11:40.64] subtraction on dates works exactly the
[L257] [11:43.84] way you would expect it to.
[L258] [11:46.08] But he said that's not what I want in
[L259] [11:49.68] his particular world. He he said he was
[L260] [11:54.16] he was dealing with with
[L261] [11:57.20] bond financial instruments and for some
[L262] [12:00.48] reason I mean you got the same amount of
[L263] [12:04.24] interest on a on his financial bonds
[L264] [12:07.76] during each month no matter how long the
[L265] [12:10.56] month was.
[L266] [12:12.56] So he had the date you bought the bond,
[L267] [12:15.28] the date you sold the bond. He wanted to
[L268] [12:18.32] do a subtraction,
[L269] [12:20.32] multiply it by the coupon rate, and say
[L270] [12:23.68] that's what that's the interest we paid
[L271] [12:25.44] you.
[L272] [12:27.04] But of course, his version of
[L273] [12:28.88] subtraction was March 15 minus February
[L274] [12:32.64] 15th is 30 days because that's the
[L275] [12:35.60] definition of his calendar.
[L276] [12:38.24] And so he had to uh retrieve two dates
[L277] [12:42.96] out to user code, do the subtraction in
[L278] [12:45.44] user code, put the answer back, and it
[L279] [12:48.88] cost him a factor of two or three in in
[L280] [12:51.44] efficiency.
[L281] [12:52.96] And he said, "Why can't I just overload
[L282] [12:55.60] your definition of subtraction with what
[L283] [12:58.40] I want?" And of course with Ingress, it
[L284] [13:01.04] was hardcoded.
[L285] [13:02.80] And the problem was this is a case where
[L286] [13:06.64] you wanted bond time just like you
[L287] [13:09.84] wanted uh points, lines and polygons.
[L288] [13:13.12] And so Postgress was engineered to have
[L289] [13:15.36] an extendable type system.
[L290] [13:18.08] So you could have whatever data types
[L291] [13:19.68] you wanted and they were very efficient
[L292] [13:24.32] and that was the main gist of Postgress
[L293] [13:26.96] was that it had that flexibility.
[L294] [13:29.52] Uh and as
[L295] [13:32.40] you know in business data processing
[L296] [13:36.56] a lot most people were happy with the
[L297] [13:39.04] standard data types but relational
[L298] [13:42.96] databases started to spread to all kinds
[L299] [13:45.44] of other places what are called abstract
[L300] [13:47.76] data types or you know uh stored
[L301] [13:52.56] procedures you know bunch of names
[L302] [13:55.84] they're called uh you know had had great
[L303] [13:58.96] applicability
[L304] [14:00.80] and so Postgress that was that was the
[L305] [14:04.24] big thing in Postgress. Uh we also
[L306] [14:08.56] Postgress also
[L307] [14:11.44] uh supported what the AI guys at the
[L308] [14:14.00] time wanted in the way of inheritance.
[L309] [14:17.84] Uh we also supported time travel. Uh but
[L310] [14:22.72] the implementation absolutely sucked and
[L311] [14:26.08] it got taken out after a while. So there
[L312] [14:28.48] were a huge number of of really nifty
[L313] [14:31.44] things at Postgress.
[L314] [14:33.04] >> You mentioned you you want to hire
[L315] [14:35.28] extraordinary software engineers and I
[L316] [14:37.60] think you've you've said before that you
[L317] [14:39.84] have no trouble finding those people.
[L318] [14:42.80] How do you identify those people in your
[L319] [14:45.60] hiring that they're the extraordinary
[L320] [14:47.28] ones?
[L321] [14:48.96] It's usually pretty obvious. I mean I
[L322] [14:52.24] have a good feel for how difficult stuff
[L323] [14:55.20] is. if they get 3x the am the the amount
[L324] [14:59.04] done, you know, in school that I think
[L325] [15:02.32] is reasonable, then then they're
[L326] [15:04.40] incredible.
[L327] [15:05.84] >> On the flip side, you had this
[L328] [15:07.20] interesting quote. I wrote I wrote it
[L329] [15:09.04] down. He said, um, I can't stand people
[L330] [15:12.16] who are who aren't really smart. It's
[L331] [15:15.44] challenging to talk to them. How do you
[L332] [15:17.84] identify the people who aren't smart?
[L333] [15:20.72] >> Well, I mean, it's it's very easy. you
[L334] [15:23.60] you talk to them and and it it rapidly
[L335] [15:28.08] you can rapidly surface whether they're
[L336] [15:30.24] smart or not. You know, what was your
[L337] [15:32.48] master's thesis? What did you do? Uh
[L338] [15:36.16] well, how did it how did it exactly
[L339] [15:38.24] work? Well, how did you deal with error
[L340] [15:42.00] conditions?
[L341] [15:43.68] Uh [snorts] how many processes did you
[L342] [15:45.52] have? Why didn't you use threads?
[L343] [15:49.12] I only you ask them technical deep
[L344] [15:51.60] technical quest questions.
[L345] [15:54.40] >> You you gave a talk and I think there's
[L346] [15:56.00] also a paper behind it of this idea that
[L347] [15:59.68] uh one sizefits all database systems not
[L348] [16:02.80] optimal one size actually fits none and
[L349] [16:05.92] that what you really want is database
[L350] [16:09.04] solutions that target specific needs.
[L351] [16:12.48] What database offerings you see today
[L352] [16:14.40] that are one-sizefits-all? In 2004 when
[L353] [16:17.76] I wrote the paper, we had an academic
[L354] [16:20.32] project which was building what became
[L355] [16:23.52] streambase. And so a stream processing
[L356] [16:26.40] engine looks nothing like a relational
[L357] [16:29.44] database.
[L358] [16:30.96] And we had the gist of an idea for
[L359] [16:34.88] column stores for the for data
[L360] [16:36.88] warehouses which was popularized by
[L361] [16:39.84] Vertica looks nothing like a row store.
[L362] [16:43.44] So here were three wildly different
[L363] [16:45.76] implementations that had no resemblance
[L364] [16:48.40] to each other and in each case they were
[L365] [16:51.44] an order of magnitude faster than the
[L366] [16:54.32] other guys. So it's pretty clear that
[L367] [16:57.04] one side, you know, that in with those
[L368] [16:59.68] three instances,
[L369] [17:01.92] you give up an order of magnitude
[L370] [17:04.88] uh when you're running a database system
[L371] [17:08.00] that isn't
[L372] [17:10.00] that isn't architected for your kind of
[L373] [17:12.16] stuff. I think that's still true. I
[L374] [17:15.92] mean, I think Clickhouse is a column
[L375] [17:18.40] store. Pine cone is faster than
[L376] [17:23.84] userdefined types
[L377] [17:26.64] on on textbased vector processing.
[L378] [17:31.52] And so I think it's it's still very much
[L379] [17:34.48] the case [snorts] and I think
[L380] [17:38.40] there's no difficulty
[L381] [17:41.20] putting a common parser on top of
[L382] [17:43.68] multiple implementations.
[L383] [17:46.80] uh Postgress has so far chosen not to do
[L384] [17:49.92] that. they don't implement a column
[L385] [17:52.88] store
[L386] [17:54.48] and so I think they are not they are not
[L387] [17:56.88] competitive you know on sizable data
[L388] [18:00.88] warehouses
[L389] [18:02.72] they also don't have multi-node support
[L390] [18:06.32] again for people with big data
[L391] [18:08.08] warehouses that's table stakes so I
[L392] [18:11.44] think it's just as true today as it ever
[L393] [18:13.52] was I think that
[L394] [18:17.28] what is true
[L395] [18:19.52] is that if you want to get going, you
[L396] [18:21.92] have a database problem,
[L397] [18:24.64] you know, the answer is choose Postgress
[L398] [18:27.62] [snorts] and there's a huge programming
