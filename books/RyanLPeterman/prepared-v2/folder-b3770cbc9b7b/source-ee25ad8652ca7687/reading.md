# Bjarne Stroustrup (Creator of C++) On Why C++ Is Faster Than C

Source ID: source-ee25ad8652ca7687
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Bjarne_Stroustrup_(Creator_of_C++)_On_Why_C++_Is_Faster_Than_C_en.txt
Video: https://www.youtube.com/watch?v=htY1IFhrGGc

[L10] [00:00.00] Generally with programming languages,
[L11] [00:02.24] there's this
[L12] [00:04.00] you know, high-level intuition that the
[L13] [00:06.16] closer to the machine you are, the
[L14] [00:08.32] higher the performance is. And um, you
[L15] [00:11.52] know, I I tend to see C as closer to the
[L16] [00:14.84] machine than C++ for instance. Um, you
[L17] [00:18.44] know, that's not the case.
[L18] [00:19.52] >> It's not the case. It's not as good as
[L19] [00:21.68] compile time calculation as C++ is. And
[L20] [00:26.04] anyway, we have exactly the same machine
[L21] [00:28.28] model because
[L22] [00:31.20] C borrowed the C++ 11 machine model.
[L23] [00:35.24] Um, so
[L24] [00:37.12] if you write the same code in both
[L25] [00:39.04] languages, it's
[L26] [00:40.72] you get the same result. Except the C++
[L27] [00:44.64] compilers can do more at compile time.
[L28] [00:48.64] And so C++ runs as fast or faster than C
[L29] [00:53.40] in most cases.
[L30] [00:55.28] There's more information.
[L31] [00:57.32] If if if you give the
[L32] [00:59.40] optimizer some more information, it can
[L33] [01:01.36] do a better job.
[L34] [01:02.64] >> Ah, okay. Yeah, cuz that was what I was
[L35] [01:04.80] going to ask you was
[L36] [01:06.48] you had said somewhere that C++ can be
[L37] [01:09.24] more performant than C, but I tend to
[L38] [01:12.12] think that more abstraction costs you
[L39] [01:14.12] something.
[L40] [01:14.76] >> It's compiled away. This is why I talk
[L41] [01:17.36] about zero overhead abstraction.
[L42] [01:20.16] And people are beginning to take me to
[L43] [01:22.68] task for that because that's
[L44] [01:25.04] underestimating the and understating the
[L45] [01:28.60] ability of the C++ plus compiler. We can
[L46] [01:31.68] do negative overhead uh, abstraction.
[L47] [01:36.20] >> What if I was really good at writing
[L48] [01:38.48] assembly and I had all the time in the
[L49] [01:40.48] world to write it? Could that How about
[L50] [01:42.96] How does that compare?
[L51] [01:44.56] >> If you are very smart
[L52] [01:47.20] and you have infinite time,
[L53] [01:49.52] uh, you can do better.
[L54] [01:52.00] Um,
[L55] [01:53.16] by and large, we are not as smart as the
[L56] [01:57.20] optimizers anymore.
[L57] [01:59.40] And we don't have infinite time.
[L58] [02:02.16] So, if we are
[L59] [02:03.88] smart enough, we can only do a small
[L60] [02:06.44] piece of code.
[L61] [02:08.08] And now
[L62] [02:09.92] the question is did we get
[L63] [02:12.28] enough time to use our smarts?
[L64] [02:15.36] Uh
[L65] [02:16.92] this is even starting to affect
[L66] [02:20.44] uh clever code.
[L67] [02:23.12] I gave a talk to
[L68] [02:25.52] uh Slack last year, which is the group
[L69] [02:27.72] of
[L70] [02:28.80] very performant interested people from
[L71] [02:32.48] the finance industry.
[L72] [02:34.76] And my title was don't be clever.
[L73] [02:39.28] Actually, the written title was don't be
[L74] [02:41.24] too clever, but I can't pronounce
[L75] [02:43.08] parentheses.
[L76] [02:44.88] Um
[L77] [02:46.36] and I got out alive.
[L78] [02:48.80] Um and my main point was that C++ is
[L79] [02:52.96] good enough
[L80] [02:54.84] for
[L81] [02:56.00] uh more than 98% of your code.
[L82] [02:59.04] So, if you want time to be clever,
[L83] [03:02.28] you use these techniques that I showed
[L84] [03:04.24] modern C++.
[L85] [03:06.52] And that way you get time so you can do
[L86] [03:09.48] all the clever optimizations. The
[L87] [03:11.48] problem is clever optimizations these
[L88] [03:13.92] days tend to be machine dependent.
[L89] [03:17.36] That is, if you get a new
[L90] [03:20.96] computer or if you get a new version of
[L91] [03:23.76] the compiler, you might actually have
[L92] [03:26.16] pessimized your code. I've seen this
[L93] [03:29.00] repeatedly ever since the
[L94] [03:31.80] uh the ages.
[L95] [03:33.64] Uh
[L96] [03:34.52] and there there there there's people who
[L97] [03:36.92] does nothing but uh
[L98] [03:39.12] um
[L99] [03:40.16] using different optimizations on the
[L100] [03:42.52] next generation hardware.
[L101] [03:45.12] And um my standard techniques for
[L102] [03:49.28] um
[L103] [03:49.92] for for improving things
[L104] [03:52.72] actually is to first throw away the
[L105] [03:54.88] clever stuff.
[L106] [03:57.04] And then see if you run fast or slow.
[L107] [04:01.16] Usually you run faster. Because clever
[L108] [04:03.80] stuff tend
[L109] [04:05.56] at least 9090s
[L110] [04:07.92] store style clever stuff, which is
[L111] [04:09.76] there's a lot of it still today.
[L112] [04:12.36] Because the techniques carry on in
[L113] [04:15.00] people's heads and
[L114] [04:17.64] some of the code remains.
[L115] [04:20.00] Uh tend to use a richness of pointers.
[L116] [04:23.52] And that
[L117] [04:24.92] gives the compilers and optimizers
[L118] [04:27.64] problems.
[L119] [04:29.52] They also sometimes use
[L120] [04:32.28] more allocations.
[L121] [04:34.32] Which is not good. You want to minimize
[L122] [04:36.48] memory access. You want to
[L123] [04:38.92] maximize your cache performance and
[L124] [04:42.72] things like that.
[L125] [04:44.16] And compilers are getting very good at
[L126] [04:46.12] that.
[L127] [04:47.60] And I have seen
[L128] [04:49.32] this kind of thinking. I wrote a paper
[L129] [04:52.44] about it together with a friend of mine
[L130] [04:54.32] in Spain doing fluid dynamics.
[L131] [04:58.08] And uh
[L132] [04:59.76] uh we we we threw away
[L133] [05:02.20] uh the clever stuff for a
[L134] [05:04.68] uh
[L135] [05:05.84] uh
[L136] [05:07.12] actually a performance uh
[L137] [05:09.92] test suite example. So it was not toy.
[L138] [05:14.16] And we got only 20% improvement.
[L139] [05:17.84] You know,
[L140] [05:18.68] by reducing the code to about 80% of uh
[L141] [05:22.24] what it was before.
[L142] [05:24.16] And so some people didn't think that was
[L143] [05:27.20] significant. I thought it was a
[L144] [05:29.24] significant proof that the technique was
[L145] [05:31.96] appropriate. You apply optimizations
[L146] [05:35.20] only when you need them.
[L147] [05:37.84] Knuth says don't do premature
[L148] [05:40.08] optimization. But he also pointed out
[L149] [05:42.64] that 2 to 3% is where you
[L150] [05:45.92] uh where you stop optimize. Which is
[L151] [05:47.92] exactly the number I'm using.
[L152] [05:51.48] And so, first build the stuff
[L153] [05:54.76] using high-level facilities,
[L154] [05:57.40] see if it's good enough, and if it isn't
[L155] [06:00.36] uh, and you have to time it. You don't
[L156] [06:03.00] guess, you time. Uh, then you
[L157] [06:06.64] uh,
[L158] [06:07.64] then you figure out where the time is
[L159] [06:09.40] spent, and then you optimize that.
[L160] [06:12.28] But, a lot of the time you don't need to
[L161] [06:14.72] go to that stage. It's It's fast enough.
[L162] [06:18.16] >> I see. So, when you say cleverness here,
[L163] [06:20.28] it's uh, like human-level uh, manual
[L164] [06:23.60] management that eke out performance.
[L165] [06:25.84] Yes. And you're saying that actually, if
[L166] [06:28.60] you don't do that, the compiler you're
[L167] [06:30.28] giving the compiler more to optimize,
[L168] [06:32.48] and they can do a good job.
[L169] [06:34.16] >> It's and it's much much better than it
[L170] [06:36.12] used to be. Code that was cleverly and
[L171] [06:39.80] correctly optimized in 1990s
[L172] [06:43.88] are often pessimized today
[L173] [06:47.68] because machine architectures have
[L174] [06:49.60] changed.
[L175] [06:51.24] And the compilers have improved.
