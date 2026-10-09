# Is "Vibecoding" Bad for the Industry | Casey Muratori
Source: source-0a0a19a690dbea54 | Chunk 1 of 1
Video: https://www.youtube.com/watch?v=KNuBSNffSUo
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.00–00:04.76; L10–L12] Andre Karpathy had this famous tweet that kind of coined the phrase five coding.

[00:05.28–00:05.28; L13–L13] >> Yes.

[00:06.00–00:12.32; L14–L17] >> And then you said if you thought software was bad today, buckle up because it's about to get a whole lot worse.

[00:12.92–00:12.92; L18–L18] >> Yes.

[00:13.60–00:22.88; L19–L23] >> It's been about a year and a half since that tweet came out. The tweet came out February of 2025. Would you say that that was an accurate prediction?

[00:24.40–01:20.28; L24–L49] >> To be clear, I think it the whole lot worse part is predicated on something that may not happen. And that is that the idea that we just kind of type some stuff in the computer and ship it to prod, right? Basically like, "Hey, could you make me a thing and then publish it?" becomes a common way of doing things, right? For example, also done by people who maybe don't have a computer science background. I think it's fair to say and that I wouldn't be being sort of overly dismissive of AI at this point to say that a person who is well trained in computer science using an AI to make code right now can make substantially better code than someone who doesn't know anything about computer science who is just given, you know, Fable and type some thought stuff in, right? The difference is rather dramatic, I would say, from everything that I've seen.

[01:22.20–02:08.44; L50–L72] So, part part of my concern that I was trying to express in that tweet was like if the idea is like we're just going to type stuff in and we're not going to really be checking the code, you know, someone who knows computer science is not really going to be looking at it. Um worst case scenario, it's literally just like some random person in marketing somewhere who has no idea what programming is just type some stuff in and hit crosses their fingers, right? I think we're in for a world of hurt, right? Now, it's a race, so it's hard to say because it's basically a race of how good can you make the AI versus how much adoption does it get? Right? It's a curve, right? It's like if you can make the AI good enough that the people who are adopting it at a particular rate are always using an AI that's good enough for what

[02:09.96–02:41.52; L73–L90] they're adopting it for, we wouldn't expect software to get significantly worse. If those curves go the other way, we're in a lot of trouble, right? So, we're I feel like right now we're we're almost kind of teetering on this knife's edge. It's it's really to me it feels like a foot race of like improving AI so it can be more autonomous and make better decisions without your without you needing to make them for it versus the capability level of people who are using it and the degree to which they're paying attention to its output. It's like these two curves that are just like you know, like what's

[02:42.44–02:42.44; L91–L91] >> [laughter]

[02:42.84–03:37.32; L92–L116] >> what's going to happen? I don't have a prediction. I don't know where we'll be in a year. Obviously, for all of our sake, I'm hoping that the AI curve wins because I agree like I understand certainly the perspective of people who maybe just don't like AI and don't want there to be AI. I can understand the wanting it to fail. I I understand that, right? Um and I'm no fan of AI myself, so it's not like I like I'm going to criticize someone for taking that position. But at the end of the day, if you're talking about something that tons of people are using, you're going to kind of want it to be good. Like I think at this point, given the level of adoption of AI, I really don't think it's would be great if it stopped getting any better right now. Like if this was as good as it was going to get, I think that might be bad.

[03:39.48–04:09.36; L117–L130] Um certainly 6 months ago, I think that was true. Uh and I think it's probably still true today. So, I think ideally, if you want software to not be terrible, you have to kind of still be hoping that 6 months from now the AIs are again significantly better than they were, right? Like that that is the only way out of the current situation as I see it, right? Uh I don't know if that's fair, but that's my that's my sort of feeling on that.

[04:10.32–04:17.44; L131–L134] >> One of your other top tweets, it was, you know, Shopify put out this internal memo and you just, you know, you replied, you know, "Slopify."

[04:19.36–04:19.36; L135–L135] >> Yes. [laughter]

[04:19.92–04:26.88; L136–L139] >> I guess it's cuz in this tweet it's leadership pushing the adoption curve maybe harder than the capabilities of the AI in this case.

[04:28.52–05:11.24; L140–L162] >> Yeah, although I also just like the pun. One of the things that I think is most unfortunate about the AI adoption as I've seen it is just the because people think that it's going to be this major um I guess if I had to categorize the way it appears that companies are reasoning about it, they're assuming that if they don't get in early, it will be a big disaster for them, right? Like like there's a tremendous like they don't just think, "Oh, well, we can just wait until the AI does what we need it to do and then start using it." They're like, "No, we have to do it now, like even before we know whether it can really do the thing that we want it to do or whether we know whether the outcomes will be good. Everyone has to do it right now. Let's do this, right?" Um and I understand why they want why

[05:13.48–06:00.56; L163–L187] why they're going about that way because they think that that that is critical, right? They obviously believe that's very important. Um and to me, that's just that's just kind of terrifying because as with any technology, the sane way to do it is to measure its capabilities, see how well it is able to solve problems that you have, see if it solves them faster than the way that you were do doing it, and a put it into a workflow at such a time as you've determined that it is a net positive. That's just the same like that's the what you would do with any technology, right? And you'd probably have like your team of people whose job it is to assess this thing and they're out there yolo swagging it, right? They've got 3,000 agents working on this cluster talking to each other doing, you know, God knows what, right? And uh So, there's going to be that and

[06:02.20–06:58.20; L188–L213] someone's going to be doing that, but that is should not be every org, right? Like you wouldn't just be like everyone needs to use a ton of tokens, right? Um So, yeah, like I I do have concerns about that. I don't think that that the way AI adoption was done was was the best way for quality in software. But, I would temper that statement with just the obvious fact that like we were not exactly a five-nines uh industry to start out with. Like software quality was really pretty low rolling into the AI era. So, I always try to just also caveat most of the things that I have to say that might be critical of a particular thing happening AI with just the fact that like look, it wasn't particularly great beforehand, either. Uh a lot of the software was pretty low quality and so you can't some AI things may may make things worse, but it's not like software was

[07:00.32–07:05.44; L214–L217] amazing and the AI showed up and ruined everything. That is a completely ridiculous narrative that that is not true at all.
