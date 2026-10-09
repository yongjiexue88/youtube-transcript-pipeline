# OpenAI Codex Tech Lead: How His Career Grew And How He Uses Codex | Michael Bolin

Source ID: source-d89129dbba19118b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/OpenAI_Codex_Tech_Lead_How_His_Career_Grew_And_How_He_Uses_Codex_Michael_Bolin_en.txt
Video: https://www.youtube.com/watch?v=hN5ZFzWFhhg

[L10] [00:00.08] the questions that you asked the agent
[L11] [00:02.16] is going to affect the quality of the
[L12] [00:03.76] thing that you get out.
[L13] [00:05.84] >> This is Michael Bolan, tech lead for the
[L14] [00:08.16] open-source codeex repository and former
[L15] [00:10.80] distinguished engineer at Meta. And we
[L16] [00:12.80] talked about how his career grew.
[L17] [00:14.80] >> So I was like, all right, hackathon
[L18] [00:17.20] totally going to like make a new build
[L19] [00:18.80] system. You know, it relatively quickly
[L20] [00:20.64] had something that was dramatically
[L21] [00:22.00] better, like at least like twice as
[L22] [00:23.52] fast.
[L23] [00:24.00] >> He shared about how OpenAI engineers
[L24] [00:26.16] actually [music] use codecs. I almost
[L25] [00:27.76] feel a little bad writing code by hand.
[L26] [00:29.84] >> Well, what percent of your code would
[L27] [00:31.68] you say is human written?
[L28] [00:33.04] >> You know, because every time I sit down,
[L29] [00:34.40] I'm like, should I write this? I mean,
[L30] [00:35.68] the answer is almost always no.
[L31] [00:37.04] >> And we discussed AI research versus big
[L32] [00:39.28] tech engineering cultures. What are your
[L33] [00:41.20] thoughts on that? Research-led culture
[L34] [00:42.96] versus engineering culture.
[L35] [00:44.72] >> I mean, it was certainly an adjustment,
[L36] [00:46.16] right? I mean, I think if anyone who
[L37] [00:47.68] comes here and says otherwise is a liar,
[L38] [00:49.76] but [laughter]
[L39] [00:50.80] here's the full episode.
[L40] [00:56.80] I was looking deep into your website and
[L41] [01:00.16] there was something most everything I
[L42] [01:02.08] could find more information about, but
[L43] [01:03.44] there's this one thing that you seem to
[L44] [01:05.36] be pretty excited about at the time, but
[L45] [01:06.72] I couldn't find any information about it
[L46] [01:08.08] because all the links were dead. What is
[L47] [01:10.08] chickenfoot? Oh man, that's strangely
[L48] [01:13.52] relevant because it's uh it was my my
[L49] [01:15.68] master's thesis pro project.
[L50] [01:17.84] >> Uh it was a Firefox extension. Uh
[L51] [01:20.88] probably one of the very few that was
[L52] [01:22.08] written, you know, in JavaScript for
[L53] [01:23.52] Firefox as a thesis project. And it was
[L54] [01:26.24] a it was actually a little coding tool
[L55] [01:28.16] in a sidebar of Firefox and it was like
[L56] [01:31.04] a little uh ripple. It was called end
[L57] [01:33.36] user the idea was end user programming
[L58] [01:34.88] for the web. And so there were functions
[L59] [01:37.44] like enter and click and things like
[L60] [01:39.28] that and you'd say enter and you know
[L61] [01:41.20] have pass a string arg and it would like
[L62] [01:43.28] find the box and you'd say click search
[L63] [01:45.84] or whatever and um and you know a lot of
[L64] [01:49.84] the work was all these heristics that we
[L65] [01:51.60] built under the hood that if you said
[L66] [01:53.60] you know enter first name finding the
[L67] [01:56.40] like the words first and name and
[L68] [01:57.92] finding the text box that was closest
[L69] [01:59.60] and then like using that and then
[L70] [02:00.88] through JavaScript like using that as
[L71] [02:03.04] the input and I just think about that
[L72] [02:05.44] now because it's really funny. We did
[L73] [02:07.04] all you know a lot of work and that's
[L74] [02:10.00] >> you know a lot of what these agents are
[L75] [02:11.44] doing right now right is like similar
[L76] [02:13.04] but now actually truly in natural
[L77] [02:14.72] language like not in this little like
[L78] [02:16.08] JavaScript ripple.
[L79] [02:17.04] >> Oh interesting. So it parsed the front
[L80] [02:18.72] end and had this ripple where you could
[L81] [02:20.64] say I don't know find the the first name
[L82] [02:23.60] field and you know
[L83] [02:24.72] >> yeah we'd use like you know the the
[L84] [02:26.24] accessibility tags and alt alt text for
[L85] [02:28.64] images and we'd you know and and it
[L86] [02:30.56] worked well. um was really good at
[L87] [02:32.88] Craigslist actually because that's one
[L88] [02:34.40] of the simplest uh websites you could
[L89] [02:36.72] you could use. But I had I had friends
[L90] [02:38.16] who like made like automated tasks and
[L91] [02:40.56] like made real money off of things they
[L92] [02:42.40] automated with this tool which was
[L93] [02:44.72] really fun.
[L94] [02:45.60] >> When you entered the industry you were
[L95] [02:47.12] really excited about going to Google and
[L96] [02:49.28] specifically working on Google Calendar.
[L97] [02:51.68] Yeah.
[L98] [02:52.00] >> Um so what drew you to Google and what
[L99] [02:54.00] was that like? Yeah, I mean, you know,
[L100] [02:56.72] so I, you know, got online in the 90s,
[L101] [02:59.60] right? I remember, you know, browsing
[L102] [03:01.44] the web and it was at a time you'd go to
[L103] [03:03.12] like you try five different search
[L104] [03:04.80] engines to like hopefully find the thing
[L105] [03:06.32] that you wanted. And I, and it's funny
[L106] [03:08.08] because I distinctly remember my
[L107] [03:09.92] roommate in March of 2000 saying like,
[L108] [03:12.56] "Hey, there's this site, this search
[L109] [03:14.32] engine that looks a bit better." I think
[L110] [03:15.76] it was still stanford.google.edu.
[L111] [03:18.24] And I was like, "Oh, this is better."
[L112] [03:19.52] And like, you know, and then you started
[L113] [03:22.16] reading and they they were just so
[L114] [03:23.28] different, right? Yahoo was all like
[L115] [03:24.80] very cluttered and like they tried to be
[L116] [03:26.48] very sparse and um were more I think
[L117] [03:30.16] principled about it at that time and
[L118] [03:31.92] then you know like a lot of things you
[L119] [03:33.92] start seeing people who you know who
[L120] [03:35.44] gets a job there and you're like oh man
[L121] [03:37.36] they're taking really good people like I
[L122] [03:38.96] want to work with with those people and
[L123] [03:41.12] I felt like they just you know really
[L124] [03:43.60] got the web like especially at that time
[L125] [03:45.68] like Microsoft didn't around that time
[L126] [03:47.12] Microsoft killed the internet explorer
[L127] [03:49.28] project alto together and I was like
[L128] [03:50.72] this is the portal into the web and you
[L129] [03:52.56] guys are you know, dismantling it.
[L130] [03:54.48] Whereas, you know, Google was way more,
[L131] [03:56.16] you know, web forward. And so, between
[L132] [03:57.68] that and like the quality of engineering
[L133] [03:59.20] and the and the impact they were having,
[L134] [04:01.68] you know, certainly a place that I was
[L135] [04:03.60] really excited to go to coming out of
[L136] [04:05.28] school.
[L137] [04:05.84] >> And what was the culture like there at
[L138] [04:08.00] the time? Like, um, I think in some of
[L139] [04:10.24] your writing, you talked about like
[L140] [04:11.52] product versus infrastructure. You know,
[L141] [04:14.08] a lot of companies, especially ones that
[L142] [04:16.00] get big like that, you know, it's kind
[L143] [04:17.84] of like whatever they were good at first
[L144] [04:19.20] is I feel like the founders always have
[L145] [04:21.36] a have a soft spot uh for, right? So, uh
[L146] [04:24.80] certainly in information retrieval and
[L147] [04:26.88] and infrastructure, right, were like key
[L148] [04:29.60] to, you know, growing that that company.
[L149] [04:32.64] And um whereas I was drawn there at the
[L150] [04:36.40] time because like, you know, they put
[L151] [04:37.44] out things like Gmail, right, which were
[L152] [04:39.52] vague, right? But it didn't um it still
[L153] [04:43.36] I think didn't have the the same cache
[L154] [04:45.12] inside the company right as the as
[L155] [04:46.72] search and that sort of thing. Um and so
[L156] [04:49.76] you know we when I was working on it
[L157] [04:52.08] calendar it was still like mostly
[L158] [04:54.24] consumer it was like kind of it was also
[L159] [04:56.96] sold to enterprises right but like we
[L160] [04:59.52] were not the ones making the money like
[L161] [05:00.80] we were probably a call center right at
[L162] [05:02.96] that point in time.
[L163] [05:04.08] >> I saw eventually you you ended up
[L164] [05:05.76] leaving Google and I from your post it
[L165] [05:08.32] looks like it was pretty bittersweet. So
[L166] [05:10.32] what left you to leaving Google?
[L167] [05:13.04] >> I had been there for 4 years. Um and you
[L168] [05:16.16] know uh I mean realistically like
[L169] [05:18.24] investing was a [laughter] thing like
[L170] [05:20.00] finances definitely changed after that
[L171] [05:22.08] four-year period uh ended. But you know
[L172] [05:25.20] also it was just tough like I I had a I
[L173] [05:28.72] guess a bad habit at that point of
[L174] [05:30.32] working really hard on things that like
[L175] [05:32.24] really were important to me but maybe
[L176] [05:33.84] weren't important to to Google, right?
[L177] [05:35.60] So like I worked on calendar that was
[L178] [05:37.20] pretty important. Um and then I worked
[L179] [05:39.20] on Google tasks which was like a very
[L180] [05:40.96] small feature within calendar right like
[L181] [05:42.88] probably at least two to three orders of
[L182] [05:45.12] magnitude fewer users right but I was
[L183] [05:47.12] really passionate about it and then I
[L184] [05:48.56] was really passionate about um the like
[L185] [05:51.84] the JavaScript infra and the the the uh
[L186] [05:55.04] closure that that suite of uh JavaScript
[L187] [05:57.20] tools and um you know it's great I mean
[L188] [06:00.88] I enjoyed and I'm proud of all the
[L189] [06:02.88] effort that I put into the things um you
[L190] [06:05.60] know that I went and wrote the the book
[L191] [06:06.80] on closure because I was motivated, but
[L192] [06:09.44] uh career-wise maybe not the best move,
[L193] [06:11.52] right? You're like, "But I'm doing all
[L194] [06:12.80] this high quality stuff," and you see
[L195] [06:14.16] other people getting recognized. You're
[L196] [06:16.40] like, "But I'm working so hard," you
[L197] [06:18.08] know, like that's, you know, kind of
[L198] [06:19.28] like the the harder not smarter uh type
[L199] [06:21.84] of mistake. Um and so, [clears throat]
[L200] [06:25.04] you know, it's kind of like I should go
[L201] [06:26.24] somewhere or try something else and see
[L202] [06:28.64] if like the things that I'm excited
[L203] [06:30.00] about are the things that like the
[L204] [06:31.28] company I'm working at is most excited
[L205] [06:33.44] about. later you came back into big tech
[L206] [06:36.24] and you you started working at Facebook.
[L207] [06:38.48] I understand that you were kind of like
[L208] [06:40.24] a JavaScript expert at the time and then
[L209] [06:42.96] one of your first big projects at at
[L210] [06:45.36] Meta was kind of build tooling in the
[L211] [06:48.40] Android codebase. So I want to know the
[L212] [06:50.40] story behind how you got involved in in
[L213] [06:52.48] that. So um at the time it was like
[L214] [06:55.92] Facebook's going to make a phone, right?
[L215] [06:57.52] Actually there were some failed projects
[L216] [06:59.04] but it was like this time it's really
[L217] [07:00.40] going to happen. we're gonna um partner
[L218] [07:03.52] with HTC. we're going to like fork
[L219] [07:05.36] Android and you know and and do some
[L220] [07:07.60] stuff and uh you know so that seemed
[L221] [07:11.28] super exciting right uh as a as a person
[L222] [07:13.92] you know just coming into the company
[L223] [07:15.92] and and I you know I had done like quite
[L224] [07:17.76] a bit of Java I was more JavaScript um
[L225] [07:21.28] but uh at this point this is also where
[L226] [07:26.00] you know they called it what uh face web
[L227] [07:28.24] the version of like they kind of like
[L228] [07:29.60] put HTML 5 Facebook on the phone and
[L229] [07:31.76] like that was clearly not working And um
[L230] [07:36.24] it was clear that like you know mobile
[L231] [07:38.08] was going to be the future. That was
[L232] [07:39.28] kind of make or break for the company.
[L233] [07:41.28] And uh suddenly
[L234] [07:44.24] you know a friend was like hey like I
[L235] [07:46.08] know you really like JavaScript but like
[L236] [07:48.72] you should really pick Java or Objective
[L237] [07:51.04] C and like get good at this if you want
[L238] [07:52.80] to be a product person. And that was
[L239] [07:54.72] really really great advice. And so I was
[L240] [07:56.64] like well I like Java. I don't like
[L241] [07:57.76] Objective C. So like let's go. Um, and
[L242] [08:01.12] so that's how I, you know, found myself
[L243] [08:03.20] on that project. Um, and I,
[L244] [08:08.64] you know, we we had a very short
[L245] [08:11.36] timeline because unlike almost every
[L246] [08:13.92] other project, there was a hard
[L247] [08:16.16] deadline. Usually, you know, you ship
[L248] [08:17.60] when it's ready. This was like, nope, we
[L249] [08:19.84] got to send a bill to HTC because
[L250] [08:21.36] they're going to like burn it into
[L251] [08:22.80] phones on like March 1st or whatever it
[L252] [08:24.80] was. Um, so, you know, it was really a
[L253] [08:28.32] scramble. Um, but and and
[L254] [08:33.12] the the original Android code base was
[L255] [08:36.08] or a bunch of it was also like inherited
[L256] [08:38.56] from a contractor that Google paid. Like
[L257] [08:40.64] it's like Facebook didn't want to make
[L258] [08:42.56] like a native app and they paid some guy
[L259] [08:44.80] and then it was like the app in the
[L260] [08:46.08] store and they're like here the code's
[L261] [08:47.20] yours now and we should have thrown it
[L262] [08:49.12] away but we didn't. And there were a lot
[L263] [08:51.28] of things that were that were
[L264] [08:52.00] frustrating but also like iteration time
[L265] [08:54.32] right I think for everybody if you had
[L266] [08:56.56] been a web developer for such a long
[L267] [08:58.24] time you're used to this edit refresh
[L268] [09:00.32] and then you know it like the Android
[L269] [09:02.24] build system was was rough right it was
[L270] [09:04.64] this um like some build tools and ant
[L271] [09:08.00] like there were no there was no way to
[L272] [09:10.48] modularize it out of the bot like we had
[L273] [09:12.48] to hack it up just to even have like
[L274] [09:13.92] four modules or five modules or
[L275] [09:15.92] something like that. Um, and it was so
[L276] [09:20.40] painful to get anything done
[L277] [09:24.00] uh that I was like, I need to I need to
[L278] [09:25.52] fix the build system. Like I was like, I
[L279] [09:26.88] know I've done a lot with Java. I know
[L280] [09:28.56] it's not like fundamentally this slow to
[L281] [09:31.12] like iteratively, you know, build this
[L282] [09:33.60] sort of thing. And so, uh, you know,
[L283] [09:36.80] Facebook has this hackathon culture. So,
[L284] [09:38.80] I was like, all right, hackathon.
[L285] [09:41.04] Totally going to like make a new build
[L286] [09:42.64] system. um you know like unceremoniously
[L287] [09:45.52] in the style of of Google's uh build
[L288] [09:47.68] system. Um and there's actually another
[L289] [09:49.92] build system called FB build that was
[L290] [09:52.00] already a different uh mirror of of the
[L291] [09:55.52] Google build system as well. Uh, that
[L292] [09:57.60] one's written in in Python. I only did
[L293] [09:59.36] C++. But, um, yeah. And I was like,
[L294] [10:03.12] either I'm going to make this work or
[L295] [10:04.88] and like and then I'm gonna be happy to
[L296] [10:06.88] be a developer or like I don't even know
[L297] [10:08.56] if I'm going to make it here because
[L298] [10:10.56] it's just going to be like tearing my
[L299] [10:11.60] hair out, you know, working on this
[L300] [10:13.20] thing. And uh,
[L301] [10:15.92] >> so if you if you didn't fix this, you
[L302] [10:18.16] would have quit the company if it
[L303] [10:20.56] >> was I mean it was I was like or I'll at
[L304] [10:22.88] least switch projects or I need to find
[L305] [10:24.64] a way to find a happy place, right? and
[L306] [10:26.40] and come into work every day. Like I
[L307] [10:27.92] came I want to write code. I want to do
[L308] [10:29.36] work. I just want to you know try to do
[L309] [10:31.52] my best work. Um and so it was funny
[L310] [10:34.88] actually I give people credit. A lot of
[L311] [10:36.64] people told me what I was doing was a
[L312] [10:39.12] very bad idea. Um almost everybody
[L313] [10:42.00] except one person. Um it was a senior
[L314] [10:44.96] Android engineer. Uh but nobody said no,
[L315] [10:49.04] you know, whereas I felt like at Google
[L316] [10:50.64] like people said no more. Um, and so,
[L317] [10:54.80] uh, so I just rolled with it and, you
[L318] [10:57.52] know, I quickly, relatively quickly, had
[L319] [10:59.52] something that was, you know,
[L320] [11:00.88] dramatically better, like at least like
[L321] [11:02.48] twice as fast or something like that.
[L322] [11:04.56] And, uh, so that, you know, that turned
[L323] [11:08.00] a lot of heads and people were like,
[L324] [11:10.32] okay, you know, [laughter] I guess we,
[L325] [11:12.08] yeah, we'll go with that one, right?
[L326] [11:13.52] Like I think the interesting thing to me
[L327] [11:15.84] is it seemed like all the odds were
[L328] [11:18.80] stacked in your a lot of people who are
[L329] [11:20.48] an engineer noticed the same problem
[L330] [11:22.40] would not have chosen to start the
[L331] [11:25.52] project because there's an existing one
[L332] [11:28.00] and then also Google's got some you know
[L333] [11:30.48] competing one maybe you're not going to
[L334] [11:32.00] beat that one.
[L335] [11:33.12] >> What gave you the conviction that your
[L336] [11:36.00] your project could beat the other ones
[L337] [11:38.16] and become the default?
[L338] [11:39.84] >> Yeah I mean I guess a couple things. I
[L339] [11:41.36] mean one like I said I you know I'd done
[L340] [11:42.96] other Java stuff I was like like this
[L341] [11:44.72] shouldn't be that slow or just as a
[L342] [11:46.00] software engineer like this
[L343] [11:47.20] fundamentally should not be as slow um
[L344] [11:51.12] as it is and there yeah most of the
[L345] [11:55.04] actually most of the push back was of
[L346] [11:57.28] the nature like well if we deviate from
[L347] [11:58.96] the standard thing um you know we're not
[L348] [12:01.84] going to be on the standard thing and
[L349] [12:02.88] what if it gets like 100x better next
[L350] [12:04.88] week and now we're stuck on your thing.
[L351] [12:07.36] Um which is really funny when you think
[L352] [12:09.20] about it because there's like so many
[L353] [12:10.56] things like you know making their own
[L354] [12:12.56] you know uh PHP virtual machine at
[L355] [12:15.36] language right like they've certainly
[L356] [12:17.12] embraced doing their own thing many
[L357] [12:18.88] times why this one was different I don't
[L358] [12:21.28] know I mean it was it was just I guess
[L359] [12:22.72] everything about mobile was like how are
[L360] [12:24.48] we going to make this work I guess there
[L361] [12:25.60] was just like a lot of fear and you know
[L362] [12:28.16] again like timelines it's like we have
[L363] [12:29.60] the senior person like why it seems
[L364] [12:32.08] sounds like they're going to go off and
[L365] [12:33.04] do a science project but we have a hard
[L366] [12:34.64] deadline like is that the best use of
[L367] [12:36.16] our of our time. Um, but you know, it it
[L368] [12:40.80] worked out. It worked out. I will say
[L369] [12:42.88] another thing too was um I also tried to
[L370] [12:47.52] to couch it a little bit. I was like,
[L371] [12:49.04] "Hey, I'm just I'm just trying to make
[L372] [12:50.56] an Android build system. I'm not trying
[L373] [12:51.92] to like take over the company. I'm not
[L374] [12:53.12] trying to change anyone else's project,
[L375] [12:54.80] right?" Um because I certainly felt that
[L376] [12:58.24] that was going to cause more I was going
[L377] [12:59.76] to invite more friction. Um, and so, you
[L378] [13:03.92] know, I I knew that it it I tried to
[L379] [13:06.96] make it in a way that it could support
[L380] [13:09.36] more of the company, but I never I never
[L381] [13:11.76] pushed it. And so I was like really
[L382] [13:12.96] heartened when the year or so later the
[L383] [13:15.12] iOS people were like, "Hey, our built
[L384] [13:17.28] system sucks. [laughter] Can we, you
[L385] [13:18.48] know, can we use Buck?" I was like,
[L386] [13:19.84] "Yeah, sure." Like I don't, you know,
[L387] [13:22.16] come on board.
[L388] [13:23.04] >> Yeah. That that's also another
[L389] [13:24.24] interesting because you you came in and
[L390] [13:26.40] you didn't have a whole lot of
[L391] [13:27.84] credibility. you were just hired
[L392] [13:29.92] >> and then you're trying to build
[L393] [13:31.84] something and get every and also
[L394] [13:33.84] everyone's saying don't do this
[L395] [13:36.16] >> and then you have to convince them hey
[L396] [13:38.08] this is the right direction how do you
[L397] [13:40.64] influence that change without any
[L398] [13:42.48] credibility
[L399] [13:43.92] >> I I mean I borrowed some um there's one
[L400] [13:46.56] senior Android engineer you know who was
[L401] [13:48.56] also ex Google um John Perllo and he was
[L402] [13:51.76] like I think he said right he's like
[L403] [13:53.44] you're going to do it just do it fast
[L404] [13:54.64] before like anyone gets you know like
[L405] [13:56.24] cancels you or something he's like but
[L406] [13:57.44] I'll support you if you if you get this
[L407] [13:59.36] done. So he was one of the first people
[L408] [14:00.72] and he was a very prolific uh coder. So
[L409] [14:03.36] he was like genuinely very happy to have
[L410] [14:05.60] a faster dev cycle. Um so he was one of
[L411] [14:08.56] the first people to you know give it
[L412] [14:09.92] kudos and I think that that helped a
[L413] [14:12.08] lot. Um also but I will say you know I I
[L414] [14:16.56] made a big some big mistakes uh on my
[L415] [14:19.84] way in there. you know, you mentioned
[L416] [14:21.28] like about having no credibility is
[L417] [14:23.04] like, you know, I came from Google and I
[L418] [14:25.52] was like, "Oh, this is where, you know,
[L419] [14:27.04] the Expell Labs people are like all
[L420] [14:28.72] these like great people." And then you
[L421] [14:30.16] go to like Facebook, you're like, "Oh,
[L422] [14:31.92] it's a bunch of college kids. How could
[L423] [14:33.12] they possibly know what they're doing,
[L424] [14:34.72] right?" And you, you know, I made a few
[L425] [14:36.80] times certainly I made the mistake like,
[L426] [14:38.64] "Well, at Google, we did it this way."
[L427] [14:40.32] And people were like, "We really don't
[L428] [14:41.84] care." You know, and they were they were
[L429] [14:44.16] right in in in most cases, right? that
[L430] [14:47.12] like just because it worked there didn't
[L431] [14:49.04] mean it was going to work here.
[L432] [14:50.88] >> One one last thing on this topic is I
[L433] [14:53.68] mean what you built was
[L434] [14:56.48] way more performant than anything else
[L435] [14:58.64] by you know many multiples. What's the
[L436] [15:02.08] intuition like the technical intuition
[L437] [15:03.84] behind what was done and what you did
[L438] [15:05.84] that made it so much more efficient? I
[L439] [15:08.64] think the the big thing was is that I
[L440] [15:10.80] just sat down and looked at the um the
[L441] [15:14.00] tool from Google and I was like what is
[L442] [15:15.84] it actually doing right and and where
[L443] [15:19.20] and uh I think the big thing is that the
[L444] [15:21.12] Google one would kind of just if you
[L445] [15:23.84] changed anything it would just start
[L446] [15:25.20] over from scratch and so that's why it
[L447] [15:27.28] was so slow especially for for
[L448] [15:28.64] incremental builds and so then I started
[L449] [15:31.12] really understanding like okay but what
[L450] [15:32.88] depends on what because there is these
[L451] [15:34.56] um still are I'm sure like Android
[L452] [15:36.40] resources which had like a very bespoke
[L453] [15:38.32] thing and it was it was complicated. Um,
[L454] [15:41.60] and because it was somewhat complicated,
[L455] [15:43.76] I think that's probably why I just by
[L456] [15:45.12] default I blew everything away and
[L457] [15:46.64] started over. Um, but once I got in
[L458] [15:49.20] there and I was like, oh, okay, you
[L459] [15:50.96] know, we can take advantage of it. If
[L460] [15:52.24] these things don't change, then, you
[L461] [15:54.08] know, we can cache this result from this
[L462] [15:55.60] step. We don't have to redo it. And like
[L463] [15:57.20] suddenly, you know, that made things
[L464] [15:59.20] like quite a bit faster. And then also
[L465] [16:00.96] just even um supporting the idea that
[L466] [16:04.24] you could have more than like the four
[L467] [16:06.32] modules that we had. I mean I think I
[L468] [16:08.08] think every time someone added a module
[L469] [16:09.76] you know they had to add like 200 lines
[L470] [16:12.00] of XML of like AMP build script that
[L471] [16:14.00] like nobody really understood and so it
[L472] [16:15.92] was not so no one no one wanted to
[L473] [16:18.24] modularize anything right you didn't
[L474] [16:19.60] want to be responsible for that so a big
[L475] [16:21.12] thing with buck was making it that it
[L476] [16:22.40] was like a lot um simpler to add a new
[L477] [16:24.88] module and so then that also meant we
[L478] [16:27.28] ended up with more modules and then
[L479] [16:29.04] builds are more incremental as a result
[L480] [16:30.80] right so it's really a change in the the
[L481] [16:32.96] mindset
[L482] [16:33.84] >> so less redundant work basically
[L483] [16:35.60] >> yeah after you saw solved this uh build
[L484] [16:38.16] problems I guess in Android uh builds
[L485] [16:40.56] and I obviously I went later to further
[L486] [16:43.28] parts of the company. I saw that you
[L487] [16:45.76] started to work more on like the IDE.
[L488] [16:48.00] What was the problem that you saw that
[L489] [16:50.24] you saw in ideides that made you want to
[L490] [16:52.16] get into that? So I yeah I took I did a
[L491] [16:56.16] brief stint after Buck on Messenger
[L492] [17:00.64] uh uh iOS messenger. So I was like okay
[L493] [17:02.88] I've done Android maybe I should
[L494] [17:04.32] actually branch out even though I don't
[L495] [17:05.60] like it. Um, and I still didn't like it.
[L496] [17:08.96] Um, I people don't even realize in in in
[L497] [17:12.40] Objective C, there's a thing that
[L498] [17:14.32] happens for a long time now called ARC.
[L499] [17:16.40] Um, like the automatic uh reference
[L500] [17:18.72] counting like nowadays the compiler
[L501] [17:21.20] injects it, but you used to have to like
[L502] [17:22.80] actually add code into Objective C to do
[L503] [17:25.68] every like reference count like memory
[L504] [17:28.88] allocation.
[L505] [17:29.68] >> Yeah. or like every reference that you
[L506] [17:31.20] created like you would have to do it and
[L507] [17:33.20] um and the and and most people have
[L508] [17:36.16] never seen this type of code but the iOS
[L509] [17:38.24] messenger code that came in through
[L510] [17:39.60] acquisition was so old that it was still
[L511] [17:41.20] written in this other way and it's it's
[L512] [17:43.04] it's incredibly painful. Um I guess now
[L513] [17:45.52] you'd have like codeex cleaned it up or
[L514] [17:47.20] something like that but at the time we
[L515] [17:48.64] just sucked it up and and and just Xcode
[L516] [17:51.12] just didn't you know feel right to me. I
[L517] [17:53.20] didn't like header files and
[L518] [17:54.48] implementation files. I still don't. Um
[L519] [17:57.84] and and also the I would say
[L520] [18:02.16] for both Android and iOS, you know,
[L521] [18:04.16] Facebook always had like the biggest
[L522] [18:05.52] app, right? We had like one app with
[L523] [18:07.92] every with every feature in it and we,
[L524] [18:10.08] you know, would ship it as opposed to
[L525] [18:11.44] Google with like they'd have like a
[L526] [18:12.88] drive app and a no, you know, a Sheets
[L527] [18:15.28] app or whatever. But they also owned one
[L528] [18:17.44] of the platforms so they could put 20
[L529] [18:19.04] apps by default on there. And so what
[L530] [18:21.76] that meant was is that Facebook was
[L531] [18:23.84] always hitting the scaling limits of
[L532] [18:25.84] every mobile developer tool before
[L533] [18:28.24] everybody else. Um which was painful but
[L534] [18:31.12] you know actually as a dev tools person
[L535] [18:32.64] was kind of interesting because we got
[L536] [18:33.76] to solve problems that nobody had solved
[L537] [18:35.52] before. Um and and like you know not
[L538] [18:37.84] just as a science project but because it
[L539] [18:39.44] was like real you know business value.
[L540] [18:42.24] >> Um and so you know Xcode similarly we we
[L541] [18:46.24] talked to Apple like hey Xcode is like
[L542] [18:48.00] not really scaling to our project.
[L543] [18:49.28] They're like, "Your project's too big.
[L544] [18:50.48] You should make it smaller." Like that
[L545] [18:51.76] was [laughter] kind of the feedback that
[L546] [18:52.96] we got from them. And so it seemed
[L547] [18:55.12] justifiable to like go and build an an
[L548] [18:58.00] editor. It was similar thing. It was
[L549] [18:59.52] like I was like what is you know what is
[L550] [19:00.72] an ID you know doing right? It's like
[L551] [19:03.36] it's talking to clang like the language
[L552] [19:04.96] server and that sort of stuff. I was
[L553] [19:06.24] like we could build like a nicer shell
[L554] [19:08.16] on top of that you know then we had
[L555] [19:09.84] started by that point um deviating from
[L556] [19:13.20] git and switching to Mercurial as a
[L557] [19:14.88] company. I was like no one's going to
[L558] [19:15.92] support material out of the box, right?
[L559] [19:17.44] And so like that should happen and then
[L560] [19:19.44] like oh actually if if buck is going to
[L561] [19:21.28] be our build system then like we really
[L562] [19:23.52] like you know like that's Xcode is never
[L563] [19:25.36] going to do all of these bespoke
[L564] [19:27.60] Facebook things right so it seemed
[L565] [19:29.36] justifiable to like invest the time to
[L566] [19:32.72] um to try to like improve that
[L567] [19:35.52] experience and I didn't feel that way
[L568] [19:38.08] about Android because Intelligj was
[L569] [19:39.84] actually like quite good and we had
[L570] [19:40.88] figured out how to make that work at
[L571] [19:42.16] scale but but Xcode was a little more
[L572] [19:44.16] difficult at that point. So there was
[L573] [19:46.24] Xcode which was bad, didn't fit the
[L574] [19:48.96] existing needs.
[L575] [19:50.56] >> And then there was another IDE that
[L576] [19:53.28] another team was building. I think it
[L577] [19:55.12] was web- based if I it was it was web-
[L578] [19:57.76] based. Um I'm not laughing at that part.
[L579] [20:01.04] That part's fine. It was but it was
[L580] [20:02.96] built off of uh an abandoned Google open
[L581] [20:06.24] source project written in Gwit, which is
[L582] [20:09.12] Google Web Toolkit where you would write
[L583] [20:11.12] um Java and it would codegen to to
[L584] [20:13.44] JavaScript for everything.
[L585] [20:15.60] And um I tried to build on what they
[L586] [20:18.48] had. I tried to build some credibility
[L587] [20:20.00] even actually sped up their build a bit.
[L588] [20:21.92] Um but again kind of like looking at the
[L589] [20:24.56] iteration times and also I was like this
[L590] [20:26.48] is an abandoned open source project.
[L591] [20:28.96] it's written in Google web toolkit and I
[L592] [20:30.88] was like we are the react company at
[L593] [20:32.88] that point right right like how why why
[L594] [20:36.40] would we not empower you know people who
[L595] [20:38.80] want to build dev tools to use you know
[L596] [20:41.44] uh you know to build on a you know
[L597] [20:43.84] technologies that we are the leader in
[L598] [20:46.32] and actually really like because you
[L599] [20:47.84] know we think we're actually really good
[L600] [20:50.08] um so I was like you guys are crazy and
[L601] [20:54.34] [laughter] so so I started go and and
[L602] [20:56.32] it's similar to the thing where I you
[L603] [20:57.60] know I mentioned with the book I was
[L604] [20:58.80] like, I started it as the the Java build
[L605] [21:01.28] tool, not the everything build tool,
[L606] [21:02.80] right? I was like, it was a similar
[L607] [21:04.08] thing. I was like, hey, I'm going to go
[L608] [21:05.36] over here and start this other editor,
[L609] [21:07.76] but we're just we're just going to focus
[L610] [21:09.44] on iOS. Like you I'm not trying to take
[L611] [21:12.00] things over.
[L612] [21:12.72] >> Yeah. You didn't want all the friction.
[L613] [21:14.24] And I mean that team, they had all the
[L614] [21:17.12] existing users though, right? They had
[L615] [21:18.72] thousands of engineers.
[L616] [21:20.24] >> I maybe a thousand. I think eventually
[L617] [21:23.84] leadership sided with um what eventually
[L618] [21:26.88] became New Clyde which is what you what
[L619] [21:28.64] you built.
[L620] [21:29.68] >> Um but why did they side with you when
[L621] [21:32.32] you didn't have any users on your your
[L622] [21:34.64] product?
[L623] [21:35.60] >> Yeah, I mean I think it was combination
[L624] [21:37.12] of two things. I mean, I think the the
[L625] [21:38.56] arguments that I made in favor of um
[L626] [21:42.16] like the technology stack to build on.
[L627] [21:44.56] Um another was that um
[L628] [21:48.16] uh newly was was a desktop application
[L629] [21:51.36] and part of it was if this is actually
[L630] [21:52.96] going to be a an iOS, you know, Xcode
[L631] [21:55.20] replacement, like people are going to
[L632] [21:56.64] want to use it need to be able to talk
[L633] [21:58.48] to the simulator or plug in the phone or
[L634] [22:00.24] whatever. Like in theory, we could go
[L635] [22:01.68] through the web and do all those things,
[L636] [22:02.80] but it just seems like a lot more a lot
[L637] [22:04.64] of extra work. Um and um and I think the
[L638] [22:10.16] other part is that you know I had built
[L639] [22:12.96] up some credibility with the the buck
[L640] [22:14.96] thing that um they're willing to like
[L641] [22:18.00] take a gamble like well the last thing
[L642] [22:20.16] you know worked out like we'll try this
[L643] [22:22.08] one.
[L644] [22:22.96] >> I saw that this in combination with some
[L645] [22:25.12] of your other work led to your promotion
[L646] [22:27.20] to E8 which is also known as principle
[L647] [22:29.44] in the industry. What was your reaction
[L648] [22:31.92] to that at the time? Yeah, I mean
[L649] [22:34.72] certainly I was I was very excited. Um
[L650] [22:37.52] you know I felt like you know in the
[L651] [22:39.28] ways that I
[L652] [22:41.28] um had been out of step. I felt like you
[L653] [22:43.44] know when I was at Google I was like
[L654] [22:45.12] this was also not just it was also
[L655] [22:47.44] validation that like oh now I'm also
[L656] [22:49.76] growing not just like technically but
[L657] [22:51.20] like understanding like what it means to
[L658] [22:52.80] kind of you know do the things that like
[L659] [22:54.16] are in line with your uh employer. Um
[L660] [22:57.36] and so like that also just you know was
[L661] [22:59.92] equally valuable or satisfying. I I know
[L662] [23:02.48] that uh Newcloud was open source and I
[L663] [23:04.56] think Buck was as well if I recall
[L664] [23:06.32] correctly. What's the rationale for open
[L665] [23:08.72] sourcing if um yeah like what are the
[L666] [23:10.96] pros and cons of open sourcing
[L667] [23:12.56] technology that you build?
[L668] [23:14.24] >> Yeah, I mean let's see the buck is the
[L669] [23:17.44] more interesting one. Newly kind of
[L670] [23:18.80] didn't really get adopted externally. I
[L671] [23:21.60] I think in both cases I think
[L672] [23:24.88] um you know all these companies have
[L673] [23:27.84] benefited so much from open source like
[L674] [23:29.60] there I think there's just a feeling of
[L675] [23:30.88] like if this is not really the secret
[L676] [23:32.16] sauce like let's let's share this with
[L677] [23:34.72] with other people right like I mean done
[L678] [23:36.96] like codeex as well and a number of
[L679] [23:38.24] other things in my career so I do feel
[L680] [23:40.24] like that that that sharing of
[L681] [23:42.96] information is just good even if no one
[L682] [23:44.88] uses your tool just as like seeing as a
[L683] [23:47.44] reference of like how a thing could be
[L684] [23:48.88] done um could be
[L685] [23:51.60] um you know and in the in the better
[L686] [23:54.32] scenarios you actually get you know
[L687] [23:56.88] meaningful contributions back and and
[L688] [23:59.04] things like that and um you know I
[L689] [24:01.84] remember like I think Uber adopted Buck
[L690] [24:03.92] I think Airbnb did like it was funny
[L691] [24:05.52] right like I said like Facebook was the
[L692] [24:07.52] biggest app so we would hit all these
[L693] [24:08.72] problems first and then this next wave
[L694] [24:10.96] of companies would start these things
[L695] [24:12.56] and be like let's check out what these
[L696] [24:14.00] guys did um I think I mean honestly we
[L697] [24:17.44] also you know at at Google it the it's
[L698] [24:21.04] internally it's blaze externally it's
[L699] [24:22.64] basil. Uh so we were open source first
[L700] [24:24.88] and we always do we always did kind of
[L701] [24:26.16] wonder like if we put some pressure on
[L702] [24:28.08] like you know we get and you know
[L703] [24:29.76] ultimately I did I think I think I think
[L704] [24:31.76] we've gotten a little bit of credit from
[L705] [24:33.12] that unofficially from uh some of the
[L706] [24:35.04] folks who worked on that but I think
[L707] [24:37.12] also that you know we you know it's also
[L708] [24:40.08] like a recruiting thing too or just
[L709] [24:42.00] showing like hey if you want to like you
[L710] [24:43.60] know being at like the you know the the
[L711] [24:45.36] leading edge in like whatever area this
[L712] [24:47.52] technology is and you want to do this
[L713] [24:48.88] all the time not just as like a driveby
[L714] [24:50.72] contributor like you know this is what
[L715] [24:52.56] we do this we are and then this decision
[L716] [24:55.28] to open source is this was this a
[L717] [24:57.68] bottoms up decision where engineers said
[L718] [25:00.08] we're just going to do this or is this
[L719] [25:02.16] kind of also leadership buy in hey this
[L720] [25:05.28] is going to be valuable and you got like
[L721] [25:06.64] a dock is not
[L722] [25:08.32] >> yeah I think I think both cases it was
[L723] [25:11.44] certainly like bottoms up I don't think
[L724] [25:16.32] so you know things like react and
[L725] [25:18.96] pytorch like those are like the the big
[L726] [25:21.20] success stories right where where the
[L727] [25:23.28] value back to the company is like
[L728] [25:24.80] unquestionable and then there's this
[L729] [25:27.28] like longer tail of things where um I
[L730] [25:31.60] think depending on the economy and other
[L731] [25:33.12] things the managers get grumbly if they
[L732] [25:34.64] feel like their engineers are like doing
[L733] [25:36.00] too much open source or things like
[L734] [25:37.52] that. So, it's almost almost always um I
[L735] [25:40.72] feel like like bottoms up, I think.
[L736] [25:42.64] Yeah, I would say that's that's often
[L737] [25:44.24] the case. But it wasn't like met with a
[L738] [25:46.00] lot of resistance, you know, and you
[L739] [25:47.36] usually get like a good conference talk
[L740] [25:49.52] or two and a nice blog post and and
[L741] [25:51.28] those blog posts like, you know, do I
[L742] [25:53.68] would say b pay dividends over time,
[L743] [25:55.76] >> right? Recruiting stuff.
[L744] [25:57.76] >> Yeah. And like they have like like a
[L745] [25:59.20] longer shelf life than I think people
[L746] [26:00.96] realize.
[L747] [26:01.76] >> Okay. So, you got your your E8 promo at
[L748] [26:04.24] this point and
[L749] [26:05.44] >> I imagine the expectations uh maybe in
[L750] [26:08.08] your mind are kind of going up a little
[L751] [26:09.68] bit and now you need to go and find a E8
[L752] [26:13.04] problem, I guess.
[L753] [26:14.24] >> So, what did you do after you got proed?
[L754] [26:17.04] >> Uh I think that's where I did a uh I I
[L755] [26:20.24] got a little over my skis and I tried to
[L756] [26:22.24] help with web speed, I think is what I
[L757] [26:24.32] did. Um because again it was a thing
[L758] [26:26.40] that was like a really big problem for
[L759] [26:28.32] the like like the just the load time of
[L760] [26:30.32] facebook.com was was not uh in great
[L761] [26:33.12] shape. um you know the architecture was
[L762] [26:35.68] a bit stale um and it was just um the
[L763] [26:41.28] problem was so big and um and I didn't
[L764] [26:45.92] have
[L765] [26:47.76] I think the you know a lot of people who
[L766] [26:49.44] had worked on web at Facebook had worked
[L767] [26:51.20] on it for like a long time and like I
[L768] [26:52.80] had you know put myself in mobile and
[L769] [26:54.24] dev tools I actually wasn't in that
[L770] [26:56.48] world and um I remember I was like ah
[L771] [27:00.32] you know what do we do I mean actually
[L772] [27:01.44] sat down with another person we started
[L773] [27:02.80] like compiling piling V8 from source and
[L774] [27:05.52] trying to see like if we could like
[L775] [27:07.52] change the way that we generated
[L776] [27:08.80] JavaScript, if it was like it'd be
[L777] [27:10.16] friendlier to V8, like we're just trying
[L778] [27:11.44] like wacky things. Um, none of which
[L779] [27:13.92] panned out by the way. And I just it was
[L780] [27:17.44] it was there's different there's
[L781] [27:20.00] different people who are like good for
[L782] [27:21.36] different projects and I think that was
[L783] [27:22.80] just not the one. like I'm better in a
[L784] [27:25.84] project that involves writing a lot of
[L785] [27:27.28] code from the beginning and I think a
[L786] [27:29.60] project like that was like more about
[L787] [27:31.52] like looking at data and talking to a
[L788] [27:33.28] lot of people and like I just that's not
[L789] [27:35.52] my strength.
[L790] [27:36.72] >> I think you mentioned at this point in
[L791] [27:38.48] your career the the idea of a hero
[L792] [27:40.24] quest.
[L793] [27:40.72] >> Yeah.
[L794] [27:42.00] >> What's what's that mean? the idea that
[L795] [27:44.72] you know that uh [sighs]
[L796] [27:46.88] it's like you know it's embarrassing
[L797] [27:48.08] because there's like something about ego
[L798] [27:49.84] this idea that you know there's this
[L799] [27:51.44] like you know Gordian not and all these
[L800] [27:53.12] engineers are like if only someone would
[L801] [27:56.00] come in and like solve this you know
[L802] [27:58.40] engineering problem I was like I know
[L803] [28:00.08] JavaScript right
[L804] [28:02.24] um just come in that way and uh but I
[L805] [28:05.84] didn't I I definitely did not you know
[L806] [28:08.16] uh and I think that um it's been an
[L807] [28:10.96] important learning and I've had to
[L808] [28:12.16] relearn it like at least one other time
[L809] [28:13.60] that
[L810] [28:15.76] you know I can do a lot of things but
[L811] [28:18.08] there there is a smaller subset of
[L812] [28:20.16] things that I genuinely enjoy doing and
[L813] [28:22.88] that I'm going to be a lot more
[L814] [28:25.04] successful right if I stay in the things
[L815] [28:26.88] that I genuinely enjoy doing you know I
[L816] [28:28.96] try to expand that over time but you
[L817] [28:32.72] know we don't all have to be the best at
[L818] [28:34.96] everything right I think that's we
[L819] [28:36.64] should accept it and you know embrace it
[L820] [28:39.52] >> so then how did you find the EA problem
[L821] [28:41.76] after that like what was the next stair
[L822] [28:44.40] >> that was uh I think a bit of luck as
[L823] [28:47.60] well or I guess you know we had we had
[L824] [28:49.84] sometimes we'd have these little summits
[L825] [28:52.56] uh with like smaller groups of engineers
[L826] [28:54.56] about like brainstorming what's going to
[L827] [28:57.44] you know bite us in the future you I
[L828] [28:59.52] mentioned like you know the repo keeps
[L829] [29:00.88] growing you know they're going to hit
[L830] [29:03.12] some scaling problem at some point and
[L831] [29:04.96] um uh a person or my manager I think
[L832] [29:07.92] became my manager uh Brian Ovin
[L833] [29:10.56] um he decided to some people together to
[L834] [29:13.20] like work on making a virtual file
[L835] [29:15.12] system um to uh to to get try to get
[L836] [29:19.36] ahead of that that problem. Um and so we
[L837] [29:22.24] got myself and um Adam Simpkins and Wes
[L838] [29:24.64] Furlong um you know both tremendous
[L839] [29:27.28] engineers actually I was the worst
[L840] [29:28.56] engineer on the project for quite a bit.
[L841] [29:30.64] You mentioned a virtual file system.
[L842] [29:33.12] What on a high level, what's the benefit
[L843] [29:35.04] to a company like uh Meta for if you had
[L844] [29:38.40] something like that?
[L845] [29:39.44] >> If you uh have bought into the monor
[L846] [29:41.52] repo philosophy, right? Put all the code
[L847] [29:43.28] in one repo. Um you know, most things
[L848] [29:47.44] that people do need only a subset of
[L849] [29:50.80] that repo like have to look at the the
[L850] [29:52.64] files at any point in time. And um so
[L851] [29:56.72] the idea is that uh you know you design
[L852] [30:00.00] all your tooling around this virtual
[L853] [30:01.36] file system so that when you say uh
[L854] [30:03.76] clone the repo or then you update to a
[L855] [30:05.92] different commit or anything like that
[L856] [30:07.84] you don't actually have to like write
[L857] [30:09.44] out every single file in the repo on
[L858] [30:11.20] disk when you make that change which is
[L859] [30:12.64] which is the default in your you know
[L860] [30:13.92] traditional file system because that uh
[L861] [30:16.32] is going to grow proportionally to the
[L862] [30:17.84] time with the the size of the repo right
[L863] [30:19.76] so at some point you're you know going
[L864] [30:20.96] to be very sad and um and Uh and so you
[L865] [30:25.84] know there's actually kind of two at
[L866] [30:27.76] least two parts to it. One is um
[L867] [30:30.56] building this virtual file system that's
[L868] [30:32.72] like hey I know the user at this commit
[L869] [30:34.96] if if the operating system asked me for
[L870] [30:36.96] the contents of a file like I can go get
[L871] [30:39.20] it and it will appear like they had
[L872] [30:41.12] actually you know laid out all the
[L873] [30:42.40] files. Um the other part of it which is
[L874] [30:44.96] the part that I maybe I was actually
[L875] [30:46.08] better at I think is um then trying to
[L876] [30:49.28] anticipate well we have all these tools
[L877] [30:51.52] in our tool chain that are used to just
[L878] [30:54.16] reading all the files you know you just
[L879] [30:55.36] rip grap it just reads everything right
[L880] [30:57.04] that sort of thing and how do we start
[L881] [31:00.32] changing also our our development flow
[L882] [31:02.24] and our tools such that they are um uh
[L883] [31:06.32] designed with the virtual file system in
[L884] [31:08.16] mind because if you just you know
[L885] [31:09.36] materialize all the files with your tool
[L886] [31:11.04] now you've like actually just lost all
[L887] [31:13.12] the benefits that that you've made.
[L888] [31:15.76] >> So on a high level, it's basically just
[L889] [31:18.00] lazy loading a huge file system. So it's
[L890] [31:21.12] more efficient because you don't need to
[L891] [31:22.24] do everything at the beginning.
[L892] [31:23.68] >> Yeah.
[L893] [31:24.08] >> And so that part of this project that
[L894] [31:25.68] you said you're better at
[L895] [31:27.04] >> is is integrating everything into this
[L896] [31:29.92] on top of that primitive.
[L897] [31:31.44] >> Yeah. Yeah. So one thing that I did um
[L898] [31:34.24] actually with uh Hansen Wong who's here
[L899] [31:36.00] actually on the codeex team with me now
[L900] [31:38.40] um was I was like oh okay you know the
[L901] [31:40.88] the traditional way you have you know
[L902] [31:42.40] you want um really fast file search in
[L903] [31:44.72] your in your IDE and your editor and you
[L904] [31:47.44] know the way most of these things do is
[L905] [31:48.72] the first thing you do is they walk the
[L906] [31:50.00] entire file system to find out what the
[L907] [31:51.44] files are and I was like well that's
[L908] [31:53.12] going to be a that's going to be a
[L909] [31:54.08] serious problem right it's going to undo
[L910] [31:55.36] all the benefits like and and then it's
[L911] [31:57.92] one of these things is like not you know
[L912] [31:59.84] first it was like okay how can me
[L913] [32:02.40] implement file search that's not going
[L914] [32:04.16] to undo all the benefits. And then it
[L915] [32:06.72] was how can we do it even better than
[L916] [32:09.84] how it's done uh today. And so we ended
[L917] [32:13.52] up um building this file system called
[L918] [32:16.24] miles for for my files and it um you
[L919] [32:19.28] know on like kind of like a cron job it
[L920] [32:21.04] would index um it would ingest all the
[L921] [32:24.16] new commits that had come in on you know
[L922] [32:26.24] on trunk and keep track of like which
[L923] [32:29.04] files had been added or removed. So just
[L924] [32:31.20] like the names of the files, not the
[L925] [32:32.48] contents because all you need is the
[L926] [32:33.68] names. And um and then and then Hansen
[L927] [32:37.76] had some clever ideas about how we
[L928] [32:39.52] maintained that index um such that we
[L929] [32:43.04] could support fuzzy file matching. So
[L930] [32:45.12] instead of just substring matching,
[L931] [32:46.64] right? Like you type, you know, like a
[L932] [32:48.48] if you have like a camelc case thing,
[L933] [32:50.08] you want to be able to type just maybe
[L934] [32:51.20] the uppercase letters or just your
[L935] [32:52.64] spelling's bad or what have you. Um and
[L936] [32:56.16] so it came up with this really uh
[L937] [32:57.92] interesting way to represent uh you know
[L938] [33:00.80] kind of all the files that had been seen
[L939] [33:02.16] at some point and then some bits to
[L940] [33:03.76] represent um you know if I'm at this
[L941] [33:06.32] commit was this file present or not
[L942] [33:08.96] present at that point in time and then
[L943] [33:12.08] also when you ask you sent a query to
[L944] [33:15.44] this thing so you'd send like what
[L945] [33:16.64] commit you're at and like if you've
[L946] [33:18.16] added any files locally or removed any
[L947] [33:20.24] locally. Um, and I think we got this,
[L948] [33:23.44] you know, like, you know, over a million
[L949] [33:25.52] files in like, I don't know, like 10 to
[L950] [33:28.48] 20 milliseconds or something like that.
[L951] [33:30.16] So that you would be in your editor, you
[L952] [33:31.68] know, typing. And so that was way faster
[L953] [33:34.16] than uh I think than you know, like what
[L954] [33:36.48] Xcode or or like VSS code or something
[L955] [33:38.48] like would give you um out of the box.
[L956] [33:41.76] And uh so so that was you know, so like
[L957] [33:44.08] it was solving a problem for Eden that
[L958] [33:47.12] was the name of the file system
[L959] [33:48.00] originally, the virtual file system. um
[L960] [33:51.12] you know in anticipation before it was
[L961] [33:53.12] even ready um but then it was so fast um
[L962] [33:56.48] and it was available as a trip service
[L963] [33:58.08] internally like people started using it
[L964] [33:59.84] for all sorts of other things I think
[L965] [34:01.28] when I left like I don't know I think
[L966] [34:03.36] there were these like 30 servers running
[L967] [34:04.88] mile like spread around the globe
[L968] [34:06.90] [laughter] so clearly that was more than
[L969] [34:08.88] just people like personally searching
[L970] [34:10.64] for files and then you did that much you
[L971] [34:12.32] know capacity
[L972] [34:13.36] >> interesting yeah I mean when you talked
[L973] [34:14.72] about I guess the implementation details
[L974] [34:18.56] most most people They they don't use
[L975] [34:20.88] leak code on the job. But that sounds
[L976] [34:23.76] like I was thinking about the I don't I
[L977] [34:26.56] don't even know how you put that. Is it
[L978] [34:27.84] like a tree like a try thing?
[L979] [34:29.92] >> No. So that's what's funny that Yeah. Um
[L980] [34:33.04] this was this was pretty cool in that um
[L981] [34:35.92] we we had kind of like two parallel
[L982] [34:39.28] arrays. One was like the file contents
[L983] [34:42.56] and one was uh maybe an integer into
[L984] [34:45.28] that um index. I forget. And then we had
[L985] [34:48.96] a we had a 64-bit um
[L986] [34:53.60] uh mask that was like it was like so you
[L987] [34:56.00] had like 26 lowercase 26 capital 10
[L988] [35:00.08] digits and like maybe dash and whatever.
[L989] [35:02.32] And uh and it would and it was uh every
[L990] [35:04.72] bit was set if the um if that character
[L991] [35:08.80] was used at all in the file that you
[L992] [35:10.80] were searching. And so the first thing
[L993] [35:11.92] was we could like blow through that list
[L994] [35:15.60] and um you know exclude a bunch of
[L995] [35:17.84] things like right off the top. But we
[L996] [35:20.32] was also like very designed like all
[L997] [35:21.92] these arrays were in parallel to each
[L998] [35:23.76] other so that
[L999] [35:25.12] >> for like cache wise we knew it' be very
[L1000] [35:27.12] efficient for for the CPU to to like
[L1001] [35:30.08] read memory you know linearly and then
[L1002] [35:32.48] it lend itself to you could just
[L1003] [35:33.92] partition that array it, you know, lend
[L1004] [35:35.92] itself to parallelism. Um, so it was
[L1005] [35:38.96] really Yeah, I should really probably
[L1006] [35:40.48] write it up at some point because I that
[L1007] [35:42.48] is really cool. It was It was f because
[L1008] [35:44.56] it wasn't just kind of like out of the
[L1009] [35:46.16] textbook. That's that's for sure.
[L1010] [35:48.00] >> I understand that. Um, yeah, you worked
[L1011] [35:50.40] on Eden and then obviously there's Miles
[L1012] [35:52.72] as well.
[L1013] [35:53.92] >> Um, and then these eventually led to
[L1014] [35:55.92] another promotion and um, but prior to
[L1015] [35:58.72] that promotion, there was some learnings
[L1016] [36:00.88] you might have had about influence and
[L1017] [36:02.88] conflict in org. So maybe if you want to
[L1018] [36:05.04] share that. Yeah, I mean that's
[L1019] [36:09.04] one of the things I guess about being an
[L1020] [36:11.12] E8 um who primarily writes code, right?
[L1021] [36:15.44] Um there's other people I'd say actually
[L1022] [36:18.08] the majority of people that level or
[L1023] [36:19.52] higher are not writing code, right?
[L1024] [36:22.24] They're they're actually kind of
[L1025] [36:23.52] exclusively spent doing more like
[L1026] [36:25.92] influence or working across teams, you
[L1027] [36:28.08] know, writing the big Google doc and
[L1028] [36:30.08] getting everyone on board and all that
[L1029] [36:32.24] um sort of stuff. And so, you know,
[L1030] [36:37.04] as an E8 trying to have that level,
[L1031] [36:39.20] like, you know, that level of impact
[L1032] [36:40.72] that you're expected to have, it's like,
[L1033] [36:42.64] oh, it's hard to do that just writing
[L1034] [36:44.00] code. So, it's like I need to spend at
[L1035] [36:45.28] least some time probably probably
[L1036] [36:49.52] influencing other people. That would
[L1037] [36:50.88] probably be be good for me. That would
[L1038] [36:52.32] probably make my manager happy. Um, and
[L1039] [36:56.96] I think
[L1040] [36:59.12] uh
[L1041] [37:00.80] you know sometimes you're just so
[L1042] [37:03.76] uh confident in in some uh insights you
[L1043] [37:07.52] have that or certainly I was that I
[L1044] [37:10.40] would just I I just came down like way
[L1045] [37:12.32] too hard I would say and uh and that did
[L1046] [37:16.16] not go well for me and yeah and so like
[L1047] [37:18.88] like uh promo got delayed because I was
[L1048] [37:21.92] very excited are anxious about uh when
[L1049] [37:27.52] Microsoft acquired GitHub
[L1050] [37:31.36] and uh oh yeah because new Clyde was
[L1051] [37:33.36] built on this um you know primarily
[L1052] [37:34.96] GitHub technology and I was like that's
[L1053] [37:36.80] going to go away because VS Code's going
[L1054] [37:38.72] to not make them be a project anymore
[L1055] [37:40.96] which was true which did happen and I
[L1056] [37:44.48] was just so
[L1057] [37:46.64] uh anxious that that this was like now a
[L1058] [37:49.52] risk right and I was pushing people but
[L1059] [37:51.28] you know people were I didn't really
[L1060] [37:54.16] account for the fact uh that people were
[L1061] [37:56.88] happy with what they were doing at the
[L1062] [37:58.40] moment and like didn't want their cheese
[L1063] [38:00.40] moved, you know, like uh right out from
[L1064] [38:02.48] under them. And so um you know, I got
[L1065] [38:05.36] like a little bit of a talking to, you
[L1066] [38:06.80] know, I had to wait a little bit for
[L1067] [38:08.08] promo and things like that. But I you
[L1068] [38:10.08] know, I actually got some coaching I
[L1069] [38:12.88] think after that point. I can't remember
[L1070] [38:14.08] the exact chronology um to to work on
[L1071] [38:16.64] that like specifically. What's the
[L1072] [38:19.04] number one thing you learned about
[L1073] [38:20.32] coaching? I would say for me is like um
[L1074] [38:25.84] I think I'm more aware of like things
[L1075] [38:27.52] that trigger me like know be technical
[L1076] [38:30.48] decisions or what have you and recognize
[L1077] [38:33.20] when that's happening and be like okay
[L1078] [38:34.88] let's not act in that moment or you know
[L1079] [38:37.76] if I if I don't think I can have the
[L1080] [38:39.92] conversation like uh or I'm not the in
[L1081] [38:42.96] the best place to have it like maybe I
[L1082] [38:44.96] go talk to the person's manager instead
[L1083] [38:46.64] rather than like you know like bull and
[L1084] [38:48.40] china shop to the engineer and be
[L1085] [38:50.80] So, I have this thing. I'm thinking
[L1086] [38:52.08] about it this way. I'm kind of riled up
[L1087] [38:53.76] about it. Like, help me like how can I,
[L1088] [38:56.40] you know, work with your team or or
[L1089] [38:58.24] whatever like that's happened to you.
[L1090] [39:00.08] >> Well, it's interesting to me in your
[L1091] [39:02.32] career because the promo got postponed
[L1092] [39:05.92] and you were you were seeing that VS
[L1093] [39:08.48] Code was going to come up and the thing
[L1094] [39:10.32] that new cloud was built on was going to
[L1095] [39:12.56] go down and you were actually right in
[L1096] [39:16.64] hindsight too. like in the future that
[L1097] [39:19.12] is what happened and
[L1098] [39:21.44] >> you were battling for what was right yet
[L1099] [39:24.40] you were told calm down a little bit and
[L1100] [39:27.44] this so I mean what are your thoughts
[L1101] [39:29.44] when you saw things play out and you go
[L1102] [39:31.12] actually I was right the whole
[L1103] [39:32.72] >> um I did have some conversations like
[L1104] [39:35.20] about a year later and I was like hey
[L1105] [39:37.68] [laughter]
[L1106] [39:38.16] >> can we balance the ledger a little bit
[L1107] [39:39.92] like it didn't be pretty hard for that
[L1108] [39:41.84] thing and it was kind of good and we we
[L1109] [39:44.24] worked it out I would say
[L1110] [39:46.40] >> okay so I guess that the learning is
[L1111] [39:48.16] just
[L1112] [39:49.28] >> how you went about it, not what you were
[L1113] [39:51.52] like.
[L1114] [39:52.48] >> Yeah. Yeah. Um I would say that's true.
[L1115] [39:56.48] >> You seem to have a great time at Meta
[L1116] [39:58.96] and eventually you left. So what was the
[L1117] [40:01.60] thing that drew you to OpenAI?
[L1118] [40:04.00] >> Yeah, I mean um a number of things. I
[L1119] [40:06.72] mean one was uh so I I interviewed at
[L1120] [40:09.28] the end of 2023 with OpenAI I believe
[L1121] [40:12.40] and um and I had spent 2023 at Meta um
[L1122] [40:16.00] trying to do LM based developer tools
[L1123] [40:19.12] right with uh there's a you know we had
[L1124] [40:20.72] our own light version even met like
[L1125] [40:23.12] little version of uh GitHub copilot
[L1126] [40:25.28] right that one did like a paper and a
[L1127] [40:27.36] talk on that one was a code compose
[L1128] [40:29.44] right that was code compose yeah
[L1129] [40:31.20] >> and um you know we uh like now uh
[L1130] [40:36.00] there's a lot of uh uh enthusiasm around
[L1131] [40:40.00] you know delivering quickly and pushing
[L1132] [40:42.00] the boundaries of that sort of stuff and
[L1133] [40:44.48] uh you know I mean truthfully I mean you
[L1134] [40:47.76] know we get feedback on some of these
[L1135] [40:49.04] things it's like why is this not you
[L1136] [40:50.40] know GBT4 and I was like well we're on
[L1137] [40:52.40] like llama 2 it's not the same thing and
[L1138] [40:55.76] uh you know I was not not a researcher
[L1139] [40:58.96] right I was like but I and I you know
[L1140] [41:01.12] just wanted to to build the experiences
[L1141] [41:03.52] right and that sort of thing And um and
[L1142] [41:08.40] so so that was that was one thing was
[L1143] [41:10.16] that like I wanted to build stuff and I
[L1144] [41:11.84] wanted to go to the place where I could
[L1145] [41:13.12] actually build with the best model. Um
[L1146] [41:15.68] you know two again was um similar to
[L1147] [41:18.00] like you know Google originally like
[L1148] [41:20.16] seeing the people who were coming here
[L1149] [41:22.00] to open AAI and I was like well those
[L1150] [41:23.76] are people I really respect. I was like
[L1151] [41:25.28] those are I could actually work with
[L1152] [41:26.64] more senior people you know like meta
[L1153] [41:30.08] eights and nines at open I felt like
[L1154] [41:32.40] that I could where I was um and um you
[L1155] [41:37.60] know third was just like this also seems
[L1156] [41:40.08] like uh and it has been just a very
[L1157] [41:42.96] special place at at the point in time.
[L1158] [41:45.68] So I told a lot of people I was like,
[L1159] [41:47.04] you know, I felt like this would be like
[L1160] [41:49.20] the most similar to starting at Google
[L1161] [41:52.24] in 2000. So not not to 1998, but like
[L1162] [41:54.96] let's say 2000, right? Like they kind of
[L1163] [41:56.72] got some footing and got some, you know,
[L1164] [41:58.56] product market fit. And so like just as
[L1165] [42:00.40] a personal level, that was just a very
[L1166] [42:02.24] exciting thing.
[L1167] [42:03.60] >> Um and um you know, the last one was
[L1168] [42:06.72] that u funny thing is that when I I
[L1169] [42:10.64] really enjoyed calendar because I it was
[L1170] [42:12.64] consumer and I shipped to a lot of
[L1171] [42:14.00] people. I went to Facebook because I
[L1172] [42:15.60] thought huge consumer place. Ended up
[L1173] [42:19.12] not doing consumer at all, right? Ended
[L1174] [42:20.80] up doing developer tools, but like you
[L1175] [42:23.04] know my users were my friends at work.
[L1176] [42:24.64] It was just like 20,000 people, not like
[L1177] [42:26.24] a billion people, but it was good enough
[L1178] [42:27.60] for me at the time. And then, you know,
[L1179] [42:30.08] thinking about OpenAI and then the
[L1180] [42:32.00] chance to actually, you know, come back
[L1181] [42:33.76] to to consumer um or at least like have
[L1182] [42:37.20] a large user base, right? And so now
[L1183] [42:39.52] working on codecs um you know I wonder
[L1184] [42:42.24] if like over a million weeklyies or I
[L1185] [42:44.16] forget how much it is right now um and
[L1186] [42:46.16] and just keeps growing like like you
[L1187] [42:49.20] know hockey stick or more like vertical
[L1188] [42:50.64] line than hockey stick even um that uh
[L1189] [42:54.64] you know so it's like way more than the
[L1190] [42:56.88] 20 to 40,000 developers you know you
[L1191] [42:59.28] could affect at meta.
[L1192] [43:00.80] >> Yeah absolutely and dev tooling for the
[L1193] [43:03.44] industry almost.
[L1194] [43:04.64] >> Yeah. Um, Meta when I think of the
[L1195] [43:06.80] company it's kind of engineering driven
[L1196] [43:10.80] like engineers are king and queen I
[L1197] [43:13.60] guess and they kind of like drive
[L1198] [43:15.20] everything. It's very bottoms up from
[L1199] [43:16.64] that sense. And I feel like a lot of the
[L1200] [43:19.28] lab companies are also like that but on
[L1201] [43:22.48] the research side. So rather than
[L1202] [43:24.32] engineer is the first class citizen it's
[L1203] [43:27.20] like let's make sure the research goes
[L1204] [43:29.04] well and for good reason right like
[L1205] [43:30.32] that's also part of why you came is the
[L1206] [43:31.92] models are good. But as an engineer, you
[L1207] [43:34.96] mentioned you weren't doing research.
[L1208] [43:36.96] Um, what are your thoughts on that
[L1209] [43:38.40] researchled culture versus engineering
[L1210] [43:40.48] le culture?
[L1211] [43:41.36] >> I mean, it was certainly an adjustment,
[L1212] [43:42.80] right? I mean, I think if anyone who
[L1213] [43:44.32] comes here and says otherwise is a liar,
[L1214] [43:46.40] but [laughter]
[L1215] [43:47.52] um, you know, if you've been at like the
[L1216] [43:48.72] fangs or whatever. Um, and uh, but you
[L1217] [43:52.64] know, they are, you know, when you talk
[L1218] [43:55.04] about impact, right, which I think is
[L1219] [43:56.56] important, like a real like you
[L1220] [43:57.68] genuinely, you know, mean it. um like I
[L1221] [44:02.32] you know I love the work that I do on
[L1222] [44:03.44] Codex on the harness and I think we do a
[L1223] [44:05.04] lot of very meaningful things um but you
[L1224] [44:08.80] know if the model weren't very good it
[L1225] [44:10.56] wouldn't really matter what we did you
[L1226] [44:12.08] know on the harness right and so um so I
[L1227] [44:14.88] don't uh
[L1228] [44:17.44] so you know that that's how it is I
[L1229] [44:20.40] would say um but I you know I feel
[L1230] [44:23.52] really great like you know we we sit
[L1231] [44:25.04] right next to the the research team uh
[L1232] [44:27.12] work really closely with And um and so
[L1233] [44:30.16] that relationship that we have that we
[L1234] [44:32.08] get to co-develop the thing. I mean that
[L1235] [44:34.40] that was another reason you know leaving
[L1236] [44:36.16] leaving Meta I mean was that for for for
[L1237] [44:39.12] in the LM space was like you know I want
[L1238] [44:41.92] to build the product with the people who
[L1239] [44:44.16] are building the model so we can do this
[L1240] [44:45.68] thing together. I mean may you know
[L1241] [44:46.88] maybe you could do that there sort of
[L1242] [44:48.48] but not anyway the the the impact was
[L1243] [44:51.92] not you know quite quite the same. So
[L1244] [44:54.16] you mentioned I mean when you got here
[L1245] [44:55.44] it sounds like you were working on
[L1246] [44:56.40] codecs and starting uh that project up.
[L1247] [44:59.28] So I understand with the initial launch
[L1248] [45:01.36] of Codex CLI it was uh not exactly what
[L1249] [45:04.72] you hoped for like in terms of the how
[L1250] [45:07.28] it was received but um later it kind of
[L1251] [45:10.72] really all came together. Can you tell
[L1252] [45:12.96] that story?
[L1253] [45:13.84] >> Yeah sure. I mean it's been a wild ride.
[L1254] [45:16.56] So Codeex CLI we launched it in April
[L1255] [45:20.40] 2025. It was kind of like this like one
[L1256] [45:23.20] more thing moment at the end of the 03
[L1257] [45:25.20] uh 04 mini uh live stream and uh so we
[L1258] [45:28.80] demoed it live. We open sourced it, you
[L1259] [45:30.80] know, called 3o at that point. Uh a lot
[L1260] [45:33.20] of people tried it out, you know,
[L1261] [45:34.24] everyone was excited to try a new um
[L1262] [45:36.48] coding agent, you know, and it was and
[L1263] [45:38.56] it was pretty good, but it was it was
[L1264] [45:40.40] pretty rushed um to get it out the door,
[L1265] [45:42.80] right? There was um which in some ways
[L1266] [45:45.28] was good for engagement because now
[L1267] [45:46.48] we're open source. we were getting poll
[L1268] [45:47.76] requests, you know, coming in all over
[L1269] [45:49.60] the place and uh I forget, you know, I
[L1270] [45:52.72] feel like we're like 10 to 20,000 stars
[L1271] [45:54.64] in like a week or two or something like
[L1272] [45:56.00] that. So, like that that part was fun
[L1273] [45:58.32] and um you know, there were people who
[L1274] [46:00.08] did like it, you know, like nobody liked
[L1275] [46:01.84] it or anything like that, but then um
[L1276] [46:05.28] but that I I think we didn't we weren't
[L1277] [46:08.48] maybe quite staffed to like really drive
[L1278] [46:10.72] that the way that we needed to. Um
[L1279] [46:12.96] because you know we're we're trying to
[L1280] [46:14.80] cover multiple things as a company and
[L1281] [46:16.88] so you know just a month after that and
[L1282] [46:19.60] you know team of like seven engineers
[L1283] [46:21.28] and I forget how many researchers
[L1284] [46:23.20] launched um codeex web or cloud web um
[L1285] [46:27.28] where you know you use codeex in a
[L1286] [46:28.96] container or you could just you know
[L1287] [46:31.04] kick off a new thing from your phone
[L1288] [46:32.40] which is super cool and um and there
[L1289] [46:35.84] that was like a more wellstaffed effort
[L1290] [46:38.00] and I and I think you know that one is
[L1291] [46:40.08] still the I think the the long-term
[L1292] [46:42.80] vision is is correct. But I think with a
[L1293] [46:44.80] lot of this stuff that we've seen, you
[L1294] [46:46.72] know, you have to bring the the users
[L1295] [46:48.00] with you and and uh and and I think that
[L1296] [46:50.24] one's just like a little bit ahead of
[L1297] [46:51.52] its of its time and people were still
[L1298] [46:53.52] actually more into the the local um
[L1299] [46:56.32] coding agents. And so we kind of, you
[L1300] [46:58.56] know, we saw, you know, the like the web
[L1301] [47:01.60] product like there's a big adoption
[L1302] [47:03.44] initially. It wasn't, you know, as
[L1303] [47:06.08] sticky, I would say, as we we had hoped.
[L1304] [47:08.48] Um and then through the summer, you
[L1305] [47:10.32] know, both products still kept kept uh
[L1306] [47:13.60] you know, we're working on both. Um but
[L1307] [47:16.16] then somewhere that midsummer, again,
[L1308] [47:17.68] like I said, it's like, you know, this
[L1309] [47:19.04] moment like local agents are still the I
[L1310] [47:22.08] guess the stronger product market fit,
[L1311] [47:23.68] but again, I still think in the limit
[L1312] [47:25.60] personally, right? Like uh you you're
[L1313] [47:28.48] going to need more machines than just
[L1314] [47:29.84] your laptop to as a place for agents to
[L1315] [47:31.84] run. And um so we we shifted quite a bit
[L1316] [47:35.84] um over the summer. So we we brought
[L1317] [47:37.60] more people onto the codeci.
[L1318] [47:40.48] Yeah. A few kid things bring more people
[L1319] [47:42.32] on. You know, GBT5 was uh going to come
[L1320] [47:45.76] out and that was looking really really
[L1321] [47:47.44] good. And um a thing I was personally
[L1322] [47:51.44] excited about because I had prototyped
[L1323] [47:52.96] it a couple times before um was that in
[L1324] [47:56.32] addition to the CLI then we also had
[L1325] [47:58.08] enough staffing we also started working
[L1326] [47:59.76] on um the VS code extension and you know
[L1327] [48:03.36] and I felt actually very strongly that
[L1328] [48:05.36] you know the the the terminal is good
[L1329] [48:07.60] for a lot of things but it has a lot of
[L1330] [48:09.28] limitations uh always just it's just
[L1331] [48:11.28] like you make a lot of compromises to
[L1332] [48:12.88] make you know a nice UI in the terminal
[L1333] [48:15.04] whereas VS code we didn't have to make
[L1334] [48:17.20] quite as many compromise devices and um
[L1335] [48:20.72] so I think like August I think was a
[L1336] [48:22.24] crazy month. I think GPT5 came out. I
[L1337] [48:24.16] think we we released our new refresh
[L1338] [48:26.64] terminal UI. Also the GPT open source
[L1339] [48:28.96] model came out. We supported that um in
[L1340] [48:31.44] the in the TUI as well. So that was
[L1341] [48:33.36] really cool that you had, you know, an
[L1342] [48:34.56] open weights model and the and an open
[L1343] [48:36.56] harness and um and then later that month
[L1344] [48:39.28] the VS Code extension, you know, came
[L1345] [48:41.28] out. And so we were just like, you know,
[L1346] [48:43.60] shipping like like crazy. And um and
[L1347] [48:46.72] that's really where like that confluence
[L1348] [48:49.04] of things, I would say, um is where we
[L1349] [48:52.64] started to see the inflection point
[L1350] [48:54.08] that's brought us to like, you know, the
[L1351] [48:55.60] vertical growth that we're that we're at
[L1352] [48:57.76] today. Um and so that's, you know, uh
[L1353] [49:01.04] that's been really exciting. I mean, you
[L1354] [49:03.20] know, some of these things you can you
[L1355] [49:04.24] can go to the repo, check for yourself,
[L1356] [49:05.92] right? And and and you know, gut check
[L1357] [49:07.68] on on some of these things. Um, terms of
[L1358] [49:09.84] number of people, uh, number of commits
[L1359] [49:11.44] and all this sort of thing. Um, and
[L1360] [49:14.32] yeah, so it's it's it's been quite a
[L1361] [49:16.56] ride.
[L1362] [49:17.76] >> You mentioned the local versus the
[L1363] [49:19.36] remote version of these coding agents,
[L1364] [49:21.04] and sounds like you have a lot of
[L1365] [49:22.96] conviction that the right long-term
[L1366] [49:24.80] direction is not the local versions,
[L1367] [49:27.52] it's remote and in the cloud. Why is
[L1368] [49:30.40] that? Well, I think about I think that
[L1369] [49:32.80] the people who actually for whom it is
[L1370] [49:34.48] sticky now and I think there'll be more
[L1371] [49:35.84] of it is that you imagine if you imagine
[L1372] [49:38.00] you want to just automatically
[L1373] [49:40.72] um you know set for the agent every like
[L1374] [49:43.68] GitHub issue or linear tile thing that
[L1375] [49:45.68] comes in or anything like that. I mean
[L1376] [49:47.04] obviously you know there's there's costs
[L1377] [49:49.04] with those things but or or you can it
[L1378] [49:51.04] could be abused but like you know let's
[L1379] [49:52.16] say for an internal private repo right
[L1380] [49:54.48] that you yeah want to be able to just
[L1381] [49:57.92] have it be a piece in in any sort of
[L1382] [49:59.92] automation pipeline right and so you
[L1383] [50:02.72] can't [laughter] you have all that
[L1384] [50:04.56] happening on your on your laptop and so
[L1385] [50:06.96] I guess I mean you know as a as an
[L1386] [50:08.96] individual I see maybe we'll still
[L1387] [50:10.88] personally spend more time with the
[L1388] [50:13.36] local agent but in terms of uh you know,
[L1389] [50:17.28] compute time of agents doing work,
[L1390] [50:19.36] right? I think getting that set up in
[L1391] [50:21.04] the cloud, I think, you know, a little
[L1392] [50:22.88] bit it's like a little more to get set
[L1393] [50:24.16] up right now, but once you have it, it's
[L1394] [50:25.92] it's quite nice. I see. Okay. So, you're
[L1395] [50:28.40] not saying that product, the local one
[L1396] [50:31.04] will change. You're saying that like
[L1397] [50:33.84] across the industry, the compute that
[L1398] [50:36.16] goes towards agents, majority will be in
[L1399] [50:38.24] the cloud.
[L1400] [50:39.44] Yeah, I mean even in um I think when the
[L1401] [50:42.24] VS Code extension first came out, you
[L1402] [50:44.16] know, one of the things was um the
[L1403] [50:46.32] ability to take the conversation that
[L1404] [50:47.68] you were having and like hit a button,
[L1405] [50:49.12] have it like transfer to the cloud if
[L1406] [50:50.72] you were set up to do it,
[L1407] [50:52.00] >> right? And um so I think that we'll
[L1408] [50:54.32] continue to see that where you maybe
[L1409] [50:55.76] you're working on something, you want to
[L1410] [50:56.88] throw it over here, you're like, bring
[L1411] [50:58.48] it back, you know, when it's done. Your
[L1412] [51:00.72] codeex usage is uh 5xed since the
[L1413] [51:04.16] beginning of the year and over a million
[L1414] [51:06.00] people are using it now. I'm curious,
[L1415] [51:08.32] has your AI workflow changed a lot since
[L1416] [51:10.72] you've uh you started to use this newer
[L1417] [51:13.44] version of Codeex?
[L1418] [51:14.48] >> Yeah, it has. It has. Um I'm a much
[L1419] [51:17.04] bigger user of the app now maybe than I
[L1420] [51:19.92] thought I would be. Um I uh yeah, like
[L1421] [51:25.76] for a while I was I was uh very strongly
[L1422] [51:28.64] in like our VS Code extension. Like I
[L1423] [51:30.40] need I want that sidebar. I want all the
[L1424] [51:32.16] code there next to me. I feel like these
[L1425] [51:33.92] things should be, you know, together.
[L1426] [51:35.76] Um, I'm not a I'm not a person who
[L1427] [51:38.24] doesn't look at the code. I'm not a like
[L1428] [51:39.60] a I I don't for for projects that are
[L1429] [51:42.72] like true prototypes that are throwaway
[L1430] [51:44.56] like I will actually not look at the
[L1431] [51:45.68] code. It's very freeing. I understand
[L1432] [51:47.04] why people so excited about it. But for
[L1433] [51:49.04] the code that goes into codeex itself,
[L1434] [51:50.80] I'm like no, I still need to look at
[L1435] [51:52.24] this, right? This is pretty important.
[L1436] [51:53.68] This is like what's going to, you know,
[L1437] [51:54.96] affect everybody else. Um, but you know,
[L1438] [51:58.16] you start to get a sense of, okay, I
[L1439] [52:01.20] like I'm confident the model's gonna be
[L1440] [52:02.96] able to do this, you know, this this
[L1441] [52:04.64] change and this sort of thing. Like I,
[L1442] [52:06.16] you know, I don't need to to babysit it.
[L1443] [52:07.76] I'm going to just like write a lot up
[L1444] [52:09.12] front. And so, you know, I have like
[L1445] [52:11.36] four or five clones of the Codeex repo
[L1446] [52:13.84] on my machine. And I I have enjoyed in
[L1447] [52:16.88] the Codeex app um like the multitasking
[L1448] [52:20.40] I just is is just a lot easier because
[L1449] [52:22.24] now you're just kind of hang out in one
[L1450] [52:23.44] window. Um, and you know, I try and it's
[L1451] [52:28.64] a game exactly, but it's like, you know,
[L1452] [52:30.16] it's like how much throughput can I get,
[L1453] [52:32.00] right? In terms of how many balls can I
[L1454] [52:34.24] juggle in the air? Sometimes it feels
[L1455] [52:35.68] like um it, you know, can it can feel
[L1456] [52:38.08] like a little hectic when you're really
[L1457] [52:39.76] trying to
[L1458] [52:40.80] >> context. context switch
[L1459] [52:42.40] >> but at the same time you're you're like
[L1460] [52:45.04] I I'm getting a lot more done you know
[L1461] [52:48.24] and uh and that you know almost feel a
[L1462] [52:52.00] little bad writing code by hand
[L1463] [52:53.52] sometimes because you're like I I could
[L1464] [52:55.28] have if I had asked this in the right
[L1465] [52:57.36] way I I you know it's like it's like
[L1466] [52:59.68] when you started it was like oh I'm just
[L1467] [53:00.80] going to change these three lines and
[L1468] [53:01.84] then like you know 30 minutes later
[L1469] [53:03.12] you're like oh I kind of [laughter] you
[L1470] [53:05.04] know you know we all we all like to type
[L1471] [53:07.04] still I think and that sort of thing.
[L1472] [53:08.64] What percent of your code would you say
[L1473] [53:10.56] is human written versus the model
[L1474] [53:13.12] generates it these days?
[L1475] [53:14.48] >> Oh man, it's models be like 80 to 90%. I
[L1476] [53:19.12] mean yeah. Yeah. I mean like I
[L1477] [53:21.28] especially like debugging a test or like
[L1478] [53:24.64] the CI thing is bad. Like I'm like I'm
[L1479] [53:26.88] like hey you know you know how to write
[L1480] [53:28.24] you know print debug whatever like and
[L1481] [53:30.56] that's great. That's really freeing
[L1482] [53:32.56] >> digging into the problems that are
[L1483] [53:35.12] suitable for LLMs and the ones that are
[L1484] [53:37.04] not. like what what do you need to see
[L1485] [53:39.76] where you think okay I need to go in and
[L1486] [53:41.84] you know write it myself what's that 10%
[L1487] [53:44.00] and also what's in that 80 90%
[L1488] [53:47.60] >> yeah I mean that's a good one I think
[L1489] [53:49.68] about that you know because every time I
[L1490] [53:51.12] sit down I'm like like should I write
[L1491] [53:53.52] this I mean the answer is almost always
[L1492] [53:54.80] no um
[L1493] [53:56.88] uh there's
[L1494] [53:59.36] things that are like lower level and
[L1495] [54:01.20] someone you know so codeex the the
[L1496] [54:02.88] harness the part that I you know spend
[L1497] [54:04.56] my time on is in Rust and that means
[L1498] [54:07.44] means that you know we can do and we do
[L1499] [54:09.92] do like operating system specific things
[L1500] [54:12.16] in that codebase. Um and actually and I
[L1501] [54:16.40] spend a lot of time on on the sandboxing
[L1502] [54:18.48] right so the thing that really upholds
[L1503] [54:20.16] like uh you know the security integrity
[L1504] [54:22.08] of what of what we're doing and that the
[L1505] [54:23.68] model can't go outside um you know the
[L1506] [54:26.08] bounds that you set um you know I I do
[L1507] [54:29.60] more of that um by hand because I need
[L1508] [54:32.32] to make sure really sure that that's all
[L1509] [54:35.04] correct right that our test coverage is
[L1510] [54:37.20] is good um or sometimes I'll you know
[L1511] [54:40.08] seed it and then you know once I've got
[L1512] [54:42.48] like the groundwork I'm like Okay, I
[L1513] [54:44.00] have the pieces that I that I was had a
[L1514] [54:46.96] lot of feelings about and then could let
[L1515] [54:48.48] it like fill in the rest and that sort
[L1516] [54:49.84] of thing. But, you know, a lot of like
[L1517] [54:51.92] refactors and things like that.
[L1518] [54:53.52] Actually, think like a lot right now is
[L1519] [54:55.20] like, you know, I'll have to build up a
[L1520] [54:57.44] big, you know, PR that does too many
[L1521] [54:59.44] things, but I know it does too many
[L1522] [55:01.20] things. I'll be like, "Okay, please, you
[L1523] [55:02.88] know, please split this up into
[L1524] [55:04.32] reviewable sized commits." Um, things
[L1525] [55:06.88] like that. Like I think about how much
[L1526] [55:09.68] time I probably spent on that sort of
[L1527] [55:11.20] stuff before and now I can right frees
[L1528] [55:14.00] you up. Um what about um like code
[L1529] [55:17.20] review? Is there like what percent of
[L1530] [55:20.40] lines of code do you and at OpenAI
[L1531] [55:23.84] generally are people reviewing manually
[L1532] [55:25.47] [snorts] or are there agents that are
[L1533] [55:28.08] like yeah imagine you write a test or
[L1534] [55:29.84] something. I don't really need to review
[L1535] [55:31.12] that. I mean it
[L1536] [55:32.88] >> I would say I liked the approach where
[L1537] [55:35.52] you know the the agent should do
[L1538] [55:38.96] you know multiple rounds of review or
[L1539] [55:40.16] whatever until it's confident and that
[L1540] [55:41.84] that it's like kind of you know worth a
[L1541] [55:43.12] human's time of looking at it. Um but we
[L1542] [55:46.00] still do look at it um like ultimately
[L1543] [55:48.64] before it goes in. I would say generally
[L1544] [55:50.24] speaking um I think there's you know we
[L1545] [55:53.60] have like our agents MD file like
[L1546] [55:55.28] everybody else does. there still
[L1547] [55:57.04] sometimes you find like a gap in
[L1548] [55:58.64] knowledge that needs like that some
[L1549] [56:00.08] context that needs to get added back
[L1550] [56:01.84] into there or it's um yeah just just
[L1551] [56:05.84] things that we haven't yeah memorialized
[L1552] [56:08.16] that that the agent this but like as a
[L1553] [56:09.92] human I I still happen to know right
[L1554] [56:12.40] >> um and things like that so we do catch
[L1555] [56:14.32] things um but you know I'll say actually
[L1556] [56:17.68] now that people are uh also using AI to
[L1557] [56:20.32] write their like pull request summaries
[L1558] [56:22.48] our summaries across the team I would
[L1559] [56:23.76] say are getting way better so now
[L1560] [56:25.08] [laughter] these It's also when I'm
[L1561] [56:26.40] going into review, right, it's been
[L1562] [56:28.48] reviewed by codeex, there's a summary
[L1563] [56:30.88] that's like that we actually make sure
[L1564] [56:32.48] it has like the why and the what of why,
[L1565] [56:34.72] you know, the reason behind the PR. So
[L1566] [56:37.04] that is certainly I think helping like
[L1567] [56:40.64] get through these PRs faster, which is
[L1568] [56:42.48] good because there was a lot more review
[L1569] [56:44.40] to do.
[L1570] [56:45.28] >> That's I mean that's amazing. I feel
[L1571] [56:46.80] like and 50% of diffs have like you know
[L1572] [56:51.36] almost blank the test plan says you know
[L1573] [56:55.28] >> uh I don't know arc build or whatever
[L1574] [56:56.88] the oh I know but [laughter]
[L1575] [57:00.40] >> um I want to talk about the the the
[L1576] [57:03.12] codec cli that's that's open source why
[L1577] [57:06.48] is it open source
[L1578] [57:08.96] you know for something that's that
[L1579] [57:11.60] critical to like what's going on on your
[L1580] [57:14.00] machine right like that that like that's
[L1581] [57:16.64] one of the aspects of open source is
[L1582] [57:18.08] that I'm not you know the most um
[L1583] [57:21.28] zealous about this sort of thing but I
[L1584] [57:22.88] but I I sympathize with it this idea
[L1585] [57:24.48] that like hey you're going to put this
[L1586] [57:26.72] thing on my machine I care about what
[L1587] [57:29.52] it's doing right and I think in this
[L1588] [57:30.88] domain in particular it's really
[L1589] [57:32.56] important that people can look at it you
[L1590] [57:35.28] know and have have an idea of what it's
[L1591] [57:37.36] doing um because you know people have a
[L1592] [57:39.44] lot of questions about AI agents and
[L1593] [57:41.92] that sort of thing um and so I think I
[L1594] [57:45.92] think this this this
[L1595] [57:48.16] area this domain I think it's actually
[L1596] [57:49.76] really important um and also we um you
[L1597] [57:53.52] know we have gotten a lot of uh I think
[L1598] [57:56.00] like great compriations and bug reports
[L1599] [57:58.16] and things like that that we um would
[L1600] [58:00.72] have missed out on um and and and then
[L1601] [58:03.44] also I think it's you know um just you
[L1602] [58:06.32] know sharing with the world with like
[L1603] [58:07.92] how this is done um so we do it through
[L1604] [58:09.76] code right I've I've put out um one blog
[L1605] [58:12.48] post about how the agent loop works like
[L1606] [58:14.40] there is plan to do more of that. I'm
[L1607] [58:15.92] actually excited to. It's just, you
[L1608] [58:17.12] know, just it's just time is this liming
[L1609] [58:19.68] factor.
[L1610] [58:21.20] >> Really, not
[L1611] [58:22.16] >> Yeah. It was funny because I had I had I
[L1612] [58:25.20] had two candidates who came through and
[L1613] [58:26.64] one's like he's like, "Hey, I wrote it,
[L1614] [58:28.00] right?" I was like, "No, no, I I
[L1615] [58:29.53] [snorts] wrote it." And another person
[L1616] [58:30.80] came in. He's like, "Oh, you can tell
[L1617] [58:32.00] that that you know that you did not
[L1618] [58:34.08] outsource the
[L1619] [58:35.36] >> Okay, good. Right. I was like, oh, thank
[L1620] [58:36.64] you." You know? Um, so yeah,
[L1621] [58:38.56] >> you mentioned the blog post. How does
[L1622] [58:40.48] Codeex find what is available to it in
[L1623] [58:43.20] its environment? And when I'm running
[L1624] [58:45.12] these things, I'll see it's kind of
[L1625] [58:47.60] amazing. It's thinking to itself and
[L1626] [58:49.52] like discovering all these things in in
[L1627] [58:51.76] my uh terminal. So yeah, how does that
[L1628] [58:54.64] typically work?
[L1629] [58:55.52] >> Yeah, I mean there's, you know, there's
[L1630] [58:56.72] a few. I mean there's obviously what is
[L1631] [58:58.88] you know when Codex is based training
[L1632] [59:00.40] like it loves to use rip grip. It uses
[L1633] [59:01.84] rip grip very well to find all sorts of
[L1634] [59:04.00] things. Um, and then there's, you know,
[L1635] [59:06.40] if you have your agents MD file and
[L1636] [59:07.92] you're say, hey, in this repo, like
[L1637] [59:09.52] these tools are really important, right?
[L1638] [59:11.60] You should use these, right? Or the
[L1639] [59:13.04] readmemes or whatever. Um, or uh
[L1640] [59:16.80] obviously if you use MCP and you
[L1641] [59:19.52] associate these MCP servers with your
[L1642] [59:22.08] um, you know, where you're working on,
[L1643] [59:23.52] right, that that that um injects the set
[L1644] [59:26.64] of tool definitions like at the start of
[L1645] [59:29.04] the the conversation, right? So then uh
[L1646] [59:32.16] that kind of Yeah. So that's that's not
[L1647] [59:34.16] even like discovery on Codex's part,
[L1648] [59:36.08] right? It's kind of just like put front
[L1649] [59:37.68] and center there. I see. So some of it's
[L1650] [59:39.60] the harness explicitly throwing that
[L1651] [59:42.72] into the context
[L1652] [59:44.16] >> and then there is a big chunk though
[L1653] [59:46.00] where the model is just doing all the
[L1654] [59:47.84] heavy lifting of finding things. Is that
[L1655] [59:49.84] right?
[L1656] [59:50.16] >> Yeah.
[L1657] [59:50.64] >> Kind of like reflecting over your
[L1658] [59:52.16] career. The breadth and depth of your
[L1659] [59:55.20] work if we look across all of it. I mean
[L1660] [59:57.44] it's it's insane. you were your
[L1661] [59:59.44] javascript front end then you have all
[L1662] [01:00:01.76] these dev tool you know build fuzzy file
[L1663] [01:00:04.48] search you know virtual now you're
[L1664] [01:00:06.64] working on codecs you I'm sure you had
[L1665] [01:00:09.68] to uh continue your engineering educa
[L1666] [01:00:12.16] education to kind of get through all
[L1667] [01:00:14.08] these projects what are the top
[L1668] [01:00:16.64] technical books that have helped you
[L1669] [01:00:18.96] educate yourself
[L1670] [01:00:20.24] >> yeah I mean um you know so one was this
[L1671] [01:00:23.92] uh this book on operating systems um
[L1672] [01:00:26.88] it's like a thousand pages or something
[L1673] [01:00:28.96] like this. Uh it's the Addison Wesley
[L1674] [01:00:31.68] book. I'm trying the author, but it was
[L1675] [01:00:33.28] funny because I was when I was working
[L1676] [01:00:35.44] on the virtual file system. So I had
[L1677] [01:00:37.44] actually gotten to that point in my
[L1678] [01:00:39.04] career without ever writing C like
[L1679] [01:00:41.44] undergrad like it was like more
[L1680] [01:00:42.80] theoretical like we just never had to
[L1681] [01:00:44.88] touch it. And then yet I'm like working
[L1682] [01:00:46.64] on a virtual file system project and
[L1683] [01:00:48.56] then like very low operating system.
[L1684] [01:00:50.64] That's why I was, you know, joke that I
[L1685] [01:00:51.92] was kind of the worst engineer of the
[L1686] [01:00:53.12] project. And, you know, and someone said
[L1687] [01:00:55.76] something and I realized I was like, I
[L1688] [01:00:57.76] don't know what they're talking about.
[L1689] [01:00:59.20] This is kind of embarrassing. And I was
[L1690] [01:01:01.20] just like, you know, what book do I have
[L1691] [01:01:02.96] to read? And I think my manager, Aaron
[L1692] [01:01:04.80] Kushner at the time was like, he's like,
[L1693] [01:01:06.00] well, there's this thousandpage book.
[L1694] [01:01:07.20] And I was like, done. So, I bought it,
[L1695] [01:01:10.48] read the thing cover to cover. I like
[L1696] [01:01:12.08] took it to Hawaii with me. I took it
[L1697] [01:01:13.44] everywhere until I finished it. It's
[L1698] [01:01:15.12] it's kind of amazing and sad or weird
[L1699] [01:01:17.44] that like how um how far many of us can
[L1700] [01:01:21.20] get like in software engineering without
[L1701] [01:01:22.96] really having a clue how computers work.
[L1702] [01:01:24.88] Like there's just so many of those
[L1703] [01:01:26.72] levels of abstraction. Um but you know
[L1704] [01:01:29.92] one hand it's very freeing and then on
[L1705] [01:01:31.60] the other hand it's a little bananas.
[L1706] [01:01:33.52] And I think that um what I would say to
[L1707] [01:01:35.52] people right now is um is you know
[L1708] [01:01:41.04] actively trying to go like deeper
[L1709] [01:01:42.72] through the layers and understand these
[L1710] [01:01:44.48] things. Um and uh like cuz many times I
[L1711] [01:01:50.64] saw other people do it and now I can do
[L1712] [01:01:52.40] it is that there are problems some other
[L1713] [01:01:54.24] people could solve that I couldn't solve
[L1714] [01:01:55.92] because I just didn't know that like
[L1715] [01:01:58.08] there was this croft between these two
[L1716] [01:01:59.68] layers and if you got rid of it, right,
[L1717] [01:02:00.96] you get like a 10x improvement or
[L1718] [01:02:02.40] something like that, right? If you if
[L1719] [01:02:04.00] you're just operating so high up, you
[L1720] [01:02:05.44] don't really know, you know, what you
[L1721] [01:02:06.72] can what you can break down. um you know
[L1722] [01:02:09.68] so that um and so in terms of books like
[L1723] [01:02:12.32] uh I've enjoyed the like the O'Reilly uh
[L1724] [01:02:14.24] the Rust books um I you know big fan of
[L1725] [01:02:16.80] Rust um I think but they're also like
[L1726] [01:02:18.96] well written um and and thorough and
[L1727] [01:02:22.08] then honestly another thing I've been
[L1728] [01:02:24.08] telling people um that's not in the book
[L1729] [01:02:26.72] category but probably more fun and I
[L1730] [01:02:29.12] learned a lot uh actually um are um
[L1731] [01:02:32.72] these CTFs are like capture the flag
[L1732] [01:02:35.28] like security type competitions And
[L1733] [01:02:38.40] just, you know, it helps with like kind
[L1734] [01:02:40.00] of like adversarial mindset. it helps
[L1735] [01:02:42.32] with I think uh they're usually just
[L1736] [01:02:44.80] like it's like a it's like a dicath like
[L1737] [01:02:47.28] a computer dicathlon I feel like right
[L1738] [01:02:48.96] because like like there'll be multiple
[L1739] [01:02:50.64] challenges and maybe this one you need
[L1740] [01:02:52.56] to like understand assembly and this one
[L1741] [01:02:54.24] you need to understand like what
[L1742] [01:02:56.08] someone's like janky PHP admin pages do
[L1743] [01:02:59.92] all this sort of thing and it and it
[L1744] [01:03:01.68] just forces this um breadth on you uh in
[L1745] [01:03:06.08] a way that's kind of hard to to generate
[L1746] [01:03:08.72] otherwise and it's also you know just
[L1747] [01:03:10.56] more fun because it's like a game and
[L1748] [01:03:12.00] that sort of thing.
[L1749] [01:03:12.72] >> Can you give some context on what CTF
[L1750] [01:03:14.88] is? Yeah. So, it's it's it can be a
[L1751] [01:03:17.44] number of things, but uh it's it's
[L1752] [01:03:18.88] usually a competition usually in like
[L1753] [01:03:20.56] the infosc the security domain and
[L1754] [01:03:23.60] there'll be a set of uh there's like the
[L1755] [01:03:26.24] Jeopardy style one which is like there's
[L1756] [01:03:27.68] a bunch of challenges um and like you
[L1757] [01:03:30.96] know designed like crafted ahead of time
[L1758] [01:03:33.44] and they all have point values
[L1759] [01:03:34.80] associated with them and so you know
[L1760] [01:03:37.12] there's usually some fixed amount of
[L1761] [01:03:38.40] time and it could be individual it could
[L1762] [01:03:39.76] be with a team and you're trying to
[L1763] [01:03:41.84] solve these things and and there's a
[L1764] [01:03:44.16] flag there's always like a secret, you
[L1765] [01:03:46.32] know, um, piece of text um, in there
[L1766] [01:03:49.68] that usually has some format. And the
[L1767] [01:03:52.40] way is that you basically if you can
[L1768] [01:03:54.16] discover the secret piece of text, that
[L1769] [01:03:55.68] means that you have the the challenge is
[L1770] [01:03:58.24] set up that you would only have gotten
[L1771] [01:03:59.44] that if you had figured out, you know,
[L1772] [01:04:00.56] reverse engineered or whatever you were
[L1773] [01:04:02.08] supposed to do and then you get submit
[L1774] [01:04:03.44] that piece of text and that's your, you
[L1775] [01:04:05.28] know, token to demonstrate that you had
[L1776] [01:04:06.80] solved the challenge. And so it could be
[L1777] [01:04:08.08] like a race to like solve everything
[L1778] [01:04:10.24] first or get the most points in a
[L1779] [01:04:11.60] certain amount of time or different
[L1780] [01:04:12.80] things like that. So it's like it's kind
[L1781] [01:04:14.56] of like an escape room but in your
[L1782] [01:04:16.56] terminal you use only computers to
[L1783] [01:04:18.72] figure everything out.
[L1784] [01:04:19.76] >> Yes.
[L1785] [01:04:20.48] >> I see. Okay. And your recommendation is
[L1786] [01:04:22.88] people who want to become better
[L1787] [01:04:25.12] engineers they should invest in doing
[L1788] [01:04:28.08] some of these CTF because they make you
[L1789] [01:04:29.84] solve problems that make you a better
[L1790] [01:04:31.20] engineer.
[L1791] [01:04:31.92] >> Yeah. and you know and then you you know
[L1792] [01:04:33.60] also develop skills and things that you
[L1793] [01:04:35.52] just wouldn't have you know if you're
[L1794] [01:04:36.72] just like a you know writing react every
[L1795] [01:04:38.72] day like you're probably not going to
[L1796] [01:04:41.12] like open up GDB and like reverse a you
[L1797] [01:04:43.92] know a tic-tac-toe game but like I did
[L1798] [01:04:45.68] that because of you know a CTF challenge
[L1799] [01:04:47.68] was to do you know exactly that
[L1800] [01:04:49.76] >> right
[L1801] [01:04:50.48] >> um and but then it's like but then I
[L1802] [01:04:52.56] learned how to use GDB and like and and
[L1803] [01:04:55.04] then then you start you know when you're
[L1804] [01:04:57.04] faced with other problems you're like oh
[L1805] [01:04:58.40] my my just toolkit of of ways to solve
[L1806] [01:05:00.96] things is just much broader broader a
[L1807] [01:05:03.04] lot of people especially earlier in
[L1808] [01:05:04.80] their career they see the power of
[L1809] [01:05:07.52] codeex doing everything for them in the
[L1810] [01:05:10.40] terminal and I just imagine them saying
[L1811] [01:05:12.48] oh well I don't need to learn GDB
[L1812] [01:05:14.24] because uh Codex knows it so
[L1813] [01:05:17.44] >> um would what would your advice be given
[L1814] [01:05:19.92] the landscape of these AI tools for
[L1815] [01:05:22.08] people thinking about their engineering
[L1816] [01:05:23.68] education
[L1817] [01:05:24.56] >> yeah no that's I mean I think everyone's
[L1818] [01:05:26.40] like struggling to answer that uh
[L1819] [01:05:28.32] question right now um I do think about
[L1820] [01:05:31.12] it you a a lot and I I don't have a
[L1821] [01:05:33.44] great answer. I I I kind of personally
[L1822] [01:05:35.52] come back to my thing about like
[L1823] [01:05:38.40] um I still think like trying to
[L1824] [01:05:41.60] forcefully kind of go through the levels
[L1825] [01:05:43.20] of of abstraction and just understand um
[L1826] [01:05:46.96] you know more like at a deeper level how
[L1827] [01:05:48.96] things work um is going to be important.
[L1828] [01:05:51.44] I mean I think this will change. I'm
[L1829] [01:05:53.60] sure this will change over time, but
[L1830] [01:05:54.80] right now it's still kind of like,
[L1831] [01:05:57.68] you know, the questions that you asked
[L1832] [01:06:00.08] the agent is going to affect the quality
[L1833] [01:06:02.00] of the thing that you get out, right?
[L1834] [01:06:04.16] So, if you're not asking the right
[L1835] [01:06:05.60] questions, you're not maybe going to get
[L1836] [01:06:07.60] the best engineering solution out the
[L1837] [01:06:09.44] other side. You know, as things go on,
[L1838] [01:06:11.92] perhaps that will also be, you know,
[L1839] [01:06:14.48] another layer that's removed. I mean, I
[L1840] [01:06:16.00] think, you know, that's certainly where
[L1841] [01:06:16.88] we're going. I don't know what time
[L1842] [01:06:18.08] frame we'll get there. things do seem to
[L1843] [01:06:19.36] be happening faster than we expect. But
[L1844] [01:06:22.16] um
[L1845] [01:06:23.68] yeah, I think in general, but
[L1846] [01:06:27.20] learning how to ask what the right
[L1847] [01:06:28.56] question is and I and I haven't, you
[L1848] [01:06:30.64] know, for myself even like totally
[L1849] [01:06:32.16] pinned down what that means for for
[L1850] [01:06:33.84] someone who's like starting out new,
[L1851] [01:06:35.28] right? You fortunately have experience
[L1852] [01:06:37.36] to to fall back on or like that's where
[L1853] [01:06:39.52] that that that taste or that um
[L1854] [01:06:43.28] intuition of what to ask has has
[L1855] [01:06:45.20] developed. But, you know, if you're if
[L1856] [01:06:46.80] you're starting out, um, I'm still not
[L1857] [01:06:49.68] sure yet. And it's also hard to say
[L1858] [01:06:51.20] because we we don't really know 100%
[L1859] [01:06:53.20] where everything's going.
[L1860] [01:06:54.96] >> Yeah. When you reflect over your career,
[L1861] [01:06:58.24] the expectations at these really high
[L1862] [01:07:00.40] levels is kind of crazy. I mean, it's
[L1863] [01:07:02.72] like already for most people, this E7 or
[L1864] [01:07:05.92] senior staff level is this unattainable
[L1865] [01:07:08.80] level of impact. So someone who gets
[L1866] [01:07:10.40] promoted to that level is thinking, I
[L1867] [01:07:12.88] gotta really work super hard now because
[L1868] [01:07:15.84] the bar is like up here.
[L1869] [01:07:18.16] >> And then you went two levels past that.
[L1870] [01:07:20.64] And so I I'm curious like in the
[L1871] [01:07:23.60] day-to-day now, what what are your
[L1872] [01:07:25.76] thoughts on these like crazy
[L1873] [01:07:27.60] expectations? Is it stressful for you?
[L1874] [01:07:30.08] I mean it never it was never not
[L1875] [01:07:32.88] stressful I think um for me because I
[L1876] [01:07:36.64] really I think also because I sat in
[L1877] [01:07:39.20] calibrations right and I um you know so
[L1878] [01:07:42.48] for a bunch of other people you know you
[L1879] [01:07:44.08] talk about their level you talk about
[L1880] [01:07:45.44] their impact and you know you wanted to
[L1881] [01:07:47.04] be really fair and have this integrity
[L1882] [01:07:49.44] around well this level means this thing
[L1883] [01:07:50.96] and this is the impact like that's what
[L1884] [01:07:52.32] it means all is that's what exceeds this
[L1885] [01:07:53.76] and then knowing that like then you're
[L1886] [01:07:55.52] you know playing it out in your mind
[L1887] [01:07:56.56] like well someone's sitting in my
[L1888] [01:07:57.76] calibration and talking about this thing
[L1889] [01:07:59.68] and they want to be fair, right? And and
[L1890] [01:08:02.08] it is a little scary like you know you
[L1891] [01:08:03.76] get to E8 and you're like oh you know
[L1892] [01:08:05.28] it's a D1 a director
[L1893] [01:08:07.28] >> and you're like how do I have as much
[L1894] [01:08:08.80] impact as a person who has maybe like
[L1895] [01:08:11.20] over a hundred people
[L1896] [01:08:12.96] >> in their or so that's hard a lot of
[L1897] [01:08:15.36] people do it again a lot of people who
[L1898] [01:08:17.84] are I see who do it do it more by
[L1899] [01:08:21.36] >> uh a different form of people management
[L1900] [01:08:24.32] right where they're trying to you know
[L1901] [01:08:25.76] like write the right doc and get the
[L1902] [01:08:27.04] people aligned and do that sort of thing
[L1903] [01:08:28.40] and the and the reason that they do it
[L1904] [01:08:30.56] and are not a director is that
[L1905] [01:08:33.04] oftentimes the the people I've talked to
[L1906] [01:08:35.04] people who are in this like that they're
[L1907] [01:08:36.32] like well I have this technical
[L1908] [01:08:37.52] credibility or because I built this
[L1909] [01:08:39.44] thing like when I go to the team and
[L1910] [01:08:41.28] talk to them it lands differently than
[L1911] [01:08:42.88] if like a engineering director does or
[L1912] [01:08:45.44] some version of that right happens a lot
[L1913] [01:08:48.08] um and so then you know when you when
[L1914] [01:08:50.72] you say you're influencing you know 50
[L1915] [01:08:53.04] to 100 people as a senior IC then you're
[L1916] [01:08:55.28] like oh okay that's like you know D1
[L1917] [01:08:57.52] impact um you know whereas as as if
[L1918] [01:09:01.20] you're a coder. I see. Um, uh,
[L1919] [01:09:06.40] you know, being really thoughtful about
[L1920] [01:09:08.64] the projects that you pick and it can't
[L1921] [01:09:11.68] just be a like this is fun for me type
[L1922] [01:09:13.60] of project. I mean, you know, if you
[L1923] [01:09:16.16] actually care about, you know, not
[L1924] [01:09:17.92] getting fired or getting you're getting
[L1925] [01:09:19.20] like Sam or better. Um, and even when I
[L1926] [01:09:23.20] would start a project, certainly like
[L1927] [01:09:24.88] the later I went on, I would think a lot
[L1928] [01:09:26.64] about like, okay, like I maybe there's
[L1929] [01:09:29.36] this feature I just want to write it
[L1930] [01:09:30.48] because it's fun. And I'd be like, uh,
[L1931] [01:09:31.84] no, I should let somebody else do that
[L1932] [01:09:34.08] and think about, okay, I mean, it's kind
[L1933] [01:09:36.32] of like with with Codeex now, like what
[L1934] [01:09:38.40] code do should I personally write to
[L1935] [01:09:40.96] maximize my impact versus if someone
[L1936] [01:09:42.88] else could do it about as well as me,
[L1937] [01:09:45.28] let's say 80% as good, I should probably
[L1938] [01:09:47.44] let, you know, have someone else do
[L1939] [01:09:48.88] that. Um and but but even then you know
[L1940] [01:09:53.92] if you're leading a fivep person project
[L1941] [01:09:56.64] is that still you know still getting to
[L1942] [01:09:58.16] E8 E9 impact still hard. Um so really
[L1943] [01:10:04.56] finding that that uh project that's a
[L1944] [01:10:07.28] force multiplier. So, you know, like
[L1945] [01:10:09.12] like uh like the virtual file system was
[L1946] [01:10:11.12] a really great project because that was
[L1947] [01:10:12.88] gonna, you know, we knew that down the
[L1948] [01:10:14.80] road like this was really going to
[L1949] [01:10:15.84] unlock so many things, prevent us from
[L1950] [01:10:18.00] from being completely blocked, right? Um
[L1951] [01:10:20.96] actually another big part of it is um
[L1952] [01:10:24.00] and you know one of my managers talked
[L1953] [01:10:25.92] to me about it is um you know not
[L1954] [01:10:29.20] actually recognizing senior managers
[L1955] [01:10:31.60] enough who are the person who um pairs
[L1956] [01:10:35.76] the senior IC with the right project
[L1957] [01:10:38.72] >> and uh because some senior engineers are
[L1958] [01:10:42.24] amazing uh you know fixerscoders
[L1959] [01:10:46.72] but they're not the idea cumber upers
[L1960] [01:10:48.56] with and um they're the but they're the
[L1961] [01:10:50.96] person you want for like you know very
[L1962] [01:10:52.88] difficult um technical projects. I don't
[L1963] [01:10:54.88] want to like out anybody here but I have
[L1964] [01:10:57.04] people in mind and um but but you know a
[L1965] [01:11:00.16] lot of times it's the manager who
[L1966] [01:11:01.36] realizes like oh this project needs this
[L1967] [01:11:03.76] person right and like that person would
[L1968] [01:11:05.52] have never realized it themselves. one
[L1969] [01:11:07.60] of your old colleagues, Adam Ernst, I
[L1970] [01:11:09.52] think I asked him, you know, what are
[L1971] [01:11:11.04] some other engineers that you admire and
[L1972] [01:11:12.64] why? And you know, he he mentioned your
[L1973] [01:11:14.40] name, of course. And specifically, he
[L1974] [01:11:16.40] talked about your ability to start
[L1975] [01:11:19.28] projects was really good. And obviously,
[L1976] [01:11:21.20] I mean, you look at all these projects,
[L1977] [01:11:23.28] right? I mean, a lot of them you created
[L1978] [01:11:25.52] them out of nowhere, like it was just
[L1979] [01:11:27.76] you had an idea and you went off and
[L1980] [01:11:29.92] built a prototype, you came back and you
[L1981] [01:11:31.92] were very convincing that it was a
[L1982] [01:11:33.28] better solution. Do you have any advice
[L1983] [01:11:35.12] for engineers who they have a a problem
[L1984] [01:11:38.16] and a solution and they want to like
[L1985] [01:11:39.76] build a project from scratch? I mean I
[L1986] [01:11:42.24] think I don't know a lot of good
[L1987] [01:11:43.28] projects I think come from being a
[L1988] [01:11:44.56] little bit dissatisfied about about
[L1989] [01:11:46.48] something, right? And I think um you
[L1990] [01:11:49.04] know it's funny like sometimes I uh for
[L1991] [01:11:51.28] better or for worse I was just so
[L1992] [01:11:53.60] charging ahead and just like building
[L1993] [01:11:55.60] the thing that like not really thinking
[L1994] [01:11:57.28] about um like what the best way to do it
[L1995] [01:12:00.80] was. So, actually a really funny example
[L1996] [01:12:02.56] is um Google Calendar. So, going back
[L1997] [01:12:05.44] really far. I was like, I want weather.
[L1998] [01:12:08.00] I want to have weather all little icons
[L1999] [01:12:10.24] showing the weather in Google Calendar
[L2000] [01:12:12.24] and I was like, I'm going to do it, you
[L2001] [01:12:13.60] know. And I had mostly been JavaScript
[L2002] [01:12:15.76] especially and not done any of the
[L2003] [01:12:17.12] backend stuff. And I just like charged
[L2004] [01:12:20.08] through and I cobbled things together
[L2005] [01:12:22.32] and uh you know, made it happen. And
[L2006] [01:12:24.64] then then my tech lead was like, "Wait,
[L2007] [01:12:26.16] how are you um how are you storing that
[L2008] [01:12:28.88] information about like the weather and
[L2009] [01:12:30.48] stuff and I was like, "Oh, I I just
[L2010] [01:12:32.80] like, you know, threw a blob of like XML
[L2011] [01:12:34.72] and everything like thing." He's like,
[L2012] [01:12:37.12] he's like, "We should have talked about
[L2013] [01:12:38.32] protocol buffers or I was like, you
[L2014] [01:12:40.88] know, like binary formats and save bytes
[L2015] [01:12:42.48] that I like I was just so, you know, set
[L2016] [01:12:46.16] on weather of all things that like I
[L2017] [01:12:47.84] never bothered to ask anybody if there
[L2018] [01:12:49.12] was like a better way to do what I was
[L2019] [01:12:50.32] doing." I was like, "It's done." So I I
[L2020] [01:12:52.08] mean I guess that's a a unique skill of
[L2021] [01:12:54.96] yours is the digging into the satis
[L2022] [01:12:57.44] dissatisfaction and solving your own
[L2023] [01:12:59.44] problems. Seems like almost every single
[L2024] [01:13:01.44] one of these projects is I want my I
[L2025] [01:13:05.20] want something to happen. This this
[L2026] [01:13:06.64] shouldn't be this way and then you went
[L2027] [01:13:07.92] and you solved it.
[L2028] [01:13:09.04] >> Yeah.
[L2029] [01:13:09.68] >> Yeah. Um but I think another unique
[L2030] [01:13:12.16] thing that I see is a lot of people they
[L2031] [01:13:14.32] they get to work and they I don't know
[L2032] [01:13:16.48] they're they're in their dev
[L2033] [01:13:17.60] environment. I'm sure there were many
[L2034] [01:13:19.76] other people who saw with the buck story
[L2035] [01:13:21.84] for instance they go oh wow this build
[L2036] [01:13:23.36] is really slow oh well like I guess I'm
[L2037] [01:13:26.48] going to go to the micro kitchen and get
[L2038] [01:13:28.56] call it builds
[L2039] [01:13:30.00] >> what gave you the confidence to know
[L2040] [01:13:32.16] that you could make it so much better
[L2041] [01:13:34.72] >> I mean that one was you know I I have to
[L2042] [01:13:38.16] credit like having been at Google I
[L2043] [01:13:39.92] never worked on the Blaze team I never
[L2044] [01:13:41.36] knew how that like worked I never
[L2045] [01:13:42.96] touched their code or anything but I was
[L2046] [01:13:44.32] like I know that there's a thing out
[L2047] [01:13:45.92] there that has this shape and is a lot
[L2048] [01:13:47.92] better in this thing. So that's an
[L2049] [01:13:49.44] existence proof.
[L2050] [01:13:51.04] >> Um whether I could do it or not like
[L2051] [01:13:53.20] TBD, right? But I think that was helpful
[L2052] [01:13:55.76] on that one.
[L2053] [01:13:56.96] >> Um you know I yeah I mean there's a lot
[L2054] [01:13:59.68] of I guess prior art that gives me you
[L2055] [01:14:02.40] know confidence and things and I think
[L2056] [01:14:04.16] and you know I usually generally
[L2057] [01:14:05.68] identify myself as a coding machine. I
[L2058] [01:14:07.28] guess with codeex now everyone wants a
[L2059] [01:14:08.32] coding machine but um that you know I
[L2060] [01:14:10.96] felt that I always had confidence like
[L2061] [01:14:13.60] you know build a prototype correctly
[L2062] [01:14:14.88] right and at least answer that question
[L2063] [01:14:16.16] or like the basic my test my basic
[L2064] [01:14:18.16] hypothesis like spiritually should there
[L2065] [01:14:20.96] be a way forward to this thing that I
[L2066] [01:14:22.88] think should exist and you know
[L2067] [01:14:23.92] generally I could you know you're if you
[L2068] [01:14:25.76] are determined you find a way
[L2069] [01:14:28.00] >> yeah I've noticed that pattern um a lot
[L2070] [01:14:30.16] of people who go to big companies they
[L2071] [01:14:31.84] see this worldclass infrastructure and
[L2072] [01:14:34.64] then they go to the other company. Oh,
[L2073] [01:14:37.12] you don't have this, you don't have
[L2074] [01:14:38.16] this. And they build their, you know,
[L2075] [01:14:39.52] those new versions of it.
[L2076] [01:14:41.68] >> I've read a lot of your writing at this
[L2077] [01:14:43.12] point, and it is so clear. It's some of
[L2078] [01:14:46.24] the best examples of good technical
[L2079] [01:14:48.24] writing. What advice would you have for
[L2080] [01:14:50.24] engineers who want to write better?
[L2081] [01:14:52.56] >> I mean, I think a lot of it is well, I
[L2082] [01:14:54.64] think reading other good writing is a is
[L2083] [01:14:56.32] a certainly a good start, right? You
[L2084] [01:14:58.08] started maybe, you know, consciously or
[L2085] [01:14:59.84] subconsciously start to pick up patterns
[L2086] [01:15:01.28] of like what what is out there. I think
[L2087] [01:15:04.00] um you know really high level thinking
[L2088] [01:15:06.56] about like what what is it that I'm
[L2089] [01:15:09.12] trying to convey? What would someone
[L2090] [01:15:10.16] actually really want to know um and and
[L2091] [01:15:13.12] outlining a lot up front, right? Is that
[L2092] [01:15:16.00] a lot of people give that feedback, but
[L2093] [01:15:17.60] it's it's impressive how how really
[L2094] [01:15:20.48] important that is and just being like
[L2095] [01:15:22.72] does this set of things like linearly
[L2096] [01:15:25.04] follow? I think is a big thing. And and
[L2097] [01:15:28.64] and then asking yourself, oh, I went
[L2098] [01:15:30.88] from this point to this point. Was that
[L2099] [01:15:32.32] too big of a jump? Is there something
[L2100] [01:15:33.60] that like somebody actually like would
[L2101] [01:15:35.04] have reasonably missed? And I think
[L2102] [01:15:37.92] uh personally I feel like that's I have
[L2103] [01:15:40.56] I have reasonable feel for like what
[L2104] [01:15:42.48] where that gap would arise. And like and
[L2105] [01:15:44.64] then if you can kind of anticipate that
[L2106] [01:15:46.80] and magically put in the example that
[L2107] [01:15:48.96] like someone would have that someone
[L2108] [01:15:50.72] needed to make that jump. Um I think
[L2109] [01:15:53.92] like that at least for for technical
[L2110] [01:15:56.56] writing is like is is a big deal.
[L2111] [01:15:59.20] you have that career note that I love
[L2112] [01:16:00.96] and at the at the beginning of it uh you
[L2113] [01:16:03.60] lay out this three-step plan for impact.
[L2114] [01:16:06.48] >> Can you explain that three three stuff
[L2115] [01:16:08.56] on early? Feel like that's a good
[L2116] [01:16:10.00] algorithm for people to use in their
[L2117] [01:16:11.76] careers.
[L2118] [01:16:12.48] >> Step one is uh figure out what you
[L2119] [01:16:14.72] really like to do, right? And you know,
[L2120] [01:16:16.48] as I mentioned, like [sighs]
[L2121] [01:16:18.48] it's good to broaden that, but it's also
[L2122] [01:16:20.88] good to to be honest with yourself so
[L2123] [01:16:23.60] you don't know. and like the the quote
[L2124] [01:16:25.12] the hero quest that I went on that that
[L2125] [01:16:26.72] didn't pan out because I I was working
[L2126] [01:16:28.16] on stuff that I didn't really, you know,
[L2127] [01:16:30.00] truly love. Um, and then two, step two
[L2128] [01:16:33.52] was figuring out what your employer is,
[L2129] [01:16:35.84] what's really valuable to them, right?
[L2130] [01:16:37.92] And as I talked about at Google, I I
[L2131] [01:16:39.68] didn't do a good job of that. I did
[L2132] [01:16:40.88] stuff that I was really excited about,
[L2133] [01:16:42.32] but it wasn't, you know, it wasn't uh,
[L2134] [01:16:45.04] you know, AdWords for Google or anything
[L2135] [01:16:46.64] like that. Um, yeah. And then step three
[L2136] [01:16:50.00] is like find that intersection and then
[L2137] [01:16:51.76] just really lean into that. Um, and you
[L2138] [01:16:54.40] know, the more that you can do that, I
[L2139] [01:16:56.24] think the more successful, you know,
[L2140] [01:16:58.32] you're going to be and and and the and
[L2141] [01:16:59.84] the challenge is sometimes it's not
[L2142] [01:17:01.12] always there, right? And maybe you have
[L2143] [01:17:03.28] to go, you know, find somewhere else to
[L2144] [01:17:05.04] make that happen.
[L2145] [01:17:06.72] >> Okay. And then, yeah, last question for
[L2146] [01:17:08.24] you is, uh, if you go back to yourself
[L2147] [01:17:10.16] at the beginning of your career knowing
[L2148] [01:17:11.60] everything you know now, what advice
[L2149] [01:17:13.44] would you give yourself? I think I
[L2150] [01:17:15.60] should have been
[L2151] [01:17:17.60] open to learning more things sooner and
[L2152] [01:17:20.64] and I I you know to be a little gentle
[L2153] [01:17:23.60] to myself and I think other people are
[L2154] [01:17:24.88] in that situation is that you know
[L2155] [01:17:26.88] there's so much to learn when you're
[L2156] [01:17:28.64] starting and then whatever your first
[L2157] [01:17:30.72] programming language is I think it's
[L2158] [01:17:32.00] funny I think everyone has a soft spot
[L2159] [01:17:33.76] for they'll like make excuses for it
[L2160] [01:17:35.60] like ever like oh this no it's a totally
[L2161] [01:17:37.04] good language and I think it's because
[L2162] [01:17:39.04] it's like the first thing that enabled
[L2163] [01:17:40.64] you to do a thing you know do anything
[L2164] [01:17:43.04] right and And then it's like, oh, okay,
[L2165] [01:17:46.08] I can finally do something. It's such a
[L2166] [01:17:47.60] relief. And um and but it's also like a
[L2167] [01:17:51.12] hazard because like then you kind of
[L2168] [01:17:52.56] want to hold on to that thing because
[L2169] [01:17:53.84] like you're finally productive and now
[L2170] [01:17:55.44] you're like, ah, it took so long to get
[L2171] [01:17:57.28] to this foothold. I don't know how long
[L2172] [01:17:59.36] it's going to take to get to the next
[L2173] [01:18:00.40] foothold. So I think like in you know,
[L2174] [01:18:02.24] my particular case, I probably did maybe
[L2175] [01:18:04.32] went too deep with JavaScript and like
[L2176] [01:18:06.08] like I said, it took a long time before
[L2177] [01:18:07.36] I wrote NEC. Um, and I think uh, you
[L2178] [01:18:11.52] know, I if I had been a little bit more
[L2179] [01:18:13.68] curious and a little more flexible in
[L2180] [01:18:15.92] terms of what like types of projects I
[L2181] [01:18:17.68] was willing to take on or things I was
[L2182] [01:18:18.88] willing to learn and you know it came
[L2183] [01:18:20.24] eventually, but I think if uh that is
[L2184] [01:18:22.80] probably the biggest thing that maybe
[L2185] [01:18:24.00] could have made a shift for me earlier.
[L2186] [01:18:25.68] Yeah, I I gather from your story there
[L2187] [01:18:28.08] was um a point with the Xcode where you
[L2188] [01:18:31.12] said you you you hated Objective
[L2189] [01:18:33.43] [laughter] C and then you you were you
[L2190] [01:18:35.60] were coming up with like ways to compile
[L2191] [01:18:38.16] the Objective C into Java or Java into
[L2192] [01:18:40.48] Objective C or something like that maybe
[L2193] [01:18:42.56] and then
[L2194] [01:18:43.68] >> you know also talking about the C++ for
[L2195] [01:18:46.00] miles. It was like
[L2196] [01:18:47.52] >> it it seemed like a very concerted okay
[L2197] [01:18:49.76] I'm going to I'm going to learn this as
[L2198] [01:18:51.68] opposed to like just kind of being open
[L2199] [01:18:53.60] to it. So
[L2200] [01:18:54.56] >> yeah. Yeah, makes sense. Well, maybe
[L2201] [01:18:56.16] with codecs in the future, it'll be less
[L2202] [01:18:58.40] of a hurdle for people. You could just
[L2203] [01:18:59.92] kind of say, "Hey, I know JavaScript.
[L2204] [01:19:02.32] Write this in Rust or whatever." No,
[L2205] [01:19:04.40] it's true. Opens a lot of doors.
[L2206] [01:19:06.32] >> Sure.
[L2207] [01:19:06.96] >> Awesome. Well, thank you so much for
[L2208] [01:19:08.24] your time. I appreciate it. All right.
[L2209] [01:19:09.60] Thank you, Ryan.
[L2210] [01:19:10.80] >> Thank you for listening to the podcast.
[L2211] [01:19:12.56] It's a passion project of mine that I've
[L2212] [01:19:14.72] really enjoyed building. Another passion
[L2213] [01:19:16.80] project that I've been working on kind
[L2214] [01:19:18.16] of in secret is building an ergonomic
[L2215] [01:19:20.64] keyboard that I wish existed and I
[L2216] [01:19:22.88] finally have a prototype. So, I'd love
[L2217] [01:19:24.56] to show you what we've built. It's ultra
[L2218] [01:19:27.36] lowprofile and ergonomic, and I couldn't
[L2219] [01:19:30.16] find anything like it on the market, so
[L2220] [01:19:31.76] that's why we built it. I'll put a link
[L2221] [01:19:33.52] to the keyboard in the description. You
[L2222] [01:19:35.20] can take a look and learn more about the
[L2223] [01:19:36.80] project there. We could definitely use
[L2224] [01:19:38.48] your support. Also, if you have any
[L2225] [01:19:40.48] feedback for me about the show, I'd love
[L2226] [01:19:42.40] to hear it. Comments on YouTube have led
[L2227] [01:19:44.88] to guests coming on like Ilia Gregoric
[L2228] [01:19:47.52] and David Fowler. I wasn't aware of them
[L2229] [01:19:49.84] until someone dropped a comment. Also,
[L2230] [01:19:52.08] feedback in the comments helped me learn
[L2231] [01:19:53.60] to reduce the number of cliffhers in the
[L2232] [01:19:56.08] intros. So, your comments definitely
[L2233] [01:19:57.92] make a difference. Please keep letting
[L2234] [01:19:59.36] me know what you'd like to see more of
[L2235] [01:20:00.96] in the show, and I'll see you in the
[L2236] [01:20:02.48] next episode.
