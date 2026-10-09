# Why C Is a Dangerous Language | Simon Peyton Jones

Source ID: source-deae94e8883282bf
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Why_C_Is_a_Dangerous_Language_Simon_Peyton_Jones_en.txt
Video: https://www.youtube.com/watch?v=RTY2vhey-zI

[L10] [00:00.00] Then see, you program my mutation, so
[L11] [00:03.48] it's unsafe in the sense that any
[L12] [00:04.64] function can mutate any variables any
[L13] [00:06.32] time. It does a lot you you pass
[L14] [00:07.68] pointers around a lot and functions
[L15] [00:09.72] mutate the memory pointed to by those
[L16] [00:11.84] pointers. And moreover, typically they
[L17] [00:13.76] can mutate it anywhere. There's no array
[L18] [00:15.32] bounds checks or anything. So, it's kind
[L19] [00:17.80] of like super unsafe and in fact and
[L20] [00:19.16] this is demonstrated by the fact can you
[L21] [00:20.68] imagine that like all of these exploits
[L22] [00:23.36] that we get every day, right? Um
[L23] [00:26.16] that you know, MSRC is discovering in
[L24] [00:28.48] huge numbers, but but we've had you know
[L25] [00:30.80] Why is the internet so insecure?
[L26] [00:33.28] Primarily because all of our software
[L27] [00:35.04] infrastructure is written in unsafe
[L28] [00:36.24] languages. If we I mean
[L29] [00:39.16] if we'd written all of our,
[L30] [00:40.88] you know, internet software and
[L31] [00:42.64] operating systems in Haskell or maybe in
[L32] [00:44.96] OCaml or ML
[L33] [00:46.88] 99% of all these exploits would be
[L34] [00:49.24] removed by construction.
[L35] [00:52.64] Like it's like we've built a boat out of
[L36] [00:57.24] paperclips and we're surprised that it's
[L37] [00:59.12] leaky. I mean, you shouldn't build boats
[L38] [01:01.40] out of paperclips, right? Because they
[L39] [01:03.00] have a holes in them. You should build
[L40] [01:04.76] it out of a secure substance. Like but
[L41] [01:06.88] then it's too late. So, we spend
[L42] [01:09.20] incredible amounts of human ingenuity
[L43] [01:11.32] and effort patching the holes in our
[L44] [01:13.68] boat built of paperclips. It's tragic.
[L45] [01:17.12] It's tragic how much effort and
[L46] [01:19.44] ingenuity and money has been lost and
[L47] [01:21.96] waste of resources just because we wrote
[L48] [01:24.52] our
[L49] [01:25.80] you know computational infrastructure
[L50] [01:28.00] for the world in an insecure language.
[L51] [01:30.60] That's what I mean by unsafe. How many
[L52] [01:32.92] exploits are based on buffer overruns?
[L53] [01:35.88] Or you know, pointer manipulation that's
[L54] [01:37.96] gone wrong. If you couldn't have a
[L55] [01:39.96] buffer overrun, you couldn't do pointer
[L56] [01:41.36] manipulation that go wrong. Those those
[L57] [01:43.08] exploits just wouldn't exist.
[L58] [01:44.40] >> What about more modern versions of those
[L59] [01:47.76] lower-level languages?
[L60] [01:48.96] >> Oh, much much better. Much much much
[L61] [01:51.32] better, right? If we rewrote all of our
[L62] [01:53.80] software infrastructure in Rust
[L63] [01:56.00] things would be way way
[L64] [01:58.60] I I'm not actually even sure whether
[L65] [02:00.28] Rust has array bounds checks built in,
[L66] [02:02.44] but suppose it but it must have the
[L67] [02:04.20] ability to
[L68] [02:07.24] promise that you're not and actually out
[L69] [02:08.76] of bounds. I don't quite know quite know
[L70] [02:09.84] how, but if you compile all your code
[L71] [02:10.96] with that switched on,
[L72] [02:12.44] you're a way better situation. Way
[L73] [02:14.52] better.
[L74] [02:16.92] So, yes, this is not just functional
[L75] [02:18.48] programming, but you did ask about why I
[L76] [02:20.64] thought C was an insecure, unsafe
[L77] [02:22.40] language.
