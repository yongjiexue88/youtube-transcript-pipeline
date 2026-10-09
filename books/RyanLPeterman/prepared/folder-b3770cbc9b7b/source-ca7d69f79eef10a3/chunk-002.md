Chunk 2; segments 324–650. Start may repeat the previous chunk for context.

# Tech Lead for Meta's Most-Used Programming Language (Promotion Story)

Source ID: source-ca7d69f79eef10a3
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Tech_Lead_for_Meta's_Most-Used_Programming_Language_(Promotion_Story)_en.txt
Video: https://www.youtube.com/watch?v=SbKWawTrsb0

[L333] [12:35.76] traverse that and provide value to us.
[L334] [12:38.32] So that's a big value ad for industry
[L335] [12:40.88] code. Is that right?
[L336] [12:41.84] >> Yeah. And it's actually kind of
[L337] [12:43.76] incredible to think about that you write
[L338] [12:46.48] some text in a file and because you
[L339] [12:48.72] write it in this way that we have
[L340] [12:51.84] developed ways of proving that hey this
[L341] [12:54.80] this text you've written does not
[L342] [12:56.72] exhibit these classes of of errors at
[L343] [12:58.96] all and you could just rely on it and
[L344] [13:01.52] that's really powerful right and it's
[L345] [13:04.16] you know one of the I think main
[L346] [13:06.24] achievements we we've uh had in the
[L347] [13:08.96] space of computer science
[L348] [13:10.72] >> definitely like formally verifying that
[L349] [13:13.20] this bug cannot happen because of those
[L350] [13:16.00] types.
[L351] [13:16.48] >> Exactly.
[L352] [13:17.36] >> In my research and kind of uh you know
[L353] [13:20.16] studying some of the the type
[L354] [13:22.08] migrations. I think you mentioned before
[L355] [13:24.16] like this uncanny valley of type
[L356] [13:26.16] systems. I'm curious can you explain
[L357] [13:28.40] what that phenomenon is and what you
[L358] [13:30.80] mean by uncanny valley?
[L359] [13:32.16] >> I grew up playing video games. So this
[L360] [13:34.08] was a term I learned in that space where
[L361] [13:37.28] from there it's from more like if you
[L362] [13:39.20] have computer graphics as you try to
[L363] [13:41.60] make something look more humanlike in
[L364] [13:43.60] general you feel better about it like
[L365] [13:45.52] you feel more connected to it as it
[L366] [13:47.12] starts to look more human but then it
[L367] [13:48.72] gets to a certain point where it's
[L368] [13:51.04] almost humanlike but it's off in subtle
[L369] [13:53.28] ways and all of a sudden you get kind of
[L370] [13:55.52] put off from it and me being familiar
[L371] [13:58.32] with this term I feel the same thing
[L372] [14:00.48] will happen in terms of as you move from
[L373] [14:04.32] dynamic languages to static languages.
[L374] [14:07.04] And the reason I felt this way is at the
[L375] [14:10.80] time people only worked with dynamic
[L376] [14:12.96] languages that only fully fully
[L377] [14:14.72] statically type languages and did not
[L378] [14:16.96] necessarily have the muscle like memory
[L379] [14:19.76] or like weight trained in their brain.
[L380] [14:22.40] What does it mean if I have a type? It
[L381] [14:24.40] actually is not correct. And as you add
[L382] [14:26.80] more and more of these, the the places
[L383] [14:29.44] where the types actually aren't doing
[L384] [14:31.84] what you would expect in a static
[L385] [14:33.84] language that exists, the more
[L386] [14:35.68] off-putting it will feel. And so that's
[L387] [14:38.40] how I came up with that concept, right,
[L388] [14:40.32] was comparing this to how it applies to
[L389] [14:42.80] the space of graphics, human human
[L390] [14:45.92] graphics, and trying to make a similar
[L391] [14:48.88] analogy to communicate this point. And
[L392] [14:51.20] it proved to be really effective way of
[L393] [14:53.76] uh contextualizing the problem we were
[L394] [14:55.60] trying to solve on the hack team at the
[L395] [14:57.12] time.
[L396] [14:57.68] >> In the process of migrating to a fully
[L397] [15:00.40] statically typed codebase, that last bit
[L398] [15:04.16] actually things start to get worse
[L399] [15:05.68] because you're almost there. And so the
[L400] [15:07.60] the bugs that come are much more subtle
[L401] [15:09.52] and the behaviors are much more subtle
[L402] [15:11.36] and it's actually worse for a bit till
[L403] [15:13.44] 100%.
[L404] [15:14.24] >> Yeah. And I think there's even something
[L405] [15:17.12] particular because we were you know the
[L406] [15:20.56] foundation of the language was PHP was
[L407] [15:22.96] that at the time there were certain
[L408] [15:25.12] behaviors PHP had which were
[L409] [15:28.08] incompatible with trying to make a sound
[L410] [15:30.88] type checker for and there were some
[L411] [15:33.84] questions at the time of like well
[L412] [15:36.24] should we keep those behaviors or should
[L413] [15:38.40] we get rid of them and I think my post
[L414] [15:41.04] was more making a statement we should
[L415] [15:42.80] get rid of those behaviors. Because if
[L416] [15:45.20] you have a language even if you had
[L417] [15:47.04] everything typed the fact that the types
[L418] [15:49.20] can't be relied upon because of these
[L419] [15:51.12] subtle behavioral differences then that
[L420] [15:53.92] will be a problem or will create a less
[L421] [15:56.80] than ideal uh state for development. So
[L422] [16:00.16] I think that's it's also some of it is
[L423] [16:02.24] you know because of PHP and some of the
[L424] [16:05.20] peculiar decisions they made of how
[L425] [16:07.52] their runtime would operate.
[L426] [16:09.36] >> I see I see that makes sense. And so in
[L427] [16:12.56] your time as a IC, I I know eventually
[L428] [16:14.88] you transitioned to management. So you
[L429] [16:16.56] must have had some promotions and things
[L430] [16:18.80] that helped your career grow. Are there
[L431] [16:20.96] any stories like particular times where
[L432] [16:24.24] you felt like okay that was a really
[L433] [16:26.16] good learning experience and helped you
[L434] [16:27.92] grow as an IC?
[L435] [16:29.20] >> Yes, two two of them come to mind. So
[L436] [16:31.92] one was when I got promoted yeah as a
[L437] [16:34.64] senior engineer. I kind of mentioned
[L438] [16:36.64] earlier about this project I worked on
[L439] [16:38.96] of trying to create a hack API for the
[L440] [16:43.12] for the ants framework. So since that
[L441] [16:45.28] went well, I was asked to hey can we do
[L442] [16:48.96] this at a at a larger scale like can we
[L443] [16:52.08] move more code from PHP to hack? And so
[L444] [16:54.48] I ended up spending a a half doing that.
[L445] [16:58.48] And at that time, up to that point, my
[L446] [17:01.28] idea of what value I gave to the company
[L447] [17:04.40] was 100% based off of what code I was
[L448] [17:07.20] able to output. And so when I started
[L449] [17:11.04] this, I was talking to so many people. I
[L450] [17:14.40] was like giving ideas to the hack team,
[L451] [17:17.52] giving ideas to other engineers to work
[L452] [17:19.44] on that I had almost no time to actually
[L453] [17:22.00] write code myself. And because of this,
[L454] [17:24.24] I felt I was having the worst half I
[L455] [17:26.48] ever had at the company. And I remember
[L456] [17:28.56] like having a conversation with my
[L457] [17:29.92] manager about this. And she was like,
[L458] [17:31.44] you know, it's important that, you know,
[L459] [17:33.36] you're doing the right thing in terms of
[L460] [17:35.20] talking to other people and getting them
[L461] [17:36.96] involved, but you should find some time
[L462] [17:38.88] to write some code on your on yourself.
[L463] [17:41.60] And I don't know if she talked to her
[L464] [17:43.12] her her manager afterwards, but like I
[L465] [17:46.40] think the next one, she was like, "Yeah,
[L466] [17:48.24] that thing I told you that's actually
[L467] [17:49.60] wrong." Like keep on focusing on just
[L468] [17:51.60] what the end results were. And for me
[L469] [17:54.48] the thing that really connected still at
[L470] [17:57.20] the end of the half I thought that I was
[L471] [17:59.52] like yeah you know we had some results.
[L472] [18:02.72] Yes we increased the amount of uh hack
[L473] [18:05.68] adoption of or coverage from like I
[L474] [18:08.00] think 20 or 30% of the code base to like
[L475] [18:10.72] 60 or 70%. Now like hack felt like it
[L476] [18:14.64] was a fixture in the company like people
[L477] [18:16.56] weren't really looking to write PHP
[L478] [18:18.48] first. Everyone was starting to write
[L479] [18:20.00] hack first. I felt like I had good
[L480] [18:22.08] results, but again, I wrote the least
[L481] [18:24.64] amount of code in my career so far. So,
[L482] [18:26.40] I wasn't sure how that was going to play
[L483] [18:27.76] out in terms of my performance review.
[L484] [18:29.84] And the thing that really connected was
[L485] [18:31.52] like, oh, actually, that was the highest
[L486] [18:34.56] review I ever got. I ended up getting
[L487] [18:36.08] redefined that half. Um,
[L488] [18:38.00] >> wow.
[L489] [18:38.48] >> And I got promoted to IC5, which I
[L490] [18:40.88] wasn't even in the conversation because
[L491] [18:42.88] I thought, oh, I'm not writing enough
[L492] [18:44.24] code to even justify that. And it really
[L493] [18:46.24] solidified to me that writing code is
[L494] [18:49.20] just is not what my job as a software
[L495] [18:51.28] engineer is. My job is to identify and
[L496] [18:54.24] solve problems. Sometimes that's the
[L497] [18:57.20] best way of doing that is writing code.
[L498] [18:59.28] Sometimes it's me bringing clarity to a
[L499] [19:03.04] problem and a path forward for how to
[L500] [19:04.72] solve it. And if others end up writing
[L501] [19:06.40] the code, then that's fine. Um, so
[L502] [19:08.24] that's something I think was a pretty
[L503] [19:10.40] big mind shift there of experience in of
[L504] [19:12.80] like, okay, I don't have to be the most
[L505] [19:16.16] uh efficient, you know, coded machine
[L506] [19:18.64] out there, right? There's other ways I
[L507] [19:21.04] could add value. So that was definitely
[L508] [19:22.72] one of the one of the pieces. And the
[L509] [19:25.20] second one was also, I guess, what led
[L510] [19:27.76] to my promotion to IC6. So after that
[L511] [19:30.64] half, right, that I just explained, I
[L512] [19:32.80] was asked to join the hack team. So I
[L513] [19:34.48] wasn't even on the hack team at the
[L514] [19:35.76] time. So uh this was uh started in I
[L515] [19:39.60] think 2015 right I joined the team uh
[L516] [19:43.52] they said like hey you would be the tech
[L517] [19:45.20] lead I have no idea what that was and
[L518] [19:48.40] most of the engineers who were on the
[L519] [19:50.48] team before they ended up leaving. So it
[L520] [19:53.28] was like me and other engineer I brought
[L521] [19:56.00] on the team who I worked with before and
[L522] [19:58.24] like a new grad hire and we were like
[L523] [20:00.32] this whole system we were now
[L524] [20:02.32] responsible for. I quickly struggled for
[L525] [20:05.36] a few years trying to understand what
[L526] [20:07.04] was my role as a tech lead. You know, I
[L527] [20:08.96] was comfortable that my output didn't
[L528] [20:10.64] necessarily need to be related to the
[L529] [20:12.40] code I wrote, but I still felt like I
[L530] [20:14.80] was responsible for seeing the outcomes
[L531] [20:16.80] and the end. So, one of the things I
[L532] [20:19.28] worked on was trying to redesign how our
[L533] [20:24.08] collection system work arrays and stuff
[L534] [20:26.72] within hack. And I spent all this work
[L535] [20:28.80] on the design, spent a whole year on it,
[L536] [20:31.20] convinced our runtime team to implement
[L537] [20:33.36] it. Started with the implementation and
[L538] [20:35.84] started to roll in. We had some people
[L539] [20:37.76] join the team and I was like, "All
[L540] [20:39.44] right, here's my, you know, project to
[L541] [20:41.44] get me to IC6 is trying to complete
[L542] [20:43.68] this." And I remember my manager telling
[L543] [20:45.92] me, "Okay, Dwayne, I actually want you
[L544] [20:48.24] to work on something else." And I was
[L545] [20:50.00] really upset because I was like, "What?
[L546] [20:51.92] Why you tell me to work on something
[L547] [20:53.20] else? This is my project is up to speed.
[L548] [20:55.92] Why do you want me to do something
[L549] [20:56.96] else?" and this is my path. And he was
[L550] [20:58.88] saying like and he gave this analogy
[L551] [21:00.80] which is really interesting. It's like
[L552] [21:02.56] think of what you're doing is like
[L553] [21:03.84] you're like a rocket ship and like
[L554] [21:05.68] there's different stages as you are
[L555] [21:07.28] firing and like you know you have the
[L556] [21:08.88] initial set of like engines that are
[L557] [21:11.76] meant to like leave the orbit, right?
[L558] [21:14.40] But once you escape the orbit there's
[L559] [21:16.08] like other jets that can fire and he was
[L560] [21:18.48] like I only cared about you getting us
[L561] [21:20.48] out of orbit. now that we've done that,
[L562] [21:23.04] you should pass this off to someone
[L563] [21:24.48] else. And now you can find something
[L564] [21:26.00] else to do instead. And he wouldn't let
[L565] [21:28.08] me leave the 101 until I agreed to do
[L566] [21:29.92] it. And you know, I passed this on to
[L567] [21:31.92] another engineer. And I was uh I don't
[L568] [21:34.16] even remember what I was focusing on,
[L569] [21:36.56] but I remember, you know, the half
[L570] [21:38.48] ended. And again, I was like, "Okay,
[L571] [21:40.88] well, I did that. So, let's talk about,
[L572] [21:42.96] you know, what my path for six would
[L573] [21:44.72] be." It's like, "Oh, actually, I just
[L574] [21:47.20] got you promoted. So, uh,
[L575] [21:49.12] congratulations. cuz you're now 06. So
[L576] [21:51.52] in both cases, like those promotions
[L577] [21:53.44] were kind of a surprise for me because I
[L578] [21:55.36] had a mismatch between what my
[L579] [21:56.96] expectations in my head of what I needed
[L580] [22:00.24] to do to perform at the next level
[L581] [22:02.32] versus what in reality was important.
[L582] [22:05.36] And each time it felt like being okay
[L583] [22:08.80] with having less direct control on the
[L584] [22:11.36] outcome. And the real important thing I
[L585] [22:14.24] did was just aligning what the right
[L586] [22:16.64] strategy and what the right problems
[L587] [22:18.32] were in the first place.
[L588] [22:20.24] >> A lot of more senior IC's the value is
[L589] [22:22.88] they come in they figure out what's
[L590] [22:25.44] important to solve why you know get all
[L591] [22:28.08] the alignment and now there's this it
[L592] [22:30.40] kind of like the you've left orbit at
[L593] [22:32.24] that point. This is something everyone's
[L594] [22:33.92] interested in. Then you hand it to
[L595] [22:35.36] someone who's great at you know getting
[L596] [22:36.88] it done. And so it and it's cool that
[L597] [22:39.12] your managers were uh proactive and
[L598] [22:43.36] driving your growth because it sounds
[L599] [22:45.60] like you weren't really eagerly involved
[L600] [22:49.12] and figuring out, hey, what do I do to
[L601] [22:51.20] six and you know scale myself? Okay, I'm
[L602] [22:53.52] going to go scale myself. It's almost
[L603] [22:54.88] like you begrudgingly did the things and
[L604] [22:57.60] they were coaching you and you just got
[L605] [22:59.36] promoted as a byproduct.
[L606] [23:00.96] >> Yeah. uh you know it was also a bit
[L607] [23:03.52] earlier at the company so some of it was
[L608] [23:05.52] like probably they were willing to move
[L609] [23:07.60] faster like hey Dwayne we we see the
[L610] [23:09.92] potential in him by like hold the
[L611] [23:11.92] promotion for another half. Having a
[L612] [23:14.16] strong relationship with your manager is
[L613] [23:16.32] the thing I see most consistent in like
[L614] [23:18.32] my career. Whenever I felt disconnect
[L615] [23:20.96] with my manager is when I felt most
[L616] [23:22.72] frustrated. The times when I felt most
[L617] [23:25.76] connected is when I felt I was doing my
[L618] [23:27.52] best work. And I I think I see that that
[L619] [23:29.68] through line in a lot of people's uh
[L620] [23:32.16] careers. Like almost everyone who has
[L621] [23:34.08] had success, they had a good
[L622] [23:35.84] relationship with their manager. Um and
[L623] [23:37.84] so speaking of management, I know you
[L624] [23:40.16] eventually transitioned to, you know,
[L625] [23:42.32] being a manager. Curious, what made you
[L626] [23:44.48] want to try management? What's the story
[L627] [23:46.64] behind you becoming a manager?
[L628] [23:48.08] >> Uh it's interesting because it's kind of
[L629] [23:50.16] kind of similar to how I ended up at
[L630] [23:52.16] Facebook is like I I didn't want to be
[L631] [23:54.00] manager. It was not a part of my career
[L632] [23:56.08] plans. The team was at this point
[L633] [23:58.24] growing rapidly and you know my manager
[L634] [24:02.24] at the time he was like hey we need more
[L635] [24:04.88] managers on the team just because of the
[L636] [24:06.64] growth rate. Here's an opportunity for
[L637] [24:08.48] you and we could either try and find
[L638] [24:10.00] another manager externally or you can
[L639] [24:11.76] give this a shot. And I said no. And the
[L640] [24:15.36] next time I met him I heard about the
[L641] [24:18.32] TLM role like tech lead manager and I
[L642] [24:20.88] was like oh yeah I could do some coding
[L643] [24:22.80] and maybe a little management. This
[L644] [24:24.16] might be a nice transition. And I
[L645] [24:25.60] mentioned it to my manager and he was
[L646] [24:27.44] like, "Oh, you don't want to do this. I
[L647] [24:28.72] was a TLM at another company. It's like
[L648] [24:30.80] you're doing two jobs.
[L649] [24:32.96] I wouldn't recommend this as a manager."
[L650] [24:34.64] So I was like, "Okay, that's fine. I
[L651] [24:36.40] won't be a manager." And I think he
[L652] [24:38.24] probably talked to my director because
[L653] [24:40.40] he came back the next 101. He was like,
[L654] [24:42.16] "Actually, yeah, we should we should try
[L655] [24:44.08] this. You could, you know, be a TLM or
[L656] [24:46.48] whatever you want. You know, just try
[L657] [24:47.92] this management thing." And since I, you
[L658] [24:50.56] know, was starting to get more
[L659] [24:52.08] comfortable with like delegating and I
