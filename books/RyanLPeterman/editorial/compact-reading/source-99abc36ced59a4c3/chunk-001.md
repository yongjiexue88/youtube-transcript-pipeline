# Instagram Principal Eng (IC8) On Why He Accepts Broken Code
Source: source-99abc36ced59a4c3 | Chunk 1 of 1
Video: https://www.youtube.com/watch?v=836CauoVekQ
All caption text retained; paragraphs merge caption fragments without changing words.

[00:00.08–00:01.76; L10–L11] Even if I see your diff is going to blow up production.

[00:03.60–00:38.96; L12–L31] >> I will I will comment on it and be like this is going to blow up production and then accept it and be like, "Yeah, make sure you fix that first, right?" I've never had a case where someone's like landed it cuz like people put up diffs and like 5 minutes later it's like stamp on me and they're like, "What the hell is going on?" [laughter] And that's a lot cuz I'm on top of it. But also because I have this philosophy on like diff reviews and risk where if I don't think the diff is risky, right? You're getting a very rudimentary review and like basically you can put that code in like so if it's like gated, it's not on a core system, right? These things then you're going to just get a very high level diff and then basically I'm just like trusting you.

[00:39.92–00:44.64; L32–L34] >> So you're saying you you modulate your level of time investment based on how risky the diff is

[00:46.40–00:59.52; L35–L42] >> based on how risky the diff is, right? So if you're rewriting it, right, we're it it's all gated right now and we just want the highle trunk architecture to be correct. If you're working on like some child component or something, it's like cool, it's gated. It's not critical to the system. Like

[01:01.20–01:03.28; L43–L44] >> yeah, I'm trusting you to do whatever you need to do over there.

[01:04.32–01:06.48; L45–L46] >> So you'll just stamp it stamp stamp it let it. Yeah.

[01:07.60–01:45.28; L47–L64] >> Some people view quality different view as a uh like an important thing rather than just stamping. So do you ever get push back on? This is my controversial one for sure. So yeah, so I I think that is correct for like the the trunk of the system, the core core parts of the system or anything that's already live in prod like is going to get pretty thorough review. Yeah, if it's not live and prod and it is one of these sub like sub parts of the system or less critical things like I'll still skim it to make sure you didn't do anything like absolutely crazy like introduce like I don't know security issues or you know start mining crypto on our servers or something

[01:46.08–01:49.76; L65–L66] >> but uh yeah I'll just like let let that let that fly in.

[01:51.12–02:01.84; L67–L71] >> Yeah, I I mean it makes sense. So you're basically trading off speed for I guess quality, but it's not dumb quality. It's like these are places where it makes sense to make the trade-off

[02:03.20–02:12.24; L72–L77] >> where you make Yeah. So you can have like lower quality components for like these the child the child parts of the system, right? Or the leaf parts of the system. And also these parts are like generally easier to unit test.

[02:14.40–02:16.24; L78–L79] >> If they do fail, they only blow up like a small part of it, right?

[02:18.48–02:18.48; L80–L80] >> Just a little blow up.

[02:19.52–02:29.60; L81–L86] >> Just a little part of it. If it is badly architected, it's only on this like tiny part of the system. It's not impacting, you know, hundreds of engineers. Maybe it impacts a couple and someone one day is like, "What the hell's up with this?"

[02:31.60–02:33.04; L87–L88] >> Doesn't take a long time to rewrite. Right. Right.

[02:33.76–02:49.20; L89–L96] >> If you mess up the architecture in the core trunk, probably takes like hundreds of people a long time to like fix. Have you ever had someone I remember early in my career I was all about speed and I was approving some diffs and then someone would come back to me and say why'd you approve this that was too

[02:51.36–02:53.36; L97–L98] >> you know like let's slow down a little bit on this

[02:54.48–02:55.92; L99–L100] >> oh they get some feedback or someone says hey

[02:57.28–03:10.08; L101–L106] >> you know calm down like this defin this definitely happens actually interesting thing so teach the people close to me in my teams that like hey it's okay buy stamp your diff to put it back in review again if you actually need deeper review

[03:13.20–03:33.44; L107–L118] >> or like flag it flag it in the summary or the test plan like or comment on it like hey I'm actually looking for a deep review on this if you know that's how our team operates now and this is actually really good because I might have thought it's like a child part of the system and maybe it is still a child part of the system but they've thought hey this is like could be like more performant or like I actually want you to double check this

[03:34.96–03:45.92; L119–L125] >> uh so then we use that signal to be like okay this person actually wants thing. So if I missed it, even if they put a comment on it, they'll throw it back into review and like be like need real review or something like that cuz they knew they knew what happened.

[03:47.36–03:47.36; L126–L126] >> Yeah. Yeah. Yeah.

[03:48.24–03:48.24; L127–L127] >> Yeah. I see. That makes sense.

[03:50.24–03:53.44; L128–L130] >> But yeah, there's definitely this is not the philosophy of everyone at Meta, right? Like we most people it's like

[03:55.44–03:55.44; L131–L131] >> quality high quality for everything.

[03:57.28–03:59.12; L132–L133] >> Yeah. And it depends on the system though.

[03:59.52–04:03.76; L134–L137] >> Depends on the system. Also depends on like this is like trust you build on your team too, right? If you're new on the team

[04:04.40–04:06.88; L138–L140] >> probably not going to get this treatment for the first couple of weeks. Yeah. Yeah.

[04:07.20–04:11.20; L141–L143] >> Although I do want to defer to like how do I accept this diff, not how do I reject this diff,

