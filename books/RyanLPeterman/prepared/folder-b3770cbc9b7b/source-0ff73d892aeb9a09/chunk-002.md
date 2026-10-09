Chunk 2; segments 330–382. Start may repeat the previous chunk for context.

# Testing Neetcode With 3 Leetcode Hards (Live Whiteboarding)

Source ID: source-0ff73d892aeb9a09
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Testing_Neetcode_With_3_Leetcode_Hards_(Live_Whiteboarding)_en.txt
Video: https://www.youtube.com/watch?v=rbtO3a6Qb00

[L339] [13:53.04] >> so you're just trying to get quick
[L340] [13:55.04] diagonal membership like given, you
[L341] [13:58.00] know, is that is that occupied or not?
[L342] [14:00.00] >> Yeah, exactly. It's just like a key
[L343] [14:01.28] value lookup.
[L344] [14:02.16] >> Yeah.
[L345] [14:02.64] >> So,
[L346] [14:04.64] um,
[L347] [14:06.16] but as you're going this way, the
[L348] [14:07.92] diagonal is different. It's like 0 + 0,
[L349] [14:11.68] 1 + 1, 2 + 2.
[L350] [14:15.60] So, okay. So I guess based on that uh I
[L351] [14:19.52] would say that if we want it to be
[L352] [14:21.12] constant the obvious thing that we can
[L353] [14:23.20] do instead of adding both of these is
[L354] [14:25.20] just taking the difference because uh we
[L355] [14:28.96] on this diagonal we chose to add them
[L356] [14:30.80] because then they would it would stay
[L357] [14:32.00] the same value along that and on this
[L358] [14:33.68] one we decide to take the difference
[L359] [14:36.16] because if we just add them it's not
[L360] [14:37.76] going to be the same. Um yeah so so the
[L361] [14:41.36] approach would work. It was just that
[L362] [14:42.64] that little trick. Um, but then other
[L363] [14:46.56] than that, it's just like a hashbased
[L364] [14:48.00] like lookup where we would um the
[L365] [14:50.64] backtracking would basically be for
[L366] [14:52.24] every single spot we either make a
[L367] [14:54.32] decision of like whether we put a queen
[L368] [14:56.40] there or we skip it. And um sometimes
[L369] [15:00.32] we'd want to skip it if we already know
[L370] [15:02.24] that there's like another queen
[L371] [15:03.52] attacking that one.
[L372] [15:04.72] >> Yeah.
[L373] [15:05.36] >> But yeah,
[L374] [15:06.00] >> I see. Okay. So you it's just brute
[L375] [15:09.04] force with a bunch of checks to make
[L376] [15:11.68] sure Okay. It's a valid step forward.
[L377] [15:14.40] >> Yeah. So, I think I don't know off the
[L378] [15:16.64] top of my head the complexity, but I'm
[L379] [15:18.72] pretty sure it'd be optimal because at
[L380] [15:20.56] each step, like each hash lookup would
[L381] [15:22.32] be constant, but in terms of like the
[L382] [15:24.16] complexity of this entire tree,
[L383] [15:27.04] um,
[L384] [15:29.44] it'd be pretty big. I don't know exactly
[L385] [15:32.32] like it might be n to the power of n,
[L386] [15:34.24] but it's definitely more than like
[L387] [15:36.96] it's definitely exponential or
[L388] [15:38.80] something.
[L389] [15:39.68] >> Yeah. Yeah, I see. Yeah, I think that
[L390] [15:41.92] would work. [laughter]
[L391] [15:43.44] Shot ad.
