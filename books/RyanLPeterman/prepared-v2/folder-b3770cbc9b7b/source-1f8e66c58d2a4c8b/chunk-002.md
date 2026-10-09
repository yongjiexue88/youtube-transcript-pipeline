Chunk 2; segments 368–441. Start may repeat the previous chunk for context.

# AWS to Dropbox: The Largest Ever Data Migration In History | James Cowling

Source ID: source-1f8e66c58d2a4c8b
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/AWS_to_Dropbox_The_Largest_Ever_Data_Migration_In_History_James_Cowling_en.txt
Video: https://www.youtube.com/watch?v=Ar84Ow4l2XE

[L377] [12:06.72] a process called I think it's called
[L378] [12:07.88] FMEA,
[L379] [12:09.44] which is like a threat modeling process
[L380] [12:11.08] where you had a big spreadsheet and you
[L381] [12:12.68] kind of write down every bad thing that
[L382] [12:15.04] could possibly happen and then, you
[L383] [12:16.76] know, all the how bad it would be if it
[L384] [12:18.92] happened.
[L385] [12:20.16] Existential risk
[L386] [12:22.16] to someone die, you know, if there's a
[L387] [12:23.48] fire in the data center. All these kind
[L388] [12:24.84] of things get put into the spreadsheet.
[L389] [12:26.72] And you kind of do a bit of a almost
[L390] [12:28.64] pre-mortem kind of a work to figure out
[L391] [12:31.28] all the all the potential failure modes
[L392] [12:33.36] and then design around them. And I
[L393] [12:35.20] that's I love that work. I I really um
[L394] [12:38.84] I don't know. I do like the firefight. I
[L395] [12:40.68] I like the
[L396] [12:42.48] I don't I can't say I like getting paged
[L397] [12:44.16] because
[L398] [12:45.52] I've spent my whole life on call,
[L399] [12:47.64] but I do like that rubber hits the road
[L400] [12:50.08] stuff. I like that
[L401] [12:52.64] wow, there's congestion collapse and and
[L402] [12:54.36] there's no one that can help you. And so
[L403] [12:56.72] you've got to
[L404] [12:58.12] think through this problem.
[L405] [12:59.72] >> When I worked on infrastructure at
[L406] [13:01.12] Instagram, we had this concept of DEFCON
[L407] [13:03.16] knobs, which are basically these configs
[L408] [13:06.60] that you could flip that would
[L409] [13:08.68] gracefully degrade your system where you
[L410] [13:11.36] can still operate it, but you know,
[L411] [13:13.32] maybe in the case of Dropbox, you store
[L412] [13:15.96] less replicas. So, you take on a
[L413] [13:18.48] temporary increase of
[L414] [13:21.12] risk in losing data because you need to.
[L415] [13:24.40] Did you have something like that and did
[L416] [13:25.84] you flip it in that type of case?
[L417] [13:27.88] >> Never when it came to durability. So, I
[L418] [13:30.32] mean, we just had an just absolute zero
[L419] [13:33.20] non-negotiable like there was no room
[L420] [13:35.20] for negotiation on on users' durability.
[L421] [13:37.84] And so, um
[L422] [13:39.64] we had those knobs for background
[L423] [13:41.04] processes for CPU and and memory, for
[L424] [13:42.92] example. So, if there was like a spike
[L425] [13:44.32] in load, you could turn off background
[L426] [13:46.44] processes and and turn off um you know,
[L427] [13:49.12] um the the test load, for example, on
[L428] [13:51.16] the system. Eventually, we we built this
[L429] [13:53.48] system called
[L430] [13:55.96] trampoline.
[L431] [13:57.24] And what trampoline did was um which
[L432] [14:00.08] actually was a it it saved us a ton of
[L433] [14:01.92] money, right? When if we ever got too
[L434] [14:04.72] close to the threshold, we would just
[L435] [14:06.72] start writing data to S3.
[L436] [14:08.68] Cuz it's right there, right? So, it's um
[L437] [14:11.60] you can run your capacity way closer to
[L438] [14:14.12] the edge if you're willing under
[L439] [14:16.12] worst-case scenarios just to just to
[L440] [14:18.56] dump 30 petabytes on S3 and then move it
[L441] [14:21.36] back when it's done. And now, it did it
[L442] [14:23.52] didn't happen very often. We would do it
[L443] [14:24.96] to test it. We would do that just to
[L444] [14:26.20] make sure the system worked.
[L445] [14:27.92] But, um yeah, being able to have a
[L446] [14:30.52] escape hatch for worst-case scenario was
[L447] [14:32.84] really nice.
[L448] [14:34.00] >> I see. So, S3 is kind of um
[L449] [14:36.20] it's like elastic storage.
[L450] [14:37.88] >> Exactly.
