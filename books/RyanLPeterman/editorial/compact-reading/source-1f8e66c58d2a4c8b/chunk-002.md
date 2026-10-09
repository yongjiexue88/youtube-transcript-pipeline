# AWS to Dropbox: The Largest Ever Data Migration In History | James Cowling
Source: source-1f8e66c58d2a4c8b | Chunk 2 of 2
Video: https://www.youtube.com/watch?v=Ar84Ow4l2XE
All caption text retained; paragraphs merge caption fragments without changing words.

[12:06.72–12:52.64; L377–L401] a process called I think it's called FMEA, which is like a threat modeling process where you had a big spreadsheet and you kind of write down every bad thing that could possibly happen and then, you know, all the how bad it would be if it happened. Existential risk to someone die, you know, if there's a fire in the data center. All these kind of things get put into the spreadsheet. And you kind of do a bit of a almost pre-mortem kind of a work to figure out all the all the potential failure modes and then design around them. And I that's I love that work. I I really um I don't know. I do like the firefight. I I like the I don't I can't say I like getting paged because I've spent my whole life on call, but I do like that rubber hits the road stuff. I like that wow, there's congestion collapse and and

[12:54.36–12:58.12; L402–L404] there's no one that can help you. And so you've got to think through this problem.

[12:59.72–13:25.84; L405–L416] >> When I worked on infrastructure at Instagram, we had this concept of DEFCON knobs, which are basically these configs that you could flip that would gracefully degrade your system where you can still operate it, but you know, maybe in the case of Dropbox, you store less replicas. So, you take on a temporary increase of risk in losing data because you need to. Did you have something like that and did you flip it in that type of case?

[13:27.88–14:18.56; L417–L440] >> Never when it came to durability. So, I mean, we just had an just absolute zero non-negotiable like there was no room for negotiation on on users' durability. And so, um we had those knobs for background processes for CPU and and memory, for example. So, if there was like a spike in load, you could turn off background processes and and turn off um you know, um the the test load, for example, on the system. Eventually, we we built this system called trampoline. And what trampoline did was um which actually was a it it saved us a ton of money, right? When if we ever got too close to the threshold, we would just start writing data to S3. Cuz it's right there, right? So, it's um you can run your capacity way closer to the edge if you're willing under worst-case scenarios just to just to dump 30 petabytes on S3 and then move it

[14:21.36–14:32.84; L441–L447] back when it's done. And now, it did it didn't happen very often. We would do it to test it. We would do that just to make sure the system worked. But, um yeah, being able to have a escape hatch for worst-case scenario was really nice.

[14:34.00–14:36.20; L448–L449] >> I see. So, S3 is kind of um it's like elastic storage.

[14:37.88–14:37.88; L450–L450] >> Exactly.
