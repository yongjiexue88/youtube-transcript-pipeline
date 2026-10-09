Chunk 2; segments 353–714. Start may repeat the previous chunk for context.

# Harvard Professor: CS50, What Matters More Than Programming Now, Lecturing Well | David J Malan

Source ID: source-f55dd5f460ec58d2
Original: /Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman/Harvard_Professor_CS50,_What_Matters_More_Than_Programming_Now,_Lecturing_Well_David_J_Malan_en.txt
Video: https://www.youtube.com/watch?v=bB2o81DnKHk

[L362] [11:37.96] algorithms, we very often have a student
[L363] [11:40.08] come up on stage, for instance. And for
[L364] [11:41.32] sorting or for searching, we have a
[L365] [11:42.96] whole bunch of like gym lockers, small
[L366] [11:44.56] versions thereof, that we put numbers
[L367] [11:46.48] in, either on printed paper or little
[L368] [11:47.88] plastic numbers. And the goal is to have
[L369] [11:49.64] a student like find the number 50 or
[L370] [11:51.96] some other number that we've hidden
[L371] [11:53.36] behind the doors. And it's an
[L372] [11:54.40] opportunity just to talk about either
[L373] [11:56.44] searching the doors linearly, left to
[L374] [11:57.76] right, right to left, maybe you randomly
[L375] [12:00.16] maybe more methodically as by a binary
[L376] [12:02.36] search if the numbers are sorted. That
[L377] [12:04.76] then leads us to opportunities to talk
[L378] [12:06.40] about bubble sort and selection sort and
[L379] [12:08.52] insertion sort. Algorithms that you
[L380] [12:10.28] probably wouldn't bother implementing or
[L381] [12:11.96] using in the wild cuz there's more
[L382] [12:13.56] performant ones, certainly. But we use
[L383] [12:15.56] them as these pedagogical tools to
[L384] [12:17.40] explore the the problem to be solved,
[L385] [12:19.24] which is, all right, I can only use
[L386] [12:20.40] binary search if the data is sorted. So,
[L387] [12:22.68] how do I sort it? And how expensive is
[L388] [12:24.56] that going to be to make worthwhile the
[L389] [12:26.48] whole process in the get-go? And so,
[L390] [12:28.20] we'll have uh eight students come up on
[L391] [12:30.52] stage and sort themselves physically and
[L392] [12:33.04] really perform in certain ways. And
[L393] [12:35.00] there's so many examples of that through
[L394] [12:36.64] CS 50. We try to do at least one such
[L395] [12:39.00] thing every class. I mean, not unlike
[L396] [12:41.40] the way John Oliver, for instance, ends
[L397] [12:43.52] Last Week Tonight. We're trying to do
[L398] [12:44.80] some big song and dance, which
[L399] [12:46.08] ironically is always at the end as the
[L400] [12:47.68] hook. We do try to put it maybe toward
[L401] [12:49.40] the beginning of lecture or in the
[L402] [12:50.72] middle. But that's not just for
[L403] [12:52.60] engagement and not to
[L404] [12:54.80] make to keep folks' attention, but
[L405] [12:57.52] really to latch onto their memories. So,
[L406] [13:00.08] that even if you're in the weeds of this
[L407] [13:02.24] introductory computer science course,
[L408] [13:03.72] there's so much new information, it's
[L409] [13:05.12] the proverbial fire hose hitting you in
[L410] [13:06.68] the face,
[L411] [13:07.76] you can cling to, okay, all right, I
[L412] [13:09.32] remember like my my roommate was
[L413] [13:11.16] literally the one on stage acting out
[L414] [13:13.00] bubble sort. And you can kind of picture
[L415] [13:14.52] in your mind's eye what was happening.
[L416] [13:17.04] Or that phone book example is a perfect
[L417] [13:18.80] one that years after leaving Harvard, we
[L418] [13:21.00] have alumni coming up to us and saying,
[L419] [13:22.92] oh, I still remember the phone book
[L420] [13:24.24] demo. And those memorable moments,
[L421] [13:26.64] ideally theatrical in nature, I think
[L422] [13:29.16] are what brings material, whether it's
[L423] [13:30.52] CS or something else, to life. But that
[L424] [13:32.52] is very much to engage any learner,
[L425] [13:35.88] present or remote, um as opposed to
[L426] [13:38.44] being optimized for some technology.
[L427] [13:41.00] >> One thing that I I wonder cuz computer
[L428] [13:43.76] science is such a dense topic where I
[L429] [13:47.44] guess there could be a trade-off with
[L430] [13:49.92] Yeah, imagine another style of lecture
[L431] [13:52.12] is uh you know, there's a chalkboard and
[L432] [13:54.84] you're up there kind of blandly writing
[L433] [13:57.28] out all of the information. I I could
[L434] [14:00.16] imagine you could go through much more
[L435] [14:03.16] depth in that case. Do you feel like
[L436] [14:05.20] there's any trade-off there?
[L437] [14:07.56] >> Absolutely. I mean, this is a criticism
[L438] [14:09.36] we get from some students, particularly
[L439] [14:11.32] those with prior background or among
[L440] [14:13.08] those more comfortable, where do we
[L441] [14:14.96] really need 10 minutes on linear search
[L442] [14:17.32] or, you know, another 15 minutes on
[L443] [14:18.88] binary search? And the answer is quite
[L444] [14:20.28] clearly no for those students. And even
[L445] [14:22.12] for most students, I would say we do
[L446] [14:24.76] spend a disproportionate amount of time
[L447] [14:28.04] on certain cherry-picked topics that we
[L448] [14:30.04] do think lend themselves to this
[L449] [14:31.44] theatricality
[L450] [14:33.00] for really getting students interested
[L451] [14:36.00] in fundamentally and excited by the
[L452] [14:38.08] material to help motivate them the rest
[L453] [14:40.24] of the week when they're going to be
[L454] [14:41.08] spending 5, 10, 15, 20 plus hours on
[L455] [14:43.92] some week's assignment and to help them
[L456] [14:45.72] see sort of the forest for the trees.
[L457] [14:47.28] Like, what is actually important and
[L458] [14:48.80] meaningful and fun about this? Because
[L459] [14:50.68] it's probably not the keystrokes and the
[L460] [14:52.16] debugging and the lower-level
[L461] [14:53.72] implementation details. So, we talk
[L462] [14:55.96] about this actually in a paper in a talk
[L463] [14:57.32] we we gave at a CS education conference
[L464] [14:59.96] a few years back trying to find that
[L465] [15:02.12] balance between the theatricality and
[L466] [15:04.64] the density of material. But to your
[L467] [15:07.80] question about dryness, I mean, I would
[L468] [15:09.64] like to think that dryness really has no
[L469] [15:11.60] place in most forms of education
[L470] [15:14.16] because, you know, then it could have
[L471] [15:15.36] been a book or it could have been an
[L472] [15:16.64] email. Like, if it's just someone
[L473] [15:18.00] reciting words or worse, writing things
[L474] [15:20.60] down in ways that aren't at all
[L475] [15:22.68] interactive. Like, do we really need to
[L476] [15:24.52] be all in this room together? Like, that
[L477] [15:27.24] doesn't seem like the best design to me.
[L478] [15:31.04] >> In my research and looking at the
[L479] [15:32.92] reception of CS50 and people's
[L480] [15:34.92] perspective on how you are as an
[L481] [15:37.52] educator, they absolutely love your
[L482] [15:40.68] energy and like your delivery.
[L483] [15:43.04] Do you rehearse that or is that
[L484] [15:44.72] something that you always had as an
[L485] [15:46.40] educator?
[L486] [15:47.48] >> Yeah, I think it's just the sort of
[L487] [15:48.76] expression. You got to bring your A-game
[L488] [15:50.08] when you get up onto stage. And I think
[L489] [15:51.64] a lot of it honestly comes from a place
[L490] [15:52.92] of insecurity. Like, I really don't want
[L491] [15:54.84] to be the one on stage in front of a
[L492] [15:56.64] bored audience. Like, no one wants to be
[L493] [15:59.36] in that situation. And so I think a lot
[L494] [16:01.60] of the energy that I try to bring to
[L495] [16:03.32] bear and the excitement I show is really
[L496] [16:06.32] meant to one, make sure people want to
[L497] [16:08.24] be and stay there for the duration of
[L498] [16:09.96] the class, whether it's short or long,
[L499] [16:11.64] and also help them see
[L500] [16:14.36] the excitement in and the possibilities
[L501] [16:16.72] of and the applicability of a field that
[L502] [16:18.56] I myself had fell in love with so many
[L503] [16:20.72] years ago.
[L504] [16:22.00] Um, because then they can decide for
[L505] [16:23.36] themselves if they feel that same
[L506] [16:24.80] emotion, if they too look forward to
[L507] [16:26.48] going home to their dorm or their home
[L508] [16:27.92] on Friday nights and working on
[L509] [16:29.84] programming assignments of all things.
[L510] [16:31.72] But, I feel like we certainly owe them,
[L511] [16:34.20] and I think teachers owe students more
[L512] [16:35.72] generally educationally, the opportunity
[L513] [16:38.36] to make that decision for themselves and
[L514] [16:39.84] to
[L515] [16:40.76] put uh forward our best foot or to
[L516] [16:44.00] present the field in the most
[L517] [16:46.36] exciting and inspiring way that we can,
[L518] [16:49.48] if indeed we think it's important that
[L519] [16:51.04] other people after us study and research
[L520] [16:54.00] and apply these fields.
[L521] [16:56.08] >> I noticed this uh dichotomy in education
[L522] [16:59.76] when I was going to UCLA, which was
[L523] [17:02.16] there were roughly two types of
[L524] [17:04.60] professors that I had. There was one
[L525] [17:06.92] type of professor that was beloved by
[L526] [17:09.48] the students and really passionate at
[L527] [17:12.00] educating and kind of involved. And then
[L528] [17:14.16] there's this other type of professor,
[L529] [17:15.56] which was really they might have been
[L530] [17:18.20] really incredible and impressive as
[L531] [17:20.68] researchers,
[L532] [17:22.08] but their classes were really
[L533] [17:25.12] uh poorly rated by all the students. And
[L534] [17:27.76] with the online education that we can do
[L535] [17:30.16] today, I mean like CS50, all the
[L536] [17:31.48] resources are available. I could imagine
[L537] [17:34.00] that objectively we could take the
[L538] [17:36.04] people who are most passionate about
[L539] [17:37.84] teaching and give it to everyone rather
[L540] [17:41.12] than having some teachers that are not
[L541] [17:42.60] excited. Kind of consolidate Take
[L542] [17:44.80] Imagine taking the world's best
[L543] [17:46.28] instructor and giving that to everyone.
[L544] [17:49.00] Why doesn't consolidation happen if we
[L545] [17:51.56] have all the technology for spreading
[L546] [17:54.00] literally the world's best resources to
[L547] [17:56.48] every situation?
[L548] [17:57.56] >> Yeah, that's a good question since I
[L549] [17:59.92] think our own goal is certainly not to
[L550] [18:02.20] put out of business other educators,
[L551] [18:04.36] other classes. However, as a computer
[L552] [18:06.04] scientist, I would be among the first to
[L553] [18:08.68] notice that there's a huge inefficiency
[L554] [18:11.88] in the way education broadly works, not
[L555] [18:14.12] only in this country, but presumably um
[L556] [18:15.88] internationally as well, whereby you
[L557] [18:17.44] have hundreds, thousands of teachers
[L558] [18:19.36] essentially all doing the same thing in
[L559] [18:21.08] parallel and not necessarily the
[L560] [18:22.60] meaningful part of interacting with and
[L561] [18:24.40] uplifting and mentoring students, but
[L562] [18:26.44] like preparing their their presentations
[L563] [18:28.88] or their lecture notes or writing the
[L564] [18:30.84] assignments or grading that work.
[L565] [18:32.68] There's so much meta work involved in
[L566] [18:35.32] education that probably doesn't need to
[L567] [18:37.08] be borne by so many people that the
[L568] [18:39.40] computer scientist in me like invariably
[L569] [18:40.88] wants to factor that out somehow. And so
[L570] [18:42.76] I absolutely think that we educationally
[L571] [18:45.56] as universities, as schools should be
[L572] [18:47.76] leaning on each other much more. Um I'd
[L573] [18:50.72] like to think that's a lot of what
[L574] [18:51.80] drives us in terms of CS50's own mission
[L575] [18:54.32] and the work that we do, but we too have
[L576] [18:56.12] encountered frictions along the way. Um
[L577] [18:58.28] it was very unusual for instance for 10
[L578] [19:00.68] years that we were collaborating with
[L579] [19:01.80] our friends down the road in New Haven
[L580] [19:03.08] at Yale University where we were
[L581] [19:04.44] offering CS50
[L582] [19:06.20] on both campuses in parallel. And more
[L583] [19:07.72] recently we've been doing this um with
[L584] [19:09.64] some of our friends at Oxford in the
[L585] [19:10.92] lifelong learning group there. This is
[L586] [19:12.76] very much still the exception to the
[L587] [19:14.36] rule. Unfortunately, even after
[L588] [19:17.12] 10 plus years of MOOCs, massive open
[L589] [19:19.40] online courses,
[L590] [19:21.16] I dare say a lot of institutions, a lot
[L591] [19:23.32] of faculty are very set in their ways.
[L592] [19:25.28] In fact, one of my regrets of the COVID
[L593] [19:27.08] era were that we was that we had this
[L594] [19:29.36] unpresed opportunity now and almost
[L595] [19:31.64] mandate to move everything online and we
[L596] [19:34.04] therefore had this opportunity to say,
[L597] [19:35.80] "Hey, to Harvard students, why don't you
[L598] [19:37.20] take this Stanford course or this UCLA
[L599] [19:39.04] course or this Yale course or this MIT
[L600] [19:40.84] course that you couldn't necessarily
[L601] [19:42.64] take in person
[L602] [19:44.64] uh for lack of transport or for lack of
[L603] [19:46.48] safety at the time. And I could get no
[L604] [19:49.12] one on campus to to get on board with
[L605] [19:52.72] this idea of maybe offering one computer
[L606] [19:55.08] science course on this campus and let
[L607] [19:57.00] the other students take it. Then you
[L608] [19:58.32] offer, as we did it yeah, like a digital
[L609] [20:00.32] humanities class on some other campus
[L610] [20:01.80] and let the Harvard students take it.
[L611] [20:03.16] And there's just not much of an
[L612] [20:04.56] appetite, I dare say in higher education
[L613] [20:06.80] if not education at large, for that
[L614] [20:09.28] resource sharing. And I think there
[L615] [20:10.68] should be. Um I don't think there should
[L616] [20:12.28] be one computer science course,
[L617] [20:14.00] introductory course. I think some
[L618] [20:16.52] healthy competition is a good thing. I
[L619] [20:18.88] don't think there need to be thousands,
[L620] [20:20.52] probably not hundreds, maybe dozens from
[L621] [20:23.28] some of the best teachers, the best
[L622] [20:25.08] schools um would probably benefit us all
[L623] [20:28.76] if those same teachers then were not put
[L624] [20:30.64] out of work, but then could lean on each
[L625] [20:32.48] other, use some of the materials we've
[L626] [20:34.36] created, adopt or as we say adapt some
[L627] [20:36.16] of our own resources and treat education
[L628] [20:38.00] as a buffet of educational materials
[L629] [20:39.92] that you can then make your own without
[L630] [20:41.64] having to do so much of the same legwork
[L631] [20:43.72] and reinventing wheels across
[L632] [20:45.92] school and state lines.
[L633] [20:48.28] >> The mindset that you said, the the
[L634] [20:50.00] computer scientist mindset of getting
[L635] [20:51.96] rid of the redundancies and kind of um
[L636] [20:54.60] consolidating resources, I mean, it's
[L637] [20:57.16] immediately logically obvious to me, but
[L638] [21:00.48] um what would like let's say there's
[L639] [21:02.48] there's three top courses in America.
[L640] [21:04.92] There's like MIT's, there's
[L641] [21:07.64] Stanford's, and there's Harvard's, and
[L642] [21:10.48] you know, they want to give that to
[L643] [21:13.40] other institutions like I don't know,
[L644] [21:16.44] other other colleges.
[L645] [21:18.44] What would What would stop those
[L646] [21:20.16] colleges from taking an objectively
[L647] [21:22.08] better set of resources and giving that
[L648] [21:24.24] to their students?
[L649] [21:26.24] >> I sense, but I would defer to others who
[L650] [21:28.64] who hold these views that there is a
[L651] [21:31.32] concern that maybe we are putting
[L652] [21:33.20] ourselves out of business or there's
[L653] [21:34.64] more of a a school pride and Did I
[L654] [21:36.44] definitely saw some of that on Harvard's
[L655] [21:38.20] own campus where like, "No, no, no, no.
[L656] [21:40.00] We like we should be offering courses to
[L657] [21:42.80] our students that we have created and
[L658] [21:44.96] that we are teaching and not lean for
[L659] [21:46.76] instance on our friends down the road at
[L660] [21:47.96] MIT who have and have for decades had a
[L661] [21:50.44] larger, richer course catalog than us
[L662] [21:52.36] simply by nature of being a bigger place
[L663] [21:54.60] at least for computer science and it
[L664] [21:56.16] seems silly to me not to lean on each
[L665] [21:58.60] other. Maybe each of us can specialize a
[L666] [22:00.52] bit more. Maybe each of us can offer
[L667] [22:02.40] slightly different modes of of
[L668] [22:04.16] instruction for students. Maybe that's a
[L669] [22:05.84] little more intimate on this campus
[L670] [22:07.24] versus that so as to really leverage
[L671] [22:10.36] shared resources. I mean, this is done
[L672] [22:11.92] endlessly in research having
[L673] [22:13.36] cross-campus collaborations.
[L674] [22:15.76] And there's something very personal
[L675] [22:18.60] about or very
[L676] [22:21.12] fundamentally threatening, I think,
[L677] [22:23.36] about leaning on each other
[L678] [22:25.28] educationally and I wish people would
[L679] [22:27.36] move away from this mindset because it
[L680] [22:29.20] doesn't mean some failure of the
[L681] [22:30.92] institution to offer these courses. It
[L682] [22:32.64] means we can do a better job offering
[L683] [22:34.44] what resources we do have, I would like
[L684] [22:36.40] to think.
[L685] [22:38.12] >> In designing the curriculum for CS50,
[L686] [22:40.80] how did you pick C for instance? Because
[L687] [22:43.48] I think a lot of people would look at
[L688] [22:44.68] that decision and think
[L689] [22:46.56] I'm not going to use C in my day-to-day
[L690] [22:48.96] full stack job. So, why do I need to
[L691] [22:50.64] learn this?
[L692] [22:51.56] >> Sure. Um so, it was not picked by me per
[L693] [22:54.60] se, but I chose to keep C in the course
[L694] [22:57.00] certainly since as far back as 1996 when
[L695] [22:59.32] Brian was teaching it, Professor Margo
[L696] [23:01.20] Seltzer before that, and many other
[L697] [23:03.40] faculty prior to me and them. Um
[L698] [23:07.12] it is
[L699] [23:08.60] a wonderful foundation on which to build
[L700] [23:11.60] your understanding of how a computer
[L701] [23:13.32] works and how software is built. It's
[L702] [23:15.68] about as close as you can get to the
[L703] [23:17.20] hardware before things devolve, at least
[L704] [23:20.52] aesthetically, into assembly code, which
[L705] [23:22.24] is much scarier looking code, I think,
[L706] [23:23.68] for most people, almost everyone,
[L707] [23:25.56] perhaps. Um and certainly uh beyond that
[L708] [23:28.48] is zeros and ones, which is not going to
[L709] [23:30.40] be fun for anyone. Um so C kind of
[L710] [23:32.52] strikes, I think, pedagogically this
[L711] [23:34.28] really nice balance of having
[L712] [23:35.76] English-like syntax and abstractions on
[L713] [23:38.12] top of lower-level primitives that allow
[L714] [23:41.56] you to explore procedural programming,
[L715] [23:44.60] uh in particular, with some fundament
[L716] [23:47.40] constructs that are now fundamental to
[L717] [23:48.92] those kinds of languages, loops and
[L718] [23:50.44] conditions and functions and variables
[L719] [23:52.08] and return values and so forth. It sort
[L720] [23:53.52] of got It's got everything, but it's
[L721] [23:55.28] also a pretty small language, and unless
[L722] [23:57.52] you download third-party stuff, there's
[L723] [23:59.48] not a very large standard library, in
