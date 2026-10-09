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
[L399] [18:29.84] community, all kinds of all kinds of,
[L400] [18:32.96] you know, data type implementations.
[L401] [18:35.76] it's free uh and you can find Postgress
[L402] [18:41.36] talent easily and get going
[L403] [18:44.72] and and so I think it's it's it's a
[L404] [18:47.68] great choice for lowest common
[L405] [18:49.36] denominator
[L406] [18:51.28] and until you're trying to do [snorts] a
[L407] [18:55.84] million transactions a second it works
[L408] [18:57.84] just fine until you're trying to support
[L409] [19:01.04] a pabyte data warehouse it it I say at
[L410] [19:03.92] the low end it it's absolutely
[L411] [19:05.44] Absolutely the right one sizefits-all at
[L412] [19:07.92] the low end it's Postgress at the high
[L413] [19:10.72] end that's just not true
[L414] [19:13.12] >> GPUs do they make available some new
[L415] [19:16.56] opportunities to optimize databases
[L416] [19:19.44] probably but I think the the big
[L417] [19:22.08] challenge is that GPUs are
[L418] [19:27.20] you know sum simd you know single
[L419] [19:29.92] instruction multi- data and that's
[L420] [19:32.64] that's the anathema of indexing
[L421] [19:36.08] And so whenever indexing is the right
[L422] [19:38.40] answer, they're probably not a good
[L423] [19:41.36] idea.
[L424] [19:43.44] And I think uh also you've got to
[L425] [19:47.76] architect them so that the so that the
[L426] [19:51.52] bandwidth
[L427] [19:53.44] so that the bandwidth from storage is is
[L428] [19:57.76] not not the bottleneck. And so if
[L429] [20:01.52] they're an add-on to the CPU as often as
[L430] [20:04.16] not the bus connecting it to the the GPU
[L431] [20:07.68] to the CPU is a bottleneck.
[L432] [20:10.08] >> Can you explain why indexing would be
[L433] [20:13.52] not as effective when there's SIMD?
[L434] [20:17.84] >> So let's let's say I'm I'm [snorts]
[L435] [20:21.60] looking for Ryan's
[L436] [20:24.40] I'm looking for Ryan's salary and I have
[L437] [20:26.56] a B tree.
[L438] [20:28.64] So you go to the root of the B tree.
[L439] [20:32.24] You find you find the divider that has
[L440] [20:36.16] both sides of Ryan.
[L441] [20:38.48] You follow the pointer.
[L442] [20:41.12] That's a memory access for sure. Then
[L443] [20:44.24] you do it all again and you do this like
[L444] [20:47.04] three or four times.
[L445] [20:49.28] So that doesn't parallelize well. So the
[L446] [20:52.00] answer is indexing doesn't parallelize
[L447] [20:54.24] well. You mentioned B trees. When you
[L448] [20:56.64] first implemented
[L449] [20:58.48] uh that first version of ingress, did
[L450] [21:01.36] you write all of that by hand? Because I
[L451] [21:03.84] imagine there's probably not some
[L452] [21:05.44] existing B tree library or something.
[L453] [21:08.16] >> Yeah, we wrote the original version of
[L454] [21:10.32] ingress was all written from scratch.
[L455] [21:12.96] >> What was the hardest part of that
[L456] [21:14.24] implementation?
[L457] [21:16.56] >> Uh query optimizer.
[L458] [21:18.56] >> And why was that hard?
[L459] [21:20.24] >> It's tough. It's it's just
[L460] [21:24.48] algorithmically difficult. It's still if
[L461] [21:27.68] you ask most any senior database
[L462] [21:30.88] programmer what's the hardest hardest
[L463] [21:33.44] part, they'll still say the optimizer.
[L464] [21:36.80] Map produce came out at some point in
[L465] [21:39.20] the early 2000s and it kind of took the
[L466] [21:41.68] data world by storm. People were really
[L467] [21:44.56] impressed by it. They thought Google
[L468] [21:46.40] really knows what they're doing. this is
[L469] [21:48.56] the best thing since sliced bread. But
[L470] [21:51.28] it seems like when I look at the
[L471] [21:53.92] literature and what you thought at the
[L472] [21:55.44] time, you kind of disagreed heavily. Why
[L473] [21:58.08] did you disagree so much with uh map
[L474] [22:00.80] produce?
[L475] [22:02.32] Well, I think
[L476] [22:04.80] there were a lot of
[L477] [22:07.28] not very enlightened people who said
[L478] [22:09.44] Google Google is really smart. They must
[L479] [22:12.32] know what they're doing and so we'll do
[L480] [22:15.36] whatever they say. And so they would
[L481] [22:18.40] they would uh they would engage in
[L482] [22:22.56] Hadoop or engage with Hadoop. But Hadoop
[L483] [22:26.16] is ridiculously inefficient. And so uh
[L484] [22:30.24] at the time,
[L485] [22:32.64] you know, others, you know, Dave Dwit
[L486] [22:34.64] and others who who were involved in our
[L487] [22:36.88] 2011 paper, we understood distributed
[L488] [22:40.56] databases
[L489] [22:42.72] and understood that you could beat the
[L490] [22:44.80] heck out of Hadoop.
[L491] [22:46.80] uh with a distributed database system,
[L492] [22:49.20] which is basically what that 2011 paper
[L493] [22:52.56] says.
[L494] [22:54.08] And of course, it was it's true. And
[L495] [22:58.24] but that wasn't the only that wasn't the
[L496] [23:01.60] only thing Google was stupid about.
[L497] [23:04.80] So Google also
[L498] [23:08.08] had the opinion that eventual
[L499] [23:11.44] consistency was the right way to do
[L500] [23:14.00] concurrency control.
[L501] [23:16.64] And so that was postulated from on high
[L502] [23:20.64] by Google all during that same period of
[L503] [23:23.68] time.
[L504] [23:25.36] And it it wasn't and all the database
[L505] [23:29.44] people said, you know, you're out of
[L506] [23:31.84] your frigin mind because it doesn't it
[L507] [23:36.24] solves one particular kind of problem
[L508] [23:38.80] but only and that very rarely occurs in
[L509] [23:41.84] practice. Why did they pursue eventual
[L510] [23:44.48] consistency?
[L511] [23:45.68] >> Okay, well the idea is that you have an
[L512] [23:47.76] east coast database and a west coast
[L513] [23:49.44] database and they're replicas. So you
[L514] [23:51.36] want them to be the same. If you say I'm
[L515] [23:56.00] going to do a transaction, I'm going to
[L516] [23:58.16] decrement by one the number of widgets
[L517] [24:01.36] in the west coast warehouse then I'm
[L518] [24:04.16] going to with before I commit that
[L519] [24:06.72] transaction I'm going to update the east
[L520] [24:09.44] coast warehouse pay pay a message over
[L521] [24:11.68] and back to update it and then to make
[L522] [24:15.36] sure everything goes well it takes a it
[L523] [24:17.68] takes another roundtrip a message to
[L524] [24:20.56] make sure that both of them actually do
[L525] [24:23.68] the commit correctly. So it's expensive
[L526] [24:26.56] to do a distributed commit and it still
[L527] [24:30.24] is. And so the idea was well you you do
[L528] [24:35.12] the e you do the west coast update you
[L529] [24:37.68] decrease the widgets by one you just
[L530] [24:39.52] send a message asynchronously and not in
[L531] [24:42.64] a transaction so that eventually the
[L532] [24:45.84] east coast uh warehouse gets decremented
[L533] [24:49.44] by one.
[L534] [24:51.36] So meanwhile,
[L535] [24:53.44] if you're on the east coast, you you
[L536] [24:55.92] decrement, you know, food stuffs by one.
[L537] [24:59.52] You send an asynchronous message.
[L538] [25:01.84] Eventually, the West Coast gets it and
[L539] [25:04.48] eventually everything settles out. So if
[L540] [25:10.16] you're allowed to to go below zero
[L541] [25:14.72] then what will happen is if the east
[L542] [25:16.72] coast guy and the west coast guy
[L543] [25:18.24] simultaneously
[L544] [25:20.24] sell the last widget
[L545] [25:22.64] then then eventually
[L546] [25:25.28] uh the
[L547] [25:27.44] state of the warehouse will be minus one
[L548] [25:32.16] and somebody won't get their widget
[L549] [25:34.32] their widget
[L550] [25:36.80] and So, uh, if if you're allowed like
[L551] [25:41.36] Amazon to say usually ships in 24 hours,
[L552] [25:45.12] then maybe you're can allowed to
[L553] [25:47.68] oversell, but most enterprises can't do
[L554] [25:51.60] that. And so eventual consistency just
[L555] [25:54.88] doesn't work. So, we talked a million
[L556] [25:58.64] hours ago about referential integrity.
[L557] [26:01.92] So referential integrity in a sales
[L558] [26:04.32] system is uh integrity constraint is
[L559] [26:08.40] stock is greater than minus one and that
[L560] [26:12.08] fails
[L561] [26:13.60] with eventual consistency.
[L562] [26:16.32] And so uh Jeff Dean finally of Google
[L563] [26:19.92] finally figured that out
[L564] [26:22.40] and uh when they did Spanner, Spanner
[L565] [26:26.16] had a conventional transactional system
[L566] [26:29.04] and so Google comp uh completely
[L567] [26:31.84] abandoned eventual consistency
[L568] [26:34.72] and completely abandoned map reduce.
[L569] [26:37.84] >> So the trade-offs basically um
[L570] [26:40.64] correctness for performance. So, it's
[L571] [26:43.04] performance versus data integrity. And
[L572] [26:46.00] if you don't care about your data,
[L573] [26:48.80] then you're willing to deal with with
[L574] [26:52.00] bad things happening.
[L575] [26:54.24] So, did you ever talk to the Google team
[L576] [26:56.64] while they were doing those things that
[L577] [26:58.48] you thought were so wrong? We talked to
[L578] [27:01.28] them before the
[L579] [27:05.20] 2011 paper
[L580] [27:08.64] and said, "Why why don't we why don't we
[L581] [27:12.32] partner up and do some stuff?" And they
[L582] [27:15.84] weren't they weren't interested.
[L583] [27:18.24] So, they declined. Have you seen other
[L584] [27:20.72] examples in other big tech companies
[L585] [27:22.64] where their databases or database
[L586] [27:25.20] solutions where you actively disagree
[L587] [27:27.76] with them? like maybe Amazon or or
[L588] [27:30.64] Facebook. Well, I gave a talk at Amazon
[L589] [27:34.08] maybe three years ago
[L590] [27:37.04] and I told them all the things I thought
[L591] [27:38.96] they were doing wrong and I think uh
[L592] [27:44.16] Amazon's problem is that they are
[L593] [27:47.36] supporting you know
[L594] [27:50.72] 15 different database systems
[L595] [27:53.76] and that's about 12 too many. So, so I
[L596] [27:58.16] think they have their own culture and I
[L597] [28:01.04] told I I said you're supporting too many
[L598] [28:03.36] database systems
[L599] [28:05.52] and at this point they haven't chosen to
[L600] [28:07.76] retire any of them.
[L601] [28:09.76] >> Why do you say that the 15 should be
[L602] [28:12.08] three? Well, they're supporting a
[L603] [28:14.56] graph-based database system, and it's
[L604] [28:17.44] well understood that a graph-based
[L605] [28:21.12] database system is almost never the
[L606] [28:25.12] performant option.
[L607] [28:27.92] And so, if you want a graph, if you
[L608] [28:31.20] want, if you like the idea of having a
[L609] [28:34.96] user interface that deals with nodes and
[L610] [28:38.72] edges, that's fine. put put a layer on
[L611] [28:41.52] top of a relational database system that
[L612] [28:44.56] gives you that user model. And so most
[L613] [28:48.88] of their database systems, there's some
[L614] [28:51.52] other of their database systems that
[L615] [28:53.44] better at what it does than
[L616] [28:56.72] than it is.
[L617] [28:59.04] And so so the answer is you should
[L618] [29:01.12] retire
[L619] [29:04.32] you should retire any database system
[L620] [29:06.56] that isn't performant
[L621] [29:10.24] in in a big enough market to justify the
[L622] [29:13.36] maintenance. you've uh influenced
[L623] [29:16.32] industry significantly from academia
[L624] [29:19.92] and my one thought that I had is what
[L625] [29:24.24] why not work directly in industry or why
[L626] [29:28.08] why do you prefer the position of being
[L627] [29:30.56] in academia and having influence in the
[L628] [29:32.88] way that you have versus just uh taking
[L629] [29:36.16] a job at AWS or something like that
[L630] [29:38.72] being a very you know distinguished
[L631] [29:40.64] engineer there
[L632] [29:43.20] uh because that gives you to a boss.
[L633] [29:45.55] [laughter]
[L634] [29:46.64] And that gives you company rules, limits
[L635] [29:49.44] your ability to publish, limits your
[L636] [29:52.16] ability to go talk at conferences,
[L637] [29:55.12] uh limits your abil your ability to
[L638] [30:01.20] go go poke at what what various
[L639] [30:04.64] competitors are doing that they won't
[L640] [30:07.68] tell their competitors.
[L641] [30:10.40] But mostly I really like being in
[L642] [30:12.72] startups and I and I after the
[L643] [30:15.28] commercial version of Postgress got
[L644] [30:17.28] acquired by InformX.
[L645] [30:19.60] You know I was working part-time for
[L646] [30:22.64] InformX
[L647] [30:24.40] which was a 2,000 person company and I
[L648] [30:27.28] didn't feel like I could make a
[L649] [30:28.80] difference because it was bureaucratic
[L650] [30:32.16] and and whatever the president wanted he
[L651] [30:35.76] got.
[L652] [30:38.40] So, I think I'm just not cut out for I'm
[L653] [30:41.92] not cut out for politicking. I don't do
[L654] [30:44.16] that very well
[L655] [30:46.32] and I have a hard time interacting with
[L656] [30:48.80] people I think are dumb and that again.
[L657] [30:51.68] So, I guess I I I have I have some
[L658] [30:54.64] problems with with big companies.
[L659] [30:58.00] >> I I want to talk a little bit about
[L660] [31:00.24] Debboss. I just thought it was a really
[L661] [31:02.80] interesting technical model. Can you
[L662] [31:05.36] explain what the boss is? We started the
[L663] [31:09.12] academic project in
[L664] [31:12.48] 20
[L665] [31:14.96] 19 2020 something like that. And the
[L666] [31:18.40] gist of it was
[L667] [31:20.88] uh at that point Mate Mate Haria who is
[L668] [31:24.88] on the faculty at Stanford was also one
[L669] [31:27.52] of the founders of data bricks was the
[L670] [31:30.16] original creator of Spark.
[L671] [31:33.68] And so he said uh
[L672] [31:38.08] at the time data bricks you know
[L673] [31:40.48] basically was running people's spark
[L674] [31:43.60] jobs on the cloud. And so he said at any
[L675] [31:48.16] given time we might be orchestrating a
[L676] [31:52.08] million Spark jobs.
[L677] [31:54.40] And so we have to write a scheduler
[L678] [31:57.04] that's going to decide who to run next
[L679] [32:00.88] at scale a million.
[L680] [32:03.28] And he said there was no we tried all
[L681] [32:06.40] the all the schedulers written by the OS
[L682] [32:09.28] folks and they they couldn't they didn't
[L683] [32:12.32] scale.
[L684] [32:14.64] So we put all the scheduling data in a
[L685] [32:16.64] Postgress database and basically a
[L686] [32:20.24] Postgress application was doing
[L687] [32:22.16] scheduling and then it sort of clicked
[L688] [32:24.88] that by and large most everything you do
[L689] [32:28.56] in an operating system
[L690] [32:30.96] is managing data at scale
[L691] [32:34.00] and you should do that using database
[L692] [32:36.40] technology.
[L693] [32:38.32] So why don't we just replace at least
[L694] [32:41.28] the upper half of Linux with a database
[L695] [32:44.24] system.
[L696] [32:46.88] So that was the gist of the academic
[L697] [32:49.36] project and we worked on it at Berkeley
[L698] [32:52.64] and Stanford
[L699] [32:54.48] uh in the early early 20s and it was it
[L700] [32:59.12] was very successful. It clearly it
[L701] [33:02.16] clearly worked.
[L702] [33:04.24] And in the process
[L703] [33:07.20] uh the Stanford folks wrote an extension
[L704] [33:12.56] to uh JavaScript so that you could
[L705] [33:15.84] program you need some programming world
[L706] [33:18.32] that can can talk to your
[L707] [33:21.44] implementation.
[L708] [33:23.68] So if you're doing what amounts to a
[L709] [33:27.52] programming language and you're running
[L710] [33:30.08] on top of what amounts to an operating
[L711] [33:32.96] system that is a database,
[L712] [33:35.76] then the obvious thing to do is put all
[L713] [33:37.92] your state in the database. And that's
[L714] [33:40.00] exactly what they did. And so we had an
[L715] [33:42.40] innovative
[L716] [33:44.08] programming language model, an
[L717] [33:46.64] innovative operating system model
[L718] [33:50.40] and and of course then the idea was well
[L719] [33:53.84] can we start a company
[L720] [33:56.24] and so we talked to the VCs
[L721] [34:00.88] who to a person said
[L722] [34:04.88] you're you're dreaming if you think
[L723] [34:06.80] you're going to displace Linux. However,
[L724] [34:10.08] this programming language stuff is
[L725] [34:11.76] really nifty. We had what amounted to
[L726] [34:15.76] extensions to JavaScript
[L727] [34:19.84] that would allow
[L728] [34:21.92] any any program to have all of the nice
[L729] [34:24.88] features of a database system. You know,
[L730] [34:27.76] stuff was durable. You could have
[L731] [34:29.84] transactions.
[L732] [34:31.52] If it failed, you'd fail over. You know,
[L733] [34:34.32] it was all that nifty stuff.
[L734] [34:37.36] So we got funded
[L735] [34:39.60] uh to start a company in 2023
[L736] [34:44.80] and that was Debboss Incorporated and we
[L737] [34:49.12] decided that that was the name of the
[L738] [34:51.04] project since it always been the name of
[L739] [34:53.44] the project
[L740] [34:55.20] but we were ba we were basically in the
[L741] [34:57.84] programming language business and so at
[L742] [35:00.72] the current time uh deboss has a version
[L743] [35:05.20] of Typescript a version of Java, version
[L744] [35:07.76] of Joe, Go,
[L745] [35:10.56] and a version of Python, which which are
[L746] [35:15.60] basically seamless. It runs what looks
[L747] [35:18.40] like vanilla programs. In the world of
[L748] [35:23.44] the cloud, there's every incentive for
[L749] [35:26.80] you to structure your your your
[L750] [35:28.88] application as a workflow.
[L751] [35:31.36] And so we decided that we would support
[L752] [35:34.96] a workflow system period.
[L753] [35:38.48] And so the workflow that that deboss
[L754] [35:43.04] supports in [snorts] those four
[L755] [35:45.12] languages is the steps in in a workflow,
[L756] [35:50.32] the individual
[L757] [35:52.40] micro apps, whatever you want to call
[L758] [35:54.32] them, are transactional.
[L759] [35:57.36] Uh workflows are durable. So that once
[L760] [36:00.80] you do a step it's not forgotten.
[L761] [36:04.48] Uh and it's clear that we can make
[L762] [36:10.00] uh workflows atomic if there was a
[L763] [36:13.44] market for it which means the whole
[L764] [36:16.08] workflow would either finish or look
[L765] [36:19.60] like it never happened. So it has very
[L766] [36:22.32] very nice properties
[L767] [36:24.64] and is
[L768] [36:27.52] a great deal faster and a great deal
[L769] [36:29.36] easier to use than the competition.
[L770] [36:32.48] So
[L771] [36:34.00] the company is selling and innovating in
[L772] [36:37.28] this area.
[L773] [36:39.60] And so so the idea is that you want to
[L774] [36:43.04] make state of your application
[L775] [36:45.52] persistent when you put it in the
[L776] [36:47.84] database. uh and then it and then you
[L777] [36:50.96] figure out how to do it fast.
[L778] [36:53.68] And I [snorts] think their their
[L779] [36:56.80] business model as we were talking
[L780] [36:59.44] earlier is very much get and get leaf
[L781] [37:04.16] level programmers
[L782] [37:06.32] interested.
[L783] [37:07.92] So it's been very much uh you know tell
[L784] [37:11.84] us leaf level programmer tell us what
[L785] [37:14.56] you need that we don't have get it
[L786] [37:17.44] quickly
[L787] [37:19.28] and convince people to try it and
[L788] [37:24.72] we've been very very successful with
[L789] [37:26.72] other with other startups who want to
[L790] [37:29.44] choose the best thing and we're starting
[L791] [37:32.40] to be to be successful with the the big
[L792] [37:35.20] boys. So it's it's an interesting
[L793] [37:39.36] interesting market and I think the key
[L794] [37:42.16] thing so far it's
[L795] [37:46.88] probably twothirds of the customers are
[L796] [37:50.16] doing agentic AI which means that they
[L797] [37:54.16] have a large language model surrounded
[L798] [37:56.56] by a bunch of stuff that that adds more
[L799] [38:00.88] signal
[L800] [38:02.48] and so far
[L801] [38:05.76] Most of Agentic AI is read only,
[L802] [38:10.00] meaning uh you want to produce a
[L803] [38:12.96] prediction
[L804] [38:14.56] for whether Ryan is is going to be a
[L805] [38:17.20] good customer or not. And so that just
[L806] [38:20.64] runs some stuff and then produces a new
[L807] [38:23.52] thing that's given to somebody. So
[L808] [38:27.92] basically read only which means that uh
[L809] [38:33.28] you're not you're not actually updating
[L810] [38:37.28] Ryan's credit rating or and so I think
[L811] [38:42.24] fairly quickly this the whole world is
[L812] [38:45.60] going to move to using
[L813] [38:48.00] you know agents to do read write
[L814] [38:50.64] applications
[L815] [38:52.24] and that's going to make that's going to
[L816] [38:54.48] make them very very databasey
[L817] [38:58.48] and DeBoss does that stuff really really
[L818] [39:01.92] well. And so, you know, for instance, if
[L819] [39:06.16] you want to write an agent or two agents
[L820] [39:10.24] that move a $100 from my account to your
[L821] [39:14.08] account.
[L822] [39:15.60] And so you debit my account, you
[L823] [39:17.92] increment your account
[L824] [39:20.24] and these two agents have to agree to
[L825] [39:23.76] commit
[L826] [39:25.60] or you have to back everything out,
[L827] [39:29.12] which is to say the workflow [snorts]
[L828] [39:31.92] needs to be what I called atomic, which
[L829] [39:34.48] is it all happens or it looks like it
[L830] [39:37.20] never happened. And so I think the the
[L831] [39:40.32] demands on in this market will escalate
[L832] [39:45.28] with with things with people wanting
[L833] [39:47.84] stuff to be read, right? And so I think
[L834] [39:50.72] that that will bode well for the market
[L835] [39:54.16] and bode well for deboss.
[L836] [39:57.20] And this this what's being offered in
[L837] [39:59.36] the market today to application
[L838] [40:01.52] developers differs from the original
[L839] [40:04.00] research project where that was actually
[L840] [40:06.16] swapping out the guts of an operating
[L841] [40:08.24] system with a database. I see that's I
[L842] [40:11.68] mean that's really cool. I never
[L843] [40:12.96] imagined replacing all the state of a of
[L844] [40:16.16] an operating system with a database.
[L845] [40:18.32] What's the there there's got to be some
[L846] [40:20.80] trade-off there.
[L847] [40:22.88] Well, a file system written on top of a
[L848] [40:25.68] DBMS is faster than than the Linux file
[L849] [40:30.16] system. The scheduling engine is
[L850] [40:33.36] competitive with other scheduling
[L851] [40:35.20] engines. You can make everything fail
[L852] [40:38.16] over. So, you get high availability
[L853] [40:41.12] without having to do anything else. The
[L854] [40:44.48] answer is there there's really no
[L855] [40:47.28] downside.
[L856] [40:49.84] Then why wouldn't Linux
[L857] [40:52.08] incorporate that and upgrade itself with
[L858] [40:55.12] this? You hope they would. In other
[L859] [40:58.24] words, you should you should keep all
[L860] [41:00.56] the device driver junk down at the
[L861] [41:02.56] bottom because that's there's a lot of
[L862] [41:04.96] it and no one wants to do that and
[L863] [41:08.48] replace everything else with the
[L864] [41:10.00] database implementation.
[L865] [41:12.40] Is that something that you've mentioned
[L866] [41:14.08] to Linux people and what's their typical
[L867] [41:16.64] reaction
[L868] [41:17.84] >> back in the academic project when I'd
[L869] [41:20.32] mentioned that to operating system folks
[L870] [41:23.76] they would get very very threatened
[L871] [41:26.48] which is this is the database guys
[L872] [41:28.96] trying to take over their turf
[L873] [41:32.32] and I think the programming language
[L874] [41:34.40] guys ditto you know which is you know
[L875] [41:37.52] the the the
[L876] [41:40.32] way to implement the runtime for a
[L877] [41:42.72] programming environment is with a
[L878] [41:44.72] database.
[L879] [41:46.48] >> That's uh that's interesting. I mean, if
[L880] [41:48.96] it's objectively true, then maybe it
[L881] [41:50.80] will take over.
[L882] [41:53.04] >> Well, I mean, it took Java 10 years to
[L883] [41:56.08] become widely accepted. I just think the
[L884] [41:59.12] time constant is substantial. I think we
[L885] [42:02.80] talked a lot about the past of databases
[L886] [42:05.20] and I'm curious your thoughts on
[L887] [42:07.76] unsolved problems in databases and what
[L888] [42:10.80] you think the future might look like.
[L889] [42:13.12] >> Okay. So I think two different things
[L890] [42:15.60] that I'd like to talk about. The first
[L891] [42:18.48] one is
[L892] [42:20.40] like everyone else
[L893] [42:23.44] three years ago we started to look at
[L894] [42:26.56] what were large language models good
[L895] [42:28.64] for. So, we've been trying to get what's
[L896] [42:33.60] now called text to SQL
[L897] [42:36.64] uh to we've been we've been trying to
[L898] [42:39.92] make it work
[L899] [42:42.72] on real world databases,
[L900] [42:46.88] especially real world data warehouses.
[L901] [42:50.48] So we've been trying the technology
[L902] [42:54.08] on four different production databases
[L903] [42:57.28] warehouses
[L904] [42:59.04] where we've gotten the workload the
[L905] [43:02.00] actual workload that's run
[L906] [43:05.20] and
[L907] [43:06.96] you know from the actual users using the
[L908] [43:10.08] system
[L909] [43:11.86] [clears throat] and we've gotten them to
[L910] [43:14.48] reverse engineer the text that
[L911] [43:17.20] corresponds to that sequence. So we have
[L912] [43:20.64] text and SQL for we have four
[L913] [43:25.04] benchmarks.
[L914] [43:26.40] >> When you say text to SQL, you mean uh
[L915] [43:28.64] like a human prompting model or
[L916] [43:31.12] something like I would just in English
[L917] [43:33.68] that text would be you know everyone
[L918] [43:36.32] over four years old. Tell me all the
[L919] [43:38.96] professors at MIT who won the touring
[L920] [43:41.76] award. And so an LLM is supposedly good
[L921] [43:45.44] at that.
[L922] [43:48.48] And so uh the text to SQL benchmarks
[L923] [43:52.72] there's a one called spider another one
[L924] [43:54.72] called bird
[L925] [43:56.80] and the best LLM systems are pretty good
[L926] [43:59.60] at those benchmarks you know like 80%
[L927] [44:02.64] accuracy or better
[L928] [44:04.40] >> so not superhuman
[L929] [44:06.80] >> not superhuman but they're pretty good
[L930] [44:09.04] like you would consider using them a and
[L931] [44:12.64] you know like current current
[L932] [44:14.40] leaderboard is something like 85% %
[L933] [44:16.96] accuracy, which I mean it's getting
[L934] [44:19.36] there. You say maybe it's not quite
[L935] [44:21.52] ready for prime time, but it's simply it
[L936] [44:23.76] certainly
[L937] [44:25.28] looks looks pretty good.
[L938] [44:28.24] Well, on our benchmarks,
[L939] [44:30.80] uh, large language models get 0%. And if
[L940] [44:35.60] you enhance them with rag and and all
[L941] [44:38.72] the tricks goes to 10%. And if you give
[L942] [44:42.72] as a prompt the from clause, in other
[L943] [44:46.08] words, all the actual tables that need
[L944] [44:48.24] to be accessed [snorts] and all the
[L945] [44:51.28] actual join clauses that need to be
[L946] [44:53.60] joined, then accuracy goes to about 35%.
[L947] [45:00.16] So the definition of this stuff doesn't
[L948] [45:04.08] is not ready for prime time and not
[L949] [45:07.52] going to be for a while, if ever.
[L950] [45:10.48] So what what's the difference? Uh number
[L951] [45:13.52] one, data wareh you know LL LLMs are
[L952] [45:17.36] trained on the pile.
[L953] [45:20.00] Data warehouse data is not in the pile.
[L954] [45:23.20] And there's an adage that if you haven't
[L955] [45:25.44] seen the data a couple times before, you
[L956] [45:29.12] have no chance of regurgitating it.
[L957] [45:32.88] That's number one. Uh number two uh
[L958] [45:37.76] query complexity on spider and bird is
[L959] [45:40.80] maybe 10 to 20 lines of SQL. Real world
[L960] [45:45.44] data warehouses it's 100 lines of SQL.
[L961] [45:49.36] Complexity is bigger.
[L962] [45:51.76] Number three the schema in spider and
[L963] [45:55.84] bird is clean.
[L964] [45:58.24] You know the table names are are mmonic.
[L965] [46:02.08] The column names are pneummonic and
[L966] [46:04.24] there's no duplication.
[L967] [46:06.80] In data warehouses, people have
[L968] [46:08.96] materialized views all the time. It
[L969] [46:11.68] means there's redundancy
[L970] [46:14.16] and and column names are often
[L971] [46:18.16] underscore
[L972] [46:19.68] Zuppers blah. And so they're not mmonic.
[L973] [46:24.80] So that makes it a lot harder. uh and
[L974] [46:28.08] then they also have idiosyncratic data.
[L975] [46:31.76] So J term is popular thing at MIT. It's
[L976] [46:35.84] a one-month term in January.
[L977] [46:39.44] Not unique to to MIT but not very
[L978] [46:43.12] popular.
[L979] [46:44.88] So not in the pile
[L980] [46:47.52] idiosyncratic data simple queries schema
[L981] [46:53.44] schema is a mess.
[L982] [46:56.64] make make it not work. And those are
[L983] [46:59.44] true of every data warehouse I know of.
[L984] [47:03.20] And so I think the the technology simply
[L985] [47:08.08] doesn't work and isn't going to work
[L986] [47:09.84] anytime soon.
[L987] [47:12.56] So we've been So what do you do? So well
[L988] [47:16.64] first of all we published our benchmark.
[L989] [47:19.12] It's a thing called Beaver, which is an
[L990] [47:21.92] anonymized
[L991] [47:23.60] and abstracted version of these four
[L992] [47:25.84] data warehouses.
[L993] [47:27.92] And so if you think you're really good
[L994] [47:30.16] at doing text to SQL, try a real
[L995] [47:33.20] benchmark, not a fake one.
[L996] [47:36.32] So number two, uh,
[L997] [47:40.40] borrowing from what I just said, if you
[L998] [47:43.28] don't have all the join terms and you
[L999] [47:45.12] don't have the from clause, you're
[L1000] [47:48.16] toast.
[L1001] [47:50.64] What's more, if you don't break down the
[L1002] [47:52.48] query into simpler pieces, you're toast.
[L1003] [47:57.20] So that says to me that uh you want to
[L1004] [48:04.72] give
[L1005] [48:06.80] your retrieval system simpler pieces
[L1006] [48:10.56] which include the from clause and
[L1007] [48:12.32] include join terms. That's number one.
[L1008] [48:15.76] Uh number two, the minute you want to
[L1009] [48:19.52] talk to two different structured
[L1010] [48:22.16] databases, you know, like your data
[L1011] [48:24.64] warehouse and your CRM system,
[L1012] [48:28.56] then it's pretty clear to me that doing
[L1013] [48:31.44] a structured data join using an LLM is a
[L1014] [48:35.92] bad idea. It's just you're much better
[L1015] [48:38.96] off
[L1016] [48:40.80] you leaving them as tables and doing a
[L1017] [48:43.20] join in SQL.
[L1018] [48:45.52] So our point of view is we are trying
[L1019] [48:47.76] out
[L1020] [48:49.28] turning everything into tables. You
[L1021] [48:51.60] know, we're we're working with the
[L1022] [48:54.16] Department of Transportation in the city
[L1023] [48:56.72] of Munich, Germany,
[L1024] [48:58.96] and they have six people full-time who
[L1025] [49:02.40] are answering citizens
[L1026] [49:05.12] complaints,
[L1027] [49:06.72] queries,
[L1028] [49:08.56] which are of the form, how come I don't
[L1029] [49:11.84] have enough time to cross this
[L1030] [49:14.80] intersection next to my house before the
[L1031] [49:17.68] light turns? All kinds of stuff. How
[L1032] [49:20.96] come the trolley doesn't stop for enough
[L1033] [49:23.68] time for me to get on the trolley? You
[L1034] [49:25.92] know, it's How come the trolley doesn't
[L1035] [49:28.32] come uh more than once an hour? I mean,
[L1036] [49:33.28] it's all this stuff. Their database is
[L1037] [49:36.80] the trolley schedule, that's SQL. The
[L1038] [49:39.44] light sequencing, that's SQL.
[L1039] [49:42.88] The intersections, that's CAD.
[L1040] [49:46.80] the federal
[L1041] [49:50.08] you know country of Germany regulations
[L1042] [49:52.96] of this stuff that's text city of Munich
[L1043] [49:57.68] regulations for this stuff which is text
[L1044] [50:01.20] so you got to join SQL SQL CAD text and
[L1045] [50:05.52] text so our point of view is turn it all
[L1046] [50:08.64] into SQL all into tables and do a join
[L1047] [50:12.56] with what amounts to a query optimizer
[L1048] [50:16.40] So that's what we're working on. I think
[L1049] [50:18.96] other people will have other ideas but I
[L1050] [50:21.68] think it's extremely fertile area
[L1051] [50:24.24] because people really want to do it.
[L1052] [50:27.76] So that's number one. Uh number two we
[L1053] [50:30.56] talked earlier about agentic AI. The
[L1054] [50:33.84] minute this becomes read write it's a
[L1055] [50:35.76] distributed database problem and you
[L1056] [50:38.56] want atomicity
[L1057] [50:40.96] consistency all that stuff. I think a
[L1058] [50:43.68] very interesting area. So that's pretty
[L1059] [50:47.84] much what I what I am what I'm working
[L1060] [50:50.40] on now
[L1061] [50:52.24] >> on that benchmark where it's 0% right
[L1062] [50:54.56] now. What percent is human? Like if you
[L1063] [50:58.48] took someone who really knows SQL, what
[L1064] [51:00.80] would they score like the average human?
[L1065] [51:03.04] So once you disambiguate the the text,
[L1066] [51:07.12] a a knowledgeable SQL user programmer
[L1067] [51:11.28] with the schema will do will will get
[L1068] [51:13.76] very high accuracy.
[L1069] [51:15.68] >> Okay. Like 90% or something at least.
[L1070] [51:18.72] >> Okay. Okay. Wow. It's I'm surprised that
[L1071] [51:22.16] the LM so score so lowly on on this kind
[L1072] [51:25.36] of benchmark. Maybe when this goes out,
[L1073] [51:27.76] someone who works at Anthropic will
[L1074] [51:29.60] reach out to you or something and say,
[L1075] [51:31.28] "Let's
[L1076] [51:31.92] >> I'd love to I'd love to find out because
[L1077] [51:35.04] I mean it's a terrific success story
[L1078] [51:38.32] >> for people who want to deeply understand
[L1079] [51:40.64] databases and they're looking for some
[L1080] [51:43.92] material to study. Is there a book that
[L1081] [51:46.72] you recommend that's a top technical
[L1082] [51:48.72] book to learn databases
[L1083] [51:50.88] >> papers in the literature?"
[L1084] [51:53.84] I think uh Joey Helerstein and I
[L1085] [51:56.56] published a red book what's called the
[L1086] [51:58.88] red book which is called readings and
[L1087] [52:01.28] database systems. It's now
[L1088] [52:05.92] eight years old. I mean I think that
[L1089] [52:08.80] that would be a great set of readings
[L1090] [52:10.88] for eight years ago
[L1091] [52:13.20] and beyond that uh papers
[L1092] [52:17.20] popular papers from the literature. If
[L1093] [52:20.24] you could go back to yourself when you
[L1094] [52:22.16] just graduated, give yourself some
[L1095] [52:24.56] advice knowing what you know today, what
[L1096] [52:26.40] would you say?
[L1097] [52:28.08] >> Back at when I first took the job at
[L1098] [52:30.56] Berkeley and without thinking about it
[L1099] [52:33.04] much, we said, "Let's write a database
[L1100] [52:34.80] system." And we we knew nothing about
[L1101] [52:37.20] databases,
[L1102] [52:39.20] nothing about implementations. We were
[L1103] [52:41.52] not skilled programmers
[L1104] [52:44.00] like Bill Joy. So starting off doing
[L1105] [52:47.84] something that was that crazy
[L1106] [52:50.64] was really pretty crazy.
[L1107] [52:53.28] And and you know you you effort and you
[L1108] [52:57.20] make stuff work and you learn along the
[L1109] [52:59.76] way. And so I think the answer is
[L1110] [53:03.84] think outside the box.
[L1111] [53:06.40] Think crazy thoughts
[L1112] [53:08.64] and try and do them.
[L1113] [53:11.12] And I think
[L1114] [53:13.60] to me it's not at all obvious. The the
[L1115] [53:17.36] better question is if you were starting
[L1116] [53:20.00] out today, what would you major in? Uh
[L1117] [53:23.28] because I think, you know, computer
[L1118] [53:26.00] science may well not be a growth
[L1119] [53:27.92] industry going forward. And I'm not sure
[L1120] [53:31.12] I would recommend 18 year olds to major
[L1121] [53:34.40] in computer science.
[L1122] [53:36.64] I mean, I think health health care and
[L1123] [53:38.80] and the building trades are are are safe
[L1124] [53:42.32] bets and everything else looks much
[L1125] [53:45.28] riskier. Uh, if if you're about to get
[L1126] [53:48.96] your PhD and are trying to decide what
[L1127] [53:51.28] to do,
[L1128] [53:53.04] then I think life is pretty easy. you
[L1129] [53:55.52] know, take take the most prestigious job
[L1130] [53:58.08] you can get
[L1131] [54:00.24] and find a mentor who's willing to help
[L1132] [54:03.60] you
[L1133] [54:05.28] and then pick some area that isn't, you
[L1134] [54:10.08] know, like our our stuff, you know,
[L1135] [54:12.56] which is called Rubicon, is definitely
[L1136] [54:14.88] not going with the flow. So, choose
[L1137] [54:18.40] something that's not that isn't going
[L1138] [54:20.96] with the flow
[L1139] [54:22.88] and try and make it work. Both my wife
[L1140] [54:25.20] and I said, "F follow your passion.
[L1141] [54:28.56] Somehow the money will work out." And I
[L1142] [54:31.68] don't believe that for a minute, but I
[L1143] [54:33.76] think that's what you have to tell your
[L1144] [54:35.20] kids. [laughter]
[L1145] [54:36.96] >> And your grandkids.
[L1146] [54:38.56] >> If you don't believe that, then uh why
[L1147] [54:41.04] do you have to tell them that?
[L1148] [54:42.90] [clears throat]
[L1149] [54:43.04] >> My wife is is a good example. So she has
[L1150] [54:46.16] an she has a master's degree in computer
[L1151] [54:49.04] science, undergraduate degree in
[L1152] [54:50.80] computer science, and she wanted to be a
[L1153] [54:54.16] teacher, you know, you know, K K12
[L1154] [54:57.84] teacher. And her parents said, "You
[L1155] [55:00.00] can't do that. It doesn't pay enough
[L1156] [55:01.60] money."
[L1157] [55:03.60] And so I think and I think she ever
[L1158] [55:06.48] since that time has regretted
[L1159] [55:09.52] that decision. She wasn't passionate
[L1160] [55:12.48] about doing computer science. it was
[L1161] [55:14.40] simply a trade.
[L1162] [55:17.20] And so I think find something you're
[L1163] [55:19.60] passionate about and and you will, you
[L1164] [55:23.04] know, either
[L1165] [55:25.20] you won't starve. You may not make a lot
[L1166] [55:27.76] of money, but I think chances are you'll
[L1167] [55:30.96] be happier than if you do something
[L1168] [55:33.28] you're not passionate about. Because I
[L1169] [55:35.60] think a lot of people I know view their
[L1170] [55:38.80] job as simply a job and life is what
[L1171] [55:42.96] happens between 5:00 pm and 8 am. I
[L1172] [55:46.48] don't feel that way at all. I really
[L1173] [55:48.00] like what I do. Wouldn't matter whether
[L1174] [55:50.88] I made a lot of money or didn't.
[L1175] [55:53.12] >> Awesome. All right. Well, thank you so
[L1176] [55:54.96] much for your time. Really appreciate
[L1177] [55:56.48] it.
[L1178] [55:57.44] >> Thank you for listening to the podcast.
[L1179] [55:59.20] It's a passion project of mine that I've
[L1180] [56:01.44] really enjoyed building. Another passion
[L1181] [56:03.44] project that I've been working on kind
[L1182] [56:04.80] of in secret is building an ergonomic
[L1183] [56:07.28] keyboard that I wish existed and I
[L1184] [56:09.60] finally have a prototype. So, I'd love
[L1185] [56:11.20] to show you what we've built. It's ultra
[L1186] [56:14.08] low profile and ergonomic and I couldn't
[L1187] [56:16.80] find anything like it on the market. So,
[L1188] [56:18.48] that's why we built it. I'll put a link
[L1189] [56:20.24] to the keyboard in the description. You
[L1190] [56:21.92] can take a look and learn more about the
[L1191] [56:23.52] project there. We could definitely use
[L1192] [56:25.12] your support. Also, if you have any
[L1193] [56:27.12] feedback for me about the show, I'd love
[L1194] [56:29.12] to hear it. Comments on YouTube have led
[L1195] [56:31.52] to guests coming on like Ilia Gregoric
[L1196] [56:34.16] and David Fowler. I wasn't aware of them
[L1197] [56:36.56] until someone dropped a comment. Also,
[L1198] [56:38.72] feedback in the comments helped me learn
[L1199] [56:40.24] to reduce the number of cliffhers in the
[L1200] [56:42.80] intros. So, your comments definitely
[L1201] [56:44.64] make a difference. Please keep letting
[L1202] [56:46.08] me know what you'd like to see more of
[L1203] [56:47.68] in the show, and I'll see you in the
[L1204] [56:49.20] next episode.
