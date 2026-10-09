# Meta Distinguished Eng (IC9) On Major Failed Project Learnings

Source ID: source-e763d45a670dd9ac
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Meta_Distinguished_Eng_(IC9)_On_Major_Failed_Project_Learnings_en.txt
Video: https://www.youtube.com/watch?v=u6r0asGw4ws

[L10] [00:00.00] So, component script was interesting
[L11] [00:01.32] because it was a total and complete
[L12] [00:02.80] failure. And I worked on it for like 2
[L13] [00:04.48] years.
[L14] [00:05.80] At the time, my manager was a guy named
[L15] [00:08.72] Ari Grant, who was a force of nature,
[L16] [00:10.80] right? He was like all over the place,
[L17] [00:12.92] very busy,
[L18] [00:14.76] carried a lot of influence.
[L19] [00:16.36] And Ari felt really strongly that we
[L20] [00:17.92] needed to get out of the per platform
[L21] [00:20.68] silo, right? So, like iOS had component
[L22] [00:22.84] kit, Android had a React and component
[L23] [00:25.20] kit inspired by then called Litho. But
[L24] [00:27.36] this meant we were writing everything
[L25] [00:28.52] multiple times, right? We had to write
[L26] [00:29.84] it in component kit for iOS, we had to
[L27] [00:31.28] write it in Android. He wanted to have a
[L28] [00:32.96] cross-platform solution. React Native
[L29] [00:34.80] was not that solution, and we knew that.
[L30] [00:36.88] At this time, we'd tried React Native
[L31] [00:38.32] and it didn't go well. The reason was,
[L32] [00:40.36] in my opinion, this is just my opinion,
[L33] [00:42.28] React Native is designed to be in charge
[L34] [00:44.08] of the entire app. It works really well
[L35] [00:45.76] if your entire app is React Native,
[L36] [00:47.88] or if you have entire apps React Native
[L37] [00:49.56] and then small little pieces on the very
[L38] [00:51.48] bottom are native or bridged.
[L39] [00:54.04] Where it doesn't work is the way we
[L40] [00:56.36] wrote software at that time, which was
[L41] [00:58.84] we had this large, complex native app,
[L42] [01:01.68] and we wanted to slot in small pieces of
[L43] [01:04.12] cross-platform in different areas,
[L44] [01:06.20] right? So, like oh, maybe this little
[L45] [01:07.56] square on this screen is
[L46] [01:09.84] rendered using JavaScript. Maybe
[L47] [01:12.24] this tab is rendered in JavaScript and
[L48] [01:14.36] this tab is native. React Native could
[L49] [01:16.16] not do that for us at the time.
[L50] [01:18.36] They've done a lot of architectural
[L51] [01:19.36] changes to React Native in the last 10
[L52] [01:21.36] years since then, and maybe it's better
[L53] [01:22.76] at it now, but at the time, didn't
[L54] [01:24.40] really work.
[L55] [01:26.00] So, we want a cross-platform. We knew
[L56] [01:27.84] React Native was not it. What could we
[L57] [01:29.56] do? And so, Ari asked me to go and work
[L58] [01:31.80] on this. And I at the time, it was like,
[L59] [01:33.96] okay, this is the next nudge, right?
[L60] [01:35.36] Like we Byron nudged me to work on React
[L61] [01:37.84] for iOS. That was component kit, great.
[L62] [01:40.04] This is the next nudge. Work on
[L63] [01:41.32] cross-platform for our UI rendering
[L64] [01:44.44] frameworks that we use in iOS and
[L65] [01:45.64] Android. And so, I came up with a
[L66] [01:47.40] framework called component script. The
[L67] [01:49.80] idea was basically, at first, I took the
[L68] [01:51.84] React APIs, the actual React
[L69] [01:53.92] implementation. I said, what if we just
[L70] [01:55.16] made a different React Native, right?
[L71] [01:56.44] So, exactly like React Native, except
[L72] [01:58.04] that it works on top of component kit
[L73] [01:59.40] and Litho that's what we already have.
[L74] [02:01.44] This turned out to be too difficult.
[L75] [02:03.20] React had a really large surface area
[L76] [02:05.36] and a very complex surface area, and
[L77] [02:07.40] trying to make that work on on component
[L78] [02:09.68] kit and Litho was too challenging. So, I
[L79] [02:11.12] was like, all right, I'll do a smaller,
[L80] [02:14.00] pared-down API that feels just like
[L81] [02:16.44] React, but actually is simpler, and make
[L82] [02:19.08] that work on top of component kit and
[L83] [02:20.44] Litho. And I made it work. It was a real
[L84] [02:22.32] framework. People built real features on
[L85] [02:24.36] it. You could build full screens, you
[L86] [02:26.00] could build individual units, you could
[L87] [02:27.76] do all kinds of, you know, you
[L88] [02:29.12] bidirectional embeddings. You could have
[L89] [02:30.52] a native screen that had a component
[L90] [02:31.76] script unit, which had a native
[L91] [02:33.88] component inside of that. You could have
[L92] [02:35.56] a component script screen, which had a
[L93] [02:37.04] native section. All this stuff. Really
[L94] [02:39.24] cool features.
[L95] [02:40.76] And for me, it was a real learning
[L96] [02:42.88] experience because I learned that just
[L97] [02:44.56] because it was technically excellent
[L98] [02:46.48] didn't mean it was going to win.
[L99] [02:48.80] It checked all the boxes we needed in
[L100] [02:51.08] terms of interop and type safety,
[L101] [02:54.40] but it didn't win and didn't come close
[L102] [02:56.28] to winning because there were many other
[L103] [02:57.84] factors that I didn't take into account.
[L104] [03:01.36] So, a great example of writing a lot of
[L105] [03:02.96] code and doing a lot of technical work
[L106] [03:04.88] doesn't mean that it's going to win.
[L107] [03:06.76] And you know, in this case, you drove a
[L108] [03:08.56] very ambitious project, and it did fail
[L109] [03:11.92] in the end. When it comes to performance
[L110] [03:14.32] reviews in a half where something like
[L111] [03:16.64] this is happening, or a year where
[L112] [03:18.08] something like this is happening, how
[L113] [03:19.84] does that play out? And should people be
[L114] [03:22.04] worried about, you know, their projects
[L115] [03:24.24] getting canceled or things like that?
[L116] [03:26.16] The thing that made me realize it needed
[L117] [03:27.72] to be canceled is that I got to meet
[L118] [03:29.28] some most, so performance did its job
[L119] [03:31.36] there. My manager at the time did the
[L120] [03:34.00] right thing, and was like, this is not
[L121] [03:35.28] working. He was also a new manager for
[L122] [03:38.00] me, so I think he like
[L123] [03:40.20] could see it with fresh eyes and be
[L124] [03:41.52] like, this is not going to work.
[L125] [03:43.88] And then when I did cancel it, I like to
[L126] [03:46.44] think I did it in the right way, which
[L127] [03:47.76] is there were products and features
[L128] [03:49.80] written in component script, and I
[L129] [03:51.12] helped those teams migrate back to
[L130] [03:52.68] native code or to React Native or
[L131] [03:54.32] whatever they wanted.
[L132] [03:55.96] And I completely deleted the framework.
[L133] [03:58.00] I didn't leave it as like, you know, oh,
[L134] [04:00.76] this one product is still on component
[L135] [04:02.36] script, so we have to leave it around
[L136] [04:03.32] forever, and someone will have to clean
[L137] [04:04.68] it up someday. No, I was like, I'm
[L138] [04:06.80] driving this all the way, and I'm
[L139] [04:07.84] deleting the code, it's going to be gone
[L140] [04:09.20] from the repo, which I think garnered
[L141] [04:10.92] some goodwill because it showed others,
[L142] [04:13.16] this is the right way to clean up after
[L143] [04:14.44] your mess.
[L144] [04:16.04] Um, so I feel like I got, in if
[L145] [04:17.84] anything, a positive bump after the
[L146] [04:19.48] fact, right? Like there was enough
[L147] [04:21.84] relief of like, all right, this showed
[L148] [04:23.48] people how to wind up that wind down a
[L149] [04:25.32] project that isn't working out, and you
[L150] [04:27.24] posted publicly about it, showed talking
[L151] [04:29.80] about the lessons learned, and there's
[L152] [04:31.52] no mess left behind. So, if anything, I
[L153] [04:33.64] feel like it helped in the in the
[L154] [04:35.76] immediate aftermath. So, if anyone is
[L155] [04:37.32] like staring down the barrel of like, I
[L156] [04:38.92] think my framework's not going well, but
[L157] [04:40.32] I'm afraid to kill it, you might get
[L158] [04:41.88] more goodwill from killing it
[L159] [04:43.16] responsibly than just like dragging it
[L160] [04:45.52] out and constantly waiting until it's
[L161] [04:47.64] too late.
[L162] [04:49.00] Were there signs that, like looking
[L163] [04:51.60] back, you could have maybe avoided some
[L164] [04:54.28] of the pain of, I don't know, meets
[L165] [04:56.48] most, or, you know, kind of like it
[L166] [04:58.64] going on as long as it did? Yeah, I
[L167] [05:00.88] mean, look, there were there was it was
[L168] [05:03.16] a 2-year project, and for the last year,
[L169] [05:04.80] I knew it wasn't going right. And I
[L170] [05:06.56] should have listened to my gut, right? I
[L171] [05:08.20] there were some literally sleepless
[L172] [05:09.60] nights, not a lot, but like some where I
[L173] [05:11.44] was like, this is it doesn't feel right,
[L174] [05:12.88] it's not going well, I don't understand
[L175] [05:14.32] what to do.
[L176] [05:15.44] And I'm a coding machine, so my reaction
[L177] [05:18.12] was I just need to write more code, I
[L178] [05:19.44] just need to help more features convert,
[L179] [05:21.48] and it'll suddenly take off. And I
[L180] [05:23.32] should have listened instead
[L181] [05:25.44] to that part of my gut that was telling
[L182] [05:26.80] me, this is not going to work out. Just
[L183] [05:28.36] go do something you love, and find a
[L184] [05:30.48] different way to have impact, and uh,
[L185] [05:32.84] that would have been much better for me
[L186] [05:34.28] in the short and long run.
