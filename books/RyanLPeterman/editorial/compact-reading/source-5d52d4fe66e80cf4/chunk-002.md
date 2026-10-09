# GoogleX Chief Scientist: Imposter Syndrome, Career Growth, Project Taste | Carey Nachenberg
Source: source-5d52d4fe66e80cf4 | Chunk 2 of 7
Video: https://www.youtube.com/watch?v=zsoDJXTaahk
All caption text retained; paragraphs merge caption fragments without changing words.

[12:13.60–12:37.84; L342–L355] you know, search for a string to find these things." So, I'm like, "Oh, that seems like a really interesting hard problem." So, I picked it and then I started working on it. That was my master thesis and then eventually transferred to the product. If you were to think about the things that you took on, they were a series of I guess side projects or or you know, whatever you wanted to take on where you you'd take on this new thing, maybe something else would come in, you take that on. Is that kind of how you were working?

[12:39.20–13:13.12; L356–L373] >> I would say there are probably six or seven times in my career where I'm like, "Oh, the company needs this type of thing. Let me go spend six weeks, two months, five months figuring out what that looks like, building prototypes, talking to engineers, and figuring out what they need. and then you know building that and there were other times which is probably 80% of my career where I was just sort of tweaking those things in other words we built them we were trying to either tech transfer it so I was helping with that fixing bugs improving those were sort of incremental improvements on those systems but that that it's one of those two things generally

[13:13.92–13:30.00; L374–L382] >> so you mentioned a little bit about viruses and when I was doing some research I saw that you had done some storytelling on top of stuckset and kind of compiled I think that's such an interesting story. Uh can you tell me a little bit about stuckset? Maybe we can go into that.

[13:30.48–14:10.96; L383–L402] >> Sure. Stuckset was um at the time just unfathomable. It was just a very complex piece of malware which was multiplatform. So it didn't just infect like Mac machines or Windows machines. It infected I think you know Windows machines but also like microcontrollers that would actually run like centrifuges and so on. Um, and so it was probably the first multi-platform piece of malware we had discovered. Uh, use zero days in order to break into systems that you know that you know basically vulnerabilities, exploiting vulnerabilities that hadn't been patched because they weren't even known about. And it didn't use just one of those or two of those. I think it used like six different vulnerabilities to spread, many of which were zero days.

[14:12.40–14:12.40; L403–L403] >> My god.

[14:12.88–15:01.36; L404–L426] >> Um, it would literally stealth itself. So on your computer, if you were to look at a at a thumb drive which had Snapchatnet on it and look in your your your Finder application or your Windows, you know, file system application, you would see, you know, nothing there, but it was there. You'd stick that in your computer, it would auto launch. It actually had a a payload to auto launch. If you were to look at the logic that was running on a centrifuge or rather the controller that ran the frequency converters, you would not see any of the specs in that logic. It was in that controller. But if you downloaded the the logic from that controller onto a Windows machine, it would stealth and remove the logic from stuckset as it pulled it off. And then if you updated that logic, for instance, it would reinsert itself into that logic to reinfect it as it went back. So we

[15:03.68–15:11.12; L427–L431] actually like sort of piggyback on back and forth stealth itself. Um it was just amazing. And then of course how it disrupted the centrifuges is super interesting as well.

[15:12.16–15:33.92; L432–L441] >> Yeah, it's so complicated and sophisticated that it makes me wonder who wrote it and I saw something like it was, you know, 50 times bigger than the average virus. Incredibly complicated software. And I was reading into Wikipedia a little bit before we kind of it said no one has claimed credit for who wrote this thing. Who do you think wrote this thing? It's

[15:34.96–15:49.92; L442–L449] >> I think it's pretty good. You'd be pretty safe to say it was the Israelis and the American government. You know, my understanding or recollection is that there are water not watermarks but sort of, you know, coding styles or things in there that sort of implicate both uh governments.

[15:50.56–15:52.00; L450–L451] >> Have you ever looked at the source code or played?

