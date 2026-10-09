Chunk 1; segments 1–327. 

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
