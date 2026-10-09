Chunk 1; segments 1–208. 

# Is "Vibecoding" Bad for the Industry | Casey Muratori

Source ID: source-0a0a19a690dbea54
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Is_Vibecoding_Bad_for_the_Industry_Casey_Muratori_en.txt
Video: https://www.youtube.com/watch?v=KNuBSNffSUo

[L10] [00:00.00] Andre Karpathy had this famous tweet
[L11] [00:03.08] that kind of coined the phrase five
[L12] [00:04.76] coding.
[L13] [00:05.28] >> Yes.
[L14] [00:06.00] >> And then you said if you thought
[L15] [00:08.20] software was bad today, buckle up
[L16] [00:10.68] because it's about to get a whole lot
[L17] [00:12.32] worse.
[L18] [00:12.92] >> Yes.
[L19] [00:13.60] >> It's been about a year and a half since
[L20] [00:16.44] that tweet came out. The tweet came out
[L21] [00:18.12] February of 2025.
[L22] [00:20.60] Would you say that that was an accurate
[L23] [00:22.88] prediction?
[L24] [00:24.40] >> To be clear, I think
[L25] [00:28.24] it the whole lot worse part is
[L26] [00:30.40] predicated on something that may not
[L27] [00:32.92] happen.
[L28] [00:34.00] And that is that the idea that we just
[L29] [00:37.52] kind of type some stuff in the computer
[L30] [00:38.92] and ship it to prod, right? Basically
[L31] [00:40.88] like, "Hey, could you make me a thing
[L32] [00:42.28] and then publish it?"
[L33] [00:44.08] becomes a common way of doing things,
[L34] [00:46.24] right? For example, also done by people
[L35] [00:49.72] who maybe don't have a computer science
[L36] [00:50.84] background. I think it's fair to say and
[L37] [00:54.40] that I wouldn't be
[L38] [00:56.28] being sort of overly dismissive of AI at
[L39] [00:58.56] this point to say that
[L40] [01:01.36] a person who is well trained in computer
[L41] [01:03.60] science using an AI to make code right
[L42] [01:06.56] now
[L43] [01:07.80] can make substantially better code than
[L44] [01:10.04] someone who doesn't know anything about
[L45] [01:11.12] computer science who is just given, you
[L46] [01:13.28] know, Fable and type some thought stuff
[L47] [01:16.00] in, right? The difference is rather
[L48] [01:18.56] dramatic, I would say, from everything
[L49] [01:20.28] that I've seen.
[L50] [01:22.20] So, part part of my
[L51] [01:25.20] concern that I was trying to express in
[L52] [01:26.84] that tweet was like
[L53] [01:28.72] if the idea is like we're just going to
[L54] [01:30.04] type stuff in and we're not going to
[L55] [01:31.40] really be checking the code, you know,
[L56] [01:33.48] someone who knows computer science is
[L57] [01:35.08] not really going to be looking at it. Um
[L58] [01:37.28] worst case scenario, it's literally just
[L59] [01:38.76] like some random person in marketing
[L60] [01:41.88] somewhere who has no idea what
[L61] [01:43.16] programming is just type some stuff in
[L62] [01:44.84] and hit crosses their fingers, right? I
[L63] [01:47.24] think we're in for a
[L64] [01:48.68] world of hurt, right? Now, it's a race,
[L65] [01:52.32] so it's hard to say because it's
[L66] [01:54.84] basically a race of how good can you
[L67] [01:57.04] make the AI versus how much adoption
[L68] [02:00.00] does it get? Right? It's a curve, right?
[L69] [02:01.60] It's like if you can make the AI good
[L70] [02:03.76] enough that the people who are adopting
[L71] [02:05.96] it at a particular rate are always using
[L72] [02:08.44] an AI that's good enough for what
[L73] [02:09.96] they're adopting it for, we wouldn't
[L74] [02:11.76] expect software to get significantly
[L75] [02:13.12] worse. If those curves go the other way,
[L76] [02:15.76] we're in a lot of trouble, right? So,
[L77] [02:17.08] we're I feel like right now we're we're
[L78] [02:18.72] almost kind of teetering on this knife's
[L79] [02:20.40] edge. It's it's really to me it feels
[L80] [02:22.52] like a foot race of like
[L81] [02:24.64] improving AI so it can be more
[L82] [02:27.20] autonomous and make better decisions
[L83] [02:29.28] without your without you needing to make
[L84] [02:31.28] them for it
[L85] [02:32.84] versus the capability level of people
[L86] [02:35.88] who are using it and the degree to which
[L87] [02:37.40] they're paying attention to its output.
[L88] [02:38.84] It's like these two curves that are just
[L89] [02:40.28] like
[L90] [02:41.52] you know, like what's
[L91] [02:42.44] >> [laughter]
[L92] [02:42.84] >> what's going to happen?
[L93] [02:44.88] I don't have a prediction. I don't know
[L94] [02:46.80] where we'll be in a year. Obviously, for
[L95] [02:49.36] all of our sake, I'm hoping that the AI
[L96] [02:52.16] curve wins
[L97] [02:54.08] because I agree like I understand
[L98] [02:58.24] certainly the perspective of people who
[L99] [03:01.20] maybe just don't like AI and don't want
[L100] [03:03.28] there to be AI. I can understand the
[L101] [03:07.44] wanting it to fail. I I understand that,
[L102] [03:10.16] right?
[L103] [03:11.40] Um and I'm no fan of AI myself, so it's
[L104] [03:14.52] not like I
[L105] [03:15.96] like I'm going to criticize someone for
[L106] [03:17.52] taking that position.
[L107] [03:19.72] But at the end of the day, if you're
[L108] [03:21.16] talking about something that tons of
[L109] [03:22.60] people are using,
[L110] [03:24.92] you're going to kind of want it to be
[L111] [03:26.44] good. Like I think at this point, given
[L112] [03:28.72] the level of adoption of AI, I really
[L113] [03:31.16] don't think it's would be great if it
[L114] [03:33.76] stopped getting any better right now.
[L115] [03:36.00] Like if this was as good as it was going
[L116] [03:37.32] to get, I think that might be bad.
[L117] [03:39.48] Um certainly 6 months ago, I think that
[L118] [03:42.92] was true.
[L119] [03:44.04] Uh and I think it's probably still true
[L120] [03:45.68] today. So, I think ideally, if you want
[L121] [03:49.48] software to not be terrible,
[L122] [03:52.12] you have to kind of still be hoping that
[L123] [03:54.20] 6 months from now the AIs are again
[L124] [03:57.08] significantly better than they were,
[L125] [03:58.68] right? Like that that is the only way
[L126] [04:01.00] out of the current situation as I see
[L127] [04:03.84] it, right?
[L128] [04:05.80] Uh I don't know if that's fair, but
[L129] [04:07.40] that's my that's my sort of feeling on
[L130] [04:09.36] that.
[L131] [04:10.32] >> One of your other top tweets, it was,
[L132] [04:13.04] you know, Shopify put out this internal
[L133] [04:15.44] memo and you just, you know, you
[L134] [04:17.44] replied, you know, "Slopify."
[L135] [04:19.36] >> Yes. [laughter]
[L136] [04:19.92] >> I guess it's cuz in this tweet it's
[L137] [04:22.16] leadership pushing the adoption curve
[L138] [04:24.36] maybe harder than the capabilities of
[L139] [04:26.88] the AI in this case.
[L140] [04:28.52] >> Yeah, although I also just like the pun.
[L141] [04:31.24] One of the things that I think is most
[L142] [04:33.52] unfortunate about the AI adoption as
[L143] [04:36.48] I've seen it
[L144] [04:38.00] is just the
[L145] [04:40.24] because people think that it's going to
[L146] [04:42.80] be this major um
[L147] [04:45.64] I guess if I had to categorize the way
[L148] [04:47.08] it appears that companies are reasoning
[L149] [04:48.76] about it, they're assuming that if they
[L150] [04:50.84] don't get in early, it will be a big
[L151] [04:53.00] disaster for them,
[L152] [04:54.52] right? Like like there's a tremendous
[L153] [04:56.00] like they don't just think, "Oh, well,
[L154] [04:57.96] we can just wait until the AI does what
[L155] [04:59.84] we need it to do and then start using
[L156] [05:01.24] it." They're like, "No, we have to do it
[L157] [05:02.72] now, like even before we know whether it
[L158] [05:05.00] can really do the thing that we want it
[L159] [05:06.20] to do or whether we know whether the
[L160] [05:07.32] outcomes will be good. Everyone has to
[L161] [05:08.88] do it right now. Let's do this, right?"
[L162] [05:11.24] Um and I understand why they want why
[L163] [05:13.48] why they're going about that way because
[L164] [05:14.52] they think that that that is critical,
[L165] [05:15.92] right? They obviously believe that's
[L166] [05:17.00] very important.
[L167] [05:18.88] Um and to me, that's just that's just
[L168] [05:21.52] kind of terrifying because
[L169] [05:23.72] as with any technology, the sane way to
[L170] [05:26.16] do it is to
[L171] [05:28.12] measure its capabilities, see how well
[L172] [05:30.96] it is able to solve problems that you
[L173] [05:32.28] have, see if it solves them faster than
[L174] [05:34.48] the way that you were do doing it, and a
[L175] [05:37.84] put it into a workflow at such a time as
[L176] [05:40.28] you've determined that it is a net
[L177] [05:41.96] positive. That's just the same like
[L178] [05:43.84] that's the what you would do with any
[L179] [05:44.88] technology, right? And you'd probably
[L180] [05:46.92] have like your team of people whose job
[L181] [05:49.04] it is to assess this thing and they're
[L182] [05:50.80] out there yolo swagging it, right?
[L183] [05:52.16] They've got
[L184] [05:53.56] 3,000 agents working on this cluster
[L185] [05:55.80] talking to each other doing, you know,
[L186] [05:57.56] God knows what, right? And uh
[L187] [06:00.56] So, there's going to be that and
[L188] [06:02.20] someone's going to be doing that, but
[L189] [06:03.12] that is should not be every org, right?
[L190] [06:04.80] Like you wouldn't just be like everyone
[L191] [06:06.68] needs to use a ton of tokens, right? Um
[L192] [06:10.44] So, yeah, like I I do have concerns
[L193] [06:12.60] about that. I don't think that that the
[L194] [06:15.32] way AI adoption was done was
[L195] [06:18.04] was the best way for quality in
[L196] [06:20.20] software.
[L197] [06:21.64] But,
[L198] [06:22.84] I would temper that statement with just
[L199] [06:25.00] the obvious fact that like we were not
[L200] [06:27.32] exactly a five-nines uh industry to
[L201] [06:31.20] start out with. Like software quality
[L202] [06:33.12] was really pretty low rolling into the
[L203] [06:36.52] AI era.
[L204] [06:37.84] So, I always try to just
[L205] [06:39.88] also caveat most of the things that I
[L206] [06:41.76] have to say that might be critical of a
[L207] [06:44.00] particular thing happening AI with just
[L208] [06:45.64] the fact that like look, it wasn't
[L209] [06:47.24] particularly great beforehand, either.
[L210] [06:50.24] Uh a lot of the software was pretty low
[L211] [06:52.08] quality and so you can't
[L212] [06:55.64] some AI things may may make things
[L213] [06:58.20] worse, but it's not like software was
[L214] [07:00.32] amazing and the AI showed up and ruined
[L215] [07:02.24] everything. That is a completely
[L216] [07:03.76] ridiculous narrative that that is not
[L217] [07:05.44] true at all.