[15:52.88–16:12.40; L452–L462] >> I have not. I didn't do any analysis on stuck set. Um my career was focused early on analyzing malware like literally looking at the machine language and disassembling and so on. But later on in my career it was mostly about detecting sort knows how how could I build algorithms to detect that malware rather than hands-on analyzing the malware myself. So I'd never looked at stuckset. Yeah.

[16:13.44–16:18.80; L463–L466] >> You mentioned a little bit about uh assembly code. Did you ever write assembly code when you were working at cement?

[16:19.68–16:25.44; L467–L469] >> I did. Yeah. I wrote assembly code as an intern. Um and uh although back in those days it was mostly C.

[16:26.80–16:26.80; L470–L470] >> Yeah.

[16:27.12–16:54.64; L471–L486] >> Um but some assembly as well. And I remember the first antivirus engines were written in assembly for speed. And one of my first tasks as I joined full-time was I said, you know, this really needs to be a C so it's more maintainable. So we ported the thing to C and actually made it faster because the people back then people didn't know algorithms. They didn't understand what an what a big O was or how to you know they would do linear searches. And so we were able to go and take something in assembly language, move it over to C, have less code, um, and it would be, you know, five times faster. So

[16:56.64–17:05.36; L487–L491] >> I see. So the the speed ups moving from assembly to C was due to better algorithms and things like that. It wasn't because of a compiler or something.

[17:06.08–17:13.12; L492–L496] >> No, the compilers weren't that great back then. But even without an optimizing compiler, if you use a hasht versus or binary search versus a linear search over 60,000 signatures, you know,

[17:16.16–17:28.56; L497–L502] >> I I saw that you worked at Semantic for a long time and you know, I think in the tech industry, it's common for people to move around here and there. What do you think kept you at semantic as long as you were?

[17:29.28–17:33.36; L503–L505] >> You know, that's a great question. Um, if I have to be perfectly honest, I would say imposttor syndrome.

[17:36.40–18:17.92; L506–L526] >> Really? So well yes and no. So at semantic I didn't really have imposttor syndrome because I had done a lot of stuff and I was well regarded you know I was known in the company and so I had a good safe place but I always worried what if it just is because I'm at Semantic and I grew up here and I learned the stuff here. what if I went somewhere else and I wouldn't be able to learn the stuff or what if people had different standards and what if like I'm not good enough for Google or Meta or something and so I stayed because it was comfortable and I complained I complained all the time I wasn't happy later on in my career I have to be honest with you I wasn't doing things that made me happy more when you get more senior you do a lot more BS right and and and

[18:20.72–18:30.96; L527–L532] you also have the opportunity not to do as much BS but you have to push yourself not to do it because it's very easy to, you know, go to meetings and, you know, have broad discussions and it's not really that necessarily fun,

[18:32.88–18:32.88; L533–L533] >> right?

[18:33.20–19:03.52; L534–L548] >> Um, and so I wasn't happy near the end of my tenure at Semantic, but I was afraid that I wouldn't be able to do well or I'd fail the interview process. And so I just stayed and it was comfortable. throughout your career there were so many promotions and you had so much impact for someone like you to have imposter syndrome you know I feel like that shows that a lot of people you know it's it's a very natural feeling for a lot of people did you eventually you did leave semantics so was there anything that helped you uh overcome imposter syndrome

[19:05.36–19:32.24; L549–L562] >> you know what the thing that that helped me was that somebody said hey we want to interview you we think you'd be a good fit and so I said you Well, I'm probably going to fail this interview. I'm sure I'm not good enough, but I'm going to do it. And so, I just did it. And so, that, you know, I needed an external pull or push, I don't know what you would call it, but in order to get me to to take the chance, and then it worked out. But for me, like in my head, I was, you know, I wasn't competent to do that job. You know,

