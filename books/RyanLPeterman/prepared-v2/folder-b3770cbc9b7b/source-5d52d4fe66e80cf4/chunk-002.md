Chunk 2; segments 333–680. Start may repeat the previous chunk for context.

# GoogleX Chief Scientist: Imposter Syndrome, Career Growth, Project Taste | Carey Nachenberg

Source ID: source-5d52d4fe66e80cf4
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/GoogleX_Chief_Scientist_Imposter_Syndrome,_Career_Growth,_Project_Taste_Carey_Nachenberg_en.txt
Video: https://www.youtube.com/watch?v=zsoDJXTaahk

[L342] [12:13.60] you know, search for a string to find
[L343] [12:15.04] these things." So, I'm like, "Oh, that
[L344] [12:16.64] seems like a really interesting hard
[L345] [12:17.84] problem." So, I picked it and then I
[L346] [12:20.24] started working on it. That was my
[L347] [12:21.44] master thesis and then eventually
[L348] [12:23.20] transferred to the product. If you were
[L349] [12:25.44] to think about the things that you took
[L350] [12:26.80] on, they were a series of I guess side
[L351] [12:29.84] projects or or you know, whatever you
[L352] [12:31.76] wanted to take on where you you'd take
[L353] [12:33.76] on this new thing, maybe something else
[L354] [12:35.76] would come in, you take that on. Is that
[L355] [12:37.84] kind of how you were working?
[L356] [12:39.20] >> I would say there are probably six or
[L357] [12:40.72] seven times in my career where I'm like,
[L358] [12:42.48] "Oh, the company needs this type of
[L359] [12:44.56] thing. Let me go spend six weeks, two
[L360] [12:46.64] months, five months figuring out what
[L361] [12:49.52] that looks like, building prototypes,
[L362] [12:51.44] talking to engineers, and figuring out
[L363] [12:52.80] what they need. and then you know
[L364] [12:54.96] building that and there were other times
[L365] [12:56.88] which is probably 80% of my career where
[L366] [12:59.36] I was just sort of tweaking those things
[L367] [13:00.96] in other words we built them we were
[L368] [13:03.76] trying to either tech transfer it so I
[L369] [13:05.28] was helping with that fixing bugs
[L370] [13:07.28] improving those were sort of incremental
[L371] [13:09.60] improvements on those systems but that
[L372] [13:11.52] that it's one of those two things
[L373] [13:13.12] generally
[L374] [13:13.92] >> so you mentioned a little bit about
[L375] [13:15.84] viruses and when I was doing some
[L376] [13:17.76] research I saw that you had done some
[L377] [13:20.48] storytelling on top of stuckset and kind
[L378] [13:22.88] of compiled
[L379] [13:23.84] I think that's such an interesting
[L380] [13:25.92] story. Uh can you tell me a little bit
[L381] [13:28.24] about stuckset? Maybe we can go into
[L382] [13:30.00] that.
[L383] [13:30.48] >> Sure. Stuckset was um at the time just
[L384] [13:35.68] unfathomable. It was just a very complex
[L385] [13:38.96] piece of malware which was
[L386] [13:40.16] multiplatform. So it didn't just infect
[L387] [13:42.00] like Mac machines or Windows machines.
[L388] [13:44.32] It infected I think you know Windows
[L389] [13:46.32] machines but also like microcontrollers
[L390] [13:49.12] that would actually run like centrifuges
[L391] [13:50.80] and so on. Um, and so it was probably
[L392] [13:53.60] the first multi-platform piece of
[L393] [13:55.36] malware we had discovered. Uh, use zero
[L394] [13:58.40] days in order to break into systems that
[L395] [14:00.40] you know that you know basically
[L396] [14:01.52] vulnerabilities, exploiting
[L397] [14:02.56] vulnerabilities that hadn't been patched
[L398] [14:04.64] because they weren't even known about.
[L399] [14:06.08] And it didn't use just one of those or
[L400] [14:07.68] two of those. I think it used like six
[L401] [14:09.52] different vulnerabilities to spread,
[L402] [14:10.96] many of which were zero days.
[L403] [14:12.40] >> My god.
[L404] [14:12.88] >> Um, it would literally stealth itself.
[L405] [14:15.52] So on your computer, if you were to look
[L406] [14:17.92] at a at a thumb drive which had
[L407] [14:20.96] Snapchatnet on it and look in your your
[L408] [14:23.28] your Finder application or your Windows,
[L409] [14:25.20] you know, file system application, you
[L410] [14:27.44] would see, you know, nothing there, but
[L411] [14:29.68] it was there. You'd stick that in your
[L412] [14:31.44] computer, it would auto launch. It
[L413] [14:33.36] actually had a a payload to auto launch.
[L414] [14:35.76] If you were to look at the logic that
[L415] [14:38.32] was running on a centrifuge or rather
[L416] [14:40.48] the controller that ran the frequency
[L417] [14:42.00] converters, you would not see any of the
[L418] [14:44.16] specs in that logic. It was in that
[L419] [14:46.88] controller. But if you downloaded the
[L420] [14:50.00] the logic from that controller onto a
[L421] [14:51.92] Windows machine, it would stealth and
[L422] [14:54.16] remove the logic from stuckset as it
[L423] [14:56.16] pulled it off. And then if you updated
[L424] [14:57.92] that logic, for instance, it would
[L425] [14:59.52] reinsert itself into that logic to
[L426] [15:01.36] reinfect it as it went back. So we
[L427] [15:03.68] actually like sort of piggyback on back
[L428] [15:05.76] and forth stealth itself. Um it was just
[L429] [15:08.64] amazing. And then of course how it
[L430] [15:09.68] disrupted the centrifuges is super
[L431] [15:11.12] interesting as well.
[L432] [15:12.16] >> Yeah, it's so complicated and
[L433] [15:15.92] sophisticated that it makes me wonder
[L434] [15:19.12] who wrote it and I saw something like it
[L435] [15:21.04] was, you know, 50 times bigger than the
[L436] [15:23.20] average virus. Incredibly complicated
[L437] [15:25.76] software. And I was reading into
[L438] [15:27.44] Wikipedia a little bit before we kind of
[L439] [15:29.36] it said no one has claimed credit for
[L440] [15:31.68] who wrote this thing. Who do you think
[L441] [15:33.92] wrote this thing? It's
[L442] [15:34.96] >> I think it's pretty good. You'd be
[L443] [15:37.12] pretty safe to say it was the Israelis
[L444] [15:38.64] and the American government. You know,
[L445] [15:40.32] my understanding or recollection is that
[L446] [15:42.16] there are water not watermarks but sort
[L447] [15:44.96] of, you know, coding styles or things in
[L448] [15:47.04] there that sort of implicate both uh
[L449] [15:49.92] governments.
[L450] [15:50.56] >> Have you ever looked at the source code
[L451] [15:52.00] or played?
[L452] [15:52.88] >> I have not. I didn't do any analysis on
[L453] [15:54.72] stuck set. Um my career was focused
[L454] [15:57.44] early on analyzing malware like
[L455] [15:59.12] literally looking at the machine
[L456] [16:00.56] language and disassembling and so on.
[L457] [16:02.48] But later on in my career it was mostly
[L458] [16:04.08] about detecting sort knows how how could
[L459] [16:05.92] I build algorithms to detect that
[L460] [16:08.40] malware rather than hands-on analyzing
[L461] [16:10.40] the malware myself. So I'd never looked
[L462] [16:12.40] at stuckset. Yeah.
[L463] [16:13.44] >> You mentioned a little bit about uh
[L464] [16:15.12] assembly code. Did you ever write
[L465] [16:17.04] assembly code when you were working at
[L466] [16:18.80] cement?
[L467] [16:19.68] >> I did. Yeah. I wrote assembly code as an
[L468] [16:21.60] intern. Um and uh although back in those
[L469] [16:25.44] days it was mostly C.
[L470] [16:26.80] >> Yeah.
[L471] [16:27.12] >> Um but some assembly as well. And I
[L472] [16:29.28] remember the first antivirus engines
[L473] [16:30.72] were written in assembly for speed. And
[L474] [16:32.64] one of my first tasks as I joined
[L475] [16:34.40] full-time was I said, you know, this
[L476] [16:36.08] really needs to be a C so it's more
[L477] [16:37.28] maintainable. So we ported the thing to
[L478] [16:38.72] C and actually made it faster because
[L479] [16:40.56] the people back then people didn't know
[L480] [16:42.32] algorithms. They didn't understand what
[L481] [16:44.24] an what a big O was or how to you know
[L482] [16:46.32] they would do linear searches. And so we
[L483] [16:48.64] were able to go and take something in
[L484] [16:49.76] assembly language, move it over to C,
[L485] [16:52.08] have less code, um, and it would be, you
[L486] [16:54.64] know, five times faster. So
[L487] [16:56.64] >> I see. So the the speed ups moving from
[L488] [16:59.12] assembly to C was due to better
[L489] [17:02.00] algorithms and things like that. It
[L490] [17:03.68] wasn't because of a compiler or
[L491] [17:05.36] something.
[L492] [17:06.08] >> No, the compilers weren't that great
[L493] [17:07.36] back then. But even without an
[L494] [17:08.48] optimizing compiler, if you use a hasht
[L495] [17:11.12] versus or binary search versus a linear
[L496] [17:13.12] search over 60,000 signatures, you know,
[L497] [17:16.16] >> I I saw that you worked at Semantic for
[L498] [17:18.32] a long time and you know, I think in the
[L499] [17:20.48] tech industry, it's common for people to
[L500] [17:24.00] move around here and there. What do you
[L501] [17:26.48] think kept you at semantic as long as
[L502] [17:28.56] you were?
[L503] [17:29.28] >> You know, that's a great question. Um,
[L504] [17:31.68] if I have to be perfectly honest, I
[L505] [17:33.36] would say imposttor syndrome.
[L506] [17:36.40] >> Really? So well yes and no. So at
[L507] [17:39.20] semantic I didn't really have imposttor
[L508] [17:41.04] syndrome because I had done a lot of
[L509] [17:43.04] stuff and I was well regarded you know I
[L510] [17:45.68] was known in the company and so I had a
[L511] [17:48.24] good safe place but I always worried
[L512] [17:50.80] what if it just is because I'm at
[L513] [17:52.96] Semantic and I grew up here and I
[L514] [17:54.64] learned the stuff here. what if I went
[L515] [17:55.84] somewhere else and I wouldn't be able to
[L516] [17:57.28] learn the stuff or what if people had
[L517] [17:59.52] different standards and what if like I'm
[L518] [18:01.36] not good enough for Google or Meta or
[L519] [18:04.00] something and so I stayed because it was
[L520] [18:06.80] comfortable and I complained I
[L521] [18:08.24] complained all the time I wasn't happy
[L522] [18:09.76] later on in my career I have to be
[L523] [18:11.28] honest with you I wasn't doing things
[L524] [18:13.52] that made me happy more when you get
[L525] [18:15.76] more senior you do a lot more BS right
[L526] [18:17.92] and and and
[L527] [18:20.72] you also have the opportunity not to do
[L528] [18:22.64] as much BS but you have to push yourself
[L529] [18:25.20] not to do it because it's very easy to,
[L530] [18:27.04] you know, go to meetings and, you know,
[L531] [18:29.12] have broad discussions and it's not
[L532] [18:30.96] really that necessarily fun,
[L533] [18:32.88] >> right?
[L534] [18:33.20] >> Um, and so I wasn't happy near the end
[L535] [18:36.24] of my tenure at Semantic, but I was
[L536] [18:38.00] afraid that I wouldn't be able to do
[L537] [18:39.68] well or I'd fail the interview process.
[L538] [18:41.28] And so I just stayed and it was
[L539] [18:43.04] comfortable. throughout your career
[L540] [18:45.04] there were so many promotions and you
[L541] [18:47.36] had so much impact for someone like you
[L542] [18:49.92] to have imposter syndrome you know I
[L543] [18:52.16] feel like that shows that a lot of
[L544] [18:53.60] people you know it's it's a very natural
[L545] [18:56.08] feeling for a lot of people did you
[L546] [18:59.60] eventually you did leave semantics so
[L547] [19:01.60] was there anything that helped you uh
[L548] [19:03.52] overcome imposter syndrome
[L549] [19:05.36] >> you know what the thing that that helped
[L550] [19:08.00] me was that somebody said hey we want to
[L551] [19:10.32] interview you we think you'd be a good
[L552] [19:11.92] fit and so I said you Well, I'm probably
[L553] [19:14.24] going to fail this interview. I'm sure
[L554] [19:15.60] I'm not good enough, but I'm going to do
[L555] [19:17.20] it. And so, I just did it. And so, that,
[L556] [19:19.12] you know, I needed an external pull or
[L557] [19:21.60] push, I don't know what you would call
[L558] [19:22.56] it, but in order to get me to to take
[L559] [19:24.32] the chance, and then it worked out. But
[L560] [19:26.40] for me, like in my head, I was, you
[L561] [19:29.36] know, I wasn't competent to do that job.
[L562] [19:32.24] You know,
[L563] [19:32.80] >> you you mentioned uh also that at the
[L564] [19:35.20] highest levels, there's uh, you know, a
[L565] [19:37.52] lot of BS and, you know, I guess it
[L566] [19:39.44] sounds like meetings and things like
[L567] [19:40.72] that. Do you have any uh I guess tips on
[L568] [19:44.00] how to be less involved in the BS
[L569] [19:46.80] because I think that's a natural pull
[L570] [19:48.72] pull for anyone.
[L571] [19:50.16] >> Yeah, it's sort of natural definitely it
[L572] [19:52.80] depends what you're doing. I mean some
[L573] [19:54.24] some tech senior technical directors and
[L574] [19:56.24] distinguished engineers even fellows
[L575] [19:57.76] were working dayto-day and building code
[L576] [20:00.08] and and working with their teams. It
[L577] [20:01.76] just depended uh I was an individual
[L578] [20:04.24] contributor vice president. So I was an
[L579] [20:05.68] IC through my entire time at semantic.
[L580] [20:07.76] other people would actually manage teams
[L581] [20:09.28] and work uh more closely on projects.
[L582] [20:12.40] You know, it's just it's inevitable,
[L583] [20:13.92] right? In other words, you're having
[L584] [20:15.20] more strategic meetings and then the
[L585] [20:17.20] problem is you're having a strategic
[L586] [20:18.80] strategic meeting with a bunch of
[L587] [20:20.32] people, many of which many of whom don't
[L588] [20:23.04] necessarily know that much, but they
[L589] [20:25.28] have an opinion because everybody has an
[L590] [20:26.64] opinion. Um, and there's a lot of
[L591] [20:29.12] debating and a lot of arguing and a lot
[L592] [20:30.80] of like, you know, posturing for, you
[L593] [20:34.00] know, for power. And, you know, it's
[L594] [20:37.12] just there's a there's a lot of garbage
[L595] [20:39.36] that comes with being more senior,
[L596] [20:40.56] unfortunately. Like, there was some some
[L597] [20:42.00] joy, especially for me when I got to
[L598] [20:44.00] pick my own projects to be able to just
[L599] [20:45.28] sit down and literally go two months
[L600] [20:46.80] with nobody asking me what what are you
[L601] [20:48.32] doing? And, you know, I'm just like
[L602] [20:50.48] cranking and trying things. That doesn't
[L603] [20:52.32] work, but that does. And super exciting.
[L604] [20:54.24] Right.
[L605] [20:54.72] >> Right. Then you get into a room with
[L606] [20:57.28] seven people and you're like, "We've
[L607] [20:59.04] agreed that this is our new company
[L608] [21:00.40] strategy." One of my last rule uh things
[L609] [21:02.32] of the company I did was actually define
[L610] [21:03.84] the company technology strategy for the
[L611] [21:05.68] whole company. And everybody had agreed
[L612] [21:07.12] to it. The CEO had agreed to it. And
[L613] [21:08.40] then we get in a room and everybody
[L614] [21:09.52] would say, "Oh, sure. But you know, we
[L615] [21:12.08] have to make money on our projects or
[L616] [21:13.84] products." And so, you know, adding
[L617] [21:15.12] those features to align with technology
[L618] [21:17.04] strategy that's gonna set us back. And
[L619] [21:20.00] we've been told we have to make, you
[L620] [21:21.52] know, this much topline revenue. And so,
[L621] [21:23.44] you know, you end up having debates and
[L622] [21:25.68] discussions and it's like very very
[L623] [21:27.84] draining.
[L624] [21:28.88] >> So, you said you were pulled into Google
[L625] [21:31.60] X and you ended up taking the interview
[L626] [21:34.16] and and doing well. I'm curious, what
[L627] [21:37.04] was it like entering, you know, Google
[L628] [21:39.44] or this like fang style big tech? And
[L629] [21:41.92] were there any cultural differences that
[L630] [21:43.44] stood out to you?
[L631] [21:44.64] >> You know, few than you would think. I
[L632] [21:47.28] would say the biggest difference that I
[L633] [21:49.84] saw there was there were really really
[L634] [21:52.16] really smart people like semantic had
[L635] [21:54.72] some smart people but again it didn't
[L636] [21:56.24] have an engineering culture even when I
[L637] [21:57.60] left in 2016 it was starting to develop
[L638] [21:59.44] one but it was really you know it was
[L639] [22:01.20] more a little looser gooseier than a
[L640] [22:02.88] Google for sure um but the quality of
[L641] [22:05.60] the people in Google X and X were really
[L642] [22:08.72] very high quality in terms of
[L643] [22:10.08] intelligence now what what seemed about
[L644] [22:12.56] the same was that many people in X as
[L645] [22:16.00] there were many people in Semantic
[L646] [22:17.84] didn't have good taste, research taste
[L647] [22:19.92] if or or project taste. And so a lot of
[L648] [22:22.72] people were really smart, but it wasn't
[L649] [22:25.60] clear that they were picking projects
[L650] [22:26.88] that would be that would land or you
[L651] [22:28.96] know or that were feasible in you know
[L652] [22:32.08] at least in my opinion. So I think
[L653] [22:34.24] that's a that is an attribute of
[L654] [22:36.40] engineers no matter what company, no
[L655] [22:38.24] matter how intelligent um people are.
[L656] [22:41.44] Um, but it was uh, you know, like it was
[L657] [22:43.28] it was startling how much how much
[L658] [22:44.96] brilliance there was. And I do remember
[L659] [22:46.88] like there was one guy who was clearly
[L660] [22:48.88] like over a 200 IQ. The guy was just you
[L661] [22:52.00] talked to him and he was just
[L662] [22:54.00] astoundingly brilliant and he was still
[L663] [22:56.32] in L4.
[L664] [22:57.28] >> Yeah.
[L665] [22:57.68] >> Why was he in the L4? Because, you know,
[L666] [22:59.84] he had lack of communication skills. You
[L667] [23:02.88] know, worked on really interesting stuff
[L668] [23:04.32] that was interesting to him but not
[L669] [23:05.68] necessarily had business impact. Didn't
[L670] [23:08.00] collaborate well apparently. you know,
[L671] [23:09.52] like there were things, whatever it was.
[L672] [23:11.28] And it didn't matter that he was
[L673] [23:12.88] brilliant. Like he was twice as smart as
[L674] [23:15.36] I was, but you know, just because you
[L675] [23:17.68] have intelligence doesn't mean you're
[L676] [23:18.80] going to be successful. And so that was,
[L677] [23:20.24] you know, saw the same thing there.
[L678] [23:22.00] >> If I'm understanding correctly, if
[L679] [23:23.76] you're very ambitious and you really
[L680] [23:26.24] want career growth, intelligence is not
[L681] [23:29.84] that important. It sounds like there are
[L682] [23:31.60] some things that are much more
[L683] [23:32.64] important. You cited uh communication,
[L684] [23:34.96] soft skills, project taste, picking
[L685] [23:37.12] things that actually matter.
[L686] [23:38.56] >> Yeah. Is there anything else that you
[L687] [23:40.16] that comes to mind?
[L688] [23:41.44] >> There are definitely people who are less
[L689] [23:42.80] intelligent. You're not going to like at
