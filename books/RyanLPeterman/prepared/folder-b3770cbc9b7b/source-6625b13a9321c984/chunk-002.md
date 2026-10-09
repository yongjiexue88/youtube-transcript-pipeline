Chunk 2; segments 329–667. Start may repeat the previous chunk for context.

# Casey Muratori: The Anatomy of a 35-Year Mistake, "Clean Code" Horrible Performance

Source ID: source-6625b13a9321c984
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Casey_Muratori_The_Anatomy_of_a_35-Year_Mistake,_Clean_Code_Horrible_Performance_en.txt
Video: https://www.youtube.com/watch?v=jHLbL1Eg4gM

[L338] [11:51.28] kind of the first time this was really
[L339] [11:52.80] put to print that I know of he he does
[L340] [11:55.04] he does say it in an ACM touring lecture
[L341] [11:57.60] a little earlier but he would have
[L342] [11:59.68] submitted like based on my timeline he
[L343] [12:02.64] would have submitted the manuscript for
[L344] [12:04.80] this publication prior to the lecture.
[L345] [12:07.36] So it was the first time that I know of
[L346] [12:09.20] that he actually committed it to paper
[L347] [12:10.64] would have been there but he may have
[L348] [12:12.40] said this a lot in lectures. He kind of
[L349] [12:14.48] obliquely refers to that in the touring
[L350] [12:16.24] lecture that maybe he had said this
[L351] [12:18.00] around you know around town so to speak.
[L352] [12:20.48] So you know where this was first uttered
[L353] [12:23.52] I don't think anyone knows but point
[L354] [12:25.68] being uh when he says that phrase kind
[L355] [12:28.32] of it's in this context of saying look
[L356] [12:30.96] we we need to be very concerned about
[L357] [12:32.88] efficiency. We shouldn't be leaving
[L358] [12:34.96] performance on the table when it
[L359] [12:36.24] matters. But at the same time, we need
[L360] [12:38.32] to know that it matters. If we don't
[L361] [12:40.16] know that it matters that we're going to
[L362] [12:41.92] apply this optimization, then you know
[L363] [12:44.80] that's a premature optimization and it
[L364] [12:47.28] has real costs. It it's going to make
[L365] [12:49.76] our maintenance and debugging of this
[L366] [12:51.44] program worse for all the same reasons
[L367] [12:53.60] that it would make it worse today. Like
[L368] [12:54.96] if we go into something and we start
[L369] [12:56.72] applying these like optimizations to it
[L370] [12:59.28] that are above and beyond the kind of
[L371] [13:01.44] structural things that we might be doing
[L372] [13:02.80] to that code otherwise that's creating a
[L373] [13:05.60] cognitive burden right um that other
[L374] [13:07.92] people are now going to have to deal
[L375] [13:08.88] with and you're going to have to deal
[L376] [13:10.00] with in the future. So I don't want to
[L377] [13:12.72] put too many words in Canuth's mouth
[L378] [13:14.40] certainly, but in general that's sort of
[L379] [13:17.20] the way that this comes together is
[L380] [13:19.36] those two things. This idea that we need
[L381] [13:20.96] to be more, you know, be doing things to
[L382] [13:22.48] solve the software crisis, have a more
[L383] [13:24.24] structured appro approach to
[L384] [13:25.44] programming, care about maintainability
[L385] [13:27.04] and debugability, composability,
[L386] [13:28.64] abstraction, all that stuff. But also at
[L387] [13:31.92] the same time, we do care about
[L388] [13:33.44] optimization. So how do you dovtail
[L389] [13:34.96] those things? Premature optimization is
[L390] [13:36.32] the root of all evil is kind of like
[L391] [13:37.84] this phrase he uses. I I would I would
[L392] [13:40.08] say if I had if I had to imagine his way
[L393] [13:43.20] of sort of reminding himself, think
[L394] [13:45.52] about all this before you make a
[L395] [13:48.88] decision, right? Um
[L396] [13:52.08] that would be kind of my take on it,
[L397] [13:53.44] right? And and where it comes from. So
[L398] [13:54.80] hopefully, I don't know, that's very
[L399] [13:56.16] long, but it's a very expansive
[L400] [13:57.20] question. So hopefully I've kind of
[L401] [13:58.16] wrangled most of the stuff into there.
[L402] [14:00.16] It sounds like this is really a
[L403] [14:02.40] engineering trade-off where the software
[L404] [14:06.08] crisis is about the maintainability and
[L405] [14:10.32] uh the the complexity for people to
[L406] [14:12.80] actually write and handle their code and
[L407] [14:16.64] then the trade-off between performance
[L408] [14:19.20] and I guess you know code that is
[L409] [14:20.88] maintainable and it sounds like this new
[L410] [14:23.60] quote is
[L411] [14:25.60] you know be mindful of where you pay
[L412] [14:28.00] that cost. Yes. And it's always
[L413] [14:31.04] important to understand the context in
[L414] [14:33.44] which this was said historically. It's
[L415] [14:35.68] why I want it to be a historical talk
[L416] [14:38.64] because who your audience is is a large
[L417] [14:42.80] determiner of what the root of all evil
[L418] [14:44.80] is. Right? If you talking if you're
[L419] [14:47.44] talking to a bunch of people who don't
[L420] [14:48.88] think about optimization at all, then
[L421] [14:50.88] you don't really need to say this phrase
[L422] [14:52.32] to them, right?
[L423] [14:54.24] And so if you fast forward to today when
[L424] [14:56.16] a lot of people don't really take
[L425] [14:57.60] optimization into account at all during
[L426] [14:59.84] their programming um or very very little
[L427] [15:03.52] uh this phrase doesn't make very much
[L428] [15:05.04] sense to someone who does care about
[L429] [15:06.80] performance because like why would you
[L430] [15:07.92] ever say that? It just kind of seems
[L431] [15:08.96] like it encourages people to not be
[L432] [15:11.60] mindful of the performance of their
[L433] [15:12.88] program.
[L434] [15:14.64] But if you rewind to that time
[L435] [15:17.92] and you understand that well a lot of
[L436] [15:20.88] the program you know they had the
[L437] [15:22.48] opposite problem. A lot of the programs
[L438] [15:24.32] at that time what what programming was
[L439] [15:27.12] was coming up with all these crazy
[L440] [15:29.20] little assembly tricks to like shave a
[L441] [15:31.84] cycle off here or there, right? And if
[L442] [15:34.24] you're talking to an auditorium full of
[L443] [15:35.92] people who are really into that sort of
[L444] [15:37.60] thing,
[L445] [15:39.28] uh then it really can be the root of all
[L446] [15:41.20] evil, right? It's like you guys are
[L447] [15:42.48] spending all your time on this, but we
[L448] [15:45.28] have this really big other problem and
[L449] [15:47.28] that is not the right trade-off, right?
[L450] [15:49.04] That is you've you've swung, you know,
[L451] [15:51.44] like calling it trade-offs is a great
[L452] [15:53.28] way to say it. You've swung the pendulum
[L453] [15:55.20] way too far in one of those directions
[L454] [15:57.04] at some point. And and so, you know, to
[L455] [15:59.36] some degree, while I wouldn't while I
[L456] [16:01.60] would highly dispute the the description
[L457] [16:03.84] root of all evil today as a good thing
[L458] [16:06.24] to say to somebody or or that it leaves
[L459] [16:08.56] a good impression, when we rewind to
[L460] [16:10.24] that time period, I think it makes a lot
[L461] [16:11.84] more sense because when you look at what
[L462] [16:13.36] people were actually spending their time
[L463] [16:14.72] doing, where their priorities were, I
[L464] [16:17.20] think that maybe that wasn't so much of
[L465] [16:19.04] an exaggeration. I mean, obviously, it's
[L466] [16:20.56] a hyperbole, but it's less of one. in
[L467] [16:23.68] your slides, there were so many quotes
[L468] [16:26.08] and snippets of really kind of digging
[L469] [16:28.40] into the true history. Was there
[L470] [16:30.24] anything you found that surprised you
[L471] [16:31.84] when you were doing the research?
[L472] [16:33.44] >> I mean, constantly. Uh, absolutely,
[L473] [16:36.32] constantly. And I mean, first of all,
[L474] [16:39.04] I'll just say that there's
[L475] [16:42.80] as a meta point, I'll I'll give you a
[L476] [16:44.56] specific thing that surprised me that's
[L477] [16:46.48] kind of funny. Um, that's that's more
[L478] [16:49.28] about like a technical thing. But first
[L479] [16:51.44] I want to talk about a broader picture
[L480] [16:53.84] which is one of the things that really
[L481] [16:57.12] hits home for me whenever I do these is
[L482] [16:59.60] the personal aspects of it like these
[L483] [17:03.12] people were like friends and competitors
[L484] [17:06.48] and like all these sorts of things and
[L485] [17:08.80] it's all kind of lost to us in a way
[L486] [17:12.24] when we think about computing history in
[L487] [17:14.16] like a sterile way like you know when I
[L488] [17:18.32] read up on what Dystra Dyster was the
[L489] [17:20.96] person who kind of kicked off the
[L490] [17:23.12] structured programming.
[L491] [17:25.76] I don't want to call it a revolution.
[L492] [17:26.96] That's a bit too probably grandiose, but
[L493] [17:29.36] kicked off that train of thought. Say uh
[L494] [17:32.08] he wrote a a thing called notes on
[L495] [17:34.88] structured programming. It was a
[L496] [17:35.92] manuscript or monograph. I don't I don't
[L497] [17:38.56] remember what they called, you know, got
[L498] [17:40.16] like a typewritten like it looks like
[L499] [17:41.52] exactly like a typewriter written thing,
[L500] [17:43.92] right? Um he when he wrote that he was
[L501] [17:48.40] like very depressed like he was having a
[L502] [17:51.04] lot of trouble in his life at that time.
[L503] [17:52.80] He had he had gone through this this
[L504] [17:54.72] situation where uh they had done what
[L505] [17:58.00] people today now recognize as like
[L506] [18:00.16] pioneering work in distributed computing
[L507] [18:02.24] like he and these other uh people at the
[L508] [18:05.20] Einhovven Technological University. I
[L509] [18:07.04] don't I apologize I can't say the proper
[L510] [18:09.12] name for it. It's it's you know it's
[L511] [18:11.52] well beyond my pronunciation
[L512] [18:12.96] capabilities. But point being um he had
[L513] [18:15.84] done this really foundational work in uh
[L514] [18:19.44] distributed computing and published it
[L515] [18:21.92] and people today now recognize it as
[L516] [18:24.24] that it is like undisputedly a massive
[L517] [18:26.40] contribution to distributed computing.
[L518] [18:28.24] He did it with a part-time team of
[L519] [18:30.08] people at the university who this wasn't
[L520] [18:31.68] their job. it was a mathematics
[L521] [18:33.36] department they were in and you know as
[L522] [18:36.32] a result of that uh basically they sort
[L523] [18:38.96] of just got dissolved like the the
[L524] [18:40.80] department of mathematics I guess like
[L525] [18:42.08] he wasn't really specific about it but
[L526] [18:43.92] in his notes like the department of
[L527] [18:45.12] maths was just like they disbanded the
[L528] [18:46.72] team he was like this you know this
[L529] [18:47.84] isn't math or whatever I don't know they
[L530] [18:49.44] just had a a pessimist view of it so um
[L531] [18:52.00] and he was really depressed about that
[L532] [18:53.44] and he wasn't sure what he should do
[L533] [18:54.64] with his life and like you know what's
[L534] [18:56.16] what what's the deal here right and he
[L535] [18:57.84] was having this sort of um I don't want
[L536] [18:59.84] to call it an existential crisis because
[L537] [19:01.36] I don't want again put words in his
[L538] [19:03.04] mouth. These are historical figures and
[L539] [19:05.04] you know I can that's why I try to use
[L540] [19:06.64] quotes to try to show you like what they
[L541] [19:08.32] said. Um but like that's it's just so
[L542] [19:12.00] relatable when you go through the
[L543] [19:13.20] history this way. It it's not just some
[L544] [19:15.12] random guy who wrote some math down in a
[L545] [19:17.20] paper. It's like people were really
[L546] [19:18.56] struggling with this and some of the
[L547] [19:21.04] most important aspects of computer
[L548] [19:22.48] history come out of these amazing human
[L549] [19:24.96] stories. And I found that absolutely
[L550] [19:26.56] fascinating. So, I'll just put that out
[L551] [19:29.04] there as one of the biggest rewarding
[L552] [19:31.36] things about looking into this history
[L553] [19:32.96] if you ever do it is if you can go find
[L554] [19:35.20] the actual writings of the people,
[L555] [19:38.56] like things outside of just their
[L556] [19:40.16] technical papers, it's just fascinating
[L557] [19:42.64] and it's so much more relatable and
[L558] [19:46.16] fascinating because you feel the story.
[L559] [19:48.40] It's not just this abstract computation
[L560] [19:50.88] uh computer science thing that happened.
[L561] [19:52.72] So that's one thing.
[L562] [19:54.96] But the other thing I was going to say
[L563] [19:55.92] is like when you read through this
[L564] [19:57.60] stuff, I'm just I just go through piles
[L565] [19:59.44] of documents and I'm just reading them
[L566] [20:00.88] and seeing, you know, does this fit into
[L567] [20:04.00] this story? You know, should it be part
[L568] [20:05.76] of what I'm telling or is it extraneous?
[L569] [20:07.76] Is it something that, you know, uh is
[L570] [20:10.16] interesting perhaps, but not actually
[L571] [20:11.60] part of it? And one thing that I found I
[L572] [20:14.72] when the VOD of this lecture uh or talk
[L573] [20:17.76] goes up I'm going to uh include this in
[L574] [20:20.64] the notes because I thought it was so if
[L575] [20:22.08] it didn't make it into the talk I found
[L576] [20:24.72] a thing
[L577] [20:26.72] uh like a a uh thing from Tony
[L578] [20:30.40] So, so Charles, Anthony, Richard
[L579] [20:32.40] uh, who again is another massive figure
[L580] [20:34.32] in computer science, right? Hora,
[L581] [20:35.76] Dystra, and Canuth are like, you know,
[L582] [20:37.36] the three amigos and like they they all
[L583] [20:39.36] write to each other, right? And they're
[L584] [20:41.36] very important people in computer
[L585] [20:42.40] science history. So, um, I found a thing
[L586] [20:45.52] by him that was like a a thing he did
[L587] [20:49.12] not decide to pursue. It's like this
[L588] [20:51.36] note where he's talking about, you know,
[L589] [20:53.04] he's talking about this thing that he's
[L590] [20:54.56] thinking of doing. And there's just a
[L591] [20:57.04] handwritten thing on him from later on
[L592] [20:58.80] in his life when he was I guess
[L593] [21:00.40] categorizing these documents. And he
[L594] [21:02.32] just writes down like I decided not to
[L595] [21:04.56] pursue this because you know I I talked
[L596] [21:07.12] about it at this conference that I was
[L597] [21:09.28] at and Peter Nauer who's like again
[L598] [21:12.40] another famous figure in computer
[L599] [21:14.24] science history. If you've ever heard
[L600] [21:15.28] the if you ever looked at um like
[L601] [21:16.72] contextfree grammarss and parsing you've
[L602] [21:19.44] probably heard Bakasau form. He's the
[L603] [21:21.92] ner in Bakasnau form. If you ever heard
[L604] [21:23.76] of the language Al Gallal, he was like a
[L605] [21:25.60] major, you know, figure in in
[L606] [21:27.44] standardizing that and writing up the
[L607] [21:28.80] standard and all this stuff, right? So
[L608] [21:31.44] anyway, Horus like yeah, I I proposed
[L609] [21:34.16] this thing. I went through I said it and
[L610] [21:36.16] like and Peter now was like ah making
[L611] [21:38.56] multipass compilers is easy. I I just
[L612] [21:40.80] wrote a nine pass one. So I was you know
[L613] [21:43.28] I decided not to pursue this, right? So
[L614] [21:45.68] what's the thing? I read through the
[L615] [21:47.36] thing and like maybe I'm just
[L616] [21:50.80] overreading it with the benefit of
[L617] [21:54.24] hindsight, but he pretty much describes
[L618] [21:57.36] static single assignment form like like
[L619] [21:59.44] SSA
[L620] [22:00.96] uh which is a very standard compiler
[L621] [22:02.40] technique developed in the 80s but this
[L622] [22:04.40] note is from the 60s. So it's like in my
[L623] [22:07.92] head I'm like did Peter Nau accidentally
[L624] [22:10.72] set back like computer like like
[L625] [22:14.00] compiler science by 20 years by like
[L626] [22:17.20] telling Tony well 15 let's say by
[L627] [22:19.52] telling Tony like this is not
[L628] [22:21.68] important when actually was would have
[L629] [22:24.00] been like very very important. So uh you
[L630] [22:27.04] find stuff like that all the time where
[L631] [22:28.64] you're like whoa what is this? I I saw
[L632] [22:30.56] another one too. Uh just one more I'll
[L633] [22:32.72] mention.
[L634] [22:34.40] Uh I I can't remember now. I'm sorry. Uh
[L635] [22:36.96] again, your brain kind of turns to mush
[L636] [22:38.80] when you try to dump this many documents
[L637] [22:40.56] into it for a talk. Uh uh there was a a
[L638] [22:43.60] pretty interesting thing I thought where
[L639] [22:45.68] uh uh Margaret Hamilton so the the
[L640] [22:48.64] person who you know managed the Apollo
[L641] [22:51.76] she was she was you know one of the core
[L642] [22:53.84] programmers originally on the project
[L643] [22:55.28] and then then was like the man like the
[L644] [22:57.12] manager of the whole OS like the whole
[L645] [22:59.84] like real-time software that ran the
[L646] [23:02.40] Apollo 11 well all the Apollo uh flight
[L647] [23:05.68] computer stuff right
[L648] [23:07.76] which I mean most people today herald is
[L649] [23:10.00] like a very very significant like
[L650] [23:12.16] real-time systems like achievement in
[L651] [23:14.24] that era, right? Like everyone pretty
[L652] [23:15.76] much agrees uh with that
[L653] [23:18.72] she had to write like a defense. I think
[L654] [23:21.52] it was in the AC the communication to
[L655] [23:23.28] the ACM maybe it was in data like they
[L656] [23:24.88] say apologize I can't remember the venue
[L657] [23:28.08] because like it had been pointed out as
[L658] [23:31.44] like a failure because people didn't
[L659] [23:34.08] understand the context that like the
[L660] [23:36.00] reason that the Apollo computer had to
[L661] [23:37.60] like trip those alarms was because that
[L662] [23:39.60] it had been used improperly like it was
[L663] [23:41.36] used in a configuration it wasn't
[L664] [23:42.72] supposed to and it actually rather than
[L665] [23:44.80] crashing went into backup modes and
[L666] [23:47.20] successfully landed like it it worked
[L667] [23:49.36] like it it actually was a triumph of
[L668] [23:51.36] like fault tolerant engineering and she
[L669] [23:53.68] had to write like a defense of this
[L670] [23:54.96] because people at the time were saying
[L671] [23:56.56] like oh that they screwed up like this
[L672] [23:58.08] is an example of of how why you wouldn't
[L673] [24:00.00] want to do engineering this way or like
[L674] [24:01.68] you know don't write the code this way
[L675] [24:03.44] and so um again stuff like that always
[L676] [24:06.88] makes me think like the more things
