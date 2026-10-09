# The Co-Creator of Kubernetes: Engineering-Led Direction and Convincing Management | Brendan Burns
Source: source-176a06af7f6bc865 | Chunk 1 of 6
Video: https://www.youtube.com/watch?v=FKijpCEH9D8
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.00–00:03.92; L10–L12] There's going to be an open source one. Do you want it to be ours or do you want it to be someone else's?

[00:05.56–00:11.48; L13–L16] >> This is Brendan [music] Burns, the co-creator of Kubernetes, and I asked him about the stories behind building it. [music]

[00:11.84–00:13.76; L17–L18] >> The hardest part actually of the project was actually articulating that.

[00:15.96–00:18.92; L19–L20] >> How long did that initial MVP take to build?

[00:19.64–00:20.76; L21–L22] >> I don't know, a little under a week, maybe.

[00:21.52–00:23.40; L23–L24] >> He had interesting career advice grounded in his career story.

[00:25.24–00:27.84; L25–L26] >> I believe you can hide order 10% of your effort from your management.

[00:29.96–00:31.56; L27–L28] >> Is there any upper bound where Kubernetes just cannot handle that load?

[00:34.40–00:35.68; L29–L30] >> Every time you change an order of magnitude, the problem moves.

[00:37.68–01:09.24; L31–L44] >> Here's the full episode. I mean, let's start with Kubernetes cuz that's super interesting. I don't I don't fully understand the business motivation. Like, let's say I was your director or something like that and you you came to me with this and you said, "Hey, let's let's do this for everyone." I don't fully understand what would be in that strategy doc or that What would you say in that meeting that would say, "Here's the impact for Google if we invest in building this for the the industry?"

[01:09.96–02:02.88; L45–L71] >> Yeah, it's funny cuz like the hardest part actually of the project I would say that in those early days was actually articulating that. Um and I think it was really clear in our heads, but like figuring out how to convince people um uh was tricky. Um and you know, I think there was there were a variety of different ways that we articulated why it was important. Um one of them was uh related to the uh MapReduce white paper. Right? So, MapReduce at the time, especially like Hadoop and big data were were were a big deal. I think that, you know, other things have kind of replaced them at this point, but like MapReduce was a big deal. Um and the the big data revolution or whatever they called it. Um and you know, Google had written the original white paper. Um but Hadoop was an open source project that Google had nothing to do with.

[02:05.52–02:50.80; L72–L95] And got no credit for it. And and and they just read the white paper and they re-implemented it and it's not the same. It's similar, but it's not the same, right? Because anytime you re-implement something, it's not the same. And so part of the argument was like, "Look, like we have this cloud and we want to like be influencing the technology technological landscape if all we do is kick out white papers, we're not like if it doesn't run, if it's not something that people can run, they're not we're not going to be in the driver's seat. Um and so that was one of the one of the one of the arguments. I think, you know, the other couple arguments were like, "Why containers? Why not why why not you know, people are using VMs, why containers?" And you know, a lot of that was talking about like, "Look, the demands of writing software and we

[02:53.04–03:40.08; L96–L122] know internally, we know from doing this internally that the demands of writing reliable software necessitate having systems that are sort of like autopilots for your um you know, for your application. And and we know that this is something that as software becomes more and more critical to more and more businesses, this is something that you they're just going to have to have, right? And so that's sort of the why containers part. Um and then you know, I think that the third part was the like why open source, right? And in some sense, that's like the most interesting conversation because people are like, "Wow, this would be you know, you've convinced me, right? Like you've convinced me we should build it, we should make it available to the world. It's something that they're going to find useful. Um but wouldn't it be so much better if they could only use it on our platform?" And you're like, "Yeah, that's

[03:40.84–03:46.04; L123–L126] absolutely the case, but you can't win if you make it only on your platform."

[03:47.84–03:47.84; L127–L127] >> Well, why is that?