[19:32.80–19:48.72; L563–L570] >> you you mentioned uh also that at the highest levels, there's uh, you know, a lot of BS and, you know, I guess it sounds like meetings and things like that. Do you have any uh I guess tips on how to be less involved in the BS because I think that's a natural pull pull for anyone.

[19:50.16–20:37.12; L571–L594] >> Yeah, it's sort of natural definitely it depends what you're doing. I mean some some tech senior technical directors and distinguished engineers even fellows were working dayto-day and building code and and working with their teams. It just depended uh I was an individual contributor vice president. So I was an IC through my entire time at semantic. other people would actually manage teams and work uh more closely on projects. You know, it's just it's inevitable, right? In other words, you're having more strategic meetings and then the problem is you're having a strategic strategic meeting with a bunch of people, many of which many of whom don't necessarily know that much, but they have an opinion because everybody has an opinion. Um, and there's a lot of debating and a lot of arguing and a lot of like, you know, posturing for, you know, for power. And, you know, it's just there's a there's a lot of garbage

[20:39.36–20:54.24; L595–L604] that comes with being more senior, unfortunately. Like, there was some some joy, especially for me when I got to pick my own projects to be able to just sit down and literally go two months with nobody asking me what what are you doing? And, you know, I'm just like cranking and trying things. That doesn't work, but that does. And super exciting. Right.

[20:54.72–21:27.84; L605–L623] >> Right. Then you get into a room with seven people and you're like, "We've agreed that this is our new company strategy." One of my last rule uh things of the company I did was actually define the company technology strategy for the whole company. And everybody had agreed to it. The CEO had agreed to it. And then we get in a room and everybody would say, "Oh, sure. But you know, we have to make money on our projects or products." And so, you know, adding those features to align with technology strategy that's gonna set us back. And we've been told we have to make, you know, this much topline revenue. And so, you know, you end up having debates and discussions and it's like very very draining.

[21:28.88–21:43.44; L624–L630] >> So, you said you were pulled into Google X and you ended up taking the interview and and doing well. I'm curious, what was it like entering, you know, Google or this like fang style big tech? And were there any cultural differences that stood out to you?

[21:44.64–22:32.08; L631–L652] >> You know, few than you would think. I would say the biggest difference that I saw there was there were really really really smart people like semantic had some smart people but again it didn't have an engineering culture even when I left in 2016 it was starting to develop one but it was really you know it was more a little looser gooseier than a Google for sure um but the quality of the people in Google X and X were really very high quality in terms of intelligence now what what seemed about the same was that many people in X as there were many people in Semantic didn't have good taste, research taste if or or project taste. And so a lot of people were really smart, but it wasn't clear that they were picking projects that would be that would land or you know or that were feasible in you know at least in my opinion. So I think

[22:34.24–22:56.32; L653–L663] that's a that is an attribute of engineers no matter what company, no matter how intelligent um people are. Um, but it was uh, you know, like it was it was startling how much how much brilliance there was. And I do remember like there was one guy who was clearly like over a 200 IQ. The guy was just you talked to him and he was just astoundingly brilliant and he was still in L4.

[22:57.28–22:57.28; L664–L664] >> Yeah.

[22:57.68–23:20.24; L665–L677] >> Why was he in the L4? Because, you know, he had lack of communication skills. You know, worked on really interesting stuff that was interesting to him but not necessarily had business impact. Didn't collaborate well apparently. you know, like there were things, whatever it was. And it didn't matter that he was brilliant. Like he was twice as smart as I was, but you know, just because you have intelligence doesn't mean you're going to be successful. And so that was, you know, saw the same thing there.

[23:22.00–23:37.12; L678–L685] >> If I'm understanding correctly, if you're very ambitious and you really want career growth, intelligence is not that important. It sounds like there are some things that are much more important. You cited uh communication, soft skills, project taste, picking things that actually matter.

[23:38.56–23:40.16; L686–L687] >> Yeah. Is there anything else that you that comes to mind?

[23:41.44–23:42.80; L688–L689] >> There are definitely people who are less intelligent. You're not going to like at
