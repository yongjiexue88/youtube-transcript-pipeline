# Distinguished Eng: Stack Ranking, Competing with Bezos, Regrets | Bryan Cantrill

Source ID: source-b3da78875be78b52
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Distinguished_Eng_Stack_Ranking,_Competing_with_Bezos,_Regrets_Bryan_Cantrill_en.txt
Video: https://www.youtube.com/watch?v=qhSL-5GtmQM

[L10] [00:00.16] Static ranking is organizational cancer.
[L11] [00:02.80] >> This is Brian Canantril. He was a
[L12] [00:04.72] distinguished engineer at the original
[L13] [00:06.08] Sun Micros Systemystems and I asked him
[L14] [00:08.08] about everything he learned over his
[L15] [00:09.60] 30-year career.
[L16] [00:11.12] >> Performance review is not about you
[L17] [00:13.12] performing better. It's about us
[L18] [00:15.12] measuring your performance.
[L19] [00:16.80] >> He had interesting stories from
[L20] [00:18.24] competing with Jeff Bezos.
[L21] [00:19.76] >> He is not merely a predator. He is an
[L22] [00:21.68] apex predator in capitalism. This is
[L23] [00:23.76] what makes him so good.
[L24] [00:24.64] >> The stories from when he started his own
[L25] [00:26.48] company, Oxide. You go to hang up on a
[L26] [00:28.48] BC, they'll be like, "Wait, wait, wait,
[L27] [00:29.76] wait, wait, wait, wait." I was like,
[L28] [00:30.72] "Oh, okay." And he even let me grill him
[L29] [00:33.20] about his past. He writes this long
[L30] [00:35.20] thing and you reply with just a few
[L31] [00:36.80] words. You say, "Have you ever kissed a
[L32] [00:38.64] girl?" We actually I This is dark, but
[L33] [00:41.68] we Here's the full episode.
[L34] [00:48.72] You know, your career started at Sun
[L35] [00:50.88] Microsystems and that's kind of a
[L36] [00:53.28] legendary company. It was it was before
[L37] [00:54.96] my time. What was the industry like when
[L38] [00:58.48] you first entered it? Was there Fang
[L39] [01:00.96] equivalents at the time? What was Sun
[L40] [01:02.88] Micros Systemystems like? What were the
[L41] [01:04.16] other companies like?
[L42] [01:05.04] >> Yeah, you know, it's kind of funny
[L43] [01:06.48] because there's always been like a Fang
[L44] [01:09.52] kind of equivalent. You know, in the uh
[L45] [01:11.84] in the 60s it was called the bunch. Uh
[L46] [01:14.88] Burroughs, UNIVAC, NCR, Control Data,
[L47] [01:17.04] and Honeywell were were the bunch. It
[L48] [01:19.28] was IBM and the bunch. Um so they for
[L49] [01:22.80] kind of every era there's always you
[L50] [01:25.20] know some hot group some some growing
[L51] [01:27.76] sector um and in my day though so things
[L52] [01:31.52] were I mean I think in a bit of a divot
[L53] [01:33.44] so I graduated in 96 so I was really
[L54] [01:35.52] interviewing in 95 and uh there was uh
[L55] [01:39.28] there was for sure onampus interviews
[L56] [01:41.76] happening um but they um Microsoft was
[L57] [01:46.08] very dominant in that era um and I
[L58] [01:48.40] definitely knew I was not going to go to
[L59] [01:49.76] Microsoft as was a kind of a point of
[L60] [01:51.44] principle. Um,
[L61] [01:53.04] >> why was that?
[L62] [01:54.24] >> Oh, I I view Bill Gates robbed me of my
[L63] [01:56.88] childhood. Microsoft had such garbage. I
[L64] [01:59.20] mean, they really did. Um,
[L65] [02:01.84] >> their operating system was, you know, I
[L66] [02:04.08] I came up in the personal computer era.
[L67] [02:06.24] So, I I came up in the 80s and it wasn't
[L68] [02:10.40] until uh, you know, I I went to to
[L69] [02:13.44] university in 1992. And it wasn't um you
[L70] [02:17.12] know I had just been accustomed to kind
[L71] [02:19.12] of like garbage on the computer and it's
[L72] [02:22.16] like it's garbage in a way that is kind
[L73] [02:24.80] of unfathomable now. DOSs itself the
[L74] [02:27.44] disc operating system from Microsoft had
[L75] [02:30.64] no memory protection whatsoever. So if
[L76] [02:32.96] an application misbehaved the machine
[L77] [02:35.52] would just reboot
[L78] [02:37.12] >> and this is this just became like part
[L79] [02:39.76] of life is like the machines reboot. You
[L80] [02:41.68] got to boy, you got to save your work
[L81] [02:43.28] because you would be in word perfect or
[L82] [02:45.28] word star whatever. This is where I
[L83] [02:46.40] sound like a true like living fossil. I
[L84] [02:48.08] feel like I'm I'm relaying like coming
[L85] [02:50.00] across the Oregon Trail or something.
[L86] [02:51.76] But the you'd be in your word processor,
[L87] [02:54.24] you know, working on your English paper
[L88] [02:55.52] and all of a sudden the machine would
[L89] [02:56.88] reboot and the and that was just that
[L90] [02:59.68] was life and you hope you saved it, hope
[L91] [03:01.52] you had a hard copy. And it was only
[L92] [03:03.76] when I got to college that I realized
[L93] [03:04.96] like wait a minute hold on there's
[L94] [03:06.08] there's actually something called
[L95] [03:07.36] there's memory protection in the
[L96] [03:08.56] microprocessor and for much of my
[L97] [03:11.76] adolescence there had been memory
[L98] [03:13.68] protection present and it DOSs didn't
[L99] [03:16.72] use it at all and the and Windows used
[L100] [03:19.76] it. I mean with Windows it gets
[L101] [03:21.12] complicated but the answer the short
[L102] [03:22.56] answer is Windows didn't use it either.
[L103] [03:24.40] And uh so it wasn't until I I got to
[L104] [03:27.52] like Unix on a workstation and I just
[L105] [03:30.32] remember being like, you know, 18 years
[L106] [03:31.84] old and having like having a a command
[L107] [03:35.60] line shell up in one window, having an
[L108] [03:38.16] FTP to Woo Archive, downloading some
[L109] [03:41.04] like EGA game that I would want to go
[L110] [03:43.44] play back in my dorm in another window,
[L111] [03:45.68] having something else going on in a
[L112] [03:47.44] third window, having it compile in a
[L113] [03:48.96] fourth window, and having this happen
[L114] [03:51.36] magically concurrently was just
[L115] [03:54.48] mindbending. It's like how is this even
[L116] [03:56.88] possible? I mean, again, it it sounds
[L117] [04:00.00] and I I I appreciate how old this
[L118] [04:01.84] sounds, but but this is what it was. And
[L119] [04:04.64] the then looking back, I'm like, why do
[L120] [04:06.72] I have garbage from Microsoft? And it's
[L121] [04:09.84] Microsoft was just not an operating
[L122] [04:12.08] system company. They were the dominant
[L123] [04:13.28] operating system provider, but it but in
[L124] [04:15.68] their DNA, the most fundamental like the
[L125] [04:17.68] nucleotide base pairs of Microsoft are
[L126] [04:20.32] compilers. They were a compiler company,
[L127] [04:22.24] not an operating systems company. And
[L128] [04:24.72] Apple was, you know, Apple, what was
[L129] [04:27.12] Apple at that time? I mean, Apple had,
[L130] [04:28.88] this is long fired Steve Jobs. This is
[L131] [04:30.72] the the the Apple was kind of the the
[L132] [04:33.36] Mac was really honestly not that much
[L133] [04:34.96] better. It was like cleaner, but also
[L134] [04:36.72] didn't make use of memory protection.
[L135] [04:38.88] So, this is just like unconscionable to
[L136] [04:41.20] me. And there was just and this is like
[L137] [04:44.16] aside from all the bad behavior from
[L138] [04:46.48] Microsoft. And there was plenty of bad
[L139] [04:47.84] behavior from Microsoft. Microsoft was
[L140] [04:49.12] very anti-competitive and you know the
[L141] [04:51.12] findings of fact in the Netscape case
[L142] [04:53.20] you know years later would be just very
[L143] [04:56.72] underhanded very wanting to to it was
[L144] [05:00.80] not a company that had the best
[L145] [05:02.64] technology it was a company that that
[L146] [05:04.48] that jockeyed for position and then
[L147] [05:06.88] would kind of abuse its position.
[L148] [05:08.80] >> What's the TLDDR of that that abuse? So
[L149] [05:12.72] what Microsoft would do, and this is a
[L150] [05:15.04] pattern you would see repeated since,
[L151] [05:16.72] but what Microsoft would do is they
[L152] [05:19.20] would announce, you know, you're a
[L153] [05:20.32] promising company that has something
[L154] [05:22.48] that that is that's that's a that's a
[L155] [05:24.88] application that people might use. They
[L156] [05:27.04] would announce that it's going to become
[L157] [05:28.40] a forthcoming feature of the operating
[L158] [05:29.84] system and then but as it turns out then
[L159] [05:32.88] it wouldn't show up. It was vaporware.
[L160] [05:34.48] uh that the term vaporware I think if it
[L161] [05:36.72] if it didn't originate with Microsoft
[L162] [05:38.32] Microsoft definitely perfected the art
[L163] [05:39.84] of vaporware of announcing something
[L164] [05:41.36] didn't that didn't exist and they were
[L165] [05:44.48] kind of dominant with this mediocrity
[L166] [05:46.16] now to their credit they also when they
[L167] [05:49.28] went and so for example Microsoft Word
[L168] [05:51.76] which I mean still exists but Word
[L169] [05:54.80] Perfect was the really the dominant word
[L170] [05:57.12] processor we're perfect and WordStar but
[L171] [05:59.68] Microsoft Word was very bad and to their
[L172] [06:02.48] credit it would get better over time and
[L173] [06:04.80] ultimately supplanted uh were perfect in
[L174] [06:07.84] part because they started bundling it
[L175] [06:09.12] with the operating system. So they they
[L176] [06:11.60] were very deeply anti-competitive and
[L177] [06:13.84] that's not like an opinion that's like a
[L178] [06:15.20] that's like a judicial finding of fact
[L179] [06:17.36] that's a judge also finding of fact. Um
[L180] [06:20.40] and the um and that changed a lot when
[L181] [06:24.40] Gates I mean Gates when he hit middle
[L182] [06:27.92] age that company changed a bunch and
[L183] [06:29.52] after the antitrust case in the late 90s
[L184] [06:31.12] but I was not going to work for
[L185] [06:32.00] Microsoft. I saw in your goodbye post
[L186] [06:36.40] for from Sun Micros Systemystem when you
[L187] [06:38.48] were leaving the company you wrote
[L188] [06:40.08] >> a public post and
[L189] [06:42.00] >> you said that uh you when you joined the
[L190] [06:45.36] company and you interviewed you only
[L191] [06:47.84] knew two things that you one you wanted
[L192] [06:50.56] to work on an operating system kernel
[L193] [06:52.56] development and two is that you didn't
[L194] [06:55.20] particularly want to work for Sun but it
[L195] [06:58.24] looks like you had an amazing time. So
[L196] [07:00.64] what what flipped the switch from going
[L197] [07:02.40] from I don't want to work here to I love
[L198] [07:04.72] working here.
[L199] [07:05.84] >> So the when I I had kind of talked with
[L200] [07:08.48] other groups at Sun and I just like the
[L201] [07:10.32] people I dealt with at Sun were um fine
[L202] [07:13.84] but just not where it didn't feel
[L203] [07:16.00] energizing and uh and certainly PBN did
[L204] [07:19.44] not feel energizing. Um, and you know, I
[L205] [07:22.32] was kind of accustomed to being the
[L206] [07:24.48] youngest person in a group, but you
[L207] [07:26.32] know, you don't want to be completely by
[L208] [07:27.52] your lonesome. You you want to feel like
[L209] [07:29.12] there are other people that have that
[L210] [07:30.16] kind of that same shared passion. And,
[L211] [07:33.52] uh, when I met Kevin Clark and Jeff
[L212] [07:35.60] Bonwick, um, it was like a bolt of
[L213] [07:38.08] lightning. Um those two were um were uh
[L214] [07:41.60] energized, passionate, really they they
[L215] [07:44.16] saw all of the same things that I saw in
[L216] [07:47.12] terms of the potential for operating
[L217] [07:49.44] systems to be innovative and were and
[L218] [07:52.24] wanted to go like rip out broken code
[L219] [07:54.08] and replace it with with beautiful code
[L220] [07:56.00] and all that that same verve um that
[L221] [07:59.52] that I felt. Um and yeah, it was it was
[L222] [08:02.88] absolutely meeting those two. You're
[L223] [08:04.40] just like, "Okay, I I I there are I am
[L224] [08:07.44] gonna work for Sun." I remember actually
[L225] [08:08.64] very vividly coming back from that trip
[L226] [08:10.16] being like, "Oh my god, I'm gonna go
[L227] [08:11.76] work for Sun. If they make that they're
[L228] [08:13.44] going to make me an offer and I'm
[L229] [08:14.48] absolutely going to go work there."
[L230] [08:15.84] >> I saw that eventually you grew to a
[L231] [08:18.24] distinguished engineer there. And what
[L232] [08:20.24] was the career ladder like?
[L233] [08:22.56] >> It would be interesting to know where
[L234] [08:23.76] the kind of member of technical staff,
[L235] [08:25.52] staff engineer, senior staff engineer,
[L236] [08:27.12] distinguished engineer comes from. Um I
[L237] [08:30.32] think it might come from Sun. I think
[L238] [08:31.76] it's possible that Sun is the
[L239] [08:33.12] originating company. It's also possible
[L240] [08:34.88] from Xerox Park. You'd have to kind of
[L241] [08:36.16] take it apart where and I actually
[L242] [08:37.92] remember when uh you know I had
[L243] [08:40.64] interacted with some folks at Sun and
[L244] [08:42.80] they give me a business card and I
[L245] [08:44.64] remember like coming out to Sun being
[L246] [08:46.16] like and not really knowing what my rank
[L247] [08:48.08] was and I'm like I was going to make
[L248] [08:50.08] business cards. I'm like well I'm an
[L249] [08:51.76] engineer and I'm on staff so I like I
[L250] [08:53.28] think I'm a staff engineer. So and and
[L251] [08:55.12] you know I kind of go to make business
[L252] [08:56.16] cards and then I kind of like didn't
[L253] [08:58.00] didn't complete submission on the form
[L254] [08:59.76] or whatever. And then of course it
[L255] [09:01.12] wasn't that long afterwards everybody
[L256] [09:02.32] was like oh wait a minute that was like
[L257] [09:03.84] that would have been like saying I had
[L258] [09:05.20] got tenure like I definitely am not a
[L259] [09:06.56] staff engineer I'm a member of technical
[L260] [09:08.24] staff u I was an MTS3 so the there was
[L261] [09:12.08] the uh you would kind of climb up
[L262] [09:13.92] through those ranks and then to to staff
[L263] [09:16.16] engineer senior staff engineer
[L264] [09:17.28] distinguished engineer
[L265] [09:18.16] >> and three was the start of the
[L266] [09:20.16] >> no I mean I suppose I think it did start
[L267] [09:21.68] at MTS one um no most college hires
[L268] [09:23.76] would start at MTS2 um but they um but I
[L269] [09:27.52] I was an unusual college hire in a lot
[L270] [09:29.76] of ways Interesting. So they brought you
[L271] [09:31.92] on two levels deep as a new grad.
[L272] [09:34.72] >> Yeah. Yeah. Yeah. That's right. Um I
[L273] [09:36.24] mean I'd had a lot I um so was actually
[L274] [09:38.72] not the first company I worked for. I
[L275] [09:39.76] worked for a company called Kunx in
[L276] [09:40.96] Canada. Um and I had done kernel
[L277] [09:42.96] development there. So I had done um OS
[L278] [09:45.28] development at at Kunix for for two
[L279] [09:47.76] summers. Um and done some actually some
[L280] [09:49.60] work that I was that I still think is
[L281] [09:51.44] actually I love that. I love working for
[L282] [09:53.20] Kunix. I love being in Canada. uh and
[L283] [09:55.76] really and and I I had decided that I
[L284] [09:59.04] didn't want to go back to Kunix
[L285] [10:00.80] professionally that I I that I did want
[L286] [10:02.72] the other the other thing I would say is
[L287] [10:03.92] I decided that I wanted to come out of
[L288] [10:05.20] Silicon Valley. I I did not want to be
[L289] [10:07.36] I'd gone to school in the Northeast had
[L290] [10:08.80] worked in Canada but I really wanted to
[L291] [10:09.84] come out of Silicon Valley.
[L292] [10:11.36] >> I see. So then when you when you look at
[L293] [10:13.28] your journey growing from I guess this
[L294] [10:15.84] MTS3 to yeah up to where you grew like
[L295] [10:18.96] if you were to break down that I guess
[L296] [10:21.04] the story behind that growth and kind of
[L297] [10:23.44] >> what are the highlights that that stuck
[L298] [10:25.36] out to you that made you grow?
[L299] [10:27.20] >> Yeah. So I I mean I was not I was very
[L300] [10:31.52] much not focused on my my my grade my
[L301] [10:35.84] rank or promotion. That was not on I was
[L302] [10:39.28] not interested in that. My view was
[L303] [10:41.12] always like I I would much rather be
[L304] [10:43.68] underpromoted than overpromoted. Um I'd
[L305] [10:46.24] much rather be doing work where people
[L306] [10:48.08] are like, "Wait a minute, why is wait
[L307] [10:50.24] why why are you back here? Like what
[L308] [10:52.16] happened to you?" You know, I I I that's
[L309] [10:54.00] just I I am not interested in being kind
[L310] [10:57.44] of doing work performatively. Um I was
[L311] [11:00.40] always going to do what like what I felt
[L312] [11:02.48] was the most important thing to go do.
[L313] [11:04.16] Um and you know, Sun was a company that
[L314] [11:06.40] was very accommodating of headstrong
[L315] [11:08.72] engineers. Uh and um so I um that's what
[L316] [11:12.40] I I what I wanted to do was solve the
[L317] [11:14.48] problems that our customers had, make
[L318] [11:15.92] the operating system what I believed it
[L319] [11:19.28] could be. Kind of realize that vision
[L320] [11:20.96] for what the OS could be. Um Sun was the
[L321] [11:23.44] only company honestly in 1996 that was
[L322] [11:26.64] really invested in the operating system.
[L323] [11:29.04] Every other company was mortgaging its
[L324] [11:30.80] future to Microsoft and Windows and all
[L325] [11:32.32] these computer companies were giving up
[L326] [11:33.76] on their own operating system, giving up
[L327] [11:35.12] on Unix. was really Unix's darkest hour
[L328] [11:37.68] and the being in that group in Solaris
[L329] [11:42.08] kernel development during those years
[L330] [11:43.76] was enormously energizing and allowed us
[L331] [11:46.56] to do all sorts of things and then along
[L332] [11:48.56] the way you get promoted right along the
[L333] [11:50.16] way like promotions were just the kind
[L334] [11:51.92] of thing that that happened as you as
[L335] [11:53.92] you went along the way um the I mean
[L336] [11:56.64] sons I became I learned I would say I I
[L337] [12:00.48] took away a lot of life lessons in terms
[L338] [12:02.56] of of what works and doesn't work um I
[L339] [12:04.96] found that the because of course we had
[L340] [12:08.56] formalized performance review and I
[L341] [12:10.88] found this is like not a deep thought
[L342] [12:12.40] but that formalized performance review
[L343] [12:14.88] never resulted in me having higher
[L344] [12:17.04] performance and this is like this one of
[L345] [12:20.80] these things that you kind of like feels
[L346] [12:22.88] very naive to say because it's like you
[L347] [12:24.88] no dummy like performance review is not
[L348] [12:26.88] about you performing better it's about
[L349] [12:29.52] us measuring your performance it's like
[L350] [12:31.84] well that's not what it should be about
[L351] [12:33.52] what it should be about is like What
[L352] [12:35.12] feedback is great like we should be
[L353] [12:36.80] making everyone be the best that they
[L354] [12:39.12] can possibly be and the the the the
[L355] [12:42.24] formalized the annual cadence of it I
[L356] [12:44.48] felt was very broken you know we would
[L357] [12:46.40] have you submit a self-review of course
[L358] [12:49.84] and then your review is like oh wow my
[L359] [12:51.60] review looks stunningly like my
[L360] [12:53.28] self-review albeit with like grammatical
[L361] [12:55.36] errors introduced uh and you know that
[L362] [12:59.12] and every review um even the reviews in
[L363] [13:02.48] which I was promoted they were not obl
[L364] [13:04.56] lifting like that was not when I look
[L365] [13:06.24] back at the moments of like what were
[L366] [13:08.00] the the the highlights for me during
[L367] [13:10.72] that progression. It was never being
[L368] [13:12.32] promoted. It was always doing a
[L369] [13:14.40] significant body of work or nailing a
[L370] [13:16.72] hard bug or working with someone on
[L371] [13:19.12] something that we thought was
[L372] [13:19.92] impossible. Like that was the stuff that
[L373] [13:21.28] that that was really catalytic for me.
[L374] [13:24.64] Um and then this like son just kind of
[L375] [13:26.72] had to promote me along the way. Now the
[L376] [13:28.96] the one exception though I would say to
[L377] [13:30.40] that is that the the promotion to
[L378] [13:33.20] distinguish engineer is uh was very
[L379] [13:35.52] regrettable and stupid. I mean not my
[L380] [13:37.04] promotion but just in general like the
[L381] [13:38.56] process the process for being promoted
[L382] [13:40.24] at Sun was I would say very traditional
[L383] [13:42.56] in that you know you're taking your
[L384] [13:44.64] folks that are performing very well and
[L385] [13:46.32] you're promoting them up to the next
[L386] [13:47.60] grade. Uh the son did have a very uh
[L387] [13:50.88] kind silly process thing that you know
[L388] [13:53.92] they had three grades they would give
[L389] [13:55.12] you superlative excellent and good and
[L390] [13:57.76] and then I think there was like a you
[L391] [13:59.52] know and like 70% good maybe 20%
[L392] [14:03.92] excellent and 10% superlative something
[L393] [14:05.60] like that and they had this thing where
[L394] [14:07.52] if you were superlative they had to
[L395] [14:10.08] promote you like that was like the index
[L396] [14:11.52] for promoting you like if you got that
[L397] [14:12.80] superlative grade they promote you but
[L398] [14:14.96] also they had to promote you if you they
[L399] [14:16.96] gave you that superlative grade. So you
[L400] [14:18.72] would I had these I had these reviews
[L401] [14:20.48] that were like apologetic being like
[L402] [14:22.08] look I have to give you an excellent
[L403] [14:24.16] grade even though like the work that
[L404] [14:26.40] you've done over this past period has
[L405] [14:29.04] been extraordinary and innovative uh and
[L406] [14:31.84] actually better than the work that you
[L407] [14:33.36] did two years ago or a year ago but I I
[L408] [14:35.76] I can't actually give you the supportive
[L409] [14:37.60] grade because if I give you the
[L410] [14:38.56] supportive grade I would have to promote
[L411] [14:40.00] you and we just promoted you a year ago
[L412] [14:42.08] and it's really like we don't want to
[L413] [14:43.36] promote people any faster than every 18
[L414] [14:44.96] months and you're like okay doesn't make
[L415] [14:47.36] sense. to you. I mean, this isn't like I
[L416] [14:48.80] I was just like, okay, if like if if
[L417] [14:50.96] you're satisfied with this, like
[L418] [14:52.32] fortunately, like I just don't care one
[L419] [14:53.76] way or the other. So, like, sounds good.
[L420] [14:56.08] Okay, can I get back to work now? Are we
[L421] [14:57.68] are we done here? It's like are we and
[L422] [15:00.00] then again trying not to be trolled by
[L423] [15:01.92] the grammatical reviews in my in in in
[L424] [15:04.08] the review that's being handed to me.
[L425] [15:05.76] Um, so now the difference for that was
[L426] [15:08.96] the and you know the promotion of staff
[L427] [15:10.96] engineers was a big deal and like great
[L428] [15:13.12] fine. Actually, it was funny because all
[L429] [15:15.36] the staff had so Sun had this thing
[L430] [15:17.28] called KEEP, the key employee incentive
[L431] [15:19.36] program and Keep was effectively like an
[L432] [15:22.72] annual dividend. It was like a bonus.
[L433] [15:24.48] So, you know, and there was like a keep
[L434] [15:26.88] pool that was set across the company and
[L435] [15:30.08] you know kind of a traditional thing,
[L436] [15:31.36] right? And the the metric was based on
[L437] [15:33.84] like company performance. That's what
[L438] [15:35.36] they and so I did hear when I was, you
[L439] [15:38.00] know, in MTS3, MTS4, the staff engineers
[L440] [15:40.56] like, you know, they would get their
[L441] [15:41.52] keep bonus and if the keep bonus is
[L442] [15:43.04] really good, they take everyone out to
[L443] [15:44.16] dinner and it was kind of like, you
[L444] [15:45.36] know, it was like being at the the
[L445] [15:46.64] mining town, right? When there's a big
[L446] [15:48.16] or strike or what have you, gold strike.
[L447] [15:50.24] So I was like, okay, wow, this is like
[L448] [15:51.76] this will be great. So of course, I
[L449] [15:53.36] mean, just like of course, like when do
[L450] [15:55.12] I get promoted to staff engineer? It
[L451] [15:56.40] must have been in like 20201. I get
[L452] [15:58.72] promoted to staff engineer as like the
[L453] [16:01.12] dotcom nuclear bomb goes off and the
[L454] [16:04.08] keep bonus was ne I never got like keep
[L455] [16:07.36] bonus was zero from then on out. Sun
[L456] [16:09.20] lost 98% of its value in the public
[L457] [16:11.12] markets and like I never so it's a good
[L458] [16:14.00] thing that I wasn't doing it for the
[L459] [16:15.12] keep bonus because the keep bonus was
[L460] [16:16.56] was zero. Um but then getting so that
[L461] [16:20.00] was staff engineer, senior staff
[L462] [16:21.28] engineer and then distinguished engineer
[L463] [16:22.96] is was really unfortunate in that there
[L464] [16:25.68] were uh there were kind of uh two paths
[L465] [16:27.92] in to distinguish engineer and this may
[L466] [16:29.68] be true of of a lot of companies. I
[L467] [16:30.96] don't know. I mean I we don't have ranks
[L468] [16:33.04] at oxide for this reason. Like I think
[L469] [16:34.40] ranks are corrosive. I don't think they
[L470] [16:36.24] get people to do their best work. I'm
[L471] [16:37.52] not interested in them. Um but the um at
[L472] [16:41.20] Sun there were two ways to be a
[L473] [16:42.88] distinguished engineer. One was of
[L474] [16:44.00] course to be like promoted from a senior
[L475] [16:45.36] staff engineer to a distinguished
[L476] [16:46.56] engineer and uh that was a very very I
[L477] [16:50.88] mean I would say rigorous but it's
[L478] [16:52.00] giving it far too much credit. It was
[L479] [16:53.36] very political process. the dees would
[L480] [16:55.68] vote on whether you should be admitted
[L481] [16:58.32] to this country club of distinguished
[L482] [16:59.92] engineers which is a terrible idea
[L483] [17:01.92] putting like this is like the wrong
[L484] [17:03.60] place for democracy in a society right
[L485] [17:05.92] the for so many different reasons and
[L486] [17:08.88] the but so that's how you would get
[L487] [17:10.24] promoted to distinguish engineer very
[L488] [17:11.84] hard to get promoted the other way to
[L489] [17:13.60] become a distinguished engineer is son
[L490] [17:15.76] is buying your little company is aqua
[L491] [17:18.32] hiring your company and your the
[L492] [17:21.12] company's got just enough leverage
[L493] [17:22.64] during that process to be like oh by the
[L494] [17:24.24] our CTO needs to be a DE. So you would
[L495] [17:26.56] have these like dees just kind of like
[L496] [17:28.00] pop in the side. You're like, who is
[L497] [17:30.16] this? Like, oh yeah, we then we acquired
[L498] [17:32.72] their company. So, and and there was
[L499] [17:34.96] definitely a difference in like you you
[L500] [17:36.88] knew the the homegrown dees versus the
[L501] [17:39.36] ones that had been had been aqua hired
[L502] [17:41.52] in. Um, but when I and I actually like
[L503] [17:44.48] and this is like I just do not want to
[L504] [17:46.24] even think about this process. Like
[L505] [17:47.68] again, I'm not really a political
[L506] [17:48.72] person. Like the last thing I want to
[L507] [17:50.72] do. Uh fortunately we had um I I'd done
[L508] [17:54.24] work that was kind of so indisputable at
[L509] [17:56.32] that point that it was going to be um it
[L510] [17:58.72] was pretty clear that if Sun is going to
[L511] [18:00.72] have such a rank I was probably worthy
[L512] [18:02.00] of it but again I didn't want to deal
[L513] [18:02.96] with it. Uh Sun's CTO at the time Greg
[L514] [18:05.28] Papadopoulos very grateful to Greg. Um
[L515] [18:07.92] Greg had chartered this group that we
[L516] [18:10.32] developed um inside actually in San
[L517] [18:12.24] Francisco first on mission called
[L518] [18:14.00] Fishworks where we had developed a new
[L519] [18:15.68] storage product. uh storage product was
[L520] [18:17.84] going gang busters. Um was a great
[L521] [18:20.24] product. Um although a great product
[L522] [18:22.32] with asterisks on it. Wasn't as great as
[L523] [18:24.00] we thought it was when we shipped it. We
[L524] [18:25.28] learned a lot about it. Um but the
[L525] [18:28.08] product was doing really well. Uh Greg
[L526] [18:30.00] again I was not in the meeting so this
[L527] [18:31.52] was told to me secondhand. Um but uh the
[L528] [18:34.56] your DE case needs to be presented by
[L529] [18:36.96] someone another DE. Well, Greg presented
[L530] [18:39.68] my case and so you had the CTO of the
[L531] [18:42.16] company and some was not a very
[L532] [18:43.44] hierarchal company and Greg was not a
[L533] [18:45.04] very hierarchical person, but Greg put
[L534] [18:47.92] apparently my materials up and it's like
[L535] [18:49.92] I don't expect anyone to vote against
[L536] [18:51.28] this. Take your vote.
[L537] [18:52.80] >> He said that.
[L538] [18:53.44] >> Yeah. And apparently it was unanimous.
[L539] [18:54.96] So I was like, "Thank you, Greg." Um,
[L540] [18:56.64] deeply appreciative. So Greg, I didn't
[L541] [18:58.40] have to deal with that because
[L542] [19:00.00] uh Greg was dealing with it for me. Um,
[L543] [19:01.84] and it was kind of like, you know,
[L544] [19:02.96] honestly, it was kind of a validation of
[L545] [19:04.16] my hypothesis. Like Greg honestly viewed
[L546] [19:06.08] it more of a reflection on the company
[L547] [19:07.44] than a reflection on me. It's like great
[L548] [19:09.36] I had done work that was at some level
[L549] [19:11.20] kind of indisputable and that's kind of
[L550] [19:12.56] the way I had wanted to chart my career.
[L551] [19:14.64] I I think there's two schools of
[L552] [19:15.92] thoughts on on you know how people
[L553] [19:17.60] structure their careers within these I
[L554] [19:19.28] guess ladders. If a really ambitious new
[L555] [19:23.12] graduate engineer comes to you and they
[L556] [19:24.72] say hey I want to be a distinguished
[L557] [19:26.48] engineer one day I have two ideas. One
[L558] [19:30.16] idea is I'm going to just focus on the
[L559] [19:33.60] work and just you know promotions will
[L560] [19:36.24] be a byproduct or I'm going to do the
[L561] [19:39.44] other thing where you know I talk to my
[L562] [19:41.36] manager I'm like hey how do I get to
[L563] [19:42.80] that next level and hey what are those
[L564] [19:44.80] things that the next level needs to do
[L565] [19:47.12] and then I will do work that molds to
[L566] [19:50.64] that mold.
[L567] [19:52.00] >> Yeah I would try to steer someone to a
[L568] [19:54.08] third path. What's the third path? like
[L569] [19:56.16] what why why do you want to be what what
[L570] [19:57.76] does it why do you want to be
[L571] [19:58.80] distinguished engineer because if that's
[L572] [20:01.28] the goal if the goal is to be a
[L573] [20:02.96] distinguished engineer you get there be
[L574] [20:05.20] a distinguished engineer now what I I
[L575] [20:08.08] mean do you like you know you you can be
[L576] [20:11.44] so fixated on that it's like it doesn't
[L577] [20:14.80] at some level it doesn't that doesn't
[L578] [20:17.60] actually that's not the thing that
[L579] [20:19.04] matters that's that doesn't give you
[L580] [20:21.44] meaning and to me if I had a young
[L581] [20:23.68] engineer it's like I'm I want to be a
[L582] [20:25.12] distinguished engineer. I'm like, that's
[L583] [20:26.40] a recipe for a midlife crisis. So, let's
[L584] [20:29.52] try to dial you differently. And I think
[L585] [20:32.32] that what I think what you would what I
[L586] [20:34.56] would steer someone to is what what's
[L587] [20:37.36] get you on a path that has meaning where
[L588] [20:40.64] you're going to be developing and what
[L589] [20:43.12] drives meaning for you? What's important
[L590] [20:45.28] to you? And it's like, well, what's
[L591] [20:47.04] what's important to me is to be a
[L592] [20:48.08] distinguished be like, okay, well, I
[L593] [20:50.24] mean, you'd want to tease it apart. Get
[L594] [20:51.76] them on the couch a little bit. Like,
[L595] [20:53.04] why I mean, are you not were you not
[L596] [20:54.16] loved enough as a child? like what's
[L597] [20:55.36] going on like you
[L598] [20:57.28] and and you know kind of work through
[L599] [20:59.20] some of these issues because you don't
[L600] [21:01.12] want to be dependent on that kind of
[L601] [21:03.12] external validation
[L602] [21:05.20] you I would want to be like let me
[L603] [21:06.96] introduce you to people who have
[L604] [21:08.24] achieved what you are putitively setting
[L605] [21:10.64] out as your goal and are miserable like
[L606] [21:13.44] let me introduce you to some miserable
[L607] [21:14.80] dees you want to be wealthy let me
[L608] [21:16.40] introduce you to some miserable wealthy
[L609] [21:18.00] people so you know that it's like that's
[L610] [21:21.52] that can't be it it's there's got to be
[L611] [21:24.72] something else that that is that the
[L612] [21:27.60] fuel in that furnace and like let's go
[L613] [21:29.68] find that thing and and and then we then
[L614] [21:32.88] like the promotions will happen and the
[L615] [21:34.56] work will happen okay but let's say okay
[L616] [21:37.36] mentee comes to you and says you have a
[L617] [21:40.24] good point I want financial independence
[L618] [21:42.88] a lot of people I think want that is
[L619] [21:44.80] they they want to
[L620] [21:46.48] >> yeah what's financial independence
[L621] [21:47.68] though because like we are in such a
[L622] [21:49.52] well-compensated domain it's like you
[L623] [21:51.60] and I right now could go out and get a
[L624] [21:54.72] cup of coffee that is the best cup of
[L625] [21:57.68] coffee in the We're in San Francisco.
[L626] [21:58.88] We're in the mission. We can get some
[L627] [22:00.48] coffee that is like some Ethiopian
[L628] [22:02.08] coffee, some amazing coffee that is like
[L629] [22:04.88] the And that is attainable to you and me
[L630] [22:08.00] and and to basically everyone else. It's
[L631] [22:10.96] like a $6 cup of coffee,
[L632] [22:13.20] >> right?
[L633] [22:13.84] >> Yeah. Yeah. Well, okay. Well, let's say
[L634] [22:15.84] you define it as you don't need to work
[L635] [22:18.40] for money ever again. But then what?
[L636] [22:21.84] This is like, okay, you don't need to
[L637] [22:22.72] work for money ever again. Like, okay, I
[L638] [22:24.32] get that, but but so you can go off and
[L639] [22:26.72] do the thing that actually motivates
[L640] [22:27.76] you. Well, then go off and do the thing
[L641] [22:28.88] that actually motivates you. But what if
[L642] [22:30.64] it doesn't make money?
[L643] [22:31.68] >> Well, I think and I this is where I you
[L644] [22:34.32] want to take it apart. And so like you
[L645] [22:36.48] want to find a way I mean certainly
[L646] [22:37.92] you're going to have things like the the
[L647] [22:40.32] the the difference that you want to
[L648] [22:42.40] make, the meaning that you're going to
[L649] [22:43.68] find is going to be something that's
[L650] [22:45.52] like, yeah, this is this is just not a
[L651] [22:47.12] career path at all. like I can't
[L652] [22:48.64] actually sustain myself at all. So then
[L653] [22:50.72] you need to find a way to balance that I
[L654] [22:52.88] would say with your career and you want
[L655] [22:55.12] to keep that balance. I think I also
[L656] [22:56.56] think it's a mistake to be like I'm
[L657] [22:57.92] going to achieve financial independence
[L658] [22:59.28] and then I'm going to do the thing that
[L659] [23:00.64] is meaningful to me. It's like and again
[L660] [23:03.04] you just and I I definitely had the
[L661] [23:05.76] blessing of know most people were like
[L662] [23:08.56] me made a lot of money on paper in the
[L663] [23:11.84] dot boom and just lost every penny of
[L664] [23:13.92] it. I mean, I had a I had a lost carry
[L665] [23:15.92] forward for so many years that I
[L666] [23:18.16] actually like one year I lost track of
[L667] [23:19.92] my lost carry forward. Oh my god, I just
[L668] [23:21.92] So, but I had a lost carry forward. I
[L669] [23:23.92] that and I was, you know, I had like
[L670] [23:25.44] fond memories of the do bubble when I
[L671] [23:27.04] would take my whatever it was $3,000 a
[L672] [23:28.96] year against my from a lost carry
[L673] [23:30.72] forward. Um the that was most people
[L674] [23:33.12] around here. Most people kind of like
[L675] [23:36.16] lost it all but also were fine. I think
[L676] [23:39.36] this is the other thing like the.com
[L677] [23:40.56] bust was super helpful because if you
[L678] [23:43.36] had geared yourself to be really
[L679] [23:45.68] economically motivated in 99 2000 98 99
[L680] [23:49.76] 2000 which would have been easy 2001
[L681] [23:52.24] 2002 2003 like you that was not why you
[L682] [23:54.72] were here because this place was nuclear
[L683] [23:58.00] winter and and you had to had to find
[L684] [24:01.84] something else and I I knew like so the
[L685] [24:04.56] funny thing I knew like lots of people
[L686] [24:05.92] that like had to remind themselves why
[L687] [24:09.20] they got in this and it wasn't money. I
[L688] [24:11.04] also knew people I did know people that
[L689] [24:12.88] made a bunch of money in the do boom.
[L690] [24:14.64] The people that made a bunch of money in
[L691] [24:15.84] the do boom weren't that interested in
[L692] [24:17.76] tech to begin with. So when it went up
[L693] [24:20.88] in you know late9 2000 they're like I'm
[L694] [24:24.00] selling at all like I actually don't
[L695] [24:25.52] want to do this and those people and
[L696] [24:28.96] there are a couple of them that I knew
[L697] [24:30.24] and some of them really really struggled
[L698] [24:32.80] in the next decade because they didn't
[L699] [24:34.24] have to work for the rest of their lives
[L700] [24:35.84] but now what? like you don't have to
[L701] [24:38.08] work. So like now what do you do? And
[L702] [24:39.28] and they were on their own search for
[L703] [24:42.00] meaning and like not easy. And going
[L704] [24:44.08] through periods of like oh like I'll buy
[L705] [24:45.68] six houses. Then you realize that like
[L706] [24:47.68] six houses are kind of like a pain in
[L707] [24:49.36] the ass. It's like you and I could go
[L708] [24:51.12] drink six cups of coffee concurrently.
[L709] [24:53.28] You're just like what am I doing here?
[L710] [24:54.48] Am I just like proving that I can buy
[L711] [24:55.92] six cups? It's like why do I want six
[L712] [24:57.44] houses? Then then you you scale that way
[L713] [25:00.40] back. I mean, it gives you like it it
[L714] [25:02.80] really opens your eyes about what
[L715] [25:04.72] matters and what doesn't matter. What
[L716] [25:07.44] doesn't matter as much. Certainly, you
[L717] [25:09.28] need to be able to provide for yourself
[L718] [25:10.80] and provide for for a family. You want
[L719] [25:12.96] to be able to raise a family and so on.
[L720] [25:15.28] So, you want to be able to have that,
[L721] [25:16.96] but you want to do that in a way that's
[L722] [25:18.08] honestly sustainable. I think that that
[L723] [25:19.84] too many folks are focused on like I'm
[L724] [25:21.28] going to do this so I can leave. It's
[L725] [25:22.56] like then maybe you shouldn't be in this
[L726] [25:24.16] industry at like go do something go do
[L727] [25:25.68] the thing you would do when you left and
[L728] [25:27.60] find a way to do that in a way like and
[L729] [25:30.48] and go pursue that dream and cuz you'll
[L730] [25:33.52] be you'll be happier. You'll you'll have
[L731] [25:35.84] meaning doing that. Quit your job at
[L732] [25:38.32] Meta and become a podcaster, you know.
[L733] [25:40.08] >> Oh, well, I did. [laughter] Yeah. Yeah.
[L734] [25:43.36] Well, um yeah, it's it's uh it's
[L735] [25:46.24] interesting you say that because there's
[L736] [25:47.76] this um there's this subreddit, this
[L737] [25:50.24] community that's all about uh financial
[L738] [25:52.64] independence, earning enough, and
[L739] [25:54.56] >> Jesus,
[L740] [25:54.88] >> I'll see a very regular post that says,
[L741] [25:58.80] "Guys, I did it
[L742] [26:00.64] >> and I don't know what to do now."
[L743] [26:02.19] [laughter]
[L744] [26:03.44] >> Yeah.
[L745] [26:04.40] >> Yeah. I did it. I did. And also like I
[L746] [26:06.48] gear I mean I think this is like this is
[L747] [26:08.08] a problem by the way in engineering, not
[L748] [26:09.76] even in the Even when the goal is has
[L749] [26:13.52] meaning, this is a problem. This is what
[L750] [26:14.80] I this is what I call postpartum
[L751] [26:16.40] engineering. When you are really focused
[L752] [26:18.48] on shipping something and you're just
[L753] [26:20.32] like shipping this thing is just the
[L754] [26:22.32] lens through which you're doing
[L755] [26:23.52] everything. And when we shipped our
[L756] [26:25.12] first racket oxide, I was very concerned
[L757] [26:27.36] about like we are going to have
[L758] [26:28.48] postpartum and there are going to be
[L759] [26:30.24] people who are like I was working so
[L760] [26:32.00] hard and pulling so hard for so long and
[L761] [26:34.32] now we shipped it and like now what? And
[L762] [26:36.16] I'm I so even when the thing you've done
[L763] [26:38.64] is obviously meaningful and you've
[L764] [26:40.48] achieved something extraordinary, you're
[L765] [26:42.08] going to have that when the thing you've
[L766] [26:43.92] also achieved is like well I can like
[L767] [26:46.48] buy any cup of coffee I want. It's like
[L768] [26:48.16] the thing I want like now I'm not even
[L769] [26:49.52] like I got like what am I supposed to
[L770] [26:52.16] it's just easy to see how you people be
[L771] [26:56.64] wondering
[L772] [26:58.32] of it really is. And then there are some
[L773] [26:59.68] people that just like snip all the wires
[L774] [27:01.60] and they're like, "Well, the meaning of
[L775] [27:02.48] it is to get even more." And then just
[L776] [27:03.92] like, you know, then you get like Larry
[L777] [27:05.92] Ellison or whatever. But like that's
[L778] [27:07.76] also not something that people should
[L779] [27:08.80] aspire to,
[L780] [27:09.52] >> right? I I Well, what would you say? Cuz
[L781] [27:12.00] I I do know someone who is genuinely
[L782] [27:15.12] happy just doing nothing. By doing
[L783] [27:18.96] nothing, I just mean like uh relaxing in
[L784] [27:22.00] bed, you know, watching their shows, you
[L785] [27:24.40] know, going to hanging out with friends
[L786] [27:26.40] and stuff. I mean,
[L787] [27:27.52] >> I think if they had the billion dollars,
[L788] [27:28.64] they just do that every day.
[L789] [27:30.32] >> Yeah.
[L790] [27:30.72] >> But what you said doesn't work in that
[L791] [27:33.20] case cuz that doesn't earn anything.
[L792] [27:36.00] >> I, you know, I actually did know a guy I
[L793] [27:38.00] knew a guy who I actually did know a guy
[L794] [27:39.36] who did this who as I'm thinking about
[L795] [27:41.36] people who made money in the com. I knew
[L796] [27:43.12] one of uh I I believe one of Yahoo's
[L797] [27:46.88] like first employees, but not because he
[L798] [27:49.52] was like crazy sharp or anything because
[L799] [27:51.76] he like they they wanted to hire a web
[L800] [27:54.08] surfer and he was like a pthead who's
[L801] [27:56.88] like this like this sounds like the
[L802] [27:59.04] level of work that I'm a so he gets a
[L803] [28:01.28] job as like a web surfer one at Yahoo
[L804] [28:03.52] but as like employee number like single
[L805] [28:05.36] digit. He gets the equity grant as part
[L806] [28:08.40] of like joining the company, never gets
[L807] [28:10.32] another equity grant, but makes a king's
[L808] [28:13.20] ransom because he's very early at Yahoo,
[L809] [28:16.24] never promoted above like web server
[L810] [28:18.32] rank one or whatever, and was
[L811] [28:20.00] complaining to everybody about how much
[L812] [28:21.60] his job sucked. And it was like, you
[L813] [28:23.60] surf the web for a living. Like you've
[L814] [28:26.08] somehow managed to like win this insane
[L815] [28:28.72] lottery where you're getting paid to do
[L816] [28:30.88] like very close to nothing. And he like
[L817] [28:32.80] at when it started he owned like all of
[L818] [28:35.12] Yahoo in terms of like surfing because
[L819] [28:36.72] the way Yahoo worked you you may be
[L820] [28:38.24] wondering what the hell I talk about.
[L821] [28:39.60] Yahoo was a curated directory of links.
[L822] [28:42.32] This is again where I sound like
[L823] [28:43.52] >> pre Google
[L824] [28:44.64] >> very much pre Google. This is like pre
[L825] [28:46.40] Google. This is not just pre Google.
[L826] [28:47.76] This is like pre-locost preh hotbot
[L827] [28:49.92] pre-lta vista. This is this is like
[L828] [28:52.56] basically pre the ability to search the
[L829] [28:55.12] internet. you would have these curated
[L830] [28:57.76] directory of links and someone needs to
[L831] [29:00.48] go like find this content and it was
[L832] [29:02.40] like this guy Yahoo employee number six
[L833] [29:04.40] or whatever he was and so he originally
[L834] [29:06.64] like owned the entire directory but he's
[L835] [29:08.32] like not very good and not very
[L836] [29:09.52] energetic it was like you know stoned
[L837] [29:11.52] all the time so they kind of like carved
[L838] [29:13.60] and so finally he I I believe at the end
[L839] [29:15.92] before he finally quit he owned only
[L840] [29:18.08] like snowboarding in Northern California
[L841] [29:21.12] that's what it was his like
[L842] [29:22.24] responsibility to it's like this is a
[L843] [29:25.04] job And so that is the kind of person
[L844] [29:27.76] who was and you would like to think that
[L845] [29:29.28] that he found something that was
[L846] [29:30.72] actually meaningful to him but clearly
[L847] [29:32.08] it was not the work or work for that
[L848] [29:34.00] matter
[L849] [29:34.40] >> right um you said earlier there were
[L850] [29:36.96] these ratings there was superlative
[L851] [29:39.76] excellent
[L852] [29:41.60] >> I noticed you didn't mention there's
[L853] [29:43.44] there's a bad rating
[L854] [29:44.72] >> right there was a yeah no there was not
[L855] [29:48.08] basically not sun did not um the the
[L856] [29:52.16] idea of like a pip or the the whole like
[L857] [29:54.80] rank and yang which is what Intel
[L858] [29:56.40] famously did. Um the um rank and yank
[L859] [30:00.00] >> rank and yank was was stack ranking and
[L860] [30:02.88] it was it was their name for stack
[L861] [30:04.16] ranking. Yeah. Was rank and yank. Um
[L862] [30:06.64] yeah stack stack ranking is
[L863] [30:08.56] organizational cancer. It is it is very
[L864] [30:10.80] very very bad news when you especially
[L865] [30:13.04] if you are going to terminate a bottom
[L866] [30:15.52] end percent that is um that's death. I I
[L867] [30:18.72] I really think that is just a a wall
[L868] [30:20.80] to-wall terrible idea because you've
[L869] [30:22.48] incentivized people to have dead weight
[L870] [30:24.40] on their teams. Um that they can that
[L871] [30:26.64] >> Oh, is that Oh, so they have
[L872] [30:28.88] >> that they got someone to throw into the
[L873] [30:30.32] wood chipper?
[L874] [30:31.28] >> Oh, wait. So, you think that a manager
[L875] [30:33.52] strategically keeping around?
[L876] [30:35.60] >> Oh, I know. So, I mean that definitely
[L877] [30:36.96] happened at Sun for sure. Oh, yeah. For
[L878] [30:38.96] sure. I mean, there were people that
[L879] [30:39.84] were like, why are they still here?
[L880] [30:41.68] Like, they don't they don't not seem to
[L881] [30:43.12] be doing anything. And someone kind of
[L882] [30:44.56] took me aside and like yeah that person
[L883] [30:46.48] is in your best interest because like do
[L884] [30:48.96] you know what that person's rating is?
[L885] [30:50.24] It is always like good like they they
[L886] [30:53.60] get a good so you can be an excellent or
[L887] [30:55.52] a superlative. And I'm again I'm like
[L888] [30:57.04] does this make sense to you? Like why
[L889] [30:58.40] are we okay? So no all sorts of perverse
[L890] [31:02.32] incentives all sorts of perverse
[L891] [31:03.92] incentives with with stack ranking and
[L892] [31:05.52] stack ranking fundamentally you that
[L893] [31:08.56] stack ranking teaches you that your team
[L894] [31:10.56] are adversaries and that's a bad idea
[L895] [31:14.40] that is and it's just not the way I want
[L896] [31:15.84] to operate like the the my big belief is
[L897] [31:18.88] that that teams do extraordinary things
[L898] [31:23.20] and that everybody should want to be
[L899] [31:25.60] serving the team. It is it is the team
[L900] [31:28.64] that wins or loses, the team that
[L901] [31:30.80] succeeds. And I I think that stack
[L902] [31:33.12] ranking really operates very much
[L903] [31:35.04] contrary to that.
[L904] [31:36.48] >> You mentioned that Sun I mean the stock
[L905] [31:40.24] price went down by 98%.
[L906] [31:42.48] >> Yeah. Trading below our cash at one
[L907] [31:44.48] point.
[L908] [31:45.04] >> So I mean was there not some management
[L909] [31:47.28] at some point saying hey we got to it's
[L910] [31:49.52] time to I mean
[L911] [31:51.68] >> mass layoffs.
[L912] [31:52.48] >> Oh no no no. Sun did I mean Sun resisted
[L913] [31:55.60] layoffs for a little while. Scott was
[L914] [31:57.52] kind of famously did not McNeely
[L915] [31:59.12] famously did not want to lay people off
[L916] [32:00.32] but that which was a mistake. He waited
[L917] [32:01.68] too long for that. Um but no once the
[L918] [32:03.84] layoffs started I mean I think at one
[L919] [32:05.52] point I counted the the number of
[L920] [32:08.24] layoffs that had the rounds of layoffs
[L921] [32:10.40] was like 35 layoffs. 35 rounds of
[L922] [32:12.56] layoffs over like eight years.
[L923] [32:14.80] >> That's I mean it's more than for a year.
[L924] [32:16.80] >> Oh yeah. Absolutely. Yeah. No, it was it
[L925] [32:18.64] was brutal.
[L926] [32:19.36] >> That's that's insane.
[L927] [32:20.32] >> And you get these like small layoffs,
[L928] [32:21.84] big layoffs. I mean this was actually
[L929] [32:23.44] before the warrant act I think. Um but
[L930] [32:25.92] you would get we actually I mean this is
[L931] [32:27.52] dark but we you could you could uh uh
[L932] [32:32.40] there was an API effectively to the
[L933] [32:35.52] although this is like before the era of
[L934] [32:37.52] rest APIs but there was a way to get the
[L935] [32:40.80] employee directory programmatically and
[L936] [32:42.96] so we would run what we called the obits
[L937] [32:45.44] and the obits would run every day and
[L938] [32:47.44] would tell you who was no longer at the
[L939] [32:48.88] company and so you would see these small
[L940] [32:51.12] layoffs that were not actually like you
[L941] [32:53.20] you would see you know a group that was
[L942] [32:54.48] let go or you would see and then you
[L943] [32:56.48] would see like oh my god like that's
[L944] [32:57.92] 1500 people or that's 3,000 in today's
[L945] [32:59.76] obits.
[L946] [33:01.20] >> Was the company aware that you had that
[L947] [33:03.52] access to that data?
[L948] [33:06.72] >> Sun you son's strength and weakness was
[L949] [33:09.84] that no one was truly in charge. So um I
[L950] [33:12.64] mean I think it would not have been it
[L951] [33:15.04] would not have been surprising. Um but
[L952] [33:18.16] um I mean Sun to its credit um was a
[L953] [33:20.24] pretty transparent company. So I don't
[L954] [33:21.92] think that we would have I think that we
[L955] [33:24.40] weren't violating any kind of policy. We
[L956] [33:26.40] were accessing a we were accessing the
[L957] [33:27.84] org tool which was the tool they had to
[L958] [33:30.00] show you kind of organizational layout.
[L959] [33:31.28] So we weren't doing anything unourred.
[L960] [33:33.28] Um but it was a way for us to know like
[L961] [33:35.60] what's happening in the company as the
[L962] [33:37.60] so no it was layoff after layoff after
[L963] [33:39.28] layoff after layoff after layoff.
[L964] [33:40.88] >> That I mean 35 layoffs that's it almost
[L965] [33:44.32] yeah it's crazy. I um
[L966] [33:46.00] >> but that was everybody too. again that
[L967] [33:47.92] was not like
[L968] [33:49.36] >> like oh I mean the it is hard to express
[L969] [33:54.08] the period from the.com bust um when you
[L970] [33:57.36] know kind of pets.com creators in in the
[L971] [33:59.76] spring of 2000 the there kind of ran on
[L972] [34:03.20] on momentum until the end of 2000 and at
[L973] [34:06.64] the end of 2000 the dotcom bubble truly
[L974] [34:08.48] truly burst for everybody um for son
[L975] [34:11.04] included um and then uh and 911 did not
[L976] [34:14.48] help right so uh what And the economy
[L977] [34:17.68] was tech was basically dead for 5 years.
[L978] [34:21.92] Um and and Y cominator is formed kind of
[L979] [34:25.28] at that Y cominator is I think 2006.
[L980] [34:29.04] >> I see.
[L981] [34:29.68] >> Um and starts to form I think in part
[L982] [34:32.80] because I think to get Graham's
[L983] [34:35.36] perspective on this but the uh I mean
[L984] [34:38.48] there was a there was a capital deficit
[L985] [34:41.36] at that point. There were like people
[L986] [34:42.56] that could solve interesting things and
[L987] [34:44.00] there was like no way to start a company
[L988] [34:45.52] to go do it. Um, so the it was really
[L989] [34:48.56] really bleak here for many many years.
[L990] [34:50.40] >> I see. Slightly off topic, but I I was
[L991] [34:53.28] stalking your Twitter and I saw that
[L992] [34:55.04] Paul Graham had blocked you.
[L993] [34:56.96] >> Do you know is
[L994] [34:58.24] >> uh Paul Graham blocked me. He did block
[L995] [34:59.76] me. I think he un Yeah, that was a point
[L996] [35:01.36] of pride. That did felt like I really
[L997] [35:03.20] arrived when Paul Graham blocked me.
[L998] [35:04.72] Yeah, Paul Graham blocked me. Yeah, I
[L999] [35:06.00] definitely feel like I'm I'm on the
[L1000] [35:06.88] right side of history on that one. Um,
[L1001] [35:08.80] >> well, what do you think that was for?
[L1002] [35:10.32] Uh, no. I know what that was for. Um,
[L1003] [35:12.32] that was for um I think that uh Paul
[L1004] [35:14.80] Graham was uh defending some of the
[L1005] [35:17.36] worst behavior of Richard Stallman. And
[L1006] [35:18.80] the worst behavior of Richard Stallman
[L1007] [35:20.08] does not age very well. It's truly truly
[L1008] [35:22.96] uh some pretty gross kind of behavior.
[L1009] [35:25.36] Uh and he was defending that and I was
[L1010] [35:27.60] attacking him for it and he was blocking
[L1011] [35:29.04] me for that. So like all right, I'll
[L1012] [35:31.36] take that. Um yeah, I mean Paul Graham
[L1013] [35:34.00] is complicated for me. he uh and there
[L1014] [35:36.08] and there are a couple people like this
[L1015] [35:37.36] in Silicon Valley that are complicated
[L1016] [35:39.12] in that there are uh says some things
[L1017] [35:41.92] that I really strongly agree with and
[L1018] [35:44.24] some things that I really strongly
[L1019] [35:46.32] disagree with um often in the same
[L1020] [35:48.48] sentence. so often and you're just like
[L1021] [35:50.96] my brain's getting zapped like okay this
[L1022] [35:52.88] is like wrong but also not wrong and uh
[L1023] [35:56.00] so um yeah he's he's a complicated one
[L1024] [35:58.40] there a couple people like that
[L1025] [36:00.40] >> I understand that Sun Micros
[L1026] [36:01.92] systemystems was eventually acquired by
[L1027] [36:04.00] Oracle
[L1028] [36:04.80] >> invaded yeah
[L1029] [36:05.84] >> and uh I just want to know why was it so
[L1030] [36:09.12] controversial at the time there's even a
[L1031] [36:10.48] Wikipedia page that says the acquisition
[L1032] [36:13.44] of Sun Micros systemystems and there's
[L1033] [36:15.60] it's almost like an obituary and there's
[L1034] [36:18.08] >> a lot
[L1035] [36:19.04] you know, top level engineers who
[L1036] [36:20.88] >> um well, it was uh it was dramatic. Um
[L1037] [36:24.64] there's actually a really interesting
[L1038] [36:26.16] SEC filing because it's a public
[L1039] [36:27.36] company. Um that IBM and HP were both
[L1040] [36:29.92] jockeying to try to buy Sun and each was
[L1041] [36:32.64] trying to sabotage the other and each
[L1042] [36:35.20] was trying to get the kind they're
[L1043] [36:37.44] because they almost wanted to buy Sun
[L1044] [36:40.08] punitively. They were both competitors
[L1045] [36:41.76] with Sun. Um and while they were kind of
[L1046] [36:44.96] screwing with one another, uh Oracle
[L1047] [36:46.80] swept in and bought the company. Um so
[L1048] [36:49.68] um Oracle that happened really quickly.
[L1049] [36:53.36] Um the actual acquisition itself was
[L1050] [36:55.20] necessarily controversial. It took a
[L1051] [36:56.32] while to close. Um what I mean to to the
[L1052] [37:00.08] contrary I mean there's nothing like
[L1053] [37:01.20] really controversial about Oracle
[L1054] [37:03.20] because Oracle is what it is. Um Oracle
[L1055] [37:05.92] is just there's not a lot of depth to
[L1056] [37:08.40] Oracle. Um, Oracle is just an octopus
[L1057] [37:10.80] that knows how to feed itself. And the
[L1058] [37:14.00] um the Sun was very much not that way.
[L1059] [37:17.92] Sun was there was there was a level I
[L1060] [37:19.76] wouldn't call it purism, but there was
[L1061] [37:22.08] Sun was always endeavoring to do the
[L1062] [37:25.36] right thing by its customers. Sun was
[L1063] [37:27.76] endeavoring to to solve hard interesting
[L1064] [37:29.92] technical problems that had commercial
[L1065] [37:32.88] relevance. And it gave its engineers, us
[L1066] [37:36.96] tremendous freedom to go do so. And and
[L1067] [37:40.24] it tended to attract people that wanted
[L1068] [37:43.44] to to do that that wanted to do that was
[L1069] [37:46.48] wanted to be bold and uh it was it was a
[L1070] [37:49.68] great place for that reason because it
[L1071] [37:51.20] rewarded that kind of technical
[L1072] [37:52.40] boldness. So that's why you know NFS and
[L1073] [37:55.36] Spark and Java and and Saras and then
[L1074] [37:58.00] all the technologies that I worked on
[L1075] [37:59.20] you know all these things came out of
[L1076] [38:00.72] Sun. There were so many of these like
[L1077] [38:01.84] seminal technologies that came out of
[L1078] [38:03.44] Sun because of of of that kind of that
[L1079] [38:05.92] passion and independence. Oracle doesn't
[L1080] [38:07.28] have any of that. Oracle is just like
[L1081] [38:09.20] Oracle truly is is focused on really on
[L1082] [38:13.28] on one thing namely its own
[L1083] [38:15.12] profitability which is like I I thought
[L1084] [38:17.36] when the acquisition happened I'm like
[L1085] [38:18.48] well this will be interesting because
[L1086] [38:19.28] we'll get someone with like great
[L1087] [38:20.72] business savvy maybe. One of the things
[L1088] [38:22.56] that was frustrating to me about Sun is
[L1089] [38:24.16] that Sun um on terms of business
[L1090] [38:26.56] execution, Sun fell down a bunch of
[L1091] [38:28.80] times and I thought we would have
[L1092] [38:30.32] someone in Oracle that would be just
[L1093] [38:31.68] better at the execution of a commercial
[L1094] [38:34.00] enterprise. Uh as it turns out, I was
[L1095] [38:36.08] really overestimating Oracle. Um Oracle
[L1096] [38:38.80] really is about um being able to to get
[L1097] [38:42.64] effectively a monopoly, a natural
[L1098] [38:44.40] monopoly over its own customers,
[L1099] [38:46.88] esphixxiating competition and then
[L1100] [38:48.88] raising the rent on its customers. like
[L1101] [38:50.80] that is really what Oracle wanted to go
[L1102] [38:53.60] do. Um, and it's not a company I wanted
[L1103] [38:56.00] to work for.
[L1104] [38:57.12] >> I see. Because I there's a talk that you
[L1105] [39:00.24] gave that where you really uh I mean,
[L1106] [39:02.64] >> you know, I didn't even Yeah, I know
[L1107] [39:03.92] you're talking.
[L1108] [39:04.56] >> The talk is the Lisa talk from 2011.
[L1109] [39:07.84] >> Yeah. Before you even got to talking
[L1110] [39:10.40] about it, you said, "I'm going to try
[L1111] [39:12.64] and make it through this slide without
[L1112] [39:14.16] crying."
[L1113] [39:15.04] >> Oh, that was on the the slide
[L1114] [39:16.88] >> before. Yeah. Yeah. And then I think you
[L1115] [39:19.44] were talking about Oracle and you said
[L1116] [39:21.20] that they screw customers and lie. I
[L1117] [39:23.84] guess you explained the screw customers
[L1118] [39:26.16] part, but what's the live part of
[L1119] [39:29.60] >> of Oracle?
[L1120] [39:30.56] >> Yeah, Oracle is um has made many
[L1121] [39:34.56] promises to its own customers that it
[L1122] [39:36.16] does not keep. Oracle does not has not
[L1123] [39:38.00] earned the trust of its customers. If
[L1124] [39:39.52] you ask customers, do you trust Oracle?
[L1125] [39:41.04] The answer to that would be no. And I
[L1126] [39:42.88] would kind of let that speak for itself.
[L1127] [39:44.24] Um the yeah the making that slide
[L1128] [39:46.16] without crying bit was not about Oracle.
[L1129] [39:47.84] That was about very much about Sun. Um
[L1130] [39:50.00] and that was the and the the
[L1131] [39:53.52] Scott McNeely's
[L1132] [39:55.44] epitap for Sun. Kicked butt, had fun,
[L1133] [39:58.08] didn't cheat, loved our customers,
[L1134] [39:59.52] changed computing forever.
[L1135] [40:00.32] >> Yeah, you said that. Yeah.
[L1136] [40:01.20] >> Yeah. That was the bit that and like it
[L1137] [40:03.12] still chokes me up a little bit just
[L1138] [40:04.80] because it it's true. It was true. And
[L1139] [40:08.88] we um when we started Oxide, it's like
[L1140] [40:12.08] adopted that as our own mission because
[L1141] [40:14.48] that that's exactly what we wanted to go
[L1142] [40:16.08] do at Oxide. Um and I thought was a very
[L1143] [40:18.96] uh concise distillation of that and that
[L1144] [40:20.96] was just not Oracle. Oracle was not
[L1145] [40:22.32] interested in that.
[L1146] [40:23.12] >> Um
[L1147] [40:23.68] >> when when a lot of the top engineer it
[L1148] [40:25.60] seems like there was a an exodus big
[L1149] [40:28.24] >> where people confiding with each other
[L1150] [40:30.48] like were you talking to other highle
[L1151] [40:32.24] engineers say hey we got to get out of
[L1152] [40:33.76] here.
[L1153] [40:34.48] >> Oh. Oh yeah. I mean, it's not even like
[L1154] [40:36.88] I mean, you're just like you're in a
[L1155] [40:38.16] burning building. Are people confiding
[L1156] [40:39.52] with one another that they should leave
[L1157] [40:40.48] the burning building? It's like, no,
[L1158] [40:41.52] actually, people are just like running
[L1159] [40:42.64] for their lives. I mean, you're just not
[L1160] [40:44.32] like, "Oh, what do you think of the
[L1161] [40:45.44] burning building? Like, do you think the
[L1162] [40:46.64] building is burning? What do you uh" And
[L1163] [40:49.44] no, I mean, it was pretty clear. And
[L1164] [40:51.44] there were actually the real true
[L1165] [40:54.40] jockeying came from those engineers
[L1166] [40:58.32] before it actually closed. There were
[L1167] [41:00.40] going to be some engineers that would be
[L1168] [41:01.84] laid off before it closed. But as the
[L1169] [41:06.08] acquisition closed, in other words,
[L1170] [41:06.96] there were some people that were some
[L1171] [41:08.08] employees that were not going to be
[L1172] [41:09.12] Oracle employees.
[L1173] [41:10.40] >> Uh Aqua laid off. Like they wouldn't
[L1174] [41:12.96] there wouldn't be a a existing company.
[L1175] [41:15.12] They just
[L1176] [41:16.08] >> That's right. So So they would they
[L1177] [41:17.60] would lose their job.
[L1178] [41:18.48] >> Okay. Okay.
[L1179] [41:18.96] >> But they would get like a pretty rich
[L1180] [41:20.72] severance package. So you had like an
[L1181] [41:23.60] absolute line at the trough for how can
[L1182] [41:25.92] I get laid off? You [laughter] like I
[L1183] [41:28.16] lay me off first. Um this was not me.
[L1184] [41:30.40] This was not us. We were I I was I mean
[L1185] [41:33.68] in many I mean at least to the credit of
[L1186] [41:35.52] the like the people lining up at the
[L1187] [41:36.56] trough at least they knew what was going
[L1188] [41:37.92] to happen. Uh [snorts] and there's still
[L1189] [41:39.44] people to this day that are a little
[L1190] [41:40.56] resentful of people like that guy that
[L1191] [41:42.96] guy got laid off and I I mean I quit
[L1192] [41:45.28] because I could not work there in good
[L1193] [41:47.04] conscience after 45 days that guy got
[L1194] [41:49.36] laid off and got a year of salary or
[L1195] [41:50.88] whatever it was. Um but we no I um I was
[L1196] [41:54.72] not that I was we were at this Fishworks
[L1197] [41:57.12] group in San Francisco and I was really
[L1198] [41:58.48] optimistic that really optimistic
[L1199] [42:00.72] somewhat optimistic um that we could
[L1200] [42:02.80] combine the best of both companies or
[L1201] [42:04.24] what I perceived to be the best of both
[L1202] [42:05.68] companies and as turns out that's not
[L1203] [42:07.36] the case. So
[L1204] [42:08.24] >> what did you see cuz you left really
[L1205] [42:10.32] quick so what see that
[L1206] [42:12.16] >> oh it was really clear to me that that
[L1207] [42:14.56] this was a very very different company.
[L1208] [42:16.24] I mean, Oracle gave me like I had
[L1209] [42:18.16] decided like I can't work here anymore.
[L1210] [42:20.88] And the time between I decided that and
[L1211] [42:24.00] I actually left which was only like 30
[L1212] [42:26.00] days more a little longer than that
[L1213] [42:28.32] maybe 45 days. Um Oracle gave me like
[L1214] [42:31.12] four other reasons to be like oh my god
[L1215] [42:33.28] I just can't I can't stomach working
[L1216] [42:35.68] here. I mean I and I mean it was a bunch
[L1217] [42:37.68] of things. One it was Sun for all of its
[L1218] [42:40.80] faults and there were many many faults
[L1219] [42:42.32] of Sun. Sun had the trust of its
[L1220] [42:45.04] customers. Our customers actually were
[L1221] [42:47.52] rooting for us at Sun. Our customers
[L1222] [42:50.24] wanted us to prevail. Why? Because they
[L1223] [42:52.24] we actually they they trusted us and
[L1224] [42:54.56] they even when it wasn't in our own best
[L1225] [42:56.64] interests like we would we would be
[L1226] [42:59.36] straight with our customers and I think
[L1227] [43:01.04] that that was we did not lie to our
[L1228] [43:02.88] customers, right? And that was something
[L1229] [43:04.64] that our customers found very very
[L1230] [43:06.32] appealing. That was not Oracle. Oracle
[L1231] [43:08.64] does not have the trust of its
[L1232] [43:09.68] customers. And I realized something very
[L1233] [43:12.40] important about myself. I can't work for
[L1234] [43:14.40] a company that has that kind of profound
[L1235] [43:17.04] distrust. I mean, in terms of like we're
[L1236] [43:18.48] talking about meaning, that so eroded my
[L1237] [43:20.80] own sense of meaning. I felt ashamed. I
[L1238] [43:23.20] felt ashamed to work there. And I had
[L1239] [43:25.68] never felt that. I've never, you know,
[L1240] [43:28.96] for Sun I was embarrassed from time to
[L1241] [43:31.12] time, but never ashamed. And with
[L1242] [43:33.28] Oracle, I was ashamed.
[L1243] [43:34.96] >> Uh, you mentioned people were were eager
[L1244] [43:37.12] to get themselves laid off.
[L1245] [43:39.52] >> How do you even u How do you even do
[L1246] [43:41.60] that? It's just like,
[L1247] [43:42.32] >> oh, you tell your manager, look, if
[L1248] [43:43.44] there's a list, put me on it.
[L1249] [43:45.36] >> Okay.
[L1250] [43:45.60] >> Yeah. Oh, there is a list. Okay. Who
[L1251] [43:46.96] else is on it? Like, I want to be on it.
[L1252] [43:48.24] I mean, it's like all the ways that you
[L1253] [43:50.16] I mean, it's not like you don't fill out
[L1254] [43:51.52] a web form. I mean, you're obviously
[L1255] [43:53.20] like, you know, you're you're a courtier
[L1256] [43:55.68] kind of whispering about trying to
[L1257] [43:57.04] figure out like what's the scuttlebutt
[L1258] [43:58.96] who's going to get laid off.
[L1259] [44:00.32] >> I thought you'd have to like really, you
[L1260] [44:02.24] know, underperform and like
[L1261] [44:03.68] >> No, no, no, no. No, no. I I think that
[L1262] [44:05.68] they were No, it was all about like,
[L1263] [44:07.28] hey, I I'm I I have no value to Oracle.
[L1264] [44:10.08] could you? I mean, it was much more like
[L1265] [44:11.47] [laughter] Oracle's not interested in
[L1266] [44:12.48] what I'm doing, right? And then you get
[L1267] [44:13.44] like Oracle is interested. You're like,
[L1268] [44:14.72] "Oh, god damn it."
[L1269] [44:17.92] >> Um, [snorts]
[L1270] [44:19.44] uh, so, okay, so I I get why you left
[L1271] [44:21.44] Oracle and and obviously Sun was
[L1272] [44:23.52] acquired. Yeah. And so, the next place
[L1273] [44:25.28] you worked at was, uh, Joyant. Yeah. And
[L1274] [44:28.24] >> I understand that this company competed
[L1275] [44:31.20] with AWS.
[L1276] [44:32.48] >> That's right. Yeah.
[L1277] [44:33.28] >> And, uh, I listened to some of the
[L1278] [44:35.84] conversation you already had and you had
[L1279] [44:37.76] interesting quote. You said Bezos is the
[L1280] [44:40.64] apex predator of capitalism.
[L1281] [44:42.72] >> Yeah.
[L1282] [44:43.60] >> What makes you say that?
[L1283] [44:44.80] >> Very they're just Amazon was Amazon at
[L1284] [44:47.76] its height was such so relentless on
[L1285] [44:51.52] execution and what made Bezos really
[L1286] [44:55.36] really good is that and and I would say
[L1287] [44:57.84] like and when I say its height I mean
[L1288] [44:59.92] they Amazon hits the mother lode and
[L1289] [45:02.32] they they hit the mother lode not
[L1290] [45:04.32] because they're lucky. they there's like
[L1291] [45:06.24] luck involved, you know, they they allow
[L1292] [45:08.80] S3 to be developed, right? They develop
[L1293] [45:11.12] EC2, then they they realize what they're
[L1294] [45:13.60] on to and they're on to cloud computing
[L1295] [45:16.32] before anyone has figured it out. And
[L1296] [45:18.48] the the the the the reinvents in like
[L1297] [45:22.16] from 2010 to say 2015
[L1298] [45:26.72] were relentless. Every reinvent was a
[L1299] [45:29.04] price cut. It was price cut and it was a
[L1300] [45:31.60] bunch of new services. And if you're a
[L1301] [45:33.76] customer, you're like, "This is awesome.
[L1302] [45:35.52] I love this. This is great. Like, why
[L1303] [45:37.84] would I not?" I mean, so it was so And
[L1304] [45:39.84] that's what I mean by the Apex Predator
[L1305] [45:41.12] because he was on something that was
[L1306] [45:43.60] wildly profitable.
[L1307] [45:45.68] He pulled off a just an absolute move of
[L1308] [45:50.00] moves in that Amazon did not break out
[L1309] [45:53.28] their revenue. So, it's just like
[L1310] [45:55.36] Amazon, it's like you got the dot side,
[L1311] [45:57.76] you have AWS, they're not breaking out
[L1312] [45:59.28] any of that. They're just like literally
[L1313] [46:00.24] like this is how much Amazon's making.
[L1314] [46:01.92] analysts would ask in the call, they're
[L1315] [46:03.12] just like, "Yeah, we're not talking
[L1316] [46:03.92] about that." And which apparently you
[L1317] [46:05.44] can get away with as a public company.
[L1318] [46:07.28] Um, and so they actually created this
[L1319] [46:09.36] idea, especially with the relentless
[L1320] [46:11.04] price cuts, people are like, "Oh, the
[L1321] [46:12.64] cloud's a terrible business." Like no
[L1322] [46:14.16] one no one should get into the cloud
[L1323] [46:15.68] because it's a terrible business. And so
[L1324] [46:18.88] people didn't and meanwhile like what we
[L1325] [46:20.64] knew because we did compete with Amazon.
[L1326] [46:22.16] We did have a public cloud and we knew
[L1327] [46:23.92] it's like no the actual the margins on
[L1328] [46:25.76] this thing are great like this is
[L1329] [46:27.92] actually a great business and Amazon and
[L1330] [46:31.68] Amazon is executing very very very very
[L1331] [46:35.44] well and they did extraordinarily well
[L1332] [46:37.20] in the in in those years and I mean they
[L1333] [46:39.28] are still obviously it's a it's a it's a
[L1334] [46:41.20] very profitable company but they have
[L1335] [46:42.72] Amazon has is not what it was in in
[L1336] [46:46.24] those years. Um, I not sure when the
[L1337] [46:49.52] last price cut was announced at
[L1338] [46:50.80] reinvent, but it's been a while. Um, it
[L1339] [46:53.20] is not that that's not what you get at
[L1340] [46:54.80] reinvent. You don't get the kind of the
[L1341] [46:56.56] new services that you can't live
[L1342] [46:57.68] without. Um, so it's it's a different
[L1343] [46:59.60] company.
[L1344] [47:00.48] >> AWS was was early and they already had,
[L1345] [47:05.04] I guess, a dominant market share.
[L1346] [47:06.72] >> Yeah.
[L1347] [47:07.20] >> Why would Jeff Bezos continue to just
[L1348] [47:09.84] like ruthlessly keep going and keep
[L1349] [47:12.32] going
[L1350] [47:13.52] >> instead of milking it, you know?
[L1351] [47:14.56] >> Because he is not merely a predator. He
[L1352] [47:16.48] is an apex predator in capitalism. This
[L1353] [47:18.72] is what makes him so good. He's like,
[L1354] [47:19.84] I'm not gonna no like I'm gonna I'm
[L1355] [47:21.52] gonna press my advantage.
[L1356] [47:23.84] Like I'm I'm gonna make it so no one can
[L1357] [47:25.92] compete with me and I'm going to make it
[L1358] [47:28.16] so no one wants to get into this
[L1359] [47:30.00] business and I'm going to do it honestly
[L1360] [47:32.00] like the right way. I'm going to do it
[L1361] [47:33.44] by like giving a great product at a
[L1362] [47:36.24] reasonable price. It's like damn. Yeah,
[L1363] [47:38.80] that's that's good. That's like that's
[L1364] [47:40.32] how that's a win-win. That's a win-win.
[L1365] [47:42.16] It was like essential for innovation
[L1366] [47:44.16] during that era of companies that were
[L1367] [47:45.84] cloud-born. Uh and it I mean it was
[L1368] [47:48.32] really and it was very very hard to
[L1369] [47:50.24] compete with Amazon. I'll tell you that
[L1370] [47:51.44] you had to you had to really like find a
[L1371] [47:53.76] lane and you know we we found lanes
[L1372] [47:56.00] where we could go compete with Amazon
[L1373] [47:57.52] but it was uh it was it was brutal. They
[L1374] [47:59.92] their their execution was extraordinary
[L1375] [48:03.28] >> at this company. I I saw that you you
[L1376] [48:05.92] started out as a VP and you transitioned
[L1377] [48:07.68] to CTO at some point and
[L1378] [48:09.60] >> yeah,
[L1379] [48:10.32] >> what's the difference in the roles?
[L1380] [48:13.04] >> That's a great question. I actually gave
[L1381] [48:14.48] a talk on this with joint CTO at the
[L1382] [48:16.72] time on the contrast between BP of
[L1383] [48:18.24] engineering and CTO. Um and you know,
[L1384] [48:21.12] I'm not sure how much I how much I buy
[L1385] [48:24.64] the difference now. I mean, I think both
[L1386] [48:26.32] in both capacities, you're serving as an
[L1387] [48:28.32] engineering leader. Um and I I think
[L1388] [48:30.96] that you you know I guess you can argue
[L1389] [48:32.48] that a CTO is more outward looking for
[L1390] [48:34.24] sure. Chief travel officer is kind of
[L1391] [48:36.08] the the porative for it. You're on the
[L1392] [48:37.92] road talking to customers a lot. Um you
[L1393] [48:40.08] you are um a VP of engineering may be
[L1394] [48:42.96] more focused on some of of the necessary
[L1395] [48:45.44] like mechanics that you have in an
[L1396] [48:47.68] engineering organization. Um for me
[L1397] [48:50.56] personally I mean they brought me in as
[L1398] [48:52.32] a VP of engineering because they frankly
[L1399] [48:53.92] already had a CTO. So I mean like I
[L1400] [48:55.52] again it's just like the the grade I was
[L1401] [48:57.92] at uh at Sun I didn't particularly care.
[L1402] [49:00.64] What I did care about is when the you
[L1403] [49:03.20] know CTO had left and then another CT
[L1404] [49:05.44] that we had CTO who had been a founder
[L1405] [49:07.44] of the company and when he left uh so
[L1406] [49:09.36] there was kind of like the the empty CTO
[L1407] [49:12.56] position. I didn't care. What I did care
[L1408] [49:15.68] was that we didn't hire externally for
[L1409] [49:18.08] that because I so that I did care about
[L1410] [49:20.56] a lot about like look if there's going
[L1411] [49:21.84] to be a CTO I'm happy to be the VP of
[L1412] [49:23.92] engineering in perpetuity but like I I
[L1413] [49:26.16] would rather like if there's going to be
[L1414] [49:27.84] a CTO I would like to not hire
[L1415] [49:29.60] externally for that please or let me be
[L1416] [49:31.44] involved in that anyway but um yeah I
[L1417] [49:32.96] was later the CTO
[L1418] [49:34.08] >> and why not hire externally?
[L1419] [49:35.68] >> I just didn't want to deal with like
[L1420] [49:36.88] having to bring in I didn't need that
[L1421] [49:38.56] that's not what we needed at that time.
[L1422] [49:40.24] what what we needed um at at that time
[L1423] [49:42.96] especially well we had we gott rid of
[L1424] [49:45.12] the CEO um and we we really were um we
[L1425] [49:49.84] needed a really a terrific CEO which we
[L1426] [49:53.04] which we later got so
[L1427] [49:54.96] >> and so then you started Oxide
[L1428] [49:56.96] >> started Oxide in 2019. Yeah.
[L1429] [49:58.48] >> And what's the story behind you starting
[L1430] [50:00.40] your own company? Well, I knew again I I
[L1431] [50:03.84] kind of had in my my mind that like I
[L1432] [50:07.04] want to start a company and the thing
[L1433] [50:08.72] that I knew is I want to start a company
[L1434] [50:10.56] with Steve. Um Steve and I had worked
[L1435] [50:12.32] together at that point for I mean I
[L1436] [50:14.64] Steve was the uh when when I went to
[L1437] [50:17.04] join I had not talked to Steve prior to
[L1438] [50:18.96] going to join and I was going to join in
[L1439] [50:20.56] part because I was running away from
[L1440] [50:21.84] Oracle and it was a I it was going to
[L1441] [50:24.72] allow me to to hire folks and so on. Um,
[L1442] [50:27.84] but the I didn't talk to Steve until
[L1443] [50:29.84] after I came to join and I'm like this
[L1444] [50:31.52] guy is amazing and uh Steve and I just
[L1445] [50:35.28] worked very closely together. Steve came
[L1446] [50:36.88] up on the go to market side on the sales
[L1447] [50:38.40] side and um I knew I'm like I definitely
[L1448] [50:41.92] want to start a company with this guy. I
[L1449] [50:43.76] and and he fortunately he felt the same.
[L1450] [50:45.44] So we we both felt like all right
[L1451] [50:47.84] whatever we do next we do it together.
[L1452] [50:49.60] Um and so now it's like all right well
[L1453] [50:52.32] now what? Now we got to figure out what
[L1454] [50:53.84] we want to go do. And we had these long
[L1455] [50:56.80] walks in the city cuz we were work in
[L1456] [51:00.00] San Francisco and we had so many bad
[L1457] [51:02.16] ideas. I mean, it was just it was just
[L1458] [51:03.60] basically one bad idea after another. So
[L1459] [51:05.52] then we're trying to come up with ideas
[L1460] [51:06.80] that like were a better match for the
[L1461] [51:10.00] kinds of things that people would fund.
[L1462] [51:12.96] And we recommend people not do this. Uh
[L1463] [51:15.28] it's understandable. I did it. I don't
[L1464] [51:16.96] understand. But we're we're trying to
[L1465] [51:18.56] like come up with things that people
[L1466] [51:20.24] would fund and coming up with things
[L1467] [51:22.48] that were just like not in our heart.
[L1468] [51:24.32] You know what I mean? Like this is like
[L1469] [51:25.60] okay I could do this but like really I
[L1470] [51:27.44] mean it would be fun to do it with Steve
[L1471] [51:28.72] but just doesn't feel like that's not
[L1472] [51:30.40] going to I want to do something that is
[L1473] [51:32.16] like that is this next long chapter of
[L1474] [51:34.72] my career. And so as we're kind of
[L1475] [51:37.28] struggling with that um and I was trying
[L1476] [51:39.04] to figure out like okay we actually need
[L1477] [51:40.32] to start talking to venture capitalists
[L1478] [51:41.52] at some point. we need to like start
[L1479] [51:43.36] like get this ball rolling and
[L1480] [51:45.04] understand like I and I had always known
[L1481] [51:48.40] venture capitalists and had gotten lunch
[L1482] [51:50.08] with them over the years but had not
[L1483] [51:51.76] really like you know kind of gone deep
[L1484] [51:53.92] and I' known the venture capitalist
[L1485] [51:55.36] associated with with joint for sure um
[L1486] [51:57.92] and so I got uh I was reminding myself
[L1487] [52:00.72] of the email address of one VC in
[L1488] [52:02.48] particular actually a very famous VC and
[L1489] [52:05.04] but it's someone I had known since early
[L1490] [52:07.52] early early early in his career and he
[L1491] [52:08.80] and I had just gotten lunch periodically
[L1492] [52:10.56] through our careers from when he was
[L1493] [52:12.32] first in venture and I was in
[L1494] [52:13.76] engineering and we it's like and he had
[L1495] [52:15.52] kind of become uh become pretty famous
[L1496] [52:17.84] and I was just want to remind myself the
[L1497] [52:19.92] email address and the last email he had
[L1498] [52:21.76] sent to me which is maybe you know 18
[L1499] [52:23.28] months prior was like hey Brian really
[L1500] [52:25.28] enjoyed getting lunch with you today I
[L1501] [52:26.80] just want to remind you I will fund
[L1502] [52:29.20] literally anything you put in front of
[L1503] [52:30.96] me thinking like wow and I was like
[L1504] [52:35.68] Steve you know reminded myself of this
[L1505] [52:38.00] email of this guy's email address he
[L1506] [52:39.84] said he will fund literally anything we
[L1507] [52:43.20] put in front of them. So like we should
[L1508] [52:46.56] just go big. We should do we should do
[L1509] [52:49.12] the thing that is in our heart. And
[L1510] [52:52.08] Steve's like what do you mean? I'm like
[L1511] [52:53.52] we should build the computer that we
[L1512] [52:56.64] want to build. We should build a rack
[L1513] [52:58.80] scale machine. And he's like yeah that'd
[L1514] [53:02.08] be amazing. Like do you think we can get
[L1515] [53:04.80] that funded? And I'm like I yeah I yeah
[L1516] [53:07.28] I think so. And you know that was very
[L1517] [53:10.48] much in our heart. That was what we had
[L1518] [53:13.04] lived that he had lived at Steve had
[L1519] [53:15.20] been at at Dell prior to Joyant. Um he'd
[L1520] [53:18.48] been at Dell for a decade. I'd been at
[L1521] [53:20.32] obviously at Sun for for 14 years. We
[L1522] [53:22.72] and then together at Joyant for another
[L1523] [53:24.80] decade and this is we this was truly in
[L1524] [53:28.80] our marrow. Um and we found like okay
[L1525] [53:32.08] like we can go and we as we started
[L1526] [53:33.44] talking VCs about this about building
[L1527] [53:35.60] and we again envisioned rack scale
[L1528] [53:37.68] design we wanted to do our our our own
[L1529] [53:40.48] board design do our own switch do our DC
[L1530] [53:43.68] bus bar base design do all of our own
[L1531] [53:45.12] software do build the machine that we
[L1532] [53:48.16] ourselves wish we could have had at
[L1533] [53:50.64] Samsung a after Samsung acquired joint
[L1534] [53:53.68] and what was very catalyzing actually
[L1535] [53:55.28] was going to you know you were at at
[L1536] [53:57.12] what would have been Facebook at the
[L1537] [53:58.40] time before they renamed and going to
[L1538] [54:00.24] their open compute going to the open
[L1539] [54:02.08] compute summit and and looking at like
[L1540] [54:04.08] Tyogga Pass and you're like what is this
[L1541] [54:07.12] like Tyogga pass like it I mean it was
[L1542] [54:09.20] like I would liken it to discovering
[L1543] [54:12.00] Unix as an undergrad when I had been
[L1544] [54:14.32] living with DOSs and be like what is
[L1545] [54:16.96] this and you go look at Tyogga Pass
[L1546] [54:18.40] you're like this is a like this is what
[L1547] [54:20.56] a computer can be like this is gorgeous
[L1548] [54:23.44] this is amazing we got to go build this
[L1549] [54:26.40] for the enterprise market and We what we
[L1550] [54:29.60] discovered is this was uh very
[L1551] [54:32.16] contrarian.
[L1552] [54:33.76] Um but things that are contrarian are
[L1553] [54:36.64] attractive to venture. So we would get
[L1554] [54:38.64] this thing where people would actually
[L1555] [54:39.68] be pretty interested in it. Um and I I
[L1556] [54:42.72] mean I don't have to tell you how the
[L1557] [54:43.84] story ends, but we went back we'
[L1558] [54:45.20] actually talked to a bunch of venture
[L1559] [54:46.08] capitalists before I went back to that
[L1560] [54:47.52] same VC that sent me the email and I get
[L1561] [54:51.92] maybe 45 seconds into describing the
[L1562] [54:55.04] problem we want to go solve at Ox. He's
[L1563] [54:56.24] like, "Brian, Brian, stop. Stop. Stop.
[L1564] [54:58.72] If you are talking about starting a
[L1565] [55:00.16] computer company, I want nothing to do
[L1566] [55:01.44] with it." And I'm like, "You know, it's
[L1567] [55:03.68] funny. You sent me an email years ago
[L1568] [55:07.44] that said you would fund literally
[L1569] [55:09.68] anything I put in front of you." And he
[L1570] [55:11.36] said, "Doesn't sound like me." I'm like,
[L1571] [55:13.36] "Well, okay. What do you want me to do
[L1572] [55:14.80] with that one?" Like, you sent me the
[L1573] [55:15.92] email. It's like, is your admin writing
[L1574] [55:17.52] all your emails? I don't You have your
[L1575] [55:19.20] kid write the email? I I don't know what
[L1576] [55:20.40] to do with that one. Like, you didn't
[L1577] [55:21.28] send me the email. Are you calling me a
[L1578] [55:22.48] liar? I mean, and I'm like, "All right,
[L1579] [55:24.00] fine." And it's like, "Fine." And I we
[L1580] [55:25.76] over the phone I go to hang up on him
[L1581] [55:27.20] and of course like VCs this is just like
[L1582] [55:31.12] it's in the animal brain, right? If you
[L1583] [55:33.12] you go to hang up on a VC, they'll be
[L1584] [55:34.56] like, "Wait, wait, wait, wait, wait,
[L1585] [55:35.76] wait." I was like, "Oh, okay." He's
[L1586] [55:37.04] like, "Wait, wait, wait, wait." Cuz I'm
[L1587] [55:38.24] like, "Fine, got it." He's like, "Wait,
[L1588] [55:40.48] wait, wait, wait, wait. I'm not going to
[L1589] [55:42.72] invest." And I'm like, "I know you're
[L1590] [55:43.92] not going to invest." And I knew the
[L1591] [55:44.96] reason I knew he wasn't going to invest
[L1592] [55:46.16] is he's had some big zeros in this
[L1593] [55:48.72] department. And when a VC has had zeros
[L1594] [55:51.52] in something that looks close to what
[L1595] [55:53.20] you're doing, they're like, I want
[L1596] [55:54.24] nothing to do that again. Like, nope,
[L1597] [55:56.16] nope, nope, nope, nope, nope. Was in a
[L1598] [55:57.60] bad relationship with one of those.
[L1599] [55:59.04] Don't want to do that again. And in
[L1600] [56:00.16] part, in their defense, it's often
[L1601] [56:01.52] because like, actually, I understand
[L1602] [56:02.72] this problem a lot better. And now I
[L1603] [56:04.48] understand all of the headwinds. And now
[L1604] [56:07.04] I can I mean in some ways like you need
[L1605] [56:09.44] VCs to be and they need themselves to be
[L1606] [56:12.08] like naive at some level optimistic is a
[L1607] [56:15.20] would be a better way of phrasing it
[L1608] [56:16.32] where they can like envision the world
[L1609] [56:18.64] as it could be as opposed to getting all
[L1610] [56:21.28] mired in the way the world is. You got
[L1611] [56:23.04] to be kind of blind to the odds to a
[L1612] [56:24.72] certain degree. And I knew that he was
[L1613] [56:26.08] not blind to the odds cuz he'd had two
[L1614] [56:27.60] big zeros. And so I knew that he was
[L1615] [56:29.92] going to be like uh and one zero that
[L1616] [56:32.08] like looked a lot like like oxide. Um,
[L1617] [56:35.92] and so he's like, "Look, I'm not going
[L1618] [56:37.20] to find that." I'm like, "Again, I knew
[L1619] [56:38.24] that, but I do want to help you." Like,
[L1620] [56:40.88] "Okay, it's great." And I always tell
[L1621] [56:42.72] people like when you are VCs will ask
[L1622] [56:45.20] this a lot, especially a VC that's like
[L1623] [56:47.44] where you're not a fit for them. You're
[L1624] [56:48.80] not a portfolio fit for them. You're not
[L1625] [56:50.32] a thesis fit, whatever it is. You're not
[L1626] [56:52.00] a stage fit. If they like you, they'll
[L1627] [56:54.40] be like, "Look, I'm not going to invest,
[L1628] [56:56.00] but how can I help?" And you always want
[L1629] [56:57.92] to have an answer to that question of
[L1630] [56:59.36] how you can help. And I had an I I knew
[L1631] [57:00.88] how you could help. I had a very
[L1632] [57:02.08] concrete idea. It's like one of those
[L1633] [57:03.84] zeros. Um, I want to talk to him. I want
[L1634] [57:06.96] to talk to the I want to talk to the
[L1635] [57:08.32] founders. I want to understand
[L1636] [57:09.60] everything that went wrong. And I did.
[L1637] [57:11.76] He's like, "Okay, that I can do." He
[L1638] [57:13.52] made the intro and it was really really
[L1639] [57:16.08] interesting. And like the the mistake
[L1640] [57:17.92] that they that that company had made and
[L1641] [57:20.08] again had a thesis that looked like
[L1642] [57:22.16] Oxide, but they they didn't raise a lot
[L1643] [57:24.40] of c they raised kind of arguably too
[L1644] [57:26.24] little capital. They got something
[L1645] [57:28.00] working that's smaller than what we
[L1646] [57:29.44] built at Oxide. Minimum viable product
[L1647] [57:30.72] at Oxide is a rack. It's big. Took us
[L1648] [57:33.36] three years, three plus years to
[L1649] [57:34.88] develop. They developed something a
[L1650] [57:36.40] little bit faster, but it was much
[L1651] [57:37.44] smaller. It was basically it. You could
[L1652] [57:39.60] view it as like Nitro circa like 2013.
[L1653] [57:42.64] Nitro from the enterprise acquisition at
[L1654] [57:44.48] AWS. Uh does a lot of a lot of really
[L1655] [57:47.28] important offload for AWS. So you could
[L1656] [57:49.60] view it as like very early Nitro, but it
[L1657] [57:52.00] didn't really have a market, but they
[L1658] [57:53.52] had a customer and they got a customer
[L1659] [57:55.52] and they're like great. And the customer
[L1660] [57:57.52] was happy and they wanted to use it in
[L1661] [57:59.04] particular on their active directory
[L1662] [58:00.56] servers. Great, we have product market
[L1663] [58:02.48] fit. Raised a bunch of money, hired a
[L1664] [58:05.20] huge go to market team. Problem is that
[L1665] [58:08.24] customer, huge bank, only wanted to run
[L1666] [58:11.12] it on like their six active directory
[L1667] [58:13.28] servers. So they were going to buy like
[L1668] [58:15.44] quantity six and this is one of the
[L1669] [58:17.52] world's largest banks. And you're like,
[L1670] [58:19.84] uhoh. So you're like, how many world's
[L1671] [58:21.92] largest banks are there? Like well there
[L1672] [58:23.36] like a couple of others, but like we're
[L1673] [58:25.52] going to sell like, you know, two dozen
[L1674] [58:27.04] of these things. like we got to and they
[L1675] [58:29.68] by the time they realized that they had
[L1676] [58:31.20] a lot of mouths to feed on the on the go
[L1677] [58:32.80] to market side and uh they and that
[L1678] [58:36.00] wasn't a zero. It they were acquired but
[L1679] [58:38.64] they were acquired in a way that left
[L1680] [58:41.44] the founder extremely bitter um and
[L1681] [58:44.48] really felt um like he like the VCs had
[L1682] [58:47.60] pumped too much capital in him at the
[L1683] [58:49.12] wrong time had gotten him to do the
[L1684] [58:50.64] wrong thing and was then trapped at the
[L1685] [58:54.08] acquiring company and was really not
[L1686] [58:55.92] happy about it. He was also the one. So
[L1687] [58:57.52] I was describing what we were going to
[L1688] [58:58.56] do at Oxide. He's like that is a suicide
[L1689] [59:00.72] mission. And I just remember writing
[L1690] [59:02.08] down a little notebook almost like
[L1691] [59:03.44] writing down suicide mission. Kind of
[L1692] [59:05.04] underlining it like okay we're on a
[L1693] [59:06.32] suicide mission.
[L1694] [59:07.52] >> That's fun.
[L1695] [59:08.56] >> When I think of rack scale compute
[L1696] [59:11.60] especially these days I I think of racks
[L1697] [59:13.76] of GPUs more than CPUs.
[L1698] [59:16.32] >> Yeah.
[L1699] [59:16.80] >> Is that something that you're building?
[L1700] [59:19.76] >> Yeah. Right. Yeah. a very reasonable
[L1701] [59:21.52] question and when we set out we're like
[L1702] [59:24.16] we I mean again set out in 2019 the
[L1703] [59:27.12] GPGPU is was around obviously and
[L1704] [59:29.44] important but that's not what we were
[L1705] [59:30.64] focused on we were really focused on
[L1706] [59:33.68] general purpose compute general purpose
[L1707] [59:35.52] compute general purpose storage general
[L1708] [59:36.88] purpose networking and our belief had
[L1709] [59:38.08] always been like that's what we actually
[L1710] [59:40.16] want there there is so much to go build
[L1711] [59:43.12] there and go differentiate there and of
[L1712] [59:45.04] course along the way people are like
[L1713] [59:46.00] what about an accelerator like what
[L1714] [59:47.20] about an accelerator GPU and the problem
[L1715] [59:50.32] is that the way we want to build systems
[L1716] [59:52.80] we want to really build systems from
[L1717] [59:54.08] first principles where we have
[L1718] [59:56.72] components that have that have
[L1719] [59:58.48] transparency at that hardware software
[L1720] [59:59.92] interface and we want to write that
[L1721] [01:00:01.52] lowest layer of software we are the
[L1722] [01:00:04.00] company I mean ultimately we're building
[L1723] [01:00:05.12] a hardware software co-design product
[L1724] [01:00:06.96] and in order to be able to do that you
[L1725] [01:00:08.16] need to be able to write very low-level
[L1726] [01:00:10.32] software the problem is that's really
[L1727] [01:00:12.48] not compatible with Nvidia Nvidia is a
[L1728] [01:00:14.32] pretty proprietary company executes well
[L1729] [01:00:16.08] but a very proprietary company and what
[L1730] [01:00:18.16] that meant is there are effectively two
[L1731] [01:00:20.56] doors for Oxide. One is labeled compete
[L1732] [01:00:23.52] with Nvidia and the other is labeled
[L1733] [01:00:25.20] partner with Nvidia. And I didn't want
[L1734] [01:00:26.80] to do either of those things. I have not
[L1735] [01:00:27.92] wanted to do either of those things
[L1736] [01:00:28.96] because I certainly don't want to
[L1737] [01:00:29.84] compete with Nvidia. Um and I think
[L1738] [01:00:32.08] that's getting more plausible now. Um
[L1739] [01:00:34.88] but we can't partner because we just
[L1740] [01:00:36.48] have a very different view of how
[L1741] [01:00:38.88] systems should be built and the Nvidia
[L1742] [01:00:41.68] wants to like their view is like we
[L1743] [01:00:43.12] should own the whole stack. Like forget
[L1744] [01:00:44.48] you whoever you are. Um so like okay
[L1745] [01:00:47.44] that's fine. We're going to be we're
[L1746] [01:00:49.04] going to focus on general purpose CPU.
[L1747] [01:00:50.88] We got plenty to do over here. I think
[L1748] [01:00:52.24] the thing that's been interesting and a
[L1749] [01:00:53.68] bit surprising is that because the GPU
[L1750] [01:00:57.04] landscape is so so cluttered. I mean
[L1751] [01:01:01.84] you've got this very aggressive the very
[L1752] [01:01:04.40] uh executing the well executing company
[L1753] [01:01:06.32] in terms of Nvidia. You've got a lot of
[L1754] [01:01:07.60] competitors around it. Um it's it's a
[L1755] [01:01:10.08] little it's gory right over there to and
[L1756] [01:01:12.96] meanwhile on the general purpose CPU
[L1757] [01:01:14.80] side it's like HP Dell supermarket the
[L1758] [01:01:17.44] same companies that are are doing the
[L1759] [01:01:19.04] same kind of junk honestly that they
[L1760] [01:01:21.52] have been doing and so we are by our
[L1761] [01:01:25.76] lonesomes in terms of a hardware
[L1762] [01:01:27.84] software product over there. So over and
[L1763] [01:01:30.00] over and over again we have had people
[L1764] [01:01:31.68] come to Oxide that we think like no no
[L1765] [01:01:34.40] we're not a fit for you because you like
[L1766] [01:01:36.56] you do a lot of GPU you've got a ton of
[L1767] [01:01:38.56] GPUs like you company famously have a
[L1768] [01:01:40.96] lot of GPUs no no we do have a lot of
[L1769] [01:01:42.64] GPUs we also have a lot of CPU as it
[L1770] [01:01:44.48] turns out because the
[L1771] [01:01:47.84] certainly the emerging AI workloads not
[L1772] [01:01:50.32] just AI workloads but special but
[L1773] [01:01:51.92] certainly AI workloads but high
[L1774] [01:01:53.44] performance computing workloads there's
[L1775] [01:01:54.80] a lot of general purpose CPU that's
[L1776] [01:01:56.64] attached to this special purpose compute
[L1777] [01:01:58.96] you You know, when you're sitting there
[L1778] [01:01:59.84] on chat GPT and it's surfing the web,
[L1779] [01:02:02.56] you got the little spinny saying it's
[L1780] [01:02:03.92] surfing the web. That is not a GPU
[L1781] [01:02:05.28] that's surfing the web. That is a CPU
[L1782] [01:02:06.72] that's surfing the web. And the the CPU
[L1783] [01:02:09.68] is really really important. So for us,
[L1784] [01:02:12.48] we are more focused than ever on the
[L1785] [01:02:14.64] general purpose CPU and there's there is
[L1786] [01:02:17.52] a ton to go do there fortunately to get
[L1787] [01:02:19.60] this product to be where we believe it
[L1788] [01:02:21.68] can be. And I think we will do an
[L1789] [01:02:23.12] accelerator at some point, but um you
[L1790] [01:02:25.36] know, I've been kind of saying it's like
[L1791] [01:02:26.56] 18 months away for a while or 18 months
[L1792] [01:02:28.40] that we would really start thinking
[L1793] [01:02:29.44] about it. And you know, again, I I I
[L1794] [01:02:32.08] know we'll do it in the limit. Um but
[L1795] [01:02:35.20] boy, not in the foreseeable future.
[L1796] [01:02:36.80] We've got a lot to go do as it is.
[L1797] [01:02:38.88] >> I think coming to the end, I I want to
[L1798] [01:02:40.56] ask you some uh career reflections and
[L1799] [01:02:43.12] kind of just all over the place type of
[L1800] [01:02:45.36] questions. You you wrote a tweet a while
[L1801] [01:02:47.92] ago I thought was a really interesting
[L1802] [01:02:49.28] idea which was you you said it would be
[L1803] [01:02:51.84] interesting to have a conference called
[L1804] [01:02:53.60] in retrospect where presenters revisit
[L1805] [01:02:57.04] talks that they've given prior and
[L1806] [01:02:59.36] describe how their her thinking has
[L1807] [01:03:01.52] evolved since and I pulled a bunch of
[L1808] [01:03:04.00] stuff that you've I guess written or
[L1809] [01:03:08.08] said in the past. I'm curious if your
[L1810] [01:03:10.08] perspective has evolved since then. So
[L1811] [01:03:12.16] we'll go through each of those.
[L1812] [01:03:13.60] >> Sure. So first one which is actually
[L1813] [01:03:16.24] really famous as when I saw I kind of
[L1814] [01:03:19.44] did a double take. Um so in in 1996 as a
[L1815] [01:03:24.00] new grad there's this this I don't even
[L1816] [01:03:26.72] know what you use Usenet was. I had to
[L1817] [01:03:29.68] do research actually but there's a guy
[L1818] [01:03:32.00] who he writes this long technical
[L1819] [01:03:33.68] response David S. Miller.
[L1820] [01:03:34.96] >> Yes. And a part of it too it's it's not
[L1821] [01:03:37.76] nice either this I saw there's a line in
[L1822] [01:03:40.16] there. It says Linux is lightweight.
[L1823] [01:03:42.32] Solaris is a pig. which Solaris is what
[L1824] [01:03:44.88] I guess son was.
[L1825] [01:03:45.92] >> Yeah. Yes.
[L1826] [01:03:46.64] >> And then he writes this long thing and
[L1827] [01:03:48.24] you reply with just a few words. You
[L1828] [01:03:50.00] say, "Yeah, have you ever kissed a
[L1829] [01:03:51.76] girl?"
[L1830] [01:03:52.16] >> Yeah.
[L1831] [01:03:53.12] >> Well, first of all, I want to know the
[L1832] [01:03:54.32] context behind it. And then also knowing
[L1833] [01:03:56.16] what you know now.
[L1834] [01:03:56.96] >> Oh, definitely in the regret department
[L1835] [01:03:58.40] if that's what that's asking. Like I've
[L1836] [01:03:59.92] got very few regrets in my career, but
[L1837] [01:04:01.44] like you can put that one like pretty
[L1838] [01:04:02.88] firmly in the regret column. [laughter]
[L1839] [01:04:04.64] Uh yeah. No, that that was that was well
[L1840] [01:04:07.04] and also had no idea that this was going
[L1841] [01:04:11.28] to live in perpetuity that I mean if you
[L1842] [01:04:13.68] could have told me in I think 1997 is
[L1843] [01:04:16.32] maybe when I posted maybe it was 96 it
[L1844] [01:04:18.32] was 96 97 certainly like I'm I'm like 22
[L1845] [01:04:22.00] like I'm I'm very young if you had told
[L1846] [01:04:24.88] me like oh by the way 30 years in the
[L1847] [01:04:27.36] future you're going to be asked about
[L1848] [01:04:29.20] this I'd be like what the hell what like
[L1849] [01:04:32.16] no no trust me it's like the world gets
[L1850] [01:04:34.08] weird you're going to be asked about
[L1851] [01:04:35.28] this. Um I the uh so it was actually a
[L1852] [01:04:39.84] Okay, this is I'm not defending it. I
[L1853] [01:04:41.20] just want to be sure that I want to be
[L1854] [01:04:42.48] clear that like it was a mistake. Um the
[L1855] [01:04:46.00] uh it was actually a reference to a
[L1856] [01:04:47.36] Saturday Night Live sketch. So, there's
[L1857] [01:04:49.44] an SNL sketch that is from an era of
[L1858] [01:04:52.08] Saturday Night Live that it's like you
[L1859] [01:04:53.52] can't even find the video, but they have
[L1860] [01:04:56.56] uh so the um they William Shatner is
[L1861] [01:05:01.20] guest starring on Saturday Night Live
[L1862] [01:05:03.84] and the skit is that William Shatner is
[L1863] [01:05:07.52] at a a Treky convention and the Trekies
[L1864] [01:05:10.48] are asking him all of these questions
[L1865] [01:05:13.52] and they're asking him questions and of
[L1866] [01:05:14.80] course like you know in episode you know
[L1867] [01:05:16.88] this season and this episode you know
[L1868] [01:05:18.32] what what was the combination on the
[L1869] [01:05:20.24] safe? He's like, "What? I don't know
[L1870] [01:05:22.08] that. [clears throat] I don't I don't I
[L1871] [01:05:23.04] don't know that. Why why would I know
[L1872] [01:05:24.16] that? Like I don't that's not even and
[L1873] [01:05:25.60] he's like these two people are kind of
[L1874] [01:05:26.56] arguing themselves." And they're asking
[L1875] [01:05:28.08] him questions that are like this that
[L1876] [01:05:29.36] are all about like the the kind of the
[L1877] [01:05:30.56] cannon of Star Trek. And then he's like,
[L1878] [01:05:32.80] "Hey, can I just say something? Get a
[L1879] [01:05:35.04] life people. You you have you ever
[L1880] [01:05:37.60] kissed a girl?" That was the that was
[L1881] [01:05:39.12] where you know going to a 30 going to
[L1882] [01:05:41.12] John Loveitz when like Vulcaners John
[L1883] [01:05:43.36] Lovevitz do you know? Yeah. Doesn't
[L1884] [01:05:45.60] matter like lost to history. Why am I
[L1885] [01:05:47.52] doing this? and he kind of like looks
[L1886] [01:05:49.04] down at himself and so like it was
[L1887] [01:05:50.96] actually like an obscure Saturday Night
[L1888] [01:05:52.96] Live reference which again like I'm not
[L1889] [01:05:54.72] that doesn't make it any better. Um the
[L1890] [01:05:57.60] uh yeah was that that was that's
[L1891] [01:06:00.00] definitely in the in the the regret
[L1892] [01:06:02.16] department.
[L1893] [01:06:03.68] What did he say back to that or
[L1894] [01:06:06.32] >> Oh, he had a whole lot to say about back
[L1895] [01:06:08.08] to that. And I actually did have a
[L1896] [01:06:09.76] longer post kind of taking apart what he
[L1897] [01:06:13.92] had said about the about like all right
[L1898] [01:06:16.96] like a lot of what you've said here is
[L1899] [01:06:18.32] actually wrong. And so like really going
[L1900] [01:06:20.40] through kind of point by point. I think
[L1901] [01:06:23.44] you know I've actually never t I've
[L1902] [01:06:24.88] never met him never talked about this
[L1903] [01:06:26.48] very talented guy. I think he actually I
[L1904] [01:06:29.44] actually did read I think it was in um
[L1905] [01:06:31.68] the with the Rebel book um about Linux
[L1906] [01:06:34.72] that remember him reading that he's like
[L1907] [01:06:37.92] yeah I kind of like was shooting my
[L1908] [01:06:39.28] mouth off and a son engineer kind of put
[L1909] [01:06:40.80] me in put me back in my place and I'm
[L1910] [01:06:42.88] like man if that is his read on it he's
[L1911] [01:06:44.88] being very generous to me so I'd like to
[L1912] [01:06:46.40] believe that maybe he and I both regret
[L1913] [01:06:47.92] it a little bit we were both like a
[L1914] [01:06:49.28] little you know a little young and
[L1915] [01:06:51.20] excitable um but yeah that was
[L1916] [01:06:53.44] definitely uh that was a life lesson I
[L1917] [01:06:55.76] would say that history forgot about that
[L1918] [01:06:58.08] though.
[L1919] [01:06:58.96] >> So on another tweet
[L1920] [01:07:00.08] >> Yeah. Sorry. Yeah. Here we go.
[L1921] [01:07:01.09] [laughter] This is great. We're This is
[L1922] [01:07:02.64] We're uh This is like the cleanse. Yeah.
[L1923] [01:07:05.44] >> Okay. This is in 2022. You wrote a
[L1924] [01:07:07.20] tweet. You said uh if you're tempted to
[L1925] [01:07:09.52] blame a team for a startup's failure.
[L1926] [01:07:11.68] Please don't. Success is often due to a
[L1927] [01:07:14.64] great team, but failure is almost always
[L1928] [01:07:16.72] due to bad leadership.
[L1929] [01:07:18.48] >> I I wrote that. That's a good [laughter]
[L1930] [01:07:19.44] one. That's a good one. I don't remember
[L1931] [01:07:20.72] writing that.
[L1932] [01:07:21.76] >> That's it. I I agree with that guy. He's
[L1933] [01:07:24.24] he's on I guess the question
[L1934] [01:07:25.76] >> What was I responding to? I would miss
[L1935] [01:07:27.20] something been something that day on the
[L1936] [01:07:28.56] internet or some weather on the internet
[L1937] [01:07:29.92] that I'm subweeting Paul Graham there
[L1938] [01:07:31.76] somewhere. I think that must have been
[L1939] [01:07:33.04] it.
[L1940] [01:07:33.44] >> But um22 I'm curious. Do you think
[L1941] [01:07:35.92] that's true for for Sun? Because Sun
[L1942] [01:07:39.36] >> ultimately failed.
[L1943] [01:07:41.04] >> So okay, I don't agree that Sun failed.
[L1944] [01:07:42.88] I don't agree that Sun failed because
[L1945] [01:07:44.80] Sun again Sun is founded in 1983 and is
[L1946] [01:07:48.48] invaded in in 2008
[L1947] [01:07:52.08] 2009. That's a good run. That's a really
[L1948] [01:07:55.20] good run. Sun was a public company. Sun
[L1949] [01:07:57.76] was in the Fortune 200. Lots of people
[L1950] [01:07:59.76] like kids went to college because their
[L1951] [01:08:02.00] their parents were able to work for Sun.
[L1952] [01:08:04.16] And you got, you know, so I I don't
[L1953] [01:08:05.76] views I do not view Sun as a failure.
[L1954] [01:08:07.44] Sun is like Sun did not I mean arguably
[L1955] [01:08:11.20] did not or not maybe inarguably did not
[L1956] [01:08:14.48] succeed to the scope of its own
[L1957] [01:08:16.72] ambition. But Sun to me is not a
[L1958] [01:08:18.16] failure. Sun is a success. Was its
[L1959] [01:08:20.32] collapse at the end uh I guess
[L1960] [01:08:23.92] changeable in hindsight with different
[L1961] [01:08:25.68] leadership?
[L1962] [01:08:26.32] >> I think so. I think that there were I
[L1963] [01:08:28.16] mean this is a classic power game of
[L1964] [01:08:29.84] like why did Sun ultimately not not
[L1965] [01:08:34.40] survive as an independent entity? Um and
[L1966] [01:08:36.96] why is that? I think there were a bunch
[L1967] [01:08:38.96] of reasons. I think that the I I think
[L1968] [01:08:41.28] that there's a degree to which Sun got
[L1969] [01:08:43.84] very strung out on the very high margins
[L1970] [01:08:46.40] during the dot boom and never quite like
[L1971] [01:08:49.92] got off of that. Never like they we
[L1972] [01:08:52.16] embraced x86 too late. Um we um we kind
[L1973] [01:08:56.32] of thought of ourselves I mean the the
[L1974] [01:08:58.24] company itself became fractured. The
[L1975] [01:08:59.60] layoffs didn't help. I mean I think we
[L1976] [01:09:01.44] at Fish Works where we were developing a
[L1977] [01:09:03.20] storage appliance. I felt that we could
[L1978] [01:09:05.68] have been an example of an exemplar of
[L1979] [01:09:08.72] what the kinds of products I felt Sun
[L1980] [01:09:11.44] could develop an independent Sun could
[L1981] [01:09:13.36] develop, but it was going to be there's
[L1982] [01:09:14.96] a lot of like stuff that needed to be
[L1983] [01:09:16.88] changed for that and you needed
[L1984] [01:09:19.04] leadership that really was very very
[L1985] [01:09:21.44] interested in that. Um, and it's like
[L1986] [01:09:23.36] that just wasn't like that that's not
[L1987] [01:09:25.28] what we had. Um, and in hindsight, it
[L1988] [01:09:28.40] was probably time for a change. But it
[L1989] [01:09:30.40] was, you know, it's like it it kind of
[L1990] [01:09:32.16] the way a a forest fire in in a normal
[L1991] [01:09:35.04] healthy forest fires is is kind of a
[L1992] [01:09:36.96] part of the life cycle of a forest and
[L1993] [01:09:39.68] you need that to have to have to have
[L1994] [01:09:42.16] rebirth and I think that that it's I
[L1995] [01:09:44.72] mean ultimately I think that that um Sun
[L1996] [01:09:48.32] had succeeded but had also run its
[L1997] [01:09:50.32] course and it was it was time for
[L1998] [01:09:52.24] >> I see had its time.
[L1999] [01:09:53.84] >> It had its time. Absolutely had its
[L2000] [01:09:55.20] time. Um, okay. And that next past take
[L2001] [01:09:58.80] of yours you you wrote in 2022.
[L2002] [01:10:01.44] >> Um, perhaps this shouldn't have been
[L2003] [01:10:02.88] surprising, but Musk has absolutely no
[L2004] [01:10:05.36] idea what he's doing. And
[L2005] [01:10:07.28] >> this is about the takeover of Twitter.
[L2006] [01:10:09.20] And I actually don't even know what's
[L2007] [01:10:10.80] going on Twitter because it's private at
[L2008] [01:10:12.16] this.
[L2009] [01:10:12.48] >> Excuse me. I'll I will thank you to not
[L2010] [01:10:14.32] refer to SpaceX that way.
[L2011] [01:10:16.00] >> Oh, right. It has been acquired by XAI
[L2012] [01:10:18.32] and then Xi has been rolled into SpaceX.
[L2013] [01:10:19.84] So like we're now I guess Gwen Shotwell
[L2014] [01:10:22.00] now runs runs Twitter. So I I guess do
[L2015] [01:10:26.24] do you still agree that it's it's run
[L2016] [01:10:28.40] poorly and
[L2017] [01:10:29.04] >> Oh god. Yes. Yes. Yeah. I agree that I
[L2018] [01:10:32.40] mean because Yeah, definitely. It's so I
[L2019] [01:10:34.96] mean
[L2020] [01:10:36.88] Yeah. Yes. Yes. I mean yes. I really I
[L2021] [01:10:40.00] like I literally feel dirty being
[L2022] [01:10:42.00] specific about that. But when I mean
[L2023] [01:10:44.64] when there's a lot of there's rampant
[L2024] [01:10:48.16] bad behavior on Twitter. Um community
[L2025] [01:10:51.28] notes. Yes. Community notes. Great.
[L2026] [01:10:53.92] Everything else pretty much a tire fire.
[L2027] [01:10:56.32] >> What's your number one thing that is
[L2028] [01:10:58.64] tire?
[L2029] [01:10:59.60] >> Um the number one thing of tire is that
[L2030] [01:11:02.16] they the the Oh, we'll tell you this.
[L2031] [01:11:04.16] The reason that we at Oxide don't engage
[L2032] [01:11:06.56] on Twitter. I can't have an Oxide tweet
[L2033] [01:11:08.72] that is sitting next to some of the
[L2034] [01:11:09.92] tweets that I've seen.
[L2035] [01:11:11.60] >> Oh, you you see
[L2036] [01:11:13.28] >> it's like it's like the level of racism.
[L2037] [01:11:15.76] The bluntly I mean crazy racism. Crazy
[L2038] [01:11:21.52] crazy crazy racism, crazy anti-semitism,
[L2039] [01:11:24.64] crazy
[L2040] [01:11:26.40] and crazy the anti-Islam like just crazy
[L2041] [01:11:31.84] hate
[L2042] [01:11:33.76] crazy levels. The kinds of things that
[L2043] [01:11:36.32] you literally could not say and they
[L2044] [01:11:39.68] like, "Oh, it's free speech." It's like,
[L2045] [01:11:40.72] "It's not free speech. It's it's it's so
[L2046] [01:11:42.96] deeply offensive and and reflective.
[L2047] [01:11:46.08] It's like it's so deeply offensive that
[L2048] [01:11:48.80] I don't want my content to be anywhere
[L2049] [01:11:50.80] near it. I don't want someone to be
[L2050] [01:11:52.56] looking at that and looking at my
[L2051] [01:11:54.56] content. I'm sorry. I I'm just not going
[L2052] [01:11:56.56] to do that.
[L2053] [01:11:57.60] >> And you live through a bunch of booms
[L2054] [01:12:00.00] and busts and honestly, I don't even
[L2055] [01:12:02.00] know exactly if we're in a boom or a
[L2056] [01:12:04.24] bust right now. [laughter] There's I
[L2057] [01:12:06.48] mean, AI is going crazy and there's all
[L2058] [01:12:08.32] these layoffs.
[L2059] [01:12:09.20] >> Crazy. Yeah, that's a good point. Yeah.
[L2060] [01:12:10.80] But um what what advice would you give
[L2061] [01:12:13.68] given your experience through the booms
[L2062] [01:12:15.44] and bust for people who are in today's
[L2063] [01:12:17.44] market?
[L2064] [01:12:18.80] >> Yeah. And I would say that some of this
[L2065] [01:12:20.72] I do think is endemic. I mean when I
[L2066] [01:12:22.16] first moved out here I'm like oh this is
[L2067] [01:12:23.36] great. My my grandfather was a petroleum
[L2068] [01:12:25.12] engineer and so I kind of grew up with
[L2069] [01:12:26.96] stories of like plants that were going
[L2070] [01:12:28.72] to be built and then shut down or
[L2071] [01:12:29.92] pipelines that were going to be built
[L2072] [01:12:30.88] and then shut down. Like everything
[L2073] [01:12:31.92] tracking the price of oil, right? Very
[L2074] [01:12:33.68] oil the oil patch is very boom and bust.
[L2075] [01:12:35.92] And I'm like oh this is great. I'm in
[L2076] [01:12:37.28] software like I'm immune from booms and
[L2077] [01:12:39.36] bust. I remember thinking this like you
[L2078] [01:12:40.96] know you're just like [laughter]
[L2079] [01:12:42.40] and of course looking back at it now
[L2080] [01:12:44.64] you're like oh my god no we are the they
[L2081] [01:12:48.16] are a bit endemic and they're endemic
[L2082] [01:12:50.40] for reasons that are are somewhat
[L2083] [01:12:51.76] endearing in that like we get so
[L2084] [01:12:54.48] optimistic that we kind of get ahead of
[L2085] [01:12:56.88] ourselves from an optimism perspective
[L2086] [01:12:59.36] we also get ahead of ourselves from a
[L2087] [01:13:00.88] pessimism perspective and the and what I
[L2088] [01:13:03.92] would say is like you got to be really
[L2089] [01:13:05.76] careful about listening to other people
[L2090] [01:13:09.60] people will tell you that this is going
[L2091] [01:13:11.12] to be the future or that thing is dead.
[L2092] [01:13:13.52] And you got to be like just be your own
[L2093] [01:13:16.56] judge. I had people tell me that
[L2094] [01:13:18.32] operating systems are done in 1996.
[L2095] [01:13:21.76] I'm really glad I didn't listen to them.
[L2096] [01:13:23.84] Really glad I didn't listen to them. We
[L2097] [01:13:25.60] people tell us you can't start a
[L2098] [01:13:27.04] computer company in 2019. I'm really
[L2099] [01:13:29.04] glad we didn't listen to them. That you
[L2100] [01:13:31.20] I VC firms we only fund SAS. Those VC
[L2101] [01:13:34.56] firms are like well it's like SAS is
[L2102] [01:13:36.32] struggling right now. Um but I would
[L2103] [01:13:38.24] also say similarly like if SAS is in
[L2104] [01:13:40.72] your heart as an example where people
[L2105] [01:13:42.32] are like right now people are like SAS
[L2106] [01:13:45.04] is going to be the the Genai the LLM
[L2107] [01:13:48.96] assisted coding is going to really put a
[L2108] [01:13:51.68] squeeze on the SAS companies and I think
[L2109] [01:13:54.32] like there's definitely truth to that
[L2110] [01:13:56.08] but if one's heart is in that you should
[L2111] [01:13:58.48] ignore the ignore the pessimism or or or
[L2112] [01:14:02.40] treat the pessimism and the optimism
[L2113] [01:14:05.44] with a grain of salt. be be your own
[L2114] [01:14:07.36] judge and be be true to what you want to
[L2115] [01:14:11.84] do. Don't do the things that like well
[L2116] [01:14:14.00] I'm doing this because it's like a hot
[L2117] [01:14:15.68] space. It's like you should do this
[L2118] [01:14:17.84] because I think it's and there are
[L2119] [01:14:19.44] plenty of people for good reason. I mean
[L2120] [01:14:21.04] these things are amazing. I mean the the
[L2121] [01:14:23.68] where we are with respect to these LLMs
[L2122] [01:14:25.60] is just bonkers. And you could easily
[L2123] [01:14:27.28] say I want to be very find a great deal
[L2124] [01:14:31.20] of intrinsic appeal to that. But that's
[L2125] [01:14:33.20] the reason that you should be going into
[L2126] [01:14:34.40] these systems is because you think like
[L2127] [01:14:35.92] no no this is this is to to quote Steve
[L2128] [01:14:39.12] Jobs this is the dent I want to kick in
[L2129] [01:14:40.80] the universe.
[L2130] [01:14:42.00] >> I noticed your career almost
[L2131] [01:14:43.60] everything's driven from fulfillment and
[L2132] [01:14:46.56] intrinsic motivation.
[L2133] [01:14:49.36] >> Is there a time in your career that you
[L2134] [01:14:51.68] look at and you say that's the happiest
[L2135] [01:14:53.20] time of my career?
[L2136] [01:14:55.04] >> Yeah that's a great question. We ask
[L2137] [01:14:56.32] this at oxide. We ask you when have you
[L2138] [01:14:57.76] been happiest and why? Um for exactly
[L2139] [01:15:00.16] that reason. And I would say that like
[L2140] [01:15:02.00] there it's not the it's not necessarily
[L2141] [01:15:05.28] an era. Um it is it is the it is times
[L2142] [01:15:09.20] that I've been happy. I mean bluntly
[L2143] [01:15:10.72] like I'm pretty happy right now. Oxide's
[L2144] [01:15:12.40] great.
[L2145] [01:15:13.52] >> Right. The we have the moments for me
[L2146] [01:15:16.80] and this was an important kind of
[L2147] [01:15:18.00] question for me to reflect on as we were
[L2148] [01:15:19.92] starting Oxide. And this is actually due
[L2149] [01:15:21.60] to a friend of mine who um had been at a
[L2150] [01:15:24.16] startup and he and I were taking a walk
[L2151] [01:15:26.08] in San Francisco as kind of Steve and I
[L2152] [01:15:27.84] are talking about bad ideas and he was
[L2153] [01:15:30.00] like you really need to answer for
[L2154] [01:15:31.52] yourself why do you want to do this?
[L2155] [01:15:33.92] What what is drawing you to start a
[L2156] [01:15:35.84] company? And because it wasn't financial
[L2157] [01:15:38.88] return for me and people should not
[L2158] [01:15:40.56] start a company for financial return.
[L2159] [01:15:41.76] That's just not a good that's not good
[L2160] [01:15:43.04] life advice. Um, but what was drawing
[L2161] [01:15:45.68] like well the thing that's drawing me
[L2162] [01:15:47.04] actually is the the moments that have
[L2163] [01:15:48.96] been the happiest have been working on
[L2164] [01:15:51.44] an incredible team and being on a team
[L2165] [01:15:55.28] that where everyone individually is like
[L2166] [01:15:57.68] I don't think we can pull this off like
[L2167] [01:15:59.68] this is actually too difficult to pull
[L2168] [01:16:01.20] off and then everybody works together
[L2169] [01:16:04.72] compliments one another and you pull it
[L2170] [01:16:06.80] off man that is that feeling is
[L2171] [01:16:10.88] extraordinary and the times that I'd had
[L2172] [01:16:12.88] that I'd had it with trace. I I had had
[L2173] [01:16:14.88] it at Fishworks. I'd had it at Joint a
[L2174] [01:16:17.52] couple of times with LX with Triton. Um
[L2175] [01:16:20.40] that those times have been like, "Oh,
[L2176] [01:16:22.24] that that's what's amazing to me." And
[L2177] [01:16:24.48] so, I mean, in many ways, like the
[L2178] [01:16:26.24] bedrock of Oxide is like, "What if we
[L2179] [01:16:27.84] found a company around part of the
[L2180] [01:16:29.92] reason we were appealing the larger
[L2181] [01:16:31.84] problem was appealing to us is like
[L2182] [01:16:33.36] we're going to be able to attract an
[L2183] [01:16:35.76] extraordinary team." And we have a team
[L2184] [01:16:38.24] that is it is so uplifting to be on a
[L2185] [01:16:41.92] team. I've always said that the the
[L2186] [01:16:43.04] organizational model for for Oxide is a
[L2187] [01:16:45.20] heist movie. You know, you've got your
[L2188] [01:16:46.72] safe cracker, you've got your getaway
[L2189] [01:16:48.08] driver, your demolitions expert, right?
[L2190] [01:16:49.44] Like heist movies are great because of
[L2191] [01:16:51.04] that. And like because it's the it's the
[L2192] [01:16:53.12] group coming together, everyone's
[L2193] [01:16:55.18] [snorts] skill sets kind of coming in at
[L2194] [01:16:56.80] exactly the right moment. And man, I
[L2195] [01:16:59.20] love that. I I love that so much. And
[L2196] [01:17:02.00] and Steve loves that. I mean, that's
[L2197] [01:17:03.60] that's part of like our shared bond is
[L2198] [01:17:06.32] he and I are both very very team
[L2199] [01:17:08.08] oriented. We built a company around
[L2200] [01:17:09.68] that. And uh it's extraordinary. I it is
[L2201] [01:17:12.72] it is truly truly extraordinary. It's
[L2202] [01:17:14.24] why we've been able to pull off what
[L2203] [01:17:15.52] we've been able to pull off with the
[L2204] [01:17:17.12] small team that we've got. I think
[L2205] [01:17:18.16] people are kind of shocked at how small
[L2206] [01:17:20.00] a team that that we've got given what
[L2207] [01:17:21.68] we've been able to pull off.
[L2208] [01:17:22.72] >> You when you look back on your whole
[L2209] [01:17:24.08] career, is there a particular top regret
[L2210] [01:17:27.28] that you have? [laughter]
[L2211] [01:17:28.96] >> I mean, I made an extraordinarily bad
[L2212] [01:17:31.28] hire at joint. I think the worst hire in
[L2213] [01:17:33.44] human history. Many people in Silicon
[L2214] [01:17:35.60] Valley will say like, "Well, that can't
[L2215] [01:17:36.80] be the worst hire in human history
[L2216] [01:17:38.16] because I feel I have made the worst
[L2217] [01:17:40.16] hire in human history." And as I tell
[L2218] [01:17:41.84] people like, "Look, I'm happy to give up
[L2219] [01:17:43.20] the give up the crown." But you should
[L2220] [01:17:45.12] know that my guy presented himself under
[L2221] [01:17:46.64] an assumed name and just got off parole
[L2222] [01:17:48.24] for violent felonies from San Quinton
[L2223] [01:17:50.24] and it's not what made him a bad
[L2224] [01:17:51.76] employee. And usually people are like,
[L2225] [01:17:54.56] "No, no, no. I think you've made the
[L2226] [01:17:55.76] worstful time." I'm like, "Thank you.
[L2227] [01:17:56.96] Thank you very much." Um, that was a bad
[L2228] [01:18:00.24] experience.
[L2229] [01:18:01.76] It was also very eye- openening because
[L2230] [01:18:03.84] everything I was doing about hiring was
[L2231] [01:18:05.28] wrong. And we after we rectified that
[L2232] [01:18:08.16] situation and got him out, we stripped
[L2233] [01:18:10.80] hiring to the studs and really rethought
[L2234] [01:18:13.20] hiring from the from the very first
[L2235] [01:18:15.04] principles. That hiring process, a very
[L2236] [01:18:17.60] writing intensive process, one that
[L2237] [01:18:19.28] really gets to intrinsic motivation
[L2238] [01:18:22.40] became the hiring process at Oxide. And
[L2239] [01:18:25.04] there was a moment where I'm like, "Oh
[L2240] [01:18:26.48] my god." Like this extraordinary team at
[L2241] [01:18:28.80] Oxide. Very much I think related
[L2242] [01:18:32.56] absolutely to the hiring process that we
[L2243] [01:18:34.16] have. This hiring process that I built
[L2244] [01:18:36.00] because I made the worst hiring hire of
[L2245] [01:18:37.52] all time. I needed that guy.
[L2246] [01:18:38.88] >> So you don't regret it?
[L2247] [01:18:39.92] >> I don't regret it. I don't I don't
[L2248] [01:18:41.52] regret it. In fact, I'm even like to
[L2249] [01:18:43.92] kind of go back into the time machine
[L2250] [01:18:45.36] and remove it. I think oxide I don't
[L2251] [01:18:47.68] think no oxide makes it because I would
[L2252] [01:18:50.48] have continued to hire the way I was
[L2253] [01:18:52.88] hiring which was naively it was hiring
[L2254] [01:18:57.28] not rigorously it was not selecting
[L2255] [01:18:59.60] people based on their values so no I
[L2256] [01:19:01.60] absolutely needed it so I think and I
[L2257] [01:19:03.20] view that way of a lot of things that
[L2258] [01:19:04.48] maybe not gone the right way but all of
[L2259] [01:19:06.80] those failures were really really
[L2260] [01:19:09.20] important and it's very hard to go back
[L2261] [01:19:11.68] and and and you don't want to take those
[L2262] [01:19:14.16] away I mean if I go to the time machine
[L2263] [01:19:15.68] maybe I would take away the the Usenet
[L2264] [01:19:17.04] post and maybe that would maybe that
[L2265] [01:19:18.64] wouldn't have any long-lasting
[L2266] [01:19:19.68] consequences. But boy, that's about it.
[L2267] [01:19:21.68] >> Awesome. And then last question is uh if
[L2268] [01:19:24.32] you could go back to the beginning of
[L2269] [01:19:25.36] your career knowing everything you know
[L2270] [01:19:26.88] now, what advice would you give
[L2271] [01:19:28.80] yourself?
[L2272] [01:19:29.28] >> Jesus, don't it up.
[L2273] [01:19:31.12] >> Don't I I I just think because like
[L2274] [01:19:33.84] I feel like so
[L2275] [01:19:35.92] lucky. So I I I've been so lucky in so
[L2276] [01:19:39.12] many regards. has been in the right
[L2277] [01:19:40.24] place at the right time so many
[L2278] [01:19:41.68] different times over and I've trusted my
[L2279] [01:19:44.24] gut when sometimes that was not the
[L2280] [01:19:45.92] thing that when that was kind of a a
[L2281] [01:19:48.64] controver thing to do. I I I mean I
[L2282] [01:19:51.76] would be scared to give myself advice
[L2283] [01:19:55.04] because I would be worried that I would
[L2284] [01:19:58.00] somehow tamper with what I feel has been
[L2285] [01:20:01.36] an extraordinarily lucky career where I
[L2286] [01:20:04.16] have I I've been able to do so much with
[L2287] [01:20:07.68] so many extraordinary people. I' I've
[L2288] [01:20:09.44] I've been blessed with so many
[L2289] [01:20:11.92] incredible colleagues and I that has
[L2290] [01:20:16.16] been so essential for everything that
[L2291] [01:20:18.48] I've done and I wouldn't want to do
[L2292] [01:20:19.68] anything to endanger that. So I'd be
[L2293] [01:20:20.88] going back to my past self. I'd be like,
[L2294] [01:20:22.16] I got nothing to say. Like just yeah, I
[L2295] [01:20:24.08] don't want to screw anything up. Like I
[L2296] [01:20:25.52] just because I I feel that I feel really
[L2297] [01:20:28.40] really lucky. And it wasn't always
[L2298] [01:20:29.60] because of because again, it's like I I
[L2299] [01:20:31.44] made mistakes along the way, but the
[L2300] [01:20:33.92] mistakes became loadbearing and
[L2301] [01:20:36.16] important and I wouldn't want to I
[L2302] [01:20:37.84] wouldn't want to not make those
[L2303] [01:20:39.12] mistakes. Those mistakes were really
[L2304] [01:20:40.56] important.
[L2305] [01:20:41.60] >> Well, doesn't get better than that and
[L2306] [01:20:43.44] thank you for your time today. I really
[L2307] [01:20:45.04] appreciate it.
[L2308] [01:20:45.52] >> Absolutely. Thank you for the thoughtful
[L2309] [01:20:46.64] questions. really great conversation and
[L2310] [01:20:48.00] thanks for I I doing the the hall of
[L2311] [01:20:51.12] shame here on on the past tweets. That
[L2312] [01:20:53.28] was a lot of fun.
[L2313] [01:20:54.08] >> Yeah. [laughter] Awesome. Thanks so
[L2314] [01:20:55.52] much.
[L2315] [01:20:56.16] >> Thank you.
[L2316] [01:20:57.36] >> Thank you for listening to the podcast.
[L2317] [01:20:59.12] It's a passion project of mine that I've
[L2318] [01:21:01.36] really enjoyed building. Another passion
[L2319] [01:21:03.36] project that I've been working on kind
[L2320] [01:21:04.72] of in secret is building an ergonomic
[L2321] [01:21:07.28] keyboard that I wish existed and I
[L2322] [01:21:09.52] finally have a prototype. So, I'd love
[L2323] [01:21:11.12] to show you what we've built. It's ultra
[L2324] [01:21:14.00] low profile and ergonomic. and I
[L2325] [01:21:16.64] couldn't find anything like it on the
[L2326] [01:21:18.00] market. So, that's why we built it. I'll
[L2327] [01:21:19.84] put a link to the keyboard in the
[L2328] [01:21:21.20] description. You can take a look and
[L2329] [01:21:22.64] learn more about the project there. We
[L2330] [01:21:24.48] could definitely use your support. Also,
[L2331] [01:21:26.48] if you have any feedback for me about
[L2332] [01:21:28.08] the show, I'd love to hear it. Comments
[L2333] [01:21:30.48] on YouTube have led to guests coming on
[L2334] [01:21:32.56] like Ilia Gregoric and David Fowler. I
[L2335] [01:21:35.68] wasn't aware of them until someone
[L2336] [01:21:37.44] dropped a comment. Also, feedback in the
[L2337] [01:21:39.44] comments helped me learn to reduce the
[L2338] [01:21:41.12] number of cliffhers in the intros. So,
[L2339] [01:21:43.76] your comments definitely make a
[L2340] [01:21:44.96] difference. Please keep letting me know
[L2341] [01:21:46.40] what you'd like to see more of in the
[L2342] [01:21:48.00] show, and I'll see you in the next
[L2343] [01:21:49.36] episode.