[03:49.44–04:37.16; L128–L152] >> Well, because there's other platforms out there, right? And so, if you make it an exclusive, then the people who for other reasons are on other clouds or on on-premise, they're shut out. And so, they're going to just go build an alternative. Right? Like the like the the open source the it's it's sort of like a Linux, you know, uh the reason Linux won, right? It's because Linux could go anywhere. Right? The whole reason that open tech and open ecosystems win is because you the majority of people are going to be not on your plat like if you're if you're not the leader, and we and you know, GCP was not the leader, then the majority of people are not going to be on your platform. And so, if you make it such that the majority of people can't use your thing, they're just going to ignore you, and then they're going to go build their

[04:38.08–05:24.48; L153–L180] own. Right? Whereas, if you go and build it and you build it for everybody, but you make sure that it's awesome on your platform, then you have a chance of attracting people attracting more people to your platform, uh than otherwise. And and then I mean, also in some ways it's just like the aesthetic of the time, also, right? It's like if everybody's using Linux, and everybody's using Docker, and everybody's using these programming languages that are all open, like if everything else is open source, you don't want to be the thing that's not. Right? And and there's only a few places where like where that hasn't been true historically in technology, where you could be different and still succeed, and you have to be so differentiated that and I don't think that we were different that differentiated. You have to be so differentiated such that people are like, "Oh, actually, I want that thing so bad, I don't care that it's

[05:26.12–05:26.12; L181–L181] closed."

[05:26.96–06:00.28; L182–L195] >> So, at the time just thinking what was the competitive landscape, I guess if I if I remember, it was I mean, AWS was dominant. They were there first and doing very well. GCP at that time probably an up-and-coming company uh or I guess offering. And so, am I understanding then that the idea is let's pull market share away by giving kind of open source distributing Kubernetes to more and more developers and then they'll be more open to kind of migrating or using GCP because you'll make a

[06:00.96–06:47.12; L196–L221] >> They'll pay attention. Right, they'll pay attention. And also like you change the dialogue too, right? Like tail light chasing is hard. Right? Like if if someone else has built VMs and everybody's using VMs and all you're doing is saying like, "Well, we're building the same thing that they have only maybe it's a little bit better because we do something else over here or you know, whatever." Like that's a hard market strategy to articulate. But if you create a brand new playing field where you are the thought leader um suddenly like people are listening to you. Even if they're not using it on your platform, they're listening to you and that gives you way more voice. You get you get a lot more voice in the market. It changes the narrative. It changes who people are listening to. Um and so that control of of the story is an important aspect of of of how I think how you

[06:49.24–07:09.88; L222–L234] break through that or you try to break through that dynamic. Obviously, like you know, they're still in third at this point. So like didn't work out, but um I mean, I wouldn't say it didn't work out. I think it worked out in general, but it's still hard. Like overcoming those kinds of market dynamics is hard and you know, I think the other thing that happened is everybody in the cloud consolidated around it and so now Kubernetes is just sort of a utility everywhere.

[07:12.32–07:42.64; L235–L249] >> You you mentioned that I guess that perception benefit of being at the dominant offering. Um which I mean, if you if you look at what happened in hindsight, it makes a lot of sense. I mean, that is what happened and it's it's uh a wonderful benefit. But I guess when you were looking forward and you were talking to leadership were you cognizant of those benefits and saying, "We need to do this because we're going to kind of become the dominant offering and it's going to have all these uh optics benefits.

[07:44.88–07:55.84; L250–L256] >> I mean, I think we absolutely wanted to make sure that we were front and center in terms of thought leadership and we definitely articulated that. Right? Absolutely right. Like being being in a thought leadership position is value is valuable.

[07:56.96–08:02.88; L257–L260] >> It's interesting cuz um I feel like it's hard to quantify. I mean, if I was in that meeting and we're trying to make a call

[08:03.76–08:03.76; L261–L261] >> Yeah, yeah, yeah.

[08:04.32–08:04.32; L262–L262] >> how much is that worth?