[04:12.56–04:14.72; L144–L145] >> which I think is an important philosophy to have.

[04:16.00–04:16.00; L146–L146] >> Why is that?

[04:16.72–04:16.72; L147–L147] >> Yeah.

[04:17.36–04:36.72; L148–L157] >> Uh cuz like I'm not trying to like knit your code and get you to write it the exact way I would write it, right? I'm trying to be like, okay, what is absolutely blocking this thing from going to going to production? Like big highle architecture things like I don't know some critical bugs like is it going to blow up prod right? not like write it exactly the way I would write it.

[04:38.40–04:43.60; L158–L161] >> Right. I think that takes a while to get to too, right? Like more senior engineers usually become amendable to this.

[04:44.08–04:44.08; L162–L162] >> Yeah.

[04:44.48–04:50.24; L163–L167] >> But when you're in Yeah. When you're like in the first 5 years of your career, maybe you've only seen a few ways of writing it, right? So you want people to write it that exact way.

[04:52.40–04:58.88; L168–L171] >> Yeah. Yeah. Definitely. I I think when you're working in a team where there's high trust and you get to the point where people

[05:00.40–05:05.60; L172–L175] >> they have feedback but they accept with nits, you know. I I love that because you just everyone's just trusting each other, you know, move fast.

[05:06.72–05:06.72; L176–L176] >> Yeah.

[05:07.20–05:07.20; L177–L177] >> And I have some feedback, but

[05:09.68–05:09.68; L178–L178] >> it's not that important. It's just like

[05:12.08–05:17.60; L179–L182] >> take it if you will. Man, this is where I push that needle even further again. So, I will like even if I see your diff is going to blow up production.

[05:20.08–05:21.76; L183–L184] >> I will I will comment on it and be like, "This is going to blow up production."

[05:23.92–05:28.96; L185–L188] >> And then accept it and be like, "Yeah, make sure you fix that first." Right. And like I've never had a case where someone's like landed it.

[05:30.40–05:36.32; L189–L193] >> Yeah. like with a comment on it that says, "Hey, this is going to blow up production." Cuz you can can you imagine like sitting in SE review or something and someone's like,

[05:37.44–05:40.40; L194–L196] >> "The diff had a comment on it. This is going to blow up production." And it blow up.

[05:41.12–05:41.12; L197–L197] >> That's wild that.

[05:43.12–05:45.04; L198–L199] >> Yeah. Except I just trust him to fix it. Right. Like

[05:45.44–05:45.44; L200–L200] >> Yeah. Yeah. Yeah.

[05:46.24–05:51.04; L201–L204] >> Fix it the right way. Once again, if they have trust, if it's like a new person on the team and I'm not sure if they're going to fix it the right way,

[05:53.04–05:54.64; L205–L206] >> right, I might be like, "Ping me again when it's like ready."

[05:55.84–05:55.84; L207–L207] >> Yeah. Yeah.

[05:56.40–05:58.08; L208–L209] >> But yeah, 99% of the time, I'll just like accept and go.

[05:59.20–05:59.20; L210–L210] >> Yeah.

[05:59.52–06:03.04; L211–L213] >> And Yeah. haven't had to do the thing where I pull back because I've never had one that's been shipped accidentally

[06:05.20–06:05.20; L214–L214] >> exploded production.

[06:07.36–06:12.72; L215–L218] >> And that's actually a little bit of a philosophy I use across like I guess building these systems judging how fast I'm moving.

[06:14.00–06:21.12; L219–L223] >> If I'm doing something and it's not I'm not getting feedback that it's like broken or I'm not seeing negative effects from it, right? Even if it is controversial and crazy,

[06:22.48–06:35.28; L224–L231] >> I'll keep pushing the boundary on it, right? Same as our rollouts. Like if we're at 1% we're getting like very little feedback and like metrics are looking good and we might move to like 10% the next day and people are like that's crazy like step to like two three five things. It's like

[06:36.64–06:36.64; L232–L232] >> well not we're not getting any like

[06:38.64–06:38.64; L233–L233] >> signals that it's not going poorly.

[06:40.64–06:42.00; L234–L235] >> As soon as we get signals that it's going poorly we start pulling back. But

[06:44.40–06:46.24; L236–L237] >> otherwise I find you like move too slowly.

[06:46.96–06:46.96; L238–L238] >> Yeah.

[06:47.44–06:53.52; L239–L242] >> Right. You want to be moving at like the fastest speed you can without ruining things. Right. So, if you're not getting if you're not

[06:54.48–06:56.08; L243–L244] >> making anything worse, like keep trying to find that edge.

[06:57.36–07:23.44; L245–L254] >> Yeah. I I had a tech lead early in my career and I had taken down prod or something and I was talking to him about it and he you know at one on one end you shouldn't break prod generally but he also said if you never break prod that's probably not also optimal like there there should be some level of risk otherwise you're moving too slowly and so

[07:23.68–07:23.68; L255–L255] >> yeah exactly

[07:24.48–07:24.48; L256–L256] >> yeah try not to break prod But

[07:27.20–07:29.28; L257–L258] >> if you never break it, you're probably like very slow and

[07:30.64–07:34.40; L259–L261] >> Yeah. And if you're breaking it every day, you're probably going way too fast. Yeah.

[07:34.80–07:34.80; L262–L262] >> Exactly.

[07:36.24–07:48.32; L263–L270] >> Hey, thanks for watching that clip. If you thought it was interesting, it's part of a longer conversation which you can find right here, right now. And as always, if you have any feedback for me, I'd love to hear it. You can leave a comment on YouTube. I read every single one that I get.
