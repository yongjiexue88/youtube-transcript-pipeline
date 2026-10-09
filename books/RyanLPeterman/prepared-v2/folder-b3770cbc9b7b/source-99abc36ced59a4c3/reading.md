# Instagram Principal Eng (IC8) On Why He Accepts Broken Code

Source ID: source-99abc36ced59a4c3
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Instagram_Principal_Eng_(IC8)_On_Why_He_Accepts_Broken_Code_en.txt
Video: https://www.youtube.com/watch?v=836CauoVekQ

[L10] [00:00.08] Even if I see your diff is going to blow
[L11] [00:01.76] up production.
[L12] [00:03.60] >> I will I will comment on it and be like
[L13] [00:05.44] this is going to blow up production and
[L14] [00:07.52] then accept it and be like, "Yeah, make
[L15] [00:09.04] sure you fix that first, right?" I've
[L16] [00:10.96] never had a case where someone's like
[L17] [00:12.32] landed it cuz like people put up diffs
[L18] [00:14.16] and like 5 minutes later it's like stamp
[L19] [00:15.60] on me and they're like, "What the hell
[L20] [00:16.72] is going on?" [laughter] And that's a
[L21] [00:18.56] lot cuz I'm on top of it. But also
[L22] [00:19.92] because I have this philosophy on like
[L23] [00:21.60] diff reviews and risk where if I don't
[L24] [00:23.60] think the diff is risky, right? You're
[L25] [00:25.04] getting a very rudimentary review and
[L26] [00:26.96] like basically you can put that code in
[L27] [00:29.28] like so if it's like gated, it's not on
[L28] [00:32.16] a core system, right? These things then
[L29] [00:34.88] you're going to just get a very high
[L30] [00:36.80] level diff and then basically I'm just
[L31] [00:38.96] like trusting you.
[L32] [00:39.92] >> So you're saying you you modulate your
[L33] [00:42.64] level of time investment based on how
[L34] [00:44.64] risky the diff is
[L35] [00:46.40] >> based on how risky the diff is, right?
[L36] [00:47.92] So if you're rewriting it, right, we're
[L37] [00:49.36] it it's all gated right now and we just
[L38] [00:51.12] want the highle trunk architecture to be
[L39] [00:53.52] correct. If you're working on like some
[L40] [00:54.88] child component or something, it's like
[L41] [00:57.44] cool, it's gated. It's not critical to
[L42] [00:59.52] the system. Like
[L43] [01:01.20] >> yeah, I'm trusting you to do whatever
[L44] [01:03.28] you need to do over there.
[L45] [01:04.32] >> So you'll just stamp it stamp stamp it
[L46] [01:06.48] let it. Yeah.
[L47] [01:07.60] >> Some people view quality different view
[L48] [01:09.36] as a uh like an important thing rather
[L49] [01:13.76] than just stamping. So do you ever get
[L50] [01:15.52] push back on? This is my controversial
[L51] [01:17.28] one for sure. So yeah, so I I think that
[L52] [01:20.32] is correct for like the the trunk of the
[L53] [01:22.64] system, the core core parts of the
[L54] [01:24.32] system or anything that's already live
[L55] [01:25.84] in prod like is going to get pretty
[L56] [01:28.08] thorough review. Yeah, if it's not live
[L57] [01:30.08] and prod and it is one of these sub like
[L58] [01:33.20] sub parts of the system or less critical
[L59] [01:35.28] things like I'll still skim it to make
[L60] [01:37.28] sure you didn't do anything like
[L61] [01:38.64] absolutely crazy like introduce like I
[L62] [01:40.96] don't know security issues or you know
[L63] [01:42.80] start mining crypto on our servers or
[L64] [01:45.28] something
[L65] [01:46.08] >> but uh yeah I'll just like let let that
[L66] [01:49.76] let that fly in.
[L67] [01:51.12] >> Yeah, I I mean it makes sense. So you're
[L68] [01:53.52] basically trading off speed for I guess
[L69] [01:56.72] quality, but it's not dumb quality. It's
[L70] [02:00.16] like these are places where it makes
[L71] [02:01.84] sense to make the trade-off
[L72] [02:03.20] >> where you make Yeah. So you can have
[L73] [02:04.72] like lower quality components for like
[L74] [02:06.88] these the child the child parts of the
[L75] [02:09.04] system, right? Or the leaf parts of the
[L76] [02:10.56] system. And also these parts are like
[L77] [02:12.24] generally easier to unit test.
[L78] [02:14.40] >> If they do fail, they only blow up like
[L79] [02:16.24] a small part of it, right?
[L80] [02:18.48] >> Just a little blow up.
[L81] [02:19.52] >> Just a little part of it. If it is badly
[L82] [02:21.20] architected, it's only on this like tiny
[L83] [02:24.40] part of the system. It's not impacting,
[L84] [02:26.24] you know, hundreds of engineers. Maybe
[L85] [02:27.52] it impacts a couple and someone one day
[L86] [02:29.60] is like, "What the hell's up with this?"
[L87] [02:31.60] >> Doesn't take a long time to rewrite.
[L88] [02:33.04] Right. Right.
[L89] [02:33.76] >> If you mess up the architecture in the
[L90] [02:34.96] core trunk, probably takes like hundreds
[L91] [02:36.56] of people a long time to like fix. Have
[L92] [02:38.96] you ever had someone I remember early in
[L93] [02:40.72] my career I was all about speed and I
[L94] [02:45.84] was approving some diffs and then
[L95] [02:47.68] someone would come back to me and say
[L96] [02:49.20] why'd you approve this that was too
[L97] [02:51.36] >> you know like let's slow down a little
[L98] [02:53.36] bit on this
[L99] [02:54.48] >> oh they get some feedback or someone
[L100] [02:55.92] says hey
[L101] [02:57.28] >> you know calm down like this defin this
[L102] [02:59.12] definitely happens actually interesting
[L103] [03:00.72] thing so teach the people close to me in
[L104] [03:03.92] my teams that like hey it's okay buy
[L105] [03:07.20] stamp your diff to put it back in review
[L106] [03:10.08] again if you actually need deeper review
[L107] [03:13.20] >> or like flag it flag it in the summary
[L108] [03:15.44] or the test plan like or comment on it
[L109] [03:17.44] like hey I'm actually looking for a deep
[L110] [03:19.28] review on this if you know that's how
[L111] [03:21.04] our team operates now and this is
[L112] [03:22.80] actually really good because I might
[L113] [03:24.48] have thought it's like a child part of
[L114] [03:26.16] the system and maybe it is still a child
[L115] [03:27.76] part of the system but they've thought
[L116] [03:29.20] hey this is like could be like more
[L117] [03:31.52] performant or like I actually want you
[L118] [03:33.44] to double check this
[L119] [03:34.96] >> uh so then we use that signal to be like
[L120] [03:36.80] okay this person actually wants thing.
[L121] [03:38.40] So if I missed it, even if they put a
[L122] [03:40.24] comment on it, they'll throw it back
[L123] [03:41.68] into review and like be like need real
[L124] [03:44.16] review or something like that cuz they
[L125] [03:45.92] knew they knew what happened.
[L126] [03:47.36] >> Yeah. Yeah. Yeah.
[L127] [03:48.24] >> Yeah. I see. That makes sense.
[L128] [03:50.24] >> But yeah, there's definitely this is not
[L129] [03:51.84] the philosophy of everyone at Meta,
[L130] [03:53.44] right? Like we most people it's like
[L131] [03:55.44] >> quality high quality for everything.
[L132] [03:57.28] >> Yeah. And it depends on the system
[L133] [03:59.12] though.
[L134] [03:59.52] >> Depends on the system. Also depends on
[L135] [04:01.04] like this is like trust you build on
[L136] [04:02.40] your team too, right? If you're new on
[L137] [04:03.76] the team
[L138] [04:04.40] >> probably not going to get this treatment
[L139] [04:05.60] for the first couple of weeks. Yeah.
[L140] [04:06.88] Yeah.
[L141] [04:07.20] >> Although I do want to defer to like how
[L142] [04:09.12] do I accept this diff, not how do I
[L143] [04:11.20] reject this diff,
[L144] [04:12.56] >> which I think is an important philosophy
[L145] [04:14.72] to have.
[L146] [04:16.00] >> Why is that?
[L147] [04:16.72] >> Yeah.
[L148] [04:17.36] >> Uh cuz like I'm not trying to like knit
[L149] [04:19.68] your code and get you to write it the
[L150] [04:21.20] exact way I would write it, right? I'm
[L151] [04:23.12] trying to be like, okay, what is
[L152] [04:24.56] absolutely blocking this thing from
[L153] [04:26.24] going to going to production? Like big
[L154] [04:29.84] highle architecture things like I don't
[L155] [04:32.24] know some critical bugs like is it going
[L156] [04:34.32] to blow up prod right? not like write it
[L157] [04:36.72] exactly the way I would write it.
[L158] [04:38.40] >> Right. I think that takes a while to get
[L159] [04:40.08] to too, right? Like more senior
[L160] [04:41.84] engineers usually become amendable to
[L161] [04:43.60] this.
[L162] [04:44.08] >> Yeah.
[L163] [04:44.48] >> But when you're in Yeah. When you're
[L164] [04:46.08] like in the first 5 years of your
[L165] [04:47.36] career, maybe you've only seen a few
[L166] [04:48.88] ways of writing it, right? So you want
[L167] [04:50.24] people to write it that exact way.
[L168] [04:52.40] >> Yeah. Yeah. Definitely. I I think when
[L169] [04:55.36] you're working in a team where there's
[L170] [04:57.20] high trust and you get to the point
[L171] [04:58.88] where people
[L172] [05:00.40] >> they have feedback but they accept with
[L173] [05:02.24] nits, you know. I I love that because
[L174] [05:04.40] you just everyone's just trusting each
[L175] [05:05.60] other, you know, move fast.
[L176] [05:06.72] >> Yeah.
[L177] [05:07.20] >> And I have some feedback, but
[L178] [05:09.68] >> it's not that important. It's just like
[L179] [05:12.08] >> take it if you will. Man, this is where
[L180] [05:13.92] I push that needle even further again.
[L181] [05:15.60] So, I will like even if I see your diff
[L182] [05:17.60] is going to blow up production.
[L183] [05:20.08] >> I will I will comment on it and be like,
[L184] [05:21.76] "This is going to blow up production."
[L185] [05:23.92] >> And then accept it and be like, "Yeah,
[L186] [05:25.36] make sure you fix that first." Right.
[L187] [05:27.28] And like I've never had a case where
[L188] [05:28.96] someone's like landed it.
[L189] [05:30.40] >> Yeah. like with a comment on it that
[L190] [05:32.16] says, "Hey, this is going to blow up
[L191] [05:33.20] production." Cuz you can can you imagine
[L192] [05:34.72] like sitting in SE review or something
[L193] [05:36.32] and someone's like,
[L194] [05:37.44] >> "The diff had a comment on it. This is
[L195] [05:39.20] going to blow up production." And it
[L196] [05:40.40] blow up.
[L197] [05:41.12] >> That's wild that.
[L198] [05:43.12] >> Yeah. Except I just trust him to fix it.
[L199] [05:45.04] Right. Like
[L200] [05:45.44] >> Yeah. Yeah. Yeah.
[L201] [05:46.24] >> Fix it the right way. Once again, if
[L202] [05:48.08] they have trust, if it's like a new
[L203] [05:49.60] person on the team and I'm not sure if
[L204] [05:51.04] they're going to fix it the right way,
[L205] [05:53.04] >> right, I might be like, "Ping me again
[L206] [05:54.64] when it's like ready."
[L207] [05:55.84] >> Yeah. Yeah.
[L208] [05:56.40] >> But yeah, 99% of the time, I'll just
[L209] [05:58.08] like accept and go.
[L210] [05:59.20] >> Yeah.
[L211] [05:59.52] >> And Yeah. haven't had to do the thing
[L212] [06:01.44] where I pull back because I've never had
[L213] [06:03.04] one that's been shipped accidentally
[L214] [06:05.20] >> exploded production.
[L215] [06:07.36] >> And that's actually a little bit of a
[L216] [06:08.48] philosophy I use across like I guess
[L217] [06:10.80] building these systems judging how fast
[L218] [06:12.72] I'm moving.
[L219] [06:14.00] >> If I'm doing something and it's not I'm
[L220] [06:16.48] not getting feedback that it's like
[L221] [06:17.92] broken or I'm not seeing negative
[L222] [06:19.44] effects from it, right? Even if it is
[L223] [06:21.12] controversial and crazy,
[L224] [06:22.48] >> I'll keep pushing the boundary on it,
[L225] [06:24.48] right? Same as our rollouts. Like if
[L226] [06:26.00] we're at 1% we're getting like very
[L227] [06:27.68] little feedback and like metrics are
[L228] [06:29.92] looking good and we might move to like
[L229] [06:32.00] 10% the next day and people are like
[L230] [06:33.60] that's crazy like step to like two three
[L231] [06:35.28] five things. It's like
[L232] [06:36.64] >> well not we're not getting any like
[L233] [06:38.64] >> signals that it's not going poorly.
[L234] [06:40.64] >> As soon as we get signals that it's
[L235] [06:42.00] going poorly we start pulling back. But
[L236] [06:44.40] >> otherwise I find you like move too
[L237] [06:46.24] slowly.
[L238] [06:46.96] >> Yeah.
[L239] [06:47.44] >> Right. You want to be moving at like the
[L240] [06:49.28] fastest speed you can without ruining
[L241] [06:51.44] things. Right. So, if you're not getting
[L242] [06:53.52] if you're not
[L243] [06:54.48] >> making anything worse, like keep trying
[L244] [06:56.08] to find that edge.
[L245] [06:57.36] >> Yeah. I I had a tech lead early in my
[L246] [07:00.32] career and I had taken down prod or
[L247] [07:02.72] something and I was talking to him about
[L248] [07:05.36] it and he you know at one on one end you
[L249] [07:08.72] shouldn't break prod generally but he
[L250] [07:11.28] also said if you never break prod
[L251] [07:15.28] that's probably not also optimal like
[L252] [07:17.76] there there should be some level of risk
[L253] [07:21.84] otherwise you're moving too slowly and
[L254] [07:23.44] so
[L255] [07:23.68] >> yeah exactly
[L256] [07:24.48] >> yeah try not to break prod But
[L257] [07:27.20] >> if you never break it, you're probably
[L258] [07:29.28] like very slow and
[L259] [07:30.64] >> Yeah. And if you're breaking it every
[L260] [07:32.08] day, you're probably going way too fast.
[L261] [07:34.40] Yeah.
[L262] [07:34.80] >> Exactly.
[L263] [07:36.24] >> Hey, thanks for watching that clip. If
[L264] [07:37.84] you thought it was interesting, it's
[L265] [07:39.12] part of a longer conversation which you
[L266] [07:40.88] can find right here, right now. And as
[L267] [07:43.12] always, if you have any feedback for me,
[L268] [07:44.72] I'd love to hear it. You can leave a
[L269] [07:46.40] comment on YouTube. I read every single
[L270] [07:48.32] one that I get.