[08:06.08–08:48.84; L263–L286] >> Yeah. Well, I think you have to also realize that at the time like it was pretty cheap, right? It was like eight or nine engineers. And and we kind of and this is in some sense I mean it's both a blessing and a curse. Like part of the reason why we articulated and argued for having such a distinct brand where the Kubernetes brand was separated from the Google brand um was that it kind of gave us freedom to fail also. It was like, "Hey, if these eight people go off and you know, do something and and it turns out to be stupid, like we'll just kill it off and it won't have like it won't you know, it won't um it won't damage the broader perception of the cloud. And so I think there's there's that benefit of the open source part of it, too. Um it helped with adoption, right? Like it helped

[08:50.28–09:24.12; L287–L304] it helped us and especially as we went to like the Linux Foundation and things like that and truly established like an independent entity, it helped ensure that you know, people like Red Hat or Azure or AWS could take a bet on Kubernetes and feel confident in that bet. Um but it also was an insurance policy against failure. And and also to be honest like it was it it simplified a lot of things, too, because you know, we were competing against startups, right? Like at the time Docker is a startup. They can be way more agile than a big company and so by virtue of sort of like being a separate entity uh we could be a little bit more agile, also.

[09:26.08–09:30.84; L305–L307] >> I mean, the earliest conception of this project was you and two others kind of hacking something together.

[09:32.40–09:38.44; L308–L312] >> Yeah, it was a demo. I mean, it was sort of a demo almost. It was like, "Look look what we can do if we just smash a bunch of existing open source tech together.

[09:39.44–09:39.44; L313–L313] >> Well, what did that demo do?

[09:42.00–10:20.32; L314–L336] >> Uh I mean, it was basically like a basic cube control. It was like, "Hey, here's like here's a container I built." I mean, at the time you had to explain Docker to people. You were like, "Hey, here's Docker. I used it to like build this container image." Um and and then you could run it and deploy it and see that it had gotten distributed across a bunch of machines and that you could, you know, load balance to it cuz you you'd hit a single endpoint and it would go, "I'm replica one." And then you'd hit reload and go, "I'm replica three." And, you know, so it like showed that it was replicated and then um basic health checking. So, like if you killed it, it would come back and uh a V2 to V or a V1 to V2 upgrade. That was about it.

[10:21.12–10:24.40; L337–L338] >> How How long did that that initial MVP take to build?

[10:25.92–10:34.56; L339–L344] >> Uh I wrote it in, I don't know, a little under a week, maybe. Something like that. I mean, like I don't don't work on the weekends, so maybe 5 days, 4 days, 5 days.

[10:35.76–10:44.20; L345–L349] >> Did And did you drop all of your existing work? Cuz I'm imagining your you had existing project work and this is kind of extra credit stuff that you were working on.

[10:45.60–11:28.04; L350–L371] >> Yeah, well, I mean, I wouldn't say I I dropped it, but like in in a time scale of that time scale, like you can kind of like slack on it a little bit. You know, like like you could be sick for a week. I mean, I guess the thing is like you could be sick for a week, you know? And I'm not saying that I That's not what we did. That's not what I did, but like but but there was enough flexibility in in the system that like you could hack it together. Um And I mean, believe me, it was hacked together, right? Like every possible shortcut to take and every And, you know, I think one of the things I've been good at historically is um integrating other open source projects together, seeing how you can take stuff off the shelf and put it together. And so, you know, a lot of the nuts and bolts were

[11:31.76–11:42.00; L372–L377] pieces that we could take from other open-source projects and um and kind of combine together with a little with glue and glue code to they'll you know to to give the feel of it. So, that helps, too.

[11:43.56–11:56.44; L378–L384] >> I think a lot of software engineers when they hear this kind of story, they think, "Oh, I have my existing responsibilities and I can't necessarily go off and build this thing, even though I think it's a great idea." Do you have any advice for someone who has that
