# Instagram iOS Principal Eng (IC8): Building IG Stories, 1 Promo Per Half, Small Teams

Source ID: source-77b7f65a700842eb
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Instagram_iOS_Principal_Eng_(IC8)_Building_IG_Stories,_1_Promo_Per_Half,_Small_Teams_en.txt
Video: https://www.youtube.com/watch?v=gpVETZnY9Y0

[L10] [00:00.08] It actually felt in some ways like
[L11] [00:02.16] Instagram was dying.
[L12] [00:04.16] >> This is Ryan Olsen. He grew to a
[L13] [00:06.56] principal engineer or IC8 at Instagram
[L14] [00:09.04] in just a few years. One promo per half
[L15] [00:12.32] or two halves straight. What was that
[L16] [00:14.32] like?
[L17] [00:14.88] >> I was like, "Hey, I think I got misleled
[L18] [00:16.72] and I think you should promote me from
[L19] [00:18.24] four to six in this cycle." [laughter]
[L20] [00:20.96] >> As the lead iOS engineer on Instagram
[L21] [00:23.28] stories, he shared what it was like
[L22] [00:24.88] behind the scenes.
[L23] [00:26.00] >> The CTO and co-founder Mike Kger, he was
[L24] [00:28.48] like, "You know what? Don't don't worry
[L25] [00:30.00] about trying to AB test this thing.
[L26] [00:31.68] Build and ship it.
[L27] [00:33.20] >> Do you think that the company would be
[L28] [00:35.36] better off if you just like laid off
[L29] [00:37.28] half the people?
[L30] [00:38.56] >> Even if it's a random selection, do
[L31] [00:40.72] things go better and frequently we felt
[L32] [00:43.36] like, yeah, maybe.
[L33] [00:48.64] >> In 2011, I understand that you you
[L34] [00:51.28] interviewed for Facebook and and you
[L35] [00:53.60] failed. Can you talk through that
[L36] [00:55.52] experience and what that was like? I
[L37] [00:57.44] thought Facebook was super cool at the
[L38] [00:59.04] time. Um, I wanted it so bad. And uh I
[L39] [01:03.12] was just incredibly nervous. Like
[L40] [01:05.50] [laughter]
[L41] [01:06.72] um I I remember the uh interviewer, he
[L42] [01:09.92] kind of asked the question. He's like,
[L43] [01:11.28] "Oh, you can just do it on my machine."
[L44] [01:12.88] He turned around his laptop, pushed it
[L45] [01:15.28] over to me. I put my hands on the
[L46] [01:17.12] keyboard. You could actually hear like
[L47] [01:19.36] the the keys like rattling because I was
[L48] [01:21.76] shaking so bad, which just, you know, it
[L49] [01:23.92] starts this feedback loop. um hearts
[L50] [01:26.48] pounding and uh the question that he
[L51] [01:29.52] asked was actually one that ended up
[L52] [01:31.04] getting banned at Facebook um which I
[L53] [01:33.20] feel some uh somewhat better about but
[L54] [01:36.88] um
[L55] [01:37.44] >> what was the question? It was this
[L56] [01:39.68] engram buckets question which yeah
[L57] [01:42.88] there's like a very simple solution if
[L58] [01:44.72] you know data structures um where use a
[L59] [01:48.32] dictionary um and that solution didn't
[L60] [01:51.76] come to me so I wrote this like
[L61] [01:53.84] horrendous triple nested for loop um I
[L62] [01:57.28] mean it was definitely like you know the
[L63] [01:58.96] interview went quite poorly and yeah so
[L64] [02:01.60] he he actually cut the interview short
[L65] [02:03.84] which as as an interviewer that's like
[L66] [02:06.08] something I would never do um even if
[L67] [02:08.32] somebody's was failing like you want to
[L68] [02:10.24] you want to try to have a good candidate
[L69] [02:11.76] experience. Um and so he cut it short
[L70] [02:14.72] and he was just like look you you you're
[L71] [02:16.64] just not going to be able to make it at
[L72] [02:18.72] Facebook. Um which was like kind of a
[L73] [02:22.08] knife to the heart like I I you know I
[L74] [02:24.32] wanted this thing so bad and then this
[L75] [02:25.84] guy is just like yeah you're just not
[L76] [02:27.36] good enough for this. Um and it actually
[L77] [02:30.40] took me like I was really down from that
[L78] [02:32.48] for for a while. It took me a while to
[L79] [02:34.00] kind of like bounce back uh after that.
[L80] [02:36.48] Luckily I did bounce back. I feel like I
[L81] [02:38.64] I I had a pretty good good career at
[L82] [02:40.88] Facebook, so I managed to managed to
[L83] [02:43.04] prove him wrong. I I I never got the
[L84] [02:46.00] name of the interviewer. Um, so I I have
[L85] [02:48.72] no idea who it was, but Yeah.
[L86] [02:50.40] >> Yeah. Well, I mean, that to me shows how
[L87] [02:53.68] broken the interview process is. If I
[L88] [02:56.32] mean, you're an incredibly high
[L89] [02:58.24] performer and if you are not getting
[L90] [03:01.12] through it, then clearly it's not, you
[L91] [03:03.28] know, testing for the right things.
[L92] [03:05.20] >> Yeah. I've always I've always struggled
[L93] [03:06.88] actually with like the the lead code
[L94] [03:08.48] style um interview and and uh it was
[L95] [03:12.00] something I was always interested in
[L96] [03:13.28] trying to change while at Facebook but
[L97] [03:15.60] um it you know it's the interview
[L98] [03:17.60] process there is such a such a machine
[L99] [03:19.92] across a big company. Um it's one of the
[L100] [03:22.48] things I enjoy about having my own
[L101] [03:23.76] company is like you know I don't have to
[L102] [03:25.52] do those things that I don't agree with.
[L103] [03:27.44] And so after failing that Facebook
[L104] [03:29.12] interview, I understand that you went to
[L105] [03:31.52] go work at a startup named Flipboard and
[L106] [03:34.08] you were an intern, one of four interns.
[L107] [03:36.40] What was that experience like working at
[L108] [03:38.80] Flipboard?
[L109] [03:39.76] >> Yeah, so um I'll tell a little bit more
[L110] [03:41.52] of the in between story there. Um I a
[L111] [03:45.36] couple months after the Facebook
[L112] [03:47.04] interviewed
[L113] [03:49.12] with Amazon um and uh it was a phone
[L114] [03:52.88] interview, so I was actually a lot more
[L115] [03:54.40] comfortable. Um I did well on that. how
[L116] [03:56.80] I got the offer. Uh they did the kind of
[L117] [03:59.04] exploding offer. It was like, you know,
[L118] [04:01.28] I got a call on Friday. It was like, you
[L119] [04:02.88] need to tell us by Monday if you're
[L120] [04:04.40] taking this or not. Um and I was
[L121] [04:08.72] prepared to take it. Seemed like a cool
[L122] [04:11.04] cool opportunity. I had a an investor
[L123] [04:13.92] friend. He um founded Insight Partners,
[L124] [04:17.20] which is one of the big uh venture
[L125] [04:19.52] firms. and um he had mentioned at some
[L126] [04:24.24] point in the past he's like you know at
[L127] [04:26.24] some point maybe I'll connect you with
[L128] [04:27.52] with some startups and so I just reached
[L129] [04:30.08] out to him and I said hey you know I'm I
[L130] [04:32.72] got this intern offer at Amazon I think
[L131] [04:34.48] I'm going to take it and he was like
[L132] [04:36.88] don't take it yet like let me connect
[L133] [04:38.80] you with some startup people um so it
[L134] [04:42.00] was on a Sunday and he um sent an email
[L135] [04:46.80] connecting me with uh the co-founder of
[L136] [04:49.04] Flipboard this guy Evan Well, Evan
[L137] [04:51.44] called me right away and I actually I
[L138] [04:54.08] didn't really want to pick up the phone
[L139] [04:55.44] cuz I was like, "Oh man, I I don't want
[L140] [04:57.20] to do another interview and um kind of
[L141] [04:59.76] just want to take this job offer that I
[L142] [05:01.44] have." Um but I'm very glad I picked up
[L143] [05:03.68] the phone. Um and I had a great
[L144] [05:05.76] conversation with Evan. He uh he had
[L145] [05:09.04] worked at Apple on kind of the core of
[L146] [05:11.60] iOS. Um he actually wrote UI view
[L147] [05:13.92] controller which is you know like the
[L148] [05:15.92] the core kind of UI uh class that you
[L149] [05:18.88] interact with and uh he had also taught
[L150] [05:22.56] this course at Stanford um called CS
[L151] [05:26.00] 193P which they made available on iTunes
[L152] [05:30.00] and that was how I learned iOS
[L153] [05:32.00] development. I I took it a different
[L154] [05:33.92] year that Evan didn't teach. Um, but we
[L155] [05:36.72] had a really good conversation about
[L156] [05:38.08] that and uh, so after that phone call I
[L157] [05:41.44] was like, "Yeah, okay. This this makes
[L158] [05:42.88] sense. Like this this just seems way
[L159] [05:44.88] more interesting than whatever I'm going
[L160] [05:46.32] to do at at Amazon." So I went there in
[L161] [05:49.36] the summer and the company was about 50
[L162] [05:52.56] people at that time and I think yeah, we
[L163] [05:55.36] had like maybe four interns or so. Um,
[L164] [05:59.28] and it was just a a an extremely high
[L165] [06:03.20] density of talent like uh people were
[L166] [06:07.04] all super smart. Um, they come from
[L167] [06:10.48] these backgrounds, you know, like
[L168] [06:12.48] writing the iOS frameworks at Apple. Um,
[L169] [06:16.32] the one of the other interns that I sat
[L170] [06:19.04] next to, he he wasn't really an intern.
[L171] [06:20.64] He had worked at Apple and he was
[L172] [06:22.32] actually doing a medical degree and he
[L173] [06:24.72] just needed a job for the summer. He was
[L174] [06:26.56] friends with Evan. So, um, but he had
[L175] [06:29.76] written the push notifications framework
[L176] [06:32.24] and he was talking about like how he set
[L177] [06:34.64] that up for the demo at WWC and it was
[L178] [06:36.96] like running off his like Mac Mini just
[L179] [06:39.76] in Moscone where they had the conference
[L180] [06:42.56] and um and another story he told was uh
[L181] [06:46.80] he had written like the um kind of clock
[L182] [06:50.40] framework, the clock app and they had a
[L183] [06:53.60] bad time zone bug one year for I think
[L184] [06:56.32] it was around New years or something and
[L185] [06:58.00] they screwed up and like people's alarms
[L186] [06:59.76] didn't go off and was like fairly
[L187] [07:02.32] catastrophic. Um, and it's like yeah,
[L188] [07:05.52] actually make making sure people's
[L189] [07:07.36] alarms go off is pretty important. Um,
[L190] [07:10.24] so yeah, it was just a really really
[L191] [07:12.40] good learning environment and I learned
[L192] [07:14.16] a ton about iOS and about building
[L193] [07:16.72] product. Two of the other interns um
[L194] [07:21.04] have gone on to to make multi-billion
[L195] [07:24.24] dollar companies. Um, one is Dylan Field
[L196] [07:27.52] who founded Figma, which went public
[L197] [07:29.84] yesterday. I think it's a $50 billion
[L198] [07:32.16] market cap today. Um, he actually he was
[L199] [07:36.48] an intern through the first half of the
[L200] [07:38.56] summer that I was there and then um he
[L201] [07:41.36] ended his internship and he founded
[L202] [07:43.28] Figma then. Um, so um yeah, that that it
[L203] [07:48.40] it was it was cool. People were kind of
[L204] [07:50.48] into startups, entrepreneurial. Um, I
[L205] [07:53.20] actually really questioned whether I
[L206] [07:54.72] should go back to finish my last year of
[L207] [07:56.64] school. I'm ultimately glad that I did,
[L208] [07:58.96] but it felt like there was just this
[L209] [08:00.48] moment happening. I was like, I can't
[L210] [08:01.92] leave. I I have to stay here and um if
[L211] [08:05.04] if I go back to school, I'm going to
[L212] [08:06.56] miss out on on something really
[L213] [08:08.00] critical.
[L214] [08:08.88] >> So, Dylan Field, co-founder of Figma, is
[L215] [08:11.60] one of the interns. And I saw in your
[L216] [08:14.08] writing the other intern was Devon Fin
[L217] [08:16.72] Fininser who's like founder of OpenC
[L218] [08:19.92] which is also at some point it was
[L219] [08:21.92] billion dollar. I don't know the exact
[L220] [08:23.28] valuation now but that is that is
[L221] [08:26.08] absurd. Were there any traits that you
[L222] [08:28.32] noticed in those people or that intern
[L223] [08:31.04] class that kind of foreshadowed that
[L224] [08:33.04] they would be that successful?
[L225] [08:34.96] >> They were definitely determined to start
[L226] [08:36.64] companies. it was like that was what
[L227] [08:38.40] they wanted to do. And I think that was
[L228] [08:40.64] a bit different than what I saw, you
[L229] [08:44.00] know, from like my university
[L230] [08:45.28] classmates. People just wanted to get a
[L231] [08:47.76] job, you know, kind of like the highest
[L232] [08:50.40] aspiration was like to work at a big
[L233] [08:52.16] tech company. Um, and both Devon and
[L234] [08:55.92] Dylan were like, you know, we want to
[L235] [08:58.24] start companies. And there was a lot of
[L236] [09:00.56] talk about ideas and and what they would
[L237] [09:03.28] do. It's interesting to think back of
[L238] [09:05.68] back to the early days of Figma or you
[L239] [09:09.68] know like talking to Dylan around that
[L240] [09:11.92] time. I think the idea that they had
[L241] [09:16.56] they they weren't totally landed on the
[L242] [09:18.32] idea but they had this one really
[L243] [09:20.16] interesting insight which was WebGL was
[L244] [09:23.36] this new technology that was really
[L245] [09:25.28] going to enable new things on the web.
[L246] [09:27.92] And Dylan's co-founder Evan was a really
[L247] [09:31.12] talented engineer and was like very
[L248] [09:32.72] early to WebGL and very skilled at that.
[L249] [09:35.68] Um, and I think they went through some
[L250] [09:38.00] different iterations of the product that
[L251] [09:39.92] weren't really tailored toward designers
[L252] [09:41.60] at all. Like they Dylan had talked about
[L253] [09:44.16] how they were a meme generator app for a
[L254] [09:47.04] week or something like that. Yeah. I
[L255] [09:49.36] mean, so I think it took them a bit to
[L256] [09:51.04] to find exactly kind of their use case
[L257] [09:53.92] and their customer base. Um, but they
[L258] [09:56.64] they had this vision of like this
[L259] [09:58.96] technology is really going to change
[L260] [10:00.32] things and they stuck with that and uh
[L261] [10:02.48] it's it's cool cool to see how how far
[L262] [10:05.44] they came.
[L263] [10:06.32] >> Yeah. It seems like while you were
[L264] [10:07.44] working at Flipboard, you built a a
[L265] [10:10.00] successful open- source project and you
[L266] [10:12.56] know, yeah, some of the first commits
[L267] [10:13.92] are in 2014. I'm curious what's the
[L268] [10:17.52] story behind that and why did you open
[L269] [10:19.36] source that? So during my internship, I
[L270] [10:23.52] did some work on just kind of internal
[L271] [10:26.64] debugging tools for our iOS app. And um
[L272] [10:31.68] it was the it was the first time I'd
[L273] [10:33.36] really worked deeply in Objective C. And
[L274] [10:36.72] I found the language really interesting
[L275] [10:38.88] because it's a compiled language, but it
[L276] [10:41.12] has this dynamic aspect. It has this
[L277] [10:43.04] runtime that exposes actually quite a
[L278] [10:45.28] bit of information. you know while the
[L279] [10:47.20] app is running you can inspect a lot of
[L280] [10:49.36] things about um what are [clears throat]
[L281] [10:51.12] the classes what are the methods on
[L282] [10:52.64] those classes you can call them
[L283] [10:54.48] dynamically you can see all the state
[L284] [10:56.56] all the properties and uh so the first
[L285] [11:00.56] kind of iteration of that was just
[L286] [11:02.72] building a tool to kind of inspect the
[L287] [11:05.84] state of the app and and tweak it um on
[L288] [11:08.08] demand I think we called it tweaker it
[L289] [11:10.08] was FL tweaker um and I just kind of
[L290] [11:14.32] continued iterating on that um as like a
[L291] [11:17.52] side project. I mean my main you know we
[L292] [11:19.84] were a startup so we had probably
[L293] [11:21.84] between three to five people on the iOS
[L294] [11:24.16] team through through most of my time
[L295] [11:26.24] there and so mostly I was building
[L296] [11:28.96] Flipboard, building the app, building
[L297] [11:30.40] new features. Um so it was kind of like
[L298] [11:32.64] a nights and weekends thing that I was
[L299] [11:34.40] working on this debugging tool and uh
[L300] [11:37.68] people in the company found it really
[L301] [11:39.36] useful. It was just um yeah a way to
[L302] [11:42.48] kind of like understand what was going
[L303] [11:45.12] on in the app under the hood. Um you
[L304] [11:47.20] could see all the network requests, you
[L305] [11:48.72] could see what was on the file system. I
[L306] [11:50.88] kind of asked, hey, can I open source
[L307] [11:52.72] this? I think it's like going to be
[L308] [11:54.00] useful for for other people. And um
[L309] [11:58.08] everyone was on board with that. So we
[L310] [12:00.16] pushed it out and uh yeah, it's it's
[L311] [12:02.48] become um [snorts] one of the more
[L312] [12:05.12] popular iOS debugging tools. I think a
[L313] [12:07.68] lot of a lot of apps use it. definitely
[L314] [12:09.76] used it uh Facebook and Instagram. It's
[L315] [12:12.32] It was also cool to see it. It took on
[L316] [12:14.80] kind of a life of its own. So, I've been
[L317] [12:17.44] less active as a maintainer of it in the
[L318] [12:20.40] past probably probably really since I
[L319] [12:22.48] started Instagram. Uh maybe a couple
[L320] [12:24.72] years into that. Uh but this guy Tanner
[L321] [12:27.36] really took it over and um has continued
[L322] [12:29.84] evolving it and adding features.
[L323] [12:31.76] >> That's awesome. Um, I remember hearing
[L324] [12:34.48] about Flex at Instagram as well. So, I
[L325] [12:37.60] wasn't aware that that was actually
[L326] [12:38.96] something you'd built before you were at
[L327] [12:40.72] the company, which is really cool. I'm
[L328] [12:42.96] curious, did building something like
[L329] [12:44.80] that and open sourcing it have some
[L330] [12:47.28] unexpected, you know, butterfly effect
[L331] [12:49.68] on your career in some way?
[L332] [12:51.28] >> In some ways it did. In some ways, I
[L333] [12:53.04] thought maybe it would have more um
[L334] [12:55.84] impact than than it did. So an example
[L335] [12:59.04] of that is um when I came to interview
[L336] [13:02.00] at Instagram uh I had already released
[L337] [13:05.52] this open source and so I was like you
[L338] [13:07.36] know here's here's my code you want to
[L339] [13:09.12] see what I can do like this is a thing
[L340] [13:11.04] that I built that you can go look at and
[L341] [13:13.44] and none of my interviewers had any
[L342] [13:15.20] interest in in in looking at it you know
[L343] [13:17.84] they were like we want to know if you
[L344] [13:19.12] can do this phone number sorting thing
[L345] [13:21.84] um and so that was like pretty
[L346] [13:23.52] frustrating to me I was like you know
[L347] [13:25.36] you you can see my work here and you and
[L348] [13:27.76] you choosing not to look at it. Other
[L349] [13:30.00] people who are kind of slightly outside
[L350] [13:32.32] of the interview loop but part of the
[L351] [13:33.84] recruiting process um like uh Jonathan
[L352] [13:37.68] Dan was this guy who worked at uh
[L353] [13:40.48] Facebook on the iOS team. He kind of I
[L354] [13:43.52] think he actually did the file new
[L355] [13:46.08] project in Xcode for the Facebook iOS
[L356] [13:48.32] app. [laughter] Um, so he'd kind of
[L357] [13:50.08] started that and uh he was the one who
[L358] [13:53.12] who got me to interview in the first
[L359] [13:55.04] place and and that was all through him
[L360] [13:57.60] seeing this tool and what it could do
[L361] [13:59.92] and yeah and I think he advocated in the
[L362] [14:02.96] candidate review or whatever cuz I I
[L363] [14:04.64] think I had kind of a mixed mixed
[L364] [14:06.64] interview loop. Um yeah, I mentioned
[L365] [14:09.04] before like I was uh was very nervous in
[L366] [14:12.00] my in my uh internship interview. Um,
[L367] [14:15.76] and uh the I did something for my
[L368] [14:19.28] full-time interview that um it's maybe
[L369] [14:21.60] helpful to to some people out there uh
[L370] [14:24.56] that get nervous in interview
[L371] [14:26.24] situations. Um there's something called
[L372] [14:28.24] beta blockers which uh they they block
[L373] [14:32.16] adrenaline. So when you have kind of the
[L374] [14:35.84] physical effects of being nervous like
[L375] [14:38.56] pounding heart or you know sweaty palms,
[L376] [14:41.20] that type of thing, you can start to
[L377] [14:42.96] feel those and and it can create this
[L378] [14:45.44] feedback loop where you kind of spiral
[L379] [14:47.20] down and really starts to like block
[L380] [14:49.52] your performance. Um and so what a beta
[L381] [14:52.40] blocker does is it just stops that
[L382] [14:55.52] adrenaline from firing and so you can
[L383] [14:58.40] kind of stay calm and never end up in
[L384] [15:01.04] that spiral. So, um, I got a
[L385] [15:03.20] prescription for that for for my
[L386] [15:04.88] interview, um, interview
[L387] [15:06.48] performance-enhancing drugs, I guess,
[L388] [15:08.64] and, uh, and I took that and it was very
[L389] [15:11.28] helpful for me. So, I was able to to
[L390] [15:12.96] stay calm. Um, I think performers
[L391] [15:15.20] sometimes use this, uh, you know,
[L392] [15:18.08] comedians or whatever, um, just to to
[L393] [15:20.88] kind of like, you know, be able to stay
[L394] [15:23.28] themselves and not um, end up in this in
[L395] [15:26.24] this nervous loop. So I did that, but
[L396] [15:28.16] you know, I was still like kind of elite
[L397] [15:30.16] code style interview loop, which which I
[L398] [15:32.72] um don't do that well at. So I think I
[L399] [15:35.44] had like a few like absolute confidence
[L400] [15:37.92] hire uh interviews and probably a few no
[L401] [15:40.48] hires. Um somehow I managed to to get
[L402] [15:43.36] through. Um but I think that also
[L403] [15:46.32] contributed to I came into to Facebook
[L404] [15:50.48] as a IC4. Um I guess one level up from
[L405] [15:54.88] new grad engineer and um I would say
[L406] [15:59.04] like I was underleveled higher. I think
[L407] [16:01.76] you know part of that would have came
[L408] [16:03.04] from my interview loop. And when you use
[L409] [16:05.68] the beta blockers, I'm curious, is it
[L410] [16:07.92] basically completely removed the nerves
[L411] [16:10.72] component for you or is it just kind of
[L412] [16:12.56] like helps a little bit?
[L413] [16:14.16] >> I've only used them a handful of times.
[L414] [16:16.08] Um, but it pretty much completely, you
[L415] [16:19.44] know, like no noticeable kind of nervous
[L416] [16:23.20] effects. I mean, I think you can still
[L417] [16:25.44] be in your head for sure about um what
[L418] [16:29.20] you're saying, but um it takes away a
[L419] [16:31.68] lot of those physical effects. Um, so no
[L420] [16:34.40] no pounding hard or or you know
[L421] [16:36.32] sweating, that type of thing.
[L422] [16:37.58] [clears throat]
[L423] [16:37.84] >> After you passed the interview for
[L424] [16:39.20] full-time, you started working on the
[L425] [16:41.92] Instagram team working on iOS and I'm
[L426] [16:45.60] curious what the what the environment
[L427] [16:48.16] was like at the time. You know, what was
[L428] [16:49.92] the size of the team?
[L429] [16:51.20] >> Um, yes. So I came in and I think there
[L430] [16:53.84] were about 10 iOS engineers working on
[L431] [16:56.72] Instagram then. Um, which was actually
[L432] [16:59.68] the team size had come down. So the the
[L433] [17:03.60] way the story's been told to me is um
[L434] [17:06.40] there were maybe about 20 iOS engineers
[L435] [17:09.68] and there was kind of this internal war
[L436] [17:12.56] over um the direction of the the
[L437] [17:17.04] codebase like the infrastructure how how
[L438] [17:19.36] the Instagram iOS app would be built.
[L439] [17:22.48] And there was a really talented uh iOS
[L440] [17:24.96] engineer uh Scott Goodson who was
[L441] [17:26.96] managing the team and he had made this
[L442] [17:30.32] framework for the Facebook paper app
[L443] [17:33.44] called Async Display Kit and it was kind
[L444] [17:36.48] of a different approach towards how you
[L445] [17:39.84] manage um writing iOS. Uh, and I guess
[L446] [17:45.20] there were kind of like waring factions
[L447] [17:46.80] like some people were, you know, very
[L448] [17:48.24] pro async display kit and other people
[L449] [17:50.64] were like, "No, we should just stick to
[L450] [17:52.24] vanilla iOS, how Apple builds apps." The
[L451] [17:55.36] way it was told to me is like these two
[L452] [17:57.20] factions like they fought each other and
[L453] [17:59.04] they destroyed each side destroyed each
[L454] [18:01.04] other. Everyone just left and nobody
[L455] [18:03.28] won. So, um, so I came into kind of like
[L456] [18:07.12] this uh this team. I mean, I got to I I
[L457] [18:11.04] feel like not many engineers had been
[L458] [18:13.68] there more than, you know, 6 months to a
[L459] [18:16.00] year. It was like a pretty new team.
[L460] [18:19.52] Um, and because of that, there was
[L461] [18:23.28] actually like a lot of lowhanging fruit.
[L462] [18:25.28] Um, a lot [clears throat] of places to
[L463] [18:26.96] to have impact. One of the first things
[L464] [18:29.28] I did was just to put the app into uh a
[L465] [18:33.12] tool called the time profiler. Most iOS
[L466] [18:35.68] developers will will know this in Xcode.
[L467] [18:38.56] um or in instruments um and just looked
[L468] [18:41.68] at you know okay what is happening on
[L469] [18:43.68] cold start and there was a bunch in in
[L470] [18:47.68] kind of the startup path there was a
[L471] [18:49.12] bunch of work happening for the profile
[L472] [18:50.80] tab which you know many people will
[L473] [18:52.96] never tap into and um if they do you can
[L474] [18:56.00] kind of do that work at that time so it
[L475] [18:58.08] was like a very easy win to shave 20%
[L476] [19:01.20] off our cold start time just by
[L477] [19:03.12] deferring that work until later. Another
[L478] [19:05.76] example was we had this networking
[L479] [19:08.32] library uh AF networking and there's
[L480] [19:11.84] something um I mean I guess most
[L481] [19:14.40] programmers are familiar with assertions
[L482] [19:17.28] um in iOS the way assertions are
[L483] [19:20.08] typically handled is it's something that
[L484] [19:22.80] you run when the app is in debug mode to
[L485] [19:25.44] kind of crash and and alert you to a
[L486] [19:28.00] problem. uh but you kind of have
[L487] [19:30.88] fallback behavior for production and you
[L488] [19:33.60] don't actually crash the app and so this
[L489] [19:36.56] networking library was building being
[L490] [19:38.48] built with assertions on and it was
[L491] [19:42.72] crashing the app for like benign
[L492] [19:44.32] failures like a network failure right
[L493] [19:46.08] where the app could recover we were just
[L494] [19:48.32] crashing um and so that cut our crash
[L495] [19:50.80] rate by 80%. Um and uh you know it was
[L496] [19:54.40] just like a one on one line change just
[L497] [19:55.92] NS block assertions but it's a pretty
[L498] [19:58.32] significant impact on on the functioning
[L499] [20:01.52] of the app. Uh and we uh Instagram had
[L500] [20:05.04] this this cool tradition uh where every
[L501] [20:08.72] week they would give what was called the
[L502] [20:12.24] axe and it wasn't getting fired which it
[L503] [20:15.60] sounds like um if you got the axe it was
[L504] [20:18.40] like you did something of outsiz impact.
[L505] [20:21.20] Um, and it was actually across all
[L506] [20:23.36] functions. Didn't have to be
[L507] [20:24.64] engineering, could be product, design,
[L508] [20:26.64] whatever. And so for that 80% crash,
[L509] [20:30.16] crash reduction. I won the axe. And um
[L510] [20:33.44] it was this big physical axe uh that you
[L511] [20:36.16] got to carry around for a week. At
[L512] [20:37.52] first, I thought you got to take like I
[L513] [20:38.96] was like, "Oh, I get this axe."
[L514] [20:40.58] [laughter]
[L515] [20:40.80] >> Yeah.
[L516] [20:41.28] >> I had it at my desk for a week and I was
[L517] [20:43.04] like, "Oh, no. There's just one axe.
[L518] [20:44.72] Somebody else is going to get it next
[L519] [20:46.24] week." Um but yeah,
[L520] [20:48.80] >> I remember the axe. What's the story
[L521] [20:50.96] behind that? Is that something the
[L522] [20:52.64] Instagram founders like had done?
[L523] [20:55.36] >> At some point, they had been asked by
[L524] [20:57.04] like GQ or some men's magazine to do
[L525] [21:00.64] like a holiday gift guide and I think
[L526] [21:03.60] they just kind of came up with like
[L527] [21:05.20] random gifts and um one of them was like
[L528] [21:08.32] they found this service that was making
[L529] [21:10.08] like bespoke axes.
[L530] [21:13.60] you you could get this axe. And then one
[L531] [21:16.64] of their investors like read that
[L532] [21:18.16] article and then they sent them this
[L533] [21:19.76] huge axe. Um, and apparently Facebook
[L534] [21:23.44] security was like pretty unhappy about
[L535] [21:25.92] this axe, this weapon in the office, so
[L536] [21:29.20] they made them put it on a plaque. Uh,
[L537] [21:31.04] it was like mounted to the plaque. You
[L538] [21:32.72] couldn't take it off. Uh, but it was
[L539] [21:35.44] Yeah, it was it was a cool tradition.
[L540] [21:37.28] Um, you know, later, uh, in my time
[L541] [21:40.56] there, they ended the axe as like a very
[L542] [21:43.04] intentional thing. They were like, I
[L543] [21:44.64] guess they thought people were feeling
[L544] [21:46.16] excluded because it was like a weapon
[L545] [21:48.16] that was being given or something like
[L546] [21:49.76] that. But I I was kind of sad when that
[L547] [21:51.68] happened cuz it felt like, you know, at
[L548] [21:53.52] that time the founders were were gone
[L549] [21:55.44] and it was like this piece of like early
[L550] [21:57.76] Instagram culture that they were kind of
[L551] [21:59.36] like sweeping under the rug. So,
[L552] [22:02.32] >> so I guess going into your first major
[L553] [22:04.40] project after all those lowh hanging
[L554] [22:05.92] fruit, I understand there was a big
[L555] [22:08.48] redesign of the Instagram app called
[L556] [22:10.32] White Out. Can you talk about the story
[L557] [22:13.04] behind that project?
[L558] [22:14.16] >> Yeah, it was a couple months into my
[L559] [22:15.84] time there and it kind of got word that
[L560] [22:18.16] um we were working on a new icon which
[L561] [22:20.24] ended up being very controversial. Um,
[L562] [22:22.88] and as part of that, we were going to do
[L563] [22:24.80] like this kind of uh redesign of the
[L564] [22:27.20] app, a big visual refresh. And I don't
[L565] [22:31.60] remember exactly what I did, but I
[L566] [22:33.36] remember being like, I have to work on
[L567] [22:35.12] this thing. This is like, this sounds so
[L568] [22:37.20] cool. This is what I want to do. And,
[L569] [22:39.76] you know, I told my manager, I was like
[L570] [22:41.52] meeting the designers that were working
[L571] [22:42.96] on it. Um, so I basically just
[L572] [22:44.96] maneuvered myself in into working on
[L573] [22:47.68] this project. And uh the the main
[L574] [22:51.04] designer on it, Joy Vincent, um who was
[L575] [22:53.92] just like yeah, just an incredible
[L576] [22:56.88] talent and the nicest guy ever. Really
[L577] [22:59.68] sad. He he passed away while we were at
[L578] [23:01.84] Instagram. Um but um I sat in a war room
[L579] [23:07.28] um you know just like a conference room
[L580] [23:10.08] basically uh with him for I think
[L581] [23:14.08] probably two or three months and just
[L582] [23:16.32] every day we'd be like okay new screen
[L583] [23:18.48] and app we'd go look at it. He'd be like
[L584] [23:20.64] all right I want to do this this this
[L585] [23:22.08] and I would do that and I' you know pass
[L586] [23:23.68] the phone over to him and just back and
[L587] [23:26.40] forth like that. Um, you know, we
[L588] [23:28.27] [clears throat] we did kind of a whole
[L589] [23:30.40] new color palette for the app, new
[L590] [23:32.24] icons. Um, and one of the goals was to
[L591] [23:38.00] really make all of the focus in
[L592] [23:39.92] Instagram on the content on the photos
[L593] [23:42.16] and the videos and to take all the color
[L594] [23:44.88] out of the chrome. And it's basically,
[L595] [23:47.84] you know, how Instagram looks today. But
[L596] [23:49.60] at that time, you know, we had this kind
[L597] [23:51.60] of dark blue and black chrome everywhere
[L598] [23:54.64] in the app. and uh things were have a
[L599] [23:57.44] lot heavier um and uh yeah so we just
[L600] [24:01.12] tried to to really simplify it down and
[L601] [24:03.76] make all the color come from the content
[L602] [24:05.84] itself.
[L603] [24:06.88] >> Was it a gated launch or was it a just
[L604] [24:09.28] launch it all at once kind of project?
[L605] [24:11.68] >> So AB testing was like pretty new at
[L606] [24:13.92] Instagram at that point. Um you Facebook
[L607] [24:16.40] was was doing a lot of it and Instagram
[L608] [24:18.72] was kind of more the like oh we know
[L609] [24:20.24] what's good so we'll just ship it. And
[L610] [24:23.76] uh when I started working on on this
[L611] [24:26.56] project, the the CTO and co-founder of
[L612] [24:28.80] Mike Creger, he he was like, "You know
[L613] [24:31.28] what? Don't don't worry about trying to
[L614] [24:32.88] AB test this thing." He's like, "Just
[L615] [24:35.44] just ship it. Like build it and ship
[L616] [24:37.28] it." Um, and actually at that time like
[L617] [24:41.44] they were still sort of using branching
[L618] [24:43.36] as like a way to to build big features,
[L619] [24:46.00] but I had seen some longived branches
[L620] [24:50.08] uh like the the um direct messaging
[L621] [24:53.36] feature had been built as a as a longive
[L622] [24:56.32] branch and it was a nightmare merging it
[L623] [24:58.72] back in because they branched off for
[L624] [25:00.08] like 3 months and weren't really
[L625] [25:01.92] rebasing and then they you know merge
[L626] [25:03.52] this thing back in. It was it was I
[L627] [25:05.60] think pretty awful and and this redesign
[L628] [25:07.60] touched literally every surface of of
[L629] [25:09.68] the app. Um so I was kind of like well
[L630] [25:12.16] this is not going to be a good way to
[L631] [25:14.00] build it. So I put it behind kind of a
[L632] [25:16.00] feature flag and was constantly merging
[L633] [25:18.24] it and had to build abstractions like
[L634] [25:21.52] all the colors became semantic colors.
[L635] [25:23.76] So you know um it's like instead of
[L636] [25:27.60] saying that icon is black it's like it's
[L637] [25:29.68] icon color or something like that. um or
[L638] [25:32.80] it's disabled icon color and then you
[L639] [25:35.60] could switch inside of that function for
[L640] [25:38.32] you know are we on the new design or the
[L641] [25:40.08] old design. Um [snorts] and so that
[L642] [25:42.56] ended up being just kind of a much
[L643] [25:44.16] easier way to to build it incrementally.
[L644] [25:46.80] And then it also actually opened up the
[L645] [25:48.96] possibility of testing it. Um and so we
[L646] [25:52.56] we went to to ship it and it was going
[L647] [25:55.52] to be just like a 2% hold out. So, like,
[L648] [25:58.88] you know, we were going to ship the new
[L649] [26:00.40] icon. Um, it 98% of people were going to
[L650] [26:04.08] have the new design and then we were
[L651] [26:06.40] just going to have like 2% of people,
[L652] [26:08.96] you know, with the old design just to
[L653] [26:11.20] make sure that like nothing was was
[L654] [26:13.20] broken or changed drastically. And uh I
[L655] [26:16.56] had submitted the app to Apple. I I
[L656] [26:18.80] dropped in the new icon. You know, we
[L657] [26:20.40] were ready to go. People had champagne
[L658] [26:22.24] ready for the launch party. And it was
[L659] [26:23.68] like the night before we were supposed
[L660] [26:25.60] to to launch this thing. And um someone
[L661] [26:30.64] kind of in the Facebook executive ex
[L662] [26:32.96] executive team above uh Instagram came
[L663] [26:37.04] in and was like no [snorts] you guys are
[L664] [26:39.04] not doing this.
[L665] [26:41.04] Um I guess they Facebook had had a
[L666] [26:43.52] redesign that went poorly. Um and they
[L667] [26:47.36] just saw this as the same thing and uh
[L668] [26:50.64] and so they were like you need to run AB
[L669] [26:52.56] tests of this up front. Um, so I I was
[L670] [26:55.60] up at like 1:00 a.m. just like backing
[L671] [26:57.60] things out and trying to like resubmit
[L672] [26:59.44] the app to Apple and uh we we tested it.
[L673] [27:03.84] I actually tested really well. Um
[L674] [27:06.38] [clears throat] was a little bit sad
[L675] [27:07.52] because it kind of crushed like the
[L676] [27:09.20] launch that we we had planned. Um you
[L677] [27:12.08] know cuz then there are all these
[L678] [27:13.76] articles about this new UI that
[L679] [27:15.76] Instagram's maybe going to do. Um
[L680] [27:18.17] [snorts] but uh but yeah, I mean it all
[L681] [27:20.80] worked out. Um but I I did have a a
[L682] [27:24.48] takeaway from that which is like um I
[L683] [27:27.28] mean testing definitely has a a place.
[L684] [27:30.80] It's extremely useful even in our
[L685] [27:32.64] startup you know we test things where
[L686] [27:35.36] you sometimes get counterintuitive
[L687] [27:37.44] results um things in our onboarding flow
[L688] [27:40.56] how people convert on things um it's
[L689] [27:43.44] extremely useful to run AB tests for
[L690] [27:45.36] that I think for like highle product
[L691] [27:48.24] direction and like what you want the
[L692] [27:49.84] thing to be I I prefer to come in with a
[L693] [27:52.56] a stronger opinion and not just kind of
[L694] [27:55.12] like um look at the look at the data and
[L695] [27:58.88] only let the the data guide the
[L696] [28:01.20] decisions.
[L697] [28:02.72] Um, so I I think there's a risk if you
[L698] [28:06.24] do too much experimentation that you get
[L699] [28:08.00] trapped in kind of incrementalism.
[L700] [28:10.24] So it's, you know, easy to get those 1%
[L701] [28:12.40] wins, but you're never going to get that
[L702] [28:14.24] 50% uh jump.
[L703] [28:16.64] >> On the major redesign case though, if
[L704] [28:19.20] you just went for it though too, there's
[L705] [28:21.60] also the other side risk though, right?
[L706] [28:23.36] which is your product taste might be off
[L707] [28:26.96] and people hate it and then it's a a
[L708] [28:29.76] pain to come back.
[L709] [28:31.28] >> Yeah. Yeah, for sure. Um I I think we we
[L710] [28:36.80] had enough confidence I guess in in
[L711] [28:38.96] using it. I mean it felt really good
[L712] [28:40.80] internally and um I think at least on
[L713] [28:45.36] the inter in kind of redesigning the
[L714] [28:47.76] app, we we thought that would be good.
[L715] [28:49.84] Um the icon was definitely a little bit
[L716] [28:51.76] more controversial and then when we
[L717] [28:54.24] shipped that people hated it. I mean it
[L718] [28:57.36] was like I say it's the last time I
[L719] [28:58.88] looked at Twitter after our product
[L720] [29:00.24] launch because I went on and you know it
[L721] [29:02.80] was supposed to be the celebratory day.
[L722] [29:04.32] We had worked so hard on this thing. it
[L723] [29:05.76] went out and we were just getting raked
[L724] [29:08.16] on Twitter and uh yeah I mean it was it
[L725] [29:12.24] was kind of sad but I think you know
[L726] [29:14.88] change is hard. Um especially I think
[L727] [29:18.24] people feel ownership over their home
[L728] [29:20.32] screens and and all of a sudden this
[L729] [29:22.64] thing just changed on them. Um and
[L730] [29:25.24] [snorts] it was kind of like a a little
[L731] [29:27.44] bit more of a bleeding edge design
[L732] [29:28.96] direction too. Like I think the the flat
[L733] [29:31.20] icon and the gradient, you know, today
[L734] [29:33.52] feels very at home, but at that time a
[L735] [29:36.16] lot of the icons were pretty skephic and
[L736] [29:38.08] 3D. Yeah. So so it was a bit rough. The
[L737] [29:41.60] the funny other thing from that, you
[L738] [29:44.00] know, we could see from the data
[L739] [29:45.60] actually that uh this icon change uh it
[L740] [29:49.76] materially improved how many people a
[L741] [29:52.48] day open the app. Um, and we've actually
[L742] [29:56.32] seen this in in um the app of my new
[L743] [30:00.16] company called Retro, but actually like
[L744] [30:02.80] the icon uh can impact whether people
[L745] [30:06.48] open the app like how visible it is to
[L746] [30:08.40] them on on the screen. So, it became
[L747] [30:10.64] more noticeable I think amongst the
[L748] [30:12.32] other icons and people actually uh
[L749] [30:15.84] tapped it more often. It reminds me of I
[L750] [30:18.80] think some of Thomas Dimson's work on
[L751] [30:21.36] the ranking versus chronological
[L752] [30:25.36] like the public perception is so
[L753] [30:27.52] different from how actually people are
[L754] [30:30.48] voting with their usage. Like people are
[L755] [30:32.88] using it a lot more when it's when it's
[L756] [30:34.88] ranked but you know for some reason
[L757] [30:37.20] there's this like very vocal minority
[L758] [30:39.20] that is saying I absolutely hate this.
[L759] [30:42.40] >> Totally. Yeah. that that actually um the
[L760] [30:45.12] feed ranking um shipped about the same
[L761] [30:47.76] time as as this redesign and
[L762] [30:51.44] uh I mean I was actually skeptical of it
[L763] [30:53.92] as well. Um the the metric that changed
[L764] [30:58.40] my mind on the ranking which I think the
[L765] [31:01.20] story might be a little bit different
[L766] [31:02.40] today but um [snorts]
[L767] [31:04.72] at the time uh one of the things that
[L768] [31:07.12] moved was actually how often people
[L769] [31:09.20] shared to Instagram. So people that had
[L770] [31:12.56] this uh feed ranking experience were
[L771] [31:15.04] actually creating more themselves. They
[L772] [31:16.96] were sharing more. Um and it was partly
[L773] [31:19.92] because the feed ranking allowed uh
[L774] [31:22.88] Instagram to show them their friends
[L775] [31:25.28] more often. Um and so you saw content
[L776] [31:30.08] from people like you and I think you
[L777] [31:32.96] wanted to have that mutual connection so
[L778] [31:34.56] you would actually share more yourself.
[L779] [31:36.72] And so that kind of was an insight that
[L780] [31:39.36] flipped it in my mind where, you know,
[L781] [31:42.08] cuz people would say, "Oh, I'm just
[L782] [31:43.60] using the app more because like you're
[L783] [31:45.04] not showing me the things I want, so I'm
[L784] [31:46.64] scrolling further or whatever." But I
[L785] [31:48.80] was kind of like, "Okay, they're
[L786] [31:49.84] actually like creating more content."
[L787] [31:51.36] That that's kind of hard to dispute.
[L788] [31:53.36] Like that's that's probably a good
[L789] [31:55.12] thing. Um I I really liked uh kind of
[L790] [32:00.00] the mission the original mission of
[L791] [32:01.60] Instagram was like capture and share the
[L792] [32:03.44] world's moments. And I I really liked it
[L793] [32:05.36] as a way to kind of encourage people to
[L794] [32:08.40] be creative and see beauty in the world.
[L795] [32:11.36] And that was just a mission I felt like
[L796] [32:13.28] I could get behind. And so something
[L797] [32:15.76] like this where people were actually
[L798] [32:17.84] creating more, I was like, "Okay, yeah,
[L799] [32:19.36] that that that's probably a good thing."
[L800] [32:21.28] I think at this leg of your career, I
[L801] [32:23.28] think one thing that you wrote you wrote
[L802] [32:25.44] about is that, you know, finding an
[L803] [32:27.68] amazing designer was like a big part of
[L804] [32:29.60] it for you. And so I'm curious, how did
[L805] [32:32.56] you find the amazing designer that you
[L806] [32:35.12] did work with and what makes a great
[L807] [32:37.52] designer great?
[L808] [32:38.72] >> Yeah, I've always just tried to, you
[L809] [32:40.24] know, be be the engineer that like the
[L810] [32:42.40] top designers want to work with. Um, and
[L811] [32:47.28] yeah, it's just an incredible
[L812] [32:48.96] opportunity if you work at these types
[L813] [32:50.32] of companies where you can just have
[L814] [32:52.56] their work kind of flow through you. Um,
[L815] [32:55.12] be a part of it. Um so that for product
[L816] [32:58.56] engineers that that's one piece of
[L817] [33:00.24] advice I often give is like um your
[L818] [33:03.38] [clears throat] impact can be multiplied
[L819] [33:05.20] so much by finding a good designer and
[L820] [33:08.56] and creating a really good working
[L821] [33:10.40] relationship with them.
[L822] [33:11.76] >> Is there a reason why you say
[L823] [33:14.48] specifically the design function versus
[L824] [33:16.64] the engineering function? Like imagine I
[L825] [33:19.04] I identify some very senior engineer
[L826] [33:22.16] that has some engineering design and I
[L827] [33:24.80] just devote myself to it and kind of
[L828] [33:26.88] attach to them. What's the difference
[L829] [33:28.96] between doing that versus the really
[L830] [33:31.12] talented designer? So I should make a
[L831] [33:33.68] bit of a distinction between like if
[L832] [33:35.52] you're in sort of a product engineering
[L833] [33:37.60] um function where you're you're working
[L834] [33:39.28] on like the features for users, the
[L835] [33:41.52] interface kind of the front end then I
[L836] [33:43.36] think like you know that's where you
[L837] [33:45.20] really want to pair with a designer. If
[L838] [33:47.20] you're in a more infrastructure role,
[L839] [33:49.28] maybe the analogy is like finding that
[L840] [33:51.76] really talented um super senior engineer
[L841] [33:55.44] uh and and being the engineer they want
[L842] [33:58.32] to work with. Um you know, they've got
[L843] [34:01.20] great ideas and you can kind of
[L844] [34:03.20] implement that. So yeah, probably
[L845] [34:04.88] different depending on kind of uh what
[L846] [34:07.28] role you have.
[L847] [34:08.88] >> And so this white out project was in
[L848] [34:10.96] 2016. I'm kind of surprised in the same
[L849] [34:13.76] year you also built stories with Tiger
[L850] [34:17.68] Squad of some very famous people I'm
[L851] [34:19.44] aware of. Can you tell me the story
[L852] [34:21.28] about you know building stories for
[L853] [34:23.92] Instagram?
[L854] [34:24.64] >> Uh the redesign wrapped up and um I had
[L855] [34:28.56] actually been kind of kicked off my my
[L856] [34:31.44] uh previous team. Um right after I
[L857] [34:35.20] joined they said we're moving the team
[L858] [34:36.64] to New York. Do you want to move to New
[L859] [34:38.08] York? And I was like no.
[L860] [34:41.68] I I kind of I'm okay here in California.
[L861] [34:44.24] They're like, "Okay, that's fine. Well,
[L862] [34:45.44] you just have to find a new team." I was
[L863] [34:46.96] like, "Okay, I I kind of wanted to be on
[L864] [34:49.84] this team." Um so, um I kind of like
[L865] [34:53.60] delayed it. I worked on this uh redesign
[L866] [34:56.16] project and um then I joined the search
[L867] [34:59.52] and explore team. Um, and I was only on
[L868] [35:04.56] the team for a couple of weeks and a
[L869] [35:08.40] friend of mine, um, who was also an iOS
[L870] [35:11.60] engineer at the company decided to quit
[L871] [35:14.16] and he had been working on what was
[L872] [35:16.08] called the creation team and leading the
[L873] [35:18.96] project that would become stories. And
[L874] [35:22.56] uh my manager um was like, "Hey, you
[L875] [35:27.12] know, this is actually a really
[L876] [35:28.72] important effort for the company. Like,
[L877] [35:31.84] I don't necessarily want you to lead my
[L878] [35:33.76] team, but like I think this is a good
[L879] [35:35.12] opportunity for you." And um I really
[L880] [35:37.76] believed in in what this team was trying
[L881] [35:39.60] to do. Um, at that time it it's sort of
[L882] [35:44.56] surprising in hindsight given how big
[L883] [35:46.56] Instagram is today, but it actually felt
[L884] [35:49.04] in some ways like Instagram was dying
[L885] [35:51.60] because a lot of the sort of everyday
[L886] [35:54.32] sharing uh from people you knew, normal
[L887] [35:57.36] people was evaporating. It was kind of
[L888] [36:01.44] being replaced by creators and
[L889] [36:03.76] influencers.
[L890] [36:05.28] And uh some of that everyday sharing was
[L891] [36:08.24] going to Snapchat which had this
[L892] [36:09.76] ephemeral format. Um [snorts] and so we
[L893] [36:13.12] were tasked with just you know how do we
[L894] [36:15.60] get kind of normal people to feel
[L895] [36:18.16] comfortable sharing to Instagram again.
[L896] [36:20.80] So I I went over to to lead the iOS team
[L897] [36:24.40] on stories and
[L898] [36:27.28] uh one of the first things we did after
[L899] [36:30.48] I joined the team is we actually cut the
[L900] [36:32.48] team size significantly. So there had
[L901] [36:35.12] been a lot of people working on it. It
[L902] [36:36.80] had been pretty churny. Um they had
[L903] [36:39.20] tried different product directions. Uh a
[L904] [36:41.92] lot of them didn't really feel that
[L905] [36:44.32] great. They weren't working out. And in
[L906] [36:47.84] some ways they were working on things to
[L907] [36:49.84] have work for people to do um or or
[L908] [36:54.00] there was just like not um not enough
[L909] [36:56.64] space for the people that were there.
[L910] [36:58.08] And we just decided, hey, we can
[L911] [36:59.76] actually move a lot faster if we go down
[L912] [37:02.00] to a smaller team. So, uh, it was myself
[L913] [37:05.12] and one other iOS engineer was kind of
[L914] [37:06.88] like the core team, and then we'd get
[L915] [37:08.40] some help from other iOS engineers, two
[L916] [37:11.04] Android engineers, and we didn't even
[L917] [37:12.88] have a dedicated server engineer. It was
[L918] [37:15.76] the infrastructure team, or like you can
[L919] [37:18.00] have half a person. Um, it's half their
[L920] [37:21.04] time. Uh, which, you know, for what
[L921] [37:24.48] stories has become, it's it seems kind
[L922] [37:26.32] of crazy. Uh, but it it really allowed
[L923] [37:28.80] us to to move quickly. Um, you had
[L924] [37:31.92] ownership over the whole thing. So, it's
[L925] [37:33.60] never like a question of am I working on
[L926] [37:35.92] something that someone else is working
[L927] [37:37.28] on, am I going to step on their toes?
[L928] [37:39.52] You know, if there's a bug, it's like,
[L929] [37:41.28] okay, that's that's my bug. I got to go
[L930] [37:43.20] fix it. And uh and there was less
[L931] [37:47.76] discussion around decisions, we could
[L932] [37:49.68] just make them more quickly. I say like
[L933] [37:51.92] if you want to go fast, go small. Uh and
[L934] [37:54.56] I'm a a strong believer in small teams
[L935] [37:57.12] as like really the best way to operate.
[L936] [37:59.68] Um it's definitely not the only way to
[L937] [38:02.32] operate, but it's my preferred way. And
[L938] [38:04.72] uh yeah, so we we went through that and
[L939] [38:07.36] um we built it just over two to three
[L940] [38:10.32] months. Was pretty quick. I
[L941] [38:14.72] never worked so hard in my life. I was
[L942] [38:18.56] working Yes. like 16 18 hour days, 7
[L943] [38:22.00] days a week. Uh in the office every
[L944] [38:25.04] weekend.
[L945] [38:26.64] Yeah. I would like leave at like 1 or 2
[L946] [38:29.68] a.m. to go home. I was driving back and
[L947] [38:31.92] forth from San Francisco. I I was really
[L948] [38:34.48] determined to not sleep in the office. I
[L949] [38:36.48] was like, you know what? I'm always
[L950] [38:37.84] going to go home, see my girlfriend. And
[L951] [38:40.56] it was kind of silly because I was
[L952] [38:42.08] spending this extra time driving. I
[L953] [38:43.60] really should have just slept in the
[L954] [38:44.88] office. Uh but um yeah, it was intense,
[L955] [38:49.52] but it was fun. It felt like we were
[L956] [38:51.20] building something really important and
[L957] [38:54.72] we were using the product ourselves. We
[L958] [38:57.36] were really enjoying it. It also was
[L959] [38:59.60] like this bonding experience amongst
[L960] [39:01.44] this small team. So our PM on the
[L961] [39:04.40] project is now my co-founder at at my
[L962] [39:07.20] company and
[L963] [39:10.08] um you know I'm very close still with
[L964] [39:12.72] with uh the other folks that worked on
[L965] [39:15.52] it. And it also it felt in it's funny
[L966] [39:19.44] because in some ways we were kind of the
[L967] [39:22.48] incumbent to to Snapchat, but in other
[L968] [39:25.12] ways they were very much winning in
[L969] [39:27.44] terms of this kind of like everyday
[L970] [39:29.04] sharing. And so we actually kind of felt
[L971] [39:32.24] like the underdog. We we had a poster
[L972] [39:34.56] up, a Ghostbusters poster up in our our
[L973] [39:37.52] war room. Um, and yeah, just it felt
[L974] [39:41.44] like we were kind of um [snorts] in this
[L975] [39:45.60] in this war against them and uh and I
[L976] [39:48.24] thought, you know, maybe we maybe we
[L977] [39:49.76] could win.
[L978] [39:51.12] >> What was it in your opinion that like
[L979] [39:53.04] when you look at those two products,
[L980] [39:54.64] what was it that the Instagram version
[L981] [39:56.56] was doing so much better than the
[L982] [39:57.92] Snapchat one? Yeah, I think we we had a
[L983] [40:01.52] sort of unfair advantage in that people
[L984] [40:03.44] already had their friend grafted on
[L985] [40:06.24] Instagram
[L986] [40:07.84] and the people that they wanted to share
[L987] [40:10.64] with, but we just kind of weren't giving
[L988] [40:13.12] them the right outlet um to to actually
[L989] [40:16.96] do that sharing. And so as soon as we
[L990] [40:19.44] had that, I think it really stopped the
[L991] [40:23.20] outward flow um to to go to Snapchat for
[L992] [40:27.20] that type of sharing. Um you know, I
[L993] [40:30.24] think we also did push the the format
[L994] [40:33.04] forward. Um certainly Snapchat deserves
[L995] [40:36.40] all the credit for coming up with this
[L996] [40:39.36] container that was a lot more
[L997] [40:40.72] comfortable. Um you know, it's kind of
[L998] [40:43.52] 24-hour, the content doesn't stick
[L999] [40:45.92] around forever. um full screen immersive
[L1000] [40:49.44] all those things. Uh but at the time
[L1001] [40:52.08] there was like a lot uh that exists in
[L1002] [40:55.52] both stories products today that was not
[L1003] [40:57.60] there in Snapchat. So um you
[L1004] [41:00.86] [clears throat] know even be able to
[L1005] [41:02.00] navigate backwards by tapping left on
[L1006] [41:04.48] the screen like that didn't exist. So I
[L1007] [41:06.72] think we brought a lot of nice touches
[L1008] [41:08.24] like that. Uh the hold to pause
[L1009] [41:10.80] something I mentioned in the career
[L1010] [41:12.32] notes. So, you know, I was using this
[L1011] [41:14.40] early version that we had built and
[L1012] [41:16.96] these things were autoplay and they were
[L1013] [41:18.96] kind of going by too quickly and just
[L1014] [41:21.12] like intuitively put my thumb on the
[L1015] [41:23.28] screen and wanted to pause it and it
[L1016] [41:26.16] didn't pause. So, I was like, "Oh, I can
[L1017] [41:27.60] just do that." So, then I I built the
[L1018] [41:29.92] hold to pause and you know, now that
[L1019] [41:32.56] just feels like a core part of the
[L1020] [41:34.40] navigation and and the format. Um so
[L1021] [41:38.24] yeah that that's another uh thing like
[L1022] [41:41.52] when I mentor engineers um I mean you
[L1023] [41:44.40] just have this power as an engineer to
[L1024] [41:46.88] just build your ideas like if you are
[L1025] [41:49.04] using something and you think it should
[L1026] [41:50.64] work a different way you can just go do
[L1027] [41:52.08] that and that's that's such an awesome
[L1028] [41:53.68] thing. Um, and so, uh, I encourage, you
[L1029] [41:57.68] know, for sure product engineers, it's
[L1030] [41:59.52] like if you have ideas, just just build
[L1031] [42:02.24] them and put them out and have people
[L1032] [42:04.24] try them. And, uh, it's it's such a cool
[L1033] [42:07.52] thing to be able to do.
[L1034] [42:09.60] >> It's insane that you were you were
[L1035] [42:11.36] commuting from San Francisco to Menel
[L1036] [42:13.60] Park, so that's like almost an hour in
[L1037] [42:15.52] each direction. And you said you were
[L1038] [42:17.68] working 16 to 18 hours a day, about 7
[L1039] [42:21.04] days a week. I can't imagine what that
[L1040] [42:24.24] was like. One of the learnings from your
[L1041] [42:26.40] your note is that you should find work
[L1042] [42:28.72] that you care about deeply. I still
[L1043] [42:31.36] wonder were there times where you were
[L1044] [42:33.12] thinking I you care about the work but
[L1045] [42:34.80] that just as a human I can't imagine
[L1046] [42:38.16] surviving that kind of work schedule. I
[L1047] [42:40.96] mean, I I it probably wasn't 16 to 18
[L1048] [42:43.28] every day, but you know, it was
[L1049] [42:45.66] [clears throat] was working a lot for
[L1050] [42:47.12] sure. And and I definitely sacrificed
[L1051] [42:49.68] other parts of my life. Like I used to
[L1052] [42:51.92] be a very serious rock climber. I uh was
[L1053] [42:55.44] on the US team. I competed in World Cups
[L1054] [42:57.44] and I basically gave up that part of my
[L1055] [43:00.16] my life, you know, for sure in that
[L1056] [43:02.08] time. Um, but it was also such a unique
[L1057] [43:06.64] opportunity to like be able to build
[L1058] [43:09.04] this thing that was just going to go out
[L1059] [43:10.56] to hundreds of millions of people. And
[L1060] [43:14.08] uh, you know, one of the things I loved
[L1061] [43:16.64] most when I was working on Instagram is
[L1062] [43:18.48] I'd be like riding the Cal Train and I'd
[L1063] [43:21.04] look over someone's shoulder and I'd see
[L1064] [43:23.20] them using the thing I just built like a
[L1065] [43:25.36] week before and like that was such a
[L1066] [43:27.28] cool experience. So, uh, yeah, it was
[L1067] [43:30.88] like, you know, you sacrifice certain
[L1068] [43:32.64] things, but I was kind of happy to do
[L1069] [43:35.28] so. Uh, definitely not a sustainable
[L1070] [43:38.00] model. So, I wouldn't, you know, I
[L1071] [43:39.52] wouldn't recommend
[L1072] [43:41.36] doing that over a long period of time,
[L1073] [43:43.12] but in in stints, it can it can make
[L1074] [43:46.80] sense. And I think by
[L1075] [43:50.16] doing that work with that intensity, it
[L1076] [43:53.12] it paid dividends later on. So um the
[L1077] [43:57.12] stories Instagram stories product came
[L1078] [43:58.88] out. It was much better executed I think
[L1079] [44:01.92] than some of the other stories efforts
[L1080] [44:04.32] at the company. There were ones
[L1081] [44:05.68] happening in Facebook and in in
[L1082] [44:08.00] Messenger. I think part of that was just
[L1083] [44:10.40] the care that we put into it. It
[L1084] [44:13.52] contributed to its success. I think the
[L1085] [44:16.00] reception on launch was very positive. I
[L1086] [44:19.36] actually was really worried about it. I
[L1087] [44:21.12] thought the whole thing was just going
[L1088] [44:22.32] to crash and burn just because I could
[L1089] [44:24.80] see all these cracks in it. You know,
[L1090] [44:26.40] you you see the crash reports, you see
[L1091] [44:28.64] all the bugs, like you're kind of your
[L1092] [44:30.16] own harshest critic. But then when it
[L1093] [44:32.88] went out, people were like, "Wow, this
[L1094] [44:34.08] is so polished." And I was like,
[L1095] [44:35.20] "Really? Are we using the same thing?"
[L1096] [44:37.36] Um, but [snorts] uh yeah, it was it was
[L1097] [44:39.76] nice to have that reception. And uh so I
[L1098] [44:42.88] think it helped the product. And then
[L1099] [44:45.60] you know personally for my career having
[L1100] [44:50.40] kind of demonstrated that I could
[L1101] [44:52.64] deliver this project on a on a tight
[L1102] [44:54.80] timeline uh with this level of craft
[L1103] [44:58.32] helped me get on to you know the most
[L1104] [45:01.12] interesting projects going forward. I
[L1105] [45:03.60] saw at the end of the note it says you
[L1106] [45:05.20] you started at IC4 at Instagram and you
[L1107] [45:08.08] got to IC6 by the end of you know after
[L1108] [45:12.16] this gauntlet of these projects of white
[L1109] [45:14.64] out and stories. That's incredible. Like
[L1110] [45:17.12] one promo per half for two halves
[L1111] [45:19.44] straight. What was that like?
[L1112] [45:21.20] >> There's a bit bit of a funny story. Um
[L1113] [45:24.24] so the promotion cycle happened in July.
[L1114] [45:27.52] We we shipped stories at the beginning
[L1115] [45:29.36] of August. So calibrations were kind of
[L1116] [45:31.84] happening in in July and so we were in
[L1117] [45:35.28] the middle of this like very intense
[L1118] [45:37.12] project and I think like the there was a
[L1119] [45:42.24] lot of recognition of how hard we were
[L1120] [45:43.92] working. I think the managers like they
[L1121] [45:47.44] were being cautious around us and I knew
[L1122] [45:52.08] so I I felt fairly confident that I'd
[L1123] [45:55.44] been misleled on higher. I just wasn't
[L1124] [45:57.52] that familiar with levels when I came in
[L1125] [46:00.16] and I kind of looked around and I was
[L1126] [46:02.64] like, you know, I'm executing a lot
[L1127] [46:05.52] higher than I IC4.
[L1128] [46:08.24] um my Android counterpart uh who was an
[L1129] [46:11.60] incredible engineer, Will Bailey, he was
[L1130] [46:14.24] sort of the tech lead for the whole
[L1131] [46:15.76] stories uh project and he really like
[L1132] [46:18.56] set the example for me of like how you
[L1133] [46:20.80] could be a successful product engineer
[L1134] [46:23.44] and he was incredible at getting me into
[L1135] [46:25.68] the meetings and you know being in the
[L1136] [46:27.60] room with Mike and Kevin as we made all
[L1137] [46:29.28] the decisions. So he was an IC8. So I
[L1138] [46:32.24] kind of like, you know, we he certainly
[L1139] [46:35.04] had a bigger role on the project, but we
[L1140] [46:36.80] had some somewhat similar roles and was
[L1141] [46:39.44] like, "Okay, I'm you're at IC4, you're
[L1142] [46:41.12] at IC8." Um, and so that kind of opened
[L1143] [46:44.16] my eyes to to some of the leveling
[L1144] [46:46.24] stuff. So I told my manager at the time,
[L1145] [46:49.44] Eddie, uh, he he was he was the
[L1146] [46:53.12] director. So I was reporting to the
[L1147] [46:54.40] director just um because uh you know
[L1148] [46:57.60] it's kind of a unique project [snorts]
[L1149] [46:59.28] at the company and I was like hey I
[L1150] [47:02.48] think I got misleled and I think you
[L1151] [47:04.16] should promote me from four to six in
[L1152] [47:05.92] this cycle. [laughter]
[L1153] [47:08.08] >> Wow.
[L1154] [47:08.56] >> And uh to his credit like he didn't just
[L1155] [47:11.60] totally brush me off and be like you
[L1156] [47:13.92] know just dismiss it. He he said he
[L1157] [47:16.24] actually went and talked to HR about it
[L1158] [47:18.72] and they came back and they were like,
[L1159] [47:20.08] "We've done this twice in the history of
[L1160] [47:21.92] the company. In both cases, it worked
[L1161] [47:23.60] out terribly. The the people left um you
[L1162] [47:26.88] know, very quickly." Uh so he was like
[L1163] [47:29.60] he's like, "We're not going to do it."
[L1164] [47:31.12] But I kind of wanted to seed a little
[L1165] [47:33.44] bit that like, you know, probably the
[L1166] [47:36.16] correct level for me is is a higher IC6.
[L1167] [47:40.72] Um, and I knew it was unlikely that they
[L1168] [47:43.52] were just going to do that one step. Um,
[L1169] [47:46.08] but I I had a guess that like if I was
[L1170] [47:49.52] just on that normal cycle, you know, it
[L1171] [47:52.00] would come up the next time and they'd
[L1172] [47:53.52] be like, well, he just got promoted last
[L1173] [47:55.20] half like um you know, we we can wait.
[L1174] [47:58.32] Uh, and I think it's good for people to
[L1175] [48:02.40] recognize that ultimately these levels
[L1176] [48:06.08] and promotions, they're an incentive
[L1177] [48:08.32] system. I think in the long run like
[L1178] [48:10.56] there's really an effort to make it
[L1179] [48:12.32] fair. Um, but there's also an element of
[L1180] [48:15.52] like it's the carrot that's being
[L1181] [48:17.12] dangled in front of you, right? And so
[L1182] [48:20.24] it can actually make sense even if
[L1183] [48:21.92] somebody's performing at a higher level
[L1184] [48:23.60] that like the promotion gets delayed um
[L1185] [48:26.64] just so that they're not happening in
[L1186] [48:28.24] quick succession. So I kind of wanted to
[L1187] [48:29.84] like seed the idea that like you should
[L1188] [48:32.00] probably probably get me to six pretty
[L1189] [48:33.76] soon here. Um so yeah they they uh you
[L1190] [48:38.24] know the first half on um white out the
[L1191] [48:41.20] redesign and some of the infrastructure
[L1192] [48:44.00] stuff I got the IC5 promotion and then
[L1193] [48:48.32] uh the six came for stories.
[L1194] [48:51.20] >> It's interesting you say like your high
[L1195] [48:53.04] performance I mean you know of course
[L1196] [48:55.20] the promotions are one thing but one of
[L1197] [48:57.60] the things that you took away personally
[L1198] [48:59.28] was that it gave you freedom to work on
[L1199] [49:02.32] whatever projects you wanted. How does
[L1200] [49:04.48] that play out?
[L1201] [49:05.44] >> Yeah, I think it's just like
[L1202] [49:06.72] demonstrated that like, you know, if you
[L1203] [49:09.12] put me on a project, I'm going to do a
[L1204] [49:10.56] good job with it. And so when there is a
[L1205] [49:14.16] new effort at the company, you know,
[L1206] [49:16.80] it's just kind of a natural like, okay,
[L1207] [49:19.20] let's take the people that have done
[L1208] [49:21.12] well on the new efforts before. And um
[L1209] [49:25.12] yeah, so I mean I was very lucky to to
[L1210] [49:28.08] have the opportunity, but then like
[L1211] [49:29.60] executing well on it set me up well for
[L1212] [49:31.76] the future.
[L1213] [49:32.80] >> Yeah. you already left before the
[L1214] [49:34.48] Instagram threads, but I noticed a
[L1215] [49:36.24] similar model which is you pull together
[L1216] [49:38.80] all the the top Instagram people and you
[L1217] [49:42.08] got this small kind of similar like the
[L1218] [49:43.92] stories team and you know all those
[L1219] [49:46.00] people have proven themselves
[L1220] [49:47.12] repeatedly. So
[L1221] [49:48.64] >> and it's a very fun environment to be a
[L1222] [49:50.64] part of that kind of team. The next
[L1223] [49:52.32] promotion actually came from IGTV which
[L1224] [49:55.52] my understanding it's like a I mean I
[L1225] [49:58.00] was at the company at the time so it's
[L1226] [49:59.44] kind of like a YouTube clone almost or
[L1227] [50:01.60] like but vertical video first in
[L1228] [50:03.52] Instagram. Could you talk about that
[L1229] [50:05.60] project that got you promoted to IC7 or
[L1230] [50:08.24] senior staff?
[L1231] [50:09.20] >> So it was very much like uh uh came from
[L1232] [50:12.48] Kevin the CEO him and Ian Sber who's
[L1233] [50:16.24] another amazing designer. They before
[L1234] [50:20.24] like an end of year all hands had um
[L1235] [50:23.36] kind of designed this thing together
[L1236] [50:26.48] laid out this vision for uh Instagram
[L1237] [50:30.08] getting into
[L1238] [50:32.00] kind of longer form video was was the
[L1239] [50:34.48] pitch and it was going to be mobile
[L1240] [50:37.52] native so it was going to be vertical
[L1241] [50:39.12] the way that you hold your phone and uh
[L1242] [50:43.44] so they came actually with like a fairly
[L1243] [50:45.20] developed vision to all hands and kind
[L1244] [50:47.68] of surprised guys presented it to
[L1245] [50:49.60] everybody. It's like here's what we're
[L1246] [50:51.12] going to do. Yeah, I I saw that and
[L1247] [50:52.96] again I was like I got to work on this
[L1248] [50:54.40] thing. This looks cool. It ended up
[L1249] [50:57.28] being a bit of a weird project in the
[L1250] [50:59.52] beginning because um yeah, it was like
[L1251] [51:01.84] the surprise reveal. If you read through
[L1252] [51:04.64] some of the recent antitrust uh
[L1253] [51:07.12] litigation with Facebook, there's some
[L1254] [51:09.28] insights into tensions between Facebook
[L1255] [51:12.32] and Instagram during this time. like we
[L1256] [51:14.56] were told not to work on it for for a
[L1257] [51:16.56] while was kind of like the end of the
[L1258] [51:19.60] founders time at Instagram. IGTV was
[L1259] [51:21.76] kind of like the last thing that they or
[L1260] [51:24.48] last major thing they were there for. Um
[L1261] [51:27.20] but it was again a really cool group,
[L1262] [51:30.72] very small team. Myself, Will Bailey,
[L1263] [51:33.28] Thomas Dimpson, um and uh you know kind
[L1264] [51:37.84] of like iOS, Android and um server
[L1265] [51:41.60] leads. And then we each had like one or
[L1266] [51:44.24] two other uh people per platform
[L1267] [51:48.01] [snorts] and uh yeah just like super
[L1268] [51:50.88] talented group um great engineers, great
[L1269] [51:53.68] designers. Uh we moved super quickly. I
[L1270] [51:57.36] mean the product doesn't exist anymore
[L1271] [51:58.96] today. it didn't it didn't end up doing
[L1272] [52:00.96] that well. And it's kind of interesting
[L1273] [52:02.64] to reflect on why I think like it had
[L1274] [52:05.28] some things that uh ended up becoming
[L1275] [52:08.56] the future like vertical video is very
[L1276] [52:10.80] much a thing today. Um but it was kind
[L1277] [52:13.28] of trying to mix like this long form
[L1278] [52:15.84] YouTube style content into this vertical
[L1279] [52:18.24] format and maybe that was a bit of a
[L1280] [52:20.16] mismatch. Uh people just weren't
[L1281] [52:23.12] producing highquality long form in the
[L1282] [52:26.80] vertical format. We tried some
[L1283] [52:30.80] interesting AI techniques to take
[L1284] [52:33.20] landscape content and reformat it for
[L1285] [52:35.84] vertical. I've got a patent on that.
[L1286] [52:37.84] That's kind of one of my more
[L1287] [52:39.20] interesting patents. Um [clears throat]
[L1288] [52:41.92] but uh we showed that to create video
[L1289] [52:45.20] creators and they were like horrified.
[L1290] [52:46.88] They were like, "You're destroying my
[L1291] [52:48.40] content. Like why? I've spent so long
[L1292] [52:50.16] making this nice landscape video now.
[L1293] [52:52.32] You've just ruined it." So, we tried to
[L1294] [52:54.48] push people to produce this original
[L1295] [52:56.72] long- form vertical video. And I think
[L1296] [52:58.40] the inventory just never really showed
[L1297] [53:00.88] up. And there was maybe a little bit of
[L1298] [53:02.88] hubris. It was like, you know, Instagram
[L1299] [53:05.60] can just change the industry. We can
[L1300] [53:07.76] just people will just start making this
[L1301] [53:10.08] because we have this platform, this
[L1302] [53:11.92] audience. And that didn't totally
[L1303] [53:14.16] materialize. So, I think it probably did
[L1304] [53:17.36] inform a lot of like, you know, what
[L1305] [53:19.20] ultimately shipped as as reals. Um but
[L1306] [53:23.52] uh yeah, IGTV itself didn't didn't
[L1307] [53:26.64] totally work out.
[L1308] [53:27.92] >> Yeah, I was cuz I was working on the
[L1309] [53:29.92] like video infrastructure team at the
[L1310] [53:31.76] time. So actually that was one of the
[L1311] [53:33.76] things that I got plugged into at some
[L1312] [53:35.36] point. I remember the energy in the San
[L1313] [53:38.24] Francisco office and the war rooms etc.
[L1314] [53:41.12] >> Yeah, totally.
[L1315] [53:42.40] >> You mentioned antitrust and what's the
[L1316] [53:45.12] antirust component you're talking about?
[L1317] [53:47.44] a lot of the sort of internal
[L1318] [53:50.08] communication has now become public
[L1319] [53:52.00] through this antirust uh lawsuit where
[L1320] [53:56.96] um the Justice Department I think is is
[L1321] [54:00.24] suing Facebook to unwind the Instagram
[L1322] [54:03.44] acquisition. Um, and so certain things
[L1323] [54:07.44] that were kind of confusing to me at the
[L1324] [54:09.36] time, like why why were certain things
[L1325] [54:11.76] happening, um, are less confusing now
[L1326] [54:14.96] that I read some of the the internal
[L1327] [54:17.84] communications that was previously
[L1328] [54:19.28] private, including private to me. You
[L1329] [54:21.20] know, I didn't I wasn't exposed, uh, to
[L1330] [54:24.00] it. But, um, yeah, I mean, I think
[L1331] [54:26.32] basically
[L1332] [54:27.84] Instagram, you know, had been acquired.
[L1333] [54:30.24] It was it was smaller,
[L1334] [54:33.28] certainly small relative to Facebook and
[L1335] [54:36.00] then had gone through several years of
[L1336] [54:38.00] just incredible growth and now was kind
[L1337] [54:43.12] of more of like a peer to Facebook and
[L1338] [54:46.88] was kind of like the new popular kid
[L1339] [54:50.32] terms of like you know the Instagram
[L1340] [54:51.92] stories was received better than the
[L1341] [54:54.48] stories in Facebook. And so I think that
[L1342] [54:58.24] created some tension between the
[L1343] [55:00.80] Instagram leadership and the Facebook
[L1344] [55:02.40] leadership. And there was concerns about
[L1345] [55:05.68] Instagram cannibalizing or taking users
[L1346] [55:08.40] from Facebook. Um
[L1347] [55:11.60] which yeah just kind of guided some of
[L1348] [55:14.40] the the
[L1349] [55:16.64] strategy decisions I guess. I remember
[L1350] [55:19.12] that too because I was I mean I was also
[L1351] [55:20.88] on the Instagram team and I remember
[L1352] [55:23.04] there was some confusion about you know
[L1353] [55:25.36] why are we turning off the I guess
[L1354] [55:28.72] somehow like followers were being
[L1355] [55:30.48] forwarded from Facebook to Instagram or
[L1356] [55:33.20] was like cross sharing or something like
[L1357] [55:35.12] the direction from Facebook to Instagram
[L1358] [55:37.68] was getting turned off or something like
[L1359] [55:39.28] that and yeah I think I read the same
[L1360] [55:41.92] thing you read because I was like oh
[L1361] [55:43.44] this makes so much sense it's like Mark
[L1362] [55:45.44] Zuckerberg's internal memo on you know
[L1363] [55:48.56] all of that and all the tensions between
[L1364] [55:51.84] you know the Instagram founders Mark and
[L1365] [55:54.24] he's saying
[L1366] [55:55.04] >> he wants to keep them and they're great
[L1367] [55:56.88] at building products but you know he's
[L1368] [55:59.52] like trying to navigate his side of the
[L1369] [56:01.92] equation. Super interesting.
[L1370] [56:03.92] >> It'd be really interesting to know how
[L1371] [56:06.80] you know how he thinks about it today.
[L1372] [56:09.36] Uh that was now seven years ago.
[L1373] [56:12.64] >> Mark or the Instagram founders? Mark. Um
[L1374] [56:16.64] because I sense in those communications
[L1375] [56:20.40] like something of a very understandable
[L1376] [56:23.92] emotional attachment to the Facebook
[L1377] [56:25.84] product, right? This was like kind of
[L1378] [56:27.60] the thing that he created and Instagram.
[L1379] [56:30.40] He deserves all the credit for acquiring
[L1380] [56:32.56] it, but it was a little bit less his
[L1381] [56:34.56] thing. Um,
[L1382] [56:37.12] and yeah, I just wonder, uh, does he
[L1383] [56:40.80] view that differently today than he did
[L1384] [56:44.40] now? Uh, you know, seven years on, um,
[L1385] [56:48.16] he owns both of these things. Um, I
[L1386] [56:51.76] always had the view that like the best
[L1387] [56:54.72] the way to get the best outcome for the
[L1388] [56:57.84] overall company was actually to have
[L1389] [57:00.56] these things compete with each other
[L1390] [57:02.24] because it's like you own both. they're
[L1391] [57:04.24] going to make each other better and you
[L1392] [57:06.08] know one of them will win versus like if
[L1393] [57:07.84] you don't if you [clears throat] kind of
[L1394] [57:09.44] stifle that competition
[L1395] [57:11.60] somebody from the outside is like more
[L1396] [57:13.68] likely to come up with something better
[L1397] [57:15.60] and and take over. [snorts] Um but uh
[L1398] [57:20.32] yeah I don't know I mean he's the one
[L1399] [57:22.64] running a multi-trillion dollar company
[L1400] [57:24.56] and [laughter] I'm not so arm armchair
[L1401] [57:27.76] CEOing over here.
[L1402] [57:30.24] >> Yeah. Maybe one day if this podcast
[L1403] [57:32.72] scales up and I ever have Mark on, I'll
[L1404] [57:35.28] I'll ask him that. [laughter]
[L1405] [57:37.36] >> And then lastly at Instagram, I know you
[L1406] [57:40.40] started a group called IG Labs. I'm
[L1407] [57:42.96] curious the story behind you starting
[L1408] [57:45.04] that group and I also understand this is
[L1409] [57:47.52] your promo to IC8 or like director
[L1410] [57:50.72] equivalent at Instagram. So yeah, what's
[L1411] [57:53.28] the story behind IGLabs? after IGTV. Um,
[L1412] [57:59.04] definitely spent some time like Thomas
[L1413] [58:02.32] Simpson has this phrase like wandering
[L1414] [58:04.00] the impact desert like just looking for
[L1415] [58:08.08] for things to do and and not necessarily
[L1416] [58:11.68] finding anything great. Um, and I was
[L1417] [58:14.48] actually pretty close to to leaving the
[L1418] [58:17.04] company at that time. Um, [snorts]
[L1419] [58:20.32] and kind of the new effort became reals
[L1420] [58:24.08] and I didn't feel good about working on
[L1421] [58:26.72] like passive video consumption. Um, my
[L1422] [58:29.28] manager was was over the reals or so, so
[L1423] [58:32.72] it, you know, would have made sense for
[L1424] [58:34.32] me to work on it, but I was I was fairly
[L1425] [58:36.96] certain I I I didn't want to work on
[L1426] [58:39.04] that. I I helped the team a bit, but
[L1427] [58:41.20] like um yeah, it wasn't going to be my
[L1428] [58:43.92] project. Through that time, there was a
[L1429] [58:46.32] lot of like culture change. the founders
[L1430] [58:48.48] had left. Um, you know, the leadership
[L1431] [58:51.60] kind of came over from Facebook,
[L1432] [58:55.28] uh, the new leadership. Um, a lot of
[L1433] [58:58.56] kind of like the old Instagram culture,
[L1434] [59:00.72] it felt like was being kind of pushed
[L1435] [59:02.56] out.
[L1436] [59:04.08] And I was talking with like the the new
[L1437] [59:08.64] head of engineering um [snorts] about
[L1438] [59:12.80] trying to bring back some of that energy
[L1439] [59:15.28] that I think had made product
[L1440] [59:17.12] development at Instagram special, small
[L1441] [59:20.08] teams, attention to craft, uh and also
[L1442] [59:23.60] really expanding
[L1443] [59:25.60] kind of the
[L1444] [59:27.68] the scope of what we worked on. So, you
[L1445] [59:32.40] know, we were very focused on like the
[L1446] [59:34.96] existing Instagram app and the existing
[L1447] [59:36.96] features within Instagram and just kind
[L1448] [59:38.88] of like iterative features on that, very
[L1449] [59:41.92] like incremental improvements. And I
[L1450] [59:45.68] kind of made this pitch that like we
[L1451] [59:47.12] have this great brand um we could do
[L1452] [59:50.00] other things under the Instagram brand
[L1453] [59:51.92] like let's let's go try that. let's, you
[L1454] [59:54.88] know, explore like location ideas, maps
[L1455] [59:58.64] ideas, uh, places. Um, and again, paire
[L1456] [01:00:03.92] paired with a really awesome designer,
[L1457] [01:00:06.64] uh, Vivian Wong. And, um, we, yeah, made
[L1458] [01:00:10.88] the pitch to to start this team. It was
[L1459] [01:00:12.88] just her and myself in the beginning.
[L1460] [01:00:15.36] And uh the idea was just to have kind of
[L1461] [01:00:18.64] this like Delta Force like small group,
[L1462] [01:00:21.68] very high talent density that would work
[L1463] [01:00:23.84] on new product initiatives and things
[L1464] [01:00:26.00] that just didn't slot cleanly into the
[L1465] [01:00:28.64] org. Like Instagram had grown to such a
[L1466] [01:00:31.60] size where you really needed like a lot
[L1467] [01:00:34.80] of structure in the org just to keep
[L1468] [01:00:37.04] things sane. But that meant that
[L1469] [01:00:40.08] projects that like didn't slot cleanly
[L1470] [01:00:42.88] into one of those orgs were probably
[L1471] [01:00:45.28] underinvested in. And so part of the
[L1472] [01:00:47.84] idea of this team was that we would span
[L1473] [01:00:49.84] across, you know, we wouldn't have a
[L1474] [01:00:52.08] focus area. We could kind of work work
[L1475] [01:00:54.64] across many things. Um
[L1476] [01:00:57.44] we we tried a lot. I mean, a lot of it
[L1477] [01:00:59.68] didn't ship or tested. Um, probably one
[L1478] [01:01:02.96] of the more lasting impactful things, it
[L1479] [01:01:06.80] it seems small, but I think it actually
[L1480] [01:01:08.40] gets used quite a bit is the
[L1481] [01:01:09.60] collaborative post feature where uh you
[L1482] [01:01:12.48] can have multiple authors on a post. Um,
[L1483] [01:01:15.28] it's another of the more interesting
[L1484] [01:01:17.76] patents I have is is on that one. Um and
[L1485] [01:01:22.32] uh and so yeah, I think I think we found
[L1486] [01:01:24.24] good impact and then we were also this
[L1487] [01:01:25.68] concentration of talent that like when
[L1488] [01:01:27.28] there was a new important initiative
[L1489] [01:01:29.60] ultimately ended up being threads um you
[L1490] [01:01:32.88] had this group that that could go work
[L1491] [01:01:34.40] on it and uh and yeah just trying to uh
[L1492] [01:01:38.64] I don't know kind of encourage
[L1493] [01:01:40.80] innovation trying new things and and
[L1494] [01:01:43.20] push that at the company. The last thing
[L1495] [01:01:45.44] at your on your Instagram journey was
[L1496] [01:01:47.68] that you tried management at some point
[L1497] [01:01:50.32] or as an ICA you switched to I guess
[L1498] [01:01:53.20] TLDD or tech lead director. What was
[L1499] [01:01:56.96] your thinking behind that and how'd it
[L1500] [01:01:58.40] go?
[L1501] [01:01:58.96] >> It's a very unusual or rare role within
[L1502] [01:02:02.48] Facebook. Um even like TLM I think is
[L1503] [01:02:05.28] quite rare or was at the time um than
[L1504] [01:02:09.92] like tech lead director probably even
[L1505] [01:02:11.92] even more so. Um, [snorts]
[L1506] [01:02:15.44] it kind of happened mostly because I had
[L1507] [01:02:18.32] started this group and at some point it
[L1508] [01:02:21.36] just made a lot more sense for me to
[L1509] [01:02:23.20] manage the people in that group rather
[L1510] [01:02:25.68] than my manager who was over the reals
[L1511] [01:02:29.36] or um just less connected to to their
[L1512] [01:02:33.92] work. You know, I could probably
[L1513] [01:02:35.12] represent them better in calibrations. I
[L1514] [01:02:36.88] mean, I was in the calibrations anyways,
[L1515] [01:02:38.80] so I was kind of like doing a lot of
[L1516] [01:02:40.32] this work. So um yeah, in some ways it
[L1517] [01:02:43.52] was just kind of like a formal
[L1518] [01:02:45.04] recognition of like what I was doing
[L1519] [01:02:47.12] already. Um to to have these people
[L1520] [01:02:50.48] report to me. Um Facebook is is very
[L1521] [01:02:54.24] much of the school of thought of like
[L1522] [01:02:57.36] individual contributors and management
[L1523] [01:02:59.04] should be separate and I don't subscribe
[L1524] [01:03:02.88] to that. Um, other companies work
[L1525] [01:03:05.84] differently. Like my wife is a senior
[L1526] [01:03:07.68] staff engineer at Tesla and like um
[L1527] [01:03:10.96] they're very flexible. It's like
[L1528] [01:03:13.92] IC's have people report to them all the
[L1529] [01:03:15.68] time. Um, managers are expected to be
[L1530] [01:03:18.80] like pretty competent uh technical
[L1531] [01:03:22.08] contributors and like doing individual
[L1532] [01:03:23.92] contributions.
[L1533] [01:03:25.44] Um, and I think I prefer that model. Um,
[L1534] [01:03:30.80] and so it was interesting for me to to
[L1535] [01:03:34.00] try it. I think like another one of my
[L1536] [01:03:37.52] sort of controversial opinions is like I
[L1537] [01:03:39.60] think senior engineers should be
[L1538] [01:03:41.36] involved in coding. Um, [clears throat]
[L1539] [01:03:44.16] there's overlap between that thought and
[L1540] [01:03:46.48] like the thought that like um managers
[L1541] [01:03:49.28] should be still somewhat involved.
[L1542] [01:03:52.24] There's
[L1543] [01:03:54.00] an author I I really like, Nasim Talb.
[L1544] [01:03:56.56] Um and he talks about having skin in the
[L1545] [01:04:00.40] game and um yeah, I think like if you're
[L1546] [01:04:03.76] a senior IC who has to do some coding,
[L1547] [01:04:06.32] like you have more skin in the game.
[L1548] [01:04:07.76] Like you're not going to come up with
[L1549] [01:04:09.20] some architecture that like you just
[L1550] [01:04:11.52] hand off to somebody else and it's their
[L1551] [01:04:13.28] problem now, right? Like you're going to
[L1552] [01:04:15.04] be involved. You're going to see more
[L1553] [01:04:17.52] hands-on what the issues are. Um, and I
[L1554] [01:04:21.44] think like similarly like if you're
[L1555] [01:04:23.12] managing a team and you're much more
[L1556] [01:04:24.96] like with them in the day-to-day stuff,
[L1557] [01:04:28.80] uh, I think that you will operate
[L1558] [01:04:31.12] better. So, um, yeah, it's,
[L1559] [01:04:33.71] [clears throat] you know, maybe a bit
[L1560] [01:04:35.52] against the grain at Facebook. Um, but
[L1561] [01:04:38.88] it [clears throat] was a philosophy I
[L1562] [01:04:40.56] had and I wanted to to try it out. Um,
[L1563] [01:04:43.44] and then there was an upside to it as
[L1564] [01:04:46.24] well in a company that grew so much and
[L1565] [01:04:48.72] was so big where
[L1566] [01:04:52.48] at Facebook the levels are are private,
[L1567] [01:04:55.12] right? So you're just a software
[L1568] [01:04:56.80] engineer through through your whole IC
[L1569] [01:05:00.16] time. And in some ways I like that for
[L1570] [01:05:03.28] like engineering discussions that
[L1571] [01:05:04.80] there's no like pulling of rank like hey
[L1572] [01:05:06.64] I'm more senior you know just take my
[L1573] [01:05:08.88] idea like it's a little bit more
[L1574] [01:05:10.88] meritocratic perhaps but in cross
[L1575] [01:05:13.52] functional situations say you're working
[L1576] [01:05:15.44] with like a PM like I'm trying to ship
[L1577] [01:05:18.00] this um [snorts] collaborative post
[L1578] [01:05:20.88] thing and I have to like meet with PM
[L1579] [01:05:24.15] [snorts] all these different PMs on
[L1580] [01:05:25.52] these different teams. Um, there was an
[L1581] [01:05:28.24] element where having a little bit higher
[L1582] [01:05:30.72] of a title I think just made those
[L1583] [01:05:33.36] conversations easier. Like I had a
[L1584] [01:05:35.28] higher baseline where they were like,
[L1585] [01:05:37.12] "Okay, this person like maybe they like
[L1586] [01:05:39.84] know something. They they've been here a
[L1587] [01:05:42.24] bit like they're not just um, you know,
[L1588] [01:05:44.80] totally new." And um you know you you
[L1589] [01:05:48.32] build up some reputation in a company
[L1590] [01:05:50.16] but when it gets so big and there's new
[L1591] [01:05:51.68] people joining all the time like you're
[L1592] [01:05:54.08] actually having to like reestablish that
[L1593] [01:05:55.76] a lot with with folks. So um yeah I
[L1594] [01:05:59.68] think like it it it was somewhat helpful
[L1595] [01:06:01.84] to have that title. There would be
[L1596] [01:06:03.84] discussions in the in the senior
[L1597] [01:06:05.44] engineering group about like should
[L1598] [01:06:07.76] should there be some form of of public
[L1599] [01:06:10.72] levels um within the company and I was
[L1600] [01:06:14.08] supportive of like maybe like a two
[L1601] [01:06:17.04] maybe not like the full level is is
[L1602] [01:06:18.96] public but like there's like a senior
[L1603] [01:06:21.28] designation or something. Um
[L1604] [01:06:23.76] [clears throat] just uh yeah I think
[L1605] [01:06:25.84] largely for like when you're working
[L1606] [01:06:28.08] with people outside of your normal
[L1607] [01:06:30.56] working group so that they start from a
[L1608] [01:06:32.72] slightly better baseline on you know
[L1609] [01:06:35.52] whether whether you know what you're
[L1610] [01:06:37.04] talking about. The [clears throat]
[L1611] [01:06:38.48] number one thing I hear people say is
[L1612] [01:06:40.32] the this is not optimal because it's
[L1613] [01:06:44.88] you're doing two jobs at once and you're
[L1614] [01:06:47.44] gonna drown and your career will not
[L1615] [01:06:49.52] flourish in either direction. What do
[L1616] [01:06:51.68] you say to that? I think it's probably
[L1617] [01:06:53.60] correct. [laughter] Like um at that
[L1618] [01:06:57.36] point I was really not optimizing for
[L1619] [01:07:00.64] career. Um you know it was never my
[L1620] [01:07:03.12] intent to stay longterm.
[L1621] [01:07:06.80] Uh I I mentioned this in the career note
[L1622] [01:07:09.92] like Facebook does these internal
[L1623] [01:07:13.12] employee sentiment surveys every 6
[L1624] [01:07:16.24] months I think or year and one of the
[L1625] [01:07:18.16] questions on there is how long do you
[L1626] [01:07:19.92] intend to to stay with the company. I
[L1627] [01:07:22.80] never put more than one year. [laughter]
[L1628] [01:07:25.52] It was always like okay this is my last
[L1629] [01:07:27.44] year I'm going to I'm going to get out
[L1630] [01:07:29.44] soon. Um, and so yeah, I think like I
[L1631] [01:07:33.60] didn't have aspirations to get to IC9.
[L1632] [01:07:37.28] Um, and so it kind of freed me up where
[L1633] [01:07:39.84] it was like, you know, um, well, I don't
[L1634] [01:07:42.00] want to get fired for performance, but I
[L1635] [01:07:43.44] kind of knew I wasn't going to get fired
[L1636] [01:07:44.72] for performance. Um, and so, yeah, there
[L1637] [01:07:49.36] was just a little bit less pressure on
[L1638] [01:07:51.20] that. and um yeah, so I could just kind
[L1639] [01:07:54.16] of like do the thing that made sense for
[L1640] [01:07:56.08] our group, our team um and and worry a
[L1641] [01:07:59.60] little bit less about the career stuff.
[L1642] [01:08:01.52] But yeah, absolutely. I think like I saw
[L1643] [01:08:04.40] firsthand like I think my ratings were
[L1644] [01:08:07.44] probably lower than they would have been
[L1645] [01:08:09.12] if I was just an IC maybe. Um [snorts]
[L1646] [01:08:13.76] it was like okay you're exceeding as an
[L1647] [01:08:16.16] IC but you're meeting as a manager so
[L1648] [01:08:18.24] you're just meeting
[L1649] [01:08:19.68] >> you know that's kind of like the full
[L1650] [01:08:21.76] journey from you know start to finish of
[L1651] [01:08:24.96] Instagram and I know you you've left
[L1652] [01:08:27.28] you've since left and you're working on
[L1653] [01:08:29.12] retro which is a popular social media
[L1654] [01:08:31.52] app with a lot of the polish that I kind
[L1655] [01:08:34.48] of recognize in Instagram as well. I'm
[L1656] [01:08:37.20] curious you know what made you want to
[L1657] [01:08:39.04] leave to start that? what's the story
[L1658] [01:08:40.72] behind creating retro?
[L1659] [01:08:43.04] >> So, around the last few months of my
[L1660] [01:08:46.64] time there, I was talking with Nathan,
[L1661] [01:08:49.36] who's my my co-founder. Um, we had
[L1662] [01:08:51.44] worked on stories together. He had gone
[L1663] [01:08:53.28] over to the Facebook side. He started
[L1664] [01:08:56.08] Facebook dating. Uh, and then he was
[L1665] [01:08:59.12] working on some of the virtual reality
[L1666] [01:09:01.68] products. And through our whole time,
[L1667] [01:09:05.36] you know, we were close friends. We
[L1668] [01:09:07.12] would meet up at this bar sometimes in
[L1669] [01:09:09.68] the mission called Lone Palm and we
[L1670] [01:09:12.40] would talk about how we just saw a
[L1671] [01:09:14.96] different way to build products to
[L1672] [01:09:17.52] structure a company and you know we
[L1673] [01:09:19.68] really wanted to be in the driver's seat
[L1674] [01:09:21.28] of that and uh we would talk about
[L1675] [01:09:24.48] starting a company but it was always
[L1676] [01:09:26.56] like that the timing wasn't right for
[L1677] [01:09:28.40] me. I was on a project that I was
[L1678] [01:09:30.24] engaged on and then I'd be like okay I
[L1679] [01:09:32.56] think I'm ready and he was on something
[L1680] [01:09:34.56] new. Um, and so finally our our timing
[L1681] [01:09:37.52] kind of aligned um where we
[L1682] [01:09:39.60] [clears throat] were both ready to leave
[L1683] [01:09:41.52] and I had a conversation with um this
[L1684] [01:09:45.36] investor friend, the same one that
[L1685] [01:09:46.88] connected me with Flipboard who's he's
[L1686] [01:09:49.84] kind of a mentor of mine and um he was
[L1687] [01:09:52.56] like it's time you should you should
[L1688] [01:09:54.16] really take a bet on yourself and and
[L1689] [01:09:56.56] that stuck with me. I was like yeah I
[L1690] [01:09:58.08] should like take a bet on myself. Um,
[L1691] [01:10:00.80] and so we left to start the company. And
[L1692] [01:10:04.40] actually our our goal with the company
[L1693] [01:10:06.24] is really to create this world-class
[L1694] [01:10:08.96] product studio. And Retro is our first
[L1695] [01:10:12.72] product, but it's not necessarily like
[L1696] [01:10:15.60] uh the reason for the company existing.
[L1697] [01:10:18.64] And we yeah, we just want to kind of
[L1698] [01:10:23.68] create this environment where great
[L1699] [01:10:25.76] product builders can do the best work of
[L1700] [01:10:28.08] their lives. and create products that
[L1701] [01:10:30.96] are good for people that they feel good
[L1702] [01:10:33.84] after using
[L1703] [01:10:35.28] >> [clears throat]
[L1704] [01:10:35.44] >> um and and also to create a successful
[L1705] [01:10:38.48] business. Uh so retro is our is our
[L1706] [01:10:40.96] first product and it's a social app but
[L1707] [01:10:44.64] it's actually quite different from what
[L1708] [01:10:46.72] are called the social apps today I would
[L1709] [01:10:49.36] say um in that it's actually social
[L1710] [01:10:52.31] [laughter]
[L1711] [01:10:53.04] you you you see people you know on it uh
[L1712] [01:10:56.40] friends it's it's all focused around
[L1713] [01:10:58.72] friends and um you know I'd say like the
[L1714] [01:11:02.56] traditional social media is maybe well
[L1715] [01:11:06.24] the derogatory word I would say is like
[L1716] [01:11:08.00] brain brain brain rot media. Um,
[L1717] [01:11:11.60] entertainment is maybe like a more
[L1718] [01:11:13.44] favorable uh term, but if I open
[L1719] [01:11:15.84] Instagram today, I don't see a lot of
[L1720] [01:11:19.52] the people I know. Um, even if I
[L1721] [01:11:21.76] actually go to seek that out, I tend to
[L1722] [01:11:24.08] end up down a rabbit hole of uh kind of
[L1723] [01:11:27.76] short form video entertaining content.
[L1724] [01:11:30.40] And um, it's definitely entertaining,
[L1725] [01:11:32.96] but it it kind of hijacks my attention.
[L1726] [01:11:35.68] I get sucked into it. And so the idea
[L1727] [01:11:38.88] behind Retro is we're creating a space
[L1728] [01:11:40.96] that's all about connecting with the
[L1729] [01:11:42.72] people that you actually know, staying
[L1730] [01:11:45.36] up to date with them, and also
[L1731] [01:11:47.36] appreciating your own life by looking
[L1732] [01:11:49.36] back on your photos and kind of picking
[L1733] [01:11:51.28] out the highlights. And in some ways,
[L1734] [01:11:54.00] it's a throwback to kind of the earlier
[L1735] [01:11:55.92] times in social media, what Instagram
[L1736] [01:11:58.32] used to be, all about creation. Um,
[L1737] [01:12:00.88] almost half of the people that use retro
[L1738] [01:12:03.12] on a daily basis actually post
[L1739] [01:12:04.64] something. Um, which you know I know
[L1740] [01:12:07.28] from working at Instagram that like that
[L1741] [01:12:09.04] number is quite a bit lower. Um, and I
[L1742] [01:12:13.76] take it as a really good sign that we
[L1743] [01:12:16.56] have created a product where people show
[L1744] [01:12:18.72] up to create almost as much as they show
[L1745] [01:12:21.04] up to consume. Uh, so we've been working
[L1746] [01:12:24.32] on that for the past few years. Um, it's
[L1747] [01:12:28.00] uh become very popular in Taiwan.
[L1748] [01:12:30.32] >> Oh, interesting. which is not something
[L1749] [01:12:32.56] we expected, but um you know, social
[L1750] [01:12:35.20] networks are so much about the network,
[L1751] [01:12:37.52] whether your friends get on it and we we
[L1752] [01:12:39.76] managed to hit the critical mass in
[L1753] [01:12:42.08] Taiwan and sort of all of the usage
[L1754] [01:12:44.96] patterns end up looking different when
[L1755] [01:12:46.56] when you hit that critical mass. Um so
[L1756] [01:12:49.04] we were number one on the app store
[L1757] [01:12:50.64] there for a period last uh last year. Um
[L1758] [01:12:54.96] and we still are at the top of the of
[L1759] [01:12:57.68] the photo category. We were number two
[L1760] [01:12:59.52] when I looked this morning. Um, so we've
[L1761] [01:13:02.24] kind of shown that like it when it
[L1762] [01:13:04.56] works, it works. Um, [snorts] and we had
[L1763] [01:13:07.60] just have this challenge of making it
[L1764] [01:13:08.96] work in more places. And um, you it's
[L1765] [01:13:11.60] very challenging to get people to try a
[L1766] [01:13:13.36] new app. Um, but if you miss seeing your
[L1767] [01:13:17.20] friends and people you know on social
[L1768] [01:13:18.96] media and staying connected with them, I
[L1769] [01:13:21.60] you know, very much encourage you to uh
[L1770] [01:13:24.08] to try out Retro. And uh and yeah, it's
[L1771] [01:13:27.84] I I think it's a a really delightful
[L1772] [01:13:29.84] app. I love seeing photos from my family
[L1773] [01:13:31.92] on there. And uh and we want it to feel
[L1774] [01:13:36.08] good when you open it and feel good when
[L1775] [01:13:38.24] you close it. So you don't feel like
[L1776] [01:13:40.32] your attention was hijacked that you
[L1777] [01:13:42.40] feel like this was a good use of time.
[L1778] [01:13:44.08] You got caught up with the people you
[L1779] [01:13:46.00] care about and then you can go on with
[L1780] [01:13:47.60] your life. You can get out and enjoy the
[L1781] [01:13:49.20] world. the design philosophy you went
[L1782] [01:13:52.08] for with this app. Is it more
[L1783] [01:13:54.56] challenging to get people to use it
[L1784] [01:13:56.24] because it's less addictive?
[L1785] [01:13:57.84] >> So, one of the key decisions that we've
[L1786] [01:14:01.84] designed around is that we don't have an
[L1787] [01:14:04.80] adbased business model. Um, and I
[L1788] [01:14:09.44] actually I don't think like ads are
[L1789] [01:14:12.40] evil, but I I do think that ads when
[L1790] [01:14:15.04] combined with an algorithmic feed are a
[L1791] [01:14:18.72] little bit evil. Um, because you have
[L1792] [01:14:22.80] this misaligned incentive. Um, you know,
[L1793] [01:14:26.64] I think the app is incentivized for you
[L1794] [01:14:30.00] to just consume more and more. It just
[L1795] [01:14:32.56] wants more and more of your time and
[L1796] [01:14:34.24] attention.
[L1797] [01:14:35.76] um even past, you know, what you wanted
[L1798] [01:14:39.20] to get out of the app. I show up to see
[L1799] [01:14:41.20] what a friend is doing, it's going to
[L1800] [01:14:43.52] try to keep me there for the next hour,
[L1801] [01:14:46.00] 2 hours, whatever. Uh and so I I think
[L1802] [01:14:50.80] ads fundamentally kind of like when
[L1803] [01:14:54.00] combined with an algorithmic feed um
[L1804] [01:14:57.04] make products that aren't super aligned
[L1805] [01:14:59.12] with people. Uh but there there is
[L1806] [01:15:02.08] definitely a challenge uh in terms of
[L1807] [01:15:04.96] like growing retro. So you know we don't
[L1808] [01:15:08.32] have uh creators the the model is mutual
[L1809] [01:15:13.20] friending. So um everyone
[L1810] [01:15:15.62] [clears throat] is private. You can only
[L1811] [01:15:17.20] see people that you've uh accepted as
[L1812] [01:15:20.16] friends and has to go both ways. It's
[L1813] [01:15:22.32] not like a following model. And we have
[L1814] [01:15:24.56] a limit of 250 friends. And so, um, you
[L1815] [01:15:28.00] can't build an audience on this
[L1816] [01:15:29.52] platform. And so, a lot of the ways that
[L1817] [01:15:31.76] like Instagram grew was through creators
[L1818] [01:15:34.00] that were financially incentivized to
[L1819] [01:15:36.16] spread this app and get more followers.
[L1820] [01:15:38.32] And so, those those pathways to growth
[L1821] [01:15:41.60] are not open to us. Um, but we've we've
[L1822] [01:15:44.72] seen examples of like, you know, Bal uh
[L1823] [01:15:47.52] managed to get a decent growth. They had
[L1824] [01:15:51.76] kind of a nice viral uh mechanic built
[L1825] [01:15:55.04] in with this notification that everyone
[L1826] [01:15:57.52] got that was weird. It's time to be
[L1827] [01:15:59.92] real. [laughter] You know, that created
[L1828] [01:16:02.00] a lot of conversation. So, that
[L1829] [01:16:03.36] certainly helped. Um, but I think it is
[L1830] [01:16:05.76] possible to to grow a friends only uh
[L1831] [01:16:08.80] social network, but in many ways it is
[L1832] [01:16:11.04] it is harder and and also the business
[L1833] [01:16:12.96] model is is harder. Um, that's something
[L1834] [01:16:15.36] that that we're very open about like
[L1835] [01:16:17.68] this is a challenge. um there would be
[L1836] [01:16:20.72] easier ways to do things, but we think
[L1837] [01:16:23.60] they would lead to bad outcomes,
[L1838] [01:16:26.56] outcomes we don't want in the long term.
[L1839] [01:16:28.88] We're very much taking an opinion on
[L1840] [01:16:33.20] what this product should be and what we
[L1841] [01:16:34.96] want to see in the world. Um you know,
[L1842] [01:16:37.52] some people say just just build what
[L1843] [01:16:38.96] people want and you know, maybe you
[L1844] [01:16:41.04] could say like in Instagram people are
[L1845] [01:16:43.52] demonstrating that it's what they want
[L1846] [01:16:45.04] cuz they spend more of their time there.
[L1847] [01:16:47.36] Um, and we're taking a little bit more
[L1848] [01:16:49.68] of an opinionated stance saying no, we
[L1849] [01:16:52.32] think like actually that's not great and
[L1850] [01:16:54.56] this is better and even if it's more
[L1851] [01:16:56.88] challenging, it's something we strongly
[L1852] [01:16:58.88] believe should exist in the world and
[L1853] [01:17:00.88] should be an option there for for people
[L1854] [01:17:03.20] that want it. Um, I think we also
[L1855] [01:17:05.20] actually coexist really nicely alongside
[L1856] [01:17:07.28] Instagram. Like I still have it. I still
[L1857] [01:17:09.44] open it. Um, but I'm getting sucked into
[L1858] [01:17:11.84] it a lot less and it's helped me kind of
[L1859] [01:17:13.60] break this like phone addiction that um,
[L1860] [01:17:16.80] yeah, I just I didn't feel good about.
[L1861] [01:17:19.36] >> How do you monetize if you're not using
[L1862] [01:17:21.76] ads?
[L1863] [01:17:22.48] >> We have a a subscription, a premium
[L1864] [01:17:24.40] subscription and um, so it's only a
[L1865] [01:17:27.04] small percentage of users that are
[L1866] [01:17:28.64] subscribers and it's just kind of like
[L1867] [01:17:30.08] an extra tier of features particularly
[L1868] [01:17:32.56] some of the things that cost us a lot to
[L1869] [01:17:34.48] provide as a service. So video as you
[L1870] [01:17:36.96] know from video infrastructure like the
[L1871] [01:17:39.20] storage and bandwidth for that is quite
[L1872] [01:17:41.04] a bit more than than photos. Um and so
[L1873] [01:17:44.48] you have to subscribe if you want to
[L1874] [01:17:46.24] share out video. Uh [snorts] but the
[L1875] [01:17:48.96] free version of the app is like actually
[L1876] [01:17:51.12] great. Um you know uh you can share
[L1877] [01:17:53.76] photos, you can remember your own life.
[L1878] [01:17:55.44] Um and it's like 93% of what people
[L1879] [01:17:59.60] share on retro is photos anyways. Um,
[L1880] [01:18:03.20] and uh, and so, um, yeah, if you want to
[L1881] [01:18:06.48] kind of like support the mission and and
[L1882] [01:18:08.56] get those extra features, you can become
[L1883] [01:18:10.16] a subscriber.
[L1884] [01:18:11.28] >> That's awesome. I love like the
[L1885] [01:18:13.04] intention behind it and like the the
[L1886] [01:18:15.44] mission. It's really cool.
[L1887] [01:18:17.28] >> It's definitely a product that's fun to
[L1888] [01:18:18.80] work on. It feels good like Yeah, it's
[L1889] [01:18:21.76] it's very a very feel-good. We had a
[L1890] [01:18:24.56] tagline for a while like feel good
[L1891] [01:18:25.92] social media and um yeah it's very much
[L1892] [01:18:28.16] that
[L1893] [01:18:29.60] >> coming from big tech and starting your
[L1894] [01:18:31.44] own company. I'm curious like looking
[L1895] [01:18:33.28] back on you know across the various
[L1896] [01:18:36.48] career axes of maybe like you know
[L1897] [01:18:39.12] learning
[L1898] [01:18:40.80] satisfaction compensation
[L1899] [01:18:43.76] you know the things that people look at
[L1900] [01:18:45.20] for their career. How has it been so far
[L1901] [01:18:47.84] working on your own thing?
[L1902] [01:18:49.44] >> Yeah um compensation is quite a bit
[L1903] [01:18:51.92] worse. [laughter] We we pay Nathan and I
[L1904] [01:18:55.44] pay ourselves less than all of our
[L1905] [01:18:57.20] employees and we have more ownership in
[L1906] [01:18:58.80] the in the company which I think is the
[L1907] [01:19:00.88] right way. It's how it should be. Um uh
[L1908] [01:19:04.56] but that means that yeah, you know, kind
[L1909] [01:19:06.96] of um certainly put off that short-term
[L1910] [01:19:09.12] compensation. We hope to become a very
[L1911] [01:19:11.44] successful company and that that equity
[L1912] [01:19:13.12] is going to be worth a lot both for us
[L1913] [01:19:15.44] and for our employees. It was always the
[L1914] [01:19:17.60] thing I wanted to do. Like I I I was a
[L1915] [01:19:20.96] bit surprised actually that I ended up
[L1916] [01:19:22.56] in in in big tech, you know, talking
[L1917] [01:19:24.40] about like those early days in in
[L1918] [01:19:26.80] Flipboard and um kind of this like
[L1919] [01:19:29.68] entrepreneurial culture. Like it was
[L1920] [01:19:31.76] always exciting to me. I would read
[L1921] [01:19:34.00] TechCrunch all the time um about the new
[L1922] [01:19:37.36] startups and uh yeah, I just always
[L1923] [01:19:40.08] wanted to kind of build a company, you
[L1924] [01:19:43.36] know, be able to to bring the best
[L1925] [01:19:45.76] people together, work on the things that
[L1926] [01:19:48.24] we thought were cool. Um do the things
[L1927] [01:19:52.08] do things in the way that we wanted to
[L1928] [01:19:54.32] do them. And uh yeah, it's been it's
[L1929] [01:19:56.72] been awesome for that. Um, and uh, and
[L1930] [01:20:00.40] definitely like have learned a ton. I
[L1931] [01:20:03.12] think the amount of time that I get to
[L1932] [01:20:06.24] spend on interesting work is much higher
[L1933] [01:20:09.68] than it was, especially in my later
[L1934] [01:20:11.92] years at Instagram. Like a lot of my
[L1935] [01:20:14.40] work became kind of like convincing
[L1936] [01:20:18.08] uh, you know, layers above me that we
[L1937] [01:20:21.04] should do something. I I would say there
[L1938] [01:20:24.80] were probably more people working on
[L1939] [01:20:26.72] that app than there needed to be.
[L1940] [01:20:28.72] [gasps] And so actually there was a lot
[L1941] [01:20:30.56] of gatekeeping
[L1942] [01:20:32.24] um where it was like is your team
[L1943] [01:20:35.04] allowed to ship? So you would do this
[L1944] [01:20:37.92] work and then there was like you have to
[L1945] [01:20:39.92] convince somebody that like this is a
[L1946] [01:20:41.68] good enough thing for to ship in the
[L1947] [01:20:43.84] product which is understandable because
[L1948] [01:20:46.88] you know it becomes very complex if you
[L1949] [01:20:49.52] just let everybody go. But it means that
[L1950] [01:20:52.48] there's a lot of work in just kind of
[L1951] [01:20:54.96] like that political wrangling and like
[L1952] [01:20:56.72] how do I how do I make this person feel
[L1953] [01:20:58.80] like this is their idea, not my idea. Um
[L1954] [01:21:02.12] [snorts] and and I'd spend none of my
[L1955] [01:21:03.76] time on that now. Um you know, we we do
[L1956] [01:21:06.88] a 1-hour standup uh every day. That's
[L1957] [01:21:09.68] basically the only meeting uh on my
[L1958] [01:21:12.24] calendar. So, um, I get almost the whole
[L1959] [01:21:15.12] day to to just, uh, build, think about,
[L1960] [01:21:19.28] you know, what people want and and try
[L1961] [01:21:21.12] to make it. Um, so, um, yeah, I'd say
[L1962] [01:21:24.80] like satisfaction is definitely higher.
[L1963] [01:21:27.20] Um, learning is definitely higher,
[L1964] [01:21:29.52] compensation is definitely lower.
[L1965] [01:21:32.25] [snorts and laughter] I
[L1966] [01:21:32.96] >> I think throughout the conversation you
[L1967] [01:21:34.72] mentioned that, you know, smaller teams
[L1968] [01:21:37.12] can move faster. Do you think that the
[L1969] [01:21:39.92] company would be better off if you just
[L1970] [01:21:42.48] like laid off half the people?
[L1971] [01:21:44.72] >> I was I would say yes. [laughter] We we
[L1972] [01:21:46.96] used to talk about this a lot when the
[L1973] [01:21:49.04] company was much smaller. Um like uh
[L1974] [01:21:52.24] this thought experiment of like you know
[L1975] [01:21:54.08] the Thanos like you just snap your
[L1976] [01:21:55.92] fingers like half of people are fired
[L1977] [01:21:58.64] even if it's a random selection um do
[L1978] [01:22:01.60] things go better and frequently we felt
[L1979] [01:22:04.24] like yeah maybe I think they would. Um,
[L1980] [01:22:07.44] so yeah. Um, I mean it's tough because
[L1981] [01:22:12.88] with a business like Instagram, you
[L1982] [01:22:14.88] know, if you can make a.1% improvement,
[L1983] [01:22:17.20] it's actually like hundreds of millions
[L1984] [01:22:18.88] of dollars to to the business. And so
[L1985] [01:22:22.40] sometimes um, you know, that incremental
[L1986] [01:22:25.28] person maybe they they're able to find
[L1987] [01:22:27.12] those things. Uh, but I think it's less
[L1988] [01:22:31.20] appreciated the cost of each person you
[L1989] [01:22:35.36] add. And there's sort of like maybe the
[L1990] [01:22:37.76] more obvious just organizational
[L1991] [01:22:40.72] communication overhead. You know, you
[L1992] [01:22:43.20] you just have more stakeholders, more
[L1993] [01:22:45.12] meetings, more coordination.
[L1994] [01:22:47.44] But um even just like writing more code,
[L1995] [01:22:50.88] like having more code in the app. Um I
[L1996] [01:22:54.48] remember right before I left, they had
[L1997] [01:22:57.92] this tool where you could see how much
[L1998] [01:22:59.92] time you were spending compiling the
[L1999] [01:23:02.08] app. Um, and I was spending more than
[L2000] [01:23:06.72] four hours a day waiting for the app to
[L2001] [01:23:09.76] build just because there was so much
[L2002] [01:23:12.56] code and you know the tooling just had
[L2003] [01:23:15.60] not kept up with basically the the
[L2004] [01:23:18.00] velocity at which people were writing
[L2005] [01:23:20.56] code and uh so that's a huge cost that's
[L2006] [01:23:24.24] kind of you know it's not noticeable
[L2007] [01:23:26.72] with each incremental person you have
[L2008] [01:23:28.40] but now you have this you have a
[L2009] [01:23:29.92] thousand engineers and all of a sudden
[L2010] [01:23:31.52] like everyone's just like so slowed down
[L2011] [01:23:33.92] because uh yeah because of this
[L2012] [01:23:37.36] overhead. So um yeah with a with a
[L2013] [01:23:40.80] smaller team you know like when we were
[L2014] [01:23:42.48] 10 people and the app was tiny it was
[L2015] [01:23:44.32] like so much easier to get things done
[L2016] [01:23:46.24] like a project like like white out um
[L2017] [01:23:49.28] you know would be like a massive project
[L2018] [01:23:52.24] for Instagram today because there's so
[L2019] [01:23:54.64] many more surfaces there's so much more
[L2020] [01:23:56.08] code there's so many more people was
[L2021] [01:23:58.16] actually like a lot easier at the time
[L2022] [01:24:00.48] that I did it. Yeah, I guess you know
[L2023] [01:24:03.12] Twitter is kind of an interesting case
[L2024] [01:24:05.12] study of that because they kind of did
[L2025] [01:24:08.24] went through that and the the app's
[L2026] [01:24:10.32] still operating. I do get the sense that
[L2027] [01:24:12.88] there's a lot more breakages, but I'd be
[L2028] [01:24:15.36] curious like on the product development
[L2029] [01:24:17.04] side, you know, is it how has that been
[L2030] [01:24:19.20] being on those teams?
[L2031] [01:24:20.80] >> Totally. Yeah. I mean, I think there
[L2032] [01:24:22.48] were projections when Elon came in and I
[L2033] [01:24:26.48] think he cut like 80%
[L2034] [01:24:28.16] >> Yeah.
[L2035] [01:24:28.48] >> of the staff or people left as well,
[L2036] [01:24:30.32] >> right? that like, oh, this thing was
[L2037] [01:24:32.16] just going to 100% fall over. Um, and I
[L2038] [01:24:36.08] mean, my experience is somewhat buggy.
[L2039] [01:24:38.27] [laughter] There's definitely some
[L2040] [01:24:39.52] issues. Um, but I mean, you know, it's
[L2041] [01:24:43.60] very much continuing to to run. I think
[L2042] [01:24:46.08] also I saw like the economics of the
[L2043] [01:24:49.92] business have actually become much
[L2044] [01:24:51.92] better. Um, it's [snorts] actually
[L2045] [01:24:54.72] profitable now. uh whereas you know
[L2046] [01:24:57.36] through almost its entire history it was
[L2047] [01:24:59.84] operating at quite a loss and so um yeah
[L2048] [01:25:03.92] somebody coming in and and with a
[L2049] [01:25:06.88] machete cutting [laughter] things like
[L2050] [01:25:08.96] may maybe it's okay
[L2051] [01:25:10.64] >> towards the end of the conversation I
[L2052] [01:25:12.32] just want to wrap up with a few career
[L2053] [01:25:14.24] reflections I think first thing is you
[L2054] [01:25:17.28] throughout your projects you worked with
[L2055] [01:25:18.88] like a lot of very talented people I
[L2056] [01:25:21.36] think you mentioned you know Thomas
[L2057] [01:25:22.40] Dimpson will Bailey a few incredible
[L2058] [01:25:25.60] designers. Also, sounds like you worked
[L2059] [01:25:27.60] with the founders of Instagram. And I'm
[L2060] [01:25:29.92] curious, do you have any stories that
[L2061] [01:25:32.64] you share that illustrate what made them
[L2062] [01:25:35.52] exceptional?
[L2063] [01:25:36.48] >> Mike Kger is is definitely something of
[L2064] [01:25:39.36] a of a hero of mine and it was like such
[L2065] [01:25:41.68] a privilege to to get to work with him.
[L2066] [01:25:44.96] They they say like don't meet your
[L2067] [01:25:46.56] heroes because you'll be disappointed,
[L2068] [01:25:48.08] but I think like you should meet Mike
[L2069] [01:25:49.44] Creger. He's he's actually an awesome
[L2070] [01:25:51.76] human and um a lot of the ways that I
[L2071] [01:25:55.84] think about
[L2072] [01:25:57.68] engineering leadership and engineering
[L2073] [01:26:00.32] philosophy came from him. Uh so I
[L2074] [01:26:03.68] mentioned earlier the simple thing
[L2075] [01:26:05.04] first, you know, that's really stuck
[L2076] [01:26:06.72] with me. I think the attention to detail
[L2077] [01:26:09.68] and craft. Um, but another thing is he
[L2078] [01:26:13.12] had this sort of I don't know if it was
[L2079] [01:26:15.12] intentional or just the way he is, but
[L2080] [01:26:16.56] it was like this lead from the front uh
[L2081] [01:26:18.64] or I call it like lead from the front
[L2082] [01:26:20.88] way of operating where he never put
[L2083] [01:26:23.92] himself above the team and he would just
[L2084] [01:26:28.00] jump in to whatever team if an effort
[L2085] [01:26:32.72] needed help. So uh at the end of stories
[L2086] [01:26:37.04] I had brought in a friend of mine from
[L2087] [01:26:39.52] Flipboard actually who was then working
[L2088] [01:26:41.60] at Facebook not at Instagram very
[L2089] [01:26:43.84] different team to do the drawing tools
[L2090] [01:26:46.24] just because he had worked on a drawing
[L2091] [01:26:47.84] app before and I was like hey we need
[L2092] [01:26:49.36] drawing like can you work on this um
[L2093] [01:26:52.56] it's kind of a an interesting insight
[L2094] [01:26:54.48] into like how Facebook operates that I
[L2095] [01:26:56.32] could just like go to this random you
[L2096] [01:26:58.88] know person on a very different part of
[L2097] [01:27:01.04] the or and pull him in to this project.
[L2098] [01:27:03.76] Um, so he worked on it for a few weeks
[L2099] [01:27:05.76] and and got it reasonably far, but uh
[L2100] [01:27:07.92] then kind of got pulled back by his
[L2101] [01:27:09.92] team. Um, so we were in we were in a bit
[L2102] [01:27:12.64] of a pickle and um Mike just came in and
[L2103] [01:27:15.84] was like, "Okay, I'll I'll finish it."
[L2104] [01:27:17.52] Like um so he, you know, he's in there
[L2105] [01:27:20.80] coding the the neon brush and uh you
[L2106] [01:27:24.32] know, we were working those insane
[L2107] [01:27:25.84] hours. He was there working them with
[L2108] [01:27:27.76] us. Um he's up at 2 am reviewing my
[L2109] [01:27:31.28] diffs. Um, and uh, yeah, just seeing
[L2110] [01:27:35.60] that and how that felt as a team uh,
[L2111] [01:27:39.84] really has informed like the way I think
[L2112] [01:27:42.16] about leading teams. Um, and and so
[L2113] [01:27:45.92] yeah, that he he's he's awesome. Um,
[L2114] [01:27:49.84] some of the other folks you mentioned,
[L2115] [01:27:51.92] Will Bailey, I talked about him a little
[L2116] [01:27:54.64] bit before. He has just this product
[L2117] [01:28:00.00] vision that he sticks to very strongly
[L2118] [01:28:02.72] and frequently it's quite good. He at
[L2119] [01:28:06.56] the kind of like I would say like dark
[L2120] [01:28:09.52] days of development of the stories
[L2121] [01:28:11.76] project when it was spinning in circles.
[L2122] [01:28:14.64] It was taking different forms. None of
[L2123] [01:28:16.32] them felt very good. He just kind of
[L2124] [01:28:18.40] outlined this full vision in a document
[L2125] [01:28:21.04] for like how this product should work.
[L2126] [01:28:23.92] um you know the things that we could do
[L2127] [01:28:25.84] with it going forward. And I looked back
[L2128] [01:28:28.24] on it five years later and I was like,
[L2129] [01:28:29.60] "Wow, this was like the five-year road
[L2130] [01:28:31.04] map for for what we ended up doing."
[L2131] [01:28:32.96] Like he basically nailed it all from the
[L2132] [01:28:35.12] start. Um and uh and yeah, he was such a
[L2133] [01:28:38.80] good example for like how you could
[L2134] [01:28:42.32] succeed as a product focused engineer.
[L2135] [01:28:44.64] Um which actually was fairly it it was
[L2136] [01:28:49.20] much more of a thing in Instagram than
[L2137] [01:28:51.04] it was in Facebook. I remember being in
[L2138] [01:28:53.28] boot camp and people were saying okay if
[L2139] [01:28:55.68] you're junior you go work on a product
[L2140] [01:28:57.28] team and then if you're senior you work
[L2141] [01:28:58.64] on an infrastructure team and that was
[L2142] [01:29:00.96] kind of the culture was like you know
[L2143] [01:29:03.60] product is easy but like you know real
[L2144] [01:29:06.24] engineers they work on infrastructure
[L2145] [01:29:08.40] and uh and Instagram actually
[L2146] [01:29:10.88] prioritized more in some ways the the
[L2147] [01:29:14.16] product side and I think that was
[L2148] [01:29:15.92] reflected in you know the various
[L2149] [01:29:18.56] versions of stories for example um And
[L2150] [01:29:22.00] so Will was such a great kind of mentor
[L2151] [01:29:25.04] and um example of like how you could
[L2152] [01:29:27.84] have this successful career as a as a
[L2153] [01:29:30.72] product engineer. Um how you could
[L2154] [01:29:34.40] influence product direction as an
[L2155] [01:29:36.40] engineer. And then Thomas is uh is
[L2156] [01:29:40.80] probably just like the smartest person
[L2157] [01:29:42.16] I've ever met. Like he's [laughter] he
[L2158] [01:29:44.16] he's incredibly smart, but not in like a
[L2159] [01:29:47.12] savant kind of way. like he's also like
[L2160] [01:29:49.36] you know uh got great social still
[L2161] [01:29:52.48] skills and understands people um
[L2162] [01:29:55.30] [snorts] and uh so he did the feed
[L2163] [01:29:58.00] ranking or you know basically started
[L2164] [01:30:00.00] all the ranking at Instagram um he
[L2165] [01:30:02.48] started his own company open a open AI
[L2166] [01:30:05.28] bought his company he's a researcher
[L2167] [01:30:07.68] there now maybe Zuck's coming to him
[L2168] [01:30:09.44] with a$und00 million offer [laughter] I
[L2169] [01:30:12.08] don't know um but uh but yeah again like
[L2170] [01:30:16.88] you know he actually had like this skill
[L2171] [01:30:20.08] on the infrastructure side. Um, you
[L2172] [01:30:22.32] know, built a lot of the infrastructure
[L2173] [01:30:24.40] for the ranking stuff, but always
[L2174] [01:30:27.68] approached it with a product mindset and
[L2175] [01:30:29.84] and I think would probably consider
[L2176] [01:30:31.60] himself like [snorts] a product person.
[L2177] [01:30:34.00] Um, I have always been interested in
[L2178] [01:30:38.80] technology as like a means to
[L2179] [01:30:42.08] create things for people. Um, I've never
[L2180] [01:30:45.68] been that interested in like the
[L2181] [01:30:47.12] technology itself. Um, it's like only
[L2182] [01:30:50.00] interesting to me to the extent that
[L2183] [01:30:52.24] like I can create interesting
[L2184] [01:30:54.72] experiences for people. Uh so yeah, I
[L2185] [01:30:59.36] think like um Thomas and and Will
[L2186] [01:31:03.76] um you know kind of had maybe a similar
[L2187] [01:31:06.96] approach very like humanoriented
[L2188] [01:31:10.72] um thinking about the psychology how
[L2189] [01:31:13.76] people use these things and how it makes
[L2190] [01:31:15.36] them feel. And then you know last
[L2191] [01:31:17.36] question is if you could go back to
[L2192] [01:31:20.16] yourself after all this experience that
[L2193] [01:31:22.24] you have and talk to yourself when you
[L2194] [01:31:24.64] were just graduating college and give
[L2195] [01:31:26.48] yourself some career advice what would
[L2196] [01:31:28.24] you say
[L2197] [01:31:28.88] >> like just invest in the tools of your
[L2198] [01:31:31.28] time to build things for people like
[L2199] [01:31:34.80] build products for people and I think if
[L2200] [01:31:38.88] you if you do that you'll be pretty
[L2201] [01:31:41.52] flexible and adaptable and in many ways
[L2202] [01:31:44.40] you have a unique opportunity as a new
[L2203] [01:31:46.24] grad because you you aren't sort of
[L2204] [01:31:49.84] stuck on this path of like I'm I'm an
[L2205] [01:31:53.04] iOS person. I know this technology
[L2206] [01:31:55.12] really well. Like it's all new to you
[L2207] [01:31:57.44] and so you can pick up the latest thing,
[L2208] [01:31:59.60] right? And so I think like with these AI
[L2209] [01:32:01.92] tools that are coming out um you can do
[L2210] [01:32:04.00] incredible things with them and you're
[L2211] [01:32:06.32] probably going to be more skilled at
[L2212] [01:32:07.76] those than the senior engineers um
[L2213] [01:32:11.44] because it's just not the thing that
[L2214] [01:32:13.52] they you know learned natively that
[L2215] [01:32:16.24] they've invested their time into. And I
[L2216] [01:32:18.80] had that to some extent with iOS where
[L2217] [01:32:20.88] it was a it was a newer thing and so
[L2218] [01:32:23.76] like the senior engineers were like
[L2219] [01:32:25.20] writing Java or something you know they
[L2220] [01:32:26.72] were writing our back end and I could
[L2221] [01:32:28.40] actually stand out and excel on this
[L2222] [01:32:30.88] thing because it was the first thing I
[L2223] [01:32:32.72] learned and um you know I was eager
[L2224] [01:32:35.36] hungry and uh I think there's there's
[L2225] [01:32:38.48] something to that with like this new set
[L2226] [01:32:40.24] of AI tools. So yeah, I think my advice
[L2227] [01:32:42.56] for new grads is just like you learn the
[L2228] [01:32:44.56] tools of your time and and and get good
[L2229] [01:32:46.48] at them and and make things make good
[L2230] [01:32:49.36] things for people. Um, and I think I
[L2231] [01:32:52.72] think that will work out. I imagine it's
[L2232] [01:32:54.16] it's a bit scary probably because it's
[L2233] [01:32:56.32] hard to say how it's going to play out,
[L2234] [01:32:58.00] but like it seems like there's reducing
[L2235] [01:33:01.04] demand for like junior software
[L2236] [01:33:03.12] engineers because of some of these AI
[L2237] [01:33:04.88] tools. But I think if you can yourself
[L2238] [01:33:07.76] get really good at using those tools,
[L2239] [01:33:10.16] there will definitely be roles for you.
[L2240] [01:33:12.48] >> Awesome. Well, yeah, thank you so much
[L2241] [01:33:14.40] for your time, Ryan. I was really um
[L2242] [01:33:16.64] yeah, you're a legend at Instagram and I
[L2243] [01:33:18.48] worked there for so long. Super excited
[L2244] [01:33:20.80] to talk to you at this point. Is there
[L2245] [01:33:23.60] anything you want to redirect the
[L2246] [01:33:25.28] audience attention to?
[L2247] [01:33:26.72] >> If the ideas behind Retro sound
[L2248] [01:33:28.88] interesting to you, um definitely try it
[L2249] [01:33:31.28] out. Um it's, you know, it's a great
[L2250] [01:33:34.16] place to to reconnect with people that
[L2251] [01:33:36.80] you you uh want to see into their lives,
[L2252] [01:33:40.16] but maybe they've stopped posting on
[L2253] [01:33:42.24] social media. So, so get them on, too.
[L2254] [01:33:44.88] If you're a designer, you're an
[L2255] [01:33:46.32] engineer, um definitely reach out. I
[L2256] [01:33:48.48] think we have some interesting ideas in
[L2257] [01:33:51.44] in how we're building this company. You
[L2258] [01:33:54.08] know, I mentioned before our goal is to
[L2259] [01:33:56.32] become a world-class product studio.
[L2260] [01:33:58.80] multiple products. We have um Retro, we
[L2261] [01:34:01.20] have two more in the pipeline right now.
[L2262] [01:34:03.36] And I think we have some interesting
[L2263] [01:34:05.84] ways we're structuring revenue share
[L2264] [01:34:08.40] with employees. So, as these apps start
[L2265] [01:34:10.88] to make money, um even if the company's
[L2266] [01:34:13.84] ambition is to kind of like take that
[L2267] [01:34:16.16] and reinvest it into growth, um you can
[L2268] [01:34:19.28] see some of that upside right away. And
[L2269] [01:34:22.00] we're building infrastructure that helps
[L2270] [01:34:24.48] support products across the portfolio.
[L2271] [01:34:27.44] So, we're building growth tools,
[L2272] [01:34:29.52] analytics tools, all of that, um, that I
[L2273] [01:34:32.56] think are going to really help us excel
[L2274] [01:34:34.40] as a product studio. So, if that's
[L2275] [01:34:36.32] interesting to you, you know, reach out
[L2276] [01:34:37.60] for a conversation. And, uh, yeah, it's
[L2277] [01:34:40.00] just been a pleasure chatting and thanks
[L2278] [01:34:41.84] for having me on.
[L2279] [01:34:42.88] >> Thanks so much, Ryan. Really appreciate
[L2280] [01:34:44.24] your time.
[L2281] [01:34:45.52] >> Thanks for listening to the podcast. I
[L2282] [01:34:48.08] don't sell anything or do sponsorships,
[L2283] [01:34:50.64] but if you want to help out with the
[L2284] [01:34:52.56] podcast, you can support by engaging
[L2285] [01:34:55.68] with the content on YouTube or on
[L2286] [01:34:58.08] Spotify. If you want to drop a review,
[L2287] [01:34:59.76] that'll be super helpful. And if there's
[L2288] [01:35:02.08] any guests that you want to bring on to,
[L2289] [01:35:04.00] please let me know. I feel like sourcing
[L2290] [01:35:06.40] very senior IC's, there's no wellstudied
[L2291] [01:35:10.16] list out there on Google that I can just
[L2292] [01:35:12.00] search this up. So, if there's someone
[L2293] [01:35:13.68] in your org or at your company who you
[L2294] [01:35:15.60] really look up to and you want to hear
[L2295] [01:35:17.04] their career story, let me know and I'll
[L2296] [01:35:19.52] reach out to
