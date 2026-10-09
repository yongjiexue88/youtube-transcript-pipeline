# Testing Neetcode With 3 Leetcode Hards (Live Whiteboarding)
Source: source-0ff73d892aeb9a09 | Chunk 2 of 2
Video: https://www.youtube.com/watch?v=rbtO3a6Qb00
All caption text retained; paragraphs merge caption fragments without changing words.

[13:53.04–13:58.00; L339–L341] >> so you're just trying to get quick diagonal membership like given, you know, is that is that occupied or not?

[14:00.00–14:01.28; L342–L343] >> Yeah, exactly. It's just like a key value lookup.

[14:02.16–14:02.16; L344–L344] >> Yeah.

[14:02.64–14:54.32; L345–L367] >> So, um, but as you're going this way, the diagonal is different. It's like 0 + 0, 1 + 1, 2 + 2. So, okay. So I guess based on that uh I would say that if we want it to be constant the obvious thing that we can do instead of adding both of these is just taking the difference because uh we on this diagonal we chose to add them because then they would it would stay the same value along that and on this one we decide to take the difference because if we just add them it's not going to be the same. Um yeah so so the approach would work. It was just that that little trick. Um, but then other than that, it's just like a hashbased like lookup where we would um the backtracking would basically be for every single spot we either make a decision of like whether we put a queen

[14:56.40–15:03.52; L368–L371] there or we skip it. And um sometimes we'd want to skip it if we already know that there's like another queen attacking that one.

[15:04.72–15:04.72; L372–L372] >> Yeah.

[15:05.36–15:05.36; L373–L373] >> But yeah,

[15:06.00–15:11.68; L374–L376] >> I see. Okay. So you it's just brute force with a bunch of checks to make sure Okay. It's a valid step forward.

[15:14.40–15:38.80; L377–L388] >> Yeah. So, I think I don't know off the top of my head the complexity, but I'm pretty sure it'd be optimal because at each step, like each hash lookup would be constant, but in terms of like the complexity of this entire tree, um, it'd be pretty big. I don't know exactly like it might be n to the power of n, but it's definitely more than like it's definitely exponential or something.

[15:39.68–15:43.44; L389–L391] >> Yeah. Yeah, I see. Yeah, I think that would work. [laughter] Shot ad.
